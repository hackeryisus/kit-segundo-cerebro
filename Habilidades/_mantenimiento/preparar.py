"""Empaqueta una base limpia o las skills del kit. No instala ni borra archivos."""
import argparse
import datetime
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
    "Plantillas/politica-uso-ia-template.md", "Plantillas/formato.md",
    ".obsidian/snippets/lectura.css",
)
PLUGIN_IDS = ("settings-search", "recent-files-obsidian", "editing-toolbar", "iconic")
FACTORY = {
    "PERFIL.md": "38c452f728607d4e12499095de5f0c006ccd4d1d5745677d5d5ee93746c0de96",
    "MEMORIA.md": "8109efd453041f05a5644936ccbde4966e0f95a9bce0e19258766d5fd6e11cfa",
    "Proyectos/INDEX.md": "20c926b3455e4a70a3b6864a2a419ac1ac73ac906620f11ef87b37238e65b6f2",
}


def read_file(root, name):
    path = root / name
    if path.is_symlink() or not path.resolve().is_relative_to(root.resolve()):
        raise ValueError(f"Ruta fuera de la base o enlace simbólico: {name}")
    return path.read_bytes()


DESCRIPTION_MAX = 200  # límite de Claude al subir una skill (support.claude.com, 2026-07-22)


def check_description(skill_md, name):
    # Una línea entre comillas simples; así se mide igual que la cuenta la app.
    for line in skill_md.decode().split("---")[1].splitlines():
        if line.startswith("description:"):
            value = line[len("description:"):].strip()
            if not (value.startswith("'") and value.endswith("'")):
                raise ValueError(f"{name}: description en una sola línea entre comillas simples")
            if len(value[1:-1]) > DESCRIPTION_MAX:
                raise ValueError(f"{name}: description de {len(value) - 2} caracteres; máximo {DESCRIPTION_MAX}")
            return
    raise ValueError(f"{name}: falta description")


def skill_files(root, name):
    folder = root / "Habilidades" / name
    if not (folder / "SKILL.md").is_file():
        raise ValueError(f"Falta SKILL.md: {name}")
    # Solo instrucciones y recursos mantenidos en Git, nunca archivos locales.
    tracked = subprocess.check_output(
        ["git", "-C", str(root), "ls-files", "-z", "--", str(folder.relative_to(root))]
    ).decode().split("\0")
    files = {p: read_file(root, p) for p in tracked if p}
    check_description(files[f"Habilidades/{name}/SKILL.md"], name)
    return files


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
    # Única excepción dentro de la base: Entregas/, ignorada por Git. Las fuentes
    # se leen por lista blanca, así que un ZIP previo nunca viaja en otro ZIP.
    if output.is_relative_to(root) and not output.is_relative_to(root / "Entregas"):
        raise ValueError("Elige una carpeta de salida en Entregas/ o fuera de la base del kit")
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
    parser.add_argument("salida", type=Path, nargs="?",
                        help="Carpeta nueva; por defecto Entregas/<fecha>/<kit|habilidades>")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    salida = args.salida or (root / "Entregas" / datetime.date.today().isoformat()
                             / ("kit" if args.modo == "kit" else "habilidades"))
    try:
        for result in build(root, salida, args.modo):
            print(result)
    except (ValueError, OSError, subprocess.CalledProcessError) as exc:
        parser.exit(1, f"No se preparó la entrega: {exc}\n")
