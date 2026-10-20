# Natives de GTA V — PED (parte 1 de 2: AddArmourToPed … SetPedToInformRespectedFriends)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `PED`: **612** natives.

Partes: **[1]** · [2](PED-2.md)

[← Índice de natives](../README.md)

## Índice de esta página

[`AddArmourToPed`](#addarmourtoped) · [`AddPedDecorationFromHashes`](#addpeddecorationfromhashes) · [`AddPedDecorationFromHashesInCorona`](#addpeddecorationfromhashesincorona) · [`AddRelationshipGroup`](#addrelationshipgroup) · [`AddScenarioBlockingArea`](#addscenarioblockingarea) · [`ApplyDamageToPed`](#applydamagetoped) · [`ApplyPedBlood`](#applypedblood) · [`ApplyPedBloodByZone`](#applypedbloodbyzone) · [`ApplyPedBloodDamageByZone`](#applypedblooddamagebyzone) · [`ApplyPedBloodSpecific`](#applypedbloodspecific) · [`ApplyPedDamageDecal`](#applypeddamagedecal) · [`ApplyPedDamagePack`](#applypeddamagepack) · [`AttachSynchronizedSceneToEntity`](#attachsynchronizedscenetoentity) · [`BlockPedDeadBodyShockingEvents`](#blockpeddeadbodyshockingevents) · [`CanCreateRandomBikeRider`](#cancreaterandombikerider) · [`CanCreateRandomCops`](#cancreaterandomcops) · [`CanCreateRandomDriver`](#cancreaterandomdriver) · [`CanCreateRandomPed`](#cancreaterandomped) · [`CanKnockPedOffVehicle`](#canknockpedoffvehicle) · [`CanPedInCombatSeeTarget`](#canpedincombatseetarget) · [`CanPedRagdoll`](#canpedragdoll) · [`CanPedSeeHatedPed`](#canpedseehatedped) · [`ClearAllPedProps`](#clearallpedprops) · [`ClearAllPedVehicleForcedSeatUsage`](#clearallpedvehicleforcedseatusage) · [`ClearFacialClipsetOverride`](#clearfacialclipsetoverride) · [`ClearFacialIdleAnimOverride`](#clearfacialidleanimoverride) · [`ClearPedAlternateMovementAnim`](#clearpedalternatemovementanim) · [`ClearPedAlternateWalkAnim`](#clearpedalternatewalkanim) · [`ClearPedBloodDamage`](#clearpedblooddamage) · [`ClearPedBloodDamageByZone`](#clearpedblooddamagebyzone) · [`ClearPedCoverClipsetOverride`](#clearpedcoverclipsetoverride) · [`ClearPedDamageDecalByZone`](#clearpeddamagedecalbyzone) · [`ClearPedDecorations`](#clearpeddecorations) · [`ClearPedDecorationsLeaveScars`](#clearpeddecorationsleavescars) · [`ClearPedDriveByClipsetOverride`](#clearpeddrivebyclipsetoverride) · [`ClearPedEnvDirt`](#clearpedenvdirt) · [`ClearPedLastDamageBone`](#clearpedlastdamagebone) · [`ClearPedNonCreationArea`](#clearpednoncreationarea) · [`ClearPedParachutePackVariation`](#clearpedparachutepackvariation) · [`ClearPedProp`](#clearpedprop) · [`ClearPedScubaGearVariation`](#clearpedscubagearvariation) · [`ClearPedStoredHatProp`](#clearpedstoredhatprop) · [`ClearPedWetness`](#clearpedwetness) · [`ClearRagdollBlockingFlags`](#clearragdollblockingflags) · [`ClearRelationshipBetweenGroups`](#clearrelationshipbetweengroups) · [`ClonePed`](#cloneped) · [`ClonePedEx`](#clonepedex) · [`ClonePedToTarget`](#clonepedtotarget) · [`ClonePedToTargetEx`](#clonepedtotargetex) · [`CreateGroup`](#creategroup) · [`CreateNmMessage`](#createnmmessage) · [`CreateParachuteBagObject`](#createparachutebagobject) · [`CreatePed`](#createped) · [`CreatePedInsideVehicle`](#createpedinsidevehicle) · [`CreateRandomPed`](#createrandomped) · [`CreateRandomPedAsDriver`](#createrandompedasdriver) · [`CreateSynchronizedScene`](#createsynchronizedscene) · [`CreateSynchronizedScene_2`](#createsynchronizedscene_2) · [`DeletePed`](#deleteped) · [`DetachSynchronizedScene`](#detachsynchronizedscene) · [`DisableHeadBlendPaletteColor`](#disableheadblendpalettecolor) · [`DisablePedHeatscaleOverride`](#disablepedheatscaleoverride) · [`DoesGroupExist`](#doesgroupexist) · [`DoesRelationshipGroupExist`](#doesrelationshipgroupexist) · [`DoesScenarioBlockingAreaExist`](#doesscenarioblockingareaexist) · [`DropAmbientProp`](#dropambientprop) · [`ExplodePedHead`](#explodepedhead) · [`FinalizeHeadBlend`](#finalizeheadblend) · [`ForcePedAiAndAnimationUpdate`](#forcepedaiandanimationupdate) · [`ForcePedMotionState`](#forcepedmotionstate) · [`ForcePedToOpenParachute`](#forcepedtoopenparachute) · [`FreezePedCameraRotation`](#freezepedcamerarotation) · [`GetAnimInitialOffsetPosition`](#getaniminitialoffsetposition) · [`GetAnimInitialOffsetRotation`](#getaniminitialoffsetrotation) · [`GetClosestPed`](#getclosestped) · [`GetCombatFloat`](#getcombatfloat) · [`GetDeadPedPickupCoords`](#getdeadpedpickupcoords) · [`GetGroupSize`](#getgroupsize) · [`GetJackTarget`](#getjacktarget) · [`GetMeleeTargetForPed`](#getmeleetargetforped) · [`GetMount`](#getmount) · [`GetNumHairColors`](#getnumhaircolors) · [`GetNumMakeupColors`](#getnummakeupcolors) · [`GetNumberOfPedDrawableVariations`](#getnumberofpeddrawablevariations) · [`GetNumberOfPedPropDrawableVariations`](#getnumberofpedpropdrawablevariations) · [`GetNumberOfPedPropTextureVariations`](#getnumberofpedproptexturevariations) · [`GetNumberOfPedTextureVariations`](#getnumberofpedtexturevariations) · [`GetPedAccuracy`](#getpedaccuracy) · [`GetPedAlertness`](#getpedalertness) · [`GetPedArmour`](#getpedarmour) · [`GetPedAsGroupLeader`](#getpedasgroupleader) · [`GetPedAsGroupMember`](#getpedasgroupmember) · [`GetPedBoneCoords`](#getpedbonecoords) · [`GetPedBoneIndex`](#getpedboneindex) · [`GetPedCauseOfDeath`](#getpedcauseofdeath) · [`GetPedCombatMovement`](#getpedcombatmovement) · [`GetPedCombatRange`](#getpedcombatrange) · [`GetPedConfigFlag`](#getpedconfigflag) · [`GetPedCurrentMovementSpeed`](#getpedcurrentmovementspeed) · [`GetPedDecorationZoneFromHashes`](#getpeddecorationzonefromhashes) · [`GetPedDecorationsState`](#getpeddecorationsstate) · [`GetPedDefensiveAreaPosition`](#getpeddefensiveareaposition) · [`GetPedDiesInWater`](#getpeddiesinwater) · [`GetPedDrawableVariation`](#getpeddrawablevariation) · [`GetPedEmissiveIntensity`](#getpedemissiveintensity) · [`GetPedEnveffScale`](#getpedenveffscale) · [`GetPedEventData`](#getpedeventdata) · [`GetPedExtractedDisplacement`](#getpedextracteddisplacement) · [`GetPedEyeColor`](#getpedeyecolor) · [`GetPedGroupIndex`](#getpedgroupindex) · [`GetPedHairRgbColor`](#getpedhairrgbcolor) · [`GetPedHeadBlendData`](#getpedheadblenddata) · [`GetPedHeadBlendFirstIndex`](#getpedheadblendfirstindex) · [`GetPedHeadBlendNumHeads`](#getpedheadblendnumheads) · [`GetPedHeadOverlayNum`](#getpedheadoverlaynum) · [`GetPedHeadOverlayValue`](#getpedheadoverlayvalue) · [`GetPedHelmetStoredHatPropIndex`](#getpedhelmetstoredhatpropindex) · [`GetPedHelmetStoredHatTexIndex`](#getpedhelmetstoredhattexindex) · [`GetPedLastDamageBone`](#getpedlastdamagebone) · [`GetPedMakeupRgbColor`](#getpedmakeuprgbcolor) · [`GetPedMaxHealth`](#getpedmaxhealth) · [`GetPedMoney`](#getpedmoney) · [`GetPedNearbyPeds`](#getpednearbypeds) · [`GetPedNearbyVehicles`](#getpednearbyvehicles) · [`GetPedPaletteVariation`](#getpedpalettevariation) · [`GetPedParachuteLandingType`](#getpedparachutelandingtype) · [`GetPedParachuteState`](#getpedparachutestate) · [`GetPedParachuteTintIndex`](#getpedparachutetintindex) · [`GetPedPropIndex`](#getpedpropindex) · [`GetPedPropTextureIndex`](#getpedproptextureindex) · [`GetPedRagdollBoneIndex`](#getpedragdollboneindex) · [`GetPedRelationshipGroupDefaultHash`](#getpedrelationshipgroupdefaulthash) · [`GetPedRelationshipGroupHash`](#getpedrelationshipgrouphash) · [`GetPedResetFlag`](#getpedresetflag) · [`GetPedSourceOfDeath`](#getpedsourceofdeath) · [`GetPedStealthMovement`](#getpedstealthmovement) · [`GetPedTaskCombatTarget`](#getpedtaskcombattarget) · [`GetPedTextureVariation`](#getpedtexturevariation) · [`GetPedTimeOfDeath`](#getpedtimeofdeath) · [`GetPedType`](#getpedtype) · [`GetPedVisualFieldCenterAngle`](#getpedvisualfieldcenterangle) · [`GetPedheadshotTxdString`](#getpedheadshottxdstring) · [`GetPedsJacker`](#getpedsjacker) · [`GetPlayerPedIsFollowing`](#getplayerpedisfollowing) · [`GetRandomPedAtCoord`](#getrandompedatcoord) · [`GetRelationshipBetweenGroups`](#getrelationshipbetweengroups) · [`GetRelationshipBetweenPeds`](#getrelationshipbetweenpeds) · [`GetSeatPedIsTryingToEnter`](#getseatpedistryingtoenter) · [`GetSynchronizedScenePhase`](#getsynchronizedscenephase) · [`GetSynchronizedSceneRate`](#getsynchronizedscenerate) · [`GetTimeOfLastPedWeaponDamage`](#gettimeoflastpedweapondamage) · [`GetVehiclePedIsEntering`](#getvehiclepedisentering) · [`GetVehiclePedIsIn`](#getvehiclepedisin) · [`GetVehiclePedIsTryingToEnter`](#getvehiclepedistryingtoenter) · [`GetVehiclePedIsUsing`](#getvehiclepedisusing) · [`GivePedHelmet`](#givepedhelmet) · [`GivePedNmMessage`](#givepednmmessage) · [`HasActionModeAssetLoaded`](#hasactionmodeassetloaded) · [`HasPedHeadBlendFinished`](#haspedheadblendfinished) · [`HasPedPreloadPropDataFinished`](#haspedpreloadpropdatafinished) · [`HasPedPreloadVariationDataFinished`](#haspedpreloadvariationdatafinished) · [`HasPedReceivedEvent`](#haspedreceivedevent) · [`HasPedheadshotImgUploadFailed`](#haspedheadshotimguploadfailed) · [`HasPedheadshotImgUploadSucceeded`](#haspedheadshotimguploadsucceeded) · [`HasStealthModeAssetLoaded`](#hasstealthmodeassetloaded) · [`HaveAllStreamingRequestsCompleted`](#haveallstreamingrequestscompleted) · [`HidePedBloodDamageByZone`](#hidepedblooddamagebyzone) · [`InstantlyFillPedPopulation`](#instantlyfillpedpopulation) · [`IsAnyHostilePedNearPoint`](#isanyhostilepednearpoint) · [`IsAnyPedNearPoint`](#isanypednearpoint) · [`IsAnyPedShootingInArea`](#isanypedshootinginarea) · [`IsConversationPedDead`](#isconversationpeddead) · [`IsCopPedInArea_3d`](#iscoppedinarea_3d) · [`IsPedAPlayer`](#ispedaplayer) · [`IsPedAimingFromCover`](#ispedaimingfromcover) · [`IsPedBeingJacked`](#ispedbeingjacked) · [`IsPedBeingStealthKilled`](#ispedbeingstealthkilled) · [`IsPedBeingStunned`](#ispedbeingstunned) · [`IsPedBlushColorValid`](#ispedblushcolorvalid) · [`IsPedBlushColorValid_2`](#ispedblushcolorvalid_2) · [`IsPedBodyBlemishValid`](#ispedbodyblemishvalid) · [`IsPedClimbing`](#ispedclimbing) · [`IsPedComponentVariationValid`](#ispedcomponentvariationvalid) · [`IsPedDeadOrDying`](#ispeddeadordying) · [`IsPedDefensiveAreaActive`](#ispeddefensiveareaactive) · [`IsPedDiving`](#ispeddiving) · [`IsPedDoingBeastJump`](#ispeddoingbeastjump) · [`IsPedDoingDriveby`](#ispeddoingdriveby) · [`IsPedDucking`](#ispedducking) · [`IsPedEvasiveDiving`](#ispedevasivediving) · [`IsPedFacingPed`](#ispedfacingped) · [`IsPedFalling`](#ispedfalling) · [`IsPedFatallyInjured`](#ispedfatallyinjured) · [`IsPedFleeing`](#ispedfleeing) · [`IsPedGettingIntoAVehicle`](#ispedgettingintoavehicle) · [`IsPedGoingIntoCover`](#ispedgoingintocover) · [`IsPedGroupMember`](#ispedgroupmember) · [`IsPedHairColorValid`](#ispedhaircolorvalid) · [`IsPedHairColorValid_2`](#ispedhaircolorvalid_2) · [`IsPedHangingOnToVehicle`](#ispedhangingontovehicle) · [`IsPedHeadingTowardsPosition`](#ispedheadingtowardsposition) · [`IsPedHeadtrackingEntity`](#ispedheadtrackingentity) · [`IsPedHeadtrackingPed`](#ispedheadtrackingped) · [`IsPedHelmetUnk`](#ispedhelmetunk) · [`IsPedHuman`](#ispedhuman) · [`IsPedHurt`](#ispedhurt) · [`IsPedInAnyBoat`](#ispedinanyboat) · [`IsPedInAnyHeli`](#ispedinanyheli) · [`IsPedInAnyPlane`](#ispedinanyplane) · [`IsPedInAnyPoliceVehicle`](#ispedinanypolicevehicle) · [`IsPedInAnySub`](#ispedinanysub) · [`IsPedInAnyTaxi`](#ispedinanytaxi) · [`IsPedInAnyTrain`](#ispedinanytrain) · [`IsPedInAnyVehicle`](#ispedinanyvehicle) · [`IsPedInCombat`](#ispedincombat) · [`IsPedInCover`](#ispedincover) · [`IsPedInCoverFacingLeft`](#ispedincoverfacingleft) · [`IsPedInFlyingVehicle`](#ispedinflyingvehicle) · [`IsPedInGroup`](#ispedingroup) · [`IsPedInHighCover`](#ispedinhighcover) · [`IsPedInMeleeCombat`](#ispedinmeleecombat) · [`IsPedInModel`](#ispedinmodel) · [`IsPedInParachuteFreeFall`](#ispedinparachutefreefall) · [`IsPedInSphereAreaOfAnyEnemyPeds`](#ispedinsphereareaofanyenemypeds) · [`IsPedInVehicle`](#ispedinvehicle) · [`IsPedInjured`](#ispedinjured) · [`IsPedJacking`](#ispedjacking) · [`IsPedJumping`](#ispedjumping) · [`IsPedJumpingOutOfVehicle`](#ispedjumpingoutofvehicle) · [`IsPedLipstickColorValid`](#ispedlipstickcolorvalid) · [`IsPedLipstickColorValid_2`](#ispedlipstickcolorvalid_2) · [`IsPedMale`](#ispedmale) · [`IsPedModel`](#ispedmodel) · [`IsPedOnAnyBike`](#ispedonanybike) · [`IsPedOnFoot`](#ispedonfoot) · [`IsPedOnMount`](#ispedonmount) · [`IsPedOnSpecificVehicle`](#ispedonspecificvehicle) · [`IsPedOnVehicle`](#ispedonvehicle) · [`IsPedOpeningADoor`](#ispedopeningadoor) · [`IsPedPerformingDependentComboLimit`](#ispedperformingdependentcombolimit) · [`IsPedPerformingMeleeAction`](#ispedperformingmeleeaction) · [`IsPedPerformingStealthKill`](#ispedperformingstealthkill) · [`IsPedPlantingBomb`](#ispedplantingbomb) · [`IsPedProne`](#ispedprone) · [`IsPedRagdoll`](#ispedragdoll) · [`IsPedReloading`](#ispedreloading) · [`IsPedRespondingToEvent`](#ispedrespondingtoevent) · [`IsPedRunningMeleeTask`](#ispedrunningmeleetask) · [`IsPedRunningMobilePhoneTask`](#ispedrunningmobilephonetask) · [`IsPedRunningRagdollTask`](#ispedrunningragdolltask) · [`IsPedShaderEffectValid`](#ispedshadereffectvalid) · [`IsPedSheltered`](#ispedsheltered) · [`IsPedShooting`](#ispedshooting) · [`IsPedShootingInArea`](#ispedshootinginarea) · [`IsPedSittingInAnyVehicle`](#ispedsittinginanyvehicle) · [`IsPedSittingInVehicle`](#ispedsittinginvehicle) · [`IsPedStopped`](#ispedstopped) · [`IsPedSwappingWeapon`](#ispedswappingweapon) · [`IsPedSwimming`](#ispedswimming) · [`IsPedSwimmingUnderWater`](#ispedswimmingunderwater) · [`IsPedTakingOffHelmet`](#ispedtakingoffhelmet) · [`IsPedTracked`](#ispedtracked) · [`IsPedTryingToEnterALockedVehicle`](#ispedtryingtoenteralockedvehicle) · [`IsPedUsingActionMode`](#ispedusingactionmode) · [`IsPedUsingAnyScenario`](#ispedusinganyscenario) · [`IsPedUsingScenario`](#ispedusingscenario) · [`IsPedVaulting`](#ispedvaulting) · [`IsPedWearingHelmet`](#ispedwearinghelmet) · [`IsPedheadshotImgUploadAvailable`](#ispedheadshotimguploadavailable) · [`IsPedheadshotReady`](#ispedheadshotready) · [`IsPedheadshotValid`](#ispedheadshotvalid) · [`IsScriptedScenarioPedUsingConditionalAnim`](#isscriptedscenariopedusingconditionalanim) · [`IsScubaGearLightEnabled`](#isscubagearlightenabled) · [`IsSynchronizedSceneHoldLastFrame`](#issynchronizedsceneholdlastframe) · [`IsSynchronizedSceneLooped`](#issynchronizedscenelooped) · [`IsSynchronizedSceneRunning`](#issynchronizedscenerunning) · [`IsTrackedPedVisible`](#istrackedpedvisible) · [`KnockOffPedProp`](#knockoffpedprop) · [`KnockPedOffVehicle`](#knockpedoffvehicle) · [`N_0x03ea03af85a85cb7`](#n_0x03ea03af85a85cb7) · [`N_0x06087579e7aa85a9`](#n_0x06087579e7aa85a9) · [`N_0x061cb768363d6424`](#n_0x061cb768363d6424) · [`N_0x0b3e35ac043707d9`](#n_0x0b3e35ac043707d9) · [`N_0x0f62619393661d6e`](#n_0x0f62619393661d6e) · [`N_0x110f526ab784111f`](#n_0x110f526ab784111f) · [`N_0x1216e0bfa72cc703`](#n_0x1216e0bfa72cc703) · [`N_0x1a330d297aac6bc1`](#n_0x1a330d297aac6bc1) · [`N_0x1e77fa7a62ee6c4c`](#n_0x1e77fa7a62ee6c4c) · [`N_0x2016c603d6b8987c`](#n_0x2016c603d6b8987c) · [`N_0x25361a96e0f7e419`](#n_0x25361a96e0f7e419) · [`N_0x2735233a786b1bef`](#n_0x2735233a786b1bef) · [`N_0x288df530c92dad6f`](#n_0x288df530c92dad6f) · [`N_0x2b694afcf64e6994`](#n_0x2b694afcf64e6994) · [`N_0x2dfc81c9b9608549`](#n_0x2dfc81c9b9608549) · [`N_0x2f074c904d85129e`](#n_0x2f074c904d85129e) · [`N_0x2f3c3d9f50681de4`](#n_0x2f3c3d9f50681de4) · [`N_0x336b3d200ab007cb`](#n_0x336b3d200ab007cb) · [`N_0x3e9679c1dfcf422c`](#n_0x3e9679c1dfcf422c) · [`N_0x412f1364fa066cfb`](#n_0x412f1364fa066cfb) · [`N_0x425aecf167663f48`](#n_0x425aecf167663f48) · [`N_0x46b05bcae43856b0`](#n_0x46b05bcae43856b0) · [`N_0x49e50bdb8ba4dab2`](#n_0x49e50bdb8ba4dab2) · [`N_0x511f1a683387c7e2`](#n_0x511f1a683387c7e2) · [`N_0x5407b7288d0478b7`](#n_0x5407b7288d0478b7) · [`N_0x5a7f62fda59759bd`](#n_0x5a7f62fda59759bd) · [`N_0x5b6010b3cbc29095`](#n_0x5b6010b3cbc29095) · [`N_0x711794453cfd692b`](#n_0x711794453cfd692b) · [`N_0x733c87d4ce22bea2`](#n_0x733c87d4ce22bea2) · [`N_0x75ba1cb3b7d40caf`](#n_0x75ba1cb3b7d40caf) · [`N_0x80054d7fcc70eec6`](#n_0x80054d7fcc70eec6) · [`N_0x820e9892a77e97cd`](#n_0x820e9892a77e97cd) · [`N_0x87ddeb611b329a9c`](#n_0x87ddeb611b329a9c) · [`N_0x9911f4a24485f653`](#n_0x9911f4a24485f653) · [`N_0x9a77dfd295e29b09`](#n_0x9a77dfd295e29b09) · [`N_0x9c6a6c19b6c0c496`](#n_0x9c6a6c19b6c0c496) · [`N_0x9e30e91fb03a2caf`](#n_0x9e30e91fb03a2caf) · [`N_0xa3f3564a5b3646c0`](#n_0xa3f3564a5b3646c0) · [`N_0xa52d5247a4227e14`](#n_0xa52d5247a4227e14) · [`N_0xa660faf550eb37e5`](#n_0xa660faf550eb37e5) · [`N_0xa9b61a329bfdcbea`](#n_0xa9b61a329bfdcbea) · [`N_0xaaa6a3698a69e048`](#n_0xaaa6a3698a69e048) · [`N_0xad27d957598e49e9`](#n_0xad27d957598e49e9) · [`N_0xafc976fd0580c7b3`](#n_0xafc976fd0580c7b3) · [`N_0xb282749d5e028163`](#n_0xb282749d5e028163) · [`N_0xb3352e018d6f89df`](#n_0xb3352e018d6f89df) · [`N_0xc2ee020f5fb4db53`](#n_0xc2ee020f5fb4db53) · [`N_0xc30bdaee47256c13`](#n_0xc30bdaee47256c13) · [`N_0xc56fbf2f228e1dac`](#n_0xc56fbf2f228e1dac) · [`N_0xcd018c591f94cb43`](#n_0xcd018c591f94cb43) · [`N_0xceda60a74219d064`](#n_0xceda60a74219d064) · [`N_0xd33daa36272177c4`](#n_0xd33daa36272177c4) · [`N_0xdfe68c4b787e1bfb`](#n_0xdfe68c4b787e1bfb) · [`N_0xe906ec930f5fe7c8`](#n_0xe906ec930f5fe7c8) · [`N_0xea9960d07dadcf10`](#n_0xea9960d07dadcf10) · [`N_0xec4b4b3b9908052a`](#n_0xec4b4b3b9908052a) · [`N_0xed3c76adfa6d07c4`](#n_0xed3c76adfa6d07c4) · [`N_0xf033419d1b81fae8`](#n_0xf033419d1b81fae8) · [`N_0xf2385935bffd4d92`](#n_0xf2385935bffd4d92) · [`N_0xf2bebcdfafdaa19e`](#n_0xf2bebcdfafdaa19e) · [`N_0xfab944d4d481accb`](#n_0xfab944d4d481accb) · [`N_0xfd325494792302d7`](#n_0xfd325494792302d7) · [`N_0xfec9a3b1820f3331`](#n_0xfec9a3b1820f3331) · [`N_0xff4803bc019852d9`](#n_0xff4803bc019852d9) · [`PlayFacialAnim`](#playfacialanim) · [`RegisterHatedTargetsAroundPed`](#registerhatedtargetsaroundped) · [`RegisterPedheadshot`](#registerpedheadshot) · [`RegisterPedheadshotTransparent`](#registerpedheadshottransparent) · [`RegisterPedheadshot_3`](#registerpedheadshot_3) · [`RegisterTarget`](#registertarget) · [`ReleasePedPreloadPropData`](#releasepedpreloadpropdata) · [`ReleasePedPreloadVariationData`](#releasepedpreloadvariationdata) · [`ReleasePedheadshotImgUpload`](#releasepedheadshotimgupload) · [`RemoveActionModeAsset`](#removeactionmodeasset) · [`RemoveGroup`](#removegroup) · [`RemovePedDefensiveArea`](#removepeddefensivearea) · [`RemovePedElegantly`](#removepedelegantly) · [`RemovePedFromGroup`](#removepedfromgroup) · [`RemovePedHelmet`](#removepedhelmet) · [`RemovePedPreferredCoverSet`](#removepedpreferredcoverset) · [`RemoveRelationshipGroup`](#removerelationshipgroup) · [`RemoveScenarioBlockingArea`](#removescenarioblockingarea) · [`RemoveScenarioBlockingAreas`](#removescenarioblockingareas) · [`RemoveStealthModeAsset`](#removestealthmodeasset) · [`RequestActionModeAsset`](#requestactionmodeasset) · [`RequestPedVehicleVisibilityTracking`](#requestpedvehiclevisibilitytracking) · [`RequestPedVisibilityTracking`](#requestpedvisibilitytracking) · [`RequestPedheadshotImgUpload`](#requestpedheadshotimgupload) · [`RequestStealthModeAsset`](#requeststealthmodeasset) · [`ResetAiMeleeWeaponDamageModifier`](#resetaimeleeweapondamagemodifier) · [`ResetAiWeaponDamageModifier`](#resetaiweapondamagemodifier) · [`ResetGroupFormationDefaultSpacing`](#resetgroupformationdefaultspacing) · [`ResetPedInVehicleContext`](#resetpedinvehiclecontext) · [`ResetPedLastVehicle`](#resetpedlastvehicle) · [`ResetPedMovementClipset`](#resetpedmovementclipset) · [`ResetPedRagdollTimer`](#resetpedragdolltimer) · [`ResetPedStrafeClipset`](#resetpedstrafeclipset) · [`ResetPedVisibleDamage`](#resetpedvisibledamage) · [`ResetPedWeaponMovementClipset`](#resetpedweaponmovementclipset) · [`ResurrectPed`](#resurrectped) · [`ReviveInjuredPed`](#reviveinjuredped) · [`SetAiMeleeWeaponDamageModifier`](#setaimeleeweapondamagemodifier) · [`SetAiWeaponDamageModifier`](#setaiweapondamagemodifier) · [`SetAmbientPedsDropMoney`](#setambientpedsdropmoney) · [`SetBlockAmbientPedsFromDroppingWeaponsThisFrame`](#setblockambientpedsfromdroppingweaponsthisframe) · [`SetBlockingOfNonTemporaryEvents`](#setblockingofnontemporaryevents) · [`SetCanAttackFriendly`](#setcanattackfriendly) · [`SetCombatFloat`](#setcombatfloat) · [`SetCreateRandomCops`](#setcreaterandomcops) · [`SetCreateRandomCopsNotOnScenarios`](#setcreaterandomcopsnotonscenarios) · [`SetCreateRandomCopsOnScenarios`](#setcreaterandomcopsonscenarios) · [`SetDriverAbility`](#setdriverability) · [`SetDriverAggressiveness`](#setdriveraggressiveness) · [`SetDriverRacingModifier`](#setdriverracingmodifier) · [`SetEnableBoundAnkles`](#setenableboundankles) · [`SetEnableHandcuffs`](#setenablehandcuffs) · [`SetEnablePedEnveffScale`](#setenablepedenveffscale) · [`SetEnableScuba`](#setenablescuba) · [`SetEnableScubaGearLight`](#setenablescubagearlight) · [`SetFacialClipsetOverride`](#setfacialclipsetoverride) · [`SetFacialIdleAnimOverride`](#setfacialidleanimoverride) · [`SetForceFootstepUpdate`](#setforcefootstepupdate) · [`SetForceStepType`](#setforcesteptype) · [`SetGroupFormation`](#setgroupformation) · [`SetGroupFormationSpacing`](#setgroupformationspacing) · [`SetGroupSeparationRange`](#setgroupseparationrange) · [`SetHeadBlendPaletteColor`](#setheadblendpalettecolor) · [`SetIkTarget`](#setiktarget) · [`SetMovementModeOverride`](#setmovementmodeoverride) · [`SetPedAccuracy`](#setpedaccuracy) · [`SetPedAlertness`](#setpedalertness) · [`SetPedAllowVehiclesOverride`](#setpedallowvehiclesoverride) · [`SetPedAllowedToDuck`](#setpedallowedtoduck) · [`SetPedAlternateMovementAnim`](#setpedalternatemovementanim) · [`SetPedAlternateWalkAnim`](#setpedalternatewalkanim) · [`SetPedAngledDefensiveArea`](#setpedangleddefensivearea) · [`SetPedAoBlobRendering`](#setpedaoblobrendering) · [`SetPedArmour`](#setpedarmour) · [`SetPedAsCop`](#setpedascop) · [`SetPedAsEnemy`](#setpedasenemy) · [`SetPedAsGroupLeader`](#setpedasgroupleader) · [`SetPedAsGroupMember`](#setpedasgroupmember) · [`SetPedBlendFromParents`](#setpedblendfromparents) · [`SetPedBlocksPathingWhenDead`](#setpedblockspathingwhendead) · [`SetPedBoundsOrientation`](#setpedboundsorientation) · [`SetPedCanArmIk`](#setpedcanarmik) · [`SetPedCanBeDraggedOut`](#setpedcanbedraggedout) · [`SetPedCanBeKnockedOffVehicle`](#setpedcanbeknockedoffvehicle) · [`SetPedCanBeShotInVehicle`](#setpedcanbeshotinvehicle) · [`SetPedCanBeTargetedWhenInjured`](#setpedcanbetargetedwheninjured) · [`SetPedCanBeTargetedWithoutLos`](#setpedcanbetargetedwithoutlos) · [`SetPedCanBeTargetted`](#setpedcanbetargetted) · [`SetPedCanBeTargettedByPlayer`](#setpedcanbetargettedbyplayer) · [`SetPedCanBeTargettedByTeam`](#setpedcanbetargettedbyteam) · [`SetPedCanCowerInCover`](#setpedcancowerincover) · [`SetPedCanEvasiveDive`](#setpedcanevasivedive) · [`SetPedCanHeadIk`](#setpedcanheadik) · [`SetPedCanLegIk`](#setpedcanlegik) · [`SetPedCanLosePropsOnDamage`](#setpedcanlosepropsondamage) · [`SetPedCanPeekInCover`](#setpedcanpeekincover) · [`SetPedCanPlayAmbientAnims`](#setpedcanplayambientanims) · [`SetPedCanPlayAmbientBaseAnims`](#setpedcanplayambientbaseanims) · [`SetPedCanPlayGestureAnims`](#setpedcanplaygestureanims) · [`SetPedCanPlayInjuredAnims`](#setpedcanplayinjuredanims) · [`SetPedCanPlayVisemeAnims`](#setpedcanplayvisemeanims) · [`SetPedCanRagdoll`](#setpedcanragdoll) · [`SetPedCanRagdollFromPlayerImpact`](#setpedcanragdollfromplayerimpact) · [`SetPedCanSmashGlass`](#setpedcansmashglass) · [`SetPedCanSwitchWeapon`](#setpedcanswitchweapon) · [`SetPedCanTeleportToGroupLeader`](#setpedcanteleporttogroupleader) · [`SetPedCanTorsoIk`](#setpedcantorsoik) · [`SetPedCanTorsoReactIk`](#setpedcantorsoreactik) · [`SetPedCanTorsoVehicleIk`](#setpedcantorsovehicleik) · [`SetPedCanUseAutoConversationLookat`](#setpedcanuseautoconversationlookat) · [`SetPedCapsule`](#setpedcapsule) · [`SetPedClothPackageIndex`](#setpedclothpackageindex) · [`SetPedClothProne`](#setpedclothprone) · [`SetPedCombatAbility`](#setpedcombatability) · [`SetPedCombatAttributes`](#setpedcombatattributes) · [`SetPedCombatMovement`](#setpedcombatmovement) · [`SetPedCombatRange`](#setpedcombatrange) · [`SetPedComponentVariation`](#setpedcomponentvariation) · [`SetPedConfigFlag`](#setpedconfigflag) · [`SetPedCoordsKeepVehicle`](#setpedcoordskeepvehicle) · [`SetPedCoordsNoGang`](#setpedcoordsnogang) · [`SetPedCoverClipsetOverride`](#setpedcoverclipsetoverride) · [`SetPedCowerHash`](#setpedcowerhash) · [`SetPedDefaultComponentVariation`](#setpeddefaultcomponentvariation) · [`SetPedDefensiveAreaAttachedToPed`](#setpeddefensiveareaattachedtoped) · [`SetPedDefensiveAreaDirection`](#setpeddefensiveareadirection) · [`SetPedDefensiveSphereAttachedToPed`](#setpeddefensivesphereattachedtoped) · [`SetPedDefensiveSphereAttachedToVehicle`](#setpeddefensivesphereattachedtovehicle) · [`SetPedDensityMultiplierThisFrame`](#setpeddensitymultiplierthisframe) · [`SetPedDesiredHeading`](#setpeddesiredheading) · [`SetPedDiesInSinkingVehicle`](#setpeddiesinsinkingvehicle) · [`SetPedDiesInVehicle`](#setpeddiesinvehicle) · [`SetPedDiesInWater`](#setpeddiesinwater) · [`SetPedDiesInstantlyInWater`](#setpeddiesinstantlyinwater) · [`SetPedDiesWhenInjured`](#setpeddieswheninjured) · [`SetPedDriveByClipsetOverride`](#setpeddrivebyclipsetoverride) · [`SetPedDucking`](#setpedducking) · [`SetPedEmissiveIntensity`](#setpedemissiveintensity) · [`SetPedEnableWeaponBlocking`](#setpedenableweaponblocking) · [`SetPedEnveffColorModulator`](#setpedenveffcolormodulator) · [`SetPedEnveffScale`](#setpedenveffscale) · [`SetPedEyeColor`](#setpedeyecolor) · [`SetPedFaceFeature`](#setpedfacefeature) · [`SetPedFiringPattern`](#setpedfiringpattern) · [`SetPedFleeAttributes`](#setpedfleeattributes) · [`SetPedGeneratesDeadBodyEvents`](#setpedgeneratesdeadbodyevents) · [`SetPedGestureGroup`](#setpedgesturegroup) · [`SetPedGetOutUpsideDownVehicle`](#setpedgetoutupsidedownvehicle) · [`SetPedGravity`](#setpedgravity) · [`SetPedGroupMemberPassengerIndex`](#setpedgroupmemberpassengerindex) · [`SetPedHairTint`](#setpedhairtint) · [`SetPedHeadBlendData`](#setpedheadblenddata) · [`SetPedHeadOverlay`](#setpedheadoverlay) · [`SetPedHeadOverlayColor`](#setpedheadoverlaycolor) · [`SetPedHearingRange`](#setpedhearingrange) · [`SetPedHeatscaleOverride`](#setpedheatscaleoverride) · [`SetPedHelmet`](#setpedhelmet) · [`SetPedHelmetFlag`](#setpedhelmetflag) · [`SetPedHelmetPropIndex`](#setpedhelmetpropindex) · [`SetPedHelmetTextureIndex`](#setpedhelmettextureindex) · [`SetPedHelmetUnk`](#setpedhelmetunk) · [`SetPedHighlyPerceptive`](#setpedhighlyperceptive) · [`SetPedIdRange`](#setpedidrange) · [`SetPedInVehicleContext`](#setpedinvehiclecontext) · [`SetPedIncreasedAvoidanceRadius`](#setpedincreasedavoidanceradius) · [`SetPedIntoVehicle`](#setpedintovehicle) · [`SetPedKeepTask`](#setpedkeeptask) · [`SetPedLegIkMode`](#setpedlegikmode) · [`SetPedLodMultiplier`](#setpedlodmultiplier) · [`SetPedMaxHealth`](#setpedmaxhealth) · [`SetPedMaxMoveBlendRatio`](#setpedmaxmoveblendratio) · [`SetPedMaxTimeInWater`](#setpedmaxtimeinwater) · [`SetPedMaxTimeUnderwater`](#setpedmaxtimeunderwater) · [`SetPedMinGroundTimeForStungun`](#setpedmingroundtimeforstungun) · [`SetPedMinMoveBlendRatio`](#setpedminmoveblendratio) · [`SetPedModelIsSuppressed`](#setpedmodelissuppressed) · [`SetPedMoney`](#setpedmoney) · [`SetPedMotionBlur`](#setpedmotionblur) · [`SetPedMoveAnimsBlendOut`](#setpedmoveanimsblendout) · [`SetPedMoveRateOverride`](#setpedmoverateoverride) · [`SetPedMovementClipset`](#setpedmovementclipset) · [`SetPedNameDebug`](#setpednamedebug) · [`SetPedNeverLeavesGroup`](#setpedneverleavesgroup) · [`SetPedNonCreationArea`](#setpednoncreationarea) · [`SetPedPanicExitScenario`](#setpedpanicexitscenario) · [`SetPedParachuteTintIndex`](#setpedparachutetintindex) · [`SetPedPhonePaletteIdx`](#setpedphonepaletteidx) · [`SetPedPinnedDown`](#setpedpinneddown) · [`SetPedPlaysHeadOnHornAnimWhenDiesInVehicle`](#setpedplaysheadonhornanimwhendiesinvehicle) · [`SetPedPreferredCoverSet`](#setpedpreferredcoverset) · [`SetPedPreloadPropData`](#setpedpreloadpropdata) · [`SetPedPreloadVariationData`](#setpedpreloadvariationdata) · [`SetPedPrimaryLookat`](#setpedprimarylookat) · [`SetPedPropIndex`](#setpedpropindex) · [`SetPedRagdollForceFall`](#setpedragdollforcefall) · [`SetPedRagdollOnCollision`](#setpedragdolloncollision) · [`SetPedRandomComponentVariation`](#setpedrandomcomponentvariation) · [`SetPedRandomProps`](#setpedrandomprops) · [`SetPedRelationshipGroupDefaultHash`](#setpedrelationshipgroupdefaulthash) · [`SetPedRelationshipGroupHash`](#setpedrelationshipgrouphash) · [`SetPedReserveParachuteTintIndex`](#setpedreserveparachutetintindex) · [`SetPedResetFlag`](#setpedresetflag) · [`SetPedScubaGearVariation`](#setpedscubagearvariation) · [`SetPedSeeingRange`](#setpedseeingrange) · [`SetPedShootRate`](#setpedshootrate) · [`SetPedShootsAtCoord`](#setpedshootsatcoord) · [`SetPedShouldPlayDirectedScenarioExit`](#setpedshouldplaydirectedscenarioexit) · [`SetPedShouldPlayFleeScenarioExit`](#setpedshouldplayfleescenarioexit) · [`SetPedShouldPlayImmediateScenarioExit`](#setpedshouldplayimmediatescenarioexit) · [`SetPedShouldPlayNormalScenarioExit`](#setpedshouldplaynormalscenarioexit) · [`SetPedSphereDefensiveArea`](#setpedspheredefensivearea) · [`SetPedStayInVehicleWhenJacked`](#setpedstayinvehiclewhenjacked) · [`SetPedStealthMovement`](#setpedstealthmovement) · [`SetPedSteersAroundObjects`](#setpedsteersaroundobjects) · [`SetPedSteersAroundPeds`](#setpedsteersaroundpeds) · [`SetPedSteersAroundVehicles`](#setpedsteersaroundvehicles) · [`SetPedStrafeClipset`](#setpedstrafeclipset) · [`SetPedSuffersCriticalHits`](#setpedsufferscriticalhits) · [`SetPedSurvivesBeingOutOfWater`](#setpedsurvivesbeingoutofwater) · [`SetPedSweat`](#setpedsweat) · [`SetPedTargetLossResponse`](#setpedtargetlossresponse) · [`SetPedToInformRespectedFriends`](#setpedtoinformrespectedfriends)

---
### AddArmourToPed

`ADD_ARMOUR_TO_PED` · hash `0x5BA652A0CD14DF2F` · jhash `0xF686B26E` · **Cliente**

```lua
AddArmourToPed(ped, amount)
```
```c
void ADD_ARMOUR_TO_PED(Ped ped, int amount);
```

**Parámetros**

- `ped` (`Ped`)
- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Same as SET_PED_ARMOUR, but ADDS 'amount' to the armor the Ped already has.  
```

---
### AddPedDecorationFromHashes

`ADD_PED_DECORATION_FROM_HASHES` · hash `0x5F5D1665E352A839` · jhash `0x70559AC7` · **Cliente · también en el servidor (RPC)**

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

**Nombres antiguos (alias):** `_APPLY_PED_OVERLAY` (`ApplyPedOverlay`), `_SET_PED_DECORATION` (`SetPedDecoration`)

---
### AddPedDecorationFromHashesInCorona

`ADD_PED_DECORATION_FROM_HASHES_IN_CORONA` · hash `0x5619BFA07CFD7833` · jhash `0x8CD3E487` · **Cliente**

```lua
AddPedDecorationFromHashesInCorona(ped, collection, overlay)
```
```c
void ADD_PED_DECORATION_FROM_HASHES_IN_CORONA(Ped ped, Hash collection, Hash overlay);
```

**Parámetros**

- `ped` (`Ped`)
- `collection` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `overlay` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5619BFA07CFD7833` (`N_0x5619bfa07cfd7833`), `_SET_PED_FACIAL_DECORATION` (`SetPedFacialDecoration`)

---
### AddRelationshipGroup

`ADD_RELATIONSHIP_GROUP` · hash `0xF372BC22FCB88606` · jhash `0x8B635546` · **Cliente**

```lua
local retval, groupHash = AddRelationshipGroup(name, groupHash)
```
```c
Any ADD_RELATIONSHIP_GROUP(char* name, Hash* groupHash);
```

**Parámetros**

- `name` (`char*`)
- `groupHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

**Descripción oficial:**

```
Can't select void. This function returns nothing. The hash of the created relationship group is output in the second parameter.  
```

---
### AddScenarioBlockingArea

`ADD_SCENARIO_BLOCKING_AREA` · hash `0x1B5C85C612E5256E` · jhash `0xA38C0234` · **Cliente**

```lua
local retval = AddScenarioBlockingArea(posMinX, posMinY, posMinZ, posMaxX, posMaxY, posMaxZ, network, cancelActive, blockPeds, blockVehicles)
```
```c
int ADD_SCENARIO_BLOCKING_AREA(float posMinX, float posMinY, float posMinZ, float posMaxX, float posMaxY, float posMaxZ, BOOL network, BOOL cancelActive, BOOL blockPeds, BOOL blockVehicles);
```

**Parámetros**

- `posMinX` (`float`): Min X Coordinate.
- `posMinY` (`float`): Min Y Coordinate.
- `posMinZ` (`float`): Min Z Coordinate.
- `posMaxX` (`float`): Max X Coordinate.
- `posMaxY` (`float`): Max Y Coordinate.
- `posMaxZ` (`float`): Max Z Coordinate.
- `network` (`BOOL`): Optionally networked to all other players
- `cancelActive` (`BOOL`): Should this cause peds already in active scenario points in the area specified to leave
- `blockPeds` (`BOOL`): if this area effects scenarios with peds
- `blockVehicles` (`BOOL`): if this area effects scenarios with vehicles

**Devuelve:** `int`

**Descripción oficial:**

Sets an area where scenarios are blocked

---
### ApplyDamageToPed

`APPLY_DAMAGE_TO_PED` · hash `0x697157CED63F18D4` · jhash `0x4DC27FCF` · **Cliente**

```lua
ApplyDamageToPed(ped, damageAmount, armorFirst)
```
```c
void APPLY_DAMAGE_TO_PED(Ped ped, int damageAmount, BOOL armorFirst);
```

**Parámetros**

- `ped` (`Ped`)
- `damageAmount` (`int`)
- `armorFirst` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
damages a ped with the given amount  
----  
armorFirst means it will damage/lower the armor first before damaging the player.  
setting damageAmount to a negative amount will cause the player or the armor (depending on armorFirst) to be healed by damageAmount instead.  
```

```
NativeDB Added Parameter 4: Any p3
```

---
### ApplyPedBlood

`APPLY_PED_BLOOD` · hash `0x83F7E01C7B769A26` · jhash `0x376CE3C0` · **Cliente**

```lua
ApplyPedBlood(ped, boneIndex, xRot, yRot, zRot, woundType)
```
```c
void APPLY_PED_BLOOD(Ped ped, int boneIndex, float xRot, float yRot, float zRot, char* woundType);
```

**Parámetros**

- `ped` (`Ped`)
- `boneIndex` (`int`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `woundType` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Found one occurence in re_crashrescue.c4  
PED::APPLY_PED_BLOOD(l_4B, 3, 0.0, 0.0, 0.0, "wound_sheet");  
```

---
### ApplyPedBloodByZone

`APPLY_PED_BLOOD_BY_ZONE` · hash `0x3311E47B91EDCBBC` · jhash `0x8F3F3A9C` · **Cliente**

```lua
local p4 = ApplyPedBloodByZone(ped, p1, p2, p3, p4)
```
```c
void APPLY_PED_BLOOD_BY_ZONE(Ped ped, Any p1, float p2, float p3, Any* p4);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3311E47B91EDCBBC` (`N_0x3311e47b91edcbbc`)

---
### ApplyPedBloodDamageByZone

`APPLY_PED_BLOOD_DAMAGE_BY_ZONE` · hash `0x816F6981C60BF53B` · jhash `0x1E54DB12` · **Cliente**

```lua
ApplyPedBloodDamageByZone(ped, p1, p2, p3, p4)
```
```c
void APPLY_PED_BLOOD_DAMAGE_BY_ZONE(Ped ped, Any p1, float p2, float p3, Any p4);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x816F6981C60BF53B` (`N_0x816f6981c60bf53b`)

---
### ApplyPedBloodSpecific

`APPLY_PED_BLOOD_SPECIFIC` · hash `0xEF0D582CBF2D9B0F` · jhash `0xFC13CE80` · **Cliente**

```lua
ApplyPedBloodSpecific(ped, component, u, v, rotation, scale, forcedFrame, preAge, bloodName)
```
```c
void APPLY_PED_BLOOD_SPECIFIC(Ped ped, int component, float u, float v, float rotation, float scale, int forcedFrame, float preAge, char* bloodName);
```

**Parámetros**

- `ped` (`Ped`): The Ped to which blood damage is applied.
- `component` (`int`): Specific component or body part.
- `u` (`float`): UV texture coordinates for placing the decal in the specified zone.
- `v` (`float`): UV texture coordinates for placing the decal in the specified zone.
- `rotation` (`float`): Angle in degrees for the rotation of the blood decal.
- `scale` (`float`): Scale factor for the damage, ranging from 0.0 to 1.0.
- `forcedFrame` (`int`): Allows a specific frame of damage to be chosen (-1 for random selection).
- `preAge` (`float`): Number of seconds to pre-age the damage for an "old wound" effect (0.0 for fresh wound).
- `bloodName` (`char*`): Name of the blood type, matching an entry in peddamage.xml.

**Devuelve:** `void`

**Descripción oficial:**

Applies blood damage to a ped with specific parameters for zone, UV offsets, rotation, scale, and initial aging.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xEF0D582CBF2D9B0F` (`N_0xef0d582cbf2d9b0f`)

---
### ApplyPedDamageDecal

`APPLY_PED_DAMAGE_DECAL` · hash `0x397C38AA7B4A5F83` · jhash `0x8A13A41F` · **Cliente**

```lua
ApplyPedDamageDecal(ped, damageZone, xOffset, yOffset, heading, scale, alpha, variation, fadeIn, decalName)
```
```c
void APPLY_PED_DAMAGE_DECAL(Ped ped, int damageZone, float xOffset, float yOffset, float heading, float scale, float alpha, int variation, BOOL fadeIn, char* decalName);
```

**Parámetros**

- `ped` (`Ped`)
- `damageZone` (`int`): Refer to `ePedDecorationZone` in [GET_PED_DECORATION_ZONE_FROM_HASHES](#getpeddecorationzonefromhashes)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `heading` (`float`)
- `scale` (`float`)
- `alpha` (`float`)
- `variation` (`int`)
- `fadeIn` (`BOOL`)
- `decalName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
scar
blushing
cs_flush_anger
cs_flush_anger_face
bruise
bruise_large
herpes
ArmorBullet
basic_dirt_cloth
basic_dirt_skin
cs_trev1_dirt
```

---
### ApplyPedDamagePack

`APPLY_PED_DAMAGE_PACK` · hash `0x46DF918788CB093F` · jhash `0x208D0CB8` · **Cliente**

```lua
ApplyPedDamagePack(ped, damagePack, damage, mult)
```
```c
void APPLY_PED_DAMAGE_PACK(Ped ped, char* damagePack, float damage, float mult);
```

**Parámetros**

- `ped` (`Ped`)
- `damagePack` (`char*`)
- `damage` (`float`)
- `mult` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Damage Packs:  
"SCR_TrevorTreeBang"  
"HOSPITAL_0"  
"HOSPITAL_1"  
"HOSPITAL_2"  
"HOSPITAL_3"  
"HOSPITAL_4"  
"HOSPITAL_5"  
"HOSPITAL_6"  
"HOSPITAL_7"  
"HOSPITAL_8"  
"HOSPITAL_9"  
"SCR_Dumpster"  
"BigHitByVehicle"  
"SCR_Finale_Michael_Face"  
"SCR_Franklin_finb"  
"SCR_Finale_Michael"  
"SCR_Franklin_finb2"  
"Explosion_Med"  
"SCR_Torture"  
"SCR_TracySplash"  
"Skin_Melee_0"  
Additional damage packs:  
gist.github.com/alexguirre/f3f47f75ddcf617f416f3c8a55ae2227  
```

---
### AttachSynchronizedSceneToEntity

`ATTACH_SYNCHRONIZED_SCENE_TO_ENTITY` · hash `0x272E4723B56A3B96` · jhash `0xE9BA6189` · **Cliente**

```lua
AttachSynchronizedSceneToEntity(sceneID, entity, boneIndex)
```
```c
void ATTACH_SYNCHRONIZED_SCENE_TO_ENTITY(int sceneID, Entity entity, int boneIndex);
```

**Parámetros**

- `sceneID` (`int`)
- `entity` (`Entity`)
- `boneIndex` (`int`)

**Devuelve:** `void`

---
### BlockPedDeadBodyShockingEvents

`_BLOCK_PED_DEAD_BODY_SHOCKING_EVENTS` · hash `0xE43A13C9E4CCCBCF` · jhash `0xFF1F6AEB` · **Cliente**

```lua
BlockPedDeadBodyShockingEvents(ped, toggle)
```
```c
void _BLOCK_PED_DEAD_BODY_SHOCKING_EVENTS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE43A13C9E4CCCBCF` (`N_0xe43a13c9e4cccbcf`)

---
### CanCreateRandomBikeRider

`CAN_CREATE_RANDOM_BIKE_RIDER` · hash `0xEACEEDA81751915C` · jhash `0x7018BE31` · **Cliente**

```lua
local retval = CanCreateRandomBikeRider()
```
```c
BOOL CAN_CREATE_RANDOM_BIKE_RIDER();
```

**Devuelve:** `BOOL`

---
### CanCreateRandomCops

`CAN_CREATE_RANDOM_COPS` · hash `0x5EE2CAFF7F17770D` · jhash `0xAA73DAD9` · **Cliente**

```lua
local retval = CanCreateRandomCops()
```
```c
BOOL CAN_CREATE_RANDOM_COPS();
```

**Devuelve:** `BOOL`

---
### CanCreateRandomDriver

`CAN_CREATE_RANDOM_DRIVER` · hash `0xB8EB95E5B4E56978` · jhash `0x99861609` · **Cliente**

```lua
local retval = CanCreateRandomDriver()
```
```c
BOOL CAN_CREATE_RANDOM_DRIVER();
```

**Devuelve:** `BOOL`

---
### CanCreateRandomPed

`CAN_CREATE_RANDOM_PED` · hash `0x3E8349C08E4B82E4` · jhash `0xF9ABE88F` · **Cliente**

```lua
local retval = CanCreateRandomPed(unk)
```
```c
BOOL CAN_CREATE_RANDOM_PED(BOOL unk);
```

**Parámetros**

- `unk` (`BOOL`)

**Devuelve:** `BOOL`

---
### CanKnockPedOffVehicle

`CAN_KNOCK_PED_OFF_VEHICLE` · hash `0x51AC07A44D4F5B8A` · jhash `0xC9D098B3` · **Cliente**

```lua
local retval = CanKnockPedOffVehicle(ped)
```
```c
BOOL CAN_KNOCK_PED_OFF_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### CanPedInCombatSeeTarget

`CAN_PED_IN_COMBAT_SEE_TARGET` · hash `0xEAD42DE3610D0721` · jhash `0xCCD525E1` · **Cliente**

```lua
local retval = CanPedInCombatSeeTarget(ped, target)
```
```c
BOOL CAN_PED_IN_COMBAT_SEE_TARGET(Ped ped, Ped target);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)

**Devuelve:** `BOOL`

---
### CanPedRagdoll

`CAN_PED_RAGDOLL` · hash `0x128F79EDCECE4FD5` · jhash `0xC0EFB7A3` · **Cliente**

```lua
local retval = CanPedRagdoll(ped)
```
```c
BOOL CAN_PED_RAGDOLL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Prevents the ped from going limp.  
[Example: Can prevent peds from falling when standing on moving vehicles.]  
```

---
### CanPedSeeHatedPed

`CAN_PED_SEE_HATED_PED` · hash `0x6CD5A433374D4CFB` · jhash `0x74A0F291` · **Cliente**

```lua
local retval = CanPedSeeHatedPed(ped1, ped2)
```
```c
BOOL CAN_PED_SEE_HATED_PED(Ped ped1, Ped ped2);
```

**Parámetros**

- `ped1` (`Ped`)
- `ped2` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6CD5A433374D4CFB` (`N_0x6cd5a433374d4cfb`), `_CAN_PED_SEE_PED` (`CanPedSeePed`)

---
### ClearAllPedProps

`CLEAR_ALL_PED_PROPS` · hash `0xCD8A7537A9B52F06` · jhash `0x81DF8B43` · **Cliente**

```lua
ClearAllPedProps(ped)
```
```c
void CLEAR_ALL_PED_PROPS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.

**Devuelve:** `void`

---
### ClearAllPedVehicleForcedSeatUsage

`CLEAR_ALL_PED_VEHICLE_FORCED_SEAT_USAGE` · hash `0xE6CA85E7259CE16B` · jhash `0xCC1D8F66` · **Cliente**

```lua
ClearAllPedVehicleForcedSeatUsage(ped)
```
```c
void CLEAR_ALL_PED_VEHICLE_FORCED_SEAT_USAGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE6CA85E7259CE16B` (`N_0xe6ca85e7259ce16b`)

---
### ClearFacialClipsetOverride

`_CLEAR_FACIAL_CLIPSET_OVERRIDE` · hash `0x637822DC2AFEEBF8` · **Cliente**

```lua
ClearFacialClipsetOverride(ped)
```
```c
void _CLEAR_FACIAL_CLIPSET_OVERRIDE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x637822DC2AFEEBF8` (`N_0x637822dc2afeebf8`)

---
### ClearFacialIdleAnimOverride

`CLEAR_FACIAL_IDLE_ANIM_OVERRIDE` · hash `0x726256CC1EEB182F` · jhash `0x5244F4E2` · **Cliente**

```lua
ClearFacialIdleAnimOverride(ped)
```
```c
void CLEAR_FACIAL_IDLE_ANIM_OVERRIDE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ClearPedAlternateMovementAnim

`CLEAR_PED_ALTERNATE_MOVEMENT_ANIM` · hash `0xD8D19675ED5FBDCE` · jhash `0x7A7F5BC3` · **Cliente**

```lua
ClearPedAlternateMovementAnim(ped, stance, p2)
```
```c
void CLEAR_PED_ALTERNATE_MOVEMENT_ANIM(Ped ped, int stance, float p2);
```

**Parámetros**

- `ped` (`Ped`)
- `stance` (`int`)
- `p2` (`float`)

**Devuelve:** `void`

---
### ClearPedAlternateWalkAnim

`CLEAR_PED_ALTERNATE_WALK_ANIM` · hash `0x8844BBFCE30AA9E9` · jhash `0x5736FB23` · **Cliente**

```lua
ClearPedAlternateWalkAnim(ped, p1)
```
```c
void CLEAR_PED_ALTERNATE_WALK_ANIM(Ped ped, float p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)

**Devuelve:** `void`

---
### ClearPedBloodDamage

`CLEAR_PED_BLOOD_DAMAGE` · hash `0x8FE22675A5A45817` · jhash `0xF7ADC960` · **Cliente**

```lua
ClearPedBloodDamage(ped)
```
```c
void CLEAR_PED_BLOOD_DAMAGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): Ped id.

**Devuelve:** `void`

**Descripción oficial:**

Clears the blood on a ped.

---
### ClearPedBloodDamageByZone

`CLEAR_PED_BLOOD_DAMAGE_BY_ZONE` · hash `0x56E3B78C5408D9F4` · jhash `0xF210BE69` · **Cliente**

```lua
ClearPedBloodDamageByZone(ped, p1)
```
```c
void CLEAR_PED_BLOOD_DAMAGE_BY_ZONE(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Somehow related to changing ped's clothes.  
```

**Nombres antiguos (alias):** `0x56E3B78C5408D9F4` (`N_0x56e3b78c5408d9f4`)

---
### ClearPedCoverClipsetOverride

`_CLEAR_PED_COVER_CLIPSET_OVERRIDE` · hash `0xC79196DCB36F6121` · **Cliente**

```lua
ClearPedCoverClipsetOverride(ped)
```
```c
void _CLEAR_PED_COVER_CLIPSET_OVERRIDE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
CLEAR_PED_*
```

**Nombres antiguos (alias):** `0xC79196DCB36F6121` (`N_0xc79196dcb36f6121`)

---
### ClearPedDamageDecalByZone

`CLEAR_PED_DAMAGE_DECAL_BY_ZONE` · hash `0x523C79AEEFCC4A2A` · jhash `0x70AA5B7D` · **Cliente**

```lua
ClearPedDamageDecalByZone(ped, p1, p2)
```
```c
void CLEAR_PED_DAMAGE_DECAL_BY_ZONE(Ped ped, int p1, char* p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)
- `p2` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1: from 0 to 5 in the b617d scripts.  
p2: "blushing" and "ALL" found in the b617d scripts.  
```

**Nombres antiguos (alias):** `0x523C79AEEFCC4A2A` (`N_0x523c79aeefcc4a2a`)

---
### ClearPedDecorations

`CLEAR_PED_DECORATIONS` · hash `0x0E5173C163976E38` · jhash `0xD4496BF3` · **Cliente**

```lua
ClearPedDecorations(ped)
```
```c
void CLEAR_PED_DECORATIONS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ClearPedDecorationsLeaveScars

`CLEAR_PED_DECORATIONS_LEAVE_SCARS` · hash `0xE3B27E70CEAB9F0C` · jhash `0xEFD58EB9` · **Cliente**

```lua
ClearPedDecorationsLeaveScars(ped)
```
```c
void CLEAR_PED_DECORATIONS_LEAVE_SCARS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE3B27E70CEAB9F0C` (`N_0xe3b27e70ceab9f0c`), `_CLEAR_PED_FACIAL_DECORATIONS` (`ClearPedFacialDecorations`)

---
### ClearPedDriveByClipsetOverride

`CLEAR_PED_DRIVE_BY_CLIPSET_OVERRIDE` · hash `0x4AFE3690D7E0B5AC` · jhash `0xAEC9163B` · **Cliente**

```lua
ClearPedDriveByClipsetOverride(ped)
```
```c
void CLEAR_PED_DRIVE_BY_CLIPSET_OVERRIDE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ClearPedEnvDirt

`CLEAR_PED_ENV_DIRT` · hash `0x6585D955A68452A5` · jhash `0xA993915F` · **Cliente**

```lua
ClearPedEnvDirt(ped)
```
```c
void CLEAR_PED_ENV_DIRT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6585D955A68452A5` (`N_0x6585d955a68452a5`)

---
### ClearPedLastDamageBone

`CLEAR_PED_LAST_DAMAGE_BONE` · hash `0x8EF6B7AC68E2F01B` · jhash `0x56CB715E` · **Cliente**

```lua
ClearPedLastDamageBone(ped)
```
```c
void CLEAR_PED_LAST_DAMAGE_BONE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ClearPedNonCreationArea

`CLEAR_PED_NON_CREATION_AREA` · hash `0x2E05208086BA0651` · jhash `0x6F7043A3` · **Cliente**

```lua
ClearPedNonCreationArea()
```
```c
void CLEAR_PED_NON_CREATION_AREA();
```

**Devuelve:** `void`

---
### ClearPedParachutePackVariation

`CLEAR_PED_PARACHUTE_PACK_VARIATION` · hash `0x1280804F7CFD2D6C` · jhash `0x7BCD8991` · **Cliente**

```lua
ClearPedParachutePackVariation(ped)
```
```c
void CLEAR_PED_PARACHUTE_PACK_VARIATION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1280804F7CFD2D6C` (`N_0x1280804f7cfd2d6c`)

---
### ClearPedProp

`CLEAR_PED_PROP` · hash `0x0943E5B8E078E76E` · jhash `0x2D23D743` · **Cliente · también en el servidor (RPC)**

```lua
ClearPedProp(ped, propId)
```
```c
void CLEAR_PED_PROP(Ped ped, int propId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `propId` (`int`): The prop id you want to clear from the ped. Refer to [SET_PED_PROP_INDEX](../cfx/servidor.md#setpedpropindex).

**Devuelve:** `void`

---
### ClearPedScubaGearVariation

`CLEAR_PED_SCUBA_GEAR_VARIATION` · hash `0xB50EB4CCB29704AC` · jhash `0x080275EE` · **Cliente**

```lua
ClearPedScubaGearVariation(ped)
```
```c
void CLEAR_PED_SCUBA_GEAR_VARIATION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped to remove the scuba gear from.

**Devuelve:** `void`

**Descripción oficial:**

Removes the scubagear (for mp male: component id: 8, drawableId: 123, textureId: any) from peds. Does not play the 'remove scuba gear' animation, but instantly removes it.

**Nombres antiguos (alias):** `0xB50EB4CCB29704AC` (`N_0xb50eb4ccb29704ac`), `_REMOVE_PED_SCUBA_GEAR_NOW` (`RemovePedScubaGearNow`)

---
### ClearPedStoredHatProp

`CLEAR_PED_STORED_HAT_PROP` · hash `0x687C0B594907D2E8` · jhash `0x24A1284E` · **Cliente**

```lua
ClearPedStoredHatProp(ped)
```
```c
void CLEAR_PED_STORED_HAT_PROP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x687C0B594907D2E8` (`N_0x687c0b594907d2e8`)

---
### ClearPedWetness

`CLEAR_PED_WETNESS` · hash `0x9C720776DAA43E7E` · jhash `0x629F15BD` · **Cliente**

```lua
ClearPedWetness(ped)
```
```c
void CLEAR_PED_WETNESS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
It clears the wetness of the selected Ped/Player. Clothes have to be wet to notice the difference.  
```

---
### ClearRagdollBlockingFlags

`CLEAR_RAGDOLL_BLOCKING_FLAGS` · hash `0xD86D101FCFD00A4B` · jhash `0x77CBA290` · **Cliente**

```lua
ClearRagdollBlockingFlags(ped, flags)
```
```c
void CLEAR_RAGDOLL_BLOCKING_FLAGS(Ped ped, int flags);
```

**Parámetros**

- `ped` (`Ped`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
There seem to be 26 flags  
```

**Nombres antiguos (alias):** `0xD86D101FCFD00A4B` (`N_0xd86d101fcfd00a4b`), `_RESET_PED_RAGDOLL_BLOCKING_FLAGS` (`ResetPedRagdollBlockingFlags`)

---
### ClearRelationshipBetweenGroups

`CLEAR_RELATIONSHIP_BETWEEN_GROUPS` · hash `0x5E29243FB56FC6D4` · jhash `0x994B8C2D` · **Cliente**

```lua
ClearRelationshipBetweenGroups(relationship, group1, group2)
```
```c
void CLEAR_RELATIONSHIP_BETWEEN_GROUPS(int relationship, Hash group1, Hash group2);
```

**Parámetros**

- `relationship` (`int`)
- `group1` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `group2` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Clears the relationship between two groups. This should be called twice (once for each group).  
Relationship types:  
0 = Companion  
1 = Respect  
2 = Like  
3 = Neutral  
4 = Dislike  
5 = Hate  
255 = Pedestrians  
(Credits: Inco)  
Example:  
PED::CLEAR_RELATIONSHIP_BETWEEN_GROUPS(2, l_1017, 0xA49E591C);  
PED::CLEAR_RELATIONSHIP_BETWEEN_GROUPS(2, 0xA49E591C, l_1017);  
```

---
### ClonePed

`CLONE_PED` · hash `0xEF29A16337FACADB` · jhash `0x8C8A8D6E` · **Cliente**

```lua
local retval = ClonePed(ped, isNetwork, bScriptHostPed, copyHeadBlendFlag)
```
```c
Ped CLONE_PED(Ped ped, BOOL isNetwork, BOOL bScriptHostPed, BOOL copyHeadBlendFlag);
```

**Parámetros**

- `ped` (`Ped`): The input ped.
- `isNetwork` (`BOOL`): Whether or not the ped should be registered as a network object.
- `bScriptHostPed` (`BOOL`): Script host flag.
- `copyHeadBlendFlag` (`BOOL`): If true, head blend data is referenced, not copied.

**Devuelve:** `Ped` — A new ped handle representing the ped's copy.

**Descripción oficial:**

Creates a copy of the passed ped, optionally setting it as local and/or shallow-copying the head blend data.

**Ejemplo (lua):**

```lua
-- makes a locally visible duplicate of the local player for presentation
local playerDummy = ClonePed(PlayerPedId(), false, false, true)
SetEntityCoords(playerDummy, pos.x, pos.y, pos.z)
```

---
### ClonePedEx

`_CLONE_PED_EX` · hash `0x668FD40BCBA5DE48` · **Cliente**

```lua
local retval = ClonePedEx(ped, heading, isNetwork, bScriptHostPed, p4)
```
```c
Ped _CLONE_PED_EX(Ped ped, float heading, BOOL isNetwork, BOOL bScriptHostPed, Any p4);
```

**Parámetros**

- `ped` (`Ped`)
- `heading` (`float`)
- `isNetwork` (`BOOL`)
- `bScriptHostPed` (`BOOL`)
- `p4` (`Any`)

**Devuelve:** `Ped`

**Descripción oficial:**

Used one time in fmmc_launcher.c instead of CLONE_PED because ?

**Nombres antiguos (alias):** `0x668FD40BCBA5DE48` (`N_0x668fd40bcba5de48`), `_CLONE_PED_2` (`ClonePed_2`)

---
### ClonePedToTarget

`CLONE_PED_TO_TARGET` · hash `0xE952D6431689AD9A` · jhash `0xFC70EEC7` · **Cliente**

```lua
ClonePedToTarget(ped, targetPed)
```
```c
void CLONE_PED_TO_TARGET(Ped ped, Ped targetPed);
```

**Parámetros**

- `ped` (`Ped`)
- `targetPed` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
Copies ped's components and props to targetPed.
```

**Nombres antiguos (alias):** `_ASSIGN_PLAYER_TO_PED` (`AssignPlayerToPed`)

---
### ClonePedToTargetEx

`_CLONE_PED_TO_TARGET_EX` · hash `0x148B08C2D2ACB884` · **Cliente**

```lua
ClonePedToTargetEx(ped, targetPed, p2)
```
```c
void _CLONE_PED_TO_TARGET_EX(Ped ped, Ped targetPed, Any p2);
```

**Parámetros**

- `ped` (`Ped`)
- `targetPed` (`Ped`)
- `p2` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x148B08C2D2ACB884` (`N_0x148b08c2d2acb884`)

---
### CreateGroup

`CREATE_GROUP` · hash `0x90370EBE0FEE1A3D` · jhash `0x8DC0368D` · **Cliente**

```lua
local retval = CreateGroup(unused)
```
```c
int CREATE_GROUP(int unused);
```

**Parámetros**

- `unused` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Creates a new ped group.  
Groups can contain up to 8 peds.  
The parameter is unused.  
Returns a handle to the created group, or 0 if a group couldn't be created.  
```

---
### CreateNmMessage

`CREATE_NM_MESSAGE` · hash `0x418EF2A1BCE56685` · jhash `0x1CFBFD4B` · **Cliente**

```lua
CreateNmMessage(startImmediately, messageId)
```
```c
void CREATE_NM_MESSAGE(BOOL startImmediately, int messageId);
```

**Parámetros**

- `startImmediately` (`BOOL`)
- `messageId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Creates a new NaturalMotion message.  
startImmediately: If set to true, the character will perform the message the moment it receives it by GIVE_PED_NM_MESSAGE. If false, the Ped will get the message but won't perform it yet. While it's a boolean value, if negative, the message will not be initialized.  
messageId: The ID of the NaturalMotion message.  
If a message already exists, this function does nothing. A message exists until the point it has been successfully dispatched by GIVE_PED_NM_MESSAGE.  
```

---
### CreateParachuteBagObject

`CREATE_PARACHUTE_BAG_OBJECT` · hash `0x8C4F3BF23B6237DB` · jhash `0x19198A16` · **Cliente**

```lua
local retval = CreateParachuteBagObject(ped, p1, p2)
```
```c
Object CREATE_PARACHUTE_BAG_OBJECT(Ped ped, BOOL p1, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `Object`

**Nombres antiguos (alias):** `0x8C4F3BF23B6237DB` (`N_0x8c4f3bf23b6237db`), `_CREATE_PARACHUTE_OBJECT` (`CreateParachuteObject`)

---
### CreatePed

`CREATE_PED` · hash `0xD49F9B0955C367DE` · jhash `0x0389EF71` · **Cliente · también en el servidor (RPC)**

```lua
local retval = CreatePed(pedType, modelHash, x, y, z, heading, isNetwork, bScriptHostPed)
```
```c
Ped CREATE_PED(int pedType, Hash modelHash, float x, float y, float z, float heading, BOOL isNetwork, BOOL bScriptHostPed);
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

**Devuelve:** `Ped` — A script handle (fwScriptGuid index) for the ped, or `0` if the ped failed to be created.

**Descripción oficial:**

Creates a ped (biped character, pedestrian, actor) with the specified model at the specified position and heading.
This ped will initially be owned by the creating script as a mission entity, and the model should be loaded already
(e.g. using REQUEST_MODEL).

---
### CreatePedInsideVehicle

`CREATE_PED_INSIDE_VEHICLE` · hash `0x7DD959874C1FD534` · jhash `0x3000F092` · **Cliente · también en el servidor (RPC)**

```lua
local retval = CreatePedInsideVehicle(vehicle, pedType, modelHash, seat, isNetwork, bScriptHostPed)
```
```c
Ped CREATE_PED_INSIDE_VEHICLE(Vehicle vehicle, int pedType, Hash modelHash, int seat, BOOL isNetwork, BOOL bScriptHostPed);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `pedType` (`int`): See [`CREATE_PED`](../cfx/servidor.md#createped)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `seat` (`int`)
- `isNetwork` (`BOOL`)
- `bScriptHostPed` (`BOOL`)

**Devuelve:** `Ped`

---
### CreateRandomPed

`CREATE_RANDOM_PED` · hash `0xB4AC7D0CF06BFE8F` · jhash `0x5A949543` · **Cliente**

```lua
local retval = CreateRandomPed(posX, posY, posZ)
```
```c
Ped CREATE_RANDOM_PED(float posX, float posY, float posZ);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `Ped`

**Descripción oficial:**

```
vb.net
Dim ped_handle As Integer
                    With Game.Player.Character
                        Dim pos As Vector3 = .Position + .ForwardVector * 3
                        ped_handle = Native.Function.Call(Of Integer)(Hash.CREATE_RANDOM_PED, pos.X, pos.Y, pos.Z)
                    End With
Creates a Ped at the specified location, returns the Ped Handle.
Ped will not act until SET_PED_AS_NO_LONGER_NEEDED is called.
```

---
### CreateRandomPedAsDriver

`CREATE_RANDOM_PED_AS_DRIVER` · hash `0x9B62392B474F44A0` · jhash `0xB927CE9A` · **Cliente**

```lua
local retval = CreateRandomPedAsDriver(vehicle, returnHandle)
```
```c
Ped CREATE_RANDOM_PED_AS_DRIVER(Vehicle vehicle, BOOL returnHandle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `returnHandle` (`BOOL`)

**Devuelve:** `Ped`

---
### CreateSynchronizedScene

`CREATE_SYNCHRONIZED_SCENE` · hash `0x8C18E0F9080ADD73` · jhash `0xFFDDF8FA` · **Cliente**

```lua
local retval = CreateSynchronizedScene(x, y, z, roll, pitch, yaw, p6)
```
```c
int CREATE_SYNCHRONIZED_SCENE(float x, float y, float z, float roll, float pitch, float yaw, int p6);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `roll` (`float`)
- `pitch` (`float`)
- `yaw` (`float`)
- `p6` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
p6 always 2 (but it doesnt seem to matter...)  
roll and pitch 0  
yaw to Ped.rotation  
```

---
### CreateSynchronizedScene_2

`_CREATE_SYNCHRONIZED_SCENE_2` · hash `0x62EC273D00187DCA` · jhash `0xF3876894` · **Cliente**

```lua
local retval = CreateSynchronizedScene_2(x, y, z, radius, object)
```
```c
int _CREATE_SYNCHRONIZED_SCENE_2(float x, float y, float z, float radius, Hash object);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `object` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x62EC273D00187DCA` (`N_0x62ec273d00187dca`)

---
### DeletePed

`DELETE_PED` · hash `0x9614299DCB53E54B` · jhash `0x13EFB9A0` · **Cliente**

```lua
local ped = DeletePed(ped)
```
```c
void DELETE_PED(Ped* ped);
```

**Parámetros**

- `ped` (`Ped*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Deletes the specified ped, then sets the handle pointed to by the pointer to NULL.  
```

---
### DetachSynchronizedScene

`DETACH_SYNCHRONIZED_SCENE` · hash `0x6D38F1F04CBB37EA` · jhash `0x52A1CAB2` · **Cliente**

```lua
DetachSynchronizedScene(sceneID)
```
```c
void DETACH_SYNCHRONIZED_SCENE(int sceneID);
```

**Parámetros**

- `sceneID` (`int`)

**Devuelve:** `void`

---
### DisableHeadBlendPaletteColor

`DISABLE_HEAD_BLEND_PALETTE_COLOR` · hash `0xA21C118553BBDF02` · jhash `0xC6F36292` · **Cliente**

```lua
DisableHeadBlendPaletteColor(ped)
```
```c
void DISABLE_HEAD_BLEND_PALETTE_COLOR(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA21C118553BBDF02` (`N_0xa21c118553bbdf02`)

---
### DisablePedHeatscaleOverride

`DISABLE_PED_HEATSCALE_OVERRIDE` · hash `0x600048C60D5C2C51` · jhash `0x0688DE64` · **Cliente**

```lua
DisablePedHeatscaleOverride(ped)
```
```c
void DISABLE_PED_HEATSCALE_OVERRIDE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x600048C60D5C2C51` (`N_0x600048c60d5c2c51`)

---
### DoesGroupExist

`DOES_GROUP_EXIST` · hash `0x7C6B0C22F9F40BBE` · jhash `0x935C978D` · **Cliente**

```lua
local retval = DoesGroupExist(groupId)
```
```c
BOOL DOES_GROUP_EXIST(int groupId);
```

**Parámetros**

- `groupId` (`int`)

**Devuelve:** `BOOL`

---
### DoesRelationshipGroupExist

`_DOES_RELATIONSHIP_GROUP_EXIST` · hash `0xCC6E3B6BB69501F1` · **Cliente**

```lua
local retval = DoesRelationshipGroupExist(groupHash)
```
```c
BOOL _DOES_RELATIONSHIP_GROUP_EXIST(Hash groupHash);
```

**Parámetros**

- `groupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xCC6E3B6BB69501F1` (`N_0xcc6e3b6bb69501f1`)

---
### DoesScenarioBlockingAreaExist

`_DOES_SCENARIO_BLOCKING_AREA_EXIST` · hash `0x8A24B067D175A7BD` · **Cliente**

```lua
local retval = DoesScenarioBlockingAreaExist(x1, y1, z1, x2, y2, z2)
```
```c
BOOL _DOES_SCENARIO_BLOCKING_AREA_EXIST(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8A24B067D175A7BD` (`N_0x8a24b067d175a7bd`)

---
### DropAmbientProp

`DROP_AMBIENT_PROP` · hash `0xAFF4710E2A0A6C12` · jhash `0x728D3D53` · **Cliente**

```lua
DropAmbientProp(ped)
```
```c
void DROP_AMBIENT_PROP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAFF4710E2A0A6C12` (`N_0xaff4710e2a0a6c12`)

---
### ExplodePedHead

`EXPLODE_PED_HEAD` · hash `0x2D05CED3A38D0F3A` · jhash `0x05CC1380` · **Cliente**

```lua
ExplodePedHead(ped, weaponHash)
```
```c
void EXPLODE_PED_HEAD(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`): The ped to lethally injure.
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The weapon to attribute the damage to.

**Devuelve:** `void`

**Descripción oficial:**

Applies lethal damage (FLT_MAX) to the `SKEL_Head` bone of the specified ped using the weapon passed, leading to the
ped's untimely demise.

The naming of the native is a legacy leftover (formerly EXPLODE_CHAR_HEAD in GTA3) as in the early 3D GTA games, lethal
damage to a ped head would 'explode' it.

Do note that this native function does not work in multiplayer/network environment.

---
### FinalizeHeadBlend

`FINALIZE_HEAD_BLEND` · hash `0x4668D80430D6C299` · jhash `0x894314A4` · **Cliente**

```lua
FinalizeHeadBlend(ped)
```
```c
void FINALIZE_HEAD_BLEND(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4668D80430D6C299` (`N_0x4668d80430d6c299`)

---
### ForcePedAiAndAnimationUpdate

`FORCE_PED_AI_AND_ANIMATION_UPDATE` · hash `0x2208438012482A1A` · jhash `0x187B9070` · **Cliente**

```lua
ForcePedAiAndAnimationUpdate(ped, forceAiPreCameraUpdate, forceZeroTimestep)
```
```c
void FORCE_PED_AI_AND_ANIMATION_UPDATE(Ped ped, BOOL forceAiPreCameraUpdate, BOOL forceZeroTimestep);
```

**Parámetros**

- `ped` (`Ped`)
- `forceAiPreCameraUpdate` (`BOOL`)
- `forceZeroTimestep` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Forces an instant ped AI and Animation update. Use this if your transitions between animations (especially secondary upper body animations) are janky or not smooth.
Do note this is an expensive function.

**Nombres antiguos (alias):** `0x2208438012482A1A` (`N_0x2208438012482a1a`)

---
### ForcePedMotionState

`FORCE_PED_MOTION_STATE` · hash `0xF28965D04F570DCA` · jhash `0x164DDEFF` · **Cliente**

```lua
local retval = ForcePedMotionState(ped, motionStateHash, shouldReset, updateState, forceAIPreCameraUpdate)
```
```c
BOOL FORCE_PED_MOTION_STATE(Ped ped, Hash motionStateHash, BOOL shouldReset, int updateState, BOOL forceAIPreCameraUpdate);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `motionStateHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The motion state hash.
- `shouldReset` (`BOOL`): If the motion state should be set even if the ped is already in the specified motion state.
- `updateState` (`int`): Integer but treated as a boolean (only allows 1 or 0). Sets ped reset flags `CPED_RESET_FLAG_ForcePreCameraAiAnimUpdateIfFirstPerson` and `CPED_RESET_FLAG_ForcePostCameraAnimUpdate`.
- `forceAIPreCameraUpdate` (`BOOL`): If `updateState` is 1, will set either `CPED_RESET_FLAG_ForcePreCameraAIUpdate` (if true) or `CPED_RESET_FLAG_ForcePostCameraAIUpdate` (if false) ped reset flags.

**Devuelve:** `BOOL` — Whether or not the motion state was forced on the ped successfully.

**Descripción oficial:**

```cpp
enum ePedMotionState
{
    MOTIONSTATE_NONE = -294553821, // MotionState_None
    MOTIONSTATE_IDLE = -1871534317, // MotionState_Idle
    MOTIONSTATE_WALK = -668482597, // MotionState_Walk
    MOTIONSTATE_RUN = -530524, // MotionState_Run
    MOTIONSTATE_SPRINT = -1115154469, // MotionState_Sprint
    MOTIONSTATE_CROUCH_IDLE = 1140525470, // MotionState_Crouch_Idle
    MOTIONSTATE_CROUCH_WALK = 147004056, // MotionState_Crouch_Walk
    MOTIONSTATE_CROUCH_RUN = 898879241, // MotionState_Crouch_Run
    MOTIONSTATE_DONOTHING = 247561816, // MotionState_DoNothing
    MOTIONSTATE_ANIMATEDVELOCITY = 1427811395, // MotionState_AnimatedVelocity
    MOTIONSTATE_INVEHICLE = -1797663347, // MotionState_InVehicle
    MOTIONSTATE_AIMING = 1063765679, // MotionState_Aiming
    MOTIONSTATE_DIVING_IDLE = 1212730861, // MotionState_Diving_Idle
    MOTIONSTATE_DIVING_SWIM = -1855028596, // MotionState_Diving_Swim
    MOTIONSTATE_SWIMMING_TREADWATER = -776007225, // MotionState_Swimming_TreadWater
    MOTIONSTATE_DEAD = 230360860, // MotionState_Dead
    MOTIONSTATE_STEALTH_IDLE = 1110276645, // MotionState_Stealth_Idle
    MOTIONSTATE_STEALTH_WALK = 69908130, // MotionState_Stealth_Walk
    MOTIONSTATE_STEALTH_RUN = -83133983, // MotionState_Stealth_Run
    MOTIONSTATE_PARACHUTING = -1161760501, // MotionState_Parachuting
    MOTIONSTATE_ACTIONMODE_IDLE = -633298724, // MotionState_ActionMode_Idle
    MOTIONSTATE_ACTIONMODE_WALK = -762290521, // MotionState_ActionMode_Walk
    MOTIONSTATE_ACTIONMODE_RUN = 834330132, // MotionState_ActionMode_Run
    MOTIONSTATE_JETPACK = 1398696542 // MotionState_Jetpack
}
```

---
### ForcePedToOpenParachute

`FORCE_PED_TO_OPEN_PARACHUTE` · hash `0x16E42E800B472221` · jhash `0xA819680B` · **Cliente**

```lua
ForcePedToOpenParachute(ped)
```
```c
void FORCE_PED_TO_OPEN_PARACHUTE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### FreezePedCameraRotation

`_FREEZE_PED_CAMERA_ROTATION` · hash `0xFF287323B0E2C69A` · jhash `0x290421BE` · **Cliente**

```lua
FreezePedCameraRotation(ped)
```
```c
void _FREEZE_PED_CAMERA_ROTATION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFF287323B0E2C69A` (`N_0xff287323b0e2c69a`)

---
### GetAnimInitialOffsetPosition

`GET_ANIM_INITIAL_OFFSET_POSITION` · hash `0xBE22B26DD764C040` · jhash `0xC59D4268` · **Cliente**

```lua
local retval = GetAnimInitialOffsetPosition(animDict, animName, x, y, z, xRot, yRot, zRot, p8, p9)
```
```c
Vector3 GET_ANIM_INITIAL_OFFSET_POSITION(char* animDict, char* animName, float x, float y, float z, float xRot, float yRot, float zRot, float p8, int p9);
```

**Parámetros**

- `animDict` (`char*`)
- `animName` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `p8` (`float`)
- `p9` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### GetAnimInitialOffsetRotation

`GET_ANIM_INITIAL_OFFSET_ROTATION` · hash `0x4B805E6046EE9E47` · jhash `0x5F7789E6` · **Cliente**

```lua
local retval = GetAnimInitialOffsetRotation(animDict, animName, x, y, z, xRot, yRot, zRot, p8, p9)
```
```c
Vector3 GET_ANIM_INITIAL_OFFSET_ROTATION(char* animDict, char* animName, float x, float y, float z, float xRot, float yRot, float zRot, float p8, int p9);
```

**Parámetros**

- `animDict` (`char*`)
- `animName` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `p8` (`float`)
- `p9` (`int`)

**Devuelve:** `Vector3`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### GetClosestPed

`GET_CLOSEST_PED` · hash `0xC33AB876A77F8164` · jhash `0x8F6C1F55` · **Cliente**

```lua
local retval, outPed = GetClosestPed(x, y, z, radius, p4, p5, p7, p8, pedType)
```
```c
BOOL GET_CLOSEST_PED(float x, float y, float z, float radius, BOOL p4, BOOL p5, Ped* outPed, BOOL p7, BOOL p8, int pedType);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)
- `outPed` (`Ped*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p7` (`BOOL`)
- `p8` (`BOOL`)
- `pedType` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets the closest ped in a radius.  
Ped Types:  
Any ped = -1  
Player = 1  
Male = 4   
Female = 5   
Cop = 6  
Human = 26  
SWAT = 27   
Animal = 28  
Army = 29  
------------------  
P4 P5 P7 P8  
1  0  x  x  = return nearest walking Ped  
1  x  0  x  = return nearest walking Ped  
x  1  1  x  = return Ped you are using  
0  0  x  x  = no effect  
0  x  0  x  = no effect  
x = can be 1 or 0. Does not have any obvious changes.  
This function does not return ped who is:  
1. Standing still  
2. Driving  
3. Fleeing  
4. Attacking  
This function only work if the ped is:  
1. walking normally.  
2. waiting to cross a road.  
Note: PED::GET_PED_NEARBY_PEDS works for more peds.  
```

---
### GetCombatFloat

`GET_COMBAT_FLOAT` · hash `0x52DFF8A10508090A` · jhash `0x511D7EF8` · **Cliente**

```lua
local retval = GetCombatFloat(ped, p1)
```
```c
float GET_COMBAT_FLOAT(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

```
p0: Ped Handle  
p1: int i | 0 <= i <= 27  
p1 probably refers to the attributes configured in combatbehavior.meta. There are 13. Example:  
<BlindFireChance value="0.1"/>  
<WeaponShootRateModifier value="1.0"/>  
<TimeBetweenBurstsInCover value="1.25"/>  
<BurstDurationInCover value="2.0"/>  
<TimeBetweenPeeks value="10.0"/>  
<WeaponAccuracy value="0.18"/>  
<FightProficiency value="0.8"/>  
<StrafeWhenMovingChance value="1.0"/>  
<WalkWhenStrafingChance value="0.0"/>  
<AttackWindowDistanceForCover value="55.0"/>  
<TimeToInvalidateInjuredTarget value="9.0"/>  
<TriggerChargeTime_Near value="4.0"/>  
<TriggerChargeTime_Far value="10.0"/>  
-------------Confirmed by editing combatbehavior.meta:  
p1:  
0=BlindFireChance  
1=BurstDurationInCover  
3=TimeBetweenBurstsInCover  
4=TimeBetweenPeeks  
5=StrafeWhenMovingChance  
8=WalkWhenStrafingChance  
11=AttackWindowDistanceForCover  
12=TimeToInvalidateInjuredTarget  
16=OptimalCoverDistance  
```

---
### GetDeadPedPickupCoords

`GET_DEAD_PED_PICKUP_COORDS` · hash `0xCD5003B097200F36` · jhash `0x129F9DC1` · **Cliente**

```lua
local retval = GetDeadPedPickupCoords(ped, p1, p2)
```
```c
Vector3 GET_DEAD_PED_PICKUP_COORDS(Ped ped, float p1, float p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)
- `p2` (`float`)

**Devuelve:** `Vector3`

---
### GetGroupSize

`GET_GROUP_SIZE` · hash `0x8DE69FE35CA09A45` · jhash `0xF7E1A691` · **Cliente**

```lua
local unknown, sizeInMembers = GetGroupSize(groupID)
```
```c
void GET_GROUP_SIZE(int groupID, Any* unknown, int* sizeInMembers);
```

**Parámetros**

- `groupID` (`int`)
- `unknown` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `sizeInMembers` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
p1 may be a BOOL representing whether or not the group even exists  
```

---
### GetJackTarget

`GET_JACK_TARGET` · hash `0x5486A79D9FBD342D` · jhash `0x1D196361` · **Cliente**

```lua
local retval = GetJackTarget(ped)
```
```c
Ped GET_JACK_TARGET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Ped`

---
### GetMeleeTargetForPed

`GET_MELEE_TARGET_FOR_PED` · hash `0x18A3E9EE1297FD39` · jhash `0xAFEC26A4` · **Cliente**

```lua
local retval = GetMeleeTargetForPed(ped)
```
```c
Ped GET_MELEE_TARGET_FOR_PED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Ped`

---
### GetMount

`GET_MOUNT` · hash `0xE7E11B8DCBED1058` · jhash `0xDD31EC4E` · **Cliente**

```lua
local retval = GetMount(ped)
```
```c
Ped GET_MOUNT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Ped`

**Descripción oficial:**

```
Function just returns 0  
void __fastcall ped__get_mount(NativeContext *a1)  
{  
  NativeContext *v1; // rbx@1  
  v1 = a1;  
  GetAddressOfPedFromScriptHandle(a1->Args->Arg1);  
  v1->Returns->Item1= 0;  
}  
```

---
### GetNumHairColors

`_GET_NUM_HAIR_COLORS` · hash `0xE5C0CF872C2AD150` · **Cliente**

```lua
local retval = GetNumHairColors()
```
```c
int _GET_NUM_HAIR_COLORS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Used for freemode (online) characters.  
```

---
### GetNumMakeupColors

`_GET_NUM_MAKEUP_COLORS` · hash `0xD1F7CA1535D22818` · **Cliente**

```lua
local retval = GetNumMakeupColors()
```
```c
int _GET_NUM_MAKEUP_COLORS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xD1F7CA1535D22818` (`N_0xd1f7ca1535d22818`)

---
### GetNumberOfPedDrawableVariations

`GET_NUMBER_OF_PED_DRAWABLE_VARIATIONS` · hash `0x27561561732A7842` · jhash `0x9754C27D` · **Cliente**

```lua
local retval = GetNumberOfPedDrawableVariations(ped, componentId)
```
```c
int GET_NUMBER_OF_PED_DRAWABLE_VARIATIONS(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component id you want to get the drawable variatons of. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation)

**Devuelve:** `int`

---
### GetNumberOfPedPropDrawableVariations

`GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS` · hash `0x5FAF9754E789FB47` · jhash `0xC9780B95` · **Cliente**

```lua
local retval = GetNumberOfPedPropDrawableVariations(ped, propId)
```
```c
int GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS(Ped ped, int propId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `propId` (`int`): The prop id you want to get the drawable variations of. Refer to [SET_PED_PROP_INDEX](../cfx/servidor.md#setpedpropindex)

**Devuelve:** `int`

---
### GetNumberOfPedPropTextureVariations

`GET_NUMBER_OF_PED_PROP_TEXTURE_VARIATIONS` · hash `0xA6E7F1CEB523E171` · jhash `0x4892B882` · **Cliente**

```lua
local retval = GetNumberOfPedPropTextureVariations(ped, propId, drawableId)
```
```c
int GET_NUMBER_OF_PED_PROP_TEXTURE_VARIATIONS(Ped ped, int propId, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `propId` (`int`): The prop id you want to get the texture variations of. Refer to [SET_PED_PROP_INDEX](../cfx/servidor.md#setpedpropindex)
- `drawableId` (`int`): The drawable id of the prop you want to get the texture variations of. Refer to [GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS](#getnumberofpedpropdrawablevariations).

**Devuelve:** `int`

**Descripción oficial:**

```
Need to check behavior when drawableId = -1
```

---
### GetNumberOfPedTextureVariations

`GET_NUMBER_OF_PED_TEXTURE_VARIATIONS` · hash `0x8F7156A3142A6BAD` · jhash `0x83D9FBE7` · **Cliente**

```lua
local retval = GetNumberOfPedTextureVariations(ped, componentId, drawableId)
```
```c
int GET_NUMBER_OF_PED_TEXTURE_VARIATIONS(Ped ped, int componentId, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component id you want to get the texture variations of. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).
- `drawableId` (`int`): The drawable id of the component you want to get the texture variations of. Refer to [GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS](#getnumberofpedpropdrawablevariations).

**Devuelve:** `int`

---
### GetPedAccuracy

`GET_PED_ACCURACY` · hash `0x37F4AD56ECBC0CD6` · jhash `0x0A2A0AA0` · **Cliente**

```lua
local retval = GetPedAccuracy(ped)
```
```c
int GET_PED_ACCURACY(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetPedAlertness

`GET_PED_ALERTNESS` · hash `0xF6AA118530443FD2` · jhash `0xF83E4DAF` · **Cliente**

```lua
local retval = GetPedAlertness(ped)
```
```c
int GET_PED_ALERTNESS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the ped's alertness (0-3).  
Values :   
0 : Neutral  
1 : Heard something (gun shot, hit, etc)  
2 : Knows (the origin of the event)  
3 : Fully alerted (is facing the event?)  
If the Ped does not exist, returns -1.  
```

---
### GetPedArmour

`GET_PED_ARMOUR` · hash `0x9483AF821605B1D8` · jhash `0x2CE311A7` · **Cliente**

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
### GetPedAsGroupLeader

`GET_PED_AS_GROUP_LEADER` · hash `0x5CCE68DBD5FE93EC` · jhash `0x52873C6A` · **Cliente**

```lua
local retval = GetPedAsGroupLeader(groupID)
```
```c
Ped GET_PED_AS_GROUP_LEADER(int groupID);
```

**Parámetros**

- `groupID` (`int`)

**Devuelve:** `Ped`

**Nombres antiguos (alias):** `_GET_PED_AS_GROUP_LEADER` (`GetPedAsGroupLeader`)

---
### GetPedAsGroupMember

`GET_PED_AS_GROUP_MEMBER` · hash `0x51455483CF23ED97` · jhash `0x9AA3CC8C` · **Cliente**

```lua
local retval = GetPedAsGroupMember(groupID, memberNumber)
```
```c
Ped GET_PED_AS_GROUP_MEMBER(int groupID, int memberNumber);
```

**Parámetros**

- `groupID` (`int`)
- `memberNumber` (`int`)

**Devuelve:** `Ped`

**Descripción oficial:**

```
from fm_mission_controller.c4 (variable names changed for clarity):  
int groupID = PLAYER::GET_PLAYER_GROUP(PLAYER::PLAYER_ID());  
PED::GET_GROUP_SIZE(group, &unused, &groupSize);  
if (groupSize >= 1) {  
. . . . for (int memberNumber = 0; memberNumber < groupSize; memberNumber++) {  
. . . . . . . . Ped ped1 = PED::GET_PED_AS_GROUP_MEMBER(groupID, memberNumber);  
. . . . . . . . //and so on  
```

---
### GetPedBoneCoords

`GET_PED_BONE_COORDS` · hash `0x17C07FC640E86B4E` · jhash `0x4579CAB1` · **Cliente**

```lua
local retval = GetPedBoneCoords(ped, boneId, offsetX, offsetY, offsetZ)
```
```c
Vector3 GET_PED_BONE_COORDS(Ped ped, int boneId, float offsetX, float offsetY, float offsetZ);
```

**Parámetros**

- `ped` (`Ped`)
- `boneId` (`int`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Gets the position of the specified bone of the specified ped.  
ped: The ped to get the position of a bone from.  
boneId: The ID of the bone to get the position from. This is NOT the index.  
offsetX: The X-component of the offset to add to the position relative to the bone's rotation.  
offsetY: The Y-component of the offset to add to the position relative to the bone's rotation.  
offsetZ: The Z-component of the offset to add to the position relative to the bone's rotation.  
```

---
### GetPedBoneIndex

`GET_PED_BONE_INDEX` · hash `0x3F428D08BE5AAE31` · jhash `0x259C6BA2` · **Cliente**

```lua
local retval = GetPedBoneIndex(ped, boneId)
```
```c
int GET_PED_BONE_INDEX(Ped ped, int boneId);
```

**Parámetros**

- `ped` (`Ped`)
- `boneId` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```cpp
enum ePedBoneId : uint16_t
{
    SKEL_ROOT = 0x0,
    SKEL_Pelvis = 0x2E28,
    SKEL_L_Thigh = 0xE39F,
    SKEL_L_Calf = 0xF9BB,
    SKEL_L_Foot = 0x3779,
    SKEL_L_Toe0 = 0x83C,
    EO_L_Foot = 0x84C5,
    EO_L_Toe = 0x68BD,
    IK_L_Foot = 0xFEDD,
    PH_L_Foot = 0xE175,
    MH_L_Knee = 0xB3FE,
    SKEL_R_Thigh = 0xCA72,
    SKEL_R_Calf = 0x9000,
    SKEL_R_Foot = 0xCC4D,
    SKEL_R_Toe0 = 0x512D,
    EO_R_Foot = 0x1096,
    EO_R_Toe = 0x7163,
    IK_R_Foot = 0x8AAE,
    PH_R_Foot = 0x60E6,
    MH_R_Knee = 0x3FCF,
    RB_L_ThighRoll = 0x5C57,
    RB_R_ThighRoll = 0x192A,
    SKEL_Spine_Root = 0xE0FD,
    SKEL_Spine0 = 0x5C01,
    SKEL_Spine1 = 0x60F0,
    SKEL_Spine2 = 0x60F1,
    SKEL_Spine3 = 0x60F2,
    SKEL_L_Clavicle = 0xFCD9,
    SKEL_L_UpperArm = 0xB1C5,
    SKEL_L_Forearm = 0xEEEB,
    SKEL_L_Hand = 0x49D9,
    SKEL_L_Finger00 = 0x67F2,
    SKEL_L_Finger01 = 0xFF9,
    SKEL_L_Finger02 = 0xFFA,
    SKEL_L_Finger10 = 0x67F3,
    SKEL_L_Finger11 = 0x1049,
    SKEL_L_Finger12 = 0x104A,
    SKEL_L_Finger20 = 0x67F4,
    SKEL_L_Finger21 = 0x1059,
    SKEL_L_Finger22 = 0x105A,
    SKEL_L_Finger30 = 0x67F5,
    SKEL_L_Finger31 = 0x1029,
    SKEL_L_Finger32 = 0x102A,
    SKEL_L_Finger40 = 0x67F6,
    SKEL_L_Finger41 = 0x1039,
    SKEL_L_Finger42 = 0x103A,
    PH_L_Hand = 0xEB95,
    IK_L_Hand = 0x8CBD,
    RB_L_ForeArmRoll = 0xEE4F,
    RB_L_ArmRoll = 0x1470,
    MH_L_Elbow = 0x58B7,
    SKEL_R_Clavicle = 0x29D2,
    SKEL_R_UpperArm = 0x9D4D,
    SKEL_R_Forearm = 0x6E5C,
    SKEL_R_Hand = 0xDEAD,
    SKEL_R_Finger00 = 0xE5F2,
    SKEL_R_Finger01 = 0xFA10,
    SKEL_R_Finger02 = 0xFA11,
    SKEL_R_Finger10 = 0xE5F3,
    SKEL_R_Finger11 = 0xFA60,
    SKEL_R_Finger12 = 0xFA61,
    SKEL_R_Finger20 = 0xE5F4,
    SKEL_R_Finger21 = 0xFA70,
    SKEL_R_Finger22 = 0xFA71,
    SKEL_R_Finger30 = 0xE5F5,
    SKEL_R_Finger31 = 0xFA40,
    SKEL_R_Finger32 = 0xFA41,
    SKEL_R_Finger40 = 0xE5F6,
    SKEL_R_Finger41 = 0xFA50,
    SKEL_R_Finger42 = 0xFA51,
    PH_R_Hand = 0x6F06,
    IK_R_Hand = 0x188E,
    RB_R_ForeArmRoll = 0xAB22,
    RB_R_ArmRoll = 0x90FF,
    MH_R_Elbow = 0xBB0,
    SKEL_Neck_1 = 0x9995,
    SKEL_Head = 0x796E,
    IK_Head = 0x322C,
    FACIAL_facialRoot = 0xFE2C,
    FB_L_Brow_Out_000 = 0xE3DB,
    FB_L_Lid_Upper_000 = 0xB2B6,
    FB_L_Eye_000 = 0x62AC,
    FB_L_CheekBone_000 = 0x542E,
    FB_L_Lip_Corner_000 = 0x74AC,
    FB_R_Lid_Upper_000 = 0xAA10,
    FB_R_Eye_000 = 0x6B52,
    FB_R_CheekBone_000 = 0x4B88,
    FB_R_Brow_Out_000 = 0x54C,
    FB_R_Lip_Corner_000 = 0x2BA6,
    FB_Brow_Centre_000 = 0x9149,
    FB_UpperLipRoot_000 = 0x4ED2,
    FB_UpperLip_000 = 0xF18F,
    FB_L_Lip_Top_000 = 0x4F37,
    FB_R_Lip_Top_000 = 0x4537,
    FB_Jaw_000 = 0xB4A0,
    FB_LowerLipRoot_000 = 0x4324,
    FB_LowerLip_000 = 0x508F,
    FB_L_Lip_Bot_000 = 0xB93B,
    FB_R_Lip_Bot_000 = 0xC33B,
    FB_Tongue_000 = 0xB987,
    RB_Neck_1 = 0x8B93,
    SPR_L_Breast = 0xFC8E,
    SPR_R_Breast = 0x885F,
    IK_Root = 0xDD1C,
    SKEL_Neck_2 = 0x5FD4,
    SKEL_Pelvis1 = 0xD003,
    SKEL_PelvisRoot = 0x45FC,
    SKEL_SADDLE = 0x9524,
    MH_L_CalfBack = 0x1013,
    MH_L_ThighBack = 0x600D,
    SM_L_Skirt = 0xC419,
    MH_R_CalfBack = 0xB013,
    MH_R_ThighBack = 0x51A3,
    SM_R_Skirt = 0x7712,
    SM_M_BackSkirtRoll = 0xDBB,
    SM_L_BackSkirtRoll = 0x40B2,
    SM_R_BackSkirtRoll = 0xC141,
    SM_M_FrontSkirtRoll = 0xCDBB,
    SM_L_FrontSkirtRoll = 0x9B69,
    SM_R_FrontSkirtRoll = 0x86F1,
    SM_CockNBalls_ROOT = 0xC67D,
    SM_CockNBalls = 0x9D34,
    MH_L_Finger00 = 0x8C63,
    MH_L_FingerBulge00 = 0x5FB8,
    MH_L_Finger10 = 0x8C53,
    MH_L_FingerTop00 = 0xA244,
    MH_L_HandSide = 0xC78A,
    MH_Watch = 0x2738,
    MH_L_Sleeve = 0x933C,
    MH_R_Finger00 = 0x2C63,
    MH_R_FingerBulge00 = 0x69B8,
    MH_R_Finger10 = 0x2C53,
    MH_R_FingerTop00 = 0xEF4B,
    MH_R_HandSide = 0x68FB,
    MH_R_Sleeve = 0x92DC,
    FACIAL_jaw = 0xB21,
    FACIAL_underChin = 0x8A95,
    FACIAL_L_underChin = 0x234E,
    FACIAL_chin = 0xB578,
    FACIAL_chinSkinBottom = 0x98BC,
    FACIAL_L_chinSkinBottom = 0x3E8F,
    FACIAL_R_chinSkinBottom = 0x9E8F,
    FACIAL_tongueA = 0x4A7C,
    FACIAL_tongueB = 0x4A7D,
    FACIAL_tongueC = 0x4A7E,
    FACIAL_tongueD = 0x4A7F,
    FACIAL_tongueE = 0x4A80,
    FACIAL_L_tongueE = 0x35F2,
    FACIAL_R_tongueE = 0x2FF2,
    FACIAL_L_tongueD = 0x35F1,
    FACIAL_R_tongueD = 0x2FF1,
    FACIAL_L_tongueC = 0x35F0,
    FACIAL_R_tongueC = 0x2FF0,
    FACIAL_L_tongueB = 0x35EF,
    FACIAL_R_tongueB = 0x2FEF,
    FACIAL_L_tongueA = 0x35EE,
    FACIAL_R_tongueA = 0x2FEE,
    FACIAL_chinSkinTop = 0x7226,
    FACIAL_L_chinSkinTop = 0x3EB3,
    FACIAL_chinSkinMid = 0x899A,
    FACIAL_L_chinSkinMid = 0x4427,
    FACIAL_L_chinSide = 0x4A5E,
    FACIAL_R_chinSkinMid = 0xF5AF,
    FACIAL_R_chinSkinTop = 0xF03B,
    FACIAL_R_chinSide = 0xAA5E,
    FACIAL_R_underChin = 0x2BF4,
    FACIAL_L_lipLowerSDK = 0xB9E1,
    FACIAL_L_lipLowerAnalog = 0x244A,
    FACIAL_L_lipLowerThicknessV = 0xC749,
    FACIAL_L_lipLowerThicknessH = 0xC67B,
    FACIAL_lipLowerSDK = 0x7285,
    FACIAL_lipLowerAnalog = 0xD97B,
    FACIAL_lipLowerThicknessV = 0xC5BB,
    FACIAL_lipLowerThicknessH = 0xC5ED,
    FACIAL_R_lipLowerSDK = 0xA034,
    FACIAL_R_lipLowerAnalog = 0xC2D9,
    FACIAL_R_lipLowerThicknessV = 0xC6E9,
    FACIAL_R_lipLowerThicknessH = 0xC6DB,
    FACIAL_nose = 0x20F1,
    FACIAL_L_nostril = 0x7322,
    FACIAL_L_nostrilThickness = 0xC15F,
    FACIAL_noseLower = 0xE05A,
    FACIAL_L_noseLowerThickness = 0x79D5,
    FACIAL_R_noseLowerThickness = 0x7975,
    FACIAL_noseTip = 0x6A60,
    FACIAL_R_nostril = 0x7922,
    FACIAL_R_nostrilThickness = 0x36FF,
    FACIAL_noseUpper = 0xA04F,
    FACIAL_L_noseUpper = 0x1FB8,
    FACIAL_noseBridge = 0x9BA3,
    FACIAL_L_nasolabialFurrow = 0x5ACA,
    FACIAL_L_nasolabialBulge = 0xCD78,
    FACIAL_L_cheekLower = 0x6907,
    FACIAL_L_cheekLowerBulge1 = 0xE3FB,
    FACIAL_L_cheekLowerBulge2 = 0xE3FC,
    FACIAL_L_cheekInner = 0xE7AB,
    FACIAL_L_cheekOuter = 0x8161,
    FACIAL_L_eyesackLower = 0x771B,
    FACIAL_L_eyeball = 0x1744,
    FACIAL_L_eyelidLower = 0x998C,
    FACIAL_L_eyelidLowerOuterSDK = 0xFE4C,
    FACIAL_L_eyelidLowerOuterAnalog = 0xB9AA,
    FACIAL_L_eyelashLowerOuter = 0xD7F6,
    FACIAL_L_eyelidLowerInnerSDK = 0xF151,
    FACIAL_L_eyelidLowerInnerAnalog = 0x8242,
    FACIAL_L_eyelashLowerInner = 0x4CCF,
    FACIAL_L_eyelidUpper = 0x97C1,
    FACIAL_L_eyelidUpperOuterSDK = 0xAF15,
    FACIAL_L_eyelidUpperOuterAnalog = 0x67FA,
    FACIAL_L_eyelashUpperOuter = 0x27B7,
    FACIAL_L_eyelidUpperInnerSDK = 0xD341,
    FACIAL_L_eyelidUpperInnerAnalog = 0xF092,
    FACIAL_L_eyelashUpperInner = 0x9B1F,
    FACIAL_L_eyesackUpperOuterBulge = 0xA559,
    FACIAL_L_eyesackUpperInnerBulge = 0x2F2A,
    FACIAL_L_eyesackUpperOuterFurrow = 0xC597,
    FACIAL_L_eyesackUpperInnerFurrow = 0x52A7,
    FACIAL_forehead = 0x9218,
    FACIAL_L_foreheadInner = 0x843,
    FACIAL_L_foreheadInnerBulge = 0x767C,
    FACIAL_L_foreheadOuter = 0x8DCB,
    FACIAL_skull = 0x4221,
    FACIAL_foreheadUpper = 0xF7D6,
    FACIAL_L_foreheadUpperInner = 0xCF13,
    FACIAL_L_foreheadUpperOuter = 0x509B,
    FACIAL_R_foreheadUpperInner = 0xCEF3,
    FACIAL_R_foreheadUpperOuter = 0x507B,
    FACIAL_L_temple = 0xAF79,
    FACIAL_L_ear = 0x19DD,
    FACIAL_L_earLower = 0x6031,
    FACIAL_L_masseter = 0x2810,
    FACIAL_L_jawRecess = 0x9C7A,
    FACIAL_L_cheekOuterSkin = 0x14A5,
    FACIAL_R_cheekLower = 0xF367,
    FACIAL_R_cheekLowerBulge1 = 0x599B,
    FACIAL_R_cheekLowerBulge2 = 0x599C,
    FACIAL_R_masseter = 0x810,
    FACIAL_R_jawRecess = 0x93D4,
    FACIAL_R_ear = 0x1137,
    FACIAL_R_earLower = 0x8031,
    FACIAL_R_eyesackLower = 0x777B,
    FACIAL_R_nasolabialBulge = 0xD61E,
    FACIAL_R_cheekOuter = 0xD32,
    FACIAL_R_cheekInner = 0x737C,
    FACIAL_R_noseUpper = 0x1CD6,
    FACIAL_R_foreheadInner = 0xE43,
    FACIAL_R_foreheadInnerBulge = 0x769C,
    FACIAL_R_foreheadOuter = 0x8FCB,
    FACIAL_R_cheekOuterSkin = 0xB334,
    FACIAL_R_eyesackUpperInnerFurrow = 0x9FAE,
    FACIAL_R_eyesackUpperOuterFurrow = 0x140F,
    FACIAL_R_eyesackUpperInnerBulge = 0xA359,
    FACIAL_R_eyesackUpperOuterBulge = 0x1AF9,
    FACIAL_R_nasolabialFurrow = 0x2CAA,
    FACIAL_R_temple = 0xAF19,
    FACIAL_R_eyeball = 0x1944,
    FACIAL_R_eyelidUpper = 0x7E14,
    FACIAL_R_eyelidUpperOuterSDK = 0xB115,
    FACIAL_R_eyelidUpperOuterAnalog = 0xF25A,
    FACIAL_R_eyelashUpperOuter = 0xE0A,
    FACIAL_R_eyelidUpperInnerSDK = 0xD541,
    FACIAL_R_eyelidUpperInnerAnalog = 0x7C63,
    FACIAL_R_eyelashUpperInner = 0x8172,
    FACIAL_R_eyelidLower = 0x7FDF,
    FACIAL_R_eyelidLowerOuterSDK = 0x1BD,
    FACIAL_R_eyelidLowerOuterAnalog = 0x457B,
    FACIAL_R_eyelashLowerOuter = 0xBE49,
    FACIAL_R_eyelidLowerInnerSDK = 0xF351,
    FACIAL_R_eyelidLowerInnerAnalog = 0xE13,
    FACIAL_R_eyelashLowerInner = 0x3322,
    FACIAL_L_lipUpperSDK = 0x8F30,
    FACIAL_L_lipUpperAnalog = 0xB1CF,
    FACIAL_L_lipUpperThicknessH = 0x37CE,
    FACIAL_L_lipUpperThicknessV = 0x38BC,
    FACIAL_lipUpperSDK = 0x1774,
    FACIAL_lipUpperAnalog = 0xE064,
    FACIAL_lipUpperThicknessH = 0x7993,
    FACIAL_lipUpperThicknessV = 0x7981,
    FACIAL_L_lipCornerSDK = 0xB1C,
    FACIAL_L_lipCornerAnalog = 0xE568,
    FACIAL_L_lipCornerThicknessUpper = 0x7BC,
    FACIAL_L_lipCornerThicknessLower = 0xDD42,
    FACIAL_R_lipUpperSDK = 0x7583,
    FACIAL_R_lipUpperAnalog = 0x51CF,
    FACIAL_R_lipUpperThicknessH = 0x382E,
    FACIAL_R_lipUpperThicknessV = 0x385C,
    FACIAL_R_lipCornerSDK = 0xB3C,
    FACIAL_R_lipCornerAnalog = 0xEE0E,
    FACIAL_R_lipCornerThicknessUpper = 0x54C3,
    FACIAL_R_lipCornerThicknessLower = 0x2BBA,
    MH_MulletRoot = 0x3E73,
    MH_MulletScaler = 0xA1C2,
    MH_Hair_Scale = 0xC664,
    MH_Hair_Crown = 0x1675,
    SM_Torch = 0x8D6,
    FX_Light = 0x8959,
    FX_Light_Scale = 0x5038,
    FX_Light_Switch = 0xE18E,
    BagRoot = 0xAD09,
    BagPivotROOT = 0xB836,
    BagPivot = 0x4D11,
    BagBody = 0xAB6D,
    BagBone_R = 0x937,
    BagBone_L = 0x991,
    SM_LifeSaver_Front = 0x9420,
    SM_R_Pouches_ROOT = 0x2962,
    SM_R_Pouches = 0x4141,
    SM_L_Pouches_ROOT = 0x2A02,
    SM_L_Pouches = 0x4B41,
    SM_Suit_Back_Flapper = 0xDA2D,
    SPR_CopRadio = 0x8245,
    SM_LifeSaver_Back = 0x2127,
    MH_BlushSlider = 0xA0CE,
    SKEL_Tail_01 = 0x347,
    SKEL_Tail_02 = 0x348,
    MH_L_Concertina_B = 0xC988,
    MH_L_Concertina_A = 0xC987,
    MH_R_Concertina_B = 0xC8E8,
    MH_R_Concertina_A = 0xC8E7,
    MH_L_ShoulderBladeRoot = 0x8711,
    MH_L_ShoulderBlade = 0x4EAF,
    MH_R_ShoulderBladeRoot = 0x3A0A,
    MH_R_ShoulderBlade = 0x54AF,
    FB_R_Ear_000 = 0x6CDF,
    SPR_R_Ear = 0x63B6,
    FB_L_Ear_000 = 0x6439,
    SPR_L_Ear = 0x5B10,
    FB_TongueA_000 = 0x4206,
    FB_TongueB_000 = 0x4207,
    FB_TongueC_000 = 0x4208,
    SKEL_L_Toe1 = 0x1D6B,
    SKEL_R_Toe1 = 0xB23F,
    SKEL_Tail_03 = 0x349,
    SKEL_Tail_04 = 0x34A,
    SKEL_Tail_05 = 0x34B,
    SPR_Gonads_ROOT = 0xBFDE,
    SPR_Gonads = 0x1C00,
    FB_L_Brow_Out_001 = 0xE3DB,
    FB_L_Lid_Upper_001 = 0xB2B6,
    FB_L_Eye_001 = 0x62AC,
    FB_L_CheekBone_001 = 0x542E,
    FB_L_Lip_Corner_001 = 0x74AC,
    FB_R_Lid_Upper_001 = 0xAA10,
    FB_R_Eye_001 = 0x6B52,
    FB_R_CheekBone_001 = 0x4B88,
    FB_R_Brow_Out_001 = 0x54C,
    FB_R_Lip_Corner_001 = 0x2BA6,
    FB_Brow_Centre_001 = 0x9149,
    FB_UpperLipRoot_001 = 0x4ED2,
    FB_UpperLip_001 = 0xF18F,
    FB_L_Lip_Top_001 = 0x4F37,
    FB_R_Lip_Top_001 = 0x4537,
    FB_Jaw_001 = 0xB4A0,
    FB_LowerLipRoot_001 = 0x4324,
    FB_LowerLip_001 = 0x508F,
    FB_L_Lip_Bot_001 = 0xB93B,
    FB_R_Lip_Bot_001 = 0xC33B,
    FB_Tongue_001 = 0xB987
}; 
```

---
### GetPedCauseOfDeath

`GET_PED_CAUSE_OF_DEATH` · hash `0x16FFE42AB2D2DC59` · jhash `0x63458C27` · **Cliente**

```lua
local retval = GetPedCauseOfDeath(ped)
```
```c
Hash GET_PED_CAUSE_OF_DEATH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Returns the hash of the weapon/model/object that killed the ped.  
```

---
### GetPedCombatMovement

`GET_PED_COMBAT_MOVEMENT` · hash `0xDEA92412FCAEB3F5` · jhash `0xF3E7730E` · **Cliente**

```lua
local retval = GetPedCombatMovement(ped)
```
```c
int GET_PED_COMBAT_MOVEMENT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetPedCombatRange

`GET_PED_COMBAT_RANGE` · hash `0xF9D9F7F2DB8E2FA0` · jhash `0x9B9B7163` · **Cliente**

```lua
local retval = GetPedCombatRange(ped)
```
```c
int GET_PED_COMBAT_RANGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetPedConfigFlag

`GET_PED_CONFIG_FLAG` · hash `0x7EE53118C892B513` · jhash `0xABE98267` · **Cliente**

```lua
local retval = GetPedConfigFlag(ped, flagId, p2)
```
```c
BOOL GET_PED_CONFIG_FLAG(Ped ped, int flagId, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `flagId` (`int`)
- `p2` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

See [`SET_PED_CONFIG_FLAG`](../cfx/servidor.md#setpedconfigflag).

---
### GetPedCurrentMovementSpeed

`_GET_PED_CURRENT_MOVEMENT_SPEED` · hash `0xF60165E1D2C5370B` · **Cliente**

```lua
local retval, speedX, speedY = GetPedCurrentMovementSpeed(ped)
```
```c
BOOL _GET_PED_CURRENT_MOVEMENT_SPEED(Ped ped, float* speedX, float* speedY);
```

**Parámetros**

- `ped` (`Ped`)
- `speedX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `speedY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF60165E1D2C5370B` (`N_0xf60165e1d2c5370b`)

---
### GetPedDecorationZoneFromHashes

`GET_PED_DECORATION_ZONE_FROM_HASHES` · hash `0x9FD452BFBE7A7A8B` · jhash `0x3543019E` · **Cliente**

```lua
local retval = GetPedDecorationZoneFromHashes(collection, overlay)
```
```c
int GET_PED_DECORATION_ZONE_FROM_HASHES(Hash collection, Hash overlay);
```

**Parámetros**

- `collection` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `overlay` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int` — Returns the doeciration zone for the specific collection and overlay combination, refer to `ePedDecorationZone`

**Descripción oficial:**

```cpp
enum ePedDecorationZone
{
	ZONE_TORSO = 0,
	ZONE_HEAD = 1,
	ZONE_LEFT_ARM = 2,
	ZONE_RIGHT_ARM = 3,
	ZONE_LEFT_LEG = 4,
	ZONE_RIGHT_LEG = 5,
	ZONE_UNKNOWN = 6,
	ZONE_NONE = 7
};
```

**Nombres antiguos (alias):** `_GET_TATTOO_ZONE` (`GetTattooZone`)

---
### GetPedDecorationsState

`GET_PED_DECORATIONS_STATE` · hash `0x71EAB450D86954A1` · jhash `0x47187F7F` · **Cliente**

```lua
local retval = GetPedDecorationsState(ped)
```
```c
int GET_PED_DECORATIONS_STATE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x71EAB450D86954A1` (`N_0x71eab450d86954a1`)

---
### GetPedDefensiveAreaPosition

`GET_PED_DEFENSIVE_AREA_POSITION` · hash `0x3C06B8786DD94CD1` · jhash `0xCB65198D` · **Cliente**

```lua
local retval = GetPedDefensiveAreaPosition(ped, p1)
```
```c
Vector3 GET_PED_DEFENSIVE_AREA_POSITION(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `Vector3`

---
### GetPedDiesInWater

`_GET_PED_DIES_IN_WATER` · hash `0x65671A4FB8218930` · **Cliente**

```lua
local retval = GetPedDiesInWater(ped)
```
```c
BOOL _GET_PED_DIES_IN_WATER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### GetPedDrawableVariation

`GET_PED_DRAWABLE_VARIATION` · hash `0x67F3780DD425D4FC` · jhash `0x29850FE2` · **Cliente**

```lua
local retval = GetPedDrawableVariation(ped, componentId)
```
```c
int GET_PED_DRAWABLE_VARIATION(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`)
- `componentId` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Ids
0 - Head
1 - Beard
2 - Hair
3 - Torso
4 - Legs
5 - Hands
6 - Foot
7 - Scarfs/Neck Accessories
8 - Accessories 1
9 - Accessories 2
10- Decals
11 - Auxiliary parts for torso
```

---
### GetPedEmissiveIntensity

`_GET_PED_EMISSIVE_INTENSITY` · hash `0x1461B28A06717D68` · **Cliente**

```lua
local retval = GetPedEmissiveIntensity(ped)
```
```c
float _GET_PED_EMISSIVE_INTENSITY(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped to get the glow intensity from.

**Devuelve:** `float` — A float between 0.0 and 1.0 representing the current illuminated clothing glow intensity.

**Descripción oficial:**

Use [`SetPedIlluminatedClothingGlowIntensity`](#setpedemissiveintensity) to set the illuminated clothing glow intensity for a specific ped.

**Nombres antiguos (alias):** `0x1461B28A06717D68` (`N_0x1461b28a06717d68`), `_GET_PED_ILLUMINATED_CLOTHING_GLOW_INTENSITY` (`GetPedIlluminatedClothingGlowIntensity`)

---
### GetPedEnveffScale

`GET_PED_ENVEFF_SCALE` · hash `0x9C14D30395A51A3C` · jhash `0xA3421E39` · **Cliente**

```lua
local retval = GetPedEnveffScale(ped)
```
```c
float GET_PED_ENVEFF_SCALE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `float`

---
### GetPedEventData

`_GET_PED_EVENT_DATA` · hash `0xBA656A3BB01BDEA3` · **Cliente**

```lua
local retval, outData = GetPedEventData(ped, eventType, outData)
```
```c
BOOL _GET_PED_EVENT_DATA(Ped ped, int eventType, Any* outData);
```

**Parámetros**

- `ped` (`Ped`)
- `eventType` (`int`)
- `outData` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### GetPedExtractedDisplacement

`GET_PED_EXTRACTED_DISPLACEMENT` · hash `0xE0AF41401ADF87E3` · jhash `0x5231F901` · **Cliente**

```lua
local retval = GetPedExtractedDisplacement(ped, worldSpace)
```
```c
Vector3 GET_PED_EXTRACTED_DISPLACEMENT(Ped ped, BOOL worldSpace);
```

**Parámetros**

- `ped` (`Ped`)
- `worldSpace` (`BOOL`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Gets the offset the specified ped has moved since the previous tick.  
If worldSpace is false, the returned offset is relative to the ped. That is, if the ped has moved 1 meter right and 5 meters forward, it'll return 1,5,0.  
If worldSpace is true, the returned offset is relative to the world. That is, if the ped has moved 1 meter on the X axis and 5 meters on the Y axis, it'll return 1,5,0.  
```

---
### GetPedEyeColor

`_GET_PED_EYE_COLOR` · hash `0x76BBA2CEE66D47E9` · **Cliente**

```lua
local retval = GetPedEyeColor(ped)
```
```c
int _GET_PED_EYE_COLOR(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `int` — Returns ped's eye colour, or -1 if fails to get.

**Descripción oficial:**

A getter for [`_SET_PED_EYE_COLOR`](../cfx/servidor.md#setpedeyecolor).

**Nombres antiguos (alias):** `0x76BBA2CEE66D47E9` (`N_0x76bba2cee66d47e9`)

**Ejemplo (lua):**

```lua
local pedEyeColour = N_0x76bba2cee66d47e9(PlayerPedId())
if pedEyeColour == 7 then
  print("Gray eyes!")
end
```

---
### GetPedGroupIndex

`GET_PED_GROUP_INDEX` · hash `0xF162E133B4E7A675` · jhash `0x134E0785` · **Cliente**

```lua
local retval = GetPedGroupIndex(ped)
```
```c
int GET_PED_GROUP_INDEX(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the group id of which the specified ped is a member of.  
```

---
### GetPedHairRgbColor

`_GET_PED_HAIR_RGB_COLOR` · hash `0x4852FC386E2E1BB5` · **Cliente**

```lua
local outR, outG, outB = GetPedHairRgbColor(hairColorIndex)
```
```c
void _GET_PED_HAIR_RGB_COLOR(int hairColorIndex, int* outR, int* outG, int* outB);
```

**Parámetros**

- `hairColorIndex` (`int`): The hair color index. Value between 0-63 (inclusive).
- `outR` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Output red value.
- `outG` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Output green value.
- `outB` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Output blue value.

**Devuelve:** `void`

**Descripción oficial:**

Input: Haircolor index, value between 0 and 63 (inclusive).
Output: RGB values for the haircolor specified in the input.

This is used with the hair color swatches scaleform.

Use [`_0x013E5CFC38CD5387`](#getpedmakeuprgbcolor) to get the makeup colors.

**Nombres antiguos (alias):** `0x4852FC386E2E1BB5` (`N_0x4852fc386e2e1bb5`), `_GET_HAIR_RGB_COLOR` (`GetHairRgbColor`)

---
### GetPedHeadBlendData

`GET_PED_HEAD_BLEND_DATA` · hash `0x2746BD9D88C5C5D0` · jhash `0x44E1680C` · **Cliente**

```lua
local retval, headBlendData = GetPedHeadBlendData(ped, headBlendData)
```
```c
BOOL GET_PED_HEAD_BLEND_DATA(Ped ped, Any* headBlendData);
```

**Parámetros**

- `ped` (`Ped`)
- `headBlendData` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
The pointer is to a padded struct that matches the arguments to SET_PED_HEAD_BLEND_DATA(...). There are 4 bytes of padding after each field.  
pass this struct in the second parameter   
typedef struct  
{  
        int shapeFirst, shapeSecond, shapeThird;   
        int skinFirst, skinSecond, skinThird;   
	float shapeMix, skinMix, thirdMix;  
} headBlendData;  
```

**Nombres antiguos (alias):** `_GET_PED_HEAD_BLEND_DATA` (`GetPedHeadBlendData`)

---
### GetPedHeadBlendFirstIndex

`GET_PED_HEAD_BLEND_FIRST_INDEX` · hash `0x68D353AB88B97E0C` · jhash `0x211DEFEC` · **Cliente**

```lua
local retval = GetPedHeadBlendFirstIndex(type)
```
```c
int GET_PED_HEAD_BLEND_FIRST_INDEX(int type);
```

**Parámetros**

- `type` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Type equals 0 for male non-dlc, 1 for female non-dlc, 2 for male dlc, and 3 for female dlc.
Used when calling SET_PED_HEAD_BLEND_DATA.
```

**Nombres antiguos (alias):** `_GET_FIRST_PARENT_ID_FOR_PED_TYPE` (`GetFirstParentIdForPedType`)

---
### GetPedHeadBlendNumHeads

`GET_PED_HEAD_BLEND_NUM_HEADS` · hash `0x5EF37013A6539C9D` · jhash `0x095D3BD8` · **Cliente**

```lua
local retval = GetPedHeadBlendNumHeads(type)
```
```c
int GET_PED_HEAD_BLEND_NUM_HEADS(int type);
```

**Parámetros**

- `type` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Type equals 0 for male non-dlc, 1 for female non-dlc, 2 for male dlc, and 3 for female dlc.  
```

**Nombres antiguos (alias):** `_GET_NUM_PARENT_PEDS_OF_TYPE` (`GetNumParentPedsOfType`)

---
### GetPedHeadOverlayNum

`GET_PED_HEAD_OVERLAY_NUM` · hash `0xCF1CE768BB43480E` · jhash `0xFF43C18D` · **Cliente**

```lua
local retval = GetPedHeadOverlayNum(overlayID)
```
```c
int GET_PED_HEAD_OVERLAY_NUM(int overlayID);
```

**Parámetros**

- `overlayID` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Used with freemode (online) characters.
```

**Nombres antiguos (alias):** `_GET_NUM_HEAD_OVERLAY_VALUES` (`GetNumHeadOverlayValues`)

---
### GetPedHeadOverlayValue

`_GET_PED_HEAD_OVERLAY_VALUE` · hash `0xA60EF3B6461A4D43` · **Cliente**

```lua
local retval = GetPedHeadOverlayValue(ped, overlayID)
```
```c
int _GET_PED_HEAD_OVERLAY_VALUE(Ped ped, int overlayID);
```

**Parámetros**

- `ped` (`Ped`)
- `overlayID` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Likely a char, if that overlay is not set, e.i. "None" option, returns 255;
This might be the once removed native GET_PED_HEAD_OVERLAY.
```

---
### GetPedHelmetStoredHatPropIndex

`GET_PED_HELMET_STORED_HAT_PROP_INDEX` · hash `0x451294E859ECC018` · jhash `0x8A3A3116` · **Cliente**

```lua
local retval = GetPedHelmetStoredHatPropIndex(ped)
```
```c
int GET_PED_HELMET_STORED_HAT_PROP_INDEX(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x451294E859ECC018` (`N_0x451294e859ecc018`)

---
### GetPedHelmetStoredHatTexIndex

`GET_PED_HELMET_STORED_HAT_TEX_INDEX` · hash `0x9D728C1E12BF5518` · jhash `0x74EB662D` · **Cliente**

```lua
local retval = GetPedHelmetStoredHatTexIndex(ped)
```
```c
int GET_PED_HELMET_STORED_HAT_TEX_INDEX(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x9D728C1E12BF5518` (`N_0x9d728c1e12bf5518`)

---
### GetPedLastDamageBone

`GET_PED_LAST_DAMAGE_BONE` · hash `0xD75960F6BD9EA49C` · jhash `0xAB933841` · **Cliente**

```lua
local retval, outBone = GetPedLastDamageBone(ped, outBone)
```
```c
BOOL GET_PED_LAST_DAMAGE_BONE(Ped ped, int* outBone);
```

**Parámetros**

- `ped` (`Ped`)
- `outBone` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### GetPedMakeupRgbColor

`_GET_PED_MAKEUP_RGB_COLOR` · hash `0x013E5CFC38CD5387` · **Cliente**

```lua
local outR, outG, outB = GetPedMakeupRgbColor(makeupColorIndex)
```
```c
void _GET_PED_MAKEUP_RGB_COLOR(int makeupColorIndex, int* outR, int* outG, int* outB);
```

**Parámetros**

- `makeupColorIndex` (`int`): The hair color index. Value between 0-63 (inclusive).
- `outR` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Output red value.
- `outG` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Output green value.
- `outB` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Output blue value.

**Devuelve:** `void`

**Descripción oficial:**

Input: Makeup color index, value between 0 and 63 (inclusive).
Output: RGB values for the makeup color specified in the input.

This is used with the makeup color swatches scaleform.

Use [`_0x4852FC386E2E1BB5`](#getpedhairrgbcolor) to get the hair colors.

**Nombres antiguos (alias):** `0x013E5CFC38CD5387` (`N_0x013e5cfc38cd5387`), `_GET_MAKEUP_RGB_COLOR` (`GetMakeupRgbColor`)

---
### GetPedMaxHealth

`GET_PED_MAX_HEALTH` · hash `0x4700A416E8324EF3` · jhash `0xA45B6C8D` · **Cliente**

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
### GetPedMoney

`GET_PED_MONEY` · hash `0x3F69145BBA87BAE7` · jhash `0xEB3C4C7E` · **Cliente**

```lua
local retval = GetPedMoney(ped)
```
```c
int GET_PED_MONEY(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetPedNearbyPeds

`GET_PED_NEARBY_PEDS` · hash `0x23F8F5FC7E8C4A6B` · jhash `0x4D3325F4` · **Cliente**

```lua
local retval, sizeAndPeds = GetPedNearbyPeds(ped, ignore)
```
```c
int GET_PED_NEARBY_PEDS(Ped ped, int* sizeAndPeds, int ignore);
```

**Parámetros**

- `ped` (`Ped`)
- `sizeAndPeds` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `ignore` (`int`): Ped type to ignore

**Devuelve:** `int`

**Descripción oficial:**

Console/PC structure definitions and example: pastebin.com/SsFej963

For FiveM/Cfx.Re use-cases refer to: [`GET_GAME_POOL`](../cfx/compartidos.md#getgamepool).

---
### GetPedNearbyVehicles

`GET_PED_NEARBY_VEHICLES` · hash `0xCFF869CBFA210D82` · jhash `0xCB716F68` · **Cliente**

```lua
local retval, sizeAndVehs = GetPedNearbyVehicles(ped, sizeAndVehs)
```
```c
int GET_PED_NEARBY_VEHICLES(Ped ped, int* sizeAndVehs);
```

**Parámetros**

- `ped` (`Ped`)
- `sizeAndVehs` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

**Descripción oficial:**

```
Returns size of array, passed into the second variable.  
See below for usage information.  
This function actually requires a struct, where the first value is the maximum number of elements to return.  Here is a sample of how I was able to get it to work correctly, without yet knowing the struct format.  
//Setup the array  
	const int numElements = 10;  
	const int arrSize = numElements * 2 + 2;  
	Any veh[arrSize];  
	//0 index is the size of the array  
	veh[0] = numElements;  
	int count = PED::GET_PED_NEARBY_VEHICLES(PLAYER::PLAYER_PED_ID(), veh);  
	if (veh != NULL)  
	{  
//Simple loop to go through results  
for (int i = 0; i < count; i++)  
{  
	int offsettedID = i * 2 + 2;  
	//Make sure it exists  
	if (veh[offsettedID] != NULL && ENTITY::DOES_ENTITY_EXIST(veh[offsettedID]))  
	{  
//Do something  
	}  
}  
	}    
Here's the right way to do it (console and pc):  
pastebin.com/SsFej963  
```

---
### GetPedPaletteVariation

`GET_PED_PALETTE_VARIATION` · hash `0xE3DD5F2A84B42281` · jhash `0xEF1BC082` · **Cliente**

```lua
local retval = GetPedPaletteVariation(ped, componentId)
```
```c
int GET_PED_PALETTE_VARIATION(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component id to get the palette variation from. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).

**Devuelve:** `int`

---
### GetPedParachuteLandingType

`GET_PED_PARACHUTE_LANDING_TYPE` · hash `0x8B9F1FC6AE8166C0` · jhash `0x01F3B035` · **Cliente**

```lua
local retval = GetPedParachuteLandingType(ped)
```
```c
int GET_PED_PARACHUTE_LANDING_TYPE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
-1: no landing  
0: landing on both feet  
1: stumbling  
2: rolling  
3: ragdoll  
```

---
### GetPedParachuteState

`GET_PED_PARACHUTE_STATE` · hash `0x79CFD9827CC979B6` · jhash `0x7D4BC475` · **Cliente**

```lua
local retval = GetPedParachuteState(ped)
```
```c
int GET_PED_PARACHUTE_STATE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns:  
-1: Normal  
0: Wearing parachute on back  
1: Parachute opening  
2: Parachute open  
3: Falling to doom (e.g. after exiting parachute)  
Normal means no parachute?  
```

---
### GetPedParachuteTintIndex

`GET_PED_PARACHUTE_TINT_INDEX` · hash `0xEAF5F7E5AE7C6C9D` · jhash `0xE9E7FAC5` · **Cliente**

```lua
local outTintIndex = GetPedParachuteTintIndex(ped, outTintIndex)
```
```c
void GET_PED_PARACHUTE_TINT_INDEX(Ped ped, int* outTintIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `outTintIndex` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetPedPropIndex

`GET_PED_PROP_INDEX` · hash `0x898CC20EA75BACD8` · jhash `0x746DDAC0` · **Cliente**

```lua
local retval = GetPedPropIndex(ped, componentId)
```
```c
int GET_PED_PROP_INDEX(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component id to get the prop index from. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).

**Devuelve:** `int`

---
### GetPedPropTextureIndex

`GET_PED_PROP_TEXTURE_INDEX` · hash `0xE131A28626F81AB2` · jhash `0x922A6653` · **Cliente**

```lua
local retval = GetPedPropTextureIndex(ped, componentId)
```
```c
int GET_PED_PROP_TEXTURE_INDEX(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component id to get the prop texture index from. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).

**Devuelve:** `int`

---
### GetPedRagdollBoneIndex

`GET_PED_RAGDOLL_BONE_INDEX` · hash `0x2057EF813397A772` · jhash `0x849F0716` · **Cliente**

```lua
local retval = GetPedRagdollBoneIndex(ped, bone)
```
```c
int GET_PED_RAGDOLL_BONE_INDEX(Ped ped, int bone);
```

**Parámetros**

- `ped` (`Ped`)
- `bone` (`int`)

**Devuelve:** `int`

---
### GetPedRelationshipGroupDefaultHash

`GET_PED_RELATIONSHIP_GROUP_DEFAULT_HASH` · hash `0x42FDD0F017B1E38E` · jhash `0x714BD6E4` · **Cliente**

```lua
local retval = GetPedRelationshipGroupDefaultHash(ped)
```
```c
Hash GET_PED_RELATIONSHIP_GROUP_DEFAULT_HASH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Hash`

---
### GetPedRelationshipGroupHash

`GET_PED_RELATIONSHIP_GROUP_HASH` · hash `0x7DBDD04862D95F04` · jhash `0x354F283C` · **Cliente**

```lua
local retval = GetPedRelationshipGroupHash(ped)
```
```c
Hash GET_PED_RELATIONSHIP_GROUP_HASH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Hash`

---
### GetPedResetFlag

`GET_PED_RESET_FLAG` · hash `0xAF9E59B1B1FBF2A0` · jhash `0x2FC10D11` · **Cliente**

```lua
local retval = GetPedResetFlag(ped, flagId)
```
```c
BOOL GET_PED_RESET_FLAG(Ped ped, int flagId);
```

**Parámetros**

- `ped` (`Ped`)
- `flagId` (`int`)

**Devuelve:** `BOOL`

---
### GetPedSourceOfDeath

`GET_PED_SOURCE_OF_DEATH` · hash `0x93C8B64DEB84728C` · jhash `0x84ADF9EB` · **Cliente**

```lua
local retval = GetPedSourceOfDeath(ped)
```
```c
Entity GET_PED_SOURCE_OF_DEATH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Entity`

**Descripción oficial:**

```
Returns the Entity (Ped, Vehicle, or ?Object?) that killed the 'ped'  
Is best to check if the Ped is dead before asking for its killer.  
```

**Nombres antiguos (alias):** `_GET_PED_KILLER` (`GetPedKiller`)

---
### GetPedStealthMovement

`GET_PED_STEALTH_MOVEMENT` · hash `0x7C2AC9CA66575FBF` · jhash `0x40321B83` · **Cliente**

```lua
local retval = GetPedStealthMovement(ped)
```
```c
BOOL GET_PED_STEALTH_MOVEMENT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the entity is in stealth mode  
```

---
### GetPedTaskCombatTarget

`_GET_PED_TASK_COMBAT_TARGET` · hash `0x32C27A11307B01CC` · **Cliente**

```lua
local retval = GetPedTaskCombatTarget(ped, p1)
```
```c
Entity _GET_PED_TASK_COMBAT_TARGET(Ped ped, Any p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any`)

**Devuelve:** `Entity`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x32C27A11307B01CC` (`N_0x32c27a11307b01cc`)

---
### GetPedTextureVariation

`GET_PED_TEXTURE_VARIATION` · hash `0x04A355E041E004E6` · jhash `0xC0A8590A` · **Cliente**

```lua
local retval = GetPedTextureVariation(ped, componentId)
```
```c
int GET_PED_TEXTURE_VARIATION(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component id to get the texture variation from. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).

**Devuelve:** `int`

---
### GetPedTimeOfDeath

`GET_PED_TIME_OF_DEATH` · hash `0x1E98817B311AE98A` · jhash `0xDF6D5D54` · **Cliente**

```lua
local retval = GetPedTimeOfDeath(ped)
```
```c
int GET_PED_TIME_OF_DEATH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `_GET_PED_TIME_OF_DEATH` (`GetPedTimeOfDeath`), `0x1E98817B311AE98A` (`N_0x1e98817b311ae98a`)

---
### GetPedType

`GET_PED_TYPE` · hash `0xFF059E1E4C01E63C` · jhash `0xB1460D43` · **Cliente**

```lua
local retval = GetPedType(ped)
```
```c
int GET_PED_TYPE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

Ped types:

```cpp
enum ePedType
{
	PED_TYPE_PLAYER_0 = 0,
	PED_TYPE_PLAYER_1 = 1,
	PED_TYPE_NETWORK_PLAYER = 2,
	PED_TYPE_PLAYER_2 = 3,
	PED_TYPE_CIVMALE = 4,
	PED_TYPE_CIVFEMALE = 5,
	PED_TYPE_COP = 6,
	PED_TYPE_GANG_ALBANIAN = 7,
	PED_TYPE_GANG_BIKER_1 = 8,
	PED_TYPE_GANG_BIKER_2 = 9,
	PED_TYPE_GANG_ITALIAN = 10,
	PED_TYPE_GANG_RUSSIAN = 11,
	PED_TYPE_GANG_RUSSIAN_2 = 12,
	PED_TYPE_GANG_IRISH = 13,
	PED_TYPE_GANG_JAMAICAN = 14,
	PED_TYPE_GANG_AFRICAN_AMERICAN = 15,
	PED_TYPE_GANG_KOREAN = 16,
	PED_TYPE_GANG_CHINESE_JAPANESE = 17,
	PED_TYPE_GANG_PUERTO_RICAN = 18,
	PED_TYPE_DEALER = 19,
	PED_TYPE_MEDIC = 20,
	PED_TYPE_FIREMAN = 21,
	PED_TYPE_CRIMINAL = 22,
	PED_TYPE_BUM = 23,
	PED_TYPE_PROSTITUTE = 24,
	PED_TYPE_SPECIAL = 25,
	PED_TYPE_MISSION = 26,
	PED_TYPE_SWAT = 27,
	PED_TYPE_ANIMAL = 28,
	PED_TYPE_ARMY = 29
};
```

---
### GetPedVisualFieldCenterAngle

`_GET_PED_VISUAL_FIELD_CENTER_ANGLE` · hash `0xEF2C71A32CAD5FBD` · **Cliente**

```lua
local retval = GetPedVisualFieldCenterAngle(ped)
```
```c
float _GET_PED_VISUAL_FIELD_CENTER_ANGLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### GetPedheadshotTxdString

`GET_PEDHEADSHOT_TXD_STRING` · hash `0xDB4EACD4AD0A5D6B` · jhash `0x76D28E96` · **Cliente**

```lua
local retval = GetPedheadshotTxdString(id)
```
```c
char* GET_PEDHEADSHOT_TXD_STRING(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
gtaforums.com/topic/885580-ped-headshotmugshot-txd/  
```

---
### GetPedsJacker

`GET_PEDS_JACKER` · hash `0x9B128DC36C1E04CF` · jhash `0xDE1DBB59` · **Cliente**

```lua
local retval = GetPedsJacker(ped)
```
```c
Ped GET_PEDS_JACKER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Ped`

---
### GetPlayerPedIsFollowing

`GET_PLAYER_PED_IS_FOLLOWING` · hash `0x6A3975DEA89F9A17` · jhash `0xDE7442EE` · **Cliente**

```lua
local retval = GetPlayerPedIsFollowing(ped)
```
```c
Player GET_PLAYER_PED_IS_FOLLOWING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Player`

---
### GetRandomPedAtCoord

`GET_RANDOM_PED_AT_COORD` · hash `0x876046A8E3A4B71C` · jhash `0xDC8239EB` · **Cliente**

```lua
local retval = GetRandomPedAtCoord(x, y, z, xRadius, yRadius, zRadius, pedType)
```
```c
Ped GET_RANDOM_PED_AT_COORD(float x, float y, float z, float xRadius, float yRadius, float zRadius, int pedType);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `xRadius` (`float`)
- `yRadius` (`float`)
- `zRadius` (`float`)
- `pedType` (`int`)

**Devuelve:** `Ped`

**Descripción oficial:**

```
Gets a random ped in the x/y/zRadius near the x/y/z coordinates passed.   
Ped Types:  
Any = -1  
Player = 1  
Male = 4   
Female = 5   
Cop = 6  
Human = 26  
SWAT = 27   
Animal = 28  
Army = 29  
```

---
### GetRelationshipBetweenGroups

`GET_RELATIONSHIP_BETWEEN_GROUPS` · hash `0x9E6B70061662AE5C` · jhash `0x4E372FE2` · **Cliente**

```lua
local retval = GetRelationshipBetweenGroups(group1, group2)
```
```c
int GET_RELATIONSHIP_BETWEEN_GROUPS(Hash group1, Hash group2);
```

**Parámetros**

- `group1` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `group2` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the relationship between two groups. This should be called twice (once for each group).  
Relationship types:  
0 = Companion  
1 = Respect  
2 = Like  
3 = Neutral  
4 = Dislike  
5 = Hate  
255 = Pedestrians  
Example:  
PED::GET_RELATIONSHIP_BETWEEN_GROUPS(l_1017, 0xA49E591C);  
PED::GET_RELATIONSHIP_BETWEEN_GROUPS(0xA49E591C, l_1017);  
```

---
### GetRelationshipBetweenPeds

`GET_RELATIONSHIP_BETWEEN_PEDS` · hash `0xEBA5AD3A0EAF7121` · jhash `0xE254C39C` · **Cliente**

```lua
local retval = GetRelationshipBetweenPeds(ped1, ped2)
```
```c
int GET_RELATIONSHIP_BETWEEN_PEDS(Ped ped1, Ped ped2);
```

**Parámetros**

- `ped1` (`Ped`)
- `ped2` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the relationship between two peds. This should be called twice (once for each ped).  
Relationship types:  
0 = Companion  
1 = Respect  
2 = Like  
3 = Neutral  
4 = Dislike  
5 = Hate  
255 = Pedestrians  
(Credits: Inco)  
Example:  
PED::GET_RELATIONSHIP_BETWEEN_PEDS(2, l_1017, 0xA49E591C);  
PED::GET_RELATIONSHIP_BETWEEN_PEDS(2, 0xA49E591C, l_1017);  
```

---
### GetSeatPedIsTryingToEnter

`GET_SEAT_PED_IS_TRYING_TO_ENTER` · hash `0x6F4C85ACD641BCD2` · jhash `0xACF162E0` · **Cliente**

```lua
local retval = GetSeatPedIsTryingToEnter(ped)
```
```c
int GET_SEAT_PED_IS_TRYING_TO_ENTER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

---
### GetSynchronizedScenePhase

`GET_SYNCHRONIZED_SCENE_PHASE` · hash `0xE4A310B1D7FA73CC` · jhash `0xB0B2C852` · **Cliente**

```lua
local retval = GetSynchronizedScenePhase(sceneID)
```
```c
float GET_SYNCHRONIZED_SCENE_PHASE(int sceneID);
```

**Parámetros**

- `sceneID` (`int`)

**Devuelve:** `float`

---
### GetSynchronizedSceneRate

`GET_SYNCHRONIZED_SCENE_RATE` · hash `0xD80932D577274D40` · jhash `0x89365F0D` · **Cliente**

```lua
local retval = GetSynchronizedSceneRate(sceneID)
```
```c
float GET_SYNCHRONIZED_SCENE_RATE(int sceneID);
```

**Parámetros**

- `sceneID` (`int`)

**Devuelve:** `float`

---
### GetTimeOfLastPedWeaponDamage

`_GET_TIME_OF_LAST_PED_WEAPON_DAMAGE` · hash `0x36B77BB84687C318` · jhash `0x0170C6E1` · **Cliente**

```lua
local retval = GetTimeOfLastPedWeaponDamage(ped, weaponHash)
```
```c
int _GET_TIME_OF_LAST_PED_WEAPON_DAMAGE(Ped ped, Hash weaponHash);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
GET_TIME_*
```

**Nombres antiguos (alias):** `0x36B77BB84687C318` (`N_0x36b77bb84687c318`)

---
### GetVehiclePedIsEntering

`GET_VEHICLE_PED_IS_ENTERING` · hash `0xF92691AED837A5FC` · jhash `0x56E0C163` · **Cliente**

```lua
local retval = GetVehiclePedIsEntering(ped)
```
```c
Vehicle GET_VEHICLE_PED_IS_ENTERING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Vehicle`

**Nombres antiguos (alias):** `SET_EXCLUSIVE_PHONE_RELATIONSHIPS` (`SetExclusivePhoneRelationships`)

---
### GetVehiclePedIsIn

`GET_VEHICLE_PED_IS_IN` · hash `0x9A9112A0FE9A4713` · jhash `0xAFE92319` · **Cliente**

```lua
local retval = GetVehiclePedIsIn(ped, lastVehicle)
```
```c
Vehicle GET_VEHICLE_PED_IS_IN(Ped ped, BOOL lastVehicle);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `lastVehicle` (`BOOL`): A boolean value where `false` represents the current vehicle the Ped is in, and `true` represents the last vehicle the Ped was in.

**Devuelve:** `Vehicle` — The vehicle id. Returns 0 if the ped is/was not in a vehicle.

**Descripción oficial:**

Retrieves the vehicle the specified ped is currently in, or the last vehicle they were in.

**Ejemplo (lua):**

```lua
-- This example gets the vehicle the player is currently in and print the vehicle id.

-- Retrieve the LocalPlayer.
local playerPed = PlayerPedId()

-- Retrieve the vehicle the player is currently in. 
local vehicle = GetVehiclePedIsIn(playerPed, false)

-- Check if the vehicle exists in the game world.
if not DoesEntityExist(vehicle) then 
    -- If the vehicle does not exist, end the execution of the code here.
    return 
end

-- Print the vehicle id
print("Vehicle ID: " .. vehicle)
```

**Ejemplo (js):**

```js
// This example gets the vehicle the player is currently in and print the vehicle id.

// Retrieve the player ped.
const playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
const vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// Print the vehicle id
console.log(`Vehicle ID: ${vehicle}`);
```

**Ejemplo (cs):**

```cs
// This example gets the vehicle the player is currently in and print the vehicle id.
using static CitizenFX.Core.Native.API;

// Retrieve the player ped
int playerPed = PlayerPedId();

// Retrieve the vehicle the player is currently in.
int vehicle = GetVehiclePedIsIn(playerPed, false);

// Check if the vehicle exists in the game world.
if (!DoesEntityExist(vehicle)) {
    // If the vehicle does not exist, end the execution of the code here.
    return;
}

// Print the vehicle id
Debug.WriteLine($"Vehicle ID: {vehicle}");
```

---
### GetVehiclePedIsTryingToEnter

`GET_VEHICLE_PED_IS_TRYING_TO_ENTER` · hash `0x814FA8BE5449445D` · jhash `0x99968B37` · **Cliente**

```lua
local retval = GetVehiclePedIsTryingToEnter(ped)
```
```c
Vehicle GET_VEHICLE_PED_IS_TRYING_TO_ENTER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Vehicle`

---
### GetVehiclePedIsUsing

`GET_VEHICLE_PED_IS_USING` · hash `0x6094AD011A2EA87D` · jhash `0x6DE3AADA` · **Cliente**

```lua
local retval = GetVehiclePedIsUsing(ped)
```
```c
Vehicle GET_VEHICLE_PED_IS_USING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Vehicle`

**Descripción oficial:**

```
Gets ID of vehicle player using. It means it can get ID at any interaction with vehicle. Enter\exit for example. And that means it is faster than GET_VEHICLE_PED_IS_IN but less safe.  
```

---
### GivePedHelmet

`GIVE_PED_HELMET` · hash `0x54C7C4A94367717E` · jhash `0x1862A461` · **Cliente**

```lua
GivePedHelmet(ped, cannotRemove, helmetFlag, textureIndex)
```
```c
void GIVE_PED_HELMET(Ped ped, BOOL cannotRemove, int helmetFlag, int textureIndex);
```

**Parámetros**

- `ped` (`Ped`): Ped index.
- `cannotRemove` (`BOOL`): Can remove helmet or not.
- `helmetFlag` (`int`): Flag for the helmet, the helmet appearance depends on the ped it's being applied on.
- `textureIndex` (`int`): Texture index; any value other than `-1` will overwrite the default texture index. The helmet texture index needs to be valid for it to be applied.

**Devuelve:** `void`

**Descripción oficial:**

Gives the ped a helmet. Can be removed by invoking [`REMOVE_PED_HELMET`](#removepedhelmet).

```cpp
enum ePedCompFlags {
  PV_FLAG_NONE                  = 0, // 0
  PV_FLAG_BULKY                 = 1, // 1<<0
  PV_FLAG_JOB                   = 2, // 1<<1
  PV_FLAG_SUNNY                 = 4, // 1<<2
  PV_FLAG_WET                   = 8, // 1<<3
  PV_FLAG_COLD                  = 16, // 1<<4
  PV_FLAG_NOT_IN_CAR            = 32, // 1<<5
  PV_FLAG_BIKE_ONLY             = 64, // 1<<6
  PV_FLAG_NOT_INDOORS           = 128, // 1<<7
  PV_FLAG_FIRE_RETARDENT        = 256, // 1<<8
  PV_FLAG_ARMOURED              = 512, // 1<<9
  PV_FLAG_LIGHTLY_ARMOURED      = 1024, // 1<<10
  PV_FLAG_HIGH_DETAIL           = 2048, // 1<<11
  PV_FLAG_DEFAULT_HELMET        = 4096, // 1<<12
  PV_FLAG_RANDOM_HELMET         = 8192, // 1<<13
  PV_FLAG_SCRIPT_HELMET         = 16384, // 1<<14
  PV_FLAG_FLIGHT_HELMET         = 32768, // 1<<15
  PV_FLAG_HIDE_IN_FIRST_PERSON  = 65536, // 1<<16
  PV_FLAG_USE_PHYSICS_HAT_2     = 131072, // 1<<17
  PV_FLAG_PILOT_HELMET          = 262144 // 1<<18
};
```

---
### GivePedNmMessage

`GIVE_PED_NM_MESSAGE` · hash `0xB158DFCCC56E5C5B` · jhash `0x737C3689` · **Cliente**

```lua
GivePedNmMessage(ped)
```
```c
void GIVE_PED_NM_MESSAGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sends the message that was created by a call to CREATE_NM_MESSAGE to the specified Ped.  
If a message hasn't been created already, this function does nothing.  
If the Ped is not ragdolled with Euphoria enabled, this function does nothing.  
The following call can be used to ragdoll the Ped with Euphoria enabled: SET_PED_TO_RAGDOLL(ped, 4000, 5000, 1, 1, 1, 0);  
Call order:  
SET_PED_TO_RAGDOLL  
CREATE_NM_MESSAGE  
GIVE_PED_NM_MESSAGE  
Multiple messages can be chained. Eg. to make the ped stagger and swing his arms around, the following calls can be made:  
SET_PED_TO_RAGDOLL(ped, 4000, 5000, 1, 1, 1, 0);  
CREATE_NM_MESSAGE(true, 0); // stopAllBehaviours - Stop all other behaviours, in case the Ped is already doing some Euphoria stuff.  
GIVE_PED_NM_MESSAGE(ped); // Dispatch message to Ped.  
CREATE_NM_MESSAGE(true, 1151); // staggerFall - Attempt to walk while falling.  
GIVE_PED_NM_MESSAGE(ped); // Dispatch message to Ped.  
CREATE_NM_MESSAGE(true, 372); // armsWindmill - Swing arms around.  
GIVE_PED_NM_MESSAGE(ped); // Dispatch message to Ped.  
```

---
### HasActionModeAssetLoaded

`HAS_ACTION_MODE_ASSET_LOADED` · hash `0xE4B5F4BF2CB24E65` · jhash `0xF7EB2BF1` · **Cliente**

```lua
local retval = HasActionModeAssetLoaded(asset)
```
```c
BOOL HAS_ACTION_MODE_ASSET_LOADED(char* asset);
```

**Parámetros**

- `asset` (`char*`)

**Devuelve:** `BOOL`

---
### HasPedHeadBlendFinished

`HAS_PED_HEAD_BLEND_FINISHED` · hash `0x654CD0A825161131` · jhash `0x2B1BD9C5` · **Cliente**

```lua
local retval = HasPedHeadBlendFinished(ped)
```
```c
BOOL HAS_PED_HEAD_BLEND_FINISHED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### HasPedPreloadPropDataFinished

`HAS_PED_PRELOAD_PROP_DATA_FINISHED` · hash `0x784002A632822099` · jhash `0x3B0CA391` · **Cliente**

```lua
local retval = HasPedPreloadPropDataFinished(ped)
```
```c
BOOL HAS_PED_PRELOAD_PROP_DATA_FINISHED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x784002A632822099` (`N_0x784002a632822099`)

---
### HasPedPreloadVariationDataFinished

`HAS_PED_PRELOAD_VARIATION_DATA_FINISHED` · hash `0x66680A92700F43DF` · jhash `0xC6517D52` · **Cliente**

```lua
local retval = HasPedPreloadVariationDataFinished(ped)
```
```c
BOOL HAS_PED_PRELOAD_VARIATION_DATA_FINISHED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x66680A92700F43DF` (`N_0x66680a92700f43df`)

---
### HasPedReceivedEvent

`HAS_PED_RECEIVED_EVENT` · hash `0x8507BCB710FA6DC0` · jhash `0xECD73DB0` · **Cliente**

```lua
local retval = HasPedReceivedEvent(ped, eventId)
```
```c
BOOL HAS_PED_RECEIVED_EVENT(Ped ped, int eventId);
```

**Parámetros**

- `ped` (`Ped`)
- `eventId` (`int`)

**Devuelve:** `BOOL`

---
### HasPedheadshotImgUploadFailed

`HAS_PEDHEADSHOT_IMG_UPLOAD_FAILED` · hash `0x876928DDDFCCC9CD` · jhash `0x05023F8F` · **Cliente**

```lua
local retval = HasPedheadshotImgUploadFailed()
```
```c
BOOL HAS_PEDHEADSHOT_IMG_UPLOAD_FAILED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x876928DDDFCCC9CD` (`N_0x876928dddfccc9cd`)

---
### HasPedheadshotImgUploadSucceeded

`HAS_PEDHEADSHOT_IMG_UPLOAD_SUCCEEDED` · hash `0xE8A169E666CBC541` · jhash `0xAA39FD6C` · **Cliente**

```lua
local retval = HasPedheadshotImgUploadSucceeded()
```
```c
BOOL HAS_PEDHEADSHOT_IMG_UPLOAD_SUCCEEDED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE8A169E666CBC541` (`N_0xe8a169e666cbc541`)

---
### HasStealthModeAssetLoaded

`HAS_STEALTH_MODE_ASSET_LOADED` · hash `0xE977FC5B08AF3441` · jhash `0x39245667` · **Cliente**

```lua
local retval = HasStealthModeAssetLoaded(asset)
```
```c
BOOL HAS_STEALTH_MODE_ASSET_LOADED(char* asset);
```

**Parámetros**

- `asset` (`char*`)

**Devuelve:** `BOOL`

---
### HaveAllStreamingRequestsCompleted

`HAVE_ALL_STREAMING_REQUESTS_COMPLETED` · hash `0x7350823473013C02` · jhash `0xF9FB4B71` · **Cliente**

```lua
local retval = HaveAllStreamingRequestsCompleted(ped)
```
```c
BOOL HAVE_ALL_STREAMING_REQUESTS_COMPLETED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x7350823473013C02` (`N_0x7350823473013c02`), `_HAS_STREAMED_PED_ASSETS_LOADED` (`HasStreamedPedAssetsLoaded`)

---
### HidePedBloodDamageByZone

`HIDE_PED_BLOOD_DAMAGE_BY_ZONE` · hash `0x62AB793144DE75DC` · jhash `0x0CB6C4ED` · **Cliente**

```lua
HidePedBloodDamageByZone(ped, p1, p2)
```
```c
void HIDE_PED_BLOOD_DAMAGE_BY_ZONE(Ped ped, Any p1, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x62AB793144DE75DC` (`N_0x62ab793144de75dc`)

---
### InstantlyFillPedPopulation

`INSTANTLY_FILL_PED_POPULATION` · hash `0x4759CC730F947C81` · jhash `0x8C555ADD` · **Cliente**

```lua
InstantlyFillPedPopulation()
```
```c
void INSTANTLY_FILL_PED_POPULATION();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4759CC730F947C81` (`N_0x4759cc730f947c81`)

---
### IsAnyHostilePedNearPoint

`IS_ANY_HOSTILE_PED_NEAR_POINT` · hash `0x68772DB2B2526F9F` · jhash `0x1A464167` · **Cliente**

```lua
local retval = IsAnyHostilePedNearPoint(ped, x, y, z, radius)
```
```c
BOOL IS_ANY_HOSTILE_PED_NEAR_POINT(Ped ped, float x, float y, float z, float radius);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x68772DB2B2526F9F` (`N_0x68772db2b2526f9f`)

---
### IsAnyPedNearPoint

`IS_ANY_PED_NEAR_POINT` · hash `0x083961498679DC9F` · jhash `0xFBD9B050` · **Cliente**

```lua
local retval = IsAnyPedNearPoint(x, y, z, radius)
```
```c
BOOL IS_ANY_PED_NEAR_POINT(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

---
### IsAnyPedShootingInArea

`IS_ANY_PED_SHOOTING_IN_AREA` · hash `0xA0D3D71EA1086C55` · jhash `0x91833867` · **Cliente**

```lua
local retval = IsAnyPedShootingInArea(minX, minY, minZ, maxX, maxY, maxZ, bHighlightArea, bDo3DCheck)
```
```c
BOOL IS_ANY_PED_SHOOTING_IN_AREA(float minX, float minY, float minZ, float maxX, float maxY, float maxZ, BOOL bHighlightArea, BOOL bDo3DCheck);
```

**Parámetros**

- `minX` (`float`): Minimum X vector
- `minY` (`float`): Minimum Y vector
- `minZ` (`float`): Minimum Z vector
- `maxX` (`float`): Maximum X vector
- `maxY` (`float`): Maximum Y vector
- `maxZ` (`float`): Maximum Z vector
- `bHighlightArea` (`BOOL`): Highlights the area to check when set to `true`.
- `bDo3DCheck` (`BOOL`): Conducts a 3D height check when set to `true`.

**Devuelve:** `BOOL` — `true` if a ped is within the defined area, `false` otherwise.

**Descripción oficial:**

Verifies whether a ped is firing within a specific area.

---
### IsConversationPedDead

`IS_CONVERSATION_PED_DEAD` · hash `0xE0A0AEC214B1FABA` · jhash `0x1FA39EFE` · **Cliente**

```lua
local retval = IsConversationPedDead(ped)
```
```c
BOOL IS_CONVERSATION_PED_DEAD(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsCopPedInArea_3d

`IS_COP_PED_IN_AREA_3D` · hash `0x16EC4839969F9F5E` · jhash `0xB98DB96B` · **Cliente**

```lua
local retval = IsCopPedInArea_3d(x1, y1, z1, x2, y2, z2)
```
```c
BOOL IS_COP_PED_IN_AREA_3D(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
xyz - relative to the world origin.  
```

---
### IsPedAPlayer

`IS_PED_A_PLAYER` · hash `0x12534C348C6CB68B` · jhash `0x404794CA` · **Cliente**

```lua
local retval = IsPedAPlayer(ped)
```
```c
BOOL IS_PED_A_PLAYER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the given ped has a valid pointer to CPlayerInfo in its CPed class. That's all.
```

---
### IsPedAimingFromCover

`IS_PED_AIMING_FROM_COVER` · hash `0x3998B1276A3300E5` · jhash `0xDEBAB2AF` · **Cliente**

```lua
local retval = IsPedAimingFromCover(ped)
```
```c
BOOL IS_PED_AIMING_FROM_COVER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedBeingJacked

`IS_PED_BEING_JACKED` · hash `0x9A497FE2DF198913` · jhash `0xD45D605C` · **Cliente**

```lua
local retval = IsPedBeingJacked(ped)
```
```c
BOOL IS_PED_BEING_JACKED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedBeingStealthKilled

`IS_PED_BEING_STEALTH_KILLED` · hash `0x863B23EFDE9C5DF2` · jhash `0xD044C8AF` · **Cliente**

```lua
local retval = IsPedBeingStealthKilled(ped)
```
```c
BOOL IS_PED_BEING_STEALTH_KILLED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedBeingStunned

`IS_PED_BEING_STUNNED` · hash `0x4FBACCE3B4138EE8` · jhash `0x0A66CE30` · **Cliente**

```lua
local retval = IsPedBeingStunned(ped, p1)
```
```c
BOOL IS_PED_BEING_STUNNED(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p1 is always 0  
```

---
### IsPedBlushColorValid

`_IS_PED_BLUSH_COLOR_VALID` · hash `0x604E810189EE3A59` · **Cliente**

```lua
local retval = IsPedBlushColorValid(colorID)
```
```c
BOOL _IS_PED_BLUSH_COLOR_VALID(int colorID);
```

**Parámetros**

- `colorID` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x604E810189EE3A59` (`N_0x604e810189ee3a59`)

---
### IsPedBlushColorValid_2

`_IS_PED_BLUSH_COLOR_VALID_2` · hash `0xF41B5D290C99A3D6` · **Cliente**

```lua
local retval = IsPedBlushColorValid_2(colorId)
```
```c
BOOL _IS_PED_BLUSH_COLOR_VALID_2(int colorId);
```

**Parámetros**

- `colorId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF41B5D290C99A3D6` (`N_0xf41b5d290c99a3d6`)

---
### IsPedBodyBlemishValid

`_IS_PED_BODY_BLEMISH_VALID` · hash `0x09E7ECA981D9B210` · **Cliente**

```lua
local retval = IsPedBodyBlemishValid(colorID)
```
```c
BOOL _IS_PED_BODY_BLEMISH_VALID(int colorID);
```

**Parámetros**

- `colorID` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x09E7ECA981D9B210` (`N_0x09e7eca981d9b210`)

---
### IsPedClimbing

`IS_PED_CLIMBING` · hash `0x53E8CB4F48BFE623` · jhash `0xBCE03D35` · **Cliente**

```lua
local retval = IsPedClimbing(ped)
```
```c
BOOL IS_PED_CLIMBING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedComponentVariationValid

`IS_PED_COMPONENT_VARIATION_VALID` · hash `0xE825F6B6CEA7671D` · jhash `0x952ABD9A` · **Cliente**

```lua
local retval = IsPedComponentVariationValid(ped, componentId, drawableId, textureId)
```
```c
BOOL IS_PED_COMPONENT_VARIATION_VALID(Ped ped, int componentId, int drawableId, int textureId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component id to check the variation of. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).
- `drawableId` (`int`): The drawable id to get the component variation of. Refer to [GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS](#getnumberofpedpropdrawablevariations).
- `textureId` (`int`): The texture id to get the component variation of. Refer to [GET_NUMBER_OF_PED_PROP_TEXTURE_VARIATIONS](#getnumberofpedproptexturevariations).

**Devuelve:** `BOOL`

**Descripción oficial:**

Checks if the component variation is valid, this works great for randomizing components using loops.

---
### IsPedDeadOrDying

`IS_PED_DEAD_OR_DYING` · hash `0x3317DEDB88C95038` · jhash `0xCBDB7739` · **Cliente**

```lua
local retval = IsPedDeadOrDying(ped, checkMeleeDeathFlags)
```
```c
BOOL IS_PED_DEAD_OR_DYING(Ped ped, BOOL checkMeleeDeathFlags);
```

**Parámetros**

- `ped` (`Ped`): The ped to check.
- `checkMeleeDeathFlags` (`BOOL`): If set to `true`, extends the check to include melee takedown moves as part of the dying phase.

**Devuelve:** `BOOL` — Returns `true` if the ped is dead. When `checkMeleeDeathFlags` is set to `true`, it also considers peds in melee takedown moves as dying, although the broader 'dying' phase may not be detected.

**Descripción oficial:**

Determines if a ped is dead. Contrary to what the name might suggest, it does not always detect when a ped is in the 'dying' phase (transitioning to death). The exception is when `checkMeleeDeathFlags` is set to `true`, which then includes peds in the midst of melee takedown moves as being in a dying state, even if the death task has not yet started.

```
NativeDB Introduced: v323
```

---
### IsPedDefensiveAreaActive

`IS_PED_DEFENSIVE_AREA_ACTIVE` · hash `0xBA63D9FE45412247` · jhash `0x6D88BCD3` · **Cliente**

```lua
local retval = IsPedDefensiveAreaActive(ped, p1)
```
```c
BOOL IS_PED_DEFENSIVE_AREA_ACTIVE(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBA63D9FE45412247` (`N_0xba63d9fe45412247`)

---
### IsPedDiving

`IS_PED_DIVING` · hash `0x5527B8246FEF9B11` · jhash `0x7BC5BF3C` · **Cliente**

```lua
local retval = IsPedDiving(ped)
```
```c
BOOL IS_PED_DIVING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedDoingBeastJump

`_IS_PED_DOING_BEAST_JUMP` · hash `0x451D05012CCEC234` · **Cliente**

```lua
local retval = IsPedDoingBeastJump(ped)
```
```c
BOOL _IS_PED_DOING_BEAST_JUMP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x451D05012CCEC234` (`N_0x451d05012ccec234`)

---
### IsPedDoingDriveby

`IS_PED_DOING_DRIVEBY` · hash `0xB2C086CC1BF8F2BF` · jhash `0xAC3CEB9C` · **Cliente**

```lua
local retval = IsPedDoingDriveby(ped)
```
```c
BOOL IS_PED_DOING_DRIVEBY(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedDucking

`IS_PED_DUCKING` · hash `0xD125AE748725C6BC` · jhash `0x9199C77D` · **Cliente**

```lua
local retval = IsPedDucking(ped)
```
```c
BOOL IS_PED_DUCKING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedEvasiveDiving

`IS_PED_EVASIVE_DIVING` · hash `0x414641C26E105898` · jhash `0xD82829DC` · **Cliente**

```lua
local retval, evadingEntity = IsPedEvasiveDiving(ped, evadingEntity)
```
```c
BOOL IS_PED_EVASIVE_DIVING(Ped ped, Entity* evadingEntity);
```

**Parámetros**

- `ped` (`Ped`)
- `evadingEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Presumably returns the Entity that the Ped is currently diving out of the way of.
var num3;
    if (PED::IS_PED_EVASIVE_DIVING(A_0, &num3) != 0)
        if (ENTITY::IS_ENTITY_A_VEHICLE(num3) != 0)
```

---
### IsPedFacingPed

`IS_PED_FACING_PED` · hash `0xD71649DB0A545AA3` · jhash `0x0B775838` · **Cliente**

```lua
local retval = IsPedFacingPed(ped, otherPed, angle)
```
```c
BOOL IS_PED_FACING_PED(Ped ped, Ped otherPed, float angle);
```

**Parámetros**

- `ped` (`Ped`)
- `otherPed` (`Ped`)
- `angle` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
angle is ped's view cone  
```

---
### IsPedFalling

`IS_PED_FALLING` · hash `0xFB92A102F1C4DFA3` · jhash `0xABF77334` · **Cliente**

```lua
local retval = IsPedFalling(ped)
```
```c
BOOL IS_PED_FALLING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedFatallyInjured

`IS_PED_FATALLY_INJURED` · hash `0xD839450756ED5A80` · jhash `0xBADA0093` · **Cliente**

```lua
local retval = IsPedFatallyInjured(ped)
```
```c
BOOL IS_PED_FATALLY_INJURED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets a value indicating whether this ped's health is below its fatally injured threshold. The default threshold is 100.  
If the handle is invalid, the function returns true.  
```

---
### IsPedFleeing

`IS_PED_FLEEING` · hash `0xBBCCE00B381F8482` · jhash `0x85D813C6` · **Cliente**

```lua
local retval = IsPedFleeing(ped)
```
```c
BOOL IS_PED_FLEEING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedGettingIntoAVehicle

`IS_PED_GETTING_INTO_A_VEHICLE` · hash `0xBB062B2B5722478E` · jhash `0x90E805AC` · **Cliente**

```lua
local retval = IsPedGettingIntoAVehicle(ped)
```
```c
BOOL IS_PED_GETTING_INTO_A_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedGoingIntoCover

`IS_PED_GOING_INTO_COVER` · hash `0x9F65DBC537E59AD5` · jhash `0xA3589628` · **Cliente**

```lua
local retval = IsPedGoingIntoCover(ped)
```
```c
BOOL IS_PED_GOING_INTO_COVER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedGroupMember

`IS_PED_GROUP_MEMBER` · hash `0x9BB01E3834671191` · jhash `0x876D5363` · **Cliente**

```lua
local retval = IsPedGroupMember(ped, groupId)
```
```c
BOOL IS_PED_GROUP_MEMBER(Ped ped, int groupId);
```

**Parámetros**

- `ped` (`Ped`)
- `groupId` (`int`)

**Devuelve:** `BOOL`

---
### IsPedHairColorValid

`_IS_PED_HAIR_COLOR_VALID` · hash `0xE0D36E5D9E99CC21` · **Cliente**

```lua
local retval = IsPedHairColorValid(colorID)
```
```c
BOOL _IS_PED_HAIR_COLOR_VALID(int colorID);
```

**Parámetros**

- `colorID` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE0D36E5D9E99CC21` (`N_0xe0d36e5d9e99cc21`)

---
### IsPedHairColorValid_2

`_IS_PED_HAIR_COLOR_VALID_2` · hash `0xED6D8E27A43B8CDE` · **Cliente**

```lua
local retval = IsPedHairColorValid_2(colorId)
```
```c
BOOL _IS_PED_HAIR_COLOR_VALID_2(int colorId);
```

**Parámetros**

- `colorId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xED6D8E27A43B8CDE` (`N_0xed6d8e27a43b8cde`)

---
### IsPedHangingOnToVehicle

`IS_PED_HANGING_ON_TO_VEHICLE` · hash `0x1C86D8AEF8254B78` · jhash `0x9678D4FF` · **Cliente**

```lua
local retval = IsPedHangingOnToVehicle(ped)
```
```c
BOOL IS_PED_HANGING_ON_TO_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedHeadingTowardsPosition

`IS_PED_HEADING_TOWARDS_POSITION` · hash `0xFCF37A457CB96DC0` · jhash `0x45037B9B` · **Cliente**

```lua
local retval = IsPedHeadingTowardsPosition(ped, x, y, z, p4)
```
```c
BOOL IS_PED_HEADING_TOWARDS_POSITION(Ped ped, float x, float y, float z, float p4);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p4` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFCF37A457CB96DC0` (`N_0xfcf37a457cb96dc0`)

---
### IsPedHeadtrackingEntity

`IS_PED_HEADTRACKING_ENTITY` · hash `0x813A0A7C9D2E831F` · jhash `0x233C9ACF` · **Cliente**

```lua
local retval = IsPedHeadtrackingEntity(ped, entity)
```
```c
BOOL IS_PED_HEADTRACKING_ENTITY(Ped ped, Entity entity);
```

**Parámetros**

- `ped` (`Ped`)
- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsPedHeadtrackingPed

`IS_PED_HEADTRACKING_PED` · hash `0x5CD3CB88A7F8850D` · jhash `0x2A5DF721` · **Cliente**

```lua
local retval = IsPedHeadtrackingPed(ped1, ped2)
```
```c
BOOL IS_PED_HEADTRACKING_PED(Ped ped1, Ped ped2);
```

**Parámetros**

- `ped1` (`Ped`)
- `ped2` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedHelmetUnk

`_IS_PED_HELMET_UNK` · hash `0xB9496CE47546DB2C` · **Cliente**

```lua
local retval = IsPedHelmetUnk(ped)
```
```c
BOOL _IS_PED_HELMET_UNK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB9496CE47546DB2C` (`N_0xb9496ce47546db2c`)

---
### IsPedHuman

`IS_PED_HUMAN` · hash `0xB980061DA992779D` · jhash `0x194BB7B0` · **Cliente**

```lua
local retval = IsPedHuman(ped)
```
```c
BOOL IS_PED_HUMAN(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true/false if the ped is/isn't humanoid.  
```

---
### IsPedHurt

`IS_PED_HURT` · hash `0x5983BB449D7FDB12` · jhash `0x69DFA0AF` · **Cliente**

```lua
local retval = IsPedHurt(ped)
```
```c
BOOL IS_PED_HURT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the specified ped is hurt.  
```

---
### IsPedInAnyBoat

`IS_PED_IN_ANY_BOAT` · hash `0x2E0E1C2B4F6CB339` · jhash `0x1118A947` · **Cliente**

```lua
local retval = IsPedInAnyBoat(ped)
```
```c
BOOL IS_PED_IN_ANY_BOAT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInAnyHeli

`IS_PED_IN_ANY_HELI` · hash `0x298B91AE825E5705` · jhash `0x7AB5523B` · **Cliente**

```lua
local retval = IsPedInAnyHeli(ped)
```
```c
BOOL IS_PED_IN_ANY_HELI(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInAnyPlane

`IS_PED_IN_ANY_PLANE` · hash `0x5FFF4CFC74D8FB80` · jhash `0x51BBCE7E` · **Cliente**

```lua
local retval = IsPedInAnyPlane(ped)
```
```c
BOOL IS_PED_IN_ANY_PLANE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInAnyPoliceVehicle

`IS_PED_IN_ANY_POLICE_VEHICLE` · hash `0x0BD04E29640C9C12` · jhash `0x84FA790D` · **Cliente**

```lua
local retval = IsPedInAnyPoliceVehicle(ped)
```
```c
BOOL IS_PED_IN_ANY_POLICE_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInAnySub

`IS_PED_IN_ANY_SUB` · hash `0xFBFC01CCFB35D99E` · jhash `0xE65F8059` · **Cliente**

```lua
local retval = IsPedInAnySub(ped)
```
```c
BOOL IS_PED_IN_ANY_SUB(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInAnyTaxi

`IS_PED_IN_ANY_TAXI` · hash `0x6E575D6A898AB852` · jhash `0x16FD386C` · **Cliente**

```lua
local retval = IsPedInAnyTaxi(ped)
```
```c
BOOL IS_PED_IN_ANY_TAXI(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInAnyTrain

`IS_PED_IN_ANY_TRAIN` · hash `0x6F972C1AB75A1ED0` · jhash `0x759EF63A` · **Cliente**

```lua
local retval = IsPedInAnyTrain(ped)
```
```c
BOOL IS_PED_IN_ANY_TRAIN(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInAnyVehicle

`IS_PED_IN_ANY_VEHICLE` · hash `0x997ABD671D25CA0B` · jhash `0x3B0171EE` · **Cliente**

```lua
local retval = IsPedInAnyVehicle(ped, atGetIn)
```
```c
BOOL IS_PED_IN_ANY_VEHICLE(Ped ped, BOOL atGetIn);
```

**Parámetros**

- `ped` (`Ped`): The ped to check.
- `atGetIn` (`BOOL`): `true` to also consider attempting to enter a vehicle.

**Devuelve:** `BOOL` — Whether or not the ped is currently involved in any vehicle.

**Descripción oficial:**

Returns whether the specified ped is in any vehicle. If `atGetIn` is set to true, also returns true if the ped is
currently in the process of entering a vehicle (a specific stage check for `CTaskEnterVehicle`).

**Ejemplo (lua):**

```lua
if IsPedInAnyVehicle(PlayerPedId(), false) then
    print('Local player is in a vehicle!')
end
```

---
### IsPedInCombat

`IS_PED_IN_COMBAT` · hash `0x4859F1FC66A6278E` · jhash `0xFE027CB5` · **Cliente**

```lua
local retval = IsPedInCombat(ped, target)
```
```c
BOOL IS_PED_IN_COMBAT(Ped ped, Ped target);
```

**Parámetros**

- `ped` (`Ped`): Ped index.
- `target` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Examines whether the ped is engaged in combat; when given a target ped index, it confirms if the ped is actively fighting the specified target, returning true if engaged and false if not.

---
### IsPedInCover

`IS_PED_IN_COVER` · hash `0x60DFD0691A170B88` · jhash `0x972C5A8B` · **Cliente**

```lua
local retval = IsPedInCover(ped, exceptUseWeapon)
```
```c
BOOL IS_PED_IN_COVER(Ped ped, BOOL exceptUseWeapon);
```

**Parámetros**

- `ped` (`Ped`)
- `exceptUseWeapon` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p1 is nearly always 0 in the scripts.  
```

---
### IsPedInCoverFacingLeft

`IS_PED_IN_COVER_FACING_LEFT` · hash `0x845333B3150583AB` · jhash `0xB89DBB80` · **Cliente**

```lua
local retval = IsPedInCoverFacingLeft(ped)
```
```c
BOOL IS_PED_IN_COVER_FACING_LEFT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInFlyingVehicle

`IS_PED_IN_FLYING_VEHICLE` · hash `0x9134873537FA419C` · jhash `0xCA072485` · **Cliente**

```lua
local retval = IsPedInFlyingVehicle(ped)
```
```c
BOOL IS_PED_IN_FLYING_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInGroup

`IS_PED_IN_GROUP` · hash `0x5891CAC5D4ACFF74` · jhash `0x836D9795` · **Cliente**

```lua
local retval = IsPedInGroup(ped)
```
```c
BOOL IS_PED_IN_GROUP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInHighCover

`IS_PED_IN_HIGH_COVER` · hash `0x6A03BF943D767C93` · jhash `0xDD5D08A7` · **Cliente**

```lua
local retval = IsPedInHighCover(ped)
```
```c
BOOL IS_PED_IN_HIGH_COVER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6A03BF943D767C93` (`N_0x6a03bf943d767c93`), `_IS_PED_STANDING_IN_COVER` (`IsPedStandingInCover`)

---
### IsPedInMeleeCombat

`IS_PED_IN_MELEE_COMBAT` · hash `0x4E209B2C1EAD5159` · jhash `0xFD7814A5` · **Cliente**

```lua
local retval = IsPedInMeleeCombat(ped)
```
```c
BOOL IS_PED_IN_MELEE_COMBAT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Notes: The function only returns true while the ped is:   
A.) Swinging a random melee attack (including pistol-whipping)  
B.) Reacting to being hit by a melee attack (including pistol-whipping)  
C.) Is locked-on to an enemy (arms up, strafing/skipping in the default fighting-stance, ready to dodge+counter).   
You don't have to be holding the melee-targetting button to be in this stance; you stay in it by default for a few seconds after swinging at someone. If you do a sprinting punch, it returns true for the duration of the punch animation and then returns false again, even if you've punched and made-angry many peds  
```

---
### IsPedInModel

`IS_PED_IN_MODEL` · hash `0x796D90EFB19AA332` · jhash `0xA6438D4B` · **Cliente**

```lua
local retval = IsPedInModel(ped, modelHash)
```
```c
BOOL IS_PED_IN_MODEL(Ped ped, Hash modelHash);
```

**Parámetros**

- `ped` (`Ped`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsPedInParachuteFreeFall

`IS_PED_IN_PARACHUTE_FREE_FALL` · hash `0x7DCE8BDA0F1C1200` · jhash `0xCD71F11B` · **Cliente**

```lua
local retval = IsPedInParachuteFreeFall(ped)
```
```c
BOOL IS_PED_IN_PARACHUTE_FREE_FALL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedInSphereAreaOfAnyEnemyPeds

`IS_PED_IN_SPHERE_AREA_OF_ANY_ENEMY_PEDS` · hash `0x082D79E15302F0C2` · **Cliente**

```lua
local retval = IsPedInSphereAreaOfAnyEnemyPeds(ped, x, y, z, range)
```
```c
BOOL IS_PED_IN_SPHERE_AREA_OF_ANY_ENEMY_PEDS(Ped ped, float x, float y, float z, float range);
```

**Parámetros**

- `ped` (`Ped`): The ped to check.
- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `range` (`float`): Radius of sphere.

**Devuelve:** `BOOL` — Returns `true` if ped is within range of any enemies, `false` otherwise.

**Descripción oficial:**

```
NativeDB Introduced: v3407
```

---
### IsPedInVehicle

`IS_PED_IN_VEHICLE` · hash `0xA3EE4A07279BB9DB` · jhash `0x7DA6BC83` · **Cliente**

```lua
local retval = IsPedInVehicle(ped, vehicle, atGetIn)
```
```c
BOOL IS_PED_IN_VEHICLE(Ped ped, Vehicle vehicle, BOOL atGetIn);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `atGetIn` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets a value indicating whether the specified ped is in the specified vehicle.  
If 'atGetIn' is false, the function will not return true until the ped is sitting in the vehicle and is about to close the door. If it's true, the function returns true the moment the ped starts to get onto the seat (after opening the door). Eg. if false, and the ped is getting into a submersible, the function will not return true until the ped has descended down into the submersible and gotten into the seat, while if it's true, it'll return true the moment the hatch has been opened and the ped is about to descend into the submersible.  
```

---
### IsPedInjured

`IS_PED_INJURED` · hash `0x84A2DD9AC37C35C1` · jhash `0x2530A087` · **Cliente**

```lua
local retval = IsPedInjured(ped)
```
```c
BOOL IS_PED_INJURED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped to check for injuries.

**Devuelve:** `BOOL` — Returns `true` if the ped is injured, `false` otherwise.

**Descripción oficial:**

Indicates whether this ped's health is below its injured threshold.
The default threshold is 100, these are stored in the `pedhealth.meta` file located in `common:\data\`

**Below are some of the values**

| InjuredHealthThreshold | Name      |
|------------------------|-----------|
| 100.000000             | Strong    |
| 100.000000             | Average   |
| 100.000000             | Weak      |

---
### IsPedJacking

`IS_PED_JACKING` · hash `0x4AE4FF911DFB61DA` · jhash `0x3B321816` · **Cliente**

```lua
local retval = IsPedJacking(ped)
```
```c
BOOL IS_PED_JACKING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedJumping

`IS_PED_JUMPING` · hash `0xCEDABC5900A0BF97` · jhash `0x07E5BC0E` · **Cliente**

```lua
local retval = IsPedJumping(ped)
```
```c
BOOL IS_PED_JUMPING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedJumpingOutOfVehicle

`IS_PED_JUMPING_OUT_OF_VEHICLE` · hash `0x433DDFFE2044B636` · jhash `0xB19215F6` · **Cliente**

```lua
local retval = IsPedJumpingOutOfVehicle(ped)
```
```c
BOOL IS_PED_JUMPING_OUT_OF_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedLipstickColorValid

`_IS_PED_LIPSTICK_COLOR_VALID` · hash `0x0525A2C2562F3CD4` · **Cliente**

```lua
local retval = IsPedLipstickColorValid(colorID)
```
```c
BOOL _IS_PED_LIPSTICK_COLOR_VALID(int colorID);
```

**Parámetros**

- `colorID` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0525A2C2562F3CD4` (`N_0x0525a2c2562f3cd4`)

---
### IsPedLipstickColorValid_2

`_IS_PED_LIPSTICK_COLOR_VALID_2` · hash `0x3E802F11FBE27674` · **Cliente**

```lua
local retval = IsPedLipstickColorValid_2(colorId)
```
```c
BOOL _IS_PED_LIPSTICK_COLOR_VALID_2(int colorId);
```

**Parámetros**

- `colorId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3E802F11FBE27674` (`N_0x3e802f11fbe27674`)

---
### IsPedMale

`IS_PED_MALE` · hash `0x6D9F5FAA7488BA46` · jhash `0x90950455` · **Cliente**

```lua
local retval = IsPedMale(ped)
```
```c
BOOL IS_PED_MALE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true/false if the ped is/isn't male.  
```

---
### IsPedModel

`IS_PED_MODEL` · hash `0xC9D55B1A358A5BF7` · jhash `0x5F1DDFCB` · **Cliente**

```lua
local retval = IsPedModel(ped, modelHash)
```
```c
BOOL IS_PED_MODEL(Ped ped, Hash modelHash);
```

**Parámetros**

- `ped` (`Ped`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsPedOnAnyBike

`IS_PED_ON_ANY_BIKE` · hash `0x94495889E22C6479` · jhash `0x4D885B2E` · **Cliente**

```lua
local retval = IsPedOnAnyBike(ped)
```
```c
BOOL IS_PED_ON_ANY_BIKE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedOnFoot

`IS_PED_ON_FOOT` · hash `0x01FEE67DB37F59B2` · jhash `0xC60D0785` · **Cliente**

```lua
local retval = IsPedOnFoot(ped)
```
```c
BOOL IS_PED_ON_FOOT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedOnMount

`IS_PED_ON_MOUNT` · hash `0x460BC76A0E10655E` · jhash `0x43103006` · **Cliente**

```lua
local retval = IsPedOnMount(ped)
```
```c
BOOL IS_PED_ON_MOUNT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Same function call as PED::GET_MOUNT, aka just returns 0  
```

---
### IsPedOnSpecificVehicle

`IS_PED_ON_SPECIFIC_VEHICLE` · hash `0xEC5F66E459AF3BB2` · jhash `0x63CB4603` · **Cliente**

```lua
local retval = IsPedOnSpecificVehicle(ped, vehicle)
```
```c
BOOL IS_PED_ON_SPECIFIC_VEHICLE(Ped ped, Vehicle vehicle);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsPedOnVehicle

`IS_PED_ON_VEHICLE` · hash `0x67722AEB798E5FAB` · jhash `0xA1AE7CC7` · **Cliente**

```lua
local retval = IsPedOnVehicle(ped)
```
```c
BOOL IS_PED_ON_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets a value indicating whether the specified ped is on top of any vehicle.  
Return 1 when ped is on vehicle.  
Return 0 when ped is not on a vehicle.  
```

---
### IsPedOpeningADoor

`_IS_PED_OPENING_A_DOOR` · hash `0x26AF0E8E30BD2A2C` · **Cliente**

```lua
local retval = IsPedOpeningADoor(ped)
```
```c
BOOL _IS_PED_OPENING_A_DOOR(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_PED_*

Returns true if the ped is currently opening a door (CTaskOpenDoor).
```

**Nombres antiguos (alias):** `0x26AF0E8E30BD2A2C` (`N_0x26af0e8e30bd2a2c`)

---
### IsPedPerformingDependentComboLimit

`IS_PED_PERFORMING_DEPENDENT_COMBO_LIMIT` · hash `0xEBD0EDBA5BE957CF` · jhash `0x9BE7C860` · **Cliente**

```lua
local retval = IsPedPerformingDependentComboLimit(ped)
```
```c
BOOL IS_PED_PERFORMING_DEPENDENT_COMBO_LIMIT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEBD0EDBA5BE957CF` (`N_0xebd0edba5be957cf`)

---
### IsPedPerformingMeleeAction

`IS_PED_PERFORMING_MELEE_ACTION` · hash `0xDCCA191DF9980FD7` · jhash `0x139C0875` · **Cliente**

```lua
local retval = IsPedPerformingMeleeAction(ped)
```
```c
BOOL IS_PED_PERFORMING_MELEE_ACTION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xDCCA191DF9980FD7` (`N_0xdcca191df9980fd7`)

---
### IsPedPerformingStealthKill

`IS_PED_PERFORMING_STEALTH_KILL` · hash `0xFD4CCDBCC59941B7` · jhash `0x9ADD7B21` · **Cliente**

```lua
local retval = IsPedPerformingStealthKill(ped)
```
```c
BOOL IS_PED_PERFORMING_STEALTH_KILL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedPlantingBomb

`IS_PED_PLANTING_BOMB` · hash `0xC70B5FAE151982D8` · jhash `0x0EDAC574` · **Cliente**

```lua
local retval = IsPedPlantingBomb(ped)
```
```c
BOOL IS_PED_PLANTING_BOMB(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedProne

`IS_PED_PRONE` · hash `0xD6A86331A537A7B9` · jhash `0x02C2A6C3` · **Cliente**

```lua
local retval = IsPedProne(ped)
```
```c
BOOL IS_PED_PRONE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedRagdoll

`IS_PED_RAGDOLL` · hash `0x47E4E977581C5B55` · jhash `0xC833BBE1` · **Cliente**

```lua
local retval = IsPedRagdoll(ped)
```
```c
BOOL IS_PED_RAGDOLL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
If the ped handle passed through the parenthesis is in a ragdoll state this will return true.  
```

---
### IsPedReloading

`IS_PED_RELOADING` · hash `0x24B100C68C645951` · jhash `0x961E1745` · **Cliente**

```lua
local retval = IsPedReloading(ped)
```
```c
BOOL IS_PED_RELOADING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the specified ped is reloading.  
```

---
### IsPedRespondingToEvent

`IS_PED_RESPONDING_TO_EVENT` · hash `0x625B774D75C87068` · jhash `0x7A877554` · **Cliente**

```lua
local retval = IsPedRespondingToEvent(ped, event)
```
```c
BOOL IS_PED_RESPONDING_TO_EVENT(Ped ped, Any event);
```

**Parámetros**

- `ped` (`Ped`)
- `event` (`Any`)

**Devuelve:** `BOOL`

---
### IsPedRunningMeleeTask

`IS_PED_RUNNING_MELEE_TASK` · hash `0xD1871251F3B5ACD7` · jhash `0xBD4236F6` · **Cliente**

```lua
local retval = IsPedRunningMeleeTask(ped)
```
```c
BOOL IS_PED_RUNNING_MELEE_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD1871251F3B5ACD7` (`N_0xd1871251f3b5acd7`)

---
### IsPedRunningMobilePhoneTask

`IS_PED_RUNNING_MOBILE_PHONE_TASK` · hash `0x2AFE52F782F25775` · jhash `0xFB2AFED1` · **Cliente**

```lua
local retval = IsPedRunningMobilePhoneTask(ped)
```
```c
BOOL IS_PED_RUNNING_MOBILE_PHONE_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedRunningRagdollTask

`IS_PED_RUNNING_RAGDOLL_TASK` · hash `0xE3B6097CC25AA69E` · jhash `0x44A153F2` · **Cliente**

```lua
local retval = IsPedRunningRagdollTask(ped)
```
```c
BOOL IS_PED_RUNNING_RAGDOLL_TASK(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedShaderEffectValid

`_IS_PED_SHADER_EFFECT_VALID` · hash `0x81AA517FBBA05D39` · **Cliente**

```lua
local retval = IsPedShaderEffectValid(ped)
```
```c
BOOL _IS_PED_SHADER_EFFECT_VALID(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x81AA517FBBA05D39` (`N_0x81aa517fbba05d39`)

---
### IsPedSheltered

`IS_PED_SHELTERED` · hash `0xB8B52E498014F5B0` · **Cliente**

```lua
local retval = IsPedSheltered(ped)
```
```c
BOOL IS_PED_SHELTERED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped entity to check.

**Devuelve:** `BOOL` — Returns `true` if the ped is sheltered, `false` otherwise.

**Descripción oficial:**

Returns whether the specified ped is currently sheltered.
A ped is considered sheltered if they are under a **roof**, a **bridge**, inside a **tunnel**, or within a **vehicle with a solid roof**, meaning they are not directly exposed to the open sky.

**Nombres antiguos (alias):** `0xB8B52E498014F5B0` (`N_0xb8b52e498014f5b0`)

**Ejemplo (lua):**

```lua
-- Check if the player's ped is currently under a shelter.
local playerPed = PlayerPedId()
local isSheltered = IsPedSheltered(playerPed)

if isSheltered then
    print("The player is currently sheltered.")
else
    print("The player is out in the open.")
end
```

**Ejemplo (js):**

```js
// Check if the player's ped is currently under a shelter.
const playerPed = PlayerPedId();
const isSheltered = IsPedSheltered(playerPed);

if (isSheltered) {
    console.log("The player is currently sheltered.");
} else {
    console.log("The player is out in the open.");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Check if the player's ped is currently under a shelter.
int playerPed = PlayerPedId();
bool isSheltered = IsPedSheltered(playerPed);

if (isSheltered)
{
    Debug.WriteLine("The player is currently sheltered.");
}
else
{
    Debug.WriteLine("The player is out in the open.");
}
```

---
### IsPedShooting

`IS_PED_SHOOTING` · hash `0x34616828CD07F1A1` · jhash `0xE7C3405E` · **Cliente**

```lua
local retval = IsPedShooting(ped)
```
```c
BOOL IS_PED_SHOOTING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the specified ped is shooting.  
```

---
### IsPedShootingInArea

`IS_PED_SHOOTING_IN_AREA` · hash `0x7E9DFE24AC1E58EF` · jhash `0x741BF04F` · **Cliente**

```lua
local retval = IsPedShootingInArea(ped, x1, y1, z1, x2, y2, z2, p7, p8)
```
```c
BOOL IS_PED_SHOOTING_IN_AREA(Ped ped, float x1, float y1, float z1, float x2, float y2, float z2, BOOL p7, BOOL p8);
```

**Parámetros**

- `ped` (`Ped`)
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsPedSittingInAnyVehicle

`IS_PED_SITTING_IN_ANY_VEHICLE` · hash `0x826AA586EDB9FEF8` · jhash `0x0EA9CA03` · **Cliente**

```lua
local retval = IsPedSittingInAnyVehicle(ped)
```
```c
BOOL IS_PED_SITTING_IN_ANY_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Detect if ped is in any vehicle  
[True/False]  
```

---
### IsPedSittingInVehicle

`IS_PED_SITTING_IN_VEHICLE` · hash `0xA808AA1D79230FC2` · jhash `0xDDDE26FA` · **Cliente**

```lua
local retval = IsPedSittingInVehicle(ped, vehicle)
```
```c
BOOL IS_PED_SITTING_IN_VEHICLE(Ped ped, Vehicle vehicle);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Detect if ped is sitting in the specified vehicle  
[True/False]  
```

---
### IsPedStopped

`IS_PED_STOPPED` · hash `0x530944F6F4B8A214` · jhash `0xA0DC0B87` · **Cliente**

```lua
local retval = IsPedStopped(ped)
```
```c
BOOL IS_PED_STOPPED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the ped doesn't do any movement. If the ped is being pushed forwards by using APPLY_FORCE_TO_ENTITY for example, the function returns false.  
```

---
### IsPedSwappingWeapon

`_IS_PED_SWAPPING_WEAPON` · hash `0x3795688A307E1EB6` · **Cliente**

```lua
local retval = IsPedSwappingWeapon(Ped)
```
```c
BOOL _IS_PED_SWAPPING_WEAPON(Ped Ped);
```

**Parámetros**

- `Ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3795688A307E1EB6` (`N_0x3795688a307e1eb6`)

---
### IsPedSwimming

`IS_PED_SWIMMING` · hash `0x9DE327631295B4C2` · jhash `0x7AB43DB8` · **Cliente**

```lua
local retval = IsPedSwimming(ped)
```
```c
BOOL IS_PED_SWIMMING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedSwimmingUnderWater

`IS_PED_SWIMMING_UNDER_WATER` · hash `0xC024869A53992F34` · jhash `0x0E8D524F` · **Cliente**

```lua
local retval = IsPedSwimmingUnderWater(ped)
```
```c
BOOL IS_PED_SWIMMING_UNDER_WATER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedTakingOffHelmet

`IS_PED_TAKING_OFF_HELMET` · hash `0x14590DDBEDB1EC85` · jhash `0xA1008E0E` · **Cliente**

```lua
local retval = IsPedTakingOffHelmet(ped)
```
```c
BOOL IS_PED_TAKING_OFF_HELMET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x14590DDBEDB1EC85` (`N_0x14590ddbedb1ec85`)

---
### IsPedTracked

`IS_PED_TRACKED` · hash `0x4C5E1F087CD10BB7` · jhash `0x7EB613D9` · **Cliente**

```lua
local retval = IsPedTracked(ped)
```
```c
BOOL IS_PED_TRACKED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedTryingToEnterALockedVehicle

`IS_PED_TRYING_TO_ENTER_A_LOCKED_VEHICLE` · hash `0x44D28D5DDFE5F68C` · jhash `0x46828B4E` · **Cliente**

```lua
local retval = IsPedTryingToEnterALockedVehicle(ped)
```
```c
BOOL IS_PED_TRYING_TO_ENTER_A_LOCKED_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): Ped index.

**Devuelve:** `BOOL`

**Descripción oficial:**

If the ped is attempting to enter a locked vehicle.

---
### IsPedUsingActionMode

`IS_PED_USING_ACTION_MODE` · hash `0x00E73468D085F745` · jhash `0x5AE7EDA2` · **Cliente**

```lua
local retval = IsPedUsingActionMode(ped)
```
```c
BOOL IS_PED_USING_ACTION_MODE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedUsingAnyScenario

`IS_PED_USING_ANY_SCENARIO` · hash `0x57AB4A3080F85143` · jhash `0x195EF5B7` · **Cliente**

```lua
local retval = IsPedUsingAnyScenario(ped)
```
```c
BOOL IS_PED_USING_ANY_SCENARIO(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.

**Devuelve:** `BOOL` — Returns true if the ped is using any scenario.

---
### IsPedUsingScenario

`IS_PED_USING_SCENARIO` · hash `0x1BF094736DD62C2E` · jhash `0x0F65B0D4` · **Cliente**

```lua
local retval = IsPedUsingScenario(ped, scenario)
```
```c
BOOL IS_PED_USING_SCENARIO(Ped ped, char* scenario);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `scenario` (`char*`): The scenario name.

**Devuelve:** `BOOL` — Returns true if the specified ped is using the specified scenario.

**Descripción oficial:**

See [`TASK_START_SCENARIO_IN_PLACE`](TASK.md#taskstartscenarioinplace) for a list of scenarios.

---
### IsPedVaulting

`IS_PED_VAULTING` · hash `0x117C70D1F5730B5E` · jhash `0xC3169BDA` · **Cliente**

```lua
local retval = IsPedVaulting(ped)
```
```c
BOOL IS_PED_VAULTING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsPedWearingHelmet

`IS_PED_WEARING_HELMET` · hash `0xF33BDFE19B309B19` · jhash `0x0D680D49` · **Cliente**

```lua
local retval = IsPedWearingHelmet(ped)
```
```c
BOOL IS_PED_WEARING_HELMET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the ped passed through the parenthesis is wearing a helmet.  
```

---
### IsPedheadshotImgUploadAvailable

`IS_PEDHEADSHOT_IMG_UPLOAD_AVAILABLE` · hash `0xEBB376779A760AA8` · jhash `0x810158F8` · **Cliente**

```lua
local retval = IsPedheadshotImgUploadAvailable()
```
```c
BOOL IS_PEDHEADSHOT_IMG_UPLOAD_AVAILABLE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEBB376779A760AA8` (`N_0xebb376779a760aa8`)

---
### IsPedheadshotReady

`IS_PEDHEADSHOT_READY` · hash `0x7085228842B13A67` · jhash `0x761CD02E` · **Cliente**

```lua
local retval = IsPedheadshotReady(id)
```
```c
BOOL IS_PEDHEADSHOT_READY(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
gtaforums.com/topic/885580-ped-headshotmugshot-txd/  
```

---
### IsPedheadshotValid

`IS_PEDHEADSHOT_VALID` · hash `0xA0A9668F158129A2` · jhash `0x0B1080C4` · **Cliente**

```lua
local retval = IsPedheadshotValid(id)
```
```c
BOOL IS_PEDHEADSHOT_VALID(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
gtaforums.com/topic/885580-ped-headshotmugshot-txd/  
```

---
### IsScriptedScenarioPedUsingConditionalAnim

`IS_SCRIPTED_SCENARIO_PED_USING_CONDITIONAL_ANIM` · hash `0x6EC47A344923E1ED` · jhash `0x3C30B447` · **Cliente**

```lua
local retval = IsScriptedScenarioPedUsingConditionalAnim(ped, animDict, anim)
```
```c
BOOL IS_SCRIPTED_SCENARIO_PED_USING_CONDITIONAL_ANIM(Ped ped, char* animDict, char* anim);
```

**Parámetros**

- `ped` (`Ped`)
- `animDict` (`char*`)
- `anim` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### IsScubaGearLightEnabled

`_IS_SCUBA_GEAR_LIGHT_ENABLED` · hash `0x88274C11CF0D866D` · **Cliente**

```lua
local retval = IsScubaGearLightEnabled(ped)
```
```c
BOOL _IS_SCUBA_GEAR_LIGHT_ENABLED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### IsSynchronizedSceneHoldLastFrame

`IS_SYNCHRONIZED_SCENE_HOLD_LAST_FRAME` · hash `0x7F2F4F13AC5257EF` · jhash `0x72CF2514` · **Cliente**

```lua
local retval = IsSynchronizedSceneHoldLastFrame(sceneID)
```
```c
BOOL IS_SYNCHRONIZED_SCENE_HOLD_LAST_FRAME(int sceneID);
```

**Parámetros**

- `sceneID` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x7F2F4F13AC5257EF` (`N_0x7f2f4f13ac5257ef`)

---
### IsSynchronizedSceneLooped

`IS_SYNCHRONIZED_SCENE_LOOPED` · hash `0x62522002E0C391BA` · jhash `0x47D87A84` · **Cliente**

```lua
local retval = IsSynchronizedSceneLooped(sceneID)
```
```c
BOOL IS_SYNCHRONIZED_SCENE_LOOPED(int sceneID);
```

**Parámetros**

- `sceneID` (`int`)

**Devuelve:** `BOOL`

---
### IsSynchronizedSceneRunning

`IS_SYNCHRONIZED_SCENE_RUNNING` · hash `0x25D39B935A038A26` · jhash `0x57A282F1` · **Cliente**

```lua
local retval = IsSynchronizedSceneRunning(sceneId)
```
```c
BOOL IS_SYNCHRONIZED_SCENE_RUNNING(int sceneId);
```

**Parámetros**

- `sceneId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if a synchronized scene is running  
```

---
### IsTrackedPedVisible

`IS_TRACKED_PED_VISIBLE` · hash `0x91C8E617F64188AC` · jhash `0x33248CC1` · **Cliente**

```lua
local retval = IsTrackedPedVisible(ped)
```
```c
BOOL IS_TRACKED_PED_VISIBLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
returns whether or not a ped is visible within your FOV, not this check auto's to false after a certain distance.  
Target needs to be tracked.. won't work otherwise.  
```

---
### KnockOffPedProp

`KNOCK_OFF_PED_PROP` · hash `0x6FD7816A36615F48` · jhash `0x08D8B180` · **Cliente**

```lua
KnockOffPedProp(ped, p1, p2, p3, p4)
```
```c
void KNOCK_OFF_PED_PROP(Ped ped, BOOL p1, BOOL p2, BOOL p3, BOOL p4);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)

**Devuelve:** `void`

---
### KnockPedOffVehicle

`KNOCK_PED_OFF_VEHICLE` · hash `0x45BBCBA77C29A841` · jhash `0xACDD0674` · **Cliente**

```lua
KnockPedOffVehicle(ped)
```
```c
void KNOCK_PED_OFF_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### N_0x03ea03af85a85cb7

`0x03EA03AF85A85CB7` · hash `0x03EA03AF85A85CB7` · jhash `0x18DD76A1` · **Cliente**

```lua
local retval = N_0x03ea03af85a85cb7(ped, p1, p2, p3, p4, p5, p6, p7, p8)
```
```c
BOOL 0x03EA03AF85A85CB7(Ped ped, BOOL p1, BOOL p2, BOOL p3, BOOL p4, BOOL p5, BOOL p6, BOOL p7, Any p8);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)
- `p8` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x06087579e7aa85a9

`0x06087579E7AA85A9` · hash `0x06087579E7AA85A9` · jhash `0xD0567D41` · **Cliente**

```lua
local retval = N_0x06087579e7aa85a9(p0, p1, p2, p3, p4, p5)
```
```c
BOOL 0x06087579E7AA85A9(Any p0, Any p1, float p2, float p3, float p4, float p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `BOOL`

---
### N_0x061cb768363d6424

`0x061CB768363D6424` · hash `0x061CB768363D6424` · jhash `0x7DA12905` · **Cliente**

```lua
N_0x061cb768363d6424(ped, toggle)
```
```c
void 0x061CB768363D6424(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x0b3e35ac043707d9

`0x0B3E35AC043707D9` · hash `0x0B3E35AC043707D9` · **Cliente**

```lua
N_0x0b3e35ac043707d9(p0, p1)
```
```c
void 0x0B3E35AC043707D9(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x0f62619393661d6e

`0x0F62619393661D6E` · hash `0x0F62619393661D6E` · **Cliente**

```lua
N_0x0f62619393661d6e(p0, p1, p2)
```
```c
void 0x0F62619393661D6E(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

---
### N_0x110f526ab784111f

`0x110F526AB784111F` · hash `0x110F526AB784111F` · jhash `0x3B882533` · **Cliente**

```lua
N_0x110f526ab784111f(ped, p1)
```
```c
void 0x110F526AB784111F(Ped ped, float p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
In agency_heist3b.c4, its like this 90% of the time:  
PED::_110F526AB784111F(ped, 0.099);  
PED::SET_PED_ENVEFF_SCALE(ped, 1.0);  
PED::_D69411AA0CEBF9E9(ped, 87, 81, 68);  
PED::SET_ENABLE_PED_ENVEFF_SCALE(ped, 1);  
and its like this 10% of the time:  
PED::_110F526AB784111F(ped, 0.2);  
PED::SET_PED_ENVEFF_SCALE(ped, 0.65);  
PED::_D69411AA0CEBF9E9(ped, 74, 69, 60);  
PED::SET_ENABLE_PED_ENVEFF_SCALE(ped, 1);  
```

---
### N_0x1216e0bfa72cc703

`0x1216E0BFA72CC703` · hash `0x1216E0BFA72CC703` · jhash `0x7BD26837` · **Cliente**

```lua
N_0x1216e0bfa72cc703(p0, p1)
```
```c
void 0x1216E0BFA72CC703(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x1a330d297aac6bc1

`0x1A330D297AAC6BC1` · hash `0x1A330D297AAC6BC1` · jhash `0x77BB7CB8` · **Cliente**

```lua
N_0x1a330d297aac6bc1(ped, p1)
```
```c
void 0x1A330D297AAC6BC1(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only appears in lamar1 script.  
```

---
### N_0x1e77fa7a62ee6c4c

`0x1E77FA7A62EE6C4C` · hash `0x1E77FA7A62EE6C4C` · jhash `0x021F5B36` · **Cliente**

```lua
local retval = N_0x1e77fa7a62ee6c4c(p0)
```
```c
Any 0x1E77FA7A62EE6C4C(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
GET_*
```

---
### N_0x2016c603d6b8987c

`0x2016C603D6B8987C` · hash `0x2016C603D6B8987C` · jhash `0xA6F2C057` · **Cliente**

```lua
N_0x2016c603d6b8987c(ped, toggle)
```
```c
void 0x2016C603D6B8987C(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PED_STE*
```

---
### N_0x25361a96e0f7e419

`0x25361A96E0F7E419` · hash `0x25361A96E0F7E419` · jhash `0x58C0F6CF` · **Cliente**

```lua
local retval = N_0x25361a96e0f7e419(p0, p1, p2, p3)
```
```c
Any 0x25361A96E0F7E419(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `Any`

---
### N_0x2735233a786b1bef

`0x2735233A786B1BEF` · hash `0x2735233A786B1BEF` · jhash `0x373CC405` · **Cliente**

```lua
N_0x2735233a786b1bef(ped, p1)
```
```c
void 0x2735233A786B1BEF(Ped ped, float p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0x288df530c92dad6f

`0x288DF530C92DAD6F` · hash `0x288DF530C92DAD6F` · **Cliente**

```lua
N_0x288df530c92dad6f(ped, value)
```
```c
void 0x288DF530C92DAD6F(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

[`SET_VEHICLE_STEER_BIAS`](VEHICLE-2.md#setvehiclesteerbias) for peds, e.g., `_SET_PED_STEER_BIAS`.

---
### N_0x2b694afcf64e6994

`0x2B694AFCF64E6994` · hash `0x2B694AFCF64E6994` · **Cliente**

```lua
N_0x2b694afcf64e6994(ped, p1)
```
```c
void 0x2B694AFCF64E6994(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x2dfc81c9b9608549

`0x2DFC81C9B9608549` · hash `0x2DFC81C9B9608549` · **Cliente**

```lua
local retval, p1 = N_0x2dfc81c9b9608549(ped, p1)
```
```c
BOOL 0x2DFC81C9B9608549(Ped ped, int* p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x2f074c904d85129e

`0x2F074C904D85129E` · hash `0x2F074C904D85129E` · **Cliente**

```lua
N_0x2f074c904d85129e(p0, p1, p2, p3, p4, p5, p6)
```
```c
void 0x2F074C904D85129E(float p0, float p1, float p2, float p3, float p4, float p5, float p6);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)

**Devuelve:** `void`

---
### N_0x2f3c3d9f50681de4

`0x2F3C3D9F50681DE4` · hash `0x2F3C3D9F50681DE4` · jhash `0xCC9D7F1A` · **Cliente**

```lua
N_0x2f3c3d9f50681de4(p0, p1)
```
```c
void 0x2F3C3D9F50681DE4(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x336b3d200ab007cb

`0x336B3D200AB007CB` · hash `0x336B3D200AB007CB` · jhash `0xFB18CB19` · **Cliente**

```lua
local retval = N_0x336b3d200ab007cb(p0, p1, p2, p3, p4)
```
```c
Any 0x336B3D200AB007CB(Any p0, float p1, float p2, float p3, float p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `Any`

---
### N_0x3e9679c1dfcf422c

`0x3E9679C1DFCF422C` · hash `0x3E9679C1DFCF422C` · **Cliente**

```lua
N_0x3e9679c1dfcf422c(p0, p1)
```
```c
void 0x3E9679C1DFCF422C(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x412f1364fa066cfb

`0x412F1364FA066CFB` · hash `0x412F1364FA066CFB` · **Cliente**

```lua
local retval = N_0x412f1364fa066cfb(p0)
```
```c
Any 0x412F1364FA066CFB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x425aecf167663f48

`0x425AECF167663F48` · hash `0x425AECF167663F48` · jhash `0x5BC276AE` · **Cliente**

```lua
N_0x425aecf167663f48(ped, p1)
```
```c
void 0x425AECF167663F48(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x46b05bcae43856b0

`0x46B05BCAE43856B0` · hash `0x46B05BCAE43856B0` · jhash `0x79543043` · **Cliente**

```lua
local retval = N_0x46b05bcae43856b0(ped, flag)
```
```c
BOOL 0x46B05BCAE43856B0(Ped ped, int flag);
```

**Parámetros**

- `ped` (`Ped`)
- `flag` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Checks if the specified unknown flag is set in the ped's model.  
The engine itself seems to exclusively check for flags 1 and 4 (Might be inlined code of the check that checks for other flags).  
Game scripts exclusively check for flags 1 and 4.  
```

---
### N_0x49e50bdb8ba4dab2

`0x49E50BDB8BA4DAB2` · hash `0x49E50BDB8BA4DAB2` · jhash `0x397F06E3` · **Cliente**

```lua
N_0x49e50bdb8ba4dab2(ped, toggle)
```
```c
void 0x49E50BDB8BA4DAB2(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PED_ALLOW*
```

---
### N_0x511f1a683387c7e2

`0x511F1A683387C7E2` · hash `0x511F1A683387C7E2` · jhash `0x5B1B70AA` · **Cliente**

```lua
local retval = N_0x511f1a683387c7e2(ped)
```
```c
int 0x511F1A683387C7E2(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Descripción oficial:**

```
GET_*
```

---
### N_0x5407b7288d0478b7

`0x5407B7288D0478B7` · hash `0x5407B7288D0478B7` · jhash `0xEF0B78E6` · **Cliente**

```lua
local retval = N_0x5407b7288d0478b7(p0)
```
```c
int 0x5407B7288D0478B7(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `int`

---
### N_0x5a7f62fda59759bd

`0x5A7F62FDA59759BD` · hash `0x5A7F62FDA59759BD` · jhash `0xB48C0C04` · **Cliente**

```lua
N_0x5a7f62fda59759bd()
```
```c
void 0x5A7F62FDA59759BD();
```

**Devuelve:** `void`

---
### N_0x5b6010b3cbc29095

`0x5B6010B3CBC29095` · hash `0x5B6010B3CBC29095` · **Cliente**

```lua
N_0x5b6010b3cbc29095(p0, p1)
```
```c
void 0x5B6010B3CBC29095(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x711794453cfd692b

`0x711794453CFD692B` · hash `0x711794453CFD692B` · **Cliente**

```lua
N_0x711794453cfd692b(p0, p1)
```
```c
void 0x711794453CFD692B(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x733c87d4ce22bea2

`0x733C87D4CE22BEA2` · hash `0x733C87D4CE22BEA2` · jhash `0x43709044` · **Cliente**

```lua
N_0x733c87d4ce22bea2(ped)
```
```c
void 0x733C87D4CE22BEA2(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### N_0x75ba1cb3b7d40caf

`0x75BA1CB3B7D40CAF` · hash `0x75BA1CB3B7D40CAF` · jhash `0x9194DB71` · **Cliente**

```lua
N_0x75ba1cb3b7d40caf(ped, p1)
```
```c
void 0x75BA1CB3B7D40CAF(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
REQUEST_*
```

---
### N_0x80054d7fcc70eec6

`0x80054D7FCC70EEC6` · hash `0x80054D7FCC70EEC6` · **Cliente**

```lua
N_0x80054d7fcc70eec6(ped)
```
```c
void 0x80054D7FCC70EEC6(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
CLEAR_PED_*
```

---
### N_0x820e9892a77e97cd

`0x820E9892A77E97CD` · hash `0x820E9892A77E97CD` · **Cliente**

```lua
N_0x820e9892a77e97cd(p0, p1)
```
```c
void 0x820E9892A77E97CD(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x87ddeb611b329a9c

`0x87DDEB611B329A9C` · hash `0x87DDEB611B329A9C` · **Cliente**

```lua
N_0x87ddeb611b329a9c(multiplier)
```
```c
void 0x87DDEB611B329A9C(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_A*
```

---
### N_0x9911f4a24485f653

`0x9911F4A24485F653` · hash `0x9911F4A24485F653` · jhash `0x02A080C8` · **Cliente**

```lua
N_0x9911f4a24485f653(p0)
```
```c
void 0x9911F4A24485F653(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x9a77dfd295e29b09

`0x9A77DFD295E29B09` · hash `0x9A77DFD295E29B09` · jhash `0xC08FE5F6` · **Cliente**

```lua
N_0x9a77dfd295e29b09(ped, toggle)
```
```c
void 0x9A77DFD295E29B09(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x9c6a6c19b6c0c496

`0x9C6A6C19B6C0C496` · hash `0x9C6A6C19B6C0C496` · **Cliente**

```lua
local retval, p1 = N_0x9c6a6c19b6c0c496(ped, p1)
```
```c
BOOL 0x9C6A6C19B6C0C496(Ped ped, int* p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x9e30e91fb03a2caf

`0x9E30E91FB03A2CAF` · hash `0x9E30E91FB03A2CAF` · jhash `0x52559BB6` · **Cliente**

```lua
local retval, p0, p1 = N_0x9e30e91fb03a2caf()
```
```c
BOOL 0x9E30E91FB03A2CAF(Any* p0, Any* p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### N_0xa3f3564a5b3646c0

`0xA3F3564A5B3646C0` · hash `0xA3F3564A5B3646C0` · jhash `0x97353375` · **Cliente**

```lua
local retval = N_0xa3f3564a5b3646c0(ped)
```
```c
BOOL 0xA3F3564A5B3646C0(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Only called once in the scripts:
if (sub_1abd() && (!PED::_A3F3564A5B3646C0(l_8C))) {
    if (sub_52e3("RESNA_CELLR", 0)) {
        PED::SET_PED_CAN_PLAY_GESTURE_ANIMS(l_8C, 1);
        PED::SET_PED_CAN_PLAY_AMBIENT_ANIMS(l_8C, 1);
        PED::SET_PED_CAN_PLAY_VISEME_ANIMS(l_8C, 1, 0);
        l_184 += 1;
    }
}
Checks something related to the mobile phone task.
IS_*
```

---
### N_0xa52d5247a4227e14

`0xA52D5247A4227E14` · hash `0xA52D5247A4227E14` · jhash `0xB52BA5F5` · **Cliente**

```lua
N_0xa52d5247a4227e14(p0)
```
```c
void 0xA52D5247A4227E14(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xa660faf550eb37e5

`0xA660FAF550EB37E5` · hash `0xA660FAF550EB37E5` · **Cliente**

```lua
N_0xa660faf550eb37e5(p0, p1)
```
```c
void 0xA660FAF550EB37E5(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xa9b61a329bfdcbea

`0xA9B61A329BFDCBEA` · hash `0xA9B61A329BFDCBEA` · jhash `0x2276DE0D` · **Cliente**

```lua
N_0xa9b61a329bfdcbea(p0, p1)
```
```c
void 0xA9B61A329BFDCBEA(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xaaa6a3698a69e048

`0xAAA6A3698A69E048` · hash `0xAAA6A3698A69E048` · **Cliente**

```lua
local retval = N_0xaaa6a3698a69e048(p0)
```
```c
Any 0xAAA6A3698A69E048(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0xad27d957598e49e9

`0xAD27D957598E49E9` · hash `0xAD27D957598E49E9` · **Cliente**

```lua
N_0xad27d957598e49e9(ped, p1, p2, hash, p4, p5)
```
```c
void 0xAD27D957598E49E9(Ped ped, Any p1, float p2, Hash hash, Any p4, Any p5);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any`)
- `p2` (`float`)
- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xafc976fd0580c7b3

`0xAFC976FD0580C7B3` · hash `0xAFC976FD0580C7B3` · jhash `0x1572022A` · **Cliente**

```lua
N_0xafc976fd0580c7b3(ped, toggle)
```
```c
void 0xAFC976FD0580C7B3(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PED_*
```

---
### N_0xb282749d5e028163

`0xB282749D5E028163` · hash `0xB282749D5E028163` · **Cliente**

```lua
N_0xb282749d5e028163(p0, p1)
```
```c
void 0xB282749D5E028163(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xb3352e018d6f89df

`0xB3352E018D6F89DF` · hash `0xB3352E018D6F89DF` · **Cliente**

```lua
N_0xb3352e018d6f89df(toggle)
```
```c
void 0xB3352E018D6F89DF(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
_SET_PED_HEAD_* - _SET_PED_HEARING_*

_SET_PED_HEALTH_...
```

```
NativeDB Introduced: v2699
```

---
### N_0xc2ee020f5fb4db53

`0xC2EE020F5FB4DB53` · hash `0xC2EE020F5FB4DB53` · jhash `0xB7CD0A49` · **Cliente**

```lua
N_0xc2ee020f5fb4db53(ped)
```
```c
void 0xC2EE020F5FB4DB53(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### N_0xc30bdaee47256c13

`0xC30BDAEE47256C13` · hash `0xC30BDAEE47256C13` · **Cliente**

```lua
local retval = N_0xc30bdaee47256c13(p0)
```
```c
Any 0xC30BDAEE47256C13(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0xc56fbf2f228e1dac

`0xC56FBF2F228E1DAC` · hash `0xC56FBF2F228E1DAC` · **Cliente**

```lua
local retval = N_0xc56fbf2f228e1dac(modelHash, p1, p2)
```
```c
Any 0xC56FBF2F228E1DAC(Hash modelHash, Any p1, Any p2);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `Any`

---
### N_0xcd018c591f94cb43

`0xCD018C591F94CB43` · hash `0xCD018C591F94CB43` · **Cliente**

```lua
N_0xcd018c591f94cb43(ped, p1)
```
```c
void 0xCD018C591F94CB43(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
REQUEST_*
```

---
### N_0xceda60a74219d064

`0xCEDA60A74219D064` · hash `0xCEDA60A74219D064` · **Cliente**

```lua
N_0xceda60a74219d064(p0, p1)
```
```c
void 0xCEDA60A74219D064(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xd33daa36272177c4

`0xD33DAA36272177C4` · hash `0xD33DAA36272177C4` · jhash `0xA89A53F2` · **Cliente**

```lua
N_0xd33daa36272177c4(ped)
```
```c
void 0xD33DAA36272177C4(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### N_0xdfe68c4b787e1bfb

`0xDFE68C4B787E1BFB` · hash `0xDFE68C4B787E1BFB` · **Cliente**

```lua
N_0xdfe68c4b787e1bfb(ped)
```
```c
void 0xDFE68C4B787E1BFB(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0xe906ec930f5fe7c8

`0xE906EC930F5FE7C8` · hash `0xE906EC930F5FE7C8` · **Cliente**

```lua
N_0xe906ec930f5fe7c8(p0, p1)
```
```c
void 0xE906EC930F5FE7C8(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xea9960d07dadcf10

`0xEA9960D07DADCF10` · hash `0xEA9960D07DADCF10` · **Cliente**

```lua
local retval = N_0xea9960d07dadcf10(p0)
```
```c
int 0xEA9960D07DADCF10(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `int`

---
### N_0xec4b4b3b9908052a

`0xEC4B4B3B9908052A` · hash `0xEC4B4B3B9908052A` · jhash `0xF30658D2` · **Cliente**

```lua
N_0xec4b4b3b9908052a(ped, unk)
```
```c
void 0xEC4B4B3B9908052A(Ped ped, float unk);
```

**Parámetros**

- `ped` (`Ped`)
- `unk` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PED_*  
Has most likely to do with some shooting attributes as it sets the float which is in the same range as shootRate.  
```

---
### N_0xed3c76adfa6d07c4

`0xED3C76ADFA6D07C4` · hash `0xED3C76ADFA6D07C4` · jhash `0xFB4000DC` · **Cliente**

```lua
N_0xed3c76adfa6d07c4(ped)
```
```c
void 0xED3C76ADFA6D07C4(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
FORCE_*
```

---
### N_0xf033419d1b81fae8

`0xF033419D1B81FAE8` · hash `0xF033419D1B81FAE8` · jhash `0x8FDDB5DB` · **Cliente**

```lua
local retval = N_0xf033419d1b81fae8(p0)
```
```c
Any 0xF033419D1B81FAE8(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
GET_*
```

---
### N_0xf2385935bffd4d92

`0xF2385935BFFD4D92` · hash `0xF2385935BFFD4D92` · jhash `0xFFF149FE` · **Cliente**

```lua
local retval = N_0xf2385935bffd4d92(ped)
```
```c
BOOL 0xF2385935BFFD4D92(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Initial guess of native: `_IS_PED_WEARING_MOTORCYCLE_HELMET`.

---
### N_0xf2bebcdfafdaa19e

`0xF2BEBCDFAFDAA19E` · hash `0xF2BEBCDFAFDAA19E` · jhash `0x6CD58238` · **Cliente**

```lua
N_0xf2bebcdfafdaa19e(toggle)
```
```c
void 0xF2BEBCDFAFDAA19E(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PED_ALLOW*
toggle was always false except in one instance (b678).
The one time this is set to true seems to do with when you fail the mission.
```

---
### N_0xfab944d4d481accb

`0xFAB944D4D481ACCB` · hash `0xFAB944D4D481ACCB` · **Cliente**

```lua
N_0xfab944d4d481accb(ped, toggle)
```
```c
void 0xFAB944D4D481ACCB(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

SET_A\*

```
NativeDB Introduced: v1734
```

---
### N_0xfd325494792302d7

`0xFD325494792302D7` · hash `0xFD325494792302D7` · jhash `0x7F67671D` · **Cliente**

```lua
N_0xfd325494792302d7(ped, toggle)
```
```c
void 0xFD325494792302D7(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `SET_TIME_EXCLUSIVE_DISPLAY_TEXTURE` (`SetTimeExclusiveDisplayTexture`)

---
### N_0xfec9a3b1820f3331

`0xFEC9A3B1820F3331` · hash `0xFEC9A3B1820F3331` · **Cliente**

```lua
local retval = N_0xfec9a3b1820f3331(ped)
```
```c
BOOL 0xFEC9A3B1820F3331(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Native to check whether [`_SET_PED_SCUBA_GEAR_VARIATION`](#setpedscubagearvariation) is enabled/actived.

---
### N_0xff4803bc019852d9

`0xFF4803BC019852D9` · hash `0xFF4803BC019852D9` · jhash `0xD41C9AED` · **Cliente**

```lua
N_0xff4803bc019852d9(p0, p1)
```
```c
void 0xFF4803BC019852D9(float p0, Any p1);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
Related to Peds dropping pickup_health_snack; p0 is a value between [0.0, 1.0] that corresponds to drop rate
```

---
### PlayFacialAnim

`PLAY_FACIAL_ANIM` · hash `0xE1E65CA8AC9C00ED` · jhash `0x1F6CCDDE` · **Cliente**

```lua
PlayFacialAnim(ped, animName, animDict)
```
```c
void PLAY_FACIAL_ANIM(Ped ped, char* animName, char* animDict);
```

**Parámetros**

- `ped` (`Ped`)
- `animName` (`char*`)
- `animDict` (`char*`)

**Devuelve:** `void`

---
### RegisterHatedTargetsAroundPed

`REGISTER_HATED_TARGETS_AROUND_PED` · hash `0x9222F300BF8354FE` · jhash `0x7F87559E` · **Cliente**

```lua
RegisterHatedTargetsAroundPed(ped, radius)
```
```c
void REGISTER_HATED_TARGETS_AROUND_PED(Ped ped, float radius);
```

**Parámetros**

- `ped` (`Ped`)
- `radius` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Based on TASK_COMBAT_HATED_TARGETS_AROUND_PED, the parameters are likely similar (PedHandle, and area to attack in).  
```

---
### RegisterPedheadshot

`REGISTER_PEDHEADSHOT` · hash `0x4462658788425076` · jhash `0xFFE2667B` · **Cliente**

```lua
local retval = RegisterPedheadshot(ped)
```
```c
int REGISTER_PEDHEADSHOT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped you want to take the "headshot" of.

**Devuelve:** `int` — It returns a Pedheadshot handle, which can be used by natives such as [`GET_PEDHEADSHOT_TXD_STRING`](#getpedheadshottxdstring)

**Descripción oficial:**

```
gtaforums.com/topic/885580-ped-headshotmugshot-txd/  
```

**Ejemplo (lua):**

```lua
CreateThread(function()
    -- Get the ped headshot image.
    local handle = RegisterPedheadshot(PlayerPedId())
    while not IsPedheadshotReady(handle) or not IsPedheadshotValid(handle) do
        Wait(0)
    end
    local txd = GetPedheadshotTxdString(handle)

    -- Add the notification text, the more text you add the smaller the font
    -- size will become (text is forced on 1 line only), so keep this short!
    SetNotificationTextEntry("STRING")
    AddTextComponentSubstringPlayerName("Headshot")

    -- Draw the notification
    DrawNotificationAward(txd, txd, 200, 0, "FM_GEN_UNLOCK")

    -- Cleanup after yourself!
    UnregisterPedheadshot(handle)
end)
```

**Ejemplo (js):**

```js
  // This function gets the ped headshot texture and returns an url which can be used in NUI (written in TypeScript)
  
  export const GetPedHeadShotUrl = (ped: number): Promise<string> => {
    // We return a Promise so we can async await it, because registering the ped headshot takes some time.
    
    return new Promise(async res => {
        const handle = RegisterPedheadshot(ped)
        
        while (!IsPedheadshotReady(handle) || !IsPedheadshotValid(handle)) {
            // This is a custom function, not a native, which just returns a promise that is resolved after the ms specified using the setTimeout function
            await Delay(10)
        }
        
        const txdString = GetPedheadshotTxdString(handle)
        
        // We "unload" the handle as we no longer need it
        UnregisterPedheadshot(handle)
        
        // From forum post: https://forum.cfx.re/t/ped-headshot-to-image/4813157/2
        
        const pictureUrl = `https://nui-img/${txdString}/${txdString}?v=${Date.now()}`
        
        // Finally we resolve the Promise!
        res(pictureUrl)
    })
}
```

---
### RegisterPedheadshotTransparent

`REGISTER_PEDHEADSHOT_TRANSPARENT` · hash `0x953563CE563143AF` · jhash `0x4DD03628` · **Cliente**

```lua
local retval = RegisterPedheadshotTransparent(ped)
```
```c
int REGISTER_PEDHEADSHOT_TRANSPARENT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): A ped handle.

**Devuelve:** `int` — The Pedheadshot handle.

**Descripción oficial:**

Similar to REGISTER_PEDHEADSHOT but creates a transparent background instead of black.

**Result of the example code:**

![](https://i.imgur.com/TDV7XMx.png)

**Nombres antiguos (alias):** `0x953563CE563143AF` (`N_0x953563ce563143af`)

**Ejemplo (lua):**

```lua
CreateThread(function()
    -- Get the ped headshot image.
    local handle = RegisterPedheadshotTransparent(PlayerPedId())
    while not IsPedheadshotReady(handle) or not IsPedheadshotValid(handle) do
        Wait(0)
    end
    local txd = GetPedheadshotTxdString(handle)

    -- Add the notification text, the more text you add the smaller the font
    -- size will become (text is forced on 1 line only), so keep this short!
    SetNotificationTextEntry("STRING")
    AddTextComponentSubstringPlayerName("Transparent Headshot")

    -- Draw the notification
    DrawNotificationAward(txd, txd, 200, 0, "FM_GEN_UNLOCK")
    
    -- Cleanup after yourself!
    UnregisterPedheadshot(handle)
end)
```

---
### RegisterPedheadshot_3

`_REGISTER_PEDHEADSHOT_3` · hash `0xBA8805A1108A2515` · **Cliente**

```lua
local retval = RegisterPedheadshot_3(ped)
```
```c
int _REGISTER_PEDHEADSHOT_3(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xBA8805A1108A2515` (`N_0xba8805a1108a2515`)

---
### RegisterTarget

`REGISTER_TARGET` · hash `0x2F25D9AEFA34FBA2` · jhash `0x50A95442` · **Cliente**

```lua
RegisterTarget(ped, target)
```
```c
void REGISTER_TARGET(Ped ped, Ped target);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
PED::REGISTER_TARGET(l_216, PLAYER::PLAYER_PED_ID()); from re_prisonbreak.txt.  
l_216 = RECSBRobber1  
```

---
### ReleasePedPreloadPropData

`RELEASE_PED_PRELOAD_PROP_DATA` · hash `0xF79F9DEF0AADE61A` · jhash `0xFD103BA7` · **Cliente**

```lua
ReleasePedPreloadPropData(ped)
```
```c
void RELEASE_PED_PRELOAD_PROP_DATA(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF79F9DEF0AADE61A` (`N_0xf79f9def0aade61a`)

---
### ReleasePedPreloadVariationData

`RELEASE_PED_PRELOAD_VARIATION_DATA` · hash `0x5AAB586FFEC0FD96` · jhash `0x6435F67F` · **Cliente**

```lua
ReleasePedPreloadVariationData(ped)
```
```c
void RELEASE_PED_PRELOAD_VARIATION_DATA(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5AAB586FFEC0FD96` (`N_0x5aab586ffec0fd96`)

---
### ReleasePedheadshotImgUpload

`RELEASE_PEDHEADSHOT_IMG_UPLOAD` · hash `0x5D517B27CF6ECD04` · jhash `0x0DBB2FA7` · **Cliente**

```lua
ReleasePedheadshotImgUpload(id)
```
```c
void RELEASE_PEDHEADSHOT_IMG_UPLOAD(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5D517B27CF6ECD04` (`N_0x5d517b27cf6ecd04`)

---
### RemoveActionModeAsset

`REMOVE_ACTION_MODE_ASSET` · hash `0x13E940F88470FA51` · jhash `0x3F480F92` · **Cliente**

```lua
RemoveActionModeAsset(asset)
```
```c
void REMOVE_ACTION_MODE_ASSET(char* asset);
```

**Parámetros**

- `asset` (`char*`)

**Devuelve:** `void`

---
### RemoveGroup

`REMOVE_GROUP` · hash `0x8EB2F69076AF7053` · jhash `0x48D72B88` · **Cliente**

```lua
RemoveGroup(groupId)
```
```c
void REMOVE_GROUP(int groupId);
```

**Parámetros**

- `groupId` (`int`)

**Devuelve:** `void`

---
### RemovePedDefensiveArea

`REMOVE_PED_DEFENSIVE_AREA` · hash `0x74D4E028107450A9` · jhash `0x34AAAFA5` · **Cliente**

```lua
RemovePedDefensiveArea(ped, toggle)
```
```c
void REMOVE_PED_DEFENSIVE_AREA(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Ped will no longer get angry when you stay near him.  
```

---
### RemovePedElegantly

`REMOVE_PED_ELEGANTLY` · hash `0xAC6D445B994DF95E` · jhash `0x4FFB8C6C` · **Cliente**

```lua
local ped = RemovePedElegantly(ped)
```
```c
void REMOVE_PED_ELEGANTLY(Ped* ped);
```

**Parámetros**

- `ped` (`Ped*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Judging purely from a quick disassembly, if the ped is in a vehicle, the ped will be deleted immediately. If not, it'll be marked as no longer needed. 
```

---
### RemovePedFromGroup

`REMOVE_PED_FROM_GROUP` · hash `0xED74007FFB146BC2` · jhash `0x82697713` · **Cliente**

```lua
RemovePedFromGroup(ped)
```
```c
void REMOVE_PED_FROM_GROUP(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### RemovePedHelmet

`REMOVE_PED_HELMET` · hash `0xA7B2458D0AD6DED8` · jhash `0x2086B1F0` · **Cliente**

```lua
RemovePedHelmet(ped, instantly)
```
```c
void REMOVE_PED_HELMET(Ped ped, BOOL instantly);
```

**Parámetros**

- `ped` (`Ped`): Ped index.
- `instantly` (`BOOL`): Force to remove.

**Devuelve:** `void`

**Descripción oficial:**

Remove a helmet from a ped

---
### RemovePedPreferredCoverSet

`REMOVE_PED_PREFERRED_COVER_SET` · hash `0xFDDB234CF74073D9` · jhash `0xA0134498` · **Cliente**

```lua
RemovePedPreferredCoverSet(ped)
```
```c
void REMOVE_PED_PREFERRED_COVER_SET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFDDB234CF74073D9` (`N_0xfddb234cf74073d9`)

---
### RemoveRelationshipGroup

`REMOVE_RELATIONSHIP_GROUP` · hash `0xB6BA2444AB393DA2` · jhash `0x4A1DC59A` · **Cliente**

```lua
RemoveRelationshipGroup(groupHash)
```
```c
void REMOVE_RELATIONSHIP_GROUP(Hash groupHash);
```

**Parámetros**

- `groupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### RemoveScenarioBlockingArea

`REMOVE_SCENARIO_BLOCKING_AREA` · hash `0x31D16B74C6E29D66` · jhash `0x4483EF06` · **Cliente**

```lua
RemoveScenarioBlockingArea(scenarioBlockingIndex, bNetwork)
```
```c
void REMOVE_SCENARIO_BLOCKING_AREA(int scenarioBlockingIndex, BOOL bNetwork);
```

**Parámetros**

- `scenarioBlockingIndex` (`int`): the index of the Scenario blocking area
- `bNetwork` (`BOOL`): Optionally networked to all other players

**Devuelve:** `void`

---
### RemoveScenarioBlockingAreas

`REMOVE_SCENARIO_BLOCKING_AREAS` · hash `0xD37401D78A929A49` · jhash `0x4DDF845F` · **Cliente**

```lua
RemoveScenarioBlockingAreas()
```
```c
void REMOVE_SCENARIO_BLOCKING_AREAS();
```

**Devuelve:** `void`

---
### RemoveStealthModeAsset

`REMOVE_STEALTH_MODE_ASSET` · hash `0x9219857D21F0E842` · jhash `0x8C0B243A` · **Cliente**

```lua
RemoveStealthModeAsset(asset)
```
```c
void REMOVE_STEALTH_MODE_ASSET(char* asset);
```

**Parámetros**

- `asset` (`char*`)

**Devuelve:** `void`

---
### RequestActionModeAsset

`REQUEST_ACTION_MODE_ASSET` · hash `0x290E2780BB7AA598` · jhash `0x572BA553` · **Cliente**

```lua
RequestActionModeAsset(asset)
```
```c
void REQUEST_ACTION_MODE_ASSET(char* asset);
```

**Parámetros**

- `asset` (`char*`)

**Devuelve:** `void`

---
### RequestPedVehicleVisibilityTracking

`REQUEST_PED_VEHICLE_VISIBILITY_TRACKING` · hash `0x2BC338A7B21F4608` · jhash `0x31C31DAA` · **Cliente**

```lua
RequestPedVehicleVisibilityTracking(ped, p1)
```
```c
void REQUEST_PED_VEHICLE_VISIBILITY_TRACKING(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `GET_PED_FLOOD_INVINCIBILITY` (`GetPedFloodInvincibility`)

---
### RequestPedVisibilityTracking

`REQUEST_PED_VISIBILITY_TRACKING` · hash `0x7D7A2E43E74E2EB8` · jhash `0x840D24D3` · **Cliente**

```lua
RequestPedVisibilityTracking(ped)
```
```c
void REQUEST_PED_VISIBILITY_TRACKING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7D7A2E43E74E2EB8` (`N_0x7d7a2e43e74e2eb8`)

---
### RequestPedheadshotImgUpload

`REQUEST_PEDHEADSHOT_IMG_UPLOAD` · hash `0xF0DAEF2F545BEE25` · jhash `0x10F2C023` · **Cliente**

```lua
local retval = RequestPedheadshotImgUpload(id)
```
```c
BOOL REQUEST_PEDHEADSHOT_IMG_UPLOAD(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF0DAEF2F545BEE25` (`N_0xf0daef2f545bee25`)

---
### RequestStealthModeAsset

`REQUEST_STEALTH_MODE_ASSET` · hash `0x2A0A62FCDEE16D4F` · jhash `0x280A004A` · **Cliente**

```lua
RequestStealthModeAsset(asset)
```
```c
void REQUEST_STEALTH_MODE_ASSET(char* asset);
```

**Parámetros**

- `asset` (`char*`)

**Devuelve:** `void`

---
### ResetAiMeleeWeaponDamageModifier

`RESET_AI_MELEE_WEAPON_DAMAGE_MODIFIER` · hash `0x46E56A7CD1D63C3F` · jhash `0x97886238` · **Cliente**

```lua
ResetAiMeleeWeaponDamageModifier()
```
```c
void RESET_AI_MELEE_WEAPON_DAMAGE_MODIFIER();
```

**Devuelve:** `void`

---
### ResetAiWeaponDamageModifier

`RESET_AI_WEAPON_DAMAGE_MODIFIER` · hash `0xEA16670E7BA4743C` · jhash `0x6E965420` · **Cliente**

```lua
ResetAiWeaponDamageModifier()
```
```c
void RESET_AI_WEAPON_DAMAGE_MODIFIER();
```

**Devuelve:** `void`

---
### ResetGroupFormationDefaultSpacing

`RESET_GROUP_FORMATION_DEFAULT_SPACING` · hash `0x63DAB4CCB3273205` · jhash `0x267FCEAD` · **Cliente**

```lua
ResetGroupFormationDefaultSpacing(groupHandle)
```
```c
void RESET_GROUP_FORMATION_DEFAULT_SPACING(int groupHandle);
```

**Parámetros**

- `groupHandle` (`int`)

**Devuelve:** `void`

---
### ResetPedInVehicleContext

`RESET_PED_IN_VEHICLE_CONTEXT` · hash `0x22EF8FF8778030EB` · jhash `0x3C94D88A` · **Cliente**

```lua
ResetPedInVehicleContext(ped)
```
```c
void RESET_PED_IN_VEHICLE_CONTEXT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ResetPedLastVehicle

`RESET_PED_LAST_VEHICLE` · hash `0xBB8DE8CF6A8DD8BB` · jhash `0x5E3B5942` · **Cliente**

```lua
ResetPedLastVehicle(ped)
```
```c
void RESET_PED_LAST_VEHICLE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
Resets the value for the last vehicle driven by the Ped.  
```

---
### ResetPedMovementClipset

`RESET_PED_MOVEMENT_CLIPSET` · hash `0xAA74EC0CB0AAEA2C` · jhash `0xB83CEE93` · **Cliente**

```lua
ResetPedMovementClipset(ped, transitionSpeed)
```
```c
void RESET_PED_MOVEMENT_CLIPSET(Ped ped, float transitionSpeed);
```

**Parámetros**

- `ped` (`Ped`)
- `transitionSpeed` (`float`)

**Devuelve:** `void`

---
### ResetPedRagdollTimer

`RESET_PED_RAGDOLL_TIMER` · hash `0x9FA4664CF62E47E8` · jhash `0xF2865370` · **Cliente**

```lua
ResetPedRagdollTimer(ped)
```
```c
void RESET_PED_RAGDOLL_TIMER(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ResetPedStrafeClipset

`RESET_PED_STRAFE_CLIPSET` · hash `0x20510814175EA477` · jhash `0xF1967A12` · **Cliente**

```lua
ResetPedStrafeClipset(ped)
```
```c
void RESET_PED_STRAFE_CLIPSET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ResetPedVisibleDamage

`RESET_PED_VISIBLE_DAMAGE` · hash `0x3AC1F7B898F30C05` · jhash `0xC4BC4841` · **Cliente**

```lua
ResetPedVisibleDamage(ped)
```
```c
void RESET_PED_VISIBLE_DAMAGE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ResetPedWeaponMovementClipset

`RESET_PED_WEAPON_MOVEMENT_CLIPSET` · hash `0x97B0DB5B4AA74E77` · jhash `0xC60C9ACD` · **Cliente**

```lua
ResetPedWeaponMovementClipset(ped)
```
```c
void RESET_PED_WEAPON_MOVEMENT_CLIPSET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ResurrectPed

`RESURRECT_PED` · hash `0x71BC8E838B9C6035` · jhash `0xA4B82097` · **Cliente**

```lua
ResurrectPed(ped)
```
```c
void RESURRECT_PED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
This function will simply bring the dead person back to life.
Try not to use it alone, since using this function alone, will make peds fall through ground in hell(well for the most of the times).
Instead, before calling this function, you may want to declare the position, where your Resurrected ped to be spawn at.(For instance, Around 2 floats of Player's current position.)
Also, disabling any assigned task immediately helped in the number of scenarios, where If you want peds to perform certain decided tasks.
```

---
### ReviveInjuredPed

`REVIVE_INJURED_PED` · hash `0x8D8ACD8388CD99CE` · jhash `0x14D3E6E3` · **Cliente**

```lua
ReviveInjuredPed(ped)
```
```c
void REVIVE_INJURED_PED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
It will revive/cure the injured ped. The condition is ped must not be dead.  
Upon setting and converting the health int, found, if health falls below 5, the ped will lay on the ground in pain(Maximum default health is 100).  
This function is well suited there.  
```

---
### SetAiMeleeWeaponDamageModifier

`SET_AI_MELEE_WEAPON_DAMAGE_MODIFIER` · hash `0x66460DEDDD417254` · jhash `0x0F9A401F` · **Cliente**

```lua
SetAiMeleeWeaponDamageModifier(modifier)
```
```c
void SET_AI_MELEE_WEAPON_DAMAGE_MODIFIER(float modifier);
```

**Parámetros**

- `modifier` (`float`)

**Devuelve:** `void`

---
### SetAiWeaponDamageModifier

`SET_AI_WEAPON_DAMAGE_MODIFIER` · hash `0x1B1E2A40A65B8521` · jhash `0x516E30EE` · **Cliente**

```lua
SetAiWeaponDamageModifier(value)
```
```c
void SET_AI_WEAPON_DAMAGE_MODIFIER(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `void`

---
### SetAmbientPedsDropMoney

`SET_AMBIENT_PEDS_DROP_MONEY` · hash `0x6B0E6172C9A4D902` · jhash `0x30B98369` · **Cliente**

```lua
SetAmbientPedsDropMoney(p0)
```
```c
void SET_AMBIENT_PEDS_DROP_MONEY(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6B0E6172C9A4D902` (`N_0x6b0e6172c9a4d902`)

---
### SetBlockAmbientPedsFromDroppingWeaponsThisFrame

`_SET_BLOCK_AMBIENT_PEDS_FROM_DROPPING_WEAPONS_THIS_FRAME` · hash `0xC73EFFC5E043A8BA` · **Cliente**

```lua
SetBlockAmbientPedsFromDroppingWeaponsThisFrame()
```
```c
void _SET_BLOCK_AMBIENT_PEDS_FROM_DROPPING_WEAPONS_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Prevents ambient peds from dropping their weapons for the current frame.

```
NativeDB Introduced: v3258
```

---
### SetBlockingOfNonTemporaryEvents

`SET_BLOCKING_OF_NON_TEMPORARY_EVENTS` · hash `0x9F8AA94D6D97DBF4` · jhash `0xDFE34E4A` · **Cliente**

```lua
SetBlockingOfNonTemporaryEvents(ped, toggle)
```
```c
void SET_BLOCKING_OF_NON_TEMPORARY_EVENTS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
works with TASK::TASK_SET_BLOCKING_OF_NON_TEMPORARY_EVENTS to make a ped completely oblivious to all events going on around him
```

---
### SetCanAttackFriendly

`SET_CAN_ATTACK_FRIENDLY` · hash `0xB3B1CB349FF9C75D` · jhash `0x47C60963` · **Cliente**

```lua
SetCanAttackFriendly(ped, toggle, p2)
```
```c
void SET_CAN_ATTACK_FRIENDLY(Ped ped, BOOL toggle, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Setting ped to true allows the ped to shoot "friendlies".  
p2 set to true when toggle is also true seams to make peds permanently unable to aim at, even if you set p2 back to false.  
p1 = false & p2 = false for unable to aim at.  
p1 = true & p2 = false for able to aim at.  
```

---
### SetCombatFloat

`SET_COMBAT_FLOAT` · hash `0xFF41B4B141ED981C` · jhash `0xD8B7637C` · **Cliente**

```lua
SetCombatFloat(ped, combatType, p2)
```
```c
void SET_COMBAT_FLOAT(Ped ped, int combatType, float p2);
```

**Parámetros**

- `ped` (`Ped`)
- `combatType` (`int`): A value between 0-14, See [`GET_COMBAT_FLOAT`](#getcombatfloat) for a list of possible parameters.
- `p2` (`float`)

**Devuelve:** `void`

---
### SetCreateRandomCops

`SET_CREATE_RANDOM_COPS` · hash `0x102E68B2024D536D` · jhash `0x23441648` · **Cliente**

```lua
SetCreateRandomCops(toggle)
```
```c
void SET_CREATE_RANDOM_COPS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetCreateRandomCopsNotOnScenarios

`SET_CREATE_RANDOM_COPS_NOT_ON_SCENARIOS` · hash `0x8A4986851C4EF6E7` · jhash `0x82E548CC` · **Cliente**

```lua
SetCreateRandomCopsNotOnScenarios(toggle)
```
```c
void SET_CREATE_RANDOM_COPS_NOT_ON_SCENARIOS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetCreateRandomCopsOnScenarios

`SET_CREATE_RANDOM_COPS_ON_SCENARIOS` · hash `0x444CB7D7DBE6973D` · jhash `0xEDC31475` · **Cliente**

```lua
SetCreateRandomCopsOnScenarios(toggle)
```
```c
void SET_CREATE_RANDOM_COPS_ON_SCENARIOS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetDriverAbility

`SET_DRIVER_ABILITY` · hash `0xB195FFA8042FC5C3` · jhash `0xAAD4012C` · **Cliente**

```lua
SetDriverAbility(driver, ability)
```
```c
void SET_DRIVER_ABILITY(Ped driver, float ability);
```

**Parámetros**

- `driver` (`Ped`)
- `ability` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
The function specifically verifies the value is equal to, or less than 1.0f. If it is greater than 1.0f, the function does nothing at all.  
```

---
### SetDriverAggressiveness

`SET_DRIVER_AGGRESSIVENESS` · hash `0xA731F608CA104E3C` · jhash `0x8B02A8FB` · **Cliente**

```lua
SetDriverAggressiveness(driver, aggressiveness)
```
```c
void SET_DRIVER_AGGRESSIVENESS(Ped driver, float aggressiveness);
```

**Parámetros**

- `driver` (`Ped`)
- `aggressiveness` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
range 0.0f - 1.0f  
```

---
### SetDriverRacingModifier

`SET_DRIVER_RACING_MODIFIER` · hash `0xDED5AF5A0EA4B297` · jhash `0x6D55B3B3` · **Cliente**

```lua
SetDriverRacingModifier(driver, modifier)
```
```c
void SET_DRIVER_RACING_MODIFIER(Ped driver, float modifier);
```

**Parámetros**

- `driver` (`Ped`)
- `modifier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Scripts use 0.2, 0.5 and 1.0. Value must be >= 0.0 && <= 1.0
```

**Nombres antiguos (alias):** `0xDED5AF5A0EA4B297` (`N_0xded5af5a0ea4b297`)

---
### SetEnableBoundAnkles

`SET_ENABLE_BOUND_ANKLES` · hash `0xC52E0F855C58FC2E` · jhash `0x9208D689` · **Cliente**

```lua
SetEnableBoundAnkles(ped, toggle)
```
```c
void SET_ENABLE_BOUND_ANKLES(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Used with [SET_ENABLE_HANDCUFFS](#setenablehandcuffs) in decompiled scripts. From my observations, I have noticed that while being ragdolled you are not able to get up but you can still run. Your legs can also bend.

---
### SetEnableHandcuffs

`SET_ENABLE_HANDCUFFS` · hash `0xDF1AF8B5D56542FA` · jhash `0xAC9BBA23` · **Cliente**

```lua
SetEnableHandcuffs(ped, toggle)
```
```c
void SET_ENABLE_HANDCUFFS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`): The ped to toggle handcuffs on
- `toggle` (`BOOL`): true to enable handcuffs, false to disable

**Devuelve:** `void`

**Descripción oficial:**

Sets the IsHandCuffed (120) config flag on the ped. This blocks the ped from switching weapons (with the exception of switching to `weapon_unarmed`), makes the ped ragdoll on getting punched and forces a different get-up animation after ragdolling. The ped can also not vault over or climb on top of objects.

Used in combination with [SET_ENABLE_BOUND_ANKLES](#setenableboundankles) in decompiled scripts.

**Ejemplo (lua):**

```lua
local playerId = PlayerId()
local isHandcuffed = false

local function whileCuffed()
    while isHandcuffed do
        local playerPed = PlayerPedId()
        -- The ragdoll and getting up checks prevents race-conditions when the game syncs the animation to other players
        if not (IsPedRagdoll(playerPed) or IsPedGettingUp(playerPed)) and not IsEntityPlayingAnim(playerPed, 'mp_arresting', 'idle', 3) then
            TaskPlayAnim(playerPed, 'mp_arresting', 'idle', 8.0, -8, -1, 49, 0.0, false, false, false)
        end

        -- Prevents the player from punching / firing weapons
        DisablePlayerFiring(playerId, true)
        DisableControlAction(0, 140, true) -- INPUT_MELEE_ATTACK_LIGHT

        Wait(0)
    end
end

local function setPlayerInHandcuffs(state)
    local playerPed = PlayerPedId()
    SetEnableHandcuffs(playerPed, state)
    isHandcuffed = state

    if state then
        -- Request the handcuff animations (and don't proceed until it has loaded)
        RequestAnimDict('mp_arresting')
        while not HasAnimDictLoaded('mp_arresting') do Wait(0) end

        -- Disarms the player and calls the whileCuffed function inside a thread
        SetCurrentPedWeapon(playerPed, `WEAPON_UNARMED`, true)
        CreateThread(whileCuffed)
    else
        -- Unloads and stops the handcuff animation
        RemoveAnimDict('mp_arresting')
        StopAnimTask(playerPed, 'mp_arresting', 'idle', 2.0)
    end
end

setPlayerInHandcuffs(true)
```

---
### SetEnablePedEnveffScale

`SET_ENABLE_PED_ENVEFF_SCALE` · hash `0xD2C5AA0C0E8D0F1E` · jhash `0xC70F4A84` · **Cliente**

```lua
SetEnablePedEnveffScale(ped, toggle)
```
```c
void SET_ENABLE_PED_ENVEFF_SCALE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetEnableScuba

`SET_ENABLE_SCUBA` · hash `0xF99F62004024D506` · jhash `0x7BF61471` · **Cliente**

```lua
SetEnableScuba(ped, toggle)
```
```c
void SET_ENABLE_SCUBA(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enables diving motion when underwater.  
```

---
### SetEnableScubaGearLight

`_SET_ENABLE_SCUBA_GEAR_LIGHT` · hash `0xEE2476B9EE4A094F` · **Cliente**

```lua
SetEnableScubaGearLight(ped, toggle)
```
```c
void _SET_ENABLE_SCUBA_GEAR_LIGHT(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### SetFacialClipsetOverride

`_SET_FACIAL_CLIPSET_OVERRIDE` · hash `0x5687C7F05B39E401` · **Cliente**

```lua
SetFacialClipsetOverride(ped, animDict)
```
```c
void _SET_FACIAL_CLIPSET_OVERRIDE(Ped ped, char* animDict);
```

**Parámetros**

- `ped` (`Ped`)
- `animDict` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Clipsets:
"facials@gen_female@base"
"facials@gen_male@base"
"facials@p_m_zero@base"

Typically followed with [SET_FACIAL_IDLE_ANIM_OVERRIDE](#setfacialidleanimoverride):
"mood_drunk\_1"
"mood_stressed\_1"
"mood_happy\_1"
"mood_talking\_1"

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x5687C7F05B39E401` (`N_0x5687c7f05b39e401`)

---
### SetFacialIdleAnimOverride

`SET_FACIAL_IDLE_ANIM_OVERRIDE` · hash `0xFFC24B988B938B38` · jhash `0x9BA19C13` · **Cliente**

```lua
SetFacialIdleAnimOverride(ped, animName, animDict)
```
```c
void SET_FACIAL_IDLE_ANIM_OVERRIDE(Ped ped, char* animName, char* animDict);
```

**Parámetros**

- `ped` (`Ped`)
- `animName` (`char*`)
- `animDict` (`char*`)

**Devuelve:** `void`

---
### SetForceFootstepUpdate

`SET_FORCE_FOOTSTEP_UPDATE` · hash `0x129466ED55140F8D` · jhash `0x37DBC2AD` · **Cliente**

```lua
SetForceFootstepUpdate(ped, toggle)
```
```c
void SET_FORCE_FOOTSTEP_UPDATE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x129466ED55140F8D` (`N_0x129466ed55140f8d`)

---
### SetForceStepType

`SET_FORCE_STEP_TYPE` · hash `0xCB968B53FC7F916D` · jhash `0xC0F1BC91` · **Cliente**

```lua
SetForceStepType(ped, p1, type, p3)
```
```c
void SET_FORCE_STEP_TYPE(Ped ped, BOOL p1, int type, int p3);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `type` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCB968B53FC7F916D` (`N_0xcb968b53fc7f916d`)

---
### SetGroupFormation

`SET_GROUP_FORMATION` · hash `0xCE2F5FC3AF7E8C1E` · jhash `0x08FAC739` · **Cliente**

```lua
SetGroupFormation(groupId, formationType)
```
```c
void SET_GROUP_FORMATION(int groupId, int formationType);
```

**Parámetros**

- `groupId` (`int`)
- `formationType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
0: Freedom to move
1: Circle Around Leader
2: Alternative Circle Around Leader  
3: Line, with Leader at center  
4: Arrow Formation
5: "V" Formation
6: Line Follow Formation
7: Single Formation
8: Pairwise
```

---
### SetGroupFormationSpacing

`SET_GROUP_FORMATION_SPACING` · hash `0x1D9D45004C28C916` · jhash `0xB1E086FF` · **Cliente**

```lua
SetGroupFormationSpacing(groupId, p1, p2, p3)
```
```c
void SET_GROUP_FORMATION_SPACING(int groupId, float p1, float p2, float p3);
```

**Parámetros**

- `groupId` (`int`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### SetGroupSeparationRange

`SET_GROUP_SEPARATION_RANGE` · hash `0x4102C7858CFEE4E4` · jhash `0x7B820CD5` · **Cliente**

```lua
SetGroupSeparationRange(groupHandle, separationRange)
```
```c
void SET_GROUP_SEPARATION_RANGE(int groupHandle, float separationRange);
```

**Parámetros**

- `groupHandle` (`int`)
- `separationRange` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the range at which members will automatically leave the group.  
```

---
### SetHeadBlendPaletteColor

`SET_HEAD_BLEND_PALETTE_COLOR` · hash `0xCC9682B8951C5229` · jhash `0x57E5B3F9` · **Cliente**

```lua
SetHeadBlendPaletteColor(ped, r, g, b, id)
```
```c
void SET_HEAD_BLEND_PALETTE_COLOR(Ped ped, int r, int g, int b, int id);
```

**Parámetros**

- `ped` (`Ped`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `id` (`int`): From 0 to 3.

**Devuelve:** `void`

**Descripción oficial:**

Preview: https://gfycat.com/MaleRareAmazonparrot

**Nombres antiguos (alias):** `0xCC9682B8951C5229` (`N_0xcc9682b8951c5229`)

---
### SetIkTarget

`SET_IK_TARGET` · hash `0xC32779C16FCEECD9` · jhash `0x6FE5218C` · **Cliente**

```lua
SetIkTarget(ped, ikIndex, entityLookAt, boneLookAt, offsetX, offsetY, offsetZ, ikTargetFlags, blendInDuration, blendOutDuration)
```
```c
void SET_IK_TARGET(Ped ped, int ikIndex, Entity entityLookAt, int boneLookAt, float offsetX, float offsetY, float offsetZ, int ikTargetFlags, int blendInDuration, int blendOutDuration);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `ikIndex` (`int`): See `eIkPart` for indexes.
- `entityLookAt` (`Entity`): Set to 0 for no entity, offsets will be world coordinates instead.
- `boneLookAt` (`int`): Set to -1 for no target bone.
- `offsetX` (`float`): X-axis offset calculated from the position of `entityLookAt`.
- `offsetY` (`float`): Y-axis offset calculated from the position of `entityLookAt`.
- `offsetZ` (`float`): Z-axis offset calculated from the position of `entityLookAt`.
- `ikTargetFlags` (`int`): See `eIkTargetFlags` for flags.
- `blendInDuration` (`int`): Animation blending in (in ms). `-1` by default.
- `blendOutDuration` (`int`): Animation blending out (in ms). `-1` by default.

**Devuelve:** `void`

**Descripción oficial:**

Sets the IK target for a given IK part belonging to the ped.

**Please note:** The IK target will only be valid for one update, so it needs to be set for as long as it is needed (to avoid IK targets not being cleared and getting stuck enabled).

```cpp
enum eIkPart {
  IK_PART_INVALID = 0,
  // head
  IK_PART_HEAD = 1,
  // spine
  IK_PART_SPINE = 2,
  // Left Arm
  IK_PART_ARM_LEFT = 3,
  // Right Arm
  IK_PART_ARM_RIGHT = 4,
  // Left Leg
  IK_PART_LEG_LEFT = 5,
  // Right Leg
  IK_PART_LEG_RIGHT = 6
};

```

```cpp
enum eIkTargetFlags {
  ITF_DEFAULT = 0,
  // arm target relative to the handbone
  ITF_ARM_TARGET_WRT_HANDBON = 1,
  // arm target relative to the pointhelper
  ITF_ARM_TARGET_WRT_POINTHELPER = 2,
  // arm target relative to the ikhelper
  ITF_ARM_TARGET_WRT_IKHELPE = 4,
  // use animation tags directly
  ITF_IK_TAG_MODE_NORMAL = 8,
  // use animation tags in ALLOW mode
  ITF_IK_TAG_MODE_ALLOW = 16,
  // use animation tags in BLOCK mode
  ITF_IK_TAG_MODE_BLOCK = 32,
  // solve for orientation in addition to position
  ITF_ARM_USE_ORIENTATION = 64
};

```

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
-- Points the right arm to -1849.0, -1231.0, 13.0 for 10 seconds
SetIkTarget(PlayerPedId(), 4, 0, 0, -1849.0, -1231.0, 13.0, 0, 0, 10000)
```

**Ejemplo (js):**

```js
// Points the right arm to -1849.0, -1231.0, 13.0 for 10 seconds
SetIkTarget(PlayerPedId(), 4, 0, 0, -1849.0, -1231.0, 13.0, 0, 0, 10000);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

// Points the right arm to -1849.0, -1231.0, 13.0 for 10 seconds
SetIkTarget(PlayerPedId(), 4, 0, 0, -1849.0f, -1231.0f, 13.0f, 0, 0, 10000);
```

---
### SetMovementModeOverride

`SET_MOVEMENT_MODE_OVERRIDE` · hash `0x781DE8FA214E87D2` · jhash `0x83BAE814` · **Cliente**

```lua
SetMovementModeOverride(ped, name)
```
```c
void SET_MOVEMENT_MODE_OVERRIDE(Ped ped, char* name);
```

**Parámetros**

- `ped` (`Ped`)
- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
name: "MP_FEMALE_ACTION" found multiple times in the b617d scripts.
```

**Nombres antiguos (alias):** `0x781DE8FA214E87D2` (`N_0x781de8fa214e87d2`)

---
### SetPedAccuracy

`SET_PED_ACCURACY` · hash `0x7AEFB85C1D49DEB6` · jhash `0x6C17122E` · **Cliente**

```lua
SetPedAccuracy(ped, accuracy)
```
```c
void SET_PED_ACCURACY(Ped ped, int accuracy);
```

**Parámetros**

- `ped` (`Ped`)
- `accuracy` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
accuracy = 0-100, 100 being perfectly accurate
```

---
### SetPedAlertness

`SET_PED_ALERTNESS` · hash `0xDBA71115ED9941A6` · jhash `0x2C32D9AE` · **Cliente**

```lua
SetPedAlertness(ped, value)
```
```c
void SET_PED_ALERTNESS(Ped ped, int value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
value ranges from 0 to 3.  
```

---
### SetPedAllowVehiclesOverride

`SET_PED_ALLOW_VEHICLES_OVERRIDE` · hash `0x3C028C636A414ED9` · jhash `0x58A80BD5` · **Cliente**

```lua
SetPedAllowVehiclesOverride(ped, toggle)
```
```c
void SET_PED_ALLOW_VEHICLES_OVERRIDE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedAllowedToDuck

`SET_PED_ALLOWED_TO_DUCK` · hash `0xDA1F1B7BE1A8766F` · jhash `0xC4D122F8` · **Cliente**

```lua
SetPedAllowedToDuck(ped, toggle)
```
```c
void SET_PED_ALLOWED_TO_DUCK(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedAlternateMovementAnim

`SET_PED_ALTERNATE_MOVEMENT_ANIM` · hash `0x90A43CC281FFAB46` · jhash `0xBA84FD8C` · **Cliente**

```lua
SetPedAlternateMovementAnim(ped, stance, animDictionary, animationName, p4, p5)
```
```c
void SET_PED_ALTERNATE_MOVEMENT_ANIM(Ped ped, int stance, char* animDictionary, char* animationName, float p4, BOOL p5);
```

**Parámetros**

- `ped` (`Ped`)
- `stance` (`int`)
- `animDictionary` (`char*`)
- `animationName` (`char*`)
- `p4` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
stance:  
0 = idle  
1 = walk  
2 = running  
p5 = usually set to true  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### SetPedAlternateWalkAnim

`SET_PED_ALTERNATE_WALK_ANIM` · hash `0x6C60394CB4F75E9A` · jhash `0x895E1D67` · **Cliente**

```lua
SetPedAlternateWalkAnim(ped, animDict, animName, p3, p4)
```
```c
void SET_PED_ALTERNATE_WALK_ANIM(Ped ped, char* animDict, char* animName, float p3, BOOL p4);
```

**Parámetros**

- `ped` (`Ped`)
- `animDict` (`char*`)
- `animName` (`char*`)
- `p3` (`float`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### SetPedAngledDefensiveArea

`SET_PED_ANGLED_DEFENSIVE_AREA` · hash `0xC7F76DF27A5045A1` · jhash `0x3EFBDD9B` · **Cliente**

```lua
SetPedAngledDefensiveArea(ped, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
void SET_PED_ANGLED_DEFENSIVE_AREA(Ped ped, float p1, float p2, float p3, float p4, float p5, float p6, float p7, BOOL p8, BOOL p9);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)
- `p8` (`BOOL`)
- `p9` (`BOOL`)

**Devuelve:** `void`

---
### SetPedAoBlobRendering

`SET_PED_AO_BLOB_RENDERING` · hash `0x2B5AA717A181FB4C` · jhash `0x98E29ED0` · **Cliente**

```lua
SetPedAoBlobRendering(ped, toggle)
```
```c
void SET_PED_AO_BLOB_RENDERING(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enable/disable ped shadow (ambient occlusion). https://gfycat.com/thankfulesteemedgecko
```

**Nombres antiguos (alias):** `0x2B5AA717A181FB4C` (`N_0x2b5aa717a181fb4c`)

---
### SetPedArmour

`SET_PED_ARMOUR` · hash `0xCEA04D83135264CC` · jhash `0x4E3A0CC4` · **Cliente · también en el servidor (RPC)**

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

---
### SetPedAsCop

`SET_PED_AS_COP` · hash `0xBB03C38DD3FB7FFD` · jhash `0x84E7DE9F` · **Cliente**

```lua
SetPedAsCop(ped, toggle)
```
```c
void SET_PED_AS_COP(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Turns the desired ped into a cop. If you use this on the player ped, you will become almost invisible to cops dispatched for you. You will also report your own crimes, get a generic cop voice, get a cop-vision-cone on the radar, and you will be unable to shoot at other cops. SWAT and Army will still shoot at you. Toggling ped as "false" has no effect; you must change p0's ped model to disable the effect.  
```

---
### SetPedAsEnemy

`SET_PED_AS_ENEMY` · hash `0x02A0C9720B854BFA` · jhash `0xAE620A1B` · **Cliente**

```lua
SetPedAsEnemy(ped, toggle)
```
```c
void SET_PED_AS_ENEMY(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedAsGroupLeader

`SET_PED_AS_GROUP_LEADER` · hash `0x2A7819605465FBCE` · jhash `0x7265BEA2` · **Cliente**

```lua
SetPedAsGroupLeader(ped, groupId)
```
```c
void SET_PED_AS_GROUP_LEADER(Ped ped, int groupId);
```

**Parámetros**

- `ped` (`Ped`)
- `groupId` (`int`)

**Devuelve:** `void`

---
### SetPedAsGroupMember

`SET_PED_AS_GROUP_MEMBER` · hash `0x9F3480FE65DB31B5` · jhash `0x0EE13F92` · **Cliente**

```lua
SetPedAsGroupMember(ped, groupId)
```
```c
void SET_PED_AS_GROUP_MEMBER(Ped ped, int groupId);
```

**Parámetros**

- `ped` (`Ped`)
- `groupId` (`int`)

**Devuelve:** `void`

---
### SetPedBlendFromParents

`SET_PED_BLEND_FROM_PARENTS` · hash `0x137BBD05230DB22D` · jhash `0x837BD370` · **Cliente**

```lua
SetPedBlendFromParents(ped, father, mother, fathersSide, mothersSide)
```
```c
void SET_PED_BLEND_FROM_PARENTS(Ped ped, Ped father, Ped mother, float fathersSide, float mothersSide);
```

**Parámetros**

- `ped` (`Ped`)
- `father` (`Ped`)
- `mother` (`Ped`)
- `fathersSide` (`float`)
- `mothersSide` (`float`)

**Devuelve:** `void`

---
### SetPedBlocksPathingWhenDead

`SET_PED_BLOCKS_PATHING_WHEN_DEAD` · hash `0x576594E8D64375E2` · jhash `0x1D87DDC1` · **Cliente**

```lua
SetPedBlocksPathingWhenDead(ped, toggle)
```
```c
void SET_PED_BLOCKS_PATHING_WHEN_DEAD(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x576594E8D64375E2` (`N_0x576594e8d64375e2`)

---
### SetPedBoundsOrientation

`SET_PED_BOUNDS_ORIENTATION` · hash `0x4F5F651ACCC9C4CF` · jhash `0xCFA20D68` · **Cliente**

```lua
SetPedBoundsOrientation(ped, p1, p2, p3, p4, p5)
```
```c
void SET_PED_BOUNDS_ORIENTATION(Ped ped, float p1, float p2, float p3, float p4, float p5);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `void`

---
### SetPedCanArmIk

`SET_PED_CAN_ARM_IK` · hash `0x6C3B4D6D13B4C841` · jhash `0x343B4DE0` · **Cliente**

```lua
SetPedCanArmIk(ped, toggle)
```
```c
void SET_PED_CAN_ARM_IK(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanBeDraggedOut

`SET_PED_CAN_BE_DRAGGED_OUT` · hash `0xC1670E958EEE24E5` · jhash `0xAA7F1131` · **Cliente**

```lua
SetPedCanBeDraggedOut(ped, toggle)
```
```c
void SET_PED_CAN_BE_DRAGGED_OUT(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanBeKnockedOffVehicle

`SET_PED_CAN_BE_KNOCKED_OFF_VEHICLE` · hash `0x7A6535691B477C48` · jhash `0x8A251612` · **Cliente**

```lua
SetPedCanBeKnockedOffVehicle(ped, state)
```
```c
void SET_PED_CAN_BE_KNOCKED_OFF_VEHICLE(Ped ped, int state);
```

**Parámetros**

- `ped` (`Ped`)
- `state` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
state: https://alloc8or.re/gta5/doc/enums/eKnockOffVehicle.txt
```

---
### SetPedCanBeShotInVehicle

`SET_PED_CAN_BE_SHOT_IN_VEHICLE` · hash `0xC7EF1BA83230BA07` · jhash `0x5DB7B3A9` · **Cliente**

```lua
SetPedCanBeShotInVehicle(ped, toggle)
```
```c
void SET_PED_CAN_BE_SHOT_IN_VEHICLE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanBeTargetedWhenInjured

`SET_PED_CAN_BE_TARGETED_WHEN_INJURED` · hash `0x638C03B0F9878F57` · jhash `0x6FD9A7CD` · **Cliente**

```lua
SetPedCanBeTargetedWhenInjured(ped, toggle)
```
```c
void SET_PED_CAN_BE_TARGETED_WHEN_INJURED(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanBeTargetedWithoutLos

`SET_PED_CAN_BE_TARGETED_WITHOUT_LOS` · hash `0x4328652AE5769C71` · jhash `0x7FDDC0A6` · **Cliente**

```lua
SetPedCanBeTargetedWithoutLos(ped, toggle)
```
```c
void SET_PED_CAN_BE_TARGETED_WITHOUT_LOS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanBeTargetted

`SET_PED_CAN_BE_TARGETTED` · hash `0x63F58F7C80513AAD` · jhash `0x75C49F74` · **Cliente**

```lua
SetPedCanBeTargetted(ped, toggle)
```
```c
void SET_PED_CAN_BE_TARGETTED(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanBeTargettedByPlayer

`SET_PED_CAN_BE_TARGETTED_BY_PLAYER` · hash `0x66B57B72E0836A76` · jhash `0xD050F490` · **Cliente**

```lua
SetPedCanBeTargettedByPlayer(ped, player, toggle)
```
```c
void SET_PED_CAN_BE_TARGETTED_BY_PLAYER(Ped ped, Player player, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanBeTargettedByTeam

`SET_PED_CAN_BE_TARGETTED_BY_TEAM` · hash `0xBF1CA77833E58F2C` · jhash `0xB103A8E1` · **Cliente**

```lua
SetPedCanBeTargettedByTeam(ped, team, toggle)
```
```c
void SET_PED_CAN_BE_TARGETTED_BY_TEAM(Ped ped, int team, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `team` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanCowerInCover

`SET_PED_CAN_COWER_IN_COVER` · hash `0xCB7553CDCEF4A735` · jhash `0x5194658B` · **Cliente**

```lua
SetPedCanCowerInCover(ped, toggle)
```
```c
void SET_PED_CAN_COWER_IN_COVER(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
It simply makes the said ped to cower behind cover object(wall, desk, car)  
Peds flee attributes must be set to not to flee, first. Else, most of the peds, will just flee from gunshot sounds or any other panic situations.  
```

---
### SetPedCanEvasiveDive

`SET_PED_CAN_EVASIVE_DIVE` · hash `0x6B7A646C242A7059` · jhash `0x542FEB4D` · **Cliente**

```lua
SetPedCanEvasiveDive(ped, toggle)
```
```c
void SET_PED_CAN_EVASIVE_DIVE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanHeadIk

`SET_PED_CAN_HEAD_IK` · hash `0xC11C18092C5530DC` · jhash `0xD3B04476` · **Cliente**

```lua
SetPedCanHeadIk(ped, toggle)
```
```c
void SET_PED_CAN_HEAD_IK(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanLegIk

`SET_PED_CAN_LEG_IK` · hash `0x73518ECE2485412B` · jhash `0x9955BC6F` · **Cliente**

```lua
SetPedCanLegIk(ped, toggle)
```
```c
void SET_PED_CAN_LEG_IK(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanLosePropsOnDamage

`SET_PED_CAN_LOSE_PROPS_ON_DAMAGE` · hash `0xE861D0B05C7662B8` · jhash `0x2F9550C2` · **Cliente**

```lua
SetPedCanLosePropsOnDamage(ped, loseProps, p2)
```
```c
void SET_PED_CAN_LOSE_PROPS_ON_DAMAGE(Ped ped, BOOL loseProps, int p2);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `loseProps` (`BOOL`): true = allow props to fall off, false = don't let props fall off
- `p2` (`int`): purpose unknown, usually 0

**Devuelve:** `void`

**Descripción oficial:**

It makes the ped lose (or not lose) their props (like glasses or helmets/hat) when someone punches or pushes the ped.
This is probably what's being used in GTA:O to keep players from knocking other player's hats/glasses off when in combat.

**Nombres antiguos (alias):** `0xE861D0B05C7662B8` (`N_0xe861d0b05c7662b8`)

**Ejemplo (lua):**

```lua
-- Make the ped NOT lose their props when they're hit or pushed.
SetPedCanLosePropsOnDamage(PlayerPedId(), false, 0)

-- Make the ped LOSE their props when they're hit or pushed.
SetPedCanLosePropsOnDamage(PlayerPedId(), true, 0)
```

---
### SetPedCanPeekInCover

`SET_PED_CAN_PEEK_IN_COVER` · hash `0xC514825C507E3736` · jhash `0xC1DAE216` · **Cliente**

```lua
SetPedCanPeekInCover(ped, toggle)
```
```c
void SET_PED_CAN_PEEK_IN_COVER(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanPlayAmbientAnims

`SET_PED_CAN_PLAY_AMBIENT_ANIMS` · hash `0x6373D1349925A70E` · jhash `0xF8053081` · **Cliente**

```lua
SetPedCanPlayAmbientAnims(ped, toggle)
```
```c
void SET_PED_CAN_PLAY_AMBIENT_ANIMS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanPlayAmbientBaseAnims

`SET_PED_CAN_PLAY_AMBIENT_BASE_ANIMS` · hash `0x0EB0585D15254740` · jhash `0x5720A5DD` · **Cliente**

```lua
SetPedCanPlayAmbientBaseAnims(ped, toggle)
```
```c
void SET_PED_CAN_PLAY_AMBIENT_BASE_ANIMS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanPlayGestureAnims

`SET_PED_CAN_PLAY_GESTURE_ANIMS` · hash `0xBAF20C5432058024` · jhash `0xE131E3B3` · **Cliente**

```lua
SetPedCanPlayGestureAnims(ped, toggle)
```
```c
void SET_PED_CAN_PLAY_GESTURE_ANIMS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanPlayInjuredAnims

`_SET_PED_CAN_PLAY_INJURED_ANIMS` · hash `0x33A60D8BDD6E508C` · jhash `0xADB2511A` · **Cliente**

```lua
SetPedCanPlayInjuredAnims(ped, p1)
```
```c
void _SET_PED_CAN_PLAY_INJURED_ANIMS(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x33A60D8BDD6E508C` (`N_0x33a60d8bdd6e508c`)

---
### SetPedCanPlayVisemeAnims

`SET_PED_CAN_PLAY_VISEME_ANIMS` · hash `0xF833DDBA3B104D43` · jhash `0xA2FDAF27` · **Cliente**

```lua
SetPedCanPlayVisemeAnims(ped, toggle, p2)
```
```c
void SET_PED_CAN_PLAY_VISEME_ANIMS(Ped ped, BOOL toggle, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p2 usually 0  
```

---
### SetPedCanRagdoll

`SET_PED_CAN_RAGDOLL` · hash `0xB128377056A54E2A` · jhash `0xCF1384C4` · **Cliente · también en el servidor (RPC)**

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

---
### SetPedCanRagdollFromPlayerImpact

`SET_PED_CAN_RAGDOLL_FROM_PLAYER_IMPACT` · hash `0xDF993EE5E90ABA25` · jhash `0xE9BD733A` · **Cliente**

```lua
SetPedCanRagdollFromPlayerImpact(ped, toggle)
```
```c
void SET_PED_CAN_RAGDOLL_FROM_PLAYER_IMPACT(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanSmashGlass

`SET_PED_CAN_SMASH_GLASS` · hash `0x1CCE141467FF42A2` · jhash `0x149C60A8` · **Cliente**

```lua
SetPedCanSmashGlass(ped, p1, p2)
```
```c
void SET_PED_CAN_SMASH_GLASS(Ped ped, BOOL p1, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanSwitchWeapon

`SET_PED_CAN_SWITCH_WEAPON` · hash `0xED7F7EFE9FABF340` · jhash `0xB5F8BA28` · **Cliente**

```lua
SetPedCanSwitchWeapon(ped, toggle)
```
```c
void SET_PED_CAN_SWITCH_WEAPON(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanTeleportToGroupLeader

`SET_PED_CAN_TELEPORT_TO_GROUP_LEADER` · hash `0x2E2F4240B3F24647` · jhash `0xD0D8BDBC` · **Cliente**

```lua
SetPedCanTeleportToGroupLeader(pedHandle, groupHandle, toggle)
```
```c
void SET_PED_CAN_TELEPORT_TO_GROUP_LEADER(Ped pedHandle, int groupHandle, BOOL toggle);
```

**Parámetros**

- `pedHandle` (`Ped`)
- `groupHandle` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This only will teleport the ped to the group leader if the group leader teleports (sets coords).  
Only works in singleplayer  
```

---
### SetPedCanTorsoIk

`SET_PED_CAN_TORSO_IK` · hash `0xF2B7106D37947CE0` · jhash `0x8E5D4EAB` · **Cliente**

```lua
SetPedCanTorsoIk(ped, toggle)
```
```c
void SET_PED_CAN_TORSO_IK(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCanTorsoReactIk

`SET_PED_CAN_TORSO_REACT_IK` · hash `0xF5846EDB26A98A24` · jhash `0x7B0040A8` · **Cliente**

```lua
SetPedCanTorsoReactIk(ped, p1)
```
```c
void SET_PED_CAN_TORSO_REACT_IK(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF5846EDB26A98A24` (`N_0xf5846edb26a98a24`)

---
### SetPedCanTorsoVehicleIk

`SET_PED_CAN_TORSO_VEHICLE_IK` · hash `0x6647C5F6F5792496` · jhash `0x0FDA62DE` · **Cliente**

```lua
SetPedCanTorsoVehicleIk(ped, p1)
```
```c
void SET_PED_CAN_TORSO_VEHICLE_IK(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6647C5F6F5792496` (`N_0x6647c5f6f5792496`)

---
### SetPedCanUseAutoConversationLookat

`SET_PED_CAN_USE_AUTO_CONVERSATION_LOOKAT` · hash `0xEC4686EC06434678` · jhash `0x584C5178` · **Cliente**

```lua
SetPedCanUseAutoConversationLookat(ped, toggle)
```
```c
void SET_PED_CAN_USE_AUTO_CONVERSATION_LOOKAT(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedCapsule

`SET_PED_CAPSULE` · hash `0x364DF566EC833DE2` · jhash `0xB153E1B9` · **Cliente**

```lua
SetPedCapsule(ped, value)
```
```c
void SET_PED_CAPSULE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Overrides the ped's collision capsule radius for the current tick.  
Must be called every tick to be effective.  
Setting this to 0.001 will allow warping through some objects.  
```

---
### SetPedClothPackageIndex

`SET_PED_CLOTH_PACKAGE_INDEX` · hash `0x78C4E9961DB3EB5B` · jhash `0xFC942D7C` · **Cliente**

```lua
SetPedClothPackageIndex(ped, p1)
```
```c
void SET_PED_CLOTH_PACKAGE_INDEX(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x78C4E9961DB3EB5B` (`N_0x78c4e9961db3eb5b`)

---
### SetPedClothProne

`SET_PED_CLOTH_PRONE` · hash `0x82A3D6D9CC2CB8E3` · jhash `0x89EEE07B` · **Cliente**

```lua
SetPedClothProne(p0, p1)
```
```c
void SET_PED_CLOTH_PRONE(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x82A3D6D9CC2CB8E3` (`N_0x82a3d6d9cc2cb8e3`)

---
### SetPedCombatAbility

`SET_PED_COMBAT_ABILITY` · hash `0xC7622C0D36B2FDA8` · jhash `0x6C23D329` · **Cliente**

```lua
SetPedCombatAbility(ped, p1)
```
```c
void SET_PED_COMBAT_ABILITY(Ped ped, int p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
100 would equal attack  
less then 50ish would mean run away  
Only the values 0, 1 and 2 occur in the decompiled scripts. Most likely refers directly to the values also described in combatbehaviour.meta:  
0: CA_Poor  
1: CA_Average  
2: CA_Professional  
Tested this and got the same results as the first explanation here. Could not find any difference between 0, 1 and 2.  
```

---
### SetPedCombatAttributes

`SET_PED_COMBAT_ATTRIBUTES` · hash `0x9F7794730795E019` · jhash `0x81D64248` · **Cliente**

```lua
SetPedCombatAttributes(ped, attributeIndex, enabled)
```
```c
void SET_PED_COMBAT_ATTRIBUTES(Ped ped, int attributeIndex, BOOL enabled);
```

**Parámetros**

- `ped` (`Ped`): The ped to set attributes to.
- `attributeIndex` (`int`): The attribute index to set. See `eCombatAttribute` enum.
- `enabled` (`BOOL`): A boolean to enable/disable the attribute (true/false).

**Devuelve:** `void`

**Descripción oficial:**

These combat attributes seem to be the same as the BehaviourFlags from combatbehaviour.meta.

So far, these are the equivalents found:

```cpp
enum eCombatAttribute
{
  CA_INVALID = -1,	
  // AI will only use cover if this is set
  CA_USE_COVER = 0,
  // AI will only use vehicles if this is set
  CA_USE_VEHICLE = 1,
  // AI will only driveby from a vehicle if this is set
  CA_DO_DRIVEBYS = 2,
  // Will be forced to stay in a ny vehicel if this isn't set
  CA_LEAVE_VEHICLES = 3,
  // This ped can make decisions on whether to strafe or not based on distance to destination, recent bullet events, etc.
  CA_CAN_USE_DYNAMIC_STRAFE_DECISIONS	= 4,
  // Ped will always fight upon getting threat response task
  CA_ALWAYS_FIGHT = 5,
  // If in combat and in a vehicle, the ped will flee rather than attacking
  CA_FLEE_WHILST_IN_VEHICLE = 6,
  // If in combat and chasing in a vehicle, the ped will keep a distance behind rather than ramming
  CA_JUST_FOLLOW_VEHICLE = 7,
  // Deprecated
  CA_PLAY_REACTION_ANIMS = 8,
  // Peds will scan for and react to dead peds found
  CA_WILL_SCAN_FOR_DEAD_PEDS = 9,
  // Deprecated
  CA_IS_A_GUARD = 10,
  // The ped will seek cover only 
  CA_JUST_SEEK_COVER = 11,
  // Ped will only blind fire when in cover
  CA_BLIND_FIRE_IN_COVER = 12,
  // Ped may advance
  CA_AGGRESSIVE = 13,
  // Ped can investigate events such as distant gunfire, footsteps, explosions etc
  CA_CAN_INVESTIGATE = 14,
  // Ped can use a radio to call for backup (happens after a reaction)
  CA_CAN_USE_RADIO = 15,
  // Deprecated
  CA_CAN_CAPTURE_ENEMY_PEDS = 16,
  // Ped will always flee upon getting threat response task
  CA_ALWAYS_FLEE = 17,
  // Ped can do unarmed taunts in vehicle
  CA_CAN_TAUNT_IN_VEHICLE = 20,
  // Ped will be able to chase their targets if both are on foot and the target is running away
  CA_CAN_CHASE_TARGET_ON_FOOT = 21,
  // Ped can drag injured peds to safety
  CA_WILL_DRAG_INJURED_PEDS_TO_SAFETY = 22,
  // Ped will require LOS to the target it is aiming at before shooting
  CA_REQUIRES_LOS_TO_SHOOT = 23,
  // Ped is allowed to use proximity based fire rate (increasing fire rate at closer distances)
  CA_USE_PROXIMITY_FIRING_RATE = 24,
  // Normally peds can switch briefly to a secondary target in combat, setting this will prevent that
  CA_DISABLE_SECONDARY_TARGET = 25,
  // This will disable the flinching combat entry reactions for peds, instead only playing the turn and aim anims
  CA_DISABLE_ENTRY_REACTIONS = 26,
  // Force ped to be 100% accurate in all situations (added by Jay Reinebold)
  CA_PERFECT_ACCURACY = 27,
  // If we don't have cover and can't see our target it's possible we will advance, even if the target is in cover
  CA_CAN_USE_FRUSTRATED_ADVANCE	= 28,
  // This will have the ped move to defensive areas and within attack windows before performing the cover search
  CA_MOVE_TO_LOCATION_BEFORE_COVER_SEARCH = 29,
  // Allow shooting of our weapon even if we don't have LOS (this isn't X-ray vision as it only affects weapon firing)
  CA_CAN_SHOOT_WITHOUT_LOS = 30,
  // Ped will try to maintain a min distance to the target, even if using defensive areas (currently only for cover finding + usage) 
  CA_MAINTAIN_MIN_DISTANCE_TO_TARGET = 31,
  // Allows ped to use steamed variations of peeking anims
  CA_CAN_USE_PEEKING_VARIATIONS	= 34,
  // Disables pinned down behaviors
  CA_DISABLE_PINNED_DOWN = 35,
  // Disables pinning down others
  CA_DISABLE_PIN_DOWN_OTHERS = 36,
  // When defensive area is reached the area is cleared and the ped is set to use defensive combat movement
  CA_OPEN_COMBAT_WHEN_DEFENSIVE_AREA_IS_REACHED = 37,
  // Disables bullet reactions
  CA_DISABLE_BULLET_REACTIONS = 38,
  // Allows ped to bust the player
  CA_CAN_BUST = 39,
  // This ped is ignored by other peds when wanted
  CA_IGNORED_BY_OTHER_PEDS_WHEN_WANTED = 40,
  // Ped is allowed to "jack" vehicles when needing to chase a target in combat
  CA_CAN_COMMANDEER_VEHICLES = 41,
  // Ped is allowed to flank
  CA_CAN_FLANK = 42,
  // Ped will switch to advance if they can't find cover
  CA_SWITCH_TO_ADVANCE_IF_CANT_FIND_COVER = 43,
  // Ped will switch to defensive if they are in cover
  CA_SWITCH_TO_DEFENSIVE_IF_IN_COVER = 44,
  // Ped will clear their primary defensive area when it is reached
  CA_CLEAR_PRIMARY_DEFENSIVE_AREA_WHEN_REACHED = 45,
  // Ped is allowed to fight armed peds when not armed
  CA_CAN_FIGHT_ARMED_PEDS_WHEN_NOT_ARMED = 46,
  // Ped is not allowed to use tactical points if set to use defensive movement (will only use cover)
  CA_ENABLE_TACTICAL_POINTS_WHEN_DEFENSIVE = 47,
  // Ped cannot adjust cover arcs when testing cover safety (atm done on corner cover points when  ped usingdefensive area + no LOS)
  CA_DISABLE_COVER_ARC_ADJUSTMENTS = 48,
  // Ped may use reduced accuracy with large number of enemies attacking the same local player target
  CA_USE_ENEMY_ACCURACY_SCALING	= 49,
  // Ped is allowed to charge the enemy position
  CA_CAN_CHARGE = 50,
  // When defensive area is reached the area is cleared and the ped is set to use will advance movement
  CA_REMOVE_AREA_SET_WILL_ADVANCE_WHEN_DEFENSIVE_AREA_REACHED = 51,
  // Use the vehicle attack mission during combat (only works on driver)
  CA_USE_VEHICLE_ATTACK = 52,
  // Use the vehicle attack mission during combat if the vehicle has mounted guns (only works on driver)
  CA_USE_VEHICLE_ATTACK_IF_VEHICLE_HAS_MOUNTED_GUNS = 53,
  // Always equip best weapon in combat
  CA_ALWAYS_EQUIP_BEST_WEAPON = 54,
  // Ignores in water at depth visibility check
  CA_CAN_SEE_UNDERWATER_PEDS = 55,
  // Will prevent this ped from aiming at any AI targets that are in helicopters
  CA_DISABLE_AIM_AT_AI_TARGETS_IN_HELIS = 56,
  // Disables peds seeking due to no clear line of sight
  CA_DISABLE_SEEK_DUE_TO_LINE_OF_SIGHT = 57,
  // To be used when releasing missions peds if we don't want them fleeing from combat (mission peds already prevent flee)
  CA_DISABLE_FLEE_FROM_COMBAT = 58,
  // Disables target changes during vehicle pursuit
  CA_DISABLE_TARGET_CHANGES_DURING_VEHICLE_PURSUIT = 59,
  // Ped may throw a smoke grenade at player loitering in combat
  CA_CAN_THROW_SMOKE_GRENADE = 60,
  // Will clear a set defensive area if that area cannot be reached
  CA_CLEAR_AREA_SET_DEFENSIVE_IF_DEFENSIVE_CANNOT_BE_REACHED = 62,
  // Disable block from pursue during vehicle chases
  CA_DISABLE_BLOCK_FROM_PURSUE_DURING_VEHICLE_CHASE = 64,
  // Disable spin out during vehicle chases
  CA_DISABLE_SPIN_OUT_DURING_VEHICLE_CHASE = 65,
  // Disable cruise in front during block during vehicle chases
  CA_DISABLE_CRUISE_IN_FRONT_DURING_BLOCK_DURING_VEHICLE_CHASE = 66,
  // Makes it more likely that the ped will continue targeting a target with blocked los for a few seconds
  CA_CAN_IGNORE_BLOCKED_LOS_WEIGHTING = 67,
  // Disables the react to buddy shot behaviour.
  CA_DISABLE_REACT_TO_BUDDY_SHOT = 68,
  // Prefer pathing using navmesh over road nodes
  CA_PREFER_NAVMESH_DURING_VEHICLE_CHASE = 69,
  // Ignore road edges when avoiding
  CA_ALLOWED_TO_AVOID_OFFROAD_DURING_VEHICLE_CHASE = 70,
  // Permits ped to charge a target outside the assigned defensive area.
  CA_PERMIT_CHARGE_BEYOND_DEFENSIVE_AREA = 71,
  // This ped will switch to an RPG if target is in a vehicle, otherwise will use alternate weapon.
  CA_USE_ROCKETS_AGAINST_VEHICLES_ONLY = 72,
  // Disables peds moving to a tactical point without clear los
  CA_DISABLE_TACTICAL_POINTS_WITHOUT_CLEAR_LOS = 73,
  // Disables pull alongside during vehicle chase
  CA_DISABLE_PULL_ALONGSIDE_DURING_VEHICLE_CHASE = 74,
  // If set on a ped, they will not flee when all random peds flee is set to TRUE (they are still able to flee due to other reasons)
  CA_DISABLE_ALL_RANDOMS_FLEE = 78,
  // This ped will send out a script DeadPedSeenEvent when they see a dead ped
  CA_WILL_GENERATE_DEAD_PED_SEEN_SCRIPT_EVENTS = 79,
  // This will use the receiving peds sense range rather than the range supplied to the communicate event
  CA_USE_MAX_SENSE_RANGE_WHEN_RECEIVING_EVENTS = 80,
  // When aiming from a vehicle the ped will only aim at targets on his side of the vehicle
  CA_RESTRICT_IN_VEHICLE_AIMING_TO_CURRENT_SIDE = 81,
  // LOS to the target is blocked we return to our default position and direction until we have LOS (no aiming)
  CA_USE_DEFAULT_BLOCKED_LOS_POSITION_AND_DIRECTION = 82,
  // LOS to the target is blocked we return to our default position and direction until we have LOS (no aiming)
  CA_REQUIRES_LOS_TO_AIM = 83,
  // Allow vehicles spawned infront of target facing away to enter cruise and wait to block approaching target
  CA_CAN_CRUISE_AND_BLOCK_IN_VEHICLE = 84,
  // Peds flying aircraft will prefer to target other aircraft over entities on the ground
  CA_PREFER_AIR_COMBAT_WHEN_IN_AIRCRAFT = 85,
  //Allow peds flying aircraft to use dog fighting behaviours
  CA_ALLOW_DOG_FIGHTING = 86,
  // This will make the weight of targets who aircraft vehicles be reduced greatly compared to targets on foot or in ground based vehicles
  CA_PREFER_NON_AIRCRAFT_TARGETS = 87,
  //When peds are tasked to go to combat, they keep searching for a known target for a while before forcing an unknown one
  CA_PREFER_KNOWN_TARGETS_WHEN_COMBAT_CLOSEST_TARGET = 88,
  // Only allow mounted weapons to fire if within the correct attack angle (default 25-degree cone). On a flag in order to keep exiting behaviour and only fix in specific cases.
  CA_FORCE_CHECK_ATTACK_ANGLE_FOR_MOUNTED_GUNS = 89,
  // Blocks the firing state for passenger-controlled mounted weapons. Existing flags CA_USE_VEHICLE_ATTACK and CA_USE_VEHICLE_ATTACK_IF_VEHICLE_HAS_MOUNTED_GUNS only work for drivers.
  CA_BLOCK_FIRE_FOR_VEHICLE_PASSENGER_MOUNTED_GUNS = 90 
};
```

---
### SetPedCombatMovement

`SET_PED_COMBAT_MOVEMENT` · hash `0x4D9CA1009AFBD057` · jhash `0x12E62F9E` · **Cliente**

```lua
SetPedCombatMovement(ped, combatMovement)
```
```c
void SET_PED_COMBAT_MOVEMENT(Ped ped, int combatMovement);
```

**Parámetros**

- `ped` (`Ped`)
- `combatMovement` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
0 - Stationary (Will just stand in place)  
1 - Defensive (Will try to find cover and very likely to blind fire)  
2 - Offensive (Will attempt to charge at enemy but take cover as well)  
3 - Suicidal Offensive (Will try to flank enemy in a suicidal attack)  
```

---
### SetPedCombatRange

`SET_PED_COMBAT_RANGE` · hash `0x3C606747B23E497B` · jhash `0x8818A959` · **Cliente**

```lua
SetPedCombatRange(ped, range)
```
```c
void SET_PED_COMBAT_RANGE(Ped ped, int range);
```

**Parámetros**

- `ped` (`Ped`): Ped index
- `range` (`int`): See `eCombatRange` enum.

**Devuelve:** `void`

**Descripción oficial:**

Define the scope within which the ped will engage in combat with the target.

```cpp
enum eCombatRange {
    CR_NEAR = 0, // keeps within 5-15m
    CR_MEDIUM = 1, // keeps within 7-30m
    CR_FAR = 2, // keeps within 15-40m
    CR_VERY_FAR = 3 // keeps within 22-45m
};
```

---
### SetPedComponentVariation

`SET_PED_COMPONENT_VARIATION` · hash `0x262B14F48D29DE80` · jhash `0xD4F7B05C` · **Cliente · también en el servidor (RPC)**

```lua
SetPedComponentVariation(ped, componentId, drawableId, textureId, paletteId)
```
```c
void SET_PED_COMPONENT_VARIATION(Ped ped, int componentId, int drawableId, int textureId, int paletteId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component that you want to set.
- `drawableId` (`int`): The drawable id that is going to be set. Refer to [GET_NUMBER_OF_PED_DRAWABLE_VARIATIONS](#getnumberofpeddrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_TEXTURE_VARIATIONS](#getnumberofpedtexturevariations).
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

---
### SetPedConfigFlag

`SET_PED_CONFIG_FLAG` · hash `0x1913FE4CBF41C463` · jhash `0x9CFBE10D` · **Cliente · también en el servidor (RPC)**

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

---
### SetPedCoordsKeepVehicle

`SET_PED_COORDS_KEEP_VEHICLE` · hash `0x9AFEFF481A85AB2E` · jhash `0xD66AE1D3` · **Cliente**

```lua
SetPedCoordsKeepVehicle(ped, posX, posY, posZ)
```
```c
void SET_PED_COORDS_KEEP_VEHICLE(Ped ped, float posX, float posY, float posZ);
```

**Parámetros**

- `ped` (`Ped`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
teleports ped to coords along with the vehicle ped is in  
```

---
### SetPedCoordsNoGang

`SET_PED_COORDS_NO_GANG` · hash `0x87052FE446E07247` · jhash `0x9561AD98` · **Cliente**

```lua
SetPedCoordsNoGang(ped, posX, posY, posZ)
```
```c
void SET_PED_COORDS_NO_GANG(Ped ped, float posX, float posY, float posZ);
```

**Parámetros**

- `ped` (`Ped`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `void`

---
### SetPedCoverClipsetOverride

`_SET_PED_COVER_CLIPSET_OVERRIDE` · hash `0x9DBA107B4937F809` · **Cliente**

```lua
SetPedCoverClipsetOverride(ped, p1)
```
```c
void _SET_PED_COVER_CLIPSET_OVERRIDE(Ped ped, char* p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Found in the b617d scripts:
PED::_9DBA107B4937F809(v_7, "trevor_heist_cover_2h");
SET_PED_MO*
```

**Nombres antiguos (alias):** `0x9DBA107B4937F809` (`N_0x9dba107b4937f809`)

---
### SetPedCowerHash

`SET_PED_COWER_HASH` · hash `0xA549131166868ED3` · jhash `0x16F30DF4` · **Cliente**

```lua
SetPedCowerHash(ped, p1)
```
```c
void SET_PED_COWER_HASH(Ped ped, char* p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1: Only "CODE_HUMAN_STAND_COWER" found in the b617d scripts.  
```

---
### SetPedDefaultComponentVariation

`SET_PED_DEFAULT_COMPONENT_VARIATION` · hash `0x45EEE61580806D63` · jhash `0xC866A984` · **Cliente · también en el servidor (RPC)**

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

---
### SetPedDefensiveAreaAttachedToPed

`SET_PED_DEFENSIVE_AREA_ATTACHED_TO_PED` · hash `0x4EF47FE21698A8B6` · jhash `0x74BDA7CE` · **Cliente**

```lua
SetPedDefensiveAreaAttachedToPed(ped, attachPed, p2, p3, p4, p5, p6, p7, p8, p9, p10)
```
```c
void SET_PED_DEFENSIVE_AREA_ATTACHED_TO_PED(Ped ped, Ped attachPed, float p2, float p3, float p4, float p5, float p6, float p7, float p8, BOOL p9, BOOL p10);
```

**Parámetros**

- `ped` (`Ped`)
- `attachPed` (`Ped`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`float`)
- `p8` (`float`)
- `p9` (`BOOL`)
- `p10` (`BOOL`)

**Devuelve:** `void`

---
### SetPedDefensiveAreaDirection

`SET_PED_DEFENSIVE_AREA_DIRECTION` · hash `0x413C6C763A4AFFAD` · jhash `0xB66B0C9A` · **Cliente**

```lua
SetPedDefensiveAreaDirection(ped, p1, p2, p3, p4)
```
```c
void SET_PED_DEFENSIVE_AREA_DIRECTION(Ped ped, float p1, float p2, float p3, BOOL p4);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`BOOL`)

**Devuelve:** `void`

---
### SetPedDefensiveSphereAttachedToPed

`SET_PED_DEFENSIVE_SPHERE_ATTACHED_TO_PED` · hash `0xF9B8F91AAD3B953E` · jhash `0x40638BDC` · **Cliente**

```lua
SetPedDefensiveSphereAttachedToPed(ped, target, xOffset, yOffset, zOffset, radius, p6)
```
```c
void SET_PED_DEFENSIVE_SPHERE_ATTACHED_TO_PED(Ped ped, Ped target, float xOffset, float yOffset, float zOffset, float radius, BOOL p6);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Ped`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `radius` (`float`)
- `p6` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF9B8F91AAD3B953E` (`N_0xf9b8f91aad3b953e`)

---
### SetPedDefensiveSphereAttachedToVehicle

`SET_PED_DEFENSIVE_SPHERE_ATTACHED_TO_VEHICLE` · hash `0xE4723DB6E736CCFF` · jhash `0x4763B2C6` · **Cliente**

```lua
SetPedDefensiveSphereAttachedToVehicle(ped, target, xOffset, yOffset, zOffset, radius, p6)
```
```c
void SET_PED_DEFENSIVE_SPHERE_ATTACHED_TO_VEHICLE(Ped ped, Vehicle target, float xOffset, float yOffset, float zOffset, float radius, BOOL p6);
```

**Parámetros**

- `ped` (`Ped`)
- `target` (`Vehicle`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `radius` (`float`)
- `p6` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE4723DB6E736CCFF` (`N_0xe4723db6e736ccff`)

---
### SetPedDensityMultiplierThisFrame

`SET_PED_DENSITY_MULTIPLIER_THIS_FRAME` · hash `0x95E3D6257B166CF2` · jhash `0x039C82BB` · **Cliente**

```lua
SetPedDensityMultiplierThisFrame(multiplier)
```
```c
void SET_PED_DENSITY_MULTIPLIER_THIS_FRAME(float multiplier);
```

**Parámetros**

- `multiplier` (`float`): Adjust from 0.0 (minimum, indicating no pedestrians in the street) to 1.0 (maximum, representing a normal amount of pedestrians on the street).

**Devuelve:** `void`

**Descripción oficial:**

**Usage:** Call this native every frame

**Ejemplo (lua):**

```lua
-- 0.0 means no peds, while 1.0 indicates the regular density of peds.
local pedsDensityFactor = 0.0 

Citizen.CreateThread(function()
   while true do
       SetPedDensityMultiplierThisFrame(pedsDensityFactor)
       Citizen.Wait(0)    
   end
end)
```

**Ejemplo (js):**

```js
// 0.0 means no peds, while 1.0 indicates the regular density of peds.
const pedsDensityFactor = 0.0;

setTick(() => {
    SetPedDensityMultiplierThisFrame(pedsDensityFactor);  
});
```

---
### SetPedDesiredHeading

`SET_PED_DESIRED_HEADING` · hash `0xAA5A7ECE2AA8FE70` · jhash `0x961458F9` · **Cliente**

```lua
SetPedDesiredHeading(ped, heading)
```
```c
void SET_PED_DESIRED_HEADING(Ped ped, float heading);
```

**Parámetros**

- `ped` (`Ped`)
- `heading` (`float`)

**Devuelve:** `void`

---
### SetPedDiesInSinkingVehicle

`SET_PED_DIES_IN_SINKING_VEHICLE` · hash `0xD718A22995E2B4BC` · jhash `0x8D4D9ABB` · **Cliente**

```lua
SetPedDiesInSinkingVehicle(ped, toggle)
```
```c
void SET_PED_DIES_IN_SINKING_VEHICLE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedDiesInVehicle

`SET_PED_DIES_IN_VEHICLE` · hash `0x2A30922C90C9B42C` · jhash `0x6FE1E440` · **Cliente**

```lua
SetPedDiesInVehicle(ped, toggle)
```
```c
void SET_PED_DIES_IN_VEHICLE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedDiesInWater

`SET_PED_DIES_IN_WATER` · hash `0x56CEF0AC79073BDE` · jhash `0x604C872B` · **Cliente**

```lua
SetPedDiesInWater(ped, toggle)
```
```c
void SET_PED_DIES_IN_WATER(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedDiesInstantlyInWater

`SET_PED_DIES_INSTANTLY_IN_WATER` · hash `0xEEB64139BA29A7CF` · jhash `0xFE2554FC` · **Cliente**

```lua
SetPedDiesInstantlyInWater(ped, toggle)
```
```c
void SET_PED_DIES_INSTANTLY_IN_WATER(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedDiesWhenInjured

`SET_PED_DIES_WHEN_INJURED` · hash `0x5BA7919BED300023` · jhash `0xE94E24D4` · **Cliente**

```lua
SetPedDiesWhenInjured(ped, toggle)
```
```c
void SET_PED_DIES_WHEN_INJURED(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedDriveByClipsetOverride

`SET_PED_DRIVE_BY_CLIPSET_OVERRIDE` · hash `0xED34AB6C5CB36520` · jhash `0xD4C73595` · **Cliente**

```lua
SetPedDriveByClipsetOverride(ped, clipset)
```
```c
void SET_PED_DRIVE_BY_CLIPSET_OVERRIDE(Ped ped, char* clipset);
```

**Parámetros**

- `ped` (`Ped`)
- `clipset` (`char*`)

**Devuelve:** `void`

---
### SetPedDucking

`SET_PED_DUCKING` · hash `0x030983CA930B692D` · jhash `0xB90353D7` · **Cliente**

```lua
SetPedDucking(ped, toggle)
```
```c
void SET_PED_DUCKING(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This is the SET_CHAR_DUCKING from GTA IV, that makes Peds duck. This function does nothing in GTA V. It cannot set the ped as ducking in vehicles, and IS_PED_DUCKING will always return false.  
```

---
### SetPedEmissiveIntensity

`_SET_PED_EMISSIVE_INTENSITY` · hash `0x4E90D746056E273D` · **Cliente**

```lua
SetPedEmissiveIntensity(ped, intensity)
```
```c
void _SET_PED_EMISSIVE_INTENSITY(Ped ped, float intensity);
```

**Parámetros**

- `ped` (`Ped`): The ped to set the glow intensity on.
- `intensity` (`float`): The glow intensity, value between `0.0` and `1.0`.

**Devuelve:** `void`

**Descripción oficial:**

This native sets the glow intensity of illuminated clothing items.

This native does **NOT** need to be executed every tick.
This native is **NOT** synced with other connected players, you will have to set the opacity on the ped on all clients individually.

Glow intensity is a value between `0.0` and `1.0`.

In some older decompiled scripts this is known as `_SET_PED_REFLECTION_INTENSITY`.
Since there's no joaat hash for this, I find `_SET_PED_ILLUMINATED_CLOTHING_GLOW_INTENSITY` more descriptive than `_SET_PED_REFLECTION_INTENSITY`.

Use [`GetPedIlluminatedClothingGlowIntensity`](#getpedemissiveintensity) to get the illuminated clothing glow intensity of a specific ped.

Intensity: `1.0`:
![](https://www.vespura.com/hi/i/2018-11-13\_17-03\_c2e23\_229.png)

Intensity: `0.0`:
![](https://www.vespura.com/hi/i/2018-11-13\_17-03\_35c33\_230.png)

**Examples code result**:
![](https://www.vespura.com/hi/i/2018-11-13\_17-11\_10199\_232.gif)

(Direct link if embed doesn't work: [here](https://www.vespura.com/hi/i/2018-11-13\_17-11\_10199\_232.gif))

**Nombres antiguos (alias):** `0x4E90D746056E273D` (`N_0x4e90d746056e273d`), `_SET_PED_ILLUMINATED_CLOTHING_GLOW_INTENSITY` (`SetPedIlluminatedClothingGlowIntensity`)

**Ejemplo (lua):**

```lua
CreateThread(function()
    local glowIntensity = 0.0
    local reverse = false
    while true do
        Wait(100)
        SetPedIlluminatedClothingGlowIntensity(PlayerPedId(), glowIntensity)
        if reverse then
            glowIntensity = glowIntensity - 0.05
            if glowIntensity < 0.0 then
                reverse = false
                glowIntensity = 0.0
            end
        else
            glowIntensity = glowIntensity + 0.05
            if glowIntensity > 1.0 then
                reverse = true
                glowIntensity = 1.0
            end
        end
    end
end)
```

**Ejemplo (cs):**

```cs
private float intensity = 0.0f;
private bool reverse = false;

// Execute this function every tick (for example: Tick += OnTickFunction; in your constructor )
private async Task OnTickFunction()
{
    await Delay(100);
    SetPedIlluminatedClothingGlowIntensity(PlayerPedId(), intensity);
    if (reverse)
    {
        intensity -= 0.05f;
        if (intensity < 0.0f)
        {
            intensity = 0.0f;
            reverse = false;
        }
    }
    else
    {
        intensity += 0.05f;
        if (intensity > 1.0f)
        {
            intensity = 1.0f;
            reverse = true;
        }
    }
}
```

---
### SetPedEnableWeaponBlocking

`SET_PED_ENABLE_WEAPON_BLOCKING` · hash `0x97A790315D3831FD` · jhash `0x4CAD1A4A` · **Cliente**

```lua
SetPedEnableWeaponBlocking(ped, toggle)
```
```c
void SET_PED_ENABLE_WEAPON_BLOCKING(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedEnveffColorModulator

`SET_PED_ENVEFF_COLOR_MODULATOR` · hash `0xD69411AA0CEBF9E9` · jhash `0x87A0C174` · **Cliente**

```lua
SetPedEnveffColorModulator(ped, r, g, b)
```
```c
void SET_PED_ENVEFF_COLOR_MODULATOR(Ped ped, int r, int g, int b);
```

**Parámetros**

- `ped` (`Ped`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Something related to the environmental effects natives.
In the "agency_heist3b" script, p1 - p3 are always under 100 - usually they are {87, 81, 68}. If SET_PED_ENVEFF_SCALE is set to 0.65 (instead of the usual 1.0), they use {74, 69, 60}
```

**Nombres antiguos (alias):** `0xD69411AA0CEBF9E9` (`N_0xd69411aa0cebf9e9`)

---
### SetPedEnveffScale

`SET_PED_ENVEFF_SCALE` · hash `0xBF29516833893561` · jhash `0xFC1CFC27` · **Cliente**

```lua
SetPedEnveffScale(ped, value)
```
```c
void SET_PED_ENVEFF_SCALE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Values look to be between 0.0 and 1.0  
From decompiled scripts: 0.0, 0.6, 0.65, 0.8, 1.0  
You are correct, just looked in IDA it breaks from the function if it's less than 0.0f or greater than 1.0f.  
```

---
### SetPedEyeColor

`_SET_PED_EYE_COLOR` · hash `0x50B56988B170AFDF` · **Cliente · también en el servidor (RPC)**

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

---
### SetPedFaceFeature

`_SET_PED_FACE_FEATURE` · hash `0x71A5C1DBA060049E` · **Cliente · también en el servidor (RPC)**

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

You may need to call [`SetPedHeadBlendData`](../cfx/servidor.md#setpedheadblenddata) prior to calling this native in order for it to work.

---
### SetPedFiringPattern

`SET_PED_FIRING_PATTERN` · hash `0x9AC577F5A12AD8A9` · jhash `0xB4629D66` · **Cliente**

```lua
SetPedFiringPattern(ped, patternHash)
```
```c
void SET_PED_FIRING_PATTERN(Ped ped, Hash patternHash);
```

**Parámetros**

- `ped` (`Ped`)
- `patternHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
FIRING_PATTERN_BURST_FIRE = 0xD6FF6D61 ( 1073727030 )  
FIRING_PATTERN_BURST_FIRE_IN_COVER = 0x026321F1 ( 40051185 )  
FIRING_PATTERN_BURST_FIRE_DRIVEBY = 0xD31265F2 ( -753768974 )  
FIRING_PATTERN_FROM_GROUND = 0x2264E5D6 ( 577037782 )  
FIRING_PATTERN_DELAY_FIRE_BY_ONE_SEC = 0x7A845691 ( 2055493265 )  
FIRING_PATTERN_FULL_AUTO = 0xC6EE6B4C ( -957453492 )  
FIRING_PATTERN_SINGLE_SHOT = 0x5D60E4E0 ( 1566631136 )  
FIRING_PATTERN_BURST_FIRE_PISTOL = 0xA018DB8A ( -1608983670 )  
FIRING_PATTERN_BURST_FIRE_SMG = 0xD10DADEE ( 1863348768 )  
FIRING_PATTERN_BURST_FIRE_RIFLE = 0x9C74B406 ( -1670073338 )  
FIRING_PATTERN_BURST_FIRE_MG = 0xB573C5B4 ( -1250703948 )  
FIRING_PATTERN_BURST_FIRE_PUMPSHOTGUN = 0x00BAC39B ( 12239771 )  
FIRING_PATTERN_BURST_FIRE_HELI = 0x914E786F ( -1857128337 )  
FIRING_PATTERN_BURST_FIRE_MICRO = 0x42EF03FD ( 1122960381 )  
FIRING_PATTERN_SHORT_BURSTS = 0x1A92D7DF ( 445831135 )  
FIRING_PATTERN_SLOW_FIRE_TANK = 0xE2CA3A71 ( -490063247 )  
if anyone is interested firing pattern info: pastebin.com/Px036isB  
```

---
### SetPedFleeAttributes

`SET_PED_FLEE_ATTRIBUTES` · hash `0x70A2D1137C8ED7C9` · jhash `0xA717A875` · **Cliente**

```lua
SetPedFleeAttributes(ped, attributeFlags, enable)
```
```c
void SET_PED_FLEE_ATTRIBUTES(Ped ped, int attributeFlags, BOOL enable);
```

**Parámetros**

- `ped` (`Ped`)
- `attributeFlags` (`int`)
- `enable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
bit 15 (0x8000) = force cower
```

---
### SetPedGeneratesDeadBodyEvents

`SET_PED_GENERATES_DEAD_BODY_EVENTS` · hash `0x7FB17BA2E7DECA5B` · jhash `0xE9B97A2B` · **Cliente**

```lua
SetPedGeneratesDeadBodyEvents(ped, toggle)
```
```c
void SET_PED_GENERATES_DEAD_BODY_EVENTS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedGestureGroup

`SET_PED_GESTURE_GROUP` · hash `0xDDF803377F94AAA8` · jhash `0x170DA109` · **Cliente**

```lua
SetPedGestureGroup(ped, animGroupGesture)
```
```c
void SET_PED_GESTURE_GROUP(Ped ped, char* animGroupGesture);
```

**Parámetros**

- `ped` (`Ped`)
- `animGroupGesture` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
From the scripts:  
PED::SET_PED_GESTURE_GROUP(PLAYER::PLAYER_PED_ID(),  
"ANIM_GROUP_GESTURE_MISS_FRA0");  
PED::SET_PED_GESTURE_GROUP(PLAYER::PLAYER_PED_ID(),  
"ANIM_GROUP_GESTURE_MISS_DocksSetup1");  
```

---
### SetPedGetOutUpsideDownVehicle

`SET_PED_GET_OUT_UPSIDE_DOWN_VEHICLE` · hash `0xBC0ED94165A48BC2` · jhash `0x89AD49FF` · **Cliente**

```lua
SetPedGetOutUpsideDownVehicle(ped, toggle)
```
```c
void SET_PED_GET_OUT_UPSIDE_DOWN_VEHICLE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedGravity

`SET_PED_GRAVITY` · hash `0x9FF447B6B6AD960A` · jhash `0x3CA16652` · **Cliente**

```lua
SetPedGravity(ped, toggle)
```
```c
void SET_PED_GRAVITY(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
enable or disable the gravity of a ped  
Examples:  
PED::SET_PED_GRAVITY(PLAYER::PLAYER_PED_ID(), 0x00000001);  
PED::SET_PED_GRAVITY(Local_289[iVar0 /*20*/], 0x00000001);  
```

---
### SetPedGroupMemberPassengerIndex

`SET_PED_GROUP_MEMBER_PASSENGER_INDEX` · hash `0x0BDDB8D9EC6BCF3C` · jhash `0x2AB3670B` · **Cliente**

```lua
SetPedGroupMemberPassengerIndex(ped, index)
```
```c
void SET_PED_GROUP_MEMBER_PASSENGER_INDEX(Ped ped, int index);
```

**Parámetros**

- `ped` (`Ped`)
- `index` (`int`)

**Devuelve:** `void`

---
### SetPedHairTint

`SET_PED_HAIR_TINT` · hash `0x4CFFC65454C93A49` · **Cliente**

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

**Nombres antiguos (alias):** `_SET_PED_HAIR_COLOR` (`SetPedHairColor`)

---
### SetPedHeadBlendData

`SET_PED_HEAD_BLEND_DATA` · hash `0x9414E18B9434C2FE` · jhash `0x60746B88` · **Cliente · también en el servidor (RPC)**

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

*   [`SetPedHairColor`](../cfx/servidor.md#setpedhairtint)
*   [`SetPedHeadOverlayColor`](../cfx/servidor.md#setpedheadoverlaycolor)
*   [`SetPedHeadOverlay`](../cfx/servidor.md#setpedheadoverlay)
*   [`SetPedFaceFeature`](../cfx/servidor.md#setpedfacefeature)

**Ejemplo (lua):**

```lua
-- Unfortunately, there's no clear way of getting the head blend data in lua out of the box, but there are wrappers:
-- https://forum.cfx.re/t/small-c-export-event-wrapper-for-getpedheadblenddata/214611
SetPedHeadBlendData(PlayerPedId(), 0, 0, 0, 0, 0, 0, 0, 0, 0, false)
```

---
### SetPedHeadOverlay

`SET_PED_HEAD_OVERLAY` · hash `0x48F44967FA05CC1E` · jhash `0xD28DBA90` · **Cliente · también en el servidor (RPC)**

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

You may need to call [`SetPedHeadBlendData`](../cfx/servidor.md#setpedheadblenddata) prior to calling this native in order for it to work.

---
### SetPedHeadOverlayColor

`_SET_PED_HEAD_OVERLAY_COLOR` · hash `0x497BF74A7B9CB952` · **Cliente · también en el servidor (RPC)**

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

You may need to call [`SetPedHeadBlendData`](../cfx/servidor.md#setpedheadblenddata) prior to calling this native in order for it to work.

---
### SetPedHearingRange

`SET_PED_HEARING_RANGE` · hash `0x33A8F7F7D5F7F33C` · jhash `0xB32087E0` · **Cliente**

```lua
SetPedHearingRange(ped, value)
```
```c
void SET_PED_HEARING_RANGE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedHeatscaleOverride

`SET_PED_HEATSCALE_OVERRIDE` · hash `0xC1F6EBF9A3D55538` · jhash `0xEF9142DB` · **Cliente**

```lua
SetPedHeatscaleOverride(ped, heatScale)
```
```c
void SET_PED_HEATSCALE_OVERRIDE(Ped ped, float heatScale);
```

**Parámetros**

- `ped` (`Ped`)
- `heatScale` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC1F6EBF9A3D55538` (`N_0xc1f6ebf9a3d55538`)

---
### SetPedHelmet

`SET_PED_HELMET` · hash `0x560A43136EB58105` · jhash `0xED366E53` · **Cliente**

```lua
SetPedHelmet(ped, bEnable)
```
```c
void SET_PED_HELMET(Ped ped, BOOL bEnable);
```

**Parámetros**

- `ped` (`Ped`): Ped index.
- `bEnable` (`BOOL`): Boolean value that indicates whether the helmet should be worn or not.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether a pedestrian should wear a helmet.

---
### SetPedHelmetFlag

`SET_PED_HELMET_FLAG` · hash `0xC0E78D5C2CE3EB25` · jhash `0x12677780` · **Cliente**

```lua
SetPedHelmetFlag(ped, helmetFlag)
```
```c
void SET_PED_HELMET_FLAG(Ped ped, int helmetFlag);
```

**Parámetros**

- `ped` (`Ped`)
- `helmetFlag` (`int`)

**Devuelve:** `void`

---
### SetPedHelmetPropIndex

`SET_PED_HELMET_PROP_INDEX` · hash `0x26D83693ED99291C` · jhash `0xA316D13F` · **Cliente**

```lua
SetPedHelmetPropIndex(ped, propIndex)
```
```c
void SET_PED_HELMET_PROP_INDEX(Ped ped, int propIndex);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `propIndex` (`int`): The prop index to set the helmet to. Refer to [SET_PED_PROP_INDEX](../cfx/servidor.md#setpedpropindex).

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 3: BOOL p2
```

---
### SetPedHelmetTextureIndex

`SET_PED_HELMET_TEXTURE_INDEX` · hash `0xF1550C4BD22582E2` · jhash `0x5F6C3328` · **Cliente**

```lua
SetPedHelmetTextureIndex(ped, textureIndex)
```
```c
void SET_PED_HELMET_TEXTURE_INDEX(Ped ped, int textureIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `textureIndex` (`int`)

**Devuelve:** `void`

---
### SetPedHelmetUnk

`_SET_PED_HELMET_UNK` · hash `0x3F7325574E41B44D` · **Cliente**

```lua
SetPedHelmetUnk(ped, p1, p2, p3)
```
```c
void _SET_PED_HELMET_UNK(Ped ped, BOOL p1, int p2, int p3);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `p2` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x3F7325574E41B44D` (`N_0x3f7325574e41b44d`)

---
### SetPedHighlyPerceptive

`SET_PED_HIGHLY_PERCEPTIVE` · hash `0x52D59AB61DDC05DD` · jhash `0x9A2180FF` · **Cliente**

```lua
SetPedHighlyPerceptive(ped, toggle)
```
```c
void SET_PED_HIGHLY_PERCEPTIVE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x52D59AB61DDC05DD` (`N_0x52d59ab61ddc05dd`)

---
### SetPedIdRange

`SET_PED_ID_RANGE` · hash `0xF107E836A70DCE05` · jhash `0xEF3B4ED9` · **Cliente**

```lua
SetPedIdRange(ped, value)
```
```c
void SET_PED_ID_RANGE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedInVehicleContext

`SET_PED_IN_VEHICLE_CONTEXT` · hash `0x530071295899A8C6` · jhash `0x27F25C0E` · **Cliente**

```lua
SetPedInVehicleContext(ped, context)
```
```c
void SET_PED_IN_VEHICLE_CONTEXT(Ped ped, Hash context);
```

**Parámetros**

- `ped` (`Ped`)
- `context` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
PED::SET_PED_IN_VEHICLE_CONTEXT(l_128, MISC::GET_HASH_KEY("MINI_PROSTITUTE_LOW_PASSENGER"));
PED::SET_PED_IN_VEHICLE_CONTEXT(l_128, MISC::GET_HASH_KEY("MINI_PROSTITUTE_LOW_RESTRICTED_PASSENGER"));
PED::SET_PED_IN_VEHICLE_CONTEXT(l_3212, MISC::GET_HASH_KEY("MISS_FAMILY1_JIMMY_SIT"));
PED::SET_PED_IN_VEHICLE_CONTEXT(l_3212, MISC::GET_HASH_KEY("MISS_FAMILY1_JIMMY_SIT_REAR"));
PED::SET_PED_IN_VEHICLE_CONTEXT(l_95, MISC::GET_HASH_KEY("MISS_FAMILY2_JIMMY_BICYCLE"));
PED::SET_PED_IN_VEHICLE_CONTEXT(num3, MISC::GET_HASH_KEY("MISSFBI2_MICHAEL_DRIVEBY"));
PED::SET_PED_IN_VEHICLE_CONTEXT(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("MISS_ARMENIAN3_FRANKLIN_TENSE"));
PED::SET_PED_IN_VEHICLE_CONTEXT(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("MISSFBI5_TREVOR_DRIVING"));
```

---
### SetPedIncreasedAvoidanceRadius

`SET_PED_INCREASED_AVOIDANCE_RADIUS` · hash `0x570389D1C3DE3C6B` · jhash `0x59C52BE6` · **Cliente**

```lua
SetPedIncreasedAvoidanceRadius(ped)
```
```c
void SET_PED_INCREASED_AVOIDANCE_RADIUS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x570389D1C3DE3C6B` (`N_0x570389d1c3de3c6b`)

---
### SetPedIntoVehicle

`SET_PED_INTO_VEHICLE` · hash `0xF75B0D629E1C063D` · jhash `0x07500C79` · **Cliente · también en el servidor (RPC)**

```lua
SetPedIntoVehicle(ped, vehicle, seatIndex)
```
```c
void SET_PED_INTO_VEHICLE(Ped ped, Vehicle vehicle, int seatIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `vehicle` (`Vehicle`)
- `seatIndex` (`int`): See eSeatPosition declared in [`IS_VEHICLE_SEAT_FREE`](VEHICLE-1.md#isvehicleseatfree). -2 for the first available seat.

**Devuelve:** `void`

---
### SetPedKeepTask

`SET_PED_KEEP_TASK` · hash `0x971D38760FBC02EF` · jhash `0xA7EC79CE` · **Cliente**

```lua
SetPedKeepTask(ped, toggle)
```
```c
void SET_PED_KEEP_TASK(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedLegIkMode

`SET_PED_LEG_IK_MODE` · hash `0xC396F5B86FF9FEBD` · jhash `0xFDDB042E` · **Cliente**

```lua
SetPedLegIkMode(ped, mode)
```
```c
void SET_PED_LEG_IK_MODE(Ped ped, int mode);
```

**Parámetros**

- `ped` (`Ped`)
- `mode` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
"IK" stands for "Inverse kinematics." I assume this has something to do with how the ped uses his legs to balance. In the scripts, the second parameter is always an int with a value of 2, 0, or sometimes 1  
```

---
### SetPedLodMultiplier

`SET_PED_LOD_MULTIPLIER` · hash `0xDC2C5C242AAC342B` · jhash `0x1D2B5C70` · **Cliente**

```lua
SetPedLodMultiplier(ped, multiplier)
```
```c
void SET_PED_LOD_MULTIPLIER(Ped ped, float multiplier);
```

**Parámetros**

- `ped` (`Ped`)
- `multiplier` (`float`)

**Devuelve:** `void`

---
### SetPedMaxHealth

`SET_PED_MAX_HEALTH` · hash `0xF5F6378C4F3419D3` · jhash `0x5533F60B` · **Cliente**

```lua
SetPedMaxHealth(ped, value)
```
```c
void SET_PED_MAX_HEALTH(Ped ped, int value);
```

**Parámetros**

- `ped` (`Ped`): The ped handle we're setting this for.
- `value` (`int`): The new max health.

**Devuelve:** `void`

---
### SetPedMaxMoveBlendRatio

`SET_PED_MAX_MOVE_BLEND_RATIO` · hash `0x433083750C5E064A` · jhash `0xEAD0269A` · **Cliente**

```lua
SetPedMaxMoveBlendRatio(ped, value)
```
```c
void SET_PED_MAX_MOVE_BLEND_RATIO(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedMaxTimeInWater

`SET_PED_MAX_TIME_IN_WATER` · hash `0x43C851690662113D` · jhash `0xFE0A106B` · **Cliente**

```lua
SetPedMaxTimeInWater(ped, value)
```
```c
void SET_PED_MAX_TIME_IN_WATER(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedMaxTimeUnderwater

`SET_PED_MAX_TIME_UNDERWATER` · hash `0x6BA428C528D9E522` · jhash `0x082EF240` · **Cliente**

```lua
SetPedMaxTimeUnderwater(ped, value)
```
```c
void SET_PED_MAX_TIME_UNDERWATER(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`): Ped id.
- `value` (`float`): Time in seconds. Maximum is 50.0, any value above will be changed to 50.0.

**Devuelve:** `void`

**Descripción oficial:**

Set the maximum time a ped can stay underwater. Maximum seems to be 50 seconds.

---
### SetPedMinGroundTimeForStungun

`SET_PED_MIN_GROUND_TIME_FOR_STUNGUN` · hash `0xFA0675AB151073FA` · jhash `0x2F0D0973` · **Cliente**

```lua
SetPedMinGroundTimeForStungun(ped, minTimeInMs)
```
```c
void SET_PED_MIN_GROUND_TIME_FOR_STUNGUN(Ped ped, int minTimeInMs);
```

**Parámetros**

- `ped` (`Ped`): The ped to set the min ground time for
- `minTimeInMs` (`int`): The minimum time the stun should last in milliseconds.

**Devuelve:** `void`

**Descripción oficial:**

Overwrites the minimum time the ped will stay on the ground for after being stunned. Setting this while the ped is stunned will not alter the duration of the current stun but will still effect future stuns.

Passing -1 into the second parameter `minTimeInMs` will reset the modifier, making it use the weapons original `DamageTime` as the stun duration (see `update/update.rpf/common/data/ai/weapons.meta`)

**NOTE**: Unlike what the native name implies, this works on any weapon that has its `DamageType` in the `weapons.meta` set to `ELECTRIC`.

**Ejemplo (lua):**

```lua
-- This sets the minimum stun ground time for the player's ped to 10 seconds (and re-applies it if the player's ped changes)

local currentPed = 0
CreateThread(function()
    while true do
        local playerPed = PlayerPedId()

        -- Checks if the player ped has changed
        if currentPed ~= playerPed then
            currentPed = playerPed

            -- Sets the minimum stun ground time to 10 seconds
            SetPedMinGroundTimeForStungun(currentPed, 10000)
        end

        Wait(1000)
    end
end)
```

**Ejemplo (js):**

```js
// This sets the minimum stun ground time for the player's ped to 10 seconds (and re-applies it if the player's ped changes)

let currentPed = 0;

setInterval(() => {
    const playerPed = PlayerPedId();

    // Checks if the player ped has changed
    if (currentPed !== playerPed) {
        currentPed = playerPed;

        // Sets the minimum stun ground time to 10 seconds
        SetPedMinGroundTimeForStungun(currentPed, 10000);
    };
}, 1000);
```

**Ejemplo (cs):**

```cs
// This sets the minimum stun ground time for the player's ped to 10 seconds (and re-applies it if the player's ped changes)

using static CitizenFX.Core.Native.API;
// ...

private int currentPed = 0;

public Main() 
{
    Tick += OnTick;
}

private async Task OnTick()
{
    int playerPed = PlayerPedId();

    // Checks if the player ped has changed
    if (currentPed != playerPed)
    {
        currentPed = playerPed;

        // Sets the minimum stun ground time to 10 seconds
        SetPedMinGroundTimeForStungun(currentPed, 10000);
    }

    await BaseScript.Delay(1000);
}
```

---
### SetPedMinMoveBlendRatio

`SET_PED_MIN_MOVE_BLEND_RATIO` · hash `0x01A898D26E2333DD` · jhash `0x383EC364` · **Cliente**

```lua
SetPedMinMoveBlendRatio(ped, value)
```
```c
void SET_PED_MIN_MOVE_BLEND_RATIO(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedModelIsSuppressed

`SET_PED_MODEL_IS_SUPPRESSED` · hash `0xE163A4BCE4DE6F11` · jhash `0x7820CA43` · **Cliente**

```lua
SetPedModelIsSuppressed(model, toggle)
```
```c
void SET_PED_MODEL_IS_SUPPRESSED(Hash model, BOOL toggle);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedMoney

`SET_PED_MONEY` · hash `0xA9C8960E8684C1B5` · jhash `0x40D90BF2` · **Cliente**

```lua
SetPedMoney(ped, amount)
```
```c
void SET_PED_MONEY(Ped ped, int amount);
```

**Parámetros**

- `ped` (`Ped`)
- `amount` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Maximum possible amount of money on MP is 2000. ~JX  
-----------------------------------------------------------------------------  
Maximum amount that a ped can theoretically have is 65535 (0xFFFF) since the amount is stored as an unsigned short (uint16_t) value.  
```

---
### SetPedMotionBlur

`SET_PED_MOTION_BLUR` · hash `0x0A986918B102B448` · jhash `0xA211A128` · **Cliente**

```lua
SetPedMotionBlur(ped, toggle)
```
```c
void SET_PED_MOTION_BLUR(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedMoveAnimsBlendOut

`SET_PED_MOVE_ANIMS_BLEND_OUT` · hash `0x9E8C908F41584ECD` · jhash `0x20E01957` · **Cliente**

```lua
SetPedMoveAnimsBlendOut(ped)
```
```c
void SET_PED_MOVE_ANIMS_BLEND_OUT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### SetPedMoveRateOverride

`SET_PED_MOVE_RATE_OVERRIDE` · hash `0x085BF80FA50A39D1` · jhash `0x900008C6` · **Cliente**

```lua
SetPedMoveRateOverride(ped, value)
```
```c
void SET_PED_MOVE_RATE_OVERRIDE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Min: 0.00  
Max: 10.00  
Can be used in combo with fast run cheat.  
When value is set to 10.00:  
Sprinting without fast run cheat: 66 m/s  
Sprinting with fast run cheat: 77 m/s  
Needs to be looped!  
Note: According to IDA for the Xbox360 xex, when they check bgt they seem to have the min to 0.0f, but the max set to 1.15f not 10.0f.  
```

---
### SetPedMovementClipset

`SET_PED_MOVEMENT_CLIPSET` · hash `0xAF8A94EDE7712BEF` · jhash `0xA817CDEB` · **Cliente**

```lua
SetPedMovementClipset(ped, clipSet, transitionSpeed)
```
```c
void SET_PED_MOVEMENT_CLIPSET(Ped ped, char* clipSet, float transitionSpeed);
```

**Parámetros**

- `ped` (`Ped`)
- `clipSet` (`char*`)
- `transitionSpeed` (`float`): time in seconds it takes to transition from one movement clipset to another.

**Devuelve:** `void`

**Descripción oficial:**

```
List of movement clipsets:
Thanks to elsewhat for list.
 "ANIM_GROUP_MOVE_BALLISTIC"
 "ANIM_GROUP_MOVE_LEMAR_ALLEY"
 "clipset@move@trash_fast_turn"
 "FEMALE_FAST_RUNNER"
 "missfbi4prepp1_garbageman"
 "move_characters@franklin@fire"
 "move_characters@Jimmy@slow@"
 "move_characters@michael@fire"
 "move_f@flee@a"
 "move_f@scared"
 "move_f@sexy@a"
 "move_heist_lester"
 "move_injured_generic"
 "move_lester_CaneUp"
 "move_m@bag"
 "MOVE_M@BAIL_BOND_NOT_TAZERED"
 "MOVE_M@BAIL_BOND_TAZERED"
 "move_m@brave"
 "move_m@casual@d"
 "move_m@drunk@moderatedrunk"
 "MOVE_M@DRUNK@MODERATEDRUNK"
 "MOVE_M@DRUNK@MODERATEDRUNK_HEAD_UP"
 "MOVE_M@DRUNK@SLIGHTLYDRUNK"
 "MOVE_M@DRUNK@VERYDRUNK"
 "move_m@fire"
 "move_m@gangster@var_e"
 "move_m@gangster@var_f"
 "move_m@gangster@var_i"
 "move_m@JOG@"
 "MOVE_M@PRISON_GAURD"
 "MOVE_P_M_ONE"
 "MOVE_P_M_ONE_BRIEFCASE"
 "move_p_m_zero_janitor"
 "move_p_m_zero_slow"
 "move_ped_bucket"
 "move_ped_crouched"
 "move_ped_mop"
 "MOVE_M@FEMME@"
 "MOVE_F@FEMME@"
 "MOVE_M@GANGSTER@NG"
 "MOVE_F@GANGSTER@NG"
 "MOVE_M@POSH@"
 "MOVE_F@POSH@"
 "MOVE_M@TOUGH_GUY@"
 "MOVE_F@TOUGH_GUY@"
~ NotCrunchyTaco
```

---
### SetPedNameDebug

`SET_PED_NAME_DEBUG` · hash `0x98EFA132A4117BE1` · jhash `0x20D6273E` · **Cliente**

```lua
SetPedNameDebug(ped, name)
```
```c
void SET_PED_NAME_DEBUG(Ped ped, char* name);
```

**Parámetros**

- `ped` (`Ped`)
- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
*untested but char *name could also be a hash for a localized string  
```

---
### SetPedNeverLeavesGroup

`SET_PED_NEVER_LEAVES_GROUP` · hash `0x3DBFC55D5C9BB447` · jhash `0x0E038813` · **Cliente**

```lua
SetPedNeverLeavesGroup(ped, toggle)
```
```c
void SET_PED_NEVER_LEAVES_GROUP(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedNonCreationArea

`SET_PED_NON_CREATION_AREA` · hash `0xEE01041D559983EA` · jhash `0x7A97283F` · **Cliente**

```lua
SetPedNonCreationArea(x1, y1, z1, x2, y2, z2)
```
```c
void SET_PED_NON_CREATION_AREA(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
The distance between these points, is the diagonal of a box (remember it's 3D).  
```

---
### SetPedPanicExitScenario

`SET_PED_PANIC_EXIT_SCENARIO` · hash `0xFE07FF6495D52E2A` · jhash `0x59DE73AC` · **Cliente**

```lua
local retval = SetPedPanicExitScenario(ped, x, y, z)
```
```c
Any SET_PED_PANIC_EXIT_SCENARIO(Ped ped, float x, float y, float z);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xFE07FF6495D52E2A` (`N_0xfe07ff6495d52e2a`)

---
### SetPedParachuteTintIndex

`SET_PED_PARACHUTE_TINT_INDEX` · hash `0x333FC8DB079B7186` · jhash `0x5AEFEC3A` · **Cliente**

```lua
SetPedParachuteTintIndex(ped, tintIndex)
```
```c
void SET_PED_PARACHUTE_TINT_INDEX(Ped ped, int tintIndex);
```

**Parámetros**

- `ped` (`Ped`)
- `tintIndex` (`int`)

**Devuelve:** `void`

---
### SetPedPhonePaletteIdx

`SET_PED_PHONE_PALETTE_IDX` · hash `0x83A169EABCDB10A2` · **Cliente**

```lua
SetPedPhonePaletteIdx(ped, index)
```
```c
void SET_PED_PHONE_PALETTE_IDX(Ped ped, int index);
```

**Parámetros**

- `ped` (`Ped`): The Ped whose phone palette is to be set.
- `index` (`int`): The index of the color palette to apply to the ped's phone.

**Devuelve:** `void`

**Descripción oficial:**

Sets the palette index of a ped's phone.

| Value | Color      |
| :---: | :-----:    |
|  `0`  | Light Blue |
|  `1`  | Green      |
|  `2`  | Red        |
|  `3`  | Orange     |
|  `4`  | Grey       |
|  `5`  | Purple     |
|  `6`  | Pink       |

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x83A169EABCDB10A2` (`N_0x83a169eabcdb10a2`)

**Ejemplo (lua):**

```lua
-- Define a table with color names mapped to their corresponding palette indices for phone colors
local PhoneColors = {
    Blue = 0,
    Green = 1,
    Red = 2,
    Orange = 3,
    Grey = 4,
    Purple = 5,
    Pink = 6
}

-- Retrieve the current player ped
local playerPed = PlayerPedId()

-- Set the phone color of the player's ped to Green using the corresponding index from the PhoneColors table
SetPedPhonePaletteIdx(playerPed, PhoneColors.Green)
```

**Ejemplo (js):**

```js
// Define an object with color names mapped to their corresponding palette indices for phone colors
const PhoneColors = {
    Blue: 0,
    Green: 1,
    Red: 2,
    Orange: 3,
    Grey: 4,
    Purple: 5,
    Pink: 6
};

// Retrieve the current player ped
const playerPed = PlayerPedId();

// Set the phone color of the player's ped to Green using the corresponding index from the PhoneColors object
SetPedPhonePaletteIdx(playerPed, PhoneColors.Green);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Define an enum with color names and their corresponding indices
public enum PhoneColors
{
    Blue = 0,
    Green = 1,
    Red = 2,
    Orange = 3,
    Grey = 4,
    Purple = 5,
    Pink = 6
}

// Retrieve the current player ped
int playerPed = PlayerPedId();

// Set the phone color of the player's ped to Green using the enum value
SetPedPhonePaletteIdx(playerPed, (int)PhoneColors.Green);
```

---
### SetPedPinnedDown

`SET_PED_PINNED_DOWN` · hash `0xAAD6D1ACF08F4612` · jhash `0xCC78999D` · **Cliente**

```lua
local retval = SetPedPinnedDown(ped, pinned, i)
```
```c
Any SET_PED_PINNED_DOWN(Ped ped, BOOL pinned, int i);
```

**Parámetros**

- `ped` (`Ped`)
- `pinned` (`BOOL`)
- `i` (`int`)

**Devuelve:** `Any`

**Descripción oficial:**

```
i could be time. Only example in the decompiled scripts uses it as -1.
```

---
### SetPedPlaysHeadOnHornAnimWhenDiesInVehicle

`SET_PED_PLAYS_HEAD_ON_HORN_ANIM_WHEN_DIES_IN_VEHICLE` · hash `0x94D94BF1A75AED3D` · jhash `0x7C563CD2` · **Cliente**

```lua
SetPedPlaysHeadOnHornAnimWhenDiesInVehicle(ped, toggle)
```
```c
void SET_PED_PLAYS_HEAD_ON_HORN_ANIM_WHEN_DIES_IN_VEHICLE(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

```
Points to the same function as for example GET_RANDOM_VEHICLE_MODEL_IN_MEMORY and it does absolutely nothing.  
```

---
### SetPedPreferredCoverSet

`SET_PED_PREFERRED_COVER_SET` · hash `0x8421EB4DA7E391B9` · jhash `0xF3B7EFBF` · **Cliente**

```lua
SetPedPreferredCoverSet(ped, itemSet)
```
```c
void SET_PED_PREFERRED_COVER_SET(Ped ped, Any itemSet);
```

**Parámetros**

- `ped` (`Ped`)
- `itemSet` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8421EB4DA7E391B9` (`N_0x8421eb4da7e391b9`)

---
### SetPedPreloadPropData

`SET_PED_PRELOAD_PROP_DATA` · hash `0x2B16A3BFF1FBCE49` · jhash `0xC0E23671` · **Cliente**

```lua
local retval = SetPedPreloadPropData(ped, componentId, drawableId, textureId)
```
```c
BOOL SET_PED_PRELOAD_PROP_DATA(Ped ped, int componentId, int drawableId, int textureId);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component that you want to set. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).
- `drawableId` (`int`): The drawable id that is going to be set. Refer to [GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS](#getnumberofpedpropdrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_PROP_TEXTURE_VARIATIONS](#getnumberofpedproptexturevariations).

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2B16A3BFF1FBCE49` (`N_0x2b16a3bff1fbce49`), `_IS_PED_PROP_VALID` (`IsPedPropValid`)

---
### SetPedPreloadVariationData

`SET_PED_PRELOAD_VARIATION_DATA` · hash `0x39D55A620FCB6A3A` · jhash `0x45F3BDFB` · **Cliente**

```lua
local retval = SetPedPreloadVariationData(ped, slot, drawableId, textureId)
```
```c
Any SET_PED_PRELOAD_VARIATION_DATA(Ped ped, int slot, int drawableId, int textureId);
```

**Parámetros**

- `ped` (`Ped`)
- `slot` (`int`)
- `drawableId` (`int`)
- `textureId` (`int`)

**Devuelve:** `Any`

**Descripción oficial:**

```
from extreme3.c4
PED::_39D55A620FCB6A3A(PLAYER::PLAYER_PED_ID(), 8, PED::GET_PED_DRAWABLE_VARIATION(PLAYER::PLAYER_PED_ID(), 8), PED::GET_PED_TEXTURE_VARIATION(PLAYER::PLAYER_PED_ID(), 8));
p1 is probably componentId
```

**Nombres antiguos (alias):** `0x39D55A620FCB6A3A` (`N_0x39d55a620fcb6a3a`)

---
### SetPedPrimaryLookat

`SET_PED_PRIMARY_LOOKAT` · hash `0xCD17B554996A8D9E` · jhash `0x6DEF6F1C` · **Cliente**

```lua
SetPedPrimaryLookat(ped, lookAt)
```
```c
void SET_PED_PRIMARY_LOOKAT(Ped ped, Ped lookAt);
```

**Parámetros**

- `ped` (`Ped`)
- `lookAt` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

```
This is only called once in the scripts.
sub_1CD9(&l_49, 0, getElem(3, &l_34, 4), "MICHAEL", 0, 1);
                    sub_1CA8("WORLD_HUMAN_SMOKING", 2);
                    PED::SET_PED_PRIMARY_LOOKAT(getElem(3, &l_34, 4), PLAYER::PLAYER_PED_ID());
```

---
### SetPedPropIndex

`SET_PED_PROP_INDEX` · hash `0x93376B65A266EB5F` · jhash `0x0829F2E2` · **Cliente · también en el servidor (RPC)**

```lua
SetPedPropIndex(ped, componentId, drawableId, textureId, attach)
```
```c
void SET_PED_PROP_INDEX(Ped ped, int componentId, int drawableId, int textureId, BOOL attach);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.
- `componentId` (`int`): The component that you want to set. Refer to [SET_PED_COMPONENT_VARIATION](../cfx/servidor.md#setpedcomponentvariation).
- `drawableId` (`int`): The drawable id that is going to be set. Refer to [GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS](#getnumberofpedpropdrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_PROP_TEXTURE_VARIATIONS](#getnumberofpedproptexturevariations).
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

---
### SetPedRagdollForceFall

`SET_PED_RAGDOLL_FORCE_FALL` · hash `0x01F6594B923B9251` · jhash `0x20A5BDE0` · **Cliente**

```lua
SetPedRagdollForceFall(ped)
```
```c
void SET_PED_RAGDOLL_FORCE_FALL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### SetPedRagdollOnCollision

`SET_PED_RAGDOLL_ON_COLLISION` · hash `0xF0A4F1BBF4FA7497` · jhash `0x2654A0F4` · **Cliente**

```lua
SetPedRagdollOnCollision(ped, toggle)
```
```c
void SET_PED_RAGDOLL_ON_COLLISION(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Causes Ped to ragdoll on collision with any object (e.g Running into trashcan). If applied to player you will sometimes trip on the sidewalk.
Needs to be recalled after each ragdoll from a Collision.

---
### SetPedRandomComponentVariation

`SET_PED_RANDOM_COMPONENT_VARIATION` · hash `0xC8A9481A01E63C28` · jhash `0x4111BA46` · **Cliente · también en el servidor (RPC)**

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

---
### SetPedRandomProps

`SET_PED_RANDOM_PROPS` · hash `0xC44AA05345C992C6` · jhash `0xE3318E0E` · **Cliente · también en el servidor (RPC)**

```lua
SetPedRandomProps(ped)
```
```c
void SET_PED_RANDOM_PROPS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped handle.

**Devuelve:** `void`

---
### SetPedRelationshipGroupDefaultHash

`SET_PED_RELATIONSHIP_GROUP_DEFAULT_HASH` · hash `0xADB3F206518799E8` · jhash `0x423B7BA2` · **Cliente**

```lua
SetPedRelationshipGroupDefaultHash(ped, hash)
```
```c
void SET_PED_RELATIONSHIP_GROUP_DEFAULT_HASH(Ped ped, Hash hash);
```

**Parámetros**

- `ped` (`Ped`)
- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### SetPedRelationshipGroupHash

`SET_PED_RELATIONSHIP_GROUP_HASH` · hash `0xC80A74AC829DDD92` · jhash `0x79F8C18C` · **Cliente**

```lua
SetPedRelationshipGroupHash(ped, hash)
```
```c
void SET_PED_RELATIONSHIP_GROUP_HASH(Ped ped, Hash hash);
```

**Parámetros**

- `ped` (`Ped`)
- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### SetPedReserveParachuteTintIndex

`SET_PED_RESERVE_PARACHUTE_TINT_INDEX` · hash `0xE88DA0751C22A2AD` · jhash `0x177EFC79` · **Cliente**

```lua
SetPedReserveParachuteTintIndex(ped, p1)
```
```c
void SET_PED_RESERVE_PARACHUTE_TINT_INDEX(Ped ped, Any p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### SetPedResetFlag

`SET_PED_RESET_FLAG` · hash `0xC1E8A365BF3B29F2` · jhash `0xCFF6FF66` · **Cliente · también en el servidor (RPC)**

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

---
### SetPedScubaGearVariation

`_SET_PED_SCUBA_GEAR_VARIATION` · hash `0x36C6984C3ED0C911` · **Cliente**

```lua
SetPedScubaGearVariation(ped)
```
```c
void _SET_PED_SCUBA_GEAR_VARIATION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

This native sets a scuba mask for freemode models and an oxygen bottle for player_\* models. It works on freemode and player_\* models.

**Nombres antiguos (alias):** `0x36C6984C3ED0C911` (`N_0x36c6984c3ed0c911`)

---
### SetPedSeeingRange

`SET_PED_SEEING_RANGE` · hash `0xF29CF591C4BF6CEE` · jhash `0x4BD72FE8` · **Cliente**

```lua
SetPedSeeingRange(ped, value)
```
```c
void SET_PED_SEEING_RANGE(Ped ped, float value);
```

**Parámetros**

- `ped` (`Ped`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetPedShootRate

`SET_PED_SHOOT_RATE` · hash `0x614DA022990752DC` · jhash `0xFB301746` · **Cliente**

```lua
SetPedShootRate(ped, shootRate)
```
```c
void SET_PED_SHOOT_RATE(Ped ped, int shootRate);
```

**Parámetros**

- `ped` (`Ped`)
- `shootRate` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
shootRate 0-1000  
```

---
### SetPedShootsAtCoord

`SET_PED_SHOOTS_AT_COORD` · hash `0x96A05E4FB321B1BA` · jhash `0xFD64EAE5` · **Cliente**

```lua
SetPedShootsAtCoord(ped, x, y, z, toggle)
```
```c
void SET_PED_SHOOTS_AT_COORD(Ped ped, float x, float y, float z, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`): Ped index.
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Fires a weapon at a coordinate using a ped.

---
### SetPedShouldPlayDirectedScenarioExit

`_SET_PED_SHOULD_PLAY_DIRECTED_SCENARIO_EXIT` · hash `0xEC6935EBE0847B90` · jhash `0x761F8F48` · **Cliente**

```lua
local retval = SetPedShouldPlayDirectedScenarioExit(ped, x, y, z)
```
```c
BOOL _SET_PED_SHOULD_PLAY_DIRECTED_SCENARIO_EXIT(Ped ped, float x, float y, float z);
```

**Parámetros**

- `ped` (`Ped`): the ped who should play a normal (unhurried) exit the next time they are given a script command.
- `x` (`float`): X Coordinate.
- `y` (`float`): Y Coordinate.
- `z` (`float`): Z Coordinate.

**Devuelve:** `BOOL` — Returns true if the position was successfully set.

**Descripción oficial:**

When this ped receives its next script task, they will exit from their scenario using the normal scenario exit.
Exiting the scenario may take several frames while the ped is playing the exit animation.
If the ped is not currently using a scenario at the time of the command or 0,0,0 is specified as the reaction position,
then the ped will by default attempt to direct their exit forwards.

**Nombres antiguos (alias):** `0xEC6935EBE0847B90` (`N_0xec6935ebe0847b90`)

---
### SetPedShouldPlayFleeScenarioExit

`SET_PED_SHOULD_PLAY_FLEE_SCENARIO_EXIT` · hash `0xEEED8FAFEC331A70` · jhash `0x7B4C3E6F` · **Cliente**

```lua
local retval = SetPedShouldPlayFleeScenarioExit(ped, p1, p2, p3)
```
```c
Any SET_PED_SHOULD_PLAY_FLEE_SCENARIO_EXIT(Ped ped, Any p1, Any p2, Any p3);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xEEED8FAFEC331A70` (`N_0xeeed8fafec331a70`)

---
### SetPedShouldPlayImmediateScenarioExit

`SET_PED_SHOULD_PLAY_IMMEDIATE_SCENARIO_EXIT` · hash `0xF1C03A5352243A30` · jhash `0x4C684C81` · **Cliente**

```lua
SetPedShouldPlayImmediateScenarioExit(ped)
```
```c
void SET_PED_SHOULD_PLAY_IMMEDIATE_SCENARIO_EXIT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF1C03A5352243A30` (`N_0xf1c03a5352243a30`)

---
### SetPedShouldPlayNormalScenarioExit

`SET_PED_SHOULD_PLAY_NORMAL_SCENARIO_EXIT` · hash `0xA3A9299C4F2ADB98` · jhash `0x033F43FA` · **Cliente**

```lua
SetPedShouldPlayNormalScenarioExit(ped)
```
```c
void SET_PED_SHOULD_PLAY_NORMAL_SCENARIO_EXIT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA3A9299C4F2ADB98` (`N_0xa3a9299c4f2adb98`)

---
### SetPedSphereDefensiveArea

`SET_PED_SPHERE_DEFENSIVE_AREA` · hash `0x9D3151A373974804` · jhash `0xBD96D8E8` · **Cliente**

```lua
SetPedSphereDefensiveArea(ped, x, y, z, radius, p5, p6)
```
```c
void SET_PED_SPHERE_DEFENSIVE_AREA(Ped ped, float x, float y, float z, float radius, BOOL p5, BOOL p6);
```

**Parámetros**

- `ped` (`Ped`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p5` (`BOOL`)
- `p6` (`BOOL`)

**Devuelve:** `void`

---
### SetPedStayInVehicleWhenJacked

`SET_PED_STAY_IN_VEHICLE_WHEN_JACKED` · hash `0xEDF4079F9D54C9A1` · jhash `0xB014A09C` · **Cliente**

```lua
SetPedStayInVehicleWhenJacked(ped, toggle)
```
```c
void SET_PED_STAY_IN_VEHICLE_WHEN_JACKED(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedStealthMovement

`SET_PED_STEALTH_MOVEMENT` · hash `0x88CBB5CEB96B7BD2` · jhash `0x67E28E1D` · **Cliente**

```lua
SetPedStealthMovement(ped, p1, action)
```
```c
void SET_PED_STEALTH_MOVEMENT(Ped ped, BOOL p1, char* action);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)
- `action` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 is usually 0 in the scripts. action is either 0 or a pointer to "DEFAULT_ACTION".  
```

---
### SetPedSteersAroundObjects

`SET_PED_STEERS_AROUND_OBJECTS` · hash `0x1509C089ADC208BF` · jhash `0x3BD9B0A6` · **Cliente**

```lua
SetPedSteersAroundObjects(ped, toggle)
```
```c
void SET_PED_STEERS_AROUND_OBJECTS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedSteersAroundPeds

`SET_PED_STEERS_AROUND_PEDS` · hash `0x46F2193B3AD1D891` · jhash `0x797CAE4F` · **Cliente**

```lua
SetPedSteersAroundPeds(ped, toggle)
```
```c
void SET_PED_STEERS_AROUND_PEDS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedSteersAroundVehicles

`SET_PED_STEERS_AROUND_VEHICLES` · hash `0xEB6FB9D48DDE23EC` · jhash `0x533C0651` · **Cliente**

```lua
SetPedSteersAroundVehicles(ped, toggle)
```
```c
void SET_PED_STEERS_AROUND_VEHICLES(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedStrafeClipset

`SET_PED_STRAFE_CLIPSET` · hash `0x29A28F3F8CF6D854` · jhash `0x0BACF010` · **Cliente**

```lua
SetPedStrafeClipset(ped, clipSet)
```
```c
void SET_PED_STRAFE_CLIPSET(Ped ped, char* clipSet);
```

**Parámetros**

- `ped` (`Ped`)
- `clipSet` (`char*`)

**Devuelve:** `void`

---
### SetPedSuffersCriticalHits

`SET_PED_SUFFERS_CRITICAL_HITS` · hash `0xEBD76F2359F190AC` · jhash `0x6F6FC7E6` · **Cliente**

```lua
SetPedSuffersCriticalHits(ped, toggle)
```
```c
void SET_PED_SUFFERS_CRITICAL_HITS(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Ped no longer takes critical damage modifiers if set to FALSE.

Example: Headshotting a player no longer one shots them. Instead they will take the same damage as a torso shot.

---
### SetPedSurvivesBeingOutOfWater

`_SET_PED_SURVIVES_BEING_OUT_OF_WATER` · hash `0x100CD221F572F6E1` · **Cliente**

```lua
local retval = SetPedSurvivesBeingOutOfWater(ped, toggle)
```
```c
BOOL _SET_PED_SURVIVES_BEING_OUT_OF_WATER(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`): The marine animal ped
- `toggle` (`BOOL`): `true` to allow survival out of water, `false` to apply normal water restrictions.

**Devuelve:** `BOOL` — Returns `true` if successful.

**Descripción oficial:**

Allows marine animals to survive outside of water (R\* is using it for sharks).

```
NativeDB Introduced: v3407
```

---
### SetPedSweat

`SET_PED_SWEAT` · hash `0x27B0405F59637D1F` · jhash `0x76A1DB9F` · **Cliente**

```lua
SetPedSweat(ped, sweat)
```
```c
void SET_PED_SWEAT(Ped ped, float sweat);
```

**Parámetros**

- `ped` (`Ped`)
- `sweat` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sweat is set to 100.0 or 0.0 in the decompiled scripts.  
```

---
### SetPedTargetLossResponse

`SET_PED_TARGET_LOSS_RESPONSE` · hash `0x0703B9079823DA4A` · jhash `0xCFA613FF` · **Cliente**

```lua
SetPedTargetLossResponse(ped, responseType)
```
```c
void SET_PED_TARGET_LOSS_RESPONSE(Ped ped, int responseType);
```

**Parámetros**

- `ped` (`Ped`)
- `responseType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only 1 and 2 appear in the scripts. combatbehaviour.meta seems to only have TLR_SearchForTarget for all peds, but we don't know if that's 1 or 2.  
```

---
### SetPedToInformRespectedFriends

`SET_PED_TO_INFORM_RESPECTED_FRIENDS` · hash `0x112942C6E708F70B` · jhash `0xD78AC46C` · **Cliente**

```lua
SetPedToInformRespectedFriends(ped, radius, maxFriends)
```
```c
void SET_PED_TO_INFORM_RESPECTED_FRIENDS(Ped ped, float radius, int maxFriends);
```

**Parámetros**

- `ped` (`Ped`)
- `radius` (`float`)
- `maxFriends` (`int`)

**Devuelve:** `void`

---
