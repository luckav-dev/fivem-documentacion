[Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [02-conceptos-fundamentales →](02-conceptos-fundamentales.md)

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


## Ver también (documentación offline)

- [Oficial: getting-started](../docs-oficiales/getting-started/README.md)
- [Oficial: client-manual/installing-fivem](../docs-oficiales/client-manual/installing-fivem.md)
- [Oficial: client-manual/where-to-buy-gtav](../docs-oficiales/client-manual/where-to-buy-gtav.md)

---

[Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [02-conceptos-fundamentales →](02-conceptos-fundamentales.md)
