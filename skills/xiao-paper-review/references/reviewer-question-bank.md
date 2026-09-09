# Questions that lead to a useful revision

Select only the groups relevant to the actual claims. These are prompts for judgment, not a checklist every paper must pass. Source examples identify a place to learn the question; they are not evidence about the manuscript under review. See `review-protocol.md` for severity and delivery.

## Contribution and logical coherence

- What important uncertainty does the paper resolve? If it is unclear, request a precise problem and distinction from the nearest alternative, not stronger adjectives.
- Why should the proposed mechanism address the named failure? Ask for the missing reasoning or evidence rather than an architectural inventory.
- Which contribution survives if the favored method loses? Resource, measurement, and negative-result contributions may remain valuable.
- Can the reader trace each major limitation to a design choice and an evaluation? `squid` pp1–2 provides a clear framing example; the links are promises to test.

## Comparison and mechanism

- What differs between systems besides the claimed mechanism: data, pretraining, sensing, tuning, speed, compute, or intervention? Ask for the material asymmetries and a control only if needed for the attribution.
- Does a tuned or strengthened baseline explain the gain? `appld_ral` p5 illustrates why parameter choices matter. A default baseline can still be appropriate for a clearly labeled out-of-box deployment question.
- Is the ablation a valid alternative system, and are retraining and coupled changes accounted for? `anticipatory_tamp` p4 uses a meaningful zero-estimator baseline.
- Does the system-level study establish individual feature effects? `mrvs` p19 explicitly leaves them open. Accept a bounded system contribution when warranted.

## Generalization, sampling, and selection

- What is held out: scene, participant, session, terrain, robot, task, or time? What remains shared?
- Are observations nested or paired? Request the relevant counts and analysis rather than presuming frame count is independent sample size.
- Were test outcomes used to select checkpoints, thresholds, prompts, or methods? Ask for the full selection procedure and untouched evaluation where the claim requires it.
- Is the claim about the tested cases or a broader population? The number of cases alone does not decide the answer.

## Safety, completion, and runtime

- Is the statement about a formal property, an implemented precaution, or observed failures? Ask for assumptions or empirical counts accordingly.
- Do “success,” “collision,” “reset,” and “intervention” mean the same thing across reported settings? Separate them when they differ.
- What is the complete pipeline's latency distribution, on what hardware, relative to what deadline? Do asynchronous stages or communications affect this?
- Is a safety or energy claim supported by an actual measure of that property? Throughput, completion, and proximity may be relevant proxies but are not interchangeable constructs.

## Data, benchmarks, and simulators

- What question does the collection process make answerable? `mtc` p1 motivates coupling motion with scene geometry; `m2p2` p1 motivates passive sensing when visible light fails.
- Are coverage, labels, contributor counts, split rules, and annotation quality recoverable? Ask for the detail that bears on the claim.
- What makes a difficulty or fidelity label meaningful for the robot and task? `verti_bench` p9 identifies ideal perception as an assumption.
- Do invalid outputs and failed attempts remain in the proper denominator? If conditional performance is informative, report it alongside total failure and coverage rates, not instead of them.
- Are data access, licensing, privacy, and applicable collection permissions adequately reported for the intended reuse? Do not infer a violation merely from public-space data collection.

## Human outcomes and field studies

- What construct is measured, and how well does the instrument capture it? `social_nav_protocol` p4 pilots repeated scenarios; that suggests checks rather than certifying every questionnaire.
- Who participated, how were they recruited, and how do order, familiarity, repeated encounters, or coadaptation affect interpretation?
- Is trajectory prediction being promoted to comfort or social acceptance without a validated bridge? Ask for the proxy label or evidence of the human outcome.
- Does an uncontrolled field result remain bounded to its conditions? A controlled component experiment is needed only when the central claim depends on component causality.

## Theory and hardware

- Which assumptions support the derivation, and does the tested implementation satisfy them?
- Are definitions stable across related formulations? `risk_ssrr` p6 and `risk_ral` p8 use different risk properties.
- Can the claimed physical capability be traced from requirements through design to measurement? `car_jmee` pp6–10 offers this organizational pattern.
- Is a prototype demonstration, projected mission capability, or calibrated measurement being confused? `nasa` pp9,159 separates exploration stages and development needs.

## Statistics and reporting

- What are the effect, estimand, unit, and uncertainty? A p-value alone does not answer practical importance.
- What does `±` mean? `vs` p6 labels spread as variance; do not substitute SD or perform standardized-gap calculations without clarification.
- Does the conclusion preserve mixed conditions and null findings? A lower mean need not imply dominance across every example; SD overlap does not refute a difference in means.
- Can relative improvements and aggregate scores be recomputed using the stated reference set? Ask for reconciliation when they cannot.

Avoid universal trial quotas, a mandatory experiment type based on venue, a significance rule based on SD overlap, or a demand to imitate an author's structure. Every requested change should improve either scientific interpretation or the reader's ability to assess it.
