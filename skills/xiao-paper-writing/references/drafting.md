# Draft a paper the reader can reason through

Use with `argument-workshop.md` for substantial reconstruction. For narrow edits, jump to Paragraph revision. Examples are analytical paraphrases of coauthored papers; page numbers refer to physical PDFs. The observed habits are options, not a formula for acceptance.

## 1. Title and abstract

The title names the contribution at the scope actually supported: capability, mechanism, setting, or artifact type. Include the mechanism when it distinguishes the work. Use an acronym only when it helps the reader remember or discuss the system; its spelling need not dictate the paper's structure.

An abstract usually needs a concrete problem, the unresolved limitation, the proposed contribution, enough mechanism to explain the idea, and the main evidence-backed answer. Background and release information are optional. A resource can lead with the artifact; an empirical finding can lead with the result. Venue requirements and the user's requested length govern the word budget.

For the mechanism, state what changes and what it does. `lfh_cp` p1 explains a factorization into critical points and obstacle trajectories. `sbt` p1 states which modalities train the representation and which remain at inference. These are more informative than listing network components without their purpose.

For an empirical result, make the comparator, metric, setting, and evidence base recoverable. Spread necessary context across adjacent sentences when it improves readability. Include the important tradeoff or boundary; do not force every experimental detail into the abstract. `cahsor` p1 connects its modeling assumption to concrete stability failures; use that specificity when motivating a method.

For a proposal, keep proposed evaluations in future tense. For a completed study with missing results in the supplied material, use `[needed: measured result and source]`. Never borrow a source paper's numbers.

## 2. Introduction

Give each paragraph a job in the explanation:

- Establish a consequential failure in a particular setting.
- Explain what existing approaches already solve and why a remaining assumption matters here.
- Present the insight that makes the proposed change plausible.
- Describe the contribution and summarize the evidence at its actual scope.

A useful bridge has a reason, not merely “therefore we propose.” For example, `vi-ikd` p1 moves from terrain-dependent kinodynamics to the need for anticipation beyond inertial history. The new information channel follows from the stated limitation.

For several linked gaps, make the correspondence visible. `squid` pp1–2 numbers limitations and links the design to them. Tags are useful when they reduce ambiguity; a single-gap paper rarely needs them. Treat the mapping as promises that evaluation must assess, not as proof that each limitation was solved.

Avoid an extended application preamble that never affects the problem formulation. An application matters scientifically when it changes the available information, acceptable cost, required capability, or consequence of failure.

## 3. Contributions

State the scientific changes, not a project activity log. Each contribution should tell the reader what now exists or what was learned, what differentiates it, and where its support appears. A formulation, artifact, empirical finding, or mechanism can each be a contribution.

Combine items that are merely implementation steps of one idea. Separate a dataset and an algorithm when each has its own evidence obligations. Use as many items as the argument needs; explicit lists and numerical claims are optional. Avoid counting routine evaluation as a separate contribution unless the study itself produces new knowledge.

A provisional contribution remains provisional. For a plan, distinguish “we propose to build” from “we will test whether”; for a manuscript, distinguish “we introduce” from “our results establish.”

## 4. Related work

Organize by the decisions that distinguish the new work: information access, learning signal, representation, planning horizon, objective, deployment constraint, or evaluation object. A historical sequence is useful only when the progression explains the gap.

Credit the nearest work specifically. Then state the difference and its consequence. `apple` p1 acknowledges earlier adaptive parameter learning before motivating evaluative feedback; `hpr-tcgre` p1 states the three assumptions its extension relaxes. Follow-ups can change several coupled assumptions if the paper explains their necessity and evaluates the resulting scope.

Use primary sources to verify a claimed absence, priority, or recent best result. Include the strongest relevant work outside this corpus. “Underexplored” is not a substitute for explaining why the unanswered question matters. A knowledge hedge does not replace a literature search.

## 5. Method

Begin with the decision problem: inputs, outputs, information available when decisions are made, objective, and assumptions. Introduce notation when it becomes useful. State what a variable means physically before deriving with it.

Explain components in dependency order. For each substantial component, tell the reader the requirement it meets, the operation it performs, and the output consumed next. Distinguish the scientific change from standard infrastructure. A long architecture inventory without these connections leaves the rationale unproved.

State training and deployment separately, including privileged inputs, human intervention, external services, and adaptation. Document the exact variant used for each result. A retained planner does not automatically confer a guarantee on a learned wrapper; explain which assumptions and parameter restrictions keep the property valid.

