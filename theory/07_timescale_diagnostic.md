# Time-scale separation diagnostic — predeclared protocol

## Question
Does the finite-horizon discrepancy between a sequential origin–fixation approximation and a Wright–Fisher reference contract as the observation horizon becomes long relative to the hidden segregation/sweep time?

## Why one locus
The diagnostic uses K=1 to remove route multiplicity, epistasis, multi-step waiting-time interactions, and Monte Carlo noise. This is a mechanism-isolation experiment, not the final biological benchmark.

## Exact reference
For K=1, M1 is evaluated exactly as a Markov chain over mutant counts 0,...,N. The transition from count i to the next generation is binomial after selection and forward mutation. State N is absorbing. Matrix exponentiation gives the fixation-by-T probability without simulation error.

## Controlled design
N in {100,200,500}; s=0.01; T in {500,1000,2000,5000,10000,20000}.

For every N,T cell, mu is chosen before evaluation so that M0-O predicts the same fixation probability, P0=0.5:

mu = -log(1-0.5)/(N * p_fix * T).

Thus the approximation's cumulative successful-origin opportunity is held fixed while the finite-population reference is allowed to reveal the cost of explicit segregation/sweep time.

## Predictions
If instantaneous substitution is the principal source of the earlier finite-horizon discrepancy, then:
1. P1 should generally lie below P0 at shorter T;
2. E_log should approach zero as T increases for fixed N;
3. the pattern should be systematic across N rather than a Monte Carlo artifact.

These are predictions, not guaranteed outcomes.

## Decision rule
The diagnostic is considered mechanistically supportive if the exact-reference discrepancy contracts consistently with increasing T across population sizes. Failure or non-monotonicity is retained and triggers alternative diagnosis.

No adequacy threshold is fitted from these data. No external dataset is required.
