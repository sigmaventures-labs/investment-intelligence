---
name: investment-memo
description: >
  Generate a professional investment memo for any asset class — public equities,
  real estate acquisitions, or private equity deals. Use when the user wants to
  write up an investment idea, pitch a position, create a long/short thesis, draft
  an acquisition memo, or produce any formal investment recommendation. Trigger for
  'write me a pitch on X', 'draft an investment case', 'build a memo on Y',
  'acquisition memo', 'deal memo', or any investment recommendation document.
---

# Investment Memo Generation

Produce a professional-grade investment memo that a decision-maker would take seriously.

## Asset Class Detection

Determine the asset class from context. Then load the appropriate reference file
for the memo template, key variables, and valuation methodology:

- **Public Equities (L/S)**: Read `references/public-equities.md`
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

## Core Principles (All Asset Classes)

These principles apply regardless of what you're pitching:

**Argue, don't describe.** Every section advances the investment thesis. If a
paragraph could appear in a generic overview without modification, it's too generic.

**Quantify everything.** Vague directional claims ("strong growth potential") must
be replaced with specific estimates and the assumptions behind them.

**Identify the variant perception.** Every memo must answer: "What do we believe
that the market / other bidders / consensus does not?" If you can't articulate this,
there may not be a trade.

**Steel-man the counter-argument.** The risk section should articulate the bear case
as well as an opponent would. Then explain why the risk/reward is still attractive.

**Time-bound the thesis.** Every memo needs a defined horizon and a path to value
realization — catalysts (equities), business plan milestones (PE), or lease-up /
stabilization timeline (RE).

**Source the edge.** For each key driver, state what data, analysis, or access
underlies your differentiated view. Primary research beats secondary. Proprietary
analysis beats consensus.

## Universal Memo Skeleton

Regardless of asset class, every memo contains these structural elements (the
specific implementation differs — see reference files):

1. **Header / Deal Summary** — Key terms at a glance
2. **Executive Summary** — 3-5 sentences; thesis, edge, return, and catalyst/milestone
3. **Variant Perception / Edge** — What you see that others don't
4. **Asset / Business Overview** — Thesis-relevant description only
5. **Key Drivers / Value Creation** — The 3-5 variables that matter most
6. **Path to Value Realization** — Catalysts, milestones, or stabilization timeline
7. **Valuation / Returns Analysis** — Primary methodology + sensitivity
8. **Risk Factors** — Honest assessment with mitigants
9. **Position Sizing / Capital Deployment**
10. **Monitoring Framework** — Leading indicators and decision triggers

## Common Pitfalls (Universal)

- **Describing instead of arguing**: If a paragraph could appear in a sell-side
  initiation without modification, delete it. Every sentence should advance
  the thesis.
- **Vague variant perception**: "We think it's undervalued" is not a variant
  perception. What specific thing do you believe that the market does not?
- **Risk section as CYA laundry list**: Listing 15 generic risks without
  assessing probability or providing mitigants is worthless. Fewer, honest
  risks with genuine mitigants.
- **No path to value realization**: A thesis without a catalyst timeline is
  a hope, not an investment. When and how does the market recognize the value?

## Quality Checklist (Universal)

- [ ] Executive summary is self-contained and compelling in under 5 sentences
- [ ] Variant perception is specific, not generic
- [ ] At least 3 key drivers with your view vs. consensus/market
- [ ] Value realization path is time-bound
- [ ] Valuation includes sensitivity on key assumptions
- [ ] Risks are honest and include mitigants
- [ ] Return target is transparently derived
- [ ] No section reads like a generic overview — every paragraph earns its place

## Worked Example (Truncated)

**Executive Summary**: We recommend a long position in Copart (CPRT) at $45.30
with a 12-month price target of $58 (28% upside). Our thesis centers on
structural growth in total-loss frequency that the market is modeling as
cyclical. ADAS-equipped vehicles are 40% more expensive to repair, permanently
raising the share of claims that become total losses — a dynamic consensus
attributes to transient used-car inflation. The thesis catalyzes through Q2
earnings (July) when we expect volume guidance to inflect. We size at 300bps
with a stop at $38 for 2.3:1 risk/reward.

**Variant Perception**: Consensus models total-loss frequency reverting to
18-19% as used-car prices normalize. We believe structural ADAS penetration
floors frequency at 21-22%, independent of used-car values. Our analysis of
150K claims across 3 major insurers shows ADAS-equipped vehicles are totaled
at 1.4x the rate of non-ADAS vehicles at the same age, controlling for value.
The sell-side is anchoring to the pre-ADAS mean.
