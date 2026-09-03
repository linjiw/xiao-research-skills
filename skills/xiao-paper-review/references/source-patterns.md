# Source-grounded patterns and counterpatterns

Provenance: the user's local collection from Xuesu Xiao's publication page. The corpus was re-downloaded and hash-verified on 2026-09-03; all 137 source files matched the SHA-256 recorded in `evidence-ledger.json`. A second close reading of all 137 papers (136 from extracted full text; the scanned `car_jmee`, which has no text layer, read visually) was then performed in 29 thematic batches plus 9 cross-cutting lenses (titles, abstracts, introductions in two eras, endings, experiments, related work, figures, overclaims). This is an analytical synthesis across **coauthored** papers; "research mindset" means an observable problem-solving practice, not a private psychological claim. No claim of reproducing results, checking proofs, or reading every supplement.

Page references are **physical PDF pages**. Use `../scripts/lookup_evidence.py --key KEY` to locate a source, and open the original before reusing any number or phrasing. Patterns below are structures, not prose to copy. Read the index; open only the sections you need.

## Index — the 19 rules

1. Name the constraint and the insufficient assumption before the technique.
2. Separate the new module from the deployed stack; state what keeps inherited properties.
3. Build one comparator differing in exactly one informative way — zero your own mechanism.
4. Strengthen the baseline until the margin survives, or state the untested caveat.
5. Label evidence tiers separately; name the tier in the sentence carrying the number.
6. Recompute every abstract number from a printed cell; label points versus relative.
7. Define the construct, then test whether the metric moves with it.
8. Write each limitation as precondition → failure → the mechanism that removes it.
9. Price the resource that limits deployment, in the paragraph stating the benefit.
10. For "this is hard", prefer a third party's admission or a counted population.
11. With no ground truth, install a reference population on the identical interface.
12. Print the reference population's own spread beside any between-group gap.
13. Put uncertainty in the symbol: range, censoring token, inline denominator, explicit `NA`.
14. Choose columns that can contradict your headline; explain each losing cell.
15. Trace every headline number to its cell; preserve someone else's discrepancy and ask.
16. Re-check a recurring term's definition each time; never pool across a change.
17. Name the exact configuration behind every headline number, not the architectural idea.
18. Exclude on a stated criterion, in the results section, and re-scope the claim.
19. Publish the ceiling with the metric and the confound beside the claim.

---

## 1. Start with the operational constraint

**Observation:** APPLD names re-tuning cost and the failure of one parameter set across regions of one environment (`appld_ral` p1). LfH names the danger of collecting the data — training requires the robot to "operate in close proximity to obstacles" (`hallucination` p1). The vertically-challenging line attacks a representation choice: partitioning the world "into free spaces and obstacles" discards hardware capability (`vw` p1); CAHSOR names the SE(2) assumption and three physical consequences (`cahsor` p1). M2P2 intersects two individually solved constraints, darkness and passivity, since active emissions "expose the presence of the robot" (`m2p2` p1). MTC names an absent artifact: "no public dataset systematically couples full-body human" motion with scene geometry (`mtc` p1).

**Transfer:** name the constraint and the insufficient assumption before the technique. Prefer one that is physical, economic, or set-theoretic — one a reader can check.

**Boundary:** do not retrofit a deployment story onto a theoretical contribution. A constraint that no proposed mechanism relieves is decoration.

## 2. Make the changed component and the retained contract visible

**Observation:** APPL changes only planner parameters and states that the system "inherits safety and explainability" from the classical stack (`applx` p1), restated as safety "provided by the provable guarantees" of that stack (`applx` p13). But the learned set includes `inflation_radius` and `max_vel_x` (`applx` p5) — the quantities a DWA safety argument is conditioned on. Deployment-time policy selection instead swaps one rule: its baseline runs the same selection equation (`deployment_learning_adaptation` p7) on estimates the paper calls "stale", where the method refreshes them by replay (`deployment_learning_adaptation` p2).

**Transfer:** separate the new module from the deployed stack, including safety layers, recovery behaviors, and fallbacks. State the condition under which an inherited property survives your intervention.

**Boundary:** inheritance is an argument, not a measurement. Where you have collision or failure counts, the counts overrule the argument.

## 3. Build the discriminating control

**Observation:** APPLD (NO CONTEXT) is the same behavior-cloning search run "without context", i.e. without segmentation and switching (`appld_ral` p4). MYOPIC is the paper's own algorithm run with a zero-function estimator, "ensuring fair comparison" (`anticipatory_tamp` p4). VI-IKD uses "same data to train both" models, so only the anticipatory patch differs (`vi-ikd` p5). CBM holds dynamics and learner fixed — "all methods use implicit dynamics models, including CDL", all with Soft Actor Critic (`cbm` p6). Forecast-aware allocation draws every arm from one pool so "differences arise solely from the support allocation" (`temporal_tcgre` p6).

