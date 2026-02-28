# Investment Intelligence — AI Skills for Equity Analysis

Six structured analyst workflows for public equities — thematic screening,
investment memos, IC prep, catalyst mapping, cross-asset signals, and scenario
analysis. Available as a Cursor plugin, compatible with Claude Code and OpenClaw.

## Quick Start

Install the plugin, then try:

```
/thematic-screen GLP-1 drug adoption is reshaping consumer and healthcare spending
```

You'll get a structured screen with 3-tier causal chains, beneficiaries and losers
with tickers, exposure metrics, counter-theses, and deep-dive candidates.
See [examples/](examples/) for full sample outputs from all 6 skills.

---

## Skills

| Skill | What it does | Command | What you provide |
|-------|-------------|---------|-----------------|
| **Thematic Screening** | Map macro thesis to investable universe with causal chains | `/thematic-screen` | A thesis or trend statement |
| **Investment Memo** | Professional equity pitch in institutional format | `/investment-memo` | Ticker + price + your thesis |
| **CIO/PM Q&A Prep** | Anticipate 15-25 IC questions with answer playbook | `/cio-qa-prep` | Your thesis + meeting context |
| **Catalyst Mapping** | Forward event calendar with asymmetry analysis | `/catalyst-map` | Ticker + thesis + time horizon |
| **Cross-Asset Signals** | Read rates, credit, FX, commodities, vol to test thesis | `/cross-asset` | A testable thesis statement |
| **Scenario Analysis** | Bull/base/bear with sensitivity tables and decision triggers | `/scenario-analysis` | Ticker + price + key variables |

### What Each Skill Needs from You

The more specific context you provide, the more differentiated the output.
Generic prompts produce generic analysis.

- **`/thematic-screen`** — A macro thesis or trend (e.g., "GLP-1 adoption reshaping consumer spending"). No specific asset required.
- **`/investment-memo`** — A specific equity + price + investment thesis. Include key drivers, variant perception, and time horizon for best results.
- **`/cio-qa-prep`** — Your thesis + who you're presenting to (PM, IC, CIO) + what you think the weak points are.
- **`/catalyst-map`** — A specific position + time horizon (e.g., "Vertex Pharma over the next 8 months").
- **`/cross-asset`** — A testable thesis statement (e.g., "US consumer resilience supports long consumer discretionary over 6 months").
- **`/scenario-analysis`** — An equity + current price + the 2-4 variables you want in the sensitivity table (e.g., "revenue growth, margins, multiple").

---

## Data Philosophy

This system is data-agnostic. It works with public data. It becomes materially
more powerful when used with proprietary operating data.

- **Surface Mode** — Out of the box, skills produce structured analysis using
  AI estimates from training data. Every estimate is flagged with `[estimate]`
  for verification. Outputs include a Data Inputs block showing what was sourced
  vs. estimated.
- **Enhanced Mode** — Connect MCP data sources (FRED for macro data, or paid
  providers like FactSet) and the same skills produce analysis grounded in real,
  verified data.

Data quality determines signal strength. Workflow quality determines decision
discipline. These skills encode the latter.

### MCP Data Connectors

The `.mcp.json` file configures data connections:

- **FRED** (active, free) — macro data: Treasury yields, credit spreads,
  employment, CPI, Fed funds rate
- **Paid providers** (stubs, requires subscription) — FactSet, S&P Global,
  PitchBook, Morningstar, Daloopa, Aiera, LSEG, Moody's

To enable a paid provider, uncomment its entry in `.mcp.json` and configure
your API credentials per the provider's documentation.

---

## Example Outputs

Each link shows a full output from one skill run in Surface Mode:

- [Thematic Screening](examples/thematic-screening.md) — GLP-1 adoption screen
- [Investment Memo](examples/investment-memo.md) — Copart (CPRT) long pitch
- [CIO Q&A Prep](examples/cio-qa-prep.md) — Danaher (DHR) IC prep
- [Catalyst Mapping](examples/catalyst-mapping.md) — Vertex Pharma catalyst calendar
- [Cross-Asset Signals](examples/cross-asset-signals.md) — Consumer discretionary thesis check
- [Scenario Analysis](examples/scenario-analysis.md) — CrowdStrike (CRWD) bull/base/bear

---

## How the Skills Chain Together

```
Thematic Screening
  → identifies companies
    → Investment Memo (per company)
      → CIO/PM Q&A Prep (per memo)

Catalyst Mapping + Cross-Asset Signals
  → feed into Scenario Analysis
    → feeds back into Investment Memo (returns + risk sections)
```

