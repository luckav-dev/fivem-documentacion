# Natives de GTA V — INTERIOR

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `INTERIOR`: **45** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivateInteriorEntitySet`](#activateinteriorentityset) · [`AddPickupToInteriorRoomByName`](#addpickuptointeriorroombyname) · [`CapInterior`](#capinterior) · [`ClearInteriorForEntity`](#clearinteriorforentity) · [`ClearRoomForEntity`](#clearroomforentity) · [`ClearRoomForGameViewport`](#clearroomforgameviewport) · [`DeactivateInteriorEntitySet`](#deactivateinteriorentityset) · [`DisableInterior`](#disableinterior) · [`EnableExteriorCullModelThisFrame`](#enableexteriorcullmodelthisframe) · [`EnableScriptCullModelThisFrame`](#enablescriptcullmodelthisframe) · [`ForceRoomForEntity`](#forceroomforentity) · [`ForceRoomForGameViewport`](#forceroomforgameviewport) · [`GetInteriorAtCoords`](#getinterioratcoords) · [`GetInteriorAtCoordsWithType`](#getinterioratcoordswithtype) · [`GetInteriorAtCoordsWithTypehash`](#getinterioratcoordswithtypehash) · [`GetInteriorFromCollision`](#getinteriorfromcollision) · [`GetInteriorFromEntity`](#getinteriorfromentity) · [`GetInteriorFromPrimaryView`](#getinteriorfromprimaryview) · [`GetInteriorGroupId`](#getinteriorgroupid) · [`GetInteriorHeading`](#getinteriorheading) · [`GetInteriorLocationAndNamehash`](#getinteriorlocationandnamehash) · [`GetKeyForEntityInRoom`](#getkeyforentityinroom) · [`GetOffsetFromInteriorInWorldCoords`](#getoffsetfrominteriorinworldcoords) · [`GetRoomKeyForGameViewport`](#getroomkeyforgameviewport) · [`GetRoomKeyFromEntity`](#getroomkeyfromentity) · [`IsCollisionMarkedOutside`](#iscollisionmarkedoutside) · [`IsInteriorCapped`](#isinteriorcapped) · [`IsInteriorDisabled`](#isinteriordisabled) · [`IsInteriorEntitySetActive`](#isinteriorentitysetactive) · [`IsInteriorReady`](#isinteriorready) · [`IsInteriorScene`](#isinteriorscene) · [`IsValidInterior`](#isvalidinterior) · [`N_0x38c1cb1cb119a016`](#n_0x38c1cb1cb119a016) · [`N_0x405dc2aef6af95b9`](#n_0x405dc2aef6af95b9) · [`N_0x483aca1176ca93f1`](#n_0x483aca1176ca93f1) · [`N_0x4c2330e61d3deb56`](#n_0x4c2330e61d3deb56) · [`N_0x7241ccb7d020db69`](#n_0x7241ccb7d020db69) · [`N_0x7ecdf98587e92dec`](#n_0x7ecdf98587e92dec) · [`N_0x82ebb79e258fa2b7`](#n_0x82ebb79e258fa2b7) · [`N_0x9e6542f0ce8e70a3`](#n_0x9e6542f0ce8e70a3) · [`N_0xaf348afcb575a441`](#n_0xaf348afcb575a441) · [`PinInteriorInMemory`](#pininteriorinmemory) · [`RefreshInterior`](#refreshinterior) · [`SetInteriorEntitySetColor`](#setinteriorentitysetcolor) · [`UnpinInterior`](#unpininterior)

---
### ActivateInteriorEntitySet

`ACTIVATE_INTERIOR_ENTITY_SET` · hash `0x55E86AF2712B36A1` · jhash `0xC80A5DDF` · **Cliente**

```lua
ActivateInteriorEntitySet(interior, entitySetName)
```
```c
void ACTIVATE_INTERIOR_ENTITY_SET(int interior, char* entitySetName);
```

**Parámetros**

- `interior` (`int`)
- `entitySetName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
More info: http://gtaforums.com/topic/836367-adding-props-to-interiors/  
```

**Nombres antiguos (alias):** `0x55E86AF2712B36A1` (`N_0x55e86af2712b36a1`), `_ENABLE_INTERIOR_PROP` (`EnableInteriorProp`)

---
### AddPickupToInteriorRoomByName

`ADD_PICKUP_TO_INTERIOR_ROOM_BY_NAME` · hash `0x3F6167F351168730` · jhash `0xA2A73564` · **Cliente**

```lua
AddPickupToInteriorRoomByName(pickup, roomName)
```
```c
void ADD_PICKUP_TO_INTERIOR_ROOM_BY_NAME(Pickup pickup, char* roomName);
```

**Parámetros**

- `pickup` (`Pickup`)
- `roomName` (`char*`)

**Devuelve:** `void`

---
### CapInterior

`CAP_INTERIOR` · hash `0xD9175F941610DB54` · jhash `0x34E735A6` · **Cliente**

```lua
CapInterior(interiorID, toggle)
```
```c
void CAP_INTERIOR(int interiorID, BOOL toggle);
```

**Parámetros**

- `interiorID` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does something similar to INTERIOR::DISABLE_INTERIOR  
```

