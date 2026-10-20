[← 16-base-de-datos](16-base-de-datos.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [18-voz →](18-voz.md)

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

## 17.6 Crear tu propio framework

Si no quieres depender de ESX, QBCore o Qbox, puedes hacer tu propio núcleo. Esta sección explica **qué debe hacer un framework**, el **contrato de comportamiento** que deberían poder dar por hecho el resto de recursos y un **núcleo mínimo completo** (`mi_core`) que funciona tal cual: sus natives y funciones están comprobados contra la base de datos oficial y el runtime de FiveM.

### 17.6.1 Responsabilidades de un framework

| Área | Qué resuelve |
|---|---|
| **Ciclo de vida del jugador** | Conexión (validación/bans), carga de datos, jugador "listo", guardado y desconexión. |
| **Identidad** | Elegir el identificador persistente (`license:`) y, si hay varios personajes, el id de personaje. |
| **Persistencia** | Base de datos, caché en memoria y guardado periódico y al salir. |
| **Economía** | Cuentas (efectivo, banco…) con el servidor como **única autoridad**. |
| **Trabajos y grupos** | Trabajo, rango y permisos (integrados con ACE). |
| **API pública** | *Exports* y eventos estables y documentados para otros recursos. |
| **Sincronización con el cliente** | Datos privados solo a su dueño; datos públicos mediante state bags. |
| **Utilidades** | Callbacks, ítems usables, notificaciones, comandos, locales. |

### 17.6.2 Contrato de comportamiento (lo que otros recursos esperan)

Si publicas un framework, **documenta y cumple** estas garantías:

1. **El servidor es la única fuente de verdad.** Ningún dato de dinero, trabajo o inventario se acepta desde el cliente.
2. **Evento de jugador cargado, una sola vez por sesión**: en servidor (local) `mi_core:playerLoaded(src, datos)` y en el cliente `mi_core:client:playerLoaded(datos)`. Ningún otro recurso debería pedir datos antes de ese evento.
3. **Evento de salida**: `mi_core:playerDropped(src, datos)` (servidor) **después** de guardar.
4. **Cada cambio emite un evento**: `mi_core:moneyChanged(src, cuenta, nuevoValor, motivo)`, `mi_core:jobChanged(src, trabajo, anterior)`.
5. **Las funciones que cambian datos devuelven `true`/`false`** (y nunca dejan valores negativos ni no numéricos).
6. **Los datos se guardan** al desconectarse, periódicamente, al parar el recurso y cuando txAdmin anuncia reinicio o apagado.
7. **API por exports**, no por variables globales. Los exports que modifican datos solo existen en el **servidor** (los clientes no pueden llamar a exports del servidor).
8. **Auditoría**: registra qué recurso cambió el dinero (`GetInvokingResource()`).
9. **Eventos de red validados** (tipos, rangos, permisos, frecuencia) y con espacio de nombres (`mi_core:server:*`, `mi_core:client:*`).
10. **Compatibilidad**: si cambias la API, mantén *aliases* o versión mayor (SemVer) y avisa en el *changelog*.

### 17.6.3 Flujo de vida del jugador

```
playerConnecting (deferrals: license, ban)      ← source TEMPORAL
        │
        ▼
cliente arranca → NetworkIsPlayerActive(PlayerId())
        │  TriggerServerEvent('mi_core:server:ready')
        ▼
servidor: carga de BD → objeto en memoria → state bags públicos
        │  TriggerEvent('mi_core:playerLoaded', src, datos)              (servidor)
        │  TriggerClientEvent('mi_core:client:playerLoaded', src, datos)  (solo su cliente)
        ▼
juego: cambios vía exports (servidor) → evento + sincronización
        │
        ▼
playerDropped → guardar → TriggerEvent('mi_core:playerDropped', src, datos) → liberar memoria
```

> `playerConnecting` usa un id **temporal**: no cargues aún el personaje ahí. Cárgalo cuando el cliente avise de que está listo (o en `playerJoining`, que recibe el id definitivo en `source` y el temporal como argumento).

### 17.6.4 Estructura

```
mi_core/
├── fxmanifest.lua
├── config.lua
├── sql/install.sql
├── server/
│   ├── player.lua      ← clase Player (memoria + BD)
│   ├── main.lua        ← ciclo de vida, guardado, eventos
│   └── api.lua         ← exports públicos
└── client/
    └── main.lua        ← PlayerData local, eventos, export de lectura
```

### 17.6.5 `fxmanifest.lua`

```lua
fx_version 'cerulean'
game 'gta5'

name 'mi_core'
description 'Framework propio mínimo'
version '1.0.0'

shared_script 'config.lua'
server_scripts {
    '@oxmysql/lib/MySQL.lua',
    'server/player.lua',
    'server/main.lua',
    'server/api.lua',
}
client_script 'client/main.lua'

dependencies { 'oxmysql', '/onesync' }
```

### 17.6.6 `config.lua`

```lua
Config = {}
Config.Cuentas = { cash = 500, bank = 2500 }       -- cuentas y saldo inicial
Config.TrabajoPorDefecto = { name = 'desempleado', grade = 0 }
Config.Trabajos = {
    desempleado = { label = 'Desempleado', grados = { [0] = { label = 'Ciudadano', sueldo = 50 } } },
    policia = { label = 'Policía', grados = {
        [0] = { label = 'Cadete', sueldo = 300 },
        [1] = { label = 'Agente', sueldo = 450 },
        [2] = { label = 'Sargento', sueldo = 600 },
    } },
}
Config.AutoguardadoMinutos = 5
```

### 17.6.7 `sql/install.sql`

```sql
CREATE TABLE IF NOT EXISTS `mi_core_jugadores` (
  `license` VARCHAR(60) NOT NULL,
  `nombre` VARCHAR(100) NOT NULL,
  `cuentas` LONGTEXT NOT NULL,
  `trabajo` VARCHAR(50) NOT NULL DEFAULT 'desempleado',
  `grado` INT NOT NULL DEFAULT 0,
  `grupo` VARCHAR(50) NOT NULL DEFAULT 'user',
  `metadata` LONGTEXT NOT NULL,
  `ultima_conexion` TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`license`)
) DEFAULT CHARSET=utf8mb4;

CREATE TABLE IF NOT EXISTS `mi_core_bans` (
  `license` VARCHAR(60) NOT NULL,
  `motivo` VARCHAR(255) NOT NULL,
  `fecha` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`license`)
) DEFAULT CHARSET=utf8mb4;
```

### 17.6.8 `server/player.lua` (clase Player)

```lua
-- server
Jugadores = {}            -- [source] = objeto Player (solo este recurso)

local PlayerClass = {}
PlayerClass.__index = PlayerClass

local function copiar(t)
    local r = {}
    for k, v in pairs(t) do r[k] = type(v) == 'table' and copiar(v) or v end
    return r
end

function CrearJugador(src, fila)
    local self = setmetatable({}, PlayerClass)
    self.source = src
    self.license = fila.license
    self.nombre = fila.nombre
    self.cuentas = json.decode(fila.cuentas) or copiar(Config.Cuentas)
    self.trabajo = { name = fila.trabajo, grade = fila.grado }
    self.grupo = fila.grupo
    self.metadata = json.decode(fila.metadata) or {}
    return self
end

-- Datos que se pueden mandar al cliente o a otros recursos (sin métodos)
function PlayerClass:datos()
    return {
        source = self.source, license = self.license, nombre = self.nombre,
        cuentas = copiar(self.cuentas), trabajo = copiar(self.trabajo),
        grupo = self.grupo, metadata = copiar(self.metadata),
    }
end

-- Datos públicos visibles para todos los clientes (state bag replicado)
function PlayerClass:sincronizarPublico()
    Player(self.source).state:set('trabajo', { name = self.trabajo.name, grade = self.trabajo.grade }, true)
end

function PlayerClass:getDinero(cuenta)
    return self.cuentas[cuenta]
end

function PlayerClass:setDinero(cuenta, cantidad, motivo)
    if self.cuentas[cuenta] == nil then return false end
    if type(cantidad) ~= 'number' or cantidad < 0 or cantidad ~= cantidad then return false end -- NaN
    cantidad = math.floor(cantidad)
    self.cuentas[cuenta] = cantidad
    TriggerClientEvent('mi_core:client:moneyChanged', self.source, cuenta, cantidad)
    TriggerEvent('mi_core:moneyChanged', self.source, cuenta, cantidad, motivo or 'sin motivo')
    return true
end

function PlayerClass:addDinero(cuenta, cantidad, motivo)
    if type(cantidad) ~= 'number' or cantidad <= 0 then return false end
    local actual = self.cuentas[cuenta]
    if actual == nil then return false end
    return self:setDinero(cuenta, actual + cantidad, motivo)
end

function PlayerClass:quitarDinero(cuenta, cantidad, motivo)
    if type(cantidad) ~= 'number' or cantidad <= 0 then return false end
    local actual = self.cuentas[cuenta]
    if actual == nil or actual < cantidad then return false end
    return self:setDinero(cuenta, actual - cantidad, motivo)
end

function PlayerClass:setTrabajo(nombre, grado)
    local t = Config.Trabajos[nombre]
    if not t or not t.grados[grado] then return false end
    local anterior = copiar(self.trabajo)
    self.trabajo = { name = nombre, grade = grado }
    self:sincronizarPublico()
    TriggerClientEvent('mi_core:client:jobChanged', self.source, self.trabajo, anterior)
    TriggerEvent('mi_core:jobChanged', self.source, self.trabajo, anterior)
    return true
end

function PlayerClass:setMeta(clave, valor)
    self.metadata[clave] = valor
    TriggerClientEvent('mi_core:client:metaChanged', self.source, clave, valor)
end

function PlayerClass:getMeta(clave)
    return self.metadata[clave]
end

function PlayerClass:guardar()
    MySQL.update.await(
        'UPDATE mi_core_jugadores SET nombre = ?, cuentas = ?, trabajo = ?, grado = ?, grupo = ?, metadata = ? WHERE license = ?',
        { self.nombre, json.encode(self.cuentas), self.trabajo.name, self.trabajo.grade, self.grupo, json.encode(self.metadata), self.license }
    )
end
```

### 17.6.9 `server/main.lua` (ciclo de vida)

```lua
-- server
local function cargarFila(license, nombre)
    local fila = MySQL.single.await('SELECT * FROM mi_core_jugadores WHERE license = ?', { license })
    if fila then return fila end
    MySQL.insert.await(
        'INSERT INTO mi_core_jugadores (license, nombre, cuentas, trabajo, grado, metadata) VALUES (?, ?, ?, ?, ?, ?)',
        { license, nombre, json.encode(Config.Cuentas), Config.TrabajoPorDefecto.name, Config.TrabajoPorDefecto.grade, '{}' }
    )
    return MySQL.single.await('SELECT * FROM mi_core_jugadores WHERE license = ?', { license })
end

-- 1. Conexión: comprobar licencia y bans (source TEMPORAL)
AddEventHandler('playerConnecting', function(name, setKickReason, deferrals)
    local src = source
    deferrals.defer()
    Wait(0)
    deferrals.update('Comprobando tu cuenta...')

    local license = GetPlayerIdentifierByType(src, 'license')
    local ban = license and MySQL.single.await('SELECT motivo FROM mi_core_bans WHERE license = ?', { license })

    Wait(0)
    if not license then return deferrals.done('No se ha encontrado tu licencia de Rockstar.') end
    if ban then return deferrals.done('Estás baneado: ' .. ban.motivo) end
    deferrals.done()
end)

-- 2. El cliente avisa de que está listo → cargar
RegisterNetEvent('mi_core:server:ready', function()
    local src = source
    if Jugadores[src] then return end                         -- una sola carga por sesión

    local license = GetPlayerIdentifierByType(src, 'license')
    if not license then return DropPlayer(src, 'Sin licencia') end

    local fila = cargarFila(license, GetPlayerName(src))
    if not GetPlayerName(src) then return end                 -- se desconectó mientras cargaba

    local jugador = CrearJugador(src, fila)
    Jugadores[src] = jugador
    jugador:sincronizarPublico()

    -- Permisos: el grupo del framework se refleja en ACE
    ExecuteCommand(('add_principal identifier.%s group.%s'):format(license, jugador.grupo))

    local datos = jugador:datos()
    TriggerEvent('mi_core:playerLoaded', src, datos)
    TriggerClientEvent('mi_core:client:playerLoaded', src, datos)
end)

-- 3. Desconexión: guardar y liberar
AddEventHandler('playerDropped', function(reason)
    local src = source
    local jugador = Jugadores[src]
    if not jugador then return end
    jugador:guardar()
    ExecuteCommand(('remove_principal identifier.%s group.%s'):format(jugador.license, jugador.grupo))
    TriggerEvent('mi_core:playerDropped', src, jugador:datos())
    Jugadores[src] = nil
end)

-- 4. Guardado periódico
local function guardarTodos()
    for _, jugador in pairs(Jugadores) do jugador:guardar() end
end

CreateThread(function()
    while true do
        Wait(Config.AutoguardadoMinutos * 60000)
        guardarTodos()
    end
end)

-- 5. Guardar al parar el recurso y antes de reinicios/apagados de txAdmin
AddEventHandler('onResourceStop', function(res)
    if res == GetCurrentResourceName() then guardarTodos() end
end)
AddEventHandler('txAdmin:events:serverShuttingDown', guardarTodos)
AddEventHandler('txAdmin:events:scheduledRestart', function(data)
    if data.secondsRemaining <= 60 then guardarTodos() end
end)
```

`server.cfg` (permisos que necesita el núcleo para gestionar grupos):

```cfg
add_ace resource.mi_core command.add_principal allow
add_ace resource.mi_core command.remove_principal allow
add_principal group.admin group.user
add_ace group.admin command allow
ensure oxmysql
ensure mi_core
```

### 17.6.10 `server/api.lua` (exports públicos)

```lua
-- server
local function log(accion, src, ...)
    print(('[mi_core] %s src=%s por=%s %s'):format(accion, src, GetInvokingResource() or GetCurrentResourceName(), table.concat({ ... }, ' ')))
end

exports('GetPlayerData', function(src)
    local j = Jugadores[tonumber(src)]
    return j and j:datos() or nil
end)

exports('GetMoney', function(src, cuenta)
    local j = Jugadores[tonumber(src)]
    return j and j:getDinero(cuenta) or nil
end)

exports('AddMoney', function(src, cuenta, cantidad, motivo)
    local j = Jugadores[tonumber(src)]
    if not j then return false end
    local ok = j:addDinero(cuenta, cantidad, motivo)
    if ok then log('AddMoney', src, cuenta, cantidad, motivo or '') end
    return ok
end)

exports('RemoveMoney', function(src, cuenta, cantidad, motivo)
    local j = Jugadores[tonumber(src)]
    if not j then return false end
    local ok = j:quitarDinero(cuenta, cantidad, motivo)
    if ok then log('RemoveMoney', src, cuenta, cantidad, motivo or '') end
    return ok
end)

exports('SetJob', function(src, trabajo, grado)
    local j = Jugadores[tonumber(src)]
    return j and j:setTrabajo(trabajo, tonumber(grado) or 0) or false
end)

exports('HasJob', function(src, trabajo, gradoMinimo)
    local j = Jugadores[tonumber(src)]
    return j ~= nil and j.trabajo.name == trabajo and j.trabajo.grade >= (gradoMinimo or 0)
end)

exports('SetMeta', function(src, clave, valor)
    local j = Jugadores[tonumber(src)]
    if not j then return false end
    j:setMeta(clave, valor)
    return true
end)

exports('GetPlayers', function()
    local lista = {}
    for src, j in pairs(Jugadores) do lista[#lista + 1] = j:datos() end
    return lista
end)

-- Ítems usables (los registra cada recurso)
local Usables = {}
exports('RegisterUsableItem', function(item, cb)
    Usables[item] = cb
end)
exports('UseItem', function(src, item, ...)
    local cb = Usables[item]
    if not cb then return false end
    cb(src, ...)
    return true
end)

-- Comando de administración (restringido por ACE: requiere command.darDinero)
RegisterCommand('darDinero', function(source, args)
    local objetivo, cuenta, cantidad = tonumber(args[1]), args[2], tonumber(args[3])
    local j = objetivo and Jugadores[objetivo]
    if not j or not cantidad then return print('Uso: darDinero <id> <cash|bank> <cantidad>') end
    j:addDinero(cuenta, cantidad, 'comando admin')
end, true)
```

> **Sobre los exports**: los argumentos y valores de retorno se **serializan** entre recursos. Una tabla con metatabla (el objeto `Player`) llegaría al otro recurso **sin sus métodos**. Por eso la API expone **funciones** (`AddMoney`, `SetJob`…) y devuelve **copias de datos** (`GetPlayerData`), no el objeto interno.

### 17.6.11 `client/main.lua`

```lua
-- client
PlayerData = {}
local cargado = false

-- Avisar al servidor cuando la sesión de red está activa (una sola vez)
CreateThread(function()
    while not NetworkIsPlayerActive(PlayerId()) do Wait(250) end
    TriggerServerEvent('mi_core:server:ready')
end)

RegisterNetEvent('mi_core:client:playerLoaded', function(datos)
    PlayerData = datos
    cargado = true
    TriggerEvent('mi_core:client:onLoaded', datos)        -- para otros recursos del cliente
end)

RegisterNetEvent('mi_core:client:moneyChanged', function(cuenta, valor)
    if PlayerData.cuentas then PlayerData.cuentas[cuenta] = valor end
end)

RegisterNetEvent('mi_core:client:jobChanged', function(trabajo, anterior)
    PlayerData.trabajo = trabajo
end)

RegisterNetEvent('mi_core:client:metaChanged', function(clave, valor)
    if PlayerData.metadata then PlayerData.metadata[clave] = valor end
end)

-- API de solo lectura para otros recursos del cliente
exports('GetPlayerData', function() return PlayerData end)
exports('IsLoaded', function() return cargado end)

-- Ver el trabajo de OTROS jugadores (state bag público)
AddStateBagChangeHandler('trabajo', nil, function(bagName, key, value)
    local ply = GetPlayerFromStateBagName(bagName)       -- en el cliente: player handle
    if ply == 0 then return end
    -- p. ej. mostrar placa de policía sobre su cabeza si value.name == 'policia'
end)
```

### 17.6.12 Cómo lo usa otro recurso

```lua
-- server de otro recurso
AddEventHandler('mi_core:playerLoaded', function(src, datos)
    print(('%s ha cargado con %d$ en el banco'):format(datos.nombre, datos.cuentas.bank))
end)

RegisterNetEvent('mi_trabajo:server:cobrar', function()
    local src = source
    if not exports.mi_core:HasJob(src, 'policia') then return end
    exports.mi_core:AddMoney(src, 'bank', 300, 'sueldo policía')
end)

exports.mi_core:RegisterUsableItem('agua', function(src)
    exports.mi_core:SetMeta(src, 'sed', 100)
end)
```

```lua
-- client de otro recurso
AddEventHandler('mi_core:client:onLoaded', function(datos)
    print('Mi trabajo: ' .. datos.trabajo.name)
end)
local datos = exports.mi_core:GetPlayerData()
```

### 17.6.13 Siguientes pasos para un framework completo

- **Multipersonaje**: tabla `personajes` con `license` + `id_personaje`; selección en una NUI antes de `playerLoaded`.
- **Inventario**: integrar `ox_inventory` (bridge propio) o crear uno con slots y peso.
- **Callbacks**: `lib.callback` de ox_lib (17.1) o la implementación propia de 8.3.
- **Sueldos**: un thread que pague a todos cada X minutos según `Config.Trabajos[...].grados[...].sueldo`.
- **Compatibilidad**: con `provide 'es_extended'`/`provide 'qb-core'` y un *bridge* podrías hacer que funcionen scripts de otros frameworks, pero tendrías que implementar **toda** la API que esos scripts usan.
- **Tests**: un servidor de desarrollo con 2-3 clientes, probando desconexiones durante la carga, reinicios del recurso y valores extremos.


## Ver también (documentación offline)

- [Oficial: server-manual/frameworks](../docs-oficiales/server-manual/frameworks.md)
- [Terceros: README](../docs-terceros/README.md)

---

[← 16-base-de-datos](16-base-de-datos.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [18-voz →](18-voz.md)
