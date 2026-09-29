# Stage 6 empirical LTEE stress-evidence protocol

Status: **FROZEN BEFORE STAGE-6 OUTCOME ANALYSIS**

## Purpose

Stage 6 is an empirical stress-evidence stage, not a validation of the mathematical approximation framework. It asks whether biological features represented by controlled Stage-5 perturbations are observed in a long-term experimental-evolution system.

## Source currently supplied

Dryad DOI **10.5061/dryad.6226d**, original archive supplied unchanged by the author.

The archive contains the files required for the first two empirical questions, including:
- LTEE_Mutator_info.txt
- MutationTypesThroughTime.txt
- spectrum_counts.csv
- count.LTEE.final_masked.csv
- the full mutation table and associated source scripts.

No Stage-6 numerical outcome was inspected before freezing the analysis rules below, apart from file names, headers, and format needed to establish feasibility.

## E1 — mutation-rate-state heterogeneity

Use the supplied mutator-status metadata and mutation-count data. At the latest common generation with appropriate observations, compare accumulated mutation burden between populations/clones classified as point mutators and non-mutators.

Report:
- group sizes;
- individual observations;
- medians and interquartile ranges;
- median ratio when defined;
- exact two-sided Mann–Whitney test for the prespecified two-group comparison.

Interpretation is descriptive evidence that a constant-mutation-rate assumption can be biologically violated. It is not evidence that mutation-rate heterogeneity necessarily makes an approximation inadequate.

## E2 — mutation-spectrum heterogeneity

Construct a prespecified mutation-spectrum vector from the mutation categories provided by the source data. For each eligible observation, convert category counts to proportions and calculate Shannon entropy

H = - sum_i p_i log(p_i)

over nonzero categories.

Compare point-mutator and non-mutator groups at the same endpoint used in E1. Report individual values, group medians/IQR, and an exact two-sided Mann–Whitney comparison.

This is a descriptive measure of spectrum concentration, not a universal measure of evolutionary complexity.

## E3 — route multiplicity

The currently supplied 6226d archive will not be forced to answer a route-multiplicity question that it does not directly encode. The Cit+ route analysis will be performed only from a source that explicitly supports the relevant independent Cit+ mutational routes. If the second archived source (Dryad 10.5061/dryad.8q6n4) is required, it will be acquired before E3 and its files will be inventoried before analysis.

## Claim discipline

Stage 6 may support statements that LTEE data exhibit mutation-state/spectrum heterogeneity and, if independently sourced, multiple routes to a phenotype.

Stage 6 must not be used to claim:
- that LTEE proves the approximation-error framework;
- that these empirical features necessarily cross the factor-two adequacy tolerance;
- that the empirical observations are causal estimates of Stage-5 perturbation effects;
- that the selected LTEE populations represent all evolving populations.

## Stop rule

After E1, E2, and E3 (if supported by the dedicated route dataset), Stage 6 ends. No additional empirical endpoint will be mined merely because it gives a stronger contrast. After Stage 6 the project proceeds to manuscript construction unless a reproducibility defect is discovered.


---

## Post-execution record for manuscript alignment

Stage 6 was completed without adding further empirical endpoints. At generation 50,000, population-level mutation burden differed between six point-mutator and six nonmutator LTEE populations (medians 1210.5 vs 80.0; 15.13-fold; exact two-sided Mann–Whitney `U=36`, `p=0.0021645`). Mutation-spectrum Shannon entropy also differed (medians 0.513582 vs 1.236223; `U=0`, `p=0.0021645`). The dedicated Dryad `10.5061/dryad.8q6n4` source listed 14 independent Cit+ mutants across two structural-event classes: 8 variant `cit` duplications and 6 IS3 insertions.

The final manuscript uses these results only as independent empirical evidence that mutation-state heterogeneity, mutation-spectrum differences, and alternative structural routes occur in a real long-term evolutionary system. They are not presented as causal validation of the Stage-5 discrepancy responses.
