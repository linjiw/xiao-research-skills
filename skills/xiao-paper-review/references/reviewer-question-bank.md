# Reviewer question bank

Grouped by **claim type**, not paper section. Each question is answerable from the manuscript and carries the *cheap* answer that closes it; a question with no bounded answer is a demand, not a review. `key pN` marks a corpus paper where the question is live (physical page) — craft observation, never accusation. See `review-protocol.md` for the read order these feed.

## Read this first: questions not to ask

Rule these out before you open a claim-type section below.

- **"Run 100 physical trials."** Per-cell budgets here are around ten — `vertiformer` p7 Table 1 x/10, `adp` p7 Table IV x/8. Ask for the count in the caption and a claim scaled to it; `verti_bench` p8 publishes its own shrinkage to 30.
- **"Add a robot experiment"** to a theory paper, or **"add an ablation"** to a field report. Match the demand to the genre (`genre-guide.md`).
- **"Compare against every baseline."** A comparator dropped with a stated reason is a disclosure: `carol` p7 names what it cannot run physically, and rescopes that tier.
- **"Report every metric."** An explained absent column beats a padded one — `appld_ral` p6 omits real-world time because "a quick traversal is not the purpose" of that demonstration.
- **"Match every resource."** A structural asymmetry, disclosed and checked, is fine: `e2e_params` p3 omits a penalty reward from one arm, promising it "will not deteriorate the collision avoidance behavior".
- **"Run a statistical test"** where n makes one meaningless. At three to five trials per cell ask for raw fractions; `social_nav_guidelines` p26 bars significance language "unless the proper statistical tests are conducted". Delete the word, print the number.
- **"Show that this is surprising."** A foregone conclusion is fine when the paper says so: `scand` p7 calls a baseline's loss expected, since it is "not designed to exhibit social compli[ance]".
- **Anything about the authors.** Do not guess identity, ask what they believe, or require a citation to your own work.

## Superiority over a baseline

1. Was the baseline at defaults, and does the gap survive re-tuning? `appld_ral` p5: the same DWA fails 8/10 at defaults, succeeds with learned parameters. *Cheap:* one strengthened arm.
2. What differs besides the mechanism — data, sensors, maps, ground truth, compute, tuning? `wm_vct` p5 discloses a baseline's "larger (70,143vs. 42,000 data points)" dataset. *Cheap:* a sentence per asymmetry.
3. "Consistently outperforms" quantifies over metrics too — which moved the wrong way? `applv` p6: TEB collision 00.78 → 08.90 as success rises. *Cheap:* the losing cell, in the winning sentence.
4. Are baseline numbers re-run, or quoted from other platforms? `hacl` p4's "Robots Tested (Sim)" row varies by column. *Cheap:* mark quoted rows non-comparable in the caption.
5. In how many conditions is there no difference? `applr` p5 prints both directions, 106 (42.4%) vs 12 (4.8%). *Cheap:* wins both ways.

## Generalization or transfer

1. Which axis was held out — location, terrain, robot, person, session? `cahsor` p8's caption says "UNSEEN TERRAIN"; p6 tests "locations with similar terrain". *Cheap:* the held-out variable, in the caption.
2. How many times was the gap crossed? `zlik` p1 "generalizes across the sim-to-real and full-to-1/10th scale gaps"; p6 deploys on one platform. *Cheap:* label it an existence claim.
3. Is the split by scene, session, or site — or only by frame? *Cheap:* name the split unit.
4. Was a test-set quantity used to pick a checkpoint, threshold, or prior? *Cheap:* the selection protocol, and final-policy not best-checkpoint numbers.
5. Is the unseen condition matched in difficulty? `performer_mpc` p7 runs ten trials in the demonstration corner, ten in another. *Cheap:* the paired cells.

## Safety

1. A proof with stated assumptions, or a measured rate with its n? `barn24_report` p6 says an approach "ensures collision-free naviga[tion]"; that entry finished 5/9 trials (p3). *Cheap:* the measurement, not the verb.
2. What is the collision rate where success improves? `applv` p6: 1.98–8.90% across four planners. *Cheap:* a safety column beside the success column.
3. Does the summary name only metrics that exist as columns? `adp` p7's conclusion claims "success, safety, and efficiency"; Table IV has no safety column. *Cheap:* delete the rest.
4. Does "success" mean the same in every tier? `t_cbf` p6 makes real-world success "the ability to keep robot safe", not goal-reaching. *Cheap:* one definition per tier, in the caption.
5. What does a success tolerate? `verti_bench` p5: "A successful trial may include contacts with obstacles." *Cheap:* state the tolerance.

## Real-time or on-board feasibility

