# 📘 Guía de FiveM (Legacy) en español — Edición 2026

> **Guía en español, en un único archivo, de todo lo que necesitas para montar, programar, asegurar y mantener un servidor de FiveM.**
> Actualizada a **20 de octubre de 2026**. Cubre **exclusivamente FiveM Legacy** (FiveM clásico sobre GTA V Legacy con **FXServer**).

| Dato clave (oct. 2026) | Valor |
|---|---|
| Artefacto de servidor *recommended* / *latest* | **35245** / 37579 (mínimo para poder conectarse: **35245**) |
| Game build más reciente | **3889** — *The Kortz Center Heist* (`mp2026_01`) |
| Lua | **CfxLua 5.4.8** (Lua 5.3 eliminado en julio de 2025) |
| Node.js (servidor) | 16 por defecto, **22** con `node_version '22'` |
| txAdmin | **8.1.1** |
| Frameworks | ESX Legacy **1.16.4** · Qbox **1.24.0** · QBCore 1.3.0 · ox_core 1.5.14 |
| Librerías Overextended | ox_lib **3.40.x** · oxmysql **2.14.x** · ox_inventory **2.48.x** · ox_target 1.18.x |
| Base de datos recomendada | MariaDB **11.4 LTS** u **11.8 LTS** |
| Licencia de plataforma | Creator Platform License Agreement (actualizado el 10/09/2026) |

**Cómo usar este documento**

- Si empiezas de cero: lee en orden las secciones **1 → 7**, luego el **tutorial (27)**.
- Si ya programas: ve directo a **8-15** (scripting, natives, red, NUI, streaming) y **19-20** (seguridad y rendimiento).
- Si administras un servidor: **3-6**, **16-18**, **21-25**.
- ¿Prisa? **Chuleta (28)** y **FAQ (29)**.
- Referencias exhaustivas: **runtime Lua (9.9)**, **navegador NUI (14.11)**, **framework propio (17.6)** y **todos los natives** ([../natives/](../natives/README.md)).
- Los ejemplos de código están en **Lua** salvo que se indique otro lenguaje.
- **Funciones de ejemplo**: las funciones con nombre en español (`AbrirTienda`, `DarItem`, `QuitarDinero`, `LogSospechoso`…) representan **tu** lógica y debes implementarlas tú. Todo lo demás está verificado.

**Cómo se ha verificado este documento**

- Cada llamada a un native en los ejemplos Lua y JavaScript se ha comprobado automáticamente contra la **base de datos oficial de natives** (`natives.json` y `natives_cfx.json`): que exista y que lleve el **número de argumentos** correcto.
- El runtime Lua, los eventos de OneSync y el navegador NUI se han contrastado con el **código fuente de FiveM** (`citizenfx/fivem`, build 37579).
- Las APIs de ox_lib, ox_inventory, ox_target, ESX, QBCore, Qbox y pma-voice se han contrastado con **sus repositorios oficiales**.
- Lo que no se ha podido confirmar en una fuente oficial aparece marcado como tal en el texto.

[← Inicio del repositorio](../README.md)

## Capítulos

