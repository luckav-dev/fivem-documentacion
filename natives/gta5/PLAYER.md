# Natives de GTA V — PLAYER

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `PLAYER`: **248** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ArePlayerFlashingStarsAboutToDrop`](#areplayerflashingstarsabouttodrop) · [`ArePlayerStarsGreyedOut`](#areplayerstarsgreyedout) · [`AssistedMovementCloseRoute`](#assistedmovementcloseroute) · [`AssistedMovementFlushRoute`](#assistedmovementflushroute) · [`CanPedHearPlayer`](#canpedhearplayer) · [`CanPlayerStartMission`](#canplayerstartmission) · [`ChangePlayerPed`](#changeplayerped) · [`ClearPlayerHasDamagedAtLeastOneNonAnimalPed`](#clearplayerhasdamagedatleastonenonanimalped) · [`ClearPlayerHasDamagedAtLeastOnePed`](#clearplayerhasdamagedatleastoneped) · [`ClearPlayerParachuteModelOverride`](#clearplayerparachutemodeloverride) · [`ClearPlayerParachutePackModelOverride`](#clearplayerparachutepackmodeloverride) · [`ClearPlayerParachuteVariationOverride`](#clearplayerparachutevariationoverride) · [`ClearPlayerReserveParachuteModelOverride`](#clearplayerreserveparachutemodeloverride) · [`ClearPlayerWantedLevel`](#clearplayerwantedlevel) · [`DisablePlayerFiring`](#disableplayerfiring) · [`DisablePlayerVehicleRewards`](#disableplayervehiclerewards) · [`DisplaySystemSigninUi`](#displaysystemsigninui) · [`EnableSpecialAbility`](#enablespecialability) · [`ExtendWorldBoundaryForPlayer`](#extendworldboundaryforplayer) · [`ForceCleanup`](#forcecleanup) · [`ForceCleanupForAllThreadsWithThisName`](#forcecleanupforallthreadswiththisname) · [`ForceCleanupForThreadWithThisId`](#forcecleanupforthreadwiththisid) · [`GetAchievementProgress`](#getachievementprogress) · [`GetAreCameraControlsDisabled`](#getarecameracontrolsdisabled) · [`GetCauseOfMostRecentForceCleanup`](#getcauseofmostrecentforcecleanup) · [`GetEntityPlayerIsFreeAimingAt`](#getentityplayerisfreeaimingat) · [`GetIsPlayerDrivingOnHighway`](#getisplayerdrivingonhighway) · [`GetMaxWantedLevel`](#getmaxwantedlevel) · [`GetNumberOfPlayers`](#getnumberofplayers) · [`GetNumberOfPlayersInTeam`](#getnumberofplayersinteam) · [`GetPlayerCurrentStealthNoise`](#getplayercurrentstealthnoise) · [`GetPlayerFakeWantedLevel`](#getplayerfakewantedlevel) · [`GetPlayerGroup`](#getplayergroup) · [`GetPlayerHasReserveParachute`](#getplayerhasreserveparachute) · [`GetPlayerHealthRechargeLimit`](#getplayerhealthrechargelimit) · [`GetPlayerIndex`](#getplayerindex) · [`GetPlayerInvincible`](#getplayerinvincible) · [`GetPlayerMaxArmour`](#getplayermaxarmour) · [`GetPlayerName`](#getplayername) · [`GetPlayerParachuteModelOverride`](#getplayerparachutemodeloverride) · [`GetPlayerParachutePackTintIndex`](#getplayerparachutepacktintindex) · [`GetPlayerParachuteSmokeTrailColor`](#getplayerparachutesmoketrailcolor) · [`GetPlayerParachuteTintIndex`](#getplayerparachutetintindex) · [`GetPlayerPed`](#getplayerped) · [`GetPlayerPedScriptIndex`](#getplayerpedscriptindex) · [`GetPlayerReserveParachuteModelOverride`](#getplayerreserveparachutemodeloverride) · [`GetPlayerReserveParachuteTintIndex`](#getplayerreserveparachutetintindex) · [`GetPlayerRgbColour`](#getplayerrgbcolour) · [`GetPlayerSprintStaminaRemaining`](#getplayersprintstaminaremaining) · [`GetPlayerSprintTimeRemaining`](#getplayersprinttimeremaining) · [`GetPlayerTargetEntity`](#getplayertargetentity) · [`GetPlayerTeam`](#getplayerteam) · [`GetPlayerUnderwaterTimeRemaining`](#getplayerunderwatertimeremaining) · [`GetPlayerWantedCentrePosition`](#getplayerwantedcentreposition) · [`GetPlayerWantedLevel`](#getplayerwantedlevel) · [`GetPlayersLastVehicle`](#getplayerslastvehicle) · [`GetTimeSinceLastArrest`](#gettimesincelastarrest) · [`GetTimeSinceLastDeath`](#gettimesincelastdeath) · [`GetTimeSincePlayerDroveAgainstTraffic`](#gettimesinceplayerdroveagainsttraffic) · [`GetTimeSincePlayerDroveOnPavement`](#gettimesinceplayerdroveonpavement) · [`GetTimeSincePlayerHitPed`](#gettimesinceplayerhitped) · [`GetTimeSincePlayerHitVehicle`](#gettimesinceplayerhitvehicle) · [`GetWantedLevelParoleDuration`](#getwantedlevelparoleduration) · [`GetWantedLevelRadius`](#getwantedlevelradius) · [`GetWantedLevelThreshold`](#getwantedlevelthreshold) · [`GiveAchievementToPlayer`](#giveachievementtoplayer) · [`GivePlayerRagdollControl`](#giveplayerragdollcontrol) · [`HasAchievementBeenPassed`](#hasachievementbeenpassed) · [`HasForceCleanupOccurred`](#hasforcecleanupoccurred) · [`HasPlayerBeenShotByCop`](#hasplayerbeenshotbycop) · [`HasPlayerBeenSpottedInStolenVehicle`](#hasplayerbeenspottedinstolenvehicle) · [`HasPlayerDamagedAtLeastOneNonAnimalPed`](#hasplayerdamagedatleastonenonanimalped) · [`HasPlayerDamagedAtLeastOnePed`](#hasplayerdamagedatleastoneped) · [`HasPlayerLeftTheWorld`](#hasplayerlefttheworld) · [`IntToParticipantindex`](#inttoparticipantindex) · [`IntToPlayerindex`](#inttoplayerindex) · [`IsPlayerBattleAware`](#isplayerbattleaware) · [`IsPlayerBeingArrested`](#isplayerbeingarrested) · [`IsPlayerBluetoothEnable`](#isplayerbluetoothenable) · [`IsPlayerClimbing`](#isplayerclimbing) · [`IsPlayerControlOn`](#isplayercontrolon) · [`IsPlayerDead`](#isplayerdead) · [`IsPlayerDrivingDangerously`](#isplayerdrivingdangerously) · [`IsPlayerFreeAiming`](#isplayerfreeaiming) · [`IsPlayerFreeAimingAtEntity`](#isplayerfreeaimingatentity) · [`IsPlayerFreeForAmbientTask`](#isplayerfreeforambienttask) · [`IsPlayerLoggingInNp`](#isplayerlogginginnp) · [`IsPlayerOnline`](#isplayeronline) · [`IsPlayerPlaying`](#isplayerplaying) · [`IsPlayerPressingHorn`](#isplayerpressinghorn) · [`IsPlayerReadyForCutscene`](#isplayerreadyforcutscene) · [`IsPlayerRidingTrain`](#isplayerridingtrain) · [`IsPlayerScriptControlOn`](#isplayerscriptcontrolon) · [`IsPlayerTargettingAnything`](#isplayertargettinganything) · [`IsPlayerTargettingEntity`](#isplayertargettingentity) · [`IsPlayerTeleportActive`](#isplayerteleportactive) · [`IsPlayerWantedLevelGreater`](#isplayerwantedlevelgreater) · [`IsSpecialAbilityActive`](#isspecialabilityactive) · [`IsSpecialAbilityEnabled`](#isspecialabilityenabled) · [`IsSpecialAbilityMeterFull`](#isspecialabilitymeterfull) · [`IsSpecialAbilityUnlocked`](#isspecialabilityunlocked) · [`IsSystemUiBeingDisplayed`](#issystemuibeingdisplayed) · [`N_0x0032a6dba562c518`](#n_0x0032a6dba562c518) · [`N_0x237440e46d918649`](#n_0x237440e46d918649) · [`N_0x2382ab11450ae7ba`](#n_0x2382ab11450ae7ba) · [`N_0x2f41a3bae005e5fa`](#n_0x2f41a3bae005e5fa) · [`N_0x2f7ceb6520288061`](#n_0x2f7ceb6520288061) · [`N_0x31e90b8873a4cd3b`](#n_0x31e90b8873a4cd3b) · [`N_0x36f1b38855f2a8df`](#n_0x36f1b38855f2a8df) · [`N_0x4669b3ed80f24b4e`](#n_0x4669b3ed80f24b4e) · [`N_0x5501b7a5cdb79d37`](#n_0x5501b7a5cdb79d37) · [`N_0x55fcc0c390620314`](#n_0x55fcc0c390620314) · [`N_0x690a61a6d13583f6`](#n_0x690a61a6d13583f6) · [`N_0x6e4361ff3e8cd7ca`](#n_0x6e4361ff3e8cd7ca) · [`N_0x70a382adec069dd3`](#n_0x70a382adec069dd3) · [`N_0x7148e0f43d11f0d9`](#n_0x7148e0f43d11f0d9) · [`N_0x7bae68775557ae0b`](#n_0x7bae68775557ae0b) · [`N_0x7e07c78925d5fd96`](#n_0x7e07c78925d5fd96) · [`N_0x823ec8e82ba45986`](#n_0x823ec8e82ba45986) · [`N_0x8d768602adef2245`](#n_0x8d768602adef2245) · [`N_0x9097eb6d4bb9a12a`](#n_0x9097eb6d4bb9a12a) · [`N_0x9edd76e87d5d51ba`](#n_0x9edd76e87d5d51ba) · [`N_0x9f260bfb59adbca3`](#n_0x9f260bfb59adbca3) · [`N_0xad73ce5a09e42d12`](#n_0xad73ce5a09e42d12) · [`N_0xb45eff719d8427a6`](#n_0xb45eff719d8427a6) · [`N_0xb885852c39cc265d`](#n_0xb885852c39cc265d) · [`N_0xb9cf1f793a9f1bf1`](#n_0xb9cf1f793a9f1bf1) · [`N_0xbc9490ca15aea8fb`](#n_0xbc9490ca15aea8fb) · [`N_0xc3376f42b1faccc6`](#n_0xc3376f42b1faccc6) · [`N_0xcac57395b151135f`](#n_0xcac57395b151135f) · [`N_0xcb645e85e97ea48b`](#n_0xcb645e85e97ea48b) · [`N_0xd821056b9acf8052`](#n_0xd821056b9acf8052) · [`N_0xdcc07526b8ec45af`](#n_0xdcc07526b8ec45af) · [`N_0xdd2620b7b9d16ff1`](#n_0xdd2620b7b9d16ff1) · [`N_0xde45d1a1ef45ee61`](#n_0xde45d1a1ef45ee61) · [`N_0xfac75988a7d078d3`](#n_0xfac75988a7d078d3) · [`N_0xffee8fa29ab9a18e`](#n_0xffee8fa29ab9a18e) · [`NetworkPlayerIdToInt`](#networkplayeridtoint) · [`PlayerAttachVirtualBound`](#playerattachvirtualbound) · [`PlayerDetachVirtualBound`](#playerdetachvirtualbound) · [`PlayerId`](#playerid) · [`PlayerPedId`](#playerpedid) · [`RemovePlayerHelmet`](#removeplayerhelmet) · [`ReportCrime`](#reportcrime) · [`ReportPoliceSpottedPlayer`](#reportpolicespottedplayer) · [`ResetPlayerArrestState`](#resetplayerarreststate) · [`ResetPlayerInputGait`](#resetplayerinputgait) · [`ResetPlayerStamina`](#resetplayerstamina) · [`ResetWantedLevelDifficulty`](#resetwantedleveldifficulty) · [`ResetWorldBoundaryForPlayer`](#resetworldboundaryforplayer) · [`RestorePlayerStamina`](#restoreplayerstamina) · [`SetAchievementProgress`](#setachievementprogress) · [`SetAirDragMultiplierForPlayersVehicle`](#setairdragmultiplierforplayersvehicle) · [`SetAllRandomPedsFlee`](#setallrandompedsflee) · [`SetAllRandomPedsFleeThisFrame`](#setallrandompedsfleethisframe) · [`SetAutoGiveParachuteWhenEnterPlane`](#setautogiveparachutewhenenterplane) · [`SetAutoGiveScubaGearWhenExitVehicle`](#setautogivescubagearwhenexitvehicle) · [`SetDisableAmbientMeleeMove`](#setdisableambientmeleemove) · [`SetDispatchCopsForPlayer`](#setdispatchcopsforplayer) · [`SetEveryoneIgnorePlayer`](#seteveryoneignoreplayer) · [`SetIgnoreLowPriorityShockingEvents`](#setignorelowpriorityshockingevents) · [`SetMaxWantedLevel`](#setmaxwantedlevel) · [`SetPlayerBluetoothState`](#setplayerbluetoothstate) · [`SetPlayerCanBeHassledByGangs`](#setplayercanbehassledbygangs) · [`SetPlayerCanDoDriveBy`](#setplayercandodriveby) · [`SetPlayerCanLeaveParachuteSmokeTrail`](#setplayercanleaveparachutesmoketrail) · [`SetPlayerCanUseCover`](#setplayercanusecover) · [`SetPlayerClothLockCounter`](#setplayerclothlockcounter) · [`SetPlayerClothPackageIndex`](#setplayerclothpackageindex) · [`SetPlayerClothPinFrames`](#setplayerclothpinframes) · [`SetPlayerControl`](#setplayercontrol) · [`SetPlayerFallDistance`](#setplayerfalldistance) · [`SetPlayerForceSkipAimIntro`](#setplayerforceskipaimintro) · [`SetPlayerForcedAim`](#setplayerforcedaim) · [`SetPlayerForcedZoom`](#setplayerforcedzoom) · [`SetPlayerHasReserveParachute`](#setplayerhasreserveparachute) · [`SetPlayerHealthRechargeLimit`](#setplayerhealthrechargelimit) · [`SetPlayerHealthRechargeMultiplier`](#setplayerhealthrechargemultiplier) · [`SetPlayerHomingRocketDisabled`](#setplayerhomingrocketdisabled) · [`SetPlayerInvincible`](#setplayerinvincible) · [`SetPlayerInvincibleKeepRagdollEnabled`](#setplayerinvinciblekeepragdollenabled) · [`SetPlayerLeavePedBehind`](#setplayerleavepedbehind) · [`SetPlayerLockon`](#setplayerlockon) · [`SetPlayerLockonRangeOverride`](#setplayerlockonrangeoverride) · [`SetPlayerMaxArmour`](#setplayermaxarmour) · [`SetPlayerMayNotEnterAnyVehicle`](#setplayermaynotenteranyvehicle) · [`SetPlayerMayOnlyEnterThisVehicle`](#setplayermayonlyenterthisvehicle) · [`SetPlayerMeleeWeaponDamageModifier`](#setplayermeleeweapondamagemodifier) · [`SetPlayerMeleeWeaponDefenseModifier`](#setplayermeleeweapondefensemodifier) · [`SetPlayerModel`](#setplayermodel) · [`SetPlayerNoiseMultiplier`](#setplayernoisemultiplier) · [`SetPlayerParachuteModelOverride`](#setplayerparachutemodeloverride) · [`SetPlayerParachutePackModelOverride`](#setplayerparachutepackmodeloverride) · [`SetPlayerParachutePackTintIndex`](#setplayerparachutepacktintindex) · [`SetPlayerParachuteSmokeTrailColor`](#setplayerparachutesmoketrailcolor) · [`SetPlayerParachuteTintIndex`](#setplayerparachutetintindex) · [`SetPlayerParachuteVariationOverride`](#setplayerparachutevariationoverride) · [`SetPlayerReserveParachuteModelOverride`](#setplayerreserveparachutemodeloverride) · [`SetPlayerReserveParachuteTintIndex`](#setplayerreserveparachutetintindex) · [`SetPlayerResetFlagPreferRearSeats`](#setplayerresetflagpreferrearseats) · [`SetPlayerSimulateAiming`](#setplayersimulateaiming) · [`SetPlayerSneakingNoiseMultiplier`](#setplayersneakingnoisemultiplier) · [`SetPlayerSprint`](#setplayersprint) · [`SetPlayerStealthPerceptionModifier`](#setplayerstealthperceptionmodifier) · [`SetPlayerTargetLevel`](#setplayertargetlevel) · [`SetPlayerTargetingMode`](#setplayertargetingmode) · [`SetPlayerTeam`](#setplayerteam) · [`SetPlayerUnderwaterTimeRemaining`](#setplayerunderwatertimeremaining) · [`SetPlayerVehicleDamageModifier`](#setplayervehicledamagemodifier) · [`SetPlayerVehicleDefenseModifier`](#setplayervehicledefensemodifier) · [`SetPlayerWantedCentrePosition`](#setplayerwantedcentreposition) · [`SetPlayerWantedLevel`](#setplayerwantedlevel) · [`SetPlayerWantedLevelNoDrop`](#setplayerwantedlevelnodrop) · [`SetPlayerWantedLevelNow`](#setplayerwantedlevelnow) · [`SetPlayerWeaponDamageModifier`](#setplayerweapondamagemodifier) · [`SetPlayerWeaponDefenseModifier`](#setplayerweapondefensemodifier) · [`SetPlayerWeaponDefenseModifier_2`](#setplayerweapondefensemodifier_2) · [`SetPoliceIgnorePlayer`](#setpoliceignoreplayer) · [`SetPoliceRadarBlips`](#setpoliceradarblips) · [`SetRunSprintMultiplierForPlayer`](#setrunsprintmultiplierforplayer) · [`SetSpecialAbility`](#setspecialability) · [`SetSpecialAbilityMultiplier`](#setspecialabilitymultiplier) · [`SetSwimMultiplierForPlayer`](#setswimmultiplierforplayer) · [`SetWantedLevelDifficulty`](#setwantedleveldifficulty) · [`SetWantedLevelHiddenEvasionTime`](#setwantedlevelhiddenevasiontime) · [`SetWantedLevelMultiplier`](#setwantedlevelmultiplier) · [`SimulatePlayerInputGait`](#simulateplayerinputgait) · [`SpecialAbilityActivate`](#specialabilityactivate) · [`SpecialAbilityChargeAbsolute`](#specialabilitychargeabsolute) · [`SpecialAbilityChargeContinuous`](#specialabilitychargecontinuous) · [`SpecialAbilityChargeLarge`](#specialabilitychargelarge) · [`SpecialAbilityChargeMedium`](#specialabilitychargemedium) · [`SpecialAbilityChargeNormalized`](#specialabilitychargenormalized) · [`SpecialAbilityChargeOnMissionFailed`](#specialabilitychargeonmissionfailed) · [`SpecialAbilityChargeSmall`](#specialabilitychargesmall) · [`SpecialAbilityDeactivate`](#specialabilitydeactivate) · [`SpecialAbilityDeactivateFast`](#specialabilitydeactivatefast) · [`SpecialAbilityDeplete`](#specialabilitydeplete) · [`SpecialAbilityDepleteMeter`](#specialabilitydepletemeter) · [`SpecialAbilityFillMeter`](#specialabilityfillmeter) · [`SpecialAbilityLock`](#specialabilitylock) · [`SpecialAbilityReset`](#specialabilityreset) · [`SpecialAbilityUnlock`](#specialabilityunlock) · [`StartFiringAmnesty`](#startfiringamnesty) · [`StartPlayerTeleport`](#startplayerteleport) · [`StopPlayerTeleport`](#stopplayerteleport) · [`SuppressCrimeThisFrame`](#suppresscrimethisframe) · [`UpdatePlayerTeleport`](#updateplayerteleport)

---
### ArePlayerFlashingStarsAboutToDrop

`ARE_PLAYER_FLASHING_STARS_ABOUT_TO_DROP` · hash `0xAFAF86043E5874E9` · jhash `0xE13A71C7` · **Cliente**

```lua
local retval = ArePlayerFlashingStarsAboutToDrop(player)
```
```c
BOOL ARE_PLAYER_FLASHING_STARS_ABOUT_TO_DROP(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### ArePlayerStarsGreyedOut

`ARE_PLAYER_STARS_GREYED_OUT` · hash `0x0A6EB355EE14A2DB` · jhash `0x5E72AB72` · **Cliente**

```lua
local retval = ArePlayerStarsGreyedOut(player)
```
```c
BOOL ARE_PLAYER_STARS_GREYED_OUT(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### AssistedMovementCloseRoute

`ASSISTED_MOVEMENT_CLOSE_ROUTE` · hash `0xAEBF081FFC0A0E5E` · jhash `0xF23277F3` · **Cliente**

```lua
AssistedMovementCloseRoute()
```
```c
void ASSISTED_MOVEMENT_CLOSE_ROUTE();
```

**Devuelve:** `void`

---
### AssistedMovementFlushRoute

`ASSISTED_MOVEMENT_FLUSH_ROUTE` · hash `0x8621390F0CDCFE1F` · jhash `0xD04568B9` · **Cliente**

```lua
AssistedMovementFlushRoute()
```
```c
void ASSISTED_MOVEMENT_FLUSH_ROUTE();
```

**Devuelve:** `void`

---
### CanPedHearPlayer

`CAN_PED_HEAR_PLAYER` · hash `0xF297383AA91DCA29` · jhash `0x1C70B2EB` · **Cliente**

```lua
local retval = CanPedHearPlayer(player, ped)
```
```c
BOOL CAN_PED_HEAR_PLAYER(Player player, Ped ped);
```

**Parámetros**

- `player` (`Player`)
- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### CanPlayerStartMission

`CAN_PLAYER_START_MISSION` · hash `0xDE7465A27D403C06` · jhash `0x39E3CB3F` · **Cliente**

```lua
local retval = CanPlayerStartMission(player)
```
```c
BOOL CAN_PLAYER_START_MISSION(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### ChangePlayerPed

`CHANGE_PLAYER_PED` · hash `0x048189FAC643DEEE` · jhash `0xBE515485` · **Cliente**

```lua
ChangePlayerPed(player, ped, b2, resetDamage)
```
```c
void CHANGE_PLAYER_PED(Player player, Ped ped, BOOL b2, BOOL resetDamage);
```

**Parámetros**

- `player` (`Player`)
- `ped` (`Ped`)
- `b2` (`BOOL`)
- `resetDamage` (`BOOL`)

**Devuelve:** `void`

---
### ClearPlayerHasDamagedAtLeastOneNonAnimalPed

`CLEAR_PLAYER_HAS_DAMAGED_AT_LEAST_ONE_NON_ANIMAL_PED` · hash `0x4AACB96203D11A31` · jhash `0x7E3BFBC5` · **Cliente**

```lua
ClearPlayerHasDamagedAtLeastOneNonAnimalPed(player)
```
```c
void CLEAR_PLAYER_HAS_DAMAGED_AT_LEAST_ONE_NON_ANIMAL_PED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ClearPlayerHasDamagedAtLeastOnePed

`CLEAR_PLAYER_HAS_DAMAGED_AT_LEAST_ONE_PED` · hash `0xF0B67A4DE6AB5F98` · jhash `0x1D31CBBD` · **Cliente**

```lua
ClearPlayerHasDamagedAtLeastOnePed(player)
```
```c
void CLEAR_PLAYER_HAS_DAMAGED_AT_LEAST_ONE_PED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ClearPlayerParachuteModelOverride

`CLEAR_PLAYER_PARACHUTE_MODEL_OVERRIDE` · hash `0x8753997EB5F6EE3F` · jhash `0x6FF034BB` · **Cliente**

```lua
ClearPlayerParachuteModelOverride(player)
```
```c
void CLEAR_PLAYER_PARACHUTE_MODEL_OVERRIDE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ClearPlayerParachutePackModelOverride

`CLEAR_PLAYER_PARACHUTE_PACK_MODEL_OVERRIDE` · hash `0x10C54E4389C12B42` · jhash `0xBB62AAC5` · **Cliente**

```lua
ClearPlayerParachutePackModelOverride(player)
```
```c
void CLEAR_PLAYER_PARACHUTE_PACK_MODEL_OVERRIDE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ClearPlayerParachuteVariationOverride

`CLEAR_PLAYER_PARACHUTE_VARIATION_OVERRIDE` · hash `0x0F4CC924CF8C7B21` · jhash `0xFD60F5AB` · **Cliente**

```lua
ClearPlayerParachuteVariationOverride(player)
```
```c
void CLEAR_PLAYER_PARACHUTE_VARIATION_OVERRIDE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ClearPlayerReserveParachuteModelOverride

`_CLEAR_PLAYER_RESERVE_PARACHUTE_MODEL_OVERRIDE` · hash `0x290D248E25815AE8` · **Cliente**

```lua
ClearPlayerReserveParachuteModelOverride(player)
```
```c
void _CLEAR_PLAYER_RESERVE_PARACHUTE_MODEL_OVERRIDE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### ClearPlayerWantedLevel

`CLEAR_PLAYER_WANTED_LEVEL` · hash `0xB302540597885499` · jhash `0x54EA5BCC` · **Cliente · también en el servidor (RPC)**

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

---
### DisablePlayerFiring

`DISABLE_PLAYER_FIRING` · hash `0x5E6CC07646BBEAB8` · jhash `0x30CB28CB` · **Cliente**

```lua
DisablePlayerFiring(player, toggle)
```
```c
void DISABLE_PLAYER_FIRING(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`): The player for which to disable combat methods.
- `toggle` (`BOOL`): Unused, as this native will disable combat regardless of the value of this parameter.

**Devuelve:** `void`

**Descripción oficial:**

Inhibits the player from using any method of combat including melee and firearms.\
NOTE: Only disables the firing for one frame

---
### DisablePlayerVehicleRewards

`DISABLE_PLAYER_VEHICLE_REWARDS` · hash `0xC142BE3BB9CE125F` · jhash `0x8C6E611D` · **Cliente**

```lua
DisablePlayerVehicleRewards(player)
```
```c
void DISABLE_PLAYER_VEHICLE_REWARDS(Player player);
```

**Parámetros**

- `player` (`Player`): The player to disable rewards

**Devuelve:** `void`

**Descripción oficial:**

Disables vehicle rewards for the current frame.

---
### DisplaySystemSigninUi

`DISPLAY_SYSTEM_SIGNIN_UI` · hash `0x94DD7888C10A979E` · jhash `0x4264CED2` · **Cliente**

```lua
DisplaySystemSigninUi(unk)
```
```c
void DISPLAY_SYSTEM_SIGNIN_UI(BOOL unk);
```

**Parámetros**

- `unk` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Purpose of the BOOL currently unknown.  
Both, true and false, work  
```

---
### EnableSpecialAbility

`ENABLE_SPECIAL_ABILITY` · hash `0x181EC197DAEFE121` · jhash `0xC86C1B4E` · **Cliente**

```lua
EnableSpecialAbility(player, toggle)
```
```c
void ENABLE_SPECIAL_ABILITY(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 3: Any p2
```

---
### ExtendWorldBoundaryForPlayer

`EXTEND_WORLD_BOUNDARY_FOR_PLAYER` · hash `0x5006D96C995A5827` · jhash `0x64DDB07D` · **Cliente**

```lua
ExtendWorldBoundaryForPlayer(x, y, z)
```
```c
void EXTEND_WORLD_BOUNDARY_FOR_PLAYER(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Appears only 3 times in the scripts, more specifically in michael1.ysc
-
This can be used to prevent dying if you are "out of the world"
```

**Nombres antiguos (alias):** `0x5006D96C995A5827` (`N_0x5006d96c995a5827`), `_EXPAND_WORLD_LIMITS` (`ExpandWorldLimits`)

---
### ForceCleanup

`FORCE_CLEANUP` · hash `0xBC8983F38F78ED51` · jhash `0xFDAAEA2B` · **Cliente**

```lua
ForceCleanup(cleanupFlags)
```
```c
void FORCE_CLEANUP(int cleanupFlags);
```

**Parámetros**

- `cleanupFlags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
used with 1,2,8,64,128 in the scripts  
```

---
### ForceCleanupForAllThreadsWithThisName

`FORCE_CLEANUP_FOR_ALL_THREADS_WITH_THIS_NAME` · hash `0x4C68DDDDF0097317` · jhash `0x04256C73` · **Cliente**

```lua
ForceCleanupForAllThreadsWithThisName(name, cleanupFlags)
```
```c
void FORCE_CLEANUP_FOR_ALL_THREADS_WITH_THIS_NAME(char* name, int cleanupFlags);
```

**Parámetros**

- `name` (`char*`)
- `cleanupFlags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
PLAYER::FORCE_CLEANUP_FOR_ALL_THREADS_WITH_THIS_NAME("pb_prostitute", 1); // Found in decompilation  
```

---
### ForceCleanupForThreadWithThisId

`FORCE_CLEANUP_FOR_THREAD_WITH_THIS_ID` · hash `0xF745B37630DF176B` · jhash `0x882D3EB3` · **Cliente**

```lua
ForceCleanupForThreadWithThisId(id, cleanupFlags)
```
```c
void FORCE_CLEANUP_FOR_THREAD_WITH_THIS_ID(int id, int cleanupFlags);
```

**Parámetros**

- `id` (`int`)
- `cleanupFlags` (`int`)

**Devuelve:** `void`

---
### GetAchievementProgress

`_GET_ACHIEVEMENT_PROGRESS` · hash `0x1C186837D0619335` · **Cliente**

```lua
local retval = GetAchievementProgress(achievement)
```
```c
int _GET_ACHIEVEMENT_PROGRESS(int achievement);
```

**Parámetros**

- `achievement` (`int`)

**Devuelve:** `int` — Returns the progression of an achievement; 0 if the achievement cannot be progressed.

**Descripción oficial:**

```
For Steam.
Always returns 0 in retail version of the game.
```

**Nombres antiguos (alias):** `0x1C186837D0619335` (`N_0x1c186837d0619335`), `_GET_ACHIEVEMENT_PROGRESSION` (`GetAchievementProgression`)

---
### GetAreCameraControlsDisabled

`GET_ARE_CAMERA_CONTROLS_DISABLED` · hash `0x7C814D2FB49F40C0` · jhash `0x4C456AF2` · **Cliente**

```lua
local retval = GetAreCameraControlsDisabled()
```
```c
BOOL GET_ARE_CAMERA_CONTROLS_DISABLED();
```

**Devuelve:** `BOOL` — Returns `true` if the main player's camera controls are disabled. Also returns `true` if the there is no main player info.

**Nombres antiguos (alias):** `_IS_PLAYER_CAM_CONTROL_DISABLED` (`IsPlayerCamControlDisabled`), `0x7C814D2FB49F40C0` (`N_0x7c814d2fb49f40c0`)

---
### GetCauseOfMostRecentForceCleanup

`GET_CAUSE_OF_MOST_RECENT_FORCE_CLEANUP` · hash `0x9A41CF4674A12272` · jhash `0x39AA9FC8` · **Cliente**

```lua
local retval = GetCauseOfMostRecentForceCleanup()
```
```c
int GET_CAUSE_OF_MOST_RECENT_FORCE_CLEANUP();
```

**Devuelve:** `int`

---
### GetEntityPlayerIsFreeAimingAt

`GET_ENTITY_PLAYER_IS_FREE_AIMING_AT` · hash `0x2975C866E6713290` · jhash `0x8866D9D0` · **Cliente**

```lua
local retval, entity = GetEntityPlayerIsFreeAimingAt(player, entity)
```
```c
BOOL GET_ENTITY_PLAYER_IS_FREE_AIMING_AT(Player player, Entity* entity);
```

**Parámetros**

- `player` (`Player`)
- `entity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns TRUE if it found an entity in your crosshair within range of your weapon. Assigns the handle of the target to the *entity that you pass it.  
Returns false if no entity found.  
```

---
### GetIsPlayerDrivingOnHighway

`GET_IS_PLAYER_DRIVING_ON_HIGHWAY` · hash `0x5FC472C501CCADB3` · jhash `0x46E7E31D` · **Cliente**

```lua
local retval = GetIsPlayerDrivingOnHighway(playerId)
```
```c
BOOL GET_IS_PLAYER_DRIVING_ON_HIGHWAY(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The local index of the player to check (see [PLAYER_ID](#playerid))

**Devuelve:** `BOOL` — Returns a boolean value representing if the player is driving on a highway.

**Nombres antiguos (alias):** `0x5FC472C501CCADB3` (`N_0x5fc472c501ccadb3`)

**Ejemplo (lua):**

```lua
-- Get and store the local player index
local playerId = PlayerId()

if GetIsPlayerDrivingOnHighway(playerId) then
    print("Player is driving on a highway!")
else
    print("Player is not driving on a highway.")
end
```

---
### GetMaxWantedLevel

`GET_MAX_WANTED_LEVEL` · hash `0x462E0DB9B137DC5F` · jhash `0x457F1E44` · **Cliente**

```lua
local retval = GetMaxWantedLevel()
```
```c
int GET_MAX_WANTED_LEVEL();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the maximum wanted level the player can get.  
Ranges from 0 to 5.  
```

---
### GetNumberOfPlayers

`GET_NUMBER_OF_PLAYERS` · hash `0x407C7F91DDB46C16` · jhash `0x4C1B8867` · **Cliente**

```lua
local retval = GetNumberOfPlayers()
```
```c
int GET_NUMBER_OF_PLAYERS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the number of players in the current session.
If not multiplayer, always returns 1.
```

---
### GetNumberOfPlayersInTeam

`_GET_NUMBER_OF_PLAYERS_IN_TEAM` · hash `0x1FC200409F10E6F1` · **Cliente**

```lua
local retval = GetNumberOfPlayersInTeam(team)
```
```c
int _GET_NUMBER_OF_PLAYERS_IN_TEAM(int team);
```

**Parámetros**

- `team` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### GetPlayerCurrentStealthNoise

`GET_PLAYER_CURRENT_STEALTH_NOISE` · hash `0x2F395D61F3A1F877` · jhash `0xC3B02362` · **Cliente**

```lua
local retval = GetPlayerCurrentStealthNoise(player)
```
```c
float GET_PLAYER_CURRENT_STEALTH_NOISE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

---
### GetPlayerFakeWantedLevel

`GET_PLAYER_FAKE_WANTED_LEVEL` · hash `0x56105E599CAB0EFA` · jhash `0x0098D244` · **Cliente**

```lua
local retval = GetPlayerFakeWantedLevel(player)
```
```c
int GET_PLAYER_FAKE_WANTED_LEVEL(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x56105E599CAB0EFA` (`N_0x56105e599cab0efa`)

---
### GetPlayerGroup

`GET_PLAYER_GROUP` · hash `0x0D127585F77030AF` · jhash `0xA5EDCDE8` · **Cliente**

```lua
local retval = GetPlayerGroup(player)
```
```c
int GET_PLAYER_GROUP(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the group ID the player is member of.  
```

---
### GetPlayerHasReserveParachute

`GET_PLAYER_HAS_RESERVE_PARACHUTE` · hash `0x5DDFE2FF727F3CA3` · jhash `0x30DA1DA1` · **Cliente**

```lua
local retval = GetPlayerHasReserveParachute(player)
```
```c
BOOL GET_PLAYER_HAS_RESERVE_PARACHUTE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### GetPlayerHealthRechargeLimit

`_GET_PLAYER_HEALTH_RECHARGE_LIMIT` · hash `0x8BC515BAE4AAF8FF` · **Cliente**

```lua
local retval = GetPlayerHealthRechargeLimit(player)
```
```c
float _GET_PLAYER_HEALTH_RECHARGE_LIMIT(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x8BC515BAE4AAF8FF` (`N_0x8bc515bae4aaf8ff`)

---
### GetPlayerIndex

`GET_PLAYER_INDEX` · hash `0xA5EDC40EF369B48D` · jhash `0x309BBDC1` · **Cliente**

```lua
local retval = GetPlayerIndex()
```
```c
Player GET_PLAYER_INDEX();
```

**Devuelve:** `Player`

**Descripción oficial:**

```
Returns the same as PLAYER_ID and NETWORK_PLAYER_ID_TO_INT  
```

---
### GetPlayerInvincible

`GET_PLAYER_INVINCIBLE` · hash `0xB721981B2B939E07` · jhash `0x680C90EE` · **Cliente**

```lua
local retval = GetPlayerInvincible(player)
```
```c
BOOL GET_PLAYER_INVINCIBLE(Player player);
```

**Parámetros**

- `player` (`Player`): The player index

**Devuelve:** `BOOL` — A boolean to tell if the player is invincible.

**Descripción oficial:**

This native will only return true if a player was made invincible with [`SET_PLAYER_INVINCIBLE`](../cfx/servidor.md#setplayerinvincible).

You should use [`GET_PLAYER_INVINCIBLE_2`](../cfx/cliente-1.md#getplayerinvincible_2) to get both [`SET_PLAYER_INVINCIBLE`](../cfx/servidor.md#setplayerinvincible) and [`SET_PLAYER_INVINCIBLE_KEEP_RAGDOLL_ENABLED`](#setplayerinvinciblekeepragdollenabled) invincibility state.

---
### GetPlayerMaxArmour

`GET_PLAYER_MAX_ARMOUR` · hash `0x92659B4CE1863CB3` · jhash `0x02A50657` · **Cliente**

```lua
local retval = GetPlayerMaxArmour(player)
```
```c
int GET_PLAYER_MAX_ARMOUR(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### GetPlayerName

`GET_PLAYER_NAME` · hash `0x6D0DE6A7B5DA71F8` · jhash `0x406B4B20` · **Cliente**

```lua
local retval = GetPlayerName(player)
```
```c
char* GET_PLAYER_NAME(Player player);
```

**Parámetros**

- `player` (`Player`): The player index, or -1 to get the local player ped.

**Devuelve:** `char*` — The name of the queried player. "**Invalid**" if the player does not exist.

**Descripción oficial:**

Returns the players name from a specified player index

---
### GetPlayerParachuteModelOverride

`_GET_PLAYER_PARACHUTE_MODEL_OVERRIDE` · hash `0xC219887CA3E65C41` · **Cliente**

```lua
local retval = GetPlayerParachuteModelOverride(player)
```
```c
Hash _GET_PLAYER_PARACHUTE_MODEL_OVERRIDE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### GetPlayerParachutePackTintIndex

`GET_PLAYER_PARACHUTE_PACK_TINT_INDEX` · hash `0x6E9C742F340CE5A2` · jhash `0x4E418E13` · **Cliente**

```lua
local tintIndex = GetPlayerParachutePackTintIndex(player, tintIndex)
```
```c
void GET_PLAYER_PARACHUTE_PACK_TINT_INDEX(Player player, int* tintIndex);
```

**Parámetros**

- `player` (`Player`)
- `tintIndex` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetPlayerParachuteSmokeTrailColor

`GET_PLAYER_PARACHUTE_SMOKE_TRAIL_COLOR` · hash `0xEF56DBABD3CD4887` · jhash `0xF66E5CDD` · **Cliente**

```lua
local r, g, b = GetPlayerParachuteSmokeTrailColor(player)
```
```c
void GET_PLAYER_PARACHUTE_SMOKE_TRAIL_COLOR(Player player, int* r, int* g, int* b);
```

**Parámetros**

- `player` (`Player`)
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetPlayerParachuteTintIndex

`GET_PLAYER_PARACHUTE_TINT_INDEX` · hash `0x75D3F7A1B0D9B145` · jhash `0x432B0509` · **Cliente**

```lua
local tintIndex = GetPlayerParachuteTintIndex(player, tintIndex)
```
```c
void GET_PLAYER_PARACHUTE_TINT_INDEX(Player player, int* tintIndex);
```

**Parámetros**

- `player` (`Player`)
- `tintIndex` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Tints:  
None = -1,  
Rainbow = 0,  
Red = 1,  
SeasideStripes = 2,  
WidowMaker = 3,  
Patriot = 4,  
Blue = 5,  
Black = 6,  
Hornet = 7,  
AirFocce = 8,  
Desert = 9,  
Shadow = 10,  
HighAltitude = 11,  
Airbone = 12,  
Sunrise = 13,  
```

---
### GetPlayerPed

`GET_PLAYER_PED` · hash `0x43A66C31C68491C0` · jhash `0x6E31E993` · **Cliente**

```lua
local retval = GetPlayerPed(playerId)
```
```c
Ped GET_PLAYER_PED(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index, or -1 to get the local player ped.

**Devuelve:** `Ped` — The specified player's ped, or 0 if invalid.

**Descripción oficial:**

Gets the ped for a specified player index.

Note: For performance reasons, usage of [`PLAYER_PED_ID`](#playerpedid) is recommended over the use of `GetPlayerPed(-1)` when wanting to acquire your local player ped. For more information, please refer to [this](https://forum.cfx.re/t/question-difference-between-getplayerped-1-and-playerpedid/539437/2) forum post.

**Ejemplo (lua):**

```lua
local playerIdx = GetPlayerFromServerId(source)
local ped = GetPlayerPed(playerIdx)

-- act on the ped
```

---
### GetPlayerPedScriptIndex

`GET_PLAYER_PED_SCRIPT_INDEX` · hash `0x50FAC3A3E030A6E1` · jhash `0x6AC64990` · **Cliente**

```lua
local retval = GetPlayerPedScriptIndex(player)
```
```c
Ped GET_PLAYER_PED_SCRIPT_INDEX(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `Ped`

**Descripción oficial:**

```
Does the same like PLAYER::GET_PLAYER_PED
```

---
### GetPlayerReserveParachuteModelOverride

`_GET_PLAYER_RESERVE_PARACHUTE_MODEL_OVERRIDE` · hash `0x37FAAA68DCA9D08D` · **Cliente**

```lua
local retval = GetPlayerReserveParachuteModelOverride(player)
```
```c
Hash _GET_PLAYER_RESERVE_PARACHUTE_MODEL_OVERRIDE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### GetPlayerReserveParachuteTintIndex

`GET_PLAYER_RESERVE_PARACHUTE_TINT_INDEX` · hash `0xD5A016BC3C09CF40` · jhash `0x77B8EF01` · **Cliente**

```lua
local index = GetPlayerReserveParachuteTintIndex(player, index)
```
```c
void GET_PLAYER_RESERVE_PARACHUTE_TINT_INDEX(Player player, int* index);
```

**Parámetros**

- `player` (`Player`)
- `index` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Tints:  
None = -1,  
Rainbow = 0,  
Red = 1,  
SeasideStripes = 2,  
WidowMaker = 3,  
Patriot = 4,  
Blue = 5,  
Black = 6,  
Hornet = 7,  
AirFocce = 8,  
Desert = 9,  
Shadow = 10,  
HighAltitude = 11,  
Airbone = 12,  
Sunrise = 13,  
```

---
### GetPlayerRgbColour

`GET_PLAYER_RGB_COLOUR` · hash `0xE902EF951DCE178F` · jhash `0x6EF43BBB` · **Cliente**

```lua
local r, g, b = GetPlayerRgbColour(player)
```
```c
void GET_PLAYER_RGB_COLOUR(Player player, int* r, int* g, int* b);
```

**Parámetros**

- `player` (`Player`)
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetPlayerSprintStaminaRemaining

`GET_PLAYER_SPRINT_STAMINA_REMAINING` · hash `0x3F9F16F8E65A7ED7` · jhash `0x47017C90` · **Cliente**

```lua
local retval = GetPlayerSprintStaminaRemaining(player)
```
```c
float GET_PLAYER_SPRINT_STAMINA_REMAINING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

---
### GetPlayerSprintTimeRemaining

`GET_PLAYER_SPRINT_TIME_REMAINING` · hash `0x1885BC9B108B4C99` · jhash `0x40E80543` · **Cliente**

```lua
local retval = GetPlayerSprintTimeRemaining(player)
```
```c
float GET_PLAYER_SPRINT_TIME_REMAINING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

---
### GetPlayerTargetEntity

`GET_PLAYER_TARGET_ENTITY` · hash `0x13EDE1A5DBF797C9` · jhash `0xF6AAA2D7` · **Cliente**

```lua
local retval, entity = GetPlayerTargetEntity(player, entity)
```
```c
BOOL GET_PLAYER_TARGET_ENTITY(Player player, Entity* entity);
```

**Parámetros**

- `player` (`Player`)
- `entity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Assigns the handle of locked-on melee target to *entity that you pass it.  
Returns false if no entity found.  
```

---
### GetPlayerTeam

`GET_PLAYER_TEAM` · hash `0x37039302F4E0A008` · jhash `0x9873E404` · **Cliente**

```lua
local retval = GetPlayerTeam(player)
```
```c
int GET_PLAYER_TEAM(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the player's team.  
Does nothing in singleplayer.  
```

---
### GetPlayerUnderwaterTimeRemaining

`GET_PLAYER_UNDERWATER_TIME_REMAINING` · hash `0xA1FCF8E6AF40B731` · jhash `0x1317125A` · **Cliente**

```lua
local retval = GetPlayerUnderwaterTimeRemaining(player)
```
```c
float GET_PLAYER_UNDERWATER_TIME_REMAINING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

---
### GetPlayerWantedCentrePosition

`GET_PLAYER_WANTED_CENTRE_POSITION` · hash `0x0C92BA89F1AF26F8` · jhash `0x821F2D2C` · **Cliente**

```lua
local retval = GetPlayerWantedCentrePosition(player)
```
```c
Vector3 GET_PLAYER_WANTED_CENTRE_POSITION(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `Vector3`

---
### GetPlayerWantedLevel

`GET_PLAYER_WANTED_LEVEL` · hash `0xE28E54788CE8F12D` · jhash `0xBDCDD163` · **Cliente**

```lua
local retval = GetPlayerWantedLevel(player)
```
```c
int GET_PLAYER_WANTED_LEVEL(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### GetPlayersLastVehicle

`GET_PLAYERS_LAST_VEHICLE` · hash `0xB6997A7EB3F5C8C0` · jhash `0xE2757AC1` · **Cliente**

```lua
local retval = GetPlayersLastVehicle()
```
```c
Vehicle GET_PLAYERS_LAST_VEHICLE();
```

**Devuelve:** `Vehicle` — A vehicle handle containing the last player's vehicle.

**Descripción oficial:**

**Warning**

This native will return `0` if the last vehicle the player was in was destroyed.

**Alternative**

You can use [GET_VEHICLE_PED_IS_IN](../cfx/servidor.md#getvehiclepedisin), which will actually get the last vehicle, even if it was destroyed.

---
### GetTimeSinceLastArrest

`GET_TIME_SINCE_LAST_ARREST` · hash `0x5063F92F07C2A316` · jhash `0x62824EF4` · **Cliente**

```lua
local retval = GetTimeSinceLastArrest()
```
```c
int GET_TIME_SINCE_LAST_ARREST();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the time since the character was arrested in (ms) milliseconds.  
example  
var time = Function.call<int>(Hash.GET_TIME_SINCE_LAST_ARREST();  
UI.DrawSubtitle(time.ToString());  
if player has not been arrested, the int returned will be -1.  
```

---
### GetTimeSinceLastDeath

`GET_TIME_SINCE_LAST_DEATH` · hash `0xC7034807558DDFCA` · jhash `0x24BC5AC0` · **Cliente**

```lua
local retval = GetTimeSinceLastDeath()
```
```c
int GET_TIME_SINCE_LAST_DEATH();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the time since the character died in (ms) milliseconds.  
example  
var time = Function.call<int>(Hash.GET_TIME_SINCE_LAST_DEATH();  
UI.DrawSubtitle(time.ToString());  
if player has not died, the int returned will be -1.  
```

---
### GetTimeSincePlayerDroveAgainstTraffic

`GET_TIME_SINCE_PLAYER_DROVE_AGAINST_TRAFFIC` · hash `0xDB89591E290D9182` · jhash `0x9F27D00E` · **Cliente**

```lua
local retval = GetTimeSincePlayerDroveAgainstTraffic(player)
```
```c
int GET_TIME_SINCE_PLAYER_DROVE_AGAINST_TRAFFIC(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### GetTimeSincePlayerDroveOnPavement

`GET_TIME_SINCE_PLAYER_DROVE_ON_PAVEMENT` · hash `0xD559D2BE9E37853B` · jhash `0x8836E732` · **Cliente**

```lua
local retval = GetTimeSincePlayerDroveOnPavement(player)
```
```c
int GET_TIME_SINCE_PLAYER_DROVE_ON_PAVEMENT(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### GetTimeSincePlayerHitPed

`GET_TIME_SINCE_PLAYER_HIT_PED` · hash `0xE36A25322DC35F42` · jhash `0xB6209195` · **Cliente**

```lua
local retval = GetTimeSincePlayerHitPed(player)
```
```c
int GET_TIME_SINCE_PLAYER_HIT_PED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### GetTimeSincePlayerHitVehicle

`GET_TIME_SINCE_PLAYER_HIT_VEHICLE` · hash `0x5D35ECF3A81A0EE0` · jhash `0x6E9B8B9E` · **Cliente**

```lua
local retval = GetTimeSincePlayerHitVehicle(player)
```
```c
int GET_TIME_SINCE_PLAYER_HIT_VEHICLE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### GetWantedLevelParoleDuration

`_GET_WANTED_LEVEL_PAROLE_DURATION` · hash `0xA72200F51875FEA4` · **Cliente**

```lua
local retval = GetWantedLevelParoleDuration()
```
```c
int _GET_WANTED_LEVEL_PAROLE_DURATION();
```

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xA72200F51875FEA4` (`N_0xa72200f51875fea4`)

---
### GetWantedLevelRadius

`GET_WANTED_LEVEL_RADIUS` · hash `0x085DEB493BE80812` · jhash `0x1CF7D7DA` · **Cliente**

```lua
local retval = GetWantedLevelRadius(player)
```
```c
float GET_WANTED_LEVEL_RADIUS(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

**Descripción oficial:**

```
Remnant from GTA IV. Does nothing in GTA V.
```

---
### GetWantedLevelThreshold

`GET_WANTED_LEVEL_THRESHOLD` · hash `0xFDD179EAF45B556C` · jhash `0xD9783F6B` · **Cliente**

```lua
local retval = GetWantedLevelThreshold(wantedLevel)
```
```c
int GET_WANTED_LEVEL_THRESHOLD(int wantedLevel);
```

**Parámetros**

- `wantedLevel` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Drft  
```

---
### GiveAchievementToPlayer

`GIVE_ACHIEVEMENT_TO_PLAYER` · hash `0xBEC7076D64130195` · jhash `0x822BC992` · **Cliente**

```lua
local retval = GiveAchievementToPlayer(achievement)
```
```c
BOOL GIVE_ACHIEVEMENT_TO_PLAYER(int achievement);
```

**Parámetros**

- `achievement` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Achievements from 0-57
more achievements came with update 1.29 (freemode events update), I'd say that they now go to 60, but I'll need to check.
```

---
### GivePlayerRagdollControl

`GIVE_PLAYER_RAGDOLL_CONTROL` · hash `0x3C49C870E66F0A28` · jhash `0xC7B4D7AC` · **Cliente**

```lua
GivePlayerRagdollControl(player, toggle)
```
```c
void GIVE_PLAYER_RAGDOLL_CONTROL(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### HasAchievementBeenPassed

`HAS_ACHIEVEMENT_BEEN_PASSED` · hash `0x867365E111A3B6EB` · jhash `0x136A5BE9` · **Cliente**

```lua
local retval = HasAchievementBeenPassed(achievement)
```
```c
BOOL HAS_ACHIEVEMENT_BEEN_PASSED(int achievement);
```

**Parámetros**

- `achievement` (`int`)

**Devuelve:** `BOOL`

---
### HasForceCleanupOccurred

`HAS_FORCE_CLEANUP_OCCURRED` · hash `0xC968670BFACE42D9` · jhash `0x4B37333C` · **Cliente**

```lua
local retval = HasForceCleanupOccurred(cleanupFlags)
```
```c
BOOL HAS_FORCE_CLEANUP_OCCURRED(int cleanupFlags);
```

**Parámetros**

- `cleanupFlags` (`int`)

**Devuelve:** `BOOL`

---
### HasPlayerBeenShotByCop

`_HAS_PLAYER_BEEN_SHOT_BY_COP` · hash `0xBC0753C9CA14B506` · jhash `0x9DF75B2A` · **Cliente**

```lua
local retval = HasPlayerBeenShotByCop(player, ms, p2)
```
```c
BOOL _HAS_PLAYER_BEEN_SHOT_BY_COP(Player player, int ms, BOOL p2);
```

**Parámetros**

- `player` (`Player`)
- `ms` (`int`): Time since last bullet fired
- `p2` (`BOOL`): Always false

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBC0753C9CA14B506` (`N_0xbc0753c9ca14b506`)

---
### HasPlayerBeenSpottedInStolenVehicle

`HAS_PLAYER_BEEN_SPOTTED_IN_STOLEN_VEHICLE` · hash `0xD705740BB0A1CF4C` · jhash `0x4A01B76A` · **Cliente**

```lua
local retval = HasPlayerBeenSpottedInStolenVehicle(player)
```
```c
BOOL HAS_PLAYER_BEEN_SPOTTED_IN_STOLEN_VEHICLE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### HasPlayerDamagedAtLeastOneNonAnimalPed

`HAS_PLAYER_DAMAGED_AT_LEAST_ONE_NON_ANIMAL_PED` · hash `0xE4B90F367BD81752` · jhash `0xA3707DFC` · **Cliente**

```lua
local retval = HasPlayerDamagedAtLeastOneNonAnimalPed(player)
```
```c
BOOL HAS_PLAYER_DAMAGED_AT_LEAST_ONE_NON_ANIMAL_PED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### HasPlayerDamagedAtLeastOnePed

`HAS_PLAYER_DAMAGED_AT_LEAST_ONE_PED` · hash `0x20CE80B0C2BF4ACC` · jhash `0x14F52453` · **Cliente**

```lua
local retval = HasPlayerDamagedAtLeastOnePed(player)
```
```c
BOOL HAS_PLAYER_DAMAGED_AT_LEAST_ONE_PED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### HasPlayerLeftTheWorld

`HAS_PLAYER_LEFT_THE_WORLD` · hash `0xD55DDFB47991A294` · jhash `0xFEA40B6C` · **Cliente**

```lua
local retval = HasPlayerLeftTheWorld(player)
```
```c
BOOL HAS_PLAYER_LEFT_THE_WORLD(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IntToParticipantindex

`INT_TO_PARTICIPANTINDEX` · hash `0x9EC6603812C24710` · jhash `0x98F3B274` · **Cliente**

```lua
local retval = IntToParticipantindex(value)
```
```c
int INT_TO_PARTICIPANTINDEX(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Simply returns whatever is passed to it (Regardless of whether the handle is valid or not).  
--------------------------------------------------------  
if (NETWORK::NETWORK_IS_PARTICIPANT_ACTIVE(PLAYER::INT_TO_PARTICIPANTINDEX(i)))  
```

---
### IntToPlayerindex

`INT_TO_PLAYERINDEX` · hash `0x41BD2A6B006AF756` · jhash `0x98DD98F1` · **Cliente**

```lua
local retval = IntToPlayerindex(value)
```
```c
Player INT_TO_PLAYERINDEX(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `Player`

**Descripción oficial:**

```
Simply returns whatever is passed to it (Regardless of whether the handle is valid or not).  
```

---
### IsPlayerBattleAware

`IS_PLAYER_BATTLE_AWARE` · hash `0x38D28DA81E4E9BF9` · jhash `0x013B4F72` · **Cliente**

```lua
local retval = IsPlayerBattleAware(player)
```
```c
BOOL IS_PLAYER_BATTLE_AWARE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if an unk value is greater than 0.0f  
```

**Nombres antiguos (alias):** `0x38D28DA81E4E9BF9` (`N_0x38d28da81e4e9bf9`)

---
### IsPlayerBeingArrested

`IS_PLAYER_BEING_ARRESTED` · hash `0x388A47C51ABDAC8E` · jhash `0x7F6A60D3` · **Cliente**

```lua
local retval = IsPlayerBeingArrested(player, atArresting)
```
```c
BOOL IS_PLAYER_BEING_ARRESTED(Player player, BOOL atArresting);
```

**Parámetros**

- `player` (`Player`)
- `atArresting` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Return true while player is being arrested / busted.  
If atArresting is set to 1, this function will return 1 when player is being arrested (while player is putting his hand up, but still have control)  
If atArresting is set to 0, this function will return 1 only when the busted screen is shown.  
```

---
### IsPlayerBluetoothEnable

`IS_PLAYER_BLUETOOTH_ENABLE` · hash `0x65FAEE425DE637B0` · jhash `0xEA01BD4A` · **Cliente**

```lua
local retval = IsPlayerBluetoothEnable(player)
```
```c
BOOL IS_PLAYER_BLUETOOTH_ENABLE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x65FAEE425DE637B0` (`N_0x65faee425de637b0`)

---
### IsPlayerClimbing

`IS_PLAYER_CLIMBING` · hash `0x95E8F73DC65EFB9C` · jhash `0x4A9E9AE0` · **Cliente**

```lua
local retval = IsPlayerClimbing(player)
```
```c
BOOL IS_PLAYER_CLIMBING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns TRUE if the player ('s ped) is climbing at the moment.  
```

---
### IsPlayerControlOn

`IS_PLAYER_CONTROL_ON` · hash `0x49C32D60007AFA47` · jhash `0x618857F2` · **Cliente**

```lua
local retval = IsPlayerControlOn(player)
```
```c
BOOL IS_PLAYER_CONTROL_ON(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Can the player control himself, used to disable controls for player for things like a cutscene.  
---  
You can't disable controls with this, use SET_PLAYER_CONTROL(...) for this.  
```

---
### IsPlayerDead

`IS_PLAYER_DEAD` · hash `0x424D4687FA1E5652` · jhash `0x140CA5A8` · **Cliente**

```lua
local retval = IsPlayerDead(player)
```
```c
BOOL IS_PLAYER_DEAD(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IsPlayerDrivingDangerously

`_IS_PLAYER_DRIVING_DANGEROUSLY` · hash `0xF10B44FD479D69F3` · jhash `0x1E359CC8` · **Cliente**

```lua
local retval = IsPlayerDrivingDangerously(player, type)
```
```c
BOOL _IS_PLAYER_DRIVING_DANGEROUSLY(Player player, int type);
```

**Parámetros**

- `player` (`Player`): Player ID
- `type` (`int`): Refer to `eViolationType`.

**Devuelve:** `BOOL` — Returns true if the player is performing the `type` traffic violation.

**Descripción oficial:**

```cpp
enum eViolationType {
  // Checks if the player is driving on pedestrians walk ways
  VT_PAVED_PEDESTRIAN_AREAS = 0,
  // Checks if the player is running through red lights
  // This takes some time to return true.
  VT_RUNNING_REDS = 1,
  // checks if the player is driving on the wrong side of the road
  VT_AGAINST_TRAFFIC = 2
};
```

Used solely in "Al Di Napoli" with type 2 for a voiceline.

**Nombres antiguos (alias):** `0xF10B44FD479D69F3` (`N_0xf10b44fd479d69f3`)

---
### IsPlayerFreeAiming

`IS_PLAYER_FREE_AIMING` · hash `0x2E397FD2ECD37C87` · jhash `0x1DEC67B7` · **Cliente**

```lua
local retval = IsPlayerFreeAiming(player)
```
```c
BOOL IS_PLAYER_FREE_AIMING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets a value indicating whether the specified player is currently aiming freely.  
```

---
### IsPlayerFreeAimingAtEntity

`IS_PLAYER_FREE_AIMING_AT_ENTITY` · hash `0x3C06B5C839B38F7B` · jhash `0x7D80EEAA` · **Cliente**

```lua
local retval = IsPlayerFreeAimingAtEntity(player, entity)
```
```c
BOOL IS_PLAYER_FREE_AIMING_AT_ENTITY(Player player, Entity entity);
```

**Parámetros**

- `player` (`Player`)
- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets a value indicating whether the specified player is currently aiming freely at the specified entity.  
```

---
### IsPlayerFreeForAmbientTask

`IS_PLAYER_FREE_FOR_AMBIENT_TASK` · hash `0xDCCFD3F106C36AB4` · jhash `0x85C7E232` · **Cliente**

```lua
local retval = IsPlayerFreeForAmbientTask(player)
```
```c
BOOL IS_PLAYER_FREE_FOR_AMBIENT_TASK(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IsPlayerLoggingInNp

`IS_PLAYER_LOGGING_IN_NP` · hash `0x74556E1420867ECA` · jhash `0x8F72FAD0` · **Cliente**

```lua
local retval = IsPlayerLoggingInNp()
```
```c
BOOL IS_PLAYER_LOGGING_IN_NP();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
this function is hard-coded to always return 0.  
```

---
### IsPlayerOnline

`IS_PLAYER_ONLINE` · hash `0xF25D331DC2627BBC` · jhash `0x9FAB6729` · **Cliente**

```lua
local retval = IsPlayerOnline()
```
```c
BOOL IS_PLAYER_ONLINE();
```

**Devuelve:** `BOOL` — It provides a true value if the game is in online mode and false if it's in offline mode.

**Descripción oficial:**

It returns true if the player is online, suggesting they are also logged in locally. Note that this is an alias for `NETWORK_IS_SIGNED_ONLINE`.

---
### IsPlayerPlaying

`IS_PLAYER_PLAYING` · hash `0x5E9564D8246B909A` · jhash `0xE15D777F` · **Cliente**

```lua
local retval = IsPlayerPlaying(player)
```
```c
BOOL IS_PLAYER_PLAYING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks whether the specified player has a Ped, the Ped is not dead, is not injured and is not arrested.  
```

---
### IsPlayerPressingHorn

`IS_PLAYER_PRESSING_HORN` · hash `0xFA1E2BF8B10598F9` · jhash `0xED1D1662` · **Cliente**

```lua
local retval = IsPlayerPressingHorn(player)
```
```c
BOOL IS_PLAYER_PRESSING_HORN(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IsPlayerReadyForCutscene

`IS_PLAYER_READY_FOR_CUTSCENE` · hash `0x908CBECC2CAA3690` · jhash `0xBB77E9CD` · **Cliente**

```lua
local retval = IsPlayerReadyForCutscene(player)
```
```c
BOOL IS_PLAYER_READY_FOR_CUTSCENE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IsPlayerRidingTrain

`IS_PLAYER_RIDING_TRAIN` · hash `0x4EC12697209F2196` · jhash `0x9765E71D` · **Cliente**

```lua
local retval = IsPlayerRidingTrain(player)
```
```c
BOOL IS_PLAYER_RIDING_TRAIN(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the player is riding a train.  
```

---
### IsPlayerScriptControlOn

`IS_PLAYER_SCRIPT_CONTROL_ON` · hash `0x8A876A65283DD7D7` · jhash `0x61B00A84` · **Cliente**

```lua
local retval = IsPlayerScriptControlOn(player)
```
```c
BOOL IS_PLAYER_SCRIPT_CONTROL_ON(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IsPlayerTargettingAnything

`IS_PLAYER_TARGETTING_ANYTHING` · hash `0x78CFE51896B6B8A4` · jhash `0x456DB50D` · **Cliente**

```lua
local retval = IsPlayerTargettingAnything(player)
```
```c
BOOL IS_PLAYER_TARGETTING_ANYTHING(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

---
### IsPlayerTargettingEntity

`IS_PLAYER_TARGETTING_ENTITY` · hash `0x7912F7FC4F6264B6` · jhash `0xF3240B77` · **Cliente**

```lua
local retval = IsPlayerTargettingEntity(player, entity)
```
```c
BOOL IS_PLAYER_TARGETTING_ENTITY(Player player, Entity entity);
```

**Parámetros**

- `player` (`Player`)
- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsPlayerTeleportActive

`IS_PLAYER_TELEPORT_ACTIVE` · hash `0x02B15662D7F8886F` · jhash `0x3A11D118` · **Cliente**

```lua
local retval = IsPlayerTeleportActive()
```
```c
BOOL IS_PLAYER_TELEPORT_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsPlayerWantedLevelGreater

`IS_PLAYER_WANTED_LEVEL_GREATER` · hash `0x238DB2A2C23EE9EF` · jhash `0x589A2661` · **Cliente**

```lua
local retval = IsPlayerWantedLevelGreater(player, wantedLevel)
```
```c
BOOL IS_PLAYER_WANTED_LEVEL_GREATER(Player player, int wantedLevel);
```

**Parámetros**

- `player` (`Player`)
- `wantedLevel` (`int`)

**Devuelve:** `BOOL`

---
### IsSpecialAbilityActive

`IS_SPECIAL_ABILITY_ACTIVE` · hash `0x3E5F7FC85D854E15` · jhash `0x1B17E334` · **Cliente**

```lua
local retval = IsSpecialAbilityActive(player)
```
```c
BOOL IS_SPECIAL_ABILITY_ACTIVE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### IsSpecialAbilityEnabled

`IS_SPECIAL_ABILITY_ENABLED` · hash `0xB1D200FE26AEF3CB` · jhash `0xC01238CC` · **Cliente**

```lua
local retval = IsSpecialAbilityEnabled(player)
```
```c
BOOL IS_SPECIAL_ABILITY_ENABLED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### IsSpecialAbilityMeterFull

`IS_SPECIAL_ABILITY_METER_FULL` · hash `0x05A1FE504B7F2587` · jhash `0x2E19D7F6` · **Cliente**

```lua
local retval = IsSpecialAbilityMeterFull(player)
```
```c
BOOL IS_SPECIAL_ABILITY_METER_FULL(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### IsSpecialAbilityUnlocked

`IS_SPECIAL_ABILITY_UNLOCKED` · hash `0xC6017F6A6CDFA694` · jhash `0xC9C75E82` · **Cliente**

```lua
local retval = IsSpecialAbilityUnlocked(playerModel)
```
```c
BOOL IS_SPECIAL_ABILITY_UNLOCKED(Hash playerModel);
```

**Parámetros**

- `playerModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsSystemUiBeingDisplayed

`IS_SYSTEM_UI_BEING_DISPLAYED` · hash `0x5D511E3867C87139` · jhash `0xE495B6DA` · **Cliente**

```lua
local retval = IsSystemUiBeingDisplayed()
```
```c
BOOL IS_SYSTEM_UI_BEING_DISPLAYED();
```

**Devuelve:** `BOOL`

---
### N_0x0032a6dba562c518

`0x0032A6DBA562C518` · hash `0x0032A6DBA562C518` · jhash `0x47CAB814` · **Cliente**

```lua
N_0x0032a6dba562c518()
```
```c
void 0x0032A6DBA562C518();
```

**Devuelve:** `void`

**Descripción oficial:**

```
2 matches in 1 script - am_hold_up
Used in multiplayer scripts?
```

---
### N_0x237440e46d918649

`0x237440E46D918649` · hash `0x237440E46D918649` · **Cliente**

```lua
N_0x237440e46d918649(p0)
```
```c
void 0x237440E46D918649(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x2382ab11450ae7ba

`0x2382AB11450AE7BA` · hash `0x2382AB11450AE7BA` · **Cliente**

```lua
N_0x2382ab11450ae7ba(p0, p1)
```
```c
void 0x2382AB11450AE7BA(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x2f41a3bae005e5fa

`0x2F41A3BAE005E5FA` · hash `0x2F41A3BAE005E5FA` · **Cliente**

```lua
N_0x2f41a3bae005e5fa(p0, p1)
```
```c
void 0x2F41A3BAE005E5FA(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x2f7ceb6520288061

`0x2F7CEB6520288061` · hash `0x2F7CEB6520288061` · jhash `0x2849D4B2` · **Cliente**

```lua
N_0x2f7ceb6520288061(p0)
```
```c
void 0x2F7CEB6520288061(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used with radios:
void sub_cf383(auto _a0) {
    if ((a_0)==1) {
        if (MISC::IS_BIT_SET((g_240005._f1), 3)) {
            PLAYER::_2F7CEB6520288061(0);
            AUDIO::SET_AUDIO_FLAG("AllowRadioDuringSwitch", 0);
            AUDIO::SET_MOBILE_PHONE_RADIO_STATE(0);
            AUDIO::SET_AUDIO_FLAG("MobileRadioInGame", 0);
        }
        sub_cf3f6(1);
    } else {
        if (MISC::IS_BIT_SET((g_240005._f1), 3)) {
            PLAYER::_2F7CEB6520288061(1);
            AUDIO::SET_AUDIO_FLAG("AllowRadioDuringSwitch", 1);
            AUDIO::SET_MOBILE_PHONE_RADIO_STATE(1);
            AUDIO::SET_AUDIO_FLAG("MobileRadioInGame", 1);
        }
        sub_cf3f6(0);
    }
}
SET_PLAYER_S*
```

---
### N_0x31e90b8873a4cd3b

`0x31E90B8873A4CD3B` · hash `0x31E90B8873A4CD3B` · **Cliente**

```lua
N_0x31e90b8873a4cd3b(player, p1)
```
```c
void 0x31E90B8873A4CD3B(Player player, float p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0x36f1b38855f2a8df

`0x36F1B38855F2A8DF` · hash `0x36F1B38855F2A8DF` · jhash `0x3A7E5FB6` · **Cliente**

```lua
N_0x36f1b38855f2a8df(player)
```
```c
void 0x36F1B38855F2A8DF(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### N_0x4669b3ed80f24b4e

`0x4669B3ED80F24B4E` · hash `0x4669B3ED80F24B4E` · jhash `0xB9FB142F` · **Cliente**

```lua
N_0x4669b3ed80f24b4e(player)
```
```c
void 0x4669B3ED80F24B4E(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
This has been found in use in the decompiled files.  
```

---
### N_0x5501b7a5cdb79d37

`0x5501B7A5CDB79D37` · hash `0x5501B7A5CDB79D37` · **Cliente**

```lua
N_0x5501b7a5cdb79d37(player)
```
```c
void 0x5501B7A5CDB79D37(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
Name between DISABLE_ALL_CONTROL_ACTIONS and DISABLE_CONTROL_ACTION
```

---
### N_0x55fcc0c390620314

`0x55FCC0C390620314` · hash `0x55FCC0C390620314` · **Cliente**

```lua
N_0x55fcc0c390620314(player1, player2, toggle)
```
```c
void 0x55FCC0C390620314(Player player1, Player player2, BOOL toggle);
```

**Parámetros**

- `player1` (`Player`)
- `player2` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x690a61a6d13583f6

`0x690A61A6D13583F6` · hash `0x690A61A6D13583F6` · jhash `0x1D371529` · **Cliente**

```lua
local retval = N_0x690a61a6d13583f6(player)
```
```c
BOOL 0x690A61A6D13583F6(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_*
```

---
### N_0x6e4361ff3e8cd7ca

`0x6E4361FF3E8CD7CA` · hash `0x6E4361FF3E8CD7CA` · **Cliente**

```lua
local retval = N_0x6e4361ff3e8cd7ca(p0)
```
```c
Any 0x6E4361FF3E8CD7CA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x70a382adec069dd3

`0x70A382ADEC069DD3` · hash `0x70A382ADEC069DD3` · **Cliente**

```lua
N_0x70a382adec069dd3(coordX, coordY, coordZ)
```
```c
void 0x70A382ADEC069DD3(float coordX, float coordY, float coordZ);
```

**Parámetros**

- `coordX` (`float`)
- `coordY` (`float`)
- `coordZ` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x7148e0f43d11f0d9

`0x7148E0F43D11F0D9` · hash `0x7148E0F43D11F0D9` · **Cliente**

```lua
N_0x7148e0f43d11f0d9()
```
```c
void 0x7148E0F43D11F0D9();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x7bae68775557ae0b

`0x7BAE68775557AE0B` · hash `0x7BAE68775557AE0B` · **Cliente**

```lua
N_0x7bae68775557ae0b(p0, p1, p2, p3, p4, p5)
```
```c
void 0x7BAE68775557AE0B(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x7e07c78925d5fd96

`0x7E07C78925D5FD96` · hash `0x7E07C78925D5FD96` · **Cliente**

```lua
local retval = N_0x7e07c78925d5fd96(p0)
```
```c
Any 0x7E07C78925D5FD96(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x823ec8e82ba45986

`0x823EC8E82BA45986` · hash `0x823EC8E82BA45986` · **Cliente**

```lua
N_0x823ec8e82ba45986(p0)
```
```c
void 0x823EC8E82BA45986(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0x8d768602adef2245

`0x8D768602ADEF2245` · hash `0x8D768602ADEF2245` · **Cliente**

```lua
N_0x8d768602adef2245(player, p1)
```
```c
void 0x8D768602ADEF2245(Player player, float p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PLAYER_MAX_*
```

---
### N_0x9097eb6d4bb9a12a

`0x9097EB6D4BB9A12A` · hash `0x9097EB6D4BB9A12A` · **Cliente**

```lua
N_0x9097eb6d4bb9a12a(player, entity)
```
```c
void 0x9097EB6D4BB9A12A(Player player, Entity entity);
```

**Parámetros**

- `player` (`Player`)
- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

ADD_\*

```
NativeDB Introduced: v1868
```

---
### N_0x9edd76e87d5d51ba

`0x9EDD76E87D5D51BA` · hash `0x9EDD76E87D5D51BA` · jhash `0xE30A64DC` · **Cliente**

```lua
N_0x9edd76e87d5d51ba(player)
```
```c
void 0x9EDD76E87D5D51BA(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### N_0x9f260bfb59adbca3

`0x9F260BFB59ADBCA3` · hash `0x9F260BFB59ADBCA3` · **Cliente**

```lua
N_0x9f260bfb59adbca3(player, entity)
```
```c
void 0x9F260BFB59ADBCA3(Player player, Entity entity);
```

**Parámetros**

- `player` (`Player`)
- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

REMOVE_\*

```
NativeDB Introduced: v1868
```

---
### N_0xad73ce5a09e42d12

`0xAD73CE5A09E42D12` · hash `0xAD73CE5A09E42D12` · jhash `0x85725848` · **Cliente**

```lua
N_0xad73ce5a09e42d12(player)
```
```c
void 0xAD73CE5A09E42D12(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
This has been found in use in the decompiled files.  
```

---
### N_0xb45eff719d8427a6

`0xB45EFF719D8427A6` · hash `0xB45EFF719D8427A6` · jhash `0xBF6993C7` · **Cliente**

```lua
N_0xb45eff719d8427a6(p0)
```
```c
void 0xB45EFF719D8427A6(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
PLAYER::0xBF6993C7(rPtr((&l_122) + 71)); // Found in decompilation
***
In "am_hold_up.ysc" used once:
l_8d._f47 = MISC::GET_RANDOM_FLOAT_IN_RANGE(18.0, 28.0);
PLAYER::_B45EFF719D8427A6((l_8d._f47));
```

---
### N_0xb885852c39cc265d

`0xB885852C39CC265D` · hash `0xB885852C39CC265D` · jhash `0x47D6004E` · **Cliente**

```lua
N_0xb885852c39cc265d()
```
```c
void 0xB885852C39CC265D();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Disables something. Used only once in R* scripts (freemode.ysc).
DISABLE_PLAYER_*
```

---
### N_0xb9cf1f793a9f1bf1

`0xB9CF1F793A9F1BF1` · hash `0xB9CF1F793A9F1BF1` · **Cliente**

```lua
local retval = N_0xb9cf1f793a9f1bf1()
```
```c
BOOL 0xB9CF1F793A9F1BF1();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns profile setting 237.
GET_*
```

---
### N_0xbc9490ca15aea8fb

`0xBC9490CA15AEA8FB` · hash `0xBC9490CA15AEA8FB` · jhash `0x6B34A160` · **Cliente**

```lua
N_0xbc9490ca15aea8fb(player)
```
```c
void 0xBC9490CA15AEA8FB(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
Seems to only appear in scripts used in Singleplayer.  
Always used like this in scripts  
PLAYER::_BC9490CA15AEA8FB(PLAYER::PLAYER_ID());  
```

---
### N_0xc3376f42b1faccc6

`0xC3376F42B1FACCC6` · hash `0xC3376F42B1FACCC6` · jhash `0x02DF7AF4` · **Cliente**

```lua
N_0xc3376f42b1faccc6(player)
```
```c
void 0xC3376F42B1FACCC6(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
- This is called after SET_ALL_RANDOM_PEDS_FLEE_THIS_FRAME
```

**Nombres antiguos (alias):** `SET_AREAS_GENERATOR_ORIENTATION` (`SetAreasGeneratorOrientation`)

---
### N_0xcac57395b151135f

`0xCAC57395B151135F` · hash `0xCAC57395B151135F` · jhash `0x00563E0D` · **Cliente**

```lua
N_0xcac57395b151135f(player, p1)
```
```c
void 0xCAC57395B151135F(Player player, BOOL p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Found in "director_mode", "fm_bj_race_controler", "fm_deathmatch_controler", "fm_impromptu_dm_controler", "fm_race_controler", "gb_deathmatch".  
```

---
### N_0xcb645e85e97ea48b

`0xCB645E85E97EA48B` · hash `0xCB645E85E97EA48B` · **Cliente**

```lua
local retval = N_0xcb645e85e97ea48b()
```
```c
BOOL 0xCB645E85E97EA48B();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns profile setting 243.
GET_*
```

---
### N_0xd821056b9acf8052

`0xD821056B9ACF8052` · hash `0xD821056B9ACF8052` · **Cliente**

```lua
N_0xd821056b9acf8052(player, p1)
```
```c
void 0xD821056B9ACF8052(Player player, Any p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xdcc07526b8ec45af

`0xDCC07526B8EC45AF` · hash `0xDCC07526B8EC45AF` · **Cliente**

```lua
local retval = N_0xdcc07526b8ec45af(player)
```
```c
BOOL 0xDCC07526B8EC45AF(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Always returns false.

```
NativeDB Introduced: v1868
```

---
### N_0xdd2620b7b9d16ff1

`0xDD2620B7B9D16FF1` · hash `0xDD2620B7B9D16FF1` · jhash `0x8CB53C9F` · **Cliente**

```lua
local retval = N_0xdd2620b7b9d16ff1(player, p1)
```
```c
BOOL 0xDD2620B7B9D16FF1(Player player, float p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
2 occurrences in agency_heist3a. p1 was 0.7f then 0.4f.  
```

---
### N_0xde45d1a1ef45ee61

`0xDE45D1A1EF45EE61` · hash `0xDE45D1A1EF45EE61` · jhash `0x274631FE` · **Cliente**

```lua
N_0xde45d1a1ef45ee61(player, toggle)
```
```c
void 0xDE45D1A1EF45EE61(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `SET_HUD_ANIM_STOP_LEVEL` (`SetHudAnimStopLevel`)

---
### N_0xfac75988a7d078d3

`0xFAC75988A7D078D3` · hash `0xFAC75988A7D078D3` · **Cliente**

```lua
N_0xfac75988a7d078d3(player)
```
```c
void 0xFAC75988A7D078D3(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### N_0xffee8fa29ab9a18e

`0xFFEE8FA29AB9A18E` · hash `0xFFEE8FA29AB9A18E` · jhash `0x5D0FE25B` · **Cliente**

```lua
N_0xffee8fa29ab9a18e(player)
```
```c
void 0xFFEE8FA29AB9A18E(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### NetworkPlayerIdToInt

`NETWORK_PLAYER_ID_TO_INT` · hash `0xEE68096F9F37341E` · jhash `0x8DD5B838` · **Cliente**

```lua
local retval = NetworkPlayerIdToInt()
```
```c
int NETWORK_PLAYER_ID_TO_INT();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Does exactly the same thing as PLAYER_ID()  
```

---
### PlayerAttachVirtualBound

`PLAYER_ATTACH_VIRTUAL_BOUND` · hash `0xED51733DC73AED51` · jhash `0xECD12E60` · **Cliente**

```lua
PlayerAttachVirtualBound(p0, p1, p2, p3, p4, p5, p6, p7)
```
```c
void PLAYER_ATTACH_VIRTUAL_BOUND(float p0, float p1, float p2, float p3, float p4, float p5, float p6, float p7);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only 1 match. ob_sofa_michael.  
PLAYER::PLAYER_ATTACH_VIRTUAL_BOUND(-804.5928f, 173.1801f, 71.68436f, 0f, 0f, 0.590625f, 1f, 0.7f);1.0.335.2, 1.0.350.1/2, 1.0.372.2, 1.0.393.2, 1.0.393.4, 1.0.463.1;  
```

---
### PlayerDetachVirtualBound

`PLAYER_DETACH_VIRTUAL_BOUND` · hash `0x1DD5897E2FA6E7C9` · jhash `0x96100EA4` · **Cliente**

```lua
PlayerDetachVirtualBound()
```
```c
void PLAYER_DETACH_VIRTUAL_BOUND();
```

**Devuelve:** `void`

**Descripción oficial:**

```
1.0.335.2, 1.0.350.1/2, 1.0.372.2, 1.0.393.2, 1.0.393.4, 1.0.463.1;  
```

---
### PlayerId

`PLAYER_ID` · hash `0x4F8644AF03D0E0D6` · jhash `0x8AEA886C` · **Cliente**

```lua
local retval = PlayerId()
```
```c
Player PLAYER_ID();
```

**Devuelve:** `Player` — The local player's player index.

**Descripción oficial:**

Returns the player index for the local player.

---
### PlayerPedId

`PLAYER_PED_ID` · hash `0xD80958FC74E988A6` · jhash `0xFA92E226` · **Cliente**

```lua
local retval = PlayerPedId()
```
```c
Ped PLAYER_PED_ID();
```

**Devuelve:** `Ped` — The local player ped's entity handle.

**Descripción oficial:**

Returns the entity handle for the local player ped. Note that this entity handle will change after using commands such as SET_PLAYER_MODEL.

---
### RemovePlayerHelmet

`REMOVE_PLAYER_HELMET` · hash `0xF3AC26D3CC576528` · jhash `0x6255F3B4` · **Cliente**

```lua
RemovePlayerHelmet(player, p2)
```
```c
void REMOVE_PLAYER_HELMET(Player player, BOOL p2);
```

**Parámetros**

- `player` (`Player`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### ReportCrime

`REPORT_CRIME` · hash `0xE9B09589827545E7` · jhash `0xD8EB3A44` · **Cliente**

```lua
ReportCrime(player, crimeType, wantedLvlThresh)
```
```c
void REPORT_CRIME(Player player, int crimeType, int wantedLvlThresh);
```

**Parámetros**

- `player` (`Player`)
- `crimeType` (`int`)
- `wantedLvlThresh` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
PLAYER::REPORT_CRIME(PLAYER::PLAYER_ID(), 37, PLAYER::GET_WANTED_LEVEL_THRESHOLD(1));  
From am_armybase.ysc.c4:  
PLAYER::REPORT_CRIME(PLAYER::PLAYER_ID(4), 36, PLAYER::GET_WANTED_LEVEL_THRESHOLD(4));  
-----  
This was taken from the GTAV.exe v1.334. The function is called sub_140592CE8. For a full decompilation of the function, see here: pastebin.com/09qSMsN7   
-----  
crimeType:  
1: Firearms possession  
2: Person running a red light ("5-0-5")  
3: Reckless driver  
4: Speeding vehicle (a "5-10")  
5: Traffic violation (a "5-0-5")  
6: Motorcycle rider without a helmet  
7: Vehicle theft (a "5-0-3")  
8: Grand Theft Auto  
9: ???  
10: ???  
11: Assault on a civilian (a "2-40")  
12: Assault on an officer  
13: Assault with a deadly weapon (a "2-45")  
14: Officer shot (a "2-45")  
15: Pedestrian struck by a vehicle  
16: Officer struck by a vehicle  
17: Helicopter down (an "AC"?)  
18: Civilian on fire (a "2-40")  
19: Officer set on fire (a "10-99")  
20: Car on fire  
21: Air unit down (an "AC"?)  
22: An explosion (a "9-96")  
23: A stabbing (a "2-45") (also something else I couldn't understand)  
24: Officer stabbed (also something else I couldn't understand)  
25: Attack on a vehicle ("MDV"?)  
26: Damage to property  
27: Suspect threatening officer with a firearm  
28: Shots fired  
29: ???  
30: ???  
31: ???  
32: ???  
33: ???  
34: A "2-45"  
35: ???  
36: A "9-25"  
37: ???  
38: ???  
39: ???  
40: ???  
41: ???  
42: ???  
43: Possible disturbance  
44: Civilian in need of assistance  
45: ???  
46: ???  
```

---
### ReportPoliceSpottedPlayer

`REPORT_POLICE_SPOTTED_PLAYER` · hash `0xDC64D2C53493ED12` · jhash `0xD15C4B1C` · **Cliente**

```lua
ReportPoliceSpottedPlayer(player)
```
```c
void REPORT_POLICE_SPOTTED_PLAYER(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDC64D2C53493ED12` (`N_0xdc64d2c53493ed12`)

---
### ResetPlayerArrestState

`RESET_PLAYER_ARREST_STATE` · hash `0x2D03E13C460760D6` · jhash `0x453C7CAB` · **Cliente**

```lua
ResetPlayerArrestState(player)
```
```c
void RESET_PLAYER_ARREST_STATE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ResetPlayerInputGait

`RESET_PLAYER_INPUT_GAIT` · hash `0x19531C47A2ABD691` · jhash `0x4A701EE1` · **Cliente**

```lua
ResetPlayerInputGait(player)
```
```c
void RESET_PLAYER_INPUT_GAIT(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ResetPlayerStamina

`RESET_PLAYER_STAMINA` · hash `0xA6F312FCCE9C1DFE` · jhash `0xC0445A9C` · **Cliente**

```lua
ResetPlayerStamina(player)
```
```c
void RESET_PLAYER_STAMINA(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ResetWantedLevelDifficulty

`RESET_WANTED_LEVEL_DIFFICULTY` · hash `0xB9D0DD990DC141DD` · jhash `0xA64C378D` · **Cliente**

```lua
ResetWantedLevelDifficulty(player)
```
```c
void RESET_WANTED_LEVEL_DIFFICULTY(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### ResetWorldBoundaryForPlayer

`RESET_WORLD_BOUNDARY_FOR_PLAYER` · hash `0xDA1DF03D5A315F4E` · jhash `0xA97C2F6C` · **Cliente**

```lua
ResetWorldBoundaryForPlayer()
```
```c
void RESET_WORLD_BOUNDARY_FOR_PLAYER();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### RestorePlayerStamina

`RESTORE_PLAYER_STAMINA` · hash `0xA352C1B864CAFD33` · jhash `0x62A93608` · **Cliente**

```lua
RestorePlayerStamina(player, percentage)
```
```c
void RESTORE_PLAYER_STAMINA(Player player, float percentage);
```

**Parámetros**

- `player` (`Player`): player to restore the stamina for
- `percentage` (`float`): seems to be a percentage that ranges from 0.0 to 1.0 (1.0 being 100%)

**Devuelve:** `void`

**Descripción oficial:**

Adds a percentage to a players stamina

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
  while true do
    RestorePlayerStamina(PlayerId(), 0.3)
    Citizen.Wait(15000) -- 15 seconds
  end
end)
```

---
### SetAchievementProgress

`_SET_ACHIEVEMENT_PROGRESS` · hash `0xC2AFFFDABBDC2C5C` · **Cliente**

```lua
local retval = SetAchievementProgress(achievement, progress)
```
```c
BOOL _SET_ACHIEVEMENT_PROGRESS(int achievement, int progress);
```

**Parámetros**

- `achievement` (`int`)
- `progress` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

For Steam.
Does nothing and always returns false in the retail version of the game.

**Nombres antiguos (alias):** `0xC2AFFFDABBDC2C5C` (`N_0xc2afffdabbdc2c5c`), `_SET_ACHIEVEMENT_PROGRESSION` (`SetAchievementProgression`)

---
### SetAirDragMultiplierForPlayersVehicle

`SET_AIR_DRAG_MULTIPLIER_FOR_PLAYERS_VEHICLE` · hash `0xCA7DC8329F0A1E9E` · jhash `0xF20F72E5` · **Cliente**

```lua
SetAirDragMultiplierForPlayersVehicle(player, multiplier)
```
```c
void SET_AIR_DRAG_MULTIPLIER_FOR_PLAYERS_VEHICLE(Player player, float multiplier);
```

**Parámetros**

- `player` (`Player`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This can be between 1.0f - 14.9f   
You can change the max in IDA from 15.0. I say 15.0 as the function blrs if what you input is greater than or equal to 15.0 hence why it's 14.9 max default.  
On PC the multiplier can be between 0.0f and 50.0f (inclusive).  
```

---
### SetAllRandomPedsFlee

`SET_ALL_RANDOM_PEDS_FLEE` · hash `0x056E0FE8534C2949` · jhash `0x49EAE968` · **Cliente**

```lua
SetAllRandomPedsFlee(player, toggle)
```
```c
void SET_ALL_RANDOM_PEDS_FLEE(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`): The Player ID for whom you want to set this behavior.
- `toggle` (`BOOL`): true/false.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether all random peds will run away from the player if they are agitated (threatened) (bool=true), or if they will stand their ground (bool=false).

---
### SetAllRandomPedsFleeThisFrame

`SET_ALL_RANDOM_PEDS_FLEE_THIS_FRAME` · hash `0x471D2FF42A94B4F2` · jhash `0xBF974891` · **Cliente**

```lua
SetAllRandomPedsFleeThisFrame(player)
```
```c
void SET_ALL_RANDOM_PEDS_FLEE_THIS_FRAME(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### SetAutoGiveParachuteWhenEnterPlane

`SET_AUTO_GIVE_PARACHUTE_WHEN_ENTER_PLANE` · hash `0x9F343285A00B4BB6` · jhash `0xA97C2059` · **Cliente**

```lua
SetAutoGiveParachuteWhenEnterPlane(player, toggle)
```
```c
void SET_AUTO_GIVE_PARACHUTE_WHEN_ENTER_PLANE(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetAutoGiveScubaGearWhenExitVehicle

`SET_AUTO_GIVE_SCUBA_GEAR_WHEN_EXIT_VEHICLE` · hash `0xD2B315B6689D537D` · jhash `0xA25D767E` · **Cliente**

```lua
SetAutoGiveScubaGearWhenExitVehicle(player, toggle)
```
```c
void SET_AUTO_GIVE_SCUBA_GEAR_WHEN_EXIT_VEHICLE(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD2B315B6689D537D` (`N_0xd2b315b6689d537d`)

---
### SetDisableAmbientMeleeMove

`SET_DISABLE_AMBIENT_MELEE_MOVE` · hash `0x2E8AABFA40A84F8C` · jhash `0xCCD937E7` · **Cliente**

```lua
SetDisableAmbientMeleeMove(player, toggle)
```
```c
void SET_DISABLE_AMBIENT_MELEE_MOVE(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetDispatchCopsForPlayer

`SET_DISPATCH_COPS_FOR_PLAYER` · hash `0xDB172424876553F4` · jhash `0x48A18913` · **Cliente**

```lua
SetDispatchCopsForPlayer(player, toggle)
```
```c
void SET_DISPATCH_COPS_FOR_PLAYER(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEveryoneIgnorePlayer

`SET_EVERYONE_IGNORE_PLAYER` · hash `0x8EEDA153AD141BA4` · jhash `0xC915285E` · **Cliente**

```lua
SetEveryoneIgnorePlayer(player, toggle)
```
```c
void SET_EVERYONE_IGNORE_PLAYER(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetIgnoreLowPriorityShockingEvents

`SET_IGNORE_LOW_PRIORITY_SHOCKING_EVENTS` · hash `0x596976B02B6B5700` · jhash `0xA3D675ED` · **Cliente**

```lua
SetIgnoreLowPriorityShockingEvents(player, toggle)
```
```c
void SET_IGNORE_LOW_PRIORITY_SHOCKING_EVENTS(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetMaxWantedLevel

`SET_MAX_WANTED_LEVEL` · hash `0xAA5F02DB48D704B9` · jhash `0x665A06F5` · **Cliente**

```lua
SetMaxWantedLevel(maxWantedLevel)
```
```c
void SET_MAX_WANTED_LEVEL(int maxWantedLevel);
```

**Parámetros**

- `maxWantedLevel` (`int`)

**Devuelve:** `void`

---
### SetPlayerBluetoothState

`SET_PLAYER_BLUETOOTH_STATE` · hash `0x5DC40A8869C22141` · jhash `0x7A6B0EF8` · **Cliente**

```lua
SetPlayerBluetoothState(player, state)
```
```c
void SET_PLAYER_BLUETOOTH_STATE(Player player, BOOL state);
```

**Parámetros**

- `player` (`Player`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5DC40A8869C22141` (`N_0x5dc40a8869c22141`)

---
### SetPlayerCanBeHassledByGangs

`SET_PLAYER_CAN_BE_HASSLED_BY_GANGS` · hash `0xD5E460AD7020A246` · jhash `0x71B305BB` · **Cliente**

```lua
SetPlayerCanBeHassledByGangs(player, toggle)
```
```c
void SET_PLAYER_CAN_BE_HASSLED_BY_GANGS(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets whether this player can be hassled by gangs.  
```

---
### SetPlayerCanDoDriveBy

`SET_PLAYER_CAN_DO_DRIVE_BY` · hash `0x6E8834B52EC20C77` · jhash `0xF4D99685` · **Cliente**

```lua
SetPlayerCanDoDriveBy(player, toggle)
```
```c
void SET_PLAYER_CAN_DO_DRIVE_BY(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`): The player to target.
- `toggle` (`BOOL`): If set to false, disables the players ability to do drive bys.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether the player is able to do drive-bys in vehicle (shooting & aiming in vehicles), this also includes middle finger taunts.

This is a toggle, it does not have to be ran every frame.

**Ejemplo (lua):**

```lua
SetPlayerCanDoDriveBy(PlayerId(), false)
```

---
### SetPlayerCanLeaveParachuteSmokeTrail

`SET_PLAYER_CAN_LEAVE_PARACHUTE_SMOKE_TRAIL` · hash `0xF401B182DBA8AF53` · jhash `0x832DEB7A` · **Cliente**

```lua
SetPlayerCanLeaveParachuteSmokeTrail(player, enabled)
```
```c
void SET_PLAYER_CAN_LEAVE_PARACHUTE_SMOKE_TRAIL(Player player, BOOL enabled);
```

**Parámetros**

- `player` (`Player`)
- `enabled` (`BOOL`)

**Devuelve:** `void`

---
### SetPlayerCanUseCover

`SET_PLAYER_CAN_USE_COVER` · hash `0xD465A8599DFF6814` · jhash `0x13CAFAFA` · **Cliente**

```lua
SetPlayerCanUseCover(player, toggle)
```
```c
void SET_PLAYER_CAN_USE_COVER(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets whether this player can take cover.
```

---
### SetPlayerClothLockCounter

`SET_PLAYER_CLOTH_LOCK_COUNTER` · hash `0x14D913B777DFF5DA` · jhash `0x8D9FD4D1` · **Cliente**

```lua
SetPlayerClothLockCounter(value)
```
```c
void SET_PLAYER_CLOTH_LOCK_COUNTER(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
6 matches across 4 scripts. 5 occurrences were 240. The other was 255.  
```

---
### SetPlayerClothPackageIndex

`SET_PLAYER_CLOTH_PACKAGE_INDEX` · hash `0x9F7BBA2EA6372500` · jhash `0xB8209F16` · **Cliente**

```lua
SetPlayerClothPackageIndex(index)
```
```c
void SET_PLAYER_CLOTH_PACKAGE_INDEX(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Every occurrence was either 0 or 2.  
```

---
### SetPlayerClothPinFrames

`SET_PLAYER_CLOTH_PIN_FRAMES` · hash `0x749FADDF97DFE930` · jhash `0xF7A0F00F` · **Cliente**

```lua
SetPlayerClothPinFrames(player, p1)
```
```c
void SET_PLAYER_CLOTH_PIN_FRAMES(Player player, int p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`int`)

**Devuelve:** `void`

---
### SetPlayerControl

`SET_PLAYER_CONTROL` · hash `0x8D32347D6D4C40A2` · jhash `0xD17AFCD8` · **Cliente · también en el servidor (RPC)**

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

---
### SetPlayerFallDistance

`_SET_PLAYER_FALL_DISTANCE` · hash `0xEFD79FA81DFBA9CB` · **Cliente**

```lua
SetPlayerFallDistance(player, distance)
```
```c
void _SET_PLAYER_FALL_DISTANCE(Player player, float distance);
```

**Parámetros**

- `player` (`Player`)
- `distance` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEFD79FA81DFBA9CB` (`N_0xefd79fa81dfba9cb`)

---
### SetPlayerForceSkipAimIntro

`SET_PLAYER_FORCE_SKIP_AIM_INTRO` · hash `0x7651BC64AE59E128` · jhash `0x374F42F0` · **Cliente**

```lua
SetPlayerForceSkipAimIntro(player, toggle)
```
```c
void SET_PLAYER_FORCE_SKIP_AIM_INTRO(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPlayerForcedAim

`SET_PLAYER_FORCED_AIM` · hash `0x0FEE4F80AC44A726` · jhash `0x94E42E2E` · **Cliente**

```lua
SetPlayerForcedAim(player, toggle)
```
```c
void SET_PLAYER_FORCED_AIM(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPlayerForcedZoom

`SET_PLAYER_FORCED_ZOOM` · hash `0x75E7D505F2B15902` · jhash `0xB0C576CB` · **Cliente**

```lua
SetPlayerForcedZoom(player, toggle)
```
```c
void SET_PLAYER_FORCED_ZOOM(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPlayerHasReserveParachute

`SET_PLAYER_HAS_RESERVE_PARACHUTE` · hash `0x7DDAB28D31FAC363` · jhash `0xA3E4798E` · **Cliente**

```lua
SetPlayerHasReserveParachute(player)
```
```c
void SET_PLAYER_HAS_RESERVE_PARACHUTE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### SetPlayerHealthRechargeLimit

`_SET_PLAYER_HEALTH_RECHARGE_LIMIT` · hash `0xC388A0F065F5BC34` · **Cliente**

```lua
SetPlayerHealthRechargeLimit(player, limit)
```
```c
void _SET_PLAYER_HEALTH_RECHARGE_LIMIT(Player player, float limit);
```

**Parámetros**

- `player` (`Player`): The local player ID.
- `limit` (`float`): A value between 0.0 and 1.0, 0.5 is default.

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC388A0F065F5BC34` (`N_0xc388a0f065f5bc34`)

---
### SetPlayerHealthRechargeMultiplier

`SET_PLAYER_HEALTH_RECHARGE_MULTIPLIER` · hash `0x5DB660B38DD98A31` · jhash `0x45514731` · **Cliente**

```lua
SetPlayerHealthRechargeMultiplier(player, regenRate)
```
```c
void SET_PLAYER_HEALTH_RECHARGE_MULTIPLIER(Player player, float regenRate);
```

**Parámetros**

- `player` (`Player`): The local player ID, see [PLAYER_ID](#playerid).
- `regenRate` (`float`): The recharge multiplier, this value needs to be a positive float value to work.

**Devuelve:** `void`

**Descripción oficial:**

This multiplier is reset to `1.0` every time the player ped is changed, often times via [`SET_PLAYER_MODEL`](../cfx/servidor.md#setplayermodel) or [`CHANGE_PLAYER_PED`](#changeplayerped).

**Ejemplo (lua):**

```lua
-- To disable the health recharge completely:
SetPlayerHealthRechargeMultiplier(PlayerId(), 0.0)

-- To reset it back to the normal recharge speed:
SetPlayerHealthRechargeMultiplier(PlayerId(), 1.0)
```

---
### SetPlayerHomingRocketDisabled

`_SET_PLAYER_HOMING_ROCKET_DISABLED` · hash `0xEE4EBDD2593BA844` · **Cliente**

```lua
SetPlayerHomingRocketDisabled(player, p1)
```
```c
void _SET_PLAYER_HOMING_ROCKET_DISABLED(Player player, BOOL p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0xEE4EBDD2593BA844` (`N_0xee4ebdd2593ba844`)

---
### SetPlayerInvincible

`SET_PLAYER_INVINCIBLE` · hash `0x239528EACDC3E7DE` · jhash `0xDFB9A2A2` · **Cliente · también en el servidor (RPC)**

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

---
### SetPlayerInvincibleKeepRagdollEnabled

`_SET_PLAYER_INVINCIBLE_KEEP_RAGDOLL_ENABLED` · hash `0x6BC97F4F4BB3C04B` · **Cliente**

```lua
SetPlayerInvincibleKeepRagdollEnabled(player, toggle)
```
```c
void _SET_PLAYER_INVINCIBLE_KEEP_RAGDOLL_ENABLED(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6BC97F4F4BB3C04B` (`N_0x6bc97f4f4bb3c04b`)

---
### SetPlayerLeavePedBehind

`SET_PLAYER_LEAVE_PED_BEHIND` · hash `0xFF300C7649724A0B` · jhash `0xAD8383FA` · **Cliente**

```lua
SetPlayerLeavePedBehind(player, toggle)
```
```c
void SET_PLAYER_LEAVE_PED_BEHIND(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFF300C7649724A0B` (`N_0xff300c7649724a0b`)

---
### SetPlayerLockon

`SET_PLAYER_LOCKON` · hash `0x5C8B2F450EE4328E` · jhash `0x0B270E0F` · **Cliente**

```lua
SetPlayerLockon(player, toggle)
```
```c
void SET_PLAYER_LOCKON(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`): The player ID to toggle the lock on for.
- `toggle` (`BOOL`): Set to false to prevent lock on, set to true to allow for lock on.

**Devuelve:** `void`

**Descripción oficial:**

```
Used to toggle the square up aim.
```

**Ejemplo (lua):**

```lua
local plyId = PlayerId()
SetPlayerLockon(plyId, false)
```

---
### SetPlayerLockonRangeOverride

`SET_PLAYER_LOCKON_RANGE_OVERRIDE` · hash `0x29961D490E5814FD` · jhash `0x74D42C03` · **Cliente**

```lua
SetPlayerLockonRangeOverride(player, range)
```
```c
void SET_PLAYER_LOCKON_RANGE_OVERRIDE(Player player, float range);
```

**Parámetros**

- `player` (`Player`)
- `range` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Affects the range of auto aim target.  
```

---
### SetPlayerMaxArmour

`SET_PLAYER_MAX_ARMOUR` · hash `0x77DFCCF5948B8C71` · jhash `0xC6C3C53B` · **Cliente**

```lua
SetPlayerMaxArmour(player, value)
```
```c
void SET_PLAYER_MAX_ARMOUR(Player player, int value);
```

**Parámetros**

- `player` (`Player`)
- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Default is 100. Use player id and not ped id. For instance: PLAYER::SET_PLAYER_MAX_ARMOUR(PLAYER::PLAYER_ID(), 100); // main_persistent.ct4  
```

---
### SetPlayerMayNotEnterAnyVehicle

`SET_PLAYER_MAY_NOT_ENTER_ANY_VEHICLE` · hash `0x1DE37BBF9E9CC14A` · jhash `0xAF7AFCC4` · **Cliente**

```lua
SetPlayerMayNotEnterAnyVehicle(player)
```
```c
void SET_PLAYER_MAY_NOT_ENTER_ANY_VEHICLE(Player player);
```

**Parámetros**

- `player` (`Player`): The player index.

**Devuelve:** `void`

**Descripción oficial:**

Establishes a reset flag to prevent the player from entering any vehicle. Not that this native must be called every frame.

---
### SetPlayerMayOnlyEnterThisVehicle

`SET_PLAYER_MAY_ONLY_ENTER_THIS_VEHICLE` · hash `0x8026FF78F208978A` · jhash `0xA454DD29` · **Cliente**

```lua
SetPlayerMayOnlyEnterThisVehicle(player, vehicle)
```
```c
void SET_PLAYER_MAY_ONLY_ENTER_THIS_VEHICLE(Player player, Vehicle vehicle);
```

**Parámetros**

- `player` (`Player`): The player index.
- `vehicle` (`Vehicle`): Vehicle id.

**Devuelve:** `void`

**Descripción oficial:**

Limit the player to only enter this vehicle. Note set vehicle to false if you want them to access any vehicle.

---
### SetPlayerMeleeWeaponDamageModifier

`SET_PLAYER_MELEE_WEAPON_DAMAGE_MODIFIER` · hash `0x4A3DC7ECCC321032` · jhash `0x362E69AD` · **Cliente**

```lua
SetPlayerMeleeWeaponDamageModifier(player, modifier)
```
```c
void SET_PLAYER_MELEE_WEAPON_DAMAGE_MODIFIER(Player player, float modifier);
```

**Parámetros**

- `player` (`Player`)
- `modifier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 3: BOOL p2
```

---
### SetPlayerMeleeWeaponDefenseModifier

`SET_PLAYER_MELEE_WEAPON_DEFENSE_MODIFIER` · hash `0xAE540335B4ABC4E2` · jhash `0x9F3D577F` · **Cliente**

```lua
SetPlayerMeleeWeaponDefenseModifier(player, modifier)
```
```c
void SET_PLAYER_MELEE_WEAPON_DEFENSE_MODIFIER(Player player, float modifier);
```

**Parámetros**

- `player` (`Player`)
- `modifier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
modifier's min value is 0.1
```

---
### SetPlayerModel

`SET_PLAYER_MODEL` · hash `0x00A1CADD00108836` · jhash `0x774A4C54` · **Cliente · también en el servidor (RPC)**

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

**Ejemplo (lua):**

```lua
local model = `a_f_m_beach_01`
if IsModelInCdimage(model) and IsModelValid(model) then
  RequestModel(model)
  while not HasModelLoaded(model) do
    Wait(0)
  end
  SetPlayerModel(PlayerId(), model)
  SetModelAsNoLongerNeeded(model)
end
```

---
### SetPlayerNoiseMultiplier

`SET_PLAYER_NOISE_MULTIPLIER` · hash `0xDB89EF50FF25FCE9` · jhash `0x15786DD1` · **Cliente**

```lua
SetPlayerNoiseMultiplier(player, multiplier)
```
```c
void SET_PLAYER_NOISE_MULTIPLIER(Player player, float multiplier);
```

**Parámetros**

- `player` (`Player`)
- `multiplier` (`float`)

**Devuelve:** `void`

---
### SetPlayerParachuteModelOverride

`SET_PLAYER_PARACHUTE_MODEL_OVERRIDE` · hash `0x977DB4641F6FC3DB` · jhash `0x5D382498` · **Cliente**

```lua
SetPlayerParachuteModelOverride(player, model)
```
```c
void SET_PLAYER_PARACHUTE_MODEL_OVERRIDE(Player player, Hash model);
```

**Parámetros**

- `player` (`Player`)
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
example:  
PLAYER::SET_PLAYER_PARACHUTE_MODEL_OVERRIDE(PLAYER::PLAYER_ID(), 0x73268708);  
```

---
### SetPlayerParachutePackModelOverride

`SET_PLAYER_PARACHUTE_PACK_MODEL_OVERRIDE` · hash `0xDC80A4C2F18A2B64` · jhash `0xA877FF5E` · **Cliente**

```lua
SetPlayerParachutePackModelOverride(player, model)
```
```c
void SET_PLAYER_PARACHUTE_PACK_MODEL_OVERRIDE(Player player, Hash model);
```

**Parámetros**

- `player` (`Player`)
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### SetPlayerParachutePackTintIndex

`SET_PLAYER_PARACHUTE_PACK_TINT_INDEX` · hash `0x93B0FB27C9A04060` · jhash `0xD79D5D1B` · **Cliente**

```lua
SetPlayerParachutePackTintIndex(player, tintIndex)
```
```c
void SET_PLAYER_PARACHUTE_PACK_TINT_INDEX(Player player, int tintIndex);
```

**Parámetros**

- `player` (`Player`)
- `tintIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
tints 0- 13
0 - unkown
1 - unkown
2 - unkown
3 - unkown
4 - unkown
```

---
### SetPlayerParachuteSmokeTrailColor

`SET_PLAYER_PARACHUTE_SMOKE_TRAIL_COLOR` · hash `0x8217FD371A4625CF` · jhash `0x14FE9264` · **Cliente**

```lua
SetPlayerParachuteSmokeTrailColor(player, r, g, b)
```
```c
void SET_PLAYER_PARACHUTE_SMOKE_TRAIL_COLOR(Player player, int r, int g, int b);
```

**Parámetros**

- `player` (`Player`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `void`

---
### SetPlayerParachuteTintIndex

`SET_PLAYER_PARACHUTE_TINT_INDEX` · hash `0xA3D0E54541D9A5E5` · jhash `0x8EA12EDB` · **Cliente**

```lua
SetPlayerParachuteTintIndex(player, tintIndex)
```
```c
void SET_PLAYER_PARACHUTE_TINT_INDEX(Player player, int tintIndex);
```

**Parámetros**

- `player` (`Player`)
- `tintIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Tints:  
None = -1,  
Rainbow = 0,  
Red = 1,  
SeasideStripes = 2,  
WidowMaker = 3,  
Patriot = 4,  
Blue = 5,  
Black = 6,  
Hornet = 7,  
AirFocce = 8,  
Desert = 9,  
Shadow = 10,  
HighAltitude = 11,  
Airbone = 12,  
Sunrise = 13,  
```

---
### SetPlayerParachuteVariationOverride

`SET_PLAYER_PARACHUTE_VARIATION_OVERRIDE` · hash `0xD9284A8C0D48352C` · jhash `0x9254249D` · **Cliente**

```lua
SetPlayerParachuteVariationOverride(player, p1, p2, p3, p4)
```
```c
void SET_PLAYER_PARACHUTE_VARIATION_OVERRIDE(Player player, int p1, Any p2, Any p3, BOOL p4);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`int`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 was always 5.  
p4 was always false.  
```

---
### SetPlayerReserveParachuteModelOverride

`_SET_PLAYER_RESERVE_PARACHUTE_MODEL_OVERRIDE` · hash `0x0764486AEDE748DB` · **Cliente**

```lua
SetPlayerReserveParachuteModelOverride(player, model)
```
```c
void _SET_PLAYER_RESERVE_PARACHUTE_MODEL_OVERRIDE(Player player, Hash model);
```

**Parámetros**

- `player` (`Player`)
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### SetPlayerReserveParachuteTintIndex

`SET_PLAYER_RESERVE_PARACHUTE_TINT_INDEX` · hash `0xAF04C87F5DC1DF38` · jhash `0x70689638` · **Cliente**

```lua
SetPlayerReserveParachuteTintIndex(player, index)
```
```c
void SET_PLAYER_RESERVE_PARACHUTE_TINT_INDEX(Player player, int index);
```

**Parámetros**

- `player` (`Player`)
- `index` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Tints:  
None = -1,  
Rainbow = 0,  
Red = 1,  
SeasideStripes = 2,  
WidowMaker = 3,  
Patriot = 4,  
Blue = 5,  
Black = 6,  
Hornet = 7,  
AirFocce = 8,  
Desert = 9,  
Shadow = 10,  
HighAltitude = 11,  
Airbone = 12,  
Sunrise = 13,  
```

---
### SetPlayerResetFlagPreferRearSeats

`SET_PLAYER_RESET_FLAG_PREFER_REAR_SEATS` · hash `0x11D5F725F0E780E0` · jhash `0x725C6174` · **Cliente**

```lua
SetPlayerResetFlagPreferRearSeats(player, flags)
```
```c
void SET_PLAYER_RESET_FLAG_PREFER_REAR_SEATS(Player player, int flags);
```

**Parámetros**

- `player` (`Player`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
example:  
flags: 0-6  
PLAYER::SET_PLAYER_RESET_FLAG_PREFER_REAR_SEATS(PLAYER::PLAYER_ID(), 6);  
wouldnt the flag be the seatIndex?  
```

---
### SetPlayerSimulateAiming

`SET_PLAYER_SIMULATE_AIMING` · hash `0xC54C95DA968EC5B5` · jhash `0xF1E0CAFC` · **Cliente**

```lua
SetPlayerSimulateAiming(player, toggle)
```
```c
void SET_PLAYER_SIMULATE_AIMING(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPlayerSneakingNoiseMultiplier

`SET_PLAYER_SNEAKING_NOISE_MULTIPLIER` · hash `0xB2C1A29588A9F47C` · jhash `0x8D2D89C4` · **Cliente**

```lua
SetPlayerSneakingNoiseMultiplier(player, multiplier)
```
```c
void SET_PLAYER_SNEAKING_NOISE_MULTIPLIER(Player player, float multiplier);
```

**Parámetros**

- `player` (`Player`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Values around 1.0f to 2.0f used in game scripts.  
```

---
### SetPlayerSprint

`SET_PLAYER_SPRINT` · hash `0xA01B8075D8B92DF4` · jhash `0x7DD7900C` · **Cliente**

```lua
SetPlayerSprint(player, toggle)
```
```c
void SET_PLAYER_SPRINT(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPlayerStealthPerceptionModifier

`SET_PLAYER_STEALTH_PERCEPTION_MODIFIER` · hash `0x4E9021C1FCDD507A` · jhash `0x3D26105F` · **Cliente**

```lua
SetPlayerStealthPerceptionModifier(player, value)
```
```c
void SET_PLAYER_STEALTH_PERCEPTION_MODIFIER(Player player, float value);
```

**Parámetros**

- `player` (`Player`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPlayerTargetLevel

`SET_PLAYER_TARGET_LEVEL` · hash `0x5702B917B99DB1CD` · jhash `0x772DA539` · **Cliente**

```lua
SetPlayerTargetLevel(targetLevel)
```
```c
void SET_PLAYER_TARGET_LEVEL(int targetLevel);
```

**Parámetros**

- `targetLevel` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5702B917B99DB1CD` (`N_0x5702b917b99db1cd`)

---
### SetPlayerTargetingMode

`SET_PLAYER_TARGETING_MODE` · hash `0xB1906895227793F3` · jhash `0x61CAE253` · **Cliente**

```lua
SetPlayerTargetingMode(targetMode)
```
```c
void SET_PLAYER_TARGETING_MODE(int targetMode);
```

**Parámetros**

- `targetMode` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets your targeting mode.
0 = Assisted Aim - Full
1 = Assisted Aim - Partial
2 = Free Aim - Assisted
3 = Free Aim
```

---
### SetPlayerTeam

`SET_PLAYER_TEAM` · hash `0x0299FA38396A4940` · jhash `0x725ADCF2` · **Cliente**

```lua
SetPlayerTeam(player, team)
```
```c
void SET_PLAYER_TEAM(Player player, int team);
```

**Parámetros**

- `player` (`Player`): The player index.
- `team` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Set the player's current team.

---
### SetPlayerUnderwaterTimeRemaining

`_SET_PLAYER_UNDERWATER_TIME_REMAINING` · hash `0xA0D3E4F7AAFB7E78` · **Cliente**

```lua
local retval = SetPlayerUnderwaterTimeRemaining(player, percentage)
```
```c
Any _SET_PLAYER_UNDERWATER_TIME_REMAINING(Player player, float percentage);
```

**Parámetros**

- `player` (`Player`): Player id.
- `percentage` (`float`): Maximum is `100.0`. Any value above `100.0` and less than `0.0` will have no effect on [GET_PLAYER_UNDERWATER_TIME_REMAINING](#getplayerunderwatertimeremaining).

**Devuelve:** `Any`

**Descripción oficial:**

Seems to lock the underwater timer of the specified player. Set `percentage` to `50.0` will reduce the value of [GET_PLAYER_UNDERWATER_TIME_REMAINING](#getplayerunderwatertimeremaining) to 5.0.

If you want to increase the underwater time for ped, use [SET_PED_MAX_TIME_UNDERWATER](PED-1.md#setpedmaxtimeunderwater) instead.

Using this native after [SET_PED_MAX_TIME_UNDERWATER](PED-1.md#setpedmaxtimeunderwater) **WILL NOT** get what you want. For example, if you set the max time underwater to `100.0` seconds using [SET_PED_MAX_TIME_UNDERWATER](PED-1.md#setpedmaxtimeunderwater) and then call this native and set the `percentage` to 50.0, you will not get `50.0`, instead `2.0`.

**Nombres antiguos (alias):** `0xA0D3E4F7AAFB7E78` (`N_0xa0d3e4f7aafb7e78`)

---
### SetPlayerVehicleDamageModifier

`SET_PLAYER_VEHICLE_DAMAGE_MODIFIER` · hash `0xA50E117CDDF82F0C` · jhash `0x823ECA63` · **Cliente**

```lua
SetPlayerVehicleDamageModifier(player, modifier)
```
```c
void SET_PLAYER_VEHICLE_DAMAGE_MODIFIER(Player player, float modifier);
```

**Parámetros**

- `player` (`Player`)
- `modifier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
modifier's min value is 0.1
```

---
### SetPlayerVehicleDefenseModifier

`SET_PLAYER_VEHICLE_DEFENSE_MODIFIER` · hash `0x4C60E6EFDAFF2462` · jhash `0xA16626C7` · **Cliente**

```lua
SetPlayerVehicleDefenseModifier(player, modifier)
```
```c
void SET_PLAYER_VEHICLE_DEFENSE_MODIFIER(Player player, float modifier);
```

**Parámetros**

- `player` (`Player`)
- `modifier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
modifier's min value is 0.1
```

---
### SetPlayerWantedCentrePosition

`SET_PLAYER_WANTED_CENTRE_POSITION` · hash `0x520E541A97A13354` · jhash `0xF261633A` · **Cliente**

```lua
local position = SetPlayerWantedCentrePosition(player, p2, p3)
```
```c
void SET_PLAYER_WANTED_CENTRE_POSITION(Player player, Vector3* position, BOOL p2, BOOL p3);
```

**Parámetros**

- `player` (`Player`)
- `position` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
**Predominant call signatures**
PLAYER::SET_PLAYER_WANTED_CENTRE_POSITION(PLAYER::PLAYER_ID(), ENTITY::GET_ENTITY_COORDS(PLAYER::PLAYER_PED_ID(), 1));  
**Parameter value ranges**
P0: PLAYER::PLAYER_ID()  
P1: ENTITY::GET_ENTITY_COORDS(PLAYER::PLAYER_PED_ID(), 1)  
P2: Not set by any call  
```

---
### SetPlayerWantedLevel

`SET_PLAYER_WANTED_LEVEL` · hash `0x39FF19C64EF7DA5B` · jhash `0xB7A0914B` · **Cliente · también en el servidor (RPC)**

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

**Ejemplo (lua):**

```lua
local player = PlayerId()
SetPlayerWantedLevel(player, 5, false) -- 5 star wanted level
```

---
### SetPlayerWantedLevelNoDrop

`SET_PLAYER_WANTED_LEVEL_NO_DROP` · hash `0x340E61DE7F471565` · jhash `0xED6F44F5` · **Cliente**

```lua
SetPlayerWantedLevelNoDrop(player, wantedLevel, delayedResponse)
```
```c
void SET_PLAYER_WANTED_LEVEL_NO_DROP(Player player, int wantedLevel, BOOL delayedResponse);
```

**Parámetros**

- `player` (`Player`): the target player
- `wantedLevel` (`int`): the wanted level 1-5
- `delayedResponse` (`BOOL`): false = 0-10sec police spawn response time, true = 10-20sec police spawn response time

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local player = PlayerId()
SetPlayerWantedLevelNoDrop(player, 5, false) -- 5 star wanted level
```

---
### SetPlayerWantedLevelNow

`SET_PLAYER_WANTED_LEVEL_NOW` · hash `0xE0A7D1E497FFCD6F` · jhash `0xAF3AFD83` · **Cliente**

```lua
SetPlayerWantedLevelNow(player, p1)
```
```c
void SET_PLAYER_WANTED_LEVEL_NOW(Player player, BOOL p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Forces any pending wanted level to be applied to the specified player immediately.  
Call SET_PLAYER_WANTED_LEVEL with the desired wanted level, followed by SET_PLAYER_WANTED_LEVEL_NOW.  
Second parameter is unknown (always false).  
```

---
### SetPlayerWeaponDamageModifier

`SET_PLAYER_WEAPON_DAMAGE_MODIFIER` · hash `0xCE07B9F7817AADA3` · jhash `0xB02C2F39` · **Cliente**

```lua
SetPlayerWeaponDamageModifier(player, modifier)
```
```c
void SET_PLAYER_WEAPON_DAMAGE_MODIFIER(Player player, float modifier);
```

**Parámetros**

- `player` (`Player`)
- `modifier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

The native ensures the 'modifier' parameter is 0.1 or greater.

---
### SetPlayerWeaponDefenseModifier

`SET_PLAYER_WEAPON_DEFENSE_MODIFIER` · hash `0x2D83BC011CA14A3C` · jhash `0xAE446344` · **Cliente**

```lua
SetPlayerWeaponDefenseModifier(player, modifier)
```
```c
void SET_PLAYER_WEAPON_DEFENSE_MODIFIER(Player player, float modifier);
```

**Parámetros**

- `player` (`Player`)
- `modifier` (`float`)

**Devuelve:** `void`

---
### SetPlayerWeaponDefenseModifier_2

`_SET_PLAYER_WEAPON_DEFENSE_MODIFIER_2` · hash `0xBCFDE9EDE4CF27DC` · **Cliente**

```lua
SetPlayerWeaponDefenseModifier_2(player, modifier)
```
```c
void _SET_PLAYER_WEAPON_DEFENSE_MODIFIER_2(Player player, float modifier);
```

**Parámetros**

- `player` (`Player`)
- `modifier` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBCFDE9EDE4CF27DC` (`N_0xbcfde9ede4cf27dc`)

---
### SetPoliceIgnorePlayer

`SET_POLICE_IGNORE_PLAYER` · hash `0x32C62AA929C2DA6A` · jhash `0xE6DE71B7` · **Cliente**

```lua
SetPoliceIgnorePlayer(player, toggle)
```
```c
void SET_POLICE_IGNORE_PLAYER(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
The player will be ignored by the police if toggle is set to true  
```

---
### SetPoliceRadarBlips

`SET_POLICE_RADAR_BLIPS` · hash `0x43286D561B72B8BF` · jhash `0x8E114B10` · **Cliente**

```lua
SetPoliceRadarBlips(toggle)
```
```c
void SET_POLICE_RADAR_BLIPS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If toggle is set to false:
 The police won't be shown on the (mini)map
If toggle is set to true:
 The police will be shown on the (mini)map
```

---
### SetRunSprintMultiplierForPlayer

`SET_RUN_SPRINT_MULTIPLIER_FOR_PLAYER` · hash `0x6DB47AA77FD94E09` · jhash `0x825423C2` · **Cliente**

```lua
SetRunSprintMultiplierForPlayer(player, multiplier)
```
```c
void SET_RUN_SPRINT_MULTIPLIER_FOR_PLAYER(Player player, float multiplier);
```

**Parámetros**

- `player` (`Player`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Multiplier goes up to 1.49 any value above will be completely overruled by the game and the multiplier will not take effect, this can be edited in memory however.  
Just call it one time, it is not required to be called once every tick.  
Note: At least the IDA method if you change the max float multiplier from 1.5 it will change it for both this and SWIM above. I say 1.5 as the function blrs if what you input is greater than or equal to 1.5 hence why it's 1.49 max default.  
It is not possible to "decrease" speed. Anything below 1 will be ignored.  
```

---
### SetSpecialAbility

`_SET_SPECIAL_ABILITY` · hash `0xB214D570EAD7F81A` · **Cliente**

```lua
SetSpecialAbility(player, p1)
```
```c
void _SET_SPECIAL_ABILITY(Player player, int p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 3: Any p2
```

**Nombres antiguos (alias):** `0xB214D570EAD7F81A` (`N_0xb214d570ead7f81a`)

---
### SetSpecialAbilityMultiplier

`SET_SPECIAL_ABILITY_MULTIPLIER` · hash `0xA49C426ED0CA4AB7` · jhash `0xFF1BC556` · **Cliente**

```lua
SetSpecialAbilityMultiplier(multiplier)
```
```c
void SET_SPECIAL_ABILITY_MULTIPLIER(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

---
### SetSwimMultiplierForPlayer

`SET_SWIM_MULTIPLIER_FOR_PLAYER` · hash `0xA91C6F0FF7D16A13` · jhash `0xB986FF47` · **Cliente**

```lua
SetSwimMultiplierForPlayer(player, multiplier)
```
```c
void SET_SWIM_MULTIPLIER_FOR_PLAYER(Player player, float multiplier);
```

**Parámetros**

- `player` (`Player`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Swim speed multiplier.  
Multiplier goes up to 1.49  
Just call it one time, it is not required to be called once every tick. - Note copied from below native.  
Note: At least the IDA method if you change the max float multiplier from 1.5 it will change it for both this and RUN_SPRINT below. I say 1.5 as the function blrs if what you input is greater than or equal to 1.5 hence why it's 1.49 max default.  
```

---
### SetWantedLevelDifficulty

`SET_WANTED_LEVEL_DIFFICULTY` · hash `0x9B0BB33B04405E7A` · jhash `0xB552626C` · **Cliente**

```lua
SetWantedLevelDifficulty(player, difficulty)
```
```c
void SET_WANTED_LEVEL_DIFFICULTY(Player player, float difficulty);
```

**Parámetros**

- `player` (`Player`)
- `difficulty` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Max value is 1.0  
```

---
### SetWantedLevelHiddenEvasionTime

`_SET_WANTED_LEVEL_HIDDEN_EVASION_TIME` · hash `0x49B856B1360C47C7` · **Cliente**

```lua
SetWantedLevelHiddenEvasionTime(player, wantedLevel, lossTime)
```
```c
void _SET_WANTED_LEVEL_HIDDEN_EVASION_TIME(Player player, int wantedLevel, int lossTime);
```

**Parámetros**

- `player` (`Player`)
- `wantedLevel` (`int`)
- `lossTime` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

**Nombres antiguos (alias):** `0x49B856B1360C47C7` (`N_0x49b856b1360c47c7`)

---
### SetWantedLevelMultiplier

`SET_WANTED_LEVEL_MULTIPLIER` · hash `0x020E5F00CDA207BA` · jhash `0x1359292F` · **Cliente**

```lua
SetWantedLevelMultiplier(multiplier)
```
```c
void SET_WANTED_LEVEL_MULTIPLIER(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

---
### SimulatePlayerInputGait

`SIMULATE_PLAYER_INPUT_GAIT` · hash `0x477D5D63E63ECA5D` · jhash `0x0D77CC34` · **Cliente**

```lua
SimulatePlayerInputGait(player, amount, gaitType, rotationSpeed, p4, p5)
```
```c
void SIMULATE_PLAYER_INPUT_GAIT(Player player, float amount, int gaitType, float rotationSpeed, BOOL p4, BOOL p5);
```

**Parámetros**

- `player` (`Player`): The player to target (always your local player id).
- `amount` (`float`): For game pads, using anything less than 1.0 will make it partially press analog controls (like sticks/triggers).
- `gaitType` (`int`): Value in increments of 100's. 2000, 500, 300, 200, etc. Set to -1 if you want your ped to walk forever.
- `rotationSpeed` (`float`): Determines the counterclockwise rotation angle when walking.
- `p4` (`BOOL`): Always true
- `p5` (`BOOL`): Always false

**Devuelve:** `void`

**Descripción oficial:**

This is to make the player walk without accepting input.

Call this native every frame so you can control the direction of your ped.

**Ejemplo (cs):**

```cs
SimulatePlayerInputGait(Game.Player.Handle, 1f, 100, 1f, 1, 0); //Player will go forward for 100ms
SimulatePlayerInputGait(Game.Player.Handle, 1f, -1, 0f, 1, 0); //Player will go straight forward forever, stop when facing walls or obstacles.
```

---
### SpecialAbilityActivate

`_SPECIAL_ABILITY_ACTIVATE` · hash `0x821FDC827D6F4090` · **Cliente**

```lua
SpecialAbilityActivate(player)
```
```c
void _SPECIAL_ABILITY_ACTIVATE(Any player);
```

**Parámetros**

- `player` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0x821FDC827D6F4090` (`N_0x821fdc827d6f4090`)

---
### SpecialAbilityChargeAbsolute

`SPECIAL_ABILITY_CHARGE_ABSOLUTE` · hash `0xB7B0870EB531D08D` · jhash `0x72429998` · **Cliente**

```lua
SpecialAbilityChargeAbsolute(player, p1, p2)
```
```c
void SPECIAL_ABILITY_CHARGE_ABSOLUTE(Player player, int p1, BOOL p2);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 appears as 5, 10, 15, 25, or 30. p2 is always true.
```

```
NativeDB Added Parameter 4: Any p3
```

---
### SpecialAbilityChargeContinuous

`SPECIAL_ABILITY_CHARGE_CONTINUOUS` · hash `0xED481732DFF7E997` · jhash `0x5FEE98A2` · **Cliente**

```lua
SpecialAbilityChargeContinuous(player, p2)
```
```c
void SPECIAL_ABILITY_CHARGE_CONTINUOUS(Player player, Ped p2);
```

**Parámetros**

- `player` (`Player`)
- `p2` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 appears to always be 1 (only comes up twice)
```

```
NativeDB Added Parameter 3: Any p2
```

---
### SpecialAbilityChargeLarge

`SPECIAL_ABILITY_CHARGE_LARGE` · hash `0xF733F45FA4497D93` · jhash `0xF440C04D` · **Cliente**

```lua
SpecialAbilityChargeLarge(player, p1, p2)
```
```c
void SPECIAL_ABILITY_CHARGE_LARGE(Player player, BOOL p1, BOOL p2);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
2 matches. p1 was always true.
```

```
NativeDB Added Parameter 4: Any p3
```

---
### SpecialAbilityChargeMedium

`SPECIAL_ABILITY_CHARGE_MEDIUM` · hash `0xF113E3AA9BC54613` · jhash `0xAB55D8F3` · **Cliente**

```lua
SpecialAbilityChargeMedium(player, p1, p2)
```
```c
void SPECIAL_ABILITY_CHARGE_MEDIUM(Player player, BOOL p1, BOOL p2);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only 1 match. Both p1 & p2 were true.
```

```
NativeDB Added Parameter 4: Any p3
```

---
### SpecialAbilityChargeNormalized

`SPECIAL_ABILITY_CHARGE_NORMALIZED` · hash `0xA0696A65F009EE18` · jhash `0x8C7E68C1` · **Cliente**

```lua
SpecialAbilityChargeNormalized(player, normalizedValue, p2)
```
```c
void SPECIAL_ABILITY_CHARGE_NORMALIZED(Player player, float normalizedValue, BOOL p2);
```

**Parámetros**

- `player` (`Player`)
- `normalizedValue` (`float`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
normalizedValue is from 0.0 - 1.0
p2 is always 1
```

```
NativeDB Added Parameter 4: Any p3
```

**Nombres antiguos (alias):** `RESET_SPECIAL_ABILITY_CONTROLS_CINEMATIC` (`ResetSpecialAbilityControlsCinematic`)

---
### SpecialAbilityChargeOnMissionFailed

`SPECIAL_ABILITY_CHARGE_ON_MISSION_FAILED` · hash `0xC9A763D8FE87436A` · jhash `0x4136829A` · **Cliente**

```lua
SpecialAbilityChargeOnMissionFailed(player)
```
```c
void SPECIAL_ABILITY_CHARGE_ON_MISSION_FAILED(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0xC9A763D8FE87436A` (`N_0xc9a763d8fe87436a`)

---
### SpecialAbilityChargeSmall

`SPECIAL_ABILITY_CHARGE_SMALL` · hash `0x2E7B9B683481687D` · jhash `0x6F463F56` · **Cliente**

```lua
SpecialAbilityChargeSmall(player, p1, p2)
```
```c
void SPECIAL_ABILITY_CHARGE_SMALL(Player player, BOOL p1, BOOL p2);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Every occurrence of p1 & p2 were both true.
```

```
NativeDB Added Parameter 4: Any p3
```

---
### SpecialAbilityDeactivate

`SPECIAL_ABILITY_DEACTIVATE` · hash `0xD6A953C6D1492057` · jhash `0x80C2AB09` · **Cliente**

```lua
SpecialAbilityDeactivate(player)
```
```c
void SPECIAL_ABILITY_DEACTIVATE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### SpecialAbilityDeactivateFast

`SPECIAL_ABILITY_DEACTIVATE_FAST` · hash `0x9CB5CE07A3968D5A` · jhash `0x0751908A` · **Cliente**

```lua
SpecialAbilityDeactivateFast(player)
```
```c
void SPECIAL_ABILITY_DEACTIVATE_FAST(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### SpecialAbilityDeplete

`_SPECIAL_ABILITY_DEPLETE` · hash `0x17F7471EACA78290` · **Cliente**

```lua
SpecialAbilityDeplete(p0)
```
```c
void _SPECIAL_ABILITY_DEPLETE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0x17F7471EACA78290` (`N_0x17f7471eaca78290`)

---
### SpecialAbilityDepleteMeter

`SPECIAL_ABILITY_DEPLETE_METER` · hash `0x1D506DBBBC51E64B` · jhash `0x9F80F6DF` · **Cliente**

```lua
SpecialAbilityDepleteMeter(player, p1)
```
```c
void SPECIAL_ABILITY_DEPLETE_METER(Player player, BOOL p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 was always true.
```

```
NativeDB Added Parameter 3: Any p2
```

---
### SpecialAbilityFillMeter

`SPECIAL_ABILITY_FILL_METER` · hash `0x3DACA8DDC6FD4980` · jhash `0xB71589DA` · **Cliente**

```lua
SpecialAbilityFillMeter(player, p1)
```
```c
void SPECIAL_ABILITY_FILL_METER(Player player, BOOL p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Also known as _RECHARGE_SPECIAL_ABILITY
```

```
NativeDB Added Parameter 3: Any p2
```

---
### SpecialAbilityLock

`SPECIAL_ABILITY_LOCK` · hash `0x6A09D0D590A47D13` · jhash `0x1B7BB388` · **Cliente**

```lua
SpecialAbilityLock(playerModel)
```
```c
void SPECIAL_ABILITY_LOCK(Hash playerModel);
```

**Parámetros**

- `playerModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### SpecialAbilityReset

`SPECIAL_ABILITY_RESET` · hash `0x375F0E738F861A94` · jhash `0xA7D8BCD3` · **Cliente**

```lua
SpecialAbilityReset(player)
```
```c
void SPECIAL_ABILITY_RESET(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### SpecialAbilityUnlock

`SPECIAL_ABILITY_UNLOCK` · hash `0xF145F3BE2EFA9A3B` · jhash `0x1FDB2919` · **Cliente**

```lua
SpecialAbilityUnlock(playerModel)
```
```c
void SPECIAL_ABILITY_UNLOCK(Hash playerModel);
```

**Parámetros**

- `playerModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

---
### StartFiringAmnesty

`START_FIRING_AMNESTY` · hash `0xBF9BD71691857E48` · jhash `0x5F8A22A6` · **Cliente**

```lua
StartFiringAmnesty(duration)
```
```c
void START_FIRING_AMNESTY(int duration);
```

**Parámetros**

- `duration` (`int`)

**Devuelve:** `void`

---
### StartPlayerTeleport

`START_PLAYER_TELEPORT` · hash `0xAD15F075A4DA0FDE` · jhash `0xC552E06C` · **Cliente**

```lua
StartPlayerTeleport(player, x, y, z, heading, teleportWithVehicle, findCollisionLand, p7)
```
```c
void START_PLAYER_TELEPORT(Player player, float x, float y, float z, float heading, BOOL teleportWithVehicle, BOOL findCollisionLand, BOOL p7);
```

**Parámetros**

- `player` (`Player`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `teleportWithVehicle` (`BOOL`): Teleports the player along with the vehicle they are in.
- `findCollisionLand` (`BOOL`): Attempt to find a ground coordinate at the given XY location; overriding the Z value.
- `p7` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Teleports the player to the given coordinates.

If findCollisionLand is true it will try to find the Z value for you, this however has a timeout of 100 frames.

When trying to find the Z value the native will take longer the higher the difference from the given Z to the ground, this combined with the timeout can cause the teleport to just teleport to the given Z value, so try to estimate the z value, so don't just pass in 1000.0.

Also if you're in a vehicle and teleportWithVehicle is true it will not find the Z value for you.

**Ejemplo (lua):**

```lua
local coords = vector3(100.0, 100.0, 50.0)
StartPlayerTeleport(PlayerId(), coords.x, coords.y, coords.z, 0.0, false, true, true)

while IsPlayerTeleportActive() do
  Citizen.Wait(0)
end

--- If you would want to make 100% sure the ped is on the ground here you would have to do some additional checks here
--- Easiest would be a simple: GetEntityHeightAboveGround(PlayerPedId())
```

---
### StopPlayerTeleport

`STOP_PLAYER_TELEPORT` · hash `0xC449EDED9D73009C` · jhash `0x86AB8DBB` · **Cliente**

```lua
StopPlayerTeleport()
```
```c
void STOP_PLAYER_TELEPORT();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Disables the player's teleportation  
```

---
### SuppressCrimeThisFrame

`SUPPRESS_CRIME_THIS_FRAME` · hash `0x9A987297ED8BD838` · jhash `0x59B5C2A2` · **Cliente**

```lua
SuppressCrimeThisFrame(player, crimeType)
```
```c
void SUPPRESS_CRIME_THIS_FRAME(Player player, int crimeType);
```

**Parámetros**

- `player` (`Player`): The player we are suppressing the crime for.
- `crimeType` (`int`): The crime to suppress, see [`REPORT_CRIME`](#reportcrime) for available types.

**Devuelve:** `void`

**Descripción oficial:**

Suppresses a crime for a given player for this frame only.

**Note:** This native needs to be executed inside a thread if a crime is meant to be suppressed for a given amount of time.

**Nombres antiguos (alias):** `0x9A987297ED8BD838` (`N_0x9a987297ed8bd838`), `_SWITCH_CRIME_TYPE` (`SwitchCrimeType`)

---
### UpdatePlayerTeleport

`_UPDATE_PLAYER_TELEPORT` · hash `0xE23D5873C2394C61` · **Cliente**

```lua
local retval = UpdatePlayerTeleport(player)
```
```c
BOOL _UPDATE_PLAYER_TELEPORT(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE23D5873C2394C61` (`N_0xe23d5873c2394c61`), `_HAS_PLAYER_TELEPORT_FINISHED` (`HasPlayerTeleportFinished`)

---
