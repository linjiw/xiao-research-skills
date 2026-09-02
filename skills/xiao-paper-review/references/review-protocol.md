# Evidence-focused review protocol

Use a compact claim table for several claims, prose for one:

| Claim / manuscript location | Evidence supplied | Warrant | Smallest repair |
| --- | --- | --- | --- |
| Faithful paraphrase | Figure/table/proof/section and setting | Supported, partial, unclear, contradicted, not assessable | Reporting, analysis, narrower wording, decisive experiment |

“Not assessable from the abstract” is not “the authors did not do it.” Prefer exact page/line locations when available, but never invent them.

## Checks

- **Contribution:** difference from relevant alternatives; verified versus asserted novelty; resource contributions judged as resources.
- **Mechanism:** interfaces, observability, assumptions, training/runtime information; alternative explanations; proof conclusion versus actual assumptions.
- **Experiment:** question answered; tuning/data/sensors/speed/compute/interventions disclosed; independent split units appropriate to the transfer claim.
- **Measurement:** proxy versus construct; conditional versus overall outcomes; averaged metric versus population inference; units and normalization; uncertainty at the independent unit.
- **Operational validity:** simulation, offline prediction, hardware-in-loop, physical closed loop, human study. Check end-to-end latency and recovery only when pertinent. A photograph proves none of these alone.
- **Reproducibility:** settings, resource costs, failures, protocol/code/data availability as reported. Do not assert an external repository is unavailable without checking if that audit was requested.

Audit what enters the denominator: eligibility must be distinguished from desirable outcomes; restricted-envelope results need the overall attempts and exclusions. Resets can turn a route claim into a segment claim. Ground-truth-assisted alignment or cropping changes what a reconstruction metric establishes. A changed class definition or risk formulation changes the quantity being compared. If an abstract and methods section disagree on sample counts, identify both locations and ask for reconciliation rather than guessing which is correct.

## Severity

- **Validity-critical:** contradicts a central claim, established leakage, wrong calculation, invalid proof step, or missing decisive evidence. Explain what conclusion changes.
- **Major clarification:** evidence may suffice but an essential setting or interpretation is unclear; ask a precise question before declaring invalidity.
- **Useful extension:** broadens the scope but is not required for the bounded contribution.
- **Presentation:** organization, notation, wording, captions. Do not let polish dominate a technical review.

No universal score or acceptance threshold. Use the actual venue rubric only if requested.

## Synthetic concern example

“Results paragraph 2 calls a change from 60% to 75% a 15% relative improvement. It is 15 percentage points, or 25% relative to 60%. Correct the abstract and results consistently; the ranking remains unchanged.”

This is an arithmetic example, not a finding about an unseen paper.

End with a repair order: claim-changing issues, experimental reporting, then exposition. Every requested experiment must resolve a stated uncertainty. Offer narrower claims when sufficient.
