> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_core/Events/server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server Events

> **Advertencia:** These events are triggered by ox_core when an action occurs. You should not trigger them from
> other scripts.

## ox:savedPlayers

When players are saved to the database.

> **Nota:** By default this event is triggered:
> * Every 10 minutes.
> * When the server is shutdown.
> * When [`Ox.SaveAllPlayers`](../Functions/server.md#oxsaveallplayers) is called.
> * When the command `saveplayers` is used.

**Lua**

```lua copy
AddEventHandler('ox:savedPlayers', function(playersSaved)
    print(playersSaved)
end)
```

**JS**

```ts copy
on('ox:savedPlayers', (playersSaved: number) => {
  console.log(playersSaved);
});
```

* playersSaved: `number`

## ox:setActiveGroup

When the active group of a character has changed.

**Lua**

```lua copy
AddEventHandler('ox:setActiveGroup', function(playerId, groupName, previousGroupName)
    print(playerId, groupName, previousGroupName)
end)
```

**JS**

```ts copy
on('ox:setActiveGroup', (playerId: number, groupName: string, previousGroupName: string | undefined) => {
  console.log(playersSaved);
});
```

- playerId: `number`
- groupName: `string`
- previousGroupName: `string | undefined`

## ox:setGroup

When a character is added or removed from a group.

**Lua**

```lua copy
AddEventHandler('ox:setGroup', function(playerId, groupName, grade)
    print(playerId, groupName, grade)
end)
```

**JS**

```ts copy
on('ox:setGroup', (playerId: number, groupName: string, grade?: number) => {
  console.log(playerId, groupName, grade);
});
```

- playerId: `number`
- groupName: `string`
- grade?: `number`

## ox:licenseAdded

When a character receives a new license.

**Lua**

```lua copy
AddEventHandler('ox:licenseAdded', function(playerId, licenseName)
    print(playerId, licenseName)
end)
```

**JS**

```ts copy
on('ox:licenseAdded', (playerId: number, licenseName: string) => {
  console.log(playerId, licenseName);
});
```

- playerId: `number`
- licenseName: `string`

## ox:licenseRemoved

When a character's license is removed.

**Lua**

```lua copy
AddEventHandler('ox:licenseRemoved', function(playerId, licenseName)
    print(playerId, licenseName)
end)
```

**JS**

```ts copy
on('ox:licenseRemoved', (playerId: number, licenseName: string) => {
  console.log(playerId, licenseName);
});
```

- playerId: `number`
- licenseName: `string`

## ox:playerLogout

When a player logs out from their current character, crashes, or otherwise disconnects from the server.

**Lua**

```lua copy
AddEventHandler('ox:playerLogout', function(playerId, userId, charId)
    print(playerId, userId, charId)
end)
```

**JS**

```ts copy
on('ox:playerLogout', (playerId: number, userId: number, charId: number) => {
  console.log(playerId, userId, charId);
});
```

- playerId: `number`
- userId: `number`
- charId: `number`

## ox:createdCharacter

When a player has created a new character.

**Lua**

```lua copy
AddEventHandler('ox:createdCharacter', function(playerId, userId, charId)
    print(playerId, userId, charId)
end)
```

**JS**

```ts copy
on('ox:createdCharacter', (playerId: number, userId: number, charId: number) => {
  console.log(playerId, userId, charId);
});
```

- playerId: `number`
- userId: `number`
- charId: `number`

## ox:playerLoaded

When a player selects and loads a character.

**Lua**

```lua copy
AddEventHandler('ox:playerLoaded', function(playerId, userId, charId)
    print(playerId, userId, charId)
end)
```

**JS**

```ts copy
on('ox:playerLoaded', (playerId: number, userId: number, charId: number) => {
  console.log(playerId, userId, charId);
});
```

- playerId: `number`
- userId: `number`
- charId: `number`

## ox:deletedCharacter

When a character is deleted.

**Lua**

```lua copy
AddEventHandler('ox:deletedCharacter', function(playerId, userId, charId)
    print(playerId, userId, charId)
end)
```

**JS**

```ts copy
on('ox:deletedCharacter', (playerId: number, userId: number, charId: number) => {
  console.log(playerId, userId, charId);
});
```

- playerId: `number`
- userId: `number`
- charId: `number`

## ox:savedVehicles

When vehicles are saved to the database.

**Lua**

```lua copy
AddEventHandler('ox:savedVehicles', function(vehiclesSaved)
    print(vehiclesSaved)
end)
```

**JS**

```ts copy
on('ox:savedVehicles', (vehiclesSaved: number) => {
  console.log(vehiclesSaved);
});
```

- vehiclesSaved: `number`

## ox:spawnedVehicle

When an [`OxVehicle`](../Classes/Server/OxVehicle.md) has spawned.

**Lua**

```lua copy
AddEventHandler('ox:spawnedVehicle', function(entityId, id)
    print(entityId, id)
end)
```

**JS**

```ts copy
on('ox:spawnedVehicle', (entityId: number, id: number) => {
  console.log(entityId, id);
});
```

- entityId: `number`
- id: `number`

## ox:despawnVehicle

Before an [`OxVehicle`](../Classes/Server/OxVehicle.md) gets despawned.

**Lua**

```lua copy
AddEventHandler('ox:despawnVehicle', function(entityId, id)
    print(entityId, id)
end)
```

**JS**

```ts copy
on('ox:despawnVehicle', (entityId: number, id: number) => {
  console.log(entityId, id);
});
```

- entityId: `number`
- id: `number`

## ox:updatedBalance

When an account's balance is updated.

**Lua**

```lua copy
AddEventHandler('ox:updatedBalance', function(data)
    print(json.encode(data))
end)
```
* data `table`
  * accountId: `number`
  * amount: `number`
  * action: `'add' | 'remove'`

**JS**

```ts copy
on('ox:updatedBalance', (data: object) => {
  console.log(data);
});
```
* data `object`
  * accountId: `number`
  * amount: `number`
  * action: `'add' | 'remove'`

## ox:transferredMoney

When an account's money is transferred.

**Lua**

```lua copy
AddEventHandler('ox:transferredMoney', function(data)
    print(json.encode(data))
end)
```
* data `table`
  * fromAccountId: `number`
  * toAccountId: `number`
  * amount: `'add' | 'remove'`

**JS**

```ts copy
on('ox:transferredMoney', (data: object) => {
  console.log(data);
});
```
* data `object`
  * fromAccountId: `number`
  * toAccountId: `number`
  * amount: `'add' | 'remove'`

## ox:depositedMoney

When money is deposited into an account.

**Lua**

```lua copy
AddEventHandler('ox:depositedMoney', function(data)
    print(json.encode(data))
end)
```
* data `table`
  * playerId: `number`
  * accountId: `number`
  * amount: `number`

**JS**

```ts copy
on('ox:depositedMoney', (data: object) => {
  console.log(data);
});
```
* data `object`
  * playerId: `number`
  * accountId: `number`
  * amount: `number`

## ox:withdrewMoney

When money is withdrawn from an account.

**Lua**

```lua copy
AddEventHandler('ox:withdrewMoney', function(data)
    print(json.encode(data))
end)
```
* data `table`
  * playerId: `number`
  * accountId: `number`
  * amount: `number`

**JS**

```ts copy
on('ox:withdrewMoney', (data: object) => {
  console.log(data);
});
```
* data `object`
  * playerId: `number`
  * accountId: `number`
  * amount: `number`

## ox:invoicePaid

When an invoice is paid.

**Lua**

```lua copy
AddEventHandler('ox:invoicePaid', function(data)
    print(json.encode(data))
end)
```
* data `table`
  * amount: `number`
  * payerId: `number`
  * fromAccount: `number`
  * toAccount: `number`

**JS**

```ts copy
on('ox:invoicePaid', (data: object) => {
  console.log(data);
});
```
* data `object`
  * amount: `number`
  * payerId: `number`
  * fromAccount: `number`
  * toAccount: `number`
