#!/usr/bin/env python3
"""Convierte la documentación oficial de FiveM (repositorio citizenfx/fivem-docs, formato Hugo)
en Markdown que se lee sin conexión y se renderiza en GitHub (carpeta docs-oficiales/).

Uso:
    python3 herramientas/convertir_docs_oficiales.py [ruta_a_fivem-docs]

Si no se indica ruta, clona https://github.com/citizenfx/fivem-docs en .cache/fivem-docs.
Requiere haber generado antes natives/ (herramientas/generar_natives.py) para enlazar los natives.

Solo FiveM Legacy: se omiten las páginas exclusivas de "FiveM for GTAV Enhanced" y las secciones
o filas de tabla marcadas como exclusivas de Enhanced.
"""
import html
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
SALIDA = RAIZ / 'docs-oficiales'
IMAGENES = SALIDA / '_archivos'
WEB = 'https://docs.fivem.net'

# Páginas que solo tratan de FiveM for GTAV Enhanced (fuera del alcance: solo Legacy)
EXCLUIR = {
    'alchemist/_index.md',
    'developers/legacy-vs-enhanced.md',
    'server-manual/onboarding-guide-fivem-for-gtav-enhanced.md',
}

ETIQUETAS_ALERTA = {
    'info': 'ℹ️ Información', 'primary': 'ℹ️ Nota', 'secondary': 'ℹ️ Nota', 'success': '✅ Consejo',
    'warning': '⚠️ Advertencia', 'danger': '⛔ Importante',
}

registro = {'omitidas': [], 'secciones_enhanced': [], 'sin_resolver': set(), 'archivos': set()}


# ---------------------------------------------------------------- utilidades

def cargar_repo():
    if len(sys.argv) > 1:
        return Path(sys.argv[1]).resolve()
    destino = RAIZ / '.cache' / 'fivem-docs'
    if not destino.exists():
        destino.parent.mkdir(exist_ok=True)
        subprocess.run(['git', 'clone', '--depth', '1', 'https://github.com/citizenfx/fivem-docs.git', str(destino)], check=True)
    return destino


def commit(repo):
    try:
        return subprocess.run(['git', '-C', str(repo), 'log', '-1', '--format=%h'], capture_output=True, text=True).stdout.strip()
    except Exception:
        return '?'


def front_matter(texto):
    meta = {}
    if texto.startswith('---'):
        fin = texto.find('\n---', 3)
        if fin != -1:
            for linea in texto[3:fin].splitlines():
                m = re.match(r'^(\w+):\s*(.*)$', linea)
                if m:
                    meta[m.group(1)] = m.group(2).strip().strip('"\'')
            texto = texto[fin + 4:].lstrip('\n')
    return meta, texto


