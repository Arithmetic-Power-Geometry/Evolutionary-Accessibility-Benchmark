# Recovery protocol (predeclared)

## Purpose
The first computational checkpoint tests whether the established origin–fixation approximation (M0-O) approaches the matched finite-population Wright–Fisher reference (M1) in a mutation-limited regime.

## Endpoint
The endpoint is **fixation of the all-mutant target genotype by generation T**.

This endpoint is intentionally different from the earlier manuscript's "at least one target individual appears" endpoint. The change is necessary so M0-O and M1 answer the same probability question.

## Shared specification
Initial recovery experiments use:
- haploid populations;
- K=2 binary loci;
- wild-type initial fixation;
- independent forward mutation at unreached loci;
- no back mutation;
- no recombination;
- multiplicative fitness w(g)=(1+s)^k(g);
- all-mutant genotype as the target;
- identical N, mu, s and T wherever defined.

## Approximation M0-O
M0-O is a sequential origin–fixation continuous-time chain over monomorphic genotypes. One-step substitution rates are N*mu*p_fix, with p_fix evaluated using a documented diffusion approximation.

The approximation treats successful substitutions as instantaneous. It should therefore recover M1 only when mutation waiting times dominate sweep durations.

## Reference M1
M1 is an explicit haploid Wright–Fisher process with selection, mutation and multinomial finite-population sampling.

## Predeclared recovery grid
The initial grid is stored in configs/recovery.csv. It is deliberately small and diagnostic. It is not the final phase-map experiment.

## Acceptance logic
Recovery is supported only if discrepancies are compatible with Monte Carlo uncertainty and/or decrease as the process moves further into the approximation-compatible regime. No fixed numerical adequacy threshold is retrofitted after seeing results.

If recovery fails, the next action is model/endpoint/time-scale diagnosis, not expansion to the large benchmark.

## Required diagnostics
- unit tests pass;
- zero-mutation control gives zero target probability;
- mutation matrices are stochastic;
- target is absorbing under the recovery mutation model;
- probabilities lie in [0,1];
- Monte Carlo confidence intervals are reported;
- all seeds and configurations are retained.


## Outcome note

The six-cell recovery benchmark did not establish universal recovery. It motivated the exact Stage-2 mechanism test. This file remains a pre-execution protocol record; final numerical interpretation is in `results/recovery_v1_diagnosis.md` and the manuscript.
