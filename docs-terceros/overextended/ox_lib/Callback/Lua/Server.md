> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Callback/Lua/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

## Trigger Client Callback

### lib.callback

The response is handled in a separate coroutine.

```lua
lib.callback(name, playerId, cb, ...)
```

- name: `string`
- playerId: `number`
- cb: `function`
- ...: `any`

```lua
lib.callback('ox:getNearbyVehicles', source, function(vehicles)
    for i = 1, #vehicles do
        DeleteEntity(entity)
    end
end, args.radius)
```

### lib.callback.await

The current coroutine is yielded until a response is received.

```lua
lib.callback.await(name, playerId, ...)
```

- name: `string`
- playerId: `number`
- ...: `any`

```lua
local vehicles = lib.callback.await('ox:getNearbyVehicles', source, args.radius)

for i = 1, #vehicles do
    DeleteEntity(entity)
end
```

## Register Server Callback

### lib.callback.register

Register an event handler for responding to client requests.

```lua
lib.callback.register(name, cb)
```

- name: `string`
- cb: `function`

```lua
lib.callback.register('ox_inventory:getItemCount', function(source, item, metadata, target)
    local inventory = target and Inventory(target) or Inventory(source)
    return (inventory and Inventory.GetItem(inventory, item, metadata, true)) or 0
end)
```
