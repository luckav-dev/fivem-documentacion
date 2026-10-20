# 📘 Documentación completa de FiveM (Legacy) — Edición 2026

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
- Los ejemplos de código están en **Lua** salvo que se indique otro lenguaje.

---

## Índice

- [1. Introducción](#1-introducción)
  - [1.1 ¿Qué es FiveM?](#11-qué-es-fivem)
  - [1.2 Historia resumida](#12-historia-resumida)
  - [1.3 Ecosistema Cfx.re](#13-ecosistema-cfxre)
- [2. Conceptos fundamentales](#2-conceptos-fundamentales)
  - [2.1 Arquitectura cliente-servidor](#21-arquitectura-cliente-servidor)
  - [2.2 Recursos (*resources*)](#22-recursos-resources)
  - [2.3 Lado cliente, lado servidor y "shared"](#23-lado-cliente-lado-servidor-y-shared)
  - [2.4 Natives](#24-natives)
  - [2.5 OneSync](#25-onesync)
  - [2.6 Game build](#26-game-build)
  - [2.7 Runtimes de scripting](#27-runtimes-de-scripting)
  - [2.8 Identificadores de jugador](#28-identificadores-de-jugador)
  - [2.9 Glosario rápido de esta sección](#29-glosario-rápido-de-esta-sección)
- [3. Instalación y puesta en marcha del servidor](#3-instalación-y-puesta-en-marcha-del-servidor)
  - [3.1 Requisitos](#31-requisitos)
  - [3.2 Obtener una clave de servidor (*license key*)](#32-obtener-una-clave-de-servidor-license-key)
  - [3.3 Descargar los artefactos (FXServer)](#33-descargar-los-artefactos-fxserver)
  - [3.4 Estructura de carpetas recomendada](#34-estructura-de-carpetas-recomendada)
  - [3.5 Instalación en Windows (con txAdmin, recomendado)](#35-instalación-en-windows-con-txadmin-recomendado)
  - [3.6 Instalación en Windows (manual, sin txAdmin)](#36-instalación-en-windows-manual-sin-txadmin)
  - [3.7 Instalación en Linux](#37-instalación-en-linux)
  - [3.8 Puertos y firewall](#38-puertos-y-firewall)
  - [3.9 Conectarse al servidor](#39-conectarse-al-servidor)
  - [3.10 Actualizar el servidor (artefactos)](#310-actualizar-el-servidor-artefactos)
  - [3.11 Recursos base de cfx-server-data](#311-recursos-base-de-cfx-server-data)
- [4. server.cfg a fondo](#4-servercfg-a-fondo)
  - [4.1 set, sets, setr y exec](#41-set-sets-setr-y-exec)
  - [4.2 server.cfg completo y comentado](#42-servercfg-completo-y-comentado)
  - [4.3 Colores en el nombre del servidor](#43-colores-en-el-nombre-del-servidor)
  - [4.4 Orden de carga y dependencias](#44-orden-de-carga-y-dependencias)
- [5. Comandos de consola y convars (referencia completa)](#5-comandos-de-consola-y-convars-referencia-completa)
  - [5.1 Comandos de recursos](#51-comandos-de-recursos)
  - [5.2 Comandos globales y de gestión](#52-comandos-globales-y-de-gestión)
  - [5.3 Convars de configuración](#53-convars-de-configuración)
  - [5.4 Game builds (sv_enforceGameBuild)](#54-game-builds-sv_enforcegamebuild)
  - [5.5 Pools (increase_pool_size)](#55-pools-increase_pool_size)
- [6. Permisos: sistema ACE](#6-permisos-sistema-ace)
  - [6.1 Conceptos](#61-conceptos)
  - [6.2 Comandos](#62-comandos)
  - [6.3 Ejemplo de jerarquía completa](#63-ejemplo-de-jerarquía-completa)
  - [6.4 Usar ACE desde scripts](#64-usar-ace-desde-scripts)
- [7. Recursos y fxmanifest.lua](#7-recursos-y-fxmanifestlua)
  - [7.1 Estructura típica de un recurso](#71-estructura-típica-de-un-recurso)
  - [7.2 fxmanifest.lua mínimo](#72-fxmanifestlua-mínimo)
  - [7.3 fxmanifest.lua completo con todas las directivas habituales](#73-fxmanifestlua-completo-con-todas-las-directivas-habituales)
  - [7.4 Referencia de directivas](#74-referencia-de-directivas)
  - [7.5 Prefijo @ y rutas](#75-prefijo--y-rutas)
  - [7.6 Metadatos desde código](#76-metadatos-desde-código)
  - [7.7 Ciclo de vida de un recurso](#77-ciclo-de-vida-de-un-recurso)
  - [7.8 Funciones de gestión de recursos (servidor)](#78-funciones-de-gestión-de-recursos-servidor)
- [8. Scripting: fundamentos comunes (todos los lenguajes)](#8-scripting-fundamentos-comunes-todos-los-lenguajes)
  - [8.1 Hilos (*threads*), Wait y el planificador](#81-hilos-threads-wait-y-el-planificador)
  - [8.2 Eventos](#82-eventos)
  - [8.3 Patrón *callback* (petición/respuesta cliente⇄servidor)](#83-patrón-callback-peticiónrespuesta-clienteservidor)
  - [8.4 Exports](#84-exports)
  - [8.5 Referencias a funciones](#85-referencias-a-funciones)
  - [8.6 Comandos](#86-comandos)
  - [8.7 Teclas: RegisterKeyMapping](#87-teclas-registerkeymapping)
  - [8.8 Controles del juego](#88-controles-del-juego)
  - [8.9 Convars desde scripts](#89-convars-desde-scripts)
  - [8.10 KVP (almacenamiento clave-valor)](#810-kvp-almacenamiento-clave-valor)
  - [8.11 HTTP: peticiones salientes y endpoints propios](#811-http-peticiones-salientes-y-endpoints-propios)
  - [8.12 Utilidades comunes](#812-utilidades-comunes)
  - [8.13 Eventos del sistema más importantes](#813-eventos-del-sistema-más-importantes)
  - [8.14 Conexión de jugadores: playerConnecting y *deferrals*](#814-conexión-de-jugadores-playerconnecting-y-deferrals)
  - [8.15 Funciones de jugador en el servidor](#815-funciones-de-jugador-en-el-servidor)
- [9. Lua en FiveM (CfxLua 5.4)](#9-lua-en-fivem-cfxlua-54)
  - [9.1 Qué Lua usa FiveM](#91-qué-lua-usa-fivem)
  - [9.2 Cambios de 5.3 → 5.4 que pueden romper scripts antiguos](#92-cambios-de-53--54-que-pueden-romper-scripts-antiguos)
  - [9.3 Extensiones de sintaxis de CfxLua](#93-extensiones-de-sintaxis-de-cfxlua)
  - [9.4 Vectores y cuaterniones](#94-vectores-y-cuaterniones)
  - [9.5 Librerías y globales integradas](#95-librerías-y-globales-integradas)
  - [9.6 Estilo y buenas prácticas en Lua](#96-estilo-y-buenas-prácticas-en-lua)
  - [9.7 Módulos y organización](#97-módulos-y-organización)
  - [9.8 Autocompletado en el editor (VS Code)](#98-autocompletado-en-el-editor-vs-code)
- [10. JavaScript y TypeScript](#10-javascript-y-typescript)
  - [10.1 Entornos](#101-entornos)
  - [10.2 Manifest](#102-manifest)
  - [10.3 API básica](#103-api-básica)
  - [10.4 Diferencias importantes respecto a Lua](#104-diferencias-importantes-respecto-a-lua)
  - [10.5 TypeScript con tipos oficiales](#105-typescript-con-tipos-oficiales)
  - [10.6 Servidor: async, base de datos y npm](#106-servidor-async-base-de-datos-y-npm)
- [11. C# (.NET / Mono)](#11-c-net--mono)
  - [11.1 Proyecto](#111-proyecto)
  - [11.2 Script básico](#112-script-básico)
  - [11.3 Conceptos](#113-conceptos)
  - [11.4 Plantillas oficiales](#114-plantillas-oficiales)
- [12. Natives: guía práctica](#12-natives-guía-práctica)
  - [12.1 Cómo leer la referencia de natives](#121-cómo-leer-la-referencia-de-natives)
  - [12.2 Tipos y convenciones](#122-tipos-y-convenciones)
  - [12.3 Cargar modelos, animaciones y otros assets (*streaming*)](#123-cargar-modelos-animaciones-y-otros-assets-streaming)
  - [12.4 Jugador y ped](#124-jugador-y-ped)
  - [12.5 Vehículos](#125-vehículos)
  - [12.6 Entidades: control y red](#126-entidades-control-y-red)
  - [12.7 Objetos (props)](#127-objetos-props)
  - [12.8 Animaciones y escenarios](#128-animaciones-y-escenarios)
  - [12.9 Blips (iconos del mapa)](#129-blips-iconos-del-mapa)
  - [12.10 Marcadores, texto 3D y notificaciones](#1210-marcadores-texto-3d-y-notificaciones)
  - [12.11 Cámaras](#1211-cámaras)
  - [12.12 Mundo: hora, clima, IPLs, población](#1212-mundo-hora-clima-ipls-población)
  - [12.13 Armas](#1213-armas)
  - [12.14 Audio y sonidos](#1214-audio-y-sonidos)
  - [12.15 Scaleforms](#1215-scaleforms)
  - [12.16 Raycast (qué estoy mirando)](#1216-raycast-qué-estoy-mirando)
  - [12.17 Natives propios del servidor (lista útil)](#1217-natives-propios-del-servidor-lista-útil)
- [13. Red, OneSync, State Bags y Routing Buckets](#13-red-onesync-state-bags-y-routing-buckets)
  - [13.1 Cómo funciona la sincronización con OneSync](#131-cómo-funciona-la-sincronización-con-onesync)
  - [13.2 Ámbitos (*scopes*)](#132-ámbitos-scopes)
  - [13.3 Control de entidades creadas por clientes](#133-control-de-entidades-creadas-por-clientes)
  - [13.4 State Bags](#134-state-bags)
  - [13.5 Routing Buckets (dimensiones)](#135-routing-buckets-dimensiones)
  - [13.6 Eventos latentes y tamaño de los datos](#136-eventos-latentes-y-tamaño-de-los-datos)
  - [13.7 Comprobar OneSync desde scripts](#137-comprobar-onesync-desde-scripts)
- [14. NUI (interfaces web dentro del juego)](#14-nui-interfaces-web-dentro-del-juego)
  - [14.1 Estructura mínima](#141-estructura-mínima)
  - [14.2 Lua → NUI: SendNUIMessage](#142-lua--nui-sendnuimessage)
  - [14.3 NUI → Lua: RegisterNUICallback + fetch](#143-nui--lua-registernuicallback--fetch)
  - [14.4 Foco, ratón y teclado](#144-foco-ratón-y-teclado)
  - [14.5 Rutas de archivos dentro de NUI](#145-rutas-de-archivos-dentro-de-nui)
  - [14.6 Depurar la NUI](#146-depurar-la-nui)
  - [14.7 NUI con React/Vue/Svelte + Vite](#147-nui-con-reactvuesvelte--vite)
  - [14.8 Pantalla de carga (*loadscreen*)](#148-pantalla-de-carga-loadscreen)
  - [14.9 DUI (páginas web como texturas en el mundo)](#149-dui-páginas-web-como-texturas-en-el-mundo)
  - [14.10 Rendimiento NUI](#1410-rendimiento-nui)
- [15. Streaming de assets (vehículos, mapas, ropa, armas…)](#15-streaming-de-assets-vehículos-mapas-ropa-armas)
  - [15.1 Carpeta stream](#151-carpeta-stream)
  - [15.2 Reemplazo vs *add-on*](#152-reemplazo-vs-add-on)
  - [15.3 Vehículo add-on completo](#153-vehículo-add-on-completo)
  - [15.4 Mapas: ymaps y MLOs](#154-mapas-ymaps-y-mlos)
  - [15.5 Ropa add-on (EUP y similares)](#155-ropa-add-on-eup-y-similares)
  - [15.6 data_file: tipos más usados](#156-data_file-tipos-más-usados)
  - [15.7 Armas add-on](#157-armas-add-on)
  - [15.8 Texturas en tiempo de ejecución (runtime TXD)](#158-texturas-en-tiempo-de-ejecución-runtime-txd)
  - [15.9 Optimización de assets](#159-optimización-de-assets)
  - [15.10 Assets de pago y escrow](#1510-assets-de-pago-y-escrow)
- [16. Base de datos (MariaDB + oxmysql)](#16-base-de-datos-mariadb--oxmysql)
  - [16.1 Instalar MariaDB](#161-instalar-mariadb)
  - [16.2 oxmysql: instalación y conexión](#162-oxmysql-instalación-y-conexión)
  - [16.3 API de oxmysql (Lua)](#163-api-de-oxmysql-lua)
  - [16.4 Buenas prácticas SQL en FiveM](#164-buenas-prácticas-sql-en-fivem)
  - [16.5 Patrón: caché de jugador + guardado](#165-patrón-caché-de-jugador--guardado)
- [17. Frameworks](#17-frameworks)
  - [17.1 Ecosistema Overextended (ox_*)](#171-ecosistema-overextended-ox_)
  - [17.2 ESX Legacy (1.16.x)](#172-esx-legacy-116x)
  - [17.3 QBCore](#173-qbcore)
  - [17.4 Qbox (qbx_core)](#174-qbox-qbx_core)
  - [17.5 Escribir scripts compatibles con varios frameworks (*bridge*)](#175-escribir-scripts-compatibles-con-varios-frameworks-bridge)
- [18. Voz: pma-voice y Mumble](#18-voz-pma-voice-y-mumble)
  - [18.1 Estado de pma-voice (2026)](#181-estado-de-pma-voice-2026)
  - [18.2 Convars (con setr)](#182-convars-con-setr)
  - [18.3 Exports](#183-exports)
  - [18.4 Natives de Mumble (para sistemas propios)](#184-natives-de-mumble-para-sistemas-propios)
- [19. Seguridad y anti-cheat](#19-seguridad-y-anti-cheat)
  - [19.1 Principios](#191-principios)
  - [19.2 Errores típicos (y cómo evitarlos)](#192-errores-típicos-y-cómo-evitarlos)
  - [19.3 Plantilla de evento seguro](#193-plantilla-de-evento-seguro)
  - [19.4 Convars de seguridad recomendadas](#194-convars-de-seguridad-recomendadas)
  - [19.5 Eventos de juego para detectar trampas (servidor)](#195-eventos-de-juego-para-detectar-trampas-servidor)
  - [19.6 Protección de eventos con tokens: ¿sirve?](#196-protección-de-eventos-con-tokens-sirve)
  - [19.7 Eventos "trampa" (*honeypots*)](#197-eventos-trampa-honeypots)
  - [19.8 Identificadores, tokens y bans](#198-identificadores-tokens-y-bans)
  - [19.9 Anti-cheat](#199-anti-cheat)
  - [19.10 Seguridad del host](#1910-seguridad-del-host)
- [20. Rendimiento y optimización](#20-rendimiento-y-optimización)
  - [20.1 Medir antes de optimizar](#201-medir-antes-de-optimizar)
  - [20.2 Cliente: reglas de oro](#202-cliente-reglas-de-oro)
  - [20.3 Servidor: reglas de oro](#203-servidor-reglas-de-oro)
  - [20.4 Población y entidades](#204-población-y-entidades)
  - [20.5 Streaming](#205-streaming)
- [21. Depuración y errores comunes](#21-depuración-y-errores-comunes)
  - [21.1 Dónde mirar](#211-dónde-mirar)
  - [21.2 Leer un error de script](#212-leer-un-error-de-script)
  - [21.3 Errores frecuentes y soluciones](#213-errores-frecuentes-y-soluciones)
  - [21.4 Técnicas de depuración](#214-técnicas-de-depuración)
- [22. El cliente FiveM](#22-el-cliente-fivem)
  - [22.1 Instalación](#221-instalación)
  - [22.2 Carpetas importantes](#222-carpetas-importantes)
  - [22.3 Opciones de lanzamiento](#223-opciones-de-lanzamiento)
  - [22.4 Comandos de consola del cliente (F8)](#224-comandos-de-consola-del-cliente-f8)
  - [22.5 Nombres de jugador](#225-nombres-de-jugador)
  - [22.6 Problemas habituales del jugador](#226-problemas-habituales-del-jugador)
- [23. Monetización, legalidad y Asset Escrow](#23-monetización-legalidad-y-asset-escrow)
  - [23.1 Creator Platform License Agreement (PLA)](#231-creator-platform-license-agreement-pla)
  - [23.2 Tebex](#232-tebex)
  - [23.3 Asset Escrow](#233-asset-escrow)
  - [23.4 Si vendes recursos (creadores)](#234-si-vendes-recursos-creadores)
- [24. txAdmin a fondo](#24-txadmin-a-fondo)
  - [24.1 Funciones](#241-funciones)
  - [24.2 Configuración por variables de entorno (TXHOST_*)](#242-configuración-por-variables-de-entorno-txhost_)
  - [24.3 Convars del menú de txAdmin](#243-convars-del-menú-de-txadmin)
  - [24.4 Eventos de txAdmin para tus scripts](#244-eventos-de-txadmin-para-tus-scripts)
- [25. Hosting, despliegue y operación](#25-hosting-despliegue-y-operación)
  - [25.1 Opciones de hosting](#251-opciones-de-hosting)
  - [25.2 Flujo de trabajo recomendado](#252-flujo-de-trabajo-recomendado)
  - [25.3 Proxies y descargas a gran escala](#253-proxies-y-descargas-a-gran-escala)
  - [25.4 Mantenimiento periódico](#254-mantenimiento-periódico)
- [26. Buenas prácticas de desarrollo](#26-buenas-prácticas-de-desarrollo)
  - [26.1 Nombres y organización](#261-nombres-y-organización)
  - [26.2 Configuración](#262-configuración)
  - [26.3 Locales (traducciones)](#263-locales-traducciones)
  - [26.4 Versionado y comprobación de actualizaciones](#264-versionado-y-comprobación-de-actualizaciones)
  - [26.5 Lista de comprobación antes de publicar un recurso](#265-lista-de-comprobación-antes-de-publicar-un-recurso)
- [27. Tutorial completo: recurso "tienda" de principio a fin](#27-tutorial-completo-recurso-tienda-de-principio-a-fin)
  - [27.1 Estructura](#271-estructura)
  - [27.2 fxmanifest.lua](#272-fxmanifestlua)
  - [27.3 config.lua](#273-configlua)
  - [27.4 locales/es.json](#274-localesesjson)
  - [27.5 sql/install.sql](#275-sqlinstallsql)
  - [27.6 client/main.lua](#276-clientmainlua)
  - [27.7 server/main.lua](#277-servermainlua)
  - [27.8 Instalación](#278-instalación)
- [28. Chuleta rápida (*cheat sheet*)](#28-chuleta-rápida-cheat-sheet)
  - [28.1 Lua cliente](#281-lua-cliente)
  - [28.2 Lua servidor](#282-lua-servidor)
  - [28.3 Consola del servidor](#283-consola-del-servidor)
  - [28.4 F8 cliente](#284-f8-cliente)
  - [28.5 Puertos](#285-puertos)
- [29. Preguntas frecuentes (FAQ)](#29-preguntas-frecuentes-faq)
- [30. Glosario](#30-glosario)
- [31. Enlaces oficiales y recursos](#31-enlaces-oficiales-y-recursos)
  - [Oficiales Cfx.re](#oficiales-cfxre)
  - [Ecosistema](#ecosistema)
- [32. Historial de este documento](#32-historial-de-este-documento)

---

# 1. Introducción

## 1.1 ¿Qué es FiveM?

**FiveM** es una plataforma de modificación multijugador para **Grand Theft Auto V (PC)** desarrollada por **Cfx.re** (el equipo detrás de FiveM y RedM). Permite crear y jugar en **servidores dedicados personalizados** con sus propias reglas, mapas, vehículos, scripts e interfaces. Es la base de casi todo el *roleplay* (RP) de GTA V, pero también de servidores de carreras, *freeroam*, *drift*, PvP, minijuegos, etc.

Puntos clave:

- **No modifica tu GTA V original**: FiveM usa su propio proceso y su propia caché; tu partida de GTA Online no se toca.
- **Necesita una copia legítima de GTA V** (Steam, Epic Games, Rockstar Games Launcher o Microsoft Store/Xbox Game Pass para PC; esta última se admite oficialmente desde abril de 2025). La propiedad del juego se verifica a través del Rockstar Games Launcher al iniciar.
- **Los servidores ejecutan "recursos"** (*resources*): paquetes de código (Lua, JavaScript o C#), interfaces web (NUI), y *assets* de juego (vehículos, mapas, ropa…).
- **Está integrado en Rockstar Games**: Cfx.re pasó a formar parte de Rockstar Games en **agosto de 2023**. Desde entonces FiveM es una plataforma oficialmente aprobada y sujeta al **Platform License Agreement (PLA)** y a los Términos de Servicio de Cfx.re.

## 1.2 Historia resumida

| Año | Hito |
|---|---|
| 2014-2015 | Nace el proyecto CitizenMP/FiveM como modificación multijugador independiente. |
| 2017 | Se estabilizan FXServer (el servidor actual) y el sistema de recursos `__resource.lua`. |
| 2019 | Se introduce `fxmanifest.lua` y llega **OneSync** (sincronización controlada por el servidor). |
| 2020-2021 | **txAdmin** se integra en el propio servidor; OneSync deja de requerir Patreon; llegan *state bags* y *routing buckets*. |
| 2022 | Se introduce **Asset Escrow** (protección de recursos de pago) y la integración con Tebex. |
| 2023 | **Rockstar Games adquiere Cfx.re** (agosto). |
| 2024 | Node.js 22 se ofrece como versión alternativa del runtime JS. En diciembre se lanza **portal.cfx.re**, que sustituye a *Keymaster* y Patreon. |
| 2025 | txAdmin pasa a ser oficialmente parte de Cfx.re (abril). **Lua 5.3 se elimina**: todo Lua pasa a 5.4.8 (junio/julio). Integración más estricta con el Rockstar Games Launcher, soporte de Microsoft Store/Game Pass, *release notes* mensuales. Builds 3570 (*Money Fronts*) y 3751 (*A Safehouse in the Hills*). Overextended archiva sus repositorios (abril). |
| 2026 | Nuevo **Creator Platform License Agreement** (12 de enero, revisado el 10 de septiembre) y Cfx Marketplace. Se eliminan los identificadores `xbl:` y `live:` (abril). Overextended retoma el desarrollo (abril). Build **3889** (*The Kortz Center Heist*). Artefacto **35245** como mínimo para que se pueda entrar al servidor (15 de octubre). Los metadatos del servidor (nombre, descripción, tags, banner) pasan a gestionarse en Portal (21 de octubre). |

> **Alcance de esta documentación:** cubre **exclusivamente FiveM "Legacy"**, es decir, el FiveM clásico sobre **GTA V Legacy** con el servidor **FXServer**. No mezcla nada de otras ediciones/plataformas para evitar confusiones. Si un dato aquí no te cuadra, comprueba que estás usando FiveM clásico y FXServer.

## 1.3 Ecosistema Cfx.re

| Componente | Qué es |
|---|---|
| **FiveM (cliente)** | La aplicación que instala el jugador y que se conecta a los servidores. |
| **FXServer** | El servidor dedicado (binario `FXServer.exe` en Windows, `run.sh` + `alpine` en Linux). |
| **Artefactos (*artifacts*)** | Las versiones compiladas de FXServer que se descargan desde runtime.fivem.net. |
| **txAdmin** | Panel web de administración incluido dentro de FXServer (puerto 40120 por defecto). Versión actual **8.1.1**. |
| **cfx-server-data** | Repositorio con los recursos base (`mapmanager`, `spawnmanager`, `chat`, `sessionmanager`, `hardcap`, `rconlog`, `basic-gamemode`, `baseevents`, …). |
| **portal.cfx.re** | Portal para crear claves de servidor (*license keys*), gestionar Asset Escrow y ver tus recursos comprados. |
| **forum.cfx.re** | Foro oficial: anuncios, *release notes*, lanzamientos de recursos, soporte. |
| **docs.fivem.net** | Documentación oficial y **referencia de natives** (`docs.fivem.net/natives`). |
| **Tebex** | Única plataforma de monetización autorizada (tiendas de servidor y venta de recursos). |
| **Cfx Marketplace** | Mercado oficial de recursos (desde enero de 2026). |
| **cfx.re/join** | Códigos cortos para unirse a un servidor (`cfx.re/join/abc123`). |
| **RedM** | La plataforma hermana para Red Dead Redemption 2 (fuera del alcance de este documento). |

---

# 2. Conceptos fundamentales

Antes de tocar nada conviene entender **cómo está montado FiveM**. Casi todos los errores de principiante vienen de no tener claros estos conceptos.

## 2.1 Arquitectura cliente-servidor

```
┌──────────────────────────────┐            ┌──────────────────────────────┐
│        CLIENTE (jugador)     │            │      SERVIDOR (FXServer)     │
│                              │            │                              │
│  GTA V + FiveM               │   UDP/TCP  │  Gestiona recursos           │
│  ├─ client_scripts (Lua/JS/  │◄──────────►│  ├─ server_scripts           │
│  │  C#) se descargan y       │   30120    │  │  (NUNCA se envían al      │
│  │  ejecutan aquí            │            │  │  cliente)                 │
│  ├─ NUI (HTML/CSS/JS)        │            │  ├─ OneSync (estado mundo)   │
│  ├─ Streaming de assets      │            │  ├─ Base de datos (MySQL)    │
│  └─ Natives del juego        │            │  └─ txAdmin (40120)          │
└──────────────────────────────┘            └──────────────────────────────┘
```

- **Cliente**: ejecuta la lógica visual e interactiva (dibujar marcadores, menús, controles, animaciones, NUI). Todo lo que está en el cliente **puede ser leído y manipulado por un tramposo**.
- **Servidor**: es la **autoridad**. Guarda el dinero, inventarios, permisos, base de datos. **Nunca confíes en el cliente.**
- La comunicación entre ambos se hace con **eventos de red** (*net events*), **state bags**, **exports** (solo dentro del mismo lado) y la **sincronización de entidades** de OneSync.

## 2.2 Recursos (*resources*)

Un **recurso** es una carpeta dentro de `resources/` que contiene un archivo **`fxmanifest.lua`** y sus archivos. Puede ser:

- Un **script** (lógica de juego): trabajos, tiendas, HUD, inventario…
- Un **mapa** (MLO, ymaps).
- Un **paquete de streaming** (vehículos, ropa, armas).
- Una **librería** (ox_lib, oxmysql).
- Un **gamemode** o **mapa base** (`basic-gamemode`, `fivem-map-skater`).
- Una **pantalla de carga** (*loadscreen*).

Los recursos se arrancan con `ensure nombre` en `server.cfg`. Las carpetas entre corchetes (`[esx]`, `[standalone]`) son **categorías**: solo sirven para organizar y se pueden arrancar de golpe con `ensure [categoria]`.

## 2.3 Lado cliente, lado servidor y "shared"

| Tipo en `fxmanifest.lua` | Dónde se ejecuta | ¿Se descarga al jugador? |
|---|---|---|
| `client_script(s)` | Cliente | Sí |
| `server_script(s)` | Servidor | **No** |
| `shared_script(s)` | Ambos | Sí |
| `files` | No se ejecutan; quedan disponibles para el cliente (NUI, datos, metas) | Sí |
| `ui_page` | Página NUI cargada en el cliente | Sí |

> **Regla de oro:** cualquier cosa sensible (tokens de Discord, webhooks, contraseñas de base de datos, precios autoritativos, lógica de recompensas) va **solo** en `server_scripts`.

## 2.4 Natives

Los **natives** son las funciones internas del motor de GTA V (RAGE) que FiveM expone a los scripts: `GetEntityCoords`, `SetPedArmour`, `CreateVehicle`, `DrawMarker`… Además, Cfx.re añade **natives propios de FiveM** (prefijo de categoría `CFX`) tanto de cliente como de servidor (`GetPlayerIdentifiers`, `SetPlayerRoutingBucket`, `AddStateBagChangeHandler`…).

- Referencia oficial: **https://docs.fivem.net/natives/**
- En Lua se llaman en **PascalCase**: `GET_ENTITY_COORDS` → `GetEntityCoords`.
- Cada native se identifica por un **hash** de 64 bits (por ejemplo `0x3FEF770D40960D5A`) y se puede invocar con `Citizen.InvokeNative(hash, ...)`.

## 2.5 OneSync

**OneSync** es el sistema de sincronización en el que **el servidor conoce y controla el estado del mundo** (entidades, jugadores, posiciones). Hoy está **activado por defecto** (`onesync on`) y es obligatorio para:

- Más de 32 jugadores (hasta **2048** slots).
- Entidades creadas en el servidor (`CreateVehicle`, `CreatePed` en *server-side*).
- State bags de entidades, routing buckets, `GetEntityCoords` desde el servidor, eventos de juego de servidor (`entityCreating`, `weaponDamageEvent`…).

Modos: `on` (completo, recomendado), `legacy` (compatibilidad, no recomendado), `off` (solo retransmisión, hasta 32 jugadores).

## 2.6 Game build

El **game build** es la versión de GTA V (y por tanto el DLC más reciente) que usará el cliente al entrar al servidor. Se fija con `sv_enforceGameBuild`. Si no lo fijas, se usa la build por defecto **1604** (*Arena War*, 2018), y no tendrás vehículos/ropa/mapas de DLC recientes. Ver la tabla completa en la [sección 5.4](#54-game-builds-sv_enforcegamebuild).

## 2.7 Runtimes de scripting

| Runtime | Lenguaje | Lado | Notas |
|---|---|---|---|
| **Lua** (CfxLua 5.4.8) | Lua | Cliente y servidor | El más usado: rápido y ligero. Desde julio de 2025 es el **único** Lua disponible (Lua 5.3 eliminado), así que `lua54 'yes'` ya no hace falta. |
| **V8 / Node.js** | JavaScript / TypeScript | Cliente (V8) y servidor (Node.js) | En servidor tienes `require`, `npm`, `fs`, `http`… Node 16 por defecto, Node 22 opcional. |
| **Mono** | C# (.NET) | Cliente y servidor | Compilado a DLL. Usa `CitizenFX.Core`. |

Se pueden **mezclar** dentro de un mismo recurso (por ejemplo cliente en Lua y servidor en JS) y comunicarse vía eventos o exports.

## 2.8 Identificadores de jugador

Cada jugador conectado tiene un **server ID** (`source`, número entero) que **cambia en cada conexión**, y varios **identificadores persistentes**:

| Prefijo | Origen | ¿Siempre presente? |
|---|---|---|
| `license:` | Licencia de Rockstar (cuenta Social Club) | Sí (con verificación de propiedad) |
| `license2:` | Licencia secundaria | Normalmente |
| `fivem:` | Cuenta Cfx.re del jugador | Si la ha vinculado |
| `discord:` | ID de Discord | Si Discord está abierto y vinculado |
| `steam:` | SteamID en hexadecimal | Solo si Steam está abierto **y** el servidor tiene `steam_webApiKey` |
| `ip:` | IP | Sí (no fiable para identificar) |

> Los identificadores **`xbl:`** (Xbox Live) y **`live:`** (Microsoft) se **eliminaron el 27 de abril de 2026**. Si tu base de datos o tu sistema de bans dependía de ellos, migra a `license:`/`fivem:`/`discord:`.

> Para guardar datos de personajes usa **`license:`** (o el identificador que use tu framework). Nunca uses el `source` como clave persistente: solo vale mientras dura la sesión.

> **Actualización de seguridad de cuentas (24 de junio de 2026):** a algunos jugadores les puede cambiar el `license:`/`license2:`. Durante un año (hasta el 24 de junio de 2027) pueden volver a elegir su identidad por defecto. Ten un procedimiento de soporte para migrar personajes de un `license:` antiguo a uno nuevo.

Además existen los **tokens de hardware** (`GetPlayerTokens`) útiles para sistemas de *ban*.

## 2.9 Glosario rápido de esta sección

- **Tick / frame**: una iteración del bucle del juego (cliente ~60+ por segundo, servidor ~20 por defecto).
- **Thread / hilo**: en FiveM son **corrutinas** cooperativas, no hilos reales del SO.
- **Entity**: cualquier objeto del mundo (ped, vehículo, objeto/prop).
- **Ped**: personaje (jugador o NPC).
- **Handle**: número local que identifica una entidad en *ese* cliente/servidor.
- **Network ID (netId)**: identificador de red de una entidad, **igual para todos** los clientes y el servidor.
- **Owner**: el cliente que "simula" una entidad en un momento dado.

---

# 3. Instalación y puesta en marcha del servidor

## 3.1 Requisitos

### Hardware orientativo

| Tamaño de servidor | CPU | RAM | Disco | Red |
|---|---|---|---|---|
| Desarrollo / pruebas (1-10 jugadores) | 2-4 núcleos modernos | 4-8 GB | SSD 30 GB | Doméstica |
| Pequeño (≤ 48 jugadores) | 4 núcleos con **alta frecuencia** (single-thread) | 8-16 GB | NVMe 60 GB | 100 Mbps-1 Gbps |
| Mediano (48-128) | 6-8 núcleos alta frecuencia | 16-32 GB | NVMe | 1 Gbps + anti-DDoS |
| Grande (128-2048) | CPU de gama alta (frecuencia > núcleos) | 32-64 GB | NVMe | 1-10 Gbps + anti-DDoS |

> FXServer es muy dependiente del **rendimiento por núcleo**. Una CPU con menos núcleos pero más GHz suele rendir mejor que una con muchos núcleos lentos. La base de datos (MariaDB) conviene tenerla en el mismo host o en la misma red local.

### Software

- **Windows**: Windows 10/11 o Windows Server 2016+ (x64). **Visual C++ Redistributable** (2015-2022 x64) instalado.
- **Linux**: cualquier distribución x64 moderna (Debian/Ubuntu recomendadas). El artefacto de Linux trae su propio *rootfs* Alpine, así que casi no necesita dependencias (`xz-utils` o `tar` para descomprimir).
- **Base de datos** (si usas framework): **MariaDB 11.4 LTS u 11.8 LTS** (recomendadas; la 10.6 llegó a fin de soporte en julio de 2026 y `ox_core` exige 11.4+). MySQL 8 funciona pero da más problemas (palabras reservadas, valores por defecto en JSON/LONGTEXT).
- **Git** (opcional pero recomendado) para versionar tu `server-data`.

## 3.2 Obtener una clave de servidor (*license key*)

1. Entra en **https://portal.cfx.re** e inicia sesión con tu cuenta Cfx.re (la del foro).
2. Ve a **Server Management → Registration Keys** (o similar) y pulsa **Generate key**.
3. Indica la **IP pública** del servidor y el tipo (Windows/Linux/hosting).
4. Copia la clave (`cfxk_xxxxxxxxxxxxxxxxxxxx_xxxxxx`).
5. En `server.cfg`: `sv_licenseKey "cfxk_..."`.

> Cada clave está ligada a una cuenta. No la compartas ni la subas a GitHub. Si se filtra, revócala en el portal.

### Metadatos del servidor en Portal (desde el 21 de octubre de 2026)

Portal pasa a ser el lugar donde se configuran los datos que aparecen en la lista de servidores:

- **Nombre**, **descripción**, hasta **5 tags**, **banner** (recomendado 2560×280) y **enlace de Discord**.
- Los servidores que no lo configuren mostrarán *"Missing server data (must be configured in Portal)"*.
- Límites aplicados desde febrero de 2026: `sv_projectName` 40 caracteres, `sv_hostname` 120 y `sv_projectDesc` 250. Los colores en el título ya no se muestran.

En Portal también tienes: tus **assets** comprados (Asset Escrow, con historial de hasta 5 versiones y changelogs), la subida de recursos si eres creador y la gestión de claves.

## 3.3 Descargar los artefactos (FXServer)

Los artefactos son las versiones compiladas del servidor. La página oficial de descarga es:

- **https://docs.fivem.net/docs/server-download/?platform=legacy** (elige `os=windows` o `os=linux`)

> Las antiguas URLs de índice `runtime.fivem.net/artifacts/fivem/build_server_windows/master/` y `.../build_proot_linux/master/` ahora **redirigen** a esa página. Los enlaces directos a cada archivo (`.../master/<build>-<hash>/server.7z` o `fx.tar.xz`) siguen funcionando.

Canales:

| Canal | Build (20 oct 2026) | Uso |
|---|---|---|
| **Recommended** | **35245** | El que debes usar en producción. Probado por Cfx.re. |
| **Latest** | 37579 | La más nueva del *pipeline*. Pruébala antes de ponerla en producción. |

Enlaces directos del *recommended* actual:

- Windows: `https://runtime.fivem.net/artifacts/fivem/build_server_windows/master/35245-6efb47dff473c0e2a12fb50b08d74c0eb24a50d5/server.7z`
- Linux: `https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/35245-6efb47dff473c0e2a12fb50b08d74c0eb24a50d5/fx.tar.xz`

### Política de soporte (EOS / EOL)

- Una build *recommended* tiene soporte hasta **6 semanas** después de la siguiente; una *latest*, hasta **2 semanas** después.
- En la lista de servidores, los artefactos sin soporte se marcan en gris (**EOS**, *End of Support*) o en rojo (**EOL**, *End of Life*).
- Los artefactos **con más de tres meses sin soporte** no se pueden unir desde la lista de servidores.
- **Desde el 15 de octubre de 2026 no se puede conectar a servidores con artefactos anteriores a 35245.** Con 35245 o superior, el cliente ejecuta siempre el ejecutable estable más reciente de GTA V y carga solo el contenido DLC de la build fijada en `sv_enforceGameBuild` (por eso `sv_replaceExeToSwitchBuilds` queda obsoleto).

> Consulta siempre la página de descarga y el foro antes de actualizar un servidor en producción.

## 3.4 Estructura de carpetas recomendada

Separa siempre **binarios** (artefactos) de **datos** (tu configuración y recursos):

```
FXServer/
├── server/                 ← Artefactos (se reemplazan al actualizar)
│   ├── FXServer.exe        (Windows)  /  run.sh + alpine/ (Linux)
│   ├── citizen/
│   └── components.json ...
└── server-data/            ← TU servidor (versionar con git)
    ├── server.cfg
    ├── resources/
    │   ├── [cfx-default]/  ← recursos base (chat, spawnmanager…)
    │   ├── [framework]/    ← es_extended / qb-core / qbx_core
    │   ├── [ox]/           ← ox_lib, oxmysql, ox_inventory, ox_target…
    │   ├── [scripts]/      ← tus scripts
    │   ├── [maps]/         ← MLOs, ymaps
    │   ├── [vehicles]/     ← vehículos add-on
    │   └── [clothing]/     ← ropa/EUP
    ├── cache/              ← generado automáticamente (no versionar)
    └── txData/             ← datos de txAdmin si se usa (no versionar)
```

## 3.5 Instalación en Windows (con txAdmin, recomendado)

1. Crea `C:\FXServer\server` y `C:\FXServer\server-data`.
2. Descarga el `server.7z` del canal **recommended** y descomprímelo (7-Zip) en `C:\FXServer\server`.
3. Ejecuta `FXServer.exe` **sin** argumentos +exec. Se iniciará **txAdmin** y te mostrará:
   - Una URL (`http://localhost:40120`) y un **PIN** de 4 dígitos.
4. Abre la URL, introduce el PIN y **vincula tu cuenta Cfx.re** (o crea una cuenta local).
5. Sigue el asistente:
   - **Server Name**.
   - **Deployment type**: *Popular Recipes* (ESX, QBCore, QBox, CFX Default…), *Existing Server Data* (si ya tienes `server-data`), *Remote URL Template*, *Custom Template*.
   - Introduce la **license key**.
   - txAdmin descargará los recursos, creará la base de datos (si la receta lo requiere) y generará `server.cfg`.
6. Pulsa **Start Server** en el panel.
7. Abre FiveM → F8 → `connect localhost:30120` (o `connect 127.0.0.1`).

## 3.6 Instalación en Windows (manual, sin txAdmin)

```bat
cd C:\FXServer
git clone https://github.com/citizenfx/cfx-server-data.git server-data
```

Crea `server-data\server.cfg` (ver [sección 4](#4-servercfg-a-fondo)) y luego un `start.bat` en `server-data`:

```bat
@echo off
cd /d C:\FXServer\server-data
C:\FXServer\server\FXServer.exe +exec server.cfg
pause
```

> Si arrancas `FXServer.exe` con `+exec server.cfg`, txAdmin **no** se inicia. Para usar txAdmin arranca sin `+exec` y apunta txAdmin a tu `server-data`.

## 3.7 Instalación en Linux

```bash
# 1. Usuario dedicado (nunca ejecutes el servidor como root)
sudo adduser --disabled-login fivem
sudo -iu fivem

# 2. Artefactos
mkdir -p ~/FXServer/server && cd ~/FXServer/server
# Copia la URL del fx.tar.xz "recommended" desde la página de descarga (ejemplo: 35245)
wget https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/35245-6efb47dff473c0e2a12fb50b08d74c0eb24a50d5/fx.tar.xz
tar xf fx.tar.xz
rm fx.tar.xz

# 3. Datos del servidor
cd ~/FXServer
git clone https://github.com/citizenfx/cfx-server-data.git server-data

# 4. Arrancar (con txAdmin)
cd ~/FXServer/server
./run.sh

# 4b. Arrancar sin txAdmin
cd ~/FXServer/server-data
bash ~/FXServer/server/run.sh +exec server.cfg
```

### Mantenerlo en segundo plano

**Con `screen` / `tmux`:**

```bash
screen -S fivem
cd ~/FXServer/server && ./run.sh
# Ctrl+A, D para salir sin cerrarlo; screen -r fivem para volver
```

**Con `systemd`** (`/etc/systemd/system/fivem.service`):

```ini
[Unit]
Description=FiveM FXServer (txAdmin)
After=network.target mariadb.service

[Service]
Type=simple
User=fivem
WorkingDirectory=/home/fivem/FXServer/server
ExecStart=/bin/bash /home/fivem/FXServer/server/run.sh
Restart=on-failure
RestartSec=10
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now fivem
journalctl -u fivem -f
```

## 3.8 Puertos y firewall

| Puerto | Protocolo | Uso |
|---|---|---|
| **30120** | **TCP + UDP** | Puerto del juego (conexión, HTTP de recursos, sincronización). Configurable con `endpoint_add_tcp/udp`. |
| **40120** | TCP | Panel web de txAdmin (no lo expongas si no hace falta; mejor tras VPN o con contraseña fuerte + 2FA). |
| 3306 | TCP | MariaDB/MySQL (**nunca** lo abras a Internet). |

**Windows (PowerShell como administrador):**

```powershell
New-NetFirewallRule -DisplayName "FiveM TCP" -Direction Inbound -Protocol TCP -LocalPort 30120 -Action Allow
New-NetFirewallRule -DisplayName "FiveM UDP" -Direction Inbound -Protocol UDP -LocalPort 30120 -Action Allow
```

**Linux (ufw):**

```bash
sudo ufw allow 30120/tcp
sudo ufw allow 30120/udp
sudo ufw allow from <TU_IP> to any port 40120 proto tcp   # txAdmin solo desde tu IP
```

En casa también tendrás que **redirigir los puertos** (port forwarding) en el router hacia la IP local del PC.

## 3.9 Conectarse al servidor

- **F8 (consola del cliente)**: `connect 127.0.0.1:30120` / `connect mi.dominio.com`
- **Enlace directo**: `fivem://connect/127.0.0.1:30120`
- **Código Cfx**: `cfx.re/join/xxxxxx` (aparece en la consola del servidor cuando está listado públicamente).
- **Lista de servidores** del cliente, buscando por nombre o tags.
- **Favoritos / historial** en el cliente.

## 3.10 Actualizar el servidor (artefactos)

1. **Para** el servidor (desde txAdmin o cerrando la consola).
2. **Copia de seguridad** de `server-data` (o al menos `server.cfg`, `resources/` y `txData/`) y de la base de datos.
3. Borra el contenido de la carpeta `server/` (binarios) — **no** `server-data` ni `txData`.
4. Descomprime el nuevo artefacto *recommended* en `server/`.
5. Arranca y revisa la consola en busca de errores.

> Nunca mezcles archivos de versiones distintas de artefactos en la misma carpeta. Mantén la carpeta antigua unos días por si necesitas volver atrás.

## 3.11 Recursos base de `cfx-server-data`

| Recurso | Para qué sirve | ¿Necesario? |
|---|---|---|
| `mapmanager` | Gestiona mapas y gamemodes. | Sí, si usas `spawnmanager` |
| `spawnmanager` | Lógica de aparición/reaparición (`exports.spawnmanager:spawnPlayer`). | Si no tienes framework con su propio spawn |
| `sessionmanager` | Gestión de sesión de host (legado). | Recomendado |
| `chat` | Chat por defecto y sugerencias de comandos. | Recomendado |
| `basic-gamemode` | Gamemode mínimo. | Opcional |
| `hardcap` | Limita jugadores al `sv_maxclients`. | Recomendado |
| `rconlog` | Comandos `status`, `clientkick` y log RCON. | Opcional |
| `baseevents` | Eventos `baseevents:onPlayerDied`, `onPlayerKilled`, `enteredVehicle`, `leftVehicle`… | Opcional |
| `fivem-map-skater` / `fivem-map-hipster` | Mapas de ejemplo con puntos de aparición. | Opcional |
| `webpack` / `yarn` | *Builders* para recursos JS que usan dependencias npm. | Si los necesitas |
| `runcode` | Ejecutar código desde consola (solo desarrollo). | **No en producción** |
| `money`, `money-fountain`, `ped-money-drops`, `player-data` | Ejemplos educativos. | No |

---

# 4. `server.cfg` a fondo

El `server.cfg` es un archivo de **comandos de consola** que se ejecutan en orden al arrancar. Todo lo que pones ahí podrías escribirlo a mano en la consola del servidor.

## 4.1 `set`, `sets`, `setr` y `exec`

| Comando | Qué hace |
|---|---|
| `set nombre valor` | Define una **convar** solo en el servidor. |
| `sets nombre valor` | Define una convar **y la publica** en la lista de servidores (*server info*): tags, idioma, descripción… |
| `setr nombre valor` | Define una convar **replicada** a los clientes (se puede leer con `GetConvar` desde el cliente). |
| `exec archivo.cfg` | Ejecuta otro archivo `.cfg` (útil para separar permisos, secretos o recursos). Admite `@recurso/archivo.cfg`. |
| `#` o `//` | Comentarios. |

> **Nunca uses `setr` ni `sets` con secretos** (tokens, contraseñas, webhooks): los clientes o la lista pública podrían verlos. Usa `set`.

## 4.2 `server.cfg` completo y comentado

```cfg
## ======================================================
##  RED / PUERTOS
## ======================================================
endpoint_add_tcp "0.0.0.0:30120"
endpoint_add_udp "0.0.0.0:30120"

## ======================================================
##  IDENTIDAD DEL SERVIDOR (lista pública)
##  Desde el 21/10/2026 el nombre, la descripción, los tags, el banner y el
##  Discord que se ven en la lista se configuran en portal.cfx.re.
##  Mantén estas líneas igualmente (consola, txAdmin, recursos que las leen).
##  Límites: sv_projectName 40 caracteres, sv_hostname 120, sv_projectDesc 250.
## ======================================================
sv_hostname "^2Mi Servidor RP ^7| ^3Español ^7| Serious RP"
sets sv_projectName "Mi Servidor RP"
sets sv_projectDesc "Servidor de roleplay serio en español con economía realista."
sets tags "roleplay, rp, español, serious, economy"
sets locale "es-ES"
sets banner_detail "https://midominio.com/banner_detail.png"       # 1920x200 aprox.
sets banner_connecting "https://midominio.com/banner_connecting.png"
sets Discord "https://discord.gg/xxxx"
load_server_icon logo.png        # PNG 96x96 en la carpeta server-data

## ¿Mostrar candado de allowlist en la lista?
# sets sv_appearAllowlisted true
# sets sv_allowlistInstructions "Solicita acceso en nuestro Discord"

## ======================================================
##  LICENCIA / CLAVES
## ======================================================
sv_licenseKey "cfxk_XXXXXXXXXXXXXXXXXXXX_XXXXXX"
set steam_webApiKey "none"        # Pon tu API key de Steam si necesitas identificadores steam:

## ======================================================
##  JUGADORES / ONESYNC / BUILD
## ======================================================
sv_maxclients 48                  # >32 requiere OneSync; >64 requiere "onesync on"
set onesync on
sv_enforceGameBuild 3889          # The Kortz Center Heist (ver tabla de builds)
# set onesync_population true     # NPCs/tráfico (true por defecto)

## ======================================================
##  SEGURIDAD
## ======================================================
sv_scriptHookAllowed 0            # Nunca permitas ScriptHookV en servidores públicos
sv_endpointPrivacy true           # Oculta IPs de jugadores
sv_pureLevel 1                    # 0 = sin control; 1 = permite audio y gráficos conocidos; 2 = bloquea todo
set sv_entityLockdown relaxed     # inactive | relaxed | strict (ver sección 13)
set sv_filterRequestControl 2     # Bloquea robo de control de entidades de jugadores
setr sv_stateBagStrictMode false  # true = solo el servidor puede escribir state bags replicados
# rcon_password "xxxxx"           # Déjalo sin definir si no usas RCON
# sv_master1 ""                   # Servidor privado (oculta botón conectar; no lo quita de la lista)

## ======================================================
##  BASE DE DATOS (oxmysql)
## ======================================================
set mysql_connection_string "mysql://usuario:contraseña@127.0.0.1:3306/mi_base?charset=utf8mb4"
# Alternativa formato clave=valor:
# set mysql_connection_string "server=127.0.0.1;database=mi_base;userid=usuario;password=contraseña;charset=utf8mb4"
set mysql_slow_query_warning 200  # avisa de consultas lentas (ms)
# set mysql_ui true               # Interfaz /mysql (oxmysql)

## ======================================================
##  VOZ (pma-voice)
## ======================================================
setr voice_useNativeAudio true
setr voice_useSendingRangeOnly true
setr voice_defaultCycle "F11"

## ======================================================
##  RECURSOS (el ORDEN importa: dependencias primero)
## ======================================================
ensure mapmanager
ensure chat
ensure spawnmanager
ensure sessionmanager
ensure hardcap
ensure baseevents

ensure oxmysql
ensure ox_lib
# ensure es_extended   /  ensure qb-core  /  ensure qbx_core
ensure [framework]
ensure [ox]
ensure [scripts]
ensure [maps]
ensure [vehicles]

## ======================================================
##  PERMISOS (ver sección 6)
## ======================================================
add_ace group.admin command allow
add_ace group.admin command.quit deny
add_principal identifier.fivem:123456 group.admin
add_principal identifier.license:abcdef0123456789 group.admin

## Secretos en archivo aparte (añádelo a .gitignore)
exec secrets.cfg
```

`secrets.cfg` (no lo subas nunca al repositorio):

```cfg
sv_licenseKey "cfxk_..."
set mysql_connection_string "mysql://..."
set discord_bot_token "..."
```

## 4.3 Colores en el nombre del servidor

Códigos `^0`-`^9` (válidos en `sv_hostname`, chat y `print` de consola):

| Código | Color |
|---|---|
| `^0` | Blanco |
| `^1` | Rojo |
| `^2` | Verde |
| `^3` | Amarillo |
| `^4` | Azul |
| `^5` | Azul claro / cian |
| `^6` | Morado / violeta |
| `^7` | Blanco (reset) |
| `^8` | Rojo oscuro / naranja |
| `^9` | Gris / rosa (depende del contexto) |

> Desde febrero de 2026 la lista pública de servidores **no muestra los colores** del título y aplica límites de caracteres. Los colores siguen funcionando en la consola, el chat y `print`.

## 4.4 Orden de carga y dependencias

- Los recursos se arrancan **en el orden** en que aparecen los `ensure`.
- Si un recurso declara `dependency 'oxmysql'` en su manifest, FXServer intenta arrancar la dependencia antes; si no existe, el recurso **no arranca** (`Could not find dependency oxmysql for resource X`).
- Si un recurso usa exports de otro en el **primer tick** (al cargar el archivo), el otro debe estar arrancado antes.
- `ensure [categoria]` arranca **todo** lo que hay dentro, en orden alfabético de carpeta, después de resolver dependencias.

---

# 5. Comandos de consola y convars (referencia completa)

## 5.1 Comandos de recursos

| Comando | Descripción |
|---|---|
| `start <recurso>` | Arranca un recurso parado (acepta categoría). |
| `stop <recurso>` | Para un recurso (acepta categoría). |
| `ensure <recurso>` | Lo reinicia si está arrancado o lo arranca si no. **El más usado.** |
| `restart <recurso>` | Reinicia un recurso arrancado. |
| `refresh` | Reescanea `resources/` para detectar recursos nuevos o manifests modificados. |

## 5.2 Comandos globales y de gestión

| Comando | Descripción |
|---|---|
| `exec <archivo>` | Ejecuta un `.cfg`. |
| `quit [motivo]` | Apaga el servidor (con motivo opcional para los jugadores). |
| `status` | (rconlog) Lista jugadores: id, nombre, identificador, IP, ping. |
| `clientkick <id> <motivo>` | (rconlog) Expulsa a un jugador. |
| `say <mensaje>` | (chat) Mensaje en el chat como consola. |
| `svgui` | Muestra/oculta la interfaz de depuración del servidor (ImGui). |
| `profiler record <ticks>` / `profiler saveJSON <archivo>` | Perfilado del servidor (ver sección 21). |
| `con_addChannelFilter <filtro> <acción>` | Filtra canales de consola por regex (`noprint`, `drop`, `devonly`). |
| `con_removeChannelFilter <filtro> <acción>` | Quita un filtro. |
| `con_channelFilters` | Lista filtros activos. |

## 5.3 Convars de configuración

### Red y listado

| Convar | Valores / defecto | Descripción |
|---|---|---|
| `endpoint_add_tcp "ip:puerto"` | — | Crea un endpoint TCP. |
| `endpoint_add_udp "ip:puerto"` | — | Crea un endpoint UDP. |
| `netPort <puerto>` | — | Puerto primario usado para el listado/master y DNS. |
| `sv_endpoints "<ip:puerto> ..."` | — | Direcciones UDP a las que se pueden conectar los clientes (se elige una al azar si hay varias). |
| `sv_hostname` | — | Nombre del servidor. |
| `sets sv_projectName` / `sv_projectDesc` | — | Nombre y descripción del proyecto en la lista. |
| `gametype` / `mapname` | — | Texto mostrado en la lista. |
| `sv_lan` | `false` | Modo LAN: oculto de la lista pública y sin comprobación de licencia. |
| `sv_master1 ""` | — | Hace el servidor privado (desactiva el botón de conectar). |
| `sv_forceIndirectListing` | `false` | Publica la IP del proxy/override en lugar de la real. |
| `sv_listingIpOverride` / `sv_listingHostOverride` | — | Sustituye IP/host enviados al master. |
| `sv_registerMulticastDns` | `true` | Anuncia el servidor por mDNS en LAN. |
| `sv_tcpConnectionTimeoutSeconds` | `5` | Timeout de conexiones TCP inactivas. |
| `net_tcpConnLimit` | `16` | Conexiones TCP simultáneas por IP. |
| `sv_proxyIPRanges "cidr ..."` | — | Rangos considerados proxy inverso (para obtener la IP real). |
| `sv_httpFileServerProxyOnly` | `false` | Solo permite descargas del servidor de archivos desde `sv_proxyIPRanges`. |
| `sv_endpointPrivacy` | — | Oculta IPs de jugadores en informes públicos. |
| `sv_maxClients` | 1-2048 | Slots. >32 requiere OneSync; >64 requiere `onesync on`. |

### OneSync

| Convar | Defecto | Descripción |
|---|---|---|
| `onesync` | `on` | `on` / `legacy` / `off`. |
| `onesync_enableInfinity` | `true` | Sincronización a gran escala (solo al arrancar). |
| `onesync_population` | `true` | Generación de NPCs/tráfico. |
| `onesync_forceMigration` | `true` | Transfiere la propiedad de entidades cuando el owner se va. |
| `onesync_distanceCulling` | `true` | No sincroniza entidades lejanas. |
| `onesync_distanceCullVehicles` | `false` | Aplica *culling* también a vehículos. |
| `onesync_radiusFrequency` | `true` | Actualiza más a menudo las entidades cercanas. |
| `sv_useAccurateSends` | `true` | Envíos de estado según relevancia y distancia. |
| `sv_experimentalStateBagsHandler` | `true` | Serialización más rápida de state bags. |
| `sv_experimentalOnesyncPopulation` | `true` | Corrige el límite de IDs con población desactivada. |
| `sv_experimentalNetGameEventHandler` | `true` | Serialización más rápida de *game events*. |

### Seguridad

| Convar | Defecto | Descripción |
|---|---|---|
| `sv_scriptHookAllowed` | `false` | Permite clientes con ScriptHookV. **No lo actives.** |
| `sv_pureLevel` | — | `1` = permite audio y mods gráficos conocidos; `2` = bloquea todo archivo modificado. |
| `sv_entityLockdown` | `inactive` | `strict` (clientes no crean entidades), `relaxed` (bloquea entidades de script creadas por cliente), `inactive`. |
| `sv_filterRequestControl` | `0` | Filtra `REQUEST_CONTROL_EVENT` (ver tabla abajo). |
| `sv_filterRequestControlSettleTimer` | `30000` | ms hasta que una entidad se considera "asentada". |
| `setr sv_stateBagStrictMode` | `false` | `true` = solo el servidor modifica state bags replicados. |
| `sv_enableNetworkedSounds` | `true` | Permite `NETWORK_PLAY_SOUND_EVENT`. |
| `sv_enableNetworkedPhoneExplosions` | `false` | Permite `REQUEST_PHONE_EXPLOSION_EVENT`. |
| `sv_enableNetworkedScriptEntityStates` | `true` | Permite `SCRIPT_ENTITY_STATE_CHANGE_EVENT`. |
| `sv_enableNetEventReassembly` | `true` | Reensambla eventos de red grandes divididos. |
| `sv_netEventReassemblyMaxPendingEvents` | `100` | Máx. eventos pendientes por cliente (0-254). |
| `sv_netEventReassemblyUnlimitedPendingEvents` | `false` | Elimina ese límite. |
| `sv_requestParanoia` | `0` | Contra *floods* HTTP vía proxy (ver tabla abajo). |
| `sv_authMaxVariance` | `5` | 1-5: probabilidad de que cambie un identificador del proveedor. |
| `sv_authMinTrust` | `1` | 1-5: dificultad para falsificar la identidad. |
| `rcon_password` | (vacío) | Activa RCON (UDP). Vacío = desactivado. |
| `block_net_game_event <nombre>` | — | Bloquea un *net game event* por nombre (necesita `sv_experimentalNetGameEventHandler`, activado por defecto). |
| `unblock_net_game_event <nombre>` | — | Lo desbloquea. |

**`sv_filterRequestControl`:**

| Modo | Efecto |
|---|---|
| `-1` | Como `2` pero además avisa en consola. |
| `0` | Desactivado (defecto). También desactiva la política de buckets/lockdown para estas peticiones. |
| `1` | Bloquea peticiones de control sobre entidades controladas por jugadores (vehículos ocupados) ya "asentadas". |
| `2` | Bloquea peticiones sobre **todas** las entidades controladas por jugadores. |
| `3` | Como `2` + entidades no-jugador asentadas. |
| `4` | Nunca enruta `REQUEST_CONTROL_EVENT`. |

Cualquier modo distinto de `0` bloquea también las peticiones entre *routing buckets* distintos.

**Limitadores de frecuencia (*rate limiters*)**: FXServer limita cuántos eventos y escrituras de state bags acepta de cada cliente. Valores por defecto en Legacy:

| Limitador | Tasa (por segundo) | Ráfaga |
|---|---|---|
| `netEvent` | 50 | 200 |
| `netEventFlood` | 75 | 300 |
| `stateBag` | 75 | 125 |
| `stateBagFlood` | 150 | 175 |
| `stateBagSize` | 128 KiB | 256 KiB |
| `http_info` | 4 | 10 |
| `http_players` | 4 | 10 |
| `http_perf` | 2 | 5 |

Se ajustan con `set rateLimiter_<nombre>_rate <n>` y `set rateLimiter_<nombre>_burst <n>`. Si un recurso legítimo supera los límites (por ejemplo, porque envía eventos en un bucle), **arregla el recurso** en vez de subir los límites. Desde abril de 2025 el servidor también avisa en consola (y en txAdmin) de los eventos demasiado grandes.

**`sv_requestParanoia`:**

| Nivel | Efecto |
|---|---|
| `0` | Desactivado. |
| `1` | Bloquea IPs cuyas peticiones incluyan cabecera `Via`. |
| `2` | Además bloquea las que incluyan `Upgrade-Insecure-Requests` (afecta también a abrir los `.json` desde navegador). |
| `3` | Como `2` y además cierra el socket. |

### Otros

| Convar | Defecto | Descripción |
|---|---|---|
| `gamename` | `gta5` | Juego objetivo (`gta5`/`rdr3`). |
| `sv_enforceGameBuild` | — | Build del juego (solo al arrancar). |
| `sv_replaceExeToSwitchBuilds` | — | **Obsoleta** desde el artefacto 35245 (el cliente usa siempre el ejecutable más reciente y solo carga los DLC de la build fijada). |
| `setr sv_showBusySpinnerOnLoadingScreen` | `true` | `false` oculta el icono de carga de la pantalla de carga (desde marzo de 2025). |
| `load_server_icon <png>` | — | Icono 96x96. |
| `steam_webApiKey` | — | Necesario para obtener `steam:`. |
| `steam_webApiDomain` | `api.steampowered.com` | Dominio de la API de Steam. |
| `sv_prometheusBasicAuthUser` / `Password` | — | Autenticación del endpoint `/perf` (métricas Prometheus). |
| `sv_kvsName` | `default` | Nombre del archivo de KVP del servidor (solo al arrancar). |
| `sv_tebexSecret` | — | Clave de Tebex para la integración. |
| `increase_pool_size <pool> <n>` | — | Aumenta un *pool* de memoria del juego (ver 5.5). |

## 5.4 Game builds (`sv_enforceGameBuild`)

Cada build incluye el contenido de todas las anteriores.

| Número | Alias | DLC (nombre comercial) |
|---|---|---|
| `1` | — | Juego base sin DLC |
| `1604` | `xm18`, `christmas2018`, `mpchristmas2018` | Arena War (**por defecto**) |
| `2060` | `sum`, `mpsum` | Los Santos Summer Special (incluye Diamond Casino & Resort y Diamond Casino Heist) |
| `2189` | `h4`, `heist4`, `mpheist4` | Cayo Perico Heist |
| `2372` | `tuner`, `mptuner` | Los Santos Tuners |
| `2545` | `security`, `mpsecurity` | The Contract |
| `2612` | `mpg9ec` | Contenido "Expanded & Enhanced" |
| `2699` | `mpsum2` | The Criminal Enterprises |
| `2802` | `mpchristmas3` | Los Santos Drug Wars |
| `2944` | `mp2023_01` | San Andreas Mercenaries |
| `3095` | `mp2023_02` | The Chop Shop |
| `3258` | `mp2024_01` | Bottom Dollar Bounties |
| `3407` | `mp2024_02` | Agents of Sabotage |
| `3570` | `mp2025_01` | Money Fronts |
| `3751` | `mp2025_02` | A Safehouse in the Hills |
| `3889` | `mp2026_01` | **The Kortz Center Heist** (la más reciente a octubre de 2026; requiere artefacto **35245 o superior**) |

Consejos:

- Usa **la última build** salvo que algún recurso tuyo no sea compatible.
- Cambiar de build obliga a los jugadores a descargar el contenido del DLC la primera vez.
- Algunas builds nuevas requieren artefactos recientes: si el servidor no reconoce la build, **actualiza los artefactos**.
- Natives, hashes de vehículos/ropa y offsets de *drawables* pueden variar entre builds: prueba todo tras cambiar.

## 5.5 Pools (`increase_pool_size`)

Si ves errores como `Pool full: TxdStore` o `Exhausted pool`, puedes ampliar el *pool* (solo al arrancar, en `server.cfg`):

```cfg
increase_pool_size "TxdStore" 2000
increase_pool_size "FragmentStore" 2000
increase_pool_size "CMoveObject" 100
```

| Pool | Aumento máximo (FiveM) |
|---|---|
| `AnimStore` | 20480 |
| `AttachmentExtension` | 430 |
| `Building` | 20000 |
| `CMoveObject` | 600 |
| `CWeaponComponentInfo` | 2048 |
| `EntityDescPool` | 20480 |
| `fragInstGta` | 2000 |
| `FragmentStore` | 14000 |
| `InteriorProxy` | 450 |
| `LightEntity` | 1000 |
| `netGameEvent` | 400 |
| `Object` | 2000 |
| `ObjectIntelligence` | 512 |
| `OcclusionInteriorInfo` | 20 |
| `OcclusionPathNode` | 5000 |
| `OcclusionPortalEntity` | 750 |
| `OcclusionPortalInfo` | 750 |
| `PortalInst` | 225 |
| `ScaleformStore` | 200 |
| `StaticBounds` | 5000 |
| `TxdStore` | 26000 |

> Ampliar pools aumenta el uso de memoria del cliente. Hazlo solo cuando un error concreto lo indique.

---

# 6. Permisos: sistema ACE

FiveM tiene un sistema de permisos integrado basado en **ACE** (*Access Control Entries*) y **principals**.

## 6.1 Conceptos

- **Principal**: "quién". Ej.: `identifier.license:xxxx`, `identifier.discord:1234`, `identifier.fivem:5678`, `group.admin`, `resource.mi_recurso`, `builtin.everyone`.
- **Object (objeto)**: "qué". Ej.: `command`, `command.ban`, `mi_recurso.abrir_menu`, `vehicle.spawn`.
- **ACE**: regla `principal + objeto + allow/deny`.
- **Herencia**: `add_principal hijo padre` hace que el hijo herede los permisos del padre.
- Los objetos son jerárquicos con puntos: permitir `command` permite `command.lo_que_sea`, salvo que exista un `deny` más específico.
- `deny` siempre gana sobre `allow` del mismo nivel.

## 6.2 Comandos

```cfg
add_ace <principal> <objeto> <allow|deny>
remove_ace <principal> <objeto> <allow|deny>
add_principal <hijo> <padre>
remove_principal <hijo> <padre>
test_ace <principal> <objeto>          # comprueba si está permitido
list_aces                              # lista todas las ACE
list_principals                        # lista toda la herencia
```

## 6.3 Ejemplo de jerarquía completa

```cfg
# Grupos (de menor a mayor)
add_principal group.mod group.helper
add_principal group.admin group.mod
add_principal group.superadmin group.admin

# Permisos de cada grupo
add_ace group.helper chat.staff allow
add_ace group.mod command.kick allow
add_ace group.mod command.tp allow
add_ace group.admin command allow        # todos los comandos
add_ace group.admin command.quit deny    # menos apagar el servidor
add_ace group.superadmin command.quit allow

# Asignar jugadores
add_principal identifier.fivem:1234567 group.superadmin
add_principal identifier.license:1a2b3c4d5e6f group.admin
add_principal identifier.discord:123456789012345678 group.mod

# Permitir a un recurso ejecutar comandos (p. ej. que pueda usar ExecuteCommand)
add_ace resource.mi_admin command allow

# Permitir a un recurso arrancar/parar otros recursos
add_ace resource.mi_gestor command.start allow
add_ace resource.mi_gestor command.stop allow
add_ace resource.mi_gestor command.ensure allow
```

## 6.4 Usar ACE desde scripts

**Comandos restringidos** — con el tercer parámetro `true`, FiveM exige `command.<nombre>`:

```lua
RegisterCommand('anuncio', function(source, args, raw)
    local texto = table.concat(args, ' ')
    TriggerClientEvent('chat:addMessage', -1, { args = { '^1ANUNCIO', texto } })
end, true) -- restringido: requiere "command.anuncio"
```

**Comprobar permisos propios:**

```lua
-- servidor
if IsPlayerAceAllowed(source, 'mi_recurso.abrir_menu') then
    -- permitido
end
```

```cfg
add_ace group.admin mi_recurso.abrir_menu allow
```

**Añadir/quitar permisos en caliente desde un script** (el recurso necesita permiso para ejecutar `add_principal`):

```lua
ExecuteCommand(('add_principal identifier.%s group.admin'):format(license))
```

```cfg
add_ace resource.mi_admin command.add_principal allow
add_ace resource.mi_admin command.remove_principal allow
```

> Los frameworks (ESX, QBCore, Qbox) suelen tener su propio sistema de grupos que **se apoya** en ACE (`group.admin`, `qbcore.god`, etc.). Revisa su documentación para no duplicar.

---

# 7. Recursos y `fxmanifest.lua`

## 7.1 Estructura típica de un recurso

```
mi_recurso/
├── fxmanifest.lua        ← obligatorio
├── config.lua            ← configuración compartida
├── locales/
│   ├── es.lua
│   └── en.lua
├── client/
│   ├── main.lua
│   └── nui.lua
├── server/
│   ├── main.lua
│   └── db.lua
├── shared/
│   └── utils.lua
├── web/                  ← NUI (HTML/CSS/JS o build de React/Vue/Svelte)
│   └── dist/
│       ├── index.html
│       └── assets/...
├── stream/               ← assets de streaming (ytd, ydr, yft, ymap…)
├── data/                 ← metas (vehicles.meta, handling.meta…)
└── sql/
    └── install.sql
```

## 7.2 `fxmanifest.lua` mínimo

```lua
fx_version 'cerulean'
game 'gta5'

author 'TuNombre'
description 'Descripción del recurso'
version '1.0.0'

client_script 'client/main.lua'
server_script 'server/main.lua'
```

> **¿Y `lua54 'yes'`?** Desde **julio de 2025** Lua 5.3 está eliminado y **todo** Lua se ejecuta en 5.4, así que esa línea **ya no tiene efecto**. Dejarla no hace daño (la verás en casi todos los recursos de antes de 2025), pero no hace falta en recursos nuevos.

## 7.3 `fxmanifest.lua` completo con todas las directivas habituales

```lua
fx_version 'cerulean'          -- versión del formato de manifest
game 'gta5'                    -- 'gta5' | 'rdr3' | 'common'  (varios: games { 'gta5', 'rdr3' })
lua54 'yes'                    -- obsoleta desde 2025 (sin efecto); se suele dejar por compatibilidad
-- use_experimental_fxv2_oal 'yes' -- EXPERIMENTAL: invocación de natives más rápida en Lua
                                   -- (ojo: con esto un vector3 NO se desempaqueta solo; pasa .x, .y, .z)

name 'mi_recurso'
author 'TuNombre'
description 'Descripción'
version '1.2.3'
repository 'https://github.com/tu/mi_recurso'

-- Scripts (admiten globs: 'client/*.lua', 'client/**/*.lua')
shared_scripts {
    '@ox_lib/init.lua',         -- '@recurso/archivo' carga un archivo de OTRO recurso
    'config.lua',
    'shared/*.lua',
}
client_scripts {
    'client/*.lua',
}
server_scripts {
    '@oxmysql/lib/MySQL.lua',
    'server/*.lua',
}

-- NUI
ui_page 'web/dist/index.html'   -- o una URL: ui_page 'https://mi-web.com/ui'
files {
    'web/dist/index.html',
    'web/dist/assets/*.js',
    'web/dist/assets/*.css',
    'locales/*.json',
    'data/*.meta',
}

-- Archivos de datos del juego (metas)
data_file 'VEHICLE_METADATA_FILE' 'data/vehicles.meta'
data_file 'HANDLING_FILE'         'data/handling.meta'
data_file 'CARCOLS_FILE'          'data/carcols.meta'
data_file 'VEHICLE_VARIATION_FILE' 'data/carvariations.meta'

-- Dependencias (no arranca si faltan)
dependencies {
    '/server:12913',        -- build mínima de FXServer
    '/onesync',             -- requiere OneSync activo
    '/gameBuild:3095',      -- build mínima del juego (también acepta alias: '/gameBuild:mp2023_02')
    'oxmysql',
    'ox_lib',
}

-- Este recurso "proporciona" otro nombre (compatibilidad: p. ej. oxmysql provide 'mysql-async')
provide 'mysql-async'

-- Exports declarados (necesario en JS/C# para algunos casos; en Lua basta con exports(...) en el código)
exports { 'MiFuncionCliente' }
server_exports { 'MiFuncionServidor' }

-- Asset Escrow: archivos que quedan sin cifrar
escrow_ignore {
    'config.lua',
    'locales/*.lua',
}

-- Mapas
this_is_a_map 'yes'

-- Pantalla de carga
-- loadscreen 'loading/index.html'
-- loadscreen_manual_shutdown 'yes'

-- Recurso solo de servidor (no se anuncia al cliente)
-- server_only 'yes'

-- JS en servidor: versión de Node.js
-- node_version '22'
```

## 7.4 Referencia de directivas

| Directiva | Descripción |
|---|---|
| `fx_version` | Versión del formato. Usa siempre **`'cerulean'`**. Valores: `adamant` (dic. 2019), `bodacious` (feb. 2020), `cerulean` (actual); cada uno hereda del anterior. |
| `game` / `games` | Juego(s) objetivo: `gta5`, `rdr3`, `common`. |
| `resource_manifest_version` | GUID del formato antiguo `__resource.lua`. **Obsoleta.** |
| `lua54` | **Obsoleta y sin efecto** desde 2025: todo Lua es 5.4. Inofensiva si la dejas. |
| `use_experimental_fxv2_oal` | `'yes'` activa la invocación *One Argument List* en Lua (más rápida). **Experimental**: los `vector3` no se desempaquetan automáticamente al pasarlos a natives. |
| `node_version` | Versión de Node.js para `server_scripts` JS: `'16'` (defecto) o `'22'`. |
| `client_script(s)` | Scripts de cliente. |
| `server_script(s)` | Scripts de servidor (no se envían al cliente). |
| `shared_script(s)` | Scripts en ambos lados (se cargan **antes** que client/server). |
| `files` | Archivos accesibles por el cliente (NUI, JSON, metas). |
| `ui_page` | Página principal de NUI. |
| `loadscreen` | HTML de la pantalla de carga. |
| `loadscreen_manual_shutdown` | `'yes'` → la pantalla de carga se cierra cuando llames a `ShutdownLoadingScreenNui()`. |
| `data_file` | Registra un archivo de datos del juego (ver 15.6). Admite globs. |
| `this_is_a_map` | Marca el recurso como mapa. |
| `dependency` / `dependencies` | Recursos o requisitos necesarios: `'/server:4500'` (build mínima de FXServer), `'/onesync'`, `'/gameBuild:h4'` (mismos valores que `sv_enforceGameBuild`), `'/policy:subdir_file_mapping'`, `'/native:0xE27C97A0'` (exige que exista un native). |
| `provide` | Declara que este recurso sustituye a otro nombre. |
| `export(s)` / `server_export(s)` | Declara exports (sobre todo para JS/C#). |
| `escrow_ignore` | Archivos que el Asset Escrow deja sin cifrar. |
| `server_only` | `'yes'` → recurso exclusivamente de servidor. |
| `clr_disable_task_scheduler` | `'yes'` → desactiva el planificador de tareas de .NET (C#) para usar el propio. |
| `mono_rt2` | Runtime Mono v2 (C#) en fase piloto. **Su periodo de prueba caducó el 30 de junio de 2026**: en los artefactos actuales los recursos con `mono_rt2` **no se cargan**. Usa el runtime C# clásico (sin esta clave). |
| `convar_category` | Describe convars configurables del recurso (lo usan herramientas como FxDK). Tipos `CV_STRING`, `CV_BOOL`, `CV_INT`, `CV_SLIDER`, `CV_COMBI`, `CV_PASSWORD`, `CV_MULTI`. |
| `replace_level_meta` | Sustituye el `level.meta` (mapas totales). |
| `before_level_meta` / `after_level_meta` | **Obsoletas.** |
| Cualquier otra clave | Se convierte en **metadato** legible con `GetResourceMetadata(recurso, clave, índice)`. |

> **`__resource.lua`** es el formato antiguo (pre-2019). Está obsoleto: migra siempre a `fxmanifest.lua`.

## 7.5 Prefijo `@` y rutas

- `'@ox_lib/init.lua'` → carga `init.lua` del recurso `ox_lib` dentro del tuyo (se ejecuta en el contexto de tu recurso).
- Globs: `*` (archivos de una carpeta), `**` (recursivo). Ej.: `'web/dist/**/*'`.
- Las rutas son relativas a la carpeta del recurso y **sensibles a mayúsculas en Linux**.

## 7.6 Metadatos desde código

```lua
local version = GetResourceMetadata(GetCurrentResourceName(), 'version', 0)
print(('mi_recurso v%s cargado'):format(version))
```

## 7.7 Ciclo de vida de un recurso

1. `refresh` detecta el recurso y lee el manifest.
2. `ensure` → servidor dispara `onResourceStarting` (cancelable con `CancelEvent()`).
3. Se cargan los `shared_scripts` y luego los `server_scripts`.
4. Se dispara `onResourceStart` (servidor).
5. Los clientes conectados descargan los archivos (si han cambiado) y ejecutan `shared` + `client_scripts`; se dispara `onClientResourceStart` (cliente).
6. Al parar: `onResourceStop` (servidor) y `onClientResourceStop` (cliente). Las entidades creadas por *script* en el servidor se eliminan.

```lua
AddEventHandler('onResourceStart', function(resourceName)
    if resourceName ~= GetCurrentResourceName() then return end
    print('Arrancado: ' .. resourceName)
end)

AddEventHandler('onResourceStop', function(resourceName)
    if resourceName ~= GetCurrentResourceName() then return end
    -- limpiar: borrar entidades, cerrar NUI, guardar datos...
end)
```

## 7.8 Funciones de gestión de recursos (servidor)

| Native | Uso |
|---|---|
| `GetCurrentResourceName()` | Nombre del recurso actual. |
| `GetResourceState(nombre)` | `missing`, `started`, `starting`, `stopped`, `stopping`, `uninitialized`, `unknown`. |
| `GetNumResources()` / `GetResourceByFindIndex(i)` | Recorrer todos los recursos. |
| `GetResourcePath(nombre)` | Ruta absoluta del recurso (servidor). |
| `LoadResourceFile(nombre, ruta)` | Lee un archivo de un recurso (cliente y servidor). |
| `SaveResourceFile(nombre, ruta, datos, longitud)` | Escribe un archivo (servidor). Usa `-1` como longitud para todo el string. |
| `StartResource(nombre)` / `StopResource(nombre)` | Arrancar/parar (requiere ACE `command.start`/`command.stop` para el recurso). |
| `GetResourceMetadata(nombre, clave, i)` / `GetNumResourceMetadata(nombre, clave)` | Leer metadatos del manifest. |

```lua
-- Leer un JSON propio
local raw = LoadResourceFile(GetCurrentResourceName(), 'data/precios.json')
local precios = json.decode(raw or '{}')

-- Guardarlo
SaveResourceFile(GetCurrentResourceName(), 'data/precios.json', json.encode(precios, { indent = true }), -1)
```

---

# 8. Scripting: fundamentos comunes (todos los lenguajes)

Los ejemplos de esta sección están en **Lua**, que es el lenguaje más usado. En las secciones 10 y 11 tienes los equivalentes en JavaScript y C#.

## 8.1 Hilos (*threads*), `Wait` y el planificador

En FiveM no hay hilos reales: hay **corrutinas** que el planificador (*scheduler*) reanuda cada tick. Un bucle infinito **sin `Wait`** congela el juego.

```lua
-- Bucle que se ejecuta cada frame (Wait(0))
CreateThread(function()
    while true do
        DrawMarker(1, 200.0, -900.0, 30.0, 0, 0, 0, 0, 0, 0, 1.5, 1.5, 1.0, 0, 150, 255, 120, false, false, 2, false, nil, nil, false)
        Wait(0)
    end
end)
```

- `CreateThread(fn)` = `Citizen.CreateThread(fn)`.
- `Wait(ms)` = `Citizen.Wait(ms)`. Solo puede llamarse **dentro** de un thread (o de un handler, que en FiveM también es una corrutina).
- `Wait(0)` = esperar al siguiente frame.
- `SetTimeout(ms, fn)` = `Citizen.SetTimeout`: ejecuta una vez tras `ms`.
- `CreateThreadNow(fn)` = ejecuta inmediatamente hasta el primer `Wait`.

### Patrón de "espera dinámica" (el más importante para rendimiento)

```lua
local tienda = vec3(25.7, -1347.3, 29.49)

CreateThread(function()
    while true do
        local sleep = 1000                         -- lejos: comprobar 1 vez por segundo
        local coords = GetEntityCoords(PlayerPedId())
        local dist = #(coords - tienda)

        if dist < 20.0 then
            sleep = 0                              -- cerca: cada frame para dibujar
            DrawMarker(2, tienda.x, tienda.y, tienda.z, 0,0,0, 0,0,0, 0.3,0.3,0.3, 255,255,255,180, false,true,2,false,nil,nil,false)
            if dist < 1.5 then
                BeginTextCommandDisplayHelp('STRING')
                AddTextComponentSubstringPlayerName('Pulsa ~INPUT_CONTEXT~ para abrir la tienda')
                EndTextCommandDisplayHelp(0, false, true, -1)
                if IsControlJustReleased(0, 38) then  -- 38 = E
                    TriggerEvent('mi_tienda:abrir')
                end
            end
        end
        Wait(sleep)
    end
end)
```

## 8.2 Eventos

FiveM tiene un sistema de **eventos** con nombre (string) para comunicar código:

| Función | Desde | Hacia | Notas |
|---|---|---|---|
| `TriggerEvent(nombre, ...)` | Cualquier lado | El **mismo** lado (todos los recursos) | Local, no viaja por la red. |
| `TriggerServerEvent(nombre, ...)` | Cliente | Servidor | El servidor recibe el `source` del jugador. |
| `TriggerClientEvent(nombre, target, ...)` | Servidor | Cliente(s) | `target` = id del jugador o `-1` para todos. |
| `TriggerLatentServerEvent(nombre, bps, ...)` | Cliente | Servidor | Para datos grandes, se envía troceado a `bps` bytes/seg. |
| `TriggerLatentClientEvent(nombre, target, bps, ...)` | Servidor | Cliente(s) | Igual para servidor→cliente. |

**Registrar handlers:**

```lua
-- Evento solo local (otros recursos del mismo lado)
AddEventHandler('mi_recurso:algoLocal', function(dato)
    print(dato)
end)

-- Evento que puede llegar POR LA RED (obligatorio registrarlo como net event)
RegisterNetEvent('mi_recurso:algoRed', function(dato)
    print(dato)
end)

-- Forma antigua (equivalente)
RegisterNetEvent('mi_recurso:algoRed')
AddEventHandler('mi_recurso:algoRed', function(dato) end)
```

> Un evento que no está registrado con `RegisterNetEvent` **no se puede disparar desde el otro lado**. Esto es una medida de seguridad: registra como *net event* solo lo que de verdad deba llegar por red.

### Cliente → Servidor (con validación)

```lua
-- client.lua
RegisterCommand('pagar', function(_, args)
    local objetivo = tonumber(args[1])
    local cantidad = tonumber(args[2])
    TriggerServerEvent('banco:pagar', objetivo, cantidad)
end)
```

```lua
-- server.lua
RegisterNetEvent('banco:pagar', function(objetivo, cantidad)
    local src = source                       -- ¡guárdalo en local inmediatamente!
    if type(objetivo) ~= 'number' or type(cantidad) ~= 'number' then return end
    if cantidad <= 0 or cantidad > 100000 or cantidad ~= math.floor(cantidad) then return end
    if not GetPlayerName(objetivo) then return end                    -- jugador existe
    local dist = #(GetEntityCoords(GetPlayerPed(src)) - GetEntityCoords(GetPlayerPed(objetivo)))
    if dist > 5.0 then return end                                      -- tienen que estar cerca
    -- ... comprobar saldo en BD y transferir ...
end)
```

> **`source`** es una variable global que solo es válida al principio del handler. Si haces `Wait` o llamas a algo asíncrono, puede cambiar. Guárdala siempre en `local src = source`.

### Servidor → Cliente

```lua
-- server.lua
TriggerClientEvent('chat:addMessage', src, { args = { 'Banco', 'Pago realizado' } })
TriggerClientEvent('mi_hud:actualizar', -1, { hora = '12:00' })  -- a todos
```

### Cancelar eventos

```lua
AddEventHandler('chatMessage', function(source, name, message)
    if message:find('palabrota') then
        CancelEvent()
    end
end)
```

`WasEventCanceled()` permite saber si otro handler canceló el evento.

### Tipos de datos que se pueden enviar

Los argumentos se serializan con **MessagePack**: números, strings, booleanos, `nil`, tablas (arrays y diccionarios), vectores (`vector3`…). **No** se pueden enviar funciones (salvo como *function references*, ver 8.5), *handles* de entidad útiles (son locales: envía el **netId**), ni objetos con metatablas.

Límites prácticos: evita enviar eventos de más de unos pocos KB con frecuencia. Para datos grandes usa eventos **latentes** o reparte en fragmentos.

## 8.3 Patrón *callback* (petición/respuesta cliente⇄servidor)

FiveM no trae *callbacks* nativos de red; se implementan con dos eventos. La forma moderna es usar **`ox_lib`** (`lib.callback`) o el sistema de tu framework.

**Con ox_lib:**

```lua
-- server
lib.callback.register('mi_recurso:getSaldo', function(source)
    return ObtenerSaldo(source)
end)

-- client
local saldo = lib.callback.await('mi_recurso:getSaldo', false)
print('Saldo: ' .. saldo)
```

**Implementación propia (para entender cómo funciona):**

```lua
-- shared/callbacks.lua (versión simplificada)
if IsDuplicityVersion() then  -- true en servidor
    local cbs = {}
    function RegisterCallback(name, fn) cbs[name] = fn end
    RegisterNetEvent('cb:request', function(name, id, ...)
        local src = source
        if not cbs[name] then return end
        TriggerClientEvent('cb:response', src, id, cbs[name](src, ...))
    end)
else
    local pending, nextId = {}, 0
    RegisterNetEvent('cb:response', function(id, ...)
        if pending[id] then pending[id]:resolve({ ... }); pending[id] = nil end
    end)
    function AwaitCallback(name, ...)
        nextId += 1
        local p = promise.new()
        pending[nextId] = p
        TriggerServerEvent('cb:request', name, nextId, ...)
        return table.unpack(Citizen.Await(p))
    end
end
```

## 8.4 Exports

Los **exports** permiten llamar funciones de **otro recurso del mismo lado** (cliente↔cliente o servidor↔servidor).

```lua
-- recurso "mi_banco" (server)
exports('GetSaldo', function(src)
    return Saldos[src] or 0
end)
```

```lua
-- otro recurso (server)
local saldo = exports.mi_banco:GetSaldo(source)
-- equivalente: exports['mi_banco']:GetSaldo(source)
```

- Si el recurso exportador no está arrancado, la llamada lanza error: comprueba `GetResourceState('mi_banco') == 'started'`.
- Los argumentos y retornos se serializan (no pases objetos con métodos).
- Para **cliente→servidor** no hay exports: usa eventos o callbacks.

## 8.5 Referencias a funciones

Puedes pasar funciones a través de exports y eventos locales: FiveM crea una *function reference* que se puede llamar desde otro recurso (incluso de otro lenguaje). Útil para APIs de librerías (por ejemplo `lib.registerContext` recibe funciones `onSelect`).

## 8.6 Comandos

```lua
RegisterCommand('coche', function(source, args, rawCommand)
    -- source = 0 si se ejecuta desde la consola del servidor
    local modelo = args[1] or 'adder'
    -- ...
end, false) -- false = cualquiera puede usarlo; true = requiere ACE command.coche
```

Sugerencias en el chat (recurso `chat`):

```lua
TriggerEvent('chat:addSuggestion', '/coche', 'Spawnea un vehículo', {
    { name = 'modelo', help = 'Nombre del modelo, p. ej. adder' }
})
-- Para quitarla: TriggerEvent('chat:removeSuggestion', '/coche')
```

## 8.7 Teclas: `RegisterKeyMapping`

Asigna una tecla **configurable por el jugador** (Ajustes → Teclas → FiveM) a un comando. Es la forma recomendada en lugar de comprobar `IsControlPressed` cada frame.

```lua
RegisterCommand('+abrirInventario', function()
    AbrirInventario()
end, false)
RegisterCommand('-abrirInventario', function() end, false) -- al soltar

RegisterKeyMapping('+abrirInventario', 'Abrir inventario', 'keyboard', 'TAB')
```

- Mapeadores: `keyboard`, `mouse_button` (`MOUSE_LEFT`, `MOUSE_RIGHT`, `MOUSE_MIDDLE`, `MOUSE_EXTRABTN1`…), `mouse_wheel` (`IOM_WHEEL_UP/DOWN`), `pad_digitalbuttonany` (mando), etc.
- Comandos con prefijo `+`/`-` → se ejecuta `+` al pulsar y `-` al soltar.
- El jugador puede reasignarla; la tecla por defecto solo se aplica la primera vez.
- Ocultar el comando del chat: no añadas sugerencia o usa nombres que empiecen por `+`.
- `SetKeyMappingHideResources(true)` oculta el nombre del recurso en el menú de teclas del jugador.

## 8.8 Controles del juego

Para detectar teclas puntuales (sin keymapping):

```lua
if IsControlJustPressed(0, 38) then end      -- E (INPUT_CONTEXT)
DisableControlAction(0, 24, true)             -- desactiva disparar (INPUT_ATTACK) este frame
```

Controles frecuentes:

| ID | Nombre | Tecla por defecto |
|---|---|---|
| 22 | INPUT_JUMP | Espacio |
| 23 | INPUT_ENTER | F |
| 24 | INPUT_ATTACK | Clic izq. |
| 25 | INPUT_AIM | Clic der. |
| 38 | INPUT_PICKUP | E |
| 51 | INPUT_CONTEXT | E |
| 44 | INPUT_COVER | Q |
| 45 | INPUT_RELOAD | R |
| 47 | INPUT_DETONATE | G |
| 73 | INPUT_VEH_DUCK | X |
| 166 | INPUT_SELECT_CHARACTER_MICHAEL | F5 |
| 167 | INPUT_SELECT_CHARACTER_FRANKLIN | F6 |
| 168 | INPUT_SELECT_CHARACTER_TREVOR | F7 |
| 170 | INPUT_SAVE_REPLAY_CLIP | F3 |
| 177 | INPUT_CELLPHONE_CANCEL | Backspace / Esc / clic der. |
| 182 | INPUT_CELLPHONE_CAMERA_FOCUS_LOCK | L |
| 199 | INPUT_FRONTEND_PAUSE | P |
| 200 | INPUT_FRONTEND_PAUSE_ALTERNATE | Esc |
| 244 | INPUT_INTERACTION_MENU | M |
| 245 | INPUT_MP_TEXT_CHAT_ALL | T |
| 246 | INPUT_MP_TEXT_CHAT_TEAM | Y |
| 249 | INPUT_PUSH_TO_TALK | N |
| 288 / 289 | F1 / F2 | F1 / F2 |
| 311 | INPUT_REPLAY_SHOWHOTKEY | K |
| 322 | ESC | Esc |

Lista completa: https://docs.fivem.net/docs/game-references/controls/

## 8.9 Convars desde scripts

```lua
local maxJugadores = GetConvarInt('sv_maxclients', 48)
local debug = GetConvar('mi_recurso_debug', 'false') == 'true'
local token = GetConvar('discord_bot_token', '')   -- 'set' → solo legible en servidor
```

- En el **cliente** solo puedes leer convars definidas con `setr`.
- Desde el servidor puedes cambiarlas: `SetConvar('x', 'y')`, `SetConvarReplicated('x','y')`, `SetConvarServerInfo('x','y')`.
- Para booleanos y decimales, lo más compatible es leer con `GetConvar` y convertir (`== 'true'`, `tonumber`).

## 8.10 KVP (almacenamiento clave-valor)

FiveM incluye un almacén **clave-valor persistente** por recurso:

- **Cliente**: se guarda en el PC del jugador, por servidor. Ideal para preferencias (posición del HUD, volumen).
- **Servidor**: se guarda en la carpeta del servidor (`db/`), nombre configurable con `sv_kvsName`.

```lua
SetResourceKvp('hud_pos', json.encode({ x = 0.1, y = 0.9 }))
SetResourceKvpInt('volumen', 70)
SetResourceKvpFloat('escala', 1.25)

local pos = json.decode(GetResourceKvpString('hud_pos') or '{}')
local vol = GetResourceKvpInt('volumen')
DeleteResourceKvp('hud_pos')

-- Recorrer claves con prefijo
local handle = StartFindKvp('jugador:')
if handle ~= -1 then
    local key
    repeat
        key = FindKvp(handle)
        if key then print(key, GetResourceKvpString(key)) end
    until not key
    EndFindKvp(handle)
end
```

Variantes asíncronas `SetResourceKvpNoSync`, `SetResourceKvpIntNoSync`, `SetResourceKvpFloatNoSync` y `DeleteResourceKvpNoSync`, seguidas de `FlushResourceKvp()`, para escribir en lote sin bloquear (en el cliente desde abril de 2025).

En el cliente, `GetExternalKvpString/Int/Float(recurso, clave)` y `StartFindExternalKvp` leen el KVP de **otro** recurso.

> El KVP **no** sustituye a una base de datos para datos de jugadores en servidores grandes, pero es perfecto para configuración y caché sencilla.

## 8.11 HTTP: peticiones salientes y endpoints propios

**Peticiones salientes (servidor):**

```lua
PerformHttpRequest('https://api.ejemplo.com/data', function(status, body, headers, errorData)
    if status ~= 200 then
        print('Error HTTP', status, errorData)
        return
    end
    local data = json.decode(body)
end, 'POST', json.encode({ hola = 'mundo' }), { ['Content-Type'] = 'application/json' })
```

**Webhook de Discord:**

```lua
local WEBHOOK = GetConvar('mi_webhook', '')

local function logDiscord(titulo, descripcion, color)
    PerformHttpRequest(WEBHOOK, function() end, 'POST', json.encode({
        username = 'Logs',
        embeds = { {
            title = titulo,
            description = descripcion,
            color = color or 3447003,
            footer = { text = os.date('%d/%m/%Y %H:%M:%S') },
        } }
    }), { ['Content-Type'] = 'application/json' })
end
```

**Endpoint HTTP propio** — accesible en `http://IP:30120/<nombre_recurso>/...`:

```lua
SetHttpHandler(function(req, res)
    -- req.method, req.path, req.headers, req.address, req.setDataHandler(cb)
    if req.path == '/estado' then
        res.writeHead(200, { ['Content-Type'] = 'application/json' })
        res.send(json.encode({ jugadores = #GetPlayers() }))
        return
    end
    res.writeHead(404)
    res.send('No encontrado')
end)
```

**Versión síncrona** (dentro de un thread o handler, servidor):

```lua
local status, body, headers = PerformHttpRequestAwait('https://api.ejemplo.com/data', 'GET')
```

Para leer el cuerpo de un POST en `SetHttpHandler`:

```lua
req.setDataHandler(function(body)
    local data = json.decode(body)
    -- ...
end)
```

> Protege los endpoints con un token (cabecera `Authorization`) y no expongas acciones peligrosas.

## 8.12 Utilidades comunes

| Función | Lado | Descripción |
|---|---|---|
| `IsDuplicityVersion()` | Ambos | `true` en servidor, `false` en cliente (útil en `shared`). |
| `GetGameTimer()` | Ambos | ms desde el arranque (monótono). Ideal para *cooldowns*. |
| `GetGameName()` | Ambos | `'fivem'`, `'redm'`… |
| `GetHashKey('adder')` / `` `adder` `` | Ambos | Hash Joaat de un string. |
| `json.encode` / `json.decode` | Ambos | JSON integrado. |
| `msgpack.pack` / `msgpack.unpack` | Ambos | MessagePack. |
| `os.time()`, `os.date()` | Servidor (y cliente parcial) | Fecha/hora. En cliente `os` está limitado; usa `GetLocalTime`/`GetUtcTime`. |
| `print(...)` | Ambos | Imprime en consola (F8 en cliente). |
| `GetInvokingResource()` | Ambos | Qué recurso llamó al export/evento actual (útil para seguridad). |

### Cooldown simple por jugador (servidor)

```lua
local cooldowns = {}

local function enCooldown(src, ms)
    local ahora = GetGameTimer()
    if cooldowns[src] and ahora - cooldowns[src] < ms then return true end
    cooldowns[src] = ahora
    return false
end

AddEventHandler('playerDropped', function() cooldowns[source] = nil end)
```

## 8.13 Eventos del sistema más importantes

### Servidor

| Evento | Parámetros | Cuándo |
|---|---|---|
| `playerConnecting` | `name, setKickReason, deferrals` | Un jugador intenta conectarse (ver 8.14). |
| `playerJoining` | `oldId` (id temporal) | El jugador ya tiene id definitivo y está entrando. |
| `playerDropped` | `reason` | El jugador se desconecta (`source` = su id). |
| `onResourceStart` / `onResourceStop` / `onResourceStarting` | `resourceName` | Ciclo de vida de recursos. |
| `onServerResourceStart` / `onServerResourceStop` | `resourceName` | Variantes de servidor. |
| `rconCommand` | `commandName, args` | Comando recibido por RCON. |
| `playerEnteredScope` / `playerLeftScope` | `data` (`data.player`, `data['for']`) | OneSync: un jugador entra/sale del rango de otro. |
| `entityCreating` | `handle` | OneSync: una entidad va a crearse (cancelable). |
| `entityCreated` / `entityRemoved` | `handle` | OneSync: entidad creada/eliminada. |
| `onPlayerBucketChange` / `onEntityBucketChange` | | Cambio de routing bucket. |
| `weaponDamageEvent` | `sender, data` | Daño de arma (cancelable). |
| `explosionEvent` | `sender, ev` | Explosión (cancelable). |
| `startProjectileEvent` | `sender, data` | Disparo de proyectil. |
| `ptFxEvent` | `sender, data` | Efecto de partículas en red. |
| `clearPedTasksEvent` | `sender, data` | Intento de limpiar tareas de un ped (anti-cheat). |
| `giveWeaponEvent` / `removeWeaponEvent` / `removeAllWeaponsEvent` | `sender, data` | Dar/quitar armas por red. |
| `fireEvent` | `sender, data` | Fuego. |
| `respawnPlayerPedEvent` | `sender, data` | Reaparición. |
| `vehicleComponentControlEvent` | | Control de componentes de vehículo. |

### Cliente

| Evento | Parámetros | Cuándo |
|---|---|---|
| `onClientResourceStart` / `onClientResourceStop` | `resourceName` | Ciclo de vida en cliente. |
| `gameEventTriggered` | `name, args` | Eventos internos del juego (`CEventNetworkEntityDamage`, `CEventNetworkPlayerEnteredVehicle`…). |
| `populationPedCreating` | `x, y, z, model, setters` | Va a aparecer un NPC (cancelable / modificable). |
| `playerSpawned` | `spawnInfo` | (spawnmanager) El jugador ha aparecido. |
| `baseevents:onPlayerDied` / `onPlayerKilled` / `onPlayerWasted` | | (baseevents) Muerte. |
| `baseevents:enteredVehicle` / `leftVehicle` / `enteringVehicle` | | (baseevents) Vehículos. |

**Detectar daño con `gameEventTriggered`:**

```lua
AddEventHandler('gameEventTriggered', function(name, args)
    if name ~= 'CEventNetworkEntityDamage' then return end
    local victima, atacante = args[1], args[2]
    local murio = args[6] == 1
    local arma = args[7]
    if victima == PlayerPedId() and murio then
        print('Me ha matado', atacante, 'con', arma)
    end
end)
```

## 8.14 Conexión de jugadores: `playerConnecting` y *deferrals*

Los **deferrals** permiten retener la conexión para hacer comprobaciones (ban, allowlist, Discord…):

```lua
AddEventHandler('playerConnecting', function(name, setKickReason, deferrals)
    local src = source
    deferrals.defer()                 -- obligatorio antes de cualquier Wait
    Wait(0)                           -- siempre un frame tras defer()
    deferrals.update(('Hola %s, comprobando tu cuenta...'):format(name))

    local license = GetPlayerIdentifierByType(src, 'license')
    if not license then
        return deferrals.done('No se ha encontrado tu licencia de Rockstar.')
    end

    if EstaBaneado(license) then
        return deferrals.done('Estás baneado. Apela en discord.gg/xxxx')
    end

    deferrals.done()                  -- sin argumento = permitir
end)
```

- `deferrals.defer()` – empezar a retener.
- `deferrals.update(texto)` – mensaje de progreso.
- `deferrals.presentCard(cardJson, callback)` – muestra una **Adaptive Card** (formularios, botones). Ver https://adaptivecards.io/designer/
- `deferrals.handover(tabla)` – adjunta datos de *handover* a la conexión del cliente (uso avanzado; p. ej. lo usan pantallas de carga para recibir datos del servidor).
- `deferrals.done(motivo?)` – terminar: sin motivo = aceptar; con motivo = rechazar.

**Adaptive Card con botón:**

```lua
local card = {
    type = 'AdaptiveCard',
    version = '1.3',
    body = {
        { type = 'TextBlock', text = 'Normas del servidor', weight = 'Bolder', size = 'Large' },
        { type = 'TextBlock', text = 'Al entrar aceptas las normas.', wrap = true },
    },
    actions = {
        { type = 'Action.Submit', title = 'Acepto', data = { acepto = true } },
    },
}
deferrals.presentCard(json.encode(card), function(data, rawData)
    if data.acepto then deferrals.done() else deferrals.done('Debes aceptar las normas') end
end)
```

## 8.15 Funciones de jugador en el servidor

| Native | Descripción |
|---|---|
| `GetPlayers()` | Lista (strings) de ids conectados. |
| `GetPlayerName(src)` | Nombre. |
| `GetPlayerIdentifiers(src)` | Todos los identificadores. |
| `GetPlayerIdentifierByType(src, 'license')` | Un identificador concreto. |
| `GetNumPlayerIdentifiers(src)` / `GetPlayerIdentifier(src, i)` | Recorrerlos uno a uno. |
| `GetPlayerTokens(src)` / `GetNumPlayerTokens` / `GetPlayerToken(src, i)` | Tokens de hardware. |
| `GetPlayerPing(src)` | Ping. |
| `GetPlayerEndpoint(src)` | IP:puerto. |
| `GetPlayerPed(src)` | Ped del jugador (OneSync). |
| `GetPlayerLastMsg(src)` | ms desde el último mensaje recibido. |
| `GetPlayerGuid(src)` | GUID. |
| `DropPlayer(src, motivo)` | Expulsar. |
| `IsPlayerAceAllowed(src, objeto)` | Comprobación ACE. |
| `GetPlayerRoutingBucket(src)` / `SetPlayerRoutingBucket(src, b)` | Routing buckets. |
| `Player(src).state` | State bag del jugador. |

```lua
local function getIdentificadores(src)
    local ids = {}
    for _, id in ipairs(GetPlayerIdentifiers(src)) do
        local tipo, valor = id:match('([^:]+):(.+)')
        ids[tipo] = valor
    end
    return ids
end
```

---

# 9. Lua en FiveM (CfxLua 5.4)

## 9.1 Qué Lua usa FiveM

- **CfxLua**: una versión modificada de **Lua 5.4.8** basada en *LuaGLM*.
- **Lua 5.3 se eliminó**: anunciado el 24 de junio de 2025 y retirado de producción a finales de julio de 2025. **Todos** los scripts Lua se ejecutan ahora en 5.4, con o sin `lua54 'yes'`.
- Incluye tipos de vector nativos (GLM), extensiones de sintaxis y librerías integradas (`json`, `msgpack`, `promise`).

## 9.2 Cambios de 5.3 → 5.4 que pueden romper scripts antiguos

Si heredas recursos viejos, revisa estos puntos (los anunció Cfx.re al eliminar 5.3):

| Cambio | Qué pasa | Solución |
|---|---|---|
| Sin conversión automática string→número en aritmética y operaciones de bits | `"10" + 5` puede fallar | `tonumber("10") + 5` |
| Literales enteros decimales que desbordan pasan a ser *float* | Números gigantes cambian de tipo | Usa `math.tointeger` o strings |
| `__lt` ya no emula `__le` | Metatablas con solo `__lt` fallan en `<=` | Define `__le` |
| Bucles `for` numéricos | Cambia el comportamiento en casos límite (desbordamiento, paso 0) | Revisa bucles con pasos raros |
| Reglas nuevas de etiquetas `goto` | Errores de compilación en código antiguo con `goto` | Renombra/mueve etiquetas |
| `json.decode` más estricto | No acepta corchetes sueltos, valores sin clave ni claves numéricas en ciertos formatos | Valida el JSON |
| `print` no llama a `tostring` | Usa `__tostring` directamente | Normalmente no afecta |
| `math.random` sembrado aleatoriamente | Ya no hace falta `math.randomseed(os.time())` | Quítalo si quieres |
| `utf8` rechaza *surrogates* | Strings UTF-8 inválidas fallan | Limpia los datos |
| `collectgarbage("setpause"/"setstepmul")` obsoletos | | Usa `collectgarbage("incremental", ...)` |
| `io.lines` devuelve 4 valores | | Normalmente no afecta |

Además, 5.4 añade **variables `<const>` y `<close>`**:

```lua
local MAX_JUGADORES <const> = 64
```

## 9.3 Extensiones de sintaxis de CfxLua

| Extensión | Ejemplo | Equivale a |
|---|---|---|
| **Hash en compilación** (backticks) | `` local h = `adder` `` | `GetHashKey('adder')` (calculado al compilar, más rápido) |
| `joaat(str[, ignoreCase])` | `joaat('adder')` | Hash Joaat en tiempo de ejecución |
| **Operadores compuestos** | `x += 1`, `x -= 1`, `n *= 2`, `n /= 2`, `n <<= 1`, `n >>= 1`, `n &= 3`, `n \|= 4`, `n ^= 2` | `x = x + 1`, etc. |
| **Navegación segura** | `local z = jugador?.coords?.z` | `jugador and jugador.coords and jugador.coords.z` |
| Navegación segura en llamadas y asignaciones (2025) | `obj?.metodo()`, `obj?.valor = 1` | Solo si `obj` no es `nil` |
| **Desempaquetado `in`** | `local x, y, z in coords` | `local x, y, z = coords.x, coords.y, coords.z` |
| **Constructor de conjuntos** | `local s = { .a, .b }` | `{ a = true, b = true }` |
| **Comentarios estilo C** | `/* comentario */` | `--[[ comentario ]]` |
| `each(t)` | `for k, v in each(t) do end` | Iteración genérica (respeta `__iter`) |
| `defer(fn)` | Función que se ejecuta al salir del ámbito | (función de la librería base, no una sentencia) |

> Operadores compuestos disponibles: `+=  -=  *=  /=  <<=  >>=  &=  |=  ^=`. **No** existen `++`, `--` (que en Lua es un comentario) ni `..=`.

Funciones extra en librerías estándar (estilo *WoW*): `table.create`, `table.wipe`, `table.clone`, `table.type`, `string.strjoin`, `string.strtrim`, `string.strsplit`, `string.strconcat`, `string.tostringall`, `scrub`.

## 9.4 Vectores y cuaterniones

```lua
local a = vector3(100.0, 200.0, 30.0)   -- alias corto: vec3(...)
local b = vec3(110.0, 205.0, 30.0)

local distancia = #(a - b)               -- # = magnitud → distancia
local suma = a + b
local escalado = a * 2.0
local xy = a.xy                          -- swizzling → vector2
local normalizado = a / #a               -- vector unitario

local glm = require 'glm'                -- librería GLM completa
local producto = glm.dot(a, b)
local perpendicular = glm.cross(a, b)

local v2 = vec2(1.0, 2.0)
local v4 = vec4(1.0, 2.0, 3.0, 4.0)      -- típico para coords + heading: vec4(x, y, z, h)
local q = quat(1.0, 0.0, 0.0, 0.0)

print(a)                                 -- vector3(100.0, 200.0, 30.0)
print(type(a))                           -- 'vector3'
```

- `GetEntityCoords` devuelve un `vector3`. Compara distancias con `#(a - b) < 5.0` en lugar de `GetDistanceBetweenCoords` (más lento).
- Para guardar un vector en JSON: `{ x = v.x, y = v.y, z = v.z }` (luego `vec3(t.x, t.y, t.z)`).
- `require 'glm'` da acceso a la librería GLM completa (matrices, funciones matemáticas avanzadas).

## 9.5 Librerías y globales integradas

| Global | Descripción |
|---|---|
| `json` | `json.encode(t, { indent = true })`, `json.decode(s)`. Implementación nativa (*rapidjson*). |
| `msgpack` | `msgpack.pack(...)`, `msgpack.unpack(s)` (*cmsgpack* nativo). |
| `promise` | `promise.new()`, `p:resolve(v)`, `p:reject(e)`, `promise.all`, `promise.first`, `promise.map`. |
| `Citizen.Await(p)` | Espera una promesa (dentro de thread/handler). Lanza error si se rechaza. |
| `CreateThread`, `Wait`, `SetTimeout`, `ClearTimeout` | Planificador. |
| `exports` | Exports. |
| `GlobalState`, `Entity`, `Player`, `LocalPlayer` | State bags. |
| `vector2/3/4`, `vec2/3/4`, `quat` | Vectores. |
| `require` | Solo módulos integrados (`'glm'`, `'lmprof'`). Para módulos propios usa `shared_scripts` o `require` de **ox_lib**. |
| `IsDuplicityVersion()` | `true` en servidor. |

### Promesas y await

```lua
local function esperarRespuesta()
    local p = promise.new()
    SetTimeout(1000, function() p:resolve('hecho') end)
    return Citizen.Await(p)
end

CreateThread(function()
    print(esperarRespuesta())   -- 'hecho' (tras 1s)
end)
```

## 9.6 Estilo y buenas prácticas en Lua

- Usa **`local`** siempre. Las globales son más lentas y chocan entre archivos del mismo recurso (todos los scripts de un mismo lado de un recurso comparten el entorno global).
- Cachea natives que llamas mucho en bucles calientes: `local GetEntityCoords = GetEntityCoords`.
- No llames a `PlayerPedId()` miles de veces por frame; guárdalo en una variable o usa `cache.ped` (ox_lib).
- Prefiere **tablas indexadas por clave** (`tabla[id]`) a recorrer arrays para buscar.
- `table.concat` en lugar de concatenar strings en bucles.
- `('%s tiene %d$'):format(nombre, dinero)` para formatear.
- Maneja errores con `pcall`/`xpcall` en código que llama a otros recursos:

```lua
local ok, res = pcall(function()
    return exports.otro_recurso:Algo()
end)
if not ok then print('^1Error: ' .. tostring(res) .. '^0') end
```

## 9.7 Módulos y organización

Dentro de un recurso, los archivos del mismo lado comparten el **entorno global**, así que puedes declarar una tabla y usarla en otros archivos:

```lua
-- shared/config.lua
Config = {}
Config.Debug = false
Config.Tiendas = {
    { nombre = '24/7 Grove', coords = vec3(-47.5, -1757.5, 29.4) },
}
```

```lua
-- client/main.lua
for _, t in ipairs(Config.Tiendas) do
    -- crear blips...
end
```

Con **ox_lib** puedes usar `require` para módulos con ámbito propio (los archivos deben estar en `files` si son de cliente):

```lua
-- modules/utils.lua
local M = {}
function M.redondear(n, d) local m = 10 ^ (d or 0); return math.floor(n * m + 0.5) / m end
return M

-- client/main.lua
local utils = require 'modules.utils'
print(utils.redondear(3.14159, 2))
```

## 9.8 Autocompletado en el editor (VS Code)

- La extensión **"CfxLua IntelliSense"** (`overextended/cfxlua-vscode`) está **descontinuada**, y su *fork* de CommunityOx pertenece a una organización archivada.
- Recomendación actual: **`overextended/fivem-lls-addon`** (natives regenerados semanalmente) con la extensión **Lua** de *sumneko/LuaLS*.

Pasos:

1. Clona el addon: `git clone https://github.com/overextended/fivem-lls-addon`.
2. Crea la variable de entorno `CFX_LUALS_ADDON` apuntando a esa carpeta.
3. Crea `.luarc.json` en tu proyecto:

```json
{
  "runtime": {
    "version": "Lua 5.4",
    "nonstandardSymbol": ["/**/", "`", "+=", "-=", "*=", "/=", "<<=", ">>=", "&=", "|=", "^="],
    "plugin": "${env:CFX_LUALS_ADDON}/plugin.lua"
  },
  "workspace": {
    "library": ["${env:CFX_LUALS_ADDON}/library"]
  }
}
```

4. Añade a `workspace.library` las rutas de las librerías que uses (por ejemplo, tu copia de `ox_lib`) para tener autocompletado de sus funciones.

---

# 10. JavaScript y TypeScript

## 10.1 Entornos

| Lado | Motor | Qué tienes |
|---|---|---|
| Cliente | **V8** (sin Node) | ES moderno, `setTick`, natives globales, `fetch` **no** (usa eventos/NUI). Sin `require` de npm (empaqueta con un *bundler*). |
| Servidor | **Node.js** (16 por defecto, 22 con `node_version '22'`) | `require`/`import` de npm, `fs`, `path`, `http`, `crypto`, `fetch` (Node 18+ → con Node 22), `async/await`. |

## 10.2 Manifest

```lua
fx_version 'cerulean'
game 'gta5'
node_version '22'

client_script 'dist/client.js'
server_script 'dist/server.js'
```

## 10.3 API básica

```js
// ===== client.js =====
setTick(() => {
  // cada frame (equivale a Wait(0)); evita trabajo pesado aquí
});

// Bucle con espera
const delay = (ms) => new Promise((r) => setTimeout(r, ms));
(async () => {
  while (true) {
    const ped = PlayerPedId();
    const [x, y, z] = GetEntityCoords(ped, true);
    await delay(1000);
  }
})();

on('miRecurso:local', (dato) => console.log(dato));   // AddEventHandler
onNet('miRecurso:red', (dato) => console.log(dato));  // RegisterNetEvent + handler
emit('miRecurso:local', 123);                         // TriggerEvent
emitNet('miRecurso:alServidor', { a: 1 });            // TriggerServerEvent

RegisterCommand('hola', (source, args, raw) => {
  emit('chat:addMessage', { args: ['Sistema', `Hola ${args.join(' ')}`] });
}, false);

exports('MiExport', (a, b) => a + b);
const resultado = exports.otro_recurso.OtraFuncion(1, 2);
```

```js
// ===== server.js =====
onNet('miRecurso:alServidor', (data) => {
  const src = global.source;        // ¡guárdalo!
  console.log(`Jugador ${GetPlayerName(src)} envió`, data);
  emitNet('miRecurso:red', src, 'respuesta'); // TriggerClientEvent(src)
  emitNet('miRecurso:red', -1, 'a todos');
});

on('playerConnecting', (name, setKickReason, deferrals) => {
  const src = global.source;
  deferrals.defer();
  setTimeout(() => {
    deferrals.update(`Comprobando a ${name}...`);
    deferrals.done();
  }, 0);
});

on('playerDropped', (reason) => {
  console.log(`${GetPlayerName(global.source)} salió: ${reason}`);
});
```

## 10.4 Diferencias importantes respecto a Lua

- Los natives que en Lua devuelven varios valores en JS devuelven **arrays**: `const [x, y, z] = GetEntityCoords(ped)`.
- Los vectores son arrays `[x, y, z]`, no objetos `vector3`.
- Hashes: `GetHashKey('adder')` (no existe la sintaxis de backticks de CfxLua).
- `source` está en `global.source` (o simplemente `source` en el ámbito global del servidor).
- Los timers (`setTimeout`, `setInterval`) existen en ambos lados y se integran en el *scheduler* de FiveM.
- Usa `Wait` solo en Lua; en JS usa `await new Promise(r => setTimeout(r, ms))`.
- `setTick` devuelve un id: `clearTick(id)` para pararlo.

## 10.5 TypeScript con tipos oficiales

```bash
npm init -y
npm i -D typescript esbuild @citizenfx/client @citizenfx/server @types/node
```

`tsconfig.json` (cliente):

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "types": ["@citizenfx/client"],
    "outDir": "dist"
  },
  "include": ["src/client/**/*"]
}
```

Build con esbuild (`build.js`):

```js
const esbuild = require('esbuild');

const comunes = { bundle: true, minify: true, sourcemap: false, logLevel: 'info' };

Promise.all([
  esbuild.build({ ...comunes, entryPoints: ['src/client/main.ts'], outfile: 'dist/client.js', platform: 'browser', target: 'es2020' }),
  esbuild.build({ ...comunes, entryPoints: ['src/server/main.ts'], outfile: 'dist/server.js', platform: 'node', target: 'node22' }),
]).catch(() => process.exit(1));
```

```ts
// src/client/main.ts
RegisterCommand('pos', () => {
  const [x, y, z] = GetEntityCoords(PlayerPedId(), true);
  console.log(`vec3(${x.toFixed(2)}, ${y.toFixed(2)}, ${z.toFixed(2)})`);
}, false);
```

> Empaqueta siempre las dependencias npm en el **cliente** (V8 no tiene `require`). En el **servidor** puedes empaquetar o dejar `node_modules` dentro del recurso.

## 10.6 Servidor: async, base de datos y npm

```js
// server.js con oxmysql (export)
const oxmysql = exports.oxmysql;

onNet('banco:saldo', async () => {
  const src = global.source;
  const license = GetPlayerIdentifierByType(src, 'license');
  const row = await oxmysql.single_async('SELECT saldo FROM cuentas WHERE license = ?', [license]);
  emitNet('banco:saldo:respuesta', src, row?.saldo ?? 0);
});
```

> Las funciones *async* de exports de oxmysql en JS siguen el patrón `query_async`, `single_async`, `scalar_async`, `insert_async`, `update_async`, `prepare_async`.

---

# 11. C# (.NET / Mono)

## 11.1 Proyecto

FiveM ejecuta C# con **Mono** (compatible con .NET Standard 2.0 / .NET Framework 4.x). Se compila a **DLL** y se carga desde el manifest.

`MiRecurso.Client.csproj`:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net452</TargetFramework>
    <DebugType>portable</DebugType>
    <AssemblyName>MiRecurso.Client.net</AssemblyName>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="CitizenFX.Core.Client" Version="1.0.*" ExcludeAssets="runtime" />
  </ItemGroup>
</Project>
```

`MiRecurso.Server.csproj`: igual pero `TargetFramework` `netstandard2.0` y `CitizenFX.Core.Server`.

> El nombre del DLL **debe terminar en `.net.dll`** para que FiveM lo reconozca como ensamblado de script.

Manifest:

```lua
fx_version 'cerulean'
game 'gta5'

client_script 'Client/bin/Release/net452/MiRecurso.Client.net.dll'
server_script 'Server/bin/Release/netstandard2.0/MiRecurso.Server.net.dll'
```

## 11.2 Script básico

```csharp
using System;
using System.Threading.Tasks;
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

namespace MiRecurso.Client
{
    public class Main : BaseScript
    {
        public Main()
        {
            EventHandlers["onClientResourceStart"] += new Action<string>(OnStart);
            EventHandlers["miRecurso:red"] += new Action<string>(msg => Debug.WriteLine(msg));

            RegisterCommand("pos", new Action<int, System.Collections.Generic.List<object>, string>((src, args, raw) =>
            {
                var p = Game.PlayerPed.Position;
                Debug.WriteLine($"vec3({p.X:F2}, {p.Y:F2}, {p.Z:F2})");
            }), false);

            Exports.Add("Sumar", new Func<int, int, int>((a, b) => a + b));
        }

        private void OnStart(string res)
        {
            if (res != GetCurrentResourceName()) return;
            TriggerServerEvent("miRecurso:alServidor", "hola");
        }

        [Tick]
        private async Task OnTick()
        {
            // cada frame
            await Delay(1000); // espera 1s antes del siguiente tick de este método
        }
    }
}
```

Servidor:

```csharp
using System;
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

namespace MiRecurso.Server
{
    public class Main : BaseScript
    {
        public Main()
        {
            EventHandlers["miRecurso:alServidor"] += new Action<Player, string>(OnMensaje);
            EventHandlers["playerConnecting"] += new Action<Player, string, dynamic, dynamic>(OnConnecting);
        }

        private void OnMensaje([FromSource] Player jugador, string msg)
        {
            Debug.WriteLine($"{jugador.Name}: {msg}");
            jugador.TriggerEvent("miRecurso:red", "respuesta");
            TriggerClientEvent("miRecurso:red", "a todos");
        }

        private async void OnConnecting([FromSource] Player p, string name, dynamic setKickReason, dynamic deferrals)
        {
            deferrals.defer();
            await Delay(0);
            deferrals.update("Comprobando...");
            deferrals.done();
        }
    }
}
```

## 11.3 Conceptos

| Concepto | Equivalente Lua |
|---|---|
| `BaseScript` | Cada clase que hereda es un "script" que FiveM instancia. |
| `[Tick]` / `Tick += OnTick` | `CreateThread` con bucle. |
| `await Delay(ms)` | `Wait(ms)`. |
| `EventHandlers["x"] += ...` | `AddEventHandler` / `RegisterNetEvent`. |
| `[FromSource] Player` | `source`. |
| `TriggerServerEvent` / `TriggerClientEvent` / `player.TriggerEvent` | Igual. |
| `Exports["recurso"].Funcion(...)` | `exports.recurso:Funcion(...)`. |
| `Players` (servidor) | `GetPlayers()`. |
| `Function.Call(Hash.X, ...)` | `Citizen.InvokeNative`. |
| `API.*` (static import) | Natives directamente. |

Wrappers útiles en cliente: `Game.PlayerPed`, `World.CreateVehicle(model, pos, heading)`, `Vehicle`, `Ped`, `Entity`, `Model`, `Screen.ShowNotification`.

> **Mono v2 (`mono_rt2`)**: era un runtime C# experimental que se activaba con una cadena de "prerelease" con fecha de caducidad. La última fecha aceptada fue el **30 de junio de 2026**; en los artefactos actuales los recursos con `mono_rt2` muestran *"mono_rt2 is no longer supported"* y **no se cargan**. En FiveM Legacy usa el runtime clásico (Mono v1) con `CitizenFX.Core.Client` / `CitizenFX.Core.Server`.

## 11.4 Plantillas oficiales

```bash
dotnet new -i CitizenFX.Templates
dotnet new cfx-resource -n MiRecurso
```

Genera la estructura con proyectos de cliente, servidor y `fxmanifest.lua`.

---

# 12. Natives: guía práctica

## 12.1 Cómo leer la referencia de natives

En https://docs.fivem.net/natives/ cada native muestra:

```
-- GET_ENTITY_COORDS
-- 0x3FEF770D40960D5A
Vector3 GET_ENTITY_COORDS(Entity entity, BOOL alive);
```

- **Nombre** en MAYÚSCULAS_CON_GUIONES → en Lua/JS/C# se usa en **PascalCase** (`GetEntityCoords`).
- **Hash** → para `Citizen.InvokeNative(0x3FEF770D40960D5A, entity, true)`.
- **Parámetros** con tipos (`Entity`, `Ped`, `Vehicle`, `Hash`, `BOOL`, `float`, `int`, `char*`, `Vector3`, punteros `int*`/`float*`/`Vector3*`).
- **Punteros (`*`)**: en Lua/JS se convierten en **valores de retorno adicionales**. Ej.: `GetGroundZFor_3dCoord(x, y, z, includeWater)` devuelve `found, groundZ`.
- **Categorías**: `PLAYER`, `PED`, `VEHICLE`, `ENTITY`, `OBJECT`, `STREAMING`, `HUD`, `GRAPHICS`, `CAM`, `TASK`, `WEAPON`, `NETWORK`, `AUDIO`, `MISC`, `INTERIOR`, `ZONE`, `PATHFIND`, `FIRE`, `WATER`, `CFX` (propios de FiveM)…
- La etiqueta **Server** indica natives disponibles en el servidor; los marcados como **RPC** se ejecutan en un cliente propietario (p. ej. `SetPedArmour` en el servidor envía la orden al dueño de la entidad).

## 12.2 Tipos y convenciones

| Tipo | En Lua | Notas |
|---|---|---|
| `Hash` | número | `` `adder` `` o `GetHashKey('adder')`. |
| `BOOL` | `true`/`false` | Algunos natives devuelven `1/0`. |
| `float` | número con decimales | Pasa `1.0`, no `1`, cuando el native espera float (en Lua 5.4 un entero puede interpretarse distinto). |
| `Vector3` | `vector3(x,y,z)` / `vec3` | Devuelto por natives como `GetEntityCoords`. |
| `char*` | string | |
| `Any*` / estructuras | complejo | Requiere `DataView`/buffers en Lua; raro. |

> **Importante:** pasa siempre **floats como floats** (`0.0`, `1.0`). Pasar `0` donde se espera `0.0` puede causar comportamientos extraños.

## 12.3 Cargar modelos, animaciones y otros assets (*streaming*)

Antes de crear entidades o reproducir animaciones, hay que **cargar** el asset:

```lua
local function cargarModelo(modelo)
    local hash = type(modelo) == 'string' and joaat(modelo) or modelo
    if not IsModelInCdimage(hash) or not IsModelValid(hash) then return false end
    RequestModel(hash)
    local timeout = GetGameTimer() + 5000
    while not HasModelLoaded(hash) do
        if GetGameTimer() > timeout then return false end
        Wait(0)
    end
    return hash
end

local function cargarAnimDict(dict)
    RequestAnimDict(dict)
    while not HasAnimDictLoaded(dict) do Wait(0) end
end

-- Liberar cuando ya no se necesiten
SetModelAsNoLongerNeeded(hash)
RemoveAnimDict(dict)
```

Otros pares *request/has/remove*: `RequestNamedPtfxAsset`/`HasNamedPtfxAssetLoaded`, `RequestStreamedTextureDict`/`HasStreamedTextureDictLoaded`, `RequestScaleformMovie`/`HasScaleformMovieLoaded`, `RequestWeaponAsset`, `RequestAnimSet` (*walk styles*), `RequestIpl`.

> Con **ox_lib**: `lib.requestModel('adder')`, `lib.requestAnimDict('...')`, `lib.requestNamedPtfxAsset`, etc.

## 12.4 Jugador y ped

```lua
local ped = PlayerPedId()                  -- tu ped (cliente)
local playerId = PlayerId()                -- tu índice local de jugador
local serverId = GetPlayerServerId(playerId)
local otroPlayer = GetPlayerFromServerId(5) -- -1 si no está en tu rango
local otroPed = GetPlayerPed(otroPlayer)

local coords = GetEntityCoords(ped)
local heading = GetEntityHeading(ped)
SetEntityCoords(ped, 0.0, 0.0, 72.0, false, false, false, false)
SetEntityHeading(ped, 90.0)
SetEntityHealth(ped, 200)                  -- 100 = muerto, 200 = máximo por defecto
SetPedArmour(ped, 100)
SetEntityInvincible(ped, true)
FreezeEntityPosition(ped, true)
SetEntityVisible(ped, false, false)
SetPlayerInvincible(PlayerId(), true)
IsPedInAnyVehicle(ped, false)
IsEntityDead(ped)
NetworkResurrectLocalPlayer(x, y, z, heading, true, false)
ClearPedTasksImmediately(ped)
SetPedCanRagdoll(ped, false)
SetPlayerWantedLevel(PlayerId(), 0, false); SetPlayerWantedLevelNow(PlayerId(), false)
SetMaxWantedLevel(0)                        -- desactiva policía
```

### Teletransporte seguro (con colisión cargada)

```lua
local function teleport(x, y, z, h)
    local ped = PlayerPedId()
    DoScreenFadeOut(500); while not IsScreenFadedOut() do Wait(0) end
    RequestCollisionAtCoord(x, y, z)
    SetEntityCoordsNoOffset(ped, x, y, z, false, false, false)
    if h then SetEntityHeading(ped, h) end
    local t = GetGameTimer() + 5000
    while not HasCollisionLoadedAroundEntity(ped) and GetGameTimer() < t do Wait(0) end
    DoScreenFadeIn(500)
end
```

### Cambiar modelo del jugador

```lua
local hash = cargarModelo('mp_m_freemode_01')
SetPlayerModel(PlayerId(), hash)
SetPedDefaultComponentVariation(PlayerPedId())
SetModelAsNoLongerNeeded(hash)
```

### Ropa (componentes y props)

```lua
-- SetPedComponentVariation(ped, componentId, drawable, texture, palette)
SetPedComponentVariation(ped, 11, 15, 0, 0)  -- torso/chaqueta
SetPedPropIndex(ped, 0, 8, 0, true)           -- sombrero
ClearPedProp(ped, 0)
```

| ID componente | Parte | ID prop | Parte |
|---|---|---|---|
| 0 | Cara/cabeza | 0 | Sombrero/casco |
| 1 | Máscara | 1 | Gafas |
| 2 | Pelo | 2 | Orejas |
| 3 | Torso (brazos) | 6 | Reloj |
| 4 | Piernas | 7 | Pulsera |
| 5 | Mochila/paracaídas | | |
| 6 | Zapatos | | |
| 7 | Accesorios (cuello) | | |
| 8 | Camiseta interior | | |
| 9 | Chaleco antibalas | | |
| 10 | Calcomanías | | |
| 11 | Chaqueta/torso superior | | |

## 12.5 Vehículos

### Crear un vehículo (cliente)

```lua
local function spawnVehiculo(modelo, coords, heading)
    local hash = cargarModelo(modelo)
    if not hash then return print('Modelo inválido: ' .. modelo) end
    local veh = CreateVehicle(hash, coords.x, coords.y, coords.z, heading, true, false) -- isNetwork=true
    SetVehicleOnGroundProperly(veh)
    SetVehicleNumberPlateText(veh, 'FIVEM')
    SetPedIntoVehicle(PlayerPedId(), veh, -1) -- -1 = conductor
    SetVehicleEngineOn(veh, true, true, false)
    SetModelAsNoLongerNeeded(hash)
    return veh
end
```

### Crear un vehículo en el servidor (recomendado con OneSync)

```lua
-- server.lua
local function spawnVehiculoServidor(src, modelo, coords, heading)
    local hash = joaat(modelo)
    -- 'automobile', 'bike', 'boat', 'heli', 'plane', 'submarine', 'trailer', 'train'
    local veh = CreateVehicleServerSetter(hash, 'automobile', coords.x, coords.y, coords.z, heading)
    local timeout = 0
    while not DoesEntityExist(veh) and timeout < 100 do Wait(10); timeout += 1 end
    if not DoesEntityExist(veh) then return end
    SetVehicleNumberPlateText(veh, 'SRV001')
    local netId = NetworkGetNetworkIdFromEntity(veh)
    Entity(veh).state:set('propietario', GetPlayerIdentifierByType(src, 'license'), true)
    TaskWarpPedIntoVehicle(GetPlayerPed(src), veh, -1)
    return veh, netId
end
```

> `CreateVehicleServerSetter` crea el vehículo directamente con su tipo, sin depender de un cliente. `CreateVehicle` en servidor también existe (como RPC) pero es menos fiable para algunos tipos.

### Funciones frecuentes de vehículos

```lua
local veh = GetVehiclePedIsIn(ped, false)      -- false = el actual; true = el último
GetPedInVehicleSeat(veh, -1)                    -- conductor
GetEntityModel(veh); GetDisplayNameFromVehicleModel(GetEntityModel(veh))
GetVehicleNumberPlateText(veh)
SetVehicleFixed(veh); SetVehicleDeformationFixed(veh)
SetVehicleDirtLevel(veh, 0.0)
SetVehicleFuelLevel(veh, 100.0)
GetVehicleEngineHealth(veh); GetVehicleBodyHealth(veh)
SetVehicleDoorsLocked(veh, 2)                   -- 1 abierto, 2 cerrado
SetVehicleColours(veh, primario, secundario)
SetVehicleCustomPrimaryColour(veh, 255, 0, 0)
SetVehicleModKit(veh, 0); SetVehicleMod(veh, 11, 3, false)  -- motor nivel 4
ToggleVehicleMod(veh, 18, true)                -- turbo
SetVehicleTyresCanBurst(veh, false)
SetVehicleEngineOn(veh, false, true, true)
DeleteEntity(veh)                               -- necesita control de la entidad
```

Índices de `SetVehicleMod` más usados: `0` alerón, `1` parachoques delantero, `2` trasero, `3` faldones, `4` escape, `11` motor, `12` frenos, `13` transmisión, `14` claxon, `15` suspensión, `16` blindaje, `18` turbo (toggle), `22` faros xenón (toggle), `23` ruedas delanteras, `48` *livery*.

## 12.6 Entidades: control y red

```lua
NetworkGetNetworkIdFromEntity(ent)   -- entidad → netId
NetworkGetEntityFromNetworkId(netId) -- netId → entidad (cliente y servidor)
NetToVeh(netId); NetToPed(netId); NetToObj(netId)  -- cliente
NetworkDoesNetworkIdExist(netId)
NetworkHasControlOfEntity(ent)
NetworkRequestControlOfEntity(ent)
NetworkGetEntityOwner(ent)           -- servidor: id del cliente dueño
SetEntityAsMissionEntity(ent, true, true)  -- evita que el juego la borre
SetEntityAsNoLongerNeeded(ent)
DoesEntityExist(ent)
```

**Pedir control antes de modificar/borrar una entidad ajena (cliente):**

```lua
local function pedirControl(ent, timeoutMs)
    local t = GetGameTimer() + (timeoutMs or 2000)
    NetworkRequestControlOfEntity(ent)
    while not NetworkHasControlOfEntity(ent) and GetGameTimer() < t do
        Wait(0)
        NetworkRequestControlOfEntity(ent)
    end
    return NetworkHasControlOfEntity(ent)
end
```

> Con `sv_filterRequestControl` activo, pedir control de vehículos ocupados por otros jugadores se bloquea. Para borrar entidades de forma fiable hazlo **desde el servidor** con `DeleteEntity`.

**Enumerar entidades:**

```lua
-- Cliente
for _, veh in ipairs(GetGamePool('CVehicle')) do end   -- 'CPed', 'CObject', 'CVehicle', 'CPickup'
-- Servidor
for _, veh in ipairs(GetAllVehicles()) do end           -- GetAllPeds(), GetAllObjects()
```

## 12.7 Objetos (props)

```lua
local hash = cargarModelo('prop_barrier_work05')
local obj = CreateObject(hash, x, y, z, true, true, false)   -- isNetwork, netMissionEntity, doorFlag
PlaceObjectOnGroundProperly(obj)
FreezeEntityPosition(obj, true)
AttachEntityToEntity(obj, ped, GetPedBoneIndex(ped, 57005), 0.1, 0.0, 0.0, 0.0, 0.0, 0.0, true, true, false, true, 1, true)
DetachEntity(obj, true, true)
DeleteObject(obj)
```

Huesos (*bones*) frecuentes del ped: `57005` mano derecha (SKEL_R_Hand), `18905` mano izquierda (SKEL_L_Hand), `31086` cabeza (SKEL_Head), `24818` columna superior (SKEL_Spine3), `0` raíz.

## 12.8 Animaciones y escenarios

```lua
cargarAnimDict('mp_common')
TaskPlayAnim(ped, 'mp_common', 'givetake1_a', 8.0, -8.0, 2000, 49, 0.0, false, false, false)
-- flags: 1 loop, 2 detener en último frame, 16 solo parte superior, 32 permitir moverse, 48/49 = tren superior + movimiento
StopAnimTask(ped, 'mp_common', 'givetake1_a', 1.0)
ClearPedTasks(ped)

TaskStartScenarioInPlace(ped, 'WORLD_HUMAN_SMOKING', 0, true)
TaskStartScenarioInPlace(ped, 'PROP_HUMAN_SEAT_BENCH', 0, true)
```

Lista de animaciones: busca "GTA V animations list" (por ejemplo, el visor de *alexguirre* o la lista de `dpemotes`/`rpemotes`).

## 12.9 Blips (iconos del mapa)

```lua
local blip = AddBlipForCoord(25.7, -1347.3, 29.49)
SetBlipSprite(blip, 52)          -- icono (52 = tienda)
SetBlipColour(blip, 2)           -- color
SetBlipScale(blip, 0.8)
SetBlipAsShortRange(blip, true)  -- solo visible cerca en el minimapa
SetBlipDisplay(blip, 4)
BeginTextCommandSetBlipName('STRING')
AddTextComponentSubstringPlayerName('Tienda 24/7')
EndTextCommandSetBlipName(blip)

-- Otros
AddBlipForEntity(ent); AddBlipForRadius(x, y, z, radio)
SetBlipRoute(blip, true); SetBlipRouteColour(blip, 5)
SetNewWaypoint(x, y)
RemoveBlip(blip)
```

Referencia de sprites y colores: https://docs.fivem.net/docs/game-references/blips/

## 12.10 Marcadores, texto 3D y notificaciones

```lua
-- Marcador (cada frame)
DrawMarker(1, x, y, z - 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.5, 1.5, 0.5, 0, 150, 255, 100, false, false, 2, false, nil, nil, false)

-- Texto 3D
local function texto3D(x, y, z, texto)
    local enPantalla, sx, sy = World3dToScreen2d(x, y, z)
    if not enPantalla then return end
    SetTextScale(0.35, 0.35)
    SetTextFont(4)
    SetTextProportional(true)
    SetTextColour(255, 255, 255, 215)
    SetTextCentre(true)
    SetTextOutline()
    BeginTextCommandDisplayText('STRING')
    AddTextComponentSubstringPlayerName(texto)
    EndTextCommandDisplayText(sx, sy)
end

-- Notificación nativa encima del minimapa
local function notificar(msg)
    BeginTextCommandThefeedPost('STRING')
    AddTextComponentSubstringPlayerName(msg)
    EndTextCommandThefeedPostTicker(false, true)
end

-- Ayuda arriba a la izquierda
local function ayuda(msg)
    BeginTextCommandDisplayHelp('STRING')
    AddTextComponentSubstringPlayerName(msg)
    EndTextCommandDisplayHelp(0, false, true, -1)
end
```

Tipos de marcador: `0` cilindro con flecha, `1` cilindro, `2` flecha, `20`-`22` chevrons, `25`-`27` círculos en el suelo, `36` coche… Lista: https://docs.fivem.net/docs/game-references/markers/

Códigos dentro de texto: `~r~` rojo, `~g~` verde, `~b~` azul, `~y~` amarillo, `~w~` blanco, `~o~` naranja, `~p~` morado, `~h~` negrita, `~n~` salto de línea, `~INPUT_CONTEXT~` icono de tecla.

## 12.11 Cámaras

```lua
local cam = CreateCamWithParams('DEFAULT_SCRIPTED_CAMERA', x, y, z, rotX, rotY, rotZ, 60.0, false, 0)
SetCamActive(cam, true)
RenderScriptCams(true, true, 1000, true, true)   -- activar con transición de 1s
PointCamAtEntity(cam, ped, 0.0, 0.0, 0.0, true)
-- ...
RenderScriptCams(false, true, 1000, true, true)
DestroyCam(cam, false)
```

## 12.12 Mundo: hora, clima, IPLs, población

```lua
NetworkOverrideClockTime(12, 0, 0)       -- hora
SetWeatherTypeNowPersist('CLEAR')        -- EXTRASUNNY, CLEAR, CLOUDS, OVERCAST, RAIN, THUNDER, CLEARING, FOGGY, SMOG, SNOW, BLIZZARD, SNOWLIGHT, XMAS, HALLOWEEN, NEUTRAL
SetWeatherTypeOverTime('RAIN', 15.0)
SetBlackout(true)
RequestIpl('shr_int'); RemoveIpl('shr_int')
SetPedDensityMultiplierThisFrame(0.5)    -- cada frame
SetVehicleDensityMultiplierThisFrame(0.5)
SetRandomVehicleDensityMultiplierThisFrame(0.5)
SetParkedVehicleDensityMultiplierThisFrame(0.5)
SetScenarioPedDensityMultiplierThisFrame(0.5, 0.5)
SetGarbageTrucks(false); SetRandomBoats(false); SetCreateRandomCops(false)
```

En servidor (OneSync), sincroniza clima/hora para todos con un recurso de clima (p. ej. `vSync`, `cd_easytime`, `qb-weathersync`, `Renewed-Weathersync`) o con `GlobalState` + handler en cliente.

## 12.13 Armas

```lua
GiveWeaponToPed(ped, `WEAPON_PISTOL`, 100, false, true)
RemoveWeaponFromPed(ped, `WEAPON_PISTOL`)
RemoveAllPedWeapons(ped, true)
SetPedAmmo(ped, `WEAPON_PISTOL`, 250)
GiveWeaponComponentToPed(ped, `WEAPON_PISTOL`, `COMPONENT_AT_PI_SUPP_02`)
GetSelectedPedWeapon(ped)
SetCurrentPedWeapon(ped, `WEAPON_UNARMED`, true)
SetPedInfiniteAmmoClip(ped, false)
```

> Dar armas desde el servidor: `GiveWeaponToPed(GetPlayerPed(src), hash, ammo, false, true)` (RPC). Con un inventario (ox_inventory), las armas son ítems y las gestiona el inventario.

## 12.14 Audio y sonidos

```lua
PlaySoundFrontend(-1, 'SELECT', 'HUD_FRONTEND_DEFAULT_SOUNDSET', true)
PlaySoundFromEntity(-1, 'Beep_Red', ped, 'DLC_HEIST_HACKING_SNAKE_SOUNDS', true, 0)
```

Para sonidos personalizados: NUI (`<audio>` en HTML) o bancos de audio nativos (`data_file 'AUDIO_WAVEPACK'`, ver 15).

## 12.15 Scaleforms

```lua
local sf = RequestScaleformMovie('MP_BIG_MESSAGE_FREEMODE')
while not HasScaleformMovieLoaded(sf) do Wait(0) end
BeginScaleformMovieMethod(sf, 'SHOW_SHARD_WASTED_MP_MESSAGE')
ScaleformMovieMethodAddParamTextureNameString('~r~HAS MUERTO')
ScaleformMovieMethodAddParamTextureNameString('Intenta tener más cuidado')
EndScaleformMovieMethod()
CreateThread(function()
    local fin = GetGameTimer() + 4000
    while GetGameTimer() < fin do
        DrawScaleformMovieFullscreen(sf, 255, 255, 255, 255, 0)
        Wait(0)
    end
    SetScaleformMovieAsNoLongerNeeded(sf)
end)
```

## 12.16 Raycast (qué estoy mirando)

```lua
local function raycastCamara(distancia)
    local camRot = GetGameplayCamRot(2)
    local camPos = GetGameplayCamCoord()
    local rx, rz = math.rad(camRot.x), math.rad(camRot.z)
    local dir = vector3(-math.sin(rz) * math.abs(math.cos(rx)), math.cos(rz) * math.abs(math.cos(rx)), math.sin(rx))
    local destino = camPos + dir * distancia
    local ray = StartShapeTestLosProbe(camPos.x, camPos.y, camPos.z, destino.x, destino.y, destino.z, -1, PlayerPedId(), 4)
    local estado, hit, coords, normal, entidad
    repeat
        estado, hit, coords, normal, entidad = GetShapeTestResult(ray)
        Wait(0)
    until estado ~= 1
    return hit == 1, coords, entidad
end
```

> `lib.raycast.cam()` de ox_lib hace esto por ti.

## 12.17 Natives propios del servidor (lista útil)

| Categoría | Natives |
|---|---|
| Jugadores | `GetPlayers`, `GetPlayerName`, `GetPlayerIdentifiers`, `GetPlayerIdentifierByType`, `GetPlayerPed`, `GetPlayerPing`, `DropPlayer`, `GetPlayerTokens` |
| Entidades | `GetAllVehicles`, `GetAllPeds`, `GetAllObjects`, `GetEntityCoords`, `GetEntityHeading`, `SetEntityCoords`, `SetEntityHeading`, `DeleteEntity`, `DoesEntityExist`, `GetEntityModel`, `GetEntityType`, `NetworkGetEntityOwner`, `NetworkGetNetworkIdFromEntity`, `NetworkGetEntityFromNetworkId`, `GetEntityPopulationType`, `SetEntityDistanceCullingRadius`, `SetEntityOrphanMode` |
| Creación | `CreateVehicleServerSetter`, `CreateVehicle`, `CreatePed`, `CreatePedInsideVehicle`, `CreateObject`, `CreateObjectNoOffset` |
| Vehículos | `GetVehiclePedIsIn`, `GetPedInVehicleSeat`, `GetVehicleNumberPlateText`, `SetVehicleNumberPlateText`, `SetVehicleDoorsLocked`, `GetVehicleType`, `GetVehicleEngineHealth`, `GetVehicleBodyHealth` |
| Peds | `GetPedArmour`, `GetEntityHealth`, `GetSelectedPedWeapon`, `GiveWeaponToPed`, `RemoveAllPedWeapons`, `SetPedArmour`, `TaskWarpPedIntoVehicle`, `ClearPedTasks` |
| Buckets | `SetPlayerRoutingBucket`, `GetPlayerRoutingBucket`, `SetEntityRoutingBucket`, `GetEntityRoutingBucket`, `SetRoutingBucketPopulationEnabled`, `SetRoutingBucketEntityLockdownMode` |
| State bags | `Entity(e).state`, `Player(src).state`, `GlobalState`, `AddStateBagChangeHandler`, `RemoveStateBagChangeHandler`, `GetStateBagValue`, `GetEntityFromStateBagName`, `GetPlayerFromStateBagName` |
| Recursos | `GetCurrentResourceName`, `GetResourceState`, `GetResourcePath`, `LoadResourceFile`, `SaveResourceFile`, `StartResource`, `StopResource`, `GetResourceMetadata` |
| Sistema | `ExecuteCommand`, `GetConvar`, `SetConvar`, `PerformHttpRequest`, `SetHttpHandler`, `GetGameTimer`, `IsPlayerAceAllowed`, `ScheduleResourceTick` |

---

# 13. Red, OneSync, State Bags y Routing Buckets

## 13.1 Cómo funciona la sincronización con OneSync

- El servidor mantiene un **árbol de sincronización** (*sync tree*) de cada entidad en red: posición, salud, modelo, estado de puertas, etc.
- Cada entidad tiene un **owner** (un cliente) que la simula y envía su estado al servidor; el servidor lo reenvía a los clientes que la tienen **en su ámbito** (*scope*), normalmente por distancia (~424 m por defecto para la mayoría de entidades).
- Si el owner se aleja o se desconecta, la entidad **migra** a otro cliente cercano (`onesync_forceMigration`).
- Si no hay ningún jugador cerca de una entidad creada por script en el servidor, ésta **sigue existiendo en el servidor** (se queda "huérfana" hasta que alguien vuelva a acercarse), lo que permite, por ejemplo, vehículos persistentes.
- Entidades **fuera de tu ámbito no existen en tu cliente**: `NetToVeh(netId)` devuelve 0 y `GetPlayerFromServerId` devuelve -1. Desde el servidor sí puedes leerlas.

### Qué puedes hacer en el servidor gracias a OneSync

```lua
-- Coordenadas de cualquier jugador, aunque esté lejos de todos
local coords = GetEntityCoords(GetPlayerPed(src))

-- Vehículo en el que va
local veh = GetVehiclePedIsIn(GetPlayerPed(src), false)

-- Todas las entidades del mundo
for _, ped in ipairs(GetAllPeds()) do
    if not IsPedAPlayer(ped) then --[[ NPC ]] end
end
```

### Huérfanos y *culling*

```lua
-- Qué hacer con una entidad de servidor cuando nadie la "posee"
-- 0 = DeleteWhenNotRelevant (por defecto), 1 = DeleteOnOwnerDisconnect, 2 = KeepEntity
SetEntityOrphanMode(veh, 2)

-- Radio de sincronización personalizado para una entidad (en metros)
SetEntityDistanceCullingRadius(veh, 1000.0)
```

## 13.2 Ámbitos (*scopes*)

Eventos del servidor para saber quién "ve" a quién:

```lua
local enRango = {}  -- enRango[jugador] = { [otro] = true }

AddEventHandler('playerEnteredScope', function(data)
    local quien, para = tonumber(data.player), tonumber(data['for'])
    enRango[para] = enRango[para] or {}
    enRango[para][quien] = true
end)

AddEventHandler('playerLeftScope', function(data)
    local quien, para = tonumber(data.player), tonumber(data['for'])
    if enRango[para] then enRango[para][quien] = nil end
end)
```

Útil para enviar eventos **solo a jugadores cercanos** en lugar de a `-1`.

## 13.3 Control de entidades creadas por clientes

### `entityCreating` (bloquear modelos)

```lua
local prohibidos = { [`rhino`] = true, [`hydra`] = true, [`lazer`] = true }

AddEventHandler('entityCreating', function(entity)
    if prohibidos[GetEntityModel(entity)] then
        CancelEvent()
    end
end)
```

### Entity lockdown

| Modo `sv_entityLockdown` | Efecto |
|---|---|
| `inactive` (defecto) | Los clientes pueden crear cualquier entidad. |
| `relaxed` | Se bloquean las entidades **de script** creadas por clientes (las de población/tráfico siguen permitidas). |
| `strict` | Los clientes **no pueden crear ninguna** entidad: todo debe crearse en el servidor. |

Por bucket: `SetRoutingBucketEntityLockdownMode(bucket, 'strict')`.

> `strict` es la protección más fuerte contra *spawners* de cheats, pero obliga a que **todos** tus scripts creen vehículos/objetos desde el servidor. `relaxed` es un buen término medio.

### Población (NPCs)

```lua
-- Servidor: desactivar NPCs en un bucket
SetRoutingBucketPopulationEnabled(5, false)

-- Cliente: impedir que aparezcan ciertos peds
AddEventHandler('populationPedCreating', function(x, y, z, model, setters)
    if model == `s_m_y_cop_01` then CancelEvent() end
    -- setters.setModel(`a_m_y_hipster_01`) / setters.setPosition(x, y, z)
end)
```

## 13.4 State Bags

Los **state bags** son pares **clave-valor sincronizados automáticamente** asociados a una entidad, a un jugador o al servidor (global). Son la forma moderna de compartir estado sin enviar eventos constantemente.

| Tipo | Acceso | Quién escribe (por defecto) |
|---|---|---|
| **Global** | `GlobalState.clave` | Solo el servidor. |
| **Jugador** | `Player(src).state` (servidor) / `LocalPlayer.state` (cliente) | El servidor y el propio jugador. |
| **Entidad** | `Entity(entidad).state` | El servidor y el **owner** de la entidad. |

### Escribir

```lua
-- SERVIDOR (por defecto replicado a los clientes)
GlobalState.horaServidor = '12:00'
Player(src).state.trabajo = 'policia'
Entity(veh).state.combustible = 80.0

-- Controlar la replicación explícitamente
Player(src).state:set('dinero_secreto', 5000, false)  -- solo servidor
Entity(veh).state:set('bloqueado', true, true)         -- replicado
```

```lua
-- CLIENTE (por defecto NO replicado; hay que pedirlo)
LocalPlayer.state:set('animando', true, true)          -- se replica al servidor y otros clientes
```

### Leer

```lua
-- Cualquier lado
print(GlobalState.horaServidor)
print(LocalPlayer.state.trabajo)                     -- cliente
print(Player(src).state.trabajo)                     -- servidor
print(Entity(NetToVeh(netId)).state.combustible)     -- cliente
print(Entity(veh).state.combustible)                 -- servidor
```

### Escuchar cambios: `AddStateBagChangeHandler`

```lua
-- AddStateBagChangeHandler(clave|nil, nombreBag|nil, function(bagName, key, value, reserved, replicated) end)

-- Cualquier cambio de 'trabajo' en cualquier jugador
AddStateBagChangeHandler('trabajo', nil, function(bagName, key, value, _, replicated)
    local ply = GetPlayerFromStateBagName(bagName)   -- en cliente devuelve el player index; 0 si no
    if ply == 0 then return end
    print(('Jugador %s ahora es %s'):format(GetPlayerServerId(ply), value))
end)

-- Solo cambios de MI jugador
AddStateBagChangeHandler('trabajo', ('player:%s'):format(GetPlayerServerId(PlayerId())), function(_, _, value)
    ActualizarHUD(value)
end)

-- Cambios en entidades
AddStateBagChangeHandler('bloqueado', nil, function(bagName, _, value)
    local ent = GetEntityFromStateBagName(bagName)
    if ent == 0 then return end
    SetVehicleDoorsLocked(ent, value and 2 or 1)
end)

-- Global
AddStateBagChangeHandler('horaServidor', 'global', function(_, _, value) end)
```

Nombres de bag: `global`, `player:<serverId>`, `entity:<netId>`, `localEntity:<handle>`.

`RemoveStateBagChangeHandler(cookie)` elimina un handler (el `Add...` devuelve el *cookie*).

Otros natives útiles:

| Native | Uso |
|---|---|
| `GetStateBagValue(bagName, key)` | Leer un valor a partir del nombre de la bag. |
| `GetStateBagKeys(bagName)` | Lista de claves de una bag. |
| `StateBagHasKey(bagName, key)` | ¿Existe la clave? |
| `EnsureEntityStateBag(entity)` | Garantiza que la entidad tenga bag (útil en entidades recién creadas). |
| `GetEntityFromStateBagName(bagName)` / `GetPlayerFromStateBagName(bagName)` | Convertir el nombre de la bag en entidad/jugador. |

### Limitaciones y buenas prácticas

- Son **superficiales**: `Entity(x).state.datos.sub = 1` **no** se replica. Reasigna el objeto entero o usa claves planas: `Entity(x).state['datos:sub'] = 1`.
- Leer valores anidados deserializa todo el estado cada vez: guarda en una variable local si lo usas mucho.
- No metas tablas enormes (inventarios completos) en un state bag que cambia constantemente.
- **Seguridad**: por defecto un cliente puede escribir en **su propio** player state y en entidades que posee. Valida en el servidor o activa **`setr sv_stateBagStrictMode true`** para que solo el servidor pueda escribir valores replicados.
- Un handler del **servidor** que reacciona a un state bag escrito por un cliente debe tratar el valor como **no fiable**.

### Ejemplo completo: sistema de "esposado"

```lua
-- server
RegisterNetEvent('policia:esposar', function(objetivo)
    local src = source
    if Player(src).state.trabajo ~= 'policia' then return end
    local esposado = Player(objetivo).state.esposado
    Player(objetivo).state:set('esposado', not esposado, true)
end)
```

```lua
-- client
AddStateBagChangeHandler('esposado', ('player:%s'):format(GetPlayerServerId(PlayerId())), function(_, _, value)
    local ped = PlayerPedId()
    if value then
        cargarAnimDict('mp_arresting')
        TaskPlayAnim(ped, 'mp_arresting', 'idle', 8.0, -8, -1, 49, 0, false, false, false)
        SetEnableHandcuffs(ped, true)
    else
        ClearPedTasks(ped)
        SetEnableHandcuffs(ped, false)
    end
end)
```

## 13.5 Routing Buckets (dimensiones)

Un **routing bucket** es una "dimensión" separada: los jugadores y entidades de un bucket **no ven ni sincronizan** con los de otros buckets. El bucket por defecto es el `0`.

Usos: interiores instanciados (casas, apartamentos), carreras privadas, zonas de creación de personaje, eventos, sesiones de *deathmatch*.

```lua
-- server
SetPlayerRoutingBucket(src, 100)
SetEntityRoutingBucket(veh, 100)
print(GetPlayerRoutingBucket(src))

SetRoutingBucketPopulationEnabled(100, false)          -- sin NPCs
SetRoutingBucketEntityLockdownMode(100, 'strict')      -- sin entidades de cliente

-- Volver al mundo normal
SetPlayerRoutingBucket(src, 0)

AddEventHandler('onPlayerBucketChange', function(player, bucket, oldBucket) end)
```

### Ejemplo: casa instanciada

```lua
local casas = {}  -- casas[idCasa] = bucket

RegisterNetEvent('casas:entrar', function(idCasa)
    local src = source
    local bucket = casas[idCasa] or (1000 + idCasa)
    casas[idCasa] = bucket
    SetPlayerRoutingBucket(src, bucket)
    TriggerClientEvent('casas:tpInterior', src, idCasa)
end)

RegisterNetEvent('casas:salir', function()
    SetPlayerRoutingBucket(source, 0)
end)
```

> La **voz** (pma-voice) también respeta los buckets si está configurada para ello. Los **state bags** globales son visibles desde todos los buckets.

## 13.6 Eventos latentes y tamaño de los datos

- Los eventos normales se envían "de golpe". Si son grandes (más de unos pocos KB) pueden saturar la red o fragmentarse.
- Usa **`TriggerLatentClientEvent(nombre, target, bps, ...)`** para enviar datos grandes (p. ej. una lista de 5.000 registros) a una velocidad controlada.
- Si necesitas saber cuándo ha llegado todo, haz que el cliente responda con un evento de confirmación.
- `sv_enableNetEventReassembly` permite enviar eventos grandes fragmentados (activado por defecto).

## 13.7 Comprobar OneSync desde scripts

```lua
local onesync = GetConvar('onesync', 'off')
if onesync == 'off' then
    print('^1Este recurso requiere OneSync^0')
end
```

O en el manifest: `dependency '/onesync'`.

---

# 14. NUI (interfaces web dentro del juego)

**NUI** (*New UI*) permite mostrar interfaces hechas con **HTML/CSS/JavaScript** encima del juego, renderizadas con un navegador Chromium (CEF) embebido. Se usa para HUDs, menús, inventarios, teléfonos, tablets policiales, pantallas de carga…

## 14.1 Estructura mínima

```
mi_ui/
├── fxmanifest.lua
├── client.lua
└── html/
    ├── index.html
    ├── style.css
    └── app.js
```

```lua
-- fxmanifest.lua
fx_version 'cerulean'
game 'gta5'

ui_page 'html/index.html'
files { 'html/index.html', 'html/style.css', 'html/app.js' }
client_script 'client.lua'
```

```html
<!-- html/index.html -->
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div id="menu" class="oculto">
    <h1 id="titulo">Menú</h1>
    <button id="cerrar">Cerrar</button>
  </div>
  <script src="app.js"></script>
</body>
</html>
```

```css
/* html/style.css: el fondo SIEMPRE transparente */
html, body { margin: 0; background: transparent; font-family: sans-serif; overflow: hidden; }
.oculto { display: none; }
#menu { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: rgba(20,20,20,.9); color: #fff; padding: 24px; border-radius: 12px; }
```

## 14.2 Lua → NUI: `SendNUIMessage`

```lua
-- client.lua
local abierto = false

local function abrirMenu()
    abierto = true
    SetNuiFocus(true, true)                 -- (foco de teclado, cursor)
    SendNUIMessage({ action = 'abrir', titulo = 'Tienda 24/7' })
end

RegisterCommand('menu', abrirMenu, false)
```

```js
// html/app.js
window.addEventListener('message', (event) => {
  const data = event.data;
  if (data.action === 'abrir') {
    document.getElementById('titulo').textContent = data.titulo;
    document.getElementById('menu').classList.remove('oculto');
  }
});
```

## 14.3 NUI → Lua: `RegisterNUICallback` + `fetch`

```js
// html/app.js
document.getElementById('cerrar').addEventListener('click', async () => {
  document.getElementById('menu').classList.add('oculto');
  const resp = await fetch(`https://${GetParentResourceName()}/cerrar`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=UTF-8' },
    body: JSON.stringify({ motivo: 'boton' }),
  });
  const json = await resp.json();
  console.log(json);
});

// Cerrar con ESC
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') document.getElementById('cerrar').click();
});
```

```lua
-- client.lua
RegisterNUICallback('cerrar', function(data, cb)
    abierto = false
    SetNuiFocus(false, false)
    print('Cerrado por: ' .. tostring(data.motivo))
    cb({ ok = true })     -- ¡SIEMPRE responde al callback, o el fetch se queda colgado!
end)
```

- `RegisterNuiCallback` es un alias de `RegisterNUICallback`. Para recibir el cuerpo sin procesar existe `RegisterRawNuiCallback`.
- `GetParentResourceName()` es una función que FiveM inyecta en la página NUI y devuelve el nombre del recurso.
- La URL es `https://<nombre_recurso>/<callback>`.
- Los datos viajan como JSON.

## 14.4 Foco, ratón y teclado

| Native | Descripción |
|---|---|
| `SetNuiFocus(teclado, cursor)` | Da el foco a la NUI. **Recuerda quitarlo al cerrar.** |
| `SetNuiFocusKeepInput(true)` | Mantiene los controles del juego mientras la NUI tiene foco (para HUDs interactivos; combínalo con `DisableControlAction` para lo que no quieras). |
| `IsNuiFocused()` | ¿Tiene foco la NUI? |
| `SetCursorLocation(x, y)` | Mueve el cursor (0.0-1.0). |

> Si un jugador se queda "atascado" sin poder moverse, casi siempre es una NUI que no ha llamado a `SetNuiFocus(false, false)`. Añade siempre un `onResourceStop` que lo quite.

## 14.5 Rutas de archivos dentro de NUI

| Ruta | Uso |
|---|---|
| `https://cfx-nui-mi_recurso/html/img.png` | **Forma recomendada** para archivos de un recurso (deben estar en `files`). |
| `nui://mi_recurso/html/img.png` | Forma antigua. Sigue funcionando para cargar archivos, pero **ya no es un "contexto seguro"** (APIs del navegador como portapapeles, cripto, etc. pueden fallar). |
| Rutas relativas (`img/logo.png`) | Relativas a la `ui_page`. |

Imágenes de ítems de inventario, por ejemplo: `https://cfx-nui-ox_inventory/web/images/agua.png`.

## 14.6 Depurar la NUI

- En el cliente, F8 → **`nui_devtools`** abre las DevTools de Chromium para inspeccionar tus páginas (elige el *frame* de tu recurso).
- `console.log` dentro de la NUI aparece en las DevTools, **no** en F8.
- Para desarrollar con *hot-reload*, puedes apuntar `ui_page` a `http://localhost:5173` mientras desarrollas con Vite (y volver a la build final para producción).

## 14.7 NUI con React/Vue/Svelte + Vite

1. Crea el proyecto en `mi_recurso/web`: `npm create vite@latest web -- --template react-ts`.
2. En `vite.config.ts` pon `base: './'` para que las rutas sean relativas y `build.outDir: 'dist'`.
3. `npm run build` → genera `web/dist`.
4. Manifest:

```lua
ui_page 'web/dist/index.html'
files { 'web/dist/index.html', 'web/dist/assets/*' }
```

Helper de `fetch` para NUI (TypeScript):

```ts
export async function fetchNui<T = unknown>(evento: string, data?: unknown): Promise<T> {
  const recurso = (window as any).GetParentResourceName ? (window as any).GetParentResourceName() : 'nui-dev';
  const resp = await fetch(`https://${recurso}/${evento}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=UTF-8' },
    body: JSON.stringify(data ?? {}),
  });
  return resp.json();
}
```

Hook para escuchar mensajes:

```ts
import { useEffect } from 'react';

export function useNuiEvent<T>(action: string, handler: (data: T) => void) {
  useEffect(() => {
    const listener = (e: MessageEvent) => {
      if (e.data?.action === action) handler(e.data.data);
    };
    window.addEventListener('message', listener);
    return () => window.removeEventListener('message', listener);
  }, [action, handler]);
}
```

> Hay *boilerplates* populares que ya traen esto montado (p. ej. `project-error/fivem-react-boilerplate-lua` —React 19 + Vite— o `overextended/fivem-typescript-boilerplate`). Búscalos en GitHub.

## 14.8 Pantalla de carga (*loadscreen*)

```lua
-- fxmanifest.lua de un recurso de loadscreen
fx_version 'cerulean'
game 'gta5'

loadscreen 'index.html'
loadscreen_manual_shutdown 'yes'   -- opcional
files { 'index.html', 'style.css', 'script.js', 'music.mp3', 'bg.webm' }
client_script 'client.lua'
```

```lua
-- client.lua (solo si loadscreen_manual_shutdown = 'yes')
AddEventHandler('playerSpawned', function()
    ShutdownLoadingScreenNui()
end)
```

Eventos que recibe la pantalla de carga (en `window.addEventListener('message')`):

```js
const handlers = {
  startInitFunctionOrder(data) { /* data.type, data.order, data.count */ },
  initFunctionInvoking(data)   { /* data.name, data.idx */ },
  startDataFileEntries(data)   { /* data.count */ },
  performMapLoadFunction(data) { /* data.idx */ },
  onLogLine(data)              { console.log(data.message); },
  loadProgress(data)           { document.querySelector('#barra').style.width = `${data.loadFraction * 100}%`; },
};
window.addEventListener('message', (e) => (handlers[e.data.eventName] || (() => {}))(e.data));
```

Dentro de la pantalla de carga también tienes `window.nuiHandoverData` con los datos enviados con `deferrals.handover`.

- El native `SetManualShutdownLoadingScreenNui` está **obsoleto**: usa `loadscreen_manual_shutdown 'yes'` en el manifest.
- `setr sv_showBusySpinnerOnLoadingScreen false` oculta el icono giratorio de carga.

## 14.9 DUI (páginas web como texturas en el mundo)

Las **DUI** permiten renderizar una página web en una **textura** (pantallas de TV, carteles, cines):

```lua
local dui = CreateDui('https://ejemplo.com', 1280, 720)
local handle = GetDuiHandle(dui)
local txd = CreateRuntimeTxd('mi_tv_txd')
CreateRuntimeTextureFromDuiHandle(txd, 'mi_tv_tex', handle)
AddReplaceTexture('prop_tv_flat_01', 'script_rt_tvscreen', 'mi_tv_txd', 'mi_tv_tex')
-- SetDuiUrl(dui, 'https://otra.com'); SendDuiMessage(dui, json.encode({...})); DestroyDui(dui)
```

## 14.10 Rendimiento NUI

- Una NUI con animaciones CSS pesadas, vídeos o `setInterval` rápidos **consume FPS** aunque esté oculta. Pausa lo que no se ve.
- Envía mensajes solo cuando cambian los datos, no cada frame (para un HUD de velocidad, 10-20 veces/seg es suficiente).
- Usa imágenes optimizadas (WebP) y evita fuentes enormes.
- No cargues frameworks gigantes para una UI simple.

---

# 15. Streaming de assets (vehículos, mapas, ropa, armas…)

## 15.1 Carpeta `stream`

Todo archivo dentro de una carpeta llamada **`stream`** (o subcarpetas suyas) de un recurso se **transmite** a los clientes y el juego lo carga como si fuera parte del juego. No hace falta declararlo en el manifest.

| Extensión | Contenido |
|---|---|
| `.ytd` | Diccionario de texturas. |
| `.ydr` | Modelo (drawable) simple. |
| `.ydd` | Diccionario de drawables (ropa, cabezas). |
| `.yft` | Modelo fragmentable (vehículos, objetos rompibles). |
| `.ybn` | Colisiones (*bounds*). |
| `.ymap` | Colocación de entidades en el mapa. |
| `.ytyp` | Definición de arquetipos (props, MLOs). |
| `.ymf` | Manifest de mapa. |
| `.ycd` | Animaciones (clip dictionary). |
| `.ypt` | Efectos de partículas. |
| `.ynv` / `.ynd` | Navmesh / nodos de ruta. |
| `.awc` | Audio. |
| `.gfx` | Scaleform. |
| `.ymt` | Metadatos binarios (ropa, escenarios). |

Los archivos **`.meta`** (XML) **no** van en `stream`: se declaran con `data_file` (ver 15.6).

## 15.2 Reemplazo vs *add-on*

- **Reemplazo** (*replace*): el archivo tiene el **mismo nombre** que uno del juego (`adder.yft`) y lo sustituye.
- **Add-on**: añade un modelo **nuevo** con nombre propio (`micoche.yft`) más sus metas. Es lo recomendado: no rompe nada del juego base.

## 15.3 Vehículo add-on completo

```
mi_coche/
├── fxmanifest.lua
├── stream/
│   ├── micoche.yft
│   ├── micoche_hi.yft
│   ├── micoche.ytd
│   └── micoche+hi.ytd      (opcional)
└── data/
    ├── vehicles.meta
    ├── carvariations.meta
    ├── carcols.meta
    ├── handling.meta
    └── vehiclelayouts.meta (si lo trae)
```

```lua
fx_version 'cerulean'
game 'gta5'

files {
    'data/vehicles.meta',
    'data/carvariations.meta',
    'data/carcols.meta',
    'data/handling.meta',
    'data/vehiclelayouts.meta',
}

data_file 'HANDLING_FILE'          'data/handling.meta'
data_file 'VEHICLE_METADATA_FILE'  'data/vehicles.meta'
data_file 'CARCOLS_FILE'           'data/carcols.meta'
data_file 'VEHICLE_VARIATION_FILE' 'data/carvariations.meta'
data_file 'VEHICLE_LAYOUTS_FILE'   'data/vehiclelayouts.meta'
```

Nombre del vehículo en el juego (para que no salga "NULL"):

```lua
-- client.lua
CreateThread(function()
    AddTextEntry('MICOCHE', 'Mi Coche Deportivo')   -- gameName de vehicles.meta
end)
```

### Pack de varios vehículos

Puedes juntar muchos coches en un solo recurso con metas combinados o usando globs:

```lua
files { 'data/**/*.meta' }
data_file 'HANDLING_FILE'          'data/**/handling.meta'
data_file 'VEHICLE_METADATA_FILE'  'data/**/vehicles.meta'
data_file 'CARCOLS_FILE'           'data/**/carcols.meta'
data_file 'VEHICLE_VARIATION_FILE' 'data/**/carvariations.meta'
```

> Cuidado: demasiados vehículos/ropa de alta calidad aumentan la **memoria de texturas** y los tiempos de carga. Optimiza (ver 15.9).

## 15.4 Mapas: ymaps y MLOs

- Un **ymap** coloca objetos en el mundo. Basta con meterlo en `stream/`.
- Un **MLO** (*Milo*, interior) suele traer `.ymap` + `.ytyp` + `.ybn` + `.ydr` + `.ytd`.
- Si el MLO trae `.ytyp`, en muchos casos hay que declararlo:

```lua
fx_version 'cerulean'
game 'gta5'
this_is_a_map 'yes'

data_file 'DLC_ITYP_REQUEST' 'stream/mi_interior.ytyp'
```

- Para quitar edificios del mapa base hay que usar ymaps con *entity removal* (o recursos tipo "map fixes").
- Interiores del juego (IPL) se cargan con `RequestIpl` o con recursos como **bob74_ipl**.

## 15.5 Ropa add-on (EUP y similares)

- La ropa se basa en archivos `.ydd`/`.ytd` con nombres especiales (`mp_m_freemode_01_mp_m_mi_pack^jbib_000_u.ydd`) y un `.ymt` de metadatos de *ped* (`mp_m_freemode_01_mp_m_mi_pack.ymt`).
- Herramientas como **Durty Cloth Tool** o **Grzyb's/Clothing Tool** generan el recurso de *streaming* listo para FiveM.
- Las prendas add-on se suman **después** de las del juego, así que sus índices de *drawable* dependen del **game build**: cambiar de build puede desplazar los IDs.

## 15.6 `data_file`: tipos más usados

| Tipo | Archivo típico |
|---|---|
| `HANDLING_FILE` | `handling.meta` |
| `VEHICLE_METADATA_FILE` | `vehicles.meta` |
| `CARCOLS_FILE` | `carcols.meta` (modkits, sirenas, luces) |
| `VEHICLE_VARIATION_FILE` | `carvariations.meta` |
| `VEHICLE_LAYOUTS_FILE` | `vehiclelayouts.meta` |
| `CONTENT_UNLOCKING_META_FILE` | `contentunlocks.meta` |
| `PED_METADATA_FILE` | `peds.meta` |
| `SHOP_PED_APPAREL_META_FILE` | metas de ropa de tienda (`shop_*.meta`) |
| `PED_PERSONALITY_FILE` | `pedpersonality.meta` |
| `WEAPONINFO_FILE` | `weapons.meta` |
| `WEAPON_ANIMATIONS_FILE` | `weaponanimations.meta` |
| `WEAPON_METADATA_FILE` | `weaponarchetypes.meta` |
| `WEAPONCOMPONENTSINFO_FILE` | `weaponcomponents.meta` |
| `LOADOUTS_FILE` | `loadouts.meta` |
| `DLC_ITYP_REQUEST` | `*.ytyp` |
| `AUDIO_GAMEDATA` | `*_game.dat` |
| `AUDIO_SOUNDDATA` | `*_sounds.dat` |
| `AUDIO_SYNTHDATA` | `*_amp.dat` |
| `AUDIO_WAVEPACK` | carpeta con `.awc` |
| `TIMECYCLEMOD_FILE` | `timecycle_mods_*.xml` |
| `SCALEFORM_DLC_FILE` | `*.gfx` |
| `TEXTFILE_METAFILE` | textos (gxt2) |
| `TRAINCONFIGS_FILE` | `trains.xml` |
| `TRAINTRACK_FILE` | `traintracks.xml` |
| `INTERIOR_PROXY_ORDER_FILE` | `interiorproxies.meta` |

Lista completa y oficial: https://docs.fivem.net/docs/game-references/data-files/

## 15.7 Armas add-on

```lua
fx_version 'cerulean'
game 'gta5'

files {
    'meta/weaponarchetypes.meta',
    'meta/weaponanimations.meta',
    'meta/pedpersonality.meta',
    'meta/weapons.meta',
    'meta/weaponcomponents.meta',
}

data_file 'WEAPON_METADATA_FILE'      'meta/weaponarchetypes.meta'
data_file 'WEAPON_ANIMATIONS_FILE'    'meta/weaponanimations.meta'
data_file 'PED_PERSONALITY_FILE'      'meta/pedpersonality.meta'
data_file 'WEAPONCOMPONENTSINFO_FILE' 'meta/weaponcomponents.meta'
data_file 'WEAPONINFO_FILE'           'meta/weapons.meta'
```

## 15.8 Texturas en tiempo de ejecución (runtime TXD)

```lua
local txd = CreateRuntimeTxd('mis_logos')
CreateRuntimeTextureFromImage(txd, 'logo', 'img/logo.png')  -- archivo en 'files'
-- Usar: DrawSprite('mis_logos', 'logo', 0.5, 0.5, 0.1, 0.1, 0.0, 255, 255, 255, 255)
```

## 15.9 Optimización de assets

- **Tamaño de texturas**: evita `.ytd` de más de **16 MB** (FiveM avisa de *oversized assets* en consola) — reduce a 2K/1K, usa compresión DXT, genera *mipmaps*.
- **Polígonos**: vehículos de 500k+ polígonos destrozan el rendimiento; usa LODs (`_hi.yft` + versión baja).
- **Herramientas**: **CodeWalker** (mapas, ymaps), **OpenIV** (explorar y editar RPF), **Sollumz** (Blender: modelos, MLOs), **ZModeler3** (vehículos), **Texture Toolkit**/**Paint.NET + DDS**.
- Usa `strdbg` (F8) para ver qué se está transmitiendo y cuánto ocupa.
- Revisa los avisos de *"physical memory"* y *"virtual memory"* del recurso en `resmon`.

## 15.10 Assets de pago y escrow

- Los assets comprados en tiendas Tebex suelen venir **cifrados con Asset Escrow** y solo funcionan en los servidores cuya clave pertenece a la cuenta que los compró.
- Si un recurso con escrow da *"You lack the required entitlement"*, la clave del servidor no pertenece a la cuenta que tiene el recurso, la suscripción caducó o el recurso se ha renombrado.
- El escrow admite Lua y modelos (YFT, YDD, YDR); **la NUI no se cifra**.
- Más en la [sección 23](#23-monetización-legalidad-y-asset-escrow).

---

# 16. Base de datos (MariaDB + oxmysql)

## 16.1 Instalar MariaDB

**Versiones recomendadas (octubre 2026):**

| Serie | Tipo | Fin de soporte |
|---|---|---|
| **11.8** | LTS | febrero 2030 |
| **11.4** | LTS | mayo 2029 |
| 12.3 | LTS (nueva) | junio 2029 |
| 10.11 | LTS | febrero 2028 |
| 10.6 | LTS | **julio 2026 (ya sin soporte)** |

> Usa **MariaDB 11.4 LTS u 11.8 LTS**. Se desaconseja MySQL 8 (palabras reservadas como `group`, sin valores por defecto en columnas JSON/LONGTEXT) y **XAMPP** (versiones viejas, inseguro, no pensado para producción).

**Windows:** instalador MSI de https://mariadb.org/download → marca "Use UTF8 as default server's character set" → pon contraseña de root. Cliente gráfico: **HeidiSQL** (viene incluido; última versión 12.21).

**Linux (Debian/Ubuntu):**

```bash
# Repositorio oficial de MariaDB (elige la serie en https://mariadb.org/download/?t=repo-config)
sudo apt install mariadb-server
sudo mariadb-secure-installation
sudo mariadb
```

```sql
CREATE DATABASE fivem CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'fivem'@'localhost' IDENTIFIED BY 'una_contraseña_larga_y_segura';
GRANT ALL PRIVILEGES ON fivem.* TO 'fivem'@'localhost';
FLUSH PRIVILEGES;
```

> **Nunca** uses el usuario `root` para FiveM y **nunca** abras el puerto 3306 a Internet.

## 16.2 oxmysql: instalación y conexión

**oxmysql** (Overextended, v2.14.x) es el conector estándar de FiveM. Sustituye (y es compatible con) los antiguos `mysql-async` y `ghmattimysql`.

```cfg
# server.cfg (usa SET, nunca setr)
set mysql_connection_string "mysql://fivem:contraseña@127.0.0.1:3306/fivem?charset=utf8mb4"
# o formato clave=valor:
# set mysql_connection_string "user=fivem;password=contraseña;host=127.0.0.1;port=3306;database=fivem"

set mysql_slow_query_warning 150   # ms: avisa de consultas lentas
# set mysql_debug true             # registra todas las consultas (solo desarrollo)
# set mysql_ui true                # interfaz de consultas con el comando /mysql

ensure oxmysql                      # SIEMPRE antes que los recursos que lo usan
```

> Si la contraseña tiene caracteres como `; , / ? : @ & = + $ #`, usa el **otro** formato de cadena o cámbiala; romperán el formato URI.

En el manifest de tu recurso:

```lua
server_scripts {
    '@oxmysql/lib/MySQL.lua',
    'server/*.lua',
}
dependency 'oxmysql'
```

## 16.3 API de oxmysql (Lua)

Cada función tiene forma **`.await`** (síncrona dentro de un thread/handler) y forma con **callback**.

```lua
-- SELECT varias filas → array de filas
local filas = MySQL.query.await('SELECT * FROM vehiculos WHERE propietario = ?', { license })

-- Una sola fila → tabla o nil
local fila = MySQL.single.await('SELECT nombre, dinero FROM usuarios WHERE license = ? LIMIT 1', { license })

-- Un solo valor → valor o nil
local dinero = MySQL.scalar.await('SELECT dinero FROM usuarios WHERE license = ?', { license })

-- INSERT → id insertado
local id = MySQL.insert.await('INSERT INTO usuarios (license, nombre) VALUES (?, ?)', { license, nombre })

-- UPDATE/DELETE → filas afectadas
local n = MySQL.update.await('UPDATE usuarios SET dinero = dinero + ? WHERE license = ?', { 500, license })

-- Sentencia preparada en el servidor (solo placeholders ?), más rápida para consultas repetidas
local r = MySQL.prepare.await('SELECT dinero FROM usuarios WHERE license = ?', { license })

-- Transacción (todo o nada)
local ok = MySQL.transaction.await({
    { query = 'UPDATE usuarios SET dinero = dinero - ? WHERE license = ?', values = { 100, origen } },
    { query = 'UPDATE usuarios SET dinero = dinero + ? WHERE license = ?', values = { 100, destino } },
})

-- Forma con callback
MySQL.query('SELECT * FROM usuarios', {}, function(resultado)
    print(#resultado)
end)

-- Ejecutar SQL al arrancar (crear tablas)
MySQL.ready(function()
    MySQL.query([[
        CREATE TABLE IF NOT EXISTS mi_tabla (
            id INT AUTO_INCREMENT PRIMARY KEY,
            license VARCHAR(60) NOT NULL,
            datos LONGTEXT NULL,
            creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_license (license)
        )
    ]])
end)
```

- Placeholders: usa **`?`** con un array de valores. Los placeholders con nombre (`@nombre`) están **obsoletos**.
- Para "insertar o actualizar" usa `INSERT ... ON DUPLICATE KEY UPDATE`.
- En JavaScript: `exports.oxmysql.query_async(sql, params)`, `single_async`, `scalar_async`, `insert_async`, `update_async`, `prepare_async`, `transaction_async`, o el paquete npm `@overextended/oxmysql`.

## 16.4 Buenas prácticas SQL en FiveM

- **Nunca concatenes** datos del jugador en el SQL (`'... WHERE nombre = "' .. nombre .. '"'`): **inyección SQL**. Usa siempre `?`.
- Crea **índices** en las columnas por las que filtras (`license`, `citizenid`, `identifier`, `plate`).
- No hagas consultas **por frame** ni dentro de bucles grandes; **cachea** en memoria y guarda periódicamente o al desconectar.
- Guarda datos de jugador en `playerDropped` **y** cada X minutos (por si el servidor se cae).
- Usa `utf8mb4` para soportar emojis y caracteres especiales.
- Para datos complejos (metadatos, inventarios), `LONGTEXT` con JSON o columnas `JSON` en MariaDB.
- Haz **backups** automáticos (`mariadb-dump` diario + rotación). txAdmin no hace copias de la BD por ti.

```bash
# Backup diario (cron) 
mariadb-dump -u fivem -p'contraseña' --single-transaction --routines fivem | gzip > /backups/fivem_$(date +%F).sql.gz
find /backups -name "fivem_*.sql.gz" -mtime +14 -delete
```

## 16.5 Patrón: caché de jugador + guardado

```lua
local Jugadores = {}  -- [src] = { license, dinero, ... }

local function cargar(src)
    local license = GetPlayerIdentifierByType(src, 'license')
    local fila = MySQL.single.await('SELECT * FROM usuarios WHERE license = ?', { license })
    if not fila then
        MySQL.insert.await('INSERT INTO usuarios (license, nombre, dinero) VALUES (?, ?, ?)', { license, GetPlayerName(src), 500 })
        fila = { license = license, dinero = 500 }
    end
    Jugadores[src] = fila
end

local function guardar(src)
    local p = Jugadores[src]
    if not p then return end
    MySQL.update.await('UPDATE usuarios SET dinero = ? WHERE license = ?', { p.dinero, p.license })
end

RegisterNetEvent('mi_core:jugadorListo', function() cargar(source) end)

AddEventHandler('playerDropped', function()
    local src = source
    guardar(src)
    Jugadores[src] = nil
end)

CreateThread(function()
    while true do
        Wait(5 * 60 * 1000)               -- cada 5 minutos
        for src in pairs(Jugadores) do guardar(src) end
    end
end)

AddEventHandler('onResourceStop', function(res)
    if res ~= GetCurrentResourceName() then return end
    for src in pairs(Jugadores) do guardar(src) end
end)
```

---

# 17. Frameworks

Un **framework** proporciona la base de un servidor RP: personajes, dinero, trabajos, inventario, permisos, callbacks… Estado a **octubre de 2026**:

| Framework | Repositorio | Versión | Estado | Documentación |
|---|---|---|---|---|
| **ESX Legacy** | `esx-framework/esx_core` | **1.16.4** (oct 2026) | Muy activo | https://docs.esx-framework.org |
| **QBCore** | `qbcore-framework/qb-core` | 1.3.0 (sin releases formales) | Actividad baja | https://docs.qbcore.org |
| **Qbox** | `Qbox-project/qbx_core` | **1.24.0** (ago 2026) | Activo | https://docs.qbox.re |
| **ox_core** | `overextended/ox_core` | 1.5.14 | Activo (TypeScript) | https://overextended.dev |
| **ND Framework** | `ND-Framework/ND_Core` | — | Activo, nicho | Repositorio |
| **Standalone** | — | — | Tú lo haces todo | — |

### ¿Cuál elegir?

- **Qbox**: moderno, rendimiento cuidado, basado en **ox_lib + ox_inventory**, compatible con la mayoría de scripts de QBCore gracias a su *bridge* (`provide 'qb-core'`). Muy buena opción para un servidor nuevo en 2026.
- **ESX Legacy**: el más veterano y con más scripts disponibles; desde la 1.16 trae su propia librería (`esx_lib`) e inventario NUI (`esx_inventory`), y detecta `ox_inventory` automáticamente.
- **QBCore**: enorme catálogo de scripts, pero el núcleo se mueve poco; muchos servidores nuevos lo sustituyen por Qbox.
- **ox_core**: para desarrolladores con experiencia que quieren algo minimalista y tipado (TypeScript), requiere MariaDB 11.4+.
- **Standalone**: para servidores no-RP (carreras, drift, PvP) o proyectos muy personalizados.

## 17.1 Ecosistema Overextended (ox_*)

> **Aviso importante de 2025-2026:** Overextended **archivó** sus repositorios en **abril de 2025**; la comunidad los mantuvo como **CommunityOx** durante 2025. En **abril de 2026** el desarrollo **volvió a `overextended/*`** y la organización CommunityOx quedó **archivada** (sin mantenimiento). **Usa siempre `github.com/overextended`, la documentación https://overextended.dev y los paquetes npm `@overextended/*`.** Si tienes recursos descargados de CommunityOx, actualízalos desde Overextended.

| Recurso | Versión (oct 2026) | Qué hace |
|---|---|---|
| **ox_lib** | 3.40.x | Librería de utilidades: UI (notificaciones, menús, diálogos, barras de progreso), callbacks, zonas, puntos, keybinds, caché, locales… |
| **oxmysql** | 2.14.x | Conector MySQL/MariaDB. |
| **ox_inventory** | 2.48.x | Inventario por slots con peso, metadatos, tiendas, alijos, armas. Bridges: `ox`, `esx`, `qbx`, `nd`. |
| **ox_target** | 1.18.x | Sistema de "ojo"/*target* para interactuar con entidades y zonas (sustituye a qtarget/qb-target). |
| **ox_doorlock** | 1.23.x | Puertas con cerradura sincronizadas. |
| **ox_fuel** | 1.5.x | Combustible. |
| **ox_core** | 1.5.x | Framework. |

### ox_lib: instalación

```lua
-- fxmanifest.lua de TU recurso
shared_script '@ox_lib/init.lua'
-- opcional: cargar módulos concretos de forma global
ox_libs { 'locale', 'math', 'table' }
dependency 'ox_lib'
```

```cfg
# server.cfg
ensure ox_lib
setr ox:locale es
setr ox:primaryColor blue
setr ox:primaryShade 8
```

Variables globales que obtienes: `lib`, `cache`, `require` (módulos por ruta `@recurso.ruta`).

### ox_lib: lo más usado

```lua
-- ===== CALLBACKS =====
-- server
lib.callback.register('tienda:comprar', function(source, item, cantidad)
    -- validar y devolver
    return true, 'Compra realizada'
end)
-- client
local ok, msg = lib.callback.await('tienda:comprar', false, 'agua', 2)

-- ===== NOTIFICACIONES =====
lib.notify({ title = 'Banco', description = 'Has recibido $500', type = 'success' }) -- inform | error | success | warning
-- desde el servidor:
TriggerClientEvent('ox_lib:notify', src, { title = 'Banco', description = 'Pago recibido', type = 'success' })

-- ===== MENÚ CONTEXTUAL =====
lib.registerContext({
    id = 'menu_tienda',
    title = 'Tienda 24/7',
    options = {
        { title = 'Agua', description = '$5', icon = 'bottle-water', onSelect = function() Comprar('agua') end },
        { title = 'Pan', description = '$3', icon = 'bread-slice', serverEvent = 'tienda:comprarPan', args = { cantidad = 1 } },
        { title = 'Submenú', menu = 'otro_menu', arrow = true },
    },
})
lib.showContext('menu_tienda')

-- ===== DIÁLOGO DE ENTRADA =====
local input = lib.inputDialog('Transferencia', {
    { type = 'number', label = 'ID del jugador', required = true },
    { type = 'number', label = 'Cantidad', min = 1, max = 100000, required = true },
    { type = 'input', label = 'Concepto' },
})
if input then
    local id, cantidad, concepto = input[1], input[2], input[3]
end

-- ===== DIÁLOGO DE CONFIRMACIÓN =====
local alerta = lib.alertDialog({ header = '¿Seguro?', content = 'Vas a vender tu casa', centered = true, cancel = true })
if alerta == 'confirm' then end

-- ===== BARRA DE PROGRESO =====
if lib.progressBar({
    duration = 5000,
    label = 'Reparando vehículo...',
    useWhileDead = false,
    canCancel = true,
    disable = { move = true, car = true, combat = true },
    anim = { dict = 'mini@repair', clip = 'fixing_a_ped' },
}) then
    print('Terminado')
else
    print('Cancelado')
end

-- ===== TEXTO UI =====
lib.showTextUI('[E] Abrir tienda', { position = 'left-center', icon = 'store' })
lib.hideTextUI()

-- ===== PUNTOS (alternativa eficiente a bucles de distancia) =====
local punto = lib.points.new({ coords = vec3(25.7, -1347.3, 29.49), distance = 5 })
function punto:onEnter() lib.showTextUI('[E] Tienda') end
function punto:onExit() lib.hideTextUI() end
function punto:nearby()
    if self.currentDistance < 1.5 and IsControlJustReleased(0, 38) then AbrirTienda() end
end

-- ===== ZONAS =====
local zona = lib.zones.box({
    coords = vec3(441.0, -982.0, 30.7),
    size = vec3(10, 10, 4),
    rotation = 0,
    debug = false,
    onEnter = function() print('Has entrado a comisaría') end,
    onExit = function() print('Has salido') end,
    inside = function() --[[ cada frame dentro ]] end,
})
-- lib.zones.sphere({ coords, radius, ... }), lib.zones.poly({ points = { vec3(...), ... }, thickness = 4 })

-- ===== KEYBINDS =====
lib.addKeybind({
    name = 'abrir_tablet',
    description = 'Abrir tablet',
    defaultKey = 'F9',
    onPressed = function() AbrirTablet() end,
})

-- ===== CACHÉ (valores que se actualizan solos) =====
print(cache.ped, cache.playerId, cache.serverId, cache.vehicle, cache.seat, cache.weapon)
lib.onCache('vehicle', function(veh, anterior)
    if veh then print('Has subido a un vehículo') end
end)

-- ===== LOCALES =====
-- locales/es.json: { "bienvenida": "Hola %s" }    (añade 'locales/*.json' a files)
lib.locale()
print(locale('bienvenida', GetPlayerName(PlayerId())))

-- ===== OTROS =====
lib.requestModel(`adder`)
lib.requestAnimDict('mp_common')
lib.playAnim(cache.ped, 'mp_common', 'givetake1_a')
local veh, coordsVeh = lib.getClosestVehicle(GetEntityCoords(cache.ped), 5.0, false)
lib.addCommand('dv', { help = 'Borrar vehículo', restricted = 'group.admin' }, function(source, args) end) -- servidor
lib.versionCheck('tuusuario/mi_recurso') -- servidor, usa releases de GitHub
```

### ox_inventory: API básica (servidor)

```lua
local inv = exports.ox_inventory

inv:AddItem(src, 'agua', 2)                          -- (inventario, item, cantidad, metadatos?, slot?)
inv:AddItem(src, 'documento', 1, { nombre = 'Juan', dni = '12345678X' })
inv:RemoveItem(src, 'agua', 1)
local n = inv:GetItemCount(src, 'agua')
local puede = inv:CanCarryItem(src, 'agua', 5)
local item = inv:GetItem(src, 'agua', nil, false)
inv:RegisterStash('taquilla_policia', 'Taquilla LSPD', 50, 100000, false, { police = 0 })
local todos = inv:Items()                            -- definiciones de ítems
```

```cfg
setr inventory:framework "qbx"     # ox | esx | qbx | nd
```

Los ítems se definen en `ox_inventory/data/items.lua`; las imágenes en `ox_inventory/web/images/<item>.png`.

### ox_target: ejemplos

```lua
exports.ox_target:addBoxZone({
    coords = vec3(441.0, -982.0, 30.7),
    size = vec3(1, 1, 1),
    rotation = 0,
    options = {
        { name = 'fichar', label = 'Fichar entrada', icon = 'fa-solid fa-clock', groups = { police = 0 },
          onSelect = function() TriggerServerEvent('policia:fichar') end },
    },
})

exports.ox_target:addGlobalVehicle({
    { name = 'revisar_maletero', label = 'Abrir maletero', icon = 'fa-solid fa-car-rear', bones = { 'boot' },
      distance = 2.0, onSelect = function(data) AbrirMaletero(data.entity) end },
})

exports.ox_target:addModel({ `prop_atm_01`, `prop_atm_02` }, {
    { name = 'atm', label = 'Usar cajero', icon = 'fa-solid fa-money-bill', onSelect = AbrirCajero },
})
```

## 17.2 ESX Legacy (1.16.x)

**Estructura (`[core]`):** `es_extended`, **`esx_lib`** (nuevo, librería propia con callbacks, puntos, zonas, caché, keybinds), **`esx_inventory`** (nuevo inventario NUI por slots, 1.16.0), `esx_context`, `esx_identity`, `esx_multicharacter`, `esx_notify`, `esx_progressbar`, `esx_textui`, `esx_menu_default/dialog/list`, `esx_skin`, `skinchanger`, `esx_loadingscreen`, `esx_whitelist` (nuevo), `cron`. El SQL está en `[SQL]/`.

> ESX **no depende** de ox_lib: usa `esx_lib` (global `xLib`). Si tienes `ox_inventory` instalado, ESX lo detecta y lo usa automáticamente (`Config.CustomInventory = "ox"`).

**Obtener el objeto ESX:**

```lua
-- Opción A (recomendada): en fxmanifest.lua
shared_script '@es_extended/imports.lua'
-- → crea la global ESX y mantiene ESX.PlayerData actualizado en el cliente

-- Opción B
local ESX = exports['es_extended']:getSharedObject()

-- Obsoleto (no lo uses): TriggerEvent('esx:getSharedObject', function(obj) ESX = obj end)
```

**Servidor:**

```lua
local xPlayer = ESX.GetPlayerFromId(source)
local xPlayer2 = ESX.GetPlayerFromIdentifier('char1:abcdef...')
local policias = ESX.GetExtendedPlayers('job', 'police')

-- Dinero
xPlayer.getMoney(); xPlayer.addMoney(500, 'Sueldo'); xPlayer.removeMoney(100, 'Compra')
xPlayer.getAccount('bank').money
xPlayer.addAccountMoney('bank', 1000, 'Transferencia')
xPlayer.removeAccountMoney('black_money', 50, 'Blanqueo')

-- Inventario
xPlayer.addInventoryItem('bread', 2)
xPlayer.removeInventoryItem('bread', 1)
xPlayer.getInventoryItem('bread').count
xPlayer.canCarryItem('bread', 5)
xPlayer.hasItem('bread')

-- Trabajo y grupo
xPlayer.getJob().name; xPlayer.getJob().grade
xPlayer.setJob('police', 2)
xPlayer.getGroup(); xPlayer.setGroup('admin'); xPlayer.isAdmin()

-- Otros
xPlayer.getIdentifier(); xPlayer.getName(); xPlayer.getCoords(true)
xPlayer.showNotification('Hola', 'success', 3000)
xPlayer.setMeta('hambre', 80); xPlayer.getMeta('hambre')
xPlayer.kick('Motivo')

-- Ítems usables
ESX.RegisterUsableItem('bread', function(source)
    local xPlayer = ESX.GetPlayerFromId(source)
    xPlayer.removeInventoryItem('bread', 1)
    TriggerClientEvent('mi_hambre:comer', source, 20)
end)

-- Callbacks (firma clásica, ahora sobre xLib.callback)
ESX.RegisterServerCallback('mi_recurso:getDinero', function(source, cb)
    cb(ESX.GetPlayerFromId(source).getMoney())
end)
```

**Cliente:**

```lua
ESX.TriggerServerCallback('mi_recurso:getDinero', function(dinero) print(dinero) end)
local dinero = ESX.AwaitServerCallback('mi_recurso:getDinero')   -- versión síncrona (1.16)

print(ESX.PlayerData.job.name)
RegisterNetEvent('esx:setJob', function(job) ESX.PlayerData.job = job end)
RegisterNetEvent('esx:playerLoaded', function(xPlayer) ESX.PlayerData = xPlayer end)

ESX.ShowNotification('Mensaje')
ESX.Game.SpawnVehicle('adder', GetEntityCoords(PlayerPedId()), 0.0, function(veh) end)
```

Convars: `setr esx:locale "es"`, `set esx:identifier "license"`.

## 17.3 QBCore

```lua
local QBCore = exports['qb-core']:GetCoreObject()
```

**Servidor:**

```lua
local Player = QBCore.Functions.GetPlayer(source)
local Player2 = QBCore.Functions.GetPlayerByCitizenId('ABC12345')

local pd = Player.PlayerData
print(pd.citizenid, pd.charinfo.firstname, pd.job.name, pd.job.grade.level, pd.money.cash, pd.money.bank)

Player.Functions.AddMoney('cash', 500, 'sueldo')       -- 'cash' | 'bank' | 'crypto'
Player.Functions.RemoveMoney('bank', 100, 'compra')
Player.Functions.SetJob('police', 2)
Player.Functions.SetMetaData('hunger', 100)
Player.Functions.GetMetaData('hunger')

-- Ítems (el inventario es qb-inventory; Player.Functions.AddItem ya NO existe en el core actual)
exports['qb-inventory']:AddItem(source, 'water_bottle', 1, false, false, 'compra en tienda')
exports['qb-inventory']:RemoveItem(source, 'water_bottle', 1, false, 'consumido')

QBCore.Functions.CreateUseableItem('water_bottle', function(source, item) end)
QBCore.Functions.CreateCallback('mi:cb', function(source, cb, arg) cb(true) end)
QBCore.Functions.Notify(source, 'Texto', 'success', 5000)
```

**Cliente:**

```lua
local PlayerData = QBCore.Functions.GetPlayerData()
QBCore.Functions.TriggerCallback('mi:cb', function(res) end, 'arg')
local res = QBCore.Functions.TriggerCallback('mi:cb', 'arg')     -- sin cb → espera el resultado
QBCore.Functions.Notify('Texto', 'error')

RegisterNetEvent('QBCore:Client:OnPlayerLoaded', function() PlayerData = QBCore.Functions.GetPlayerData() end)
RegisterNetEvent('QBCore:Client:OnJobUpdate', function(job) PlayerData.job = job end)
RegisterNetEvent('QBCore:Player:SetPlayerData', function(data) PlayerData = data end)
```

Datos compartidos en `qb-core/shared/`: `items.lua`, `jobs.lua`, `gangs.lua`, `vehicles.lua`, `weapons.lua`, `locations.lua`.

> `QBCore.Functions.AddItem` / `exports['qb-core']:AddItem(nombre, definicion)` **registran la definición** de un ítem en `QBCore.Shared.Items`; **no** dan ítems al jugador.

## 17.4 Qbox (qbx_core)

- Fork moderno de QBCore, **sin objeto core**: API basada en **exports**.
- Dependencias: `ox_lib`, `oxmysql`, `ox_inventory`, OneSync.
- Incluye multipersonaje, multi-trabajo/banda, cola y vehículos persistentes.
- `provide 'qb-core'` + *bridge*: la mayoría de scripts de QBCore funcionan sin cambios.

```lua
-- Servidor
local player = exports.qbx_core:GetPlayer(source)
print(player.PlayerData.citizenid, player.PlayerData.job.name)

exports.qbx_core:AddMoney(source, 'cash', 500, 'sueldo')
exports.qbx_core:RemoveMoney(source, 'bank', 100, 'compra')
exports.qbx_core:SetJob(source, 'police', 2)
exports.qbx_core:HasGroup(source, 'police')
exports.qbx_core:SetMetadata(source, 'hunger', 100)
exports.qbx_core:Notify(source, 'Hola', 'success')

-- Ítems: directamente con ox_inventory
exports.ox_inventory:AddItem(source, 'water', 1)
```

```lua
-- Cliente: módulo de PlayerData
-- fxmanifest: client_script '@qbx_core/modules/playerdata.lua'
print(QBX.PlayerData.job.name)

-- Utilidades: shared_script '@qbx_core/modules/lib.lua'
local matricula = qbx.getVehiclePlate(cache.vehicle)
```

Equivalencias al convertir desde QBCore:

| QBCore | Qbox |
|---|---|
| `QBCore.Functions.GetPlayer(src)` | `exports.qbx_core:GetPlayer(src)` |
| `QBCore.Shared.Items` | `exports.ox_inventory:Items()` |
| `QBCore.Shared.Jobs` | `exports.qbx_core:GetJobs()` |
| `QBCore.Functions.Notify` | `exports.qbx_core:Notify` / `lib.notify` |
| `exports['qb-core']:DrawText` | `lib.showTextUI` |
| `QBCore.Functions.GetPlate` | `qbx.getVehiclePlate` |
| `QBCore.Functions.CreateCallback` | `lib.callback.register` |

## 17.5 Escribir scripts compatibles con varios frameworks (*bridge*)

```lua
-- shared/bridge.lua
Framework = {}

if GetResourceState('qbx_core') == 'started' then
    Framework.name = 'qbx'
elseif GetResourceState('es_extended') == 'started' then
    Framework.name = 'esx'
    ESX = exports.es_extended:getSharedObject()
elseif GetResourceState('qb-core') == 'started' then
    Framework.name = 'qb'
    QBCore = exports['qb-core']:GetCoreObject()
end

if IsDuplicityVersion() then
    function Framework.AddMoney(src, cuenta, cantidad)
        if Framework.name == 'qbx' then
            return exports.qbx_core:AddMoney(src, cuenta == 'money' and 'cash' or cuenta, cantidad)
        elseif Framework.name == 'esx' then
            local x = ESX.GetPlayerFromId(src)
            return x and x.addAccountMoney(cuenta == 'cash' and 'money' or cuenta, cantidad)
        elseif Framework.name == 'qb' then
            local p = QBCore.Functions.GetPlayer(src)
            return p and p.Functions.AddMoney(cuenta == 'money' and 'cash' or cuenta, cantidad)
        end
    end
end
```

---

# 18. Voz: pma-voice y Mumble

FiveM incluye un servidor de voz **Mumble** integrado en FXServer. El recurso estándar para usarlo es **pma-voice** (`AvarianKnight/pma-voice`).

## 18.1 Estado de pma-voice (2026)

- Versión del manifest **7.0.1**; última etiqueta **v7.0.2-rc3**; la rama *master* tiene cambios incompatibles con 7.0.0:
  - `voice_enablePhones` → **`voice_enableCalls`**
  - `voice_defaultPhoneVolume` → **`voice_defaultCallVolume`**
  - State bag `state.phone` → **`state.call`**
- Requiere OneSync. Funciona en FiveM y RedM (`game 'common'`).

## 18.2 Convars (con `setr`)

```cfg
setr voice_useNativeAudio true          # audio 3D nativo con eco/reverb (necesario para submixes)
setr voice_useSendingRangeOnly true     # solo oyes a quien está en tu rango (anti-troll, recomendado)
setr voice_enableUi 1
setr voice_enableProximityCycle 1
setr voice_defaultCycle "F11"           # tecla para cambiar distancia
setr voice_defaultVoiceMode 2           # 1 susurro, 2 normal, 3 gritar
setr voice_enableRadios 1
setr voice_defaultRadio "LMENU"         # Alt izquierdo
setr voice_defaultRadioVolume 30
setr voice_enableCalls 1
setr voice_defaultCallVolume 60
setr voice_enableSubmix 1
setr voice_enableRadioAnim 1
# Servidor de voz externo (FXServer dedicado solo a voz):
# setr voice_externalAddress "1.2.3.4"
# setr voice_externalPort 30120
```

Elige **un solo** modo de audio: `voice_useNativeAudio`, `voice_use3dAudio` o `voice_use2dAudio`.

## 18.3 Exports

```lua
-- Cliente
exports['pma-voice']:setRadioChannel(5)
exports['pma-voice']:setCallChannel(12345)
exports['pma-voice']:setRadioVolume(50)
exports['pma-voice']:setVoiceProperty('radioEnabled', true)
exports['pma-voice']:toggleMutePlayer(serverId)

-- Servidor
exports['pma-voice']:setPlayerRadio(src, 5)
exports['pma-voice']:setPlayerCall(src, 12345)
local enCanal = exports['pma-voice']:getPlayersInRadioChannel(5)
exports['pma-voice']:addChannelCheck(1, function(source)       -- canal 1 solo para policía
    return Player(source).state.trabajo == 'policia'
end)
```

State bags que usa: `proximity`, `radioChannel`, `callChannel`, `voiceIntent`, `disableRadio`.

## 18.4 Natives de Mumble (para sistemas propios)

`MumbleSetVoiceTarget`, `MumbleAddVoiceTargetChannel`, `MumbleAddVoiceTargetPlayerByServerId`, `MumbleClearVoiceTarget`, `MumbleSetVoiceChannel`, `MumbleSetAudioInputDistance`, `MumbleSetAudioOutputDistance`, `MumbleSetTalkerProximity`, `MumbleIsPlayerTalking`, `NetworkIsPlayerTalking`, `MumbleSetVolumeOverrideByServerId`, `MumbleSetSubmixForServerId`.

---

# 19. Seguridad y anti-cheat

## 19.1 Principios

1. **El cliente miente.** Todo lo que viene del cliente (eventos, state bags, callbacks NUI) puede estar manipulado: un *executor* de cheats puede disparar **cualquier** `TriggerServerEvent` con **cualquier** argumento.
2. **El servidor decide.** Dinero, ítems, permisos, precios, recompensas, posiciones válidas: se calculan y comprueban en el servidor.
3. **Mínimo privilegio.** Registra como *net event* solo lo imprescindible, da ACE solo a quien las necesita y no expongas secretos al cliente.
4. **Defensa en profundidad.** Combina validación por evento, límites de frecuencia, convars de seguridad, logs y un anti-cheat.

## 19.2 Errores típicos (y cómo evitarlos)

| Mal ❌ | Bien ✅ |
|---|---|
| `TriggerServerEvent('banco:dar', 5000)` y el servidor suma lo que llega | El servidor calcula la cantidad según la acción real (trabajo completado, precio de la tienda en `Config` del servidor). |
| El cliente dice "he completado el trabajo" y el servidor paga | El servidor comprueba distancia al punto, tiempo transcurrido desde el inicio y que el jugador tenía ese trabajo activo. |
| Precios en un `shared/config.lua` que el servidor lee del **evento** | El servidor usa su **propia** copia del `Config`, nunca el precio que envía el cliente. |
| Evento admin `admin:darDinero` sin comprobar permisos | `if not IsPlayerAceAllowed(src, 'admin.dinero') then return end` |
| Webhook de Discord en un `client_script` | Webhook en `server_script`, leído de una convar `set`. |
| SQL concatenado con datos del jugador | Placeholders `?` (ver 16.4). |
| `RegisterNetEvent` en eventos que solo se usan entre recursos del servidor | `AddEventHandler` (no es accesible desde la red). |
| Borrar entidades que manda el cliente por netId sin comprobar | Comprueba propietario, distancia, tipo y modelo. |
| Callback NUI que llama directamente a un evento de servidor con los datos tal cual | Validar en el servidor igualmente. |

## 19.3 Plantilla de evento seguro

```lua
local Cooldown = {}

RegisterNetEvent('tienda:comprar', function(itemName, cantidad)
    local src = source

    -- 1. Tipos y rangos
    if type(itemName) ~= 'string' or type(cantidad) ~= 'number' then return end
    cantidad = math.floor(cantidad)
    if cantidad < 1 or cantidad > 50 then return end

    -- 2. El ítem existe en la config DEL SERVIDOR
    local item = Config.ItemsTienda[itemName]
    if not item then return end

    -- 3. Frecuencia
    local ahora = GetGameTimer()
    if Cooldown[src] and ahora - Cooldown[src] < 500 then return end
    Cooldown[src] = ahora

    -- 4. Contexto: está cerca de una tienda
    local coords = GetEntityCoords(GetPlayerPed(src))
    local cerca = false
    for _, t in ipairs(Config.Tiendas) do
        if #(coords - t.coords) < 5.0 then cerca = true break end
    end
    if not cerca then
        return LogSospechoso(src, 'compra lejos de tienda')
    end

    -- 5. Lógica con datos del servidor
    local precio = item.precio * cantidad
    if not QuitarDinero(src, precio) then return end
    DarItem(src, itemName, cantidad)
end)

AddEventHandler('playerDropped', function() Cooldown[source] = nil end)
```

## 19.4 Convars de seguridad recomendadas

```cfg
sv_scriptHookAllowed 0
sv_pureLevel 1
set sv_entityLockdown relaxed           # o strict si TODO se crea en servidor
set sv_filterRequestControl 2
setr sv_stateBagStrictMode false        # true si ningún recurso escribe state bags desde el cliente
sv_endpointPrivacy true
set sv_enableNetworkedPhoneExplosions false
set sv_requestParanoia 1                # si estás detrás de proxy, revísalo antes
# Bloquear eventos de juego que no uses:
# block_net_game_event REQUEST_PHONE_EXPLOSION_EVENT
```

## 19.5 Eventos de juego para detectar trampas (servidor)

```lua
-- Explosiones: bloquear tipos peligrosos y registrar
AddEventHandler('explosionEvent', function(sender, ev)
    -- IDs de tipo de explosión: 0 GRENADE, 1 GRENADELAUNCHER, 2 STICKYBOMB, 3 MOLOTOV, 4 ROCKET, 5 TANKSHELL...
    -- (lista completa en la documentación del native ADD_EXPLOSION)
    local prohibidas = { [1] = true, [4] = true, [5] = true }
    if prohibidas[ev.explosionType] then
        CancelEvent()
        LogSospechoso(sender, ('explosión tipo %s'):format(ev.explosionType))
    end
end)

-- Armas entregadas por otros clientes (no las da el servidor)
AddEventHandler('giveWeaponEvent', function(sender, data)
    CancelEvent()
    LogSospechoso(sender, 'giveWeaponEvent')
end)

-- Intentos de quitar tareas a otros jugadores (sacarlos del coche, congelarlos)
AddEventHandler('clearPedTasksEvent', function(sender, data)
    if data.immediately then
        CancelEvent()
        LogSospechoso(sender, 'clearPedTasksEvent')
    end
end)

-- Daño anómalo
AddEventHandler('weaponDamageEvent', function(sender, data)
    if data.weaponDamage > 500 then
        CancelEvent()
        LogSospechoso(sender, 'daño excesivo ' .. data.weaponDamage)
    end
end)
```

> Ajusta estas reglas a tu servidor y **prueba** antes de banear automáticamente: los falsos positivos son peores que no tener reglas.

## 19.6 Protección de eventos con tokens: ¿sirve?

Los "tokens" que se pasan en cada `TriggerServerEvent` **no protegen de verdad**: el cheat puede leer el token desde la memoria del cliente. La seguridad real es **validar en el servidor** (19.3). Los tokens solo añaden fricción.

## 19.7 Eventos "trampa" (*honeypots*)

Registra eventos con nombres atractivos que **ningún recurso legítimo** usa (`esx_admin:giveMoney`, `bank:addMoney`…) y banea a quien los dispare:

```lua
local trampas = { 'esx:giveInventoryItemAdmin', 'banco:darDineroGratis', 'admin:setGod' }
for _, ev in ipairs(trampas) do
    RegisterNetEvent(ev, function()
        local src = source
        LogSospechoso(src, 'honeypot ' .. ev)
        -- BanPlayer(src, 'Uso de cheats')
    end)
end
```

## 19.8 Identificadores, tokens y bans

- Guarda **todos** los identificadores (`license`, `license2`, `fivem`, `discord`, `steam`, `ip`) **y** los tokens (`GetPlayerTokens`) al banear.
- Al conectar (`playerConnecting`), comprueba si **cualquiera** de ellos coincide con un ban.
- `ip` cambia y puede compartirse (VPN, residencias): no lo uses como único criterio.
- txAdmin incluye un sistema de **bans y avisos** con base de datos propia que ya hace esto.

## 19.9 Anti-cheat

- **Cfx.re** tiene medidas propias en el cliente y bans globales para cheats conocidos.
- txAdmin ofrece bans, avisos, logs de acciones y de servidor.
- Existen anti-cheats de terceros (de pago y gratuitos). Elige uno con buena reputación y que no rompa tu framework; ningún anti-cheat sustituye a validar tus eventos.
- **Cuidado con "anti-cheats" o recursos *leakeados***: suelen traer *backdoors* (código ofuscado que hace `PerformHttpRequest` y ejecuta lo que recibe con `load`). Busca en tus recursos `load(`, `loadstring`, `PerformHttpRequest` a dominios raros, `assert(load(` y código ofuscado.

```bash
# Buscar patrones sospechosos en todos los recursos (Linux)
grep -rnE "assert\(load|loadstring\(|load\(.*PerformHttpRequest|\\\\x[0-9a-f]{2}\\\\x" resources/ --include=*.lua | head -50
```

## 19.10 Seguridad del host

- Servidor de juego con **usuario sin privilegios** (nunca `root`/Administrador).
- Firewall: solo 30120 TCP/UDP (y 40120 restringido a tu IP o tras VPN).
- txAdmin con contraseñas fuertes y cuentas Cfx.re individuales para cada admin; revoca accesos de quien deje el staff.
- Mantén artefactos, txAdmin y recursos actualizados.
- Backups automáticos fuera del servidor (BD + `server-data`).
- **Protección DDoS** del proveedor de hosting; para grandes servidores, proxies/redes de mitigación (ver 25.3).

---

# 20. Rendimiento y optimización

## 20.1 Medir antes de optimizar

| Herramienta | Dónde | Qué muestra |
|---|---|---|
| `resmon 1` | F8 (cliente) | Tiempo de CPU (ms) y memoria de **cada recurso** en el cliente. |
| `profiler record 500` → `profiler view` / `profiler saveJSON archivo.json` | F8 o consola del servidor | Perfil detallado de N frames (visor en Chrome DevTools/Perfetto). |
| `cl_drawfps true` / `cl_drawperf true` | F8 | FPS y estadísticas. |
| `netgraph true` | F8 | Ping, pérdida de paquetes, ancho de banda. |
| `strdbg` / `strlist` / `strmem` | F8 | Streaming de assets y memoria. |
| txAdmin → *Dashboard* | Panel | CPU/RAM del servidor, gráfico de rendimiento por hilo. |
| `/perf` (Prometheus) | `http://IP:30120/perf/` | Histogramas de tiempo de tick (protegido con `sv_prometheusBasicAuthUser/Password`). |

> Algunos comandos de desarrollador del cliente (`resmon`, `strdbg`, `profiler`…) pueden requerir el **modo desarrollador**. Si ves *"Access denied for command"*, inicia FiveM con `+set moo 31337` o usa un canal de actualización de desarrollo (Ajustes → canal *Beta/Canary*).

**Referencia en `resmon`:** un recurso de cliente bien hecho debería estar en **0.00-0.02 ms** en reposo. Por encima de 0.10 ms constante, revisa; por encima de 0.5-1 ms, hay un problema serio.

## 20.2 Cliente: reglas de oro

1. **Nunca `Wait(0)` permanente** si no dibujas nada. Usa **espera dinámica** (8.1) o `lib.points`/`lib.zones` (ox_lib).
2. **Un solo bucle** por recurso que gestione varias cosas, mejor que diez bucles.
3. **Cachea** `PlayerPedId()`, coordenadas y vehículo: actualízalos cada 250-500 ms en vez de por frame (o usa `cache.*` de ox_lib).
4. **Evita natives caros por frame**: `GetGamePool`, `GetClosestVehicle`, `GetEntityCoords` de muchas entidades, raycasts.
5. **`RegisterKeyMapping`** en lugar de comprobar teclas cada frame.
6. **Eventos en lugar de *polling***: reacciona a `gameEventTriggered`, state bags o `lib.onCache` en lugar de comprobar cada frame si algo cambió.
7. Libera modelos/animaciones con `SetModelAsNoLongerNeeded`/`RemoveAnimDict`.
8. **NUI**: pocas actualizaciones por segundo, nada de animaciones pesadas ocultas (14.10).

```lua
-- ❌ Mal: 3 natives por frame, siempre
CreateThread(function()
    while true do
        local ped = PlayerPedId()
        local veh = GetVehiclePedIsIn(ped, false)
        if veh ~= 0 then
            local vel = GetEntitySpeed(veh) * 3.6
            SendNUIMessage({ vel = vel })    -- ¡60 mensajes por segundo a la NUI!
        end
        Wait(0)
    end
end)

-- ✅ Bien: solo actúa dentro de vehículo y a 10 Hz
CreateThread(function()
    while true do
        local veh = GetVehiclePedIsIn(PlayerPedId(), false)
        if veh ~= 0 then
            SendNUIMessage({ vel = math.floor(GetEntitySpeed(veh) * 3.6) })
            Wait(100)
        else
            Wait(1000)
        end
    end
end)
```

## 20.3 Servidor: reglas de oro

1. **No bloquees el hilo principal**: nada de bucles enormes sin `Wait`, ni lecturas de archivos gigantes en cada evento.
2. **Base de datos**: consultas indexadas, cacheadas y en lote; nunca por tick (16.4).
3. **Envía eventos solo a quien los necesita** (jugadores cercanos, por *scope* o bucket), no a `-1` constantemente.
4. **State bags** para estado persistente compartido en vez de reenviar eventos (13.4), pero sin meter tablas gigantes que cambian cada segundo.
5. **Eventos latentes** para datos grandes.
6. **Limita entidades**: limpia vehículos abandonados, objetos y peds de script. Miles de entidades en red degradan a todos.
7. **Reinicios programados** (txAdmin) cada 6-12 h en servidores grandes para liberar memoria.

## 20.4 Población y entidades

- La población (tráfico, peatones) consume CPU de los clientes y ancho de banda. Reduce densidad con los multiplicadores *ThisFrame* (12.12) o desactiva con `onesync_population false`/buckets sin población.
- `SetEntityDistanceCullingRadius` solo cuando haga falta (aumenta el tráfico de red).
- Borra entidades de script cuando ya no se usen (`DeleteEntity` en servidor).

## 20.5 Streaming

- Vigila el tamaño total de assets que descarga un jugador nuevo; cientos de vehículos/ropa en 4K → descargas de varios GB y *crasheos* por memoria.
- Optimiza texturas (15.9) y elimina recursos que no uses.
- Usa un **servidor de archivos/caché externo** (proxy de descargas, 25.3) en servidores grandes para no saturar el ancho de banda del servidor de juego.

---

# 21. Depuración y errores comunes

## 21.1 Dónde mirar

| Lugar | Qué ves |
|---|---|
| **Consola del servidor** / *Live Console* de txAdmin | Errores de `server_scripts`, arranque de recursos, conexiones. |
| **F8** en el cliente | Errores de `client_scripts`, `print` del cliente. |
| **DevTools de NUI** (`nui_devtools`) | Errores de JavaScript y `console.log` de tus interfaces. |
| **Logs del cliente** | `%localappdata%\FiveM\FiveM.app\logs\CitizenFX_log_*.log` |
| **Crash dumps** | `%localappdata%\FiveM\FiveM.app\crashes\` (el cliente ofrece un código de crash para el soporte). |
| **txAdmin → Server Log / System Logs** | Historial de acciones, conexiones, muertes, chat, comandos. |

## 21.2 Leer un error de script

```
SCRIPT ERROR: @mi_recurso/client/main.lua:42: attempt to index a nil value (local 'data')
> handler (@mi_recurso/client/main.lua:42)
```

- `@mi_recurso/client/main.lua:42` → recurso, archivo y **línea**.
- `attempt to index a nil value (local 'data')` → intentaste acceder a `data.algo` cuando `data` era `nil`.
- Las líneas con `>` son la *traza* (de dónde venía la llamada).

## 21.3 Errores frecuentes y soluciones

| Error | Causa | Solución |
|---|---|---|
| `Couldn't find resource X` | La carpeta no existe, mal escrita o falta `refresh`. | Revisa el nombre (sensible a mayúsculas en Linux) y ejecuta `refresh`. |
| `Could not find dependency X for resource Y` | Falta un recurso del que depende. | Instálalo y arráncalo **antes**. |
| `Failed to load script X` | Ruta mal en `fxmanifest.lua` o error de sintaxis. | Revisa rutas/globs y la sintaxis. |
| `No such export X in resource Y` | El recurso Y no está arrancado, el nombre del export es incorrecto o cambió entre versiones. | Comprueba versión y `GetResourceState`. |
| `attempt to index a nil value` | Variable `nil` (jugador no cargado, item inexistente…). | Comprueba antes de usar: `if not x then return end` o `x?.campo`. |
| `attempt to call a nil value (global 'X')` | Función no definida, framework no cargado, orden de carga. | Revisa `shared_scripts` (`@ox_lib/init.lua`, `@es_extended/imports.lua`) y el orden de `ensure`. |
| `attempt to perform arithmetic on a string value` | Lua 5.4 no convierte strings en números. | `tonumber()`. |
| `bad argument #1 to 'X' (number expected, got nil)` | Pasaste `nil` a un native. | Valida argumentos. |
| `mysql_connection_string is not set` / `ER_ACCESS_DENIED_ERROR` | Cadena de conexión ausente o credenciales incorrectas. | Revisa `set mysql_connection_string` y los permisos del usuario SQL. |
| `ER_BAD_FIELD_ERROR` / `ER_NO_SUCH_TABLE` | Falta importar el `.sql` del recurso. | Importa el SQL incluido. |
| `You lack the required entitlement` | Recurso con Asset Escrow no asociado a tu clave. | Usa la clave de la cuenta que compró el recurso; no lo renombres. |
| `Server list query returned an error` / el servidor no aparece | Clave inválida, puertos cerrados, artefacto sin soporte. | Revisa `sv_licenseKey`, firewall, y que el artefacto sea ≥ 35245. |
| `Failed to verify server ownership` / *heartbeat* | La IP no coincide con la registrada en la clave. | Regenera la clave con la IP correcta en Portal. |
| `Pool full: X` / `Exhausted pool` | Demasiados assets de un tipo. | `increase_pool_size` (5.5) y optimiza. |
| `Oversized assets` en consola | Texturas/modelos demasiado grandes. | Optimiza (15.9). |
| `Connection timed out` / `Connection rejected` al entrar | Firewall, servidor saturado, *deferrals* sin `done()`. | Revisa puertos y que todo `defer()` termine en `done()`. |
| *Network event X was not safe for net* | El evento no está registrado con `RegisterNetEvent`. | Regístralo (si debe venir por red). |
| Jugador congelado con cursor | NUI con foco sin liberar. | `SetNuiFocus(false, false)` en todos los caminos de cierre. |
| `mono_rt2 is no longer supported` | Recurso C# con `mono_rt2` caducado. | Quita la línea `mono_rt2` y recompila para el runtime clásico. |

## 21.4 Técnicas de depuración

```lua
-- Modo debug controlado por convar
local DEBUG = GetConvar('mi_recurso_debug', 'false') == 'true'
local function dbg(...) if DEBUG then print('^3[DEBUG]^7', ...) end end

-- Ver tablas
print(json.encode(tabla, { indent = true }))
-- o con ox_lib
lib.print.info(tabla)

-- Medir cuánto tarda algo
local t = os.clock()
HacerAlgoPesado()
print(('Tardó %.3f ms'):format((os.clock() - t) * 1000))
```

- Reinicia solo tu recurso con `ensure mi_recurso` (no hace falta reiniciar el servidor).
- Si un recurso de cliente no se actualiza, puede ser caché: `ensure` de nuevo o borra la caché del cliente.
- Usa un **servidor local de desarrollo** (`sv_lan true` o tu propia clave) con `sv_maxclients 2` y sin recursos innecesarios.

---

# 22. El cliente FiveM

## 22.1 Instalación

1. Descarga desde **https://fivem.net** (botón de descarga de FiveM).
2. Ejecuta `FiveM.exe`; se instalará en `%localappdata%\FiveM\`.
3. Al abrirlo te pedirá iniciar sesión con tu cuenta de Rockstar (verifica que tienes GTA V) y opcionalmente con tu cuenta Cfx.re.
4. Desde 2026 FiveM tiene su propia **Steam App ID** (Rich Presence y grupos de amigos en Steam).

## 22.2 Carpetas importantes

| Ruta | Contenido |
|---|---|
| `%localappdata%\FiveM\FiveM.app\` | Instalación del cliente. |
| `...\FiveM.app\CitizenFX.ini` | Configuración (ruta del juego, canal de actualización). |
| `...\FiveM.app\data\server-cache\` | Caché de recursos descargados de servidores. |
| `...\FiveM.app\data\cache\`, `server-cache-priv\`, `nui-storage\` | Otras cachés (NUI, archivos privados). |
| `...\FiveM.app\logs\` | Logs del cliente. |
| `...\FiveM.app\crashes\` | Volcados de *crash*. |
| `...\FiveM.app\plugins\` | Plugins gráficos permitidos (ReShade/ENB según `sv_pureLevel`). |
| `...\FiveM.app\mods\` | Mods locales (solo en servidores sin *pure mode*). |

**Limpiar caché** (soluciona muchos problemas de descarga/texturas): cierra FiveM y borra `data\cache`, `data\server-cache` y `data\server-cache-priv`. **No** borres `citizen` ni el resto de la carpeta. Borrar `caches.xml` soluciona algunos errores de descarga.

## 22.3 Opciones de lanzamiento

| Opción | Efecto |
|---|---|
| `FiveM.exe -b3407` | Lanza con una build concreta del juego. |
| `FiveM.exe -pure_1` | Fuerza *pure mode* nivel 1. |
| `FiveM.exe +set moo 31337` | Activa el modo desarrollador del cliente (comandos de depuración). |
| `fivem://connect/IP:PUERTO` | Conexión directa (también `fivem://connect/cfx.re/join/xxxx`). |

## 22.4 Comandos de consola del cliente (F8)

**Para todos:**

| Comando | Uso |
|---|---|
| `connect <ip:puerto \| cfx.re/join/xxxx>` | Conectarse. |
| `disconnect` | Desconectarse. |
| `quit` | Salir. |
| `cl_drawfps true` | Mostrar FPS. |
| `cl_drawperf true` | Estadísticas de rendimiento. |
| `bind keyboard F7 "comando"` / `rbind` / `unbind` | Asignar teclas a comandos. |
| `loadlevel` / `storymode` | Cargar mapas / modo historia (según disponibilidad). |

**De desarrollo** (pueden requerir modo desarrollador):

| Comando | Uso |
|---|---|
| `resmon 1` | Monitor de recursos. |
| `netgraph true` | Gráfico de red. |
| `strdbg`, `strlist`, `strmem` | Depuración de streaming. |
| `profiler record 500` / `profiler status` / `profiler view` / `profiler saveJSON x.json` | Perfilador. |
| `nui_devtools` | DevTools de NUI. |
| `netEventLog` | Registro de eventos de red. |
| `cl_drawResTimeGraphs` / `cl_drawResTimeWarnings` | Gráficas/avisos de tiempo por recurso. |
| `cmdlist` | Lista de comandos disponibles. |
| `save_gta_cache` | Guarda la caché del juego. |

La consola F8 tiene un **cuadro de filtro** (desde 2025) para buscar en la salida.

## 22.5 Nombres de jugador

Si el jugador no tiene otro nombre configurado, FiveM le asigna un nombre aleatorio tipo *"IcyGoose1337"* en lugar del nombre de usuario de Windows.

## 22.6 Problemas habituales del jugador

| Problema | Solución |
|---|---|
| "Could not find game executable" | Indica la ruta de GTA V en Ajustes o en `CitizenFX.ini`. |
| Errores de propiedad del juego | Abre el Rockstar Games Launcher e inicia sesión; verifica los archivos del juego. |
| *Crash* al entrar a un servidor concreto | Limpia la caché; prueba otra build; revisa la memoria (assets pesados). |
| Texturas que no cargan | Ajustes gráficos (calidad de texturas), cierra programas que usen VRAM, limpia caché. |
| No se oye la voz | Permisos de micrófono de Windows, dispositivo en Ajustes → Voz, tecla N por defecto. |
| "Server is running an outdated version" | El servidor usa artefactos sin soporte; debe actualizar a ≥ 35245. |

---

# 23. Monetización, legalidad y Asset Escrow

> Esto **no es asesoramiento legal**. Lee siempre los documentos oficiales: el texto vinculante es el del PLA.

## 23.1 Creator Platform License Agreement (PLA)

- Documento: **https://fivem.net/terms** (redirige al PDF vigente, *"Last Updated: Sept. 10 2026"*). Hubo una actualización importante en vigor desde el **12 de enero de 2026**.
- Partes: **Rockstar Games** y **Take-Two**. Incorpora los Términos de Servicio y las Normas de la Comunidad de Rockstar.

**Obligaciones de un servidor:**

- Toda web/tienda del servidor debe identificar al **operador**, dar un **email de contacto** y mostrar el aviso: **"[NOMBRE DEL SERVIDOR] IS NOT APPROVED, SPONSORED, OR ENDORSED BY ROCKSTAR GAMES"**.
- **No** usar propiedad intelectual de Rockstar en el nombre o la marca del servidor (logos, "GTA", tipografías oficiales…).
- **No** usar música con licencia ni voces del juego alteradas.

**Monetización prohibida (§3.1):**

1. Retirada de dinero real (*cash-out*) o apuestas con dinero real.
2. Cajas de botín (*loot boxes*), *gacha*, sorteos.
3. **Vender moneda virtual del juego por dinero real.**
4. Vender objetos virtuales creados por Rockstar.
5. Servidores patrocinados por marcas o presentados como "oficiales".
6. Tiendas que agregan *assets* de terceros.
7. Publicidad o patrocinios de terceros.
8. Criptomonedas o NFTs.

Otros puntos: Rockstar puede exigir el uso de **servicios autorizados** (como Tebex) y prohibir proveedores no autorizados con 30 días de aviso; en el **Marketplace**, las compras únicas son irrevocables y las suscripciones terminan con la suscripción; prohibido usar los assets para entrenar IA.

## 23.2 Tebex

- **Tebex** es el **socio de monetización exclusivo** de Cfx.re. Las tiendas de servidor (VIP, prioridad de cola, cosméticos permitidos) y la venta de recursos van por Tebex.
- Configuración: crea la tienda en Tebex, vincúlala y pon la clave en `server.cfg`:

```cfg
set sv_tebexSecret "tu_clave_secreta_de_tebex"
```

- Tebex ejecuta **comandos** en tu servidor cuando alguien compra (por ejemplo `darvip {id}`); créalos con `RegisterCommand` restringido y valida los argumentos.
- Solo los **creadores acreditados por Tebex** pueden revender assets. Un servidor pillado con assets *leakeados* recibe una **suspensión de 2 semanas**; si reincide, **cierre permanente** (política de agosto de 2025).

## 23.3 Asset Escrow

**Asset Escrow** cifra recursos de pago para que solo funcionen en servidores autorizados.

- Admite **Lua** y modelos **YFT, YDD, YDR**. **La NUI no se cifra.** Tamaño máximo: 1 GB.
- El creador sube el recurso a **Portal** y lo vende **solo** a través de paquetes "FiveM Asset" de Tebex.
- El comprador lo descarga desde **Portal** (o desde Tebex) y funciona en los servidores cuya clave pertenece a su cuenta.
- Los assets **no se pueden transferir** entre cuentas. Los de suscripción se retiran al caducar.
- Portal guarda hasta **5 versiones** de cada asset con su *changelog* (desde mayo de 2026).
- El creador decide qué queda abierto con `escrow_ignore` en el manifest (normalmente `config.lua`, locales, `client/editable.lua`…).

```lua
escrow_ignore {
    'config.lua',
    'locales/*.lua',
    'client/editable.lua',
    'server/editable.lua',
}
```

## 23.4 Si vendes recursos (creadores)

1. Cuenta en Cfx.re + vinculación con Tebex como creador.
2. Prepara el recurso: deja configurables los archivos con `escrow_ignore`, documenta dependencias.
3. Súbelo en Portal → *Assets* → *Create*.
4. Crea el paquete en tu tienda Tebex de tipo **FiveM Asset** y asócialo.
5. Mantén versiones con *changelog* en Portal.

---

# 24. txAdmin a fondo

**txAdmin** viene integrado en FXServer. Versión actual: **8.1.1** (junio de 2026). Es oficialmente parte de Cfx.re desde abril de 2025.

## 24.1 Funciones

- **Despliegue con recetas** (*recipes*): ESX, QBCore, Qbox, CFX Default y otras (en 2026 se añadieron StreetKings, vMenu y Warfare Tactics V).
- **Menú dentro del juego** con `/tx` (o `/txadmin`) o una tecla: noclip, teletransporte, curar, espectar, gestionar jugadores, anuncios.
- **Inicio de sesión** con cuenta Cfx.re o contraseña; **permisos** por administrador; **registro de acciones**.
- **Bot de Discord**: *embed* de estado, comandos de allowlist e información de jugadores.
- **Monitorización**: reinicio automático si el servidor se cae o se cuelga, CPU/RAM, **Live Console** con historial y búsqueda, gráfico de rendimiento por hilo.
- **Registro de actividad** del servidor (conexiones, muertes, chat, comandos, explosiones…).
- **Base de datos de jugadores** propia (no necesita MySQL): notas, tiempo jugado, historial.
- **Avisos y bans** (por identificadores y tokens).
- **Allowlist**: por miembro de Discord, por rol de Discord, por licencia aprobada o solo administradores; desde la 8.1, también una opción de allowlist externa.
- **Reinicios programados** con avisos a los jugadores.
- **Editor del `server.cfg`** y más de 30 idiomas.

Cambios recientes:

- **v8.0** (marzo de 2025): apagado ordenado con SIGINT/SIGTERM/SIGHUP, los reinicios programados se saltan si el servidor está cerrado, tolerancia de arranque de recursos de 90 s y nueva página de login.
- **v8.1** (junio de 2026): allowlist externa, borrar IDs de jugadores, consola que sigue el tema, `printFxResourcesBootLog` y "whitelist" renombrado a "allowlist". El candado de allowlist en la lista de servidores se activa desde txAdmin o con `sets sv_appearAllowlisted true` y `sets sv_allowlistInstructions "..."`.

## 24.2 Configuración por variables de entorno (`TXHOST_*`)

Desde la v8, la configuración del *host* se hace con **variables de entorno** (las antiguas convars `txAdminPort`, `txAdminInterface`, `txDataPath` y el archivo `txAdminZapConfig.json` están **obsoletos**):

| Variable | Uso |
|---|---|
| `TXHOST_DATA_PATH` | Carpeta de datos de txAdmin (`txData`). |
| `TXHOST_TXA_PORT` | Puerto del panel (defecto **40120**; no puede ser 30120). |
| `TXHOST_FXS_PORT` | Puerto del juego (no puede ser 40120). |
| `TXHOST_INTERFACE` | Interfaz de escucha (defecto `0.0.0.0`). |
| `TXHOST_TXA_URL` | URL pública del panel. |
| `TXHOST_GAME_NAME` | `fivem` o `redm`. |
| `TXHOST_MAX_SLOTS` | Límite de slots (para *hostings*). |
| `TXHOST_QUIET_MODE` | Menos salida por consola. |
| `TXHOST_API_TOKEN` | Token para el endpoint `/host/status`. |
| `TXHOST_PROVIDER_NAME` / `TXHOST_PROVIDER_LOGO` | Marca del proveedor de hosting. |
| `TXHOST_DEFAULT_DBHOST/PORT/USER/PASS/NAME` | BD por defecto para recetas. |
| `TXHOST_DEFAULT_CFXKEY` | Clave por defecto. |
| `TXHOST_DEFAULT_ACCOUNT` | Cuenta de administrador por defecto. |
| `TXHOST_IGNORE_DEPRECATED_CONFIGS` | Ignorar la configuración antigua. |

Ejemplo (Linux, `systemd`):

```ini
[Service]
Environment=TXHOST_DATA_PATH=/home/fivem/FXServer/txData
Environment=TXHOST_TXA_PORT=40120
ExecStart=/bin/bash /home/fivem/FXServer/server/run.sh
```

Ejemplo (Windows, `.bat`):

```bat
@echo off
set TXHOST_DATA_PATH=C:\FXServer\txData
set TXHOST_TXA_PORT=40120
C:\FXServer\server\FXServer.exe
```

## 24.3 Convars del menú de txAdmin

| Convar | Defecto | Descripción |
|---|---|---|
| `txAdmin-menuEnabled` | `true` | Activa el menú (requiere reiniciar). |
| `txAdmin-menuAlignRight` | `false` | Menú a la derecha. |
| `txAdmin-menuPageKey` | `Tab` | Tecla para cambiar de página (código `event.code`). |
| `txAdmin-playerModePtfx` | `true` | Partículas/sonido al activar god mode, noclip… |
| `txAdmin-hideAdminInPunishments` | `true` | Oculta el nombre del admin en bans y avisos. |
| `txAdmin-hideAdminInMessages` | `false` | Oculta el admin en anuncios y mensajes directos. |
| `txAdmin-hideDefaultAnnouncement` | `false` | Oculta el anuncio por defecto (para usar tu propio diseño con el evento). |
| `txAdmin-hideDefaultDirectMessage` | `false` | Igual para los mensajes directos. |
| `txAdmin-hideDefaultWarning` | `false` | Igual para los avisos (*warns*). |
| `txAdmin-hideDefaultScheduledRestartWarning` | `false` | Igual para el aviso de reinicio programado. |
| `txAdmin-menuPlayerIdDistance` | `150` | Distancia a la que se ven los IDs de jugador. |
| `txAdmin-menuDrunkDuration` | `30` | Segundos del efecto "borracho" (acción *troll*). |
| `txAdmin-menuAnnounceNotiPos` | `top-center` | Posición de los anuncios. |
| `txAdmin-debugMode` | `false` | Mensajes de depuración. |

```cfg
setr txAdmin-menuEnabled true
setr txAdmin-hideAdminInPunishments true
setr txAdmin-menuPlayerIdDistance 100
```

Comandos: `/tx` o `/txadmin` (con un ID opcional abre la ficha de ese jugador) y `/txAdmin-reauth` (vuelve a autenticarte). Tecla configurable en *Ajustes → Teclas → FiveM → "(txAdmin) Menu: Open Main Page"*.

## 24.4 Eventos de txAdmin para tus scripts

Todos se llaman `txAdmin:events:<nombre>` y reciben **una tabla** como único parámetro:

| Evento | Campos principales |
|---|---|
| `announcement` | `author`, `message` |
| `serverShuttingDown` | `delay`, `author`, `message` |
| `scheduledRestart` | `secondsRemaining`, `translatedMessage` |
| `scheduledRestartSkipped` | `secondsRemaining`, `temporary`, `author` |
| `playerBanned` | `author`, `reason`, `actionId`, `expiration`, `durationTranslated`, `targetNetId`, `targetIds`, `targetHwids`, `targetName`, `kickMessage` |
| `playerKicked` | `target`, `author`, `reason`, `dropMessage` |
| `playerWarned` | `author`, `reason`, `actionId`, `targetNetId`, `targetIds`, `targetName` |
| `playerDirectMessage` | `target`, `author`, `message` |
| `playerHealed` | `target`, `author` |
| `actionRevoked` | `actionId`, `actionType`, `actionReason`, `actionAuthor`, `playerName`, `playerIds`, `revokedBy` |
| `whitelistPlayer` / `whitelistPreApproval` / `whitelistRequest` | Cambios de allowlist |
| `adminAuth` | `netid`, `isAdmin`, `username` |
| `adminsUpdated` | Array de IDs de admins conectados |
| `configChanged` | (sin datos) |
| `consoleCommand` | `author`, `channel`, `command` |

Obsoletos: `healedPlayer` → `playerHealed`; `skippedNextScheduledRestart` → `scheduledRestartSkipped`; `playerWhitelisted`.

```lua
-- Guardar todo antes de un reinicio programado
AddEventHandler('txAdmin:events:scheduledRestart', function(data)
    if data.secondsRemaining == 60 then
        GuardarTodosLosJugadores()
    end
end)

-- Apagado del servidor (data.delay = ms antes del cierre)
AddEventHandler('txAdmin:events:serverShuttingDown', function(data)
    GuardarTodosLosJugadores()
end)

-- Anuncio con tu propia UI (con txAdmin-hideDefaultAnnouncement true)
AddEventHandler('txAdmin:events:announcement', function(data)
    TriggerClientEvent('ox_lib:notify', -1, { title = 'Anuncio', description = data.message, type = 'inform', duration = 10000 })
end)
```

---

# 25. Hosting, despliegue y operación

## 25.1 Opciones de hosting

| Tipo | Pros | Contras |
|---|---|---|
| **PC de casa** | Gratis, ideal para desarrollar | IP doméstica expuesta, sin protección DDoS, ancho de banda de subida limitado |
| **VPS** | Barato, control total | Rendimiento por núcleo variable; ojo con CPUs compartidas |
| **Servidor dedicado** | Máximo rendimiento y control | Más caro, administración propia |
| **Hosting específico de FiveM** (panel) | Fácil, txAdmin preinstalado | Menos control, a veces sobrevendido |

Al elegir: **CPU de alta frecuencia**, **NVMe**, **protección DDoS** con filtrado para juegos (UDP) y ubicación cercana a tus jugadores.

## 25.2 Flujo de trabajo recomendado

1. `server-data` en un **repositorio Git privado** (sin `secrets.cfg`, `cache/`, `txData/`).
2. Un **servidor de desarrollo** local o separado; nunca pruebes en producción.
3. Despliegue: `git pull` en el servidor + `ensure` del recurso cambiado (o reinicio programado).
4. **Backups** automáticos de BD y `server-data` fuera de la máquina.
5. **Changelog** para tu comunidad.

`.gitignore` sugerido:

```gitignore
cache/
txData/
secrets.cfg
*.log
node_modules/
db/
.DS_Store
Thumbs.db
```

## 25.3 Proxies y descargas a gran escala

Con un proxy (nginx) delante del servidor puedes ocultar la IP real, servir las descargas con caché y usar HTTPS con tu dominio:

```cfg
# server.cfg
set sv_forceIndirectListing true                     # la lista no anuncia la IP real
set sv_listingHostOverride "fivem.midominio.com"     # la lista consulta tu dominio/proxy
set sv_proxyIPRanges "100.64.1.1/32"                 # IP(s) del proxy (CIDR): pueden enviar X-Real-IP
set sv_endpoints "100.64.1.2:30120"                  # endpoint(s) UDP reales o proxies de UDP
fileserver_add ".*" "https://fivem.midominio.com/files"  # descargas de recursos a través del proxy
set adhesive_cdnKey "una_clave_secreta"              # ofuscación con clave global (necesaria para cachear)
```

```nginx
# nginx: proxy de conexión + caché de archivos
upstream backend {
    server 100.64.1.2:30120;
}

proxy_cache_path /srv/cache levels=1:2 keys_zone=assets:48m max_size=20g inactive=2h;

server {
    listen 443 ssl http2;
    server_name fivem.midominio.com;
    ssl_certificate     /etc/letsencrypt/live/fivem.midominio.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/fivem.midominio.com/privkey.pem;

    location / {
        proxy_pass http://backend;
        proxy_pass_request_headers on;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /files/ {
        proxy_pass http://backend$request_uri;
        proxy_cache assets;
        proxy_cache_valid 1y;
        proxy_cache_lock on;
        proxy_cache_revalidate on;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

Comprueba que funciona abriendo en el navegador `https://fivem.midominio.com/info.json`, `/players.json` y `/dynamic.json`, y que `/client` responde *"/client is POST only"*.

> El UDP del juego **no** pasa por nginx HTTP: o lo expones directamente en `sv_endpoints` o usas un proxy UDP (nginx `stream`, o el de tu proveedor anti-DDoS).

> El antiguo proxy inverso `*.users.cfx.re` se cerró el **31 de marzo de 2026**: si dependías de él, configura tu propio dominio/proxy.

## 25.4 Mantenimiento periódico

- **Semanal**: revisar errores en consola, recursos con alto `resmon`, tamaño de la BD.
- **Mensual**: actualizar artefactos *recommended*, txAdmin, ox_lib/oxmysql/framework (leyendo *changelogs*), revisar bans y logs.
- **Siempre**: probar actualizaciones en desarrollo primero y tener un plan de vuelta atrás.

---

# 26. Buenas prácticas de desarrollo

## 26.1 Nombres y organización

- **Nombres de recursos** en minúsculas, sin espacios: `mi_tienda`, `prefix_trabajo_basurero`. Usa un **prefijo** propio para tus recursos (`lx_`, `rp_`…).
- **Nombres de eventos** con espacio de nombres: `recurso:accion` o `recurso:server:accion` / `recurso:client:accion`.
- **Exports** en PascalCase o camelCase, pero **consistentes**.
- Separa `client/`, `server/`, `shared/`, `web/`, `locales/`, `sql/`.
- Un `config.lua` (compartido) para lo que el dueño del servidor quiere cambiar, y `server/config.lua` (solo servidor) para valores sensibles (precios autoritativos, webhooks).

## 26.2 Configuración

```lua
-- shared/config.lua
Config = {}
Config.Locale = GetConvar('ox:locale', 'es')
Config.Debug = false
Config.Blip = { sprite = 52, color = 2, scale = 0.8 }
```

```lua
-- server/config.lua (no visible para el cliente)
ServerConfig = {
    Webhook = GetConvar('mi_tienda_webhook', ''),
    Precios = { agua = 5, pan = 3 },
}
```

## 26.3 Locales (traducciones)

Con ox_lib: `locales/es.json`, `locales/en.json` + `lib.locale()` (ver 17.1). Sin librerías:

```lua
-- locales/es.lua
Locales = Locales or {}
Locales['es'] = { compra_ok = 'Has comprado %sx %s', sin_dinero = 'No tienes dinero suficiente' }

-- shared/locale.lua
function _L(key, ...)
    local str = (Locales[Config.Locale] or Locales['es'])[key] or key
    return select('#', ...) > 0 and str:format(...) or str
end
```

## 26.4 Versionado y comprobación de actualizaciones

- Usa **SemVer** (`1.2.3`) en `version` del manifest y etiquetas/releases en GitHub.
- `lib.versionCheck('usuario/repositorio')` (ox_lib) avisa en consola si hay una versión nueva.
- Mantén un `CHANGELOG.md` en tus recursos.

## 26.5 Lista de comprobación antes de publicar un recurso

- [ ] Funciona en un servidor limpio con solo sus dependencias.
- [ ] Sin errores en F8 ni en consola del servidor.
- [ ] `resmon` en reposo ≈ 0.00-0.02 ms.
- [ ] Todos los eventos de red validados en el servidor (tipos, rangos, permisos, distancia, *cooldown*).
- [ ] Sin secretos en archivos de cliente.
- [ ] Limpieza en `onResourceStop` (entidades, blips, NUI, foco).
- [ ] SQL incluido (`sql/install.sql`) e índices creados.
- [ ] README con instalación, dependencias, configuración y capturas.
- [ ] Licencia (si es *open source*: MIT, GPL-3.0, LGPL-3.0…).

---

# 27. Tutorial completo: recurso "tienda" de principio a fin

Vamos a construir una tienda **standalone** con ox_lib + oxmysql que demuestra todo lo anterior: config, blips, puntos, menú, callback seguro, base de datos y logs.

## 27.1 Estructura

```
lx_tienda/
├── fxmanifest.lua
├── config.lua
├── client/main.lua
├── server/main.lua
├── locales/es.json
└── sql/install.sql
```

## 27.2 `fxmanifest.lua`

```lua
fx_version 'cerulean'
game 'gta5'

name 'lx_tienda'
author 'TuNombre'
description 'Tienda de ejemplo (ox_lib + oxmysql)'
version '1.0.0'

shared_scripts {
    '@ox_lib/init.lua',
    'config.lua',
}
client_script 'client/main.lua'
server_scripts {
    '@oxmysql/lib/MySQL.lua',
    'server/main.lua',
}
files { 'locales/*.json' }

dependencies { 'ox_lib', 'oxmysql', '/onesync' }
```

## 27.3 `config.lua`

```lua
Config = {}

Config.Tiendas = {
    { id = 'grove', nombre = '24/7 Grove Street', coords = vec3(-47.52, -1757.51, 29.42) },
    { id = 'vinewood', nombre = '24/7 Vinewood', coords = vec3(373.87, 325.89, 103.57) },
}

-- El servidor usa ESTOS precios, nunca los que envíe el cliente
Config.Productos = {
    agua = { label = 'Agua', precio = 5, icono = 'bottle-water' },
    pan  = { label = 'Pan',  precio = 3, icono = 'bread-slice' },
}

Config.DistanciaInteraccion = 2.0
```

## 27.4 `locales/es.json`

```json
{
  "abrir": "[E] Abrir %s",
  "comprar": "Comprar %s ($%s)",
  "cantidad": "Cantidad",
  "compra_ok": "Has comprado %sx %s por $%s",
  "sin_dinero": "No tienes suficiente dinero",
  "lejos": "Estás demasiado lejos de la tienda"
}
```

## 27.5 `sql/install.sql`

```sql
CREATE TABLE IF NOT EXISTS `lx_tienda_saldos` (
  `license` VARCHAR(60) NOT NULL,
  `dinero` INT NOT NULL DEFAULT 100,
  PRIMARY KEY (`license`)
);

CREATE TABLE IF NOT EXISTS `lx_tienda_compras` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `license` VARCHAR(60) NOT NULL,
  `producto` VARCHAR(50) NOT NULL,
  `cantidad` INT NOT NULL,
  `total` INT NOT NULL,
  `fecha` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_license` (`license`)
);
```

## 27.6 `client/main.lua`

```lua
lib.locale()

-- Blips
CreateThread(function()
    for _, t in ipairs(Config.Tiendas) do
        local blip = AddBlipForCoord(t.coords.x, t.coords.y, t.coords.z)
        SetBlipSprite(blip, 52)
        SetBlipColour(blip, 2)
        SetBlipScale(blip, 0.8)
        SetBlipAsShortRange(blip, true)
        BeginTextCommandSetBlipName('STRING')
        AddTextComponentSubstringPlayerName(t.nombre)
        EndTextCommandSetBlipName(blip)
    end
end)

local function comprar(tiendaId, productoId)
    local p = Config.Productos[productoId]
    local input = lib.inputDialog(p.label, {
        { type = 'number', label = locale('cantidad'), default = 1, min = 1, max = 20, required = true },
    })
    if not input then return end

    local ok, msg = lib.callback.await('lx_tienda:comprar', false, tiendaId, productoId, input[1])
    lib.notify({ description = msg, type = ok and 'success' or 'error' })
end

local function abrirTienda(tienda)
    local opciones = {}
    for id, p in pairs(Config.Productos) do
        opciones[#opciones + 1] = {
            title = locale('comprar', p.label, p.precio),
            icon = p.icono,
            onSelect = function() comprar(tienda.id, id) end,
        }
    end
    lib.registerContext({ id = 'lx_tienda_menu', title = tienda.nombre, options = opciones })
    lib.showContext('lx_tienda_menu')
end

-- Puntos de interacción (sin bucles Wait(0) permanentes)
for _, tienda in ipairs(Config.Tiendas) do
    local punto = lib.points.new({ coords = tienda.coords, distance = Config.DistanciaInteraccion })

    function punto:onEnter() lib.showTextUI(locale('abrir', tienda.nombre)) end
    function punto:onExit() lib.hideTextUI() end
    function punto:nearby()
        if IsControlJustReleased(0, 38) then abrirTienda(tienda) end
    end
end

AddEventHandler('onResourceStop', function(res)
    if res == GetCurrentResourceName() then lib.hideTextUI() end
end)
```

## 27.7 `server/main.lua`

```lua
lib.locale()

local Cooldown = {}
local Tiendas = {}
for _, t in ipairs(Config.Tiendas) do Tiendas[t.id] = t end

local function getLicense(src)
    return GetPlayerIdentifierByType(src, 'license')
end

local function getSaldo(license)
    local dinero = MySQL.scalar.await('SELECT dinero FROM lx_tienda_saldos WHERE license = ?', { license })
    if not dinero then
        MySQL.insert.await('INSERT INTO lx_tienda_saldos (license) VALUES (?)', { license })
        return 100
    end
    return dinero
end

lib.callback.register('lx_tienda:comprar', function(source, tiendaId, productoId, cantidad)
    local src = source

    -- 1. Tipos
    if type(tiendaId) ~= 'string' or type(productoId) ~= 'string' or type(cantidad) ~= 'number' then
        return false, 'Petición inválida'
    end
    cantidad = math.floor(cantidad)
    if cantidad < 1 or cantidad > 20 then return false, 'Cantidad inválida' end

    -- 2. Existen en la config del servidor
    local tienda, producto = Tiendas[tiendaId], Config.Productos[productoId]
    if not tienda or not producto then return false, 'Producto inválido' end

    -- 3. Cooldown
    local ahora = GetGameTimer()
    if Cooldown[src] and ahora - Cooldown[src] < 1000 then return false, 'Espera un momento' end
    Cooldown[src] = ahora

    -- 4. Distancia real (OneSync)
    local coords = GetEntityCoords(GetPlayerPed(src))
    if #(coords - tienda.coords) > Config.DistanciaInteraccion + 3.0 then
        print(('^3[lx_tienda] %s (%s) intentó comprar lejos de la tienda^7'):format(GetPlayerName(src), src))
        return false, locale('lejos')
    end

    -- 5. Dinero y compra (transacción atómica)
    local license = getLicense(src)
    local total = producto.precio * cantidad
    if getSaldo(license) < total then return false, locale('sin_dinero') end

    local ok = MySQL.transaction.await({
        { query = 'UPDATE lx_tienda_saldos SET dinero = dinero - ? WHERE license = ? AND dinero >= ?', values = { total, license, total } },
        { query = 'INSERT INTO lx_tienda_compras (license, producto, cantidad, total) VALUES (?, ?, ?, ?)', values = { license, productoId, cantidad, total } },
    })
    if not ok then return false, 'Error al procesar la compra' end

    -- Aquí darías el ítem con tu inventario, p. ej.:
    -- exports.ox_inventory:AddItem(src, productoId, cantidad)

    return true, locale('compra_ok', cantidad, producto.label, total)
end)

AddEventHandler('playerDropped', function() Cooldown[source] = nil end)

lib.versionCheck('tuusuario/lx_tienda')
```

## 27.8 Instalación

1. Copia `lx_tienda` en `resources/[scripts]/`.
2. Importa `sql/install.sql` en tu base de datos.
3. En `server.cfg`, **después** de `oxmysql` y `ox_lib`: `ensure lx_tienda`.
4. Entra al juego, ve al blip de la tienda y pulsa **E**.

---

# 28. Chuleta rápida (*cheat sheet*)

## 28.1 Lua cliente

```lua
local ped = PlayerPedId()
local coords = GetEntityCoords(ped)
local veh = GetVehiclePedIsIn(ped, false)
local myId = GetPlayerServerId(PlayerId())
TriggerServerEvent('x:y', data)
RegisterNetEvent('x:z', function(data) end)
RegisterCommand('cmd', function(_, args) end, false)
RegisterKeyMapping('cmd', 'Descripción', 'keyboard', 'F5')
SetNuiFocus(true, true); SendNUIMessage({ action = 'open' })
RegisterNUICallback('close', function(data, cb) SetNuiFocus(false, false); cb('ok') end)
LocalPlayer.state:set('clave', valor, true)
```

## 28.2 Lua servidor

```lua
RegisterNetEvent('x:y', function(data) local src = source end)
TriggerClientEvent('x:z', src, data)         -- -1 = todos
local license = GetPlayerIdentifierByType(src, 'license')
local ped = GetPlayerPed(src)
local coords = GetEntityCoords(ped)
DropPlayer(src, 'Motivo')
IsPlayerAceAllowed(src, 'permiso')
Player(src).state:set('clave', valor, true)
GlobalState.clave = valor
SetPlayerRoutingBucket(src, 1)
local veh = CreateVehicleServerSetter(`adder`, 'automobile', x, y, z, h)
MySQL.query.await('SELECT * FROM t WHERE a = ?', { a })
```

## 28.3 Consola del servidor

```
refresh            ensure <res>        stop <res>        restart <res>
status             clientkick <id> <r> say <msg>         quit [motivo]
add_ace ...        add_principal ...   test_ace ...      list_aces
exec archivo.cfg   profiler record 500 svgui
```

## 28.4 F8 cliente

```
connect <ip>   disconnect   quit   cl_drawfps true   cl_drawperf true
resmon 1       netgraph true        strdbg            nui_devtools
profiler record 500 / profiler view
```

## 28.5 Puertos

```
30120 TCP+UDP  → juego
40120 TCP      → txAdmin
3306  TCP      → MariaDB (NUNCA público)
```

---

# 29. Preguntas frecuentes (FAQ)

**¿Necesito `lua54 'yes'` en 2026?**
No. Desde julio de 2025 todo Lua es 5.4. La línea es inofensiva.

**¿Qué artefacto uso?**
El **recommended** (35245 a 20 de octubre de 2026). Nada por debajo de 35245 permite conexiones desde el 15 de octubre de 2026.

**¿Qué game build pongo?**
La última: `sv_enforceGameBuild 3889` (*The Kortz Center Heist*), salvo incompatibilidades.

**¿ESX, QBCore o Qbox?**
Para un servidor nuevo: **Qbox** (moderno, ox) o **ESX Legacy 1.16** (muy activo). QBCore se mueve poco. Ver 17.

**¿ox_lib de Overextended o de CommunityOx?**
De **Overextended** (`github.com/overextended`). CommunityOx está archivado desde abril de 2026.

**¿Puedo vender dinero del juego por dinero real?**
**No.** Está prohibido por el PLA (§3.1). Lo mismo con cajas de botín, apuestas, cripto/NFT y publicidad de terceros. Usa Tebex para lo que sí está permitido.

**¿Cómo pongo mi servidor privado?**
`sv_master1 ""` (desactiva el botón de conectar, no lo borra de la lista) o una allowlist (txAdmin o `playerConnecting`). Para desarrollo local: `sv_lan true`.

**Mi servidor no aparece en la lista.**
Revisa la clave (`sv_licenseKey`), los puertos 30120 TCP/UDP, que el artefacto tenga soporte y, desde el 21/10/2026, los metadatos del servidor en Portal.

**¿Por qué mi script consume tanto en `resmon`?**
Casi siempre un `Wait(0)` permanente o natives caros por frame. Ver 20.2.

**¿Cómo protejo mis eventos?**
Validando todo en el servidor (19.3). Los tokens no son protección real.

**¿Dónde están los logs del cliente?**
`%localappdata%\FiveM\FiveM.app\logs\`.

**¿Mis recursos C# con `mono_rt2` ya no cargan?**
La prueba de Mono v2 caducó el 30/06/2026. Quita `mono_rt2` y compila para el runtime clásico (`CitizenFX.Core`).

**Algunos jugadores tienen un `license:` nuevo.**
Es por la actualización de seguridad de cuentas del 24/06/2026. Pueden volver a elegir su identidad por defecto hasta el 24/06/2027; ten un proceso para migrar personajes.

---

# 30. Glosario

| Término | Significado |
|---|---|
| **ACE** | *Access Control Entry*: regla de permisos (`add_ace`). |
| **Artefacto** | Build compilada de FXServer. |
| **Bucket** | *Routing bucket*: dimensión separada de sincronización. |
| **Callback** | Petición con respuesta entre cliente y servidor (implementada con eventos). |
| **CfxLua** | Lua 5.4 modificado de FiveM. |
| **Culling** | No sincronizar entidades lejanas. |
| **Deferrals** | Mecanismo para retener/validar una conexión en `playerConnecting`. |
| **DUI** | Página web renderizada como textura en el mundo. |
| **Entity lockdown** | Restringir la creación de entidades por clientes. |
| **Escrow** | Cifrado de recursos de pago. |
| **Export** | Función de un recurso llamable desde otro del mismo lado. |
| **FXServer** | Servidor dedicado de FiveM. |
| **Game build** | Versión de GTA V/DLC que usa el servidor. |
| **Handle** | Identificador local de una entidad. |
| **Hash / Joaat** | Número que identifica un string (modelos, armas). |
| **IPL** | Conjunto de objetos del mapa que se carga/descarga. |
| **KVP** | Almacén clave-valor persistente. |
| **Latent event** | Evento enviado poco a poco a una velocidad dada. |
| **MLO** | Interior personalizado. |
| **Native** | Función del motor del juego o de FiveM. |
| **NetID** | ID de red de una entidad, común a todos. |
| **NUI** | Interfaces HTML dentro del juego. |
| **OneSync** | Sincronización con el servidor como autoridad. |
| **Owner** | Cliente que simula una entidad. |
| **Ped** | Personaje (jugador o NPC). |
| **PLA** | *Platform License Agreement*: licencia de la plataforma. |
| **Pool** | Reserva de memoria para un tipo de objeto del juego. |
| **Portal** | portal.cfx.re: claves, assets, metadatos del servidor. |
| **Principal** | "Quién" en el sistema ACE. |
| **Pure mode** | Bloqueo de archivos modificados en el cliente (`sv_pureLevel`). |
| **Recipe** | Plantilla de despliegue de txAdmin. |
| **Recurso** | Paquete de código/assets con `fxmanifest.lua`. |
| **resmon** | Monitor de recursos del cliente. |
| **Scope** | Conjunto de entidades/jugadores relevantes para un cliente. |
| **Source** | ID de servidor del jugador que disparó un evento. |
| **State bag** | Pares clave-valor sincronizados. |
| **Streaming** | Transmisión de assets (`stream/`) a los clientes. |
| **Tick** | Iteración del bucle principal. |
| **txAdmin** | Panel de administración integrado. |
| **ymap / ytyp / ytd / yft / ydr** | Formatos de archivo de RAGE (mapa, arquetipos, texturas, fragmentos, drawables). |

---

# 31. Enlaces oficiales y recursos

## Oficiales Cfx.re

| Recurso | URL |
|---|---|
| Documentación | https://docs.fivem.net/docs/ |
| Referencia de natives | https://docs.fivem.net/natives/ |
| Descarga del servidor (Legacy) | https://docs.fivem.net/docs/server-download/?platform=legacy |
| Comandos y convars | https://docs.fivem.net/docs/server-manual/server-commands/ |
| Manifest | https://docs.fivem.net/docs/scripting-reference/resource-manifest/ |
| Eventos | https://docs.fivem.net/docs/scripting-reference/events/list/ |
| State bags | https://docs.fivem.net/docs/scripting-manual/networking/state-bags/ |
| Data files | https://docs.fivem.net/docs/game-references/data-files/ |
| Controles | https://docs.fivem.net/docs/game-references/controls/ |
| Blips | https://docs.fivem.net/docs/game-references/blips/ |
| Marcadores | https://docs.fivem.net/docs/game-references/markers/ |
| Proxy | https://docs.fivem.net/docs/server-manual/proxy-setup/ |
| EOS / EOL | https://docs.fivem.net/docs/server-manual/end-of-support-end-of-life/ |
| Asset Escrow | https://docs.fivem.net/docs/server-manual/asset-escrow/ |
| Tebex | https://docs.fivem.net/docs/server-manual/setting-up-a-tebex-store/ |
| Comandos de consola del cliente | https://docs.fivem.net/docs/client-manual/console-commands/ |
| Portal | https://portal.cfx.re |
| Foro | https://forum.cfx.re |
| Licencia (PLA) | https://fivem.net/terms |
| Código fuente | https://github.com/citizenfx/fivem |
| Recursos base | https://github.com/citizenfx/cfx-server-data |
| txAdmin | https://github.com/citizenfx/txAdmin |

## Ecosistema

| Recurso | URL |
|---|---|
| Overextended (ox_lib, oxmysql, ox_inventory, ox_target…) | https://github.com/overextended · https://overextended.dev |
| ESX Legacy | https://github.com/esx-framework/esx_core · https://docs.esx-framework.org |
| QBCore | https://github.com/qbcore-framework · https://docs.qbcore.org |
| Qbox | https://github.com/Qbox-project · https://docs.qbox.re |
| pma-voice | https://github.com/AvarianKnight/pma-voice |
| Addon LuaLS para FiveM | https://github.com/overextended/fivem-lls-addon |
| Tipos TypeScript | `@citizenfx/client`, `@citizenfx/server` (npm) |
| Boilerplate React | https://github.com/project-error/fivem-react-boilerplate-lua |
| Boilerplate TypeScript | https://github.com/overextended/fivem-typescript-boilerplate |
| CodeWalker | https://github.com/dexyfex/CodeWalker |
| Sollumz (Blender) | https://github.com/Sollumz/Sollumz |
| MariaDB | https://mariadb.org/download |
| Adaptive Cards (deferrals) | https://adaptivecards.io/designer/ |

---

# 32. Historial de este documento

| Fecha | Cambio |
|---|---|
| 2026-10-20 | Primera versión completa, centrada exclusivamente en FiveM Legacy (FXServer). Datos verificados a esta fecha: artefacto *recommended* 35245 / *latest* 37579, build 3889, txAdmin 8.1.1, ESX 1.16.4, Qbox 1.24.0, ox_lib 3.40.x, oxmysql 2.14.x, ox_inventory 2.48.x, MariaDB 11.4/11.8 LTS. |

> **Cómo mantener esta guía al día:** revisa cada mes las *release notes* del foro (categoría *Cfx.re Announcements → Release Notes*), la página de descarga de artefactos, los *changelogs* de txAdmin y de tu framework, y actualiza las versiones de la tabla anterior.

