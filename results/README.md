# Frozen results

This directory records the outputs used to evaluate the matched finite-horizon target-probability benchmark.

## Core result files

- `recovery_v1.csv`: six-cell matched K=2 recovery diagnostic.
- `timescale_diagnostic_v1.csv`: 18 exact K=1 finite-time diagnostic cells.
- `timescale_holdout_summary_v1.csv`: predeclared hold-out correlation and monotonicity summary.
- `k2_boundary_v1.csv`: 32-cell K=2 benchmark.
- `stage5_primary_v1_diagnosis.md`: frozen interpretation of the 36-cell Stage-5 stress experiment.
- `stage6_ltee_e1_e2_v1.md`: frozen LTEE mutation-state and mutation-spectrum results.
- `stage6_ltee_e3_v1.md`: frozen Cit+ route result.

Result-diagnosis files distinguish descriptive observations from broader claims and preserve null or adverse results.

## Stage-5 primary workflow

GitHub Actions run **36424797701** completed successfully after the unchanged scientific design was sharded by baseline for runtime. The preceding unsharded run **36403211328** reached its 180-minute infrastructure timeout. No scientific parameter was changed to obtain the successful run.

The primary Stage-5 conclusion is intentionally negative with respect to the frozen factor-two threshold: **36/36 cells remained adequate under the predeclared tolerance** (|E_{\log}|\le\log_{10}(2)). This result must not be replaced by post-hoc grid expansion merely to create a threshold crossing.

## Empirical evidence

The LTEE files summarize analyses of public Dryad datasets **10.5061/dryad.6226d** and **10.5061/dryad.8q6n4**. These observations establish biological occurrence of mutation-state heterogeneity, mutation-spectrum differences, and alternative Cit+ structural route classes. They do not causally validate the simulated approximation-error responses.
