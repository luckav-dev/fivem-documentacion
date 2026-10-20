> Fuente original: https://github.com/AvarianKnight/pma-voice/blob/6c9d96ed7a02e30912f1a0ce92629bf9afbbca8c/docs/client-setters/setCallChannel.md · repositorio AvarianKnight/pma-voice @ 6c9d96e · copiado el 2026-10-20

## setCallChannel | addPlayerToCall | SetCallChannel

## Description

Sets the local players call channel.

## Parameters

* **callChannel**: the call channel to join

```lua
-- Joins call channel 1
exports['pma-voice']:setCallChannel(1)

-- This will remove them from the call channel
exports['pma-voice']:setCallChannel(0)
```

addPlayerToCall is provided as a 'easier to read' version of setCallChannel.

```lua
-- Joins call channel 1
exports['pma-voice']:addPlayerToCall(1)
```
