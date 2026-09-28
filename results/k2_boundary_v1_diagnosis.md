# K=2 adequacy-boundary experiment: v1 diagnosis

## Provenance
Workflow run 36389065932 completed successfully on commit 14156a05b3d64f4ea8c5249220b599d1b2c34202. Artifact: k2-boundary-results (10956653505). The predeclared 32-cell design and 2,000 Wright–Fisher replicates per cell were retained.

## Main results

The K=2 experiment does not support a one-variable account in which sweep-time fraction alone determines finite-horizon approximation error.

Across all 32 cells, Spearman correlation between phi=t_sweep/T and |E_log| was rho=0.5761 (p=5.60e-4). Thus larger sweep-time fraction is associated with larger discrepancy, consistent with the K=1 time-scale diagnostic, but the association is not sufficient to describe all K=2 behavior.

At fixed mutation-supply level, the phi relationship was especially strong for lambda=N*mu >=0.005: rho=0.9762 for lambda=0.005 and 0.02, and rho=0.9524 for lambda=0.05. For lambda=0.001 the eight-cell correlation was weaker (rho=0.5476, p=0.160), where probabilities are often small and Monte Carlo uncertainty is proportionally larger.

Horizon extension from T=5,000 to T=20,000 reduced |E_log| in 15 of 16 matched (N,s,N*mu) pairs. The single exception was N=300, s=0.005, N*mu=0.001, where |E_log| increased from 0.0567 to 0.1125. This cell has only 6 and 55 WF fixation hits at the two horizons and should be treated as a low-probability diagnostic rather than used to overturn the broader time-scale pattern.

The signed discrepancy was not restricted to one direction: 20 cells had E_log<0, 11 had E_log>0, and one saturated cell had E_log=0. Thus the approximation can overestimate or underestimate the finite-population target probability, although negative discrepancies predominate in this grid.

The origin-fixation estimate lay inside the 95% Wilson interval for the Wright–Fisher estimate in 20 of 32 raw cells. This is a Monte Carlo agreement diagnostic, not the definition of an adequacy boundary.

## Mutation supply

The pooled correlation between N*mu and |E_log| was negative (Spearman rho=-0.7265, p=2.50e-6), but this must NOT be interpreted as evidence that increasing mutation supply generally improves origin-fixation accuracy. The grid contains strong probability saturation at high N*mu: many high-supply cells have P0 and P1 near 1, mechanically compressing absolute and log discrepancies.

Therefore N*mu contributes structure, but its effect is conditional on horizon, selection, population size, and event-probability saturation. Stage 5 must avoid a naive monotone N*mu claim and should include probability-matched or otherwise saturation-aware contrasts.

## Important numerical note

Cell 32 stores raw p0=1.0000000000000002 from matrix-exponential floating-point roundoff while the error metric correctly clamps machine-level boundary noise. Its raw p0_inside_wf_ci flag is consequently False because the Wilson upper endpoint is 0.9999999999999998. This is a numerical comparison artifact, not biological disagreement. Future result scripts should use the validated/clamped probability for CI-membership comparisons as well as for error metrics.

## Interpretation

The K=1 result generalizes partially: hidden sweep/segregation time remains an important organizer of finite-horizon approximation error. But K=2 introduces additional structure. In particular, mutation supply and multi-step lineage dynamics cannot be summarized safely by phi alone, and saturation can hide discrepancies.

This is exactly the motivation for the next controlled stage: perturb biological assumptions while matching or stratifying baseline target probabilities so that boundary movement is not confounded by trivial P≈0 or P≈1 saturation.

## Decision

Stage 4 is complete. Do not enlarge this grid post hoc.

Proceed to a predeclared Stage-5 factorial stress test. The design should:
1. retain a matched K=2 baseline;
2. perturb route multiplicity, epistasis, and mutation-rate heterogeneity separately;
3. include selected paired perturbations for interaction contrasts I_ij;
4. use saturation-aware baseline cells, preferentially with intermediate target probabilities;
5. preserve signed E_log and E_abs;
6. define the adequacy tolerance before seeing Stage-5 results;
7. quantify boundary displacement rather than merely asking whether each biological feature affects evolution.

No external empirical dataset is required for Stage 5. LTEE data should enter only after this controlled stress test is frozen and completed.
