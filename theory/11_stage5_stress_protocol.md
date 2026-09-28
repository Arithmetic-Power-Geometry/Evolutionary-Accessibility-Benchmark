# Stage 5 protocol: controlled biological stress test

Status: **PREDECLARED BEFORE STAGE-5 RESULTS**

## 1. Purpose

Stage 4 showed that finite-horizon sweep/segregation time remains an important organizer of K=2 approximation error, but phi alone is insufficient and raw mutation-supply comparisons are confounded by target-probability saturation.

Stage 5 therefore asks a narrower question:

> At baseline parameter settings with non-saturated target probabilities, how do controlled departures from the approximation assumptions change the magnitude and direction of target-probability error, and are paired departures additive or interactive?

This stage does **not** test whether epistasis, route multiplicity, or mutation-rate heterogeneity affect evolution in general. Those effects are established. The estimand is their effect on approximation adequacy.

## 2. Models and endpoint

- Reduced model: M0-O, sequential origin-fixation CTMC.
- Reference model: M1, explicit haploid Wright-Fisher process.
- Genotypes: K=2 binary loci.
- Initial state: population fixed for 00.
- Endpoint: fixation of a declared target set by finite horizon T.
- No recombination.
- Population size constant within a cell.
- Forward mutation unless the perturbation definition explicitly changes mutation rates.
- Both models receive the same biological specification wherever that specification is representable. A perturbation that is intentionally omitted from M0 is labelled an **assumption-mismatch stressor**, not a matched-model comparison.

## 3. Primary error quantities

P0 = Pr_M0(tau_A <= T)
P1 = Pr_M1(tau_A <= T)

E_log = log10[(P1 + epsilon)/(P0 + epsilon)]
E_abs = |P1-P0|

Sign:
- E_log > 0: M0 underestimates M1.
- E_log < 0: M0 overestimates M1.

epsilon = 1/(2R), where R is the Wright-Fisher replicate count.

## 4. Adequacy tolerance

Before results, fix the primary tolerance at

tau = log10(2) = 0.30103.

Thus a cell is called **factor-two adequate** when |E_log| <= tau.

This is an analytical convention, not a biological constant. Sensitivity results will additionally report tau = log10(1.5) = 0.17609 and tau = 0.5, but the primary classification will not be changed after seeing results.

Because Stage 4 errors were mostly much smaller than 0.301, Stage 5 will also report continuous E_log and E_abs; the binary label must not replace the continuous analysis.

## 5. Saturation-aware baseline selection

Use Stage-4 cells only to choose parameter strata, not to fit effects.

Primary baseline strata:
- B1: N=100, s=0.005, T=5,000, N*mu=0.005 (Stage-4 P0 about 0.106)
- B2: N=100, s=0.02, T=5,000, N*mu=0.005 (P0 about 0.399)
- B3: N=300, s=0.005, T=20,000, N*mu=0.005 (P0 about 0.421)
- B4: N=300, s=0.02, T=20,000, N*mu=0.001 (P0 about 0.295)

These span target probabilities roughly 0.1-0.42 while avoiding the severe P≈1 saturation seen at high mutation supply.

The exact same four baselines are used for all stressors.

## 6. Stressor A: route multiplicity

Baseline target: fixation of genotype 11.

Route-multiplicity perturbation: create two declared target outcomes in a K=2 construction, A={10,01}, and compare with a single-route target matched to one member, while preserving the same N, per-locus mutation scale, s and T.

Because this changes the target event itself, report it as a **target-set stress test**, not as evidence that route multiplicity is intrinsically novel.

For the reduced model, target states are absorbing for the target-hitting calculation. For M1, success is fixation of any declared target genotype by T.

Primary contrast:
Delta_R = E_log(route-multiple) - E_log(route-single).

A probability-matched secondary analysis may be added only if its matching rule is specified before simulation.

## 7. Stressor B: epistasis

Use
w(00)=1,
w(10)=w(01)=1+s,
w(11)=(1+s)^2 * exp(eta).

