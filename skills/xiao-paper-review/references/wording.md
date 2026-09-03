# Wording a claim so it is clear and solid

Use while editing a sentence. Every `key pN` is a physical PDF page in this study's 137-paper corpus.
`../scripts/lookup_evidence.py --key KEY` returns that paper's record, not the page: to open the page, append
`#page=N` to the record's `source_url`. Most pages cited here are absent from the ledger's `evidence_pages`, so an
anchor missing from it is not a broken anchor — it still needs the PDF. Quotations below are ≤8 words. These rules
are a **correction to apply**, not a description of corpus practice — see the note at the end.

## 0. The 30-second pass — run this first

1. `significantly` — a named test with statistic, p and n? Else print the number and its n.
2. `real-time` — a Hz or ms, and the deadline it meets?
3. `extensive` / `comprehensive` / `thorough` — replace with the count.
4. `the first` / `novel` — add a knowledge hedge or delete.
5. `ensure` / `guarantee` / `always` / `collision-free` — a proof with assumptions, or a measured rate.
6. `confirms` / `proves` / `validates` — downgrade to "is consistent with" unless a prediction could have failed.
7. `up to` — add the median. Every `N×` — re-derive from the table; delete ratios against zero.
8. Every percentage — points or relative, denominator present, recomputable from a printed table?
9. Every `±` — defined over what unit, and is the spread wider than the gap you claim?
10. Read the conclusion's metric list against your table headers, the conclusion against your **negative**
    results, and each heading and caption against its own paragraph.

## 1. The claim-strength ladder

Find the highest rung your evidence reaches. Use that rung's verbs; carry that rung's fence.

| Rung | Evidence that must exist | Verbs licensed | Fence required |
| --- | --- | --- | --- |
| 0 Demo | One uncontrolled run or figure | illustrates, we observed | "in a single run"; no aggregate noun |
| 1 Trials, one arm | k of n closed-loop attempts, one setting | completed k of n, demonstrates <system> can | n, platform, environment |
| 2 Head-to-head | Same task and contract; you re-ran the comparator | reduced X from a to b, lower X than B | comparator, n per arm, what was held fixed |
| 3 Ablation | Arms differ in exactly one factor | attributable to F, removing F costs g | that single difference — else the confounds |
| 4 Held-out split | A named axis withheld from training | transfers to held-out <axis> | which axis: scene, operator, terrain, platform |
| 5 Repeats + dispersion | Several seeds or sessions, a spread | consistently, reliably, stable across | repeat count and dispersion measure |
| 6 Statistical test | Named test, statistic, p, n | significantly, detectably | test, statistic, p, n |
| 7 Proof | Theorem with stated assumptions | guarantees, ensures, is optimal | the assumptions, in the same sentence |

Rung 6 done right: `applr` p5 t-tests each environment pair, reports both directions (APPLR better in 42.4% of
training environments, DWA in 4.8%), and breaks the advantage down until it shrinks (Easy 58% vs 5%, Difficult
31% vs 4%); `hallway_icsr` p10 reports F(1,26) = 10.185, p = 0.004 with its nulls. Against that, `ado` p7 writes
"This confirms that" over a table with no test (10 trials per arm, p6), then reads a progression off an adjacent
table whose own text says "three distinct runs over the identical path".
**`confirms` beside an untested comparison is the string to grep first in your own draft.**

## 2. The four fences

| Fence | Question | Skeleton |
| --- | --- | --- |
| Condition | Under what regime? | `Under <condition>, <system> <verb> <effect>.` |
| Population | Over what, how many? | `Across <n> <units> in <setting>, …` |
| Comparator | Against what, run how? | `…relative to <NamedSystem> [cite], re-run under the same <contract>.` |
| Measurement | Measured how, over what subset? | `…measured as <metric> over <eligible subset>.` |

