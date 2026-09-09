# Match the evidence to the contribution

Apply the rows that bear on the actual claims. Mixed papers may need several rows. These are methodological distinctions, not a venue checklist or a guarantee of acceptance.

| Contribution | Main question and evidence | Inappropriate automatic demand |
| --- | --- | --- |
| Algorithm or integrated system | Defined problem and information; relevant comparators; system benefit and any claimed mechanism; cost, failures, and scope | A larger model, replacement of classical components, or an ablation for every implementation detail |
| Dataset | What question the data unlocks; collection and annotation; coverage, splits, leakage, access and applicable permissions; useful validation | A novel algorithm or a claim of algorithmic superiority |
| Benchmark, simulator, or testbed | Which phenomenon it measures; reproducible tasks and scoring; fidelity and coverage; discriminative results; assumptions | Universal realism, field readiness, or ranking every method |
| Theory, planning, or control | Precise definitions and assumptions; valid derivation; approximation, complexity, and connection to implementation | Physical experiments for a purely formal claim |
| Human or social study | Defined construct; recruitment and population; protocol; relevant order, learning and dependence effects; suitable measurement and analysis | Treating geometry, imitation, or low collision rates as sufficient evidence of comfort |
| Hardware, field system, or case study | Requirements linked to design and measurement; operating envelope; integration costs, interventions, failures; achieved versus projected ability | ML-style component ablations unrelated to the claim |
| Survey, position, or methodology | Declared scope and selection; defensible synthesis, counterexamples, and useful implications | Treating a position paper as an exhaustive systematic review |
| Challenge report | Rules and changes; entrant/attrition counts; complete outcomes; operational confounds and limits of inference | A controlled causal ranking of whole algorithm classes |
| Technical report | Clear separation of measured, borrowed, projected, and proposed claims across components | Letting an integrated roadmap inherit the strongest evidence of one component |
| Workshop or late-breaking abstract | An intelligible idea, evidence status, and precise open questions | A fictitious full-paper verdict from a short abstract |

## Source examples that change the review

`car_jmee` pp6–10 links intended display functions to mechanical and control subsystems, then reports functional demonstrations and unfinished control integration. It illustrates a requirements-to-test argument, not validation of every intended use.

`social_nav_guidelines` p11 explicitly recommends choosing methodology for the research question. Human data can have participant, session, encounter, or other dependency structures: identify them rather than imposing one unit on every design.

`hirl_vision_paper` p3 states that its aim is a vision and research agenda rather than a systematic survey. Assess the reasoning and scope it actually promises.

`verti_bench` pp1,9 motivates interactive mobility evaluation and identifies ideal perception as a limitation. `mtc` pp1,7 couples scene geometry to motion collection and evaluation. The benchmark's artifact value and its downstream claims deserve separate assessment.

`mrvs` p19 distinguishes integrated experience from causal effects of individual features. An integrated evaluation can support a system contribution without establishing every component's isolated effect.

`nasa` pp9,159 separates exploration stages and near-term possibilities from deep-access development. Readiness claims should retain those boundaries.

## Format and mixed contributions

Check current official venue instructions when a format or submission decision depends on them. Published lengths in this corpus do not establish present page limits, required contribution counts, section order, or mandatory robot trials.

Obligations follow each claimed contribution. A dataset-plus-algorithm paper owes data provenance and evidence for its comparative algorithm claims. A theory-plus-system paper must explain which properties the implementation retains. A resource may remain valuable if its demonstration method loses, but central measurements of the resource itself still need to be correct.

Distinguish the operational question from the explanatory question. Unequal resources can be relevant to a deployment comparison; matched controls may still be needed for a specific attribution. A correctly bounded limitation is a boundary of the contribution, not an automatic reason to reject it.
