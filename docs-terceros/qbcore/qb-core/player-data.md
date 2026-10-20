> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qb-core/player-data.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# 📊 Player Data

*Learn how to access and modify a player's data*

## Introduction

The **Player Data** object in `qb-core` stores all information related to a player's character, such as personal details, job, gang affiliation, metadata, and more. These values are initialized using default values defined in the `config.lua` file of `qb-core`.

This guide will provide an overview of the structure, default values, and how you can access or modify player data

```
QBCore
├── Players
│   ├── [source]
│       ├── PlayerData
│           ├── citizenid: string (Unique identifier)
│           ├── cid: number (Character ID)
│           ├── money: table
│           │   └── { cash: number, bank: number }
│           ├── charinfo: table
│           │   ├── firstname: string
│           │   ├── lastname: string
│           │   ├── ...
│           ├── job: table
│           │   ├── name: string
│           │   ├── label: string
│           │   ├── payment: number
│           │   ├── onduty: boolean
│           │   ├── isboss: boolean
│           │   └── grade: table
│           │       ├── name: string
│           │       └── level: number
│           ├── gang: table
│           │   ├── name: string
│           │   ├── label: string
│           │   ├── isboss: boolean
│           │   └── grade: table
│           │       ├── name: string
│           │       └── level: number
│           ├── metadata: table
│           │   ├── hunger: number
│           │   ├── thirst: number
│           │   ├── stress: number
│           │   ├── isdead: boolean
│           │   └── ...
│           ├── position: vector3
│           └── items: table (inventory items)
```

## Configuration

The player data default values can be modified in the `config.lua` file of `qb-core`. These defaults are stored in `QBConfig.Player.PlayerDefaults` and determine what a player starts with when creating a new character

## Player Data Object Structure

> **Consejo:** As of `qb-core` version 1.3.0 (check your fxmanifest.lua) you don't have to import the core to have access to the player data. You can call it like this!\
> \
> `exports['qb-core']:GetPlayer(source)` — server\
> \
> `exports['qb-core']:GetPlayerData()` — client

> **Nota:** When accessing the player object on the server using `QBCore.Functions.GetPlayer` pass the source (player net id) — shown in examples
>
> \
> When accessing the player object on the client, you don't have to pass anything and can just call `QBCore.Functions.GetPlayerData`
>
>
>
> If you prefer to access the player data directly instead of calling the functions, you can do so with this format `QBCore.Players[source].PlayerData` but it's not recommended

Below is a breakdown of the player data structure, its properties, default values and how to access them when retrieving the player object

### Identification Table

| Property    | Type     | Default Value                   | Description                                      |
| ----------- | -------- | ------------------------------- | ------------------------------------------------ |
| `citizenid` | `string` | Generated via `CreateCitizenId` | A unique identifier for the player.              |
| `cid`       | `number` | `1`                             | Character ID (used for multi-character systems). |

```lua
local QBCore = exports['qb-core']:GetCoreObject()

RegisterNetEvent('qb-docs:server:getPlayerInfo', function(source)
    local Player = QBCore.Functions.GetPlayer(source)
    if not Player then return end
    local citizenid = Player.PlayerData.citizenid
    print(citizenid)
end)
```

### Money Table

| Property | Type    | Default Value            | Description                                   |
| -------- | ------- | ------------------------ | --------------------------------------------- |
| `money`  | `table` | `{ cash = 0, bank = 0 }` | Contains the player’s cash and bank balances. |

```lua
local QBCore = exports['qb-core']:GetCoreObject()

RegisterNetEvent('qb-docs:server:getPlayerInfo', function(source)
    local Player = QBCore.Functions.GetPlayer(source)
    if not Player then return end
    local money = Player.PlayerData.money
    local cash = money.cash
    local bank = money.bank
    print(cash, bank)
end)
```

### Character Information Table

| Property   | Type    | Default Value                  | Description                                  |
| ---------- | ------- | ------------------------------ | -------------------------------------------- |
| `charinfo` | `table` | `{ firstname, lastname, ... }` | Basic personal information about the player. |

#### **Subfields**:

| Subfield      | Type     | Default Value                       | Description                                     |
| ------------- | -------- | ----------------------------------- | ----------------------------------------------- |
| `firstname`   | `string` | `"Firstname"`                       | The player's first name.                        |
| `lastname`    | `string` | `"Lastname"`                        | The player's last name.                         |
| `birthdate`   | `string` | `"00-00-0000"`                      | The player's date of birth.                     |
| `gender`      | `number` | `0`                                 | The player's gender (0 for male, 1 for female). |
| `nationality` | `string` | `"USA"`                             | The player's nationality.                       |
| `phone`       | `string` | Generated via `CreatePhoneNumber`   | The player's phone number.                      |
| `account`     | `string` | Generated via `CreateAccountNumber` | The player's bank account number.               |

