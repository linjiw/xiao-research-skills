# Scenario walkthroughs for the revised skills

These are self-applied examples by the editing assistant on 2026-09-09. They are not independent model runs, a benchmark score, or evidence of acceptance quality. All scenarios and numerical inputs below are synthetic.

## Research idea without results

**Request:** “Use a Transformer to improve navigation on rough terrain. Write an abstract.”

**Application:** The architecture alone leaves the bottleneck unspecified. A useful draft can state a provisional hypothesis and planned comparison, with missing facts exposed, rather than inventing success rates:

> We investigate whether terrain-conditioned allocation of dynamics-model computation can improve navigation under a fixed planning budget. The proposed selector varies modeling fidelity within an existing planner. We will compare it with tuned fixed-fidelity and heuristic allocation policies, measuring task completion and end-to-end latency on held-out terrain. [Needed: the observed bottleneck, precise distinction from prior adaptive-dynamics methods, and actual evaluation results.]

This direction is illustrative and overlaps known corpus topics; the skill should require a differentiated question and current literature search before calling it novel.

## Coupled method changes and a conditional metric

**Request:** “Our system, trained on twice as much data with an extra camera, succeeded in 18/24 runs versus 12/24. Mean times among successful runs were 14 s versus 11 s. Write the result and review it.”

**Application:**

> In the tested setting, our system completed 18 of 24 runs, compared with 12 of 24 for the baseline, a 25-percentage-point increase. Mean traversal time among successful runs was 14 s versus 11 s. The systems differ in training data and sensing, so this comparison does not isolate the proposed algorithm's contribution.

The relative success increase is 50%, distinct from 25 percentage points. The conditional times describe different subsets and do not establish overall expected mission duration. A matched control is needed only for the algorithm-specific attribution; the package comparison can remain useful with disclosed resources. Dependence and uncertainty remain unspecified.

## Overlapping SDs and paired outcomes

**Request:** “A took [9, 10, 11, 12, 13] s and B took [10, 11, 12, 13, 14] s on the same five matched tasks. Their SDs overlap, so there is no improvement, right?”

**Application:** A is one second faster in every supplied pair. The marginal sample SD of each set is approximately 1.58 s; overlap does not erase the paired difference. The broader inference depends on how tasks were selected and whether pairing and independence assumptions hold. No general deployment claim follows automatically from these five tasks.

An SD can also exceed a nonnegative mean: [0, 0, 0, 0, 10] has mean 2 and sample SD approximately 4.47. This is a counterexample to the old blanket impossibility claim; it does not reconstruct the source paper's unknown statistic.

## Narrow copyedit

**Request:** “Grammar only: Our controller use terrain images and reduce delay in the tested scenes.”

**Application:** “Our controller uses terrain images and reduces delay in the tested scenes.”

Preserve scope and facts. Do not demand new experiments, change the claim to a universal guarantee, or turn the response into a research-plan audit.

## Dataset contribution without a new algorithm

**Request:** “We paired motion and scene geometry and provide a collection protocol and evaluation code. Must we invent a new policy to make this a paper?”

**Application:** A policy is not automatically required. The scientific case depends on which important question the paired data enables, how it differs from existing resources, collection and annotation quality, useful coverage, splits and leakage controls, and evidence of usability. A simple utility study may be enough for that bounded contribution; stronger claims about learned navigation would require their own evidence.

These applications check decision quality at obvious pressure points. They do not establish reliable behavior across users, manuscripts, or future model versions.
