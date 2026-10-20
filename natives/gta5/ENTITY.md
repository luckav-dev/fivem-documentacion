# Natives de GTA V — ENTITY

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `ENTITY`: **185** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ApplyForceToEntity`](#applyforcetoentity) · [`ApplyForceToEntityCenterOfMass`](#applyforcetoentitycenterofmass) · [`AttachEntityBoneToEntityBone`](#attachentitybonetoentitybone) · [`AttachEntityBoneToEntityBonePhysically`](#attachentitybonetoentitybonephysically) · [`AttachEntityToEntity`](#attachentitytoentity) · [`AttachEntityToEntityPhysically`](#attachentitytoentityphysically) · [`ClearEntityLastDamageEntity`](#clearentitylastdamageentity) · [`CreateForcedObject`](#createforcedobject) · [`CreateModelHide`](#createmodelhide) · [`CreateModelHideExcludingScriptObjects`](#createmodelhideexcludingscriptobjects) · [`CreateModelSwap`](#createmodelswap) · [`DeleteEntity`](#deleteentity) · [`DetachEntity`](#detachentity) · [`DoesEntityBelongToThisScript`](#doesentitybelongtothisscript) · [`DoesEntityExist`](#doesentityexist) · [`DoesEntityHaveAnimDirector`](#doesentityhaveanimdirector) · [`DoesEntityHaveDrawable`](#doesentityhavedrawable) · [`DoesEntityHavePhysics`](#doesentityhavephysics) · [`DoesEntityHaveSkeletonData`](#doesentityhaveskeletondata) · [`EnableEntityUnk`](#enableentityunk) · [`FindAnimEventPhase`](#findanimeventphase) · [`ForceEntityAiAndAnimationUpdate`](#forceentityaiandanimationupdate) · [`FreezeEntityPosition`](#freezeentityposition) · [`GetAnimDuration`](#getanimduration) · [`GetCollisionNormalOfLastHitForEntity`](#getcollisionnormaloflasthitforentity) · [`GetEntityAlpha`](#getentityalpha) · [`GetEntityAnimCurrentTime`](#getentityanimcurrenttime) · [`GetEntityAnimTotalTime`](#getentityanimtotaltime) · [`GetEntityAttachedTo`](#getentityattachedto) · [`GetEntityBoneCount`](#getentitybonecount) · [`GetEntityBoneIndexByName`](#getentityboneindexbyname) · [`GetEntityBonePosition_2`](#getentityboneposition_2) · [`GetEntityBoneRotation`](#getentitybonerotation) · [`GetEntityBoneRotationLocal`](#getentitybonerotationlocal) · [`GetEntityCanBeDamaged`](#getentitycanbedamaged) · [`GetEntityCollisionDisabled`](#getentitycollisiondisabled) · [`GetEntityCoords`](#getentitycoords) · [`GetEntityForwardVector`](#getentityforwardvector) · [`GetEntityForwardX`](#getentityforwardx) · [`GetEntityForwardY`](#getentityforwardy) · [`GetEntityHeading`](#getentityheading) · [`GetEntityHeadingFromEulers`](#getentityheadingfromeulers) · [`GetEntityHealth`](#getentityhealth) · [`GetEntityHeight`](#getentityheight) · [`GetEntityHeightAboveGround`](#getentityheightaboveground) · [`GetEntityLodDist`](#getentityloddist) · [`GetEntityMatrix`](#getentitymatrix) · [`GetEntityMaxHealth`](#getentitymaxhealth) · [`GetEntityModel`](#getentitymodel) · [`GetEntityPickup`](#getentitypickup) · [`GetEntityPitch`](#getentitypitch) · [`GetEntityPopulationType`](#getentitypopulationtype) · [`GetEntityProofs`](#getentityproofs) · [`GetEntityQuaternion`](#getentityquaternion) · [`GetEntityRoll`](#getentityroll) · [`GetEntityRotation`](#getentityrotation) · [`GetEntityRotationVelocity`](#getentityrotationvelocity) · [`GetEntityScript`](#getentityscript) · [`GetEntitySpeed`](#getentityspeed) · [`GetEntitySpeedVector`](#getentityspeedvector) · [`GetEntitySubmergedLevel`](#getentitysubmergedlevel) · [`GetEntityType`](#getentitytype) · [`GetEntityUprightValue`](#getentityuprightvalue) · [`GetEntityVelocity`](#getentityvelocity) · [`GetLastMaterialHitByEntity`](#getlastmaterialhitbyentity) · [`GetNearestPlayerToEntity`](#getnearestplayertoentity) · [`GetNearestPlayerToEntityOnTeam`](#getnearestplayertoentityonteam) · [`GetObjectIndexFromEntityIndex`](#getobjectindexfromentityindex) · [`GetOffsetFromEntityGivenWorldCoords`](#getoffsetfromentitygivenworldcoords) · [`GetOffsetFromEntityInWorldCoords`](#getoffsetfromentityinworldcoords) · [`GetPedIndexFromEntityIndex`](#getpedindexfromentityindex) · [`GetVehicleIndexFromEntityIndex`](#getvehicleindexfromentityindex) · [`GetWorldPositionOfEntityBone`](#getworldpositionofentitybone) · [`HasAnimEventFired`](#hasanimeventfired) · [`HasCollisionLoadedAroundEntity`](#hascollisionloadedaroundentity) · [`HasEntityAnimFinished`](#hasentityanimfinished) · [`HasEntityBeenDamagedByAnyObject`](#hasentitybeendamagedbyanyobject) · [`HasEntityBeenDamagedByAnyPed`](#hasentitybeendamagedbyanyped) · [`HasEntityBeenDamagedByAnyVehicle`](#hasentitybeendamagedbyanyvehicle) · [`HasEntityBeenDamagedByEntity`](#hasentitybeendamagedbyentity) · [`HasEntityClearLosToEntity`](#hasentityclearlostoentity) · [`HasEntityClearLosToEntityInFront`](#hasentityclearlostoentityinfront) · [`HasEntityClearLosToEntity_2`](#hasentityclearlostoentity_2) · [`HasEntityCollidedWithAnything`](#hasentitycollidedwithanything) · [`IsAnEntity`](#isanentity) · [`IsEntityAMissionEntity`](#isentityamissionentity) · [`IsEntityAPed`](#isentityaped) · [`IsEntityAVehicle`](#isentityavehicle) · [`IsEntityAnObject`](#isentityanobject) · [`IsEntityAtCoord`](#isentityatcoord) · [`IsEntityAtEntity`](#isentityatentity) · [`IsEntityAttached`](#isentityattached) · [`IsEntityAttachedToAnyObject`](#isentityattachedtoanyobject) · [`IsEntityAttachedToAnyPed`](#isentityattachedtoanyped) · [`IsEntityAttachedToAnyVehicle`](#isentityattachedtoanyvehicle) · [`IsEntityAttachedToEntity`](#isentityattachedtoentity) · [`IsEntityDead`](#isentitydead) · [`IsEntityInAir`](#isentityinair) · [`IsEntityInAngledArea`](#isentityinangledarea) · [`IsEntityInArea`](#isentityinarea) · [`IsEntityInWater`](#isentityinwater) · [`IsEntityInZone`](#isentityinzone) · [`IsEntityOccluded`](#isentityoccluded) · [`IsEntityOnScreen`](#isentityonscreen) · [`IsEntityPlayingAnim`](#isentityplayinganim) · [`IsEntityStatic`](#isentitystatic) · [`IsEntityTouchingEntity`](#isentitytouchingentity) · [`IsEntityTouchingModel`](#isentitytouchingmodel) · [`IsEntityUpright`](#isentityupright) · [`IsEntityUpsidedown`](#isentityupsidedown) · [`IsEntityVisible`](#isentityvisible) · [`IsEntityVisibleToScript`](#isentityvisibletoscript) · [`IsEntityWaitingForWorldCollision`](#isentitywaitingforworldcollision) · [`N_0x1a092bb0c3808b96`](#n_0x1a092bb0c3808b96) · [`N_0x352e2b5cf420bf3b`](#n_0x352e2b5cf420bf3b) · [`N_0x36f32de87082343e`](#n_0x36f32de87082343e) · [`N_0x490861b88f4fd846`](#n_0x490861b88f4fd846) · [`N_0x5c3b791d580e0bc2`](#n_0x5c3b791d580e0bc2) · [`N_0x68b562e124cc0aef`](#n_0x68b562e124cc0aef) · [`N_0x78e8e3a640178255`](#n_0x78e8e3a640178255) · [`N_0xb17bc6453f6cf5ac`](#n_0xb17bc6453f6cf5ac) · [`N_0xc34bc448da29f5e9`](#n_0xc34bc448da29f5e9) · [`N_0xcea7c8e1b48ff68c`](#n_0xcea7c8e1b48ff68c) · [`N_0xe66377cddada4810`](#n_0xe66377cddada4810) · [`PlayEntityAnim`](#playentityanim) · [`PlaySynchronizedEntityAnim`](#playsynchronizedentityanim) · [`PlaySynchronizedMapEntityAnim`](#playsynchronizedmapentityanim) · [`ProcessEntityAttachments`](#processentityattachments) · [`RemoveForcedObject`](#removeforcedobject) · [`RemoveModelHide`](#removemodelhide) · [`RemoveModelSwap`](#removemodelswap) · [`ResetEntityAlpha`](#resetentityalpha) · [`SetCanAutoVaultOnEntity`](#setcanautovaultonentity) · [`SetCanClimbOnEntity`](#setcanclimbonentity) · [`SetEntityAlpha`](#setentityalpha) · [`SetEntityAlwaysPrerender`](#setentityalwaysprerender) · [`SetEntityAngularVelocity`](#setentityangularvelocity) · [`SetEntityAnimCurrentTime`](#setentityanimcurrenttime) · [`SetEntityAnimSpeed`](#setentityanimspeed) · [`SetEntityAsMissionEntity`](#setentityasmissionentity) · [`SetEntityAsNoLongerNeeded`](#setentityasnolongerneeded) · [`SetEntityCanBeDamaged`](#setentitycanbedamaged) · [`SetEntityCanBeDamagedByRelationshipGroup`](#setentitycanbedamagedbyrelationshipgroup) · [`SetEntityCanBeTargetedWithoutLos`](#setentitycanbetargetedwithoutlos) · [`SetEntityCleanupByEngine`](#setentitycleanupbyengine) · [`SetEntityCollision`](#setentitycollision) · [`SetEntityCompletelyDisableCollision`](#setentitycompletelydisablecollision) · [`SetEntityCoords`](#setentitycoords) · [`SetEntityCoordsNoOffset`](#setentitycoordsnooffset) · [`SetEntityCoordsWithoutPlantsReset`](#setentitycoordswithoutplantsreset) · [`SetEntityDecalsDisabled`](#setentitydecalsdisabled) · [`SetEntityDynamic`](#setentitydynamic) · [`SetEntityHasGravity`](#setentityhasgravity) · [`SetEntityHeading`](#setentityheading) · [`SetEntityHealth`](#setentityhealth) · [`SetEntityInvincible`](#setentityinvincible) · [`SetEntityIsTargetPriority`](#setentityistargetpriority) · [`SetEntityLights`](#setentitylights) · [`SetEntityLoadCollisionFlag`](#setentityloadcollisionflag) · [`SetEntityLodDist`](#setentityloddist) · [`SetEntityMaxHealth`](#setentitymaxhealth) · [`SetEntityMaxSpeed`](#setentitymaxspeed) · [`SetEntityMotionBlur`](#setentitymotionblur) · [`SetEntityNoCollisionEntity`](#setentitynocollisionentity) · [`SetEntityNoCollisionWithNetworkedEntity`](#setentitynocollisionwithnetworkedentity) · [`SetEntityOnlyDamagedByPlayer`](#setentityonlydamagedbyplayer) · [`SetEntityOnlyDamagedByRelationshipGroup`](#setentityonlydamagedbyrelationshipgroup) · [`SetEntityProofs`](#setentityproofs) · [`SetEntityQuaternion`](#setentityquaternion) · [`SetEntityRecordsCollisions`](#setentityrecordscollisions) · [`SetEntityRenderScorched`](#setentityrenderscorched) · [`SetEntityRequiresMoreExpensiveRiverCheck`](#setentityrequiresmoreexpensiverivercheck) · [`SetEntityRotation`](#setentityrotation) · [`SetEntityTrafficlightOverride`](#setentitytrafficlightoverride) · [`SetEntityVelocity`](#setentityvelocity) · [`SetEntityVisible`](#setentityvisible) · [`SetObjectAsNoLongerNeeded`](#setobjectasnolongerneeded) · [`SetPedAsNoLongerNeeded`](#setpedasnolongerneeded) · [`SetPickUpByCargobobDisabled`](#setpickupbycargobobdisabled) · [`SetVehicleAsNoLongerNeeded`](#setvehicleasnolongerneeded) · [`SetWaitForCollisionsBeforeProbe`](#setwaitforcollisionsbeforeprobe) · [`StopEntityAnim`](#stopentityanim) · [`StopSynchronizedEntityAnim`](#stopsynchronizedentityanim) · [`StopSynchronizedMapEntityAnim`](#stopsynchronizedmapentityanim) · [`WouldEntityBeOccluded`](#wouldentitybeoccluded)

---
### ApplyForceToEntity

`APPLY_FORCE_TO_ENTITY` · hash `0xC5F68BE9613E2D18` · jhash `0xC1C0855A` · **Cliente · también en el servidor (RPC)**

```lua
ApplyForceToEntity(entity, forceType, x, y, z, offX, offY, offZ, nComponent, bLocalForce, bLocalOffset, bScaleByMass, bPlayAudio, bScaleByTimeWarp)
```
```c
void APPLY_FORCE_TO_ENTITY(Entity entity, int forceType, float x, float y, float z, float offX, float offY, float offZ, int nComponent, BOOL bLocalForce, BOOL bLocalOffset, BOOL bScaleByMass, BOOL bPlayAudio, BOOL bScaleByTimeWarp);
```

**Parámetros**

- `entity` (`Entity`): The entity handle
- `forceType` (`int`): The force type
- `x` (`float`): The x component of the force to apply
- `y` (`float`): The y component of the force to apply
- `z` (`float`): The z component of the force to apply
- `offX` (`float`): Offset from center of entity (X)
- `offY` (`float`): Offset from center of entity (Y)
- `offZ` (`float`): Offset from center of entity (Z)
- `nComponent` (`int`): Component of the entity to apply the force too. Only matters for breakable or articulated (ragdoll) physics. 0 means the root or parent component
- `bLocalForce` (`BOOL`): Specifies whether the force vector passed in is in local or world coordinates. `true` means the force will get automatically transformed into world space before being applied
- `bLocalOffset` (`BOOL`): Specifies whether the offset passed in is in local or world coordinates
- `bScaleByMass` (`BOOL`): Specifies whether to scale the force by mass
- `bPlayAudio` (`BOOL`): Specifies whether to play audio events related to the force being applied. The audio will depend on the entity type. Currently vehicles are the only entity types supported, and will play a suspension squeal depending on the magnitude of the force
- `bScaleByTimeWarp` (`BOOL`): Specifies whether to scale the force by time warp. Default is `true`

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eApplyForceTypes {
    APPLY_TYPE_FORCE = 0,
    APPLY_TYPE_IMPULSE = 1,
    APPLY_TYPE_EXTERNAL_FORCE = 2,
    APPLY_TYPE_EXTERNAL_IMPULSE = 3,
    APPLY_TYPE_TORQUE = 4,
    APPLY_TYPE_ANGULAR_IMPULSE = 5
}
```

**Ejemplo (lua):**

```lua
local entity = PlayerPedId()
local forceType = 2
 -- sends the entity straight up into the sky:
local direction = vector3(0.0, 0.0, 15.0)
local offset = vector3(0.0, 0.0, 0.0)
local component = 0
local localForce = false
local localOffset = true
local scaleByMass = true
local playAudio = false
local scaleByTimeWarp = true

ApplyForceToEntity(
    entity,
    forceType,
    direction,
    offset,
    boneIndex,
    localForce,
    localOffset,
    scaleByMass,
    playAudio,
    scaleByTimeWarp
)
```

---
### ApplyForceToEntityCenterOfMass

`APPLY_FORCE_TO_ENTITY_CENTER_OF_MASS` · hash `0x18FF00FC7EFF559E` · jhash `0x28924E98` · **Cliente**

```lua
ApplyForceToEntityCenterOfMass(entity, forceType, x, y, z, nComponent, bLocalForce, bScaleByMass, bApplyToChildren)
```
```c
void APPLY_FORCE_TO_ENTITY_CENTER_OF_MASS(Entity entity, int forceType, float x, float y, float z, int nComponent, BOOL bLocalForce, BOOL bScaleByMass, BOOL bApplyToChildren);
```

**Parámetros**

