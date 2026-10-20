> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qb-core/client-event-reference.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# 🎮 Client Event Reference

*Learn about and how to use common core client events!*

### QBCore:Client:OnPlayerLoaded

-   Handles the player loading in after character selection

> **Consejo:** This event can be used as an event handler to trigger code because it signifies the player has successfully loaded into the server!

```lua
RegisterNetEvent('QBCore:Client:OnPlayerLoaded', function()
    print('Im a client and i just loaded into your server!')
end)
```

### QBCore:Client:OnPlayerUnload

-   Handles the player login out to character selection

> **Consejo:** This event can be used as an event handler to trigger code because it signifies the player has successfully unloaded or logged out of the server!

```lua
RegisterNetEvent('QBCore:Client:OnPlayerUnload', function()
    print('Im a client and i just logged out of your server!')
end)
```

### QBCore:Client:PvpHasToggled

> **Nota:** On player load this event checks is triggered after checking the qb-core config to see if PVP should be enabled or disabled

```lua
RegisterNetEvent('QBCore:Client:PvpHasToggled', function(pvp_state)
    print('PVP mode has been set to '..pvp_state..'!')
end)
```

### QBCore:Command:SpawnVehicle

|   Arguments   |  Type  | Required | Default |
| :-----------: | :----: | :------: | :-----: |
| vehicle model | string |   yes    |  none   |

> **Nota:** Client example

```lua
-- /spawnveh adder

RegisterCommand('spawnveh', function(_, args)
    local vehicle = QBCore.Shared.Trim(args[1])
    TriggerEvent('QBCore:Command:SpawnVehicle', vehicle)
end)
```

> **Nota:** Server example

```lua
-- /spawnveh adder

RegisterCommand('spawnveh', function(source, args)
    local vehicle = QBCore.Shared.Trim(args[1])
    TriggerClientEvent('QBCore:Command:SpawnVehicle', source, vehicle)
end)
```

### QBCore:Command:DeleteVehicle

| Arguments | Type | Required | Default |
| :-------: | :--: | :------: | :-----: |
|   none    | none |    no    |  none   |

> **Nota:** Client example

```lua
RegisterCommand('deleteveh', function(_, args)
    TriggerEvent('QBCore:Command:DeleteVehicle')
end)
```

> **Nota:** Server example

```lua
RegisterCommand('deleteveh', function(source, args)
    TriggerClientEvent('QBCore:Command:DeleteVehicle', source)
end)
```

### QBCore:Player:SetPlayerData

> **Consejo:** This event can be used as an event handler to trigger code because it indicates that the players data has changed!

```lua
RegisterNetEvent('QBCore:Player:SetPlayerData', function(val)
    PlayerData = val
    print(QBCore.Debug(PlayerData))
end)
```

### QBCore:Client:VehicleInfo

> **Consejo:** This event can be used as an event handler to trigger code because it indicates that the player has interacted with a vehicle!

Data fields:

|  Field  |  Type  |              Description              |
| :-----: | :----: | :-----------------------------------: |
| vehicle | number |          Vehicle Network ID           |
|  seat   | number | Seat number (-1, 0, 1, 2, 3, 4, 5, 6) |
|  name   | string |          Model Display Name           |
|  event  | string |        Entering, Entered, Left        |

```lua
RegisterNetEvent('QBCore:Client:VehicleInfo', function(data)
    print(QBCore.Debug(data))
end)
```

### QBCore:Notify

| Arguments |      Type       | Required |    Default    |
| :-------: | :-------------: | :------: | :-----------: |
|  message  | string \| table |   yes    | 'Placeholder' |
|   type    |     string      |   yes    |   'primary'   |
|  length   |     number      |   yes    |     5000      |

> **Nota:** Client example

