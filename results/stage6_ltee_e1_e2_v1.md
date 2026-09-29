# Stage 6 LTEE empirical stress evidence — E1/E2

## Source

Dryad DOI 10.5061/dryad.6226d. Analysis used the original archive supplied for Stage 6.

Primary source tables:
- `LTEE_Mutator_info.txt` for point-mutator status;
- `count.LTEE.final_masked.csv` for mutation counts and mutually exclusive top-level mutation categories.

The endpoint is generation 50,000, the latest common generation represented for all 12 LTEE populations. The population is the inferential unit: the two endpoint clones are aggregated/averaged within population before the six-mutator versus six-nonmutator comparison, avoiding treatment of sister clones as independent population replicates.

## E1 — mutation burden

At generation 50,000 the six point-mutator populations had population-level mean clone mutation totals:

1691.0, 2430.5, 1101.0, 1063.0, 782.5, 1320.0.

The six nonmutator populations had:

124.0, 68.0, 68.5, 77.5, 91.0, 82.5.

Median mutation burden:
- point mutators: **1210.5**
- nonmutators: **80.0**
- median ratio: **15.13**

Exact two-sided Mann–Whitney: **U = 36, p = 0.0021645**.

This reproduces the descriptive endpoint contrast reported in the earlier manuscript, now with the population explicitly retained as the inferential unit.

## E2 — mutation-spectrum concentration

For each population, counts from the two endpoint clones were summed within the mutually exclusive top-level categories:

base substitution, small indel, large deletion, large insertion, large amplification, large substitution, mobile-element insertion, gene conversion, inversion.

The population spectrum was normalized to proportions and Shannon entropy was calculated as

H = -sum_i p_i log(p_i).

Point-mutator population entropies:
0.478882, 0.041557, 0.158943, 0.553319, 0.682087, 0.548281.

Nonmutator population entropies:
1.440627, 1.251661, 1.162706, 1.220784, 1.132421, 1.277973.

Median entropy:
- point mutators: **0.513582**
- nonmutators: **1.236223**

Exact two-sided Mann–Whitney: **U = 0, p = 0.0021645**.

Thus the supplied LTEE archive independently supports two empirical stress features relevant to the approximation study: strong among-population mutation-state heterogeneity and markedly different mutation-spectrum concentration.

## Interpretation boundary

These results establish occurrence of approximation-relevant biological heterogeneity in the LTEE. They do **not** establish that this heterogeneity caused the Stage-5 approximation-discrepancy patterns, nor that LTEE crosses the factor-two adequacy threshold.

## Remaining Stage-6 item

E3, route multiplicity, is not inferred from these tables. It requires the dedicated Cit+ route source. Acquire and inventory Dryad DOI 10.5061/dryad.8q6n4 before E3. No additional endpoint will be mined from 6226d merely to strengthen the result.


## Final manuscript alignment

The manuscript reports the population-level endpoint exactly as above: median mutation burden 1210.5 versus 80.0 (15.13-fold; exact two-sided Mann–Whitney `U=36`, `p=0.0021645`) and median Shannon entropy 0.513582 versus 1.236223 (`U=0`, `p=0.0021645`). These are descriptive LTEE stress observations, not causal validation of Stage 5.
