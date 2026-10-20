# Natives de GTA V — BRAIN

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `BRAIN`: **11** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddScriptToRandomPed`](#addscripttorandomped) · [`DisableScriptBrainSet`](#disablescriptbrainset) · [`EnableScriptBrainSet`](#enablescriptbrainset) · [`IsObjectWithinBrainActivationRange`](#isobjectwithinbrainactivationrange) · [`IsWorldPointWithinBrainActivationRange`](#isworldpointwithinbrainactivationrange) · [`N_0x0b40ed49d7d6ff84`](#n_0x0b40ed49d7d6ff84) · [`N_0x4d953df78ebf8158`](#n_0x4d953df78ebf8158) · [`N_0x6d6840cee8845831`](#n_0x6d6840cee8845831) · [`N_0x6e91b04e08773030`](#n_0x6e91b04e08773030) · [`RegisterObjectScriptBrain`](#registerobjectscriptbrain) · [`RegisterWorldPointScriptBrain`](#registerworldpointscriptbrain)

---
### AddScriptToRandomPed

`ADD_SCRIPT_TO_RANDOM_PED` · hash `0x4EE5367468A65CCC` · jhash `0xECC76C3D` · **Cliente**

```lua
AddScriptToRandomPed(name, model, p2, p3)
```
```c
void ADD_SCRIPT_TO_RANDOM_PED(char* name, Hash model, float p2, float p3);
```

**Parámetros**

- `name` (`char*`)
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
BRAIN::ADD_SCRIPT_TO_RANDOM_PED("pb_prostitute", ${s_f_y_hooker_01}, 100, 0);
- Nacorpio
-----
Hardcoded to not work in Multiplayer.
```

---
### DisableScriptBrainSet

`DISABLE_SCRIPT_BRAIN_SET` · hash `0x14D8518E9760F08F` · jhash `0xFBD13FAD` · **Cliente**

```lua
DisableScriptBrainSet(brainSet)
```
```c
void DISABLE_SCRIPT_BRAIN_SET(int brainSet);
```

**Parámetros**

- `brainSet` (`int`)

**Devuelve:** `void`

---
### EnableScriptBrainSet

`ENABLE_SCRIPT_BRAIN_SET` · hash `0x67AA4D73F0CFA86B` · jhash `0x2765919F` · **Cliente**

```lua
EnableScriptBrainSet(brainSet)
```
```c
void ENABLE_SCRIPT_BRAIN_SET(int brainSet);
```

**Parámetros**

- `brainSet` (`int`)

**Devuelve:** `void`

---
### IsObjectWithinBrainActivationRange

`IS_OBJECT_WITHIN_BRAIN_ACTIVATION_RANGE` · hash `0xCCBA154209823057` · jhash `0xBA4CAA56` · **Cliente**

```lua
local retval = IsObjectWithinBrainActivationRange(object)
```
```c
BOOL IS_OBJECT_WITHIN_BRAIN_ACTIVATION_RANGE(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

---
### IsWorldPointWithinBrainActivationRange

`IS_WORLD_POINT_WITHIN_BRAIN_ACTIVATION_RANGE` · hash `0xC5042CC6F5E3D450` · jhash `0x2CF305A0` · **Cliente**

```lua
local retval = IsWorldPointWithinBrainActivationRange()
```
```c
BOOL IS_WORLD_POINT_WITHIN_BRAIN_ACTIVATION_RANGE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets whether the world point the calling script is registered to is within desired range of the player.  
```

---
### N_0x0b40ed49d7d6ff84

`0x0B40ED49D7D6FF84` · hash `0x0B40ED49D7D6FF84` · jhash `0x19B27825` · **Cliente**

```lua
N_0x0b40ed49d7d6ff84()
```
```c
void 0x0B40ED49D7D6FF84();
```

**Devuelve:** `void`

---
### N_0x4d953df78ebf8158

`0x4D953DF78EBF8158` · hash `0x4D953DF78EBF8158` · jhash `0xF3A3AB08` · **Cliente**

```lua
N_0x4d953df78ebf8158()
```
```c
void 0x4D953DF78EBF8158();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Something like flush_all_scripts   
Most of time comes after NETWORK_END_TUTORIAL_SESSION() or before TERMINATE_THIS_THREAD()  
```

---
### N_0x6d6840cee8845831

`0x6D6840CEE8845831` · hash `0x6D6840CEE8845831` · jhash `0x949FE53E` · **Cliente**

```lua
N_0x6d6840cee8845831(action)
```
```c
void 0x6D6840CEE8845831(char* action);
```

**Parámetros**

- `action` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Possible values:  
act_cinema  
am_mp_carwash_launch  
am_mp_carwash_control  
am_mp_property_ext  
chop  
fairgroundHub  
launcher_BasejumpHeli  
launcher_BasejumpPack  
launcher_CarWash  
launcher_golf  
launcher_Hunting_Ambient  
launcher_MrsPhilips  
launcher_OffroadRacing  
launcher_pilotschool  
launcher_Racing  
launcher_rampage  
launcher_rampage  
launcher_range  
launcher_stunts  
launcher_stunts  
launcher_tennis  
launcher_Tonya  
launcher_Triathlon  
launcher_Yoga  
ob_mp_bed_low  
ob_mp_bed_med  
```

---
### N_0x6e91b04e08773030

`0x6E91B04E08773030` · hash `0x6E91B04E08773030` · jhash `0x29CE8BAA` · **Cliente**

```lua
N_0x6e91b04e08773030(action)
```
```c
void 0x6E91B04E08773030(char* action);
```

**Parámetros**

- `action` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Looks like a cousin of above function _6D6840CEE8845831 as it was found among them. Must be similar  
Here are possible values of argument -   
"ob_tv"  
"launcher_Darts"  
```

---
### RegisterObjectScriptBrain

`REGISTER_OBJECT_SCRIPT_BRAIN` · hash `0x0BE84C318BA6EC22` · jhash `0xB6BCC608` · **Cliente**

```lua
RegisterObjectScriptBrain(scriptName, modelHash, p2, activationRange, p4, p5)
```
```c
void REGISTER_OBJECT_SCRIPT_BRAIN(char* scriptName, Hash modelHash, int p2, float activationRange, int p4, int p5);
```

**Parámetros**

- `scriptName` (`char*`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`int`)
- `activationRange` (`float`)
- `p4` (`int`)
- `p5` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Registers a script for any object with a specific model hash.
BRAIN::REGISTER_OBJECT_SCRIPT_BRAIN("ob_telescope", ${prop_telescope_01}, 100, 4.0, -1, 9);
```

---
### RegisterWorldPointScriptBrain

`REGISTER_WORLD_POINT_SCRIPT_BRAIN` · hash `0x3CDC7136613284BD` · jhash `0x725D91F7` · **Cliente**

```lua
RegisterWorldPointScriptBrain(scriptName, activationRange, p2)
```
```c
void REGISTER_WORLD_POINT_SCRIPT_BRAIN(char* scriptName, float activationRange, int p2);
```

**Parámetros**

- `scriptName` (`char*`)
- `activationRange` (`float`)
- `p2` (`int`)

**Devuelve:** `void`

---
