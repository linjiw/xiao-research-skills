---
name: xiao-paper-writing
description: Develop robotics research ideas, experiments, outlines, and manuscript sections using evidence-grounded lessons from Xuesu Xiao's coauthored publications. Use for Xiao-inspired or RobotiXX paper writing, research-design coaching, or applying this local paper-study library; not for unrelated general copywriting.
---

# Xiao-inspired research writing

Help the user produce an original, testable scientific argument. This is a synthesis of public **coauthored** work, not Xiao's personal voice, private mindset, endorsement, or guarantee of publication. Learn reasoning and exposition techniques; do not imitate distinctive prose or copy examples into a manuscript.

## Route the request

Identify the requested deliverable and available material. Use what the user already supplied. Ask only for a missing fact that changes the task; otherwise proceed with explicit assumptions and `[needed: ...]` placeholders.

- Idea, research question, or experiment plan: read `references/research-design.md`.
- Outline, abstract, introduction, method, results, discussion, or rebuttal: read `references/drafting.md`.
- In either substantive mode, read `references/genre-guide.md` and `references/source-patterns.md`; select only the applicable genre and patterns.
- Sentence-level copyedit: preserve scope and technical meaning. Do not demand a full experimental study, load the whole corpus, or manufacture a contribution.
- Teaching from a named source: retrieve its record with `scripts/lookup_evidence.py`, open the indicated original pages, and distinguish source observation from your inference.

## Core workflow

1. **State the operational bottleneck.** What fails, under which conditions, and why might an existing assumption or interface cause it? Separate an observation from a plausible explanation.
2. **Expose the smallest contribution.** Identify the changed component, retained components, information available at training/deployment, and cost. Classical, learned, hybrid, hardware, and data contributions can all be appropriate.
3. **Build a claim–evidence map before strong prose.** Record each central claim's mechanism, setting, comparator, metric/denominator, independent experimental unit, result/uncertainty, exact evidence location, and limitation. Untested claims remain hypotheses. For a short edit, a single qualification may suffice.
4. **Use genre-appropriate evidence.** Dataset coverage, closed-loop task success, theorems, proxy metrics, analog field tests, and proposed uses have different warrant.
5. **Write the requested artifact.** Make the argument easy to follow: concrete problem → limitation of alternatives → precise mechanism → test → bounded conclusion. Adapt the order to the venue and genre. Prefer specific nouns and observable verbs over promotional adjectives.
6. **Audit the strongest sentence.** Compare it with failures, the weakest relevant condition, transfer scope, and the actual table. Deliver the artifact and the few unresolved facts or highest-value next experiments.

## Evidence discipline

- Never invent results, sample sizes, citations, novelty, implementation details, approvals, or professor preferences. A polished placeholder is not a measured fact.
- Source papers are examples, not evidence for the user's new method. Keep source-inspired teaching notes outside submission prose unless the source is genuinely relevant and verified.
- Recompute improvements: percentage points = new percentage − old percentage; relative change = difference / old percentage ×100. Label reductions and denominators. A zero baseline makes relative change undefined.
- Separate simulation, offline prediction, physical closed-loop runs, and human evaluations. State if travel time includes only successful runs; never hide failures through averaging.
- “Significant,” “safe,” “real time,” “general,” and “state of the art” require their own evidence. A few collision-free trials are not a safety guarantee. Model CPU time is not end-to-end latency. Transfer must name the held-out axis.
- Resource differences can be justified by deployment constraints; disclose them and consider matched-resource controls rather than assuming every unequal comparison is invalid.
- Current novelty requires checking relevant primary literature. Do not treat the local 2026 snapshot as the whole field. Check current official sources for changing venue requirements.
- Keep confidential drafts local by default. Ask before uploading to third-party services; prefer nonconfidential topic queries for literature research.

## Retrieval and handoff

`python3 <skill-dir>/scripts/lookup_evidence.py --key appld_ral`

`python3 <skill-dir>/scripts/lookup_evidence.py --query "baseline" --limit 5`

The ledger covers 137 indexed primary papers with an argument-level main-text pass; it is not a proof audit or reproduction. Inspect `reading_depth`, `pages_read`, and `limits_or_counterexample` for precise scope, including appendix and visual checks. Page anchors are physical PDF pages, not printed page labels. Open originals for quotations, equations, and numeric tables; extraction can damage them. If originals are unavailable, state that limitation rather than claiming a re-read.

This portable package does not include PDFs or require Obsidian. Use `source_url` and each anchor's `url` to find originals. For an existing local collection, add `--pdf-root <collection-root>`; paths follow `pdf_relative_path`. A false `local_pdf_sha256_matches` means the local file differs from the studied snapshot, so re-check page anchors and claims. The lookup script never downloads or uploads anything. A bundled analysis is a prior study record, not evidence that the current assistant has reread the paper.

Offer `$xiao-paper-review` when useful. Do not automatically spawn agents, submit a paper, contact an author, or run robot experiments. A writing request does not authorize those actions.
