[← 07-recursos-y-fxmanifest](07-recursos-y-fxmanifest.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [09-lua →](09-lua.md)

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
- Natives tipados (cliente y servidor): `GetConvarInt(nombre, defecto)`, `GetConvarBool(nombre, defecto)` y `GetConvarFloat(nombre, defecto)` (este último con la imprecisión normal de los decimales).
- `AddConvarChangeListener(filtro, function(nombre, reservado) end)` avisa cuando cambia una convar (el filtro admite patrones como `'mi_recurso:*'`).

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

Variantes asíncronas (cliente y servidor): `SetResourceKvpNoSync`, `SetResourceKvpIntNoSync`, `SetResourceKvpFloatNoSync` y `DeleteResourceKvpNoSync`. No esperan a que se escriba en disco: son mucho más rápidas para operaciones en lote, pero si el sistema se cae se pueden perder las últimas escrituras. En el **servidor**, `FlushResourceKvp()` fuerza la escritura (este native solo existe en el servidor).

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
| `os.time()`, `os.date()`, `os.clock()` | **Solo servidor** | En el cliente la librería `os` **no existe** (ver 9.9). En el cliente usa `GetGameTimer()` (ms), `GetCloudTimeAsInt()` (tiempo Unix) o `GetLocalTime()`/`GetUtcTime()` (fecha y hora). |
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
    deferrals.defer()                 -- empezar a retener la conexión
    Wait(0)                           -- OBLIGATORIO: al menos un tick tras defer()
    deferrals.update(('Hola %s, comprobando tu cuenta...'):format(name))

    local license = GetPlayerIdentifierByType(src, 'license')
    local baneado = license and EstaBaneado(license)   -- tu función (p. ej. consulta a la BD)

    Wait(0)                           -- OBLIGATORIO: al menos un tick tras update() antes de done()
    if not license then
        return deferrals.done('No se ha encontrado tu licencia de Rockstar.')
    end
    if baneado then
        return deferrals.done('Estás baneado. Apela en discord.gg/xxxx')
    end
    deferrals.done()                  -- sin argumento = permitir
end)
```

- `deferrals.defer()` – empezar a retener. **Regla oficial:** espera al menos un tick (`Wait(0)`) tras `defer()` antes de `update`/`presentCard`/`done`, y al menos un tick tras cualquiera de ellos antes de `done`.
- `deferrals.update(texto)` – mensaje de progreso.
- `deferrals.presentCard(card, callback)` – muestra una **Adaptive Card** (formularios, botones). `card` puede ser una tabla o un string JSON; `callback(data, rawData)` se llama con cada `Action.Submit`. Diseñador: https://adaptivecards.io/designer/
- `deferrals.handover(tabla)` – *handover* dinámico. Según la documentación oficial sirve para indicar los **endpoints** de conexión de ese jugador (`deferrals.handover({ endpoints = { '1.2.3.4' } })`). En el código del cliente, ese bloque de datos se entrega también a la pantalla de carga como `window.nuiHandoverData`.
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
-- dentro de playerConnecting, después de deferrals.defer() y Wait(0):
deferrals.presentCard(card, function(data, rawData)   -- el callback llega en un tick posterior (clic del jugador)
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


## Ver también (documentación offline)

- [Oficial: scripting-manual/working-with-events](../docs-oficiales/scripting-manual/working-with-events/README.md)
- [Oficial: scripting-reference/events](../docs-oficiales/scripting-reference/events/README.md)
- [Oficial: scripting-reference/events/server-events](../docs-oficiales/scripting-reference/events/server-events/README.md)
- [Oficial: scripting-reference/events/client-events](../docs-oficiales/scripting-reference/events/client-events/README.md)
- [Oficial: cookbook/2020/01/06/using-the-new-console-key-bindings](../docs-oficiales/cookbook/2020/01/06/using-the-new-console-key-bindings.md)
- [Oficial: cookbook/2019/06/29/adaptive-cards-in-deferrals](../docs-oficiales/cookbook/2019/06/29/adaptive-cards-in-deferrals.md)

---

[← 07-recursos-y-fxmanifest](07-recursos-y-fxmanifest.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [09-lua →](09-lua.md)