```lua
local QBCore = exports['qb-core']:GetCoreObject()

RegisterNetEvent('qb-docs:server:getPlayerInfo', function(source)
    local Player = QBCore.Functions.GetPlayer(source)
    if not Player then return end
    local charinfo = Player.PlayerData.charinfo
    local firstname = Player.PlayerData.firstname
    local lastname = Player.PlayerData.lastname
    local birthdate = Player.PlayerData.birthdate
    local gender = Player.PlayerData.gender
    local nationality = Player.PlayerData.nationality
    local phone = Player.PlayerData.phone
    local account = Player.PlayerData.account
    print("Player's name:", firstname, lastname)
end)
```

### Job Table

| Property | Type    | Default Value                  | Description                                       |
| -------- | ------- | ------------------------------ | ------------------------------------------------- |
| `job`    | `table` | `{ name = 'unemployed', ... }` | The player’s current job and related information. |

#### Subfields

| Subfield  | Type      | Default Value                  | Description                                |
| --------- | --------- | ------------------------------ | ------------------------------------------ |
| `name`    | `string`  | `"unemployed"`                 | The job name.                              |
| `label`   | `string`  | `"Civilian"`                   | The display label of the job.              |
| `payment` | `number`  | `10`                           | The player’s salary.                       |
| `onduty`  | `boolean` | `false`                        | Whether the player is on duty.             |
| `isboss`  | `boolean` | `false`                        | Whether the player is the boss of the job. |
| `grade`   | `table`   | `{ name = 'Freelancer', ... }` | The player's job grade.                    |

```lua
local QBCore = exports['qb-core']:GetCoreObject()

RegisterNetEvent('qb-docs:server:getPlayerInfo', function(source)
    local Player = QBCore.Functions.GetPlayer(source)
    if not Player then return end
    local jobInfo = Player.PlayerData.job
    local name = jobInfo.name
    local label = jobInfo.label
    local payment = jobInfo.payment
    local onduty = jobInfo.onduty
    local isboss = jobInfo.isboss
    print("Player's job:", name)
    print("Job label:", label)
end)
```

### Gang Table

| Property | Type    | Default Value                    | Description                                        |
| -------- | ------- | -------------------------------- | -------------------------------------------------- |
| `gang`   | `table` | `{ name = 'Unaffiliated', ... }` | The player’s current gang and related information. |

#### Subfields

| Subfield | Type      | Default Value                    | Description                                |
| -------- | --------- | -------------------------------- | ------------------------------------------ |
| `name`   | `string`  | `"Unaffiliated"`                 | The gang name.                             |
| `label`  | `string`  | `"No Gang"`                      | The display label of the gang.             |
| `isboss` | `boolean` | `false`                          | Whether the player is the boss of the job. |
| `grade`  | `table`   | `{ name = 'Unaffiliated', ... }` | The player's job grade.                    |

```lua
local QBCore = exports['qb-core']:GetCoreObject()

RegisterNetEvent('qb-docs:server:getPlayerInfo', function(source)
    local Player = QBCore.Functions.GetPlayer(source)
    if not Player then return end
    local gangInfo = Player.PlayerData.gang
    local name = gangInfo.name
    local label = gangInfo.label
    print("Player's gang:", name)
    print("Gang label:", label)
end)
```

### Metadata Table

| Property | Type      | Default Value | Description                                        |
| -------- | --------- | ------------- | -------------------------------------------------- |
| `hunger` | `number`  | `100`         | The player’s hunger level (0–100).                 |
| `thirst` | `number`  | `100`         | The player’s thirst level (0–100).                 |
| `stress` | `number`  | `0`           | The player’s stress level (0–100).                 |
| `isdead` | `boolean` | `false`       | Whether the player is dead.                        |
| `inhale` | `boolean` | `false`       | Whether the player is handcuffed.                  |
| `phone`  | `table`   | `{}`          | Stores phone-specific data such as installed apps. |

```lua
local QBCore = exports['qb-core']:GetCoreObject()

RegisterNetEvent('qb-docs:server:getPlayerInfo', function(source)
    local Player = QBCore.Functions.GetPlayer(source)
    if not Player then return end
    local metadata = Player.PlayerData.metadata
    local hunger = metadata.hunger
    local thirst = metadata.thirst
    print('Hunger Level: ', hunger)
    print('Thirst Level: ', thirst)
end)
```

## Player Object Functions

Every player that is created on the server has certain functions that are attached to them. These functions can be called on them directly!

### UpdatePlayerData

Update the players data on the client & server

> **Nota:** This function triggers the event `QBCore:Player:SetPlayerData`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.UpdatePlayerData()
```

### SetJob

Set a player's job and grade

* job: `string`
* grade: `number`
* <mark>returns</mark>: `boolean` - true for successful, false for unsuccessful

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.SetJob('police', 1)
```

