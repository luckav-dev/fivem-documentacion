> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/GetClosestVehicle/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

## lib.getClosestVehicle

Get the vehicle handle and coords of the closest vehicle to a set of coordinates.

```lua
lib.getClosestVehicle(coords, maxDistance, includePlayerVehicle)
```

- coords: `vector3`
  - The coords to check from.
- maxDistance?: `number`
  - The max distance to check.
  - Default: `2.0`
- includePlayerVehicle?: `boolean`
  - Whether or not to include the player's current vehicle. Ignored on the server.
  - Default: `false`

Return:

- vehicle?: `number`
- vehicleCoords?: `vector3`
