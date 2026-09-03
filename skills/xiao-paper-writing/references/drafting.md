# Drafting, section by section

Measured architecture of 137 coauthored papers (2012-2026). Patterns are **sentence skeletons with placeholders**, never prose to copy. Counts describe this corpus — a baseline to beat, not a quota — and where its own sentences outrun its evidence, that is an observation about a sentence. Anchors are physical PDF pages.

**Status of the counts.** Every percentage and tally below is this study's own — close reading plus regex over the extracted text of the 136 machine-readable papers (the 137th has no text layer). Denominators are the population read for that lens — 137 titles, 133 abstracts, 134 closing sections, 135 recoverable Figure 1 captions — not always all 137. The shipped `evidence-ledger.json` holds per-paper metadata, not the codings behind these aggregates, so no `key pN` anchor verifies one: to recount one, obtain the sources through each ledger record's `source_url` and re-run the stated method. The page-anchored examples are checkable against the original paper; the aggregates are not.

## 0. The five revision passes — start here, then open the section you need

1. **Argument.** One gap, one mechanism, one claim, all naming the same thing; the contribution list naming the same comparison class as the results table.
2. **Evidence.** Per claim: setting, comparator, metric, denominator, unit of analysis, dispersion, exact location of the number. Untested claims become hypotheses or go.
3. **Calibration.** Verb tier against denominator; superlatives, "significant", "safe", "real time", "general", "first". Every number carries metric, setting, and N in one sentence; recompute every percentage from the table. (84 of 136 papers use "significantly"; 73 report no test anywhere.)
4. **Structure.** Gap by paragraph 2, Figure 1 cited at the hinge, contributions before the end of page 2, limitations under a heading.
5. **Sentence.** Concrete transitive verbs; specific nouns over promotional adjectives; the acronym introduced once and then used; priority sentences proofread last and hardest.

## 1. Title

Slots coded over all 137 titles: **capability** 120 (88%), **mechanism** 88 (64%), **setting** 60 (44%), **coined name** 50 (36%), **genre word** (Dataset, Benchmark, Survey) 30 (22%), **metaphor** 11 (8%). Capability first; mechanism only if it is what you changed; setting only if it is what makes the problem hard. Absent everywhere: **"novel"/"new" (0 of 137)** and **any quantitative result** — headline numbers live one layer down (`hacl` p1, "peak forward velocity of 6.7 m/s"). Median 10 words; a colon in 52%, usually `<Name>: <what it is>`.

**Acronyms.** 50 titles carry a coined name, 29 letter-mapped. Grade the mapping: *exact* (the subtitle **is** the expansion, letter for letter — the APPL\* family), *pun-first* (the reader supplies or reorders letters), *mismatch* (the subtitle names the task while the acronym encodes the architecture). **If the expansion cannot be the literal subtitle, change the acronym or drop it.** At least 23 papers instead spell the mechanism out and keep the acronym in the body: a spelled-out title is searchable, a name used once is decoration.

**Family membership.** A family exists only if the name is a template varying exactly one dimension: APPL\* the supervision source, Verti\* the artifact's role, the TCGRE line the assumption dropped. **A new member must supply a genuinely different value on that dimension, legible from the title alone.** `Toward X` (3 titles) names an unreached capability only if the colon says what you shipped instead (`vw` p1).

**Title-to-abstract contract.** Of 48 `<Name>: <subtitle>` titles, about 8 open the abstract with the name; ~83% state the gap first. **A coined name in the title obliges the abstract to withhold that name until the gap is stated.** Name-first belongs to resource papers, where the artifact is the news. Leaving a shipped system or benchmark out of the title should be a decision, not an accident.

## 2. Abstract

Write to this shape first, then check it against the move table below. **Budget** (medians 174 words, 7 sentences): 1 ground (optional) · 1-2 gap · 1 propose · 2 mechanism · **1 setup, which two-thirds of the corpus skips — do not** · 1 result · 0-1 release.

Nine moves, over 133 abstracts:

