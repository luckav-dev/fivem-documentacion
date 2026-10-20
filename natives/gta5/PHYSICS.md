# Natives de GTA V — PHYSICS

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `PHYSICS`: **49** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivatePhysics`](#activatephysics) · [`AddRope`](#addrope) · [`ApplyImpulseToCloth`](#applyimpulsetocloth) · [`AttachEntitiesToRope`](#attachentitiestorope) · [`AttachRopeToEntity`](#attachropetoentity) · [`BreakEntityGlass`](#breakentityglass) · [`DeleteChildRope`](#deletechildrope) · [`DeleteRope`](#deleterope) · [`DetachRopeFromEntity`](#detachropefromentity) · [`DoesRopeBelongToThisScript`](#doesropebelongtothisscript) · [`DoesRopeExist`](#doesropeexist) · [`GetCgoffset`](#getcgoffset) · [`GetDamping`](#getdamping) · [`GetHasObjectFragInst`](#gethasobjectfraginst) · [`GetRopeLastVertexCoord`](#getropelastvertexcoord) · [`GetRopeVertexCoord`](#getropevertexcoord) · [`GetRopeVertexCount`](#getropevertexcount) · [`LoadRopeData`](#loadropedata) · [`N_0x36ccb9be67b970fd`](#n_0x36ccb9be67b970fd) · [`N_0x84de3b5fb3e666f0`](#n_0x84de3b5fb3e666f0) · [`N_0x9ebd751e5787baf2`](#n_0x9ebd751e5787baf2) · [`N_0xa1ae736541b0fca3`](#n_0xa1ae736541b0fca3) · [`N_0xb1b6216ca2e7b55e`](#n_0xb1b6216ca2e7b55e) · [`N_0xb743f735c03d7810`](#n_0xb743f735c03d7810) · [`N_0xbc0ce682d4d05650`](#n_0xbc0ce682d4d05650) · [`N_0xcc6e963682533882`](#n_0xcc6e963682533882) · [`PinRopeVertex`](#pinropevertex) · [`RopeAreTexturesLoaded`](#ropearetexturesloaded) · [`RopeConvertToSimple`](#ropeconverttosimple) · [`RopeDrawShadowEnabled`](#ropedrawshadowenabled) · [`RopeForceLength`](#ropeforcelength) · [`RopeGetDistanceBetweenEnds`](#ropegetdistancebetweenends) · [`RopeLoadTextures`](#ropeloadtextures) · [`RopeResetLength`](#roperesetlength) · [`RopeSetUpdateOrder`](#ropesetupdateorder) · [`RopeSetUpdatePinverts`](#ropesetupdatepinverts) · [`RopeUnloadTextures`](#ropeunloadtextures) · [`SetCgAtBoundcenter`](#setcgatboundcenter) · [`SetCgoffset`](#setcgoffset) · [`SetDamping`](#setdamping) · [`SetDisableBreaking`](#setdisablebreaking) · [`SetDisableFragDamage`](#setdisablefragdamage) · [`SetEntityProofUnk`](#setentityproofunk) · [`SetLaunchControlEnabled`](#setlaunchcontrolenabled) · [`StartRopeUnwindingFront`](#startropeunwindingfront) · [`StartRopeWinding`](#startropewinding) · [`StopRopeUnwindingFront`](#stopropeunwindingfront) · [`StopRopeWinding`](#stopropewinding) · [`UnpinRopeVertex`](#unpinropevertex)

---
### ActivatePhysics

`ACTIVATE_PHYSICS` · hash `0x710311ADF0E20730` · jhash `0x031711B8` · **Cliente**

```lua
ActivatePhysics(entity)
```
```c
void ACTIVATE_PHYSICS(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### AddRope

`ADD_ROPE` · hash `0xE832D760399EB220` · jhash `0xA592EC74` · **Cliente**

```lua
local retval, unkPtr = AddRope(x, y, z, rotX, rotY, rotZ, maxLength, ropeType, initLength, minLength, lengthChangeRate, onlyPPU, collisionOn, lockFromFront, timeMultiplier, breakable, unkPtr)
```
```c
int ADD_ROPE(float x, float y, float z, float rotX, float rotY, float rotZ, float maxLength, int ropeType, float initLength, float minLength, float lengthChangeRate, BOOL onlyPPU, BOOL collisionOn, BOOL lockFromFront, float timeMultiplier, BOOL breakable, Any* unkPtr);
```

**Parámetros**

- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `rotX` (`float`): Rotation X component.
- `rotY` (`float`): Rotation Y component.
- `rotZ` (`float`): Rotation Z component.
- `maxLength` (`float`): The maximum length the rope can droop.
- `ropeType` (`int`): The zero-based index of the entry in the `ropedata.xml` file. *NOTE: Using an index which does not exist will crash the game. As of game build 3258, valid values are from `0` to `7` inclusive.*
- `initLength` (`float`): The initial length of the rope.
- `minLength` (`float`): The minimum length the rope can be.
- `lengthChangeRate` (`float`): The speed in which the rope will wind if winding is started.
- `onlyPPU` (`BOOL`)
- `collisionOn` (`BOOL`): Whether the rope should have collision. In original scripts this is followed by a LoadRopeData call when set.
- `lockFromFront` (`BOOL`): If max length is zero, and this is set to false the rope will become rigid (it will force a specific distance, what ever length is, between the objects).
- `timeMultiplier` (`float`): The speed as which physics should run at. 1.0f is normal, 2.0f is twice as fast, -1.0f is time going backwards. This can affect gravity, etc.
- `breakable` (`BOOL`): Whether shooting the rope will break it.
- `unkPtr` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: Unknown pointer, always 0 in original scrips.

**Devuelve:** `int` — A script handle for the rope

**Descripción oficial:**

```
Creates a rope at the specific position, that extends in the specified direction when not attached to any entities.
__
Rope does NOT interact with anything you attach it to, in some cases it make interact with the world AFTER it breaks (seems to occur if you set the type to -1).
Rope will sometimes contract and fall to the ground like you'd expect it to, but since it doesn't interact with the world the effect is just jaring.
```

There are 8 different rope types in the base game. Full rope data can be found in `ropedata.xml`.

```cpp
enum ePhysicsRopeType {
    RopeThin = 0, // Verticies: 1, Radius: 0.03, Textures: rope & rope_n
    RopeWire6 = 1, // Verticies: 4, Radius: 0.015, Textures: steel_cable & steel_cable_n
    RopeWire32 = 2, // Verticies: 32, Radius: 0.025, Textures: steel_cable & steel_cable_n
    RopeMesh = 3, // Verticies: 6, Radius: 0.03, Textures: rope & rope_n
    RopeThinWire32 = 4, // Verticies: 32, Radius: 0.01, Textures: rope & rope_n
    RopeReins = 5, // Verticies: 32, Radius: 0.005, Textures: rope & rope_n
    RopeThin4 = 6, // Verticies: 4, Radius: 0.03, Textures: rope & rope_n
    RopeWire64 = 7 // Verticies: 64, Radius: 0.025, Textures: steel_cable & steel_cable_n
}
```

**Ejemplo (lua):**

```lua
local function cleanup_rope_textures()
	-- we only want to cleanup if there are no other ropes still left on the map
	-- otherwise we'll make them go invisible.
	if #GetAllRopes() == 0 then
		-- there are no ropes on the map, we're safe to unload the textures.
		RopeUnloadTextures()
	end
end

CreateThread(function()
	-- if textures aren't loaded then we need to load them
	if not RopeAreTexturesLoaded() then
		-- load the textures so we can see the rope
		RopeLoadTextures()
		while not RopeAreTexturesLoaded() do
			Wait(0)
		end
	end

	-- Create a rope and store the handle
	local rope = AddRope(-2096.096, -311.906, 14.51, 0.0, 0.0, 0.0, 10.0, 1, 10.0, 0.0, 1.0, false, false, false, 1.0, false, 0)
	-- Check if the rope exists.
	if not DoesRopeExist(rope) then
		cleanup_rope_textures()
		-- If the rope does not exist, end the execution of the code here.
		return
	end
	-- Let the rope exist for 3 seconds
	Wait(3000)
	-- Delete the rope!
	DeleteRope(rope)
	cleanup_rope_textures()
end)
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

async Task CreateRope()
{
    // wait for the textures to be loaded before we create the rope,
    // otherwise it will be invisible.
    bool isLoadedByAnotherScript = RopeAreTexturesLoaded();
    if (!isLoadedByAnotherScript)
    {
        RopeLoadTextures();
        while (!RopeAreTexturesLoaded())
        {
            await BaseScript.Delay(0);
        }
    }

    /// <summary>
    /// Unloads the rope texture if we were the script that requested it.
    /// NOTE: This is bug prone, if possible you should do your own reference
    /// counting via global state bags.
    /// </summary>
    void CleanupRopeTextures(bool alreadyLoadedByOtherScript)
    {
        // if we were the script to load the textures then we want to cleanup
        // the textures,
        if (!alreadyLoadedByOtherScript)
        {
            RopeUnloadTextures();
        }
    }

    // not used by anything
    int _unusedStringPtr = 0;

    Vector3 ropePosition = new Vector3(-2096.09f, -311.90f, 14.51f);
    Vector3 ropeRotation = Vector3.Zero;

    // Create a rope and store the handle
    int ropehandle = AddRope(
            ropePosition.X,
            ropePosition.Y,
            ropePosition.Z,
            ropeRotation.X,
            ropeRotation.Y,
            ropeRotation.Z,
            10f /* max length */,
            1 /* rope type */,
            10f /* init length */,
            0.5f /* min length */,
            0.5f /* length change rate */,
            false /* ppu only */,
            false /* collision on */,
            false /* lock from front */,
            1f /* time multiplier */,
            false /* breakable */,
            ref _unusedStringPtr /* unused */
    );

    // Check if the rope exists.
    if (!DoesRopeExist(ref ropehandle))
    {
        CleanupRopeTextures(isLoadedByAnotherScript);
        // whoops, the rope doesn't exist, we don't want to do
        // anything with an invalid reference
        return;
    }

    // We want to see the rope for 3 seconds
    await BaseScript.Delay(3000);

    // begone rope!
    DeleteRope(ref ropehandle);
    CleanupRopeTextures(isLoadedByAnotherScript);
}
```

---
### ApplyImpulseToCloth

`APPLY_IMPULSE_TO_CLOTH` · hash `0xE37F721824571784` · jhash `0xA2A5C9FE` · **Cliente**

```lua
ApplyImpulseToCloth(posX, posY, posZ, vecX, vecY, vecZ, impulse)
```
```c
void APPLY_IMPULSE_TO_CLOTH(float posX, float posY, float posZ, float vecX, float vecY, float vecZ, float impulse);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `vecX` (`float`)
- `vecY` (`float`)
- `vecZ` (`float`)
- `impulse` (`float`)

**Devuelve:** `void`

---
### AttachEntitiesToRope

`ATTACH_ENTITIES_TO_ROPE` · hash `0x3D95EC8B6D940AC3` · jhash `0x7508668F` · **Cliente**

```lua
AttachEntitiesToRope(ropeId, ent1, ent2, ent1_x, ent1_y, ent1_z, ent2_x, ent2_y, ent2_z, length, p10, p11, boneName1, boneName2)
```
```c
void ATTACH_ENTITIES_TO_ROPE(int ropeId, Entity ent1, Entity ent2, float ent1_x, float ent1_y, float ent1_z, float ent2_x, float ent2_y, float ent2_z, float length, BOOL p10, BOOL p11, char* boneName1, char* boneName2);
```

**Parámetros**

- `ropeId` (`int`)
- `ent1` (`Entity`)
- `ent2` (`Entity`)
- `ent1_x` (`float`)
- `ent1_y` (`float`)
- `ent1_z` (`float`)
- `ent2_x` (`float`)
- `ent2_y` (`float`)
- `ent2_z` (`float`)
- `length` (`float`)
- `p10` (`BOOL`)
- `p11` (`BOOL`)
- `boneName1` (`char*`)
- `boneName2` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Attaches entity 1 to entity 2.  
```

---
### AttachRopeToEntity

`ATTACH_ROPE_TO_ENTITY` · hash `0x4B490A6832559A65` · jhash `0xB25D9536` · **Cliente**

```lua
AttachRopeToEntity(ropeId, entity, x, y, z, p5)
```
```c
void ATTACH_ROPE_TO_ENTITY(int ropeId, Entity entity, float x, float y, float z, BOOL p5);
```

**Parámetros**

- `ropeId` (`int`)
- `entity` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
The position supplied can be anywhere, and the entity should anchor relative to that point from it's origin.  
```

---
### BreakEntityGlass

`BREAK_ENTITY_GLASS` · hash `0x2E648D16F6E308F3` · jhash `0xD0E0402F` · **Cliente**

```lua
BreakEntityGlass(entity, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
```
```c
void BREAK_ENTITY_GLASS(Entity entity, float p1, float p2, float p3, float p4, float p5, float p6, float p7, float p8, Any p9, BOOL p10);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)
- `p8` (`float`)
- `p9` (`Any`)
- `p10` (`BOOL`)

**Devuelve:** `void`

---
### DeleteChildRope

`DELETE_CHILD_ROPE` · hash `0xAA5D6B1888E4DB20` · jhash `0xB19B4706` · **Cliente**

```lua
DeleteChildRope(ropeId)
```
```c
void DELETE_CHILD_ROPE(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `void`

---
### DeleteRope

`DELETE_ROPE` · hash `0x52B4829281364649` · jhash `0x748D72AF` · **Cliente**

```lua
local ropeId = DeleteRope(ropeId)
```
```c
void DELETE_ROPE(int* ropeId);
```

**Parámetros**

- `ropeId` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The handle of the rope to delete

**Devuelve:** `void`

**Descripción oficial:**

Deletes the rope with the specified handle.

You should check if the rope exists before trying to delete it, see [DOES_ROPE_EXIST](#doesropeexist).

For an example on how to use this native please refer to [ADD_ROPE](#addrope)

---
### DetachRopeFromEntity

`DETACH_ROPE_FROM_ENTITY` · hash `0xBCF3026912A8647D` · jhash `0x3E720BEE` · **Cliente**

```lua
DetachRopeFromEntity(ropeId, entity)
```
```c
void DETACH_ROPE_FROM_ENTITY(int ropeId, Entity entity);
```

**Parámetros**

- `ropeId` (`int`)
- `entity` (`Entity`)

**Devuelve:** `void`

---
### DoesRopeBelongToThisScript

`_DOES_ROPE_BELONG_TO_THIS_SCRIPT` · hash `0x271C9D3ACA5D6409` · **Cliente**

```lua
local retval = DoesRopeBelongToThisScript(ropeId)
```
```c
BOOL _DOES_ROPE_BELONG_TO_THIS_SCRIPT(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Return if the rope was generated or not by the script where the native is called.

**Nombres antiguos (alias):** `0x271C9D3ACA5D6409` (`N_0x271c9d3aca5d6409`)

---
### DoesRopeExist

`DOES_ROPE_EXIST` · hash `0xFD5448BE3111ED96` · jhash `0x66E4A3AC` · **Cliente**

```lua
local retval, ropeId = DoesRopeExist(ropeId)
```
```c
BOOL DOES_ROPE_EXIST(int* ropeId);
```

**Parámetros**

- `ropeId` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The handle of the rope to check

**Devuelve:** `BOOL` — Returns `true` if the rope exists, `false` otherwise.

**Descripción oficial:**

For an example on how to use this native please refer to [ADD_ROPE](#addrope)

---
### GetCgoffset

`GET_CGOFFSET` · hash `0x8214A4B5A7A33612` · jhash `0x49A11F0D` · **Cliente**

```lua
local retval = GetCgoffset(entity)
```
```c
Vector3 GET_CGOFFSET(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vector3`

---
### GetDamping

`GET_DAMPING` · hash `0x8C520A929415BCD2` · **Cliente**

```lua
local retval = GetDamping(entity, type)
```
```c
Vector3 GET_DAMPING(Entity entity, int type);
```

**Parámetros**

- `entity` (`Entity`)
- `type` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### GetHasObjectFragInst

`_GET_HAS_OBJECT_FRAG_INST` · hash `0x0C112765300C7E1E` · **Cliente**

```lua
local retval = GetHasObjectFragInst(object)
```
```c
BOOL _GET_HAS_OBJECT_FRAG_INST(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
GET_*
```

**Nombres antiguos (alias):** `0x0C112765300C7E1E` (`N_0x0c112765300c7e1e`), `_DOES_ENTITY_HAVE_FRAG_INST` (`DoesEntityHaveFragInst`)

---
### GetRopeLastVertexCoord

`GET_ROPE_LAST_VERTEX_COORD` · hash `0x21BB0FBD3E217C2D` · jhash `0x91F6848B` · **Cliente**

```lua
local retval = GetRopeLastVertexCoord(ropeId)
```
```c
Vector3 GET_ROPE_LAST_VERTEX_COORD(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `Vector3`

---
### GetRopeVertexCoord

`GET_ROPE_VERTEX_COORD` · hash `0xEA61CA8E80F09E4D` · jhash `0x84374452` · **Cliente**

```lua
local retval = GetRopeVertexCoord(ropeId, vertex)
```
```c
Vector3 GET_ROPE_VERTEX_COORD(int ropeId, int vertex);
```

**Parámetros**

- `ropeId` (`int`)
- `vertex` (`int`)

**Devuelve:** `Vector3`

---
### GetRopeVertexCount

`GET_ROPE_VERTEX_COUNT` · hash `0x3655F544CD30F0B5` · jhash `0x5131CD2C` · **Cliente**

```lua
local retval = GetRopeVertexCount(ropeId)
```
```c
int GET_ROPE_VERTEX_COUNT(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `int`

---
### LoadRopeData

`LOAD_ROPE_DATA` · hash `0xCBB203C04D1ABD27` · jhash `0x9E8F1644` · **Cliente**

```lua
LoadRopeData(ropeId, rope_preset)
```
```c
void LOAD_ROPE_DATA(int ropeId, char* rope_preset);
```

**Parámetros**

- `ropeId` (`int`)
- `rope_preset` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Rope presets can be found in the gamefiles. One example is "ropeFamily3", it is NOT a hash but rather a string.
```

---
### N_0x36ccb9be67b970fd

`0x36CCB9BE67B970FD` · hash `0x36CCB9BE67B970FD` · jhash `0xC67D5CF6` · **Cliente**

```lua
N_0x36ccb9be67b970fd(ropeId, p1)
```
```c
void 0x36CCB9BE67B970FD(int ropeId, BOOL p1);
```

**Parámetros**

- `ropeId` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
ROPE_*
```

---
### N_0x84de3b5fb3e666f0

`0x84DE3B5FB3E666F0` · hash `0x84DE3B5FB3E666F0` · jhash `0x7A18BB9C` · **Cliente**

```lua
local retval, ropeId = N_0x84de3b5fb3e666f0(ropeId)
```
```c
BOOL 0x84DE3B5FB3E666F0(int* ropeId);
```

**Parámetros**

- `ropeId` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x9ebd751e5787baf2

`0x9EBD751E5787BAF2` · hash `0x9EBD751E5787BAF2` · **Cliente**

```lua
N_0x9ebd751e5787baf2(p0)
```
```c
void 0x9EBD751E5787BAF2(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_*
```

---
### N_0xa1ae736541b0fca3

`0xA1AE736541B0FCA3` · hash `0xA1AE736541B0FCA3` · **Cliente**

```lua
local ropeId = N_0xa1ae736541b0fca3(p1)
```
```c
void 0xA1AE736541B0FCA3(int* ropeId, BOOL p1);
```

**Parámetros**

- `ropeId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

ROPE_\*

```
NativeDB Introduced: v1868
```

---
### N_0xb1b6216ca2e7b55e

`0xB1B6216CA2E7B55E` · hash `0xB1B6216CA2E7B55E` · jhash `0x7C6F7668` · **Cliente**

```lua
N_0xb1b6216ca2e7b55e(p0, p1, p2)
```
```c
void 0xB1B6216CA2E7B55E(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### N_0xb743f735c03d7810

`0xB743F735C03D7810` · hash `0xB743F735C03D7810` · jhash `0x686672DD` · **Cliente**

```lua
N_0xb743f735c03d7810(ropeId, p1)
```
```c
void 0xB743F735C03D7810(int ropeId, int p1);
```

**Parámetros**

- `ropeId` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
ROPE_*
```

---
### N_0xbc0ce682d4d05650

`0xBC0CE682D4D05650` · hash `0xBC0CE682D4D05650` · jhash `0x106BA127` · **Cliente**

```lua
N_0xbc0ce682d4d05650(ropeId, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
```
```c
void 0xBC0CE682D4D05650(int ropeId, int p1, float p2, float p3, float p4, float p5, float p6, float p7, float p8, float p9, float p10, float p11, float p12, float p13);
```

**Parámetros**

- `ropeId` (`int`)
- `p1` (`int`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)
- `p8` (`float`)
- `p9` (`float`)
- `p10` (`float`)
- `p11` (`float`)
- `p12` (`float`)
- `p13` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Most likely ROPE_ATTACH_*  
```

---
### N_0xcc6e963682533882

`0xCC6E963682533882` · hash `0xCC6E963682533882` · **Cliente**

```lua
N_0xcc6e963682533882(object)
```
```c
void 0xCC6E963682533882(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `void`

**Descripción oficial:**

```
RESET_*  
```

---
### PinRopeVertex

`PIN_ROPE_VERTEX` · hash `0x2B320CF14146B69A` · jhash `0xAE1D101B` · **Cliente**

```lua
PinRopeVertex(ropeId, vertex, x, y, z)
```
```c
void PIN_ROPE_VERTEX(int ropeId, int vertex, float x, float y, float z);
```

**Parámetros**

- `ropeId` (`int`)
- `vertex` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### RopeAreTexturesLoaded

`ROPE_ARE_TEXTURES_LOADED` · hash `0xF2D0E6A75CC05597` · jhash `0x5FDC1047` · **Cliente**

```lua
local retval = RopeAreTexturesLoaded()
```
```c
BOOL ROPE_ARE_TEXTURES_LOADED();
```

**Devuelve:** `BOOL`

---
### RopeConvertToSimple

`ROPE_CONVERT_TO_SIMPLE` · hash `0x5389D48EFA2F079A` · jhash `0x43E92628` · **Cliente**

```lua
RopeConvertToSimple(ropeId)
```
```c
void ROPE_CONVERT_TO_SIMPLE(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `void`

---
### RopeDrawShadowEnabled

`ROPE_DRAW_SHADOW_ENABLED` · hash `0xF159A63806BB5BA8` · jhash `0x51523B8C` · **Cliente**

```lua
local ropeId = RopeDrawShadowEnabled(toggle)
```
```c
void ROPE_DRAW_SHADOW_ENABLED(int* ropeId, BOOL toggle);
```

**Parámetros**

- `ropeId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### RopeForceLength

`ROPE_FORCE_LENGTH` · hash `0xD009F759A723DB1B` · jhash `0xABF3130F` · **Cliente**

```lua
RopeForceLength(ropeId, length)
```
```c
void ROPE_FORCE_LENGTH(int ropeId, float length);
```

**Parámetros**

- `ropeId` (`int`)
- `length` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Forces a rope to a certain length.
```

---
### RopeGetDistanceBetweenEnds

`ROPE_GET_DISTANCE_BETWEEN_ENDS` · hash `0x73040398DFF9A4A6` · jhash `0xFD309DC8` · **Cliente**

```lua
local retval = RopeGetDistanceBetweenEnds(ropeId)
```
```c
float ROPE_GET_DISTANCE_BETWEEN_ENDS(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `_GET_ROPE_LENGTH` (`GetRopeLength`)

---
### RopeLoadTextures

`ROPE_LOAD_TEXTURES` · hash `0x9B9039DBF2D258C1` · jhash `0xBA97CE91` · **Cliente**

```lua
RopeLoadTextures()
```
```c
void ROPE_LOAD_TEXTURES();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Loads rope textures for all ropes in the current scene.
```

---
### RopeResetLength

`ROPE_RESET_LENGTH` · hash `0xC16DE94D9BEA14A0` · jhash `0xC8A423A3` · **Cliente**

```lua
RopeResetLength(ropeId, length)
```
```c
void ROPE_RESET_LENGTH(int ropeId, float length);
```

**Parámetros**

- `ropeId` (`int`)
- `length` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Reset a rope to a certain length.  
```

---
### RopeSetUpdateOrder

`ROPE_SET_UPDATE_ORDER` · hash `0xDC57A637A20006ED` · jhash `0x80DB77A7` · **Cliente**

```lua
RopeSetUpdateOrder(ropeId, p1)
```
```c
void ROPE_SET_UPDATE_ORDER(int ropeId, Any p1);
```

**Parámetros**

- `ropeId` (`int`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDC57A637A20006ED` (`N_0xdc57a637a20006ed`)

---
### RopeSetUpdatePinverts

`ROPE_SET_UPDATE_PINVERTS` · hash `0xC8D667EE52114ABA` · jhash `0xEAF291A0` · **Cliente**

```lua
RopeSetUpdatePinverts(ropeId)
```
```c
void ROPE_SET_UPDATE_PINVERTS(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `void`

---
### RopeUnloadTextures

`ROPE_UNLOAD_TEXTURES` · hash `0x6CE36C35C1AC8163` · jhash `0x584463E0` · **Cliente**

```lua
RopeUnloadTextures()
```
```c
void ROPE_UNLOAD_TEXTURES();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Unloads rope textures for all ropes in the current scene.
```

---
### SetCgAtBoundcenter

`SET_CG_AT_BOUNDCENTER` · hash `0xBE520D9761FF811F` · jhash `0xA5B55421` · **Cliente**

```lua
SetCgAtBoundcenter(entity)
```
```c
void SET_CG_AT_BOUNDCENTER(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### SetCgoffset

`SET_CGOFFSET` · hash `0xD8FA3908D7B86904` · jhash `0x59910AB2` · **Cliente**

```lua
SetCgoffset(entity, x, y, z)
```
```c
void SET_CGOFFSET(Entity entity, float x, float y, float z);
```

**Parámetros**

- `entity` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### SetDamping

`SET_DAMPING` · hash `0xEEA3B200A6FEB65B` · jhash `0xCFB37773` · **Cliente**

```lua
SetDamping(entity, vertex, value)
```
```c
void SET_DAMPING(Entity entity, int vertex, float value);
```

**Parámetros**

- `entity` (`Entity`)
- `vertex` (`int`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetDisableBreaking

`SET_DISABLE_BREAKING` · hash `0x5CEC1A84620E7D5B` · jhash `0xEE77C326` · **Cliente**

```lua
SetDisableBreaking(object, toggle)
```
```c
void SET_DISABLE_BREAKING(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetDisableFragDamage

`SET_DISABLE_FRAG_DAMAGE` · hash `0x01BA3AED21C16CFB` · jhash `0x97269DC8` · **Cliente**

```lua
SetDisableFragDamage(object, toggle)
```
```c
void SET_DISABLE_FRAG_DAMAGE(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityProofUnk

`_SET_ENTITY_PROOF_UNK` · hash `0x15F944730C832252` · **Cliente**

```lua
SetEntityProofUnk(entity, toggle)
```
```c
void _SET_ENTITY_PROOF_UNK(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x15F944730C832252` (`N_0x15f944730c832252`)

---
### SetLaunchControlEnabled

`_SET_LAUNCH_CONTROL_ENABLED` · hash `0xAA6A6098851C396F` · **Cliente**

```lua
SetLaunchControlEnabled(toggle)
```
```c
void _SET_LAUNCH_CONTROL_ENABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Toggles "Arena Mode", a global flag that affects physics, damage, and handling for all vehicles.

When enabled:

*   fTractionLossMult is multiplied by 0.25, increasing grip significantly.
*   Mid-air vehicle control rotation force is increased by 50%.
*   Vehicles explode immediately when body health reaches 0.
*   Disables chain-reaction explosions for nearby vehicles.
*   Prevents engine damage from colliding with Ramp Cars.
*   Overrides the Stunt Mode ([`N_0x9ebd751e5787baf2`](#n_0x9ebd751e5787baf2)) collision protection.
*   Reduces the chance of falling off bikes/quads.

```
NativeDB Introduced: v1604
```

**Nombres antiguos (alias):** `0xAA6A6098851C396F` (`N_0xaa6a6098851c396f`)

---
### StartRopeUnwindingFront

`START_ROPE_UNWINDING_FRONT` · hash `0x538D1179EC1AA9A9` · jhash `0xFC0DB4C3` · **Cliente**

```lua
StartRopeUnwindingFront(ropeId)
```
```c
void START_ROPE_UNWINDING_FRONT(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `void`

---
### StartRopeWinding

`START_ROPE_WINDING` · hash `0x1461C72C889E343E` · jhash `0x5187BED3` · **Cliente**

```lua
StartRopeWinding(ropeId)
```
```c
void START_ROPE_WINDING(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `void`

---
### StopRopeUnwindingFront

`STOP_ROPE_UNWINDING_FRONT` · hash `0xFFF3A50779EFBBB3` · jhash `0x2EEDB18F` · **Cliente**

```lua
StopRopeUnwindingFront(ropeId)
```
```c
void STOP_ROPE_UNWINDING_FRONT(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `void`

---
### StopRopeWinding

`STOP_ROPE_WINDING` · hash `0xCB2D4AB84A19AA7C` · jhash `0x46826B53` · **Cliente**

```lua
StopRopeWinding(ropeId)
```
```c
void STOP_ROPE_WINDING(int ropeId);
```

**Parámetros**

- `ropeId` (`int`)

**Devuelve:** `void`

---
### UnpinRopeVertex

`UNPIN_ROPE_VERTEX` · hash `0x4B5AE2EEE4A8F180` · jhash `0xB30B552F` · **Cliente**

```lua
UnpinRopeVertex(ropeId, vertex)
```
```c
void UNPIN_ROPE_VERTEX(int ropeId, int vertex);
```

**Parámetros**

- `ropeId` (`int`)
- `vertex` (`int`)

**Devuelve:** `void`

---
