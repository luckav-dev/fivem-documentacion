# Natives de GTA V — PAD

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `PAD`: **48** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`DisableAllControlActions`](#disableallcontrolactions) · [`DisableControlAction`](#disablecontrolaction) · [`DisableInputGroup`](#disableinputgroup) · [`EnableAllControlActions`](#enableallcontrolactions) · [`EnableControlAction`](#enablecontrolaction) · [`GetAllowMovementWhileZoomed`](#getallowmovementwhilezoomed) · [`GetControlGroupInstructionalButton`](#getcontrolgroupinstructionalbutton) · [`GetControlInstructionalButton`](#getcontrolinstructionalbutton) · [`GetControlNormal`](#getcontrolnormal) · [`GetControlUnboundNormal`](#getcontrolunboundnormal) · [`GetControlValue`](#getcontrolvalue) · [`GetDisabledControlNormal`](#getdisabledcontrolnormal) · [`GetDisabledControlUnboundNormal`](#getdisabledcontrolunboundnormal) · [`GetIsUsingAlternateDriveby`](#getisusingalternatedriveby) · [`GetLocalPlayerAimState`](#getlocalplayeraimstate) · [`GetLocalPlayerGamepadAimState`](#getlocalplayergamepadaimstate) · [`GetTimeSinceLastInput`](#gettimesincelastinput) · [`IsControlEnabled`](#iscontrolenabled) · [`IsControlJustPressed`](#iscontroljustpressed) · [`IsControlJustReleased`](#iscontroljustreleased) · [`IsControlPressed`](#iscontrolpressed) · [`IsControlReleased`](#iscontrolreleased) · [`IsDisabledControlJustPressed`](#isdisabledcontroljustpressed) · [`IsDisabledControlJustReleased`](#isdisabledcontroljustreleased) · [`IsDisabledControlPressed`](#isdisabledcontrolpressed) · [`IsDisabledControlReleased`](#isdisabledcontrolreleased) · [`IsLookInverted`](#islookinverted) · [`IsUsingKeyboard`](#isusingkeyboard) · [`IsUsingKeyboard_2`](#isusingkeyboard_2) · [`N_0x14d29bb12d47f68c`](#n_0x14d29bb12d47f68c) · [`N_0x23f09eadc01449d6`](#n_0x23f09eadc01449d6) · [`N_0x25aaa32bdc98f2a3`](#n_0x25aaa32bdc98f2a3) · [`N_0x5b73c77d9eb66e24`](#n_0x5b73c77d9eb66e24) · [`N_0x6cd79468a1e595c6`](#n_0x6cd79468a1e595c6) · [`N_0xa0cefcea390aab9b`](#n_0xa0cefcea390aab9b) · [`N_0xcb0360efefb2580d`](#n_0xcb0360efefb2580d) · [`N_0xe1615ec03b3bb4fd`](#n_0xe1615ec03b3bb4fd) · [`N_0xf239400e16c23e08`](#n_0xf239400e16c23e08) · [`ResetInputMappingScheme`](#resetinputmappingscheme) · [`SetControlLightEffectColor`](#setcontrollighteffectcolor) · [`SetControlNormal`](#setcontrolnormal) · [`SetCursorLocation`](#setcursorlocation) · [`SetInputExclusive`](#setinputexclusive) · [`SetPadShake`](#setpadshake) · [`SetPlayerpadShakesWhenControllerDisabled`](#setplayerpadshakeswhencontrollerdisabled) · [`StopPadShake`](#stoppadshake) · [`SwitchToInputMappingScheme`](#switchtoinputmappingscheme) · [`SwitchToInputMappingScheme_2`](#switchtoinputmappingscheme_2)

---
### DisableAllControlActions

`DISABLE_ALL_CONTROL_ACTIONS` · hash `0x5F4B6931816E599B` · jhash `0x16753CF4` · **Cliente**

```lua
DisableAllControlActions(padIndex)
```
```c
void DISABLE_ALL_CONTROL_ACTIONS(int padIndex);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).

**Devuelve:** `void`

---
### DisableControlAction

`DISABLE_CONTROL_ACTION` · hash `0xFE99B66D079CF6BC` · jhash `0x3800C0DC` · **Cliente**

```lua
DisableControlAction(padIndex, control, disable)
```
```c
void DISABLE_CONTROL_ACTION(int padIndex, int control, BOOL disable);
```

**Parámetros**

- `padIndex` (`int`)
- `control` (`int`)
- `disable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

[Control values and meaning](https://docs.fivem.net/docs/game-references/controls/#controls)

Example: `CONTROLS::DISABLE_CONTROL_ACTION(2, 19, true)` disables the switching UI from appearing both when using a keyboard and Xbox 360 controller. Needs to be executed each frame.
Control group 1 and 0 gives the same results as 2. Same results for all players.

---
### DisableInputGroup

`_DISABLE_INPUT_GROUP` · hash `0x7F4724035FDCA1DD` · jhash `0x2CEDE6C5` · **Cliente**

```lua
DisableInputGroup(padIndex)
```
```c
void _DISABLE_INPUT_GROUP(int padIndex);
```

**Parámetros**

- `padIndex` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7F4724035FDCA1DD` (`N_0x7f4724035fdca1dd`)

---
### EnableAllControlActions

`ENABLE_ALL_CONTROL_ACTIONS` · hash `0xA5FFE9B05F199DE7` · jhash `0xFC2F119F` · **Cliente**

```lua
EnableAllControlActions(padIndex)
```
```c
void ENABLE_ALL_CONTROL_ACTIONS(int padIndex);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use.

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum ePadType {
  PLAYER_CONTROL = 0,
  CAMERA_CONTROL = 1,
  FRONTEND_CONTRO = 2
};
```

---
### EnableControlAction

`ENABLE_CONTROL_ACTION` · hash `0x351220255D64C155` · jhash `0xD2753551` · **Cliente**

```lua
EnableControlAction(padIndex, control, enable)
```
```c
void ENABLE_CONTROL_ACTION(int padIndex, int control, BOOL enable);
```

**Parámetros**

- `padIndex` (`int`)
- `control` (`int`)
- `enable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
control values and meaning: https://github.com/scripthookvdotnet/scripthookvdotnet/blob/47f8bb02a50e27d4bb982f43a78091feac59b21c/source/scripting_v3/GTA/Control.cs
and  
https://docs.fivem.net/docs/game-references/controls/
0, 1 and 2 used in the scripts.  
Control values from the decompiled scripts:   
0,1,2,3,4,5,6,8,9,10,11,14,15,16,17,19,21,22,24,25,26,30,31,32,33,34,35,36,  
37,44,46,47,59,60,65,68,69,70,71,72,73,74,75,76,79,80,81,82,86,95,98,99,100  
,101,114,140,141,143,172,173,174,175,176,177,178,179,180,181,187,188,189,19  
0,195,196,197,198,199,201,202,203,204,205,206,207,208,209,210,217,218,219,2  
20,221,225,228,229,230,231,234,235,236,237,238,239,240,241,242,245,246,257,  
261,262,263,264,286,287,288,289,337,338,339,340,341,342,343  
INPUTGROUP_MOVE  
INPUTGROUP_LOOK  
INPUTGROUP_WHEEL  
INPUTGROUP_CELLPHONE_NAVIGATE  
INPUTGROUP_CELLPHONE_NAVIGATE_UD  
INPUTGROUP_CELLPHONE_NAVIGATE_LR  
INPUTGROUP_FRONTEND_DPAD_ALL  
INPUTGROUP_FRONTEND_DPAD_UD  
INPUTGROUP_FRONTEND_DPAD_LR  
INPUTGROUP_FRONTEND_LSTICK_ALL  
INPUTGROUP_FRONTEND_RSTICK_ALL  
INPUTGROUP_FRONTEND_GENERIC_UD  
INPUTGROUP_FRONTEND_GENERIC_LR  
INPUTGROUP_FRONTEND_GENERIC_ALL  
INPUTGROUP_FRONTEND_BUMPERS  
INPUTGROUP_FRONTEND_TRIGGERS  
INPUTGROUP_FRONTEND_STICKS  
INPUTGROUP_SCRIPT_DPAD_ALL  
INPUTGROUP_SCRIPT_DPAD_UD  
INPUTGROUP_SCRIPT_DPAD_LR  
INPUTGROUP_SCRIPT_LSTICK_ALL  
INPUTGROUP_SCRIPT_RSTICK_ALL  
INPUTGROUP_SCRIPT_BUMPERS  
INPUTGROUP_SCRIPT_TRIGGERS  
INPUTGROUP_WEAPON_WHEEL_CYCLE  
INPUTGROUP_FLY  
INPUTGROUP_SUB  
INPUTGROUP_VEH_MOVE_ALL  
INPUTGROUP_CURSOR  
INPUTGROUP_CURSOR_SCROLL  
INPUTGROUP_SNIPER_ZOOM_SECONDARY  
INPUTGROUP_VEH_HYDRAULICS_CONTROL  
Took those in IDA Pro.Not sure in which order they go  
```

---
### GetAllowMovementWhileZoomed

`GET_ALLOW_MOVEMENT_WHILE_ZOOMED` · hash `0xFC859E2374407556` · jhash `0xC0823820` · **Cliente**

```lua
local retval = GetAllowMovementWhileZoomed()
```
```c
BOOL GET_ALLOW_MOVEMENT_WHILE_ZOOMED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns profile setting 17.
```

**Nombres antiguos (alias):** `0xFC859E2374407556` (`N_0xfc859e2374407556`)

---
### GetControlGroupInstructionalButton

`GET_CONTROL_GROUP_INSTRUCTIONAL_BUTTON` · hash `0x80C2FD58D720C801` · jhash `0x3EE71F6A` · **Cliente**

```lua
local retval = GetControlGroupInstructionalButton(padIndex, controlGroup, p2)
```
```c
char* GET_CONTROL_GROUP_INSTRUCTIONAL_BUTTON(int padIndex, int controlGroup, BOOL p2);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `controlGroup` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0x80C2FD58D720C801` (`N_0x80c2fd58d720c801`)

---
### GetControlInstructionalButton

`GET_CONTROL_INSTRUCTIONAL_BUTTON` · hash `0x0499D7B09FC9B407` · jhash `0x3551727A` · **Cliente**

```lua
local retval = GetControlInstructionalButton(padIndex, control, p2)
```
```c
char* GET_CONTROL_INSTRUCTIONAL_BUTTON(int padIndex, int control, BOOL p2);
```

**Parámetros**

- `padIndex` (`int`)
- `control` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `char*`

**Descripción oficial:**

```
formerly called _GET_CONTROL_ACTION_NAME incorrectly  
p2 appears to always be true.  
p2 is unused variable in function.  
EG:  
GET_CONTROL_INSTRUCTIONAL_BUTTON (2, 201, 1) /*INPUT_FRONTEND_ACCEPT (e.g. Enter button)*/  
GET_CONTROL_INSTRUCTIONAL_BUTTON (2, 202, 1) /*INPUT_FRONTEND_CANCEL (e.g. ESC button)*/  
GET_CONTROL_INSTRUCTIONAL_BUTTON (2, 51, 1) /*INPUT_CONTEXT (e.g. E button)*/  
gtaforums.com/topic/819070-c-draw-instructional-buttons-scaleform-movie/#entry1068197378  
0, 1 and 2 used in the scripts. 0 is by far the most common of them.  
```

**Nombres antiguos (alias):** `0x0499D7B09FC9B407` (`N_0x0499d7b09fc9b407`)

---
### GetControlNormal

`GET_CONTROL_NORMAL` · hash `0xEC3C9B8D5327B563` · jhash `0x5DE226A5` · **Cliente**

```lua
local retval = GetControlNormal(padIndex, control)
```
```c
float GET_CONTROL_NORMAL(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `float` — Returns the value of [`GET_CONTROL_VALUE`](#getcontrolvalue) normalized, i.e. a real number value between -1.0 and 1.0

---
### GetControlUnboundNormal

`GET_CONTROL_UNBOUND_NORMAL` · hash `0x5B84D09CEC5209C5` · jhash `0xC49343BB` · **Cliente**

```lua
local retval = GetControlUnboundNormal(padIndex, control)
```
```c
float GET_CONTROL_UNBOUND_NORMAL(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `float`

**Descripción oficial:**

```
Seems to return values between -1 and 1 for controls like gas and steering.
```

**Nombres antiguos (alias):** `0x5B84D09CEC5209C5` (`N_0x5b84d09cec5209c5`)

---
### GetControlValue

`GET_CONTROL_VALUE` · hash `0xD95E79E8686D2C27` · jhash `0xC526F3C6` · **Cliente**

```lua
local retval = GetControlValue(padIndex, control)
```
```c
int GET_CONTROL_VALUE(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `int`

---
### GetDisabledControlNormal

`GET_DISABLED_CONTROL_NORMAL` · hash `0x11E65974A982637C` · jhash `0x66FF4FAA` · **Cliente**

```lua
local retval = GetDisabledControlNormal(padIndex, control)
```
```c
float GET_DISABLED_CONTROL_NORMAL(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `float`

---
### GetDisabledControlUnboundNormal

`GET_DISABLED_CONTROL_UNBOUND_NORMAL` · hash `0x4F8A26A890FD62FB` · jhash `0xF2A65A4C` · **Cliente**

```lua
local retval = GetDisabledControlUnboundNormal(padIndex, control)
```
```c
float GET_DISABLED_CONTROL_UNBOUND_NORMAL(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x4F8A26A890FD62FB` (`N_0x4f8a26a890fd62fb`)

---
### GetIsUsingAlternateDriveby

`GET_IS_USING_ALTERNATE_DRIVEBY` · hash `0x0F70731BACCFBB96` · jhash `0xC1AFABD5` · **Cliente**

```lua
local retval = GetIsUsingAlternateDriveby()
```
```c
BOOL GET_IS_USING_ALTERNATE_DRIVEBY();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns profile setting 225.
```

**Nombres antiguos (alias):** `0x0F70731BACCFBB96` (`N_0x0f70731baccfbb96`)

---
### GetLocalPlayerAimState

`GET_LOCAL_PLAYER_AIM_STATE` · hash `0xBB41AFBBBC0A0287` · jhash `0x81802053` · **Cliente**

```lua
local retval = GetLocalPlayerAimState()
```
```c
int GET_LOCAL_PLAYER_AIM_STATE();
```

**Devuelve:** `int`

**Descripción oficial:**

Returns the local player's targeting mode. See [`SET_PLAYER_TARGETING_MODE`](PLAYER.md#setplayertargetingmode).

---
### GetLocalPlayerGamepadAimState

`GET_LOCAL_PLAYER_GAMEPAD_AIM_STATE` · hash `0x59B9A7AF4C95133C` · **Cliente**

```lua
local retval = GetLocalPlayerGamepadAimState()
```
```c
int GET_LOCAL_PLAYER_GAMEPAD_AIM_STATE();
```

**Devuelve:** `int` — Returns the local player's targeting mode. See [`SET_PLAYER_TARGETING_MODE`](PLAYER.md#setplayertargetingmode).

**Descripción oficial:**

Same behavior as [`GET_LOCAL_PLAYER_AIM_STATE`](#getlocalplayeraimstate) but will also return if player using a keyboard.

**Nombres antiguos (alias):** `0x59B9A7AF4C95133C` (`N_0x59b9a7af4c95133c`), `_GET_LOCAL_PLAYER_AIM_STATE_2` (`GetLocalPlayerAimState_2`)

---
### GetTimeSinceLastInput

`_GET_TIME_SINCE_LAST_INPUT` · hash `0xD7D22F5592AED8BA` · jhash `0x0E8EF929` · **Cliente**

```lua
local retval = GetTimeSinceLastInput(padIndex)
```
```c
int _GET_TIME_SINCE_LAST_INPUT(int padIndex);
```

**Parámetros**

- `padIndex` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
The number of milliseconds since last padIndex registered pressed
```

**Nombres antiguos (alias):** `0xD7D22F5592AED8BA` (`N_0xd7d22f5592aed8ba`)

---
### IsControlEnabled

`IS_CONTROL_ENABLED` · hash `0x1CEA6BFDF248E5D9` · jhash `0x9174AF84` · **Cliente**

```lua
local retval = IsControlEnabled(padIndex, control)
```
```c
BOOL IS_CONTROL_ENABLED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL`

---
### IsControlJustPressed

`IS_CONTROL_JUST_PRESSED` · hash `0x580417101DDB492F` · jhash `0x4487F579` · **Cliente**

```lua
local retval = IsControlJustPressed(padIndex, control)
```
```c
BOOL IS_CONTROL_JUST_PRESSED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL` — True if the control was pressed.

**Descripción oficial:**

Returns whether a control was newly pressed since the last check.

---
### IsControlJustReleased

`IS_CONTROL_JUST_RELEASED` · hash `0x50F940259D3841E6` · jhash `0x2314444B` · **Cliente**

```lua
local retval = IsControlJustReleased(padIndex, control)
```
```c
BOOL IS_CONTROL_JUST_RELEASED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL` — True if the control was recently released.

**Descripción oficial:**

Returns whether a control was newly released since the last check.

---
### IsControlPressed

`IS_CONTROL_PRESSED` · hash `0xF3A21BCD95725A4A` · jhash `0x517A4384` · **Cliente**

```lua
local retval = IsControlPressed(padIndex, control)
```
```c
BOOL IS_CONTROL_PRESSED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL` — True if the control was pressed.

**Descripción oficial:**

Returns whether a control is currently pressed.

---
### IsControlReleased

`IS_CONTROL_RELEASED` · hash `0x648EE3E7F38877DD` · jhash `0x1F91A06E` · **Cliente**

```lua
local retval = IsControlReleased(padIndex, control)
```
```c
BOOL IS_CONTROL_RELEASED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL` — True if the control is not pressed.

**Descripción oficial:**

Returns whether a control is currently *not* pressed.

---
### IsDisabledControlJustPressed

`IS_DISABLED_CONTROL_JUST_PRESSED` · hash `0x91AEF906BCA88877` · jhash `0xEE6ABD32` · **Cliente**

```lua
local retval = IsDisabledControlJustPressed(padIndex, control)
```
```c
BOOL IS_DISABLED_CONTROL_JUST_PRESSED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL`

---
### IsDisabledControlJustReleased

`IS_DISABLED_CONTROL_JUST_RELEASED` · hash `0x305C8DCD79DA8B0F` · jhash `0xD6A679E1` · **Cliente**

```lua
local retval = IsDisabledControlJustReleased(padIndex, control)
```
```c
BOOL IS_DISABLED_CONTROL_JUST_RELEASED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL`

---
### IsDisabledControlPressed

`IS_DISABLED_CONTROL_PRESSED` · hash `0xE2587F8CBBD87B1D` · jhash `0x32A93544` · **Cliente**

```lua
local retval = IsDisabledControlPressed(padIndex, control)
```
```c
BOOL IS_DISABLED_CONTROL_PRESSED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL`

---
### IsDisabledControlReleased

`_IS_DISABLED_CONTROL_RELEASED` · hash `0xFB6C4072E9A32E92` · **Cliente**

```lua
local retval = IsDisabledControlReleased(padIndex, control)
```
```c
BOOL _IS_DISABLED_CONTROL_RELEASED(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFB6C4072E9A32E92` (`N_0xfb6c4072e9a32e92`)

---
### IsLookInverted

`IS_LOOK_INVERTED` · hash `0x77B612531280010D` · jhash `0x313434B2` · **Cliente**

```lua
local retval = IsLookInverted()
```
```c
BOOL IS_LOOK_INVERTED();
```

**Devuelve:** `BOOL`

---
### IsUsingKeyboard

`_IS_USING_KEYBOARD` · hash `0xA571D46727E2B718` · **Cliente**

```lua
local retval = IsUsingKeyboard(padIndex)
```
```c
BOOL _IS_USING_KEYBOARD(int padIndex);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_GET_LAST_INPUT_METHOD` (`GetLastInputMethod`), `_IS_INPUT_DISABLED` (`IsInputDisabled`)

---
### IsUsingKeyboard_2

`_IS_USING_KEYBOARD_2` · hash `0x13337B38DB572509` · **Cliente**

```lua
local retval = IsUsingKeyboard_2(padIndex)
```
```c
BOOL _IS_USING_KEYBOARD_2(int padIndex);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x13337B38DB572509` (`N_0x13337b38db572509`), `_IS_INPUT_JUST_DISABLED` (`IsInputJustDisabled`)

---
### N_0x14d29bb12d47f68c

`0x14D29BB12D47F68C` · hash `0x14D29BB12D47F68C` · **Cliente**

```lua
N_0x14d29bb12d47f68c(p0, p1, p2, p3, p4)
```
```c
void 0x14D29BB12D47F68C(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x23f09eadc01449d6

`0x23F09EADC01449D6` · hash `0x23F09EADC01449D6` · **Cliente**

```lua
local retval = N_0x23f09eadc01449d6(padIndex)
```
```c
BOOL 0x23F09EADC01449D6(int padIndex);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).

**Devuelve:** `BOOL`

**Descripción oficial:**

Hardcoded to return false.

---
### N_0x25aaa32bdc98f2a3

`0x25AAA32BDC98F2A3` · hash `0x25AAA32BDC98F2A3` · **Cliente**

```lua
local retval = N_0x25aaa32bdc98f2a3()
```
```c
Any 0x25AAA32BDC98F2A3();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

---
### N_0x5b73c77d9eb66e24

`0x5B73C77D9EB66E24` · hash `0x5B73C77D9EB66E24` · **Cliente**

```lua
N_0x5b73c77d9eb66e24(p0)
```
```c
void 0x5B73C77D9EB66E24(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x6cd79468a1e595c6

`0x6CD79468A1E595C6` · hash `0x6CD79468A1E595C6` · **Cliente**

```lua
local retval = N_0x6cd79468a1e595c6(padIndex)
```
```c
BOOL 0x6CD79468A1E595C6(int padIndex);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).

**Devuelve:** `BOOL`

---
### N_0xa0cefcea390aab9b

`0xA0CEFCEA390AAB9B` · hash `0xA0CEFCEA390AAB9B` · **Cliente**

```lua
N_0xa0cefcea390aab9b(p0)
```
```c
void 0xA0CEFCEA390AAB9B(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xcb0360efefb2580d

`0xCB0360EFEFB2580D` · hash `0xCB0360EFEFB2580D` · **Cliente**

```lua
N_0xcb0360efefb2580d(padIndex)
```
```c
void 0xCB0360EFEFB2580D(int padIndex);
```

**Parámetros**

- `padIndex` (`int`)

**Devuelve:** `void`

---
### N_0xe1615ec03b3bb4fd

`0xE1615EC03B3BB4FD` · hash `0xE1615EC03B3BB4FD` · **Cliente**

```lua
local retval = N_0xe1615ec03b3bb4fd()
```
```c
BOOL 0xE1615EC03B3BB4FD();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Used with IS_LOOK_INVERTED() and negates its affect.
--
Not sure how the person above got that description, but here's an actual example:
if (PAD::_GET_LAST_INPUT_METHOD(2)) {
    if (a_5) {
        if (PAD::IS_LOOK_INVERTED()) {
            a_3 *= -1;
        }
        if (PAD::_E1615EC03B3BB4FD()) {
            a_3 *= -1;
        }
    }
}
```

---
### N_0xf239400e16c23e08

`0xF239400E16C23E08` · hash `0xF239400E16C23E08` · jhash `0x7D65EB6E` · **Cliente**

```lua
N_0xf239400e16c23e08(padIndex, p1)
```
```c
void 0xF239400E16C23E08(int padIndex, int p1);
```

**Parámetros**

- `padIndex` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

---
### ResetInputMappingScheme

`_RESET_INPUT_MAPPING_SCHEME` · hash `0x643ED62D5EA3BEBD` · jhash `0x42140FF9` · **Cliente**

```lua
ResetInputMappingScheme()
```
```c
void _RESET_INPUT_MAPPING_SCHEME();
```

**Devuelve:** `void`

**Descripción oficial:**

```
S*
```

**Nombres antiguos (alias):** `0x643ED62D5EA3BEBD` (`N_0x643ed62d5ea3bebd`)

---
### SetControlLightEffectColor

`_SET_CONTROL_LIGHT_EFFECT_COLOR` · hash `0x8290252FFF36ACB5` · **Cliente**

```lua
SetControlLightEffectColor(padIndex, red, green, blue)
```
```c
void _SET_CONTROL_LIGHT_EFFECT_COLOR(int padIndex, int red, int green, int blue);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8290252FFF36ACB5` (`N_0x8290252fff36acb5`), `_SET_CONTROL_GROUP_COLOR` (`SetControlGroupColor`)

---
### SetControlNormal

`_SET_CONTROL_NORMAL` · hash `0xE8A25867FBA3B05E` · **Cliente**

```lua
local retval = SetControlNormal(padIndex, control, amount)
```
```c
BOOL _SET_CONTROL_NORMAL(int padIndex, int control, float amount);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.
- `amount` (`float`): An unbounded normal value.

**Devuelve:** `BOOL`

**Descripción oficial:**

This is for simulating player input.

**Nombres antiguos (alias):** `0xE8A25867FBA3B05E` (`N_0xe8a25867fba3b05e`)

---
### SetCursorLocation

`_SET_CURSOR_LOCATION` · hash `0xFC695459D4D0E219` · **Cliente**

```lua
local retval = SetCursorLocation(x, y)
```
```c
BOOL _SET_CURSOR_LOCATION(float x, float y);
```

**Parámetros**

- `x` (`float`): Horizontal position (0.0 = left, 1.0 = right)
- `y` (`float`): Vertical position (0.0 = top, 1.0 = bottom)

**Devuelve:** `BOOL` — Returns `true` if the cursor position was successfully set, otherwise `false`.

**Descripción oficial:**

Sets the position of the mouse cursor within the current UI context (e.g., NUI menu or pause menu).\
Coordinates must be in the range 0.0 to 1.0, where (0.5, 0.5) represents the center of the screen.

**Nombres antiguos (alias):** `0xFC695459D4D0E219` (`N_0xfc695459d4d0e219`)

---
### SetInputExclusive

`SET_INPUT_EXCLUSIVE` · hash `0xEDE476E5EE29EDB1` · jhash `0x4E8E29E6` · **Cliente**

```lua
SetInputExclusive(padIndex, control)
```
```c
void SET_INPUT_EXCLUSIVE(int padIndex, int control);
```

**Parámetros**

- `padIndex` (`int`): The control system instance to use. See [`ENABLE_ALL_CONTROL_ACTIONS`](#enableallcontrolactions).
- `control` (`int`): The [control ID](https://docs.fivem.net/docs/game-references/controls/#controls) to check.

**Devuelve:** `void`

---
### SetPadShake

`SET_PAD_SHAKE` · hash `0x48B3886C1358D0D5` · jhash `0x5D38BD2F` · **Cliente**

```lua
SetPadShake(padIndex, duration, frequency)
```
```c
void SET_PAD_SHAKE(int padIndex, int duration, int frequency);
```

**Parámetros**

- `padIndex` (`int`)
- `duration` (`int`)
- `frequency` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
p0 always seems to be 0  
duration in milliseconds   
frequency should range from about 10 (slow vibration) to 255 (very fast)  
example:  
SET_PAD_SHAKE(0, 100, 200);  
```

---
### SetPlayerpadShakesWhenControllerDisabled

`SET_PLAYERPAD_SHAKES_WHEN_CONTROLLER_DISABLED` · hash `0x798FDEB5B1575088` · jhash `0xA86BD91F` · **Cliente**

```lua
SetPlayerpadShakesWhenControllerDisabled(toggle)
```
```c
void SET_PLAYERPAD_SHAKES_WHEN_CONTROLLER_DISABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### StopPadShake

`STOP_PAD_SHAKE` · hash `0x38C16A305E8CDC8D` · jhash `0x8F75657E` · **Cliente**

```lua
StopPadShake(padIndex)
```
```c
void STOP_PAD_SHAKE(int padIndex);
```

**Parámetros**

- `padIndex` (`int`)

**Devuelve:** `void`

---
### SwitchToInputMappingScheme

`_SWITCH_TO_INPUT_MAPPING_SCHEME` · hash `0x3D42B92563939375` · jhash `0xD2C80B2E` · **Cliente**

```lua
local retval = SwitchToInputMappingScheme(name)
```
```c
BOOL _SWITCH_TO_INPUT_MAPPING_SCHEME(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Used in carsteal3 script with p0 = "Carsteal4_spycar".
S*
```

**Nombres antiguos (alias):** `0x3D42B92563939375` (`N_0x3d42b92563939375`)

---
### SwitchToInputMappingScheme_2

`_SWITCH_TO_INPUT_MAPPING_SCHEME_2` · hash `0x4683149ED1DDE7A1` · jhash `0xBBFC9050` · **Cliente**

```lua
local retval = SwitchToInputMappingScheme_2(name)
```
```c
BOOL _SWITCH_TO_INPUT_MAPPING_SCHEME_2(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Same as 0x3D42B92563939375

S*
```

**Nombres antiguos (alias):** `0x4683149ED1DDE7A1` (`N_0x4683149ed1dde7a1`)

---
