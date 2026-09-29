# Model hierarchy

## M0-I: independent-lineage benchmark
The independent-lineage model retained from the earlier study is a controlled benchmark, not a standard population-genetic theory. It is useful as a deliberately restrictive baseline and must be labelled accordingly.

## M0-O: origin–fixation / weak-mutation approximation
The primary biologically recognized approximation is a sequential-fixation model appropriate to a mutation-limited regime. Its transition structure will be constructed from mutation origination and fixation probabilities.

This model is established theory. The contribution is not its construction.

## M1: finite-population reference process
The initial reference process is a haploid Wright–Fisher model with explicit finite-population sampling. The benchmark retains explicit genotype counts with finite-population selection, mutation, and multinomial sampling. The final stress extension adds epistasis, state-dependent mutation, and an alternative target set while retaining constant population size, forward mutation, and no recombination.

Wright–Fisher theory is established and is used here as a reference process.

## Matching rule
A comparison is valid only when M0 and M1 are matched on:
1. genotype/state space;
2. mutation opportunities or mutation matrix;
3. fitness landscape;
4. initial state;
5. target set;
6. observation horizon;
7. population size and other shared biological parameters where defined.

Any unavoidable mismatch must be documented as part of the approximation itself.

## Experimental hierarchy
1. Verify implementation against analytically or numerically checkable special cases.
2. Establish an assumption-compatible recovery regime.
3. Vary one assumption at a time.
4. Study combinations only after single-factor behavior is characterized.
5. Estimate adequacy/failure regions without selecting only large-error cases.
6. Test robustness to target definitions, tolerances, seeds, replicate counts, and numerical regularization.


## Final manuscript hierarchy

The submitted study uses `M0-O` as the primary approximation, `M1` as the finite-population Wright–Fisher comparison, an exact `K=1` mutant-count Wright–Fisher chain for mechanism tests, and a `K=2` stress extension. `M1` is a comparison model, not biological ground truth. The implemented `p_fix` is itself a diffusion approximation, so the reported discrepancy evaluates the complete origin–fixation approximation.
