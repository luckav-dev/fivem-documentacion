> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_vehiclekeys/exports/server.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Server Exports

*Documentation for server-side exports in the qbx_vehiclekeys resource. These exports provide functionality for checking and managing vehicle key ownership within the Qbox framework.*

## HasKeys

Returns whether the player has keys to the given vehicle entity

```lua
exports.qbx_vehiclekeys:HasKeys(source, vehicle)
```

- source: `number`
- vehicle: `number`

## GiveKeys

Gives keys to a player so that they can unlock/lock the doors and toggle the engine.
Notifies the player unless skipNotification is true.

```lua
exports.qbx_vehiclekeys:GiveKeys(source, vehicle, skipNotification)
```

- source: `number`
- vehicle: `number`
- skipNotification?: `boolean`

## RemoveKeys

Removes keys from the player. Notifies the player unless skipNotification is true.

```lua
exports.qbx_vehiclekeys:RemoveKeys(source, vehicle, skipNotification)
```

- source: `number`
- vehicle: `number`
- skipNotification?: `boolean`
