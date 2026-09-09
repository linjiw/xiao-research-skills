# Review the scientific argument and its evidence

Use for substantive manuscript or research-plan review. This rubric learns from coauthored papers and from errors in the earlier skills; it is not a venue rubric or an individual's judgment. Match the review to the material actually supplied.

## Reconstruct before criticizing

Read the requested material and identify the consequential question, nearest alternative, proposed insight, and strongest supported contribution. State the scope: full supplied manuscript, selected sections, abstract, or plan. A missing abstract detail is not proof that the full paper omitted it.

For a full paper, follow the central claims from title and abstract through method, experiments, figures, and conclusion. Inspect underlying tables or original PDF pages where extraction may corrupt data. Move between sections as needed; a fixed pass order is less important than tracing the argument accurately.

Assess both why the work matters and whether the evidence warrants it. A technically correct implementation can leave its research question unclear. A worthwhile artifact or empirical finding can survive a narrower claim about its mechanism.

## Map the important commitments

| Claim and location | Proposed reason | Evidence and location | Population, units, comparator | Assessment | Smallest sufficient repair |
| --- | --- | --- | --- | --- | --- |
| Faithful paraphrase | Mechanism or rationale, if claimed | Measured, formal, qualitative, or absent | Definitions and dependencies | supported / partial / unclear / contradicted / not assessable | Clarification, re-analysis, narrower claim, control, or new study |

For short reviews, keep this as working notes instead of producing a large table. Distinguish the paper's observations from your inferences. A rival explanation is a testable possibility, not an accusation.

## Check the links that could change the conclusion

1. **Importance and positioning.** Does the problem matter under a concrete operational or scientific constraint? Is the nearest work characterized accurately? Check current primary literature if novelty or a recent-best claim determines your assessment; disclose search scope.
2. **Gap to method.** Would the proposed design address the named limitation? Does it remove a requirement, change a representation, or enable a measurement? `squid` pp1–2 makes this correspondence explicit; the correspondence still requires testing.
3. **Method to experiment.** Does the comparison answer the claimed question? A package comparison cannot isolate every component. `anticipatory_tamp` p4 provides a zero-estimator comparator; `mrvs` p19 instead acknowledges what integrated evaluation leaves unresolved.
4. **Experiment to inference.** Check units, dependence, training/test separation, selection, comparator resources, outcome definitions, failures, and uncertainty. The question is what the design identifies, not whether it meets a universal trial quota.
5. **Inference to prose.** Trace each headline number and strong word to its support. Keep proxy/construct, simulation/physical, mechanism/package, and observed/guaranteed distinctions intact. A figure, formal argument, or text result can support a claim; a table column is not universally required.

## Arithmetic and uncertainty pass

Recompute percentage points, relative changes, ratios, and averages from the actual reference set. Preserve zero-denominator cases as undefined. Check whether rows share the same conditions and whether timing excludes failures. In `appld_ral` p5, the declared failure penalty is part of the metric, not incidental prose.

Identify what each uncertainty number represents and over which units. Separate variation in individual observations from uncertainty in an estimated effect. If paired or clustered observations matter, the analysis must account for that structure. One course repeated twenty times supports within-course observations; it is not twenty independently sampled courses.

Do not infer significance, equivalence, or invalidity from SD overlap or from the gap being smaller than one SD. Small samples can be informative, depending on design and effect; large correlated datasets can still be weak evidence for population transfer. Statistical significance does not establish practical importance, and failure to reject a null does not establish equivalence.

**Corrected teaching case:** `vs` p6 prints 6.46 ± 26.21 for roll and calls the spread variance. The earlier protocol incorrectly assumed SD, computed a standardized gap, and inferred pooling. The justified concern is an unclear statistic, units, and aggregation. Even a confirmed SD above a nonnegative mean is not intrinsically impossible. Ask before calculating with an unidentified spread.

Report a discrepancy as a discrepancy. Do not guess the missing factor, silently repair a value, or convert uncertainty into a misconduct allegation.

## Distinguish evidence types

Offline prediction, closed-loop simulation, controlled physical experiments, human evaluations, field reports, and proofs answer different questions. They are not interchangeable or ordered on a universal ladder. More simulation reduces sampling uncertainty within a simulator; it does not eliminate model bias. A limited physical study can support a conditional comparison without establishing broad transfer.

`social_nav_guidelines` p11 argues for question-dependent methodology. `hirl_vision_paper` p3 identifies a vision/agenda rather than a systematic survey. Use `genre-guide.md` for the relevant obligations and avoid demands belonging to a different contribution type.

## Prioritize a repair that is sufficient

| Finding | Usually appropriate response |
| --- | --- |
| Central scientific question or distinction is unclear | Identify what must be explained; propose a clearer contribution framing. |
| Result is sound but claim too broad | Narrow the claim and retain the supported contribution. |
| A necessary definition, denominator, configuration, or uncertainty unit is missing | Ask for that information before declaring the result invalid. |
| Existing data can resolve averaging, subgroup, or dependence concerns | Request the specific re-analysis and explain its purpose. |
| A leading confound blocks a central attribution | Request a relevant control or a system-level claim that does not require the attribution. |
| The central capability has no supporting evidence | Identify the smallest decisive study, or explain why narrowing would change the contribution. |
| A proposed extension broadens an already supported claim | Mark it optional; do not present it as required for validity. |

An experiment request should distinguish two explanations or establish a missing central capability. State how its possible outcomes would change the conclusion. Avoid unlimited baseline lists and demands for additional hardware, data, or participants without that connection.

## Severity and delivery

- **Validity-critical:** demonstrated defect or missing central warrant changes the conclusion; provide the location and consequence.
- **Major clarification:** the evidence may suffice but an essential interpretation remains unclear; ask a precise question.
- **Useful extension:** expands beyond the supported scope; label it optional.
- **Presentation:** improves comprehension without changing validity.

Default output: actual review scope; strongest contribution and specific strengths; a few prioritized concerns; recommended revision order; essential open questions. Each concern is location → observation → consequence → remedy. Do not let polish crowd out the scientific assessment.

Only give a score when requested against a supplied or verified venue rubric, and mark it provisional. Do not predict an individual's review or acceptance. Review is read-only unless editing is requested.
