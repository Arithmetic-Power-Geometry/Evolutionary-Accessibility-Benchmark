# Hold-out time-scale validation — result

## Provenance
GitHub Actions run 36384641998 completed successfully.
The protocol was frozen in theory/08_holdout_timescale_validation.md before these results.
The validation set contains 54 exact Wright-Fisher cells using N and s values absent from the discovery diagnostic.

## Predeclared predictions
1. phi=t_sweep/T should be positively associated with |E_log|.
2. rho=t_wait/t_sweep should be negatively associated with |E_log|.
3. |E_log| should contract with increasing T within (N,s,q) series.

## Results
All three predictions were supported.

Across all 54 hold-out cells:
- Spearman(phi, |E_log|) = 0.9225933364, p = 3.67e-23.
- Spearman(rho, |E_log|) = -0.7372212693, p = 2.06e-10.

Within target-probability strata, phi correlations were 0.9278, 0.9278, and 0.9319 for q=0.25,0.50,0.75. The corresponding rho correlations were -0.9278, -0.9278, and -0.9319.

All 18/18 (N,s,q) series showed monotone contraction of |E_log| as T increased.

## Interpretation
The independently specified hold-out experiment validates time-scale separation as an organizer of finite-horizon approximation error for this one-locus beneficial-substitution model. The especially strong phi result indicates that the fraction of the observation horizon occupied by a simple sweep-time scale is a useful candidate predictor.

This does NOT establish phi as a universal evolutionary law. The result is currently limited to the specified model pair, beneficial one-locus dynamics, forward mutation, constant population size, and the tested parameter domain.

The weaker pooled rho correlation relative to its within-q correlations also matters: target probability level changes t_wait through -log(1-q), so pooling q strata introduces structure not captured by rho alone. This is evidence against prematurely collapsing everything to a single universal predictor.

## Next step
Move from K=1 mechanism validation to a small, predeclared K=2 finite-population boundary experiment. Use phi as a candidate covariate, but do not assume it remains sufficient. Vary mutation supply and horizon independently enough to distinguish sweep-time error from multi-step/segregating-lineage effects.

No external dataset is required for the next experiment.
