# Natives de FiveM (CFX) — solo servidor

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

**290** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddBlipForArea`](#addblipforarea) · [`AddBlipForCoord`](#addblipforcoord) · [`AddBlipForEntity`](#addblipforentity) · [`AddBlipForRadius`](#addblipforradius) · [`AddPedDecorationFromHashes`](#addpeddecorationfromhashes) · [`ApplyForceToEntity`](#applyforcetoentity) · [`CanPlayerStartCommerceSession`](#canplayerstartcommercesession) · [`ClearPedProp`](#clearpedprop) · [`ClearPedSecondaryTask`](#clearpedsecondarytask) · [`ClearPedTasks`](#clearpedtasks) · [`ClearPedTasksImmediately`](#clearpedtasksimmediately) · [`ClearPlayerWantedLevel`](#clearplayerwantedlevel) · [`CreateObject`](#createobject) · [`CreateObjectNoOffset`](#createobjectnooffset) · [`CreatePed`](#createped) · [`CreatePedInsideVehicle`](#createpedinsidevehicle) · [`CreateVehicle`](#createvehicle) · [`CreateVehicleServerSetter`](#createvehicleserversetter) · [`DeleteEntity`](#deleteentity) · [`DeleteTrain`](#deletetrain) · [`DoesBoatSinkWhenWrecked`](#doesboatsinkwhenwrecked) · [`DoesEntityExist`](#doesentityexist) · [`DoesPlayerExist`](#doesplayerexist) · [`DoesPlayerOwnSku`](#doesplayerownsku) · [`DoesPlayerOwnSkuExt`](#doesplayerownskuext) · [`DropPlayer`](#dropplayer) · [`EnableEnhancedHostSupport`](#enableenhancedhostsupport) · [`FlagServerAsPrivate`](#flagserverasprivate) · [`FlushResourceKvp`](#flushresourcekvp) · [`FreezeEntityPosition`](#freezeentityposition) · [`GetAirDragMultiplierForPlayersVehicle`](#getairdragmultiplierforplayersvehicle) · [`GetAllObjects`](#getallobjects) · [`GetAllPeds`](#getallpeds) · [`GetAllVehicles`](#getallvehicles) · [`GetColshapeDimension`](#getcolshapedimension) · [`GetConsoleBuffer`](#getconsolebuffer) · [`GetCurrentPedWeapon`](#getcurrentpedweapon) · [`GetEntityAttachedTo`](#getentityattachedto) · [`GetEntityCollisionDisabled`](#getentitycollisiondisabled) · [`GetEntityCoords`](#getentitycoords) · [`GetEntityHeading`](#getentityheading) · [`GetEntityHealth`](#getentityhealth) · [`GetEntityMaxHealth`](#getentitymaxhealth) · [`GetEntityModel`](#getentitymodel) · [`GetEntityOrphanMode`](#getentityorphanmode) · [`GetEntityPopulationType`](#getentitypopulationtype) · [`GetEntityRemoteSyncedScenesAllowed`](#getentityremotesyncedscenesallowed) · [`GetEntityRotation`](#getentityrotation) · [`GetEntityRotationVelocity`](#getentityrotationvelocity) · [`GetEntityRoutingBucket`](#getentityroutingbucket) · [`GetEntityScript`](#getentityscript) · [`GetEntitySpeed`](#getentityspeed) · [`GetEntityType`](#getentitytype) · [`GetEntityVelocity`](#getentityvelocity) · [`GetGameTimer`](#getgametimer) · [`GetHashKey`](#gethashkey) · [`GetHeliBodyHealth`](#gethelibodyhealth) · [`GetHeliDisableExplodeFromBodyDamage`](#gethelidisableexplodefrombodydamage) · [`GetHeliEngineHealth`](#gethelienginehealth) · [`GetHeliGasTankHealth`](#getheligastankhealth) · [`GetHeliMainRotorDamageScale`](#gethelimainrotordamagescale) · [`GetHeliMainRotorHealth`](#gethelimainrotorhealth) · [`GetHeliPitchControl`](#gethelipitchcontrol) · [`GetHeliRearRotorDamageScale`](#gethelirearrotordamagescale) · [`GetHeliRearRotorHealth`](#gethelirearrotorhealth) · [`GetHeliRollControl`](#gethelirollcontrol) · [`GetHeliTailRotorDamageScale`](#gethelitailrotordamagescale) · [`GetHeliTailRotorHealth`](#gethelitailrotorhealth) · [`GetHeliThrottleControl`](#gethelithrottlecontrol) · [`GetHeliYawControl`](#getheliyawcontrol) · [`GetHostId`](#gethostid) · [`GetIsHeliEngineRunning`](#getishelienginerunning) · [`GetIsVehicleEngineRunning`](#getisvehicleenginerunning) · [`GetIsVehiclePrimaryColourCustom`](#getisvehicleprimarycolourcustom) · [`GetIsVehicleSecondaryColourCustom`](#getisvehiclesecondarycolourcustom) · [`GetLandingGearState`](#getlandinggearstate) · [`GetLastPedInVehicleSeat`](#getlastpedinvehicleseat) · [`GetNetTypeFromEntity`](#getnettypefromentity) · [`GetNumPlayerIdentifiers`](#getnumplayeridentifiers) · [`GetNumPlayerIndices`](#getnumplayerindices) · [`GetNumPlayerTokens`](#getnumplayertokens) · [`GetPasswordHash`](#getpasswordhash) · [`GetPedArmour`](#getpedarmour) · [`GetPedCauseOfDeath`](#getpedcauseofdeath) · [`GetPedDesiredHeading`](#getpeddesiredheading) · [`GetPedInVehicleSeat`](#getpedinvehicleseat) · [`GetPedMaxHealth`](#getpedmaxhealth) · [`GetPedRelationshipGroupHash`](#getpedrelationshipgrouphash) · [`GetPedScriptTaskCommand`](#getpedscripttaskcommand) · [`GetPedScriptTaskStage`](#getpedscripttaskstage) · [`GetPedSourceOfDamage`](#getpedsourceofdamage) · [`GetPedSourceOfDeath`](#getpedsourceofdeath) · [`GetPedSpecificTaskType`](#getpedspecifictasktype) · [`GetPedStealthMovement`](#getpedstealthmovement) · [`GetPlayerCameraRotation`](#getplayercamerarotation) · [`GetPlayerEndpoint`](#getplayerendpoint) · [`GetPlayerFakeWantedLevel`](#getplayerfakewantedlevel) · [`GetPlayerFocusPos`](#getplayerfocuspos) · [`GetPlayerFromIndex`](#getplayerfromindex) · [`GetPlayerGuid`](#getplayerguid) · [`GetPlayerIdentifier`](#getplayeridentifier) · [`GetPlayerIdentifierByType`](#getplayeridentifierbytype) · [`GetPlayerInvincible`](#getplayerinvincible) · [`GetPlayerLastMsg`](#getplayerlastmsg) · [`GetPlayerMaxArmour`](#getplayermaxarmour) · [`GetPlayerMaxHealth`](#getplayermaxhealth) · [`GetPlayerName`](#getplayername) · [`GetPlayerPed`](#getplayerped) · [`GetPlayerPeerStatistics`](#getplayerpeerstatistics) · [`GetPlayerPing`](#getplayerping) · [`GetPlayerRoutingBucket`](#getplayerroutingbucket) · [`GetPlayerTeam`](#getplayerteam) · [`GetPlayerTimeInPursuit`](#getplayertimeinpursuit) · [`GetPlayerTimeOnline`](#getplayertimeonline) · [`GetPlayerToken`](#getplayertoken) · [`GetPlayerWantedCentrePosition`](#getplayerwantedcentreposition) · [`GetPlayerWantedLevel`](#getplayerwantedlevel) · [`GetResourcePath`](#getresourcepath) · [`GetSeatPedIsUsing`](#getseatpedisusing) · [`GetSelectedPedWeapon`](#getselectedpedweapon) · [`GetThrusterSideRcsThrottle`](#getthrustersidercsthrottle) · [`GetThrusterThrottle`](#getthrusterthrottle) · [`GetTrainBackwardCarriage`](#gettrainbackwardcarriage) · [`GetTrainCarriageEngine`](#gettraincarriageengine) · [`GetTrainCarriageIndex`](#gettraincarriageindex) · [`GetTrainForwardCarriage`](#gettrainforwardcarriage) · [`GetVehicleBodyHealth`](#getvehiclebodyhealth) · [`GetVehicleColours`](#getvehiclecolours) · [`GetVehicleCustomPrimaryColour`](#getvehiclecustomprimarycolour) · [`GetVehicleCustomSecondaryColour`](#getvehiclecustomsecondarycolour) · [`GetVehicleDashboardColour`](#getvehicledashboardcolour) · [`GetVehicleDirtLevel`](#getvehicledirtlevel) · [`GetVehicleDoorLockStatus`](#getvehicledoorlockstatus) · [`GetVehicleDoorStatus`](#getvehicledoorstatus) · [`GetVehicleDoorsLockedForPlayer`](#getvehicledoorslockedforplayer) · [`GetVehicleEngineHealth`](#getvehicleenginehealth) · [`GetVehicleExtraColours`](#getvehicleextracolours) · [`GetVehicleFlightNozzlePosition`](#getvehicleflightnozzleposition) · [`GetVehicleHeadlightsColour`](#getvehicleheadlightscolour) · [`GetVehicleHomingLockonState`](#getvehiclehominglockonstate) · [`GetVehicleHornType`](#getvehiclehorntype) · [`GetVehicleInteriorColour`](#getvehicleinteriorcolour) · [`GetVehicleLightsState`](#getvehiclelightsstate) · [`GetVehicleLivery`](#getvehiclelivery) · [`GetVehicleLockOnTarget`](#getvehiclelockontarget) · [`GetVehicleNeonColour`](#getvehicleneoncolour) · [`GetVehicleNeonEnabled`](#getvehicleneonenabled) · [`GetVehicleNumberPlateText`](#getvehiclenumberplatetext) · [`GetVehicleNumberPlateTextIndex`](#getvehiclenumberplatetextindex) · [`GetVehiclePedIsIn`](#getvehiclepedisin) · [`GetVehiclePetrolTankHealth`](#getvehiclepetroltankhealth) · [`GetVehicleRadioStationIndex`](#getvehicleradiostationindex) · [`GetVehicleRoofLivery`](#getvehiclerooflivery) · [`GetVehicleTotalRepairs`](#getvehicletotalrepairs) · [`GetVehicleTyreSmokeColor`](#getvehicletyresmokecolor) · [`GetVehicleWheelType`](#getvehiclewheeltype) · [`GetVehicleWindowTint`](#getvehiclewindowtint) · [`GiveWeaponComponentToPed`](#giveweaponcomponenttoped) · [`GiveWeaponToPed`](#giveweapontoped) · [`HasEntityBeenMarkedAsNoLongerNeeded`](#hasentitybeenmarkedasnolongerneeded) · [`HasVehicleBeenDamagedByBullets`](#hasvehiclebeendamagedbybullets) · [`HasVehicleBeenOwnedByPlayer`](#hasvehiclebeenownedbyplayer) · [`IsBoatAnchoredAndFrozen`](#isboatanchoredandfrozen) · [`IsBoatWrecked`](#isboatwrecked) · [`IsEntityVisible`](#isentityvisible) · [`IsFlashLightOn`](#isflashlighton) · [`IsHeliTailBoomBreakable`](#ishelitailboombreakable) · [`IsHeliTailBoomBroken`](#ishelitailboombroken) · [`IsPedAPlayer`](#ispedaplayer) · [`IsPedHandcuffed`](#ispedhandcuffed) · [`IsPedInAnyVehicle`](#ispedinanyvehicle) · [`IsPedInVehicle`](#ispedinvehicle) · [`IsPedRagdoll`](#ispedragdoll) · [`IsPedStrafing`](#ispedstrafing) · [`IsPedUsingActionMode`](#ispedusingactionmode) · [`IsPlayerAceAllowed`](#isplayeraceallowed) · [`IsPlayerCommerceInfoLoaded`](#isplayercommerceinfoloaded) · [`IsPlayerCommerceInfoLoadedExt`](#isplayercommerceinfoloadedext) · [`IsPlayerEvadingWantedLevel`](#isplayerevadingwantedlevel) · [`IsPlayerInFreeCamMode`](#isplayerinfreecammode) · [`IsPlayerUsingSuperJump`](#isplayerusingsuperjump) · [`IsTrainCaboose`](#istraincaboose) · [`IsVehicleExtraTurnedOn`](#isvehicleextraturnedon) · [`IsVehicleSirenOn`](#isvehiclesirenon) · [`IsVehicleTyreBurst`](#isvehicletyreburst) · [`IsVehicleWindowIntact`](#isvehiclewindowintact) · [`LoadPlayerCommerceData`](#loadplayercommercedata) · [`LoadPlayerCommerceDataExt`](#loadplayercommercedataext) · [`MumbleCreateChannel`](#mumblecreatechannel) · [`MumbleIsPlayerMuted`](#mumbleisplayermuted) · [`MumbleSetPlayerMuted`](#mumblesetplayermuted) · [`NetworkGetEntityFromNetworkId`](#networkgetentityfromnetworkid) · [`NetworkGetFirstEntityOwner`](#networkgetfirstentityowner) · [`NetworkGetNetworkIdFromEntity`](#networkgetnetworkidfromentity) · [`NetworkGetVoiceProximityOverrideForPlayer`](#networkgetvoiceproximityoverrideforplayer) · [`PerformHttpRequestInternal`](#performhttprequestinternal) · [`PerformHttpRequestInternalEx`](#performhttprequestinternalex) · [`PrintStructuredTrace`](#printstructuredtrace) · [`RecorderStartRecording`](#recorderstartrecording) · [`RecorderStartReplay`](#recorderstartreplay) · [`RecorderStopRecording`](#recorderstoprecording) · [`RecorderStopReplay`](#recorderstopreplay) · [`RegisterConsoleListener`](#registerconsolelistener) · [`RegisterResourceAsset`](#registerresourceasset) · [`RegisterResourceBuildTaskFactory`](#registerresourcebuildtaskfactory) · [`RemoveAllPedWeapons`](#removeallpedweapons) · [`RemoveBlip`](#removeblip) · [`RemoveWeaponComponentFromPed`](#removeweaponcomponentfromped) · [`RemoveWeaponFromPed`](#removeweaponfromped) · [`RequestPlayerCommerceSession`](#requestplayercommercesession) · [`SaveResourceFile`](#saveresourcefile) · [`ScanResourceRoot`](#scanresourceroot) · [`ScheduleResourceTick`](#scheduleresourcetick) · [`SetBlipSprite`](#setblipsprite) · [`SetColshapeDimension`](#setcolshapedimension) · [`SetConvar`](#setconvar) · [`SetConvarReplicated`](#setconvarreplicated) · [`SetConvarServerInfo`](#setconvarserverinfo) · [`SetCurrentPedWeapon`](#setcurrentpedweapon) · [`SetEntityCoords`](#setentitycoords) · [`SetEntityDistanceCullingRadius`](#setentitydistancecullingradius) · [`SetEntityHeading`](#setentityheading) · [`SetEntityIgnoreRequestControlFilter`](#setentityignorerequestcontrolfilter) · [`SetEntityOrphanMode`](#setentityorphanmode) · [`SetEntityRemoteSyncedScenesAllowed`](#setentityremotesyncedscenesallowed) · [`SetEntityRotation`](#setentityrotation) · [`SetEntityRoutingBucket`](#setentityroutingbucket) · [`SetEntityVelocity`](#setentityvelocity) · [`SetGameType`](#setgametype) · [`SetHttpHandler`](#sethttphandler) · [`SetMapName`](#setmapname) · [`SetPedAmmo`](#setpedammo) · [`SetPedArmour`](#setpedarmour) · [`SetPedCanRagdoll`](#setpedcanragdoll) · [`SetPedComponentVariation`](#setpedcomponentvariation) · [`SetPedConfigFlag`](#setpedconfigflag) · [`SetPedDefaultComponentVariation`](#setpeddefaultcomponentvariation) · [`SetPedEyeColor`](#setpedeyecolor) · [`SetPedFaceFeature`](#setpedfacefeature) · [`SetPedHairTint`](#setpedhairtint) · [`SetPedHeadBlendData`](#setpedheadblenddata) · [`SetPedHeadOverlay`](#setpedheadoverlay) · [`SetPedHeadOverlayColor`](#setpedheadoverlaycolor) · [`SetPedIntoVehicle`](#setpedintovehicle) · [`SetPedPropIndex`](#setpedpropindex) · [`SetPedRandomComponentVariation`](#setpedrandomcomponentvariation) · [`SetPedRandomProps`](#setpedrandomprops) · [`SetPedResetFlag`](#setpedresetflag) · [`SetPedToRagdoll`](#setpedtoragdoll) · [`SetPedToRagdollWithFall`](#setpedtoragdollwithfall) · [`SetPlayerControl`](#setplayercontrol) · [`SetPlayerCullingRadius`](#setplayercullingradius) · [`SetPlayerInvincible`](#setplayerinvincible) · [`SetPlayerModel`](#setplayermodel) · [`SetPlayerRoutingBucket`](#setplayerroutingbucket) · [`SetPlayerWantedLevel`](#setplayerwantedlevel) · [`SetRoutingBucketEntityLockdownMode`](#setroutingbucketentitylockdownmode) · [`SetRoutingBucketPopulationEnabled`](#setroutingbucketpopulationenabled) · [`SetVehicleAlarm`](#setvehiclealarm) · [`SetVehicleBodyHealth`](#setvehiclebodyhealth) · [`SetVehicleColourCombination`](#setvehiclecolourcombination) · [`SetVehicleColours`](#setvehiclecolours) · [`SetVehicleCustomPrimaryColour`](#setvehiclecustomprimarycolour) · [`SetVehicleCustomSecondaryColour`](#setvehiclecustomsecondarycolour) · [`SetVehicleDirtLevel`](#setvehicledirtlevel) · [`SetVehicleDoorBroken`](#setvehicledoorbroken) · [`SetVehicleDoorsLocked`](#setvehicledoorslocked) · [`SetVehicleNumberPlateText`](#setvehiclenumberplatetext) · [`StartResource`](#startresource) · [`StopResource`](#stopresource) · [`TaskCombatPed`](#taskcombatped) · [`TaskDriveBy`](#taskdriveby) · [`TaskEnterVehicle`](#taskentervehicle) · [`TaskEveryoneLeaveVehicle`](#taskeveryoneleavevehicle) · [`TaskGoStraightToCoord`](#taskgostraighttocoord) · [`TaskGoToCoordAnyMeans`](#taskgotocoordanymeans) · [`TaskGoToEntity`](#taskgotoentity) · [`TaskHandsUp`](#taskhandsup) · [`TaskLeaveAnyVehicle`](#taskleaveanyvehicle) · [`TaskLeaveVehicle`](#taskleavevehicle) · [`TaskPlayAnim`](#taskplayanim) · [`TaskPlayAnimAdvanced`](#taskplayanimadvanced) · [`TaskReactAndFleePed`](#taskreactandfleeped) · [`TaskShootAtCoord`](#taskshootatcoord) · [`TaskShootAtEntity`](#taskshootatentity) · [`TaskWarpPedIntoVehicle`](#taskwarppedintovehicle) · [`TempBanPlayer`](#tempbanplayer) · [`TriggerClientEventInternal`](#triggerclienteventinternal) · [`TriggerLatentClientEventInternal`](#triggerlatentclienteventinternal) · [`VerifyPasswordHash`](#verifypasswordhash)

---
### AddBlipForArea

`_ADD_BLIP_FOR_AREA` · hash `0x6228F159` · **Servidor**

```lua
local retval = AddBlipForArea(x, y, z, width, height)
```
```c
Blip _ADD_BLIP_FOR_AREA(float x, float y, float z, float width, float height);
```

**Parámetros**

- `x` (`float`): The X coordinate of the center of the blip.
- `y` (`float`): The Y coordinate of the center of the blip.
- `z` (`float`): The Z coordinate of the center of the blip.
- `width` (`float`): The width of the blip.
- `height` (`float`): The height of the blip.

**Devuelve:** `Blip` — A handle to the blip.

**Descripción oficial:**

Adds a rectangular blip for the specified coordinates/area.
It is recommended to use [SET_BLIP_ROTATION](../gta5/HUD.md#setbliprotation) and [SET_BLIP_COLOUR](../gta5/HUD.md#setblipcolour) to make the blip not rotate along with the camera.
By default, the blip will show as a *regular* blip with the specified color/sprite if it is outside of the minimap view.
(Native name is *likely* to actually be ADD_BLIP_FOR_AREA, but due to the usual reasons this can't be confirmed)

**This is the server-side RPC native equivalent of the client native [\_ADD_BLIP_FOR_AREA](#addblipforarea).**

**Nombres antiguos (alias):** `0xCE5D0E5E315DB238` (`N_0xce5d0e5e315db238`)

---
### AddBlipForCoord

`ADD_BLIP_FOR_COORD` · hash `0xC6F43D0E` · **Servidor**

```lua
local retval = AddBlipForCoord(x, y, z)
```
```c
Blip ADD_BLIP_FOR_COORD(float x, float y, float z);
```

**Parámetros**

- `x` (`float`): The X coordinate to create the blip on.
- `y` (`float`): The Y coordinate.
- `z` (`float`): The Z coordinate.

**Devuelve:** `Blip` — A blip handle.

**Descripción oficial:**

Creates a blip for the specified coordinates. You can use `SET_BLIP_` natives to change the blip.

**This is the server-side RPC native equivalent of the client native [ADD_BLIP_FOR_COORD](#addblipforcoord).**

---
### AddBlipForEntity

`ADD_BLIP_FOR_ENTITY` · hash `0x30822554` · **Servidor**

```lua
local retval = AddBlipForEntity(entity)
```
```c
Blip ADD_BLIP_FOR_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity handle to create the blip.

**Devuelve:** `Blip` — A blip handle.

**Descripción oficial:**

