[← 11-csharp](11-csharp.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [13-red-onesync-statebags-buckets →](13-red-onesync-statebags-buckets.md)

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


## Ver también (documentación offline)

- [natives](../natives/README.md)
- [Oficial: scripting-manual/introduction/about-native-functions](../docs-oficiales/scripting-manual/introduction/about-native-functions.md)
- [Oficial: game-references/controls](../docs-oficiales/game-references/controls.md)
- [Oficial: game-references/blips](../docs-oficiales/game-references/blips.md)
- [Oficial: game-references/markers](../docs-oficiales/game-references/markers.md)
- [Oficial: game-references/text-formatting](../docs-oficiales/game-references/text-formatting.md)
- [Oficial: game-references/ped-models](../docs-oficiales/game-references/ped-models.md)
- [Oficial: game-references/vehicle-references/vehicle-models](../docs-oficiales/game-references/vehicle-references/vehicle-models.md)
- [Oficial: game-references/weapon-models](../docs-oficiales/game-references/weapon-models.md)

---

[← 11-csharp](11-csharp.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [13-red-onesync-statebags-buckets →](13-red-onesync-statebags-buckets.md)