**Transfer:** build one comparator that differs in exactly one informative way, and say so in the sentence defining it. Where possible, build it by zeroing your own mechanism.

**Boundary:** an ablation shows a component helps; it does not rule out other causes, nor settle whether a different architecture would extract the same signal.

## 4. Prove the baseline is not merely mis-parameterized

**Observation:** the corpus refutes default-parameter comparisons itself: the same DWA planner fails "8/10 trials in the narrow" corridor with manufacturer defaults and succeeds in every trial with learned parameters (`appld_ral` p5). LfH states the caveat instead of running the check: "We acknowledge that if re-tuned" per environment, DWA could do better (`hallucination` p6). LfLH runs it, quadrupling the baseline's sampling rate to 24 and 80 and reporting roughly unchanged performance (`lflh` p4).

**Transfer:** either strengthen the comparison arm until your margin survives, or state the untested caveat explicitly next to the result.

**Boundary:** a strengthened baseline bounds one confound, not all. Tuning budget, compute, data volume, and sensing remain separate axes.

## 5. Keep evidence levels separate

**Observation:** Verti-Bench prints the shrinkage: 30 physical trials against 10000 simulated (`verti_bench` p8; §15 works that sentence's arithmetic). RTW titles its small-*n* section "Physical Demonstration" (`rtw` p5) while its conclusion pools that tier with simulation and names a planner absent from the physical table (`rtw` p6). VertiAdaptor's physical section is prediction accuracy over 42.2 s of held-out driving, not closed-loop navigation (`va` p7).

**Transfer:** label dataset coverage, offline accuracy, simulation, open-loop physical prediction, closed-loop physical trials, and human evaluation as separate tiers. Say which tier a number came from in the sentence carrying it.

**Boundary:** not every genre owes every tier. Narrow the claim to the tier you ran.

## 6. Audit the headline arithmetic

**Observation:** RTW reports "2.35%" in navigation success and "122.62%" in off-road mobility in one sentence (`rtw` p1); its table gives 80.32 → 82.67 (2.35 percentage points) and 34.44 → 76.67 (relative) (`rtw` p5). GACL's "6.8% and 6.1%" (`gacl` p1) are relative — 76.67 → 81.85 and 74.65 → 79.21, i.e. 5.18 and 4.56 points — while the same paper writes "−5.49" for an absolute difference (`gacl` p5). VertiSelector's "23.08%" (`vs` p1) is 26/50 → 32/50, twelve points (`vs` p6). T-CBF's "30%" (`t_cbf` p1) is unexplained; the only printed pair giving 30 points is 7/10 → 10/10 at the highest difficulty against one baseline (`t_cbf` p5).

**Transfer:** recompute every abstract number from a printed cell. Name the unit (points versus relative), the denominator set, and the comparator. Pair "up to" with a median.

**Boundary:** a relative figure is not dishonest; an unlabeled one is unreadable. Fixing the label is usually the repair.

## 7. Validate the measurement, not just the method

**Observation:** the community guidelines paper polices one word — "significance" should not be used without the proper test (`social_nav_guidelines` p26) — and gives a falsifiable floor, "at least 30 samples" for real-robot trials, with conditions for overriding it (`social_nav_guidelines` p42). Performer-MPC runs psychometrics on its own instrument, reports that one item "inadvertently prescribes a solution" and inflates a weak baseline's score (`performer_mpc` p22), and labels its outputs "not statistically significant findings" (`performer_mpc` p20). The protocol paper measures its instrument before comparing policies; its strongest evidence is a run in which the robot drove onto a participant's foot and the questionnaire caught it (`social_nav_protocol` p4).

**Transfer:** define the construct, then test whether the metric moves with it. Report the metric's parameters, units, and range. Find the case your measure catches and the incumbent misses.

**Boundary:** comparability is not construct validity. A shared API or a bigger sample makes numbers consistent, not meaningful.

## 8. Let limitations generate the next test

**Observation:** VI-IKD names unseen terrain as "essential in off-road conditions" (`vi-ikd` p7), and later terrain-representation papers answer it. CBM's one-sentence limitation names assumption, extension, and domain — relax the factored-state assumption to "extend CBM to high-dimensional state" spaces (`cbm` p7); WM-VCT titles its closing section "CONCLUSION AND LIMITATIONS" (`wm_vct` p7). Dyna-LfLH self-diagnoses mode collapse (`dyna_lflh` p6); the successor takes that diagnosis as its problem statement and explains why the obvious fix fails, since extra obstacles create the illusion of a safe "tunnel" (`lfh_cp` p2).

**Transfer:** write each limitation as precondition → failure → the mechanism that removes it. A limitation specific enough to be a method section is a project; a shopping list is a purchase order.

**Boundary:** a proposed diagnosis is not a demonstrated one; a named fix is not a tested one.

## 9. Count system and human cost

**Observation:** APPLD prices its own search — "approximately eight hours" on one laptop with 16 threads (`appld_ral` p4). Anticipatory TAMP reports minutes per labeled example and calls the operation "prohibitive to do during planning", which is why it is learned (`anticipatory_tamp` p5). CARoL reports ten adaptation iterations of eight trials, "approximately 130 minutes in total" (`carol` p7). APPLV discloses that the robot sends observations to an off-board GPU server, at roughly 0.41 s per prediction (`applv` p6).

**Transfer:** price the resource that limits deployment — compute, latency, annotation, tuning, operator attention, collection time — in the paragraph that states the benefit.

**Boundary:** a model-only timing figure does not establish end-to-end real-time execution, and off-board inference is not onboard efficiency.

## 10. Borrow an external authority's admission of difficulty

**Observation:** APPLD backs its tuning-cost claim by quoting a widely used navigation tuning guide's admission that the task is hard for users who are "sophomoric" about the concepts (`appld_ral` p1). A challenge report attacks a belief rather than a paper: deployed systems "may create the perception" that ground navigation is solved (`barn22_report` p1). A survey inverts the usual motivation for learning with a count from its own corpus: manual hyperparameter search was required for "73 out of 74" surveyed approaches (`ml4nav_survey` p24).

**Transfer:** to establish that a problem is hard, prefer a third party's admission, a counted population, or a documented deployment outcome over your own assertion.

**Boundary:** a borrowed admission dates. Cite what the source says, with its year, and do not extend it to systems the source never examined.

## 11. Convert an ungradeable task into one with a reference population

**Observation:** the Earth Rover Challenge scores AI teams and top human gamers on the same platform, missions, and scoring, isolating policy rather than hardware (`erc2024` p1–p2). BARN later imports the device as a normalizer: "a human teleoperated trial" per course sets the denominator for robot traversal time (`barn26_report` p3). The vertically-challenging platform paper uses a human run as a feasibility certificate — courses "can be conquered by human teleoperation" and are therefore within the vehicle's mechanical limit (`vw` p6). APPLD uses the demonstrator as a "point of reference", not a baseline (`appld_ral` p5).

**Transfer:** with no ground truth, install a reference population on the identical interface. Distinguish its three roles: upper bound, normalizer, and certificate that the task is solvable.

**Boundary:** a human reference is only as comparable as the interface. Asymmetric affordances — AI teams received up to three interventions with points halved, humans none (`erc2024` p2) — make the ranking a joint statement about policy and protocol.

## 12. Report the within-group spread beside the between-group gap

**Observation:** the challenge report gives a 20.84-point gap between the last human and the best AI team, then the denominator that makes it legible: the entire human spread was "merely six points" (`erc2024` p7). Elsewhere spread swallows gap — HUMAIN's ADE is 0.578 ± 0.374 against 0.753 ± 0.397 (`humain` p6); VertiSelector reports roll as 6.46 ± 26.21 degrees, incompatible with a per-trial reading (`vs` p6). PIETRA is the counterexample that works: deviations over five seeds are ±0.01–0.02 against much larger gaps (`pietra` p5).

**Transfer:** print the reference population's own spread beside any between-group difference, and state the unit it is computed over.

**Boundary:** overlapping error bars do not prove equivalence, and printing ± is not a test. Say which you are claiming.

## 13. Encode uncertainty into the notation

**Observation:** a system diagram gives one number where latency is stable and the range "[1, 2,000 ms]" where it is not (`erc2024` p6). LfLH uses ∞ as an explicit did-not-complete token, not an imputed time (`lflh` p5). The RL benchmark prints the success denominator inside every timing cell — `4.6 ± 0.8 (3/3)`, `N (0/3)` (`navbenchmark` p6).

**Transfer:** put uncertainty in the symbol, not only the caption. A range, a censoring token, an inline denominator, and an explicit `NA` each carry information a mean deletes.

**Boundary:** notation discloses; it does not repair. A censored cell still means an unmatched comparison.

## 14. Show the losing subgroup

**Observation:** APPLR reports its advantage shrinking with difficulty — 58% versus 5% of environments on Easy, 31% versus 4% on Difficult — and conjectures a ceiling in the underlying planner (`applr` p5). VertiSelector prints a physical row where the manual curriculum wins Easy 9/10 to 8/10, beside Hard 5/10 to 0/10 (`vs` p6). Social-LLaVA loses its own Overall row, 0.29 against 0.30 and 0.32 (`social_llava` p5). PIETRA reports that one ablated loss alone "leads to the best" in-distribution accuracy (`pietra` p6). A benchmark reports automatic curriculum losing to manual — "the results suggest otherwise" (`verti_bench` p6).

**Transfer:** choose a column set that can contradict your headline, print every cell, and spend a paragraph on the mechanism behind each loss, not the excuse.

**Boundary:** printing a losing cell is not explaining it, and a prose explanation is a hypothesis until measured.

## 15. Reconcile internal count discrepancies rather than normalizing them

**Observation:** MuSoHu reports "13 humans" in its dataset summary (`musohu` p1) and "seven human demonstrators" in its collection procedure (`musohu` p3). A benchmark's body cites 88.6 s as a planner's best survival time while the table on the same page lists 62.7 (`navbenchmark` p5). VertiCoder describes a frozen encoder of "3.67 million" parameters (`verticoder` p3) inside a model totalling 2.71 M (`verticoder` p5). AutoSpatial prints one model row twice on a page, 6.471 in one table and 6.065 in the other (`auto_spatial` p5).

**Worked case:** Verti-Bench limits its physical tier to "three systems and five trials each", "totaling 30 trials" (`verti_bench` p8). The printed factors give 15. The same page builds the testbed in two configurations, "low and high elevation", and its Table II prints a separate 3×5 block for each — a reconciliation to 30 that is this study's inference, not a sentence the paper writes. Report it as a question about the missing factor, not as a wrong total.

**Transfer:** before submission, trace every abstract, intro, and conclusion number to the cell producing it, and grep each headline noun against every caption. In someone else's paper, preserve the discrepancy and ask; do not guess a correction.

**Boundary:** an unreconciled count is a reproducibility defect, not evidence of misconduct. Raise it as a question about the number, not a claim about the authors.

## 16. Track a definition that changed across a research line

**Observation:** an early risk framework stipulates additivity (`risk_ssrr` p3); the successor derives risk as a probability and reports the reversal — formal methods reveal "risk's non-additivity and history-dependency" (`risk_ral` p8). T-CBF's simulation success is reaching the goal (`t_cbf` p5) while its physical success is remaining safe and "searching for feasible paths towards the goal" (`t_cbf` p6), both printed in one table. SQUID's simulated success is reaching the tunnel exit without a reset (`squid` p5–p6); its physical success is traversing 80% of the tunnel without external recovery (`squid` p7).

**Transfer:** when a term recurs across a line, check the derivation each time. A stipulated axiom is a hypothesis; refuting your own earlier definition is a contribution if you say which quantity changed.

**Boundary:** two papers using one word are not measuring one thing. Never pool numbers across a definition change, or cite the later number for the earlier claim.

## 17. Name the deployed variant, not the architectural idea

**Observation:** HACL's headline column reports energy −4000, stability 2000, 90% success (`hacl` p4), matching the LSTM column of the architecture table rather than the RNN column at −2600, 1400, 80% (`hacl` p6), while the method text names the architecture only generically as an RNN and writes its update with an LSTM (`hacl` p4). VANP benchmarks a variant it names VANP-50 (`vanp` p3) and deploys VANP-18 (`vanp` p5). TransCurriculum's abstract carries 6.3 m/s (`transcurriculum` p1); a footnote reads "Reported for command only", and the full curriculum reaches 5.8 (`transcurriculum` p7).

**Transfer:** name the exact configuration behind every headline number — variant, hardware placement, data budget, ablation arm. A method name denoting different configurations in different tables is the commonest way a good result becomes unreproducible.

**Boundary:** a broad architectural idea does not establish every proposed variant, and a variant's number does not transfer to the family.

## 18. Stop an unsafe comparison and report the exclusion

**Observation:** a multimodal study excludes the RGB-only controller after it moved dangerously close to participants — "we exclude the RGB module" from the human study (`multimodal_social_nav` p6). A planner is dropped from physical evaluation for poor performance and "safety considerations for the physical testing" (`adp` p7). CARoL omits four baselines from hardware for stated data-cost reasons and re-scopes what that tier proves; in the simulated tier it strengthens RMA until the enlarged version "obtains comparable performance" (`carol` p7).

**Transfer:** exclude on a stated criterion, in the results section, and re-scope the claim that arm would have supported. An exclusion with a reason is evidence; a missing row is a hole.

**Boundary:** an exclusion changes what the tier establishes. If the strongest comparator is absent, the tier shows feasibility, not superiority.

## 19. Declare what a competition or challenge can and cannot establish

**Observation:** the first BARN report publishes the metric's ceiling — baselines score 0.1627 to 0.2334 against a maximum possible 0.25 (`barn22_report` p2) — making every later score interpretable. The fifth gives a complete tuning-dependence measurement across all 12 cold trials — "only a single cold trial was successfully completed" — names the exception, then supplies the best alternative explanation for its own ranking: wireless interference tracked a neighboring competition's schedule, one team losing most of its session (`barn26_report` p7). The fourth names a defect in its own course design, penalizing a team for reasons "which was not fair" (`barn25_report` p9).

**Transfer:** publish the ceiling with the metric, the participation funnel with the leaderboard, and the confound beside the claim it undermines. Treat approach to the ceiling as a measurement about the instrument.

**Boundary:** a challenge measures entrants, not the field. Attendance, self-selection, and protocol changes explain most cross-year trends before methods do.

---

## Attribution caution

The community guidelines document lists 31 authors (`social_nav_guidelines` p1); its contribution statement records Xiao as "a presenter at the symposium", a position-paper contributor, and a contributor to the Benchmarks and Datasets working groups (`social_nav_guidelines` p57). The framework should not be credited to him. Apply the same caution to all multi-author work: cite the paper, not a person, unless a contribution statement supports more. Throughout this file a pattern belongs to a paper and a page, never to an individual.

## Counterpatterns: craft observations, not accusations

Each item is an observation about a sentence, caption, or table cell. The corpus is not a style authority; several appear in papers that also hold its best calibration writing, sometimes three pages apart.

- **A summary names a metric its table lacks.** A conclusion credits gains in success, safety, and efficiency where the physical table reports success, progress, and time only (`adp` p7). *Repair:* a summary may name only metrics that appear in a table.
- **A caption is stricter than the setup it summarizes.** A results caption reads "ON UNSEEN TERRAIN" (`cahsor` p8) where the setup says testing occurred at "locations with similar terrain" (`cahsor` p6). *Repair:* name the axis held out; captions travel further than setup paragraphs.
- **A section heading asserts what its own body declines to assert.** A heading uses "Significantly" for a difference in pipeline evaluability, while the body beneath hedges with "suggests" and "likely reflects" (`barn26_report` p7–p8). *Repair:* audit headings last, against the paragraph beneath them.
- **A conclusion overwrites a correctly reported null.** A results section reports no significant multimodal advantage over point-cloud-only; a conclusion on the same page claims a clear advantage in both studies (`multimodal_social_nav` p6). *Repair:* read the conclusion against the negative results, not the abstract.
- **A guarantee verb sits over an empirical adequacy claim.** A certificate paper states plainly that qualitative validation "does not constitutes a formal proof" (`t_cbf` p5) — the model sentence. *Repair:* reserve guarantee verbs for theorems with stated assumptions, or a measured zero-rate with its *n*.
- **A proxy label surviving onto the number is the good version.** Trajectory divergence is introduced "as a proxy for socially compliant behavior" (`humain` p6), and the abstract sentence carrying the 29.8% still calls them "trajectory prediction metrics", though the surrounding abstract prose calls the behavior socially compliant (`humain` p1). *Repair for the bad version:* the proxy label must survive into every sentence that quotes the number.
- **Naming a speculation as untestable is the good version.** "we cannot validate this speculation", with the blocking reason attached (`social_llava` p6).
- **A non-comparability warning is the good version.** A dynamic-navigation paper forbids pooling because slower obstacle speeds made "the physical experiments comparatively easier" (`dyna_lflh` p6). *Repair for the bad version:* if two tiers are not comparable, say so where both numbers appear.
- **A limitation that blocks a specific misreading is the good version.** A testbed paper states that low error on one small zone does "not imply" the surface is easy in nature, and names the mechanism (`verti_arena` p5).
- **Extra supervision can reduce performance, and saying so is informative.** Additional demonstrations collected where the default system already worked introduce "suboptimal parameters and consequently worse performance" (`appli` p4). *Repair:* examine information value, not example count.

## The transferable rule

Preserve what the evidence actually measures, including the inconvenient cases. Every pattern above reduces to one discipline: make the claim narrow enough that the table can hold it, then print the table that could refute it. These are reviewer questions and writing lessons, not allegations about authors, and not universal prescriptions.
