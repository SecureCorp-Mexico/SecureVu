#!/usr/bin/env python3
"""
=================================================================
  SecureVu Smart Rebranding Tool v2 — SecureCorp Mexico
  Reemplaza Frigate → SecureVu SIN romper funcionalidad

  Uso:
    python3 smart_rebrand.py                  # aplica en directorio actual
    python3 smart_rebrand.py --path /repo     # ruta específica
    python3 smart_rebrand.py --dry-run        # solo analiza, sin cambios
    python3 smart_rebrand.py --verbose        # muestra cada archivo
=================================================================
"""

import os, re, sys, json, shutil, argparse, datetime
from pathlib import Path
from typing import List, Dict, Tuple, Optional

# ══════════════════════════════════════════════════════════════
#  ZONA DE PROTECCIÓN — Líneas que NUNCA se modifican
# ══════════════════════════════════════════════════════════════

PROTECTED_LINE_PATTERNS: List[re.Pattern] = [
    # Docker FROM — requiere "/" (path de imagen, no import Python)
    re.compile(r"^\s*FROM\s+\S+/\S*frigate", re.IGNORECASE),
    # Imagen Docker upstream en cualquier contexto
    re.compile(r"ghcr\.io/blakeblackshear"),
    # Repositorio GitHub upstream (solo patrones más complejos, el texto simple se reescribe)
    re.compile(r"github\.com/blakeblackshear/frigate\.git"),
    # Rutas de grabaciones en disco (datos de usuario)
    re.compile(r"/media/frigate/"),
    # Identificador de add-on de Home Assistant (fijo, externo)
    re.compile(r"ccab4aaf_frigate"),
    # Variables de autenticación definidas por el usuario
    re.compile(r"\{FRIGATE_RTSP_"),
    re.compile(r"\{FRIGATE_ONVIF_"),
    re.compile(r"\{FRIGATE_MQTT_"),
    re.compile(r"\{FRIGATE_GO2RTC_"),
    re.compile(r"\{FRIGATE_GENAI_"),
]

PROTECTED_SUBSTRINGS: List[str] = [
    "ghcr.io/blakeblackshear",
    "/media/frigate/",
    "ccab4aaf_frigate",
]

def is_protected_line(line: str) -> bool:
    for p in PROTECTED_LINE_PATTERNS:
        if p.search(line):
            return True
    for s in PROTECTED_SUBSTRINGS:
        if s in line:
            return True
    return False


# ══════════════════════════════════════════════════════════════
#  REGLAS DE REEMPLAZO (orden importa — más específico primero)
# ══════════════════════════════════════════════════════════════

DISPLAY_REPLACEMENTS: List[Tuple[str, str]] = [
    # URLs de documentación
    ("https://docs.frigate.video", "https://docs.secure.vu"),
    ("docs.frigate.video", "docs.secure.vu"),
    # Repositorio GitHub (texto simple, README, docs)
    ("github.com/blakeblackshear/frigate", "github.com/SecureCorp-Mexico/SecureVu"),
    # Branding general
    ("Frigate NVR",  "SecureVu NVR"),
    ("Frigate nvr",  "SecureVu NVR"),
    ("frigate-nvr",  "securevu-nvr"),
    ("frigate_nvr",  "securevu_nvr"),
    ("Frigate",      "SecureVu"),
    ("FRIGATE",      "SECUREVU"),
    ("frigate",      "securevu"),
]

def apply_replacements(text: str) -> Tuple[str, int]:
    count = 0
    for old, new in DISPLAY_REPLACEMENTS:
        n = text.count(old)
        if n:
            text = text.replace(old, new)
            count += n
    return text, count

def process_line_safe(line: str) -> Tuple[str, int]:
    """Reemplaza en una línea respetando protecciones."""
    if is_protected_line(line):
        return line, 0
    return apply_replacements(line)


# ══════════════════════════════════════════════════════════════
#  PROCESADORES POR TIPO DE ARCHIVO
# ══════════════════════════════════════════════════════════════

def process_generic(content: str) -> Tuple[str, int]:
    """Markdown, HTML, CSS, TXT, YAML, Dockerfile, JS/TS, XML..."""
    lines = content.splitlines(keepends=True)
    result, total = [], 0
    for line in lines:
        new_line, n = process_line_safe(line)
        result.append(new_line)
        total += n
    return "".join(result), total


