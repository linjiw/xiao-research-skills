# Retrieve and interpret corpus evidence

Use this reference when looking up a corpus precedent or verifying a source claim. The lookup helper is offline and does not download or upload files.

```sh
python3 <skill-dir>/scripts/lookup_evidence.py --key appld_ral
python3 <skill-dir>/scripts/lookup_evidence.py --query "representation" --limit 5
```

Browse with `--line`, `--venue`, `--type`, `--year`, or `--topic`; use `--list` for compact rows, `--all` for complete matches, and `--stats` for distributions. Query words are literal, case-insensitive terms that must all occur; this is lexical lookup, not semantic search. A zero-result search does not establish that the corpus lacks a topic. Check truncation. An unknown key or empty search does not authorize invented evidence.

The ledger contains 137 historical argument-level main-text records. The separate `craft_reread` field records the 2026-09-09 selected-section pass, including visual reading of the scanned article. It is not a new full-text or technical audit. Consult per-paper scope fields. A prior record is not proof that the current assistant has read the original; its lesson is an analyst's synthesis, not an author-endorsed rule.

No PDFs are bundled. Retrieve originals through `source_url`, or use `--pdf-root <collection-root>` with an existing collection matching `pdf_relative_path`. Check `local_pdf_sha256_matches` before relying on stored page anchors; a mismatch calls for version and page verification. Physical PDF pages can differ from printed labels.

Open the original for quotations, equations, figures, or numerical claims. If it is inaccessible, state the limitation and attribute any summary to the ledger instead of claiming fresh verification. Source examples inform questions; they do not validate the user's unpublished method.
