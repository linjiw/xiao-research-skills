# Evidence-focused review protocol

A rubric derived from a study of 137 coauthored papers — not a venue rubric, not any individual's judgment. Examples are craft observations about *sentences and tables*, never accusations about people; in several papers the overclaim and its repair sit pages apart. Pages are physical PDF pages. Never assert a page limit or submission rule; cite the call for papers. Corpus percentages below are this study's own measurement over the extracted text of the 136 machine-readable papers (the 137th has no text layer); the shipped ledger does not record the per-paper values, so to recount one, obtain the sources through each ledger record's `source_url` and re-run the stated method before relying on it.

## Read order

Three passes. Do not evaluate in pass 1; do not recompute in pass 2.

| Pass | Read | Record |
| --- | --- | --- |
| **1. Inventory** | Title, abstract, Fig. 1 and caption, every table caption, headings, conclusion, limitations | Located claim list; genre; every metric named in abstract or conclusion; every tier named; what the material lacks |
| **2. Evidence map** | Method, experiment setup, results, ablations | One claim-table row per central claim; what a reimplementer could not build; unclear settings, as questions |
| **3. Arithmetic** | Tables, and the sentences summarizing them | Every headline number recomputed: unit, denominator, reference set, conditioning |

Pass 1 buys the cheapest audit available: **a summary may only name metrics that appear in a table.** `adp` p7 concludes that the evaluation "enhances navigation success, safety, and efficiency" while Table IV on that page has only Success, Avg. Progress and Avg. Time. It also catches headings asserting what the prose beneath declines to assert (`barn26_report` p7 vs its hedged body, p8).

Record **"not assessable from the supplied material"** as a finding in its own right. It is not "the authors did not do it," and it is required wherever you would otherwise guess.

## The claim-evidence table

| Claim (located) | Unit of analysis | Denominator | Comparator contract | Evidence level | Warrant | Smallest repair |
| --- | --- | --- | --- | --- | --- | --- |
| Faithful paraphrase + section/figure | Coarsest thing re-randomized | n, and what n counts | What differs between arms besides the mechanism | Tier that produced the number | supported / partial / unclear / contradicted / not assessable | reporting, re-analysis, narrower wording, one control, experiment |

**Unit of analysis** is the coarsest thing re-randomized. `navdiffdataset_ssrr` p5 offers 50 physical trials for a claim about difficulty across unseen environments, but the fitted relation has one difficulty value per environment — five. `anticipatory_tamp` p6 aggregates 64 deployments, each "a sequence of 10 tasks," per deployment. One course run 20 times is n = 1 course.

**Denominator.** Ask where it is printed. `cahsor` Table II (p8) reports six methods on unseen terrain with no n in table or caption; the only n is two pages earlier — "Autonomous navigation (three loops each method)" (p6). `t_cbf` Table I (p5) prints simulation success of 60.7 / 58.2 / 40.12% over 30 environments with no trials-per-environment stated, while its real-world rows use `x/10`.

**Comparator contract** is every asymmetry between arms — data, sensors, maps, ground truth, seeds, decoding parameters, compute, tuning budget, speed cap. `wm_vct` p5 discloses *against its own interest* a baseline dataset larger and cleaner than its own (70,143 vs 42,000 points, expert vs random exploration); `humembr` p5 reports three seeds for the method while "the baseline is evaluated using a single seed."

**Evidence level.** Six tiers, never pooled in one sentence: analysis or proof; offline prediction on held-out data (`va` p7 reports MSE on 42.2 s of recorded driving under a "Physical Experiment" heading); closed-loop simulation; physical closed loop; human study; fielded deployment. `verti_bench` p8 contrasts its 30 physical trials with 10000 simulated. A metric can change definition across tiers while keeping its name: `t_cbf` p5 makes simulation success "the percentage of time the robot successfully reaches" the goal, p6 makes real-world success "the ability to keep robot safe." Sharing a column heading is what makes that a problem.