---
### ClearInteriorForEntity

`_CLEAR_INTERIOR_FOR_ENTITY` · hash `0x85D5422B2039A70D` · **Cliente**

```lua
ClearInteriorForEntity(entity)
```
```c
void _CLEAR_INTERIOR_FOR_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

Immediately removes entity from an interior. Like sets entity to `limbo` room.

```
NativeDB Introduced: v2189
```

---
### ClearRoomForEntity

`CLEAR_ROOM_FOR_ENTITY` · hash `0xB365FC0C4E27FFA7` · jhash `0x7DDADB92` · **Cliente**

```lua
ClearRoomForEntity(entity)
```
```c
void CLEAR_ROOM_FOR_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### ClearRoomForGameViewport

`CLEAR_ROOM_FOR_GAME_VIEWPORT` · hash `0x23B59D8912F94246` · jhash `0x617DC75D` · **Cliente**

```lua
ClearRoomForGameViewport()
```
```c
void CLEAR_ROOM_FOR_GAME_VIEWPORT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x23B59D8912F94246` (`N_0x23b59d8912f94246`)

---
### DeactivateInteriorEntitySet

`DEACTIVATE_INTERIOR_ENTITY_SET` · hash `0x420BD37289EEE162` · jhash `0xDBA768A1` · **Cliente**

```lua
DeactivateInteriorEntitySet(interior, entitySetName)
```
```c
void DEACTIVATE_INTERIOR_ENTITY_SET(int interior, char* entitySetName);
```

**Parámetros**

- `interior` (`int`)
- `entitySetName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x420BD37289EEE162` (`N_0x420bd37289eee162`), `_DISABLE_INTERIOR_PROP` (`DisableInteriorProp`)

---
### DisableInterior

`DISABLE_INTERIOR` · hash `0x6170941419D7D8EC` · jhash `0x093ADEA5` · **Cliente**

```lua
DisableInterior(interiorID, toggle)
```
```c
void DISABLE_INTERIOR(int interiorID, BOOL toggle);
```

**Parámetros**

- `interiorID` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example:   
This removes the interior from the strip club and when trying to walk inside the player just falls:  
INTERIOR::DISABLE_INTERIOR(118018, true);  
```

---
### EnableExteriorCullModelThisFrame

`ENABLE_EXTERIOR_CULL_MODEL_THIS_FRAME` · hash `0xA97F257D0151A6AB` · jhash `0x1F375B4C` · **Cliente**

```lua
EnableExteriorCullModelThisFrame(mapObjectHash)
```
```c
void ENABLE_EXTERIOR_CULL_MODEL_THIS_FRAME(Hash mapObjectHash);
```

**Parámetros**

- `mapObjectHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
This is the native that is used to hide the exterior of GTA Online apartment buildings when you are inside an apartment.
```

**Nombres antiguos (alias):** `0xA97F257D0151A6AB` (`N_0xa97f257d0151a6ab`), `_HIDE_MAP_OBJECT_THIS_FRAME` (`HideMapObjectThisFrame`)

---
### EnableScriptCullModelThisFrame

`_ENABLE_SCRIPT_CULL_MODEL_THIS_FRAME` · hash `0x50C375537449F369` · **Cliente**

```lua
EnableScriptCullModelThisFrame(mapObjectHash)
```
```c
void _ENABLE_SCRIPT_CULL_MODEL_THIS_FRAME(Hash mapObjectHash);
```

**Parámetros**

- `mapObjectHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x50C375537449F369` (`N_0x50c375537449f369`)

---
### ForceRoomForEntity

`FORCE_ROOM_FOR_ENTITY` · hash `0x52923C4710DD9907` · jhash `0x10BD4435` · **Cliente**

```lua
ForceRoomForEntity(entity, interior, roomHashKey)
```
```c
void FORCE_ROOM_FOR_ENTITY(Entity entity, int interior, Hash roomHashKey);
```

**Parámetros**

- `entity` (`Entity`)
- `interior` (`int`)
- `roomHashKey` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Forces the particular room in an interior to load incase not teleporting into the portal.
```

