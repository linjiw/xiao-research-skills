# State the strongest claim the evidence supports

Use for claim calibration or technical copyediting. These are evidence requirements and writing choices, not estimates of an author's preferences. Source keys refer to physical PDF pages through the bundled ledger.

## 1. Match the kind of claim, not a universal ladder

| Claim | Needed warrant | Example wording shape |
| --- | --- | --- |
| Existence or feasibility | Observed instance, with material conditions | “The prototype completed [task] in [demonstration setting].” |
| Comparative performance | Relevant comparator, clear outcome, design and uncertainty | “[A] achieved [outcome] compared with [B] over [units].” |
| Mechanism contribution | A defensible intervention or other identification argument; alternatives considered | “Removing [component] reduced [outcome] in [design].” |
| Generalization | Specified held-out axis and evidence that matches the target population | “The frozen policy transferred to [held-out scenes/platform].” |
| Statistical difference | Suitable test or interval-based analysis, design and relevant reporting | “We detected [difference] using [analysis], with [effect and uncertainty].” |
| Equivalence | Defined tolerance and an analysis that can establish it | “The difference lies within [prespecified practical bounds].” |
| Guarantee | Valid formal or exhaustive argument under explicit assumptions | “Under [assumptions], [property] holds.” |
| Novelty or priority | Current primary-literature search and a precise distinction | “Unlike [nearest approach], this method [verified difference].” |

These dimensions combine. A theorem does not establish empirical transfer, a held-out split does not isolate a mechanism, and a small p-value does not make an effect useful. A component ablation may require retraining and can create distribution shift; do not automatically turn it into an unrestricted causal claim.

## 2. Keep the necessary context attached

Ask four questions: under what condition, over which population, compared with what, and measured how? Make their answers easy to find, especially in the abstract, captions, and conclusion. Use adjacent sentences when packing everything into one would obscure the point.

Scope can make a sentence precise without making its verb timid: “In [tested setting], [method] reduced [metric] from [a] to [b].” A genuinely uncertain explanation should remain uncertain: “This pattern is consistent with [mechanism]; [alternative] remains possible.” Do not delete “may” or “could” when uncertainty is what the evidence warrants.

The result and its explanation are separate propositions. `applr` pp1,6 distinguishes parameter-policy learning from earlier demonstration-based adaptation; a later performance comparison must still establish what that change buys. `mrvs` p19 explicitly leaves individual feature effects unresolved after evaluating the integrated system.

## 3. Words that need particular evidence

| Wording | Check |
| --- | --- |
| significant | Is statistical significance intended and supported by an appropriate analysis? If “large” is intended, state the magnitude. |
| safe, collision-free, guarantees | Distinguish a formal property, a safety mechanism, and observed outcomes. Zero failures in finite trials is not a guarantee. |
| real time | Name the measured end-to-end latency or rate, hardware, and deadline; consider tails and missed deadlines when material. |
| efficient | Specify the resource: data, compute, energy, wall time, tuning, or human effort. Throughput alone does not measure energy. |
| robust, generalizes | State the perturbation or held-out axis, tested range, and boundary. There is no universal three-point threshold. |
| consistently outperforms | Define whether consistency means metrics, conditions, seeds, or paired examples. Check exceptions at that level. |
| scalable | State which size or workload grows and how cost or performance changes. Use the range needed to support the claimed trend. |
| zero-shot | Specify what is held out and whether target examples, descriptions, prompts, calibration, or adaptation are provided. The term alone is ambiguous. |
| end-to-end | Specify the relevant training or input-output boundary. It does not universally mean absence of hand-designed components. |
| human-like, understands | Name the behavior, cue, or measured construct. Prediction accuracy alone does not establish a mental process or human preference. |
| first, state of the art | Verify a dated primary-literature comparison. A hedge is not a substitute for the search. |

`legs_over_arms` p1 names trajectory-prediction error, while `social_nav_protocol` p1 motivates a human-rating instrument. These answer different questions even though both inform social navigation.

## 4. Numbers and uncertainty

- Percentage-point change is the difference between percentages. Relative change divides that difference by the reference percentage. Name the baseline and direction. A zero reference makes a relative ratio undefined.
- Give counts for small-denominator rates. Keep simulation, physical runs, and human-study results identifiable when summarizing them together.
- Define every `±`: SD, SE, interval half-width, variance, or something else; report the aggregation unit. SD can exceed the mean. Overlapping SD bars neither prove equivalence nor rule out a difference in means.
- Do not infer per-example dominance from the lowest mean. Conversely, large individual variation does not by itself refute a consistent mean advantage across conditions.
- “Up to” identifies a maximum. State the relevant condition and, when needed for representativeness, provide the distribution, typical case, or other summary. A median is useful only when the cells form a meaningful population to summarize.
- State whether an average weights scenes, trials, datasets, or baselines equally. Avoid averaging incomparable metrics into a headline without a defensible definition.
- Keep conditional times beside success rates. Failed runs excluded from a timing mean can change which tasks the mean describes.
- Trace headline numbers to the exact evidence, which may be in a table, figure, text, or supplement. Resolve discrepancies rather than choosing the more favorable value.

A correction to the previous skills: `vs` p6 calls its angle measure a mean with variance and prints 6.46 ± 26.21. This does not justify the old interpretation that the second quantity must be timestep-pooled SD, nor an SD-based significance calculation. The legitimate question concerns definition, units, and aggregation.

## 5. Synthetic rewrite examples

The following are invented teaching sentences with placeholders, not reported results.

| Weak sentence | More informative version |
| --- | --- |
| “Our intelligent framework guarantees robust navigation.” | “[Method] rejects [specified unsafe candidates]. It completed [k/N] trials under [conditions]; [failure types] occurred.” |
| “Language improves navigation.” | “[A] had higher [metric] than [B]. Because the systems also differ in [backbone/data], this comparison does not isolate language input.” |
| “The method is efficient.” | “On [hardware], the complete pipeline took [latency distribution] per update, within [deadline] for [fraction] of updates.” |
| “The result proves our hypothesis.” | “[Intervention] changed [outcome] in the predicted direction under [design], supporting [bounded explanation].” |
| “The robot behaves like a human.” | “The policy uses [human-derived cue]; we evaluated [measured behavior]. [Broader construct] was not measured.” |

Be as direct as the evidence allows. The aim is an informative statement, not a disclaimer attached to every sentence.

## 6. Fast revision pass

First locate the strongest claim and its evidence. Recalculate comparisons, identify the evidence type and population, and check the important exceptions. Then inspect the connecting verbs and nouns: does a proxy become a broader construct, an association become causation, or a demonstration become a general result?

For polish-only work, preserve technical meaning and flag substantive concerns separately. For a substantive rewrite, repair the mismatch with the smallest accurate change. Source-inspired teaching notes do not belong in the user's submission prose unless cited for a relevant scientific reason.
