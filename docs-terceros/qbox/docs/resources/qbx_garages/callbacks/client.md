> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_garages/callbacks/client.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Server Callbacks

*This document details the client-side callbacks available in the qbx_garages resource. These callbacks facilitate communication between client and server for garage management operations like retrieving garage data, vehicle management, and parking functionalities.*

Can be used to support a custom UI. Called from the client.

## getGarages

Get the currently registered garages

```lua
lib.callback.await('qbx_garages:server:getGarages')
```

## getGarageVehicles

Get vehicles that the player has access to in the given garage. Does not return vehicles currently spawned in the world.

```lua
lib.callback.await('qbx_garages:server:getGarageVehicles', false, garageName)
```

## isParkable

Returns true if the player can access the garage and the vehicle matches the garage filters

```lua
lib.callback.await('qbx_garages:server:isParkable', false, garageName, netId)
```

## parkVehicle

Stores the vehicle in the garage and deletes the entity from the world

```lua
lib.callback.await('qbx_garages:server:parkVehicle', false, netId, props, garageName)
```

## payDepotPrice

Takes vehicle's depot price from cash or bank and returns true if player paid. Does not update the vehicle's depot price after payment.

```lua
lib.callback.await('qbx_garages:server:payDepotPrice', false, vehicleId)
```

## spawnVehicle

Spawns the vehicle entity in the world at the given garage's access point. Checks that the player has required access permissions to do so.
Attempts to give the player vehicle keys.

```lua
lib.callback.await('qbx_garages:server:spawnVehicle', false, vehicleId, garageName, accessPointIndex)
```
