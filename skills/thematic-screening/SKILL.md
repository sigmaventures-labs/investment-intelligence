---
name: thematic-screening
description: >
  Map a macro or thematic investment thesis to the full chain of affected investable
  assets — companies, properties, funds, or deals — identifying beneficiaries, losers,
  and second/third-order effects across sectors and geographies. Works across asset
  classes: public equities, real estate, and private equity. Use this skill whenever
  the user provides a macro thesis, secular trend, or policy shift and wants to identify
  investable opportunities. Trigger for 'who benefits from X', 'what plays on Y',
  'map the supply chain for Z', 'screen for exposure to W', or any thematic screening.
---

# Thematic Screening

Turn a macro thesis into a structured, investable universe of affected assets.

## Asset Class Detection

Determine the asset class from context. If ambiguous, ask. Then load the
appropriate reference file for asset-class-specific taxonomy and output format:

- **Public Equities**: Read `references/public-equities.md`
- **Real Estate**: Read `references/real-estate.md`
- **Private Equity**: Read `references/private-equity.md`

If the thesis spans multiple asset classes (e.g., "rising rates reshape capital
allocation"), run the screen across all relevant classes and note cross-asset
implications.

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

Most thematic investing stops at the obvious: "AI is big, buy NVDA." The real
alpha is in second and third-order effects — the non-obvious beneficiaries and
losers the market hasn't connected to the thesis. Systematic screening forces
you past the first-order consensus names into the tail of the distribution,
where ideas are less crowded and pricing is less efficient.

### Inputs

- **Thesis statement**: Clear articulation of the macro trend, policy change, or
  secular shift
- **Asset class**: Public equities, real estate, private equity, or multi-asset
- **Scope constraints** (optional): Geography, size floor, liquidity minimum,
  sector/property type exclusions
- **Time horizon** (optional): Near-term catalyst-driven vs. multi-year secular

### Step 1 — Decompose the Thesis into Causal Chains

Break the thesis into discrete causal mechanisms. For each, trace effects forward:

- **First-order**: Who/what is immediately and directly affected?
- **Second-order**: Who supplies, competes with, or depends on the first-order
  affected? What shifts in pricing power, demand, or capital flows result?
- **Third-order**: What behavioral shifts emerge? What adjacent markets expand
  or contract? What substitution effects arise?

The causal chain methodology is identical across asset classes — only the nodes
change (companies vs. property types vs. deal categories).

### Step 2 — Build the Asset Map

Organize identified opportunities into a tiered structure. See the asset-class
reference file for the specific taxonomy and table format. Every map must include:

- **Tier 1 — Direct beneficiaries/exposure**
- **Tier 2 — Indirect / second-order**
- **Tier 3 — Non-obvious / third-order**
- **Negative exposure — Losers / impaired assets**

For each entry: specific mechanism (one sentence), conviction level (H/M/L),
and a quantified exposure metric (defined per asset class).

### Step 3 — Validate and Pressure-Test

For each entry on the map, ask:

1. **Is this already priced in / consensus?** Has the market, asset price, or
   deal flow already adjusted for this theme?
2. **What's the counter-thesis?** Why might the impact be overstated?
3. **Is the exposure pure or diluted?** How concentrated is the thematic
   exposure relative to the total asset?
4. **Investability filter**: Can you actually express this view given size,
   liquidity, access, and mandate constraints?

### Step 4 — Prioritize for Deep Dives

Rank by composite of: magnitude of thematic exposure, degree the thesis is
underappreciated, investability, and upcoming catalysts or decision points.

Produce a **Top 5 Deep Dive Candidates** list with 2-3 sentence rationale each.

## Output Structure

1. **Thesis Summary** — 2-3 sentences restating thesis and key assumptions
2. **Causal Chain Diagram** — Text-based flow: first → second → third-order
3. **Asset Map** — Tiered tables per asset-class reference format
4. **Pressure Test Notes** — Counter-arguments and "priced in" assessments
5. **Top 5 Deep Dive Candidates** — Prioritized shortlist with rationale
6. **Cross-Asset Implications** (if applicable) — How the thesis plays across
   asset classes differently
7. **Data Gaps & Next Steps** — Additional research needed

## Common Pitfalls

- **Stopping at first-order effects**: The obvious names are already crowded.
  The value of systematic screening is in second and third-order effects.
- **Omitting losers**: The short side of a thematic screen is often more
  actionable than the long side — fewer people are looking for it.
- **Category association as analysis**: "AI is good for tech companies" is not
  a specific mechanism. Each entry must articulate exactly how and why.
- **Ignoring "priced in"**: An obvious beneficiary trading at 40x forward is
  a very different proposition from one trading at 12x. Screen for alpha, not
  just exposure.

## Quality Checklist

- [ ] At least 3 levels of causal chain depth explored
- [ ] Negative exposure / losers included, not just beneficiaries
- [ ] Each entry has a specific mechanism, not just category association
- [ ] Counter-thesis articulated for top candidates
- [ ] Exposure metric quantified where possible
- [ ] Non-obvious / surprising entries included (the value is in the tail)
- [ ] Investability constraints acknowledged

## Worked Example (Truncated)

**Thesis**: "GLP-1 drug adoption reshapes consumer and healthcare spending"

**Causal chain**: GLP-1 adoption → reduced caloric intake →
**1st order**: food/bev volume decline, bariatric surgery decline →
**2nd order**: snack reformulation, gym pivot from weight-loss to fitness,
health insurance cost reduction →
**3rd order**: reduced diabetes/cardio spend reshapes managed care loss ratios,
restaurant foot traffic impacts commercial RE

| Tier | Asset | Mechanism | Conviction | Rev. Exposure |
|------|-------|-----------|------------|---------------|
| **T1** | LLY, NVO | Drug manufacturers | H | 30-50% of pipeline value |
| **T1 Neg** | GKOS, INSP | Bariatric/surgical displacement | H | 60-80% procedure risk |
| **T2** | MDLZ, PEP | Snack volume headwind, reformulation cost | M | 5-10% volume risk |
| **T3** | UNH, HUM | Lower chronic disease cost → MLR improvement | M | 2-4% MLR over 5-10yr |

**Priced in?** LLY/NVO fully. Bariatric disruption partially. Snack headwinds
starting. Managed care benefit — not priced (too long-dated for the market).

**Top deep-dive candidate**: UnitedHealth (UNH) — if GLP-1s reduce diabetes
prevalence by even 5% over 10 years, the MLR impact is material but too far
out for the market to discount today. Non-consensus, high-magnitude, uninvested.
