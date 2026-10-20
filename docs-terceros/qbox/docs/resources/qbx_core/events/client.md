> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_core/events/client.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Client Events

*This document provides comprehensive documentation for client-side events within the Qbox Core framework. It outlines both non-networked and networked events that are triggered on the client, offering details on their purpose, usage, and any associated data structures (types).*

> **Advertencia:** These events **MUST NOT** be triggered by any other scripts.

> **Nota:** Some of these events use custom types.
> You can learn more about those in the Types section of this resource.

## Non-Networked Events

### OnPlayerLoaded

Triggered when the player finishes spawning.

```lua
AddEventHandler('QBCore:Client:OnPlayerLoaded', function() end)
```

## Networked Events

### SetDuty

Triggered when the player's job duty is updated.

```lua
RegisterNetEvent('QBCore:Client:SetDuty', function(onDuty) end)
```

- onDuty: `boolean`

### OnPermissionUpdate

Triggered when the player's permissions are updated. \
Only works for permissions set via Qbox.

```lua
RegisterNetEvent('QBCore:Client:OnPermissionUpdate', function() end)
```

### playerLoggedOut

Triggered when the player logs out and no longer exists in qbx_core's memory.

```lua
RegisterNetEvent('qbx_core:client:playerLoggedOut', function() end)
```

### OnJobUpdate

Triggered when the player's job is updated.

```lua
RegisterNetEvent('QBCore:Client:OnJobUpdate', function(job) end)
```

- job: [`PlayerJob`](../types/player.md#playerjob)

### OnGangUpdate

Triggered when the player's gang is updated.

```lua
RegisterNetEvent('QBCore:Client:OnGangUpdate', function(gang) end)
```

- gang: [`PlayerGang`](../types/player.md#playergang)

### onGroupUpdate

Triggered when the player's groups are updated. If grade is nil then group was removed otherwise group was added

```lua
RegisterNetEvent('qbx_core:client:onGroupUpdate', function(groupName, groupGrade) end)
```

- groupName: `string`
- groupGrade?: `number`

### OnMoneyChange

Triggered when the player's cash/bank balance is updated.

```lua
RegisterNetEvent('QBCore:Client:OnMoneyChange', function(moneytype, amount, operation, reason) end)
```

- moneyType: `'cash' | 'bank' | 'crypto'`
- amount: `number`
- operation: `'add' | 'remove' | 'set'`
- reason: `string`

### onSetMetaData

Triggered when player.Functions.setMetaData() is used.

```lua
RegisterNetEvent('qbx_core:client:onSetMetaData', function(key, oldValue, newValue) end)
```

- key: `string`
- oldValue: `any`
- newValue: `any`
