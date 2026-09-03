# How a research program compounds

One paper answers a question. A program makes the next question cheaper to ask. Use this file when the question is what to work on next, not how to write what already exists.

**Scope and caution.** The line names below are **this study's editorial grouping** of 137 coauthored papers, inferred from shared artifacts, citations, and platforms — not labels the authors use for themselves. Verify membership and chronology (`scripts/lookup_evidence.py --query`, then the PDFs) before relying on any line. Page numbers are physical PDF pages. A coauthor list never licenses attributing a method, a sentence, or a belief to any individual.

The grouped lines: APPL (planner-parameter learning), LfH (learning from hallucination), BARN (constrained-navigation benchmarking and challenge), Verti (vertically challenging terrain), IKD (off-road inverse kinodynamics), TCGRE (team coordination on graphs), social navigation (data, benchmarks, language reasoning), tethered UAV and risk-aware assistance, energy and achievable range, wearable inertial pose tracking, causal state abstraction, motion memory, legged locomotion and curriculum learning, human-robot co-transportation, snake robots, low-light and thermal off-road perception.

## 1. The compounding ladder

Steps get skipped and reordered. The one constraint that holds across lines: **each step must emit an object the next step can consume** — a definition, a platform, a generator, a formalism, a scored leaderboard.

| Step | Object emitted | Instance |
| --- | --- | --- |
| Name the bottleneck | a definition or taxonomy others cite | `snake_ras` p1 finds no formal categorization of snake-robot work envelopes and test methods |
| Build the platform that makes it measurable | hardware whose limits are themselves research questions | `vw` p1 ships two wheeled platforms, datasets, and three algorithms |
| Release the dataset, generator, or benchmark | a scored comparison anyone can enter | `navdiffdataset_ssrr` p1 ships BARN, 300 simulated environments |
| Attack the mechanism | a method that needs no new apparatus | `wm_vct` p1 learns the vehicle-terrain forward model |
| Scale or automate the hand-set part | a variable where a constant was | `adp` p1 replaces DDP's "manually designed scheme" with a learned one |
| Generalize across robot, terrain, modality | a transfer claim with a named held-out axis | `car` p1 adapts across vehicle configurations, still on Verti-Bench |
| Consolidate | a formalism, survey, or guideline | `applx` p2 formalizes APPL, adds a cycle-of-learning scheme |

### Three lines walked end to end

**BARN, 2018-2026.** `snake_ras` (2018, p1) states the evaluation gap on the environment side, not the robot side. `navdiffdataset_ssrr` (2020) converts that complaint into an artifact — 300 environments plus a difficulty model (p1) — and cites the 2018 review as its warrant (p2). Difficulty is *defined* by two planners: DWA/E-Band traversal time over ten trials, normalized by path length, 30 s failure penalty (p4). `dynabarn` (2022, p1) extends the same idea to dynamic obstacles. `barn22_report` (2022) makes it a community instrument: 50 unseen worlds, six baselines scoring 0.1627-0.2334, and a published ceiling — "maximum possible score based on our metric" was 0.25 (p2). Four more annual reports follow. `barn26_report` (2026) reports the cold-trial result at full resolution: "Across all 12 cold trials", one succeeded (p7). By 2026 the leaderboard is currency: `applv` p5 introduces a test planner by noting it took second place in the 2025 BARN Challenge.

**Verti, 2024-2026.** `vw` (ICRA 2024) ships two platforms, datasets, and three simple controllers (p1) plus a reconfigurable indoor rock testbed (p3); its future work names the next paper — "design or learn a vehicle dynamics model" (p6). `vw_chrono` (SSRR 2024, p2) reuses the physical testbed's elevation data to build a simulator. `wm_vct` (RA-L 2024) writes the model, opens by saying recent wheeled-mobility results "invalidate both assumptions" of planar rigid-body navigation (p1), and reuses `vw`'s three controllers as baselines, one of which doubles as its ablation (p5). 2025 adds evaluation infrastructure: `verti_bench` (RSS, 100 environments, 1000 tasks, p1) and `verti_arena` (SSRR, an 8x8 m instrumented indoor arena with 0.7 m maximum elevation difference, p1). By 2026 the substrate is fixed and each paper varies one thing on it — `car` p1 varies the vehicle, `va` p1 varies the environment, both evaluated in Verti-Bench and validated on the physical Verti-4-Wheeler.

