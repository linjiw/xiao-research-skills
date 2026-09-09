# Xiao-inspired research writing and review skills

Two reusable Codex skills for developing and reviewing original robotics research, grounded in an AI-assisted study of 137 publications coauthored by Xuesu Xiao.

This is an independent educational project. It is not affiliated with or endorsed by Xuesu Xiao, RobotiXX, or George Mason University, and does not represent anyone's private reviewing preferences. Learn research reasoning and evidence-aware writing—not imitation of an author's prose.

## The skills

| Skill | Use it for |
| --- | --- |
| [xiao-paper-writing](skills/xiao-paper-writing/SKILL.md) | Research questions, competing explanations, discriminating experiments, coherent paper arguments, section drafting, revision, and source-based teaching |
| [xiao-paper-review](skills/xiao-paper-review/SKILL.md) | Scientific contribution and argument review, evidence checks, numerical interpretation, and prioritized repairs |

The recurring workflow is: identify a consequential question → reason about competing explanations → design an informative test → connect the result to a clear paper argument. Dataset, theory, hardware, human-study, survey, and algorithm papers have different evidence obligations.

### What each skill carries

| Reference | Answers |
| --- | --- |
| `argument-workshop.md` (writing) | How to turn a vague idea into a testable research question and a connected manuscript; includes a hypothetical worked example |
| `research-design.md` (writing) | Which experiment distinguishes explanations, how to choose units and comparators, and what each evidence type supports |
| `drafting.md` (writing) | How sections and paragraphs advance the same argument, from title through conclusion |
| `wording.md` (both) | How to state precise claims, comparisons, uncertainty, scope, and missing evidence |
| `research-programs.md` (writing) | How to choose a worthwhile follow-up and learn from negative or mixed results |
| `genre-guide.md` (both) | What evidence the actual contribution needs |
| `source-patterns.md` (both) | Source observations, transferable practices, and their boundaries |
| `review-protocol.md` and `reviewer-question-bank.md` (review) | How to assess importance, logic, evidence, and the smallest sufficient repair |

The [2026-09-09 rebuild](docs/REBUILD-2026-09-09.md) adds a separate, bounded rereading record for every paper and corrects overly rigid writing and statistical rules. It does not require a fixed contribution count, paragraph order, trial count, or evidence ladder.

## Install

In Codex, ask the built-in installer:

```text
$skill-installer Install both skills from linjiw/xiao-research-skills:
skills/xiao-paper-writing and skills/xiao-paper-review.
```