| Move | Presence | Commits you to |
| --- | --- | --- |
| `PROPOSE` the contribution | 99.2% | the genus chosen; "framework" invites a component list |
| `MECHANISM` how it works | 75.9% | these components, in this order, in the method |
| `GAP` what breaks | 74.4% | this being *the* gap you close |
| `RESULT` the outcome | 60.2% | the number, its setting, its denominator |
| `GROUND` situate the task | 52.6% | relevance granted before you show anything |
| `SETUP` where evidence came from | 33.1% | those being the only settings you claim |
| `PRIOR` what others do | 24.1% | a characterization the cited authors would accept |
| `RELEASE` / `OUTLOOK` | 12% / 9.8% | a resolving URL; a discussion holding the directions |

**Ordering.** 83.5% put context and gap before the pivot and evidence after; 67.7% run `GAP … PROPOSE`.

- Gap: `[Standard assumption] may not hold when [condition], because [consequence 1]; [consequence 2].` State the gap as a **physical consequence, not a literature complaint**: `cahsor` p1 names rollover, lateral sliding, and vertical vibration rather than saying prior work ignores SE(3).
- Propose: `To address [the named gap], we propose [Expanded Name] ([ACRONYM]), a [genus] that [differentia].` 61.7% define the acronym here, 1.5% in sentence 1.
- Result: `Compared with [named system], [NAME] [verb] [metric] by [x] over [N] [units] in [setting], while [conceded cost].`

**The result sentence is the corpus's weakest slot and your cheapest win.** 43.6% of final claim sentences name no setting, 69.2% no baseline, **4.5% carry a denominator**; none fences on all four axes — spread them across two sentences rather than stacking four (`wording.md` §2). Match verb to denominator: *demonstrate* is honest at n = 5, *outperform* needs a named system and an N. `cahsor` p1 prices its trade — 62% less instability "while only compromising 8.6% average speed".

**Proposal or artifact abstract, no results yet** (15% here). Four honest closes: the artifact's dimensions (`bsn_biorob` p1, "215 trials on" 12 subjects); the affordance rather than the outcome (`verti_arena` p1, "supports reproducible experiments"); the analysis labelled preliminary; the promise placed after the result sentence. Test: **a closing sentence equally true had the experiments failed is not a result sentence.**

## 3. Introduction

Median ~540-640 words, the same for journals and conferences, which differ only in which optional slots appear. Sequence: **concession → turn (the gap) → optional second turn (the nearest fix also fails) → hinge → optional evaluation sentence → optional contributions → optional roadmap.** Gap placement: median paragraph 2; 66% land it by the end of paragraph 2, 81% by paragraph 3. One paragraph of concession is the budget.

**Blame the assumption, never the authors.** Searching 48 introductions for "et al." beside a failure verb returns **zero hits**. Where named authors appear, the verb credits them and the *next* sentence switches subject to an artifact: `vi-ikd` p1 credits a prior learned inverse-kinodynamics model, then says "inertial sensor is limited in its capability".

- Assumption: `[Existing class] achieve this by assuming [assumption]. That holds in [regime A]; in [your regime], [mechanism by which it breaks], and [consequence].`
- Ladder rung, 1-3 of them: `[Approach class] [strength granted]. While effective for [narrow condition], these methods [mechanism of failure], and consequently [observable consequence].`
- Self-critique of your own prior method: `[Your prior method] removes [old requirement], but still [residual requirement], and applies only to [narrow regime].`

**Numbered-limitation tagging is the most transferable under-used device found.** `squid` p1 names "three core limitations", tags each prior work with the numbers it fails on, then tags its own design choices with the limitation each repairs (`squid` p2). One paper in the corpus does this; it binds gap → mechanism → contribution with no slack.

**Hinge** — concrete transitive verbs, one new noun, no equations.

- Appositive (34% of modern hinges, from 6%): `To address [the limitation just named], we propose [Expanded Name] ([ACRONYM], Fig. 1), a [type-noun] that [does the one thing the gap demanded].` Use a type-noun a reviewer can classify: "a framework that…", not "a novel approach".
- Preserved component (35% of modern intros): `[ACRONYM] uses [learned component] for [high-level job] while [classical component] [low-level job], enabling [new capability] while maintaining [what the classical component guaranteed].`

