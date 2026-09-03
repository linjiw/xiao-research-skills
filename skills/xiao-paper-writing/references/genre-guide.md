# Match evidence to the contribution

A study-derived rubric, not a venue checklist. Apply only what bears on the actual claim; mixed papers need two branches. Corpus composition, from the `paper_type` field of `evidence-ledger.json` (137 coauthored papers, 2012-2026): algorithm 83, dataset/benchmark 18, survey/position 7, hardware/field 7, challenge report 6, theory/planning 5, technical report 4, human study 3, simulator 2, workshop abstract 2.

| Genre | Main evidence obligations | False demand to avoid | The question that decides delivery |
| --- | --- | --- | --- |
| Algorithm / learned or hybrid system | Defined information and interfaces; a relevant baseline with disclosed contract; mechanism-isolating comparison; failure and transfer boundaries; operational cost | It must replace classical components or use a larger model | Zero the mechanism, hold all else fixed: do the numbers move? |
| Dataset | Why existing data cannot answer the question; collection and annotation protocol; splits and leakage risk; access, license, consent; a rebuild-grade spec | It must also introduce an algorithm or benchmark the field | Could a stranger answer a new question with it, unaided? |
| Benchmark / simulator / testbed | Task generation and coverage; success and failure defined quantitatively before results; a training and tuning rule; evidence it discriminates; inherited validation kept separate | It must prove deployment readiness or beat a prior benchmark | Do systems score differently for a reason the paper can name? |
| Theory / planning / control | Precise definitions and assumptions; valid derivation; scope of the guarantee; approximation and complexity; experiments only for empirical claims | A theorem is invalid without a robot experiment | Does each assumption travel with its guarantee, and does the implementation satisfy it? |
| Human / social study | Construct validity; population and context; protocol, order, blinding, familiarity; participant as the independent unit; uncertainty and agreement coefficients; ethics | Proximity, imitation, or collision avoidance alone proves comfort | Is the unit the participant, and the measure experience rather than geometry? |
| Hardware / field system / case report | Requirements to design choices; integration tradeoffs; calibrated measurement; operating conditions; interventions and failures; achieved versus proposed capability | ML ablations are required, or an analog demo proves target readiness | Can a reader predict, in physical units, where it stops working? |
| Survey / position / methodology | Scope and selection rule; fair taxonomy; supported synthesis; counterexamples; normative recommendations that cost the authors something | Every statement needs an experiment, or the framework must be proven | Is the inclusion rule stated, and would a recommendation fail the authors' own papers? |
| Challenge or competition report | Rules, scoring and tie-breaks fixed before any number; the participation funnel; per-entry results including non-finishers; confounds beside claims; rule edits traced to failures | It must contain a method, hypothesis, or controlled comparison | Were rules fixed before results, and is the attrition denominator printed? |
| Technical report | Claim-type labeling throughout (measured / projected / borrowed / proposed); qualifiers preserved when a result is lifted into a summary; rejected candidates with their disqualifying mechanism; a dated roadmap | Calibration is optional because it is not peer reviewed | Does every headline claim carry its own evidence type? |
| Workshop abstract / late-breaking report | One idea, its epistemic status marked, a deferral list precise enough to be the next paper's outline, genre declared in the title | Full experiments, ablations, or baselines | Does it name what it does not know, precisely enough to study? |

## Genre notes with sources

**Challenge report.** Rules precede results: `barn26_report` p3 fixes a cold trial run "without any fine-tuning" and a human-teleoperated time normalizer before the physical results table (Table II, p4). The attrition funnel goes in the abstract (17 simulation entrants, seven invited, four competing, p1), a confound gets its own subsection (wireless interference hitting one team and not another, p7), and the headline is bounded by its count: one success in 12 cold trials (p7). The recurring defect is headings that outrun their hedged bodies - p7's "Significantly Outperform" heads a body about how many entries were evaluable.

**Technical report.** `nasa` p133 is the template for a conditional success rate: raw rate with denominator (40 of 64 trials, 62.5%), each stress condition with its own rate (69% clean, 33% with simulant), then the fenced subset with its own n and exclusion list (31 of 31, 100%). The failure mode is upward compression: p10 reports DEM "errors of less than 50m" where p65 says *most* errors, *after* ICP alignment, against a reference of nearer 300 m/pixel. Copy the qualifier, not the number. The roadmap dates itself and so stays falsifiable ("possible now" / 10-20 years / 20-30 years, p143).

**Workshop abstract.** `compound_icra15_ws` p1 is one page, no results table, cross-field transfer marked as conjecture ("also serves as a hypothesis"), closing on an open cross-field question it has not studied; its unfenced verb ("to replicate," no metric) is the register's cost. `sss21_appl_tr` p1 declares the genre in its title ("Extended Abstract:") and claims a gap legitimate here - the recipe does not exist - yet sells "parallelized" with no throughput number.

**Simulator and testbed.** Separate inherited from new validation: `faas` p2 notes its solver was already "validated against both real-world compartment fire" experiments, yet p7 sets a predicted peak irradiance of 55.8 kW m^-2 against Table I's measured 8.4 (p6) and calls it "same trends as the predicted values" instead of reporting an error. Grounding buys credibility: `vw_chrono` p2 builds its heightfield from elevation collected by driving the physical testbed; `verti_arena` p4 proves its terrain zones distinct with a per-zone forward model that omits environmental features "to highlight the differences caused by them."