Levels:
- eta=0: multiplicative baseline;
- eta=+0.02: positive epistasis;
- eta=-0.02: negative epistasis.

The same fitness map is supplied to both M0 and M1.

Primary contrasts:
Delta_E+ = E_log(eta=+0.02)-E_log(eta=0)
Delta_E- = E_log(eta=-0.02)-E_log(eta=0)

No monotone direction is predeclared.

## 8. Stressor C: mutation-rate heterogeneity

Use a state-dependent forward mutation rate:
- from 00: mu;
- after the first derived allele (10 or 01): h*mu.

Levels:
- h=1 baseline;
- h=5 elevated second-step mutation;
- h=0.2 reduced second-step mutation.

Both M0 and M1 receive the same state-dependent mutation rule. This tests approximation behavior under heterogeneity rather than deliberately hiding the heterogeneity from M0.

Primary contrasts:
Delta_M5 = E_log(h=5)-E_log(h=1)
Delta_M02 = E_log(h=0.2)-E_log(h=1)

## 9. Paired perturbations and interaction

Use one predeclared non-baseline level per factor for interaction analysis:
- R: multiple target routes;
- E: eta=+0.02;
- M: h=5.

Evaluate pairs R+E, R+M, E+M at all four baselines.

For signed error:
I_ij = E_ij - E_i - E_j + E_0.

Also report the corresponding magnitude interaction
J_ij = |E_ij| - |E_i| - |E_j| + |E_0|
so cancellation in signed error is visible.

Do not label a nonzero Monte-Carlo estimate as mechanistic synergy without uncertainty support.

## 10. Replication and uncertainty

- R=5,000 Wright-Fisher replicates per condition.
- Deterministic seed per baseline × condition.
- Report Wilson 95% intervals for P1.
- For contrasts in E_log and interactions, use a reproducible nonparametric bootstrap over replicate-level success indicators with 2,000 bootstrap draws.
- M0 is deterministic conditional on parameters; Monte-Carlo uncertainty arises from M1.
- If a cell is near a tolerance boundary, increase R using a predeclared adaptive rule: add blocks of 5,000 until the 95% interval for E_log lies wholly on one side of the boundary or R reaches 20,000. Retain all blocks.

## 11. Condition count

Per baseline:
- baseline: 1
- epistasis: 2 non-baseline levels
- mutation heterogeneity: 2 non-baseline levels
- route target stress: 1
- paired positive stressors: 3

Total = 9 conditions per baseline × 4 baselines = 36 primary cells.

The single-route comparator required for the route-target contrast is generated explicitly and retained. If it is not identical to the baseline endpoint, it is counted as an additional control rather than silently reusing the baseline.

## 12. Predeclared questions

Q1. Does each perturbation move signed E_log relative to its matched baseline?
Q2. Does it move |E_log|?
Q3. Does any perturbation change the direction of approximation error?
Q4. Does any cell cross the predeclared factor-two adequacy boundary?
Q5. Are paired perturbation effects compatible with additivity, amplification, or compensation?
Q6. Are conclusions robust to the two secondary tolerance conventions?
Q7. Do effects persist away from P≈0 and P≈1 saturation?

## 13. Falsification / null outcomes

Scientifically valid outcomes include:
- negligible boundary movement;
- perturbations improving approximation;
- sign reversals;
- interactions compatible with zero;
- all cells remaining factor-two adequate.

No condition will be removed because it fails to support the expected narrative.

## 14. Numerical safeguards

All model probabilities must pass the validated probability-boundary helper before:
- error computation;
- confidence-interval membership;
- adequacy classification.

Machine-level excursions within 1e-12 are clamped; larger excursions fail loudly.

Stage-4 cell 32 established why this rule is necessary.

## 15. Stop rule

Do not enlarge Stage 5 after inspecting results merely to obtain boundary crossings. If all 36 cells remain adequate, report that result and use continuous boundary-displacement/error contrasts.

Only implementation defects or predeclared adaptive replication may alter computation.

## 16. External data

No external dataset is used in Stage 5.

LTEE data enter only in Stage 6, after Stage 5 code, configuration, and results are frozen.
