> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_core/modules/lib/server.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Server Lib

*Documentation for server-side library functions in the qbx_core resource. These functions provide utilities for spawning vehicles, managing entities, and handling server-side operations within the Qbox framework.*

## spawnVehicle

Creates a vehicle on the server-side and returns its net ID. If this is a player owned vehicle, and the persistence convar is enabled, the spawned vehicle will be persisted.

```lua
qbx.spawnVehicle(params)
```

- params: `table`
  - model: `integer`
    - A vehicle modle hash.
  - spawnSource: `integer | vector3 | vector4`
    - The handle of an entity or coords to spawn the vehicle at.
  - warp?: `boolean | integer`
    - An optional ped ID to warp into the vehicle after it spawns.
    - If `spawnSource` is a ped ID, you can pass `true` to warp the ped specified there instead.
  - props?: `table`
    - Refer to ox_lib's [Vehicle Properties](https://coxdocs.dev/ox_lib/Modules/VehicleProperties/Client#vehicle-properties).
  - bucket? `integer`
    - An optional routing bucket to move the spawned entity to.

Returns:

- netId: `integer`
- entity: `integer`

```lua
-- spawns the vehicle at `myVectorCoords` and warps `myPed` inside
qbx.spawnVehicle({
  model = `asbo`,
  spawnSource = myVectorCoords,
  warp = myPed,
})

-- spawns the vehicle at `myPed` and warps the same ped inside
qbx.spawnVehicle({
  model = `asbo`,
  spawnSource = myPed,
  warp = true, -- causes `myPed` to be warped into the vehicle
})
```
