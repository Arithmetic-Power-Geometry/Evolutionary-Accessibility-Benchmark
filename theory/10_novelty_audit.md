# Novelty audit: approximation adequacy and finite-population target probabilities

Status: literature boundary frozen before Stage 5. This is a claim-discipline document, not a claim of exhaustive priority.

## Question audited
Has prior evolutionary theory already established the proposed object: a signed error surface between a specified simplified evolutionary probability model and a finite-population reference target-hitting/fixation probability, together with tolerance-dependent adequacy regions/boundaries and perturbation/interactions analysis?

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
**Our permitted use:** use the ratio as a predeclared explanatory variable for a different response variable: finite-horizon target-probability approximation error.

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

> We develop and benchmark a model-adequacy framework for finite-horizon evolutionary target probabilities. Rather than treating accessibility, origin–fixation dynamics, or SSWM breakdown as new, the framework makes approximation error itself the object of analysis: it measures its magnitude and direction, identifies tolerance-dependent adequacy regions relative to an explicit finite-population reference process, and tests how departures from approximation assumptions move those regions.

## Claims we should never make

- “We introduce evolutionary accessibility.”
- “We first model evolution as a stochastic state-transition process.”
- “We introduce genotype findability/hitting times.”
- “We discover that origin–fixation requires weak mutation.”
- “We discover that fixation time matters.”
- “We discover the N*mu boundary between periodic selection and interference.”
- “We introduce epistasis, route multiplicity, mutation-rate heterogeneity, or historical contingency.”

## Novelty threats to keep testing

A future search could still find a paper that explicitly maps probability-level approximation error between origin–fixation and Wright–Fisher processes. Before manuscript submission, search combinations of: model adequacy, approximation error, origin-fixation, Wright-Fisher, finite-horizon fixation/hitting probability, SSWM validity boundary, first-passage probability, and error surface.

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
