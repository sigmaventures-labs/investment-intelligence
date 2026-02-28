---
name: catalyst-mapping
description: >
  Build a forward-looking catalyst calendar for any asset class — mapping events that will
  prove or disprove a thesis and trigger value realization. Works for public equities
  (earnings, regulatory decisions), real estate (lease events, refinancing, permits), and
  private equity (portfolio milestones, exit windows, fund lifecycle). Use when the user
  wants to map upcoming events, plan around binary outcomes, build an event calendar, or
  assess timing risk. Trigger for 'what events are coming up', 'map the catalysts',
  'build an event calendar', 'what could move this', or identifying price/value-moving events.
---

# Catalyst Mapping

Map the events that will prove or disprove a thesis — and when they land.

## Asset Class Detection

Load the asset-class-specific catalyst taxonomy:

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

A thesis without a catalyst path is a thought experiment, not an actionable
investment. Catalyst mapping converts directional conviction into time-bound,
observable events. This is essential for timing entries/exits, avoiding dead
money, managing event risk, and prioritizing research effort.

### Inputs

- **Scope**: Single asset/company, portfolio, sector, or fund
- **Time horizon**: Typically 3-24 months forward (longer for PE/RE)
- **Thesis context** (optional): Helps prioritize confirming vs. threatening events
- **Current positioning** (optional): Direction, size, basis/entry price

### Step 1 — Enumerate All Known Catalysts

Walk through every category in the asset-class-specific taxonomy. For each:

```markdown
- Event: [Description]
- Date: [Exact date or estimated window]
- Date certainty: [Confirmed / Estimated / Speculative]
- Category: [From taxonomy]
- Outcome if positive: [Impact direction and estimated magnitude]
- Outcome if negative: [Impact direction and estimated magnitude]
- Probability of positive outcome: [%]
- Thesis relevance: [Confirming / Threatening / Neutral]
```

### Step 2 — Assess Asymmetry

For each material catalyst, the key question is NOT "what's the most likely
outcome" but "what's the risk/reward of holding through the event."

- **What's priced in?** If the market expects the positive outcome at 90%
  probability, upside on confirmation is small but downside on miss is large.
- **Historical precedent**: How have similar events moved similar assets?
- **Positioning**: If everyone is positioned for one outcome, surprise value
  is in the other direction.

Classify each: **Positive asymmetry** (favorable to hold through) /
**Negative asymmetry** (consider reducing/hedging) / **Symmetric**

### Step 3 — Build the Calendar

Chronological timeline organized by month/quarter with all metadata.

### Step 4 — Identify Clusters, Gaps, and Dependencies

- **Clusters**: Multiple catalysts converging → high-volatility windows
- **Gaps**: Extended periods without catalysts → dead money / carrying cost
- **Sequencing**: Catalysts whose outcomes change the probability of subsequent events

### Step 5 — Action Recommendations

```markdown
### Pre-position: [Positive asymmetry events where thesis has edge]
### Reduce / Hedge: [Negative asymmetry or high uncertainty]
### Monitor Closely: [Thesis-critical, action depends on incoming info]
### Research Priorities: [Analysis needed before next catalyst]
```

## Common Pitfalls

- **Only listing confirming catalysts**: Ignoring events that could disprove
  the thesis leads to blind spots. Every map must include threatening events.
- **Treating all catalysts as equal**: A widely expected earnings beat is not
  a catalyst — always assess what's already priced in.
- **Ignoring sequencing dependencies**: A failed Phase 2 trial changes the
  probability of everything downstream. Catalysts are not independent.
- **Static calendar**: Building it once and never updating as events resolve
  and new information changes probabilities.

## Quality Checklist

- [ ] All categories in the asset-class taxonomy systematically checked
- [ ] Dates classified as Confirmed / Estimated / Speculative
- [ ] Magnitude estimates for material catalysts
- [ ] Asymmetry assessed (not just direction)
- [ ] "Priced in" analysis for highest-impact events
- [ ] Clusters and gaps identified
- [ ] Dependencies/sequencing mapped
- [ ] Action recommendations are specific and time-bound

## Worked Example (Truncated)

**Subject**: Vertex Pharmaceuticals (VRTX) — long thesis on pipeline optionality
**Horizon**: 6 months

| Event | Date | Certainty | Category | Asymmetry | P(Pos.) |
|-------|------|-----------|----------|-----------|---------|
| PDUFA: VX-548 (acute pain) | Mar 30 | Confirmed | Regulatory | Positive — market pricing ~30% approval; upside +15-25% vs. downside -10% | 45% |
| Q1 Earnings | Apr 24 | Confirmed | Earnings | Negative — beat → +5-8%, miss on Trikafta trends → -8-12% | 60% |
| JPM Healthcare Conference | Jan 13 | Confirmed | Industry | Symmetric — sentiment update, no binary outcome | 70% |

**Cluster alert**: PDUFA + earnings within 4 weeks creates a high-vol window
(Mar-Apr).

**Action**: Pre-position ahead of PDUFA (positive asymmetry — market underpricing
approval odds). Consider reducing into earnings if PDUFA resolves positively
(lock gains before negatively asymmetric event).