### SetGang

Set a players gang and grade

* gang: `string`
* grade: `number`
* <mark>returns</mark>: `boolean` - true for successful, false for unsuccessful

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.SetGang('lostmc', 1)
```

### Notify

Shows the player a notification

* text: `string`
* type: `string` — error, success, primary, warning
* length (optional): `number`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.Notify('Hello!', 'success', 5000)
```

### HasItem

> **Nota:** Preferred to use inventory export for checking if has item! This function just routes to that

* item: `string | table`
* amount: `number`
* <mark>returns</mark>: `boolean`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.HasItem('water_bottle', 1)
```

### GetName

Get's the players full character name

* <mark>returns</mark>: `string`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.GetName()
```

### SetJobDuty

Sets the player on/off duty

> **Nota:** This function triggers the events `QBCore:Server:OnJobUpdate` and `QBCore:Client:OnJobUpdate` It also triggers the function `UpdatePlayerData`&#x20;

* duty: `boolean`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.SetJobDuty(true)
```

### SetPlayerData

Set the player data value of a player specifically by it's name

> **Nota:** This function also triggers the function `UpdatePlayerData`&#x20;

* key: `string`
* value: `string | table`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.SetPlayerData('position', vector3(-425.3, 1123.6, 325.0))
```

### SetMetaData

Set the metadata value of a player specifically by it's name

> **Nota:** This function also triggers the function `UpdatePlayerData`&#x20;

* key: `string`
* value: `string | table | number`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.SetMetaData('hunger', 80)
```

### GetMetaData

Gets the value of a player metadata specifically by it's name

* value: `string`
* <mark>returns</mark>: `string | table | number`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.GetMetaData('hunger')
```

### AddRep

Adds rep to value to a rep specifically by it's name

> **Nota:** This function also triggers the function `UpdatePlayerData`&#x20;

> **Nota:** Add different kinds of rep in `qb-core/config.lua`

* rep: `string`
* amount: `number`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.AddRep('selling', 10)
```

### RemoveRep

Decreases value to a rep specifically by it's name

> **Nota:** This function also triggers the function `UpdatePlayerData`&#x20;

> **Nota:** Add different kinds of rep in `qb-core/config.lua`

* rep: `string`
* amount: `number`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.RemoveRep('selling', 10)
```

### GetRep

Gets the current value of rep specifically by it's name

* rep: `string`
* <mark>returns</mark>: `number`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.GetRep('selling')
```

### AddMoney

Adds to the value of a specific money type by it's name

> **Nota:** This function also triggers the function `UpdatePlayerData`&#x20;

* money: `string`
* <mark>returns</mark>: `boolean`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.AddMoney('cash', 1000)
```

### RemoveMoney

Decreases the value of a specific money type by it's name

> **Nota:** This function also triggers the function `UpdatePlayerData`&#x20;

* money: `string`
* <mark>returns</mark>: `boolean`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.RemoveMoney('cash', 1000)
```

### SetMoney

Sets the value of a specific money type by it's name

> **Nota:** This function also triggers the function `UpdatePlayerData`&#x20;

* money: `string`
* <mark>returns</mark>: `boolean`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.SetMoney('cash', 1000)
```

### GetMoney

Returns the value of the money type supplied

* money: `string`
* <mark>returns</mark>: `number`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.GetMoney('cash')
```

### Save

Triggers a save of the player

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.Save()
```

### Logout

Forces the player to logout back to the multicharacter screen

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.Logout()
```

### AddMethod

The `AddMethod` function allows you to dynamically add custom methods (functions) to the player object. This is particularly useful for extending player functionality in a modular and reusable way

> **Advertencia:** It's worth checking if a method already exists! You can do so by running this check\
> \
> `if Player.Functions.MyMethod then`\
> &#x20;   `print("Method already exists!")`\
> `end`

* method: `string`
* handler: `function`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end

Player.Functions.AddMethod('Greet', function()
    print("Hello, " .. Player.Functions.GetName() .. "!")
)

Player.Functions.Greet()
```

### AddField

The `AddField` function allows you to dynamically add custom fields (variables or data) to the player object. This is useful for storing additional player-specific data that isn’t part of the default `PlayerData` structure

> **Advertencia:** It's worth checking if a field already exists! You can do so by running this check\
> \
> `if Player.MyField then`\
> &#x20;   `print("Field already exists!")`\
> `end`

* field: `string`
* data: `any`

```lua
local Player = QBCore.Functions.GetPlayer(source)
if not Player then return end
Player.Functions.AddField("Skills", {
    hacking = 1,
    driving = 3,
    shooting = 2
})
```
