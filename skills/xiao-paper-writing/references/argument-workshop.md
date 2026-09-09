# Build the scientific argument

Use this workshop for substantial research development, outlines, and manuscript reconstruction. For a requested paragraph edit, use only the relevant paragraph guidance in `drafting.md`. The tools below are working notes, not mandatory sections to insert into the paper.

These are analytical lessons from coauthored papers. A source observation is distinct from the proposed practice it inspires. Neither establishes novelty or results for a new project.

## Find the question before choosing the model

Start with a consequential situation the intended reader can picture. What decision fails, for whom, under which constraint? Trace the failure to competing explanations before naming a solution. A larger network, extra data, a new benchmark, better tuning, or a hardware change might each be the right intervention.

Useful searches through a research problem:

| Look for | Ask | Source observation |
| --- | --- | --- |
| A capability the platform has but autonomy cannot use | Is the limit mechanical, perceptual, or algorithmic? | `vw` pp1,6 separates wheeled capability from the conventional obstacle/free-space abstraction. |
| Information available too late | What must be anticipated, and what signal could carry it? | `vi-ikd` p1 motivates visual anticipation alongside inertial history. |
| An expensive requirement | Can its useful information be supplied another way? | `apple` p1 replaces takeover-style interaction with evaluation; `sbt` p1 separates multimodal training from thermal-only deployment. |
| A representation that creates the difficulty | Can we reformulate the learning or planning target? | `lfh_cp` p2 replaces direct dynamic-obstacle hallucination with critical points and trajectory generation. |
| A measurement that misses the phenomenon | What interaction must the evaluation allow to unfold? | `verti_bench` p1 explains why static recorded data cannot by itself evaluate closed-loop mobility. |
| A surprising failure or mixed result | Which assumption distinguishes the winning and losing regimes? | `barn26_report` p7 exposes tuning dependence through cold trials. |

These are routes to questions, not findings that these explanations hold in the user's project. Check nearest primary literature before calling the proposed difference new. Search beyond this author's corpus and include strong alternatives from other groups.

## Write an argument that can be wrong

A useful working sentence is:

> In [operational condition], [existing mechanism] is limited by [specific requirement]; changing [intervention] is predicted to improve [outcome] because [explanation], at a cost of [tradeoff].

Mark which parts are observed, inferred, proposed, and measured. Then ask what a capable skeptic would offer as the simpler explanation. If retuning the existing method solves the failure, the project may be about adaptation or usability rather than a new planner class. If extra data explains the result, test the data contribution directly.

Choose the next study for the decision it changes. A small diagnostic with opposite predictions under two explanations can be more useful than a broad leaderboard. If no feasible observation distinguishes the explanations, weaken the mechanism claim or reformulate the question.

## Connect the paper's commitments

Keep a compact map while developing a substantial paper:

| Problem evidence | Proposed explanation | Design choice | Discriminating test | Actual result | Conclusion allowed |
| --- | --- | --- | --- | --- | --- |
| Located observation | Hypothesis, including rival | What changes and why | Comparator, outcome, expected alternatives | Evidence location or `[not measured]` | Scope and unresolved explanation |

Not every row needs a new experiment. A definition may need an example and counterexample; a theorem needs a derivation; a dataset needs evidence of coverage and utility. One experiment can answer several questions if the comparisons actually distinguish them.

Read this map in both directions:

- Forward: would this method address the stated failure, and would this test notice if it did not?
- Backward: does the result answer the introduction's question, and does the conclusion require evidence missing from the map?

A system comparison establishes the value of the package. A component intervention may explain that value. Confusing the two is a common logical break. `anticipatory_tamp` p4 makes the myopic comparator a zero-estimator version of the same planning algorithm. `mrvs` p19 explicitly leaves component causality unresolved after evaluating an integrated system. Both can support worthwhile papers with different claims.

## Build a reader's route through the evidence

Sketch the key figure or table before polishing the introduction. Decide what the reader should learn from it, what each condition tests, and which outcome would challenge the story. Use real evidence when available; leave an empty table as a plan when it is not.

Then write an outline whose section summaries form an argument when read alone:

1. Why this failure matters in the stated setting.
2. What prior approaches achieve, and which assumption remains limiting.
3. The insight and the design it motivates.
4. The evidence needed to establish benefit, explain it, and locate its boundary.
5. What has been learned, including what remains unresolved.

Adapt that order for a theory, resource, field, or position paper. Multiple contributions are appropriate when their dependencies are clear. Do not force a paper to change exactly one component, carry exactly three contributions, or introduce its gap in a particular numbered paragraph.

Use a repeated technical term to connect sections when it denotes the same quantity. Do not rotate synonyms for a central variable. Conversely, when a term changes meaning, state the change: `risk_ssrr` p6 uses an additive risk index, while `risk_ral` p8 defines a probability with non-additivity and history dependence.

## Worked example: a hypothetical research direction

**Synthetic teaching example. No experiment or result below has been performed.**

Starting idea: “Use a Transformer to improve terrain navigation.” This names a tool but leaves the scientific question open.

Research version: “Our current planner uses the same dynamics fidelity throughout a rollout. We hypothesize that the cost of model error depends on the terrain segment and that allocating a fixed computation budget accordingly can improve completion.” The fixed-fidelity limitation is a premise to verify in the user's system, not a measured fact supplied by this example.

Competing explanations and useful tests:

| Explanation | Test | How the answer changes the project |
| --- | --- | --- |
| The baseline is simply under-tuned | Tune a fixed-fidelity baseline on separate validation tasks | If this removes the gap, study tuning cost or robustness rather than claiming a new source of planning ability. |
| Gains come from more computation | Compare fixed, heuristic, and learned allocation under a stated matched budget | If a heuristic matches the learner, retain the allocation insight and simplify the proposed method. |
| Context predicts where fidelity matters | Compare aligned context with an appropriate shuffled-context control; check distribution and timing effects | An unchanged result weakens the contextual explanation. A degraded control supports it only within that intervention. |
| Adaptation creates latency failures | Log end-to-end deadlines, outcomes, and interventions across held-out terrain | Better prediction without better completion redirects the work toward the planning interface or latency. |

A provisional introduction paragraph:

> Accurate dynamics predictions help a robot plan through uneven terrain, but evaluating a detailed model throughout every candidate rollout can limit the planner's update rate. We investigate whether allocating modeling effort according to terrain context can improve navigation under a fixed computation budget. Our proposed selector assigns modeling fidelity within the existing planner. We will compare this design with tuned fixed-fidelity and heuristic allocation policies, using task completion and end-to-end latency to distinguish useful allocation from additional computation.

This is proposal prose. After experiments, replace its final sentence with the measured answer and scope; do not automatically convert the hypothesis into a finding. If the user requests a finished-paper abstract before providing results, produce the useful draft with explicit result placeholders.

The example follows reasoning visible in `ddp` p1, `adp` p1, and `ado` p1. It is not a claim that this direction is novel. A real project would need a substantially differentiated question and current literature verification.

## Deliberate practice

When the user wants to learn, reconstruct a named source's problem, insight, decisive comparison, and limitation from verified pages. Have the learner propose a rival explanation, then draft a paragraph for their own project using its logic. Evaluate the paragraph for scientific importance, explanatory connection, evidence fit, and clarity. Do not score resemblance to an author's wording or predict anyone's judgment.

For ordinary writing requests, do the writing. Use the workshop to improve the requested artifact rather than replacing it with homework.
