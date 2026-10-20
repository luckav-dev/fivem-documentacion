#!/usr/bin/env python3
"""Genera la referencia offline de natives (natives/) a partir de las bases de datos oficiales.

Uso:
    python3 herramientas/generar_natives.py            # usa datos/*.json
    python3 herramientas/generar_natives.py --descargar  # descarga antes las versiones actuales

Fuentes oficiales:
    https://static.cfx.re/natives/natives.json      (natives de GTA V)
    https://static.cfx.re/natives/natives_cfx.json  (natives propios de FiveM / CFX)
    datos/rpc_spec_natives.lua                       (natives de GTA V que FiveM permite usar en el servidor como RPC)
"""
import json
import re
import shutil
import sys
import urllib.request
from collections import defaultdict
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
DATOS = RAIZ / 'datos'
SALIDA = RAIZ / 'natives'
MAX_BYTES = 320_000  # GitHub deja de renderizar markdown hacia los 512 KB

FUENTES = {
    'natives.json': 'https://static.cfx.re/natives/natives.json',
    'natives_cfx.json': 'https://static.cfx.re/natives/natives_cfx.json',
}


def descargar():
    for nombre, url in FUENTES.items():
        print('Descargando', url)
        with urllib.request.urlopen(url) as r, open(DATOS / nombre, 'wb') as f:
            shutil.copyfileobj(r, f)


def nombre_lua(nombre):
    """Misma conversión que ext/natives/codegen_out_lua.lua (printFunctionName)."""
    s = nombre.lower().replace('0x', 'n_0x')
    s = re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)
    return s[0].upper() + s[1:] if s else s


def es_puntero(tipo):
    return tipo.endswith('*') and tipo not in ('char*', 'const char*')


def firma_lua(n):
    ps = n.get('params', [])
    ptr = [es_puntero(p['type']) for p in ps]
    unico_final = sum(ptr) == 1 and ptr and ptr[-1]
    args = [p['name'] for p, x in zip(ps, ptr) if unico_final or not x]
    rets = []
    if n.get('results') not in (None, 'void'):
        rets.append('retval')
    rets += [p['name'] for p, x in zip(ps, ptr) if x]
    llamada = f"{nombre_lua(n['name'])}({', '.join(args)})"
    return (f"local {', '.join(rets)} = {llamada}" if rets else llamada), unico_final


def firma_c(n):
    ps = ', '.join(f"{p['type']} {p['name']}" for p in n.get('params', []))
    return f"{n.get('results', 'void')} {n['name']}({ps});"


def limpiar_markdown(texto):
    """Ajusta el markdown oficial para que no rompa la estructura del archivo."""
    if not texto:
        return ''
    lineas = []
    for linea in texto.replace('\r\n', '\n').split('\n'):
        m = re.match(r'^(#{1,6})\s+(.*)$', linea)
        if m:
            linea = f'**{m.group(2).strip()}**'
        lineas.append(linea)
    t = '\n'.join(lineas).strip()
    if t.count('```') % 2:
        t += '\n```'
    return t


def rpc_servidor():
    nombres = set()
    f = DATOS / 'rpc_spec_natives.lua'
    if f.exists():
        for linea in f.read_text(encoding='utf-8').splitlines():
            for m in re.finditer(r"_rpc '([A-Z0-9_]+)'(?: \{ '([A-Z0-9_]+)' \})?", linea):
                nombres.add(m.group(1))  # el segundo nombre entre llaves es solo el getter interno, no un RPC
    return nombres


ENLACE_HASH = re.compile(r'\]\((?:https://docs\.fivem\.net/natives/)?[#?]?(?:\\?_)?(0(?:\\?_)?x[0-9A-Fa-f]+)\)')  # incluye la errata oficial '#0\_x...'

LADO = {'client': 'Cliente', 'server': 'Servidor', 'shared': 'Cliente y servidor'}


