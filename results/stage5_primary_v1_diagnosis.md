# Stage 5 primary stress test: v1 diagnosis

## Provenance

Corrected sharded workflow run **36424797701** completed successfully on commit **b58756de8fd27ff8c6c45cb9fa1b38bad4108a63**. All four frozen baseline shards B1-B4 succeeded. The preceding unsharded run 36403211328 was cancelled at the 180-minute infrastructure timeout during simulation; tests had passed and no scientific parameter was changed. Sharding altered execution only.

Artifacts and SHA-256 digests:
- B1 artifact 10972462895: 27d2a4c3cece18e696e52f31e97b7d1d7cea5c4c79479121034377f3db750a84
- B2 artifact 10972856574: f4692d55fe2e48a96539bb09c3b261aa6669714556780df5d545850a53367045
- B3 artifact 10973996662: 0ba3213ff0caee54b43a3e68a718dc8dfb3a1bdd39624e3ae789a8b76009d195
- B4 artifact 10977355843: 7f76a5024856d5770e205c97b674afd2eaac5457b0fdaa638b39b58aae32b4d2

Each of the 36 frozen conditions used 5,000 Wright-Fisher replicates and retained replicate-level binary outcomes.

## Primary adequacy result

All **36/36 cells** remained within the factor-two adequacy tolerance fixed in the computational specification before primary execution

|E_log| <= log10(2) = 0.30103.

The largest observed |E_log| was **0.17996**, in B3 under negative epistasis. Therefore Stage 5 provides no factor-two boundary crossing in the tested domain. Per the predeclared stop rule, the grid will not be enlarged merely to manufacture a crossing.

Signed errors were predominantly negative: **33/36 negative and 3/36 positive**. Thus M0-O usually overestimated the finite-population target probability in this grid, but sign reversal is possible.

## Individual perturbations

Across the four baselines, multiple-target perturbation, positive epistasis, and elevated second-step mutation generally produced modest changes in signed approximation discrepancy. Negative epistasis generated the largest single observed change, especially B3, but that B3 target probability is extremely small and its bootstrap uncertainty is correspondingly broad.

No universal monotone direction should be claimed for any single perturbation.

## Predeclared 2,000-draw bootstrap contrasts

The bootstrap analysis used deterministic seed 20260928 and resampled the retained Wright-Fisher success indicators independently within condition.

Most single-factor contrast intervals included zero.

Notable paired-interaction results:
- B2 route + elevated mutation: I_RM = -0.05325, 95% bootstrap CI [-0.07292, -0.03503].
- B3 route + positive epistasis: I_RE = -0.03501, 95% CI [-0.05251, -0.01799].
- B3 route + elevated mutation: I_RM = -0.03953, 95% CI [-0.05814, -0.02160].

Other predeclared interaction intervals included zero or were borderline. These are approximation-discrepancy interactions, not claims of novel biological epistasis or synergy.

## Interpretation

Stage 5 supports a deliberately narrower conclusion than a universal failure-boundary claim.

Within four saturation-aware K=2 baseline regimes and the frozen perturbation magnitudes, the origin-fixation approximation remained factor-two adequate for every tested condition. Biological departures nevertheless moved the signed approximation discrepancy, and selected paired perturbations produced reproducible non-additive changes in error.

Therefore the useful object is not simply a binary statement that origin-fixation fails. It is the **model- and endpoint-specific approximation discrepancy response** and how controlled assumption changes move that response.

The absence of a factor-two crossing is scientifically informative and is retained as a negative result.

## Claim discipline

Do not claim:
- a universal evolutionary adequacy boundary;
- that multiple-target perturbation, epistasis, or mutation-rate heterogeneity are new mechanisms;
- that Stage 5 proves these factors generally increase approximation discrepancy;
- that the significant interaction contrasts are universal biological interactions.

Safe statement:

> In the tested finite-horizon K=2 regimes, origin-fixation remained within a predeclared factor-two tolerance, while controlled biological perturbations changed the magnitude and occasionally the direction of target-probability error; selected paired perturbations produced non-additive error responses.

## Decision

**Stage 5 is complete. Do not enlarge the simulation grid post hoc.**

Proceed to Stage 6 empirical LTEE stress evidence. Stage 6 should test whether approximation-relevant features represented in the controlled study occur in long-term experimental evolution data; it must not be presented as proving the mathematical approximation framework.


## Final manuscript alignment

The final manuscript reports this stage conservatively. The `{10,01}` condition is a **multiple-target perturbation**: relative to the baseline target `{11}`, it changes the target set and mutational depth. The primary runner did not generate the single-route comparator proposed in the frozen protocol, so no clean causal route-multiplicity contrast is claimed. Final interaction reporting uses the signed contrast `I_ij = E_ij - E_i - E_j + E_0`; the unused magnitude contrast proposed during protocol development is not part of the manuscript analysis. “Predeclared” means fixed in the computational specification before primary Stage-5 execution, not externally preregistered.