Create a blip that by default is red (enemy), you can use [SET_BLIP_AS_FRIENDLY](#addblipforcoord) to make it blue (friend).\
Can be used for objects, vehicles and peds.
Example of enemy:
![enemy](https://i.imgur.com/LIizV6S.png)
Example of friend:
![friend](https://i.imgur.com/XrCuvZP.png)

**This is the server-side RPC native equivalent of the client native [ADD_BLIP_FOR_ENTITY](#addblipforentity).**

---
### AddBlipForRadius

`ADD_BLIP_FOR_RADIUS` · hash `0x4626756C` · **Servidor**

```lua
local retval = AddBlipForRadius(posX, posY, posZ, radius)
```
```c
Blip ADD_BLIP_FOR_RADIUS(float posX, float posY, float posZ, float radius);
```

**Parámetros**

- `posX` (`float`): The x position of the blip (you can also send a vector3 instead of the bulk coordinates)
- `posY` (`float`): The y position of the blip (you can also send a vector3 instead of the bulk coordinates)
- `posZ` (`float`): The z position of the blip (you can also send a vector3 instead of the bulk coordinates)
- `radius` (`float`): The number that defines the radius of the blip circle

**Devuelve:** `Blip` — The blip handle that can be manipulated with every `SetBlip` natives

**Descripción oficial:**

Create a blip with a radius for the specified coordinates (it doesnt create the blip sprite, so you need to use [AddBlipCoords](#addblipforcoord))
Example image:
![example](https://i.imgur.com/fDCmHVD.png)

**This is the server-side RPC native equivalent of the client native [ADD_BLIP_FOR_RADIUS](#addblipforradius).**

---
### AddPedDecorationFromHashes

`ADD_PED_DECORATION_FROM_HASHES` · hash `0x70559AC7` · **Servidor**

```lua
AddPedDecorationFromHashes(ped, collection, overlay)
```
```c
void ADD_PED_DECORATION_FROM_HASHES(Ped ped, Hash collection, Hash overlay);
```

**Parámetros**

- `ped` (`Ped`)
- `collection` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `overlay` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Applies an Item from a PedDecorationCollection to a ped. These include tattoos and shirt decals.
collection - PedDecorationCollection filename hash
overlay - Item name hash
Example:
Entry inside "mpbeach_overlays.xml" -
<Item>
<uvPos x="0.500000" y="0.500000" />
<scale x="0.600000" y="0.500000" />
<rotation value="0.000000" />
<nameHash>FM_Hair_Fuzz</nameHash>
<txdHash>mp_hair_fuzz</txdHash>
<txtHash>mp_hair_fuzz</txtHash>
<zone>ZONE_HEAD</zone>
<type>TYPE_TATTOO</type>
<faction>FM</faction>
<garment>All</garment>
<gender>GENDER_DONTCARE</gender>
<award />
<awardLevel />
</Item>
Code:
PED::_0x5F5D1665E352A839(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("mpbeach_overlays"), MISC::GET_HASH_KEY("fm_hair_fuzz"))
```

**This is the server-side RPC native equivalent of the client native [ADD_PED_DECORATION_FROM_HASHES](#addpeddecorationfromhashes).**

**Nombres antiguos (alias):** `_APPLY_PED_OVERLAY` (`ApplyPedOverlay`), `_SET_PED_DECORATION` (`SetPedDecoration`)

---
### ApplyForceToEntity

`APPLY_FORCE_TO_ENTITY` · hash `0xC1C0855A` · **Servidor**

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

**This is the server-side RPC native equivalent of the client native [APPLY_FORCE_TO_ENTITY](#applyforcetoentity).**

---
### CanPlayerStartCommerceSession

`CAN_PLAYER_START_COMMERCE_SESSION` · hash `0x429461C3` · **Servidor**

```lua
local retval = CanPlayerStartCommerceSession(playerSrc)
```
```c
BOOL CAN_PLAYER_START_COMMERCE_SESSION(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `BOOL` — True or false.

**Descripción oficial:**

> This native is deprecated and may be removed in a future version. Use the [Tebex API](https://docs.tebex.io/) instead.

Returns whether or not the specified player has enough information to start a commerce session for.

---
### ClearPedProp

`CLEAR_PED_PROP` · hash `0x2D23D743` · **Servidor**

```lua
ClearPedProp(ped, propId)
```
```c
void CLEAR_PED_PROP(Ped ped, int propId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `propId` (`int`): The prop id you want to clear from the ped. Refer to [SET_PED_PROP_INDEX](#setpedpropindex).

**Devuelve:** `void`

**Descripción oficial:**

CLEAR_PED_PROP

**This is the server-side RPC native equivalent of the client native [CLEAR_PED_PROP](#clearpedprop).**

---
### ClearPedSecondaryTask

`CLEAR_PED_SECONDARY_TASK` · hash `0xA635F451` · **Servidor**

```lua
ClearPedSecondaryTask(ped)
```
```c
void CLEAR_PED_SECONDARY_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

CLEAR_PED_SECONDARY_TASK

**This is the server-side RPC native equivalent of the client native [CLEAR_PED_SECONDARY_TASK](#clearpedsecondarytask).**

---
### ClearPedTasks

`CLEAR_PED_TASKS` · hash `0xDE3316AB` · **Servidor**

```lua
ClearPedTasks(ped)
```
```c
void CLEAR_PED_TASKS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): Ped id. Use PlayerPedId() for your own character.

**Devuelve:** `void`

**Descripción oficial:**

Clear a ped's tasks. Stop animations and other tasks created by scripts.

**This is the server-side RPC native equivalent of the client native [CLEAR_PED_TASKS](#clearpedtasks).**

---
### ClearPedTasksImmediately

`CLEAR_PED_TASKS_IMMEDIATELY` · hash `0xBC045625` · **Servidor**

```lua
ClearPedTasksImmediately(ped)
```
```c
void CLEAR_PED_TASKS_IMMEDIATELY(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): Ped id.

**Devuelve:** `void`

**Descripción oficial:**

Immediately stops the pedestrian from whatever it's doing. The difference between this and [CLEAR_PED_TASKS](#clearpedtasks) is that this one teleports the ped but does not change the position of the ped.

**This is the server-side RPC native equivalent of the client native [CLEAR_PED_TASKS_IMMEDIATELY](#clearpedtasksimmediately).**

---
### ClearPlayerWantedLevel

`CLEAR_PLAYER_WANTED_LEVEL` · hash `0x54EA5BCC` · **Servidor**

```lua
ClearPlayerWantedLevel(player)
```
```c
void CLEAR_PLAYER_WANTED_LEVEL(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
This executes at the same as speed as PLAYER::SET_PLAYER_WANTED_LEVEL(player, 0, false);
PLAYER::GET_PLAYER_WANTED_LEVEL(player); executes in less than half the time. Which means that it's worth first checking if the wanted level needs to be cleared before clearing. However, this is mostly about good code practice and can important in other situations. The difference in time in this example is negligible.
```

**This is the server-side RPC native equivalent of the client native [CLEAR_PLAYER_WANTED_LEVEL](#clearplayerwantedlevel).**

---
### CreateObject

`CREATE_OBJECT` · hash `0x2F7AA05C` · **Servidor**

```lua
local retval = CreateObject(modelHash, x, y, z, isNetwork, netMissionEntity, doorFlag)
```
```c
Entity CREATE_OBJECT(Hash modelHash, float x, float y, float z, BOOL isNetwork, BOOL netMissionEntity, BOOL doorFlag);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to spawn.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component, 'ground level'.
- `isNetwork` (`BOOL`): Whether to create a network object for the object. If false, the object exists only locally.
- `netMissionEntity` (`BOOL`): Whether to register the object as pinned to the script host in the R\* network model.
- `doorFlag` (`BOOL`): False to create a door archetype (archetype flag bit 26 set) as a door. Required to be set to true to create door models in network mode.

**Devuelve:** `Entity` — A script handle (fwScriptGuid index) for the object, or `0` if the object failed to be created.

**Descripción oficial:**

Creates an object (prop) with the specified model at the specified position, offset on the Z axis by the radius of the object's model.
This object will initially be owned by the creating script as a mission entity, and the model should be loaded already (e.g. using REQUEST_MODEL).

**This is the server-side RPC native equivalent of the client native [CREATE_OBJECT](#createobject).**

---
### CreateObjectNoOffset

`CREATE_OBJECT_NO_OFFSET` · hash `0x58040420` · **Servidor**

```lua
local retval = CreateObjectNoOffset(modelHash, x, y, z, isNetwork, netMissionEntity, doorFlag)
```
```c
Entity CREATE_OBJECT_NO_OFFSET(Hash modelHash, float x, float y, float z, BOOL isNetwork, BOOL netMissionEntity, BOOL doorFlag);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to spawn.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `isNetwork` (`BOOL`): Whether to create a network object for the object. If false, the object exists only locally.
- `netMissionEntity` (`BOOL`): Whether to register the object as pinned to the script host in the R\* network model.
- `doorFlag` (`BOOL`): False to create a door archetype (archetype flag bit 26 set) as a door. Required to be set to true to create door models in network mode.

**Devuelve:** `Entity` — A script handle (fwScriptGuid index) for the object, or `0` if the object failed to be created.

**Descripción oficial:**

Creates an object (prop) with the specified model centered at the specified position.
This object will initially be owned by the creating script as a mission entity, and the model should be loaded already (e.g. using REQUEST_MODEL).

**This is the server-side RPC native equivalent of the client native [CREATE_OBJECT_NO_OFFSET](#createobjectnooffset).**

---
### CreatePed

`CREATE_PED` · hash `0x389EF71` · **Servidor**

```lua
local retval = CreatePed(pedType, modelHash, x, y, z, heading, isNetwork, bScriptHostPed)
```
```c
Entity CREATE_PED(int pedType, Hash modelHash, float x, float y, float z, float heading, BOOL isNetwork, BOOL bScriptHostPed);
```

**Parámetros**

- `pedType` (`int`): Unused. Peds get set to CIVMALE/CIVFEMALE/etc. no matter the value specified.
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model of ped to spawn.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `heading` (`float`): Heading to face towards, in degrees.
- `isNetwork` (`BOOL`): Whether to create a network object for the ped. If false, the ped exists only locally.
- `bScriptHostPed` (`BOOL`): Whether to register the ped as pinned to the script host in the R\* network model.

**Devuelve:** `Entity` — A script handle (fwScriptGuid index) for the ped, or `0` if the ped failed to be created.

**Descripción oficial:**

Creates a ped (biped character, pedestrian, actor) with the specified model at the specified position and heading.
This ped will initially be owned by the creating script as a mission entity, and the model should be loaded already
(e.g. using REQUEST_MODEL).

**This is the server-side RPC native equivalent of the client native [CREATE_PED](#createped).**

---
### CreatePedInsideVehicle

`CREATE_PED_INSIDE_VEHICLE` · hash `0x3000F092` · **Servidor**

```lua
local retval = CreatePedInsideVehicle(vehicle, pedType, modelHash, seat, isNetwork, bScriptHostPed)
```
```c
Entity CREATE_PED_INSIDE_VEHICLE(Vehicle vehicle, int pedType, Hash modelHash, int seat, BOOL isNetwork, BOOL bScriptHostPed);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `pedType` (`int`): See [`CREATE_PED`](#createped)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `seat` (`int`)
- `isNetwork` (`BOOL`)
- `bScriptHostPed` (`BOOL`)

**Devuelve:** `Entity`

**Descripción oficial:**

CREATE_PED_INSIDE_VEHICLE

**This is the server-side RPC native equivalent of the client native [CREATE_PED_INSIDE_VEHICLE](#createpedinsidevehicle).**

---
### CreateVehicle

`CREATE_VEHICLE` · hash `0xDD75460A` · **Servidor**

```lua
local retval = CreateVehicle(modelHash, x, y, z, heading, isNetwork, netMissionEntity)
```
```c
Entity CREATE_VEHICLE(Hash modelHash, float x, float y, float z, float heading, BOOL isNetwork, BOOL netMissionEntity);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model of vehicle to spawn.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `heading` (`float`): Heading to face towards, in degrees.
- `isNetwork` (`BOOL`): Whether to create a network object for the vehicle. If false, the vehicle exists only locally.
- `netMissionEntity` (`BOOL`): Whether to register the vehicle as pinned to the script host in the R\* network model.

**Devuelve:** `Entity` — A script handle (fwScriptGuid index) for the vehicle, or `0` if the vehicle failed to be created.

**Descripción oficial:**

Creates a vehicle with the specified model at the specified position. This vehicle will initially be owned by the creating
script as a mission entity, and the model should be loaded already (e.g. using REQUEST_MODEL).

```
NativeDB Added Parameter 8: BOOL p7
```

**This is the server-side RPC native equivalent of the client native [CREATE_VEHICLE](#createvehicle).**

---
### CreateVehicleServerSetter

`CREATE_VEHICLE_SERVER_SETTER` · hash `0x6AE51D4B` · **Servidor**

```lua
local retval = CreateVehicleServerSetter(modelHash, type, x, y, z, heading)
```
```c
Vehicle CREATE_VEHICLE_SERVER_SETTER(Hash modelHash, char* type, float x, float y, float z, float heading);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model of vehicle to spawn.
- `type` (`char*`): The appropriate vehicle type for the model info. Can be one of `automobile`, `bike`, `boat`, `heli`, `plane`, `submarine`, `trailer`, and (potentially), `train`. This should be the same type as the `type` field in `vehicles.meta`.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `heading` (`float`): Heading to face towards, in degrees.

**Devuelve:** `Vehicle` — A script handle for the vehicle, or 0 if the vehicle failed to be created.

**Descripción oficial:**

Equivalent to CREATE_VEHICLE, but it uses 'server setter' logic (like the former CREATE_AUTOMOBILE) as a workaround for
reliability concerns regarding entity creation RPC.

Unlike CREATE_AUTOMOBILE, this supports other vehicle types as well.

**Ejemplo (lua):**

```lua
local heli = CreateVehicleServerSetter(`seasparrow`, 'heli', GetEntityCoords(GetPlayerPed(GetPlayers()[1])) + vector3(0, 0, 15), 0.0)
print(GetEntityCoords(heli)) -- should return correct coordinates
```

---
### DeleteEntity

`DELETE_ENTITY` · hash `0xFAA3D236` · **Servidor**

```lua
DeleteEntity(entity)
```
```c
void DELETE_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to delete.

**Devuelve:** `void`

**Descripción oficial:**

Deletes the specified entity.

**NOTE**: For trains this will only work if called on the train engine, it will not work on its carriages.

---
### DeleteTrain

`DELETE_TRAIN` · hash `0x523BA3DA` · **Servidor**

```lua
DeleteTrain(entity)
```
```c
void DELETE_TRAIN(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The carriage to delete.

**Devuelve:** `void`

**Descripción oficial:**

Deletes the specified `entity` and any carriage its attached to, or that is attached to it.

---
### DoesBoatSinkWhenWrecked

`DOES_BOAT_SINK_WHEN_WRECKED` · hash `0x43F15989` · **Servidor**

```lua
local retval = DoesBoatSinkWhenWrecked(vehicle)
```
```c
bool DOES_BOAT_SINK_WHEN_WRECKED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `bool` — Returns whether or not the boat sinks when wrecked.

---
### DoesEntityExist

`DOES_ENTITY_EXIST` · hash `0x3AC90869` · **Servidor**

```lua
local retval = DoesEntityExist(entity)
```
```c
BOOL DOES_ENTITY_EXIST(Object entity);
```

**Parámetros**

- `entity` (`Object`)

**Devuelve:** `BOOL`

---
### DoesPlayerExist

`DOES_PLAYER_EXIST` · hash `0x12038599` · **Servidor**

```lua
local retval = DoesPlayerExist(playerSrc)
```
```c
BOOL DOES_PLAYER_EXIST(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `BOOL` — True if the player exists, false otherwise

**Descripción oficial:**

Returns whether or not the player exists

**Ejemplo (lua):**

```lua
local deferralMessages = { "Isn't this just magical!", "We can defer all day!", "You'll get in eventually", "You're totally not going to sit here forever", "The Fruit Tree is a lie" }
AddEventHandler("playerConnecting", function(name, setKickReason, deferrals)
    local source = source
    deferrals.defer()

    Wait(0)


    local messageIndex = 0

    repeat
        Wait(2000)
        if messageIndex >= #deferralMessages then
            deferrals.done()
        else
            messageIndex = messageIndex + 1
        end
        deferrals.update(deferralMessages[messageIndex])
    until not DoesPlayerExist(source)
end)
```

---
### DoesPlayerOwnSku

`DOES_PLAYER_OWN_SKU` · hash `0x167ABA27` · **Servidor**

```lua
local retval = DoesPlayerOwnSku(playerSrc, skuId)
```
```c
BOOL DOES_PLAYER_OWN_SKU(char* playerSrc, int skuId);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle
- `skuId` (`int`): The ID of the SKU.

**Devuelve:** `BOOL` — A boolean.

**Descripción oficial:**

> This native is deprecated and may be removed in a future version. Use [`DOES_PLAYER_OWN_SKU_EXT`](#doesplayerownskuext) instead.

Requests whether or not the player owns the specified SKU.

---
### DoesPlayerOwnSkuExt

`DOES_PLAYER_OWN_SKU_EXT` · hash `0xDEF0480B` · **Servidor**

```lua
local retval = DoesPlayerOwnSkuExt(playerSrc, skuId)
```
```c
BOOL DOES_PLAYER_OWN_SKU_EXT(char* playerSrc, int skuId);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle
- `skuId` (`int`): The package ID on Tebex.

**Devuelve:** `BOOL` — A boolean.

**Descripción oficial:**

Requests whether or not the player owns the specified package.

---
### DropPlayer

`DROP_PLAYER` · hash `0xBA0613E1` · **Servidor**

```lua
DropPlayer(playerSrc, reason)
```
```c
void DROP_PLAYER(char* playerSrc, char* reason);
```

**Parámetros**

- `playerSrc` (`char*`)
- `reason` (`char*`)

**Devuelve:** `void`

---
### EnableEnhancedHostSupport

`ENABLE_ENHANCED_HOST_SUPPORT` · hash `0xF97B1C93` · **Servidor**

```lua
EnableEnhancedHostSupport(enabled)
```
```c
void ENABLE_ENHANCED_HOST_SUPPORT(BOOL enabled);
```

**Parámetros**

- `enabled` (`BOOL`)

**Devuelve:** `void`

---
### FlagServerAsPrivate

`FLAG_SERVER_AS_PRIVATE` · hash `0x13B6855D` · **Servidor**

```lua
FlagServerAsPrivate(private_)
```
```c
void FLAG_SERVER_AS_PRIVATE(BOOL private_);
```

**Parámetros**

- `private_` (`BOOL`)

**Devuelve:** `void`

---
### FlushResourceKvp

`FLUSH_RESOURCE_KVP` · hash `0xE27C97A0` · **Servidor**

```lua
FlushResourceKvp()
```
```c
void FLUSH_RESOURCE_KVP();
```

**Devuelve:** `void`

**Descripción oficial:**

Nonsynchronous operations will not wait for a disk/filesystem flush before returning from a write or delete call. They will be much faster than their synchronous counterparts (e.g., bulk operations), however, a system crash may lose the data to some recent operations.

This native ensures all `_NO_SYNC` operations are synchronized with the disk/filesystem.

**Ejemplo (lua):**

```lua
-- Bulk write many <key, value> pairs to the resource KVP.
local key = "bug_%d"
local value = "unintended_feature_%d"
for i=1,10000 do
	SetResourceKvpNoSync(key:format(i), value:format(i))
end

-- Ensure all data is synchronized to the filesystem
FlushResourceKvp()
```

---
### FreezeEntityPosition

`FREEZE_ENTITY_POSITION` · hash `0x65C16D57` · **Servidor**

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

Freezes or unfreezes an entity preventing its coordinates to change by the player if set to `true`. You can still change the entity position using [`SET_ENTITY_COORDS`](#setentitycoords).

**This is the server-side RPC native equivalent of the client native [FREEZE_ENTITY_POSITION](#freezeentityposition).**

---
### GetAirDragMultiplierForPlayersVehicle

`GET_AIR_DRAG_MULTIPLIER_FOR_PLAYERS_VEHICLE` · hash `0x62FC38D0` · **Servidor**

```lua
local retval = GetAirDragMultiplierForPlayersVehicle(playerSrc)
```
```c
float GET_AIR_DRAG_MULTIPLIER_FOR_PLAYERS_VEHICLE(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `float`

---
### GetAllObjects

`GET_ALL_OBJECTS` · hash `0x6886C3FE` · **Servidor**

```lua
local retval = GetAllObjects()
```
```c
object GET_ALL_OBJECTS();
```

**Devuelve:** `object` — An object containing a list of object handles.

**Descripción oficial:**

Returns all object handles known to the server.
The data returned adheres to the following layout:

```
[127, 42, 13, 37]
```

---
### GetAllPeds

`GET_ALL_PEDS` · hash `0xB8584FEF` · **Servidor**

```lua
local retval = GetAllPeds()
```
```c
object GET_ALL_PEDS();
```

**Devuelve:** `object` — An object containing a list of peds handles.

**Descripción oficial:**

Returns all peds handles known to the server.
The data returned adheres to the following layout:

```
[127, 42, 13, 37]
```

**Ejemplo (lua):**

```lua
-- This example prints information of every ped that has an owner.

for i, ped in ipairs(GetAllPeds()) do
    local pedOwner = NetworkGetEntityOwner(ped)
    if pedOwner > 0 then
       local playerName = GetPlayerName(pedOwner)
       local pedModel = GetEntityModel(ped)
       local pedArmour = GetPedArmour(ped)
       print("Ped : "..ped.." | Owner name : "..playerName.." | Model : "..pedModel.." | Armour : "..pedArmour)
    end
end
```

---
### GetAllVehicles

`GET_ALL_VEHICLES` · hash `0x332169F5` · **Servidor**

```lua
local retval = GetAllVehicles()
```
```c
object GET_ALL_VEHICLES();
```

**Devuelve:** `object` — An object containing a list of vehicle handles.

**Descripción oficial:**

Returns all vehicle handles known to the server.
The data returned adheres to the following layout:

```
[127, 42, 13, 37]
```

---
### GetColshapeDimension

`GET_COLSHAPE_DIMENSION` · hash `0x8B7A9C14` · **Servidor**

```lua
local retval = GetColshapeDimension(colShapeId)
```
```c
int GET_COLSHAPE_DIMENSION(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.

**Devuelve:** `int` — The dimension assigned to the collision shape.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns the dimension (routing bucket) of the collision shape.

---
### GetConsoleBuffer

`GET_CONSOLE_BUFFER` · hash `0xE57429FA` · **Servidor**

```lua
local retval = GetConsoleBuffer()
```
```c
char* GET_CONSOLE_BUFFER();
```

**Devuelve:** `char*` — The most recent game console output, as a string.

**Descripción oficial:**

Returns the current console output buffer.

---
### GetCurrentPedWeapon

`GET_CURRENT_PED_WEAPON` · hash `0xB0237302` · **Servidor**

```lua
local retval = GetCurrentPedWeapon(ped)
```
```c
Hash GET_CURRENT_PED_WEAPON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `Hash` — The weapon hash.

**Descripción oficial:**

Returns the hash of weapon the Ped is currently using.

---
### GetEntityAttachedTo

`GET_ENTITY_ATTACHED_TO` · hash `0xFE1589F9` · **Servidor**

```lua
local retval = GetEntityAttachedTo(entity)
```
```c
Entity GET_ENTITY_ATTACHED_TO(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to check.

**Devuelve:** `Entity` — The attached entity handle. 0 returned if the entity is not attached.

**Descripción oficial:**

Gets the entity that this entity is attached to.

---
### GetEntityCollisionDisabled

`GET_ENTITY_COLLISION_DISABLED` · hash `0xE8C0C629` · **Servidor**

```lua
local retval = GetEntityCollisionDisabled(entity)
```
```c
bool GET_ENTITY_COLLISION_DISABLED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The target entity.

**Devuelve:** `bool` — Returns whether or not entity collisions are disabled.

---
### GetEntityCoords

`GET_ENTITY_COORDS` · hash `0x1647F1CB` · **Servidor**

```lua
local retval = GetEntityCoords(entity)
```
```c
Vector3 GET_ENTITY_COORDS(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the coordinates from.

**Devuelve:** `Vector3` — The current entity coordinates.

**Descripción oficial:**

Gets the current coordinates for a specified entity. This native is used server side when using OneSync.

See [GET_ENTITY_COORDS](#getentitycoords) for client side.

**Ejemplo (lua):**

```lua
local function ShowCoordinates()
    local player = source
    local ped = GetPlayerPed(player)
    local playerCoords = GetEntityCoords(ped)

    print(playerCoords) -- vector3(...)
end

RegisterNetEvent("myCoordinates")
AddEventHandler("myCoordinates", ShowCoordinates)
```

**Ejemplo (js):**

```js
onNet('myCoordinates', () => {
  const player = global.source; // use (global as any).source for Typescript
  const ped = GetPlayerPed(player);
  const [playerX, playerY, playerZ] = GetEntityCoords(ped);

  console.log(`${playerX}, ${playerY}, ${playerZ}`);
});
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

// In class constructor
EventHandlers["myCoordinates"] += new Action<Player>(ShowCoordinates);

// Delegate method
private void ShowCoordinates([FromSource]Player player) {
    Vector3 playerCoords = GetEntityCoords(player.Character);

    // or the preferred use of C# wrapper
    Vector3 playerCoords = player.Character.Position;

    Debug.WriteLine($"{playerCoords}");
}
```

---
### GetEntityHeading

`GET_ENTITY_HEADING` · hash `0x972CC383` · **Servidor**

```lua
local retval = GetEntityHeading(entity)
```
```c
float GET_ENTITY_HEADING(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `float`

---
### GetEntityHealth

`GET_ENTITY_HEALTH` · hash `0x8E3222B7` · **Servidor**

```lua
local retval = GetEntityHealth(entity)
```
```c
int GET_ENTITY_HEALTH(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to check the health of

**Devuelve:** `int` — If the entity is a vehicle it will return 0-1000
 If the entity is a ped it will return 0-200
 If the entity is an object it will return 0

**Descripción oficial:**

Only works for vehicle and peds

---
### GetEntityMaxHealth

`GET_ENTITY_MAX_HEALTH` · hash `0xC7AE6AA1` · **Servidor**

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

Currently it only works with peds.

---
### GetEntityModel

`GET_ENTITY_MODEL` · hash `0xDAFCB3EC` · **Servidor**

```lua
local retval = GetEntityModel(entity)
```
```c
Hash GET_ENTITY_MODEL(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Hash`

---
### GetEntityOrphanMode

`GET_ENTITY_ORPHAN_MODE` · hash `0xD16EA02F` · **Servidor**

```lua
local retval = GetEntityOrphanMode(entity)
```
```c
int GET_ENTITY_ORPHAN_MODE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the orphan mode of

**Devuelve:** `int` — Returns the entities current orphan mode, refer to enum in [SET_ENTITY_ORPHAN_MODE](#setentityorphanmode)

---
### GetEntityPopulationType

`GET_ENTITY_POPULATION_TYPE` · hash `0xFC30DDFF` · **Servidor**

```lua
local retval = GetEntityPopulationType(entity)
```
```c
int GET_ENTITY_POPULATION_TYPE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): the entity to obtain the population type from

**Devuelve:** `int` — Returns the population type ID, defined by the below enumeration:```cpp enum ePopulationType
 {
 	POPTYPE_UNKNOWN = 0,
 	POPTYPE_RANDOM_PERMANENT,
 	POPTYPE_RANDOM_PARKED,
 	POPTYPE_RANDOM_PATROL,
 	POPTYPE_RANDOM_SCENARIO,
 	POPTYPE_RANDOM_AMBIENT,
 	POPTYPE_PERMANENT,
 	POPTYPE_MISSION,
 	POPTYPE_REPLAY,
 	POPTYPE_CACHE,
 	POPTYPE_TOOL
 }; ```

**Descripción oficial:**

This native gets an entity's population type.

---
### GetEntityRemoteSyncedScenesAllowed

`GET_ENTITY_REMOTE_SYNCED_SCENES_ALLOWED` · hash `0x91B38FB6` · **Servidor**

```lua
local retval = GetEntityRemoteSyncedScenesAllowed(entity)
```
```c
BOOL GET_ENTITY_REMOTE_SYNCED_SCENES_ALLOWED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the flag for.

**Devuelve:** `BOOL` — Returns if the entity is allowed to participate in network-synchronized scenes initiated by clients that do not own the entity.

---
### GetEntityRotation

`GET_ENTITY_ROTATION` · hash `0x8FF45B04` · **Servidor**

```lua
local retval = GetEntityRotation(entity)
```
```c
Vector3 GET_ENTITY_ROTATION(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vector3`

---
### GetEntityRotationVelocity

`GET_ENTITY_ROTATION_VELOCITY` · hash `0x9BF8A73F` · **Servidor**

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
### GetEntityRoutingBucket

`GET_ENTITY_ROUTING_BUCKET` · hash `0xED4B0486` · **Servidor**

```lua
local retval = GetEntityRoutingBucket(entity)
```
```c
int GET_ENTITY_ROUTING_BUCKET(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the routing bucket for.

**Devuelve:** `int` — The routing bucket ID.

**Descripción oficial:**

Gets the routing bucket for the specified entity.

Routing buckets are also known as 'dimensions' or 'virtual worlds' in past echoes, however they are population-aware.

---
### GetEntityScript

`GET_ENTITY_SCRIPT` · hash `0xB7F70784` · **Servidor**

```lua
local retval = GetEntityScript(entity)
```
```c
char* GET_ENTITY_SCRIPT(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `char*`

---
### GetEntitySpeed

`GET_ENTITY_SPEED` · hash `0x9E1E4798` · **Servidor**

```lua
local retval = GetEntitySpeed(entity)
```
```c
float GET_ENTITY_SPEED(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the speed of

**Devuelve:** `float` — The speed of the entity in meters per second

**Descripción oficial:**

Gets the current speed of the entity in meters per second.

```
To convert to MPH: speed * 2.236936
To convert to KPH: speed * 3.6
```

---
### GetEntityType

`GET_ENTITY_TYPE` · hash `0xB1BD08D` · **Servidor**

```lua
local retval = GetEntityType(entity)
```
```c
int GET_ENTITY_TYPE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the type of.

**Devuelve:** `int` — The entity type returned as an integer value.

**Descripción oficial:**

Gets the entity type (as an integer), which can be one of the following defined down below:

**The following entities will return type `1`:**

*   Ped
*   Player
*   Animal (Red Dead Redemption 2)
*   Horse (Red Dead Redemption 2)

**The following entities will return type `2`:**

*   Automobile
*   Bike
*   Boat
*   Heli
*   Plane
*   Submarine
*   Trailer
*   Train
*   DraftVeh (Red Dead Redemption 2)

**The following entities will return type `3`:**

*   Object
*   Door
*   Pickup

Otherwise, a value of `0` will be returned.

---
### GetEntityVelocity

`GET_ENTITY_VELOCITY` · hash `0xC14C9B6B` · **Servidor**

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
### GetGameTimer

`GET_GAME_TIMER` · hash `0xA4EA0691` · **Servidor**

```lua
local retval = GetGameTimer()
```
```c
long GET_GAME_TIMER();
```

**Devuelve:** `long` — The game time.

**Descripción oficial:**

Gets the current game timer in milliseconds.

---
### GetHashKey

`GET_HASH_KEY` · hash `0x98EFF6F1` · **Servidor**

```lua
local retval = GetHashKey(model)
```
```c
Hash GET_HASH_KEY(char* model);
```

**Parámetros**

- `model` (`char*`)

**Devuelve:** `Hash`

**Descripción oficial:**

This native converts the passed string to a hash.

---
### GetHeliBodyHealth

`GET_HELI_BODY_HEALTH` · hash `0xA886495D` · **Servidor**

```lua
local retval = GetHeliBodyHealth(heli)
```
```c
int GET_HELI_BODY_HEALTH(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `int` — Returns the current health of the helicopter's body.

**Descripción oficial:**

**Note** This native will always return `1000.0` unless [SET_VEHICLE_BODY_HEALTH](#setvehiclebodyhealth), [SET_VEHICLE_ENGINE_HEALTH](../gta5/VEHICLE-2.md#setvehicleenginehealth), or [SET_VEHICLE_PETROL_TANK_HEALTH](../gta5/VEHICLE-2.md#setvehiclepetroltankhealth) have been called with a value greater than `1000.0`.

---
### GetHeliDisableExplodeFromBodyDamage

`GET_HELI_DISABLE_EXPLODE_FROM_BODY_DAMAGE` · hash `0x82AFC0A3` · **Servidor**

```lua
local retval = GetHeliDisableExplodeFromBodyDamage(heli)
```
```c
BOOL GET_HELI_DISABLE_EXPLODE_FROM_BODY_DAMAGE(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `BOOL` — Returns `true` if the helicopter is set to be protected from exploding due to minor body damage, `false` otherwise.

**Descripción oficial:**

This is a getter for [SET_DISABLE_HELI_EXPLODE_FROM_BODY_DAMAGE](../gta5/VEHICLE-1.md#setdisableheliexplodefrombodydamage)

---
### GetHeliEngineHealth

`GET_HELI_ENGINE_HEALTH` · hash `0xA0FA0354` · **Servidor**

```lua
local retval = GetHeliEngineHealth(heli)
```
```c
int GET_HELI_ENGINE_HEALTH(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `int` — Returns the current health of the helicopter's engine.

**Descripción oficial:**

**Note** This native will always return `1000.0` unless [SET_VEHICLE_BODY_HEALTH](#setvehiclebodyhealth), [SET_VEHICLE_ENGINE_HEALTH](../gta5/VEHICLE-2.md#setvehicleenginehealth), or [SET_VEHICLE_PETROL_TANK_HEALTH](../gta5/VEHICLE-2.md#setvehiclepetroltankhealth) have been called with a value greater than `1000.0`.

---
### GetHeliGasTankHealth

`GET_HELI_GAS_TANK_HEALTH` · hash `0xD4EC7858` · **Servidor**

```lua
local retval = GetHeliGasTankHealth(heli)
```
```c
int GET_HELI_GAS_TANK_HEALTH(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `int` — Returns the current health of the helicopter's gas tank.

**Descripción oficial:**

**Note** This native will always return `1000.0` unless [SET_VEHICLE_BODY_HEALTH](#setvehiclebodyhealth), [SET_VEHICLE_ENGINE_HEALTH](../gta5/VEHICLE-2.md#setvehicleenginehealth), or [SET_VEHICLE_PETROL_TANK_HEALTH](../gta5/VEHICLE-2.md#setvehiclepetroltankhealth) have been called with a value greater than `1000.0`.

---
### GetHeliMainRotorDamageScale

`GET_HELI_MAIN_ROTOR_DAMAGE_SCALE` · hash `0xC37D668` · **Servidor**

```lua
local retval = GetHeliMainRotorDamageScale(heli)
```
```c
float GET_HELI_MAIN_ROTOR_DAMAGE_SCALE(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `float` — Returns a value representing the damage scaling factor applied to the helicopter's main rotor. The value ranges from `0.0` (no damage scaling) to`  1.0 ` (full damage scaling).

---
### GetHeliMainRotorHealth

`GET_HELI_MAIN_ROTOR_HEALTH` · hash `0xF01E2AAB` · **Servidor**

```lua
local retval = GetHeliMainRotorHealth(vehicle)
```
```c
float GET_HELI_MAIN_ROTOR_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `float` — See the client-side [GET_HELI_MAIN_ROTOR_HEALTH](#gethelimainrotorhealth) for the return value.

---
### GetHeliPitchControl

`GET_HELI_PITCH_CONTROL` · hash `0x1944AC95` · **Servidor**

```lua
local retval = GetHeliPitchControl(heli)
```
```c
float GET_HELI_PITCH_CONTROL(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check.

**Devuelve:** `float` — Returns a value representing the pitch control of the helicopter. The values range from `-1.0` (nose down) to `1.0` (nose up), with `0.0` indicating no pitch input.

---
### GetHeliRearRotorDamageScale

`GET_HELI_REAR_ROTOR_DAMAGE_SCALE` · hash `0xC40161E2` · **Servidor**

```lua
local retval = GetHeliRearRotorDamageScale(heli)
```
```c
float GET_HELI_REAR_ROTOR_DAMAGE_SCALE(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `float` — Returns a value representing the damage scaling factor applied to the helicopter's rear rotor. The value ranges from `0.0` (no damage scaling) to`  1.0 ` (full damage scaling).

---
### GetHeliRearRotorHealth

`GET_HELI_REAR_ROTOR_HEALTH` · hash `0x33EE6E2B` · **Servidor**

```lua
local retval = GetHeliRearRotorHealth(vehicle)
```
```c
float GET_HELI_REAR_ROTOR_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `float` — Returns the health of the helicopter's rear rotor. The maximum health value is `1000`.

**Descripción oficial:**

This native is a getter for [SET_HELI_TAIL_ROTOR_HEALTH](../gta5/VEHICLE-1.md#sethelitailrotorhealth)

---
### GetHeliRollControl

`GET_HELI_ROLL_CONTROL` · hash `0x12948DE9` · **Servidor**

```lua
local retval = GetHeliRollControl(heli)
```
```c
float GET_HELI_ROLL_CONTROL(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check.

**Devuelve:** `float` — Returns a value representing the roll control of the helicopter. The values range from `-1.0` (roll left) to `1.0` (roll right), with `0.0` indicating no roll input.

---
### GetHeliTailRotorDamageScale

`GET_HELI_TAIL_ROTOR_DAMAGE_SCALE` · hash `0x22239130` · **Servidor**

```lua
local retval = GetHeliTailRotorDamageScale(heli)
```
```c
float GET_HELI_TAIL_ROTOR_DAMAGE_SCALE(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `float` — Returns a value representing the damage scaling factor applied to the helicopter's tail rotor. The value ranges from `0.0` (no damage scaling) to`  1.0 ` (full damage scaling).

---
### GetHeliTailRotorHealth

`GET_HELI_TAIL_ROTOR_HEALTH` · hash `0xA41BC13D` · **Servidor**

```lua
local retval = GetHeliTailRotorHealth(vehicle)
```
```c
float GET_HELI_TAIL_ROTOR_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `float` — Return the health of the rear rotor of the helicopter, not the tail rotor.

**Descripción oficial:**

**Note**: This native is deprecated, please use [`GET_HELI_REAR_ROTOR_HEALTH`](#gethelirearrotorhealth) instead.

---
### GetHeliThrottleControl

`GET_HELI_THROTTLE_CONTROL` · hash `0x8E86238D` · **Servidor**

```lua
local retval = GetHeliThrottleControl(heli)
```
```c
float GET_HELI_THROTTLE_CONTROL(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check.

**Devuelve:** `float` — Returns a value representing the throttle control of the helicopter. The value ranges from `0.0` (no throttle) to `2.0` (full throttle).

---
### GetHeliYawControl

`GET_HELI_YAW_CONTROL` · hash `0x8FDC0768` · **Servidor**

```lua
local retval = GetHeliYawControl(heli)
```
```c
float GET_HELI_YAW_CONTROL(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check.

**Devuelve:** `float` — Returns a value the yaw control of the helicopter. The value ranges from `-1.0` (yaw left) to `1.0` (yaw right), with `0.0` meaning no yaw input.

---
### GetHostId

`GET_HOST_ID` · hash `0x5F70F5A3` · **Servidor**

```lua
local retval = GetHostId()
```
```c
char* GET_HOST_ID();
```

**Devuelve:** `char*`

---
### GetIsHeliEngineRunning

`GET_IS_HELI_ENGINE_RUNNING` · hash `0x3EFE38D1` · **Servidor**

```lua
local retval = GetIsHeliEngineRunning(heli)
```
```c
BOOL GET_IS_HELI_ENGINE_RUNNING(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `BOOL` — Returns `true` if the helicopter's engine is running, `false` if it is not.

---
### GetIsVehicleEngineRunning

`GET_IS_VEHICLE_ENGINE_RUNNING` · hash `0x7DC6D022` · **Servidor**

```lua
local retval = GetIsVehicleEngineRunning(vehicle)
```
```c
BOOL GET_IS_VEHICLE_ENGINE_RUNNING(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### GetIsVehiclePrimaryColourCustom

`GET_IS_VEHICLE_PRIMARY_COLOUR_CUSTOM` · hash `0xD7EC8760` · **Servidor**

```lua
local retval = GetIsVehiclePrimaryColourCustom(vehicle)
```
```c
BOOL GET_IS_VEHICLE_PRIMARY_COLOUR_CUSTOM(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### GetIsVehicleSecondaryColourCustom

`GET_IS_VEHICLE_SECONDARY_COLOUR_CUSTOM` · hash `0x288AD228` · **Servidor**

```lua
local retval = GetIsVehicleSecondaryColourCustom(vehicle)
```
```c
BOOL GET_IS_VEHICLE_SECONDARY_COLOUR_CUSTOM(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### GetLandingGearState

`GET_LANDING_GEAR_STATE` · hash `0xA6F02670` · **Servidor**

```lua
local retval = GetLandingGearState(vehicle)
```
```c
int GET_LANDING_GEAR_STATE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `int` — The current state of the vehicles landing gear.

**Descripción oficial:**

See the client-side [GET_LANDING_GEAR_STATE](#getlandinggearstate) native for a description of landing gear states.

---
### GetLastPedInVehicleSeat

`GET_LAST_PED_IN_VEHICLE_SEAT` · hash `0xF7C6792D` · **Servidor**

```lua
local retval = GetLastPedInVehicleSeat(vehicle, seatIndex)
```
```c
Entity GET_LAST_PED_IN_VEHICLE_SEAT(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](../gta5/VEHICLE-1.md#isvehicleseatfree).

**Devuelve:** `Entity` — The last ped in the specified seat of the passed vehicle. Returns 0 if the specified seat was never occupied or the last ped does not exist anymore.

---
### GetNetTypeFromEntity

`GET_NET_TYPE_FROM_ENTITY` · hash `0x23B2A641` · **Servidor**

```lua
local retval = GetNetTypeFromEntity(entity)
```
```c
int GET_NET_TYPE_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the specific type of.

**Devuelve:** `int` — The specific entity type returned as an integer value or -1 if the entity is invalid.

**Descripción oficial:**

Gets the specific entity type (as an integer), which can be one of the following defined down below:

**FiveM:**

```cpp
enum eNetObjEntityType
{
    Automobile = 0,
    Bike = 1,
    Boat = 2,
    Door = 3,
    Heli = 4,
    Object = 5,
    Ped = 6,
    Pickup = 7,
    PickupPlacement = 8,
    Plane = 9,
    Submarine = 10,
    Player = 11,
    Trailer = 12,
    Train = 13
};
```

**RedM:**

```cpp
enum eNetObjEntityType
{
    Animal = 0,
    Automobile = 1,
    Bike = 2,
    Boat = 3,
    Door = 4,
    Heli = 5,
    Object = 6,
    Ped = 7,
    Pickup = 8,
    PickupPlacement = 9,
    Plane = 10,
    Submarine = 11,
    Player = 12,
    Trailer = 13,
    Train = 14,
    DraftVeh = 15,
    StatsTracker = 16,
    PropSet = 17,
    AnimScene = 18,
    GroupScenario = 19,
    Herd = 20,
    Horse = 21,
    WorldState = 22,
    WorldProjectile = 23,
    Incident = 24,
    Guardzone = 25,
    PedGroup = 26,
    CombatDirector = 27,
    PedSharedTargeting = 28,
    Persistent = 29
};
```

---
### GetNumPlayerIdentifiers

`GET_NUM_PLAYER_IDENTIFIERS` · hash `0xFF7F66AB` · **Servidor**

```lua
local retval = GetNumPlayerIdentifiers(playerSrc)
```
```c
int GET_NUM_PLAYER_IDENTIFIERS(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `int`

---
### GetNumPlayerIndices

`GET_NUM_PLAYER_INDICES` · hash `0x63D13184` · **Servidor**

```lua
local retval = GetNumPlayerIndices()
```
```c
int GET_NUM_PLAYER_INDICES();
```

**Devuelve:** `int`

---
### GetNumPlayerTokens

`GET_NUM_PLAYER_TOKENS` · hash `0x619E4A3D` · **Servidor**

```lua
local retval = GetNumPlayerTokens(playerSrc)
```
```c
int GET_NUM_PLAYER_TOKENS(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `int`

---
### GetPasswordHash

`GET_PASSWORD_HASH` · hash `0x23473EA4` · **Servidor**

```lua
local retval = GetPasswordHash(password)
```
```c
char* GET_PASSWORD_HASH(char* password);
```

**Parámetros**

- `password` (`char*`)

**Devuelve:** `char*`

---
### GetPedArmour

`GET_PED_ARMOUR` · hash `0x2CE311A7` · **Servidor**

```lua
local retval = GetPedArmour(ped)
```
```c
int GET_PED_ARMOUR(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetPedCauseOfDeath

`GET_PED_CAUSE_OF_DEATH` · hash `0x63458C27` · **Servidor**

```lua
local retval = GetPedCauseOfDeath(ped)
```
```c
Hash GET_PED_CAUSE_OF_DEATH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Hash`

---
### GetPedDesiredHeading

`GET_PED_DESIRED_HEADING` · hash `0xC182F76E` · **Servidor**

```lua
local retval = GetPedDesiredHeading(ped)
```
```c
float GET_PED_DESIRED_HEADING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `float` — Returns ped's desired heading.

---
### GetPedInVehicleSeat

`GET_PED_IN_VEHICLE_SEAT` · hash `0x388FDE9A` · **Servidor**

```lua
local retval = GetPedInVehicleSeat(vehicle, seatIndex)
```
```c
Entity GET_PED_IN_VEHICLE_SEAT(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](../gta5/VEHICLE-1.md#isvehicleseatfree).

**Devuelve:** `Entity` — The ped in the specified seat of the passed vehicle. Returns 0 if the specified seat is not occupied.

---
### GetPedMaxHealth

`GET_PED_MAX_HEALTH` · hash `0xA45B6C8D` · **Servidor**

```lua
local retval = GetPedMaxHealth(ped)
```
```c
int GET_PED_MAX_HEALTH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetPedRelationshipGroupHash

`GET_PED_RELATIONSHIP_GROUP_HASH` · hash `0x354F283C` · **Servidor**

```lua
local retval = GetPedRelationshipGroupHash(ped)
```
```c
Hash GET_PED_RELATIONSHIP_GROUP_HASH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `Hash` — The relationship group hash.

**Descripción oficial:**

Gets the current relationship group hash of a ped.

---
### GetPedScriptTaskCommand

`GET_PED_SCRIPT_TASK_COMMAND` · hash `0x84FE084` · **Servidor**

```lua
local retval = GetPedScriptTaskCommand(ped)
```
```c
Hash GET_PED_SCRIPT_TASK_COMMAND(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `Hash` — The script task command currently assigned to the ped. A value of 0x811E343C denotes no script task is assigned.

**Descripción oficial:**

Gets the script task command currently assigned to the ped.

---
### GetPedScriptTaskStage

`GET_PED_SCRIPT_TASK_STAGE` · hash `0x44B0E5E2` · **Servidor**

```lua
local retval = GetPedScriptTaskStage(ped)
```
```c
int GET_PED_SCRIPT_TASK_STAGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `int` — The stage of the ped's scripted task. A value of 3 denotes no script task is assigned.

**Descripción oficial:**

Gets the stage of the peds scripted task.

---
### GetPedSourceOfDamage

`GET_PED_SOURCE_OF_DAMAGE` · hash `0x535DB43F` · **Servidor**

```lua
local retval = GetPedSourceOfDamage(ped)
```
```c
Entity GET_PED_SOURCE_OF_DAMAGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `Entity` — The entity id. Returns 0 if the ped has not been damaged recently.

**Descripción oficial:**

Get the last entity that damaged the ped. This native is used server side when using OneSync.

---
### GetPedSourceOfDeath

`GET_PED_SOURCE_OF_DEATH` · hash `0x84ADF9EB` · **Servidor**

```lua
local retval = GetPedSourceOfDeath(ped)
```
```c
Entity GET_PED_SOURCE_OF_DEATH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `Entity` — The entity id. Returns 0 if the ped has no killer.

**Descripción oficial:**

Get the entity that killed the ped. This native is used server side when using OneSync.

---
### GetPedSpecificTaskType

`GET_PED_SPECIFIC_TASK_TYPE` · hash `0x7F4563D3` · **Servidor**

```lua
local retval = GetPedSpecificTaskType(ped, index)
```
```c
int GET_PED_SPECIFIC_TASK_TYPE(Ped ped, int index);
```

**Parámetros**

- `ped` (`Ped`): The target ped.
- `index` (`int`): A zero-based index with a maximum value of 7.

**Devuelve:** `int` — The type of the specific task.
 1604: A value of 530 denotes no script task is assigned or an invalid input was given.
 2060+: A value of 531 denotes no script task is assigned or an invalid input was given.

**Descripción oficial:**

Gets the type of a ped's specific task given an index of the CPedTaskSpecificDataNode nodes.
A ped will typically have a task at index 0, if a ped has multiple tasks at once they will be in the order 0, 1, 2, etc.

---
### GetPedStealthMovement

`GET_PED_STEALTH_MOVEMENT` · hash `0x40321B83` · **Servidor**

```lua
local retval = GetPedStealthMovement(ped)
```
```c
bool GET_PED_STEALTH_MOVEMENT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `bool` — Whether or not the ped is stealthy.

---
### GetPlayerCameraRotation

`GET_PLAYER_CAMERA_ROTATION` · hash `0x433C765D` · **Servidor**

```lua
local retval = GetPlayerCameraRotation(playerSrc)
```
```c
Vector3 GET_PLAYER_CAMERA_ROTATION(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle.

**Devuelve:** `Vector3` — The player's camera rotation. Values are in radians.

**Descripción oficial:**

Gets the current camera rotation for a specified player. This native is used server side when using OneSync.

---
### GetPlayerEndpoint

`GET_PLAYER_ENDPOINT` · hash `0xFEE404F9` · **Servidor**

```lua
local retval = GetPlayerEndpoint(playerSrc)
```
```c
char* GET_PLAYER_ENDPOINT(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `char*`

---
### GetPlayerFakeWantedLevel

`GET_PLAYER_FAKE_WANTED_LEVEL` · hash `0x98D244` · **Servidor**

```lua
local retval = GetPlayerFakeWantedLevel(playerSrc)
```
```c
int GET_PLAYER_FAKE_WANTED_LEVEL(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The target player

**Devuelve:** `int` — The fake wanted level

**Descripción oficial:**

Gets the current fake wanted level for a specified player. This native is used server side when using OneSync.

---
### GetPlayerFocusPos

`GET_PLAYER_FOCUS_POS` · hash `0x586F80FF` · **Servidor**

```lua
local retval = GetPlayerFocusPos(playerSrc)
```
```c
Vector3 GET_PLAYER_FOCUS_POS(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player to get the focus position of

**Devuelve:** `Vector3` — Returns a `Vector3` containing the focus position of the player.

**Descripción oficial:**

Gets the focus position (i.e. the position of the active camera in the game world) of a player.

---
### GetPlayerFromIndex

`GET_PLAYER_FROM_INDEX` · hash `0xC8A9CE08` · **Servidor**

```lua
local retval = GetPlayerFromIndex(index)
```
```c
char* GET_PLAYER_FROM_INDEX(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `char*`

---
### GetPlayerGuid

`GET_PLAYER_GUID` · hash `0xE52D9680` · **Servidor**

```lua
local retval = GetPlayerGuid(playerSrc)
```
```c
char* GET_PLAYER_GUID(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `char*`

---
### GetPlayerIdentifier

`GET_PLAYER_IDENTIFIER` · hash `0x7302DBCF` · **Servidor**

```lua
local retval = GetPlayerIdentifier(playerSrc, identiferIndex)
```
```c
char* GET_PLAYER_IDENTIFIER(char* playerSrc, int identiferIndex);
```

**Parámetros**

- `playerSrc` (`char*`)
- `identiferIndex` (`int`)

**Devuelve:** `char*` — Returns the identifier at the specific index, if out of bounds returns `null`

**Descripción oficial:**

To get the number of identifiers, use [GET_NUM_PLAYER_IDENTIFIERS](#getnumplayeridentifiers)

To get a specific type of identifier, use [GET_PLAYER_IDENTIFIER_BY_TYPE](#getplayeridentifierbytype)

---
### GetPlayerIdentifierByType

`GET_PLAYER_IDENTIFIER_BY_TYPE` · hash `0xA61C8FC6` · **Servidor**

```lua
local retval = GetPlayerIdentifierByType(playerSrc, identifierType)
```
```c
char* GET_PLAYER_IDENTIFIER_BY_TYPE(char* playerSrc, char* identifierType);
```

**Parámetros**

- `playerSrc` (`char*`): The player to get the identifier for
- `identifierType` (`char*`): The string to match in an identifier, this can be `"license"` for example.

**Devuelve:** `char*` — The identifier that matches the string provided

**Descripción oficial:**

Get an identifier from a player by the type of the identifier.
Known [Identifiers](https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/GetPlayerIdentifiers/#identifier-types)

**Ejemplo (lua):**

```lua
local playerLicenses = {}

AddEventHandler('playerJoining', function()
    playerLicenses[source] = GetPlayerIdentifierByType(source, 'license')
end)
```

**Ejemplo (js):**

```js
let playerLicenses = {};

on('playerJoining', () => {
    playerLicenses[source] = GetPlayerIdentifierByType(source, 'license');
});
```

**Ejemplo (cs):**

```cs
using System.Collections.Generic;
using static CitizenFX.Core.Native.API;
// ...

// In class
private Dictionary<int, string> PlayerLicenses = new Dictionary<int, string>();

// In class constructor
EventHandlers["playerJoining"] += new Action<Player>(SetLicense);

// Delegate method
private void SetLicense([FromSource]Player player) {
    PlayerLicenses.Add(player.Handle, GetPlayerIdentifierByType(player.Handle, "license"));
}
```

---
### GetPlayerInvincible

`GET_PLAYER_INVINCIBLE` · hash `0x680C90EE` · **Servidor**

```lua
local retval = GetPlayerInvincible(playerSrc)
```
```c
BOOL GET_PLAYER_INVINCIBLE(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `BOOL` — A boolean to tell if the player is invincible.

---
### GetPlayerLastMsg

`GET_PLAYER_LAST_MSG` · hash `0x427E8E6A` · **Servidor**

```lua
local retval = GetPlayerLastMsg(playerSrc)
```
```c
int GET_PLAYER_LAST_MSG(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `int`

---
### GetPlayerMaxArmour

`GET_PLAYER_MAX_ARMOUR` · hash `0x2A50657` · **Servidor**

```lua
local retval = GetPlayerMaxArmour(playerSrc)
```
```c
int GET_PLAYER_MAX_ARMOUR(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `int`

---
### GetPlayerMaxHealth

`GET_PLAYER_MAX_HEALTH` · hash `0x8154E470` · **Servidor**

```lua
local retval = GetPlayerMaxHealth(playerSrc)
```
```c
int GET_PLAYER_MAX_HEALTH(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `int`

---
### GetPlayerName

`GET_PLAYER_NAME` · hash `0x406B4B20` · **Servidor**

```lua
local retval = GetPlayerName(playerSrc)
```
```c
char* GET_PLAYER_NAME(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `char*`

---
### GetPlayerPed

`GET_PLAYER_PED` · hash `0x6E31E993` · **Servidor**

```lua
local retval = GetPlayerPed(playerSrc)
```
```c
Entity GET_PLAYER_PED(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player source, passed as a string.

**Devuelve:** `Entity` — Returns a valid Ped Entity ID if the passed `playerSrc` is valid, `0` if not.

**Descripción oficial:**

Used to get the player's Ped Entity ID when a valid `playerSrc` is passed.

**Ejemplo (lua):**

```lua
-- Let's assume source is a valid ID
local pedId = GetPlayerPed(source);

-- If pedId is valid (not equal to 0)
if pedId ~= 0 then
    -- Do something with this ped!
end
```

---
### GetPlayerPeerStatistics

`GET_PLAYER_PEER_STATISTICS` · hash `0x9A928294` · **Servidor**

```lua
local retval = GetPlayerPeerStatistics(playerSrc, peerStatistic)
```
```c
int GET_PLAYER_PEER_STATISTICS(char* playerSrc, int peerStatistic);
```

**Parámetros**

- `playerSrc` (`char*`): The player to get the stats of
- `peerStatistic` (`int`): The statistic to get, this will error if its out of range

**Devuelve:** `int` — See `ENetStatisticType` for what this will return.

**Descripción oficial:**

```cpp
const int ENET_PACKET_LOSS_SCALE = 65536;

enum PeerStatistics
{
	// PacketLoss will only update once every 10 seconds, use PacketLossEpoch if you want the time
	// since the last time the packet loss was updated.

	// the amount of packet loss the player has, needs to be scaled with PACKET_LOSS_SCALE
	PacketLoss = 0,
	// The variance in the packet loss
	PacketLossVariance = 1,
	// The time since the last packet update in ms, relative to the peers connection time
	PacketLossEpoch = 2,
	// The mean amount of time it takes for a packet to get to the client (ping)
	RoundTripTime = 3,
	// The variance in the round trip time
	RoundTripTimeVariance = 4,
	// Despite their name, these are only updated once every 5 seconds, you can get the last time this was updated with PacketThrottleEpoch
	// The last recorded round trip time of a packet
	LastRoundTripTime = 5,
	// The last round trip time variance
	LastRoundTripTimeVariance = 6,
	// The time since the last packet throttle update, relative to the peers connection time
	PacketThrottleEpoch = 7,
};
```

These statistics only update once every 10 seconds.

**Ejemplo (js):**

```js

setInterval(() => {
	const ENET_PACKET_LOSS_SCALE = 65536;

	const PLAYER_SERVER_ID = 1;

	const packetLoss = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 0 /* PacketLoss */);
	const packetLossVariance = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 1 /* PacketLossVariance */);
	const packetLossEpoch = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 2 /* PacketLossEpoch */)
	const rtt = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 3 /* RoundTripTime */);
	const rttVariance = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 4 /* RoundTripTimeVariance */);
	const lastRtt = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 5 /* LastRoundTripTime */);
	const lastRttVariance = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 6 /* LastRoundTripTimeVariance */);
	const packetThrottleEpoch = GetPlayerPeerStatistics(PLAYER_SERVER_ID, 7 /* PacketThrottleEpoch */);

	console.log(`packetLoss: ${packetLoss}`);
	console.log(`packetLossVariance: ${packetLossVariance}`);
	console.log(`packetLossEpch: ${packetLossEpoch}`);

	console.log(`packetLossScaled: ${packetLoss / ENET_PACKET_LOSS_SCALE}`);
	console.log(`packetLossVarianceScaled: ${packetLossVariance / ENET_PACKET_LOSS_SCALE}`);

	console.log(`rtt: ${rtt}`);
	console.log(`rttVariance: ${rttVariance}`);

	console.log(`lastRtt: ${lastRtt}`);
	console.log(`lastRttVariance: ${lastRttVariance}`);
	console.log(`packetThrottleEpoch: ${packetThrottleEpoch}`);
}, 10000)
```

---
### GetPlayerPing

`GET_PLAYER_PING` · hash `0xFF1290D4` · **Servidor**

```lua
local retval = GetPlayerPing(playerSrc)
```
```c
int GET_PLAYER_PING(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`)

**Devuelve:** `int` — Returns the mean amount of time a packet takes to get to the client

**Descripción oficial:**

See [GET_PLAYER_PEER_STATISTICS](#getplayerpeerstatistics) if you want more detailed information, like packet loss, and packet/rtt variance

---
### GetPlayerRoutingBucket

`GET_PLAYER_ROUTING_BUCKET` · hash `0x52441C34` · **Servidor**

```lua
local retval = GetPlayerRoutingBucket(playerSrc)
```
```c
int GET_PLAYER_ROUTING_BUCKET(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player to get the routing bucket for.

**Devuelve:** `int` — The routing bucket ID.

**Descripción oficial:**

Gets the routing bucket for the specified player.

Routing buckets are also known as 'dimensions' or 'virtual worlds' in past echoes, however they are population-aware.

---
### GetPlayerTeam

`GET_PLAYER_TEAM` · hash `0x9873E404` · **Servidor**

```lua
local retval = GetPlayerTeam(playerSrc)
```
```c
int GET_PLAYER_TEAM(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `int`

---
### GetPlayerTimeInPursuit

`GET_PLAYER_TIME_IN_PURSUIT` · hash `0x7ADE63E1` · **Servidor**

```lua
local retval = GetPlayerTimeInPursuit(playerSrc, lastPursuit)
```
```c
int GET_PLAYER_TIME_IN_PURSUIT(char* playerSrc, BOOL lastPursuit);
```

**Parámetros**

- `playerSrc` (`char*`): The target player
- `lastPursuit` (`BOOL`): False = CurrentPursuit, True = LastPursuit

**Devuelve:** `int` — Returns -1, if the player is not wanted or wasn't in pursuit before, depending on the lastPursuit parameter
 Returns 0, if lastPursuit == False and the player has a wanted level, but the pursuit has not started yet
 Otherwise, will return the milliseconds of the pursuit.

**Descripción oficial:**

```
Gets the amount of time player has spent evading the cops.
Counter starts and increments only when cops are chasing the player.
If the player is evading, the timer will pause.
```

---
### GetPlayerTimeOnline

`GET_PLAYER_TIME_ONLINE` · hash `0x67D2E605` · **Servidor**

```lua
local retval = GetPlayerTimeOnline(playerSrc)
```
```c
int GET_PLAYER_TIME_ONLINE(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): A player.

**Devuelve:** `int` — The current time online in seconds.

**Descripción oficial:**

Gets the current time online for a specified player.

**Ejemplo (lua):**

```lua
local function ShowTimeOnline()
    local player = source
    local secondsTotalOnline = GetPlayerTimeOnline(player)

    print(("Time online : %f H %f min %f"):format(
        (secondsTotalOnline / 3600),
        ((secondsTotalOnline / 60) % 60),
        (secondsTotalOnline % 60)
    ))
end

RegisterNetEvent("myTimeOnline", ShowTimeOnline)
```

---
### GetPlayerToken

`GET_PLAYER_TOKEN` · hash `0x54C06897` · **Servidor**

```lua
local retval = GetPlayerToken(playerSrc, index)
```
```c
char* GET_PLAYER_TOKEN(char* playerSrc, int index);
```

**Parámetros**

- `playerSrc` (`char*`): A player.
- `index` (`int`): Index between 0 and GET_NUM_PLAYER_TOKENS.

**Devuelve:** `char*` — A token value.

**Descripción oficial:**

Gets a player's token. Tokens can be used to enhance banning logic, however are specific to a server.

---
### GetPlayerWantedCentrePosition

`GET_PLAYER_WANTED_CENTRE_POSITION` · hash `0x821F2D2C` · **Servidor**

```lua
local retval = GetPlayerWantedCentrePosition(playerSrc)
```
```c
Vector3 GET_PLAYER_WANTED_CENTRE_POSITION(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The target player

**Devuelve:** `Vector3` — The player's position known by police. Vector zero if the player has no wanted level.

**Descripción oficial:**

Gets the current known coordinates for the specified player from cops perspective. This native is used server side when using OneSync.

---
### GetPlayerWantedLevel

`GET_PLAYER_WANTED_LEVEL` · hash `0xBDCDD163` · **Servidor**

```lua
local retval = GetPlayerWantedLevel(playerSrc)
```
```c
int GET_PLAYER_WANTED_LEVEL(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The target player

**Devuelve:** `int` — The wanted level

**Descripción oficial:**

```
Returns given players wanted level server-side.
```

---
### GetResourcePath

`GET_RESOURCE_PATH` · hash `0x61DCF017` · **Servidor**

```lua
local retval = GetResourcePath(resourceName)
```
```c
char* GET_RESOURCE_PATH(char* resourceName);
```

**Parámetros**

- `resourceName` (`char*`): The name of the resource.

**Devuelve:** `char*` — The resource directory name, possibly without trailing slash.

**Descripción oficial:**

Returns the physical on-disk path of the specified resource.

---
### GetSeatPedIsUsing

`GET_SEAT_PED_IS_USING` · hash `0x57B78C17` · **Servidor**

```lua
local retval = GetSeatPedIsUsing(ped)
```
```c
int GET_SEAT_PED_IS_USING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): the ped id

**Devuelve:** `int` — Returns the seat index for specified `ped`, if the ped is not sitting in a vehicle it will return -3.

---
### GetSelectedPedWeapon

`GET_SELECTED_PED_WEAPON` · hash `0xD240123E` · **Servidor**

```lua
local retval = GetSelectedPedWeapon(ped)
```
```c
Hash GET_SELECTED_PED_WEAPON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `Hash` — The weapon hash.

**Descripción oficial:**

An alias of [GET_CURRENT_PED_WEAPON](#getcurrentpedweapon).

Note, the client-side [GET_SELECTED_PED_WEAPON](#getselectedpedweapon) native returns the weapon selected via the HUD (weapon wheel). This data is not available to FXServer.

---
### GetThrusterSideRcsThrottle

`GET_THRUSTER_SIDE_RCS_THROTTLE` · hash `0x1C939E87` · **Servidor**

```lua
local retval = GetThrusterSideRcsThrottle(jetpack)
```
```c
float GET_THRUSTER_SIDE_RCS_THROTTLE(Vehicle jetpack);
```

**Parámetros**

- `jetpack` (`Vehicle`): The jetpack to check.

**Devuelve:** `float` — Returns a value representing the side RCS (Reaction Control System) throttle of the jetpack. The values range from `0.0` (no throttle) to `1.0` (full throttle).

---
### GetThrusterThrottle

`GET_THRUSTER_THROTTLE` · hash `0x94E24C96` · **Servidor**

```lua
local retval = GetThrusterThrottle(jetpack)
```
```c
float GET_THRUSTER_THROTTLE(Vehicle jetpack);
```

**Parámetros**

- `jetpack` (`Vehicle`): The jetpack to check.

**Devuelve:** `float` — Returns a value representing the main throttle of the jetpack. The values range from `0.0` (no throttle) to `1.0` (full throttle)

---
### GetTrainBackwardCarriage

`GET_TRAIN_BACKWARD_CARRIAGE` · hash `0x456E34A` · **Servidor**

```lua
local retval = GetTrainBackwardCarriage(train)
```
```c
int GET_TRAIN_BACKWARD_CARRIAGE(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `int` — The handle of the carriage behind this train in the chain. Otherwise returns 0 if the train is the caboose of the chain.

---
### GetTrainCarriageEngine

`GET_TRAIN_CARRIAGE_ENGINE` · hash `0x95070FA` · **Servidor**

```lua
local retval = GetTrainCarriageEngine(train)
```
```c
int GET_TRAIN_CARRIAGE_ENGINE(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The entity handle.

**Devuelve:** `int` — The train engine carriage.

---
### GetTrainCarriageIndex

`GET_TRAIN_CARRIAGE_INDEX` · hash `0x4B8285CF` · **Servidor**

```lua
local retval = GetTrainCarriageIndex(train)
```
```c
int GET_TRAIN_CARRIAGE_INDEX(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The entity handle.

**Devuelve:** `int` — The carriage index. -1 returned if invalid result.

---
### GetTrainForwardCarriage

`GET_TRAIN_FORWARD_CARRIAGE` · hash `0x24DC88D9` · **Servidor**

```lua
local retval = GetTrainForwardCarriage(train)
```
```c
int GET_TRAIN_FORWARD_CARRIAGE(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `int` — The handle of the carriage in front of this train in the chain. Otherwise returns 0 if the train has no carriage in front of it

---
### GetVehicleBodyHealth

`GET_VEHICLE_BODY_HEALTH` · hash `0x2B2FCC28` · **Servidor**

```lua
local retval = GetVehicleBodyHealth(vehicle)
```
```c
float GET_VEHICLE_BODY_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleColours

`GET_VEHICLE_COLOURS` · hash `0x40D82D88` · **Servidor**

```lua
local colorPrimary, colorSecondary = GetVehicleColours(vehicle)
```
```c
void GET_VEHICLE_COLOURS(Vehicle vehicle, int* colorPrimary, int* colorSecondary);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `colorPrimary` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `colorSecondary` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVehicleCustomPrimaryColour

`GET_VEHICLE_CUSTOM_PRIMARY_COLOUR` · hash `0x1C2B9FEF` · **Servidor**

```lua
local r, g, b = GetVehicleCustomPrimaryColour(vehicle)
```
```c
void GET_VEHICLE_CUSTOM_PRIMARY_COLOUR(Vehicle vehicle, int* r, int* g, int* b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVehicleCustomSecondaryColour

`GET_VEHICLE_CUSTOM_SECONDARY_COLOUR` · hash `0x3FF247A2` · **Servidor**

```lua
local r, g, b = GetVehicleCustomSecondaryColour(vehicle)
```
```c
void GET_VEHICLE_CUSTOM_SECONDARY_COLOUR(Vehicle vehicle, int* r, int* g, int* b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVehicleDashboardColour

`GET_VEHICLE_DASHBOARD_COLOUR` · hash `0xA0DBD08D` · **Servidor**

```lua
local color = GetVehicleDashboardColour(vehicle, color)
```
```c
void GET_VEHICLE_DASHBOARD_COLOUR(Vehicle vehicle, int* color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `color` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetVehicleDirtLevel

`GET_VEHICLE_DIRT_LEVEL` · hash `0xFD15C065` · **Servidor**

```lua
local retval = GetVehicleDirtLevel(vehicle)
```
```c
float GET_VEHICLE_DIRT_LEVEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleDoorLockStatus

`GET_VEHICLE_DOOR_LOCK_STATUS` · hash `0xD72CEF2` · **Servidor**

```lua
local retval = GetVehicleDoorLockStatus(vehicle)
```
```c
int GET_VEHICLE_DOOR_LOCK_STATUS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): A vehicle handle.

**Devuelve:** `int` — The door lock status for the specified vehicle.

**Descripción oficial:**

```lua
enum_VehicleLockStatus = {
    None = 0,
    Locked = 2,
    LockedForPlayer = 3,
    StickPlayerInside = 4, -- Doesn't allow players to exit the vehicle with the exit vehicle key.
    CanBeBrokenInto = 7, -- Can be broken into the car. If the glass is broken, the value will be set to 1
    CanBeBrokenIntoPersist = 8, -- Can be broken into persist
    CannotBeTriedToEnter = 10, -- Cannot be tried to enter (Nothing happens when you press the vehicle enter key).
}
```

It should be [noted](https://forum.cfx.re/t/4863241) that while the [client-side command](#getvehicledoorlockstatus) and its
setter distinguish between states 0 (unset) and 1 (unlocked), the game will synchronize both as state 0, so the server-side
command will return only '0' if unlocked.

---
### GetVehicleDoorStatus

`GET_VEHICLE_DOOR_STATUS` · hash `0x6E35C49C` · **Servidor**

```lua
local retval = GetVehicleDoorStatus(vehicle, doorIndex)
```
```c
int GET_VEHICLE_DOOR_STATUS(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `doorIndex` (`int`): Index of door to check (0-6).

**Devuelve:** `int` — A number from 0 to 7.

**Descripción oficial:**

Returns the open position of the specified door on the target vehicle.

---
### GetVehicleDoorsLockedForPlayer

`GET_VEHICLE_DOORS_LOCKED_FOR_PLAYER` · hash `0x1DC50247` · **Servidor**

```lua
local retval = GetVehicleDoorsLockedForPlayer(vehicle)
```
```c
int GET_VEHICLE_DOORS_LOCKED_FOR_PLAYER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

Currently it only works when set to "all players".

---
### GetVehicleEngineHealth

`GET_VEHICLE_ENGINE_HEALTH` · hash `0x8880038A` · **Servidor**

```lua
local retval = GetVehicleEngineHealth(vehicle)
```
```c
float GET_VEHICLE_ENGINE_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleExtraColours

`GET_VEHICLE_EXTRA_COLOURS` · hash `0x80E4659B` · **Servidor**

```lua
local pearlescentColor, wheelColor = GetVehicleExtraColours(vehicle)
```
```c
void GET_VEHICLE_EXTRA_COLOURS(Vehicle vehicle, int* pearlescentColor, int* wheelColor);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `pearlescentColor` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `wheelColor` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVehicleFlightNozzlePosition

`GET_VEHICLE_FLIGHT_NOZZLE_POSITION` · hash `0xAD40AD55` · **Servidor**

```lua
local retval = GetVehicleFlightNozzlePosition(vehicle)
```
```c
float GET_VEHICLE_FLIGHT_NOZZLE_POSITION(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `float` — The flight nozzel position between 0.0 (flying normally) and 1.0 (VTOL mode)

**Descripción oficial:**

Gets the flight nozzel position for the specified vehicle. See the client-side [\_GET_VEHICLE_FLIGHT_NOZZLE_POSITION](#getvehicleflightnozzleposition) native for usage examples.

---
### GetVehicleHeadlightsColour

`GET_VEHICLE_HEADLIGHTS_COLOUR` · hash `0xD7147656` · **Servidor**

```lua
local retval = GetVehicleHeadlightsColour(vehicle)
```
```c
int GET_VEHICLE_HEADLIGHTS_COLOUR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleHomingLockonState

`GET_VEHICLE_HOMING_LOCKON_STATE` · hash `0xFBDE9FD8` · **Servidor**

```lua
local retval = GetVehicleHomingLockonState(vehicle)
```
```c
int GET_VEHICLE_HOMING_LOCKON_STATE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `int` — The lock on state.

**Descripción oficial:**

Gets the lock on state for the specified vehicle. See the client-side [GET_VEHICLE_HOMING_LOCKON_STATE](#getvehiclehominglockonstate) native for a description of lock on states.

---
### GetVehicleHornType

`GET_VEHICLE_HORN_TYPE` · hash `0xDEA49773` · **Servidor**

```lua
local retval = GetVehicleHornType(vehicle)
```
```c
Hash GET_VEHICLE_HORN_TYPE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check the horn type.

**Devuelve:** `Hash` — Returns the vehicle horn type hash, or `0` if one is not set.

**Descripción oficial:**

This is a getter for the client-side native [`START_VEHICLE_HORN`](../gta5/VEHICLE-2.md#startvehiclehorn), which allows you to return the horn type of the vehicle.

**Note**: This native only gets the hash value set with `START_VEHICLE_HORN`. If a wrong hash is passed into `START_VEHICLE_HORN`, it will return this wrong hash.

```cpp
enum eHornTypes
{
    NORMAL = 1330140148,
    HELDDOWN = -2087385909,
    AGGRESSIVE = -92810745
}
```

---
### GetVehicleInteriorColour

`GET_VEHICLE_INTERIOR_COLOUR` · hash `0xCCFF3B6E` · **Servidor**

```lua
local color = GetVehicleInteriorColour(vehicle, color)
```
```c
void GET_VEHICLE_INTERIOR_COLOUR(Vehicle vehicle, int* color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `color` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetVehicleLightsState

`GET_VEHICLE_LIGHTS_STATE` · hash `0x7C278621` · **Servidor**

```lua
local retval, lightsOn, highbeamsOn = GetVehicleLightsState(vehicle)
```
```c
BOOL GET_VEHICLE_LIGHTS_STATE(Vehicle vehicle, BOOL* lightsOn, BOOL* highbeamsOn);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `lightsOn` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `highbeamsOn` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### GetVehicleLivery

`GET_VEHICLE_LIVERY` · hash `0xEC82A51D` · **Servidor**

```lua
local retval = GetVehicleLivery(vehicle)
```
```c
int GET_VEHICLE_LIVERY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleLockOnTarget

`GET_VEHICLE_LOCK_ON_TARGET` · hash `0x4A557117` · **Servidor**

```lua
local retval = GetVehicleLockOnTarget(vehicle)
```
```c
Vehicle GET_VEHICLE_LOCK_ON_TARGET(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `Vehicle` — The vehicle that is locked on. 0 returned if no vehicle is locked on.

**Descripción oficial:**

Gets the vehicle that is locked on to for the specified vehicle.

---
### GetVehicleNeonColour

`GET_VEHICLE_NEON_COLOUR` · hash `0xD9319DCB` · **Servidor**

```lua
local red, green, blue = GetVehicleNeonColour(vehicle)
```
```c
void GET_VEHICLE_NEON_COLOUR(Vehicle vehicle, int* red, int* green, int* blue);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `red` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to an integer where the red component of the neon color will be stored.
- `green` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to an integer where the green component of the neon color will be stored.
- `blue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to an integer where the blue component of the neon color will be stored.

**Devuelve:** `void` — None. The neon color values are retrieved and stored in the `red`, `green`, and `blue` pointers. Make sure to store the returned values in variables for further use.

**Descripción oficial:**

Getter to check the neon colour of a vehicle. This native is the server side getter of [GET_VEHICLE_NEON_LIGHTS_COLOUR](../gta5/VEHICLE-1.md#getvehicleneonlightscolour).

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(GetPlayerPed(1), false) -- 1 is the source here
local red, green, blue = GetVehicleNeonColour(vehicle)
print(red, green, blue)
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(GetPlayerPed(1), false); // 1 is the source here
const [red, green, blue] = GetVehicleNeonColour(vehicle);
console.log(red, green, blue);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(GetPlayerPed(1), false); // 1 is the source here
int red, green, blue;
GetVehicleNeonColour(vehicle, out red, out green, out blue);
Debug.WriteLine($"{red}, {green}, {blue}");
```

---
### GetVehicleNeonEnabled

`GET_VEHICLE_NEON_ENABLED` · hash `0x684BDBF2` · **Servidor**

```lua
local retval = GetVehicleNeonEnabled(vehicle, neonIndex)
```
```c
BOOL GET_VEHICLE_NEON_ENABLED(Vehicle vehicle, int neonIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `neonIndex` (`int`): A value from the neonIndex enum representing the neon light to check.

**Devuelve:** `BOOL` — Returns `true` if the specified neon light is enabled, `false` otherwise.

**Descripción oficial:**

Getter to check if one of the neon lights of a vehicle is enabled. This native is the server side getter of [IS_VEHICLE_NEON_LIGHT_ENABLED](../gta5/VEHICLE-1.md#isvehicleneonlightenabled).

```cpp
enum neonIndex
{
    NEON_BACK = 0,   // Back neon
    NEON_RIGHT = 1,  // Right neon
    NEON_LEFT = 2,   // Left neon
    NEON_FRONT = 3   // Front neon
};
```

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(GetPlayerPed(1), false) -- 1 is the source here
local isRightNeonOn = GetVehicleNeonEnabled(vehicle, 1)
print(isRightNeonOn)
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(GetPlayerPed(1), false); // 1 is the source here
const isRightNeonOn = GetVehicleNeonEnabled(vehicle, 1);
console.log(isRightNeonOn);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(GetPlayerPed(1), false); // 1 is the source here
bool isRightNeonOn = GetVehicleNeonEnabled(vehicle, 1);
Debug.WriteLine($"{isRightNeonOn}");
```

---
### GetVehicleNumberPlateText

`GET_VEHICLE_NUMBER_PLATE_TEXT` · hash `0xE8522D58` · **Servidor**

```lua
local retval = GetVehicleNumberPlateText(vehicle)
```
```c
char* GET_VEHICLE_NUMBER_PLATE_TEXT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `char*`

---
### GetVehicleNumberPlateTextIndex

`GET_VEHICLE_NUMBER_PLATE_TEXT_INDEX` · hash `0x499747B6` · **Servidor**

```lua
local retval = GetVehicleNumberPlateTextIndex(vehicle)
```
```c
int GET_VEHICLE_NUMBER_PLATE_TEXT_INDEX(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehiclePedIsIn

`GET_VEHICLE_PED_IS_IN` · hash `0xAFE92319` · **Servidor**

```lua
local retval = GetVehiclePedIsIn(ped, lastVehicle)
```
```c
Vehicle GET_VEHICLE_PED_IS_IN(Ped ped, BOOL lastVehicle);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `lastVehicle` (`BOOL`): False = CurrentVehicle, True = LastVehicle

**Devuelve:** `Vehicle` — The vehicle id. Returns 0 if the ped is/was not in a vehicle.

**Descripción oficial:**

Gets the vehicle the specified Ped is/was in depending on bool value. This native is used server side when using OneSync.

---
### GetVehiclePetrolTankHealth

`GET_VEHICLE_PETROL_TANK_HEALTH` · hash `0xE41595CE` · **Servidor**

```lua
local retval = GetVehiclePetrolTankHealth(vehicle)
```
```c
float GET_VEHICLE_PETROL_TANK_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleRadioStationIndex

`GET_VEHICLE_RADIO_STATION_INDEX` · hash `0x57037960` · **Servidor**

```lua
local retval = GetVehicleRadioStationIndex(vehicle)
```
```c
int GET_VEHICLE_RADIO_STATION_INDEX(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleRoofLivery

`GET_VEHICLE_ROOF_LIVERY` · hash `0x872CF42` · **Servidor**

```lua
local retval = GetVehicleRoofLivery(vehicle)
```
```c
int GET_VEHICLE_ROOF_LIVERY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleTotalRepairs

`GET_VEHICLE_TOTAL_REPAIRS` · hash `0x9963D5F9` · **Servidor**

```lua
local retval = GetVehicleTotalRepairs(vehicle)
```
```c
int GET_VEHICLE_TOTAL_REPAIRS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int` — Returns the total amount of repairs. Each repair will increase the count to make it possible to detect client repairs.
 The value has a range from 0 to 15. Next value after 15 is 0.

---
### GetVehicleTyreSmokeColor

`GET_VEHICLE_TYRE_SMOKE_COLOR` · hash `0x75280015` · **Servidor**

```lua
local r, g, b = GetVehicleTyreSmokeColor(vehicle)
```
```c
void GET_VEHICLE_TYRE_SMOKE_COLOR(Vehicle vehicle, int* r, int* g, int* b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVehicleWheelType

`GET_VEHICLE_WHEEL_TYPE` · hash `0xDA58D7AE` · **Servidor**

```lua
local retval = GetVehicleWheelType(vehicle)
```
```c
int GET_VEHICLE_WHEEL_TYPE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleWindowTint

`GET_VEHICLE_WINDOW_TINT` · hash `0x13D53892` · **Servidor**

```lua
local retval = GetVehicleWindowTint(vehicle)
```
```c
int GET_VEHICLE_WINDOW_TINT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GiveWeaponComponentToPed

`GIVE_WEAPON_COMPONENT_TO_PED` · hash `0x3E1E286D` · **Servidor**

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

**Descripción oficial:**

GIVE_WEAPON_COMPONENT_TO_PED

**This is the server-side RPC native equivalent of the client native [GIVE_WEAPON_COMPONENT_TO_PED](#giveweaponcomponenttoped).**

---
### GiveWeaponToPed

`GIVE_WEAPON_TO_PED` · hash `0xC4D88A85` · **Servidor**

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

**Descripción oficial:**

GIVE_WEAPON_TO_PED

**This is the server-side RPC native equivalent of the client native [GIVE_WEAPON_TO_PED](#giveweapontoped).**

---
### HasEntityBeenMarkedAsNoLongerNeeded

`HAS_ENTITY_BEEN_MARKED_AS_NO_LONGER_NEEDED` · hash `0x9C9A3BE0` · **Servidor**

```lua
local retval = HasEntityBeenMarkedAsNoLongerNeeded(vehicle)
```
```c
BOOL HAS_ENTITY_BEEN_MARKED_AS_NO_LONGER_NEEDED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### HasVehicleBeenDamagedByBullets

`HAS_VEHICLE_BEEN_DAMAGED_BY_BULLETS` · hash `0xB8AF3137` · **Servidor**

```lua
local retval = HasVehicleBeenDamagedByBullets(vehicle)
```
```c
BOOL HAS_VEHICLE_BEEN_DAMAGED_BY_BULLETS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `BOOL` — Returns whether or not the target vehicle has been damaged by bullets.

---
### HasVehicleBeenOwnedByPlayer

`HAS_VEHICLE_BEEN_OWNED_BY_PLAYER` · hash `0xE4E83A5B` · **Servidor**

```lua
local retval = HasVehicleBeenOwnedByPlayer(vehicle)
```
```c
BOOL HAS_VEHICLE_BEEN_OWNED_BY_PLAYER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsBoatAnchoredAndFrozen

`IS_BOAT_ANCHORED_AND_FROZEN` · hash `0xD5C39EE6` · **Servidor**

```lua
local retval = IsBoatAnchoredAndFrozen(vehicle)
```
```c
bool IS_BOAT_ANCHORED_AND_FROZEN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `bool` — Returns whether or not the boat is anchored and frozen.

---
### IsBoatWrecked

`IS_BOAT_WRECKED` · hash `0x9049DB44` · **Servidor**

```lua
local retval = IsBoatWrecked(vehicle)
```
```c
bool IS_BOAT_WRECKED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `bool` — Returns whether or not the boat is wrecked.

---
### IsEntityVisible

`IS_ENTITY_VISIBLE` · hash `0x120B4ED5` · **Servidor**

```lua
local retval = IsEntityVisible(entity)
```
```c
BOOL IS_ENTITY_VISIBLE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL` — Returns `true` if the entity is visible, `false` otherwise.

**Descripción oficial:**

This native checks if the given entity is visible.

---
### IsFlashLightOn

`IS_FLASH_LIGHT_ON` · hash `0x76876154` · **Servidor**

```lua
local retval = IsFlashLightOn(ped)
```
```c
bool IS_FLASH_LIGHT_ON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `bool` — Whether or not the ped's flash light is on.

---
### IsHeliTailBoomBreakable

`IS_HELI_TAIL_BOOM_BREAKABLE` · hash `0x23E46BD7` · **Servidor**

```lua
local retval = IsHeliTailBoomBreakable(heli)
```
```c
BOOL IS_HELI_TAIL_BOOM_BREAKABLE(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `BOOL` — Returns `true` if the helicopter's tail boom can break, `false` if it cannot.

**Descripción oficial:**

This is a getter for [SET_HELI_TAIL_EXPLODE_THROW_DASHBOARD](../gta5/VEHICLE-1.md#sethelitailboomcanbreakoff)

---
### IsHeliTailBoomBroken

`IS_HELI_TAIL_BOOM_BROKEN` · hash `0x2C59F987` · **Servidor**

```lua
local retval = IsHeliTailBoomBroken(heli)
```
```c
BOOL IS_HELI_TAIL_BOOM_BROKEN(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter to check

**Devuelve:** `BOOL` — Returns `true` if the helicopter's tail boom is broken, `false` if it is intact.

---
### IsPedAPlayer

`IS_PED_A_PLAYER` · hash `0x404794CA` · **Servidor**

```lua
local retval = IsPedAPlayer(ped)
```
```c
BOOL IS_PED_A_PLAYER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns `true` if the ped is a player, `false` otherwise.

**Descripción oficial:**

This native checks if the given ped is a player.

---
### IsPedHandcuffed

`IS_PED_HANDCUFFED` · hash `0x25865633` · **Servidor**

```lua
local retval = IsPedHandcuffed(ped)
```
```c
bool IS_PED_HANDCUFFED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `bool` — Whether or not the ped is handcuffed.

---
### IsPedInAnyVehicle

`IS_PED_IN_ANY_VEHICLE` · hash `0x3B0171EE` · **Servidor**

```lua
local retval = IsPedInAnyVehicle(ped)
```
```c
BOOL IS_PED_IN_ANY_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): the ped id

**Devuelve:** `BOOL` — Returns `true` if the specified `ped` is in any vehicle

---
### IsPedInVehicle

`IS_PED_IN_VEHICLE` · hash `0x7DA6BC83` · **Servidor**

```lua
local retval = IsPedInVehicle(ped, vehicle)
```
```c
BOOL IS_PED_IN_VEHICLE(Ped ped, Vehicle vehicle);
```

**Parámetros**

- `ped` (`Ped`): the ped id
- `vehicle` (`Vehicle`): the vehicle id

**Devuelve:** `BOOL` — Returns `true` if the specified `ped` is in the specified `vehicle`

---
### IsPedRagdoll

`IS_PED_RAGDOLL` · hash `0xC833BBE1` · **Servidor**

```lua
local retval = IsPedRagdoll(ped)
```
```c
bool IS_PED_RAGDOLL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `bool` — Whether or not the ped is ragdolling.

---
### IsPedStrafing

`IS_PED_STRAFING` · hash `0xEFEED13C` · **Servidor**

```lua
local retval = IsPedStrafing(ped)
```
```c
bool IS_PED_STRAFING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `bool` — Whether or not the ped is strafing.

---
### IsPedUsingActionMode

`IS_PED_USING_ACTION_MODE` · hash `0x5AE7EDA2` · **Servidor**

```lua
local retval = IsPedUsingActionMode(ped)
```
```c
bool IS_PED_USING_ACTION_MODE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `bool` — Whether or not the ped is using action mode.

---
### IsPlayerAceAllowed

`IS_PLAYER_ACE_ALLOWED` · hash `0xDEDAE23D` · **Servidor**

```lua
local retval = IsPlayerAceAllowed(playerSrc, object)
```
```c
BOOL IS_PLAYER_ACE_ALLOWED(char* playerSrc, char* object);
```

**Parámetros**

- `playerSrc` (`char*`)
- `object` (`char*`)

**Devuelve:** `BOOL`

---
### IsPlayerCommerceInfoLoaded

`IS_PLAYER_COMMERCE_INFO_LOADED` · hash `0xBEFE93F4` · **Servidor**

```lua
local retval = IsPlayerCommerceInfoLoaded(playerSrc)
```
```c
BOOL IS_PLAYER_COMMERCE_INFO_LOADED(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `BOOL` — A boolean.

**Descripción oficial:**

> This native is deprecated and may be removed in a future version. Use [`IS_PLAYER_COMMERCE_INFO_LOADED_EXT`](#isplayercommerceinfoloadedext) instead.

Requests whether or not the commerce data for the specified player has loaded.

---
### IsPlayerCommerceInfoLoadedExt

`IS_PLAYER_COMMERCE_INFO_LOADED_EXT` · hash `0x1D14F4FE` · **Servidor**

```lua
local retval = IsPlayerCommerceInfoLoadedExt(playerSrc)
```
```c
BOOL IS_PLAYER_COMMERCE_INFO_LOADED_EXT(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `BOOL` — A boolean.

**Descripción oficial:**

Requests whether or not the commerce data for the specified player has loaded from Tebex.

---
### IsPlayerEvadingWantedLevel

`IS_PLAYER_EVADING_WANTED_LEVEL` · hash `0x89A3881A` · **Servidor**

```lua
local retval = IsPlayerEvadingWantedLevel(playerSrc)
```
```c
BOOL IS_PLAYER_EVADING_WANTED_LEVEL(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The target player

**Devuelve:** `BOOL` — boolean value, depending if the player is evading his wanted level or not.

**Descripción oficial:**

```
This will return true if the player is evading wanted level, meaning that the wanted level stars are blink.
Otherwise will return false.

If the player is not wanted, it simply returns false.
```

---
### IsPlayerInFreeCamMode

`IS_PLAYER_IN_FREE_CAM_MODE` · hash `0x1F14F2AC` · **Servidor**

```lua
local retval = IsPlayerInFreeCamMode(playerSrc)
```
```c
bool IS_PLAYER_IN_FREE_CAM_MODE(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player to get the free camera mode status of

**Devuelve:** `bool` — Returns if the player is in free camera mode.

---
### IsPlayerUsingSuperJump

`IS_PLAYER_USING_SUPER_JUMP` · hash `0xC7D2C20C` · **Servidor**

```lua
local retval = IsPlayerUsingSuperJump(playerSrc)
```
```c
BOOL IS_PLAYER_USING_SUPER_JUMP(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `BOOL` — A boolean.

---
### IsTrainCaboose

`IS_TRAIN_CABOOSE` · hash `0xFA9336E5` · **Servidor**

```lua
local retval = IsTrainCaboose(train)
```
```c
bool IS_TRAIN_CABOOSE(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `bool` — Returns true if the train is the caboose of the chain.

---
### IsVehicleExtraTurnedOn

`IS_VEHICLE_EXTRA_TURNED_ON` · hash `0x42098B5` · **Servidor**

```lua
local retval = IsVehicleExtraTurnedOn(vehicle, extraId)
```
```c
BOOL IS_VEHICLE_EXTRA_TURNED_ON(Vehicle vehicle, int extraId);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `extraId` (`int`)

**Devuelve:** `BOOL`

---
### IsVehicleSirenOn

`IS_VEHICLE_SIREN_ON` · hash `0x25EB5873` · **Servidor**

```lua
local retval = IsVehicleSirenOn(vehicle)
```
```c
BOOL IS_VEHICLE_SIREN_ON(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleTyreBurst

`IS_VEHICLE_TYRE_BURST` · hash `0x48C80210` · **Servidor**

```lua
local retval = IsVehicleTyreBurst(vehicle, wheelID, completely)
```
```c
BOOL IS_VEHICLE_TYRE_BURST(Vehicle vehicle, int wheelID, BOOL completely);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelID` (`int`)
- `completely` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsVehicleWindowIntact

`IS_VEHICLE_WINDOW_INTACT` · hash `0xAC4EF23D` · **Servidor**

```lua
local retval = IsVehicleWindowIntact(vehicle, windowIndex)
```
```c
BOOL IS_VEHICLE_WINDOW_INTACT(Vehicle vehicle, int windowIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `windowIndex` (`int`): The window index.

**Devuelve:** `BOOL`

**Descripción oficial:**

See the client-side [IS_VEHICLE_WINDOW_INTACT](#isvehiclewindowintact) for a window indexes list.

---
### LoadPlayerCommerceData

`LOAD_PLAYER_COMMERCE_DATA` · hash `0xA8F63EAB` · **Servidor**

```lua
LoadPlayerCommerceData(playerSrc)
```
```c
void LOAD_PLAYER_COMMERCE_DATA(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `void`

**Descripción oficial:**

> This native is deprecated and may be removed in a future version. Use [`LOAD_PLAYER_COMMERCE_DATA_EXT`](#loadplayercommercedataext) instead.

Requests the commerce data for the specified player, including the owned SKUs. Use `IS_PLAYER_COMMERCE_INFO_LOADED` to check if it has loaded.

---
### LoadPlayerCommerceDataExt

`LOAD_PLAYER_COMMERCE_DATA_EXT` · hash `0x7995539E` · **Servidor**

```lua
LoadPlayerCommerceDataExt(playerSrc)
```
```c
void LOAD_PLAYER_COMMERCE_DATA_EXT(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `void`

**Descripción oficial:**

Requests the commerce data from Tebex for the specified player, including the owned SKUs.

Use [`IS_PLAYER_COMMERCE_INFO_LOADED_EXT`](#isplayercommerceinfoloadedext) to check if it has loaded.

This will not automatically update whenever a client purchases a package, if you want to fetch new purchases you will need to call this native again.

This native will temporarily cache the players commerce data for 10 seconds, a call to this native after 10 seconds will re-fetch the players commerce data.

**Ejemplo (lua):**

```lua
RegisterNetEvent("doesOwnPackage", function(packageIdSku)
	-- source isn't valid across waits, so we localize it
	local source = source

	-- input isn't right
	if type(packageIdSku) ~= "number" then
		return
	end

	-- The native will cache the results
	LoadPlayerCommerceDataExt(source)
	-- Wait for the players data to load
	while not IsPlayerCommerceInfoLoadedExt(source) do
		Wait(0)
	end

	-- Tell the client if they own the package or not
	TriggerClientEvent("doesOwnPackage", source, DoesPlayerOwnSkuExt(source, packageIdSku))
end)
```

---
### MumbleCreateChannel

`MUMBLE_CREATE_CHANNEL` · hash `0x262663C5` · **Servidor**

```lua
MumbleCreateChannel(id)
```
```c
void MUMBLE_CREATE_CHANNEL(int id);
```

**Parámetros**

- `id` (`int`): ID of the channel.

**Devuelve:** `void`

**Descripción oficial:**

Create a permanent voice channel.

---
### MumbleIsPlayerMuted

`MUMBLE_IS_PLAYER_MUTED` · hash `0x1D5D50C2` · **Servidor**

```lua
local retval = MumbleIsPlayerMuted(playerSrc)
```
```c
BOOL MUMBLE_IS_PLAYER_MUTED(int playerSrc);
```

**Parámetros**

- `playerSrc` (`int`): The player to get the mute state for

**Devuelve:** `BOOL` — Whether or not the player is muted

**Descripción oficial:**

Checks if the player is currently muted

---
### MumbleSetPlayerMuted

`MUMBLE_SET_PLAYER_MUTED` · hash `0xCC6C2EB1` · **Servidor**

```lua
MumbleSetPlayerMuted(playerSrc, toggle)
```
```c
void MUMBLE_SET_PLAYER_MUTED(int playerSrc, bool toggle);
```

**Parámetros**

- `playerSrc` (`int`): The player to set the mute state of
- `toggle` (`bool`): Whether to mute or unmute the player

**Devuelve:** `void`

**Descripción oficial:**

Mutes or unmutes the specified player

---
### NetworkGetEntityFromNetworkId

`NETWORK_GET_ENTITY_FROM_NETWORK_ID` · hash `0x5B912C3F` · **Servidor**

```lua
local retval = NetworkGetEntityFromNetworkId(netId)
```
```c
Entity NETWORK_GET_ENTITY_FROM_NETWORK_ID(int netId);
```

**Parámetros**

- `netId` (`int`)

**Devuelve:** `Entity`

---
### NetworkGetFirstEntityOwner

`NETWORK_GET_FIRST_ENTITY_OWNER` · hash `0x1E546224` · **Servidor**

```lua
local retval = NetworkGetFirstEntityOwner(entity)
```
```c
int NETWORK_GET_FIRST_ENTITY_OWNER(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the first owner for.

**Devuelve:** `int` — The server ID of the first entity owner.

**Descripción oficial:**

Returns the first owner ID of the specified entity.

---
### NetworkGetNetworkIdFromEntity

`NETWORK_GET_NETWORK_ID_FROM_ENTITY` · hash `0x9E35DAB6` · **Servidor**

```lua
local retval = NetworkGetNetworkIdFromEntity(entity)
```
```c
int NETWORK_GET_NETWORK_ID_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `int`

---
### NetworkGetVoiceProximityOverrideForPlayer

`NETWORK_GET_VOICE_PROXIMITY_OVERRIDE_FOR_PLAYER` · hash `0xFFEEF513` · **Servidor**

```lua
local retval = NetworkGetVoiceProximityOverrideForPlayer(playerSrc)
```
```c
Vector3 NETWORK_GET_VOICE_PROXIMITY_OVERRIDE_FOR_PLAYER(char* playerSrc);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle

**Devuelve:** `Vector3`

---
### PerformHttpRequestInternal

`PERFORM_HTTP_REQUEST_INTERNAL` · hash `0x8E8CC653` · **Servidor**

```lua
local retval = PerformHttpRequestInternal(requestData, requestDataLength)
```
```c
int PERFORM_HTTP_REQUEST_INTERNAL(char* requestData, int requestDataLength);
```

**Parámetros**

- `requestData` (`char*`)
- `requestDataLength` (`int`)

**Devuelve:** `int`

---
### PerformHttpRequestInternalEx

`PERFORM_HTTP_REQUEST_INTERNAL_EX` · hash `0x6B171E87` · **Servidor**

```lua
local retval = PerformHttpRequestInternalEx(requestData)
```
```c
int PERFORM_HTTP_REQUEST_INTERNAL_EX(object requestData);
```

**Parámetros**

- `requestData` (`object`)

**Devuelve:** `int`

---
### PrintStructuredTrace

`PRINT_STRUCTURED_TRACE` · hash `0x90892DED` · **Servidor**

```lua
PrintStructuredTrace(jsonString)
```
```c
void PRINT_STRUCTURED_TRACE(char* jsonString);
```

**Parámetros**

- `jsonString` (`char*`): JSON data to submit as `payload` in the `script_structured_trace` event.

**Devuelve:** `void`

**Descripción oficial:**

Prints 'structured trace' data to the server `file descriptor 3` channel. This is not generally useful outside of
server monitoring utilities.

---
### RecorderStartRecording

`RECORDER_START_RECORDING` · hash `0xA966E104` · **Servidor**

```lua
RecorderStartRecording(netId, compressed, fileName)
```
```c
void RECORDER_START_RECORDING(int netId, BOOL compressed, char* fileName);
```

**Parámetros**

- `netId` (`int`): The network ID of the entity to record.
- `compressed` (`BOOL`): Whether to enable compression of the recording.
- `fileName` (`char*`): The name of the file to write the recording to.

**Devuelve:** `void`

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Starts recording the network sync of the entity with the given network ID to a file.

---
### RecorderStartReplay

`RECORDER_START_REPLAY` · hash `0xACD27A01` · **Servidor**

```lua
local retval = RecorderStartReplay(fileName, mode)
```
```c
int RECORDER_START_REPLAY(char* fileName, int mode);
```

**Parámetros**

- `fileName` (`char*`): The name of the recorded file to replay.
- `mode` (`int`): The playback mode. See the description for supported values.

**Devuelve:** `int` — A replay ID that can be passed to `RECORDER_STOP_REPLAY`.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Starts replaying a previously recorded file. The `mode` argument controls playback behavior:

* `0`: Once. Play the recording a single time.
* `1`: Loop. Repeat the recording continuously.
* `2`: Perfect loop. Repeat the recording seamlessly.

---
### RecorderStopRecording

`RECORDER_STOP_RECORDING` · hash `0xA124422F` · **Servidor**

```lua
RecorderStopRecording(netId)
```
```c
void RECORDER_STOP_RECORDING(int netId);
```

**Parámetros**

- `netId` (`int`): The network ID of the entity whose recording should be stopped.

**Devuelve:** `void`

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Stops the recording in progress for the entity with the given network ID.

---
### RecorderStopReplay

`RECORDER_STOP_REPLAY` · hash `0x31A548AC` · **Servidor**

```lua
RecorderStopReplay(replayId)
```
```c
void RECORDER_STOP_REPLAY(int replayId);
```

**Parámetros**

- `replayId` (`int`): The replay ID as returned by `RECORDER_START_REPLAY`.

**Devuelve:** `void`

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Stops the replay with the given replay ID.

---
### RegisterConsoleListener

`REGISTER_CONSOLE_LISTENER` · hash `0x281B5448` · **Servidor**

```lua
RegisterConsoleListener(listener)
```
```c
void REGISTER_CONSOLE_LISTENER(func listener);
```

**Parámetros**

- `listener` (`func`): A function of `(channel: string, message: string) => void`. The message might contain `\n`.

**Devuelve:** `void`

**Descripción oficial:**

Registers a listener for console output messages.

---
### RegisterResourceAsset

`REGISTER_RESOURCE_ASSET` · hash `0x9862B266` · **Servidor**

```lua
local retval = RegisterResourceAsset(resourceName, fileName)
```
```c
char* REGISTER_RESOURCE_ASSET(char* resourceName, char* fileName);
```

**Parámetros**

- `resourceName` (`char*`): The resource to add the asset to.
- `fileName` (`char*`): A file name in the resource.

**Devuelve:** `char*` — A cache string to pass to `REGISTER_STREAMING_FILE_FROM_CACHE` on the client.

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Registers a cached resource asset with the resource system, similar to the automatic scanning of the `stream/` folder.

---
### RegisterResourceBuildTaskFactory

`REGISTER_RESOURCE_BUILD_TASK_FACTORY` · hash `0x285B43CA` · **Servidor**

```lua
RegisterResourceBuildTaskFactory(factoryId, factoryFn)
```
```c
void REGISTER_RESOURCE_BUILD_TASK_FACTORY(char* factoryId, func factoryFn);
```

**Parámetros**

- `factoryId` (`char*`): The identifier for the build task.
- `factoryFn` (`func`): The factory function.

**Devuelve:** `void`

**Descripción oficial:**

Registers a build task factory for resources.
The function should return an object (msgpack map) with the following fields:

```
{
// returns whether the specific resource should be built
shouldBuild = func(resourceName: string): bool,

// asynchronously start building the specific resource.
// call cb when completed
build = func(resourceName: string, cb: func(success: bool, status: string): void): void
}
```

---
### RemoveAllPedWeapons

`REMOVE_ALL_PED_WEAPONS` · hash `0xA44CE817` · **Servidor**

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

**This is the server-side RPC native equivalent of the client native [REMOVE_ALL_PED_WEAPONS](#removeallpedweapons).**

---
### RemoveBlip

`REMOVE_BLIP` · hash `0xD8C3C1CD` · **Servidor**

```lua
local blip = RemoveBlip(blip)
```
```c
void REMOVE_BLIP(Blip* blip);
```

**Parámetros**

- `blip` (`Blip*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: Blip handle to remove.

**Devuelve:** `void`

**Descripción oficial:**

Removes the blip from your map.
**Note:** This function only works on the script that created the blip, if you wish to remove blips created by other scripts, see [`SET_THIS_SCRIPT_CAN_REMOVE_BLIPS_CREATED_BY_ANY_SCRIPT`](../gta5/MISC.md#setthisscriptcanremoveblipscreatedbyanyscript).

**This is the server-side RPC native equivalent of the client native [REMOVE_BLIP](#removeblip).**

---
### RemoveWeaponComponentFromPed

`REMOVE_WEAPON_COMPONENT_FROM_PED` · hash `0x412AA00D` · **Servidor**

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

**Descripción oficial:**

REMOVE_WEAPON_COMPONENT_FROM_PED

**This is the server-side RPC native equivalent of the client native [REMOVE_WEAPON_COMPONENT_FROM_PED](#removeweaponcomponentfromped).**

---
### RemoveWeaponFromPed

`REMOVE_WEAPON_FROM_PED` · hash `0x9C37F220` · **Servidor**

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

**This is the server-side RPC native equivalent of the client native [REMOVE_WEAPON_FROM_PED](#removeweaponfromped).**

---
### RequestPlayerCommerceSession

`REQUEST_PLAYER_COMMERCE_SESSION` · hash `0x96F93CCE` · **Servidor**

```lua
RequestPlayerCommerceSession(playerSrc, skuId)
```
```c
void REQUEST_PLAYER_COMMERCE_SESSION(char* playerSrc, int skuId);
```

**Parámetros**

- `playerSrc` (`char*`): The player handle
- `skuId` (`int`): The ID of the SKU.

**Devuelve:** `void`

**Descripción oficial:**

> This native is deprecated and may be removed in a future version. Use the [Tebex API](https://docs.tebex.io/) instead.

Requests the specified player to buy the passed SKU. This'll pop up a prompt on the client, which upon acceptance
will open the browser prompting further purchase details.

---
### SaveResourceFile

`SAVE_RESOURCE_FILE` · hash `0xA09E7E7B` · **Servidor**

```lua
local retval = SaveResourceFile(resourceName, fileName, data, dataLength)
```
```c
BOOL SAVE_RESOURCE_FILE(char* resourceName, char* fileName, char* data, int dataLength);
```

**Parámetros**

- `resourceName` (`char*`): The name of the resource.
- `fileName` (`char*`): The name of the file.
- `data` (`char*`): The data to write to the file.
- `dataLength` (`int`): The length of the written data.

**Devuelve:** `BOOL` — A value indicating if the write succeeded.

**Descripción oficial:**

Writes the specified data to a file in the specified resource.
Using a length of `-1` will automatically detect the length assuming the data is a C string.

---
### ScanResourceRoot

`SCAN_RESOURCE_ROOT` · hash `0x636F097F` · **Servidor**

```lua
ScanResourceRoot(rootPath, callback)
```
```c
void SCAN_RESOURCE_ROOT(char* rootPath, func callback);
```

**Parámetros**

- `rootPath` (`char*`): The resource directory to scan.
- `callback` (`func`): A callback that will receive an object with results.

**Devuelve:** `void`

**Descripción oficial:**

Scans the resources in the specified resource root. This function is only available in the 'monitor mode' process and is
not available for user resources.

---
### ScheduleResourceTick

`SCHEDULE_RESOURCE_TICK` · hash `0xB88A73AD` · **Servidor**

```lua
ScheduleResourceTick(resourceName)
```
```c
void SCHEDULE_RESOURCE_TICK(char* resourceName);
```

**Parámetros**

- `resourceName` (`char*`): The resource to tick.

**Devuelve:** `void`

**Descripción oficial:**

Schedules the specified resource to run a tick as soon as possible, bypassing the server's fixed tick rate.

---
### SetBlipSprite

`SET_BLIP_SPRITE` · hash `0x8DBBB0B9` · **Servidor**

```lua
SetBlipSprite(blip, spriteId)
```
```c
void SET_BLIP_SPRITE(Blip blip, int spriteId);
```

**Parámetros**

- `blip` (`Blip`): The blip to change.
- `spriteId` (`int`): The sprite ID to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets the displayed sprite for a specific blip.
There's a [list of sprites](https://docs.fivem.net/docs/game-references/blips/) on the FiveM documentation site.

**This is the server-side RPC native equivalent of the client native [SET_BLIP_SPRITE](#setblipsprite).**

---
### SetColshapeDimension

`SET_COLSHAPE_DIMENSION` · hash `0x38482191` · **Servidor**

```lua
SetColshapeDimension(colShapeId, dimension)
```
```c
void SET_COLSHAPE_DIMENSION(int colShapeId, int dimension);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `dimension` (`int`): The dimension (routing bucket) to assign.

**Devuelve:** `void`

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Sets the dimension (routing bucket) of the collision shape. Only entities in the same dimension will trigger enter/exit events.

**Ejemplo (lua):**

```lua
-- Server-side: create a sphere colshape in a specific dimension
local colShape = CreateColshapeSphere(100.0, 200.0, 30.0, 25.0)
SetColshapeDimension(colShape, 5)

AddEventHandler('onColshapeEnter', function(entity, shape)
    if shape == colShape then
        print('entity entered the sphere zone in dimension 5')
    end
end)
```

---
### SetConvar

`SET_CONVAR` · hash `0x341B16D2` · **Servidor**

```lua
SetConvar(varName, value)
```
```c
void SET_CONVAR(char* varName, char* value);
```

**Parámetros**

- `varName` (`char*`)
- `value` (`char*`)

**Devuelve:** `void`

---
### SetConvarReplicated

`SET_CONVAR_REPLICATED` · hash `0xF292858C` · **Servidor**

```lua
SetConvarReplicated(varName, value)
```
```c
void SET_CONVAR_REPLICATED(char* varName, char* value);
```

**Parámetros**

- `varName` (`char*`): The console variable name.
- `value` (`char*`): The value to set for the given console variable.

**Devuelve:** `void`

**Descripción oficial:**

Used to replicate a server variable onto clients.

**Ejemplo (lua):**

```lua
SetConvarReplicated('voice_useNativeAudio', 'true')
```

---
### SetConvarServerInfo

`SET_CONVAR_SERVER_INFO` · hash `0x9338D547` · **Servidor**

```lua
SetConvarServerInfo(varName, value)
```
```c
void SET_CONVAR_SERVER_INFO(char* varName, char* value);
```

**Parámetros**

- `varName` (`char*`)
- `value` (`char*`)

**Devuelve:** `void`

---
### SetCurrentPedWeapon

`SET_CURRENT_PED_WEAPON` · hash `0xB8278882` · **Servidor**

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

**Descripción oficial:**

SET_CURRENT_PED_WEAPON

**This is the server-side RPC native equivalent of the client native [SET_CURRENT_PED_WEAPON](#setcurrentpedweapon).**

---
### SetEntityCoords

`SET_ENTITY_COORDS` · hash `0xDF70B41B` · **Servidor**

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

**This is the server-side RPC native equivalent of the client native [SET_ENTITY_COORDS](#setentitycoords).**

---
### SetEntityDistanceCullingRadius

`SET_ENTITY_DISTANCE_CULLING_RADIUS` · hash `0xD3A183A3` · **Servidor**

```lua
SetEntityDistanceCullingRadius(entity, radius)
```
```c
void SET_ENTITY_DISTANCE_CULLING_RADIUS(Entity entity, float radius);
```

**Parámetros**

- `entity` (`Entity`): The entity handle to override the distance culling radius.
- `radius` (`float`): The new distance culling radius.

**Devuelve:** `void`

**Descripción oficial:**

It overrides the default distance culling radius of an entity. Set to `0.0` to reset.
If you want to interact with an entity outside of your players' scopes set the radius to a huge number.

**WARNING**: Culling natives are deprecated and have known, [unfixable issues](https://forum.cfx.re/t/issue-with-culling-radius-and-server-side-entities/4900677/4)

---
### SetEntityHeading

`SET_ENTITY_HEADING` · hash `0xE0FF064D` · **Servidor**

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

**This is the server-side RPC native equivalent of the client native [SET_ENTITY_HEADING](#setentityheading).**

---
### SetEntityIgnoreRequestControlFilter

`SET_ENTITY_IGNORE_REQUEST_CONTROL_FILTER` · hash `0x9F7F8D36` · **Servidor**

```lua
SetEntityIgnoreRequestControlFilter(entity, ignore)
```
```c
void SET_ENTITY_IGNORE_REQUEST_CONTROL_FILTER(Entity entity, bool ignore);
```

**Parámetros**

- `entity` (`Entity`): The entity handle to ignore the request control filter.
- `ignore` (`bool`): Define if the entity ignores the request control filter policy.

**Devuelve:** `void`

**Descripción oficial:**

It allows to flag an entity to ignore the request control filter policy.

---
### SetEntityOrphanMode

`SET_ENTITY_ORPHAN_MODE` · hash `0x489E9162` · **Servidor**

```lua
SetEntityOrphanMode(entity, orphanMode)
```
```c
void SET_ENTITY_ORPHAN_MODE(Entity entity, int orphanMode);
```

**Parámetros**

- `entity` (`Entity`): The entity to set the orphan mode of
- `orphanMode` (`int`): The mode that the server should use for determining if an entity should be removed.

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum EntityOrphanMode {
    // Default, this will delete the entity when it isn't relevant to any players
    // NOTE: this *doesn't* mean when they're no longer in scope
    DeleteWhenNotRelevant = 0,
    // The entity will be deleted whenever its original owner disconnects
    // NOTE: if this is set when the entities original owner has already left it will be
    // marked for deletion (similar to just calling DELETE_ENTITY)
    DeleteOnOwnerDisconnect = 1,
    // The entity will never be deleted by the server when it does relevancy checks
    // you should only use this on entities that need to be relatively persistent
    KeepEntity = 2
}
```

Sets what the server will do when the entity no longer has its original owner. By default the server will cleanup entities that it considers "no longer relevant".

When used on trains, this native will recursively call onto all attached carriages.

**NOTE**: When used with `KeepEntity` (2) this native only guarantees that the ***server*** will not delete the entity, client requests to delete the entity will still work perfectly fine.

---
### SetEntityRemoteSyncedScenesAllowed

`SET_ENTITY_REMOTE_SYNCED_SCENES_ALLOWED` · hash `0xD3FC9D88` · **Servidor**

```lua
SetEntityRemoteSyncedScenesAllowed(entity, allow)
```
```c
void SET_ENTITY_REMOTE_SYNCED_SCENES_ALLOWED(Entity entity, bool allow);
```

**Parámetros**

- `entity` (`Entity`): The entity to set the flag for.
- `allow` (`bool`): Whether to allow remote synced scenes for the entity.

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables the owner check for the specified entity in network-synchronized scenes. When set to `false`, the entity cannot participate in synced scenes initiated by clients that do not own the entity.

By default, this is `false` for all entities, meaning only the entity's owner can include it in networked synchronized scenes.

---
### SetEntityRotation

`SET_ENTITY_ROTATION` · hash `0xA345EFE` · **Servidor**

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
- `rotationOrder` (`int`): Specifies the order in which yaw, pitch, and roll are applied, see [`GET_ENTITY_ROTATION`](#getentityrotation) for the available rotation orders.
- `bDeadCheck` (`BOOL`): Usually set to `true`. Determines whether to check if the entity is dead before applying the rotation.

**Devuelve:** `void`

**Descripción oficial:**

Sets the rotation of a specified entity in the game world.

```
NativeDB Introduced: v323
```

**This is the server-side RPC native equivalent of the client native [SET_ENTITY_ROTATION](#setentityrotation).**

---
### SetEntityRoutingBucket

`SET_ENTITY_ROUTING_BUCKET` · hash `0x635E5289` · **Servidor**

```lua
SetEntityRoutingBucket(entity, bucket)
```
```c
void SET_ENTITY_ROUTING_BUCKET(Entity entity, int bucket);
```

**Parámetros**

- `entity` (`Entity`): The entity to set the routing bucket for.
- `bucket` (`int`): The bucket ID.

**Devuelve:** `void`

**Descripción oficial:**

Sets the routing bucket for the specified entity.

Routing buckets are also known as 'dimensions' or 'virtual worlds' in past echoes, however they are population-aware.

---
### SetEntityVelocity

`SET_ENTITY_VELOCITY` · hash `0xFF5A1988` · **Servidor**

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

**This is the server-side RPC native equivalent of the client native [SET_ENTITY_VELOCITY](#setentityvelocity).**

---
### SetGameType

`SET_GAME_TYPE` · hash `0xF90B7469` · **Servidor**

```lua
SetGameType(gametypeName)
```
```c
void SET_GAME_TYPE(char* gametypeName);
```

**Parámetros**

- `gametypeName` (`char*`)

**Devuelve:** `void`

---
### SetHttpHandler

`SET_HTTP_HANDLER` · hash `0xF5C6330C` · **Servidor**

```lua
SetHttpHandler(handler)
```
```c
void SET_HTTP_HANDLER(func handler);
```

**Parámetros**

- `handler` (`func`): The handler function.

**Devuelve:** `void`

**Descripción oficial:**

Sets the handler for HTTP requests made to the executing resource.

Example request URL: `http://localhost:30120/http-test/ping` - this request will be sent to the `http-test` resource with the `/ping` path.

The handler function assumes the following signature:

```ts
function HttpHandler(
  request: {
    address: string;
    headers: Record<string, string>;
    method: string;
    path: string;
    setDataHandler(handler: (data: string) => void): void;
    setDataHandler(handler: (data: ArrayBuffer) => void, binary: 'binary'): void;
    setCancelHandler(handler: () => void): void;
  },
  response: {
    writeHead(code: number, headers?: Record<string, string | string[]>): void;
    write(data: string): void;
    send(data?: string): void;
  }
): void;
```

*   **request**: The request object.
    *   **address**: The IP address of the request sender.
    *   **path**: The path to where the request was sent.
    *   **headers**: The headers sent with the request.
    *   **method**: The request method.
    *   **setDataHandler**: Sets the handler for when a data body is passed with the request. Additionally you can pass the `'binary'` argument to receive a `BufferArray` in JavaScript or `System.Byte[]` in C# (has no effect in Lua).
    *   **setCancelHandler**: Sets the handler for when the request is cancelled.
*   **response**: An object to control the response.
    *   **writeHead**: Sets the status code & headers of the response. Can be only called once and won't work if called after running other response functions.
    *   **write**: Writes to the response body without sending it. Can be called multiple times.
    *   **send**: Writes to the response body and then sends it along with the status code & headers, finishing the request.

**Ejemplo (lua):**

```lua
SetHttpHandler(function(request, response)
  if request.method == 'GET' and request.path == '/ping' then -- if a GET request was sent to the `/ping` path
      response.writeHead(200, { ['Content-Type'] = 'text/plain' }) -- set the response status code to `200 OK` and the body content type to plain text
      response.send('pong') -- respond to the request with `pong`
  else -- otherwise
      response.writeHead(404) -- set the response status code to `404 Not Found`
      response.send() -- respond to the request with no data
  end
end)
```

---
### SetMapName

`SET_MAP_NAME` · hash `0xB7BA82DC` · **Servidor**

```lua
SetMapName(mapName)
```
```c
void SET_MAP_NAME(char* mapName);
```

**Parámetros**

- `mapName` (`char*`)

**Devuelve:** `void`

---
### SetPedAmmo

`SET_PED_AMMO` · hash `0xBF90DF1A` · **Servidor**

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

**This is the server-side RPC native equivalent of the client native [SET_PED_AMMO](#setpedammo).**

---
### SetPedArmour

`SET_PED_ARMOUR` · hash `0x4E3A0CC4` · **Servidor**

```lua
SetPedArmour(ped, amount)
```
```c
void SET_PED_ARMOUR(Ped ped, int amount);
```

**Parámetros**

- `ped` (`Ped`)
- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the armor of the specified ped.
ped: The Ped to set the armor of.
amount: A value between 0 and 100 indicating the value to set the Ped's armor to.
```

**This is the server-side RPC native equivalent of the client native [SET_PED_ARMOUR](#setpedarmour).**

---
### SetPedCanRagdoll

`SET_PED_CAN_RAGDOLL` · hash `0xCF1384C4` · **Servidor**

```lua
SetPedCanRagdoll(ped, toggle)
```
```c
void SET_PED_CAN_RAGDOLL(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

SET_PED_CAN_RAGDOLL

**This is the server-side RPC native equivalent of the client native [SET_PED_CAN_RAGDOLL](#setpedcanragdoll).**

---
### SetPedComponentVariation

`SET_PED_COMPONENT_VARIATION` · hash `0xD4F7B05C` · **Servidor**

```lua
SetPedComponentVariation(ped, componentId, drawableId, textureId, paletteId)
```
```c
void SET_PED_COMPONENT_VARIATION(Ped ped, int componentId, int drawableId, int textureId, int paletteId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component that you want to set.
- `drawableId` (`int`): The drawable id that is going to be set. Refer to [GET_NUMBER_OF_PED_DRAWABLE_VARIATIONS](../gta5/PED-1.md#getnumberofpeddrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_TEXTURE_VARIATIONS](../gta5/PED-1.md#getnumberofpedtexturevariations).
- `paletteId` (`int`): 0 to 3.

**Devuelve:** `void`

**Descripción oficial:**

This native is used to set component variation on a ped. Components, drawables and textures IDs are related to the ped model.

**MP Freemode list of components**

**0**: Face
**1**: Mask
**2**: Hair
**3**: Torso
**4**: Leg
**5**: Parachute / bag
**6**: Shoes
**7**: Accessory
**8**: Undershirt
**9**: Kevlar
**10**: Badge
**11**: Torso 2
List of Component IDs

```cpp
// Components
enum ePedVarComp
{
PV_COMP_INVALID = 0xFFFFFFFF,
PV_COMP_HEAD = 0, // "HEAD"
PV_COMP_BERD = 1, // "BEARD"
PV_COMP_HAIR = 2, // "HAIR"
PV_COMP_UPPR = 3, // "UPPER"
PV_COMP_LOWR = 4, // "LOWER"
PV_COMP_HAND = 5, // "HAND"
PV_COMP_FEET = 6, // "FEET"
PV_COMP_TEEF = 7, // "TEETH"
PV_COMP_ACCS = 8, // "ACCESSORIES"
PV_COMP_TASK = 9, // "TASK"
PV_COMP_DECL = 10, // "DECL"
PV_COMP_JBIB = 11, // "JBIB"
PV_COMP_MAX = 12,
};
```

**This is the server-side RPC native equivalent of the client native [SET_PED_COMPONENT_VARIATION](#setpedcomponentvariation).**

---
### SetPedConfigFlag

`SET_PED_CONFIG_FLAG` · hash `0x9CFBE10D` · **Servidor**

```lua
SetPedConfigFlag(ped, flagId, value)
```
```c
void SET_PED_CONFIG_FLAG(Ped ped, int flagId, BOOL value);
```

**Parámetros**

- `ped` (`Ped`)
- `flagId` (`int`)
- `value` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
// Potential names and hash collisions included as comments
enum ePedConfigFlags {
CPED_CONFIG_FLAG_CreatedByFactory = 0,
CPED_CONFIG_FLAG_CanBeShotInVehicle = 1,
CPED_CONFIG_FLAG_NoCriticalHits = 2,
CPED_CONFIG_FLAG_DrownsInWater = 3,
CPED_CONFIG_FLAG_DrownsInSinkingVehicle = 4,
CPED_CONFIG_FLAG_DiesInstantlyWhenSwimming = 5,
CPED_CONFIG_FLAG_HasBulletProofVest = 6,
CPED_CONFIG_FLAG_UpperBodyDamageAnimsOnly = 7,
CPED_CONFIG_FLAG_NeverFallOffSkis = 8,
CPED_CONFIG_FLAG_NeverEverTargetThisPed = 9,
CPED_CONFIG_FLAG_ThisPedIsATargetPriority = 10,
CPED_CONFIG_FLAG_TargettableWithNoLos = 11,
CPED_CONFIG_FLAG_DoesntListenToPlayerGroupCommands = 12,
CPED_CONFIG_FLAG_NeverLeavesGroup = 13,
CPED_CONFIG_FLAG_DoesntDropWeaponsWhenDead = 14,
CPED_CONFIG_FLAG_SetDelayedWeaponAsCurrent = 15,
CPED_CONFIG_FLAG_KeepTasksAfterCleanUp = 16,
CPED_CONFIG_FLAG_BlockNonTemporaryEvents = 17,
CPED_CONFIG_FLAG_HasAScriptBrain = 18,
CPED_CONFIG_FLAG_WaitingForScriptBrainToLoad = 19,
CPED_CONFIG_FLAG_AllowMedicsToReviveMe = 20,
CPED_CONFIG_FLAG_MoneyHasBeenGivenByScript = 21,
CPED_CONFIG_FLAG_NotAllowedToCrouch = 22,
CPED_CONFIG_FLAG_DeathPickupsPersist = 23,
CPED_CONFIG_FLAG_IgnoreSeenMelee = 24,
CPED_CONFIG_FLAG_ForceDieIfInjured = 25,
CPED_CONFIG_FLAG_DontDragMeOutCar = 26,
CPED_CONFIG_FLAG_StayInCarOnJack = 27,
CPED_CONFIG_FLAG_ForceDieInCar = 28,
CPED_CONFIG_FLAG_GetOutUndriveableVehicle = 29,
CPED_CONFIG_FLAG_WillRemainOnBoatAfterMissionEnds = 30,
CPED_CONFIG_FLAG_DontStoreAsPersistent = 31,
CPED_CONFIG_FLAG_WillFlyThroughWindscreen = 32,
CPED_CONFIG_FLAG_DieWhenRagdoll = 33,
CPED_CONFIG_FLAG_HasHelmet = 34,
CPED_CONFIG_FLAG_UseHelmet = 35,
CPED_CONFIG_FLAG_DontTakeOffHelmet = 36,
CPED_CONFIG_FLAG_HideInCutscene = 37,
CPED_CONFIG_FLAG_PedIsEnemyToPlayer = 38,
CPED_CONFIG_FLAG_DisableEvasiveDives = 39,
CPED_CONFIG_FLAG_PedGeneratesDeadBodyEvents = 40,
CPED_CONFIG_FLAG_DontAttackPlayerWithoutWantedLevel = 41,
CPED_CONFIG_FLAG_DontInfluenceWantedLevel = 42,
CPED_CONFIG_FLAG_DisablePlayerLockon = 43,
CPED_CONFIG_FLAG_DisableLockonToRandomPeds = 44,
CPED_CONFIG_FLAG_AllowLockonToFriendlyPlayers = 45,
_0xDB115BFA = 46,
CPED_CONFIG_FLAG_PedBeingDeleted = 47,
CPED_CONFIG_FLAG_BlockWeaponSwitching = 48,
CPED_CONFIG_FLAG_BlockGroupPedAimedAtResponse = 49,
CPED_CONFIG_FLAG_WillFollowLeaderAnyMeans = 50,
CPED_CONFIG_FLAG_BlippedByScript = 51,
CPED_CONFIG_FLAG_DrawRadarVisualField = 52,
CPED_CONFIG_FLAG_StopWeaponFiringOnImpact = 53,
CPED_CONFIG_FLAG_DissableAutoFallOffTests = 54,
CPED_CONFIG_FLAG_SteerAroundDeadBodies = 55,
CPED_CONFIG_FLAG_ConstrainToNavMesh = 56,
CPED_CONFIG_FLAG_SyncingAnimatedProps = 57,
CPED_CONFIG_FLAG_IsFiring = 58,
CPED_CONFIG_FLAG_WasFiring = 59,
CPED_CONFIG_FLAG_IsStanding = 60,
CPED_CONFIG_FLAG_WasStanding = 61,
CPED_CONFIG_FLAG_InVehicle = 62,
CPED_CONFIG_FLAG_OnMount = 63,
CPED_CONFIG_FLAG_AttachedToVehicle = 64,
CPED_CONFIG_FLAG_IsSwimming = 65,
CPED_CONFIG_FLAG_WasSwimming = 66,
CPED_CONFIG_FLAG_IsSkiing = 67,
CPED_CONFIG_FLAG_IsSitting = 68,
CPED_CONFIG_FLAG_KilledByStealth = 69,
CPED_CONFIG_FLAG_KilledByTakedown = 70,
CPED_CONFIG_FLAG_Knockedout = 71,
CPED_CONFIG_FLAG_ClearRadarBlipOnDeath = 72,
CPED_CONFIG_FLAG_JustGotOffTrain = 73,
CPED_CONFIG_FLAG_JustGotOnTrain = 74,
CPED_CONFIG_FLAG_UsingCoverPoint = 75,
CPED_CONFIG_FLAG_IsInTheAir = 76,
CPED_CONFIG_FLAG_KnockedUpIntoAir = 77,
CPED_CONFIG_FLAG_IsAimingGun = 78,
CPED_CONFIG_FLAG_HasJustLeftCar = 79,
CPED_CONFIG_FLAG_TargetWhenInjuredAllowed = 80,
CPED_CONFIG_FLAG_CurrLeftFootCollNM = 81,
CPED_CONFIG_FLAG_PrevLeftFootCollNM = 82,
CPED_CONFIG_FLAG_CurrRightFootCollNM = 83,
CPED_CONFIG_FLAG_PrevRightFootCollNM = 84,
CPED_CONFIG_FLAG_HasBeenBumpedInCar = 85,
CPED_CONFIG_FLAG_InWaterTaskQuitToClimbLadder = 86,
CPED_CONFIG_FLAG_NMTwoHandedWeaponBothHandsConstrained = 87,
CPED_CONFIG_FLAG_CreatedBloodPoolTimer = 88,
CPED_CONFIG_FLAG_DontActivateRagdollFromAnyPedImpact = 89,
CPED_CONFIG_FLAG_GroupPedFailedToEnterCover = 90,
CPED_CONFIG_FLAG_AlreadyChattedOnPhone = 91,
CPED_CONFIG_FLAG_AlreadyReactedToPedOnRoof = 92,
CPED_CONFIG_FLAG_ForcePedLoadCover = 93,
CPED_CONFIG_FLAG_BlockCoweringInCover = 94,
CPED_CONFIG_FLAG_BlockPeekingInCover = 95,
CPED_CONFIG_FLAG_JustLeftCarNotCheckedForDoors = 96,
CPED_CONFIG_FLAG_VaultFromCover = 97,
CPED_CONFIG_FLAG_AutoConversationLookAts = 98,
CPED_CONFIG_FLAG_UsingCrouchedPedCapsule = 99,
CPED_CONFIG_FLAG_HasDeadPedBeenReported = 100,
CPED_CONFIG_FLAG_ForcedAim = 101,
CPED_CONFIG_FLAG_SteersAroundPeds = 102,
CPED_CONFIG_FLAG_SteersAroundObjects = 103,
CPED_CONFIG_FLAG_OpenDoorArmIK = 104,
CPED_CONFIG_FLAG_ForceReload = 105,
CPED_CONFIG_FLAG_DontActivateRagdollFromVehicleImpact = 106,
CPED_CONFIG_FLAG_DontActivateRagdollFromBulletImpact = 107,
CPED_CONFIG_FLAG_DontActivateRagdollFromExplosions = 108,
CPED_CONFIG_FLAG_DontActivateRagdollFromFire = 109,
CPED_CONFIG_FLAG_DontActivateRagdollFromElectrocution = 110,
CPED_CONFIG_FLAG_IsBeingDraggedToSafety = 111,
CPED_CONFIG_FLAG_HasBeenDraggedToSafety = 112,
CPED_CONFIG_FLAG_KeepWeaponHolsteredUnlessFired = 113,
CPED_CONFIG_FLAG_ForceScriptControlledKnockout = 114,
CPED_CONFIG_FLAG_FallOutOfVehicleWhenKilled = 115,
CPED_CONFIG_FLAG_GetOutBurningVehicle = 116,
CPED_CONFIG_FLAG_BumpedByPlayer = 117,
CPED_CONFIG_FLAG_RunFromFiresAndExplosions = 118,
CPED_CONFIG_FLAG_TreatAsPlayerDuringTargeting = 119,
CPED_CONFIG_FLAG_IsHandCuffed = 120,
CPED_CONFIG_FLAG_IsAnkleCuffed = 121,
CPED_CONFIG_FLAG_DisableMelee = 122,
CPED_CONFIG_FLAG_DisableUnarmedDrivebys = 123,
CPED_CONFIG_FLAG_JustGetsPulledOutWhenElectrocuted = 124,
CPED_CONFIG_FLAG_UNUSED_REPLACE_ME = 125,
CPED_CONFIG_FLAG_WillNotHotwireLawEnforcementVehicle = 126,
CPED_CONFIG_FLAG_WillCommandeerRatherThanJack = 127,
CPED_CONFIG_FLAG_CanBeAgitated = 128,
CPED_CONFIG_FLAG_ForcePedToFaceLeftInCover = 129,
CPED_CONFIG_FLAG_ForcePedToFaceRightInCover = 130,
CPED_CONFIG_FLAG_BlockPedFromTurningInCover = 131,
CPED_CONFIG_FLAG_KeepRelationshipGroupAfterCleanUp = 132,
CPED_CONFIG_FLAG_ForcePedToBeDragged = 133,
CPED_CONFIG_FLAG_PreventPedFromReactingToBeingJacked = 134,
CPED_CONFIG_FLAG_IsScuba = 135,
CPED_CONFIG_FLAG_WillArrestRatherThanJack = 136,
CPED_CONFIG_FLAG_RemoveDeadExtraFarAway = 137,
CPED_CONFIG_FLAG_RidingTrain = 138,
CPED_CONFIG_FLAG_ArrestResult = 139,
CPED_CONFIG_FLAG_CanAttackFriendly = 140,
CPED_CONFIG_FLAG_WillJackAnyPlayer = 141,
CPED_CONFIG_FLAG_BumpedByPlayerVehicle = 142,
CPED_CONFIG_FLAG_DodgedPlayerVehicle = 143,
CPED_CONFIG_FLAG_WillJackWantedPlayersRatherThanStealCar = 144,
CPED_CONFIG_FLAG_NoCopWantedAggro = 145,
CPED_CONFIG_FLAG_DisableLadderClimbing = 146,
CPED_CONFIG_FLAG_StairsDetected = 147,
CPED_CONFIG_FLAG_SlopeDetected = 148,
CPED_CONFIG_FLAG_HelmetHasBeenShot = 149,
CPED_CONFIG_FLAG_CowerInsteadOfFlee = 150,
CPED_CONFIG_FLAG_CanActivateRagdollWhenVehicleUpsideDown = 151,
CPED_CONFIG_FLAG_AlwaysRespondToCriesForHelp = 152,
CPED_CONFIG_FLAG_DisableBloodPoolCreation = 153,
CPED_CONFIG_FLAG_ShouldFixIfNoCollision = 154,
CPED_CONFIG_FLAG_CanPerformArrest = 155,
CPED_CONFIG_FLAG_CanPerformUncuff = 156,
CPED_CONFIG_FLAG_CanBeArrested = 157,
CPED_CONFIG_FLAG_MoverConstrictedByOpposingCollisions = 158,
CPED_CONFIG_FLAG_PlayerPreferFrontSeatMP = 159,
CPED_CONFIG_FLAG_DontActivateRagdollFromImpactObject = 160,
CPED_CONFIG_FLAG_DontActivateRagdollFromMelee = 161,
CPED_CONFIG_FLAG_DontActivateRagdollFromWaterJet = 162,
CPED_CONFIG_FLAG_DontActivateRagdollFromDrowning = 163,
CPED_CONFIG_FLAG_DontActivateRagdollFromFalling = 164,
CPED_CONFIG_FLAG_DontActivateRagdollFromRubberBullet = 165,
CPED_CONFIG_FLAG_IsInjured = 166,
CPED_CONFIG_FLAG_DontEnterVehiclesInPlayersGroup = 167,
CPED_CONFIG_FLAG_SwimmingTasksRunning = 168,
CPED_CONFIG_FLAG_PreventAllMeleeTaunts = 169,
CPED_CONFIG_FLAG_ForceDirectEntry = 170,
CPED_CONFIG_FLAG_AlwaysSeeApproachingVehicles = 171,
CPED_CONFIG_FLAG_CanDiveAwayFromApproachingVehicles = 172,
CPED_CONFIG_FLAG_AllowPlayerToInterruptVehicleEntryExit = 173,
CPED_CONFIG_FLAG_OnlyAttackLawIfPlayerIsWanted = 174,
CPED_CONFIG_FLAG_PlayerInContactWithKinematicPed = 175,
CPED_CONFIG_FLAG_PlayerInContactWithSomethingOtherThanKinematicPed = 176,
CPED_CONFIG_FLAG_PedsJackingMeDontGetIn = 177,
CPED_CONFIG_FLAG_AdditionalRappellingPed = 178,
CPED_CONFIG_FLAG_PedIgnoresAnimInterruptEvents = 179,
CPED_CONFIG_FLAG_IsInCustody = 180,
CPED_CONFIG_FLAG_ForceStandardBumpReactionThresholds = 181,
CPED_CONFIG_FLAG_LawWillOnlyAttackIfPlayerIsWanted = 182,
CPED_CONFIG_FLAG_IsAgitated = 183,
CPED_CONFIG_FLAG_PreventAutoShuffleToDriversSeat = 184,
CPED_CONFIG_FLAG_UseKinematicModeWhenStationary = 185,
CPED_CONFIG_FLAG_EnableWeaponBlocking = 186,
CPED_CONFIG_FLAG_HasHurtStarted = 187,
CPED_CONFIG_FLAG_DisableHurt = 188,
CPED_CONFIG_FLAG_PlayerIsWeird = 189,
CPED_CONFIG_FLAG_PedHadPhoneConversation = 190,
CPED_CONFIG_FLAG_BeganCrossingRoad = 191,
CPED_CONFIG_FLAG_WarpIntoLeadersVehicle = 192,
CPED_CONFIG_FLAG_DoNothingWhenOnFootByDefault = 193,
CPED_CONFIG_FLAG_UsingScenario = 194,
CPED_CONFIG_FLAG_VisibleOnScreen = 195,
CPED_CONFIG_FLAG_DontCollideWithKinematic = 196,
CPED_CONFIG_FLAG_ActivateOnSwitchFromLowPhysicsLod = 197,
CPED_CONFIG_FLAG_DontActivateRagdollOnPedCollisionWhenDead = 198,
CPED_CONFIG_FLAG_DontActivateRagdollOnVehicleCollisionWhenDead = 199,
CPED_CONFIG_FLAG_HasBeenInArmedCombat = 200,
CPED_CONFIG_FLAG_UseDiminishingAmmoRate = 201,
CPED_CONFIG_FLAG_Avoidance_Ignore_All = 202,
CPED_CONFIG_FLAG_Avoidance_Ignored_by_All = 203,
CPED_CONFIG_FLAG_Avoidance_Ignore_Group1 = 204,
CPED_CONFIG_FLAG_Avoidance_Member_of_Group1 = 205,
CPED_CONFIG_FLAG_ForcedToUseSpecificGroupSeatIndex = 206,
CPED_CONFIG_FLAG_LowPhysicsLodMayPlaceOnNavMesh = 207,
CPED_CONFIG_FLAG_DisableExplosionReactions = 208,
CPED_CONFIG_FLAG_DodgedPlayer = 209,
CPED_CONFIG_FLAG_WaitingForPlayerControlInterrupt = 210,
CPED_CONFIG_FLAG_ForcedToStayInCover = 211,
CPED_CONFIG_FLAG_GeneratesSoundEvents = 212,
CPED_CONFIG_FLAG_ListensToSoundEvents = 213,
CPED_CONFIG_FLAG_AllowToBeTargetedInAVehicle = 214,
CPED_CONFIG_FLAG_WaitForDirectEntryPointToBeFreeWhenExiting = 215,
CPED_CONFIG_FLAG_OnlyRequireOnePressToExitVehicle = 216,
CPED_CONFIG_FLAG_ForceExitToSkyDive = 217,
CPED_CONFIG_FLAG_SteersAroundVehicles = 218,
CPED_CONFIG_FLAG_AllowPedInVehiclesOverrideTaskFlags = 219,
CPED_CONFIG_FLAG_DontEnterLeadersVehicle = 220,
CPED_CONFIG_FLAG_DisableExitToSkyDive = 221,
CPED_CONFIG_FLAG_ScriptHasDisabledCollision = 222,
CPED_CONFIG_FLAG_UseAmbientModelScaling = 223,
CPED_CONFIG_FLAG_DontWatchFirstOnNextHurryAway = 224,
CPED_CONFIG_FLAG_DisablePotentialToBeWalkedIntoResponse = 225,
CPED_CONFIG_FLAG_DisablePedAvoidance = 226,
CPED_CONFIG_FLAG_ForceRagdollUponDeath = 227,
CPED_CONFIG_FLAG_CanLosePropsOnDamage = 228,
CPED_CONFIG_FLAG_DisablePanicInVehicle = 229,
CPED_CONFIG_FLAG_AllowedToDetachTrailer = 230,
CPED_CONFIG_FLAG_HasShotBeenReactedToFromFront = 231,
CPED_CONFIG_FLAG_HasShotBeenReactedToFromBack = 232,
CPED_CONFIG_FLAG_HasShotBeenReactedToFromLeft = 233,
CPED_CONFIG_FLAG_HasShotBeenReactedToFromRight = 234,
CPED_CONFIG_FLAG_AllowBlockDeadPedRagdollActivation = 235,
CPED_CONFIG_FLAG_IsHoldingProp = 236,
CPED_CONFIG_FLAG_BlocksPathingWhenDead = 237,
CPED_CONFIG_FLAG_ForcePlayNormalScenarioExitOnNextScriptCommand = 238,
CPED_CONFIG_FLAG_ForcePlayImmediateScenarioExitOnNextScriptCommand = 239,
CPED_CONFIG_FLAG_ForceSkinCharacterCloth = 240,
CPED_CONFIG_FLAG_LeaveEngineOnWhenExitingVehicles = 241,
CPED_CONFIG_FLAG_PhoneDisableTextingAnimations = 242,
CPED_CONFIG_FLAG_PhoneDisableTalkingAnimations = 243,
CPED_CONFIG_FLAG_PhoneDisableCameraAnimations = 244,
CPED_CONFIG_FLAG_DisableBlindFiringInShotReactions = 245,
CPED_CONFIG_FLAG_AllowNearbyCoverUsage = 246,
CPED_CONFIG_FLAG_InStrafeTransition = 247,
CPED_CONFIG_FLAG_CanPlayInCarIdles = 248,
CPED_CONFIG_FLAG_CanAttackNonWantedPlayerAsLaw = 249,
CPED_CONFIG_FLAG_WillTakeDamageWhenVehicleCrashes = 250,
CPED_CONFIG_FLAG_AICanDrivePlayerAsRearPassenger = 251,
CPED_CONFIG_FLAG_PlayerCanJackFriendlyPlayers = 252,
CPED_CONFIG_FLAG_OnStairs = 253,
CPED_CONFIG_FLAG_SimulatingAiming = 254,
CPED_CONFIG_FLAG_AIDriverAllowFriendlyPassengerSeatEntry = 255,
CPED_CONFIG_FLAG_ParentCarIsBeingRemoved = 256,
CPED_CONFIG_FLAG_AllowMissionPedToUseInjuredMovement = 257,
CPED_CONFIG_FLAG_CanLoseHelmetOnDamage = 258,
CPED_CONFIG_FLAG_NeverDoScenarioExitProbeChecks = 259,
CPED_CONFIG_FLAG_SuppressLowLODRagdollSwitchWhenCorpseSettles = 260,
CPED_CONFIG_FLAG_PreventUsingLowerPrioritySeats = 261,
CPED_CONFIG_FLAG_JustLeftVehicleNeedsReset = 262,
CPED_CONFIG_FLAG_TeleportIfCantReachPlayer = 263,
CPED_CONFIG_FLAG_PedsInVehiclePositionNeedsReset = 264,
CPED_CONFIG_FLAG_PedsFullyInSeat = 265,
CPED_CONFIG_FLAG_AllowPlayerLockOnIfFriendly = 266,
CPED_CONFIG_FLAG_UseCameraHeadingForDesiredDirectionLockOnTest = 267,
CPED_CONFIG_FLAG_TeleportToLeaderVehicle = 268,
CPED_CONFIG_FLAG_Avoidance_Ignore_WeirdPedBuffer = 269,
CPED_CONFIG_FLAG_OnStairSlope = 270,
CPED_CONFIG_FLAG_HasPlayedNMGetup = 271,
CPED_CONFIG_FLAG_DontBlipCop = 272,
CPED_CONFIG_FLAG_SpawnedAtExtendedRangeScenario = 273,
CPED_CONFIG_FLAG_WalkAlongsideLeaderWhenClose = 274,
CPED_CONFIG_FLAG_KillWhenTrapped = 275,
CPED_CONFIG_FLAG_EdgeDetected = 276,
CPED_CONFIG_FLAG_AlwaysWakeUpPhysicsOfIntersectedPeds = 277,
CPED_CONFIG_FLAG_EquippedAmbientLoadOutWeapon = 278,
CPED_CONFIG_FLAG_AvoidTearGas = 279,
CPED_CONFIG_FLAG_StoppedSpeechUponFreezing = 280,
CPED_CONFIG_FLAG_DisableGoToWritheWhenInjured = 281,
CPED_CONFIG_FLAG_OnlyUseForcedSeatWhenEnteringHeliInGroup = 282,
CPED_CONFIG_FLAG_ThrownFromVehicleDueToExhaustion = 283,
CPED_CONFIG_FLAG_UpdateEnclosedSearchRegion = 284,
CPED_CONFIG_FLAG_DisableWeirdPedEvents = 285,
CPED_CONFIG_FLAG_ShouldChargeNow = 286,
CPED_CONFIG_FLAG_RagdollingOnBoat = 287,
CPED_CONFIG_FLAG_HasBrandishedWeapon = 288,
CPED_CONFIG_FLAG_AllowMinorReactionsAsMissionPed = 289,
CPED_CONFIG_FLAG_BlockDeadBodyShockingEventsWhenDead = 290,
CPED_CONFIG_FLAG_PedHasBeenSeen = 291,
CPED_CONFIG_FLAG_PedIsInReusePool = 292,
CPED_CONFIG_FLAG_PedWasReused = 293,
CPED_CONFIG_FLAG_DisableShockingEvents = 294,
CPED_CONFIG_FLAG_MovedUsingLowLodPhysicsSinceLastActive = 295,
CPED_CONFIG_FLAG_NeverReactToPedOnRoof = 296,
CPED_CONFIG_FLAG_ForcePlayFleeScenarioExitOnNextScriptCommand = 297,
CPED_CONFIG_FLAG_JustBumpedIntoVehicle = 298,
CPED_CONFIG_FLAG_DisableShockingDrivingOnPavementEvents = 299,
CPED_CONFIG_FLAG_ShouldThrowSmokeNow = 300,
CPED_CONFIG_FLAG_DisablePedConstraints = 301,
CPED_CONFIG_FLAG_ForceInitialPeekInCover = 302,
CPED_CONFIG_FLAG_CreatedByDispatch = 303,
CPED_CONFIG_FLAG_PointGunLeftHandSupporting = 304,
CPED_CONFIG_FLAG_DisableJumpingFromVehiclesAfterLeader = 305,
CPED_CONFIG_FLAG_DontActivateRagdollFromPlayerPedImpact = 306,
CPED_CONFIG_FLAG_DontActivateRagdollFromAiRagdollImpact = 307,
CPED_CONFIG_FLAG_DontActivateRagdollFromPlayerRagdollImpact = 308,
CPED_CONFIG_FLAG_DisableQuadrupedSpring = 309,
CPED_CONFIG_FLAG_IsInCluster = 310,
CPED_CONFIG_FLAG_ShoutToGroupOnPlayerMelee = 311,
CPED_CONFIG_FLAG_IgnoredByAutoOpenDoors = 312,
CPED_CONFIG_FLAG_PreferInjuredGetup = 313,
CPED_CONFIG_FLAG_ForceIgnoreMeleeActiveCombatant = 314,
CPED_CONFIG_FLAG_CheckLoSForSoundEvents = 315,
CPED_CONFIG_FLAG_JackedAbandonedCar = 316,
CPED_CONFIG_FLAG_CanSayFollowedByPlayerAudio = 317,
CPED_CONFIG_FLAG_ActivateRagdollFromMinorPlayerContact = 318,
CPED_CONFIG_FLAG_HasPortablePickupAttached = 319,
CPED_CONFIG_FLAG_ForcePoseCharacterCloth = 320,
CPED_CONFIG_FLAG_HasClothCollisionBounds = 321,
CPED_CONFIG_FLAG_HasHighHeels = 322,
CPED_CONFIG_FLAG_TreatAsAmbientPedForDriverLockOn = 323,
CPED_CONFIG_FLAG_DontBehaveLikeLaw = 324,
CPED_CONFIG_FLAG_SpawnedAtScenario = 325,
CPED_CONFIG_FLAG_DisablePoliceInvestigatingBody = 326,
CPED_CONFIG_FLAG_DisableWritheShootFromGround = 327,
CPED_CONFIG_FLAG_LowerPriorityOfWarpSeats = 328,
CPED_CONFIG_FLAG_DisableTalkTo = 329,
CPED_CONFIG_FLAG_DontBlip = 330,
CPED_CONFIG_FLAG_IsSwitchingWeapon = 331,
CPED_CONFIG_FLAG_IgnoreLegIkRestrictions = 332,
CPED_CONFIG_FLAG_ScriptForceNoTimesliceIntelligenceUpdate = 333,
CPED_CONFIG_FLAG_JackedOutOfMyVehicle = 334,
CPED_CONFIG_FLAG_WentIntoCombatAfterBeingJacked = 335,
CPED_CONFIG_FLAG_DontActivateRagdollForVehicleGrab = 336,
CPED_CONFIG_FLAG_ForcePackageCharacterCloth = 337,
CPED_CONFIG_FLAG_DontRemoveWithValidOrder = 338,
CPED_CONFIG_FLAG_AllowTaskDoNothingTimeslicing = 339,
CPED_CONFIG_FLAG_ForcedToStayInCoverDueToPlayerSwitch = 340,
CPED_CONFIG_FLAG_ForceProneCharacterCloth = 341,
CPED_CONFIG_FLAG_NotAllowedToJackAnyPlayers = 342,
CPED_CONFIG_FLAG_InToStrafeTransition = 343,
CPED_CONFIG_FLAG_KilledByStandardMelee = 344,
CPED_CONFIG_FLAG_AlwaysLeaveTrainUponArrival = 345,
CPED_CONFIG_FLAG_ForcePlayDirectedNormalScenarioExitOnNextScriptCommand = 346,
CPED_CONFIG_FLAG_OnlyWritheFromWeaponDamage = 347,
CPED_CONFIG_FLAG_UseSloMoBloodVfx = 348,
CPED_CONFIG_FLAG_EquipJetpack = 349,
CPED_CONFIG_FLAG_PreventDraggedOutOfCarThreatResponse = 350,
CPED_CONFIG_FLAG_ScriptHasCompletelyDisabledCollision = 351,
CPED_CONFIG_FLAG_NeverDoScenarioNavChecks = 352,
CPED_CONFIG_FLAG_ForceSynchronousScenarioExitChecking = 353,
CPED_CONFIG_FLAG_ThrowingGrenadeWhileAiming = 354,
CPED_CONFIG_FLAG_HeadbobToRadioEnabled = 355,
CPED_CONFIG_FLAG_ForceDeepSurfaceCheck = 356,
CPED_CONFIG_FLAG_DisableDeepSurfaceAnims = 357,
CPED_CONFIG_FLAG_DontBlipNotSynced = 358,
CPED_CONFIG_FLAG_IsDuckingInVehicle = 359,
CPED_CONFIG_FLAG_PreventAutoShuffleToTurretSeat = 360,
CPED_CONFIG_FLAG_DisableEventInteriorStatusCheck = 361,
CPED_CONFIG_FLAG_HasReserveParachute = 362,
CPED_CONFIG_FLAG_UseReserveParachute = 363,
CPED_CONFIG_FLAG_TreatDislikeAsHateWhenInCombat = 364,
CPED_CONFIG_FLAG_OnlyUpdateTargetWantedIfSeen = 365,
CPED_CONFIG_FLAG_AllowAutoShuffleToDriversSeat = 366,
CPED_CONFIG_FLAG_DontActivateRagdollFromSmokeGrenade = 367,
CPED_CONFIG_FLAG_LinkMBRToOwnerOnChain = 368,
CPED_CONFIG_FLAG_AmbientFriendBumpedByPlayer = 369,
CPED_CONFIG_FLAG_AmbientFriendBumpedByPlayerVehicle = 370,
CPED_CONFIG_FLAG_InFPSUnholsterTransition = 371,
CPED_CONFIG_FLAG_PreventReactingToSilencedCloneBullets = 372,
CPED_CONFIG_FLAG_DisableInjuredCryForHelpEvents = 373,
CPED_CONFIG_FLAG_NeverLeaveTrain = 374,
CPED_CONFIG_FLAG_DontDropJetpackOnDeath = 375,
CPED_CONFIG_FLAG_UseFPSUnholsterTransitionDuringCombatRoll = 376,
CPED_CONFIG_FLAG_ExitingFPSCombatRoll = 377,
CPED_CONFIG_FLAG_ScriptHasControlOfPlayer = 378,
CPED_CONFIG_FLAG_PlayFPSIdleFidgetsForProjectile = 379,
CPED_CONFIG_FLAG_DisableAutoEquipHelmetsInBikes = 380,
CPED_CONFIG_FLAG_DisableAutoEquipHelmetsInAircraft = 381,
CPED_CONFIG_FLAG_WasPlayingFPSGetup = 382,
CPED_CONFIG_FLAG_WasPlayingFPSMeleeActionResult = 383,
CPED_CONFIG_FLAG_PreferNoPriorityRemoval = 384,
CPED_CONFIG_FLAG_FPSFidgetsAbortedOnFire = 385,
CPED_CONFIG_FLAG_ForceFPSIKWithUpperBodyAnim = 386,
CPED_CONFIG_FLAG_SwitchingCharactersInFirstPerson = 387,
CPED_CONFIG_FLAG_IsClimbingLadder = 388,
CPED_CONFIG_FLAG_HasBareFeet = 389,
CPED_CONFIG_FLAG_UNUSED_REPLACE_ME_2 = 390,
CPED_CONFIG_FLAG_GoOnWithoutVehicleIfItIsUnableToGetBackToRoad = 391,
CPED_CONFIG_FLAG_BlockDroppingHealthSnacksOnDeath = 392,
CPED_CONFIG_FLAG_ResetLastVehicleOnVehicleExit = 393,
CPED_CONFIG_FLAG_ForceThreatResponseToNonFriendToFriendMeleeActions = 394,
CPED_CONFIG_FLAG_DontRespondToRandomPedsDamage = 395,
CPED_CONFIG_FLAG_AllowContinuousThreatResponseWantedLevelUpdates = 396,
CPED_CONFIG_FLAG_KeepTargetLossResponseOnCleanup = 397,
CPED_CONFIG_FLAG_PlayersDontDragMeOutOfCar = 398,
CPED_CONFIG_FLAG_BroadcastRepondedToThreatWhenGoingToPointShooting = 399,
CPED_CONFIG_FLAG_IgnorePedTypeForIsFriendlyWith = 400,
CPED_CONFIG_FLAG_TreatNonFriendlyAsHateWhenInCombat = 401,
CPED_CONFIG_FLAG_DontLeaveVehicleIfLeaderNotInVehicle = 402,
CPED_CONFIG_FLAG_ChangeFromPermanentToAmbientPopTypeOnMigration = 403,
CPED_CONFIG_FLAG_AllowMeleeReactionIfMeleeProofIsOn = 404,
CPED_CONFIG_FLAG_UsingLowriderLeans = 405,
CPED_CONFIG_FLAG_UsingAlternateLowriderLeans = 406,
CPED_CONFIG_FLAG_UseNormalExplosionDamageWhenBlownUpInVehicle = 407,
CPED_CONFIG_FLAG_DisableHomingMissileLockForVehiclePedInside = 408,
CPED_CONFIG_FLAG_DisableTakeOffScubaGear = 409,
CPED_CONFIG_FLAG_IgnoreMeleeFistWeaponDamageMult = 410,
CPED_CONFIG_FLAG_LawPedsCanFleeFromNonWantedPlayer = 411,
CPED_CONFIG_FLAG_ForceBlipSecurityPedsIfPlayerIsWanted = 412,
CPED_CONFIG_FLAG_IsHolsteringWeapon = 413,
CPED_CONFIG_FLAG_UseGoToPointForScenarioNavigation = 414,
CPED_CONFIG_FLAG_DontClearLocalPassengersWantedLevel = 415,
CPED_CONFIG_FLAG_BlockAutoSwapOnWeaponPickups = 416,
CPED_CONFIG_FLAG_ThisPedIsATargetPriorityForAI = 417,
CPED_CONFIG_FLAG_IsSwitchingHelmetVisor = 418,
CPED_CONFIG_FLAG_ForceHelmetVisorSwitch = 419,
CPED_CONFIG_FLAG_IsPerformingVehicleMelee = 420,
CPED_CONFIG_FLAG_UseOverrideFootstepPtFx = 421,
CPED_CONFIG_FLAG_DisableVehicleCombat = 422,
CPED_CONFIG_FLAG_TreatAsFriendlyForTargetingAndDamage = 423,
CPED_CONFIG_FLAG_AllowBikeAlternateAnimations = 424,
CPED_CONFIG_FLAG_TreatAsFriendlyForTargetingAndDamageNonSynced = 425,
CPED_CONFIG_FLAG_UseLockpickVehicleEntryAnimations = 426,
CPED_CONFIG_FLAG_IgnoreInteriorCheckForSprinting = 427,
CPED_CONFIG_FLAG_SwatHeliSpawnWithinLastSpottedLocation = 428,
CPED_CONFIG_FLAG_DisableStartEngine = 429,
CPED_CONFIG_FLAG_IgnoreBeingOnFire = 430,
CPED_CONFIG_FLAG_DisableTurretOrRearSeatPreference = 431,
CPED_CONFIG_FLAG_DisableWantedHelicopterSpawning = 432,
CPED_CONFIG_FLAG_UseTargetPerceptionForCreatingAimedAtEvents = 433,
CPED_CONFIG_FLAG_DisableHomingMissileLockon = 434,
CPED_CONFIG_FLAG_ForceIgnoreMaxMeleeActiveSupportCombatants = 435,
CPED_CONFIG_FLAG_StayInDefensiveAreaWhenInVehicle = 436,
CPED_CONFIG_FLAG_DontShoutTargetPosition = 437,
CPED_CONFIG_FLAG_DisableHelmetArmor = 438,
CPED_CONFIG_FLAG_CreatedByConcealedPlayer = 439,
CPED_CONFIG_FLAG_PermanentlyDisablePotentialToBeWalkedIntoResponse = 440,
CPED_CONFIG_FLAG_PreventVehExitDueToInvalidWeapon = 441,
CPED_CONFIG_FLAG_IgnoreNetSessionFriendlyFireCheckForAllowDamage = 442,
CPED_CONFIG_FLAG_DontLeaveCombatIfTargetPlayerIsAttackedByPolice = 443,
CPED_CONFIG_FLAG_CheckLockedBeforeWarp = 444,
CPED_CONFIG_FLAG_DontShuffleInVehicleToMakeRoom = 445,
CPED_CONFIG_FLAG_GiveWeaponOnGetup = 446,
CPED_CONFIG_FLAG_DontHitVehicleWithProjectiles = 447,
CPED_CONFIG_FLAG_DisableForcedEntryForOpenVehiclesFromTryLockedDoor = 448,
CPED_CONFIG_FLAG_FiresDummyRockets = 449,
CPED_CONFIG_FLAG_PedIsArresting = 450,
CPED_CONFIG_FLAG_IsDecoyPed = 451,
CPED_CONFIG_FLAG_HasEstablishedDecoy = 452,
CPED_CONFIG_FLAG_BlockDispatchedHelicoptersFromLanding = 453,
CPED_CONFIG_FLAG_DontCryForHelpOnStun = 454,
CPED_CONFIG_FLAG_HitByTranqWeapon = 455,
CPED_CONFIG_FLAG_CanBeIncapacitated = 456,
CPED_CONFIG_FLAG_ForcedAimFromArrest = 457,
CPED_CONFIG_FLAG_DontChangeTargetFromMelee = 458,
_0x4376ABF2 = 459,
CPED_CONFIG_FLAG_RagdollFloatsIndefinitely = 460,
CPED_CONFIG_FLAG_BlockElectricWeaponDamage = 461,
_0x262A3B8E = 462,
_0x1AA79A25 = 463,
}
```

**This is the server-side RPC native equivalent of the client native [SET_PED_CONFIG_FLAG](#setpedconfigflag).**

---
### SetPedDefaultComponentVariation

`SET_PED_DEFAULT_COMPONENT_VARIATION` · hash `0xC866A984` · **Servidor**

```lua
SetPedDefaultComponentVariation(ped)
```
```c
void SET_PED_DEFAULT_COMPONENT_VARIATION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets Ped Default Clothes
```

**This is the server-side RPC native equivalent of the client native [SET_PED_DEFAULT_COMPONENT_VARIATION](#setpeddefaultcomponentvariation).**

---
### SetPedEyeColor

`_SET_PED_EYE_COLOR` · hash `0xEC09DB1B` · **Servidor**

```lua
SetPedEyeColor(ped, index)
```
```c
void _SET_PED_EYE_COLOR(Ped ped, int index);
```

**Parámetros**

- `ped` (`Ped`)
- `index` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Used for freemode (online) characters.
Indices:

1.  black
2.  very light blue/green
3.  dark blue
4.  brown
5.  darker brown
6.  light brown
7.  blue
8.  light blue
9.  pink
10. yellow
11. purple
12. black
13. dark green
14. light brown
15. yellow/black pattern
16. light colored spiral pattern
17. shiny red
18. shiny half blue/half red
19. half black/half light blue
20. white/red perimter
21. green snake
22. red snake
23. dark blue snake
24. dark yellow
25. bright yellow
26. all black
27. red small pupil
28. devil blue/black
29. white small pupil
30. glossed over

**This is the server-side RPC native equivalent of the client native [\_SET_PED_EYE_COLOR](#setpedeyecolor).**

---
### SetPedFaceFeature

`_SET_PED_FACE_FEATURE` · hash `0x6C8D4458` · **Servidor**

```lua
SetPedFaceFeature(ped, index, scale)
```
```c
void _SET_PED_FACE_FEATURE(Ped ped, int index, float scale);
```

**Parámetros**

- `ped` (`Ped`): The ped entity
- `index` (`int`): An integer ranging from 0 to 19
- `scale` (`float`): A float ranging from -1.0 to 1.0

**Devuelve:** `void`

**Descripción oficial:**

Sets the various freemode face features, e.g. nose length, chin shape.
**Indexes (From 0 to 19):**
Parentheses indicate morph scale/direction as in (-1.0 to 1.0)

*   **0**: Nose Width (Thin/Wide)
*   **1**: Nose Peak (Up/Down)
*   **2**: Nose Length (Long/Short)
*   **3**: Nose Bone Curveness (Crooked/Curved)
*   **4**: Nose Tip (Up/Down)
*   **5**: Nose Bone Twist (Left/Right)
*   **6**: Eyebrow (Up/Down)
*   **7**: Eyebrow (In/Out)
*   **8**: Cheek Bones (Up/Down)
*   **9**: Cheek Sideways Bone Size (In/Out)
*   **10**: Cheek Bones Width (Puffed/Gaunt)
*   **11**: Eye Opening (Both) (Wide/Squinted)
*   **12**: Lip Thickness (Both) (Fat/Thin)
*   **13**: Jaw Bone Width (Narrow/Wide)
*   **14**: Jaw Bone Shape (Round/Square)
*   **15**: Chin Bone (Up/Down)
*   **16**: Chin Bone Length (In/Out or Backward/Forward)
*   **17**: Chin Bone Shape (Pointed/Square)
*   **18**: Chin Hole (Chin Bum)
*   **19**: Neck Thickness (Thin/Thick)
    **Note:**
    You may need to call [`SetPedHeadBlendData`](#setpedheadblenddata) prior to calling this native in order for it to work.

**This is the server-side RPC native equivalent of the client native [\_SET_PED_FACE_FEATURE](#setpedfacefeature).**

---
### SetPedHairTint

`SET_PED_HAIR_TINT` · hash `0xA23FE32C` · **Servidor**

```lua
SetPedHairTint(ped, colorID, highlightColorID)
```
```c
void SET_PED_HAIR_TINT(Ped ped, int colorID, int highlightColorID);
```

**Parámetros**

- `ped` (`Ped`): The Ped whose hair tint is to be set.
- `colorID` (`int`): The tint index for the primary hair color.
- `highlightColorID` (`int`): The tint index for the hair highlight color.

**Devuelve:** `void`

**Descripción oficial:**

Sets the tint index for the hair on the specified ped.

```
NativeDB Introduced: v323
```

**This is the server-side RPC native equivalent of the client native [SET_PED_HAIR_TINT](#setpedhairtint).**

**Nombres antiguos (alias):** `_SET_PED_HAIR_COLOR` (`SetPedHairColor`)

---
### SetPedHeadBlendData

`SET_PED_HEAD_BLEND_DATA` · hash `0x60746B88` · **Servidor**

```lua
SetPedHeadBlendData(ped, shapeFirstID, shapeSecondID, shapeThirdID, skinFirstID, skinSecondID, skinThirdID, shapeMix, skinMix, thirdMix, isParent)
```
```c
void SET_PED_HEAD_BLEND_DATA(Ped ped, int shapeFirstID, int shapeSecondID, int shapeThirdID, int skinFirstID, int skinSecondID, int skinThirdID, float shapeMix, float skinMix, float thirdMix, BOOL isParent);
```

**Parámetros**

- `ped` (`Ped`): The ped entity
- `shapeFirstID` (`int`): Controls the shape of the first ped's face
- `shapeSecondID` (`int`): Controls the shape of the second ped's face
- `shapeThirdID` (`int`): Controls the shape of the third ped's face
- `skinFirstID` (`int`): Controls the first id's skin tone
- `skinSecondID` (`int`): Controls the second id's skin tone
- `skinThirdID` (`int`): Controls the third id's skin tone
- `shapeMix` (`float`): 0.0 - 1.0 Of whose characteristics to take Mother -> Father (shapeFirstID and shapeSecondID)
- `skinMix` (`float`): 0.0 - 1.0 Of whose characteristics to take Mother -> Father (skinFirstID and skinSecondID)
- `thirdMix` (`float`): Overrides the others in favor of the third IDs.
- `isParent` (`BOOL`): IsParent is set for "children" of the player character's grandparents during old-gen character creation. It has unknown effect otherwise.

**Devuelve:** `void`

**Descripción oficial:**

For more info and the list of faceIDs please refer to [this](https://gtaforums.com/topic/858970-all-gtao-face-ids-pedset-ped-head-blend-data-explained) topic. Note that the Skin and Shape IDs are shared. This native will use this same list for both Skin and Shape IDs.
**Other information:**
IDs start at zero and go Male Non-DLC, Female Non-DLC, Male DLC, and Female DLC.
This native function is often called prior to calling natives such as:

*   [`SetPedHairColor`](#setpedhairtint)
*   [`SetPedHeadOverlayColor`](#setpedheadoverlaycolor)
*   [`SetPedHeadOverlay`](#setpedheadoverlay)
*   [`SetPedFaceFeature`](#setpedfacefeature)

**This is the server-side RPC native equivalent of the client native [SET_PED_HEAD_BLEND_DATA](#setpedheadblenddata).**

---
### SetPedHeadOverlay

`SET_PED_HEAD_OVERLAY` · hash `0xD28DBA90` · **Servidor**

```lua
SetPedHeadOverlay(ped, overlayID, index, opacity)
```
```c
void SET_PED_HEAD_OVERLAY(Ped ped, int overlayID, int index, float opacity);
```

**Parámetros**

- `ped` (`Ped`): The ped entity
- `overlayID` (`int`): The overlay id displayed up above.
- `index` (`int`): An integer representing the index (from 0 to `_GET_NUM_OVERLAY_VALUES(overlayID)-1`)
- `opacity` (`float`): A float ranging from 0.0 to 1.0

**Devuelve:** `void`

**Descripción oficial:**

```
OverlayID ranges from 0 to 12, index from 0 to _GET_NUM_OVERLAY_VALUES(overlayID)-1, and opacity from 0.0 to 1.0.
overlayID       Part                  Index, to disable
0               Blemishes             0 - 23, 255
1               Facial Hair           0 - 28, 255
2               Eyebrows              0 - 33, 255
3               Ageing                0 - 14, 255
4               Makeup                0 - 74, 255
5               Blush                 0 - 6, 255
6               Complexion            0 - 11, 255
7               Sun Damage            0 - 10, 255
8               Lipstick              0 - 9, 255
9               Moles/Freckles        0 - 17, 255
10              Chest Hair            0 - 16, 255
11              Body Blemishes        0 - 11, 255
12              Add Body Blemishes    0 - 1, 255
```

**Note:**
You may need to call [`SetPedHeadBlendData`](#setpedheadblenddata) prior to calling this native in order for it to work.

**This is the server-side RPC native equivalent of the client native [SET_PED_HEAD_OVERLAY](#setpedheadoverlay).**

---
### SetPedHeadOverlayColor

`_SET_PED_HEAD_OVERLAY_COLOR` · hash `0x78935A27` · **Servidor**

```lua
SetPedHeadOverlayColor(ped, overlayID, colorType, colorID, secondColorID)
```
```c
void _SET_PED_HEAD_OVERLAY_COLOR(Ped ped, int overlayID, int colorType, int colorID, int secondColorID);
```

**Parámetros**

- `ped` (`Ped`): The ped entity
- `overlayID` (`int`): An integer representing the overlay id
- `colorType` (`int`): 1 for eyebrows, beards, makeup, and chest hair; 2 for blush and lipstick; and 0 otherwise, though not called in those cases.
- `colorID` (`int`): An integer representing the primary color id
- `secondColorID` (`int`): An integer representing the secondary color id

**Devuelve:** `void`

**Descripción oficial:**

```
Used for freemode (online) characters.
Called after SET_PED_HEAD_OVERLAY().
```

**Note:**
You may need to call [`SetPedHeadBlendData`](#setpedheadblenddata) prior to calling this native in order for it to work.

**This is the server-side RPC native equivalent of the client native [\_SET_PED_HEAD_OVERLAY_COLOR](#setpedheadoverlaycolor).**

---
### SetPedIntoVehicle

`SET_PED_INTO_VEHICLE` · hash `0x7500C79` · **Servidor**

```lua
SetPedIntoVehicle(ped, vehicle, seatIndex)
```
```c
void SET_PED_INTO_VEHICLE(Ped ped, Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](../gta5/VEHICLE-1.md#isvehicleseatfree). -2 for the first available seat.

**Devuelve:** `void`

**Descripción oficial:**

SET_PED_INTO_VEHICLE

**This is the server-side RPC native equivalent of the client native [SET_PED_INTO_VEHICLE](#setpedintovehicle).**

---
### SetPedPropIndex

`SET_PED_PROP_INDEX` · hash `0x829F2E2` · **Servidor**

```lua
SetPedPropIndex(ped, componentId, drawableId, textureId, attach)
```
```c
void SET_PED_PROP_INDEX(Ped ped, int componentId, int drawableId, int textureId, BOOL attach);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component that you want to set. Refer to [SET_PED_COMPONENT_VARIATION](#setpedcomponentvariation).
- `drawableId` (`int`): The drawable id that is going to be set. Refer to [GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS](../gta5/PED-1.md#getnumberofpedpropdrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_PROP_TEXTURE_VARIATIONS](../gta5/PED-1.md#getnumberofpedproptexturevariations).
- `attach` (`BOOL`): Attached or not.

**Devuelve:** `void`

**Descripción oficial:**

This native is used to set prop variation on a ped. Components, drawables and textures IDs are related to the ped model.

**MP Freemode list of props**

**0**: Hats
**1**: Glasses
**2**: Ears
**6**: Watches
**7**: Bracelets
List of Prop IDs

```cpp
enum eAnchorPoints
{
ANCHOR_HEAD = 0, // "p_head"
ANCHOR_EYES = 1, // "p_eyes"
ANCHOR_EARS = 2, // "p_ears"
ANCHOR_MOUTH = 3, // "p_mouth"
ANCHOR_LEFT_HAND = 4, // "p_lhand"
ANCHOR_RIGHT_HAND = 5, // "p_rhand"
ANCHOR_LEFT_WRIST = 6, // "p_lwrist"
ANCHOR_RIGHT_WRIST = 7, // "p_rwrist"
ANCHOR_HIP = 8, // "p_lhip"
ANCHOR_LEFT_FOOT = 9, // "p_lfoot"
ANCHOR_RIGHT_FOOT = 10, // "p_rfoot"
ANCHOR_PH_L_HAND = 11, // "ph_lhand"
ANCHOR_PH_R_HAND = 12, // "ph_rhand"
NUM_ANCHORS = 13,
};
```

**This is the server-side RPC native equivalent of the client native [SET_PED_PROP_INDEX](#setpedpropindex).**

---
### SetPedRandomComponentVariation

`SET_PED_RANDOM_COMPONENT_VARIATION` · hash `0x4111BA46` · **Servidor**

```lua
SetPedRandomComponentVariation(ped, p1)
```
```c
void SET_PED_RANDOM_COMPONENT_VARIATION(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 is always 0 in R* scripts; and a quick disassembly seems to indicate that p1 is unused.
```

**This is the server-side RPC native equivalent of the client native [SET_PED_RANDOM_COMPONENT_VARIATION](#setpedrandomcomponentvariation).**

---
### SetPedRandomProps

`SET_PED_RANDOM_PROPS` · hash `0xE3318E0E` · **Servidor**

```lua
SetPedRandomProps(ped)
```
```c
void SET_PED_RANDOM_PROPS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.

**Devuelve:** `void`

**Descripción oficial:**

SET_PED_RANDOM_PROPS

**This is the server-side RPC native equivalent of the client native [SET_PED_RANDOM_PROPS](#setpedrandomprops).**

---
### SetPedResetFlag

`SET_PED_RESET_FLAG` · hash `0xCFF6FF66` · **Servidor**

```lua
SetPedResetFlag(ped, flagId, doReset)
```
```c
void SET_PED_RESET_FLAG(Ped ped, int flagId, BOOL doReset);
```

**Parámetros**

- `ped` (`Ped`)
- `flagId` (`int`)
- `doReset` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

PED::SET_PED_RESET_FLAG(PLAYER::PLAYER_PED_ID(), 240, 1);
Known values:

**This is the server-side RPC native equivalent of the client native [SET_PED_RESET_FLAG](#setpedresetflag).**

---
### SetPedToRagdoll

`SET_PED_TO_RAGDOLL` · hash `0x83CB5052` · **Servidor**

```lua
SetPedToRagdoll(ped, minTime, maxTime, ragdollType, bAbortIfInjured, bAbortIfDead, bForceScriptControl)
```
```c
void SET_PED_TO_RAGDOLL(Ped ped, int minTime, int maxTime, int ragdollType, BOOL bAbortIfInjured, BOOL bAbortIfDead, BOOL bForceScriptControl);
```

**Parámetros**

- `ped` (`Ped`): The ped to ragdoll.
- `minTime` (`int`): Time(ms) Ped is in ragdoll mode; only applies to ragdoll types 0 and not 1.
- `maxTime` (`int`)
- `ragdollType` (`int`)
- `bAbortIfInjured` (`BOOL`): unused
- `bAbortIfDead` (`BOOL`): unused
- `bForceScriptControl` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

p4/p5: Unusued in TU27

**Ragdoll Types**

**0**: CTaskNMRelax
**1**: CTaskNMScriptControl: Hardcoded not to work in networked environments.
**Else**: CTaskNMBalance

**This is the server-side RPC native equivalent of the client native [SET_PED_TO_RAGDOLL](#setpedtoragdoll).**

---
### SetPedToRagdollWithFall

`SET_PED_TO_RAGDOLL_WITH_FALL` · hash `0xFA12E286` · **Servidor**

```lua
SetPedToRagdollWithFall(ped, minTime, maxTime, nFallType, dirX, dirY, dirZ, fGroundHeight, grab1X, grab1Y, grab1Z, grab2X, grab2Y, grab2Z)
```
```c
void SET_PED_TO_RAGDOLL_WITH_FALL(Ped ped, int minTime, int maxTime, int nFallType, float dirX, float dirY, float dirZ, float fGroundHeight, float grab1X, float grab1Y, float grab1Z, float grab2X, float grab2Y, float grab2Z);
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

**Devuelve:** `void`

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

**This is the server-side RPC native equivalent of the client native [SET_PED_TO_RAGDOLL_WITH_FALL](#setpedtoragdollwithfall).**

---
### SetPlayerControl

`SET_PLAYER_CONTROL` · hash `0xD17AFCD8` · **Servidor**

```lua
SetPlayerControl(player, bHasControl, flags)
```
```c
void SET_PLAYER_CONTROL(Player player, BOOL bHasControl, int flags);
```

**Parámetros**

- `player` (`Player`)
- `bHasControl` (`BOOL`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Flags:
SPC_AMBIENT_SCRIPT = (1 << 1),
SPC_CLEAR_TASKS = (1 << 2),
SPC_REMOVE_FIRES = (1 << 3),
SPC_REMOVE_EXPLOSIONS = (1 << 4),
SPC_REMOVE_PROJECTILES = (1 << 5),
SPC_DEACTIVATE_GADGETS = (1 << 6),
SPC_REENABLE_CONTROL_ON_DEATH = (1 << 7),
SPC_LEAVE_CAMERA_CONTROL_ON = (1 << 8),
SPC_ALLOW_PLAYER_DAMAGE = (1 << 9),
SPC_DONT_STOP_OTHER_CARS_AROUND_PLAYER = (1 << 10),
SPC_PREVENT_EVERYBODY_BACKOFF = (1 << 11),
SPC_ALLOW_PAD_SHAKE = (1 << 12)
See: https://alloc8or.re/gta5/doc/enums/eSetPlayerControlFlag.txt
```

**This is the server-side RPC native equivalent of the client native [SET_PLAYER_CONTROL](#setplayercontrol).**

---
### SetPlayerCullingRadius

`SET_PLAYER_CULLING_RADIUS` · hash `0x8A2FBAD4` · **Servidor**

```lua
SetPlayerCullingRadius(playerSrc, radius)
```
```c
void SET_PLAYER_CULLING_RADIUS(char* playerSrc, float radius);
```

**Parámetros**

- `playerSrc` (`char*`): The player to set the culling radius for.
- `radius` (`float`): The radius.

**Devuelve:** `void`

**Descripción oficial:**

Sets the culling radius for the specified player.
Set to `0.0` to reset.

**WARNING**: Culling natives are deprecated and have known, [unfixable issues](https://forum.cfx.re/t/issue-with-culling-radius-and-server-side-entities/4900677/4)

---
### SetPlayerInvincible

`SET_PLAYER_INVINCIBLE` · hash `0xDFB9A2A2` · **Servidor**

```lua
SetPlayerInvincible(player, bInvincible)
```
```c
void SET_PLAYER_INVINCIBLE(Player player, BOOL bInvincible);
```

**Parámetros**

- `player` (`Player`): The player index.
- `bInvincible` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Make the player impervious to all forms of damage.

**This is the server-side RPC native equivalent of the client native [SET_PLAYER_INVINCIBLE](#setplayerinvincible).**

---
### SetPlayerModel

`SET_PLAYER_MODEL` · hash `0x774A4C54` · **Servidor**

```lua
SetPlayerModel(player, model)
```
```c
void SET_PLAYER_MODEL(Player player, Hash model);
```

**Parámetros**

- `player` (`Player`): The player to set the model for
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to use

**Devuelve:** `void`

**Descripción oficial:**

Set the model for a specific Player. Note that this will destroy the current Ped for the Player and create a new one, any reference to the old ped will be invalid after calling this.
As per usual, make sure to request the model first and wait until it has loaded.

**This is the server-side RPC native equivalent of the client native [SET_PLAYER_MODEL](#setplayermodel).**

---
### SetPlayerRoutingBucket

`SET_PLAYER_ROUTING_BUCKET` · hash `0x6504EB38` · **Servidor**

```lua
SetPlayerRoutingBucket(playerSrc, bucket)
```
```c
void SET_PLAYER_ROUTING_BUCKET(char* playerSrc, int bucket);
```

**Parámetros**

- `playerSrc` (`char*`): The player to set the routing bucket for.
- `bucket` (`int`): The bucket ID.

**Devuelve:** `void`

**Descripción oficial:**

Sets the routing bucket for the specified player.

Routing buckets are also known as 'dimensions' or 'virtual worlds' in past echoes, however they are population-aware.

---
### SetPlayerWantedLevel

`SET_PLAYER_WANTED_LEVEL` · hash `0xB7A0914B` · **Servidor**

```lua
SetPlayerWantedLevel(player, wantedLevel, delayedResponse)
```
```c
void SET_PLAYER_WANTED_LEVEL(Player player, int wantedLevel, BOOL delayedResponse);
```

**Parámetros**

- `player` (`Player`): the target player
- `wantedLevel` (`int`): the wanted level 1-5
- `delayedResponse` (`BOOL`): false = 0-10sec police spawn response time, true = 10-20sec police spawn response time

**Devuelve:** `void`

**Descripción oficial:**

SET_PLAYER_WANTED_LEVEL

**This is the server-side RPC native equivalent of the client native [SET_PLAYER_WANTED_LEVEL](#setplayerwantedlevel).**

---
### SetRoutingBucketEntityLockdownMode

`SET_ROUTING_BUCKET_ENTITY_LOCKDOWN_MODE` · hash `0xA0F2201F` · **Servidor**

```lua
SetRoutingBucketEntityLockdownMode(bucketId, mode)
```
```c
void SET_ROUTING_BUCKET_ENTITY_LOCKDOWN_MODE(int bucketId, char* mode);
```

**Parámetros**

- `bucketId` (`int`): The routing bucket ID to adjust.
- `mode` (`char*`): One of aforementioned modes.

**Devuelve:** `void`

**Descripción oficial:**

Sets the entity lockdown mode for a specific routing bucket.

Lockdown modes are:

| Mode       | Meaning                                                    |
| ---------- | ---------------------------------------------------------- |
| `strict`   | No entities can be created by clients at all.              |
| `relaxed`  | Only script-owned entities created by clients are blocked. |
| `inactive` | Clients can create any entity they want.                   |

---
### SetRoutingBucketPopulationEnabled

`SET_ROUTING_BUCKET_POPULATION_ENABLED` · hash `0xCE51AC2C` · **Servidor**

```lua
SetRoutingBucketPopulationEnabled(bucketId, mode)
```
```c
void SET_ROUTING_BUCKET_POPULATION_ENABLED(int bucketId, BOOL mode);
```

**Parámetros**

- `bucketId` (`int`): The routing bucket ID to adjust.
- `mode` (`BOOL`): `true` to enable population, `false` to disable population.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether or not the specified routing bucket has automatically-created population enabled.

---
### SetVehicleAlarm

`SET_VEHICLE_ALARM` · hash `0x24877D84` · **Servidor**

```lua
SetVehicleAlarm(vehicle, state)
```
```c
void SET_VEHICLE_ALARM(Vehicle vehicle, BOOL state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

SET_VEHICLE_ALARM

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_ALARM](#setvehiclealarm).**

---
### SetVehicleBodyHealth

`SET_VEHICLE_BODY_HEALTH` · hash `0x920C2517` · **Servidor**

```lua
SetVehicleBodyHealth(vehicle, value)
```
```c
void SET_VEHICLE_BODY_HEALTH(Vehicle vehicle, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
p2 often set to 1000.0 in the decompiled scripts.
```

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_BODY_HEALTH](#setvehiclebodyhealth).**

---
### SetVehicleColourCombination

`SET_VEHICLE_COLOUR_COMBINATION` · hash `0xA557AEAD` · **Servidor**

```lua
SetVehicleColourCombination(vehicle, colorCombination)
```
```c
void SET_VEHICLE_COLOUR_COMBINATION(Vehicle vehicle, int colorCombination);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to modify.
- `colorCombination` (`int`): One of the default color values of the vehicle.

**Devuelve:** `void`

**Descripción oficial:**

Sets the selected vehicle's colors to their default value (specific variant specified using the colorCombination parameter).
Range of possible values for colorCombination is currently unknown, I couldn't find where these values are stored either (Disquse's guess was vehicles.meta but I haven't seen it in there.)

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_COLOUR_COMBINATION](#setvehiclecolourcombination).**

---
### SetVehicleColours

`SET_VEHICLE_COLOURS` · hash `0x57F24253` · **Servidor**

```lua
SetVehicleColours(vehicle, colorPrimary, colorSecondary)
```
```c
void SET_VEHICLE_COLOURS(Vehicle vehicle, int colorPrimary, int colorSecondary);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `colorPrimary` (`int`)
- `colorSecondary` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

colorPrimary & colorSecondary are the paint indexes for the vehicle.
For a list of valid paint indexes, view: pastebin.com/pwHci0xK

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_COLOURS](#setvehiclecolours).**

---
### SetVehicleCustomPrimaryColour

`SET_VEHICLE_CUSTOM_PRIMARY_COLOUR` · hash `0x8DF9F9BC` · **Servidor**

```lua
SetVehicleCustomPrimaryColour(vehicle, r, g, b)
```
```c
void SET_VEHICLE_CUSTOM_PRIMARY_COLOUR(Vehicle vehicle, int r, int g, int b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1, p2, p3 are RGB values for color (255,0,0 for Red, ect)
```

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_CUSTOM_PRIMARY_COLOUR](#setvehiclecustomprimarycolour).**

---
### SetVehicleCustomSecondaryColour

`SET_VEHICLE_CUSTOM_SECONDARY_COLOUR` · hash `0x9D77259E` · **Servidor**

```lua
SetVehicleCustomSecondaryColour(vehicle, r, g, b)
```
```c
void SET_VEHICLE_CUSTOM_SECONDARY_COLOUR(Vehicle vehicle, int r, int g, int b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1, p2, p3 are RGB values for color (255,0,0 for Red, ect)
```

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_CUSTOM_SECONDARY_COLOUR](#setvehiclecustomsecondarycolour).**

---
### SetVehicleDirtLevel

`SET_VEHICLE_DIRT_LEVEL` · hash `0x2B39128B` · **Servidor**

```lua
SetVehicleDirtLevel(vehicle, dirtLevel)
```
```c
void SET_VEHICLE_DIRT_LEVEL(Vehicle vehicle, float dirtLevel);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set.
- `dirtLevel` (`float`): A number between 0.0 and 15.0 representing the vehicles dirt level.

**Devuelve:** `void`

**Descripción oficial:**

Sets the dirt level of the passed vehicle.

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_DIRT_LEVEL](#setvehicledirtlevel).**

---
### SetVehicleDoorBroken

`SET_VEHICLE_DOOR_BROKEN` · hash `0x8147FEA7` · **Servidor**

```lua
SetVehicleDoorBroken(vehicle, doorIndex, deleteDoor)
```
```c
void SET_VEHICLE_DOOR_BROKEN(Vehicle vehicle, int doorIndex, BOOL deleteDoor);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)
- `deleteDoor` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](../gta5/VEHICLE-2.md#setvehicledoorshut)

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_DOOR_BROKEN](#setvehicledoorbroken).**

---
### SetVehicleDoorsLocked

`SET_VEHICLE_DOORS_LOCKED` · hash `0x4CDD35D0` · **Servidor**

```lua
SetVehicleDoorsLocked(vehicle, doorLockStatus)
```
```c
void SET_VEHICLE_DOORS_LOCKED(Vehicle vehicle, int doorLockStatus);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle whose doors are to be locked.
- `doorLockStatus` (`int`): The lock state to apply to the vehicle's doors, see `eVehicleLockState`.

**Devuelve:** `void`

**Descripción oficial:**

Locks the doors of a specified vehicle to a defined lock state, affecting how players and NPCs can interact with the vehicle.

```
NativeDB Introduced: v323
```

```cpp
enum eVehicleLockState {
// No specific lock state, vehicle behaves according to the game's default settings.
VEHICLELOCK_NONE = 0,
// Vehicle is fully unlocked, allowing free entry by players and NPCs.
VEHICLELOCK_UNLOCKED = 1,
// Vehicle is locked, preventing entry by players and NPCs.
VEHICLELOCK_LOCKED = 2,
// Vehicle locks out only players, allowing NPCs to enter.
VEHICLELOCK_LOCKOUT_PLAYER_ONLY = 3,
// Vehicle is locked once a player enters, preventing others from entering.
VEHICLELOCK_LOCKED_PLAYER_INSIDE = 4,
// Vehicle starts in a locked state, but may be unlocked through game events.
VEHICLELOCK_LOCKED_INITIALLY = 5,
// Forces the vehicle's doors to shut and lock.
VEHICLELOCK_FORCE_SHUT_DOORS = 6,
// Vehicle is locked but can still be damaged.
VEHICLELOCK_LOCKED_BUT_CAN_BE_DAMAGED = 7,
// Vehicle is locked, but its trunk/boot remains unlocked.
VEHICLELOCK_LOCKED_BUT_BOOT_UNLOCKED = 8,
// Vehicle is locked and does not allow passengers, except for the driver.
VEHICLELOCK_LOCKED_NO_PASSENGERS = 9,
// Vehicle is completely locked, preventing entry entirely, even if previously inside.
VEHICLELOCK_CANNOT_ENTER = 10
};
```

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_DOORS_LOCKED](#setvehicledoorslocked).**

---
### SetVehicleNumberPlateText

`SET_VEHICLE_NUMBER_PLATE_TEXT` · hash `0x400F9556` · **Servidor**

```lua
SetVehicleNumberPlateText(vehicle, plateText)
```
```c
void SET_VEHICLE_NUMBER_PLATE_TEXT(Vehicle vehicle, char* plateText);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set the plate for
- `plateText` (`char*`): The text to set the plate to, 8 chars maximum

**Devuelve:** `void`

**Descripción oficial:**

SET_VEHICLE_NUMBER_PLATE_TEXT

**This is the server-side RPC native equivalent of the client native [SET_VEHICLE_NUMBER_PLATE_TEXT](#setvehiclenumberplatetext).**

---
### StartResource

`START_RESOURCE` · hash `0x29B440DC` · **Servidor**

```lua
local retval = StartResource(resourceName)
```
```c
BOOL START_RESOURCE(char* resourceName);
```

**Parámetros**

- `resourceName` (`char*`)

**Devuelve:** `BOOL`

---
### StopResource

`STOP_RESOURCE` · hash `0x21783161` · **Servidor**

```lua
local retval = StopResource(resourceName)
```
```c
BOOL STOP_RESOURCE(char* resourceName);
```

**Parámetros**

- `resourceName` (`char*`)

**Devuelve:** `BOOL`

---
### TaskCombatPed

`TASK_COMBAT_PED` · hash `0xCB0D8932` · **Servidor**

```lua
TaskCombatPed(ped, targetPed, p2, p3)
```
```c
void TASK_COMBAT_PED(Ped ped, Ped targetPed, int p2, int p3);
```

**Parámetros**

- `ped` (`Ped`)
- `targetPed` (`Ped`)
- `p2` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the specified ped attack the target ped.
p2 should be 0
p3 should be 16
```

**This is the server-side RPC native equivalent of the client native [TASK_COMBAT_PED](#taskcombatped).**

---
### TaskDriveBy

`TASK_DRIVE_BY` · hash `0x2B84D1C4` · **Servidor**

```lua
TaskDriveBy(driverPed, targetPed, targetVehicle, targetX, targetY, targetZ, distanceToShoot, pedAccuracy, p8, firingPattern)
```
```c
void TASK_DRIVE_BY(Ped driverPed, Ped targetPed, Vehicle targetVehicle, float targetX, float targetY, float targetZ, float distanceToShoot, int pedAccuracy, BOOL p8, Hash firingPattern);
```

**Parámetros**

- `driverPed` (`Ped`)
- `targetPed` (`Ped`)
- `targetVehicle` (`Vehicle`)
- `targetX` (`float`)
- `targetY` (`float`)
- `targetZ` (`float`)
- `distanceToShoot` (`float`)
- `pedAccuracy` (`int`)
- `p8` (`BOOL`)
- `firingPattern` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Example:
TASK::TASK_DRIVE_BY(l_467[1/*22*/], PLAYER::PLAYER_PED_ID(), 0, 0.0, 0.0, 2.0, 300.0, 100, 0, ${firing_pattern_burst_fire_driveby});
Needs working example. Doesn't seem to do anything.
I marked p2 as targetVehicle as all these shooting related tasks seem to have that in common.
I marked p6 as distanceToShoot as if you think of GTA's Logic with the native SET_VEHICLE_SHOOT natives, it won't shoot till it gets within a certain distance of the target.
I marked p7 as pedAccuracy as it seems it's mostly 100 (Completely Accurate), 75, 90, etc. Although this could be the ammo count within the gun, but I highly doubt it. I will change this comment once I find out if it's ammo count or not.
```

**This is the server-side RPC native equivalent of the client native [TASK_DRIVE_BY](#taskdriveby).**

---
### TaskEnterVehicle

`TASK_ENTER_VEHICLE` · hash `0xB8689B4E` · **Servidor**

```lua
TaskEnterVehicle(ped, vehicle, timeout, seatIndex, speed, flag, p6)
```
```c
void TASK_ENTER_VEHICLE(Ped ped, Vehicle vehicle, int timeout, int seatIndex, float speed, int flag, Any p6);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `timeout` (`int`)
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](../gta5/VEHICLE-1.md#isvehicleseatfree).
- `speed` (`float`)
- `flag` (`int`)
- `p6` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
speed 1.0 = walk, 2.0 = run
p5 1 = normal, 3 = teleport to vehicle, 8 = normal/carjack ped from seat, 16 = teleport directly into vehicle
p6 is always 0
```

**This is the server-side RPC native equivalent of the client native [TASK_ENTER_VEHICLE](#taskentervehicle).**

---
### TaskEveryoneLeaveVehicle

`TASK_EVERYONE_LEAVE_VEHICLE` · hash `0xC1971F30` · **Servidor**

```lua
TaskEveryoneLeaveVehicle(vehicle)
```
```c
void TASK_EVERYONE_LEAVE_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

TASK_EVERYONE_LEAVE_VEHICLE

**This is the server-side RPC native equivalent of the client native [TASK_EVERYONE_LEAVE_VEHICLE](#taskeveryoneleavevehicle).**

---
### TaskGoStraightToCoord

`TASK_GO_STRAIGHT_TO_COORD` · hash `0x80A9E7A7` · **Servidor**

```lua
TaskGoStraightToCoord(ped, x, y, z, speed, timeout, targetHeading, distanceToSlide)
```
```c
void TASK_GO_STRAIGHT_TO_COORD(Ped ped, float x, float y, float z, float speed, int timeout, float targetHeading, float distanceToSlide);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `x` (`float`): The x coordinate.
- `y` (`float`): The y coordinate.
- `z` (`float`): The z coordinate.
- `speed` (`float`): The ped movement speed.
- `timeout` (`int`): \-1 , other values appear to break the ped movement.
- `targetHeading` (`float`): The heading you want the ped to be on x,y,z coord.
- `distanceToSlide` (`float`): The distance from x,y,z where the ped will start sliding.

**Devuelve:** `void`

**Descripción oficial:**

TASK_GO_STRAIGHT_TO_COORD

**This is the server-side RPC native equivalent of the client native [TASK_GO_STRAIGHT_TO_COORD](#taskgostraighttocoord).**

---
### TaskGoToCoordAnyMeans

`TASK_GO_TO_COORD_ANY_MEANS` · hash `0xF91DF93B` · **Servidor**

```lua
TaskGoToCoordAnyMeans(ped, x, y, z, fMoveBlendRatio, vehicle, bUseLongRangeVehiclePathing, drivingFlags, fMaxRangeToShootTargets)
```
```c
void TASK_GO_TO_COORD_ANY_MEANS(Ped ped, float x, float y, float z, float fMoveBlendRatio, Vehicle vehicle, BOOL bUseLongRangeVehiclePathing, int drivingFlags, float fMaxRangeToShootTargets);
```

**Parámetros**

- `ped` (`Ped`): The `Ped` Handle.
- `x` (`float`): The goto target coordinate.
- `y` (`float`): The goto target coordinate.
- `z` (`float`): The goto target coordinate.
- `fMoveBlendRatio` (`float`): 0.0 = still, 1.0 = walk, 2.0 = run, 3.0 = sprint.
- `vehicle` (`Vehicle`): If defined, the pedestrian will only move if said vehicle exists. If you don't want any sort of association, just set it to `0`.
- `bUseLongRangeVehiclePathing` (`BOOL`): Setting to `true` tells the vehicle to use longrange vehicle pathing.
- `drivingFlags` (`int`): See `eDrivingMode` enum.
- `fMaxRangeToShootTargets` (`float`): Determines the maximum distance at which the `Ped` will engage in combat with threatening targets.

**Devuelve:** `void`

**Descripción oficial:**

Tells a ped to go to a coord by any means.

```cpp
enum eDrivingMode {
DF_StopForCars = 1,
DF_StopForPeds = 2,
DF_SwerveAroundAllCars = 4,
DF_SteerAroundStationaryCars = 8,
DF_SteerAroundPeds = 16,
DF_SteerAroundObjects = 32,
DF_DontSteerAroundPlayerPed = 64,
DF_StopAtLights = 128,
DF_GoOffRoadWhenAvoiding = 256,
DF_DriveIntoOncomingTraffic = 512,
DF_DriveInReverse = 1024,
// If pathfinding fails, cruise randomly instead of going on a straight line
DF_UseWanderFallbackInsteadOfStraightLine = 2048,
DF_AvoidRestrictedAreas = 4096,
// These only work on MISSION_CRUISE
DF_PreventBackgroundPathfinding = 8192,
DF_AdjustCruiseSpeedBasedOnRoadSpeed = 16384,
DF_UseShortCutLinks =  262144,
DF_ChangeLanesAroundObstructions = 524288,
// cruise tasks ignore this anyway--only used for goto's
DF_UseSwitchedOffNodes =  2097152,
// if you're going to be primarily driving off road
DF_PreferNavmeshRoute =  4194304,
// Only works for planes using MISSION_GOTO, will cause them to drive along the ground instead of fly
DF_PlaneTaxiMode =  8388608,
DF_ForceStraightLine = 16777216,
DF_UseStringPullingAtJunctions = 33554432,
DF_AvoidHighways = 536870912,
DF_ForceJoinInRoadDirection = 1073741824,
// Standard driving mode. stops for cars, peds, and lights, goes around stationary obstructions
DRIVINGMODE_STOPFORCARS = 786603, // DF_StopForCars|DF_StopForPeds|DF_SteerAroundObjects|DF_SteerAroundStationaryCars|DF_StopAtLights|DF_UseShortCutLinks|DF_ChangeLanesAroundObstructions,		// Obey lights too
// Like the above, but doesn't steer around anything in its way - will only wait instead.
DRIVINGMODE_STOPFORCARS_STRICT = 262275, // DF_StopForCars|DF_StopForPeds|DF_StopAtLights|DF_UseShortCutLinks, // Doesn't deviate an inch.
// Default "alerted" driving mode. drives around everything, doesn't obey lights
DRIVINGMODE_AVOIDCARS = 786469, // DF_SwerveAroundAllCars|DF_SteerAroundObjects|DF_UseShortCutLinks|DF_ChangeLanesAroundObstructions|DF_StopForCars,
// Very erratic driving. difference between this and AvoidCars is that it doesn't use the brakes at ALL to help with steering
DRIVINGMODE_AVOIDCARS_RECKLESS = 786468, // DF_SwerveAroundAllCars|DF_SteerAroundObjects|DF_UseShortCutLinks|DF_ChangeLanesAroundObstructions,
// Smashes through everything
DRIVINGMODE_PLOUGHTHROUGH = 262144, // DF_UseShortCutLinks
// Drives normally except for the fact that it ignores lights
DRIVINGMODE_STOPFORCARS_IGNORELIGHTS = 786475, // DF_StopForCars|DF_SteerAroundStationaryCars|DF_StopForPeds|DF_SteerAroundObjects|DF_UseShortCutLinks|DF_ChangeLanesAroundObstructions
// Try to swerve around everything, but stop for lights if necessary
DRIVINGMODE_AVOIDCARS_OBEYLIGHTS = 786597, // DF_SwerveAroundAllCars|DF_StopAtLights|DF_SteerAroundObjects|DF_UseShortCutLinks|DF_ChangeLanesAroundObstructions|DF_StopForCars
// Swerve around cars, be careful around peds, and stop for lights
DRIVINGMODE_AVOIDCARS_STOPFORPEDS_OBEYLIGHTS = 786599 // DF_SwerveAroundAllCars|DF_StopAtLights|DF_StopForPeds|DF_SteerAroundObjects|DF_UseShortCutLinks|DF_ChangeLanesAroundObstructions|DF_StopForCars
};
```

**This is the server-side RPC native equivalent of the client native [TASK_GO_TO_COORD_ANY_MEANS](#taskgotocoordanymeans).**

---
### TaskGoToEntity

`TASK_GO_TO_ENTITY` · hash `0x374827C2` · **Servidor**

```lua
TaskGoToEntity(entity, target, duration, distance, speed, p5, p6)
```
```c
void TASK_GO_TO_ENTITY(Entity entity, Entity target, int duration, float distance, float speed, float p5, int p6);
```

**Parámetros**

- `entity` (`Entity`)
- `target` (`Entity`)
- `duration` (`int`)
- `distance` (`float`)
- `speed` (`float`)
- `p5` (`float`)
- `p6` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
The entity will move towards the target until time is over (duration) or get in target's range (distance). p5 and p6 are unknown, but you could leave p5 = 1073741824 or 100 or even 0 (didn't see any difference but on the decompiled scripts, they use 1073741824 mostly) and p6 = 0
Note: I've only tested it on entity -> ped and target -> vehicle. It could work differently on other entities, didn't try it yet.
Example: TASK::TASK_GO_TO_ENTITY(pedHandle, vehicleHandle, 5000, 4.0, 100, 1073741824, 0)
Ped will run towards the vehicle for 5 seconds and stop when time is over or when he gets 4 meters(?) around the vehicle (with duration = -1, the task duration will be ignored).
```

**This is the server-side RPC native equivalent of the client native [TASK_GO_TO_ENTITY](#taskgotoentity).**

---
### TaskHandsUp

`TASK_HANDS_UP` · hash `0x8DCC19C5` · **Servidor**

```lua
TaskHandsUp(ped, duration, facingPed, p3, p4)
```
```c
void TASK_HANDS_UP(Ped ped, int duration, Ped facingPed, int p3, BOOL p4);
```

**Parámetros**

- `ped` (`Ped`)
- `duration` (`int`)
- `facingPed` (`Ped`)
- `p3` (`int`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
In the scripts, p3 was always -1.
p3 seems to be duration or timeout of turn animation.
Also facingPed can be 0 or -1 so ped will just raise hands up.
```

**This is the server-side RPC native equivalent of the client native [TASK_HANDS_UP](#taskhandsup).**

---
### TaskLeaveAnyVehicle

`TASK_LEAVE_ANY_VEHICLE` · hash `0xDBDD79FA` · **Servidor**

```lua
TaskLeaveAnyVehicle(ped, p1, flags)
```
```c
void TASK_LEAVE_ANY_VEHICLE(Ped ped, int p1, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Flags are the same flags used in [`TASK_LEAVE_VEHICLE`](#taskleavevehicle)

**This is the server-side RPC native equivalent of the client native [TASK_LEAVE_ANY_VEHICLE](#taskleaveanyvehicle).**

---
### TaskLeaveVehicle

`TASK_LEAVE_VEHICLE` · hash `0x7B1141C6` · **Servidor**

```lua
TaskLeaveVehicle(ped, vehicle, flags)
```
```c
void TASK_LEAVE_VEHICLE(Ped ped, Vehicle vehicle, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Flags from decompiled scripts:
0 = normal exit and closes door.
1 = normal exit and closes door.
16 = teleports outside, door kept closed.  (This flag does not seem to work for the front seats in buses, NPCs continue to exit normally)
64 = normal exit and closes door, maybe a bit slower animation than 0.
256 = normal exit but does not close the door.
4160 = ped is throwing himself out, even when the vehicle is still.
262144 = ped moves to passenger seat first, then exits normally
Others to be tried out: 320, 512, 131072.
```

**This is the server-side RPC native equivalent of the client native [TASK_LEAVE_VEHICLE](#taskleavevehicle).**

---
### TaskPlayAnim

`TASK_PLAY_ANIM` · hash `0x5AB552C6` · **Servidor**

```lua
TaskPlayAnim(ped, animDictionary, animationName, blendInSpeed, blendOutSpeed, duration, flag, playbackRate, lockX, lockY, lockZ)
```
```c
void TASK_PLAY_ANIM(Ped ped, char* animDictionary, char* animationName, float blendInSpeed, float blendOutSpeed, int duration, int flag, float playbackRate, BOOL lockX, BOOL lockY, BOOL lockZ);
```

**Parámetros**

- `ped` (`Ped`): The ped you want to play the animation
- `animDictionary` (`char*`): The animation dictionary
- `animationName` (`char*`): The animation name
- `blendInSpeed` (`float`): The speed at which the animation blends in. Lower is slower and higher is faster, 1.0 is normal, 8.0 is basically instant
- `blendOutSpeed` (`float`): The speed at which the animation blends out. Lower is slower and higher is faster, 1.0 is normal, 8.0 is basically instant
- `duration` (`int`): The duration of the animation in milliseconds. -1 will play the animation until canceled
- `flag` (`int`): The animation flags (see enum)
- `playbackRate` (`float`): The playback rate (between 0.0 and 1.0)
- `lockX` (`BOOL`)
- `lockY` (`BOOL`)
- `lockZ` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

```cpp
enum eScriptedAnimFlags
{
AF_LOOPING = 1,
AF_HOLD_LAST_FRAME = 2,
AF_REPOSITION_WHEN_FINISHED = 4,
AF_NOT_INTERRUPTABLE = 8,
AF_UPPERBODY = 16,
AF_SECONDARY = 32,
AF_REORIENT_WHEN_FINISHED = 64,
AF_ABORT_ON_PED_MOVEMENT = 128,
AF_ADDITIVE = 256,
AF_TURN_OFF_COLLISION = 512,
AF_OVERRIDE_PHYSICS = 1024,
AF_IGNORE_GRAVITY = 2048,
AF_EXTRACT_INITIAL_OFFSET = 4096,
AF_EXIT_AFTER_INTERRUPTED = 8192,
AF_TAG_SYNC_IN = 16384,
AF_TAG_SYNC_OUT = 32768,
AF_TAG_SYNC_CONTINUOUS = 65536,
AF_FORCE_START = 131072,
AF_USE_KINEMATIC_PHYSICS = 262144,
AF_USE_MOVER_EXTRACTION = 524288,
AF_HIDE_WEAPON = 1048576,
AF_ENDS_IN_DEAD_POSE = 2097152,
AF_ACTIVATE_RAGDOLL_ON_COLLISION = 4194304,
AF_DONT_EXIT_ON_DEATH = 8388608,
AF_ABORT_ON_WEAPON_DAMAGE = 16777216,
AF_DISABLE_FORCED_PHYSICS_UPDATE = 33554432,
AF_PROCESS_ATTACHMENTS_ON_START = 67108864,
AF_EXPAND_PED_CAPSULE_FROM_SKELETON = 134217728,
AF_USE_ALTERNATIVE_FP_ANIM = 268435456,
AF_BLENDOUT_WRT_LAST_FRAME = 536870912,
AF_USE_FULL_BLENDING = 1073741824
}
```

**This is the server-side RPC native equivalent of the client native [TASK_PLAY_ANIM](#taskplayanim).**

---
### TaskPlayAnimAdvanced

`TASK_PLAY_ANIM_ADVANCED` · hash `0x3DDEB0E6` · **Servidor**

```lua
TaskPlayAnimAdvanced(ped, animDictionary, animationName, posX, posY, posZ, rotX, rotY, rotZ, blendInSpeed, blendOutSpeed, duration, flag, animTime, p14, p15)
```
```c
void TASK_PLAY_ANIM_ADVANCED(Ped ped, char* animDictionary, char* animationName, float posX, float posY, float posZ, float rotX, float rotY, float rotZ, float blendInSpeed, float blendOutSpeed, int duration, Any flag, float animTime, Any p14, Any p15);
```

**Parámetros**

- `ped` (`Ped`): The ped you want to play the animation
- `animDictionary` (`char*`): The animation dictionary
- `animationName` (`char*`): The animation name
- `posX` (`float`): Initial X position of the task
- `posY` (`float`): Initial Y position of the task
- `posZ` (`float`): Initial Z position of the task
- `rotX` (`float`): Initial X rotation of the task
- `rotY` (`float`): Initial Y rotation of the task
- `rotZ` (`float`): Initial Z rotation of the task
- `blendInSpeed` (`float`): The speed at which the animation blends in. Lower is slower and higher is faster, 1.0 is normal, 8.0 is basically instant
- `blendOutSpeed` (`float`): The speed at which the animation blends out. Lower is slower and higher is faster, 1.0 is normal, 8.0 is basically instant
- `duration` (`int`): The duration of the animation in milliseconds. -1 will play the animation until canceled
- `flag` (`Any`): See [`TASK_PLAY_ANIM`](#taskplayanim)
- `animTime` (`float`): Value between 0.0 and 1.0, lets you start an animation from the given point
- `p14` (`Any`)
- `p15` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

Similar in functionality to [`TASK_PLAY_ANIM`](#taskplayanim), except the position and rotation parameters let you specify the initial position and rotation of the task. The ped is teleported to the position specified.
[Animations list](https://alexguirre.github.io/animations-list/)

**This is the server-side RPC native equivalent of the client native [TASK_PLAY_ANIM_ADVANCED](#taskplayanimadvanced).**

---
### TaskReactAndFleePed

`TASK_REACT_AND_FLEE_PED` · hash `0x8A632BD8` · **Servidor**

```lua
TaskReactAndFleePed(ped, fleeTarget)
```
```c
void TASK_REACT_AND_FLEE_PED(Ped ped, Ped fleeTarget);
```

**Parámetros**

- `ped` (`Ped`)
- `fleeTarget` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

TASK_REACT_AND_FLEE_PED

**This is the server-side RPC native equivalent of the client native [TASK_REACT_AND_FLEE_PED](#taskreactandfleeped).**

---
### TaskShootAtCoord

`TASK_SHOOT_AT_COORD` · hash `0x601C22E3` · **Servidor**

```lua
TaskShootAtCoord(ped, x, y, z, duration, firingPattern)
```
```c
void TASK_SHOOT_AT_COORD(Ped ped, float x, float y, float z, int duration, Hash firingPattern);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `duration` (`int`)
- `firingPattern` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Firing Pattern Hash Information: https://pastebin.com/Px036isB
```

**This is the server-side RPC native equivalent of the client native [TASK_SHOOT_AT_COORD](#taskshootatcoord).**

---
### TaskShootAtEntity

`TASK_SHOOT_AT_ENTITY` · hash `0xAC0631C9` · **Servidor**

```lua
TaskShootAtEntity(entity, target, duration, firingPattern)
```
```c
void TASK_SHOOT_AT_ENTITY(Entity entity, Entity target, int duration, Hash firingPattern);
```

**Parámetros**

- `entity` (`Entity`)
- `target` (`Entity`)
- `duration` (`int`)
- `firingPattern` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
//this part of the code is to determine at which entity the player is aiming, for example if you want to create a mod where you give orders to peds
Entity aimedentity;
Player player = PLAYER::PLAYER_ID();
PLAYER::_GET_AIMED_ENTITY(player, &aimedentity);
//bg is an array of peds
TASK::TASK_SHOOT_AT_ENTITY(bg[i], aimedentity, 5000, MISC::GET_HASH_KEY("FIRING_PATTERN_FULL_AUTO"));
in practical usage, getting the entity the player is aiming at and then task the peds to shoot at the entity, at a button press event would be better.
Firing Pattern Hash Information: https://pastebin.com/Px036isB
```

**This is the server-side RPC native equivalent of the client native [TASK_SHOOT_AT_ENTITY](#taskshootatentity).**

---
### TaskWarpPedIntoVehicle

`TASK_WARP_PED_INTO_VEHICLE` · hash `0x65D4A35D` · **Servidor**

```lua
TaskWarpPedIntoVehicle(ped, vehicle, seatIndex)
```
```c
void TASK_WARP_PED_INTO_VEHICLE(Ped ped, Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `ped` (`Ped`): The Ped to be warped into the vehicle.
- `vehicle` (`Vehicle`): The target vehicle into which the ped will be warped.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](../gta5/VEHICLE-1.md#isvehicleseatfree).

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

Warp a ped into a vehicle.
**Note**: It's better to use [`TASK_ENTER_VEHICLE`](#taskentervehicle) with the flag "warp" flag instead of this native.

**This is the server-side RPC native equivalent of the client native [TASK_WARP_PED_INTO_VEHICLE](#taskwarppedintovehicle).**

---
### TempBanPlayer

`TEMP_BAN_PLAYER` · hash `0x1E35DBBA` · **Servidor**

```lua
TempBanPlayer(playerSrc, reason)
```
```c
void TEMP_BAN_PLAYER(char* playerSrc, char* reason);
```

**Parámetros**

- `playerSrc` (`char*`)
- `reason` (`char*`)

**Devuelve:** `void`

---
### TriggerClientEventInternal

`TRIGGER_CLIENT_EVENT_INTERNAL` · hash `0x2F7A49E6` · **Servidor**

```lua
TriggerClientEventInternal(eventName, eventTarget, eventPayload, payloadLength)
```
```c
void TRIGGER_CLIENT_EVENT_INTERNAL(char* eventName, char* eventTarget, char* eventPayload, int payloadLength);
```

**Parámetros**

- `eventName` (`char*`)
- `eventTarget` (`char*`)
- `eventPayload` (`char*`)
- `payloadLength` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

The backing function for TriggerClientEvent.

---
### TriggerLatentClientEventInternal

`TRIGGER_LATENT_CLIENT_EVENT_INTERNAL` · hash `0x70B35890` · **Servidor**

```lua
TriggerLatentClientEventInternal(eventName, eventTarget, eventPayload, payloadLength, bps)
```
```c
void TRIGGER_LATENT_CLIENT_EVENT_INTERNAL(char* eventName, char* eventTarget, char* eventPayload, int payloadLength, int bps);
```

**Parámetros**

- `eventName` (`char*`)
- `eventTarget` (`char*`)
- `eventPayload` (`char*`)
- `payloadLength` (`int`)
- `bps` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

The backing function for TriggerLatentClientEvent.

---
### VerifyPasswordHash

`VERIFY_PASSWORD_HASH` · hash `0x2E310ACD` · **Servidor**

```lua
local retval = VerifyPasswordHash(password, hash)
```
```c
BOOL VERIFY_PASSWORD_HASH(char* password, char* hash);
```

**Parámetros**

- `password` (`char*`)
- `hash` (`char*`)

**Devuelve:** `BOOL`

---
