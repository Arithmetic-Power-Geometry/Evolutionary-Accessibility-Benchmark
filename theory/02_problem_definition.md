# Problem definition

## Models and target
Let M0 denote a specified approximation model and M1 a matched finite-population reference model. Both must use the same genotype space, mutation specification, fitness specification, initial state, target definition, and observation horizon wherever their mathematical assumptions permit.

Let `A` be the declared biological target-genotype set. Because the models have different state representations, define model-specific target-state sets: `A0=A` for the monomorphic origin–fixation process and `A1={C : there exists a in A with C_a=N}` for the finite-population genotype-count process. For model `Mj`, define `tau_A^(j)=inf{t>=0 : X_t^(j) in A_j}`.

For parameter vector theta and horizon T, define

P_j(theta) = Pr_{M_j}(tau_A^(j) <= T | X_0^(j), theta),  j in {0,1}.

## Error measures
Primary signed error:

E_log(theta) = log10[(P_1(theta)+epsilon)/(P_0(theta)+epsilon)].

Interpretation:
- E_log > 0: M0 underestimates the reference target probability.
- E_log = 0: agreement on the log-ratio scale.
- E_log < 0: M0 overestimates the reference target probability.

Complementary absolute error:

E_abs(theta) = |P_1(theta)-P_0(theta)|.

A relative-error statistic may be reported where numerically meaningful, but no single metric will be treated as universally sufficient.

epsilon is a numerical regularizer and must be reported explicitly. Sensitivity to its value must be checked when probabilities approach zero.

## Adequacy
For a prespecified tolerance tau,

A_tau = {theta : |E_log(theta)| <= tau}

is the log-ratio adequacy region and

F_tau = {theta : |E_log(theta)| > tau}

is its complement in the evaluated parameter domain.

The interface between these regions is denoted

partial A_tau = {theta : |E_log(theta)| = tau}

when a continuous/interpolated parameter representation makes this boundary meaningful.

Tolerances are analytical choices, not biological constants. Results must be repeated for multiple defensible tolerances.

## Core scientific question
The project does not ask whether stochastic evolutionary dynamics exist. It asks where a simplified model is quantitatively adequate for a specified target-probability question and how that adequacy changes when its assumptions are relaxed.


## Reference-model interpretation and numerical regularization

`M1` is an explicitly resolved finite-population **comparison/reference model**; “reference” does not mean biological ground truth. The frozen computations used `epsilon=2.5e-4` in Stages 1 and 4, `epsilon=1e-12` in exact Stages 2 and 3, and `epsilon=1e-4` in Stage 5. Stage 5 used the primary tolerance `tau=log10(2)=0.30103`, an analytical convention rather than a biological constant.
