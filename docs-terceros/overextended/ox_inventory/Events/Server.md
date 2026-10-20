> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_inventory/Events/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

This is not a comprehensive list of events and is missing events intended for internal use only.

## Handlers

> **Advertencia:** These events **should not** be triggered by any other scripts.

### ox_inventory:openedInventory

Triggered after an inventory is opened by a player.

```lua
AddEventHandler('ox_inventory:openedInventory', function(playerId, inventoryId) end)
```

- playerId: `number`
- inventoryId: `string`

### ox_inventory:closedInventory

Triggered after an inventory is closed by a player.

```lua
AddEventHandler('ox_inventory:closedInventory', function(playerId, inventoryId) end)
```

### ox_inventory:usedItem

```lua
AddEventHandler('ox_inventory:usedItem', function(playerId, name, slotId, metadata) end)
```

- playerId: `number`
- name: `string`
- slotId: `number`
- metadata?: `table`
