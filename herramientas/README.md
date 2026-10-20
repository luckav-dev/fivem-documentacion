# Herramientas

[← Inicio del repositorio](../README.md)

Scripts en Python 3 (solo biblioteca estándar) para regenerar y comprobar el contenido del repositorio. Se ejecutan desde la raíz del repositorio.

| Script | Qué hace | Uso |
|---|---|---|
| [`generar_natives.py`](generar_natives.py) | Genera [`natives/`](../natives/README.md) desde `datos/natives.json` y `datos/natives_cfx.json`: una página por namespace (dividida si pasa de ~320 KB), natives CFX por lado e índice alfabético. Las firmas Lua siguen las reglas del generador oficial de FiveM (`codegen_out_lua.lua`). | `python3 herramientas/generar_natives.py` · con `--descargar` baja antes las bases de datos actuales |
| [`convertir_docs_oficiales.py`](convertir_docs_oficiales.py) | Convierte el repositorio `citizenfx/fivem-docs` (Hugo) en Markdown para GitHub en [`docs-oficiales/`](../docs-oficiales/README.md): *shortcodes*, enlaces internos, enlaces a natives, imágenes, vídeos y listas de eventos. Omite lo exclusivo de FiveM for GTAV Enhanced. | `python3 herramientas/convertir_docs_oficiales.py [ruta_a_fivem-docs]` (sin ruta, lo clona en `.cache/`) |
| [`comprobar_enlaces.py`](comprobar_enlaces.py) | Comprueba que todos los enlaces relativos y anclas de los `.md` existen (anclas calculadas como en GitHub). | `python3 herramientas/comprobar_enlaces.py [carpeta ...]` |

## Actualizar todo

```bash
python3 herramientas/generar_natives.py --descargar
curl -sS -o datos/eventos_cliente.json https://runtime.fivem.net/doc/events/client.html.json
curl -sS -o datos/eventos_servidor.json https://runtime.fivem.net/doc/events/server.html.json
rm -rf .cache/fivem-docs && python3 herramientas/convertir_docs_oficiales.py
python3 herramientas/comprobar_enlaces.py
```

El orden importa: `convertir_docs_oficiales.py` usa el índice de `natives/` para enlazar los natives.
