# Astra instruction audit — 2026-09-16

This maintenance pass applies the user-supplied “Rethinking skills and prompts for GPT-6 Astra” article and the [official Astra prompting guidance](https://developers.openai.com/api/docs/guides/latest-model). It changes instructions, not the model configuration or historical corpus evidence.

## Findings and changes

| Finding | Change | What remains essential |
| --- | --- | --- |
| Descriptions enumerate many overlapping tasks. | Shorten them around writing/development versus substantive assessment. | Robotics domain and source-informed purpose. |
| Entrypoints repeat mode details and numbered workflows. | Route detailed work to existing references and express scientific criteria without a fixed sequence. | Claim/evidence alignment, factual fidelity, and scope. |
| Retrieval mechanics and provenance occupy both roots. | Move them into identical standalone `source-retrieval.md` references. | Original-page verification and bounded historical coverage. |
| The project has no repository `AGENTS.md`. | Add contextual reading, local authorization, completion criteria, and proportionate validation. | Standalone installation, shared-file parity, and distribution hygiene. |
| Good source patterns exist, but comparative learning is spread across references. | Add `learning-from-papers.md` for source observation, inferred lesson, counterexample, and transfer. | Learn reasoning without imitation or importing source results. |

These are project design decisions, not experimentally established improvements in Astra performance. The detailed research-design, drafting, and review references remain available. No new paper reading or evidence-ledger audit is claimed.

## Validation and limits

Use the offline package tests for reference paths, shared-resource parity, provenance, lookup behavior, and private-file exclusion. Skill validation checks the entrypoints' structural validity. Neither establishes instruction quality.

For this instruction pass, inspect these existing synthetic walkthroughs against the new routes:

- Grammar-only request: answer directly; no corpus loading or research audit.
- Idea without results: produce useful provisional prose with explicit missing evidence.
- Coupled method changes: retain package value without claiming component causality.
- Dataset contribution: assess resource utility without requiring a new policy.

Additional acceptance cases for future behavioral evaluation:

- An inaccessible original: identify a ledger-derived summary and avoid asserting fresh page verification.
- A request to learn from a strong introduction: explain the passage's function and transfer it to new facts without copying distinctive prose.
- A request for a full section: complete the section and expose consequential missing facts, rather than returning only an outline.

The cases above are inspection criteria, not recorded independent model runs. To measure improvement, compare old and new instructions on the same held-out requests and supplied artifacts, recording factual errors, scope violations, unnecessary clarification, completion, and relevant reading volume. Keep evaluator judgments separate from package test results. Independent agents or paid model runs need the applicable authorization; this maintenance task does not introduce an automated evaluation service.
