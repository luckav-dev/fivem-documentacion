> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_inventory/Events/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

This is not a comprehensive list of events and is missing events intended for internal use only.

## Event Triggers

> **Nota:** These events **are safe** to trigger and handle in other scripts.

### ox_inventory:disarm

Can be triggered to force the player to disarm.

```lua
TriggerClientEvent('ox_inventory:disarm', playerId, noAnim)
```

- playerId: `number`
- noAnim: `boolean`
  - If `true`, disarm animation will be skipped

### ox_inventory:suppressItemNotifications

Can be triggered to enable or disable NUI item notifications

```lua
TriggerClientEvent('ox_inventory:suppressItemNotifications', playerId, value)
```

- playerId: `number`
- value: `boolean`

## Event Handlers

> **Advertencia:** These events **should not** be triggered by any other scripts.

### ox_inventory:updateInventory

Triggered after inventory slots have been updated, included on load.  
Changes is a table containing all updated slot data indexed by slotId. Empty slots are `false`.

```lua
AddEventHandler('ox_inventory:updateInventory', function(changes) end)
```

- changes: `table<number, table | false>`

### ox_inventory:currentWeapon

Triggered when a weapon is equipped or its metadata is altered.

```lua
AddEventHandler('ox_inventory:currentWeapon', function(weapon) end)
```

- weapon?: `table`

### ox_inventory:itemCount

Triggered when the amount of an item in the player's inventory is changed.  
_Note: Not available for ESX, use esx:addInventoryItem or esx:removeInventoryItem._

```lua
AddEventHandler('ox_inventory:itemCount', function(itemName, totalCount) end)
```

- itemName: `string`
- totalCount: `number`

### ox_inventory:updateWeaponComponent

```lua
AddEventHandler('ox_inventory:updateWeaponComponent', function(action, componentHash, componentItem) end)
```

- action: `'added' | 'removed'`
- componentHash: `number`
- componentItem: `string`

### ox_inventory:usedItem

```lua
AddEventHandler('ox_inventory:usedItem', function(name, slotId, metadata) end)
```

- name: `string`
- slotId: `number`
- metadata?: `table`