## Checks by section

| Section | The question that exposes the failure |
| --- | --- |
| Abstract / title | Does every metric and superlative have a column somewhere? Is an evidence verb attached to a tier that did not produce the number? `hacl` p1 writes "In practice" with 6.7 m/s; p6 says "Currently, We are testing" on hardware, at 3.2–4.4 m/s. |
| Intro / contributions | Is the priority claim hedged, and is the claimed class as narrow as the thing built? Does a contribution inherit a null result? `multimodal_social_nav` p6 results: "we do not observe a significant advantage" over point cloud only; conclusion, same page: "clear advantage over either unimodal counterpart". |
| Method | **What could a reimplementer still not build?** Name the missing item — a loss weight, an input normalization, the train/inference split, a stopping rule — and ask which configuration produced the headline number when one name covers several variants. |
| Experiment design and results | What would have to be true for this gap to have a cause other than the mechanism? Is there a condition where the method should lose, and was it run? Which metric moved the wrong way, and is it printed? |
| Figures / captions | Does the caption carry n, the meaning of `±`, and the bolding rule? Roughly 1.4% of harvested figure captions state a sample size, so a missing convention is a question, not an indictment. Is a qualitative panel captioned as a ranking? |
| Limitations | Does it name an assumption and an observation that would settle the matter, or only apologize for a quantity? `verti_bench` p9 "assumes ground truth perception is available," notes "such an assumption does not hold," then names the future work that would settle it — adding realistic perception noise. Does a heading promise more than the text delivers? |
| Reproducibility | Could someone rerun *this comparison* — success definition, failure taxonomy, timeout, failure penalty, recovery-behavior state per tier, seeds? `appld_ral` p5 prices failures instead of dropping them: "penalty time value of 60 s." |

## The arithmetic pass

| Failure | Detection | Worked instance |
| --- | --- | --- |
| Points read as relative change | Recompute both | *Synthetic:* 60% → 75% is 15 **points**, 25% relative. *Real:* `rtw` p5 Table II, 80.32 → 82.67% = 2.35 points = 2.93% relative. |
| Small-integer ratios, missing denominator | Convert every rate back to counts | `dyna_lflh` p1 advertises up to 25% improvement in success; Table II (p6) is 0.50 vs 0.40 at 20 trials each (p5) — two extra successes. |
| Unstated reference set; headline not reconstructible | Recompute every abstract percentage against the strongest baseline and the baseline mean | `humain` p1 reports an average 29.8% gain. From Table I (p6), the mean of the 12 baseline × metric relative improvements is 29.84%; against the strongest baseline per metric it is 23.2 / 15.2 / 21.7, mean 20.0%. The body's 14.2% for FDE matches neither (1 − 1.064/1.254 = 15.2% vs GNM). Ask which reference set; do not assume an error. |
| Rows averaged over different subsets | Check that every row's "All" uses the same k | `narrate2nav` Table II (p7): GNM shows FAIL in one of four scenarios, so its All is (0+9+9)/3 = 6.0 while other rows average four. The conclusion's 41.67% is 8.5/6.0 — against the row whose worst scenario was dropped. In Narrow Passageway the method is 4/10 to ViNT's 10/10. |
| Metric conditional on success | Ask what the mean is over | `verti_bench` p5 defines traversal time as "how long it takes to finish a successful" traversal, then Fig. 6 (p7) plots it for ten systems including one at 10.0% success (Table I, p6). In `t_cbf` p5, Real World – High, the fastest time (14.16 ± 1.10) is a 6/10 method's; the 10/10 method took 17.92. |
| Bolded within-noise difference | gap ÷ pooled sd, from the table's own dispersion | `vs` p6: roll 6.46 ± 26.21 vs 6.55 ± 17.56 — gap 0.09, pooled sd √((26.21² + 17.56²)/2) = 22.3, i.e. 0.004 sd. `gacl` p5 calls a −1.99 point ablation drop one that "significantly degrades performance," against the full model's own ± 2.51. A `±` exceeding a bounded non-negative mean is likely pooled over timesteps, not trials; ask. |
| Sim and physical numbers pooled | Trace each summary number to its tier and table | `rtw` labels its physical section "B. Physical Demonstration" (p5; three methods × 5 trials, MPPI absent from Table III), then credits results over "the classical MPPI planner" (p6) — only simulation ran it. |
| Significance asserted without a test | Grep for the word, then for a test | The corpus's own guidelines say such terms should not be used "unless the proper statistical tests are conducted" (`social_nav_guidelines` p26). Absent one, ask for the number and n. |

