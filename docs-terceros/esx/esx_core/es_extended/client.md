> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/client.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# Client

## Global variables
All variables available on the client side inside the ESX Object.

### ESX.PlayerData
This is the player data object. See the [Player Data](playerdata.md) page for more information.

### ESX.PlayerLoaded
Is the player and his character loaded?

**Example**
```lua
if ESX.PlayerLoaded then
    print('Player is loaded')
end
```

### ESX.playerId
The player's local id, a cached value of `PlayerId()`.

### ESX.serverId
The player's server id, a cached value of `GetPlayerServerId(PlayerId())`.
