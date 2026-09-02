# Match evidence to the contribution

This is a study-derived rubric, not a mandatory venue checklist. Mixed papers may need two branches. Apply only what bears on the actual claim.

| Genre | Main evidence obligations | Avoid this false demand |
| --- | --- | --- |
| Algorithm / learned or hybrid system | Defined information and interfaces; relevant baseline; mechanism-isolating comparison; failure and transfer boundaries; operational cost | Every solution must replace classical components or use larger models |
| Dataset / benchmark / simulator | Motivation and coverage; collection/annotation protocol; splits; independence/leakage risk; accessibility/license/consent as pertinent; metrics and meaningful baselines | It must introduce a new algorithm or prove general deployment to be valuable |
| Theory / planning / control | Precise definitions and assumptions; valid derivation; scope of guarantee; approximation/complexity; experiments where empirical claims are made | A theorem is invalid merely because no robot experiment appears |
| Human / social study | Construct validity; context and population; protocol/order/familiarity; independent participant unit; uncertainty; ethics; proxy-versus-experience distinction | Proximity, imitation, or collision avoidance alone proves human comfort |
| Hardware / field system / case report | Requirements→design choices; integration tradeoffs; calibrated measurement; operating conditions; interventions/failures; achieved versus proposed capability | ML ablations are always required, or an analog demonstration proves target-environment readiness |
| Survey / position / methodology | Scope and selection method; fair taxonomy; supported synthesis; counterexamples; explicit normative recommendations | Every statement needs a new experiment, or a proposed framework is experimentally proven |

## Recurrent checks across genres

- The experimental unit can be a person, run, environment, robot, trajectory, or independent seed—not automatically a frame.
- “Generalization” must name what changed and what remained shared.
- Safety, liveness (not getting stuck), and goal completion can require different metrics.
- Baselines need relevance and disclosed contracts, not mechanical equality in every resource.
- A mechanism can be useful within a limited domain. Scope correction is often a legitimate remedy.
- Do not infer individual authorship of a method, writing move, or belief from a coauthor list.

Source examples: `social_nav_guidelines` pp11–14,24–27,41–42; `car_jmee` pp7–10; `nasa` pp34–37,135–146; `mtc` pp7–8. Consult the ledger and original pages for details.
