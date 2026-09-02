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


def records(skill):
    return json.loads((skill/'references/evidence-ledger.json').read_text())


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
        for relative in ('references/evidence-ledger.json', 'scripts/lookup_evidence.py'):
            self.assertEqual((SKILLS[0]/relative).read_bytes(), (SKILLS[1]/relative).read_bytes())

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

    def test_distribution_contains_no_private_paths_or_pdfs(self):
        private_path = re.compile(r'/(?:Users|home)/[^/\s]+/')
        token_like = re.compile(r'(?:gh[pousr]_[A-Za-z0-9]{30,}|github_pat_[A-Za-z0-9_]{30,}|-----BEGIN [A-Z ]*PRIVATE KEY-----)')
        for path in ROOT.rglob('*'):
            if not path.is_file() or any(part in ('.git', '__pycache__', '.venv') for part in path.relative_to(ROOT).parts):
                continue
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
