"""Valida sintaxis Python y enlaces Markdown locales, sin servicios ni credenciales.

Ejecutar desde cualquier directorio: python docente/validar_materiales.py
No evalúa exactitud pedagógica ni disponibilidad de enlaces externos. Omite ejemplos
dentro de bloques de código; comprueba archivos y anclas de los enlaces Markdown.
"""
from __future__ import annotations

import ast
from collections import Counter
from pathlib import Path
import re
import subprocess
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r'!?\[[^\]\n]*\]\(\s*(<[^>]+>|[^\s)]+)(?:\s+"[^"]*")?\s*\)')


def prose(text: str):
    """Conserva números de línea y omite fences de backticks o tildes."""
    fence = None
    for number, line in enumerate(text.splitlines(), 1):
        marker = re.match(r'^\s{0,3}(`{3,}|~{3,})', line)
        if marker:
            token = marker.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            continue
        if fence is None:
            yield number, line


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)', text))
    used: Counter = Counter()
    for _, line in prose(text):
        heading = re.match(r'^ {0,3}#{1,6}\s+(.+?)\s*#*$', line)
        if not heading:
            continue
        label = re.sub(r'\[([^\]]+)\]\([^)]*\)', r'\1', heading.group(1))
        label = re.sub(r'<[^>]*>', '', label).lower()
        slug = re.sub(r'[^\w\- ]', '', label, flags=re.UNICODE).replace(' ', '-')
        result.add(slug + (f'-{used[slug]}' if used[slug] else ''))
        used[slug] += 1
    return result


def main() -> int:
    raw = subprocess.check_output(
        ['git', 'ls-files', '--cached', '--others', '--exclude-standard', '-z'], cwd=ROOT)
    paths = sorted({ROOT / name.decode() for name in raw.split(b'\0') if name})
    errors = []
    counts: Counter = Counter()
    anchor_cache = {}
    for path in paths:
        if not path.is_file() or path.suffix not in {'.md', '.py'}:
            continue
        content = path.read_text(encoding='utf-8')
        relative = path.relative_to(ROOT)
        counts[path.suffix] += 1
        if path.suffix == '.py':
            try:
                ast.parse(content, filename=str(relative))
            except SyntaxError as error:
                errors.append(f'{relative}:{error.lineno}: {error.msg}')
            continue
        for number, line in prose(content):
            for match in LINK.finditer(line):
                href = match.group(1).strip('<>')
                parsed = urlsplit(href)
                if parsed.scheme or parsed.netloc:
                    counts['externos omitidos'] += 1
                    continue
                target = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
                counts['enlaces locales'] += 1
                if not target.exists():
                    errors.append(f'{relative}:{number}: ruta inexistente: {href}')
                elif parsed.fragment and target.suffix == '.md':
                    if target not in anchor_cache:
                        anchor_cache[target] = anchors(target.read_text(encoding='utf-8'))
                    if unquote(parsed.fragment) not in anchor_cache[target]:
                        errors.append(f'{relative}:{number}: ancla inexistente: {href}')
    for name, count in counts.items():
        print(f'{name}: {count}')
    for error in errors:
        print(f'ERROR {error}')
    print(f'Resultado: {len(errors)} errores; sin llamadas a servicios externos.')
    return 1 if errors else 0


if __name__ == '__main__':
    raise SystemExit(main())
