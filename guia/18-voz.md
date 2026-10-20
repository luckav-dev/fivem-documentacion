[← 17-frameworks](17-frameworks.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [19-seguridad →](19-seguridad.md)

# 18. Voz: pma-voice y Mumble

FiveM incluye un servidor de voz **Mumble** integrado en FXServer. El recurso estándar para usarlo es **pma-voice** (`AvarianKnight/pma-voice`).

## 18.1 Estado de pma-voice (2026)

- Versión del manifest **7.0.1**; última etiqueta **v7.0.2-rc3**; la rama *master* tiene cambios incompatibles con 7.0.0:
  - `voice_enablePhones` → **`voice_enableCalls`**
  - `voice_defaultPhoneVolume` → **`voice_defaultCallVolume`**
  - State bag `state.phone` → **`state.call`**
- Requiere OneSync. Funciona en FiveM y RedM (`game 'common'`).

## 18.2 Convars (con `setr`)

```cfg
setr voice_useNativeAudio true          # audio 3D nativo con eco/reverb (necesario para submixes)
setr voice_useSendingRangeOnly true     # solo oyes a quien está en tu rango (anti-troll, recomendado)
setr voice_enableUi 1
setr voice_enableProximityCycle 1
setr voice_defaultCycle "F11"           # tecla para cambiar distancia
setr voice_defaultVoiceMode 2           # 1 susurro, 2 normal, 3 gritar
setr voice_enableRadios 1
setr voice_defaultRadio "LMENU"         # Alt izquierdo
setr voice_defaultRadioVolume 30
setr voice_enableCalls 1
setr voice_defaultCallVolume 60
setr voice_enableSubmix 1
setr voice_enableRadioAnim 1
# Servidor de voz externo (FXServer dedicado solo a voz):
# setr voice_externalAddress "1.2.3.4"
# setr voice_externalPort 30120
```

Elige **un solo** modo de audio: `voice_useNativeAudio`, `voice_use3dAudio` o `voice_use2dAudio`.

## 18.3 Exports

```lua
-- Cliente
exports['pma-voice']:setRadioChannel(5)
exports['pma-voice']:setCallChannel(12345)
exports['pma-voice']:setRadioVolume(50)
exports['pma-voice']:setVoiceProperty('radioEnabled', true)
exports['pma-voice']:toggleMutePlayer(serverId)

-- Servidor
exports['pma-voice']:setPlayerRadio(src, 5)
exports['pma-voice']:setPlayerCall(src, 12345)
local enCanal = exports['pma-voice']:getPlayersInRadioChannel(5)
exports['pma-voice']:addChannelCheck(1, function(source)       -- canal 1 solo para policía
    return Player(source).state.trabajo == 'policia'
end)
```

State bags que usa: `proximity`, `radioChannel`, `callChannel`, `voiceIntent`, `disableRadio`.

## 18.4 Natives de Mumble (para sistemas propios)

`MumbleSetVoiceTarget`, `MumbleAddVoiceTargetChannel`, `MumbleAddVoiceTargetPlayerByServerId`, `MumbleClearVoiceTarget`, `MumbleSetVoiceChannel`, `MumbleSetAudioInputDistance`, `MumbleSetAudioOutputDistance`, `MumbleSetTalkerProximity`, `MumbleIsPlayerTalking`, `NetworkIsPlayerTalking`, `MumbleSetVolumeOverrideByServerId`, `MumbleSetSubmixForServerId`.


## Ver también (documentación offline)

- [Oficial: scripting-manual/voice](../docs-oficiales/scripting-manual/voice/README.md)
- [Terceros: pma-voice](../docs-terceros/pma-voice/README.md)

---

[← 17-frameworks](17-frameworks.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [19-seguridad →](19-seguridad.md)
