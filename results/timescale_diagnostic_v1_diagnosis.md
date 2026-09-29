# Exact time-scale diagnostic — result

## Provenance
GitHub Actions run 36383351714 completed successfully.
The diagnostic contains 18 exact-reference cells; there is no Monte Carlo uncertainty in P1.

## Main result
The predeclared prediction is supported across every population size tested.

For fixed N, increasing T while choosing mu so that M0-O remains at P0=0.5 causes the exact Wright-Fisher fixation probability to move monotonically toward 0.5 and the signed log discrepancy to move monotonically toward zero.

### N=100
E_log: -0.1542, -0.0691, -0.0331, -0.01336, -0.00705, -0.00394 as T increases from 500 to 20000.

### N=200
E_log: -0.3389, -0.1352, -0.0602, -0.02316, -0.01189, -0.00644.

### N=500
E_log: -0.8374, -0.2721, -0.1054, -0.03761, -0.01863, -0.00969.

The short-horizon discrepancy becomes larger with N in this design, while all three series contract strongly with increasing horizon.

## Interpretation
This exact diagnostic supports the mechanism that a finite-horizon origin-fixation approximation can overestimate fixation probability when it collapses segregation/sweep duration into an instantaneous substitution. The experiment isolates this mechanism from route multiplicity, epistasis, multi-step path structure, and Monte Carlo error.

It does not establish a universal scaling law. The next step is to construct and independently test candidate time-scale separation variables rather than selecting a formula solely because it fits these 18 cells.

## Next locked step
Build candidate predictors from quantities specified without fitting E_log:
- successful-origin waiting time, t_wait = 1/(N*mu*p_fix);
- a documented sweep/absorption-time scale t_sweep;
- separation ratio rho = t_wait/t_sweep;
- finite-horizon sweep fraction phi = t_sweep/T.

Then evaluate candidate collapse on a new hold-out grid varying N, s, T and mu. The current 18 cells may be used for mechanism discovery, but the hold-out grid must be used for validation.

No external dataset is required.


## Final manuscript alignment

This is Stage 2 of the final evidence chain. Across all 18 exact cells, discrepancy contracts toward zero as the horizon increases. The result isolates a finite-time mechanism: the reduced chain credits a successful substitution as complete at origin, whereas the explicit finite-population process spends generations segregating before fixation.
