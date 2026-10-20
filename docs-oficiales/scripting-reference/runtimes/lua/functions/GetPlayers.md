# GetPlayers

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/GetPlayers/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Returns a table of all connected players (server ID's).

## Syntax

```lua
GetPlayers()
```

## Examples

```lua
for _, playerId in ipairs(GetPlayers()) do
  local name = GetPlayerName(playerId)
  print(('Player %s with id %i is in the server'):format(name, playerId))
  -- ('%s'):format('text') is same as string.format('%s', 'text')
end
```
