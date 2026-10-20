> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/GetClosestPlayer/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

## lib.getClosestPlayer

Get the player id, ped handle, and coords of the closest player to a set of coordinates.

```lua
lib.getClosestPlayer(coords, maxDistance, ignorePlayerId)
```

- coords: `vector3`
  - The coords to check from.
- maxDistance?: `number`
  - The max distance to check.
  - Default: `2.0`
- ignorePlayerId?: `number`|`false`
  - A player ID to ignore when checking. Set to `false` to include all players.
  - Default: `false`

Return:

- playerId?: `number`
- playerPed?: `number`
- playerCoords?: `vector3`
