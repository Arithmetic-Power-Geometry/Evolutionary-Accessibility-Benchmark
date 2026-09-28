# Recovery experiment 1 — locked result and diagnosis

## Provenance
GitHub Actions run: 36381859390
Commit: b5555ebd91933f14755bdd0180ab8434f24a17a9
Workflow conclusion: success
Replicates per cell: 2,000
Raw output: results/recovery_v1.csv

## Result
The first recovery experiment is informative but does **not** justify declaring universal recovery.

Three cells show close numerical agreement (especially N=100, mu=1e-5 and N=500, mu=1e-5). In three cells the origin–fixation estimate is above the upper 95% Wilson interval of the Wright–Fisher estimate, or marginally so. Across all six cells E_log ranges from about -0.053 to +0.0003, so the approximation is mostly biased toward overestimating finite-horizon fixation in this grid.

This direction is consistent with a plausible finite-time mechanism: M0-O treats successful substitutions as instantaneous, whereas M1 spends generations in segregating/sweeping states. That explanation is a diagnosis to test, not a conclusion established by this six-cell experiment.

## Important structure in the grid
The paired configurations keep the origin–fixation cumulative opportunity approximately matched while doubling mu and halving T. M0-O therefore gives the same P0 within each N pair, while M1 can respond to the shorter horizon and explicit sweep duration.

Observed paired E_log:
- N=100: -0.0033 at mu=1e-5,T=20000; -0.0529 at mu=2e-5,T=10000.
- N=200: -0.0379; -0.0410.
- N=500: +0.0003; -0.0215.

The pattern is suggestive but not perfectly monotone, so it must not be overstated.

## Decision
H1 is **not rejected**, but it is also **not yet established**. Before the large phase map, run a dedicated time-scale diagnostic that separates mutation waiting time from sweep duration and checks whether error contracts when their ratio increases.

## Next predeclared diagnostic
Define a dimensionless separation quantity based on expected successful-mutant waiting time and an independently estimated/approximated sweep-time scale. Vary this separation while holding other quantities as controlled as practical.

The next experiment must:
1. include the original six cells as anchors;
2. include lower-mutation / longer-horizon cells;
3. report runtime and Monte Carlo uncertainty;
4. retain all cells;
5. test whether E_log approaches zero as time-scale separation increases;
6. avoid fitting a threshold until the diagnostic data are generated.

No external empirical dataset is required for this diagnostic.
