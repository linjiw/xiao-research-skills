# Design research that changes what we know

Use with `argument-workshop.md` for a new project or substantial redesign. Source examples are coauthored work, identified by ledger key and physical PDF page. They suggest tests; they are not evidence about a new method.

## 1. Start with the uncertainty

Write the operational problem, the evidence it exists, the proposed explanation, and a credible rival explanation. Then state what an informative result would change: the choice of algorithm, a belief about a mechanism, the feasibility of an application, or the ability to measure a phenomenon.

A useful claim is conditional: under a named setting, an intervention should affect an outcome compared with an alternative for a stated reason. Mark conjectures and missing information. Check current primary literature before making a novelty claim, including nearest alternatives outside the local corpus.

Consider simple repairs before building a complex system. Retuning, a better objective, a data change, or a mechanical redesign may address the bottleneck. If so, that can be the research insight. In `appld_ral` p5, the same navigation stack behaves differently under different parameter policies; `compa` p1 instead changes the mechanical/control interface to stabilize a payload.

## 2. Match a test to its job

| Question | Useful comparison | What remains unresolved |
| --- | --- | --- |
| Does the proposed package help? | Relevant strong systems under the intended deployment contract | Which of several changed components explains a gain |
| Does the named mechanism contribute? | The system with a justified component intervention, including a valid fallback | Interactions, retraining effects, and alternative implementations |
| Is the baseline under-tuned? | A tuned or strengthened baseline with a disclosed selection budget | Performance of all algorithms in that class |
| Does information explain the gain? | Matched backbone and training with input removed, replaced, or appropriately shuffled | Architecture dependence and artifacts introduced by the intervention |
| Does the data recipe matter? | Same learner, different collection, labeling, or sampling strategy | Which property of the data is causal |
| Does the behavior transfer? | Freeze the appropriate training decisions and hold out the claimed axis | Other untested axes or populations |
| Does the proposed measure mean what we think? | Reliability and construct checks before ranking methods | Validity for other participants, sites, or constructs |
| Is a formal property established? | Definitions, assumptions, derivation, boundary cases | Whether an approximate implementation satisfies the assumptions |

Examples: `anticipatory_tamp` p4 uses the same planning algorithm with a zero anticipatory-cost estimator as its myopic comparator. `mocap_icra` pp1,6 distinguishes kinematic and learned approaches to sensor displacement. `social_nav_protocol` p4 pilots repeated scenarios across participants and sessions before using the instrument to compare policies. Those pilots suggest a validation strategy; they do not establish reliability of every questionnaire or population.

An ablation that disables the system without a meaningful alternative is usually uninformative. If two components interact, a factorial comparison or a carefully chosen set of joint interventions may be needed. Keep causal language proportional to what the intervention identifies.

## 3. Specify the experiment before its outcome

For each important experiment, record only the details needed to make the decision and interpretation clear:

| Field | Specify |
| --- | --- |
| Scientific question | Claim, competing explanations, predicted outcomes under each |
| Intervention and comparators | Changed variables, retained components, retraining and tuning rules |
| Population and sampling | Eligible tasks, split, independent sampling/assignment units, repeated observations |
| Outcomes | Success, failure, timeout, intervention, units, denominator, conditioning |
| Resources | Training data, sensors, privileged information, compute, speed, adaptation, human effort |
| Analysis | Estimand, aggregation, uncertainty method, important subgroups, selection procedure |
| Decision | What supports, weakens, or leaves the hypothesis unresolved |

Use empty tables or expected qualitative directions for a plan; never invent future numbers. Label analyses chosen after seeing results as exploratory where that matters. Keep validation tuning separate from final testing. Repeatedly selecting the best checkpoint on the test set changes what its reported performance estimates.

## 4. Define the claim's population and unit

Distinguish the unit assigned an intervention, the unit sampled independently, the unit measured, and the population to which the claim refers. They can differ. Episodes may be nested within scenes, trajectories within people, and evaluations within trained seeds. Pairing and dependence matter to the analysis.

One course run twenty times provides twenty observations of performance on that course; it does not provide twenty independently sampled courses. It can support a comparison conditional on that course with an appropriate design. Generalization across courses requires evidence at that level. Do not discard valid within-course information or automatically declare every observation dependent.

Report the counts at relevant levels. For an environment-level prediction fitted to five environment summaries, fifty underlying trials do not create fifty independent points in that fit (`navdiffdataset_ssrr` p5). Persistent task sequences similarly require accounting for dependence between tasks (`anticipatory_tamp` p1 motivates precisely those carryover effects).

## 5. Size evidence for the question

There is no universal minimum number of trials, seeds, scenes, or participants. Plan from the smallest practically meaningful effect, plausible variability, dependence, desired precision or power, and collection cost. A pilot can estimate feasibility and variance; it should not manufacture certainty about a population from a favorable small sample.

