# Working on this repository

This project packages two standalone robotics research skills. Improve scientific reasoning and clear writing from public coauthored work; do not imitate an author or imply endorsement.

## Astra and task completion

For GPT-6 Astra and other capable agents, specify outcomes and evidence boundaries rather than mandatory itineraries. Follow the user's requested scope and format. For an authorized local change, carry it through implementation, relevant validation, and repair of failures caused by the change. Do not stop at a proposal or ask again for routine reversible edits. Ask when missing information would materially change the result; continue independent work meanwhile.

A maintenance task is complete when the requested files are updated, affected package invariants have been checked, and remaining limitations are reported. Passing package checks does not establish scientific correctness or improved model behavior. Do not expand a skill edit into a new corpus audit, installed-skill replacement, model configuration change, or publication unless requested.

## Read according to the change

- Skill routing or descriptions: inspect the affected `skills/*/SKILL.md` and its relevant references. Keep descriptions short and discriminating; keep the entrypoint a router with essential constraints.
- Research or writing guidance: preserve observation → interpretation → transferable practice → boundary. Prefer a useful counterexample over another universal rule. Read the relevant mode reference, not the entire corpus.
- Evidence or coverage changes: consult `docs/PROVENANCE.md`; use `docs/CORPUS-STUDY.md` and `docs/REBUILD-2026-09-09.md` for the historical passes. Verify original pages before adding precise source claims. Do not rewrite historical reading scope to imply a fresh audit.
- Retrieval or packaging: inspect `tests/test_package.py` and the affected helper. Each skill must work when installed alone.

## Package invariants

The two skills intentionally duplicate `evidence-ledger.json`, `genre-guide.md`, `source-patterns.md`, `source-retrieval.md`, `wording.md`, and `lookup_evidence.py` within their corresponding folders. Keep these shared copies identical; avoid cross-skill runtime dependencies.

Keep PDFs, extracted full text, private drafts, credentials, and personal absolute paths out of distributed files. `local-papers/` is an ignored optional local collection. Historical ledger analysis is not evidence that the current assistant inspected an original. Do not invent citations, results, novelty, or reading coverage.

## Proportionate validation

`python3 -m unittest discover -s tests -v` checks provenance, shared resources, lookup behavior, and distribution hygiene. The tests are offline, use disposable fixtures, and have no production access. Run affected checks and fix regressions without repeated approval; stop testing when the relevant checks pass unless new evidence warrants more.

For substantial instruction changes, use the relevant cases in `docs/SCENARIO-WALKTHROUGHS.md` to inspect scope preservation, factual fidelity, and completion. Label self-checks honestly. New tests should exercise behavior or package invariants, not exact prose or heading choices. Delegate only when the user explicitly asks for agents.
