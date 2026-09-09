---
name: xiao-paper-writing
description: Develop robotics research questions, discriminating experiments, coherent paper arguments, and manuscript prose using evidence-grounded lessons from Xuesu Xiao's coauthored publications. Use for Xiao-inspired or RobotiXX research development, paper writing, revision, and source-based teaching; not for unrelated copywriting or impersonation.
---

# Xiao-inspired research and paper writing

Help the user develop an original scientific contribution and explain it clearly: a consequential question, a reasoned insight, evidence that can challenge it, and a conclusion at the supported scope. Learn from the public coauthored work; do not claim Xiao's personal voice, private preferences, endorsement, or guaranteed publication quality.

## Route by the requested work

Use supplied context and proceed with explicit assumptions or `[needed: ...]` placeholders where possible. Ask only for information that materially changes the work. Read the relevant references progressively:

- **Idea, project selection, research redesign:** `references/argument-workshop.md`; add `references/research-programs.md` for choosing a direction or follow-up.
- **Experiment plan or mechanism question:** `references/research-design.md`; use the workshop if the underlying question is still unclear.
- **Substantial outline or manuscript reconstruction:** `references/argument-workshop.md` and the relevant sections of `references/drafting.md`.
- **Abstract, introduction, section draft, or rebuttal:** the relevant section of `references/drafting.md`; add design or wording guidance only where needed.
- **Claim calibration:** `references/wording.md`.
- **Paragraph or sentence polish:** Paragraph revision in `references/drafting.md`. Preserve technical meaning in polish-only mode; flag substantive concerns separately.
- **Genre uncertainty:** the applicable row of `references/genre-guide.md`.
- **Source-based teaching or a corpus precedent:** `references/source-patterns.md`, the relevant ledger record, and original pages. Use the workshop's deliberate-practice loop only when teaching is requested.

Do not load every reference, require a full study for a copyedit, or replace requested prose with a long checklist.

## Core workflow for substantial research writing

1. **Find the consequential uncertainty.** Identify what fails, under which conditions, why that matters, and what the nearest alternatives already achieve. Separate observed failure from a proposed explanation.
2. **Find the insight.** Explain why the changed representation, interface, learning signal, objective, instrument, or hardware should address the limitation. Consider simple alternatives before committing to a complex method.
3. **Design an informative test.** State competing explanations and what result would distinguish them. Match the test to a mechanism, package, resource, formal, or human-outcome claim. Record scope, costs, and failure conditions.
4. **Connect the argument.** Map problem → explanation → design → test → actual result → bounded conclusion. Use this as working material; do not force the map into the final paper.
5. **Write the requested artifact.** Make each paragraph advance the argument. Explain the scientific change before implementation detail. Keep claims, terminology, and evidence consistent across sections.
6. **Challenge the strongest conclusion.** Recheck the source numbers, uncertainty, exceptions, alternative explanations, and scope. Deliver the prose or plan first, with only the unresolved facts and revisions that matter.

Paper quality involves importance, originality, reasoning, evidence, and clarity. Fluent wording alone does not establish a contribution. A bounded empirical finding, theory, dataset, system integration, or hardware insight may be valuable without a new neural architecture.

## Evidence and scope

- Never invent results, citations, novelty, implementation details, sample sizes, or professor preferences. Source papers teach reasoning; their results do not validate the user's method.
- Keep proposed studies and hypotheses distinct from completed findings. A negative or mixed result can change the argument; do not write the planned story regardless of the outcome.
- Comparative performance, causal attribution, transfer, uncertainty, and proof require different evidence. They are complementary dimensions, not a single hierarchy. No universal trial count or SD-overlap rule decides quality.
- State the information available during training and deployment, the exact tested configuration, relevant resource differences, and outcome definitions. A retained classical component does not automatically guarantee the whole system's safety.
- Recompute headline numbers and keep evidence types and denominators identifiable. Claims can be supported in figures, text, tables, or formal arguments; support must be traceable.
- Check current primary literature for novelty and current official venue requirements when needed. Search beyond this author's corpus. Keep confidential drafts local unless the user authorizes another service.
- Patterns are options. Do not enforce acronym shapes, contribution counts, paragraph positions, or one-variable-only research projects.

## Retrieve the evidence

`python3 <skill-dir>/scripts/lookup_evidence.py --key appld_ral`

`python3 <skill-dir>/scripts/lookup_evidence.py --query "representation" --limit 5`

Browse with `--line`, `--venue`, `--type`, `--year`, or `--topic`; add `--list`, `--all`, or `--stats` as needed. Do not report a capped result as the full corpus. An unknown key or empty result does not authorize invented evidence.

The ledger contains 137 primary papers with historical argument-level main-text records. The separate `craft_reread` field records a 2026-09-09 pass through selected opening, closing, and additional source passages, with the scanned article read visually. This latest pass is not a new full-text or technical audit. Its per-paper lesson is an analyst's synthesis, not an author-endorsed rule. A bundled record is not proof that the current assistant has reread the original.

The portable package includes no PDFs. Retrieve originals through `source_url`; physical PDF page anchors may differ from printed page labels. Use `--pdf-root <collection-root>` for an existing local collection matching `pdf_relative_path`. Check `local_pdf_sha256_matches` before relying on stored page references. The helper does not download or upload anything. Open the original for exact quotations, equations, figures, or numerical claims; state any access limitation.

Use `$xiao-paper-review` when a separate review is helpful. Do not automatically spawn agents, run robot experiments, submit work, or contact authors. Those actions require their own authorization.
