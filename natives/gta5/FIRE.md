# Natives de GTA V — FIRE

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `FIRE`: **18** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddExplosion`](#addexplosion) · [`AddExplosionWithUserVfx`](#addexplosionwithuservfx) · [`AddOwnedExplosion`](#addownedexplosion) · [`GetClosestFirePos`](#getclosestfirepos) · [`GetEntityInsideExplosionArea`](#getentityinsideexplosionarea) · [`GetEntityInsideExplosionSphere`](#getentityinsideexplosionsphere) · [`GetNumberOfFiresInRange`](#getnumberoffiresinrange) · [`IsEntityOnFire`](#isentityonfire) · [`IsExplosionActiveInArea`](#isexplosionactiveinarea) · [`IsExplosionInAngledArea`](#isexplosioninangledarea) · [`IsExplosionInArea`](#isexplosioninarea) · [`IsExplosionInSphere`](#isexplosioninsphere) · [`RemoveScriptFire`](#removescriptfire) · [`SetFireSpreadRate`](#setfirespreadrate) · [`StartEntityFire`](#startentityfire) · [`StartScriptFire`](#startscriptfire) · [`StopEntityFire`](#stopentityfire) · [`StopFireInRange`](#stopfireinrange)

---
### AddExplosion

`ADD_EXPLOSION` · hash `0xE3AD2BDBAEE269AC` · jhash `0x10AF5258` · **Cliente**

```lua
AddExplosion(x, y, z, explosionType, damageScale, isAudible, isInvisible, cameraShake)
```
```c
void ADD_EXPLOSION(float x, float y, float z, int explosionType, float damageScale, BOOL isAudible, BOOL isInvisible, float cameraShake);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `explosionType` (`int`)
- `damageScale` (`float`)
- `isAudible` (`BOOL`)
- `isInvisible` (`BOOL`)
- `cameraShake` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 9: BOOL noDamage
```

```
BOOL isAudible = If explosion makes a sound.  
BOOL isInvisible = If the explosion is invisible or not.
BOOL noDamage = false: damage || nodamage = true: no damage
```

```cpp
enum eExplosionTag
{
	DONTCARE = -1,
	GRENADE = 0,
	GRENADELAUNCHER = 1,
	STICKYBOMB = 2,
	MOLOTOV = 3,
	ROCKET = 4,
	TANKSHELL = 5,
	HI_OCTANE = 6,
	CAR = 7,
	PLANE = 8,
	PETROL_PUMP = 9,
	BIKE = 10,
	DIR_STEAM = 11,
	DIR_FLAME = 12,
	DIR_WATER_HYDRANT = 13,
	DIR_GAS_CANISTER = 14,
	BOAT = 15,
	SHIP_DESTROY = 16,
	TRUCK = 17,
	BULLET = 18,
	SMOKE_GRENADE_LAUNCHER = 19,
	SMOKE_GRENADE = 20,
	BZGAS = 21,
	FLARE = 22,
	GAS_CANISTER = 23,
	EXTINGUISHER = 24,
	PROGRAMMABLEAR = 25,
	TRAIN = 26,
	BARREL = 27,
	PROPANE = 28,
	BLIMP = 29,
	DIR_FLAME_EXPLODE = 30,
	TANKER = 31,
	PLANE_ROCKET = 32,
	VEHICLE_BULLET = 33,
	GAS_TANK = 34,
	BIRD_CRAP = 35,
	RAILGUN = 36,
	BLIMP2 = 37,
	FIREWORK = 38,
	SNOWBALL = 39,
	PROXMINE = 40,
	VALKYRIE_CANNON = 41,
	AIR_DEFENCE = 42,
	PIPEBOMB = 43,
	VEHICLEMINE = 44,
	EXPLOSIVEAMMO = 45,
	APCSHELL = 46,
	BOMB_CLUSTER = 47,
	BOMB_GAS = 48,
	BOMB_INCENDIARY = 49,
	BOMB_STANDARD = 50,
	TORPEDO = 51,
	TORPEDO_UNDERWATER = 52,
	BOMBUSHKA_CANNON = 53,
	BOMB_CLUSTER_SECONDARY = 54,
	HUNTER_BARRAGE = 55,
	HUNTER_CANNON = 56,
	ROGUE_CANNON = 57,
	MINE_UNDERWATER = 58,
	ORBITAL_CANNON = 59,
	BOMB_STANDARD_WIDE = 60,
	EXPLOSIVEAMMO_SHOTGUN = 61,
	OPPRESSOR2_CANNON = 62,
	MORTAR_KINETIC = 63,
	VEHICLEMINE_KINETIC = 64,
	VEHICLEMINE_EMP = 65,
	VEHICLEMINE_SPIKE = 66,
	VEHICLEMINE_SLICK = 67,
	VEHICLEMINE_TAR = 68,
	SCRIPT_DRONE = 69,
	RAYGUN = 70,
	BURIEDMINE = 71,
	SCRIPT_MISSILE = 72,
	RCTANK_ROCKET = 73,
	BOMB_WATER = 74,
	BOMB_WATER_SECONDARY = 75,
	MINE_CNCSPIKE = 76,
	BZGAS_MK2 = 77,
	FLASHGRENADE = 78,
	STUNGRENADE = 79,
	CNC_KINETICRAM = 80,
	SCRIPT_MISSILE_LARGE = 81,
	SUBMARINE_BIG = 82,
	EMPLAUNCHER_EMP = 83
};
```

---
### AddExplosionWithUserVfx

`ADD_EXPLOSION_WITH_USER_VFX` · hash `0x36DD3FE58B5E5212` · jhash `0xCF358946` · **Cliente**

```lua
AddExplosionWithUserVfx(x, y, z, explosionType, explosionFx, damageScale, isAudible, isInvisible, cameraShake)
```
```c
void ADD_EXPLOSION_WITH_USER_VFX(float x, float y, float z, int explosionType, Hash explosionFx, float damageScale, BOOL isAudible, BOOL isInvisible, float cameraShake);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `explosionType` (`int`): See [`ADD_EXPLOSION`](#addexplosion).
- `explosionFx` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `damageScale` (`float`)
- `isAudible` (`BOOL`): If explosion makes a sound.
- `isInvisible` (`BOOL`): If the explosion is invisible or not.
- `cameraShake` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ADD_SPECFX_EXPLOSION` (`AddSpecfxExplosion`)

---
### AddOwnedExplosion

`ADD_OWNED_EXPLOSION` · hash `0x172AA1B624FA1013` · jhash `0x27EE0D67` · **Cliente**

```lua
AddOwnedExplosion(ped, x, y, z, explosionType, damageScale, isAudible, isInvisible, cameraShake)
```
```c
void ADD_OWNED_EXPLOSION(Ped ped, float x, float y, float z, int explosionType, float damageScale, BOOL isAudible, BOOL isInvisible, float cameraShake);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `explosionType` (`int`): See [`ADD_EXPLOSION`](#addexplosion).
- `damageScale` (`float`)
- `isAudible` (`BOOL`): If explosion makes a sound.
- `isInvisible` (`BOOL`): If the explosion is invisible or not.
- `cameraShake` (`float`)

**Devuelve:** `void`

---
### GetClosestFirePos

`GET_CLOSEST_FIRE_POS` · hash `0x352A9F6BCF90081F` · jhash `0xC4977B47` · **Cliente**

```lua
local retval, outPosition = GetClosestFirePos(x, y, z)
```
```c
BOOL GET_CLOSEST_FIRE_POS(Vector3* outPosition, float x, float y, float z);
```

**Parámetros**

- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns TRUE if it found something. FALSE if not.  
```

---
### GetEntityInsideExplosionArea

`_GET_ENTITY_INSIDE_EXPLOSION_AREA` · hash `0x14BA4BA137AF6CEC` · jhash `0xAEC0D176` · **Cliente**

```lua
local retval = GetEntityInsideExplosionArea(explosionType, x1, y1, z1, x2, y2, z2, radius)
```
```c
Entity _GET_ENTITY_INSIDE_EXPLOSION_AREA(int explosionType, float x1, float y1, float z1, float x2, float y2, float z2, float radius);
```

**Parámetros**

- `explosionType` (`int`): See [`ADD_EXPLOSION`](#addexplosion).
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `radius` (`float`)

**Devuelve:** `Entity`

**Descripción oficial:**

```
Returns a handle to the first entity within the a circle spawned inside the 2 points from a radius.
```

**Nombres antiguos (alias):** `_GET_PED_INSIDE_EXPLOSION_AREA` (`GetPedInsideExplosionArea`)

---
### GetEntityInsideExplosionSphere

`_GET_ENTITY_INSIDE_EXPLOSION_SPHERE` · hash `0xB3CD51E3DB86F176` · **Cliente**

```lua
local retval = GetEntityInsideExplosionSphere(explosionType, x, y, z, radius)
```
```c
Entity _GET_ENTITY_INSIDE_EXPLOSION_SPHERE(int explosionType, float x, float y, float z, float radius);
```

**Parámetros**

- `explosionType` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `Entity`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### GetNumberOfFiresInRange

`GET_NUMBER_OF_FIRES_IN_RANGE` · hash `0x50CAD495A460B305` · jhash `0x654D93B7` · **Cliente**

```lua
local retval = GetNumberOfFiresInRange(x, y, z, radius)
```
```c
int GET_NUMBER_OF_FIRES_IN_RANGE(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `int`

---
### IsEntityOnFire

`IS_ENTITY_ON_FIRE` · hash `0x28D3FED7190D3A0B` · jhash `0x8C73E64F` · **Cliente**

```lua
local retval = IsEntityOnFire(entity)
```
```c
BOOL IS_ENTITY_ON_FIRE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsExplosionActiveInArea

`IS_EXPLOSION_ACTIVE_IN_AREA` · hash `0x6070104B699B2EF4` · jhash `0x37C388DB` · **Cliente**

```lua
local retval = IsExplosionActiveInArea(explosionType, x1, y1, z1, x2, y2, z2)
```
```c
BOOL IS_EXPLOSION_ACTIVE_IN_AREA(int explosionType, float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `explosionType` (`int`): See [`ADD_EXPLOSION`](#addexplosion).
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6070104B699B2EF4` (`N_0x6070104b699b2ef4`)

---
### IsExplosionInAngledArea

`IS_EXPLOSION_IN_ANGLED_AREA` · hash `0xA079A6C51525DC4B` · jhash `0x0128FED9` · **Cliente**

```lua
local retval = IsExplosionInAngledArea(explosionType, x1, y1, z1, x2, y2, z2, width)
```
```c
BOOL IS_EXPLOSION_IN_ANGLED_AREA(int explosionType, float x1, float y1, float z1, float x2, float y2, float z2, float width);
```

**Parámetros**

- `explosionType` (`int`): explosion enum, -1 for any explosion type. See [ADD_EXPLOSION](#addexplosion).
- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area

**Devuelve:** `BOOL`

**Descripción oficial:**

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

---
### IsExplosionInArea

`IS_EXPLOSION_IN_AREA` · hash `0x2E2EBA0EE7CED0E0` · jhash `0xFB40075B` · **Cliente**

```lua
local retval = IsExplosionInArea(explosionType, x1, y1, z1, x2, y2, z2)
```
```c
BOOL IS_EXPLOSION_IN_AREA(int explosionType, float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `explosionType` (`int`): See [`ADD_EXPLOSION`](#addexplosion).
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `BOOL`

---
### IsExplosionInSphere

`IS_EXPLOSION_IN_SPHERE` · hash `0xAB0F816885B0E483` · jhash `0xD455A7F3` · **Cliente**

```lua
local retval = IsExplosionInSphere(explosionType, x, y, z, radius)
```
```c
BOOL IS_EXPLOSION_IN_SPHERE(int explosionType, float x, float y, float z, float radius);
```

**Parámetros**

- `explosionType` (`int`): See [`ADD_EXPLOSION`](#addexplosion).
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

---
### RemoveScriptFire

`REMOVE_SCRIPT_FIRE` · hash `0x7FF548385680673F` · jhash `0x6B21FE26` · **Cliente**

```lua
RemoveScriptFire(fireHandle)
```
```c
void REMOVE_SCRIPT_FIRE(FireId fireHandle);
```

**Parámetros**

- `fireHandle` (`FireId`)

**Devuelve:** `void`

---
### SetFireSpreadRate

`_SET_FIRE_SPREAD_RATE` · hash `0x8F390AC4155099BA` · **Cliente**

```lua
SetFireSpreadRate(p0)
```
```c
void _SET_FIRE_SPREAD_RATE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

SET_FIRE_\*

```
NativeDB Introduced: v1734
```

---
### StartEntityFire

`START_ENTITY_FIRE` · hash `0xF6A9D9708F6F23DF` · jhash `0x8928428E` · **Cliente**

```lua
local retval = StartEntityFire(entity)
```
```c
FireId START_ENTITY_FIRE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `FireId`

---
### StartScriptFire

`START_SCRIPT_FIRE` · hash `0x6B83617E04503888` · jhash `0xE7529357` · **Cliente**

```lua
local retval = StartScriptFire(X, Y, Z, maxChildren, isGasFire)
```
```c
FireId START_SCRIPT_FIRE(float X, float Y, float Z, int maxChildren, BOOL isGasFire);
```

**Parámetros**

- `X` (`float`)
- `Y` (`float`)
- `Z` (`float`)
- `maxChildren` (`int`)
- `isGasFire` (`BOOL`)

**Devuelve:** `FireId`

**Descripción oficial:**

```
Starts a fire:  
xyz: Location of fire  
maxChildren: The max amount of times a fire can spread to other objects. Must be 25 or less, or the function will do nothing.  
isGasFire: Whether or not the fire is powered by gasoline.  
```

---
### StopEntityFire

`STOP_ENTITY_FIRE` · hash `0x7F0DD2EBBB651AFF` · jhash `0xCE8C9066` · **Cliente**

```lua
StopEntityFire(entity)
```
```c
void STOP_ENTITY_FIRE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### StopFireInRange

`STOP_FIRE_IN_RANGE` · hash `0x056A8A219B8E829F` · jhash `0x725C7205` · **Cliente**

```lua
StopFireInRange(x, y, z, radius)
```
```c
void STOP_FIRE_IN_RANGE(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

---
