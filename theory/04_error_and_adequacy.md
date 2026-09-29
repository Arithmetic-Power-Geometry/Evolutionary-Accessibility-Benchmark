# Error, adequacy, and boundary analysis

## Why error is signed
Approximation failure is not assumed to have one direction. The study must deliberately identify regimes of underestimation, approximate agreement, and overestimation.

## Primary surfaces
For theta in the evaluated parameter domain, estimate:
- P0(theta)
- P1(theta)
- E_log(theta)
- E_abs(theta)
- uncertainty for simulation-derived quantities

The principal object is the discrepancy surface E_log(theta), not a single maximum discrepancy.

## Adequacy set and sampled boundary
For tolerance tau, estimate the interface between |E_log| <= tau and |E_log| > tau. Boundary estimates must include numerical/Monte Carlo uncertainty and must not imply precision beyond the sampled grid or interpolation method.

## Assumption perturbation
Let a_j index a controlled departure from approximation assumption j. A finite-difference sensitivity can be estimated as

S_j(delta) = [E(theta + delta e_j) - E(theta)] / delta,

where the parameterization makes this interpretation meaningful.

## Interactions
For a baseline E0, single perturbations Ei and Ej, and joint perturbation Eij,

I_ij = Eij - Ei - Ej + E0.

Because E_log is signed, an analogous analysis on |E_log| or E_abs must accompany interaction claims where cancellation could otherwise hide large errors.

## Boundary displacement
If adequacy boundaries are well resolved, quantify how a perturbation changes their location. The distance metric must be declared before use and validated for the geometry of the estimated boundary.

## Scaling search
Candidate control variables include mutation-supply and scaled-selection quantities such as N*mu, N*s, and horizon-scaled mutation opportunity. These are hypotheses to test, not assumed universal scaling laws.

A successful collapse of multiple raw parameter combinations onto a lower-dimensional discrepancy surface would be treated as an empirical/theoretical result only after out-of-sample or held-out validation.


## Final manuscript implementation

For Stage 5, write `E=E_log`. Single-factor contrasts are `Delta_i=E_i-E_0`; for a paired perturbation `Delta_ij=E_ij-E_0`, and the signed interaction is `I_ij=E_ij-E_i-E_j+E_0`. The final manuscript reports these signed contrasts and does not use the earlier proposed magnitude-interaction statistic. No factor-two boundary was crossed in the frozen Stage-5 domain, so the paper reports bounded-domain adequacy and discrepancy responses rather than claiming a resolved universal boundary.