| # | Capítulo | Archivo |
|---|---|---|
| 1 | [Introducción](01-introduccion.md) | `01-introduccion.md` |
| 2 | [Conceptos fundamentales](02-conceptos-fundamentales.md) | `02-conceptos-fundamentales.md` |
| 3 | [Instalación y puesta en marcha del servidor](03-instalacion-servidor.md) | `03-instalacion-servidor.md` |
| 4 | [server.cfg a fondo](04-server-cfg.md) | `04-server-cfg.md` |
| 5 | [Comandos de consola y convars (referencia completa)](05-comandos-y-convars.md) | `05-comandos-y-convars.md` |
| 6 | [Permisos: sistema ACE](06-permisos-ace.md) | `06-permisos-ace.md` |
| 7 | [Recursos y fxmanifest.lua](07-recursos-y-fxmanifest.md) | `07-recursos-y-fxmanifest.md` |
| 8 | [Scripting: fundamentos comunes (todos los lenguajes)](08-scripting-fundamentos.md) | `08-scripting-fundamentos.md` |
| 9 | [Lua en FiveM (CfxLua 5.4)](09-lua.md) | `09-lua.md` |
| 10 | [JavaScript y TypeScript](10-javascript-typescript.md) | `10-javascript-typescript.md` |
| 11 | [C# (.NET / Mono)](11-csharp.md) | `11-csharp.md` |
| 12 | [Natives: guía práctica](12-natives-guia-practica.md) | `12-natives-guia-practica.md` |
| 13 | [Red, OneSync, State Bags y Routing Buckets](13-red-onesync-statebags-buckets.md) | `13-red-onesync-statebags-buckets.md` |
| 14 | [NUI (interfaces web dentro del juego)](14-nui.md) | `14-nui.md` |
| 15 | [Streaming de assets (vehículos, mapas, ropa, armas…)](15-streaming-assets.md) | `15-streaming-assets.md` |
| 16 | [Base de datos (MariaDB + oxmysql)](16-base-de-datos.md) | `16-base-de-datos.md` |
| 17 | [Frameworks](17-frameworks.md) | `17-frameworks.md` |
| 18 | [Voz: pma-voice y Mumble](18-voz.md) | `18-voz.md` |
| 19 | [Seguridad y anti-cheat](19-seguridad.md) | `19-seguridad.md` |
| 20 | [Rendimiento y optimización](20-rendimiento.md) | `20-rendimiento.md` |
| 21 | [Depuración y errores comunes](21-depuracion.md) | `21-depuracion.md` |
| 22 | [El cliente FiveM](22-cliente-fivem.md) | `22-cliente-fivem.md` |
| 23 | [Monetización, legalidad y Asset Escrow](23-monetizacion-y-legal.md) | `23-monetizacion-y-legal.md` |
| 24 | [txAdmin a fondo](24-txadmin.md) | `24-txadmin.md` |
| 25 | [Hosting, despliegue y operación](25-hosting-y-despliegue.md) | `25-hosting-y-despliegue.md` |
| 26 | [Buenas prácticas de desarrollo](26-buenas-practicas.md) | `26-buenas-practicas.md` |
| 27 | [Tutorial completo: recurso "tienda" de principio a fin](27-tutorial-recurso-tienda.md) | `27-tutorial-recurso-tienda.md` |
| 28 | [Chuleta rápida (*cheat sheet*)](28-chuleta.md) | `28-chuleta.md` |
| 29 | [Preguntas frecuentes (FAQ)](29-faq.md) | `29-faq.md` |
| 30 | [Glosario](30-glosario.md) | `30-glosario.md` |
| 31 | [Enlaces oficiales y recursos](31-enlaces.md) | `31-enlaces.md` |

## Contenido detallado

- **[1. Introducción](01-introduccion.md)**
  - [1.1 ¿Qué es FiveM?](01-introduccion.md#11-qué-es-fivem)
  - [1.2 Historia resumida](01-introduccion.md#12-historia-resumida)
  - [1.3 Ecosistema Cfx.re](01-introduccion.md#13-ecosistema-cfxre)
- **[2. Conceptos fundamentales](02-conceptos-fundamentales.md)**
  - [2.1 Arquitectura cliente-servidor](02-conceptos-fundamentales.md#21-arquitectura-cliente-servidor)
  - [2.2 Recursos (*resources*)](02-conceptos-fundamentales.md#22-recursos-resources)
  - [2.3 Lado cliente, lado servidor y "shared"](02-conceptos-fundamentales.md#23-lado-cliente-lado-servidor-y-shared)
  - [2.4 Natives](02-conceptos-fundamentales.md#24-natives)
  - [2.5 OneSync](02-conceptos-fundamentales.md#25-onesync)
  - [2.6 Game build](02-conceptos-fundamentales.md#26-game-build)
  - [2.7 Runtimes de scripting](02-conceptos-fundamentales.md#27-runtimes-de-scripting)
  - [2.8 Identificadores de jugador](02-conceptos-fundamentales.md#28-identificadores-de-jugador)
  - [2.9 Glosario rápido de esta sección](02-conceptos-fundamentales.md#29-glosario-rápido-de-esta-sección)
- **[3. Instalación y puesta en marcha del servidor](03-instalacion-servidor.md)**
  - [3.1 Requisitos](03-instalacion-servidor.md#31-requisitos)
  - [3.2 Obtener una clave de servidor (*license key*)](03-instalacion-servidor.md#32-obtener-una-clave-de-servidor-license-key)
  - [3.3 Descargar los artefactos (FXServer)](03-instalacion-servidor.md#33-descargar-los-artefactos-fxserver)
  - [3.4 Estructura de carpetas recomendada](03-instalacion-servidor.md#34-estructura-de-carpetas-recomendada)
  - [3.5 Instalación en Windows (con txAdmin, recomendado)](03-instalacion-servidor.md#35-instalación-en-windows-con-txadmin-recomendado)
  - [3.6 Instalación en Windows (manual, sin txAdmin)](03-instalacion-servidor.md#36-instalación-en-windows-manual-sin-txadmin)
  - [3.7 Instalación en Linux](03-instalacion-servidor.md#37-instalación-en-linux)
  - [3.8 Puertos y firewall](03-instalacion-servidor.md#38-puertos-y-firewall)
  - [3.9 Conectarse al servidor](03-instalacion-servidor.md#39-conectarse-al-servidor)
  - [3.10 Actualizar el servidor (artefactos)](03-instalacion-servidor.md#310-actualizar-el-servidor-artefactos)
  - [3.11 Recursos base de cfx-server-data](03-instalacion-servidor.md#311-recursos-base-de-cfx-server-data)
- **[4. server.cfg a fondo](04-server-cfg.md)**
  - [4.1 set, sets, setr y exec](04-server-cfg.md#41-set-sets-setr-y-exec)
  - [4.2 server.cfg completo y comentado](04-server-cfg.md#42-servercfg-completo-y-comentado)
  - [4.3 Colores en el nombre del servidor](04-server-cfg.md#43-colores-en-el-nombre-del-servidor)
  - [4.4 Orden de carga y dependencias](04-server-cfg.md#44-orden-de-carga-y-dependencias)
- **[5. Comandos de consola y convars (referencia completa)](05-comandos-y-convars.md)**
  - [5.1 Comandos de recursos](05-comandos-y-convars.md#51-comandos-de-recursos)
  - [5.2 Comandos globales y de gestión](05-comandos-y-convars.md#52-comandos-globales-y-de-gestión)
  - [5.3 Convars de configuración](05-comandos-y-convars.md#53-convars-de-configuración)
  - [5.4 Game builds (sv_enforceGameBuild)](05-comandos-y-convars.md#54-game-builds-sv_enforcegamebuild)
  - [5.5 Pools (increase_pool_size)](05-comandos-y-convars.md#55-pools-increase_pool_size)
- **[6. Permisos: sistema ACE](06-permisos-ace.md)**
  - [6.1 Conceptos](06-permisos-ace.md#61-conceptos)
  - [6.2 Comandos](06-permisos-ace.md#62-comandos)
  - [6.3 Ejemplo de jerarquía completa](06-permisos-ace.md#63-ejemplo-de-jerarquía-completa)
  - [6.4 Usar ACE desde scripts](06-permisos-ace.md#64-usar-ace-desde-scripts)
- **[7. Recursos y fxmanifest.lua](07-recursos-y-fxmanifest.md)**
  - [7.1 Estructura típica de un recurso](07-recursos-y-fxmanifest.md#71-estructura-típica-de-un-recurso)
  - [7.2 fxmanifest.lua mínimo](07-recursos-y-fxmanifest.md#72-fxmanifestlua-mínimo)
  - [7.3 fxmanifest.lua completo con todas las directivas habituales](07-recursos-y-fxmanifest.md#73-fxmanifestlua-completo-con-todas-las-directivas-habituales)
  - [7.4 Referencia de directivas](07-recursos-y-fxmanifest.md#74-referencia-de-directivas)
  - [7.5 Prefijo @ y rutas](07-recursos-y-fxmanifest.md#75-prefijo--y-rutas)
  - [7.6 Metadatos desde código](07-recursos-y-fxmanifest.md#76-metadatos-desde-código)
  - [7.7 Ciclo de vida de un recurso](07-recursos-y-fxmanifest.md#77-ciclo-de-vida-de-un-recurso)
  - [7.8 Funciones de gestión de recursos (servidor)](07-recursos-y-fxmanifest.md#78-funciones-de-gestión-de-recursos-servidor)
- **[8. Scripting: fundamentos comunes (todos los lenguajes)](08-scripting-fundamentos.md)**
  - [8.1 Hilos (*threads*), Wait y el planificador](08-scripting-fundamentos.md#81-hilos-threads-wait-y-el-planificador)
  - [8.2 Eventos](08-scripting-fundamentos.md#82-eventos)
  - [8.3 Patrón *callback* (petición/respuesta cliente⇄servidor)](08-scripting-fundamentos.md#83-patrón-callback-peticiónrespuesta-clienteservidor)
  - [8.4 Exports](08-scripting-fundamentos.md#84-exports)
  - [8.5 Referencias a funciones](08-scripting-fundamentos.md#85-referencias-a-funciones)
  - [8.6 Comandos](08-scripting-fundamentos.md#86-comandos)
  - [8.7 Teclas: RegisterKeyMapping](08-scripting-fundamentos.md#87-teclas-registerkeymapping)
  - [8.8 Controles del juego](08-scripting-fundamentos.md#88-controles-del-juego)
  - [8.9 Convars desde scripts](08-scripting-fundamentos.md#89-convars-desde-scripts)
  - [8.10 KVP (almacenamiento clave-valor)](08-scripting-fundamentos.md#810-kvp-almacenamiento-clave-valor)
  - [8.11 HTTP: peticiones salientes y endpoints propios](08-scripting-fundamentos.md#811-http-peticiones-salientes-y-endpoints-propios)
  - [8.12 Utilidades comunes](08-scripting-fundamentos.md#812-utilidades-comunes)
  - [8.13 Eventos del sistema más importantes](08-scripting-fundamentos.md#813-eventos-del-sistema-más-importantes)
  - [8.14 Conexión de jugadores: playerConnecting y *deferrals*](08-scripting-fundamentos.md#814-conexión-de-jugadores-playerconnecting-y-deferrals)
  - [8.15 Funciones de jugador en el servidor](08-scripting-fundamentos.md#815-funciones-de-jugador-en-el-servidor)
- **[9. Lua en FiveM (CfxLua 5.4)](09-lua.md)**
  - [9.1 Qué Lua usa FiveM](09-lua.md#91-qué-lua-usa-fivem)
  - [9.2 Cambios de 5.3 → 5.4 que pueden romper scripts antiguos](09-lua.md#92-cambios-de-53--54-que-pueden-romper-scripts-antiguos)
  - [9.3 Extensiones de sintaxis de CfxLua](09-lua.md#93-extensiones-de-sintaxis-de-cfxlua)
  - [9.4 Vectores y cuaterniones](09-lua.md#94-vectores-y-cuaterniones)
  - [9.5 Librerías y globales integradas](09-lua.md#95-librerías-y-globales-integradas)
  - [9.6 Estilo y buenas prácticas en Lua](09-lua.md#96-estilo-y-buenas-prácticas-en-lua)
  - [9.7 Módulos y organización](09-lua.md#97-módulos-y-organización)
  - [9.8 Autocompletado en el editor (VS Code)](09-lua.md#98-autocompletado-en-el-editor-vs-code)
  - [9.9 Referencia completa del runtime Lua (verificada en el código fuente)](09-lua.md#99-referencia-completa-del-runtime-lua-verificada-en-el-código-fuente)
- **[10. JavaScript y TypeScript](10-javascript-typescript.md)**
  - [10.1 Entornos](10-javascript-typescript.md#101-entornos)
  - [10.2 Manifest](10-javascript-typescript.md#102-manifest)
  - [10.3 API básica](10-javascript-typescript.md#103-api-básica)
  - [10.4 Diferencias importantes respecto a Lua](10-javascript-typescript.md#104-diferencias-importantes-respecto-a-lua)
  - [10.5 TypeScript con tipos oficiales](10-javascript-typescript.md#105-typescript-con-tipos-oficiales)
  - [10.6 Servidor: async, base de datos y npm](10-javascript-typescript.md#106-servidor-async-base-de-datos-y-npm)
- **[11. C# (.NET / Mono)](11-csharp.md)**
  - [11.1 Proyecto](11-csharp.md#111-proyecto)
  - [11.2 Script básico](11-csharp.md#112-script-básico)
  - [11.3 Conceptos](11-csharp.md#113-conceptos)
  - [11.4 Plantillas oficiales](11-csharp.md#114-plantillas-oficiales)
- **[12. Natives: guía práctica](12-natives-guia-practica.md)**
  - [12.1 Cómo leer la referencia de natives](12-natives-guia-practica.md#121-cómo-leer-la-referencia-de-natives)
  - [12.2 Tipos y convenciones](12-natives-guia-practica.md#122-tipos-y-convenciones)
  - [12.3 Cargar modelos, animaciones y otros assets (*streaming*)](12-natives-guia-practica.md#123-cargar-modelos-animaciones-y-otros-assets-streaming)
  - [12.4 Jugador y ped](12-natives-guia-practica.md#124-jugador-y-ped)
  - [12.5 Vehículos](12-natives-guia-practica.md#125-vehículos)
  - [12.6 Entidades: control y red](12-natives-guia-practica.md#126-entidades-control-y-red)
  - [12.7 Objetos (props)](12-natives-guia-practica.md#127-objetos-props)
  - [12.8 Animaciones y escenarios](12-natives-guia-practica.md#128-animaciones-y-escenarios)
  - [12.9 Blips (iconos del mapa)](12-natives-guia-practica.md#129-blips-iconos-del-mapa)
  - [12.10 Marcadores, texto 3D y notificaciones](12-natives-guia-practica.md#1210-marcadores-texto-3d-y-notificaciones)
  - [12.11 Cámaras](12-natives-guia-practica.md#1211-cámaras)
  - [12.12 Mundo: hora, clima, IPLs, población](12-natives-guia-practica.md#1212-mundo-hora-clima-ipls-población)
  - [12.13 Armas](12-natives-guia-practica.md#1213-armas)
  - [12.14 Audio y sonidos](12-natives-guia-practica.md#1214-audio-y-sonidos)
  - [12.15 Scaleforms](12-natives-guia-practica.md#1215-scaleforms)
  - [12.16 Raycast (qué estoy mirando)](12-natives-guia-practica.md#1216-raycast-qué-estoy-mirando)
  - [12.17 Natives propios del servidor (lista útil)](12-natives-guia-practica.md#1217-natives-propios-del-servidor-lista-útil)
- **[13. Red, OneSync, State Bags y Routing Buckets](13-red-onesync-statebags-buckets.md)**
  - [13.1 Cómo funciona la sincronización con OneSync](13-red-onesync-statebags-buckets.md#131-cómo-funciona-la-sincronización-con-onesync)
  - [13.2 Ámbitos (*scopes*)](13-red-onesync-statebags-buckets.md#132-ámbitos-scopes)
  - [13.3 Control de entidades creadas por clientes](13-red-onesync-statebags-buckets.md#133-control-de-entidades-creadas-por-clientes)
  - [13.4 State Bags](13-red-onesync-statebags-buckets.md#134-state-bags)
  - [13.5 Routing Buckets (dimensiones)](13-red-onesync-statebags-buckets.md#135-routing-buckets-dimensiones)
  - [13.6 Eventos latentes y tamaño de los datos](13-red-onesync-statebags-buckets.md#136-eventos-latentes-y-tamaño-de-los-datos)
  - [13.7 Comprobar OneSync desde scripts](13-red-onesync-statebags-buckets.md#137-comprobar-onesync-desde-scripts)
- **[14. NUI (interfaces web dentro del juego)](14-nui.md)**
  - [14.1 Estructura mínima](14-nui.md#141-estructura-mínima)
  - [14.2 Lua → NUI: SendNUIMessage](14-nui.md#142-lua--nui-sendnuimessage)
  - [14.3 NUI → Lua: RegisterNUICallback + fetch](14-nui.md#143-nui--lua-registernuicallback--fetch)
  - [14.4 Foco, ratón y teclado](14-nui.md#144-foco-ratón-y-teclado)
  - [14.5 Rutas de archivos dentro de NUI](14-nui.md#145-rutas-de-archivos-dentro-de-nui)
  - [14.6 Depurar la NUI](14-nui.md#146-depurar-la-nui)
  - [14.7 NUI con React/Vue/Svelte + Vite](14-nui.md#147-nui-con-reactvuesvelte--vite)
  - [14.8 Pantalla de carga (*loadscreen*)](14-nui.md#148-pantalla-de-carga-loadscreen)
  - [14.9 DUI (páginas web como texturas en el mundo)](14-nui.md#149-dui-páginas-web-como-texturas-en-el-mundo)
  - [14.10 Rendimiento NUI](14-nui.md#1410-rendimiento-nui)
  - [14.11 Qué soporta el navegador de FiveM (CEF): referencia verificada](14-nui.md#1411-qué-soporta-el-navegador-de-fivem-cef-referencia-verificada)
- **[15. Streaming de assets (vehículos, mapas, ropa, armas…)](15-streaming-assets.md)**
  - [15.1 Carpeta stream](15-streaming-assets.md#151-carpeta-stream)
  - [15.2 Reemplazo vs *add-on*](15-streaming-assets.md#152-reemplazo-vs-add-on)
  - [15.3 Vehículo add-on completo](15-streaming-assets.md#153-vehículo-add-on-completo)
  - [15.4 Mapas: ymaps y MLOs](15-streaming-assets.md#154-mapas-ymaps-y-mlos)
  - [15.5 Ropa add-on (EUP y similares)](15-streaming-assets.md#155-ropa-add-on-eup-y-similares)
  - [15.6 data_file: tipos más usados](15-streaming-assets.md#156-data_file-tipos-más-usados)
  - [15.7 Armas add-on](15-streaming-assets.md#157-armas-add-on)
  - [15.8 Texturas en tiempo de ejecución (runtime TXD)](15-streaming-assets.md#158-texturas-en-tiempo-de-ejecución-runtime-txd)
  - [15.9 Optimización de assets](15-streaming-assets.md#159-optimización-de-assets)
  - [15.10 Assets de pago y escrow](15-streaming-assets.md#1510-assets-de-pago-y-escrow)
- **[16. Base de datos (MariaDB + oxmysql)](16-base-de-datos.md)**
  - [16.1 Instalar MariaDB](16-base-de-datos.md#161-instalar-mariadb)
  - [16.2 oxmysql: instalación y conexión](16-base-de-datos.md#162-oxmysql-instalación-y-conexión)
  - [16.3 API de oxmysql (Lua)](16-base-de-datos.md#163-api-de-oxmysql-lua)
  - [16.4 Buenas prácticas SQL en FiveM](16-base-de-datos.md#164-buenas-prácticas-sql-en-fivem)
  - [16.5 Patrón: caché de jugador + guardado](16-base-de-datos.md#165-patrón-caché-de-jugador--guardado)
- **[17. Frameworks](17-frameworks.md)**
  - [17.1 Ecosistema Overextended (ox_*)](17-frameworks.md#171-ecosistema-overextended-ox_)
  - [17.2 ESX Legacy (1.16.x)](17-frameworks.md#172-esx-legacy-116x)
  - [17.3 QBCore](17-frameworks.md#173-qbcore)
  - [17.4 Qbox (qbx_core)](17-frameworks.md#174-qbox-qbx_core)
  - [17.5 Escribir scripts compatibles con varios frameworks (*bridge*)](17-frameworks.md#175-escribir-scripts-compatibles-con-varios-frameworks-bridge)
  - [17.6 Crear tu propio framework](17-frameworks.md#176-crear-tu-propio-framework)
- **[18. Voz: pma-voice y Mumble](18-voz.md)**
  - [18.1 Estado de pma-voice (2026)](18-voz.md#181-estado-de-pma-voice-2026)
  - [18.2 Convars (con setr)](18-voz.md#182-convars-con-setr)
  - [18.3 Exports](18-voz.md#183-exports)
  - [18.4 Natives de Mumble (para sistemas propios)](18-voz.md#184-natives-de-mumble-para-sistemas-propios)
- **[19. Seguridad y anti-cheat](19-seguridad.md)**
  - [19.1 Principios](19-seguridad.md#191-principios)
  - [19.2 Errores típicos (y cómo evitarlos)](19-seguridad.md#192-errores-típicos-y-cómo-evitarlos)
  - [19.3 Plantilla de evento seguro](19-seguridad.md#193-plantilla-de-evento-seguro)
  - [19.4 Convars de seguridad recomendadas](19-seguridad.md#194-convars-de-seguridad-recomendadas)
  - [19.5 Eventos de juego para detectar trampas (servidor)](19-seguridad.md#195-eventos-de-juego-para-detectar-trampas-servidor)
  - [19.6 Protección de eventos con tokens: ¿sirve?](19-seguridad.md#196-protección-de-eventos-con-tokens-sirve)
  - [19.7 Eventos "trampa" (*honeypots*)](19-seguridad.md#197-eventos-trampa-honeypots)
  - [19.8 Identificadores, tokens y bans](19-seguridad.md#198-identificadores-tokens-y-bans)
  - [19.9 Anti-cheat](19-seguridad.md#199-anti-cheat)
  - [19.10 Seguridad del host](19-seguridad.md#1910-seguridad-del-host)
- **[20. Rendimiento y optimización](20-rendimiento.md)**
  - [20.1 Medir antes de optimizar](20-rendimiento.md#201-medir-antes-de-optimizar)
  - [20.2 Cliente: reglas de oro](20-rendimiento.md#202-cliente-reglas-de-oro)
  - [20.3 Servidor: reglas de oro](20-rendimiento.md#203-servidor-reglas-de-oro)
  - [20.4 Población y entidades](20-rendimiento.md#204-población-y-entidades)
  - [20.5 Streaming](20-rendimiento.md#205-streaming)
- **[21. Depuración y errores comunes](21-depuracion.md)**
  - [21.1 Dónde mirar](21-depuracion.md#211-dónde-mirar)
  - [21.2 Leer un error de script](21-depuracion.md#212-leer-un-error-de-script)
  - [21.3 Errores frecuentes y soluciones](21-depuracion.md#213-errores-frecuentes-y-soluciones)
  - [21.4 Técnicas de depuración](21-depuracion.md#214-técnicas-de-depuración)
- **[22. El cliente FiveM](22-cliente-fivem.md)**
  - [22.1 Instalación](22-cliente-fivem.md#221-instalación)
  - [22.2 Carpetas importantes](22-cliente-fivem.md#222-carpetas-importantes)
  - [22.3 Opciones de lanzamiento](22-cliente-fivem.md#223-opciones-de-lanzamiento)
  - [22.4 Comandos de consola del cliente (F8)](22-cliente-fivem.md#224-comandos-de-consola-del-cliente-f8)
  - [22.5 Nombres de jugador](22-cliente-fivem.md#225-nombres-de-jugador)
  - [22.6 Problemas habituales del jugador](22-cliente-fivem.md#226-problemas-habituales-del-jugador)
- **[23. Monetización, legalidad y Asset Escrow](23-monetizacion-y-legal.md)**
  - [23.1 Creator Platform License Agreement (PLA)](23-monetizacion-y-legal.md#231-creator-platform-license-agreement-pla)
  - [23.2 Tebex](23-monetizacion-y-legal.md#232-tebex)
  - [23.3 Asset Escrow](23-monetizacion-y-legal.md#233-asset-escrow)
  - [23.4 Si vendes recursos (creadores)](23-monetizacion-y-legal.md#234-si-vendes-recursos-creadores)
- **[24. txAdmin a fondo](24-txadmin.md)**
  - [24.1 Funciones](24-txadmin.md#241-funciones)
  - [24.2 Configuración por variables de entorno (TXHOST_*)](24-txadmin.md#242-configuración-por-variables-de-entorno-txhost_)
  - [24.3 Convars del menú de txAdmin](24-txadmin.md#243-convars-del-menú-de-txadmin)
  - [24.4 Eventos de txAdmin para tus scripts](24-txadmin.md#244-eventos-de-txadmin-para-tus-scripts)
- **[25. Hosting, despliegue y operación](25-hosting-y-despliegue.md)**
  - [25.1 Opciones de hosting](25-hosting-y-despliegue.md#251-opciones-de-hosting)
  - [25.2 Flujo de trabajo recomendado](25-hosting-y-despliegue.md#252-flujo-de-trabajo-recomendado)
  - [25.3 Proxies y descargas a gran escala](25-hosting-y-despliegue.md#253-proxies-y-descargas-a-gran-escala)
  - [25.4 Mantenimiento periódico](25-hosting-y-despliegue.md#254-mantenimiento-periódico)
- **[26. Buenas prácticas de desarrollo](26-buenas-practicas.md)**
  - [26.1 Nombres y organización](26-buenas-practicas.md#261-nombres-y-organización)
  - [26.2 Configuración](26-buenas-practicas.md#262-configuración)
  - [26.3 Locales (traducciones)](26-buenas-practicas.md#263-locales-traducciones)
  - [26.4 Versionado y comprobación de actualizaciones](26-buenas-practicas.md#264-versionado-y-comprobación-de-actualizaciones)
  - [26.5 Lista de comprobación antes de publicar un recurso](26-buenas-practicas.md#265-lista-de-comprobación-antes-de-publicar-un-recurso)
- **[27. Tutorial completo: recurso "tienda" de principio a fin](27-tutorial-recurso-tienda.md)**
  - [27.1 Estructura](27-tutorial-recurso-tienda.md#271-estructura)
  - [27.2 fxmanifest.lua](27-tutorial-recurso-tienda.md#272-fxmanifestlua)
  - [27.3 config.lua](27-tutorial-recurso-tienda.md#273-configlua)
  - [27.4 locales/es.json](27-tutorial-recurso-tienda.md#274-localesesjson)
  - [27.5 sql/install.sql](27-tutorial-recurso-tienda.md#275-sqlinstallsql)
  - [27.6 client/main.lua](27-tutorial-recurso-tienda.md#276-clientmainlua)
  - [27.7 server/main.lua](27-tutorial-recurso-tienda.md#277-servermainlua)
  - [27.8 Instalación](27-tutorial-recurso-tienda.md#278-instalación)
- **[28. Chuleta rápida (*cheat sheet*)](28-chuleta.md)**
  - [28.1 Lua cliente](28-chuleta.md#281-lua-cliente)
  - [28.2 Lua servidor](28-chuleta.md#282-lua-servidor)
  - [28.3 Consola del servidor](28-chuleta.md#283-consola-del-servidor)
  - [28.4 F8 cliente](28-chuleta.md#284-f8-cliente)
  - [28.5 Puertos](28-chuleta.md#285-puertos)
- **[29. Preguntas frecuentes (FAQ)](29-faq.md)**
- **[30. Glosario](30-glosario.md)**
- **[31. Enlaces oficiales y recursos](31-enlaces.md)**
  - [Oficiales Cfx.re](31-enlaces.md#oficiales-cfxre)
  - [Ecosistema](31-enlaces.md#ecosistema)
