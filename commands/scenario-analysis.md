# Scenario Analysis

Build a scenario and sensitivity analysis for:

$ARGUMENTS

Refer to @.cursor/skills/scenario-analysis/SKILL.md for the core framework, then load the public equities variables and return metrics: @.cursor/skills/scenario-analysis/references/public-equities.md

Follow the full framework:
1. Identify 2-5 highest-sensitivity variables using asset-class-specific variable list
2. Define 3-5 scenarios (all variables specified, internally consistent, base = your view)
3. Probability-weighted expected return using asset-class-specific metric (stock return / IRR+MOIC / levered+unlevered IRR)
4. Sensitivity tables for top 2 variables highlighting cliff edges and break-even
5. Monitoring dashboard with thresholds
6. Decision triggers for increase/hold/reduce/exit

Show implied return at current price.

Note: Real estate and private equity overlays are in development and will be available in a future release.
