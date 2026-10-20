# getPlayers

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/getPlayers/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Returns an array of all connected players (server ID's) **as strings**. Equivalent to [GetPlayers()](../../lua/functions/GetPlayers.md) in Lua.

## Syntax

```js
getPlayers();
```

## Examples

```js
const players = getPlayers();
for (const playerId of players) {
  console.log(playerId);
}
```
