# Natives de GTA V — TASK

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `TASK`: **306** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddCoverBlockingArea`](#addcoverblockingarea) · [`AddCoverPoint`](#addcoverpoint) · [`AddPatrolRouteLink`](#addpatrolroutelink) · [`AddPatrolRouteNode`](#addpatrolroutenode) · [`AddVehicleSubtaskAttackCoord`](#addvehiclesubtaskattackcoord) · [`AddVehicleSubtaskAttackPed`](#addvehiclesubtaskattackped) · [`AssistedMovementIsRouteLoaded`](#assistedmovementisrouteloaded) · [`AssistedMovementOverrideLoadDistanceThisFrame`](#assistedmovementoverrideloaddistancethisframe) · [`AssistedMovementRemoveRoute`](#assistedmovementremoveroute) · [`AssistedMovementRequestRoute`](#assistedmovementrequestroute) · [`AssistedMovementSetRouteProperties`](#assistedmovementsetrouteproperties) · [`ClearDrivebyTaskUnderneathDrivingTask`](#cleardrivebytaskunderneathdrivingtask) · [`ClearPedScriptTaskIfRunningThreatResponseNonTempTask`](#clearpedscripttaskifrunningthreatresponsenontemptask) · [`ClearPedSecondaryTask`](#clearpedsecondarytask) · [`ClearPedTasks`](#clearpedtasks) · [`ClearPedTasksImmediately`](#clearpedtasksimmediately) · [`ClearSequenceTask`](#clearsequencetask) · [`ClearVehicleTasks`](#clearvehicletasks) · [`ClosePatrolRoute`](#closepatrolroute) · [`CloseSequenceTask`](#closesequencetask) · [`ControlMountedWeapon`](#controlmountedweapon) · [`CreatePatrolRoute`](#createpatrolroute) · [`DeletePatrolRoute`](#deletepatrolroute) · [`DoesScenarioExistInArea`](#doesscenarioexistinarea) · [`DoesScenarioGroupExist`](#doesscenariogroupexist) · [`DoesScenarioOfTypeExistInArea`](#doesscenariooftypeexistinarea) · [`DoesScriptedCoverPointExistAtCoords`](#doesscriptedcoverpointexistatcoords) · [`GetActiveVehicleMissionType`](#getactivevehiclemissiontype) · [`GetClipSetForScriptedGunTask`](#getclipsetforscriptedguntask) · [`GetIsTaskActive`](#getistaskactive) · [`GetIsWaypointRecordingLoaded`](#getiswaypointrecordingloaded) · [`GetNavmeshRouteDistanceRemaining`](#getnavmeshroutedistanceremaining) · [`GetNavmeshRouteResult`](#getnavmeshrouteresult) · [`GetPedDesiredMoveBlendRatio`](#getpeddesiredmoveblendratio) · [`GetPedWaypointDistance`](#getpedwaypointdistance) · [`GetPedWaypointProgress`](#getpedwaypointprogress) · [`GetPhoneGestureAnimCurrentTime`](#getphonegestureanimcurrenttime) · [`GetPhoneGestureAnimTotalTime`](#getphonegestureanimtotaltime) · [`GetScriptTaskStatus`](#getscripttaskstatus) · [`GetScriptedCoverPointCoords`](#getscriptedcoverpointcoords) · [`GetSequenceProgress`](#getsequenceprogress) · [`GetTaskMoveNetworkEvent`](#gettaskmovenetworkevent) · [`GetTaskMoveNetworkSignalBool`](#gettaskmovenetworksignalbool) · [`GetTaskMoveNetworkSignalFloat`](#gettaskmovenetworksignalfloat) · [`GetTaskMoveNetworkState`](#gettaskmovenetworkstate) · [`GetVehicleWaypointProgress`](#getvehiclewaypointprogress) · [`GetVehicleWaypointTargetPoint`](#getvehiclewaypointtargetpoint) · [`GetWaypointDistanceAlongRoute`](#getwaypointdistancealongroute) · [`IsDrivebyTaskUnderneathDrivingTask`](#isdrivebytaskunderneathdrivingtask) · [`IsMountedWeaponTaskUnderneathDrivingTask`](#ismountedweapontaskunderneathdrivingtask) · [`IsMoveBlendRatioRunning`](#ismoveblendratiorunning) · [`IsMoveBlendRatioSprinting`](#ismoveblendratiosprinting) · [`IsMoveBlendRatioStill`](#ismoveblendratiostill) · [`IsMoveBlendRatioWalking`](#ismoveblendratiowalking) · [`IsPedActiveInScenario`](#ispedactiveinscenario) · [`IsPedBeingArrested`](#ispedbeingarrested) · [`IsPedCuffed`](#ispedcuffed) · [`IsPedGettingUp`](#ispedgettingup) · [`IsPedInWrithe`](#ispedinwrithe) · [`IsPedPlayingBaseClipInScenario`](#ispedplayingbaseclipinscenario) · [`IsPedRunning`](#ispedrunning) · [`IsPedRunningArrestTask`](#ispedrunningarresttask) · [`IsPedSprinting`](#ispedsprinting) · [`IsPedStill`](#ispedstill) · [`IsPedStrafing`](#ispedstrafing) · [`IsPedWalking`](#ispedwalking) · [`IsPlayingPhoneGestureAnim`](#isplayingphonegestureanim) · [`IsScenarioGroupEnabled`](#isscenariogroupenabled) · [`IsScenarioOccupied`](#isscenariooccupied) · [`IsScenarioTypeEnabled`](#isscenariotypeenabled) · [`IsTaskMoveNetworkActive`](#istaskmovenetworkactive) · [`IsTaskMoveNetworkReadyForTransition`](#istaskmovenetworkreadyfortransition) · [`IsWaypointPlaybackGoingOnForPed`](#iswaypointplaybackgoingonforped) · [`IsWaypointPlaybackGoingOnForVehicle`](#iswaypointplaybackgoingonforvehicle) · [`N_0x0ffb3c758e8c07b9`](#n_0x0ffb3c758e8c07b9) · [`N_0x1f351cf1c6475734`](#n_0x1f351cf1c6475734) · [`N_0x29682e2ccf21e9b5`](#n_0x29682e2ccf21e9b5) · [`N_0x3e38e28a1d80ddf6`](#n_0x3e38e28a1d80ddf6) · [`N_0x53ddc75bc3ac0a90`](#n_0x53ddc75bc3ac0a90) · [`N_0x6100b3cefd43452e`](#n_0x6100b3cefd43452e) · [`N_0x8423541e8b3a1589`](#n_0x8423541e8b3a1589) · [`N_0x8634cef2522d987b`](#n_0x8634cef2522d987b) · [`N_0x9d252648778160df`](#n_0x9d252648778160df) · [`N_0xab13a5565480b6d9`](#n_0xab13a5565480b6d9) · [`N_0xfa83ca6776038f64`](#n_0xfa83ca6776038f64) · [`OpenPatrolRoute`](#openpatrolroute) · [`OpenSequenceTask`](#opensequencetask) · [`PedHasUseScenarioTask`](#pedhasusescenariotask) · [`PlayAnimOnRunningScenario`](#playanimonrunningscenario) · [`PlayEntityScriptedAnim`](#playentityscriptedanim) · [`RemoveAllCoverBlockingAreas`](#removeallcoverblockingareas) · [`RemoveCoverPoint`](#removecoverpoint) · [`RemoveWaypointRecording`](#removewaypointrecording) · [`RequestTaskMoveNetworkStateTransition`](#requesttaskmovenetworkstatetransition) · [`RequestWaypointRecording`](#requestwaypointrecording) · [`ResetExclusiveScenarioGroup`](#resetexclusivescenariogroup) · [`ResetScenarioGroupsEnabled`](#resetscenariogroupsenabled) · [`ResetScenarioTypesEnabled`](#resetscenariotypesenabled) · [`SetAnimLooped`](#setanimlooped) · [`SetAnimPhase`](#setanimphase) · [`SetAnimRate`](#setanimrate) · [`SetAnimWeight`](#setanimweight) · [`SetDriveTaskCruiseSpeed`](#setdrivetaskcruisespeed) · [`SetDriveTaskDrivingStyle`](#setdrivetaskdrivingstyle) · [`SetDriveTaskMaxCruiseSpeed`](#setdrivetaskmaxcruisespeed) · [`SetDrivebyTaskTarget`](#setdrivebytasktarget) · [`SetExclusiveScenarioGroup`](#setexclusivescenariogroup) · [`SetGlobalMinBirdFlightHeight`](#setglobalminbirdflightheight) · [`SetHighFallTask`](#sethighfalltask) · [`SetMountedWeaponTarget`](#setmountedweapontarget) · [`SetNextDesiredMoveState`](#setnextdesiredmovestate) · [`SetParachuteTaskTarget`](#setparachutetasktarget) · [`SetParachuteTaskThrust`](#setparachutetaskthrust) · [`SetPedCanPlayAmbientIdles`](#setpedcanplayambientidles) · [`SetPedDesiredMoveBlendRatio`](#setpeddesiredmoveblendratio) · [`SetPedPathAvoidFire`](#setpedpathavoidfire) · [`SetPedPathCanDropFromHeight`](#setpedpathcandropfromheight) · [`SetPedPathCanUseClimbovers`](#setpedpathcanuseclimbovers) · [`SetPedPathCanUseLadders`](#setpedpathcanuseladders) · [`SetPedPathClimbCostModifier`](#setpedpathclimbcostmodifier) · [`SetPedPathMayEnterWater`](#setpedpathmayenterwater) · [`SetPedPathPreferToAvoidWater`](#setpedpathprefertoavoidwater) · [`SetPedWaypointRouteOffset`](#setpedwaypointrouteoffset) · [`SetScenarioGroupEnabled`](#setscenariogroupenabled) · [`SetScenarioTypeEnabled`](#setscenariotypeenabled) · [`SetSequenceToRepeat`](#setsequencetorepeat) · [`SetTaskMoveNetworkSignalBool`](#settaskmovenetworksignalbool) · [`SetTaskMoveNetworkSignalFloat`](#settaskmovenetworksignalfloat) · [`SetTaskMoveNetworkSignalFloat_2`](#settaskmovenetworksignalfloat_2) · [`SetTaskVehicleChaseBehaviorFlag`](#settaskvehiclechasebehaviorflag) · [`SetTaskVehicleChaseIdealPursuitDistance`](#settaskvehiclechaseidealpursuitdistance) · [`StopAnimPlayback`](#stopanimplayback) · [`StopAnimTask`](#stopanimtask) · [`TaskAchieveHeading`](#taskachieveheading) · [`TaskAgitatedAction`](#taskagitatedaction) · [`TaskAimGunAtCoord`](#taskaimgunatcoord) · [`TaskAimGunAtEntity`](#taskaimgunatentity) · [`TaskAimGunScripted`](#taskaimgunscripted) · [`TaskAimGunScriptedWithTarget`](#taskaimgunscriptedwithtarget) · [`TaskArrestPed`](#taskarrestped) · [`TaskBoatMission`](#taskboatmission) · [`TaskChatToPed`](#taskchattoped) · [`TaskClearDefensiveArea`](#taskcleardefensivearea) · [`TaskClearLookAt`](#taskclearlookat) · [`TaskClimb`](#taskclimb) · [`TaskClimbLadder`](#taskclimbladder) · [`TaskCombatHatedTargetsAroundPed`](#taskcombathatedtargetsaroundped) · [`TaskCombatHatedTargetsAroundPedTimed`](#taskcombathatedtargetsaroundpedtimed) · [`TaskCombatHatedTargetsInArea`](#taskcombathatedtargetsinarea) · [`TaskCombatPed`](#taskcombatped) · [`TaskCombatPedTimed`](#taskcombatpedtimed) · [`TaskCower`](#taskcower) · [`TaskDriveBy`](#taskdriveby) · [`TaskEnterVehicle`](#taskentervehicle) · [`TaskEveryoneLeaveVehicle`](#taskeveryoneleavevehicle) · [`TaskExitCover`](#taskexitcover) · [`TaskExtendRoute`](#taskextendroute) · [`TaskFlushRoute`](#taskflushroute) · [`TaskFollowNavMeshToCoord`](#taskfollownavmeshtocoord) · [`TaskFollowNavMeshToCoordAdvanced`](#taskfollownavmeshtocoordadvanced) · [`TaskFollowPointRoute`](#taskfollowpointroute) · [`TaskFollowToOffsetOfEntity`](#taskfollowtooffsetofentity) · [`TaskFollowWaypointRecording`](#taskfollowwaypointrecording) · [`TaskForceMotionState`](#taskforcemotionstate) · [`TaskGetOffBoat`](#taskgetoffboat) · [`TaskGoStraightToCoord`](#taskgostraighttocoord) · [`TaskGoStraightToCoordRelativeToEntity`](#taskgostraighttocoordrelativetoentity) · [`TaskGoToCoordAndAimAtHatedEntitiesNearCoord`](#taskgotocoordandaimathatedentitiesnearcoord) · [`TaskGoToCoordAnyMeans`](#taskgotocoordanymeans) · [`TaskGoToCoordAnyMeansExtraParams`](#taskgotocoordanymeansextraparams) · [`TaskGoToCoordAnyMeansExtraParamsWithCruiseSpeed`](#taskgotocoordanymeansextraparamswithcruisespeed) · [`TaskGoToCoordWhileAimingAtCoord`](#taskgotocoordwhileaimingatcoord) · [`TaskGoToCoordWhileAimingAtEntity`](#taskgotocoordwhileaimingatentity) · [`TaskGoToEntity`](#taskgotoentity) · [`TaskGoToEntityWhileAimingAtCoord`](#taskgotoentitywhileaimingatcoord) · [`TaskGoToEntityWhileAimingAtEntity`](#taskgotoentitywhileaimingatentity) · [`TaskGotoEntityAiming`](#taskgotoentityaiming) · [`TaskGotoEntityOffset`](#taskgotoentityoffset) · [`TaskGotoEntityOffsetXy`](#taskgotoentityoffsetxy) · [`TaskGuardAssignedDefensiveArea`](#taskguardassigneddefensivearea) · [`TaskGuardCurrentPosition`](#taskguardcurrentposition) · [`TaskGuardSphereDefensiveArea`](#taskguardspheredefensivearea) · [`TaskHandsUp`](#taskhandsup) · [`TaskHeliChase`](#taskhelichase) · [`TaskHeliEscortHeli`](#taskheliescortheli) · [`TaskHeliMission`](#taskhelimission) · [`TaskJump`](#taskjump) · [`TaskLeaveAnyVehicle`](#taskleaveanyvehicle) · [`TaskLeaveVehicle`](#taskleavevehicle) · [`TaskLookAtCoord`](#tasklookatcoord) · [`TaskLookAtEntity`](#tasklookatentity) · [`TaskMoveNetworkAdvancedByName`](#taskmovenetworkadvancedbyname) · [`TaskMoveNetworkByName`](#taskmovenetworkbyname) · [`TaskMoveNetworkByNameWithInitParams`](#taskmovenetworkbynamewithinitparams) · [`TaskOpenVehicleDoor`](#taskopenvehicledoor) · [`TaskParachute`](#taskparachute) · [`TaskParachuteToTarget`](#taskparachutetotarget) · [`TaskPatrol`](#taskpatrol) · [`TaskPause`](#taskpause) · [`TaskPedSlideToCoord`](#taskpedslidetocoord) · [`TaskPedSlideToCoordHdgRate`](#taskpedslidetocoordhdgrate) · [`TaskPerformSequence`](#taskperformsequence) · [`TaskPerformSequenceFromProgress`](#taskperformsequencefromprogress) · [`TaskPerformSequenceLocally`](#taskperformsequencelocally) · [`TaskPlaneChase`](#taskplanechase) · [`TaskPlaneGotoPreciseVtol`](#taskplanegotoprecisevtol) · [`TaskPlaneLand`](#taskplaneland) · [`TaskPlaneMission`](#taskplanemission) · [`TaskPlaneTaxi`](#taskplanetaxi) · [`TaskPlantBomb`](#taskplantbomb) · [`TaskPlayAnim`](#taskplayanim) · [`TaskPlayAnimAdvanced`](#taskplayanimadvanced) · [`TaskPlayPhoneGestureAnimation`](#taskplayphonegestureanimation) · [`TaskPutPedDirectlyIntoCover`](#taskputpeddirectlyintocover) · [`TaskPutPedDirectlyIntoMelee`](#taskputpeddirectlyintomelee) · [`TaskRappelDownWall`](#taskrappeldownwall) · [`TaskRappelFromHeli`](#taskrappelfromheli) · [`TaskReactAndFleePed`](#taskreactandfleeped) · [`TaskReloadWeapon`](#taskreloadweapon) · [`TaskScriptedAnimation`](#taskscriptedanimation) · [`TaskSeekCoverFromPed`](#taskseekcoverfromped) · [`TaskSeekCoverFromPos`](#taskseekcoverfrompos) · [`TaskSeekCoverToCoords`](#taskseekcovertocoords) · [`TaskSeekCoverToCoverPoint`](#taskseekcovertocoverpoint) · [`TaskSetBlockingOfNonTemporaryEvents`](#tasksetblockingofnontemporaryevents) · [`TaskSetDecisionMaker`](#tasksetdecisionmaker) · [`TaskSetSphereDefensiveArea`](#tasksetspheredefensivearea) · [`TaskSharkCircleCoord`](#tasksharkcirclecoord) · [`TaskShockingEventReact`](#taskshockingeventreact) · [`TaskShootAtCoord`](#taskshootatcoord) · [`TaskShootAtEntity`](#taskshootatentity) · [`TaskShuffleToNextVehicleSeat`](#taskshuffletonextvehicleseat) · [`TaskSkyDive`](#taskskydive) · [`TaskSmartFleeCoord`](#tasksmartfleecoord) · [`TaskSmartFleePed`](#tasksmartfleeped) · [`TaskStandGuard`](#taskstandguard) · [`TaskStandStill`](#taskstandstill) · [`TaskStartScenarioAtPosition`](#taskstartscenarioatposition) · [`TaskStartScenarioInPlace`](#taskstartscenarioinplace) · [`TaskStayInCover`](#taskstayincover) · [`TaskStealthKill`](#taskstealthkill) · [`TaskStopPhoneGestureAnimation`](#taskstopphonegestureanimation) · [`TaskSubmarineGotoAndStop`](#tasksubmarinegotoandstop) · [`TaskSwapWeapon`](#taskswapweapon) · [`TaskSweepAimEntity`](#tasksweepaimentity) · [`TaskSweepAimPosition`](#tasksweepaimposition) · [`TaskSynchronizedScene`](#tasksynchronizedscene) · [`TaskThrowProjectile`](#taskthrowprojectile) · [`TaskToggleDuck`](#tasktoggleduck) · [`TaskTurnPedToFaceCoord`](#taskturnpedtofacecoord) · [`TaskTurnPedToFaceEntity`](#taskturnpedtofaceentity) · [`TaskUseMobilePhone`](#taskusemobilephone) · [`TaskUseMobilePhoneTimed`](#taskusemobilephonetimed) · [`TaskUseNearestScenarioChainToCoord`](#taskusenearestscenariochaintocoord) · [`TaskUseNearestScenarioChainToCoordWarp`](#taskusenearestscenariochaintocoordwarp) · [`TaskUseNearestScenarioToCoord`](#taskusenearestscenariotocoord) · [`TaskUseNearestScenarioToCoordWarp`](#taskusenearestscenariotocoordwarp) · [`TaskVehicleAimAtCoord`](#taskvehicleaimatcoord) · [`TaskVehicleAimAtPed`](#taskvehicleaimatped) · [`TaskVehicleChase`](#taskvehiclechase) · [`TaskVehicleDriveToCoord`](#taskvehicledrivetocoord) · [`TaskVehicleDriveToCoordLongrange`](#taskvehicledrivetocoordlongrange) · [`TaskVehicleDriveWander`](#taskvehicledrivewander) · [`TaskVehicleEscort`](#taskvehicleescort) · [`TaskVehicleFollow`](#taskvehiclefollow) · [`TaskVehicleFollowWaypointRecording`](#taskvehiclefollowwaypointrecording) · [`TaskVehicleGotoNavmesh`](#taskvehiclegotonavmesh) · [`TaskVehicleHeliProtect`](#taskvehicleheliprotect) · [`TaskVehicleMission`](#taskvehiclemission) · [`TaskVehicleMissionCoorsTarget`](#taskvehiclemissioncoorstarget) · [`TaskVehicleMissionPedTarget`](#taskvehiclemissionpedtarget) · [`TaskVehiclePark`](#taskvehiclepark) · [`TaskVehiclePlayAnim`](#taskvehicleplayanim) · [`TaskVehicleShootAtCoord`](#taskvehicleshootatcoord) · [`TaskVehicleShootAtPed`](#taskvehicleshootatped) · [`TaskVehicleTempAction`](#taskvehicletempaction) · [`TaskWanderInArea`](#taskwanderinarea) · [`TaskWanderSpecific`](#taskwanderspecific) · [`TaskWanderStandard`](#taskwanderstandard) · [`TaskWarpPedDirectlyIntoCover`](#taskwarppeddirectlyintocover) · [`TaskWarpPedIntoVehicle`](#taskwarppedintovehicle) · [`TaskWrithe`](#taskwrithe) · [`UncuffPed`](#uncuffped) · [`UpdateTaskAimGunScriptedTarget`](#updatetaskaimgunscriptedtarget) · [`UpdateTaskHandsUpDuration`](#updatetaskhandsupduration) · [`UpdateTaskSweepAimEntity`](#updatetasksweepaimentity) · [`UpdateTaskSweepAimPosition`](#updatetasksweepaimposition) · [`UseWaypointRecordingAsAssistedMovementRoute`](#usewaypointrecordingasassistedmovementroute) · [`VehicleWaypointPlaybackOverrideSpeed`](#vehiclewaypointplaybackoverridespeed) · [`VehicleWaypointPlaybackPause`](#vehiclewaypointplaybackpause) · [`VehicleWaypointPlaybackResume`](#vehiclewaypointplaybackresume) · [`VehicleWaypointPlaybackUseDefaultSpeed`](#vehiclewaypointplaybackusedefaultspeed) · [`WaypointPlaybackGetIsPaused`](#waypointplaybackgetispaused) · [`WaypointPlaybackOverrideSpeed`](#waypointplaybackoverridespeed) · [`WaypointPlaybackPause`](#waypointplaybackpause) · [`WaypointPlaybackResume`](#waypointplaybackresume) · [`WaypointPlaybackStartAimingAtCoord`](#waypointplaybackstartaimingatcoord) · [`WaypointPlaybackStartAimingAtPed`](#waypointplaybackstartaimingatped) · [`WaypointPlaybackStartShootingAtCoord`](#waypointplaybackstartshootingatcoord) · [`WaypointPlaybackStartShootingAtPed`](#waypointplaybackstartshootingatped) · [`WaypointPlaybackStopAimingOrShooting`](#waypointplaybackstopaimingorshooting) · [`WaypointPlaybackUseDefaultSpeed`](#waypointplaybackusedefaultspeed) · [`WaypointRecordingGetClosestWaypoint`](#waypointrecordinggetclosestwaypoint) · [`WaypointRecordingGetCoord`](#waypointrecordinggetcoord) · [`WaypointRecordingGetNumPoints`](#waypointrecordinggetnumpoints) · [`WaypointRecordingGetSpeedAtPoint`](#waypointrecordinggetspeedatpoint)

---
### AddCoverBlockingArea

`ADD_COVER_BLOCKING_AREA` · hash `0x45C597097DD7CB81` · jhash `0x3536946F` · **Cliente**

```lua
AddCoverBlockingArea(playerX, playerY, playerZ, radiusX, radiusY, radiusZ, p6, p7, p8, p9)
```
```c
void ADD_COVER_BLOCKING_AREA(float playerX, float playerY, float playerZ, float radiusX, float radiusY, float radiusZ, BOOL p6, BOOL p7, BOOL p8, BOOL p9);
```

**Parámetros**

- `playerX` (`float`)
- `playerY` (`float`)
- `playerZ` (`float`)
- `radiusX` (`float`)
- `radiusY` (`float`)
- `radiusZ` (`float`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)
- `p9` (`BOOL`)

**Devuelve:** `void`

---
### AddCoverPoint

`ADD_COVER_POINT` · hash `0xD5C12A75C7B9497F` · jhash `0xA0AF0B98` · **Cliente**

```lua
local retval = AddCoverPoint(p0, p1, p2, p3, p4, p5, p6, p7)
```
```c
ScrHandle ADD_COVER_POINT(float p0, float p1, float p2, float p3, Any p4, Any p5, Any p6, BOOL p7);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`BOOL`)

**Devuelve:** `ScrHandle`

---
### AddPatrolRouteLink

`ADD_PATROL_ROUTE_LINK` · hash `0x23083260DEC3A551` · jhash `0xD8761BB3` · **Cliente**

```lua
AddPatrolRouteLink(id1, id2)
```
```c
void ADD_PATROL_ROUTE_LINK(int id1, int id2);
```

**Parámetros**

- `id1` (`int`): the id representing the first route node
- `id2` (`int`): the id representing the second route node

**Devuelve:** `void`

**Descripción oficial:**

