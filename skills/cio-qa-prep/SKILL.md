---
name: cio-qa-prep
description: >
  Anticipate and pre-build answers to tough questions from CIOs, PMs, or investment
  committee members about any investment position — equities, real estate, or PE deals.
  Use when preparing for IC meetings, portfolio reviews, risk meetings, deal committee,
  or any situation where a position must be defended. Trigger for 'help me prepare for IC',
  'what will the PM push back on', 'stress test my thesis', 'prep me for deal committee',
  'what questions will I get', or anticipating tough questions about any investment.
---

# CIO/PM Q&A Prep

Prepare the analyst to survive the toughest room in finance.

## Asset Class Detection

Load the asset-class-specific question bank and answer patterns:

- **Public Equities**: Read `references/public-equities.md`
- **Real Estate**: Read `references/real-estate.md`
- **Private Equity**: Read `references/private-equity.md`

## Data Transparency & Verification

### Analysis Mode

Every output must display an analysis mode label in the header:

- **Surface Mode** — No MCP data connectors or proprietary data available. All market data, prices, and estimates are based on training data and must be flagged. Header reads: `Analysis Mode: Surface (public data only — verify all figures)`
- **Enhanced Mode** — MCP data sources or user-provided proprietary data are available. Header reads: `Analysis Mode: Enhanced`. In this mode, also ask: "What internal KPIs are most predictive? What data contradicts consensus? What proprietary signals exist?"

Default to Surface Mode unless MCP tools or user-provided data are explicitly present.

### Data Inputs Block

The first section of every output (immediately after the header) must be a **Data Inputs** block listing all sources used:

- **MCP-sourced**: List specific data points pulled from MCP connectors (e.g., "10Y Treasury yield: 4.1% via FRED")
- **User-provided**: List data explicitly provided by the user (e.g., "Target price: $45 per user input")
- **Training-data estimates**: List figures derived from training data, each flagged with `[estimate]` (e.g., "HY spreads: ~320bps [estimate]")

### Source Flagging Rules

- Never present training-data numbers as verified facts
- Flag all training-data figures with `[estimate]` inline
- If MCP data is available for a figure, use it and cite the source
- If the user provided a figure, use it exactly and cite "per user input"
- Include a "Sources & Verification" section at the end of every output listing what was sourced vs. estimated

### Verification Checklist

Every output must pass these checks before delivery:
- [ ] All price targets and valuations marked as estimates unless sourced
- [ ] Historical data points cite specific source or flagged for verification
- [ ] Consensus estimates cite provider and date, or flagged as training-data approximation
- [ ] User-provided inputs used exactly as given, never silently altered
- [ ] Analysis Mode label present in output header
- [ ] Data Inputs block present as first section of output

## Core Framework (All Asset Classes)

### Why This Matters

The gap between a good thesis and a funded position is the IC meeting. Strong
ideas routinely die in committee because the analyst can't handle adversarial
questioning — or worse, hasn't thought through the weak points an experienced
PM will immediately spot. Preparation isn't about memorizing answers; it's about
stress-testing your thesis deeply enough to survive the toughest room in finance
while honestly conceding where uncertainty exists.

### Inputs

- **The investment thesis or memo**
- **Fund context** (optional): Strategy, current portfolio, performance, risk budget
- **Meeting type** (optional): Initial pitch, position review, risk committee,
  drawdown/loss defense, deal committee approval

### Step 1 — Questioner Archetypes

These archetypes are universal — only the specific questions change by asset class:

**The PM / Deal Lead** — Sizing, timing, opportunity cost, risk/reward asymmetry.
Core question: "Why this instead of something else?"

**The CIO / Managing Partner** — Strategic fit, macro overlay, tail risks, fund-level
impact, LP/investor optics. Core question: "What's the scenario where this costs us?"

**The Risk Manager** — Downside quantification, stress scenarios, hedging, limits.
Core question: "What's the max loss and how do we contain it?"

**The Skeptic / Devil's Advocate** — Weakest link, contrarian view, consensus challenge.
Core question: "Why are you right and the market/seller/other bidders wrong?"

### Step 2 — Generate 15-25 Questions

