# From an idea to a decisive experiment

An evaluation-design playbook from a study of 137 coauthored publications (2012–2026). Corpus counts are this study's own measurement over the extracted text of the 136 machine-readable papers; the shipped ledger does not carry the per-paper codings, so to lean on one, obtain the sources through each record's `source_url` and re-run the stated method. Every claim about a paper carries `key pN` (physical PDF page). Source papers are teaching examples, never evidence for the user's method.

## 1. Research brief

Build only as much as the user needs.

1. **Deployment context:** robot, environment, user need, failure cost, resources.
2. **Observed bottleneck:** the concrete failure and the assumption that might explain it, marked tested or conjectured.
3. **Nearest alternatives:** what works already, what changes here, why that matters. Verify novelty separately.
4. **Mechanism:** new representation, objective, adaptation signal, interface, data source, or proof; name retained components.
5. **Falsifiable claim:** "Under C, changing X should improve Y over B because M." State what would weaken it.
6. **Evidence design:** smallest discriminating comparison, strong baseline, controls, ablations, alternative explanations.
7. **Scope and cost:** training versus deployment information, tuning, compute, data, engineering and human effort.

## 2. Experiment card

| Field | Decision |
| --- | --- |
| Scientific question | What uncertainty does this resolve? |
| Changed variable | What changes, what is held fixed |
| Comparator | Matched contract, or asymmetries disclosed with numbers |
| Setting and split | Held-out scenes, people, trajectories, robots, terrain, time; correlated-sample risks |
| Unit of analysis | Coarsest thing re-randomized; must match the noun in the claim |
| Eligibility and outcomes | In-scope cases defined separately from success, failure, timeout, exclusion; metric, units, denominator |
| Replication | Repeats, seeds, participants; dispersion at the claim's unit |
| Resources | Tuning, data size and provenance, sensors, maps, ground truth, speed caps, compute, runtime, interventions |
| Evidence tier | Named in the sentence where each number appears |
| Interpretation | Support, contradiction, or inconclusiveness; the leading alternative explanation |
| Safety | Offline and simulation screening; qualified oversight for physical runs |

## 3. Discriminating-comparison catalogue

| Design | Isolates | Cannot isolate | Cheapest version | Corpus instance |
| --- | --- | --- | --- | --- |
| Same planner, different parameters | Algorithmic versus parametric gap | The algorithm class | Retune the baseline on your hardest condition | `appld_ral` p5: default DWA fails 8/10 in the narrow corridor; with learned parameters, 10/10 |
| Matched-backbone information ablation | Marginal value of one input | Whether another architecture extracts it better | Zero one input channel, nothing else | `cahsor` p7: methods "use the same model architecture"; `dynabarn` p5: one network, two signals |
| Baseline as degenerate case, or shared layer fixed | The mechanism you added | Standing versus the field; the shared layer | Zero your new term, or compare against the model your method already calls | `anticipatory_tamp` p4: the same algorithm with a zero-function estimator; `dyna_lflh` p6: recovery on for all arms |
| Physics / hybrid / full-learning arms | Where value sits on the modeling spectrum | Which inductive bias caused it | Three arms, one dataset | `mocap_icra` p4: kinematics / learned displacement plus kinematics / end-to-end |
| Training-recipe ablation: data source or schedule | Whether the recipe, not the learner, carries the result | Data quality within a source | One learner, two recipes | `dyna_lflh` p5: 8.7 hours of expert data versus under 10 minutes of self-supervised data; `verti_bench` p6: the automatic curriculum loses to the manual one |
| Held-out axis: environment, terrain, robot, person | Transfer along one named axis | Transfer along any other | Ten trials somewhere you never trained; or today's model on the other robot | `performer_mpc` p7: ten runs in the demonstration corner, ten in another; `vw` p6: the V4W-trained policy beats the V6W's own on the V6W, 10/10/9 versus 9/9/6 |
| Cold or untuned trial | Deployability without expert fiddling | Ceiling performance | One trial before anyone touches a parameter | `barn26_report` p3, p7: 12 cold trials, one success |
| Human reference on the same interface | Course feasibility, a normalizer, a reference level | Optimality | One teleoperated run per environment | `vw` p6, course "conquered by human teleoperation"; `barn26_report` p3, teleoperated time as normalizer |
| Sweep a budget or a nuisance parameter | A trend; whether a win is an artifact of one operating point | Untested settings | Spread the same trials over many settings | `anticipatory_tamp` p6: 1, 2, 5, 10, 100 samples; `offroad` p5–p6: ten speeds, failure rate rising with speed |
| Negative control | That your method does not harm what it constrains | Benefit | One arm where your mechanism should do nothing | `cahsor` p7: slow planner plus the method, "to demonstrate it doesn't unnecessarily reduce speed" |
| Strengthened baseline | Whether your advantage survives giving the baseline more | Whether a different baseline wins | Quadruple one baseline budget, rerun | `lflh` p4, quadrupled sampling rate; `carol` p7, an enlarged baseline reaches "comparable performance" |
| Instrument-reliability study first | Whether the measure is stable across places and raters | Anything about methods | Repeat one scenario in two places first | `social_nav_protocol` p4: two locations, three participants over 30 runs, then 20 per policy |
| Withheld-feature transfer test | Whether a testbed's conditions are genuinely distinct | Whether they are representative | One model per condition, label withheld | `verti_arena` p4 deliberately omits "the environmental features" from the model input |
| Decomposition by subtraction | One term of a physical budget | Interactions between terms | Run with one load removed, subtract | `battery_iros` p6: a wheels-up test minus ancillary power isolates internal friction loss |