Attach fences as phrases or clauses; never stack four in one sentence. A fenced sentence is still strong.
`cahsor` p1 prices its trade in one clause — 62% instability reduction "while only compromising 8.6% average
speed". `mm` p1 makes the denominator the fence, "over 30,000 problem instances" beside "up to 89%"; `musohu` p1
parenthesizes its evidence base (~100 km, 20 hours, 300 trials, 13 humans — though its p3 says seven
demonstrators; reconcile a count like that before copying the form, `source-patterns.md` §15). `sober` p1 admits
the exception first, "In most cases, HLSD outperforms"; `tcgre` p1 puts the assumption inside the guarantee
sentence.

Fences fall off at boundaries. Captions and headings are read more often than setup paragraphs and carry the
stricter burden: `cahsor` p8's caption reads "ON UNSEEN TERRAIN" where its p6 setup says "locations with similar
terrain"; `barn26_report` p7's heading asserts "ROS Teams Significantly Outperform ROS2 Teams" where its p8 prose
writes "This disparity suggests".

## 3. High-risk vocabulary

| Word | Reader infers | Licensed by | Honest alternative, with a corpus instance |
| --- | --- | --- | --- |
| significant(ly) | A hypothesis test | Test, statistic, p, n | The number and its n (`ado` p1 "significantly reduces modeling error"; 10 trials/method, no test, p6) |
| safe / collision-free | Bounded worst case | A proof, or a measured zero with n | Mechanism plus rate (`barn24_report` p6 "ensures collision-free navigation"; 5/9 trials, p3) |
| real-time | A met deadline | Measured rate plus the deadline | "<r> Hz on <hw>, above the <d> Hz <consumer> needs" (`humain` p1 claims it; its only rate, 4 Hz on p5, is the data-processing frequency, not an inference rate) |
| robust | Graceful off-nominal | A perturbation sweep and degradation curve | The perturbation and range survived (`emily_iros` p3: "robustly enough in all our field experiments") |
| general(izes) | Holds over a population | ≥3 points on the named axis | "transfers to <one held-out axis>" (`zlik` p1 claims plural "gaps"; one physical platform, p6) |
| state-of-the-art | The checked current best | A dated re-run against it | "the strongest baseline we could run, <Name> [cite]" (`energy_mechatronics` p14: "considered as a state-of-the-art") |
| outperforms | Wins on every metric named | A win on each | Name it (`applv` p7 "consistently improves upon APPLV-SL" on success; TEB collision 0.78% → 8.90% in its p6 Table I) |
| efficient | Cost fell on some axis | The axis — compute, energy, samples, time — in units | Say which (`tnt` p1 calls a 26.7% time cut "efficiency"; compute unmeasured) |
| scalable | A trend across sizes | ≥3 points on the size axis | "transferable across <k tested configurations>" (`car` p8 infers "effectiveness for scalable" from one family) |
| novel | Not previously done | A describable literature search | State the difference (0 of 137 titles use "novel" or "new"; `sober` p1's abstract does) |
| first | Priority | A search, never an experiment | Hedge or drop (`mgmm` p1 unfenced: "the first method to integrate past planning"; `cbm` p2 hedges) |
| human-like | Matches human behavior | Human comparison on a defined construct | Name the cue you manipulated (`hallway_icsr` p11 generalizes from one head-turn cue to "human-like facial features") |
| guarantees / ensures | Theorem or hard constraint | Rung 7 | "was sufficient in our trials" (`emily_iros` p3: a tracker to "guarantee smooth tracking") |
| end-to-end | No hand-designed stage | The whole stack, stages named | "whole-system", then list them (`ado` p7 uses it inside a "confirms" over an untested comparison) |
| zero-shot | No target-domain adaptation at all | What the target supplied, listed | Name the test-time input (`zlik` p1 supplies a language damage description) |

## 4. Numbers in prose

- **Points vs relative, spelled out.** `tnt` p6: success 6/10 → 9/10 is **+30 percentage points** or **+50%
  relative**; time 24.0 s → 17.6 s is **−6.4 s** or **−26.7%**. Both reach the abstract as bare "50%, 26.7%"
  (`tnt` p1). `coral` p1 is the corpus's clearest fix: "14.28% percentage points, or 17.85% relatively".
- **The denominator travels with the number.** `wm_vct` p1 claims "up to 60% improvement"; its p7 caption reads
  "…(OUT OF 5)". A percentage with no n is not checkable, and "up to" reports the best cell — pair it with the
  median (`mgmm` p1 "up to 90%", `car` p8 "up to 67.2%").
- **Label conditional metrics.** `wm_vct` p7 and `tnt` p6 write time "of successful trials" — copy that. A mean
  over successes rewards failing fast, so print it beside the success rate; `adp` p6 instead caps failed trials
  at 50 s, and says so.
- **Ratios of small integers.** `hacl` p6's caption claims "5-10 times better" where its table gives 6.62 vs
  0.62 m/s (≈10.7×) and 80% vs 0% success. Never divide by zero; re-derive every "N×" from the table.
- **Reconstructibility.** Name the reference set. `humain` p7's 29.8% is not recomputable from Table I (p6)
  without guessing strongest-baseline vs baseline-mean; `tnt` p1's 9.2% recovers only as mean absolute roll plus
  pitch summed, 16.3° → 14.8° (this study's reconstruction, not the paper's), an aggregate that hides a losing
  pitch column.
- **Give a range, not a point,** when n is small or spread is wide: `hacl` p6 reports hardware velocity as
  3.2–4.4 m/s; `verti_bench` p9 states its limit as "real time factor ranging between 0.4 and 1.5".
- **Define "±"** — std, SEM or IQR, over what unit. `humain` p6's 0.578 ± 0.374 vs 0.753 ± 0.397 describes
  overlapping distributions, contradicting "consistently outperforms" on that page; `tnt` p6's WMVCT time is
  21.1 s ± 24.90 s, an SD above its own mean. Round to the precision your n supports.

## 5. Comparatives

Name four things or the comparison is unfalsifiable: **against what** (a named, cited system), **on what metric**
(one), **under what shared contract** (sensors, compute, tuning, episode definition), **with what spread**.

- Put the within-group spread beside the between-group gap. With spreads like `humain` p6's, the strongest
  available sentence is `<ours> has the lowest mean on all three metrics, though per-sample spread is large`.
- Report both directions and the subgroups: `applr` p5 prints wins and losses, then shows its own advantage
  shrinking with difficulty. A gap that survives its breakdown outranks a mean.
- Check the arms share a platform: `hacl` p4's Table II varies the robot per column (Go1, AnyMal, A1, Mini
  Cheetah). Numbers quoted from other papers on other hardware are anecdotes.
