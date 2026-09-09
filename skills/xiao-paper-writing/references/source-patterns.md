# Source patterns: observation, transfer, boundary

This index connects research and writing decisions to coauthored papers. It is an analytical synthesis, not an author's private philosophy. Retrieve a key with `scripts/lookup_evidence.py`, then open the original before making a precise source claim. Pages below are physical PDF pages. Consult each record's coverage: a prior full main-text study and the 2026-09-09 selected-section rereading are distinct.

## Choose the relevant pattern

| Pattern and verified source location | Source observation | Transfer to a new project | Boundary |
| --- | --- | --- | --- |
| Requirements lead the architecture: `car_jmee` pp6–10 | The scanned article moves from an external-view display problem through coordinated mechanical/control subsystems to functional demonstrations and unfinished control work. | Make requirements explain components, then make tests answer those requirements. | Demonstrating display functions does not establish all proposed training or user benefits. |
| Price the whole system: `energy_considerations` p3; `energy_mechatronics` p1 | Range estimation considers the energy consumers beyond propulsion and motivates preventing immobilization. | Measure the resource that limits the mission, including non-algorithmic costs. | A model's insight is conditional on its calibrated loads and operating regime. |
| Define stages of feasibility: `nasa` pp9,159 | The report separates exploration stages and near-term reconnaissance from deeper access requiring further development. | State which enabling capability each study establishes and what the next stage requires. | Terrestrial analogs and proposed missions have different evidence status. |
| Make a deployment nuisance the research problem: `mocap_icra` pp1,6 | Sensor movement in garments undermines rigid-placement kinematic assumptions. | Explain why the user-friendly interface breaks a modeling assumption, then test the proposed compensation. | Better pose tracking is not automatically evidence of downstream human benefit. |
| Change a narrow interface: `appld_ral` pp2,5; `apple` p1 | Context-dependent planner parameters and different forms of human input become learning targets. | Consider changing the expensive or brittle decision inside an existing system. | Retained components confer properties only if their assumptions still hold. |
| Relax a specific dependency: `applr` pp1,6; `sober` pp1,6 | One changes demonstration-limited adaptation; the other removes runtime hallucination requirements. | Describe the requirement removed, what replaces it, and the new cost. | Removing a dependency can introduce another; measure both. |
| Anticipate information: `vi-ikd` p1 | Visual terrain information is motivated by the limits of reacting from inertial history. | Ask what needs to be known before the action and which signal can supply it. | A multimodal system gain alone does not isolate the information channel. |
| Reformulate instead of merely enlarging: `lfh_cp` pp1–2 | Dynamic-obstacle generation is factorized around critical points after diagnosing mode collapse and a misleading tunnel effect. | Find a representation that preserves the needed constraint while simplifying the variable to learn. | The diagnosis and the proposed repair each need evidence; a good explanation is not its own test. |
| Map limitations to design: `squid` pp1–2 | Numbered limitations connect prior approaches, procedural environments, and expert-to-student transfer. | Let the reader trace the reason for each major design choice. | A correspondence in the introduction is a commitment, not validation. |
| Reconsider an abstraction: `vw` pp1,6; `wm_vct` p1; `tnt` p1 | Traversable rugged terrain challenges a flat-world obstacle/free-space treatment. | Separate a platform's capability from what the current representation permits. | Mechanical feasibility, model accuracy, and autonomous completion require different tests. |
| Preserve structure while adding information: `pietra` p4 | Physics enters both a probabilistic prior and a training loss. | Explain where domain knowledge enters the mathematics and what ambiguity it resolves. | Separate the contribution of each route when the mechanism claim depends on it. |
| Validate the measurement: `social_nav_protocol` pp1,4; `social_nav_guidelines` p11 | A rating protocol is piloted across conditions; the guidelines explicitly reject one universal protocol for all questions. | Choose and check the instrument for the specific construct. | A pilot or consensus recommendation does not certify universal validity. |
| Let interaction unfold: `verti_bench` pp1,9; `mtc` pp1,7 | Mobility depends on interaction; scene-conditioned motion requires geometry-aware evaluation. | Match the evaluation object to what decisions change over time. | Offline agreement and simulator outcomes do not automatically establish deployment behavior. |
| Separate training from runtime information: `sbt` p1; `humain` p1 | Rich training signals support a restricted inference interface. | Specify which information teaches the model and which is actually needed during operation. | Distillation does not itself demonstrate latency, robustness, or social benefit. |
| Turn deployment into a measurement: `barn26_report` pp1,7 | The report identifies entrants and exposes tuning dependence with cold trials. | Measure adaptation and integration effort alongside tuned performance. | The entrants and uncontrolled conditions limit class-wide causal conclusions. |
| Distinguish package benefit from component effect: `anticipatory_tamp` p4; `mrvs` p19 | A zero-estimator comparator isolates one planning addition; an integrated interface study explicitly leaves feature effects open. | Make the claim match whether the design evaluates a mechanism or a package. | Either contribution can be valuable; do not force causal claims onto an integrated evaluation. |
| Revisit definitions across a line: `risk_ssrr` p6; `risk_ral` p8 | An additive risk index gives way to a probability formulation with non-additivity and history dependence. | Make changed definitions and assumptions explicit in a follow-up. | The same word across papers does not guarantee the same quantity. |

## Counterexamples improve the guidance

The source corpus and this skill package can both make mistakes. Preserve useful patterns without treating their authorship or repetition as validation.

- `vs` p6 provides an instructive reporting ambiguity: the prose calls the angle spread variance, while the table uses `±`. The previous skills assumed SD and claimed the values could not describe trial-level variation. That inference was unsupported. Ask what statistic, units, and aggregation were used.
- `vs` p6 also reports an easy physical condition favoring the manual curriculum and a hard condition favoring the learned one. A conditional claim retains that information.
- `appld_ral` p5 explains a failure penalty and recovery-related failures. A comparison must be read with these definitions, not only its headline time.
- `hirl_vision_paper` p3 identifies itself as a vision and agenda rather than a systematic survey. Evaluate its argument accordingly.
- `social_nav_guidelines` p11 argues for question-dependent methodology. It is evidence against turning this collection into one mandatory paper template.

## How to use a precedent

State the observation, explain your inference, and propose the decision it informs in the user's project. Verify page versions and precise claims. Do not cite a source as evidence for the user's unpublished method, import its results, or attribute a coauthored contribution to one person without evidence.
