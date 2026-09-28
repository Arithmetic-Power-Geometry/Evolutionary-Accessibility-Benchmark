# Testable hypotheses and falsification criteria

These hypotheses are frozen before the expanded benchmark is run. They are directional only where theory justifies direction.

## H1 — Recovery
As the finite-population reference process approaches the assumptions of the selected approximation model, discrepancy should approach the simulation/numerical error floor.

Falsification signal: persistent, reproducible discrepancy after implementation error, finite-horizon mismatch, and numerical uncertainty are excluded.

## H2 — Departure from mutation-limited conditions
Leaving the mutation-limited regime can change approximation error.

No universal sign is assumed.

## H3 — Route multiplicity
Changing the number or structure of routes to a common target set can change approximation error relative to a model that does not represent the same route structure.

No claim is made that additional routes universally increase signed error.

## H4 — Mutation-process heterogeneity
State- or time-dependent mutation processes can shift the location of an adequacy boundary relative to an otherwise matched stationary approximation.

## H5 — Epistasis
Epistatic landscape structure can alter both magnitude and sign of approximation error. No monotone relationship is assumed a priori.

## H6 — Interactions
Joint assumption departures need not equal the sum of their separate effects. Amplifying, approximately additive, and compensating regimes are all admissible outcomes.

## H7 — Reduced control variables
A lower-dimensional set of scaled variables may predict a substantial fraction of adequacy-boundary location across raw parameter combinations.

This is an exploratory-but-predeclared hypothesis. Failure to obtain a robust collapse is a valid result.

## Required negative controls
The benchmark must contain:
- regimes expected to agree;
- regimes in which M0 underestimates M1;
- searches for regimes in which M0 overestimates M1;
- parameter combinations with negligible effects;
- replicate/convergence controls.

## Reporting rule
All evaluated parameter cells are retained in machine-readable output. Results are not filtered to retain only large discrepancies or hypothesis-supporting cases.
