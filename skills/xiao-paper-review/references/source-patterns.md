# Source-grounded patterns and counterpatterns

Provenance: the user's local collection from Xuesu Xiao's publication page, downloaded 2026-09-02. This is an analytical synthesis across **coauthored** papers. “Research mindset” below means an observable problem-solving practice, not a private psychological claim. All 137 primary papers have an argument-level main-text reading pass; see `evidence-ledger.json` for exact pages and limits. No claim of reproducing results, exhaustively checking proofs, or reading all supplements.

Page references are physical PDF pages. Use `../scripts/lookup_evidence.py --key KEY` to locate the source. Exact numeric or textual reuse requires the original, not just these paraphrases.

## 1. Start with the operational constraint

**Observation:** APPLD motivates context-dependent planner tuning (`appld_ral` pp1–2,4–6); LfH addresses difficult/unsafe collection of constrained-motion experience (`hallucination` pp1–2,5–7); the early panorama simulator responds to an exhibition-space/viewpoint constraint (`car_jmee` pp6–10).

**Transfer:** name the constraint and the insufficient assumption before introducing the technique. This pattern recurs across different methods and eras.

**Boundary:** do not retrofit a dramatic deployment story onto a purely theoretical contribution.

## 2. Make the changed component and retained contract visible

**Observation:** APPLD changes planner parameters; LfH still uses classical checking/recovery; Performer-MPC combines learned costs with optimization (`performer_mpc` pp1,7–8).

**Transfer:** distinguish new module from complete deployed stack, including safety and fallback layers. Show training versus deployment interfaces.

**Boundary:** hybridization is an option, not a universal superior method. Parameter changes cannot remove every limitation of the underlying planner.

## 3. Separate the mechanism claim from the leaderboard result

**Observation:** APPLD's comparisons probe contextual versus non-contextual parameter choices (pp5–6). Off-road inverse kinodynamics ties learning to vehicle–terrain dynamics and exposes transition failure (`offroad` pp6–7).

**Transfer:** use a comparison that distinguishes your explanation from plausible alternatives, then interpret wins and losses.

**Boundary:** an ablation is not proof that no other cause exists; different tuning budgets or information can confound it.

## 4. Keep evidence levels separate

**Observation:** MuSoHu's small downstream cloning demonstration is not complete social validation (`musohu` pp4–6); MTC labels motion tracking preliminary and lists scene-agnostic retargeting limits (`mtc` pp7–8). NASA analog tests and readiness roadmaps are different evidence types (`nasa` pp135–146).

**Transfer:** label dataset coverage, offline accuracy, simulation, physical closed-loop trials, human evaluations, and future uses separately.

**Boundary:** do not require every genre to deliver every evidence level. Narrow the claim to its contribution.

## 5. Audit headline arithmetic and adverse conditions

**Observation:** RTW Table II (`rtw` p5) changes navigation success from80.32% to82.67%: **2.35 percentage points**, approximately **2.93% relative**. Its off-road mean roll/pitch do not uniformly beat every comparator. Physical Table III's5/5 successes remain a small sample. These observations were checked against the rendered table.

**Transfer:** recompute effect sizes, distinguish task/setting, show subgroup losses, and qualify uncertainty. Conditional travel time must be identified.

**Boundary:** a source paper's imprecise prose is a lesson to correct, not a style to copy.

## 6. Validate the measurement, not just the method

**Observation:** Social-navigation guidelines connect context, validated human instruments, traditional navigation metrics, and distributional reporting (`social_nav_guidelines` pp11–14,23–27,41–42).

**Transfer:** define the construct and test whether the metric measures it; record context and parameter choices. A human-derived proxy needs validation in the context used.

**Boundary:** neither a single geometric score nor a universal sample-count heuristic solves the measurement problem.

## 7. Let limitations generate the next test

**Observation:** Off-road transition behavior motivates future sensing (`offroad` pp6–7); MTC identifies retargeting, placement-prior, contact, and tracking limits (p8); the hardware simulator distinguishes unfinished controls (`car_jmee` p10).

**Transfer:** describe a failure, the assumption it stresses, a plausible mechanism, and a test that could distinguish explanations.

**Boundary:** a proposed diagnosis or future solution is not already demonstrated.

## 8. Include system and human cost

**Observation:** Performer-MPC distinguishes model/runtime measurements (pp7–8); NASA energy analysis makes power, mass, terrain resistance, speed, and duty-cycle assumptions explicit (`nasa` pp139–141). Mechanical simplification can increase control work (`car_jmee` p8).

**Transfer:** account for the resource that limits deployment, including sensing, control, data collection, tuning, or operator effort.

**Boundary:** CPU-only model time does not establish end-to-end real-time execution; modeled energy is not measured mission endurance.

## Attribution caution