- Print the absolute beside the relative: `dyna_lflh` p6 reports beating classical and supervised baselines on a
  table reading 0.50 vs 0.40 vs 0.15. And an A-vs-B gap licenses a claim about A vs B only — `applv` p7 reads its
  gap over APPLR as evidence for vision-language input, though the arms also differ in backbone and pretraining.

## 6. Hedges that inform, hedges that hide

| Hedge | Signals | Verdict |
| --- | --- | --- |
| in <N> indoor layouts; on the tested <platform> | Bounded population | Keep — a fence, not a hedge |
| "to the best of our knowledge" (`cbm` p2) | Search limit on a priority claim | Keep, on priority claims only |
| "we conjecture / posit / speculate" (`applr` p5, `multimodal_social_nav` p6) | Explanation offered, untested | Keep; say what would test it |
| "we cannot validate this speculation, as …" (`social_llava` p6) | A blocked test, named | Keep — the corpus's strongest |
| "preliminary" (`scand` p1) | Evidence level declared | Keep when true |
| "may", "could", "has the potential to" | Author uncertainty, unbounded | Cut, or make it a condition |
| "generally", "often", "tends to" | Unquantified frequency | Replace with the count |
| "quite", "relatively", "fairly" | Nothing | Delete |

Over-hedging deletes the contribution: a closing sentence that would stay true had every experiment failed is not
a result sentence. Move the softness from the verb to the scope — `Under <condition>, <method> improved <metric>
from <a> to <b> over <n> trials; whether this holds for <untested axis> is open.`

## 7. Verb and noun discipline

- Prefer checkable verbs — *reduced, completed, transferred, ran at, required*. Distrust *validates, confirms,
  proves, showcases, unlocks, paves the way*. *Demonstrate* is the commonest claim verb in this study's abstract
  lens (44 of 126 final claim sentences — this study's own count over the abstracts it could parse; the shipped
  ledger does not record the per-paper values, so re-run the count over the sources before relying on it): honest for existence, dishonest
  where the reader hears *outperform*.