def html_a_md(h):
    """Conversión HTML → Markdown suficiente para TypeDoc y posts del foro."""
    h = re.sub(r'<wbr\s*/?>', '', h)
    h = re.sub(r'<pre[^>]*>\s*<code(?: class="(?:language-|lang-)?([\w-]*)[^"]*")?[^>]*>(.*?)</code>\s*</pre>',
               lambda m: f'\n```{m.group(1) or ""}\n{html.unescape(re.sub(r"<[^>]+>", "", m.group(2))).strip()}\n```\n', h, flags=re.S)
    h = re.sub(r'<code[^>]*>(.*?)</code>', lambda m: '`' + re.sub(r'<[^>]+>', '', m.group(1)) + '`', h, flags=re.S)
    h = re.sub(r'<(strong|b)>(.*?)</\1>', r'**\2**', h, flags=re.S)
    h = re.sub(r'<(em|i)>(.*?)</\1>', r'*\2*', h, flags=re.S)
    h = re.sub(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', r'[\2](\1)', h, flags=re.S)
    h = re.sub(r'<img [^>]*src="([^"]+)"[^>]*>', r'![](\1)', h)
    h = re.sub(r'<h([1-6])[^>]*>(.*?)</h\1>', lambda m: '\n' + '#' * (int(m.group(1)) + 2) + ' ' + re.sub(r'<[^>]+>', '', m.group(2)).strip() + '\n', h, flags=re.S)
    h = re.sub(r'<li[^>]*>', '\n- ', h)
    h = re.sub(r'</p>|<br\s*/?>', '\n\n', h)
    h = re.sub(r'<[^>]+>', '', h)
    h = html.unescape(h)
    # quitar la sangría del HTML fuera de los bloques de código (si no, Markdown la toma como código)
    trozos = re.split(r'(```.*?```)', h, flags=re.S)
    for i in range(0, len(trozos), 2):
        trozos[i] = '\n'.join(l.strip() for l in trozos[i].split('\n'))
    h = ''.join(trozos)
    return re.sub(r'\n{3,}', '\n\n', h).strip()


# ---------------------------------------------------------------- natives

def mapa_natives():
    """nombre oficial / nombre Lua / alias → ruta relativa a la raíz + ancla."""
    mapa = {}
    for indice in (RAIZ / 'natives' / 'indice').glob('*.md'):
        for m in re.finditer(r'\| \[`([^`]+)`\]\(\.\./([^)#]+)#([^)]+)\) \| `([^`]+)`', indice.read_text(encoding='utf-8')):
            lua, ruta, ancla, oficial = m.groups()
            destino = ('natives/' + ruta, ancla)
            mapa[lua] = mapa[oficial] = mapa[oficial.lstrip('_')] = destino
    datos = RAIZ / 'datos'
    for archivo in ('natives.json', 'natives_cfx.json'):
        p = datos / archivo
        if not p.exists():
            continue
        for ns in json.load(open(p, encoding='utf-8')).values():
            for n in ns.values():
                nombre = n.get('name') or n.get('hash')
                if nombre in mapa:
                    for alias in n.get('aliases') or []:
                        mapa.setdefault(alias, mapa[nombre])
                    if n.get('hash'):
                        mapa.setdefault(n['hash'].upper(), mapa[nombre])
    return mapa


# ---------------------------------------------------------------- conversión de una página

class Convertidor:
    def __init__(self, repo, natives):
        self.repo = repo
        self.contenido = repo / 'content' / 'docs'
        self.static = repo / 'static'
        self.natives = natives
        self.paginas = {}  # ruta web (/docs/x/y/) -> archivo de salida

    def salida_de(self, rel):
        rel = Path(rel)
        if rel.as_posix() == '_index.md':
            return SALIDA / 'inicio.md'
        if rel.name == '_index.md':
            return SALIDA / rel.parent / 'README.md'
        return SALIDA / rel

    def registrar(self):
        for md in sorted(self.contenido.rglob('*.md')):
            rel = md.relative_to(self.contenido).as_posix()
            if rel in EXCLUIR:
                registro['omitidas'].append(rel)
                continue
            web = '/docs/' + (rel[:-len('_index.md')] if rel.endswith('_index.md') else rel[:-3] + '/')
            self.paginas[web.rstrip('/') + '/'] = self.salida_de(rel)

    def rel(self, destino, desde):
        return os.path.relpath(destino, desde.parent).replace(os.sep, '/')

    def enlace_interno(self, url, desde):
        """Convierte /docs/..., https://docs.fivem.net/... y /natives/?_0x... en rutas locales."""
        original = url
        u = url
        if not re.match(r'^([a-z][a-z0-9+.-]*:|/|#)', u, re.I) and (desde.parent / u.split('#')[0]).exists():
            return original  # ya es una ruta local válida (p. ej. vídeos descargados)
        if not re.match(r'^([a-z][a-z0-9+.-]*:|/|#)', u, re.I) and u and not u.startswith('{{'):
            # enlace relativo al estilo Hugo: se resuelve contra la URL de la página actual
            from urllib.parse import urljoin
            u = urljoin(self.web_actual, u)
            if u.startswith('/docs/') and not re.search(r'\.[a-z0-9]{2,4}(#|$)', u.split('/')[-1] or 'x/'):
                pass
            elif not u.startswith('/docs/'):
                return original
        if u.startswith(WEB):
            u = u[len(WEB):]
        if u in ('', '/'):
            return self.rel(SALIDA / 'README.md', desde)
        if re.match(r'^/natives/?$', u):
            return self.rel(RAIZ / 'natives' / 'README.md', desde)
        m = re.match(r'^/natives/?\?n_(\w+)$', u)
        if m:
            ns = m.group(1).upper()
            if ns == 'CFX':
                return self.rel(RAIZ / 'natives' / 'README.md', desde) + '#natives-propios-de-fivem-cfx'
            for candidato in (f'{ns}.md', f'{ns}-1.md'):
                if (RAIZ / 'natives' / 'gta5' / candidato).exists():
                    return self.rel(RAIZ / 'natives' / 'gta5' / candidato, desde)
        m = re.match(r'^/natives/?\??#?_?(0x[0-9A-Fa-f]+)', u)
        if m:
            d = self.natives.get(m.group(1).upper())
            if d:
                return self.rel(RAIZ / d[0], desde) + '#' + d[1]
            registro['sin_resolver'].add(original)
            return WEB + u if not original.startswith('http') else original
        if u.startswith('/docs/'):
            ruta, _, ancla = u.partition('#')
            ruta = ruta.split('?')[0]
            if ruta.endswith('.md'):
                ruta = ruta[:-3]
                if ruta.endswith('/_index'):
                    ruta = ruta[:-len('_index')]
            if not ruta.endswith('/'):
                ruta += '/'
            destino = self.paginas.get(ruta)
            if destino:
                return self.rel(destino, desde) + ('#' + ancla if ancla else '')
            registro['sin_resolver'].add(original)
            return WEB + u
        if u.startswith('/') and not u.startswith('//'):
            archivo = self.static / u.lstrip('/').split('?')[0].split('#')[0]
            if archivo.is_file():
                return self.rel(self.copiar(archivo), desde)
            registro['sin_resolver'].add(original)
            return WEB + u
        return original

    def copiar(self, archivo):
        destino = IMAGENES / archivo.relative_to(self.static)
        if not destino.exists():
            destino.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(archivo, destino)
        registro['archivos'].add(destino)
        return destino

    def native(self, nombre, desde):
        d = self.natives.get(nombre) or self.natives.get(nombre.lstrip('_'))
        if not d:
            registro['sin_resolver'].add('native:' + nombre)
            return f'`{nombre}`'
        return f'[`{nombre}`]({self.rel(RAIZ / d[0], desde)}#{d[1]})'

    def alertas(self, t):
        patron = re.compile(r'\{\{([%<])\s*alert([^%>]*)[%>]\}\}(.*?)\{\{[%<]\s*/alert\s*[%>]\}\}', re.S)

        def sustituir(m):
            attrs = dict(re.findall(r'(\w+)="([^"]*)"', m.group(2)))
            tipo = attrs.get('color') or attrs.get('theme') or 'info'
            etiqueta = ETIQUETAS_ALERTA.get(tipo, 'ℹ️ Nota')
            cuerpo = m.group(3).strip()
            lineas = [f'> **{etiqueta}' + (f' — {attrs["title"]}' if attrs.get('title') else '') + '**', '>']
            lineas += [('> ' + l) if l.strip() else '>' for l in cuerpo.splitlines()]
            return '\n'.join(lineas) + '\n'
        return patron.sub(sustituir, t)

    def eventos(self, tipo, desde):
        p = RAIZ / 'datos' / f'eventos_{"cliente" if tipo == "client" else "servidor"}.json'
        h = json.load(open(p, encoding='utf-8'))['content']
        partes = []
        for sec in re.findall(r'<section class="tsd-panel tsd-member[^"]*">(.*?)</section>', h, re.S):
            nombre = re.sub(r'<[^>]+>', '', re.search(r'<h3>(.*?)</h3>', sec, re.S).group(1)).strip()
            firma = re.search(r'<li class="tsd-signature[^"]*">(.*?)</li>', sec, re.S)
            firma = html.unescape(re.sub(r'<[^>]+>', '', firma.group(1))).strip() if firma else ''
            desc = re.search(r'<div class="tsd-comment tsd-typography">(.*?)</div>\s*(?:<h4|</li>)', sec, re.S)
            params = re.findall(r'<h5>(.*?)</h5>\s*(?:<div class="tsd-comment tsd-typography">(.*?)</div>)?', sec, re.S)
            bloque = [f'### {nombre}', '', '```ts', firma, '```', '']
            if desc:
                bloque += [html_a_md(desc.group(1)), '']
            if params:
                bloque.append('**Parámetros**')
                bloque.append('')
                for cab, com in params:
                    cab = html.unescape(re.sub(r'<[^>]+>', '', cab)).strip()
                    com = html_a_md(com).replace('\n', ' ') if com else ''
                    bloque.append(f'- `{cab}`' + (f': {com}' if com else ''))
                bloque.append('')
            partes.append('\n'.join(bloque))
        return '\n'.join(partes)

    def pasos(self, origen_rel, desde):
        carpeta = (self.contenido / origen_rel).parent
        hijos = []
        for md in sorted(carpeta.glob('*.md')):
            if md.name == '_index.md':
                continue
            meta, _ = front_matter(md.read_text(encoding='utf-8'))
            hijos.append((int(meta.get('weight', 999) or 999), meta.get('title', md.stem), meta.get('description', ''), md))
        lineas = []
        for i, (_, titulo, descripcion, md) in enumerate(sorted(hijos), 1):
            destino = self.salida_de(md.relative_to(self.contenido))
            lineas.append(f'{i}. **[{titulo}]({self.rel(destino, desde)})**' + (f' — {descripcion}' if descripcion else ''))
        return '\n'.join(lineas)

    def foro(self, tema):
        try:
            with urllib.request.urlopen(f'https://forum.cfx.re/t/{tema}.json') as r:
                datos = json.load(r)
            post = datos['post_stream']['posts'][0]
            return (f'*Publicación de la comunidad por **{post["username"]}** (foro de Cfx.re, tema {tema}).*\n\n'
                    + html_a_md(post['cooked']))
        except Exception as e:
            registro['sin_resolver'].add(f'forum_topic {tema}: {e}')
            return f'[Tema del foro {tema}](https://forum.cfx.re/t/{tema})'

    def video(self, url, desde):
        nombre = url.rsplit('/', 1)[-1]
        destino = IMAGENES / 'videos' / nombre
        try:
            if not destino.exists():
                destino.parent.mkdir(parents=True, exist_ok=True)
                with urllib.request.urlopen(url) as r, open(destino, 'wb') as f:
                    shutil.copyfileobj(r, f)
            registro['archivos'].add(destino)
            return f'🎬 Vídeo: [{nombre}]({self.rel(destino, desde)}) (copia local de {url})'
        except Exception:
            return f'🎬 Vídeo: {url}'

    def quitar_enhanced(self, texto, rel):
        """Elimina secciones cuyo título es exclusivo de Enhanced y filas de tabla 'Only ... Enhanced'."""
        lineas, salida, saltar_nivel = texto.split('\n'), [], None
        en_codigo = False
        for linea in lineas:
            if linea.lstrip().startswith('```'):
                en_codigo = not en_codigo
            m = None if en_codigo else re.match(r'^(#{1,6})\s+(.*)$', linea)
            if m:
                nivel = len(m.group(1))
                if saltar_nivel is not None and nivel <= saltar_nivel:
                    saltar_nivel = None
                if saltar_nivel is None and re.search(r'enhanced', m.group(2), re.I):
                    saltar_nivel = nivel
                    registro['secciones_enhanced'].append(f'{rel}: {m.group(2).strip()}')
                    continue
            if saltar_nivel is not None:
                continue
            if not en_codigo and linea.lstrip().startswith('|') and re.search(r'(only|exclusive)[^|]*enhanced', linea, re.I):
                registro['secciones_enhanced'].append(f'{rel}: fila «{linea.strip()[:80]}»')
                continue
            salida.append(linea)
        return '\n'.join(salida)

    def convertir(self, md, version):
        rel = md.relative_to(self.contenido).as_posix()
        if rel in EXCLUIR:
            return None
        destino = self.salida_de(rel)
        self.web_actual = '/docs/' + (rel[:-len('_index.md')] if rel.endswith('_index.md') else rel[:-3] + '/')
        meta, t = front_matter(md.read_text(encoding='utf-8'))
        titulo = meta.get('title') or md.stem

        # Ejemplos escapados de shortcodes ({{%/* ... */%}}) → texto literal
        t = re.sub(r'\{\{([%<])/\*\s*(.*?)\s*\*/([%>])\}\}',
                   lambda m: '⦃' + m.group(1) + ' ' + m.group(2) + ' ' + m.group(3) + '⦄', t)
        t = self.alertas(t)
        t = re.sub(r'\{\{%\s*native_link\s+"([^"]+)"\s*%\}\}', lambda m: self.native(m.group(1), destino), t)
        t = re.sub(r'\{\{%\s*article-nav\s*%\}\}', '', t)
        t = re.sub(r'\{\{%\s*rmv2\s*%\}\}', lambda m: (self.static / 'resource_manifest_version2.txt').read_text().strip(), t)
        t = re.sub(r'\{\{%\s*rmv\s*%\}\}', lambda m: (self.static / 'resource_manifest_version.txt').read_text().strip(), t)
        t = re.sub(r'\{\{%\s*code\s+file="([^"]+)"\s+language="([^"]*)"\s*%\}\}',
                   lambda m: f'```{m.group(2)}\n' + (self.repo / m.group(1).lstrip('/')).read_text(encoding='utf-8').replace(
                       '{{RMV}}', (self.static / 'resource_manifest_version.txt').read_text().strip()).rstrip() + '\n```', t)
        t = re.sub(r'\{\{%\s*events\s+"(\w+)"\s*%\}\}', lambda m: self.eventos(m.group(1), destino), t)
        t = re.sub(r'\{\{%\s*steps\s*%\}\}', lambda m: self.pasos(rel, destino), t)
        t = re.sub(r'\{\{%\s*forum_topic\s+"(\d+)"\s*%\}\}', lambda m: self.foro(m.group(1)), t)
        t = re.sub(r'\{\{%\s*youtube\s+id="([^"]+)"\s*%\}\}', r'🎬 Vídeo de YouTube: https://www.youtube.com/watch?v=\1', t)
        t = re.sub(r'\{\{%\s*video\s+src="([^"]+)"\s*%\}\}', lambda m: self.video(m.group(1), destino), t)
        t = t.replace('⦃', '{{').replace('⦄', '}}')

        # Contenedores HTML de idioma (l-lua, l-js, l-cs...): se quitan las etiquetas, se conserva el contenido
        t = re.sub(r'</?div[^>]*>', '', t)
        t = re.sub(r'<span class="l-[^"]*">(.*?)</span>', r'\1', t, flags=re.S)

        # Enlaces e imágenes (solo fuera de los bloques de código)
        trozos = re.split(r'(```.*?```)', t, flags=re.S)
        for i in range(0, len(trozos), 2):
            s = trozos[i]
            s = re.sub(r'(\]\()(\s*)([^)\s]+)', lambda m: m.group(1) + m.group(2) + self.enlace_interno(m.group(3), destino), s)
            s = re.sub(r'^(\[[^\]]+\]:\s*)(\S+)', lambda m: m.group(1) + self.enlace_interno(m.group(2), destino), s, flags=re.M)
            s = re.sub(r'((?:src|href)=")([^"]+)(")', lambda m: m.group(1) + self.enlace_interno(m.group(2), destino) + m.group(3), s)
            trozos[i] = s
        t = ''.join(trozos)

        t = self.quitar_enhanced(t, rel)
        # enlaces a secciones de Enhanced eliminadas → solo texto
        t = re.sub(r'\[([^\]]+)\]\(#[^)]*enhanced[^)]*\)', r'\1', t, flags=re.I)
        if t.count('```') % 2:
            t += '\n```\n'

        web = WEB + '/docs/' + (rel[:-len('_index.md')] if rel.endswith('_index.md') else rel[:-3] + '/')
        cab = [f'# {titulo}', '']
        if meta.get('description'):
            cab += [f'*{meta["description"]}*', '']
        cab += [f'> Fuente original: {web} · repositorio `citizenfx/fivem-docs` @ `{version}` · copiado el {date.today().isoformat()} · '
                f'[índice de la documentación oficial]({self.rel(SALIDA / "README.md", destino)})', '']
        destino.parent.mkdir(parents=True, exist_ok=True)
        destino.write_text('\n'.join(cab) + '\n' + t.strip() + '\n', encoding='utf-8')
        return destino, titulo, meta


def arreglar_anclas(archivos):
    """Corrige anclas que en el original no coinciden por mayúsculas, guiones o guiones bajos."""
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    from comprobar_enlaces import anclas
    norm = lambda a: re.sub(r'[-_]', '', a.lower())
    arregladas = 0
    for md in archivos:
        texto = md.read_text(encoding='utf-8')
        trozos = re.split(r'(```.*?```)', texto, flags=re.S)
        for i in range(0, len(trozos), 2):
            def sustituir(m):
                nonlocal arregladas
                ruta, ancla = m.group(2), m.group(3)
                objetivo = (md.parent / ruta).resolve() if ruta else md
                if not objetivo.exists() or objetivo.suffix != '.md':
                    return m.group(0)
                disponibles = anclas(objetivo)
                if ancla in disponibles:
                    return m.group(0)
                candidatos = [a for a in disponibles if norm(a) == norm(ancla)]
                if len(candidatos) == 1:
                    arregladas += 1
                    return f'{m.group(1)}{ruta}#{candidatos[0]})'
                return m.group(0)
            trozos[i] = re.sub(r'(\]\()([^)#\s]*)#([^)\s]+)\)', sustituir, trozos[i])
        md.write_text(''.join(trozos), encoding='utf-8')
    print('Anclas corregidas:', arregladas)


def indice(conv, paginas, version):
    """README.md de docs-oficiales con el árbol completo de páginas."""
    secciones = {
        'getting-started': 'Primeros pasos: requisitos, instalar FiveM, montar un servidor, primer script.',
        'client-manual': 'Manual del cliente: instalación, comandos de consola, volcados de errores, accesos directos.',
        'server-manual': 'Manual del servidor: instalación (txAdmin y manual), comandos y convars, proxy, Tebex, Escrow, EOS/EOL.',
        'scripting-manual': 'Manual de scripting: recursos, eventos, red, state bags, NUI, voz, runtimes, depuración.',
        'scripting-reference': 'Referencia de scripting: manifest, convars, eventos, OneSync, funciones de Lua/JS/C#.',
        'game-references': 'Referencias del juego: controles, blips, marcadores, modelos de peds/vehículos/armas, data files…',
        'resources': 'Recursos base de cfx-server-data: chat, spawnmanager, mapmanager, sessionmanager, baseevents, txAdmin.',
        'assets-manual': 'Manual de assets: serie para principiantes sobre modelado y streaming.',
        'developers': 'Para desarrolladores: runtimes, sandbox y seguridad del servidor.',
        'fxdk': 'FxDK: entorno de desarrollo de Cfx.re.',
        'cookbook': 'Cookbook: artículos técnicos del blog oficial.',
        'support': 'Soporte: problemas del cliente y del servidor, preguntas frecuentes.',
        'contributing': 'Cómo contribuir a la documentación oficial.',
    }
    lineas = ['# Documentación oficial de FiveM (copia offline)', '',
              f'Copia completa de **docs.fivem.net** convertida a Markdown desde el repositorio `citizenfx/fivem-docs` '
              f'(commit `{version}`, {date.today().isoformat()}). El texto es el **original en inglés, sin modificar**; '
              'los índices están en español.', '',
              '- Los enlaces a natives apuntan a la [referencia local de natives](../natives/README.md).',
              '- Las imágenes y vídeos están en [`_archivos/`](_archivos).',
              '- Solo FiveM Legacy: se han omitido las páginas y secciones exclusivas de *FiveM for GTAV Enhanced* (ver al final).',
              '- Para actualizar: `python3 herramientas/convertir_docs_oficiales.py`.', '']
    por_seccion = {}
    for destino, titulo, meta in paginas:
        rel = destino.relative_to(SALIDA)
        por_seccion.setdefault(rel.parts[0] if len(rel.parts) > 1 else '', []).append((rel, titulo, meta))
    lineas += ['## Secciones', '', '| Sección | Contenido | Páginas |', '|---|---|---|']
    for clave in secciones:
        if clave in por_seccion:
            lineas.append(f'| [{clave}]({clave}/README.md) | {secciones[clave]} | {len(por_seccion[clave])} |')
    lineas += ['', '## Todas las páginas', '']
    for clave in list(secciones) + sorted(k for k in por_seccion if k not in secciones):
        if clave not in por_seccion:
            continue
        lineas += [f'### {clave or "(raíz)"}', '']
        for rel, titulo, meta in sorted(por_seccion[clave], key=lambda x: (len(x[0].parts), x[0].as_posix())):
            sangria = '  ' * max(0, len(rel.parts) - 2 - (1 if rel.name == 'README.md' else 0))
            lineas.append(f'{sangria}- [{titulo}]({rel.as_posix()})')
        lineas.append('')
    lineas += ['## Contenido omitido (exclusivo de FiveM for GTAV Enhanced)', '']
    lineas += [f'- Página `{p}`' for p in registro['omitidas']]
    lineas += [f'- Sección/fila en {s}' for s in registro['secciones_enhanced']]
    lineas.append('')
    (SALIDA / 'README.md').write_text('\n'.join(lineas), encoding='utf-8')


def main():
    repo = cargar_repo()
    version = commit(repo)
    if SALIDA.exists():
        shutil.rmtree(SALIDA)
    SALIDA.mkdir()
    conv = Convertidor(repo, mapa_natives())
    conv.registrar()
    paginas = []
    for md in sorted(conv.contenido.rglob('*.md')):
        r = conv.convertir(md, version)
        if r and r[0] != SALIDA / 'README.md':
            paginas.append(r)
    arreglar_anclas([d for d, *_ in paginas])
    indice(conv, paginas, version)
    print(f'{len(paginas)} páginas · {len(registro["archivos"])} archivos multimedia · '
          f'{len(registro["omitidas"])} páginas omitidas · {len(registro["secciones_enhanced"])} secciones/filas Enhanced quitadas')
    if registro['sin_resolver']:
        print('Sin resolver (se dejan con enlace web):')
        for s in sorted(registro['sin_resolver']):
            print('  ', s)


if __name__ == '__main__':
    main()
