[← 27-tutorial-recurso-tienda](27-tutorial-recurso-tienda.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [29-faq →](29-faq.md)

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

[← 27-tutorial-recurso-tienda](27-tutorial-recurso-tienda.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [29-faq →](29-faq.md)