A small study can reveal a large difference, while a large collection of correlated frames can leave the central question unresolved. Report uncertainty for the quantity actually claimed, using a method appropriate to the design. For success rates report counts and an appropriate interval when useful. For paired runs, analyze paired differences when the pairing is meaningful. Clustered data may need cluster-level resampling or a multilevel model.

A standard deviation describes variation; it is not the standard error of a mean or an interval for the difference between methods. SD overlap does not establish equivalence or absence of a difference. Non-overlap is not a universal significance test. A non-significant result is not evidence of equivalence without an appropriate equivalence question and analysis.

Source correction: `vs` p6 prints 6.46 ± 26.21 and describes its angle metric as a mean with variance. The table alone does not identify an aggregation unit or justify treating 26.21 as an SD. Ask for the statistic, its units, and its aggregation. Even an SD greater than a nonnegative mean can be mathematically possible; it does not prove timestep pooling or an error.

## 6. Disclose the comparison contract

Different resources can be appropriate when the question is operational performance. Record what each system may use during training and deployment: data and pretraining, sensing, maps, ground truth, model size, compute placement, inference latency, adaptation, parameter selection, and human assistance.

Use matched-resource controls when resource asymmetry is a plausible explanation for the claimed mechanism. If exact matching changes the intended deployment question, report the operational comparison and explain the remaining attribution limit. `carol` p7 reports a strengthened adaptation baseline becoming comparable; this is an informative boundary, not a reason to conceal the comparison.

“Learning preserves the classical planner's safety” needs an argument about allowed parameter ranges, perception, model error, recovery logic, and timing. Keeping a component does not ensure its assumptions survive the wrapper. The physical failures described in `appld_ral` p5 also involve recovery behavior, making the deployed stack relevant to the interpretation.

## 7. Keep evidence types distinct

| Evidence | Can answer | Additional question it leaves open |
| --- | --- | --- |
| Offline prediction | Error on the recorded distribution | What happens when actions change future observations? |
| Closed-loop simulation | Behavior and comparisons within that simulator | Are the relevant dynamics and interactions faithful? |
| Hardware timing or replay | Interface and timing behavior in that setup | Is physical task performance improved? |
| Physical controlled study | Feasibility and comparative effects in the tested design | Does it transfer to other sites, robots, or people? |
| Field deployment or competition | Performance under documented operational conditions | How do tuning, entrants, environment, and other confounds affect attribution? |
| Human evaluation | A specified human outcome with a suitable instrument | Does it measure the broader construct or population invoked? |
| Formal analysis | A property under stated assumptions | Does the implemented system satisfy them? |

These are complementary forms of evidence, not rungs on a ladder. More simulation trials can reduce sampling uncertainty within a simulator; they do not remove simulation bias. A physical demonstration does not automatically outrank a well-controlled simulation on every question.

## 8. Account for every attempt

Define eligibility separately from favorable outcomes. Record success, timeout, intervention, reset, and relevant failure modes; use a stated precedence rule if categories must be mutually exclusive. Timeouts may be their own category. A restricted operating envelope needs both its in-scope results and an account of omitted attempts where relevant.

Traversal time on successes answers a different question from expected mission cost over all attempts. Report the success counts beside conditional time. A failure penalty is another valid metric when justified and explicit; show whether reasonable penalties change the conclusion. `appld_ral` p5 uses a stated penalty; `vs` p6 reports success-conditioned time.

Do not infer uninterrupted completion from reset-separated segments. Disclose reference-assisted alignment, oracle perception, and human recovery. A zero observed failure count is an empirical result with a denominator, not a universal guarantee.

## 9. Resource, benchmark, and theory contributions

A dataset should unlock a defined research question through its collection process, annotations, coverage, and usable access. Size is relevant but cannot substitute for the right information. `mtc` p1 couples motion with scene geometry; `m2p2` p1 motivates passive perception under extreme low light.

A benchmark needs operational task definitions, reproducible scoring, justified coverage, and results showing what it distinguishes. Difficulty is relative to a specified robot, task, and metric. `verti_bench` p9 states a perception assumption that bounds its mobility evaluation. A competition's entrants do not represent the entire field; `barn26_report` pp1,7 reports its participation funnel and untuned trials.

A theory contribution needs exact assumptions and a valid argument, with experiments for empirical claims. A position paper needs a reasoned, bounded synthesis. Neither should receive an automatic demand for a new neural architecture or physical experiment.

Deliver the requested research plan with the decisive comparisons prioritized. If a test is infeasible, identify the narrower conclusion available and the unresolved uncertainty. Do not initiate data collection or robot runs merely because a plan describes them.