def entrada(n, lado, rpc=False):
    nl = nombre_lua(n['name'])
    lua, unico_final = firma_lua(n)
    out = [f'### {nl}', '']
    meta = [f"`{n['name']}`", f"hash `{n.get('hash', '?')}`"]
    if n.get('jhash'):
        meta.append(f"jhash `{n['jhash']}`")
    lado_txt = LADO.get(lado, lado)
    if rpc:
        lado_txt += ' · también en el servidor (RPC)'
    meta.append(f'**{lado_txt}**')
    out.append(' · '.join(meta))
    out.append('')
    out += ['```lua', lua, '```', '```c', firma_c(n), '```', '']
    ps = n.get('params', [])
    if ps:
        out.append('**Parámetros**')
        out.append('')
        for p in ps:
            d = (p.get('description') or '').strip().replace('\n', ' ')
            extra = ''
            if es_puntero(p['type']):
                extra = ' *(puntero: se devuelve como valor de retorno' + (', argumento opcional' if unico_final else ', no se pasa') + ')*'
            elif p['type'] == 'Hash':
                extra = ' *(acepta un string: se convierte con GetHashKey)*'
            out.append(f"- `{p['name']}` (`{p['type']}`){extra}" + (f': {d}' if d else ''))
        out.append('')
    res = n.get('results', 'void')
    rdesc = (n.get('resultsDescription') or '').strip().replace('\n', ' ')
    out.append(f'**Devuelve:** `{res}`' + (f' — {rdesc}' if rdesc else ''))
    out.append('')
    desc = limpiar_markdown(n.get('description'))
    if desc:
        out += ['**Descripción oficial:**', '', desc, '']
    alias = n.get('aliases') or []
    if alias:
        out.append('**Nombres antiguos (alias):** ' + ', '.join(f'`{a}` (`{nombre_lua(a)}`)' for a in alias))
        out.append('')
    for ej in n.get('examples') or []:
        lang = ej.get('lang') or ''
        code = (ej.get('code') or '').rstrip()
        if code:
            out += [f'**Ejemplo ({lang or "código"}):**', '', f'```{lang}', code, '```', '']
    out.append('---')
    out.append('')
    return ENLACE_HASH.sub(lambda m: f'](@@{int(re.sub(r"[^0-9A-Fa-fx]", "", m.group(1)), 16):x}@@)', '\n'.join(out))


DESTINO = {}  # nombre_lua -> archivo


def escribir_partes(base, titulo, intro, entradas):
    """Escribe una o varias partes (<=MAX_BYTES). Devuelve [(archivo, primero, ultimo, n)]."""
    partes, actual, tam = [], [], 0
    for nombre, texto in entradas:
        b = len(texto.encode('utf-8'))
        if actual and tam + b > MAX_BYTES:
            partes.append(actual)
            actual, tam = [], 0
        actual.append((nombre, texto))
        tam += b
    if actual:
        partes.append(actual)
    resultado = []
    for i, parte in enumerate(partes, 1):
        sufijo = '' if len(partes) == 1 else f'-{i}'
        archivo = base.with_name(base.stem + sufijo + '.md')
        primero, ultimo = parte[0][0], parte[-1][0]
        cab = [f'# {titulo}' + (f' (parte {i} de {len(partes)}: {primero} … {ultimo})' if len(partes) > 1 else ''), '']
        cab += [intro, '']
        if len(partes) > 1:
            nav = []
            for j in range(1, len(partes) + 1):
                nombre_j = base.stem + f'-{j}.md'
                nav.append(f'**[{j}]**' if j == i else f'[{j}]({nombre_j})')
            cab += ['Partes: ' + ' · '.join(nav), '']
        cab += ['[← Índice de natives](../README.md)', '', '## Índice de esta página', '']
        cab += [' · '.join(f'[`{nm}`](#{nm.lower()})' for nm, _ in parte), '', '---', '']
        archivo.write_text('\n'.join(cab) + ''.join(t for _, t in parte), encoding='utf-8')
        for nm, _ in parte:
            DESTINO[nm] = archivo
        resultado.append((archivo, primero, ultimo, len(parte)))
    return resultado