**Tethered UAV, 2016-2019.** `case_ssrr` (2016) reports two flood deployments and delivers a gap taxonomy — informatics, manpower, human-robot interaction, cost-benefit (p1). Two 2017 application papers attack the manpower gap and expose which component is broken; 2018 supplies it (`localization_ssrr`, `planning_iros`). `tether_fsr` (FSR 2019, 14 pp) consolidates and states the operational claim: human-robot ratio reduced "from 2:2 to 1:2" (p1). The application preceded its own enabling component: the application tells you which component paper is worth writing. Standing weakness — every paper motivates on a human outcome and measures a machine quantity; `servoing_ssrr` p6 correctly claims only "potential to improve teleoperation performance".

## 2. What each follow-up had to add

A follow-up earns its place by changing exactly one thing while holding the substrate fixed. Build this table for your own line before drafting.

| Paper | Yr | What changed | What was reused | Claim newly available |
| --- | --- | --- | --- | --- |
| `applx` | 2022 | nothing empirical except composition; a meta-MDP formalism and a cycle-of-learning scheme (p2, p3) | the four APPL methods, the Jackal/`move_base`/DWA stack (p5), BARN's 300 environments (p8) | the four methods are one object, and can be chained |
| `applv` | 2026 | supervision source becomes a vision-language-action model | the APPL parameter interface, BARN, challenge-vetted planners (p5) | a new learner behind a standardized interface |
| `wm_vct` | 2024 | learned forward dynamics replaces hand controllers | `vw` platforms, datasets, three baselines (p5) | up to 60% success improvement, 46% roll/pitch reduction (p1) |
| `vertiformer` | 2025 | one multi-task transformer replaces per-task heads | same dataset and robot, prior lab models as baselines | joint training beats separate training, "except Z prediction" (p7) |
| `lfh_cp` | 2025 | factorize hallucination into critical points, then generate | the LfH problem formulation and the DynaBARN benchmark (p7) | fixes the mode collapse `dyna_lflh` p6 self-diagnosed (`lfh_cp` p2) |
| `hpr-tcgre` | 2025 | drops three assumptions it attributes to `tcgre` — homogeneity, full observability, free communication (`hpr-tcgre` p1; only homogeneity is explicit at `tcgre` p2) | the graph formulation and a naive no-coordination baseline (p5) | coordination survives a realistic sensing and comms model (p1) |
| `energy_mechatronics` | 2019 | scope widens from ground to aerial and adds an online estimator | the prior model, its ancillary-loss terms, and the wheels-up system-identification test (p9) | "extend and generalize our previous model" (p1) |
| `e_socialnav` | 2026 | distillation attacks latency | the social-navigation reasoning task, with a prior lab system named as the bottleneck | closes the bottleneck `vlm_social_nav` exposed (`e_socialnav` p1) |

The reusable move: **write your assumptions as a numbered list in the problem formulation.** `hpr-tcgre` p1 does exactly this, numbering the three `tcgre` assumptions it relaxes — only the first of which `tcgre` p2 states outright. Two papers, one list.

Corollary, from `hallucination` p8: write future work as the abstracts of your next two papers. That paragraph proposes going beyond 2D ground navigation, and hallucinating so runtime hallucination is "no longer necessary" — both became papers. Conversely, delete any future-work sentence that neither points back to a named limitation nor says what would change if it worked.

## 3. Instruments, not just papers

A benchmark, simulator, testbed, dataset, or competition is a **durable asset**: it outlives the paper that shipped it, and it converts every later mechanism paper from "build an apparatus, then argue" into "add a row".

