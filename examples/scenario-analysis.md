> **Skill**: Scenario Analysis | **Asset Class**: Public Equities
> **Prompt**: "Build bull/base/bear scenarios for CrowdStrike (CRWD) at $310. Key variables: revenue growth, NRR, FCF margin, forward EV/Sales"
> **Analysis Mode**: Surface (public data only)

---

**Subject**: CrowdStrike (CRWD) — Long position at $310  
**Time Horizon**: 12 months  
**Key Variables**: Revenue Growth, Net Revenue Retention (NRR), Free Cash Flow (FCF) Margin, Forward EV/Sales Multiple  
**Base Case Thesis**: Platform consolidation drives steady growth  
**Bull Case Thesis**: TAM expansion into SIEM/observability  
**Bear Case Thesis**: Macro seat optimization and Microsoft E5 competition pressure  

---

## Step 1 — Key Variables Sensitivity Ranking

| Variable        | Current/Consensus | Your Base Case | Sensitivity Rank                  |
|-----------------|-------------------|----------------|---------------------------------|
| Revenue Growth  | 30%               | 30%            | 1 (highest impact on valuation) |
| NRR             | 118%              | 118%           | 2                               |
| FCF Margin      | ~28%              | 28%            | 3                               |
| Forward EV/Sales| ~14x               | 14x            | 4                               |

---

## Step 2 — Define Scenarios

### Bull — TAM Expansion into SIEM/Observability  
**Narrative**: CrowdStrike successfully expands its Total Addressable Market (TAM) by integrating SIEM and observability capabilities, driving higher customer wallet share and accelerating revenue growth. Strong product innovation and cross-selling increase NRR and justify premium valuation multiples.  
**Probability**: 25%  

| Variable        | Assumption | vs. Consensus/Market | Rationale                                             |
|-----------------|------------|----------------------|-------------------------------------------------------|
| Revenue Growth  | 38%        | +8pp                 | TAM expansion and cross-sell accelerate growth       |
| NRR             | 125%       | +7pp                 | Strong customer retention and expansion               |
| FCF Margin      | 32%        | +4pp                 | Operating leverage from scale and efficiency          |
| Forward EV/Sales| 18x        | +4x                  | Premium multiple for growth and TAM expansion         |

**Implied return**: +45% total price appreciation over 12 months (to ~$450)

---

### Base — Steady Platform Consolidation  
**Narrative**: CrowdStrike continues steady execution on its core platform, consolidating market share in endpoint security with moderate growth and stable retention. Valuation multiples remain stable as growth moderates but remains above peers.  
**Probability**: 50%  

| Variable        | Assumption | vs. Consensus/Market | Rationale                                             |
|-----------------|------------|----------------------|-------------------------------------------------------|
| Revenue Growth  | 30%        | In line              | Steady organic growth, no major TAM expansion         |
| NRR             | 118%       | In line              | Stable customer retention                              |
| FCF Margin      | 28%        | In line              | Margins steady with ongoing investments                |
| Forward EV/Sales| 14x        | In line              | Valuation multiple stable                              |

**Implied return**: +18% total price appreciation over 12 months (to ~$366)

---

### Bear — Macro Seat Optimization & MSFT E5 Competition  
**Narrative**: Macro headwinds and aggressive competition from Microsoft E5 bundle lead to customer seat optimization and slower growth. NRR declines as customers churn or reduce spend. Valuation multiples compress due to increased risk and slower growth outlook.  
**Probability**: 25%  

| Variable        | Assumption | vs. Consensus/Market | Rationale                                             |
|-----------------|------------|----------------------|-------------------------------------------------------|
| Revenue Growth  | 22%        | -8pp                  | Seat optimization and competitive pressure            |
| NRR             | 110%       | -8pp                  | Increased churn and lower expansion                    |
| FCF Margin      | 24%        | -4pp                  | Margin pressure from pricing and investments           |
| Forward EV/Sales| 10x        | -4x                   | Multiple contraction due to risk and slower growth     |

**Implied return**: -15% total price depreciation over 12 months (to ~$264)

---

## Step 3 — Calculate Expected Return

