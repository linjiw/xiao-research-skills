#!/usr/bin/env python3
"""Search bundled study paraphrases; does not fetch or execute source content."""
import argparse
import collections
import hashlib
import json
import sys
from pathlib import Path

BROWSE = ('line', 'venue', 'type', 'year', 'topic')
LIST_FIELDS = ('key', 'year', 'venue', 'paper_type', 'research_line', 'title')


def matches(record, args):
    if args.line and args.line.casefold() not in record.get('research_line', '').casefold():
        return False
    if args.venue and args.venue.casefold() != record.get('venue', '').casefold():
        return False
    if args.type and args.type.casefold() not in record.get('paper_type', '').casefold():
        return False
    if args.year and str(args.year) != str(record.get('year')):
        return False
    if args.topic and not any(args.topic.casefold() in t.casefold() for t in record.get('topics', ())):
        return False
    return True


def summarize(rows):
    for field in ('year', 'venue', 'venue_kind', 'paper_type', 'research_line', 'topics'):
        counts = collections.Counter(
            value for r in rows
            for value in (r.get('topics', ()) if field == 'topics' else [str(r.get(field, 'unrecorded'))]))
        order = sorted(counts.items()) if field == 'year' else counts.most_common()
        print(f'{field} ({len(counts)} values, {len(rows)} records)')
        for name, count in order:
            print(f'  {count:4d}  {name}')
        print()


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group()
    group.add_argument('--key')
    group.add_argument('--query', default='')
    parser.add_argument('--line', help='filter by research_line substring')
    parser.add_argument('--venue', help='filter by exact venue tag, e.g. RA-L, IROS, RSS')
    parser.add_argument('--type', help='filter by paper_type substring')
    parser.add_argument('--year')
    parser.add_argument('--topic', help='filter by topic substring')
    parser.add_argument('--limit', type=int, default=5)
    parser.add_argument('--all', action='store_true', help='return every match instead of --limit')
    parser.add_argument('--list', action='store_true', help='one compact line per record instead of JSON')
    parser.add_argument('--stats', action='store_true', help='summarize the ledger by year, venue, type, research line, and topic')
    parser.add_argument('--pdf-root', type=Path, help='Optional local collection root matching pdf_relative_path; never downloads files')
    args = parser.parse_args()
    if args.limit < 1:
        parser.error('--limit must be positive')
    used = [name for name in BROWSE if getattr(args, name)]
    if args.key and used:
        parser.error('--key selects one record; drop ' + ', '.join('--'+name for name in used))
    if args.stats and (args.key or args.query):
        parser.error('--stats summarizes the browse facets; drop --key and --query')
    source = Path(__file__).resolve().parents[1] / 'references/evidence-ledger.json'
    if not source.is_file():
        parser.error('Bundled evidence ledger is unavailable; do not invent source evidence.')
    rows = json.loads(source.read_text())
    if args.stats:
        summarize([p for p in rows if matches(p, args)])
        return 0
    if args.key:
        selected = [p for p in rows if p['key'] == args.key]
        if not selected:
            print('Unknown paper key: ' + args.key, file=sys.stderr)
            return 2
    else:
        words = args.query.casefold().split()
        scored = []
        for p in rows:
            if not matches(p, args):
                continue
            hay = json.dumps({k:v for k,v in p.items() if k not in ('local_pdf', 'obsidian_note', 'source_url', 'source_sha256', 'pdf_relative_path')}, ensure_ascii=False).casefold()
            if all(w in hay for w in words):
                scored.append((sum(hay.count(w) for w in words), p))
        ranked = [p for _, p in sorted(scored, key=lambda x: (-x[0], x[1]['id']))]
        selected = ranked if args.all else ranked[:args.limit]
        tried = [f'--{name} {getattr(args, name)!r}' for name in used]
        if args.query:
            tried.append(f'--query {args.query!r}')
        if not ranked and tried:
            hint = ('--venue takes an exact tag; run --stats for the valid facet values.' if used
                    else '--query needs every word present literally.')
            print(f'0 records match {", ".join(tried)}. {hint}', file=sys.stderr)
        elif len(ranked) > len(selected):
            print(f'{len(ranked)} records match; showing {len(selected)}. Use --limit N or --all for the rest.', file=sys.stderr)
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
    if args.list:
        for p in selected:
            print('\t'.join(str(p.get(field, '')) for field in LIST_FIELDS))
    else:
        print(json.dumps(selected, ensure_ascii=False, indent=2))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
