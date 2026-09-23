import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from preparar import build, read_file, write_zip, kit_files, check_description, SKILLS


class PackagingTests(unittest.TestCase):
    def test_no_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            dest = Path(tmp) / "kit.zip"
            write_zip(dest, {"CLAUDE.md": b"rules"}, "Mi Segundo Cerebro")
            original = dest.read_bytes()
            with self.assertRaises(ValueError):
                write_zip(dest, {}, "Mi Segundo Cerebro")
            self.assertEqual(dest.read_bytes(), original)

    def test_refuses_output_inside_source(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                build(tmp, Path(tmp) / "entrega", "kit")

    def test_allows_output_in_entregas(self):
        with tempfile.TemporaryDirectory() as tmp:
            # Pasa la comprobación de ruta y falla después por falta de fuentes.
            with self.assertRaises(OSError):
                build(tmp, Path(tmp) / "Entregas" / "hoy", "kit")

    def test_description_limit(self):
        ok = b"---\nname: x\ndescription: '" + b"a" * 200 + b"'\n---\n"
        check_description(ok, "x")
        for bad in (b"---\nname: x\ndescription: '" + b"a" * 201 + b"'\n---\n",
                    b"---\nname: x\ndescription: |\n  larga\n---\n"):
            with self.assertRaises(ValueError):
                check_description(bad, "x")

    def test_refuses_existing_output(self):
        with tempfile.TemporaryDirectory() as tmp:
            with self.assertRaises(ValueError):
                build(Path(tmp) / "source", tmp, "skills")

    def test_skill_zips_have_one_root_and_preserve_bytes(self):
        with tempfile.TemporaryDirectory() as tmp:
            def files(root, skill):
                return {f"Habilidades/{skill}/SKILL.md": b"test skill"}
            with patch("preparar.skill_files", side_effect=files):
                results = build(Path(tmp) / "source", Path(tmp) / "out", "skills")
            self.assertEqual(len(results), len(SKILLS))
            for skill, result in zip(SKILLS, results):
                with zipfile.ZipFile(result) as archive:
                    self.assertEqual(archive.namelist(), [f"{skill}/SKILL.md"])
                    self.assertEqual(archive.read(f"{skill}/SKILL.md"), b"test skill")

    def test_personalized_profile_rejected_even_if_state_is_template(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch("preparar.subprocess.check_output", return_value=b"template"), \
                 patch("preparar.read_file", return_value=b"template with personal data"):
                with self.assertRaises(ValueError):
                    kit_files(Path(tmp))

    def test_symlink_not_followed(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "source"
            root.mkdir()
            (root / "secret").symlink_to(Path(tmp) / "external")
            with self.assertRaises(ValueError):
                read_file(root, "secret")


if __name__ == "__main__":
    unittest.main()
