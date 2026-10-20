[← 01-introduccion](01-introduccion.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [03-instalacion-servidor →](03-instalacion-servidor.md)

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

El **game build** es la versión de GTA V (y por tanto el DLC más reciente) que usará el cliente al entrar al servidor. Se fija con `sv_enforceGameBuild`. Si no lo fijas, se usa la build por defecto **1604** (*Arena War*, 2018), y no tendrás vehículos/ropa/mapas de DLC recientes. Ver la tabla completa en la [sección 5.4](05-comandos-y-convars.md#54-game-builds-sv_enforcegamebuild).

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


## Ver también (documentación offline)

- [Oficial: scripting-manual/introduction/introduction-to-resources](../docs-oficiales/scripting-manual/introduction/introduction-to-resources.md)
- [Oficial: scripting-manual/introduction/fact-sheet](../docs-oficiales/scripting-manual/introduction/fact-sheet.md)

---

[← 01-introduccion](01-introduccion.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [03-instalacion-servidor →](03-instalacion-servidor.md)