## 4. Choosing the unit of analysis

**The unit is the coarsest thing you re-randomized, and it must be the noun in your claim.** One obstacle course run twenty times is n = 1 course.

Across the 64 corpus papers that state what a mean is over, the units named most are trial (24), environment (19), run (16), model (16), task (15), trajectory (15), episode (7); seed and participant appear once each.

- *Correct coarsening:* in the Cabinet domain, `anticipatory_tamp` p6 evaluates 64 deployments of ten tasks each and reports average cost-per-task; tasks in a persistent environment are not independent, so the deployment, not the task, is the re-randomized unit *(this study's reading)*.
- *Claim coarser than design:* `navdiffdataset_ssrr` p5 offers 50 physical trials for a claim about unseen environments, but the fitted line (slope 0.96) has one difficulty value per environment, so its effective n is 5. `dyna_lflh` p5–p6 runs 3 planners × 20 trials in one 8.2 m × 4.3 m arena.
- *Unit finer than the claim, unstated:* `vs` p6 reports simulation roll as 6.46 ± 26.21 degrees over 50 trials. A mean absolute roll of 6.46° cannot carry a trial-to-trial standard deviation of 26.21°, so the interval is almost certainly pooled over timesteps within trajectories; the paper does not say *(this study's inference)*. State in the caption what the ± is over.

## 5. How much evidence is enough

No universal trial count. Size from **claim strength × expected effect size × cost per trial × failure risk**: write the sentence you want to publish, then build the smallest design that could falsify it. In this corpus 72 of the 136 machine-readable papers state a trial count; per-condition budgets cluster at 3, 5, 10, 20, mode 10.

| Budget | Supports | Does not support |
| --- | --- | --- |
| 3–5 per cell | Existence, feasibility, a baseline that never succeeds | Any ranking. `verti_bench` p8 reports three systems, five trials each, "totaling 30 trials", and says why; 3 × 5 = 15, and its Table II runs five trials per system on each of a low- and a high-elevation testbed *(this study's inference)* |
| 10 per cell | A directional claim when the gap nearly saturates: 8/10 failures versus 10/10 successes (`appld_ral` p5) | A moderate gap |
| 20 per cell | The smallest budget at which a large success-rate gap is worth stating | 10/20 versus 8/20 (`dyna_lflh` p6, 0.50 versus 0.40), which the abstract renders as "up to a 25% improvement" (p1) |
| 3 seeds | Separating initialization noise from a method effect, if spread is reported | A comparison against a single-seed baseline, unless disclosed (`humembr` p5) |
| ≥50 trials over ≥3 environments | A comparative claim about the setting, not the course (`t_cbf` p6, 90 runs; `vw` p5, 240) | Environment classes you never sampled |
| Hundreds of environments, tested per environment | A population claim: `applx` p8 runs 300 environments × 12 runs per method, 25,200 trials in all, counting where one method is significantly worse at p < 0.05 | Anything about the physical world |

One corpus correction: 45 papers claim to outperform a named baseline and 40 report no test, while a guidelines paper in the same corpus says "significance" should not be used without one (`social_nav_guidelines` p26).

## 6. Baseline contracts

Disclose the resource contract with numbers, in the sentence that reports the result.

- *Against your own interest:* `wm_vct` p5 states the baseline trained on 70,143 expert points against the authors' 42,000 random-exploration points.
- *Matched except one, with a reason:* `e2e_params` p4 matches hyperparameters except the discount factor, because the time step differs; p3 declares an unavoidable asymmetry and promises the check.
- *A cap disclosed, then used to bound the claim:* `sober` p6 notes the baseline's 1.0 m/s cap against 0.6 m/s and attributes its easy-environment advantage to speed.
- *Whole-benchmark contract:* `verti_bench` p6 replaces visual odometry with ground-truth state, skips real elevation mapping, and states no learning system was "trained in Verti-Bench".
- *Deliberately unequal, handled honestly:* `carol` p7 names the baselines it did not run physically and why, then re-scopes what that tier proves.

Buy a matched-resource control when resource asymmetry is the leading alternative explanation for your win; the strongest form grows the baseline until your advantage disappears (`carol` p7). Skipping it is the corpus's commonest way for a claim to outrun its comparison: 17 papers compare against a classical planner on manufacturer defaults, 3 run a strengthened variant. `hallucination` p6 states the caveat without running the check; `vagn` p6 attributes its baseline's failure to "the default parameters not allowing progress", so that comparison measures parameterization rather than algorithm quality. Only 4 of 136 papers assert matched compute.

## 7. Evidence-level ladder

| Tier | Supports | Does not support |
| --- | --- | --- |
| Offline prediction on held-out recordings | Accuracy under the recorded distribution | Closed-loop behavior; the policy moves the distribution |
| Simulation, closed loop | Rankings inside the simulator; tight sampling error | Model bias; extra simulated trials buy sampling precision, not fidelity *(this study's point)* — `verti_bench` p8 sets its 10,000 simulated trials against 30 physical ones |
| Hardware in the loop | Timing, interfaces, failure handling under real compute | Terrain and contact physics. The phrase appears in 0 of 136 corpus papers; define it if you use it |
| Physical closed loop, one venue | Feasibility, deployability, existence of a failure mode | A ranking. `rtw` p5 titles this tier "Physical Demonstration" |
| Physical, multiple venues or a held-out axis | A comparative claim about the setting | Populations you never sampled |
| Field deployment or competition | Deployability under time pressure and uncontrolled confounds | Algorithmic rankings; the confounds are the point (`barn26_report` p7) |
| Human evaluation | Perceived quality, given a validated instrument, blinding, counterbalancing | Anything the instrument was not shown to measure |

Three blurring cases from the corpus. (a) *A metric keeps its name while its definition changes:* `t_cbf` scores success as reaching the goal in simulation (p5) and as staying safe and mobile in the real world (p6). (b) *A conclusion pools tiers:* `rtw` p6 lists MPPI among methods outperformed "through extensive simulation and physical experiments", though its physical tier (p5) is 3 methods × 5 trials. (c) *A headline outruns its qualification by pages:* `performer_mpc` p1 advertises ">65% better on social metrics"; p20 calls it an "exploratory pilot study", not fully controlled or counterbalanced, and p22 names research team members as the participants.

## 8. Failure accounting

Predefine exclusions independently of observed success. If reporting a restricted operating envelope, disclose the full attempted denominator and why cases fell outside it. Record resets and interventions: successful segments separated by resets do not establish uninterrupted mission completion. Disclose any reference-assisted alignment, calibration, or cropping used for evaluation; geometric agreement after alignment is not unassisted localization accuracy.

- **Quantify success and every failure mode before running.** `verti_bench` p5 defines rollover as roll above 30° at the end of a failed trial, stuck as under 1 m of motion in the last 10 s, success as reaching within 10 m of the goal in under 60 s, contacts tolerated.
- **Publish an exhaustive, mutually exclusive outcome partition**, leaving no bucket for timeouts. `verti_bench` p6 gives rollover / stuck / success per system over 1000 tasks: rollover rates are near-constant while stuck rates run 24.6% to 75.7% — a contrast no aggregate success rate shows.
- **Declare the censoring rule and the survivorship.** `appld_ral` p5 marks failures with an asterisk and a 60 s penalty; `navdiffdataset_ssrr` p4 uses 30 s; `verti_bench` p8 and `wm_vct` p6 state inline that traversal time averages successes only. Print the denominator in the cell: `e2e_params` p5's `12.42s (3/3)`, `NA (0/3)`.
- **Count failures individually, with causes.** `pietra` p7 gives one roll-constraint violation with its cause and separate out-of-bound counts per method. Only 6 of 136 corpus papers state an explicit timeout rule and 6 a failure penalty — a cheap place to beat the norm.

## 9. The benchmark or dataset as the contribution

- **Name the axis nobody varies, and coin a term for it.** `dynabarn` p1 names motion profiles and enumerates their dimensions, turning the absence of any benchmark that varies this into a testable deficiency; its contribution list is an inventory — dataset, generator, pipeline, baselines — claiming no win. Stronger: show the existing evaluation object is the wrong *type*, as `verti_bench` p1 does in arguing interactions must be unfolded during evaluation, so a static dataset cannot evaluate mobility.
- **Discriminating means the difficulty label orders failure rates.** `dynabarn` p3–p4 derives easy/medium/hard from obstacle motion parameters chosen for the Jackal, not from measured planner failure rates — a designed label; the p5 baseline results report success per difficulty level only after the fact, so the label was never validated before use. `verti_arena` p4 validates instead: one forward model per zone, "the environmental features" withheld from the input, cross-zone error as evidence the zones differ. Hard to game means publishing the generative parameters — friction per semantic class, obstacle counts and separations, elevation scaling (`verti_bench` p3–p4). An unpublished generator is a leaderboard.
- **Splits and leakage.** `navbenchmark` p4 holds out 50 environments per type and nests training sets at 5/10/50/100/250, so the generalization curve varies one quantity. The failure case, disclosed in methods but not restated at the ranking: in `dynabarn` p5 the reinforcement-learning entry has seen "the largest amount of data points (20M)" and trains in the evaluation worlds.
- **A benchmark must be able to embarrass its owners.** `verti_bench` p6 prints an automatic curriculum losing to a manual one, p8 a simple PID planner beating a sophisticated one; `navbenchmark` p6 finds an architecture only marginally better in simulation but clearly better in reality, and promotes the disagreement into a finding.
- **Scale claims need units, denominators, and an independence statement.** `mtc` p6 reports 145 scenes and 348 trajectories, roughly 2.3 hours; scenes are reused, so a scene-level claim rests on the coarser count. Delegate the wide comparison rather than pad it (`musohu` p2 triangulates two predecessors).
- **A competition is a research instrument** measuring deployability under time pressure and confounds you do not control; it cannot rank algorithms. `barn26_report` p3 adds a cold trial and a human-teleoperated normalizer; p7 reports one success in 12 cold trials and prints a neighboring competition's wireless interference as the alternative explanation for its own results. Its "ROS Teams Significantly Outperform ROS2 Teams" heading (p7) actually measures *evaluability*: one of five ROS2 submissions ran through the standard pipeline. Match headings to the measured quantity.
- **Benchmarks compound only when the substrate stops moving:** fix robot, simulator, middleware, and generator, and each follow-up changes one thing and stays comparable.

## 10. Turning a limitation into the next project

A limitation is generative when it names the mechanism that must change and the study that would remove it; it is an apology when it says performance depends on a component. Write it to block a misreading: `verti_arena` p5 says low error on its smallest zone does not imply the terrain "is inherently easy" in nature, names the cause (a small zone narrows the state and command distribution), and fences the envelope to fixed low gear with locked differentials.

| Limitation, where stated | What it became |
| --- | --- |
| `servoing_ssrr` (2017) p6: the risk of navigating through obstacles "needs to be quantified"; the optimal viewpoint per task "remains to be determined" | `planning_iros` (2018), tether motion planning; `viewpoints` (2021), best assisting viewpoints |
| `appld_ral` (2020) learns planner parameters from one demonstration; `applr` (2021) p1 names the ceiling: demonstration caps performance at "a potentially-suboptimal demonstrator" | `applr` (2021), which changes the supervision source |
| `vw` (2024) p6 names two directions: "explicitly model terrain traversability", and to "design or learn a vehicle dynamics model" for this terrain | `wm_vct` (2024); `tnt` (2026) |
| `musohu` (2023) p6 releases a demonstration dataset whose stated uses are follow-ups | `vanp` (2024) p4, trained on SCAND and MuSoHu |

Model form: *"{OBSERVED DEFECT} occurs because {MECHANISM}; removing it requires {NAMED STUDY OR INSTRUMENT}."* `mrvs` p19 proposes "controlled, feature-by-feature comparisons" for exactly the inference its integrated design blocks.

## 11. Deliverable

Prioritize by claim importance and uncertainty reduced, subject to cost and risk; a test that could disprove the mechanism beats another favorable scene. Offer narrower wording when broader evidence is unavailable. Deliver a research brief, prioritized experiment cards, and a provisional contribution statement — never a proposed result written as a past-tense finding. Shape that statement with the contribution-list spec in `drafting.md` §3.
