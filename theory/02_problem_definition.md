# Problem definition

## Models and target
Let M0 denote a specified approximation model and M1 a matched finite-population reference model. Both must use the same genotype space, mutation specification, fitness specification, initial state, target definition, and observation horizon wherever their mathematical assumptions permit.

Let A be a target set and let

tau_A = inf{t : X_t enters A}

be its first hitting time.

For parameter vector theta and horizon T, define

P_j(theta) = Pr_{M_j}(tau_A <= T | X_0, theta),  j in {0,1}.

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