**Figure 1's job.** Cited inside the introduction in 52% of earlier and 62% of modern papers, at a median 53% through the text — **at the hinge, not the hook.** It can do that work if it pictures the problem, the claimed capability, or a labelled contrast; an architecture diagram cannot, because it presupposes the method.

### Contributions — the shape of a contribution statement

Explicit lists: 23% of 2012-2022 introductions, 56% of 2023-2026. Items: minimum 2, maximum 4, mode and median 3 — **none claims five.** Modern shape: representation/formulation → algorithm → optional design-space study → evaluation, the last an evaluation claim in ~69% of lists. Write items as noun phrases; make two carry a checkable integer a reviewer can audit against a later page. Only 21% of earlier introductions bound the claim, and the strongest do it inside a contribution bullet.

## 4. Related work

81 of 137 papers carry a heading. Organizations, most common first: **ingredient/axis composition** (a subsection per ingredient you combine; the gap is their intersection) 20, **maturity ladder** (classical → learning → newest paradigm) 11, **evaluation-practice comparison** 5. Axis composition works best when every subsection is bounded on the dimension the paper moves, so the reader predicts the contribution.

**Credit-then-bound, four beats.** 40 of 46 clean sections name a mechanism-level bound; only 7 use attention phrasing ("underexplored", "remains limited"). Prefer a named assumption over a claim about the field's attention.

1. Name the method and what it buys.
2. `[FAMILY] enables [capability], but imposes [requirement] at [train/deploy] time.`
3. `In [our setting], [requirement] is unsatisfiable because [physical or operational reason].`
4. `[OURS] therefore [changed ingredient], at a cost of [conceded property].`

Two more moves: *concept substitution*, which keeps the formal machinery and swaps the concept it instantiates (`t_cbf` p2 extends control barrier functions "from collision avoidance to traversability safety"); and naming your nearest neighbour outright, as `narrate2nav` p2 does before differentiating.

**The delta sentence.** A follow-up in your own line earns its place by changing **exactly one** thing: `[Prior work] [does X] by [mechanism A]; [Ours] [does X] by [mechanism B], because [what A cannot represent].` The dimensions observed: decision criterion (`apple` p3, parameters chosen "based on the expected evaluative feedback" rather than environment similarity); horizon (`applr` p2, "goes beyond this myopic parameter" selection); prior (`pietra` p4, the predecessor "uses an uninformative prior"); scope (`energy_mechatronics` p1); interface (`vi-ikd` p2); generality (`mm` p2, "a universal technique" for any planner).

State the delta at **three altitudes** — framework, consequence, implementation — as `pietra` does at p3, p4, p5. Then **cash it**: a generality claim obliges a cross-product experiment, and the strongest instances make the prior method both a baseline and the base of the ablation.

## 5. Method

Pin down, in order:

- **Inputs and outputs** — signals, rates, frames, units at every interface.
- **Objective** — what is optimized, over what.
- **Assumptions**, as conditions of validity rather than buried in a derivation, since the limitations section will stress exactly these.
- **Algorithm**, its components in the order the abstract's mechanism sentences promised.
- **Training versus deployment information**, including what the deployed system does *not* have (privileged state, maps, ground-truth pose).
- **Retained classical and safety components**, named with the property they still guarantee.
- **Cost** — data, compute, tuning, human effort, latency, and what a new platform would require.

Tie each design choice to the bottleneck it addresses, reusing the introduction's limitation numbers as tags.

## 6. Experiments and results

Organize around questions, not apparatus: each claim gets a test, each test an interpretive purpose stated before the numbers. `research-design.md` carries the comparison catalogue and sizing.

