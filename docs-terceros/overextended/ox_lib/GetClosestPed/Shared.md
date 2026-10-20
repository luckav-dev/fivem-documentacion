> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/GetClosestPed/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

## lib.getClosestPed

Get the ped handle and coords of the closest ped to a set of coordinates.

```lua
lib.getClosestPed(coords, maxDistance)
```

- coords: `vector3`
  - The coords to check from.
- maxDistance?: `number`
  - The max distance to check.
  - Default: `2.0`

Return:

- ped?: `number`
- coords?: `vector3`
