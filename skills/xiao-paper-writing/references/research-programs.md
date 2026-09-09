# Choose a research direction that earns its place

Use for project selection or planning a line of work. The line names are this study's editorial grouping of coauthored papers, not claims about individual authors' plans. A shared topic is not proof of a direct historical dependency; inspect citations before asserting one.

## Follow the unresolved constraint

A useful next project changes what can be explained, achieved, measured, or afforded. It can introduce a new mechanism, test a disputed explanation, relax assumptions, create an instrument, or consolidate a framework. It need not change exactly one variable, and a reused benchmark need not define the entire research agenda.

| Illustrative sequence | Question that changes | Reusable lesson |
| --- | --- | --- |
| `appld_ral` p1 → `apple` p1 / `applr` p1 → `applv` p1 | How can planner adaptation use different information or learning signals? | A stable interface makes alternatives easier to compare, while every new learner owes its own cost and performance evidence. |
| `hallucination` p1 → `sober` p1 / `lflh` p1 → `lfh_cp` p2 | Which collection, runtime, or representation requirement still restricts learning? | An explicit residual requirement can motivate a follow-up more clearly than an architectural upgrade. |
| `vw` pp1,6 → `wm_vct` p1 → `verti_bench` p1 / `verti_arena` p1 | Is mobility mechanically possible, can autonomy exploit it, and how can it be evaluated? | Platform, model, and instrument contributions can make one another testable. |
| `team_coordination` p1 → `team_coordination_rl` p1 / `hpr-tcgre` p1 | How does coordination change with scale and more realistic information assumptions? | Retain the problem's meaning while making each relaxation and its cost explicit. |
| `offroad` p1 → `vi-ikd` p1 → `cahsor` p1 | What aspects of vehicle-terrain interaction must the controller predict? | New operating regimes can expose missing state or information rather than merely insufficient model capacity. |
| `musohu` p1 / `scand` p1 → `vanp` p1 | Which recorded information can teach navigation-relevant representations? | Data value depends on what it enables downstream; amount alone is insufficient. |
| `risk_ssrr` p6 → `risk_ral` p8 | Does the formal definition justify the assumed risk properties? | Revising a prior definition can be a substantive contribution if the consequences are clear. |

These sequences are teaching comparisons, not exhaustive histories or proof that one paper caused another.

## Compare candidate projects

For each plausible direction, write a short brief:

- The consequential uncertainty and the evidence it remains open.
- The strongest existing alternative, including a simple repair.
- What new knowledge or capability would survive even if the favored method loses.
- The discriminating study, required resources, and likely failure modes.
- What would make you stop, simplify, or change the question.

Judge candidates by importance, originality, ability to obtain informative evidence, feasibility, and cumulative value. Use the user's constraints; do not create a spurious numerical score from arbitrary weights. A cheap study is not valuable if the question is trivial, and a large study is not valuable if its outcome cannot distinguish explanations.

A well-designed negative result can redirect the program: a tuned baseline may remove the apparent need for a new method; a null ablation may favor simpler deployment; a failed transfer may locate the missing information. Do not define success solely as producing a favorable leaderboard.

## Build instruments when they unlock questions

A dataset, simulator, testbed, or benchmark can reduce future research cost. It earns a paper by making a consequential question answerable with a documented protocol, useful coverage, and evidence of what the instrument represents.

Keep versions, split rules, baseline configurations, and metric definitions stable enough to compare results. Change them when scientifically necessary and report the break in comparability. Treat a benchmark's assumptions as research limitations: `verti_bench` p9 identifies ideal perception and limited physical counterparts as boundaries. `barn26_report` p7 shows that cold trials can expose deployment work hidden by tuned scores.

Do not choose a project merely because the existing instrument makes it easy. Ask what phenomena the instrument excludes and whether that exclusion now limits the research question.

## Write the follow-up's difference plainly

A useful sentence is:

> [Prior work] established [bounded result] under [assumption]. We study [remaining question] by changing [mechanism or design], while retaining [shared parts] and evaluating [new obligation].

Multiple changes are legitimate when necessary. Explain their dependencies and choose comparisons that distinguish the claims the paper actually makes. Integration itself can be the contribution when its system-level value is the question; do not invent independent component novelty.

A limitation can seed a project when it identifies an uncertain condition and a test that would decide it. `mrvs` p19 distinguishes its integrated evaluation from future feature-by-feature comparisons. `nasa` pp9,159 separates enabling stages and readiness levels. These offer different ways to plan a program without promising that every proposed next step will work.

Deliver a recommended direction with its scientific reason, decisive next study, main risk, and viable alternative. If the user supplies no project, teach the framework or use an explicitly hypothetical example; do not pretend to have selected a novel publishable contribution for them.
