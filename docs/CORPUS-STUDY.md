# The 2026-09-03 full-text study

> Historical study record. The current guidance was rebuilt on 2026-09-09; see [the new source work, corrections, and coverage limits](REBUILD-2026-09-09.md). Earlier counts and workflow descriptions below describe that earlier version.

This documents the second reading pass over the corpus: what was read, how, what was produced, and what it does not establish. The first pass and the original snapshot are described in [provenance](PROVENANCE.md).

## Why a second pass

The bundled ledger already recorded an argument-level reading of all 137 primary papers. The reference files, however, drew their patterns from roughly a dozen of them. The skills therefore taught a defensible discipline but a narrow one, and they said almost nothing about the thing a writer needs most often: how to word a claim so it survives contact with a reviewer.

## What was read

- **137 primary PDFs**, re-downloaded on 2026-09-03 from the source URLs recorded in the ledger. Every file's SHA-256 matched the recorded value — 137 of 137, no mismatches. The bundled page anchors therefore address the same bytes the first pass read.
- 11 additional related files (extended versions, with-reference variants, late-breaking reports) were downloaded for context. They are **not** in the ledger and are not counted as separate papers.
- Text was extracted with `pdftotext -layout`, which preserves table columns. 136 of 137 produced usable text; `car_jmee`, a scanned Chinese-language article, has no text layer and was handled visually, as in the first pass.

## How it was read

Two independent passes over the same corpus, then a verification pass.

**Thematic pass.** 137 papers in 29 batches grouped by research area, so that each reader saw a lineage rather than isolated papers. Each batch was read from extracted full text with the PDFs available (the scanned Chinese-language article excepted, as above), and produced a page-anchored dossier covering problem framing, title and abstract architecture, introduction structure, wording and calibration, experiment design, results reporting, limitations, figures and tables, the sharpest unanswered reviewer questions, and how the papers in the batch built on each other. Output: 29 dossiers, about 170,000 words, plus 379 structured lessons and 495 checkable page anchors.

**Cross-cutting pass.** Nine lenses read one aspect across the whole corpus rather than one paper at a time: titles and acronyms, abstract grammar, introduction architecture (split 2012–2022 / 2023–2026), limitations and conclusions, experiment design, related-work positioning, figures and tables, and an adversarial hunt for places where the writing outruns the evidence. Output: 9 reports, about 41,000 words, 203 findings, 236 sentence skeletons, and 211 measured corpus statistics. Each lens states its own counting method and coverage limits.

**Verification pass.** Every source citation in every rewritten reference file was checked against the physical PDF page by a reader whose instruction was to default to skepticism, with separate flags for personal attribution, over-long quotation, asserted venue rules, and unlabelled invented examples.

## What was produced

| File | Before | After | What it now covers |
| --- | --- | --- | --- |
| `wording.md` | did not exist | ~3,200 words | Claim-strength ladder, the four fences, high-risk vocabulary, numbers in prose, comparatives, hedges, a rewrite gallery, a sentence-audit checklist |
| `research-programs.md` | did not exist | ~2,600 words | How a line of papers compounds; what a follow-up must add; benchmarks and testbeds as durable instruments; choosing the next paper; anti-patterns |
| `reviewer-question-bank.md` | did not exist | ~3,800 words | Sharp reviewer questions organized by claim type, each with a corpus instance and the cheap answer that should satisfy it |
| `drafting.md` | ~600 words | ~5,100 words | Measured move grammar for title, abstract, introduction, related work, method, experiments, endings, figures, rebuttal, revision passes |
| `source-patterns.md` | ~1,700 words | ~3,900 words | Patterns broadened from a starter set to the whole corpus, each with observation, transfer, and boundary |
| `research-design.md` | ~600 words | ~3,400 words | Discriminating-comparison catalogue, unit of analysis, how much evidence is enough, baseline contracts, evidence-level ladder, failure accounting |
| `review-protocol.md` | ~550 words | ~3,100 words | Read order, section-by-section checks, the arithmetic pass, confound checklist, repair decision table, severity calibration |
| `genre-guide.md` | ~450 words | ~2,000 words | Ten genres including challenge reports and tech reports; venue and format calibration from measured page counts; mixed contributions |

The ledger gained seven browsable fields per record — `venue`, `venue_kind`, `venue_full`, `awards`, `artifacts`, `paper_type`, `research_line` — with no existing field changed. `research_line` is this study's editorial grouping, not a label the authors use.

## What this does not establish

The reading is argument-level. It is not reproduction, proof checking, code audit, or exhaustive inspection of every figure and table cell. Counts reported in the reference files were computed by regular expression over extracted text, and each carries its method; two-column extraction interleaves columns, so multi-word phrase counts across line breaks are unreliable and were avoided.

The corpus is **coauthored** work. Nothing here attributes a method, a sentence, or a belief to any individual, predicts anyone's review, or claims anyone's endorsement. Where a reference file observes that a sentence outruns its evidence, that is a craft observation about a sentence offered as a teaching case — not an allegation about people, and not a finding that the paper's contribution is unsound. Several of the same papers supply the corpus's best calibration writing.

Venue page limits and submission requirements change. The observed page counts in `genre-guide.md` describe what was published; the current call for papers is the authority.