```lua
-- /testnotify This is my message, primary, 5000

RegisterCommand('testnotify', function(_, args)
    local message = {}
    for i=1, #args do
        message[#message + 1] = args[i]
        if string.match(args[i], ',') then
            local text = table.concat(message, ' '):gsub(",", "")
            local type = args[i + 1]:gsub(",", "")
            local length = args[i + 2]
            TriggerEvent('QBCore:Notify', text, type, length)
            break
        end
    end
end)

-- Using QBCore's shared functions!

RegisterCommand('testnotify', function(_, args)
    local message = QBCore.Shared.SplitStr(table.concat(args, ' '), ",")
    local text = message[1]
    local type = QBCore.Shared.Trim(message[2])
    local length = tonumber(message[3])
    TriggerEvent('QBCore:Notify', text, type, length)
end)
```

> **Nota:** Server example

```lua
-- /testnotify This is my message, primary, 5000

RegisterCommand('testnotify', function(source, args)
    local message = {}
    for i=1, #args do
        message[#message + 1] = args[i]
        if string.match(args[i], ',') then
            local text = table.concat(message, ' '):gsub(",", "")
            local type = args[i + 1]:gsub(",", "")
            local length = args[i + 2]
            TriggerClientEvent('QBCore:Notify', source, text, type, length)
            break
        end
    end
end)

-- Using QBCore's shared functions!

RegisterCommand('testnotify', function(source, args)
    local message = QBCore.Shared.SplitStr(table.concat(args, ' '), ",")
    local text = message[1]
    local type = QBCore.Shared.Trim(message[2])
    local length = tonumber(message[3])
    TriggerClientEvent('QBCore:Notify', source, text, type, length)
end)
```

### QBCore:Client:UseItem

| Arguments |  Type  | Required | Default |
| :-------: | :----: | :------: | :-----: |
| item name | string |   yes    |  none   |

> **Nota:** Client example (must have the item in your inventory)

```lua
-- /useitem sandwich 1

RegisterCommand('useitem', function(_, args)
    local item = {
        name = args[1],
        amount = tonumber(args[2])
    }
    TriggerEvent('QBCore:Client:UseItem', item)
end)
```

> **Nota:** Server example (must have the item in your inventory)

```lua
-- /useitem sandwich 1

RegisterCommand('useitem', function(source, args)
    local item = {
        name = args[1],
        amount = tonumber(args[2])
    }
    TriggerClientEvent('QBCore:Client:UseItem', source, item)
end)
```

### QBCore:Command:ShowMe3D

| Arguments |  Type  | Required | Default |
| :-------: | :----: | :------: | :-----: |
| player id | number |   yes    |  none   |
|  message  | string |   yes    |  none   |

> **Nota:** Client example

```lua
-- /3dtext This is my message

RegisterCommand('3dtext', function(_, args)
    local message = table.concat(args, ' ')
    TriggerEvent('QBCore:Command:ShowMe3D', PlayerId(), message)
end)
```

> **Nota:** Server example

```lua
-- /3dtext This is my message

RegisterCommand('3dtext', function(source, args)
    local message = table.concat(args, ' ')
    TriggerClientEvent('QBCore:Command:ShowMe3D', source, message)
end)
```

### QBCore:Client:OnSharedUpdate

> **Nota:** Server example

> **Importante:** This only updates shared data for the client, it does not update the server. Also it does not persist through server restarts. To make persistent changes you must update the shared files.

Arguments:

1. tableName: The Shared field that should be updated
2. key: Key of the field to update
3. value: New value of the field to update

```lua
    RegisterCommand('addjob', function()
        TriggerClientEvent('QBCore:Client:OnSharedUpdate', -1, 'Jobs', 'sheriff', {
            label = 'Sheriff\'s',
            type = 'leo',
            defaultDuty = true,
            offDutyPay = false,
            grades = {
                ['0'] = { name = 'Recruit', payment = 50 },
                ['1'] = { name = 'Officer', payment = 75 },
                ['2'] = { name = 'Sergeant', payment = 100 },
                ['3'] = { name = 'Lieutenant', payment = 125 },
                ['4'] = { name = 'Sheriff', isboss = true, payment = 150 },
            },
        })
    end)
```

