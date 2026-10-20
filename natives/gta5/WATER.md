# Natives de GTA V — WATER

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `WATER`: **12** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddExtraCalmingQuad`](#addextracalmingquad) · [`GetDeepOceanScaler`](#getdeepoceanscaler) · [`GetWaterHeight`](#getwaterheight) · [`GetWaterHeightNoWaves`](#getwaterheightnowaves) · [`ModifyWater`](#modifywater) · [`N_0x547237aa71ab44de`](#n_0x547237aa71ab44de) · [`RemoveCurrentRise`](#removecurrentrise) · [`ResetDeepOceanScaler`](#resetdeepoceanscaler) · [`SetDeepOceanScaler`](#setdeepoceanscaler) · [`TestProbeAgainstAllWater`](#testprobeagainstallwater) · [`TestProbeAgainstWater`](#testprobeagainstwater) · [`TestVerticalProbeAgainstAllWater`](#testverticalprobeagainstallwater)

---
### AddExtraCalmingQuad

`ADD_EXTRA_CALMING_QUAD` · hash `0xFDBF4CDBC07E1706` · jhash `0xA9419B6D` · **Cliente**

```lua
local retval = AddExtraCalmingQuad(xLow, yLow, xHigh, yHigh, height)
```
```c
int ADD_EXTRA_CALMING_QUAD(float xLow, float yLow, float xHigh, float yHigh, float height);
```

**Parámetros**

- `xLow` (`float`)
- `yLow` (`float`)
- `xHigh` (`float`)
- `yHigh` (`float`)
- `height` (`float`)

**Devuelve:** `int` — If succeeded to add, returns a rise index that can be used on REMOVE_EXTRA_CALMING_QUAD. If failed to add, returns -1 (make sure you don't pass -1 to REMOVE_EXTRA_CALMING_QUAD).

**Descripción oficial:**

Only 8 current rises can exist. If rises need to be changed, use REMOVE_EXTRA_CALMING_QUAD and then ADD_EXTRA_CALMING_QUAD again.
After removing a rise, you will be able to add a rise again.

**Nombres antiguos (alias):** `0xFDBF4CDBC07E1706` (`N_0xfdbf4cdbc07e1706`), `_ADD_CURRENT_RISE` (`AddCurrentRise`)

---
### GetDeepOceanScaler

`GET_DEEP_OCEAN_SCALER` · hash `0x2B2A2CC86778B619` · jhash `0xBD0A67FB` · **Cliente**

```lua
local retval = GetDeepOceanScaler()
```
```c
float GET_DEEP_OCEAN_SCALER();
```

**Devuelve:** `float`

**Descripción oficial:**

```
Gets the aggressiveness factor of the ocean waves.  
```

**Nombres antiguos (alias):** `0x2B2A2CC86778B619` (`N_0x2b2a2cc86778b619`), `_GET_WAVES_INTENSITY` (`GetWavesIntensity`), `_GET_CURRENT_INTENSITY` (`GetCurrentIntensity`)

---
### GetWaterHeight

`GET_WATER_HEIGHT` · hash `0xF6829842C06AE524` · jhash `0xD864E17C` · **Cliente**

```lua
local retval, height = GetWaterHeight(x, y, z, height)
```
```c
BOOL GET_WATER_HEIGHT(float x, float y, float z, float* height);
```

**Parámetros**

- `x` (`float`): The coordinate at which to test at for water.
- `y` (`float`): The coordinate at which to test at for water.
- `z` (`float`): The coordinate at which to test at for water.
- `height` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The height at which to test at for water.

**Devuelve:** `BOOL` — Returns `false` when land at the tested coordinates is higher than water, `true` otherwise.

**Descripción oficial:**

Retrieves the depth of the water beneath the specified position, accounting for the waves.

**Note:** The result might vary depending on the specific frame when this command is executed due to wave fluctuations.

---
### GetWaterHeightNoWaves

`GET_WATER_HEIGHT_NO_WAVES` · hash `0x8EE6B53CE13A9794` · jhash `0x262017F8` · **Cliente**

```lua
local retval, height = GetWaterHeightNoWaves(x, y, z, height)
```
```c
BOOL GET_WATER_HEIGHT_NO_WAVES(float x, float y, float z, float* height);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `height` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Retrieves the depth of the water beneath the specified position, disregarding wave effects.

**Note:** The result remains consistent across different frames as it doesn't consider wave fluctuations.