**Also audit, where pertinent:** proxy versus construct (a displacement metric is not comfort); a proof's conclusion against its stated assumptions; eligibility versus desirable outcome in the denominator, and restricted-envelope results against total attempts and exclusions; resets, which turn a route claim into a segment claim; ground-truth-assisted alignment or cropping, which changes what a reconstruction metric establishes; a changed class or risk definition; counts that disagree across sections (`musohu` p1 "13 humans", p3 "seven human demonstrators") — cite both, never guess. Never assert an external repository is unavailable unless that audit was requested.

## Alternative explanations

Each is a hypothesis for the authors to rule out. Phrase it as a question, never as a finding of unfairness.

| Confound | Ask |
| --- | --- |
| Tuning budget | Were the baseline's parameters tuned for this regime, and does the gap survive a strengthened variant? `appld_ral` p5 shows one DWA failing 8/10 in a narrow corridor on defaults and succeeding in every trial after re-parameterization. Either answer suffices: run the check (`lflh` p4, "quadrupling DWA's default sampling rate") or state the caveat (`hallucination` p6: "re-tuned for each environment DWA can achieve better"). |
| Coupled differences and extra information | How many things differ between the arms, and what was each allowed to see? `applv` p7 reads a gap over an RL baseline as "validating that vision-language representations significantly outperform" laser-scan approaches, where the arms also differ in backbone, pretraining corpus and training procedure. Ask for the ablation isolating the named factor, or for the sentence to name its confounds. |
| Sensors, speed, actuation envelope | Are the arms capped alike? `sober` p6 discloses that "DWA has max speed of 1.0m/s" against 0.6 for the learned planners, and bounds its claim accordingly. |
| Compute and runtime | Same hardware for inference? Is a real-time claim backed by a measured rate and the deadline it must meet? Did sessions differ in operator, battery, or network (`barn26_report` p7 reports wireless interference hitting some teams only)? |
| Map or ground-truth access | Did any arm get a prior map, ground-truth state, or oracle perception? `navdiffdataset_ssrr` p5 discloses that its physical planners "do not have access to a pre-built map," unlike simulation; `verti_bench` p6 substitutes ground truth for visual odometry. |
| Environment difficulty | Does the advantage hold as difficulty rises? `applr` Table III (p5) reports its own advantage shrinking, 58% → 37% → 31% of environments from easy to difficult — a credibility move, not a weakness. |
| Order and familiarity | Was condition order randomized or counterbalanced, and could participants have adapted across trials (`social_nav_guidelines` p22)? Is a replayed trajectory read as a reacting human (p52)? |
| Self-selection | How many variants of the method got a draw at the test set, versus one per baseline? `dyna_lflh` p5 evaluates four hallucination lengths and carries the best forward. Which scenarios or baselines were dropped, and why? |

## The smallest sufficient repair