Install only the skill you need if preferred. If one with the same name is already installed, compare versions before replacing it. The package uses standard skill folders; it is not a marketplace plugin. See the [official skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery and installation behavior. Restart Codex if a newly installed skill does not appear.

The optional lookup helper requires Python 3.9 or newer and only the standard library. No API key, Obsidian installation, or PDF collection is required.

## Use

```text
$xiao-paper-writing My research idea is [idea], and my constraints are [details].
Help me formulate a falsifiable claim and three discriminating experiments.
Separate observations, hypotheses, and missing evidence.
```

```text
$xiao-paper-writing Revise this abstract using only my actual results.
Preserve facts and numbers; mark missing evidence instead of inventing it: [abstract].
```

```text
$xiao-paper-review Review [local draft path]. State what you read, identify the
strongest contribution, and give up to five prioritized concerns with locations,
consequences, and the smallest sufficient repairs. Do not edit the file.
```

```text
$xiao-paper-writing Teach me the research reasoning in appld_ral.
Verify the source pages, then give me an exercise for my own project.
```

```text
$xiao-paper-writing Audit this paragraph sentence by sentence: for each claim, name the
type of evidence it needs, the scope or uncertainty it leaves unclear, and the smallest
accurate rewrite: [paragraph].
```

```text
$xiao-paper-writing My line so far is [papers]. What does the next paper have to add to earn
its place, and which limitation has the most claim leverage?
```

For a separate review agent, explicitly ask for one. Invoking the reviewer alone does not authorize delegation, external manuscript uploads, submission, or contact with an author. See the [handoff template](skills/xiao-paper-review/references/reviewer-handoff.md).

## Evidence and coverage

Each skill bundles the same 137-record evidence ledger, containing brief analytical paraphrases, full citation metadata, public source URLs, physical PDF page anchors, study scope, limitations, and the SHA-256 hash of the studied source version. The snapshot is dated September 2, 2026 and comes from [Xuesu Xiao's publication list](https://people.cs.gmu.edu/~xiao/#publications).

Coverage is 135 main-text records plus 2 visual-main-text records. This means an argument-level pass of all 137 primary papers, not independent proof checking, experimental reproduction, exhaustive figure/statistical auditing, or complete supplement/appendix reading. The primary PDFs total 1,460 physical pages, including material outside the close-reading scope. See [provenance and validation](docs/PROVENANCE.md).

On 2026-09-03 the corpus was re-downloaded and all 137 files matched their recorded SHA-256, then read again in 29 thematic batches plus 9 cross-cutting lenses (136 from extracted full text; the scanned Chinese-language article was handled visually, as in the first pass) to rebuild the reference files from the whole corpus rather than a starter set, and every page citation in them was verified against the PDF. Method and limits: [the corpus study](docs/CORPUS-STUDY.md). Records are also browsable by facet: `venue`, `venue_kind`, `paper_type`, and `research_line` (an editorial grouping made by this study, not the authors' own label).

The latest pass on **2026-09-09** revisited selected opening, closing, and evidence passages across all 137 primary papers, including visual reading of the scanned article. All primary local files matched their recorded hashes. This pass is **not a new full-text or technical audit**. Its date, pages, scope, and analytical lesson are recorded separately in each paper's `craft_reread` field; the earlier main-text records are preserved. Details: [rebuild and actual coverage](docs/REBUILD-2026-09-09.md).

**No source PDFs, extracted full texts, Obsidian vault, private drafts, or personal filesystem paths are distributed.** Follow the source links and obtain originals from their authorized hosts. Linked files can change; page references and findings must be checked against the version actually used.

## Search the evidence locally

From this repository:

```sh
python3 skills/xiao-paper-writing/scripts/lookup_evidence.py --key appld_ral
python3 skills/xiao-paper-review/scripts/lookup_evidence.py --query "baseline" --limit 3
python3 skills/xiao-paper-writing/scripts/lookup_evidence.py --line APPL --all --list
python3 skills/xiao-paper-writing/scripts/lookup_evidence.py --type challenge-report --all --list
python3 skills/xiao-paper-writing/scripts/lookup_evidence.py --stats
```

`--line`, `--venue`, `--type`, `--year`, and `--topic` narrow the ledger; `--list` prints one line per record, `--all` defeats the default cap, and `--stats` summarizes the corpus. A truncated result says so on stderr rather than passing itself off as complete.

Lookup is offline. It returns source links but does not download files or send data anywhere. Unknown keys return an error instead of invented evidence. The reading records are prior analyses, not a claim that a fresh assistant has read the originals.

If you separately maintain the original collection layout, provide its root:

```sh
python3 skills/xiao-paper-review/scripts/lookup_evidence.py --key rtw --pdf-root ./local-papers
```

Each record's `pdf_relative_path` identifies the expected location. The helper reports availability and whether the file matches the studied hash. A mismatch is a reason to check versions, not evidence that the new file is wrong.

## Test

```sh
python3 -m unittest discover -s tests -v
```

Tests check the ledger, source provenance, portable retrieval, input errors, reference links, and accidental private-path/PDF inclusion. They do not prove research correctness or acceptance prospects. [Scenario walkthroughs](docs/SCENARIO-WALKTHROUGHS.md) provide transparent self-checks, not independent behavioral validation.

## Reuse and attribution

Third-party publications remain the work of their respective authors and rights holders; they are linked, not redistributed. This repository currently does not specify a reuse license for its own materials. Public availability should not be mistaken for an author endorsement or a grant of rights in the source papers.
