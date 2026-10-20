# 📚 FiveM (Legacy): documentación completa y offline

Todo lo necesario para montar, programar y mantener servidores de **FiveM Legacy** (FiveM clásico con FXServer) **sin depender de internet**:

- una **guía completa en español**;
- **todos los natives** con su descripción oficial;
- la **documentación oficial** de docs.fivem.net al completo, con imágenes y vídeos;
- la documentación de los **frameworks y herramientas** más usados;
- los **datos en bruto** y los **scripts** para actualizarlo todo.

> Actualizado el **20 de octubre de 2026**. No incluye nada de *FiveM for GTAV Enhanced*. De dónde sale cada contenido y en qué condiciones: [FUENTES.md](FUENTES.md). Cambios: [HISTORIAL.md](HISTORIAL.md).

## Qué hay en cada carpeta

| Carpeta / archivo | Qué contiene | Idioma |
|---|---|---|
| 📘 [`guia/`](guia/README.md) | **Guía completa en español** en 31 capítulos: instalación, `server.cfg`, convars, permisos, recursos, Lua/JS/C#, natives, OneSync, NUI, streaming, base de datos, frameworks (incluido cómo crear uno propio), voz, seguridad, rendimiento, depuración, txAdmin, hosting, tutorial, chuleta y FAQ. Verificada contra el código fuente de FiveM. | Español |
| 🧩 [`natives/`](natives/README.md) | **Referencia de todos los natives**: 6.436 de GTA V (44 namespaces) y 942 propios de FiveM (CFX), con firma Lua, declaración C, parámetros, valor devuelto, descripción oficial, alias y ejemplos. Incluye un índice alfabético. | Índices en español, descripciones oficiales en inglés |
| 📖 [`docs-oficiales/`](docs-oficiales/README.md) | **Copia completa de docs.fivem.net** (334 páginas): manuales de cliente, servidor, scripting y assets, referencia de scripting (manifest, convars, eventos, OneSync, funciones de Lua/JS/C#), referencias del juego (controles, blips, marcadores, modelos de peds/vehículos/armas, colores, data files…), recursos base, cookbook y soporte. Con todas sus imágenes y los vídeos tutoriales. | Inglés (original), índices en español |
| 🧰 [`docs-terceros/`](docs-terceros/README.md) | Documentación de **Overextended** (ox_lib, oxmysql, ox_inventory, ox_target, ox_core…), **txAdmin**, **Qbox**, **QBCore**, **ESX** y **pma-voice**. | Inglés (original), índices en español |
| 🗃️ [`datos/`](datos/README.md) | Bases de datos oficiales en bruto: `natives.json`, `natives_cfx.json`, listas de eventos y natives RPC. | — |
| 🛠️ [`herramientas/`](herramientas/README.md) | Scripts para **actualizar** natives y documentación oficial, y para **comprobar** todos los enlaces. | Español |
| [`FUENTES.md`](FUENTES.md) | Origen, autoría y condiciones de uso de cada contenido. | Español |
| [`HISTORIAL.md`](HISTORIAL.md) | Historial de cambios del repositorio. | Español |

## Por dónde empezar

| Quiero… | Ve a |
|---|---|
| Aprender FiveM desde cero | [Guía → capítulos 1 a 7](guia/README.md) y luego el [tutorial](guia/27-tutorial-recurso-tienda.md) |
| Instalar un servidor | [Guía 3: instalación](guia/03-instalacion-servidor.md) · [Guía 4: server.cfg](guia/04-server-cfg.md) · [Oficial: txAdmin](docs-oficiales/server-manual/setting-up-a-server-txadmin.md) |
| Programar mi primer script | [Guía 8: fundamentos](guia/08-scripting-fundamentos.md) · [Guía 9: Lua](guia/09-lua.md) · [Oficial: primer script](docs-oficiales/scripting-manual/introduction/creating-your-first-script.md) |
| Buscar qué hace un native | [Índice alfabético de natives](natives/README.md#índice-alfabético) o `grep -rn "NombreDelNative" natives/` |
| Saber qué natives existen en el servidor | [Natives CFX de servidor](natives/cfx/servidor.md) · [compartidos](natives/cfx/compartidos.md) |
| Hacer una interfaz (NUI) | [Guía 14: NUI](guia/14-nui.md) · [Oficial: NUI](docs-oficiales/scripting-manual/nui-development/README.md) |
| Crear mi propio framework | [Guía 17.6: framework propio](guia/17-frameworks.md#176-crear-tu-propio-framework) |
| Usar ox_lib / oxmysql / ox_inventory | [docs-terceros/overextended](docs-terceros/overextended/README.md) |
| Consultar un comando o convar del servidor | [Guía 5](guia/05-comandos-y-convars.md) · [Oficial: server commands](docs-oficiales/server-manual/server-commands.md) |
| Ver controles, blips, marcadores o modelos | [Oficial: game references](docs-oficiales/game-references/README.md) |
| Proteger mi servidor | [Guía 19: seguridad](guia/19-seguridad.md) · [Oficial: server security](docs-oficiales/developers/server-security.md) |
| Resolver un error | [Guía 21: depuración](guia/21-depuracion.md) · [Oficial: soporte](docs-oficiales/support/README.md) |
| Una respuesta rápida | [Chuleta](guia/28-chuleta.md) · [FAQ](guia/29-faq.md) · [Glosario](guia/30-glosario.md) |

## Guía en español: capítulos

| # | Capítulo | De qué trata |
|---|---|---|
| 1 | [Introducción](guia/01-introduccion.md) | Qué es FiveM, historia, ecosistema Cfx.re. |
| 2 | [Conceptos fundamentales](guia/02-conceptos-fundamentales.md) | Cliente/servidor, recursos, natives, OneSync, game build, runtimes, identificadores. |
| 3 | [Instalación del servidor](guia/03-instalacion-servidor.md) | Requisitos, clave, artefactos (EOS/EOL), Windows, Linux, puertos, actualizar. |
| 4 | [server.cfg](guia/04-server-cfg.md) | `set`/`sets`/`setr`, archivo completo comentado, colores, orden de carga. |
| 5 | [Comandos y convars](guia/05-comandos-y-convars.md) | Referencia completa, *rate limiters*, game builds, pools. |
| 6 | [Permisos ACE](guia/06-permisos-ace.md) | Principals, objetos, herencia, uso desde scripts. |
| 7 | [Recursos y fxmanifest](guia/07-recursos-y-fxmanifest.md) | Estructura, todas las directivas, ciclo de vida. |
| 8 | [Scripting: fundamentos](guia/08-scripting-fundamentos.md) | Threads, eventos, callbacks, exports, comandos, teclas, KVP, HTTP, deferrals. |
| 9 | [Lua (CfxLua 5.4)](guia/09-lua.md) | Cambios respecto a 5.3, extensiones, vectores y la referencia completa del runtime. |
| 10 | [JavaScript y TypeScript](guia/10-javascript-typescript.md) | API, diferencias con Lua, tipos, esbuild. |
| 11 | [C#](guia/11-csharp.md) | Proyecto, BaseScript, plantillas, Mono. |
| 12 | [Natives: guía práctica](guia/12-natives-guia-practica.md) | Jugador, vehículos, entidades, blips, marcadores, cámaras, armas… |
| 13 | [Red, OneSync, state bags y buckets](guia/13-red-onesync-statebags-buckets.md) | Sincronización, *scopes*, *entity lockdown*, state bags, dimensiones. |
| 14 | [NUI](guia/14-nui.md) | Interfaces web, callbacks, React/Vite, pantallas de carga, DUI, qué soporta el navegador. |
| 15 | [Streaming de assets](guia/15-streaming-assets.md) | Vehículos, mapas, MLOs, ropa, armas, `data_file`. |
| 16 | [Base de datos](guia/16-base-de-datos.md) | MariaDB y oxmysql. |
| 17 | [Frameworks](guia/17-frameworks.md) | ESX, QBCore, Qbox, ox y cómo **crear tu propio framework**. |
| 18 | [Voz](guia/18-voz.md) | pma-voice y natives de Mumble. |
| 19 | [Seguridad](guia/19-seguridad.md) | Validación, convars, eventos de juego, *honeypots*, bans. |
| 20 | [Rendimiento](guia/20-rendimiento.md) | resmon, profiler, buenas prácticas en cliente y servidor. |
| 21 | [Depuración](guia/21-depuracion.md) | Logs y errores frecuentes con su solución. |
| 22 | [Cliente FiveM](guia/22-cliente-fivem.md) | Carpetas, caché, opciones de lanzamiento, consola F8. |
| 23 | [Monetización y legal](guia/23-monetizacion-y-legal.md) | PLA, Tebex, Asset Escrow. |
| 24 | [txAdmin](guia/24-txadmin.md) | Funciones, `TXHOST_*`, convars del menú, eventos. |
| 25 | [Hosting y despliegue](guia/25-hosting-y-despliegue.md) | Opciones, flujo con git, proxy y CDN, mantenimiento. |
| 26 | [Buenas prácticas](guia/26-buenas-practicas.md) | Nombres, configuración, locales, versionado, checklist. |
| 27 | [Tutorial: recurso tienda](guia/27-tutorial-recurso-tienda.md) | Recurso completo de principio a fin. |
| 28 | [Chuleta](guia/28-chuleta.md) | Lo más usado en una página. |
| 29 | [FAQ](guia/29-faq.md) | Preguntas frecuentes. |
| 30 | [Glosario](guia/30-glosario.md) | Términos. |
| 31 | [Enlaces](guia/31-enlaces.md) | Webs oficiales y del ecosistema. |

## Natives

| Tipo | Natives | Dónde |
|---|---|---|
| FiveM (CFX), cliente y servidor | 98 | [natives/cfx/compartidos.md](natives/cfx/compartidos.md) |
| FiveM (CFX), solo servidor | 290 | [natives/cfx/servidor.md](natives/cfx/servidor.md) |
| FiveM (CFX), solo cliente | 554 | [parte 1](natives/cfx/cliente-1.md) · [parte 2](natives/cfx/cliente-2.md) |
| GTA V | 6.436 en 44 namespaces | [natives/README.md](natives/README.md#natives-de-gta-v-por-namespace) |

Namespaces de GTA V: [APP](natives/gta5/APP.md) · [AUDIO](natives/gta5/AUDIO.md) · [BRAIN](natives/gta5/BRAIN.md) · [CAM](natives/gta5/CAM.md) · [CLOCK](natives/gta5/CLOCK.md) · [CUTSCENE](natives/gta5/CUTSCENE.md) · [DATAFILE](natives/gta5/DATAFILE.md) · [DECORATOR](natives/gta5/DECORATOR.md) · [DLC](natives/gta5/DLC.md) · [ENTITY](natives/gta5/ENTITY.md) · [EVENT](natives/gta5/EVENT.md) · [FILES](natives/gta5/FILES.md) · [FIRE](natives/gta5/FIRE.md) · [GRAPHICS](natives/gta5/GRAPHICS.md) · [HUD](natives/gta5/HUD.md) · [INTERIOR](natives/gta5/INTERIOR.md) · [ITEMSET](natives/gta5/ITEMSET.md) · [LOADINGSCREEN](natives/gta5/LOADINGSCREEN.md) · [LOCALIZATION](natives/gta5/LOCALIZATION.md) · [MISC](natives/gta5/MISC.md) · [MOBILE](natives/gta5/MOBILE.md) · [MONEY](natives/gta5/MONEY.md) · [NETSHOPPING](natives/gta5/NETSHOPPING.md) · [NETWORK](natives/gta5/NETWORK-1.md) · [OBJECT](natives/gta5/OBJECT.md) · [PAD](natives/gta5/PAD.md) · [PATHFIND](natives/gta5/PATHFIND.md) · [PED](natives/gta5/PED-1.md) · [PHYSICS](natives/gta5/PHYSICS.md) · [PLAYER](natives/gta5/PLAYER.md) · [RECORDING](natives/gta5/RECORDING.md) · [REPLAY](natives/gta5/REPLAY.md) · [SAVEMIGRATION](natives/gta5/SAVEMIGRATION.md) · [SCRIPT](natives/gta5/SCRIPT.md) · [SHAPETEST](natives/gta5/SHAPETEST.md) · [SOCIALCLUB](natives/gta5/SOCIALCLUB.md) · [STATS](natives/gta5/STATS.md) · [STREAMING](natives/gta5/STREAMING.md) · [SYSTEM](natives/gta5/SYSTEM.md) · [TASK](natives/gta5/TASK.md) · [VEHICLE](natives/gta5/VEHICLE-1.md) · [WATER](natives/gta5/WATER.md) · [WEAPON](natives/gta5/WEAPON.md) · [ZONE](natives/gta5/ZONE.md)

## Documentación oficial (docs.fivem.net)

| Sección | Contenido | Páginas |
|---|---|---|
| [getting-started](docs-oficiales/getting-started/README.md) | Primeros pasos: requisitos, instalar FiveM, montar un servidor, primer script (con vídeos). | 5 |
| [client-manual](docs-oficiales/client-manual/README.md) | Cliente: instalación, comandos de consola, volcados de errores, accesos directos. | 9 |
| [server-manual](docs-oficiales/server-manual/README.md) | Servidor: instalación con txAdmin y manual, comandos y convars, proxy, Tebex, Escrow, EOS/EOL. | 15 |
| [scripting-manual](docs-oficiales/scripting-manual/README.md) | Scripting: recursos, eventos, red, state bags, NUI, voz, runtimes, depuración, scaleform. | 46 |
| [scripting-reference](docs-oficiales/scripting-reference/README.md) | Referencia: manifest, convars, eventos, OneSync, funciones de Lua, JS y C#. | 105 |
| [game-references](docs-oficiales/game-references/README.md) | Juego: controles, blips, marcadores, checkpoints, modelos de peds/vehículos/armas, colores, zonas, data files, eventos de juego. | 50 |
| [resources](docs-oficiales/resources/README.md) | Recursos base: chat, spawnmanager, mapmanager, sessionmanager, baseevents, txAdmin. | 52 |
| [assets-manual](docs-oficiales/assets-manual/README.md) | Assets: serie para principiantes. | 10 |
| [developers](docs-oficiales/developers/README.md) | Runtimes, sandbox y seguridad del servidor. | 4 |
| [fxdk](docs-oficiales/fxdk/README.md) | FxDK, el entorno de desarrollo de Cfx.re. | 5 |
| [cookbook](docs-oficiales/cookbook/README.md) | Artículos técnicos del blog oficial. | 21 |
| [support](docs-oficiales/support/README.md) | Soporte y preguntas frecuentes. | 6 |
| [contributing](docs-oficiales/contributing/README.md) | Cómo contribuir a la documentación oficial. | 5 |

Índice con todas las páginas: [docs-oficiales/README.md](docs-oficiales/README.md#todas-las-páginas).

## Documentación de terceros

| Proyecto | Qué contiene | Páginas | Dónde |
|---|---|---|---|
| Overextended | ox_lib, oxmysql, ox_inventory, ox_target, ox_core, ox_doorlock, ox_fuel y guías | 127 | [docs-terceros/overextended](docs-terceros/overextended/README.md) |
| txAdmin | Menú in-game, permisos, eventos, recetas, variables de entorno, logs | 13 | [docs-terceros/txadmin](docs-terceros/txadmin/README.md) |
| Qbox | qbx_core y recursos qbx_*, Dashboard, Tebex y blog | 83 | [docs-terceros/qbox](docs-terceros/qbox/README.md) |
| QBCore | Guías, referencia de qb-core y recursos qb-* | 84 | [docs-terceros/qbcore](docs-terceros/qbcore/README.md) |
| ESX Legacy | es_extended, recursos del núcleo, addons esx_* y tutoriales | 82 | [docs-terceros/esx](docs-terceros/esx/README.md) |
| pma-voice | Convars, exports, eventos y state bags del sistema de voz | 19 | [docs-terceros/pma-voice](docs-terceros/pma-voice/README.md) |

Índice general: [docs-terceros/README.md](docs-terceros/README.md).

## Buscar sin internet

Clona el repositorio una vez (`git clone …`) y busca en local:

```bash
# ¿Qué hace un native?
grep -rn "^### SetEntityCoords$" -A 40 natives/

# Natives que mencionan algo en su descripción
grep -rln "routing bucket" natives/ docs-oficiales/

# Buscar en toda la documentación (insensible a mayúsculas)
grep -rni "sv_entityLockdown" guia/ docs-oficiales/ docs-terceros/
```

En VS Code: abre la carpeta y usa la búsqueda global (`Ctrl+Shift+F`). La vista previa de Markdown (`Ctrl+Shift+V`) muestra las imágenes locales.

## Mantenerlo actualizado

Ver [herramientas/README.md](herramientas/README.md). En resumen:

```bash
python3 herramientas/generar_natives.py --descargar     # natives
python3 herramientas/convertir_docs_oficiales.py         # documentación oficial
python3 herramientas/comprobar_enlaces.py                # comprobar que no hay enlaces rotos
```
