> Fuente original: https://github.com/AvarianKnight/pma-voice/blob/6c9d96ed7a02e30912f1a0ce92629bf9afbbca8c/docs/state-getters/stateBagGetters.md · repositorio AvarianKnight/pma-voice @ 6c9d96e · copiado el 2026-10-20

## State Bag Getters/Setters

## Description

State bag getters are a little bit simpler, they just return the current value that is set in the state bag.

#### Note: If you're on the client and only using it on the current player, you can replace Player(source) with LocalPlayer

## Example for Proximity

```lua
local plyState = Player(source).state
local proximity = plyState.proximity
print(proximity.index) -- prints the index of the proximity as seen in Cfg.voiceModes
print(proximity.distance) -- prints the distance of the proximity
print(proximity.mode) -- prints the mode name of the proximity
```