| Problem class | Repair | Why it is enough |
| --- | --- | --- |
| Claim broader than the manipulated variable | Narrower wording | The measurement stands; the noun is wrong. |
| Summary names a metric with no column | Delete the word, or measure it | Cheapest fix available. |
| Missing n, denominator, `±` definition, bolding rule, exclusion, tier label | Clarified reporting | No new data needed. |
| Headline percentage not reconstructible | State the reference set, recompute | The ranking usually survives. |
| Aggregate hides a losing subgroup, or rows use different subsets | Re-analysis of existing data | The table holds the answer. |
| Unit-of-analysis mismatch | Re-analysis at the coarser unit, or a narrower claim | Turns an environment claim into a course claim. |
| Baseline may be mis-parameterized, or arms differ in several respects | **One** added control: a strengthened baseline, or the mechanism zeroed inside the authors' own algorithm (`anticipatory_tamp` p4 runs its baseline as Alg. 1 "using a zero-function for the anticipatory cost estimator," "ensuring fair comparison") | Ablation and baseline become one object. |
| A central mechanism claim no existing data can support | New experiment — only if the claim is central and cannot be narrowed | Otherwise the narrowing is the accept path. |

Every requested experiment names the uncertainty it resolves: *"Running <control> would distinguish <explanation A> from <explanation B>; without it, narrow the claim to <C>."* Never issue a list whose cost exceeds the paper. `carol` p7 is the generous form: when a baseline failed at matched size, the authors "increased the network complexity of the adaptation module" until it matched, and said so.

## Calibrating severity

| Level | Criterion | What you must supply |
| --- | --- | --- |
| Validity-critical | Contradicts a central claim: leakage, wrong calculation, invalid proof step, a comparison that cannot support the attribution, missing decisive evidence | The conclusion that changes, and the repair |
| Major clarification | Evidence may suffice, but an essential setting or interpretation is unclear | A precise question, before declaring invalidity |
| Useful extension | Broadens scope beyond the bounded contribution | A note that it is not required |
| Presentation | Organization, notation, wording, captions | Brevity; do not let polish dominate |

Miscalibrations run both ways:

- Do not demand deep learning, a physical robot from a theory paper, an algorithm from a dataset paper, or a human study from a hardware report. Match obligation to genre.
- Do not treat a small sample as automatic rejection. As this rubric's rule of thumb, not a corpus finding and not an acceptance threshold: n = 3–5 supports existence claims; n = 10 a directional claim only when the gap is large; n ≥ 50 across several environments a claim about the setting. Say which claim the n supports, then ask the claim to match it.
- Do not treat an acronym, a robot photograph, dataset size, or a leaderboard placement as merit by itself.
- Do not reject for a limitation the paper already scopes correctly; do not credit a hedge one column from an unhedged number (`narrate2nav` p7 concedes limited robustness beside the aggregate that ignores it).
- Do not let a paper's imprecise sentence become your standard; where its prose outruns its tables, the repair is the lesson.
- No universal score or threshold. Rate only against a venue rubric the user supplies, provisionally.

## Writing the review

Order: scope; strongest supported contribution; validity-critical concerns; major clarifications; useful extensions; presentation. Cap the list near five concerns so the ranking carries information.

Each concern takes one shape: **location → observation → consequence → smallest repair.** Keep observation separable from inference: cite what is printed, say what you infer, then say what you cannot tell. "Table 3 reports X; the text summarizes it as Y; if the reference set is Z, the number should be W" is actionable. "The evaluation is weak" is not.

Separate validity from taste, and label taste as taste. A preference for a different architecture, baseline family, or narrative order is extension or presentation, never validity. Two reviewers agreeing is not evidence.

Claims inflate at section boundaries, so read across them: conclusion against results tables and against negative results; headings against the paragraphs beneath; summary against a discussion hedge (`narrate2nav` p7 concedes the model is "not yet ready for different robot embodiments" on the page headlining a 41.67% improvement); and any new dimension of merit no table reports (`e_socialnav` p4 claims "reduced energy consumption" from a table with throughput but no energy). A contradiction can sit inside one page: `mrvs` p13 calls its night result the best precision at 0.440 while the table on that page gives a baseline 0.623.

End with a repair order: claim-changing issues, then experimental reporting, then exposition. Offer the narrower claim wherever it suffices, and say plainly what you could not assess.
