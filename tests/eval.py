#!/usr/bin/env python3
"""
LLM-as-judge evaluation pipeline for investment analysis skills.

Loads test cases from test_matrix.yaml, runs each through the selected model
provider (OpenAI or Anthropic) with the appropriate skill context, then
evaluates the output against the skill's quality checklist.
"""

import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"
TESTS_DIR = REPO_ROOT / "tests"
REPORTS_DIR = TESTS_DIR / "reports"

ASSET_CLASS_FILES = {
    "public-equities": "public-equities.md",
    "real-estate": "real-estate.md",
    "private-equity": "private-equity.md",
}

PROVIDER = os.environ.get("EVAL_PROVIDER", "openai").lower()
MODEL = os.environ.get(
    "EVAL_MODEL",
    "gpt-4.1-mini" if PROVIDER == "openai" else "claude-sonnet-4-20250514",
)
JUDGE_MODEL = os.environ.get(
    "EVAL_JUDGE_MODEL",
    "gpt-4.1-mini" if PROVIDER == "openai" else "claude-sonnet-4-20250514",
)
MAX_TOKENS = int(os.environ.get("EVAL_MAX_TOKENS", "4096"))
JUDGE_MAX_TOKENS = int(os.environ.get("EVAL_JUDGE_MAX_TOKENS", "2048"))
MAX_RETRIES = 5
BASE_DELAY = 2.0


def _load_env_var_from_dotenv(var_name: str) -> Optional[str]:
    env_path = REPO_ROOT / ".env"
    if not env_path.exists():
        return None
    for line in env_path.read_text().splitlines():
        if line.startswith(f"{var_name}="):
            return line.split("=", 1)[1].strip()
    return None


def _build_client() -> Any:
    if PROVIDER == "openai":
        from openai import OpenAI

        api_key = os.environ.get("OPENAI_API_KEY") or _load_env_var_from_dotenv("OPENAI_API_KEY")
        if not api_key:
            print("ERROR: OPENAI_API_KEY not found in environment or .env")
            sys.exit(1)
        return OpenAI(api_key=api_key)

    if PROVIDER == "anthropic":
        import anthropic

        api_key = os.environ.get("ANTHROPIC_API_KEY") or _load_env_var_from_dotenv("ANTHROPIC_API_KEY")
        if not api_key:
            print("ERROR: ANTHROPIC_API_KEY not found in environment or .env")
            sys.exit(1)
        return anthropic.Anthropic(api_key=api_key)

    print("ERROR: Unsupported EVAL_PROVIDER. Use 'openai' or 'anthropic'.")
    sys.exit(1)


def _retryable_status_code(provider: str, exc: Exception) -> Optional[int]:
    status = getattr(exc, "status_code", None)
    if status in (429, 500, 502, 503, 504, 529):
        return status
    if provider == "anthropic" and exc.__class__.__name__ == "OverloadedError":
        return 529
    return None


def _api_call_with_retry(fn, label: str = "API call"):
    for attempt in range(MAX_RETRIES):
        try:
            return fn()
        except Exception as e:  # noqa: BLE001
            retry_status = _retryable_status_code(PROVIDER, e)
            if retry_status is not None:
                delay = BASE_DELAY * (2 ** attempt)
                print(
                    f" [{retry_status}, retry {attempt + 1}/{MAX_RETRIES}, wait {delay:.0f}s]",
                    end="",
                    flush=True,
                )
                time.sleep(delay)
            else:
                raise
    print(f" FAILED after {MAX_RETRIES} retries")
    raise RuntimeError(f"{label} failed after {MAX_RETRIES} retries")


def load_skill_context(skill: str, asset_class: str) -> str:
    skill_md = (SKILLS_DIR / skill / "SKILL.md").read_text()

    ref_file = ASSET_CLASS_FILES.get(asset_class)
    if ref_file:
        ref_path = SKILLS_DIR / skill / "references" / ref_file
        if ref_path.exists():
            ref_content = ref_path.read_text()
            return f"{skill_md}\n\n---\n\n# Asset-Class Reference\n\n{ref_content}"

    if asset_class in ("multi-asset", "ambiguous"):
        refs = []
        for name, filename in ASSET_CLASS_FILES.items():
            ref_path = SKILLS_DIR / skill / "references" / filename
            if ref_path.exists():
                refs.append(f"# {name}\n\n{ref_path.read_text()}")
        if refs:
            return f"{skill_md}\n\n---\n\n# Asset-Class References (all)\n\n{'---'.join(refs)}"

    return skill_md


