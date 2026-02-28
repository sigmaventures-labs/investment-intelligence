# Scenario & Sensitivity Analysis — Private Equity

## Key Variables (Typical High-Sensitivity)

1. **Entry multiple** — Price paid. The single biggest determinant of returns.
   Always sensitivity-test even if "agreed."
2. **Revenue CAGR** — Organic + inorganic growth through hold period.
3. **EBITDA margin at exit** — Reflects operational value creation achievement.
4. **Exit multiple** — Terminal value driver. Must justify vs. entry.
5. **Leverage** — Amplifies equity returns but adds fragility.
6. **Hold period** — Longer holds compress IRR even if MOIC rises.

## Return Metrics

Present ALL of:
- **Gross IRR**: Pre-fee, pre-carry return to the fund
- **Net IRR**: After management fee and carry
- **Gross MOIC**: Total value / invested capital
- **Net MOIC**: After fees and carry
- **DPI**: Distributions to paid-in (realized return)

## Returns Bridge

Decompose gross IRR into value creation components:

```
### Returns Bridge — Base Case

| Component | Contribution to MOIC | Notes |
|-----------|---------------------|-------|
| Revenue growth | [X.Xx] | Organic [X.Xx] + M&A [X.Xx] |
| Margin expansion | [X.Xx] | From [X]% to [X]% EBITDA |
| Multiple expansion | [X.Xx] | Entry [X]x → Exit [X]x |
| Leverage / deleveraging | [X.Xx] | Entry [X]x → Exit [X]x |
| Fees & transaction costs | ([X.Xx]) | |
| **Total Gross MOIC** | **[X.Xx]** | **Gross IRR: [X]%** |
```

## Decision Rules

- Gross IRR > 20-25% (typical buyout hurdle)
- Gross MOIC > 2.0-2.5x
- Downside case must return capital (>1.0x MOIC) — cannot lose money
- No more than 40% of return from multiple expansion alone (must be
  grounded in operational value creation)
- Returns should be attractive even if hold period extends 1-2 years

## Sensitivity Table Format

```
### Gross IRR: [Exit Multiple] × [Exit EBITDA]

|                    | $[XX]M  | $[XX]M  | $[XX]M  |
|--------------------|---------|---------|---------|
| **[X-1]x exit**    | [IRR]%  | [IRR]%  | [IRR]%  |
| **[X]x exit**      | [IRR]%  | [IRR]%  | [IRR]%  |
| **[X+1]x exit**    | [IRR]%  | [IRR]%  | [IRR]%  |
```

Also produce: **Entry Multiple × Exit Multiple** (shows how sensitive
returns are to spread) and **Revenue CAGR × Margin at Exit**.

## PE-Specific Scenario Design

Scenarios should decompose along the value creation plan:

- **Bull**: Full value creation plan + bolt-ons execute + exit into strong
  M&A market. All levers work. Multiple expands.
- **Base**: Organic plan on-track, 1-2 bolt-ons vs. planned 3-4, margin
  improvement partially achieved. Exit at entry multiple.
- **Bear**: Revenue growth disappoints, margin plan stalls, no bolt-ons,
  exit delayed 1-2 years. Exit at discount to entry.
- **Downside floor**: Operations flat, no value creation, exit at entry
  multiple with some deleveraging. Tests whether you can return capital.

Key PE scenario nuance: **IRR is non-linear with time.** A 2.5x MOIC in
3 years = ~36% IRR. The same 2.5x in 5 years = ~20% IRR. Always show
how returns change if hold period extends.

## Portfolio / Fund-Level Scenarios

For fund-level stress tests, model each portfolio company under macro regimes:

| Portfolio Co | Equity | Leverage | Base IRR | Recession | Rate Shock | Ops Fail |
|-------------|--------|----------|----------|-----------|------------|----------|
| **Fund Total** | $[X]M | [Avg]x | **[IRR]%** | **[IRR]%** | **[IRR]%** | **[IRR]%** |

Include MOIC alongside IRR. LP reporting typically emphasizes MOIC for
unrealized and IRR for realized.