### Example Workflow

```
/thematic-screen GLP-1 drug adoption reshapes consumer and healthcare spending
/investment-memo Copart (CPRT) at $45 — ADAS raises total-loss frequency structurally
/catalyst-map Vertex Pharma over the next 8 months, long on pipeline optionality
/scenario-analysis CrowdStrike at $310 — revenue growth, NRR, FCF margin, EV/Sales
/cross-asset US consumer resilience supports long consumer discretionary over 6 months
/cio-qa-prep pitching long Danaher to PM — biotech funding recovery thesis
```

---

## Installation

### Cursor — Marketplace

Install from the [Cursor Marketplace](https://cursor.com/marketplace) — search
for **investment-intelligence**.

### Cursor — Manual

```bash
cp -r skills/ /path/to/your/project/.cursor/skills/
cp -r rules/ /path/to/your/project/.cursor/rules/
cp -r commands/ /path/to/your/project/.cursor/commands/
```

### Claude Code

```bash
cp -r skills/ /path/to/your/project/.claude/skills/
cp -r .claude/commands/ /path/to/your/project/.claude/commands/
```

### OpenClaw

```bash
cp -r skills/ ~/.openclaw/skills/
```

### Prerequisites

- Cursor, Claude Code, or OpenClaw — the LLM is provided by your IDE
- No API keys needed for the skills themselves
- Optional: FRED MCP connector for live macro data (free)
- Optional: paid data provider subscriptions for Enhanced Mode

---

## Architecture

Each skill follows a modular core + overlay design using the
[AgentSkills](https://agentskills.io) spec (`SKILL.md` with YAML frontmatter):

```
skill-name/
├── SKILL.md                    # Core framework + data verification rules
└── references/
    └── public-equities.md      # Equity-specific templates and variables
```

### How the Three Layers Work Together (Cursor)

1. **Rules** (`.mdc`) — Condensed frameworks the agent auto-triggers based on
   your natural language request. Good enough for quick tasks.

2. **Skills** (`SKILL.md` + `references/`) — Full analytical frameworks with
   data verification, source flagging, and quality checklists. Pulled in by
   commands via `@` references.

3. **Commands** (`.md`) — Slash commands you invoke with `/command-name`. These
   bridge rules and skills: they accept your input and pull the right SKILL.md
   + overlay into context.

For maximum depth, use the `/commands`. For quick natural-language requests,
let the rules auto-trigger.

---

## Customization

Adapt to your fund's specific needs:

- **Output templates**: Replace memo templates with your house format
- **Valuation methods**: Add preferred approaches in the references files
- **Data sources**: Configure MCP connectors in `.mcp.json` for your providers
- **Risk parameters**: Adjust hurdle rates, drawdown thresholds, sizing rules
- **Sector overlays**: Add sub-sector reference files (e.g., `references/biotech.md`)
- **Question banks**: Add firm-specific IC questions to the Q&A prep overlays

---

## Roadmap

| Version | Scope | Status |
|---------|-------|--------|
| **v1** | 6 skills, public equities. FRED MCP. Surface/Enhanced modes. | Current |
| **v1.5** | Real estate and private equity overlays with asset-class-native frameworks | Planned |
| **v2** | Internal/proprietary data integration via MCP. Structured ingestion for internal KPIs, portfolio data, deal models. | Future |

---

## FAQ

**Do I need an API key?**
No. The skills run on whatever LLM your IDE provides (Cursor, Claude Code, etc.).
The optional FRED MCP connector is also free.

**Are the numbers in the output real?**
In Surface Mode, all market data and estimates come from the LLM's training data
and are flagged with `[estimate]`. Connect MCP data sources for verified figures.

**Can I use this for real estate or private equity?**
RE and PE overlays are in development (see Roadmap). The current release is
optimized for public equities.

**How do I connect my firm's internal data?**
Add your own MCP server to `.mcp.json`. Skills automatically use MCP data when
available. See the [MCP documentation](https://modelcontextprotocol.io/) for
building custom connectors.

**What's the difference between rules and commands?**
Rules auto-trigger from natural language. Commands are explicit (`/command-name`)
and pull in the full skill framework for deeper analysis.

---

## Disclaimer

These skills assist with financial analysis workflows but do not provide
financial or investing advice. Outputs contain AI-generated estimates that
should be verified against authoritative data sources. Always review
AI-generated analysis with qualified financial professionals before making
investment decisions.

---

## License

[MIT](LICENSE)
