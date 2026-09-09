"""Offline checks for the portable skill package; no external services required."""
import hashlib
import json
import re
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILLS = tuple(ROOT/'skills'/name for name in ('xiao-paper-writing', 'xiao-paper-review'))
SHARED = ('references/evidence-ledger.json', 'references/genre-guide.md',
          'references/source-patterns.md', 'references/wording.md', 'scripts/lookup_evidence.py')
PAPER_TYPES = frozenset((
    'algorithm', 'dataset-benchmark', 'simulator', 'theory-planning', 'human-study',
    'hardware-field', 'survey-position', 'challenge-report', 'tech-report', 'workshop-abstract',
))
# `key` p4 / `key` pp1–2,5 / (key p4) / (key pp3-4) — the citation forms the references use.
# A comma continues a page list only when unspaced, so "`key` p6, 90 physical runs" stays one page.
CITATION = re.compile(r'[`(]([a-z0-9][a-z0-9_-]{1,40})[`]?\s*(?:\))?[ ,]*pp?\.?\s*([0-9]+(?:[-–][0-9]+)?(?:,[0-9]+(?:[-–][0-9]+)?)*)')


def records(skill):
    return json.loads((skill/'references/evidence-ledger.json').read_text())


def distributed_files():
    """Files this repository actually ships.

    Ignored working-tree material—an optional `local-papers/` collection above all—is a
    reader's own copy of third-party PDFs, not part of the distribution, so it is out of
    scope for the no-PDF and no-private-path guarantees.
    """
    listing = subprocess.run(['git', '-C', str(ROOT), 'ls-files', '-z', '--cached', '--others', '--exclude-standard'],
                             capture_output=True, text=True, check=False)
    if listing.returncode == 0:
        candidates = (ROOT/name for name in listing.stdout.split('\0') if name)
    else:  # exported without version control: fall back to walking the tree
        candidates = (path for path in ROOT.rglob('*')
                      if not any(part in ('.git', '__pycache__', '.venv', 'local-papers') for part in path.relative_to(ROOT).parts))
    return [path for path in candidates if path.is_file() or path.is_symlink()]


def lookup(skill, *arguments):
    return subprocess.run(
        [sys.executable, str(skill/'scripts/lookup_evidence.py'), *arguments],
        capture_output=True, text=True, check=False,
    )


