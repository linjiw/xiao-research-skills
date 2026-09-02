# From an idea to a decisive experiment

Build only as much of this research brief as the user needs:

1. **Deployment context:** robot, environment, user need, failure cost, resources.
2. **Observed bottleneck:** concrete failure and the assumption that might explain it; mark the explanation tested or conjectured.
3. **Nearest alternatives:** what works already, what changes in the target setting, and why that difference matters. Verify novelty separately.
4. **Mechanism:** new representation, objective, adaptation signal, hardware interface, data source, or proof; name retained components.
5. **Falsifiable claim:** “Under C, changing X should improve Y over B because M.” State what would weaken it.
6. **Evidence design:** smallest discriminating comparison, strong relevant baseline, controls/ablations, alternative explanations.
7. **Scope and cost:** training versus deployment information, tuning, compute, data collection, engineering/human effort.

## Experiment card

| Field | Decision |
| --- | --- |
| Scientific question | What uncertainty will this resolve? |
| Changed variable | What changes and what stays fixed? |
| Comparator | Relevant alternative; matched target contract or disclosed differences |
| Setting and split | Held-out scenes, people, trajectories, robots, terrain, time; correlated-sample risks |
| Eligibility and outcomes | Define in-scope cases separately from success, failure, timeout, and exclusions; primary metric, units, denominator |
| Replication | Independent unit, repeats/seeds/participants, uncertainty reporting |
| Resources | Tuning, data access, sensors, speed, compute, interventions |
| Interpretation | Support, contradiction, inconclusive result, alternative explanation |
| Safety | Offline/simulation screening and qualified real-world oversight if applicable |

Do not impose an arbitrary universal trial count. Recommend principled sizing or a pilot and qualify exploratory evidence. Adjacent frames are not necessarily independent samples.

Predefine exclusions independently of observed success. If reporting a restricted operating envelope, also disclose the full attempted denominator and why cases fell outside it. Record resets and interventions: successful segments separated by resets do not establish uninterrupted mission completion. Disclose any reference-assisted alignment, calibration, or cropping used for evaluation; geometric agreement after alignment is not automatically unassisted localization accuracy.

Prioritize the experiment by importance of the claim and uncertainty reduced, subject to cost and risk. A test that could disprove the mechanism may be more useful than another favorable scene. Offer narrower wording as an honest alternative when broader evidence is unavailable.

Useful paired readings: APPLD/APPLR for adaptation versus planner limits; MuSoHu/social-navigation guidelines for human data versus validation of human experience; early hardware/modern methods for different evidence obligations. Retrieve exact source records before teaching details.

Deliver a research brief, prioritized experiment cards, and a provisional contribution statement. Never turn a proposed result into a past-tense finding.