1. What rate, on what hardware, against what deadline? `humain` p1 distills a student "To enable real-time" deployment; its only rate, 4 Hz on p5, is the data-processing frequency, not an inference rate. *Cheap:* three numbers.
2. End-to-end, or one module's solve time? *Cheap:* a latency budget summing to the loop period.
3. Is the baseline's slowness the method's or the implementation's? `wm_vct` p6 reports a comparator at "more than 10 seconds" per planning cycle. *Cheap:* both machines.
4. At what added latency does the loop fail? `erc2024` p6 documents deployed latencies to "2,000 ms". *Cheap:* one perturbation sweep.
5. For training or throughput claims, is the simulator real-time? `verti_bench` p9: "real time factor ranging between 0.4 and 1.5". *Cheap:* the factor.

## Sample efficiency or data quality

1. Efficient relative to which arm's data, in what unit? `dyna_lflh` p5 trains on "10-minute self-supervised exploration". *Cheap:* a data-budget row.
2. Is efficiency shown at more than one budget? `vertiformer` p7 reports x/10 physical cells for one training budget only. *Cheap:* a scaling curve, or say "at this budget".
3. Where do labels come from, and are they biased where the method is tested? *Cheap:* the source, and its failure regime.
4. How much human effort sits outside the data budget? `pietra` p6 hand-sets a vegetation prior against "the 0.15 m wheel diameter". *Cheap:* list them.
5. How much extra data repairs a known failure? `vrl-pap` p6 answers it: three demonstrations, "just 27 seconds of driving". *Cheap:* count and duration.

## Sim-to-real

1. Does the perception contract change between tiers? `coral` p3 uses "ground-truth segmentation masks" in simulation, YOLO26-seg on hardware. *Cheap:* both contracts, at the comparison.
2. Closed-loop, or offline prediction on recorded data? `va` p7's "Physical Experiment for Sim-to-Real Adaptation" reports MSE over 42.2 s of recorded driving. *Cheap:* rename it, or add closed-loop rows.
3. When physical beats simulation, what made it easier? `dyna_lflh` p6: obstacles move at "constant velocity of 0.5 m/s… comparatively easier". *Cheap:* the difference.
4. Does more simulation substitute for what physical trials were for? `verti_bench` p8 contrasts 30 physical trials with "our 10000". *Cheap:* what each tier establishes — simulation shrinks sampling variance, not bias.
5. Is a sim/real disagreement reported as a finding? `navbenchmark` p6: an architecture "only marginally" better in simulation won clearly in the real world. *Cheap:* publish it.

## Human experience, comfort, or social compliance

1. The construct, or a proxy — does the proxy label reach the abstract? `humain` p6 calls trajectory divergence "a proxy for socially compliant behavior". *Cheap:* the proxy word in every summary.
2. What is the independent unit — participant, run, frame? `hybrid_social_nav` p6 runs a one-way ANOVA per question; p5 gives "fifteen interactions per individual". *Cheap:* the participant-level analysis.
3. Who were the participants, and was anyone blind? `performer_mpc` p20 calls its study "exploratory", not "counterbalanced"; p22 names "research team members as study participants". *Cheap:* population, recruitment, blinding.
4. Is a reported null carried into the abstract? `multimodal_social_nav` p6 does "not observe a significant advantage of multimodal learning" over point-cloud-only; the conclusion there claims one. *Cheap:* read the conclusion against the nulls.
5. Is the effect a property of the cue or of its salience? `hallway_icsr` p10: one LED vs one gaze cue, conflict 11 (100%) vs 8 (50%). *Cheap:* narrow the noun to what you manipulated.

## Dataset coverage and representativeness

1. How many contributors, and how many trajectories each? `musohu` p1 reports "300 trials, 13 humans"; p3 says "seven human demonstrators". *Cheap:* reconcile; give per-person counts.
2. Who annotated, how many, with what agreement? `musohu` p4 publishes 17 tag types with counts, no reliability statistic. *Cheap:* annotator count and agreement.
3. Which classes are too thin to train or evaluate on? *Cheap:* the per-class distribution, tail included.
4. What consent, IRB, or de-identification governs public recording? `musohu` p3 collects "360° RGB video" in public spaces. *Cheap:* one sentence in the text.
5. Is a coverage axis real, or a surrogate? `m2p2` p6 subsamples events to 100/80/50/25%, "mimicking increasingly darker" conditions. *Cheap:* what it misses.

## Benchmark validity

1. Who defines difficulty, and does the ordering survive another planner class? `navdiffdataset_ssrr` p5 fits difficulty to outcome at slope 0.96, one value per environment. *Cheap:* re-rank outside that family.
2. Is the normalizer measured once? `barn26_report` p3 uses "a human teleoperated trial" per course to normalize traversal time. *Cheap:* repeat it, or label it an estimate.
3. Can a reader recover the denominator? `t_cbf` p5 prints 40.12% over "30 Verti-Bench" environments beside rows written 10/10. *Cheap:* one convention per table; fractions in cells.
4. What validates the instrument against what it stands for? `verti_bench` p9 cites "the current small-scale physical testbed". *Cheap:* promise standardized and reproducible; reserve "objective" for a validated construct.
5. Are the evaluated systems inside or outside their training distribution? `verti_bench` p6 gives all systems "ground truth vehicle states"; none is "trained in Verti-Bench". *Cheap:* the contract, plus an in-distribution arm.

