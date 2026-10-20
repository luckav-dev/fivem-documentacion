> Fuente original: https://github.com/AvarianKnight/pma-voice/blob/6c9d96ed7a02e30912f1a0ce92629bf9afbbca8c/docs/client-setters/setVoiceProperty.md · repositorio AvarianKnight/pma-voice @ 6c9d96e · copiado el 2026-10-20

## setVoiceProperty | SetMumbleProperty | SetTokoProperty

## Description

Sets the voice property, currently the only use is to enable/disable radios and radio clicks.

## Parameters

* **property**: The property to set
* **value**: The value to set the property to

```lua
-- Enable the radio
exports['pma-voice']:setVoiceProperty('radioEnabled', true)
-- Disable radio clicks
exports['pma-voice']:setVoiceProperty('micClicks', false)
```
