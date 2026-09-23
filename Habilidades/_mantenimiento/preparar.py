"""Empaqueta una base limpia o las skills del kit. No instala ni borra archivos."""
import argparse
import hashlib
from pathlib import Path
import subprocess
import zipfile

SKILLS = ("dossier-inicial", "grill-me", "mi-voz", "resumen-accionable",
          "revision-semanal", "session-handoff")
CORE = (
    "AGENTS.md", "CLAUDE.md", "README.md", "GUIA-DE-INICIO.html",
    "GUIA-DE-INICIO.pdf", "LICENSE", ".gitignore", "PERFIL.md", "MEMORIA.md",
    "Entrada/README.md", "Proyectos/INDEX.md", "Habilidades/arranque.md",
    "Habilidades/segunda-opinion.md",
    "Plantillas/project-index-template.md", "Plantillas/dossier-template.md",
    "Plantillas/politica-uso-ia-template.md",
)
PLUGIN_IDS = ("settings-search", "recent-files-obsidian", "editing-toolbar", "iconic")
FACTORY = {
    "PERFIL.md": "f96a2be9abe7b8323a193e257d254575fe2d752eac147db7e5006b7564a9a3c0",
    "MEMORIA.md": "11fee9944c51d8e8562209f098b37c6af4de2b49894db47763138524b95289e1",
    "Proyectos/INDEX.md": "20c926b3455e4a70a3b6864a2a419ac1ac73ac906620f11ef87b37238e65b6f2",
}


def read_file(root, name):
    path = root / name
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Ruta fuera de la base o enlace simbólico: {name}")
    return path.read_bytes()


def skill_files(root, name):
    folder = root / "Habilidades" / name
    if not (folder / "SKILL.md").is_file():
        raise ValueError(f"Falta SKILL.md: {name}")
    # Solo instrucciones y recursos mantenidos en Git, nunca archivos locales.
    tracked = subprocess.check_output(
        ["git", "-C", str(root), "ls-files", "-z", "--", str(folder.relative_to(root))]
    ).decode().split("\0")
    return {p: read_file(root, p) for p in tracked if p}


def kit_files(root):
    # Comparación con las plantillas de fábrica originales: un perfil parcialmente
    # rellenado puede seguir diciendo plantilla. No basta comprobar ese campo.
    for name, expected in FACTORY.items():
        if hashlib.sha256(read_file(root, name)).hexdigest() != expected:
            raise ValueError(f"{name} ya tiene cambios locales: usa la base limpia, no la demo")
    files = {name: read_file(root, name) for name in CORE}
    for name in SKILLS:
        files.update(skill_files(root, name))
    config = ("app.json", "appearance.json", "community-plugins.json",
              "core-plugins.json", "daily-notes.json")
    for name in config:
        path = f".obsidian/{name}"
        files[path] = read_file(root, path)
    for name in PLUGIN_IDS:
        for asset in ("main.js", "manifest.json", "styles.css"):
            path = f".obsidian/plugins/{name}/{asset}"
            if (root / path).is_file():
                files[path] = read_file(root, path)
    for name in ("theme.css", "manifest.json"):
        path = f".obsidian/themes/AnuPpuccin/{name}"
        files[path] = read_file(root, path)
    # Configuración estética de fábrica, no historiales de navegación.
    for name in ("iconic", "editing-toolbar"):
        path = f".obsidian/plugins/{name}/data.json"
        files[path] = subprocess.check_output(
            ["git", "-C", str(root), "show", f"634e107:{path}"]
        )
    for name in ("README.md", "preparar.py", "test_preparar.py"):
        path = f"Habilidades/_mantenimiento/{name}"
        files[path] = read_file(root, path)
    return files


def write_zip(destination, files, prefix):
    # 'x' evita sobrescribir una entrega previa; valida todo antes de escribir.
    if destination.exists():
        raise ValueError(f"Ya existe la entrega: {destination}")
    with zipfile.ZipFile(destination, "x", zipfile.ZIP_DEFLATED) as archive:
        for name, data in sorted(files.items()):
            archive.writestr(f"{prefix}/{name}", data)


def build(root, output, mode):
    root, output = Path(root).resolve(), Path(output).resolve()
    if output.is_relative_to(root):
        raise ValueError("Elige una carpeta de salida fuera de la base del kit")
    if output.exists():
        raise ValueError("La carpeta de salida debe ser nueva; no se sobrescribe")
    bundles = []
    if mode == "kit":
        bundles.append(("Kit-Segundo-Cerebro.zip", kit_files(root), "Mi Segundo Cerebro"))
    else:
        for skill in SKILLS:
            source = skill_files(root, skill)
            prefix = f"Habilidades/{skill}/"
            bundles.append((f"{skill}.zip", {p[len(prefix):]: b for p, b in source.items()}, skill))
    output.mkdir(parents=True, exist_ok=False)
    for name, files, prefix in bundles:
        write_zip(output / name, files, prefix)
    return [output / name for name, _, _ in bundles]


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("modo", choices=("kit", "skills"))
    parser.add_argument("salida", type=Path, help="Carpeta nueva fuera del kit")
    args = parser.parse_args()
    try:
        for result in build(Path(__file__).resolve().parents[2], args.salida, args.modo):
            print(result)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"No se preparó la entrega: {exc}\n")