## Theoretical guarantee

1. Which assumption fails in the deployed system, and what does the theorem then bound? `cbm` p3 notes its factorization assumption fails "for instance, [for] quaternion variables". *Cheap:* the violated assumption, and the weakened conclusion.
2. Is the independence or additivity structure a domain property, or what makes the algorithm tractable? `risk_ral` p3 drops additivity, keeps lateral independence. *Cheap:* name the convenience, bound its error.
3. Which terms change the chosen action, and which only shift a constant? *Cheap:* the action-relevant terms.
4. Where does the guarantee stop being computable, and how loose is the bound there? *Cheap:* the scale boundary, and one measurement at it.
5. Do the experiments test the analyzed object or a different one? *Cheap:* the gap between analyzed model and deployed system.

## Hardware capability

1. Which claimed capabilities were measured, and which merely observed? *Cheap:* a requirement → design → measurement table.
2. Does the paper's headline metric appear in any table? `compa` p1 promises to "quantify its holonomicity using the mobility ellipsoid". *Cheap:* the metric, per configuration.
3. Is a loss or power decomposition measured or assumed? `battery_iros` p6 isolates internal friction by deducting ancillary power from a wheels-up test. *Cheap:* a subtraction experiment per term.
4. What is the reference instrument's own error? `nasa` p65 notes the comparison DEM's resolution is "nominally 100m/pixel… actually closer to 300m/pixel". *Cheap:* its uncertainty, beside yours.
5. How many independent builds, traverses, or discharge cycles? *Cheap:* count and spread; one traverse per configuration gives none.

## Competition or challenge finding

1. Is the finding about systems, or about who entered? `barn25_report` p8 reports the first all-classical winning field; its one learning entrant's team member "was unable to participate due to illness". *Cheap:* entry counts by class.
2. Was the measured quantity the one the heading names? `barn26_report` p7's heading "ROS Teams Significantly Outperform ROS2 Teams" sits above an evaluability count. *Cheap:* retitle to what was measured.
3. What confounded the run environment? `barn26_report` p7 gives a subsection to wireless interference by competition slot. *Cheap:* publish the log; call the ranking unadjusted.
4. Did the trials reach the capability tested? `barn25_report` p8: in most trials the robot "did not reach the dynamic obstacle field". *Cheap:* the conditional sample size.
5. What does a no-tuning trial measure that a tuned one cannot? `barn26_report` p3 defines a cold trial "without any fine-tuning"; p7 reports one success in 12. *Cheap:* separate columns.

## Ablation-based mechanism attribution

1. How many things change between the arms, and which is the conclusion about? `applv` p7 reads one gap as "vision-language representations significantly outperform laser-scan-based ap[proaches]", though backbone and pretraining also differ. *Cheap:* name the confounds.
2. Is the primary baseline your own algorithm with the mechanism zeroed? `anticipatory_tamp` p4: MYOPIC uses "a zero-function for the anticipatory cost estimator". *Cheap:* implement the degenerate case.
3. Is the ablation drop larger than the model's own spread? `gacl` p5 says "removing any one significantly degrades performance"; drops near 2 points sit against ±2.51. *Cheap:* the drop in spread units.
4. Does the defended configuration win in the paper's own table? `hacl` p5 calls recurrent models "the ideal choice" without naming which; Table III (p6) splits them — GRU 6.72 m/s and 90% against the RNN column's 6.62 and 80%. *Cheap:* name the defended row; if it is not the winner, say why.
5. Is the "ablation" a measurement or a gallery? `tgs` p6 Fig. 4 captions "Ablation Study on the Trajectory Generator" over one scene. *Cheap:* counts, or an honest caption.

## Foundation-model or VLM-based reasoning

1. Is the comparison about the model, the fine-tuning, or the prompt? `applv` p7 reads a VLM-vs-small-policy gap as a modality result. *Cheap:* one arm varying only the prompt, one only the backbone.
2. How were refusals and malformed outputs scored? `maction_socialnav` p6 reports a baseline producing no executable action "in 31 of 79 cases". *Cheap:* the rule, and the headline without them.
3. Are decoding parameters, temperature, and seed budget matched? `humembr` p5 uses three seeds for the method; "the baseline is evaluated using a single seed". *Cheap:* match them, or state the direction.
4. Is the judge independent of the labels the model was trained to produce? `social_llava` p6 reports "fifteen human judges", no agreement statistic. *Cheap:* agreement, plus a judge outside that vocabulary.
5. Is the win precision or coverage, at what cost per decision? `mrvs` p13 reports night precision 0.440 against a baseline's 0.623, at recall 0.792. *Cheap:* the confusion picture; latency per call.
