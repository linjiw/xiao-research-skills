# Provenance, scope, and validation

> Historical study record. The current guidance was rebuilt on 2026-09-09; see [the new source work, corrections, and coverage limits](REBUILD-2026-09-09.md). Earlier counts and workflow descriptions below describe that earlier version.

The study snapshot was assembled on September 2, 2026 from the primary-publication links on [Xuesu Xiao's GMU page](https://people.cs.gmu.edu/~xiao/#publications). The bundled ledgers identify every paper, its full citation, source URL, physical page count, source-file SHA-256, analytical observations, and actual reading scope.

The study is of **coauthored** work. Attribution to Xiao personally is not inferred from coauthorship. The skills do not impersonate him, predict his reviews, or claim his endorsement. “Research mindset” means an analyst's interpretation of observable problem-solving practices, not access to private beliefs.

## Reading coverage

- 137 primary publications, totaling 1,460 physical PDF pages.
- 135 `main-text-read` and 2 `visual-main-text` records.
- The 42 initially partial records received a follow-up main-text pass before publication of these skills.
- “Main-text read” describes argument-level reading: the problem, mechanism, assumptions, reported experiments, conclusions, and limits. It is not proof verification, reproduction, a code audit, or exhaustive inspection of every figure cell.
- References, appendices, alternate versions, and supplements have only the coverage explicitly recorded. The early scanned Chinese article was read visually; its searchable Chinese OCR was unavailable.
- The original collection contained 158 PDFs including alternate versions and supplements. They are not included in this repository and are not counted as 158 separately analyzed papers.

Page counts were checked against physical PDFs. MTC's extraction initially contained spurious form-feed characters: its correct length is 9 pages, not 25. This was corrected before the final ledger. Page anchors always mean physical PDF pages, not printed proceedings numbers.

## The 2026-09-03 full-text study

After the portable export, the corpus was re-downloaded and read again in full. All 137 source files were retrieved from their recorded URLs and every SHA-256 matched the bundled value, so the page anchors below still address the bytes that were read. All 137 papers were then read again — 29 thematic batches plus 9 cross-cutting lenses, 136 of them from extracted full text and the scanned Chinese-language article visually — and the reference files were rewritten from that reading and verified page by page against the PDFs. Method, coverage, and limits: [the corpus study](CORPUS-STUDY.md).

That second pass did not revise the per-paper analytical records; it broadened the reference files from a starter set of about a dozen papers to the whole corpus, and added `wording.md`, `research-programs.md`, and `reviewer-question-bank.md`. The ledger gained seven descriptive fields (`venue`, `venue_kind`, `venue_full`, `awards`, `artifacts`, `paper_type`, `research_line`) with no existing field altered. `research_line` is an editorial grouping made by this study, not a label used by the authors.

## Checks performed during preparation

The original local study checked all 158 downloads and their separate vault copies against manifest hashes: 316 comparisons without mismatches. That historical source-integrity check does not establish the availability or content of today's remote URLs. Bundled hashes allow readers to identify the studied versions.

Both skill entrypoints passed the skill-creator structural validator. Before the portable export, an independent agent followed the installed skills on five synthetic tasks; the coordinating assistant inspected the actual responses:

1. A proposal with no experiments: a future-tense abstract and proposed experiments without invented results.
2. A manuscript excerpt: evidence-located concerns about overclaims, percentages, success-conditioned timing, tuning, latency, and uncertainty.
3. Narrow copyediting and a dataset abstract: preservation of requested scope, genre-appropriate expectations, and no claims about unseen full-paper details.
4. A held-out numerical example: correct percentage-point/relative-change calculations and conditional-time interpretation.
5. An unknown source key: an actual failed lookup, followed by a request for a valid identifier without fabricated citations.

The initial review example overlapped with an arithmetic example in the instructions; the additional numerical task used different values. These were observed behaviors, not a blinded comparison, an exhaustive reliability test, or validation against a professor's private reviews. The portable export has additional reproducible tests in `tests/`.

## Packaging changes

The export preserves the research guidance while removing machine-specific source and Obsidian paths. It adds public page URLs, citation metadata, and source hashes. Lookup works without local PDFs; an optional collection root supports availability and version checks. No confidential drafts, source PDFs, extracted full texts, vault configuration, or unrelated personal skills are published.

The most important safeguard remains checking the original evidence before making a strong scientific claim. The skills' source examples are not evidence for a user's new method.
