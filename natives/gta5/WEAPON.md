# Natives de GTA V — WEAPON

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `WEAPON`: **122** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddAmmoToPed`](#addammotoped) · [`AddAmmoToPedByType`](#addammotopedbytype) · [`CanUseWeaponOnParachute`](#canuseweapononparachute) · [`ClearEntityLastWeaponDamage`](#clearentitylastweapondamage) · [`ClearPedLastWeaponDamage`](#clearpedlastweapondamage) · [`CreateAirDefenceAngledArea`](#createairdefenceangledarea) · [`CreateAirDefenceSphere`](#createairdefencesphere) · [`CreateWeaponObject`](#createweaponobject) · [`DoesAirDefenseZoneExist`](#doesairdefensezoneexist) · [`DoesWeaponTakeWeaponComponent`](#doesweapontakeweaponcomponent) · [`EnableLaserSightRendering`](#enablelasersightrendering) · [`ExplodeProjectiles`](#explodeprojectiles) · [`FireAirDefenseWeapon`](#fireairdefenseweapon) · [`GetAmmoInClip`](#getammoinclip) · [`GetAmmoInPedWeapon`](#getammoinpedweapon) · [`GetAmmoInVehicleWeaponClip`](#getammoinvehicleweaponclip) · [`GetBestPedWeapon`](#getbestpedweapon) · [`GetCurrentPedVehicleWeapon`](#getcurrentpedvehicleweapon) · [`GetCurrentPedWeapon`](#getcurrentpedweapon) · [`GetCurrentPedWeaponEntityIndex`](#getcurrentpedweaponentityindex) · [`GetIsPedGadgetEquipped`](#getispedgadgetequipped) · [`GetLockonDistanceOfCurrentPedWeapon`](#getlockondistanceofcurrentpedweapon) · [`GetMaxAmmo`](#getmaxammo) · [`GetMaxAmmoByType`](#getmaxammobytype) · [`GetMaxAmmoInClip`](#getmaxammoinclip) · [`GetMaxRangeOfCurrentPedWeapon`](#getmaxrangeofcurrentpedweapon) · [`GetPedAmmoByType`](#getpedammobytype) · [`GetPedAmmoTypeFromWeapon`](#getpedammotypefromweapon) · [`GetPedAmmoTypeFromWeapon_2`](#getpedammotypefromweapon_2) · [`GetPedLastWeaponImpactCoord`](#getpedlastweaponimpactcoord) · [`GetPedWeaponLiveryColor`](#getpedweaponliverycolor) · [`GetPedWeaponTintIndex`](#getpedweapontintindex) · [`GetPedWeapontypeInSlot`](#getpedweapontypeinslot) · [`GetSelectedPedWeapon`](#getselectedpedweapon) · [`GetTimeBeforeVehicleWeaponReloadFinishes`](#gettimebeforevehicleweaponreloadfinishes) · [`GetVehicleWeaponReloadTime`](#getvehicleweaponreloadtime) · [`GetWeaponClipSize`](#getweaponclipsize) · [`GetWeaponComponentHudStats`](#getweaponcomponenthudstats) · [`GetWeaponComponentTypeModel`](#getweaponcomponenttypemodel) · [`GetWeaponComponentVariantExtraComponentCount`](#getweaponcomponentvariantextracomponentcount) · [`GetWeaponComponentVariantExtraComponentModel`](#getweaponcomponentvariantextracomponentmodel) · [`GetWeaponDamage`](#getweapondamage) · [`GetWeaponDamageType`](#getweapondamagetype) · [`GetWeaponHudStats`](#getweaponhudstats) · [`GetWeaponObjectFromPed`](#getweaponobjectfromped) · [`GetWeaponObjectLiveryColor`](#getweaponobjectliverycolor) · [`GetWeaponObjectTintIndex`](#getweaponobjecttintindex) · [`GetWeaponTimeBetweenShots`](#getweapontimebetweenshots) · [`GetWeaponTintCount`](#getweapontintcount) · [`GetWeapontypeGroup`](#getweapontypegroup) · [`GetWeapontypeModel`](#getweapontypemodel) · [`GetWeapontypeSlot`](#getweapontypeslot) · [`GiveDelayedWeaponToPed`](#givedelayedweapontoped) · [`GiveLoadoutToPed`](#giveloadouttoped) · [`GiveWeaponComponentToPed`](#giveweaponcomponenttoped) · [`GiveWeaponComponentToWeaponObject`](#giveweaponcomponenttoweaponobject) · [`GiveWeaponObjectToPed`](#giveweaponobjecttoped) · [`GiveWeaponToPed`](#giveweapontoped) · [`HasEntityBeenDamagedByWeapon`](#hasentitybeendamagedbyweapon) · [`HasPedBeenDamagedByWeapon`](#haspedbeendamagedbyweapon) · [`HasPedGotWeapon`](#haspedgotweapon) · [`HasPedGotWeaponComponent`](#haspedgotweaponcomponent) · [`HasVehicleGotProjectileAttached`](#hasvehiclegotprojectileattached) · [`HasWeaponAssetLoaded`](#hasweaponassetloaded) · [`HasWeaponGotWeaponComponent`](#hasweapongotweaponcomponent) · [`HasWeaponReloadingInVehicle`](#hasweaponreloadinginvehicle) · [`HidePedWeaponForScriptedCutscene`](#hidepedweaponforscriptedcutscene) · [`IsAnyAirDefenseZoneInsideSphere`](#isanyairdefensezoneinsidesphere) · [`IsFlashLightOn`](#isflashlighton) · [`IsPedArmed`](#ispedarmed) · [`IsPedCurrentWeaponSilenced`](#ispedcurrentweaponsilenced) · [`IsPedWeaponComponentActive`](#ispedweaponcomponentactive) · [`IsPedWeaponReadyToShoot`](#ispedweaponreadytoshoot) · [`IsWeaponValid`](#isweaponvalid) · [`MakePedReload`](#makepedreload) · [`N_0x24c024ba8379a70a`](#n_0x24c024ba8379a70a) · [`N_0x977ca98939e82e4b`](#n_0x977ca98939e82e4b) · [`N_0xa2c9ac24b4061285`](#n_0xa2c9ac24b4061285) · [`N_0xe4dcec7fd5b739a5`](#n_0xe4dcec7fd5b739a5) · [`N_0xe6d2cedd370ff98e`](#n_0xe6d2cedd370ff98e) · [`RefillAmmoInstantly`](#refillammoinstantly) · [`RemoveAirDefenseZone`](#removeairdefensezone) · [`RemoveAllAirDefenseZones`](#removeallairdefensezones) · [`RemoveAllPedWeapons`](#removeallpedweapons) · [`RemoveAllProjectilesOfType`](#removeallprojectilesoftype) · [`RemoveWeaponAsset`](#removeweaponasset) · [`RemoveWeaponComponentFromPed`](#removeweaponcomponentfromped) · [`RemoveWeaponComponentFromWeaponObject`](#removeweaponcomponentfromweaponobject) · [`RemoveWeaponFromPed`](#removeweaponfromped) · [`RequestWeaponAsset`](#requestweaponasset) · [`RequestWeaponHighDetailModel`](#requestweaponhighdetailmodel) · [`SetAmmoInClip`](#setammoinclip) · [`SetAmmoInVehicleWeaponClip`](#setammoinvehicleweaponclip) · [`SetCanPedEquipAllWeapons`](#setcanpedequipallweapons) · [`SetCanPedEquipWeapon`](#setcanpedequipweapon) · [`SetCurrentPedVehicleWeapon`](#setcurrentpedvehicleweapon) · [`SetCurrentPedWeapon`](#setcurrentpedweapon) · [`SetFlashLightEnabled`](#setflashlightenabled) · [`SetFlashLightFadeDistance`](#setflashlightfadedistance) · [`SetPedAmmo`](#setpedammo) · [`SetPedAmmoByType`](#setpedammobytype) · [`SetPedAmmoToDrop`](#setpedammotodrop) · [`SetPedChanceOfFiringBlanks`](#setpedchanceoffiringblanks) · [`SetPedCurrentWeaponVisible`](#setpedcurrentweaponvisible) · [`SetPedCycleVehicleWeaponsOnly`](#setpedcyclevehicleweaponsonly) · [`SetPedDropsInventoryWeapon`](#setpeddropsinventoryweapon) · [`SetPedDropsWeapon`](#setpeddropsweapon) · [`SetPedDropsWeaponsWhenDead`](#setpeddropsweaponswhendead) · [`SetPedGadget`](#setpedgadget) · [`SetPedInfiniteAmmo`](#setpedinfiniteammo) · [`SetPedInfiniteAmmoClip`](#setpedinfiniteammoclip) · [`SetPedShootOrdnanceWeapon`](#setpedshootordnanceweapon) · [`SetPedWeaponLiveryColor`](#setpedweaponliverycolor) · [`SetPedWeaponTintIndex`](#setpedweapontintindex) · [`SetPickupAmmoAmountScaler`](#setpickupammoamountscaler) · [`SetPlayerAirDefenseZoneFlag`](#setplayerairdefensezoneflag) · [`SetWeaponAnimationOverride`](#setweaponanimationoverride) · [`SetWeaponDamageModifier`](#setweapondamagemodifier) · [`SetWeaponExplosionRadiusMultiplier`](#setweaponexplosionradiusmultiplier) · [`SetWeaponObjectLiveryColor`](#setweaponobjectliverycolor) · [`SetWeaponObjectTintIndex`](#setweaponobjecttintindex) · [`TriggerVehicleWeaponReload`](#triggervehicleweaponreload)

---
### AddAmmoToPed

`ADD_AMMO_TO_PED` · hash `0x78F0424C34306220` · jhash `0x7F0580C7` · **Cliente**

```lua
AddAmmoToPed(ped, weaponHash, ammo)
```
```c
void ADD_AMMO_TO_PED(Ped ped, Hash weaponHash, int ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int`)

**Devuelve:** `void`

---
### AddAmmoToPedByType

`_ADD_AMMO_TO_PED_BY_TYPE` · hash `0x2472622CE1F2D45F` · **Cliente**

```lua
AddAmmoToPedByType(ped, ammoType, ammo)
```
```c
void _ADD_AMMO_TO_PED_BY_TYPE(Ped ped, Hash ammoType, int ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `ammoType` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2472622CE1F2D45F` (`N_0x2472622ce1f2d45f`), `_ADD_PED_AMMO` (`AddPedAmmo`)

---
### CanUseWeaponOnParachute

`CAN_USE_WEAPON_ON_PARACHUTE` · hash `0xBC7BE5ABC0879F74` · jhash `0x135E7AD4` · **Cliente**

```lua
local retval = CanUseWeaponOnParachute(weaponHash)
```
```c
BOOL CAN_USE_WEAPON_ON_PARACHUTE(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
this returns if you can use the weapon while using a parachute  
```

---
### ClearEntityLastWeaponDamage

`CLEAR_ENTITY_LAST_WEAPON_DAMAGE` · hash `0xAC678E40BE7C74D2` · jhash `0xCEC2732B` · **Cliente**

```lua
ClearEntityLastWeaponDamage(entity)
```
```c
void CLEAR_ENTITY_LAST_WEAPON_DAMAGE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### ClearPedLastWeaponDamage

`CLEAR_PED_LAST_WEAPON_DAMAGE` · hash `0x0E98F88A24C5F4B8` · jhash `0x52C68832` · **Cliente**

```lua
ClearPedLastWeaponDamage(ped)
```
```c
void CLEAR_PED_LAST_WEAPON_DAMAGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

Does NOT seem to work with HAS_PED_BEEN_DAMAGED_BY_WEAPON. Use CLEAR_ENTITY_LAST_WEAPON_DAMAGE and HAS_ENTITY_BEEN_DAMAGED_BY_WEAPON instead.

---
### CreateAirDefenceAngledArea

`CREATE_AIR_DEFENCE_ANGLED_AREA` · hash `0x9DA58CDBF6BDBC08` · jhash `0x7F1E89F4` · **Cliente**

```lua
local retval = CreateAirDefenceAngledArea(srcCoord1X, srcCoord1Y, srcCoord1Z, srcCoord2X, srcCoord2Y, srcCoord2Z, fWidth, weaponPositionX, weaponPositionY, weaponPositionZ, weaponHash)
```
```c
int CREATE_AIR_DEFENCE_ANGLED_AREA(float srcCoord1X, float srcCoord1Y, float srcCoord1Z, float srcCoord2X, float srcCoord2Y, float srcCoord2Z, float fWidth, float weaponPositionX, float weaponPositionY, float weaponPositionZ, Hash weaponHash);
```

**Parámetros**

- `srcCoord1X` (`float`)
- `srcCoord1Y` (`float`)
- `srcCoord1Z` (`float`)
- `srcCoord2X` (`float`)
- `srcCoord2Y` (`float`)
- `srcCoord2Z` (`float`)
- `fWidth` (`float`)
- `weaponPositionX` (`float`)
- `weaponPositionY` (`float`)
- `weaponPositionZ` (`float`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x9DA58CDBF6BDBC08` (`N_0x9da58cdbf6bdbc08`), `_CREATE_AIR_DEFENSE_AREA` (`CreateAirDefenseArea`)

---
### CreateAirDefenceSphere

`CREATE_AIR_DEFENCE_SPHERE` · hash `0x91EF34584710BE99` · jhash `0x767C2435` · **Cliente**

```lua
local retval = CreateAirDefenceSphere(x, y, z, radius, weaponPositionX, weaponPositionY, weaponPositionZ, weaponHash)
```
```c
int CREATE_AIR_DEFENCE_SPHERE(float x, float y, float z, float radius, float weaponPositionX, float weaponPositionY, float weaponPositionZ, Hash weaponHash);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`): Unknown float 150.0 is used in freemode script.
- `weaponPositionX` (`float`)
- `weaponPositionY` (`float`)
- `weaponPositionZ` (`float`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: weapon_air_defence_gun and 0 are used in the decompiled scripts.

**Devuelve:** `int` — Seems to be some sort of handle, result is += 1 any time this native is called.

**Descripción oficial:**

Both coordinates are from objects in the decompiled scripts.

Native related to [\_0xECDC202B25E5CF48](#setplayerairdefensezoneflag) p1 value. The only weapon hash used in the decompiled scripts is weapon_air_defence_gun. These two natives are used by the yacht script, decompiled scripts suggest it and the weapon hash used (valkyrie's rockets) are also used by yachts.

**Nombres antiguos (alias):** `0x91EF34584710BE99` (`N_0x91ef34584710be99`), `_CREATE_AIR_DEFENSE_SPHERE` (`CreateAirDefenseSphere`)

---
### CreateWeaponObject

`CREATE_WEAPON_OBJECT` · hash `0x9541D3CF0D398F36` · jhash `0x62F5987F` · **Cliente**

```lua
local retval = CreateWeaponObject(weaponHash, ammoCount, x, y, z, bCreateDefaultComponents, scale, customModelHash)
```
```c
Object CREATE_WEAPON_OBJECT(Hash weaponHash, int ammoCount, float x, float y, float z, BOOL bCreateDefaultComponents, float scale, int customModelHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of the weapon to create.
- `ammoCount` (`int`): The amount of ammo for the weapon.
- `x` (`float`): X coordinate for the weapon's position.
- `y` (`float`): Y coordinate for the weapon's position.
- `z` (`float`): Z coordinate for the weapon's position.
- `bCreateDefaultComponents` (`BOOL`): Boolean that indicates whether the default components should be created for that weapon (`true`/`false`).
- `scale` (`float`): The size of the object, to increase it, set the scale to a value greater than `1.0`.
- `customModelHash` (`int`): The hash of the custom model to use for the weapon object. Set to `0` if you do not intend to use a custom model hash.

**Devuelve:** `Object`

**Descripción oficial:**

Create a weapon object that cannot be attached to a ped. If you want to create a weapon object that can be attached to a ped, use [`CREATE_OBJECT`](../cfx/servidor.md#createobject) instead.

```
NativeDB Added Parameter 9: BOOL bRegisterAsNetworkObject
NativeDB Added Parameter 10: BOOL bScriptHostObject
```

---
### DoesAirDefenseZoneExist

`_DOES_AIR_DEFENSE_ZONE_EXIST` · hash `0xCD79A550999D7D4F` · **Cliente**

```lua
local retval = DoesAirDefenseZoneExist(zoneId)
```
```c
BOOL _DOES_AIR_DEFENSE_ZONE_EXIST(int zoneId);
```

**Parámetros**

- `zoneId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xCD79A550999D7D4F` (`N_0xcd79a550999d7d4f`)

---
### DoesWeaponTakeWeaponComponent

`DOES_WEAPON_TAKE_WEAPON_COMPONENT` · hash `0x5CEE3DF569CECAB0` · jhash `0xB1817BAA` · **Cliente**

```lua
local retval = DoesWeaponTakeWeaponComponent(weaponHash, componentHash)
```
```c
BOOL DOES_WEAPON_TAKE_WEAPON_COMPONENT(Hash weaponHash, Hash componentHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### EnableLaserSightRendering

`ENABLE_LASER_SIGHT_RENDERING` · hash `0xC8B46D7727D864AA` · jhash `0xE3438955` · **Cliente**

```lua
EnableLaserSightRendering(toggle)
```
```c
void ENABLE_LASER_SIGHT_RENDERING(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enables laser sight on any weapon.  
It doesn't work. Neither on tick nor OnKeyDown  
```

---
### ExplodeProjectiles

`EXPLODE_PROJECTILES` · hash `0xFC4BD125DE7611E4` · jhash `0x35A0B955` · **Cliente**

```lua
ExplodeProjectiles(ped, weaponHash, p2)
```
```c
void EXPLODE_PROJECTILES(Ped ped, Hash weaponHash, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
WEAPON::EXPLODE_PROJECTILES(PLAYER::PLAYER_PED_ID(), func_221(0x00000003), 0x00000001);  
```

---
### FireAirDefenseWeapon

`_FIRE_AIR_DEFENSE_WEAPON` · hash `0x44F1012B69313374` · **Cliente**

```lua
FireAirDefenseWeapon(zoneId, x, y, z)
```
```c
void _FIRE_AIR_DEFENSE_WEAPON(int zoneId, float x, float y, float z);
```

**Parámetros**

- `zoneId` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x44F1012B69313374` (`N_0x44f1012b69313374`)

---
### GetAmmoInClip

`GET_AMMO_IN_CLIP` · hash `0x2E1202248937775C` · jhash `0x73C100C3` · **Cliente**

```lua
local retval, ammo = GetAmmoInClip(ped, weaponHash, ammo)
```
```c
BOOL GET_AMMO_IN_CLIP(Ped ped, Hash weaponHash, int* ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### GetAmmoInPedWeapon

`GET_AMMO_IN_PED_WEAPON` · hash `0x015A522136D7F951` · jhash `0x0C755733` · **Cliente**

```lua
local retval = GetAmmoInPedWeapon(ped, weaponhash)
```
```c
int GET_AMMO_IN_PED_WEAPON(Ped ped, Hash weaponhash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponhash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
WEAPON::GET_AMMO_IN_PED_WEAPON(PLAYER::PLAYER_PED_ID(), a_0)  
From decompiled scripts  
Returns total ammo in weapon  
GTALua Example :  
natives.WEAPON.GET_AMMO_IN_PED_WEAPON(plyPed, WeaponHash)  
```

---
### GetAmmoInVehicleWeaponClip

`_GET_AMMO_IN_VEHICLE_WEAPON_CLIP` · hash `0x2857938C5D407AFA` · **Cliente**

```lua
local retval = GetAmmoInVehicleWeaponClip(vehicle, seat, ammo)
```
```c
BOOL _GET_AMMO_IN_VEHICLE_WEAPON_CLIP(Vehicle vehicle, int seat, int ammo);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `seat` (`int`)
- `ammo` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### GetBestPedWeapon

`GET_BEST_PED_WEAPON` · hash `0x8483E98E8B888AE2` · jhash `0xB998D444` · **Cliente**

```lua
local retval = GetBestPedWeapon(ped, ignoreAmmoCount)
```
```c
Hash GET_BEST_PED_WEAPON(Ped ped, BOOL ignoreAmmoCount);
```

**Parámetros**

- `ped` (`Ped`)
- `ignoreAmmoCount` (`BOOL`): If set to true, the best weapon can have no ammo, otherwise, it will return the best weapon with ammo. Default value is `0`.

**Devuelve:** `Hash` — The hash of the best weapon the specified ped has

---
### GetCurrentPedVehicleWeapon

`GET_CURRENT_PED_VEHICLE_WEAPON` · hash `0x1017582BCD3832DC` · jhash `0xF26C5D65` · **Cliente**

```lua
local retval, weaponHash = GetCurrentPedVehicleWeapon(ped, weaponHash)
```
```c
BOOL GET_CURRENT_PED_VEHICLE_WEAPON(Ped ped, Hash* weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### GetCurrentPedWeapon

`GET_CURRENT_PED_WEAPON` · hash `0x3A87E44BB9A01D54` · jhash `0xB0237302` · **Cliente**

```lua
local retval, weaponHash = GetCurrentPedWeapon(ped, p2)
```
```c
BOOL GET_CURRENT_PED_WEAPON(Ped ped, Hash* weaponHash, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
The return value seems to indicate returns true if the hash of the weapon object weapon equals the weapon hash.  
p2 seems to be 1 most of the time; and is not implemented.
```

---
### GetCurrentPedWeaponEntityIndex

`GET_CURRENT_PED_WEAPON_ENTITY_INDEX` · hash `0x3B390A939AF0B5FC` · jhash `0x5D73CD20` · **Cliente**

```lua
local retval = GetCurrentPedWeaponEntityIndex(ped)
```
```c
Entity GET_CURRENT_PED_WEAPON_ENTITY_INDEX(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Entity`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### GetIsPedGadgetEquipped

`GET_IS_PED_GADGET_EQUIPPED` · hash `0xF731332072F5156C` · jhash `0x8DDD0B5B` · **Cliente**

```lua
local retval = GetIsPedGadgetEquipped(ped, gadgetHash)
```
```c
BOOL GET_IS_PED_GADGET_EQUIPPED(Ped ped, Hash gadgetHash);
```

**Parámetros**

- `ped` (`Ped`)
- `gadgetHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
gadgetHash - was always 0xFBAB5776 ("GADGET_PARACHUTE").  
```

---
### GetLockonDistanceOfCurrentPedWeapon

`GET_LOCKON_DISTANCE_OF_CURRENT_PED_WEAPON` · hash `0x840F03E9041E2C9C` · jhash `0x3612110D` · **Cliente**

```lua
local retval = GetLockonDistanceOfCurrentPedWeapon(ped)
```
```c
float GET_LOCKON_DISTANCE_OF_CURRENT_PED_WEAPON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x840F03E9041E2C9C` (`N_0x840f03e9041e2c9c`), `_GET_LOCKON_RANGE_OF_CURRENT_PED_WEAPON` (`GetLockonRangeOfCurrentPedWeapon`)

---
### GetMaxAmmo

`GET_MAX_AMMO` · hash `0xDC16122C7A20C933` · jhash `0x0B294796` · **Cliente**

```lua
local retval, ammo = GetMaxAmmo(ped, weaponHash, ammo)
```
```c
BOOL GET_MAX_AMMO(Ped ped, Hash weaponHash, int* ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### GetMaxAmmoByType

`_GET_MAX_AMMO_BY_TYPE` · hash `0x585847C5E4E11709` · **Cliente**

```lua
local retval, ammo = GetMaxAmmoByType(ped, ammoType, ammo)
```
```c
BOOL _GET_MAX_AMMO_BY_TYPE(Ped ped, Hash ammoType, int* ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `ammoType` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x585847C5E4E11709` (`N_0x585847c5e4e11709`), `_GET_MAX_AMMO_2` (`GetMaxAmmo_2`)

---
### GetMaxAmmoInClip

`GET_MAX_AMMO_IN_CLIP` · hash `0xA38DCFFCEA8962FA` · jhash `0x6961E2A4` · **Cliente**

```lua
local retval = GetMaxAmmoInClip(ped, weaponHash, p2)
```
```c
int GET_MAX_AMMO_IN_CLIP(Ped ped, Hash weaponHash, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
p2 is mostly 1 in the scripts.  
```

---
### GetMaxRangeOfCurrentPedWeapon

`GET_MAX_RANGE_OF_CURRENT_PED_WEAPON` · hash `0x814C9D19DFD69679` · jhash `0xB2B2BBAA` · **Cliente**

```lua
local retval = GetMaxRangeOfCurrentPedWeapon(ped)
```
```c
float GET_MAX_RANGE_OF_CURRENT_PED_WEAPON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `float`

---
### GetPedAmmoByType

`GET_PED_AMMO_BY_TYPE` · hash `0x39D22031557946C1` · jhash `0x54077C4D` · **Cliente**

```lua
local retval = GetPedAmmoByType(ped, ammoType)
```
```c
int GET_PED_AMMO_BY_TYPE(Ped ped, Hash ammoType);
```

**Parámetros**

- `ped` (`Ped`)
- `ammoType` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

---
### GetPedAmmoTypeFromWeapon

`GET_PED_AMMO_TYPE_FROM_WEAPON` · hash `0x7FEAD38B326B9F74` · jhash `0x09337863` · **Cliente**

```lua
local retval = GetPedAmmoTypeFromWeapon(ped, weaponHash)
```
```c
Hash GET_PED_AMMO_TYPE_FROM_WEAPON(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

**Descripción oficial:**

```
Returns the current ammo type of the specified ped's specified weapon.

MkII magazines will change the return value, like Pistol MkII returning AMMO_PISTOL without any components and returning AMMO_PISTOL_TRACER after Tracer Rounds component is attached.

Use 0xF489B44DD5AF4BD9 if you always want AMMO_PISTOL.
```

**Nombres antiguos (alias):** `_GET_PED_AMMO_TYPE` (`GetPedAmmoType`)

---
### GetPedAmmoTypeFromWeapon_2

`_GET_PED_AMMO_TYPE_FROM_WEAPON_2` · hash `0xF489B44DD5AF4BD9` · **Cliente**

```lua
local retval = GetPedAmmoTypeFromWeapon_2(ped, weaponHash)
```
```c
Hash _GET_PED_AMMO_TYPE_FROM_WEAPON_2(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

**Descripción oficial:**

```
Returns the base/default ammo type of the specified ped's specified weapon.

Use GET_PED_AMMO_TYPE_FROM_WEAPON if you want current ammo type (like AMMO_MG_INCENDIARY/AMMO_MG_TRACER while using MkII magazines) and use this if you want base ammo type. (AMMO_MG)
```

---
### GetPedLastWeaponImpactCoord

`GET_PED_LAST_WEAPON_IMPACT_COORD` · hash `0x6C4D0409BA1A2BC2` · jhash `0x9B266079` · **Cliente**

```lua
local retval, coords = GetPedLastWeaponImpactCoord(ped, coords)
```
```c
BOOL GET_PED_LAST_WEAPON_IMPACT_COORD(Ped ped, Vector3* coords);
```

**Parámetros**

- `ped` (`Ped`)
- `coords` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Pass ped. Pass address of Vector3.  
The coord will be put into the Vector3.  
The return will determine whether there was a coord found or not.  
```

---
### GetPedWeaponLiveryColor

`_GET_PED_WEAPON_LIVERY_COLOR` · hash `0xF0A60040BE558F2D` · **Cliente**

```lua
local retval = GetPedWeaponLiveryColor(ped, weaponHash, camoComponentHash)
```
```c
int _GET_PED_WEAPON_LIVERY_COLOR(Ped ped, Hash weaponHash, Hash camoComponentHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `camoComponentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xF0A60040BE558F2D` (`N_0xf0a60040be558f2d`)

---
### GetPedWeaponTintIndex

`GET_PED_WEAPON_TINT_INDEX` · hash `0x2B9EEDC07BD06B9F` · jhash `0x3F9C90A7` · **Cliente**

```lua
local retval = GetPedWeaponTintIndex(ped, weaponHash)
```
```c
int GET_PED_WEAPON_TINT_INDEX(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

---
### GetPedWeapontypeInSlot

`GET_PED_WEAPONTYPE_IN_SLOT` · hash `0xEFFED78E9011134D` · jhash `0x9BC64E16` · **Cliente**

```lua
local retval = GetPedWeapontypeInSlot(ped, weaponSlot)
```
```c
Hash GET_PED_WEAPONTYPE_IN_SLOT(Ped ped, Hash weaponSlot);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponSlot` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

---
### GetSelectedPedWeapon

`GET_SELECTED_PED_WEAPON` · hash `0x0A6DB4965674D243` · jhash `0xD240123E` · **Cliente**

```lua
local retval = GetSelectedPedWeapon(ped)
```
```c
Hash GET_SELECTED_PED_WEAPON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Hash` — Hash: The weapon hash of the currently selected weapon.

---
### GetTimeBeforeVehicleWeaponReloadFinishes

`_GET_TIME_BEFORE_VEHICLE_WEAPON_RELOAD_FINISHES` · hash `0xC8C6F4B1CDEB40EF` · **Cliente**

```lua
local retval = GetTimeBeforeVehicleWeaponReloadFinishes(vehicle, seat)
```
```c
int _GET_TIME_BEFORE_VEHICLE_WEAPON_RELOAD_FINISHES(Vehicle vehicle, int seat);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `seat` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### GetVehicleWeaponReloadTime

`_GET_VEHICLE_WEAPON_RELOAD_TIME` · hash `0xD0AD348FFD7A6868` · **Cliente**

```lua
local retval = GetVehicleWeaponReloadTime(vehicle, seat)
```
```c
float _GET_VEHICLE_WEAPON_RELOAD_TIME(Vehicle vehicle, int seat);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `seat` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### GetWeaponClipSize

`GET_WEAPON_CLIP_SIZE` · hash `0x583BE370B1EC6EB4` · jhash `0x8D515E66` · **Cliente**

```lua
local retval = GetWeaponClipSize(weaponHash)
```
```c
int GET_WEAPON_CLIP_SIZE(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
// Returns the size of the default weapon component clip.  
Use it like this:  
char cClipSize[32];  
Hash cur;  
if (WEAPON::GET_CURRENT_PED_WEAPON(playerPed, &cur, 1))  
{  
    if (WEAPON::IS_WEAPON_VALID(cur))  
    {  
        int iClipSize = WEAPON::GET_WEAPON_CLIP_SIZE(cur);  
        sprintf_s(cClipSize, "ClipSize: %.d", iClipSize);  
        vDrawString(cClipSize, 0.5f, 0.5f);  
    }  
}  
```

---
### GetWeaponComponentHudStats

`GET_WEAPON_COMPONENT_HUD_STATS` · hash `0xB3CAF387AE12E9F8` · jhash `0xBB5498F4` · **Cliente**

```lua
local retval, outData = GetWeaponComponentHudStats(componentHash, outData)
```
```c
BOOL GET_WEAPON_COMPONENT_HUD_STATS(Hash componentHash, int* outData);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outData` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### GetWeaponComponentTypeModel

`GET_WEAPON_COMPONENT_TYPE_MODEL` · hash `0x0DB57B41EC1DB083` · jhash `0x324FA47A` · **Cliente**

```lua
local retval = GetWeaponComponentTypeModel(componentHash)
```
```c
Hash GET_WEAPON_COMPONENT_TYPE_MODEL(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

---
### GetWeaponComponentVariantExtraComponentCount

`_GET_WEAPON_COMPONENT_VARIANT_EXTRA_COMPONENT_COUNT` · hash `0x6558AC7C17BFEF58` · **Cliente**

```lua
local retval = GetWeaponComponentVariantExtraComponentCount(componentHash)
```
```c
int _GET_WEAPON_COMPONENT_VARIANT_EXTRA_COMPONENT_COUNT(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x6558AC7C17BFEF58` (`N_0x6558ac7c17bfef58`)

---
### GetWeaponComponentVariantExtraComponentModel

`_GET_WEAPON_COMPONENT_VARIANT_EXTRA_COMPONENT_MODEL` · hash `0x4D1CB8DC40208A17` · **Cliente**

```lua
local retval = GetWeaponComponentVariantExtraComponentModel(componentHash, extraComponentIndex)
```
```c
Hash _GET_WEAPON_COMPONENT_VARIANT_EXTRA_COMPONENT_MODEL(Hash componentHash, int extraComponentIndex);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `extraComponentIndex` (`int`)

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0x4D1CB8DC40208A17` (`N_0x4d1cb8dc40208a17`)

---
### GetWeaponDamage

`GET_WEAPON_DAMAGE` · hash `0x3133B907D8B32053` · jhash `0xE81649C0` · **Cliente**

```lua
local retval = GetWeaponDamage(weaponHash, componentHash)
```
```c
float GET_WEAPON_DAMAGE(Hash weaponHash, Hash componentHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: 0 in the decompiled scripts.

**Devuelve:** `float` — Damages of the weapon.

**Descripción oficial:**

This native does not return damages of weapons from the melee and explosive group.

**Nombres antiguos (alias):** `0x3133B907D8B32053` (`N_0x3133b907d8b32053`), `_GET_WEAPON_DAMAGE` (`GetWeaponDamage`)

---
### GetWeaponDamageType

`GET_WEAPON_DAMAGE_TYPE` · hash `0x3BE0BB12D25FB305` · jhash `0x013AFC13` · **Cliente**

```lua
local retval = GetWeaponDamageType(weaponHash)
```
```c
int GET_WEAPON_DAMAGE_TYPE(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
0=unknown (or incorrect weaponHash)  
1= no damage (flare,snowball, petrolcan)  
2=melee  
3=bullet  
4=force ragdoll fall  
5=explosive (RPG, Railgun, grenade)  
6=fire(molotov)  
8=fall(WEAPON_HELI_CRASH)  
10=electric  
11=barbed wire  
12=extinguisher  
13=gas  
14=water cannon(WEAPON_HIT_BY_WATER_CANNON)  
```

---
### GetWeaponHudStats

`GET_WEAPON_HUD_STATS` · hash `0xD92C739EE34C9EBA` · jhash `0xA9AD3D98` · **Cliente**

```lua
local retval, outData = GetWeaponHudStats(weaponHash, outData)
```
```c
BOOL GET_WEAPON_HUD_STATS(Hash weaponHash, Any* outData);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outData` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
// members should be aligned to 8 bytes by default but it's best to use alignas here, just to be sure  
struct WeaponHudStatsData  
{  
	alignas(8) uint8_t hudDamage; // 0x0000  
	alignas(8) uint8_t hudSpeed; // 0x0008  
	alignas(8) uint8_t hudCapacity; // 0x0010  
	alignas(8) uint8_t hudAccuracy; // 0x0018  
	alignas(8) uint8_t hudRange; // 0x0020  
};  
Usage:  
WeaponHudStatsData data;  
if (GET_WEAPON_HUD_STATS(weaponHash, (Any*)&data))  
{  
    // uint8_t damagePercentage = data.hudDamage etc...  
}  
```

---
### GetWeaponObjectFromPed

`GET_WEAPON_OBJECT_FROM_PED` · hash `0xCAE1DC9A0E22A16D` · jhash `0xDF939A38` · **Cliente**

```lua
local retval = GetWeaponObjectFromPed(ped, p1)
```
```c
Object GET_WEAPON_OBJECT_FROM_PED(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `Object`

**Descripción oficial:**

```
Drops the current weapon and returns the object  
Unknown behavior when unarmed.  
```

---
### GetWeaponObjectLiveryColor

`_GET_WEAPON_OBJECT_LIVERY_COLOR` · hash `0xB3EA4FEABF41464B` · **Cliente**

```lua
local retval = GetWeaponObjectLiveryColor(weaponObject, camoComponentHash)
```
```c
int _GET_WEAPON_OBJECT_LIVERY_COLOR(Object weaponObject, Hash camoComponentHash);
```

**Parámetros**

- `weaponObject` (`Object`)
- `camoComponentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xB3EA4FEABF41464B` (`N_0xb3ea4feabf41464b`)

---
### GetWeaponObjectTintIndex

`GET_WEAPON_OBJECT_TINT_INDEX` · hash `0xCD183314F7CD2E57` · jhash `0xD91D9576` · **Cliente**

```lua
local retval = GetWeaponObjectTintIndex(weapon)
```
```c
int GET_WEAPON_OBJECT_TINT_INDEX(Object weapon);
```

**Parámetros**

- `weapon` (`Object`)

**Devuelve:** `int`

---
### GetWeaponTimeBetweenShots

`_GET_WEAPON_TIME_BETWEEN_SHOTS` · hash `0x065D2AACAD8CF7A4` · **Cliente**

```lua
local retval = GetWeaponTimeBetweenShots(weaponHash)
```
```c
float _GET_WEAPON_TIME_BETWEEN_SHOTS(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x065D2AACAD8CF7A4` (`N_0x065d2aacad8cf7a4`)

---
### GetWeaponTintCount

`GET_WEAPON_TINT_COUNT` · hash `0x5DCF6C5CAB2E9BF7` · jhash `0x99E4EAAB` · **Cliente**

```lua
local retval = GetWeaponTintCount(weaponHash)
```
```c
int GET_WEAPON_TINT_COUNT(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

---
### GetWeapontypeGroup

`GET_WEAPONTYPE_GROUP` · hash `0xC3287EE3050FB74C` · jhash `0x5F2DE833` · **Cliente**

```lua
local retval = GetWeapontypeGroup(weaponHash)
```
```c
Hash GET_WEAPONTYPE_GROUP(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of the weapon.

**Devuelve:** `Hash` — Returns the hash of the group of the weapon. Hashes:| Group                  | Unsigned   | Signed      | Example                 | |:----------------------:|:----------:|:-----------:|:-----------------------:| | GROUP_DIGISCANNER      | 3539449195 | -755518101  | WEAPON_DIGISCANNER      | | GROUP_FIREEXTINGUISHER | 4257178988 | -37788308   | WEAPON_FIREEXTINGUISHER | | GROUP_HACKINGDEVICE    | 1175761940 | 1175761940  | WEAPON_HACKINGDEVICE    | | GROUP_HEAVY            | 2725924767 | -1569042529 | WEAPON_RPG              | | GROUP_MELEE            | 3566412244 | -728555052  | WEAPON_BAT              | | GROUP_METALDETECTOR    | 3759491383 | -535475913  | WEAPON_METALDETECTOR    | | GROUP_MG               | 1159398588 | 1159398588  | WEAPON_COMBATMG         | | GROUP_NIGHTVISION      | 3493187224 | -801780072  | GADGET_NIGHTVISION      | | GROUP_PARACHUTE        | 431593103  | 431593103   | GADGET_PARACHUTE        | | GROUP_PETROLCAN        | 1595662460 | 1595662460  | WEAPON_PETROLCAN        | | GROUP_PISTOL           | 416676503  | 416676503   | WEAPON_PISTOL           | | GROUP_RIFLE            | 970310034  | 970310034   | WEAPON_ASSAULTRIFLE     | | GROUP_SHOTGUN          | 860033945  | 860033945   | WEAPON_PUMPSHOTGUN      | | GROUP_SMG              | 3337201093 | -957766203  | WEAPON_MICROSMG         | | GROUP_SNIPER           | 3082541095 | -1212426201 | WEAPON_SNIPERRIFLE      | | GROUP_STUNGUN          | 690389602  | 690389602   | WEAPON_STUNGUN          | | GROUP_THROWN           | 1548507267 | 1548507267  | WEAPON_SNOWBALL         | | GROUP_TRANQILIZER      | 75159441   | 75159441    | WEAPON_TRANQUILIZER     | | GROUP_UNARMED          | 2685387236 | -1609580060 | WEAPON_UNARMED          |

**Descripción oficial:**

Gets and returns the hash of the group of the specified weapon (group names can be found/changed under "Group" in the weapons' meta file).
Note that the group is **not** the same as the location on the weapon wheel.

**Ejemplo (lua):**

```lua
print(GetWeapontypeGroup(`WEAPON_PISTOL`)) -- Outputs the hash of GROUP_PISTOL
print(GetWeapontypeGroup(`WEAPON_RPG`)) -- Outputs the hash of GROUP_HEAVY
print(GetWeapontypeGroup(`WEAPON_SNOWBALL`)) -- Outputs the hash of GROUP_THROWN
print(GetWeapontypeGroup(`WEAPON_MUSKET`)) -- Outputs the hash of GROUP_SNIPER
print(GetWeapontypeGroup(GetSelectedPedWeapon(PlayerPedId()))) -- Outputs the hash of the currently selected weapon
```

**Ejemplo (js):**

```js
console.log(GetWeapontypeGroup(`WEAPON_PISTOL`)); // Outputs the hash of GROUP_PISTOL
console.log(GetWeapontypeGroup(`WEAPON_RPG`)); // Outputs the hash of GROUP_HEAVY
console.log(GetWeapontypeGroup(`WEAPON_SNOWBALL`)); // Outputs the hash of GROUP_THROWN
console.log(GetWeapontypeGroup(`WEAPON_MUSKET`)); // Outputs the hash of GROUP_SNIPER
console.log(GetWeapontypeGroup(GetSelectedPedWeapon(PlayerPedId()))); // Outputs the hash of the currently selected weapon
```

---
### GetWeapontypeModel

`GET_WEAPONTYPE_MODEL` · hash `0xF46CDC33180FDA94` · jhash `0x44E1C269` · **Cliente**

```lua
local retval = GetWeapontypeModel(weaponHash)
```
```c
Hash GET_WEAPONTYPE_MODEL(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

**Descripción oficial:**

```
Returns the model of any weapon.  
Can also take an ammo hash?  
sub_6663a(&l_115B, WEAPON::GET_WEAPONTYPE_MODEL(${ammo_rpg}));  
```

---
### GetWeapontypeSlot

`GET_WEAPONTYPE_SLOT` · hash `0x4215460B9B8B7FA0` · jhash `0x2E3759AF` · **Cliente**

```lua
local retval = GetWeapontypeSlot(weaponHash)
```
```c
Hash GET_WEAPONTYPE_SLOT(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

---
### GiveDelayedWeaponToPed

`GIVE_DELAYED_WEAPON_TO_PED` · hash `0xB282DC6EBD803C75` · jhash `0x5868D20D` · **Cliente**

```lua
GiveDelayedWeaponToPed(ped, weaponHash, ammoCount, bForceInHand)
```
```c
void GIVE_DELAYED_WEAPON_TO_PED(Ped ped, Hash weaponHash, int ammoCount, BOOL bForceInHand);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammoCount` (`int`)
- `bForceInHand` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Gives a weapon to PED with a delay, example:
WEAPON::GIVE_DELAYED_WEAPON_TO_PED(PED::PLAYER_PED_ID(), MISC::GET_HASH_KEY("WEAPON_PISTOL"), 1000, false)
```

---
### GiveLoadoutToPed

`_GIVE_LOADOUT_TO_PED` · hash `0x68F8BE6AF5CDF8A6` · **Cliente**

```lua
GiveLoadoutToPed(ped, loadoutHash)
```
```c
void _GIVE_LOADOUT_TO_PED(Ped ped, Hash loadoutHash);
```

**Parámetros**

- `ped` (`Ped`): The ped handle to apply this to.
- `loadoutHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The loadout to use (needs to be a hash).

**Devuelve:** `void`

**Descripción oficial:**

List of all available loadouts:

```
LOADOUT_DEFAULT
LOADOUT_ANIMAL
LOADOUT_COUGAR
LOADOUT_HILLBILLY
LOADOUT_CULT
LOADOUT_CHEAT_0
LOADOUT_CHEAT_1
LOADOUT_GUARD
LOADOUT_NETWORK_BOT
LOADOUT_LOST
LOADOUT_LOST_L1
LOADOUT_LOST_L2
LOADOUT_LOST_L3
LOADOUT_MEXICAN
LOADOUT_MEXICAN_L1
LOADOUT_MEXICAN_L2
LOADOUT_MEXICAN_L3
LOADOUT_FAMILY
LOADOUT_ASIAN
LOADOUT_SECUR
LOADOUT_POLICE_GUARD
LOADOUT_COP
LOADOUT_COP_L1
LOADOUT_COP_L2
LOADOUT_COP_L3
LOADOUT_SWAT
LOADOUT_SWAT_NO_LASER
LOADOUT_COP_SHOTGUN
LOADOUT_FIREMAN
LOADOUT_COP_HELI
LOADOUT_COP_BOAT
LOADOUT_ARMY
LOADOUT_ANIMAL_RETRIEVER
LOADOUT_SMALL_DOG
LOADOUT_TIGER_SHARK
LOADOUT_HAMMERHEAD_SHARK
LOADOUT_KILLER_WHALE
LOADOUT_BOAR
LOADOUT_PIG
LOADOUT_COYOTE
LOADOUT_DEER
LOADOUT_HEN
LOADOUT_RABBIT
LOADOUT_CAT
LOADOUT_COW
```

**Nombres antiguos (alias):** `0x68F8BE6AF5CDF8A6` (`N_0x68f8be6af5cdf8a6`)

**Ejemplo (lua):**

```lua
GiveLoadoutToPed(PlayerPedId(), `LOADOUT_FIREMAN`)
```

---
### GiveWeaponComponentToPed

`GIVE_WEAPON_COMPONENT_TO_PED` · hash `0xD966D51AA5B28BB9` · jhash `0x3E1E286D` · **Cliente · también en el servidor (RPC)**

```lua
GiveWeaponComponentToPed(ped, weaponHash, componentHash)
```
```c
void GIVE_WEAPON_COMPONENT_TO_PED(Ped ped, Hash weaponHash, Hash componentHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### GiveWeaponComponentToWeaponObject

`GIVE_WEAPON_COMPONENT_TO_WEAPON_OBJECT` · hash `0x33E179436C0B31DB` · jhash `0xF7612A37` · **Cliente**

```lua
GiveWeaponComponentToWeaponObject(weaponObject, addonHash)
```
```c
void GIVE_WEAPON_COMPONENT_TO_WEAPON_OBJECT(Object weaponObject, Hash addonHash);
```

**Parámetros**

- `weaponObject` (`Object`)
- `addonHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
addonHash:
(use WEAPON::GET_WEAPON_COMPONENT_TYPE_MODEL() to get hash value)
${component_at_ar_flsh}, ${component_at_ar_supp}, ${component_at_pi_flsh}, ${component_at_scope_large}, ${component_at_ar_supp_02}
```

---
### GiveWeaponObjectToPed

`GIVE_WEAPON_OBJECT_TO_PED` · hash `0xB1FA61371AF7C4B7` · jhash `0x639AF3EF` · **Cliente**

```lua
GiveWeaponObjectToPed(weaponObject, ped)
```
```c
void GIVE_WEAPON_OBJECT_TO_PED(Object weaponObject, Ped ped);
```

**Parámetros**

- `weaponObject` (`Object`)
- `ped` (`Ped`)

**Devuelve:** `void`

---
### GiveWeaponToPed

`GIVE_WEAPON_TO_PED` · hash `0xBF0FD6E56C964FCB` · jhash `0xC4D88A85` · **Cliente · también en el servidor (RPC)**

```lua
GiveWeaponToPed(ped, weaponHash, ammoCount, isHidden, bForceInHand)
```
```c
void GIVE_WEAPON_TO_PED(Ped ped, Hash weaponHash, int ammoCount, BOOL isHidden, BOOL bForceInHand);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammoCount` (`int`)
- `isHidden` (`BOOL`)
- `bForceInHand` (`BOOL`)

**Devuelve:** `void`

---
### HasEntityBeenDamagedByWeapon

`HAS_ENTITY_BEEN_DAMAGED_BY_WEAPON` · hash `0x131D401334815E94` · jhash `0x6DAABB39` · **Cliente**

```lua
local retval = HasEntityBeenDamagedByWeapon(entity, weaponHash, weaponType)
```
```c
BOOL HAS_ENTITY_BEEN_DAMAGED_BY_WEAPON(Entity entity, Hash weaponHash, int weaponType);
```

**Parámetros**

- `entity` (`Entity`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `weaponType` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
It determines what weapons caused damage:
If you want to define only a specific weapon, second parameter=weapon hash code, third parameter=0
If you want to define any melee weapon, second parameter=0, third parameter=1.
If you want to identify any weapon (firearms, melee, rockets, etc.), second parameter=0, third parameter=2.
```

---
### HasPedBeenDamagedByWeapon

`HAS_PED_BEEN_DAMAGED_BY_WEAPON` · hash `0x2D343D2219CD027A` · jhash `0xCDFBBCC6` · **Cliente**

```lua
local retval = HasPedBeenDamagedByWeapon(ped, weaponHash, weaponType)
```
```c
BOOL HAS_PED_BEEN_DAMAGED_BY_WEAPON(Ped ped, Hash weaponHash, int weaponType);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `weaponType` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
It determines what weapons caused damage:  
If you want to define only a specific weapon, second parameter=weapon hash code, third parameter=0  
If you want to define any melee weapon, second parameter=0, third parameter=1.  
If you want to identify any weapon (firearms, melee, rockets, etc.), second parameter=0, third parameter=2.  
```

---
### HasPedGotWeapon

`HAS_PED_GOT_WEAPON` · hash `0x8DECB02F88F428BC` · jhash `0x43D2FA82` · **Cliente**

```lua
local retval = HasPedGotWeapon(ped, weaponHash, p2)
```
```c
BOOL HAS_PED_GOT_WEAPON(Ped ped, Hash weaponHash, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p2 should be FALSE, otherwise it seems to always return FALSE  
Bool does not check if the weapon is current equipped, unfortunately.  
```

---
### HasPedGotWeaponComponent

`HAS_PED_GOT_WEAPON_COMPONENT` · hash `0xC593212475FAE340` · jhash `0xDC0FC145` · **Cliente**

```lua
local retval = HasPedGotWeaponComponent(ped, weaponHash, componentHash)
```
```c
BOOL HAS_PED_GOT_WEAPON_COMPONENT(Ped ped, Hash weaponHash, Hash componentHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### HasVehicleGotProjectileAttached

`HAS_VEHICLE_GOT_PROJECTILE_ATTACHED` · hash `0x717C8481234E3B88` · jhash `0xA57E2E80` · **Cliente**

```lua
local retval = HasVehicleGotProjectileAttached(driver, vehicle, weaponHash, p3)
```
```c
BOOL HAS_VEHICLE_GOT_PROJECTILE_ATTACHED(Ped driver, Vehicle vehicle, Hash weaponHash, Any p3);
```

**Parámetros**

- `driver` (`Ped`)
- `vehicle` (`Vehicle`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p3` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Third Parameter = unsure, but pretty sure it is weapon hash  
--> get_hash_key("weapon_stickybomb")  
Fourth Parameter = unsure, almost always -1  
```

---
### HasWeaponAssetLoaded

`HAS_WEAPON_ASSET_LOADED` · hash `0x36E353271F0E90EE` · jhash `0x1891D5BB` · **Cliente**

```lua
local retval = HasWeaponAssetLoaded(weaponHash)
```
```c
BOOL HAS_WEAPON_ASSET_LOADED(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### HasWeaponGotWeaponComponent

`HAS_WEAPON_GOT_WEAPON_COMPONENT` · hash `0x76A18844E743BF91` · jhash `0x1D368510` · **Cliente**

```lua
local retval = HasWeaponGotWeaponComponent(weapon, addonHash)
```
```c
BOOL HAS_WEAPON_GOT_WEAPON_COMPONENT(Object weapon, Hash addonHash);
```

**Parámetros**

- `weapon` (`Object`)
- `addonHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### HasWeaponReloadingInVehicle

`_HAS_WEAPON_RELOADING_IN_VEHICLE` · hash `0x8062F07153F4446F` · **Cliente**

```lua
local retval = HasWeaponReloadingInVehicle(vehicle, seat)
```
```c
BOOL _HAS_WEAPON_RELOADING_IN_VEHICLE(Vehicle vehicle, int seat);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `seat` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### HidePedWeaponForScriptedCutscene

`HIDE_PED_WEAPON_FOR_SCRIPTED_CUTSCENE` · hash `0x6F6981D2253C208F` · jhash `0x00CFD6E9` · **Cliente**

```lua
HidePedWeaponForScriptedCutscene(ped, toggle)
```
```c
void HIDE_PED_WEAPON_FOR_SCRIPTED_CUTSCENE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Hides the players weapon during a cutscene.  
```

---
### IsAnyAirDefenseZoneInsideSphere

`_IS_ANY_AIR_DEFENSE_ZONE_INSIDE_SPHERE` · hash `0xDAB963831DBFD3F4` · **Cliente**

```lua
local retval, SphereIndex = IsAnyAirDefenseZoneInsideSphere(x, y, z, radius, SphereIndex)
```
```c
BOOL _IS_ANY_AIR_DEFENSE_ZONE_INSIDE_SPHERE(float x, float y, float z, float radius, int* SphereIndex);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `SphereIndex` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xDAB963831DBFD3F4` (`N_0xdab963831dbfd3f4`), `_IS_AIR_DEFENSE_ZONE_INSIDE_SPHERE` (`IsAirDefenseZoneInsideSphere`)

---
### IsFlashLightOn

`IS_FLASH_LIGHT_ON` · hash `0x4B7620C47217126C` · jhash `0x76876154` · **Cliente**

```lua
local retval = IsFlashLightOn(ped)
```
```c
BOOL IS_FLASH_LIGHT_ON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `SET_WEAPON_SMOKEGRENADE_ASSIGNED` (`SetWeaponSmokegrenadeAssigned`)

---
### IsPedArmed

`IS_PED_ARMED` · hash `0x475768A975D5AD17` · jhash `0x0BFC892C` · **Cliente**

```lua
local retval = IsPedArmed(ped, typeFlags)
```
```c
BOOL IS_PED_ARMED(Ped ped, int typeFlags);
```

**Parámetros**

- `ped` (`Ped`): The ped to check armed state on.
- `typeFlags` (`int`): Type flags to check.

**Devuelve:** `BOOL` — Whether or not the ped is currently equipped with any weapon matching typeFlags.

**Descripción oficial:**

Checks if the ped is currently equipped with a weapon matching a bit specified using a bitwise-or in typeFlags.

| Bit value | Effect            |
|-----------|-------------------|
| 1         | Melee weapons     |
| 2         | Explosive weapons |
| 4         | Any other weapons |

Not specifying any bit will lead to the native *always* returning 'false', and for example specifying '4 | 2' will check for any weapon except fists and melee weapons.

---
### IsPedCurrentWeaponSilenced

`IS_PED_CURRENT_WEAPON_SILENCED` · hash `0x65F0C5AE05943EC7` · jhash `0xBAF7BFBE` · **Cliente**

```lua
local retval = IsPedCurrentWeaponSilenced(ped)
```
```c
BOOL IS_PED_CURRENT_WEAPON_SILENCED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This native returns a true or false value.  
Ped ped = The ped whose weapon you want to check.  
```

---
### IsPedWeaponComponentActive

`IS_PED_WEAPON_COMPONENT_ACTIVE` · hash `0x0D78DE0572D3969E` · jhash `0x7565FB19` · **Cliente**

```lua
local retval = IsPedWeaponComponentActive(ped, weaponHash, componentHash)
```
```c
BOOL IS_PED_WEAPON_COMPONENT_ACTIVE(Ped ped, Hash weaponHash, Hash componentHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsPedWeaponReadyToShoot

`IS_PED_WEAPON_READY_TO_SHOOT` · hash `0xB80CA294F2F26749` · jhash `0x02A32CB0` · **Cliente**

```lua
local retval = IsPedWeaponReadyToShoot(ped)
```
```c
BOOL IS_PED_WEAPON_READY_TO_SHOOT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsWeaponValid

`IS_WEAPON_VALID` · hash `0x937C71165CF334B3` · jhash `0x38CA2954` · **Cliente**

```lua
local retval = IsWeaponValid(weaponHash)
```
```c
BOOL IS_WEAPON_VALID(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### MakePedReload

`MAKE_PED_RELOAD` · hash `0x20AE33F3AC9C0033` · jhash `0x515292C2` · **Cliente**

```lua
local retval = MakePedReload(ped)
```
```c
BOOL MAKE_PED_RELOAD(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Forces a ped to reload only if they are able to; if they have a full magazine, they will not reload.

---
### N_0x24c024ba8379a70a

`0x24C024BA8379A70A` · hash `0x24C024BA8379A70A` · **Cliente**

```lua
N_0x24c024ba8379a70a(p0, p1)
```
```c
void 0x24C024BA8379A70A(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x977ca98939e82e4b

`0x977CA98939E82E4B` · hash `0x977CA98939E82E4B` · **Cliente**

```lua
N_0x977ca98939e82e4b(weaponObject, p1)
```
```c
void 0x977CA98939E82E4B(Object weaponObject, int p1);
```

**Parámetros**

- `weaponObject` (`Object`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_WEAPON_OBJECT_*
```

---
### N_0xa2c9ac24b4061285

`0xA2C9AC24B4061285` · hash `0xA2C9AC24B4061285` · **Cliente**

```lua
local retval = N_0xa2c9ac24b4061285(ped, weaponHash)
```
```c
int 0xA2C9AC24B4061285(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

---
### N_0xe4dcec7fd5b739a5

`0xE4DCEC7FD5B739A5` · hash `0xE4DCEC7FD5B739A5` · jhash `0x64646F1D` · **Cliente**

```lua
N_0xe4dcec7fd5b739a5(ped)
```
```c
void 0xE4DCEC7FD5B739A5(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### N_0xe6d2cedd370ff98e

`0xE6D2CEDD370FF98E` · hash `0xE6D2CEDD370FF98E` · **Cliente**

```lua
N_0xe6d2cedd370ff98e(p0, p1)
```
```c
void 0xE6D2CEDD370FF98E(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### RefillAmmoInstantly

`REFILL_AMMO_INSTANTLY` · hash `0x8C0D57EA686FAD87` · jhash `0x82EEAF0F` · **Cliente**

```lua
local retval = RefillAmmoInstantly(ped)
```
```c
BOOL REFILL_AMMO_INSTANTLY(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_PED_SKIP_NEXT_RELOADING` (`PedSkipNextReloading`)

---
### RemoveAirDefenseZone

`_REMOVE_AIR_DEFENSE_ZONE` · hash `0x0ABF535877897560` · **Cliente**

```lua
local retval = RemoveAirDefenseZone(zoneId)
```
```c
BOOL _REMOVE_AIR_DEFENSE_ZONE(int zoneId);
```

**Parámetros**

- `zoneId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0ABF535877897560` (`N_0x0abf535877897560`)

---
### RemoveAllAirDefenseZones

`_REMOVE_ALL_AIR_DEFENSE_ZONES` · hash `0x1E45B34ADEBEE48E` · **Cliente**

```lua
RemoveAllAirDefenseZones()
```
```c
void _REMOVE_ALL_AIR_DEFENSE_ZONES();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1E45B34ADEBEE48E` (`N_0x1e45b34adebee48e`)

---
### RemoveAllPedWeapons

`REMOVE_ALL_PED_WEAPONS` · hash `0xF25DF915FA38C5F3` · jhash `0xA44CE817` · **Cliente · también en el servidor (RPC)**

```lua
RemoveAllPedWeapons(ped, p1)
```
```c
void REMOVE_ALL_PED_WEAPONS(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`): The ped entity
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Parameter `p1` does not seem to be used or referenced in game binaries.\
**Note:** When called for networked entities, a `CRemoveAllWeaponsEvent` will be created per request.

---
### RemoveAllProjectilesOfType

`REMOVE_ALL_PROJECTILES_OF_TYPE` · hash `0xFC52E0F37E446528` · jhash `0xA5F89919` · **Cliente**

```lua
RemoveAllProjectilesOfType(weaponHash, explode)
```
```c
void REMOVE_ALL_PROJECTILES_OF_TYPE(Hash weaponHash, BOOL explode);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `explode` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

If `explode` true, then removal is done through exploding the projectile. Basically the same as EXPLODE_PROJECTILES but without defining the owner ped.

---
### RemoveWeaponAsset

`REMOVE_WEAPON_ASSET` · hash `0xAA08EF13F341C8FC` · jhash `0x2C0DFE3C` · **Cliente**

```lua
RemoveWeaponAsset(weaponHash)
```
```c
void REMOVE_WEAPON_ASSET(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### RemoveWeaponComponentFromPed

`REMOVE_WEAPON_COMPONENT_FROM_PED` · hash `0x1E8BE90C74FB4C09` · jhash `0x412AA00D` · **Cliente · también en el servidor (RPC)**

```lua
RemoveWeaponComponentFromPed(ped, weaponHash, componentHash)
```
```c
void REMOVE_WEAPON_COMPONENT_FROM_PED(Ped ped, Hash weaponHash, Hash componentHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### RemoveWeaponComponentFromWeaponObject

`REMOVE_WEAPON_COMPONENT_FROM_WEAPON_OBJECT` · hash `0xF7D82B0D66777611` · jhash `0xA6E7ED3C` · **Cliente**

```lua
RemoveWeaponComponentFromWeaponObject(weaponObject, addonHash)
```
```c
void REMOVE_WEAPON_COMPONENT_FROM_WEAPON_OBJECT(Object weaponObject, Hash addonHash);
```

**Parámetros**

- `weaponObject` (`Object`)
- `addonHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### RemoveWeaponFromPed

`REMOVE_WEAPON_FROM_PED` · hash `0x4899CB088EDF59B8` · jhash `0x9C37F220` · **Cliente · también en el servidor (RPC)**

```lua
RemoveWeaponFromPed(ped, weaponHash)
```
```c
void REMOVE_WEAPON_FROM_PED(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
This native removes a specified weapon from your selected ped.  
Weapon Hashes: pastebin.com/0wwDZgkF  
Example:  
C#:  
Function.Call(Hash.REMOVE_WEAPON_FROM_PED, Game.Player.Character, 0x99B507EA);  
C++:  
WEAPON::REMOVE_WEAPON_FROM_PED(PLAYER::PLAYER_PED_ID(), 0x99B507EA);  
The code above removes the knife from the player.  
```

---
### RequestWeaponAsset

`REQUEST_WEAPON_ASSET` · hash `0x5443438F033E29C3` · jhash `0x65D139A5` · **Cliente**

```lua
RequestWeaponAsset(weaponHash, p1, p2)
```
```c
void REQUEST_WEAPON_ASSET(Hash weaponHash, int p1, int p2);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)
- `p2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Nearly every instance of p1 I found was 31. Nearly every instance of p2 I found was 0.  
REQUEST_WEAPON_ASSET(iLocal_1888, 31, 26);  
```

---
### RequestWeaponHighDetailModel

`REQUEST_WEAPON_HIGH_DETAIL_MODEL` · hash `0x48164DBB970AC3F0` · jhash `0xE3BD00F9` · **Cliente**

```lua
RequestWeaponHighDetailModel(weaponObject)
```
```c
void REQUEST_WEAPON_HIGH_DETAIL_MODEL(Entity weaponObject);
```

**Parámetros**

- `weaponObject` (`Entity`)

**Devuelve:** `void`

---
### SetAmmoInClip

`SET_AMMO_IN_CLIP` · hash `0xDCD2A934D65CB497` · jhash `0xA54B0B10` · **Cliente**

```lua
local retval = SetAmmoInClip(ped, weaponHash, ammo)
```
```c
BOOL SET_AMMO_IN_CLIP(Ped ped, Hash weaponHash, int ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int`)

**Devuelve:** `BOOL`

---
### SetAmmoInVehicleWeaponClip

`_SET_AMMO_IN_VEHICLE_WEAPON_CLIP` · hash `0x873906720EE842C3` · **Cliente**

```lua
local retval = SetAmmoInVehicleWeaponClip(vehicle, seat, ammo)
```
```c
BOOL _SET_AMMO_IN_VEHICLE_WEAPON_CLIP(Vehicle vehicle, int seat, int ammo);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `seat` (`int`)
- `ammo` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### SetCanPedEquipAllWeapons

`_SET_CAN_PED_EQUIP_ALL_WEAPONS` · hash `0xEFF296097FF1E509` · **Cliente**

```lua
SetCanPedEquipAllWeapons(ped, toggle)
```
```c
void _SET_CAN_PED_EQUIP_ALL_WEAPONS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Does the same as [`_SET_CAN_PED_SELECT_WEAPON`](#setcanpedequipweapon) except for all weapons.

**Nombres antiguos (alias):** `0xEFF296097FF1E509` (`N_0xeff296097ff1e509`)

---
### SetCanPedEquipWeapon

`_SET_CAN_PED_EQUIP_WEAPON` · hash `0xB4771B9AAF4E68E4` · **Cliente**

```lua
SetCanPedEquipWeapon(ped, weaponHash, toggle)
```
```c
void _SET_CAN_PED_EQUIP_WEAPON(Ped ped, Hash weaponHash, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Disables selecting the given weapon. Ped isn't forced to put the gun away. However you can't reselect the weapon if you holster then unholster. Weapon is also grayed out on the weapon wheel.

**Nombres antiguos (alias):** `0xB4771B9AAF4E68E4` (`N_0xb4771b9aaf4e68e4`), `_SET_CAN_PED_SELECT_WEAPON` (`SetCanPedSelectWeapon`)

---
### SetCurrentPedVehicleWeapon

`SET_CURRENT_PED_VEHICLE_WEAPON` · hash `0x75C55983C2C39DAA` · jhash `0x8E6F2AF1` · **Cliente**

```lua
local retval = SetCurrentPedVehicleWeapon(ped, weaponHash)
```
```c
BOOL SET_CURRENT_PED_VEHICLE_WEAPON(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### SetCurrentPedWeapon

`SET_CURRENT_PED_WEAPON` · hash `0xADF692B254977C0C` · jhash `0xB8278882` · **Cliente · también en el servidor (RPC)**

```lua
SetCurrentPedWeapon(ped, weaponHash, bForceInHand)
```
```c
void SET_CURRENT_PED_WEAPON(Ped ped, Hash weaponHash, BOOL bForceInHand);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `bForceInHand` (`BOOL`)

**Devuelve:** `void`

---
### SetFlashLightEnabled

`_SET_FLASH_LIGHT_ENABLED` · hash `0x988DB6FE9B3AC000` · **Cliente**

```lua
SetFlashLightEnabled(ped, toggle)
```
```c
void _SET_FLASH_LIGHT_ENABLED(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Enables/disables flashlight on ped's weapon.

```
NativeDB Introduced: v2060
```

---
### SetFlashLightFadeDistance

`SET_FLASH_LIGHT_FADE_DISTANCE` · hash `0xCEA66DAD478CD39B` · jhash `0xB0127EA7` · **Cliente**

```lua
local retval = SetFlashLightFadeDistance(distance)
```
```c
Any SET_FLASH_LIGHT_FADE_DISTANCE(float distance);
```

**Parámetros**

- `distance` (`float`)

**Devuelve:** `Any`

---
### SetPedAmmo

`SET_PED_AMMO` · hash `0x14E56BC5B5DB6A19` · jhash `0xBF90DF1A` · **Cliente · también en el servidor (RPC)**

```lua
SetPedAmmo(ped, weaponHash, ammo)
```
```c
void SET_PED_AMMO(Ped ped, Hash weaponHash, int ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 4: BOOL p3
```

---
### SetPedAmmoByType

`SET_PED_AMMO_BY_TYPE` · hash `0x5FD1E1F011E76D7E` · jhash `0x311C52BB` · **Cliente**

```lua
SetPedAmmoByType(ped, ammoType, ammo)
```
```c
void SET_PED_AMMO_BY_TYPE(Ped ped, Hash ammoType, int ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `ammoType` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ammo` (`int`)

**Devuelve:** `void`

---
### SetPedAmmoToDrop

`SET_PED_AMMO_TO_DROP` · hash `0xA4EFEF9440A5B0EF` · jhash `0x2386A307` · **Cliente**

```lua
SetPedAmmoToDrop(ped, ammo)
```
```c
void SET_PED_AMMO_TO_DROP(Ped ped, int ammo);
```

**Parámetros**

- `ped` (`Ped`)
- `ammo` (`int`)

**Devuelve:** `void`

---
### SetPedChanceOfFiringBlanks

`SET_PED_CHANCE_OF_FIRING_BLANKS` · hash `0x8378627201D5497D` · jhash `0xB4F44C6E` · **Cliente**

```lua
SetPedChanceOfFiringBlanks(ped, xBias, yBias)
```
```c
void SET_PED_CHANCE_OF_FIRING_BLANKS(Ped ped, float xBias, float yBias);
```

**Parámetros**

- `ped` (`Ped`)
- `xBias` (`float`)
- `yBias` (`float`)

**Devuelve:** `void`

---
### SetPedCurrentWeaponVisible

`SET_PED_CURRENT_WEAPON_VISIBLE` · hash `0x0725A4CCFDED9A70` · jhash `0x00BECD77` · **Cliente**

```lua
SetPedCurrentWeaponVisible(ped, visible, deselectWeapon, p3, p4)
```
```c
void SET_PED_CURRENT_WEAPON_VISIBLE(Ped ped, BOOL visible, BOOL deselectWeapon, BOOL p3, BOOL p4);
```

**Parámetros**

- `ped` (`Ped`)
- `visible` (`BOOL`)
- `deselectWeapon` (`BOOL`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Has 5 parameters since latest patches.  
```

---
### SetPedCycleVehicleWeaponsOnly

`SET_PED_CYCLE_VEHICLE_WEAPONS_ONLY` · hash `0x50276EF8172F5F12` · jhash `0xE3DB81AC` · **Cliente**

```lua
SetPedCycleVehicleWeaponsOnly(ped)
```
```c
void SET_PED_CYCLE_VEHICLE_WEAPONS_ONLY(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped handle

**Devuelve:** `void`

**Descripción oficial:**

Restricts weapon selection when cycling through weapons, to select only vehicle weapons.

**Nombres antiguos (alias):** `0x50276EF8172F5F12` (`N_0x50276ef8172f5f12`)

---
### SetPedDropsInventoryWeapon

`SET_PED_DROPS_INVENTORY_WEAPON` · hash `0x208A1888007FC0E6` · jhash `0x81FFB874` · **Cliente**

```lua
SetPedDropsInventoryWeapon(ped, weaponHash, xOffset, yOffset, zOffset, ammoCount)
```
```c
void SET_PED_DROPS_INVENTORY_WEAPON(Ped ped, Hash weaponHash, float xOffset, float yOffset, float zOffset, int ammoCount);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `ammoCount` (`int`)

**Devuelve:** `void`

---
### SetPedDropsWeapon

`SET_PED_DROPS_WEAPON` · hash `0x6B7513D9966FBEC0` · jhash `0x3D3329FA` · **Cliente**

```lua
SetPedDropsWeapon(ped)
```
```c
void SET_PED_DROPS_WEAPON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### SetPedDropsWeaponsWhenDead

`SET_PED_DROPS_WEAPONS_WHEN_DEAD` · hash `0x476AE72C1D19D1A8` · jhash `0x8A444056` · **Cliente**

```lua
SetPedDropsWeaponsWhenDead(ped, toggle)
```
```c
void SET_PED_DROPS_WEAPONS_WHEN_DEAD(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedGadget

`SET_PED_GADGET` · hash `0xD0D7B1E680ED4A1A` · jhash `0x8A256D0A` · **Cliente**

```lua
SetPedGadget(ped, gadgetHash, p2)
```
```c
void SET_PED_GADGET(Ped ped, Hash gadgetHash, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `gadgetHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1/gadgetHash was always 0xFBAB5776 ("GADGET_PARACHUTE").  
p2 is always true.  
```

---
### SetPedInfiniteAmmo

`SET_PED_INFINITE_AMMO` · hash `0x3EDCB0505123623B` · jhash `0x9CB8D278` · **Cliente**

```lua
SetPedInfiniteAmmo(ped, toggle, weaponHash)
```
```c
void SET_PED_INFINITE_AMMO(Ped ped, BOOL toggle, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### SetPedInfiniteAmmoClip

`SET_PED_INFINITE_AMMO_CLIP` · hash `0x183DADC6AA953186` · jhash `0x5A5E3B67` · **Cliente**

```lua
SetPedInfiniteAmmoClip(ped, toggle)
```
```c
void SET_PED_INFINITE_AMMO_CLIP(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedShootOrdnanceWeapon

`SET_PED_SHOOT_ORDNANCE_WEAPON` · hash `0xB4C8D77C80C0421E` · jhash `0xEC2E5304` · **Cliente**

```lua
local retval = SetPedShootOrdnanceWeapon(ped, p1)
```
```c
Object SET_PED_SHOOT_ORDNANCE_WEAPON(Ped ped, float p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)

**Devuelve:** `Object`

**Descripción oficial:**

```
Returns handle of the projectile.
```

**Nombres antiguos (alias):** `0xB4C8D77C80C0421E` (`N_0xb4c8d77c80c0421e`)

---
### SetPedWeaponLiveryColor

`_SET_PED_WEAPON_LIVERY_COLOR` · hash `0x9FE5633880ECD8ED` · **Cliente**

```lua
SetPedWeaponLiveryColor(ped, weaponHash, camoComponentHash, colorIndex)
```
```c
void _SET_PED_WEAPON_LIVERY_COLOR(Ped ped, Hash weaponHash, Hash camoComponentHash, int colorIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `camoComponentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `colorIndex` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9FE5633880ECD8ED` (`N_0x9fe5633880ecd8ed`)

---
### SetPedWeaponTintIndex

`SET_PED_WEAPON_TINT_INDEX` · hash `0x50969B9B89ED5738` · jhash `0xEB2A7B23` · **Cliente**

```lua
SetPedWeaponTintIndex(ped, weaponHash, tintIndex)
```
```c
void SET_PED_WEAPON_TINT_INDEX(Ped ped, Hash weaponHash, int tintIndex);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The target weapon hash
- `tintIndex` (`int`): Tint for weapon hash

**Devuelve:** `void`

**Descripción oficial:**

```
tintIndex can be the following:  
0 : Default/Black
1 : Green
2 : Gold
3 : Pink
4 : Army
5 : LSPD
6 : Orange
7 : Platinum

tintIndex for MK2 weapons :
0 : Classic Black
1 : Classic Gray
2 : Classic Two-Tone
3 : Classic White
4 : Classic Beige
5 : Classic Green
6 : Classic Blue
7 : Classic Earth
8 : Classic Brown & Black
9 : Red Contrast
10 : Blue Contrast
11 : Yellow Contrast
12 : Orange Contrast
13 : Bold Pink
14 : Bold Purple & Yellow
15 : Bold Orange
16 : Bold Green & Purple
17 : Bold Red Features
18 : Bold Green Features
19 : Bold Cyan Features
20 : Bold Yellow Features
21 : Bold Red & White
22 : Bold Blue & White
23 : Metallic Gold
24 : Metallic Platinum
25 : Metallic Gray & Lilac
26 : Metallic Purple & Lime
27 : Metallic Red
28 : Metallic Green
29 : Metallic Blue
30 : Metallic White & Aqua
31 : Metallic Orange & Yellow
32 : Mettalic Red and Yellow
```

---
### SetPickupAmmoAmountScaler

`SET_PICKUP_AMMO_AMOUNT_SCALER` · hash `0xE620FD3512A04F18` · jhash `0xD6460EA2` · **Cliente**

```lua
SetPickupAmmoAmountScaler(p0)
```
```c
void SET_PICKUP_AMMO_AMOUNT_SCALER(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE620FD3512A04F18` (`N_0xe620fd3512a04f18`)

---
### SetPlayerAirDefenseZoneFlag

`_SET_PLAYER_AIR_DEFENSE_ZONE_FLAG` · hash `0xECDC202B25E5CF48` · **Cliente**

```lua
SetPlayerAirDefenseZoneFlag(player, zoneId, enable)
```
```c
void _SET_PLAYER_AIR_DEFENSE_ZONE_FLAG(Player player, int zoneId, BOOL enable);
```

**Parámetros**

- `player` (`Player`)
- `zoneId` (`int`)
- `enable` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xECDC202B25E5CF48` (`N_0xecdc202b25e5cf48`)

---
### SetWeaponAnimationOverride

`SET_WEAPON_ANIMATION_OVERRIDE` · hash `0x1055AC3A667F09D9` · jhash `0xA5DF7484` · **Cliente**

```lua
SetWeaponAnimationOverride(ped, animStyle)
```
```c
void SET_WEAPON_ANIMATION_OVERRIDE(Ped ped, Hash animStyle);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `animStyle` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The animation style to apply, passed as a hash.

**Devuelve:** `void`

**Descripción oficial:**

Changes the selected ped aiming animation style, you can find the list of animations below.

These are stored in the `weaponanimations.meta` file located in `Grand Theft Auto V\update\update.rpf\common\data\ai\weaponanimations.meta`.

For Lua, it's best if you send the animation using [compile-time jenkins](https://cookbook.fivem.net/2019/06/23/lua-support-for-compile-time-jenkins-hashes/) hashes to avoid overhead. An example is shown down below.

**Animations**

```cpp
enum eWeaponAnimationOverrides {
	Ballistic = 0x5534A626,
	Default = 0xE4DF46D5,
	Franklin = 0x44C24694,
	Gang = 0xBC066B98,
	Michael = 0x55932F38,
	MP_F_Freemode = 0xACB10C83,
	Trevor = 0x2737D5AC,
	Hillbilly = 0x8503D409,
	Gang1H = 0x724A7AB7,
	FirstPerson = 0xEE38E8E0,
	FirstPersonAiming = 0xC76297A3,
	FirstPersonRNG = 0xA4FDD608,
	FirstPersonScope = 0x28117C22,
	FirstPersonMichael = 0xEAA2550B,
	FirstPersonMichaelAiming = 0x3E6FF30F,
	FirstPersonMichaelRNG = 0xB7A826C1,
	FirstPersonMichaelScope = 0xC554CF97,
	FirstPersonFranklin = 0xC407163A,
	FirstPersonFranklinAiming = 0x3D4B7B03,
	FirstPersonFranklinRNG = 0xBE79B0B4,
	FirstPersonFranklinScope = 0xAFEA6593,
	FirstPersonTrevor = 0xA65D5351,
	FirstPersonTrevorAiming = 0xF9BE8ED9,
	FirstPersonTrevorRNG = 0xD181ED09,
	FirstPersonTrevorScope = 0x34A67D6D,
	FirstPersonMPFemale = 0x8431583F,
	Fat = 0xC531A409,
	SuperFat = 0x529E5780,
	Female = 0x6D155A1B,
	GangFemale = 0x678ADF82,
}
```

**Ejemplo (lua):**

```lua
-- Works when holding a pistol.
-- 'Hillbilly' also works for most peds.
SetWeaponAnimationOverride(PlayerPedId(), `Gang1H`)
```

---
### SetWeaponDamageModifier

`_SET_WEAPON_DAMAGE_MODIFIER` · hash `0x4757F00BC6323CFE` · **Cliente**

```lua
SetWeaponDamageModifier(weaponHash, damageMultiplier)
```
```c
void _SET_WEAPON_DAMAGE_MODIFIER(Hash weaponHash, float damageMultiplier);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Hash of the weapon
- `damageMultiplier` (`float`): Damage Multiplier

**Devuelve:** `void`

**Descripción oficial:**

Changes the weapon damage output by the given multiplier value.
Does NOT need to be called every frame.

**Nombres antiguos (alias):** `0x4757F00BC6323CFE` (`N_0x4757f00bc6323cfe`), `_SET_WEAPON_DAMAGE_MODIFIER_THIS_FRAME` (`SetWeaponDamageModifierThisFrame`)

**Ejemplo (lua):**

```lua
SetWeaponDamageModifier(`WEAPON_CARBINERIFLE`, 0.8)
```

---
### SetWeaponExplosionRadiusMultiplier

`_SET_WEAPON_EXPLOSION_RADIUS_MULTIPLIER` · hash `0x4AE5AC8B852D642C` · **Cliente**

```lua
SetWeaponExplosionRadiusMultiplier(weaponHash, multiplier)
```
```c
void _SET_WEAPON_EXPLOSION_RADIUS_MULTIPLIER(Hash weaponHash, float multiplier);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### SetWeaponObjectLiveryColor

`_SET_WEAPON_OBJECT_LIVERY_COLOR` · hash `0x5DA825A85D0EA6E6` · **Cliente**

```lua
SetWeaponObjectLiveryColor(weaponObject, camoComponentHash, colorIndex)
```
```c
void _SET_WEAPON_OBJECT_LIVERY_COLOR(Object weaponObject, Hash camoComponentHash, int colorIndex);
```

**Parámetros**

- `weaponObject` (`Object`)
- `camoComponentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `colorIndex` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5DA825A85D0EA6E6` (`N_0x5da825a85d0ea6e6`)

---
### SetWeaponObjectTintIndex

`SET_WEAPON_OBJECT_TINT_INDEX` · hash `0xF827589017D4E4A9` · jhash `0x44ACC1DA` · **Cliente**

```lua
SetWeaponObjectTintIndex(weapon, tintIndex)
```
```c
void SET_WEAPON_OBJECT_TINT_INDEX(Object weapon, int tintIndex);
```

**Parámetros**

- `weapon` (`Object`)
- `tintIndex` (`int`)

**Devuelve:** `void`

---
### TriggerVehicleWeaponReload

`_TRIGGER_VEHICLE_WEAPON_RELOAD` · hash `0x5B1513F27F279A44` · **Cliente**

```lua
local retval = TriggerVehicleWeaponReload(vehicle, seat, ped)
```
```c
BOOL _TRIGGER_VEHICLE_WEAPON_RELOAD(Vehicle vehicle, int seat, Ped ped);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle containing the weapon to reload.
- `seat` (`int`): The seat/weapon index.
- `ped` (`Ped`): The ped initiating the reload (the one using the weapon).

**Devuelve:** `BOOL` — Return `true` if reload was triggered successfully, `false` otherwise.

**Descripción oficial:**

Start a reload for a vehicle's weapon.

```
NativeDB Introduced: v3407
```

---
