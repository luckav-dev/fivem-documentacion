> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_core/exports/shared.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Shared Exports

*Documentation for shared exports. Learn about available functions for retrieving data like all the jobs, gangs, ... .*

## GetJobs

Returns the jobs table.

```lua
exports.qbx_core:GetJobs()
```

Returns: [`table<string, Job>`](../types/job.md)

## GetGangs

Returns the gangs table.

```lua
exports.qbx_core:GetGangs()
```

Returns: [`table<string, Gang>`](../types/gang.md)

## GetJob

Returns the given job if it exists.

```lua
exports.qbx_core:GetJob(jobName)
```

- jobName: `string`

Returns: [`Job?`](../types/job.md)

## GetGang

Returns the given gang if it exists.

```lua
exports.qbx_core:GetGang(gangName)
```
- gangName: `string`

Returns: [`Gang?`](../types/gang.md)

## GetVehiclesByName

Returns a table mapping vehicle name to vehicle.

```lua
exports.qbx_core:GetVehiclesByName(vehicle)
```

- vehicle?: `string`

Returns: [`table<string, Vehicle>`](../types/vehicle.md#vehicle)

## GetVehiclesByHash

Returns a table mapping vehicle hash to vehicle.

```lua
exports.qbx_core:GetVehiclesByHash(vehicle)
```

- vehicle?: `number`

Returns: [`table<number, Vehicle>`](../types/vehicle.md#vehicle)

## GetVehiclesByCategory

Returns a table mapping vehicle category to vehicles.

```lua
exports.qbx_core:GetVehiclesByCategory()
```

Returns: [`table<string, Vehicle[]>`](../types/vehicle.md#vehicle)

## GetWeapons

Returns the weapons table.

```lua
exports.qbx_core:GetWeapons(weapon)
```

- weapon?: `number`

Returns: `table<number, Weapon>`

## GetLocations

Returns the locations table.

```lua
exports.qbx_core:GetLocations()
```

Returns: `table<string, vector4>`