connects/links 2 [route nodes](#addpatrolroutenode)\
image representing the cyclic example below:\
![image](https://user-images.githubusercontent.com/55803068/188470866-c32c6a9f-a25d-4772-9b18-5be46e2c14a1.png)

**Ejemplo (lua):**

```lua
-- these lines connect 1,2,3,4,5,6 in a cyclic manner (1 > 2 > 3 > 4 > 5 > 6 > 1)


AddPatrolRouteLink(1,2)
AddPatrolRouteLink(2,3)
AddPatrolRouteLink(3,4)
AddPatrolRouteLink(4,5)
AddPatrolRouteLink(5,6)
AddPatrolRouteLink(6,1)
```

---
### AddPatrolRouteNode

`ADD_PATROL_ROUTE_NODE` · hash `0x8EDF950167586B7C` · jhash `0x21B48F10` · **Cliente**

```lua
AddPatrolRouteNode(id, guardScenario, x1, y1, z1, x2, y2, z2, waitTime)
```
```c
void ADD_PATROL_ROUTE_NODE(int id, char* guardScenario, float x1, float y1, float z1, float x2, float y2, float z2, int waitTime);
```

**Parámetros**

- `id` (`int`): is an integer that "identifies" the route node for linking to the route with ADD_PATROL_ROUTE_LINK.
- `guardScenario` (`char*`): can be "WORLD_HUMAN_GUARD_STAND" or "StandGuard"
- `x1` (`float`): destination
- `y1` (`float`): destination
- `z1` (`float`): destination
- `x2` (`float`): coordinates to which the ped should look
- `y2` (`float`): coordinates to which the ped should look
- `z2` (`float`): coordinates to which the ped should look
- `waitTime` (`int`): written in ms

**Devuelve:** `void`

**Descripción oficial:**

x2,y2 and z2 are the coordinates to which the ped should look at

**Ejemplo (lua):**

```lua
-- the guard will go toward vector3(1.0, 1.0, 1.0) coordinates looking toward vector3(0.0, 0.0, 0.0) coordinates waiting 1000ms with the WORLD_HUMAN_GUARD_STAND animation
AddPatrolRouteNode(1, "WORLD_HUMAN_GUARD_STAND", vector3(1.0, 1.0, 1.0), vector3(0.0, 0.0, 0.0), 1000)
```

---
### AddVehicleSubtaskAttackCoord

`ADD_VEHICLE_SUBTASK_ATTACK_COORD` · hash `0x5CF0D8F9BBA0DD75` · jhash `0x50779A2C` · **Cliente**

```lua
AddVehicleSubtaskAttackCoord(ped, x, y, z)
```
```c
void ADD_VEHICLE_SUBTASK_ATTACK_COORD(Ped ped, float x, float y, float z);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
x, y, z: offset in world coords from some entity.  
```

---
### AddVehicleSubtaskAttackPed

`ADD_VEHICLE_SUBTASK_ATTACK_PED` · hash `0x85F462BADC7DA47F` · jhash `0x80461113` · **Cliente**

```lua
AddVehicleSubtaskAttackPed(ped, ped2)
```
```c
void ADD_VEHICLE_SUBTASK_ATTACK_PED(Ped ped, Ped ped2);
```

**Parámetros**

- `ped` (`Ped`)
- `ped2` (`Ped`)

**Devuelve:** `void`

---
### AssistedMovementIsRouteLoaded

`ASSISTED_MOVEMENT_IS_ROUTE_LOADED` · hash `0x60F9A4393A21F741` · jhash `0x79B067AF` · **Cliente**

```lua
local retval = AssistedMovementIsRouteLoaded(route)
```
```c
BOOL ASSISTED_MOVEMENT_IS_ROUTE_LOADED(char* route);
```

**Parámetros**

- `route` (`char*`)

**Devuelve:** `BOOL`

---
### AssistedMovementOverrideLoadDistanceThisFrame

`ASSISTED_MOVEMENT_OVERRIDE_LOAD_DISTANCE_THIS_FRAME` · hash `0x13945951E16EF912` · jhash `0x8FB923EC` · **Cliente**

```lua
AssistedMovementOverrideLoadDistanceThisFrame(dist)
```
```c
void ASSISTED_MOVEMENT_OVERRIDE_LOAD_DISTANCE_THIS_FRAME(float dist);
```

**Parámetros**

- `dist` (`float`)

**Devuelve:** `void`

---
### AssistedMovementRemoveRoute

`ASSISTED_MOVEMENT_REMOVE_ROUTE` · hash `0x3548536485DD792B` · jhash `0xB3CEC06F` · **Cliente**

```lua
AssistedMovementRemoveRoute(route)
```
```c
void ASSISTED_MOVEMENT_REMOVE_ROUTE(char* route);
```

**Parámetros**

- `route` (`char*`)

**Devuelve:** `void`

---
### AssistedMovementRequestRoute

`ASSISTED_MOVEMENT_REQUEST_ROUTE` · hash `0x817268968605947A` · jhash `0x48262EDA` · **Cliente**

```lua
AssistedMovementRequestRoute(route)
```
```c
void ASSISTED_MOVEMENT_REQUEST_ROUTE(char* route);
```

**Parámetros**

- `route` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Routes: "1_FIBStairs", "2_FIBStairs", "3_FIBStairs", "4_FIBStairs", "5_FIBStairs", "5_TowardsFire", "6a_FIBStairs", "7_FIBStairs", "8_FIBStairs", "Aprtmnt_1", "AssAfterLift", "ATM_1", "coroner2", "coroner_stairs", "f5_jimmy1", "fame1", "family5b", "family5c", "Family5d", "family5d", "FIB_Glass1", "FIB_Glass2", "FIB_Glass3", "finaBroute1A", "finalb1st", "finalB1sta", "finalbround", "finalbroute2", "Hairdresser1", "jan_foyet_ft_door", "Jo_3", "Lemar1", "Lemar2", "mansion_1", "Mansion_1", "pols_1", "pols_2", "pols_3", "pols_4", "pols_5", "pols_6", "pols_7", "pols_8", "Pro_S1", "Pro_S1a", "Pro_S2", "Towards_case", "trev_steps", "tunrs1", "tunrs2", "tunrs3", "Wave01457s"  
```

---
### AssistedMovementSetRouteProperties

`ASSISTED_MOVEMENT_SET_ROUTE_PROPERTIES` · hash `0xD5002D78B7162E1B` · jhash `0x01CAAFCC` · **Cliente**

```lua
AssistedMovementSetRouteProperties(route, props)
```
```c
void ASSISTED_MOVEMENT_SET_ROUTE_PROPERTIES(char* route, int props);
```

**Parámetros**

- `route` (`char*`)
- `props` (`int`)

**Devuelve:** `void`

---
### ClearDrivebyTaskUnderneathDrivingTask

`CLEAR_DRIVEBY_TASK_UNDERNEATH_DRIVING_TASK` · hash `0xC35B5CDB2824CF69` · jhash `0x9B76F7E6` · **Cliente**

```lua
ClearDrivebyTaskUnderneathDrivingTask(ped)
```
```c
void CLEAR_DRIVEBY_TASK_UNDERNEATH_DRIVING_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ClearPedScriptTaskIfRunningThreatResponseNonTempTask

`CLEAR_PED_SCRIPT_TASK_IF_RUNNING_THREAT_RESPONSE_NON_TEMP_TASK` · hash `0xF6DC48E56BE1243A` · **Cliente**

```lua
ClearPedScriptTaskIfRunningThreatResponseNonTempTask(ped)
```
```c
void CLEAR_PED_SCRIPT_TASK_IF_RUNNING_THREAT_RESPONSE_NON_TEMP_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### ClearPedSecondaryTask

`CLEAR_PED_SECONDARY_TASK` · hash `0x176CECF6F920D707` · jhash `0xA635F451` · **Cliente · también en el servidor (RPC)**

```lua
ClearPedSecondaryTask(ped)
```
```c
void CLEAR_PED_SECONDARY_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ClearPedTasks

`CLEAR_PED_TASKS` · hash `0xE1EF3C1216AFF2CD` · jhash `0xDE3316AB` · **Cliente · también en el servidor (RPC)**

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

---
### ClearPedTasksImmediately

`CLEAR_PED_TASKS_IMMEDIATELY` · hash `0xAAA34F8A7CB32098` · jhash `0xBC045625` · **Cliente · también en el servidor (RPC)**

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

Immediately stops the pedestrian from whatever it's doing. The difference between this and [CLEAR_PED_TASKS](../cfx/servidor.md#clearpedtasks) is that this one teleports the ped but does not change the position of the ped.

---
### ClearSequenceTask

`CLEAR_SEQUENCE_TASK` · hash `0x3841422E9C488D8C` · jhash `0x47ED03CE` · **Cliente**

```lua
local taskSequenceId = ClearSequenceTask(taskSequenceId)
```
```c
void CLEAR_SEQUENCE_TASK(int* taskSequenceId);
```

**Parámetros**

- `taskSequenceId` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The task sequence to clear

**Devuelve:** `void`

**Descripción oficial:**

For an example on how to use this please refer to [OPEN_SEQUENCE_TASK](#opensequencetask)

**NOTE**

If you fail to call [`CLOSE_SEQUENCE_TASK`](#closesequencetask) and `CLEAR_SEQUENCE_TASK` the sequence system can get stuck in a broken state until you restart your client.

---
### ClearVehicleTasks

`_CLEAR_VEHICLE_TASKS` · hash `0xDBBC7A2432524127` · **Cliente**

```lua
ClearVehicleTasks(vehicle)
```
```c
void _CLEAR_VEHICLE_TASKS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to have tasks cleared

**Devuelve:** `void`

**Descripción oficial:**

```
CLEAR_*

NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0xDBBC7A2432524127` (`N_0xdbbc7a2432524127`)

---
### ClosePatrolRoute

`CLOSE_PATROL_ROUTE` · hash `0xB043ECA801B8CBC1` · jhash `0x67305E59` · **Cliente**

```lua
ClosePatrolRoute()
```
```c
void CLOSE_PATROL_ROUTE();
```

**Devuelve:** `void`

---
### CloseSequenceTask

`CLOSE_SEQUENCE_TASK` · hash `0x39E72BC99E6360CB` · jhash `0x1A7CEBD0` · **Cliente**

```lua
CloseSequenceTask(taskSequenceId)
```
```c
void CLOSE_SEQUENCE_TASK(int taskSequenceId);
```

**Parámetros**

- `taskSequenceId` (`int`): The task sequence to close

**Devuelve:** `void`

**Descripción oficial:**

For an example on how to use this please refer to [OPEN_SEQUENCE_TASK](#opensequencetask)

**NOTE**

If you fail to call `CLOSE_SEQUENCE_TASK` and [`CLEAR_SEQUENCE_TASK`](#clearsequencetask) this can get stuck in a broken state until you restart your client.

---
### ControlMountedWeapon

`CONTROL_MOUNTED_WEAPON` · hash `0xDCFE42068FE0135A` · jhash `0x500D9244` · **Cliente**

```lua
local retval = ControlMountedWeapon(ped)
```
```c
BOOL CONTROL_MOUNTED_WEAPON(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Forces the ped to use the mounted weapon.  
Returns false if task is not possible.  
```

---
### CreatePatrolRoute

`CREATE_PATROL_ROUTE` · hash `0xAF8A443CCC8018DC` · jhash `0x0A6C7864` · **Cliente**

```lua
CreatePatrolRoute()
```
```c
void CREATE_PATROL_ROUTE();
```

**Devuelve:** `void`

---
### DeletePatrolRoute

`DELETE_PATROL_ROUTE` · hash `0x7767DD9D65E91319` · jhash `0x2A4E6706` · **Cliente**

```lua
DeletePatrolRoute(patrolRoute)
```
```c
void DELETE_PATROL_ROUTE(char* patrolRoute);
```

**Parámetros**

- `patrolRoute` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
From the b617d scripts:
TASK::DELETE_PATROL_ROUTE("miss_merc0");
TASK::DELETE_PATROL_ROUTE("miss_merc1");
TASK::DELETE_PATROL_ROUTE("miss_merc2");
TASK::DELETE_PATROL_ROUTE("miss_dock");
```

---
### DoesScenarioExistInArea

`DOES_SCENARIO_EXIST_IN_AREA` · hash `0x5A59271FFADD33C1` · jhash `0xFA7F5047` · **Cliente**

```lua
local retval = DoesScenarioExistInArea(x, y, z, radius, b)
```
```c
BOOL DOES_SCENARIO_EXIST_IN_AREA(float x, float y, float z, float radius, BOOL b);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `b` (`BOOL`)

**Devuelve:** `BOOL`

---
### DoesScenarioGroupExist

`DOES_SCENARIO_GROUP_EXIST` · hash `0xF9034C136C9E00D3` · jhash `0x5F072EB9` · **Cliente**

```lua
local retval = DoesScenarioGroupExist(scenarioGroup)
```
```c
BOOL DOES_SCENARIO_GROUP_EXIST(char* scenarioGroup);
```

**Parámetros**

- `scenarioGroup` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Occurrences in the b617d scripts:
"ARMY_GUARD",
"ARMY_HELI",
"Cinema_Downtown",
"Cinema_Morningwood",
"Cinema_Textile",
"City_Banks",
"Countryside_Banks",
"DEALERSHIP",
"GRAPESEED_PLANES",
"KORTZ_SECURITY",
"LOST_BIKERS",
"LSA_Planes",
"LSA_Planes",
"MP_POLICE",
"Observatory_Bikers",
"POLICE_POUND1",
"POLICE_POUND2",
"POLICE_POUND3",
"POLICE_POUND4",
"POLICE_POUND5"
"QUARRY",
"SANDY_PLANES",
"SCRAP_SECURITY",
"SEW_MACHINE",
"SOLOMON_GATE",
"Triathlon_1_Start",
"Triathlon_2_Start",
"Triathlon_3_Start"
Sometimes used with IS_SCENARIO_GROUP_ENABLED:
if (TASK::DOES_SCENARIO_GROUP_EXIST("Observatory_Bikers") && (!TASK::IS_SCENARIO_GROUP_ENABLED("Observatory_Bikers"))) {
else if (TASK::IS_SCENARIO_GROUP_ENABLED("BLIMP")) {
```

---
### DoesScenarioOfTypeExistInArea

`DOES_SCENARIO_OF_TYPE_EXIST_IN_AREA` · hash `0x0A9D0C2A3BBC86C1` · jhash `0x0FB138A5` · **Cliente**

```lua
local retval = DoesScenarioOfTypeExistInArea(p0, p1, p2, p3, p4, p5)
```
```c
BOOL DOES_SCENARIO_OF_TYPE_EXIST_IN_AREA(float p0, float p1, float p2, char* p3, float p4, BOOL p5);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`char*`)
- `p4` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `BOOL`

---
### DoesScriptedCoverPointExistAtCoords

`DOES_SCRIPTED_COVER_POINT_EXIST_AT_COORDS` · hash `0xA98B8E3C088E5A31` · jhash `0x29F97A71` · **Cliente**

```lua
local retval = DoesScriptedCoverPointExistAtCoords(x, y, z)
```
```c
BOOL DOES_SCRIPTED_COVER_POINT_EXIST_AT_COORDS(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks if there is a cover point at position  
```

---
### GetActiveVehicleMissionType

`GET_ACTIVE_VEHICLE_MISSION_TYPE` · hash `0x534AEBA6E5ED4CAB` · jhash `0xAFA914EF` · **Cliente**

```lua
local retval = GetActiveVehicleMissionType(vehicle)
```
```c
int GET_ACTIVE_VEHICLE_MISSION_TYPE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
https://alloc8or.re/gta5/doc/enums/eVehicleMissionType.txt
```

---
### GetClipSetForScriptedGunTask

`GET_CLIP_SET_FOR_SCRIPTED_GUN_TASK` · hash `0x3A8CADC7D37AACC5` · jhash `0x249EB4EB` · **Cliente**

```lua
local retval = GetClipSetForScriptedGunTask(p0)
```
```c
char* GET_CLIP_SET_FOR_SCRIPTED_GUN_TASK(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `char*`

---
### GetIsTaskActive

`GET_IS_TASK_ACTIVE` · hash `0xB0760331C7AA4155` · jhash `0x86FDDF55` · **Cliente**

```lua
local retval = GetIsTaskActive(ped, taskIndex)
```
```c
BOOL GET_IS_TASK_ACTIVE(Ped ped, int taskIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `taskIndex` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Task index enum: https://alloc8or.re/gta5/doc/enums/eTaskTypeIndex.txt
```

---
### GetIsWaypointRecordingLoaded

`GET_IS_WAYPOINT_RECORDING_LOADED` · hash `0xCB4E8BE8A0063C5D` · jhash `0x87125F5D` · **Cliente**

```lua
local retval = GetIsWaypointRecordingLoaded(name)
```
```c
BOOL GET_IS_WAYPOINT_RECORDING_LOADED(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

---
### GetNavmeshRouteDistanceRemaining

`GET_NAVMESH_ROUTE_DISTANCE_REMAINING` · hash `0xC6F5C0BCDC74D62D` · jhash `0xD9281778` · **Cliente**

```lua
local retval, distanceRemaining, isPathReady = GetNavmeshRouteDistanceRemaining(ped)
```
```c
int GET_NAVMESH_ROUTE_DISTANCE_REMAINING(Ped ped, float* distanceRemaining, BOOL* isPathReady);
```

**Parámetros**

- `ped` (`Ped`)
- `distanceRemaining` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `isPathReady` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `int`

**Descripción oficial:**

```
Looks like the last parameter returns true if the path has been calculated, while the first returns the remaining distance to the end of the path.
Return value of native is the same as GET_NAVMESH_ROUTE_RESULT
Looks like the native returns an int for the path's state:
1 - ???
2 - ???
3 - Finished Generating
```

---
### GetNavmeshRouteResult

`GET_NAVMESH_ROUTE_RESULT` · hash `0x632E831F382A0FA8` · jhash `0x96491602` · **Cliente**

```lua
local retval = GetNavmeshRouteResult(ped)
```
```c
int GET_NAVMESH_ROUTE_RESULT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

See [`GET_NAVMESH_ROUTE_DISTANCE_REMAINING`](#getnavmeshroutedistanceremaining) for more details.

---
### GetPedDesiredMoveBlendRatio

`GET_PED_DESIRED_MOVE_BLEND_RATIO` · hash `0x8517D4A6CA8513ED` · jhash `0x5FEFAB72` · **Cliente**

```lua
local retval = GetPedDesiredMoveBlendRatio(ped)
```
```c
float GET_PED_DESIRED_MOVE_BLEND_RATIO(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `float`

---
### GetPedWaypointDistance

`GET_PED_WAYPOINT_DISTANCE` · hash `0xE6A877C64CAF1BC5` · jhash `0x084B35B0` · **Cliente**

```lua
local retval = GetPedWaypointDistance(p0)
```
```c
float GET_PED_WAYPOINT_DISTANCE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `float`

---
### GetPedWaypointProgress

`GET_PED_WAYPOINT_PROGRESS` · hash `0x2720AAA75001E094` · jhash `0x3595B104` · **Cliente**

```lua
local retval = GetPedWaypointProgress(ped)
```
```c
int GET_PED_WAYPOINT_PROGRESS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetPhoneGestureAnimCurrentTime

`GET_PHONE_GESTURE_ANIM_CURRENT_TIME` · hash `0x47619ABE8B268C60` · jhash `0x7B72AFD1` · **Cliente**

```lua
local retval = GetPhoneGestureAnimCurrentTime(ped)
```
```c
float GET_PHONE_GESTURE_ANIM_CURRENT_TIME(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `float`

---
### GetPhoneGestureAnimTotalTime

`GET_PHONE_GESTURE_ANIM_TOTAL_TIME` · hash `0x1EE0F68A7C25DEC6` · jhash `0xEF8C3959` · **Cliente**

```lua
local retval = GetPhoneGestureAnimTotalTime(ped)
```
```c
float GET_PHONE_GESTURE_ANIM_TOTAL_TIME(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `float`

---
### GetScriptTaskStatus

`GET_SCRIPT_TASK_STATUS` · hash `0x77F1BEB8863288D5` · jhash `0xB2477B23` · **Cliente**

```lua
local retval = GetScriptTaskStatus(ped, taskHash)
```
```c
int GET_SCRIPT_TASK_STATUS(Ped ped, Hash taskHash);
```

**Parámetros**

- `ped` (`Ped`): The ped the task is running on
- `taskHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of the task

**Devuelve:** `int` — The status of the script-assigned task.

**Descripción oficial:**

Gets the status of a spesifed script-assigned task on the given ped. The return value is always an int between 0-7.

You can set taskHash to `SCRIPT_TASK_ANY` to check if any task is active, it will return 1 for active, 3 for no active.
`SCRIPT_TASK_INVALID` can be similarly used, it returns 7 if there are any active task, and 3 if there are no active tasks.

taskHash list: https://alloc8or.re/gta5/doc/enums/eScriptTaskHash.txt

Returns:

```
0 = WAITING_TO_START_TASK
1 = PERFORMING_TASK
2 = DORMANT_TASK
3 = VACANT_STAGE
7 = TASK_FINISHED_OR_NOT_FOUND
```

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local coords = GetOffsetFromEntityInWorldCoords(playerPed, 0.0, 6.0, 0.0)
TaskGoStraightToCoord(playerPed, coords, 1.0, 5000, GetEntityHeading(playerPed), 0.15)

Citizen.CreateThread(function()
    while true do
        local taskStatus = GetScriptTaskStatus(PlayerPedId(), "SCRIPT_TASK_GO_STRAIGHT_TO_COORD")
        print(taskStatus)
        if taskStatus == 7 then print("task was finished!"); break end
        Citizen.Wait(250)
    end
end)
```

---
### GetScriptedCoverPointCoords

`GET_SCRIPTED_COVER_POINT_COORDS` · hash `0x594A1028FC2A3E85` · jhash `0xC6B6CCC1` · **Cliente**

```lua
local retval = GetScriptedCoverPointCoords(coverpoint)
```
```c
Vector3 GET_SCRIPTED_COVER_POINT_COORDS(ScrHandle coverpoint);
```

**Parámetros**

- `coverpoint` (`ScrHandle`)

**Devuelve:** `Vector3`

---
### GetSequenceProgress

`GET_SEQUENCE_PROGRESS` · hash `0x00A9010CFE1E3533` · jhash `0xA3419909` · **Cliente**

```lua
local retval = GetSequenceProgress(ped)
```
```c
int GET_SEQUENCE_PROGRESS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
returned values:
0 to 7 = task that's currently in progress, 0 meaning the first one.
-1 no task sequence in progress.
```

---
### GetTaskMoveNetworkEvent

`GET_TASK_MOVE_NETWORK_EVENT` · hash `0xB4F47213DF45A64C` · jhash `0x72FA5EF2` · **Cliente**

```lua
local retval = GetTaskMoveNetworkEvent(ped, eventName)
```
```c
BOOL GET_TASK_MOVE_NETWORK_EVENT(Ped ped, char* eventName);
```

**Parámetros**

- `ped` (`Ped`)
- `eventName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB4F47213DF45A64C` (`N_0xb4f47213df45a64c`)

---
### GetTaskMoveNetworkSignalBool

`GET_TASK_MOVE_NETWORK_SIGNAL_BOOL` · hash `0xA7FFBA498E4AAF67` · jhash `0x1EBB6F3D` · **Cliente**

```lua
local retval = GetTaskMoveNetworkSignalBool(ped, signalName)
```
```c
BOOL GET_TASK_MOVE_NETWORK_SIGNAL_BOOL(Ped ped, char* signalName);
```

**Parámetros**

- `ped` (`Ped`)
- `signalName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA7FFBA498E4AAF67` (`N_0xa7ffba498e4aaf67`)

---
### GetTaskMoveNetworkSignalFloat

`_GET_TASK_MOVE_NETWORK_SIGNAL_FLOAT` · hash `0x44AB0B3AFECCE242` · **Cliente**

```lua
local retval = GetTaskMoveNetworkSignalFloat(ped, signalName)
```
```c
float _GET_TASK_MOVE_NETWORK_SIGNAL_FLOAT(Ped ped, char* signalName);
```

**Parámetros**

- `ped` (`Ped`)
- `signalName` (`char*`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### GetTaskMoveNetworkState

`GET_TASK_MOVE_NETWORK_STATE` · hash `0x717E4D1F2048376D` · jhash `0x96C0277B` · **Cliente**

```lua
local retval = GetTaskMoveNetworkState(ped)
```
```c
char* GET_TASK_MOVE_NETWORK_STATE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0x717E4D1F2048376D` (`N_0x717e4d1f2048376d`)

---
### GetVehicleWaypointProgress

`GET_VEHICLE_WAYPOINT_PROGRESS` · hash `0x9824CFF8FC66E159` · jhash `0xD3CCF64E` · **Cliente**

```lua
local retval = GetVehicleWaypointProgress(vehicle)
```
```c
int GET_VEHICLE_WAYPOINT_PROGRESS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleWaypointTargetPoint

`GET_VEHICLE_WAYPOINT_TARGET_POINT` · hash `0x416B62AC8B9E5BBD` · jhash `0x81049608` · **Cliente**

```lua
local retval = GetVehicleWaypointTargetPoint(vehicle)
```
```c
int GET_VEHICLE_WAYPOINT_TARGET_POINT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetWaypointDistanceAlongRoute

`GET_WAYPOINT_DISTANCE_ALONG_ROUTE` · hash `0xA5B769058763E497` · jhash `0xE8422AC4` · **Cliente**

```lua
local retval = GetWaypointDistanceAlongRoute(p0, p1)
```
```c
float GET_WAYPOINT_DISTANCE_ALONG_ROUTE(char* p0, int p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`int`)

**Devuelve:** `float`

---
### IsDrivebyTaskUnderneathDrivingTask

`IS_DRIVEBY_TASK_UNDERNEATH_DRIVING_TASK` · hash `0x8785E6E40C7A8818` · jhash `0xB23F46E6` · **Cliente**

```lua
local retval = IsDrivebyTaskUnderneathDrivingTask(ped)
```
```c
BOOL IS_DRIVEBY_TASK_UNDERNEATH_DRIVING_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsMountedWeaponTaskUnderneathDrivingTask

`IS_MOUNTED_WEAPON_TASK_UNDERNEATH_DRIVING_TASK` · hash `0xA320EF046186FA3B` · jhash `0x291E938C` · **Cliente**

```lua
local retval = IsMountedWeaponTaskUnderneathDrivingTask(ped)
```
```c
BOOL IS_MOUNTED_WEAPON_TASK_UNDERNEATH_DRIVING_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsMoveBlendRatioRunning

`IS_MOVE_BLEND_RATIO_RUNNING` · hash `0xD4D8636C0199A939` · jhash `0xE76A2353` · **Cliente**

```lua
local retval = IsMoveBlendRatioRunning(ped)
```
```c
BOOL IS_MOVE_BLEND_RATIO_RUNNING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsMoveBlendRatioSprinting

`IS_MOVE_BLEND_RATIO_SPRINTING` · hash `0x24A2AD74FA9814E2` · jhash `0xDD616893` · **Cliente**

```lua
local retval = IsMoveBlendRatioSprinting(ped)
```
```c
BOOL IS_MOVE_BLEND_RATIO_SPRINTING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsMoveBlendRatioStill

`IS_MOVE_BLEND_RATIO_STILL` · hash `0x349CE7B56DAFD95C` · jhash `0xE9DAF877` · **Cliente**

```lua
local retval = IsMoveBlendRatioStill(ped)
```
```c
BOOL IS_MOVE_BLEND_RATIO_STILL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsMoveBlendRatioWalking

`IS_MOVE_BLEND_RATIO_WALKING` · hash `0xF133BBBE91E1691F` · jhash `0xD21639A8` · **Cliente**

```lua
local retval = IsMoveBlendRatioWalking(ped)
```
```c
BOOL IS_MOVE_BLEND_RATIO_WALKING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedActiveInScenario

`IS_PED_ACTIVE_IN_SCENARIO` · hash `0xAA135F9482C82CC3` · jhash `0x05038F1A` · **Cliente**

```lua
local retval = IsPedActiveInScenario(ped)
```
```c
BOOL IS_PED_ACTIVE_IN_SCENARIO(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.

**Devuelve:** `BOOL` — Returns true if the ped is in a using a scenario and is doing the ambient animations.

**Descripción oficial:**

This is a stricter version of [`IS_PED_USING_ANY_SCENARIO`](PED-1.md#ispedusinganyscenario). It only returns true if the ped is playing the ambient animations associated with the scenario.

---
### IsPedBeingArrested

`IS_PED_BEING_ARRESTED` · hash `0x90A09F3A45FED688` · jhash `0x5FF6C2ED` · **Cliente**

```lua
local retval = IsPedBeingArrested(ped)
```
```c
BOOL IS_PED_BEING_ARRESTED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function is hard-coded to always return 0.  
```

---
### IsPedCuffed

`IS_PED_CUFFED` · hash `0x74E559B3BC910685` · jhash `0x511CE741` · **Cliente**

```lua
local retval = IsPedCuffed(ped)
```
```c
BOOL IS_PED_CUFFED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedGettingUp

`IS_PED_GETTING_UP` · hash `0x2A74E1D5F2F00EEC` · jhash `0x320813E6` · **Cliente**

```lua
local retval = IsPedGettingUp(ped)
```
```c
BOOL IS_PED_GETTING_UP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInWrithe

`IS_PED_IN_WRITHE` · hash `0xDEB6D52126E7D640` · jhash `0x09E61921` · **Cliente**

```lua
local retval = IsPedInWrithe(ped)
```
```c
BOOL IS_PED_IN_WRITHE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns `true` if the ped is in [writhe](https://dictionary.cambridge.org/dictionary/english/writhe), `false` otherwise.

**Descripción oficial:**

This native checks if a ped is on the ground, in pain from a (gunshot) wound.

---
### IsPedPlayingBaseClipInScenario

`IS_PED_PLAYING_BASE_CLIP_IN_SCENARIO` · hash `0x621C6E4729388E41` · jhash `0xA0DA6B1D` · **Cliente**

```lua
local retval = IsPedPlayingBaseClipInScenario(ped)
```
```c
BOOL IS_PED_PLAYING_BASE_CLIP_IN_SCENARIO(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x621C6E4729388E41` (`N_0x621c6e4729388e41`)

---
### IsPedRunning

`IS_PED_RUNNING` · hash `0xC5286FFC176F28A2` · jhash `0xE9A5578F` · **Cliente**

```lua
local retval = IsPedRunning(ped)
```
```c
BOOL IS_PED_RUNNING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedRunningArrestTask

`IS_PED_RUNNING_ARREST_TASK` · hash `0x3DC52677769B4AE0` · jhash `0x6942DB7A` · **Cliente**

```lua
local retval = IsPedRunningArrestTask(ped)
```
```c
BOOL IS_PED_RUNNING_ARREST_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedSprinting

`IS_PED_SPRINTING` · hash `0x57E457CD2C0FC168` · jhash `0x4F3E0633` · **Cliente**

```lua
local retval = IsPedSprinting(ped)
```
```c
BOOL IS_PED_SPRINTING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedStill

`IS_PED_STILL` · hash `0xAC29253EEF8F0180` · jhash `0x09E3418D` · **Cliente**

```lua
local retval = IsPedStill(ped)
```
```c
BOOL IS_PED_STILL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedStrafing

`IS_PED_STRAFING` · hash `0xE45B7F222DE47E09` · jhash `0xEFEED13C` · **Cliente**

```lua
local retval = IsPedStrafing(ped)
```
```c
BOOL IS_PED_STRAFING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
What's strafing?  
```

---
### IsPedWalking

`IS_PED_WALKING` · hash `0xDE4C184B2B9B071A` · jhash `0x4B865C4A` · **Cliente**

```lua
local retval = IsPedWalking(ped)
```
```c
BOOL IS_PED_WALKING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPlayingPhoneGestureAnim

`IS_PLAYING_PHONE_GESTURE_ANIM` · hash `0xB8EBB1E9D3588C10` · jhash `0x500B6805` · **Cliente**

```lua
local retval = IsPlayingPhoneGestureAnim(ped)
```
```c
BOOL IS_PLAYING_PHONE_GESTURE_ANIM(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsScenarioGroupEnabled

`IS_SCENARIO_GROUP_ENABLED` · hash `0x367A09DED4E05B99` · jhash `0x90991122` · **Cliente**

```lua
local retval = IsScenarioGroupEnabled(scenarioGroup)
```
```c
BOOL IS_SCENARIO_GROUP_ENABLED(char* scenarioGroup);
```

**Parámetros**

- `scenarioGroup` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
 Occurrences in the b617d scripts:
 "ARMY_GUARD",
 "ARMY_HELI",
 "BLIMP",
 "Cinema_Downtown",
 "Cinema_Morningwood",
 "Cinema_Textile",
 "City_Banks",
 "Countryside_Banks",
 "DEALERSHIP",
 "KORTZ_SECURITY",
 "LSA_Planes",
 "MP_POLICE",
 "Observatory_Bikers",
 "POLICE_POUND1",
 "POLICE_POUND2",
 "POLICE_POUND3",
 "POLICE_POUND4",
 "POLICE_POUND5",
 "Rampage1",
 "SANDY_PLANES",
 "SCRAP_SECURITY",
 "SEW_MACHINE",
 "SOLOMON_GATE"
Sometimes used with DOES_SCENARIO_GROUP_EXIST:
if (TASK::DOES_SCENARIO_GROUP_EXIST("Observatory_Bikers") &&   (!TASK::IS_SCENARIO_GROUP_ENABLED("Observatory_Bikers"))) {
else if (TASK::IS_SCENARIO_GROUP_ENABLED("BLIMP")) {
```

---
### IsScenarioOccupied

`IS_SCENARIO_OCCUPIED` · hash `0x788756D73AC2E07C` · jhash `0x697FC008` · **Cliente**

```lua
local retval = IsScenarioOccupied(p0, p1, p2, p3, p4)
```
```c
BOOL IS_SCENARIO_OCCUPIED(float p0, float p1, float p2, float p3, BOOL p4);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsScenarioTypeEnabled

`IS_SCENARIO_TYPE_ENABLED` · hash `0x3A815DB3EA088722` · jhash `0xAE37E969` · **Cliente**

```lua
local retval = IsScenarioTypeEnabled(scenarioType)
```
```c
BOOL IS_SCENARIO_TYPE_ENABLED(char* scenarioType);
```

**Parámetros**

- `scenarioType` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Occurrences in the b617d scripts:
"PROP_HUMAN_SEAT_CHAIR",
"WORLD_HUMAN_DRINKING",
"WORLD_HUMAN_HANG_OUT_STREET",
"WORLD_HUMAN_SMOKING",
"WORLD_MOUNTAIN_LION_WANDER",
"WORLD_HUMAN_DRINKING"
Sometimes used together with MISC::IS_STRING_NULL_OR_EMPTY in the scripts.
scenarioType could be the same as scenarioName, used in for example TASK::TASK_START_SCENARIO_AT_POSITION.
```

---
### IsTaskMoveNetworkActive

`IS_TASK_MOVE_NETWORK_ACTIVE` · hash `0x921CE12C489C4C41` · jhash `0x902656EB` · **Cliente**

```lua
local retval = IsTaskMoveNetworkActive(ped)
```
```c
BOOL IS_TASK_MOVE_NETWORK_ACTIVE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x921CE12C489C4C41` (`N_0x921ce12c489c4c41`)

---
### IsTaskMoveNetworkReadyForTransition

`IS_TASK_MOVE_NETWORK_READY_FOR_TRANSITION` · hash `0x30ED88D5E0C56A37` · jhash `0x92FDBAE6` · **Cliente**

```lua
local retval = IsTaskMoveNetworkReadyForTransition(ped)
```
```c
BOOL IS_TASK_MOVE_NETWORK_READY_FOR_TRANSITION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x30ED88D5E0C56A37` (`N_0x30ed88d5e0c56a37`)

---
### IsWaypointPlaybackGoingOnForPed

`IS_WAYPOINT_PLAYBACK_GOING_ON_FOR_PED` · hash `0xE03B3F2D3DC59B64` · jhash `0x85B7725F` · **Cliente**

```lua
local retval = IsWaypointPlaybackGoingOnForPed(p0)
```
```c
BOOL IS_WAYPOINT_PLAYBACK_GOING_ON_FOR_PED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### IsWaypointPlaybackGoingOnForVehicle

`IS_WAYPOINT_PLAYBACK_GOING_ON_FOR_VEHICLE` · hash `0xF5134943EA29868C` · jhash `0x80DD15DB` · **Cliente**

```lua
local retval = IsWaypointPlaybackGoingOnForVehicle(vehicle)
```
```c
BOOL IS_WAYPOINT_PLAYBACK_GOING_ON_FOR_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### N_0x0ffb3c758e8c07b9

`0x0FFB3C758E8C07B9` · hash `0x0FFB3C758E8C07B9` · **Cliente**

```lua
local retval = N_0x0ffb3c758e8c07b9(ped, p1)
```
```c
Any 0x0FFB3C758E8C07B9(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `Any`

**Descripción oficial:**

Doesn't actually return anything.

```
NativeDB Introduced: v2060
```

---
### N_0x1f351cf1c6475734

`0x1F351CF1C6475734` · hash `0x1F351CF1C6475734` · **Cliente**

```lua
N_0x1f351cf1c6475734(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
void 0x1F351CF1C6475734(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)
- `p9` (`Any`)

**Devuelve:** `void`

---
### N_0x29682e2ccf21e9b5

`0x29682E2CCF21E9B5` · hash `0x29682E2CCF21E9B5` · **Cliente**

```lua
N_0x29682e2ccf21e9b5(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
```
```c
void 0x29682E2CCF21E9B5(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9, Any p10, Any p11, Any p12, Any p13);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)
- `p9` (`Any`)
- `p10` (`Any`)
- `p11` (`Any`)
- `p12` (`Any`)
- `p13` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x3e38e28a1d80ddf6

`0x3E38E28A1D80DDF6` · hash `0x3E38E28A1D80DDF6` · jhash `0x54856309` · **Cliente**

```lua
local retval = N_0x3e38e28a1d80ddf6(ped)
```
```c
BOOL 0x3E38E28A1D80DDF6(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_*
```

---
### N_0x53ddc75bc3ac0a90

`0x53DDC75BC3AC0A90` · hash `0x53DDC75BC3AC0A90` · **Cliente**

```lua
N_0x53ddc75bc3ac0a90(vehicle)
```
```c
void 0x53DDC75BC3AC0A90(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to have tasks cleared

**Devuelve:** `void`

**Descripción oficial:**

Related to [`_CLEAR_VEHICLE_TASKS`](#clearvehicletasks) and requires more research (e.g., \_CLEAR_VEHICLE_SECONDARY_TASKS).

```
CLEAR_*

NativeDB Introduced: v1290
```

---
### N_0x6100b3cefd43452e

`0x6100B3CEFD43452E` · hash `0x6100B3CEFD43452E` · **Cliente**

```lua
N_0x6100b3cefd43452e(p0)
```
```c
void 0x6100B3CEFD43452E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0x8423541e8b3a1589

`0x8423541E8B3A1589` · hash `0x8423541E8B3A1589` · **Cliente**

```lua
N_0x8423541e8b3a1589(p0, p1, p2)
```
```c
void 0x8423541E8B3A1589(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x8634cef2522d987b

`0x8634CEF2522D987B` · hash `0x8634CEF2522D987B` · **Cliente**

```lua
N_0x8634cef2522d987b(ped, p1, value)
```
```c
void 0x8634CEF2522D987B(Ped ped, char* p1, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x9d252648778160df

`0x9D252648778160DF` · hash `0x9D252648778160DF` · **Cliente**

```lua
local retval = N_0x9d252648778160df(p0)
```
```c
Any 0x9D252648778160DF(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0xab13a5565480b6d9

`0xAB13A5565480B6D9` · hash `0xAB13A5565480B6D9` · jhash `0x1E58A7AD` · **Cliente**

```lua
local retval = N_0xab13a5565480b6d9(ped, p1)
```
```c
Any 0xAB13A5565480B6D9(Ped ped, char* p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Used only once in the scripts (fm_mission_controller) like so:

TASK::_0xAB13A5565480B6D9(iLocal_3160, "Cutting");

SET_*
```

---
### N_0xfa83ca6776038f64

`0xFA83CA6776038F64` · hash `0xFA83CA6776038F64` · **Cliente**

```lua
N_0xfa83ca6776038f64(x, y, z)
```
```c
void 0xFA83CA6776038F64(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
REMOVE_*

NativeDB Introduced: v1493
```

---
### OpenPatrolRoute

`OPEN_PATROL_ROUTE` · hash `0xA36BFB5EE89F3D82` · jhash `0xF33F83CA` · **Cliente**

```lua
OpenPatrolRoute(patrolRoute)
```
```c
void OPEN_PATROL_ROUTE(char* patrolRoute);
```

**Parámetros**

- `patrolRoute` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
The patrol route name must starts with "miss_" to be properly created. 

 patrolRoutes found in the b617d scripts:
 "miss_Ass0",
 "miss_Ass1",
 "miss_Ass2",
 "miss_Ass3",
 "miss_Ass4",
 "miss_Ass5",
 "miss_Ass6",
 "MISS_PATROL_6",
 "MISS_PATROL_7",
 "MISS_PATROL_8",
 "MISS_PATROL_9",
 "miss_Tower_01",
 "miss_Tower_02",
 "miss_Tower_03",
 "miss_Tower_04",
 "miss_Tower_05",
 "miss_Tower_06",
 "miss_Tower_07",
 "miss_Tower_08",
 "miss_Tower_10"
```

---
### OpenSequenceTask

`OPEN_SEQUENCE_TASK` · hash `0xE8854A4326B9E12B` · jhash `0xABA6923E` · **Cliente**

```lua
local taskSequenceId = OpenSequenceTask(taskSequenceId)
```
```c
void OPEN_SEQUENCE_TASK(int* taskSequenceId);
```

**Parámetros**

- `taskSequenceId` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The reference to bind to, in Lua/JS this will be returned as a value

**Devuelve:** `void`

**Descripción oficial:**

**NOTE**

If this returns 0 that means it failed to get a sequence id.

If you fail to call [`CLOSE_SEQUENCE_TASK`](#closesequencetask) and [`CLEAR_SEQUENCE_TASK`](#clearsequencetask) the sequence system can get stuck in a broken state until you restart your client.

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    local animDict = 'timetable@ron@ig_5_p3'

    RequestAnimDict(animDict)
    while not HasAnimDictLoaded(animDict) do
        Wait(0)
    end

    local ped = PlayerPedId()
    local pos = GetEntityCoords(ped)

    -- you can change the model, but you might have to change the offsets below.
    local objModelHash = `prop_bench_01a`

    local obj = GetClosestObjectOfType(pos.x, pos.y, pos.z, 5.0, objModelHash, false, false, false)
    if obj == 0 then
        print("No valid object within range!")
        return
    end

    local tgtPos = GetOffsetFromEntityInWorldCoords(obj, 0.0, -0.7, 0.0)

    -- open the task sequence so we can get our sequence id
    local sequence = OpenSequenceTask()

    -- set our desired heading to be the same as the objects
    local desiredHeading = GetEntityHeading(obj) - 180.0

    -- go to the entities offset
    TaskGoStraightToCoord(nil, tgtPos.x, tgtPos.y, tgtPos.z, 1.0, 4000, desiredHeading, 1.0)

    -- sit on the bench indefinitely (you can change -1 here to however long you want to sit)
    TaskPlayAnim(nil, animDict, 'ig_5_p3_base', 8.0, 8.0, -1, 1)

    -- close the sequence so we can perform it
    CloseSequenceTask(sequence)

    -- perform the sequence, this will not work if the sequence is still open.
    TaskPerformSequence(ped, sequence)

    -- free the sequence slot so it can be re-used
    ClearSequenceTask(sequence)

    -- cleanup the animation dict so the engine can remove it when its no longer needed
    RemoveAnimDict(animDict)
end)
```

**Ejemplo (cs):**

```cs
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

string animDict = "timetable@ron@ig_5_p3";
RequestAnimDict(animDict);
while (!HasAnimDictLoaded(animDict))
{
	await BaseScript.Delay(0);
}

int ped = PlayerPedId();
Vector3 pos = GetEntityCoords(ped, false);

// you can change the model, but you might have to change the offsets below.
uint hash = Game.GenerateHashASCII("prop_bench_01a");

int obj = GetClosestObjectOfType(pos.X, pos.Y, pos.Z, 5.0f, hash, false, false, false);
if (obj == 0)
{
	Debug.WriteLine("No valid object within range!");
	return;
}

Vector3 tgtPos = GetOffsetFromEntityInWorldCoords(obj, 0.0f, -0.7f, 0.0f);

int sequenceId = 0;
// open the task sequence so we can get our sequence id
OpenSequenceTask(ref sequenceId);

float desiredHeading = GetEntityHeading(obj) - 180.0f;

// go to the entities offset
TaskGoStraightToCoord(0, tgtPos.X, tgtPos.Y, tgtPos.Z, 1.0f, 4000, desiredHeading, 1.0f);

// sit on the bench indefinitely (you can change -1 here to however long you want to sit)
TaskPlayAnim(0, animDict, "ig_5_p3_base", 8.0f, 8.0f, -1, 1, 1.0f, false, false, false);

// close the sequence so we can perform it
CloseSequenceTask(sequenceId);

// perform the sequence, this will not work if the sequence is still open.
TaskPerformSequence(ped, sequenceId);

// free the sequence slot so it can be re-used
ClearSequenceTask(ref sequenceId);

// cleanup the animation dict so the engine can remove it when its no longer needed
RemoveAnimDict(animDict);
```

---
### PedHasUseScenarioTask

`PED_HAS_USE_SCENARIO_TASK` · hash `0x295E3CCEC879CCD7` · jhash `0x9BE9C691` · **Cliente**

```lua
local retval = PedHasUseScenarioTask(ped)
```
```c
BOOL PED_HAS_USE_SCENARIO_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### PlayAnimOnRunningScenario

`PLAY_ANIM_ON_RUNNING_SCENARIO` · hash `0x748040460F8DF5DC` · jhash `0x1984A5D1` · **Cliente**

```lua
PlayAnimOnRunningScenario(ped, animDict, animName)
```
```c
void PLAY_ANIM_ON_RUNNING_SCENARIO(Ped ped, char* animDict, char* animName);
```

**Parámetros**

- `ped` (`Ped`)
- `animDict` (`char*`)
- `animName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### PlayEntityScriptedAnim

`PLAY_ENTITY_SCRIPTED_ANIM` · hash `0x77A1EEC547E7FCF1` · jhash `0x02F72AE5` · **Cliente**

```lua
local p1, p2, p3 = PlayEntityScriptedAnim(p0, p4, p5)
```
```c
void PLAY_ENTITY_SCRIPTED_ANIM(Any p0, Any* p1, Any* p2, Any* p3, float p4, float p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `void`

---
### RemoveAllCoverBlockingAreas

`REMOVE_ALL_COVER_BLOCKING_AREAS` · hash `0xDB6708C0B46F56D8` · jhash `0xCF9221A7` · **Cliente**

```lua
RemoveAllCoverBlockingAreas()
```
```c
void REMOVE_ALL_COVER_BLOCKING_AREAS();
```

**Devuelve:** `void`

---
### RemoveCoverPoint

`REMOVE_COVER_POINT` · hash `0xAE287C923D891715` · jhash `0x0776888B` · **Cliente**

```lua
RemoveCoverPoint(coverpoint)
```
```c
void REMOVE_COVER_POINT(ScrHandle coverpoint);
```

**Parámetros**

- `coverpoint` (`ScrHandle`)

**Devuelve:** `void`

---
### RemoveWaypointRecording

`REMOVE_WAYPOINT_RECORDING` · hash `0xFF1B8B4AA1C25DC8` · jhash `0x624530B0` · **Cliente**

```lua
RemoveWaypointRecording(name)
```
```c
void REMOVE_WAYPOINT_RECORDING(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

---
### RequestTaskMoveNetworkStateTransition

`REQUEST_TASK_MOVE_NETWORK_STATE_TRANSITION` · hash `0xD01015C7316AE176` · jhash `0x885724DE` · **Cliente**

```lua
local retval = RequestTaskMoveNetworkStateTransition(ped, name)
```
```c
BOOL REQUEST_TASK_MOVE_NETWORK_STATE_TRANSITION(Ped ped, char* name);
```

**Parámetros**

- `ped` (`Ped`): A ped handle.
- `name` (`char*`): The name of the target request state in the move network file.

**Devuelve:** `BOOL` — Technically a `void`. Scripts treat this as a boolean, but the game never sets the result, so it will return the ped handle instead.

**Nombres antiguos (alias):** `0xD01015C7316AE176` (`N_0xd01015c7316ae176`)

---
### RequestWaypointRecording

`REQUEST_WAYPOINT_RECORDING` · hash `0x9EEFB62EB27B5792` · jhash `0xAFABFB5D` · **Cliente**

```lua
RequestWaypointRecording(name)
```
```c
void REQUEST_WAYPOINT_RECORDING(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
For a full list of the points, see here: goo.gl/wIH0vn
Max number of loaded recordings is 32.
```

---
### ResetExclusiveScenarioGroup

`RESET_EXCLUSIVE_SCENARIO_GROUP` · hash `0x4202BBCB8684563D` · jhash `0x17F9DFE8` · **Cliente**

```lua
ResetExclusiveScenarioGroup()
```
```c
void RESET_EXCLUSIVE_SCENARIO_GROUP();
```

**Devuelve:** `void`

---
### ResetScenarioGroupsEnabled

`RESET_SCENARIO_GROUPS_ENABLED` · hash `0xDD902D0349AFAD3A` · jhash `0xBF55025D` · **Cliente**

```lua
ResetScenarioGroupsEnabled()
```
```c
void RESET_SCENARIO_GROUPS_ENABLED();
```

**Devuelve:** `void`

---
### ResetScenarioTypesEnabled

`RESET_SCENARIO_TYPES_ENABLED` · hash `0x0D40EE2A7F2B2D6D` · jhash `0xF58FDEB4` · **Cliente**

```lua
ResetScenarioTypesEnabled()
```
```c
void RESET_SCENARIO_TYPES_ENABLED();
```

**Devuelve:** `void`

---
### SetAnimLooped

`SET_ANIM_LOOPED` · hash `0x70033C3CC29A1FF4` · jhash `0x095D61A4` · **Cliente**

```lua
SetAnimLooped(p0, p1, p2, p3)
```
```c
void SET_ANIM_LOOPED(Any p0, BOOL p1, Any p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`Any`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### SetAnimPhase

`SET_ANIM_PHASE` · hash `0xDDF3CB5A0A4C0B49` · jhash `0xB621E7E4` · **Cliente**

```lua
SetAnimPhase(entity, p1, p2, p3)
```
```c
void SET_ANIM_PHASE(Entity entity, float p1, Any p2, BOOL p3);
```

**Parámetros**

- `entity` (`Entity`)
- `p1` (`float`)
- `p2` (`Any`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xDDF3CB5A0A4C0B49` (`N_0xddf3cb5a0a4c0b49`), `_SET_ANIM_PLAYBACK_TIME` (`SetAnimPlaybackTime`)

---
### SetAnimRate

`SET_ANIM_RATE` · hash `0x032D49C5E359C847` · jhash `0x6DB46584` · **Cliente**

```lua
SetAnimRate(p0, p1, p2, p3)
```
```c
void SET_ANIM_RATE(Any p0, float p1, Any p2, BOOL p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`Any`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### SetAnimWeight

`SET_ANIM_WEIGHT` · hash `0x207F1A47C0342F48` · jhash `0x17229D98` · **Cliente**

```lua
SetAnimWeight(p0, p1, p2, p3, p4)
```
```c
void SET_ANIM_WEIGHT(Any p0, float p1, Any p2, Any p3, BOOL p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`BOOL`)

**Devuelve:** `void`

---
### SetDriveTaskCruiseSpeed

`SET_DRIVE_TASK_CRUISE_SPEED` · hash `0x5C9B84BD7D31D908` · jhash `0x3CEC07B1` · **Cliente**

```lua
SetDriveTaskCruiseSpeed(driver, cruiseSpeed)
```
```c
void SET_DRIVE_TASK_CRUISE_SPEED(Ped driver, float cruiseSpeed);
```

**Parámetros**

- `driver` (`Ped`)
- `cruiseSpeed` (`float`)

**Devuelve:** `void`

---
### SetDriveTaskDrivingStyle

`SET_DRIVE_TASK_DRIVING_STYLE` · hash `0xDACE1BE37D88AF67` · jhash `0x59C5FAD7` · **Cliente**

```lua
SetDriveTaskDrivingStyle(ped, drivingStyle)
```
```c
void SET_DRIVE_TASK_DRIVING_STYLE(Ped ped, int drivingStyle);
```

**Parámetros**

- `ped` (`Ped`): The ped to have their driving style set.
- `drivingStyle` (`int`): The driving style (see `eVehicleDrivingFlags`).

**Devuelve:** `void`

**Descripción oficial:**

Sets the driving style for a ped currently performing a driving task.

Each flag in the `eVehicleDrivingFlags` enum can be combined to create a driving style, with each enabling or disabling a specific driving behavior. The driving style can be set to one of the predefined driving styles, or a custom driving style can be created by combining the flags. This can be done by using the bitwise OR operator (`|`) to combine the flags or by adding the decimal values of the flags together.

```cpp
enum eVehicleDrivingFlags
{
  None = 0,
  StopForVehicles = 1,
  StopForPeds = 2,
  SwerveAroundAllVehicles = 4,
  SteerAroundStationaryVehicles = 8,
  SteerAroundPeds = 16,
  SteerAroundObjects = 32,
  DontSteerAroundPlayerPed = 64,
  StopAtTrafficLights = 128,
  GoOffRoadWhenAvoiding = 256,
  AllowGoingWrongWay = 512,
  Reverse = 1024,
  UseWanderFallbackInsteadOfStraightLine = 2048,
  AvoidRestrictedAreas = 4096,
  PreventBackgroundPathfinding = 8192,
  AdjustCruiseSpeedBasedOnRoadSpeed = 16384,
  UseShortCutLinks = 262144,
  ChangeLanesAroundObstructions = 524288,
  UseSwitchedOffNodes = 2097152,
  PreferNavmeshRoute = 4194304,
  PlaneTaxiMode = 8388608,
  ForceStraightLine = 16777216,
  UseStringPullingAtJunctions = 33554432,
  TryToAvoidHighways = 536870912,
  ForceJoinInRoadDirection = 1073741824,
  StopAtDestination = 2147483648,
  // StopForVehicles | StopForPeds | SteerAroundObjects | SteerAroundStationaryVehicles | StopAtTrafficLights | UseShortCutLinks | ChangeLanesAroundObstructions
  DrivingModeStopForVehicles = 786603,
  // StopForVehicles | StopForPeds | StopAtTrafficLights | UseShortCutLinks
  DrivingModeStopForVehiclesStrict = 262275,
  // SwerveAroundAllVehicles | SteerAroundObjects | UseShortCutLinks | ChangeLanesAroundObstructions | StopForVehicles
  DrivingModeAvoidVehicles = 786469,
  // SwerveAroundAllVehicles | SteerAroundObjects | UseShortCutLinks | ChangeLanesAroundObstructions
  DrivingModeAvoidVehiclesReckless = 786468,
  // StopForVehicles | SteerAroundStationaryVehicles | StopForPeds | SteerAroundObjects | UseShortCutLinks | ChangeLanesAroundObstructions
  DrivingModeStopForVehiclesIgnoreLights = 786475,
  // SwerveAroundAllVehicles | StopAtTrafficLights | SteerAroundObjects | UseShortCutLinks | ChangeLanesAroundObstructions | StopForVehicles
  DrivingModeAvoidVehiclesObeyLights = 786597,
  // SwerveAroundAllVehicles | StopAtTrafficLights | StopForPeds | SteerAroundObjects | UseShortCutLinks | ChangeLanesAroundObstructions | StopForVehicles
  DrivingModeAvoidVehiclesStopForPedsObeyLights = 786599,
}
```

**Ejemplo (lua):**

```lua
local vehicle_model = `adder`
RequestModel(vehicle_model)
repeat Wait(0) until HasModelLoaded(vehicle_model)

-- Player needs to be in a vehicle for this to work
local ped = PlayerPedId()
local coords = GetEntityCoords(ped) - GetEntityForwardVector(ped) * 15.0
local vehicle = CreateVehicle(vehicle_model, coords.x, coords.y, coords.z, GetEntityHeading(ped), true, false)
 -- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(vehicle_model)

local ped_model = `a_m_m_skater_01`
RequestModel(ped_model)
repeat Wait(0) until HasModelLoaded(ped_model)

local driver = CreatePedInsideVehicle(vehicle, 0, ped_model, -1, true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(ped_model)

TaskVehicleChase(driver, ped)
SetDriveTaskDrivingStyle(driver, 786468)
-- Driving Style: DrivingModeAvoidVehiclesReckless
SetPedKeepTask(driver, true)
```

---
### SetDriveTaskMaxCruiseSpeed

`SET_DRIVE_TASK_MAX_CRUISE_SPEED` · hash `0x404A5AA9B9F0B746` · jhash `0x7FDF6131` · **Cliente**

```lua
SetDriveTaskMaxCruiseSpeed(p0, p1)
```
```c
void SET_DRIVE_TASK_MAX_CRUISE_SPEED(Any p0, float p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)

**Devuelve:** `void`

---
### SetDrivebyTaskTarget

`SET_DRIVEBY_TASK_TARGET` · hash `0xE5B302114D8162EE` · jhash `0xDA6A6FC1` · **Cliente**

```lua
SetDrivebyTaskTarget(shootingPed, targetPed, targetVehicle, x, y, z)
```
```c
void SET_DRIVEBY_TASK_TARGET(Ped shootingPed, Ped targetPed, Vehicle targetVehicle, float x, float y, float z);
```

**Parámetros**

- `shootingPed` (`Ped`)
- `targetPed` (`Ped`)
- `targetVehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
For p1 & p2 (Ped, Vehicle). I could be wrong, as the only time this native is called in scripts is once and both are 0, but I assume this native will work like SET_MOUNTED_WEAPON_TARGET in which has the same exact amount of parameters and the 1st and last 3 parameters are right and the same for both natives.  
```

---
### SetExclusiveScenarioGroup

`SET_EXCLUSIVE_SCENARIO_GROUP` · hash `0x535E97E1F7FC0C6A` · jhash `0x59DB8F26` · **Cliente**

```lua
SetExclusiveScenarioGroup(scenarioGroup)
```
```c
void SET_EXCLUSIVE_SCENARIO_GROUP(char* scenarioGroup);
```

**Parámetros**

- `scenarioGroup` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Groups found in the scripts used with this native:  
"AMMUNATION",  
"QUARRY",  
"Triathlon_1",  
"Triathlon_2",  
"Triathlon_3"  
```

---
### SetGlobalMinBirdFlightHeight

`SET_GLOBAL_MIN_BIRD_FLIGHT_HEIGHT` · hash `0x6C6B148586F934F7` · jhash `0x2AFB14B8` · **Cliente**

```lua
SetGlobalMinBirdFlightHeight(height)
```
```c
void SET_GLOBAL_MIN_BIRD_FLIGHT_HEIGHT(float height);
```

**Parámetros**

- `height` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Birds will try to reach the given height.  
```

---
### SetHighFallTask

`SET_HIGH_FALL_TASK` · hash `0x8C825BDC7741D37C` · jhash `0xBBB26172` · **Cliente**

```lua
SetHighFallTask(ped, duration, p2, p3)
```
```c
void SET_HIGH_FALL_TASK(Ped ped, Any duration, Any p2, Any p3);
```

**Parámetros**

- `ped` (`Ped`)
- `duration` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### SetMountedWeaponTarget

`SET_MOUNTED_WEAPON_TARGET` · hash `0xCCD892192C6D2BB9` · jhash `0x98713C68` · **Cliente**

```lua
SetMountedWeaponTarget(shootingPed, targetPed, targetVehicle, x, y, z)
```
```c
void SET_MOUNTED_WEAPON_TARGET(Ped shootingPed, Ped targetPed, Vehicle targetVehicle, float x, float y, float z);
```

**Parámetros**

- `shootingPed` (`Ped`)
- `targetPed` (`Ped`)
- `targetVehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Note: Look in decompiled scripts and the times that p1 and p2 aren't 0. They are filled with vars. If you look through out that script what other natives those vars are used in, you can tell p1 is a ped and p2 is a vehicle. Which most likely means if you want the mounted weapon to target a ped set targetVehicle to 0 or vice-versa.  
```

```
NativeDB Added Parameter 7: Any p6
NativeDB Added Parameter 8: Any p7
```

---
### SetNextDesiredMoveState

`SET_NEXT_DESIRED_MOVE_STATE` · hash `0xF1B9F16E89E2C93A` · jhash `0x4E937D57` · **Cliente**

```lua
SetNextDesiredMoveState(p0)
```
```c
void SET_NEXT_DESIRED_MOVE_STATE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### SetParachuteTaskTarget

`SET_PARACHUTE_TASK_TARGET` · hash `0xC313379AF0FCEDA7` · jhash `0x6ED3AD81` · **Cliente**

```lua
SetParachuteTaskTarget(ped, x, y, z)
```
```c
void SET_PARACHUTE_TASK_TARGET(Ped ped, float x, float y, float z);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### SetParachuteTaskThrust

`SET_PARACHUTE_TASK_THRUST` · hash `0x0729BAC1B8C64317` · jhash `0xD07C8AAA` · **Cliente**

```lua
SetParachuteTaskThrust(ped, thrust)
```
```c
void SET_PARACHUTE_TASK_THRUST(Ped ped, float thrust);
```

**Parámetros**

- `ped` (`Ped`)
- `thrust` (`float`)

**Devuelve:** `void`

---
### SetPedCanPlayAmbientIdles

`SET_PED_CAN_PLAY_AMBIENT_IDLES` · hash `0x8FD89A6240813FD0` · jhash `0xB5AD044E` · **Cliente**

```lua
SetPedCanPlayAmbientIdles(ped, bBlockIdleClips, bRemoveIdleClipIfPlaying)
```
```c
void SET_PED_CAN_PLAY_AMBIENT_IDLES(Ped ped, BOOL bBlockIdleClips, BOOL bRemoveIdleClipIfPlaying);
```

**Parámetros**

- `ped` (`Ped`): Ped index.
- `bBlockIdleClips` (`BOOL`): If true, prevents a ped from playing an idle animation this frame.
- `bRemoveIdleClipIfPlaying` (`BOOL`): If true and the ped is playing an idle animation, the clip is stopped.

**Devuelve:** `void`

**Descripción oficial:**

Prevents a ped from playing ambient idle animations.

**Note:** This native must be called every frame.

**Nombres antiguos (alias):** `0x8FD89A6240813FD0` (`N_0x8fd89a6240813fd0`)

---
### SetPedDesiredMoveBlendRatio

`SET_PED_DESIRED_MOVE_BLEND_RATIO` · hash `0x1E982AC8716912C5` · jhash `0xC65FC712` · **Cliente**

```lua
SetPedDesiredMoveBlendRatio(ped, p1)
```
```c
void SET_PED_DESIRED_MOVE_BLEND_RATIO(Ped ped, float p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)

**Devuelve:** `void`

---
### SetPedPathAvoidFire

`SET_PED_PATH_AVOID_FIRE` · hash `0x4455517B28441E60` · jhash `0xDCC5B934` · **Cliente**

```lua
SetPedPathAvoidFire(ped, avoidFire)
```
```c
void SET_PED_PATH_AVOID_FIRE(Ped ped, BOOL avoidFire);
```

**Parámetros**

- `ped` (`Ped`)
- `avoidFire` (`BOOL`)

**Devuelve:** `void`

---
### SetPedPathCanDropFromHeight

`SET_PED_PATH_CAN_DROP_FROM_HEIGHT` · hash `0xE361C5C71C431A4F` · jhash `0x394B7AC9` · **Cliente**

```lua
SetPedPathCanDropFromHeight(ped, Toggle)
```
```c
void SET_PED_PATH_CAN_DROP_FROM_HEIGHT(Ped ped, BOOL Toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `Toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedPathCanUseClimbovers

`SET_PED_PATH_CAN_USE_CLIMBOVERS` · hash `0x8E06A6FE76C9EFF4` · jhash `0xB7B7D442` · **Cliente**

```lua
SetPedPathCanUseClimbovers(ped, Toggle)
```
```c
void SET_PED_PATH_CAN_USE_CLIMBOVERS(Ped ped, BOOL Toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `Toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedPathCanUseLadders

`SET_PED_PATH_CAN_USE_LADDERS` · hash `0x77A5B103C87F476E` · jhash `0x53A879EE` · **Cliente**

```lua
SetPedPathCanUseLadders(ped, Toggle)
```
```c
void SET_PED_PATH_CAN_USE_LADDERS(Ped ped, BOOL Toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `Toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedPathClimbCostModifier

`SET_PED_PATH_CLIMB_COST_MODIFIER` · hash `0x88E32DB8C1A4AA4B` · jhash `0x55E06443` · **Cliente**

```lua
SetPedPathClimbCostModifier(ped, modifier)
```
```c
void SET_PED_PATH_CLIMB_COST_MODIFIER(Ped ped, float modifier);
```

**Parámetros**

- `ped` (`Ped`)
- `modifier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Default modifier is 1.0, minimum is 0.0 and maximum is 10.0.
```

**Nombres antiguos (alias):** `0x88E32DB8C1A4AA4B` (`N_0x88e32db8c1a4aa4b`)

---
### SetPedPathMayEnterWater

`SET_PED_PATH_MAY_ENTER_WATER` · hash `0xF35425A4204367EC` · jhash `0x9C606EE3` · **Cliente**

```lua
SetPedPathMayEnterWater(ped, mayEnterWater)
```
```c
void SET_PED_PATH_MAY_ENTER_WATER(Ped ped, BOOL mayEnterWater);
```

**Parámetros**

- `ped` (`Ped`)
- `mayEnterWater` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `SET_PED_PATHS_WIDTH_PLANT` (`SetPedPathsWidthPlant`)

---
### SetPedPathPreferToAvoidWater

`SET_PED_PATH_PREFER_TO_AVOID_WATER` · hash `0x38FE1EC73743793C` · jhash `0x0EA39A29` · **Cliente**

```lua
SetPedPathPreferToAvoidWater(ped, avoidWater)
```
```c
void SET_PED_PATH_PREFER_TO_AVOID_WATER(Ped ped, BOOL avoidWater);
```

**Parámetros**

- `ped` (`Ped`)
- `avoidWater` (`BOOL`)

**Devuelve:** `void`

---
### SetPedWaypointRouteOffset

`SET_PED_WAYPOINT_ROUTE_OFFSET` · hash `0xED98E10B0AFCE4B4` · jhash `0xF867F747` · **Cliente**

```lua
local retval = SetPedWaypointRouteOffset(p0, p1, p2, p3)
```
```c
Any SET_PED_WAYPOINT_ROUTE_OFFSET(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `Any`

---
### SetScenarioGroupEnabled

`SET_SCENARIO_GROUP_ENABLED` · hash `0x02C8E5B49848664E` · jhash `0x116997B1` · **Cliente**

```lua
SetScenarioGroupEnabled(scenarioGroup, p1)
```
```c
void SET_SCENARIO_GROUP_ENABLED(char* scenarioGroup, BOOL p1);
```

**Parámetros**

- `scenarioGroup` (`char*`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Occurrences in the b617d scripts: pastebin.com/Tvg2PRHU  
```

---
### SetScenarioTypeEnabled

`SET_SCENARIO_TYPE_ENABLED` · hash `0xEB47EC4E34FB7EE1` · jhash `0xDB18E5DE` · **Cliente**

```lua
SetScenarioTypeEnabled(scenarioType, toggle)
```
```c
void SET_SCENARIO_TYPE_ENABLED(char* scenarioType, BOOL toggle);
```

**Parámetros**

- `scenarioType` (`char*`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
seems to enable/disable specific scenario-types from happening in the game world.
Here are some scenario types from the scripts:
"WORLD_MOUNTAIN_LION_REST"
"WORLD_MOUNTAIN_LION_WANDER"
"DRIVE"
"WORLD_VEHICLE_POLICE_BIKE"
"WORLD_VEHICLE_POLICE_CAR"
"WORLD_VEHICLE_POLICE_NEXT_TO_CAR"
"WORLD_VEHICLE_DRIVE_SOLO"
"WORLD_VEHICLE_BIKER"
"WORLD_VEHICLE_DRIVE_PASSENGERS"
"WORLD_VEHICLE_SALTON_DIRT_BIKE"
"WORLD_VEHICLE_BICYCLE_MOUNTAIN"
"PROP_HUMAN_SEAT_CHAIR"
"WORLD_VEHICLE_ATTRACTOR"
"WORLD_HUMAN_LEANING"
"WORLD_HUMAN_HANG_OUT_STREET"
"WORLD_HUMAN_DRINKING"
"WORLD_HUMAN_SMOKING"
"WORLD_HUMAN_GUARD_STAND"
"WORLD_HUMAN_CLIPBOARD"
"WORLD_HUMAN_HIKER"
"WORLD_VEHICLE_EMPTY"
"WORLD_VEHICLE_BIKE_OFF_ROAD_RACE"
"WORLD_HUMAN_PAPARAZZI"
"WORLD_VEHICLE_PARK_PERPENDICULAR_NOSE_IN"
"WORLD_VEHICLE_PARK_PARALLEL"
"WORLD_VEHICLE_CONSTRUCTION_SOLO"
"WORLD_VEHICLE_CONSTRUCTION_PASSENGERS"
"WORLD_VEHICLE_TRUCK_LOGS"
scenarioType could be the same as scenarioName, used in for example TASK::TASK_START_SCENARIO_AT_POSITION.
```

---
### SetSequenceToRepeat

`SET_SEQUENCE_TO_REPEAT` · hash `0x58C70CF3A41E4AE7` · jhash `0xCDDF1508` · **Cliente**

```lua
SetSequenceToRepeat(taskSequenceId, repeat)
```
```c
void SET_SEQUENCE_TO_REPEAT(int taskSequenceId, BOOL repeat);
```

**Parámetros**

- `taskSequenceId` (`int`)
- `repeat` (`BOOL`)

**Devuelve:** `void`

---
### SetTaskMoveNetworkSignalBool

`SET_TASK_MOVE_NETWORK_SIGNAL_BOOL` · hash `0xB0A6CFD2C69C1088` · jhash `0xF3538041` · **Cliente**

```lua
SetTaskMoveNetworkSignalBool(ped, signalName, value)
```
```c
void SET_TASK_MOVE_NETWORK_SIGNAL_BOOL(Ped ped, char* signalName, BOOL value);
```

**Parámetros**

- `ped` (`Ped`): The ped that's performing the task.
- `signalName` (`char*`): The property name.
- `value` (`BOOL`): The property value to set.

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB0A6CFD2C69C1088` (`N_0xb0a6cfd2c69c1088`), `_SET_TASK_PROPERTY_BOOL` (`SetTaskPropertyBool`)

---
### SetTaskMoveNetworkSignalFloat

`SET_TASK_MOVE_NETWORK_SIGNAL_FLOAT` · hash `0xD5BB4025AE449A4E` · jhash `0xA79BE783` · **Cliente**

```lua
SetTaskMoveNetworkSignalFloat(ped, signalName, value)
```
```c
void SET_TASK_MOVE_NETWORK_SIGNAL_FLOAT(Ped ped, char* signalName, float value);
```

**Parámetros**

- `ped` (`Ped`): The ped on which the task is playing.
- `signalName` (`char*`): The property name.
- `value` (`float`): The property value to set.

**Devuelve:** `void`

**Descripción oficial:**

```
p0 - PLAYER::PLAYER_PED_ID();
p1 - "Phase", "Wobble", "x_axis","y_axis","introphase","speed".
p2 - From what i can see it goes up to 1f (maybe).
-LcGamingHD
Example: TASK::_D5BB4025AE449A4E(PLAYER::PLAYER_PED_ID(), "Phase", 0.5);
```

**Nombres antiguos (alias):** `0xD5BB4025AE449A4E` (`N_0xd5bb4025ae449a4e`), `_SET_TASK_PROPERTY_FLOAT` (`SetTaskPropertyFloat`)

---
### SetTaskMoveNetworkSignalFloat_2

`_SET_TASK_MOVE_NETWORK_SIGNAL_FLOAT_2` · hash `0x373EF409B82697A3` · **Cliente**

```lua
SetTaskMoveNetworkSignalFloat_2(ped, signalName, value)
```
```c
void _SET_TASK_MOVE_NETWORK_SIGNAL_FLOAT_2(Ped ped, char* signalName, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `signalName` (`char*`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### SetTaskVehicleChaseBehaviorFlag

`SET_TASK_VEHICLE_CHASE_BEHAVIOR_FLAG` · hash `0xCC665AAC360D31E7` · jhash `0x2A83083F` · **Cliente**

```lua
SetTaskVehicleChaseBehaviorFlag(ped, flag, set)
```
```c
void SET_TASK_VEHICLE_CHASE_BEHAVIOR_FLAG(Ped ped, int flag, BOOL set);
```

**Parámetros**

- `ped` (`Ped`)
- `flag` (`int`)
- `set` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
* Flag 1: Aggressive ramming of suspect
* Flag 2: Ram attempts
* Flag 8: Medium-aggressive boxing tactic with a bit of PIT
* Flag 16: Ramming, seems to be slightly less aggressive than 1-2.
* Flag 32: Stay back from suspect, no tactical contact. Convoy-like.
```

---
### SetTaskVehicleChaseIdealPursuitDistance

`SET_TASK_VEHICLE_CHASE_IDEAL_PURSUIT_DISTANCE` · hash `0x639B642FACBE4EDD` · jhash `0x04FD3EE7` · **Cliente**

```lua
SetTaskVehicleChaseIdealPursuitDistance(ped, distance)
```
```c
void SET_TASK_VEHICLE_CHASE_IDEAL_PURSUIT_DISTANCE(Ped ped, float distance);
```

**Parámetros**

- `ped` (`Ped`)
- `distance` (`float`)

**Devuelve:** `void`

---
### StopAnimPlayback

`STOP_ANIM_PLAYBACK` · hash `0xEE08C992D238C5D1` · jhash `0xE5F16398` · **Cliente**

```lua
StopAnimPlayback(ped, p1, p2)
```
```c
void STOP_ANIM_PLAYBACK(Ped ped, int p1, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Looks like p1 may be a flag, still need to do some research, though.
```

---
### StopAnimTask

`STOP_ANIM_TASK` · hash `0x97FF36A1D40EA00A` · jhash `0x2B520A57` · **Cliente**

```lua
StopAnimTask(ped, animDictionary, animationName, animExitSpeed)
```
```c
void STOP_ANIM_TASK(Ped ped, char* animDictionary, char* animationName, float animExitSpeed);
```

**Parámetros**

- `ped` (`Ped`)
- `animDictionary` (`char*`)
- `animationName` (`char*`)
- `animExitSpeed` (`float`): Greater than `0.0`, higher is faster. Setting to `0.0` or using an integer, will cause animation lockout - requiring the animation to be played again or the player be killed.

**Devuelve:** `void`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### TaskAchieveHeading

`TASK_ACHIEVE_HEADING` · hash `0x93B93A37987F1F3D` · jhash `0x0A0E9B42` · **Cliente**

```lua
TaskAchieveHeading(ped, heading, timeout)
```
```c
void TASK_ACHIEVE_HEADING(Ped ped, float heading, int timeout);
```

**Parámetros**

- `ped` (`Ped`)
- `heading` (`float`)
- `timeout` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the specified ped achieve the specified heading.  
pedHandle: The handle of the ped to assign the task to.  
heading: The desired heading.  
timeout: The time, in milliseconds, to allow the task to complete. If the task times out, it is cancelled, and the ped will stay at the heading it managed to reach in the time.  
```

---
### TaskAgitatedAction

`_TASK_AGITATED_ACTION` · hash `0x19D1B791CB3670FE` · **Cliente**

```lua
TaskAgitatedAction(ped, ped2)
```
```c
void _TASK_AGITATED_ACTION(Ped ped, Ped ped2);
```

**Parámetros**

- `ped` (`Ped`)
- `ped2` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x19D1B791CB3670FE` (`N_0x19d1b791cb3670fe`)

---
### TaskAimGunAtCoord

`TASK_AIM_GUN_AT_COORD` · hash `0x6671F3EEC681BDA1` · jhash `0xFBF44AD3` · **Cliente**

```lua
TaskAimGunAtCoord(ped, x, y, z, time, bInstantBlendToAim, bPlayAimIntro)
```
```c
void TASK_AIM_GUN_AT_COORD(Ped ped, float x, float y, float z, int time, BOOL bInstantBlendToAim, BOOL bPlayAimIntro);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `time` (`int`)
- `bInstantBlendToAim` (`BOOL`)
- `bPlayAimIntro` (`BOOL`)

**Devuelve:** `void`

---
### TaskAimGunAtEntity

`TASK_AIM_GUN_AT_ENTITY` · hash `0x9B53BB6E8943AF53` · jhash `0xBE32B3B6` · **Cliente**

```lua
TaskAimGunAtEntity(ped, entity, duration, bInstantBlendToAim)
```
```c
void TASK_AIM_GUN_AT_ENTITY(Ped ped, Entity entity, int duration, BOOL bInstantBlendToAim);
```

**Parámetros**

- `ped` (`Ped`)
- `entity` (`Entity`)
- `duration` (`int`)
- `bInstantBlendToAim` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
duration: the amount of time in milliseconds to do the task.  -1 will keep the task going until either another task is applied, or CLEAR_ALL_TASKS() is called with the ped  
```

---
### TaskAimGunScripted

`TASK_AIM_GUN_SCRIPTED` · hash `0x7A192BE16D373D00` · jhash `0x9D296BCD` · **Cliente**

```lua
TaskAimGunScripted(ped, scriptTask, bDisableBlockingClip, bInstantBlendToAim)
```
```c
void TASK_AIM_GUN_SCRIPTED(Ped ped, Hash scriptTask, BOOL bDisableBlockingClip, BOOL bInstantBlendToAim);
```

**Parámetros**

- `ped` (`Ped`)
- `scriptTask` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `bDisableBlockingClip` (`BOOL`)
- `bInstantBlendToAim` (`BOOL`)

**Devuelve:** `void`

---
### TaskAimGunScriptedWithTarget

`TASK_AIM_GUN_SCRIPTED_WITH_TARGET` · hash `0x8605AF0DE8B3A5AC` · jhash `0xFD517CE3` · **Cliente**

```lua
TaskAimGunScriptedWithTarget(ped, targetPed, x, y, z, iGunTaskType, bDisableBlockingClip, bForceAim)
```
```c
void TASK_AIM_GUN_SCRIPTED_WITH_TARGET(Ped ped, Ped targetPed, float x, float y, float z, Hash iGunTaskType, BOOL bDisableBlockingClip, BOOL bForceAim);
```

**Parámetros**

- `ped` (`Ped`)
- `targetPed` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `iGunTaskType` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `bDisableBlockingClip` (`BOOL`)
- `bForceAim` (`BOOL`)

**Devuelve:** `void`

---
### TaskArrestPed

`TASK_ARREST_PED` · hash `0xF3B9A78A178572B1` · jhash `0xBC0F153D` · **Cliente**

```lua
TaskArrestPed(ped, target)
```
```c
void TASK_ARREST_PED(Ped ped, Ped target);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example from "me_amanda1.ysc.c4":
TASK::TASK_ARREST_PED(l_19F /* This is a Ped */ , PLAYER::PLAYER_PED_ID());
Example from "armenian1.ysc.c4":
if (!PED::IS_PED_INJURED(l_B18[0/*1*/])) {
    TASK::TASK_ARREST_PED(l_B18[0/*1*/], PLAYER::PLAYER_PED_ID());
}
I would love to have time to experiment to see if a player Ped can arrest another Ped. Might make for a good cop mod.
Looks like only the player can be arrested this way. Peds react and try to arrest you if you task them, but the player charater doesn't do anything if tasked to arrest another ped.
```

---
### TaskBoatMission

`TASK_BOAT_MISSION` · hash `0x15C86013127CE63F` · jhash `0x5865B031` · **Cliente**

```lua
TaskBoatMission(ped, boat, vehicleTarget, pedTarget, x, y, z, missionType, speed, drivingStyle, radius, missionFlags)
```
```c
void TASK_BOAT_MISSION(Ped ped, Vehicle boat, Vehicle vehicleTarget, Ped pedTarget, float x, float y, float z, int missionType, float speed, int drivingStyle, float radius, int missionFlags);
```

**Parámetros**

- `ped` (`Ped`): The ped to be tasked.
- `boat` (`Vehicle`): The boats' entity handle.
- `vehicleTarget` (`Vehicle`): The target vehicle (default is 0).
- `pedTarget` (`Ped`): The target ped (default is 0).
- `x` (`float`): The x coordinate of the target (default is 0.0f).
- `y` (`float`): The y coordinate of the target (default is 0.0f).
- `z` (`float`): The z coordinate of the target (default is 0.0f).
- `missionType` (`int`): The mission type (default is 0) (see [TaskVehicleMission](#taskvehiclemission)).
- `speed` (`float`): The speed in m/s (default is -1.0f).
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).
- `radius` (`float`): The radius of when the task will be completed (default is -1.0f).
- `missionFlags` (`int`): The mission flags (default is 0) (see `eBoatMissionFlags`).

**Devuelve:** `void`

**Descripción oficial:**

All parameters except ped and boat are optional, with `pedTarget`, `vehicleTarget`, `x`, `y`, `z` being dependent on `missionType` (ie. Attack/Flee mission types require a target ped/vehicle, whereas GoTo mission types require either `x`, `y`, `z` or a target ped/vehicle).

If you don't want to use a parameter; pass `0.0f` for `x`, `y` and `z`, `0` for `pedTarget`, `vehicleTarget` and other int parameters, and `-1.0f` for the remaining float parameters.

```cpp
enum eBoatMissionFlags
{
  None = 0,
  StopAtEnd = 1,
  StopAtShore = 2,
  AvoidShore = 4,
  PreferForward = 8,
  NeverStop = 16,
  NeverNavMesh = 32,
  NeverRoute = 64,
  ForceBeached = 128,
  UseWanderRoute = 256,
  UseFleeRoute = 512,
  NeverPause = 1024,
  // StopAtEnd | StopAtShore | AvoidShore
  DefaultSettings = 7,
  // StopAtEnd | StopAtShore | AvoidShore | PreferForward | NeverNavMesh | NeverRoute
  OpenOceanSettings = 111,
  // StopAtEnd | StopAtShore | AvoidShore | PreferForward | NeverNavMesh | NeverPause
  BoatTaxiSettings = 1071,
}
```

**Ejemplo (lua):**

```lua
local boat_model = `tropic`
RequestModel(boat_model)
repeat Wait(0) until HasModelLoaded(boat_model)

-- Player needs to be in open water & in a boat for this to work
local ped = PlayerPedId()
local coords = GetEntityCoords(ped) - GetEntityForwardVector(ped) * 15.0
local vehicle = CreateVehicle(boat_model, coords.x, coords.y, coords.z, GetEntityHeading(ped), true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(boat_model)

local ped_model = `a_m_m_skater_01`
RequestModel(ped_model)
repeat Wait(0) until HasModelLoaded(ped_model)

local driver = CreatePedInsideVehicle(vehicle, 0, ped_model, -1, true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(ped_model)

TaskBoatMission(driver, vehicle, GetVehiclePedIsIn(ped, false), 0, 0.0, 0.0, 0.0, 7, -1.0, 786468, -1.0, 1044)
-- Mission Type: Follow | Drive Style: DrivingModeAvoidVehiclesReckless | Mission Flags: AvoidShore | NeverStop | NeverPause
SetPedKeepTask(driver, true)
```

---
### TaskChatToPed

`TASK_CHAT_TO_PED` · hash `0x8C338E0263E4FD19` · jhash `0xA2BE1821` · **Cliente**

```lua
TaskChatToPed(ped, target, p2, p3, p4, p5, p6, p7)
```
```c
void TASK_CHAT_TO_PED(Ped ped, Ped target, Any p2, float p3, float p4, float p5, float p6, float p7);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)
- `p2` (`Any`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
p2 tend to be 16, 17 or 1  
p3 to p7 tend to be 0.0  
```

---
### TaskClearDefensiveArea

`TASK_CLEAR_DEFENSIVE_AREA` · hash `0x95A6C46A31D1917D` · jhash `0x7A05BF0D` · **Cliente**

```lua
TaskClearDefensiveArea(p0)
```
```c
void TASK_CLEAR_DEFENSIVE_AREA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### TaskClearLookAt

`TASK_CLEAR_LOOK_AT` · hash `0x0F804F1DB19B9689` · jhash `0x60EB4054` · **Cliente**

```lua
TaskClearLookAt(ped)
```
```c
void TASK_CLEAR_LOOK_AT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
Not clear what it actually does, but here's how script uses it -
if (OBJECT::HAS_PICKUP_BEEN_COLLECTED(...)
{
 if(ENTITY::DOES_ENTITY_EXIST(PLAYER::PLAYER_PED_ID()))
    {
     TASK::TASK_CLEAR_LOOK_AT(PLAYER::PLAYER_PED_ID());
  }
 ...
}
Another one where it doesn't "look" at current player -
TASK::TASK_PLAY_ANIM(l_3ED, "missheist_agency2aig_2", "look_at_phone_a", 1000.0, -2.0, -1, 48, v_2, 0, 0, 0);
PED::_2208438012482A1A(l_3ED, 0, 0);
TASK::TASK_CLEAR_LOOK_AT(l_3ED);
```

---
### TaskClimb

`TASK_CLIMB` · hash `0x89D9FCC2435112F1` · jhash `0x90847790` · **Cliente**

```lua
TaskClimb(ped, unused)
```
```c
void TASK_CLIMB(Ped ped, BOOL unused);
```

**Parámetros**

- `ped` (`Ped`)
- `unused` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Climbs or vaults the nearest thing.  
```

---
### TaskClimbLadder

`TASK_CLIMB_LADDER` · hash `0xB6C987F9285A3814` · jhash `0x35BB4EE0` · **Cliente**

```lua
TaskClimbLadder(ped, p1)
```
```c
void TASK_CLIMB_LADDER(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

---
### TaskCombatHatedTargetsAroundPed

`TASK_COMBAT_HATED_TARGETS_AROUND_PED` · hash `0x7BF835BB9E2698C8` · jhash `0x2E7064E4` · **Cliente**

```lua
TaskCombatHatedTargetsAroundPed(ped, radius, p2)
```
```c
void TASK_COMBAT_HATED_TARGETS_AROUND_PED(Ped ped, float radius, int p2);
```

**Parámetros**

- `ped` (`Ped`)
- `radius` (`float`)
- `p2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Despite its name, it only attacks ONE hated target. The one closest hated target.  
p2 seems to be always 0  
```

---
### TaskCombatHatedTargetsAroundPedTimed

`TASK_COMBAT_HATED_TARGETS_AROUND_PED_TIMED` · hash `0x2BBA30B854534A0C` · jhash `0xF127AD6A` · **Cliente**

```lua
TaskCombatHatedTargetsAroundPedTimed(p0, p1, p2, p3)
```
```c
void TASK_COMBAT_HATED_TARGETS_AROUND_PED_TIMED(Any p0, float p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### TaskCombatHatedTargetsInArea

`TASK_COMBAT_HATED_TARGETS_IN_AREA` · hash `0x4CF5F55DAC3280A0` · jhash `0xDF099E18` · **Cliente**

```lua
TaskCombatHatedTargetsInArea(ped, x, y, z, radius, p5)
```
```c
void TASK_COMBAT_HATED_TARGETS_IN_AREA(Ped ped, float x, float y, float z, float radius, Any p5);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
Despite its name, it only attacks ONE hated target. The one closest to the specified position.  
```

---
### TaskCombatPed

`TASK_COMBAT_PED` · hash `0xF166E48407BAC484` · jhash `0xCB0D8932` · **Cliente · también en el servidor (RPC)**

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

---
### TaskCombatPedTimed

`TASK_COMBAT_PED_TIMED` · hash `0x944F30DCB7096BDE` · jhash `0xF5CA2A45` · **Cliente**

```lua
TaskCombatPedTimed(p0, ped, p2, p3)
```
```c
void TASK_COMBAT_PED_TIMED(Any p0, Ped ped, int p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `ped` (`Ped`)
- `p2` (`int`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### TaskCower

`TASK_COWER` · hash `0x3EB1FE9E8E908E15` · jhash `0x9CF1C19B` · **Cliente**

```lua
TaskCower(ped, duration)
```
```c
void TASK_COWER(Ped ped, int duration);
```

**Parámetros**

- `ped` (`Ped`): Ped id.
- `duration` (`int`): Duration of the animation in ms. Set to -1 if you do not want a duration.

**Devuelve:** `void`

**Descripción oficial:**

The ped will act like NPC's involved in a gunfight. The ped will squat down with their heads held in place and look around.

---
### TaskDriveBy

`TASK_DRIVE_BY` · hash `0x2F8AF0E82773A171` · jhash `0x2B84D1C4` · **Cliente · también en el servidor (RPC)**

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

---
### TaskEnterVehicle

`TASK_ENTER_VEHICLE` · hash `0xC20E50AA46D09CA8` · jhash `0xB8689B4E` · **Cliente · también en el servidor (RPC)**

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
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](VEHICLE-1.md#isvehicleseatfree).
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

---
### TaskEveryoneLeaveVehicle

`TASK_EVERYONE_LEAVE_VEHICLE` · hash `0x7F93691AB4B92272` · jhash `0xC1971F30` · **Cliente · también en el servidor (RPC)**

```lua
TaskEveryoneLeaveVehicle(vehicle)
```
```c
void TASK_EVERYONE_LEAVE_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### TaskExitCover

`TASK_EXIT_COVER` · hash `0x79B258E397854D29` · jhash `0xC829FAC9` · **Cliente**

```lua
TaskExitCover(p0, p1, p2, p3, p4)
```
```c
void TASK_EXIT_COVER(Any p0, Any p1, float p2, float p3, float p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

---
### TaskExtendRoute

`TASK_EXTEND_ROUTE` · hash `0x1E7889778264843A` · jhash `0x43271F69` · **Cliente**

```lua
TaskExtendRoute(x, y, z)
```
```c
void TASK_EXTEND_ROUTE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Adds a new point to the current point route; a maximum of 8 points can be added.

Call [TASK_FLUSH_ROUTE](#taskflushroute) before the first call to this. Call [TASK_FOLLOW_POINT_ROUTE](#taskfollowpointroute) to make the Ped go the route.

---
### TaskFlushRoute

`TASK_FLUSH_ROUTE` · hash `0x841142A1376E9006` · jhash `0x34219154` · **Cliente**

```lua
TaskFlushRoute()
```
```c
void TASK_FLUSH_ROUTE();
```

**Devuelve:** `void`

**Descripción oficial:**

Clears the current point route. Call this before [TASK_EXTEND_ROUTE](#taskextendroute) and [TASK_FOLLOW_POINT_ROUTE](#taskfollowpointroute).

---
### TaskFollowNavMeshToCoord

`TASK_FOLLOW_NAV_MESH_TO_COORD` · hash `0x15D3A79D4E44B913` · jhash `0xFE4A10D9` · **Cliente**

```lua
TaskFollowNavMeshToCoord(ped, x, y, z, moveBlendRatio, time, radius, flags, finalHeading)
```
```c
void TASK_FOLLOW_NAV_MESH_TO_COORD(Ped ped, float x, float y, float z, float moveBlendRatio, int time, float radius, int flags, float finalHeading);
```

**Parámetros**

- `ped` (`Ped`): Ped Index.
- `x` (`float`): X Position Coordinate.
- `y` (`float`): Y Position Coordinate.
- `z` (`float`): Z Position Coordinate
- `moveBlendRatio` (`float`): Ratio for ped movement (0 to 3.0 in the following order: still, walk, run and sprint)
- `time` (`int`): INT value in milliseconds.
- `radius` (`float`): distance from the final coordinates that the pedestrian should be to consider itself at the target.
- `flags` (`int`): Navigation Flags for the ped (see `eNavScriptFlags`).
- `finalHeading` (`float`): Peds heading when finished.

**Devuelve:** `void`

**Descripción oficial:**

Sometimes a path may not be able to be found. This could happen because there simply isn't any way to get there, or maybe a bunch of dynamic objects have blocked the way,
or maybe the destination is too far away. In this case the ped will simply stand still.
To identify when this has happened, you can use GET_NAVMESH_ROUTE_RESULT. This will help you find situations where peds cannot get to their target.

```cpp
enum eNavScriptFlags {
    // Default flag
    ENAV_DEFAULT = 0,
    // Will ensure the ped continues to move whilst waiting for the path
    // to be found, and will not slow down at the end of their route.
    ENAV_NO_STOPPING = 1,
    // Performs a slide-to-coord at the end of the task. This requires that the
    // accompanying NAVDATA structure has the 'SlideToCoordHeading' member set correctly.
    ENAV_ADV_SLIDE_TO_COORD_AND_ACHIEVE_HEADING_AT_END = 2,
    // If the navmesh is not loaded in under the target position, then this will
    // cause the ped to get as close as is possible on whatever navmesh is loaded.
    // The navmesh must still be loaded at the path start.
    ENAV_GO_FAR_AS_POSSIBLE_IF_TARGET_NAVMESH_NOT_LOADED = 4,
    // Will allow navigation underwater - by default this is not allowed.
    ENAV_ALLOW_SWIMMING_UNDERWATER = 8,
    // Will only allow navigation on pavements. If the path starts or ends off
    // the pavement, the command will fail. Likewise if no pavement-only route
    // can be found even although the start and end are on pavement.
    ENAV_KEEP_TO_PAVEMENTS = 16,
    // Prevents the path from entering water at all.
    ENAV_NEVER_ENTER_WATER = 32,
    // Disables object-avoidance for this path. The ped may still make minor
    // steering adjustments to avoid objects, but will not pathfind around them.
    ENAV_DONT_AVOID_OBJECTS = 64,
    // Specifies that the navmesh route will only be able to traverse up slopes
    // which are under the angle specified, in the MaxSlopeNavigable member of the accompanying NAVDATA structure.
    ENAV_ADVANCED_USE_MAX_SLOPE_NAVIGABLE = 128,
    // Unused.
    ENAV_STOP_EXACTLY = 512,
    // The entity will look ahead in its path for a longer distance to make the
    // walk/run start go more in the right direction.
    ENAV_ACCURATE_WALKRUN_START = 1024,
    // Disables ped-avoidance for this path while we move.
    ENAV_DONT_AVOID_PEDS = 2048,
    // If target pos is inside the boundingbox of an object it will otherwise be pushed out.
    ENAV_DONT_ADJUST_TARGET_POSITION = 4096,
    // Turns off the default behaviour, which is to stop exactly at the target position.
    // Occasionally this can cause footsliding/skating problems.
    ENAV_SUPPRESS_EXACT_STOP = 8192,
    // Prevents the path-search from finding paths outside of this search distance.
    // This can be used to prevent peds from finding long undesired routes.
    ENAV_ADVANCED_USE_CLAMP_MAX_SEARCH_DISTANCE = 16384,
    // Pulls out the paths from edges at corners for a longer distance, to prevent peds walking into stuff.
    ENAV_PULL_FROM_EDGE_EXTRA = 32768
};
```

---
### TaskFollowNavMeshToCoordAdvanced

`TASK_FOLLOW_NAV_MESH_TO_COORD_ADVANCED` · hash `0x17F58B88D085DBAC` · jhash `0x6BF6E296` · **Cliente**

```lua
TaskFollowNavMeshToCoordAdvanced(ped, x, y, z, speed, timeout, unkFloat, unkInt, unkX, unkY, unkZ, unk_40000f)
```
```c
void TASK_FOLLOW_NAV_MESH_TO_COORD_ADVANCED(Ped ped, float x, float y, float z, float speed, int timeout, float unkFloat, int unkInt, float unkX, float unkY, float unkZ, float unk_40000f);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `speed` (`float`)
- `timeout` (`int`)
- `unkFloat` (`float`)
- `unkInt` (`int`)
- `unkX` (`float`)
- `unkY` (`float`)
- `unkZ` (`float`)
- `unk_40000f` (`float`)

**Devuelve:** `void`

---
### TaskFollowPointRoute

`TASK_FOLLOW_POINT_ROUTE` · hash `0x595583281858626E` · jhash `0xB837C816` · **Cliente**

```lua
TaskFollowPointRoute(ped, speed, routeMode)
```
```c
void TASK_FOLLOW_POINT_ROUTE(Ped ped, float speed, int routeMode);
```

**Parámetros**

- `ped` (`Ped`): The ped to give the task to.
- `speed` (`float`): The speed to move at in m/s.
- `routeMode` (`int`): The route mode to use, refer to `eFollowPointRouteMode`

**Devuelve:** `void`

**Descripción oficial:**

Makes the ped go on a point route.

```cpp
enum eFollowPointRouteMode {
	TICKET_SINGLE = 0,
	TICKET_RETURN = 1,
	TICKET_SEASON = 2,
	TICKET_LOOP = 3
}
```

This native is often times used with [`TASK_FLUSH_ROUTE`](#taskflushroute) and [`TASK_EXTEND_ROUTE`](#taskextendroute)

**Ejemplo (lua):**

```lua
TaskFlushRoute()
TaskExtendRoute(0.0, 0.0, 70.0)
TaskExtendRoute(10.0, 0.0, 70.0)
TaskExtendRoute(10.0, 10.0, 70.0)
TaskFollowPointRoute(PlayerPedId(), 1.0, 0)
```

---
### TaskFollowToOffsetOfEntity

`TASK_FOLLOW_TO_OFFSET_OF_ENTITY` · hash `0x304AE42E357B8C7E` · jhash `0x2DF5A6AC` · **Cliente**

```lua
TaskFollowToOffsetOfEntity(ped, entity, offsetX, offsetY, offsetZ, movementSpeed, timeout, stoppingRange, persistFollowing)
```
```c
void TASK_FOLLOW_TO_OFFSET_OF_ENTITY(Ped ped, Entity entity, float offsetX, float offsetY, float offsetZ, float movementSpeed, int timeout, float stoppingRange, BOOL persistFollowing);
```

**Parámetros**

- `ped` (`Ped`)
- `entity` (`Entity`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)
- `movementSpeed` (`float`)
- `timeout` (`int`)
- `stoppingRange` (`float`)
- `persistFollowing` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p6 always -1  
p7 always 10.0  
p8 always 1  
```

---
### TaskFollowWaypointRecording

`TASK_FOLLOW_WAYPOINT_RECORDING` · hash `0x0759591819534F7B` · jhash `0xADF9904D` · **Cliente**

```lua
TaskFollowWaypointRecording(p0, p1, p2, p3, p4)
```
```c
void TASK_FOLLOW_WAYPOINT_RECORDING(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### TaskForceMotionState

`TASK_FORCE_MOTION_STATE` · hash `0x4F056E1AFFEF17AB` · jhash `0xCAD2EF77` · **Cliente**

```lua
TaskForceMotionState(ped, state, p2)
```
```c
void TASK_FORCE_MOTION_STATE(Ped ped, Hash state, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `state` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

See [`FORCE_PED_MOTION_STATE`](PED-1.md#forcepedmotionstate)

---
### TaskGetOffBoat

`TASK_GET_OFF_BOAT` · hash `0x9C00E77AF14B2DFF` · jhash `0x4293601F` · **Cliente**

```lua
TaskGetOffBoat(ped, boat)
```
```c
void TASK_GET_OFF_BOAT(Ped ped, Vehicle boat);
```

**Parámetros**

- `ped` (`Ped`)
- `boat` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_TASK_GET_OFF_BOAT` (`TaskGetOffBoat`)

---
### TaskGoStraightToCoord

`TASK_GO_STRAIGHT_TO_COORD` · hash `0xD76B57B44F1E6F8B` · jhash `0x80A9E7A7` · **Cliente · también en el servidor (RPC)**

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

---
### TaskGoStraightToCoordRelativeToEntity

`TASK_GO_STRAIGHT_TO_COORD_RELATIVE_TO_ENTITY` · hash `0x61E360B7E040D12E` · jhash `0xD26CAC68` · **Cliente**

```lua
TaskGoStraightToCoordRelativeToEntity(entity1, entity2, p2, p3, p4, p5, p6)
```
```c
void TASK_GO_STRAIGHT_TO_COORD_RELATIVE_TO_ENTITY(Entity entity1, Entity entity2, float p2, float p3, float p4, float p5, Any p6);
```

**Parámetros**

- `entity1` (`Entity`)
- `entity2` (`Entity`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### TaskGoToCoordAndAimAtHatedEntitiesNearCoord

`TASK_GO_TO_COORD_AND_AIM_AT_HATED_ENTITIES_NEAR_COORD` · hash `0xA55547801EB331FC` · jhash `0x3F91358E` · **Cliente**

```lua
TaskGoToCoordAndAimAtHatedEntitiesNearCoord(pedHandle, goToLocationX, goToLocationY, goToLocationZ, focusLocationX, focusLocationY, focusLocationZ, speed, shootAtEnemies, distanceToStopAt, noRoadsDistance, unkTrue, unkFlag, aimingFlag, firingPattern)
```
```c
void TASK_GO_TO_COORD_AND_AIM_AT_HATED_ENTITIES_NEAR_COORD(Ped pedHandle, float goToLocationX, float goToLocationY, float goToLocationZ, float focusLocationX, float focusLocationY, float focusLocationZ, float speed, BOOL shootAtEnemies, float distanceToStopAt, float noRoadsDistance, BOOL unkTrue, int unkFlag, int aimingFlag, Hash firingPattern);
```

**Parámetros**

- `pedHandle` (`Ped`)
- `goToLocationX` (`float`)
- `goToLocationY` (`float`)
- `goToLocationZ` (`float`)
- `focusLocationX` (`float`)
- `focusLocationY` (`float`)
- `focusLocationZ` (`float`)
- `speed` (`float`)
- `shootAtEnemies` (`BOOL`)
- `distanceToStopAt` (`float`)
- `noRoadsDistance` (`float`)
- `unkTrue` (`BOOL`)
- `unkFlag` (`int`)
- `aimingFlag` (`int`)
- `firingPattern` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
The ped will walk or run towards goToLocation, aiming towards goToLocation or focusLocation (depending on the aimingFlag) and shooting if shootAtEnemies = true to any enemy in his path.
If the ped is closer than noRoadsDistance, the ped will ignore pathing/navmesh and go towards goToLocation directly. This could cause the ped to get stuck behind tall walls if the goToLocation is on the other side. To avoid this, use 0.0f and the ped will always use pathing/navmesh to reach his destination.
If the speed is set to 0.0f, the ped will just stand there while aiming, if set to 1.0f he will walk while aiming, 2.0f will run while aiming.
The ped will stop aiming when he is closer than distanceToStopAt to goToLocation.
I still can't figure out what unkTrue is used for. I don't notice any difference if I set it to false but in the decompiled scripts is always true.
I think that unkFlag, like the driving styles, could be a flag that "work as a list of 32 bits converted to a decimal integer. Each bit acts as a flag, and enables or disables a function". What leads me to this conclusion is the fact that in the decompiled scripts, unkFlag takes values like: 0, 1, 5 (101 in binary) and 4097 (4096 + 1 or 1000000000001 in binary). For now, I don't know what behavior enable or disable this possible flag so I leave it at 0.
Note: After some testing, using unkFlag = 16 (0x10) enables the use of sidewalks while moving towards goToLocation.
The aimingFlag takes 2 values: 0 to aim at the focusLocation, 1 to aim at where the ped is heading (goToLocation).
Example:
enum AimFlag
{
   AimAtFocusLocation,
   AimAtGoToLocation
};
Vector3 goToLocation1 = { 996.2867f, 0, -2143.044f, 0, 28.4763f, 0 }; // remember the padding.
Vector3 goToLocation2 = { 990.2867f, 0, -2140.044f, 0, 28.4763f, 0 }; // remember the padding.
Vector3 focusLocation = { 994.3478f, 0, -2136.118f, 0, 29.2463f, 0 }; // the coord z should be a little higher, around +1.0f to avoid aiming at the ground
// 1st example
TASK::TASK_GO_TO_COORD_AND_AIM_AT_HATED_ENTITIES_NEAR_COORD(pedHandle, goToLocation1.x, goToLocation1.y, goToLocation1.z, focusLocation.x, focusLocation.y, focusLocation.z, 2.0f /*run*/, true /*shoot*/, 3.0f /*stop at*/, 0.0f /*noRoadsDistance*/, true /*always true*/, 0 /*possible flag*/, AimFlag::AimAtGoToLocation, -957453492 /*FullAuto pattern*/);
// 2nd example
TASK::TASK_GO_TO_COORD_AND_AIM_AT_HATED_ENTITIES_NEAR_COORD(pedHandle, goToLocation2.x, goToLocation2.y, goToLocation2.z, focusLocation.x, focusLocation.y, focusLocation.z, 1.0f /*walk*/, false /*don't shoot*/, 3.0f /*stop at*/, 0.0f /*noRoadsDistance*/, true /*always true*/, 0 /*possible flag*/, AimFlag::AimAtFocusLocation, -957453492 /*FullAuto pattern*/);
1st example: The ped (pedhandle) will run towards goToLocation1. While running and aiming towards goToLocation1, the ped will shoot on sight to any enemy in his path, using "FullAuto" firing pattern. The ped will stop once he is closer than distanceToStopAt to goToLocation1.
2nd example: The ped will walk towards goToLocation2. This time, while walking towards goToLocation2 and aiming at focusLocation, the ped will point his weapon on sight to any enemy in his path without shooting. The ped will stop once he is closer than distanceToStopAt to goToLocation2.
```

---
### TaskGoToCoordAnyMeans

`TASK_GO_TO_COORD_ANY_MEANS` · hash `0x5BC448CB78FA3E88` · jhash `0xF91DF93B` · **Cliente · también en el servidor (RPC)**

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

---
### TaskGoToCoordAnyMeansExtraParams

`TASK_GO_TO_COORD_ANY_MEANS_EXTRA_PARAMS` · hash `0x1DD45F9ECFDB1BC9` · jhash `0x094B75EF` · **Cliente**

```lua
TaskGoToCoordAnyMeansExtraParams(ped, x, y, z, speed, p5, p6, walkingStyle, p8, p9, p10, p11)
```
```c
void TASK_GO_TO_COORD_ANY_MEANS_EXTRA_PARAMS(Ped ped, float x, float y, float z, float speed, Any p5, BOOL p6, int walkingStyle, float p8, Any p9, Any p10, Any p11);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `speed` (`float`)
- `p5` (`Any`)
- `p6` (`BOOL`)
- `walkingStyle` (`int`)
- `p8` (`float`)
- `p9` (`Any`)
- `p10` (`Any`)
- `p11` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 13: Any p12
```

---
### TaskGoToCoordAnyMeansExtraParamsWithCruiseSpeed

`TASK_GO_TO_COORD_ANY_MEANS_EXTRA_PARAMS_WITH_CRUISE_SPEED` · hash `0xB8ECD61F531A7B02` · jhash `0x86DC03F9` · **Cliente**

```lua
TaskGoToCoordAnyMeansExtraParamsWithCruiseSpeed(ped, x, y, z, speed, p5, p6, walkingStyle, p8, p9, p10, p11, p12)
```
```c
void TASK_GO_TO_COORD_ANY_MEANS_EXTRA_PARAMS_WITH_CRUISE_SPEED(Ped ped, float x, float y, float z, float speed, Any p5, BOOL p6, int walkingStyle, float p8, Any p9, Any p10, Any p11, Any p12);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `speed` (`float`)
- `p5` (`Any`)
- `p6` (`BOOL`)
- `walkingStyle` (`int`)
- `p8` (`float`)
- `p9` (`Any`)
- `p10` (`Any`)
- `p11` (`Any`)
- `p12` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 14: Any p13
```

---
### TaskGoToCoordWhileAimingAtCoord

`TASK_GO_TO_COORD_WHILE_AIMING_AT_COORD` · hash `0x11315AB3385B8AC0` · jhash `0x1552DC91` · **Cliente**

```lua
TaskGoToCoordWhileAimingAtCoord(ped, x, y, z, aimAtX, aimAtY, aimAtZ, moveSpeed, shoot, p9, p10, p11, flags, p13, firingPattern)
```
```c
void TASK_GO_TO_COORD_WHILE_AIMING_AT_COORD(Ped ped, float x, float y, float z, float aimAtX, float aimAtY, float aimAtZ, float moveSpeed, BOOL shoot, float p9, float p10, BOOL p11, Any flags, BOOL p13, Hash firingPattern);
```

**Parámetros**

- `ped` (`Ped`): Ped to task
- `x` (`float`): Destination X position
- `y` (`float`): Destination Y position
- `z` (`float`): Destination Z position
- `aimAtX` (`float`): Aim at target x position
- `aimAtY` (`float`): Aim at target Y position
- `aimAtZ` (`float`): Aim at target Z position
- `moveSpeed` (`float`): mostly 2f, but also 1/1.2f, etc.
- `shoot` (`BOOL`): If true ped will shoot; false - will not
- `p9` (`float`): Usually 2.0f
- `p10` (`float`): Usually 0.5f
- `p11` (`BOOL`): If true ped will stay still; false - will not
- `flags` (`Any`): 0 / 512 / 513, etc
- `p13` (`BOOL`)
- `firingPattern` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: ${firing_pattern_full_auto}, 0xC6EE6B4C

**Devuelve:** `void`

**Descripción oficial:**

Will make the ped move to a coordinate while aiming (and optionally shooting) at given coordinates.

---
### TaskGoToCoordWhileAimingAtEntity

`TASK_GO_TO_COORD_WHILE_AIMING_AT_ENTITY` · hash `0xB2A16444EAD9AE47` · jhash `0x9BD52ABD` · **Cliente**

```lua
TaskGoToCoordWhileAimingAtEntity(ped, x, y, z, entityToAimAt, moveSpeed, shoot, targetRadius, slowDistance, useNavMesh, navFlags, instantBlendAtAim, firingPattern, time)
```
```c
void TASK_GO_TO_COORD_WHILE_AIMING_AT_ENTITY(Ped ped, float x, float y, float z, Entity entityToAimAt, float moveSpeed, BOOL shoot, float targetRadius, float slowDistance, BOOL useNavMesh, int navFlags, BOOL instantBlendAtAim, Hash firingPattern, int time);
```

**Parámetros**

- `ped` (`Ped`): Ped to task
- `x` (`float`): Destination X position
- `y` (`float`): Destination Y position
- `z` (`float`): Destination Z position
- `entityToAimAt` (`Entity`): Entity that the ped will aim at.
- `moveSpeed` (`float`): Mostly 2f, but also 1/1.2f, etc.
- `shoot` (`BOOL`): If true ped will shoot; false - will not
- `targetRadius` (`float`): Usually 0.5f
- `slowDistance` (`float`): Usually 4f
- `useNavMesh` (`BOOL`)
- `navFlags` (`int`): Usually 0 or 64
- `instantBlendAtAim` (`BOOL`)
- `firingPattern` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The firing pattern to use, refer to `eFiringPatternHashes`
- `time` (`int`): Usually 20000 (ms)

**Devuelve:** `void`

**Descripción oficial:**

Will make the ped move to a coordinate while aiming (and optionally shooting) at the given entity.

```cpp
enum eFiringPatternHashes {
    FIRING_PATTERN_DEFAULT = 0,
    FIRING_PATTERN_BURST_FIRE = -687903391,
    FIRING_PATTERN_BURST_FIRE_DRIVEBY = -753768974,
    FIRING_PATTERN_FULL_AUTO = -957453492,
    FIRING_PATTERN_SINGLE_SHOT = 1566631136,
    FIRING_PATTERN_DELAY_FIRE_BY_ONE_SEC = 2055493265,
    FIRING_PATTERN_BURST_FIRE_HELI = -1857128337,
    FIRING_PATTERN_SHORT_BURSTS = 445831135,
    FIRING_PATTERN_BURST_FIRE_MICRO = 1122960381,
    FIRING_PATTERN_SLOW_FIRE_TANK = -490063247,
    FIRING_PATTERN_TAMPA_MORTAR = -1842093953
}
```

---
### TaskGoToEntity

`TASK_GO_TO_ENTITY` · hash `0x6A071245EB0D1882` · jhash `0x374827C2` · **Cliente · también en el servidor (RPC)**

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

---
### TaskGoToEntityWhileAimingAtCoord

`TASK_GO_TO_ENTITY_WHILE_AIMING_AT_COORD` · hash `0x04701832B739DCE5` · jhash `0xD896CD82` · **Cliente**

```lua
TaskGoToEntityWhileAimingAtCoord(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
```
```c
void TASK_GO_TO_ENTITY_WHILE_AIMING_AT_COORD(Any p0, Any p1, float p2, float p3, float p4, float p5, BOOL p6, float p7, float p8, BOOL p9, BOOL p10, Any p11);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`BOOL`)
- `p7` (`float`)
- `p8` (`float`)
- `p9` (`BOOL`)
- `p10` (`BOOL`)
- `p11` (`Any`)

**Devuelve:** `void`

---
### TaskGoToEntityWhileAimingAtEntity

`TASK_GO_TO_ENTITY_WHILE_AIMING_AT_ENTITY` · hash `0x97465886D35210E9` · jhash `0x68E36B7A` · **Cliente**

```lua
TaskGoToEntityWhileAimingAtEntity(ped, entityToWalkTo, entityToAimAt, speed, shootatEntity, p5, p6, p7, p8, firingPattern)
```
```c
void TASK_GO_TO_ENTITY_WHILE_AIMING_AT_ENTITY(Ped ped, Entity entityToWalkTo, Entity entityToAimAt, float speed, BOOL shootatEntity, float p5, float p6, BOOL p7, BOOL p8, Hash firingPattern);
```

**Parámetros**

- `ped` (`Ped`)
- `entityToWalkTo` (`Entity`)
- `entityToAimAt` (`Entity`)
- `speed` (`float`)
- `shootatEntity` (`BOOL`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)
- `firingPattern` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
shootatEntity:  
If true, peds will shoot at Entity till it is dead.  
If false, peds will just walk till they reach the entity and will cease shooting.  
```

---
### TaskGotoEntityAiming

`TASK_GOTO_ENTITY_AIMING` · hash `0xA9DA48FAB8A76C12` · jhash `0xF1C493CF` · **Cliente**

```lua
TaskGotoEntityAiming(ped, target, distanceToStopAt, StartAimingDist)
```
```c
void TASK_GOTO_ENTITY_AIMING(Ped ped, Entity target, float distanceToStopAt, float StartAimingDist);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Entity`)
- `distanceToStopAt` (`float`)
- `StartAimingDist` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
eg
 TASK::TASK_GOTO_ENTITY_AIMING(v_2, PLAYER::PLAYER_PED_ID(), 5.0, 25.0);
ped = Ped you want to perform this task.
target = the Entity they should aim at.
distanceToStopAt = distance from the target, where the ped should stop to aim.
StartAimingDist = distance where the ped should start to aim.
```

---
### TaskGotoEntityOffset

`TASK_GOTO_ENTITY_OFFSET` · hash `0xE39B4FF4FDEBDE27` · jhash `0x1A17A85E` · **Cliente**

```lua
TaskGotoEntityOffset(ped, entity, duration, seekRadius, seekAngleDeg, moveBlendRatio, gotoEntityOffsetFlags)
```
```c
void TASK_GOTO_ENTITY_OFFSET(Ped ped, Entity entity, int duration, float seekRadius, float seekAngleDeg, float moveBlendRatio, int gotoEntityOffsetFlags);
```

**Parámetros**

- `ped` (`Ped`): The ped handle
- `entity` (`Entity`): The target entity handle
- `duration` (`int`): The duration in seconds or -1 for forever
- `seekRadius` (`float`): How many meters the destination is from the entity
- `seekAngleDeg` (`float`): The angle the destination is from the entity
- `moveBlendRatio` (`float`): The move blend ratio (speed)
- `gotoEntityOffsetFlags` (`int`): The goto entity offset flags

**Devuelve:** `void`

**Descripción oficial:**

Instructs the ped to go to the entity with the given offset.

```cpp
enum eSeekEntityOffsetFlags {
    ESEEK_OFFSET_ORIENTATES_WITH_ENTITY = 1,
    ESEEK_KEEP_TO_PAVEMENTS = 2
};
```

---
### TaskGotoEntityOffsetXy

`TASK_GOTO_ENTITY_OFFSET_XY` · hash `0x338E7EF52B6095A9` · jhash `0xBC1E3D0A` · **Cliente**

```lua
TaskGotoEntityOffsetXy(ped, entity, duration, targetRadius, offsetX, offsetY, moveBlendRatio, gotoEntityOffsetFlags)
```
```c
void TASK_GOTO_ENTITY_OFFSET_XY(Ped ped, Entity entity, int duration, float targetRadius, float offsetX, float offsetY, float moveBlendRatio, int gotoEntityOffsetFlags);
```

**Parámetros**

- `ped` (`Ped`): The ped handle
- `entity` (`Entity`): The target entity handle
- `duration` (`int`): The duration in seconds or -1 for forever
- `targetRadius` (`float`): How far away the ped needs to be from the target entity before it starts moving
- `offsetX` (`float`): The X offset
- `offsetY` (`float`): The Y offset
- `moveBlendRatio` (`float`): The move blend ratio (speed)
- `gotoEntityOffsetFlags` (`int`): The goto entity offset flags (see [`TASK_GOTO_ENTITY_OFFSET`](#taskgotoentityoffset))

**Devuelve:** `void`

**Descripción oficial:**

Instructs the ped to go to the entity with the given offset.

---
### TaskGuardAssignedDefensiveArea

`TASK_GUARD_ASSIGNED_DEFENSIVE_AREA` · hash `0xD2A207EEBDF9889B` · jhash `0x7AF0133D` · **Cliente**

```lua
TaskGuardAssignedDefensiveArea(p0, p1, p2, p3, p4, p5, p6)
```
```c
void TASK_GUARD_ASSIGNED_DEFENSIVE_AREA(Any p0, float p1, float p2, float p3, float p4, float p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### TaskGuardCurrentPosition

`TASK_GUARD_CURRENT_POSITION` · hash `0x4A58A47A72E3FCB4` · jhash `0x2FB099E9` · **Cliente**

```lua
TaskGuardCurrentPosition(p0, p1, p2, p3)
```
```c
void TASK_GUARD_CURRENT_POSITION(Ped p0, float p1, float p2, BOOL p3);
```

**Parámetros**

- `p0` (`Ped`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
From re_prisonvanbreak:
TASK::TASK_GUARD_CURRENT_POSITION(l_DD, 35.0, 35.0, 1);
```

---
### TaskGuardSphereDefensiveArea

`TASK_GUARD_SPHERE_DEFENSIVE_AREA` · hash `0xC946FE14BE0EB5E2` · jhash `0x86B76CB7` · **Cliente**

```lua
TaskGuardSphereDefensiveArea(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10)
```
```c
void TASK_GUARD_SPHERE_DEFENSIVE_AREA(Ped p0, float p1, float p2, float p3, float p4, float p5, Any p6, float p7, float p8, float p9, float p10);
```

**Parámetros**

- `p0` (`Ped`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`Any`)
- `p7` (`float`)
- `p8` (`float`)
- `p9` (`float`)
- `p10` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
p0 - Guessing PedID  
p1, p2, p3 - XYZ?  
p4 - ???  
p5 - Maybe the size of sphere from XYZ?  
p6 - ???  
p7, p8, p9 - XYZ again?  
p10 - Maybe the size of sphere from second XYZ?  
```

---
### TaskHandsUp

`TASK_HANDS_UP` · hash `0xF2EAB31979A7F910` · jhash `0x8DCC19C5` · **Cliente · también en el servidor (RPC)**

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

---
### TaskHeliChase

`TASK_HELI_CHASE` · hash `0xAC83B1DB38D0ADA0` · jhash `0xAC290A21` · **Cliente**

```lua
TaskHeliChase(pilot, entityToFollow, x, y, z)
```
```c
void TASK_HELI_CHASE(Ped pilot, Entity entityToFollow, float x, float y, float z);
```

**Parámetros**

- `pilot` (`Ped`)
- `entityToFollow` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Ped pilot should be in a heli.  
EntityToFollow can be a vehicle or Ped.  
x,y,z appear to be how close to the EntityToFollow the heli should be. Scripts use 0.0, 0.0, 80.0. Then the heli tries to position itself 80 units above the EntityToFollow. If you reduce it to -5.0, it tries to go below (if the EntityToFollow is a heli or plane)  
NOTE: If the pilot finds enemies, it will engage them, then remain there idle, not continuing to chase the Entity given.  
```

---
### TaskHeliEscortHeli

`_TASK_HELI_ESCORT_HELI` · hash `0xB385523325077210` · **Cliente**

```lua
TaskHeliEscortHeli(pilot, heli1, heli2, p3, p4, p5)
```
```c
void _TASK_HELI_ESCORT_HELI(Ped pilot, Vehicle heli1, Vehicle heli2, float p3, float p4, float p5);
```

**Parámetros**

- `pilot` (`Ped`)
- `heli1` (`Vehicle`)
- `heli2` (`Vehicle`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### TaskHeliMission

`TASK_HELI_MISSION` · hash `0xDAD029E187A2BEB4` · jhash `0x0C143E97` · **Cliente**

```lua
TaskHeliMission(ped, heli, vehicleTarget, pedTarget, x, y, z, missionType, speed, radius, heading, height, minHeight, slowDist, missionFlags)
```
```c
void TASK_HELI_MISSION(Ped ped, Vehicle heli, Vehicle vehicleTarget, Ped pedTarget, float x, float y, float z, int missionType, float speed, float radius, float heading, float height, float minHeight, float slowDist, int missionFlags);
```

**Parámetros**

- `ped` (`Ped`): The ped to be tasked.
- `heli` (`Vehicle`): The helicopters' entity handle.
- `vehicleTarget` (`Vehicle`): The target vehicle (default is 0).
- `pedTarget` (`Ped`): The target ped (default is 0).
- `x` (`float`): The x coordinate of the target (default is 0.0f).
- `y` (`float`): The y coordinate of the target (default is 0.0f).
- `z` (`float`): The z coordinate of the target (default is 0.0f).
- `missionType` (`int`): The mission type (default is 0) (see [TaskVehicleMission](#taskvehiclemission)).
- `speed` (`float`): The speed in m/s.
- `radius` (`float`): The radius of when the task will be completed (default is -1.0f).
- `heading` (`float`): The heading the helicopter will face at task completion (default is -1.0f).
- `height` (`float`): The height the helicopter will fly at (default is -1.0f).
- `minHeight` (`float`): The height the helicopter will not fly below (default is -1.0f).
- `slowDist` (`float`): The distance to the target at which the helicopter will slow down (default is -1.0f).
- `missionFlags` (`int`): The mission flags (default is 0) (see `eHeliMissionFlags`).

**Devuelve:** `void`

**Descripción oficial:**

All parameters except ped, heli and speed are optional, with `pedTarget`, `vehicleTarget`, `x`, `y`, `z` being dependent on `missionType` (ie. Attack/Flee mission types require a target ped/vehicle, whereas GoTo mission types require either `x`, `y`, `z` or a target ped/vehicle).

If you don't want to use a parameter; pass `0.0f` for `x`, `y` and `z`, `0` for `pedTarget`, `vehicleTarget`, `0` for other int parameters, and `-1.0f` for the remaining float parameters.

```cpp
enum eHeliMissionFlags
{
  None = 0,
  AttainRequestedOrientation = 1,
  DontModifyOrientation = 2,
  DontModifyPitch = 4,
  DontModifyThrottle = 8,
  DontModifyRoll = 16,
  LandOnArrival = 32,
  DontDoAvoidance = 64,
  StartEngineImmediately = 128,
  ForceHeightMapAvoidance = 256,
  DontClampProbesToDestination = 512,
  EnableTimeslicingWhenPossible = 1024,
  CircleOppositeDirection = 2048,
  MaintainHeightAboveTerrain = 4096,
  IgnoreHiddenEntitiesDuringLand = 8192,
  DisableAllHeightMapAvoidance = 16384,
  // ForceHeightMapAvoidance | DontDoAvoidance
  HeightMapOnlyAvoidance = 320,
}
```

**Ejemplo (lua):**

```lua
local heli_model = `akula`
RequestModel(heli_model)
repeat Wait(0) until HasModelLoaded(heli_model)

-- Player needs to be outside for this to work
local ped = PlayerPedId()
local coords = GetEntityCoords(ped) + GetEntityForwardVector(ped) * 100.0
local heli = CreateVehicle(heli_model, coords.x, coords.y, coords.z + 50.0, GetEntityHeading(ped) - 180.0, true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(heli_model)
SetHeliBladesFullSpeed(heli)

local ped_model = `a_m_m_skater_01`
RequestModel(ped_model)
repeat Wait(0) until HasModelLoaded(ped_model)

local pilot = CreatePedInsideVehicle(heli, 0, ped_model, -1, true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(ped_model)

TaskHeliMission(pilot, heli, 0, 0, coords.x, coords.y, coords.z, 19, 10.0, -1.0, -1.0, -1.0, -1.0, -1.0, 96)
-- Mission Type: Land | Mission Flags: LandOnArrival | DontDoAvoidance
SetPedKeepTask(pilot, true)
```

---
### TaskJump

`TASK_JUMP` · hash `0x0AE4086104E067B1` · jhash `0x0356E3CE` · **Cliente**

```lua
TaskJump(ped, unused)
```
```c
void TASK_JUMP(Ped ped, BOOL unused);
```

**Parámetros**

- `ped` (`Ped`)
- `unused` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Definition is wrong. This has 4 parameters (Not sure when they were added. v350 has 2, v678 has 4).  
v350: Ped ped, bool unused  
v678: Ped ped, bool unused, bool flag1, bool flag2  
flag1 = super jump, flag2 = do nothing if flag1 is false and doubles super jump height if flag1 is true.  
```

```
NativeDB Added Parameter 3: Any p2
NativeDB Added Parameter 4: Any p3
```

---
### TaskLeaveAnyVehicle

`TASK_LEAVE_ANY_VEHICLE` · hash `0x504D54DF3F6F2247` · jhash `0xDBDD79FA` · **Cliente · también en el servidor (RPC)**

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

Flags are the same flags used in [`TASK_LEAVE_VEHICLE`](../cfx/servidor.md#taskleavevehicle)

---
### TaskLeaveVehicle

`TASK_LEAVE_VEHICLE` · hash `0xD3DBCE61A490BE02` · jhash `0x7B1141C6` · **Cliente · también en el servidor (RPC)**

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

---
### TaskLookAtCoord

`TASK_LOOK_AT_COORD` · hash `0x6FA46612594F7973` · jhash `0x7B784DD8` · **Cliente**

```lua
TaskLookAtCoord(entity, x, y, z, duration, p5, p6)
```
```c
void TASK_LOOK_AT_COORD(Entity entity, float x, float y, float z, int duration, Any p5, Any p6);
```

**Parámetros**

- `entity` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `duration` (`int`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### TaskLookAtEntity

`TASK_LOOK_AT_ENTITY` · hash `0x69F4BE8C8CC4796C` · jhash `0x991D6619` · **Cliente**

```lua
TaskLookAtEntity(ped, lookAt, duration, unknown1, unknown2)
```
```c
void TASK_LOOK_AT_ENTITY(Ped ped, Entity lookAt, int duration, int unknown1, int unknown2);
```

**Parámetros**

- `ped` (`Ped`)
- `lookAt` (`Entity`)
- `duration` (`int`)
- `unknown1` (`int`)
- `unknown2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
param3: duration in ms, use -1 to look forever  
param4: using 2048 is fine  
param5: using 3 is fine  
```

---
### TaskMoveNetworkAdvancedByName

`TASK_MOVE_NETWORK_ADVANCED_BY_NAME` · hash `0xD5B35BEA41919ACB` · jhash `0x71A5C5DB` · **Cliente**

```lua
TaskMoveNetworkAdvancedByName(ped, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, animDict, flags)
```
```c
void TASK_MOVE_NETWORK_ADVANCED_BY_NAME(Ped ped, char* p1, float p2, float p3, float p4, float p5, float p6, float p7, Any p8, float p9, BOOL p10, char* animDict, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)
- `p8` (`Any`)
- `p9` (`float`)
- `p10` (`BOOL`)
- `animDict` (`char*`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example:
TASK::TASK_MOVE_NETWORK_ADVANCED_BY_NAME(PLAYER::PLAYER_PED_ID(), "minigame_tattoo_michael_parts", 324.13f, 181.29f, 102.6f, 0.0f, 0.0f, 22.32f, 2, 0, false, 0, 0);
```

**Nombres antiguos (alias):** `0xD5B35BEA41919ACB` (`N_0xd5b35bea41919acb`), `_TASK_MOVE_NETWORK_ADVANCED` (`TaskMoveNetworkAdvanced`)

---
### TaskMoveNetworkByName

`TASK_MOVE_NETWORK_BY_NAME` · hash `0x2D537BA194896636` · jhash `0x6F5D215F` · **Cliente**

```lua
TaskMoveNetworkByName(ped, task, multiplier, p3, animDict, flags)
```
```c
void TASK_MOVE_NETWORK_BY_NAME(Ped ped, char* task, float multiplier, BOOL p3, char* animDict, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `task` (`char*`)
- `multiplier` (`float`)
- `p3` (`BOOL`)
- `animDict` (`char*`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example:
TASK::TASK_MOVE_NETWORK_BY_NAME(PLAYER::PLAYER_PED_ID(), "arm_wrestling_sweep_paired_a_rev3", 0.0f, true, "mini@arm_wrestling", 0);
```

**Nombres antiguos (alias):** `0x2D537BA194896636` (`N_0x2d537ba194896636`), `_TASK_MOVE_NETWORK` (`TaskMoveNetwork`)

---
### TaskMoveNetworkByNameWithInitParams

`_TASK_MOVE_NETWORK_BY_NAME_WITH_INIT_PARAMS` · hash `0x3D45B0B355C5E0C9` · **Cliente**

```lua
local data = TaskMoveNetworkByNameWithInitParams(ped, p1, p3, p4, animDict, flags)
```
```c
void _TASK_MOVE_NETWORK_BY_NAME_WITH_INIT_PARAMS(Ped ped, char* p1, Any* data, float p3, BOOL p4, char* animDict, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)
- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`float`)
- `p4` (`BOOL`)
- `animDict` (`char*`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used only once in the scripts (am_mp_nightclub)
```

```
Used only once in the scripts (am_mp_nightclub)

NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `_TASK_MOVE_NETWORK_SCRIPTED` (`TaskMoveNetworkScripted`)

---
### TaskOpenVehicleDoor

`TASK_OPEN_VEHICLE_DOOR` · hash `0x965791A9A488A062` · jhash `0x8EE06BF4` · **Cliente**

```lua
TaskOpenVehicleDoor(ped, vehicle, timeOut, seat, speed)
```
```c
void TASK_OPEN_VEHICLE_DOOR(Ped ped, Vehicle vehicle, int timeOut, int seat, float speed);
```

**Parámetros**

- `ped` (`Ped`): The ped to do the task
- `vehicle` (`Vehicle`): The vehicle whose doors the ped shoud open
- `timeOut` (`int`): Sets a timeout to the task; doesn't work for 0
- `seat` (`int`): The seat index - the ped will attempt to open doors to get to the specified seat
- `speed` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

The given ped will try to open the nearest door to 'seat'.

Example: telling the ped to open the door for the driver seat does not necessarily mean it will open the driver door, it may choose to open the passenger door instead if that one is closer.

---
### TaskParachute

`TASK_PARACHUTE` · hash `0xD2F1C53C97EE81AB` · jhash `0xEC3060A2` · **Cliente**

```lua
TaskParachute(ped, p1)
```
```c
void TASK_PARACHUTE(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This function has a third parameter as well (bool).  
Second parameter is unused.  
seconds parameter was for jetpack in the early stages of gta and the hard coded code is now removed  
```

```
NativeDB Added Parameter 3: BOOL p2
```

---
### TaskParachuteToTarget

`TASK_PARACHUTE_TO_TARGET` · hash `0xB33E291AFA6BD03A` · jhash `0xE0104D6C` · **Cliente**

```lua
TaskParachuteToTarget(ped, x, y, z)
```
```c
void TASK_PARACHUTE_TO_TARGET(Ped ped, float x, float y, float z);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
makes ped parachute to coords x y z. Works well with PATHFIND::GET_SAFE_COORD_FOR_PED  
```

---
### TaskPatrol

`TASK_PATROL` · hash `0xBDA5DF49D080FE4E` · jhash `0xB92E5AF6` · **Cliente**

```lua
TaskPatrol(ped, p1, p2, p3, p4)
```
```c
void TASK_PATROL(Ped ped, char* p1, Any p2, BOOL p3, BOOL p4);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)
- `p2` (`Any`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
After looking at some scripts the second parameter seems to be an id of some kind. Here are some I found from some R* scripts:
"miss_Tower_01" (this went from 01 - 10)
"miss_Ass0" (0, 4, 6, 3)
"MISS_PATROL_8"
I think they're patrol routes, but I'm not sure. And I believe the 3rd parameter is a BOOL, but I can't confirm other than only seeing 0 and 1 being passed.
As far as I can see the patrol routes names such as "miss_Ass0" have been defined earlier in the scripts. This leads me to believe we can defined our own new patrol routes by following the same approach.
From the scripts
    TASK::OPEN_PATROL_ROUTE("miss_Ass0");
    TASK::ADD_PATROL_ROUTE_NODE(0, "WORLD_HUMAN_GUARD_STAND", l_738[0/*3*/], -139.4076690673828, -993.4732055664062, 26.2754, MISC::GET_RANDOM_INT_IN_RANGE(5000, 10000));
    TASK::ADD_PATROL_ROUTE_NODE(1, "WORLD_HUMAN_GUARD_STAND", l_738[1/*3*/], -116.1391830444336, -987.4984130859375, 26.38541030883789, MISC::GET_RANDOM_INT_IN_RANGE(5000, 10000));
    TASK::ADD_PATROL_ROUTE_NODE(2, "WORLD_HUMAN_GUARD_STAND", l_738[2/*3*/], -128.46847534179688, -979.0340576171875, 26.2754, MISC::GET_RANDOM_INT_IN_RANGE(5000, 10000));
    TASK::ADD_PATROL_ROUTE_LINK(0, 1);
    TASK::ADD_PATROL_ROUTE_LINK(1, 2);
    TASK::ADD_PATROL_ROUTE_LINK(2, 0);
    TASK::CLOSE_PATROL_ROUTE();
    TASK::CREATE_PATROL_ROUTE();
```

---
### TaskPause

`TASK_PAUSE` · hash `0xE73A266DB0CA9042` · jhash `0x17A64668` · **Cliente**

```lua
TaskPause(ped, ms)
```
```c
void TASK_PAUSE(Ped ped, int ms);
```

**Parámetros**

- `ped` (`Ped`): The ped to pause. Set to this 0 when using task sequences.
- `ms` (`int`): The amount of miliseconds to wait.

**Devuelve:** `void`

**Descripción oficial:**

This tasks the ped to do nothing for the specified amount of miliseconds.
This is useful if you want to add a delay between tasks when using a sequence task.

---
### TaskPedSlideToCoord

`TASK_PED_SLIDE_TO_COORD` · hash `0xD04FE6765D990A06` · jhash `0x225380EF` · **Cliente**

```lua
TaskPedSlideToCoord(ped, x, y, z, heading, duration)
```
```c
void TASK_PED_SLIDE_TO_COORD(Ped ped, float x, float y, float z, float heading, float duration);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `duration` (`float`)

**Devuelve:** `void`

---
### TaskPedSlideToCoordHdgRate

`TASK_PED_SLIDE_TO_COORD_HDG_RATE` · hash `0x5A4A6A6D3DC64F52` · jhash `0x38A995C1` · **Cliente**

```lua
TaskPedSlideToCoordHdgRate(ped, x, y, z, heading, p5, p6)
```
```c
void TASK_PED_SLIDE_TO_COORD_HDG_RATE(Ped ped, float x, float y, float z, float heading, float p5, float p6);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `p5` (`float`)
- `p6` (`float`)

**Devuelve:** `void`

---
### TaskPerformSequence

`TASK_PERFORM_SEQUENCE` · hash `0x5ABA3986D90D8A3B` · jhash `0x4D9FBD11` · **Cliente**

```lua
TaskPerformSequence(ped, taskSequenceId)
```
```c
void TASK_PERFORM_SEQUENCE(Ped ped, int taskSequenceId);
```

**Parámetros**

- `ped` (`Ped`): The ped to perform the sequence on
- `taskSequenceId` (`int`): The sequenceId to perform

**Devuelve:** `void`

**Descripción oficial:**

For an example on how to use this please refer to [OPEN_SEQUENCE_TASK](#opensequencetask)

---
### TaskPerformSequenceFromProgress

`TASK_PERFORM_SEQUENCE_FROM_PROGRESS` · hash `0x89221B16730234F0` · jhash `0xFA60601B` · **Cliente**

```lua
TaskPerformSequenceFromProgress(ped, taskIndex, progress1, progress2)
```
```c
void TASK_PERFORM_SEQUENCE_FROM_PROGRESS(Ped ped, int taskIndex, int progress1, int progress2);
```

**Parámetros**

- `ped` (`Ped`): The ped to perform the task on
- `taskIndex` (`int`)
- `progress1` (`int`): The progress to start from
- `progress2` (`int`): Unknown what it does, it has to be set higher than 0 to not break the sequence

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    local animDict = 'timetable@ron@ig_5_p3'

    RequestAnimDict(animDict)
    while not HasAnimDictLoaded(animDict) do
        Wait(0)
    end

    local ped = PlayerPedId()
    local pos = GetEntityCoords(ped)

    -- you can change the model, but you might have to change the offsets below.
    local objModelHash = `prop_bench_01a`

    local obj = GetClosestObjectOfType(pos.x, pos.y, pos.z, 5.0, objModelHash, false, false, false)
    if obj == 0 then
        print("No valid object within range!")
        return
    end

    local tgtPos = GetOffsetFromEntityInWorldCoords(obj, 0.0, -0.7, 0.0)

    -- open the task sequence so we can get our sequence id
    local sequence = OpenSequenceTask()

    local desiredHeading = GetEntityHeading(obj) - 180.0

    -- go to the entities offset
    TaskGoStraightToCoord(nil, tgtPos.x, tgtPos.y, tgtPos.z, 1.0, 4000, desiredHeading, 1.0)

    -- sit on the bench indefinitely (you can change -1 here to however long you want to sit)
    TaskPlayAnim(nil, animDict, 'ig_5_p3_base', 8.0, 8.0, -1, 1)

    -- close the sequence so we can perform it
    CloseSequenceTask(sequence)

    -- perform the sequence, this will not work if the sequence is still open.
    -- note that progress1 is set to 1, this means it will skip the first sequence
    TaskPerformSequenceFromProgress(ped, sequence, 1, 1)

    -- free the sequence slot so it can be re-used
    ClearSequenceTask(sequence)

    -- cleanup the animation dict so the engine can remove it when its no longer needed
    RemoveAnimDict(animDict)
end)
```

**Ejemplo (cs):**

```cs
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

string animDict = "timetable@ron@ig_5_p3";
RequestAnimDict(animDict);
while (!HasAnimDictLoaded(animDict))
{
	await BaseScript.Delay(0);
}

int ped = PlayerPedId();
Vector3 pos = GetEntityCoords(ped, false);

// you can change the model, but you might have to change the offsets below.
uint hash = Game.GenerateHashASCII("prop_bench_01a");

int obj = GetClosestObjectOfType(pos.X, pos.Y, pos.Z, 5.0f, hash, false, false, false);
if (obj == 0)
{
	Debug.WriteLine("No valid object within range!");
	return;
}

Vector3 tgtPos = GetOffsetFromEntityInWorldCoords(obj, 0.0f, -0.7f, 0.0f);

int sequenceId = 0;
// open the task sequence so we can get our sequence id
OpenSequenceTask(ref sequenceId);

float desiredHeading = GetEntityHeading(obj) - 180.0f;

// go to the entitys offset
TaskGoStraightToCoord(0, tgtPos.X, tgtPos.Y, tgtPos.Z, 1.0f, 4000, desiredHeading, 1.0f);

// sit on the bench indefinitely (you can change -1 here to however long you want to sit)
TaskPlayAnim(0, animDict, "ig_5_p3_base", 8.0f, 8.0f, -1, 1, 1.0f, false, false, false);

// close the sequence so we can perform it
CloseSequenceTask(sequenceId);

// perform the sequence, this will not work if the sequence is still open.
// note that progress1 is set to 1, this means it will skip the first sequence
TaskPerformSequenceFromProgress(ped, sequenceId, 1, 1);

// free the sequence slot so it can be re-used
ClearSequenceTask(ref sequenceId);

// cleanup the animation dict so the engine can remove it when its no longer needed
RemoveAnimDict(animDict);
```

---
### TaskPerformSequenceLocally

`TASK_PERFORM_SEQUENCE_LOCALLY` · hash `0x8C33220C8D78CA0D` · **Cliente**

```lua
TaskPerformSequenceLocally(ped, taskSequenceId)
```
```c
void TASK_PERFORM_SEQUENCE_LOCALLY(Ped ped, int taskSequenceId);
```

**Parámetros**

- `ped` (`Ped`): The ped to perform the sequence on
- `taskSequenceId` (`int`): The sequence to perform

**Devuelve:** `void`

**Descripción oficial:**

For an example on how to use this please refer to [OPEN_SEQUENCE_TASK](#opensequencetask)

**Nombres antiguos (alias):** `0x8C33220C8D78CA0D` (`N_0x8c33220c8d78ca0d`), `_TASK_PERFORM_SEQUENCE_LOCALLY` (`TaskPerformSequenceLocally`)

---
### TaskPlaneChase

`TASK_PLANE_CHASE` · hash `0x2D2386F273FF7A25` · jhash `0x12FA1C28` · **Cliente**

```lua
TaskPlaneChase(pilot, entityToFollow, x, y, z)
```
```c
void TASK_PLANE_CHASE(Ped pilot, Entity entityToFollow, float x, float y, float z);
```

**Parámetros**

- `pilot` (`Ped`)
- `entityToFollow` (`Entity`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### TaskPlaneGotoPreciseVtol

`_TASK_PLANE_GOTO_PRECISE_VTOL` · hash `0xF7F9DCCA89E7505B` · **Cliente**

```lua
TaskPlaneGotoPreciseVtol(ped, vehicle, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
void _TASK_PLANE_GOTO_PRECISE_VTOL(Ped ped, Vehicle vehicle, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)
- `p9` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### TaskPlaneLand

`TASK_PLANE_LAND` · hash `0xBF19721FA34D32C0` · jhash `0x5F7E23EA` · **Cliente**

```lua
TaskPlaneLand(pilot, plane, runwayStartX, runwayStartY, runwayStartZ, runwayEndX, runwayEndY, runwayEndZ)
```
```c
void TASK_PLANE_LAND(Ped pilot, Vehicle plane, float runwayStartX, float runwayStartY, float runwayStartZ, float runwayEndX, float runwayEndY, float runwayEndZ);
```

**Parámetros**

- `pilot` (`Ped`)
- `plane` (`Vehicle`)
- `runwayStartX` (`float`)
- `runwayStartY` (`float`)
- `runwayStartZ` (`float`)
- `runwayEndX` (`float`)
- `runwayEndY` (`float`)
- `runwayEndZ` (`float`)

**Devuelve:** `void`

---
### TaskPlaneMission

`TASK_PLANE_MISSION` · hash `0x23703CD154E83B88` · jhash `0x1D007E65` · **Cliente**

```lua
TaskPlaneMission(ped, vehicle, targetVehicle, targetPed, fTargetCoordX, fTargetCoordY, fTargetCoordZ, iMissionIndex, fCruiseSpeed, fTargetReachedDist, fOrientation, iFlightHeight, iMinHeightAboveTerrain, bPrecise)
```
```c
void TASK_PLANE_MISSION(Ped ped, Vehicle vehicle, Vehicle targetVehicle, Ped targetPed, float fTargetCoordX, float fTargetCoordY, float fTargetCoordZ, int iMissionIndex, float fCruiseSpeed, float fTargetReachedDist, float fOrientation, int iFlightHeight, int iMinHeightAboveTerrain, BOOL bPrecise);
```

**Parámetros**

- `ped` (`Ped`): The `Ped` handle.
- `vehicle` (`Vehicle`): The `Vehicle` handle for the actual plane that will be flown.
- `targetVehicle` (`Vehicle`): The target `Vehicle` handle (in case `eVehicleMission` requires one).
- `targetPed` (`Ped`): The target `Ped` (in case `eVehicleMission` requires one).
- `fTargetCoordX` (`float`)
- `fTargetCoordY` (`float`)
- `fTargetCoordZ` (`float`)
- `iMissionIndex` (`int`): The mission to be executed. See `eVehicleMission`.
- `fCruiseSpeed` (`float`): The cruise speed (in m/s).
- `fTargetReachedDist` (`float`): Distance (in meters) (at which the plane thinks it has arrived), this is also used as the hover distance for `MISSION_ATTACK` and `MISSION_CIRCLE`.
- `fOrientation` (`float`): Used to specify the desired orientation of the plane in degrees (`0` to `360`). Use `-1` if no specific orientation is required.
- `iFlightHeight` (`int`): The height above sea level the plane tries to maintain, i.e. `50` meters.
- `iMinHeightAboveTerrain` (`int`): The minimum height above terrain, i.e. `30` meters.
- `bPrecise` (`BOOL`): A boolean value, defaults to `true`.

**Devuelve:** `void`

**Descripción oficial:**

Gives the plane a mission (purpose or objective), the mission is passed onto the `iMissionIndex` parameter.

```cpp
enum eVehicleMission {
    MISSION_NONE = 0,
    MISSION_CRUISE, // 1
    MISSION_RAM, // 2
    MISSION_BLOCK, // 3
    MISSION_GOTO, // 4
    MISSION_STOP, // 5
    MISSION_ATTACK, // 6
    MISSION_FOLLOW, // 7
    MISSION_FLEE, // 8
    MISSION_CIRCLE, // 9
    MISSION_ESCORT_LEFT, // 10
    MISSION_ESCORT_RIGHT, // 11
    MISSION_ESCORT_REAR, // 12
    MISSION_ESCORT_FRONT, // 13
    MISSION_GOTO_RACING, // 14
    MISSION_FOLLOW_RECORDING, // 15
    MISSION_POLICE_BEHAVIOUR, // 16
    MISSION_PARK_PERPENDICULAR, // 17
    MISSION_PARK_PARALLEL, // 18
    MISSION_LAND, // 19
    MISSION_LAND_AND_WAIT, // 20
    MISSION_CRASH, // 21
    MISSION_PULL_OVER, // 22
    MISSION_PROTECT // 23
};
```

---
### TaskPlaneTaxi

`TASK_PLANE_TAXI` · hash `0x92C360B5F15D2302` · **Cliente**

```lua
TaskPlaneTaxi(pilot, aircraft, xPos, yPos, zPos, fCruiseSpeed, fTargetReachedDist)
```
```c
void TASK_PLANE_TAXI(Ped pilot, Vehicle aircraft, float xPos, float yPos, float zPos, float fCruiseSpeed, float fTargetReachedDist);
```

**Parámetros**

- `pilot` (`Ped`): The ped driving the plane.
- `aircraft` (`Vehicle`): The plane used.
- `xPos` (`float`): The X coordinate.
- `yPos` (`float`): The Y coordinate.
- `zPos` (`float`): The Z coordinate.
- `fCruiseSpeed` (`float`): The speed of the plane (in m/s).
- `fTargetReachedDist` (`float`): Distance (in meters) at which the plane thinks it has arrived to the given coordinates.

**Devuelve:** `void`

**Descripción oficial:**

The given ped will try to drive the plane to the given coordinates and will then drive around the given coords (the plane will form 8s on the ground)

**Nombres antiguos (alias):** `0x92C360B5F15D2302` (`N_0x92c360b5f15d2302`), `_TASK_PLANE_TAXI` (`TaskPlaneTaxi`)

---
### TaskPlantBomb

`TASK_PLANT_BOMB` · hash `0x965FEC691D55E9BF` · jhash `0x33457535` · **Cliente**

```lua
TaskPlantBomb(ped, x, y, z, heading)
```
```c
void TASK_PLANT_BOMB(Ped ped, float x, float y, float z, float heading);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)

**Devuelve:** `void`

---
### TaskPlayAnim

`TASK_PLAY_ANIM` · hash `0xEA47FE3719165B94` · jhash `0x5AB552C6` · **Cliente · también en el servidor (RPC)**

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

---
### TaskPlayAnimAdvanced

`TASK_PLAY_ANIM_ADVANCED` · hash `0x83CDB10EA29B370B` · jhash `0x3DDEB0E6` · **Cliente · también en el servidor (RPC)**

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
- `flag` (`Any`): See [`TASK_PLAY_ANIM`](../cfx/servidor.md#taskplayanim)
- `animTime` (`float`): Value between 0.0 and 1.0, lets you start an animation from the given point
- `p14` (`Any`)
- `p15` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

Similar in functionality to [`TASK_PLAY_ANIM`](../cfx/servidor.md#taskplayanim), except the position and rotation parameters let you specify the initial position and rotation of the task. The ped is teleported to the position specified.

[Animations list](https://alexguirre.github.io/animations-list/)

---
### TaskPlayPhoneGestureAnimation

`TASK_PLAY_PHONE_GESTURE_ANIMATION` · hash `0x8FBB6758B3B3E9EC` · jhash `0x1582162C` · **Cliente**

```lua
TaskPlayPhoneGestureAnimation(ped, animDict, animation, boneMaskType, p4, p5, p6, p7)
```
```c
void TASK_PLAY_PHONE_GESTURE_ANIMATION(Ped ped, char* animDict, char* animation, char* boneMaskType, float p4, float p5, BOOL p6, BOOL p7);
```

**Parámetros**

- `ped` (`Ped`)
- `animDict` (`char*`)
- `animation` (`char*`)
- `boneMaskType` (`char*`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example from the scripts:
TASK::TASK_PLAY_PHONE_GESTURE_ANIMATION(PLAYER::PLAYER_PED_ID(), v_3, v_2, v_4, 0.25, 0.25, 0, 0);
=========================================================
^^ No offense, but Idk how that would really help anyone.
As for the animDict & animation, they're both store in a global in all 5 scripts. So if anyone would be so kind as to read that global and comment what strings they use. Thanks.
Known boneMaskTypes'
"BONEMASK_HEADONLY"
"BONEMASK_HEAD_NECK_AND_ARMS"
"BONEMASK_HEAD_NECK_AND_L_ARM"
"BONEMASK_HEAD_NECK_AND_R_ARM"
p4 known args - 0.0f, 0.5f, 0.25f
p5 known args - 0.0f, 0.25f
p6 known args - 1 if a global if check is passed.
p7 known args - 1 if a global if check is passed.
The values found above, I found within the 5 scripts this is ever called in. (fmmc_launcher, fm_deathmatch_controller, fm_impromptu_dm_controller, fm_mission_controller, and freemode).
=========================================================
```

---
### TaskPutPedDirectlyIntoCover

`TASK_PUT_PED_DIRECTLY_INTO_COVER` · hash `0x4172393E6BE1FECE` · jhash `0xC9F00E68` · **Cliente**

```lua
TaskPutPedDirectlyIntoCover(ped, x, y, z, timeout, p5, p6, p7, p8, p9, p10)
```
```c
void TASK_PUT_PED_DIRECTLY_INTO_COVER(Ped ped, float x, float y, float z, Any timeout, BOOL p5, float p6, BOOL p7, BOOL p8, Any p9, BOOL p10);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `timeout` (`Any`)
- `p5` (`BOOL`)
- `p6` (`float`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)
- `p9` (`Any`)
- `p10` (`BOOL`)

**Devuelve:** `void`

---
### TaskPutPedDirectlyIntoMelee

`TASK_PUT_PED_DIRECTLY_INTO_MELEE` · hash `0x1C6CD14A876FFE39` · jhash `0x79E1D27D` · **Cliente**

```lua
TaskPutPedDirectlyIntoMelee(ped, meleeTarget, p2, p3, p4, p5)
```
```c
void TASK_PUT_PED_DIRECTLY_INTO_MELEE(Ped ped, Ped meleeTarget, float p2, float p3, float p4, BOOL p5);
```

**Parámetros**

- `ped` (`Ped`)
- `meleeTarget` (`Ped`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
from armenian3.c4
TASK::TASK_PUT_PED_DIRECTLY_INTO_MELEE(PlayerPed, armenianPed, 0.0, -1.0, 0.0, 0);
```

---
### TaskRappelDownWall

`_TASK_RAPPEL_DOWN_WALL` · hash `0xEAF66ACDDC794793` · **Cliente**

```lua
TaskRappelDownWall(ped, x1, y1, z1, x2, y2, z2, minZ, ropeId, clipset, p10)
```
```c
void _TASK_RAPPEL_DOWN_WALL(Ped ped, float x1, float y1, float z1, float x2, float y2, float z2, float minZ, int ropeId, char* clipset, Any p10);
```

**Parámetros**

- `ped` (`Ped`): Ped to perform the task
- `x1` (`float`): X coord to start the task
- `y1` (`float`): Y coord to start the task
- `z1` (`float`): Z coord to start the task
- `x2` (`float`): Second X coord, uses the same position as above in the scripts
- `y2` (`float`): Second Y coord
- `z2` (`float`): Second Z coord
- `minZ` (`float`): Minimum Z that the player can descend to
- `ropeId` (`int`): Rope to attach this task to, must be created with [ADD_ROPE](PHYSICS.md#addrope)
- `clipset` (`char*`): Clipset to use for the task
- `p10` (`Any`): Usually 1 in the scripts

**Devuelve:** `void`

**Descripción oficial:**

Attaches a ped to a rope and allows player control to rappel down a wall.
Disables all collisions while on the rope.

NativeDB Introduced: v1868

**Nombres antiguos (alias):** `0xEAF66ACDDC794793` (`N_0xeaf66acddc794793`)

**Ejemplo (lua):**

```lua
local coords = vector3(258.68, -3311.5, 45.72)
RopeLoadTextures()
SetEntityCoords(PlayerPedId(), coords - vector3(0, 0, 10.0))
local ropeId = AddRope(coords, -90.0, 90.0, -90.0, 78.0, 7, 78.0, 78.0, 1.2, false, false, true, 10.0, false, 0)
TaskRappelDownWall(PlayerPedId(), coords, coords, -130.0, ropeId, "clipset@anim_heist@hs3f@ig1_rappel@male", 1)
N_0xa1ae736541b0fca3(ropeId, true)
PinRopeVertex(ropeId, (GetRopeVertexCount(ropeId) - 1), coords + vector3(0, 0, 1.0))
RopeSetUpdateOrder(ropeId, 0)
```

---
### TaskRappelFromHeli

`TASK_RAPPEL_FROM_HELI` · hash `0x09693B0312F91649` · jhash `0x2C7ADB93` · **Cliente**

```lua
TaskRappelFromHeli(ped, unused)
```
```c
void TASK_RAPPEL_FROM_HELI(Ped ped, float unused);
```

**Parámetros**

- `ped` (`Ped`)
- `unused` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only appears twice in the scripts.
TASK::TASK_RAPPEL_FROM_HELI(PLAYER::PLAYER_PED_ID(), 0x41200000);
TASK::TASK_RAPPEL_FROM_HELI(a_0, 0x41200000);
```

---
### TaskReactAndFleePed

`TASK_REACT_AND_FLEE_PED` · hash `0x72C896464915D1B1` · jhash `0x8A632BD8` · **Cliente · también en el servidor (RPC)**

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

---
### TaskReloadWeapon

`TASK_RELOAD_WEAPON` · hash `0x62D2916F56B9CD2D` · jhash `0xCA6E91FD` · **Cliente**

```lua
TaskReloadWeapon(ped, unused)
```
```c
void TASK_RELOAD_WEAPON(Ped ped, BOOL unused);
```

**Parámetros**

- `ped` (`Ped`)
- `unused` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
The 2nd param (unused) is not implemented.
-----------------------------------------------------------------------
The only occurrence I found in a R* script ("assassin_construction.ysc.c4"):
            if (((v_3 < v_4) && (TASK::GET_SCRIPT_TASK_STATUS(PLAYER::PLAYER_PED_ID(), 0x6a67a5cc) != 1)) && (v_5 > v_3)) {
                TASK::TASK_RELOAD_WEAPON(PLAYER::PLAYER_PED_ID(), 1);
            }
```

---
### TaskScriptedAnimation

`TASK_SCRIPTED_ANIMATION` · hash `0x126EF75F1E17ABE5` · jhash `0xFC2DCF47` · **Cliente**

```lua
local p1, p2, p3 = TaskScriptedAnimation(ped, p4, p5)
```
```c
void TASK_SCRIPTED_ANIMATION(Ped ped, Any* p1, Any* p2, Any* p3, float p4, float p5);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
From fm_mission_controller.c:  
reserve_network_mission_objects(get_num_reserved_mission_objects(0) + 1);  
	vVar28 = {0.094f, 0.02f, -0.005f};  
	vVar29 = {-92.24f, 63.64f, 150.24f};  
	func_253(&uVar30, joaat("prop_ld_case_01"), Global_1592429.imm_34757[iParam1 <268>], 1, 1, 0, 1);  
	set_entity_lod_dist(net_to_ent(uVar30), 500);  
	attach_entity_to_entity(net_to_ent(uVar30), iParam0, get_ped_bone_index(iParam0, 28422), vVar28, vVar29, 1, 0, 0, 0, 2, 1);  
	Var31.imm_4 = 1065353216;  
	Var31.imm_5 = 1065353216;  
	Var31.imm_9 = 1065353216;  
	Var31.imm_10 = 1065353216;  
	Var31.imm_14 = 1065353216;  
	Var31.imm_15 = 1065353216;  
	Var31.imm_17 = 1040187392;  
	Var31.imm_18 = 1040187392;  
	Var31.imm_19 = -1;  
	Var32.imm_4 = 1065353216;  
	Var32.imm_5 = 1065353216;  
	Var32.imm_9 = 1065353216;  
	Var32.imm_10 = 1065353216;  
	Var32.imm_14 = 1065353216;  
	Var32.imm_15 = 1065353216;  
	Var32.imm_17 = 1040187392;  
	Var32.imm_18 = 1040187392;  
	Var32.imm_19 = -1;  
	Var31 = 1;  
	Var31.imm_1 = "weapons@misc@jerrycan@mp_male";  
	Var31.imm_2 = "idle";  
	Var31.imm_20 = 1048633;  
	Var31.imm_4 = 0.5f;  
	Var31.imm_16 = get_hash_key("BONEMASK_ARMONLY_R");  
	task_scripted_animation(iParam0, &Var31, &Var32, &Var32, 0f, 0.25f);  
	set_model_as_no_longer_needed(joaat("prop_ld_case_01"));  
	remove_anim_dict("anim@heists@biolab@");  
```

---
### TaskSeekCoverFromPed

`TASK_SEEK_COVER_FROM_PED` · hash `0x84D32B3BEC531324` · jhash `0xC1EC907E` · **Cliente**

```lua
TaskSeekCoverFromPed(ped, target, duration, p3)
```
```c
void TASK_SEEK_COVER_FROM_PED(Ped ped, Ped target, int duration, BOOL p3);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)
- `duration` (`int`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### TaskSeekCoverFromPos

`TASK_SEEK_COVER_FROM_POS` · hash `0x75AC2B60386D89F2` · jhash `0x83F18EE9` · **Cliente**

```lua
TaskSeekCoverFromPos(ped, x, y, z, duration, p5)
```
```c
void TASK_SEEK_COVER_FROM_POS(Ped ped, float x, float y, float z, int duration, BOOL p5);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `duration` (`int`)
- `p5` (`BOOL`)

**Devuelve:** `void`

---
### TaskSeekCoverToCoords

`TASK_SEEK_COVER_TO_COORDS` · hash `0x39246A6958EF072C` · jhash `0xFFFE754E` · **Cliente**

```lua
TaskSeekCoverToCoords(ped, x1, y1, z1, x2, y2, z2, p7, p8)
```
```c
void TASK_SEEK_COVER_TO_COORDS(Ped ped, float x1, float y1, float z1, float x2, float y2, float z2, Any p7, BOOL p8);
```

**Parámetros**

- `ped` (`Ped`)
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `p7` (`Any`)
- `p8` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
from michael2:
TASK::TASK_SEEK_COVER_TO_COORDS(ped, 967.5164794921875, -2121.603515625, 30.479299545288086, 978.94677734375, -2125.84130859375, 29.4752, -1, 1);
appears to be shorter variation
from michael3:
TASK::TASK_SEEK_COVER_TO_COORDS(ped, -2231.011474609375, 263.6326599121094, 173.60195922851562, -1, 0);
```

---
### TaskSeekCoverToCoverPoint

`TASK_SEEK_COVER_TO_COVER_POINT` · hash `0xD43D95C7A869447F` · jhash `0x3D026B29` · **Cliente**

```lua
TaskSeekCoverToCoverPoint(p0, p1, p2, p3, p4, p5, p6)
```
```c
void TASK_SEEK_COVER_TO_COVER_POINT(Any p0, Any p1, float p2, float p3, float p4, Any p5, BOOL p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`Any`)
- `p6` (`BOOL`)

**Devuelve:** `void`

---
### TaskSetBlockingOfNonTemporaryEvents

`TASK_SET_BLOCKING_OF_NON_TEMPORARY_EVENTS` · hash `0x90D2156198831D69` · jhash `0x1B54FB6B` · **Cliente**

```lua
TaskSetBlockingOfNonTemporaryEvents(ped, toggle)
```
```c
void TASK_SET_BLOCKING_OF_NON_TEMPORARY_EVENTS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
I cant believe I have to define this, this is one of the best natives.  
It makes the ped ignore basically all shocking events around it. Occasionally the ped may comment or gesture, but other than that they just continue their daily activities. This includes shooting and wounding the ped. And - most importantly - they do not flee.  
Since it is a task, every time the native is called the ped will stop for a moment.  
```

---
### TaskSetDecisionMaker

`TASK_SET_DECISION_MAKER` · hash `0xEB8517DDA73720DA` · jhash `0x830AD50C` · **Cliente**

```lua
TaskSetDecisionMaker(ped, p1)
```
```c
void TASK_SET_DECISION_MAKER(Ped ped, Hash p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
p1 is always GET_HASH_KEY("empty") in scripts, for the rare times this is used  
```

---
### TaskSetSphereDefensiveArea

`TASK_SET_SPHERE_DEFENSIVE_AREA` · hash `0x933C06518B52A9A4` · jhash `0x9F3C5D6A` · **Cliente**

```lua
TaskSetSphereDefensiveArea(p0, p1, p2, p3, p4)
```
```c
void TASK_SET_SPHERE_DEFENSIVE_AREA(Any p0, float p1, float p2, float p3, float p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

---
### TaskSharkCircleCoord

`TASK_SHARK_CIRCLE_COORD` · hash `0x60A19CF85FF4CEFA` · **Cliente**

```lua
TaskSharkCircleCoord(ped, x, y, z, moveBlendRatio, radius)
```
```c
void TASK_SHARK_CIRCLE_COORD(Ped ped, float x, float y, float z, float moveBlendRatio, float radius);
```

**Parámetros**

- `ped` (`Ped`): The shark ped.
- `x` (`float`): X coordinate to circle around
- `y` (`float`): Y coordinate to circle around
- `z` (`float`): Z coordinate to circle around
- `moveBlendRatio` (`float`): Animation blend ratio from 0.0 to 1.0
- `radius` (`float`): Radius of the circular path in meters

**Devuelve:** `void`

**Descripción oficial:**

Makes a shark ped circle around specified coordinates.

```
NativeDB Introduced: v3407
```

**Ejemplo (lua):**

```lua
CreateThread(function()
    local sharkModel = GetHashKey("a_c_sharktiger")
    RequestModel(sharkModel)
    
    while not HasModelLoaded(sharkModel) do
        Wait(0)
    end

    local coords = GetEntityCoords(PlayerPedId(), false)
    local shark = CreatePed(28, sharkModel, coords.x, coords.y, coords.z, 0.0, true, true)
    
    SetModelAsNoLongerNeeded(sharkModel)
    
    if shark == 0 then return end
    
    TaskSharkCircleCoord(shark, coords.x, coords.y, coords.z - 5.0, 1.0, 10.0)
    
    Wait(10000) -- We're letting the shark do circle movement for 10 seconds
    ClearPedTasks(shark) -- Going to stop the task
end)
```

---
### TaskShockingEventReact

`TASK_SHOCKING_EVENT_REACT` · hash `0x452419CBD838065B` · jhash `0x9BD00ACF` · **Cliente**

```lua
TaskShockingEventReact(ped, eventHandle)
```
```c
void TASK_SHOCKING_EVENT_REACT(Ped ped, int eventHandle);
```

**Parámetros**

- `ped` (`Ped`)
- `eventHandle` (`int`)

**Devuelve:** `void`

---
### TaskShootAtCoord

`TASK_SHOOT_AT_COORD` · hash `0x46A6CC01E0826106` · jhash `0x601C22E3` · **Cliente · también en el servidor (RPC)**

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

---
### TaskShootAtEntity

`TASK_SHOOT_AT_ENTITY` · hash `0x08DA95E8298AE772` · jhash `0xAC0631C9` · **Cliente · también en el servidor (RPC)**

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

---
### TaskShuffleToNextVehicleSeat

`TASK_SHUFFLE_TO_NEXT_VEHICLE_SEAT` · hash `0x7AA80209BDA643EB` · jhash `0xBEAF8F67` · **Cliente**

```lua
TaskShuffleToNextVehicleSeat(ped, vehicle)
```
```c
void TASK_SHUFFLE_TO_NEXT_VEHICLE_SEAT(Ped ped, Vehicle vehicle);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the specified ped shuffle to the next vehicle seat.  
The ped MUST be in a vehicle and the vehicle parameter MUST be the ped's current vehicle.  
```

```
NativeDB Added Parameter 3: Any p2
```

---
### TaskSkyDive

`TASK_SKY_DIVE` · hash `0x601736CFE536B0A0` · jhash `0xD3874AFA` · **Cliente**

```lua
TaskSkyDive(ped)
```
```c
void TASK_SKY_DIVE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: BOOL p1
```

---
### TaskSmartFleeCoord

`TASK_SMART_FLEE_COORD` · hash `0x94587F17E9C365D5` · jhash `0xB2E686FC` · **Cliente**

```lua
TaskSmartFleeCoord(ped, x, y, z, distance, time, p6, p7)
```
```c
void TASK_SMART_FLEE_COORD(Ped ped, float x, float y, float z, float distance, int time, BOOL p6, BOOL p7);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `distance` (`float`)
- `time` (`int`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the specified ped flee the specified distance from the specified position.  
```

---
### TaskSmartFleePed

`TASK_SMART_FLEE_PED` · hash `0x22B0D0E37CCB840D` · jhash `0xE52EB560` · **Cliente**

```lua
TaskSmartFleePed(ped, fleeTarget, distance, fleeTime, p4, p5)
```
```c
void TASK_SMART_FLEE_PED(Ped ped, Ped fleeTarget, float distance, Any fleeTime, BOOL p4, BOOL p5);
```

**Parámetros**

- `ped` (`Ped`)
- `fleeTarget` (`Ped`)
- `distance` (`float`)
- `fleeTime` (`Any`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes a ped run away from another ped (fleeTarget).  
distance = ped will flee this distance.  
fleeTime = ped will flee for this amount of time, set to "-1" to flee forever  
```

---
### TaskStandGuard

`TASK_STAND_GUARD` · hash `0xAE032F8BBA959E90` · jhash `0xD130F636` · **Cliente**

```lua
TaskStandGuard(ped, x, y, z, heading, scenarioName)
```
```c
void TASK_STAND_GUARD(Ped ped, float x, float y, float z, float heading, char* scenarioName);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `scenarioName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
scenarioName example: "WORLD_HUMAN_GUARD_STAND"  
```

---
### TaskStandStill

`TASK_STAND_STILL` · hash `0x919BE13EED931959` · jhash `0x6F80965D` · **Cliente**

```lua
TaskStandStill(ped, time)
```
```c
void TASK_STAND_STILL(Ped ped, int time);
```

**Parámetros**

- `ped` (`Ped`)
- `time` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the specified ped stand still for (time) milliseconds.  
```

---
### TaskStartScenarioAtPosition

`TASK_START_SCENARIO_AT_POSITION` · hash `0xFA4EFC79F69D4F07` · jhash `0xAA2C4AC2` · **Cliente**

```lua
TaskStartScenarioAtPosition(ped, scenarioName, x, y, z, heading, timeToLeave, playIntro, warp)
```
```c
void TASK_START_SCENARIO_AT_POSITION(Ped ped, char* scenarioName, float x, float y, float z, float heading, int timeToLeave, BOOL playIntro, BOOL warp);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `scenarioName` (`char*`): The name of the scenario to start.
- `x` (`float`): The x coordinate to start at.
- `y` (`float`): The y coordinate to start at.
- `z` (`float`): The z coordinate to start at. Should be the ground position plus the ped's ground to root offset.
- `heading` (`float`): The heading to start at.
- `timeToLeave` (`int`): Sets the timeout on the scenario point to the specified time in milliseconds. If less than 0, sets the `IdleForever` flag.
- `playIntro` (`BOOL`): If the ped should play the scenarios enter animation. Sets the `SkipEnterClip` flag.
- `warp` (`BOOL`): If the ped should be warped to the position. Sets the `Warp` flag.

**Devuelve:** `void`

**Descripción oficial:**

The ped will move or warp to the position and heading given, then start the scenario passed. See [`TASK_START_SCENARIO_IN_PLACE`](#taskstartscenarioinplace) for a list of scenarios.

---
### TaskStartScenarioInPlace

`TASK_START_SCENARIO_IN_PLACE` · hash `0x142A02425FF02BD9` · jhash `0xE50D6DDE` · **Cliente**

```lua
TaskStartScenarioInPlace(ped, scenarioName, timeToLeave, playIntroClip)
```
```c
void TASK_START_SCENARIO_IN_PLACE(Ped ped, char* scenarioName, int timeToLeave, BOOL playIntroClip);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `scenarioName` (`char*`): The name of the scenario to start.
- `timeToLeave` (`int`): Sets the timeout on the scenario point to the specified time in milliseconds. If less than 0, sets the `IdleForever` flag.
- `playIntroClip` (`BOOL`): If the ped should play the scenarios enter animation. Sets the `SkipEnterClip` flag.

**Devuelve:** `void`

**Descripción oficial:**

Puts the ped into the given scenario immediately at their current location. [List of scenario names](https://pastebin.com/6mrYTdQv) or in `update/update.rpf/common/data/ai/scenarios.meta`.

---
### TaskStayInCover

`TASK_STAY_IN_COVER` · hash `0xE5DA8615A6180789` · jhash `0xA27A9413` · **Cliente**

```lua
TaskStayInCover(ped)
```
```c
void TASK_STAY_IN_COVER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the ped run to take cover  
```

---
### TaskStealthKill

`TASK_STEALTH_KILL` · hash `0xAA5DC05579D60BD9` · jhash `0x0D64C2FA` · **Cliente**

```lua
TaskStealthKill(killer, target, actionType, p3, p4)
```
```c
void TASK_STEALTH_KILL(Ped killer, Ped target, Hash actionType, float p3, Any p4);
```

**Parámetros**

- `killer` (`Ped`)
- `target` (`Ped`)
- `actionType` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p3` (`float`)
- `p4` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
Stealth kill action name hashes:  
stealth kills can be found here: Grand Theft Auto V\common.rpf\data\action\stealth_kills.meta  
...  
{  
    "ACT_stealth_kill_a",  
    "ACT_stealth_kill_weapon",  
    "ACT_stealth_kill_b",  
    "ACT_stealth_kill_c",  
    "ACT_stealth_kill_d",  
    "ACT_stealth_kill_a_gardener"  
}  
Only known script using this native: fbi4_prep2  
EXAMPLE:  
ai::task_stealth_kill(iParam1, Local_252, gameplay::get_hash_key("AR_stealth_kill_a"), 1f, 0);ai::task_stealth_kill(iParam1, Local_252, gameplay::get_hash_key("AR_stealth_kill_knife"), 1f, 0);  
Also it may be important to note, that each time this task is called, it's followed by AI::CLEAR_PED_TASKS on the target  
```

---
### TaskStopPhoneGestureAnimation

`TASK_STOP_PHONE_GESTURE_ANIMATION` · hash `0x3FA00D4F4641BFAE` · jhash `0x5A32D4B4` · **Cliente**

```lua
TaskStopPhoneGestureAnimation(ped)
```
```c
void TASK_STOP_PHONE_GESTURE_ANIMATION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `_TASK_STOP_PHONE_GESTURE_ANIMATION` (`TaskStopPhoneGestureAnimation`)

---
### TaskSubmarineGotoAndStop

`_TASK_SUBMARINE_GOTO_AND_STOP` · hash `0xC22B40579A498CA4` · **Cliente**

```lua
TaskSubmarineGotoAndStop(p0, submarine, x, y, z, p5)
```
```c
void _TASK_SUBMARINE_GOTO_AND_STOP(Any p0, Vehicle submarine, float x, float y, float z, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `submarine` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

Used in am_vehicle_spawn.ysc and am_mp_submarine.ysc.
p0 is always 0, p5 is always 1
p1 is the vehicle handle of the submarine. Submarine must have a driver, but the ped handle is not passed to the native.
Speed can be set by calling SET_DRIVE_TASK_CRUISE_SPEED after

```
NativeDB Introduced: v2189
```

---
### TaskSwapWeapon

`TASK_SWAP_WEAPON` · hash `0xA21C51255B205245` · jhash `0xDAF4F8FC` · **Cliente**

```lua
TaskSwapWeapon(ped, p1)
```
```c
void TASK_SWAP_WEAPON(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### TaskSweepAimEntity

`TASK_SWEEP_AIM_ENTITY` · hash `0x2047C02158D6405A` · jhash `0x4D210467` · **Cliente**

```lua
TaskSweepAimEntity(ped, anim, p2, p3, p4, p5, vehicle, p7, p8)
```
```c
void TASK_SWEEP_AIM_ENTITY(Ped ped, char* anim, char* p2, char* p3, char* p4, int p5, Vehicle vehicle, float p7, float p8);
```

**Parámetros**

- `ped` (`Ped`)
- `anim` (`char*`)
- `p2` (`char*`)
- `p3` (`char*`)
- `p4` (`char*`)
- `p5` (`int`)
- `vehicle` (`Vehicle`)
- `p7` (`float`)
- `p8` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This function is called on peds in vehicles.  
anim: animation name  
p2, p3, p4: "sweep_low", "sweep_med" or "sweep_high"  
p5: no idea what it does but is usually -1  
```

---
### TaskSweepAimPosition

`TASK_SWEEP_AIM_POSITION` · hash `0x7AFE8FDC10BC07D2` · jhash `0x1683FE66` · **Cliente**

```lua
local p1, p2, p3, p4 = TaskSweepAimPosition(p0, p5, p6, p7, p8, p9, p10)
```
```c
void TASK_SWEEP_AIM_POSITION(Any p0, Any* p1, Any* p2, Any* p3, Any* p4, Any p5, float p6, float p7, float p8, float p9, float p10);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p5` (`Any`)
- `p6` (`float`)
- `p7` (`float`)
- `p8` (`float`)
- `p9` (`float`)
- `p10` (`float`)

**Devuelve:** `void`

---
### TaskSynchronizedScene

`TASK_SYNCHRONIZED_SCENE` · hash `0xEEA929141F699854` · jhash `0x4F217E7B` · **Cliente**

```lua
TaskSynchronizedScene(ped, scene, animDictionary, animationName, speed, speedMultiplier, duration, flag, playbackRate, p9)
```
```c
void TASK_SYNCHRONIZED_SCENE(Ped ped, int scene, char* animDictionary, char* animationName, float speed, float speedMultiplier, int duration, int flag, float playbackRate, Any p9);
```

**Parámetros**

- `ped` (`Ped`)
- `scene` (`int`)
- `animDictionary` (`char*`)
- `animationName` (`char*`)
- `speed` (`float`)
- `speedMultiplier` (`float`)
- `duration` (`int`)
- `flag` (`int`)
- `playbackRate` (`float`)
- `p9` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
 TASK::TASK_SYNCHRONIZED_SCENE(ped, scene, "creatures@rottweiler@in_vehicle@std_car", "get_in", 1000.0, -8.0, 4, 0, 0x447a0000, 0);
```

---
### TaskThrowProjectile

`TASK_THROW_PROJECTILE` · hash `0x7285951DBF6B5A51` · jhash `0xF65C20A7` · **Cliente**

```lua
TaskThrowProjectile(ped, x, y, z)
```
```c
void TASK_THROW_PROJECTILE(Ped ped, float x, float y, float z);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
In every case of this native, I've only seen the first parameter passed as 0, although I believe it's a Ped after seeing tasks around it using 0. That's because it's used in a Sequence Task.  
The last 3 parameters are definitely coordinates after seeing them passed in other scripts, and even being used straight from the player's coordinates.  
---  
It seems that - in the decompiled scripts - this native was used on a ped who was in a vehicle to throw a projectile out the window at the player. This is something any ped will naturally do if they have a throwable and they are doing driveby-combat (although not very accurately).  
It is possible, however, that this is how SWAT throws smoke grenades at the player when in cover.  
----------------------------------------------------  
The first comment is right it definately is the ped as if you look in script finale_heist2b.c line 59628 in Xbox Scripts atleast you will see task_throw_projectile and the first param is Local_559[2 <14>] if you look above it a little bit line 59622 give_weapon_to_ped uses the same exact param Local_559[2 <14>] and we all know the first param of that native is ped. So it guaranteed has to be ped. 0 just may mean to use your ped by default for some reason.  
```

```
NativeDB Added Parameter 5: Any p4
NativeDB Added Parameter 6: Any p5
```

---
### TaskToggleDuck

`TASK_TOGGLE_DUCK` · hash `0xAC96609B9995EDF8` · jhash `0x61CFBCBF` · **Cliente**

```lua
TaskToggleDuck(p0, p1)
```
```c
void TASK_TOGGLE_DUCK(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
used in sequence task  
both parameters seems to be always 0  
```

---
### TaskTurnPedToFaceCoord

`TASK_TURN_PED_TO_FACE_COORD` · hash `0x1DDA930A0AC38571` · jhash `0x30463D73` · **Cliente**

```lua
TaskTurnPedToFaceCoord(ped, x, y, z, duration)
```
```c
void TASK_TURN_PED_TO_FACE_COORD(Ped ped, float x, float y, float z, int duration);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `duration` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
duration in milliseconds  
```

---
### TaskTurnPedToFaceEntity

`TASK_TURN_PED_TO_FACE_ENTITY` · hash `0x5AD23D40115353AC` · jhash `0x3C37C767` · **Cliente**

```lua
TaskTurnPedToFaceEntity(ped, entity, duration)
```
```c
void TASK_TURN_PED_TO_FACE_ENTITY(Ped ped, Entity entity, int duration);
```

**Parámetros**

- `ped` (`Ped`)
- `entity` (`Entity`)
- `duration` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
duration: the amount of time in milliseconds to do the task. -1 will keep the task going until either another task is applied, or CLEAR_ALL_TASKS() is called with the ped  
```

---
### TaskUseMobilePhone

`TASK_USE_MOBILE_PHONE` · hash `0xBD2A8EC3AF4DE7DB` · jhash `0x225A38C8` · **Cliente**

```lua
TaskUseMobilePhone(ped, p1)
```
```c
void TASK_USE_MOBILE_PHONE(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Actually has 3 params, not 2.  
p0: Ped  
p1: int (or bool?)  
p2: int  
```

```
NativeDB Added Parameter 3: Any p2
```

---
### TaskUseMobilePhoneTimed

`TASK_USE_MOBILE_PHONE_TIMED` · hash `0x5EE02954A14C69DB` · jhash `0xC99C19F5` · **Cliente**

```lua
TaskUseMobilePhoneTimed(ped, duration)
```
```c
void TASK_USE_MOBILE_PHONE_TIMED(Ped ped, int duration);
```

**Parámetros**

- `ped` (`Ped`)
- `duration` (`int`)

**Devuelve:** `void`

---
### TaskUseNearestScenarioChainToCoord

`TASK_USE_NEAREST_SCENARIO_CHAIN_TO_COORD` · hash `0x9FDA1B3D7E7028B3` · jhash `0xE32FFB22` · **Cliente**

```lua
TaskUseNearestScenarioChainToCoord(p0, p1, p2, p3, p4, p5)
```
```c
void TASK_USE_NEAREST_SCENARIO_CHAIN_TO_COORD(Any p0, float p1, float p2, float p3, float p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`Any`)

**Devuelve:** `void`

---
### TaskUseNearestScenarioChainToCoordWarp

`TASK_USE_NEAREST_SCENARIO_CHAIN_TO_COORD_WARP` · hash `0x97A28E63F0BA5631` · jhash `0xBAB4C0AE` · **Cliente**

```lua
TaskUseNearestScenarioChainToCoordWarp(p0, p1, p2, p3, p4, p5)
```
```c
void TASK_USE_NEAREST_SCENARIO_CHAIN_TO_COORD_WARP(Any p0, float p1, float p2, float p3, float p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`Any`)

**Devuelve:** `void`

---
### TaskUseNearestScenarioToCoord

`TASK_USE_NEAREST_SCENARIO_TO_COORD` · hash `0x277F471BA9DB000B` · jhash `0x9C50FBF0` · **Cliente**

```lua
TaskUseNearestScenarioToCoord(ped, x, y, z, distance, duration)
```
```c
void TASK_USE_NEAREST_SCENARIO_TO_COORD(Ped ped, float x, float y, float z, float distance, int duration);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `distance` (`float`)
- `duration` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Updated variables
An alternative to TASK::TASK_USE_NEAREST_SCENARIO_TO_COORD_WARP. Makes the ped walk to the scenario instead.
```

---
### TaskUseNearestScenarioToCoordWarp

`TASK_USE_NEAREST_SCENARIO_TO_COORD_WARP` · hash `0x58E2E0F23F6B76C3` · jhash `0x1BE9D65C` · **Cliente**

```lua
TaskUseNearestScenarioToCoordWarp(ped, x, y, z, radius, p5)
```
```c
void TASK_USE_NEAREST_SCENARIO_TO_COORD_WARP(Ped ped, float x, float y, float z, float radius, Any p5);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p5` (`Any`)

**Devuelve:** `void`

---
### TaskVehicleAimAtCoord

`TASK_VEHICLE_AIM_AT_COORD` · hash `0x447C1E9EF844BC0F` · jhash `0x010F47CE` · **Cliente**

```lua
TaskVehicleAimAtCoord(ped, x, y, z)
```
```c
void TASK_VEHICLE_AIM_AT_COORD(Ped ped, float x, float y, float z);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### TaskVehicleAimAtPed

`TASK_VEHICLE_AIM_AT_PED` · hash `0xE41885592B08B097` · jhash `0x920AE6DB` · **Cliente**

```lua
TaskVehicleAimAtPed(ped, target)
```
```c
void TASK_VEHICLE_AIM_AT_PED(Ped ped, Ped target);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)

**Devuelve:** `void`

---
### TaskVehicleChase

`TASK_VEHICLE_CHASE` · hash `0x3C08A8E30363B353` · jhash `0x55634798` · **Cliente**

```lua
TaskVehicleChase(driver, targetEnt)
```
```c
void TASK_VEHICLE_CHASE(Ped driver, Entity targetEnt);
```

**Parámetros**

- `driver` (`Ped`)
- `targetEnt` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
chases targetEnt fast and aggressively  
--  
Makes ped (needs to be in vehicle) chase targetEnt.  
```

---
### TaskVehicleDriveToCoord

`TASK_VEHICLE_DRIVE_TO_COORD` · hash `0xE2A2AA2F659D77A7` · jhash `0xE4AC0387` · **Cliente**

```lua
TaskVehicleDriveToCoord(ped, vehicle, x, y, z, speed, p6, vehicleModel, drivingMode, stopRange, p10)
```
```c
void TASK_VEHICLE_DRIVE_TO_COORD(Ped ped, Vehicle vehicle, float x, float y, float z, float speed, Any p6, Hash vehicleModel, int drivingMode, float stopRange, float p10);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `speed` (`float`)
- `p6` (`Any`)
- `vehicleModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `drivingMode` (`int`)
- `stopRange` (`float`)
- `p10` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
info about driving modes: HTTP://gtaforums.com/topic/822314-guide-driving-styles/  
---------------------------------------------------------------  
Passing P6 value as floating value didn't throw any errors, though unsure what is it exactly, looks like radius or something.  
P10 though, it is mentioned as float, however, I used bool and set it to true, that too worked.  
Here the e.g. code I used  
Function.Call(Hash.TASK_VEHICLE_DRIVE_TO_COORD, Ped, Vehicle, Cor X, Cor Y, Cor Z, 30f, 1f, Vehicle.GetHashCode(), 16777216, 1f, true);  
```

---
### TaskVehicleDriveToCoordLongrange

`TASK_VEHICLE_DRIVE_TO_COORD_LONGRANGE` · hash `0x158BB33F920D360C` · jhash `0x1490182A` · **Cliente**

```lua
TaskVehicleDriveToCoordLongrange(ped, vehicle, x, y, z, speed, drivingStyle, stopRange)
```
```c
void TASK_VEHICLE_DRIVE_TO_COORD_LONGRANGE(Ped ped, Vehicle vehicle, float x, float y, float z, float speed, int drivingStyle, float stopRange);
```

**Parámetros**

- `ped` (`Ped`): Ped id for the task.
- `vehicle` (`Vehicle`): Vehicle entity id for the task.
- `x` (`float`): Destination X coordinate.
- `y` (`float`): Destination Y coordinate.
- `z` (`float`): Destination Z coordinate.
- `speed` (`float`): Speed of driving.
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).
- `stopRange` (`float`): Stops in the specific range near the destination. 20.0 works fine.

**Devuelve:** `void`

**Descripción oficial:**

You can let your character drive to the destination at the speed and driving style you set. You can use map marks to set the destination.

```cpp
enum eDriveBehaviorFlags {
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
  DF_UseWanderFallbackInsteadOfStraightLine = 2048,
  DF_AvoidRestrictedAreas = 4096,
  DF_PreventBackgroundPathfinding = 8192, // **These only work on MISSION_CRUISE**
  DF_AdjustCruiseSpeedBasedOnRoadSpeed = 16384,
  DF_UseShortCutLinks = 262144,
  DF_ChangeLanesAroundObstructions = 524288,
  DF_UseSwitchedOffNodes = 2097152,	//cruise tasks ignore this anyway--only used for goto's
  DF_PreferNavmeshRoute = 4194304,	//if you're going to be primarily driving off road
  DF_PlaneTaxiMode = 8388608, // Only works for planes using MISSION_GOTO, will cause them to drive along the ground instead of fly
  DF_ForceStraightLine = 16777216,
  DF_UseStringPullingAtJunctions = 33554432,
  DF_AvoidHighways = 536870912,
  DF_ForceJoinInRoadDirection = 1073741824
}
```

**Ejemplo (cs):**

```cs
// A short example showcasing how this native works with map marks.

// Get the map mark location.
Vector3 destination = GetBlipInfoIdCoord(GetFirstBlipInfoId(8));

// If no mark is set, return immediately.
if (destination == Vector3.Zero)
{
    return;
}

TaskVehicleDriveToCoordLongrange(Game.PlayerPed.Handle, Game.PlayerPed.CurrentVehicle.Handle, destination.X, destination.Y, destination.Z, 60f, 447, 20f);
```

---
### TaskVehicleDriveWander

`TASK_VEHICLE_DRIVE_WANDER` · hash `0x480142959D337D00` · jhash `0x36EC0EB0` · **Cliente**

```lua
TaskVehicleDriveWander(ped, vehicle, speed, drivingStyle)
```
```c
void TASK_VEHICLE_DRIVE_WANDER(Ped ped, Vehicle vehicle, float speed, int drivingStyle);
```

**Parámetros**

- `ped` (`Ped`): Ped id for the task.
- `vehicle` (`Vehicle`): Vehicle entity id for the task.
- `speed` (`float`): Speed of driving.
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).

**Devuelve:** `void`

**Descripción oficial:**

Drive randomly with no destination set.

**Ejemplo (cs):**

```cs
TaskVehicleDriveWander(Game.PlayerPed.Handle, Game.PlayerPed.CurrentVehicle.Handle, 60f, 447);
```

---
### TaskVehicleEscort

`TASK_VEHICLE_ESCORT` · hash `0x0FA6E4B75F302400` · jhash `0x9FDCB250` · **Cliente**

```lua
TaskVehicleEscort(ped, vehicle, targetVehicle, mode, speed, drivingStyle, minDistance, p7, noRoadsDistance)
```
```c
void TASK_VEHICLE_ESCORT(Ped ped, Vehicle vehicle, Vehicle targetVehicle, int mode, float speed, int drivingStyle, float minDistance, int p7, float noRoadsDistance);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `targetVehicle` (`Vehicle`)
- `mode` (`int`)
- `speed` (`float`)
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).
- `minDistance` (`float`)
- `p7` (`int`)
- `noRoadsDistance` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes a ped follow the targetVehicle with <minDistance> in between.  
note: minDistance is ignored if drivingstyle is avoiding traffic, but Rushed is fine.  
Mode: The mode defines the relative position to the targetVehicle. The ped will try to position its vehicle there.  
-1 = behind  
0 = ahead  
1 = left  
2 = right  
3 = back left  
4 = back right  
if the target is closer than noRoadsDistance, the driver will ignore pathing/roads and follow you directly.  
Driving Styles guide: gtaforums.com/topic/822314-guide-driving-styles/  
```

---
### TaskVehicleFollow

`TASK_VEHICLE_FOLLOW` · hash `0xFC545A9F0626E3B6` · jhash `0xA8B917D7` · **Cliente**

```lua
TaskVehicleFollow(driver, vehicle, targetEntity, speed, drivingStyle, minDistance)
```
```c
void TASK_VEHICLE_FOLLOW(Ped driver, Vehicle vehicle, Entity targetEntity, float speed, int drivingStyle, int minDistance);
```

**Parámetros**

- `driver` (`Ped`)
- `vehicle` (`Vehicle`)
- `targetEntity` (`Entity`)
- `speed` (`float`)
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).
- `minDistance` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes a ped in a vehicle follow an entity (ped, vehicle, etc.)
drivingStyle: http://gtaforums.com/topic/822314-guide-driving-styles/
```

**Nombres antiguos (alias):** `_TASK_VEHICLE_FOLLOW` (`TaskVehicleFollow`)

---
### TaskVehicleFollowWaypointRecording

`TASK_VEHICLE_FOLLOW_WAYPOINT_RECORDING` · hash `0x3123FAA6DB1CF7ED` · jhash `0x959818B6` · **Cliente**

```lua
TaskVehicleFollowWaypointRecording(ped, vehicle, WPRecording, p3, p4, p5, p6, p7, p8, p9)
```
```c
void TASK_VEHICLE_FOLLOW_WAYPOINT_RECORDING(Ped ped, Vehicle vehicle, char* WPRecording, int p3, int p4, int p5, int p6, float p7, BOOL p8, float p9);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `WPRecording` (`char*`)
- `p3` (`int`)
- `p4` (`int`)
- `p5` (`int`)
- `p6` (`int`)
- `p7` (`float`)
- `p8` (`BOOL`)
- `p9` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
task_vehicle_follow_waypoint_recording(Ped p0, Vehicle p1, string p2, int p3, int p4, int p5, int p6, float.x p7, float.Y p8, float.Z p9, bool p10, int p11)
p2 = Waypoint recording string (found in update\update.rpf\x64\levels\gta5\waypointrec.rpf
p3 = 786468
p4 = 0
p5 = 16
p6 = -1 (angle?)
p7/8/9 = usually v3.zero
p10 = bool (repeat?)
p11 = 1073741824
-khorio
```

---
### TaskVehicleGotoNavmesh

`TASK_VEHICLE_GOTO_NAVMESH` · hash `0x195AEEB13CEFE2EE` · jhash `0x55CF3BCD` · **Cliente**

```lua
TaskVehicleGotoNavmesh(ped, vehicle, x, y, z, speed, behaviorFlag, stoppingRange)
```
```c
void TASK_VEHICLE_GOTO_NAVMESH(Ped ped, Vehicle vehicle, float x, float y, float z, float speed, int behaviorFlag, float stoppingRange);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `speed` (`float`)
- `behaviorFlag` (`int`)
- `stoppingRange` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Differs from TASK_VEHICLE_DRIVE_TO_COORDS in that it will pick the shortest possible road route without taking one-way streets and other "road laws" into consideration.  
WARNING:  
A behaviorFlag value of 0 will result in a clunky, stupid driver!  
Recommended settings:  
speed = 30.0f,  
behaviorFlag = 156,   
stoppingRange = 5.0f;  
If you simply want to have your driver move to a fixed location, call it only once, or, when necessary in the event of interruption.   
If using this to continually follow a Ped who is on foot:  You will need to run this in a tick loop.  Call it in with the Ped's updated coordinates every 20 ticks or so and you will have one hell of a smart, fast-reacting NPC driver -- provided he doesn't get stuck.  If your update frequency is too fast, the Ped may not have enough time to figure his way out of being stuck, and thus, remain stuck.  One way around this would be to implement an "anti-stuck" mechanism, which allows the driver to realize he's stuck, temporarily pause the tick, unstuck, then resume the tick.  
EDIT:  This is being discussed in more detail at http://gtaforums.com/topic/818504-any-idea-on-how-to-make-peds-clever-and-insanely-fast-c/  
```

---
### TaskVehicleHeliProtect

`TASK_VEHICLE_HELI_PROTECT` · hash `0x1E09C32048FEFD1C` · jhash `0x0CB415EE` · **Cliente**

```lua
TaskVehicleHeliProtect(pilot, vehicle, entityToFollow, targetSpeed, p4, radius, altitude, p7)
```
```c
void TASK_VEHICLE_HELI_PROTECT(Ped pilot, Vehicle vehicle, Entity entityToFollow, float targetSpeed, int p4, float radius, int altitude, int p7);
```

**Parámetros**

- `pilot` (`Ped`)
- `vehicle` (`Vehicle`)
- `entityToFollow` (`Entity`)
- `targetSpeed` (`float`)
- `p4` (`int`)
- `radius` (`float`)
- `altitude` (`int`)
- `p7` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
pilot, vehicle and altitude are rather self-explanatory.  
p4: is unused variable in the function.  
entityToFollow: you can provide a Vehicle entity or a Ped entity, the heli will protect them.  
'targetSpeed':  The pilot will dip the nose AS MUCH AS POSSIBLE so as to reach this value AS FAST AS POSSIBLE.  As such, you'll want to modulate it as opposed to calling it via a hard-wired, constant #.  
'radius' isn't just "stop within radius of X of target" like with ground vehicles.  In this case, the pilot will fly an entire circle around 'radius' and continue to do so.  
NOT CONFIRMED:  p7 appears to be a FlyingStyle enum.  Still investigating it as of this writing, but playing around with values here appears to result in different -behavior- as opposed to offsetting coordinates, altitude, target speed, etc.  
NOTE: If the pilot finds enemies, it will engage them until it kills them, but will return to protect the ped/vehicle given shortly thereafter.  
```

---
### TaskVehicleMission

`TASK_VEHICLE_MISSION` · hash `0x659427E0EF36BCDE` · jhash `0x20609E56` · **Cliente**

```lua
TaskVehicleMission(ped, vehicle, vehicleTarget, missionType, speed, drivingStyle, radius, straightLineDist, DriveAgainstTraffic)
```
```c
void TASK_VEHICLE_MISSION(Ped ped, Vehicle vehicle, Vehicle vehicleTarget, int missionType, float speed, int drivingStyle, float radius, float straightLineDist, BOOL DriveAgainstTraffic);
```

**Parámetros**

- `ped` (`Ped`): The ped to be tasked.
- `vehicle` (`Vehicle`): The vehicles' entity handle.
- `vehicleTarget` (`Vehicle`): The target vehicle.
- `missionType` (`int`): The mission type (default is 0) (see `eVehicleMissionType`).
- `speed` (`float`): The speed in m/s.
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).
- `radius` (`float`): The radius of when the task will be completed (default is -1.0f).
- `straightLineDist` (`float`): The distance before the vehicle will drive straight to the target (default is -1.0f).
- `DriveAgainstTraffic` (`BOOL`): Whether the vehicle should drive against traffic (default is false).

**Devuelve:** `void`

**Descripción oficial:**

All parameters except ped, vehicle, vehicleTarget and speed are optional; with `missionType` being only those that require a target entity.

If you don't want to use a parameter; pass `0` for int parameters, and `-1.0f` for the remaining float parameters.

```cpp
enum eVehicleMissionType
{
  None = 0,
  Cruise = 1,
  Ram = 2,
  Block = 3,
  GoTo = 4,
  Stop = 5,
  Attack = 6,
  Follow = 7,
  Flee = 8,
  Circle = 9,
  Escort = 12,
  GoToRacing = 14,
  FollowRecording = 15,
  PoliceBehaviour = 16,
  Land = 19,
  LandAndWait = 20,
  Crash = 21,
  PullOver = 22,
  HeliProtect = 23
}
```

**Ejemplo (lua):**

```lua
local vehicle_model = `adder`
RequestModel(vehicle_model)
repeat Wait(0) until HasModelLoaded(vehicle_model)

-- Player needs in a vehicle for this to work
local ped = PlayerPedId()
local coords = GetEntityCoords(ped) - GetEntityForwardVector(ped) * 15.0
local vehicle = CreateVehicle(vehicle_model, coords.x, coords.y, coords.z, GetEntityHeading(ped), true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(vehicle_model)

local ped_model = `a_m_m_skater_01`
RequestModel(ped_model)
repeat Wait(0) until HasModelLoaded(ped_model)

local driver = CreatePedInsideVehicle(vehicle, 0, ped_model, -1, true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(ped_model)

TaskVehicleMission(driver, vehicle, GetVehiclePedIsIn(ped, false), 8, 35.0, 786468, -1.0, -1.0, true)
-- Mission Type: Flee | Drive Style: DrivingModeAvoidVehiclesReckless
SetPedKeepTask(driver, true)
```

---
### TaskVehicleMissionCoorsTarget

`TASK_VEHICLE_MISSION_COORS_TARGET` · hash `0xF0AF20AA7731F8C3` · jhash `0x6719C109` · **Cliente**

```lua
TaskVehicleMissionCoorsTarget(ped, vehicle, x, y, z, missionType, speed, drivingStyle, radius, straightLineDist, DriveAgainstTraffic)
```
```c
void TASK_VEHICLE_MISSION_COORS_TARGET(Ped ped, Vehicle vehicle, float x, float y, float z, int missionType, float speed, int drivingStyle, float radius, float straightLineDist, BOOL DriveAgainstTraffic);
```

**Parámetros**

- `ped` (`Ped`): The ped to be tasked.
- `vehicle` (`Vehicle`): The vehicles' entity handle.
- `x` (`float`): The x coordinate.
- `y` (`float`): The y coordinate.
- `z` (`float`): The z coordinate.
- `missionType` (`int`): The mission type (default is 0) (see [TaskVehicleMission](#taskvehiclemission)).
- `speed` (`float`): The speed in m/s.
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).
- `radius` (`float`): The radius of when the task will be completed (default is -1.0f).
- `straightLineDist` (`float`): The distance before the vehicle will drive straight to the target (default is -1.0f).
- `DriveAgainstTraffic` (`BOOL`): Whether the vehicle should drive against traffic (default is false).

**Devuelve:** `void`

**Descripción oficial:**

All parameters except ped, vehicle, x, y, z and speed are optional; with `missionType` being only those that don't require a target entity.

If you don't want to use a parameter; pass `0` for int parameters, and `-1.0f` for the remaining float parameters.

**Ejemplo (lua):**

```lua
local vehicle_model = `adder`
RequestModel(vehicle_model)
repeat Wait(0) until HasModelLoaded(vehicle_model)

local ped = PlayerPedId()
local coords = GetEntityCoords(ped)
local spawn_coords = coords - GetEntityForwardVector(ped) * 15.0
local vehicle = CreateVehicle(vehicle_model, spawn_coords.x, spawn_coords.y, spawn_coords.z, GetEntityHeading(ped), true, false)

-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(vehicle_model)

local ped_model = `a_m_m_skater_01`
RequestModel(ped_model)
repeat Wait(0) until HasModelLoaded(ped_model)

local driver = CreatePedInsideVehicle(vehicle, 0, ped_model, -1, true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(ped_model)

TaskVehicleMissionCoorsTarget(driver, vehicle, coords.x, coords.y, coords.z, 8, 35.0, 786468, -1.0, -1.0, true)
-- Mission Type: Flee | Drive Style: DrivingModeAvoidVehiclesReckless
SetPedKeepTask(driver, true)
```

---
### TaskVehicleMissionPedTarget

`TASK_VEHICLE_MISSION_PED_TARGET` · hash `0x9454528DF15D657A` · jhash `0xC81C4677` · **Cliente**

```lua
TaskVehicleMissionPedTarget(ped, vehicle, pedTarget, missionType, speed, drivingStyle, radius, straightLineDist, DriveAgainstTraffic)
```
```c
void TASK_VEHICLE_MISSION_PED_TARGET(Ped ped, Vehicle vehicle, Ped pedTarget, int missionType, float speed, int drivingStyle, float radius, float straightLineDist, BOOL DriveAgainstTraffic);
```

**Parámetros**

- `ped` (`Ped`): The ped to be tasked.
- `vehicle` (`Vehicle`): The vehicles' entity handle.
- `pedTarget` (`Ped`): The target ped.
- `missionType` (`int`): The mission type (default is 0) (see [TaskVehicleMission](#taskvehiclemission)).
- `speed` (`float`): The speed in m/s.
- `drivingStyle` (`int`): The driving style (default is 0) (see [SetDriveTaskDrivingStyle](#setdrivetaskdrivingstyle)).
- `radius` (`float`): The radius of when the task will be completed (default is -1.0f).
- `straightLineDist` (`float`): The distance before the vehicle will drive straight to the target (default is -1.0f).
- `DriveAgainstTraffic` (`BOOL`): Whether the vehicle should drive against traffic (default is false).

**Devuelve:** `void`

**Descripción oficial:**

All parameters except ped, vehicle, pedTarget and speed are optional; with `missionType` being only those that require a target entity.

If you don't want to use a parameter; pass `0` for int parameters, and `-1.0f` for the remaining float parameters.

**Ejemplo (lua):**

```lua
local vehicle_model = `adder`
RequestModel(vehicle_model)
repeat Wait(0) until HasModelLoaded(vehicle_model)

local ped = PlayerPedId()
local coords = GetEntityCoords(ped) - GetEntityForwardVector(ped) * 15.0
local vehicle = CreateVehicle(vehicle_model, coords.x, coords.y, coords.z, GetEntityHeading(ped), true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(vehicle_model)

local ped_model = `a_m_m_skater_01`
RequestModel(ped_model)
repeat Wait(0) until HasModelLoaded(ped_model)

local driver = CreatePedInsideVehicle(vehicle, 0, ped_model, -1, true, false)
-- Allow the game engine to clear the model from memory
SetModelAsNoLongerNeeded(ped_model)

TaskVehicleMissionPedTarget(driver, vehicle, ped, 8, 35.0, 786468, -1.0, -1.0, true)
-- Mission Type: Flee | Drive Style: DrivingModeAvoidVehiclesReckless
SetPedKeepTask(driver, true)
```

---
### TaskVehiclePark

`TASK_VEHICLE_PARK` · hash `0x0F3E34E968EA374E` · jhash `0x5C85FF90` · **Cliente**

```lua
TaskVehiclePark(ped, vehicle, x, y, z, heading, mode, radius, keepEngineOn)
```
```c
void TASK_VEHICLE_PARK(Ped ped, Vehicle vehicle, float x, float y, float z, float heading, int mode, float radius, BOOL keepEngineOn);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `mode` (`int`)
- `radius` (`float`)
- `keepEngineOn` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Modes:  
0 - ignore heading  
1 - park forward  
2 - park backwards  
Depending on the angle of approach, the vehicle can park at the specified heading or at its exact opposite (-180) angle.  
Radius seems to define how close the vehicle has to be -after parking- to the position for this task considered completed. If the value is too small, the vehicle will try to park again until it's exactly where it should be. 20.0 Works well but lower values don't, like the radius is measured in centimeters or something.  
```

---
### TaskVehiclePlayAnim

`TASK_VEHICLE_PLAY_ANIM` · hash `0x69F5C3BD0F3EBD89` · jhash `0x2B28F598` · **Cliente**

```lua
TaskVehiclePlayAnim(vehicle, animationSet, animationName)
```
```c
void TASK_VEHICLE_PLAY_ANIM(Vehicle vehicle, char* animationSet, char* animationName);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `animationSet` (`char*`)
- `animationName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Most probably plays a specific animation on vehicle. For example getting chop out of van etc...
Here's how its used -
TASK::TASK_VEHICLE_PLAY_ANIM(l_325, "rcmnigel1b", "idle_speedo");
TASK::TASK_VEHICLE_PLAY_ANIM(l_556[0/*1*/], "missfra0_chop_drhome", "InCar_GetOutofBack_Speedo");
FYI : Speedo is the name of van in which chop was put in the mission.
```

---
### TaskVehicleShootAtCoord

`TASK_VEHICLE_SHOOT_AT_COORD` · hash `0x5190796ED39C9B6D` · jhash `0xA7AAA4D6` · **Cliente**

```lua
TaskVehicleShootAtCoord(ped, x, y, z, p4)
```
```c
void TASK_VEHICLE_SHOOT_AT_COORD(Ped ped, float x, float y, float z, float p4);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

---
### TaskVehicleShootAtPed

`TASK_VEHICLE_SHOOT_AT_PED` · hash `0x10AB107B887214D8` · jhash `0x59677BA0` · **Cliente**

```lua
TaskVehicleShootAtPed(ped, target, p2)
```
```c
void TASK_VEHICLE_SHOOT_AT_PED(Ped ped, Ped target, float p2);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)
- `p2` (`float`)

**Devuelve:** `void`

---
### TaskVehicleTempAction

`TASK_VEHICLE_TEMP_ACTION` · hash `0xC429DCEEB339E129` · jhash `0x0679DFB8` · **Cliente**

```lua
TaskVehicleTempAction(driver, vehicle, action, time)
```
```c
void TASK_VEHICLE_TEMP_ACTION(Ped driver, Vehicle vehicle, int action, int time);
```

**Parámetros**

- `driver` (`Ped`): The vehicle driver (`Ped`).
- `vehicle` (`Vehicle`): The vehicle handle.
- `action` (`int`): The temporary action, see `eTempAction`.
- `time` (`int`): The time to run this temp action for, use `-1` for infinite. Time is in milliseconds.

**Devuelve:** `void`

**Descripción oficial:**

Gives the vehicle a temporary action.

**Note**: For migrating objects, a `CScriptEntityStateChangeEvent` will be sent over the network to let other clients know that this object is being given a temporary action. At the same time, temporary actions cannot be applied to clones/remote objects.

```cpp
enum eTempAction {
    TA_NONE = 0,
    TA_WAIT = 1,
    TA_UNUSED = 2,
    TA_BRAKE_REVERSE = 3,
    TA_HANDBRAKE_TURN_LEFT = 4,
    TA_HANDBRAKE_TURN_RIGHT = 5,
    TA_HANDBRAKE_UNTIL_TIME_ENDS = 6,
    TA_TURN_LEFT = 7,
    TA_TURN_RIGHT = 8,
    TA_ACCELERATE = 9,
    TA_TURN_LEFT = 10,
    TA_TURN_RIGHT = 11,
    TA_UNUSED_12 = 12,
    TA_TURN_LEFT_GO_REVERSE = 13,
    TA_TURN_RIGHT_GO_REVERSE = 14,
    TA_PLANE_FLY_UP = 15, // (crashes game if not in plane)
    TA_PLANE_FLY_STRAIGHT = 16, // (crashes game if not in plane)
    TA_PLANE_SHARP_LEFT = 17, // (crashes game if not in plane)
    TA_PLANE_SHARP_RIGHT = 18, // (crashes game if not in plane)
    TA_STRONG_BRAKE = 19,
    TA_TURN_LEFT_AND_STOP = 20,
    TA_TURN_RIGHT_AND_STOP = 21,
    TA_GO_IN_REVERSE = 22,
    TA_ACCELERATE_FAST = 23,
    TA_BRAKE_ACTION = 24,
    TA_HANDBRAKE_TURN_LEFT_MORE = 25,
    TA_HANDBRAKE_TURN_RIGHT_MORE = 26,
    TA_HANDBRAKE_BRAKE_STRAIGHT = 27,
    TA_BRAKE_STRONG_REVERSE_ACCELERATION = 28,
    TA_UNUSED_29 = 29,
    TA_PERFORMS_BURNOUT = 30,
    TA_REV_ENGINE = 31,
    TA_ACCELERATE_VERY_STRONG = 32,
    TA_SURFACE_IN_SUBMARINE = 33
};
```

---
### TaskWanderInArea

`TASK_WANDER_IN_AREA` · hash `0xE054346CA3A0F315` · jhash `0xC6981FB9` · **Cliente**

```lua
TaskWanderInArea(ped, x, y, z, radius, minimalLength, timeBetweenWalks)
```
```c
void TASK_WANDER_IN_AREA(Ped ped, float x, float y, float z, float radius, int minimalLength, float timeBetweenWalks);
```

**Parámetros**

- `ped` (`Ped`): The ped which will wander the area.
- `x` (`float`): The X coordinate.
- `y` (`float`): The Y coordinate
- `z` (`float`): The Z coordinate
- `radius` (`float`): The radius of the area to wander around in
- `minimalLength` (`int`): The minimal length it will wander before waiting timeBetweenWalks seconds before continuing
- `timeBetweenWalks` (`float`): The length of time the ped will stand still/rest between walks

**Devuelve:** `void`

**Descripción oficial:**

Makes a ped wander/patrol around the specified area.

The ped will continue to wander after getting distracted, but only if this additional task is temporary, ie. killing a target, after killing the target it will continue to wander around.

Use `GetIsTaskActive(ped, 222)` to check if the ped is still wandering the area.

**Ejemplo (lua):**

```lua
-- Load model for panther
local model = `a_c_panther`
RequestModel(model)
while not HasModelLoaded(model) do
  Citizen.Wait(0)
end

-- Spawn a panther at current coordinates
local coords = GetEntityCoords(PlayerPedId())
local ped = CreatePed(0, model, coords.x, coords.y, coords.z, 0.0, true)

-- Make sure the ped doesn't flee or gets distracted
SetBlockingOfNonTemporaryEvents(ped, true)

-- Make ped wander in spawned area with radius of 100 meters, will wander at least 2 meters and wait for around 10 seconds between patrols
TaskWanderInArea(ped, coords.x, coords.y, coords.z, 100.0, 2, 10.0)

-- Check if the ped is wandering
-- Tasks don't trigger instantly, so wait a bit before checking
Citizen.Wait(1000)
print(GetIsTaskActive(ped, 222)) -- 1
```

---
### TaskWanderSpecific

`_TASK_WANDER_SPECIFIC` · hash `0x6919A2F136426098` · **Cliente**

```lua
TaskWanderSpecific(p0, p1, p2, p3)
```
```c
void _TASK_WANDER_SPECIFIC(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### TaskWanderStandard

`TASK_WANDER_STANDARD` · hash `0xBB9CE077274F6A1B` · jhash `0xAF59151A` · **Cliente**

```lua
TaskWanderStandard(ped, p1, p2)
```
```c
void TASK_WANDER_STANDARD(Ped ped, float p1, int p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)
- `p2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes ped walk around the area.  
set p1 to 10.0f and p2 to 10 if you want the ped to walk anywhere without a duration.  
```

---
### TaskWarpPedDirectlyIntoCover

`TASK_WARP_PED_DIRECTLY_INTO_COVER` · hash `0x6E01E9E8D89F8276` · **Cliente**

```lua
TaskWarpPedDirectlyIntoCover(ped, time, canPeekAndAim, forceInitialFacingDirection, forceFaceLeft, coverIndex)
```
```c
void TASK_WARP_PED_DIRECTLY_INTO_COVER(Ped ped, int time, BOOL canPeekAndAim, BOOL forceInitialFacingDirection, BOOL forceFaceLeft, int coverIndex);
```

**Parámetros**

- `ped` (`Ped`): The ped to warp into cover.
- `time` (`int`): Duration in milliseconds the ped should take to enter the cover.
- `canPeekAndAim` (`BOOL`): If `true`, allows the ped to peek and aim while in cover.
- `forceInitialFacingDirection` (`BOOL`): If `true`, forces the ped to face the initial direction when entering cover.
- `forceFaceLeft` (`BOOL`): If `true`, forces the ped to face left relative to the cover position.
- `coverIndex` (`int`): The index of the cover point to warp the ped to. If `null`, the game will choose the nearest cover point.

**Devuelve:** `void`

**Descripción oficial:**

This task warps a ped directly into a cover position closest to the specified point. This can be used to quickly place peds in strategic positions during gameplay.

```
NativeDB Introduced: 2545
```

---
### TaskWarpPedIntoVehicle

`TASK_WARP_PED_INTO_VEHICLE` · hash `0x9A7D091411C5F684` · jhash `0x65D4A35D` · **Cliente · también en el servidor (RPC)**

```lua
TaskWarpPedIntoVehicle(ped, vehicle, seatIndex)
```
```c
void TASK_WARP_PED_INTO_VEHICLE(Ped ped, Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `ped` (`Ped`): The Ped to be warped into the vehicle.
- `vehicle` (`Vehicle`): The target vehicle into which the ped will be warped.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](VEHICLE-1.md#isvehicleseatfree).

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

Warp a ped into a vehicle.

**Note**: It's better to use [`TASK_ENTER_VEHICLE`](../cfx/servidor.md#taskentervehicle) with the flag "warp" flag instead of this native.

**Ejemplo (lua):**

```lua
-- This example creates a vehicle and warps the player into the driver's seat

-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Define the vehicle model and check if it exists in the game files
local modelHash = `adder`  -- Use Compile-time hashes to get the model hash
if not IsModelInCdimage(modelHash) then
    return
end

-- Request the model and wait for it to load
RequestModel(modelHash)  
repeat
    Wait(0)
until HasModelLoaded(modelHash)

-- Create the vehicle at the player's coordinates with a heading of 0.0
local coordsPlayer, heading = GetEntityCoords(playerPed), 0.0
local vehicle = CreateVehicle(modelHash, coordsPlayer, heading, true, false)

-- Define the seat index for the Ped (e.g., -1 for the driver's seat)
local seatIndex = -1  

-- Check if the vehicle exists and the player is alive
if not DoesEntityExist(vehicle) or IsEntityDead(playerPed) then
    return
end

-- Warp the Ped into the specified vehicle seat
TaskWarpPedIntoVehicle(playerPed, vehicle, seatIndex)
```

**Ejemplo (js):**

```js
// This example creates a vehicle and warps the player into the driver's seat

// Retrieve the player ped
const playerPed = PlayerPedId();

// Define the vehicle model and check if it exists in the game files
const modelHash = GetHashKey("adder");
if (!IsModelInCdimage(modelHash)) {
    return;
}

// Request the model and wait for it to load
RequestModel(modelHash);
while (!HasModelLoaded(modelHash)) {
    Wait(0);
}

// Create the vehicle at the player's coordinates with a heading of 0.0
const coordsPlayer = GetEntityCoords(playerPed);
const heading = 0.0;
const vehicle = CreateVehicle(modelHash, coordsPlayer, heading, true, false);

// Define the seat index for the Ped (e.g., -1 for the driver's seat)
const seatIndex = -1;

// Check if the vehicle exists and the player is alive
if (!DoesEntityExist(vehicle) || IsEntityDead(playerPed)) {
    return;
}

// Warp the Ped into the specified vehicle seat
TaskWarpPedIntoVehicle(playerPed, vehicle, seatIndex);
```

**Ejemplo (cs):**

```cs
// This example creates a vehicle and warps the player into the driver's seat
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
Ped playerPed = PlayerPedId();

// Define the vehicle model and check if it exists in the game files
uint modelHash = (uint)GetHashKey("adder");

if (!IsModelInCdimage(modelHash))
{
    return;
}

// Request the model and wait for it to load
RequestModel(modelHash);
while (!HasModelLoaded(modelHash))
{
    Delay(0);
}

// Create the vehicle at the player's coordinates with a heading of 0.0
Vector3 coordsPlayer = GetEntityCoords(playerPed);
float heading = 0.0f;
Vehicle vehicle = CreateVehicle(modelHash, coordsPlayer, heading, true, false);

// Define the seat index for the Ped (e.g., -1 for the driver's seat)
int seatIndex = -1;

// Check if the vehicle exists and the player is alive
if (!DoesEntityExist(vehicle) || IsEntityDead(playerPed))
{
    return;
}

// Warp the Ped into the specified vehicle seat
TaskWarpPedIntoVehicle(playerPed, vehicle, seatIndex);
```

---
### TaskWrithe

`TASK_WRITHE` · hash `0xCDDC2B77CE54AC6E` · jhash `0x0FDC54FC` · **Cliente**

```lua
TaskWrithe(ped, target, time, p3)
```
```c
void TASK_WRITHE(Ped ped, Ped target, int time, int p3);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)
- `time` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 5: Any p4
NativeDB Added Parameter 6: Any p5
```

---
### UncuffPed

`UNCUFF_PED` · hash `0x67406F2C8F87FC4F` · jhash `0xA23A1D61` · **Cliente**

```lua
UncuffPed(ped)
```
```c
void UNCUFF_PED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### UpdateTaskAimGunScriptedTarget

`UPDATE_TASK_AIM_GUN_SCRIPTED_TARGET` · hash `0x9724FB59A3E72AD0` · jhash `0x67E73525` · **Cliente**

```lua
UpdateTaskAimGunScriptedTarget(p0, p1, p2, p3, p4, p5)
```
```c
void UPDATE_TASK_AIM_GUN_SCRIPTED_TARGET(Ped p0, Ped p1, float p2, float p3, float p4, BOOL p5);
```

**Parámetros**

- `p0` (`Ped`)
- `p1` (`Ped`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `void`

---
### UpdateTaskHandsUpDuration

`UPDATE_TASK_HANDS_UP_DURATION` · hash `0xA98FCAFD7893C834` · jhash `0x3AA39BE9` · **Cliente**

```lua
UpdateTaskHandsUpDuration(ped, duration)
```
```c
void UPDATE_TASK_HANDS_UP_DURATION(Ped ped, int duration);
```

**Parámetros**

- `ped` (`Ped`)
- `duration` (`int`)

**Devuelve:** `void`

---
### UpdateTaskSweepAimEntity

`UPDATE_TASK_SWEEP_AIM_ENTITY` · hash `0xE4973DBDBE6E44B3` · jhash `0xF65F0F4F` · **Cliente**

```lua
UpdateTaskSweepAimEntity(ped, entity)
```
```c
void UPDATE_TASK_SWEEP_AIM_ENTITY(Ped ped, Entity entity);
```

**Parámetros**

- `ped` (`Ped`)
- `entity` (`Entity`)

**Devuelve:** `void`

---
### UpdateTaskSweepAimPosition

`UPDATE_TASK_SWEEP_AIM_POSITION` · hash `0xBB106883F5201FC4` · jhash `0x6345EC80` · **Cliente**

```lua
UpdateTaskSweepAimPosition(p0, p1, p2, p3)
```
```c
void UPDATE_TASK_SWEEP_AIM_POSITION(Any p0, float p1, float p2, float p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### UseWaypointRecordingAsAssistedMovementRoute

`USE_WAYPOINT_RECORDING_AS_ASSISTED_MOVEMENT_ROUTE` · hash `0x5A353B8E6B1095B5` · jhash `0x4DFD5FEC` · **Cliente**

```lua
UseWaypointRecordingAsAssistedMovementRoute(name, p1, p2, p3)
```
```c
void USE_WAYPOINT_RECORDING_AS_ASSISTED_MOVEMENT_ROUTE(char* name, BOOL p1, float p2, float p3);
```

**Parámetros**

- `name` (`char*`): Waypoint recording name.
- `p1` (`BOOL`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### VehicleWaypointPlaybackOverrideSpeed

`VEHICLE_WAYPOINT_PLAYBACK_OVERRIDE_SPEED` · hash `0x121F0593E0A431D7` · jhash `0xBE1E7BB4` · **Cliente**

```lua
VehicleWaypointPlaybackOverrideSpeed(vehicle, speed)
```
```c
void VEHICLE_WAYPOINT_PLAYBACK_OVERRIDE_SPEED(Vehicle vehicle, float speed);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `speed` (`float`)

**Devuelve:** `void`

---
### VehicleWaypointPlaybackPause

`VEHICLE_WAYPOINT_PLAYBACK_PAUSE` · hash `0x8A4E6AC373666BC5` · jhash `0x7C00B415` · **Cliente**

```lua
VehicleWaypointPlaybackPause(vehicle)
```
```c
void VEHICLE_WAYPOINT_PLAYBACK_PAUSE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### VehicleWaypointPlaybackResume

`VEHICLE_WAYPOINT_PLAYBACK_RESUME` · hash `0xDC04FCAA7839D492` · jhash `0xBEB14C82` · **Cliente**

```lua
VehicleWaypointPlaybackResume(vehicle)
```
```c
void VEHICLE_WAYPOINT_PLAYBACK_RESUME(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### VehicleWaypointPlaybackUseDefaultSpeed

`VEHICLE_WAYPOINT_PLAYBACK_USE_DEFAULT_SPEED` · hash `0x5CEB25A7D2848963` · jhash `0x923C3AA4` · **Cliente**

```lua
VehicleWaypointPlaybackUseDefaultSpeed(vehicle)
```
```c
void VEHICLE_WAYPOINT_PLAYBACK_USE_DEFAULT_SPEED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### WaypointPlaybackGetIsPaused

`WAYPOINT_PLAYBACK_GET_IS_PAUSED` · hash `0x701375A7D43F01CB` · jhash `0xA6BB5717` · **Cliente**

```lua
local retval = WaypointPlaybackGetIsPaused(p0)
```
```c
BOOL WAYPOINT_PLAYBACK_GET_IS_PAUSED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### WaypointPlaybackOverrideSpeed

`WAYPOINT_PLAYBACK_OVERRIDE_SPEED` · hash `0x7D7D2B47FA788E85` · jhash `0x23E6BA96` · **Cliente**

```lua
WaypointPlaybackOverrideSpeed(p0, p1, p2)
```
```c
void WAYPOINT_PLAYBACK_OVERRIDE_SPEED(Any p0, float p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### WaypointPlaybackPause

`WAYPOINT_PLAYBACK_PAUSE` · hash `0x0F342546AA06FED5` · jhash `0xFE39ECF8` · **Cliente**

```lua
WaypointPlaybackPause(p0, p1, p2)
```
```c
void WAYPOINT_PLAYBACK_PAUSE(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### WaypointPlaybackResume

`WAYPOINT_PLAYBACK_RESUME` · hash `0x244F70C84C547D2D` · jhash `0x50F392EF` · **Cliente**

```lua
WaypointPlaybackResume(p0, p1, p2, p3)
```
```c
void WAYPOINT_PLAYBACK_RESUME(Any p0, BOOL p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### WaypointPlaybackStartAimingAtCoord

`WAYPOINT_PLAYBACK_START_AIMING_AT_COORD` · hash `0x8968400D900ED8B3` · jhash `0xF120A34E` · **Cliente**

```lua
WaypointPlaybackStartAimingAtCoord(p0, p1, p2, p3, p4)
```
```c
void WAYPOINT_PLAYBACK_START_AIMING_AT_COORD(Any p0, float p1, float p2, float p3, BOOL p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`BOOL`)

**Devuelve:** `void`

---
### WaypointPlaybackStartAimingAtPed

`WAYPOINT_PLAYBACK_START_AIMING_AT_PED` · hash `0x20E330937C399D29` · jhash `0x75E60CF6` · **Cliente**

```lua
WaypointPlaybackStartAimingAtPed(p0, p1, p2)
```
```c
void WAYPOINT_PLAYBACK_START_AIMING_AT_PED(Any p0, Any p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### WaypointPlaybackStartShootingAtCoord

`WAYPOINT_PLAYBACK_START_SHOOTING_AT_COORD` · hash `0x057A25CFCC9DB671` · jhash `0xCDDB44D5` · **Cliente**

```lua
WaypointPlaybackStartShootingAtCoord(p0, p1, p2, p3, p4, p5)
```
```c
void WAYPOINT_PLAYBACK_START_SHOOTING_AT_COORD(Any p0, float p1, float p2, float p3, BOOL p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`BOOL`)
- `p5` (`Any`)

**Devuelve:** `void`

---
### WaypointPlaybackStartShootingAtPed

`WAYPOINT_PLAYBACK_START_SHOOTING_AT_PED` · hash `0xE70BA7B90F8390DC` · jhash `0xBD5F0EB8` · **Cliente**

```lua
WaypointPlaybackStartShootingAtPed(p0, p1, p2, p3)
```
```c
void WAYPOINT_PLAYBACK_START_SHOOTING_AT_PED(Any p0, Any p1, BOOL p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`BOOL`)
- `p3` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE70BA7B90F8390DC` (`N_0xe70ba7b90f8390dc`)

---
### WaypointPlaybackStopAimingOrShooting

`WAYPOINT_PLAYBACK_STOP_AIMING_OR_SHOOTING` · hash `0x47EFA040EBB8E2EA` · jhash `0x6D7CF40C` · **Cliente**

```lua
WaypointPlaybackStopAimingOrShooting(p0)
```
```c
void WAYPOINT_PLAYBACK_STOP_AIMING_OR_SHOOTING(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### WaypointPlaybackUseDefaultSpeed

`WAYPOINT_PLAYBACK_USE_DEFAULT_SPEED` · hash `0x6599D834B12D0800` · jhash `0x1BBB2CAC` · **Cliente**

```lua
WaypointPlaybackUseDefaultSpeed(p0)
```
```c
void WAYPOINT_PLAYBACK_USE_DEFAULT_SPEED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### WaypointRecordingGetClosestWaypoint

`WAYPOINT_RECORDING_GET_CLOSEST_WAYPOINT` · hash `0xB629A298081F876F` · jhash `0xC4CD35AF` · **Cliente**

```lua
local retval, point = WaypointRecordingGetClosestWaypoint(name, x, y, z, point)
```
```c
BOOL WAYPOINT_RECORDING_GET_CLOSEST_WAYPOINT(char* name, float x, float y, float z, int* point);
```

**Parámetros**

- `name` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `point` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
For a full list of the points, see here: goo.gl/wIH0vn
```

---
### WaypointRecordingGetCoord

`WAYPOINT_RECORDING_GET_COORD` · hash `0x2FB897405C90B361` · jhash `0x19266913` · **Cliente**

```lua
local retval, coord = WaypointRecordingGetCoord(name, point, coord)
```
```c
BOOL WAYPOINT_RECORDING_GET_COORD(char* name, int point, Vector3* coord);
```

**Parámetros**

- `name` (`char*`)
- `point` (`int`)
- `coord` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
For a full list of the points, see here: goo.gl/wIH0vn
```

---
### WaypointRecordingGetNumPoints

`WAYPOINT_RECORDING_GET_NUM_POINTS` · hash `0x5343532C01A07234` · jhash `0xF5F9B71E` · **Cliente**

```lua
local retval, points = WaypointRecordingGetNumPoints(name, points)
```
```c
BOOL WAYPOINT_RECORDING_GET_NUM_POINTS(char* name, int* points);
```

**Parámetros**

- `name` (`char*`)
- `points` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
For a full list of the points, see here: goo.gl/wIH0vn
```

---
### WaypointRecordingGetSpeedAtPoint

`WAYPOINT_RECORDING_GET_SPEED_AT_POINT` · hash `0x005622AEBC33ACA9` · jhash `0xC765633A` · **Cliente**

```lua
local retval = WaypointRecordingGetSpeedAtPoint(name, point)
```
```c
float WAYPOINT_RECORDING_GET_SPEED_AT_POINT(char* name, int point);
```

**Parámetros**

- `name` (`char*`)
- `point` (`int`)

**Devuelve:** `float`

---