- **Setting.** Name the tier in the sentence carrying the number — simulation closed-loop, offline prediction on recorded data, physical closed-loop — and never pool tiers in one clause. A small-*n* tier keeps its honest name into the abstract.
- **Comparator contract.** Disclose every asymmetry with numbers — data volume and quality, sensors, maps, ground truth, seeds, compute. `wm_vct` p5 discloses a baseline trained on a larger, higher-quality dataset than its own method; `humembr` p5 discloses baselines run on a "single seed" against three. Prove the baseline is not merely mis-parameterized: `appld_ral` p5 shows the same planner failing 8 of 10 trials in a narrow corridor on default parameters and succeeding in every trial once re-parameterized. Better still, strengthen a baseline until your advantage shrinks (`carol` p7).
- **Unit of analysis.** The coarsest thing you re-randomized: one course run 20 times is n = 1 course.
- **Failure accounting.** Define success and each failure mode with a threshold before running anything, and price failures rather than exempt them (`appld_ral` p5: a "penalty time value of 60 s" plus an asterisk). A metric computable only on successes carries the success fraction in the same cell.
- **The losing subgroup.** Report it, and narrow the claim rather than soften the verb. `applr` p5 breaks its win rate by difficulty — Easy 58%, Medium 37%, Difficult 31% — and conjectures why; publishing a monotone decline in your own advantage is the strongest credibility move here.

## 7. Limitations, discussion, conclusion

Order: **contribution restated → limitation → future work.** 71 of 134 closing sections (53%) name a limitation of their own contribution; 25 put "Limitations" in a heading, and the headed ones are systematically more specific. A heading is the cheapest commitment device available, and a promise you can break: check that the text under it limits *your* work, not the literature.

**The generative limitation, four steps.** Of the 71 limitation-bearing papers, S1 (a concrete observed shortfall) and S2 (the assumption or design choice producing it) are the entry; **S3, a specific candidate mechanism: 69%**; **S4, the experiment that would decide it: 37%**; both: 23%. Across all 134 closing sections the phrase family "to validate/verify/test/determine whether" occurs **once**: the corpus names fixes far better than the observation that would discriminate between explanations. Beat it with a sentence beginning *"The observation that would settle this is …"*.

