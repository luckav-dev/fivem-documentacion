> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_garages/exports/server.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Server Exports

*Documentation for server-side exports available in the qbx_garages resource. These exports provide programmatic control over garage management, vehicle storage locations, and depot pricing within the Qbox framework.*

## RegisterGarage

Registers a garage at runtime. This is an alternative to defining them in the qbx_garages config.

```lua
exports.qbx_garages:RegisterGarage(name, config)
```

## SetVehicleGarage

Sets the vehicle's garage. Only affects the database.

```lua
exports.qbx_garages:SetVehicleGarage(vehicleId, garageName)
```

## SetVehicleDepotPrice

Sets the price to take the car out of the depot

```lua
exports.qbx_garages:SetVehicleDepotPrice(vehicleId, depotPrice)
```

## GetGarages

Returns the registered garages

```lua
exports.qbx_garages:GetGarages()
```
