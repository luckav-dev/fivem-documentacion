# Natives de GTA V — SHAPETEST

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `SHAPETEST`: **11** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`GetShapeTestResult`](#getshapetestresult) · [`GetShapeTestResultIncludingMaterial`](#getshapetestresultincludingmaterial) · [`ReleaseScriptGuidFromEntity`](#releasescriptguidfromentity) · [`StartExpensiveSynchronousShapeTestLosProbe`](#startexpensivesynchronousshapetestlosprobe) · [`StartShapeTestBound`](#startshapetestbound) · [`StartShapeTestBoundingBox`](#startshapetestboundingbox) · [`StartShapeTestBox`](#startshapetestbox) · [`StartShapeTestCapsule`](#startshapetestcapsule) · [`StartShapeTestLosProbe`](#startshapetestlosprobe) · [`StartShapeTestSurroundingCoords`](#startshapetestsurroundingcoords) · [`StartShapeTestSweptSphere`](#startshapetestsweptsphere)

---
### GetShapeTestResult

`GET_SHAPE_TEST_RESULT` · hash `0x3D87450E15D98694` · jhash `0xF3C2875A` · **Cliente**

```lua
local retval, hit, endCoords, surfaceNormal, entityHit = GetShapeTestResult(shapeTestHandle)
```
```c
int GET_SHAPE_TEST_RESULT(int shapeTestHandle, BOOL* hit, Vector3* endCoords, Vector3* surfaceNormal, Entity* entityHit);
```

**Parámetros**

- `shapeTestHandle` (`int`): A shape test handle.
- `hit` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Whether or not the shape test hit any collisions.
- `endCoords` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The resulting coordinates where the shape test hit a collision.
- `surfaceNormal` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The surface normal of the hit position.
- `entityHit` (`Entity*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Any dynamic entity hit by the shape test.

**Devuelve:** `int` — `0` if the handle is invalid, `1` if the shape test is still pending, or `2` if the shape test has completed, and the handle should be invalidated.

**Descripción oficial:**

Returns the result of a shape test.

When used with an asynchronous shape test, this native should be looped until returning 0 or 2, after which the handle is invalidated.

Unless the return value is 2, the other return values are undefined.

**Nombres antiguos (alias):** `_GET_RAYCAST_RESULT` (`GetRaycastResult`)

---
### GetShapeTestResultIncludingMaterial

`GET_SHAPE_TEST_RESULT_INCLUDING_MATERIAL` · hash `0x65287525D951F6BE` · jhash `0x4301E10C` · **Cliente**

```lua
local retval, hit, endCoords, surfaceNormal, materialHash, entityHit = GetShapeTestResultIncludingMaterial(shapeTestHandle)
```
```c
int GET_SHAPE_TEST_RESULT_INCLUDING_MATERIAL(int shapeTestHandle, BOOL* hit, Vector3* endCoords, Vector3* surfaceNormal, Hash* materialHash, Entity* entityHit);
```

**Parámetros**

- `shapeTestHandle` (`int`): A shape test handle.
- `hit` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Whether or not the shape test hit any collisions.
- `endCoords` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The resulting coordinates where the shape test hit a collision.
- `surfaceNormal` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The surface normal of the hit position.
- `materialHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: hash of the hit material or surface type, see materialFX.dat
- `entityHit` (`Entity*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Any dynamic entity hit by the shape test.

**Devuelve:** `int` — `0` if the handle is invalid, `1` if the shape test is still pending, or `2` if the shape test has completed, and the handle should be invalidated.

**Descripción oficial:**

Returns the result of a shape test, also returning the material of any touched surface.

When used with an asynchronous shape test, this native should be looped until returning 0 or 2, after which the handle is invalidated.

Unless the return value is 2, the other return values are undefined.

**Nombres antiguos (alias):** `0x65287525D951F6BE` (`N_0x65287525d951f6be`), `_GET_SHAPE_TEST_RESULT_EX` (`GetShapeTestResultEx`)

---
### ReleaseScriptGuidFromEntity

`RELEASE_SCRIPT_GUID_FROM_ENTITY` · hash `0x2B3334BCA57CD799` · jhash `0xEC2AAF06` · **Cliente**

```lua
ReleaseScriptGuidFromEntity(entity)
```
```c
void RELEASE_SCRIPT_GUID_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity handle to invalidate.

**Devuelve:** `void`

**Descripción oficial:**

Invalidates the entity handle passed by removing the fwScriptGuid from the entity. This should be used when receiving an
ambient entity from shape testing natives, but can also be used for other natives returning an 'irrelevant' entity handle.

**Nombres antiguos (alias):** `0x2B3334BCA57CD799` (`N_0x2b3334bca57cd799`), `_SHAPE_TEST_RESULT_ENTITY` (`ShapeTestResultEntity`)

---
### StartExpensiveSynchronousShapeTestLosProbe

`START_EXPENSIVE_SYNCHRONOUS_SHAPE_TEST_LOS_PROBE` · hash `0x377906D8A31E5586` · jhash `0x8251485D` · **Cliente**

```lua
local retval = StartExpensiveSynchronousShapeTestLosProbe(x1, y1, z1, x2, y2, z2, flags, entity, p8)
```
```c
int START_EXPENSIVE_SYNCHRONOUS_SHAPE_TEST_LOS_PROBE(float x1, float y1, float z1, float x2, float y2, float z2, int flags, Entity entity, int p8);
```

**Parámetros**

- `x1` (`float`): Starting X coordinate.
- `y1` (`float`): Starting Y coordinate.
- `z1` (`float`): Starting Z coordinate.
- `x2` (`float`): Ending X coordinate.
- `y2` (`float`): Ending Y coordinate.
- `z2` (`float`): Ending Z coordinate.
- `flags` (`int`): See [START_SHAPE_TEST_LOS_PROBE](#startshapetestlosprobe).
- `entity` (`Entity`): An entity to ignore, or 0.
- `p8` (`int`): A bit mask with bits 1, 2 and/or 4, relating to collider types. 4 should usually be used.

**Devuelve:** `int` — A shape test handle.

**Descripción oficial:**

Does the same as [START_SHAPE_TEST_LOS_PROBE](#startshapetestlosprobe), except blocking until the shape test completes.

Use [START_SHAPE_TEST_LOS_PROBE](#startshapetestlosprobe) instead. Literally. Rockstar named this correctly: it's expensive, and it's synchronous.

**Nombres antiguos (alias):** `_CAST_RAY_POINT_TO_POINT` (`CastRayPointToPoint`), `_START_SHAPE_TEST_RAY` (`StartShapeTestRay`)

---
### StartShapeTestBound

`START_SHAPE_TEST_BOUND` · hash `0x37181417CE7C8900` · jhash `0x13BC46C0` · **Cliente**

```lua
local retval = StartShapeTestBound(entity, flags1, flags2)
```
```c
int START_SHAPE_TEST_BOUND(Entity entity, int flags1, int flags2);
```

**Parámetros**

- `entity` (`Entity`)
- `flags1` (`int`)
- `flags2` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

See [`START_SHAPE_TEST_LOS_PROBE`](#startshapetestlosprobe) for flags.

**Nombres antiguos (alias):** `0x37181417CE7C8900` (`N_0x37181417ce7c8900`)

---
### StartShapeTestBoundingBox

`START_SHAPE_TEST_BOUNDING_BOX` · hash `0x052837721A854EC7` · jhash `0xCEEAD94B` · **Cliente**

```lua
local retval = StartShapeTestBoundingBox(entity, flags1, flags2)
```
```c
int START_SHAPE_TEST_BOUNDING_BOX(Entity entity, int flags1, int flags2);
```

**Parámetros**

- `entity` (`Entity`)
- `flags1` (`int`)
- `flags2` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

See [`START_SHAPE_TEST_LOS_PROBE`](#startshapetestlosprobe) for flags.

**Nombres antiguos (alias):** `0x052837721A854EC7` (`N_0x052837721a854ec7`)

---
### StartShapeTestBox

`START_SHAPE_TEST_BOX` · hash `0xFE466162C4401D18` · jhash `0x249BC876` · **Cliente**

```lua
local retval = StartShapeTestBox(x, y, z, x1, y1, z1, rotX, rotY, rotZ, p9, flags, entity, p12)
```
```c
int START_SHAPE_TEST_BOX(float x, float y, float z, float x1, float y1, float z1, float rotX, float rotY, float rotZ, int p9, int flags, Entity entity, int p12);
```

**Parámetros**

- `x` (`float`): Starting X coordinate.
- `y` (`float`): Starting Y coordinate.
- `z` (`float`): Starting Z coordinate.
- `x1` (`float`): Ending X coordinate.
- `y1` (`float`): Ending Y coordinate.
- `z1` (`float`): Ending Z coordinate.
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `p9` (`int`): Unknown, always 2 or 0
- `flags` (`int`): See [`START_SHAPE_TEST_LOS_PROBE`](#startshapetestlosprobe)
- `entity` (`Entity`)
- `p12` (`int`): A bit mask with bits 1, 2, 4, or 7 relating to collider types. 4 and 7 are usually used.

**Devuelve:** `int`

**Descripción oficial:**

For more information, see [`START_EXPENSIVE_SYNCHRONOUS_SHAPE_TEST_LOS_PROBE`](#startexpensivesynchronousshapetestlosprobe) and [`START_SHAPE_TEST_LOS_PROBE`](#startshapetestlosprobe).

**Nombres antiguos (alias):** `0xFE466162C4401D18` (`N_0xfe466162c4401d18`)

---
### StartShapeTestCapsule

`START_SHAPE_TEST_CAPSULE` · hash `0x28579D1B8F8AAC80` · jhash `0x591EA833` · **Cliente**

```lua
local retval = StartShapeTestCapsule(x1, y1, z1, x2, y2, z2, radius, flags, entity, p9)
```
```c
int START_SHAPE_TEST_CAPSULE(float x1, float y1, float z1, float x2, float y2, float z2, float radius, int flags, Entity entity, int p9);
```

**Parámetros**

- `x1` (`float`): Starting X coordinate.
- `y1` (`float`): Starting Y coordinate.
- `z1` (`float`): Starting Z coordinate.
- `x2` (`float`): Ending X coordinate.
- `y2` (`float`): Ending Y coordinate.
- `z2` (`float`): Ending Z coordinate.
- `radius` (`float`)
- `flags` (`int`): See [`START_SHAPE_TEST_LOS_PROBE`](#startshapetestlosprobe)
- `entity` (`Entity`): Entity to ignore, or 0.
- `p9` (`int`): A bit mask with bits 1, 2, 4, or 7 relating to collider types. 4 and 7 are usually used.

**Devuelve:** `int`

**Descripción oficial:**

Raycast from point to point, where the ray has a radius.

**Nombres antiguos (alias):** `_CAST_3D_RAY_POINT_TO_POINT` (`Cast_3dRayPointToPoint`)

---
### StartShapeTestLosProbe

`START_SHAPE_TEST_LOS_PROBE` · hash `0x7EE9F5D83DD4F90E` · jhash `0xEFAF4BA6` · **Cliente**

```lua
local retval = StartShapeTestLosProbe(x1, y1, z1, x2, y2, z2, traceFlags, entity, optionFlags)
```
```c
int START_SHAPE_TEST_LOS_PROBE(float x1, float y1, float z1, float x2, float y2, float z2, int traceFlags, Entity entity, int optionFlags);
```

**Parámetros**

- `x1` (`float`): Starting X coordinate.
- `y1` (`float`): Starting Y coordinate.
- `z1` (`float`): Starting Z coordinate.
- `x2` (`float`): Ending X coordinate.
- `y2` (`float`): Ending Y coordinate.
- `z2` (`float`): Ending Z coordinate.
- `traceFlags` (`int`): Refer to `eTraceFlags`, this defines what the shape test will intersect with
- `entity` (`Entity`): An entity to ignore, or 0.
- `optionFlags` (`int`): Refer to `eTraceOptionFlags`, this defines additional options for the shape test

**Devuelve:** `int` — A shape test handle.

**Descripción oficial:**

Asynchronously starts a line-of-sight (raycast) world probe shape test.

```cpp
enum eTraceFlags
{
  None = 0,
  IntersectWorld = 1,
  IntersectVehicles = 2,
  IntersectPeds = 4,
  IntersectRagdolls = 8,
  IntersectObjects = 16,
  IntersectPickup = 32,
  IntersectGlass = 64,
  IntersectRiver = 128,
  IntersectFoliage = 256,

  IntersectEverything = 511
}
```

```cpp
enum eTraceOptionFlags
{
  None = 0,
  OptionIgnoreGlass = 1,
  OptionIgnoreSeeThrough = 2,
  OptionIgnoreNoCollision = 4,

  OptionDefault = 7
}
```

NOTE: Raycasts that intersect with mission_entites (flag = 2) has limited range and will not register for far away entites. The range seems to be about 30 metres.

Use the handle with [GET_SHAPE_TEST_RESULT](#getshapetestresult) or [GET_SHAPE_TEST_RESULT_INCLUDING_MATERIAL](#getshapetestresultincludingmaterial) until it returns 0 or 2.

**Nombres antiguos (alias):** `0x7EE9F5D83DD4F90E` (`N_0x7ee9f5d83dd4f90e`)

---
### StartShapeTestSurroundingCoords

`_START_SHAPE_TEST_SURROUNDING_COORDS` · hash `0xFF6BE494C7987F34` · **Cliente**

```lua
local retval, pVec1, pVec2 = StartShapeTestSurroundingCoords(flag, entity, flag2)
```
```c
int _START_SHAPE_TEST_SURROUNDING_COORDS(Vector3* pVec1, Vector3* pVec2, int flag, Entity entity, int flag2);
```

**Parámetros**

- `pVec1` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `pVec2` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `flag` (`int`)
- `entity` (`Entity`)
- `flag2` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

Since it is only used in the PC version, likely some mouse-friendly shape test. Uses **in** vector arguments.

Asynchronous.

```
it returns a ShapeTest handle that can be used with GET_SHAPE_TEST_RESULT.  
In its only usage in game scripts its called with flag set to 511, entity to player_ped_id and flag2 set to 7  
```

See [`START_SHAPE_TEST_LOS_PROBE`](#startshapetestlosprobe) for flags.

**Nombres antiguos (alias):** `0xFF6BE494C7987F34` (`N_0xff6be494c7987f34`)

---
### StartShapeTestSweptSphere

`START_SHAPE_TEST_SWEPT_SPHERE` · hash `0xE6AC6C45FBE83004` · jhash `0x4559460A` · **Cliente**

```lua
local retval = StartShapeTestSweptSphere(x1, y1, z1, x2, y2, z2, radius, flags, entity, p9)
```
```c
int START_SHAPE_TEST_SWEPT_SPHERE(float x1, float y1, float z1, float x2, float y2, float z2, float radius, int flags, Entity entity, int p9);
```

**Parámetros**

- `x1` (`float`): Starting X coordinate.
- `y1` (`float`): Starting Y coordinate.
- `z1` (`float`): Starting Z coordinate.
- `x2` (`float`): Ending X coordinate.
- `y2` (`float`): Ending Y coordinate.
- `z2` (`float`): Ending Z coordinate.
- `radius` (`float`)
- `flags` (`int`): See [`START_SHAPE_TEST_LOS_PROBE`](#startshapetestlosprobe)
- `entity` (`Entity`): An entity to ignore, or 0.
- `p9` (`int`): A bit mask with bits 1, 2, 4, or 7 relating to collider types. 4 and 7 are usually used.

**Devuelve:** `int`

**Descripción oficial:**

Performs the same type of trace as START_SHAPE_TEST_CAPSULE, but with some different hardcoded parameters.

**Nombres antiguos (alias):** `0xE6AC6C45FBE83004` (`N_0xe6ac6c45fbe83004`), `_START_SHAPE_TEST_CAPSULE_2` (`StartShapeTestCapsule_2`)

---