**Human study.** `viewpoints` p8 reports t statistics, p values, Cohen's d and sample counts; p9 publishes every affordance manifold's area, including the one that breaks the argument, fencing the claim to "all the affordances except manipulability." `mrvs` p6 reports an agreement coefficient (Cohen's kappa = 0.72) and confesses in its dataset section that ten single-robot sessions over ten days stand in for simultaneous coverage (p9). `social_nav_guidelines` p26 says "significance" should not be used without the test; p42 suggests 30+ real-robot samples.

**Dataset.** Compete on kind, not size. `scand` p3 disqualifies the THÖR dataset by its data-generating process - a "socially unaware, pre-defined path for the robot" - which no extra hours fix, then scopes its utility demonstrations, declaring policy benchmarking "out of scope for this paper" (p7). Its control is cheap: sixteen trajectories, two demonstrators, one route, so route choice cannot explain the classification (p5).

## Venue and format calibration

Observed physical PDF page counts of all 137 corpus papers, references and appendices included (the 14-page IROS entry, `coral`, carries an algorithm appendix, p13). **Observations, not rules.** Limits, formatting and supplement policy change yearly and differ per track; read the current call for papers, and never infer a limit here.

| Venue | n | Median | Range |
| --- | --- | --- | --- |
| IROS | 38 | 7 | 6-14 |
| ICRA | 22 | 7 | 6-8 |
| RA-L | 16 | 8 | 6-8 |
| SSRR | 12 | 6 | 6-8 |
| RAM | 5 | 8 | 7-11 |
| THRI | 3 | 36 | 31-65 |
| CoRL | 2 | - | 16, 22 |
| RSS / AAAI / ICML / ICASSP / CHI | 1 each | - | 11 / 9 / 30 / 5 / 22 |
| Other conferences | 7 | 10 | 5-14 |
| Other journals | 7 | 15 | 11-29 |
| Preprints | 11 | 8 | 7-20 |
| Workshop | 5 | 7 | 1-10 |
| Technical reports | 4 | - | 2, 6, 27, 176 |

All five RAM entries are challenge reports; the THRI entries are surveys or consensus documents.

**Supplement culture.** Recomputed over the `artifacts` field of the 137-entry ledger: 82 entries list a video, 28 a website, 15 a presentation, 12 code, 10 a dataset, 10 a poster. (A larger public listing gives a higher count; state your denominator and method.) Video presence tracks venue - IROS 34/38, ICRA 17/22, RA-L 11/16, SSRR 7/12, against RAM 0/5, THRI 0/3, technical reports 0/4. In this corpus about three quarters of conference and letter papers ship a video (74 of 102); treat that as this group's practice, not a venue requirement, and budget it early. Code and dataset releases are the exception - a gap to close, not a standard to copy.

## Mixed contributions

Obligations add; they do not average. A dataset paper that also ships an algorithm still owes the full collection protocol.

Ask what survives if the numbers are wrong. If the artifact still stands, it is the contribution, its obligations dominate, and the numbers become a utility demonstration labeled as one. Let the contribution list declare it - one type label per bullet, as in `mrvs` p3 ("Testbed environment", "System artifact", "Implications for design").

- **Dataset + algorithm.** `scand`: dataset obligations dominate; the learned planner shows only that the data is learnable, and benchmarking is declared out of scope (p7).
- **Simulator + method + study.** `vw_chrono` p1-2 lists all three as bullets; the paper stands on the simulator's grounding argument (p2) and the honest label over its small physical section ("Physical Demonstration", p4).
- **Benchmark + multi-system study.** `verti_bench`: benchmark obligations dominate - quantitative failure definitions (p5), a no-training-on-the-benchmark rule (p6) - and the comparison shows the instrument discriminates. The physical tier is downgraded in text: 30 physical trials against 10000 simulated, power difference stated (p8).
- **Theory + algorithm.** `tcgre`: the assumption rides with the guarantee in the intro (p1), and two experiments test the paper's own complexity analysis rather than beat anyone (p7).
- **Sibling submissions.** `faas` (simulation) and `fire` (hardware) came from one group in one cycle; neither reference list names the other (`faas` p8, `fire` p8). Write the cross-citation and a one-line division of labor into both.

## Recurrent checks across genres

- The experimental unit can be a person, run, environment, robot, trajectory, or seed - not a frame. One course run twenty times is n = 1 course.
- "Generalization" must name what changed and what remained shared. Safety, liveness (not getting stuck), and goal completion can require different metrics.
- Baselines need relevance and disclosed contracts, not mechanical equality in every resource. A default-parameter comparison measures parameterization: in `appld_ral` p5 the same planner goes from failing 8/10 trials to succeeding once its parameters are learned. Disclose asymmetries that run against you (`humembr` p5 gives its method three seeds, the baseline one, and says so); strengthen a baseline until your advantage might vanish (`carol` p7 enlarges RMA's adaptation module and reports it becomes comparable).
- Definitions, scoring rules, and exclusion criteria precede the first number, in every genre.
- Attach the tier to the number in the sentence where it appears: simulation, physical open-loop prediction, physical closed-loop. Never pool tiers in a conclusion, and trace every abstract number to one table cell or figure label.
- A relative percentage over small integer counts carries the raw counts beside it. "Significant" requires a test (`social_nav_guidelines` p26).
- A mechanism can be useful in a limited domain; scope correction is often the legitimate remedy. Never infer individual authorship of a method, writing move, or belief from a coauthor list.
