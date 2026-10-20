# Natives de GTA V — VEHICLE (parte 1 de 2: AddRoadNodeSpeedZone … SetNitrousIsActive)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `VEHICLE`: **751** natives.

Partes: **[1]** · [2](VEHICLE-2.md)

[← Índice de natives](../README.md)

## Índice de esta página

[`AddRoadNodeSpeedZone`](#addroadnodespeedzone) · [`AddVehicleCombatAngledAvoidanceArea`](#addvehiclecombatangledavoidancearea) · [`AddVehiclePhoneExplosiveDevice`](#addvehiclephoneexplosivedevice) · [`AddVehicleStuckCheckWithWarp`](#addvehiclestuckcheckwithwarp) · [`AddVehicleUpsidedownCheck`](#addvehicleupsidedowncheck) · [`AllowAmbientVehiclesToAvoidAdverseConditions`](#allowambientvehiclestoavoidadverseconditions) · [`AreAllVehicleWindowsIntact`](#areallvehiclewindowsintact) · [`AreAnyVehicleSeatsFree`](#areanyvehicleseatsfree) · [`AreBombBayDoorsOpen`](#arebombbaydoorsopen) · [`AreHeliStubWingsDeployed`](#arehelistubwingsdeployed) · [`AreOutriggerLegsDeployed`](#areoutriggerlegsdeployed) · [`ArePlaneControlPanelsIntact`](#areplanecontrolpanelsintact) · [`ArePlanePropellersIntact`](#areplanepropellersintact) · [`ArePlaneWingsIntact`](#areplanewingsintact) · [`AttachContainerToHandlerFrame`](#attachcontainertohandlerframe) · [`AttachEntityToCargobob`](#attachentitytocargobob) · [`AttachVehicleOnToTrailer`](#attachvehicleontotrailer) · [`AttachVehicleToCargobob`](#attachvehicletocargobob) · [`AttachVehicleToTowTruck`](#attachvehicletotowtruck) · [`AttachVehicleToTrailer`](#attachvehicletotrailer) · [`BringVehicleToHalt`](#bringvehicletohalt) · [`CanAnchorBoatHere`](#cananchorboathere) · [`CanAnchorBoatHereIgnorePlayers`](#cananchorboathereignoreplayers) · [`CanCargobobPickUpEntity`](#cancargobobpickupentity) · [`CanShuffleSeat`](#canshuffleseat) · [`ClearLastDrivenVehicle`](#clearlastdrivenvehicle) · [`ClearNitrous`](#clearnitrous) · [`ClearVehicleCustomPrimaryColour`](#clearvehiclecustomprimarycolour) · [`ClearVehicleCustomSecondaryColour`](#clearvehiclecustomsecondarycolour) · [`ClearVehicleGeneratorAreaOfInterest`](#clearvehiclegeneratorareaofinterest) · [`ClearVehiclePhoneExplosiveDevice`](#clearvehiclephoneexplosivedevice) · [`ClearVehicleRouteHistory`](#clearvehicleroutehistory) · [`CloseBombBayDoors`](#closebombbaydoors) · [`ControlLandingGear`](#controllandinggear) · [`CopyVehicleDamages`](#copyvehicledamages) · [`CreateMissionTrain`](#createmissiontrain) · [`CreatePickUpRopeForCargobob`](#createpickupropeforcargobob) · [`CreateScriptVehicleGenerator`](#createscriptvehiclegenerator) · [`CreateVehicle`](#createvehicle) · [`DeleteAllTrains`](#deletealltrains) · [`DeleteMissionTrain`](#deletemissiontrain) · [`DeleteScriptVehicleGenerator`](#deletescriptvehiclegenerator) · [`DeleteVehicle`](#deletevehicle) · [`DetachContainerFromHandlerFrame`](#detachcontainerfromhandlerframe) · [`DetachEntityFromCargobob`](#detachentityfromcargobob) · [`DetachVehicleFromAnyCargobob`](#detachvehiclefromanycargobob) · [`DetachVehicleFromAnyTowTruck`](#detachvehiclefromanytowtruck) · [`DetachVehicleFromCargobob`](#detachvehiclefromcargobob) · [`DetachVehicleFromTowTruck`](#detachvehiclefromtowtruck) · [`DetachVehicleFromTrailer`](#detachvehiclefromtrailer) · [`DetonateVehiclePhoneExplosiveDevice`](#detonatevehiclephoneexplosivedevice) · [`DisableIndividualPlanePropeller`](#disableindividualplanepropeller) · [`DisablePlaneAileron`](#disableplaneaileron) · [`DisableVehicleNeonLights`](#disablevehicleneonlights) · [`DisableVehicleTurretMovementThisFrame`](#disablevehicleturretmovementthisframe) · [`DisableVehicleWeapon`](#disablevehicleweapon) · [`DisableVehicleWorldCollision`](#disablevehicleworldcollision) · [`DoesCargobobHavePickUpRope`](#doescargobobhavepickuprope) · [`DoesCargobobHavePickupMagnet`](#doescargobobhavepickupmagnet) · [`DoesExtraExist`](#doesextraexist) · [`DoesScriptVehicleGeneratorExist`](#doesscriptvehiclegeneratorexist) · [`DoesVehicleAllowRappel`](#doesvehicleallowrappel) · [`DoesVehicleExistWithDecorator`](#doesvehicleexistwithdecorator) · [`DoesVehicleHaveLandingGear`](#doesvehiclehavelandinggear) · [`DoesVehicleHaveRoof`](#doesvehiclehaveroof) · [`DoesVehicleHaveSearchlight`](#doesvehiclehavesearchlight) · [`DoesVehicleHaveStuckVehicleCheck`](#doesvehiclehavestuckvehiclecheck) · [`DoesVehicleHaveWeapons`](#doesvehiclehaveweapons) · [`DoesVehicleTyreExist`](#doesvehicletyreexist) · [`EjectJb700Roof`](#ejectjb700roof) · [`EnableAircraftObstacleAvoidance`](#enableaircraftobstacleavoidance) · [`EnableIndividualPlanePropeller`](#enableindividualplanepropeller) · [`ExplodeVehicle`](#explodevehicle) · [`ExplodeVehicleInCutscene`](#explodevehicleincutscene) · [`FindRandomPointInSpace`](#findrandompointinspace) · [`FindVehicleCarryingThisEntity`](#findvehiclecarryingthisentity) · [`FixVehicleWindow`](#fixvehiclewindow) · [`ForcePlaybackRecordedVehicleUpdate`](#forceplaybackrecordedvehicleupdate) · [`ForceSubmarineNeurtalBuoyancy`](#forcesubmarineneurtalbuoyancy) · [`ForceSubmarineSurfaceMode`](#forcesubmarinesurfacemode) · [`FullyChargeNitrous`](#fullychargenitrous) · [`GetAllVehicles`](#getallvehicles) · [`GetBoatBoomPositionRatio`](#getboatboompositionratio) · [`GetBoatBoomPositionRatio_2`](#getboatboompositionratio_2) · [`GetBoatBoomPositionRatio_3`](#getboatboompositionratio_3) · [`GetBoatVehicleModelAgility`](#getboatvehiclemodelagility) · [`GetCanVehicleJump`](#getcanvehiclejump) · [`GetCargobobHookPosition`](#getcargobobhookposition) · [`GetClosestVehicle`](#getclosestvehicle) · [`GetConvertibleRoofState`](#getconvertibleroofstate) · [`GetCurrentPlaybackForVehicle`](#getcurrentplaybackforvehicle) · [`GetDisplayNameFromVehicleModel`](#getdisplaynamefromvehiclemodel) · [`GetDoesVehicleHaveTombstone`](#getdoesvehiclehavetombstone) · [`GetDriftTyresEnabled`](#getdrifttyresenabled) · [`GetEntityAttachedToCargobob`](#getentityattachedtocargobob) · [`GetEntityAttachedToTowTruck`](#getentityattachedtotowtruck) · [`GetEntryPositionOfDoor`](#getentrypositionofdoor) · [`GetHasRetractableWheels`](#gethasretractablewheels) · [`GetHasRocketBoost`](#gethasrocketboost) · [`GetHeliMainRotorHealth`](#gethelimainrotorhealth) · [`GetHeliTailBoomHealth`](#gethelitailboomhealth) · [`GetHeliTailRotorHealth`](#gethelitailrotorhealth) · [`GetHydraulicWheelValue`](#gethydraulicwheelvalue) · [`GetIsBoatCapsized`](#getisboatcapsized) · [`GetIsDoorValid`](#getisdoorvalid) · [`GetIsLeftVehicleHeadlightDamaged`](#getisleftvehicleheadlightdamaged) · [`GetIsRightVehicleHeadlightDamaged`](#getisrightvehicleheadlightdamaged) · [`GetIsVehicleElectric`](#getisvehicleelectric) · [`GetIsVehicleEmpDisabled`](#getisvehicleempdisabled) · [`GetIsVehicleEngineRunning`](#getisvehicleenginerunning) · [`GetIsVehiclePrimaryColourCustom`](#getisvehicleprimarycolourcustom) · [`GetIsVehicleSecondaryColourCustom`](#getisvehiclesecondarycolourcustom) · [`GetIsVehicleShuntBoostActive`](#getisvehicleshuntboostactive) · [`GetIsWheelsLoweredStateActive`](#getiswheelsloweredstateactive) · [`GetLandingGearState`](#getlandinggearstate) · [`GetLastDrivenVehicle`](#getlastdrivenvehicle) · [`GetLastPedInVehicleSeat`](#getlastpedinvehicleseat) · [`GetLastRammedVehicle`](#getlastrammedvehicle) · [`GetLiveryName`](#getliveryname) · [`GetMakeNameFromVehicleModel`](#getmakenamefromvehiclemodel) · [`GetModSlotName`](#getmodslotname) · [`GetModTextLabel`](#getmodtextlabel) · [`GetNumModColors`](#getnummodcolors) · [`GetNumModKits`](#getnummodkits) · [`GetNumVehicleMods`](#getnumvehiclemods) · [`GetNumVehicleWindowTints`](#getnumvehiclewindowtints) · [`GetNumberOfVehicleColours`](#getnumberofvehiclecolours) · [`GetNumberOfVehicleDoors`](#getnumberofvehicledoors) · [`GetNumberOfVehicleNumberPlates`](#getnumberofvehiclenumberplates) · [`GetPedInVehicleSeat`](#getpedinvehicleseat) · [`GetPedUsingVehicleDoor`](#getpedusingvehicledoor) · [`GetPositionInRecording`](#getpositioninrecording) · [`GetPositionOfVehicleRecordingAtTime`](#getpositionofvehiclerecordingattime) · [`GetPositionOfVehicleRecordingIdAtTime`](#getpositionofvehiclerecordingidattime) · [`GetRandomVehicleBackBumperInSphere`](#getrandomvehiclebackbumperinsphere) · [`GetRandomVehicleFrontBumperInSphere`](#getrandomvehiclefrontbumperinsphere) · [`GetRandomVehicleInSphere`](#getrandomvehicleinsphere) · [`GetRandomVehicleModelInMemory`](#getrandomvehiclemodelinmemory) · [`GetRemainingNitrousDuration`](#getremainingnitrousduration) · [`GetRotationOfVehicleRecordingAtTime`](#getrotationofvehiclerecordingattime) · [`GetRotationOfVehicleRecordingIdAtTime`](#getrotationofvehiclerecordingidattime) · [`GetSubmarineIsUnderDesignDepth`](#getsubmarineisunderdesigndepth) · [`GetSubmarineNumberOfAirLeaks`](#getsubmarinenumberofairleaks) · [`GetTimePositionInRecording`](#gettimepositioninrecording) · [`GetTotalDurationOfVehicleRecording`](#gettotaldurationofvehiclerecording) · [`GetTotalDurationOfVehicleRecordingId`](#gettotaldurationofvehiclerecordingid) · [`GetTrainCarriage`](#gettraincarriage) · [`GetTyreHealth`](#gettyrehealth) · [`GetTyreWearMultiplier`](#gettyrewearmultiplier) · [`GetVehicleAcceleration`](#getvehicleacceleration) · [`GetVehicleAttachedToCargobob`](#getvehicleattachedtocargobob) · [`GetVehicleBodyHealth`](#getvehiclebodyhealth) · [`GetVehicleBombCount`](#getvehiclebombcount) · [`GetVehicleCanActivateParachute`](#getvehiclecanactivateparachute) · [`GetVehicleCauseOfDestruction`](#getvehiclecauseofdestruction) · [`GetVehicleClass`](#getvehicleclass) · [`GetVehicleClassEstimatedMaxSpeed`](#getvehicleclassestimatedmaxspeed) · [`GetVehicleClassFromName`](#getvehicleclassfromname) · [`GetVehicleClassMaxAcceleration`](#getvehicleclassmaxacceleration) · [`GetVehicleClassMaxAgility`](#getvehicleclassmaxagility) · [`GetVehicleClassMaxBraking`](#getvehicleclassmaxbraking) · [`GetVehicleClassMaxTraction`](#getvehicleclassmaxtraction) · [`GetVehicleColor`](#getvehiclecolor) · [`GetVehicleColourCombination`](#getvehiclecolourcombination) · [`GetVehicleColours`](#getvehiclecolours) · [`GetVehicleColoursWhichCanBeSet`](#getvehiclecolourswhichcanbeset) · [`GetVehicleCountermeasureCount`](#getvehiclecountermeasurecount) · [`GetVehicleCurrentSlipstreamDraft`](#getvehiclecurrentslipstreamdraft) · [`GetVehicleCustomPrimaryColour`](#getvehiclecustomprimarycolour) · [`GetVehicleCustomSecondaryColour`](#getvehiclecustomsecondarycolour) · [`GetVehicleDashboardColor`](#getvehicledashboardcolor) · [`GetVehicleDeformationAtPos`](#getvehicledeformationatpos) · [`GetVehicleDirtLevel`](#getvehicledirtlevel) · [`GetVehicleDoorAngleRatio`](#getvehicledoorangleratio) · [`GetVehicleDoorLockStatus`](#getvehicledoorlockstatus) · [`GetVehicleDoorsLockedForPlayer`](#getvehicledoorslockedforplayer) · [`GetVehicleDrivetrainType`](#getvehicledrivetraintype) · [`GetVehicleEngineHealth`](#getvehicleenginehealth) · [`GetVehicleEnveffScale`](#getvehicleenveffscale) · [`GetVehicleEstimatedMaxSpeed`](#getvehicleestimatedmaxspeed) · [`GetVehicleExtraColours`](#getvehicleextracolours) · [`GetVehicleFlightNozzlePosition`](#getvehicleflightnozzleposition) · [`GetVehicleHasKers`](#getvehiclehaskers) · [`GetVehicleHasParachute`](#getvehiclehasparachute) · [`GetVehicleHealthPercentage`](#getvehiclehealthpercentage) · [`GetVehicleHomingLockonState`](#getvehiclehominglockonstate) · [`GetVehicleIndividualDoorLockStatus`](#getvehicleindividualdoorlockstatus) · [`GetVehicleInteriorColor`](#getvehicleinteriorcolor) · [`GetVehicleIsMercenary`](#getvehicleismercenary) · [`GetVehicleLayoutHash`](#getvehiclelayouthash) · [`GetVehicleLightsState`](#getvehiclelightsstate) · [`GetVehicleLivery`](#getvehiclelivery) · [`GetVehicleLiveryCount`](#getvehicleliverycount) · [`GetVehicleLockOnTarget`](#getvehiclelockontarget) · [`GetVehicleMaxBraking`](#getvehiclemaxbraking) · [`GetVehicleMaxNumberOfPassengers`](#getvehiclemaxnumberofpassengers) · [`GetVehicleMaxTraction`](#getvehiclemaxtraction) · [`GetVehicleMod`](#getvehiclemod) · [`GetVehicleModColor_1`](#getvehiclemodcolor_1) · [`GetVehicleModColor_1Name`](#getvehiclemodcolor_1name) · [`GetVehicleModColor_2`](#getvehiclemodcolor_2) · [`GetVehicleModColor_2Name`](#getvehiclemodcolor_2name) · [`GetVehicleModIdentifierHash`](#getvehiclemodidentifierhash) · [`GetVehicleModKit`](#getvehiclemodkit) · [`GetVehicleModKitType`](#getvehiclemodkittype) · [`GetVehicleModModifierValue`](#getvehiclemodmodifiervalue) · [`GetVehicleModVariation`](#getvehiclemodvariation) · [`GetVehicleModelAcceleration`](#getvehiclemodelacceleration) · [`GetVehicleModelEstimatedAgility`](#getvehiclemodelestimatedagility) · [`GetVehicleModelEstimatedMaxSpeed`](#getvehiclemodelestimatedmaxspeed) · [`GetVehicleModelMaxBraking`](#getvehiclemodelmaxbraking) · [`GetVehicleModelMaxBrakingMaxMods`](#getvehiclemodelmaxbrakingmaxmods) · [`GetVehicleModelMaxKnots`](#getvehiclemodelmaxknots) · [`GetVehicleModelMaxTraction`](#getvehiclemodelmaxtraction) · [`GetVehicleModelNumberOfSeats`](#getvehiclemodelnumberofseats) · [`GetVehicleModelValue`](#getvehiclemodelvalue) · [`GetVehicleNeonLightsColour`](#getvehicleneonlightscolour) · [`GetVehicleNumberOfBrokenBones`](#getvehiclenumberofbrokenbones) · [`GetVehicleNumberOfBrokenOffBones`](#getvehiclenumberofbrokenoffbones) · [`GetVehicleNumberOfPassengers`](#getvehiclenumberofpassengers) · [`GetVehicleNumberPlateText`](#getvehiclenumberplatetext) · [`GetVehicleNumberPlateTextIndex`](#getvehiclenumberplatetextindex) · [`GetVehiclePetrolTankHealth`](#getvehiclepetroltankhealth) · [`GetVehiclePlateType`](#getvehicleplatetype) · [`GetVehicleRecordingId`](#getvehiclerecordingid) · [`GetVehicleRoofLivery`](#getvehiclerooflivery) · [`GetVehicleRoofLiveryCount`](#getvehicleroofliverycount) · [`GetVehicleSuspensionBounds`](#getvehiclesuspensionbounds) · [`GetVehicleSuspensionHeight`](#getvehiclesuspensionheight) · [`GetVehicleTrailerVehicle`](#getvehicletrailervehicle) · [`GetVehicleTyreSmokeColor`](#getvehicletyresmokecolor) · [`GetVehicleTyresCanBurst`](#getvehicletyrescanburst) · [`GetVehicleWeaponRestrictedAmmo`](#getvehicleweaponrestrictedammo) · [`GetVehicleWheelType`](#getvehiclewheeltype) · [`GetVehicleWindowTint`](#getvehiclewindowtint) · [`GetVehicleXenonLightsColor`](#getvehiclexenonlightscolor) · [`HasFilledVehiclePopulation`](#hasfilledvehiclepopulation) · [`HasPreloadModsFinished`](#haspreloadmodsfinished) · [`HasVehicleAssetLoaded`](#hasvehicleassetloaded) · [`HasVehiclePhoneExplosiveDevice`](#hasvehiclephoneexplosivedevice) · [`HasVehicleRecordingBeenLoaded`](#hasvehiclerecordingbeenloaded) · [`HaveVehicleModsStreamedIn`](#havevehiclemodsstreamedin) · [`HideVehicleTombstone`](#hidevehicletombstone) · [`InstantlyFillVehiclePopulation`](#instantlyfillvehiclepopulation) · [`IsAnyEntityAttachedToHandlerFrame`](#isanyentityattachedtohandlerframe) · [`IsAnyPedRappellingFromHeli`](#isanypedrappellingfromheli) · [`IsAnyVehicleNearPoint`](#isanyvehiclenearpoint) · [`IsBigVehicle`](#isbigvehicle) · [`IsBoatAnchored`](#isboatanchored) · [`IsCopVehicleInArea_3d`](#iscopvehicleinarea_3d) · [`IsEntityAttachedToHandlerFrame`](#isentityattachedtohandlerframe) · [`IsEntryPointForSeatClear`](#isentrypointforseatclear) · [`IsHandlerFrameAboveContainer`](#ishandlerframeabovecontainer) · [`IsHeliLandingAreaBlocked`](#ishelilandingareablocked) · [`IsHeliPartBroken`](#ishelipartbroken) · [`IsMissionTrain`](#ismissiontrain) · [`IsNitrousActive`](#isnitrousactive) · [`IsPedExclusiveDriverOfVehicle`](#ispedexclusivedriverofvehicle) · [`IsPlaneLandingGearIntact`](#isplanelandinggearintact) · [`IsPlaybackGoingOnForVehicle`](#isplaybackgoingonforvehicle) · [`IsPlaybackUsingAiGoingOnForVehicle`](#isplaybackusingaigoingonforvehicle) · [`IsSeatWarpOnly`](#isseatwarponly) · [`IsTaxiLightOn`](#istaxilighton) · [`IsThisModelABicycle`](#isthismodelabicycle) · [`IsThisModelABike`](#isthismodelabike) · [`IsThisModelABoat`](#isthismodelaboat) · [`IsThisModelACar`](#isthismodelacar) · [`IsThisModelAHeli`](#isthismodelaheli) · [`IsThisModelAJetski`](#isthismodelajetski) · [`IsThisModelAPlane`](#isthismodelaplane) · [`IsThisModelAQuadbike`](#isthismodelaquadbike) · [`IsThisModelATrain`](#isthismodelatrain) · [`IsThisModelAnAmphibiousCar`](#isthismodelanamphibiouscar) · [`IsThisModelAnAmphibiousQuadbike`](#isthismodelanamphibiousquadbike) · [`IsToggleModOn`](#istogglemodon) · [`IsTurretSeat`](#isturretseat) · [`IsVehicleAConvertible`](#isvehicleaconvertible) · [`IsVehicleAlarmActivated`](#isvehiclealarmactivated) · [`IsVehicleAttachedToCargobob`](#isvehicleattachedtocargobob) · [`IsVehicleAttachedToTowTruck`](#isvehicleattachedtotowtruck) · [`IsVehicleAttachedToTrailer`](#isvehicleattachedtotrailer) · [`IsVehicleBeingHalted`](#isvehiclebeinghalted) · [`IsVehicleBumperBouncing`](#isvehiclebumperbouncing) · [`IsVehicleBumperBrokenOff`](#isvehiclebumperbrokenoff) · [`IsVehicleDamaged`](#isvehicledamaged) · [`IsVehicleDoorDamaged`](#isvehicledoordamaged) · [`IsVehicleDoorFullyOpen`](#isvehicledoorfullyopen) · [`IsVehicleDriveable`](#isvehicledriveable) · [`IsVehicleEngineOnFire`](#isvehicleengineonfire) · [`IsVehicleExtraTurnedOn`](#isvehicleextraturnedon) · [`IsVehicleHighDetail`](#isvehiclehighdetail) · [`IsVehicleInBurnout`](#isvehicleinburnout) · [`IsVehicleInGarageArea`](#isvehicleingaragearea) · [`IsVehicleInSubmarineMode`](#isvehicleinsubmarinemode) · [`IsVehicleModGen9Exclusive`](#isvehiclemodgen9exclusive) · [`IsVehicleModel`](#isvehiclemodel) · [`IsVehicleNeonLightEnabled`](#isvehicleneonlightenabled) · [`IsVehicleOnAllWheels`](#isvehicleonallwheels) · [`IsVehicleOnBoostPad`](#isvehicleonboostpad) · [`IsVehicleParachuteActive`](#isvehicleparachuteactive) · [`IsVehicleRocketBoostActive`](#isvehiclerocketboostactive) · [`IsVehicleSearchlightOn`](#isvehiclesearchlighton) · [`IsVehicleSeatFree`](#isvehicleseatfree) · [`IsVehicleSirenAudioOn`](#isvehiclesirenaudioon) · [`IsVehicleSirenOn`](#isvehiclesirenon) · [`IsVehicleSlipstreamLeader`](#isvehicleslipstreamleader) · [`IsVehicleSprayable`](#isvehiclesprayable) · [`IsVehicleStolen`](#isvehiclestolen) · [`IsVehicleStopped`](#isvehiclestopped) · [`IsVehicleStoppedAtTrafficLights`](#isvehiclestoppedattrafficlights) · [`IsVehicleStuckOnRoof`](#isvehiclestuckonroof) · [`IsVehicleStuckTimerUp`](#isvehiclestucktimerup) · [`IsVehicleTyreBurst`](#isvehicletyreburst) · [`IsVehicleVisible`](#isvehiclevisible) · [`IsVehicleWeaponDisabled`](#isvehicleweapondisabled) · [`IsVehicleWindowIntact`](#isvehiclewindowintact) · [`LowerConvertibleRoof`](#lowerconvertibleroof) · [`LowerRetractableWheels`](#lowerretractablewheels) · [`ModifyVehicleTopSpeed`](#modifyvehicletopspeed) · [`N_0x0205f5365292d2eb`](#n_0x0205f5365292d2eb) · [`N_0x0419b167ee128f33`](#n_0x0419b167ee128f33) · [`N_0x0581730ab9380412`](#n_0x0581730ab9380412) · [`N_0x063ae2b2cc273588`](#n_0x063ae2b2cc273588) · [`N_0x065d03a9d6b2c6b5`](#n_0x065d03a9d6b2c6b5) · [`N_0x107a473d7a6647a9`](#n_0x107a473d7a6647a9) · [`N_0x1312ddd8385aee4e`](#n_0x1312ddd8385aee4e) · [`N_0x182f266c2d9e2beb`](#n_0x182f266c2d9e2beb) · [`N_0x2310a8f9421ebf43`](#n_0x2310a8f9421ebf43) · [`N_0x2311dd7159f00582`](#n_0x2311dd7159f00582) · [`N_0x2c4a1590abf43e8b`](#n_0x2c4a1590abf43e8b) · [`N_0x3441cad2f2231923`](#n_0x3441cad2f2231923) · [`N_0x35bb21de06784373`](#n_0x35bb21de06784373) · [`N_0x35e0654f4bad7971`](#n_0x35e0654f4bad7971) · [`N_0x36de109527a2c0c4`](#n_0x36de109527a2c0c4) · [`N_0x3b458ddb57038f08`](#n_0x3b458ddb57038f08) · [`N_0x407dc5e97db1a4d3`](#n_0x407dc5e97db1a4d3) · [`N_0x41290b40fa63e6da`](#n_0x41290b40fa63e6da) · [`N_0x428ad3e26c8d9eb0`](#n_0x428ad3e26c8d9eb0) · [`N_0x430a7631a84c9be7`](#n_0x430a7631a84c9be7) · [`N_0x4419966c9936071a`](#n_0x4419966c9936071a) · [`N_0x4ad280eb48b2d8e6`](#n_0x4ad280eb48b2d8e6) · [`N_0x4d9d109f63fee1d4`](#n_0x4d9d109f63fee1d4) · [`N_0x51db102f4a3ba5e0`](#n_0x51db102f4a3ba5e0) · [`N_0x51f30db60626a20e`](#n_0x51f30db60626a20e) · [`N_0x56eb5e94318d3fb6`](#n_0x56eb5e94318d3fb6) · [`N_0x5845066d8a1ea7f7`](#n_0x5845066d8a1ea7f7) · [`N_0x59c3757b3b7408e8`](#n_0x59c3757b3b7408e8) · [`N_0x5ba68a0840d546ac`](#n_0x5ba68a0840d546ac) · [`N_0x5bbcf35bf6e456f7`](#n_0x5bbcf35bf6e456f7) · [`N_0x5e569ec46ec21cae`](#n_0x5e569ec46ec21cae) · [`N_0x5ee5632f47ae9695`](#n_0x5ee5632f47ae9695) · [`N_0x6501129c9e0ffa05`](#n_0x6501129c9e0ffa05) · [`N_0x65b080555ea48149`](#n_0x65b080555ea48149) · [`N_0x66e3aaface2d1eb8`](#n_0x66e3aaface2d1eb8) · [`N_0x6a973569ba094650`](#n_0x6a973569ba094650) · [`N_0x6eaaefc76acc311f`](#n_0x6eaaefc76acc311f) · [`N_0x6ebfb22d646ffc18`](#n_0x6ebfb22d646ffc18) · [`N_0x725012a415dba050`](#n_0x725012a415dba050) · [`N_0x72beccf4b829522e`](#n_0x72beccf4b829522e) · [`N_0x73561d4425a021a2`](#n_0x73561d4425a021a2) · [`N_0x737e398138550fff`](#n_0x737e398138550fff) · [`N_0x76d26a22750e849e`](#n_0x76d26a22750e849e) · [`N_0x78ceee41f49f421f`](#n_0x78ceee41f49f421f) · [`N_0x796a877e459b99ea`](#n_0x796a877e459b99ea) · [`N_0x7bbe7ff626a591fe`](#n_0x7bbe7ff626a591fe) · [`N_0x80e3357fdef45c21`](#n_0x80e3357fdef45c21) · [`N_0x8235f1bead557629`](#n_0x8235f1bead557629) · [`N_0x82e0ac411e41a5b4`](#n_0x82e0ac411e41a5b4) · [`N_0x8533cafde1f0f336`](#n_0x8533cafde1f0f336) · [`N_0x8664170ef165c4a6`](#n_0x8664170ef165c4a6) · [`N_0x870b8b7a766615c8`](#n_0x870b8b7a766615c8) · [`N_0x8821196d91fa2de5`](#n_0x8821196d91fa2de5) · [`N_0x887fa38787de8c72`](#n_0x887fa38787de8c72) · [`N_0x88bc673ca9e0ae99`](#n_0x88bc673ca9e0ae99) · [`N_0x8f0d5ba1c2cc91d7`](#n_0x8f0d5ba1c2cc91d7) · [`N_0x9640e30a7f395e4b`](#n_0x9640e30a7f395e4b) · [`N_0x97841634ef7df1d6`](#n_0x97841634ef7df1d6) · [`N_0x9849de24fcf23ccc`](#n_0x9849de24fcf23ccc) · [`N_0x99a05839c46ce316`](#n_0x99a05839c46ce316) · [`N_0x99cad8e7afdb60fa`](#n_0x99cad8e7afdb60fa) · [`N_0x9bddc73cc6a115d4`](#n_0x9bddc73cc6a115d4) · [`N_0x9becd4b9fef3f8a6`](#n_0x9becd4b9fef3f8a6) · [`N_0x9d30687c57baa0bb`](#n_0x9d30687c57baa0bb) · [`N_0x9f3f689b814f2599`](#n_0x9f3f689b814f2599) · [`N_0xa01bc64dd4bfbbac`](#n_0xa01bc64dd4bfbbac) · [`N_0xa247f9ef01d8082e`](#n_0xa247f9ef01d8082e) · [`N_0xa4822f1cf23f4810`](#n_0xa4822f1cf23f4810) · [`N_0xa4a9a4c40e615885`](#n_0xa4a9a4c40e615885) · [`N_0xa7dcdf4ded40a8f4`](#n_0xa7dcdf4ded40a8f4) · [`N_0xaa653ae61924b0a0`](#n_0xaa653ae61924b0a0) · [`N_0xab04325045427aae`](#n_0xab04325045427aae) · [`N_0xab31ef4de6800ce9`](#n_0xab31ef4de6800ce9) · [`N_0xae3fee8709b39dcb`](#n_0xae3fee8709b39dcb) · [`N_0xaf60e6a2936f982a`](#n_0xaf60e6a2936f982a) · [`N_0xb2e0c0d6922d31f2`](#n_0xb2e0c0d6922d31f2) · [`N_0xb68cfaf83a02768d`](#n_0xb68cfaf83a02768d) · [`N_0xb9562064627ff9db`](#n_0xb9562064627ff9db) · [`N_0xbb2333bb87ddd87f`](#n_0xbb2333bb87ddd87f) · [`N_0xbe5c1255a1830ff5`](#n_0xbe5c1255a1830ff5) · [`N_0xc0ed6438e6d39ba8`](#n_0xc0ed6438e6d39ba8) · [`N_0xc361aa040d6637a8`](#n_0xc361aa040d6637a8) · [`N_0xc4b3347bd68bd609`](#n_0xc4b3347bd68bd609) · [`N_0xc50ce861b55eab8b`](#n_0xc50ce861b55eab8b) · [`N_0xcf9159024555488c`](#n_0xcf9159024555488c) · [`N_0xcfd778e7904c255e`](#n_0xcfd778e7904c255e) · [`N_0xd3301660a57c9272`](#n_0xd3301660a57c9272) · [`N_0xd3e51c0ab8c26eee`](#n_0xd3e51c0ab8c26eee) · [`N_0xd4196117af7bb974`](#n_0xd4196117af7bb974) · [`N_0xd565f438137f0e10`](#n_0xd565f438137f0e10) · [`N_0xdbc631f109350b8c`](#n_0xdbc631f109350b8c) · [`N_0xdce97bdf8a0eabc8`](#n_0xdce97bdf8a0eabc8) · [`N_0xe05dd0e9707003a3`](#n_0xe05dd0e9707003a3) · [`N_0xe2f53f172b45ede1`](#n_0xe2f53f172b45ede1) · [`N_0xe5810ac70602f2f5`](#n_0xe5810ac70602f2f5) · [`N_0xe851e480b814d4ba`](#n_0xe851e480b814d4ba) · [`N_0xe8718faf591fd224`](#n_0xe8718faf591fd224) · [`N_0xed5ede9e676643c9`](#n_0xed5ede9e676643c9) · [`N_0xef9d388f8d377f44`](#n_0xef9d388f8d377f44) · [`N_0xf051d9bfb6ba39c0`](#n_0xf051d9bfb6ba39c0) · [`N_0xf25e02cb9c5818f8`](#n_0xf25e02cb9c5818f8) · [`N_0xf3b0e0aed097a3f5`](#n_0xf3b0e0aed097a3f5) · [`N_0xf8b49f5ba7f850e7`](#n_0xf8b49f5ba7f850e7) · [`N_0xfaf2a78061fd9ef4`](#n_0xfaf2a78061fd9ef4) · [`NetworkUseHighPrecisionVehicleBlending`](#networkusehighprecisionvehicleblending) · [`OpenBombBayDoors`](#openbombbaydoors) · [`PausePlaybackRecordedVehicle`](#pauseplaybackrecordedvehicle) · [`PopOutVehicleWindscreen`](#popoutvehiclewindscreen) · [`PreloadVehicleMod`](#preloadvehiclemod) · [`RaiseConvertibleRoof`](#raiseconvertibleroof) · [`RaiseRetractableWheels`](#raiseretractablewheels) · [`ReleasePreloadMods`](#releasepreloadmods) · [`RemovePickUpRopeForCargobob`](#removepickupropeforcargobob) · [`RemoveRoadNodeSpeedZone`](#removeroadnodespeedzone) · [`RemoveVehicleAsset`](#removevehicleasset) · [`RemoveVehicleCombatAvoidanceArea`](#removevehiclecombatavoidancearea) · [`RemoveVehicleHighDetailModel`](#removevehiclehighdetailmodel) · [`RemoveVehicleMod`](#removevehiclemod) · [`RemoveVehicleRecording`](#removevehiclerecording) · [`RemoveVehicleShadowEffect`](#removevehicleshadoweffect) · [`RemoveVehicleStuckCheck`](#removevehiclestuckcheck) · [`RemoveVehicleUpsidedownCheck`](#removevehicleupsidedowncheck) · [`RemoveVehicleWindow`](#removevehiclewindow) · [`RemoveVehiclesFromGeneratorsInArea`](#removevehiclesfromgeneratorsinarea) · [`RequestVehicleAsset`](#requestvehicleasset) · [`RequestVehicleDashboardScaleformMovie`](#requestvehicledashboardscaleformmovie) · [`RequestVehicleHighDetailModel`](#requestvehiclehighdetailmodel) · [`RequestVehicleRecording`](#requestvehiclerecording) · [`ResetVehicleStuckTimer`](#resetvehiclestucktimer) · [`ResetVehicleWheels`](#resetvehiclewheels) · [`RollDownWindow`](#rolldownwindow) · [`RollDownWindows`](#rolldownwindows) · [`RollUpWindow`](#rollupwindow) · [`SetAllLowPriorityVehicleGeneratorsActive`](#setalllowpriorityvehiclegeneratorsactive) · [`SetAllVehicleGeneratorsActive`](#setallvehiclegeneratorsactive) · [`SetAllVehicleGeneratorsActiveInArea`](#setallvehiclegeneratorsactiveinarea) · [`SetAmbientVehicleRangeMultiplierThisFrame`](#setambientvehiclerangemultiplierthisframe) · [`SetBikeOnStand`](#setbikeonstand) · [`SetBoatAnchor`](#setboatanchor) · [`SetBoatBoomPositionRatio`](#setboatboompositionratio) · [`SetBoatDisableAvoidance`](#setboatdisableavoidance) · [`SetBoatIsSinking`](#setboatissinking) · [`SetBoatLowLodAnchorDistance`](#setboatlowlodanchordistance) · [`SetBoatRemainsAnchoredWhilePlayerIsDriver`](#setboatremainsanchoredwhileplayerisdriver) · [`SetBoatSinksWhenWrecked`](#setboatsinkswhenwrecked) · [`SetCamberedWheelsDisabled`](#setcamberedwheelsdisabled) · [`SetCanResprayVehicle`](#setcanresprayvehicle) · [`SetCarBootOpen`](#setcarbootopen) · [`SetCarHighSpeedBumpSeverityMultiplier`](#setcarhighspeedbumpseveritymultiplier) · [`SetCargobobExcludeFromPickupEntity`](#setcargobobexcludefrompickupentity) · [`SetCargobobForceDontDetachVehicle`](#setcargobobforcedontdetachvehicle) · [`SetCargobobHookCanAttach`](#setcargobobhookcanattach) · [`SetCargobobPickupMagnetActive`](#setcargobobpickupmagnetactive) · [`SetCargobobPickupMagnetEffectRadius`](#setcargobobpickupmagneteffectradius) · [`SetCargobobPickupMagnetFalloff`](#setcargobobpickupmagnetfalloff) · [`SetCargobobPickupMagnetPullRopeLength`](#setcargobobpickupmagnetpullropelength) · [`SetCargobobPickupMagnetPullStrength`](#setcargobobpickupmagnetpullstrength) · [`SetCargobobPickupMagnetReducedFalloff`](#setcargobobpickupmagnetreducedfalloff) · [`SetCargobobPickupMagnetReducedStrength`](#setcargobobpickupmagnetreducedstrength) · [`SetCargobobPickupMagnetStrength`](#setcargobobpickupmagnetstrength) · [`SetCargobobPickupRopeDampingMultiplier`](#setcargobobpickupropedampingmultiplier) · [`SetCargobobPickupRopeType`](#setcargobobpickupropetype) · [`SetConvertibleRoof`](#setconvertibleroof) · [`SetConvertibleRoofLatchState`](#setconvertiblerooflatchstate) · [`SetDeployHeliStubWings`](#setdeployhelistubwings) · [`SetDisableBmxExtraTrickForces`](#setdisablebmxextratrickforces) · [`SetDisableExplodeFromBodyDamageOnCollision`](#setdisableexplodefrombodydamageoncollision) · [`SetDisableExplodeFromBodyDamageReceivedByAiVehicle`](#setdisableexplodefrombodydamagereceivedbyaivehicle) · [`SetDisableHeliExplodeFromBodyDamage`](#setdisableheliexplodefrombodydamage) · [`SetDisableHoverModeFlight`](#setdisablehovermodeflight) · [`SetDisablePretendOccupants`](#setdisablepretendoccupants) · [`SetDisableRandomTrainsThisFrame`](#setdisablerandomtrainsthisframe) · [`SetDisableSuperdummyMode`](#setdisablesuperdummymode) · [`SetDisableTurretMovementThisFrame`](#setdisableturretmovementthisframe) · [`SetDisableVehicleEngineFires`](#setdisablevehicleenginefires) · [`SetDisableVehicleFlightNozzlePosition`](#setdisablevehicleflightnozzleposition) · [`SetDisableVehiclePetrolTankDamage`](#setdisablevehiclepetroltankdamage) · [`SetDisableVehiclePetrolTankFires`](#setdisablevehiclepetroltankfires) · [`SetDisableVehicleUnk`](#setdisablevehicleunk) · [`SetDisableVehicleUnk_2`](#setdisablevehicleunk_2) · [`SetDisableVehicleWindowCollisions`](#setdisablevehiclewindowcollisions) · [`SetDistantCarsEnabled`](#setdistantcarsenabled) · [`SetDriftTyresEnabled`](#setdrifttyresenabled) · [`SetEnableVehicleSlipstreaming`](#setenablevehicleslipstreaming) · [`SetFarDrawVehicles`](#setfardrawvehicles) · [`SetForceHdVehicle`](#setforcehdvehicle) · [`SetForceLowLodAnchorMode`](#setforcelowlodanchormode) · [`SetForkliftForkHeight`](#setforkliftforkheight) · [`SetGarbageTrucks`](#setgarbagetrucks) · [`SetHeliBladesFullSpeed`](#sethelibladesfullspeed) · [`SetHeliBladesSpeed`](#sethelibladesspeed) · [`SetHeliCombatOffset`](#sethelicombatoffset) · [`SetHeliMainRotorHealth`](#sethelimainrotorhealth) · [`SetHeliResistToExplosion`](#setheliresisttoexplosion) · [`SetHeliTailBoomCanBreakOff`](#sethelitailboomcanbreakoff) · [`SetHeliTailRotorHealth`](#sethelitailrotorhealth) · [`SetHeliTurbulenceScalar`](#setheliturbulencescalar) · [`SetHelicopterRollPitchYawMult`](#sethelicopterrollpitchyawmult) · [`SetHoverModeWingRatio`](#sethovermodewingratio) · [`SetHydraulicRaised`](#sethydraulicraised) · [`SetHydraulicWheelState`](#sethydraulicwheelstate) · [`SetHydraulicWheelStateTransition`](#sethydraulicwheelstatetransition) · [`SetHydraulicWheelValue`](#sethydraulicwheelvalue) · [`SetLastDrivenVehicle`](#setlastdrivenvehicle) · [`SetLightsCutoffDistanceTweak`](#setlightscutoffdistancetweak) · [`SetMissionTrainAsNoLongerNeeded`](#setmissiontrainasnolongerneeded) · [`SetMissionTrainCoords`](#setmissiontraincoords) · [`SetNitrousIsActive`](#setnitrousisactive)

---
### AddRoadNodeSpeedZone

`ADD_ROAD_NODE_SPEED_ZONE` · hash `0x2CE544C68FB812A0` · jhash `0xD6685803` · **Cliente**

```lua
local retval = AddRoadNodeSpeedZone(x, y, z, radius, speed, p5)
```
```c
int ADD_ROAD_NODE_SPEED_ZONE(float x, float y, float z, float radius, float speed, BOOL p5);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `speed` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x2CE544C68FB812A0` (`N_0x2ce544c68fb812a0`), `_ADD_SPEED_ZONE_FOR_COORD` (`AddSpeedZoneForCoord`)

---
### AddVehicleCombatAngledAvoidanceArea

`ADD_VEHICLE_COMBAT_ANGLED_AVOIDANCE_AREA` · hash `0x54B0F614960F4A5F` · jhash `0x5AB26C2B` · **Cliente**

```lua
local retval = AddVehicleCombatAngledAvoidanceArea(p0, p1, p2, p3, p4, p5, p6)
```
```c
Any ADD_VEHICLE_COMBAT_ANGLED_AVOIDANCE_AREA(float p0, float p1, float p2, float p3, float p4, float p5, float p6);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x54B0F614960F4A5F` (`N_0x54b0f614960f4a5f`), `_ADD_VEHICLE_COMBAT_AVOIDANCE_AREA` (`AddVehicleCombatAvoidanceArea`)

---
### AddVehiclePhoneExplosiveDevice

`ADD_VEHICLE_PHONE_EXPLOSIVE_DEVICE` · hash `0x99AD4CCCB128CBC9` · jhash `0x811373DE` · **Cliente**

```lua
AddVehiclePhoneExplosiveDevice(vehicle)
```
```c
void ADD_VEHICLE_PHONE_EXPLOSIVE_DEVICE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x99AD4CCCB128CBC9` (`N_0x99ad4cccb128cbc9`)

---
### AddVehicleStuckCheckWithWarp

`ADD_VEHICLE_STUCK_CHECK_WITH_WARP` · hash `0x2FA9923062DD396C` · jhash `0xC8B789AD` · **Cliente**

```lua
AddVehicleStuckCheckWithWarp(p0, p1, p2, p3, p4, p5, p6)
```
```c
void ADD_VEHICLE_STUCK_CHECK_WITH_WARP(Any p0, float p1, Any p2, BOOL p3, BOOL p4, BOOL p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`Any`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### AddVehicleUpsidedownCheck

`ADD_VEHICLE_UPSIDEDOWN_CHECK` · hash `0xB72E26D81006005B` · jhash `0x3A13D384` · **Cliente**

```lua
AddVehicleUpsidedownCheck(vehicle)
```
```c
void ADD_VEHICLE_UPSIDEDOWN_CHECK(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### AllowAmbientVehiclesToAvoidAdverseConditions

`ALLOW_AMBIENT_VEHICLES_TO_AVOID_ADVERSE_CONDITIONS` · hash `0xB264C4D2F2B0A78B` · jhash `0x45F72495` · **Cliente**

```lua
AllowAmbientVehiclesToAvoidAdverseConditions(vehicle)
```
```c
void ALLOW_AMBIENT_VEHICLES_TO_AVOID_ADVERSE_CONDITIONS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

This native it's a debug native. Won't do anything.

**Nombres antiguos (alias):** `0xB264C4D2F2B0A78B` (`N_0xb264c4d2f2b0a78b`)

---
### AreAllVehicleWindowsIntact

`ARE_ALL_VEHICLE_WINDOWS_INTACT` · hash `0x11D862A3E977A9EF` · jhash `0xBB619744` · **Cliente**

```lua
local retval = AreAllVehicleWindowsIntact(vehicle)
```
```c
BOOL ARE_ALL_VEHICLE_WINDOWS_INTACT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Appears to return false if any window is broken.  
```

**Nombres antiguos (alias):** `_ARE_ALL_VEHICLE_WINDOWS_INTACT` (`AreAllVehicleWindowsIntact`)

---
### AreAnyVehicleSeatsFree

`ARE_ANY_VEHICLE_SEATS_FREE` · hash `0x2D34FC3BC4ADB780` · jhash `0x648E685A` · **Cliente**

```lua
local retval = AreAnyVehicleSeatsFree(vehicle)
```
```c
BOOL ARE_ANY_VEHICLE_SEATS_FREE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle to check.

**Devuelve:** `BOOL` — Returns `true` when the vehicle has at least one seat with no ped assigned to it. Vehicles with no seats in their model (trailers, prop carriages) or an invalid entity will return `false`.

**Descripción oficial:**

Dead peds still count as occupying a seat until the body is removed, so a vehicle full of corpses returns `false`. Peds tasked to enter the vehicle but not yet inserted do not occupy their target seat.

For per-seat queries use [IS_VEHICLE_SEAT_FREE](#isvehicleseatfree), to find which ped is in a specific seat use [GET_PED_IN_VEHICLE_SEAT](https://docs.fivem.net/natives/?_0xBB40BBB9B9A067B).

**Nombres antiguos (alias):** `_IS_ANY_VEHICLE_SEAT_EMPTY` (`IsAnyVehicleSeatEmpty`)

**Ejemplo (lua):**

```lua
-- Print whether the vehicle the player is in has a free seat
RegisterCommand("seatcheck", function()
    local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
    if vehicle == 0 then return end
    if AreAnyVehicleSeatsFree(vehicle) then
        print("Room available.")
    else
        print("Vehicle is full.")
    end
end, false)
```

**Ejemplo (js):**

```js
// Print whether the vehicle the player is in has a free seat
RegisterCommand("seatcheck", () => {
    const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
    if (vehicle === 0) return;
    if (AreAnyVehicleSeatsFree(vehicle)) {
        console.log("Room available.");
    } else {
        console.log("Vehicle is full.");
    }
}, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Print whether the vehicle the player is in has a free seat
RegisterCommand("seatcheck", new Action<int, List<object>, string>((source, args, raw) =>
{
    int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
    if (vehicle == 0) return;
    if (AreAnyVehicleSeatsFree(vehicle))
    {
        Debug.WriteLine("Room available.");
    }
    else
    {
        Debug.WriteLine("Vehicle is full.");
    }
}), false);
```

---
### AreBombBayDoorsOpen

`_ARE_BOMB_BAY_DOORS_OPEN` · hash `0xD0917A423314BBA8` · **Cliente**

```lua
local retval = AreBombBayDoorsOpen(aircraft)
```
```c
BOOL _ARE_BOMB_BAY_DOORS_OPEN(Vehicle aircraft);
```

**Parámetros**

- `aircraft` (`Vehicle`): The vehicle to check the bomb bay doors on.

**Devuelve:** `BOOL` — A bool indicating the state of the doors (true = open, false = closed).

**Descripción oficial:**

Returns true when the bomb bay doors of this plane are open. False if they're closed.

**Nombres antiguos (alias):** `0xD0917A423314BBA8` (`N_0xd0917a423314bba8`), `_GET_ARE_BOMB_BAY_DOORS_OPEN` (`GetAreBombBayDoorsOpen`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

if AreBombBayDoorsOpen(vehicle) then
    print("The doors are open!")
else
    print("The doors are closed!")
end
```

**Ejemplo (cs):**

```cs
int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);

if (AreBombBayDoorsOpen(vehicle))
{
    Debug.WriteLine("The doors are open!");
}
else
{
    Debug.WriteLine("The doors are closed!");
}
```

---
### AreHeliStubWingsDeployed

`_ARE_HELI_STUB_WINGS_DEPLOYED` · hash `0xAEF12960FA943792` · **Cliente**

```lua
local retval = AreHeliStubWingsDeployed(vehicle)
```
```c
BOOL _ARE_HELI_STUB_WINGS_DEPLOYED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Only used with the "akula" in the decompiled native scripts.

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0xAEF12960FA943792` (`N_0xaef12960fa943792`)

---
### AreOutriggerLegsDeployed

`_ARE_OUTRIGGER_LEGS_DEPLOYED` · hash `0x3A9128352EAC9E85` · **Cliente**

```lua
local retval = AreOutriggerLegsDeployed(vehicle)
```
```c
BOOL _ARE_OUTRIGGER_LEGS_DEPLOYED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL` — The deployment state of the vehicle's outrigger legs

**Descripción oficial:**

Returns whether the outrigger legs are deployed for the vehicle.
The Chernobog is one of the few vehicles with outrigger legs.

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x3A9128352EAC9E85` (`N_0x3a9128352eac9e85`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
local deployed = AreOutriggerLegsDeployed(vehicle)
print("deploy state:", deployed)
```

---
### ArePlaneControlPanelsIntact

`ARE_PLANE_CONTROL_PANELS_INTACT` · hash `0xF78F94D60248C737` · jhash `0x3B51B348` · **Cliente**

```lua
local retval = ArePlaneControlPanelsIntact(vehicle, checkForZeroHealth)
```
```c
BOOL ARE_PLANE_CONTROL_PANELS_INTACT(Vehicle vehicle, BOOL checkForZeroHealth);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check. This should be a plane.
- `checkForZeroHealth` (`BOOL`): If set to `true`, the native also checks if the plane's health is zero, indicating it is completely destroyed. If `false`, only the state of the control panels is considered.

**Devuelve:** `BOOL` — Returns `true` if the plane's control panels are intact, and, depending on the `checkForZeroHealth` parameter, the plane is not completely destroyed. Returns `false` if the control panels are damaged or the plane is destroyed (when `checkForZeroHealth` is `true`).

**Descripción oficial:**

Queries whether the control panels of a plane are intact. This native is used to determine the operational status of a plane's cockpit controls, which can affect the plane's flyability.

**Nombres antiguos (alias):** `0xF78F94D60248C737` (`N_0xf78f94d60248c737`)

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the plane the player is currently in.
local plane = GetVehiclePedIsIn(playerPed, false)

-- If the player is not in a plane, return
if (plane == 0) or (not IsThisModelAPlane(GetEntityModel(plane))) then return end

-- Check if the plane's control panels are intact
local controlPanelsIntact = ArePlaneControlPanelsIntact(plane, true)

if (controlPanelsIntact) then
    print("The plane's control panels are intact")
else
    print("The plane's control panels are damaged or the plane is destroyed")
end
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the plane the player is currently in.
const plane = GetVehiclePedIsIn(playerPed, false);

// If the player is not in a plane, return
if (plane === 0 || !IsThisModelAPlane(GetEntityModel(plane))) return;

// Check if the plane's control panels are intact
const controlPanelsIntact = ArePlaneControlPanelsIntact(plane, true);

if (controlPanelsIntact) {
    console.log("The plane's control panels are intact");
} else {
    console.log("The plane's control panels are damaged or the plane is destroyed");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the plane the player is currently flying
int plane = GetVehiclePedIsIn(playerPed, false);

// If the player is not flying a plane, return
if (plane == 0 || !IsThisModelAPlane(GetEntityModel(plane))) return;

// Check if the plane's control panels are intact
bool controlPanelsIntact = ArePlaneControlPanelsIntact(plane, true);

if (controlPanelsIntact) {
    Debug.WriteLine("The plane's control panels are intact");
} else {
    Debug.WriteLine("The plane's control panels are damaged or the plane is destroyed");
}
```

---
### ArePlanePropellersIntact

`ARE_PLANE_PROPELLERS_INTACT` · hash `0x755D6D5267CBBD7E` · jhash `0xABBDD5C6` · **Cliente**

```lua
local retval = ArePlanePropellersIntact(plane)
```
```c
BOOL ARE_PLANE_PROPELLERS_INTACT(Vehicle plane);
```

**Parámetros**

- `plane` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x755D6D5267CBBD7E` (`N_0x755d6d5267cbbd7e`), `_ARE_PROPELLERS_UNDAMAGED` (`ArePropellersUndamaged`)

---
### ArePlaneWingsIntact

`_ARE_PLANE_WINGS_INTACT` · hash `0x5991A01434CE9677` · jhash `0xAF8CB3DF` · **Cliente**

```lua
local retval = ArePlaneWingsIntact(plane)
```
```c
BOOL _ARE_PLANE_WINGS_INTACT(Vehicle plane);
```

**Parámetros**

- `plane` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5991A01434CE9677` (`N_0x5991a01434ce9677`), `ADD_A_MARKER_OVER_VEHICLE` (`AddAMarkerOverVehicle`), `_ARE_VEHICLE_WINGS_INTACT` (`AreVehicleWingsIntact`)

---
### AttachContainerToHandlerFrame

`_ATTACH_CONTAINER_TO_HANDLER_FRAME` · hash `0x6A98C2ECF57FA5D4` · jhash `0x20AB5783` · **Cliente**

```lua
AttachContainerToHandlerFrame(handler, container)
```
```c
void _ATTACH_CONTAINER_TO_HANDLER_FRAME(Vehicle handler, Entity container);
```

**Parámetros**

- `handler` (`Vehicle`)
- `container` (`Entity`)

**Devuelve:** `void`

---
### AttachEntityToCargobob

`ATTACH_ENTITY_TO_CARGOBOB` · hash `0xA1DD82F3CCF9A01E` · jhash `0xAEB29F98` · **Cliente**

```lua
AttachEntityToCargobob(vehicle, entity, p2, x, y, z)
```
```c
void ATTACH_ENTITY_TO_CARGOBOB(Vehicle vehicle, Entity entity, int p2, float x, float y, float z);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `entity` (`Entity`)
- `p2` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA1DD82F3CCF9A01E` (`N_0xa1dd82f3ccf9a01e`), `_ATTACH_ENTITY_TO_CARGOBOB` (`AttachEntityToCargobob`)

---
### AttachVehicleOnToTrailer

`ATTACH_VEHICLE_ON_TO_TRAILER` · hash `0x16B5E274BDE402F8` · jhash `0x12AC1A16` · **Cliente**

```lua
AttachVehicleOnToTrailer(vehicle, trailer, offsetX, offsetY, offsetZ, coordsX, coordsY, coordsZ, rotationX, rotationY, rotationZ, disableColls)
```
```c
void ATTACH_VEHICLE_ON_TO_TRAILER(Vehicle vehicle, Vehicle trailer, float offsetX, float offsetY, float offsetZ, float coordsX, float coordsY, float coordsZ, float rotationX, float rotationY, float rotationZ, float disableColls);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to attach to the trailer
- `trailer` (`Vehicle`): The trailer to attach the vehicle to
- `offsetX` (`float`): The x offset of the vehicle
- `offsetY` (`float`): The y offset of the vehicle
- `offsetZ` (`float`): The z offset of the vehicle
- `coordsX` (`float`): The x coords of where you want the vehicle placed (must be an offset from the trailer itself)
- `coordsY` (`float`): The y coords of where you want the vehicle placed (must be an offset from the trailer itself)
- `coordsZ` (`float`): The z coords of where you want the vehicle placed (must be an offset from the trailer itself)
- `rotationX` (`float`): The x rotation of where you want the vehicle placed
- `rotationY` (`float`): The y rotation of where you want the vehicle placed
- `rotationZ` (`float`): The z rotation of where you want the vehicle placed
- `disableColls` (`float`): Should actually be a boolean, this will disable the collision between the vehicle you're attaching and the trailer

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x16B5E274BDE402F8` (`N_0x16b5e274bde402f8`)

**Ejemplo (lua):**

```lua
-- Request the model before creating it
local truckTrailer = CreateVehicle(`tr2`, GetOffsetFromEntityInWorldCoords(PlayerPedId(), 0.0, 8.0, 0.0), true)

-- Open the rear ramp so you can drive a vehicle on
SetVehicleDoorOpen(truckTrailer, 5, false, false)

-- Get the vehicle you're in and it's coords and rotation
local veh = GetVehiclePedIsIn(PlayerPedId())
local vehCoords = GetEntityCoords(veh)
local vehRotation = GetEntityRotation(veh)

-- Park the car where on the trailer you want it, you could make sure your vehicle is touching the trailer first using "IsEntityTouchingEntity"
AttachVehicleOnToTrailer(veh, truckTrailer, 0.0, 0.0, 0.0, GetOffsetFromEntityGivenWorldCoords(truckTrailer, vehCoords), vehRotation, false)

-- Do the following to detach the vehicle from the trailer
DetachEntity(veh, true, false)
```

---
### AttachVehicleToCargobob

`ATTACH_VEHICLE_TO_CARGOBOB` · hash `0x4127F1D84E347769` · jhash `0x607DC9D5` · **Cliente**

```lua
AttachVehicleToCargobob(cargobob, vehicle, vehicleBoneIndex, x, y, z)
```
```c
void ATTACH_VEHICLE_TO_CARGOBOB(Vehicle cargobob, Vehicle vehicle, int vehicleBoneIndex, float x, float y, float z);
```

**Parámetros**

- `cargobob` (`Vehicle`): The cargobob
- `vehicle` (`Vehicle`): The vehicle that will be attached
- `vehicleBoneIndex` (`int`): A Vehicle bone the hook/magnet should attach to or -1 for none/default [GET_ENTITY_BONE_INDEX_BY_NAME](ENTITY.md#getentityboneindexbyname)
- `x` (`float`): x hook/magnet Offset
- `y` (`float`): y hook/magnet Offset
- `z` (`float`): z hook/magnet Offset

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
function RequestVehicleModel(modelHash)
    if not IsModelInCdimage(modelHash) then return end
    RequestModel(modelHash)
    while not HasModelLoaded(modelHash) do 
      Wait(0)
    end
end

RegisterCommand('spawnCargobob', function(source, args)
    local cargobobHash = `cargobob` 
    local carHash = `adder` 
    local myPed = PlayerPedId()

    local spawnCoords = GetEntityCoords(myPed)

    RequestVehicleModel(cargobobHash)
    local cargobob = CreateVehicle(cargobobHash, spawnCoords+vec3(0.0,0.0, 10.0), GetEntityHeading(myPed), true, false) -- Spawns a cargobob above players location
    SetHeliBladesSpeed(cargobob, 1.0) -- sets the helicoper blades to max spin speed
    SetPedIntoVehicle(myPed, cargobob, -1) -- sets the player into the cargobob
    SetModelAsNoLongerNeeded(cargobobHash) -- removes model from game memory as we no longer need it
    CreatePickUpRopeForCargobob(cargobob, 1) -- 0 = hook, 1 = Magnet Enable rope from cargobob

    RequestVehicleModel(carHash)
    local vehicle = CreateVehicle(carHash, spawnCoords, GetEntityHeading(myPed), true, false) -- Spawns a vehicle for the cargobob to pickup
    SetModelAsNoLongerNeeded(carHash)
    Wait(1000)
    AttachVehicleToCargobob(cargobob, vehicle, GetEntityBoneIndexByName(vehicle, 'bodyshell'), 0.0, 0.0, 0.0) --Attach the vehicle to the magnet or hook
end)
```

---
### AttachVehicleToTowTruck

`ATTACH_VEHICLE_TO_TOW_TRUCK` · hash `0x29A16F8D621C4508` · jhash `0x8151571A` · **Cliente**

```lua
AttachVehicleToTowTruck(towTruck, vehicle, rear, hookOffsetX, hookOffsetY, hookOffsetZ)
```
```c
void ATTACH_VEHICLE_TO_TOW_TRUCK(Vehicle towTruck, Vehicle vehicle, BOOL rear, float hookOffsetX, float hookOffsetY, float hookOffsetZ);
```

**Parámetros**

- `towTruck` (`Vehicle`)
- `vehicle` (`Vehicle`)
- `rear` (`BOOL`)
- `hookOffsetX` (`float`)
- `hookOffsetY` (`float`)
- `hookOffsetZ` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
HookOffset defines where the hook is attached. leave at 0 for default attachment.
```

---
### AttachVehicleToTrailer

`ATTACH_VEHICLE_TO_TRAILER` · hash `0x3C7D42D58F770B54` · jhash `0x2133977F` · **Cliente**

```lua
AttachVehicleToTrailer(vehicle, trailer, radius)
```
```c
void ATTACH_VEHICLE_TO_TRAILER(Vehicle vehicle, Vehicle trailer, float radius);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `trailer` (`Vehicle`)
- `radius` (`float`)

**Devuelve:** `void`

---
### BringVehicleToHalt

`BRING_VEHICLE_TO_HALT` · hash `0x260BE8F09E326A20` · jhash `0xCBC7D3C8` · **Cliente**

```lua
BringVehicleToHalt(vehicle, distance, duration, bControlVerticalVelocity)
```
```c
void BRING_VEHICLE_TO_HALT(Vehicle vehicle, float distance, int duration, BOOL bControlVerticalVelocity);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to stop.
- `distance` (`float`): The distance from the initial coords at which the vehicle should come to rest.
- `duration` (`int`): The length of time in seconds to hold the car at rest after stopping.
- `bControlVerticalVelocity` (`BOOL`): `false` by default which allows gravity to act normally in the z direction. Enable this option to halt the vehicle's vertical velocity as well.

**Devuelve:** `void`

**Descripción oficial:**

This native makes the vehicle stop immediately, as it happens when we enter a multiplayer garage.

**Nombres antiguos (alias):** `0x260BE8F09E326A20` (`N_0x260be8f09e326a20`), `_SET_VEHICLE_HALT` (`SetVehicleHalt`)

---
### CanAnchorBoatHere

`CAN_ANCHOR_BOAT_HERE` · hash `0x26C10ECBDA5D043B` · jhash `0xE97A4F5E` · **Cliente**

```lua
local retval = CanAnchorBoatHere(boat)
```
```c
BOOL CAN_ANCHOR_BOAT_HERE(Vehicle boat);
```

**Parámetros**

- `boat` (`Vehicle`): The boat to check.

**Devuelve:** `BOOL` — Returns `true` if the boat can be safely anchored at its current position, `false` otherwise.

**Descripción oficial:**

Checks if a boat can be anchored at its present position without possibly intersecting collision later.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x2467A2D807D37CA3` (`N_0x2467a2d807d37ca3`), `_GET_BOAT_ANCHOR` (`GetBoatAnchor`), `_CAN_BOAT_BE_ANCHORED` (`CanBoatBeAnchored`)

**Ejemplo (lua):**

```lua
local boat = GetVehiclePedIsIn(PlayerPedId(), false)
if not boat or not IsThisModelABoat(GetEntityModel(boat)) then return end

if CanAnchorBoatHere(boat) then
    print("It's safe to anchor the boat here")
else
    print("It's not safe to anchor the boat at this location")
end
```

**Ejemplo (js):**

```js
const boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (!boat || !IsThisModelABoat(GetEntityModel(boat))) return;

if (CanAnchorBoatHere(boat)) {
    console.log("It's safe to anchor the boat here");
} else {
    console.log("It's not safe to anchor the boat at this location");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (boat == 0 || !IsThisModelABoat(GetEntityModel(boat))) return;

if (CanAnchorBoatHere(boat))
{
    Debug.WriteLine("It's safe to anchor the boat here");
}
else
{
    Debug.WriteLine("It's not safe to anchor the boat at this location");
}
```

---
### CanAnchorBoatHereIgnorePlayers

`CAN_ANCHOR_BOAT_HERE_IGNORE_PLAYERS` · hash `0x24F4121D07579880` · **Cliente**

```lua
local retval = CanAnchorBoatHereIgnorePlayers(boat)
```
```c
BOOL CAN_ANCHOR_BOAT_HERE_IGNORE_PLAYERS(Vehicle boat);
```

**Parámetros**

- `boat` (`Vehicle`): The boat to check.

**Devuelve:** `BOOL` — Returns `true` if the boat can be safely anchored at its current position (ignoring players on the boat), `false` otherwise.

**Descripción oficial:**

Checks if a boat can be anchored at its present position, ignoring any players standing on the boat.

```
NativeDB Introduced: v678
```

**Nombres antiguos (alias):** `_CAN_BOAT_BE_ANCHORED_2` (`CanBoatBeAnchored_2`), `_CAN_ANCHOR_BOAT_HERE_2` (`CanAnchorBoatHere_2`)

**Ejemplo (lua):**

```lua
local boat = GetVehiclePedIsIn(PlayerPedId(), false)
if not boat or not IsThisModelABoat(GetEntityModel(boat)) then return end

if CanAnchorBoatHereIgnorePlayers(boat) then
    print("It's safe to anchor the boat here, ignoring players on the boat")
else
    print("It's not safe to anchor the boat at this location, even ignoring players")
end
```

**Ejemplo (js):**

```js
const boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (!boat || !IsThisModelABoat(GetEntityModel(boat))) return;

if (CanAnchorBoatHereIgnorePlayers(boat)) {
    console.log("It's safe to anchor the boat here, ignoring players on the boat");
} else {
    console.log("It's not safe to anchor the boat at this location, even ignoring players");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (boat == 0 || !IsThisModelABoat(GetEntityModel(boat))) return;

if (CanAnchorBoatHereIgnorePlayers(boat))
{
    Debug.WriteLine("It's safe to anchor the boat here, ignoring players on the boat");
}
else
{
    Debug.WriteLine("It's not safe to anchor the boat at this location, even ignoring players");
}
```

---
### CanCargobobPickUpEntity

`CAN_CARGOBOB_PICK_UP_ENTITY` · hash `0x2C1D8B3B19E517CC` · **Cliente**

```lua
local retval = CanCargobobPickUpEntity(cargobob, entity)
```
```c
BOOL CAN_CARGOBOB_PICK_UP_ENTITY(Vehicle cargobob, Entity entity);
```

**Parámetros**

- `cargobob` (`Vehicle`): The Cargobob helicopter to be checked.
- `entity` (`Entity`): The entity to be checked for pick-up.

**Devuelve:** `BOOL` — Returns `true` if the Cargobob can pick up the specified entity, `false` otherwise.

**Descripción oficial:**

Determines whether the specified Cargobob can pick up a given entity.

**Nombres antiguos (alias):** `0x2C1D8B3B19E517CC` (`N_0x2c1d8b3b19e517cc`)

**Ejemplo (lua):**

```lua

-- This example checks if the player is in a Cargobob and if the Cargobob can pick up the specified entity.

-- Retrieve the player ped.
local playerPed = PlayerPedId()

-- Retrieve the player's vehicle (cargobob).
local cargobob = GetVehiclePedIsIn(playerPed, false)

-- Retrieve the model hash of the cargobob.
local model = GetEntityModel(cargobob)

-- Check if the vehicle exists and if it's a Cargobob. If not, terminate the script.
if not DoesEntityExist(cargobob) or GetHashKey("cargobob") ~= model then
    return
end

local entityID = 15362 -- The entity you want to check if the Cargobob can pick up (this is a random entity ID).

-- Check if the entity exists. If not, terminate the script.
if not DoesEntityExist(entityID) then
    return
end

-- Check if the Cargobob can pick up the specified entity.
if CanCargobobPickUpEntity(vehicle, entityID) then
    print("Cargobob can pick up the specified entity")
else
    print("Cargobob can't pick up the specified entity")
end
```

**Ejemplo (js):**

```js
// This example checks if the player is in a Cargobob and if the Cargobob can pick up the specified entity.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the player's vehicle (cargobob).
const cargobob = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the cargobob.
const model = GetEntityModel(cargobob);

// Check if the vehicle exists and if it's a Cargobob. If not, terminate the script.
if (!DoesEntityExist(cargobob) || GetHashKey("cargobob") !== model) {
    return;
}

const entityID = 15362; // The entity you want to check if the Cargobob can pick up (this is a random entity ID).

// Check if the entity exists. If not, terminate the script.
if (!DoesEntityExist(entityID)) {
    return;
}

// Check if the Cargobob can pick up the specified entity.
if (CanCargobobPickUpEntity(vehicle, entityID)) {
    console.log("Cargobob can pick up the specified entity");
} else {
    console.log("Cargobob can't pick up the specified entity");
}
```

**Ejemplo (cs):**

```cs
// This example checks if the player is in a Cargobob and if the Cargobob can pick up the specified entity.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the player's vehicle (cargobob).
int cargobob = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the cargobob.
uint model = GetEntityModel(cargobob);

// Check if the vehicle exists and if it's a Cargobob. If not, terminate the script.
if (!DoesEntityExist(cargobob) || model != (uint)GetHashKey("cargobob")) {
    return;
}

int entityID = 15362; // The entity you want to check if the Cargobob can pick up (this is a random entity ID).

// Check if the entity exists. If not, terminate the script.
if (!DoesEntityExist(entityID)) {
    return;
}

// Check if the Cargobob can pick up the specified entity.
if (CanCargobobPickUpEntity(vehicle, entityID)) {
    Debug.WriteLine("Cargobob can pick up the specified entity");
} else {
    Debug.WriteLine("Cargobob can't pick up the specified entity");
}
```

---
### CanShuffleSeat

`CAN_SHUFFLE_SEAT` · hash `0x30785D90C956BF35` · jhash `0xB3EB01ED` · **Cliente**

```lua
local retval = CanShuffleSeat(vehicle, seatIndex)
```
```c
BOOL CAN_SHUFFLE_SEAT(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](#isvehicleseatfree).

**Devuelve:** `BOOL`

---
### ClearLastDrivenVehicle

`CLEAR_LAST_DRIVEN_VEHICLE` · hash `0xE01903C47C7AC89E` · jhash `0x07186AD9` · **Cliente**

```lua
ClearLastDrivenVehicle()
```
```c
void CLEAR_LAST_DRIVEN_VEHICLE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE01903C47C7AC89E` (`N_0xe01903c47c7ac89e`)

---
### ClearNitrous

`CLEAR_NITROUS` · hash `0xC889AE921400E1ED` · **Cliente**

```lua
ClearNitrous(vehicle)
```
```c
void CLEAR_NITROUS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle whose nitrous system needs to be cleared.

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: 3095
```

Resets or clears the nitrous system for a specified vehicle. You can check if a vehicle has nitrous with [`IS_NITROUS_ACTIVE`](#isnitrousactive)

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if vehicle == 0 then return end

-- Check if nitrous is active on the vehicle.
if IsNitrousActive(vehicle) then
    -- If nitrous is active, clear the nitrous boost from the vehicle.
    ClearNitrous(vehicle)
end
```

**Ejemplo (js):**

```js
// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Check if nitrous is active on the vehicle.
if (IsNitrousActive(vehicle)) {
    // If nitrous is active, clear the nitrous boost from the vehicle.
    ClearNitrous(vehicle);
}
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

// Check if nitrous is active on the vehicle.
if (IsNitrousActive(vehicle)) {
    // If nitrous is active, clear the nitrous boost from the vehicle.
    ClearNitrous(vehicle);
}
```

---
### ClearVehicleCustomPrimaryColour

`CLEAR_VEHICLE_CUSTOM_PRIMARY_COLOUR` · hash `0x55E1D2758F34E437` · jhash `0x51E1E33D` · **Cliente**

```lua
ClearVehicleCustomPrimaryColour(vehicle)
```
```c
void CLEAR_VEHICLE_CUSTOM_PRIMARY_COLOUR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### ClearVehicleCustomSecondaryColour

`CLEAR_VEHICLE_CUSTOM_SECONDARY_COLOUR` · hash `0x5FFBDEEC3E8E2009` · jhash `0x7CE00B29` · **Cliente**

```lua
ClearVehicleCustomSecondaryColour(vehicle)
```
```c
void CLEAR_VEHICLE_CUSTOM_SECONDARY_COLOUR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### ClearVehicleGeneratorAreaOfInterest

`CLEAR_VEHICLE_GENERATOR_AREA_OF_INTEREST` · hash `0x0A436B8643716D14` · jhash `0x6C73E45A` · **Cliente**

```lua
ClearVehicleGeneratorAreaOfInterest()
```
```c
void CLEAR_VEHICLE_GENERATOR_AREA_OF_INTEREST();
```

**Devuelve:** `void`

**Descripción oficial:**

Removes the cargen area of interest and resumes normal cargen spawning.

You can set the area of interest with [`SET_VEHICLE_GENERATOR_AREA_OF_INTEREST`](VEHICLE-2.md#setvehiclegeneratorareaofinterest)

**Nombres antiguos (alias):** `0x0A436B8643716D14` (`N_0x0a436b8643716d14`)

**Ejemplo (lua):**

```lua
-- This example clears the area of interest (cargen) and resumes normal spawning
ClearVehicleGeneratorAreaOfInterest()
```

**Ejemplo (js):**

```js
// This example clears the area of interest (cargen) and resumes normal spawning
ClearVehicleGeneratorAreaOfInterest();
```

**Ejemplo (cs):**

```cs
// This example clears the area of interest (cargen) and resumes normal spawning
using static CitizenFX.Core.Native.API;

ClearVehicleGeneratorAreaOfInterest();
```

---
### ClearVehiclePhoneExplosiveDevice

`_CLEAR_VEHICLE_PHONE_EXPLOSIVE_DEVICE` · hash `0xAA3F739ABDDCF21F` · **Cliente**

```lua
ClearVehiclePhoneExplosiveDevice()
```
```c
void _CLEAR_VEHICLE_PHONE_EXPLOSIVE_DEVICE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAA3F739ABDDCF21F` (`N_0xaa3f739abddcf21f`)

---
### ClearVehicleRouteHistory

`CLEAR_VEHICLE_ROUTE_HISTORY` · hash `0x6D6AF961B72728AE` · jhash `0x8DD9AA0C` · **Cliente**

```lua
ClearVehicleRouteHistory(vehicle)
```
```c
void CLEAR_VEHICLE_ROUTE_HISTORY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6D6AF961B72728AE` (`N_0x6d6af961b72728ae`)

---
### CloseBombBayDoors

`CLOSE_BOMB_BAY_DOORS` · hash `0x3556041742A0DC74` · jhash `0xF8EC5751` · **Cliente**

```lua
CloseBombBayDoors(vehicle)
```
```c
void CLOSE_BOMB_BAY_DOORS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3556041742A0DC74` (`N_0x3556041742a0dc74`)

---
### ControlLandingGear

`CONTROL_LANDING_GEAR` · hash `0xCFC8BE9A5E1FE575` · jhash `0x24F873FB` · **Cliente**

```lua
ControlLandingGear(vehicle, state)
```
```c
void CONTROL_LANDING_GEAR(Vehicle vehicle, int state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Works for vehicles with a retractable landing gear  
landing gear states:  
0: Deployed  
1: Closing  
2: Opening  
3: Retracted  
```

**Nombres antiguos (alias):** `_SET_VEHICLE_LANDING_GEAR` (`SetVehicleLandingGear`)

---
### CopyVehicleDamages

`COPY_VEHICLE_DAMAGES` · hash `0xE44A982368A4AF23` · jhash `0xBAE491C7` · **Cliente**

```lua
CopyVehicleDamages(sourceVehicle, targetVehicle)
```
```c
void COPY_VEHICLE_DAMAGES(Vehicle sourceVehicle, Vehicle targetVehicle);
```

**Parámetros**

- `sourceVehicle` (`Vehicle`): The source to copy the vehicle damage.
- `targetVehicle` (`Vehicle`): The target to paste the vehicle damage.

**Devuelve:** `void`

**Descripción oficial:**

Copies sourceVehicle's damage (broken bumpers, broken lights, etc.) to targetVehicle.

**Nombres antiguos (alias):** `0xE44A982368A4AF23` (`N_0xe44a982368a4af23`)

---
### CreateMissionTrain

`CREATE_MISSION_TRAIN` · hash `0x63C6CCA8E68AE8C8` · jhash `0xD4C2EAFD` · **Cliente**

```lua
local retval = CreateMissionTrain(variation, x, y, z, direction)
```
```c
Vehicle CREATE_MISSION_TRAIN(int variation, float x, float y, float z, BOOL direction);
```

**Parámetros**

- `variation` (`int`): The variation id, these can range from 0 to 26 as of build 2802 (previously `0-25` in build 2372 and `0-24` before that).
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `direction` (`BOOL`): The direction in which the train will go (true or false)

**Devuelve:** `Vehicle` — A script handle (fwScriptGuid index) for the train, or 0 if the train failed to be created.

**Descripción oficial:**

Train models must be [requested](STREAMING.md#requestmodel) before use. See trains.xml (located in `Grand Theft Auto V\update\update.rpf\common\data\levels\gta5\trains.xml`) for freight and metro variations.

Model names to request can be found by searching `model_name` in the file.

The `Lua` usage example provided down below has been provided in such way so users can test each and every train variation.

**Newly added parameters (seen in 2372 build)**

```
NativeDB Added Parameter 6: BOOL isNetwork
NativeDB Added Parameter 7: BOOL netMissionEntity
```

*   **isNetwork**: Whether to create a network object for the train. If false, the train exists only locally.
*   **netMissionEntity**: Whether to register the train as pinned to the script host in the R\* network model.

**Train Models:**

*   freight

**Carriage Models:**

*   freightcar
*   freightcar2 (Added v2372)
*   freightcont1
*   freightcont2
*   freightgrain
*   metrotrain
*   tankercar

**Some train variations (default from trains.xml as of build 2372)**

*   17. Very long train and freight variation.
*   18. Freight train only.
*   26. Double metro train (with both models flipped opposite to each other). This used to be `25` before the 2802 build, it also used to be `24` before the 2372 build.

**Ejemplo (lua):**

```lua
--[[ 
    This function needs to be invoked prior to calling CreateMissionTrain  or the trains (as well as its carriages) won't spawn.
    Could also result in a game-crash when CreateMissionTrain is called without
    loading the train model needed for the variation before-hand.
]]
function loadTrainModels()
    local trainsAndCarriages = {
        'freight', 'metrotrain', 'freightcont1', 'freightcar', 
        'freightcar2', 'freightcont2', 'tankercar', 'freightgrain'
    }

    for _, vehicleName in ipairs(trainsAndCarriages) do
        local modelHashKey = GetHashKey(vehicleName)
        RequestModel(modelHashKey) -- load the model
        -- wait for the model to load
        while not HasModelLoaded(modelHashKey) do
            Citizen.Wait(500)
        end
    end
end

loadTrainModels()

RegisterCommand("createtrain", function(source, args, rawCommand)
    if #args < 1 then
        TriggerEvent('chat:addMessage', {
            args = { 
                'Error, provide a variation id, you can find those in trains.xml. Variations range from 0 to 26.'
            }
        })
        return
    end
    
    local playerCoords = GetEntityCoords(PlayerPedId())
     -- Now actually create a train using a variation
     -- These coordinates were used for testing: 1438.98, 6405.92, 34.19
    CreateMissionTrain(
        tonumber(args[1]),
        playerCoords.x, playerCoords.y, playerCoords.z,
        true,
        true,
        true
    )
end, false)
```

---
### CreatePickUpRopeForCargobob

`CREATE_PICK_UP_ROPE_FOR_CARGOBOB` · hash `0x7BEB0C7A235F6F3B` · jhash `0x4D3C9A99` · **Cliente**

```lua
CreatePickUpRopeForCargobob(cargobob, state)
```
```c
void CREATE_PICK_UP_ROPE_FOR_CARGOBOB(Vehicle cargobob, int state);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `state` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Drops the Hook/Magnet on a cargobob

```cpp
enum eCargobobHook  
{  
	CARGOBOB_HOOK = 0,  
	CARGOBOB_MAGNET = 1,  
};  
```

**Nombres antiguos (alias):** `_ENABLE_CARGOBOB_HOOK` (`EnableCargobobHook`)

---
### CreateScriptVehicleGenerator

`CREATE_SCRIPT_VEHICLE_GENERATOR` · hash `0x9DEF883114668116` · jhash `0x25A9A261` · **Cliente**

```lua
local retval = CreateScriptVehicleGenerator(x, y, z, heading, p4, p5, modelHash, p7, p8, p9, p10, p11, p12, p13, p14, p15, p16)
```
```c
int CREATE_SCRIPT_VEHICLE_GENERATOR(float x, float y, float z, float heading, float p4, float p5, Hash modelHash, int p7, int p8, int p9, int p10, BOOL p11, BOOL p12, BOOL p13, BOOL p14, BOOL p15, int p16);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p7` (`int`)
- `p8` (`int`)
- `p9` (`int`)
- `p10` (`int`)
- `p11` (`BOOL`)
- `p12` (`BOOL`)
- `p13` (`BOOL`)
- `p14` (`BOOL`)
- `p15` (`BOOL`)
- `p16` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Creates a script vehicle generator at the given coordinates. Most parameters after the model hash are unknown.  
Parameters:  
a/w/s - Generator position  
heading - Generator heading  
p4 - Unknown (always 5.0)  
p5 - Unknown (always 3.0)  
modelHash - Vehicle model hash  
p7/8/9/10 - Unknown (always -1)  
p11 - Unknown (usually TRUE, only one instance of FALSE)  
p12/13 - Unknown (always FALSE)  
p14 - Unknown (usally FALSE, only two instances of TRUE)  
p15 - Unknown (always TRUE)  
p16 - Unknown (always -1)  
Vector3 coords = GET_ENTITY_COORDS(PLAYER_PED_ID(), 0);	CREATE_SCRIPT_VEHICLE_GENERATOR(coords.x, coords.y, coords.z, 1.0f, 5.0f, 3.0f, GET_HASH_KEY("adder"), -1. -1, -1, -1, -1, true, false, false, false, true, -1);  
```

---
### CreateVehicle

`CREATE_VEHICLE` · hash `0xAF35D0D2583051B0` · jhash `0xDD75460A` · **Cliente · también en el servidor (RPC)**

```lua
local retval = CreateVehicle(modelHash, x, y, z, heading, isNetwork, netMissionEntity)
```
```c
Vehicle CREATE_VEHICLE(Hash modelHash, float x, float y, float z, float heading, BOOL isNetwork, BOOL netMissionEntity);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model of vehicle to spawn.
- `x` (`float`): Spawn coordinate X component.
- `y` (`float`): Spawn coordinate Y component.
- `z` (`float`): Spawn coordinate Z component.
- `heading` (`float`): Heading to face towards, in degrees.
- `isNetwork` (`BOOL`): Whether to create a network object for the vehicle. If false, the vehicle exists only locally.
- `netMissionEntity` (`BOOL`): Whether to register the vehicle as pinned to the script host in the R\* network model.

**Devuelve:** `Vehicle` — A script handle (fwScriptGuid index) for the vehicle, or `0` if the vehicle failed to be created.

**Descripción oficial:**

Creates a vehicle with the specified model at the specified position. This vehicle will initially be owned by the creating
script as a mission entity, and the model should be loaded already (e.g. using REQUEST_MODEL).

```
NativeDB Added Parameter 8: BOOL p7
```

**Ejemplo (lua):**

```lua
local ModelHash = `adder` -- Use Compile-time hashes to get the hash of this model
if not IsModelInCdimage(ModelHash) then return end
RequestModel(ModelHash) -- Request the model
while not HasModelLoaded(ModelHash) do -- Waits for the model to load
  Wait(0)
end
local MyPed = PlayerPedId()
local Vehicle = CreateVehicle(ModelHash, GetEntityCoords(MyPed), GetEntityHeading(MyPed), true, false) -- Spawns a networked vehicle on your current coords
SetModelAsNoLongerNeeded(ModelHash) -- removes model from game memory as we no longer need it
```

---
### DeleteAllTrains

`DELETE_ALL_TRAINS` · hash `0x736A718577F39C7D` · jhash `0x83DE7ABF` · **Cliente**

```lua
DeleteAllTrains()
```
```c
void DELETE_ALL_TRAINS();
```

**Devuelve:** `void`

---
### DeleteMissionTrain

`DELETE_MISSION_TRAIN` · hash `0x5B76B14AE875C795` · jhash `0x86C9497D` · **Cliente**

```lua
local train = DeleteMissionTrain(train)
```
```c
void DELETE_MISSION_TRAIN(Vehicle* train);
```

**Parámetros**

- `train` (`Vehicle*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

Used to delete mission trains created with [`CREATE_MISSION_TRAIN`](#createmissiontrain).

**Ejemplo (lua):**

```lua
local train = CreateMissionTrain(21, 40.2, -1201.3, 31.0, false)
DeleteMissionTrain(train)
```

---
### DeleteScriptVehicleGenerator

`DELETE_SCRIPT_VEHICLE_GENERATOR` · hash `0x22102C9ABFCF125D` · jhash `0xE4328E3F` · **Cliente**

```lua
DeleteScriptVehicleGenerator(vehicleGenerator)
```
```c
void DELETE_SCRIPT_VEHICLE_GENERATOR(int vehicleGenerator);
```

**Parámetros**

- `vehicleGenerator` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Removes a scripted vehicle generator.

---
### DeleteVehicle

`DELETE_VEHICLE` · hash `0xEA386986E786A54F` · jhash `0x9803AF60` · **Cliente**

```lua
local vehicle = DeleteVehicle(vehicle)
```
```c
void DELETE_VEHICLE(Vehicle* vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Deletes a vehicle.  
The vehicle must be a mission entity to delete, so call this before deleting: SET_ENTITY_AS_MISSION_ENTITY(vehicle, true, true);  
eg how to use:  
SET_ENTITY_AS_MISSION_ENTITY(vehicle, true, true);  
DELETE_VEHICLE(&vehicle);  
Deletes the specified vehicle, then sets the handle pointed to by the pointer to NULL.  
```

---
### DetachContainerFromHandlerFrame

`DETACH_CONTAINER_FROM_HANDLER_FRAME` · hash `0x7C0043FDFF6436BC` · jhash `0x0F11D01F` · **Cliente**

```lua
DetachContainerFromHandlerFrame(vehicle)
```
```c
void DETACH_CONTAINER_FROM_HANDLER_FRAME(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7C0043FDFF6436BC` (`N_0x7c0043fdff6436bc`)

---
### DetachEntityFromCargobob

`DETACH_ENTITY_FROM_CARGOBOB` · hash `0xAF03011701811146` · **Cliente**

```lua
local retval = DetachEntityFromCargobob(vehicle, entity)
```
```c
Any DETACH_ENTITY_FROM_CARGOBOB(Vehicle vehicle, Entity entity);
```

**Parámetros**

- `vehicle` (`Vehicle`): The Cargobob helicopter.
- `entity` (`Entity`): The entity to be detached.

**Devuelve:** `Any`

**Descripción oficial:**

Detaches the specified entity currently being carried by a Cargobob.

**Nombres antiguos (alias):** `0xAF03011701811146` (`N_0xaf03011701811146`), `_DETACH_ENTITY_FROM_CARGOBOB` (`DetachEntityFromCargobob`)

**Ejemplo (lua):**

```lua
-- This example detaches a specific entity from a Cargobob.

-- Retrieve the player ped.
local playerPed = PlayerPedId()

-- Retrieve the player's vehicle (cargobob).
local cargobob = GetVehiclePedIsIn(playerPed, false)

-- Retrieve the model hash of the cargobob.
local cargobobModel = GetEntityModel(cargobob)

-- Check if the vehicle exists and if it's a Cargobob. If not, terminate the script.
if not DoesEntityExist(cargobob) or cargobobModel ~= GetHashKey("cargobob") then
    return
end

local entityID = 15362 -- The entity you want to detach from the Cargobob (this is a random entity ID).

-- Check if the entity exists; if not, terminate the script.
if not DoesEntityExist(yourEntity) then
    return
end

-- Detach the entity from the Cargobob.
DetachEntityFromCargobob(cargobob, entityID)
```

**Ejemplo (js):**

```js
// This example detaches a specific entity from a Cargobob.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the player's vehicle.
const cargobob = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the cargobob.
const cargobobModel = GetEntityModel(cargobob);

// Check if the player is in a Cargobob and if the vehicle is a Cargobob; if not, terminate the script.
if (!DoesEntityExist(cargobob) || cargobobModel !== GetHashKey("cargobob")) {
    return;
}

const entityID = 15362; // The entity you want to detach from the Cargobob (this is a random entity ID).

// Check if the entity exists; if not, terminate the script.
if (!DoesEntityExist(entityID)) {
    return;
}

// Detach the entity from the Cargobob.
DetachEntityFromCargobob(cargobob, entityID);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// This example detaches a specific entity from a Cargobob.

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the player's vehicle.
int cargobob = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the cargobob.
uint cargobobModel = (uint)GetEntityModel(cargobob);

// Check if the player is in a Cargobob and if the vehicle is a Cargobob; if not, terminate the script.
if (!DoesEntityExist(cargobob) || cargobobModel != (uint)GetHashKey("cargobob")) {
    return;
}

int entityID = 15362; // The entity you want to detach from the Cargobob (this is a random entity ID).

// Check if the entity exists; if not, terminate the script.
if (!DoesEntityExist(entityID)) {
    return;
}

// Detach the entity from the Cargobob.
DetachEntityFromCargobob(cargobob, entityID);
```

---
### DetachVehicleFromAnyCargobob

`DETACH_VEHICLE_FROM_ANY_CARGOBOB` · hash `0xADF7BE450512C12F` · jhash `0x50E0EABE` · **Cliente**

```lua
local retval = DetachVehicleFromAnyCargobob(vehicle)
```
```c
BOOL DETACH_VEHICLE_FROM_ANY_CARGOBOB(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### DetachVehicleFromAnyTowTruck

`DETACH_VEHICLE_FROM_ANY_TOW_TRUCK` · hash `0xD0E9CE05A1E68CD8` · jhash `0x3BF93651` · **Cliente**

```lua
local retval = DetachVehicleFromAnyTowTruck(vehicle)
```
```c
BOOL DETACH_VEHICLE_FROM_ANY_TOW_TRUCK(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### DetachVehicleFromCargobob

`DETACH_VEHICLE_FROM_CARGOBOB` · hash `0x0E21D3DF1051399D` · jhash `0x83D3D331` · **Cliente**

```lua
DetachVehicleFromCargobob(cargobob, vehicle)
```
```c
void DETACH_VEHICLE_FROM_CARGOBOB(Vehicle cargobob, Vehicle vehicle);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### DetachVehicleFromTowTruck

`DETACH_VEHICLE_FROM_TOW_TRUCK` · hash `0xC2DB6B6708350ED8` · jhash `0xC666CF33` · **Cliente**

```lua
DetachVehicleFromTowTruck(towTruck, vehicle)
```
```c
void DETACH_VEHICLE_FROM_TOW_TRUCK(Vehicle towTruck, Vehicle vehicle);
```

**Parámetros**

- `towTruck` (`Vehicle`)
- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
First two parameters swapped. Scripts verify that towTruck is the first parameter, not the second.  
```

---
### DetachVehicleFromTrailer

`DETACH_VEHICLE_FROM_TRAILER` · hash `0x90532EDF0D2BDD86` · jhash `0xB5DBF91D` · **Cliente**

```lua
DetachVehicleFromTrailer(vehicle)
```
```c
void DETACH_VEHICLE_FROM_TRAILER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### DetonateVehiclePhoneExplosiveDevice

`DETONATE_VEHICLE_PHONE_EXPLOSIVE_DEVICE` · hash `0xEF49CF0270307CBE` · jhash `0x65255524` · **Cliente**

```lua
DetonateVehiclePhoneExplosiveDevice()
```
```c
void DETONATE_VEHICLE_PHONE_EXPLOSIVE_DEVICE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEF49CF0270307CBE` (`N_0xef49cf0270307cbe`), `_REQUEST_VEHICLE_PHONE_EXPLOSION` (`RequestVehiclePhoneExplosion`)

---
### DisableIndividualPlanePropeller

`DISABLE_INDIVIDUAL_PLANE_PROPELLER` · hash `0x500873A45724C863` · jhash `0x004926A3` · **Cliente**

```lua
DisableIndividualPlanePropeller(vehicle, propeller)
```
```c
void DISABLE_INDIVIDUAL_PLANE_PROPELLER(Vehicle vehicle, int propeller);
```

**Parámetros**

- `vehicle` (`Vehicle`): The propeller plane
- `propeller` (`int`): The propeller index to disable (starts at 0).

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x500873A45724C863` (`N_0x500873a45724c863`), `_DISABLE_PLANE_PROPELLER` (`DisablePlanePropeller`)

---
### DisablePlaneAileron

`DISABLE_PLANE_AILERON` · hash `0x23428FC53C60919C` · jhash `0x7E84C45C` · **Cliente**

```lua
DisablePlaneAileron(vehicle, p1, p2)
```
```c
void DISABLE_PLANE_AILERON(Vehicle vehicle, BOOL p1, BOOL p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### DisableVehicleNeonLights

`_DISABLE_VEHICLE_NEON_LIGHTS` · hash `0x83F813570FF519DE` · **Cliente**

```lua
DisableVehicleNeonLights(vehicle, toggle)
```
```c
void _DISABLE_VEHICLE_NEON_LIGHTS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x83F813570FF519DE` (`N_0x83f813570ff519de`)

---
### DisableVehicleTurretMovementThisFrame

`_DISABLE_VEHICLE_TURRET_MOVEMENT_THIS_FRAME` · hash `0x32CAEDF24A583345` · **Cliente**

```lua
DisableVehicleTurretMovementThisFrame(vehicle)
```
```c
void _DISABLE_VEHICLE_TURRET_MOVEMENT_THIS_FRAME(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x32CAEDF24A583345` (`N_0x32caedf24a583345`)

---
### DisableVehicleWeapon

`DISABLE_VEHICLE_WEAPON` · hash `0xF4FC6A6F67D8D856` · jhash `0xA688B7D1` · **Cliente**

```lua
DisableVehicleWeapon(disabled, weaponHash, vehicle, owner)
```
```c
void DISABLE_VEHICLE_WEAPON(BOOL disabled, Hash weaponHash, Vehicle vehicle, Ped owner);
```

**Parámetros**

- `disabled` (`BOOL`): A boolean indicating whether to disable (`true`) or enable (`false`) the weapon.
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The specific hash of the vehicle weapon (e.g., `GetHashKey("VEHICLE_WEAPON_TANK")`).
- `vehicle` (`Vehicle`): The vehicle entity handle.
- `owner` (`Ped`): The ped entity for whom the weapon is disabled. This acts as a ped-specific lock; the ped does not need to be inside the vehicle or in a specific seat when this native is called.

**Devuelve:** `void`

**Descripción oficial:**

Disables or enables a specific weapon on a vehicle for a designated ped.

**Ejemplo (lua):**

```lua
-- Disables the Rhino's Tank gun for the local player
local ped = PlayerPedId()
local vehicle = GetVehiclePedIsIn(ped, false)
local weaponHash = GetHashKey("VEHICLE_WEAPON_TANK")

if vehicle ~= 0 then
    DisableVehicleWeapon(true, weaponHash, vehicle, ped)
end
```

**Ejemplo (js):**

```js
// Disables the Rhino's Tank gun for the local player
const ped = PlayerPedId();
const vehicle = GetVehiclePedIsIn(ped, false);
const weaponHash = GetHashKey("VEHICLE_WEAPON_TANK");

if (vehicle !== 0) {
    DisableVehicleWeapon(true, weaponHash, vehicle, ped);
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Disables the Rhino's Tank gun for the local player
int ped = PlayerPedId();
int vehicle = GetVehiclePedIsIn(ped, false);
uint weaponHash = (uint)GetHashKey("VEHICLE_WEAPON_TANK");

if (vehicle != 0) 
{
    DisableVehicleWeapon(true, weaponHash, vehicle, ped);
}
```

---
### DisableVehicleWorldCollision

`_DISABLE_VEHICLE_WORLD_COLLISION` · hash `0x75627043C6AA90AD` · **Cliente**

```lua
DisableVehicleWorldCollision(vehicle)
```
```c
void _DISABLE_VEHICLE_WORLD_COLLISION(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): the vehicle to disable world collisions for

**Devuelve:** `void`

**Descripción oficial:**

Disables collision for this vehicle (maybe it also supports other entities, not sure).
Only world/building/fixed world objects will have their collisions disabled, props, peds, or any other entity still collides with the vehicle.

[Example video](https://streamable.com/6n45d5)

Not sure if there is a native (and if so, which one) that resets the collisions.

**Nombres antiguos (alias):** `0x75627043C6AA90AD` (`N_0x75627043c6aa90ad`)

---
### DoesCargobobHavePickUpRope

`DOES_CARGOBOB_HAVE_PICK_UP_ROPE` · hash `0x1821D91AD4B56108` · jhash `0xAF769B81` · **Cliente**

```lua
local retval = DoesCargobobHavePickUpRope(cargobob)
```
```c
BOOL DOES_CARGOBOB_HAVE_PICK_UP_ROPE(Vehicle cargobob);
```

**Parámetros**

- `cargobob` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true only when the hook is active, will return false if the magnet is active  
```

**Nombres antiguos (alias):** `_IS_CARGOBOB_HOOK_ACTIVE` (`IsCargobobHookActive`)

---
### DoesCargobobHavePickupMagnet

`DOES_CARGOBOB_HAVE_PICKUP_MAGNET` · hash `0x6E08BF5B3722BAC9` · jhash `0x4778CA0A` · **Cliente**

```lua
local retval = DoesCargobobHavePickupMagnet(cargobob)
```
```c
BOOL DOES_CARGOBOB_HAVE_PICKUP_MAGNET(Vehicle cargobob);
```

**Parámetros**

- `cargobob` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true only when the magnet is active, will return false if the hook is active  
```

**Nombres antiguos (alias):** `_IS_CARGOBOB_MAGNET_ACTIVE` (`IsCargobobMagnetActive`), `_DOES_CARGOBOB_HAVE_PICKUP_MAGNET` (`DoesCargobobHavePickupMagnet`)

---
### DoesExtraExist

`DOES_EXTRA_EXIST` · hash `0x1262D55792428154` · jhash `0x409411CC` · **Cliente**

```lua
local retval = DoesExtraExist(vehicle, extraId)
```
```c
BOOL DOES_EXTRA_EXIST(Vehicle vehicle, int extraId);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `extraId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks via CVehicleModelInfo  
```

---
### DoesScriptVehicleGeneratorExist

`DOES_SCRIPT_VEHICLE_GENERATOR_EXIST` · hash `0xF6086BC836400876` · jhash `0xF6BDDA30` · **Cliente**

```lua
local retval = DoesScriptVehicleGeneratorExist(vehicleGenerator)
```
```c
BOOL DOES_SCRIPT_VEHICLE_GENERATOR_EXIST(int vehicleGenerator);
```

**Parámetros**

- `vehicleGenerator` (`int`)

**Devuelve:** `BOOL`

---
### DoesVehicleAllowRappel

`_DOES_VEHICLE_ALLOW_RAPPEL` · hash `0x4E417C547182C84D` · jhash `0x0E28D3A6` · **Cliente**

```lua
local retval = DoesVehicleAllowRappel(vehicle)
```
```c
BOOL _DOES_VEHICLE_ALLOW_RAPPEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the vehicle has the FLAG_ALLOWS_RAPPEL flag set.
```

**Nombres antiguos (alias):** `0x4E417C547182C84D` (`N_0x4e417c547182c84d`)

---
### DoesVehicleExistWithDecorator

`DOES_VEHICLE_EXIST_WITH_DECORATOR` · hash `0x956B409B984D9BF7` · jhash `0x39E68EDD` · **Cliente**

```lua
local retval = DoesVehicleExistWithDecorator(decorator)
```
```c
BOOL DOES_VEHICLE_EXIST_WITH_DECORATOR(char* decorator);
```

**Parámetros**

- `decorator` (`char*`)

**Devuelve:** `BOOL`

---
### DoesVehicleHaveLandingGear

`_DOES_VEHICLE_HAVE_LANDING_GEAR` · hash `0xE43701C36CAFF1A4` · **Cliente**

```lua
local retval = DoesVehicleHaveLandingGear(vehicle)
```
```c
BOOL _DOES_VEHICLE_HAVE_LANDING_GEAR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0xE43701C36CAFF1A4` (`N_0xe43701c36caff1a4`), `_GET_VEHICLE_HAS_LANDING_GEAR` (`GetVehicleHasLandingGear`)

---
### DoesVehicleHaveRoof

`DOES_VEHICLE_HAVE_ROOF` · hash `0x8AC862B0B32C5B80` · jhash `0xDB817403` · **Cliente**

```lua
local retval = DoesVehicleHaveRoof(vehicle)
```
```c
BOOL DOES_VEHICLE_HAVE_ROOF(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check for a roof presence.

**Devuelve:** `BOOL` — Returns `true` if the vehicle has a roof, `false` otherwise.

**Descripción oficial:**

Determines whether a specific vehicle is equipped with a roof.

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if DoesVehicleHaveRoof(vehicle) then
    print("This vehicle has a roof.")
else
    print("This vehicle does not have a roof.")
end
```

**Ejemplo (js):**

```js
let vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (DoesVehicleHaveRoof(vehicle)) {
    console.log("This vehicle has a roof.");
} else {
    console.log("This vehicle does not have a roof.");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (DoesVehicleHaveRoof(vehicle)) {
    Debug.WriteLine("This vehicle has a roof.");
} else {
    Debug.WriteLine("This vehicle does not have a roof.");
}
```

---
### DoesVehicleHaveSearchlight

`DOES_VEHICLE_HAVE_SEARCHLIGHT` · hash `0x99015ED7DBEA5113` · **Cliente**

```lua
local retval = DoesVehicleHaveSearchlight(vehicle)
```
```c
BOOL DOES_VEHICLE_HAVE_SEARCHLIGHT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check for the presence of a searchlight.

**Devuelve:** `BOOL` — Returns `true` if the vehicle has a searchlight, `false` otherwise.

**Descripción oficial:**

Determines whether the specified vehicle is equipped with a searchlight.

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `_DOES_VEHICLE_HAVE_SEARCHLIGHT` (`DoesVehicleHaveSearchlight`)

---
### DoesVehicleHaveStuckVehicleCheck

`DOES_VEHICLE_HAVE_STUCK_VEHICLE_CHECK` · hash `0x57E4C39DE5EE8470` · jhash `0x5D91D9AC` · **Cliente**

```lua
local retval = DoesVehicleHaveStuckVehicleCheck(vehicle)
```
```c
BOOL DOES_VEHICLE_HAVE_STUCK_VEHICLE_CHECK(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Maximum amount of vehicles with vehicle stuck check appears to be 16.  
```

---
### DoesVehicleHaveWeapons

`DOES_VEHICLE_HAVE_WEAPONS` · hash `0x25ECB9F8017D98E0` · jhash `0xB2E1E1FB` · **Cliente**

```lua
local retval = DoesVehicleHaveWeapons(vehicle)
```
```c
BOOL DOES_VEHICLE_HAVE_WEAPONS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### DoesVehicleTyreExist

`_DOES_VEHICLE_TYRE_EXIST` · hash `0x534E36D4DB9ECC5D` · **Cliente**

```lua
local retval = DoesVehicleTyreExist(vehicle, tyreIndex)
```
```c
BOOL _DOES_VEHICLE_TYRE_EXIST(Vehicle vehicle, int tyreIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `tyreIndex` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks if vehicle tyre at index exists. Also returns false if tyre was removed.
```

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x534E36D4DB9ECC5D` (`N_0x534e36d4db9ecc5d`)

---
### EjectJb700Roof

`_EJECT_JB700_ROOF` · hash `0xE38CB9D7D39FDBCC` · jhash `0xFDA7B6CA` · **Cliente**

```lua
EjectJb700Roof(vehicle, x, y, z)
```
```c
void _EJECT_JB700_ROOF(Vehicle vehicle, float x, float y, float z);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE38CB9D7D39FDBCC` (`N_0xe38cb9d7d39fdbcc`)

---
### EnableAircraftObstacleAvoidance

`_ENABLE_AIRCRAFT_OBSTACLE_AVOIDANCE` · hash `0x8AA9180DE2FEDD45` · jhash `0xAE040377` · **Cliente**

```lua
EnableAircraftObstacleAvoidance(vehicle, avoidObstacles)
```
```c
void _ENABLE_AIRCRAFT_OBSTACLE_AVOIDANCE(Vehicle vehicle, BOOL avoidObstacles);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle to toggle obstacle avoidance for.
- `avoidObstacles` (`BOOL`): `true` / `false` to enable/disable heightmap obstacle avoidance respectively!

**Devuelve:** `void`

**Descripción oficial:**

Will disable a plane or a helicopter's need to swerve around object in its heightmap when using TASK_PLANE_MISSION or other AI / Pilot behavior.  Will ensure plane flys directly to it's destination or die trying! This native does NOT need to be called every frame, but instead, just called once on the vehicle (NOT THE PED) you're trying to disable avoidance for!

**Nombres antiguos (alias):** `_0x8AA9180DE2FEDD45` (`N_0x8aa9180de2fedd45`)

---
### EnableIndividualPlanePropeller

`_ENABLE_INDIVIDUAL_PLANE_PROPELLER` · hash `0xDC05D2777F855F44` · **Cliente**

```lua
EnableIndividualPlanePropeller(plane, propeller)
```
```c
void _ENABLE_INDIVIDUAL_PLANE_PROPELLER(Vehicle plane, int propeller);
```

**Parámetros**

- `plane` (`Vehicle`): The propeller plane.
- `propeller` (`int`): The propeller index to enable (starts at 0).

**Devuelve:** `void`

**Descripción oficial:**

Enables individual propeller on a propeller plane. This native is the inverse of [`DISABLE_INDIVIDUAL_PLANE_PROPELLER`](#disableindividualplanepropeller).

```
NativeDB Introduced: v3407
```

**Ejemplo (lua):**

```lua
CreateThread(function()
    local vehicle = GetVehiclePedIsIn(PlayerPedId(), false) -- The plane used in this example is the cuban800

    DisableIndividualPlanePropeller(vehicle, 0)
    DisableIndividualPlanePropeller(vehicle, 1)
    -- We are disabling both propellers so we can start a specific one (since both are automatically started when entering the plane)
    Wait(5000) -- We are waiting 5 seconds
    EnableIndividualPlanePropeller(vehicle, 1) -- Starting the second propeller (since the index starts at 0)
end)
```

---
### ExplodeVehicle

`EXPLODE_VEHICLE` · hash `0xBA71116ADF5B514C` · jhash `0xBEDEACEB` · **Cliente**

```lua
ExplodeVehicle(vehicle, isAudible, isInvisible)
```
```c
void EXPLODE_VEHICLE(Vehicle vehicle, BOOL isAudible, BOOL isInvisible);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `isAudible` (`BOOL`)
- `isInvisible` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Explodes a selected vehicle.  
Vehicle vehicle = Vehicle you want to explode.  
BOOL isAudible = If explosion makes a sound.  
BOOL isInvisible = If the explosion is invisible or not.  
First BOOL does not give any visual explosion, the vehicle just falls apart completely but slowly and starts to burn.  
```

---
### ExplodeVehicleInCutscene

`EXPLODE_VEHICLE_IN_CUTSCENE` · hash `0x786A4EB67B01BF0B` · jhash `0xA85207B5` · **Cliente**

```lua
ExplodeVehicleInCutscene(vehicle, p1)
```
```c
void EXPLODE_VEHICLE_IN_CUTSCENE(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### FindRandomPointInSpace

`_FIND_RANDOM_POINT_IN_SPACE` · hash `0x8DC9675797123522` · **Cliente**

```lua
local retval = FindRandomPointInSpace(ped)
```
```c
Vector3 _FIND_RANDOM_POINT_IN_SPACE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Vector3`

**Descripción oficial:**

Native is significantly more complicated than simply generating a random vector & length.

The 'point' is either 400.0 or 250.0 units away from the Ped's current coordinates; and paths into functions like rage::grcViewport\_\__IsSphereVisible.

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x8DC9675797123522` (`N_0x8dc9675797123522`)

---
### FindVehicleCarryingThisEntity

`_FIND_VEHICLE_CARRYING_THIS_ENTITY` · hash `0x375E7FC44F21C8AB` · jhash `0x70DD5E25` · **Cliente**

```lua
local retval = FindVehicleCarryingThisEntity(entity)
```
```c
Vehicle _FIND_VEHICLE_CARRYING_THIS_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `Vehicle`

**Descripción oficial:**

```
Finds the vehicle that is carrying this entity with a handler frame.
The model of the entity must be prop_contr_03b_ld or the function will return 0.
```

**Nombres antiguos (alias):** `0x375E7FC44F21C8AB` (`N_0x375e7fc44f21c8ab`), `_GET_VEHICLE_ATTACHED_TO_ENTITY` (`GetVehicleAttachedToEntity`)

---
### FixVehicleWindow

`FIX_VEHICLE_WINDOW` · hash `0x772282EBEB95E682` · jhash `0x6B8E990D` · **Cliente**

```lua
FixVehicleWindow(vehicle, windowIndex)
```
```c
void FIX_VEHICLE_WINDOW(Vehicle vehicle, int windowIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `windowIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

See eWindowId declared in [`IS_VEHICLE_WINDOW_INTACT`](../cfx/servidor.md#isvehiclewindowintact).

This function is coded to not work on vehicles of type: `CBike`, `Bmx`, `CBoat`, `CTrain`, and `CSubmarine`.

---
### ForcePlaybackRecordedVehicleUpdate

`FORCE_PLAYBACK_RECORDED_VEHICLE_UPDATE` · hash `0x1F2E4E06DEA8992B` · jhash `0x01B91CD0` · **Cliente**

```lua
ForcePlaybackRecordedVehicleUpdate(vehicle, p1)
```
```c
void FORCE_PLAYBACK_RECORDED_VEHICLE_UPDATE(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Often called after START_PLAYBACK_RECORDED_VEHICLE and SKIP_TIME_IN_PLAYBACK_RECORDED_VEHICLE; similar in use to FORCE_ENTITY_AI_AND_ANIMATION_UPDATE.
```

**Nombres antiguos (alias):** `0x1F2E4E06DEA8992B` (`N_0x1f2e4e06dea8992b`)

---
### ForceSubmarineNeurtalBuoyancy

`FORCE_SUBMARINE_NEURTAL_BUOYANCY` · hash `0xC67DB108A9ADE3BE` · **Cliente**

```lua
ForceSubmarineNeurtalBuoyancy(submarine, time)
```
```c
void FORCE_SUBMARINE_NEURTAL_BUOYANCY(Vehicle submarine, int time);
```

**Parámetros**

- `submarine` (`Vehicle`): The submarine vehicle to apply neutral buoyancy to.
- `time` (`int`): The duration in milliseconds for which to maintain neutral buoyancy.

**Devuelve:** `void`

**Descripción oficial:**

Forces a submarine to maintain neutral buoyancy for a specified duration, preventing it from rising when unoccupied or without a driver.

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `0xC67DB108A9ADE3BE` (`N_0xc67db108a9ade3be`)

---
### ForceSubmarineSurfaceMode

`FORCE_SUBMARINE_SURFACE_MODE` · hash `0x33506883545AC0DF` · jhash `0x54E9EE75` · **Cliente**

```lua
ForceSubmarineSurfaceMode(vehicle, toggle)
```
```c
void FORCE_SUBMARINE_SURFACE_MODE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x33506883545AC0DF` (`N_0x33506883545ac0df`)

---
### FullyChargeNitrous

`FULLY_CHARGE_NITROUS` · hash `0x1A2BCC8C636F9226` · **Cliente**

```lua
FullyChargeNitrous(vehicle)
```
```c
void FULLY_CHARGE_NITROUS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle whose nitrous system is to be fully recharged.

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3095
```

Recharges the nitrous system of the specified vehicle to its maximum capacity. This action sets the nitrous charge duration to the maximum limit defined by previous settings applied through [`SET_OVERRIDE_NITROUS_LEVEL`](VEHICLE-2.md#setoverridenitrouslevel).

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if vehicle == 0 then return end

-- Set nitrous modifications with SET_OVERRIDE_NITROUS_LEVEL since this native require a durationMod to be specified.
SetOverrideNitrousLevel(vehicle, true, 1.5, 2.0, 0.5, false)

-- After setting the modifiers, fully recharge the nitrous system to the new max defined.
FullyChargeNitrous(vehicle)
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Set nitrous modifications with SET_OVERRIDE_NITROUS_LEVEL since this native require a durationMod to be specified.
SetOverrideNitrousLevel(vehicle, true, 1.5, 2.0, 0.5, false);

// After setting the modifiers, fully recharge the nitrous system to the new max defined.
FullyChargeNitrous(vehicle);
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

// Set nitrous modifications with SET_OVERRIDE_NITROUS_LEVEL since this native require a durationMod to be specified.
SetOverrideNitrousLevel(vehicle, true, 1.5, 2.0, 0.5, false);

// After setting the modifiers, fully recharge the nitrous system to the new max defined.
FullyChargeNitrous(vehicle);
```

---
### GetAllVehicles

`GET_ALL_VEHICLES` · hash `0x9B8E1BF04B51F2E8` · **Cliente**

```lua
local retval, vehArray = GetAllVehicles(vehArray)
```
```c
int GET_ALL_VEHICLES(int* vehArray);
```

**Parámetros**

- `vehArray` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int` — Returns all vehicles in the vehicle game pool.

**Descripción oficial:**

For FiveM, use [`GET_GAME_POOL`](../cfx/compartidos.md#getgamepool).

**Nombres antiguos (alias):** `_GET_ALL_VEHICLES` (`GetAllVehicles`)

---
### GetBoatBoomPositionRatio

`GET_BOAT_BOOM_POSITION_RATIO` · hash `0x6636C535F6CC2725` · jhash `0x7C8D6464` · **Cliente**

```lua
local retval = GetBoatBoomPositionRatio(vehicle)
```
```c
float GET_BOAT_BOOM_POSITION_RATIO(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x6636C535F6CC2725` (`N_0x6636c535f6cc2725`)

---
### GetBoatBoomPositionRatio_2

`_GET_BOAT_BOOM_POSITION_RATIO_2` · hash `0xC1F981A6F74F0C23` · jhash `0x00966934` · **Cliente**

```lua
GetBoatBoomPositionRatio_2(vehicle, p1)
```
```c
void _GET_BOAT_BOOM_POSITION_RATIO_2(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Same call as VEHICLE::_0x0F3B4D4E43177236
```

**Nombres antiguos (alias):** `0xC1F981A6F74F0C23` (`N_0xc1f981a6f74f0c23`)

---
### GetBoatBoomPositionRatio_3

`_GET_BOAT_BOOM_POSITION_RATIO_3` · hash `0x0F3B4D4E43177236` · jhash `0x113DF5FD` · **Cliente**

```lua
GetBoatBoomPositionRatio_3(vehicle, p1)
```
```c
void _GET_BOAT_BOOM_POSITION_RATIO_3(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0F3B4D4E43177236` (`N_0x0f3b4d4e43177236`)

---
### GetBoatVehicleModelAgility

`GET_BOAT_VEHICLE_MODEL_AGILITY` · hash `0x5AA3F878A178C4FC` · jhash `0x87C5D271` · **Cliente**

```lua
local retval = GetBoatVehicleModelAgility(modelHash)
```
```c
float GET_BOAT_VEHICLE_MODEL_AGILITY(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model hash of the boat.

**Devuelve:** `float` — Returns the agility value of the specified boat as a float number.

**Descripción oficial:**

Retrieves the agility for a specific boat model, including any vehicle mods. Unlike other vehicles where Rockstar Games typically assess performance based on traction, boats use agility as a measure. This static value is distinct from the traction metrics used for other vehicle types.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x5AA3F878A178C4FC` (`N_0x5aa3f878a178c4fc`), `_GET_VEHICLE_MODEL_MOVE_RESISTANCE` (`GetVehicleModelMoveResistance`)

**Ejemplo (lua):**

```lua
-- This example prints the agility of the player's current boat.

-- Retrieve the player ped.
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in.
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Retrieve the model hash of the boat.
local boatHash = GetEntityModel(vehicle)

-- If the vehicle does not exist or is not a boat, end the execution of the code here.
if not DoesEntityExist(vehicle) or not IsThisModelABoat(boatHash) then 
    return 
end

-- Retrieve the agility of the boat.
local agility = GetBoatVehicleModelAgility(boatHash)

-- Print the agility of the boat.
print("Boat Agility: " .. agility)
```

**Ejemplo (js):**

```js
// This example prints the agility of the player's current boat.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the boat.
const boatHash = GetEntityModel(vehicle);

// If the vehicle does not exist or is not a boat, end the execution of the code here.
if (!DoesEntityExist(vehicle) || !IsThisModelABoat(boatHash)) {
  return;
}

// Retrieve the agility of the boat.
const agility = GetBoatVehicleModelAgility(boatHash);

// Print the agility of the boat.
console.log(`Boat Agility: ${agility}`);
```

**Ejemplo (cs):**

```cs
// This example prints the agility of the player's current boat.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the boat.
uint boatHash = GetEntityModel(vehicle);

// If the vehicle does not exist or is not a boat, end the execution of the code here.
if (!DoesEntityExist(vehicle) || !IsThisModelABoat(boatHash)) {
  return;
}

// Retrieve the agility of the boat.
float agility = GetBoatVehicleModelAgility(boatHash);

// Print the agility of the boat.
Debug.WriteLine($"Boat Agility: {agility}");
```

---
### GetCanVehicleJump

`_GET_CAN_VEHICLE_JUMP` · hash `0x9078C0C5EF8C19E9` · **Cliente**

```lua
local retval = GetCanVehicleJump(vehicle)
```
```c
BOOL _GET_CAN_VEHICLE_JUMP(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the vehicle has the FLAG_JUMPING_CAR flag set.
```

**Nombres antiguos (alias):** `_HAS_VEHICLE_JUMPING_ABILITY` (`HasVehicleJumpingAbility`), `_DOES_VEHICLE_HAVE_JUMPING_ABILITY` (`DoesVehicleHaveJumpingAbility`)

---
### GetCargobobHookPosition

`_GET_CARGOBOB_HOOK_POSITION` · hash `0xCBDB9B923CACC92D` · jhash `0xE6633DCF` · **Cliente**

```lua
local retval = GetCargobobHookPosition(cargobob)
```
```c
Vector3 _GET_CARGOBOB_HOOK_POSITION(Vehicle cargobob);
```

**Parámetros**

- `cargobob` (`Vehicle`)

**Devuelve:** `Vector3`

**Descripción oficial:**

Gets the position of the cargobob hook, in world coords.

**Nombres antiguos (alias):** `0xCBDB9B923CACC92D` (`N_0xcbdb9b923cacc92d`)

---
### GetClosestVehicle

`GET_CLOSEST_VEHICLE` · hash `0xF73EB622C4F1689B` · jhash `0xD7E26B2C` · **Cliente**

```lua
local retval = GetClosestVehicle(x, y, z, radius, modelHash, flags)
```
```c
Vehicle GET_CLOSEST_VEHICLE(float x, float y, float z, float radius, Hash modelHash, int flags);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `flags` (`int`)

**Devuelve:** `Vehicle`

**Descripción oficial:**

```
Example usage  
VEHICLE::GET_CLOSEST_VEHICLE(x, y, z, radius, hash, unknown leave at 70)   
x, y, z: Position to get closest vehicle to.  
radius: Max radius to get a vehicle.  
modelHash: Limit to vehicles with this model. 0 for any.  
flags: The bitwise flags altering the function's behaviour.  
Does not return police cars or helicopters.  
It seems to return police cars for me, does not seem to return helicopters, planes or boats for some reason  
Only returns non police cars and motorbikes with the flag set to 70 and modelHash to 0. ModelHash seems to always be 0 when not a modelHash in the scripts, as stated above.   
These flags were found in the b617d scripts: 0,2,4,6,7,23,127,260,2146,2175,12294,16384,16386,20503,32768,67590,67711,98309,100359.  
Converted to binary, each bit probably represents a flag as explained regarding another native here: gtaforums.com/topic/822314-guide-driving-styles  
Conversion of found flags to binary: pastebin.com/kghNFkRi  
At exactly 16384 which is 0100000000000000 in binary and 4000 in hexadecimal only planes are returned.   
It's probably more convenient to use worldGetAllVehicles(int *arr, int arrSize) and check the shortest distance yourself and sort if you want by checking the vehicle type with for example VEHICLE::IS_THIS_MODEL_A_BOAT  
-------------------------------------------------------------------------  
Conclusion: This native is not worth trying to use. Use something like this instead: pastebin.com/xiFdXa7h
Use flag 127 to return police cars
```

---
### GetConvertibleRoofState

`GET_CONVERTIBLE_ROOF_STATE` · hash `0xF8C397922FC03F41` · jhash `0x1B09714D` · **Cliente**

```lua
local retval = GetConvertibleRoofState(vehicle)
```
```c
int GET_CONVERTIBLE_ROOF_STATE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle to get the state of

**Devuelve:** `int` — Returns the current roof state, refer to `eRoofState`

**Descripción oficial:**

Returns the convertible state of the specified vehicle.

```cpp
enum eRoofState {
    RAISED = 0,
    LOWERING = 1,
    LOWERED = 2,
    RAISING = 3,
    CLOSING_BOOT = 4,
    ROOF_STUCK_RAISED = 5,
    ROOF_STUCK_LOWERED = 6
}
```

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId())
print(GetConvertibleRoofState(vehicle))
```

---
### GetCurrentPlaybackForVehicle

`GET_CURRENT_PLAYBACK_FOR_VEHICLE` · hash `0x42BC05C27A946054` · jhash `0xA3F44390` · **Cliente**

```lua
local retval = GetCurrentPlaybackForVehicle(vehicle)
```
```c
int GET_CURRENT_PLAYBACK_FOR_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetDisplayNameFromVehicleModel

`GET_DISPLAY_NAME_FROM_VEHICLE_MODEL` · hash `0xB215AAC32D25D019` · jhash `0xEC86DF39` · **Cliente**

```lua
local retval = GetDisplayNameFromVehicleModel(modelHash)
```
```c
char* GET_DISPLAY_NAME_FROM_VEHICLE_MODEL(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: A vehicle model to check.

**Devuelve:** `char*` — The display name for the vehicle, or `'CARNOTFOUND'` if invalid.

**Descripción oficial:**

Returns the display name/text label (`gameName` in `vehicles.meta`) for the specified vehicle model.

---
### GetDoesVehicleHaveTombstone

`_GET_DOES_VEHICLE_HAVE_TOMBSTONE` · hash `0x71AFB258CCED3A27` · **Cliente**

```lua
local retval = GetDoesVehicleHaveTombstone(vehicle)
```
```c
BOOL _GET_DOES_VEHICLE_HAVE_TOMBSTONE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### GetDriftTyresEnabled

`_GET_DRIFT_TYRES_ENABLED` · hash `0x2F5A72430E78C8D3` · **Cliente**

```lua
local retval = GetDriftTyresEnabled(vehicle)
```
```c
BOOL _GET_DRIFT_TYRES_ENABLED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### GetEntityAttachedToCargobob

`_GET_ENTITY_ATTACHED_TO_CARGOBOB` · hash `0x99093F60746708CA` · **Cliente**

```lua
local retval = GetEntityAttachedToCargobob(vehicle)
```
```c
Entity _GET_ENTITY_ATTACHED_TO_CARGOBOB(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `Entity`

**Nombres antiguos (alias):** `0x99093F60746708CA` (`N_0x99093f60746708ca`)

---
### GetEntityAttachedToTowTruck

`GET_ENTITY_ATTACHED_TO_TOW_TRUCK` · hash `0xEFEA18DCF10F8F75` · jhash `0x11EC7844` · **Cliente**

```lua
local retval = GetEntityAttachedToTowTruck(towTruck)
```
```c
Entity GET_ENTITY_ATTACHED_TO_TOW_TRUCK(Vehicle towTruck);
```

**Parámetros**

- `towTruck` (`Vehicle`)

**Devuelve:** `Entity`

---
### GetEntryPositionOfDoor

`_GET_ENTRY_POSITION_OF_DOOR` · hash `0xC0572928C0ABFDA3` · **Cliente**

```lua
local retval = GetEntryPositionOfDoor(vehicle, doorIndex)
```
```c
Vector3 _GET_ENTRY_POSITION_OF_DOOR(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](VEHICLE-2.md#setvehicledoorshut)

---
### GetHasRetractableWheels

`_GET_HAS_RETRACTABLE_WHEELS` · hash `0xDCA174A42133F08C` · **Cliente**

```lua
local retval = GetHasRetractableWheels(vehicle)
```
```c
BOOL _GET_HAS_RETRACTABLE_WHEELS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_GET_HAS_LOWERABLE_WHEELS` (`GetHasLowerableWheels`), `_DOES_VEHICLE_HAVE_RETRACTABLE_WHEELS` (`DoesVehicleHaveRetractableWheels`)

---
### GetHasRocketBoost

`_GET_HAS_ROCKET_BOOST` · hash `0x36D782F68B309BDA` · **Cliente**

```lua
local retval = GetHasRocketBoost(vehicle)
```
```c
BOOL _GET_HAS_ROCKET_BOOST(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_HAS_VEHICLE_ROCKET_BOOST` (`HasVehicleRocketBoost`), `_DOES_VEHICLE_HAVE_ROCKET_BOOST` (`DoesVehicleHaveRocketBoost`)

---
### GetHeliMainRotorHealth

`GET_HELI_MAIN_ROTOR_HEALTH` · hash `0xE4CB7541F413D2C5` · jhash `0xF01E2AAB` · **Cliente**

```lua
local retval = GetHeliMainRotorHealth(vehicle)
```
```c
float GET_HELI_MAIN_ROTOR_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Max 1000.  
At 0 the main rotor will stall.  
```

**Nombres antiguos (alias):** `_GET_HELI_MAIN_ROTOR_HEALTH` (`GetHeliMainRotorHealth`)

---
### GetHeliTailBoomHealth

`GET_HELI_TAIL_BOOM_HEALTH` · hash `0xAC51915D27E4A5F7` · jhash `0x8A68388F` · **Cliente**

```lua
local retval = GetHeliTailBoomHealth(vehicle)
```
```c
float GET_HELI_TAIL_BOOM_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Max 1000.
At -100 both helicopter rotors will stall.
```

**Nombres antiguos (alias):** `_GET_HELI_ENGINE_HEALTH` (`GetHeliEngineHealth`)

---
### GetHeliTailRotorHealth

`GET_HELI_TAIL_ROTOR_HEALTH` · hash `0xAE8CE82A4219AC8C` · jhash `0xA41BC13D` · **Cliente**

```lua
local retval = GetHeliTailRotorHealth(heli)
```
```c
float GET_HELI_TAIL_ROTOR_HEALTH(Vehicle heli);
```

**Parámetros**

- `heli` (`Vehicle`): Helicopter for which you want to get the rotor health.

**Devuelve:** `float` — Returns the health of the rear rotor of the helicopter, not the tail rotor as the name suggests. The maximum value is 1000. At 0, the tail rotor will stall.

**Descripción oficial:**

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `_GET_HELI_TAIL_ROTOR_HEALTH` (`GetHeliTailRotorHealth`)

---
### GetHydraulicWheelValue

`_GET_HYDRAULIC_WHEEL_VALUE` · hash `0x0BB5CBDDD0F25AE3` · **Cliente**

```lua
local retval = GetHydraulicWheelValue(vehicle, wheelId)
```
```c
float _GET_HYDRAULIC_WHEEL_VALUE(Vehicle vehicle, int wheelId);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelId` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### GetIsBoatCapsized

`GET_IS_BOAT_CAPSIZED` · hash `0xBA91D045575699AD` · **Cliente**

```lua
local retval = GetIsBoatCapsized(vehicle)
```
```c
BOOL GET_IS_BOAT_CAPSIZED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check. This should be a boat-type vehicle.

**Devuelve:** `BOOL` — Returns `true` if the specified boat is capsized, `false` otherwise.

**Descripción oficial:**

Checks whether the specified boat vehicle is capsized, meaning it has overturned or is upside down in the water.

**Nombres antiguos (alias):** `0xBA91D045575699AD` (`N_0xba91d045575699ad`)

**Ejemplo (lua):**

```lua
-- This example checks if the player is in a boat and if the boat is capsized.

-- Retrieve the LocalPlayer.
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is in
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Retrieve the model of the vehicle
local vehicleModel = GetEntityModel(vehicle)

-- Check if the vehicle exists in the game world.
if not DoesEntityExist(vehicle) then 
    -- If the vehicle does not exist, end the execution of the code here.
    return 
end

-- Check if the vehicle is a boat.
if not IsThisModelABoat(vehicleModel) then
    -- If the vehicle is not a boat, end the execution of the code here.
    return
end

-- Check if the boat is capsized.
if GetIsBoatCapsized(vehicle) then
    print("The boat is capsized!")
else
    print("The boat is not capsized!")
end
```

**Ejemplo (js):**

```js
// This example checks if the player is in a boat and if the boat is capsized.

// Retrieve the LocalPlayer.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is in
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model of the vehicle
const vehicleModel = GetEntityModel(vehicle);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
  // If the vehicle does not exist, end the execution of the code here.
  return;
}

// Check if the vehicle is a boat.
if (!IsThisModelABoat(vehicleModel)) {
  // If the vehicle is not a boat, end the execution of the code here.
  return;
}

// Check if the boat is capsized
if (GetIsBoatCapsized(vehicle)) {
    console.log("The boat is capsized!");
} else {
    console.log("The boat is not capsized!");
}
```

**Ejemplo (cs):**

```cs
// This example checks if the player is in a boat and if the boat is capsized.
using static CitizenFX.Core.Native.API;

// Retrieve the LocalPlayer.
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is in
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model of the vehicle
uint vehicleModel = (uint)GetEntityModel(vehicle);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle))
{
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// Check if the vehicle is a boat.
if (!IsThisModelABoat(vehicleModel))
{
    // If the vehicle is not a boat, end the execution of the code here.
    return;
}

// Check if the boat is capsized
if (GetIsBoatCapsized(vehicle))
{
    Debug.WriteLine("The boat is capsized!");
}
else
{
    Debug.WriteLine("The boat is not capsized!");
}
```

---
### GetIsDoorValid

`_GET_IS_DOOR_VALID` · hash `0x645F4B6E8499F632` · **Cliente**

```lua
local retval = GetIsDoorValid(vehicle, doorIndex)
```
```c
BOOL _GET_IS_DOOR_VALID(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](VEHICLE-2.md#setvehicledoorshut)

**Nombres antiguos (alias):** `_DOES_VEHICLE_HAVE_DOOR` (`DoesVehicleHaveDoor`)

---
### GetIsLeftVehicleHeadlightDamaged

`GET_IS_LEFT_VEHICLE_HEADLIGHT_DAMAGED` · hash `0x5EF77C9ADD3B11A3` · jhash `0xA0777943` · **Cliente**

```lua
local retval = GetIsLeftVehicleHeadlightDamaged(vehicle)
```
```c
BOOL GET_IS_LEFT_VEHICLE_HEADLIGHT_DAMAGED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
From the driver's perspective, is the left headlight broken.  
```

**Nombres antiguos (alias):** `_IS_HEADLIGHT_L_BROKEN` (`IsHeadlightLBroken`)

---
### GetIsRightVehicleHeadlightDamaged

`GET_IS_RIGHT_VEHICLE_HEADLIGHT_DAMAGED` · hash `0xA7ECB73355EB2F20` · jhash `0xF178390B` · **Cliente**

```lua
local retval = GetIsRightVehicleHeadlightDamaged(vehicle)
```
```c
BOOL GET_IS_RIGHT_VEHICLE_HEADLIGHT_DAMAGED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
From the driver's perspective, is the right headlight broken.  
```

**Nombres antiguos (alias):** `_IS_HEADLIGHT_R_BROKEN` (`IsHeadlightRBroken`)

---
### GetIsVehicleElectric

`_GET_IS_VEHICLE_ELECTRIC` · hash `0x1FCB07FE230B6639` · **Cliente**

```lua
local retval = GetIsVehicleElectric(vehicleModel)
```
```c
BOOL _GET_IS_VEHICLE_ELECTRIC(Hash vehicleModel);
```

**Parámetros**

- `vehicleModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of the vehicle model to check.

**Devuelve:** `BOOL` — Returns `true` if the vehicle is electric or `false` otherwise.

**Descripción oficial:**

Checks if the vehicle is electric.

```
NativeDB Introduced: v3258
```

**Ejemplo (lua):**

```lua
local veh = GetVehiclePedIsIn(PlayerPedId(), false)
-- GetVehiclePedIsIn will return 0 if the ped isn't currently in a vehicle
if veh == 0 then return end
local model = GetEntityModel(veh)
if GetIsVehicleElectric(model) then
    print("This vehicle is electric")
else
    print("This vehicle is not electric")
end
```

---
### GetIsVehicleEmpDisabled

`_GET_IS_VEHICLE_EMP_DISABLED` · hash `0x0506ED94363AD905` · **Cliente**

```lua
local retval = GetIsVehicleEmpDisabled(vehicle)
```
```c
BOOL _GET_IS_VEHICLE_EMP_DISABLED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether this vehicle is currently disabled by an EMP mine.

NativeDB Introduced: v1604
```

---
### GetIsVehicleEngineRunning

`GET_IS_VEHICLE_ENGINE_RUNNING` · hash `0xAE31E7DF9B5B132E` · jhash `0x7DC6D022` · **Cliente**

```lua
local retval = GetIsVehicleEngineRunning(vehicle)
```
```c
BOOL GET_IS_VEHICLE_ENGINE_RUNNING(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true when in a vehicle, false whilst entering/exiting.  
```

**Nombres antiguos (alias):** `_IS_VEHICLE_ENGINE_ON` (`IsVehicleEngineOn`)

---
### GetIsVehiclePrimaryColourCustom

`GET_IS_VEHICLE_PRIMARY_COLOUR_CUSTOM` · hash `0xF095C0405307B21B` · jhash `0xD7EC8760` · **Cliente**

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

`GET_IS_VEHICLE_SECONDARY_COLOUR_CUSTOM` · hash `0x910A32E7AAD2656C` · jhash `0x288AD228` · **Cliente**

```lua
local retval = GetIsVehicleSecondaryColourCustom(vehicle)
```
```c
BOOL GET_IS_VEHICLE_SECONDARY_COLOUR_CUSTOM(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Check if Vehicle Secondary is avaliable for customize  
```

---
### GetIsVehicleShuntBoostActive

`_GET_IS_VEHICLE_SHUNT_BOOST_ACTIVE` · hash `0xA2459F72C14E2E8D` · **Cliente**

```lua
local retval = GetIsVehicleShuntBoostActive(vehicle)
```
```c
BOOL _GET_IS_VEHICLE_SHUNT_BOOST_ACTIVE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### GetIsWheelsLoweredStateActive

`_GET_IS_WHEELS_LOWERED_STATE_ACTIVE` · hash `0x1DA0DA9CB3F0C8BF` · **Cliente**

```lua
local retval = GetIsWheelsLoweredStateActive(vehicle)
```
```c
BOOL _GET_IS_WHEELS_LOWERED_STATE_ACTIVE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1DA0DA9CB3F0C8BF` (`N_0x1da0da9cb3f0c8bf`)

---
### GetLandingGearState

`GET_LANDING_GEAR_STATE` · hash `0x9B0F3DCA3DB0F4CD` · jhash `0xA6F02670` · **Cliente**

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

```
Landing gear states:  
0: Deployed  
1: Closing (Retracting)
3: Opening (Deploying)
4: Retracted  
5: Broken
```

Landing gear state 2 is never used.

**Nombres antiguos (alias):** `_GET_VEHICLE_LANDING_GEAR` (`GetVehicleLandingGear`)

---
### GetLastDrivenVehicle

`GET_LAST_DRIVEN_VEHICLE` · hash `0xB2D06FAEDE65B577` · jhash `0xFEB0C0C8` · **Cliente**

```lua
local retval = GetLastDrivenVehicle()
```
```c
Vehicle GET_LAST_DRIVEN_VEHICLE();
```

**Devuelve:** `Vehicle`

**Nombres antiguos (alias):** `0xB2D06FAEDE65B577` (`N_0xb2d06faede65b577`)

---
### GetLastPedInVehicleSeat

`GET_LAST_PED_IN_VEHICLE_SEAT` · hash `0x83F969AA1EE2A664` · jhash `0xF7C6792D` · **Cliente**

```lua
local retval = GetLastPedInVehicleSeat(vehicle, seatIndex)
```
```c
Ped GET_LAST_PED_IN_VEHICLE_SEAT(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to get the ped for.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](#isvehicleseatfree).

**Devuelve:** `Ped`

---
### GetLastRammedVehicle

`_GET_LAST_RAMMED_VEHICLE` · hash `0x04F2FA6E234162F7` · **Cliente**

```lua
local retval = GetLastRammedVehicle(vehicle)
```
```c
Vehicle _GET_LAST_RAMMED_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `Vehicle`

**Descripción oficial:**

```
Returns last vehicle that was rammed by the given vehicle using the shunt boost.

NativeDB Introduced: v1604
```

---
### GetLiveryName

`GET_LIVERY_NAME` · hash `0xB4C7A93837C91A1F` · jhash `0xED80B5BE` · **Cliente**

```lua
local retval = GetLiveryName(vehicle, liveryIndex)
```
```c
char* GET_LIVERY_NAME(Vehicle vehicle, int liveryIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `liveryIndex` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Second Param = LiveryIndex  
example   
int count = VEHICLE::GET_VEHICLE_LIVERY_COUNT(veh);  
for (int i = 0; i < count; i++)    
	{  
char* LiveryName = VEHICLE::GET_LIVERY_NAME(veh, i);  
	}  
this example will work fine to fetch all names   
for example for Sanchez we get   
SANC_LV1  
SANC_LV2  
SANC_LV3  
SANC_LV4  
SANC_LV5  
Use _GET_LABEL_TEXT, to get the localized livery name.  
```

NOTE: You may need to set the vehicle's modKit to 0 by using this function [SET_VEHICLE_MOD_KIT](VEHICLE-2.md#setvehiclemodkit) before getting the name, otherwise this native may return NULL.

---
### GetMakeNameFromVehicleModel

`GET_MAKE_NAME_FROM_VEHICLE_MODEL` · hash `0xF7AF4F159FF99F97` · **Cliente**

```lua
local retval = GetMakeNameFromVehicleModel(modelHash)
```
```c
char* GET_MAKE_NAME_FROM_VEHICLE_MODEL(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model hash of the vehicle.

**Devuelve:** `char*` — Returns the display label of the manufacturer if the vehicle model is recognized, or "CARNOTFOUND" if the hash does not correspond to any known vehicle model.

**Descripción oficial:**

Retrieves the manufacturer's name for a specified vehicle.

```
NativeDB Introduced: v1868
```

**Nombres antiguos (alias):** `_GET_MAKE_NAME_FROM_VEHICLE_MODEL` (`GetMakeNameFromVehicleModel`)

**Ejemplo (lua):**

```lua
-- This example prints the manufacturer of the player's current vehicle.

-- Retrieve the player ped.
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in.
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- If the vehicle does not exist, end the execution of the code here.
if not DoesEntityExist(vehicle) then 
    return 
end

-- Retrieve the model hash of the vehicle.
local vehicleHash = GetEntityModel(vehicle)

-- Retrieve the manufacturer of the vehicle.
local manufacturer = GetMakeNameFromVehicleModel(vehicleHash)

-- Print the manufacturer of the vehicle.
print("Vehicle Manufacturer: " .. manufacturer)
```

**Ejemplo (js):**

```js
// This example prints the manufacturer of the player's current vehicle.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// If the vehicle does not exist, end the execution of the code here.
if (!DoesEntityExist(vehicle)) {
  return;
}

// Retrieve the model hash of the vehicle.
const vehicleHash = GetEntityModel(vehicle);

// Retrieve the manufacturer of the vehicle.
const manufacturer = GetMakeNameFromVehicleModel(vehicleHash);

// Print the manufacturer of the vehicle.
console.log(`Vehicle Manufacturer: ${manufacturer}`);
```

**Ejemplo (cs):**

```cs
// This example prints the manufacturer of the player's current vehicle.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// If the vehicle does not exist, end the execution of the code here.
if (!DoesEntityExist(vehicle)) {
  return;
}

// Retrieve the model hash of the vehicle.
uint vehicleHash = (uint)GetEntityModel(vehicle);

// Retrieve the manufacturer of the vehicle.
string manufacturer = GetMakeNameFromVehicleModel(vehicleHash);

// Print the manufacturer of the vehicle.
Debug.WriteLine($"Vehicle Manufacturer: {manufacturer}");
```

---
### GetModSlotName

`GET_MOD_SLOT_NAME` · hash `0x51F0FEB9F6AE98C0` · jhash `0x5E113483` · **Cliente**

```lua
local retval = GetModSlotName(vehicle, modType)
```
```c
char* GET_MOD_SLOT_NAME(Vehicle vehicle, int modType);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).

**Devuelve:** `char*`

---
### GetModTextLabel

`GET_MOD_TEXT_LABEL` · hash `0x8935624F8C5592CC` · jhash `0x0BA39CA7` · **Cliente**

```lua
local retval = GetModTextLabel(vehicle, modType, modValue)
```
```c
char* GET_MOD_TEXT_LABEL(Vehicle vehicle, int modType, int modValue);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).
- `modValue` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns the text label of a mod type for a given vehicle  
Use _GET_LABEL_TEXT to get the part name in the game's language  
```

---
### GetNumModColors

`GET_NUM_MOD_COLORS` · hash `0xA551BE18C11A476D` · jhash `0x73722CD9` · **Cliente**

```lua
local retval = GetNumModColors(paintType, p1)
```
```c
int GET_NUM_MOD_COLORS(int paintType, BOOL p1);
```

**Parámetros**

- `paintType` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
paintType:
0: Normal
1: Metallic
2: Pearl
3: Matte
4: Metal
5: Chrome
```

---
### GetNumModKits

`GET_NUM_MOD_KITS` · hash `0x33F2E3FE70EAAE1D` · jhash `0xE4903AA0` · **Cliente**

```lua
local retval = GetNumModKits(vehicle)
```
```c
int GET_NUM_MOD_KITS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetNumVehicleMods

`GET_NUM_VEHICLE_MODS` · hash `0xE38E9162A2500646` · jhash `0x8A814FF9` · **Cliente**

```lua
local retval = GetNumVehicleMods(vehicle, modType)
```
```c
int GET_NUM_VEHICLE_MODS(Vehicle vehicle, int modType);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).

**Devuelve:** `int`

**Descripción oficial:**

```
Returns how many possible mods a vehicle has for a given mod type  
```

---
### GetNumVehicleWindowTints

`GET_NUM_VEHICLE_WINDOW_TINTS` · hash `0x9D1224004B3A6707` · jhash `0x625C7B66` · **Cliente**

```lua
local retval = GetNumVehicleWindowTints()
```
```c
int GET_NUM_VEHICLE_WINDOW_TINTS();
```

**Devuelve:** `int`

---
### GetNumberOfVehicleColours

`GET_NUMBER_OF_VEHICLE_COLOURS` · hash `0x3B963160CD65D41E` · jhash `0xF2442EE2` · **Cliente**

```lua
local retval = GetNumberOfVehicleColours(vehicle)
```
```c
int GET_NUMBER_OF_VEHICLE_COLOURS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
Actually number of color combinations  
```

---
### GetNumberOfVehicleDoors

`_GET_NUMBER_OF_VEHICLE_DOORS` · hash `0x92922A607497B14D` · **Cliente**

```lua
local retval = GetNumberOfVehicleDoors(vehicle)
```
```c
int _GET_NUMBER_OF_VEHICLE_DOORS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetNumberOfVehicleNumberPlates

`GET_NUMBER_OF_VEHICLE_NUMBER_PLATES` · hash `0x4C4D6B2644F458CB` · jhash `0xD24BC1AE` · **Cliente**

```lua
local retval = GetNumberOfVehicleNumberPlates()
```
```c
int GET_NUMBER_OF_VEHICLE_NUMBER_PLATES();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the number of *types* of licence plates, enumerated below in SET_VEHICLE_NUMBER_PLATE_TEXT_INDEX.  
```

---
### GetPedInVehicleSeat

`GET_PED_IN_VEHICLE_SEAT` · hash `0xBB40DD2270B65366` · jhash `0x388FDE9A` · **Cliente**

```lua
local retval = GetPedInVehicleSeat(vehicle, seatIndex)
```
```c
Ped GET_PED_IN_VEHICLE_SEAT(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to get the ped for.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](#isvehicleseatfree).

**Devuelve:** `Ped` — A handle to a ped in the specified vehicle seat, or 0 if no such ped existed.

**Descripción oficial:**

Gets the ped in the specified seat of the passed vehicle.

If there is no ped in the seat, and the game considers the vehicle as ambient population, this will create a random occupant ped in the seat, which may be cleaned up by the game fairly soon if not marked as script-owned mission entity.

**NativeDB Added Parameter 3**: BOOL p2 (uses a different GetOccupant function)

**Ejemplo (lua):**

```lua
-- Checks if the player ped is in the drivers seat of the vehicle they are in.
if GetPedInVehicleSeat(GetVehiclePedIsIn(PlayerPedId()), -1) == PlayerPedId() then 
  print("The player is the driver of this vehicle.")
else
  print("The player is not the driver of this vehicle.")
end
```

---
### GetPedUsingVehicleDoor

`GET_PED_USING_VEHICLE_DOOR` · hash `0x218297BF0CFD853B` · jhash `0x0630101F` · **Cliente**

```lua
local retval = GetPedUsingVehicleDoor(vehicle, doorIndex)
```
```c
Ped GET_PED_USING_VEHICLE_DOOR(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)

**Devuelve:** `Ped`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](VEHICLE-2.md#setvehicledoorshut)

**Nombres antiguos (alias):** `0x218297BF0CFD853B` (`N_0x218297bf0cfd853b`), `_GET_PED_USING_VEHICLE_DOOR` (`GetPedUsingVehicleDoor`)

---
### GetPositionInRecording

`GET_POSITION_IN_RECORDING` · hash `0x2DACD605FC681475` · jhash `0x7DCD644C` · **Cliente**

```lua
local retval = GetPositionInRecording(vehicle)
```
```c
float GET_POSITION_IN_RECORDING(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Distance traveled in the vehicles current recording.
```

---
### GetPositionOfVehicleRecordingAtTime

`GET_POSITION_OF_VEHICLE_RECORDING_AT_TIME` · hash `0xD242728AA6F0FBA2` · jhash `0x7178558D` · **Cliente**

```lua
local retval = GetPositionOfVehicleRecordingAtTime(recording, time, script)
```
```c
Vector3 GET_POSITION_OF_VEHICLE_RECORDING_AT_TIME(int recording, float time, char* script);
```

**Parámetros**

- `recording` (`int`)
- `time` (`float`)
- `script` (`char*`)

**Devuelve:** `Vector3`

**Descripción oficial:**

This native does no interpolation between pathpoints. The same position will be returned for all times up to the next pathpoint in the recording.

See [`REQUEST_VEHICLE_RECORDING`](#requestvehiclerecording).

---
### GetPositionOfVehicleRecordingIdAtTime

`GET_POSITION_OF_VEHICLE_RECORDING_ID_AT_TIME` · hash `0x92523B76657A517D` · jhash `0xF31973BB` · **Cliente**

```lua
local retval = GetPositionOfVehicleRecordingIdAtTime(id, time)
```
```c
Vector3 GET_POSITION_OF_VEHICLE_RECORDING_ID_AT_TIME(int id, float time);
```

**Parámetros**

- `id` (`int`)
- `time` (`float`)

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `0x92523B76657A517D` (`N_0x92523b76657a517d`)

---
### GetRandomVehicleBackBumperInSphere

`GET_RANDOM_VEHICLE_BACK_BUMPER_IN_SPHERE` · hash `0xB50807EABE20A8DC` · jhash `0xD6343F6B` · **Cliente**

```lua
local retval = GetRandomVehicleBackBumperInSphere(p0, p1, p2, p3, p4, p5, p6)
```
```c
Vehicle GET_RANDOM_VEHICLE_BACK_BUMPER_IN_SPHERE(float p0, float p1, float p2, float p3, int p4, int p5, int p6);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`int`)
- `p5` (`int`)
- `p6` (`int`)

**Devuelve:** `Vehicle`

---
### GetRandomVehicleFrontBumperInSphere

`GET_RANDOM_VEHICLE_FRONT_BUMPER_IN_SPHERE` · hash `0xC5574E0AEB86BA68` · jhash `0xDCADEB66` · **Cliente**

```lua
local retval = GetRandomVehicleFrontBumperInSphere(p0, p1, p2, p3, p4, p5, p6)
```
```c
Vehicle GET_RANDOM_VEHICLE_FRONT_BUMPER_IN_SPHERE(float p0, float p1, float p2, float p3, int p4, int p5, int p6);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`int`)
- `p5` (`int`)
- `p6` (`int`)

**Devuelve:** `Vehicle`

---
### GetRandomVehicleInSphere

`GET_RANDOM_VEHICLE_IN_SPHERE` · hash `0x386F6CE5BAF6091C` · jhash `0x57216D03` · **Cliente**

```lua
local retval = GetRandomVehicleInSphere(x, y, z, radius, modelHash, flags)
```
```c
Vehicle GET_RANDOM_VEHICLE_IN_SPHERE(float x, float y, float z, float radius, Hash modelHash, int flags);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `flags` (`int`)

**Devuelve:** `Vehicle`

**Descripción oficial:**

```
Gets a random vehicle in a sphere at the specified position, of the specified radius.  
x: The X-component of the position of the sphere.  
y: The Y-component of the position of the sphere.  
z: The Z-component of the position of the sphere.  
radius: The radius of the sphere. Max is 9999.9004.  
modelHash: The vehicle model to limit the selection to. Pass 0 for any model.  
flags: The bitwise flags that modifies the behaviour of this function.  
```

---
### GetRandomVehicleModelInMemory

`GET_RANDOM_VEHICLE_MODEL_IN_MEMORY` · hash `0x055BF0AC0C34F4FD` · jhash `0xE2C45631` · **Cliente**

```lua
local modelHash, successIndicator = GetRandomVehicleModelInMemory(p0)
```
```c
void GET_RANDOM_VEHICLE_MODEL_IN_MEMORY(BOOL p0, Hash* modelHash, int* successIndicator);
```

**Parámetros**

- `p0` (`BOOL`)
- `modelHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `successIndicator` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Not present in the retail version! It's just a nullsub.  
p0 always true (except in one case)  
p1 a random vehicle hash loaded in memory  
successIndicator: 0 if success, -1 if failed
```

---
### GetRemainingNitrousDuration

`_GET_REMAINING_NITROUS_DURATION` · hash `0xBEC4B8653462450E` · **Cliente**

```lua
local retval = GetRemainingNitrousDuration(vehicle)
```
```c
float _GET_REMAINING_NITROUS_DURATION(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle for which to retrieve the remaining nitrous duration.

**Devuelve:** `float` — The amount of time that the nitrous boost can still be active for the given vehicle. If there is no nitrous system active or available, this may return `0`.```lua CreateThread(function()     local playerPed, vehicle     while true do         -- Retrieve the player ped.         playerPed = PlayerPedId()          -- Retrieve the vehicle the player is currently in.         vehicle = GetVehiclePedIsIn(playerPed, false)          -- Retrieve if the nitrous of the vehicle is active.         if IsNitrousActive(vehicle) then             print(GetRemainingNitrousDuration(vehicle))         end          Wait(0)     end end) ``````js setTick(async () => {     // Retrieve the player ped.     let playerPed = PlayerPedId();          // Retrieve the vehicle the player is currently in.     let vehicle = GetVehiclePedIsIn(playerPed, false);      // Retrieve if the nitrous of the vehicle is active.     if (IsNitrousActive(vehicle)) {         console.log(GetRemainingNitrousDuration(vehicle));     } }); ```

**Descripción oficial:**

```
NativeDB Introduced: 3095
```

Retrieves the remaining duration of nitrous boost available for the specified vehicle.

---
### GetRotationOfVehicleRecordingAtTime

`GET_ROTATION_OF_VEHICLE_RECORDING_AT_TIME` · hash `0x2058206FBE79A8AD` · jhash `0xD96DEC68` · **Cliente**

```lua
local retval = GetRotationOfVehicleRecordingAtTime(recording, time, script)
```
```c
Vector3 GET_ROTATION_OF_VEHICLE_RECORDING_AT_TIME(int recording, float time, char* script);
```

**Parámetros**

- `recording` (`int`)
- `time` (`float`)
- `script` (`char*`)

**Devuelve:** `Vector3`

---
### GetRotationOfVehicleRecordingIdAtTime

`GET_ROTATION_OF_VEHICLE_RECORDING_ID_AT_TIME` · hash `0xF0F2103EFAF8CBA7` · jhash `0x4D1C15C2` · **Cliente**

```lua
local retval = GetRotationOfVehicleRecordingIdAtTime(id, time)
```
```c
Vector3 GET_ROTATION_OF_VEHICLE_RECORDING_ID_AT_TIME(int id, float time);
```

**Parámetros**

- `id` (`int`)
- `time` (`float`)

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `0xF0F2103EFAF8CBA7` (`N_0xf0f2103efaf8cba7`)

---
### GetSubmarineIsUnderDesignDepth

`GET_SUBMARINE_IS_UNDER_DESIGN_DEPTH` · hash `0x3E71D0B300B7AA79` · **Cliente**

```lua
local retval = GetSubmarineIsUnderDesignDepth(submarine)
```
```c
BOOL GET_SUBMARINE_IS_UNDER_DESIGN_DEPTH(Vehicle submarine);
```

**Parámetros**

- `submarine` (`Vehicle`): The submarine vehicle to be evaluated for being under its crush depth threshold.

**Devuelve:** `BOOL` — Returns `true` if the submarine is below its designated crush depth, `false` otherwise.

**Descripción oficial:**

Determines if the submarine is operating below its designated crush depth.

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `_GET_SUBMARINE_IS_BELOW_FIRST_CRUSH_DEPTH` (`GetSubmarineIsBelowFirstCrushDepth`)

---
### GetSubmarineNumberOfAirLeaks

`GET_SUBMARINE_NUMBER_OF_AIR_LEAKS` · hash `0x093D6DDCA5B8FBAE` · **Cliente**

```lua
local retval = GetSubmarineNumberOfAirLeaks(submarine)
```
```c
int GET_SUBMARINE_NUMBER_OF_AIR_LEAKS(Vehicle submarine);
```

**Parámetros**

- `submarine` (`Vehicle`): The submarine vehicle to check for air leaks.

**Devuelve:** `int` — Returns the number of air leaks on the submarine.

**Descripción oficial:**

Checks if a Submarine has any air leaks, when there is more than 4 the player will drown.

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `_GET_SUBMARINE_CRUSH_DEPTH_WARNING_STATE` (`GetSubmarineCrushDepthWarningState`)

---
### GetTimePositionInRecording

`GET_TIME_POSITION_IN_RECORDING` · hash `0x5746F3A7AB7FE544` · jhash `0xF8C3E4A2` · **Cliente**

```lua
local retval = GetTimePositionInRecording(vehicle)
```
```c
float GET_TIME_POSITION_IN_RECORDING(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Can be used with GET_TOTAL_DURATION_OF_VEHICLE_RECORDING{_ID} to compute a percentage.
```

---
### GetTotalDurationOfVehicleRecording

`GET_TOTAL_DURATION_OF_VEHICLE_RECORDING` · hash `0x0E48D1C262390950` · jhash `0x5B35EEB7` · **Cliente**

```lua
local retval = GetTotalDurationOfVehicleRecording(recording, script)
```
```c
float GET_TOTAL_DURATION_OF_VEHICLE_RECORDING(int recording, char* script);
```

**Parámetros**

- `recording` (`int`)
- `script` (`char*`)

**Devuelve:** `float`

---
### GetTotalDurationOfVehicleRecordingId

`GET_TOTAL_DURATION_OF_VEHICLE_RECORDING_ID` · hash `0x102D125411A7B6E6` · jhash `0x7116785E` · **Cliente**

```lua
local retval = GetTotalDurationOfVehicleRecordingId(id)
```
```c
float GET_TOTAL_DURATION_OF_VEHICLE_RECORDING_ID(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `float`

---
### GetTrainCarriage

`GET_TRAIN_CARRIAGE` · hash `0x08AAFD0814722BC3` · jhash `0x2544E7A6` · **Cliente**

```lua
local retval = GetTrainCarriage(train, trailerNumber)
```
```c
Entity GET_TRAIN_CARRIAGE(Vehicle train, int trailerNumber);
```

**Parámetros**

- `train` (`Vehicle`)
- `trailerNumber` (`int`)

**Devuelve:** `Entity`

**Descripción oficial:**

```
Corrected p1. it's basically the 'carriage/trailer number'. So if the train has 3 trailers you'd call the native once with a var or 3 times with 1, 2, 3.  
```

---
### GetTyreHealth

`_GET_TYRE_HEALTH` · hash `0x55EAB010FAEE9380` · **Cliente**

```lua
local retval = GetTyreHealth(vehicle, wheelIndex)
```
```c
float _GET_TYRE_HEALTH(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### GetTyreWearMultiplier

`_GET_TYRE_WEAR_MULTIPLIER` · hash `0x6E387895952F4F71` · **Cliente**

```lua
local retval = GetTyreWearMultiplier(vehicle, wheelIndex)
```
```c
float _GET_TYRE_WEAR_MULTIPLIER(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### GetVehicleAcceleration

`GET_VEHICLE_ACCELERATION` · hash `0x5DD35C8D074E57AE` · jhash `0x00478321` · **Cliente**

```lua
local retval = GetVehicleAcceleration(vehicle)
```
```c
float GET_VEHICLE_ACCELERATION(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle for which to obtain the acceleration.

**Devuelve:** `float` — Returns the acceleration value of the specified vehicle as a float number.

**Descripción oficial:**

Retrieves a static value representing the maximum drive force of specific a vehicle, including any vehicle mods. This value does not change dynamically during gameplay. This value provides an approximation and should be considered alongside other performance metrics like top speed for a more comprehensive understanding of the vehicle's capabilities.

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
-- This example prints the acceleration of the player's current vehicle.

-- Retrieve the player ped.
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in.
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- If the vehicle does not exist, end the execution of the code here.
if not DoesEntityExist(vehicle) then 
    return 
end

-- Retrieve the acceleration of the vehicle.
local acceleration = GetVehicleAcceleration(vehicle)

-- Print the acceleration of the vehicle.
print("Vehicle Acceleration: " .. acceleration)
```

**Ejemplo (js):**

```js
// This example prints the acceleration of the player's current vehicle.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// If the vehicle does not exist, end the execution of the code here.
if (!DoesEntityExist(vehicle)) {
  return;
}

// Retrieve the acceleration of the vehicle.
const acceleration = GetVehicleAcceleration(vehicle);

// Print the acceleration of the vehicle.
console.log(`Vehicle Acceleration: ${acceleration}`);
```

**Ejemplo (cs):**

```cs
// This example prints the acceleration of the player's current vehicle.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// If the vehicle does not exist, end the execution of the code here.
if (!DoesEntityExist(vehicle)) {
  return;
}

// Retrieve the acceleration of the vehicle.
float acceleration = GetVehicleAcceleration(vehicle);

// Print the acceleration of the vehicle.
Debug.WriteLine($"Vehicle Acceleration: {acceleration}");
```

---
### GetVehicleAttachedToCargobob

`GET_VEHICLE_ATTACHED_TO_CARGOBOB` · hash `0x873B82D42AC2B9E5` · jhash `0x301A1D24` · **Cliente**

```lua
local retval = GetVehicleAttachedToCargobob(cargobob)
```
```c
Vehicle GET_VEHICLE_ATTACHED_TO_CARGOBOB(Vehicle cargobob);
```

**Parámetros**

- `cargobob` (`Vehicle`)

**Devuelve:** `Vehicle`

**Descripción oficial:**

```
Returns attached vehicle (Vehicle in parameter must be cargobob)  
```

---
### GetVehicleBodyHealth

`GET_VEHICLE_BODY_HEALTH` · hash `0xF271147EB7B40F12` · jhash `0x2B2FCC28` · **Cliente**

```lua
local retval = GetVehicleBodyHealth(vehicle)
```
```c
float GET_VEHICLE_BODY_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Seems related to vehicle health, like the one in IV.  
Max 1000, min 0.  
Vehicle does not necessarily explode or become undrivable at 0.  
```

---
### GetVehicleBombCount

`_GET_VEHICLE_BOMB_COUNT` · hash `0xEA12BD130D7569A1` · **Cliente**

```lua
local retval = GetVehicleBombCount(aircraft)
```
```c
int _GET_VEHICLE_BOMB_COUNT(Vehicle aircraft);
```

**Parámetros**

- `aircraft` (`Vehicle`): The vehicle to get the amount of bombs from.

**Devuelve:** `int` — An int indicating the amount of bombs remaining on that plane.

**Descripción oficial:**

Gets the amount of bombs that this vehicle has. As far as I know, this does *not* impact vehicle weapons or the ammo of those weapons in any way, it is just a way to keep track of the amount of bombs in a specific plane.

In decompiled scripts this is used to check if the vehicle has enough bombs before a bomb can be dropped (bombs are dropped by using [`_SHOOT_SINGLE_BULLET_BETWEEN_COORDS_WITH_EXTRA_PARAMS`](MISC.md#shootsinglebulletbetweencoordsignoreentitynew)).

Use [`_SET_AIRCRAFT_BOMB_COUNT`](VEHICLE-2.md#setvehiclebombcount) to set the amount of bombs on that vehicle.

**Nombres antiguos (alias):** `0xEA12BD130D7569A1` (`N_0xea12bd130d7569a1`), `_GET_AIRCRAFT_BOMB_COUNT` (`GetAircraftBombCount`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
print("This plane has " .. GetAircraftBombCount(vehicle) .. " bombs left.")
```

**Ejemplo (cs):**

```cs
int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
Debug.WriteLine("This plane has " + GetAircraftBombCount(vehicle) + " bombs left.");
```

---
### GetVehicleCanActivateParachute

`_GET_VEHICLE_CAN_ACTIVATE_PARACHUTE` · hash `0xA916396DF4154EE3` · **Cliente**

```lua
local retval = GetVehicleCanActivateParachute(vehicle)
```
```c
BOOL _GET_VEHICLE_CAN_ACTIVATE_PARACHUTE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_CAN_VEHICLE_PARACHUTE_BE_ACTIVATED` (`CanVehicleParachuteBeActivated`)

---
### GetVehicleCauseOfDestruction

`GET_VEHICLE_CAUSE_OF_DESTRUCTION` · hash `0xE495D1EF4C91FD20` · jhash `0x7F8C20DD` · **Cliente**

```lua
local retval = GetVehicleCauseOfDestruction(vehicle)
```
```c
Hash GET_VEHICLE_CAUSE_OF_DESTRUCTION(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to get the cause of destruction of.

**Devuelve:** `Hash` — A hash representing the destruction cause. These can be weapon hashes.

**Ejemplo (lua):**

```lua
local destructionCauseHash = GetVehicleCauseOfDestruction(GetVehiclePedIsIn(PlayerPedId(), true))
if destructionCauseHash == GetHashKey("weapon_stickybomb") then
     -- It looks like the vehicle was destroyed by a sticky bomb
     Citizen.Trace('Vehicle was destroyed by a sticky bomb!')
elseif destructionCauseHash ~= 0 then
     -- It looks like the vehicle was destroyed by something else!
     Citizen.Trace('Vehicle was destroyed by: ' .. destructionCauseHash)
end
```

---
### GetVehicleClass

`GET_VEHICLE_CLASS` · hash `0x29439776AAA00A62` · jhash `0xC025338E` · **Cliente**

```lua
local retval = GetVehicleClass(vehicle)
```
```c
int GET_VEHICLE_CLASS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns an int  
Vehicle Classes:  
0: Compacts  
1: Sedans  
2: SUVs  
3: Coupes  
4: Muscle  
5: Sports Classics  
6: Sports  
7: Super  
8: Motorcycles  
9: Off-road  
10: Industrial  
11: Utility  
12: Vans  
13: Cycles  
14: Boats  
15: Helicopters  
16: Planes  
17: Service  
18: Emergency  
19: Military  
20: Commercial  
21: Trains  
22: Open Wheel
char buffer[128];  
std::sprintf(buffer, "VEH_CLASS_%i", VEHICLE::GET_VEHICLE_CLASS(vehicle));  
char* className = UI::_GET_LABEL_TEXT(buffer);  
```

---
### GetVehicleClassEstimatedMaxSpeed

`GET_VEHICLE_CLASS_ESTIMATED_MAX_SPEED` · hash `0x00C09F246ABEDD82` · jhash `0xCE67162C` · **Cliente**

```lua
local retval = GetVehicleClassEstimatedMaxSpeed(vehicleClass)
```
```c
float GET_VEHICLE_CLASS_ESTIMATED_MAX_SPEED(int vehicleClass);
```

**Parámetros**

- `vehicleClass` (`int`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x00C09F246ABEDD82` (`N_0x00c09f246abedd82`), `_GET_VEHICLE_CLASS_MAX_SPEED` (`GetVehicleClassMaxSpeed`)

---
### GetVehicleClassFromName

`GET_VEHICLE_CLASS_FROM_NAME` · hash `0xDEDF1C8BD47C2200` · jhash `0xEA469980` · **Cliente**

```lua
local retval = GetVehicleClassFromName(modelHash)
```
```c
int GET_VEHICLE_CLASS_FROM_NAME(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
For a full enum, see here : pastebin.com/i2GGAjY0
char buffer[128];
std::sprintf(buffer, "VEH_CLASS_%i", VEHICLE::GET_VEHICLE_CLASS_FROM_NAME (hash));
const char* className = HUD::_GET_LABEL_TEXT(buffer);
```

---
### GetVehicleClassMaxAcceleration

`GET_VEHICLE_CLASS_MAX_ACCELERATION` · hash `0x2F83E7E45D9EA7AE` · jhash `0x3E220A9B` · **Cliente**

```lua
local retval = GetVehicleClassMaxAcceleration(vehicleClass)
```
```c
float GET_VEHICLE_CLASS_MAX_ACCELERATION(int vehicleClass);
```

**Parámetros**

- `vehicleClass` (`int`)

**Devuelve:** `float`

---
### GetVehicleClassMaxAgility

`GET_VEHICLE_CLASS_MAX_AGILITY` · hash `0x4F930AD022D6DE3B` · jhash `0x45F2BD83` · **Cliente**

```lua
local retval = GetVehicleClassMaxAgility(vehicleClass)
```
```c
float GET_VEHICLE_CLASS_MAX_AGILITY(int vehicleClass);
```

**Parámetros**

- `vehicleClass` (`int`)

**Devuelve:** `float`

---
### GetVehicleClassMaxBraking

`GET_VEHICLE_CLASS_MAX_BRAKING` · hash `0x4BF54C16EC8FEC03` · jhash `0xD08CC1A5` · **Cliente**

```lua
local retval = GetVehicleClassMaxBraking(vehicleClass)
```
```c
float GET_VEHICLE_CLASS_MAX_BRAKING(int vehicleClass);
```

**Parámetros**

- `vehicleClass` (`int`)

**Devuelve:** `float`

---
### GetVehicleClassMaxTraction

`GET_VEHICLE_CLASS_MAX_TRACTION` · hash `0xDBC86D85C5059461` · jhash `0x5B4FDC16` · **Cliente**

```lua
local retval = GetVehicleClassMaxTraction(vehicleClass)
```
```c
float GET_VEHICLE_CLASS_MAX_TRACTION(int vehicleClass);
```

**Parámetros**

- `vehicleClass` (`int`)

**Devuelve:** `float`

---
### GetVehicleColor

`GET_VEHICLE_COLOR` · hash `0xF3CC740D36221548` · jhash `0x03BC8F1B` · **Cliente**

```lua
local r, g, b = GetVehicleColor(vehicle)
```
```c
void GET_VEHICLE_COLOR(Vehicle vehicle, int* r, int* g, int* b);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

See [`SET_VEHICLE_CUSTOM_PRIMARY_COLOUR`](../cfx/servidor.md#setvehiclecustomprimarycolour) and [`SET_VEHICLE_CUSTOM_SECONDARY_COLOUR`](../cfx/servidor.md#setvehiclecustomsecondarycolour).

---
### GetVehicleColourCombination

`GET_VEHICLE_COLOUR_COMBINATION` · hash `0x6A842D197F845D56` · jhash `0x77AC1B4C` · **Cliente**

```lua
local retval = GetVehicleColourCombination(vehicle)
```
```c
int GET_VEHICLE_COLOUR_COMBINATION(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleColours

`GET_VEHICLE_COLOURS` · hash `0xA19435F193E081AC` · jhash `0x40D82D88` · **Cliente**

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
### GetVehicleColoursWhichCanBeSet

`GET_VEHICLE_COLOURS_WHICH_CAN_BE_SET` · hash `0xEEBFC7A7EFDC35B4` · jhash `0x749DEEA2` · **Cliente**

```lua
local retval = GetVehicleColoursWhichCanBeSet(vehicle)
```
```c
int GET_VEHICLE_COLOURS_WHICH_CAN_BE_SET(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle

**Devuelve:** `int` — Returns a bitfield of the colours supported by the vehicle's shader.

**Descripción oficial:**

```cpp
enum eColourBitField {
    HAS_BODY_COLOUR1 = 1,
    HAS_BODY_COLOUR2 = 2,
    HAS_BODY_COLOUR3 = 4,
    HAS_BODY_COLOUR4 = 8,
    HAS_BODY_COLOUR5 = 16
}
```

**Nombres antiguos (alias):** `0xEEBFC7A7EFDC35B4` (`N_0xeebfc7a7efdc35b4`)

---
### GetVehicleCountermeasureCount

`_GET_VEHICLE_COUNTERMEASURE_COUNT` · hash `0xF846AA63DF56B804` · **Cliente**

```lua
local retval = GetVehicleCountermeasureCount(aircraft)
```
```c
int _GET_VEHICLE_COUNTERMEASURE_COUNT(Vehicle aircraft);
```

**Parámetros**

- `aircraft` (`Vehicle`): The vehicle to get the amount of countermeasures from.

**Devuelve:** `int` — An int indicating the amount of countermeasures remaining on that plane.

**Descripción oficial:**

Similar to [`_GET_AIRCRAFT_BOMB_COUNT`](#getvehiclebombcount), this gets the amount of countermeasures that are present on this vehicle.

Use [`_SET_AIRCRAFT_COUNTERMEASURE_COUNT`](VEHICLE-2.md#setvehiclecountermeasurecount) to set the current amount.

**Nombres antiguos (alias):** `0xF846AA63DF56B804` (`N_0xf846aa63df56b804`), `_GET_AIRCRAFT_COUNTERMEASURE_COUNT` (`GetAircraftCountermeasureCount`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
print("This plane has " .. GetAircraftCountermeasureCount(vehicle) .. " countermeasures left.")
```

**Ejemplo (cs):**

```cs
int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
Debug.WriteLine("This plane has " + GetAircraftCountermeasureCount(vehicle) + " countermeasures left.");
```

---
### GetVehicleCurrentSlipstreamDraft

`_GET_VEHICLE_CURRENT_SLIPSTREAM_DRAFT` · hash `0x36492C2F0D134C56` · jhash `0xA4A75FCF` · **Cliente**

```lua
local retval = GetVehicleCurrentSlipstreamDraft(vehicle)
```
```c
float _GET_VEHICLE_CURRENT_SLIPSTREAM_DRAFT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns a float value between 0.0 and 3.0 related to its slipstream draft (boost/speedup).
GET_VEHICLE_*
```

**Nombres antiguos (alias):** `0x36492C2F0D134C56` (`N_0x36492c2f0d134c56`)

---
### GetVehicleCustomPrimaryColour

`GET_VEHICLE_CUSTOM_PRIMARY_COLOUR` · hash `0xB64CF2CCA9D95F52` · jhash `0x1C2B9FEF` · **Cliente**

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

`GET_VEHICLE_CUSTOM_SECONDARY_COLOUR` · hash `0x8389CD56CA8072DC` · jhash `0x3FF247A2` · **Cliente**

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
### GetVehicleDashboardColor

`_GET_VEHICLE_DASHBOARD_COLOR` · hash `0xB7635E80A5C31BFF` · **Cliente**

```lua
local color = GetVehicleDashboardColor(vehicle, color)
```
```c
void _GET_VEHICLE_DASHBOARD_COLOR(Vehicle vehicle, int* color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `color` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `_GET_VEHICLE_DASHBOARD_COLOUR` (`GetVehicleDashboardColour`)

---
### GetVehicleDeformationAtPos

`GET_VEHICLE_DEFORMATION_AT_POS` · hash `0x4EC6CFBC7B2E9536` · jhash `0xABF02075` · **Cliente**

```lua
local retval = GetVehicleDeformationAtPos(vehicle, offsetX, offsetY, offsetZ)
```
```c
Vector3 GET_VEHICLE_DEFORMATION_AT_POS(Vehicle vehicle, float offsetX, float offsetY, float offsetZ);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
The only example I can find of this function in the scripts, is this:  
struct _s = VEHICLE::GET_VEHICLE_DEFORMATION_AT_POS(rPtr((A_0) + 4), 1.21f, 6.15f, 0.3f);  
-----------------------------------------------------------------------------------------------------------------------------------------  
PC scripts:  
v_5/*{3}*/ = VEHICLE::GET_VEHICLE_DEFORMATION_AT_POS(a_0._f1, 1.21, 6.15, 0.3);  
```

---
### GetVehicleDirtLevel

`GET_VEHICLE_DIRT_LEVEL` · hash `0x8F17BC8BA08DA62B` · jhash `0xFD15C065` · **Cliente**

```lua
local retval = GetVehicleDirtLevel(vehicle)
```
```c
float GET_VEHICLE_DIRT_LEVEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `float` — A number between 0.0 and 15.0 representing the vehicles dirt level.

**Descripción oficial:**

A getter for [`SET_VEHICLE_DIRT_LEVEL`](../cfx/servidor.md#setvehicledirtlevel).

**Ejemplo (lua):**

```lua
local Vehicle = GetVehiclePedIsUsing(PlayerPedId())
if GetVehicleDirtLevel(Vehicle) > 0.0 then -- if the cars dirt level is more than 0.0 then clean it.
  SetVehicleDirtLevel(Vehicle, 0.0) -- set the vehicle dirt level to 0.0
end
```

---
### GetVehicleDoorAngleRatio

`GET_VEHICLE_DOOR_ANGLE_RATIO` · hash `0xFE3F9C29F7B32BD5` · jhash `0x0E399C26` · **Cliente**

```lua
local retval = GetVehicleDoorAngleRatio(vehicle, doorIndex)
```
```c
float GET_VEHICLE_DOOR_ANGLE_RATIO(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle
- `doorIndex` (`int`): Index of door to check

**Devuelve:** `float` — A float representing angle of door mapped from 0.0 to 1.0

**Descripción oficial:**

Checks the angle of the door mapped from 0.0 - 1.0 where 0.0 is fully closed and 1.0 is fully open.

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](VEHICLE-2.md#setvehicledoorshut)

**Ejemplo (lua):**

```lua
local veh = GetVehiclePedIsIn(PlayerPedId()
-- check if driver door is open
if GetVehicleDoorAngleRatio(veh, 0) > 0.0 then
  print("Driver door is open!)
end
```

---
### GetVehicleDoorLockStatus

`GET_VEHICLE_DOOR_LOCK_STATUS` · hash `0x25BC98A59C2EA962` · jhash `0x0D72CEF2` · **Cliente**

```lua
local retval = GetVehicleDoorLockStatus(vehicle)
```
```c
int GET_VEHICLE_DOOR_LOCK_STATUS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int` — Returns the current lock status, refer to [SET_VEHICLE_DOORS_LOCKED](../cfx/servidor.md#setvehicledoorslocked)

---
### GetVehicleDoorsLockedForPlayer

`GET_VEHICLE_DOORS_LOCKED_FOR_PLAYER` · hash `0xF6AF6CB341349015` · jhash `0x1DC50247` · **Cliente**

```lua
local retval = GetVehicleDoorsLockedForPlayer(vehicle, player)
```
```c
BOOL GET_VEHICLE_DOORS_LOCKED_FOR_PLAYER(Vehicle vehicle, Player player);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `player` (`Player`)

**Devuelve:** `BOOL`

---
### GetVehicleDrivetrainType

`_GET_VEHICLE_DRIVETRAIN_TYPE` · hash `0x1423725069EE1D14` · **Cliente**

```lua
local retval = GetVehicleDrivetrainType(vehicleModel)
```
```c
int _GET_VEHICLE_DRIVETRAIN_TYPE(Hash vehicleModel);
```

**Parámetros**

- `vehicleModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of the vehicle model to check.

**Devuelve:** `int` — Returns the vehicle's drivetrain type.

**Descripción oficial:**

```
NativeDB Introduced: v3258
```

**Note**: When using this native, the hash of the vehicle needs to be loaded into the client's memory. This can be done by requesting the model with [`REQUEST_MODEL`](STREAMING.md#requestmodel) or by simply having the vehicle spawned.

```cpp

enum eVehicleDrivetrainType
{
    INVALID = 0,
    FWD = 1,
    RWD = 2,
    AWD = 3
};
```

```
NativeDB Introduced: v3258
```

**Ejemplo (lua):**

```lua
local vehicleHash = GetHashKey("elegy")
RequestModel(vehicleHash)
repeat
    Wait(0)
until HasModelLoaded(vehicleHash)

local driveTrainType = GetVehicleDriveTrainType(vehicleHash)

if driveTrainType == 1 then
    -- FWD
    print(GetLabelText("FMMC_DT_FWD"))
elseif driveTrainType == 2 then
    -- RWD
    print(GetLabelText("FMMC_DT_RWD"))
elseif driveTrainType == 3 then
    -- AWD
    print(GetLabelText("FMMC_DT_AWD"))
else
    print("invalid")
end
```

---
### GetVehicleEngineHealth

`GET_VEHICLE_ENGINE_HEALTH` · hash `0xC45D23BAF168AAB8` · jhash `0x8880038A` · **Cliente**

```lua
local retval = GetVehicleEngineHealth(vehicle)
```
```c
float GET_VEHICLE_ENGINE_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns 1000.0 if the function is unable to get the address of the specified vehicle or if it's not a vehicle.  
Minimum: -4000  
Maximum: 1000  
-4000: Engine is destroyed  
0 and below: Engine catches fire and health rapidly declines  
300: Engine is smoking and losing functionality  
1000: Engine is perfect  
```

---
### GetVehicleEnveffScale

`GET_VEHICLE_ENVEFF_SCALE` · hash `0xA82819CAC9C4C403` · jhash `0xD5F1EEE1` · **Cliente**

```lua
local retval = GetVehicleEnveffScale(vehicle)
```
```c
float GET_VEHICLE_ENVEFF_SCALE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
formerly known as _GET_VEHICLE_PAINT_FADE
The result is a value from 0-1, where 0 is fresh paint.
```

**Nombres antiguos (alias):** `_GET_VEHICLE_PAINT_FADE` (`GetVehiclePaintFade`)

---
### GetVehicleEstimatedMaxSpeed

`GET_VEHICLE_ESTIMATED_MAX_SPEED` · hash `0x53AF99BAA671CA47` · jhash `0x7D1A0616` · **Cliente**

```lua
local retval = GetVehicleEstimatedMaxSpeed(vehicle)
```
```c
float GET_VEHICLE_ESTIMATED_MAX_SPEED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle for which to obtain the estimated max speed.

**Devuelve:** `float` — Returns the estimated maximum speed of the specified vehicle as a float number.

**Descripción oficial:**

Retrieves a static value representing the estimated max speed of a specific vehicle, including any vehicle mods. This value does not change dynamically during gameplay.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x53AF99BAA671CA47` (`N_0x53af99baa671ca47`), `_GET_VEHICLE_MAX_SPEED` (`GetVehicleMaxSpeed`)

**Ejemplo (lua):**

```lua
-- This example prints the estimated max speed of the player's current vehicle.

-- Retrieve the player ped.
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in.
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- If the vehicle does not exist, end the execution of the code here.
if not DoesEntityExist(vehicle) then 
    return 
end

-- Retrieve the estimated max speed of the vehicle.
local estimatedMaxSpeed = GetVehicleEstimatedMaxSpeed(vehicle)

-- Print the estimated max speed of the vehicle.
print("Estimated Max Speed: " .. estimatedMaxSpeed)
```

**Ejemplo (js):**

```js
// This example prints the estimated max speed of the player's current vehicle.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// If the vehicle does not exist, end the execution of the code here.
if (!DoesEntityExist(vehicle)) {
  return;
}

// Retrieve the estimated max speed of the vehicle.
const estimatedMaxSpeed = GetVehicleEstimatedMaxSpeed(vehicle);

// Print the estimated max speed of the vehicle.
console.log(`Estimated Max Speed: ${estimatedMaxSpeed}`);
```

**Ejemplo (cs):**

```cs
// This example prints the estimated max speed of the player's current vehicle.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// If the vehicle does not exist, end the execution of the code here.
if (!DoesEntityExist(vehicle)) {
  return;
}

// Retrieve the estimated max speed of the vehicle.
float estimatedMaxSpeed = GetVehicleEstimatedMaxSpeed(vehicle);

// Print the estimated max speed of the vehicle.
Debug.WriteLine($"Estimated Max Speed: {estimatedMaxSpeed}");
```

---
### GetVehicleExtraColours

`GET_VEHICLE_EXTRA_COLOURS` · hash `0x3BC4245933A166F7` · jhash `0x80E4659B` · **Cliente**

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

`GET_VEHICLE_FLIGHT_NOZZLE_POSITION` · hash `0xDA62027C8BDB326E` · jhash `0xAD40AD55` · **Cliente**

```lua
local retval = GetVehicleFlightNozzlePosition(aircraft)
```
```c
float GET_VEHICLE_FLIGHT_NOZZLE_POSITION(Vehicle aircraft);
```

**Parámetros**

- `aircraft` (`Vehicle`): The vehicle to check the hover mode on.

**Devuelve:** `float` — A float indicating the percentage of the hover mode. 1.0 = in VTOL mode, 0.0 = in normal flying mode.

**Nombres antiguos (alias):** `0xDA62027C8BDB326E` (`N_0xda62027c8bdb326e`), `_GET_PLANE_HOVER_MODE_PERCENTAGE` (`GetPlaneHoverModePercentage`), `_GET_VEHICLE_HOVER_MODE_PERCENTAGE` (`GetVehicleHoverModePercentage`), `_GET_PLANE_VTOL_DIRECTION` (`GetPlaneVtolDirection`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

if GetVehicleFlightNozzlePosition(vehicle) == 0.0 then
    print("Flying normally!")
elseif GetVehicleFlightNozzlePosition(vehicle) == 1.0 then
    print("Flying in VTOL mode!")
else
    print("Currently switching hover mode!")
end
```

**Ejemplo (js):**

```js
let vehicle = GetVehiclePedIsIn(PlayerPedId(), false);

if (GetVehicleFlightNozzlePosition(vehicle) === 0.0) {
    console.log("Flying normally!");
}
else if (GetVehicleFlightNozzlePosition(vehicle) === 1.0) {
    console.log("Flying in VTOL mode!");
}
else {
    console.log("Currently switching hover mode!");
}
```

**Ejemplo (cs):**

```cs
int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);

if (GetVehicleFlightNozzlePosition(vehicle) == 0f)
{
    Debug.WriteLine("Flying normally!");
}
else if (GetVehicleFlightNozzlePosition(vehicle) == 1f)
{
    Debug.WriteLine("Flying in VTOL mode!");
}
else
{
    Debug.WriteLine("Currently switching hover mode!");
}
```

---
### GetVehicleHasKers

`GET_VEHICLE_HAS_KERS` · hash `0x50634E348C8D44EF` · jhash `0x0761E635` · **Cliente**

```lua
local retval = GetVehicleHasKers(vehicle)
```
```c
BOOL GET_VEHICLE_HAS_KERS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.

**Devuelve:** `BOOL` — Returns true if the vehicle has a kers boost (for instance the lectro or the vindicator)

**Nombres antiguos (alias):** `0x50634E348C8D44EF` (`N_0x50634e348c8d44ef`), `_HAS_VEHICLE_KERS_BOOST` (`HasVehicleKersBoost`)

---
### GetVehicleHasParachute

`_GET_VEHICLE_HAS_PARACHUTE` · hash `0xBC9CFF381338CB4F` · **Cliente**

```lua
local retval = GetVehicleHasParachute(vehicle)
```
```c
BOOL _GET_VEHICLE_HAS_PARACHUTE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_HAS_VEHICLE_PARACHUTE` (`HasVehicleParachute`), `_DOES_VEHICLE_HAVE_PARACHUTE` (`DoesVehicleHaveParachute`)

---
### GetVehicleHealthPercentage

`GET_VEHICLE_HEALTH_PERCENTAGE` · hash `0xB8EF61207C2393A9` · jhash `0x196BA503` · **Cliente**

```lua
local retval = GetVehicleHealthPercentage(vehicle)
```
```c
float GET_VEHICLE_HEALTH_PERCENTAGE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Added Parameter 2: float maxEngineHealth
NativeDB Added Parameter 3: float maxPetrolTankHealth
NativeDB Added Parameter 4: float maxBodyHealth
NativeDB Added Parameter 5: float maxMainRotorHealth
NativeDB Added Parameter 6: float maxTailRotorHealth
NativeDB Added Parameter 7: float maxUnkHealth
```

**Nombres antiguos (alias):** `_GET_VEHICLE_BODY_HEALTH_2` (`GetVehicleBodyHealth_2`)

---
### GetVehicleHomingLockonState

`GET_VEHICLE_HOMING_LOCKON_STATE` · hash `0xE6B0E8CFC3633BF0` · jhash `0xFBDE9FD8` · **Cliente**

```lua
local retval = GetVehicleHomingLockonState(vehicle)
```
```c
int GET_VEHICLE_HOMING_LOCKON_STATE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns a value depending on the lock-on state of vehicle weapons.
0: not locked on
1: locking on
2: locked on
```

**Nombres antiguos (alias):** `0xE6B0E8CFC3633BF0` (`N_0xe6b0e8cfc3633bf0`)

---
### GetVehicleIndividualDoorLockStatus

`GET_VEHICLE_INDIVIDUAL_DOOR_LOCK_STATUS` · hash `0xCA4AC3EAAE46EC7B` · **Cliente**

```lua
local retval = GetVehicleIndividualDoorLockStatus(vehicle, doorIndex)
```
```c
int GET_VEHICLE_INDIVIDUAL_DOOR_LOCK_STATUS(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)

**Devuelve:** `int` — Returns vehicle door lock state previously set with [`SET_VEHICLE_INDIVIDUAL_DOORS_LOCKED`](VEHICLE-2.md#setvehicleindividualdoorslocked)

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](VEHICLE-2.md#setvehicledoorshut)

**Nombres antiguos (alias):** `0xCA4AC3EAAE46EC7B` (`N_0xca4ac3eaae46ec7b`), `_GET_VEHICLE_DOOR_DESTROY_TYPE` (`GetVehicleDoorDestroyType`)

---
### GetVehicleInteriorColor

`_GET_VEHICLE_INTERIOR_COLOR` · hash `0x7D1464D472D32136` · **Cliente**

```lua
local color = GetVehicleInteriorColor(vehicle, color)
```
```c
void _GET_VEHICLE_INTERIOR_COLOR(Vehicle vehicle, int* color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `color` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `_GET_VEHICLE_INTERIOR_COLOUR` (`GetVehicleInteriorColour`)

---
### GetVehicleIsMercenary

`GET_VEHICLE_IS_MERCENARY` · hash `0xD4C4642CB7F50B5D` · jhash `0x575504DE` · **Cliente**

```lua
local retval = GetVehicleIsMercenary(vehicle)
```
```c
BOOL GET_VEHICLE_IS_MERCENARY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check for mercenary status.

**Devuelve:** `BOOL` — Returns `true` if the vehicle is a mercenary vehicle, `false` otherwise.

**Descripción oficial:**

Returns whether the specified vehicle is designated as a mercenary vehicle

**Nombres antiguos (alias):** `0xD4C4642CB7F50B5D` (`N_0xd4c4642cb7f50b5d`)

---
### GetVehicleLayoutHash

`GET_VEHICLE_LAYOUT_HASH` · hash `0x28D37D4F71AC5C58` · jhash `0xE0B35187` · **Cliente**

```lua
local retval = GetVehicleLayoutHash(vehicle)
```
```c
Hash GET_VEHICLE_LAYOUT_HASH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `Hash`

---
### GetVehicleLightsState

`GET_VEHICLE_LIGHTS_STATE` · hash `0xB91B4C20085BD12F` · jhash `0x7C278621` · **Cliente**

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

`GET_VEHICLE_LIVERY` · hash `0x2BB9230590DA5E8A` · jhash `0xEC82A51D` · **Cliente**

```lua
local retval = GetVehicleLivery(vehicle)
```
```c
int GET_VEHICLE_LIVERY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
-1 = no livery  
```

---
### GetVehicleLiveryCount

`GET_VEHICLE_LIVERY_COUNT` · hash `0x87B63E25A529D526` · jhash `0xFB0CA947` · **Cliente**

```lua
local retval = GetVehicleLiveryCount(vehicle)
```
```c
int GET_VEHICLE_LIVERY_COUNT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns -1 if the vehicle has no livery  
```

---
### GetVehicleLockOnTarget

`GET_VEHICLE_LOCK_ON_TARGET` · hash `0x8F5EBAB1F260CFCE` · jhash `0x4A557117` · **Cliente**

```lua
local retval, entity = GetVehicleLockOnTarget(vehicle, entity)
```
```c
BOOL GET_VEHICLE_LOCK_ON_TARGET(Vehicle vehicle, Entity* entity);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `entity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_GET_VEHICLE_OWNER` (`GetVehicleOwner`)

---
### GetVehicleMaxBraking

`GET_VEHICLE_MAX_BRAKING` · hash `0xAD7E85FC227197C4` · jhash `0x03B926F6` · **Cliente**

```lua
local retval = GetVehicleMaxBraking(vehicle)
```
```c
float GET_VEHICLE_MAX_BRAKING(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleMaxNumberOfPassengers

`GET_VEHICLE_MAX_NUMBER_OF_PASSENGERS` · hash `0xA7C4F2C6E744A550` · jhash `0x0A2FC08C` · **Cliente**

```lua
local retval = GetVehicleMaxNumberOfPassengers(vehicle)
```
```c
int GET_VEHICLE_MAX_NUMBER_OF_PASSENGERS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleMaxTraction

`GET_VEHICLE_MAX_TRACTION` · hash `0xA132FB5370554DB0` · jhash `0x7E5A1587` · **Cliente**

```lua
local retval = GetVehicleMaxTraction(vehicle)
```
```c
float GET_VEHICLE_MAX_TRACTION(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleMod

`GET_VEHICLE_MOD` · hash `0x772960298DA26FDB` · jhash `0xDC520069` · **Cliente**

```lua
local retval = GetVehicleMod(vehicle, modType)
```
```c
int GET_VEHICLE_MOD(Vehicle vehicle, int modType);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to get the mod of.
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).

**Devuelve:** `int` — Returns the current modIndex, or `-1` if the mod is stock.

---
### GetVehicleModColor_1

`GET_VEHICLE_MOD_COLOR_1` · hash `0xE8D65CA700C9A693` · jhash `0xE625510A` · **Cliente**

```lua
local paintType, color, pearlescentColor = GetVehicleModColor_1(vehicle)
```
```c
void GET_VEHICLE_MOD_COLOR_1(Vehicle vehicle, int* paintType, int* color, int* pearlescentColor);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `paintType` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `color` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `pearlescentColor` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVehicleModColor_1Name

`GET_VEHICLE_MOD_COLOR_1_NAME` · hash `0xB45085B721EFD38C` · jhash `0x9A0840FD` · **Cliente**

```lua
local retval = GetVehicleModColor_1Name(vehicle, p1)
```
```c
char* GET_VEHICLE_MOD_COLOR_1_NAME(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `char*`

**Descripción oficial:**

```
returns a string which is the codename of the vehicle's currently selected primary color  
p1 is always 0  
```

**Nombres antiguos (alias):** `0xB45085B721EFD38C` (`N_0xb45085b721efd38c`)

---
### GetVehicleModColor_2

`GET_VEHICLE_MOD_COLOR_2` · hash `0x81592BE4E3878728` · jhash `0x9B76BB8E` · **Cliente**

```lua
local paintType, color = GetVehicleModColor_2(vehicle)
```
```c
void GET_VEHICLE_MOD_COLOR_2(Vehicle vehicle, int* paintType, int* color);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `paintType` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `color` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVehicleModColor_2Name

`GET_VEHICLE_MOD_COLOR_2_NAME` · hash `0x4967A516ED23A5A1` · jhash `0x9BDC0B49` · **Cliente**

```lua
local retval = GetVehicleModColor_2Name(vehicle)
```
```c
char* GET_VEHICLE_MOD_COLOR_2_NAME(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `char*`

**Descripción oficial:**

```
returns a string which is the codename of the vehicle's currently selected secondary color  
```

**Nombres antiguos (alias):** `0x4967A516ED23A5A1` (`N_0x4967a516ed23a5a1`)

---
### GetVehicleModIdentifierHash

`GET_VEHICLE_MOD_IDENTIFIER_HASH` · hash `0x4593CF82AA179706` · jhash `0x94850968` · **Cliente**

```lua
local retval = GetVehicleModIdentifierHash(vehicle, modType, modIndex)
```
```c
Hash GET_VEHICLE_MOD_IDENTIFIER_HASH(Vehicle vehicle, int modType, int modIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).
- `modIndex` (`int`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Can be used for IS_DLC_VEHICLE_MOD and _0xC098810437312FFF
```

**Nombres antiguos (alias):** `0x4593CF82AA179706` (`N_0x4593cf82aa179706`), `_GET_VEHICLE_MOD_DATA` (`GetVehicleModData`)

---
### GetVehicleModKit

`GET_VEHICLE_MOD_KIT` · hash `0x6325D1A044AE510D` · jhash `0x9FE60927` · **Cliente**

```lua
local retval = GetVehicleModKit(vehicle)
```
```c
int GET_VEHICLE_MOD_KIT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleModKitType

`GET_VEHICLE_MOD_KIT_TYPE` · hash `0xFC058F5121E54C32` · jhash `0xE5F76765` · **Cliente**

```lua
local retval = GetVehicleModKitType(vehicle)
```
```c
int GET_VEHICLE_MOD_KIT_TYPE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleModModifierValue

`GET_VEHICLE_MOD_MODIFIER_VALUE` · hash `0x90A38E9838E0A8C1` · jhash `0x73AE5505` · **Cliente**

```lua
local retval = GetVehicleModModifierValue(vehicle, modType, modIndex)
```
```c
int GET_VEHICLE_MOD_MODIFIER_VALUE(Vehicle vehicle, int modType, int modIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).
- `modIndex` (`int`)

**Devuelve:** `int`

---
### GetVehicleModVariation

`GET_VEHICLE_MOD_VARIATION` · hash `0xB3924ECD70E095DC` · jhash `0xC1B92003` · **Cliente**

```lua
local retval = GetVehicleModVariation(vehicle, modType)
```
```c
BOOL GET_VEHICLE_MOD_VARIATION(Vehicle vehicle, int modType);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Only used for wheels(ModType = 23/24) Returns true if the wheels are custom wheels
```

---
### GetVehicleModelAcceleration

`GET_VEHICLE_MODEL_ACCELERATION` · hash `0x8C044C5C84505B6A` · jhash `0x29CB3537` · **Cliente**

```lua
local retval = GetVehicleModelAcceleration(modelHash)
```
```c
float GET_VEHICLE_MODEL_ACCELERATION(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Descripción oficial:**

Returns the acceleration of the specified model.

---
### GetVehicleModelEstimatedAgility

`_GET_VEHICLE_MODEL_ESTIMATED_AGILITY` · hash `0x53409B5163D5B846` · jhash `0x37FBA7BC` · **Cliente**

```lua
local retval = GetVehicleModelEstimatedAgility(modelHash)
```
```c
float _GET_VEHICLE_MODEL_ESTIMATED_AGILITY(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Descripción oficial:**

```
GET_VEHICLE_MODEL_*
9.8 * thrust if air vehicle, else 0.38 + drive force?
```

**Nombres antiguos (alias):** `0x53409B5163D5B846` (`N_0x53409b5163d5b846`), `_GET_VEHICLE_MODEL_DOWN_FORCE` (`GetVehicleModelDownForce`)

---
### GetVehicleModelEstimatedMaxSpeed

`GET_VEHICLE_MODEL_ESTIMATED_MAX_SPEED` · hash `0xF417C2502FFFED43` · jhash `0x8F291C4A` · **Cliente**

```lua
local retval = GetVehicleModelEstimatedMaxSpeed(modelHash)
```
```c
float GET_VEHICLE_MODEL_ESTIMATED_MAX_SPEED(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Descripción oficial:**

```
Returns max speed (without mods) of the specified vehicle model in m/s.
```

**Nombres antiguos (alias):** `_GET_VEHICLE_MODEL_MAX_SPEED` (`GetVehicleModelMaxSpeed`)

---
### GetVehicleModelMaxBraking

`GET_VEHICLE_MODEL_MAX_BRAKING` · hash `0xDC53FD41B4ED944C` · jhash `0x7EF02883` · **Cliente**

```lua
local retval = GetVehicleModelMaxBraking(modelHash)
```
```c
float GET_VEHICLE_MODEL_MAX_BRAKING(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Descripción oficial:**

```
Returns max braking of the specified vehicle model.
```

---
### GetVehicleModelMaxBrakingMaxMods

`GET_VEHICLE_MODEL_MAX_BRAKING_MAX_MODS` · hash `0xBFBA3BA79CFF7EBF` · jhash `0xF3A7293F` · **Cliente**

```lua
local retval = GetVehicleModelMaxBrakingMaxMods(modelHash)
```
```c
float GET_VEHICLE_MODEL_MAX_BRAKING_MAX_MODS(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xBFBA3BA79CFF7EBF` (`N_0xbfba3ba79cff7ebf`), `_GET_VEHICLE_MODEL_HAND_BRAKE` (`GetVehicleModelHandBrake`)

---
### GetVehicleModelMaxKnots

`_GET_VEHICLE_MODEL_MAX_KNOTS` · hash `0xC6AD107DDC9054CC` · jhash `0x95BB67EB` · **Cliente**

```lua
local retval = GetVehicleModelMaxKnots(modelHash)
```
```c
float _GET_VEHICLE_MODEL_MAX_KNOTS(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Descripción oficial:**

```
GET_VEHICLE_MODEL_*
Function pertains only to aviation vehicles.
```

**Nombres antiguos (alias):** `0xC6AD107DDC9054CC` (`N_0xc6ad107ddc9054cc`)

---
### GetVehicleModelMaxTraction

`GET_VEHICLE_MODEL_MAX_TRACTION` · hash `0x539DE94D44FDFD0D` · jhash `0x7F985597` · **Cliente**

```lua
local retval = GetVehicleModelMaxTraction(modelHash)
```
```c
float GET_VEHICLE_MODEL_MAX_TRACTION(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `float`

**Descripción oficial:**

```
Returns max traction of the specified vehicle model.
```

---
### GetVehicleModelNumberOfSeats

`GET_VEHICLE_MODEL_NUMBER_OF_SEATS` · hash `0x2AD93716F184EDA4` · jhash `0x838F7BF7` · **Cliente**

```lua
local retval = GetVehicleModelNumberOfSeats(modelHash)
```
```c
int GET_VEHICLE_MODEL_NUMBER_OF_SEATS(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Returns max number of passengers (including the driver) for the specified vehicle model.
```

**Nombres antiguos (alias):** `_GET_VEHICLE_MODEL_MAX_NUMBER_OF_PASSENGERS` (`GetVehicleModelMaxNumberOfPassengers`)

---
### GetVehicleModelValue

`GET_VEHICLE_MODEL_VALUE` · hash `0x5873C14A52D74236` · jhash `0x58FEFC3D` · **Cliente**

```lua
local retval = GetVehicleModelValue(vehicleModel)
```
```c
int GET_VEHICLE_MODEL_VALUE(Hash vehicleModel);
```

**Parámetros**

- `vehicleModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Returns `nMonetaryValue` from handling.meta for specific model, which is the vehicle's monetary value.
```

**Nombres antiguos (alias):** `0x5873C14A52D74236` (`N_0x5873c14a52d74236`), `_GET_VEHICLE_MODEL_MONETARY_VALUE` (`GetVehicleModelMonetaryValue`)

---
### GetVehicleNeonLightsColour

`_GET_VEHICLE_NEON_LIGHTS_COLOUR` · hash `0x7619EEE8C886757F` · **Cliente**

```lua
local r, g, b = GetVehicleNeonLightsColour(vehicle)
```
```c
void _GET_VEHICLE_NEON_LIGHTS_COLOUR(Vehicle vehicle, int* r, int* g, int* b);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `r` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `g` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `b` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

Gets the color of the neon lights of the specified vehicle.

See [`_SET_VEHICLE_NEON_LIGHTS_COLOUR`](VEHICLE-2.md#setvehicleneonlightscolour) for more information

---
### GetVehicleNumberOfBrokenBones

`_GET_VEHICLE_NUMBER_OF_BROKEN_BONES` · hash `0x2C8CBFE1EA5FC631` · jhash `0xABC99E21` · **Cliente**

```lua
local retval = GetVehicleNumberOfBrokenBones(vehicle)
```
```c
int _GET_VEHICLE_NUMBER_OF_BROKEN_BONES(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x2C8CBFE1EA5FC631` (`N_0x2c8cbfe1ea5fc631`)

---
### GetVehicleNumberOfBrokenOffBones

`_GET_VEHICLE_NUMBER_OF_BROKEN_OFF_BONES` · hash `0x42A4BEB35D372407` · jhash `0x8CDB0C09` · **Cliente**

```lua
local retval = GetVehicleNumberOfBrokenOffBones(vehicle)
```
```c
int _GET_VEHICLE_NUMBER_OF_BROKEN_OFF_BONES(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
Also includes some "turnOffBones" when vehicle mods are installed.
```

**Nombres antiguos (alias):** `0x42A4BEB35D372407` (`N_0x42a4beb35d372407`)

---
### GetVehicleNumberOfPassengers

`GET_VEHICLE_NUMBER_OF_PASSENGERS` · hash `0x24CB2137731FFE89` · jhash `0x1EF20849` · **Cliente**

```lua
local retval = GetVehicleNumberOfPassengers(vehicle)
```
```c
int GET_VEHICLE_NUMBER_OF_PASSENGERS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the number of passengers, NOT including the driver. Use IS_VEHICLE_SEAT_FREE(Vehicle, -1) to also check for the driver  
```

---
### GetVehicleNumberPlateText

`GET_VEHICLE_NUMBER_PLATE_TEXT` · hash `0x7CE1CCB9B293020E` · jhash `0xE8522D58` · **Cliente**

```lua
local retval = GetVehicleNumberPlateText(vehicle)
```
```c
char* GET_VEHICLE_NUMBER_PLATE_TEXT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns the license plate text from a vehicle.  8 chars maximum.  
```

---
### GetVehicleNumberPlateTextIndex

`GET_VEHICLE_NUMBER_PLATE_TEXT_INDEX` · hash `0xF11BC2DD9A3E7195` · jhash `0x499747B6` · **Cliente**

```lua
local retval = GetVehicleNumberPlateTextIndex(vehicle)
```
```c
int GET_VEHICLE_NUMBER_PLATE_TEXT_INDEX(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to get the plate index of

**Devuelve:** `int` — Returns the plate index, reference `eVehiclePlateIndicies`

**Descripción oficial:**

```cpp
enum eVehiclePlateIndicies {
	SanAndreasCursive = 0,
	SanAndreasBlack = 1,
	SanAndreasBlue = 2,
	SanAndreasPlain = 3,
	SRExcept = 4,
	NorthYankton = 5,
	// All indicies below this require b3095
	ECola = 6,
	LasVenturas = 7,
	LiberyCity = 8,
	LSCarMeet = 9,
	LSPanic = 10,
	LSPounders = 11,
	Sprunk = 12,
}
```

---
### GetVehiclePetrolTankHealth

`GET_VEHICLE_PETROL_TANK_HEALTH` · hash `0x7D5DABE888D2D074` · jhash `0xE41595CE` · **Cliente**

```lua
local retval = GetVehiclePetrolTankHealth(vehicle)
```
```c
float GET_VEHICLE_PETROL_TANK_HEALTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
1000 is max health  
Begins leaking gas at around 650 health  
```

---
### GetVehiclePlateType

`GET_VEHICLE_PLATE_TYPE` · hash `0x9CCC9525BF2408E0` · jhash `0x65CA9286` · **Cliente**

```lua
local retval = GetVehiclePlateType(vehicle)
```
```c
int GET_VEHICLE_PLATE_TYPE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int` — Returns the vehicle plate type, refer to `eVehiclePlateType`

**Descripción oficial:**

Returns the plates a vehicle has.

```cpp
enum eVehiclePlateType
{
	VPT_FRONT_AND_BACK_PLATES = 0,
	VPT_FRONT_PLATES = 1,
	VPT_BACK_PLATES = 2,
	VPT_NONE = 3,
};
```

Motorcycles with no visible plates will sometimes return a 2 for unknown reasons.

---
### GetVehicleRecordingId

`GET_VEHICLE_RECORDING_ID` · hash `0x21543C612379DB3C` · jhash `0x328D601D` · **Cliente**

```lua
local retval = GetVehicleRecordingId(recording, script)
```
```c
int GET_VEHICLE_RECORDING_ID(int recording, char* script);
```

**Parámetros**

- `recording` (`int`)
- `script` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

See [`REQUEST_VEHICLE_RECORDING`](#requestvehiclerecording).

---
### GetVehicleRoofLivery

`_GET_VEHICLE_ROOF_LIVERY` · hash `0x60190048C0764A26` · **Cliente**

```lua
local retval = GetVehicleRoofLivery(vehicle)
```
```c
int _GET_VEHICLE_ROOF_LIVERY(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.

**Devuelve:** `int` — An index of the current vehicle's rooftop livery.

**Descripción oficial:**

Returns index of the current vehicle's rooftop livery.
A getter for [\_SET_VEHICLE_ROOF_LIVERY](VEHICLE-2.md#setvehiclerooflivery).

**Nombres antiguos (alias):** `0x60190048C0764A26` (`N_0x60190048c0764a26`)

---
### GetVehicleRoofLiveryCount

`_GET_VEHICLE_ROOF_LIVERY_COUNT` · hash `0x5ECB40269053C0D4` · **Cliente**

```lua
local retval = GetVehicleRoofLiveryCount(vehicle)
```
```c
int _GET_VEHICLE_ROOF_LIVERY_COUNT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.

**Devuelve:** `int` — A number of available rooftop liveries for vehicle.

**Descripción oficial:**

Returns a number of available rooftop liveries, or -1 if vehicle has no rooftop liveries available.

**Nombres antiguos (alias):** `0x5ECB40269053C0D4` (`N_0x5ecb40269053c0d4`)

---
### GetVehicleSuspensionBounds

`_GET_VEHICLE_SUSPENSION_BOUNDS` · hash `0xDF7E3EEB29642C38` · **Cliente**

```lua
local out1, out2 = GetVehicleSuspensionBounds(vehicle)
```
```c
void _GET_VEHICLE_SUSPENSION_BOUNDS(Vehicle vehicle, Vector3* out1, Vector3* out2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `out1` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `out2` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Outputs 2 Vector3's.
Scripts check if out2.x - out1.x > something.x
Could be suspension related, as in max suspension height and min suspension height, considering the natives location.
```

**Nombres antiguos (alias):** `0xDF7E3EEB29642C38` (`N_0xdf7e3eeb29642c38`)

---
### GetVehicleSuspensionHeight

`_GET_VEHICLE_SUSPENSION_HEIGHT` · hash `0x53952FD2BAA19F17` · jhash `0xB73A1486` · **Cliente**

```lua
local retval = GetVehicleSuspensionHeight(vehicle)
```
```c
float _GET_VEHICLE_SUSPENSION_HEIGHT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

```
Gets the height of the vehicle's suspension.  
The higher the value the lower the suspension. Each 0.002 corresponds with one more level lowered.  
0.000 is the stock suspension.  
0.008 is Ultra Suspension.  
```

---
### GetVehicleTrailerVehicle

`GET_VEHICLE_TRAILER_VEHICLE` · hash `0x1CDD6BADC297830D` · jhash `0xAE84D758` · **Cliente**

```lua
local retval, trailer = GetVehicleTrailerVehicle(vehicle, trailer)
```
```c
BOOL GET_VEHICLE_TRAILER_VEHICLE(Vehicle vehicle, Vehicle* trailer);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `trailer` (`Vehicle*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets the trailer of a vehicle and puts it into the trailer parameter.  
```

---
### GetVehicleTyreSmokeColor

`GET_VEHICLE_TYRE_SMOKE_COLOR` · hash `0xB635392A4938B3C3` · jhash `0x75280015` · **Cliente**

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
### GetVehicleTyresCanBurst

`GET_VEHICLE_TYRES_CAN_BURST` · hash `0x678B9BB8C3F58FEB` · jhash `0x4D76CD2F` · **Cliente**

```lua
local retval = GetVehicleTyresCanBurst(vehicle)
```
```c
BOOL GET_VEHICLE_TYRES_CAN_BURST(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### GetVehicleWeaponRestrictedAmmo

`GET_VEHICLE_WEAPON_RESTRICTED_AMMO` · hash `0x8181CE2F25CB9BB7` · **Cliente**

```lua
local retval = GetVehicleWeaponRestrictedAmmo(vehicle, weaponIndex)
```
```c
int GET_VEHICLE_WEAPON_RESTRICTED_AMMO(Vehicle vehicle, int weaponIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle
- `weaponIndex` (`int`): The weapon index we're getting ammo for (see [SET_VEHICLE_WEAPON_RESTRICTED_AMMO](VEHICLE-2.md#setvehicleweaponrestrictedammo) for information on how to access these slots).

**Devuelve:** `int` — Gets the current restricted ammo count for a particular vehicle weapon index on a vehicle.

**Nombres antiguos (alias):** `0x8181CE2F25CB9BB7` (`N_0x8181ce2f25cb9bb7`), `_GET_VEHICLE_WEAPON_CAPACITY` (`GetVehicleWeaponCapacity`)

---
### GetVehicleWheelType

`GET_VEHICLE_WHEEL_TYPE` · hash `0xB3ED1BFB4BE636DC` · jhash `0xDA58D7AE` · **Cliente**

```lua
local retval = GetVehicleWheelType(vehicle)
```
```c
int GET_VEHICLE_WHEEL_TYPE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int` — Returns an eVehicleWheelType integer value.

**Descripción oficial:**

```cpp
enum eVehicleWheelType
{
    VWT_SPORT = 0,
    VWT_MUSCLE = 1,
    VWT_LOWRIDER = 2,
    VWT_SUV = 3,
    VWT_OFFROAD = 4,
    VWT_TUNER = 5,
    VWT_BIKE = 6,
    VWT_HIEND = 7,
    // Benny's Original
    VWT_SUPERMOD1 = 8,
    // Benny's Bespoke
    VWT_SUPERMOD2 = 9,
    // Open Wheel
    VWT_SUPERMOD3 = 10,
    // Street
    VWT_SUPERMOD4 = 11,
    // Track
    VWT_SUPERMOD5 = 12,
};
```

---
### GetVehicleWindowTint

`GET_VEHICLE_WINDOW_TINT` · hash `0x0EE21293DAD47C95` · jhash `0x13D53892` · **Cliente**

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
### GetVehicleXenonLightsColor

`_GET_VEHICLE_XENON_LIGHTS_COLOR` · hash `0x3DFF319A831E0CDB` · **Cliente**

```lua
local retval = GetVehicleXenonLightsColor(vehicle)
```
```c
int _GET_VEHICLE_XENON_LIGHTS_COLOR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to get the headlight color from.

**Devuelve:** `int` — Returns the xenons light color, refer to `eHeadlightColors`

**Descripción oficial:**

Use [\_SET_VEHICLE_HEADLIGHTS_COLOUR](VEHICLE-2.md#setvehiclexenonlightscolor) to set the headlights color for the vehicle.

You must enable xenon headlights for this native to work properly.

```cpp
enum eHeadlightColors {
    Default = 255,
    White = 0,
    Blue = 1,
    ElectricBlue = 2,
    MintGreen = 3,
    LimeGreen = 4,
    Yellow = 5,
    GoldenShower = 6,
    Orange = 7,
    Red = 8,
    PonyPink = 9,
    HotPink = 10,
    Purple = 11,
    Blacklight = 12
}
```

**Nombres antiguos (alias):** `0x3DFF319A831E0CDB` (`N_0x3dff319a831e0cdb`), `_GET_VEHICLE_HEADLIGHTS_COLOUR` (`GetVehicleHeadlightsColour`), `_GET_VEHICLE_XENON_LIGHTS_COLOUR` (`GetVehicleXenonLightsColour`)

---
### HasFilledVehiclePopulation

`_HAS_FILLED_VEHICLE_POPULATION` · hash `0x91D6DD290888CBAB` · jhash `0x71D898EF` · **Cliente**

```lua
local retval = HasFilledVehiclePopulation()
```
```c
BOOL _HAS_FILLED_VEHICLE_POPULATION();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
HAS_*
```

**Nombres antiguos (alias):** `0x91D6DD290888CBAB` (`N_0x91d6dd290888cbab`)

---
### HasPreloadModsFinished

`HAS_PRELOAD_MODS_FINISHED` · hash `0x06F43E5175EB6D96` · jhash `0xA8A0D246` · **Cliente**

```lua
local retval = HasPreloadModsFinished(p0)
```
```c
BOOL HAS_PRELOAD_MODS_FINISHED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### HasVehicleAssetLoaded

`HAS_VEHICLE_ASSET_LOADED` · hash `0x1BBE0523B8DB9A21` · jhash `0x8DAAC3CB` · **Cliente**

```lua
local retval = HasVehicleAssetLoaded(vehicleAsset)
```
```c
BOOL HAS_VEHICLE_ASSET_LOADED(int vehicleAsset);
```

**Parámetros**

- `vehicleAsset` (`int`)

**Devuelve:** `BOOL`

---
### HasVehiclePhoneExplosiveDevice

`HAS_VEHICLE_PHONE_EXPLOSIVE_DEVICE` · hash `0x6ADAABD3068C5235` · jhash `0xA4E69134` · **Cliente**

```lua
local retval = HasVehiclePhoneExplosiveDevice()
```
```c
BOOL HAS_VEHICLE_PHONE_EXPLOSIVE_DEVICE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6ADAABD3068C5235` (`N_0x6adaabd3068c5235`)

---
### HasVehicleRecordingBeenLoaded

`HAS_VEHICLE_RECORDING_BEEN_LOADED` · hash `0x300D614A4C785FC4` · jhash `0xF52CD7F5` · **Cliente**

```lua
local retval = HasVehicleRecordingBeenLoaded(recording, script)
```
```c
BOOL HAS_VEHICLE_RECORDING_BEEN_LOADED(int recording, char* script);
```

**Parámetros**

- `recording` (`int`)
- `script` (`char*`)

**Devuelve:** `BOOL`

---
### HaveVehicleModsStreamedIn

`HAVE_VEHICLE_MODS_STREAMED_IN` · hash `0x9A83F5F9963775EF` · jhash `0x112D637A` · **Cliente**

```lua
local retval = HaveVehicleModsStreamedIn(vehicle)
```
```c
BOOL HAVE_VEHICLE_MODS_STREAMED_IN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9A83F5F9963775EF` (`N_0x9a83f5f9963775ef`), `_IS_VEHICLE_MOD_LOAD_DONE` (`IsVehicleModLoadDone`)

---
### HideVehicleTombstone

`_HIDE_VEHICLE_TOMBSTONE` · hash `0xAE71FB656C600587` · **Cliente**

```lua
HideVehicleTombstone(vehicle, toggle)
```
```c
void _HIDE_VEHICLE_TOMBSTONE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### InstantlyFillVehiclePopulation

`INSTANTLY_FILL_VEHICLE_POPULATION` · hash `0x48ADC8A773564670` · jhash `0x37BC6ACB` · **Cliente**

```lua
InstantlyFillVehiclePopulation()
```
```c
void INSTANTLY_FILL_VEHICLE_POPULATION();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x48ADC8A773564670` (`N_0x48adc8a773564670`)

---
### IsAnyEntityAttachedToHandlerFrame

`IS_ANY_ENTITY_ATTACHED_TO_HANDLER_FRAME` · hash `0x62CA17B74C435651` · jhash `0x593143B9` · **Cliente**

```lua
local retval = IsAnyEntityAttachedToHandlerFrame(vehicle)
```
```c
BOOL IS_ANY_ENTITY_ATTACHED_TO_HANDLER_FRAME(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x62CA17B74C435651` (`N_0x62ca17b74c435651`)

---
### IsAnyPedRappellingFromHeli

`IS_ANY_PED_RAPPELLING_FROM_HELI` · hash `0x291E373D483E7EE7` · jhash `0xD656E7E5` · **Cliente**

```lua
local retval = IsAnyPedRappellingFromHeli(vehicle)
```
```c
BOOL IS_ANY_PED_RAPPELLING_FROM_HELI(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x291E373D483E7EE7` (`N_0x291e373d483e7ee7`), `_ANY_PASSENGERS_RAPPELING` (`AnyPassengersRappeling`), `_IS_ANY_PASSENGER_RAPPELING_FROM_VEHICLE` (`IsAnyPassengerRappelingFromVehicle`)

---
### IsAnyVehicleNearPoint

`IS_ANY_VEHICLE_NEAR_POINT` · hash `0x61E1DD6125A3EEE6` · jhash `0x2867A834` · **Cliente**

```lua
local retval = IsAnyVehicleNearPoint(x, y, z, radius)
```
```c
BOOL IS_ANY_VEHICLE_NEAR_POINT(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

---
### IsBigVehicle

`IS_BIG_VEHICLE` · hash `0x9F243D3919F442FE` · jhash `0x9CDBA8DE` · **Cliente**

```lua
local retval = IsBigVehicle(vehicle)
```
```c
BOOL IS_BIG_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsBoatAnchored

`IS_BOAT_ANCHORED` · hash `0xB0AD1238A709B1A2` · **Cliente**

```lua
local retval = IsBoatAnchored(boat)
```
```c
BOOL IS_BOAT_ANCHORED(Vehicle boat);
```

**Parámetros**

- `boat` (`Vehicle`): The boat to check.

**Devuelve:** `BOOL` — Returns `true` if the boat is currently anchored, `false` otherwise.

**Descripción oficial:**

Checks if a boat is currently anchored.

This native is a getter for [SET_BOAT_ANCHOR](#setboatanchor).

```
NativeDB Introduced: v573
```

**Nombres antiguos (alias):** `0xB0AD1238A709B1A2` (`N_0xb0ad1238a709b1a2`), `_IS_BOAT_ANCHORED_AND_FROZEN` (`IsBoatAnchoredAndFrozen`)

---
### IsCopVehicleInArea_3d

`IS_COP_VEHICLE_IN_AREA_3D` · hash `0x7EEF65D5F153E26A` · jhash `0xFB16C6D1` · **Cliente**

```lua
local retval = IsCopVehicleInArea_3d(x1, x2, y1, y2, z1, z2)
```
```c
BOOL IS_COP_VEHICLE_IN_AREA_3D(float x1, float x2, float y1, float y2, float z1, float z2);
```

**Parámetros**

- `x1` (`float`)
- `x2` (`float`)
- `y1` (`float`)
- `y2` (`float`)
- `z1` (`float`)
- `z2` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Usage:  
public bool isCopInRange(Vector3 Location, float Range)  
        {  
            return Function.Call<bool>(Hash.IS_COP_PED_IN_AREA_3D, Location.X - Range, Location.Y - Range, Location.Z - Range, Location.X + Range, Location.Y + Range, Location.Z + Range);  
        }  
```

---
### IsEntityAttachedToHandlerFrame

`IS_ENTITY_ATTACHED_TO_HANDLER_FRAME` · hash `0x57715966069157AD` · jhash `0x7FB25568` · **Cliente**

```lua
local retval = IsEntityAttachedToHandlerFrame(vehicle, entity)
```
```c
BOOL IS_ENTITY_ATTACHED_TO_HANDLER_FRAME(Vehicle vehicle, Entity entity);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `entity` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `SET_PED_ENABLED_BIKE_RINGTONE` (`SetPedEnabledBikeRingtone`), `_IS_VEHICLE_NEAR_ENTITY` (`IsVehicleNearEntity`)

---
### IsEntryPointForSeatClear

`IS_ENTRY_POINT_FOR_SEAT_CLEAR` · hash `0x639431E895B9AA57` · jhash `0xAB0E79EB` · **Cliente**

```lua
local retval = IsEntryPointForSeatClear(ped, vehicle, seatIndex, checkSide, leftSide)
```
```c
BOOL IS_ENTRY_POINT_FOR_SEAT_CLEAR(Ped ped, Vehicle vehicle, int seatIndex, BOOL checkSide, BOOL leftSide);
```

**Parámetros**

- `ped` (`Ped`): The ped to check.
- `vehicle` (`Vehicle`): The vehicle to check.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](#isvehicleseatfree).
- `checkSide` (`BOOL`): True to check the side of the entry point relative to the vehicle
- `leftSide` (`BOOL`): When checkSide is true together with this it only checks if entrypoints on the left side of the vehicle are clear, and for the right side when given false

**Devuelve:** `BOOL` — True if the entry point is accesible and the area is clear for the given ped.

**Descripción oficial:**

Check if a entry point for a certain seat is clear, useful for checking if a vehicle seat is accesible.
If you park your vehicle near a wall and the ped cannot enter/exit this side, the return value toggles from true (not blocked) to false (blocked).

Keep in mind, with checkSide set to true, that only certain vehicles have entry points on both sides for the same seat, like motorcycles, most normal vehicles don't have this and if the native doesn't find a entry point with the given parameters it will always return false. So for most normal usecases leaving checkSide set to false would result in the expected behavior.

**Nombres antiguos (alias):** `0x639431E895B9AA57` (`N_0x639431e895b9aa57`), `_IS_VEHICLE_SEAT_ACCESSIBLE` (`IsVehicleSeatAccessible`)

---
### IsHandlerFrameAboveContainer

`_IS_HANDLER_FRAME_ABOVE_CONTAINER` · hash `0x89D630CF5EA96D23` · jhash `0xFBF5536A` · **Cliente**

```lua
local retval = IsHandlerFrameAboveContainer(handler, container)
```
```c
BOOL _IS_HANDLER_FRAME_ABOVE_CONTAINER(Vehicle handler, Entity container);
```

**Parámetros**

- `handler` (`Vehicle`)
- `container` (`Entity`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x89D630CF5EA96D23` (`N_0x89d630cf5ea96d23`)

---
### IsHeliLandingAreaBlocked

`IS_HELI_LANDING_AREA_BLOCKED` · hash `0x634148744F385576` · jhash `0x6346B7CC` · **Cliente**

```lua
local retval = IsHeliLandingAreaBlocked(vehicle)
```
```c
BOOL IS_HELI_LANDING_AREA_BLOCKED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x634148744F385576` (`N_0x634148744f385576`)

---
### IsHeliPartBroken

`IS_HELI_PART_BROKEN` · hash `0xBC74B4BE25EB6C8A` · jhash `0xF4E4C439` · **Cliente**

```lua
local retval = IsHeliPartBroken(vehicle, p1, p2, p3)
```
```c
BOOL IS_HELI_PART_BROKEN(Vehicle vehicle, BOOL p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsMissionTrain

`_IS_MISSION_TRAIN` · hash `0xAD464F2E18836BFC` · **Cliente**

```lua
local retval = IsMissionTrain(vehicle)
```
```c
BOOL _IS_MISSION_TRAIN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### IsNitrousActive

`IS_NITROUS_ACTIVE` · hash `0x491E822B2C464FE4` · **Cliente**

```lua
local retval = IsNitrousActive(vehicle)
```
```c
BOOL IS_NITROUS_ACTIVE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `BOOL` — Returns `true` if nitrous is active, otherwise `false`.

**Descripción oficial:**

```
NativeDB Introduced: 3095
```

Determines if the nitrous is currently activated in the specified vehicle.

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if vehicle == 0 then return end

-- Print whether nitrous is active in the vehicle (True or False).
print(IsNitrousActive(vehicle))
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Print whether nitrous is active in the vehicle (True or False).
console.log(IsNitrousActive(vehicle));
```

**Ejemplo (csharp):**

```csharp
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Print whether nitrous is active in the vehicle (True or False).
Debug.WriteLine(IsNitrousActive(vehicle));
```

---
### IsPedExclusiveDriverOfVehicle

`_IS_PED_EXCLUSIVE_DRIVER_OF_VEHICLE` · hash `0xB09D25E77C33EB3F` · **Cliente**

```lua
local retval, outIndex = IsPedExclusiveDriverOfVehicle(ped, vehicle, outIndex)
```
```c
BOOL _IS_PED_EXCLUSIVE_DRIVER_OF_VEHICLE(Ped ped, Vehicle vehicle, int* outIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `outIndex` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB09D25E77C33EB3F` (`N_0xb09d25e77c33eb3f`)

---
### IsPlaneLandingGearIntact

`IS_PLANE_LANDING_GEAR_INTACT` · hash `0x4198AB0022B15F87` · jhash `0xBD085DCA` · **Cliente**

```lua
local retval = IsPlaneLandingGearIntact(plane)
```
```c
BOOL IS_PLANE_LANDING_GEAR_INTACT(Vehicle plane);
```

**Parámetros**

- `plane` (`Vehicle`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4198AB0022B15F87` (`N_0x4198ab0022b15f87`), `_VEHICLE_HAS_LANDING_GEAR` (`VehicleHasLandingGear`)

---
### IsPlaybackGoingOnForVehicle

`IS_PLAYBACK_GOING_ON_FOR_VEHICLE` · hash `0x1C8A4C2C19E68EEC` · jhash `0x61F7650D` · **Cliente**

```lua
local retval = IsPlaybackGoingOnForVehicle(vehicle)
```
```c
BOOL IS_PLAYBACK_GOING_ON_FOR_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsPlaybackUsingAiGoingOnForVehicle

`IS_PLAYBACK_USING_AI_GOING_ON_FOR_VEHICLE` · hash `0xAEA8FD591FAD4106` · jhash `0x63022C58` · **Cliente**

```lua
local retval = IsPlaybackUsingAiGoingOnForVehicle(vehicle)
```
```c
BOOL IS_PLAYBACK_USING_AI_GOING_ON_FOR_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsSeatWarpOnly

`IS_SEAT_WARP_ONLY` · hash `0xF7F203E31F96F6A1` · jhash `0x769E5CF2` · **Cliente**

```lua
local retval = IsSeatWarpOnly(vehicle, seatIndex)
```
```c
BOOL IS_SEAT_WARP_ONLY(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](#isvehicleseatfree).

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF7F203E31F96F6A1` (`N_0xf7f203e31f96f6a1`)

---
### IsTaxiLightOn

`IS_TAXI_LIGHT_ON` · hash `0x7504C0F113AB50FC` · jhash `0x6FC4924A` · **Cliente**

```lua
local retval = IsTaxiLightOn(vehicle)
```
```c
BOOL IS_TAXI_LIGHT_ON(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsThisModelABicycle

`IS_THIS_MODEL_A_BICYCLE` · hash `0xBF94DD42F63BDED2` · jhash `0x328E6FF5` · **Cliente**

```lua
local retval = IsThisModelABicycle(model)
```
```c
BOOL IS_THIS_MODEL_A_BICYCLE(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelABike

`IS_THIS_MODEL_A_BIKE` · hash `0xB50C0B0CEDC6CE84` · jhash `0x7E702CDD` · **Cliente**

```lua
local retval = IsThisModelABike(model)
```
```c
BOOL IS_THIS_MODEL_A_BIKE(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelABoat

`IS_THIS_MODEL_A_BOAT` · hash `0x45A9187928F4B9E3` · jhash `0x10F6085C` · **Cliente**

```lua
local retval = IsThisModelABoat(model)
```
```c
BOOL IS_THIS_MODEL_A_BOAT(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelACar

`IS_THIS_MODEL_A_CAR` · hash `0x7F6DB52EEFC96DF8` · jhash `0x60E4C22F` · **Cliente**

```lua
local retval = IsThisModelACar(model)
```
```c
BOOL IS_THIS_MODEL_A_CAR(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
To check if the model is an amphibious car, see gtaforums.com/topic/717612-v-scriptnative-documentation-and-research/page-33#entry1069317363 (for build 944 and above only!)  
```

---
### IsThisModelAHeli

`IS_THIS_MODEL_A_HELI` · hash `0xDCE4334788AF94EA` · jhash `0x8AF7F568` · **Cliente**

```lua
local retval = IsThisModelAHeli(model)
```
```c
BOOL IS_THIS_MODEL_A_HELI(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelAJetski

`_IS_THIS_MODEL_A_JETSKI` · hash `0x9537097412CF75FE` · **Cliente**

```lua
local retval = IsThisModelAJetski(model)
```
```c
BOOL _IS_THIS_MODEL_A_JETSKI(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks if model is a boat, then checks for FLAG_IS_JETSKI.
```

**Nombres antiguos (alias):** `_IS_THIS_MODEL_A_SUBMERSIBLE` (`IsThisModelASubmersible`), `_IS_THIS_MODEL_AN_EMERGENCY_BOAT` (`IsThisModelAnEmergencyBoat`)

---
### IsThisModelAPlane

`IS_THIS_MODEL_A_PLANE` · hash `0xA0948AB42D7BA0DE` · jhash `0x3B3907BB` · **Cliente**

```lua
local retval = IsThisModelAPlane(model)
```
```c
BOOL IS_THIS_MODEL_A_PLANE(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelAQuadbike

`IS_THIS_MODEL_A_QUADBIKE` · hash `0x39DAC362EE65FA28` · jhash `0xC1625277` · **Cliente**

```lua
local retval = IsThisModelAQuadbike(model)
```
```c
BOOL IS_THIS_MODEL_A_QUADBIKE(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelATrain

`IS_THIS_MODEL_A_TRAIN` · hash `0xAB935175B22E822B` · jhash `0xF87DCFFD` · **Cliente**

```lua
local retval = IsThisModelATrain(model)
```
```c
BOOL IS_THIS_MODEL_A_TRAIN(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelAnAmphibiousCar

`_IS_THIS_MODEL_AN_AMPHIBIOUS_CAR` · hash `0x633F6F44A537EBB6` · **Cliente**

```lua
local retval = IsThisModelAnAmphibiousCar(model)
```
```c
BOOL _IS_THIS_MODEL_AN_AMPHIBIOUS_CAR(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsThisModelAnAmphibiousQuadbike

`_IS_THIS_MODEL_AN_AMPHIBIOUS_QUADBIKE` · hash `0xA1A9FC1C76A6730D` · **Cliente**

```lua
local retval = IsThisModelAnAmphibiousQuadbike(model)
```
```c
BOOL _IS_THIS_MODEL_AN_AMPHIBIOUS_QUADBIKE(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA1A9FC1C76A6730D` (`N_0xa1a9fc1c76a6730d`)

---
### IsToggleModOn

`IS_TOGGLE_MOD_ON` · hash `0x84B233A8C8FC8AE7` · jhash `0xF0E1689F` · **Cliente**

```lua
local retval = IsToggleModOn(vehicle, modType)
```
```c
BOOL IS_TOGGLE_MOD_ON(Vehicle vehicle, int modType);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).

**Devuelve:** `BOOL`

---
### IsTurretSeat

`IS_TURRET_SEAT` · hash `0xE33FFA906CE74880` · jhash `0x7C43D32A` · **Cliente**

```lua
local retval = IsTurretSeat(vehicle, seatIndex)
```
```c
BOOL IS_TURRET_SEAT(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](#isvehicleseatfree).

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE33FFA906CE74880` (`N_0xe33ffa906ce74880`)

---
### IsVehicleAConvertible

`IS_VEHICLE_A_CONVERTIBLE` · hash `0x52F357A30698BCCE` · jhash `0x6EF54490` · **Cliente**

```lua
local retval = IsVehicleAConvertible(vehicle, checkRoofExtras)
```
```c
BOOL IS_VEHICLE_A_CONVERTIBLE(Vehicle vehicle, BOOL checkRoofExtras);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `checkRoofExtras` (`BOOL`): When set to `false`, the native checks only for vehicles with an animatable convertible roof. Set to `true` to include additional checks for vehicles that might have a non-animatable roof (i.e., using vehicle extras)

**Devuelve:** `BOOL` — Returns `true` if the vehicle is a convertible with an animatable roof or if `checkRoofExtras` is `true` and the vehicle has a roof (animatable or not). Returns `false` if the vehicle does not meet the criteria.

**Descripción oficial:**

Determines if a vehicle is a convertible with an animatable roof. This native checks if the specified vehicle model features a convertible roof that can be lowered or raised through an animation.

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if IsVehicleAConvertible(vehicle, false) then
    print("The vehicle is a convertible with an animatable roof.")
else
    print("The vehicle is not a convertible or does not have an animatable roof.")
end
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (IsVehicleAConvertible(vehicle, false)) {
    console.log("The vehicle is a convertible with an animatable roof.");
} else {
    console.log("The vehicle is not a convertible or does not have an animatable roof.");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (IsVehicleAConvertible(vehicle, false)) {
    Debug.WriteLine("The vehicle is a convertible with an animatable roof.");
} else {
    Debug.WriteLine("The vehicle is not a convertible or does not have an animatable roof.");
}
```

---
### IsVehicleAlarmActivated

`IS_VEHICLE_ALARM_ACTIVATED` · hash `0x4319E335B71FFF34` · jhash `0xF2630A4C` · **Cliente**

```lua
local retval = IsVehicleAlarmActivated(vehicle)
```
```c
BOOL IS_VEHICLE_ALARM_ACTIVATED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleAttachedToCargobob

`IS_VEHICLE_ATTACHED_TO_CARGOBOB` · hash `0xD40148F22E81A1D9` · jhash `0x5DEEC76C` · **Cliente**

```lua
local retval = IsVehicleAttachedToCargobob(cargobob, vehicleAttached)
```
```c
BOOL IS_VEHICLE_ATTACHED_TO_CARGOBOB(Vehicle cargobob, Vehicle vehicleAttached);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `vehicleAttached` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleAttachedToTowTruck

`IS_VEHICLE_ATTACHED_TO_TOW_TRUCK` · hash `0x146DF9EC4C4B9FD4` · jhash `0x9699CFDC` · **Cliente**

```lua
local retval = IsVehicleAttachedToTowTruck(towTruck, vehicle)
```
```c
BOOL IS_VEHICLE_ATTACHED_TO_TOW_TRUCK(Vehicle towTruck, Vehicle vehicle);
```

**Parámetros**

- `towTruck` (`Vehicle`)
- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Scripts verify that towTruck is the first parameter, not the second.  
```

---
### IsVehicleAttachedToTrailer

`IS_VEHICLE_ATTACHED_TO_TRAILER` · hash `0xE7CF3C4F9F489F0C` · jhash `0xE142BBCC` · **Cliente**

```lua
local retval = IsVehicleAttachedToTrailer(vehicle)
```
```c
BOOL IS_VEHICLE_ATTACHED_TO_TRAILER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleBeingHalted

`_IS_VEHICLE_BEING_HALTED` · hash `0xC69BB1D832A710EF` · **Cliente**

```lua
local retval = IsVehicleBeingHalted(vehicle)
```
```c
BOOL _IS_VEHICLE_BEING_HALTED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if vehicle is halted by BRING_VEHICLE_TO_HALT
_IS_VEHICLE_*
```

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0xC69BB1D832A710EF` (`N_0xc69bb1d832a710ef`)

---
### IsVehicleBumperBouncing

`IS_VEHICLE_BUMPER_BOUNCING` · hash `0x27B926779DEB502D` · jhash `0xB3A2CC4F` · **Cliente**

```lua
local retval = IsVehicleBumperBouncing(vehicle, frontBumper)
```
```c
BOOL IS_VEHICLE_BUMPER_BOUNCING(Vehicle vehicle, BOOL frontBumper);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `frontBumper` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x27B926779DEB502D` (`N_0x27b926779deb502d`)

---
### IsVehicleBumperBrokenOff

`IS_VEHICLE_BUMPER_BROKEN_OFF` · hash `0x468056A6BB6F3846` · jhash `0xAF25C027` · **Cliente**

```lua
local retval = IsVehicleBumperBrokenOff(vehicle, front)
```
```c
BOOL IS_VEHICLE_BUMPER_BROKEN_OFF(Vehicle vehicle, BOOL front);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `front` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsVehicleDamaged

`_IS_VEHICLE_DAMAGED` · hash `0xBCDC5017D3CE1E9E` · jhash `0xDAC523BC` · **Cliente**

```lua
local retval = IsVehicleDamaged(vehicle)
```
```c
BOOL _IS_VEHICLE_DAMAGED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Appears to return true if the vehicle has any damage, including cosmetically.
GET_*
```

---
### IsVehicleDoorDamaged

`IS_VEHICLE_DOOR_DAMAGED` · hash `0xB8E181E559464527` · jhash `0x4999E3C3` · **Cliente**

```lua
local retval = IsVehicleDoorDamaged(veh, doorID)
```
```c
BOOL IS_VEHICLE_DOOR_DAMAGED(Vehicle veh, int doorID);
```

**Parámetros**

- `veh` (`Vehicle`)
- `doorID` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](VEHICLE-2.md#setvehicledoorshut)

---
### IsVehicleDoorFullyOpen

`IS_VEHICLE_DOOR_FULLY_OPEN` · hash `0x3E933CFF7B111C22` · jhash `0xC2385B6F` · **Cliente**

```lua
local retval = IsVehicleDoorFullyOpen(vehicle, doorIndex)
```
```c
BOOL IS_VEHICLE_DOOR_FULLY_OPEN(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `doorIndex` (`int`): The index of the door to check.

**Devuelve:** `BOOL` — A bool indiciating if the specified door is fully open on the specified vehicle.

**Descripción oficial:**

See eDoorId declared in [`SET_VEHICLE_DOOR_SHUT`](VEHICLE-2.md#setvehicledoorshut)

---
### IsVehicleDriveable

`IS_VEHICLE_DRIVEABLE` · hash `0x4C241E39B23DF959` · jhash `0x41A7267A` · **Cliente**

```lua
local retval = IsVehicleDriveable(vehicle, isOnFireCheck)
```
```c
BOOL IS_VEHICLE_DRIVEABLE(Vehicle vehicle, BOOL isOnFireCheck);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `isOnFireCheck` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p1 is always 0 in the scripts.  
p1 = check if vehicle is on fire  
```

---
### IsVehicleEngineOnFire

`_IS_VEHICLE_ENGINE_ON_FIRE` · hash `0xEC69ADF931AAE0C3` · **Cliente**

```lua
local retval = IsVehicleEngineOnFire(vehicle)
```
```c
BOOL _IS_VEHICLE_ENGINE_ON_FIRE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `BOOL` — Returns true when the engine of your vehicle is on fire. Returns false if it's not on fire.

**Descripción oficial:**

Only ever used once in decompiled scripts: **am_pi_menu**:
Returns true if the engine is on fire, or if the vehicle engine health is < 0 and it **has been** on fire.

It sometimes doesn't return true when the vehicle engine has been on fire, and has since been fixed. I'm not really sure what the exact conditions are.

This usually returns true even if there are no visible flames yet (engine health > 0). However if you monitor engine health you'll see that it starts decreasing as soon as this returns true.

**Nombres antiguos (alias):** `0xEC69ADF931AAE0C3` (`N_0xec69adf931aae0c3`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetVehicleEngineHealth(vehicle, 99)

CreateThread(function()
    -- waiting for the vehicle to be on fire, usually takes one small
    -- crash into a wall or something to do this if engine health < 100.
    while IsVehicleEngineOnFire(vehicle) ~= 1 do
        Wait(0)
    end
    print("Vehicle is now on fire!")
end)
```

---
### IsVehicleExtraTurnedOn

`IS_VEHICLE_EXTRA_TURNED_ON` · hash `0xD2E6822DBFD6C8BD` · jhash `0x042098B5` · **Cliente**

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
### IsVehicleHighDetail

`IS_VEHICLE_HIGH_DETAIL` · hash `0x1F25887F3C104278` · jhash `0x55D41928` · **Cliente**

```lua
local retval = IsVehicleHighDetail(vehicle)
```
```c
BOOL IS_VEHICLE_HIGH_DETAIL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleInBurnout

`IS_VEHICLE_IN_BURNOUT` · hash `0x1297A88E081430EB` · jhash `0x6632BC12` · **Cliente**

```lua
local retval = IsVehicleInBurnout(vehicle)
```
```c
BOOL IS_VEHICLE_IN_BURNOUT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the specified vehicle is currently in a burnout.  
vb.net  
Public Function isVehicleInBurnout(vh As Vehicle) As Boolean  
        Return Native.Function.Call(Of Boolean)(Hash.IS_VEHICLE_IN_BURNOUT, vh)  
    End Function  
```

---
### IsVehicleInGarageArea

`IS_VEHICLE_IN_GARAGE_AREA` · hash `0xCEE4490CD57BB3C2` · jhash `0xA90EC257` · **Cliente**

```lua
local retval = IsVehicleInGarageArea(garageName, vehicle)
```
```c
BOOL IS_VEHICLE_IN_GARAGE_AREA(char* garageName, Vehicle vehicle);
```

**Parámetros**

- `garageName` (`char*`)
- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
garageName example "Michael - Beverly Hills"
```

---
### IsVehicleInSubmarineMode

`IS_VEHICLE_IN_SUBMARINE_MODE` · hash `0xA77DC70BD689A1E5` · jhash `0xE2FF06DB` · **Cliente**

```lua
local retval = IsVehicleInSubmarineMode(vehicle)
```
```c
BOOL IS_VEHICLE_IN_SUBMARINE_MODE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `_GET_IS_SUBMARINE_VEHICLE_TRANSFORMED` (`GetIsSubmarineVehicleTransformed`)

---
### IsVehicleModGen9Exclusive

`IS_VEHICLE_MOD_GEN9_EXCLUSIVE` · hash `0x00834EAC4A96E010` · jhash `0xEF66663B` · **Cliente**

```lua
local retval = IsVehicleModGen9Exclusive(vehicle, modType, modIndex)
```
```c
BOOL IS_VEHICLE_MOD_GEN9_EXCLUSIVE(Vehicle vehicle, int modType, int modIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle
- `modType` (`int`): The mod type (see [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod))
- `modIndex` (`int`): The mod index

**Devuelve:** `BOOL` — Returns whether the specified mod is exclusive to gen9 or not.

**Nombres antiguos (alias):** `0x00834EAC4A96E010` (`N_0x00834eac4a96e010`), `_IS_VEHICLE_MOD_HSW_EXCLUSIVE` (`IsVehicleModHswExclusive`)

---
### IsVehicleModel

`IS_VEHICLE_MODEL` · hash `0x423E8DE37D934D89` · jhash `0x013B10B6` · **Cliente**

```lua
local retval = IsVehicleModel(vehicle, model)
```
```c
BOOL IS_VEHICLE_MODEL(Vehicle vehicle, Hash model);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsVehicleNeonLightEnabled

`_IS_VEHICLE_NEON_LIGHT_ENABLED` · hash `0x8C4B92553E4766A5` · **Cliente**

```lua
local retval = IsVehicleNeonLightEnabled(vehicle, index)
```
```c
BOOL _IS_VEHICLE_NEON_LIGHT_ENABLED(Vehicle vehicle, int index);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `index` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
indices:  
0 = Left  
1 = Right  
2 = Front  
3 = Back  
```

---
### IsVehicleOnAllWheels

`IS_VEHICLE_ON_ALL_WHEELS` · hash `0xB104CD1BABF302E2` · jhash `0x10089F8E` · **Cliente**

```lua
local retval = IsVehicleOnAllWheels(vehicle)
```
```c
BOOL IS_VEHICLE_ON_ALL_WHEELS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Public Function isVehicleOnAllWheels(vh As Vehicle) As Boolean  
Return Native.Function.Call(Of Boolean)(Hash.IS_VEHICLE_ON_ALL_WHEELS, vh)  
		    End Function  
```

---
### IsVehicleOnBoostPad

`_IS_VEHICLE_ON_BOOST_PAD` · hash `0x71C6302CBCA6CA35` · **Cliente**

```lua
local retval = IsVehicleOnBoostPad(vehicle)
```
```c
BOOL _IS_VEHICLE_ON_BOOST_PAD(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `BOOL` — Return `true` if the vehicle is on a boost pad, `false` otherwise.

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### IsVehicleParachuteActive

`_IS_VEHICLE_PARACHUTE_ACTIVE` · hash `0x3DE51E9C80B116CF` · **Cliente**

```lua
local retval = IsVehicleParachuteActive(vehicle)
```
```c
BOOL _IS_VEHICLE_PARACHUTE_ACTIVE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Does not work for vehicle of type: CBike, CBmx, CBoat, CTrain, CSubmarine.

**Nombres antiguos (alias):** `0x3DE51E9C80B116CF` (`N_0x3de51e9c80b116cf`)

---
### IsVehicleRocketBoostActive

`_IS_VEHICLE_ROCKET_BOOST_ACTIVE` · hash `0x3D34E80EED4AE3BE` · **Cliente**

```lua
local retval = IsVehicleRocketBoostActive(vehicle)
```
```c
BOOL _IS_VEHICLE_ROCKET_BOOST_ACTIVE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleSearchlightOn

`IS_VEHICLE_SEARCHLIGHT_ON` · hash `0xC0F97FCE55094987` · jhash `0xADAF3513` · **Cliente**

```lua
local retval = IsVehicleSearchlightOn(vehicle)
```
```c
BOOL IS_VEHICLE_SEARCHLIGHT_ON(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Possibly: Returns whether the searchlight (found on police vehicles) is toggled on.  
```

---
### IsVehicleSeatFree

`IS_VEHICLE_SEAT_FREE` · hash `0x22AC59A870E6A669` · jhash `0xDAF42B02` · **Cliente**

```lua
local retval = IsVehicleSeatFree(vehicle, seatIndex)
```
```c
BOOL IS_VEHICLE_SEAT_FREE(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.
- `seatIndex` (`int`): The eSeatPosition or -2 for **any** vehicle seat.

**Devuelve:** `BOOL`

**Descripción oficial:**

Seat indices range from -1 to [`GET_VEHICLE_MAX_NUMBER_OF_PASSENGERS`](#getvehiclemaxnumberofpassengers) minus one.

```cpp
// CTaskExitVehicleSeat::eSeatPosition - 1
enum eSeatPosition
{
    SF_FrontDriverSide = -1,
    SF_FrontPassengerSide = 0,
    SF_BackDriverSide = 1,
    SF_BackPassengerSide = 2,
    SF_AltFrontDriverSide = 3,
    SF_AltFrontPassengerSide = 4,
    SF_AltBackDriverSide = 5,
    SF_AltBackPassengerSide = 6,
};
```

```
NativeDB Added Parameter 3: BOOL isTaskRunning

isTaskRunning = on true the function returns already false while a task on the target seat is running (TASK_ENTER_VEHICLE/TASK_SHUFFLE_TO_NEXT_VEHICLE_SEAT) - on false only when a ped is finally sitting in the seat.
```

---
### IsVehicleSirenAudioOn

`IS_VEHICLE_SIREN_AUDIO_ON` · hash `0xB5CC40FBCB586380` · jhash `0xC9458688` · **Cliente**

```lua
local retval = IsVehicleSirenAudioOn(vehicle)
```
```c
BOOL IS_VEHICLE_SIREN_AUDIO_ON(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check.

**Devuelve:** `BOOL` — Returns `true` if the siren audio is currently playing, `false` if it is silent or the vehicle does not have a siren.

**Descripción oficial:**

Checks if the siren audio is currently playing on the given vehicle.

This only checks the sound not the lights. A vehicle can have its siren lights active while the audio is silent, for example when [`SET_VEHICLE_HAS_MUTED_SIRENS`](VEHICLE-2.md#setvehiclehasmutedsirens) has been used to suppress the sound.

**Nombres antiguos (alias):** `0xB5CC40FBCB586380` (`N_0xb5cc40fbcb586380`), `_IS_VEHICLE_SIREN_SOUND_ON` (`IsVehicleSirenSoundOn`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

if IsVehicleSirenAudioOn(vehicle) then
    print("Siren is audible")
end
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);

if (IsVehicleSirenAudioOn(vehicle)) {
    console.log("Siren is audible");
}
```

---
### IsVehicleSirenOn

`IS_VEHICLE_SIREN_ON` · hash `0x4C9BF537BE2634B2` · jhash `0x25EB5873` · **Cliente**

```lua
local retval = IsVehicleSirenOn(vehicle)
```
```c
BOOL IS_VEHICLE_SIREN_ON(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL` — Returns false if siren and lights are disabled or true if they are enabled.

**Descripción oficial:**

Returns whether the vehicle's lights and sirens are on.

**Ejemplo (lua):**

```lua
local veh = GetVehiclePedIsIn(PlayerPedId())
print(tostring(IsVehicleSirenOn(veh))
```

---
### IsVehicleSlipstreamLeader

`_IS_VEHICLE_SLIPSTREAM_LEADER` · hash `0x48C633E94A8142A7` · **Cliente**

```lua
local retval = IsVehicleSlipstreamLeader(vehicle)
```
```c
BOOL _IS_VEHICLE_SLIPSTREAM_LEADER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL` — True if the vehicle is being slipstreamed by another vehicle

**Nombres antiguos (alias):** `0x48C633E94A8142A7` (`N_0x48c633e94a8142a7`)

---
### IsVehicleSprayable

`IS_VEHICLE_SPRAYABLE` · hash `0x8D474C8FAEFF6CDE` · jhash `0x5EB00A6A` · **Cliente**

```lua
local retval = IsVehicleSprayable(vehicle)
```
```c
BOOL IS_VEHICLE_SPRAYABLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns false if the vehicle has the FLAG_NO_RESPRAY flag set.
```

**Nombres antiguos (alias):** `0x8D474C8FAEFF6CDE` (`N_0x8d474c8faeff6cde`), `_IS_VEHICLE_SHOP_RESPRAY_ALLOWED` (`IsVehicleShopResprayAllowed`)

---
### IsVehicleStolen

`IS_VEHICLE_STOLEN` · hash `0x4AF9BD80EEBEB453` · jhash `0x20B61DDE` · **Cliente**

```lua
local retval = IsVehicleStolen(vehicle)
```
```c
BOOL IS_VEHICLE_STOLEN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleStopped

`IS_VEHICLE_STOPPED` · hash `0x5721B434AD84D57A` · jhash `0x655F072C` · **Cliente**

```lua
local retval = IsVehicleStopped(vehicle)
```
```c
BOOL IS_VEHICLE_STOPPED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL` — True if the vehicle's speed is equal to, or less than 0.02 meters per second, or 0.05 meters per second, if the vehicle's handbrake is engaged.

**Descripción oficial:**

```
Returns true if the vehicle's current speed is less than, or equal to 0.0025f.
For some vehicles it returns true if the current speed is <= 0.00039999999.
```

---
### IsVehicleStoppedAtTrafficLights

`IS_VEHICLE_STOPPED_AT_TRAFFIC_LIGHTS` · hash `0x2959F696AE390A99` · jhash `0x69200FA4` · **Cliente**

```lua
local retval = IsVehicleStoppedAtTrafficLights(vehicle)
```
```c
BOOL IS_VEHICLE_STOPPED_AT_TRAFFIC_LIGHTS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.

**Devuelve:** `BOOL` — Will return `true` if the vehicle is at an amber light junction and the vehicle driver's personality is set to not run amber lights, or if the vehicle is at a red light, regardless of the driver's personality. Will return `false` if the vehicle is stopped behind another vehicle waiting at a traffic light.

**Descripción oficial:**

This native checks if the given vehicle is stopped at a red or amber traffic light junction, provided the driver's personality is set to not run amber lights.

---
### IsVehicleStuckOnRoof

`IS_VEHICLE_STUCK_ON_ROOF` · hash `0xB497F06B288DCFDF` · jhash `0x18D07C6C` · **Cliente**

```lua
local retval = IsVehicleStuckOnRoof(vehicle)
```
```c
BOOL IS_VEHICLE_STUCK_ON_ROOF(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleStuckTimerUp

`IS_VEHICLE_STUCK_TIMER_UP` · hash `0x679BE1DAF71DA874` · jhash `0x2FCF58C1` · **Cliente**

```lua
local retval = IsVehicleStuckTimerUp(vehicle, p1, p2)
```
```c
BOOL IS_VEHICLE_STUCK_TIMER_UP(Vehicle vehicle, int p1, int p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`int`)
- `p2` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p1 can be anywhere from 0 to 3 in the scripts. p2 is generally somewhere in the 1000 to 10000 range.  
```

---
### IsVehicleTyreBurst

`IS_VEHICLE_TYRE_BURST` · hash `0xBA291848A0815CA9` · jhash `0x48C80210` · **Cliente**

```lua
local retval = IsVehicleTyreBurst(vehicle, wheelID, isBurstToRim)
```
```c
BOOL IS_VEHICLE_TYRE_BURST(Vehicle vehicle, int wheelID, BOOL isBurstToRim);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check the tire status of
- `wheelID` (`int`): The wheel id to check, see `eVehicleWheels`
- `isBurstToRim` (`BOOL`): Whether it should only return `true` if the tire is bursted to its rims

**Devuelve:** `BOOL` — Returns `true` if the vehicle tire is poped, `false` otherwise.

**Descripción oficial:**

```cpp
enum eVehicleWheels
{
	WHEEL_LF = 0, // Vehicle Left front
	WHEEL_RF = 1, // Vehicle Right front
	WHEEL_LM = 2, // Vehicle Left middle
	WHEEL_RM = 3, // Vehicle Right middle
	WHEEL_LR = 4, // Vehicle Left rear
	WHEEL_RR = 5, // Vehicle Right rear
	WHEEL_BF = 6, // Bike front
	WHEEL_BR = 7, // Bike rear
	MAX_WHEELS = 8
};
```

---
### IsVehicleVisible

`IS_VEHICLE_VISIBLE` · hash `0xAA0A52D24FB98293` · jhash `0x7E0D6056` · **Cliente**

```lua
local retval = IsVehicleVisible(vehicle)
```
```c
BOOL IS_VEHICLE_VISIBLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleWeaponDisabled

`_IS_VEHICLE_WEAPON_DISABLED` · hash `0x563B65A643ED072E` · **Cliente**

```lua
local retval = IsVehicleWeaponDisabled(weaponHash, vehicle, owner)
```
```c
BOOL _IS_VEHICLE_WEAPON_DISABLED(Hash weaponHash, Vehicle vehicle, Ped owner);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `vehicle` (`Vehicle`)
- `owner` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x563B65A643ED072E` (`N_0x563b65a643ed072e`)

---
### IsVehicleWindowIntact

`IS_VEHICLE_WINDOW_INTACT` · hash `0x46E571A0E20D01F1` · jhash `0xAC4EF23D` · **Cliente**

```lua
local retval = IsVehicleWindowIntact(vehicle, windowIndex)
```
```c
BOOL IS_VEHICLE_WINDOW_INTACT(Vehicle vehicle, int windowIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle
- `windowIndex` (`int`): The index of the window

**Devuelve:** `BOOL`

**Descripción oficial:**

```cpp
enum eWindowId {
	VEH_EXT_WINDOW_LF = 0,
	VEH_EXT_WINDOW_RF = 1,
	VEH_EXT_WINDOW_LR = 2,
	VEH_EXT_WINDOW_RR = 3,
	VEH_EXT_WINDOW_LM = 4,
	VEH_EXT_WINDOW_RM = 5,
	VEH_EXT_WINDSCREEN = 6,
	VEH_EXT_WINDSCREEN_R = 7,
}
```

---
### LowerConvertibleRoof

`LOWER_CONVERTIBLE_ROOF` · hash `0xDED51F703D0FA83D` · jhash `0xC5F72EAE` · **Cliente**

```lua
LowerConvertibleRoof(vehicle, instantlyLower)
```
```c
void LOWER_CONVERTIBLE_ROOF(Vehicle vehicle, BOOL instantlyLower);
```

**Parámetros**

- `vehicle` (`Vehicle`): The convertible vehicle whose roof you want to lower.
- `instantlyLower` (`BOOL`): A boolean value indicating whether the roof should be lowered instantly without transitioning through the animation. Set to `false` to lower the roof with the animation or `true` to lower it instantly.

**Devuelve:** `void`

**Descripción oficial:**

Lowers the roof on a convertible vehicle, utilizing any available animations for the action. This native is particularly useful for creating a realistic interaction with convertible vehicles by animating the process of lowering the roof.

You can check if the vehicle has an convertible roof using [`IS_VEHICLE_A_CONVERTIBLE`](#isvehicleaconvertible).

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if not IsVehicleAConvertible(vehicle, false) then return end
LowerConvertibleRoof(vehicle, false)
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!IsVehicleAConvertible(vehicle, false)) return;
LowerConvertibleRoof(vehicle, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!IsVehicleAConvertible(vehicle, false)) return;
LowerConvertibleRoof(vehicle, false);
```

---
### LowerRetractableWheels

`_LOWER_RETRACTABLE_WHEELS` · hash `0x5335BE58C083E74E` · **Cliente**

```lua
LowerRetractableWheels(vehicle)
```
```c
void _LOWER_RETRACTABLE_WHEELS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5335BE58C083E74E` (`N_0x5335be58c083e74e`)

---
### ModifyVehicleTopSpeed

`MODIFY_VEHICLE_TOP_SPEED` · hash `0x93A3996368C94158` · jhash `0xE943B09C` · **Cliente**

```lua
ModifyVehicleTopSpeed(vehicle, percentChange)
```
```c
void MODIFY_VEHICLE_TOP_SPEED(Vehicle vehicle, float percentChange);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `percentChange` (`float`): A percentage from 0 to 100, it can go past 100.

**Devuelve:** `void`

**Descripción oficial:**

Modifies a vehicle's top speed.

This is the native you have to call when trying to apply handling changes related to `fInitialDriveForce` and `fInitialDriveMaxFlatVel` via the [`SET_VEHICLE_HANDLING_FLOAT`](../cfx/cliente-1.md#setvehiclehandlingfloat) native, otherwise your changes won't apply.

Calling this native will initiate transmission setup for the given vehicle so any transmission related changes apply, it will also update the drag coefficient on the vehicle based on the percentage change.

**Nombres antiguos (alias):** `_SET_VEHICLE_ENGINE_POWER_MULTIPLIER` (`SetVehicleEnginePowerMultiplier`)

---
### N_0x0205f5365292d2eb

`0x0205F5365292D2EB` · hash `0x0205F5365292D2EB` · **Cliente**

```lua
N_0x0205f5365292d2eb(vehicle, p1)
```
```c
void 0x0205F5365292D2EB(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x0419b167ee128f33

`0x0419B167EE128F33` · hash `0x0419B167EE128F33` · **Cliente**

```lua
local retval = N_0x0419b167ee128f33(p0, p1)
```
```c
Any 0x0419B167EE128F33(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0x0581730ab9380412

`0x0581730AB9380412` · hash `0x0581730AB9380412` · **Cliente**

```lua
N_0x0581730ab9380412(p0, p1, p2, p3, p4, p5)
```
```c
void 0x0581730AB9380412(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

---
### N_0x063ae2b2cc273588

`0x063AE2B2CC273588` · hash `0x063AE2B2CC273588` · jhash `0x2EF8435C` · **Cliente**

```lua
N_0x063ae2b2cc273588(vehicle, p1)
```
```c
void 0x063AE2B2CC273588(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
A vehicle recording playback flag only used in jewelry_heist
```

---
### N_0x065d03a9d6b2c6b5

`0x065D03A9D6B2C6B5` · hash `0x065D03A9D6B2C6B5` · **Cliente**

```lua
N_0x065d03a9d6b2c6b5(p0, p1)
```
```c
void 0x065D03A9D6B2C6B5(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x107a473d7a6647a9

`0x107A473D7A6647A9` · hash `0x107A473D7A6647A9` · **Cliente**

```lua
N_0x107a473d7a6647a9(vehicle)
```
```c
void 0x107A473D7A6647A9(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x1312ddd8385aee4e

`0x1312DDD8385AEE4E` · hash `0x1312DDD8385AEE4E` · **Cliente**

```lua
N_0x1312ddd8385aee4e(p0, p1)
```
```c
void 0x1312DDD8385AEE4E(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x182f266c2d9e2beb

`0x182F266C2D9E2BEB` · hash `0x182F266C2D9E2BEB` · jhash `0x7D0DE7EA` · **Cliente**

```lua
N_0x182f266c2d9e2beb(vehicle, p1)
```
```c
void 0x182F266C2D9E2BEB(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0x2310a8f9421ebf43

`0x2310A8F9421EBF43` · hash `0x2310A8F9421EBF43` · **Cliente**

```lua
N_0x2310a8f9421ebf43(p0)
```
```c
void 0x2310A8F9421EBF43(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### N_0x2311dd7159f00582

`0x2311DD7159F00582` · hash `0x2311DD7159F00582` · jhash `0x758C5E2E` · **Cliente**

```lua
N_0x2311dd7159f00582(vehicle, p1)
```
```c
void 0x2311DD7159F00582(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x2c4a1590abf43e8b

`0x2C4A1590ABF43E8B` · hash `0x2C4A1590ABF43E8B` · jhash `0x2EC19A8B` · **Cliente**

```lua
N_0x2c4a1590abf43e8b(vehicle, p1)
```
```c
void 0x2C4A1590ABF43E8B(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VEHICLE_W* (next character is either H or I)
```

---
### N_0x3441cad2f2231923

`0x3441CAD2F2231923` · hash `0x3441CAD2F2231923` · jhash `0xC306A9A3` · **Cliente**

```lua
N_0x3441cad2f2231923(vehicle, p1)
```
```c
void 0x3441CAD2F2231923(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x35bb21de06784373

`0x35BB21DE06784373` · hash `0x35BB21DE06784373` · **Cliente**

```lua
N_0x35bb21de06784373(p0, p1)
```
```c
void 0x35BB21DE06784373(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x35e0654f4bad7971

`0x35E0654F4BAD7971` · hash `0x35E0654F4BAD7971` · **Cliente**

```lua
N_0x35e0654f4bad7971(p0)
```
```c
void 0x35E0654F4BAD7971(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x36de109527a2c0c4

`0x36DE109527A2C0C4` · hash `0x36DE109527A2C0C4` · **Cliente**

```lua
N_0x36de109527a2c0c4(toggle)
```
```c
void 0x36DE109527A2C0C4(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing. It's a nullsub.

NativeDB Introduced: v1604
```

---
### N_0x3b458ddb57038f08

`0x3B458DDB57038F08` · hash `0x3B458DDB57038F08` · **Cliente**

```lua
N_0x3b458ddb57038f08(vehicle, doorIndex, toggle)
```
```c
void 0x3B458DDB57038F08(Vehicle vehicle, int doorIndex, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Usually used alongside other vehicle door natives.
```

---
### N_0x407dc5e97db1a4d3

`0x407DC5E97DB1A4D3` · hash `0x407DC5E97DB1A4D3` · **Cliente**

```lua
N_0x407dc5e97db1a4d3(p0, p1)
```
```c
void 0x407DC5E97DB1A4D3(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x41290b40fa63e6da

`0x41290B40FA63E6DA` · hash `0x41290B40FA63E6DA` · **Cliente**

```lua
N_0x41290b40fa63e6da(p0)
```
```c
void 0x41290B40FA63E6DA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x428ad3e26c8d9eb0

`0x428AD3E26C8D9EB0` · hash `0x428AD3E26C8D9EB0` · **Cliente**

```lua
N_0x428ad3e26c8d9eb0(vehicle, x, y, z, p4)
```
```c
void 0x428AD3E26C8D9EB0(Vehicle vehicle, float x, float y, float z, float p4);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_*
```

---
### N_0x430a7631a84c9be7

`0x430A7631A84C9BE7` · hash `0x430A7631A84C9BE7` · **Cliente**

```lua
N_0x430a7631a84c9be7(p0)
```
```c
void 0x430A7631A84C9BE7(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x4419966c9936071a

`0x4419966C9936071A` · hash `0x4419966C9936071A` · **Cliente**

```lua
N_0x4419966c9936071a(vehicle)
```
```c
void 0x4419966C9936071A(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
CLEAR_VEHICLE_*
```

---
### N_0x4ad280eb48b2d8e6

`0x4AD280EB48B2D8E6` · hash `0x4AD280EB48B2D8E6` · **Cliente**

```lua
N_0x4ad280eb48b2d8e6(vehicle, togle)
```
```c
void 0x4AD280EB48B2D8E6(Vehicle vehicle, BOOL togle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `togle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x4d9d109f63fee1d4

`0x4D9D109F63FEE1D4` · hash `0x4D9D109F63FEE1D4` · jhash `0x900C878C` · **Cliente**

```lua
N_0x4d9d109f63fee1d4(p0, p1)
```
```c
void 0x4D9D109F63FEE1D4(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x51db102f4a3ba5e0

`0x51DB102F4A3BA5E0` · hash `0x51DB102F4A3BA5E0` · jhash `0x0B0523B0` · **Cliente**

```lua
N_0x51db102f4a3ba5e0(toggle)
```
```c
void 0x51DB102F4A3BA5E0(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x51f30db60626a20e

`0x51F30DB60626A20E` · hash `0x51F30DB60626A20E` · **Cliente**

```lua
local retval = N_0x51f30db60626a20e(vehicle, x, y, z, rotX, rotY, rotZ, p7, p8)
```
```c
BOOL 0x51F30DB60626A20E(Vehicle vehicle, float x, float y, float z, float rotX, float rotY, float rotZ, int p7, Any p8);
```

**Parámetros**

- `vehicle` (`Vehicle`): the target vehicle
- `x` (`float`): vehicle location
- `y` (`float`): vehicle location
- `z` (`float`): vehicle location
- `rotX` (`float`): some kind of vehicle rotation value
- `rotY` (`float`): some kind of vehicle rotation value
- `rotZ` (`float`): some kind of vehicle rotation value
- `p7` (`int`): usually 2
- `p8` (`Any`): usually 1

**Devuelve:** `BOOL` — A BOOL value, purpose unknown.

**Descripción oficial:**

Usex in decompiled scripts in combination with [`_GET_VEHICLE_SUSPENSION_BOUNDS`](#getvehiclesuspensionbounds).

NativeDB Introduced: v1180

```
// Example from fm_bj_race_controller.c
if (!VEHICLE::_0x51F30DB60626A20E(uParam0->f_26, uParam0->f_12.f_3, uParam0->f_12, 2, 1) && !func_282(uParam0->f_6))
{
    VEHICLE::_GET_VEHICLE_SUSPENSION_BOUNDS(*uParam0, &vVar15, &uVar16);
    VEHICLE::_GET_VEHICLE_SUSPENSION_BOUNDS(uParam0->f_26, &vVar17, &uVar18);
    fVar19 = SYSTEM::VDIST2(0f, 0f, vVar15.z, 0f, 0f, vVar17.z);
    uParam0->f_12.f_3.f_2 = (uParam0->f_12.f_3.f_2 + fVar19);
    if (!VEHICLE::_0x51F30DB60626A20E(uParam0->f_26, uParam0->f_12.f_3, uParam0->f_12, 2, 1))
    {
        uParam0->f_12.f_3 = { uParam0->f_6 };
        uParam0->f_12 = { uParam0->f_9 };
    }
}
```

---
### N_0x56eb5e94318d3fb6

`0x56EB5E94318D3FB6` · hash `0x56EB5E94318D3FB6` · jhash `0x30F43FE3` · **Cliente**

```lua
N_0x56eb5e94318d3fb6(vehicle, p1)
```
```c
void 0x56EB5E94318D3FB6(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x5845066d8a1ea7f7

`0x5845066D8A1EA7F7` · hash `0x5845066D8A1EA7F7` · jhash `0x943A58EB` · **Cliente**

```lua
N_0x5845066d8a1ea7f7(vehicle, x, y, z, p4)
```
```c
void 0x5845066D8A1EA7F7(Vehicle vehicle, float x, float y, float z, Any p4);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p4` (`Any`)

**Devuelve:** `void`

---
### N_0x59c3757b3b7408e8

`0x59C3757B3B7408E8` · hash `0x59C3757B3B7408E8` · **Cliente**

```lua
N_0x59c3757b3b7408e8(vehicle, toggle, p2)
```
```c
void 0x59C3757B3B7408E8(Vehicle vehicle, BOOL toggle, float p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)
- `p2` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x5ba68a0840d546ac

`0x5BA68A0840D546AC` · hash `0x5BA68A0840D546AC` · **Cliente**

```lua
local retval = N_0x5ba68a0840d546ac(p0, p1)
```
```c
Any 0x5BA68A0840D546AC(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0x5bbcf35bf6e456f7

`0x5BBCF35BF6E456F7` · hash `0x5BBCF35BF6E456F7` · **Cliente**

```lua
N_0x5bbcf35bf6e456f7(toggle)
```
```c
void 0x5BBCF35BF6E456F7(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x5e569ec46ec21cae

`0x5E569EC46EC21CAE` · hash `0x5E569EC46EC21CAE` · jhash `0xBC649C49` · **Cliente**

```lua
N_0x5e569ec46ec21cae(vehicle, toggle)
```
```c
void 0x5E569EC46EC21CAE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x5ee5632f47ae9695

`0x5EE5632F47AE9695` · hash `0x5EE5632F47AE9695` · **Cliente**

```lua
N_0x5ee5632f47ae9695(vehicle, health)
```
```c
void 0x5EE5632F47AE9695(Vehicle vehicle, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `health` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets some health value. Looks like it's used for helis.
```

---
### N_0x6501129c9e0ffa05

`0x6501129C9E0FFA05` · hash `0x6501129C9E0FFA05` · **Cliente**

```lua
N_0x6501129c9e0ffa05(p0, p1)
```
```c
void 0x6501129C9E0FFA05(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x65b080555ea48149

`0x65B080555EA48149` · hash `0x65B080555EA48149` · **Cliente**

```lua
N_0x65b080555ea48149(p0)
```
```c
void 0x65B080555EA48149(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x66e3aaface2d1eb8

`0x66E3AAFACE2D1EB8` · hash `0x66E3AAFACE2D1EB8` · **Cliente**

```lua
N_0x66e3aaface2d1eb8(p0, p1, p2)
```
```c
void 0x66E3AAFACE2D1EB8(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0x6a973569ba094650

`0x6A973569BA094650` · hash `0x6A973569BA094650` · **Cliente**

```lua
N_0x6a973569ba094650(vehicle, p1)
```
```c
void 0x6A973569BA094650(Vehicle vehicle, Any p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x6eaaefc76acc311f

`0x6EAAEFC76ACC311F` · hash `0x6EAAEFC76ACC311F` · **Cliente**

```lua
local retval = N_0x6eaaefc76acc311f(p0)
```
```c
Any 0x6EAAEFC76ACC311F(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x6ebfb22d646ffc18

`0x6EBFB22D646FFC18` · hash `0x6EBFB22D646FFC18` · jhash `0x847F1304` · **Cliente**

```lua
N_0x6ebfb22d646ffc18(vehicle, p1)
```
```c
void 0x6EBFB22D646FFC18(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x725012a415dba050

`0x725012A415DBA050` · hash `0x725012A415DBA050` · **Cliente**

```lua
local retval, p1 = N_0x725012a415dba050(p0, p2)
```
```c
Any 0x725012A415DBA050(Any p0, Any* p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

Last named native above this one is `TRACK_VEHICLE_VISIBILITY` and first named native below is `UNCUFF_PED`.
Unknown what it does, couldn't find good examples in the decompiled scripts.

---
### N_0x72beccf4b829522e

`0x72BECCF4B829522E` · hash `0x72BECCF4B829522E` · **Cliente**

```lua
N_0x72beccf4b829522e(p0, p1)
```
```c
void 0x72BECCF4B829522E(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x73561d4425a021a2

`0x73561D4425A021A2` · hash `0x73561D4425A021A2` · **Cliente**

```lua
N_0x73561d4425a021a2(p0, p1)
```
```c
void 0x73561D4425A021A2(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x737e398138550fff

`0x737E398138550FFF` · hash `0x737E398138550FFF` · **Cliente**

```lua
N_0x737e398138550fff(vehicle, toggle)
```
```c
void 0x737E398138550FFF(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x76d26a22750e849e

`0x76D26A22750E849E` · hash `0x76D26A22750E849E` · **Cliente**

```lua
N_0x76d26a22750e849e(vehicle)
```
```c
void 0x76D26A22750E849E(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VEHICLE_*
```

---
### N_0x78ceee41f49f421f

`0x78CEEE41F49F421F` · hash `0x78CEEE41F49F421F` · **Cliente**

```lua
N_0x78ceee41f49f421f(p0, p1)
```
```c
void 0x78CEEE41F49F421F(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x796a877e459b99ea

`0x796A877E459B99EA` · hash `0x796A877E459B99EA` · jhash `0x5C9F477C` · **Cliente**

```lua
N_0x796a877e459b99ea(p0, p1, p2, p3)
```
```c
void 0x796A877E459B99EA(Any p0, float p1, float p2, float p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### N_0x7bbe7ff626a591fe

`0x7BBE7FF626A591FE` · hash `0x7BBE7FF626A591FE` · **Cliente**

```lua
N_0x7bbe7ff626a591fe(p0)
```
```c
void 0x7BBE7FF626A591FE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x80e3357fdef45c21

`0x80E3357FDEF45C21` · hash `0x80E3357FDEF45C21` · **Cliente**

```lua
N_0x80e3357fdef45c21(vehicle, toggle)
```
```c
void 0x80E3357FDEF45C21(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x8235f1bead557629

`0x8235F1BEAD557629` · hash `0x8235F1BEAD557629` · **Cliente**

```lua
N_0x8235f1bead557629(vehicle, toggle)
```
```c
void 0x8235F1BEAD557629(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x82e0ac411e41a5b4

`0x82E0AC411E41A5B4` · hash `0x82E0AC411E41A5B4` · **Cliente**

```lua
N_0x82e0ac411e41a5b4(toggle)
```
```c
void 0x82E0AC411E41A5B4(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing. It's a nullsub.

NativeDB Introduced: v1604
```

---
### N_0x8533cafde1f0f336

`0x8533CAFDE1F0F336` · hash `0x8533CAFDE1F0F336` · **Cliente**

```lua
local retval = N_0x8533cafde1f0f336(p0)
```
```c
Any 0x8533CAFDE1F0F336(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x8664170ef165c4a6

`0x8664170EF165C4A6` · hash `0x8664170EF165C4A6` · **Cliente**

```lua
N_0x8664170ef165c4a6(p0, p1)
```
```c
void 0x8664170EF165C4A6(Any p0, Any p1);
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
### N_0x870b8b7a766615c8

`0x870B8B7A766615C8` · hash `0x870B8B7A766615C8` · **Cliente**

```lua
N_0x870b8b7a766615c8(p0, p1, p2)
```
```c
void 0x870B8B7A766615C8(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0x8821196d91fa2de5

`0x8821196D91FA2DE5` · hash `0x8821196D91FA2DE5` · **Cliente**

```lua
N_0x8821196d91fa2de5(vehicle, toggle)
```
```c
void 0x8821196D91FA2DE5(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x887fa38787de8c72

`0x887FA38787DE8C72` · hash `0x887FA38787DE8C72` · **Cliente**

```lua
N_0x887fa38787de8c72(vehicle)
```
```c
void 0x887FA38787DE8C72(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

---
### N_0x88bc673ca9e0ae99

`0x88BC673CA9E0AE99` · hash `0x88BC673CA9E0AE99` · jhash `0xF0E5C41D` · **Cliente**

```lua
N_0x88bc673ca9e0ae99(vehicle, p1)
```
```c
void 0x88BC673CA9E0AE99(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x8f0d5ba1c2cc91d7

`0x8F0D5BA1C2CC91D7` · hash `0x8F0D5BA1C2CC91D7` · **Cliente**

```lua
N_0x8f0d5ba1c2cc91d7(toggle)
```
```c
void 0x8F0D5BA1C2CC91D7(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x9640e30a7f395e4b

`0x9640E30A7F395E4B` · hash `0x9640E30A7F395E4B` · **Cliente**

```lua
N_0x9640e30a7f395e4b(vehicle, p1, p2, p3, p4)
```
```c
void 0x9640E30A7F395E4B(Vehicle vehicle, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x97841634ef7df1d6

`0x97841634EF7DF1D6` · hash `0x97841634EF7DF1D6` · **Cliente**

```lua
N_0x97841634ef7df1d6(vehicle, toggle)
```
```c
void 0x97841634EF7DF1D6(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0x9849de24fcf23ccc

`0x9849DE24FCF23CCC` · hash `0x9849DE24FCF23CCC` · **Cliente**

```lua
N_0x9849de24fcf23ccc(vehicle, toggle)
```
```c
void 0x9849DE24FCF23CCC(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0x99a05839c46ce316

`0x99A05839C46CE316` · hash `0x99A05839C46CE316` · **Cliente**

```lua
N_0x99a05839c46ce316(toggle)
```
```c
void 0x99A05839C46CE316(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing. It's a nullsub.

NativeDB Introduced: v1604
```

---
### N_0x99cad8e7afdb60fa

`0x99CAD8E7AFDB60FA` · hash `0x99CAD8E7AFDB60FA` · jhash `0x1128A45B` · **Cliente**

```lua
N_0x99cad8e7afdb60fa(vehicle, p1, p2)
```
```c
void 0x99CAD8E7AFDB60FA(Vehicle vehicle, float p1, float p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)
- `p2` (`float`)

**Devuelve:** `void`

---
### N_0x9bddc73cc6a115d4

`0x9BDDC73CC6A115D4` · hash `0x9BDDC73CC6A115D4` · jhash `0x50CDB295` · **Cliente**

```lua
N_0x9bddc73cc6a115d4(vehicle, p1, p2)
```
```c
void 0x9BDDC73CC6A115D4(Vehicle vehicle, BOOL p1, BOOL p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### N_0x9becd4b9fef3f8a6

`0x9BECD4B9FEF3F8A6` · hash `0x9BECD4B9FEF3F8A6` · jhash `0xACAB8FF3` · **Cliente**

```lua
N_0x9becd4b9fef3f8a6(vehicle, p1)
```
```c
void 0x9BECD4B9FEF3F8A6(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x9d30687c57baa0bb

`0x9D30687C57BAA0BB` · hash `0x9D30687C57BAA0BB` · **Cliente**

```lua
N_0x9d30687c57baa0bb(p0)
```
```c
void 0x9D30687C57BAA0BB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x9f3f689b814f2599

`0x9F3F689B814F2599` · hash `0x9F3F689B814F2599` · **Cliente**

```lua
N_0x9f3f689b814f2599(vehicle, p1)
```
```c
void 0x9F3F689B814F2599(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xa01bc64dd4bfbbac

`0xA01BC64DD4BFBBAC` · hash `0xA01BC64DD4BFBBAC` · jhash `0x5ED1EECC` · **Cliente**

```lua
local retval = N_0xa01bc64dd4bfbbac(vehicle, seatIndex)
```
```c
Hash 0xA01BC64DD4BFBBAC(Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `seatIndex` (`int`)

**Devuelve:** `Hash`

**Descripción oficial:**

Gets hash related to task happening with seat index
Native name: GET_I\*

---
### N_0xa247f9ef01d8082e

`0xA247F9EF01D8082E` · hash `0xA247F9EF01D8082E` · **Cliente**

```lua
N_0xa247f9ef01d8082e(p0)
```
```c
void 0xA247F9EF01D8082E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xa4822f1cf23f4810

`0xA4822F1CF23F4810` · hash `0xA4822F1CF23F4810` · jhash `0x34E02FCD` · **Cliente**

```lua
local retval, outVec, p1, outVec1 = N_0xa4822f1cf23f4810(p3, p4, p5, p6, p7, p8)
```
```c
BOOL 0xA4822F1CF23F4810(Vector3* outVec, Vector3* p1, Vector3* outVec1, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8);
```

**Parámetros**

- `outVec` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `outVec1` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)
- `p8` (`Any`)

**Devuelve:** `BOOL`

---
### N_0xa4a9a4c40e615885

`0xA4A9A4C40E615885` · hash `0xA4A9A4C40E615885` · **Cliente**

```lua
N_0xa4a9a4c40e615885(p0)
```
```c
void 0xA4A9A4C40E615885(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### N_0xa7dcdf4ded40a8f4

`0xA7DCDF4DED40A8F4` · hash `0xA7DCDF4DED40A8F4` · **Cliente**

```lua
N_0xa7dcdf4ded40a8f4(vehicle, p1)
```
```c
void 0xA7DCDF4DED40A8F4(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xaa653ae61924b0a0

`0xAA653AE61924B0A0` · hash `0xAA653AE61924B0A0` · **Cliente**

```lua
N_0xaa653ae61924b0a0(vehicle, toggle)
```
```c
void 0xAA653AE61924B0A0(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xab04325045427aae

`0xAB04325045427AAE` · hash `0xAB04325045427AAE` · jhash `0x1984F88D` · **Cliente**

```lua
N_0xab04325045427aae(vehicle, p1)
```
```c
void 0xAB04325045427AAE(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xab31ef4de6800ce9

`0xAB31EF4DE6800CE9` · hash `0xAB31EF4DE6800CE9` · **Cliente**

```lua
N_0xab31ef4de6800ce9(p0, p1)
```
```c
void 0xAB31EF4DE6800CE9(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xae3fee8709b39dcb

`0xAE3FEE8709B39DCB` · hash `0xAE3FEE8709B39DCB` · jhash `0xE39DAF36` · **Cliente**

```lua
local retval = N_0xae3fee8709b39dcb(vehicle)
```
```c
BOOL 0xAE3FEE8709B39DCB(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### N_0xaf60e6a2936f982a

`0xAF60E6A2936F982A` · hash `0xAF60E6A2936F982A` · **Cliente**

```lua
N_0xaf60e6a2936f982a(p0, p1)
```
```c
void 0xAF60E6A2936F982A(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xb2e0c0d6922d31f2

`0xB2E0C0D6922D31F2` · hash `0xB2E0C0D6922D31F2` · **Cliente**

```lua
N_0xb2e0c0d6922d31f2(vehicle, toggle)
```
```c
void 0xB2E0C0D6922D31F2(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_C*
```

---
### N_0xb68cfaf83a02768d

`0xB68CFAF83A02768D` · hash `0xB68CFAF83A02768D` · **Cliente**

```lua
N_0xb68cfaf83a02768d(vehicle, toggle)
```
```c
void 0xB68CFAF83A02768D(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xb9562064627ff9db

`0xB9562064627FF9DB` · hash `0xB9562064627FF9DB` · **Cliente**

```lua
N_0xb9562064627ff9db(p0, p1)
```
```c
void 0xB9562064627FF9DB(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xbb2333bb87ddd87f

`0xBB2333BB87DDD87F` · hash `0xBB2333BB87DDD87F` · **Cliente**

```lua
N_0xbb2333bb87ddd87f(p0, p1)
```
```c
void 0xBB2333BB87DDD87F(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xbe5c1255a1830ff5

`0xBE5C1255A1830FF5` · hash `0xBE5C1255A1830FF5` · jhash `0xA6D8D7A5` · **Cliente**

```lua
N_0xbe5c1255a1830ff5(vehicle, toggle)
```
```c
void 0xBE5C1255A1830FF5(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0xc0ed6438e6d39ba8

`0xC0ED6438E6D39BA8` · hash `0xC0ED6438E6D39BA8` · **Cliente**

```lua
N_0xc0ed6438e6d39ba8(p0, p1, p2)
```
```c
void 0xC0ED6438E6D39BA8(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0xc361aa040d6637a8

`0xC361AA040D6637A8` · hash `0xC361AA040D6637A8` · jhash `0x819CD954` · **Cliente**

```lua
N_0xc361aa040d6637a8(vehicle, p1)
```
```c
void 0xC361AA040D6637A8(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Vehicle must be a plane.
Native name is between SET_VEHICLE_BRAKE_LIGHTS and SET_VEHICLE_BULLDOZER_ARM_POSITION alphabetically.

---
### N_0xc4b3347bd68bd609

`0xC4B3347BD68BD609` · hash `0xC4B3347BD68BD609` · **Cliente**

```lua
N_0xc4b3347bd68bd609(p0)
```
```c
void 0xC4B3347BD68BD609(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xc50ce861b55eab8b

`0xC50CE861B55EAB8B` · hash `0xC50CE861B55EAB8B` · jhash `0x40C323AE` · **Cliente**

```lua
N_0xc50ce861b55eab8b(vehicle, p1)
```
```c
void 0xC50CE861B55EAB8B(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VEHICLE_LI*
```

---
### N_0xcf9159024555488c

`0xCF9159024555488C` · hash `0xCF9159024555488C` · **Cliente**

```lua
N_0xcf9159024555488c(p0)
```
```c
void 0xCF9159024555488C(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xcfd778e7904c255e

`0xCFD778E7904C255E` · hash `0xCFD778E7904C255E` · jhash `0x3FBE904F` · **Cliente**

```lua
N_0xcfd778e7904c255e(vehicle)
```
```c
void 0xCFD778E7904C255E(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
what does this do?  
```

---
### N_0xd3301660a57c9272

`0xD3301660A57C9272` · hash `0xD3301660A57C9272` · **Cliente**

```lua
N_0xd3301660a57c9272(p0)
```
```c
void 0xD3301660A57C9272(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xd3e51c0ab8c26eee

`0xD3E51C0AB8C26EEE` · hash `0xD3E51C0AB8C26EEE` · **Cliente**

```lua
local retval = N_0xd3e51c0ab8c26eee(p0, p1)
```
```c
Any 0xD3E51C0AB8C26EEE(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0xd4196117af7bb974

`0xD4196117AF7BB974` · hash `0xD4196117AF7BB974` · **Cliente**

```lua
local retval = N_0xd4196117af7bb974(p0, p1)
```
```c
Any 0xD4196117AF7BB974(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0xd565f438137f0e10

`0xD565F438137F0E10` · hash `0xD565F438137F0E10` · **Cliente**

```lua
N_0xd565f438137f0e10(p0, p1)
```
```c
void 0xD565F438137F0E10(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xdbc631f109350b8c

`0xDBC631F109350B8C` · hash `0xDBC631F109350B8C` · jhash `0x486C1280` · **Cliente**

```lua
N_0xdbc631f109350b8c(vehicle, p1)
```
```c
void 0xDBC631F109350B8C(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Related to locking the vehicle or something similar.  
In the decompiled scripts, its always called after  
VEHICLE::_SET_EXCLUSIVE_DRIVER(a_0, 0, 0);  
VEHICLE::SET_VEHICLE_DOORS_LOCKED_FOR_ALL_PLAYERS(a_0, 1);  
VEHICLE::SET_VEHICLE_DOORS_LOCKED_FOR_PLAYER(a_0, PLAYER::PLAYER_ID(), 0);  
```

---
### N_0xdce97bdf8a0eabc8

`0xDCE97BDF8A0EABC8` · hash `0xDCE97BDF8A0EABC8` · **Cliente**

```lua
N_0xdce97bdf8a0eabc8()
```
```c
void 0xDCE97BDF8A0EABC8();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 1: Vehicle vehicle
NativeDB Added Parameter 2: Any p1
```

---
### N_0xe05dd0e9707003a3

`0xE05DD0E9707003A3` · hash `0xE05DD0E9707003A3` · jhash `0x123E5B90` · **Cliente**

```lua
N_0xe05dd0e9707003a3(p0, p1)
```
```c
void 0xE05DD0E9707003A3(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xe2f53f172b45ede1

`0xE2F53F172B45EDE1` · hash `0xE2F53F172B45EDE1` · **Cliente**

```lua
N_0xe2f53f172b45ede1()
```
```c
void 0xE2F53F172B45EDE1();
```

**Devuelve:** `void`

**Descripción oficial:**

```
RESET_*

Resets the effect of 0x428AD3E26C8D9EB0
```

---
### N_0xe5810ac70602f2f5

`0xE5810AC70602F2F5` · hash `0xE5810AC70602F2F5` · jhash `0xB6BE07E0` · **Cliente**

```lua
N_0xe5810ac70602f2f5(vehicle, p1)
```
```c
void 0xE5810AC70602F2F5(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0xe851e480b814d4ba

`0xE851E480B814D4BA` · hash `0xE851E480B814D4BA` · jhash `0x2F98B4B7` · **Cliente**

```lua
N_0xe851e480b814d4ba(vehicle, p1)
```
```c
void 0xE851E480B814D4BA(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xe8718faf591fd224

`0xE8718FAF591FD224` · hash `0xE8718FAF591FD224` · **Cliente**

```lua
local retval = N_0xe8718faf591fd224(vehicle)
```
```c
BOOL 0xE8718FAF591FD224(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
GET_H*

NativeDB Introduced: v1604
```

---
### N_0xed5ede9e676643c9

`0xED5EDE9E676643C9` · hash `0xED5EDE9E676643C9` · **Cliente**

```lua
N_0xed5ede9e676643c9(p0, p1)
```
```c
void 0xED5EDE9E676643C9(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xef9d388f8d377f44

`0xEF9D388F8D377F44` · hash `0xEF9D388F8D377F44` · **Cliente**

```lua
N_0xef9d388f8d377f44(vehicle, p1)
```
```c
void 0xEF9D388F8D377F44(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only used in R* Script fm_content_cargo
```

```
NativeDB Introduced: v2699
```

---
### N_0xf051d9bfb6ba39c0

`0xF051D9BFB6BA39C0` · hash `0xF051D9BFB6BA39C0` · **Cliente**

```lua
N_0xf051d9bfb6ba39c0(p0)
```
```c
void 0xF051D9BFB6BA39C0(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xf25e02cb9c5818f8

`0xF25E02CB9C5818F8` · hash `0xF25E02CB9C5818F8` · jhash `0xF0E59BC1` · **Cliente**

```lua
N_0xf25e02cb9c5818f8()
```
```c
void 0xF25E02CB9C5818F8();
```

**Devuelve:** `void`

---
### N_0xf3b0e0aed097a3f5

`0xF3B0E0AED097A3F5` · hash `0xF3B0E0AED097A3F5` · **Cliente**

```lua
local retval = N_0xf3b0e0aed097a3f5(p0, p1)
```
```c
Any 0xF3B0E0AED097A3F5(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### N_0xf8b49f5ba7f850e7

`0xF8B49F5BA7F850E7` · hash `0xF8B49F5BA7F850E7` · **Cliente**

```lua
N_0xf8b49f5ba7f850e7(vehicle, p1)
```
```c
void 0xF8B49F5BA7F850E7(Vehicle vehicle, int p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0xfaf2a78061fd9ef4

`0xFAF2A78061FD9EF4` · hash `0xFAF2A78061FD9EF4` · jhash `0xCD83C393` · **Cliente**

```lua
N_0xfaf2a78061fd9ef4(p0, p1, p2, p3)
```
```c
void 0xFAF2A78061FD9EF4(Any p0, float p1, float p2, float p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### NetworkUseHighPrecisionVehicleBlending

`_NETWORK_USE_HIGH_PRECISION_VEHICLE_BLENDING` · hash `0xEC0C1D4922AF9754` · **Cliente**

```lua
NetworkUseHighPrecisionVehicleBlending(vehicle, toggle)
```
```c
void _NETWORK_USE_HIGH_PRECISION_VEHICLE_BLENDING(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Implemented only for Trains.
```

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xEC0C1D4922AF9754` (`N_0xec0c1d4922af9754`)

---
### OpenBombBayDoors

`OPEN_BOMB_BAY_DOORS` · hash `0x87E7F24270732CB1` · jhash `0x6574041D` · **Cliente**

```lua
OpenBombBayDoors(vehicle)
```
```c
void OPEN_BOMB_BAY_DOORS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_OPEN_VEHICLE_BOMB_BAY` (`OpenVehicleBombBay`)

---
### PausePlaybackRecordedVehicle

`PAUSE_PLAYBACK_RECORDED_VEHICLE` · hash `0x632A689BF42301B1` · jhash `0xCCF54912` · **Cliente**

```lua
PausePlaybackRecordedVehicle(vehicle)
```
```c
void PAUSE_PLAYBACK_RECORDED_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### PopOutVehicleWindscreen

`POP_OUT_VEHICLE_WINDSCREEN` · hash `0x6D645D59FB5F5AD3` · jhash `0xCC95C96B` · **Cliente**

```lua
PopOutVehicleWindscreen(vehicle)
```
```c
void POP_OUT_VEHICLE_WINDSCREEN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

Detaches the vehicle's windscreen.

**Nombres antiguos (alias):** `_DETACH_VEHICLE_WINDSCREEN` (`DetachVehicleWindscreen`)

---
### PreloadVehicleMod

`PRELOAD_VEHICLE_MOD` · hash `0x758F49C24925568A` · jhash `0x6EA5F4A8` · **Cliente**

```lua
PreloadVehicleMod(p0, modType, p2)
```
```c
void PRELOAD_VEHICLE_MOD(Any p0, int modType, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).
- `p2` (`Any`)

**Devuelve:** `void`

---
### RaiseConvertibleRoof

`RAISE_CONVERTIBLE_ROOF` · hash `0x8F5FB35D7E88FC70` · jhash `0xA4E4CBA3` · **Cliente**

```lua
RaiseConvertibleRoof(vehicle, instantlyRaise)
```
```c
void RAISE_CONVERTIBLE_ROOF(Vehicle vehicle, BOOL instantlyRaise);
```

**Parámetros**

- `vehicle` (`Vehicle`): The convertible vehicle whose roof you wish to raise.
- `instantlyRaise` (`BOOL`): A boolean indicating whether the roof should be raised instantly without the animation transition. Set `false` to raise the roof with the animation, or `true` to raise it immediately.

**Devuelve:** `void`

**Descripción oficial:**

Raises the roof on a convertible vehicle, utilizing any available animations for the action. This native is particularly useful for creating a realistic interaction with convertible vehicles by animating the process of raising the roof.

You can check if the vehicle has an convertible roof using [`IS_VEHICLE_A_CONVERTIBLE`](#isvehicleaconvertible).

To lower the convertible roof, you can use [`LOWER_CONVERTIBLE_ROOF`](#lowerconvertibleroof).

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if not IsVehicleAConvertible(vehicle, false) then return end
RaiseConvertibleRoof(vehicle, false)
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!IsVehicleAConvertible(vehicle, false)) return;
RaiseConvertibleRoof(vehicle, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!IsVehicleAConvertible(vehicle, false)) return;
RaiseConvertibleRoof(vehicle, false);
```

---
### RaiseRetractableWheels

`_RAISE_RETRACTABLE_WHEELS` · hash `0xF660602546D27BA8` · **Cliente**

```lua
RaiseRetractableWheels(vehicle)
```
```c
void _RAISE_RETRACTABLE_WHEELS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_RAISE_LOWERABLE_WHEELS` (`RaiseLowerableWheels`)

---
### ReleasePreloadMods

`RELEASE_PRELOAD_MODS` · hash `0x445D79F995508307` · jhash `0xD442521F` · **Cliente**

```lua
ReleasePreloadMods(vehicle)
```
```c
void RELEASE_PRELOAD_MODS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### RemovePickUpRopeForCargobob

`REMOVE_PICK_UP_ROPE_FOR_CARGOBOB` · hash `0x9768CF648F54C804` · jhash `0xA8211EE9` · **Cliente**

```lua
RemovePickUpRopeForCargobob(cargobob)
```
```c
void REMOVE_PICK_UP_ROPE_FOR_CARGOBOB(Vehicle cargobob);
```

**Parámetros**

- `cargobob` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
Retracts the hook on the cargobob.  
Note: after you retract it the natives for dropping the hook no longer work  
```

**Nombres antiguos (alias):** `_RETRACT_CARGOBOB_HOOK` (`RetractCargobobHook`)

---
### RemoveRoadNodeSpeedZone

`REMOVE_ROAD_NODE_SPEED_ZONE` · hash `0x1033371FC8E842A7` · jhash `0x0C0332A6` · **Cliente**

```lua
local retval = RemoveRoadNodeSpeedZone(speedzone)
```
```c
BOOL REMOVE_ROAD_NODE_SPEED_ZONE(int speedzone);
```

**Parámetros**

- `speedzone` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1033371FC8E842A7` (`N_0x1033371fc8e842a7`), `_REMOVE_SPEED_ZONE` (`RemoveSpeedZone`)

---
### RemoveVehicleAsset

`REMOVE_VEHICLE_ASSET` · hash `0xACE699C71AB9DEB5` · jhash `0x9620E9C6` · **Cliente**

```lua
RemoveVehicleAsset(vehicleAsset)
```
```c
void REMOVE_VEHICLE_ASSET(int vehicleAsset);
```

**Parámetros**

- `vehicleAsset` (`int`)

**Devuelve:** `void`

---
### RemoveVehicleCombatAvoidanceArea

`REMOVE_VEHICLE_COMBAT_AVOIDANCE_AREA` · hash `0xE30524E1871F481D` · jhash `0xEF05F807` · **Cliente**

```lua
RemoveVehicleCombatAvoidanceArea(p0)
```
```c
void REMOVE_VEHICLE_COMBAT_AVOIDANCE_AREA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE30524E1871F481D` (`N_0xe30524e1871f481d`)

---
### RemoveVehicleHighDetailModel

`REMOVE_VEHICLE_HIGH_DETAIL_MODEL` · hash `0x00689CDE5F7C6787` · jhash `0x382BE070` · **Cliente**

```lua
RemoveVehicleHighDetailModel(vehicle)
```
```c
void REMOVE_VEHICLE_HIGH_DETAIL_MODEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### RemoveVehicleMod

`REMOVE_VEHICLE_MOD` · hash `0x92D619E420858204` · jhash `0x9CC80A43` · **Cliente**

```lua
RemoveVehicleMod(vehicle, modType)
```
```c
void REMOVE_VEHICLE_MOD(Vehicle vehicle, int modType);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `modType` (`int`): Refer to eVehicleModType in [`SET_VEHICLE_MOD`](VEHICLE-2.md#setvehiclemod).

**Devuelve:** `void`

---
### RemoveVehicleRecording

`REMOVE_VEHICLE_RECORDING` · hash `0xF1160ACCF98A3FC8` · jhash `0xD3C05B00` · **Cliente**

```lua
RemoveVehicleRecording(recording, script)
```
```c
void REMOVE_VEHICLE_RECORDING(int recording, char* script);
```

**Parámetros**

- `recording` (`int`)
- `script` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

See [REQUEST_VEHICLE_RECORDING](#requestvehiclerecording)

---
### RemoveVehicleShadowEffect

`_REMOVE_VEHICLE_SHADOW_EFFECT` · hash `0xF87D9F2301F7D206` · jhash `0x450AD03A` · **Cliente**

```lua
RemoveVehicleShadowEffect(vehicle)
```
```c
void _REMOVE_VEHICLE_SHADOW_EFFECT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

Remove the weird shadow applied by [\_SET_VEHICLE_SHADOW_EFFECT](OBJECT.md#ispointinangledarea)

**Nombres antiguos (alias):** `0xF87D9F2301F7D206` (`N_0xf87d9f2301f7d206`)

---
### RemoveVehicleStuckCheck

`REMOVE_VEHICLE_STUCK_CHECK` · hash `0x8386BFB614D06749` · jhash `0x81594917` · **Cliente**

```lua
RemoveVehicleStuckCheck(vehicle)
```
```c
void REMOVE_VEHICLE_STUCK_CHECK(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### RemoveVehicleUpsidedownCheck

`REMOVE_VEHICLE_UPSIDEDOWN_CHECK` · hash `0xC53EB42A499A7E90` · jhash `0xF390BA1B` · **Cliente**

```lua
RemoveVehicleUpsidedownCheck(vehicle)
```
```c
void REMOVE_VEHICLE_UPSIDEDOWN_CHECK(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### RemoveVehicleWindow

`REMOVE_VEHICLE_WINDOW` · hash `0xA711568EEDB43069` · jhash `0xBB8104A3` · **Cliente**

```lua
RemoveVehicleWindow(vehicle, windowIndex)
```
```c
void REMOVE_VEHICLE_WINDOW(Vehicle vehicle, int windowIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `windowIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

See eWindowId declared in [`IS_VEHICLE_WINDOW_INTACT`](../cfx/servidor.md#isvehiclewindowintact).

---
### RemoveVehiclesFromGeneratorsInArea

`REMOVE_VEHICLES_FROM_GENERATORS_IN_AREA` · hash `0x46A1E1A299EC4BBA` · jhash `0x42CC15E0` · **Cliente**

```lua
RemoveVehiclesFromGeneratorsInArea(x1, y1, z1, x2, y2, z2, unk)
```
```c
void REMOVE_VEHICLES_FROM_GENERATORS_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2, Any unk);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `unk` (`Any`)

**Devuelve:** `void`

---
### RequestVehicleAsset

`REQUEST_VEHICLE_ASSET` · hash `0x81A15811460FAB3A` · jhash `0x902B4F06` · **Cliente**

```lua
RequestVehicleAsset(vehicleHash, vehicleAsset)
```
```c
void REQUEST_VEHICLE_ASSET(Hash vehicleHash, int vehicleAsset);
```

**Parámetros**

- `vehicleHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `vehicleAsset` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
REQUEST_VEHICLE_ASSET(GET_HASH_KEY(cargobob3), 3);  
vehicle found that have asset's:  
cargobob3  
submersible  
blazer  
```

---
### RequestVehicleDashboardScaleformMovie

`_REQUEST_VEHICLE_DASHBOARD_SCALEFORM_MOVIE` · hash `0xDBA3C090E3D74690` · **Cliente**

```lua
RequestVehicleDashboardScaleformMovie(vehicle)
```
```c
void _REQUEST_VEHICLE_DASHBOARD_SCALEFORM_MOVIE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
REQUEST_VEHICLE_*  
```

**Nombres antiguos (alias):** `0xDBA3C090E3D74690` (`N_0xdba3c090e3d74690`)

---
### RequestVehicleHighDetailModel

`REQUEST_VEHICLE_HIGH_DETAIL_MODEL` · hash `0xA6E9FDCB2C76785E` · jhash `0x9DA21956` · **Cliente**

```lua
RequestVehicleHighDetailModel(vehicle)
```
```c
void REQUEST_VEHICLE_HIGH_DETAIL_MODEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### RequestVehicleRecording

`REQUEST_VEHICLE_RECORDING` · hash `0xAF514CABE74CBF15` · jhash `0x91AFEFD9` · **Cliente**

```lua
RequestVehicleRecording(recording, script)
```
```c
void REQUEST_VEHICLE_RECORDING(int recording, char* script);
```

**Parámetros**

- `recording` (`int`)
- `script` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Request the vehicle recording defined by the lowercase format string "%s%03d.yvr". For example, REQUEST_VEHICLE_RECORDING(1, "FBIs1UBER") corresponds to fbis1uber001.yvr.
For all vehicle recording/playback natives, "script" is a common prefix that usually corresponds to the script/mission the recording is used in, "recording" is its int suffix, and "id" (e.g., in native GET_TOTAL_DURATION_OF_VEHICLE_RECORDING_ID) corresponds to a unique identifier within the recording streaming module.
Note that only 24 recordings (hardcoded in multiple places) can ever active at a given time before clobbering begins.
```

---
### ResetVehicleStuckTimer

`RESET_VEHICLE_STUCK_TIMER` · hash `0xD7591B0065AFAA7A` · jhash `0xEF2A6016` · **Cliente**

```lua
ResetVehicleStuckTimer(vehicle, nullAttributes)
```
```c
void RESET_VEHICLE_STUCK_TIMER(Vehicle vehicle, int nullAttributes);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `nullAttributes` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
The inner function has a switch on the second parameter. It's the stuck timer index.  
Here's some pseudo code I wrote for the inner function:  
void __fastcall NATIVE_RESET_VEHICLE_STUCK_TIMER_INNER(CUnknown* unknownClassInVehicle, int timerIndex)  
{  
	switch (timerIndex)  
	{  
	case 0:  
unknownClassInVehicle->FirstStuckTimer = (WORD)0u;  
	case 1:  
unknownClassInVehicle->SecondStuckTimer = (WORD)0u;  
	case 2:  
unknownClassInVehicle->ThirdStuckTimer = (WORD)0u;  
	case 3:  
unknownClassInVehicle->FourthStuckTimer = (WORD)0u;  
	case 4:  
unknownClassInVehicle->FirstStuckTimer = (WORD)0u;  
unknownClassInVehicle->SecondStuckTimer = (WORD)0u;  
unknownClassInVehicle->ThirdStuckTimer = (WORD)0u;  
unknownClassInVehicle->FourthStuckTimer = (WORD)0u;  
break;  
	};  
}  
```

---
### ResetVehicleWheels

`RESET_VEHICLE_WHEELS` · hash `0x21D2E5662C1F6FED` · jhash `0xD5FFE779` · **Cliente**

```lua
ResetVehicleWheels(vehicle, toggle)
```
```c
void RESET_VEHICLE_WHEELS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### RollDownWindow

`ROLL_DOWN_WINDOW` · hash `0x7AD9E6CE657D69E3` · jhash `0xF840134C` · **Cliente**

```lua
RollDownWindow(vehicle, windowIndex)
```
```c
void ROLL_DOWN_WINDOW(Vehicle vehicle, int windowIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `windowIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

See eWindowId declared in [`IS_VEHICLE_WINDOW_INTACT`](../cfx/servidor.md#isvehiclewindowintact).

---
### RollDownWindows

`ROLL_DOWN_WINDOWS` · hash `0x85796B0549DDE156` · jhash `0x51A16DC6` · **Cliente**

```lua
RollDownWindows(vehicle)
```
```c
void ROLL_DOWN_WINDOWS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
Roll down all the windows of the vehicle passed through the first parameter.  
```

---
### RollUpWindow

`ROLL_UP_WINDOW` · hash `0x602E548F46E24D59` · jhash `0x83B7E06A` · **Cliente**

```lua
RollUpWindow(vehicle, windowIndex)
```
```c
void ROLL_UP_WINDOW(Vehicle vehicle, int windowIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `windowIndex` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

See eWindowId declared in [`IS_VEHICLE_WINDOW_INTACT`](../cfx/servidor.md#isvehiclewindowintact).

---
### SetAllLowPriorityVehicleGeneratorsActive

`SET_ALL_LOW_PRIORITY_VEHICLE_GENERATORS_ACTIVE` · hash `0x608207E7A8FB787C` · jhash `0x87F767F2` · **Cliente**

```lua
SetAllLowPriorityVehicleGeneratorsActive(active)
```
```c
void SET_ALL_LOW_PRIORITY_VEHICLE_GENERATORS_ACTIVE(BOOL active);
```

**Parámetros**

- `active` (`BOOL`)

**Devuelve:** `void`

---
### SetAllVehicleGeneratorsActive

`SET_ALL_VEHICLE_GENERATORS_ACTIVE` · hash `0x34AD89078831A4BC` · jhash `0xAB1FDD76` · **Cliente**

```lua
SetAllVehicleGeneratorsActive()
```
```c
void SET_ALL_VEHICLE_GENERATORS_ACTIVE();
```

**Devuelve:** `void`

---
### SetAllVehicleGeneratorsActiveInArea

`SET_ALL_VEHICLE_GENERATORS_ACTIVE_IN_AREA` · hash `0xC12321827687FE4D` · jhash `0xB4E0E69A` · **Cliente**

```lua
SetAllVehicleGeneratorsActiveInArea(x1, y1, z1, x2, y2, z2, p6, p7)
```
```c
void SET_ALL_VEHICLE_GENERATORS_ACTIVE_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2, BOOL p6, BOOL p7);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `void`

---
### SetAmbientVehicleRangeMultiplierThisFrame

`SET_AMBIENT_VEHICLE_RANGE_MULTIPLIER_THIS_FRAME` · hash `0x90B6DA738A9A25DA` · jhash `0xDAE2A2BE` · **Cliente**

```lua
SetAmbientVehicleRangeMultiplierThisFrame(range)
```
```c
void SET_AMBIENT_VEHICLE_RANGE_MULTIPLIER_THIS_FRAME(float range);
```

**Parámetros**

- `range` (`float`): Most likely a value between 0.0 and 1.0.

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x90B6DA738A9A25DA` (`N_0x90b6da738a9a25da`), `_SET_SOME_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME` (`SetSomeVehicleDensityMultiplierThisFrame`)

---
### SetBikeOnStand

`SET_BIKE_ON_STAND` · hash `0x9CFA4896C3A53CBB` · jhash `0x15D40761` · **Cliente**

```lua
SetBikeOnStand(vehicle, x, y)
```
```c
void SET_BIKE_ON_STAND(Vehicle vehicle, float x, float y);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Only works on bikes, both X and Y work in the -1 - 1 range.
X forces the bike to turn left or right (-1, 1)
Y forces the bike to lean to the left or to the right (-1, 1)

Example with X -1/Y 1:

![](https://i.imgur.com/91sAMD5.png)

**Nombres antiguos (alias):** `_SET_BIKE_LEAN_ANGLE` (`SetBikeLeanAngle`)

---
### SetBoatAnchor

`SET_BOAT_ANCHOR` · hash `0x75DBEC174AEEAD10` · jhash `0xA3906284` · **Cliente**

```lua
SetBoatAnchor(boat, toggle)
```
```c
void SET_BOAT_ANCHOR(Vehicle boat, BOOL toggle);
```

**Parámetros**

- `boat` (`Vehicle`): The target boat.
- `toggle` (`BOOL`): Set the anchor state `true` deploys the anchor, false `raises` it.

**Devuelve:** `void`

**Descripción oficial:**

Sets the anchor state for a boat.

```
NativeDB Introduced: v323
```

**Note**: You might want to check if you can use your anchor before with [CAN_ANCHOR_BOAT_HERE](#cananchorboathere).

**Ejemplo (lua):**

```lua
local boat = GetVehiclePedIsIn(PlayerPedId(), false)
if not boat or not IsThisModelABoat(GetEntityModel(boat)) then return end

-- Check if we can anchor the boat here
if CanAnchorBoatHere(boat) then
    -- Deploy the boat's anchor
    SetBoatAnchor(boat, true)
    
    -- Wait for 10 seconds
    Wait(10000)
    
    -- Raise the boat's anchor
    SetBoatAnchor(boat, false)
else
    print("Cannot anchor the boat at this location")
end
```

**Ejemplo (js):**

```js
const boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (!boat || !IsThisModelABoat(GetEntityModel(boat))) return;

// Check if we can anchor the boat here
if (CanAnchorBoatHere(boat)) {
    // Deploy the boat's anchor
    SetBoatAnchor(boat, true);

    // Wait for 10 seconds
    await new Promise(resolve => setTimeout(resolve, 10000));

    // Raise the boat's anchor
    SetBoatAnchor(boat, false);
} else {
    console.log("Cannot anchor the boat at this location");
}
```

**Ejemplo (cs):**

```cs
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

int boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (boat == 0 || !IsThisModelABoat(GetEntityModel(boat))) return;

// Check if we can anchor the boat here
if (CanAnchorBoatHere(boat))
{
    // Deploy the boat's anchor
    SetBoatAnchor(boat, true);

    // Wait for 10 seconds
    await BaseScript.Delay(10000);

    // Raise the boat's anchor
    SetBoatAnchor(boat, false);
}
else
{
    Debug.WriteLine("Cannot anchor the boat at this location");
}
```

---
### SetBoatBoomPositionRatio

`_SET_BOAT_BOOM_POSITION_RATIO` · hash `0xF488C566413B4232` · jhash `0xA25CCB8C` · **Cliente**

```lua
SetBoatBoomPositionRatio(vehicle, ratio)
```
```c
void _SET_BOAT_BOOM_POSITION_RATIO(Vehicle vehicle, float ratio);
```

**Parámetros**

- `vehicle` (`Vehicle`): The TR3 vehicle.
- `ratio` (`float`): A value between 0.0 (left) and 1.0 (back)

**Devuelve:** `void`

**Descripción oficial:**

Sets the boat boom position for the `TR3` trailer.

Ratio value is between `0.0` and `1.0`, where `0.0` is 90 degrees to the left of the boat, and `1.0` is just slightly to the right/back of the boat.

To get the current boom position ratio, use [GET_BOAT_BOOM_POSITION_RATIO](#getboatboompositionratio).

**Nombres antiguos (alias):** `0xF488C566413B4232` (`N_0xf488c566413b4232`)

---
### SetBoatDisableAvoidance

`SET_BOAT_DISABLE_AVOIDANCE` · hash `0x0A6A279F3AA4FD70` · jhash `0x4C0E4031` · **Cliente**

```lua
SetBoatDisableAvoidance(vehicle, p1)
```
```c
void SET_BOAT_DISABLE_AVOIDANCE(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0A6A279F3AA4FD70` (`N_0x0a6a279f3aa4fd70`)

---
### SetBoatIsSinking

`_SET_BOAT_IS_SINKING` · hash `0xBD32E46AA95C1DD2` · **Cliente**

```lua
SetBoatIsSinking(vehicle)
```
```c
void _SET_BOAT_IS_SINKING(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBD32E46AA95C1DD2` (`N_0xbd32e46aa95c1dd2`), `_SET_BOAT_SINKING` (`SetBoatSinking`)

---
### SetBoatLowLodAnchorDistance

`SET_BOAT_LOW_LOD_ANCHOR_DISTANCE` · hash `0xE842A9398079BD82` · jhash `0x66FA450C` · **Cliente**

```lua
SetBoatLowLodAnchorDistance(boat, value)
```
```c
void SET_BOAT_LOW_LOD_ANCHOR_DISTANCE(Vehicle boat, float value);
```

**Parámetros**

- `boat` (`Vehicle`): The target boat.
- `value` (`float`): The distance at which the LOD switch occurs. Set to `-1.0` to reset the LOD distance to the default value.

**Devuelve:** `void`

**Descripción oficial:**

Sets the distance from the player at which anchored boats switch between high and low LOD (Level of Detail) buoyancy mode.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xE842A9398079BD82` (`N_0xe842a9398079bd82`), `_SET_BOAT_ANCHOR_BUOYANCY_COEFFICIENT` (`SetBoatAnchorBuoyancyCoefficient`), `_SET_BOAT_MOVEMENT_RESISTANCE` (`SetBoatMovementResistance`)

**Ejemplo (lua):**

```lua
local boat = GetVehiclePedIsIn(PlayerPedId(), false)
if not boat or not IsThisModelABoat(GetEntityModel(boat)) then return end

-- Set the low LOD anchor distance to 100 units
SetBoatLowLodAnchorDistance(boat, 100.0)
print("Set low LOD anchor distance to 100 units")
```

**Ejemplo (js):**

```js
const boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (!boat || !IsThisModelABoat(GetEntityModel(boat))) return;

// Set the low LOD anchor distance to 100 units
SetBoatLowLodAnchorDistance(boat, 100.0);
console.log("Set low LOD anchor distance to 100 units");
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (boat == 0 || !IsThisModelABoat(GetEntityModel(boat))) return;

// Set the low LOD anchor distance to 100 units
SetBoatLowLodAnchorDistance(boat, 100.0f);
Debug.WriteLine("Set low LOD anchor distance to 100 units");
```

---
### SetBoatRemainsAnchoredWhilePlayerIsDriver

`SET_BOAT_REMAINS_ANCHORED_WHILE_PLAYER_IS_DRIVER` · hash `0xE3EBAAE484798530` · jhash `0x0ED84792` · **Cliente**

```lua
SetBoatRemainsAnchoredWhilePlayerIsDriver(boat, toggle)
```
```c
void SET_BOAT_REMAINS_ANCHORED_WHILE_PLAYER_IS_DRIVER(Vehicle boat, BOOL toggle);
```

**Parámetros**

- `boat` (`Vehicle`): The target boat.
- `toggle` (`BOOL`): Set the anchoring behavior. If `true`, the boat will remain anchored even when a player is driving. If `false`, normal anchoring behavior applies (anchor is raised when a player drives).

**Devuelve:** `void`

**Descripción oficial:**

Sets whether a boat should remain anchored even when a player is driving it.

**Note**: This native is always used with [SET_BOAT_ANCHOR](#setboatanchor).

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xE3EBAAE484798530` (`N_0xe3ebaae484798530`), `_SET_BOAT_FROZEN_WHEN_ANCHORED` (`SetBoatFrozenWhenAnchored`)

**Ejemplo (lua):**

```lua
local boat = GetVehiclePedIsIn(PlayerPedId(), false)
if not boat or not IsThisModelABoat(GetEntityModel(boat)) then return end

SetBoatRemainsAnchoredWhilePlayerIsDriver(boat, true)
SetBoatAnchor(boat, true)
```

**Ejemplo (js):**

```js
const boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (!boat || !IsThisModelABoat(GetEntityModel(boat))) return;

SetBoatRemainsAnchoredWhilePlayerIsDriver(boat, true);
SetBoatAnchor(boat, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int boat = GetVehiclePedIsIn(PlayerPedId(), false);
if (boat == 0 || !IsThisModelABoat(GetEntityModel(boat))) return;

SetBoatRemainsAnchoredWhilePlayerIsDriver(boat, true);
SetBoatAnchor(boat, true);
```

---
### SetBoatSinksWhenWrecked

`SET_BOAT_SINKS_WHEN_WRECKED` · hash `0x8F719973E1445BA2` · jhash `0x35614622` · **Cliente**

```lua
SetBoatSinksWhenWrecked(vehicle, toggle)
```
```c
void SET_BOAT_SINKS_WHEN_WRECKED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8F719973E1445BA2` (`N_0x8f719973e1445ba2`), `_SET_BOAT_EXPLODES_ON_WRECKED_ACTION` (`SetBoatExplodesOnWreckedAction`)

---
### SetCamberedWheelsDisabled

`_SET_CAMBERED_WHEELS_DISABLED` · hash `0x1201E8A3290A3B98` · **Cliente**

```lua
SetCamberedWheelsDisabled(vehicle, toggle)
```
```c
void _SET_CAMBERED_WHEELS_DISABLED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1201E8A3290A3B98` (`N_0x1201e8a3290a3b98`)

---
### SetCanResprayVehicle

`SET_CAN_RESPRAY_VEHICLE` · hash `0x52BBA29D5EC69356` · jhash `0x37677590` · **Cliente**

```lua
SetCanResprayVehicle(vehicle, state)
```
```c
void SET_CAN_RESPRAY_VEHICLE(Vehicle vehicle, BOOL state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Hardcoded to not work in multiplayer.  
```

---
### SetCarBootOpen

`SET_CAR_BOOT_OPEN` · hash `0xFC40CBF7B90CA77C` · **Cliente**

```lua
SetCarBootOpen(vehicle)
```
```c
void SET_CAR_BOOT_OPEN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFC40CBF7B90CA77C` (`N_0xfc40cbf7b90ca77c`)

---
### SetCarHighSpeedBumpSeverityMultiplier

`_SET_CAR_HIGH_SPEED_BUMP_SEVERITY_MULTIPLIER` · hash `0x84FD40F56075E816` · **Cliente**

```lua
SetCarHighSpeedBumpSeverityMultiplier(multiplier)
```
```c
void _SET_CAR_HIGH_SPEED_BUMP_SEVERITY_MULTIPLIER(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Something to do with "high speed bump severity"?  
if (!sub_87a46("SET_CAR_HIGH_SPEED_BUMP_SEVERITY_MULTIPLIER")) {  
    VEHICLE::_84FD40F56075E816(0.0);  
    sub_8795b("SET_CAR_HIGH_SPEED_BUMP_SEVERITY_MULTIPLIER", 1);  
}  
```

**Nombres antiguos (alias):** `0x84FD40F56075E816` (`N_0x84fd40f56075e816`)

---
### SetCargobobExcludeFromPickupEntity

`SET_CARGOBOB_EXCLUDE_FROM_PICKUP_ENTITY` · hash `0x1F34B0626C594380` · **Cliente**

```lua
SetCargobobExcludeFromPickupEntity(cargobob, entity)
```
```c
void SET_CARGOBOB_EXCLUDE_FROM_PICKUP_ENTITY(Vehicle cargobob, Entity entity);
```

**Parámetros**

- `cargobob` (`Vehicle`): The Cargobob helicopter from which the entity is not to be detached
- `entity` (`Entity`): The entity to remain attached to the Cargobob.

**Devuelve:** `void`

**Descripción oficial:**

Prevents a specified entity from being detached from a Cargobob, even in the event of collisions.

**Nombres antiguos (alias):** `0x1F34B0626C594380` (`N_0x1f34b0626c594380`)

**Ejemplo (lua):**

```lua
-- This example prevents a specific entity from being detached from a Cargobob, even in the event of collisions.

-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the player's vehicle (cargobob)
local cargobob = GetVehiclePedIsIn(playerPed, false)

-- Retrieve the model hash of the cargobob.
local cargobobModel = GetEntityModel(cargobob)

-- Check if the cargobob exists. If not, terminate the script.
if not DoesEntityExist(cargobob) or GetHashKey("cargobob") ~= cargobobModel then 
    -- If the cargobob does not exist, end the execution of the code here.
    return 
end

local entityID = 15362 -- The entity you want to prevent from being detached from the Cargobob (this is a random entity ID).

-- Check if the entity exists; if not, terminate the script.
if not DoesEntityExist(yourEntity) then
    return
end

-- Prevent the entity from being detached from the Cargobob.
SetCargobobExcludeFromPickupEntity(cargobob, entityID)
```

**Ejemplo (js):**

```js
// This example prevents a specific entity from being detached from a Cargobob, even in the event of collisions.

// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the player's vehicle (cargobob)
const cargobob = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the cargobob.
const cargobobModel = GetEntityModel(cargobob);

// Check if the cargobob exists. If not, terminate the script.
if (!DoesEntityExist(cargobob) || GetHashKey("cargobob") !== cargobobModel) {
    // If the cargobob does not exist, end the execution of the code here.
    return;
}

const entityID = 15362; // The entity you want to prevent from being detached from the Cargobob (this is a random entity ID).

// Check if the entity exists; if not, terminate the script.
if (!DoesEntityExist(entityID)) {
    return;
}

// Prevent the entity from being detached from the Cargobob.
SetCargobobExcludeFromPickupEntity(cargobob, entityID);
```

**Ejemplo (cs):**

```cs
// This example prevents a specific entity from being detached from a Cargobob, even in the event of collisions.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the player's vehicle (cargobob)
int cargobob = GetVehiclePedIsIn(playerPed, false);

// Retrieve the model hash of the cargobob.
uint cargobobModel = GetEntityModel(cargobob);

// Check if the cargobob exists. If not, terminate the script.
if (!DoesEntityExist(cargobob) || (uint)GetHashKey("cargobob") != cargobobModel) {
    // If the cargobob does not exist, end the execution of the code here.
    return;
}

int entityID = 15362; // The entity you want to prevent from being detached from the Cargobob (this is a random entity ID).

// Check if the entity exists; if not, terminate the script.
if (!DoesEntityExist(entityID)) {
    return;
}

// Prevent the entity from being detached from the Cargobob.
SetCargobobExcludeFromPickupEntity(cargobob, entityID);
```

---
### SetCargobobForceDontDetachVehicle

`SET_CARGOBOB_FORCE_DONT_DETACH_VEHICLE` · hash `0x571FEB383F629926` · jhash `0x49949FDA` · **Cliente**

```lua
SetCargobobForceDontDetachVehicle(cargobob, toggle)
```
```c
void SET_CARGOBOB_FORCE_DONT_DETACH_VEHICLE(Vehicle cargobob, BOOL toggle);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Stops cargobob from being able to detach the attached vehicle.

**Nombres antiguos (alias):** `0x571FEB383F629926` (`N_0x571feb383f629926`), `_SET_CARGOBOB_HOOK_CAN_DETACH` (`SetCargobobHookCanDetach`)

---
### SetCargobobHookCanAttach

`_SET_CARGOBOB_HOOK_CAN_ATTACH` · hash `0x94A68DA412C4007D` · **Cliente**

```lua
SetCargobobHookCanAttach(vehicle, toggle)
```
```c
void _SET_CARGOBOB_HOOK_CAN_ATTACH(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Stops the cargobob from being able to attach any vehicle
```

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0x94A68DA412C4007D` (`N_0x94a68da412c4007d`)

---
### SetCargobobPickupMagnetActive

`SET_CARGOBOB_PICKUP_MAGNET_ACTIVE` · hash `0x9A665550F8DA349B` · jhash `0xF57066DA` · **Cliente**

```lua
SetCargobobPickupMagnetActive(cargobob, isActive)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_ACTIVE(Vehicle cargobob, BOOL isActive);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `isActive` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Won't attract or magnetize to any helicopters or planes of course, but that's common sense.  
```

**Nombres antiguos (alias):** `_CARGOBOB_MAGNET_GRAB_VEHICLE` (`CargobobMagnetGrabVehicle`), `_SET_CARGOBOB_PICKUP_MAGNET_ACTIVE` (`SetCargobobPickupMagnetActive`)

---
### SetCargobobPickupMagnetEffectRadius

`SET_CARGOBOB_PICKUP_MAGNET_EFFECT_RADIUS` · hash `0xA17BAD153B51547E` · jhash `0xE5DCD62F` · **Cliente**

```lua
SetCargobobPickupMagnetEffectRadius(vehicle, p1)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_EFFECT_RADIUS(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA17BAD153B51547E` (`N_0xa17bad153b51547e`)

---
### SetCargobobPickupMagnetFalloff

`SET_CARGOBOB_PICKUP_MAGNET_FALLOFF` · hash `0x685D5561680D088B` · jhash `0x91C80401` · **Cliente**

```lua
SetCargobobPickupMagnetFalloff(vehicle, p1)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_FALLOFF(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x685D5561680D088B` (`N_0x685d5561680d088b`)

---
### SetCargobobPickupMagnetPullRopeLength

`SET_CARGOBOB_PICKUP_MAGNET_PULL_ROPE_LENGTH` · hash `0x6D8EAC07506291FB` · jhash `0x60E29B78` · **Cliente**

```lua
SetCargobobPickupMagnetPullRopeLength(cargobob, p1)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_PULL_ROPE_LENGTH(Vehicle cargobob, float p1);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6D8EAC07506291FB` (`N_0x6d8eac07506291fb`)

---
### SetCargobobPickupMagnetPullStrength

`SET_CARGOBOB_PICKUP_MAGNET_PULL_STRENGTH` · hash `0xED8286F71A819BAA` · jhash `0x8191BC1A` · **Cliente**

```lua
SetCargobobPickupMagnetPullStrength(cargobob, p1)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_PULL_STRENGTH(Vehicle cargobob, float p1);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xED8286F71A819BAA` (`N_0xed8286f71a819baa`)

---
### SetCargobobPickupMagnetReducedFalloff

`SET_CARGOBOB_PICKUP_MAGNET_REDUCED_FALLOFF` · hash `0x66979ACF5102FD2F` · jhash `0x1CF139C6` · **Cliente**

```lua
SetCargobobPickupMagnetReducedFalloff(cargobob, p1)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_REDUCED_FALLOFF(Vehicle cargobob, float p1);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x66979ACF5102FD2F` (`N_0x66979acf5102fd2f`)

---
### SetCargobobPickupMagnetReducedStrength

`SET_CARGOBOB_PICKUP_MAGNET_REDUCED_STRENGTH` · hash `0xE301BD63E9E13CF0` · jhash `0x47D98A2E` · **Cliente**

```lua
SetCargobobPickupMagnetReducedStrength(cargobob, vehicle)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_REDUCED_STRENGTH(Vehicle cargobob, Vehicle vehicle);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE301BD63E9E13CF0` (`N_0xe301bd63e9e13cf0`)

---
### SetCargobobPickupMagnetStrength

`SET_CARGOBOB_PICKUP_MAGNET_STRENGTH` · hash `0xBCBFCD9D1DAC19E2` · jhash `0xCC3CF97D` · **Cliente**

```lua
SetCargobobPickupMagnetStrength(cargobob, strength)
```
```c
void SET_CARGOBOB_PICKUP_MAGNET_STRENGTH(Vehicle cargobob, float strength);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `strength` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBCBFCD9D1DAC19E2` (`N_0xbcbfcd9d1dac19e2`), `_SET_CARGOBOB_PICKUP_MAGNET_STRENGTH` (`SetCargobobPickupMagnetStrength`)

---
### SetCargobobPickupRopeDampingMultiplier

`SET_CARGOBOB_PICKUP_ROPE_DAMPING_MULTIPLIER` · hash `0xCF1182F682F65307` · jhash `0x7D927E1B` · **Cliente**

```lua
SetCargobobPickupRopeDampingMultiplier(cargobob, p1)
```
```c
void SET_CARGOBOB_PICKUP_ROPE_DAMPING_MULTIPLIER(Vehicle cargobob, float p1);
```

**Parámetros**

- `cargobob` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCF1182F682F65307` (`N_0xcf1182f682f65307`)

---
### SetCargobobPickupRopeType

`SET_CARGOBOB_PICKUP_ROPE_TYPE` · hash `0x0D5F65A8F4EBDAB5` · jhash `0xF258ADA1` · **Cliente**

```lua
SetCargobobPickupRopeType(vehicle, state)
```
```c
void SET_CARGOBOB_PICKUP_ROPE_TYPE(Vehicle vehicle, int state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0D5F65A8F4EBDAB5` (`N_0x0d5f65a8f4ebdab5`)

---
### SetConvertibleRoof

`SET_CONVERTIBLE_ROOF` · hash `0xF39C4F538B5124C2` · jhash `0xC87B6A51` · **Cliente**

```lua
SetConvertibleRoof(vehicle, toggle)
```
```c
void SET_CONVERTIBLE_ROOF(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to which the roof state will be applied.
- `toggle` (`BOOL`): Boolean value where `true` adds the roof and `false` removes it, applicable only if the vehicle has a version with and without a roof.

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables the convertible roof on vehicles that support old-style GTA IV roofs, which are not animated. Setting `toggle` to true will apply the roof to the vehicle, and setting it to false will remove the roof, assuming the vehicle has versions with and without a roof.

If you want to lock or unlock the roof mechanism, use [`SET_CONVERTIBLE_ROOF_LATCH_STATE`](#setconvertiblerooflatchstate).

You can check if the vehicle has a roof with [`DOES_VEHICLE_HAVE_ROOF`](#doesvehiclehaveroof).

```
NativeDB Introduced: v323
```

**Vehicles with both roofed and roofless versions (others may exist; this list is compiled from decompiled scripts).**

*   chino
*   voltic
*   buccaneer
*   buccaneer2
*   chino2
*   faction
*   faction2
*   mamba

**Ejemplo (lua):**

```lua
-- In this case we are removing the roof from the vehicle.
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if not DoesVehicleHaveRoof(vehicle) then return end
SetConvertibleRoof(vehicle, false)
```

**Ejemplo (js):**

```js
// In this case we are removing the roof from the vehicle.
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!DoesVehicleHaveRoof(vehicle)) return;
SetConvertibleRoof(vehicle, false);
```

**Ejemplo (cs):**

```cs
// In this case we are removing the roof from the vehicle.
using static CitizenFX.Core.Native.API;
int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!DoesVehicleHaveRoof(vehicle)) return;
SetConvertibleRoof(vehicle, false);
```

---
### SetConvertibleRoofLatchState

`SET_CONVERTIBLE_ROOF_LATCH_STATE` · hash `0x1A78AD3D8240536F` · jhash `0x0858678C` · **Cliente**

```lua
SetConvertibleRoofLatchState(vehicle, bLatched)
```
```c
void SET_CONVERTIBLE_ROOF_LATCH_STATE(Vehicle vehicle, BOOL bLatched);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle whose convertible roof latch state is to be set.
- `bLatched` (`BOOL`): A boolean value indicating the desired latch state of the roof. Set to `true` to latch (lock) the roof, preventing it from being opened. Set to `false` to unlatch (unlock) the roof, allowing it to be opened or closed.

**Devuelve:** `void`

**Descripción oficial:**

This native is used to latch or unlatch the convertible roof of a vehicle. It allows for direct control over the roof's mechanism without actually opening or closing the roof. This can be useful for scenarios where you need to prepare a vehicle's roof to be opened or closed by another action or to ensure it remains fixed in its current state regardless of other interactions.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x1A78AD3D8240536F` (`N_0x1a78ad3d8240536f`)

**Ejemplo (lua):**

```lua
-- To latch (lock) the convertible roof, preventing it from being opened
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
if not DoesVehicleHaveRoof(vehicle) then return end
SetConvertibleRoofLatchState(vehicle, true)
```

**Ejemplo (js):**

```js
// To latch (lock) the convertible roof, preventing it from being opened
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!DoesVehicleHaveRoof(vehicle)) return;
SetConvertibleRoofLatchState(vehicle, true);
```

**Ejemplo (cs):**

```cs
// To latch (lock) the convertible roof, preventing it from being opened
using static CitizenFX.Core.Native.API;

int vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
if (!DoesVehicleHaveRoof(vehicle)) return;
SetConvertibleRoofLatchState(vehicle, true);
```

---
### SetDeployHeliStubWings

`_SET_DEPLOY_HELI_STUB_WINGS` · hash `0xB251E0B33E58B424` · **Cliente**

```lua
SetDeployHeliStubWings(vehicle, deploy, p2)
```
```c
void _SET_DEPLOY_HELI_STUB_WINGS(Vehicle vehicle, BOOL deploy, BOOL p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `deploy` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Only used with the "akula" and "annihilator2" in the decompiled native scripts.

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0xB251E0B33E58B424` (`N_0xb251e0b33e58b424`)

---
### SetDisableBmxExtraTrickForces

`SET_DISABLE_BMX_EXTRA_TRICK_FORCES` · hash `0x26D99D5A82FD18E8` · **Cliente**

```lua
SetDisableBmxExtraTrickForces(disableExtraTrickForces)
```
```c
void SET_DISABLE_BMX_EXTRA_TRICK_FORCES(BOOL disableExtraTrickForces);
```

**Parámetros**

- `disableExtraTrickForces` (`BOOL`): Set to `true` to disable the extra forces applied for tricks on BMX bicycles, making the bike behave more like a regular bicycle without trick capabilities. Set to `false` to allow BMX bikes to perform tricks normally.

**Devuelve:** `void`

**Descripción oficial:**

Disables the additional physics forces applied to BMX bikes that enable them to perform tricks.

```
NativeDB Introduced: v463
```

**Nombres antiguos (alias):** `0x26D99D5A82FD18E8` (`N_0x26d99d5a82fd18e8`)

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the BMX bike the player is currently riding
local bmx = GetVehiclePedIsIn(playerPed, false)

-- If the player is not riding a BMX bike, return
if not IsThisModelABicycle(GetEntityModel(bmx)) then return end

-- Disable the extra forces applied to BMX bikes for tricks
SetDisableBmxExtraTrickForces(bmx, true)
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the BMX bike the player is currently riding
const bmx = GetVehiclePedIsIn(playerPed, false);

// If the player is not riding a BMX bike, return
if (!IsThisModelABicycle(GetEntityModel(bmx))) return;

// Disable the extra forces applied to BMX bikes for tricks
SetDisableBmxExtraTrickForces(bmx, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the BMX bike the player is currently riding
int bmx = GetVehiclePedIsIn(playerPed, false);

// If the player is not riding a BMX bike, return
if (!IsThisModelABicycle(GetEntityModel(bmx))) return;

// Disable the extra forces applied to BMX bikes for tricks
SetDisableBmxExtraTrickForces(bmx, true);
```

---
### SetDisableExplodeFromBodyDamageOnCollision

`SET_DISABLE_EXPLODE_FROM_BODY_DAMAGE_ON_COLLISION` · hash `0x26E13D440E7F6064` · **Cliente**

```lua
SetDisableExplodeFromBodyDamageOnCollision(vehicle, disableExplode)
```
```c
void SET_DISABLE_EXPLODE_FROM_BODY_DAMAGE_ON_COLLISION(Vehicle vehicle, BOOL disableExplode);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to apply this setting to.
- `disableExplode` (`BOOL`): `true` to disable explosion from body damage on collision; `false` to allow explosions as normal.

**Devuelve:** `void`

**Descripción oficial:**

This only works for planes.

Prevents a vehicle from exploding upon sustaining body damage from physical collisions.

For helicopters, you might want to check [`SET_DISABLE_HELI_EXPLODE_FROM_BODY_DAMAGE`](#setdisableheliexplodefrombodydamage) instead.

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x26E13D440E7F6064` (`N_0x26e13d440e7f6064`)

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Disable explosion from body damage on collision for the vehicle
SetDisableExplodeFromBodyDamageOnCollision(vehicle, true)
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Disable explosion from body damage on collision for the vehicle
SetDisableExplodeFromBodyDamageOnCollision(vehicle, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Disable explosion from body damage on collision for the vehicle
SetDisableExplodeFromBodyDamageOnCollision(vehicle, true);
```

---
### SetDisableExplodeFromBodyDamageReceivedByAiVehicle

`_SET_DISABLE_EXPLODE_FROM_BODY_DAMAGE_RECEIVED_BY_AI_VEHICLE` · hash `0xB0B7DF5CB876FF5E` · **Cliente**

```lua
SetDisableExplodeFromBodyDamageReceivedByAiVehicle(plane, disable)
```
```c
void _SET_DISABLE_EXPLODE_FROM_BODY_DAMAGE_RECEIVED_BY_AI_VEHICLE(Vehicle plane, BOOL disable);
```

**Parámetros**

- `plane` (`Vehicle`)
- `disable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

Prevents the plane from exploding when taking body damage if the inflictor is an AI-controlled vehicle. Only works for planes.

---
### SetDisableHeliExplodeFromBodyDamage

`SET_DISABLE_HELI_EXPLODE_FROM_BODY_DAMAGE` · hash `0xEDBC8405B3895CC9` · **Cliente**

```lua
SetDisableHeliExplodeFromBodyDamage(helicopter, disableExplode)
```
```c
void SET_DISABLE_HELI_EXPLODE_FROM_BODY_DAMAGE(Vehicle helicopter, BOOL disableExplode);
```

**Parámetros**

- `helicopter` (`Vehicle`): The helicopter to apply this setting to.
- `disableExplode` (`BOOL`): `true` to disable explosion from body damage on collision; `false` to allow explosions as normal.

**Devuelve:** `void`

**Descripción oficial:**

This works on helicopters and planes.

Prevents a helicopter from exploding due to relatively minor body damage.

```
NativeDB Introduced: v1103
```

**Nombres antiguos (alias):** `0xEDBC8405B3895CC9` (`N_0xedbc8405b3895cc9`)

**Ejemplo (lua):**

```lua
-- Retrieve the player ped.
local playerPed = PlayerPedId()

-- Retrieve the helicopter the player is currently in.
local helicopter = GetVehiclePedIsIn(playerPed, false)

-- If the player is not in a helicopter, or the vehicle is not a helicopter, return.
if (helicopter == 0) or (not IsThisModelAHeli(GetEntityModel(helicopter))) then return end

-- Disable explosion from body damage for the helicopter.
SetDisableHeliExplodeFromBodyDamage(helicopter, true)
```

**Ejemplo (js):**

```js
// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the helicopter the player is currently in.
const helicopter = GetVehiclePedIsIn(playerPed, false);

// If the player is not in a helicopter, or the vehicle is not a helicopter, return.
if (helicopter === 0 || !IsThisModelAHeli(GetEntityModel(helicopter))) return;

// Disable explosion from body damage for the helicopter.
SetDisableHeliExplodeFromBodyDamage(helicopter, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Retrieve the player ped.
int playerPed = PlayerPedId();

// Retrieve the helicopter the player is currently in.
int helicopter = GetVehiclePedIsIn(playerPed, false);

// If the player is not in a helicopter, or the vehicle is not a helicopter, return.
if (helicopter == 0 || !IsThisModelAHeli(GetEntityModel(helicopter))) return;

// Disable explosion from body damage for the helicopter.
SetDisableHeliExplodeFromBodyDamage(helicopter, true);
```

---
### SetDisableHoverModeFlight

`SET_DISABLE_HOVER_MODE_FLIGHT` · hash `0x2D55FE374D5FDB91` · **Cliente**

```lua
SetDisableHoverModeFlight(vehicle, toggle)
```
```c
void SET_DISABLE_HOVER_MODE_FLIGHT(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to which the toggle will be applied.
- `toggle` (`BOOL`): Boolean parameter where setting `true` disables the vehicle's wings, preventing flight. Setting it to `false` allows the vehicle to fly as usual.

**Devuelve:** `void`

**Descripción oficial:**

Disables wings for `Deluxo` and `Oppressor MK II`. For the Deluxo, it retracts the wings immediately, preventing flight. For the Oppressor Mk II, the wings retract after landing and take-off is not possible, though it can still glide if launched into the air.

**Nombres antiguos (alias):** `_SET_VEHICLE_HOVER_TRANSFORM_ACTIVE` (`SetVehicleHoverTransformActive`)

**Ejemplo (lua):**

```lua
-- In this case we are disabling the wings of the vehicle
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetDisableHoverModeFlight(vehicle, true)
```

**Ejemplo (js):**

```js
// In this case we are disabling the wings of the vehicle
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetDisableHoverModeFlight(vehicle, true);
```

**Ejemplo (cs):**

```cs
// In this case we are disabling the wings of the vehicle
using static CitizenFX.Core.Native.API;
Vehicle vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetDisableHoverModeFlight(vehicle, true);
```

---
### SetDisablePretendOccupants

`SET_DISABLE_PRETEND_OCCUPANTS` · hash `0x25367DE49D64CF16` · jhash `0xCBD98BA1` · **Cliente**

```lua
SetDisablePretendOccupants(vehicle, toggle)
```
```c
void SET_DISABLE_PRETEND_OCCUPANTS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x25367DE49D64CF16` (`N_0x25367de49d64cf16`)

---
### SetDisableRandomTrainsThisFrame

`SET_DISABLE_RANDOM_TRAINS_THIS_FRAME` · hash `0xD4B8E3D1917BC86B` · jhash `0x09462665` · **Cliente**

```lua
SetDisableRandomTrainsThisFrame(toggle)
```
```c
void SET_DISABLE_RANDOM_TRAINS_THIS_FRAME(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD4B8E3D1917BC86B` (`N_0xd4b8e3d1917bc86b`), `_SET_SOMETHING_MULTIPLIER_THIS_FRAME` (`SetSomethingMultiplierThisFrame`)

---
### SetDisableSuperdummyMode

`_SET_DISABLE_SUPERDUMMY_MODE` · hash `0xB088E9A47AE6EDD5` · **Cliente**

```lua
SetDisableSuperdummyMode(vehicle, p1)
```
```c
void _SET_DISABLE_SUPERDUMMY_MODE(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB088E9A47AE6EDD5` (`N_0xb088e9a47ae6edd5`)

---
### SetDisableTurretMovementThisFrame

`_SET_DISABLE_TURRET_MOVEMENT_THIS_FRAME` · hash `0xE615BB7A7752C76A` · **Cliente**

```lua
SetDisableTurretMovementThisFrame(vehicle, turretIdx)
```
```c
void _SET_DISABLE_TURRET_MOVEMENT_THIS_FRAME(Vehicle vehicle, int turretIdx);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `turretIdx` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Disables turret movement when called in a loop. You can still fire and aim. You cannot shoot backwards though.

```
NativeDB Introduced: v1365
```

**Nombres antiguos (alias):** `0xE615BB7A7752C76A` (`N_0xe615bb7a7752c76a`), `_SET_DISABLE_TURRET_MOVEMENT` (`SetDisableTurretMovement`)

---
### SetDisableVehicleEngineFires

`SET_DISABLE_VEHICLE_ENGINE_FIRES` · hash `0x91A0BD635321F145` · jhash `0x1784BA1A` · **Cliente**

```lua
SetDisableVehicleEngineFires(vehicle, toggle)
```
```c
void SET_DISABLE_VEHICLE_ENGINE_FIRES(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x91A0BD635321F145` (`N_0x91a0bd635321f145`)

---
### SetDisableVehicleFlightNozzlePosition

`_SET_DISABLE_VEHICLE_FLIGHT_NOZZLE_POSITION` · hash `0xCE2B43770B655F8F` · **Cliente**

```lua
SetDisableVehicleFlightNozzlePosition(vehicle, direction)
```
```c
void _SET_DISABLE_VEHICLE_FLIGHT_NOZZLE_POSITION(Vehicle vehicle, BOOL direction);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `direction` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
True stops vtols from switching modes. Doesn't stop the sound though.
```

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `_SET_PLANE_VTOL_ANIMATION_DISABLED` (`SetPlaneVtolAnimationDisabled`)

---
### SetDisableVehiclePetrolTankDamage

`SET_DISABLE_VEHICLE_PETROL_TANK_DAMAGE` · hash `0x37C8252A7C92D017` · jhash `0xAD3E05F2` · **Cliente**

```lua
SetDisableVehiclePetrolTankDamage(vehicle, toggle)
```
```c
void SET_DISABLE_VEHICLE_PETROL_TANK_DAMAGE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetDisableVehiclePetrolTankFires

`SET_DISABLE_VEHICLE_PETROL_TANK_FIRES` · hash `0x465BF26AB9684352` · jhash `0xC40192B5` · **Cliente**

```lua
SetDisableVehiclePetrolTankFires(vehicle, toggle)
```
```c
void SET_DISABLE_VEHICLE_PETROL_TANK_FIRES(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x465BF26AB9684352` (`N_0x465bf26ab9684352`)

---
### SetDisableVehicleUnk

`_SET_DISABLE_VEHICLE_UNK` · hash `0x143921E45EC44D62` · **Cliente**

```lua
SetDisableVehicleUnk(toggle)
```
```c
void _SET_DISABLE_VEHICLE_UNK(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### SetDisableVehicleUnk_2

`_SET_DISABLE_VEHICLE_UNK_2` · hash `0x211E95CE9903940C` · **Cliente**

```lua
SetDisableVehicleUnk_2(toggle)
```
```c
void _SET_DISABLE_VEHICLE_UNK_2(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### SetDisableVehicleWindowCollisions

`_SET_DISABLE_VEHICLE_WINDOW_COLLISIONS` · hash `0x1087BC8EC540DAEB` · **Cliente**

```lua
SetDisableVehicleWindowCollisions(vehicle, toggle)
```
```c
void _SET_DISABLE_VEHICLE_WINDOW_COLLISIONS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to toggle this for.
- `toggle` (`BOOL`): True disables the collision, false enables the collision

**Devuelve:** `void`

**Descripción oficial:**

R\* used it to "remove" vehicle windows when "nightshark" had some mod, which adding some kind of armored windows. When enabled, you can't break vehicles glass. All your bullets wiil shoot through glass. You also will not able to break the glass with any other way (hitting and etc)

**Nombres antiguos (alias):** `0x1087BC8EC540DAEB` (`N_0x1087bc8ec540daeb`)

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

if GetEntityModel(vehicle) == `NIGHTSHARK` then
    -- Mod index 5 = armored window plates
    if GetVehicleMod(vehicle, 5) ~= -1 then
        -- The nightshark has armored plates in front of the windows
        -- so we disable the window collisions
        SetDisableVehicleWindowCollisions(vehicle, true)
    else
        -- The nightshark has no armored plates in front of the windows
        -- so we enable the window collisions
        SetDisableVehicleWindowCollisions(vehicle, false)
    end
end
```

---
### SetDistantCarsEnabled

`SET_DISTANT_CARS_ENABLED` · hash `0xF796359A959DF65D` · jhash `0xB5CC548B` · **Cliente**

```lua
SetDistantCarsEnabled(toggle)
```
```c
void SET_DISTANT_CARS_ENABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Toggles to render distant vehicles. They may not be vehicles but images to look like vehicles.  
```

**Nombres antiguos (alias):** `0xF796359A959DF65D` (`N_0xf796359a959df65d`), `_DISPLAY_DISTANT_VEHICLES` (`DisplayDistantVehicles`)

---
### SetDriftTyresEnabled

`_SET_DRIFT_TYRES_ENABLED` · hash `0x5AC79C98C5C17F05` · **Cliente**

```lua
SetDriftTyresEnabled(vehicle, toggle)
```
```c
void _SET_DRIFT_TYRES_ENABLED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### SetEnableVehicleSlipstreaming

`SET_ENABLE_VEHICLE_SLIPSTREAMING` · hash `0xE6C0C80B8C867537` · jhash `0xD2B8ACBD` · **Cliente**

```lua
SetEnableVehicleSlipstreaming(toggle)
```
```c
void SET_ENABLE_VEHICLE_SLIPSTREAMING(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Enable/Disables global slipstream physics

**Nombres antiguos (alias):** `0xE6C0C80B8C867537` (`N_0xe6c0c80b8c867537`)

---
### SetFarDrawVehicles

`SET_FAR_DRAW_VEHICLES` · hash `0x26324F33423F3CC3` · jhash `0x9F019C49` · **Cliente**

```lua
SetFarDrawVehicles(toggle)
```
```c
void SET_FAR_DRAW_VEHICLES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetForceHdVehicle

`SET_FORCE_HD_VEHICLE` · hash `0x97CE68CB032583F0` · jhash `0xE0FC6A32` · **Cliente**

```lua
SetForceHdVehicle(vehicle, toggle)
```
```c
void SET_FORCE_HD_VEHICLE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x97CE68CB032583F0` (`N_0x97ce68cb032583f0`)

---
### SetForceLowLodAnchorMode

`SET_FORCE_LOW_LOD_ANCHOR_MODE` · hash `0xB28B1FE5BFADD7F5` · jhash `0xA739012A` · **Cliente**

```lua
SetForceLowLodAnchorMode(boat, toggle)
```
```c
void SET_FORCE_LOW_LOD_ANCHOR_MODE(Vehicle boat, BOOL toggle);
```

**Parámetros**

- `boat` (`Vehicle`): The target boat.
- `toggle` (`BOOL`): Set the forced low LOD anchor mode. If `true`, the boat will remain in low LOD anchor mode even when a player is driving.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether a boat should remain in the non-physical, low LOD anchor mode even when a player is driving it.

**Note**: This native requires [SET_BOAT_REMAINS_ANCHORED_WHILE_PLAYER_IS_DRIVER](#setboatremainsanchoredwhileplayerisdriver) to be set to `true` to work properly.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xB28B1FE5BFADD7F5` (`N_0xb28b1fe5bfadd7f5`), `_SET_FORCED_BOAT_LOCATION_WHEN_ANCHORED` (`SetForcedBoatLocationWhenAnchored`)

---
### SetForkliftForkHeight

`SET_FORKLIFT_FORK_HEIGHT` · hash `0x37EBBF3117BD6A25` · jhash `0x943A6CFC` · **Cliente**

```lua
SetForkliftForkHeight(vehicle, height)
```
```c
void SET_FORKLIFT_FORK_HEIGHT(Vehicle vehicle, float height);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `height` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
0.0 = Lowest 1.0 = Highest. This is best to be used if you wanna pick-up a car since un-realistically on GTA V forklifts can't pick up much of anything due to vehicle mass. If you put this under a car then set it above 0.0 to a 'lifted-value' it will raise the car with no issue lol
```

**Nombres antiguos (alias):** `0x37EBBF3117BD6A25` (`N_0x37ebbf3117bd6a25`)

---
### SetGarbageTrucks

`SET_GARBAGE_TRUCKS` · hash `0x2AFD795EEAC8D30D` · jhash `0xD9ABB0FF` · **Cliente**

```lua
SetGarbageTrucks(toggle)
```
```c
void SET_GARBAGE_TRUCKS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetHeliBladesFullSpeed

`SET_HELI_BLADES_FULL_SPEED` · hash `0xA178472EBB8AE60D` · jhash `0x033A9408` · **Cliente**

```lua
SetHeliBladesFullSpeed(vehicle)
```
```c
void SET_HELI_BLADES_FULL_SPEED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The helicopter or the plane

**Devuelve:** `void`

**Descripción oficial:**

Despite its name, this works on Helicopters and Planes.

Sets the speed of the helicopter blades to full speed.

This is equivalent to calling `SetHeliBladesSpeed(vehicleHandle, 1.0);`

---
### SetHeliBladesSpeed

`SET_HELI_BLADES_SPEED` · hash `0xFD280B4D7F3ABC4D` · jhash `0x5C7D4EA9` · **Cliente**

```lua
SetHeliBladesSpeed(vehicle, speed)
```
```c
void SET_HELI_BLADES_SPEED(Vehicle vehicle, float speed);
```

**Parámetros**

- `vehicle` (`Vehicle`): The helicopter or the plane
- `speed` (`float`): Desired blade rotation speed from 0.0 to 1.0

**Devuelve:** `void`

**Descripción oficial:**

Despite its name, this works on Helicopters and Planes.

Sets the speed of the helicopter blades in percentage of the full speed.

---
### SetHeliCombatOffset

`SET_HELI_COMBAT_OFFSET` · hash `0x0A3F820A9A9A9AC5` · **Cliente**

```lua
SetHeliCombatOffset(vehicle, x, y, z)
```
```c
void SET_HELI_COMBAT_OFFSET(Vehicle vehicle, float x, float y, float z);
```

**Parámetros**

- `vehicle` (`Vehicle`): Helicopter for which the combat offset is being set.
- `x` (`float`): Offset along the X-axis (left/right) relative to the helicopter's current position and orientation
- `y` (`float`): Offset along the Y-axis (forward/backward) relative to the helicopter's current position and orientation
- `z` (`float`): Offset along the Z-axis (up/down) relative to the helicopter's current position and orientation.

**Devuelve:** `void`

**Descripción oficial:**

Set a specific offset for helis chasing target in combat

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0x0A3F820A9A9A9AC5` (`N_0x0a3f820a9a9a9ac5`)

---
### SetHeliMainRotorHealth

`_SET_HELI_MAIN_ROTOR_HEALTH` · hash `0x4056EA1105F5ABD7` · **Cliente**

```lua
SetHeliMainRotorHealth(vehicle, health)
```
```c
void _SET_HELI_MAIN_ROTOR_HEALTH(Vehicle vehicle, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `health` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4056EA1105F5ABD7` (`N_0x4056ea1105f5abd7`)

---
### SetHeliResistToExplosion

`SET_HELI_RESIST_TO_EXPLOSION` · hash `0x8074CC1886802912` · **Cliente**

```lua
SetHeliResistToExplosion(helicopter, bResistToExplosion)
```
```c
void SET_HELI_RESIST_TO_EXPLOSION(Vehicle helicopter, BOOL bResistToExplosion);
```

**Parámetros**

- `helicopter` (`Vehicle`): The helicopter to apply resistance to.
- `bResistToExplosion` (`BOOL`): Set to `true` to make the helicopter resistant to explosions, or `false` to disable this resistance.

**Devuelve:** `void`

**Descripción oficial:**

Makes a helicopter resistant to multiple explosions. When enabled, helicopters can survive two or more explosions.

```
NativeDB Introduced: 2545
```

---
### SetHeliTailBoomCanBreakOff

`SET_HELI_TAIL_BOOM_CAN_BREAK_OFF` · hash `0x3EC8BF18AA453FE9` · jhash `0x2916D69B` · **Cliente**

```lua
SetHeliTailBoomCanBreakOff(heli, toggle)
```
```c
void SET_HELI_TAIL_BOOM_CAN_BREAK_OFF(Vehicle heli, BOOL toggle);
```

**Parámetros**

- `heli` (`Vehicle`): The helicopter for which the tail boom can break off.
- `toggle` (`BOOL`): Determines whether the helicopter's tail boom can break off.

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables the ability for a helicopter's tail boom to break off.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `SET_HELI_TAIL_EXPLODE_THROW_DASHBOARD` (`SetHeliTailExplodeThrowDashboard`), `WAS_COUNTER_ACTIVATED` (`WasCounterActivated`), `0x3EC8BF18AA453FE9` (`N_0x3ec8bf18aa453fe9`)

**Ejemplo (lua):**

```lua
local heli = GetVehiclePedIsIn(PlayerPedId(), false)
if heli == 0 or GetVehicleType(heli) ~= "heli" then return end

SetHeliTailBoomCanBreakOff(heli, true)
```

**Ejemplo (js):**

```js
const heli = GetVehiclePedIsIn(PlayerPedId(), false);
if (heli === 0 || GetVehicleType(heli) !== "heli") return;

SetHeliTailBoomCanBreakOff(heli, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int heli = GetVehiclePedIsIn(PlayerPedId(), false);
if (heli == 0 || GetVehicleType(heli) !== "heli") return;

SetHeliTailBoomCanBreakOff(heli, true);
```

---
### SetHeliTailRotorHealth

`_SET_HELI_TAIL_ROTOR_HEALTH` · hash `0xFE205F38AAA58E5B` · **Cliente**

```lua
SetHeliTailRotorHealth(vehicle, health)
```
```c
void _SET_HELI_TAIL_ROTOR_HEALTH(Vehicle vehicle, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `health` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFE205F38AAA58E5B` (`N_0xfe205f38aaa58e5b`)

---
### SetHeliTurbulenceScalar

`SET_HELI_TURBULENCE_SCALAR` · hash `0xE6F13851780394DA` · jhash `0xCCB41A55` · **Cliente**

```lua
SetHeliTurbulenceScalar(vehicle, p1)
```
```c
void SET_HELI_TURBULENCE_SCALAR(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE6F13851780394DA` (`N_0xe6f13851780394da`)

---
### SetHelicopterRollPitchYawMult

`_SET_HELICOPTER_ROLL_PITCH_YAW_MULT` · hash `0x6E0859B530A365CC` · jhash `0x6E67FD35` · **Cliente**

```lua
SetHelicopterRollPitchYawMult(helicopter, multiplier)
```
```c
void _SET_HELICOPTER_ROLL_PITCH_YAW_MULT(Vehicle helicopter, float multiplier);
```

**Parámetros**

- `helicopter` (`Vehicle`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
value between 0.0 and 1.0  
```

---
### SetHoverModeWingRatio

`SET_HOVER_MODE_WING_RATIO` · hash `0x70A252F60A3E036B` · **Cliente**

```lua
SetHoverModeWingRatio(vehicle, ratio)
```
```c
void SET_HOVER_MODE_WING_RATIO(Vehicle vehicle, float ratio);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to which the ratio will be applied.
- `ratio` (`float`): Between 0.0 and 1.0. 0.0 is wings closed, 1.0 is wings open.

**Devuelve:** `void`

**Descripción oficial:**

This native allows opening or closing the wings of the Deluxo/Oppressor. For the Deluxo, wing deployment depends on sufficient altitude.

**Nombres antiguos (alias):** `_SET_SPECIALFLIGHT_WING_RATIO` (`SetSpecialflightWingRatio`)

**Ejemplo (lua):**

```lua
-- In this case we are opening the wings of the vehicle
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)
SetHoverModeWingRatio(vehicle, 1.0)
```

**Ejemplo (js):**

```js
// In this case we are opening the wings of the vehicle
const vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetHoverModeWingRatio(vehicle, 1.0);
```

**Ejemplo (cs):**

```cs
// In this case we are opening the wings of the vehicle
using static CitizenFX.Core.Native.API;
Vehicle vehicle = GetVehiclePedIsIn(PlayerPedId(), false);
SetHoverModeWingRatio(vehicle, 1f);
```

---
### SetHydraulicRaised

`_SET_HYDRAULIC_RAISED` · hash `0x28B18377EB6E25F6` · **Cliente**

```lua
SetHydraulicRaised(vehicle, toggle)
```
```c
void _SET_HYDRAULIC_RAISED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x28B18377EB6E25F6` (`N_0x28b18377eb6e25f6`)

---
### SetHydraulicWheelState

`_SET_HYDRAULIC_WHEEL_STATE` · hash `0x8EA86DF356801C7D` · **Cliente**

```lua
SetHydraulicWheelState(vehicle, state)
```
```c
void _SET_HYDRAULIC_WHEEL_STATE(Vehicle vehicle, int state);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `state` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8EA86DF356801C7D` (`N_0x8ea86df356801c7d`)

---
### SetHydraulicWheelStateTransition

`_SET_HYDRAULIC_WHEEL_STATE_TRANSITION` · hash `0xC24075310A8B9CD1` · **Cliente**

```lua
SetHydraulicWheelStateTransition(vehicle, wheelId, state, value, p4)
```
```c
void _SET_HYDRAULIC_WHEEL_STATE_TRANSITION(Vehicle vehicle, int wheelId, int state, float value, float p4);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelId` (`int`)
- `state` (`int`)
- `value` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets vehicle wheel hydraulic states transition. Known states:
0 - reset
1 - raise wheel (uses value arg, works just like _SET_VEHICLE_HYDRAULIC_WHEEL_VALUE)
2 - jump using wheel
```

**Nombres antiguos (alias):** `0xC24075310A8B9CD1` (`N_0xc24075310a8b9cd1`)

---
### SetHydraulicWheelValue

`_SET_HYDRAULIC_WHEEL_VALUE` · hash `0x84EA99C62CB3EF0C` · **Cliente**

```lua
SetHydraulicWheelValue(vehicle, wheelId, value)
```
```c
void _SET_HYDRAULIC_WHEEL_VALUE(Vehicle vehicle, int wheelId, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelId` (`int`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Works only on vehicles that support hydraulic.
```

**Nombres antiguos (alias):** `0x84EA99C62CB3EF0C` (`N_0x84ea99c62cb3ef0c`), `_SET_HYDRAULIC_STATE` (`SetHydraulicState`)

---
### SetLastDrivenVehicle

`SET_LAST_DRIVEN_VEHICLE` · hash `0xACFB2463CC22BED2` · jhash `0xD1B71A25` · **Cliente**

```lua
SetLastDrivenVehicle(vehicle)
```
```c
void SET_LAST_DRIVEN_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xACFB2463CC22BED2` (`N_0xacfb2463cc22bed2`)

---
### SetLightsCutoffDistanceTweak

`SET_LIGHTS_CUTOFF_DISTANCE_TWEAK` · hash `0xBC3CCA5844452B06` · jhash `0x929801C6` · **Cliente**

```lua
SetLightsCutoffDistanceTweak(distance)
```
```c
void SET_LIGHTS_CUTOFF_DISTANCE_TWEAK(float distance);
```

**Parámetros**

- `distance` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBC3CCA5844452B06` (`N_0xbc3cca5844452b06`)

---
### SetMissionTrainAsNoLongerNeeded

`SET_MISSION_TRAIN_AS_NO_LONGER_NEEDED` · hash `0xBBE7648349B49BE8` · jhash `0x19808560` · **Cliente**

```lua
local train = SetMissionTrainAsNoLongerNeeded(p1)
```
```c
void SET_MISSION_TRAIN_AS_NO_LONGER_NEEDED(Vehicle* train, BOOL p1);
```

**Parámetros**

- `train` (`Vehicle*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 is always 0  
```

---
### SetMissionTrainCoords

`SET_MISSION_TRAIN_COORDS` · hash `0x591CA673AA6AB736` · jhash `0xD6D70803` · **Cliente**

```lua
SetMissionTrainCoords(train, x, y, z)
```
```c
void SET_MISSION_TRAIN_COORDS(Vehicle train, float x, float y, float z);
```

**Parámetros**

- `train` (`Vehicle`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### SetNitrousIsActive

`SET_NITROUS_IS_ACTIVE` · hash `0x465EEA70AF251045` · **Cliente**

```lua
SetNitrousIsActive(vehicle, isActive)
```
```c
void SET_NITROUS_IS_ACTIVE(Vehicle vehicle, BOOL isActive);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle whose nitrous system is to be controlled.
- `isActive` (`BOOL`): A boolean value where `true` activates the nitrous system and `false` deactivates it.

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: 3095
```

Activates or deactivates the nitrous system in the specified vehicle, based on the boolean value provided.
You can clear the nitrous with [`CLEAR_NITROUS`](#clearnitrous), if you want to have more control on the nitrous and those settings, use [`SET_OVERRIDE_NITROUS_LEVEL`](VEHICLE-2.md#setoverridenitrouslevel)

**Ejemplo (lua):**

```lua
-- Retrieve the player ped
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if vehicle == 0 then return end

 -- Enable the nitrous system on the vehicle.
SetNitrousIsActive(vehicle, true)
```

**Ejemplo (js):**

```js
// Retrieve the player ped
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (vehicle == 0) return;

// Enable the nitrous system on the vehicle.
SetNitrousIsActive(vehicle, true);
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

// Enable the nitrous system on the vehicle.
SetNitrousIsActive(vehicle, true);
```

---