---
### ModifyWater

`MODIFY_WATER` · hash `0xC443FD757C3BA637` · jhash `0xC49E005A` · **Cliente**

```lua
ModifyWater(x, y, height, radius)
```
```c
void MODIFY_WATER(float x, float y, float height, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `height` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the water height for a given position and radius.  
```

---
### N_0x547237aa71ab44de

`0x547237AA71AB44DE` · hash `0x547237AA71AB44DE` · jhash `0x6F5A07BA` · **Cliente**

```lua
N_0x547237aa71ab44de(p0)
```
```c
void 0x547237AA71AB44DE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### RemoveCurrentRise

`_REMOVE_CURRENT_RISE` · hash `0xB1252E3E59A82AAF` · jhash `0x7DBCEF6F` · **Cliente**

```lua
RemoveCurrentRise(p0)
```
```c
void _REMOVE_CURRENT_RISE(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
p0 is the handle returned from _0xFDBF4CDBC07E1706  
```

**Nombres antiguos (alias):** `0xB1252E3E59A82AAF` (`N_0xb1252e3e59a82aaf`)

---
### ResetDeepOceanScaler

`RESET_DEEP_OCEAN_SCALER` · hash `0x5E5E99285AE812DB` · jhash `0x4AD23212` · **Cliente**

```lua
ResetDeepOceanScaler()
```
```c
void RESET_DEEP_OCEAN_SCALER();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the waves intensity back to original (1.0 in most cases). 
```

**Nombres antiguos (alias):** `0x5E5E99285AE812DB` (`N_0x5e5e99285ae812db`), `_RESET_WAVES_INTENSITY` (`ResetWavesIntensity`), `_RESET_CURRENT_INTENSITY` (`ResetCurrentIntensity`)

---
### SetDeepOceanScaler

`SET_DEEP_OCEAN_SCALER` · hash `0xB96B00E976BE977F` · jhash `0x53B694B1` · **Cliente**

```lua
SetDeepOceanScaler(intensity)
```
```c
void SET_DEEP_OCEAN_SCALER(float intensity);
```

**Parámetros**

- `intensity` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets a value that determines how aggressive the ocean waves will be. Values of 2.0 or more make for very aggressive waves like you see during a thunderstorm.  
Works only ~200 meters around the player.  
```

**Nombres antiguos (alias):** `0xB96B00E976BE977F` (`N_0xb96b00e976be977f`), `_SET_WAVES_INTENSITY` (`SetWavesIntensity`), `_SET_CURRENT_INTENSITY` (`SetCurrentIntensity`)

---
### TestProbeAgainstAllWater

`TEST_PROBE_AGAINST_ALL_WATER` · hash `0x8974647ED222EA5F` · jhash `0x4A962D55` · **Cliente**

```lua
local retval, result = TestProbeAgainstAllWater(x1, y1, z1, x2, y2, z2, flag, result)
```
```c
BOOL TEST_PROBE_AGAINST_ALL_WATER(float x1, float y1, float z1, float x2, float y2, float z2, int flag, Vector3* result);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `flag` (`int`): See [`START_SHAPE_TEST_LOS_PROBE`](SHAPETEST.md#startshapetestlosprobe)
- `result` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Flags are identical to START_SHAPE_TEST\*, however, 128 is automatically set.

---
### TestProbeAgainstWater

`TEST_PROBE_AGAINST_WATER` · hash `0xFFA5D878809819DB` · jhash `0xAA4AE00C` · **Cliente**

```lua
local retval, result = TestProbeAgainstWater(x1, y1, z1, x2, y2, z2, result)
```
```c
BOOL TEST_PROBE_AGAINST_WATER(float x1, float y1, float z1, float x2, float y2, float z2, Vector3* result);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `result` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### TestVerticalProbeAgainstAllWater

`TEST_VERTICAL_PROBE_AGAINST_ALL_WATER` · hash `0x2B3451FA1E3142E2` · jhash `0x4C71D143` · **Cliente**

```lua
local retval, height = TestVerticalProbeAgainstAllWater(x, y, z, flag, height)
```
```c
BOOL TEST_VERTICAL_PROBE_AGAINST_ALL_WATER(float x, float y, float z, int flag, float* height);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `flag` (`int`): See [`START_SHAPE_TEST_LOS_PROBE`](SHAPETEST.md#startshapetestlosprobe)
- `height` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
