# Natives de GTA V — OBJECT

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `OBJECT`: **163** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddDoorToSystem`](#adddoortosystem) · [`AreEntitiesEntirelyInsideGarage`](#areentitiesentirelyinsidegarage) · [`AttachPortablePickupToPed`](#attachportablepickuptoped) · [`BreakObjectFragmentChild`](#breakobjectfragmentchild) · [`ClearGarageArea`](#cleargaragearea) · [`ClearObjectsInsideGarage`](#clearobjectsinsidegarage) · [`CreateAmbientPickup`](#createambientpickup) · [`CreateMoneyPickups`](#createmoneypickups) · [`CreateNonNetworkedAmbientPickup`](#createnonnetworkedambientpickup) · [`CreateNonNetworkedPortablePickup`](#createnonnetworkedportablepickup) · [`CreateObject`](#createobject) · [`CreateObjectNoOffset`](#createobjectnooffset) · [`CreatePickup`](#createpickup) · [`CreatePickupRotate`](#createpickuprotate) · [`CreatePortablePickup`](#createportablepickup) · [`DeleteObject`](#deleteobject) · [`DetachPortablePickupFromPed`](#detachportablepickupfromped) · [`DoesObjectOfTypeExistAtCoords`](#doesobjectoftypeexistatcoords) · [`DoesPickupExist`](#doespickupexist) · [`DoesPickupObjectExist`](#doespickupobjectexist) · [`DoesPickupOfTypeExistInArea`](#doespickupoftypeexistinarea) · [`DoesRayfireMapObjectExist`](#doesrayfiremapobjectexist) · [`DoorControl`](#doorcontrol) · [`DoorSystemFindExistingDoor`](#doorsystemfindexistingdoor) · [`DoorSystemGetAutomaticDistance`](#doorsystemgetautomaticdistance) · [`DoorSystemGetDoorPendingState`](#doorsystemgetdoorpendingstate) · [`DoorSystemGetDoorState`](#doorsystemgetdoorstate) · [`DoorSystemGetIsPhysicsLoaded`](#doorsystemgetisphysicsloaded) · [`DoorSystemGetOpenRatio`](#doorsystemgetopenratio) · [`DoorSystemSetAutomaticDistance`](#doorsystemsetautomaticdistance) · [`DoorSystemSetAutomaticRate`](#doorsystemsetautomaticrate) · [`DoorSystemSetDoorState`](#doorsystemsetdoorstate) · [`DoorSystemSetHoldOpen`](#doorsystemsetholdopen) · [`DoorSystemSetOpenRatio`](#doorsystemsetopenratio) · [`DoorSystemSetSpringRemoved`](#doorsystemsetspringremoved) · [`EnableSavingInGarage`](#enablesavingingarage) · [`FixObjectFragment`](#fixobjectfragment) · [`ForcePickupRegenerate`](#forcepickupregenerate) · [`GetClosestObjectOfType`](#getclosestobjectoftype) · [`GetCoordsAndRotationOfClosestObjectOfType`](#getcoordsandrotationofclosestobjectoftype) · [`GetIsArenaPropPhysicsDisabled`](#getisarenapropphysicsdisabled) · [`GetObjectFragmentDamageHealth`](#getobjectfragmentdamagehealth) · [`GetObjectTextureVariation`](#getobjecttexturevariation) · [`GetOffsetFromCoordAndHeadingInWorldCoords`](#getoffsetfromcoordandheadinginworldcoords) · [`GetPickupCoords`](#getpickupcoords) · [`GetPickupGenerationRangeMultiplier`](#getpickupgenerationrangemultiplier) · [`GetPickupHash`](#getpickuphash) · [`GetPickupHashFromWeapon`](#getpickuphashfromweapon) · [`GetPickupObject`](#getpickupobject) · [`GetRayfireMapObject`](#getrayfiremapobject) · [`GetRayfireMapObjectAnimPhase`](#getrayfiremapobjectanimphase) · [`GetSafePickupCoords`](#getsafepickupcoords) · [`GetStateOfClosestDoorOfType`](#getstateofclosestdooroftype) · [`GetStateOfRayfireMapObject`](#getstateofrayfiremapobject) · [`GetWeaponTypeFromPickupType`](#getweapontypefrompickuptype) · [`HasClosestObjectOfTypeBeenBroken`](#hasclosestobjectoftypebeenbroken) · [`HasClosestObjectOfTypeBeenCompletelyDestroyed`](#hasclosestobjectoftypebeencompletelydestroyed) · [`HasObjectBeenBroken`](#hasobjectbeenbroken) · [`HasPickupBeenCollected`](#haspickupbeencollected) · [`HidePortablePickupWhenDetached`](#hideportablepickupwhendetached) · [`IsAnyEntityEntirelyInsideGarage`](#isanyentityentirelyinsidegarage) · [`IsAnyObjectNearPoint`](#isanyobjectnearpoint) · [`IsDoorClosed`](#isdoorclosed) · [`IsDoorRegisteredWithSystem`](#isdoorregisteredwithsystem) · [`IsGarageEmpty`](#isgarageempty) · [`IsObjectAPickup`](#isobjectapickup) · [`IsObjectAPortablePickup`](#isobjectaportablepickup) · [`IsObjectEntirelyInsideGarage`](#isobjectentirelyinsidegarage) · [`IsObjectNearPoint`](#isobjectnearpoint) · [`IsObjectPartiallyInsideGarage`](#isobjectpartiallyinsidegarage) · [`IsObjectVisible`](#isobjectvisible) · [`IsPickupWeaponObjectValid`](#ispickupweaponobjectvalid) · [`IsPlayerEntirelyInsideGarage`](#isplayerentirelyinsidegarage) · [`IsPlayerPartiallyInsideGarage`](#isplayerpartiallyinsidegarage) · [`IsPointInAngledArea`](#ispointinangledarea) · [`MarkObjectForDeletion`](#markobjectfordeletion) · [`N_0x006e4b040ed37ec3`](#n_0x006e4b040ed37ec3) · [`N_0x0596843b34b95ce5`](#n_0x0596843b34b95ce5) · [`N_0x1a6cbb06e2d0d79d`](#n_0x1a6cbb06e2d0d79d) · [`N_0x1c57c94a6446492a`](#n_0x1c57c94a6446492a) · [`N_0x1e3f1b1b891a2aaa`](#n_0x1e3f1b1b891a2aaa) · [`N_0x2542269291c6ac84`](#n_0x2542269291c6ac84) · [`N_0x27f248c3febfaad3`](#n_0x27f248c3febfaad3) · [`N_0x31574b1b41268673`](#n_0x31574b1b41268673) · [`N_0x31f924b53eaddf65`](#n_0x31f924b53eaddf65) · [`N_0x394cd08e31313c28`](#n_0x394cd08e31313c28) · [`N_0x39a5fb7eaf150840`](#n_0x39a5fb7eaf150840) · [`N_0x3b2fd68db5f8331c`](#n_0x3b2fd68db5f8331c) · [`N_0x3bd770d281982db5`](#n_0x3bd770d281982db5) · [`N_0x46f3add1e2d5baf2`](#n_0x46f3add1e2d5baf2) · [`N_0x4c134b4df76025d0`](#n_0x4c134b4df76025d0) · [`N_0x62454a641b41f3c5`](#n_0x62454a641b41f3c5) · [`N_0x63ecf581bc70e363`](#n_0x63ecf581bc70e363) · [`N_0x641f272b52e2f0f8`](#n_0x641f272b52e2f0f8) · [`N_0x659f9d71f52843f8`](#n_0x659f9d71f52843f8) · [`N_0x66a49d021870fe88`](#n_0x66a49d021870fe88) · [`N_0x701fda1e82076ba4`](#n_0x701fda1e82076ba4) · [`N_0x734e1714d077da9a`](#n_0x734e1714d077da9a) · [`N_0x762db2d380b48d04`](#n_0x762db2d380b48d04) · [`N_0x7813e8b8c4ae4799`](#n_0x7813e8b8c4ae4799) · [`N_0x826d1ee4d1cafc78`](#n_0x826d1ee4d1cafc78) · [`N_0x834344a414c7c85d`](#n_0x834344a414c7c85d) · [`N_0x858ec9fd25de04aa`](#n_0x858ec9fd25de04aa) · [`N_0x8881c98a31117998`](#n_0x8881c98a31117998) · [`N_0x8caab2bd3ea58bd4`](#n_0x8caab2bd3ea58bd4) · [`N_0x8cff648fbd7330f1`](#n_0x8cff648fbd7330f1) · [`N_0x8dca505a5c196f05`](#n_0x8dca505a5c196f05) · [`N_0xa08fe5e49bdc39dd`](#n_0xa08fe5e49bdc39dd) · [`N_0xa2c1f5e92afe49ed`](#n_0xa2c1f5e92afe49ed) · [`N_0xa85a21582451e951`](#n_0xa85a21582451e951) · [`N_0xaa059c615de9dd03`](#n_0xaa059c615de9dd03) · [`N_0xadf084fb8f075d06`](#n_0xadf084fb8f075d06) · [`N_0xafe24e4d29249e4a`](#n_0xafe24e4d29249e4a) · [`N_0xb2d0bde54f0e8e5a`](#n_0xb2d0bde54f0e8e5a) · [`N_0xb5b7742424bd4445`](#n_0xb5b7742424bd4445) · [`N_0xb7c6d80fb371659a`](#n_0xb7c6d80fb371659a) · [`N_0xbffe53ae7e67fcdc`](#n_0xbffe53ae7e67fcdc) · [`N_0xc6033d32241f6fb5`](#n_0xc6033d32241f6fb5) · [`N_0xc7f29ca00f46350e`](#n_0xc7f29ca00f46350e) · [`N_0xd05a3241b9a86f19`](#n_0xd05a3241b9a86f19) · [`N_0xd4a7a435b3710d05`](#n_0xd4a7a435b3710d05) · [`N_0xdb41d07a45a6d4b7`](#n_0xdb41d07a45a6d4b7) · [`N_0xe05f6aeefeb0bb02`](#n_0xe05f6aeefeb0bb02) · [`N_0xeb6f1a9b5510a5d2`](#n_0xeb6f1a9b5510a5d2) · [`N_0xf92099527db8e2a7`](#n_0xf92099527db8e2a7) · [`N_0xfdc07c58e8aab715`](#n_0xfdc07c58e8aab715) · [`PlaceObjectOnGroundOrObjectProperly`](#placeobjectongroundorobjectproperly) · [`PlaceObjectOnGroundProperly`](#placeobjectongroundproperly) · [`PreventCollectionOfPortablePickup`](#preventcollectionofportablepickup) · [`RemoveAllPickupsOfType`](#removeallpickupsoftype) · [`RemoveDoorFromSystem`](#removedoorfromsystem) · [`RemoveObjectHighDetailModel`](#removeobjecthighdetailmodel) · [`RemovePickup`](#removepickup) · [`RenderFakePickupGlow`](#renderfakepickupglow) · [`SetActivateObjectPhysicsAsSoonAsItIsUnfrozen`](#setactivateobjectphysicsassoonasitisunfrozen) · [`SetCreateWeaponObjectLightSource`](#setcreateweaponobjectlightsource) · [`SetEnableArenaPropPhysics`](#setenablearenapropphysics) · [`SetEnableArenaPropPhysicsOnPed`](#setenablearenapropphysicsonped) · [`SetForceObjectThisFrame`](#setforceobjectthisframe) · [`SetLocalPlayerCanCollectPortablePickups`](#setlocalplayercancollectportablepickups) · [`SetLocalPlayerCanUsePickupsWithThisModel`](#setlocalplayercanusepickupswiththismodel) · [`SetMaxNumPortablePickupsCarriedByPlayer`](#setmaxnumportablepickupscarriedbyplayer) · [`SetObjectAllowLowLodBuoyancy`](#setobjectallowlowlodbuoyancy) · [`SetObjectForceVehiclesToAvoid`](#setobjectforcevehiclestoavoid) · [`SetObjectLightColor`](#setobjectlightcolor) · [`SetObjectPhysicsParams`](#setobjectphysicsparams) · [`SetObjectStuntPropDuration`](#setobjectstuntpropduration) · [`SetObjectStuntPropSpeedup`](#setobjectstuntpropspeedup) · [`SetObjectTargettable`](#setobjecttargettable) · [`SetObjectTargettableByPlayer`](#setobjecttargettablebyplayer) · [`SetObjectTextureVariation`](#setobjecttexturevariation) · [`SetPickupGenerationRangeMultiplier`](#setpickupgenerationrangemultiplier) · [`SetPickupHiddenWhenUncollectable`](#setpickuphiddenwhenuncollectable) · [`SetPickupRegenerationTime`](#setpickupregenerationtime) · [`SetPickupUncollectable`](#setpickupuncollectable) · [`SetStateOfClosestDoorOfType`](#setstateofclosestdooroftype) · [`SetStateOfRayfireMapObject`](#setstateofrayfiremapobject) · [`SetTeamPickupObject`](#setteampickupobject) · [`SetTextureVariationOfClosestObjectOfType`](#settexturevariationofclosestobjectoftype) · [`SetUnkGlobalBoolRelatedToDamage`](#setunkglobalboolrelatedtodamage) · [`SlideObject`](#slideobject) · [`ToggleUsePickupsForPlayer`](#toggleusepickupsforplayer) · [`TrackObjectVisibility`](#trackobjectvisibility)

---
### AddDoorToSystem

`ADD_DOOR_TO_SYSTEM` · hash `0x6F8838D03D1DC226` · jhash `0x9D2D778D` · **Cliente**

```lua
AddDoorToSystem(doorHash, modelHash, x, y, z, p5, scriptDoor, isLocal)
```
```c
void ADD_DOOR_TO_SYSTEM(Hash doorHash, Hash modelHash, float x, float y, float z, BOOL p5, BOOL scriptDoor, BOOL isLocal);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: A (unique) door system identifier
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Entity model hash
- `x` (`float`): The X coordinate of the door object
- `y` (`float`): The Y coordinate of the door object
- `z` (`float`): The Z coordinate of the door object
- `p5` (`BOOL`)
- `scriptDoor` (`BOOL`): false; relies upon getNetworkGameScriptHandler.
- `isLocal` (`BOOL`): On true disables the creation `CRequestDoorEvent's` in [DOOR_SYSTEM_SET_DOOR_STATE](#doorsystemsetdoorstate).

**Devuelve:** `void`

**Descripción oficial:**

p5 only set to true in single player native scripts. Door hashes normally look like `PROP_[int]_DOOR_[int]` for interior doors and `PROP_BUILDING_[int]_DOOR_[int]` exterior doors but you can just make up your own hash if you want.

If scriptDoor is true, register the door on the script handler host (note: there's a hardcap on the number of script IDs that can be added to the system at a given time). If scriptDoor and isLocal are both false, the door is considered to be in a "Persists w/o netobj" state.

A simple "localized" door-system (with hundreds/thousands of doors) can be created by setting p5, p6, and p7 to false and using EventHandlers to synchronize the states to: [DOOR_SYSTEM_SET_DOOR_STATE](#doorsystemsetdoorstate), [DOOR_SYSTEM_SET_OPEN_RATIO](#doorsystemsetopenratio), [DOOR_SYSTEM_SET_HOLD_OPEN](#doorsystemsetholdopen), etc.

---
### AreEntitiesEntirelyInsideGarage

`ARE_ENTITIES_ENTIRELY_INSIDE_GARAGE` · hash `0x85B6C850546FDDE2` · jhash `0x4BD59750` · **Cliente**

```lua
local retval = AreEntitiesEntirelyInsideGarage(garageHash, p1, p2, p3, p4)
```
```c
BOOL ARE_ENTITIES_ENTIRELY_INSIDE_GARAGE(Hash garageHash, BOOL p1, BOOL p2, BOOL p3, Any p4);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)
- `p4` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x85B6C850546FDDE2` (`N_0x85b6c850546fdde2`)

---
### AttachPortablePickupToPed

`ATTACH_PORTABLE_PICKUP_TO_PED` · hash `0x8DC39368BDD57755` · jhash `0x184F6AB3` · **Cliente**

```lua
AttachPortablePickupToPed(pickupObject, ped)
```
```c
void ATTACH_PORTABLE_PICKUP_TO_PED(Object pickupObject, Ped ped);
```

**Parámetros**

- `pickupObject` (`Object`)
- `ped` (`Ped`)

**Devuelve:** `void`

---
### BreakObjectFragmentChild

`BREAK_OBJECT_FRAGMENT_CHILD` · hash `0xE7E4C198B0185900` · jhash `0x1E82C2AE` · **Cliente**

```lua
BreakObjectFragmentChild(p0, p1, p2)
```
```c
void BREAK_OBJECT_FRAGMENT_CHILD(Object p0, Any p1, BOOL p2);
```

**Parámetros**

- `p0` (`Object`)
- `p1` (`Any`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE7E4C198B0185900` (`N_0xe7e4c198b0185900`)

---
### ClearGarageArea

`_CLEAR_GARAGE_AREA` · hash `0xDA05194260CDCDF9` · **Cliente**

```lua
ClearGarageArea(garageHash, isNetwork)
```
```c
void _CLEAR_GARAGE_AREA(Hash garageHash, BOOL isNetwork);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `isNetwork` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDA05194260CDCDF9` (`N_0xda05194260cdcdf9`)

---
### ClearObjectsInsideGarage

`CLEAR_OBJECTS_INSIDE_GARAGE` · hash `0x190428512B240692` · jhash `0xA565E27E` · **Cliente**

```lua
ClearObjectsInsideGarage(garageHash, vehicles, peds, objects, isNetwork)
```
```c
void CLEAR_OBJECTS_INSIDE_GARAGE(Hash garageHash, BOOL vehicles, BOOL peds, BOOL objects, BOOL isNetwork);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `vehicles` (`BOOL`)
- `peds` (`BOOL`)
- `objects` (`BOOL`)
- `isNetwork` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x190428512B240692` (`N_0x190428512b240692`)

---
### CreateAmbientPickup

`CREATE_AMBIENT_PICKUP` · hash `0x673966A0C0FD7171` · jhash `0x17B99CE7` · **Cliente**

```lua
local retval = CreateAmbientPickup(pickupHash, posX, posY, posZ, flags, value, modelHash, returnHandle, p8)
```
```c
Pickup CREATE_AMBIENT_PICKUP(Hash pickupHash, float posX, float posY, float posZ, int flags, int value, Hash modelHash, BOOL returnHandle, BOOL p8);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `flags` (`int`)
- `value` (`int`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `returnHandle` (`BOOL`)
- `p8` (`BOOL`)

**Devuelve:** `Pickup`

**Descripción oficial:**

Creates an ambient pickup given the hash. Pickup hashes can be found [here](https://gist.github.com/4mmonium/1eabfb6b3996e3aa6b9525a3eccf8a0b).

---
### CreateMoneyPickups

`CREATE_MONEY_PICKUPS` · hash `0x0589B5E791CE9B2B` · jhash `0x36C9A5EA` · **Cliente**

```lua
CreateMoneyPickups(x, y, z, value, amount, model)
```
```c
void CREATE_MONEY_PICKUPS(float x, float y, float z, int value, int amount, Hash model);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `value` (`int`)
- `amount` (`int`)
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Spawns one or more money pickups.  
x: The X-component of the world position to spawn the money pickups at.  
y: The Y-component of the world position to spawn the money pickups at.  
z: The Z-component of the world position to spawn the money pickups at.  
value: The combined value of the pickups (in dollars).  
amount: The number of pickups to spawn.  
model: The model to use, or 0 for default money model.  
Example:  
CREATE_MONEY_PICKUPS(x, y, z, 1000, 3, 0x684a97ae);  
Spawns 3 spray cans that'll collectively give $1000 when picked up. (Three spray cans, each giving $334, $334, $332 = $1000).  
==============================================  
Max is 2000 in MP. So if you put the amount to 20, but the value to $400,000 eg. They will only be able to pickup 20 - $2,000 bags. So, $40,000  
```

---
### CreateNonNetworkedAmbientPickup

`_CREATE_NON_NETWORKED_AMBIENT_PICKUP` · hash `0x9C93764223E29C50` · **Cliente**

```lua
local retval = CreateNonNetworkedAmbientPickup(pickupHash, posX, posY, posZ, flags, value, modelHash, p7, p8)
```
```c
Any _CREATE_NON_NETWORKED_AMBIENT_PICKUP(Any pickupHash, float posX, float posY, float posZ, int flags, int value, Any modelHash, BOOL p7, BOOL p8);
```

**Parámetros**

- `pickupHash` (`Any`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `flags` (`int`)
- `value` (`int`)
- `modelHash` (`Any`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x9C93764223E29C50` (`N_0x9c93764223e29c50`)

---
### CreateNonNetworkedPortablePickup

`CREATE_NON_NETWORKED_PORTABLE_PICKUP` · hash `0x125494B98A21AAF7` · jhash `0x56A02502` · **Cliente**

```lua
local retval = CreateNonNetworkedPortablePickup(pickupHash, x, y, z, placeOnGround, modelHash)
```
```c
Object CREATE_NON_NETWORKED_PORTABLE_PICKUP(Hash pickupHash, float x, float y, float z, BOOL placeOnGround, Hash modelHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `placeOnGround` (`BOOL`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Object`

**Nombres antiguos (alias):** `0x125494B98A21AAF7` (`N_0x125494b98a21aaf7`), `_CREATE_PORTABLE_PICKUP_2` (`CreatePortablePickup_2`)

---
### CreateObject

`CREATE_OBJECT` · hash `0x509D5878EB39E842` · jhash `0x2F7AA05C` · **Cliente · también en el servidor (RPC)**

```lua
local retval = CreateObject(modelHash, x, y, z, isNetwork, netMissionEntity, doorFlag)
```
```c
Object CREATE_OBJECT(Hash modelHash, float x, float y, float z, BOOL isNetwork, BOOL netMissionEntity, BOOL doorFlag);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to spawn.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component, 'ground level'.
- `isNetwork` (`BOOL`): Whether to create a network object for the object. If false, the object exists only locally.
- `netMissionEntity` (`BOOL`): Whether to register the object as pinned to the script host in the R\* network model.
- `doorFlag` (`BOOL`): False to create a door archetype (archetype flag bit 26 set) as a door. Required to be set to true to create door models in network mode.

**Devuelve:** `Object` — A script handle (fwScriptGuid index) for the object, or `0` if the object failed to be created.

**Descripción oficial:**

Creates an object (prop) with the specified model at the specified position, offset on the Z axis by the radius of the object's model.
This object will initially be owned by the creating script as a mission entity, and the model should be loaded already (e.g. using REQUEST_MODEL).

**Ejemplo (lua):**

```lua
local modelHash = `prop_weed_01` -- The ` return the jenkins hash of a string. see more at: https://cookbook.fivem.net/2019/06/23/lua-support-for-compile-time-jenkins-hashes/

if not HasModelLoaded(modelHash) then
    -- If the model isnt loaded we request the loading of the model and wait that the model is loaded
    RequestModel(modelHash)

    while not HasModelLoaded(modelHash) do
        Citizen.Wait(1)
    end
end

-- At this moment the model its loaded, so now we can create the object
local obj = CreateObject(modelHash, vector3(0.0, 0.0, 0.0), true)
```

**Ejemplo (js):**

```js
async function Main() {
    const modelHash = GetHashKey("prop_weed_01");

    if (!HasModelLoaded(modelHash)) {
        // If the model isnt loaded we request the loading of the model and wait that the model is loaded
        RequestModel(modelHash);
        do {
            new Promise(resolve => setTimeout(resolve, 100));
        } while (!HasModelLoaded(modelHash));
    }

    // At this moment the model its loaded, so now we can create the object
    let [x, y, z] = GetEntityCoords(PlayerPedId());
    const obj = CreateObject(modelHash, x, y, z, true);
}

Main();
```

---
### CreateObjectNoOffset

`CREATE_OBJECT_NO_OFFSET` · hash `0x9A294B2138ABB884` · jhash `0x58040420` · **Cliente · también en el servidor (RPC)**

```lua
local retval = CreateObjectNoOffset(modelHash, x, y, z, isNetwork, netMissionEntity, doorFlag)
```
```c
Object CREATE_OBJECT_NO_OFFSET(Hash modelHash, float x, float y, float z, BOOL isNetwork, BOOL netMissionEntity, BOOL doorFlag);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to spawn.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `isNetwork` (`BOOL`): Whether to create a network object for the object. If false, the object exists only locally.
- `netMissionEntity` (`BOOL`): Whether to register the object as pinned to the script host in the R\* network model.
- `doorFlag` (`BOOL`): False to create a door archetype (archetype flag bit 26 set) as a door. Required to be set to true to create door models in network mode.

**Devuelve:** `Object` — A script handle (fwScriptGuid index) for the object, or `0` if the object failed to be created.

**Descripción oficial:**

Creates an object (prop) with the specified model centered at the specified position.
This object will initially be owned by the creating script as a mission entity, and the model should be loaded already (e.g. using REQUEST_MODEL).

---
### CreatePickup

`CREATE_PICKUP` · hash `0xFBA08C503DD5FA58` · jhash `0x5E14DF68` · **Cliente**

```lua
local retval = CreatePickup(pickupHash, posX, posY, posZ, p4, value, p6, modelHash)
```
```c
Pickup CREATE_PICKUP(Hash pickupHash, float posX, float posY, float posZ, int p4, int value, BOOL p6, Hash modelHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `p4` (`int`)
- `value` (`int`)
- `p6` (`BOOL`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Pickup`

**Descripción oficial:**

Pickup hashes can be found [here](https://gist.github.com/4mmonium/1eabfb6b3996e3aa6b9525a3eccf8a0b).

---
### CreatePickupRotate

`CREATE_PICKUP_ROTATE` · hash `0x891804727E0A98B7` · jhash `0xF015BFE2` · **Cliente**

```lua
local retval = CreatePickupRotate(pickupHash, posX, posY, posZ, rotX, rotY, rotZ, flag, amount, p9, p10, modelHash)
```
```c
Pickup CREATE_PICKUP_ROTATE(Hash pickupHash, float posX, float posY, float posZ, float rotX, float rotY, float rotZ, int flag, int amount, Any p9, BOOL p10, Hash modelHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `flag` (`int`)
- `amount` (`int`)
- `p9` (`Any`)
- `p10` (`BOOL`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Pickup`

**Descripción oficial:**

```
Pickup hashes: pastebin.com/8EuSv2r1  
flags:  
8 (1 << 3): place on ground  
512 (1 << 9): spin around  
```

---
### CreatePortablePickup

`CREATE_PORTABLE_PICKUP` · hash `0x2EAF1FDB2FB55698` · jhash `0x8C886BE5` · **Cliente**

```lua
local retval = CreatePortablePickup(pickupHash, x, y, z, placeOnGround, modelHash)
```
```c
Object CREATE_PORTABLE_PICKUP(Hash pickupHash, float x, float y, float z, BOOL placeOnGround, Hash modelHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `placeOnGround` (`BOOL`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Object`

**Descripción oficial:**

Pickup hashes can be found [here](https://gist.github.com/4mmonium/1eabfb6b3996e3aa6b9525a3eccf8a0b).

---
### DeleteObject

`DELETE_OBJECT` · hash `0x539E0AE3E6634B9F` · jhash `0xD6EF9DA7` · **Cliente**

```lua
local object = DeleteObject(object)
```
```c
void DELETE_OBJECT(Object* object);
```

**Parámetros**

- `object` (`Object*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The object you want to delete.

**Devuelve:** `void`

**Descripción oficial:**

Deletes the specified object.

**Note**: If for some reason the entity won't delete, you might want to check if the object is a mission entity.

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local playerCoords = GetEntityCoords(playerPed)
local objectHash = GetHashKey("v_ret_gc_chair03")

local object = GetClosestObjectOfType(playerCoords, 10.0, objectHash, true, false, false)
if object == 0 then return end

-- If the object is a mission entity, we have to set it to false. Otherwise, it won't be possible to delete the object.
if IsEntityAMissionEntity(object) then
    SetEntityAsMissionEntity(object, false, true)
end

DeleteObject(object)
```

**Ejemplo (js):**

```js
const playerPed = PlayerPedId();
const playerCoords = GetEntityCoords(playerPed, false);
const objectHash = GetHashKey("v_ret_gc_chair03");

const object = GetClosestObjectOfType(playerCoords[0], playerCoords[1], playerCoords[2], 10.0, objectHash, true, false, false);
if (object === 0) return;

// If the object is a mission entity, we have to set it to false. Otherwise, it won't be possible to delete the object.
if (IsEntityAMissionEntity(object)) {
    SetEntityAsMissionEntity(object, false, true);
}

DeleteObject(object);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int playerPed = PlayerPedId();
Vector3 playerCoords = GetEntityCoords(playerPed, false);
uint objectHash = Game.GenerateHashASCII("v_ret_gc_chair03");

int prop = GetClosestObjectOfType(playerCoords.X, playerCoords.Y, playerCoords.Z, 10.0f, objectHash, true, false, false);
if (prop == 0) return;
// If the object is a mission entity, we have to set it to false. Otherwise, it won't be possible to delete the object.
if (IsEntityAMissionEntity(prop))
{
    SetEntityAsMissionEntity(prop, false, true);
}

DeleteObject(ref prop);
```

---
### DetachPortablePickupFromPed

`DETACH_PORTABLE_PICKUP_FROM_PED` · hash `0xCF463D1E9A0AECB1` · jhash `0x1D094562` · **Cliente**

```lua
DetachPortablePickupFromPed(pickupObject)
```
```c
void DETACH_PORTABLE_PICKUP_FROM_PED(Object pickupObject);
```

**Parámetros**

- `pickupObject` (`Object`)

**Devuelve:** `void`

---
### DoesObjectOfTypeExistAtCoords

`DOES_OBJECT_OF_TYPE_EXIST_AT_COORDS` · hash `0xBFA48E2FF417213F` · jhash `0x23FF2BA4` · **Cliente**

```lua
local retval = DoesObjectOfTypeExistAtCoords(x, y, z, radius, hash, p5)
```
```c
BOOL DOES_OBJECT_OF_TYPE_EXIST_AT_COORDS(float x, float y, float z, float radius, Hash hash, BOOL p5);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p5` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p5 is usually 0.  
```

---
### DoesPickupExist

`DOES_PICKUP_EXIST` · hash `0xAFC1CA75AD4074D1` · jhash `0x9C6DA0B3` · **Cliente**

```lua
local retval = DoesPickupExist(pickup)
```
```c
BOOL DOES_PICKUP_EXIST(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `BOOL`

---
### DoesPickupObjectExist

`DOES_PICKUP_OBJECT_EXIST` · hash `0xD9EFB6DBF7DAAEA3` · jhash `0xE0B32108` · **Cliente**

```lua
local retval = DoesPickupObjectExist(pickupObject)
```
```c
BOOL DOES_PICKUP_OBJECT_EXIST(Object pickupObject);
```

**Parámetros**

- `pickupObject` (`Object`)

**Devuelve:** `BOOL`

---
### DoesPickupOfTypeExistInArea

`DOES_PICKUP_OF_TYPE_EXIST_IN_AREA` · hash `0xF9C36251F6E48E33` · jhash `0xF139681B` · **Cliente**

```lua
local retval = DoesPickupOfTypeExistInArea(pickupHash, x, y, z, radius)
```
```c
BOOL DOES_PICKUP_OF_TYPE_EXIST_IN_AREA(Hash pickupHash, float x, float y, float z, float radius);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Pickup hashes can be found [here](https://gist.github.com/4mmonium/1eabfb6b3996e3aa6b9525a3eccf8a0b).

**Nombres antiguos (alias):** `_IS_PICKUP_WITHIN_RADIUS` (`IsPickupWithinRadius`)

---
### DoesRayfireMapObjectExist

`DOES_RAYFIRE_MAP_OBJECT_EXIST` · hash `0x52AF537A0C5B8AAD` · jhash `0xE08C834D` · **Cliente**

```lua
local retval = DoesRayfireMapObjectExist(object)
```
```c
BOOL DOES_RAYFIRE_MAP_OBJECT_EXIST(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if a destructible object with this handle exists, false otherwise.  
```

**Nombres antiguos (alias):** `0x52AF537A0C5B8AAD` (`N_0x52af537a0c5b8aad`), `_DOES_DES_OBJECT_EXIST` (`DoesDesObjectExist`)

---
### DoorControl

`_DOOR_CONTROL` · hash `0x9B12F9A24FABEDB0` · jhash `0x4E0A260B` · **Cliente**

```lua
DoorControl(modelHash, x, y, z, locked, xRotMult, yRotMult, zRotMult)
```
```c
void _DOOR_CONTROL(Hash modelHash, float x, float y, float z, BOOL locked, float xRotMult, float yRotMult, float zRotMult);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `locked` (`BOOL`): tells the game whether or not the door is locked
- `xRotMult` (`float`): multiplier that specifies how fast the door/gate will rotate in degrees per second.
- `yRotMult` (`float`): multiplier that specifies how fast the door/gate will rotate in degrees per second.
- `zRotMult` (`float`): multiplier that specifies how fast the door/gate will rotate in degrees per second.

**Devuelve:** `void`

**Descripción oficial:**

Hardcoded not to work in multiplayer environments.
Native name between `SET_LOCAL_PLAYER_VISIBLE_LOCALLY` & `SET_MAX_WANTED_LEVEL`.

```
OBJECT::_9B12F9A24FABEDB0(${prop_gate_prison_01}, 1845.0, 2605.0, 45.0, 0, 0.0, 50.0, 0);  //door unlocked
OBJECT::_9B12F9A24FABEDB0(${prop_gate_prison_01}, 1845.0, 2605.0, 45.0, 1, 0.0, 50.0, 0);  //door locked
```

**Ejemplo (lua):**

```lua
DoorControl(`prop_gate_prison_01`, 1845.0, 2605.0, 45.0, 0, 0.0, 50.0, 0) -- door unlocked
DoorControl(`prop_gate_prison_01`, 1845.0, 2605.0, 45.0, 1, 0.0, 50.0, 0) -- door locked
```

---
### DoorSystemFindExistingDoor

`DOOR_SYSTEM_FIND_EXISTING_DOOR` · hash `0x589F80B325CC82C5` · jhash `0xE9AE494F` · **Cliente**

```lua
local retval, doorOutPointer = DoorSystemFindExistingDoor(x, y, z, modelHash, doorOutPointer)
```
```c
BOOL DOOR_SYSTEM_FIND_EXISTING_DOOR(float x, float y, float z, Hash modelHash, Hash* doorOutPointer);
```

**Parámetros**

- `x` (`float`): The X coordinate of the door object
- `y` (`float`): The Y coordinate of the door object
- `z` (`float`): The Z coordinate of the door object
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Entity model hash
- `doorOutPointer` (`Hash*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Search radius: 0.5

**Nombres antiguos (alias):** `0x589F80B325CC82C5` (`N_0x589f80b325cc82c5`)

---
### DoorSystemGetAutomaticDistance

`_DOOR_SYSTEM_GET_AUTOMATIC_DISTANCE` · hash `0xE851471AEFC3374F` · **Cliente**

```lua
local retval = DoorSystemGetAutomaticDistance(doorHash)
```
```c
float _DOOR_SYSTEM_GET_AUTOMATIC_DISTANCE(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### DoorSystemGetDoorPendingState

`DOOR_SYSTEM_GET_DOOR_PENDING_STATE` · hash `0x4BC2854478F3A749` · jhash `0xD649B7E1` · **Cliente**

```lua
local retval = DoorSystemGetDoorPendingState(doorHash)
```
```c
int DOOR_SYSTEM_GET_DOOR_PENDING_STATE(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x4BC2854478F3A749` (`N_0x4bc2854478f3a749`)

---
### DoorSystemGetDoorState

`DOOR_SYSTEM_GET_DOOR_STATE` · hash `0x160AA1B32F6139B8` · jhash `0xD42A41C2` · **Cliente**

```lua
local retval = DoorSystemGetDoorState(doorHash)
```
```c
int DOOR_SYSTEM_GET_DOOR_STATE(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x160AA1B32F6139B8` (`N_0x160aa1b32f6139b8`)

---
### DoorSystemGetIsPhysicsLoaded

`DOOR_SYSTEM_GET_IS_PHYSICS_LOADED` · hash `0xDF97CDD4FC08FD34` · jhash `0x17FF9393` · **Cliente**

```lua
local retval = DoorSystemGetIsPhysicsLoaded(doorHash)
```
```c
BOOL DOOR_SYSTEM_GET_IS_PHYSICS_LOADED(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xDF97CDD4FC08FD34` (`N_0xdf97cdd4fc08fd34`)

---
### DoorSystemGetOpenRatio

`DOOR_SYSTEM_GET_OPEN_RATIO` · hash `0x65499865FCA6E5EC` · jhash `0xB74C3BD7` · **Cliente**

```lua
local retval = DoorSystemGetOpenRatio(doorHash)
```
```c
float DOOR_SYSTEM_GET_OPEN_RATIO(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x65499865FCA6E5EC` (`N_0x65499865fca6e5ec`)

---
### DoorSystemSetAutomaticDistance

`DOOR_SYSTEM_SET_AUTOMATIC_DISTANCE` · hash `0x9BA001CB45CBF627` · jhash `0x47531446` · **Cliente**

```lua
DoorSystemSetAutomaticDistance(doorHash, distance, requestDoor, forceUpdate)
```
```c
void DOOR_SYSTEM_SET_AUTOMATIC_DISTANCE(Hash doorHash, float distance, BOOL requestDoor, BOOL forceUpdate);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Door system identifier
- `distance` (`float`)
- `requestDoor` (`BOOL`)
- `forceUpdate` (`BOOL`): On true invokes [DOOR_SYSTEM_SET_DOOR_STATE](#doorsystemsetdoorstate); otherwise requestDoor is unused.

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9BA001CB45CBF627` (`N_0x9ba001cb45cbf627`)

---
### DoorSystemSetAutomaticRate

`DOOR_SYSTEM_SET_AUTOMATIC_RATE` · hash `0x03C27E13B42A0E82` · jhash `0x4F44AF21` · **Cliente**

```lua
DoorSystemSetAutomaticRate(doorHash, rate, requestDoor, forceUpdate)
```
```c
void DOOR_SYSTEM_SET_AUTOMATIC_RATE(Hash doorHash, float rate, BOOL requestDoor, BOOL forceUpdate);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Door system identifier
- `rate` (`float`)
- `requestDoor` (`BOOL`)
- `forceUpdate` (`BOOL`): On true invokes [DOOR_SYSTEM_SET_DOOR_STATE](#doorsystemsetdoorstate); otherwise requestDoor is unused.

**Devuelve:** `void`

**Descripción oficial:**

Includes networking check: ownership vs. or the door itself **isn't** networked.

**Nombres antiguos (alias):** `0x03C27E13B42A0E82` (`N_0x03c27e13b42a0e82`)

---
### DoorSystemSetDoorState

`DOOR_SYSTEM_SET_DOOR_STATE` · hash `0x6BAB9442830C7F53` · jhash `0xDF83DB47` · **Cliente**

```lua
DoorSystemSetDoorState(doorHash, state, requestDoor, forceUpdate)
```
```c
void DOOR_SYSTEM_SET_DOOR_STATE(Hash doorHash, int state, BOOL requestDoor, BOOL forceUpdate);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `state` (`int`)
- `requestDoor` (`BOOL`): On true, and when door system is configured to, i.e., "persists w/o netobj", generate a CRequestDoorEvent.
- `forceUpdate` (`BOOL`): On true, forces an update on the door system (same path as netObjDoor_applyDoorStuff)

**Devuelve:** `void`

**Descripción oficial:**

Lockstates not applied and CNetObjDoor's not created until [DOOR_SYSTEM_GET_IS_PHYSICS_LOADED](#doorsystemgetisphysicsloaded) returns true.

**Door lock states: (v323)**

*   **0**: UNLOCKED
*   **1**: LOCKED
*   **2**: DOORSTATE_FORCE_LOCKED_UNTIL_OUT_OF_AREA
*   **3**: DOORSTATE_FORCE_UNLOCKED_THIS_FRAME
*   **4**: DOORSTATE_FORCE_LOCKED_THIS_FRAME
*   **5**: DOORSTATE_FORCE_OPEN_THIS_FRAME
*   **6**: DOORSTATE_FORCE_CLOSED_THIS_FRAME

**Nombres antiguos (alias):** `0x6BAB9442830C7F53` (`N_0x6bab9442830c7f53`), `_SET_DOOR_ACCELERATION_LIMIT` (`SetDoorAccelerationLimit`)

---
### DoorSystemSetHoldOpen

`DOOR_SYSTEM_SET_HOLD_OPEN` · hash `0xD9B71952F78A2640` · jhash `0xECE58AE0` · **Cliente**

```lua
DoorSystemSetHoldOpen(doorHash, toggle)
```
```c
void DOOR_SYSTEM_SET_HOLD_OPEN(Hash doorHash, BOOL toggle);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Door system identifier
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Includes networking check: ownership vs. or the door itself **isn't** networked.

**Nombres antiguos (alias):** `0xD9B71952F78A2640` (`N_0xd9b71952f78a2640`)

---
### DoorSystemSetOpenRatio

`DOOR_SYSTEM_SET_OPEN_RATIO` · hash `0xB6E6FBA95C7324AC` · jhash `0x34883DE3` · **Cliente**

```lua
DoorSystemSetOpenRatio(doorHash, ajar, requestDoor, forceUpdate)
```
```c
void DOOR_SYSTEM_SET_OPEN_RATIO(Hash doorHash, float ajar, BOOL requestDoor, BOOL forceUpdate);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Door system identifier
- `ajar` (`float`)
- `requestDoor` (`BOOL`)
- `forceUpdate` (`BOOL`): On true invokes [DOOR_SYSTEM_SET_DOOR_STATE](#doorsystemsetdoorstate); otherwise requestDoor is unused.

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the ajar angle of a door.
Ranges from -1.0 to 1.0, and 0.0 is closed / default.
```

**Nombres antiguos (alias):** `0xB6E6FBA95C7324AC` (`N_0xb6e6fba95c7324ac`), `_SET_DOOR_AJAR_ANGLE` (`SetDoorAjarAngle`)

---
### DoorSystemSetSpringRemoved

`DOOR_SYSTEM_SET_SPRING_REMOVED` · hash `0xC485E07E4F0B7958` · jhash `0xB4A9A558` · **Cliente**

```lua
DoorSystemSetSpringRemoved(doorHash, removed, requestDoor, forceUpdate)
```
```c
void DOOR_SYSTEM_SET_SPRING_REMOVED(Hash doorHash, BOOL removed, BOOL requestDoor, BOOL forceUpdate);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Door system identifier
- `removed` (`BOOL`)
- `requestDoor` (`BOOL`)
- `forceUpdate` (`BOOL`): On true invokes [DOOR_SYSTEM_SET_DOOR_STATE](#doorsystemsetdoorstate); otherwise requestDoor is unused.

**Devuelve:** `void`

**Descripción oficial:**

Includes networking check: ownership vs. or the door itself **isn't** networked.

**Nombres antiguos (alias):** `0xC485E07E4F0B7958` (`N_0xc485e07e4f0b7958`)

---
### EnableSavingInGarage

`ENABLE_SAVING_IN_GARAGE` · hash `0xF2E1A7133DD356A6` · jhash `0x43BB7E48` · **Cliente**

```lua
EnableSavingInGarage(garageHash, toggle)
```
```c
void ENABLE_SAVING_IN_GARAGE(Hash garageHash, BOOL toggle);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF2E1A7133DD356A6` (`N_0xf2e1a7133dd356a6`)

---
### FixObjectFragment

`FIX_OBJECT_FRAGMENT` · hash `0xF9C1681347C8BD15` · **Cliente**

```lua
FixObjectFragment(object)
```
```c
void FIX_OBJECT_FRAGMENT(Object object);
```

**Parámetros**

- `object` (`Object`): The object to fix fragments for (a handle should be passed).

**Devuelve:** `void`

**Descripción oficial:**

Resets and brings back all the children of a fragment based object.
This should be used when attaching or detaching an object from another entity, especially when the object being detached consists of multiple fragments.

Attempting to teleport a fragment-based object using [`SET_ENTITY_COORDS`](../cfx/servidor.md#setentitycoords) such as a flag object, will result in it remaining in place and failing to teleport, given the condition mentioned in the preceding statement.

The native should be executed after detaching the object from its parent entity and before calling [`SET_ENTITY_COORDS`](../cfx/servidor.md#setentitycoords).

Example given down below.

**Nombres antiguos (alias):** `0xF9C1681347C8BD15` (`N_0xf9c1681347c8bd15`)

**Ejemplo (lua):**

```lua
RegisterCommand("fixobject", function(source, args, rawCommand)
    -- prop_flag_ls does not get teleported after being attached to the player
    -- prop_beachflag_01 only the pole gets teleported after being attached to the player
    local modelHash = `prop_beachflag_01`
    if not HasModelLoaded(modelHash) then
        RequestModel(modelHash)
        while not HasModelLoaded(modelHash) do
            Citizen.Wait(1)
        end
    end

    -- Set argument 1 to 0 if you wish to see what occurs when fragments aren't fixed.
    -- i.e. /fixobject 0
    local shouldFixFragments = tonumber(args[1]) or true
    
    local entity = CreateObject(modelHash, GetEntityCoords(PlayerPedId()), true, false, false)
    AttachEntityToEntity(
        entity,
        PlayerPedId(),
        GetPedBoneIndex(PlayerPedId(), 0x796E), --0x796E
        0.0, 0.0, 0.1, -- offset attachment for the first entity
        0.0, 0.0, 0.0, 
        false, 
        false, 
        false, 
        false, 
        1, -- rotation order
        true, 
        false
    )
    
    Citizen.SetTimeout(5000, function()
        DetachEntity(entity, true, true)
        Citizen.Trace("Detaching entity...")
    end)

    Citizen.SetTimeout(8000, function()
        local coords = GetEntityCoords(PlayerPedId())
        Citizen.Trace(
            string.format("Setting coords to %f %f %f...", coords.x, coords.y, coords.z)
        )
        if shouldFixFragments then
            Citizen.Trace("Fixing fragments for entity...")
            FixObjectFragment(entity)
        end
        SetEntityCoords(entity, coords, false, false, false, true)
        FreezeEntityPosition(entity, true)
    end)
end, false)
```

---
### ForcePickupRegenerate

`_FORCE_PICKUP_REGENERATE` · hash `0x758A5C1B3B1E1990` · **Cliente**

```lua
ForcePickupRegenerate(p0)
```
```c
void _FORCE_PICKUP_REGENERATE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x758A5C1B3B1E1990` (`N_0x758a5c1b3b1e1990`)

---
### GetClosestObjectOfType

`GET_CLOSEST_OBJECT_OF_TYPE` · hash `0xE143FA2249364369` · jhash `0x45619B33` · **Cliente**

```lua
local retval = GetClosestObjectOfType(x, y, z, radius, modelHash, isMission, p6, p7)
```
```c
Object GET_CLOSEST_OBJECT_OF_TYPE(float x, float y, float z, float radius, Hash modelHash, BOOL isMission, BOOL p6, BOOL p7);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `isMission` (`BOOL`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `Object`

**Descripción oficial:**

```
Has 8 params in the latest patches.  
isMission - if true doesn't return mission objects  
```

---
### GetCoordsAndRotationOfClosestObjectOfType

`GET_COORDS_AND_ROTATION_OF_CLOSEST_OBJECT_OF_TYPE` · hash `0x163F8B586BC95F2A` · jhash `0x65213FC3` · **Cliente**

```lua
local retval, outPosition, outRotation = GetCoordsAndRotationOfClosestObjectOfType(x, y, z, radius, modelHash, rotationOrder)
```
```c
Any GET_COORDS_AND_ROTATION_OF_CLOSEST_OBJECT_OF_TYPE(float x, float y, float z, float radius, Hash modelHash, Vector3* outPosition, Vector3* outRotation, int rotationOrder);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `outRotation` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rotationOrder` (`int`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x163F8B586BC95F2A` (`N_0x163f8b586bc95f2a`)

---
### GetIsArenaPropPhysicsDisabled

`_GET_IS_ARENA_PROP_PHYSICS_DISABLED` · hash `0x43C677F1E1158005` · **Cliente**

```lua
local retval = GetIsArenaPropPhysicsDisabled(entity, p1)
```
```c
BOOL _GET_IS_ARENA_PROP_PHYSICS_DISABLED(Object entity, Any p1);
```

**Parámetros**

- `entity` (`Object`)
- `p1` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

**Nombres antiguos (alias):** `0x43C677F1E1158005` (`N_0x43c677f1e1158005`)

---
### GetObjectFragmentDamageHealth

`GET_OBJECT_FRAGMENT_DAMAGE_HEALTH` · hash `0xB6FBFD079B8D0596` · jhash `0xF0B330AD` · **Cliente**

```lua
local retval = GetObjectFragmentDamageHealth(p0, p1)
```
```c
float GET_OBJECT_FRAGMENT_DAMAGE_HEALTH(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `float`

---
### GetObjectTextureVariation

`_GET_OBJECT_TEXTURE_VARIATION` · hash `0xE84EB93729C5F36A` · **Cliente**

```lua
local retval = GetObjectTextureVariation(object)
```
```c
int _GET_OBJECT_TEXTURE_VARIATION(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xE84EB93729C5F36A` (`N_0xe84eb93729c5f36a`)

---
### GetOffsetFromCoordAndHeadingInWorldCoords

`GET_OFFSET_FROM_COORD_AND_HEADING_IN_WORLD_COORDS` · hash `0x163E252DE035A133` · jhash `0x87A42A12` · **Cliente**

```lua
local retval = GetOffsetFromCoordAndHeadingInWorldCoords(xPos, yPos, zPos, heading, xOffset, yOffset, zOffset)
```
```c
Vector3 GET_OFFSET_FROM_COORD_AND_HEADING_IN_WORLD_COORDS(float xPos, float yPos, float zPos, float heading, float xOffset, float yOffset, float zOffset);
```

**Parámetros**

- `xPos` (`float`): The X coordinate of the original position.
- `yPos` (`float`): The Y coordinate of the original position.
- `zPos` (`float`): The Z coordinate of the original position.
- `heading` (`float`): The heading (in degrees) relative to which the offsets are applied.
- `xOffset` (`float`): Left/right offset from the coord.
- `yOffset` (`float`): Forward/backward offset from the coord.
- `zOffset` (`float`): Upward/downward offset from the coord.

**Devuelve:** `Vector3` — Returns a Vector3 representing the new world coordinates after applying the offsets to the original position relative to the specified heading.

**Descripción oficial:**

Calculates the world coordinates after applying the specified offsets to the given position, relative to a certain heading.
This native is similar to [`GET_OFFSET_FROM_ENTITY_IN_WORLD_COORDS`](ENTITY.md#getoffsetfromentityinworldcoords), but uses a world position and heading as the reference point.

**Nombres antiguos (alias):** `0x163E252DE035A133` (`N_0x163e252de035a133`), `_GET_OBJECT_OFFSET_FROM_COORDS` (`GetObjectOffsetFromCoords`)

---
### GetPickupCoords

`GET_PICKUP_COORDS` · hash `0x225B8B35C88029B3` · jhash `0xC2E1E2C5` · **Cliente**

```lua
local retval = GetPickupCoords(pickup)
```
```c
Vector3 GET_PICKUP_COORDS(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `Vector3`

---
### GetPickupGenerationRangeMultiplier

`_GET_PICKUP_GENERATION_RANGE_MULTIPLIER` · hash `0xB3ECA65C7317F174` · **Cliente**

```lua
local retval = GetPickupGenerationRangeMultiplier()
```
```c
float _GET_PICKUP_GENERATION_RANGE_MULTIPLIER();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xB3ECA65C7317F174` (`N_0xb3eca65c7317f174`)

---
### GetPickupHash

`_GET_PICKUP_HASH` · hash `0x5EAAD83F8CFB4575` · jhash `0x6AE36192` · **Cliente**

```lua
local retval = GetPickupHash(pickupHash)
```
```c
Hash _GET_PICKUP_HASH(Hash pickupHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

**Descripción oficial:**

```
returns pickup hash.
```

**Nombres antiguos (alias):** `0x5EAAD83F8CFB4575` (`N_0x5eaad83f8cfb4575`)

---
### GetPickupHashFromWeapon

`_GET_PICKUP_HASH_FROM_WEAPON` · hash `0xD6429A016084F1A5` · **Cliente**

```lua
local retval = GetPickupHashFromWeapon(weapon)
```
```c
Hash _GET_PICKUP_HASH_FROM_WEAPON(Hash weapon);
```

**Parámetros**

- `weapon` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash` — Returns the pickup hash for the given weapon hash

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0xD6429A016084F1A5` (`N_0xd6429a016084f1a5`)

---
### GetPickupObject

`GET_PICKUP_OBJECT` · hash `0x5099BC55630B25AE` · jhash `0x6052E62E` · **Cliente**

```lua
local retval = GetPickupObject(pickup)
```
```c
Object GET_PICKUP_OBJECT(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `Object`

**Nombres antiguos (alias):** `0x5099BC55630B25AE` (`N_0x5099bc55630b25ae`)

---
### GetRayfireMapObject

`GET_RAYFIRE_MAP_OBJECT` · hash `0xB48FCED898292E52` · jhash `0xA286DE96` · **Cliente**

```lua
local retval = GetRayfireMapObject(x, y, z, radius, name)
```
```c
Object GET_RAYFIRE_MAP_OBJECT(float x, float y, float z, float radius, char* name);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `name` (`char*`)

**Devuelve:** `Object`

**Descripción oficial:**

```
Example:
OBJECT::GET_RAYFIRE_MAP_OBJECT(-809.9619750976562, 170.919, 75.7406997680664, 3.0, "des_tvsmash");
```

**Nombres antiguos (alias):** `0xB48FCED898292E52` (`N_0xb48fced898292e52`), `_GET_DES_OBJECT` (`GetDesObject`)

---
### GetRayfireMapObjectAnimPhase

`GET_RAYFIRE_MAP_OBJECT_ANIM_PHASE` · hash `0x260EE4FDBDF4DB01` · jhash `0x020497DE` · **Cliente**

```lua
local retval = GetRayfireMapObjectAnimPhase(object)
```
```c
float GET_RAYFIRE_MAP_OBJECT_ANIM_PHASE(Object object);
```

**Parámetros**

- `object` (`Object`): The des-object handle to get the animation progress from.

**Devuelve:** `float` — A float between 0.0 and 1.0, 0.0 is the beginning of the animation, 1.0 is the end. Value resets to 0.0 instantly after reaching 1.0.

**Descripción oficial:**

```
`object`: The des-object handle to get the animation progress from.
Return value is a float between 0.0 and 1.0, 0.0 is the beginning of the animation, 1.0 is the end. Value resets to 0.0 instantly after reaching 1.0.
```

**Nombres antiguos (alias):** `0x260EE4FDBDF4DB01` (`N_0x260ee4fdbdf4db01`), `_GET_DES_OBJECT_ANIM_PROGRESS` (`GetDesObjectAnimProgress`)

**Ejemplo (lua):**

```lua
local handle = GetRayfireMapObject(7.25, -656.98, 17.14, 50.0, "des_finale_tunnel")
local handle2 = GetRayfireMapObject(7.25, -656.98, 17.14, 50.0, "des_finale_vault")

SetStateOfRayfireMapObject(handle, 4) -- set to pre-start state
SetStateOfRayfireMapObject(handle2, 4) -- set to pre-start state

Citizen.Wait(100)

SetStateOfRayfireMapObject(handle, 6) -- set to start animation state.
SetStateOfRayfireMapObject(handle2, 6) -- set to start animation state.

Citizen.CreateThread(function()
    Citizen.Wait(10)
    while GetRayfireMapObjectAnimPhase(handle) > 0.0 do
        Citizen.Wait(0)
    end
    print("Animation 1 is done!")
    while GetRayfireMapObjectAnimPhase(handle2) > 0.0 do
        Citizen.Wait(0)
    end
    print("Animation 2 is done!")
end)
```

---
### GetSafePickupCoords

`GET_SAFE_PICKUP_COORDS` · hash `0x6E16BC2503FF1FF0` · jhash `0x618B5F67` · **Cliente**

```lua
local retval = GetSafePickupCoords(x, y, z, p3, p4)
```
```c
Vector3 GET_SAFE_PICKUP_COORDS(float x, float y, float z, float p3, float p4);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `Vector3`

---
### GetStateOfClosestDoorOfType

`GET_STATE_OF_CLOSEST_DOOR_OF_TYPE` · hash `0xEDC1A5B84AEF33FF` · jhash `0x4B44A83D` · **Cliente**

```lua
local locked, heading = GetStateOfClosestDoorOfType(type, x, y, z)
```
```c
void GET_STATE_OF_CLOSEST_DOOR_OF_TYPE(Hash type, float x, float y, float z, BOOL* locked, float* heading);
```

**Parámetros**

- `type` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `locked` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `heading` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
locked is 0 if no door is found  
locked is 0 if door is unlocked  
locked is 1 if door is found and unlocked.  
-------------  
the locked bool is either 0(unlocked)(false) or 1(locked)(true)  
```

---
### GetStateOfRayfireMapObject

`GET_STATE_OF_RAYFIRE_MAP_OBJECT` · hash `0x899BA936634A322E` · jhash `0xF1B8817A` · **Cliente**

```lua
local retval = GetStateOfRayfireMapObject(object)
```
```c
int GET_STATE_OF_RAYFIRE_MAP_OBJECT(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `int`

**Descripción oficial:**

See [`SET_STATE_OF_RAYFIRE_MAP_OBJECT`](#setstateofrayfiremapobject) to see the different states

Get a destructible object's state. Substract 1 to get the real state. For example, if the object just spawned (state 2), the native will return 3.

**Nombres antiguos (alias):** `0x899BA936634A322E` (`N_0x899ba936634a322e`), `_GET_DES_OBJECT_STATE` (`GetDesObjectState`)

---
### GetWeaponTypeFromPickupType

`GET_WEAPON_TYPE_FROM_PICKUP_TYPE` · hash `0x08F96CA6C551AD51` · jhash `0xEDD01937` · **Cliente**

```lua
local retval = GetWeaponTypeFromPickupType(pickupHash)
```
```c
Hash GET_WEAPON_TYPE_FROM_PICKUP_TYPE(Hash pickupHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0x08F96CA6C551AD51` (`N_0x08f96ca6c551ad51`), `_GET_WEAPON_HASH_FROM_PICKUP` (`GetWeaponHashFromPickup`)

---
### HasClosestObjectOfTypeBeenBroken

`HAS_CLOSEST_OBJECT_OF_TYPE_BEEN_BROKEN` · hash `0x761B0E69AC4D007E` · jhash `0x6FC0353D` · **Cliente**

```lua
local retval = HasClosestObjectOfTypeBeenBroken(p0, p1, p2, p3, modelHash, p5)
```
```c
BOOL HAS_CLOSEST_OBJECT_OF_TYPE_BEEN_BROKEN(float p0, float p1, float p2, float p3, Hash modelHash, Any p5);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p5` (`Any`)

**Devuelve:** `BOOL`

---
### HasClosestObjectOfTypeBeenCompletelyDestroyed

`HAS_CLOSEST_OBJECT_OF_TYPE_BEEN_COMPLETELY_DESTROYED` · hash `0x46494A2475701343` · jhash `0x7DB578DD` · **Cliente**

```lua
local retval = HasClosestObjectOfTypeBeenCompletelyDestroyed(x, y, z, radius, modelHash, p5)
```
```c
BOOL HAS_CLOSEST_OBJECT_OF_TYPE_BEEN_COMPLETELY_DESTROYED(float x, float y, float z, float radius, Hash modelHash, BOOL p5);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p5` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x46494A2475701343` (`N_0x46494a2475701343`)

---
### HasObjectBeenBroken

`HAS_OBJECT_BEEN_BROKEN` · hash `0x8ABFB70C49CC43E2` · jhash `0xFE21F891` · **Cliente**

```lua
local retval = HasObjectBeenBroken(object)
```
```c
BOOL HAS_OBJECT_BEEN_BROKEN(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### HasPickupBeenCollected

`HAS_PICKUP_BEEN_COLLECTED` · hash `0x80EC48E6679313F9` · jhash `0x0BE5CCED` · **Cliente**

```lua
local retval = HasPickupBeenCollected(pickup)
```
```c
BOOL HAS_PICKUP_BEEN_COLLECTED(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `BOOL`

---
### HidePortablePickupWhenDetached

`HIDE_PORTABLE_PICKUP_WHEN_DETACHED` · hash `0x867458251D47CCB2` · jhash `0x1F63B042` · **Cliente**

```lua
HidePortablePickupWhenDetached(pickup, toggle)
```
```c
void HIDE_PORTABLE_PICKUP_WHEN_DETACHED(Pickup pickup, BOOL toggle);
```

**Parámetros**

- `pickup` (`Pickup`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x867458251D47CCB2` (`N_0x867458251d47ccb2`), `_HIDE_PICKUP` (`HidePickup`)

---
### IsAnyEntityEntirelyInsideGarage

`IS_ANY_ENTITY_ENTIRELY_INSIDE_GARAGE` · hash `0x673ED815D6E323B7` · jhash `0x7B44D659` · **Cliente**

```lua
local retval = IsAnyEntityEntirelyInsideGarage(garageHash, p1, p2, p3, p4)
```
```c
BOOL IS_ANY_ENTITY_ENTIRELY_INSIDE_GARAGE(Hash garageHash, BOOL p1, BOOL p2, BOOL p3, Any p4);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)
- `p4` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x673ED815D6E323B7` (`N_0x673ed815d6e323b7`)

---
### IsAnyObjectNearPoint

`IS_ANY_OBJECT_NEAR_POINT` · hash `0x397DC58FF00298D1` · jhash `0xE9E46941` · **Cliente**

```lua
local retval = IsAnyObjectNearPoint(x, y, z, range, p4)
```
```c
BOOL IS_ANY_OBJECT_NEAR_POINT(float x, float y, float z, float range, BOOL p4);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `range` (`float`)
- `p4` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsDoorClosed

`IS_DOOR_CLOSED` · hash `0xC531EE8A1145A149` · jhash `0x48659CD7` · **Cliente**

```lua
local retval = IsDoorClosed(doorHash)
```
```c
BOOL IS_DOOR_CLOSED(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsDoorRegisteredWithSystem

`IS_DOOR_REGISTERED_WITH_SYSTEM` · hash `0xC153C43EA202C8C1` · jhash `0x5AFCD8A1` · **Cliente**

```lua
local retval = IsDoorRegisteredWithSystem(doorHash)
```
```c
BOOL IS_DOOR_REGISTERED_WITH_SYSTEM(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
if (OBJECT::IS_DOOR_REGISTERED_WITH_SYSTEM(doorHash))
{
    OBJECT::REMOVE_DOOR_FROM_SYSTEM(doorHash);
}
```

**Nombres antiguos (alias):** `0xC153C43EA202C8C1` (`N_0xc153c43ea202c8c1`), `_DOES_DOOR_EXIST` (`DoesDoorExist`)

---
### IsGarageEmpty

`IS_GARAGE_EMPTY` · hash `0x90E47239EA1980B8` · jhash `0xA8B37DEA` · **Cliente**

```lua
local retval = IsGarageEmpty(garageHash, p1, p2)
```
```c
BOOL IS_GARAGE_EMPTY(Hash garageHash, BOOL p1, int p2);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`BOOL`)
- `p2` (`int`)

**Devuelve:** `BOOL`

---
### IsObjectAPickup

`IS_OBJECT_A_PICKUP` · hash `0xFC481C641EBBD27D` · jhash `0x93D23399` · **Cliente**

```lua
local retval = IsObjectAPickup(object)
```
```c
BOOL IS_OBJECT_A_PICKUP(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFC481C641EBBD27D` (`N_0xfc481c641ebbd27d`)

---
### IsObjectAPortablePickup

`IS_OBJECT_A_PORTABLE_PICKUP` · hash `0x0378C08504160D0D` · jhash `0x0F0E94FF` · **Cliente**

```lua
local retval = IsObjectAPortablePickup(object)
```
```c
BOOL IS_OBJECT_A_PORTABLE_PICKUP(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

**Nombres antiguos (alias):** `0x0378C08504160D0D` (`N_0x0378c08504160d0d`)

---
### IsObjectEntirelyInsideGarage

`IS_OBJECT_ENTIRELY_INSIDE_GARAGE` · hash `0x372EF6699146A1E4` · jhash `0x142C8F76` · **Cliente**

```lua
local retval = IsObjectEntirelyInsideGarage(garageHash, entity, p2, p3)
```
```c
BOOL IS_OBJECT_ENTIRELY_INSIDE_GARAGE(Hash garageHash, Entity entity, float p2, int p3);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `entity` (`Entity`)
- `p2` (`float`)
- `p3` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x372EF6699146A1E4` (`N_0x372ef6699146a1e4`)

---
### IsObjectNearPoint

`IS_OBJECT_NEAR_POINT` · hash `0x8C90FE4B381BA60A` · jhash `0x50A62C43` · **Cliente**

```lua
local retval = IsObjectNearPoint(objectHash, x, y, z, range)
```
```c
BOOL IS_OBJECT_NEAR_POINT(Hash objectHash, float x, float y, float z, float range);
```

**Parámetros**

- `objectHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `range` (`float`)

**Devuelve:** `BOOL`

---
### IsObjectPartiallyInsideGarage

`IS_OBJECT_PARTIALLY_INSIDE_GARAGE` · hash `0xF0EED5A6BC7B237A` · jhash `0x95A9AB2B` · **Cliente**

```lua
local retval = IsObjectPartiallyInsideGarage(garageHash, entity, p2)
```
```c
BOOL IS_OBJECT_PARTIALLY_INSIDE_GARAGE(Hash garageHash, Entity entity, int p2);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `entity` (`Entity`)
- `p2` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF0EED5A6BC7B237A` (`N_0xf0eed5a6bc7b237a`)

---
### IsObjectVisible

`IS_OBJECT_VISIBLE` · hash `0x8B32ACE6326A7546` · jhash `0xF4FD8AE4` · **Cliente**

```lua
local retval = IsObjectVisible(object)
```
```c
BOOL IS_OBJECT_VISIBLE(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

---
### IsPickupWeaponObjectValid

`IS_PICKUP_WEAPON_OBJECT_VALID` · hash `0x11D1E53A726891FE` · jhash `0x883DAB2D` · **Cliente**

```lua
local retval = IsPickupWeaponObjectValid(object)
```
```c
BOOL IS_PICKUP_WEAPON_OBJECT_VALID(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x11D1E53A726891FE` (`N_0x11d1e53a726891fe`)

---
### IsPlayerEntirelyInsideGarage

`IS_PLAYER_ENTIRELY_INSIDE_GARAGE` · hash `0x024A60DEB0EA69F0` · jhash `0xC33ED360` · **Cliente**

```lua
local retval = IsPlayerEntirelyInsideGarage(garageHash, player, p2, p3)
```
```c
BOOL IS_PLAYER_ENTIRELY_INSIDE_GARAGE(Hash garageHash, Player player, float p2, int p3);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `player` (`Player`)
- `p2` (`float`)
- `p3` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x024A60DEB0EA69F0` (`N_0x024a60deb0ea69f0`)

---
### IsPlayerPartiallyInsideGarage

`IS_PLAYER_PARTIALLY_INSIDE_GARAGE` · hash `0x1761DC5D8471CBAA` · jhash `0x41924877` · **Cliente**

```lua
local retval = IsPlayerPartiallyInsideGarage(garageHash, player, p2)
```
```c
BOOL IS_PLAYER_PARTIALLY_INSIDE_GARAGE(Hash garageHash, Player player, int p2);
```

**Parámetros**

- `garageHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `player` (`Player`)
- `p2` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1761DC5D8471CBAA` (`N_0x1761dc5d8471cbaa`)

---
### IsPointInAngledArea

`IS_POINT_IN_ANGLED_AREA` · hash `0x2A70BAE8883E4C81` · jhash `0x73BCFFDC` · **Cliente**

```lua
local retval = IsPointInAngledArea(xPos, yPos, zPos, x1, y1, z1, x2, y2, z2, width, p10, includez)
```
```c
BOOL IS_POINT_IN_ANGLED_AREA(float xPos, float yPos, float zPos, float x1, float y1, float z1, float x2, float y2, float z2, float width, BOOL p10, BOOL includez);
```

**Parámetros**

- `xPos` (`float`): The x coordinate.
- `yPos` (`float`): The y coordinate.
- `zPos` (`float`): The z coordinate.
- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area
- `p10` (`BOOL`): a debug flag invoking functions in the same path as `DRAW_MARKER`
- `includez` (`BOOL`): If true, include the Z dimension when doing the height check; otherwise the query becomes two-dimensional

**Devuelve:** `BOOL`

**Descripción oficial:**

An **angled area** is an X-Z oriented rectangle with three parameters:

1.  **origin**: the mid-point along a base edge of the rectangle;
2.  **extent**: the mid-point of opposite base edge on the other Z;
3.  **width**: the length of the base edge; (named derived from logging strings `CNetworkRoadNodeWorldStateData`).

The oriented rectangle can then be derived from the direction of the two points (`norm(origin - extent)`), its orthonormal, and the width, e.g:

1.  ![golf_mp](https://i.imgur.com/WoIozPt.png)
2.  ![am_taxi](https://i.imgur.com/lipbffH.png)

---
### MarkObjectForDeletion

`_MARK_OBJECT_FOR_DELETION` · hash `0xADBE4809F19F927A` · jhash `0x2048A7DD` · **Cliente**

```lua
MarkObjectForDeletion(object)
```
```c
void _MARK_OBJECT_FOR_DELETION(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `void`

**Descripción oficial:**

```
is this like setting is as no longer needed?  
```

---
### N_0x006e4b040ed37ec3

`0x006E4B040ED37EC3` · hash `0x006E4B040ED37EC3` · **Cliente**

```lua
N_0x006e4b040ed37ec3(p0)
```
```c
void 0x006E4B040ED37EC3(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x0596843b34b95ce5

`0x0596843B34B95CE5` · hash `0x0596843B34B95CE5` · **Cliente**

```lua
N_0x0596843b34b95ce5(p0, p1)
```
```c
void 0x0596843B34B95CE5(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x1a6cbb06e2d0d79d

`0x1A6CBB06E2D0D79D` · hash `0x1A6CBB06E2D0D79D` · **Cliente**

```lua
N_0x1a6cbb06e2d0d79d(p0, p1)
```
```c
void 0x1A6CBB06E2D0D79D(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x1c57c94a6446492a

`0x1C57C94A6446492A` · hash `0x1C57C94A6446492A` · **Cliente**

```lua
N_0x1c57c94a6446492a(p0, p1)
```
```c
void 0x1C57C94A6446492A(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x1e3f1b1b891a2aaa

`0x1E3F1B1B891A2AAA` · hash `0x1E3F1B1B891A2AAA` · **Cliente**

```lua
N_0x1e3f1b1b891a2aaa(p0, p1)
```
```c
void 0x1E3F1B1B891A2AAA(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x2542269291c6ac84

`0x2542269291C6AC84` · hash `0x2542269291C6AC84` · **Cliente**

```lua
local retval = N_0x2542269291c6ac84(p0)
```
```c
Any 0x2542269291C6AC84(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x27f248c3febfaad3

`0x27F248C3FEBFAAD3` · hash `0x27F248C3FEBFAAD3` · **Cliente**

```lua
N_0x27f248c3febfaad3(p0, p1)
```
```c
void 0x27F248C3FEBFAAD3(Any p0, Any p1);
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
### N_0x31574b1b41268673

`0x31574B1B41268673` · hash `0x31574B1B41268673` · **Cliente**

```lua
N_0x31574b1b41268673(p0, p1)
```
```c
void 0x31574B1B41268673(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x31f924b53eaddf65

`0x31F924B53EADDF65` · hash `0x31F924B53EADDF65` · jhash `0xDB18FA01` · **Cliente**

```lua
N_0x31f924b53eaddf65(p0)
```
```c
void 0x31F924B53EADDF65(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x394cd08e31313c28

`0x394CD08E31313C28` · hash `0x394CD08E31313C28` · **Cliente**

```lua
N_0x394cd08e31313c28()
```
```c
void 0x394CD08E31313C28();
```

**Devuelve:** `void`

---
### N_0x39a5fb7eaf150840

`0x39A5FB7EAF150840` · hash `0x39A5FB7EAF150840` · **Cliente**

```lua
N_0x39a5fb7eaf150840(p0, p1)
```
```c
void 0x39A5FB7EAF150840(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x3b2fd68db5f8331c

`0x3B2FD68DB5F8331C` · hash `0x3B2FD68DB5F8331C` · **Cliente**

```lua
N_0x3b2fd68db5f8331c(object, toggle, R, G, B)
```
```c
void 0x3B2FD68DB5F8331C(Object object, BOOL toggle, int R, int G, int B);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)
- `R` (`int`)
- `G` (`int`)
- `B` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Removed Parameter 3: int R
NativeDB Removed Parameter 4: int G
NativeDB Removed Parameter 5: int B
NativeDB Introduced: v757
```

**Nombres antiguos (alias):** `_SET_OBJECT_COLOUR` (`SetObjectColour`)

---
### N_0x3bd770d281982db5

`0x3BD770D281982DB5` · hash `0x3BD770D281982DB5` · **Cliente**

```lua
local retval = N_0x3bd770d281982db5(p0, p1)
```
```c
Any 0x3BD770D281982DB5(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x46f3add1e2d5baf2

`0x46F3ADD1E2D5BAF2` · hash `0x46F3ADD1E2D5BAF2` · **Cliente**

```lua
N_0x46f3add1e2d5baf2(p0, p1)
```
```c
void 0x46F3ADD1E2D5BAF2(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x4c134b4df76025d0

`0x4C134B4DF76025D0` · hash `0x4C134B4DF76025D0` · **Cliente**

```lua
N_0x4c134b4df76025d0(p0, p1)
```
```c
void 0x4C134B4DF76025D0(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x62454a641b41f3c5

`0x62454A641B41F3C5` · hash `0x62454A641B41F3C5` · **Cliente**

```lua
N_0x62454a641b41f3c5(p0)
```
```c
void 0x62454A641B41F3C5(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x63ecf581bc70e363

`0x63ECF581BC70E363` · hash `0x63ECF581BC70E363` · **Cliente**

```lua
N_0x63ecf581bc70e363(p0, p1)
```
```c
void 0x63ECF581BC70E363(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

---
### N_0x641f272b52e2f0f8

`0x641F272B52E2F0F8` · hash `0x641F272B52E2F0F8` · **Cliente**

```lua
N_0x641f272b52e2f0f8(p0, p1)
```
```c
void 0x641F272B52E2F0F8(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x659f9d71f52843f8

`0x659F9D71F52843F8` · hash `0x659F9D71F52843F8` · **Cliente**

```lua
N_0x659f9d71f52843f8(p0, p1)
```
```c
void 0x659F9D71F52843F8(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x66a49d021870fe88

`0x66A49D021870FE88` · hash `0x66A49D021870FE88` · jhash `0x6158959E` · **Cliente**

```lua
N_0x66a49d021870fe88()
```
```c
void 0x66A49D021870FE88();
```

**Devuelve:** `void`

---
### N_0x701fda1e82076ba4

`0x701FDA1E82076BA4` · hash `0x701FDA1E82076BA4` · jhash `0xF592AD10` · **Cliente**

```lua
N_0x701fda1e82076ba4()
```
```c
void 0x701FDA1E82076BA4();
```

**Devuelve:** `void`

**Descripción oficial:**

Clears the fields sets by [N\_0xc7f29ca00f46350e](#n_0xc7f29ca00f46350e) (1604 retail: 0x1424A7A10, 0x1424A7A11) and iterates over the global CDoor's bucket-list.

Related to its "Pre-networked state"?

---
### N_0x734e1714d077da9a

`0x734E1714D077DA9A` · hash `0x734E1714D077DA9A` · **Cliente**

```lua
N_0x734e1714d077da9a(p0, p1)
```
```c
void 0x734E1714D077DA9A(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x762db2d380b48d04

`0x762DB2D380B48D04` · hash `0x762DB2D380B48D04` · jhash `0xD1BAAFB7` · **Cliente**

```lua
N_0x762db2d380b48d04(p0)
```
```c
void 0x762DB2D380B48D04(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x7813e8b8c4ae4799

`0x7813E8B8C4AE4799` · hash `0x7813E8B8C4AE4799` · **Cliente**

```lua
N_0x7813e8b8c4ae4799(pickup)
```
```c
void 0x7813E8B8C4AE4799(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `void`

**Descripción oficial:**

SET_PICKUP_\*

```
NativeDB Introduced: v1734
```

---
### N_0x826d1ee4d1cafc78

`0x826D1EE4D1CAFC78` · hash `0x826D1EE4D1CAFC78` · **Cliente**

```lua
N_0x826d1ee4d1cafc78(p0, p1)
```
```c
void 0x826D1EE4D1CAFC78(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x834344a414c7c85d

`0x834344A414C7C85D` · hash `0x834344A414C7C85D` · **Cliente**

```lua
N_0x834344a414c7c85d(p0, p1)
```
```c
void 0x834344A414C7C85D(Any p0, Any p1);
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
### N_0x858ec9fd25de04aa

`0x858EC9FD25DE04AA` · hash `0x858EC9FD25DE04AA` · **Cliente**

```lua
N_0x858ec9fd25de04aa(p0, p1)
```
```c
void 0x858EC9FD25DE04AA(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x8881c98a31117998

`0x8881C98A31117998` · hash `0x8881C98A31117998` · **Cliente**

```lua
N_0x8881c98a31117998(p0)
```
```c
void 0x8881C98A31117998(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0xA90E7227A9303FA9` (`N_0xa90e7227a9303fa9`)

---
### N_0x8caab2bd3ea58bd4

`0x8CAAB2BD3EA58BD4` · hash `0x8CAAB2BD3EA58BD4` · **Cliente**

```lua
N_0x8caab2bd3ea58bd4(p0)
```
```c
void 0x8CAAB2BD3EA58BD4(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x8cff648fbd7330f1

`0x8CFF648FBD7330F1` · hash `0x8CFF648FBD7330F1` · **Cliente**

```lua
N_0x8cff648fbd7330f1(p0)
```
```c
void 0x8CFF648FBD7330F1(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v757
```

---
### N_0x8dca505a5c196f05

`0x8DCA505A5C196F05` · hash `0x8DCA505A5C196F05` · **Cliente**

```lua
N_0x8dca505a5c196f05(p0, p1)
```
```c
void 0x8DCA505A5C196F05(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0xa08fe5e49bdc39dd

`0xA08FE5E49BDC39DD` · hash `0xA08FE5E49BDC39DD` · jhash `0x276A7807` · **Cliente**

```lua
N_0xa08fe5e49bdc39dd(p0, p1, p2)
```
```c
void 0xA08FE5E49BDC39DD(Any p0, float p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### N_0xa2c1f5e92afe49ed

`0xA2C1F5E92AFE49ED` · hash `0xA2C1F5E92AFE49ED` · jhash `0xB241806C` · **Cliente**

```lua
N_0xa2c1f5e92afe49ed()
```
```c
void 0xA2C1F5E92AFE49ED();
```

**Devuelve:** `void`

**Descripción oficial:**

```
CLEAR_*
```

---
### N_0xa85a21582451e951

`0xA85A21582451E951` · hash `0xA85A21582451E951` · jhash `0xF736227C` · **Cliente**

```lua
N_0xa85a21582451e951(doorHash, p1)
```
```c
void 0xA85A21582451E951(Hash doorHash, BOOL p1);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Some property related to gates. Native name between `DOOR_SYSTEM_SET_AUTOMATIC_RATE` and `DOOR_SYSTEM_SET_DOOR_STATE`.

---
### N_0xaa059c615de9dd03

`0xAA059C615DE9DD03` · hash `0xAA059C615DE9DD03` · **Cliente**

```lua
N_0xaa059c615de9dd03(p0, p1)
```
```c
void 0xAA059C615DE9DD03(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0xadf084fb8f075d06

`0xADF084FB8F075D06` · hash `0xADF084FB8F075D06` · **Cliente**

```lua
local retval = N_0xadf084fb8f075d06(p0)
```
```c
BOOL 0xADF084FB8F075D06(Object p0);
```

**Parámetros**

- `p0` (`Object`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0xafe24e4d29249e4a

`0xAFE24E4D29249E4A` · hash `0xAFE24E4D29249E4A` · **Cliente**

```lua
local retval = N_0xafe24e4d29249e4a(object, p1, p2, p3)
```
```c
BOOL 0xAFE24E4D29249E4A(Object object, float p1, float p2, BOOL p3);
```

**Parámetros**

- `object` (`Object`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### N_0xb2d0bde54f0e8e5a

`0xB2D0BDE54F0E8E5A` · hash `0xB2D0BDE54F0E8E5A` · jhash `0x132B6D92` · **Cliente**

```lua
N_0xb2d0bde54f0e8e5a(object, toggle)
```
```c
void 0xB2D0BDE54F0E8E5A(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0xb5b7742424bd4445

`0xB5B7742424BD4445` · hash `0xB5B7742424BD4445` · **Cliente**

```lua
N_0xb5b7742424bd4445(p0, p1)
```
```c
void 0xB5B7742424BD4445(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0xb7c6d80fb371659a

`0xB7C6D80FB371659A` · hash `0xB7C6D80FB371659A` · **Cliente**

```lua
N_0xb7c6d80fb371659a()
```
```c
void 0xB7C6D80FB371659A();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Clears all areas created by 0xD4A7A435B3710D05

CLEAR_*

NativeDB Introduced: v1290
```

---
### N_0xbffe53ae7e67fcdc

`0xBFFE53AE7E67FCDC` · hash `0xBFFE53AE7E67FCDC` · **Cliente**

```lua
N_0xbffe53ae7e67fcdc(p0, p1)
```
```c
void 0xBFFE53AE7E67FCDC(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xc6033d32241f6fb5

`0xC6033D32241F6FB5` · hash `0xC6033D32241F6FB5` · jhash `0xF4A1A14A` · **Cliente**

```lua
N_0xc6033d32241f6fb5(object, toggle)
```
```c
void 0xC6033D32241F6FB5(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0xc7f29ca00f46350e

`0xC7F29CA00F46350E` · hash `0xC7F29CA00F46350E` · jhash `0x9BF33E41` · **Cliente**

```lua
N_0xc7f29ca00f46350e(p0)
```
```c
void 0xC7F29CA00F46350E(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

See [`N_0x701fda1e82076ba4`](#n_0x701fda1e82076ba4).

---
### N_0xd05a3241b9a86f19

`0xD05A3241B9A86F19` · hash `0xD05A3241B9A86F19` · **Cliente**

```lua
N_0xd05a3241b9a86f19(p0, p1)
```
```c
void 0xD05A3241B9A86F19(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0xd4a7a435b3710d05

`0xD4A7A435B3710D05` · hash `0xD4A7A435B3710D05` · **Cliente**

```lua
N_0xd4a7a435b3710d05(x, y, z, radius)
```
```c
void 0xD4A7A435B3710D05(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Adds an area that seems to be related to pickup physics behavior.
Max amount of areas is 10. Only works in multiplayer.

ADD_*

NativeDB Introduced: v1290
```

---
### N_0xdb41d07a45a6d4b7

`0xDB41D07A45A6D4B7` · hash `0xDB41D07A45A6D4B7` · jhash `0x000E92DC` · **Cliente**

```lua
local retval = N_0xdb41d07a45a6d4b7(p0)
```
```c
Any 0xDB41D07A45A6D4B7(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0xe05f6aeefeb0bb02

`0xE05F6AEEFEB0BB02` · hash `0xE05F6AEEFEB0BB02` · **Cliente**

```lua
N_0xe05f6aeefeb0bb02(p0, p1, p2)
```
```c
void 0xE05F6AEEFEB0BB02(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0xeb6f1a9b5510a5d2

`0xEB6F1A9B5510A5D2` · hash `0xEB6F1A9B5510A5D2` · jhash `0xAF016CC1` · **Cliente**

```lua
N_0xeb6f1a9b5510a5d2(p0, p1)
```
```c
void 0xEB6F1A9B5510A5D2(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xf92099527db8e2a7

`0xF92099527DB8E2A7` · hash `0xF92099527DB8E2A7` · jhash `0xA7E936FD` · **Cliente**

```lua
N_0xf92099527db8e2a7(p0, p1)
```
```c
void 0xF92099527DB8E2A7(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xfdc07c58e8aab715

`0xFDC07C58E8AAB715` · hash `0xFDC07C58E8AAB715` · **Cliente**

```lua
N_0xfdc07c58e8aab715(pickupHash)
```
```c
void 0xFDC07C58E8AAB715(Hash pickupHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

A\*

```
NativeDB Introduced: v1734
```

---
### PlaceObjectOnGroundOrObjectProperly

`PLACE_OBJECT_ON_GROUND_OR_OBJECT_PROPERLY` · hash `0xD76EEEF746057FD6` · **Cliente**

```lua
local retval = PlaceObjectOnGroundOrObjectProperly(object)
```
```c
BOOL PLACE_OBJECT_ON_GROUND_OR_OBJECT_PROPERLY(Object object);
```

**Parámetros**

- `object` (`Object`): The object handle.

**Devuelve:** `BOOL`

**Descripción oficial:**

Casts a ray downward from the object's position and places the object on the surface it hits (including world surface and objects). Use [`PLACE_OBJECT_ON_GROUND_PROPERLY`](#placeobjectongroundproperly) to not include objects when determining the surface.

**Nombres antiguos (alias):** `0xD76EEEF746057FD6` (`N_0xd76eeef746057fd6`), `_PLACE_OBJECT_ON_GROUND_PROPERLY_2` (`PlaceObjectOnGroundProperly_2`)

---
### PlaceObjectOnGroundProperly

`PLACE_OBJECT_ON_GROUND_PROPERLY` · hash `0x58A850EAEE20FAA3` · jhash `0x8F95A20B` · **Cliente**

```lua
local retval = PlaceObjectOnGroundProperly(object)
```
```c
BOOL PLACE_OBJECT_ON_GROUND_PROPERLY(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `BOOL`

---
### PreventCollectionOfPortablePickup

`PREVENT_COLLECTION_OF_PORTABLE_PICKUP` · hash `0x92AEFB5F6E294023` · jhash `0xCBB5F9B6` · **Cliente**

```lua
PreventCollectionOfPortablePickup(object, p1, p2)
```
```c
void PREVENT_COLLECTION_OF_PORTABLE_PICKUP(Object object, BOOL p1, BOOL p2);
```

**Parámetros**

- `object` (`Object`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x92AEFB5F6E294023` (`N_0x92aefb5f6e294023`)

---
### RemoveAllPickupsOfType

`REMOVE_ALL_PICKUPS_OF_TYPE` · hash `0x27F9D613092159CF` · jhash `0x40062C53` · **Cliente**

```lua
RemoveAllPickupsOfType(pickupHash)
```
```c
void REMOVE_ALL_PICKUPS_OF_TYPE(Hash pickupHash);
```

**Parámetros**

- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

Pickup hashes can be found [here](https://gist.github.com/4mmonium/1eabfb6b3996e3aa6b9525a3eccf8a0b).

---
### RemoveDoorFromSystem

`REMOVE_DOOR_FROM_SYSTEM` · hash `0x464D8E1427156FE4` · jhash `0x00253286` · **Cliente**

```lua
RemoveDoorFromSystem(doorHash)
```
```c
void REMOVE_DOOR_FROM_SYSTEM(Hash doorHash);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

CDoor and CDoorSystemData still internally allocated (and their associations between doorHash, modelHash, and coordinates).

Only its NetObj removed and flag `*(v2 + 192) |= 8u` (1604 retail) toggled.

---
### RemoveObjectHighDetailModel

`REMOVE_OBJECT_HIGH_DETAIL_MODEL` · hash `0x4A39DB43E47CF3AA` · jhash `0xE3261B35` · **Cliente**

```lua
RemoveObjectHighDetailModel(object)
```
```c
void REMOVE_OBJECT_HIGH_DETAIL_MODEL(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4A39DB43E47CF3AA` (`N_0x4a39db43e47cf3aa`)

---
### RemovePickup

`REMOVE_PICKUP` · hash `0x3288D8ACAECD2AB2` · jhash `0x64A7A0E0` · **Cliente**

```lua
RemovePickup(pickup)
```
```c
void REMOVE_PICKUP(Pickup pickup);
```

**Parámetros**

- `pickup` (`Pickup`)

**Devuelve:** `void`

---
### RenderFakePickupGlow

`RENDER_FAKE_PICKUP_GLOW` · hash `0x3430676B11CDF21D` · jhash `0x63B02FAD` · **Cliente**

```lua
RenderFakePickupGlow(x, y, z, colorIndex)
```
```c
void RENDER_FAKE_PICKUP_GLOW(float x, float y, float z, int colorIndex);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `colorIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
draws circular marker at pos
-1 = none
0 = red
1 = green
2 = blue
3 = green larger
4 = nothing
5 = green small
```

**Nombres antiguos (alias):** `0x3430676B11CDF21D` (`N_0x3430676b11cdf21d`), `_HIGHLIGHT_PLACEMENT_COORDS` (`HighlightPlacementCoords`)

---
### SetActivateObjectPhysicsAsSoonAsItIsUnfrozen

`SET_ACTIVATE_OBJECT_PHYSICS_AS_SOON_AS_IT_IS_UNFROZEN` · hash `0x406137F8EF90EAF5` · jhash `0x3E263AE1` · **Cliente**

```lua
SetActivateObjectPhysicsAsSoonAsItIsUnfrozen(object, toggle)
```
```c
void SET_ACTIVATE_OBJECT_PHYSICS_AS_SOON_AS_IT_IS_UNFROZEN(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetCreateWeaponObjectLightSource

`_SET_CREATE_WEAPON_OBJECT_LIGHT_SOURCE` · hash `0xBCE595371A5FBAAF` · jhash `0x3A68AA46` · **Cliente**

```lua
SetCreateWeaponObjectLightSource(object, toggle)
```
```c
void _SET_CREATE_WEAPON_OBJECT_LIGHT_SOURCE(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Requires a component_at_*_flsh to be attached to the weapon object
```

**Nombres antiguos (alias):** `0xBCE595371A5FBAAF` (`N_0xbce595371a5fbaaf`)

---
### SetEnableArenaPropPhysics

`_SET_ENABLE_ARENA_PROP_PHYSICS` · hash `0x911024442F4898F0` · **Cliente**

```lua
SetEnableArenaPropPhysics(entity, toggle, p2)
```
```c
void _SET_ENABLE_ARENA_PROP_PHYSICS(Object entity, BOOL toggle, int p2);
```

**Parámetros**

- `entity` (`Object`)
- `toggle` (`BOOL`)
- `p2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Activate the physics to: "xs_prop_arena_{flipper,wall,bollard,turntable,pit}"
```

```
NativeDB Introduced: v1604
```

**Nombres antiguos (alias):** `0x911024442F4898F0` (`N_0x911024442f4898f0`)

---
### SetEnableArenaPropPhysicsOnPed

`_SET_ENABLE_ARENA_PROP_PHYSICS_ON_PED` · hash `0xB20834A7DD3D8896` · **Cliente**

```lua
SetEnableArenaPropPhysicsOnPed(entity, toggle, p2, ped)
```
```c
void _SET_ENABLE_ARENA_PROP_PHYSICS_ON_PED(Object entity, BOOL toggle, int p2, Ped ped);
```

**Parámetros**

- `entity` (`Object`)
- `toggle` (`BOOL`)
- `p2` (`int`)
- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

**Nombres antiguos (alias):** `0xB20834A7DD3D8896` (`N_0xb20834a7dd3d8896`)

---
### SetForceObjectThisFrame

`SET_FORCE_OBJECT_THIS_FRAME` · hash `0xF538081986E49E9D` · jhash `0x3DA41C1A` · **Cliente**

```lua
SetForceObjectThisFrame(x, y, z, p3)
```
```c
void SET_FORCE_OBJECT_THIS_FRAME(float x, float y, float z, float p3);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### SetLocalPlayerCanCollectPortablePickups

`SET_LOCAL_PLAYER_CAN_COLLECT_PORTABLE_PICKUPS` · hash `0x78857FC65CADB909` · jhash `0xA3CDF152` · **Cliente**

```lua
SetLocalPlayerCanCollectPortablePickups(p0)
```
```c
void SET_LOCAL_PLAYER_CAN_COLLECT_PORTABLE_PICKUPS(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x78857FC65CADB909` (`N_0x78857fc65cadb909`)

---
### SetLocalPlayerCanUsePickupsWithThisModel

`_SET_LOCAL_PLAYER_CAN_USE_PICKUPS_WITH_THIS_MODEL` · hash `0x88EAEC617CD26926` · jhash `0x3A8F1BF7` · **Cliente**

```lua
SetLocalPlayerCanUsePickupsWithThisModel(modelHash, toggle)
```
```c
void _SET_LOCAL_PLAYER_CAN_USE_PICKUPS_WITH_THIS_MODEL(Hash modelHash, BOOL toggle);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Maximum amount of pickup models that can be disallowed is 30.
SET_LOCAL_PLAYER_*
```

**Nombres antiguos (alias):** `0x88EAEC617CD26926` (`N_0x88eaec617cd26926`)

---
### SetMaxNumPortablePickupsCarriedByPlayer

`SET_MAX_NUM_PORTABLE_PICKUPS_CARRIED_BY_PLAYER` · hash `0x0BF3B3BD47D79C08` · jhash `0x7EFBA039` · **Cliente**

```lua
SetMaxNumPortablePickupsCarriedByPlayer(modelHash, p1)
```
```c
void SET_MAX_NUM_PORTABLE_PICKUPS_CARRIED_BY_PLAYER(Hash modelHash, int p1);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0BF3B3BD47D79C08` (`N_0x0bf3b3bd47d79c08`)

---
### SetObjectAllowLowLodBuoyancy

`SET_OBJECT_ALLOW_LOW_LOD_BUOYANCY` · hash `0x4D89D607CB3DD1D2` · jhash `0x19B17769` · **Cliente**

```lua
SetObjectAllowLowLodBuoyancy(object, toggle)
```
```c
void SET_OBJECT_ALLOW_LOW_LOD_BUOYANCY(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Overrides the climbing/blocking flags of the object, used in the native scripts mostly for "prop_dock_bouy_*"
```

**Nombres antiguos (alias):** `0x4D89D607CB3DD1D2` (`N_0x4d89d607cb3dd1d2`), `_SET_OBJECT_CAN_CLIMB_ON` (`SetObjectCanClimbOn`)

---
### SetObjectForceVehiclesToAvoid

`SET_OBJECT_FORCE_VEHICLES_TO_AVOID` · hash `0x77F33F2CCF64B3AA` · jhash `0x483C5C88` · **Cliente**

```lua
SetObjectForceVehiclesToAvoid(object, toggle)
```
```c
void SET_OBJECT_FORCE_VEHICLES_TO_AVOID(Object object, BOOL toggle);
```

**Parámetros**

- `object` (`Object`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Overrides a flag on the object which determines if the object should be avoided by a vehicle in task: CTaskVehicleGoToPointWithAvoidanceAutomobile.
Tested on vehicles that were created by the vehicle generators.

**Nombres antiguos (alias):** `0x77F33F2CCF64B3AA` (`N_0x77f33f2ccf64b3aa`), `_SET_OBJECT_SOMETHING` (`SetObjectSomething`)

---
### SetObjectLightColor

`_SET_OBJECT_LIGHT_COLOR` · hash `0x5F048334B4A4E774` · **Cliente**

```lua
local retval = SetObjectLightColor(object, p1, r, g, b)
```
```c
Any _SET_OBJECT_LIGHT_COLOR(Object object, BOOL p1, int r, int g, int b);
```

**Parámetros**

- `object` (`Object`)
- `p1` (`BOOL`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `Any`

**Descripción oficial:**

Sets color of embedded light source.
Only appears in am_mp_nightclub.c for the nightclub dancefloor.

Not sure what p1 does, seems to only ever be '1' in scripts.

```
NativeDB Introduced: v1493
```

---
### SetObjectPhysicsParams

`SET_OBJECT_PHYSICS_PARAMS` · hash `0xF6DF6E90DE7DF90F` · jhash `0xE8D11C58` · **Cliente**

```lua
SetObjectPhysicsParams(object, mass, gravityFactor, linearC, linearV, linearV2, angularC, angularV, angularV2, p9, maxAngSpeed, buoyancyFactor)
```
```c
void SET_OBJECT_PHYSICS_PARAMS(Object object, float mass, float gravityFactor, float linearC, float linearV, float linearV2, float angularC, float angularV, float angularV2, float p9, float maxAngSpeed, float buoyancyFactor);
```

**Parámetros**

- `object` (`Object`)
- `mass` (`float`)
- `gravityFactor` (`float`)
- `linearC` (`float`)
- `linearV` (`float`)
- `linearV2` (`float`)
- `angularC` (`float`)
- `angularV` (`float`)
- `angularV2` (`float`)
- `p9` (`float`)
- `maxAngSpeed` (`float`)
- `buoyancyFactor` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
rage::phArchetypeDamp
p9: Some phBoundGeometry margin value, limited to (0.0, 0.1) exclusive.
```

---
### SetObjectStuntPropDuration

`_SET_OBJECT_STUNT_PROP_DURATION` · hash `0xDF6CA0330F2E737B` · **Cliente**

```lua
SetObjectStuntPropDuration(object, duration)
```
```c
void _SET_OBJECT_STUNT_PROP_DURATION(Object object, float duration);
```

**Parámetros**

- `object` (`Object`)
- `duration` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDF6CA0330F2E737B` (`N_0xdf6ca0330f2e737b`)

---
### SetObjectStuntPropSpeedup

`_SET_OBJECT_STUNT_PROP_SPEEDUP` · hash `0x96EE0EBA0163DF80` · **Cliente**

```lua
SetObjectStuntPropSpeedup(object, intensity)
```
```c
void _SET_OBJECT_STUNT_PROP_SPEEDUP(Object object, int intensity);
```

**Parámetros**

- `object` (`Object`): A Speed Boost or Slow Down prop
- `intensity` (`int`): Ranges from `1`-`254`, other values are ignored. Higher values will increase the effect of Speed Boosts and decrease the effect of Slow Downs.

**Devuelve:** `void`

**Descripción oficial:**

Sets the intensity of Speed Boost and Slow Down props.

The corresponding values for Speed Boosts in the Creator are:\
Weak: `15`\
Normal: `25`\
Strong: `35`\
Extra Strong: `45`\
Ultra Strong: `100`

For Slow Downs:\
Weak: `44`\
Normal: `30`\
Strong: `16`

**Nombres antiguos (alias):** `0x96EE0EBA0163DF80` (`N_0x96ee0eba0163df80`)

---
### SetObjectTargettable

`SET_OBJECT_TARGETTABLE` · hash `0x8A7391690F5AFD81` · jhash `0x3F88CD86` · **Cliente**

```lua
SetObjectTargettable(object, targettable)
```
```c
void SET_OBJECT_TARGETTABLE(Object object, BOOL targettable);
```

**Parámetros**

- `object` (`Object`)
- `targettable` (`BOOL`)

**Devuelve:** `void`

---
### SetObjectTargettableByPlayer

`_SET_OBJECT_TARGETTABLE_BY_PLAYER` · hash `0xB39F03368DB0CAA2` · **Cliente**

```lua
SetObjectTargettableByPlayer(object, setFlag34, setFlag35)
```
```c
void _SET_OBJECT_TARGETTABLE_BY_PLAYER(Object object, BOOL setFlag34, BOOL setFlag35);
```

**Parámetros**

- `object` (`Object`)
- `setFlag34` (`BOOL`)
- `setFlag35` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the 34th and 35th object flags related to player peds.

```
NativeDB Introduced: v3258
```

---
### SetObjectTextureVariation

`_SET_OBJECT_TEXTURE_VARIATION` · hash `0x971DA0055324D033` · **Cliente**

```lua
SetObjectTextureVariation(object, textureVariation)
```
```c
void _SET_OBJECT_TEXTURE_VARIATION(Object object, int textureVariation);
```

**Parámetros**

- `object` (`Object`)
- `textureVariation` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eObjectPaintVariants
{  
	Pacific = 0,  
	Azure = 1,  
	Nautical = 2,  
	Continental = 3,  
	Battleship = 4,  
	Intrepid = 5,  
	Uniform = 6,  
	Classico = 7,  
	Mediterranean = 8,  
	Command = 9,  
	Mariner = 10,  
	Ruby = 11,  
	Vintage = 12,  
	Pristine = 13,  
	Merchant = 14,  
	Voyager = 15  
};  
```

**Nombres antiguos (alias):** `0x971DA0055324D033` (`N_0x971da0055324d033`), `_SET_OBJECT_TEXTURE_VARIANT` (`SetObjectTextureVariant`)

---
### SetPickupGenerationRangeMultiplier

`SET_PICKUP_GENERATION_RANGE_MULTIPLIER` · hash `0x318516E02DE3ECE2` · jhash `0x9879AC51` · **Cliente**

```lua
SetPickupGenerationRangeMultiplier(multiplier)
```
```c
void SET_PICKUP_GENERATION_RANGE_MULTIPLIER(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x318516E02DE3ECE2` (`N_0x318516e02de3ece2`)

---
### SetPickupHiddenWhenUncollectable

`_SET_PICKUP_HIDDEN_WHEN_UNCOLLECTABLE` · hash `0x3ED2B83AB2E82799` · **Cliente**

```lua
SetPickupHiddenWhenUncollectable(p0, p1)
```
```c
void _SET_PICKUP_HIDDEN_WHEN_UNCOLLECTABLE(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3ED2B83AB2E82799` (`N_0x3ed2b83ab2e82799`)

---
### SetPickupRegenerationTime

`SET_PICKUP_REGENERATION_TIME` · hash `0x78015C9B4B3ECC9D` · jhash `0xAB11267D` · **Cliente**

```lua
SetPickupRegenerationTime(pickup, duration)
```
```c
void SET_PICKUP_REGENERATION_TIME(Pickup pickup, int duration);
```

**Parámetros**

- `pickup` (`Pickup`)
- `duration` (`int`)

**Devuelve:** `void`

---
### SetPickupUncollectable

`_SET_PICKUP_UNCOLLECTABLE` · hash `0x1C1B69FAE509BA97` · **Cliente**

```lua
SetPickupUncollectable(p0, p1)
```
```c
void _SET_PICKUP_UNCOLLECTABLE(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1C1B69FAE509BA97` (`N_0x1c1b69fae509ba97`)

---
### SetStateOfClosestDoorOfType

`SET_STATE_OF_CLOSEST_DOOR_OF_TYPE` · hash `0xF82D8F1926A02C3D` · jhash `0x38C951A4` · **Cliente**

```lua
SetStateOfClosestDoorOfType(type, x, y, z, locked, heading, p6)
```
```c
void SET_STATE_OF_CLOSEST_DOOR_OF_TYPE(Hash type, float x, float y, float z, BOOL locked, float heading, BOOL p6);
```

**Parámetros**

- `type` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `locked` (`BOOL`)
- `heading` (`float`)
- `p6` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Hardcoded to not work in multiplayer.  
Used to lock/unlock doors to interior areas of the game.  
(Possible) Door Types:  
pastebin.com/9S2m3qA4  
Heading is either 1, 0 or -1 in the scripts. Means default closed(0) or opened either into(1) or out(-1) of the interior.  
Locked means that the heading is locked.    
p6 is always 0.   
225 door types, model names and coords found in stripclub.c4:  
pastebin.com/gywnbzsH  
get door info: pastebin.com/i14rbekD  
```

---
### SetStateOfRayfireMapObject

`SET_STATE_OF_RAYFIRE_MAP_OBJECT` · hash `0x5C29F698D404C5E1` · jhash `0x21F51560` · **Cliente**

```lua
SetStateOfRayfireMapObject(object, state)
```
```c
void SET_STATE_OF_RAYFIRE_MAP_OBJECT(Object object, int state);
```

**Parámetros**

- `object` (`Object`)
- `state` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Defines the state of a destructible object.
Use the GET_RAYFIRE_MAP_OBJECT native to find an object's handle with its name / coords.
State 2 == object just spawned
State 4 == Beginning of the animation
State 6 == Start animation
State 9 == End of the animation
```

**Nombres antiguos (alias):** `0x5C29F698D404C5E1` (`N_0x5c29f698d404c5e1`), `_SET_DES_OBJECT_STATE` (`SetDesObjectState`)

---
### SetTeamPickupObject

`SET_TEAM_PICKUP_OBJECT` · hash `0x53E0DF1A2A3CF0CA` · jhash `0x77687DC5` · **Cliente**

```lua
SetTeamPickupObject(object, p1, p2)
```
```c
void SET_TEAM_PICKUP_OBJECT(Object object, Any p1, BOOL p2);
```

**Parámetros**

- `object` (`Object`)
- `p1` (`Any`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### SetTextureVariationOfClosestObjectOfType

`_SET_TEXTURE_VARIATION_OF_CLOSEST_OBJECT_OF_TYPE` · hash `0xF12E33034D887F66` · **Cliente**

```lua
local retval = SetTextureVariationOfClosestObjectOfType(x, y, z, radius, modelHash, textureVariation)
```
```c
BOOL _SET_TEXTURE_VARIATION_OF_CLOSEST_OBJECT_OF_TYPE(float x, float y, float z, float radius, Hash modelHash, int textureVariation);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `textureVariation` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF12E33034D887F66` (`N_0xf12e33034d887f66`)

---
### SetUnkGlobalBoolRelatedToDamage

`_SET_UNK_GLOBAL_BOOL_RELATED_TO_DAMAGE` · hash `0xABDABF4E1EDECBFA` · **Cliente**

```lua
SetUnkGlobalBoolRelatedToDamage(value)
```
```c
void _SET_UNK_GLOBAL_BOOL_RELATED_TO_DAMAGE(BOOL value);
```

**Parámetros**

- `value` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

---
### SlideObject

`SLIDE_OBJECT` · hash `0x2FDFF4107B8C1147` · jhash `0x63BFA7A0` · **Cliente**

```lua
local retval = SlideObject(object, toX, toY, toZ, speedX, speedY, speedZ, collision)
```
```c
BOOL SLIDE_OBJECT(Object object, float toX, float toY, float toZ, float speedX, float speedY, float speedZ, BOOL collision);
```

**Parámetros**

- `object` (`Object`)
- `toX` (`float`)
- `toY` (`float`)
- `toZ` (`float`)
- `speedX` (`float`)
- `speedY` (`float`)
- `speedZ` (`float`)
- `collision` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the object has finished moving.  
If false, moves the object towards the specified X, Y and Z coordinates with the specified X, Y and Z speed.  
See also: https://gtag.sannybuilder.com/opcode-database/opcode/034E/
Has to be looped until it returns true.   
```

---
### ToggleUsePickupsForPlayer

`_TOGGLE_USE_PICKUPS_FOR_PLAYER` · hash `0x616093EC6B139DD9` · jhash `0x7FADB4B9` · **Cliente**

```lua
ToggleUsePickupsForPlayer(player, pickupHash, toggle)
```
```c
void _TOGGLE_USE_PICKUPS_FOR_PLAYER(Player player, Hash pickupHash, BOOL toggle);
```

**Parámetros**

- `player` (`Player`): Player ID. Use [`PLAYER_ID`](PLAYER.md#playerid) for your own player.
- `pickupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Hash of the pickup, obtainable with [`GET_HASH_KEY`](../cfx/servidor.md#gethashkey)
- `toggle` (`BOOL`): boolean that enables/disables the pickup drop (false to disable, true to enable)

**Devuelve:** `void`

**Descripción oficial:**

```
Disabling/enabling a player from getting pickups. From the scripts:
OBJECT::_616093EC6B139DD9(PLAYER::PLAYER_ID(), ${pickup_portable_package}, 0);
```

**Nombres antiguos (alias):** `0x616093EC6B139DD9` (`N_0x616093ec6b139dd9`)

**Ejemplo (lua):**

```lua
-- Toggles the possibility for the player to drop the weapon pickups after death
local pickup = GetHashKey("PICKUP_WEAPON_ADVANCEDRIFLE")
ToggleUsePickupsForPlayer(PlayerId(), pickup, false)
```

---
### TrackObjectVisibility

`TRACK_OBJECT_VISIBILITY` · hash `0xB252BC036B525623` · jhash `0x46D06B9A` · **Cliente**

```lua
TrackObjectVisibility(object)
```
```c
void TRACK_OBJECT_VISIBILITY(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `void`

---
