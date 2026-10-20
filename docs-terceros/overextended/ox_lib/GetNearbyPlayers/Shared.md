> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/GetNearbyPlayers/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

## lib.getNearbyPlayers

Get the player id, ped handle, and coords of all players within range of a set of coordinates.

```lua
lib.getNearbyPlayers(coords, maxDistance, includePlayer)
```

- coords: `vector3`
  - The coords to check from.
- maxDistance?: `number`
  - The max distance to check.
  - Default: `2.0`
- includePlayer?: `boolean`
  - Whether or not to include the current player. Ignored on the server.
  - Default: `false`

Return:

- players: `{ id: number, ped: number, coords: vector3 }[]`
