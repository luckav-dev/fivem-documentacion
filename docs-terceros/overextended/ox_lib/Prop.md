> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Prop.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Prop

A class for object entities implementing a custom statebag interface and common entity operations.

## Constructor

**Lua**

```lua
lib.prop:new(handle)
```

**TypeScript**

```ts
import { Prop } from "@overextended/ox_lib";

new Prop(handle)
```

- handle: `number` The entity's [script handle](https://docs.fivem.net/docs/scripting-manual/networking/ids/#entity-handle).

**Returns:** `Prop`

## Methods

### setOnGround

Attempts to set the entity onto the ground.  
On the server, this uses the `ox_entity_setonground` state and a [statebag change handler](https://github.com/overextended/ox_lib/blob/44796d362997f9d1b67a01b56ed5bcba1e73c2f4/resource/client.lua#L39-L74).

**Lua**

```lua
entity:setOnGround()
```

**TypeScript**

```ts
entity.setOnGround()
```

**Returns:** `boolean`

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
