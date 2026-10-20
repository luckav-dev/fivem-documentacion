# Natives de GTA V — RECORDING

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `RECORDING`: **17** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`DisableRockstarEditorCameraChanges`](#disablerockstareditorcamerachanges) · [`IsRecording`](#isrecording) · [`N_0x13b350b8ad0eee10`](#n_0x13b350b8ad0eee10) · [`N_0x208784099002bc30`](#n_0x208784099002bc30) · [`N_0x293220da1b46cebc`](#n_0x293220da1b46cebc) · [`N_0x33d47e85b476abcd`](#n_0x33d47e85b476abcd) · [`N_0x4282e08174868be3`](#n_0x4282e08174868be3) · [`N_0x48621c9fca3ebd28`](#n_0x48621c9fca3ebd28) · [`N_0x66972397e0757e7a`](#n_0x66972397e0757e7a) · [`N_0x81cbae94390f9f89`](#n_0x81cbae94390f9f89) · [`N_0xdf4b952f7d381b95`](#n_0xdf4b952f7d381b95) · [`N_0xf854439efbb3b583`](#n_0xf854439efbb3b583) · [`SaveRecordingClip`](#saverecordingclip) · [`StartRecording`](#startrecording) · [`StopRecordingAndDiscardClip`](#stoprecordinganddiscardclip) · [`StopRecordingAndSaveClip`](#stoprecordingandsaveclip) · [`StopRecordingThisFrame`](#stoprecordingthisframe)

---
### DisableRockstarEditorCameraChanges

`_DISABLE_ROCKSTAR_EDITOR_CAMERA_CHANGES` · hash `0xAF66DCEE6609B148` · **Cliente**

```lua
DisableRockstarEditorCameraChanges()
```
```c
void _DISABLE_ROCKSTAR_EDITOR_CAMERA_CHANGES();
```

**Devuelve:** `void`

**Descripción oficial:**

This will disable the ability to make camera changes in R\* Editor.

**Nombres antiguos (alias):** `0xAF66DCEE6609B148` (`N_0xaf66dcee6609b148`)

---
### IsRecording

`_IS_RECORDING` · hash `0x1897CA71995A90B4` · **Cliente**

```lua
local retval = IsRecording()
```
```c
BOOL _IS_RECORDING();
```

**Devuelve:** `BOOL` — Whether recording is currently running, true when you start recording (F1) or turn on action replay (F2)

**Descripción oficial:**

Checks if you're recording.

---
### N_0x13b350b8ad0eee10

`0x13B350B8AD0EEE10` · hash `0x13B350B8AD0EEE10` · **Cliente**

```lua
N_0x13b350b8ad0eee10()
```
```c
void 0x13B350B8AD0EEE10();
```

**Devuelve:** `void`

---
### N_0x208784099002bc30

`0x208784099002BC30` · hash `0x208784099002BC30` · **Cliente**

```lua
N_0x208784099002bc30(missionNameLabel, p1)
```
```c
void 0x208784099002BC30(char* missionNameLabel, Any p1);
```

**Parámetros**

- `missionNameLabel` (`char*`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
-This function appears to be deprecated/ unused. Tracing the call internally leads to a _nullsub -  
first one seems to be a string of a mission name, second one seems to be a bool/toggle  
p1 was always 0.  
```

---
### N_0x293220da1b46cebc

`0x293220DA1B46CEBC` · hash `0x293220DA1B46CEBC` · **Cliente**

```lua
N_0x293220da1b46cebc(p0, p1, p2)
```
```c
void 0x293220DA1B46CEBC(float p0, float p1, int p2);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`int`)

**Devuelve:** `void`

---
### N_0x33d47e85b476abcd

`0x33D47E85B476ABCD` · hash `0x33D47E85B476ABCD` · **Cliente**

```lua
local retval = N_0x33d47e85b476abcd(p0)
```
```c
BOOL 0x33D47E85B476ABCD(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `BOOL`

---
### N_0x4282e08174868be3

`0x4282E08174868BE3` · hash `0x4282E08174868BE3` · **Cliente**

```lua
local retval = N_0x4282e08174868be3()
```
```c
Any 0x4282E08174868BE3();
```

**Devuelve:** `Any`

---
### N_0x48621c9fca3ebd28

`0x48621C9FCA3EBD28` · hash `0x48621C9FCA3EBD28` · **Cliente**

```lua
N_0x48621c9fca3ebd28(p0)
```
```c
void 0x48621C9FCA3EBD28(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### N_0x66972397e0757e7a

`0x66972397E0757E7A` · hash `0x66972397E0757E7A` · **Cliente**

```lua
N_0x66972397e0757e7a(p0, p1, p2)
```
```c
void 0x66972397E0757E7A(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x81cbae94390f9f89

`0x81CBAE94390F9F89` · hash `0x81CBAE94390F9F89` · **Cliente**

```lua
N_0x81cbae94390f9f89()
```
```c
void 0x81CBAE94390F9F89();
```

**Devuelve:** `void`

---
### N_0xdf4b952f7d381b95

`0xDF4B952F7D381B95` · hash `0xDF4B952F7D381B95` · **Cliente**

```lua
local retval = N_0xdf4b952f7d381b95()
```
```c
Any 0xDF4B952F7D381B95();
```

**Devuelve:** `Any`

---
### N_0xf854439efbb3b583

`0xF854439EFBB3B583` · hash `0xF854439EFBB3B583` · **Cliente**

```lua
N_0xf854439efbb3b583()
```
```c
void 0xF854439EFBB3B583();
```

**Devuelve:** `void`

---
### SaveRecordingClip

`_SAVE_RECORDING_CLIP` · hash `0x644546EC5287471B` · **Cliente**

```lua
local retval = SaveRecordingClip()
```
```c
BOOL _SAVE_RECORDING_CLIP();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x644546EC5287471B` (`N_0x644546ec5287471b`)

---
### StartRecording

`_START_RECORDING` · hash `0xC3AC2FFF9612AC81` · **Cliente**

```lua
StartRecording(mode)
```
```c
void _START_RECORDING(int mode);
```

**Parámetros**

- `mode` (`int`): 0 turns on action replay, 1 starts recording

**Devuelve:** `void`

**Descripción oficial:**

Starts recording a replay.\
If already recording a replay, does nothing.

**Nombres antiguos (alias):** `0xC3AC2FFF9612AC81` (`N_0xc3ac2fff9612ac81`)

---
### StopRecordingAndDiscardClip

`_STOP_RECORDING_AND_DISCARD_CLIP` · hash `0x88BB3507ED41A240` · **Cliente**

```lua
StopRecordingAndDiscardClip()
```
```c
void _STOP_RECORDING_AND_DISCARD_CLIP();
```

**Devuelve:** `void`

**Descripción oficial:**

Stops recording and discards the recorded clip.

**Nombres antiguos (alias):** `0x88BB3507ED41A240` (`N_0x88bb3507ed41a240`)

---
### StopRecordingAndSaveClip

`_STOP_RECORDING_AND_SAVE_CLIP` · hash `0x071A5197D6AFC8B3` · **Cliente**

```lua
StopRecordingAndSaveClip()
```
```c
void _STOP_RECORDING_AND_SAVE_CLIP();
```

**Devuelve:** `void`

**Descripción oficial:**

Stops recording and saves the recorded clip.

**Nombres antiguos (alias):** `_STOP_RECORDING` (`StopRecording`)

---
### StopRecordingThisFrame

`_STOP_RECORDING_THIS_FRAME` · hash `0xEB2D525B57F42B40` · **Cliente**

```lua
StopRecordingThisFrame()
```
```c
void _STOP_RECORDING_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Disable recording for this frame only.

**Nombres antiguos (alias):** `0xEB2D525B57F42B40` (`N_0xeb2d525b57f42b40`)

---
