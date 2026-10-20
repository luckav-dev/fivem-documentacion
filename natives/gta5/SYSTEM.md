# Natives de GTA V — SYSTEM

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `SYSTEM`: **26** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`Ceil`](#ceil) · [`Cos`](#cos) · [`Floor`](#floor) · [`Log10`](#log10) · [`Pow`](#pow) · [`Round`](#round) · [`SetThreadPriority`](#setthreadpriority) · [`Settimera`](#settimera) · [`Settimerb`](#settimerb) · [`ShiftLeft`](#shiftleft) · [`ShiftRight`](#shiftright) · [`Sin`](#sin) · [`Sqrt`](#sqrt) · [`StartNewScript`](#startnewscript) · [`StartNewScriptWithArgs`](#startnewscriptwithargs) · [`StartNewScriptWithNameHash`](#startnewscriptwithnamehash) · [`StartNewScriptWithNameHashAndArgs`](#startnewscriptwithnamehashandargs) · [`Timera`](#timera) · [`Timerb`](#timerb) · [`Timestep`](#timestep) · [`ToFloat`](#tofloat) · [`Vdist`](#vdist) · [`Vdist2`](#vdist2) · [`Vmag`](#vmag) · [`Vmag2`](#vmag2) · [`Wait`](#wait)

---
### Ceil

`CEIL` · hash `0x11E019C8F43ACC8A` · jhash `0xD536A1DF` · **Cliente**

```lua
local retval = Ceil(value)
```
```c
int CEIL(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `int`

**Descripción oficial:**

```
I'm guessing this rounds a float value up to the next whole number, and FLOOR rounds it down  
```

---
### Cos

`COS` · hash `0xD0FFB162F40A139C` · jhash `0x00238FE9` · **Cliente**

```lua
local retval = Cos(value)
```
```c
float COS(float value);
```

**Parámetros**

- `value` (`float`): The number of degrees (in degrees, not radians)

**Devuelve:** `float` — The cosine of the given number

**Descripción oficial:**

Returns the cosine of the given number.

**Ejemplo (lua):**

```lua
-- Get the heading
local heading = GetEntityHeading(PlayerPedId())
local cos = Cos(heading)

-- equivalent in lua
local cosLua = math.cos(heading * (math.pi / 180))
```

---
### Floor

`FLOOR` · hash `0xF34EE736CF047844` · jhash `0x32E9BE04` · **Cliente**

```lua
local retval = Floor(value)
```
```c
int FLOOR(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `int`

---
### Log10

`_LOG10` · hash `0xE816E655DE37FE20` · **Cliente**

```lua
local retval = Log10(value)
```
```c
float _LOG10(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### Pow

`POW` · hash `0xE3621CC40F31FE2E` · jhash `0x85D134F8` · **Cliente**

```lua
local retval = Pow(base, exponent)
```
```c
float POW(float base, float exponent);
```

**Parámetros**

- `base` (`float`)
- `exponent` (`float`)

**Devuelve:** `float`

---
### Round

`ROUND` · hash `0xF2DB717A73826179` · jhash `0x323B0E24` · **Cliente**

```lua
local retval = Round(value)
```
```c
int ROUND(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `int`

---
### SetThreadPriority

`_SET_THREAD_PRIORITY` · hash `0x42B65DEEF2EDF2A1` · **Cliente**

```lua
SetThreadPriority(priority)
```
```c
void _SET_THREAD_PRIORITY(int priority);
```

**Parámetros**

- `priority` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
0 = high
1 = normal
2 = low
```

**Nombres antiguos (alias):** `0x42B65DEEF2EDF2A1` (`N_0x42b65deef2edf2a1`)

---
### Settimera

`SETTIMERA` · hash `0xC1B1E9A034A63A62` · jhash `0x35785333` · **Cliente**

```lua
Settimera(value)
```
```c
void SETTIMERA(int value);
```

**Parámetros**

- `value` (`int`): In milliseconds.

**Devuelve:** `void`

**Descripción oficial:**

Sets the value for the timer A in milliseconds

---
### Settimerb

`SETTIMERB` · hash `0x5AE11BC36633DE4E` · jhash `0x27C1B7C6` · **Cliente**

```lua
Settimerb(value)
```
```c
void SETTIMERB(int value);
```

**Parámetros**

- `value` (`int`): In milliseconds.

**Devuelve:** `void`

**Descripción oficial:**

Sets the value for the timer B in milliseconds

---
### ShiftLeft

`SHIFT_LEFT` · hash `0xEDD95A39E5544DE8` · jhash `0x314CC6CD` · **Cliente**

```lua
local retval = ShiftLeft(value, bitShift)
```
```c
int SHIFT_LEFT(int value, int bitShift);
```

**Parámetros**

- `value` (`int`)
- `bitShift` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

Left bit shifts a value.
It is advised you use the `<<` operator instead of this native. It does the same and is faster.

---
### ShiftRight

`SHIFT_RIGHT` · hash `0x97EF1E5BCE9DC075` · jhash `0x352633CA` · **Cliente**

```lua
local retval = ShiftRight(value, bitShift)
```
```c
int SHIFT_RIGHT(int value, int bitShift);
```

**Parámetros**

- `value` (`int`)
- `bitShift` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

Right bit shifts a value.
It is advised you use the `>>` operator instead of this native. It does the same and is faster.

---
### Sin

`SIN` · hash `0x0BADBFA3B172435F` · jhash `0xBF987F58` · **Cliente**

```lua
local retval = Sin(value)
```
```c
float SIN(float value);
```

**Parámetros**

- `value` (`float`): The number of degrees (in degrees, not radians)

**Devuelve:** `float` — The sine of the given number

**Descripción oficial:**

Returns the sine of the given number.

**Ejemplo (lua):**

```lua
-- Get the heading
local heading = GetEntityHeading(PlayerPedId())
local sin = Sin(heading)

-- equivalent in lua
local sinLua = math.sin(heading * (math.pi / 180))
```

---
### Sqrt

`SQRT` · hash `0x71D93B57D07F9804` · jhash `0x145C7701` · **Cliente**

```lua
local retval = Sqrt(value)
```
```c
float SQRT(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `float`

---
### StartNewScript

`START_NEW_SCRIPT` · hash `0xE81651AD79516E48` · jhash `0x3F166D0E` · **Cliente**

```lua
local retval = StartNewScript(scriptName, stackSize)
```
```c
int START_NEW_SCRIPT(char* scriptName, int stackSize);
```

**Parámetros**

- `scriptName` (`char*`)
- `stackSize` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Examples:
 g_384A = SYSTEM::START_NEW_SCRIPT("cellphone_flashhand", 1424);
 l_10D = SYSTEM::START_NEW_SCRIPT("taxiService", 1828);
 SYSTEM::START_NEW_SCRIPT("AM_MP_YACHT", 5000);
 SYSTEM::START_NEW_SCRIPT("emergencycall", 512);
 SYSTEM::START_NEW_SCRIPT("emergencycall", 512);
 SYSTEM::START_NEW_SCRIPT("FM_maintain_cloud_header_data", 1424);
 SYSTEM::START_NEW_SCRIPT("FM_Mission_Controller", 31000);
 SYSTEM::START_NEW_SCRIPT("tennis_family", 3650);
 SYSTEM::START_NEW_SCRIPT("Celebrations", 3650);
Decompiled examples of usage when starting a script:

    SCRIPT::REQUEST_SCRIPT(a_0);
    if (SCRIPT::HAS_SCRIPT_LOADED(a_0)) {
        SYSTEM::START_NEW_SCRIPT(a_0, v_3);
        SCRIPT::SET_SCRIPT_AS_NO_LONGER_NEEDED(a_0);
        return 1;
    }

or:
    v_2 = "MrsPhilips2";
    SCRIPT::REQUEST_SCRIPT(v_2);
    while (!SCRIPT::HAS_SCRIPT_LOADED(v_2)) {
    SCRIPT::REQUEST_SCRIPT(v_2);
    SYSTEM::WAIT(0);
    }
    sub_8792(36);
    SYSTEM::START_NEW_SCRIPT(v_2, 17000);
    SCRIPT::SET_SCRIPT_AS_NO_LONGER_NEEDED(v_2);
All native script names: pastebin.com/K9adDsu4 and pastebin.com/yLNWicUi
```

---
### StartNewScriptWithArgs

`START_NEW_SCRIPT_WITH_ARGS` · hash `0xB8BA7F44DF1575E1` · jhash `0x4A2100E4` · **Cliente**

```lua
local retval, args = StartNewScriptWithArgs(scriptName, argCount, stackSize)
```
```c
int START_NEW_SCRIPT_WITH_ARGS(char* scriptName, Any* args, int argCount, int stackSize);
```

**Parámetros**

- `scriptName` (`char*`)
- `args` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `argCount` (`int`)
- `stackSize` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
return : script thread id, 0 if failed  
Pass pointer to struct of args in p1, size of struct goes into p2  
```

---
### StartNewScriptWithNameHash

`START_NEW_SCRIPT_WITH_NAME_HASH` · hash `0xEB1C67C3A5333A92` · jhash `0x8D15BE5D` · **Cliente**

```lua
local retval = StartNewScriptWithNameHash(scriptHash, stackSize)
```
```c
int START_NEW_SCRIPT_WITH_NAME_HASH(Hash scriptHash, int stackSize);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `stackSize` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `_START_NEW_STREAMED_SCRIPT` (`StartNewStreamedScript`)

---
### StartNewScriptWithNameHashAndArgs

`START_NEW_SCRIPT_WITH_NAME_HASH_AND_ARGS` · hash `0xC4BB298BD441BE78` · jhash `0xE38A3AD4` · **Cliente**

```lua
local retval, args = StartNewScriptWithNameHashAndArgs(scriptHash, argCount, stackSize)
```
```c
int START_NEW_SCRIPT_WITH_NAME_HASH_AND_ARGS(Hash scriptHash, Any* args, int argCount, int stackSize);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `args` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `argCount` (`int`)
- `stackSize` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `_START_NEW_STREAMED_SCRIPT_WITH_ARGS` (`StartNewStreamedScriptWithArgs`)

---
### Timera

`TIMERA` · hash `0x83666F9FB8FEBD4B` · jhash `0x45C8C188` · **Cliente**

```lua
local retval = Timera()
```
```c
int TIMERA();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Counts up. Every 1000 is 1 real-time second. Use SETTIMERA(int value) to set the timer (e.g.: SETTIMERA(0)).  
```

---
### Timerb

`TIMERB` · hash `0xC9D9444186B5A374` · jhash `0x330A9C0C` · **Cliente**

```lua
local retval = Timerb()
```
```c
int TIMERB();
```

**Devuelve:** `int`

---
### Timestep

`TIMESTEP` · hash `0x0000000050597EE2` · jhash `0x50597EE2` · **Cliente**

```lua
local retval = Timestep()
```
```c
float TIMESTEP();
```

**Devuelve:** `float`

**Descripción oficial:**

```
Gets the current frame time.  
```

---
### ToFloat

`TO_FLOAT` · hash `0xBBDA792448DB5A89` · jhash `0x67116627` · **Cliente**

```lua
local retval = ToFloat(value)
```
```c
float TO_FLOAT(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `float`

---
### Vdist

`VDIST` · hash `0x2A488C176D52CCA5` · jhash `0x3C08ECB7` · **Cliente**

```lua
local retval = Vdist(x1, y1, z1, x2, y2, z2)
```
```c
float VDIST(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`): X coordinate of the first point.
- `y1` (`float`): Y coordinate of the first point.
- `z1` (`float`): Z coordinate of the first point. Represents the height or elevation at the first point.
- `x2` (`float`): X coordinate of the second point.
- `y2` (`float`): Y coordinate of the second point.
- `z2` (`float`): Z coordinate of the second point. Represents the height or elevation at the second point.

**Devuelve:** `float` — Returns the distance as a float between the two points (`x1`, `y1`, `z1`) and (`x2`, `y2`, `z2`) in the game world.

**Descripción oficial:**

Calculates the distance between two points in 3D space. For performance reasons, consider using direct mathematical calculations for distance, as they can be more efficient than calling this native function.

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
-- Define a set of coordinates
local coords = vector3(145.0, 200.0, 1000.0)

-- Get the player's current ped
local playerPed = PlayerPedId()

-- Get the player's current coordinates
local coordsPlayer = GetEntityCoords(playerPed, false)

-- Calculate the distance between the player and the coordinates
local distance = Vdist(coordsPlayer.x, coordsPlayer.y, coordsPlayer.z, coords.x, coords.y, coords.z)

if (distance < 10.0) then
    print("You are close to the coordinates")
else
    print("You are far from the coordinates")
end
```

**Ejemplo (javascript):**

```javascript
// Define a set of coordinates
const coords = [145.0, 200.0, 1000.0];

// Get the player's current ped
const playerPed = PlayerPedId();

// Get the player's current coordinates
const coordsPlayer = GetEntityCoords(playerPed, false);

// Calculate the distance between the player and the coordinates
const distance = Vdist(coordsPlayer[0], coordsPlayer[1], coordsPlayer[2], coords[0], coords[1], coords[2]);

if (distance < 10.0) {
    console.log("You are close to the coordinates");
} else {
    console.log("You are far from the coordinates");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Define a set of coordinates
Vector3 coords = new Vector3(145.0f, 200.0f, 1000.0f);

// Get the player's current ped
Ped playerPed = PlayerPedId();

// Get the player's current coordinates
Vector3 coordsPlayer = GetEntityCoords(playerPed, false);

// Calculate the distance between the player and the coordinates
float distance = Vdist(coordsPlayer.X, coordsPlayer.Y, coordsPlayer.Z, coords.X, coords.Y, coords.Z);

if (distance < 10.0f)
{
    Debug.WriteLine("You are close to the coordinates");
}
else
{
    Debug.WriteLine("You are far from the coordinates");
}
```

---
### Vdist2

`VDIST2` · hash `0xB7A628320EFF8E47` · jhash `0xC85DEF1F` · **Cliente**

```lua
local retval = Vdist2(x1, y1, z1, x2, y2, z2)
```
```c
float VDIST2(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`): X coordinate of the first point.
- `y1` (`float`): Y coordinate of the first point.
- `z1` (`float`): Z coordinate of the first point. Represents the height or elevation at the first point.
- `x2` (`float`): X coordinate of the second point.
- `y2` (`float`): Y coordinate of the second point.
- `z2` (`float`): Z coordinate of the second point. Represents the height or elevation at the second point.

**Devuelve:** `float` — Returns the distance as a float between the two points (`x1`, `y1`, `z1`) and (`x2`, `y2`, `z2`) in the game world.

**Descripción oficial:**

Calculates distance between vectors but does not perform Sqrt operations. Its way faster than [`VDIST`](#vdist), but it's not faster than direct mathematical calculations.

```
NativeDB Introduced: v323
```

---
### Vmag

`VMAG` · hash `0x652D2EEEF1D3E62C` · jhash `0x1FCF1ECD` · **Cliente**

```lua
local retval = Vmag(x, y, z)
```
```c
float VMAG(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
Calculates the magnitude of a vector.  
```

---
### Vmag2

`VMAG2` · hash `0xA8CEACB4F35AE058` · jhash `0xE796E629` · **Cliente**

```lua
local retval = Vmag2(x, y, z)
```
```c
float VMAG2(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
Calculates the magnitude of a vector but does not perform Sqrt operations. (Its way faster)  
```

---
### Wait

`WAIT` · hash `0x4EDE34FBADD967A6` · jhash `0x7715C03B` · **Cliente**

```lua
Wait(ms)
```
```c
void WAIT(int ms);
```

**Parámetros**

- `ms` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Pauses execution of the current script, please note this behavior is only seen when called from one of the game script files(ysc). In order to wait an asi script use "static void WAIT(DWORD time);" found in main.h
```

---
