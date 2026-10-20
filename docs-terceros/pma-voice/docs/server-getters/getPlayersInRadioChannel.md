> Fuente original: https://github.com/AvarianKnight/pma-voice/blob/6c9d96ed7a02e30912f1a0ce92629bf9afbbca8c/docs/server-getters/getPlayersInRadioChannel.md · repositorio AvarianKnight/pma-voice @ 6c9d96e · copiado el 2026-10-20

## getPlayersInRadioChannel

## Description

Gets a list of all of the players in the specified radio channel.

## Parameters

* **radioChannel**: The channel to get all the members of

## Returns

Returns a table of all of the players in the specified radio channel

```lua
-- this will return all of the current players in radio channel 1
local players = exports['pma-voice']:getPlayersInRadioChannel(1)
for source, isTalking in pairs(players) do
	print(('%s is in radio channel 1, isTalking: %s'):format(GetPlayerName(source), isTalking))
end
```
