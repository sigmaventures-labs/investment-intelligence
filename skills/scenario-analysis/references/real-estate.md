# Scenario & Sensitivity Analysis — Real Estate

## Key Variables (Typical High-Sensitivity)

1. **Exit cap rate** — Usually THE most sensitive variable. A 25bps move can
   swing returns by 200+ bps of IRR.
2. **Rent growth / mark-to-market** — Revenue driver. Compound effect over hold.
3. **Vacancy / occupancy** — Directly impacts NOI. Lease-up assumptions are
   frequently too aggressive.
4. **Financing rate** — Cost of debt at acquisition and refinancing. Floating
   rate exposure amplifies sensitivity.
5. **Capex / TI budget** — Execution cost of the business plan. Overruns
   directly reduce equity returns.

## Return Metrics

Present ALL of:
- **Unlevered IRR**: Return on total capital (asset-level performance)
- **Levered IRR**: Return on equity (what investors actually earn)
- **Equity multiple (MOIC)**: Total distributions / equity invested
- **Cash-on-cash yield**: Annual cash flow / equity invested (by year)
- **Peak equity exposure**: Maximum capital at risk including capex

## Decision Rules

- Levered IRR > fund hurdle (typically 8% pref + promote structure)
- Unlevered IRR > weighted average cost of capital
- Equity multiple > 1.5x for core-plus, > 1.8x for value-add, > 2.0x for
  opportunistic (calibrate to strategy)
- Must generate >1.0x in downside case (return of capital)
- Cash-on-cash must service any fund-level obligations

## Sensitivity Table Format

```
### Levered IRR: [Exit Cap Rate] × [Rent Growth]

|                    | 5.0%    | 5.5%    | 6.0%    | 6.5%    |
|--------------------|---------|---------|---------|---------|
| **Rent +4%/yr**    | [IRR]%  | [IRR]%  | [IRR]%  | [IRR]%  |
| **Rent +3%/yr**    | [IRR]%  | [IRR]%  | [IRR]%  | [IRR]%  |
| **Rent +2%/yr**    | [IRR]%  | [IRR]%  | [IRR]%  | [IRR]%  |
| **Rent +1%/yr**    | [IRR]%  | [IRR]%  | [IRR]%  | [IRR]%  |
```

Also produce: **Exit Cap Rate × Vacancy at Stabilization** and
**Financing Rate × Exit Cap Rate** sensitivity tables.

## RE-Specific Scenario Design

Scenarios should be framed around the business plan, not just macro:

- **Bull**: Business plan over-achieves (faster lease-up, higher rents,
  below-budget capex) + favorable exit market
- **Base**: Business plan largely on-track with normal friction
- **Bear**: Lease-up delays, rent growth misses, capex overruns, exit
  market is soft (wider cap rates)
- **Stress / Downside floor**: What if we can't execute the business plan
  at all and just hold the asset as-is? Can we return capital?

## Portfolio-Level Scenarios

For fund/portfolio stress tests:

| Asset | Equity | Soft Landing | Recession | Rate Shock (+200bps) | Stagflation |
|-------|--------|--------------|-----------|----------------------|-------------|
| **Fund Total** | $[X]M | **[IRR]%** | **[IRR]%** | **[IRR]%** | **[IRR]%** |