**What it buys.** `t_cbf` p5 runs its simulation study on Verti-Bench; `car` p1 and `va` p1 both evaluate in it. One capital investment (`vw` 2024 platform and testbed) directly financed a simulator (`vw_chrono` p2) and seeded a line that went on to produce an indoor arena (`verti_arena`), a benchmark (`verti_bench`), and a stream of one-variable mechanism papers. Instruments also carry claims a method cannot: `verti_bench` p6 prints an automatic curriculum losing to a manual one. A benchmark that only confirms its owners' method is not doing benchmark work.

**What it costs, in the corpus's own words.** `verti_bench` p3 concedes that "Chrono is not yet GPU-accelerated", so learning in it takes significant training time, and states it is "not meant to replace existing evaluation setups". `verti_bench` p6 discloses that every learned system evaluated is "not trained in Verti-Bench" — a fairness property and a large confound at once. `verti_arena` p5 blocks a misreading of its own difficulty ranking: low error on a small zone "do not imply" that surface is inherently easy. Competitions cost rules: `barn25_report` p7 records that a no-tuning rule was "too soon for the BARN Challenge" and was reverted mid-event; `barn26_report` p8 deletes the dynamic-obstacle axis to "more precisely benchmark the core capability".

**Where an instrument paper's prose outruns its evidence.** `verti_bench` p8 argues 10,000 simulated trials give "much better statistical significance" than 30 physical trials. More simulated trials shrink sampling variance *inside the simulator* and do nothing about model bias, so they cannot be better at the question the physical trials answer. Repair: say the physical trials agree with the simulated ranking but are too few to detect small differences, and scope the tighter estimates to the simulator. Never end a validation section by arguing validation was unnecessary.

**Design rules the corpus supports.** Publish the ceiling and baselines beside the winner (`barn22_report` p2). State what a difficulty label is relative to — BARN difficulty is DWA/E-Band time at default parameters with a 30 s penalty (`navdiffdataset_ssrr` p4). Withhold exactly one thing (`barn22_report` p2 hides 50 worlds, nothing else). Release the generator, not only the data (`navdiffdataset_ssrr` p1). Make the outcome partition exhaustive so the table is auditable (`verti_bench` p6). Document why a metric was rescaled (`barn25_report` p2: the lower clip moved from 4OT to 2OT as the ceiling was approached).

## 4. Choosing the next paper

Rank candidates by claim leverage per unit of cost, then apply the tests below in order.

1. **Which limitation, if removed, upgrades the most existing claims?** `wm_vct` p5 could reuse three prior baselines only because the platform paper shipped them; fixing the model upgraded the line at once.
2. **What can nobody currently measure?** That is an instrument paper. `verti_arena` p1 names the gap as the absence of a controllable, standardized real-world testbed, not of an algorithm. `verti_bench` p2 argues the existing evaluation *object type* is wrong: interactions "need to be unfolded" (p1), so a static dataset cannot serve.
3. **Which assumption did a new sensor or platform just invalidate?** `wm_vct` p1 opens by saying recent mobility results "invalidate both assumptions" that its field had been building on. An invalidated assumption is a free introduction.
4. **Which result was mixed?** A losing subgroup is a direction with its experiment already built. `verti_bench` p6 turns a surprising loss into a stated direction.
5. **What is currently hand-set that could be estimated?** Read the method section of the paper you admire, find the constant, and learn it (`adp` p1 on `ddp`).
6. **What would make this line obsolete?** Name the sensor, model class, or hardware change that would delete the problem. `compa` (2026) is that answer inside the Verti line: a gimbal-stabilized turret on a rocker suspension leaves the robot chassis "free to absorb the terrain irregularities" (p1), so part of the terrain problem stops being a planning problem. If you cannot name the obsolescence condition, you do not yet know what your line is claiming.