def process_python(content: str) -> Tuple[str, int]:
    """
    Python — manejo especial por contexto:
      • Imports  : from frigate.X  → from securevu.X
      • General  : comentarios, docstrings y strings de display
      • NO toca: topic_prefix por defecto (se mantiene 'frigate')
    """
    lines = content.splitlines(keepends=True)
    result, total = [], 0
    for line in lines:
        if is_protected_line(line):
            result.append(line)
            continue

        new_line = line

        # 1. Imports Python: from frigate.X / import frigate
        if re.match(r"\s*(from|import)\s+frigate", new_line, re.IGNORECASE):
            new_line, n = apply_replacements(new_line)
            total += n
            result.append(new_line)
            continue

        # 2. Reemplazo general (comentarios, docstrings, strings de display)
        new_line, n = process_line_safe(new_line)
        total += n
        result.append(new_line)
    return "".join(result), total


def process_json(content: str, path: Path) -> Tuple[str, int]:
    """JSON — reemplaza valores y valida que siga siendo JSON válido."""
    try:
        new_content, n = process_generic(content)
        json.loads(new_content)   # validar integridad
        return new_content, n
    except json.JSONDecodeError:
        return content, 0         # sin cambios si el resultado rompe el JSON


# ══════════════════════════════════════════════════════════════
#  CLASIFICACIÓN DE ARCHIVOS
# ══════════════════════════════════════════════════════════════

SKIP_DIRS = {
    ".git", "node_modules", "__pycache__", ".venv", "venv",
    "dist", "build", ".next", ".nuxt", "vendor",
    "site-packages", ".mypy_cache", ".pytest_cache", "htmlcov",
}
SKIP_FILES = {
    "smart_rebrand.py", "rebrand_report.md",
    "package-lock.json", "yarn.lock", "poetry.lock", "pnpm-lock.yaml",
}
IMAGE_EXTS   = {".png", ".jpg", ".jpeg", ".ico", ".webp", ".gif"}
LOGO_KEYWORDS = {"logo", "frigate", "favicon", "icon", "brand", "splash", "apple-touch"}

def get_processor(path: Path):
    ext  = path.suffix.lower()
    name = path.name.lower()
    if name == "dockerfile" or ext == ".dockerfile":
        return process_generic
    if ext == ".py":
        return process_python
    if ext == ".json":
        return lambda c: process_json(c, path)
    if ext in {
        ".yaml", ".yml", ".toml", ".ini",
        ".cfg", ".conf", ".env", ".md", ".txt",
        ".rst", ".html", ".htm", ".css", ".scss",
        ".sass", ".less", ".svg", ".xml",
        ".js", ".ts", ".jsx", ".tsx",
        ".svelte", ".vue", ".mjs", ".cjs",
        ".sh", ".bash", ".zsh", ".service",
        ".gitignore", ".editorconfig"
    }:
        return process_generic
    return None

def is_logo_image(path: Path) -> bool:
    return (path.suffix.lower() in IMAGE_EXTS
            and any(k in path.name.lower() for k in LOGO_KEYWORDS))


# ══════════════════════════════════════════════════════════════
#  CLASE PRINCIPAL
# ══════════════════════════════════════════════════════════════

