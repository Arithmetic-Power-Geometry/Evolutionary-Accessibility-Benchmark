# Novelty audit: approximation adequacy and finite-population target probabilities

Status: literature boundary frozen before Stage 5. This is a claim-discipline document, not a claim of exhaustive priority.

## Question audited
Has prior evolutionary theory already established the proposed object: a signed discrepancy surface between a specified simplified evolutionary probability model and a finite-population reference target-hitting/fixation probability, together with tolerance-dependent adequacy regions/boundaries and perturbation/interactions analysis?

## Established prior work — not novel

### Genotype findability
McCandlish (2013), *On the Findability of Genotypes*, Evolution 67:2592–2603, DOI 10.1111/evo.12128.
For weak mutation on a time-invariant fitness landscape, genotype findability is defined through expected waiting/hitting time to fixation. Mutation, selection, substitution rate and reversion contributions are analyzed.
**Claim prohibited:** inventing genotype findability, evolutionary hitting times, or Markov-chain accessibility.

### Origin–fixation theory and its restricted domain
McCandlish & Stoltzfus (2014), *Modeling evolution using the probability of fixation: history and implications*, Quarterly Review of Biology 89:225–252, DOI 10.1086/677571.
Origin–fixation is an established theory of mutation-limited evolution. The review explicitly identifies how accurately such models approximate natural-population evolution as an important unresolved question.
**Claim prohibited:** inventing origin–fixation or the question of approximation validity.

### Waiting time versus fixation/sweep time
Prior work explicitly separates waiting time for successful mutation from fixation time and identifies mutation-limited versus fixation-time-limited regimes. Kopp & Hermisson's moving-optimum work and valley-crossing work make this timescale distinction explicit.
**Claim prohibited:** presenting waiting-time/sweep-time separation itself as new.
**Our permitted use:** use the ratio as a predeclared explanatory variable for a different response variable: finite-horizon target-probability approximation discrepancy.

### SSWM breakdown, clonal interference and mutation supply
A large literature shows that successive-fixation assumptions break when mutations arise before prior sweeps complete; N*mu and related quantities organize periodic-selection versus interference regimes.
**Claim prohibited:** inventing the SSWM/interference boundary or claiming N*mu as a new control parameter.

### Fitness-landscape accessibility
Prior work studies accessible paths, peak accessibility, population-size effects, and Wright–Fisher/Moran adaptive walks.
**Claim prohibited:** claiming evolutionary accessibility, path accessibility, peak accessibility, or population-size-dependent landscape navigation as new.

## Closest overlap found

1. Regime-boundary studies partition parameter space according to which timescale/process dominates.
2. Clonal-interference studies derive thresholds between periodic selection and interference.
3. Approximation papers compare simplified evolutionary processes with more detailed stochastic models.
4. Fitness-landscape papers quantify accessibility and population-size effects.
5. Findability theory quantifies genotype hitting/waiting times in weak-mutation Markov models.

These are substantive neighbors and must be cited.

## Distinction to test, not assume

In the literature examined for this audit, we did **not** identify the exact combined construction used here:

- define the same finite-horizon target event under M0 and M1;
- quantify signed probability error
  E_log = log10[(P1+epsilon)/(P0+epsilon)];
- retain absolute error as a complementary scale;
- define a tolerance-dependent adequacy region A_tau and boundary partial A_tau in parameter space;
- validate a recovery regime before studying failure;
- map both underestimation and overestimation rather than only breakdown;
- measure displacement of that adequacy boundary under biological assumption violations;
- decompose paired perturbations with interaction contrasts;
- connect the controlled boundary to empirical evidence that the relevant assumption violations occur.

This combination is the current candidate methodological contribution. It remains provisional until broader searching and the computational results are complete.

## Strongest safe contribution statement

> We develop and benchmark a model-adequacy framework for finite-horizon evolutionary target probabilities. Rather than treating accessibility, origin–fixation dynamics, or SSWM breakdown as new, the framework makes approximation discrepancy itself the object of analysis: it measures its magnitude and direction, identifies tolerance-dependent adequacy regions relative to an explicit finite-population reference process, and tests how departures from approximation assumptions move those regions.

## Claims we should never make

- “We introduce evolutionary accessibility.”
- “We first model evolution as a stochastic state-transition process.”
- “We introduce genotype findability/hitting times.”
- “We discover that origin–fixation requires weak mutation.”
- “We discover that fixation time matters.”
- “We discover the N*mu boundary between periodic selection and interference.”
- “We introduce epistasis, route multiplicity, mutation-rate heterogeneity, or historical contingency.”

## Novelty threats to keep testing

A future search could still find a paper that explicitly maps probability-level approximation discrepancy between origin–fixation and Wright–Fisher processes. Before manuscript submission, search combinations of: model adequacy, approximation discrepancy, origin-fixation, Wright-Fisher, finite-horizon fixation/hitting probability, SSWM validity boundary, first-passage probability, and error surface.

If exact precedent is found, novelty must move to boundary displacement/decomposition or another demonstrably distinct result rather than ignoring the precedent.

## Stage-5 implication

The biological stress experiment should not attempt to prove that epistasis, route multiplicity, or mutation heterogeneity matter in general. Those are established. It should ask the narrower new question: **how much do they move the approximation-adequacy boundary, in which direction, and are their effects additive or interactive?**