- Assumption → violation → measurement: `[METHOD] assumes [assumption]. Such an assumption does not hold in [deployment setting]. Future work will inject [the specific perturbation] and measure [the quantity that would degrade].` (`verti_bench` p9's shape.)
- Name what stops being necessary: `Another direction is [generalization]. In that case, [expensive current step] is no longer necessary.` (`hallucination` p8.) Five papers use it; the highest-value construction available.

**Conclusion restatement rights.** 77% of conclusions open with "In this paper we present X"; 23% restate a number. A conclusion may restate the problem, the mechanism, the claim **at the granularity at which it was measured**, and the scope condition. It may not introduce a dimension of merit no table reports: `e_socialnav` p4 closes on "reduced energy consumption" while its tables report only text-similarity, throughput, and action-accuracy metrics. Nor may an aggregate hide the subgroup it loses: `narrate2nav` p7 reports a 41.67% real-world gain "across various challenging scenarios" while Table II on the same page shows the method worst of four in Narrow Passageway, 4/10 against 9/10, 10/10, and 8/10. A hedge one column later does not repair an unhedged aggregate — **put the qualification in the same sentence as the number.** Model close: `barn22_report` p9 hedges its verb, reports a finding about the field ("cannot yet be considered a solved problem"), and discloses that the organizers' own prior was wrong.

**Future-work test.** Delete every future-work sentence that does not point back to a named limitation and end in a clause beginning *so that / in that case / to test whether / which would*. That deletes roughly a third of this corpus's future work — this study's estimate, not a count.

## 8. Figures and tables

**Figure 1's job**, over 135 recoverable captions: hook-scenario 31 (23%), a situation that punishes the reader's current method; mechanism-contrast 18; architecture 18; hardware photo 12; environment gallery 11; qualitative rollout 11; four smaller categories, 32 combined. The most common Figure 1 is not "here is my system" but "here is the situation in which you would lose." Each job commits you: a hook-scenario to a failure you must later reproduce or measure, an environment gallery to a coverage claim whose counts belong in the caption, a qualitative rollout to nothing statistical.

**Captions.** Median 27 words for figures, 15 for tables; sample size appears in 1.4% of figure captions and ~3.5% of table captions. A caption should let a reader state what the figure supports **and what it does not**.

- Mechanism-contrast: `Left: [baseline] [does the thing it is good at], [at this cost]; Right: [ours] avoids that cost, enabling [property].` `performer_mpc` p1 grants the virtue first: "Standard MPC efficiently cuts blind corners". `tnt` p1 uses the same two-branch form.
- Results table: `[What was measured]: [count metric] (out of [N]), [rate metric] (of [the conditioning subset], in [units]) on [condition A] (left) and [condition B] (right). [Marking] indicates [exact meaning].` The corpus's best caption, `wm_vct` p7, does all of this in one sentence: "NUMBER OF SUCCESSFUL TRIALS (OUT OF 5)", conditioning, units, panel split, marking key.

**Column sets and commitments.** `Success (n/N)` as a fraction, not a percentage: the denominator rides inside the cell. `Success | Time | Angles` commits you to a conditioning decision, since time is defined only on successes — say so. `MSE ± Std ↓` commits you to nothing about n, so add it and define `±` in the caption. An `Input` or modality column, stating what each method was allowed to see, is the most reusable idea here: it makes an unfair comparison visible rather than deniable (`tgs` p6). A significance matrix — row significantly worse than column — makes the "no difference" residual computable (`appli` p5).

**Bolding.** Only 4.2% of table captions say what bold means. Fix the marking rule and the tie rule before seeing the numbers, state both in the caption, and gate bold on dispersion: **if the gap is under one reported standard deviation, bold nothing or bold both.** If bold means deployed or selected rather than best, say so, and guard against a failed method holding one: `vs` p6 gates traversal time to `N/A` at 0/10 success but still prints that row's roll and pitch.

**Design the results table before running the experiment.** Write the caption first, naming what is counted, out of how many, over what conditioning subset, in what units. If you cannot fill "out of how many" from the planned protocol, the protocol is not finished. List every environment, scenario, difficulty, and baseline before the first run, then publish the whole grid.

## 9. Rebuttal

1. **Restate the concern faithfully:** `We understand [concern] to be that [restated claim].` If you cannot restate it, ask rather than guess.
2. **Answer with evidence and its location:** `This is addressed in [Table N / Sec. N]: [the number, its denominator, its setting].`
3. **Concede genuine gaps:** `[Concern] is correct. Our evidence covers [scope]; it does not cover [what was asked].`
4. **Name the exact revision:** `We will replace [sentence] with [the narrowed claim] and add [the specific column or caption clause].` "We will clarify" concedes nothing.
5. **Never claim an experiment you have not run**, and never write a promised result in the past tense. If one is infeasible, say why and offer the narrowed claim your evidence supports.

Rebuttal is the last cheap place to add a scope qualifier: if a reviewer's question shows the abstract implies more than the limitations section allows, fix the abstract.

## Synthetic miniature example — not source-paper text

Weak: "Our intelligent planner guarantees safe and general navigation with superior performance."

Evidence-aware: "In the tested indoor layouts, the adaptive policy completed 18 of 20 routes against 14 of 20 for the fixed-parameter planner, both under the same collision-checking layer and 2 m/s speed cap. These trials support improved completion in this setting, not a general safety guarantee."

These numbers are invented **only for this teaching example**. Never reuse them as the user's results.

## Paragraph revision

Identify the paragraph's argumentative job. Preserve every technical fact. Replace generic praise with a mechanism or a measurement. Cut repetition. Add the minimal evidence qualification — setting, denominator, or comparator — in the same sentence as the claim. Return the revised paragraph and explain only consequential changes. In language-polish-only mode, flag technical concerns separately instead of silently altering a claim's scope.

## Learning loop

Explain a source as problem → mechanism → evidence → limitation. Ask the learner to reconstruct that argument from memory, propose a counterexample, name the experiment that would decide between the paper's explanation and the counterexample, then write a paragraph for their own project using the structure rather than the vocabulary. Evaluate reasoning and evidence handling, not similarity of phrasing.