For multiple design choices, explain interactions rather than pretending they are independent. Use ablations when they answer a material mechanism question; do not prescribe one for every line of code.

## 6. Experiments and results

Organize experiments around questions. Before each comparison, state what it is intended to resolve. Report what happened before explaining why it may have happened.

A useful results paragraph contains:

> [Question and comparison.] [Located quantitative or qualitative observation.] [Interpretation warranted by that comparison.] [Relevant exception, uncertainty, or competing explanation.]

Do not narrate every table cell. Select the contrast that answers the question, then account for any cell that changes the answer. In `vs` p6, the physical table includes an easy condition favoring the manual curriculum and a hard condition favoring the learned one. This invites a conditional conclusion and a mechanism question, rather than an unrestricted ranking.

Separate measured outcomes from explanations. An ablation can support a component's contribution in that setup; it does not by itself establish a complete causal account. A model accuracy improvement needs separate evidence before becoming a closed-loop mobility claim.

`research-design.md` handles controls, units, uncertainty, and failure accounting. `wording.md` handles exact claims and arithmetic.

## 7. Figures and tables

Choose figures by their argumentative job: make the bottleneck visible, explain an interface, distinguish predictions, show a measured effect, or expose a boundary. Figure 1 may be a scenario, comparison, architecture, or result; choose whichever makes this paper's central idea easiest to understand.

Sketch the decisive table before collecting data. Its caption should name the population, units, denominator or location of that information, conditioning, uncertainty definition, and marking convention where relevant. Do not fabricate plotted results for a planned experiment.

A qualitative illustration shows an instance, not a frequency. A pipeline diagram explains operations, not effectiveness. Bold can mark the best numerical mean if stated; it must not silently imply statistical significance. SD overlap and a one-SD gap are not decision rules for significance or equivalence.

Preserve the distinction between time over successful runs and outcomes over all attempts. A blank, failure token, timeout, and zero mean different things. `appld_ral` p5 explicitly describes a failure penalty; `vs` p6 explicitly conditions traversal time on successful trials.

## 8. Discussion, limitations, and conclusion

Explain what changed in our understanding, then where that understanding stops. State important limitations beside the claims they qualify as well as in a dedicated section if appropriate.

A generative limitation identifies a failed or untested condition, a possible explanation, and an observation that would distinguish explanations. It need not promise a fix. `mrvs` p19 separates integrated-system evaluation from the controlled component studies that could explain individual feature effects. `verti_bench` p9 identifies ground-truth perception as an assumption and proposes perturbing perception to examine it.

The conclusion answers the original question using evidence already presented. It can synthesize several results, but it must preserve their definitions, populations, and qualifications. Metrics may be reported in figures, text, tables, or appendices; the requirement is traceable evidence, not a particular display format. Proposals and limitations must not become accomplishments during summarization.

## 9. Revision and rebuttal

For a substantial revision, first repair the reasoning: significance of the question, gap-to-method connection, test-to-claim fit, and consistency across sections. Then repair organization and sentence flow. Surface polish cannot resolve a missing scientific link.

A rebuttal addresses the actual concern, points to evidence, acknowledges any remaining gap, and states the concrete manuscript change. If an experiment has not been run, say so and offer the narrower claim or a feasible plan. Do not claim a promised experiment's outcome. Keep respectful credit for the concern without conceding an unsupported criticism.

## Paragraph revision

Identify the paragraph's job and preserve the supplied facts. Use this practical pass:

1. Put the known object or problem before the new information it motivates.
2. Keep the actor and action visible; replace nominal chains with direct verbs when meaning allows.
3. Check each “because,” “therefore,” “however,” and “thus” for a real logical relationship.
4. Give pronouns clear referents and keep central terminology stable.
5. Cut sentences that repeat the same job; retain necessary technical qualifications.
6. End where the next paragraph can begin, with a consequence or unresolved question rather than generic praise.

Read the topic sentences alone: they should expose the argument's progression. Then read each paragraph without its transitions: the underlying reasoning should still hold.

For language-polish-only requests, preserve technical scope and meaning. Flag substantive problems separately rather than silently correcting claims. Return the revised text first and explain only consequential changes.

## Learning loop

For source-based teaching, use the deliberate-practice loop in `argument-workshop.md`: reconstruct, challenge, transfer, write, and evaluate reasoning. Source observations and teaching notes stay outside submission prose unless the source is genuinely relevant and cited.
