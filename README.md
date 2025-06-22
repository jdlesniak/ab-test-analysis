# A/B Test Analysis — Multi-Level Headline Experiments

This repository contains a structured analysis of Upworthy-style A/B tests involving multiple headline variants. The goal is to:

1. Perform omnibus chi-squared tests per experiment (2+ variants).
2. Identify winning headlines when statistically significant.
3. Compute observed effect size and power based on real data.
4. Highlight risks of false conclusions due to low statistical power.

## Purpose

- Analyze A/B tests with two or more headline variants.
- For each test:
  - Run a chi-squared omnibus test to evaluate overall significance.
  - If significant, determine the winning headline.
  - Compute observed effect size (Cohen’s w) and estimate power based on total traffic.
- Surface potential pitfalls: low-powered tests may still yield false-positive “winners.”

## Key Findings (see `02_testing.ipynb`)

- Many seemingly successful tests (p < 0.05) have **under 50% power**.
- A significant p-value in a low-powered test *does not guarantee reliability*—there’s a high chance it’s a false positive.
- Tests with small effect sizes and/or low traffic show notable risk of drawing incorrect conclusions.
- **Recommendation**: Prior to concluding a “winner,” ensure power ≥ 0.8 to reduce false discovery risk.
