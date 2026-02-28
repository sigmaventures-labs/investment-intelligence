---
name: cross-asset-signals
description: >
  Synthesize signals across equity, credit, rates, FX, and commodity markets to confirm
  or deny investment theses, detect regime changes, and surface dislocations. Adds
  asset-class-specific signal layers for equities, real estate, and private equity on
  top of the core five-lens framework. Use when the user wants to check what other
  markets say about a thesis, find cross-market conflicts, or assess the macro backdrop.
  Trigger for 'what are rates/credit telling us', 'cross-asset check', 'macro backdrop',
  'are markets in agreement', or reading across asset classes for a unified view.
---

# Cross-Asset Signal Synthesis

Read the full market tape, not just your asset class silo.

## Asset Class Detection

The core five-lens framework applies to ALL asset classes. Additionally, load
asset-class-specific signal layers:

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

## Core Five-Lens Framework (All Asset Classes)

### 1. Rates & Duration
- Yield curve shape (2s10s, 2s30s) — growth/recession signal
- Real rates (TIPS yields) — the gravity variable for all asset valuations
- Fed funds futures / OIS — policy path pricing
- Breakeven inflation — inflation expectations

### 2. Credit
- IG and HY spreads (level + direction)
- CDS indices (CDX IG, CDX HY) — real-time risk pricing
- Leveraged loan prices and CLO issuance — risk appetite
- Distressed ratios (% HY >1000bps)
- Primary market access — can issuers access capital?

### 3. FX & Capital Flows
- DXY and major pairs
- EM FX basket — risk appetite proxy
- Carry trade dynamics
- Flow data (TIC, CFTC COT)

### 4. Commodities
- Oil — demand + input cost signal
- Copper — industrial demand barometer
- Gold — real rate sensitivity + risk sentiment
- Curve shape — supply/demand tightness

### 5. Volatility & Positioning
- VIX level and term structure
- MOVE index (rates vol)
- Skew — tail risk pricing
- Correlation regimes

## Execution Framework

### Why This Matters

Most analysts operate in a single-asset-class silo — equity analysts watch
equities, credit analysts watch credit, and neither reads the other's tape.
But markets are interconnected: when equities rally and credit widens, one of
them is wrong. Cross-asset synthesis surfaces dislocations and confirms or
contradicts your thesis with evidence from markets that have different
participants, incentives, and information sets.

### Step 1 — Define the Thesis to Test
State as a testable proposition. Identify primary (2-3) and secondary (1-2)
signal lenses. Include asset-class-specific signals from reference file.

### Step 2 — Survey Current Signals
For each: current reading, trend (1w/1m/3m), historical context, interpretation,
thesis alignment (Confirming/Contradicting/Neutral).

**Historical context requirement**: For each signal, provide at least one
concrete historical comparison — e.g., "HY spreads at 320bps are in the
25th percentile of the last 5 years" or "last time 2s10s was this steep
was Q1 2022, which preceded..." Raw levels without historical anchoring are
not actionable.

### Step 3 — Alignment Matrix

**MANDATORY**: Identify agreements AND disagreements/contradictions across lenses.
If all signals appear to confirm the thesis, explicitly investigate harder — look
for subtle tensions (e.g., credit quality dispersion, vol term structure shape,
positioning extremes) and state the most plausible contradictory signal even if
you ultimately dismiss it. A "no disagreements found" conclusion requires
specific evidence for why the rare all-confirming state is genuine, not a sign
of incomplete analysis.

For each dislocation or disagreement found:
- State the conflict clearly
- Assess which market is likely "right" and why (with historical precedent:
  reference at least one prior episode — e.g., "similar divergence in Q3 2022
  resolved in favor of credit within 2 months")
- State what would change your assessment

### Step 4 — Synthesize
Opinionated narrative (not data dump): what the tape says, thesis verdict,
cross-asset risks, actions, monitoring signals with thresholds.

## Common Cross-Asset Playbooks

- Equity rally + credit widening → equity rally suspect
- Falling real rates + rising gold + steepening curve → easing, growth leads
- Rising real rates + strong dollar + EM weakness → tightening, risk-off
- Copper + oil rising + curve steepening → reflation, cyclicals lead
- VIX contango extreme + bullish positioning → complacency, vol shock risk
- IG tightening + HY widening → quality discrimination, risk-off brewing

## Common Pitfalls

- **Data dump without synthesis**: The value is the interpretation, not the table
  of readings. Always end with an opinionated narrative.
- **Cherry-picking confirming signals**: Dismissing contradictory evidence because
  it doesn't fit the thesis is the most common failure mode. If every lens
  "confirms," you probably haven't looked hard enough.
- **All-confirming without challenge**: Presenting a unanimous confirming tape
  without acknowledging even one tension or risk signal. Real markets rarely
  agree perfectly — find the crack or explain why there isn't one.
- **Equal weighting all markets**: Credit is more relevant for leveraged companies;
  FX matters more for EM exporters. Weight signals by relevance to the thesis.
- **Levels without direction**: A VIX of 18 means different things depending on
  whether it's rising from 12 or falling from 30. Always note the trend.

## Quality Checklist

- [ ] Thesis stated as testable proposition
- [ ] At least 3 core lenses + relevant asset-class-specific signals surveyed
- [ ] Agreements AND disagreements identified
- [ ] Dislocations assessed for which market is likely right
- [ ] Historical context provided
- [ ] Synthesis is opinionated
- [ ] Monitoring signals defined with thresholds

## Worked Example (Truncated)

**Thesis to test**: "US consumer resilience supports long consumer discretionary equities"

| Lens | Signal | Reading | Trend (3m) | Thesis Alignment |
|------|--------|---------|------------|------------------|
| Rates | 2s10s spread | +45bps | Steepening | Confirming — growth expectations improving |
| Credit | HY spreads | 320bps | Tightening | Confirming — risk appetite healthy |
| FX | DXY | 104.2 | Flat | Neutral |
| Commodities | Oil (WTI) | $78 | Rising | Mixed — demand signal, but input cost pressure |
| Vol | VIX | 14.5 | Declining | Confirming — complacency supports risk assets |

**Dislocation**: Consumer confidence surveys declining while credit card ABS
performance remains strong. Trust hard data (ABS) over soft data (surveys) in
the near term, but monitor for convergence.

**Verdict**: 4 of 5 lenses confirm. Tape supports the thesis. Monitor oil above
$85 (margin compression trigger) and consumer ABS delinquency data for cracks.
