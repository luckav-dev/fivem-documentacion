# Natives de GTA V — MOBILE

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `MOBILE`: **25** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`CanPhoneBeSeenOnScreen`](#canphonebeseenonscreen) · [`CellCamActivate`](#cellcamactivate) · [`CellCamActivateSelfieMode`](#cellcamactivateselfiemode) · [`CellCamIsCharVisibleNoFaceCheck`](#cellcamischarvisiblenofacecheck) · [`CellCamMoveFinger`](#cellcammovefinger) · [`CellCamSetDistance`](#cellcamsetdistance) · [`CellCamSetHeadHeight`](#cellcamsetheadheight) · [`CellCamSetHeadPitch`](#cellcamsetheadpitch) · [`CellCamSetHeadRoll`](#cellcamsetheadroll) · [`CellCamSetHorizontalOffset`](#cellcamsethorizontaloffset) · [`CellCamSetLean`](#cellcamsetlean) · [`CellCamSetRoll`](#cellcamsetroll) · [`CellCamSetVerticalOffset`](#cellcamsetverticaloffset) · [`CreateMobilePhone`](#createmobilephone) · [`DestroyMobilePhone`](#destroymobilephone) · [`GetMobilePhonePosition`](#getmobilephoneposition) · [`GetMobilePhoneRenderId`](#getmobilephonerenderid) · [`GetMobilePhoneRotation`](#getmobilephonerotation) · [`N_0xa2ccbe62cd4c91a4`](#n_0xa2ccbe62cd4c91a4) · [`N_0xac2890471901861c`](#n_0xac2890471901861c) · [`ScriptIsMovingMobilePhoneOffscreen`](#scriptismovingmobilephoneoffscreen) · [`SetMobilePhoneDofState`](#setmobilephonedofstate) · [`SetMobilePhonePosition`](#setmobilephoneposition) · [`SetMobilePhoneRotation`](#setmobilephonerotation) · [`SetMobilePhoneScale`](#setmobilephonescale)

---
### CanPhoneBeSeenOnScreen

`CAN_PHONE_BE_SEEN_ON_SCREEN` · hash `0xC4E2813898C97A4B` · jhash `0x5F978584` · **Cliente**

```lua
local retval = CanPhoneBeSeenOnScreen()
```
```c
BOOL CAN_PHONE_BE_SEEN_ON_SCREEN();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This one is weird and seems to return a TRUE state regardless of whether the phone is visible on screen or tucked away.  
I can confirm the above. This function is hard-coded to always return 1.  
```

---
### CellCamActivate

`CELL_CAM_ACTIVATE` · hash `0xFDE8F069C542D126` · jhash `0x234C1AE9` · **Cliente**

```lua
CellCamActivate(active, bGoFirstPerson)
```
```c
void CELL_CAM_ACTIVATE(BOOL active, BOOL bGoFirstPerson);
```

**Parámetros**

- `active` (`BOOL`): Toggle whether the camera should be active.
- `bGoFirstPerson` (`BOOL`): Unused parameter.

**Devuelve:** `void`

**Descripción oficial:**

Activates the cellphone camera. Make sure you have a mobile phone created with [`CREATE_MOBILE_PHONE`](#createmobilephone) or else the camera will not work.

---
### CellCamActivateSelfieMode

`CELL_CAM_ACTIVATE_SELFIE_MODE` · hash `0x015C49A93E3E086E` · jhash `0x4479B304` · **Cliente**

```lua
CellCamActivateSelfieMode(toggle)
```
```c
void CELL_CAM_ACTIVATE_SELFIE_MODE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): True to activate and false to deactivate the selfie mode.

**Devuelve:** `void`

**Descripción oficial:**

Toggles the selfie mode on the cellphone camera. Only visible when the cell phone camera is active.

**Nombres antiguos (alias):** `0x015C49A93E3E086E` (`N_0x015c49a93e3e086e`), `_DISABLE_PHONE_THIS_FRAME` (`DisablePhoneThisFrame`), `_CELL_CAM_DISABLE_THIS_FRAME` (`CellCamDisableThisFrame`)

---
### CellCamIsCharVisibleNoFaceCheck

`CELL_CAM_IS_CHAR_VISIBLE_NO_FACE_CHECK` · hash `0x439E9BC95B7E7FBE` · jhash `0xBEA88097` · **Cliente**

```lua
local retval = CellCamIsCharVisibleNoFaceCheck(entity)
```
```c
BOOL CELL_CAM_IS_CHAR_VISIBLE_NO_FACE_CHECK(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### CellCamMoveFinger

`_CELL_CAM_MOVE_FINGER` · hash `0x95C9E72F3D7DEC9B` · **Cliente**

```lua
CellCamMoveFinger(direction)
```
```c
void _CELL_CAM_MOVE_FINGER(int direction);
```

**Parámetros**

- `direction` (`int`): The direction to swipe to, refer to `eCellInput` enum.

**Devuelve:** `void`

**Descripción oficial:**

Moves the character's finger in a swiping motion when holding a cellphone in their hand through the use of the [CREATE_MOBILE_PHONE](#createmobilephone) native.

```cpp
enum eCellInput {
    CELL_INPUT_NONE = 0,
    CELL_INPUT_UP = 1,
    CELL_INPUT_DOWN = 2,
    CELL_INPUT_LEFT = 3,
    CELL_INPUT_RIGHT = 4,
    CELL_INPUT_SELECT = 5
}
```

**Nombres antiguos (alias):** `_MOVE_FINGER` (`MoveFinger`)

**Ejemplo (lua):**

```lua
CreateThread(function()
	local eCellInput = {
		CELL_INPUT_NONE = 0,
		CELL_INPUT_UP = 1,
		CELL_INPUT_DOWN = 2,
		CELL_INPUT_LEFT = 3,
		CELL_INPUT_RIGHT = 4,
		CELL_INPUT_SELECT = 5
	}
	-- Create a mobile phone object and animate the character
	CreateMobilePhone(eCellInput.CELL_INPUT_NONE)

	Wait(2000)

	-- Swipe up
	CellCamMoveFinger(eCellInput.CELL_INPUT_UP)

	Wait(1500)

	-- Swipe right
	CellCamMoveFinger(eCellInput.CELL_INPUT_RIGHT)

	Wait(1500)

	-- Tap the screen
	CellCamMoveFinger(eCellInput.CELL_INPUT_SELECT)
end)
```

---
### CellCamSetDistance

`_CELL_CAM_SET_DISTANCE` · hash `0x53F4892D18EC90A4` · **Cliente**

```lua
CellCamSetDistance(p0)
```
```c
void _CELL_CAM_SET_DISTANCE(float p0);
```

**Parámetros**

- `p0` (`float`): Value from -1.0 to 1.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x53F4892D18EC90A4` (`N_0x53f4892d18ec90a4`)

---
### CellCamSetHeadHeight

`_CELL_CAM_SET_HEAD_HEIGHT` · hash `0x466DA42C89865553` · jhash `0x66DCD9D2` · **Cliente**

```lua
CellCamSetHeadHeight(p0)
```
```c
void _CELL_CAM_SET_HEAD_HEIGHT(float p0);
```

**Parámetros**

- `p0` (`float`): Value from -1.0 to 0.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x466DA42C89865553` (`N_0x466da42c89865553`)

---
### CellCamSetHeadPitch

`_CELL_CAM_SET_HEAD_PITCH` · hash `0xD6ADE981781FCA09` · **Cliente**

```lua
CellCamSetHeadPitch(p0)
```
```c
void _CELL_CAM_SET_HEAD_PITCH(float p0);
```

**Parámetros**

- `p0` (`float`): Value from -1.0 to 1.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD6ADE981781FCA09` (`N_0xd6ade981781fca09`)

---
### CellCamSetHeadRoll

`_CELL_CAM_SET_HEAD_ROLL` · hash `0xF1E22DC13F5EEBAD` · **Cliente**

```lua
CellCamSetHeadRoll(p0)
```
```c
void _CELL_CAM_SET_HEAD_ROLL(float p0);
```

**Parámetros**

- `p0` (`float`): Value from -1.0 to 1.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF1E22DC13F5EEBAD` (`N_0xf1e22dc13f5eebad`)

---
### CellCamSetHorizontalOffset

`_CELL_CAM_SET_HORIZONTAL_OFFSET` · hash `0x1B0B4AEED5B9B41C` · **Cliente**

```lua
CellCamSetHorizontalOffset(p0)
```
```c
void _CELL_CAM_SET_HORIZONTAL_OFFSET(float p0);
```

**Parámetros**

- `p0` (`float`): Value from -1.0 to 1.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1B0B4AEED5B9B41C` (`N_0x1b0b4aeed5b9b41c`)

---
### CellCamSetLean

`_CELL_CAM_SET_LEAN` · hash `0x44E44169EF70138E` · **Cliente**

```lua
CellCamSetLean(toggle)
```
```c
void _CELL_CAM_SET_LEAN(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
if the bool "Toggle" is "true" so the phone is lean.  
if the bool "Toggle" is "false" so the phone is not lean.  
```

**Nombres antiguos (alias):** `_SET_PHONE_LEAN` (`SetPhoneLean`)

---
### CellCamSetRoll

`_CELL_CAM_SET_ROLL` · hash `0x15E69E2802C24B8D` · **Cliente**

```lua
CellCamSetRoll(p0)
```
```c
void _CELL_CAM_SET_ROLL(float p0);
```

**Parámetros**

- `p0` (`float`): Value from -1.0 to 1.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x15E69E2802C24B8D` (`N_0x15e69e2802c24b8d`)

---
### CellCamSetVerticalOffset

`_CELL_CAM_SET_VERTICAL_OFFSET` · hash `0x3117D84EFA60F77B` · **Cliente**

```lua
CellCamSetVerticalOffset(p0)
```
```c
void _CELL_CAM_SET_VERTICAL_OFFSET(float p0);
```

**Parámetros**

- `p0` (`float`): Value from 0.0 to 2.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3117D84EFA60F77B` (`N_0x3117d84efa60f77b`)

---
### CreateMobilePhone

`CREATE_MOBILE_PHONE` · hash `0xA4E8E696C532FBC7` · jhash `0x5BBC5E23` · **Cliente**

```lua
CreateMobilePhone(phoneType)
```
```c
void CREATE_MOBILE_PHONE(int phoneType);
```

**Parámetros**

- `phoneType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Creates a mobile phone of the specified type.  
Possible phone types:  
0 - Default phone / Michael's phone  
1 - Trevor's phone  
2 - Franklin's phone  
4 - Prologue phone  
These values represent bit flags, so a value of '3' would toggle Trevor and Franklin's phones together, causing unexpected behavior and most likely crash the game.  
```

---
### DestroyMobilePhone

`DESTROY_MOBILE_PHONE` · hash `0x3BC861DF703E5097` · jhash `0x1A65037B` · **Cliente**

```lua
DestroyMobilePhone()
```
```c
void DESTROY_MOBILE_PHONE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Destroys the currently active mobile phone.  
```

---
### GetMobilePhonePosition

`GET_MOBILE_PHONE_POSITION` · hash `0x584FDFDA48805B86` · jhash `0xB2E1E1A0` · **Cliente**

```lua
local position = GetMobilePhonePosition(position)
```
```c
void GET_MOBILE_PHONE_POSITION(Vector3* position);
```

**Parámetros**

- `position` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetMobilePhoneRenderId

`GET_MOBILE_PHONE_RENDER_ID` · hash `0xB4A53E05F68B6FA1` · jhash `0x88E4FECE` · **Cliente**

```lua
local renderId = GetMobilePhoneRenderId(renderId)
```
```c
void GET_MOBILE_PHONE_RENDER_ID(int* renderId);
```

**Parámetros**

- `renderId` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetMobilePhoneRotation

`GET_MOBILE_PHONE_ROTATION` · hash `0x1CEFB61F193070AE` · jhash `0x17A29F23` · **Cliente**

```lua
local rotation = GetMobilePhoneRotation(p1)
```
```c
void GET_MOBILE_PHONE_ROTATION(Vector3* rotation, Vehicle p1);
```

**Parámetros**

- `rotation` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Vehicle`)

**Devuelve:** `void`

---
### N_0xa2ccbe62cd4c91a4

`0xA2CCBE62CD4C91A4` · hash `0xA2CCBE62CD4C91A4` · jhash `0xC273BB4D` · **Cliente**

```lua
local toggle = N_0xa2ccbe62cd4c91a4(toggle)
```
```c
void 0xA2CCBE62CD4C91A4(int* toggle);
```

**Parámetros**

- `toggle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Needs more research. If the "phone_cam12" filter is applied, this function is called with "TRUE"; otherwise, "FALSE".
Example (XBOX 360):
// check current filter selection
if (MISC::ARE_STRINGS_EQUAL(getElem(g_2471024, &l_17, 4), "phone_cam12") != 0)
{
    MOBILE::_0xC273BB4D(0); // FALSE
}
else
{
    MOBILE::_0xC273BB4D(1); // TRUE
}
```

---
### N_0xac2890471901861c

`0xAC2890471901861C` · hash `0xAC2890471901861C` · **Cliente**

```lua
N_0xac2890471901861c(p0)
```
```c
void 0xAC2890471901861C(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### ScriptIsMovingMobilePhoneOffscreen

`SCRIPT_IS_MOVING_MOBILE_PHONE_OFFSCREEN` · hash `0xF511F759238A5122` · jhash `0x29828690` · **Cliente**

```lua
ScriptIsMovingMobilePhoneOffscreen(toggle)
```
```c
void SCRIPT_IS_MOVING_MOBILE_PHONE_OFFSCREEN(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If bool Toggle = true so the mobile is hide to screen.  
If bool Toggle = false so the mobile is show to screen.  
```

---
### SetMobilePhoneDofState

`SET_MOBILE_PHONE_DOF_STATE` · hash `0x375A706A5C2FD084` · **Cliente**

```lua
SetMobilePhoneDofState(toggle)
```
```c
void SET_MOBILE_PHONE_DOF_STATE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): true/false to toggle DOF.

**Devuelve:** `void`

**Descripción oficial:**

Toggles depth of field on the cellphone camera.

**Nombres antiguos (alias):** `0x375A706A5C2FD084` (`N_0x375a706a5c2fd084`), `_SET_MOBILE_PHONE_UNK` (`SetMobilePhoneUnk`)

---
### SetMobilePhonePosition

`SET_MOBILE_PHONE_POSITION` · hash `0x693A5C6D6734085B` · jhash `0x841800B3` · **Cliente**

```lua
SetMobilePhonePosition(posX, posY, posZ)
```
```c
void SET_MOBILE_PHONE_POSITION(float posX, float posY, float posZ);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `void`

---
### SetMobilePhoneRotation

`SET_MOBILE_PHONE_ROTATION` · hash `0xBB779C0CA917E865` · jhash `0x209C28CF` · **Cliente**

```lua
SetMobilePhoneRotation(rotX, rotY, rotZ, p3)
```
```c
void SET_MOBILE_PHONE_ROTATION(float rotX, float rotY, float rotZ, Any p3);
```

**Parámetros**

- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
Last parameter is unknown and always zero.  
```

---
### SetMobilePhoneScale

`SET_MOBILE_PHONE_SCALE` · hash `0xCBDD322A73D6D932` · jhash `0x09BCF1BE` · **Cliente**

```lua
SetMobilePhoneScale(scale)
```
```c
void SET_MOBILE_PHONE_SCALE(float scale);
```

**Parámetros**

- `scale` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
The minimum/default is 500.0f. If you plan to make it bigger set it's position as well. Also this seems to need to be called in a loop as when you close the phone the scale is reset. If not in a loop you'd need to call it everytime before you re-open the phone.  
```

---
