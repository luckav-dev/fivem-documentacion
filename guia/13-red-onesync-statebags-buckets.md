[← 12-natives-guia-practica](12-natives-guia-practica.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [14-nui →](14-nui.md)

# 13. Red, OneSync, State Bags y Routing Buckets

## 13.1 Cómo funciona la sincronización con OneSync

- El servidor mantiene un **árbol de sincronización** (*sync tree*) de cada entidad en red: posición, salud, modelo, estado de puertas, etc.
- Cada entidad tiene un **owner** (un cliente) que la simula y envía su estado al servidor; el servidor lo reenvía a los clientes que la tienen **en su ámbito** (*scope*), que depende principalmente de la distancia.
- Si el owner se aleja o se desconecta, la entidad **migra** a otro cliente cercano (`onesync_forceMigration`).
- **Por defecto el servidor borra las entidades que dejan de ser relevantes para cualquier jugador** (modo *orphan* `DeleteWhenNotRelevant`). Para que una entidad de servidor persista aunque no haya nadie cerca (por ejemplo, vehículos aparcados persistentes) usa `SetEntityOrphanMode(entidad, 2)` (ver abajo).
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
-- (servidor) Qué hace el servidor con una entidad cuando ya no tiene a su owner original
-- 0 = DeleteWhenNotRelevant (por defecto): se borra cuando no es relevante para ningún jugador
-- 1 = DeleteOnOwnerDisconnect: se borra cuando se desconecta su owner original
-- 2 = KeepEntity: el servidor nunca la borra en sus comprobaciones de relevancia
SetEntityOrphanMode(veh, 2)
```

Según la documentación oficial del native:

- Con `KeepEntity` (2) solo se garantiza que **el servidor** no la borre; un cliente **sí puede** borrarla con `DeleteEntity`.
- Usado en un tren, se aplica también a todos sus vagones.

> **`SetEntityDistanceCullingRadius`** (cambiar el radio de sincronización de una entidad) existe, pero la propia documentación de Cfx.re lo marca: *"Culling natives are deprecated and have known, unfixable issues"*. **No lo uses** en recursos nuevos.

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

Detalles oficiales del handler (documentación del native `ADD_STATE_BAG_CHANGE_HANDLER`):

- Firma: `function(bagName, key, value, reserved, replicated)`; `reserved` no se usa.
- Cuando se ejecuta el handler, **el bag todavía contiene el valor antiguo**: `value` es el nuevo y puedes leer el anterior con `Entity(ent).state[key]` o `GetStateBagValue(bagName, key)`.
- El handler **no puede rechazar** el cambio. Para impedir escrituras de clientes usa `sv_stateBagStrictMode` o valida y corrige desde el servidor.
- En el **servidor** `GetPlayerFromStateBagName` devuelve el `source` del jugador; en el **cliente** devuelve el *player handle* (índice local).

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


## Ver también (documentación offline)

- [Oficial: scripting-manual/networking](../docs-oficiales/scripting-manual/networking/README.md)
- [Oficial: scripting-manual/networking/state-bags](../docs-oficiales/scripting-manual/networking/state-bags.md)
- [Oficial: scripting-manual/networking/ids](../docs-oficiales/scripting-manual/networking/ids.md)
- [Oficial: scripting-reference/onesync](../docs-oficiales/scripting-reference/onesync/README.md)
- [Oficial: cookbook/2020/11/27/routing-buckets-split-game-state](../docs-oficiales/cookbook/2020/11/27/routing-buckets-split-game-state.md)
- [Oficial: cookbook/2019/08/19/onesync-intercepting-game-events-such-as-explosions](../docs-oficiales/cookbook/2019/08/19/onesync-intercepting-game-events-such-as-explosions.md)
- [Oficial: game-references/net-game-events](../docs-oficiales/game-references/net-game-events.md)

---

[← 12-natives-guia-practica](12-natives-guia-practica.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [14-nui →](14-nui.md)