def _extract_openai_text(content: Any) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        parts = []
        for chunk in content:
            text = getattr(chunk, "text", None)
            if text:
                parts.append(text)
        return "\n".join(parts).strip()
    return str(content)


def run_skill(client: Any, skill_context: str, prompt: str, *, max_tokens: int) -> str:
    if PROVIDER == "openai":
        response = _api_call_with_retry(
            lambda: client.chat.completions.create(
                model=MODEL,
                max_tokens=max_tokens,
                messages=[
                    {"role": "system", "content": skill_context},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.2,
            ),
            label="skill generation",
        )
        return _extract_openai_text(response.choices[0].message.content)

    response = _api_call_with_retry(
        lambda: client.messages.create(
            model=MODEL,
            max_tokens=max_tokens,
            system=skill_context,
            messages=[{"role": "user", "content": prompt}],
        ),
        label="skill generation",
    )
    return response.content[0].text


JUDGE_SYSTEM = """You are an expert evaluator of investment analysis output.
You will receive:
1. The output produced by an AI skill
2. A quality checklist the output should satisfy
3. Common pitfalls the output should avoid

Evaluate the output against EACH checklist item. Be rigorous but fair.

STRICT SCORING RULES:
- If a checklist item specifies a minimum quantity (e.g., "at least 15 questions")
  and the output falls short, score it "fail" — not "partial."
- If a checklist item requires a specific output section (e.g., "sensitivity table",
  "monitoring framework", "break-even assumptions", "decision triggers") and that
  section is completely absent from the output, score it "fail" — not "partial."
  A "partial" score applies only when the section exists but is incomplete.
- If a checklist item requires identifying disagreements/contradictions and the
  output presents only confirming signals with no discussion of tensions or
  dislocations, score it "fail" unless the output explicitly addresses why no
  disagreement exists with supporting evidence.

Respond with ONLY valid JSON matching this schema:

{
  "checklist_scores": [
    {
      "item": "the checklist item text",
      "score": "pass" | "partial" | "fail",
      "note": "1-sentence explanation"
    }
  ],
  "pitfall_flags": [
    {
      "pitfall": "description of pitfall detected",
      "severity": "minor" | "major"
    }
  ],
  "overall_quality": "strong" | "acceptable" | "needs_work" | "poor",
  "summary": "2-3 sentence overall assessment"
}"""


def extract_section(text: str, heading: str) -> str:
    pattern = rf"## {re.escape(heading)}\b.*?\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, text, re.DOTALL)
    return match.group(1).strip() if match else ""


def get_common_pitfalls(skill_md: str) -> str:
    return extract_section(skill_md, "Common Pitfalls") or "No common pitfalls section found."


def judge_output(
    client: Any,
    output: str,
    checklist: List[str],
    pitfalls: str,
) -> dict:
    user_msg = f"""## Skill Output

{output}

## Quality Checklist

Evaluate each item:
{chr(10).join(f'- {item}' for item in checklist)}

## Common Pitfalls to Check For

{pitfalls}"""

    if PROVIDER == "openai":
        response = _api_call_with_retry(
            lambda: client.chat.completions.create(
                model=JUDGE_MODEL,
                max_tokens=JUDGE_MAX_TOKENS,
                messages=[
                    {"role": "system", "content": JUDGE_SYSTEM},
                    {"role": "user", "content": user_msg},
                ],
                temperature=0,
                response_format={"type": "json_object"},
            ),
            label="judge evaluation",
        )
        text = _extract_openai_text(response.choices[0].message.content)
    else:
        response = _api_call_with_retry(
            lambda: client.messages.create(
                model=JUDGE_MODEL,
                max_tokens=JUDGE_MAX_TOKENS,
                system=JUDGE_SYSTEM,
                messages=[{"role": "user", "content": user_msg}],
            ),
            label="judge evaluation",
        )
        text = response.content[0].text
    json_match = re.search(r"\{.*\}", text, re.DOTALL)
    if json_match:
        return json.loads(json_match.group())
    return {"error": "Failed to parse judge response", "raw": text[:500]}


def score_summary(scores: List[Dict]) -> Tuple[int, int, int]:
    p = sum(1 for s in scores if s.get("score") == "pass")
    par = sum(1 for s in scores if s.get("score") == "partial")
    f = sum(1 for s in scores if s.get("score") == "fail")
    return p, par, f


def _safe_filename(s: str) -> str:
    return re.sub(r"[^a-zA-Z0-9_.-]+", "_", s).strip("_")


def run_pipeline(
    test_cases: List[Dict],
    max_cases: Optional[int] = None,
    *,
    save_outputs: bool = False,
) -> List[Dict]:
    client = _build_client()

    if max_cases:
        test_cases = test_cases[:max_cases]

    results = []
    total = len(test_cases)

    outputs_dir = REPORTS_DIR / "outputs"
    if save_outputs:
        outputs_dir.mkdir(parents=True, exist_ok=True)

    for i, tc in enumerate(test_cases, 1):
        skill = tc["skill"]
        asset_class = tc["asset_class"]
        prompt = tc["prompt"]
        checklist = tc["checklist"]
        label = f"{skill} / {asset_class}"

        print(f"\n[{i}/{total}] {label}")
        print(f"  Generating output...", end="", flush=True)

        skill_context = load_skill_context(skill, asset_class)
        pitfalls = get_common_pitfalls(
            (SKILLS_DIR / skill / "SKILL.md").read_text()
        )

        t0 = time.time()
        # Some skills (e.g., cio-qa-prep) are naturally longer; avoid false fails from truncation.
        gen_max_tokens = MAX_TOKENS
        if skill == "cio-qa-prep":
            gen_max_tokens = max(gen_max_tokens, 8192)

        output = run_skill(client, skill_context, prompt, max_tokens=gen_max_tokens)
        gen_time = time.time() - t0
        print(f" done ({gen_time:.1f}s, {len(output)} chars, max_tokens={gen_max_tokens})")

        print(f"  Evaluating...", end="", flush=True)
        t0 = time.time()
        evaluation = judge_output(client, output, checklist, pitfalls)
        eval_time = time.time() - t0
        print(f" done ({eval_time:.1f}s)")

        scores = evaluation.get("checklist_scores", [])
        p, par, f = score_summary(scores)
        quality = evaluation.get("overall_quality", "unknown")
        print(f"  Result: {p} pass / {par} partial / {f} fail — {quality}")

        if save_outputs:
            out_path = outputs_dir / f"{_safe_filename(skill)}__{_safe_filename(asset_class)}.md"
            out_path.write_text(output)

        results.append({
            "skill": skill,
            "asset_class": asset_class,
            "prompt": prompt.strip()[:100] + "...",
            "output_length": len(output),
            "generation_time": round(gen_time, 1),
            "evaluation": evaluation,
            "pass": p,
            "partial": par,
            "fail": f,
            "overall_quality": quality,
        })

    return results


def generate_report(results: List[Dict]) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    lines = [
        f"# Evaluation Report — {timestamp}",
        "",
        f"**Provider**: {PROVIDER} | **Model**: {MODEL} | **Judge**: {JUDGE_MODEL} | **Cases**: {len(results)}",
        "",
        "## Summary Matrix",
        "",
        "| Skill | Asset Class | Pass | Partial | Fail | Quality |",
        "|-------|------------|------|---------|------|---------|",
    ]

    for r in results:
        lines.append(
            f"| {r['skill']} | {r['asset_class']} | {r['pass']} | "
            f"{r['partial']} | {r['fail']} | {r['overall_quality']} |"
        )

    total_p = sum(r["pass"] for r in results)
    total_par = sum(r["partial"] for r in results)
    total_f = sum(r["fail"] for r in results)
    total_items = total_p + total_par + total_f
    pass_rate = (total_p / total_items * 100) if total_items else 0

    lines += [
        "",
        f"**Overall**: {total_p}/{total_items} pass ({pass_rate:.0f}%), "
        f"{total_par} partial, {total_f} fail",
        "",
    ]

    failures = [
        r for r in results
        if r["fail"] > 0 or r["overall_quality"] in ("needs_work", "poor")
    ]
    if failures:
        lines += ["## Items Needing Attention", ""]
        for r in failures:
            lines.append(f"### {r['skill']} / {r['asset_class']}")
            lines.append("")
            ev = r["evaluation"]
            for s in ev.get("checklist_scores", []):
                if s.get("score") in ("fail", "partial"):
                    icon = "X" if s["score"] == "fail" else "~"
                    lines.append(f"- [{icon}] **{s['item']}**: {s.get('note', '')}")
            for pf in ev.get("pitfall_flags", []):
                lines.append(f"- [!] Pitfall ({pf['severity']}): {pf['pitfall']}")
            summary = ev.get("summary", "")
            if summary:
                lines.append(f"\n> {summary}")
            lines.append("")
    else:
        lines += ["## All test cases passed or acceptable.", ""]

    skill_scores = {}
    for r in results:
        skill_scores.setdefault(r["skill"], {"p": 0, "par": 0, "f": 0, "n": 0})
        skill_scores[r["skill"]]["p"] += r["pass"]
        skill_scores[r["skill"]]["par"] += r["partial"]
        skill_scores[r["skill"]]["f"] += r["fail"]
        skill_scores[r["skill"]]["n"] += 1

    lines += ["## Per-Skill Aggregate", "", "| Skill | Pass Rate | Cases |", "|-------|-----------|-------|"]
    for skill, s in sorted(skill_scores.items()):
        total = s["p"] + s["par"] + s["f"]
        rate = (s["p"] / total * 100) if total else 0
        lines.append(f"| {skill} | {rate:.0f}% | {s['n']} |")

    lines.append("")
    return "\n".join(lines)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Run LLM-as-judge evaluation pipeline")
    parser.add_argument("-n", "--max-cases", type=int, help="Limit number of test cases to run")
    parser.add_argument("--only-skill", help="Run only a specific skill (e.g., cio-qa-prep)")
    parser.add_argument("--only-asset-class", help="Run only a specific asset class (e.g., private-equity)")
    parser.add_argument("--save-outputs", action="store_true", help="Save generated outputs to tests/reports/outputs/")
    parser.add_argument("--dry-run", action="store_true", help="Show test cases without running")
    args = parser.parse_args()

    matrix_path = TESTS_DIR / "test_matrix.yaml"
    with open(matrix_path) as f:
        matrix = yaml.safe_load(f)

    test_cases = matrix["test_cases"]
    print(f"Loaded {len(test_cases)} test cases from {matrix_path.name}")

    if args.dry_run:
        for i, tc in enumerate(test_cases, 1):
            print(f"  {i}. {tc['skill']} / {tc['asset_class']}: {tc['prompt'].strip()[:80]}...")
        return

    if args.only_skill:
        test_cases = [tc for tc in test_cases if tc.get("skill") == args.only_skill]
    if args.only_asset_class:
        test_cases = [tc for tc in test_cases if tc.get("asset_class") == args.only_asset_class]
    if not test_cases:
        print("No test cases matched the provided filters.")
        return

    results = run_pipeline(
        test_cases,
        max_cases=args.max_cases,
        save_outputs=args.save_outputs,
    )

    REPORTS_DIR.mkdir(parents=True, exist_ok=True)

    report = generate_report(results)
    report_path = REPORTS_DIR / "eval-report.md"
    report_path.write_text(report)
    print(f"\nReport written to {report_path}")

    results_path = REPORTS_DIR / "eval-results.json"
    results_path.write_text(json.dumps(results, indent=2))
    print(f"Raw results written to {results_path}")

    total_f = sum(r["fail"] for r in results)
    if total_f > 0:
        print(f"\nWARNING: {total_f} checklist item(s) failed across all test cases.")
        sys.exit(1)
    else:
        print("\nAll checklist items passed or partial. Ready to publish.")


if __name__ == "__main__":
    main()