Skeleton for the brief: "`{ARTIFACT}` fixed `{VARIABLE}` by hand because `{REASON}`. `{NEW EVIDENCE}` shows that costs `{MEASURED PENALTY}`. Learning `{VARIABLE}` should recover it, testable on `{EXISTING BENCHMARK}` against `{EXISTING BASELINE}` with no new apparatus."

## 5. Cadence and scope

Observed physical page counts of *published* papers in this corpus — a calibration of increment size, not a rule. **Page limits and submission requirements change; check the current call for papers.**

| Venue | n | Median pp | Range | Typical role in a line |
| --- | --- | --- | --- | --- |
| IROS | 38 | 7 | 6-14 | one-variable mechanism increment |
| ICRA | 22 | 7 | 6-8 | mechanism or resource release |
| RA-L | 16 | 8 | 6-8 | mechanism with fuller evidence |
| SSRR | 12 | 6 | 6-8 | testbed, dataset, field probe |
| RAM | 5 | 8 | 7-11 | challenge / community report |
| CoRL, RAS | 2, 2 | 19, 14 | 16-22, 13-15 | consolidation with appendices |
| THRI | 3 | 36 | 31-65 | survey, guidelines, contested taxonomy |

Read the pattern, not the numbers: conference increments carry one changed variable; journal papers consolidate a formalism plus a composition experiment (`applx` p2); magazine challenge reports carry community findings no single lab can produce; long guideline documents appear where a taxonomy is contested. A workshop paper's deferral list can become the conference paper's sections.

## 6. Collaborators and multi-author lines

Scope is stated in the paper, and it is narrower than the author list. `social_nav_guidelines` p57 delimits each author's role explicitly; the entry for Xiao names a symposium presentation, a position paper, and participation in the Benchmarks and Datasets working groups. That settles **what a person did on that document**. It does not settle who originated an idea, who wrote a sentence, or what anyone believes — and its absence settles nothing at all. Write the same statement for your own multi-author work; when you cite someone else's, cite the paper, not the person.

Personnel is itself a compounding asset — repeated authors across a line are part of why a follow-up is cheap — but that is continuity, not a credit claim. An artifact a collaborator built can anchor your line: `musohu` p2 positions itself between a robot-sensing dataset that is expensive and a human-video corpus that is not robotic.

## 7. Anti-patterns

- **Acronym-family expansion with no new claim.** A family exists only if the stem is a template and each member changes one named thing (APPL varies the supervision source; TCGRE varies the dropped assumption). Adding a letter is not a contribution.
- **A benchmark only its authors can win.** Counter-evidence is the point: `barn22_report` p3 reports that only one entrant beat all provided baselines, and the RobotiXX (GMU) entry finished second at 3/9 behind an external team's 7/9 (`barn25_report` p2, p4). Publish the ceiling, hand out baselines, and let your own entry lose in the printed table.
- **A dataset with no downstream demonstration.** `musohu` p4 trains a behavior-cloning policy on ten trials and calls the result preliminary (p6); `scand` p7 states its own baseline "is not designed to exhibit social compliance". Ship the demonstration *and* the fence.
- **Chasing a model class instead of a bottleneck.** The durable move here is the opposite — narrow the learned interface until the surrounding system's properties are arguable; `applx` p1 says the framework "does not replace existing systems". Standing debt: that inherited-properties claim is asserted, never tested, across the APPL line.
- **A line that never revisits its own earlier assumption.** In the energy line the ancillary-power term is excluded by assumption (`battery_iros` p2 assumes no on-board computation cost), then taken as negligible (`energy_mechatronics` p9) — the term said to matter is never carried by the validated apparatus. In the LfH line a collision-checking and recovery layer runs under the learned planner and, explicitly, under the BC baseline (`hallucination` p5, p7), and is ablated in neither. One row would fix each.
- **Metric drift inside your own line.** A baseline can drift: the same planner on the same benchmark may be reported at different speeds under different failure conventions across papers — an illustration here, not a corpus count. Print the baseline's exact configuration beside every number, and say when a number is not comparable to your own earlier one.
