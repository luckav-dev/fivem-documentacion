# Natives de GTA V — PED (parte 2 de 2: SetPedToLoadCover … WasPedSkeletonUpdated)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `PED`: **612** natives.

Partes: [1](PED-1.md) · **[2]**

[← Índice de natives](../README.md)

## Índice de esta página

[`SetPedToLoadCover`](#setpedtoloadcover) · [`SetPedToRagdoll`](#setpedtoragdoll) · [`SetPedToRagdollWithFall`](#setpedtoragdollwithfall) · [`SetPedUsingActionMode`](#setpedusingactionmode) · [`SetPedVehicleForcedSeatUsage`](#setpedvehicleforcedseatusage) · [`SetPedVisualFieldCenterAngle`](#setpedvisualfieldcenterangle) · [`SetPedVisualFieldMaxAngle`](#setpedvisualfieldmaxangle) · [`SetPedVisualFieldMaxElevationAngle`](#setpedvisualfieldmaxelevationangle) · [`SetPedVisualFieldMinAngle`](#setpedvisualfieldminangle) · [`SetPedVisualFieldMinElevationAngle`](#setpedvisualfieldminelevationangle) · [`SetPedVisualFieldPeripheralRange`](#setpedvisualfieldperipheralrange) · [`SetPedWeaponMovementClipset`](#setpedweaponmovementclipset) · [`SetPedWetnessEnabledThisFrame`](#setpedwetnessenabledthisframe) · [`SetPedWetnessHeight`](#setpedwetnessheight) · [`SetPopControlSphereThisFrame`](#setpopcontrolspherethisframe) · [`SetRagdollBlockingFlags`](#setragdollblockingflags) · [`SetRelationshipBetweenGroups`](#setrelationshipbetweengroups) · [`SetRelationshipGroupDontAffectWantedLevel`](#setrelationshipgroupdontaffectwantedlevel) · [`SetScenarioPedDensityMultiplierThisFrame`](#setscenariopeddensitymultiplierthisframe) · [`SetScenarioPedsSpawnInSphereArea`](#setscenariopedsspawninspherearea) · [`SetScenarioPedsToBeReturnedByNextCommand`](#setscenariopedstobereturnedbynextcommand) · [`SetScriptedAnimSeatOffset`](#setscriptedanimseatoffset) · [`SetScriptedConversionCoordThisFrame`](#setscriptedconversioncoordthisframe) · [`SetSynchronizedSceneHoldLastFrame`](#setsynchronizedsceneholdlastframe) · [`SetSynchronizedSceneLooped`](#setsynchronizedscenelooped) · [`SetSynchronizedSceneOrigin`](#setsynchronizedsceneorigin) · [`SetSynchronizedScenePhase`](#setsynchronizedscenephase) · [`SetSynchronizedSceneRate`](#setsynchronizedscenerate) · [`SpawnpointsCancelSearch`](#spawnpointscancelsearch) · [`SpawnpointsGetNumSearchResults`](#spawnpointsgetnumsearchresults) · [`SpawnpointsGetSearchResult`](#spawnpointsgetsearchresult) · [`SpawnpointsGetSearchResultFlags`](#spawnpointsgetsearchresultflags) · [`SpawnpointsIsSearchActive`](#spawnpointsissearchactive) · [`SpawnpointsIsSearchComplete`](#spawnpointsissearchcomplete) · [`SpawnpointsIsSearchFailed`](#spawnpointsissearchfailed) · [`SpawnpointsStartSearch`](#spawnpointsstartsearch) · [`SpawnpointsStartSearchInAngledArea`](#spawnpointsstartsearchinangledarea) · [`SpecialFunctionDoNotUse`](#specialfunctiondonotuse) · [`StopAnyPedModelBeingSuppressed`](#stopanypedmodelbeingsuppressed) · [`StopPedWeaponFiringWhenDropped`](#stoppedweaponfiringwhendropped) · [`TakeOwnershipOfSynchronizedScene`](#takeownershipofsynchronizedscene) · [`UnregisterPedheadshot`](#unregisterpedheadshot) · [`UpdatePedHeadBlendData`](#updatepedheadblenddata) · [`WasPedKilledByStealth`](#waspedkilledbystealth) · [`WasPedKilledByTakedown`](#waspedkilledbytakedown) · [`WasPedKnockedOut`](#waspedknockedout) · [`WasPedSkeletonUpdated`](#waspedskeletonupdated)

---
### SetPedToLoadCover

`SET_PED_TO_LOAD_COVER` · hash `0x332B562EEDA62399` · jhash `0xCF94BA97` · **Cliente**

```lua
SetPedToLoadCover(ped, toggle)
```
```c
void SET_PED_TO_LOAD_COVER(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedToRagdoll

`SET_PED_TO_RAGDOLL` · hash `0xAE99FB955581844A` · jhash `0x83CB5052` · **Cliente · también en el servidor (RPC)**

```lua
local retval = SetPedToRagdoll(ped, minTime, maxTime, ragdollType, bAbortIfInjured, bAbortIfDead, bForceScriptControl)
```
```c
BOOL SET_PED_TO_RAGDOLL(Ped ped, int minTime, int maxTime, int ragdollType, BOOL bAbortIfInjured, BOOL bAbortIfDead, BOOL bForceScriptControl);
```

**Parámetros**

- `ped` (`Ped`): The ped to ragdoll.
- `minTime` (`int`): Time(ms) Ped is in ragdoll mode; only applies to ragdoll types 0 and not 1.
- `maxTime` (`int`)
- `ragdollType` (`int`)
- `bAbortIfInjured` (`BOOL`): unused
- `bAbortIfDead` (`BOOL`): unused
- `bForceScriptControl` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

p4/p5: Unusued in TU27

**Ragdoll Types**

**0**: CTaskNMRelax
**1**: CTaskNMScriptControl: Hardcoded not to work in networked environments.
**Else**: CTaskNMBalance

---
### SetPedToRagdollWithFall

`SET_PED_TO_RAGDOLL_WITH_FALL` · hash `0xD76632D99E4966C8` · jhash `0xFA12E286` · **Cliente · también en el servidor (RPC)**

```lua
local retval = SetPedToRagdollWithFall(ped, minTime, maxTime, nFallType, dirX, dirY, dirZ, fGroundHeight, grab1X, grab1Y, grab1Z, grab2X, grab2Y, grab2Z)
```
```c
BOOL SET_PED_TO_RAGDOLL_WITH_FALL(Ped ped, int minTime, int maxTime, int nFallType, float dirX, float dirY, float dirZ, float fGroundHeight, float grab1X, float grab1Y, float grab1Z, float grab2X, float grab2Y, float grab2Z);
```

**Parámetros**

- `ped` (`Ped`): The ped to ragdoll.
- `minTime` (`int`)
- `maxTime` (`int`)
- `nFallType` (`int`): The type of fall.
- `dirX` (`float`): The x direction of the fall.
- `dirY` (`float`): The y direction of the fall.
- `dirZ` (`float`): The z direction of the fall.
- `fGroundHeight` (`float`): The ground height (z).
- `grab1X` (`float`): unused
- `grab1Y` (`float`): unused
- `grab1Z` (`float`): unused
- `grab2X` (`float`): unused
- `grab2Y` (`float`): unused
- `grab2Z` (`float`): unused

**Devuelve:** `BOOL`

**Descripción oficial:**

```cpp
enum eNMFallType {
    TYPE_FROM_HIGH = 0,
    TYPE_OVER_WALL = 1,
    TYPE_DOWN_STAIRS = 2,
    TYPE_DIE_TYPES = 3,
    TYPE_DIE_FROM_HIGH = 4,
    TYPE_DIE_OVER_WALL = 5,
    TYPE_DIE_DOWN_STAIRS = 6
}
```

```
Return variable is never used in R*'s scripts.  
Not sure what p2 does. It seems like it would be a time judging by it's usage in R*'s scripts, but didn't seem to affect anything in my testings.  
x, y, and z are coordinates, most likely to where the ped will fall.  
p7 is probably the force of the fall, but untested, so I left the variable name the same.  
p8 to p13 are always 0f in R*'s scripts.  
(Simplified) Example of the usage of the function from R*'s scripts:  
ped::set_ped_to_ragdoll_with_fall(ped, 1500, 2000, 1, -entity::get_entity_forward_vector(ped), 1f, 0f, 0f, 0f, 0f, 0f, 0f);  
```

---
### SetPedUsingActionMode

`SET_PED_USING_ACTION_MODE` · hash `0xD75ACCF5E0FB5367` · jhash `0x8802F696` · **Cliente**

```lua
SetPedUsingActionMode(ped, p1, p2, action)
```
```c
void SET_PED_USING_ACTION_MODE(Ped ped, BOOL p1, int p2, char* action);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `p2` (`int`)
- `action` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
p2 is usually -1 in the scripts. action is either 0 or "DEFAULT_ACTION".  
```

---
### SetPedVehicleForcedSeatUsage

`SET_PED_VEHICLE_FORCED_SEAT_USAGE` · hash `0x952F06BEECD775CC` · jhash `0x79CA237B` · **Cliente**

```lua
SetPedVehicleForcedSeatUsage(ped, vehicle, seatIndex, flags)
```
```c
void SET_PED_VEHICLE_FORCED_SEAT_USAGE(Ped ped, Vehicle vehicle, int seatIndex, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](VEHICLE-1.md#isvehicleseatfree).
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 5: Any p4
```

**Nombres antiguos (alias):** `0x952F06BEECD775CC` (`N_0x952f06beecd775cc`)

---
### SetPedVisualFieldCenterAngle

`SET_PED_VISUAL_FIELD_CENTER_ANGLE` · hash `0x3B6405E8AB34A907` · jhash `0xE57202A1` · **Cliente**

```lua
SetPedVisualFieldCenterAngle(ped, angle)
```
```c
void SET_PED_VISUAL_FIELD_CENTER_ANGLE(Ped ped, float angle);
```

**Parámetros**

- `ped` (`Ped`)
- `angle` (`float`)

**Devuelve:** `void`

---
### SetPedVisualFieldMaxAngle

`SET_PED_VISUAL_FIELD_MAX_ANGLE` · hash `0x70793BDCA1E854D4` · jhash `0x0CEA0F9A` · **Cliente**

```lua
SetPedVisualFieldMaxAngle(ped, value)
```
```c
void SET_PED_VISUAL_FIELD_MAX_ANGLE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedVisualFieldMaxElevationAngle

`SET_PED_VISUAL_FIELD_MAX_ELEVATION_ANGLE` · hash `0x78D0B67629D75856` · jhash `0x39D9102F` · **Cliente**

```lua
SetPedVisualFieldMaxElevationAngle(ped, angle)
```
```c
void SET_PED_VISUAL_FIELD_MAX_ELEVATION_ANGLE(Ped ped, float angle);
```

**Parámetros**

- `ped` (`Ped`)
- `angle` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native refers to the field of vision the ped has above them, starting at 0 degrees. 90f would let the ped see enemies directly above of them.  
```

---
### SetPedVisualFieldMinAngle

`SET_PED_VISUAL_FIELD_MIN_ANGLE` · hash `0x2DB492222FB21E26` · jhash `0x72E2E18B` · **Cliente**

```lua
SetPedVisualFieldMinAngle(ped, value)
```
```c
void SET_PED_VISUAL_FIELD_MIN_ANGLE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedVisualFieldMinElevationAngle

`SET_PED_VISUAL_FIELD_MIN_ELEVATION_ANGLE` · hash `0x7A276EB2C224D70F` · jhash `0x5CC2F1B8` · **Cliente**

```lua
SetPedVisualFieldMinElevationAngle(ped, angle)
```
```c
void SET_PED_VISUAL_FIELD_MIN_ELEVATION_ANGLE(Ped ped, float angle);
```

**Parámetros**

- `ped` (`Ped`)
- `angle` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native refers to the field of vision the ped has below them, starting at 0 degrees. The angle value should be negative.  
```

---
### SetPedVisualFieldPeripheralRange

`SET_PED_VISUAL_FIELD_PERIPHERAL_RANGE` · hash `0x9C74B0BC831B753A` · jhash `0xFDF2F7C2` · **Cliente**

```lua
SetPedVisualFieldPeripheralRange(ped, range)
```
```c
void SET_PED_VISUAL_FIELD_PERIPHERAL_RANGE(Ped ped, float range);
```

**Parámetros**

- `ped` (`Ped`)
- `range` (`float`)

**Devuelve:** `void`

---
### SetPedWeaponMovementClipset

`SET_PED_WEAPON_MOVEMENT_CLIPSET` · hash `0x2622E35B77D3ACA2` · jhash `0xF8BE54DC` · **Cliente**

```lua
SetPedWeaponMovementClipset(ped, clipSet)
```
```c
void SET_PED_WEAPON_MOVEMENT_CLIPSET(Ped ped, char* clipSet);
```

**Parámetros**

- `ped` (`Ped`)
- `clipSet` (`char*`)

**Devuelve:** `void`

---
### SetPedWetnessEnabledThisFrame

`SET_PED_WETNESS_ENABLED_THIS_FRAME` · hash `0xB5485E4907B53019` · jhash `0xBDE749F7` · **Cliente**

```lua
SetPedWetnessEnabledThisFrame(ped)
```
```c
void SET_PED_WETNESS_ENABLED_THIS_FRAME(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
combined with PED::SET_PED_WETNESS_HEIGHT(), this native makes the ped drenched in water up to the height specified in the other function  
```

---
### SetPedWetnessHeight

`SET_PED_WETNESS_HEIGHT` · hash `0x44CB6447D2571AA0` · jhash `0x7B33289A` · **Cliente**

```lua
SetPedWetnessHeight(ped, height)
```
```c
void SET_PED_WETNESS_HEIGHT(Ped ped, float height);
```

**Parámetros**

- `ped` (`Ped`)
- `height` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
It adds the wetness level to the player clothing/outfit. As if player just got out from water surface.  
```

---
### SetPopControlSphereThisFrame

`SET_POP_CONTROL_SPHERE_THIS_FRAME` · hash `0xD8C3BE3EE94CAF2D` · jhash `0x4BBE5E2C` · **Cliente**

```lua
SetPopControlSphereThisFrame(x, y, z, min, max)
```
```c
void SET_POP_CONTROL_SPHERE_THIS_FRAME(float x, float y, float z, float min, float max);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `min` (`float`)
- `max` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Min and max are usually 100.0 and 200.0
```

**Nombres antiguos (alias):** `0xD8C3BE3EE94CAF2D` (`N_0xd8c3be3ee94caf2d`)

---
### SetRagdollBlockingFlags

`SET_RAGDOLL_BLOCKING_FLAGS` · hash `0x26695EC767728D84` · jhash `0x9C8F830D` · **Cliente**

```lua
SetRagdollBlockingFlags(ped, flags)
```
```c
void SET_RAGDOLL_BLOCKING_FLAGS(Ped ped, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Works for both player and peds, but some flags don't seem to work for the player (1, for example)  
1 - Blocks ragdolling when shot.  
2 - Blocks ragdolling when hit by a vehicle. The ped still might play a falling animation.  
4 - Blocks ragdolling when set on fire.  
-----------------------------------------------------------------------  
There seem to be 26 flags  
```

**Nombres antiguos (alias):** `0x26695EC767728D84` (`N_0x26695ec767728d84`), `_SET_PED_RAGDOLL_BLOCKING_FLAGS` (`SetPedRagdollBlockingFlags`)

---
### SetRelationshipBetweenGroups

`SET_RELATIONSHIP_BETWEEN_GROUPS` · hash `0xBF25EB89375A37AD` · jhash `0xD4A215BA` · **Cliente**

```lua
SetRelationshipBetweenGroups(relationship, group1, group2)
```
```c
void SET_RELATIONSHIP_BETWEEN_GROUPS(int relationship, Hash group1, Hash group2);
```

**Parámetros**

- `relationship` (`int`)
- `group1` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `group2` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the relationship between two groups. This should be called twice (once for each group).  
Relationship types:  
0 = Companion  
1 = Respect  
2 = Like  
3 = Neutral  
4 = Dislike  
5 = Hate  
255 = Pedestrians  
Example:  
PED::SET_RELATIONSHIP_BETWEEN_GROUPS(2, l_1017, 0xA49E591C);  
PED::SET_RELATIONSHIP_BETWEEN_GROUPS(2, 0xA49E591C, l_1017);  
```

---
### SetRelationshipGroupDontAffectWantedLevel

`_SET_RELATIONSHIP_GROUP_DONT_AFFECT_WANTED_LEVEL` · hash `0x5615E0C5EB2BC6E2` · **Cliente**

```lua
SetRelationshipGroupDontAffectWantedLevel(group, p1)
```
```c
void _SET_RELATIONSHIP_GROUP_DONT_AFFECT_WANTED_LEVEL(Hash group, BOOL p1);
```

**Parámetros**

- `group` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5615E0C5EB2BC6E2` (`N_0x5615e0c5eb2bc6e2`)

---
### SetScenarioPedDensityMultiplierThisFrame

`SET_SCENARIO_PED_DENSITY_MULTIPLIER_THIS_FRAME` · hash `0x7A556143A1C03898` · jhash `0x2909ABF0` · **Cliente**

```lua
SetScenarioPedDensityMultiplierThisFrame(interiorMult, exteriorMult)
```
```c
void SET_SCENARIO_PED_DENSITY_MULTIPLIER_THIS_FRAME(float interiorMult, float exteriorMult);
```

**Parámetros**

- `interiorMult` (`float`): Multiplier for ped scenarios inside interiors.
- `exteriorMult` (`float`): Multiplier for ped scenarios outside interiors.

**Devuelve:** `void`

**Descripción oficial:**

Set the number of scenario peds on the entire map

---
### SetScenarioPedsSpawnInSphereArea

`SET_SCENARIO_PEDS_SPAWN_IN_SPHERE_AREA` · hash `0x28157D43CF600981` · jhash `0x80EAD297` · **Cliente**

```lua
SetScenarioPedsSpawnInSphereArea(x, y, z, range, p4)
```
```c
void SET_SCENARIO_PEDS_SPAWN_IN_SPHERE_AREA(float x, float y, float z, float range, int p4);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `range` (`float`)
- `p4` (`int`)

**Devuelve:** `void`

---
### SetScenarioPedsToBeReturnedByNextCommand

`SET_SCENARIO_PEDS_TO_BE_RETURNED_BY_NEXT_COMMAND` · hash `0x14F19A8782C8071E` · jhash `0x85615FD0` · **Cliente**

```lua
SetScenarioPedsToBeReturnedByNextCommand(value)
```
```c
void SET_SCENARIO_PEDS_TO_BE_RETURNED_BY_NEXT_COMMAND(BOOL value);
```

**Parámetros**

- `value` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets a value indicating whether scenario peds should be returned by the next call to a command that returns peds. Eg. GET_CLOSEST_PED.  
```

---
### SetScriptedAnimSeatOffset

`SET_SCRIPTED_ANIM_SEAT_OFFSET` · hash `0x5917BBA32D06C230` · jhash `0x7CEFFA45` · **Cliente**

```lua
SetScriptedAnimSeatOffset(ped, p1)
```
```c
void SET_SCRIPTED_ANIM_SEAT_OFFSET(Ped ped, float p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)

**Devuelve:** `void`

---
### SetScriptedConversionCoordThisFrame

`SET_SCRIPTED_CONVERSION_COORD_THIS_FRAME` · hash `0x5086C7843552CF85` · jhash `0x25EA2AA5` · **Cliente**

```lua
SetScriptedConversionCoordThisFrame(x, y, z)
```
```c
void SET_SCRIPTED_CONVERSION_COORD_THIS_FRAME(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### SetSynchronizedSceneHoldLastFrame

`SET_SYNCHRONIZED_SCENE_HOLD_LAST_FRAME` · hash `0x394B9CD12435C981` · jhash `0x2DE48DA1` · **Cliente**

```lua
SetSynchronizedSceneHoldLastFrame(sceneID, toggle)
```
```c
void SET_SYNCHRONIZED_SCENE_HOLD_LAST_FRAME(int sceneID, BOOL toggle);
```

**Parámetros**

- `sceneID` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x394B9CD12435C981` (`N_0x394b9cd12435c981`), `_SET_SYNCHRONIZED_SCENE_OCCLUSION_PORTAL` (`SetSynchronizedSceneOcclusionPortal`)

---
### SetSynchronizedSceneLooped

`SET_SYNCHRONIZED_SCENE_LOOPED` · hash `0xD9A897A4C6C2974F` · jhash `0x32ED9F82` · **Cliente**

```lua
SetSynchronizedSceneLooped(sceneID, toggle)
```
```c
void SET_SYNCHRONIZED_SCENE_LOOPED(int sceneID, BOOL toggle);
```

**Parámetros**

- `sceneID` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetSynchronizedSceneOrigin

`SET_SYNCHRONIZED_SCENE_ORIGIN` · hash `0x6ACF6B7225801CD7` · jhash `0x2EC2A0B2` · **Cliente**

```lua
SetSynchronizedSceneOrigin(sceneID, x, y, z, roll, pitch, yaw, p7)
```
```c
void SET_SYNCHRONIZED_SCENE_ORIGIN(int sceneID, float x, float y, float z, float roll, float pitch, float yaw, BOOL p7);
```

**Parámetros**

- `sceneID` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `roll` (`float`)
- `pitch` (`float`)
- `yaw` (`float`)
- `p7` (`BOOL`)

**Devuelve:** `void`

---
### SetSynchronizedScenePhase

`SET_SYNCHRONIZED_SCENE_PHASE` · hash `0x734292F4F0ABF6D0` · jhash `0xF5AB0D98` · **Cliente**

```lua
SetSynchronizedScenePhase(sceneID, phase)
```
```c
void SET_SYNCHRONIZED_SCENE_PHASE(int sceneID, float phase);
```

**Parámetros**

- `sceneID` (`int`)
- `phase` (`float`)

**Devuelve:** `void`

---
### SetSynchronizedSceneRate

`SET_SYNCHRONIZED_SCENE_RATE` · hash `0xB6C49F8A5E295A5D` · jhash `0xF10112FD` · **Cliente**

```lua
SetSynchronizedSceneRate(sceneID, rate)
```
```c
void SET_SYNCHRONIZED_SCENE_RATE(int sceneID, float rate);
```

**Parámetros**

- `sceneID` (`int`)
- `rate` (`float`)

**Devuelve:** `void`

---
### SpawnpointsCancelSearch

`SPAWNPOINTS_CANCEL_SEARCH` · hash `0xFEE4A5459472A9F8` · jhash `0x492C9E46` · **Cliente**

```lua
SpawnpointsCancelSearch()
```
```c
void SPAWNPOINTS_CANCEL_SEARCH();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFEE4A5459472A9F8` (`N_0xfee4a5459472a9f8`)

---
### SpawnpointsGetNumSearchResults

`SPAWNPOINTS_GET_NUM_SEARCH_RESULTS` · hash `0xA635C11B8C44AFC2` · jhash `0xF46B4DC8` · **Cliente**

```lua
local retval = SpawnpointsGetNumSearchResults()
```
```c
int SPAWNPOINTS_GET_NUM_SEARCH_RESULTS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xA635C11B8C44AFC2` (`N_0xa635c11b8c44afc2`)

---
### SpawnpointsGetSearchResult

`SPAWNPOINTS_GET_SEARCH_RESULT` · hash `0x280C7E3AC7F56E90` · jhash `0x36A4AC65` · **Cliente**

```lua
local x, y, z = SpawnpointsGetSearchResult(randomInt)
```
```c
void SPAWNPOINTS_GET_SEARCH_RESULT(int randomInt, float* x, float* y, float* z);
```

**Parámetros**

- `randomInt` (`int`)
- `x` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `y` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `z` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x280C7E3AC7F56E90` (`N_0x280c7e3ac7f56e90`)

---
### SpawnpointsGetSearchResultFlags

`SPAWNPOINTS_GET_SEARCH_RESULT_FLAGS` · hash `0xB782F8238512BAD5` · jhash `0xBA699DDF` · **Cliente**

```lua
local p1 = SpawnpointsGetSearchResultFlags(p0, p1)
```
```c
void SPAWNPOINTS_GET_SEARCH_RESULT_FLAGS(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB782F8238512BAD5` (`N_0xb782f8238512bad5`)

---
### SpawnpointsIsSearchActive

`SPAWNPOINTS_IS_SEARCH_ACTIVE` · hash `0x3C67506996001F5E` · jhash `0x814A28F4` · **Cliente**

```lua
local retval = SpawnpointsIsSearchActive()
```
```c
BOOL SPAWNPOINTS_IS_SEARCH_ACTIVE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3C67506996001F5E` (`N_0x3c67506996001f5e`)

---
### SpawnpointsIsSearchComplete

`SPAWNPOINTS_IS_SEARCH_COMPLETE` · hash `0xA586FBEB32A53DBB` · jhash `0x0B60D2BA` · **Cliente**

```lua
local retval = SpawnpointsIsSearchComplete()
```
```c
BOOL SPAWNPOINTS_IS_SEARCH_COMPLETE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA586FBEB32A53DBB` (`N_0xa586fbeb32a53dbb`)

---
### SpawnpointsIsSearchFailed

`SPAWNPOINTS_IS_SEARCH_FAILED` · hash `0xF445DE8DA80A1792` · jhash `0x6B83ABDF` · **Cliente**

```lua
local retval = SpawnpointsIsSearchFailed()
```
```c
BOOL SPAWNPOINTS_IS_SEARCH_FAILED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF445DE8DA80A1792` (`N_0xf445de8da80a1792`)

---
### SpawnpointsStartSearch

`SPAWNPOINTS_START_SEARCH` · hash `0x2DF9038C90AD5264` · jhash `0x909A1D76` · **Cliente**

```lua
SpawnpointsStartSearch(p0, p1, p2, p3, p4, interiorFlags, scale, duration)
```
```c
void SPAWNPOINTS_START_SEARCH(float p0, float p1, float p2, float p3, float p4, int interiorFlags, float scale, int duration);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `interiorFlags` (`int`)
- `scale` (`float`)
- `duration` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2DF9038C90AD5264` (`N_0x2df9038c90ad5264`)

---
### SpawnpointsStartSearchInAngledArea

`SPAWNPOINTS_START_SEARCH_IN_ANGLED_AREA` · hash `0xB2AFF10216DEFA2F` · jhash `0x4AAD0ECB` · **Cliente**

```lua
SpawnpointsStartSearchInAngledArea(x, y, z, p3, p4, p5, p6, interiorFlags, scale, duration)
```
```c
void SPAWNPOINTS_START_SEARCH_IN_ANGLED_AREA(float x, float y, float z, float p3, float p4, float p5, float p6, int interiorFlags, float scale, int duration);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `interiorFlags` (`int`)
- `scale` (`float`)
- `duration` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB2AFF10216DEFA2F` (`N_0xb2aff10216defa2f`)

---
### SpecialFunctionDoNotUse

`SPECIAL_FUNCTION_DO_NOT_USE` · hash `0xF9ACF4A08098EA25` · jhash `0x141CC936` · **Cliente**

```lua
SpecialFunctionDoNotUse(ped, noCollisionUntilClear)
```
```c
void SPECIAL_FUNCTION_DO_NOT_USE(Ped ped, BOOL noCollisionUntilClear);
```

**Parámetros**

- `ped` (`Ped`)
- `noCollisionUntilClear` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Kicks the ped from the current vehicle and keeps the rendering-focus on this ped (also disables its collision). If doing this for your player ped, you'll still be able to drive the vehicle.\
Only to be used in very specific situations where the ped needs to be inside the car still but not attached.

**Nombres antiguos (alias):** `0xF9ACF4A08098EA25` (`N_0xf9acf4a08098ea25`)

---
### StopAnyPedModelBeingSuppressed

`STOP_ANY_PED_MODEL_BEING_SUPPRESSED` · hash `0xB47BD05FA66B40CF` · jhash `0x5AD7DC55` · **Cliente**

```lua
StopAnyPedModelBeingSuppressed()
```
```c
void STOP_ANY_PED_MODEL_BEING_SUPPRESSED();
```

**Devuelve:** `void`

---
### StopPedWeaponFiringWhenDropped

`STOP_PED_WEAPON_FIRING_WHEN_DROPPED` · hash `0xC158D28142A34608` · jhash `0x4AC3421E` · **Cliente**

```lua
StopPedWeaponFiringWhenDropped(ped)
```
```c
void STOP_PED_WEAPON_FIRING_WHEN_DROPPED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### TakeOwnershipOfSynchronizedScene

`TAKE_OWNERSHIP_OF_SYNCHRONIZED_SCENE` · hash `0xCD9CC7E200A52A6F` · jhash `0xBF7F9035` · **Cliente**

```lua
TakeOwnershipOfSynchronizedScene(scene)
```
```c
void TAKE_OWNERSHIP_OF_SYNCHRONIZED_SCENE(int scene);
```

**Parámetros**

- `scene` (`int`): Scene ID returned by [`CREATE_SYNCHRONIZED_SCENE`](PED-1.md#createsynchronizedscene)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCD9CC7E200A52A6F` (`N_0xcd9cc7e200a52a6f`), `_DISPOSE_SYNCHRONIZED_SCENE` (`DisposeSynchronizedScene`)

---
### UnregisterPedheadshot

`UNREGISTER_PEDHEADSHOT` · hash `0x96B1361D9B24C2FF` · jhash `0x0879AE45` · **Cliente**

```lua
UnregisterPedheadshot(id)
```
```c
void UNREGISTER_PEDHEADSHOT(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
gtaforums.com/topic/885580-ped-headshotmugshot-txd/  
```

---
### UpdatePedHeadBlendData

`UPDATE_PED_HEAD_BLEND_DATA` · hash `0x723538F61C647C5A` · jhash `0x5CB76219` · **Cliente**

```lua
UpdatePedHeadBlendData(ped, shapeMix, skinMix, thirdMix)
```
```c
void UPDATE_PED_HEAD_BLEND_DATA(Ped ped, float shapeMix, float skinMix, float thirdMix);
```

**Parámetros**

- `ped` (`Ped`)
- `shapeMix` (`float`)
- `skinMix` (`float`)
- `thirdMix` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

See [`SET_PED_HEAD_BLEND_DATA`](../cfx/servidor.md#setpedheadblenddata)

---
### WasPedKilledByStealth

`WAS_PED_KILLED_BY_STEALTH` · hash `0xF9800AA1A771B000` · jhash `0x2EA4B54E` · **Cliente**

```lua
local retval = WasPedKilledByStealth(ped)
```
```c
BOOL WAS_PED_KILLED_BY_STEALTH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): Ped index

**Devuelve:** `BOOL`

**Descripción oficial:**

Verifies whether ped was eliminated through stealth.

---
### WasPedKilledByTakedown

`WAS_PED_KILLED_BY_TAKEDOWN` · hash `0x7F08E26039C7347C` · jhash `0xBDD3CE69` · **Cliente**

```lua
local retval = WasPedKilledByTakedown(ped)
```
```c
BOOL WAS_PED_KILLED_BY_TAKEDOWN(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### WasPedKnockedOut

`WAS_PED_KNOCKED_OUT` · hash `0x61767F73EACEED21` · jhash `0x3993092B` · **Cliente**

```lua
local retval = WasPedKnockedOut(ped)
```
```c
BOOL WAS_PED_KNOCKED_OUT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x61767F73EACEED21` (`N_0x61767f73eaceed21`)

---
### WasPedSkeletonUpdated

`WAS_PED_SKELETON_UPDATED` · hash `0x11B499C1E0FF8559` · jhash `0xF7E2FBAD` · **Cliente**

```lua
local retval = WasPedSkeletonUpdated(ped)
```
```c
BOOL WAS_PED_SKELETON_UPDATED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Despite this function's name, it simply returns whether the specified handle is a Ped.  
```

---