## Core references
- McCandlish DM. 2013. On the Findability of Genotypes. Evolution 67:2592–2603. DOI: 10.1111/evo.12128.
- McCandlish DM, Stoltzfus A. 2014. Modeling evolution using the probability of fixation: history and implications. Q Rev Biol 89:225–252. DOI: 10.1086/677571.
- Kopp M, Hermisson J. 2009. The Genetic Basis of Phenotypic Adaptation I: Fixation of Beneficial Mutations in the Moving Optimum Model.
- Weissman DB et al. 2009. The pace of evolution across fitness valleys.
- Desai MM, Fisher DS. 2007/related successional-fixation and concurrent-mutation literature.
- Gerrish/Lenski and subsequent clonal-interference literature.


## Adversarial search update: direct Wright–Fisher/origin–fixation comparisons

A close precedent must be treated explicitly:

Baxter et al. (2021), *How individuals change language*, PLOS ONE 16:e0252582, uses an individual-level Wright–Fisher-type process and a population-level origin–fixation description. The paper derives origin/fixation quantities from the underlying process, compares the two descriptions numerically, includes sequential two-change cases, and analyzes interference when a later innovation arises before an earlier one has fixed.

This is important prior art.

### Consequence for novelty

**Claim now prohibited:** “This is the first comparison of origin–fixation and Wright–Fisher models,” “the first finite-time comparison,” or “the first study of interference between sequential changes.”

The candidate distinction is narrower:
1. probability error itself is the response variable across a predeclared evolutionary parameter grid;
2. error is signed, so approximation under- and over-estimation are separated;
3. adequacy is explicitly tolerance-relative through A_tau;
4. the location of partial A_tau is treated as an estimand;
5. biological assumption violations are evaluated by how they displace that boundary;
6. paired violations are decomposed with interaction contrasts;
7. recovery and failure regimes are both required;
8. empirical data are used as assumption-stress evidence rather than as proof of the theoretical framework.

### Additional neighboring evidence

Weissman et al. (2009), *The pace of evolution across fitness valleys*, explicitly compares mutation waiting and conditional fixation times and gives a periodic-selection/SSWM condition. This reinforces that time-scale separation itself is established.

Origin–fixation simulation work also treats resident-genotype transitions as approximations to Wright–Fisher evolution and studies accuracy/algorithmic consequences. Therefore our manuscript must cite this family and avoid generic “approximation” priority claims.

### Updated novelty test

Before submission, the central claim survives only if the literature search still fails to identify prior work that jointly:
- defines a finite-horizon target probability under both models,
- makes signed probability discrepancy the central mapped quantity,
- defines tolerance-dependent adequacy regions/boundaries,
- and quantifies boundary displacement/interactions under controlled assumption violations.

Finding any paper satisfying these conditions requires another narrowing of the claim.


## Adversarial search update: error surfaces and validity regions

A second novelty threat is now explicit. Wright–Fisher approximation studies already quantify approximation quality across parameter space using distance/error surfaces. Examples include Tataru et al.'s comparisons of approximate versus true allele-frequency distributions with Hellinger-distance heatmaps and Paris et al.'s comparison of parametric Wright–Fisher transition approximations with Wasserstein-distance heatmaps across starting frequency, time interval, and selection intensity.

Other population-genetic theory also derives ranges/conditions of validity for approximations and identifies regime/interference boundaries.

### Consequence

**Claims now prohibited:**
- first to quantify approximation discrepancy in population genetics;
- first to map approximation accuracy over parameter space;
- first to use an error/distance heatmap against Wright–Fisher dynamics;
- first to identify a parameter-space validity/range-of-validity region;
- first to identify a boundary separating evolutionary regimes.

### Candidate distinction after this search

The remaining candidate contribution must be stated at the level of the specific estimand and experiment:

1. finite-horizon **target-event probability** is matched between a reduced evolutionary process and an explicit finite-population reference;
2. the discrepancy is **signed**, preserving under- versus over-estimation rather than only distributional distance;
3. a scientifically declared tolerance converts that event-probability discrepancy into an **adequacy set for the particular approximation and endpoint**;
4. the study estimates how that adequacy set/boundary changes when biological assumptions are perturbed;
5. perturbations are compared in a common design and paired perturbations receive explicit interaction contrasts;
6. recovery, agreement, under-estimation and over-estimation are all admissible outcomes;
7. the boundary is not presented as a universal biological regime boundary.

This is narrower than the previous novelty statement and is safer.

### Terminology discipline

Prefer:
- “approximation-adequacy set/boundary for the specified endpoint and tolerance”
- “signed target-probability discrepancy”
- “boundary displacement under assumption perturbation”

Avoid:
- “new validity boundary”
- “first error landscape”
- “new evolutionary regime”
- “universal adequacy boundary”

### Falsification of novelty

If prior work is found that jointly treats a matched finite-horizon evolutionary target-event probability, signed approximation discrepancy, an explicit tolerance-defined adequacy set, and controlled displacement/interactions of that set under biological assumption violations, the current methodological novelty claim must be narrowed again.


## Final post-result novelty position

The completed study does **not** claim to resolve a universal adequacy boundary. Stage 5 produced no factor-two crossing in the frozen 36-cell domain. The final contribution is therefore framed more conservatively: finite-horizon target-event probabilities are matched between an origin–fixation approximation and an explicit finite-population comparison; signed discrepancy preserves direction; exact and held-out calculations diagnose the finite-time sweep contribution; two-locus and biological stress tests show where the simple diagnostic becomes incomplete; and LTEE data independently establish biological occurrence of relevant heterogeneity and alternative structural routes. This framing is consistent with the final *Theoretical Population Biology* manuscript and avoids priority claims already threatened by McCandlish (2013), McCandlish & Stoltzfus (2014), Baxter et al. (2021), and the Wright–Fisher approximation literature.