| Scenario | Probability | Return (%) | Prob-Weighted Return (%) |
|----------|-------------|------------|--------------------------|
| Bull     | 25%         | +45%       | +11.25%                  |
| Base     | 50%         | +18%       | +9.00%                   |
| Bear     | 25%         | -15%       | -3.75%                   |
| **Total**| **100%**    |            | **+16.5%**               |

**Expected return**: +16.5% over 12 months  
**Risk/Reward Ratio**:  
- Weighted upside = 25% × 45% + 50% × 18% (only positive returns) = 11.25% + 9.00% = 20.25%  
- Weighted downside = 25% × 15% = 3.75%  
- Risk/Reward = 20.25% / 3.75% = **5.4x** (attractive asymmetry)

---

## Step 4 — Sensitivity Table (Revenue Growth × Forward EV/Sales)

**Ranges:**  
- Revenue Growth: Low 22%, Base 30%, High 38%  
- Forward EV/Sales: Low 10x, Base 14x, High 18x  
- Current Price: $310  

| Revenue Growth \ EV/Sales | 10x    | 14x    | 18x    |
|--------------------------|--------|--------|--------|
| **22% (Bear)**            | $220   | $308   | $396   |
| **30% (Base)**            | $300   | $420   | $540   |
| **38% (Bull)**            | $380   | $532   | $684   |

**Implied Return (%) at $310:**

| Revenue Growth \ EV/Sales | 10x     | 14x     | 18x     |
|--------------------------|---------|---------|---------|
| **22% (Bear)**            | -29%    | -1%     | +28%    |
| **30% (Base)**            | -3%     | +35%    | +74%    |
| **38% (Bull)**            | +23%    | +72%    | +120%   |

---

### Break-even Assumptions

**Break-even**:  
- Revenue Growth at **~24%** with Forward EV/Sales at base 14x (return ~0%)  
- Forward EV/Sales at **~11x** with Revenue Growth at base 30% (return ~0%)

---

## Step 5 — Monitoring Framework & Decision Triggers

| Indicator                 | Bull Signal                      | Base Signal                   | Bear Signal                      | Current | Next Data Due  |
|---------------------------|---------------------------------|-------------------------------|---------------------------------|---------|----------------|
| Revenue Growth (YoY)      | >35%                            | 25-35%                        | <25%                            | TBD     | Next earnings  |
| Net Revenue Retention     | >122%                           | 115-122%                     | <115%                           | TBD     | Next earnings  |
| FCF Margin                | >30%                            | 25-30%                       | <25%                            | TBD     | Next earnings  |
| Forward EV/Sales Multiple | >16x                            | 12-16x                       | <12x                           | 14x     | Market data    |
| Competitive Landscape     | Gains share vs MSFT E5          | Stable share                  | Losing share                    | TBD     | Industry news  |
| Macro Environment         | Stable or improving             | Mild headwinds               | Recessionary or severe headwinds| TBD     | Economic data  |

---

### Decision Triggers

- **Increase/Deploy if**:  
  - Revenue Growth > 35% and NRR > 122% for two consecutive quarters  
  - Forward EV/Sales multiple expands above 16x with strong fundamentals  
  - Competitive position strengthens (e.g., wins vs Microsoft E5)  

- **Hold if**:  
  - Revenue Growth between 25-35% and NRR between 115-122%  
  - FCF margin stable or improving  
  - Valuation multiples stable within 12-16x  

- **Reduce/Exit if**:  
  - Revenue Growth < 25% and NRR < 115% for two consecutive quarters  
  - Forward EV/Sales multiple contracts below 12x  
  - Evidence of significant customer churn or competitive losses to Microsoft E5  
  - Macro environment deteriorates sharply (recession signals)  

---

# Summary

- **Expected return**: +16.5% over 12 months with a strong risk/reward ratio of 5.4x  
- **Bull case** drives significant upside via TAM expansion and multiple expansion  
- **Bear case** risks include macro seat optimization and competitive pressure from Microsoft E5  
- **Sensitivity table** reveals break-even revenue growth near 24% and EV/Sales multiple near 11x  
- **Monitoring framework** provides clear, observable triggers to adjust position sizing dynamically  

Please update the current values for revenue growth, NRR, and margins as new earnings and market data arrive to keep the scenario analysis actionable.
