# Natives de GTA V — VEHICLE (parte 2 de 2: SetNumberOfParkedVehicles … UnpausePlaybackRecordedVehicle)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `VEHICLE`: **751** natives.

Partes: [1](VEHICLE-1.md) · **[2]**

[← Índice de natives](../README.md)

## Índice de esta página

[`SetNumberOfParkedVehicles`](#setnumberofparkedvehicles) · [`SetOpenRearDoorsOnExplosion`](#setopenreardoorsonexplosion) · [`SetOppressorTransformState`](#setoppressortransformstate) · [`SetOverrideNitrousLevel`](#setoverridenitrouslevel) · [`SetParkedVehicleDensityMultiplierThisFrame`](#setparkedvehicledensitymultiplierthisframe) · [`SetPickupRopeLengthForCargobob`](#setpickupropelengthforcargobob) · [`SetPlaneAvoidsOthers`](#setplaneavoidsothers) · [`SetPlaneControlSectionsShouldBreakOffFromExplosions`](#setplanecontrolsectionsshouldbreakofffromexplosions) · [`SetPlaneEngineHealth`](#setplaneenginehealth) · [`SetPlanePropellersHealth`](#setplanepropellershealth) · [`SetPlaneResistToExplosion`](#setplaneresisttoexplosion) · [`SetPlaneSectionDamageScale`](#setplanesectiondamagescale) · [`SetPlaneTurbulenceMultiplier`](#setplaneturbulencemultiplier) · [`SetPlaybackSpeed`](#setplaybackspeed) · [`SetPlaybackToUseAi`](#setplaybacktouseai) · [`SetPlaybackToUseAiTryToRevertBackLater`](#setplaybacktouseaitrytorevertbacklater) · [`SetPlayersLastVehicle`](#setplayerslastvehicle) · [`SetPoliceFocusWillTrackVehicle`](#setpolicefocuswilltrackvehicle) · [`SetRandomBoats`](#setrandomboats) · [`SetRandomBoatsInMp`](#setrandomboatsinmp) · [`SetRandomTrains`](#setrandomtrains) · [`SetRandomVehicleDensityMultiplierThisFrame`](#setrandomvehicledensitymultiplierthisframe) · [`SetReduceDriftVehicleSuspension`](#setreducedriftvehiclesuspension) · [`SetRenderTrainAsDerailed`](#setrendertrainasderailed) · [`SetScriptVehicleGenerator`](#setscriptvehiclegenerator) · [`SetSpecialFlightModeAllowed`](#setspecialflightmodeallowed) · [`SetSpecialFlightModeRatio`](#setspecialflightmoderatio) · [`SetSpecialFlightModeTargetRatio`](#setspecialflightmodetargetratio) · [`SetSubmarineCrushDepths`](#setsubmarinecrushdepths) · [`SetTaskVehicleGotoPlaneMinHeightAboveTerrain`](#settaskvehiclegotoplaneminheightaboveterrain) · [`SetTaxiLights`](#settaxilights) · [`SetTrailerAttachmentEnabled`](#settrailerattachmentenabled) · [`SetTrailerInverseMassScale`](#settrailerinversemassscale) · [`SetTrailerLegsLowered`](#settrailerlegslowered) · [`SetTrailerLegsRaised`](#settrailerlegsraised) · [`SetTrainCruiseSpeed`](#settraincruisespeed) · [`SetTrainSpeed`](#settrainspeed) · [`SetTrainTrackSpawnFrequency`](#settraintrackspawnfrequency) · [`SetTransformRateForAnimation`](#settransformrateforanimation) · [`SetTransformToSubmarineUsesAlternateInput`](#settransformtosubmarineusesalternateinput) · [`SetTyreHealth`](#settyrehealth) · [`SetTyreSoftnessMultiplier`](#settyresoftnessmultiplier) · [`SetTyreTractionLossMultiplier`](#settyretractionlossmultiplier) · [`SetTyreWearMultiplier`](#settyrewearmultiplier) · [`SetUseHigherVehicleJumpForce`](#setusehighervehiclejumpforce) · [`SetVehicleActAsIfHighSpeedForFragSmashing`](#setvehicleactasifhighspeedforfragsmashing) · [`SetVehicleActiveDuringPlayback`](#setvehicleactiveduringplayback) · [`SetVehicleActiveForPedNavigation`](#setvehicleactiveforpednavigation) · [`SetVehicleAlarm`](#setvehiclealarm) · [`SetVehicleAllowHomingMissleLockon`](#setvehicleallowhomingmisslelockon) · [`SetVehicleAllowNoPassengersLockon`](#setvehicleallownopassengerslockon) · [`SetVehicleAutomaticallyAttaches`](#setvehicleautomaticallyattaches) · [`SetVehicleBodyHealth`](#setvehiclebodyhealth) · [`SetVehicleBombCount`](#setvehiclebombcount) · [`SetVehicleBrake`](#setvehiclebrake) · [`SetVehicleBrakeLights`](#setvehiclebrakelights) · [`SetVehicleBulldozerArmPosition`](#setvehiclebulldozerarmposition) · [`SetVehicleBurnout`](#setvehicleburnout) · [`SetVehicleCanBeLockedOn`](#setvehiclecanbelockedon) · [`SetVehicleCanBeTargetted`](#setvehiclecanbetargetted) · [`SetVehicleCanBeUsedByFleeingPeds`](#setvehiclecanbeusedbyfleeingpeds) · [`SetVehicleCanBeVisiblyDamaged`](#setvehiclecanbevisiblydamaged) · [`SetVehicleCanBreak`](#setvehiclecanbreak) · [`SetVehicleCanDeformWheels`](#setvehiclecandeformwheels) · [`SetVehicleCanEngineOperateOnFire`](#setvehiclecanengineoperateonfire) · [`SetVehicleCanLeakOil`](#setvehiclecanleakoil) · [`SetVehicleCanLeakPetrol`](#setvehiclecanleakpetrol) · [`SetVehicleCanSaveInGarage`](#setvehiclecansaveingarage) · [`SetVehicleCeilingHeight`](#setvehicleceilingheight) · [`SetVehicleCheatPowerIncrease`](#setvehiclecheatpowerincrease) · [`SetVehicleColourCombination`](#setvehiclecolourcombination) · [`SetVehicleColours`](#setvehiclecolours) · [`SetVehicleControlsInverted`](#setvehiclecontrolsinverted) · [`SetVehicleCountermeasureCount`](#setvehiclecountermeasurecount) · [`SetVehicleCustomPrimaryColour`](#setvehiclecustomprimarycolour) · [`SetVehicleCustomSecondaryColour`](#setvehiclecustomsecondarycolour) · [`SetVehicleDamage`](#setvehicledamage) · [`SetVehicleDamageModifier`](#setvehicledamagemodifier) · [`SetVehicleDashboardColor`](#setvehicledashboardcolor) · [`SetVehicleDeformationFixed`](#setvehicledeformationfixed) · [`SetVehicleDensityMultiplierThisFrame`](#setvehicledensitymultiplierthisframe) · [`SetVehicleDirtLevel`](#setvehicledirtlevel) · [`SetVehicleDisableTowing`](#setvehicledisabletowing) · [`SetVehicleDoorBroken`](#setvehicledoorbroken) · [`SetVehicleDoorCanBreak`](#setvehicledoorcanbreak) · [`SetVehicleDoorControl`](#setvehicledoorcontrol) · [`SetVehicleDoorLatched`](#setvehicledoorlatched) · [`SetVehicleDoorOpen`](#setvehicledooropen) · [`SetVehicleDoorShut`](#setvehicledoorshut) · [`SetVehicleDoorsLocked`](#setvehicledoorslocked) · [`SetVehicleDoorsLockedForAllPlayers`](#setvehicledoorslockedforallplayers) · [`SetVehicleDoorsLockedForNonScriptPlayers`](#setvehicledoorslockedfornonscriptplayers) · [`SetVehicleDoorsLockedForPlayer`](#setvehicledoorslockedforplayer) · [`SetVehicleDoorsLockedForTeam`](#setvehicledoorslockedforteam) · [`SetVehicleDoorsLockedForUnk`](#setvehicledoorslockedforunk) · [`SetVehicleDoorsShut`](#setvehicledoorsshut) · [`SetVehicleDropsMoneyWhenBlownUp`](#setvehicledropsmoneywhenblownup) · [`SetVehicleEngineCanDegrade`](#setvehicleenginecandegrade) · [`SetVehicleEngineHealth`](#setvehicleenginehealth) · [`SetVehicleEngineOn`](#setvehicleengineon) · [`SetVehicleEnveffScale`](#setvehicleenveffscale) · [`SetVehicleExclusiveDriver`](#setvehicleexclusivedriver) · [`SetVehicleExclusiveDriver_2`](#setvehicleexclusivedriver_2) · [`SetVehicleExplodesOnHighExplosionDamage`](#setvehicleexplodesonhighexplosiondamage) · [`SetVehicleExplosiveDamageScale`](#setvehicleexplosivedamagescale) · [`SetVehicleExtendedRemovalRange`](#setvehicleextendedremovalrange) · [`SetVehicleExtra`](#setvehicleextra) · [`SetVehicleExtraColours`](#setvehicleextracolours) · [`SetVehicleFixed`](#setvehiclefixed) · [`SetVehicleFlightNozzlePosition`](#setvehicleflightnozzleposition) · [`SetVehicleFlightNozzlePositionImmediate`](#setvehicleflightnozzlepositionimmediate) · [`SetVehicleForceAfterburner`](#setvehicleforceafterburner) · [`SetVehicleForwardSpeed`](#setvehicleforwardspeed) · [`SetVehicleFrictionOverride`](#setvehiclefrictionoverride) · [`SetVehicleFullbeam`](#setvehiclefullbeam) · [`SetVehicleGeneratesEngineShockingEvents`](#setvehiclegeneratesengineshockingevents) · [`SetVehicleGeneratorAreaOfInterest`](#setvehiclegeneratorareaofinterest) · [`SetVehicleGravity`](#setvehiclegravity) · [`SetVehicleHandbrake`](#setvehiclehandbrake) · [`SetVehicleHandlingHashForAi`](#setvehiclehandlinghashforai) · [`SetVehicleHasBeenDrivenFlag`](#setvehiclehasbeendrivenflag) · [`SetVehicleHasBeenOwnedByPlayer`](#setvehiclehasbeenownedbyplayer) · [`SetVehicleHasMutedSirens`](#setvehiclehasmutedsirens) · [`SetVehicleHasStrongAxles`](#setvehiclehasstrongaxles) · [`SetVehicleHasUnbreakableLights`](#setvehiclehasunbreakablelights) · [`SetVehicleHeadlightShadows`](#setvehicleheadlightshadows) · [`SetVehicleInactiveDuringPlayback`](#setvehicleinactiveduringplayback) · [`SetVehicleIndicatorLights`](#setvehicleindicatorlights) · [`SetVehicleIndividualDoorsLocked`](#setvehicleindividualdoorslocked) · [`SetVehicleInfluencesWantedLevel`](#setvehicleinfluenceswantedlevel) · [`SetVehicleInteriorColor`](#setvehicleinteriorcolor) · [`SetVehicleInteriorlight`](#setvehicleinteriorlight) · [`SetVehicleIsConsideredByPlayer`](#setvehicleisconsideredbyplayer) · [`SetVehicleIsRacing`](#setvehicleisracing) · [`SetVehicleIsStolen`](#setvehicleisstolen) · [`SetVehicleIsWanted`](#setvehicleiswanted) · [`SetVehicleKeepEngineOnWhenAbandoned`](#setvehiclekeepengineonwhenabandoned) · [`SetVehicleKersAllowed`](#setvehiclekersallowed) · [`SetVehicleLightMultiplier`](#setvehiclelightmultiplier) · [`SetVehicleLights`](#setvehiclelights) · [`SetVehicleLivery`](#setvehiclelivery) · [`SetVehicleLodMultiplier`](#setvehiclelodmultiplier) · [`SetVehicleMaxSpeed`](#setvehiclemaxspeed) · [`SetVehicleMod`](#setvehiclemod) · [`SetVehicleModColor_1`](#setvehiclemodcolor_1) · [`SetVehicleModColor_2`](#setvehiclemodcolor_2) · [`SetVehicleModKit`](#setvehiclemodkit) · [`SetVehicleModelIsSuppressed`](#setvehiclemodelissuppressed) · [`SetVehicleNameDebug`](#setvehiclenamedebug) · [`SetVehicleNeedsToBeHotwired`](#setvehicleneedstobehotwired) · [`SetVehicleNeonLightEnabled`](#setvehicleneonlightenabled) · [`SetVehicleNeonLightsColor_2`](#setvehicleneonlightscolor_2) · [`SetVehicleNeonLightsColour`](#setvehicleneonlightscolour) · [`SetVehicleNumberPlateText`](#setvehiclenumberplatetext) · [`SetVehicleNumberPlateTextIndex`](#setvehiclenumberplatetextindex) · [`SetVehicleOnGroundProperly`](#setvehicleongroundproperly) · [`SetVehicleOutOfControl`](#setvehicleoutofcontrol) · [`SetVehicleParachuteActive`](#setvehicleparachuteactive) · [`SetVehicleParachuteModel`](#setvehicleparachutemodel) · [`SetVehicleParachuteTextureVariation`](#setvehicleparachutetexturevariation) · [`SetVehiclePetrolTankHealth`](#setvehiclepetroltankhealth) · [`SetVehicleProvidesCover`](#setvehicleprovidescover) · [`SetVehicleRampLaunchModifier`](#setvehicleramplaunchmodifier) · [`SetVehicleRampSidewaysLaunchMotion`](#setvehiclerampsidewayslaunchmotion) · [`SetVehicleRampUpwardsLaunchMotion`](#setvehiclerampupwardslaunchmotion) · [`SetVehicleReceivesRampDamage`](#setvehiclereceivesrampdamage) · [`SetVehicleReduceGrip`](#setvehiclereducegrip) · [`SetVehicleReduceTraction`](#setvehiclereducetraction) · [`SetVehicleRocketBoostActive`](#setvehiclerocketboostactive) · [`SetVehicleRocketBoostPercentage`](#setvehiclerocketboostpercentage) · [`SetVehicleRocketBoostRefillTime`](#setvehiclerocketboostrefilltime) · [`SetVehicleRoofLivery`](#setvehiclerooflivery) · [`SetVehicleRudderBroken`](#setvehiclerudderbroken) · [`SetVehicleSearchlight`](#setvehiclesearchlight) · [`SetVehicleShadowEffect`](#setvehicleshadoweffect) · [`SetVehicleShootAtTarget`](#setvehicleshootattarget) · [`SetVehicleSilent`](#setvehiclesilent) · [`SetVehicleSiren`](#setvehiclesiren) · [`SetVehicleSt`](#setvehiclest) · [`SetVehicleSteerBias`](#setvehiclesteerbias) · [`SetVehicleSteeringBiasScalar`](#setvehiclesteeringbiasscalar) · [`SetVehicleStrong`](#setvehiclestrong) · [`SetVehicleTankTurretPosition`](#setvehicletankturretposition) · [`SetVehicleTimedExplosion`](#setvehicletimedexplosion) · [`SetVehicleTowTruckArmPosition`](#setvehicletowtruckarmposition) · [`SetVehicleTurretSpeedThisFrame`](#setvehicleturretspeedthisframe) · [`SetVehicleTurretUnk`](#setvehicleturretunk) · [`SetVehicleTyreBurst`](#setvehicletyreburst) · [`SetVehicleTyreFixed`](#setvehicletyrefixed) · [`SetVehicleTyreSmokeColor`](#setvehicletyresmokecolor) · [`SetVehicleTyresCanBurst`](#setvehicletyrescanburst) · [`SetVehicleUndriveable`](#setvehicleundriveable) · [`SetVehicleUnkDamageMultiplier`](#setvehicleunkdamagemultiplier) · [`SetVehicleUseAlternateHandling`](#setvehicleusealternatehandling) · [`SetVehicleUseCutsceneWheelCompression`](#setvehicleusecutscenewheelcompression) · [`SetVehicleUseHornButtonForNitrous`](#setvehicleusehornbuttonfornitrous) · [`SetVehicleUsePlayerLightSettings`](#setvehicleuseplayerlightsettings) · [`SetVehicleUsesLargeRearRamp`](#setvehicleuseslargerearramp) · [`SetVehicleWeaponRestrictedAmmo`](#setvehicleweaponrestrictedammo) · [`SetVehicleWeaponsDisabled`](#setvehicleweaponsdisabled) · [`SetVehicleWheelType`](#setvehiclewheeltype) · [`SetVehicleWheelsCanBreak`](#setvehiclewheelscanbreak) · [`SetVehicleWheelsCanBreakOffWhenBlowUp`](#setvehiclewheelscanbreakoffwhenblowup) · [`SetVehicleWheelsDealDamage`](#setvehiclewheelsdealdamage) · [`SetVehicleWindowTint`](#setvehiclewindowtint) · [`SetVehicleXenonLightsColor`](#setvehiclexenonlightscolor) · [`SkipTimeInPlaybackRecordedVehicle`](#skiptimeinplaybackrecordedvehicle) · [`SkipToEndAndStopPlaybackRecordedVehicle`](#skiptoendandstopplaybackrecordedvehicle) · [`SmashVehicleWindow`](#smashvehiclewindow) · [`StabiliseEntityAttachedToHeli`](#stabiliseentityattachedtoheli) · [`StartPlaybackRecordedVehicle`](#startplaybackrecordedvehicle) · [`StartPlaybackRecordedVehicleUsingAi`](#startplaybackrecordedvehicleusingai) · [`StartPlaybackRecordedVehicleWithFlags`](#startplaybackrecordedvehiclewithflags) · [`StartVehicleAlarm`](#startvehiclealarm) · [`StartVehicleHorn`](#startvehiclehorn) · [`StopAllGarageActivity`](#stopallgarageactivity) · [`StopBringVehicleToHalt`](#stopbringvehicletohalt) · [`StopPlaybackRecordedVehicle`](#stopplaybackrecordedvehicle) · [`SwitchTrainTrack`](#switchtraintrack) · [`ToggleVehicleMod`](#togglevehiclemod) · [`TrackVehicleVisibility`](#trackvehiclevisibility) · [`TransformToCar`](#transformtocar) · [`TransformToSubmarine`](#transformtosubmarine) · [`UnpausePlaybackRecordedVehicle`](#unpauseplaybackrecordedvehicle)

---
### SetNumberOfParkedVehicles

`SET_NUMBER_OF_PARKED_VEHICLES` · hash `0xCAA15F13EBD417FF` · jhash `0x206A58E8` · **Cliente**

```lua
SetNumberOfParkedVehicles(value)
```
```c
void SET_NUMBER_OF_PARKED_VEHICLES(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

---
### SetOpenRearDoorsOnExplosion

`SET_OPEN_REAR_DOORS_ON_EXPLOSION` · hash `0x1B212B26DD3C04DF` · **Cliente**

```lua
SetOpenRearDoorsOnExplosion(vehicle, toggle)
```
```c
void SET_OPEN_REAR_DOORS_ON_EXPLOSION(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to apply this setting to.
- `toggle` (`BOOL`): A boolean value where `true` allows the rear doors to open upon explosion, and `false` prevents them from opening.

**Devuelve:** `void` — This native does not return any value.

**Descripción oficial:**

Enables or disables the opening of a vehicle's rear doors in the event of a sticky bomb explosion. This native is effective for armored vehicles, such as the Stockade (Brinks vehicle), allowing the rear doors to be opened through controlled explosions, which might otherwise remain locked due to the vehicle nature.

**Nombres antiguos (alias):** `0x1B212B26DD3C04DF` (`N_0x1b212b26dd3c04df`)

**Ejemplo (lua):**

```lua
-- This example disables the rear doors of the vehicle from opening upon explosion.

-- Retrieve the LocalPlayer.
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if not DoesEntityExist(vehicle) then 
    -- If the vehicle does not exist, end the execution of the code here.
    return 
end

-- Retrieve the model of the vehicle
local modelVehicle = GetEntityModel(vehicle)

-- Retrieve the hash of the Stockade.
local hashStockade = GetHashKey("stockade")

-- Check if the vehicle is a Stockade.
if (modelVehicle == hashStockade) then
    -- Disable the rear doors from opening upon explosion.
    SetOpenRearDoorsOnExplosion(vehicle, true)
end
```

**Ejemplo (js):**

```js
// This example disables the rear doors of the vehicle from opening upon explosion.

// Retrieve the LocalPlayer.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
  // If the vehicle does not exist, end the execution of the code here.
  return;
}

// Retrieve the model of the vehicle.
const modelVehicle = GetEntityModel(vehicle);

// Retrieve the hash of the Stockade.
const hashStockade = GetHashKey("stockade");

// Check if the vehicle is a Stockade.
if (modelVehicle === hashStockade) {
    // Disable the rear doors from opening upon explosion.
    SetOpenRearDoorsOnExplosion(vehicle, true);
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// This example disables the rear doors of the vehicle from opening upon explosion.

// Retrieve the local ped.
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle))
{
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// Retrieve the model of the vehicle.
uint modelVehicle = (uint)GetEntityModel(vehicle);

// Retrieve the hash of the Stockade.
uint hashStockade = (uint)GetHashKey("stockade");

// Check if the vehicle is a Stockade.
if (modelVehicle == hashStockade) {
    // Disable the rear doors from opening upon explosion.
    SetOpenRearDoorsOnExplosion(vehicle, true);
}
```

---
### SetOppressorTransformState

`_SET_OPPRESSOR_TRANSFORM_STATE` · hash `0x544996C0081ABDEB` · **Cliente**

```lua
SetOppressorTransformState(vehicle, extend)
```
```c
void _SET_OPPRESSOR_TRANSFORM_STATE(Vehicle vehicle, BOOL extend);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle (tested with oppressor only)
- `extend` (`BOOL`): Set to true to extend the wings, false to retract them.

**Devuelve:** `void`

**Descripción oficial:**

Set state to true to extend the wings, false to retract them.

**Nombres antiguos (alias):** `0x544996C0081ABDEB` (`N_0x544996c0081abdeb`)

---
### SetOverrideNitrousLevel

`SET_OVERRIDE_NITROUS_LEVEL` · hash `0xC8E9B6B71B8E660D` · **Cliente**

```lua
SetOverrideNitrousLevel(vehicle, override)
```
```c
void SET_OVERRIDE_NITROUS_LEVEL(Vehicle vehicle, BOOL override);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle whose nitrous system is to be overridden.
- `override` (`BOOL`): A boolean toggle to enable or disable the override settings.

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
NativeDB Added Parameter 2 (2060): float durationMod : A multiplier applied to the default nitrous duration (default is 3 seconds). 
NativeDB Added Parameter 3 (2060): float power : A multiplier applied to the default nitrous power multiplier (default is 3).
NativeDB Added Parameter 4 (2060): float rechargeTime : A multiplier applied to the default nitrous recharge rate.
NativeDB Added Parameter 5 (2060): BOOL disableSound : A boolean to disable the default nitrous sound when the nitrous is active.
```

Overrides the default settings of a vehicle's nitrous system, allowing custom control over its performance characteristics.

**Nombres antiguos (alias):** `_SET_VEHICLE_NITRO_ENABLED` (`SetVehicleNitroEnabled`)

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if vehicle == 0 then return end

-- Configure the vehicle's nitrous system with custom settings for maximum effect.
SetOverrideNitrousLevel(vehicle, true, 100, 100, 99999999999, false);
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Configure the vehicle's nitrous system with custom settings for maximum effect.
SetOverrideNitrousLevel(vehicle, true, 100, 100, 99999999999, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Configure the vehicle's nitrous system with custom settings for maximum effect.
SetOverrideNitrousLevel(vehicle, true, 100, 100, 99999999999, false);
```

---
### SetParkedVehicleDensityMultiplierThisFrame

`SET_PARKED_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME` · hash `0xEAE6DCC7EEE3DB1D` · jhash `0xDD46CEBE` · **Cliente**

```lua
SetParkedVehicleDensityMultiplierThisFrame(multiplier)
```
```c
void SET_PARKED_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

---
### SetPickupRopeLengthForCargobob

`SET_PICKUP_ROPE_LENGTH_FOR_CARGOBOB` · hash `0x877C1EAEAC531023` · jhash `0x3A8AB081` · **Cliente**

```lua
SetPickupRopeLengthForCargobob(cargobob, length1, length2, state)
```
```c
void SET_PICKUP_ROPE_LENGTH_FOR_CARGOBOB(Vehicle cargobob, float length1, float length2, BOOL state);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `length1` (`float`)
- `length2` (`float`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
min: 1.9f, max: 100.0f
```

**Nombres antiguos (alias):** `0x877C1EAEAC531023` (`N_0x877c1eaeac531023`), `_SET_CARGOBOB_HOOK_POSITION` (`SetCargobobHookPosition`)

---
### SetPlaneAvoidsOthers

`_SET_PLANE_AVOIDS_OTHERS` · hash `0xBAFB99B304BC52A7` · **Cliente**

```lua
SetPlaneAvoidsOthers(plane, toggle)
```
```c
void _SET_PLANE_AVOIDS_OTHERS(Vehicle plane, BOOL toggle);
```

**Parámetros**

- `plane` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### SetPlaneControlSectionsShouldBreakOffFromExplosions

`SET_PLANE_CONTROL_SECTIONS_SHOULD_BREAK_OFF_FROM_EXPLOSIONS` · hash `0xDD8A2D3337F04196` · **Cliente**

```lua
SetPlaneControlSectionsShouldBreakOffFromExplosions(plane, toggle)
```
```c
void SET_PLANE_CONTROL_SECTIONS_SHOULD_BREAK_OFF_FROM_EXPLOSIONS(Vehicle plane, BOOL toggle);
```

**Parámetros**

- `plane` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### SetPlaneEngineHealth

`_SET_PLANE_ENGINE_HEALTH` · hash `0x2A86A0475B6A1434` · **Cliente**

```lua
SetPlaneEngineHealth(vehicle, health)
```
```c
void _SET_PLANE_ENGINE_HEALTH(Vehicle vehicle, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `health` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Works just like SET_VEHICLE_ENGINE_HEALTH, didn't saw any difference. But this native works only for planes.
```

**Nombres antiguos (alias):** `0x2A86A0475B6A1434` (`N_0x2a86a0475b6a1434`)

---
### SetPlanePropellersHealth

`_SET_PLANE_PROPELLERS_HEALTH` · hash `0x4C815EB175086F84` · **Cliente**

```lua
SetPlanePropellersHealth(plane, health)
```
```c
void _SET_PLANE_PROPELLERS_HEALTH(Vehicle plane, float health);
```

**Parámetros**

- `plane` (`Vehicle`)
- `health` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4C815EB175086F84` (`N_0x4c815eb175086f84`)

---
### SetPlaneResistToExplosion

`SET_PLANE_RESIST_TO_EXPLOSION` · hash `0xE16142B94664DEFD` · jhash `0xFBBA699A` · **Cliente**

```lua
SetPlaneResistToExplosion(vehicle, toggle)
```
```c
void SET_PLANE_RESIST_TO_EXPLOSION(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE16142B94664DEFD` (`N_0xe16142b94664defd`)

---
### SetPlaneSectionDamageScale

`SET_PLANE_SECTION_DAMAGE_SCALE` · hash `0x0BBB9A7A8FFE931B` · **Cliente**

```lua
SetPlaneSectionDamageScale(vehicle, damageSection, damageScale)
```
```c
void SET_PLANE_SECTION_DAMAGE_SCALE(Vehicle vehicle, int damageSection, float damageScale);
```

**Parámetros**

- `vehicle` (`Vehicle`): Plane to which the damage scale adjustment will be applied.
- `damageSection` (`int`): Specific section of the plane, as defined in the `ePlaneDamageSection` enum, where the damage scale will be adjusted.
- `damageScale` (`float`): A float value representing the scale of damage to be applied to the specified section.

**Devuelve:** `void` — This native does not return any value.

**Descripción oficial:**

Adjusts the scale of damage applied to a specified section of a plane.
In the decompiled scripts the `damageScale` is always set to `0f` (maybe to disable damages on the specified section)

```cpp
enum ePlaneDamageSection {
    WING_L = 0,
    WING_R = 1,
    TAIL = 2,
    ENGINE_L = 3,
    ENGINE_R = 4,
    ELEVATOR_L = 5,
    ELEVATOR_R = 6,
    AILERON_L = 7,
    AILERON_R = 8,
    RUDDER = 9,
    RUDDER_2 = 10,
    AIRBRAKE_L = 11,
    AIRBRAKE_R = 12
}
```

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x0BBB9A7A8FFE931B` (`N_0x0bbb9a7a8ffe931b`)

---
### SetPlaneTurbulenceMultiplier

`SET_PLANE_TURBULENCE_MULTIPLIER` · hash `0xAD2D28A1AFDFF131` · jhash `0xED159AE6` · **Cliente**

```lua
SetPlaneTurbulenceMultiplier(vehicle, multiplier)
```
```c
void SET_PLANE_TURBULENCE_MULTIPLIER(Vehicle vehicle, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`): The plane to set the multiplier for
- `multiplier` (`float`): The turbulence multiplier. Value between 0.0 and 1.0

**Devuelve:** `void`

**Descripción oficial:**

This native sets the turbulence multiplier. It only works for planes.
0.0 = no turbulence at all.
1.0 = heavy turbulence.

Works by just calling it once, does not need to be called every tick.

**Nombres antiguos (alias):** `0xAD2D28A1AFDFF131` (`N_0xad2d28a1afdff131`)

**Ejemplo (lua):**

```lua
local plane = GetVehiclePedIsIn(PlayerPedId(), false)
if IsThisModelAPlane(GetEntityModel(plane)) then
    -- Goodbye turbulence!
    SetPlaneTurbulenceMultiplier(plane, 0.0)
end
```

---
### SetPlaybackSpeed

`SET_PLAYBACK_SPEED` · hash `0x6683AB880E427778` · jhash `0x684E26E4` · **Cliente**

```lua
SetPlaybackSpeed(vehicle, speed)
```
```c
void SET_PLAYBACK_SPEED(Vehicle vehicle, float speed);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `speed` (`float`)

**Devuelve:** `void`

---
### SetPlaybackToUseAi

`SET_PLAYBACK_TO_USE_AI` · hash `0xA549C3B37EA28131` · jhash `0xB536CCD7` · **Cliente**

```lua
SetPlaybackToUseAi(vehicle, drivingStyle)
```
```c
void SET_PLAYBACK_TO_USE_AI(Vehicle vehicle, int drivingStyle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](TASK.md#setdrivetaskdrivingstyle)).

**Devuelve:** `void`

**Descripción oficial:**

Identical to SET_PLAYBACK_TO_USE_AI_TRY_TO_REVERT_BACK_LATER with 0 as arguments for p1 and p3.

---
### SetPlaybackToUseAiTryToRevertBackLater

`SET_PLAYBACK_TO_USE_AI_TRY_TO_REVERT_BACK_LATER` · hash `0x6E63860BBB190730` · jhash `0x0C8ABAA4` · **Cliente**

```lua
SetPlaybackToUseAiTryToRevertBackLater(vehicle, time, drivingStyle, p3)
```
```c
void SET_PLAYBACK_TO_USE_AI_TRY_TO_REVERT_BACK_LATER(Vehicle vehicle, int time, int drivingStyle, BOOL p3);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `time` (`int`)
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](TASK.md#setdrivetaskdrivingstyle)).
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Time is number of milliseconds before reverting, zero for indefinitely.
```

---
### SetPlayersLastVehicle

`SET_PLAYERS_LAST_VEHICLE` · hash `0xBCDF8BAF56C87B6A` · jhash `0xDE86447D` · **Cliente**

```lua
SetPlayersLastVehicle(vehicle)
```
```c
void SET_PLAYERS_LAST_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### SetPoliceFocusWillTrackVehicle

`SET_POLICE_FOCUS_WILL_TRACK_VEHICLE` · hash `0x4E74E62E0A97E901` · jhash `0x5690F6C3` · **Cliente**

```lua
SetPoliceFocusWillTrackVehicle(vehicle, p1)
```
```c
void SET_POLICE_FOCUS_WILL_TRACK_VEHICLE(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets flag on vehicle that changes behaviour in relation to when player gets wanted level

**Nombres antiguos (alias):** `0x4E74E62E0A97E901` (`N_0x4e74e62e0a97e901`)

---
### SetRandomBoats

`SET_RANDOM_BOATS` · hash `0x84436EC293B1415F` · jhash `0xB505BD89` · **Cliente**

```lua
SetRandomBoats(toggle)
```
```c
void SET_RANDOM_BOATS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetRandomBoatsInMp

`_SET_RANDOM_BOATS_IN_MP` · hash `0xDA5E12F728DB30CA` · **Cliente**

```lua
SetRandomBoatsInMp(toggle)
```
```c
void _SET_RANDOM_BOATS_IN_MP(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### SetRandomTrains

`SET_RANDOM_TRAINS` · hash `0x80D9F74197EA47D9` · jhash `0xD461CA7F` · **Cliente**

```lua
SetRandomTrains(toggle)
```
```c
void SET_RANDOM_TRAINS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Whether to enable random trains.

**Devuelve:** `void`

**Descripción oficial:**

Enables spawning random trains on the preset tracks.

Requires [`SWITCH_TRAIN_TRACK`](#switchtraintrack) and [`SET_TRAIN_TRACK_SPAWN_FREQUENCY`](#settraintrackspawnfrequency) to be set.

**Ejemplo (lua):**

```lua
SwitchTrainTrack(0, true) -- Setting the Main train track(s) around LS and towards Sandy Shores active
SwitchTrainTrack(3, true) -- Setting the Metro tracks active
SetTrainTrackSpawnFrequency(0, 120000) -- The Train spawn frequency set for the game engine
SetTrainTrackSpawnFrequency(3, 120000) -- The Metro spawn frequency set for the game engine
SetRandomTrains(true) -- Telling the game we want to use randomly spawned trains
```

---
### SetRandomVehicleDensityMultiplierThisFrame

`SET_RANDOM_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME` · hash `0xB3B3359379FE77D3` · jhash `0x543F712B` · **Cliente**

```lua
SetRandomVehicleDensityMultiplierThisFrame(multiplier)
```
```c
void SET_RANDOM_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

---
### SetReduceDriftVehicleSuspension

`_SET_REDUCE_DRIFT_VEHICLE_SUSPENSION` · hash `0x3A375167F5782A65` · **Cliente**

```lua
SetReduceDriftVehicleSuspension(vehicle, enable)
```
```c
void _SET_REDUCE_DRIFT_VEHICLE_SUSPENSION(Vehicle vehicle, BOOL enable);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `enable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Lowers the vehicle's stance. Only works for vehicles that support this feature.

```
NativeDB Introduced: v2372
```

---
### SetRenderTrainAsDerailed

`SET_RENDER_TRAIN_AS_DERAILED` · hash `0x317B11A312DF5534` · jhash `0x899D9092` · **Cliente**

```lua
SetRenderTrainAsDerailed(train, toggle)
```
```c
void SET_RENDER_TRAIN_AS_DERAILED(Vehicle train, BOOL toggle);
```

**Parámetros**

- `train` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
makes the train all jumbled up and derailed as it moves on the tracks (though that wont stop it from its normal operations)  
```

---
### SetScriptVehicleGenerator

`SET_SCRIPT_VEHICLE_GENERATOR` · hash `0xD9D620E0AC6DC4B0` · jhash `0x40D73747` · **Cliente**

```lua
SetScriptVehicleGenerator(vehicleGenerator, enabled)
```
```c
void SET_SCRIPT_VEHICLE_GENERATOR(int vehicleGenerator, BOOL enabled);
```

**Parámetros**

- `vehicleGenerator` (`int`)
- `enabled` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only called once in the decompiled scripts. Presumably activates the specified generator.  
```

---
### SetSpecialFlightModeAllowed

`SET_SPECIAL_FLIGHT_MODE_ALLOWED` · hash `0xF1211889DF15A763` · **Cliente**

```lua
SetSpecialFlightModeAllowed(vehicle, toggle)
```
```c
void SET_SPECIAL_FLIGHT_MODE_ALLOWED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to which the locking state will be applied.
- `toggle` (`BOOL`): Boolean parameter where setting `false` locks the current state of the vehicle, preventing transitions such as the `Deluxo` or Oppressor switching between their flying and driving modes. Setting it to `true` allows changing the vehicle state as usual.

**Devuelve:** `void`

**Descripción oficial:**

Allows locking the hover/non-hover mode of a vehicle, such as the flying mode of the `Deluxo`. In the decompiled scripts, this native is used on `oppressor2` but couldn't get it to work on it.

**Nombres antiguos (alias):** `0xF1211889DF15A763` (`N_0xf1211889df15a763`), `_SET_VEHICLE_HOVER_TRANSFORM_ENABLED` (`SetVehicleHoverTransformEnabled`)

**Ejemplo (lua):**

```lua
-- Checks the altitude of the Deluxo and locks its current mode when above 150 meters.
-- If the Deluxo is in flying mode at this altitude, it will be unable to switch to driving mode, and vice versa.
Citizen.CreateThread(function()
    local coords -- Variable to store the vehicle's coordinates.
    local vehicle -- Variable to store the vehicle entity.
    
    repeat
        vehicle = GetVehiclePedIsIn(PlayerPedId(), false) -- Get the vehicle the player is currently in.
        
        if (GetEntityModel(vehicle) == joaat("deluxo")) then -- Check if the vehicle is a Deluxo.
            coords = GetEntityCoords(vehicle) -- Get the current coordinates of the vehicle.
        end
        
        Citizen.Wait(0) -- Wait for the next frame.
        
    until coords.z >= 150.0 -- Keep looping until the Deluxo is above 150 meters.
    
    SetSpecialFlightModeAllowed(vehicle, false) -- Lock the Deluxo's current mode (flying or driving).
end)
```

---
### SetSpecialFlightModeRatio

`SET_SPECIAL_FLIGHT_MODE_RATIO` · hash `0xD138FA15C9776837` · **Cliente**

```lua
SetSpecialFlightModeRatio(vehicle, ratio)
```
```c
void SET_SPECIAL_FLIGHT_MODE_RATIO(Vehicle vehicle, float ratio);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to which the ratio will be applied.
- `ratio` (`float`): A value between 0.0 and 1.0 indicating the target state for the vehicle's hover mode transition. In decompiled scripts, a common usage is 0.75 - GetFrameTime(). Exceeding the maximum can cause the `Deluxo's` wheels to glitch, delaying their return to the initial position.

**Devuelve:** `void`

**Descripción oficial:**

Used alongside [`SET_SPECIAL_FLIGHT_MODE_TARGET_RATIO`](#setspecialflightmodetargetratio), this function initiates hover transformation for vehicles with a hover mode, like the `Deluxo`, based on a specified ratio (0.0 to 1.0). Incorrect values can glitch the vehicle. Without pairing, vehicles revert to car mode. Ineffective on the `oppressor2`

**Nombres antiguos (alias):** `_SET_VEHICLE_HOVER_TRANSFORM_RATIO` (`SetVehicleHoverTransformRatio`)

**Ejemplo (lua):**

```lua
-- In this case we are enabling the hover mode for the vehicle and initiates hover transformation.
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetSpecialFlightModeRatio(vehicle, 0.75 - GetFrameTime())
SetVehicleHoverTransformPercentage(vehicle, 1.0)
```

**Ejemplo (js):**

```js
// In this case we are enabling the hover mode for the vehicle and initiates hover transformation.
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetSpecialFlightModeRatio(vehicle, 0.75 - GetFrameTime());
SetVehicleHoverTransformPercentage(vehicle, 1.0);
```

**Ejemplo (cs):**

```cs
// In this case we are enabling the hover mode for the vehicle and initiates hover transformation.
using static CitizenFX.Core.Native.API;
Vehicle vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetSpecialFlightModeRatio(vehicle, 0.75f - GetFrameTime());
SetVehicleHoverTransformPercentage(vehicle, 1f);
```

---
### SetSpecialFlightModeTargetRatio

`SET_SPECIAL_FLIGHT_MODE_TARGET_RATIO` · hash `0x438B3D7CA026FE91` · **Cliente**

```lua
SetSpecialFlightModeTargetRatio(vehicle, state)
```
```c
void SET_SPECIAL_FLIGHT_MODE_TARGET_RATIO(Vehicle vehicle, float state);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle (a deluxo or oppressor2).
- `state` (`float`): The transform state (value between 0.0 and 1.0).

**Devuelve:** `void`

**Descripción oficial:**

According to decompiled scripts this should work with the `deluxo` and `oppressor2` vehicles.
Does nothing when used on `oppressor2`.

For the deluxo:

*   Set `state` to `0.0`: Fully transform to a 'road' vehicle (non-hover mode).
*   Set `state` to `1.0`: Fully transform to a 'flying' vehicle (hover mode).

If you set it to something like 0.5, then something [weird happens](https://streamable.com/p6wmr), you end up in some 50% hover mode, 50% not hover mode.

This doesn't need to be called every tick, just once and the vehicle will transform to that state at the usual transform speed. It'll just stop transforming when it reaches the state you provided.

Once this native is used then players will just be able to hit the vehicle transform key to toggle the transformation cycle; it won't block users from using the key.

**Nombres antiguos (alias):** `0x438B3D7CA026FE91` (`N_0x438b3d7ca026fe91`), `_SET_VEHICLE_TRANSFORM_STATE` (`SetVehicleTransformState`), `_SET_VEHICLE_HOVER_TRANSFORM_PERCENTAGE` (`SetVehicleHoverTransformPercentage`)

**Ejemplo (lua):**

```lua
-- In this case we are enabling the hover mode for the deluxo (fyling mode)
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetSpecialFlightModeTargetRatio(vehicle, 1.0)
```

**Ejemplo (js):**

```js
// In this case we are enabling the hover mode for the deluxo (fyling mode)
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetSpecialFlightModeTargetRatio(vehicle, 1.0);
```

**Ejemplo (cs):**

```cs
// In this case we are enabling the hover mode for the deluxo (fyling mode)
using static CitizenFX.Core.Native.API;
Vehicle vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetSpecialFlightModeTargetRatio(vehicle, 1f);
```

---
### SetSubmarineCrushDepths

`SET_SUBMARINE_CRUSH_DEPTHS` · hash `0xC59872A5134879C7` · jhash `0x4A46E814` · **Cliente**

```lua
SetSubmarineCrushDepths(vehicle, toggle, depth1, depth2, depth3)
```
```c
void SET_SUBMARINE_CRUSH_DEPTHS(Vehicle vehicle, BOOL toggle, float depth1, float depth2, float depth3);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)
- `depth1` (`float`)
- `depth2` (`float`)
- `depth3` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_JITTER_VEHICLE` (`JitterVehicle`)

---
### SetTaskVehicleGotoPlaneMinHeightAboveTerrain

`SET_TASK_VEHICLE_GOTO_PLANE_MIN_HEIGHT_ABOVE_TERRAIN` · hash `0xB893215D8D4C015B` · jhash `0x8C4B63E2` · **Cliente**

```lua
SetTaskVehicleGotoPlaneMinHeightAboveTerrain(plane, height)
```
```c
void SET_TASK_VEHICLE_GOTO_PLANE_MIN_HEIGHT_ABOVE_TERRAIN(Vehicle plane, int height);
```

**Parámetros**

- `plane` (`Vehicle`)
- `height` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB893215D8D4C015B` (`N_0xb893215d8d4c015b`), `_SET_PLANE_MIN_HEIGHT_ABOVE_GROUND` (`SetPlaneMinHeightAboveGround`), `_SET_PLANE_MIN_HEIGHT_ABOVE_TERRAIN` (`SetPlaneMinHeightAboveTerrain`)

---
### SetTaxiLights

`SET_TAXI_LIGHTS` · hash `0x598803E85E8448D9` · jhash `0x68639D85` · **Cliente**

```lua
SetTaxiLights(vehicle, state)
```
```c
void SET_TAXI_LIGHTS(Vehicle vehicle, BOOL state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This is not tested - it's just an assumption.  
Doesn't seem to work.  I'll try with an int instead. --JT  
Read the scripts, im dumpass.   
Doesn't work at all, wether with an bool neither an int  
                            if (!VEHICLE::IS_TAXI_LIGHT_ON(l_115)) {  
                                VEHICLE::SET_TAXI_LIGHTS(l_115, 1);  
                            }  
```

---
### SetTrailerAttachmentEnabled

`SET_TRAILER_ATTACHMENT_ENABLED` · hash `0x2FA2494B47FDD009` · **Cliente**

```lua
SetTrailerAttachmentEnabled(vehicle, enabled)
```
```c
void SET_TRAILER_ATTACHMENT_ENABLED(Vehicle vehicle, BOOL enabled);
```

**Parámetros**

- `vehicle` (`Vehicle`): The trailer to set attachment state for
- `enabled` (`BOOL`): Enable or disable attachment

**Devuelve:** `void`

**Descripción oficial:**

Sets whether the trailer can attach to vehicles

**Nombres antiguos (alias):** `0x2FA2494B47FDD009` (`N_0x2fa2494b47fdd009`)

**Ejemplo (lua):**

```lua
local trailerModel = `tanker`
local trailerCoordinates = vector3(-323.59, -757.83, 53.25)
local trailerHeading = 247.77

RequestModel(trailerModel)

while not HasModelLoaded(trailerModel) do
  Wait(0)
end

local trailerIndex = CreateVehicle(trailerModel, trailerCoordinates.x, trailerCoordinates.y, trailerCoordinates.z, trailerHeading, true, false)

SetTrailerAttachmentEnabled(trailerIndex, false)
SetModelAsNoLongerNeeded(trailerModel)
```

---
### SetTrailerInverseMassScale

`SET_TRAILER_INVERSE_MASS_SCALE` · hash `0x2A8F319B392E7B3F` · jhash `0xE74E85CE` · **Cliente**

```lua
SetTrailerInverseMassScale(vehicle, p1)
```
```c
void SET_TRAILER_INVERSE_MASS_SCALE(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2A8F319B392E7B3F` (`N_0x2a8f319b392e7b3f`)

---
### SetTrailerLegsLowered

`_SET_TRAILER_LEGS_LOWERED` · hash `0x878C75C09FBDB942` · **Cliente**

```lua
SetTrailerLegsLowered()
```
```c
void _SET_TRAILER_LEGS_LOWERED();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Inverse of 0x95CF53B3D687F9FA
```

```
NativeDB Added Parameter 1: Vehicle vehicle
```

**Nombres antiguos (alias):** `0x878C75C09FBDB942` (`N_0x878c75c09fbdb942`)

---
### SetTrailerLegsRaised

`SET_TRAILER_LEGS_RAISED` · hash `0x95CF53B3D687F9FA` · jhash `0x06C47A6F` · **Cliente**

```lua
SetTrailerLegsRaised(vehicle)
```
```c
void SET_TRAILER_LEGS_RAISED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
in the decompiled scripts, seems to be always called on the vehicle right after being attached to a trailer.
```

**Nombres antiguos (alias):** `0x95CF53B3D687F9FA` (`N_0x95cf53b3d687f9fa`)

---
### SetTrainCruiseSpeed

`SET_TRAIN_CRUISE_SPEED` · hash `0x16469284DB8C62B5` · jhash `0xB507F51D` · **Cliente**

```lua
SetTrainCruiseSpeed(train, speed)
```
```c
void SET_TRAIN_CRUISE_SPEED(Vehicle train, float speed);
```

**Parámetros**

- `train` (`Vehicle`)
- `speed` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Used to control train speed, can be used to start and stop its movement as well.

**Ejemplo (lua):**

```lua
local train = CreateMissionTrain(21, 40.2, -1201.3, 31.0, false)
SetTrainCruiseSpeed(train, 20.0) -- Can be used to 'start' the train
SetTrainCruiseSpeed(train, 0.0) -- Can be used to 'stop' the train
```

---
### SetTrainSpeed

`SET_TRAIN_SPEED` · hash `0xAA0BC91BE0B796E3` · jhash `0xDFC35E4D` · **Cliente**

```lua
SetTrainSpeed(train, speed)
```
```c
void SET_TRAIN_SPEED(Vehicle train, float speed);
```

**Parámetros**

- `train` (`Vehicle`)
- `speed` (`float`)

**Devuelve:** `void`

---
### SetTrainTrackSpawnFrequency

`SET_TRAIN_TRACK_SPAWN_FREQUENCY` · hash `0x21973BBF8D17EDFA` · jhash `0xD5774FB7` · **Cliente**

```lua
SetTrainTrackSpawnFrequency(trackIndex, frequency)
```
```c
void SET_TRAIN_TRACK_SPAWN_FREQUENCY(int trackIndex, int frequency);
```

**Parámetros**

- `trackIndex` (`int`)
- `frequency` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only called once inside main_persitant with the parameters, 0  
```

**Nombres antiguos (alias):** `0x21973BBF8D17EDFA` (`N_0x21973bbf8d17edfa`)

---
### SetTransformRateForAnimation

`SET_TRANSFORM_RATE_FOR_ANIMATION` · hash `0x498218259FB7C72D` · **Cliente**

```lua
SetTransformRateForAnimation(vehicle, transformRate)
```
```c
void SET_TRANSFORM_RATE_FOR_ANIMATION(Vehicle vehicle, float transformRate);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle for which the submarine car conversion animation speed should be adjusted.
- `transformRate` (`float`): The rate at which the submarine car conversion animations will be played.

**Devuelve:** `void`

**Descripción oficial:**

Affects the playback speed of the submarine car conversion animations. Does not affect hardcoded animations such as the wheels being retracted. In decompiled scripts the only value used for transformRate is 2.5.

**Nombres antiguos (alias):** `0x498218259FB7C72D` (`N_0x498218259fb7c72d`), `_SET_UNK_FLOAT_0x104_FOR_SUBMARINE_VEHICLE_TASK` (`SetUnkFloatN_0x104ForSubmarineVehicleTask`)

**Ejemplo (lua):**

```lua
-- This example sets the transform rate for the submarine car conversion animations to 2.5

-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle in which the player is currently seated
local vehicle = GetVehiclePedIsIn(playerPed, false) -- Get the vehicle in which the player is currently seated

-- Retrieve the vehicle model hash
local vehicleHash = GetEntityModel(vehicle)

-- Check if the vehicle exists in the game world and if it is a Stromberg.
if not DoesEntityExist(vehicle) or not vehicleHash == GetHashKey("stromberg") then
    -- If the vehicle does not exist or it's not a stromberg, end the execution of the code here.
    return
end

-- Set the transform rate for the submarine car conversion animations to 2.5
SetTransformRateForAnimation(vehicle, 2.5)
```

**Ejemplo (js):**

```js
// This example sets the transform rate for the submarine car conversion animations to 2.5

// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle in which the player is currently seated
const vehicle = GetVehiclePedIsIn(playerPed, false); // Get the vehicle in which the player is currently seated

// Retrieve the vehicle model hash
const vehicleHash = GetEntityModel(vehicle);

// Check if the vehicle exists in the game world and if it is a Stromberg.
if (!DoesEntityExist(vehicle) || vehicleHash !== GetHashKey("stromberg")) {
    // If the vehicle does not exist or it's not a stromberg, end the execution of the code here.
    return;
}

// Set the transform rate for the submarine car conversion animations to 2.5
SetTransformRateForAnimation(vehicle, 2.5);
```

**Ejemplo (cs):**

```cs
// This example sets the transform rate for the submarine car conversion animations to 2.5
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle in which the player is currently seated
int vehicle = GetVehiclePedIsIn(playerPed, false); // Get the vehicle in which the player is currently seated

// Retrieve the vehicle model hash
uint vehicleHash = (uint)GetEntityModel(vehicle);

// Check if the vehicle exists in the game world and if it is a Stromberg.
if (!DoesEntityExist(vehicle) || vehicleHash != (uint)GetHashKey("stromberg"))
{
    // If the vehicle does not exist or it's not a stromberg, end the execution of the code here.
    return;
}

// Set the transform rate for the submarine car conversion animations to 2.5
SetTransformRateForAnimation(vehicle, 2.5f);
```

---
### SetTransformToSubmarineUsesAlternateInput

`SET_TRANSFORM_TO_SUBMARINE_USES_ALTERNATE_INPUT` · hash `0x41B9FB92EDED32A6` · **Cliente**

```lua
SetTransformToSubmarineUsesAlternateInput(vehicle, useAlternateInput)
```
```c
void SET_TRANSFORM_TO_SUBMARINE_USES_ALTERNATE_INPUT(Vehicle vehicle, bool useAlternateInput);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle for which the submarine mode should be configured.
- `useAlternateInput` (`bool`): A boolean switch to enable/disable the use of alternate input.

**Devuelve:** `void`

**Descripción oficial:**

Changes the key used to transform a vehicle into submarine mode. When set to true, the transformation key switches from the default raise/lower convertible roof key (usually 'H') to the special vehicle transformation key (usually 'X').

```
NativeDB Introduced: v1365
```

**Nombres antiguos (alias):** `0x41B9FB92EDED32A6` (`N_0x41b9fb92eded32a6`), `_SET_UNK_BOOL_0x102_FOR_SUBMARINE_VEHICLE_TASK` (`SetUnkBoolN_0x102ForSubmarineVehicleTask`)

**Ejemplo (lua):**

```lua
-- This example sets the key for submarine mode transformation to special vehicle transform 

-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle in which the player is currently seated
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Retrieve the vehicle model hash
local vehicleHash = GetEntityModel(vehicle)

-- Check if the vehicle exists in the game world and if it is a Stromberg.
if not DoesEntityExist(vehicle) or not vehicleHash == GetHashKey("stromberg") then
    -- If the vehicle does not exist or it's not a stromberg, end the execution of the code here.
    return
end

-- Set the key for submarine mode transformation to special vehicle transform (X by default)
SetTransformToSubmarineUsesAlternateInput(vehicle, true)
```

**Ejemplo (js):**

```js
// This example sets the key for submarine mode transformation to special vehicle transform

// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle in which the player is currently seated
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Retrieve the vehicle model hash
const vehicleHash = GetEntityModel(vehicle);

// Check if the vehicle exists in the game world and if it is a Stromberg.
if (!DoesEntityExist(vehicle) || vehicleHash !== GetHashKey("stromberg")) {
    // If the vehicle does not exist or it's not a stromberg, end the execution of the code here.
    return;
}

// Set the key for submarine mode transformation to special vehicle transform (X by default)
SetTransformToSubmarineUsesAlternateInput(vehicle, true);
```

**Ejemplo (cs):**

```cs
// This example sets the key for submarine mode transformation to special vehicle transform
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle in which the player is currently seated
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Retrieve the vehicle model hash
uint vehicleHash = (uint)GetEntityModel(vehicle);

// Check if the vehicle exists in the game world and if it is a Stromberg.
if (!DoesEntityExist(vehicle) || vehicleHash != (uint)GetHashKey("stromberg"))
{
    // If the vehicle does not exist or it's not a stromberg, end the execution of the code here.
    return;
}

// Set the key for submarine mode transformation to special vehicle transform (X by default)
SetTransformToSubmarineUsesAlternateInput(vehicle, true);
```

---
### SetTyreHealth

`_SET_TYRE_HEALTH` · hash `0x74C68EF97645E79D` · **Cliente**

```lua
SetTyreHealth(vehicle, wheelIndex, health)
```
```c
void _SET_TYRE_HEALTH(Vehicle vehicle, int wheelIndex, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `health` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### SetTyreSoftnessMultiplier

`_SET_TYRE_SOFTNESS_MULTIPLIER` · hash `0x392183BB9EA57697` · **Cliente**

```lua
SetTyreSoftnessMultiplier(vehicle, wheelIndex, multiplier)
```
```c
void _SET_TYRE_SOFTNESS_MULTIPLIER(Vehicle vehicle, int wheelIndex, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Controls how fast the tires wear out.
Default values from Rockstar's Open Wheel Race JSON's:
"owrtss" (Soft): 2.2
"owrtsm" (Medium): 1.7
"owrtsh" (Hard): 1.2
Usable wheels:
0: wheel_lf
1: wheel_rf
2: wheel_lm1
3: wheel_rm1
4: wheel_lr
5: wheel_rr
```

```
NativeDB Introduced: v2060
```

**Nombres antiguos (alias):** `0x392183BB9EA57697` (`N_0x392183bb9ea57697`)

---
### SetTyreTractionLossMultiplier

`_SET_TYRE_TRACTION_LOSS_MULTIPLIER` · hash `0xC970D0E0FC31D768` · **Cliente**

```lua
SetTyreTractionLossMultiplier(vehicle, wheelIndex, multiplier)
```
```c
void _SET_TYRE_TRACTION_LOSS_MULTIPLIER(Vehicle vehicle, int wheelIndex, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Controls how much traction the wheel loses.
Default values from Rockstar's Open Wheel Race JSON's:
"owrtds" (Soft): 0.05
"owrtdm" (Medium): 0.45
"owrtdh" (Hard): 0.8
Usable wheels:
0: wheel_lf
1: wheel_rf
2: wheel_lm1
3: wheel_rm1
4: wheel_lr
5: wheel_rr
```

```
NativeDB Introduced: v2060
```

**Nombres antiguos (alias):** `0xC970D0E0FC31D768` (`N_0xc970d0e0fc31d768`)

---
### SetTyreWearMultiplier

`_SET_TYRE_WEAR_MULTIPLIER` · hash `0x01894E2EDE923CA2` · **Cliente**

```lua
SetTyreWearMultiplier(vehicle, wheelIndex, multiplier)
```
```c
void _SET_TYRE_WEAR_MULTIPLIER(Vehicle vehicle, int wheelIndex, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### SetUseHigherVehicleJumpForce

`_SET_USE_HIGHER_VEHICLE_JUMP_FORCE` · hash `0xF06A16CA55D138D8` · **Cliente**

```lua
SetUseHigherVehicleJumpForce(vehicle, toggle)
```
```c
void _SET_USE_HIGHER_VEHICLE_JUMP_FORCE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Allows vehicles with the FLAG_JUMPING_CAR flag to jump higher (i.e. Ruiner 2000).

**Nombres antiguos (alias):** `0xF06A16CA55D138D8` (`N_0xf06a16ca55d138d8`)

---
### SetVehicleActAsIfHighSpeedForFragSmashing

`SET_VEHICLE_ACT_AS_IF_HIGH_SPEED_FOR_FRAG_SMASHING` · hash `0x1F9FB66F3A3842D2` · jhash `0x4D840FC4` · **Cliente**

```lua
SetVehicleActAsIfHighSpeedForFragSmashing(vehicle, actHighSpeed)
```
```c
void SET_VEHICLE_ACT_AS_IF_HIGH_SPEED_FOR_FRAG_SMASHING(Vehicle vehicle, BOOL actHighSpeed);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to be affected by this setting.
- `actHighSpeed` (`BOOL`): A boolean flag. Set to `true` to make the vehicle act as if it's at high speed for the current frame

**Devuelve:** `void`

**Descripción oficial:**

This native is used to simulate a high-speed impact for a vehicle when it collides with a breakable object (frag). It's particularly useful in scripted sequences where a vehicle is required to break through a barrier but might not actually be moving at a sufficient speed to do so realistically. Note that this setting is temporary and will reset after one frame, so it needs to be called every frame for a lasting effect.

**Nombres antiguos (alias):** `0x1F9FB66F3A3842D2` (`N_0x1f9fb66f3a3842d2`)

---
### SetVehicleActiveDuringPlayback

`SET_VEHICLE_ACTIVE_DURING_PLAYBACK` · hash `0xDFFCEF48E511DB48` · jhash `0xEB7D7C27` · **Cliente**

```lua
SetVehicleActiveDuringPlayback(vehicle, toggle)
```
```c
void SET_VEHICLE_ACTIVE_DURING_PLAYBACK(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDFFCEF48E511DB48` (`N_0xdffcef48e511db48`)

---
### SetVehicleActiveForPedNavigation

`SET_VEHICLE_ACTIVE_FOR_PED_NAVIGATION` · hash `0x21115BCD6E44656A` · jhash `0xEBC225C1` · **Cliente**

```lua
SetVehicleActiveForPedNavigation(vehicle, toggle)
```
```c
void SET_VEHICLE_ACTIVE_FOR_PED_NAVIGATION(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x21115BCD6E44656A` (`N_0x21115bcd6e44656a`), `_SET_VEHICLE_CLOSE_DOOR_DEFERED_ACTION` (`SetVehicleCloseDoorDeferedAction`)

---
### SetVehicleAlarm

`SET_VEHICLE_ALARM` · hash `0xCDE5E70C1DDB954C` · jhash `0x24877D84` · **Cliente · también en el servidor (RPC)**

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

---
### SetVehicleAllowHomingMissleLockon

`SET_VEHICLE_ALLOW_HOMING_MISSLE_LOCKON` · hash `0x7D6F9A3EF26136A0` · jhash `0xBB54ECCA` · **Cliente**

```lua
SetVehicleAllowHomingMissleLockon(vehicle, toggle, p2)
```
```c
void SET_VEHICLE_ALLOW_HOMING_MISSLE_LOCKON(Vehicle vehicle, BOOL toggle, BOOL p2);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `toggle` (`BOOL`): `true` to allow homing missile lock-on, `false` to disable it.
- `p2` (`BOOL`): Unknown parameter, typically `false`.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether homing missiles can lock onto the specified vehicle.
When set to `false`, players using a Homing Launcher or vehicles with homing missiles will not be able to lock onto the target vehicle.

**Nombres antiguos (alias):** `0x7D6F9A3EF26136A0` (`N_0x7d6f9a3ef26136a0`)

**Ejemplo (lua):**

```lua
-- Disable homing missile lock-on for the player's current vehicle.
local playerPed = PlayerPedId()
local vehicle = GetVehiclePedIsIn(playerPed, false)

if vehicle ~= 0 then
    SetVehicleAllowHomingMissleLockon(vehicle, false, false)
end
```

**Ejemplo (js):**

```js
// Disable homing missile lock-on for the player's current vehicle.
const playerPed = PlayerPedId();
const vehicle = GetVehiclePedIsIn(playerPed, false);

if (vehicle !== 0) {
    SetVehicleAllowHomingMissleLockon(vehicle, false, false);
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Disable homing missile lock-on for the player's current vehicle.
int playerPed = PlayerPedId();
int vehicle = GetVehiclePedIsIn(playerPed, false);

if (vehicle != 0)
{
    SetVehicleAllowHomingMissleLockon(vehicle, false, false);
}
```

---
### SetVehicleAllowNoPassengersLockon

`SET_VEHICLE_ALLOW_NO_PASSENGERS_LOCKON` · hash `0x5D14D4154BFE7B2C` · jhash `0x8BAAC437` · **Cliente**

```lua
SetVehicleAllowNoPassengersLockon(veh, toggle)
```
```c
void SET_VEHICLE_ALLOW_NO_PASSENGERS_LOCKON(Vehicle veh, BOOL toggle);
```

**Parámetros**

- `veh` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the vehicle accept no passengers.  
```

---
### SetVehicleAutomaticallyAttaches

`SET_VEHICLE_AUTOMATICALLY_ATTACHES` · hash `0x8BA6F76BC53A1493` · jhash `0x4273A8D3` · **Cliente**

```lua
local retval = SetVehicleAutomaticallyAttaches(vehicle, p1, p2)
```
```c
Any SET_VEHICLE_AUTOMATICALLY_ATTACHES(Vehicle vehicle, BOOL p1, Any p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### SetVehicleBodyHealth

`SET_VEHICLE_BODY_HEALTH` · hash `0xB77D05AC8C78AADB` · jhash `0x920C2517` · **Cliente · también en el servidor (RPC)**

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

---
### SetVehicleBombCount

`_SET_VEHICLE_BOMB_COUNT` · hash `0xF4B2ED59DEB5D774` · **Cliente**

```lua
SetVehicleBombCount(aircraft, bombCount)
```
```c
void _SET_VEHICLE_BOMB_COUNT(Vehicle aircraft, int bombCount);
```

**Parámetros**

- `aircraft` (`Vehicle`): The vehicle to set the bombCount on.
- `bombCount` (`int`): The amount of bombs to set for this vehicle.

**Devuelve:** `void`

**Descripción oficial:**

Sets the amount of bombs that this vehicle has. As far as I know, this does *not* impact vehicle weapons or the ammo of those weapons in any way, it is just a way to keep track of the amount of bombs in a specific plane.

In decompiled scripts this is used to deduct from or add to the count whenever bombs are dropped or purchased/restocked.

Use [`_GET_AIRCRAFT_BOMB_COUNT`](VEHICLE-1.md#getvehiclebombcount) to get the amount of bombs on that vehicle.

**Nombres antiguos (alias):** `0xF4B2ED59DEB5D774` (`N_0xf4b2ed59deb5d774`), `_SET_VEHICLE_BOMBS` (`SetVehicleBombs`), `_SET_AIRCRAFT_BOMB_COUNT` (`SetAircraftBombCount`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetAircraftBombCount(vehicle, 10)
```

**Ejemplo (cs):**

```cs
int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetAircraftBombCount(vehicle, 10);
```

---
### SetVehicleBrake

`SET_VEHICLE_BRAKE` · hash `0xE4E2FD323574965C` · jhash `0x5A36BC37` · **Cliente**

```lua
SetVehicleBrake(vehicle, toggle)
```
```c
void SET_VEHICLE_BRAKE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE4E2FD323574965C` (`N_0xe4e2fd323574965c`)

---
### SetVehicleBrakeLights

`SET_VEHICLE_BRAKE_LIGHTS` · hash `0x92B35082E0B42F66` · jhash `0x6D9BA11E` · **Cliente**

```lua
SetVehicleBrakeLights(vehicle, toggle)
```
```c
void SET_VEHICLE_BRAKE_LIGHTS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleBulldozerArmPosition

`SET_VEHICLE_BULLDOZER_ARM_POSITION` · hash `0xF8EBCCC96ADB9FB7` · jhash `0xED23C8A3` · **Cliente**

```lua
SetVehicleBulldozerArmPosition(vehicle, position, p2)
```
```c
void SET_VEHICLE_BULLDOZER_ARM_POSITION(Vehicle vehicle, float position, BOOL p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `position` (`float`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the arm position of a bulldozer. Position must be a value between 0.0 and 1.0. Ignored when `p2` is set to false, instead incrementing arm position by 0.1 (or 10%).

**Nombres antiguos (alias):** `0xF8EBCCC96ADB9FB7` (`N_0xf8ebccc96adb9fb7`)

---
### SetVehicleBurnout

`SET_VEHICLE_BURNOUT` · hash `0xFB8794444A7D60FB` · jhash `0x9B6EF0EA` · **Cliente**

```lua
SetVehicleBurnout(vehicle, toggle)
```
```c
void SET_VEHICLE_BURNOUT(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
On accelerating, spins the driven wheels with the others braked, so you don't go anywhere.  
```

---
### SetVehicleCanBeLockedOn

`_SET_VEHICLE_CAN_BE_LOCKED_ON` · hash `0x1DDA078D12879EEE` · **Cliente**

```lua
SetVehicleCanBeLockedOn(vehicle, canBeLockedOn, unk)
```
```c
void _SET_VEHICLE_CAN_BE_LOCKED_ON(Vehicle vehicle, BOOL canBeLockedOn, BOOL unk);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `canBeLockedOn` (`BOOL`)
- `unk` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VEHICLE_AL*
```

**Nombres antiguos (alias):** `0x1DDA078D12879EEE` (`N_0x1dda078d12879eee`)

---
### SetVehicleCanBeTargetted

`SET_VEHICLE_CAN_BE_TARGETTED` · hash `0x3750146A28097A82` · jhash `0x64B70B1D` · **Cliente**

```lua
SetVehicleCanBeTargetted(vehicle, state)
```
```c
void SET_VEHICLE_CAN_BE_TARGETTED(Vehicle vehicle, BOOL state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This has not yet been tested - it's just an assumption of what the types could be.  
```

---
### SetVehicleCanBeUsedByFleeingPeds

`SET_VEHICLE_CAN_BE_USED_BY_FLEEING_PEDS` · hash `0x300504B23BD3B711` · jhash `0x5130DB1E` · **Cliente**

```lua
SetVehicleCanBeUsedByFleeingPeds(vehicle, toggle)
```
```c
void SET_VEHICLE_CAN_BE_USED_BY_FLEEING_PEDS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x300504B23BD3B711` (`N_0x300504b23bd3b711`)

---
### SetVehicleCanBeVisiblyDamaged

`SET_VEHICLE_CAN_BE_VISIBLY_DAMAGED` · hash `0x4C7028F78FFD3681` · jhash `0xC5D94017` · **Cliente**

```lua
SetVehicleCanBeVisiblyDamaged(vehicle, state)
```
```c
void SET_VEHICLE_CAN_BE_VISIBLY_DAMAGED(Vehicle vehicle, BOOL state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleCanBreak

`SET_VEHICLE_CAN_BREAK` · hash `0x59BF8C3D52C92F66` · jhash `0x90A810D1` · **Cliente**

```lua
SetVehicleCanBreak(vehicle, toggle)
```
```c
void SET_VEHICLE_CAN_BREAK(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleCanDeformWheels

`SET_VEHICLE_CAN_DEFORM_WHEELS` · hash `0x0CDDA42F9E360CA6` · jhash `0x9B581DE7` · **Cliente**

```lua
SetVehicleCanDeformWheels(vehicle, toggle)
```
```c
void SET_VEHICLE_CAN_DEFORM_WHEELS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0CDDA42F9E360CA6` (`N_0x0cdda42f9e360ca6`)

---
### SetVehicleCanEngineOperateOnFire

`_SET_VEHICLE_CAN_ENGINE_OPERATE_ON_FIRE` · hash `0x206BC5DC9D1AC70A` · jhash `0x8EACBD13` · **Cliente**

```lua
SetVehicleCanEngineOperateOnFire(vehicle, toggle)
```
```c
void _SET_VEHICLE_CAN_ENGINE_OPERATE_ON_FIRE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x206BC5DC9D1AC70A` (`N_0x206bc5dc9d1ac70a`)

---
### SetVehicleCanLeakOil

`SET_VEHICLE_CAN_LEAK_OIL` · hash `0x51BB2D88D31A914B` · jhash `0x88F0F7E7` · **Cliente**

```lua
SetVehicleCanLeakOil(vehicle, toggle)
```
```c
void SET_VEHICLE_CAN_LEAK_OIL(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x51BB2D88D31A914B` (`N_0x51bb2d88d31a914b`)

---
### SetVehicleCanLeakPetrol

`SET_VEHICLE_CAN_LEAK_PETROL` · hash `0x192547247864DFDD` · jhash `0x90D6EE57` · **Cliente**

```lua
SetVehicleCanLeakPetrol(vehicle, toggle)
```
```c
void SET_VEHICLE_CAN_LEAK_PETROL(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x192547247864DFDD` (`N_0x192547247864dfdd`)

---
### SetVehicleCanSaveInGarage

`SET_VEHICLE_CAN_SAVE_IN_GARAGE` · hash `0x428BACCDF5E26EAD` · jhash `0x1604C2F5` · **Cliente**

```lua
SetVehicleCanSaveInGarage(vehicle, toggle)
```
```c
void SET_VEHICLE_CAN_SAVE_IN_GARAGE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x428BACCDF5E26EAD` (`N_0x428baccdf5e26ead`)

---
### SetVehicleCeilingHeight

`SET_VEHICLE_CEILING_HEIGHT` · hash `0xA46413066687A328` · jhash `0x98A10A86` · **Cliente**

```lua
SetVehicleCeilingHeight(vehicle, height)
```
```c
void SET_VEHICLE_CEILING_HEIGHT(Vehicle vehicle, float height);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `height` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Previously named GET_VEHICLE_DEFORMATION_GET_TREE (hash collision)
from Decrypted Scripts I found
VEHICLE::SET_VEHICLE_CEILING_HEIGHT(l_BD9[2/*2*/], 420.0);
```

**Nombres antiguos (alias):** `GET_VEHICLE_DEFORMATION_GET_TREE` (`GetVehicleDeformationGetTree`)

---
### SetVehicleCheatPowerIncrease

`SET_VEHICLE_CHEAT_POWER_INCREASE` · hash `0xB59E4BD37AE292DB` · jhash `0x642DA5AA` · **Cliente**

```lua
SetVehicleCheatPowerIncrease(vehicle, value)
```
```c
void SET_VEHICLE_CHEAT_POWER_INCREASE(Vehicle vehicle, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
<1.0 - Decreased torque
=1.0 - Default torque
>1.0 - Increased torque
Negative values will cause the vehicle to go backwards instead of forwards while accelerating.
value - is between 0.2 and 1.8 in the decompiled scripts.
This needs to be called every frame to take effect.
```

**Nombres antiguos (alias):** `_SET_VEHICLE_ENGINE_TORQUE_MULTIPLIER` (`SetVehicleEngineTorqueMultiplier`)

---
### SetVehicleColourCombination

`SET_VEHICLE_COLOUR_COMBINATION` · hash `0x33E8CD3322E2FE31` · jhash `0xA557AEAD` · **Cliente · también en el servidor (RPC)**

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

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
local index = math.random(0, 16)
SetVehicleColourCombination(vehicle, index)
```

---
### SetVehicleColours

`SET_VEHICLE_COLOURS` · hash `0x4F1D4BE3A7F24601` · jhash `0x57F24253` · **Cliente · también en el servidor (RPC)**

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

---
### SetVehicleControlsInverted

`_SET_VEHICLE_CONTROLS_INVERTED` · hash `0x5B91B229243351A8` · **Cliente**

```lua
SetVehicleControlsInverted(vehicle, state)
```
```c
void _SET_VEHICLE_CONTROLS_INVERTED(Vehicle vehicle, BOOL state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Inverts vehicle's controls. So INPUT_VEH_ACCELERATE will be INPUT_VEH_BRAKE and vise versa (same for A/D controls)
Doesn't work for planes/helis.
```

**Nombres antiguos (alias):** `0x5B91B229243351A8` (`N_0x5b91b229243351a8`)

---
### SetVehicleCountermeasureCount

`_SET_VEHICLE_COUNTERMEASURE_COUNT` · hash `0x9BDA23BF666F0855` · **Cliente**

```lua
SetVehicleCountermeasureCount(aircraft, count)
```
```c
void _SET_VEHICLE_COUNTERMEASURE_COUNT(Vehicle aircraft, int count);
```

**Parámetros**

- `aircraft` (`Vehicle`): The vehicle to set the amount of countermeasures on.
- `count` (`int`): The amount of countermeasures to set on this vehicle.

**Devuelve:** `void`

**Descripción oficial:**

Similar to [`_SET_AIRCRAFT_BOMB_COUNT`](#setvehiclebombcount), this sets the amount of countermeasures that are present on this vehicle.

Use [`_GET_AIRCRAFT_COUNTERMEASURE_COUNT`](VEHICLE-1.md#getvehiclecountermeasurecount) to get the current amount.

**Nombres antiguos (alias):** `0x9BDA23BF666F0855` (`N_0x9bda23bf666f0855`), `_SET_AIRCRAFT_COUNTERMEASURE_COUNT` (`SetAircraftCountermeasureCount`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetAircraftCountermeasureCount(vehicle, 10)
```

**Ejemplo (cs):**

```cs
int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetAircraftCountermeasureCount(vehicle, 10);
```

---
### SetVehicleCustomPrimaryColour

`SET_VEHICLE_CUSTOM_PRIMARY_COLOUR` · hash `0x7141766F91D15BEA` · jhash `0x8DF9F9BC` · **Cliente · también en el servidor (RPC)**

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

---
### SetVehicleCustomSecondaryColour

`SET_VEHICLE_CUSTOM_SECONDARY_COLOUR` · hash `0x36CED73BFED89754` · jhash `0x9D77259E` · **Cliente · también en el servidor (RPC)**

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

---
### SetVehicleDamage

`SET_VEHICLE_DAMAGE` · hash `0xA1DD317EA8FD4F29` · jhash `0x21B458B2` · **Cliente**

```lua
SetVehicleDamage(vehicle, xOffset, yOffset, zOffset, damage, radius, focusOnModel)
```
```c
void SET_VEHICLE_DAMAGE(Vehicle vehicle, float xOffset, float yOffset, float zOffset, float damage, float radius, BOOL focusOnModel);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `damage` (`float`)
- `radius` (`float`): the size of the damage sphere to apply
- `focusOnModel` (`BOOL`): when set to `true`, the damage sphere will travel towards the vehicle from the given point, thus guaranteeing an impact

**Devuelve:** `void`

**Descripción oficial:**

Apply damage to vehicle at a location. Location is relative to vehicle model (not world).
Radius of effect damage applied in a sphere at impact location
When `focusOnModel` set to `true`, the damage sphere will travel towards the vehicle from the given point, thus guaranteeing an impact

**Ejemplo (lua):**

```lua
-- Both of these are for an average sized car

-- nothing will be hit
SetVehicleDamage(vehicle, 0.0, 0.0, 0.33, 200.0, 100.0, false)

-- will hit the first hitbox on your Z index line
SetVehicleDamage(vehicle, 0.0, 0.0, 0.33, 200.0, 100.0, true)
```

---
### SetVehicleDamageModifier

`_SET_VEHICLE_DAMAGE_MODIFIER` · hash `0x4E20D2A627011E8E` · **Cliente**

```lua
local retval = SetVehicleDamageModifier(vehicle, p1)
```
```c
Any _SET_VEHICLE_DAMAGE_MODIFIER(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `Any`

**Descripción oficial:**

```
SET_VEHICLE_D*
```

**Nombres antiguos (alias):** `0x4E20D2A627011E8E` (`N_0x4e20d2a627011e8e`)

---
### SetVehicleDashboardColor

`_SET_VEHICLE_DASHBOARD_COLOR` · hash `0x6089CDF6A57F326C` · **Cliente**

```lua
SetVehicleDashboardColor(vehicle, color)
```
```c
void _SET_VEHICLE_DASHBOARD_COLOR(Vehicle vehicle, int color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `color` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_VEHICLE_DASHBOARD_COLOUR` (`SetVehicleDashboardColour`)

---
### SetVehicleDeformationFixed

`SET_VEHICLE_DEFORMATION_FIXED` · hash `0x953DA1E1B12C0491` · jhash `0xDD2920C8` · **Cliente**

```lua
SetVehicleDeformationFixed(vehicle)
```
```c
void SET_VEHICLE_DEFORMATION_FIXED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
This fixes the deformation of a vehicle but the vehicle health doesn't improve  
```

---
### SetVehicleDensityMultiplierThisFrame

`SET_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME` · hash `0x245A6883D966D537` · jhash `0xF4187E51` · **Cliente**

```lua
SetVehicleDensityMultiplierThisFrame(multiplier)
```
```c
void SET_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

**Usage:**

*   Use this native inside a looped function.
*   Values:
    *   `0.0` = no vehicles on streets
    *   `1.0` = normal vehicles on streets

`1.0` Seems to be the maximum.

---
### SetVehicleDirtLevel

`SET_VEHICLE_DIRT_LEVEL` · hash `0x79D3B596FE44EE8B` · jhash `0x2B39128B` · **Cliente · también en el servidor (RPC)**

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

**Ejemplo (lua):**

```lua
local Vehicle = GetVehiclePedIsUsing(PlayerPedId())
SetVehicleDirtLevel(Vehicle, 0.0) -- set the vehicle dirt level to 0.0
```

---
### SetVehicleDisableTowing

`SET_VEHICLE_DISABLE_TOWING` · hash `0x2B6747FAA9DB9D6B` · jhash `0x95A9ACCB` · **Cliente**

```lua
SetVehicleDisableTowing(vehicle, toggle)
```
```c
void SET_VEHICLE_DISABLE_TOWING(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2B6747FAA9DB9D6B` (`N_0x2b6747faa9db9d6b`)

---
### SetVehicleDoorBroken

`SET_VEHICLE_DOOR_BROKEN` · hash `0xD4D4F6A4AB575A33` · jhash `0x8147FEA7` · **Cliente · también en el servidor (RPC)**

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

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](#setvehicledoorshut)

---
### SetVehicleDoorCanBreak

`_SET_VEHICLE_DOOR_CAN_BREAK` · hash `0x2FA133A4A9D37ED8` · jhash `0x065B92B3` · **Cliente**

```lua
SetVehicleDoorCanBreak(vehicle, doorIndex, isBreakable)
```
```c
void _SET_VEHICLE_DOOR_CAN_BREAK(Vehicle vehicle, int doorIndex, BOOL isBreakable);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)
- `isBreakable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](#setvehicledoorshut)

**Nombres antiguos (alias):** `_SET_VEHICLE_DOOR_BREAKABLE` (`SetVehicleDoorBreakable`)

---
### SetVehicleDoorControl

`SET_VEHICLE_DOOR_CONTROL` · hash `0xF2BFA0430F0A0FCB` · jhash `0x572DD360` · **Cliente**

```lua
SetVehicleDoorControl(vehicle, doorIndex, speed, angle)
```
```c
void SET_VEHICLE_DOOR_CONTROL(Vehicle vehicle, int doorIndex, int speed, float angle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)
- `speed` (`int`): 5 is fast, 1 is slow 3 is medium
- `angle` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](#setvehicledoorshut)

---
### SetVehicleDoorLatched

`SET_VEHICLE_DOOR_LATCHED` · hash `0xA5A9653A8D2CAF48` · jhash `0x4EB7BBFC` · **Cliente**

```lua
SetVehicleDoorLatched(vehicle, doorIndex, forceClose, lock, p4)
```
```c
void SET_VEHICLE_DOOR_LATCHED(Vehicle vehicle, int doorIndex, BOOL forceClose, BOOL lock, BOOL p4);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)
- `forceClose` (`BOOL`)
- `lock` (`BOOL`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](#setvehicledoorshut)

---
### SetVehicleDoorOpen

`SET_VEHICLE_DOOR_OPEN` · hash `0x7C65DAC73C35C862` · jhash `0xBB75D38B` · **Cliente**

```lua
SetVehicleDoorOpen(vehicle, doorIndex, loose, openInstantly)
```
```c
void SET_VEHICLE_DOOR_OPEN(Vehicle vehicle, int doorIndex, BOOL loose, BOOL openInstantly);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle.
- `doorIndex` (`int`): Index of the door you want to open (0-7)
- `loose` (`BOOL`): Whether the door is "loose" (if true the doors have no "spring" and can be closed easily.)
- `openInstantly` (`BOOL`): Whether the doors open instantly (if true this native seems to ignore loose)

**Devuelve:** `void`

**Descripción oficial:**

Sets the specified door index open on the passed vehicle. See [`IS_VEHICLE_DOOR_FULLY_OPEN`](VEHICLE-1.md#isvehicledoorfullyopen).

**Ejemplo (lua):**

```lua
local Vehicle = GetVehiclePedIsUsing(PlayerPedId())
for i = 0, 5 do
  SetVehicleDoorOpen(Vehicle, i, false, true) -- will open every door from 0-5
end
```

---
### SetVehicleDoorShut

`SET_VEHICLE_DOOR_SHUT` · hash `0x93D9BD300D7789E5` · jhash `0x142606BD` · **Cliente**

```lua
SetVehicleDoorShut(vehicle, doorIndex, closeInstantly)
```
```c
void SET_VEHICLE_DOOR_SHUT(Vehicle vehicle, int doorIndex, BOOL closeInstantly);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle.
- `doorIndex` (`int`): Index of the door you want to close.
- `closeInstantly` (`BOOL`): Whether the doors close instantly.

**Devuelve:** `void`

**Descripción oficial:**

Sets the specified door index shut on the passed vehicle.

```cpp
enum eDoorId
{
	VEH_EXT_DOOR_DSIDE_F = 0,
	VEH_EXT_DOOR_DSIDE_R = 1,
	VEH_EXT_DOOR_PSIDE_F = 2,
	VEH_EXT_DOOR_PSIDE_R = 3,
	VEH_EXT_BONNET = 4,
	VEH_EXT_BOOT = 5,
	// 0x872E72B8 = 0xFFFFFFFF,
}
```

**Ejemplo (lua):**

```lua
local Vehicle = GetVehiclePedIsUsing(PlayerPedId())
for i = 0, 5 do
  SetVehicleDoorShut(Vehicle, i, false) -- will close all doors from 0-5
end
```

---
### SetVehicleDoorsLocked

`SET_VEHICLE_DOORS_LOCKED` · hash `0xB664292EAECF7FA6` · jhash `0x4CDD35D0` · **Cliente · también en el servidor (RPC)**

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

**Ejemplo (lua):**

```lua
-- Command to lock the car of the player for everyone.
RegisterCommand("lockcar", function()
    local playerPed = PlayerPedId() -- Get the player ped
    local vehicle = GetVehiclePedIsIn(playerPed, false) -- Get the vehicle the player is in
    if (vehicle == 0) then return end -- If the player is not in a vehicle, return
    SetVehicleDoorsLocked(vehicle, 2) -- Lock the doors of the vehicle
end, false)

-- Command to unlock the car of the player for everyone.
RegisterCommand("unlockcar", function()
    local playerPed = PlayerPedId() -- Get the player ped
    local vehicle = GetVehiclePedIsIn(playerPed, false) -- Get the vehicle the player is in
    if (vehicle == 0) then return end -- If the player is not in a vehicle, return
    SetVehicleDoorsLocked(vehicle, 1) -- Unlock the doors of the vehicle
end, false)
```

**Ejemplo (js):**

```js
// Command to lock the car of the player for everyone.
RegisterCommand("lockcar", () => {
    const playerPed = PlayerPedId(); // Get the player ped
    const vehicle = GetVehiclePedIsIn(playerPed, false); // Get the vehicle the player is in
    if (vehicle === 0) return; // If the player is not in a vehicle, return
    SetVehicleDoorsLocked(vehicle, 2); // Lock the doors of the vehicle
}, false);

// Command to unlock the car of the player for everyone.
RegisterCommand("unlockcar", () => {
    const playerPed = PlayerPedId(); // Get the player ped
    const vehicle = GetVehiclePedIsIn(playerPed, false); // Get the vehicle the player is in
    if (vehicle === 0) return; // If the player is not in a vehicle, return
    SetVehicleDoorsLocked(vehicle, 1); // Unlock the doors of the vehicle
}, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Command to lock the car of the player for everyone.
RegisterCommand("lockcar", () => {
    int playerPed = PlayerPedId(); // Get the player ped
    int vehicle = GetVehiclePedIsIn(playerPed, false); // Get the vehicle the player is in
    if (vehicle == 0) return; // If the player is not in a vehicle, return
    SetVehicleDoorsLocked(vehicle, 2); // Lock the doors of the vehicle
}, false);

// Command to unlock the car of the player for everyone.
RegisterCommand("unlockcar", () => {
    int playerPed = PlayerPedId(); // Get the player ped
    int vehicle = GetVehiclePedIsIn(playerPed, false); // Get the vehicle the player is in
    if (vehicle == 0) return; // If the player is not in a vehicle, return
    SetVehicleDoorsLocked(vehicle, 1); // Unlock the doors of the vehicle
}, false);
```

---
### SetVehicleDoorsLockedForAllPlayers

`SET_VEHICLE_DOORS_LOCKED_FOR_ALL_PLAYERS` · hash `0xA2F80B8D040727CC` · jhash `0x891BA8A4` · **Cliente**

```lua
SetVehicleDoorsLockedForAllPlayers(vehicle, toggle)
```
```c
void SET_VEHICLE_DOORS_LOCKED_FOR_ALL_PLAYERS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleDoorsLockedForNonScriptPlayers

`SET_VEHICLE_DOORS_LOCKED_FOR_NON_SCRIPT_PLAYERS` · hash `0x9737A37136F07E75` · jhash `0xE4EF6514` · **Cliente**

```lua
SetVehicleDoorsLockedForNonScriptPlayers(vehicle, toggle)
```
```c
void SET_VEHICLE_DOORS_LOCKED_FOR_NON_SCRIPT_PLAYERS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9737A37136F07E75` (`N_0x9737a37136f07e75`)

---
### SetVehicleDoorsLockedForPlayer

`SET_VEHICLE_DOORS_LOCKED_FOR_PLAYER` · hash `0x517AAF684BB50CD1` · jhash `0x49829236` · **Cliente**

```lua
SetVehicleDoorsLockedForPlayer(vehicle, player, toggle)
```
```c
void SET_VEHICLE_DOORS_LOCKED_FOR_PLAYER(Vehicle vehicle, Player player, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleDoorsLockedForTeam

`SET_VEHICLE_DOORS_LOCKED_FOR_TEAM` · hash `0xB81F6D4A8F5EEBA8` · jhash `0x4F85E783` · **Cliente**

```lua
SetVehicleDoorsLockedForTeam(vehicle, team, toggle)
```
```c
void SET_VEHICLE_DOORS_LOCKED_FOR_TEAM(Vehicle vehicle, int team, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `team` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleDoorsLockedForUnk

`_SET_VEHICLE_DOORS_LOCKED_FOR_UNK` · hash `0x203B527D1B77904C` · **Cliente**

```lua
SetVehicleDoorsLockedForUnk(vehicle, toggle)
```
```c
void _SET_VEHICLE_DOORS_LOCKED_FOR_UNK(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

---
### SetVehicleDoorsShut

`SET_VEHICLE_DOORS_SHUT` · hash `0x781B3D62BB013EF5` · jhash `0xBB1FF6E7` · **Cliente**

```lua
SetVehicleDoorsShut(vehicle, closeInstantly)
```
```c
void SET_VEHICLE_DOORS_SHUT(Vehicle vehicle, BOOL closeInstantly);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `closeInstantly` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Closes all doors of a vehicle:  
```

---
### SetVehicleDropsMoneyWhenBlownUp

`SET_VEHICLE_DROPS_MONEY_WHEN_BLOWN_UP` · hash `0x068F64F2470F9656` · jhash `0x4BB5605D` · **Cliente**

```lua
SetVehicleDropsMoneyWhenBlownUp(vehicle, toggle)
```
```c
void SET_VEHICLE_DROPS_MONEY_WHEN_BLOWN_UP(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Money pickups are created around cars when they explode. Only works when the vehicle model is a car. A single pickup is between 1 and 18 dollars in size. All car models seem to give the same amount of money.

Preview:

https://youtu.be/3arlUxzHl5Y
![](https://i.imgur.com/KsaWO6E.png)

**Nombres antiguos (alias):** `0x068F64F2470F9656` (`N_0x068f64f2470f9656`), `_SET_VEHICLE_CREATES_MONEY_PICKUPS_WHEN_EXPLODED` (`SetVehicleCreatesMoneyPickupsWhenExploded`)

---
### SetVehicleEngineCanDegrade

`SET_VEHICLE_ENGINE_CAN_DEGRADE` · hash `0x983765856F2564F9` · jhash `0x081DAC12` · **Cliente**

```lua
SetVehicleEngineCanDegrade(vehicle, toggle)
```
```c
void SET_VEHICLE_ENGINE_CAN_DEGRADE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleEngineHealth

`SET_VEHICLE_ENGINE_HEALTH` · hash `0x45F6D8EEF34ABEF1` · jhash `0x1B760FB5` · **Cliente**

```lua
SetVehicleEngineHealth(vehicle, health)
```
```c
void SET_VEHICLE_ENGINE_HEALTH(Vehicle vehicle, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `health` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
1000 is max health
Begins leaking gas at around 650 health
-999.90002441406 appears to be minimum health, although nothing special occurs <- false statement
-------------------------
Minimum: -4000
Maximum: 1000
-4000: Engine is destroyed
0 and below: Engine catches fire and health rapidly declines
300: Engine is smoking and losing functionality
1000: Engine is perfect
```

---
### SetVehicleEngineOn

`SET_VEHICLE_ENGINE_ON` · hash `0x2497C4717C8B881E` · jhash `0x7FBC86F1` · **Cliente**

```lua
SetVehicleEngineOn(vehicle, value, instantly, disableAutoStart)
```
```c
void SET_VEHICLE_ENGINE_ON(Vehicle vehicle, BOOL value, BOOL instantly, BOOL disableAutoStart);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to start or stop the engine on.
- `value` (`BOOL`): true to turn the vehicle on; false to turn it off.
- `instantly` (`BOOL`): if true, the vehicle will be set to the state immediately; otherwise, the current driver will physically turn on or off the engine.
- `disableAutoStart` (`BOOL`): If true, the system will prevent the engine from starting when the player got into it.

**Devuelve:** `void`

**Descripción oficial:**

Starts or stops the engine on the specified vehicle.
From what I've tested when I do this to a helicopter the propellers turn off after the engine has started.

---
### SetVehicleEnveffScale

`SET_VEHICLE_ENVEFF_SCALE` · hash `0x3AFDC536C3D01674` · jhash `0x8332730C` · **Cliente**

```lua
SetVehicleEnveffScale(vehicle, fade)
```
```c
void SET_VEHICLE_ENVEFF_SCALE(Vehicle vehicle, float fade);
```

**Parámetros**

- `vehicle` (`Vehicle`): Target vehicle
- `fade` (`float`): The paint fade effect strength

**Devuelve:** `void`

**Descripción oficial:**

Examples with a besra:

*   Fade value `0.0`:![](https://i.imgur.com/dlWnhgZ.png)
*   Fade value `0.5`:![](https://i.imgur.com/rbzMfh6.png)
*   Fade value `1.0`:![](https://i.imgur.com/pRqLnSP.png)

The parameter fade is a value from 0-1, where 0 is fresh paint.

**Nombres antiguos (alias):** `_SET_VEHICLE_PAINT_FADE` (`SetVehiclePaintFade`)

---
### SetVehicleExclusiveDriver

`SET_VEHICLE_EXCLUSIVE_DRIVER` · hash `0x41062318F23ED854` · jhash `0xFF62D324` · **Cliente**

```lua
SetVehicleExclusiveDriver(vehicle, toggle)
```
```c
void SET_VEHICLE_EXCLUSIVE_DRIVER(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Incorrectly named `SET_VEHICLE_EXCLUSIVE_DRIVER`; likely `SET_VEHICLE_ALLOW_*`.

Toggles a flag related to `SET_VEHICLE_EXCLUSIVE_DRIVER`, however, doesn't enable that feature (or trigger script events related to it).

See [`_SET_VEHICLE_EXCLUSIVE_DRIVER_2`](#setvehicleexclusivedriver_2).

```
NativeDB Removed Parameter 2: int index
```

**Nombres antiguos (alias):** `0x41062318F23ED854` (`N_0x41062318f23ed854`)

---
### SetVehicleExclusiveDriver_2

`_SET_VEHICLE_EXCLUSIVE_DRIVER_2` · hash `0xB5C51B5502E85E83` · jhash `0xAA8BD440` · **Cliente**

```lua
SetVehicleExclusiveDriver_2(vehicle, ped, index)
```
```c
void _SET_VEHICLE_EXCLUSIVE_DRIVER_2(Vehicle vehicle, Ped ped, int index);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `ped` (`Ped`)
- `index` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

The **actual** [`SET_VEHICLE_EXCLUSIVE_DRIVER`](#setvehicleexclusivedriver) native.

**Nombres antiguos (alias):** `0xB5C51B5502E85E83` (`N_0xb5c51b5502e85e83`)

---
### SetVehicleExplodesOnHighExplosionDamage

`SET_VEHICLE_EXPLODES_ON_HIGH_EXPLOSION_DAMAGE` · hash `0x71B0892EC081D60A` · jhash `0x38CC692B` · **Cliente**

```lua
SetVehicleExplodesOnHighExplosionDamage(vehicle, toggle)
```
```c
void SET_VEHICLE_EXPLODES_ON_HIGH_EXPLOSION_DAMAGE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets a vehicle to be strongly resistant to explosions. p0 is the vehicle; set p1 to false to toggle the effect on/off.  
```

---
### SetVehicleExplosiveDamageScale

`_SET_VEHICLE_EXPLOSIVE_DAMAGE_SCALE` · hash `0x84D7FFD223CAAFFD` · **Cliente**

```lua
local retval = SetVehicleExplosiveDamageScale(vehicle, scale)
```
```c
Any _SET_VEHICLE_EXPLOSIVE_DAMAGE_SCALE(Vehicle vehicle, float scale);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `scale` (`float`)

**Devuelve:** `Any` — Does not actually return anything.

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### SetVehicleExtendedRemovalRange

`SET_VEHICLE_EXTENDED_REMOVAL_RANGE` · hash `0x79DF7E806202CE01` · jhash `0xAEF9611C` · **Cliente**

```lua
SetVehicleExtendedRemovalRange(vehicle, range)
```
```c
void SET_VEHICLE_EXTENDED_REMOVAL_RANGE(Vehicle vehicle, int range);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `range` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Max value is 32767
```

**Nombres antiguos (alias):** `0x79DF7E806202CE01` (`N_0x79df7e806202ce01`)

---
### SetVehicleExtra

`SET_VEHICLE_EXTRA` · hash `0x7EE3A3C5E4A40CC9` · jhash `0x642D065C` · **Cliente**

```lua
SetVehicleExtra(vehicle, extraId, disable)
```
```c
void SET_VEHICLE_EXTRA(Vehicle vehicle, int extraId, BOOL disable);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `extraId` (`int`)
- `disable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Note: only some vehicle have extras  
extra ids are from 1 - 9 depending on the vehicle  
-------------------------------------------------  
^ not sure if outdated or simply wrong. Max extra ID for b944 is 14  
-------------------------------------------------  
p2 is not a on/off toggle. mostly 0 means on and 1 means off.  
not sure if it really should be a BOOL.  
-------------------------------------------------  
Confirmed p2 does not work as a bool. Changed to int. [0=on, 1=off]  
```

---
### SetVehicleExtraColours

`SET_VEHICLE_EXTRA_COLOURS` · hash `0x2036F561ADD12E33` · jhash `0x515DB2A0` · **Cliente**

```lua
SetVehicleExtraColours(vehicle, pearlescentColor, wheelColor)
```
```c
void SET_VEHICLE_EXTRA_COLOURS(Vehicle vehicle, int pearlescentColor, int wheelColor);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `pearlescentColor` (`int`)
- `wheelColor` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
They use the same color indexs as SET_VEHICLE_COLOURS.  
```

---
### SetVehicleFixed

`SET_VEHICLE_FIXED` · hash `0x115722B1B9C14C1C` · jhash `0x17469AA1` · **Cliente**

```lua
SetVehicleFixed(vehicle)
```
```c
void SET_VEHICLE_FIXED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle that will be fixed

**Devuelve:** `void`

**Descripción oficial:**

Fix a given vehicle.
If the vehicle's engine's broken then you cannot fix it with this native.

**Ejemplo (lua):**

```lua
-- Get the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is in
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- If the player is not in a vehicle, return
if (vehicle == 0) then return end 

-- Fix the vehicle
SetVehicleFixed(vehicle)
```

**Ejemplo (js):**

```js
// Get the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is in
const vehicle = GetVehiclePedIsIn(playerPed, false);

// If the player is not in a vehicle, return
if (vehicle === 0) return;

// Fix the vehicle
SetVehicleFixed(vehicle);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

// Get the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is in
int vehicle = GetVehiclePedIsIn(playerPed, false);

// If the player is not in a vehicle, return
if (vehicle == 0) return; 

// Fix the vehicle
SetVehicleFixed(vehicle);
```

---
### SetVehicleFlightNozzlePosition

`SET_VEHICLE_FLIGHT_NOZZLE_POSITION` · hash `0x30D779DE7C4F6DD3` · jhash `0xA7DF64D7` · **Cliente**

```lua
SetVehicleFlightNozzlePosition(vehicle, angleRatio)
```
```c
void SET_VEHICLE_FLIGHT_NOZZLE_POSITION(Vehicle vehicle, float angleRatio);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `angleRatio` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x30D779DE7C4F6DD3` (`N_0x30d779de7c4f6dd3`), `_SET_DESIRED_VERTICAL_FLIGHT_PHASE` (`SetDesiredVerticalFlightPhase`), `_SET_PLANE_VTOL_DESIRED_DIRECTION` (`SetPlaneVtolDesiredDirection`)

---
### SetVehicleFlightNozzlePositionImmediate

`SET_VEHICLE_FLIGHT_NOZZLE_POSITION_IMMEDIATE` · hash `0x9AA47FFF660CB932` · jhash `0xDD7936F5` · **Cliente**

```lua
SetVehicleFlightNozzlePositionImmediate(vehicle, angle)
```
```c
void SET_VEHICLE_FLIGHT_NOZZLE_POSITION_IMMEDIATE(Vehicle vehicle, float angle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `angle` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9AA47FFF660CB932` (`N_0x9aa47fff660cb932`), `_SET_VERTICAL_FLIGHT_PHASE` (`SetVerticalFlightPhase`), `_SET_PLANE_VTOL_DIRECTION` (`SetPlaneVtolDirection`)

---
### SetVehicleForceAfterburner

`SET_VEHICLE_FORCE_AFTERBURNER` · hash `0xB055A34527CB8FD7` · jhash `0xC195803B` · **Cliente**

```lua
SetVehicleForceAfterburner(vehicle, toggle)
```
```c
void SET_VEHICLE_FORCE_AFTERBURNER(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB055A34527CB8FD7` (`N_0xb055a34527cb8fd7`)

---
### SetVehicleForwardSpeed

`SET_VEHICLE_FORWARD_SPEED` · hash `0xAB54A438726D25D5` · jhash `0x69880D14` · **Cliente**

```lua
SetVehicleForwardSpeed(vehicle, speed)
```
```c
void SET_VEHICLE_FORWARD_SPEED(Vehicle vehicle, float speed);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `speed` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SCALE: Setting the speed to 30 would result in a speed of roughly 60mph, according to speedometer.  
Speed is in meters per second  
You can convert meters/s to mph here:  
http://www.calculateme.com/Speed/MetersperSecond/ToMilesperHour.htm  
```

---
### SetVehicleFrictionOverride

`SET_VEHICLE_FRICTION_OVERRIDE` · hash `0x1837AF7C627009BA` · jhash `0x32AFD42E` · **Cliente**

```lua
SetVehicleFrictionOverride(vehicle, friction)
```
```c
void SET_VEHICLE_FRICTION_OVERRIDE(Vehicle vehicle, float friction);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `friction` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Seems to be related to the metal parts, not tyres (like i was expecting lol)  
Must be called every tick.  
```

---
### SetVehicleFullbeam

`SET_VEHICLE_FULLBEAM` · hash `0x8B7FD87F0DDB421E` · jhash `0x9C49CC15` · **Cliente**

```lua
SetVehicleFullbeam(vehicle, toggle)
```
```c
void SET_VEHICLE_FULLBEAM(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
It switch to highbeam when p1 is set to true.  
```

---
### SetVehicleGeneratesEngineShockingEvents

`SET_VEHICLE_GENERATES_ENGINE_SHOCKING_EVENTS` · hash `0x279D50DE5652D935` · jhash `0xB3200F72` · **Cliente**

```lua
SetVehicleGeneratesEngineShockingEvents(vehicle, toggle)
```
```c
void SET_VEHICLE_GENERATES_ENGINE_SHOCKING_EVENTS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Allows creation of CEventShockingPlaneFlyby, CEventShockingHelicopterOverhead, and other(?) Shocking events
```

**Nombres antiguos (alias):** `0x279D50DE5652D935` (`N_0x279d50de5652d935`)

---
### SetVehicleGeneratorAreaOfInterest

`SET_VEHICLE_GENERATOR_AREA_OF_INTEREST` · hash `0x9A75585FB2E54FAD` · jhash `0x935A95DA` · **Cliente**

```lua
SetVehicleGeneratorAreaOfInterest(x, y, z, radius)
```
```c
void SET_VEHICLE_GENERATOR_AREA_OF_INTEREST(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`): The X coordinate of the central point of the area of interest.
- `y` (`float`): The Y coordinate of the central point of the area of interest.
- `z` (`float`): The Z coordinate of the central point of the area of interest.
- `radius` (`float`): The radius around the central point, defining the size of the area of interest

**Devuelve:** `void`

**Descripción oficial:**

Specifies an area of interest where cargens will focus on spawning vehicles

You can clear the area of interest with [`CLEAR_VEHICLE_GENERATOR_AREA_OF_INTEREST`](VEHICLE-1.md#clearvehiclegeneratorareaofinterest)

**Nombres antiguos (alias):** `0x9A75585FB2E54FAD` (`N_0x9a75585fb2e54fad`)

**Ejemplo (lua):**

```lua
-- This example sets the area of interest (cargen) to the player's position with a radius of 100.0

-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the coordinates of the player.
local coords = GetEntityCoords(playerPed, false)

-- Set the area of interest to the player's position with a radius of 100.0
SetVehicleGeneratorAreaOfInterest(coords.x, coords.y, coords.z, 100.0)
```

**Ejemplo (js):**

```js
// This example sets the area of interest (cargen) to the player's position with a radius of 100.0

// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the coordinates of the player.
const coords = GetEntityCoords(playerPed, false);

// Set the area of interest to the player's position with a radius of 100.0
SetVehicleGeneratorAreaOfInterest(coords.x, coords.y, coords.z, 100.0);
```

**Ejemplo (cs):**

```cs
// This example sets the area of interest (cargen) to the player's position with a radius of 100.0
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the coordinates of the player.
Vector3 coords = GetEntityCoords(playerPed, false);

// Set the area of interest to the player's position with a radius of 100.0
SetVehicleGeneratorAreaOfInterest(coords.X, coords.Y, coords.Z, 100f);
```

---
### SetVehicleGravity

`SET_VEHICLE_GRAVITY` · hash `0x89F149B6131E57DA` · jhash `0x07B2A6DC` · **Cliente**

```lua
SetVehicleGravity(vehicle, toggle)
```
```c
void SET_VEHICLE_GRAVITY(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleHandbrake

`SET_VEHICLE_HANDBRAKE` · hash `0x684785568EF26A22` · jhash `0xBA729A25` · **Cliente**

```lua
SetVehicleHandbrake(vehicle, toggle)
```
```c
void SET_VEHICLE_HANDBRAKE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleHandlingHashForAi

`_SET_VEHICLE_HANDLING_HASH_FOR_AI` · hash `0x10655FAB9915623D` · **Cliente**

```lua
SetVehicleHandlingHashForAi(vehicle, hash)
```
```c
void _SET_VEHICLE_HANDLING_HASH_FOR_AI(Vehicle vehicle, Hash hash);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x10655FAB9915623D` (`N_0x10655fab9915623d`)

---
### SetVehicleHasBeenDrivenFlag

`SET_VEHICLE_HAS_BEEN_DRIVEN_FLAG` · hash `0x02398B627547189C` · jhash `0x08CD58F9` · **Cliente**

```lua
SetVehicleHasBeenDrivenFlag(vehicle, toggle)
```
```c
void SET_VEHICLE_HAS_BEEN_DRIVEN_FLAG(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x02398B627547189C` (`N_0x02398b627547189c`)

---
### SetVehicleHasBeenOwnedByPlayer

`SET_VEHICLE_HAS_BEEN_OWNED_BY_PLAYER` · hash `0x2B5F9D2AF1F1722D` · jhash `0xB4D3DBFB` · **Cliente**

```lua
SetVehicleHasBeenOwnedByPlayer(vehicle, owned)
```
```c
void SET_VEHICLE_HAS_BEEN_OWNED_BY_PLAYER(Vehicle vehicle, BOOL owned);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `owned` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleHasMutedSirens

`SET_VEHICLE_HAS_MUTED_SIRENS` · hash `0xD8050E0EB60CF274` · jhash `0xC54156A9` · **Cliente**

```lua
SetVehicleHasMutedSirens(vehicle, toggle)
```
```c
void SET_VEHICLE_HAS_MUTED_SIRENS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `DISABLE_VEHICLE_IMPACT_EXPLOSION_ACTIVATION` (`DisableVehicleImpactExplosionActivation`), `_SET_DISABLE_VEHICLE_SIREN_SOUND` (`SetDisableVehicleSirenSound`)

---
### SetVehicleHasStrongAxles

`SET_VEHICLE_HAS_STRONG_AXLES` · hash `0x92F0CF722BC4202F` · jhash `0x0D1CBC65` · **Cliente**

```lua
SetVehicleHasStrongAxles(vehicle, toggle)
```
```c
void SET_VEHICLE_HAS_STRONG_AXLES(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
if true, axles won't bend.  
```

---
### SetVehicleHasUnbreakableLights

`SET_VEHICLE_HAS_UNBREAKABLE_LIGHTS` · hash `0x1AA8A837D2169D94` · jhash `0x009AB49E` · **Cliente**

```lua
SetVehicleHasUnbreakableLights(vehicle, toggle)
```
```c
void SET_VEHICLE_HAS_UNBREAKABLE_LIGHTS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `toggle` (`BOOL`): Set the lights' breakability `true` makes lights unbreakable, `false` allows them to break.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether the vehicle's lights can be broken.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x1AA8A837D2169D94` (`N_0x1aa8a837d2169d94`), `_SET_VEHICLE_LIGHTS_CAN_BE_VISIBLY_DAMAGED` (`SetVehicleLightsCanBeVisiblyDamaged`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if not vehicle then return end

-- Make the vehicle's lights unbreakable
SetVehicleHasUnbreakableLights(vehicle, true)
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!vehicle) return;

// Make the vehicle's lights unbreakable
SetVehicleHasUnbreakableLights(vehicle, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (vehicle == 0) return;

// Make the vehicle's lights unbreakable
SetVehicleHasUnbreakableLights(vehicle, true);
```

---
### SetVehicleHeadlightShadows

`SET_VEHICLE_HEADLIGHT_SHADOWS` · hash `0x1FD09E7390A74D54` · **Cliente**

```lua
SetVehicleHeadlightShadows(vehicle, flag)
```
```c
void SET_VEHICLE_HEADLIGHT_SHADOWS(Vehicle vehicle, int flag);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `flag` (`int`): A value from `eVehicleHeadlightShadowFlags` representing the desired headlight shadow flag.

**Devuelve:** `void`

**Descripción oficial:**

Sets the vehicle headlight shadow flags.

```
NativeDB Introduced: v323
```

```cpp
enum eVehicleHeadlightShadowFlags {
    // Default (Lights can be toggled between off, normal and high beams)
    NO_HEADLIGHT_SHADOWS = 0,
    // Lights Disabled (Lights are fully disabled, cannot be toggled)
    HEADLIGHTS_CAST_DYNAMIC_SHADOWS = 1,
    // Always On (Lights can be toggled between normal and high beams)
    HEADLIGHTS_CAST_STATIC_SHADOWS = 2,
    HEADLIGHTS_CAST_FULL_SHADOWS = 3 
};
```

**Nombres antiguos (alias):** `0x1FD09E7390A74D54` (`N_0x1fd09e7390a74d54`), `_SET_VEHICLE_LIGHTS_MODE` (`SetVehicleLightsMode`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if not vehicle then return end

-- Set the vehicle headlight shadows to cast static shadows (always on)
SetVehicleHeadlightShadows(vehicle, 2)
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!vehicle) return;

// Set the vehicle headlight shadows to cast static shadows (always on)
SetVehicleHeadlightShadows(vehicle, 2);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (vehicle == 0) return;

// Set the vehicle headlight shadows to cast static shadows (always on)
SetVehicleHeadlightShadows(vehicle, 2);
```

---
### SetVehicleInactiveDuringPlayback

`SET_VEHICLE_INACTIVE_DURING_PLAYBACK` · hash `0x06582AFF74894C75` · jhash `0x50F89338` · **Cliente**

```lua
SetVehicleInactiveDuringPlayback(vehicle, toggle)
```
```c
void SET_VEHICLE_INACTIVE_DURING_PLAYBACK(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x06582AFF74894C75` (`N_0x06582aff74894c75`)

---
### SetVehicleIndicatorLights

`SET_VEHICLE_INDICATOR_LIGHTS` · hash `0xB5D45264751B7DF0` · jhash `0xA6073B5D` · **Cliente**

```lua
SetVehicleIndicatorLights(vehicle, turnSignal, toggle)
```
```c
void SET_VEHICLE_INDICATOR_LIGHTS(Vehicle vehicle, int turnSignal, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `turnSignal` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the turn signal enabled for a vehicle.  
Set turnSignal to 1 for left light, 0 for right light.  
```

---
### SetVehicleIndividualDoorsLocked

`SET_VEHICLE_INDIVIDUAL_DOORS_LOCKED` · hash `0xBE70724027F85BCD` · jhash `0xD61D182D` · **Cliente**

```lua
SetVehicleIndividualDoorsLocked(vehicle, doorIndex, doorLockStatus)
```
```c
void SET_VEHICLE_INDIVIDUAL_DOORS_LOCKED(Vehicle vehicle, int doorIndex, int doorLockStatus);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`): See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](#setvehicledoorshut)
- `doorLockStatus` (`int`): See eCarLock declared in [`SET_VEHICLE_DOORS_LOCKED`](../cfx/servidor.md#setvehicledoorslocked)

**Devuelve:** `void`

**Nombres antiguos (alias):** `SET_PED_TARGETTABLE_VEHICLE_DESTROY` (`SetPedTargettableVehicleDestroy`), `_SET_VEHICLE_DOOR_DESTROY_TYPE` (`SetVehicleDoorDestroyType`)

---
### SetVehicleInfluencesWantedLevel

`SET_VEHICLE_INFLUENCES_WANTED_LEVEL` · hash `0x0AD9E8F87FF7C16F` · jhash `0x04F5546C` · **Cliente**

```lua
SetVehicleInfluencesWantedLevel(vehicle, influenceWantedLevel)
```
```c
void SET_VEHICLE_INFLUENCES_WANTED_LEVEL(Vehicle vehicle, BOOL influenceWantedLevel);
```

**Parámetros**

- `vehicle` (`Vehicle`): The specific vehicle to be set for influencing the wanted level.
- `influenceWantedLevel` (`BOOL`): A boolean value. Set to `true` to make the vehicle influence the wanted level; `false` to prevent it from doing so.

**Devuelve:** `void`

**Descripción oficial:**

This native sets whether a specific vehicle influences the player's wanted level when it is involved in an incident that typically triggers a wanted response, such as being marked as a "victim" vehicle.

This is particularly useful when utilizing the wanted system from GTA, and you want to prevent a vehicle from affecting the wanted level when it is stolen. In the decompiled scripts this native is only used to disable the influence of the vehicle on the wanted level.

**Nombres antiguos (alias):** `0x0AD9E8F87FF7C16F` (`N_0x0ad9e8f87ff7c16f`)

**Ejemplo (lua):**

```lua
-- This example will prevent the closest vehicle from influencing the wanted level.

-- Retrieve the LocalPlayer
local playerPed = PlayerPedId()

-- Retrieve the coordinates of the player.
local playerCoords = GetEntityCoords(playerPed)

-- Retrieve the closest vehicle.
local vehicle = GetClosestVehicle(playerCoords.x, playerCoords.y, playerCoords.z, 3, 0, 70)

-- Check if the vehicle exists in the game world.
if not DoesEntityExist(vehicle) then 
    -- If the vehicle does not exist, end the execution of the code here.
    return 
end

-- Set the vehicle to not influence the wanted level.
SetVehicleInfluencesWantedLevel(vehicle, false)
```

**Ejemplo (js):**

```js
// This example will prevent the closest vehicle from influencing the wanted level.

// Retrieve the LocalPlayer
const playerPed = PlayerPedId();

// Retrieve the coordinates of the player.
const [playerX, playerY, playerZ] = GetEntityCoords(playerPed);

// Retrieve the closest vehicle.
const vehicle = GetClosestVehicle(playerX, playerY, playerZ, 3, 0, 70)

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
  // If the vehicle does not exist, end the execution of the code here.
  return;
}

// Set the vehicle to not influence the wanted level.
SetVehicleInfluencesWantedLevel(vehicle, false);
```

**Ejemplo (cs):**

```cs
// This example will prevent the closest vehicle from influencing the wanted level.
using static CitizenFX.Core.Native.API;

// Retrieve the LocalPlayer
int playerPed = PlayerPedId();

// Retrive the coordinates of the player.
Vector3 playerCoords = GetEntityCoords(playerPed);

// Retrieve the closest vehicle.
int vehicle = GetClosestVehicle(playerCoords.X, playerCoords.Y, playerCoords.Z, 3, 0, 70);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle))
{
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// Set the vehicle to not influence the wanted level.
SetVehicleInfluencesWantedLevel(vehicle, false);
```

---
### SetVehicleInteriorColor

`_SET_VEHICLE_INTERIOR_COLOR` · hash `0xF40DD601A65F7F19` · **Cliente**

```lua
SetVehicleInteriorColor(vehicle, color)
```
```c
void _SET_VEHICLE_INTERIOR_COLOR(Vehicle vehicle, int color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `color` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_VEHICLE_INTERIOR_COLOUR` (`SetVehicleInteriorColour`)

---
### SetVehicleInteriorlight

`SET_VEHICLE_INTERIORLIGHT` · hash `0xBC2042F090AF6AD3` · jhash `0x9AD1FE1E` · **Cliente**

```lua
SetVehicleInteriorlight(vehicle, toggle)
```
```c
void SET_VEHICLE_INTERIORLIGHT(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleIsConsideredByPlayer

`SET_VEHICLE_IS_CONSIDERED_BY_PLAYER` · hash `0x31B927BBC44156CD` · jhash `0x14413319` · **Cliente**

```lua
SetVehicleIsConsideredByPlayer(vehicle, toggle)
```
```c
void SET_VEHICLE_IS_CONSIDERED_BY_PLAYER(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Setting this to false, makes the specified vehicle to where if you press Y your character doesn't even attempt the animation to enter the vehicle. Hence it's not considered aka ignored.  
```

---
### SetVehicleIsRacing

`SET_VEHICLE_IS_RACING` · hash `0x07116E24E9D1929D` · jhash `0xA59E3DCD` · **Cliente**

```lua
SetVehicleIsRacing(vehicle, toggle)
```
```c
void SET_VEHICLE_IS_RACING(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 (toggle) was always 1 (true) except in one case in the b678 scripts.  
```

**Nombres antiguos (alias):** `STEER_UNLOCK_BIAS` (`SteerUnlockBias`)

---
### SetVehicleIsStolen

`SET_VEHICLE_IS_STOLEN` · hash `0x67B2C79AA7FF5738` · jhash `0x70912E42` · **Cliente**

```lua
SetVehicleIsStolen(vehicle, isStolen)
```
```c
void SET_VEHICLE_IS_STOLEN(Vehicle vehicle, BOOL isStolen);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `isStolen` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleIsWanted

`SET_VEHICLE_IS_WANTED` · hash `0xF7EC25A3EBEEC726` · jhash `0xDAA388E8` · **Cliente**

```lua
SetVehicleIsWanted(vehicle, state)
```
```c
void SET_VEHICLE_IS_WANTED(Vehicle vehicle, BOOL state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the wanted state of this vehicle.  
```

---
### SetVehicleKeepEngineOnWhenAbandoned

`SET_VEHICLE_KEEP_ENGINE_ON_WHEN_ABANDONED` · hash `0xB8FBC8B1330CA9B4` · jhash `0x51E0064F` · **Cliente**

```lua
SetVehicleKeepEngineOnWhenAbandoned(vehicle, toggle)
```
```c
void SET_VEHICLE_KEEP_ENGINE_ON_WHEN_ABANDONED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `toggle` (`BOOL`): `true` to keep the engine on, otherwise `false`.

**Devuelve:** `void`

**Descripción oficial:**

Calling this native will keep a vehicle's engine running after exiting.

**Nombres antiguos (alias):** `0xB8FBC8B1330CA9B4` (`N_0xb8fbc8b1330ca9b4`), `_SET_VEHICLE_JET_ENGINE_ON` (`SetVehicleJetEngineOn`)

---
### SetVehicleKersAllowed

`SET_VEHICLE_KERS_ALLOWED` · hash `0x99C82F8A139F3E4E` · jhash `0x71CDD52F` · **Cliente**

```lua
SetVehicleKersAllowed(vehicle, toggle)
```
```c
void SET_VEHICLE_KERS_ALLOWED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x99C82F8A139F3E4E` (`N_0x99c82f8a139f3e4e`), `_SET_VEHICLE_HUD_SPECIAL_ABILITY_BAR_ACTIVE` (`SetVehicleHudSpecialAbilityBarActive`)

---
### SetVehicleLightMultiplier

`SET_VEHICLE_LIGHT_MULTIPLIER` · hash `0xB385454F8791F57C` · jhash `0x48039D6A` · **Cliente**

```lua
SetVehicleLightMultiplier(vehicle, multiplier)
```
```c
void SET_VEHICLE_LIGHT_MULTIPLIER(Vehicle vehicle, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `multiplier` (`float`): The multiplier applied to the vehicle's headlights.

**Devuelve:** `void`

**Descripción oficial:**

This multiplier has no limit, by default the game has this set to `1.0`.

---
### SetVehicleLights

`SET_VEHICLE_LIGHTS` · hash `0x34E710FF01247C5A` · jhash `0xE8930226` · **Cliente**

```lua
SetVehicleLights(vehicle, state)
```
```c
void SET_VEHICLE_LIGHTS(Vehicle vehicle, int state);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `state` (`int`): A value from `eVehicleLightSetting` representing the desired light setting.

**Devuelve:** `void`

**Descripción oficial:**

Sets the vehicle lights state. Allowing for different lighting modes.

```
NativeDB Introduced: v323
```

```cpp
enum eVehicleLightSetting {
    // Normal light behavior. Lights cycle through off, then low beams, then high beams.
    // Note: It's affected by day or night; high beams don't exist in daytime.
    NO_VEHICLE_LIGHT_OVERRIDE = 0,
    // Vehicle doesn't have lights, always off.
    FORCE_VEHICLE_LIGHTS_OFF  = 1, 
    // Vehicle has always-on lights.
    // During day: Cycles between low beams and high beams. 
    // At night: Cycles between low beams, low beams, and high beams.
    FORCE_VEHICLE_LIGHTS_ON   = 2,
    // Sets vehicle lights on. Behaves like normal lights (same as 0).
    SET_VEHICLE_LIGHTS_ON     = 3,
    // Sets vehicle lights off. Behaves like normal lights (same as 0).
    SET_VEHICLE_LIGHTS_OFF    = 4 
};
```

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if not vehicle then return end

-- Set the vehicle lights to always on
SetVehicleLights(vehicle, 2)
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!vehicle) return;

// Set the vehicle lights to always on
SetVehicleLights(vehicle, 2);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (vehicle == 0) return;

// Set the vehicle lights to always on
SetVehicleLights(vehicle, 2);
```

---
### SetVehicleLivery

`SET_VEHICLE_LIVERY` · hash `0x60BF608F1B8CD1B6` · jhash `0x7AD87059` · **Cliente**

```lua
SetVehicleLivery(vehicle, livery)
```
```c
void SET_VEHICLE_LIVERY(Vehicle vehicle, int livery);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `livery` (`int`)

**Devuelve:** `void`

---
### SetVehicleLodMultiplier

`SET_VEHICLE_LOD_MULTIPLIER` · hash `0x93AE6A61BE015BF1` · jhash `0x569E5AE3` · **Cliente**

```lua
SetVehicleLodMultiplier(vehicle, multiplier)
```
```c
void SET_VEHICLE_LOD_MULTIPLIER(Vehicle vehicle, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `multiplier` (`float`)

**Devuelve:** `void`

---
### SetVehicleMaxSpeed

`_SET_VEHICLE_MAX_SPEED` · hash `0xBAA045B4E42F3C06` · **Cliente**

```lua
SetVehicleMaxSpeed(vehicle, speed)
```
```c
void _SET_VEHICLE_MAX_SPEED(Vehicle vehicle, float speed);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `speed` (`float`): The speed limit in meters per second.

**Devuelve:** `void`

**Descripción oficial:**

To reset the max speed, set the `speed` value to `0.0` or lower.

**Nombres antiguos (alias):** `0xBAA045B4E42F3C06` (`N_0xbaa045b4e42f3c06`)

---
### SetVehicleMod

`SET_VEHICLE_MOD` · hash `0x6AF0636DDEDCB6DD` · jhash `0xB52E5ED5` · **Cliente**

```lua
SetVehicleMod(vehicle, modType, modIndex, customTires)
```
```c
void SET_VEHICLE_MOD(Vehicle vehicle, int modType, int modIndex, BOOL customTires);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`)
- `modIndex` (`int`)
- `customTires` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
// eVehicleModType values modified to conform to script native reorganization (see 0x140D25327 in 1604).
enum eVehicleModType
{
	VMT_SPOILER = 0,
	VMT_BUMPER_F = 1,
	VMT_BUMPER_R = 2,
	VMT_SKIRT = 3,
	VMT_EXHAUST = 4,
	VMT_CHASSIS = 5,
	VMT_GRILL = 6,
	VMT_BONNET = 7,
	VMT_WING_L = 8,
	VMT_WING_R = 9,
	VMT_ROOF = 10,
	VMT_ENGINE = 11,
	VMT_BRAKES = 12,
	VMT_GEARBOX = 13,
	VMT_HORN = 14,
	VMT_SUSPENSION = 15,
	VMT_ARMOUR = 16,
	VMT_NITROUS = 17,
	VMT_TURBO = 18,
	VMT_SUBWOOFER = 19,
	VMT_TYRE_SMOKE = 20,
	VMT_HYDRAULICS = 21,
	VMT_XENON_LIGHTS = 22,
	VMT_WHEELS = 23,
	VMT_WHEELS_REAR_OR_HYDRAULICS = 24,
	VMT_PLTHOLDER = 25,
	VMT_PLTVANITY = 26,
	VMT_INTERIOR1 = 27,
	VMT_INTERIOR2 = 28,
	VMT_INTERIOR3 = 29,
	VMT_INTERIOR4 = 30,
	VMT_INTERIOR5 = 31,
	VMT_SEATS = 32,
	VMT_STEERING = 33,
	VMT_KNOB = 34,
	VMT_PLAQUE = 35,
	VMT_ICE = 36,
	VMT_TRUNK = 37,
	VMT_HYDRO = 38,
	VMT_ENGINEBAY1 = 39,
	VMT_ENGINEBAY2 = 40,
	VMT_ENGINEBAY3 = 41,
	VMT_CHASSIS2 = 42,
	VMT_CHASSIS3 = 43,
	VMT_CHASSIS4 = 44,
	VMT_CHASSIS5 = 45,
	VMT_DOOR_L = 46,
	VMT_DOOR_R = 47,
	VMT_LIVERY_MOD = 48,
	VMT_LIGHTBAR = 49,
};
```

---
### SetVehicleModColor_1

`SET_VEHICLE_MOD_COLOR_1` · hash `0x43FEB945EE7F85B8` · jhash `0xCBE9A54D` · **Cliente**

```lua
SetVehicleModColor_1(vehicle, paintType, color, pearlescentColor)
```
```c
void SET_VEHICLE_MOD_COLOR_1(Vehicle vehicle, int paintType, int color, int pearlescentColor);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `paintType` (`int`)
- `color` (`int`)
- `pearlescentColor` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
paintType:  
0: Normal  
1: Metallic  
2: Pearl  
3: Matte  
4: Metal  
5: Chrome  
color: number of the color.  
p3 seems to always be 0.  
```

---
### SetVehicleModColor_2

`SET_VEHICLE_MOD_COLOR_2` · hash `0x816562BADFDEC83E` · jhash `0xC32613C2` · **Cliente**

```lua
SetVehicleModColor_2(vehicle, paintType, color)
```
```c
void SET_VEHICLE_MOD_COLOR_2(Vehicle vehicle, int paintType, int color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `paintType` (`int`)
- `color` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Changes the secondary paint type and color  
paintType:  
0: Normal  
1: Metallic  
2: Pearl  
3: Matte  
4: Metal  
5: Chrome  
color: number of the color  
```

---
### SetVehicleModKit

`SET_VEHICLE_MOD_KIT` · hash `0x1F2AA07F00B3217A` · jhash `0xB8132158` · **Cliente**

```lua
SetVehicleModKit(vehicle, modKit)
```
```c
void SET_VEHICLE_MOD_KIT(Vehicle vehicle, int modKit);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modKit` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Set modKit to 0 if you plan to call SET_VEHICLE_MOD. That's what the game does. Most body modifications through SET_VEHICLE_MOD will not take effect until this is set to 0.
```

---
### SetVehicleModelIsSuppressed

`SET_VEHICLE_MODEL_IS_SUPPRESSED` · hash `0x0FC2D89AC25A5814` · jhash `0x42A08C9B` · **Cliente**

```lua
SetVehicleModelIsSuppressed(model, suppressed)
```
```c
void SET_VEHICLE_MODEL_IS_SUPPRESSED(Hash model, BOOL suppressed);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `suppressed` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
seems to make the vehicle stop spawning naturally in traffic. Here's an essential example:  
VEHICLE::SET_VEHICLE_MODEL_IS_SUPPRESSED(GAMEPLAY::GET_HASH_KEY("taco"), true);  
```

---
### SetVehicleNameDebug

`SET_VEHICLE_NAME_DEBUG` · hash `0xBFDF984E2C22B94F` · jhash `0xA712FF5C` · **Cliente**

```lua
SetVehicleNameDebug(vehicle, name)
```
```c
void SET_VEHICLE_NAME_DEBUG(Vehicle vehicle, char* name);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle id.
- `name` (`char*`): Debug name.

**Devuelve:** `void`

**Descripción oficial:**

This method is utilized solely for debugging purposes and is functional only in debug builds of the game. Please note that its functionality may not be available in the retail version.

---
### SetVehicleNeedsToBeHotwired

`SET_VEHICLE_NEEDS_TO_BE_HOTWIRED` · hash `0xFBA550EA44404EE6` · jhash `0xD8260751` · **Cliente**

```lua
SetVehicleNeedsToBeHotwired(vehicle, toggle)
```
```c
void SET_VEHICLE_NEEDS_TO_BE_HOTWIRED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleNeonLightEnabled

`_SET_VEHICLE_NEON_LIGHT_ENABLED` · hash `0x2AA720E4287BF269` · **Cliente**

```lua
SetVehicleNeonLightEnabled(vehicle, index, toggle)
```
```c
void _SET_VEHICLE_NEON_LIGHT_ENABLED(Vehicle vehicle, int index, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `index` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the neon lights of the specified vehicle on/off.  
Indices:  
0 = Left  
1 = Right  
2 = Front  
3 = Back  
```

---
### SetVehicleNeonLightsColor_2

`_SET_VEHICLE_NEON_LIGHTS_COLOR_2` · hash `0xB93B2867F7B479D1` · **Cliente**

```lua
SetVehicleNeonLightsColor_2(vehicle, color)
```
```c
void _SET_VEHICLE_NEON_LIGHTS_COLOR_2(Vehicle vehicle, int color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `color` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### SetVehicleNeonLightsColour

`_SET_VEHICLE_NEON_LIGHTS_COLOUR` · hash `0x8E0A582209A62695` · **Cliente**

```lua
SetVehicleNeonLightsColour(vehicle, r, g, b)
```
```c
void _SET_VEHICLE_NEON_LIGHTS_COLOUR(Vehicle vehicle, int r, int g, int b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the color of the neon lights on the specified vehicle.

RGB values and colour names taken from the decompiled scripts:

| Colour         |  R  |  G  |  B  |
|---------------|:---:|:---:|:---:|
| White         | 222 | 222 | 255 |
| Blue          | 2   | 21  | 255 |
| Electric Blue | 3   | 83  | 255 |
| Mint Green    | 0   | 255 | 140 |
| Lime Green    | 94  | 255 | 1   |
| Yellow        | 255 | 255 | 0   |
| Golden Shower | 255 | 150 | 0   |
| Orange        | 255 | 62  | 0   |
| Red           | 255 | 1   | 1   |
| Pony Pink     | 255 | 50  | 100 |
| Hot Pink      | 255 | 5   | 190 |
| Purple        | 35  | 1   | 255 |
| Blacklight    | 15  | 3   | 255 |

---
### SetVehicleNumberPlateText

`SET_VEHICLE_NUMBER_PLATE_TEXT` · hash `0x95A88F0B409CDA47` · jhash `0x400F9556` · **Cliente · también en el servidor (RPC)**

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

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local vehicle = GetVehiclePedIsIn(playerPed)
SetVehicleNumberPlateText(vehicle, "KING")
```

---
### SetVehicleNumberPlateTextIndex

`SET_VEHICLE_NUMBER_PLATE_TEXT_INDEX` · hash `0x9088EB5A43FFB0A1` · jhash `0xA1A1890E` · **Cliente**

```lua
SetVehicleNumberPlateTextIndex(vehicle, plateIndex)
```
```c
void SET_VEHICLE_NUMBER_PLATE_TEXT_INDEX(Vehicle vehicle, int plateIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `plateIndex` (`int`): The style to use for the plate, see plate styles.

**Devuelve:** `void`

**Descripción oficial:**

Please refer to [`GET_VEHICLE_NUMBER_PLATE_TEXT_INDEX`](../cfx/servidor.md#getvehiclenumberplatetextindex) for plate indicies.

---
### SetVehicleOnGroundProperly

`SET_VEHICLE_ON_GROUND_PROPERLY` · hash `0x49733E92263139D1` · jhash `0xE14FDBA6` · **Cliente**

```lua
local retval = SetVehicleOnGroundProperly(vehicle)
```
```c
BOOL SET_VEHICLE_ON_GROUND_PROPERLY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Sets a vehicle on the ground on all wheels.  Returns whether or not the operation was successful.  
```

```
NativeDB Added Parameter 2: float p1
```

---
### SetVehicleOutOfControl

`SET_VEHICLE_OUT_OF_CONTROL` · hash `0xF19D095E42D430CC` · jhash `0x3764D734` · **Cliente**

```lua
SetVehicleOutOfControl(vehicle, killDriver, explodeOnImpact)
```
```c
void SET_VEHICLE_OUT_OF_CONTROL(Vehicle vehicle, BOOL killDriver, BOOL explodeOnImpact);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `killDriver` (`BOOL`)
- `explodeOnImpact` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Tested on the player's current vehicle. Unless you kill the driver, the vehicle doesn't loose control, however, if enabled, explodeOnImpact is still active. The moment you crash, boom.  
```

---
### SetVehicleParachuteActive

`_SET_VEHICLE_PARACHUTE_ACTIVE` · hash `0x0BFFB028B3DD0A97` · **Cliente**

```lua
SetVehicleParachuteActive(vehicle, active)
```
```c
void _SET_VEHICLE_PARACHUTE_ACTIVE(Vehicle vehicle, BOOL active);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `active` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleParachuteModel

`_SET_VEHICLE_PARACHUTE_MODEL` · hash `0x4D610C6B56031351` · **Cliente**

```lua
SetVehicleParachuteModel(vehicle, modelHash)
```
```c
void _SET_VEHICLE_PARACHUTE_MODEL(Vehicle vehicle, Hash modelHash);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
parachuteModel = 230075693  
```

**Nombres antiguos (alias):** `_VEHICLE_SET_CUSTOM_PARACHUTE_MODEL` (`VehicleSetCustomParachuteModel`)

---
### SetVehicleParachuteTextureVariation

`_SET_VEHICLE_PARACHUTE_TEXTURE_VARIATION` · hash `0xA74AD2439468C883` · **Cliente**

```lua
SetVehicleParachuteTextureVariation(vehicle, textureVariation)
```
```c
void _SET_VEHICLE_PARACHUTE_TEXTURE_VARIATION(Vehicle vehicle, int textureVariation);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `textureVariation` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
colorIndex = 0 - 7
```

**Nombres antiguos (alias):** `_VEHICLE_SET_CUSTOM_PARACHUTE_TEXTURE` (`VehicleSetCustomParachuteTexture`), `_SET_VEHICLE_PARACHUTE_TEXTURE_VARIATIION` (`SetVehicleParachuteTextureVariatiion`)

---
### SetVehiclePetrolTankHealth

`SET_VEHICLE_PETROL_TANK_HEALTH` · hash `0x70DB57649FA8D0D8` · jhash `0x660A3692` · **Cliente**

```lua
SetVehiclePetrolTankHealth(vehicle, health)
```
```c
void SET_VEHICLE_PETROL_TANK_HEALTH(Vehicle vehicle, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `health` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
1000 is max health  
Begins leaking gas at around 650 health  
```

---
### SetVehicleProvidesCover

`SET_VEHICLE_PROVIDES_COVER` · hash `0x5AFEEDD9BB2899D7` · jhash `0xEFC01CA9` · **Cliente**

```lua
SetVehicleProvidesCover(vehicle, toggle)
```
```c
void SET_VEHICLE_PROVIDES_COVER(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleRampLaunchModifier

`_SET_VEHICLE_RAMP_LAUNCH_MODIFIER` · hash `0xEFC13B1CE30D755D` · **Cliente**

```lua
SetVehicleRampLaunchModifier(vehicle, p1)
```
```c
void _SET_VEHICLE_RAMP_LAUNCH_MODIFIER(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEFC13B1CE30D755D` (`N_0xefc13b1ce30d755d`)

---
### SetVehicleRampSidewaysLaunchMotion

`_SET_VEHICLE_RAMP_SIDEWAYS_LAUNCH_MOTION` · hash `0x1BBAC99C0BC53656` · **Cliente**

```lua
SetVehicleRampSidewaysLaunchMotion(vehicle, toggle)
```
```c
void _SET_VEHICLE_RAMP_SIDEWAYS_LAUNCH_MOTION(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1BBAC99C0BC53656` (`N_0x1bbac99c0bc53656`)

---
### SetVehicleRampUpwardsLaunchMotion

`_SET_VEHICLE_RAMP_UPWARDS_LAUNCH_MOTION` · hash `0x756AE6E962168A04` · **Cliente**

```lua
SetVehicleRampUpwardsLaunchMotion(vehicle, toggle)
```
```c
void _SET_VEHICLE_RAMP_UPWARDS_LAUNCH_MOTION(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x756AE6E962168A04` (`N_0x756ae6e962168a04`)

---
### SetVehicleReceivesRampDamage

`_SET_VEHICLE_RECEIVES_RAMP_DAMAGE` · hash `0x28D034A93FE31BF5` · **Cliente**

```lua
SetVehicleReceivesRampDamage(vehicle, toggle)
```
```c
void _SET_VEHICLE_RECEIVES_RAMP_DAMAGE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_RAMP_VEHICLE_RECEIVES_RAMP_DAMAGE` (`SetRampVehicleReceivesRampDamage`)

---
### SetVehicleReduceGrip

`SET_VEHICLE_REDUCE_GRIP` · hash `0x222FF6A823D122E2` · jhash `0x90D3A0D9` · **Cliente**

```lua
SetVehicleReduceGrip(vehicle, toggle)
```
```c
void SET_VEHICLE_REDUCE_GRIP(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Reduces grip significantly so it's hard to go anywhere.  
```

---
### SetVehicleReduceTraction

`_SET_VEHICLE_REDUCE_TRACTION` · hash `0x6DEE944E1EE90CFB` · **Cliente**

```lua
SetVehicleReduceTraction(vehicle, val)
```
```c
void _SET_VEHICLE_REDUCE_TRACTION(Vehicle vehicle, int val);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `val` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Often used in conjunction with: [SET_VEHICLE_REDUCE_GRIP](#setvehiclereducegrip).

```
NativeDB Introduced: v1604
```

**Nombres antiguos (alias):** `0x6DEE944E1EE90CFB` (`N_0x6dee944e1ee90cfb`)

---
### SetVehicleRocketBoostActive

`_SET_VEHICLE_ROCKET_BOOST_ACTIVE` · hash `0x81E1552E35DC3839` · **Cliente**

```lua
SetVehicleRocketBoostActive(vehicle, active)
```
```c
void _SET_VEHICLE_ROCKET_BOOST_ACTIVE(Vehicle vehicle, BOOL active);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `active` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleRocketBoostPercentage

`_SET_VEHICLE_ROCKET_BOOST_PERCENTAGE` · hash `0xFEB2DDED3509562E` · **Cliente**

```lua
SetVehicleRocketBoostPercentage(vehicle, percentage)
```
```c
void _SET_VEHICLE_ROCKET_BOOST_PERCENTAGE(Vehicle vehicle, float percentage);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `percentage` (`float`)

**Devuelve:** `void`

---
### SetVehicleRocketBoostRefillTime

`_SET_VEHICLE_ROCKET_BOOST_REFILL_TIME` · hash `0xE00F2AB100B76E89` · **Cliente**

```lua
SetVehicleRocketBoostRefillTime(vehicle, time)
```
```c
void _SET_VEHICLE_ROCKET_BOOST_REFILL_TIME(Vehicle vehicle, float time);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `time` (`float`)

**Devuelve:** `void`

---
### SetVehicleRoofLivery

`_SET_VEHICLE_ROOF_LIVERY` · hash `0xA6D3A8750DC73270` · **Cliente**

```lua
SetVehicleRoofLivery(vehicle, livery)
```
```c
void _SET_VEHICLE_ROOF_LIVERY(Vehicle vehicle, int livery);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `livery` (`int`): Livery index.

**Devuelve:** `void`

**Descripción oficial:**

Used to set the tornado custom (convertible) rooftop livery.

Livery value that works for tornado custom is between 0 and 9 from what i can tell. Maybe 0-8 even.

Might work on other custom vehicles but im not sure what those might be, only confirmed it working with the tornado custom.

**Nombres antiguos (alias):** `0xA6D3A8750DC73270` (`N_0xa6d3a8750dc73270`)

---
### SetVehicleRudderBroken

`SET_VEHICLE_RUDDER_BROKEN` · hash `0x09606148B6C71DEF` · jhash `0x3FAC3CD4` · **Cliente**

```lua
SetVehicleRudderBroken(vehicle, toggle)
```
```c
void SET_VEHICLE_RUDDER_BROKEN(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleSearchlight

`SET_VEHICLE_SEARCHLIGHT` · hash `0x14E85C5EE7A4D542` · jhash `0xE2C0DD8A` · **Cliente**

```lua
SetVehicleSearchlight(heli, toggle, canBeUsedByAI)
```
```c
void SET_VEHICLE_SEARCHLIGHT(Vehicle heli, BOOL toggle, BOOL canBeUsedByAI);
```

**Parámetros**

- `heli` (`Vehicle`)
- `toggle` (`BOOL`)
- `canBeUsedByAI` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only works during nighttime.
```

---
### SetVehicleShadowEffect

`_SET_VEHICLE_SHADOW_EFFECT` · hash `0xF0E4BA16D1DB546C` · jhash `0x5BD8D82D` · **Cliente**

```lua
SetVehicleShadowEffect(vehicle, p1, p2)
```
```c
void _SET_VEHICLE_SHADOW_EFFECT(Vehicle vehicle, int p1, int p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`int`)
- `p2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Adds some kind of shadow to the vehicle.
-1 disables the effect.
DISABLE_*
```

**Nombres antiguos (alias):** `0xF0E4BA16D1DB546C` (`N_0xf0e4ba16d1db546c`)

---
### SetVehicleShootAtTarget

`SET_VEHICLE_SHOOT_AT_TARGET` · hash `0x74CD9A9327A282EA` · jhash `0x2343FFDF` · **Cliente**

```lua
SetVehicleShootAtTarget(driver, entity, xTarget, yTarget, zTarget)
```
```c
void SET_VEHICLE_SHOOT_AT_TARGET(Ped driver, Entity entity, float xTarget, float yTarget, float zTarget);
```

**Parámetros**

- `driver` (`Ped`)
- `entity` (`Entity`)
- `xTarget` (`float`)
- `yTarget` (`float`)
- `zTarget` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Commands the driver of an armed vehicle (p0) to shoot its weapon at a target (p1). p3, p4 and p5 are the coordinates of the target. Example:  
WEAPON::SET_CURRENT_PED_VEHICLE_WEAPON(pilot,GAMEPLAY::GET_HASH_KEY("VEHICLE_WEAPON_PLANE_ROCKET"));VEHICLE::SET_VEHICLE_SHOOT_AT_TARGET(pilot, target, targPos.x, targPos.y, targPos.z);  
```

---
### SetVehicleSilent

`_SET_VEHICLE_SILENT` · hash `0x9D44FCCE98450843` · jhash `0x968E5770` · **Cliente**

```lua
SetVehicleSilent(vehicle, toggle)
```
```c
void _SET_VEHICLE_SILENT(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If set to TRUE, it seems to suppress door noises and doesn't allow the horn to be continuous.  
```

**Nombres antiguos (alias):** `0x9D44FCCE98450843` (`N_0x9d44fcce98450843`)

---
### SetVehicleSiren

`SET_VEHICLE_SIREN` · hash `0xF4924635A19EB37D` · jhash `0x4AC1EFC7` · **Cliente**

```lua
SetVehicleSiren(vehicle, toggle)
```
```c
void SET_VEHICLE_SIREN(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Activate siren on vehicle (Only works if the vehicle has a siren).  
```

---
### SetVehicleSt

`_SET_VEHICLE_ST` · hash `0x1CF38D529D7441D9` · jhash `0xDF594D8D` · **Cliente**

```lua
SetVehicleSt(vehicle, toggle)
```
```c
void _SET_VEHICLE_ST(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Has something to do with trains. Always precedes SET_MISSION_TRAIN_AS_NO_LONGER_NEEDED.  
============================================  
May be true that it can be used with trains not sure, but not specifically for trains. Go find Xbox360 decompiled scripts and search for 'func_1333' in freemode.c it isn't used just for trains. Thanks for the info tho.  
Btw, func_1333 ends up calling this func which uses this native,  
void func_1338(int iParam0)//Position   
{  
	ENTITY::FREEZE_ENTITY_POSITION(iParam0, true);  
	ENTITY::SET_ENTITY_COLLISION(iParam0, false, 0);  
	ENTITY::SET_ENTITY_INVINCIBLE(iParam0, true);  
	VEHICLE::_0xDF594D8D(iParam0, true);  
}  
```

**Nombres antiguos (alias):** `0x1CF38D529D7441D9` (`N_0x1cf38d529d7441d9`)

---
### SetVehicleSteerBias

`SET_VEHICLE_STEER_BIAS` · hash `0x42A8EC77D5150CBE` · jhash `0x7357C1EB` · **Cliente**

```lua
SetVehicleSteerBias(vehicle, value)
```
```c
void SET_VEHICLE_STEER_BIAS(Vehicle vehicle, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Locks the vehicle's steering to the desired angle, explained below.  
Requires to be called onTick. Steering is unlocked the moment the function stops being called on the vehicle.  
Steer bias:  
-1.0 = full right  
0.0 = centered steering  
1.0 = full left  
```

---
### SetVehicleSteeringBiasScalar

`SET_VEHICLE_STEERING_BIAS_SCALAR` · hash `0x9007A2F21DC108D4` · jhash `0x585E49B6` · **Cliente**

```lua
SetVehicleSteeringBiasScalar(vehicle, scalar)
```
```c
void SET_VEHICLE_STEERING_BIAS_SCALAR(Vehicle vehicle, float scalar);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `scalar` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9007A2F21DC108D4` (`N_0x9007a2f21dc108d4`)

---
### SetVehicleStrong

`SET_VEHICLE_STRONG` · hash `0x3E8C8727991A8A0B` · jhash `0xC758D19F` · **Cliente**

```lua
SetVehicleStrong(vehicle, toggle)
```
```c
void SET_VEHICLE_STRONG(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If set to true, vehicle will not take crash damage, but is still susceptible to damage from bullets and explosives  
```

---
### SetVehicleTankTurretPosition

`SET_VEHICLE_TANK_TURRET_POSITION` · hash `0x56B94C6D7127DFBA` · jhash `0xB1A52EF7` · **Cliente**

```lua
SetVehicleTankTurretPosition(vehicle, position, p2)
```
```c
void SET_VEHICLE_TANK_TURRET_POSITION(Vehicle vehicle, float position, BOOL p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `position` (`float`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x56B94C6D7127DFBA` (`N_0x56b94c6d7127dfba`)

---
### SetVehicleTimedExplosion

`SET_VEHICLE_TIMED_EXPLOSION` · hash `0x2E0A74E1002380B1` · jhash `0xDB8CB8E2` · **Cliente**

```lua
SetVehicleTimedExplosion(vehicle, ped, toggle)
```
```c
void SET_VEHICLE_TIMED_EXPLOSION(Vehicle vehicle, Ped ped, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleTowTruckArmPosition

`SET_VEHICLE_TOW_TRUCK_ARM_POSITION` · hash `0xFE54B92A344583CA` · jhash `0x88236E22` · **Cliente**

```lua
SetVehicleTowTruckArmPosition(vehicle, position)
```
```c
void SET_VEHICLE_TOW_TRUCK_ARM_POSITION(Vehicle vehicle, float position);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `position` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets how much the crane on the tow truck is raised, where 0.0 is fully lowered and 1.0 is fully raised.  
```

**Nombres antiguos (alias):** `_SET_TOW_TRUCK_CRANE_RAISED` (`SetTowTruckCraneRaised`), `_SET_TOW_TRUCK_CRANE_HEIGHT` (`SetTowTruckCraneHeight`)

---
### SetVehicleTurretSpeedThisFrame

`SET_VEHICLE_TURRET_SPEED_THIS_FRAME` · hash `0x1093408B4B9D1146` · jhash `0xF30C566F` · **Cliente**

```lua
SetVehicleTurretSpeedThisFrame(vehicle, speed)
```
```c
void SET_VEHICLE_TURRET_SPEED_THIS_FRAME(Vehicle vehicle, float speed);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `speed` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1093408B4B9D1146` (`N_0x1093408b4b9d1146`)

---
### SetVehicleTurretUnk

`_SET_VEHICLE_TURRET_UNK` · hash `0xC60060EB0D8AC7B1` · **Cliente**

```lua
SetVehicleTurretUnk(vehicle, index, toggle)
```
```c
void _SET_VEHICLE_TURRET_UNK(Vehicle vehicle, int index, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `index` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Toggles specific flag on turret
```

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0xC60060EB0D8AC7B1` (`N_0xc60060eb0d8ac7b1`)

---
### SetVehicleTyreBurst

`SET_VEHICLE_TYRE_BURST` · hash `0xEC6A202EE4960385` · jhash `0x89D28068` · **Cliente**

```lua
SetVehicleTyreBurst(vehicle, index, onRim, p3)
```
```c
void SET_VEHICLE_TYRE_BURST(Vehicle vehicle, int index, BOOL onRim, float p3);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `index` (`int`)
- `onRim` (`BOOL`)
- `p3` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
"To burst tyres VEHICLE::SET_VEHICLE_TYRE_BURST(vehicle, 0, true, 1000.0)  
to burst all tyres type it 8 times where p1 = 0 to 7.  
p3 seems to be how much damage it has taken. 0 doesn't deflate them, 1000 completely deflates them.  
'0 = wheel_lf / bike, plane or jet front  
'1 = wheel_rf  
'2 = wheel_lm / in 6 wheels trailer, plane or jet is first one on left  
'3 = wheel_rm / in 6 wheels trailer, plane or jet is first one on right  
'4 = wheel_lr / bike rear / in 6 wheels trailer, plane or jet is last one on left  
'5 = wheel_rr / in 6 wheels trailer, plane or jet is last one on right  
'45 = 6 wheels trailer mid wheel left  
'47 = 6 wheels trailer mid wheel right  
```

---
### SetVehicleTyreFixed

`SET_VEHICLE_TYRE_FIXED` · hash `0x6E13FC662B882D1D` · jhash `0xA42EFA6B` · **Cliente**

```lua
SetVehicleTyreFixed(vehicle, tyreIndex)
```
```c
void SET_VEHICLE_TYRE_FIXED(Vehicle vehicle, int tyreIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `tyreIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
tyreIndex = 0 to 4 on normal vehicles  
'0 = wheel_lf / bike, plane or jet front  
'1 = wheel_rf  
'2 = wheel_lm / in 6 wheels trailer, plane or jet is first one on left  
'3 = wheel_rm / in 6 wheels trailer, plane or jet is first one on right  
'4 = wheel_lr / bike rear / in 6 wheels trailer, plane or jet is last one on left  
'5 = wheel_rr / in 6 wheels trailer, plane or jet is last one on right  
'45 = 6 wheels trailer mid wheel left  
'47 = 6 wheels trailer mid wheel right  
```

---
### SetVehicleTyreSmokeColor

`SET_VEHICLE_TYRE_SMOKE_COLOR` · hash `0xB5BA80F839791C0F` · jhash `0x3EDEC0DB` · **Cliente**

```lua
SetVehicleTyreSmokeColor(vehicle, r, g, b)
```
```c
void SET_VEHICLE_TYRE_SMOKE_COLOR(Vehicle vehicle, int r, int g, int b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the tire smoke's color of this vehicle.  
vehicle: The vehicle that is the target of this method.  
r: The red level in the RGB color code.  
g: The green level in the RGB color code.  
b: The blue level in the RGB color code.  
Note:  
setting r,g,b to 0 will give the car independance day tyre smoke  
```

---
### SetVehicleTyresCanBurst

`SET_VEHICLE_TYRES_CAN_BURST` · hash `0xEB9DC3C7D8596C46` · jhash `0xA198DB54` · **Cliente**

```lua
SetVehicleTyresCanBurst(vehicle, toggle)
```
```c
void SET_VEHICLE_TYRES_CAN_BURST(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Allows you to toggle bulletproof tires.  
```

---
### SetVehicleUndriveable

`SET_VEHICLE_UNDRIVEABLE` · hash `0x8ABA6AF54B942B95` · jhash `0x48D02A4E` · **Cliente**

```lua
SetVehicleUndriveable(vehicle, toggle)
```
```c
void SET_VEHICLE_UNDRIVEABLE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to modify.
- `toggle` (`BOOL`): `true` to mark the vehicle as undriveable and immediately shut the engine off, `false` allows the vehicle to be driven again.

**Devuelve:** `void`

**Descripción oficial:**

Marks a vehicle as undriveable. While this is set, the engine cannot be started by anyone. Peds can still open the door, sit in the driver seat and close the door and try to start the car, but it will only turn over.

When set to `true`, the engine is forced off instantly even if it was running. A moving vehicle will coast, brakes and steering still respond.

Toggling this to `false` will not restart the engine. The driver must start it again, or you must call [SET_VEHICLE_ENGINE_ON](#setvehicleengineon).

The state is local to each client and is not synced via the network. Every client that has the vehicle in scope needs to apply it.

This flag persists across damage and repair; [SET_VEHICLE_FIXED](#setvehiclefixed) does not clear it. If you set it, you are expected to clear it.

Pair with [SET_VEHICLE_DOORS_LOCKED](../cfx/servidor.md#setvehicledoorslocked) to keep peds out entirely.

Bicycles accept the flag but have no engine to shut off, so the call has no meaningful effect on them.

**Ejemplo (lua):**

```lua
-- /lockengine toggles the undriveable flag on the player's current vehicle
local locked = false
RegisterCommand("lockengine", function()
    local ped = PlayerPedId()
    local vehicle = GetVehiclePedIsIn(ped, false)
    if vehicle == 0 then return end
    locked = not locked
    SetVehicleUndriveable(vehicle, locked)
end, false)
```

**Ejemplo (js):**

```js
// /lockengine toggles the undriveable flag on the player's current vehicle
let locked = false;
RegisterCommand("lockengine", () => {
    const ped = PlayerPedId();
    const vehicle = GetVehiclePedIsIn(ped, false);
    if (vehicle === 0) return;
    locked = !locked;
    SetVehicleUndriveable(vehicle, locked);
}, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// /lockengine toggles the undriveable flag on the player's current vehicle
private bool locked = false;

RegisterCommand("lockengine", new Action<int, List<object>, string>((source, args, raw) =>
{
    int ped = PlayerPedId();
    int vehicle = GetVehiclePedIsIn(ped, false);
    if (vehicle == 0) return;
    locked = !locked;
    SetVehicleUndriveable(vehicle, locked);
}), false);
```

---
### SetVehicleUnkDamageMultiplier

`_SET_VEHICLE_UNK_DAMAGE_MULTIPLIER` · hash `0x45A561A9421AB6AD` · **Cliente**

```lua
SetVehicleUnkDamageMultiplier(vehicle, multiplier)
```
```c
void _SET_VEHICLE_UNK_DAMAGE_MULTIPLIER(Vehicle vehicle, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x45A561A9421AB6AD` (`N_0x45a561a9421ab6ad`)

---
### SetVehicleUseAlternateHandling

`SET_VEHICLE_USE_ALTERNATE_HANDLING` · hash `0x1D97D1E3A70A649F` · jhash `0xA03E42DF` · **Cliente**

```lua
SetVehicleUseAlternateHandling(vehicle, toggle)
```
```c
void SET_VEHICLE_USE_ALTERNATE_HANDLING(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1D97D1E3A70A649F` (`N_0x1d97d1e3a70a649f`)

---
### SetVehicleUseCutsceneWheelCompression

`SET_VEHICLE_USE_CUTSCENE_WHEEL_COMPRESSION` · hash `0xE023E8AC4EF7C117` · jhash `0xA0909ADB` · **Cliente**

```lua
local retval = SetVehicleUseCutsceneWheelCompression(p0, p1, p2, p3)
```
```c
Any SET_VEHICLE_USE_CUTSCENE_WHEEL_COMPRESSION(Vehicle p0, BOOL p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`Vehicle`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `SET_ALL_VEHICLES_SPAWN` (`SetAllVehiclesSpawn`), `0xE023E8AC4EF7C117` (`N_0xe023e8ac4ef7c117`)

---
### SetVehicleUseHornButtonForNitrous

`_SET_VEHICLE_USE_HORN_BUTTON_FOR_NITROUS` · hash `0x1980F68872CC2C3D` · **Cliente**

```lua
SetVehicleUseHornButtonForNitrous(vehicle, bToggle)
```
```c
void _SET_VEHICLE_USE_HORN_BUTTON_FOR_NITROUS(Vehicle vehicle, BOOL bToggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle where this setting will be applied.
- `bToggle` (`BOOL`): If set to `true`, the horn button will activate the nitrous system; if `false`, it will not.

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3095
```

Enables or disables the use of the vehicle's horn button for activating the nitrous system.

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if vehicle == 0 then return end

-- Enable activating nitrous in the vehicle using the horn button.
SetVehicleUseHornButtonForNitrous(vehicle, true)
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Enable activating nitrous in the vehicle using the horn button.
SetVehicleUseHornButtonForNitrous(vehicle, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Enable activating nitrous in the vehicle using the horn button.
SetVehicleUseHornButtonForNitrous(vehicle, true);
```

---
### SetVehicleUsePlayerLightSettings

`SET_VEHICLE_USE_PLAYER_LIGHT_SETTINGS` · hash `0xC45C27EF50F36ADC` · jhash `0x4221E435` · **Cliente**

```lua
SetVehicleUsePlayerLightSettings(vehicle, toggle)
```
```c
void SET_VEHICLE_USE_PLAYER_LIGHT_SETTINGS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC45C27EF50F36ADC` (`N_0xc45c27ef50f36adc`), `_SET_VEHICLE_USE_PLAYER_LIGHT_SETTINGS` (`SetVehicleUsePlayerLightSettings`)

---
### SetVehicleUsesLargeRearRamp

`SET_VEHICLE_USES_LARGE_REAR_RAMP` · hash `0xCAC66558B944DA67` · jhash `0x0B200CE2` · **Cliente**

```lua
SetVehicleUsesLargeRearRamp(vehicle, toggle)
```
```c
void SET_VEHICLE_USES_LARGE_REAR_RAMP(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
vehicle must be a plane
```

**Nombres antiguos (alias):** `0xCAC66558B944DA67` (`N_0xcac66558b944da67`)

---
### SetVehicleWeaponRestrictedAmmo

`SET_VEHICLE_WEAPON_RESTRICTED_AMMO` · hash `0x44CD1F493DB2A0A6` · **Cliente**

```lua
SetVehicleWeaponRestrictedAmmo(vehicle, weaponIndex, ammoCount)
```
```c
void SET_VEHICLE_WEAPON_RESTRICTED_AMMO(Vehicle vehicle, int weaponIndex, int ammoCount);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle
- `weaponIndex` (`int`): The weapon index we're setting ammo for (between `0` and `3`), see description for more.
- `ammoCount` (`int`): When set positive, will count down with every fire and prevent firing at `0`. Set `-1` to disable restricted ammo.

**Devuelve:** `void`

**Descripción oficial:**

Sets a limited number of ammo for a particular vehicle weapon index on a vehicle.

Information about weapon indexes can be found in `handling.meta`.

In the example given below, `uWeaponHash` defines weapon hashes for the vehicle. Each `<Item>` corresponds to an index starting from `0`.

```
<uWeaponHash>
    <Item>VEHICLE_WEAPON_PLAYER_BUZZARD</Item>  <!-- Index: 0 -->
    <Item>VEHICLE_WEAPON_SPACE_ROCKET</Item>    <!-- Index: 1 -->
    <Item>VEHICLE_WEAPON_SEARCHLIGHT</Item>     <!-- Index: 2 -->
</uWeaponHash>
```

**Nombres antiguos (alias):** `0x44CD1F493DB2A0A6` (`N_0x44cd1f493db2a0a6`), `_SET_VEHICLE_WEAPON_CAPACITY` (`SetVehicleWeaponCapacity`)

---
### SetVehicleWeaponsDisabled

`_SET_VEHICLE_WEAPONS_DISABLED` · hash `0x86B4B6212CB8B627` · **Cliente**

```lua
SetVehicleWeaponsDisabled(vehicle, weaponSlot)
```
```c
void _SET_VEHICLE_WEAPONS_DISABLED(Vehicle vehicle, int weaponSlot);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `weaponSlot` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x86B4B6212CB8B627` (`N_0x86b4b6212cb8b627`)

---
### SetVehicleWheelType

`SET_VEHICLE_WHEEL_TYPE` · hash `0x487EB21CC7295BA1` · jhash `0x64BDAAAD` · **Cliente**

```lua
SetVehicleWheelType(vehicle, wheelType)
```
```c
void SET_VEHICLE_WHEEL_TYPE(Vehicle vehicle, int wheelType);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Refer to [GET_VEHICLE_WHEEL_TYPE](../cfx/servidor.md#getvehiclewheeltype) for wheel types.

---
### SetVehicleWheelsCanBreak

`SET_VEHICLE_WHEELS_CAN_BREAK` · hash `0x29B18B4FD460CA8F` · jhash `0x829ED654` · **Cliente**

```lua
SetVehicleWheelsCanBreak(vehicle, enabled)
```
```c
void SET_VEHICLE_WHEELS_CAN_BREAK(Vehicle vehicle, BOOL enabled);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `enabled` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleWheelsCanBreakOffWhenBlowUp

`SET_VEHICLE_WHEELS_CAN_BREAK_OFF_WHEN_BLOW_UP` · hash `0xA37B9A517B133349` · jhash `0x670913A4` · **Cliente**

```lua
SetVehicleWheelsCanBreakOffWhenBlowUp(vehicle, toggle)
```
```c
void SET_VEHICLE_WHEELS_CAN_BREAK_OFF_WHEN_BLOW_UP(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `SET_VEHICLE_MAX_STR_TRAP` (`SetVehicleMaxStrTrap`)

---
### SetVehicleWheelsDealDamage

`_SET_VEHICLE_WHEELS_DEAL_DAMAGE` · hash `0x2970EAA18FD5E42F` · **Cliente**

```lua
SetVehicleWheelsDealDamage(vehicle, toggle)
```
```c
void _SET_VEHICLE_WHEELS_DEAL_DAMAGE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Related to monster trucks in native scripts.
```

```
NativeDB Introduced: v1604
```

**Nombres antiguos (alias):** `0x2970EAA18FD5E42F` (`N_0x2970eaa18fd5e42f`)

---
### SetVehicleWindowTint

`SET_VEHICLE_WINDOW_TINT` · hash `0x57C51E6BAD752696` · jhash `0x497C8787` · **Cliente**

```lua
SetVehicleWindowTint(vehicle, tint)
```
```c
void SET_VEHICLE_WINDOW_TINT(Vehicle vehicle, int tint);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `tint` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum WindowTints  
{  
	WINDOWTINT_NONE = 0,
	WINDOWTINT_PURE_BLACK = 1,
	WINDOWTINT_DARKSMOKE = 2,
	WINDOWTINT_LIGHTSMOKE = 3,
	WINDOWTINT_STOCK = 4,
	WINDOWTINT_LIMO = 5,
	WINDOWTINT_GREEN = 6
};  
```

---
### SetVehicleXenonLightsColor

`_SET_VEHICLE_XENON_LIGHTS_COLOR` · hash `0xE41033B25D003A07` · **Cliente**

```lua
SetVehicleXenonLightsColor(vehicle, color)
```
```c
void _SET_VEHICLE_XENON_LIGHTS_COLOR(Vehicle vehicle, int color);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `color` (`int`): The paint index.

**Devuelve:** `void`

**Descripción oficial:**

Paint index goes from 0 to 12.

You can find the list of colors and ids here: [\_GET_VEHICLE_HEADLIGHTS_COLOUR](VEHICLE-1.md#getvehiclexenonlightscolor)

**Nombres antiguos (alias):** `0xE41033B25D003A07` (`N_0xe41033b25d003a07`), `_SET_VEHICLE_HEADLIGHTS_COLOUR` (`SetVehicleHeadlightsColour`), `_SET_VEHICLE_XENON_LIGHTS_COLOUR` (`SetVehicleXenonLightsColour`)

**Ejemplo (lua):**

```lua
local veh = GetVehiclePedIsUsing(PlayerPedId())
ToggleVehicleMod(veh, 22, true) -- toggle xenon
SetVehicleHeadlightsColour(veh, 2)
```

---
### SkipTimeInPlaybackRecordedVehicle

`SKIP_TIME_IN_PLAYBACK_RECORDED_VEHICLE` · hash `0x9438F7AD68771A20` · jhash `0xCF3EFA4B` · **Cliente**

```lua
SkipTimeInPlaybackRecordedVehicle(vehicle, time)
```
```c
void SKIP_TIME_IN_PLAYBACK_RECORDED_VEHICLE(Vehicle vehicle, float time);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `time` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_TIME_POSITION_IN_RECORDING can be emulated by: desired_time - GET_TIME_POSITION_IN_RECORDING(vehicle)
```

---
### SkipToEndAndStopPlaybackRecordedVehicle

`SKIP_TO_END_AND_STOP_PLAYBACK_RECORDED_VEHICLE` · hash `0xAB8E2EDA0C0A5883` · jhash `0x8DEA18C8` · **Cliente**

```lua
SkipToEndAndStopPlaybackRecordedVehicle(vehicle)
```
```c
void SKIP_TO_END_AND_STOP_PLAYBACK_RECORDED_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### SmashVehicleWindow

`SMASH_VEHICLE_WINDOW` · hash `0x9E5B5E4D2CCD2259` · jhash `0xDDD9A8C2` · **Cliente**

```lua
SmashVehicleWindow(vehicle, windowIndex)
```
```c
void SMASH_VEHICLE_WINDOW(Vehicle vehicle, int windowIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle id.
- `windowIndex` (`int`): Windows to smash index.

**Devuelve:** `void`

**Descripción oficial:**

Smashes a vehicles window. See eWindowId declared in [`IS_VEHICLE_WINDOW_INTACT`](../cfx/servidor.md#isvehiclewindowintact).

---
### StabiliseEntityAttachedToHeli

`STABILISE_ENTITY_ATTACHED_TO_HELI` · hash `0x374706271354CB18` · jhash `0x40C4763F` · **Cliente**

```lua
StabiliseEntityAttachedToHeli(vehicle, entity, p2)
```
```c
void STABILISE_ENTITY_ATTACHED_TO_HELI(Vehicle vehicle, Entity entity, float p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `entity` (`Entity`)
- `p2` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x374706271354CB18` (`N_0x374706271354cb18`)

---
### StartPlaybackRecordedVehicle

`START_PLAYBACK_RECORDED_VEHICLE` · hash `0x3F878F92B3A7A071` · jhash `0xCF614CA8` · **Cliente**

```lua
StartPlaybackRecordedVehicle(vehicle, recording, script, p3)
```
```c
void START_PLAYBACK_RECORDED_VEHICLE(Vehicle vehicle, int recording, char* script, BOOL p3);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `recording` (`int`)
- `script` (`char*`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

p3 is some flag related to 'trailers' (invokes CVehicle::GetTrailer).

See [`REQUEST_VEHICLE_RECORDING`](VEHICLE-1.md#requestvehiclerecording).

---
### StartPlaybackRecordedVehicleUsingAi

`START_PLAYBACK_RECORDED_VEHICLE_USING_AI` · hash `0x29DE5FA52D00428C` · jhash `0x8DE8E24E` · **Cliente**

```lua
StartPlaybackRecordedVehicleUsingAi(vehicle, recording, script, speed, drivingStyle)
```
```c
void START_PLAYBACK_RECORDED_VEHICLE_USING_AI(Vehicle vehicle, int recording, char* script, float speed, int drivingStyle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `recording` (`int`)
- `script` (`char*`)
- `speed` (`float`)
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](TASK.md#setdrivetaskdrivingstyle)).

**Devuelve:** `void`

**Descripción oficial:**

```
AI abides by the provided driving style (e.g., stopping at red lights or waiting behind traffic) while executing the specificed vehicle recording.

0x1F2E4E06DEA8992B is a related native that deals with the AI physics for such recordings.
```

---
### StartPlaybackRecordedVehicleWithFlags

`START_PLAYBACK_RECORDED_VEHICLE_WITH_FLAGS` · hash `0x7D80FD645D4DA346` · jhash `0x4E721AD2` · **Cliente**

```lua
StartPlaybackRecordedVehicleWithFlags(vehicle, recording, script, flags, time, drivingStyle)
```
```c
void START_PLAYBACK_RECORDED_VEHICLE_WITH_FLAGS(Vehicle vehicle, int recording, char* script, int flags, int time, int drivingStyle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `recording` (`int`)
- `script` (`char*`)
- `flags` (`int`)
- `time` (`int`)
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](TASK.md#setdrivetaskdrivingstyle)).

**Devuelve:** `void`

**Descripción oficial:**

```
flags requires further research, e.g., 0x4/0x8 are related to the AI driving task and 0x20 is internally set and interacts with dynamic entity components.
time, often zero and capped at 500, is related to SET_PLAYBACK_TO_USE_AI_TRY_TO_REVERT_BACK_LATER
```

---
### StartVehicleAlarm

`START_VEHICLE_ALARM` · hash `0xB8FF7AB45305C345` · jhash `0x5B451FF7` · **Cliente**

```lua
StartVehicleAlarm(vehicle)
```
```c
void START_VEHICLE_ALARM(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### StartVehicleHorn

`START_VEHICLE_HORN` · hash `0x9C8C6504B5B63D2C` · jhash `0x0DF5ADB3` · **Cliente**

```lua
StartVehicleHorn(vehicle, duration, mode, forever)
```
```c
void START_VEHICLE_HORN(Vehicle vehicle, int duration, Hash mode, BOOL forever);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle id
- `duration` (`int`): The duration to sound the horn, in milliseconds.
- `mode` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of "NORMAL" or "HELDDOWN". Can be 0.
- `forever` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sounds the horn for the specified vehicle. Note that if a player is in the vehicle, it will only sound briefly.

---
### StopAllGarageActivity

`STOP_ALL_GARAGE_ACTIVITY` · hash `0x0F87E938BDF29D66` · jhash `0x17A0BCE5` · **Cliente**

```lua
StopAllGarageActivity()
```
```c
void STOP_ALL_GARAGE_ACTIVITY();
```

**Devuelve:** `void`

---
### StopBringVehicleToHalt

`_STOP_BRING_VEHICLE_TO_HALT` · hash `0x7C06330BFDDA182E` · **Cliente**

```lua
StopBringVehicleToHalt(vehicle)
```
```c
void _STOP_BRING_VEHICLE_TO_HALT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
Stops CTaskBringVehicleToHalt
```

**Nombres antiguos (alias):** `0x7C06330BFDDA182E` (`N_0x7c06330bfdda182e`)

---
### StopPlaybackRecordedVehicle

`STOP_PLAYBACK_RECORDED_VEHICLE` · hash `0x54833611C17ABDEA` · jhash `0xAE99C57C` · **Cliente**

```lua
StopPlaybackRecordedVehicle(vehicle)
```
```c
void STOP_PLAYBACK_RECORDED_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### SwitchTrainTrack

`SWITCH_TRAIN_TRACK` · hash `0xFD813BB7DB977F20` · jhash `0x68BFDD61` · **Cliente**

```lua
SwitchTrainTrack(trackId, state)
```
```c
void SWITCH_TRAIN_TRACK(int trackId, BOOL state);
```

**Parámetros**

- `trackId` (`int`): The internal id of the train track to switch
- `state` (`BOOL`): Whether ambient trains can spawn or not

**Devuelve:** `void` — None. The original return type is `void`, but ABI compatibility makes this impossible.

**Descripción oficial:**

Toggles whether ambient trains can spawn on the specified track or not.

| trackId | File | Description |
| --- | --- | --- |
| 0 | `trains1.dat` | Main track around SA |
| 1 | `trains2.dat` | Davis Quartz Quarry branch |
| 2 | `trains3.dat` | Second track alongside live track along Roy Lewenstein Blv. |
| 3 | `trains4.dat` | Metro track circuit |
| 4 | `trains5.dat` | Branch in Mirror Park Railyard |
| 5 | `trains6.dat` | Branch in Mirror Park Railyard |
| 6 | `trains7.dat` | LS branch to Mirror Park Railyard |
| 7 | `trains8.dat` | Overground part of metro track along Forum Dr. |
| 8 | `trains9.dat` | Branch to Mirror Park Railyard |
| 9 | `trains10.dat` | Yankton train |
| 10 | `trains11.dat` | Part of metro track near mission row |
| 11 | `trains12.dat` | Yankton prologue mission train |

Tracks IDs `0` and `3` are the main tracks you find trains on during normal gameplay, all the others are used during missions and are not complete tracks.

---
### ToggleVehicleMod

`TOGGLE_VEHICLE_MOD` · hash `0x2A1F4F37F95BAD08` · jhash `0xD095F811` · **Cliente**

```lua
ToggleVehicleMod(vehicle, modType, toggle)
```
```c
void TOGGLE_VEHICLE_MOD(Vehicle vehicle, int modType, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](#setvehiclemod).
- `toggle` (`BOOL`): A bool indicating whether the mod should be enabled/disabled (true/false)

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables a vehicle mod by index (`modType`) for a given vehicle.

`eVehicleModType` enum, used for `modType` index can be found under [`SET_VEHICLE_MOD`](#setvehiclemod).

---
### TrackVehicleVisibility

`TRACK_VEHICLE_VISIBILITY` · hash `0x64473AEFDCF47DCA` · jhash `0x78122DC1` · **Cliente**

```lua
TrackVehicleVisibility(vehicle)
```
```c
void TRACK_VEHICLE_VISIBILITY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
in script hook .net   
Vehicle v = ...;  
Function.Call(Hash.TRACK_VEHICLE_VISIBILITY, v.Handle);  
```

---
### TransformToCar

`TRANSFORM_TO_CAR` · hash `0x2A69FFD1B42BFF9E` · jhash `0xD8B90941` · **Cliente**

```lua
TransformToCar(vehicle, instantly)
```
```c
void TRANSFORM_TO_CAR(Vehicle vehicle, BOOL instantly);
```

**Parámetros**

- `vehicle` (`Vehicle`): A vehicle handle.
- `instantly` (`BOOL`): If true, the vehicle will be instantly transformed, when false the transform animation plays normally.

**Devuelve:** `void`

**Descripción oficial:**

Transforms the `stormberg` to its "road vehicle" variant. If the vehicle is already in that state then the vehicle transformation audio will still play, but the vehicle won't change at all.

**Nombres antiguos (alias):** `0x2A69FFD1B42BFF9E` (`N_0x2a69ffd1b42bff9e`), `_TRANSFORM_STORMBERG_TO_ROAD_VEHICLE` (`TransformStormbergToRoadVehicle`), `_TRANSFORM_SUBMARINE_TO_VEHICLE` (`TransformSubmarineToVehicle`)

---
### TransformToSubmarine

`TRANSFORM_TO_SUBMARINE` · hash `0xBE4C854FFDB6EEBE` · jhash `0xCAFE5FE0` · **Cliente**

```lua
TransformToSubmarine(vehicle, instantly)
```
```c
void TRANSFORM_TO_SUBMARINE(Vehicle vehicle, BOOL instantly);
```

**Parámetros**

- `vehicle` (`Vehicle`): A vehicle handle.
- `instantly` (`BOOL`): If true, the vehicle will be instantly transformed, when false the transform animation plays normally.

**Devuelve:** `void`

**Descripción oficial:**

Transforms the `stormberg` to its "water vehicle" variant. If the vehicle is already in that state then the vehicle transformation audio will still play, but the vehicle won't change at all.

**Nombres antiguos (alias):** `0xBE4C854FFDB6EEBE` (`N_0xbe4c854ffdb6eebe`), `_TRANSFORM_STORMBERG_TO_WATER_VEHICLE` (`TransformStormbergToWaterVehicle`), `_TRANSFORM_VEHICLE_TO_SUBMARINE` (`TransformVehicleToSubmarine`)

---
### UnpausePlaybackRecordedVehicle

`UNPAUSE_PLAYBACK_RECORDED_VEHICLE` · hash `0x8879EE09268305D5` · jhash `0x59060F75` · **Cliente**

```lua
UnpausePlaybackRecordedVehicle(vehicle)
```
```c
void UNPAUSE_PLAYBACK_RECORDED_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
