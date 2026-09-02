# Section-specific writing and teaching moves

These are adaptable argument structures, not mandatory paragraph counts or an author's signature phrasing.

- **Title:** concrete problem/capability plus distinguishing mechanism. An acronym is optional.
- **Abstract:** context and precise limitation; mechanism; evaluation setting; strongest bounded result; implication within scope. With no results, write a proposal abstract or retain placeholders.
- **Introduction:** consequential mismatch between present capability and target setting; why alternatives leave the gap; testable contributions, not a component inventory.
- **Related work:** organize by assumptions and tradeoffs relevant to the gap. Credit what alternatives solve. Different evaluation settings do not prove another method incapable.
- **Method:** inputs/outputs, objective, assumptions, algorithm, training/deployment information, interfaces, and retained safety/recovery mechanisms. Connect each major design choice to the bottleneck.
- **Experiments:** organize around questions. Each major claim needs a test, and each test needs an interpretive purpose. Include settings, resource accounting, failures, and variability.
- **Results:** observation and setting first, interpretation second. Do not turn an association or one ablation into a unique causal explanation. Report where the method loses.
- **Discussion:** failed assumptions, affected settings, and the next discriminating test. Separate proposed explanations from demonstrated mechanisms.
- **Conclusion:** return to what was established; no new unsupported claims.
- **Rebuttal:** represent the concern accurately, answer with evidence and location, concede genuine gaps, specify revisions; never invent experiments or completed changes.

## Synthetic miniature example — not source-paper text

Weak: “Our intelligent planner guarantees safe and general navigation with superior performance.”

Evidence-aware: “In the tested indoor layouts, the adaptive policy completed 18 of 20 routes, compared with 14 of 20 for the fixed-parameter planner. Both used the same collision-checking layer. These trials support improved completion in this setting, not a general safety guarantee.”

These numbers are invented **only for this teaching example**. Never reuse them as the user's results.

## Paragraph revision

Identify its argumentative job; preserve technical facts; replace generic praise with mechanism or measurement; remove repetition; add the minimal evidence qualification. Return the revised paragraph and explain only consequential changes. In language-polish-only mode, flag technical concerns separately instead of silently altering the claim.

## Learning loop

Explain a source as problem → mechanism → evidence → limitation. Ask the learner to reconstruct that argument from memory, propose a counterexample, and write a paragraph for their own project. Evaluate reasoning and evidence, not similarity of vocabulary.

## Figures and captions

Choose a figure's scientific job before styling it: expose the bottleneck, explain the information flow, distinguish mechanisms, or summarize a bounded result. An architecture figure should distinguish new/retained modules and training/deployment inputs. An experimental figure should identify the comparator, units, population, repeats, and uncertainty; a robot photo is context, not a statistical comparison. A caption should let the reader state what the figure supports and what it does not. Match visual hierarchy to the argument rather than filling a page with impressive examples. For exact source-figure teaching, open the original PDF page instead of relying on OCR or a generic description.