class SmartRebrander:
    def __init__(self, root: Path, dry_run=False, verbose=False):
        self.root    = root
        self.dry_run = dry_run
        self.verbose = verbose
        self.changed:          List[Dict] = []
        self.images:           List[Path] = []
        self.errors:           List[str]  = []
        self.py_module_renamed = False

    def _skip_dir(self, p: Path) -> bool:
        return any(part in SKIP_DIRS for part in p.parts)

    def _rename_target(self, path: Path) -> Optional[Path]:
        if not re.search(r"frigate", path.name, re.IGNORECASE):
            return None
        new_name = re.sub(
            r"(?i)(FRIGATE|Frigate|frigate)",
            lambda m: ("SECUREVU"  if m.group().isupper() else
                       "SecureVu"  if m.group()[0].isupper() else
                       "securevu"),
            path.name,
        )
        return (path.parent / new_name) if new_name != path.name else None

    # ── Fase 1: renombrar módulo Python ───────────────────

    def _phase_python_module(self):
        src = self.root / "frigate"
        dst = self.root / "securevu"
        if src.is_dir() and not dst.exists():
            if not self.dry_run:
                shutil.copytree(str(src), str(dst))
                shutil.rmtree(str(src))
            self.py_module_renamed = True
            print("  📦 Módulo Python renombrado: frigate/ → securevu/")
        else:
            print("  ℹ️  Directorio frigate/ no encontrado o ya renombrado.")

    # ── Fase 2: archivos de texto ──────────────────────────

    def _phase_text_files(self):
        for p in sorted(self.root.rglob("*")):
            if not p.is_file():
                continue
            if self._skip_dir(p) or p.name in SKIP_FILES:
                continue
            if is_logo_image(p):
                self.images.append(p.relative_to(self.root))
                continue

            proc = get_processor(p)
            if not proc:
                continue

            try:
                raw = p.read_bytes()
                try:
                    text = raw.decode("utf-8")
                except UnicodeDecodeError:
                    try:
                        text = raw.decode("latin-1")
                    except:
                        continue

                new_text, n = proc(text)
                new_path    = self._rename_target(p)

                if n > 0 or new_path:
                    rel = p.relative_to(self.root)
                    self.changed.append({
                        "file":         str(rel),
                        "replacements": n,
                        "renamed_to":   str(new_path.relative_to(self.root)) if new_path else None,
                        "ext":          p.suffix or p.name,
                    })
                    if self.verbose:
                        tag = f" → {new_path.name}" if new_path else ""
                        print(f"  ✅ {rel}  ({n} reemplazos){tag}")

                    if not self.dry_run:
                        target = new_path if new_path else p
                        target.write_text(new_text, encoding="utf-8")
                        if new_path and p.exists() and new_path != p:
                            p.unlink()

            except Exception as exc:
                self.errors.append(f"{p.relative_to(self.root)}: {exc}")

    # ── Runner ─────────────────────────────────────────────

    def run(self):
        mode = "DRY-RUN (sin cambios reales)" if self.dry_run else "ACTIVO — aplicando cambios"
        print(f"\n{'='*62}")
        print(f"  SecureVu Smart Rebranding Tool v2 — SecureCorp Mexico")
        print(f"  Repositorio : {self.root}")
        print(f"  Modo        : {mode}")
        print(f"{'='*62}\n")

        print("⏳ Fase 1 — Módulo Python principal...")
        self._phase_python_module()

        print("\n⏳ Fase 2 — Archivos de texto y configuración...")
        self._phase_text_files()

        self._print_summary()
        self._generate_report()

    def _print_summary(self):
        total = sum(c["replacements"] for c in self.changed)
        print(f"\n{'='*62}")
        print(f"  ✅ Archivos modificados  : {len(self.changed)}")
        print(f"  🔄 Reemplazos totales    : {total}")
        print(f"  🖼  Imágenes (manual)     : {len(self.images)}")
        print(f"  ❌ Errores               : {len(self.errors)}")
        print(f"{'='*62}")
        if self.images:
            print("\n🖼  Reemplaza estos archivos con el logo de SecureCorp Mexico:")
            for img in self.images:
                print(f"   ⚠️  {img}")
        if self.errors:
            print("\n❌ Errores:")
            for e in self.errors:
                print(f"   {e}")
        print(f"\n📄 Reporte: {self.root / 'rebrand_report.md'}\n")

    def _generate_report(self):
        now   = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        total = sum(c["replacements"] for c in self.changed)

        by_ext: Dict[str, List] = {}
        for c in self.changed:
            by_ext.setdefault(c["ext"], []).append(c)

        SIZE_HINTS = {
            "favicon-16": "16×16 px",  "favicon-32": "32×32 px",
            "favicon": "ICO multi-size", "apple-touch": "180×180 px",
            "android-chrome-192": "192×192 px",
            "android-chrome-512": "512×512 px",
            "og-image": "1200×630 px",
            "logo": "SVG vectorial",
            "splash": "Según resolución",
        }

        L = [
            "# 📋 Reporte Smart Rebranding — Frigate → SecureVu",
            f"**Fecha:** {now}  ",
            f"**Modo:** {'DRY-RUN' if self.dry_run else '✅ Aplicado'}  ",
            f"**Módulo Python:** {'✅ frigate/ → securevu/' if self.py_module_renamed else '⬜ No encontrado'}  ",
            f"**Archivos modificados:** {len(self.changed)}  ",
            f"**Reemplazos totales:** {total}  ",
            "",
            "---", "",
            "## 🛡 Zonas Protegidas (no tocadas)", "",
            "| Patrón | Razón |",
            "|--------|-------|",
            "| `FROM ghcr.io/blakeblackshear/frigate` | Imagen base Docker upstream |",
            "| `ghcr.io/blakeblackshear/frigate` | Referencia a imagen upstream |",
            "| `github.com/blakeblackshear/frigate.git` | Git URL upstream completo |",
            "| `/media/frigate/` | Rutas de grabaciones en disco |",
            "| `{FRIGATE_RTSP_*}` | Variables de autenticación RTSP/ONVIF |",
            "| `{FRIGATE_MQTT_*}` | Variables de autenticación MQTT |",
            "| `{FRIGATE_GENAI_*}` | Variables de API de IA |",
            "| `ccab4aaf_frigate` | ID fijo del add-on de Home Assistant |",
            "",
            "---", "",
            "## 🔊 MQTT — Prefijo por Defecto",
            "",
            "> El valor por defecto de `topic_prefix` **se mantiene en `frigate`**.",
            "> Las instalaciones existentes que ya usan `frigate/` no requieren cambios.",
            "",
            "---", "",
            "## 📂 Archivos Modificados por Tipo", "",
        ]

        for ext, files in sorted(by_ext.items()):
            n_sum = sum(f["replacements"] for f in files)
            L.append(f"### `{ext}` — {len(files)} archivos · {n_sum} reemplazos")
            L.append("")
            L.append("| Archivo | Reemplazos | Renombrado a |")
            L.append("|---------|-----------|--------------|")
            for f in files:
                ren = f"`{f['renamed_to']}`" if f["renamed_to"] else "—"
                L.append(f"| `{f['file']}` | {f['replacements']} | {ren} |")
            L.append("")

        if self.images:
            L += [
                "---", "",
                "## 🖼 Imágenes — Reemplazo Manual", "",
                "| Archivo | Dimensiones sugeridas | Estado |",
                "|---------|----------------------|--------|",
            ]
            for img in self.images:
                hint = "Ver diseño"
                for k, v in SIZE_HINTS.items():
                    if k in str(img).lower():
                        hint = v; break
                L.append(f"| `{img}` | {hint} | ⬜ Pendiente |")
            L.append("")

        L += [
            "---", "",
            "## 🚀 Comandos Post-Rebranding", "",
            "```bash",
            "# 1. Reemplazar imágenes con assets de SecureCorp Mexico",
            "",
            "# 2. Si el módulo Python fue renombrado, actualizar pyproject.toml:",
            "# [tool.poetry.scripts]",
            "# securevu = 'securevu.__main__:main'",
            "",
            "# 3. Reconstruir el frontend",
            "cd web && npm install && npm run build",
            "",
            "# 4. Construir la imagen Docker",
            "docker build -t securevu:latest .",
            "",
            "# 5. Verificar que el módulo Python importa correctamente",
            "docker run --rm securevu:latest python -c \"import securevu; print('OK')\"",
            "",
            "# 6. Mantener topic_prefix en 'frigate' en config.yml si ya está en producción:",
            "# mqtt:",
            "#   topic_prefix: frigate",
            "",
            "# 7. Commit y push",
            "git add . && git commit -m \"rebrand: Frigate -> SecureVu (SecureCorp Mexico)\"",
            "git push origin main",
            "```",
        ]

        (self.root / "rebrand_report.md").write_text("\n".join(L), encoding="utf-8")


# ══════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════

def main():
    p = argparse.ArgumentParser(
        description="SecureVu Smart Rebranding Tool v2 — Frigate → SecureVu (SecureCorp Mexico)"
    )
    p.add_argument("--path", "-p", default=".",
                   help="Ruta al repositorio clonado (default: directorio actual)")
    p.add_argument("--dry-run", "-d", action="store_true",
                   help="Solo analiza, no aplica cambios")
    p.add_argument("--verbose", "-v", action="store_true",
                   help="Muestra cada archivo procesado en tiempo real")
    args = p.parse_args()

    root = Path(args.path).resolve()
    if not root.exists():
        print(f"Error: la ruta '{root}' no existe.")
        sys.exit(1)

    SmartRebrander(root=root, dry_run=args.dry_run, verbose=args.verbose).run()


if __name__ == "__main__":
    main()
