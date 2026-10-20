> Fuente original: https://github.com/AvarianKnight/pma-voice/blob/6c9d96ed7a02e30912f1a0ce92629bf9afbbca8c/docs/server-setters/addChannelCheck.md · repositorio AvarianKnight/pma-voice @ 6c9d96e · copiado el 2026-10-20

## addChannelCheck

## Description

Adds a channel check to radio channels.

## Parameters

* **channel**: The channel to add the check to.
* **function**: the function to call when the check is triggered, which should return a boolean of if the player is allowed to join the channel..

```lua
-- Example for addChannelCheck
-- this always has to return true/false
exports['pma-voice']:addChannelCheck(1, function(source)
	if IsPlayerAceAllowed(source, 'radio.police') then
		return true
	end
	return false
end)
```
