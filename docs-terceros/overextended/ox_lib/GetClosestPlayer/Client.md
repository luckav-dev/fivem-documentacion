> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/GetClosestPlayer/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

## lib.getClosestPlayer

Get the player id, ped handle, and coords of the closest player to a set of coordinates.

```lua
lib.getClosestPlayer(coords, maxDistance, includePlayer)
```

- coords: `vector3`
  - The coords to check from.
- maxDistance?: `number`
  - The max distance to check.
  - Default: `2.0`
- includePlayer?: `boolean`
  - Whether or not to include the current player.
  - Default: `false`

Return:

- playerId?: `number`
- playerPed?: `number`
- playerCoords?: `vector3`