The social-navigation paper's author-contribution section (`social_nav_guidelines` p57) explicitly identifies Xiao's participation in Benchmarks and Datasets working groups. The full community framework should not be credited to him alone. Apply the same caution to all multi-author work unless contribution statements provide stronger attribution.

## Lessons from the full-length reports

- **Define eligibility before evaluating success.** The social-navigation guidelines separate scenario definitions, desired outcomes, and usage instructions (`social_nav_guidelines` pp28–33). NASA reports 40/64 recharge attempts overall, versus 31/31 within a restricted envelope after excluding certain misalignments, pitch, and contamination (`nasa` p133). An operating-envelope result is useful but is not unrestricted 100% reliability. Transfer: preserve both denominators and explain exclusions.
- **Separate measurement assistance from autonomy.** NASA's cave-model evaluation uses manual scale, reference alignment, and cropping before geometric comparison (`nasa` pp78–83). Transfer: describe the assistance beside the error metric; aligned reconstruction agreement is not automatically unassisted localization accuracy or complete surface coverage.
- **A realistic replay is not a reacting human.** Recorded pedestrian motion cannot respond counterfactually to a new robot trajectory (`social_nav_guidelines` p52); familiarity and human adaptation also affect apparent robot performance (p22). Transfer: distinguish replay, reactive simulation, and human interaction, and report order or familiarity effects where relevant.
- **Comparability is not construct validity.** A shared metric API helps consistent calculation (`social_nav_guidelines` pp53–54), but does not prove that the metric measures comfort or acceptability. NASA's visualization and meshing examples similarly separate visibility, geometry, and missing-data handling (`nasa` pp108,115–122). Transfer: evaluate the actual property claimed, not only the convenience of its representation.

## Additional comparison lessons from the broader corpus

These examples broaden the toolkit beyond the starter papers. Full-main-text records now supersede the initial excerpt-level records. Use these paraphrases as evidence pointers and open the relevant original section before precise reuse.

- **Observe the missing variable, not just increase model size.** VAGN's geometrically identical but visually different obstacles discriminate semantic information (`vagn` p4). CBM holds dynamics/policy machinery common when comparing abstractions (`cbm` p6). LOGICOM adds a logical-helper control to distinguish persuasive content from simply having another helper (`llm_susceptibility` pp3,7).
- **Data quantity is not automatically data quality.** APPLI reports that additional full demonstrations can harm performance (`appli` pp4,6); the implication is to examine information value and expert quality, not assume all additional examples help.
- **A metric label may conceal a different task.** T-CBF's physical success includes continued safe mobility/searching, whereas simulation success concerns reaching the goal (`t_cbf` p6). Keep safety, progress, and task completion separate.
- **Show the losing subgroup.** VertiSelector's physical easy terrain favors manual curriculum 9/10 versus 8/10, while hard terrain favors VertiSelector 5/10 versus 0/10 (`vs` p6). Social-LLaVA's categorical spatial scores and human-rated free-form answers support different conclusions (`social_llava` pp5–6). Do not summarize mixed evidence as winning every metric.
- **Deployment readiness includes workflow.** Flood-assessment case studies expose data-to-decision and staffing constraints (`case_ssrr` pp6–8), not only aircraft capability. A system paper can contribute operational insight without a new neural network.
- **Provenance belongs beside the result.** The energy report explicitly explains extrapolating a weighted, one-active-battery test to an eighteen-battery range (`energy_considerations` p25). That is not a direct eighteen-active-battery endurance experiment. An apparent parameter inconsistency on that page needs clarification, not a guessed correction.
- **Stop unsafe comparisons rather than complete a table at any cost.** The multimodal social-navigation study excludes an RGB-only controller after unsafe close approaches (`multimodal_social_nav` p6). Use simulation, a safety layer, or a justified exclusion and report it.
- **Reconcile internal counts rather than silently normalize them.** MuSoHu reports 13 demonstrators in its abstract/introduction but seven in its collection-method section (`musohu` pp1–3). The ten-trial downstream subset is training data (p4), not the number of physical evaluation trials. Preserve the unresolved discrepancy and request clarification; it does not by itself establish misconduct.
- **Track changes in definitions across a research line.** The earlier risk framework uses relative ordinal levels with an additive construction (`risk_ssrr` pp2–3); a later formulation uses non-completion probability and non-additive survival terms (`risk_ral` p3). Inspect the assumptions of each derivation. Do not treat every paper using the word “risk” as estimating the same quantity.
- **Check the deployed variant.** VI-IKD uses off-board visual encoding and resets after turns in its outdoor baseline protocol (`vi-ikd` pp4,7). LfLH's UAV training trajectories come from constrained simulation, and its quantified UAV comparison trades longer survival against lower SPL (`lflh` pp5–6). Name the actual implementation, setting, intervention, and metric; a broad architectural idea does not establish every proposed variant.

The transferable rule is to preserve what the evidence actually measures, including inconvenient cases. These are reviewer questions and writing lessons, not allegations about authors or universal prescriptions.
