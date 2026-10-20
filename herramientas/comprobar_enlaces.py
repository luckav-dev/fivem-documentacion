#!/usr/bin/env python3
"""Comprueba que todos los enlaces relativos de los .md del repositorio apuntan a archivos y anclas que existen.

Uso: python3 herramientas/comprobar_enlaces.py [carpeta ...]
"""
import re
import sys
from functools import lru_cache
from pathlib import Path
from urllib.parse import unquote

RAIZ = Path(__file__).resolve().parent.parent
ENLACE = re.compile(r'(?<!\!)\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
IMAGEN = re.compile(r'!\[[^\]]*\]\(([^)\s]+)(?:\s+"[^"]*")?\)')
HTML_SRC = re.compile(r'<(?:img|a)\s[^>]*(?:src|href)="([^"]+)"', re.I)


def slug(texto):
    """Ancla al estilo GitHub."""
    t = re.sub(r'<[^>]+>', '', texto)
    t = re.sub(r'!?\[([^\]]*)\]\([^)]*\)', r'\1', t)
    t = t.replace('`', '').strip().lower()
    t = re.sub(r'[^\w\- ]', '', t, flags=re.UNICODE)
    return t.replace(' ', '-')


@lru_cache(maxsize=None)
def anclas(ruta):
    vistas, res, en_codigo = {}, set(), False
    for linea in ruta.read_text(encoding='utf-8', errors='replace').splitlines():
        if linea.lstrip().startswith('```'):
            en_codigo = not en_codigo
            continue
        if en_codigo:
            continue
        m = re.match(r'^(#{1,6})\s+(.+?)\s*#*\s*$', linea)
        if m:
            base = slug(m.group(2))
            n = vistas.get(base, 0)
            vistas[base] = n + 1
            res.add(base if n == 0 else f'{base}-{n}')
        for a in re.findall(r'<[a-z0-9]+\s[^>]*\b(?:name|id)="([^"]+)"', linea):
            res.add(a)
    return frozenset(res)


def sin_codigo(texto):
    return re.sub(r'```.*?```', '', texto, flags=re.S)


def main():
    carpetas = [RAIZ / c for c in sys.argv[1:]] or [RAIZ]
    errores = 0
    archivos = [p for c in carpetas for p in (c.rglob('*.md') if c.is_dir() else [c])]
    for md in archivos:
        texto = sin_codigo(md.read_text(encoding='utf-8', errors='replace'))
        destinos = ENLACE.findall(texto) + IMAGEN.findall(texto) + HTML_SRC.findall(texto)
        for destino in destinos:
            if re.match(r'^<?[a-z][a-z0-9+.-]*:', destino, re.I) or destino.startswith('//'):
                continue  # externo (http, https, mailto, fivem://...)
            ruta_txt, _, ancla = destino.partition('#')
            ruta = (md.parent / unquote(ruta_txt)).resolve() if ruta_txt else md
            if not ruta.exists():
                print(f'{md.relative_to(RAIZ)}: no existe {destino}')
                errores += 1
                continue
            if ancla and ruta.suffix == '.md' and unquote(ancla) not in anclas(ruta):
                print(f'{md.relative_to(RAIZ)}: ancla inexistente {destino}')
                errores += 1
    print(f'{len(archivos)} archivos revisados, {errores} enlaces rotos')
    return 1 if errores else 0


if __name__ == '__main__':
    sys.exit(main())
