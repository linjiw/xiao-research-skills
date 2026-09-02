#!/usr/bin/env python3
"""Search bundled study paraphrases; does not fetch or execute source content."""
import argparse
import hashlib
import json
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--key')
    group.add_argument('--query', default='')
    parser.add_argument('--limit', type=int, default=5)
    parser.add_argument('--pdf-root', type=Path, help='Optional local collection root matching pdf_relative_path; never downloads files')
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    source = Path(__file__).resolve().parents[1] / 'references/evidence-ledger.json'
    if not source.is_file():
        parser.error('Bundled evidence ledger is unavailable; do not invent source evidence.')
    rows = json.loads(source.read_text())
    if args.key:
        selected = [p for p in rows if p['key'] == args.key]
        if not selected:
            print('Unknown paper key: ' + args.key, file=sys.stderr)
            return 2
    else:
        words = args.query.casefold().split()
        scored = []
        for p in rows:
            hay = json.dumps({k:v for k,v in p.items() if k not in ('local_pdf','obsidian_note','source_url','source_sha256','pdf_relative_path')}, ensure_ascii=False).casefold()
            if all(w in hay for w in words):
                scored.append((sum(hay.count(w) for w in words), p))
        selected = [p for _, p in sorted(scored, key=lambda x: (-x[0], x[1]['id']))[:args.limit]]
    for p in selected:
        p['local_pdf_available'] = False
        if args.pdf_root is not None:
            root = args.pdf_root.expanduser().resolve()
            relative = Path(p['pdf_relative_path'])
            candidate = (root/relative).resolve()
            if relative.is_absolute() or not candidate.is_relative_to(root):
                parser.error('Source PDF path must remain within --pdf-root')
            p['local_pdf'] = str(candidate)
            p['local_pdf_available'] = candidate.is_file()
            p['local_pdf_sha256_matches'] = (
                hashlib.sha256(candidate.read_bytes()).hexdigest() == p['source_sha256']
                if candidate.is_file() else None
            )
    print(json.dumps(selected, ensure_ascii=False, indent=2))
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
