# Hold-out validation of time-scale predictors — predeclared protocol

## Status
This protocol is frozen before generation of the hold-out results. The 18 cells in timescale_diagnostic_v1.csv are discovery/mechanism data and are not the validation set.

## Question
Can a dimensionless time-scale quantity predict the magnitude of finite-horizon origin–fixation error on unseen population sizes, selection coefficients, horizons, and target probability levels?

## Candidate quantities fixed before validation
For a beneficial one-locus substitution:
- successful-origin waiting time: t_wait = 1 / (N * mu * p_fix)
- deterministic sweep scale: t_sweep = 2*log(N-1) / log(1+s)
- waiting/sweep separation: rho = t_wait / t_sweep
- horizon sweep fraction: phi = t_sweep / T

The sweep scale is a deliberately simple logistic benchmark: it is the time for log-odds to move from approximately 1/(N-1) to N-1 under per-generation log fitness advantage log(1+s). It is not claimed to equal the exact conditional Wright-Fisher absorption time.

## Hold-out grid
All N and s values are unseen in the discovery diagnostic:
- N in {75, 150, 300}
- s in {0.005, 0.02}
- T in {1000, 5000, 20000}
- target M0-O probability q in {0.25, 0.50, 0.75}

For each cell, mu is chosen analytically so that M0-O predicts q:
mu = -log(1-q)/(N*p_fix*T).

Total: 54 exact-reference cells.

## Reference
M1 is the exact K=1 Wright-Fisher count-state Markov chain already validated in the mechanism diagnostic. No Monte Carlo sampling is used.

## Predeclared validation tests
Primary qualitative prediction:
- larger phi should correspond to larger |E_log|;
- larger rho should correspond to smaller |E_log|.

Report:
1. Spearman rank correlation of phi with |E_log| across all hold-out cells;
2. Spearman rank correlation of rho with |E_log|;
3. the same correlations within each q stratum;
4. monotonicity of |E_log| as T increases within each (N,s,q) series;
5. all 54 cells, including failures and reversals.

No threshold is fitted from the hold-out data. No predictor is renamed a law on the basis of this experiment.

## Success criterion
Support requires the predicted correlation signs globally and in a clear majority of q strata, plus predominantly monotone contraction with increasing T. Exact numerical strength is reported rather than retrofitting a cutoff.

## External data
None required.