**MANDATORY**: You MUST produce at least 15 fully-formed questions with answers
before moving to the Vulnerability Assessment. Do not stop at 3-5 questions.
If the user provides limited context, make reasonable assumptions (label them)
and still generate the full set. Breadth across categories is the point — a
3-question prep is worse than no prep at all.

Organize by category with difficulty ratings. See reference file for asset-class-specific
question categories. Before finalizing, verify coverage: at least 2 questions per
archetype (PM, CIO, Risk, Skeptic) and at least 3 category groups from the
reference file.

**Difficulty levels:**
- **Standard**: Expected questions any prepared analyst should handle
- **Hard**: Requires deep knowledge or nuanced reasoning
- **Killer**: Designed to end the conversation — usually challenges why consensus
  is right and you're wrong, or exposes a structural risk

Every question set MUST include at least 3 "Killer" questions.

### Step 3 — Build the Answer Playbook

For each question:

```markdown
### Q[N]: [Question text]
**Difficulty**: [Standard/Hard/Killer]
**Best answer (2-3 sentences)**: [Concise, confident, data-backed]
**Supporting evidence**: [Specific data points or analysis]
**If pressed further**: [Follow-up when they push back]
**Red line**: [Where to concede uncertainty — honesty is a feature]
```

### Step 4 — Vulnerability Assessment

```markdown
## Vulnerability Assessment
### Strongest points in the thesis
### Weakest points in the thesis
### Recommended pre-meeting actions
[Specific: "Pull Q3 lease comps from [broker]" not "Do more research"]
### Suggested opening framing
[How to frame the pitch to preempt predictable objections]
```

## Tone by Meeting Type

- **Initial pitch / deal committee**: "Why should we care" → lead with edge
- **Position / asset review**: "What's changed" → reference original assumptions
- **Risk committee / loss defense**: Adversarial → data-driven, acknowledge what
  went wrong, explain why thesis survives (or what the new thesis is)

## Common Pitfalls

- **Defensive essays instead of answers**: If your answer exceeds 3 sentences,
  it signals insecurity. Concise and confident beats thorough and nervous.
- **Preparing only for "Standard" questions**: Getting blindsided by a Killer
  question is worse than not preparing at all — it looks like you didn't think
  about the hard parts.
- **False confidence on weak points**: Experienced PMs detect it instantly.
  Having an honest red line is a strength, not a weakness.
- **Generic answers**: Every answer should contain a specific, thesis-relevant
  data point. If the answer could apply to any company, it's not good enough.
- **Stopping at 3-5 questions**: A short question list leaves massive blind spots.
  Always produce at least 15. If context is thin, assume and label assumptions.

## Quality Checklist

- [ ] At least 15 questions across all categories
- [ ] At least 3 "Killer" difficulty questions
- [ ] Answers are concise (2-3 sentences), not defensive essays
- [ ] "If pressed further" for Hard and Killer questions
- [ ] Red lines identified
- [ ] Vulnerability assessment is honest
- [ ] Pre-meeting actions are specific
- [ ] Opening framing suggested

## Worked Example (Truncated)

**Thesis**: Long Danaher (DHR) on life sciences recovery cycle
**Meeting type**: Initial pitch to PM

### Q1: "What's your variant perception in one sentence?"
**Difficulty**: Standard
**Best answer**: "Biotech funding recovery is flowing through to instrument orders
2 quarters earlier than sell-side models assume, based on channel checks with 12
lab procurement officers."
**Supporting evidence**: Order book data from 3 major distributors showing 15% QoQ uptick.
**If pressed further**: "Sell-side bakes in recovery in H2 — we think Q1 earnings
show it, making the stock re-rate before consensus catches up."
**Red line**: "If the procurement data is noise rather than signal, our timing
edge disappears. The secular thesis holds but the catalyst is wrong."

### Q7: "Why isn't this just buying the most expensive name and hoping for a cycle turn?"
**Difficulty**: Killer
**Best answer**: "DHR trades at a 15% discount to its 5-year avg premium vs. TMO,
and our thesis is based on specific order data, not cycle hope."
**If pressed further**: "The relative valuation gap opened 6 months ago when
biotech sentiment troughed. Funding has recovered — the stock hasn't re-rated."
**Red line**: "If you believe life sciences instrumentation is in secular — not
cyclical — decline, then the valuation gap is justified and we're wrong."
