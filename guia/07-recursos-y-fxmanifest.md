[← 06-permisos-ace](06-permisos-ace.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [08-scripting-fundamentos →](08-scripting-fundamentos.md)

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


## Ver también (documentación offline)

- [Oficial: scripting-reference/resource-manifest](../docs-oficiales/scripting-reference/resource-manifest/README.md)
- [Oficial: scripting-manual/introduction/introduction-to-resources](../docs-oficiales/scripting-manual/introduction/introduction-to-resources.md)

---

[← 06-permisos-ace](06-permisos-ace.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [08-scripting-fundamentos →](08-scripting-fundamentos.md)