class PackageTests(unittest.TestCase):
    def test_corpus_and_provenance(self):
        for skill in SKILLS:
            with self.subTest(skill=skill.name):
                rows = records(skill)
                self.assertEqual(len(rows), 137)
                self.assertEqual(len({p['key'] for p in rows}), 137)
                self.assertEqual(sum(p['physical_pages'] for p in rows), 1460)
                self.assertEqual(sum(p['coverage_class'] == 'main-text-read' for p in rows), 135)
                self.assertEqual(sum(p['coverage_class'] == 'visual-main-text' for p in rows), 2)
                for p in rows:
                    self.assertNotIn('local_pdf', p)
                    self.assertNotIn('obsidian_note', p)
                    self.assertTrue(p['citation'])
                    self.assertEqual(urlsplit(p['source_url']).scheme, 'https')
                    self.assertRegex(p['source_sha256'], r'^[a-f0-9]{64}$')
                    relative = Path(p['pdf_relative_path'])
                    self.assertFalse(relative.is_absolute())
                    self.assertNotIn('..', relative.parts)
                    inspected = p['pages_read']
                    if isinstance(inspected, str):
                        # Historical records preserve human-readable ranges and visual-check notes.
                        inspected = [page for start, end in re.findall(r'(\d+)(?:\s*[–-]\s*(\d+))?', inspected)
                                     for page in range(int(start), int(end or start)+1)]
                    self.assertTrue(inspected)
                    self.assertTrue(all(1 <= n <= p['physical_pages'] for n in inspected))
                    for anchor in p['evidence_pages']:
                        self.assertIn(anchor['page'], inspected)
                        self.assertLessEqual(anchor['page'], p['physical_pages'])
                        self.assertEqual(anchor['url'], p['source_url'].split('#', 1)[0]+'#page='+str(anchor['page']))

    def test_both_skills_bundle_identical_evidence_and_helpers(self):
        for relative in SHARED:
            self.assertEqual((SKILLS[0]/relative).read_bytes(), (SKILLS[1]/relative).read_bytes())

    def test_craft_reread_preserves_separate_bounded_provenance(self):
        for skill in SKILLS:
            rows = records(skill)
            for row in rows:
                with self.subTest(skill=skill.name, key=row['key']):
                    reread = row['craft_reread']
                    self.assertEqual(reread['date'], '2026-09-09')
                    self.assertLess(row['analysis_date'], reread['date'])
                    self.assertTrue(reread['scope'])
                    self.assertTrue(reread['lesson'])
                    self.assertTrue(reread['interpretation'])
                    self.assertIs(reread['source_sha256_verified'], True)
                    pages = reread['physical_pages_consulted']
                    self.assertTrue(pages)
                    self.assertEqual(pages, sorted(set(pages)))
                    self.assertTrue(all(isinstance(n, int) and 1 <= n <= row['physical_pages']
                                        for n in pages))
            # Text extraction once introduced false page separators in this PDF.
            mtc = next(row for row in rows if row['key'] == 'mtc')
            self.assertEqual(mtc['physical_pages'], 9)
            self.assertIn(7, mtc['craft_reread']['physical_pages_consulted'])
            retrieved = lookup(skill, '--key', 'car_jmee')
            self.assertEqual(retrieved.returncode, 0, retrieved.stderr)
            self.assertEqual(json.loads(retrieved.stdout)[0]['craft_reread'],
                             next(row for row in rows if row['key'] == 'car_jmee')['craft_reread'])

    def test_skill_entrypoints_and_references(self):
        for skill in SKILLS:
            body = (skill/'SKILL.md').read_text()
            self.assertTrue(body.startswith('---\n'))
            self.assertIn('name: '+skill.name+'\n', body)
            self.assertIn('\ndescription: ', body)
            self.assertIn('$'+skill.name, (skill/'agents/openai.yaml').read_text())
            for relative in re.findall(r'`((?:references|scripts)/[^` ]+)`', body):
                self.assertTrue((skill/relative).is_file(), relative)

    def test_exact_retrieval_without_pdfs(self):
        for skill in SKILLS:
            for key in ('appld_ral', 'rtw', 'nasa', 'car_jmee', 'musohu'):
                with self.subTest(skill=skill.name, key=key):
                    result = lookup(skill, '--key', key)
                    self.assertEqual(result.returncode, 0, result.stderr)
                    row, = json.loads(result.stdout)
                    self.assertEqual(row['key'], key)
                    self.assertFalse(row['local_pdf_available'])
                    self.assertNotIn('local_pdf', row)

    def test_search_is_case_insensitive_and_limited(self):
        for skill in SKILLS:
            first = lookup(skill, '--query', 'BASELINE', '--limit', '2')
            second = lookup(skill, '--query', 'baseline', '--limit', '2')
            self.assertEqual(first.returncode, 0, first.stderr)
            self.assertEqual(first.stdout, second.stdout)
            self.assertEqual(len(json.loads(first.stdout)), 2)
            empty = lookup(skill, '--query', 'no-such-query-7f28b9')
            self.assertEqual(empty.returncode, 0)
            self.assertEqual(json.loads(empty.stdout), [])

    def test_invalid_inputs_report_errors(self):
        for skill in SKILLS:
            for arguments in (
                ('--key', 'no-such-paper-7f28b9'), ('--limit', '0'),
                ('--limit', '-1'), ('--limit', 'not-an-integer'),
                ('--key', 'rtw', '--query', 'risk'),
            ):
                with self.subTest(skill=skill.name, arguments=arguments):
                    result = lookup(skill, *arguments)
                    self.assertEqual(result.returncode, 2)
                    self.assertTrue(result.stderr.strip())
                    self.assertEqual(result.stdout, '')

    def test_optional_local_collection_detects_missing_and_wrong_version(self):
        row = next(p for p in records(SKILLS[0]) if p['key'] == 'rtw')
        with tempfile.TemporaryDirectory(prefix='xiao-skill-test-') as directory:
            root = Path(directory)
            for skill in SKILLS:
                result = lookup(skill, '--key', 'rtw', '--pdf-root', str(root))
                self.assertEqual(result.returncode, 0, result.stderr)
                missing, = json.loads(result.stdout)
                self.assertFalse(missing['local_pdf_available'])
                self.assertIsNone(missing['local_pdf_sha256_matches'])
            target = root/row['pdf_relative_path']
            target.parent.mkdir(parents=True)
            target.write_bytes(b'Synthetic different-version fixture; not a source paper.')
            for skill in SKILLS:
                result = lookup(skill, '--key', 'rtw', '--pdf-root', str(root))
                self.assertEqual(result.returncode, 0, result.stderr)
                found, = json.loads(result.stdout)
                self.assertTrue(found['local_pdf_available'])
                self.assertFalse(found['local_pdf_sha256_matches'])

    def test_local_hash_match_and_path_escape(self):
        with tempfile.TemporaryDirectory(prefix='xiao-skill-fixture-') as directory:
            fixture = Path(directory)
            script = fixture/'skill/scripts/lookup_evidence.py'
            script.parent.mkdir(parents=True)
            script.write_bytes((SKILLS[0]/'scripts/lookup_evidence.py').read_bytes())
            ledger = fixture/'skill/references/evidence-ledger.json'
            ledger.parent.mkdir()
            pdf_root = fixture/'papers'
            pdf_root.mkdir()
            content = b'Synthetic hash fixture, not copyrighted paper content.'
            (pdf_root/'example.pdf').write_bytes(content)
            row = dict(records(SKILLS[0])[0])
            row['pdf_relative_path'] = 'example.pdf'
            row['source_sha256'] = hashlib.sha256(content).hexdigest()
            ledger.write_text(json.dumps([row]))
            result = lookup(fixture/'skill', '--key', row['key'], '--pdf-root', str(pdf_root))
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(json.loads(result.stdout)[0]['local_pdf_sha256_matches'])
            row['pdf_relative_path'] = '../outside.pdf'
            ledger.write_text(json.dumps([row]))
            result = lookup(fixture/'skill', '--key', row['key'], '--pdf-root', str(pdf_root))
            self.assertEqual(result.returncode, 2)
            self.assertIn('must remain within', result.stderr)

    def test_ledger_carries_browsable_metadata(self):
        for skill in SKILLS:
            rows = records(skill)
            venues = {p['venue'] for p in rows}
            lines = {p['research_line'] for p in rows}
            with self.subTest(skill=skill.name):
                self.assertGreater(len(venues), 20)
                self.assertGreater(len(lines), 10)
                self.assertIn('standalone', lines)
                for p in rows:
                    self.assertIn(p['paper_type'], PAPER_TYPES, p['key'])
                    self.assertIn(p['venue_kind'], ('journal', 'magazine', 'conference', 'workshop', 'report', 'preprint'), p['key'])
                    self.assertTrue(p['venue'] and p['venue_full'], p['key'])
                    self.assertIsInstance(p['awards'], list)
                    self.assertIsInstance(p['artifacts'], list)
                    self.assertTrue(set(p['artifacts']) <= {'Video', 'Website', 'Code', 'Dataset', 'Poster', 'Presentation'}, p['key'])

    def test_browse_filters_and_summaries(self):
        for skill in SKILLS:
            with self.subTest(skill=skill.name):
                listed = lookup(skill, '--venue', 'RSS', '--all', '--list')
                self.assertEqual(listed.returncode, 0, listed.stderr)
                self.assertEqual(len(listed.stdout.strip().splitlines()), 1)
                self.assertIn('verti_bench', listed.stdout)
                filtered = lookup(skill, '--line', 'BARN', '--all')
                self.assertEqual(filtered.returncode, 0, filtered.stderr)
                self.assertTrue(all('BARN' in p['research_line'] for p in json.loads(filtered.stdout)))
                narrowed = lookup(skill, '--type', 'challenge-report', '--query', 'competition', '--all')
                self.assertEqual(narrowed.returncode, 0, narrowed.stderr)
                self.assertTrue(json.loads(narrowed.stdout))
                summary = lookup(skill, '--stats')
                self.assertEqual(summary.returncode, 0, summary.stderr)
                self.assertIn('research_line', summary.stdout)
                capped = lookup(skill, '--venue', 'IROS', '--limit', '3')
                self.assertEqual(len(json.loads(capped.stdout)), 3)
                self.assertIn('match', capped.stderr)  # truncation is announced, never silent
                conflict = lookup(skill, '--key', 'rtw', '--venue', 'IROS')
                self.assertEqual(conflict.returncode, 2)

    def test_reference_citations_point_at_real_pages(self):
        for skill in SKILLS:
            pages = {p['key']: p['physical_pages'] for p in records(skill)}
            for path in sorted((skill/'references').glob('*.md')):
                body = path.read_text()
                cited = CITATION.findall(body)
                with self.subTest(reference=f'{skill.name}/{path.name}'):
                    for key, span in cited:
                        self.assertIn(key, pages, f'{path.name}: unknown paper key {key}')
                        for number in re.findall(r'\d+', span):
                            self.assertLessEqual(int(number), pages[key], f'{path.name}: {key} p{number} exceeds {pages[key]} pages')
                    # A file that cites nothing has stopped being evidence-grounded.
                    if path.name in ('source-patterns.md', 'wording.md'):
                        self.assertTrue(cited, path.name)

    def test_ignored_working_tree_is_out_of_distribution_scope(self):
        shipped = {path.relative_to(ROOT).parts[0] for path in distributed_files()}
        self.assertIn('skills', shipped)
        self.assertNotIn('local-papers', shipped)
        self.assertIn('local-papers/', (ROOT/'.gitignore').read_text())

    def test_distribution_contains_no_private_paths_or_pdfs(self):
        private_path = re.compile(r'/(?:Users|home)/[^/\s]+/')
        token_like = re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)')
        for path in distributed_files():
            with self.subTest(path=str(path.relative_to(ROOT))):
                self.assertFalse(path.is_symlink())
                self.assertNotEqual(path.suffix.lower(), '.pdf')
                raw = path.read_bytes()
                self.assertFalse(raw.startswith(b'%PDF-'))
                body = raw.decode('utf-8')
                self.assertIsNone(private_path.search(body))
                self.assertIsNone(token_like.search(body))
                self.assertNotIn('[['+'Projects/', body)


if __name__ == '__main__':
    unittest.main()