def main():
    if '--descargar' in sys.argv:
        descargar()
    gta = json.load(open(DATOS / 'natives.json', encoding='utf-8'))
    cfx = json.load(open(DATOS / 'natives_cfx.json', encoding='utf-8'))
    rpc = rpc_servidor()

    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    (SALIDA / 'gta5').mkdir(parents=True)
    (SALIDA / 'cfx').mkdir(parents=True)
    (SALIDA / 'indice').mkdir(parents=True)

    hoy = date.today().isoformat()
    aviso = (f'> Generado el {hoy} desde la base de datos oficial de Cfx.re '
             '(`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. '
             'Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).')

    indice_global = []  # (nombre_lua, nombre_c, archivo_rel, lado, ns)
    tabla_ns = []

    # --- GTA V ---
    for ns in sorted(gta):
        items = []
        for n in gta[ns].values():
            if 'name' not in n:  # natives sin nombre: FiveM los expone como N_0x<hash>
                n = dict(n, name=n['hash'], sin_nombre=True)
            items.append(n)
        items.sort(key=lambda n: nombre_lua(n['name']))
        entradas = [(nombre_lua(n['name']), entrada(n, 'client', n['name'] in rpc)) for n in items]
        partes = escribir_partes(SALIDA / 'gta5' / f'{ns}.md', f'Natives de GTA V — {ns}',
                                 aviso + f'\n\nNamespace `{ns}`: **{len(items)}** natives.', entradas)
        for n in items:
            nl = nombre_lua(n['name'])
            arch = next(a for a, p, u, _ in partes if p <= nl <= u)
            indice_global.append((nl, n['name'], f'gta5/{arch.name}', 'Cliente' + (' + servidor (RPC)' if n['name'] in rpc else ''), ns))
        tabla_ns.append(('gta5', ns, len(items), partes))

    # --- CFX (solo GTA V / comunes) ---
    por_lado = defaultdict(list)
    for ns in cfx.values():
        for n in ns.values():
            if 'name' not in n or n.get('game') not in (None, 'gta5'):
                continue
            por_lado[n.get('apiset', 'client')].append(n)
    nombres_cfx = {'shared': 'compartidos', 'server': 'servidor', 'client': 'cliente'}
    titulos_cfx = {'shared': 'Natives de FiveM (CFX) — cliente y servidor',
                   'server': 'Natives de FiveM (CFX) — solo servidor',
                   'client': 'Natives de FiveM (CFX) — solo cliente'}
    for lado in ('shared', 'server', 'client'):
        items = sorted(por_lado[lado], key=lambda n: nombre_lua(n['name']))
        entradas = [(nombre_lua(n['name']), entrada(n, lado)) for n in items]
        partes = escribir_partes(SALIDA / 'cfx' / f'{nombres_cfx[lado]}.md', titulos_cfx[lado],
                                 aviso + f'\n\n**{len(items)}** natives.', entradas)
        for n in items:
            nl = nombre_lua(n['name'])
            arch = next(a for a, p, u, _ in partes if p <= nl <= u)
            indice_global.append((nl, n['name'], f'cfx/{arch.name}', LADO[lado], 'CFX'))
        tabla_ns.append(('cfx', nombres_cfx[lado], len(items), partes))

    # --- Índice alfabético por letra ---
    por_letra = defaultdict(list)
    for fila in indice_global:
        letra = fila[0][0].upper() if fila[0][0].isalpha() else '0-9'
        if fila[0].startswith('N_0x'):
            letra = 'N_0x'
        por_letra[letra].append(fila)
    letras = sorted(por_letra)
    for letra in letras:
        filas = sorted(por_letra[letra])
        lineas = [f'# Índice alfabético de natives — {letra}', '', '[← Índice de natives](../README.md)', '',
                  'Letras: ' + ' · '.join(f'[{l}]({l}.md)' for l in letras), '',
                  '| Nombre Lua | Nombre oficial | Lado | Namespace |', '|---|---|---|---|']
        for nl, nc, arch, lado, ns in filas:
            lineas.append(f'| [`{nl}`](../{arch}#{nl.lower()}) | `{nc}` | {lado} | {ns} |')
        (SALIDA / 'indice' / f'{letra}.md').write_text('\n'.join(lineas) + '\n', encoding='utf-8')

    # --- README de natives ---
    total_gta = sum(c for t, _, c, _ in tabla_ns if t == 'gta5')
    total_cfx = sum(c for t, _, c, _ in tabla_ns if t == 'cfx')
    r = [
        '# Referencia completa de natives (offline)', '',
        f'Generada el {hoy} desde la base de datos oficial de Cfx.re. Contiene **{total_gta} natives de GTA V** '
        f'y **{total_cfx} natives propios de FiveM (CFX)**: firma Lua, declaración C, parámetros, valor devuelto, '
        'descripción oficial, nombres antiguos y ejemplos oficiales.', '',
        '- Para regenerarla con la versión más reciente: `python3 herramientas/generar_natives.py --descargar`.',
        '- Para buscar un native sin internet: `grep -rn "GetEntityCoords" natives/` o el [índice alfabético](#índice-alfabético).', '',
        '## Cómo leer cada entrada', '',
        '- **Título**: nombre tal como lo escribes en Lua/JS (`GET_ENTITY_COORDS` → `GetEntityCoords`).',
        '- **Línea de datos**: nombre oficial, hash (para `Citizen.InvokeNative`) y en qué lado se puede usar.',
        '- **Bloque `lua`**: cómo se llama desde Lua. Los parámetros **puntero** (`int*`, `float*`, `Vector3*`…) **no se pasan**: '
        'se devuelven después de `retval`. Excepción del generador oficial: si el **único** puntero es el **último** parámetro, '
        'aparece como argumento (opcional) y también se devuelve.',
        '- **Bloque `c`**: declaración original del native.',
        '- **Parámetros `Hash`**: aceptan un string (FiveM lo convierte con `GetHashKey`).',
        '- **Servidor (RPC)**: natives de GTA V que FiveM permite llamar desde el servidor; se ejecutan en el cliente dueño de la entidad.',
        '- **Descripción oficial**: texto original de la documentación (inglés), sin modificar.', '',
        '## Natives propios de FiveM (CFX)', '',
        '| Lado | Natives | Archivos |', '|---|---|---|',
    ]
    for t, ns, c, partes in tabla_ns:
        if t != 'cfx':
            continue
        enlaces = ' · '.join(f'[{a.name}](cfx/{a.name})' for a, *_ in partes)
        r.append(f'| {ns} | {c} | {enlaces} |')
    r += ['', '## Natives de GTA V por namespace', '', '| Namespace | Natives | Archivos |', '|---|---|---|']
    for t, ns, c, partes in tabla_ns:
        if t != 'gta5':
            continue
        enlaces = ' · '.join(f'[{a.name}](gta5/{a.name})' for a, *_ in partes)
        r.append(f'| `{ns}` | {c} | {enlaces} |')
    r += ['', '## Índice alfabético', '', ' · '.join(f'[{l}](indice/{l}.md)' for l in letras), '']
    (SALIDA / 'README.md').write_text('\n'.join(r), encoding='utf-8')
    # --- Resolver enlaces entre natives (por hash) ---
    por_hash = {}
    for ns in gta.values():
        for n in ns.values():
            nm = nombre_lua(n.get('name') or n['hash'])
            for h in (n.get('hash'), n.get('jhash')):
                if h:
                    por_hash[int(h, 16)] = nm
    for ns in cfx.values():
        for n in ns.values():
            if 'name' in n and n.get('game') in (None, 'gta5') and n.get('hash'):
                por_hash[int(n['hash'], 16)] = nombre_lua(n['name'])
    import os
    sin_resolver = 0
    for archivo in sorted(set(DESTINO.values())):
        texto = archivo.read_text(encoding='utf-8')

        def sustituir(m):
            nonlocal sin_resolver
            nm = por_hash.get(int(m.group(1), 16))
            if not nm or nm not in DESTINO:
                sin_resolver += 1
                return f'](https://docs.fivem.net/natives/?_0x{m.group(1).upper()})'
            destino = DESTINO[nm]
            rel = os.path.relpath(destino, archivo.parent).replace(os.sep, '/')
            return f']({rel if destino != archivo else ""}#{nm.lower()})'
        archivo.write_text(re.sub(r'\]\(@@([0-9a-f]+)@@\)', sustituir, texto), encoding='utf-8')
    print('Enlaces entre natives sin resolver:', sin_resolver)
    print(f'GTA V: {total_gta} · CFX: {total_cfx} · archivos:', sum(len(p) for *_, p in tabla_ns))


if __name__ == '__main__':
    main()