- Never infer a mental state from an accuracy gap: `applv` p7 reads a performance margin as models that
  "effectively understand" navigation scenarios.
- Replace container nouns — *framework, pipeline, approach, module* — with the mechanism: "a per-scene
  planner-parameter policy", not "an intelligent navigation framework". The genus is a promise: write *framework*
  and reviewers ask for components; *benchmark* and they ask for coverage.
- A conclusion may restate problem, mechanism, the claim at the granularity measured, and scope — never a merit
  dimension no table reports. `e_socialnav` p4 claims "reduced energy consumption" where its tables report
  throughput; `adp` p7 names safety in a summary whose physical table (Success / Progress / Time) has no safety
  column. **Read your summary's metric list against your table headers.**

## 8. Rewrite gallery

Weak sentences are synthetic, written for this file, instantiating a pattern this study observed; the citation
names where it appears. Repairs keep placeholders, so nothing here is pasteable.

| # | Weak (synthetic) | Diagnosis | Repair |
| --- | --- | --- | --- |
| 1 | "Our planner significantly outperforms the baseline." | Rung 6 verb on rung 2 evidence (`ado` p1) | `Against <NamedBaseline> [cite] under the same <contract>, over <n> trials per arm, <ours> cut <metric> from <a> to <b> and raised success from <k>/<n> to <j>/<n>.` |
| 2 | "The controller ensures collision-free navigation in clutter." | A check is a procedure, not a proof (`barn24_report` p6/p3) | `The controller rejects trajectories intersecting current lidar returns; <k> of <n> trials finished without contact.` |
| 3 | "The network runs in real time on the robot." | Deadline claim, no measured rate (`humain` p1) | `The network runs at <r> Hz on <hardware>, above the <d> Hz the MPC loop needs.` |
| 4 | "Our model generalizes across embodiments." | Crossing a gap once is existence (`zlik` p1/p6) | `<Ours> transfers without retraining to one held-out <platform>; further <axis> values are untested.` |
| 5 | "We are the first to learn terrain costs from video." | Priority asserted by experiment (`emily_iros` p1; repair at `cbm` p2) | `To the best of our knowledge no prior work learns <X> from <Y>; our <n> trials demonstrate one.` |
| 6 | "Our method consistently outperforms all baselines on three metrics." | Spread swamps the gap (`humain` p6) | `<Ours> has the lowest mean on all three, though per-sample spread is large (<a> ± <s> vs <b> ± <t>).` |
| 7 | "Adding language input validates that semantics improve navigation." | Arms differ in more than the named factor (`applv` p7) | `<A> beats <B> on every planner; since they also differ in backbone and pretraining, this does not isolate modality.` |
| 8 | "The gaze study shows humans prefer human-like robots." | One cue swapped for its category (`hallway_icsr` p11) | `A head-turn gaze cue produced fewer trajectory conflicts than an LED signal (n = <N>); other humanlike cues untested.` |

Now run §0 over your own paragraph.

## Note: the corpus is not the standard on this axis

Re-verified here by regex over the 136 machine-readable papers (the 137th has no text layer): seeds mentioned in
**8**; a named statistical test in **14**; a numeric p-value in **5** (pattern `p <= 0.d`; 8 counting the phrase
"p-value"); `±` in **44**; "ablation" in **31**; "failure case/mode/analysis" in **21**. By the ladder above,
this corpus under-reports uncertainty; its abstracts are less fenced than its results sections deserve.
Take the move grammar from it and the fencing discipline from its best pages: `applr` p5, `hallway_icsr` p10,
`social_llava` p6, `verti_arena` p5 (lower errors on stone dust "therefore do not imply" the surface is easy),
and `lflh` p6, which prints its losing SPL (0.56 vs Ego-Planner's 0.74) and re-scopes — it "trades off aggressive
motions for safety". Inflation happens at section boundaries, where a fenced result is summarized by someone who has lost
sight of the fence.
