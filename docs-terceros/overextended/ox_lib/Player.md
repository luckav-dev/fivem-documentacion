> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Player.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Player

A class that extends the [Ped](Ped.md) class with additional functionality for players.

## Constructor

**Lua**

```lua
lib.player:new(netId)
```

**TypeScript**

```ts
import { Player } from "@overextended/ox_lib";

new Player(netId)
```

- netId: `number` The player's [server id](https://docs.fivem.net/docs/scripting-manual/networking/ids/#server-id).

**Returns:** `Player`

## Methods

### setModel

Creates a new ped and assigns it to the player. On the client, this invalidates the entity handle (see [setHandle](#sethandle)).

**Lua**

```lua
entity:setModel(model)
```

**TypeScript**

```ts
entity.setModel(model)
```

- model: `string` | `number`

## Ped Methods

*(Contenido incluido desde [Ped](Ped.md))*

### getArmour

Gets the entity's current armour.

**Lua**

```lua
entity:getArmour()
```

**TypeScript**

```ts
entity.getArmour()
```

**Returns:** `number`

### setArmour

Sets the entity's armour.

**Lua**

```lua
entity:setArmour(amount)
```

**TypeScript**

```ts
entity.setArmour(amount)
```

- amount: `number`

*(Contenido incluido desde [GameEntity](GameEntity.md))*

## GameEntity Methods

### set

Writes a value to the entity's statebag.

**Lua**

```lua
entity:set(key, value)
```

**TypeScript**

```ts
entity.set(key, value)
```

- key: `string`
- value: `any`

**Returns:** `boolean` - If the state changed.

### setr

Writes a replicated value to the entity's statebag. Client-set values are validated by the server (see [Hooks](Hooks.md#registered-hooks)).  
Replicated values are synced between the server and all relevant players.

**Lua**

```lua
entity:setr(key, value)
```

**TypeScript**

```ts
entity.setr(key, value)
```

- key: `string`
- value: `any`

**Returns:** `boolean` - If the state changed.

### sets

Writes a synced value to the entity's statebag. Client-set values are validated by the server (see [Hooks](Hooks.md#registered-hooks)).  
Synced values are only replicated between the player and server, and cannot be set on non-player entities.

**Lua**

```lua
entity:sets(key, value)
```

**TypeScript**

```ts
entity.sets(key, value)
```

- key: `string`
- value: `any`

**Returns:** `boolean` - If the state changed.

### get

Returns a value from the entity's statebag.

**Lua**

```lua
entity:get(key)
```

**TypeScript**

```ts
entity.get(key)
```

- key: `string`

**Returns:** `unknown`

### has

Returns whether a key exists in the entity's statebag.

**Lua**

```lua
entity:has(key)
```

**TypeScript**

```ts
entity.has(key)
```

- key: `string`

**Returns:** `boolean`

### keys

Returns an array of all keys set on the entity's statebag.

**Lua**

```lua
entity:keys()
```

**TypeScript**

```ts
entity.keys()
```

**Returns:** `string[]`

### setHandle

Updates the handle, netId, and statebag properties on an entity. Useful if re-using an entity instance, respawning an entity, changing the model, etc.

**Lua**

```lua
entity:setHandle(handle)
```

**TypeScript**

```ts
entity.setHandle(handle)
```

- handle: `number`

### getCoords

Gets the entity's current coordinates.

**Lua**

```lua
entity:getCoords()
```

**TypeScript**

```ts
entity.getCoords()
```

**Returns:** `Vector3`

### setCoords

Sets the entity's coordinates to the specified position.

**Lua**

```lua
entity:setCoords(x, y, z, deadFlag, ragdollFlag, clearArea)
```

**TypeScript**

```ts
entity.setCoords()
```

- x: `number`
- y: `number`
- z: `number`
- deadFlag?: `boolean` (Defaults to false)
- ragdollFlag?: `boolean` (Defaults to false)
- clearArea?: `boolean` (Defaults to false)

### getModel

Gets the entity's current model hash.

**Lua**

```lua
entity:getModel()
```

**TypeScript**

```ts
entity.getModel()
```

**Returns:** `number`

### getHeading

Gets the entity's current heading (or yaw) in degrees.

**Lua**

```lua
entity:getHeading()
```

**TypeScript**

```ts
entity.getHeading()
```

**Returns:** `number`

### setHeading

Sets the entity's heading (or yaw) to the given value in degrees.

**Lua**

```lua
entity:setHeading(heading)
```

**TypeScript**

```ts
entity.setHeading(heading)
```

- heading: `number`

### getRoutingBucket

Gets the entity's current routing bucket.

**Lua**

```lua
entity:getRoutingBucket()
```

**TypeScript**

```ts
entity.getRoutingBucket()
```

**Returns:** `number`

### setRoutingBucket

Sets the entity's routing bucket to the given id. **Server only.**

**Lua**

```lua
entity:setRoutingBucket(bucketId)
```

**TypeScript**

```ts
entity.setRoutingBucket(bucketId)
```

- bucketId: `number`