### QBCore:Client:OnSharedUpdateMultiple

> **Nota:** Server example

> **Importante:** This only updates shared data for the client, it does not update the server. Also it does not persist through server restarts. To make persistent changes you must update the shared files.

Arguments:

1. tableName: The Shared field it should be updated
2. values: The key-value pairs to update

```lua
    RegisterCommand('addjob', function()
        TriggerClientEvent('QBCore:Client:OnSharedUpdateMultiple', -1, 'Jobs', {
            sheriff = {
                label = 'Sheriff\'s',
                type = 'leo',
                defaultDuty = true,
                offDutyPay = false,
                grades = {
                    ['0'] = { name = 'Recruit', payment = 50 },
                    ['1'] = { name = 'Officer', payment = 75 },
                    ['2'] = { name = 'Sergeant', payment = 100 },
                    ['3'] = { name = 'Lieutenant', payment = 125 },
                    ['4'] = { name = 'Sheriff', isboss = true, payment = 150 },
                },
            },
            lspd = {
                label = 'LSPD',
                type = 'leo',
                defaultDuty = true,
                offDutyPay = false,
                grades = {
                    ['0'] = { name = 'Recruit', payment = 50 },
                    ['1'] = { name = 'Officer', payment = 75 },
                    ['2'] = { name = 'Sergeant', payment = 100 },
                    ['3'] = { name = 'Lieutenant', payment = 125 },
                    ['4'] = { name = 'Chief', isboss = true, payment = 150 },
                },
            }
        })
    end)
```

### QBCore:Client:SharedUpdate

> **Nota:** Server example

> **Importante:** This only updates shared data for the client, it does not update the server. Also it does not persist through server restarts. To make persistent changes you must update the shared files.

Arguments:

1. table: All shared data

```lua
    RegisterCommand('setshared', function()
        local newShared = {
            Jobs = {
                sheriff = {
                    label = 'Sheriff\'s',
                    type = 'leo',
                    defaultDuty = true,
                    offDutyPay = false,
                    grades = {
                        ['0'] = { name = 'Recruit', payment = 50 },
                        ['1'] = { name = 'Officer', payment = 75 },
                        ['2'] = { name = 'Sergeant', payment = 100 },
                        ['3'] = { name = 'Lieutenant', payment = 125 },
                        ['4'] = { name = 'Sheriff', isboss = true, payment = 150 },
                    },
                },
                lspd = {
                    label = 'LSPD',
                    type = 'leo',
                    defaultDuty = true,
                    offDutyPay = false,
                    grades = {
                        ['0'] = { name = 'Recruit', payment = 50 },
                        ['1'] = { name = 'Officer', payment = 75 },
                        ['2'] = { name = 'Sergeant', payment = 100 },
                        ['3'] = { name = 'Lieutenant', payment = 125 },
                        ['4'] = { name = 'Chief', isboss = true, payment = 150 },
                    },
                }
            },
            Items = {
                sandwich = {
                    name = 'sandwich',
                    label = 'Sandwich',
                    weight = 200,
                    type = 'item',
                    image = 'sandwich.png',
                    unique = false,
                    useable = true,
                    shouldClose = true,
                    combinable = nil,
                    description = 'A tasty sandwich',
                }
            }
        }
        TriggerClientEvent('QBCore:Client:SharedUpdate', -1, newShared)
    end)
```

### QBCore:Client:UpdateObject

> **Consejo:** This event must be used as a handler when using [shared-exports.md](shared-exports.md) because it refreshes the core object in your resource

```lua
RegisterNetEvent('QBCore:Client:UpdateObject', function()
    QBCore = exports['qb-core']:GetCoreObject()
end)
```