---
### ForceRoomForGameViewport

`FORCE_ROOM_FOR_GAME_VIEWPORT` · hash `0x920D853F3E17F1DA` · jhash `0xD79803B5` · **Cliente**

```lua
ForceRoomForGameViewport(interiorID, roomHashKey)
```
```c
void FORCE_ROOM_FOR_GAME_VIEWPORT(int interiorID, Hash roomHashKey);
```

**Parámetros**

- `interiorID` (`int`)
- `roomHashKey` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x920D853F3E17F1DA` (`N_0x920d853f3e17f1da`)

---
### GetInteriorAtCoords

`GET_INTERIOR_AT_COORDS` · hash `0xB0F7F8663821D9C3` · jhash `0xA17FBF37` · **Cliente**

```lua
local retval = GetInteriorAtCoords(x, y, z)
```
```c
int GET_INTERIOR_AT_COORDS(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns interior ID from specified coordinates. If coordinates are outside, then it returns 0.  
Example for VB.NET  
Dim interiorID As Integer = Native.Function.Call(Of Integer)(Hash.GET_INTERIOR_AT_COORDS, X, Y, Z)  
```

---
### GetInteriorAtCoordsWithType

`GET_INTERIOR_AT_COORDS_WITH_TYPE` · hash `0x05B7A89BD78797FC` · jhash `0x96525B06` · **Cliente**

```lua
local retval = GetInteriorAtCoordsWithType(x, y, z, interiorType)
```
```c
int GET_INTERIOR_AT_COORDS_WITH_TYPE(float x, float y, float z, char* interiorType);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `interiorType` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the interior ID representing the requested interior at that location (if found?). The supplied interior string is not the same as the one used to load the interior.  
Use: INTERIOR::UNPIN_INTERIOR(INTERIOR::GET_INTERIOR_AT_COORDS_WITH_TYPE(x, y, z, interior))  
Interior types include: "V_Michael", "V_Franklins", "V_Franklinshouse", etc.. you can find them in the scripts.  
Not a very useful native as you could just use GET_INTERIOR_AT_COORDS instead and get the same result, without even having to specify the interior type.  
```

**Nombres antiguos (alias):** `0x05B7A89BD78797FC` (`N_0x05b7a89bd78797fc`)

---
### GetInteriorAtCoordsWithTypehash

`GET_INTERIOR_AT_COORDS_WITH_TYPEHASH` · hash `0xF0F77ADB9F67E79D` · jhash `0x11718507` · **Cliente**

```lua
local retval = GetInteriorAtCoordsWithTypehash(x, y, z, typeHash)
```
```c
int GET_INTERIOR_AT_COORDS_WITH_TYPEHASH(float x, float y, float z, Hash typeHash);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `typeHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Hashed version of GET_INTERIOR_AT_COORDS_WITH_TYPE
```

**Nombres antiguos (alias):** `0xF0F77ADB9F67E79D` (`N_0xf0f77adb9f67e79d`), `_UNK_GET_INTERIOR_AT_COORDS` (`UnkGetInteriorAtCoords`)

---
### GetInteriorFromCollision

`GET_INTERIOR_FROM_COLLISION` · hash `0xEC4CF9FCB29A4424` · jhash `0x7ED33DC1` · **Cliente**

```lua
local retval = GetInteriorFromCollision(x, y, z)
```
```c
int GET_INTERIOR_FROM_COLLISION(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `int`

---
### GetInteriorFromEntity

`GET_INTERIOR_FROM_ENTITY` · hash `0x2107BA504071A6BB` · jhash `0x5C644614` · **Cliente**

```lua
local retval = GetInteriorFromEntity(entity)
```
```c
int GET_INTERIOR_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the handle of the interior that the entity is in. Returns 0 if outside.  
```

---
### GetInteriorFromPrimaryView

`GET_INTERIOR_FROM_PRIMARY_VIEW` · hash `0xE7D267EC6CA966C3` · jhash `0xA83C3D15` · **Cliente**

```lua
local retval = GetInteriorFromPrimaryView()
```
```c
int GET_INTERIOR_FROM_PRIMARY_VIEW();
```

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

**Nombres antiguos (alias):** `0xE7D267EC6CA966C3` (`N_0xe7d267ec6ca966c3`), `_GET_INTERIOR_FROM_GAMEPLAY_CAM` (`GetInteriorFromGameplayCam`)

---
### GetInteriorGroupId

`GET_INTERIOR_GROUP_ID` · hash `0xE4A84ABF135EF91A` · jhash `0x09D6376F` · **Cliente**

```lua
local retval = GetInteriorGroupId(interior)
```
```c
int GET_INTERIOR_GROUP_ID(int interior);
```

**Parámetros**

- `interior` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the group ID of the specified interior. For example, regular interiors have group 0, subway interiors have group 1. There are a few other groups too.  
```

---
### GetInteriorHeading

`GET_INTERIOR_HEADING` · hash `0xF49B58631D9E22D9` · **Cliente**

```lua
local retval = GetInteriorHeading(interior)
```
```c
float GET_INTERIOR_HEADING(int interior);
```

**Parámetros**

- `interior` (`int`): ID of the interior

**Devuelve:** `float` — Returns interior heading in radians. Multiply the returned value with 57.29578 (or 180.0 / math.pi) to convert it to degrees.

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `_GET_INTERIOR_HEADING` (`GetInteriorHeading`)

---
### GetInteriorLocationAndNamehash

`GET_INTERIOR_LOCATION_AND_NAMEHASH` · hash `0x252BDC06B73FA6EA` · jhash `0x75885CB3` · **Cliente**

```lua
local position, nameHash = GetInteriorLocationAndNamehash(interior)
```
```c
void GET_INTERIOR_LOCATION_AND_NAMEHASH(int interior, Vector3* position, Hash* nameHash);
```

**Parámetros**

- `interior` (`int`)
- `position` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `nameHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x252BDC06B73FA6EA` (`N_0x252bdc06b73fa6ea`), `_GET_INTERIOR_INFO` (`GetInteriorInfo`)

---
### GetKeyForEntityInRoom

`GET_KEY_FOR_ENTITY_IN_ROOM` · hash `0x399685DB942336BC` · jhash `0x91EA80EF` · **Cliente**

```lua
local retval = GetKeyForEntityInRoom(entity)
```
```c
Hash GET_KEY_FOR_ENTITY_IN_ROOM(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Seems to do the exact same as INTERIOR::GET_ROOM_KEY_FROM_ENTITY  
```

---
### GetOffsetFromInteriorInWorldCoords

`GET_OFFSET_FROM_INTERIOR_IN_WORLD_COORDS` · hash `0x9E3B3E6D66F6E22F` · jhash `0x7D8F26A1` · **Cliente**

```lua
local retval = GetOffsetFromInteriorInWorldCoords(interior, x, y, z)
```
```c
Vector3 GET_OFFSET_FROM_INTERIOR_IN_WORLD_COORDS(int interior, float x, float y, float z);
```

**Parámetros**

- `interior` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `Vector3`

---
### GetRoomKeyForGameViewport

`GET_ROOM_KEY_FOR_GAME_VIEWPORT` · hash `0xA6575914D2A0B450` · jhash `0x4FF3D3F5` · **Cliente**

```lua
local retval = GetRoomKeyForGameViewport()
```
```c
Hash GET_ROOM_KEY_FOR_GAME_VIEWPORT();
```

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0xA6575914D2A0B450` (`N_0xa6575914d2a0b450`), `_GET_ROOM_KEY_FROM_GAMEPLAY_CAM` (`GetRoomKeyFromGameplayCam`)

---
### GetRoomKeyFromEntity

`GET_ROOM_KEY_FROM_ENTITY` · hash `0x47C2A06D4F5F424B` · jhash `0xE4ACF8C3` · **Cliente**

```lua
local retval = GetRoomKeyFromEntity(entity)
```
```c
Hash GET_ROOM_KEY_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Gets the room hash key from the room that the specified entity is in. Each room in every interior has a unique key. Returns 0 if the entity is outside.  
```

---
### IsCollisionMarkedOutside

`IS_COLLISION_MARKED_OUTSIDE` · hash `0xEEA5AC2EDA7C33E8` · jhash `0x7762249C` · **Cliente**

```lua
local retval = IsCollisionMarkedOutside(x, y, z)
```
```c
BOOL IS_COLLISION_MARKED_OUTSIDE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Returns true if the collision at the specified coords is marked as being outside (false if there's an interior)

**Nombres antiguos (alias):** `0xEEA5AC2EDA7C33E8` (`N_0xeea5ac2eda7c33e8`), `_ARE_COORDS_COLLIDING_WITH_EXTERIOR` (`AreCoordsCollidingWithExterior`)

---
### IsInteriorCapped

`IS_INTERIOR_CAPPED` · hash `0x92BAC8ACF88CEC26` · jhash `0x18B17C80` · **Cliente**

```lua
local retval = IsInteriorCapped(interiorID)
```
```c
BOOL IS_INTERIOR_CAPPED(int interiorID);
```

**Parámetros**

- `interiorID` (`int`)

**Devuelve:** `BOOL`

---
### IsInteriorDisabled

`IS_INTERIOR_DISABLED` · hash `0xBC5115A5A939DD15` · jhash `0x81F34C71` · **Cliente**

```lua
local retval = IsInteriorDisabled(interior)
```
```c
BOOL IS_INTERIOR_DISABLED(int interior);
```

**Parámetros**

- `interior` (`int`)

**Devuelve:** `BOOL`

---
### IsInteriorEntitySetActive

`IS_INTERIOR_ENTITY_SET_ACTIVE` · hash `0x35F7DD45E8C0A16D` · jhash `0x39A3CC6F` · **Cliente**

```lua
local retval = IsInteriorEntitySetActive(interior, entitySetName)
```
```c
BOOL IS_INTERIOR_ENTITY_SET_ACTIVE(int interior, char* entitySetName);
```

**Parámetros**

- `interior` (`int`)
- `entitySetName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x35F7DD45E8C0A16D` (`N_0x35f7dd45e8c0a16d`), `_IS_INTERIOR_PROP_ENABLED` (`IsInteriorPropEnabled`)

---
### IsInteriorReady

`IS_INTERIOR_READY` · hash `0x6726BDCCC1932F0E` · jhash `0xE1EF6450` · **Cliente**

```lua
local retval = IsInteriorReady(interiorID)
```
```c
BOOL IS_INTERIOR_READY(int interiorID);
```

**Parámetros**

- `interiorID` (`int`)

**Devuelve:** `BOOL`

---
### IsInteriorScene

`IS_INTERIOR_SCENE` · hash `0xBC72B5D7A1CBD54D` · jhash `0x55226C13` · **Cliente**

```lua
local retval = IsInteriorScene()
```
```c
BOOL IS_INTERIOR_SCENE();
```

**Devuelve:** `BOOL`

---
### IsValidInterior

`IS_VALID_INTERIOR` · hash `0x26B0E73D7EAAF4D3` · jhash `0x39C0B635` · **Cliente**

```lua
local retval = IsValidInterior(interior)
```
```c
BOOL IS_VALID_INTERIOR(int interior);
```

**Parámetros**

- `interior` (`int`)

**Devuelve:** `BOOL`

---
### N_0x38c1cb1cb119a016

`0x38C1CB1CB119A016` · hash `0x38C1CB1CB119A016` · **Cliente**

```lua
N_0x38c1cb1cb119a016(p0, p1)
```
```c
void 0x38C1CB1CB119A016(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x405dc2aef6af95b9

`0x405DC2AEF6AF95B9` · hash `0x405DC2AEF6AF95B9` · jhash `0x0E9529CC` · **Cliente**

```lua
N_0x405dc2aef6af95b9(roomHashKey)
```
```c
void 0x405DC2AEF6AF95B9(Hash roomHashKey);
```

**Parámetros**

- `roomHashKey` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Usage: INTERIOR::_0x405DC2AEF6AF95B9(INTERIOR::GET_KEY_FOR_ENTITY_IN_ROOM(PLAYER::PLAYER_PED_ID()));  
```

---
### N_0x483aca1176ca93f1

`0x483ACA1176CA93F1` · hash `0x483ACA1176CA93F1` · **Cliente**

```lua
N_0x483aca1176ca93f1()
```
```c
void 0x483ACA1176CA93F1();
```

**Devuelve:** `void`

---
### N_0x4c2330e61d3deb56

`0x4C2330E61D3DEB56` · hash `0x4C2330E61D3DEB56` · **Cliente**

```lua
local retval = N_0x4c2330e61d3deb56(interior)
```
```c
Any 0x4C2330E61D3DEB56(int interior);
```

**Parámetros**

- `interior` (`int`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Only used once in the entire game scripts.
Does not actually return anything.
```

---
### N_0x7241ccb7d020db69

`0x7241CCB7D020DB69` · hash `0x7241CCB7D020DB69` · **Cliente**

```lua
N_0x7241ccb7d020db69(entity, toggle)
```
```c
void 0x7241CCB7D020DB69(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Jenkins hash _might_ be 0xFC227584.
```

---
### N_0x7ecdf98587e92dec

`0x7ECDF98587E92DEC` · hash `0x7ECDF98587E92DEC` · **Cliente**

```lua
N_0x7ecdf98587e92dec(p0)
```
```c
void 0x7ECDF98587E92DEC(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x82ebb79e258fa2b7

`0x82EBB79E258FA2B7` · hash `0x82EBB79E258FA2B7` · jhash `0xE645E162` · **Cliente**

```lua
N_0x82ebb79e258fa2b7(entity, interiorID)
```
```c
void 0x82EBB79E258FA2B7(Entity entity, int interiorID);
```

**Parámetros**

- `entity` (`Entity`)
- `interiorID` (`int`)

**Devuelve:** `void`

---
### N_0x9e6542f0ce8e70a3

`0x9E6542F0CE8E70A3` · hash `0x9E6542F0CE8E70A3` · jhash `0x5EF9C5C2` · **Cliente**

```lua
N_0x9e6542f0ce8e70a3(toggle)
```
```c
void 0x9E6542F0CE8E70A3(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
DISABLE_*
```

---
### N_0xaf348afcb575a441

`0xAF348AFCB575A441` · hash `0xAF348AFCB575A441` · jhash `0x1F6B4B13` · **Cliente**

```lua
N_0xaf348afcb575a441(roomName)
```
```c
void 0xAF348AFCB575A441(char* roomName);
```

**Parámetros**

- `roomName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Exemple of use(carmod_shop.c4)  
INTERIOR::_AF348AFCB575A441("V_CarModRoom");  
```

---
### PinInteriorInMemory

`PIN_INTERIOR_IN_MEMORY` · hash `0x2CA429C029CCF247` · jhash `0x3ADA414E` · **Cliente**

```lua
PinInteriorInMemory(interior)
```
```c
void PIN_INTERIOR_IN_MEMORY(int interior);
```

**Parámetros**

- `interior` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2CA429C029CCF247` (`N_0x2ca429c029ccf247`), `_LOAD_INTERIOR` (`LoadInterior`)

---
### RefreshInterior

`REFRESH_INTERIOR` · hash `0x41F37C3427C75AE0` · jhash `0x9A29ACE6` · **Cliente**

```lua
RefreshInterior(interiorID)
```
```c
void REFRESH_INTERIOR(int interiorID);
```

**Parámetros**

- `interiorID` (`int`)

**Devuelve:** `void`

---
### SetInteriorEntitySetColor

`_SET_INTERIOR_ENTITY_SET_COLOR` · hash `0xC1F1920BAF281317` · **Cliente**

```lua
SetInteriorEntitySetColor(interior, entitySetName, color)
```
```c
void _SET_INTERIOR_ENTITY_SET_COLOR(int interior, char* entitySetName, int color);
```

**Parámetros**

- `interior` (`int`)
- `entitySetName` (`char*`)
- `color` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_INTERIOR_PROP_COLOR` (`SetInteriorPropColor`)

---
### UnpinInterior

`UNPIN_INTERIOR` · hash `0x261CCE7EED010641` · jhash `0xFCFF792A` · **Cliente**

```lua
UnpinInterior(interior)
```
```c
void UNPIN_INTERIOR(int interior);
```

**Parámetros**

- `interior` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does something similar to INTERIOR::DISABLE_INTERIOR.  
You don't fall through the floor but everything is invisible inside and looks the same as when INTERIOR::DISABLE_INTERIOR is used. Peds behaves normally inside.  
```

---
