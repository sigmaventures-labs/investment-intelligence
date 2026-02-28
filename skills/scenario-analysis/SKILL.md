---
name: scenario-analysis
description: >
  Build rigorous scenario analyses with probability-weighted returns and sensitivity
  tables for any asset class. Works for public equities (bull/base/bear on price targets),
  real estate (rent/cap rate/occupancy scenarios), and private equity (IRR/MOIC across
  operating and exit assumptions). Use when the user wants to model outcomes, stress-test
  assumptions, build scenario trees, or assess risk/reward. Trigger for 'bull/base/bear',
  'model upside and downside', 'sensitivity analysis', 'stress test', 'expected value',
  or evaluating an investment across multiple scenarios.
---

# Scenario & Sensitivity Analysis

Quantify what happens when you're right, wrong, and somewhere in between.

## Asset Class Detection

Load the asset-class-specific key variables and returns methodology:

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

Single-point estimates are the enemy of good investing. Scenario analysis forces
intellectual honesty by asking: "What are the real range of outcomes, how likely
is each, and is the risk-adjusted return attractive enough to deploy capital?"

### Inputs

- **Subject**: Company, asset, deal, or portfolio
- **Key variables**: The 2-5 assumptions that drive most of the return
  (see reference file for asset-class-specific variables)
- **Current anchor**: Price, basis, or entry terms
- **Thesis context** (optional): Defines what bull and bear mean
- **Time horizon**: Evaluation period

### Step 1 — Identify Key Variables

Find the 2-5 highest-sensitivity variables. Sensitivity rank = "If I move this
±1 standard deviation, how much does the return change?" See reference file for
typical high-sensitivity variables per asset class.

```markdown
| Variable | Current/Consensus | Your Base | Sensitivity Rank |
```

### Step 2 — Define Scenarios

Build 3-5 scenarios. For each, specify ALL key variables:

```markdown
### [Scenario Name] — [Descriptive Label]
**Narrative**: [2-3 sentences. What world produces this outcome?]
**Probability**: [X%]

| Variable | Assumption | vs. Consensus/Market | Rationale |

**Implied return**: [IRR, price target, MOIC — per asset class]
```

**Design principles (universal):**
- Probabilities sum to ~100%
- Bull/bear are NOT symmetric (real distributions are skewed)
- Each scenario is internally consistent (no recessionary demand + peak multiples)
- Scenarios are falsifiable — define observable confirming data
- Base case = YOUR view, not market/consensus

### Step 3 — Calculate Expected Return

```markdown
| Scenario | Prob | Return Metric | Prob-Weighted |
```

**Risk/reward ratio**: Probability-weighted upside / probability-weighted downside

### Step 4 — Sensitivity Table (MANDATORY)

**You MUST produce a two-variable sensitivity matrix** using the two highest-ranked
variables. This is not optional even with limited data — use reasonable assumption
ranges and label them. The table must include:

- A grid showing the return metric across the range of both variables
- Clear marking of where the investment "breaks" (returns fall below hurdle)
- Cliff edges (small assumption changes → large return impact)
- What % of the matrix is "investable"

**Break-even assumptions (MANDATORY)**: Below the sensitivity table, explicitly
state the break-even values — the exact assumption levels at which the investment
returns zero or falls below the hurdle rate. Format:

```markdown
**Break-even**: [Variable A] at [value] with [Variable B] at base, or
[Variable B] at [value] with [Variable A] at base.
```

### Step 5 — Monitoring Framework (MANDATORY)

**You MUST produce a monitoring table and decision triggers.** Do not omit this
section even if the user provides minimal context — define the indicators that
would shift you between scenarios, using observable data with specific thresholds.

```markdown
| Indicator | Bull Signal | Base Signal | Bear Signal | Current | Next Data |

**Increase/deploy if**: [Observable conditions with thresholds]
**Hold if**: [Observable conditions]
**Reduce/exit if**: [Observable conditions with thresholds]
```

If you lack specific current data, provide the framework with placeholder
thresholds and note which data points the user should fill in. Never omit
the section entirely.

## Common Pitfalls

- **Symmetric bull/bear**: Just adding and subtracting 20% from base is lazy.
  Real distributions are skewed — think about what the actual tail looks like.
- **Internally inconsistent scenarios**: Recession + margin expansion is unlikely
  without a specific mechanism. Each scenario should describe a coherent world.
- **Base case = consensus**: Your base case should reflect your differentiated
  analysis. If it matches the market, you don't have an edge.
- **Even probabilities**: A 33/33/33 split signals you haven't formed a view.
  The whole point is to express where you have conviction.
- **Missing sensitivity table**: Producing scenarios without a sensitivity grid
  is the most common omission. The table is where you discover cliff edges
  and break-even points — without it, you don't know where the thesis breaks.
- **Omitting monitoring/triggers**: A scenario analysis without decision triggers
  is a static document. Always define what observable data would shift you
  between scenarios and what actions follow.

## Quality Checklist

- [ ] Variables ranked by sensitivity
- [ ] Scenarios internally consistent
- [ ] Probabilities sum to ~100%
- [ ] Bull/bear NOT symmetric
- [ ] Base case = your view, not consensus
- [ ] Expected return and risk/reward calculated
- [ ] Sensitivity table reveals where the thesis breaks
- [ ] Break-even assumptions identified
- [ ] Monitoring framework with specific thresholds
- [ ] Decision triggers are observable

## Worked Example (Truncated)

**Subject**: CrowdStrike (CRWD) — long position at $310

| Scenario | Prob | Rev Growth | NRR | FCF Margin | Fwd EV/Sales | Return |
|----------|------|-----------|-----|-----------|-------------|--------|
| **Bull** — TAM expansion into SIEM/observability | 25% | 38% | 125% | 32% | 18x | +45% |
| **Base** — steady platform consolidation | 45% | 30% | 118% | 28% | 14x | +18% |
| **Bear** — macro seat optimization, MSFT E5 competition | 20% | 22% | 110% | 24% | 10x | -15% |
| **Tail** — major breach of CRWD customer erodes trust | 10% | 15% | 100% | 20% | 7x | -40% |

**Expected return**: (25% x 45%) + (45% x 18%) + (20% x -15%) + (10% x -40%) = **+12.4%**
**Risk/reward**: +16.4% weighted upside / -7.0% weighted downside = **2.3x**

**Thesis breaks when**: NRR < 112% for 2 consecutive quarters (signals real churn,
not timing). Two-variable sensitivity on NRR (110-125%) x Fwd EV/Sales (8-18x)
shows 72% of the matrix is above the 10% return hurdle.