- `entity` (`Entity`): The entity handle
- `forceType` (`int`): The force type, see [`APPLY_FORCE_TO_ENTITY`](../cfx/servidor.md#applyforcetoentity)
- `x` (`float`): The x component of the force to apply
- `y` (`float`): The y component of the force to apply
- `z` (`float`): The z component of the force to apply
- `nComponent` (`int`): Component of the entity to apply the force too. Only matters for breakable or articulated (ragdoll) physics. 0 means the root or parent component
- `bLocalForce` (`BOOL`): Specifies whether the force vector passed in is in local or world coordinates. `true` means the force will get automatically transformed into world space before being applied
- `bScaleByMass` (`BOOL`): Specifies whether to scale the force by mass
- `bApplyToChildren` (`BOOL`): Default `false`. If the force should be applied to any attached children

**Devuelve:** `void`

**Descripción oficial:**

Apply a force to an entities center of mass.

---
### AttachEntityBoneToEntityBone

`_ATTACH_ENTITY_BONE_TO_ENTITY_BONE` · hash `0x5C48B75732C8456C` · **Cliente**

```lua
AttachEntityBoneToEntityBone(entity1, entity2, entityBone, entityBone2, p4, p5)
```
```c
void _ATTACH_ENTITY_BONE_TO_ENTITY_BONE(Entity entity1, Entity entity2, int entityBone, int entityBone2, BOOL p4, BOOL p5);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)
- `entityBone` (`int`)
- `entityBone2` (`int`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5C48B75732C8456C` (`N_0x5c48b75732c8456c`)

---
### AttachEntityBoneToEntityBonePhysically

`_ATTACH_ENTITY_BONE_TO_ENTITY_BONE_PHYSICALLY` · hash `0xFD1695C5D3B05439` · **Cliente**

```lua
AttachEntityBoneToEntityBonePhysically(entity1, entity2, entityBone, entityBone2, p4, p5)
```
```c
void _ATTACH_ENTITY_BONE_TO_ENTITY_BONE_PHYSICALLY(Entity entity1, Entity entity2, int entityBone, int entityBone2, BOOL p4, BOOL p5);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)
- `entityBone` (`int`)
- `entityBone2` (`int`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFD1695C5D3B05439` (`N_0xfd1695c5d3b05439`)

---
### AttachEntityToEntity

`ATTACH_ENTITY_TO_ENTITY` · hash `0x6B9BBD38AB0796DF` · jhash `0xEC024237` · **Cliente**

```lua
AttachEntityToEntity(entity1, entity2, boneIndex, xPos, yPos, zPos, xRot, yRot, zRot, p9, useSoftPinning, collision, isPed, rotationOrder, syncRot)
```
```c
void ATTACH_ENTITY_TO_ENTITY(Entity entity1, Entity entity2, int boneIndex, float xPos, float yPos, float zPos, float xRot, float yRot, float zRot, BOOL p9, BOOL useSoftPinning, BOOL collision, BOOL isPed, int rotationOrder, BOOL syncRot);
```

**Parámetros**

- `entity1` (`Entity`): Entity to attach.
- `entity2` (`Entity`): Entity to attach `entity1` with.
- `boneIndex` (`int`): This is different to boneID, use ['GET_PED_BONE_INDEX'](PED-1.md#getpedboneindex) to get the index from the ID. use the index for attaching to specific bones. `entity1` will be attached to the center of `entity2` if bone index given doesn't correspond to bone indexes for that entity type.
- `xPos` (`float`): X-axis offset from the center of `entity2`.
- `yPos` (`float`): Y-axis offset from the center of `entity2`.
- `zPos` (`float`): Z-axis offset from the center of `entity2`.
- `xRot` (`float`): X-axis rotation.
- `yRot` (`float`): Y-axis rotation.
- `zRot` (`float`): Z-axis rotation.
- `p9` (`BOOL`): Unknown. Does not seem to have any effect.
- `useSoftPinning` (`BOOL`): If set to false attached entity will not detach when fixed.
- `collision` (`BOOL`): Controls collision between the two entities (FALSE disables collision).
- `isPed` (`BOOL`): Pitch doesnt work when false and roll will only work on negative numbers (only peds)
- `rotationOrder` (`int`): The order in which the rotation is applied. See [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation)
- `syncRot` (`BOOL`): If false it ignores entity rotation.

**Devuelve:** `void`

**Descripción oficial:**

Attach an entity to the specified entity.

---
### AttachEntityToEntityPhysically

`ATTACH_ENTITY_TO_ENTITY_PHYSICALLY` · hash `0xC3675780C92F90F9` · jhash `0x0547417F` · **Cliente**

```lua
AttachEntityToEntityPhysically(entity1, entity2, boneIndex1, boneIndex2, xPos1, yPos1, zPos1, xPos2, yPos2, zPos2, xRot, yRot, zRot, breakForce, fixedRot, p15, collision, teleport, p18)
```
```c
void ATTACH_ENTITY_TO_ENTITY_PHYSICALLY(Entity entity1, Entity entity2, int boneIndex1, int boneIndex2, float xPos1, float yPos1, float zPos1, float xPos2, float yPos2, float zPos2, float xRot, float yRot, float zRot, float breakForce, BOOL fixedRot, BOOL p15, BOOL collision, BOOL teleport, int p18);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)
- `boneIndex1` (`int`)
- `boneIndex2` (`int`)
- `xPos1` (`float`)
- `yPos1` (`float`)
- `zPos1` (`float`)
- `xPos2` (`float`)
- `yPos2` (`float`)
- `zPos2` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `breakForce` (`float`)
- `fixedRot` (`BOOL`)
- `p15` (`BOOL`)
- `collision` (`BOOL`)
- `teleport` (`BOOL`)
- `p18` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
breakForce is the amount of force required to break the bond.
p14 - is always 1 in scripts
p15 - is 1 or 0 in scripts - unknown what it does
p16 - controls collision between the two entities (FALSE disables collision).
p17 - do not teleport entity to be attached to the position of the bone Index of the target entity (if 1, entity will not be teleported to target bone)
p18 - is always 2 in scripts.
```

---
### ClearEntityLastDamageEntity

`CLEAR_ENTITY_LAST_DAMAGE_ENTITY` · hash `0xA72CD9CA74A5ECBA` · jhash `0x2B83F43B` · **Cliente**

```lua
ClearEntityLastDamageEntity(entity)
```
```c
void CLEAR_ENTITY_LAST_DAMAGE_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to clear the last damaging entity from.

**Devuelve:** `void`

**Descripción oficial:**

This native **could affect** the arguments of the `CEventNetworkEntityDamage` game event, by clearing the damaging entity before the event is fired.

---
### CreateForcedObject

`CREATE_FORCED_OBJECT` · hash `0x150E808B375A385A` · jhash `0x335190A2` · **Cliente**

```lua
CreateForcedObject(x, y, z, p3, modelHash, p5)
```
```c
void CREATE_FORCED_OBJECT(float x, float y, float z, Any p3, Hash modelHash, BOOL p5);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`Any`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p5` (`BOOL`)

**Devuelve:** `void`

---
### CreateModelHide

`CREATE_MODEL_HIDE` · hash `0x8A97BCA30A0CE478` · jhash `0x7BD5CF2F` · **Cliente**

```lua
CreateModelHide(x, y, z, radius, model, surviveMapReload)
```
```c
void CREATE_MODEL_HIDE(float x, float y, float z, float radius, Hash model, BOOL surviveMapReload);
```

**Parámetros**

- `x` (`float`): X Coordinate of the hiding sphere center.
- `y` (`float`): Y Coordinate of the hiding sphere center.
- `z` (`float`): Z Coordinate of the hiding sphere center.
- `radius` (`float`): Radius of the hiding sphere.
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The object's model hash to hide.
- `surviveMapReload` (`BOOL`): If false, only currently loaded objects are hidden. If their map unloads (e.g. by moving away) and reloads, the objects will reappear.

**Devuelve:** `void`

**Descripción oficial:**

Hides all objects of the specified model intersecting a sphere centered at (x, y, z) with the given radius.
Network players do not see changes done with this.
Use [`CREATE_MODEL_HIDE_EXCLUDING_SCRIPT_OBJECTS`](#createmodelhideexcludingscriptobjects) if you only want to hide map objects and exclude those created by scripts.
Use [`REMOVE_MODEL_HIDE`](#removemodelhide) to make hidden objects visible again.

---
### CreateModelHideExcludingScriptObjects

`CREATE_MODEL_HIDE_EXCLUDING_SCRIPT_OBJECTS` · hash `0x3A52AE588830BF7F` · jhash `0x07AAF22C` · **Cliente**

```lua
CreateModelHideExcludingScriptObjects(x, y, z, radius, model, surviveMapReload)
```
```c
void CREATE_MODEL_HIDE_EXCLUDING_SCRIPT_OBJECTS(float x, float y, float z, float radius, Hash model, BOOL surviveMapReload);
```

**Parámetros**

- `x` (`float`): X Coordinate of the hiding sphere center.
- `y` (`float`): Y Coordinate of the hiding sphere center.
- `z` (`float`): Z Coordinate of the hiding sphere center.
- `radius` (`float`): Radius of the hiding sphere.
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The object's model hash to hide.
- `surviveMapReload` (`BOOL`): If false, only currently loaded objects are hidden. If their map unloads (e.g. by moving away) and reloads, the objects will reappear.

**Devuelve:** `void`

**Descripción oficial:**

Hides all objects of the specified model intersecting a sphere centered at (x, y, z) with the given radius, excluding objects created by scripts.
Network players do not see changes done with this.
Use [`REMOVE_MODEL_HIDE`](#removemodelhide) to make hidden objects visible again.

---
### CreateModelSwap

`CREATE_MODEL_SWAP` · hash `0x92C47782FDA8B2A3` · jhash `0x0BC12F9E` · **Cliente**

```lua
CreateModelSwap(x, y, z, radius, originalModel, newModel, bSurviveMapReload)
```
```c
void CREATE_MODEL_SWAP(float x, float y, float z, float radius, Hash originalModel, Hash newModel, BOOL bSurviveMapReload);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `originalModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `newModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `bSurviveMapReload` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only works with objects!  
Network players do not see changes done with this.  
```

---
### DeleteEntity

`DELETE_ENTITY` · hash `0xAE3CBE5BF394C9C9` · jhash `0xFAA3D236` · **Cliente**

```lua
local entity = DeleteEntity(entity)
```
```c
void DELETE_ENTITY(Entity* entity);
```

**Parámetros**

- `entity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The entity to delete.

**Devuelve:** `void`

**Descripción oficial:**

Delete the specified entity, and invalidate the passed handle (i.e., the in/out argument).
You might want to check if the entity exists before with [DOES_ENTITY_EXIST](../cfx/servidor.md#doesentityexist).

**Ejemplo (lua):**

```lua
-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

-- Check if the vehicle exists in the game world.
if not DoesEntityExist(vehicle) then 
    -- If the vehicle does not exist, end the execution of the code here.
    return 
end

-- If the vehicle does exist, delete the vehicle entity from the game world.
DeleteEntity(vehicle)
```

**Ejemplo (js):**

```js
// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
  // If the vehicle does not exist, end the execution of the code here.
  return;
}

// If the vehicle does exist, delete the vehicle entity from the game world.
DeleteEntity(vehicle);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Retrieve the vehicle the player is currently in.
int vehicleHandle = GetVehiclePedIsIn(PlayerPedId(), false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicleHandle))
{
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// If the vehicle does exist, delete the vehicle entity from the game world.
DeleteEntity(ref vehicleHandle);
```

---
### DetachEntity

`DETACH_ENTITY` · hash `0x961AC54BF0613F5D` · jhash `0xC8EFCB41` · **Cliente**

```lua
DetachEntity(entity, dynamic, collision)
```
```c
void DETACH_ENTITY(Entity entity, BOOL dynamic, BOOL collision);
```

**Parámetros**

- `entity` (`Entity`)
- `dynamic` (`BOOL`): Set to `true` to keep velocity after detaching
- `collision` (`BOOL`)

**Devuelve:** `void`

---
### DoesEntityBelongToThisScript

`DOES_ENTITY_BELONG_TO_THIS_SCRIPT` · hash `0xDDE6DF5AE89981D2` · jhash `0xACFEB3F9` · **Cliente**

```lua
local retval = DoesEntityBelongToThisScript(entity, p2)
```
```c
BOOL DOES_ENTITY_BELONG_TO_THIS_SCRIPT(Entity entity, BOOL p2);
```

**Parámetros**

- `entity` (`Entity`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

---
### DoesEntityExist

`DOES_ENTITY_EXIST` · hash `0x7239B21A38F536BA` · jhash `0x3AC90869` · **Cliente**

```lua
local retval = DoesEntityExist(entity)
```
```c
BOOL DOES_ENTITY_EXIST(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to check if it exists.

**Devuelve:** `BOOL` — Whether the entity exists or not.

**Descripción oficial:**

Checks whether an entity exists in the game world.

**Ejemplo (lua):**

```lua
local currentVehicle = GetVehiclePedIsIn(PlayerPedId(), false)

if DoesEntityExist(currentVehicle) then
    DeleteEntity(currentVehicle)
end
```

**Ejemplo (js):**

```js
const currentVehicle = GetVehiclePedIsIn(PlayerPedId(), false);

if (DoesEntityExist(currentVehicle)) {
  DeleteEntity(currentVehicle);
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API
// ...

int currentVehicle = GetVehiclePedIsIn(PlayerPedId(), false);

if(DoesEntityExist(currentVehicle))
{
    DeleteEntity(currentVehicle);
}

// or the preferred use of C# wrapper
Vehicle currentVehicle = Game.PlayerPed.CurrentVehicle;

// DoesEntityExist already invoked using Game.PlayerPed.CurrentVehicle
if(currentVehicle != null)
{
    currentVehicle.Delete();
}
```

---
### DoesEntityHaveAnimDirector

`_DOES_ENTITY_HAVE_ANIM_DIRECTOR` · hash `0x2158E81A6AF65EA9` · **Cliente**

```lua
local retval = DoesEntityHaveAnimDirector(entity)
```
```c
BOOL _DOES_ENTITY_HAVE_ANIM_DIRECTOR(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### DoesEntityHaveDrawable

`DOES_ENTITY_HAVE_DRAWABLE` · hash `0x060D6E96F8B8E48D` · jhash `0xA5B33300` · **Cliente**

```lua
local retval = DoesEntityHaveDrawable(entity)
```
```c
BOOL DOES_ENTITY_HAVE_DRAWABLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### DoesEntityHavePhysics

`DOES_ENTITY_HAVE_PHYSICS` · hash `0xDA95EA3317CC5064` · jhash `0x9BCD2979` · **Cliente**

```lua
local retval = DoesEntityHavePhysics(entity)
```
```c
BOOL DOES_ENTITY_HAVE_PHYSICS(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### DoesEntityHaveSkeletonData

`_DOES_ENTITY_HAVE_SKELETON_DATA` · hash `0x764EB96874EFFDC1` · **Cliente**

```lua
local retval = DoesEntityHaveSkeletonData(entity)
```
```c
BOOL _DOES_ENTITY_HAVE_SKELETON_DATA(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### EnableEntityUnk

`_ENABLE_ENTITY_UNK` · hash `0x6CE177D014502E8A` · **Cliente**

```lua
EnableEntityUnk(entity)
```
```c
void _ENABLE_ENTITY_UNK(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
ENABLE_*
```

**Nombres antiguos (alias):** `0x6CE177D014502E8A` (`N_0x6ce177d014502e8a`)

---
### FindAnimEventPhase

`FIND_ANIM_EVENT_PHASE` · hash `0x07F1BE2BCCAA27A7` · jhash `0xC41DDA62` · **Cliente**

```lua
local retval, p3, p4 = FindAnimEventPhase(animDictionary, animName, p2)
```
```c
BOOL FIND_ANIM_EVENT_PHASE(char* animDictionary, char* animName, char* p2, Any* p3, Any* p4);
```

**Parámetros**

- `animDictionary` (`char*`)
- `animName` (`char*`)
- `p2` (`char*`)
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
In the script "player_scene_t_bbfight.c4":  
"if (ENTITY::FIND_ANIM_EVENT_PHASE(&l_16E, &l_19F[v_4/*16*/], v_9, &v_A, &v_B))"  
-- &l_16E (p0) is requested as an anim dictionary earlier in the script.  
-- &l_19F[v_4/*16*/] (p1) is used in other natives in the script as the "animation" param.  
-- v_9 (p2) is instantiated as "victim_fall"; I'm guessing that's another anim  
--v_A and v_B (p3 & p4) are both set as -1.0, but v_A is used immediately after this native for:   
"if (v_A < ENTITY::GET_ENTITY_ANIM_CURRENT_TIME(...))"  
Both v_A and v_B are seemingly used to contain both Vector3's and floats, so I can't say what either really is other than that they are both output parameters. p4 looks more like a *Vector3 though  
-alphazolam  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### ForceEntityAiAndAnimationUpdate

`FORCE_ENTITY_AI_AND_ANIMATION_UPDATE` · hash `0x40FDEDB72F8293B2` · jhash `0x58D9775F` · **Cliente**

```lua
ForceEntityAiAndAnimationUpdate(entity)
```
```c
void FORCE_ENTITY_AI_AND_ANIMATION_UPDATE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
Based on carmod_shop script decompile this takes a vehicle parameter. It is called when repair is done on initial enter.  
```

---
### FreezeEntityPosition

`FREEZE_ENTITY_POSITION` · hash `0x428CA6DBD1094446` · jhash `0x65C16D57` · **Cliente · también en el servidor (RPC)**

```lua
FreezeEntityPosition(entity, toggle)
```
```c
void FREEZE_ENTITY_POSITION(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`): The entity to freeze/unfreeze.
- `toggle` (`BOOL`): Freeze or unfreeze entity.

**Devuelve:** `void`

**Descripción oficial:**

Freezes or unfreezes an entity preventing its coordinates to change by the player if set to `true`. You can still change the entity position using [`SET_ENTITY_COORDS`](../cfx/servidor.md#setentitycoords).

**Ejemplo (lua):**

```lua
-- Freeze the local player.

-- Retrieve the player ped
local playerPed = PlayerPedId() 

-- Freeze the ped
FreezeEntityPosition(playerPed, true)
```

**Ejemplo (js):**

```js
// Freeze the local player.

// Retrieve the player ped
const playerPed = PlayerPedId();

// Freeze the ped
FreezeEntityPosition(playerPed, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// Freeze the local player.

// Retrieve the player ped
int playerPed = PlayerPedId();

// Freeze the ped
FreezeEntityPosition(playerPed, true);

// or the preferred use of C# wrapper
Game.PlayerPed.IsPositionFrozen = true;
```

---
### GetAnimDuration

`GET_ANIM_DURATION` · hash `0xFEDDF04D62B8D790` · jhash `0x8B5E3E3D` · **Cliente**

```lua
local retval = GetAnimDuration(animDict, animName)
```
```c
float GET_ANIM_DURATION(char* animDict, char* animName);
```

**Parámetros**

- `animDict` (`char*`)
- `animName` (`char*`)

**Devuelve:** `float`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

**Nombres antiguos (alias):** `_GET_ANIM_DURATION` (`GetAnimDuration`)

---
### GetCollisionNormalOfLastHitForEntity

`GET_COLLISION_NORMAL_OF_LAST_HIT_FOR_ENTITY` · hash `0xE465D4AB7CA6AE72` · jhash `0xAB415C07` · **Cliente**

```lua
local retval = GetCollisionNormalOfLastHitForEntity(entity)
```
```c
Vector3 GET_COLLISION_NORMAL_OF_LAST_HIT_FOR_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vector3`

---
### GetEntityAlpha

`GET_ENTITY_ALPHA` · hash `0x5A47B3B5E63E94C6` · jhash `0x1560B017` · **Cliente**

```lua
local retval = GetEntityAlpha(entity)
```
```c
int GET_ENTITY_ALPHA(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

---
### GetEntityAnimCurrentTime

`GET_ENTITY_ANIM_CURRENT_TIME` · hash `0x346D81500D088F42` · jhash `0x83943F41` · **Cliente**

```lua
local retval = GetEntityAnimCurrentTime(entity, animDict, animName)
```
```c
float GET_ENTITY_ANIM_CURRENT_TIME(Entity entity, char* animDict, char* animName);
```

**Parámetros**

- `entity` (`Entity`)
- `animDict` (`char*`)
- `animName` (`char*`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns a float value representing animation's current playtime with respect to its total playtime. This value increasing in a range from [0 to 1] and wrap back to 0 when it reach 1.  
Example:  
0.000000 - mark the starting of animation.  
0.500000 - mark the midpoint of the animation.  
1.000000 - mark the end of animation.  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### GetEntityAnimTotalTime

`GET_ENTITY_ANIM_TOTAL_TIME` · hash `0x50BD2730B191E360` · jhash `0x433A9D18` · **Cliente**

```lua
local retval = GetEntityAnimTotalTime(entity, animDict, animName)
```
```c
float GET_ENTITY_ANIM_TOTAL_TIME(Entity entity, char* animDict, char* animName);
```

**Parámetros**

- `entity` (`Entity`)
- `animDict` (`char*`)
- `animName` (`char*`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns a float value representing animation's total playtime in milliseconds.  
Example:  
GET_ENTITY_ANIM_TOTAL_TIME(PLAYER_ID(),"amb@world_human_yoga@female@base","base_b")   
return 20800.000000  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### GetEntityAttachedTo

`GET_ENTITY_ATTACHED_TO` · hash `0x48C2BED9180FE123` · jhash `0xFE1589F9` · **Cliente**

```lua
local retval = GetEntityAttachedTo(entity)
```
```c
Entity GET_ENTITY_ATTACHED_TO(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Entity`

---
### GetEntityBoneCount

`_GET_ENTITY_BONE_COUNT` · hash `0xB328DCC3A3AA401B` · **Cliente**

```lua
local retval = GetEntityBoneCount(entity)
```
```c
int _GET_ENTITY_BONE_COUNT(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xB328DCC3A3AA401B` (`N_0xb328dcc3a3aa401b`)

---
### GetEntityBoneIndexByName

`GET_ENTITY_BONE_INDEX_BY_NAME` · hash `0xFB71170B7E76ACBA` · jhash `0xE4ECAC22` · **Cliente**

```lua
local retval = GetEntityBoneIndexByName(entity, boneName)
```
```c
int GET_ENTITY_BONE_INDEX_BY_NAME(Entity entity, char* boneName);
```

**Parámetros**

- `entity` (`Entity`)
- `boneName` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the index of the bone. If the bone was not found, -1 will be returned.   
list:  
pastebin.com/D7JMnX1g  
BoneNames:  
	chassis,  
	windscreen,  
	seat_pside_r,  
	seat_dside_r,  
	bodyshell,  
	suspension_lm,  
	suspension_lr,  
	platelight,  
	attach_female,  
	attach_male,  
	bonnet,  
	boot,  
	chassis_dummy,	//Center of the dummy  
	chassis_Control,	//Not found yet  
	door_dside_f,	//Door left, front  
	door_dside_r,	//Door left, back  
	door_pside_f,	//Door right, front  
	door_pside_r,	//Door right, back  
	Gun_GripR,  
	windscreen_f,  
	platelight,	//Position where the light above the numberplate is located  
	VFX_Emitter,  
	window_lf,	//Window left, front  
	window_lr,	//Window left, back  
	window_rf,	//Window right, front  
	window_rr,	//Window right, back  
	engine,	//Position of the engine  
	gun_ammo,  
	ROPE_ATTATCH,	//Not misspelled. In script "finale_heist2b.c4".  
	wheel_lf,	//Wheel left, front  
	wheel_lr,	//Wheel left, back  
	wheel_rf,	//Wheel right, front  
	wheel_rr,	//Wheel right, back  
	exhaust,	//Exhaust. shows only the position of the stock-exhaust  
	overheat,	//A position on the engine(not exactly sure, how to name it)  
	misc_e,	//Not a car-bone.  
	seat_dside_f,	//Driver-seat  
	seat_pside_f,	//Seat next to driver  
	Gun_Nuzzle,  
	seat_r  
I doubt that the function is case-sensitive, since I found a "Chassis" and a "chassis". - Just tested: Definitely not case-sensitive.  
```

---
### GetEntityBonePosition_2

`_GET_ENTITY_BONE_POSITION_2` · hash `0x46F8696933A63C9B` · **Cliente**

```lua
local retval = GetEntityBonePosition_2(entity, boneIndex)
```
```c
Vector3 _GET_ENTITY_BONE_POSITION_2(Entity entity, int boneIndex);
```

**Parámetros**

- `entity` (`Entity`)
- `boneIndex` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Gets the world rotation of the specified bone of the specified entity.
This native is used in casinoroulette.c but I don't know yet what is the difference with _GET_ENTITY_BONE_ROTATION
```

**Nombres antiguos (alias):** `0x46F8696933A63C9B` (`N_0x46f8696933a63c9b`), `_GET_WORLD_POSITION_OF_ENTITY_BONE_2` (`GetWorldPositionOfEntityBone_2`)

---
### GetEntityBoneRotation

`_GET_ENTITY_BONE_ROTATION` · hash `0xCE6294A232D03786` · **Cliente**

```lua
local retval = GetEntityBoneRotation(entity, boneIndex)
```
```c
Vector3 _GET_ENTITY_BONE_ROTATION(Entity entity, int boneIndex);
```

**Parámetros**

- `entity` (`Entity`)
- `boneIndex` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Gets the world rotation of the specified bone of the specified entity.
```

**Nombres antiguos (alias):** `0xCE6294A232D03786` (`N_0xce6294a232d03786`), `_GET_WORLD_ROTATION_OF_ENTITY_BONE` (`GetWorldRotationOfEntityBone`)

---
### GetEntityBoneRotationLocal

`_GET_ENTITY_BONE_ROTATION_LOCAL` · hash `0xBD8D32550E5CEBFE` · **Cliente**

```lua
local retval = GetEntityBoneRotationLocal(entity, boneIndex)
```
```c
Vector3 _GET_ENTITY_BONE_ROTATION_LOCAL(Entity entity, int boneIndex);
```

**Parámetros**

- `entity` (`Entity`)
- `boneIndex` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

Gets the local rotation of the specified bone of the specified entity.

```
NativeDB Introduced: v1734
```

---
### GetEntityCanBeDamaged

`GET_ENTITY_CAN_BE_DAMAGED` · hash `0xD95CC5D2AB15A09F` · jhash `0xE4938B5D` · **Cliente**

```lua
local retval = GetEntityCanBeDamaged(entity)
```
```c
BOOL GET_ENTITY_CAN_BE_DAMAGED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD95CC5D2AB15A09F` (`N_0xd95cc5d2ab15a09f`)

---
### GetEntityCollisionDisabled

`GET_ENTITY_COLLISION_DISABLED` · hash `0xCCF1E97BEFDAE480` · jhash `0xE8C0C629` · **Cliente**

```lua
local retval = GetEntityCollisionDisabled(entity)
```
```c
BOOL GET_ENTITY_COLLISION_DISABLED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xCCF1E97BEFDAE480` (`N_0xccf1e97befdae480`), `_GET_ENTITY_COLLISON_DISABLED` (`GetEntityCollisonDisabled`)

---
### GetEntityCoords

`GET_ENTITY_COORDS` · hash `0x3FEF770D40960D5A` · jhash `0x1647F1CB` · **Cliente**

```lua
local retval = GetEntityCoords(entity, alive)
```
```c
Vector3 GET_ENTITY_COORDS(Entity entity, BOOL alive);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the coordinates from.
- `alive` (`BOOL`): Unused by the game, potentially used by debug builds of GTA in order to assert whether or not an entity was alive.

**Devuelve:** `Vector3` — The current entity coordinates.

**Descripción oficial:**

Gets the current coordinates (world position) for a specified entity.

**Ejemplo (lua):**

```lua
local playerCoords = GetEntityCoords(PlayerPedId())
print(playerCoords) -- vector3(...)
```

**Ejemplo (js):**

```js
const [playerX, playerY, playerZ] = GetEntityCoords(PlayerPedId(), false);
console.log(`${playerX}, ${playerY}, ${playerZ}`);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...
Vector3 playerCoords = GetEntityCoords(PlayerPedId(), false);

// or the preferred use of C# wrapper
Vector3 playerCoords = Game.PlayerPed.Position;

Debug.WriteLine($"{playerCoords}");
```

---
### GetEntityForwardVector

`GET_ENTITY_FORWARD_VECTOR` · hash `0x0A794A5A57F8DF91` · jhash `0x84DCECBF` · **Cliente**

```lua
local retval = GetEntityForwardVector(entity)
```
```c
Vector3 GET_ENTITY_FORWARD_VECTOR(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the forward vector for.

**Devuelve:** `Vector3` — The forward vector.

**Descripción oficial:**

```
Gets the entity's forward vector.
```

---
### GetEntityForwardX

`GET_ENTITY_FORWARD_X` · hash `0x8BB4EF4214E0E6D5` · jhash `0x49FAE914` · **Cliente**

```lua
local retval = GetEntityForwardX(entity)
```
```c
float GET_ENTITY_FORWARD_X(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

**Descripción oficial:**

```
Gets the X-component of the entity's forward vector.  
```

---
### GetEntityForwardY

`GET_ENTITY_FORWARD_Y` · hash `0x866A4A5FAE349510` · jhash `0x9E2F917C` · **Cliente**

```lua
local retval = GetEntityForwardY(entity)
```
```c
float GET_ENTITY_FORWARD_Y(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

**Descripción oficial:**

```
Gets the Y-component of the entity's forward vector.  
```

---
### GetEntityHeading

`GET_ENTITY_HEADING` · hash `0xE83D4F9BA2A38914` · jhash `0x972CC383` · **Cliente**

```lua
local retval = GetEntityHeading(entity)
```
```c
float GET_ENTITY_HEADING(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the heading from.

**Devuelve:** `float` — The current entity heading.

**Descripción oficial:**

```
Returns the heading of the entity in degrees. Also know as the "Yaw" of an entity.
```

**Ejemplo (lua):**

```lua
local heading = GetEntityHeading(PlayerPedId())
print(heading)
```

**Ejemplo (js):**

```js
const heading = GetEntityHeading(PlayerPedId());
console.log(`${heading}`);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...
float heading = GetEntityHeading(PlayerPedId());

// or the preferred use of C# wrapper
float heading = Game.PlayerPed.Heading;

Debug.WriteLine($"{heading}");
```

---
### GetEntityHeadingFromEulers

`GET_ENTITY_HEADING_FROM_EULERS` · hash `0x846BF6291198A71E` · jhash `0x9320E642` · **Cliente**

```lua
local retval = GetEntityHeadingFromEulers(entity)
```
```c
float GET_ENTITY_HEADING_FROM_EULERS(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the heading from.

**Devuelve:** `float` — Returns a float representing the entity's heading from eulers.

**Descripción oficial:**

Gets the heading of the entity physics in degrees, which tends to be more accurate than just [`GET_ENTITY_HEADING`](../cfx/servidor.md#getentityheading). This can be clearly seen while, for example, ragdolling a ped/player.

**Nombres antiguos (alias):** `0x846BF6291198A71E` (`N_0x846bf6291198a71e`), `_GET_ENTITY_PHYSICS_HEADING` (`GetEntityPhysicsHeading`)

---
### GetEntityHealth

`GET_ENTITY_HEALTH` · hash `0xEEF059FAD016D209` · jhash `0x8E3222B7` · **Cliente**

```lua
local retval = GetEntityHealth(entity)
```
```c
int GET_ENTITY_HEALTH(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the health from.

**Devuelve:** `int` — The current entity health.

**Descripción oficial:**

```
Returns an integer value of entity's current health.
Example of range for ped:
- Player [0 to 200]
- Ped [100 to 200]
- Vehicle [0 to 1000]
- Object [0 to 1000]
Health is actually a float value but this native casts it to int.
In order to get the actual value, do:
float health = *(float *)(entityAddress + 0x280);
```

**Ejemplo (lua):**

```lua
local health = GetEntityHealth(PlayerPedId())
print(health)
```

**Ejemplo (js):**

```js
const health = GetEntityHealth(PlayerPedId());
console.log(`${health}`);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...
int health = GetEntityHealth(PlayerPedId());

// or the preferred use of C# wrapper
// Note: Returns 0-100 using this property.
int health = Game.PlayerPed.Health;

Debug.WriteLine($"{health}");
```

---
### GetEntityHeight

`GET_ENTITY_HEIGHT` · hash `0x5A504562485944DD` · jhash `0xEE443481` · **Cliente**

```lua
local retval = GetEntityHeight(entity, X, Y, Z, atTop, inWorldCoords)
```
```c
float GET_ENTITY_HEIGHT(Entity entity, float X, float Y, float Z, BOOL atTop, BOOL inWorldCoords);
```

**Parámetros**

- `entity` (`Entity`)
- `X` (`float`)
- `Y` (`float`)
- `Z` (`float`)
- `atTop` (`BOOL`)
- `inWorldCoords` (`BOOL`)

**Devuelve:** `float`

---
### GetEntityHeightAboveGround

`GET_ENTITY_HEIGHT_ABOVE_GROUND` · hash `0x1DD55701034110E5` · jhash `0x57F56A4D` · **Cliente**

```lua
local retval = GetEntityHeightAboveGround(entity)
```
```c
float GET_ENTITY_HEIGHT_ABOVE_GROUND(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

**Descripción oficial:**

```
Return height (z-dimension) above ground.   
Example: The pilot in a titan plane is 1.844176 above ground.  
How can i convert it to meters?  
Everything seems to be in meters, probably this too.  
```

---
### GetEntityLodDist

`GET_ENTITY_LOD_DIST` · hash `0x4159C2762B5791D6` · jhash `0x4DA3D51F` · **Cliente**

```lua
local retval = GetEntityLodDist(entity)
```
```c
int GET_ENTITY_LOD_DIST(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the LOD distance of an entity.  
```

---
### GetEntityMatrix

`GET_ENTITY_MATRIX` · hash `0xECB2FC7235A7D137` · jhash `0xEB9EB001` · **Cliente**

```lua
local forwardVector, rightVector, upVector, position = GetEntityMatrix(entity)
```
```c
void GET_ENTITY_MATRIX(Entity entity, Vector3* forwardVector, Vector3* rightVector, Vector3* upVector, Vector3* position);
```

**Parámetros**

- `entity` (`Entity`)
- `forwardVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rightVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `upVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `position` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetEntityMaxHealth

`GET_ENTITY_MAX_HEALTH` · hash `0x15D757606D170C3C` · jhash `0xC7AE6AA1` · **Cliente**

```lua
local retval = GetEntityMaxHealth(entity)
```
```c
int GET_ENTITY_MAX_HEALTH(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

**Descripción oficial:**

```
Return an integer value of entity's maximum health.  
Example:  
- Player = 200  
```

---
### GetEntityModel

`GET_ENTITY_MODEL` · hash `0x9F47B058362C84B5` · jhash `0xDAFCB3EC` · **Cliente**

```lua
local retval = GetEntityModel(entity)
```
```c
Hash GET_ENTITY_MODEL(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the model for.

**Devuelve:** `Hash` — The model hash of the entity.

**Descripción oficial:**

Returns the model hash from an entity.

**Ejemplo (lua):**

```lua
local hash = GetEntityModel(PlayerPedId())

if hash == `mp_m_freemode_01` then
    print("This player is using the male freemode model.")
end
```

**Ejemplo (js):**

```js
const hash = GetEntityModel(PlayerPedId());

if (hash === GetHashKey('mp_m_freemode_01')) {
  console.log('This player is using the male freemode model.');
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

uint hash = GetEntityModel(PlayerPedId());

if(hash == GetHashKey("mp_m_freemode_01"))
{
    Debug.WriteLine("This player is using the male freemode model.");
}

// or the preferred use of C# wrapper
if(Game.PlayerPed.Model.Hash == Game.GenerateHash("mp_m_freemode_01"))
{
    Debug.WriteLine("This player is using the male freemode model.");
}
```

---
### GetEntityPickup

`_GET_ENTITY_PICKUP` · hash `0x1F922734E259BD26` · **Cliente**

```lua
local retval = GetEntityPickup(entity, modelHash)
```
```c
Entity _GET_ENTITY_PICKUP(Entity entity, Hash modelHash);
```

**Parámetros**

- `entity` (`Entity`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Entity`

**Descripción oficial:**

```
GET_ENTITY_*

Seems to return the handle of the entity's portable pickup.

NativeDB Introduced: v1180
```

---
### GetEntityPitch

`GET_ENTITY_PITCH` · hash `0xD45DC2893621E1FE` · jhash `0xFCE6ECE5` · **Cliente**

```lua
local retval = GetEntityPitch(entity)
```
```c
float GET_ENTITY_PITCH(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

---
### GetEntityPopulationType

`GET_ENTITY_POPULATION_TYPE` · hash `0xF6F5161F4534EDFF` · jhash `0xFC30DDFF` · **Cliente**

```lua
local retval = GetEntityPopulationType(entity)
```
```c
int GET_ENTITY_POPULATION_TYPE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to obtain the population type from.

**Devuelve:** `int` — A population type, from the enumeration above.

**Descripción oficial:**

A population type, from the following enum: https://alloc8or.re/gta5/doc/enums/ePopulationType.txt

---
### GetEntityProofs

`_GET_ENTITY_PROOFS` · hash `0xBE8CD9BE829BBEBF` · **Cliente**

```lua
local retval, bulletProof, fireProof, explosionProof, collisionProof, meleeProof, steamProof, p7, drownProof = GetEntityProofs(entity)
```
```c
BOOL _GET_ENTITY_PROOFS(Entity entity, BOOL* bulletProof, BOOL* fireProof, BOOL* explosionProof, BOOL* collisionProof, BOOL* meleeProof, BOOL* steamProof, BOOL* p7, BOOL* drownProof);
```

**Parámetros**

- `entity` (`Entity`)
- `bulletProof` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `fireProof` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `explosionProof` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `collisionProof` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `meleeProof` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `steamProof` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p7` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `drownProof` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### GetEntityQuaternion

`GET_ENTITY_QUATERNION` · hash `0x7B3703D2D32DFA18` · jhash `0x5154EC90` · **Cliente**

```lua
local x, y, z, w = GetEntityQuaternion(entity)
```
```c
void GET_ENTITY_QUATERNION(Entity entity, float* x, float* y, float* z, float* w);
```

**Parámetros**

- `entity` (`Entity`)
- `x` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `y` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `z` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `w` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
w is the correct parameter name!  
```

---
### GetEntityRoll

`GET_ENTITY_ROLL` · hash `0x831E0242595560DF` · jhash `0x36610842` · **Cliente**

```lua
local retval = GetEntityRoll(entity)
```
```c
float GET_ENTITY_ROLL(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

**Descripción oficial:**

```
Displays the current ROLL axis of the entity [-180.0000/180.0000+]  
(Sideways Roll) such as a vehicle tipped on its side  
```

---
### GetEntityRotation

`GET_ENTITY_ROTATION` · hash `0xAFBD61CC738D9EB9` · jhash `0x8FF45B04` · **Cliente**

```lua
local retval = GetEntityRotation(entity, rotationOrder)
```
```c
Vector3 GET_ENTITY_ROTATION(Entity entity, int rotationOrder);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the rotation for.
- `rotationOrder` (`int`): The order yaw, pitch and roll is applied. Usually 2.

**Devuelve:** `Vector3` — A vector where the Z coordinate is the yaw.

**Descripción oficial:**

**NOTE**: What you use for rotationOrder when getting must be the same as rotationOrder when setting the rotation.

```cpp
enum eRotationOrder {
    // Rotate around the z-axis, then the y-axis and finally the x-axis.
    ROT_ZYX = 0,
    // Rotate around the y-axis, then the z-axis and finally the x-axis.
    ROT_YZX = 1,
    // Rotate around the z-axis, then the x-axis and finally the y-axis.
    ROT_ZXY = 2,
    // Rotate around the x-axis, then the z-axis and finally the y-axis.
    ROT_XZY = 3,
    // Rotate around the y-axis, then the x-axis and finally the z-axis.
    ROT_YXZ = 4,
    // Rotate around the x-axis, then the y-axis and finally the z-axis.
    ROT_XYZ = 5,
}
```

**Ejemplo (lua):**

```lua
local playerRotation = GetEntityRotation(PlayerPedId(), 2)
print(playerRotation)
```

**Ejemplo (js):**

```js
const [rotationX, rotationY, rotationZ] = GetEntityRotation(PlayerPedId(), 2);
console.log(`${rotationX} ${rotationY} ${rotationZ}`);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

Vector3 playerRotation = GetEntityRotation(Game.PlayerPed.Handle, 2);

// or the preferred use of C# wrapper
Vector3 playerRotation = Game.PlayerPed.Rotation;

Debug.WriteLine($"{playerRotation}");
```

---
### GetEntityRotationVelocity

`GET_ENTITY_ROTATION_VELOCITY` · hash `0x213B91045D09B983` · jhash `0x9BF8A73F` · **Cliente**

```lua
local retval = GetEntityRotationVelocity(entity)
```
```c
Vector3 GET_ENTITY_ROTATION_VELOCITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vector3`

---
### GetEntityScript

`GET_ENTITY_SCRIPT` · hash `0xA6E9C38DB51D7748` · jhash `0xB7F70784` · **Cliente**

```lua
local retval, script = GetEntityScript(entity, script)
```
```c
char* GET_ENTITY_SCRIPT(Entity entity, ScrHandle* script);
```

**Parámetros**

- `entity` (`Entity`)
- `script` (`ScrHandle*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `char*`

**Descripción oficial:**

```
All ambient entities in-world seem to have the same value for the second argument (Any *script), depending on when the scripthook was activated/re-activated. I've seen numbers from ~5 to almost 70 when the value was translated with to_string. The function return value seems to always be 0.  
```

---
### GetEntitySpeed

`GET_ENTITY_SPEED` · hash `0xD5037BA82E12416F` · jhash `0x9E1E4798` · **Cliente**

```lua
local retval = GetEntitySpeed(entity)
```
```c
float GET_ENTITY_SPEED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): Entity id you want to test for speed.

**Devuelve:** `float` — Speed of a entity in m/s. You can convert to km/h using the value you get and multiply by 3.6, and miles/h by 2.236936. Also, the float returned is the length of [GET_ENTITY_SPEED_VECTOR](#getentityspeedvector)

**Descripción oficial:**

Get the speed of a entity.

---
### GetEntitySpeedVector

`GET_ENTITY_SPEED_VECTOR` · hash `0x9A8D700A51CB7B0D` · jhash `0x3ED2B997` · **Cliente**

```lua
local retval = GetEntitySpeedVector(entity, relative)
```
```c
Vector3 GET_ENTITY_SPEED_VECTOR(Entity entity, BOOL relative);
```

**Parámetros**

- `entity` (`Entity`)
- `relative` (`BOOL`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Relative can be used for getting speed relative to the frame of the vehicle, to determine for example, if you are going in reverse (-y speed) or not (+y speed).  
```

---
### GetEntitySubmergedLevel

`GET_ENTITY_SUBMERGED_LEVEL` · hash `0xE81AFC1BC4CC41CE` · jhash `0x0170F68C` · **Cliente**

```lua
local retval = GetEntitySubmergedLevel(entity)
```
```c
float GET_ENTITY_SUBMERGED_LEVEL(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

**Descripción oficial:**

```
Get how much of the entity is submerged.  1.0f is whole entity.  
```

---
### GetEntityType

`GET_ENTITY_TYPE` · hash `0x8ACD366038D14505` · jhash `0x0B1BD08D` · **Cliente**

```lua
local retval = GetEntityType(entity)
```
```c
int GET_ENTITY_TYPE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns:
0 = no entity
1 = ped
2 = vehicle
3 = object
```

---
### GetEntityUprightValue

`GET_ENTITY_UPRIGHT_VALUE` · hash `0x95EED5A694951F9F` · jhash `0xF4268190` · **Cliente**

```lua
local retval = GetEntityUprightValue(entity)
```
```c
float GET_ENTITY_UPRIGHT_VALUE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

---
### GetEntityVelocity

`GET_ENTITY_VELOCITY` · hash `0x4805D2B1D8CF94A9` · jhash `0xC14C9B6B` · **Cliente**

```lua
local retval = GetEntityVelocity(entity)
```
```c
Vector3 GET_ENTITY_VELOCITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vector3`

---
### GetLastMaterialHitByEntity

`GET_LAST_MATERIAL_HIT_BY_ENTITY` · hash `0x5C3D0A935F535C4C` · jhash `0xC0E3AA47` · **Cliente**

```lua
local retval = GetLastMaterialHitByEntity(entity)
```
```c
Hash GET_LAST_MATERIAL_HIT_BY_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Hash`

---
### GetNearestPlayerToEntity

`GET_NEAREST_PLAYER_TO_ENTITY` · hash `0x7196842CB375CDB3` · jhash `0xCE17FDEC` · **Cliente**

```lua
local retval = GetNearestPlayerToEntity(entity)
```
```c
Player GET_NEAREST_PLAYER_TO_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Player`

---
### GetNearestPlayerToEntityOnTeam

`GET_NEAREST_PLAYER_TO_ENTITY_ON_TEAM` · hash `0x4DC9A62F844D9337` · jhash `0xB1808F56` · **Cliente**

```lua
local retval = GetNearestPlayerToEntityOnTeam(entity, team)
```
```c
Player GET_NEAREST_PLAYER_TO_ENTITY_ON_TEAM(Entity entity, int team);
```

**Parámetros**

- `entity` (`Entity`)
- `team` (`int`)

**Devuelve:** `Player`

---
### GetObjectIndexFromEntityIndex

`GET_OBJECT_INDEX_FROM_ENTITY_INDEX` · hash `0xD7E3B9735C0F89D6` · jhash `0xBC5A9C58` · **Cliente**

```lua
local retval = GetObjectIndexFromEntityIndex(entity)
```
```c
Object GET_OBJECT_INDEX_FROM_ENTITY_INDEX(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Object`

**Descripción oficial:**

```
Simply returns whatever is passed to it (Regardless of whether the handle is valid or not).  
```

---
### GetOffsetFromEntityGivenWorldCoords

`GET_OFFSET_FROM_ENTITY_GIVEN_WORLD_COORDS` · hash `0x2274BC1C4885E333` · jhash `0x6477EC9E` · **Cliente**

```lua
local retval = GetOffsetFromEntityGivenWorldCoords(entity, posX, posY, posZ)
```
```c
Vector3 GET_OFFSET_FROM_ENTITY_GIVEN_WORLD_COORDS(Entity entity, float posX, float posY, float posZ);
```

**Parámetros**

- `entity` (`Entity`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Converts world coords (posX - Z) to coords relative to the entity  
Example:  
posX = 50  
posY = 1000  
posZ = 60  
Entity's coords are: x=30, y=1000, z=60.  
All three returned coords will then be in range of [-20,20] depending on rotation of the entity.  
```

---
### GetOffsetFromEntityInWorldCoords

`GET_OFFSET_FROM_ENTITY_IN_WORLD_COORDS` · hash `0x1899F328B0E12848` · jhash `0xABCF043A` · **Cliente**

```lua
local retval = GetOffsetFromEntityInWorldCoords(entity, offsetX, offsetY, offsetZ)
```
```c
Vector3 GET_OFFSET_FROM_ENTITY_IN_WORLD_COORDS(Entity entity, float offsetX, float offsetY, float offsetZ);
```

**Parámetros**

- `entity` (`Entity`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Offset values are relative to the entity.  
x = left/right  
y = forward/backward  
z = up/down  
```

---
### GetPedIndexFromEntityIndex

`GET_PED_INDEX_FROM_ENTITY_INDEX` · hash `0x04A2A40C73395041` · jhash `0xC46F74AC` · **Cliente**

```lua
local retval = GetPedIndexFromEntityIndex(entity)
```
```c
Ped GET_PED_INDEX_FROM_ENTITY_INDEX(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Ped`

**Descripción oficial:**

```
Simply returns whatever is passed to it (Regardless of whether the handle is valid or not).  
```

---
### GetVehicleIndexFromEntityIndex

`GET_VEHICLE_INDEX_FROM_ENTITY_INDEX` · hash `0x4B53F92932ADFAC0` · jhash `0xC69CF43D` · **Cliente**

```lua
local retval = GetVehicleIndexFromEntityIndex(entity)
```
```c
Vehicle GET_VEHICLE_INDEX_FROM_ENTITY_INDEX(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vehicle`

**Descripción oficial:**

```
Simply returns whatever is passed to it (Regardless of whether the handle is valid or not).  
```

---
### GetWorldPositionOfEntityBone

`GET_WORLD_POSITION_OF_ENTITY_BONE` · hash `0x44A8FCB8ED227738` · jhash `0x7C6339DF` · **Cliente**

```lua
local retval = GetWorldPositionOfEntityBone(entity, boneIndex)
```
```c
Vector3 GET_WORLD_POSITION_OF_ENTITY_BONE(Entity entity, int boneIndex);
```

**Parámetros**

- `entity` (`Entity`)
- `boneIndex` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Returns the coordinates of an entity-bone.  
```

---
### HasAnimEventFired

`HAS_ANIM_EVENT_FIRED` · hash `0xEAF4CD9EA3E7E922` · jhash `0x66571CA0` · **Cliente**

```lua
local retval = HasAnimEventFired(entity, actionHash)
```
```c
BOOL HAS_ANIM_EVENT_FIRED(Entity entity, Hash actionHash);
```

**Parámetros**

- `entity` (`Entity`)
- `actionHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
if (ENTITY::HAS_ANIM_EVENT_FIRED(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("CreateObject")))
```

---
### HasCollisionLoadedAroundEntity

`HAS_COLLISION_LOADED_AROUND_ENTITY` · hash `0xE9676F61BC0B3321` · jhash `0x851687F9` · **Cliente**

```lua
local retval = HasCollisionLoadedAroundEntity(entity)
```
```c
BOOL HAS_COLLISION_LOADED_AROUND_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### HasEntityAnimFinished

`HAS_ENTITY_ANIM_FINISHED` · hash `0x20B711662962B472` · jhash `0x1D9CAB92` · **Cliente**

```lua
local retval = HasEntityAnimFinished(entity, animDict, animName, p3)
```
```c
BOOL HAS_ENTITY_ANIM_FINISHED(Entity entity, char* animDict, char* animName, int p3);
```

**Parámetros**

- `entity` (`Entity`)
- `animDict` (`char*`)
- `animName` (`char*`)
- `p3` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
P3 is always 3 as far as i cant tell  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### HasEntityBeenDamagedByAnyObject

`HAS_ENTITY_BEEN_DAMAGED_BY_ANY_OBJECT` · hash `0x95EB9964FF5C5C65` · jhash `0x6B74582E` · **Cliente**

```lua
local retval = HasEntityBeenDamagedByAnyObject(entity)
```
```c
BOOL HAS_ENTITY_BEEN_DAMAGED_BY_ANY_OBJECT(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### HasEntityBeenDamagedByAnyPed

`HAS_ENTITY_BEEN_DAMAGED_BY_ANY_PED` · hash `0x605F5A140F202491` · jhash `0x53FD4A25` · **Cliente**

```lua
local retval = HasEntityBeenDamagedByAnyPed(entity)
```
```c
BOOL HAS_ENTITY_BEEN_DAMAGED_BY_ANY_PED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### HasEntityBeenDamagedByAnyVehicle

`HAS_ENTITY_BEEN_DAMAGED_BY_ANY_VEHICLE` · hash `0xDFD5033FDBA0A9C8` · jhash `0x878C2CE0` · **Cliente**

```lua
local retval = HasEntityBeenDamagedByAnyVehicle(entity)
```
```c
BOOL HAS_ENTITY_BEEN_DAMAGED_BY_ANY_VEHICLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### HasEntityBeenDamagedByEntity

`HAS_ENTITY_BEEN_DAMAGED_BY_ENTITY` · hash `0xC86D67D52A707CF8` · jhash `0x07FC77E0` · **Cliente**

```lua
local retval = HasEntityBeenDamagedByEntity(entity, damager, bCheckDamagerVehicle)
```
```c
BOOL HAS_ENTITY_BEEN_DAMAGED_BY_ENTITY(Entity entity, Entity damager, BOOL bCheckDamagerVehicle);
```

**Parámetros**

- `entity` (`Entity`): The entity to check.
- `damager` (`Entity`): The entity that caused the damage.
- `bCheckDamagerVehicle` (`BOOL`): If the damager is driving a vehicle then check to see if the entity was damaged by the vehicle.

**Devuelve:** `BOOL` — Returns true if the entity has been damaged by the specified entity.

---
### HasEntityClearLosToEntity

`HAS_ENTITY_CLEAR_LOS_TO_ENTITY` · hash `0xFCDFF7B72D23A1AC` · jhash `0x53576FA7` · **Cliente**

```lua
local retval = HasEntityClearLosToEntity(entity1, entity2, flags)
```
```c
BOOL HAS_ENTITY_CLEAR_LOS_TO_ENTITY(Entity entity1, Entity entity2, int flags);
```

**Parámetros**

- `entity1` (`Entity`): Entity to start from
- `entity2` (`Entity`): Entity to check to
- `flags` (`int`): A bit mask with bits 1, 2, 4, etc, relating to collider types (see: [START_EXPENSIVE_SYNCHRONOUS_SHAPE_TEST_LOS_PROBE](SHAPETEST.md#startexpensivesynchronousshapetestlosprobe)). 17 is most common in GTA scripts.

**Devuelve:** `BOOL` — Returns `true` if no collider of specified bitmask is hit.

**Descripción oficial:**

Checks if entity1 has a clear line of sight to entity2. So a simple raycast which if it collides with any of the given colliderTypes returns false.

The direction of the check matters with for example bushes, so checking from inside to outside a bush with traceType 256 returns true, but the other way around returns false.

---
### HasEntityClearLosToEntityInFront

`HAS_ENTITY_CLEAR_LOS_TO_ENTITY_IN_FRONT` · hash `0x0267D00AF114F17A` · jhash `0x210D87C8` · **Cliente**

```lua
local retval = HasEntityClearLosToEntityInFront(entity1, entity2)
```
```c
BOOL HAS_ENTITY_CLEAR_LOS_TO_ENTITY_IN_FRONT(Entity entity1, Entity entity2);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Has the entity1 got a clear line of sight to the other entity2 from the direction entity1 is facing.  
This is one of the most CPU demanding BOOL natives in the game; avoid calling this in things like nested for-loops  
```

---
### HasEntityClearLosToEntity_2

`_HAS_ENTITY_CLEAR_LOS_TO_ENTITY_2` · hash `0x394BDE2A7BBA031E` · **Cliente**

```lua
local retval = HasEntityClearLosToEntity_2(entity1, entity2, traceType)
```
```c
Any _HAS_ENTITY_CLEAR_LOS_TO_ENTITY_2(Entity entity1, Entity entity2, int traceType);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)
- `traceType` (`int`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

**Nombres antiguos (alias):** `0x394BDE2A7BBA031E` (`N_0x394bde2a7bba031e`)

---
### HasEntityCollidedWithAnything

`HAS_ENTITY_COLLIDED_WITH_ANYTHING` · hash `0x8BAD02F0368D9E14` · jhash `0x662A2F41` · **Cliente**

```lua
local retval = HasEntityCollidedWithAnything(entity)
```
```c
BOOL HAS_ENTITY_COLLIDED_WITH_ANYTHING(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Called on tick.  
Tested with vehicles, returns true whenever the vehicle is touching any entity.  
Note: for vehicles, the wheels can touch the ground and it will still return false, but if the body of the vehicle touches the ground, it will return true.  
```

---
### IsAnEntity

`IS_AN_ENTITY` · hash `0x731EC8A916BD11A1` · jhash `0xD4B9715A` · **Cliente**

```lua
local retval = IsAnEntity(handle)
```
```c
BOOL IS_AN_ENTITY(int handle);
```

**Parámetros**

- `handle` (`int`)

**Devuelve:** `BOOL`

---
### IsEntityAMissionEntity

`IS_ENTITY_A_MISSION_ENTITY` · hash `0x0A7B270912999B3C` · jhash `0x2632E124` · **Cliente**

```lua
local retval = IsEntityAMissionEntity(entity)
```
```c
BOOL IS_ENTITY_A_MISSION_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityAPed

`IS_ENTITY_A_PED` · hash `0x524AC5ECEA15343E` · jhash `0x55D33EAB` · **Cliente**

```lua
local retval = IsEntityAPed(entity)
```
```c
BOOL IS_ENTITY_A_PED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to check if it's a Ped.

**Devuelve:** `BOOL` — Whether the entity is a Ped.

---
### IsEntityAVehicle

`IS_ENTITY_A_VEHICLE` · hash `0x6AC7003FA6E5575E` · jhash `0xBE800B01` · **Cliente**

```lua
local retval = IsEntityAVehicle(entity)
```
```c
BOOL IS_ENTITY_A_VEHICLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityAnObject

`IS_ENTITY_AN_OBJECT` · hash `0x8D68C8FD0FACA94E` · jhash `0x3F52E561` · **Cliente**

```lua
local retval = IsEntityAnObject(entity)
```
```c
BOOL IS_ENTITY_AN_OBJECT(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityAtCoord

`IS_ENTITY_AT_COORD` · hash `0x20B60995556D004F` · jhash `0xD749B606` · **Cliente**

```lua
local retval = IsEntityAtCoord(entity, xPos, yPos, zPos, xSize, ySize, zSize, highlightArea, do3dCheck, transportMode)
```
```c
BOOL IS_ENTITY_AT_COORD(Entity entity, float xPos, float yPos, float zPos, float xSize, float ySize, float zSize, BOOL highlightArea, BOOL do3dCheck, int transportMode);
```

**Parámetros**

- `entity` (`Entity`): The entity to check the position of
- `xPos` (`float`): The position of the square along the x-axis
- `yPos` (`float`): The position of the square along the y-axis
- `zPos` (`float`): The position of the square along the z-axis (only applicable if do3dCheck is true)
- `xSize` (`float`): The apothem of the square along the x-axis
- `ySize` (`float`): The apothem of the square along the y-axis
- `zSize` (`float`): The apothem of the square along the z-axis (only applicable if do3dCheck is true)
- `highlightArea` (`BOOL`): Whether to draw a marker (yellow cylindrical marker at the given coords)
- `do3dCheck` (`BOOL`): Whether to check the z-axis
- `transportMode` (`int`): Checks the transport mode the ped is using, only does something if entity is a ped. Transport modes are: 0 (any), 1 (on foot), 2 (in vehicle)

**Devuelve:** `BOOL` — A boolean value which represents if the entity is within the given square area.

**Descripción oficial:**

Checks if the entity is within the given square of size xSize, ySize, zSize centered around the given coordinates.

The sizes given are the apothem (half of side) of the square, so a size of 5 would result in a square of 10x10, not 5x5.

For the highlightArea, if do3dCheck is true, the marker will be drawn at the bottom of the target area. So if the square is centered on the ground with a zSize larger than 0, the marker will appear under the ground.
The marker also doesn't scale, so it is always the same size (around half a meter).
So unfortunately the marker isn't that useful as it doesn't convey the correct information about the area (the marker doesn't reflect when the player is actually in the marker or not)

**Ejemplo (lua):**

```lua
-- Simple demonstration which slides the ped along the x and y axis until the ped is outside the given area
local offset = 10
while IsEntityAtCoord(PlayerPedId(), coords.x, coords.y, coords.z, 20.0, 20.0, 20.0, false, false, 0) do
    offset += 0.1
    local targetCoords = coords + vector3(offset, offset, 0)
    SetEntityCoords(PlayerPedId(), targetCoords.x, targetCoords.y, targetCoords.z)
    Citizen.Wait(0)
end
print(i) -- Prints 20.1, as expected
```

---
### IsEntityAtEntity

`IS_ENTITY_AT_ENTITY` · hash `0x751B70C3D034E187` · jhash `0xDABDCB52` · **Cliente**

```lua
local retval = IsEntityAtEntity(entity, target, xSize, ySize, zSize, highlightArea, do3dCheck, transportMode)
```
```c
BOOL IS_ENTITY_AT_ENTITY(Entity entity, Entity target, float xSize, float ySize, float zSize, BOOL highlightArea, BOOL do3dCheck, int transportMode);
```

**Parámetros**

- `entity` (`Entity`): The source entity handle.
- `target` (`Entity`): The target entity handle.
- `xSize` (`float`): The x size of the axis aligned box around the target entity to check.
- `ySize` (`float`): The y size of the axis aligned box around the target entity to check.
- `zSize` (`float`): The z size of the axis aligned box around the target entity to check.
- `highlightArea` (`BOOL`)
- `do3dCheck` (`BOOL`): If the check should be 2d or 3d.
- `transportMode` (`int`): The transport mode. Returns early if the entity is not in that mode of transportation.

**Devuelve:** `BOOL`

**Descripción oficial:**

Checks if entity is within the specified axis aligned box around the target entity.

```cpp
enum eTransportMode {
    SCRIPT_TM_ANY = 0,
    SCRIPT_TM_ON_FOOT = 1,
    SCRIPT_TM_IN_VEHICLE = 2
};
```

---
### IsEntityAttached

`IS_ENTITY_ATTACHED` · hash `0xB346476EF1A64897` · jhash `0xEC1479D5` · **Cliente**

```lua
local retval = IsEntityAttached(entity)
```
```c
BOOL IS_ENTITY_ATTACHED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to check if it is attached to another entity.

**Devuelve:** `BOOL` — Whether the entity is attached to another entity.

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()

if IsEntityAttached(ped) then
    DetachEntity(ped, true, true)
end
```

**Ejemplo (js):**

```js
int ped = PlayerPedId();

if(IsEntityAttached(ped)) {
    DetachEntity(ped, true, true);
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

int ped = PlayerPedId();

if(IsEntityAttached(ped))
{
    DetachEntity(ped, true, true);
}

// or the preferred use of C# wrapper
if(Game.PlayerPed.IsAttached()) {
    Game.PlayerPed.Detach();
}
```

---
### IsEntityAttachedToAnyObject

`IS_ENTITY_ATTACHED_TO_ANY_OBJECT` · hash `0xCF511840CEEDE0CC` · jhash `0x0B5DE340` · **Cliente**

```lua
local retval = IsEntityAttachedToAnyObject(entity)
```
```c
BOOL IS_ENTITY_ATTACHED_TO_ANY_OBJECT(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityAttachedToAnyPed

`IS_ENTITY_ATTACHED_TO_ANY_PED` · hash `0xB1632E9A5F988D11` · jhash `0x9D7A609C` · **Cliente**

```lua
local retval = IsEntityAttachedToAnyPed(entity)
```
```c
BOOL IS_ENTITY_ATTACHED_TO_ANY_PED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityAttachedToAnyVehicle

`IS_ENTITY_ATTACHED_TO_ANY_VEHICLE` · hash `0x26AA915AD89BFB4B` · jhash `0xDE5C995E` · **Cliente**

```lua
local retval = IsEntityAttachedToAnyVehicle(entity)
```
```c
BOOL IS_ENTITY_ATTACHED_TO_ANY_VEHICLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityAttachedToEntity

`IS_ENTITY_ATTACHED_TO_ENTITY` · hash `0xEFBE71898A993728` · jhash `0xB0ABFEA8` · **Cliente**

```lua
local retval = IsEntityAttachedToEntity(from, to)
```
```c
BOOL IS_ENTITY_ATTACHED_TO_ENTITY(Entity from, Entity to);
```

**Parámetros**

- `from` (`Entity`)
- `to` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityDead

`IS_ENTITY_DEAD` · hash `0x5F9532F3B5CC2551` · jhash `0xB6F7CBAC` · **Cliente**

```lua
local retval = IsEntityDead(entity)
```
```c
BOOL IS_ENTITY_DEAD(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: BOOL p1
```

---
### IsEntityInAir

`IS_ENTITY_IN_AIR` · hash `0x886E37EC497200B6` · jhash `0xA4157987` · **Cliente**

```lua
local retval = IsEntityInAir(entity)
```
```c
BOOL IS_ENTITY_IN_AIR(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityInAngledArea

`IS_ENTITY_IN_ANGLED_AREA` · hash `0x51210CED3DA1C78A` · jhash `0x883622FA` · **Cliente**

```lua
local retval = IsEntityInAngledArea(entity, x1, y1, z1, x2, y2, z2, width, debug, includez, p10)
```
```c
BOOL IS_ENTITY_IN_ANGLED_AREA(Entity entity, float x1, float y1, float z1, float x2, float y2, float z2, float width, BOOL debug, BOOL includez, Any p10);
```

**Parámetros**

- `entity` (`Entity`)
- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area
- `debug` (`BOOL`): a debug flag invoking functions in the same path as `DRAW_MARKER`
- `includez` (`BOOL`): If true, include the Z dimension when doing the height check; otherwise the query becomes two-dimensional
- `p10` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

p10 is some entity flag check, also used in [`IS_ENTITY_AT_ENTITY`](#isentityatentity), [`IS_ENTITY_IN_AREA`](#isentityinarea) and [`IS_ENTITY_AT_COORD`](#isentityatcoord).

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

---
### IsEntityInArea

`IS_ENTITY_IN_AREA` · hash `0x54736AA40E271165` · jhash `0x8C2DFA9D` · **Cliente**

```lua
local retval = IsEntityInArea(entity, x1, y1, z1, x2, y2, z2, p7, p8, p9)
```
```c
BOOL IS_ENTITY_IN_AREA(Entity entity, float x1, float y1, float z1, float x2, float y2, float z2, BOOL p7, BOOL p8, Any p9);
```

**Parámetros**

- `entity` (`Entity`)
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)
- `p9` (`Any`)

**Devuelve:** `BOOL`

---
### IsEntityInWater

`IS_ENTITY_IN_WATER` · hash `0xCFB0A0D8EDD145A3` · jhash `0x4C3C2508` · **Cliente**

```lua
local retval = IsEntityInWater(entity)
```
```c
BOOL IS_ENTITY_IN_WATER(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityInZone

`IS_ENTITY_IN_ZONE` · hash `0xB6463CF6AF527071` · jhash `0x45C82B21` · **Cliente**

```lua
local retval = IsEntityInZone(entity, zone)
```
```c
BOOL IS_ENTITY_IN_ZONE(Entity entity, char* zone);
```

**Parámetros**

- `entity` (`Entity`)
- `zone` (`char*`)

**Devuelve:** `BOOL`

---
### IsEntityOccluded

`IS_ENTITY_OCCLUDED` · hash `0xE31C2C72B8692B64` · jhash `0x46BC5B40` · **Cliente**

```lua
local retval = IsEntityOccluded(entity)
```
```c
BOOL IS_ENTITY_OCCLUDED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityOnScreen

`IS_ENTITY_ON_SCREEN` · hash `0xE659E47AF827484B` · jhash `0xC1FEC5ED` · **Cliente**

```lua
local retval = IsEntityOnScreen(entity)
```
```c
BOOL IS_ENTITY_ON_SCREEN(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to check.

**Devuelve:** `BOOL` — Returns `true` if the the entity is in between the minimum and maximum values for the 2D screen bound coords; otherwise, `false`.

**Descripción oficial:**

Determines whether the screen position of the specified entity is within the 2D bounds of the screen.

This native will not check if the entity is not visible due to being occluded (for example, behind a wall). To check if a entity is on screen and is not occluded, use [IS_ENTITY_OCCLUDED](#isentityoccluded).

---
### IsEntityPlayingAnim

`IS_ENTITY_PLAYING_ANIM` · hash `0x1F0B79228E461EC9` · jhash `0x0D130D34` · **Cliente**

```lua
local retval = IsEntityPlayingAnim(entity, animDict, animName, taskFlag)
```
```c
BOOL IS_ENTITY_PLAYING_ANIM(Entity entity, char* animDict, char* animName, int taskFlag);
```

**Parámetros**

- `entity` (`Entity`)
- `animDict` (`char*`)
- `animName` (`char*`)
- `taskFlag` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

See also [`IS_SCRIPTED_SCENARIO_PED_USING_CONDITIONAL_ANIM`](PED-1.md#isscriptedscenariopedusingconditionalanim)

```
Taken from ENTITY::IS_ENTITY_PLAYING_ANIM(PLAYER::PLAYER_PED_ID(), "creatures@shark@move", "attack_player", 3)  
p4 is always 3 in the scripts.  
taskFlag:  
2 - Check synchronized scene  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### IsEntityStatic

`IS_ENTITY_STATIC` · hash `0x1218E6886D3D8327` · jhash `0x928E12E9` · **Cliente**

```lua
local retval = IsEntityStatic(entity)
```
```c
BOOL IS_ENTITY_STATIC(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
A static ped will not react to natives like "APPLY_FORCE_TO_ENTITY" or "SET_ENTITY_VELOCITY" and oftentimes will not react to task-natives like "AI::TASK_COMBAT_PED". The only way I know of to make one of these peds react is to ragdoll them (or sometimes to use CLEAR_PED_TASKS_IMMEDIATELY(). Static peds include almost all far-away peds, beach-combers, peds in certain scenarios, peds crossing a crosswalk, peds walking to get back into their cars, and others. If anyone knows how to make a ped non-static without ragdolling them, please edit this with the solution.  
^ Attach a phCollider to the ped.  
```

---
### IsEntityTouchingEntity

`IS_ENTITY_TOUCHING_ENTITY` · hash `0x17FFC1B2BA35A494` · jhash `0x6B931477` · **Cliente**

```lua
local retval = IsEntityTouchingEntity(entity, targetEntity)
```
```c
BOOL IS_ENTITY_TOUCHING_ENTITY(Entity entity, Entity targetEntity);
```

**Parámetros**

- `entity` (`Entity`)
- `targetEntity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityTouchingModel

`IS_ENTITY_TOUCHING_MODEL` · hash `0x0F42323798A58C8C` · jhash `0x307E7611` · **Cliente**

```lua
local retval = IsEntityTouchingModel(entity, modelHash)
```
```c
BOOL IS_ENTITY_TOUCHING_MODEL(Entity entity, Hash modelHash);
```

**Parámetros**

- `entity` (`Entity`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsEntityUpright

`IS_ENTITY_UPRIGHT` · hash `0x5333F526F6AB19AA` · jhash `0x3BCDF4E1` · **Cliente**

```lua
local retval = IsEntityUpright(entity, angle)
```
```c
BOOL IS_ENTITY_UPRIGHT(Entity entity, float angle);
```

**Parámetros**

- `entity` (`Entity`)
- `angle` (`float`)

**Devuelve:** `BOOL`

---
### IsEntityUpsidedown

`IS_ENTITY_UPSIDEDOWN` · hash `0x1DBD58820FA61D71` · jhash `0x5ACAA48F` · **Cliente**

```lua
local retval = IsEntityUpsidedown(entity)
```
```c
BOOL IS_ENTITY_UPSIDEDOWN(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityVisible

`IS_ENTITY_VISIBLE` · hash `0x47D6F43D77935C75` · jhash `0x120B4ED5` · **Cliente**

```lua
local retval = IsEntityVisible(entity)
```
```c
BOOL IS_ENTITY_VISIBLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityVisibleToScript

`IS_ENTITY_VISIBLE_TO_SCRIPT` · hash `0xD796CB5BA8F20E32` · jhash `0x5D240E9D` · **Cliente**

```lua
local retval = IsEntityVisibleToScript(entity)
```
```c
BOOL IS_ENTITY_VISIBLE_TO_SCRIPT(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsEntityWaitingForWorldCollision

`IS_ENTITY_WAITING_FOR_WORLD_COLLISION` · hash `0xD05BFF0C0A12C68F` · jhash `0x00AB7A4A` · **Cliente**

```lua
local retval = IsEntityWaitingForWorldCollision(entity)
```
```c
BOOL IS_ENTITY_WAITING_FOR_WORLD_COLLISION(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### N_0x1a092bb0c3808b96

`0x1A092BB0C3808B96` · hash `0x1A092BB0C3808B96` · **Cliente**

```lua
N_0x1a092bb0c3808b96(entity, p1)
```
```c
void 0x1A092BB0C3808B96(Entity entity, BOOL p1);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_ENTITY_*  
```

---
### N_0x352e2b5cf420bf3b

`0x352E2B5CF420BF3B` · hash `0x352E2B5CF420BF3B` · **Cliente**

```lua
N_0x352e2b5cf420bf3b(p0, p1)
```
```c
void 0x352E2B5CF420BF3B(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x36f32de87082343e

`0x36F32DE87082343E` · hash `0x36F32DE87082343E` · **Cliente**

```lua
N_0x36f32de87082343e(p0, p1)
```
```c
void 0x36F32DE87082343E(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x490861b88f4fd846

`0x490861B88F4FD846` · hash `0x490861B88F4FD846` · **Cliente**

```lua
N_0x490861b88f4fd846(p0)
```
```c
void 0x490861B88F4FD846(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing (essentially a nullsub).
```

---
### N_0x5c3b791d580e0bc2

`0x5C3B791D580E0BC2` · hash `0x5C3B791D580E0BC2` · **Cliente**

```lua
N_0x5c3b791d580e0bc2(entity, p1)
```
```c
void 0x5C3B791D580E0BC2(Entity entity, float p1);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only called once in the scripts.  
Related to weapon objects.  
```

---
### N_0x68b562e124cc0aef

`0x68B562E124CC0AEF` · hash `0x68B562E124CC0AEF` · **Cliente**

```lua
N_0x68b562e124cc0aef(p0, p1)
```
```c
void 0x68B562E124CC0AEF(Any p0, Any p1);
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
### N_0x78e8e3a640178255

`0x78E8E3A640178255` · hash `0x78E8E3A640178255` · **Cliente**

```lua
N_0x78e8e3a640178255(entity)
```
```c
void 0x78E8E3A640178255(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
Related to cutscene entities. Unsure about the use.
SET_ENTITY_*
```

---
### N_0xb17bc6453f6cf5ac

`0xB17BC6453F6CF5AC` · hash `0xB17BC6453F6CF5AC` · **Cliente**

```lua
N_0xb17bc6453f6cf5ac(p0, p1)
```
```c
void 0xB17BC6453F6CF5AC(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xc34bc448da29f5e9

`0xC34BC448DA29F5E9` · hash `0xC34BC448DA29F5E9` · **Cliente**

```lua
N_0xc34bc448da29f5e9(entity, toggle)
```
```c
void 0xC34BC448DA29F5E9(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_ENTITY_*
```

---
### N_0xcea7c8e1b48ff68c

`0xCEA7C8E1B48FF68C` · hash `0xCEA7C8E1B48FF68C` · **Cliente**

```lua
N_0xcea7c8e1b48ff68c(p0, p1)
```
```c
void 0xCEA7C8E1B48FF68C(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xe66377cddada4810

`0xE66377CDDADA4810` · hash `0xE66377CDDADA4810` · **Cliente**

```lua
N_0xe66377cddada4810(entity, p1)
```
```c
void 0xE66377CDDADA4810(Entity entity, BOOL p1);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

SET_ENTITY_M\*

```
NativeDB Introduced: v1734
```

---
### PlayEntityAnim

`PLAY_ENTITY_ANIM` · hash `0x7FB218262B810701` · jhash `0x878753D5` · **Cliente**

```lua
local retval = PlayEntityAnim(entity, animName, animDict, fBlendDelta, bLoop, bHoldLastFrame, bDriveToPose, fStartPhase, iFlags)
```
```c
BOOL PLAY_ENTITY_ANIM(Entity entity, char* animName, char* animDict, float fBlendDelta, BOOL bLoop, BOOL bHoldLastFrame, BOOL bDriveToPose, float fStartPhase, int iFlags);
```

**Parámetros**

- `entity` (`Entity`): The entity handle to play the animation on.
- `animName` (`char*`): The name of the animation to play.
- `animDict` (`char*`): The name of the animation dictionary to use.
- `fBlendDelta` (`float`): Blend in and out time.
- `bLoop` (`BOOL`): Sets `AF_LOOPING` in the flags.
- `bHoldLastFrame` (`BOOL`): Sets `AF_HOLD_LAST_FRAME` in the flags.
- `bDriveToPose` (`BOOL`): unused
- `fStartPhase` (`float`): Clamped between `0.0` and `1.0`. Sets the start phase of the animation.
- `iFlags` (`int`): The flags to use when playing the animation. See [`TASK_PLAY_ANIM`](../cfx/servidor.md#taskplayanim).

**Devuelve:** `BOOL`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### PlaySynchronizedEntityAnim

`PLAY_SYNCHRONIZED_ENTITY_ANIM` · hash `0xC77720A12FE14A86` · jhash `0x012760AA` · **Cliente**

```lua
local retval = PlaySynchronizedEntityAnim(entity, syncedScene, animName, animDictName, fBlendInDelta, fBlendOutDelta, iFlags, fMoverBlendInDelta)
```
```c
BOOL PLAY_SYNCHRONIZED_ENTITY_ANIM(Entity entity, int syncedScene, char* animName, char* animDictName, float fBlendInDelta, float fBlendOutDelta, int iFlags, float fMoverBlendInDelta);
```

**Parámetros**

- `entity` (`Entity`): The entity handle to play the animation on.
- `syncedScene` (`int`)
- `animName` (`char*`): The name of the animation to play.
- `animDictName` (`char*`): The name of the animation dictionary to use.
- `fBlendInDelta` (`float`): Blend in time.
- `fBlendOutDelta` (`float`): Blend out time.
- `iFlags` (`int`): The flags to use when playing the animation. See [`TASK_PLAY_ANIM`](../cfx/servidor.md#taskplayanim).
- `fMoverBlendInDelta` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### PlaySynchronizedMapEntityAnim

`PLAY_SYNCHRONIZED_MAP_ENTITY_ANIM` · hash `0xB9C54555ED30FBC4` · jhash `0xEB4CBA74` · **Cliente**

```lua
local retval = PlaySynchronizedMapEntityAnim(x, y, z, radius, objectModelHash, sceneId, pAnimName, pAnimDictName, fBlendDelta, fBlendOutDelta, flags, fMoverBlendInDelta)
```
```c
BOOL PLAY_SYNCHRONIZED_MAP_ENTITY_ANIM(float x, float y, float z, float radius, Hash objectModelHash, int sceneId, char* pAnimName, char* pAnimDictName, float fBlendDelta, float fBlendOutDelta, int flags, float fMoverBlendInDelta);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `objectModelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `sceneId` (`int`)
- `pAnimName` (`char*`): The name of the animation to play.
- `pAnimDictName` (`char*`): The name of the animation dictionary to use.
- `fBlendDelta` (`float`): Blend in time.
- `fBlendOutDelta` (`float`): Blend out time.
- `flags` (`int`): The flags to use when playing the animation. See [`TASK_PLAY_ANIM`](../cfx/servidor.md#taskplayanim).
- `fMoverBlendInDelta` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### ProcessEntityAttachments

`PROCESS_ENTITY_ATTACHMENTS` · hash `0xF4080490ADC51C6F` · jhash `0x6909BA59` · **Cliente**

```lua
ProcessEntityAttachments(entity)
```
```c
void PROCESS_ENTITY_ATTACHMENTS(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
Called to update entity attachments.
```

---
### RemoveForcedObject

`REMOVE_FORCED_OBJECT` · hash `0x61B6775E83C0DB6F` · jhash `0xAED73ADD` · **Cliente**

```lua
RemoveForcedObject(p0, p1, p2, p3, p4)
```
```c
void REMOVE_FORCED_OBJECT(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### RemoveModelHide

`REMOVE_MODEL_HIDE` · hash `0xD9E3006FB3CBD765` · jhash `0x993DBC10` · **Cliente**

```lua
RemoveModelHide(x, y, z, radius, model, lazy)
```
```c
void REMOVE_MODEL_HIDE(float x, float y, float z, float radius, Hash model, BOOL lazy);
```

**Parámetros**

- `x` (`float`): X Coordinate of the sphere center.
- `y` (`float`): Y Coordinate of the sphere center.
- `z` (`float`): Z Coordinate of the sphere center.
- `radius` (`float`): Radius of the sphere.
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model hash to make visible again.
- `lazy` (`BOOL`): false to apply the change immediately.

**Devuelve:** `void`

**Descripción oficial:**

Makes all objects of the specified model that were hidden using [`CREATE_MODEL_HIDE`](#createmodelhide) or [`CREATE_MODEL_HIDE_EXCLUDING_SCRIPT_OBJECTS`](#createmodelhideexcludingscriptobjects) visible again.

If lazy is false, all matching objects currently in scope are restored immediately.
If lazy is true, objects will only reappear when their map is reloaded.

**Ejemplo (lua):**

```lua
-- This could be any coordinates, in this example I am using the players ped coordinates
local playerPedCoords = GetEntityCoords(PlayerPedId())

-- Hides all entities with the hash "1437508529" within 1.0 gta units.
CreateModelHide(playerPedCoords, 1.0, 1437508529, true)

Citizen.Wait(2500)

-- This will make all hidden entities with the hash "1437508529" within 1.0 gta units visible.
RemoveModelHide(playerPedCoords, 1.0, 1437508529, false)
```

---
### RemoveModelSwap

`REMOVE_MODEL_SWAP` · hash `0x033C0F9A64E229AE` · jhash `0xCE0AA8BC` · **Cliente**

```lua
RemoveModelSwap(x, y, z, radius, oldModelHash, newModelHash, bLazy)
```
```c
void REMOVE_MODEL_SWAP(float x, float y, float z, float radius, Hash oldModelHash, Hash newModelHash, BOOL bLazy);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `oldModelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `newModelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `bLazy` (`BOOL`)

**Devuelve:** `void`

---
### ResetEntityAlpha

`RESET_ENTITY_ALPHA` · hash `0x9B1E824FFBB7027A` · jhash `0x8A30761C` · **Cliente**

```lua
ResetEntityAlpha(entity)
```
```c
void RESET_ENTITY_ALPHA(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### SetCanAutoVaultOnEntity

`SET_CAN_AUTO_VAULT_ON_ENTITY` · hash `0xE12ABE5E3A389A6C` · jhash `0x44767B31` · **Cliente**

```lua
SetCanAutoVaultOnEntity(entity, toggle)
```
```c
void SET_CAN_AUTO_VAULT_ON_ENTITY(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE12ABE5E3A389A6C` (`N_0xe12abe5e3a389a6c`)

---
### SetCanClimbOnEntity

`SET_CAN_CLIMB_ON_ENTITY` · hash `0xA80AE305E0A3044F` · jhash `0xE224A6A5` · **Cliente**

```lua
SetCanClimbOnEntity(entity, toggle)
```
```c
void SET_CAN_CLIMB_ON_ENTITY(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA80AE305E0A3044F` (`N_0xa80ae305e0a3044f`)

---
### SetEntityAlpha

`SET_ENTITY_ALPHA` · hash `0x44A0870B7E92D7C0` · jhash `0xAE667CB0` · **Cliente**

```lua
SetEntityAlpha(entity, alphaLevel, skin)
```
```c
void SET_ENTITY_ALPHA(Entity entity, int alphaLevel, BOOL skin);
```

**Parámetros**

- `entity` (`Entity`): The entity to change the alpha for.
- `alphaLevel` (`int`): The alpha level ranges from 0 to 255, but changes occur every 20% (every 51).
- `skin` (`BOOL`): Whether or not to change the alpha of the entity's skin.

**Devuelve:** `void`

**Descripción oficial:**

This native sets the entity's alpha level.

**Ejemplo (lua):**

```lua
SetEntityAlpha(PlayerPedId(), 51, false)
```

**Ejemplo (js):**

```js
SetEntityAlpha(PlayerPedId(), 51, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

SetEntityAlpha(PlayerPedId(), 51, 0);

// or the preferred use of C# wrapper
Game.PlayerPed.Opacity = 51;
```

---
### SetEntityAlwaysPrerender

`SET_ENTITY_ALWAYS_PRERENDER` · hash `0xACAD101E1FB66689` · jhash `0xD8FF798A` · **Cliente**

```lua
SetEntityAlwaysPrerender(entity, toggle)
```
```c
void SET_ENTITY_ALWAYS_PRERENDER(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityAngularVelocity

`_SET_ENTITY_ANGULAR_VELOCITY` · hash `0x8339643499D1222E` · **Cliente**

```lua
SetEntityAngularVelocity(entity, x, y, z)
```
```c
void _SET_ENTITY_ANGULAR_VELOCITY(Entity entity, float x, float y, float z);
```

**Parámetros**

- `entity` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x8339643499D1222E` (`N_0x8339643499d1222e`)

---
### SetEntityAnimCurrentTime

`SET_ENTITY_ANIM_CURRENT_TIME` · hash `0x4487C259F0F70977` · jhash `0x99D90735` · **Cliente**

```lua
SetEntityAnimCurrentTime(entity, animDictionary, animName, time)
```
```c
void SET_ENTITY_ANIM_CURRENT_TIME(Entity entity, char* animDictionary, char* animName, float time);
```

**Parámetros**

- `entity` (`Entity`)
- `animDictionary` (`char*`)
- `animName` (`char*`)
- `time` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### SetEntityAnimSpeed

`SET_ENTITY_ANIM_SPEED` · hash `0x28D1A16553C51776` · jhash `0x3990C90A` · **Cliente**

```lua
SetEntityAnimSpeed(entity, animDictionary, animName, speedMultiplier)
```
```c
void SET_ENTITY_ANIM_SPEED(Entity entity, char* animDictionary, char* animName, float speedMultiplier);
```

**Parámetros**

- `entity` (`Entity`)
- `animDictionary` (`char*`)
- `animName` (`char*`)
- `speedMultiplier` (`float`)

**Devuelve:** `void`

---
### SetEntityAsMissionEntity

`SET_ENTITY_AS_MISSION_ENTITY` · hash `0xAD738C3085FE7E11` · jhash `0x5D1F9E0F` · **Cliente**

```lua
SetEntityAsMissionEntity(entity, scriptHostObject, bGrabFromOtherScript)
```
```c
void SET_ENTITY_AS_MISSION_ENTITY(Entity entity, BOOL scriptHostObject, BOOL bGrabFromOtherScript);
```

**Parámetros**

- `entity` (`Entity`): An entity handle.
- `scriptHostObject` (`BOOL`): Whether or not to assign script info to this entity, if set to false the entity will only be protected from despawning locally.
- `bGrabFromOtherScript` (`BOOL`): Changes the entity so it's owned by the current script if the entity is already a mission entity. This will only work on entities the machine has control of (non-remote entities).

**Devuelve:** `void`

**Descripción oficial:**

Assigns an existing entity to be owned by the current script. If the entity was not owned by a script yet, this also means the entity will remain persistent until released.

Note that this is not needed right after creating an entity as a script-created entity will automatically be assigned.

---
### SetEntityAsNoLongerNeeded

`SET_ENTITY_AS_NO_LONGER_NEEDED` · hash `0xB736A491E64A32CF` · jhash `0xADF2267C` · **Cliente**

```lua
local entity = SetEntityAsNoLongerNeeded(entity)
```
```c
void SET_ENTITY_AS_NO_LONGER_NEEDED(Entity* entity);
```

**Parámetros**

- `entity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Marks the specified entity (ped, vehicle or object) as no longer needed.  
Entities marked as no longer needed, will be deleted as the engine sees fit.  
```

---
### SetEntityCanBeDamaged

`SET_ENTITY_CAN_BE_DAMAGED` · hash `0x1760FFA8AB074D66` · jhash `0x60B6E744` · **Cliente**

```lua
SetEntityCanBeDamaged(entity, toggle)
```
```c
void SET_ENTITY_CAN_BE_DAMAGED(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityCanBeDamagedByRelationshipGroup

`SET_ENTITY_CAN_BE_DAMAGED_BY_RELATIONSHIP_GROUP` · hash `0xE22D8FDE858B8119` · jhash `0x34165B5D` · **Cliente**

```lua
SetEntityCanBeDamagedByRelationshipGroup(entity, bCanBeDamaged, relGroup)
```
```c
void SET_ENTITY_CAN_BE_DAMAGED_BY_RELATIONSHIP_GROUP(Entity entity, BOOL bCanBeDamaged, int relGroup);
```

**Parámetros**

- `entity` (`Entity`)
- `bCanBeDamaged` (`BOOL`)
- `relGroup` (`int`)

**Devuelve:** `void`

---
### SetEntityCanBeTargetedWithoutLos

`SET_ENTITY_CAN_BE_TARGETED_WITHOUT_LOS` · hash `0xD3997889736FD899` · jhash `0x3B13797C` · **Cliente**

```lua
SetEntityCanBeTargetedWithoutLos(entity, toggle)
```
```c
void SET_ENTITY_CAN_BE_TARGETED_WITHOUT_LOS(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets whether the entity can be targeted without being in line-of-sight.  
```

---
### SetEntityCleanupByEngine

`_SET_ENTITY_CLEANUP_BY_ENGINE` · hash `0x3910051CCECDB00C` · jhash `0xD3850671` · **Cliente**

```lua
SetEntityCleanupByEngine(entity, toggle)
```
```c
void _SET_ENTITY_CLEANUP_BY_ENGINE(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
True means it can be deleted by the engine when switching lobbies/missions/etc, false means the script is expected to clean it up.
```

**Nombres antiguos (alias):** `0x3910051CCECDB00C` (`N_0x3910051ccecdb00c`), `_SET_ENTITY_REGISTER` (`SetEntityRegister`), `_SET_ENTITY_SOMETHING` (`SetEntitySomething`)

---
### SetEntityCollision

`SET_ENTITY_COLLISION` · hash `0x1A9205C1B9EE827F` · jhash `0x139FD37D` · **Cliente**

```lua
SetEntityCollision(entity, toggle, keepPhysics)
```
```c
void SET_ENTITY_COLLISION(Entity entity, BOOL toggle, BOOL keepPhysics);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)
- `keepPhysics` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityCompletelyDisableCollision

`SET_ENTITY_COMPLETELY_DISABLE_COLLISION` · hash `0x9EBC85ED0FFFE51C` · jhash `0xBD0D4831` · **Cliente**

```lua
SetEntityCompletelyDisableCollision(entity, toggle, keepPhysics)
```
```c
void SET_ENTITY_COMPLETELY_DISABLE_COLLISION(Entity entity, BOOL toggle, BOOL keepPhysics);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)
- `keepPhysics` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9EBC85ED0FFFE51C` (`N_0x9ebc85ed0fffe51c`), `_SET_ENTITY_COLLISION_2` (`SetEntityCollision_2`)

---
### SetEntityCoords

`SET_ENTITY_COORDS` · hash `0x06843DA7060A026B` · jhash `0xDF70B41B` · **Cliente · también en el servidor (RPC)**

```lua
SetEntityCoords(entity, xPos, yPos, zPos, alive, deadFlag, ragdollFlag, clearArea)
```
```c
void SET_ENTITY_COORDS(Entity entity, float xPos, float yPos, float zPos, BOOL alive, BOOL deadFlag, BOOL ragdollFlag, BOOL clearArea);
```

**Parámetros**

- `entity` (`Entity`): The entity to change coordinates for.
- `xPos` (`float`): The X coordinate.
- `yPos` (`float`): The Y coordinate.
- `zPos` (`float`): The Z coordinate, ground level.
- `alive` (`BOOL`): Unused by the game, potentially used by debug builds of GTA in order to assert whether or not an entity was alive.
- `deadFlag` (`BOOL`): Whether to disable physics for dead peds, too, and not just living peds.
- `ragdollFlag` (`BOOL`): A special flag used for ragdolling peds.
- `clearArea` (`BOOL`): Whether to clear any entities in the target area.

**Devuelve:** `void`

**Descripción oficial:**

Sets the coordinates (world position) for a specified entity, offset by the radius of the entity on the Z axis.

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
local currentPos = GetEntityCoords(ped)
print(currentPos)

SetEntityCoords(ped, 674.883, 548.269, 133.94, false, false, false, true)

currentPos = GetEntityCoords(ped)
print(currentPos) -- changed!
```

**Ejemplo (js):**

```js
const ped = PlayerPedId();
let currentPos = GetEntityCoords(ped, false);
console.log(`${currentPos[0]} ${currentPos[1]} ${currentPos[2]}`);

SetEntityCoords(ped, 674.883, 548.269, 133.94, false, false, false, true);

currentPos = GetEntityCoords(ped, false);
console.log(`${currentPos[0]} ${currentPos[1]} ${currentPos[2]}`); // changed!
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

int ped = PlayerPedId();
Vector3 currentPos = GetEntityCoords(ped, false);
Debug.WriteLine($"{currentPos}");

SetEntityCoords(ped, 674.883f, 548.269f, 133.94f, false, false, false, true);

currentPos = GetEntityCoords(ped, false);
Debug.WriteLine($"{currentPos}"); // changed!

// or the preferred use of C# wrapper
Debug.WriteLine($"{Game.PlayerPed.Position}");

Game.PlayerPed.Position = new Vector3(674.883f, 548.269f, 133.94f);

Debug.WriteLine($"{Game.PlayerPed.Position}"); // changed!
```

---
### SetEntityCoordsNoOffset

`SET_ENTITY_COORDS_NO_OFFSET` · hash `0x239A3351AC1DA385` · jhash `0x4C83DE8D` · **Cliente**

```lua
SetEntityCoordsNoOffset(entity, x, y, z, keepTasks, keepIK, doWarp)
```
```c
void SET_ENTITY_COORDS_NO_OFFSET(Entity entity, float x, float y, float z, BOOL keepTasks, BOOL keepIK, BOOL doWarp);
```

**Parámetros**

- `entity` (`Entity`): The entity to reposition.
- `x` (`float`): X coordinate for the new position.
- `y` (`float`): Y coordinate for the new position.
- `z` (`float`): Z coordinate for the new position.
- `keepTasks` (`BOOL`): If `true`, the tasks currently assigned to the ped are not removed upon teleportation. Applies only to peds.
- `keepIK` (`BOOL`): If `true`, the Inverse Kinematics (IK) on the ped are not reset upon teleportation. Applies only to peds.
- `doWarp` (`BOOL`): If `false`, the entity will maintain continuous motion and will not clear contacts nor create space for itself upon teleportation.

**Devuelve:** `void`

**Descripción oficial:**

Teleports an entity to specified coordinates directly, with options to maintain certain behaviors post-teleportation.

**Note**:

*   This native allows precise placement of entities without the usual adjustments for collision or interaction with the environment that may occur with other teleportation natives.
*   The `keepTasks` and `keepIK` parameters are specifically useful for maintaining the current state of a ped, ensuring actions or animations are not abruptly stopped due to the teleportation.
*   Setting `doWarp` to `false` is useful when simulating continuous movement or when the entity should interact with its immediate surroundings upon arrival.

---
### SetEntityCoordsWithoutPlantsReset

`SET_ENTITY_COORDS_WITHOUT_PLANTS_RESET` · hash `0x621873ECE1178967` · jhash `0x749B282E` · **Cliente**

```lua
SetEntityCoordsWithoutPlantsReset(entity, xPos, yPos, zPos, alive, deadFlag, ragdollFlag, clearArea)
```
```c
void SET_ENTITY_COORDS_WITHOUT_PLANTS_RESET(Entity entity, float xPos, float yPos, float zPos, BOOL alive, BOOL deadFlag, BOOL ragdollFlag, BOOL clearArea);
```

**Parámetros**

- `entity` (`Entity`)
- `xPos` (`float`)
- `yPos` (`float`)
- `zPos` (`float`)
- `alive` (`BOOL`)
- `deadFlag` (`BOOL`)
- `ragdollFlag` (`BOOL`)
- `clearArea` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_ENTITY_COORDS_2` (`SetEntityCoords_2`)

---
### SetEntityDecalsDisabled

`_SET_ENTITY_DECALS_DISABLED` · hash `0x2C2E3DC128F44309` · **Cliente**

```lua
SetEntityDecalsDisabled(entity, p1)
```
```c
void _SET_ENTITY_DECALS_DISABLED(Entity entity, BOOL p1);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_ENTITY_*
```

**Nombres antiguos (alias):** `0x2C2E3DC128F44309` (`N_0x2c2e3dc128f44309`)

---
### SetEntityDynamic

`SET_ENTITY_DYNAMIC` · hash `0x1718DE8E3F2823CA` · jhash `0x236F525B` · **Cliente**

```lua
SetEntityDynamic(entity, toggle)
```
```c
void SET_ENTITY_DYNAMIC(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityHasGravity

`SET_ENTITY_HAS_GRAVITY` · hash `0x4A4722448F18EEF5` · jhash `0xE2F262BF` · **Cliente**

```lua
SetEntityHasGravity(entity, toggle)
```
```c
void SET_ENTITY_HAS_GRAVITY(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityHeading

`SET_ENTITY_HEADING` · hash `0x8E2530AA8ADA980E` · jhash `0xE0FF064D` · **Cliente · también en el servidor (RPC)**

```lua
SetEntityHeading(entity, heading)
```
```c
void SET_ENTITY_HEADING(Entity entity, float heading);
```

**Parámetros**

- `entity` (`Entity`): The entity to set the heading for.
- `heading` (`float`): The heading in degrees.

**Devuelve:** `void`

**Descripción oficial:**

Set the heading of an entity in degrees also known as "Yaw".

**Ejemplo (lua):**

```lua
SetEntityHeading(PlayerPedId(), 40.0)
```

**Ejemplo (js):**

```js
SetEntityHeading(PlayerPedId(), 40);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

SetEntityHeading(PlayerPedId(), 40.0f);

// or the preferred use of C# wrapper
Game.PlayerPed.Heading = 40.0f;
```

---
### SetEntityHealth

`SET_ENTITY_HEALTH` · hash `0x6B76DC1F3AE6E6A3` · jhash `0xFBCD1831` · **Cliente**

```lua
SetEntityHealth(entity, health)
```
```c
void SET_ENTITY_HEALTH(Entity entity, int health);
```

**Parámetros**

- `entity` (`Entity`): The entity handle.
- `health` (`int`): The health we should set this entity to.

**Devuelve:** `void`

**Descripción oficial:**

When setting health for a player ped, the game will clamp the health value to ensure it does not exceed the maximum health. This maximum health can be retrieved by calling [`GET_PED_MAX_HEALTH`](../cfx/servidor.md#getpedmaxhealth). It can also be modified by calling [`SET_PED_MAX_HEALTH`](PED-1.md#setpedmaxhealth).

When setting the health for non-player peds or entities, the maximum health will be increased if the new health value exceeds the current maximum.

Default health for male peds is `200`, for female peds it is `175`.

**Added parameters**

*   **inflictor**: The handle for the entity that caused the damage.

---
### SetEntityInvincible

`SET_ENTITY_INVINCIBLE` · hash `0x3882114BDE571AD4` · jhash `0xC1213A21` · **Cliente**

```lua
SetEntityInvincible(entity, toggle)
```
```c
void SET_ENTITY_INVINCIBLE(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets a ped or an object totally invincible. It doesn't take any kind of damage. Peds will not ragdoll on explosions and the tazer animation won't apply either.  
If you use this for a ped and you want Ragdoll to stay enabled, then do:  
*(DWORD *)(pedAddress + 0x188) |= (1 << 9);  
Use this if you want to get the invincibility status:  
	bool IsPedInvincible(Ped ped)  
	{  
auto addr = getScriptHandleBaseAddress(ped);	  
if (addr)  
{  
	DWORD flag = *(DWORD *)(addr + 0x188);  
	return ((flag & (1 << 8)) != 0) || ((flag & (1 << 9)) != 0);  
}  
return false;  
	}  
```

---
### SetEntityIsTargetPriority

`SET_ENTITY_IS_TARGET_PRIORITY` · hash `0xEA02E132F5C68722` · jhash `0x9729EE32` · **Cliente**

```lua
SetEntityIsTargetPriority(entity, p1, p2)
```
```c
void SET_ENTITY_IS_TARGET_PRIORITY(Entity entity, BOOL p1, float p2);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`BOOL`)
- `p2` (`float`)

**Devuelve:** `void`

---
### SetEntityLights

`SET_ENTITY_LIGHTS` · hash `0x7CFBA6A80BDF3874` · jhash `0xE8FC85AF` · **Cliente**

```lua
SetEntityLights(entity, toggle)
```
```c
void SET_ENTITY_LIGHTS(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`): To turn the lights on, set to "false". To turn the lights off, set to "true".

**Devuelve:** `void`

---
### SetEntityLoadCollisionFlag

`SET_ENTITY_LOAD_COLLISION_FLAG` · hash `0x0DC7CABAB1E9B67E` · jhash `0xC52F295B` · **Cliente**

```lua
SetEntityLoadCollisionFlag(entity, toggle)
```
```c
void SET_ENTITY_LOAD_COLLISION_FLAG(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Loads collision grid for an entity spawned outside of a player's loaded area. This allows peds to execute tasks rather than sit dormant because of a lack of a physics grid.

Certainly not the main usage of this native but when set to true for a Vehicle, it will prevent the vehicle to explode if it is spawned far away from the player.

```
NativeDB Added Parameter 3: Any p2
```

---
### SetEntityLodDist

`SET_ENTITY_LOD_DIST` · hash `0x5927F96A78577363` · jhash `0xD7ACC7AD` · **Cliente**

```lua
SetEntityLodDist(entity, value)
```
```c
void SET_ENTITY_LOD_DIST(Entity entity, int value);
```

**Parámetros**

- `entity` (`Entity`)
- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
LOD distance can be 0 to 0xFFFF (higher values will result in 0xFFFF) as it is actually stored as a 16-bit value (aka uint16_t).  
```

---
### SetEntityMaxHealth

`SET_ENTITY_MAX_HEALTH` · hash `0x166E7CF68597D8B5` · jhash `0x96F84DF8` · **Cliente**

```lua
SetEntityMaxHealth(entity, value)
```
```c
void SET_ENTITY_MAX_HEALTH(Entity entity, int value);
```

**Parámetros**

- `entity` (`Entity`)
- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
For instance: ENTITY::SET_ENTITY_MAX_HEALTH(PLAYER::PLAYER_PED_ID(), 200); // director_mode.c4: 67849  
```

---
### SetEntityMaxSpeed

`SET_ENTITY_MAX_SPEED` · hash `0x0E46A3FCBDE2A1B1` · jhash `0x46AFFED3` · **Cliente**

```lua
SetEntityMaxSpeed(entity, speed)
```
```c
void SET_ENTITY_MAX_SPEED(Entity entity, float speed);
```

**Parámetros**

- `entity` (`Entity`): Entity to apply a maximum speed on
- `speed` (`float`): Speed in meters per second

**Devuelve:** `void`

---
### SetEntityMotionBlur

`SET_ENTITY_MOTION_BLUR` · hash `0x295D82A8559F9150` · jhash `0xE90005B8` · **Cliente**

```lua
SetEntityMotionBlur(entity, toggle)
```
```c
void SET_ENTITY_MOTION_BLUR(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityNoCollisionEntity

`SET_ENTITY_NO_COLLISION_ENTITY` · hash `0xA53ED5520C07654A` · jhash `0x1E11BFE9` · **Cliente**

```lua
SetEntityNoCollisionEntity(entity1, entity2, thisFrameOnly)
```
```c
void SET_ENTITY_NO_COLLISION_ENTITY(Entity entity1, Entity entity2, BOOL thisFrameOnly);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)
- `thisFrameOnly` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Calling this function disables collision between two entities.
The importance of the order for entity1 and entity2 is unclear.
The third parameter, `thisFrame`, decides whether the collision is to be disabled until it is turned back on, or if it's just this frame.
```

---
### SetEntityNoCollisionWithNetworkedEntity

`_SET_ENTITY_NO_COLLISION_WITH_NETWORKED_ENTITY` · hash `0x0A27A7827347B3B1` · **Cliente**

```lua
SetEntityNoCollisionWithNetworkedEntity(entity1, entity2)
```
```c
void _SET_ENTITY_NO_COLLISION_WITH_NETWORKED_ENTITY(Entity entity1, Entity entity2);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### SetEntityOnlyDamagedByPlayer

`SET_ENTITY_ONLY_DAMAGED_BY_PLAYER` · hash `0x79F020FF9EDC0748` · jhash `0x4B707F50` · **Cliente**

```lua
SetEntityOnlyDamagedByPlayer(entity, toggle)
```
```c
void SET_ENTITY_ONLY_DAMAGED_BY_PLAYER(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityOnlyDamagedByRelationshipGroup

`SET_ENTITY_ONLY_DAMAGED_BY_RELATIONSHIP_GROUP` · hash `0x7022BD828FA0B082` · jhash `0x202237E2` · **Cliente**

```lua
SetEntityOnlyDamagedByRelationshipGroup(entity, p1, relationshipHash)
```
```c
void SET_ENTITY_ONLY_DAMAGED_BY_RELATIONSHIP_GROUP(Entity entity, BOOL p1, Hash relationshipHash);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`BOOL`)
- `relationshipHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### SetEntityProofs

`SET_ENTITY_PROOFS` · hash `0xFAEE099C6F890BB8` · jhash `0x7E9EAB66` · **Cliente**

```lua
SetEntityProofs(entity, bulletProof, fireProof, explosionProof, collisionProof, meleeProof, steamProof, p7, drownProof)
```
```c
void SET_ENTITY_PROOFS(Entity entity, BOOL bulletProof, BOOL fireProof, BOOL explosionProof, BOOL collisionProof, BOOL meleeProof, BOOL steamProof, BOOL p7, BOOL drownProof);
```

**Parámetros**

- `entity` (`Entity`)
- `bulletProof` (`BOOL`)
- `fireProof` (`BOOL`)
- `explosionProof` (`BOOL`)
- `collisionProof` (`BOOL`)
- `meleeProof` (`BOOL`)
- `steamProof` (`BOOL`)
- `p7` (`BOOL`)
- `drownProof` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enable / disable each type of damage.  
--------------  
p7 is to to '1' in am_mp_property_ext/int: entity::set_entity_proofs(uParam0->f_19, true, true, true, true, true, true, 1, true);  
```

---
### SetEntityQuaternion

`SET_ENTITY_QUATERNION` · hash `0x77B21BE7AC540F07` · jhash `0x83B6046F` · **Cliente**

```lua
SetEntityQuaternion(entity, x, y, z, w)
```
```c
void SET_ENTITY_QUATERNION(Entity entity, float x, float y, float z, float w);
```

**Parámetros**

- `entity` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `w` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
w is the correct parameter name!  
```

---
### SetEntityRecordsCollisions

`SET_ENTITY_RECORDS_COLLISIONS` · hash `0x0A50A1EEDAD01E65` · jhash `0x6B189A1A` · **Cliente**

```lua
SetEntityRecordsCollisions(entity, toggle)
```
```c
void SET_ENTITY_RECORDS_COLLISIONS(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityRenderScorched

`SET_ENTITY_RENDER_SCORCHED` · hash `0x730F5F8D3F0F2050` · jhash `0xAAC9317B` · **Cliente**

```lua
SetEntityRenderScorched(entity, toggle)
```
```c
void SET_ENTITY_RENDER_SCORCHED(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEntityRequiresMoreExpensiveRiverCheck

`SET_ENTITY_REQUIRES_MORE_EXPENSIVE_RIVER_CHECK` · hash `0x694E00132F2823ED` · jhash `0x40C84A74` · **Cliente**

```lua
SetEntityRequiresMoreExpensiveRiverCheck(entity, toggle)
```
```c
void SET_ENTITY_REQUIRES_MORE_EXPENSIVE_RIVER_CHECK(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x694E00132F2823ED` (`N_0x694e00132f2823ed`)

---
### SetEntityRotation

`SET_ENTITY_ROTATION` · hash `0x8524A8B0171D5E07` · jhash `0x0A345EFE` · **Cliente · también en el servidor (RPC)**

```lua
SetEntityRotation(entity, pitch, roll, yaw, rotationOrder, bDeadCheck)
```
```c
void SET_ENTITY_ROTATION(Entity entity, float pitch, float roll, float yaw, int rotationOrder, BOOL bDeadCheck);
```

**Parámetros**

- `entity` (`Entity`): The entity to rotate.
- `pitch` (`float`): The pitch (X-axis) rotation in degrees.
- `roll` (`float`): The roll (Y-axis) rotation in degrees.
- `yaw` (`float`): The yaw (Z-axis) rotation in degrees.
- `rotationOrder` (`int`): Specifies the order in which yaw, pitch, and roll are applied, see [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation) for the available rotation orders.
- `bDeadCheck` (`BOOL`): Usually set to `true`. Determines whether to check if the entity is dead before applying the rotation.

**Devuelve:** `void`

**Descripción oficial:**

Sets the rotation of a specified entity in the game world.

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
-- Example of rotating a vehicle 360 degrees
RegisterCommand('360', function()
    local playerPed = PlayerPedId() -- Get the player's Ped
    local vehicle = GetVehiclePedIsIn(playerPed, false) -- Get the vehicle the player is currently in.
    if not vehicle or not DoesEntityExist(vehicle) then
        print("You are not in a vehicle")
        return
    end
    
    local rot = GetEntityRotation(vehicle, 2)
    local roll, pitch, yaw = rot.x, rot.y, rot.z
    local finalYaw = yaw + 360
    local steps = 20 -- Reduced the number of steps so each rotation is larger
    -- Function to perform the rotation gradually
    local function doRotation()
        local currentYaw = yaw
        -- Loop to adjust the rotation in steps
        for i = 1, steps do
            Citizen.Wait(20) -- Increases the delay between each adjustment to make the animation slower
            currentYaw = currentYaw + (360 / steps) -- Increments the rotation
            if currentYaw >= finalYaw then
                currentYaw = finalYaw
            end
            -- Apply the current rotation
            SetEntityRotation(vehicle, roll, pitch, currentYaw % 360, 2, true)
            if currentYaw == finalYaw then
                break -- Stops the loop once the rotation is complete
            end
        end
    end
    -- Execute the rotation in a coroutine to not block the main thread
    Citizen.CreateThread(doRotation)
end, false)
```

---
### SetEntityTrafficlightOverride

`SET_ENTITY_TRAFFICLIGHT_OVERRIDE` · hash `0x57C5DB656185EAC4` · jhash `0xC47F5B91` · **Cliente**

```lua
SetEntityTrafficlightOverride(entity, state)
```
```c
void SET_ENTITY_TRAFFICLIGHT_OVERRIDE(Entity entity, int state);
```

**Parámetros**

- `entity` (`Entity`)
- `state` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Changing traffic-lights will not change the behavior of NPCs.

Example: [here](https://www.gtaforums.com/topic/830463-help-with-turning-lights-green-and-causing-peds-to-crash-into-each-other/#entry1068211340)

```cpp
enum eTrafficlightOverrideMode
{
    TLO_RED = 0,
    TLO_AMBER = 1,
    TLO_GREEN = 2,
    TLO_NONE = 3
}
```

---
### SetEntityVelocity

`SET_ENTITY_VELOCITY` · hash `0x1C99BB7B6E96D16F` · jhash `0xFF5A1988` · **Cliente · también en el servidor (RPC)**

```lua
SetEntityVelocity(entity, x, y, z)
```
```c
void SET_ENTITY_VELOCITY(Entity entity, float x, float y, float z);
```

**Parámetros**

- `entity` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Note that the third parameter(denoted as z) is "up and down" with positive numbers encouraging upwards movement.
```

---
### SetEntityVisible

`SET_ENTITY_VISIBLE` · hash `0xEA1C610A04DB6BBB` · jhash `0xD043E8E1` · **Cliente**

```lua
SetEntityVisible(entity, toggle, unk)
```
```c
void SET_ENTITY_VISIBLE(Entity entity, BOOL toggle, BOOL unk);
```

**Parámetros**

- `entity` (`Entity`): The entity to change the visibility of
- `toggle` (`BOOL`): Whether or not the entity will be visible
- `unk` (`BOOL`): Always 0 in scripts

**Devuelve:** `void`

**Descripción oficial:**

Toggle the visibility of a given entity.

**Ejemplo (lua):**

```lua
SetEntityVisible(PlayerPedId(), false, 0)
```

---
### SetObjectAsNoLongerNeeded

`SET_OBJECT_AS_NO_LONGER_NEEDED` · hash `0x3AE22DEB5BA5A3E6` · jhash `0x3F6B949F` · **Cliente**

```lua
local object = SetObjectAsNoLongerNeeded(object)
```
```c
void SET_OBJECT_AS_NO_LONGER_NEEDED(Object* object);
```

**Parámetros**

- `object` (`Object*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
This is an alias of SET_ENTITY_AS_NO_LONGER_NEEDED.  
```

---
### SetPedAsNoLongerNeeded

`SET_PED_AS_NO_LONGER_NEEDED` · hash `0x2595DD4236549CE3` · jhash `0x9A388380` · **Cliente**

```lua
local ped = SetPedAsNoLongerNeeded(ped)
```
```c
void SET_PED_AS_NO_LONGER_NEEDED(Ped* ped);
```

**Parámetros**

- `ped` (`Ped*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
This is an alias of SET_ENTITY_AS_NO_LONGER_NEEDED.  
```

---
### SetPickUpByCargobobDisabled

`SET_PICK_UP_BY_CARGOBOB_DISABLED` · hash `0xD7B80E7C3BEFC396` · **Cliente**

```lua
SetPickUpByCargobobDisabled(entity, toggle)
```
```c
void SET_PICK_UP_BY_CARGOBOB_DISABLED(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`): The entity to be configured for pick up by Cargobob.
- `toggle` (`BOOL`): A boolean value where `true` prevents the entity from being picked up by Cargobobs, and `false` allows it.

**Devuelve:** `void`

**Descripción oficial:**

Configures an entity to either allow or prevent it from being picked up by Cargobobs.

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0xD7B80E7C3BEFC396` (`N_0xd7b80e7c3befc396`)

**Ejemplo (lua):**

```lua
-- This example prevents a entity (in this example the vehicle of the player) from being picked up by any Cargobobs.

-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the player's vehicle (cargobob)
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if not DoesEntityExist(vehicle) then
    -- If the vehicle does not exist, end the execution of the code here.
    return
end

-- Prevent the vehicle from being picked up by Cargobobs.
SetPickUpByCargobobDisabled(vehicle, true)
```

**Ejemplo (js):**

```js
// This example prevents a entity (in this example the vehicle of the player) from being picked up by any Cargobobs.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the player's vehicle.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// Prevent the vehicle from being picked up by Cargobobs.
SetPickUpByCargobobDisabled(vehicle, true);
```

**Ejemplo (cs):**

```cs
// This example prevents a entity (in this example the vehicle of the player) from being picked up by any Cargobobs.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the player's vehicle.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// Prevent the vehicle from being picked up by Cargobobs.
SetPickUpByCargobobDisabled(vehicle, true);
```

---
### SetVehicleAsNoLongerNeeded

`SET_VEHICLE_AS_NO_LONGER_NEEDED` · hash `0x629BFA74418D6239` · jhash `0x9B0E10BE` · **Cliente**

```lua
local vehicle = SetVehicleAsNoLongerNeeded(vehicle)
```
```c
void SET_VEHICLE_AS_NO_LONGER_NEEDED(Vehicle* vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
This is an alias of SET_ENTITY_AS_NO_LONGER_NEEDED.  
```

---
### SetWaitForCollisionsBeforeProbe

`SET_WAIT_FOR_COLLISIONS_BEFORE_PROBE` · hash `0xDC6F8601FAF2E893` · jhash `0xA0466A69` · **Cliente**

```lua
SetWaitForCollisionsBeforeProbe(entity, toggle)
```
```c
void SET_WAIT_FOR_COLLISIONS_BEFORE_PROBE(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_*
Only called within 1 script for x360. 'fm_mission_controller' and it used on an object.
Ran after these 2 natives,
set_object_targettable(uParam0, 0);
set_entity_invincible(uParam0, 1);
```

**Nombres antiguos (alias):** `0xDC6F8601FAF2E893` (`N_0xdc6f8601faf2e893`)

---
### StopEntityAnim

`STOP_ENTITY_ANIM` · hash `0x28004F88151E03E0` · jhash `0xC4769830` · **Cliente**

```lua
local retval = StopEntityAnim(entity, animation, animGroup, p3)
```
```c
Any STOP_ENTITY_ANIM(Entity entity, char* animation, char* animGroup, float p3);
```

**Parámetros**

- `entity` (`Entity`)
- `animation` (`char*`)
- `animGroup` (`char*`)
- `p3` (`float`)

**Devuelve:** `Any`

**Descripción oficial:**

```
RAGEPluginHook list: docs.ragepluginhook.net/html/62951c37-a440-478c-b389-c471230ddfc5.htm
```

---
### StopSynchronizedEntityAnim

`STOP_SYNCHRONIZED_ENTITY_ANIM` · hash `0x43D3807C077261E3` · jhash `0xE27D2FC1` · **Cliente**

```lua
local retval = StopSynchronizedEntityAnim(entity, p1, p2)
```
```c
BOOL STOP_SYNCHRONIZED_ENTITY_ANIM(Entity entity, float p1, BOOL p2);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`float`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p1 sync task id?  
```

---
### StopSynchronizedMapEntityAnim

`STOP_SYNCHRONIZED_MAP_ENTITY_ANIM` · hash `0x11E79CAB7183B6F5` · jhash `0x7253D5B2` · **Cliente**

```lua
local retval = StopSynchronizedMapEntityAnim(p0, p1, p2, p3, p4, p5)
```
```c
BOOL STOP_SYNCHRONIZED_MAP_ENTITY_ANIM(float p0, float p1, float p2, float p3, Any p4, float p5);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`Any`)
- `p5` (`float`)

**Devuelve:** `BOOL`

---
### WouldEntityBeOccluded

`WOULD_ENTITY_BE_OCCLUDED` · hash `0xEE5D2A122E09EC42` · jhash `0xEA127CBC` · **Cliente**

```lua
local retval = WouldEntityBeOccluded(entityModelHash, x, y, z, p4)
```
```c
BOOL WOULD_ENTITY_BE_OCCLUDED(Hash entityModelHash, float x, float y, float z, BOOL p4);
```

**Parámetros**

- `entityModelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p4` (`BOOL`)

**Devuelve:** `BOOL`

---
