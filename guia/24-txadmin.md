[← 23-monetizacion-y-legal](23-monetizacion-y-legal.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [25-hosting-y-despliegue →](25-hosting-y-despliegue.md)

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


## Ver también (documentación offline)

- [Oficial: resources/txAdmin](../docs-oficiales/resources/txAdmin/README.md)
- [Oficial: resources/txAdmin/permissions](../docs-oficiales/resources/txAdmin/permissions.md)
- [Terceros: txadmin](../docs-terceros/txadmin/README.md)

---

[← 23-monetizacion-y-legal](23-monetizacion-y-legal.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [25-hosting-y-despliegue →](25-hosting-y-despliegue.md)
