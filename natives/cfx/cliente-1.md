# Natives de FiveM (CFX) — solo cliente (parte 1 de 2: ActivateTimecycleEditor … SetVehicleWheelTractionVectorLength)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

**554** natives.

Partes: **[1]** · [2](cliente-2.md)

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivateTimecycleEditor`](#activatetimecycleeditor) · [`AddAudioSubmixOutput`](#addaudiosubmixoutput) · [`AddAuthorizedParachuteModel`](#addauthorizedparachutemodel) · [`AddAuthorizedParachutePackModel`](#addauthorizedparachutepackmodel) · [`AddHealthConfig`](#addhealthconfig) · [`AddMinimapOverlay`](#addminimapoverlay) · [`AddMinimapOverlayWithDepth`](#addminimapoverlaywithdepth) · [`AddReplaceTexture`](#addreplacetexture) · [`AddTextEntry`](#addtextentry) · [`AddTextEntryByHash`](#addtextentrybyhash) · [`ApplyWeatherCycles`](#applyweathercycles) · [`BreakOffVehicleWheel`](#breakoffvehiclewheel) · [`CallMinimapScaleformFunction`](#callminimapscaleformfunction) · [`ClearVehicleXenonLightsCustomColor`](#clearvehiclexenonlightscustomcolor) · [`CloneTimecycleModifier`](#clonetimecyclemodifier) · [`CommitRuntimeTexture`](#commitruntimetexture) · [`CreateAudioSubmix`](#createaudiosubmix) · [`CreateDryVolume`](#createdryvolume) · [`CreateDui`](#createdui) · [`CreateRuntimeTexture`](#createruntimetexture) · [`CreateRuntimeTextureFromDuiHandle`](#createruntimetexturefromduihandle) · [`CreateRuntimeTextureFromImage`](#createruntimetexturefromimage) · [`CreateRuntimeTxd`](#createruntimetxd) · [`CreateTimecycleModifier`](#createtimecyclemodifier) · [`DestroyDui`](#destroydui) · [`DisableEditorRuntime`](#disableeditorruntime) · [`DisableIdleCamera`](#disableidlecamera) · [`DisableRawKeyThisFrame`](#disablerawkeythisframe) · [`DisableVehiclePassengerIdleCamera`](#disablevehiclepassengeridlecamera) · [`DisableWorldhorizonRendering`](#disableworldhorizonrendering) · [`DoesTimecycleModifierHasVar`](#doestimecyclemodifierhasvar) · [`DoesVehicleUseFuel`](#doesvehicleusefuel) · [`DoorSystemGetActive`](#doorsystemgetactive) · [`DoorSystemGetSize`](#doorsystemgetsize) · [`DrawCorona`](#drawcorona) · [`DrawGizmo`](#drawgizmo) · [`DrawGlowSphere`](#drawglowsphere) · [`DrawLight`](#drawlight) · [`DrawLine_2d`](#drawline_2d) · [`DrawRectRotated`](#drawrectrotated) · [`EnableEditorRuntime`](#enableeditorruntime) · [`EndFindObject`](#endfindobject) · [`EndFindPed`](#endfindped) · [`EndFindPickup`](#endfindpickup) · [`EndFindVehicle`](#endfindvehicle) · [`EnterCursorMode`](#entercursormode) · [`ExperimentalLoadCloneCreate`](#experimentalloadclonecreate) · [`ExperimentalLoadCloneSync`](#experimentalloadclonesync) · [`ExperimentalSaveCloneCreate`](#experimentalsaveclonecreate) · [`ExperimentalSaveCloneSync`](#experimentalsaveclonesync) · [`FindFirstObject`](#findfirstobject) · [`FindFirstPed`](#findfirstped) · [`FindFirstPickup`](#findfirstpickup) · [`FindFirstVehicle`](#findfirstvehicle) · [`FindNextObject`](#findnextobject) · [`FindNextPed`](#findnextped) · [`FindNextPickup`](#findnextpickup) · [`FindNextVehicle`](#findnextvehicle) · [`ForceSnowPass`](#forcesnowpass) · [`GetActivePlayers`](#getactiveplayers) · [`GetAllRopes`](#getallropes) · [`GetAllTrackJunctions`](#getalltrackjunctions) · [`GetAllVehicleModels`](#getallvehiclemodels) · [`GetAmbientPedRangeMultiplier`](#getambientpedrangemultiplier) · [`GetAmbientVehicleRangeMultiplier`](#getambientvehiclerangemultiplier) · [`GetCalmingQuadAtCoords`](#getcalmingquadatcoords) · [`GetCalmingQuadBounds`](#getcalmingquadbounds) · [`GetCalmingQuadCount`](#getcalmingquadcount) · [`GetCalmingQuadDampening`](#getcalmingquaddampening) · [`GetCamMatrix`](#getcammatrix) · [`GetClosestTrackNodes`](#getclosesttracknodes) · [`GetCurrentGameName`](#getcurrentgamename) · [`GetCurrentServerEndpoint`](#getcurrentserverendpoint) · [`GetDuiHandle`](#getduihandle) · [`GetEntityAddress`](#getentityaddress) · [`GetEntityArchetypeName`](#getentityarchetypename) · [`GetEntityIndexFromMapdata`](#getentityindexfrommapdata) · [`GetEntityMapdataOwner`](#getentitymapdataowner) · [`GetExternalKvpFloat`](#getexternalkvpfloat) · [`GetExternalKvpInt`](#getexternalkvpint) · [`GetExternalKvpString`](#getexternalkvpstring) · [`GetFallDamageLandOnFootMultiplier`](#getfalldamagelandonfootmultiplier) · [`GetFallDamageMultiplier`](#getfalldamagemultiplier) · [`GetFuelConsumptionRateMultiplier`](#getfuelconsumptionratemultiplier) · [`GetFuelConsumptionState`](#getfuelconsumptionstate) · [`GetGlobalPassengerMassMultiplier`](#getglobalpassengermassmultiplier) · [`GetHudComponentAlign`](#gethudcomponentalign) · [`GetHudComponentName`](#gethudcomponentname) · [`GetHudComponentSize`](#gethudcomponentsize) · [`GetInteriorEntitiesExtents`](#getinteriorentitiesextents) · [`GetInteriorPortalCornerPosition`](#getinteriorportalcornerposition) · [`GetInteriorPortalCount`](#getinteriorportalcount) · [`GetInteriorPortalEntityArchetype`](#getinteriorportalentityarchetype) · [`GetInteriorPortalEntityCount`](#getinteriorportalentitycount) · [`GetInteriorPortalEntityFlag`](#getinteriorportalentityflag) · [`GetInteriorPortalEntityPosition`](#getinteriorportalentityposition) · [`GetInteriorPortalEntityRotation`](#getinteriorportalentityrotation) · [`GetInteriorPortalFlag`](#getinteriorportalflag) · [`GetInteriorPortalRoomFrom`](#getinteriorportalroomfrom) · [`GetInteriorPortalRoomTo`](#getinteriorportalroomto) · [`GetInteriorPosition`](#getinteriorposition) · [`GetInteriorRoomCount`](#getinteriorroomcount) · [`GetInteriorRoomExtents`](#getinteriorroomextents) · [`GetInteriorRoomFlag`](#getinteriorroomflag) · [`GetInteriorRoomIndexByHash`](#getinteriorroomindexbyhash) · [`GetInteriorRoomName`](#getinteriorroomname) · [`GetInteriorRoomTimecycle`](#getinteriorroomtimecycle) · [`GetInteriorRotation`](#getinteriorrotation) · [`GetKillFallHeight`](#getkillfallheight) · [`GetMapZoomDataLevel`](#getmapzoomdatalevel) · [`GetMapdataEntityHandle`](#getmapdataentityhandle) · [`GetMapdataEntityMatrix`](#getmapdataentitymatrix) · [`GetMapdataFromHashKey`](#getmapdatafromhashkey) · [`GetNuiCursorPosition`](#getnuicursorposition) · [`GetNumberOfPedCollectionDrawableVariations`](#getnumberofpedcollectiondrawablevariations) · [`GetNumberOfPedCollectionPropDrawableVariations`](#getnumberofpedcollectionpropdrawablevariations) · [`GetNumberOfPedCollectionPropTextureVariations`](#getnumberofpedcollectionproptexturevariations) · [`GetNumberOfPedCollectionTextureVariations`](#getnumberofpedcollectiontexturevariations) · [`GetParkedVehicleDensityMultiplier`](#getparkedvehicledensitymultiplier) · [`GetPauseMapPointerWorldPosition`](#getpausemappointerworldposition) · [`GetPedCollectionLocalIndexFromDrawable`](#getpedcollectionlocalindexfromdrawable) · [`GetPedCollectionLocalIndexFromProp`](#getpedcollectionlocalindexfromprop) · [`GetPedCollectionName`](#getpedcollectionname) · [`GetPedCollectionNameFromDrawable`](#getpedcollectionnamefromdrawable) · [`GetPedCollectionNameFromProp`](#getpedcollectionnamefromprop) · [`GetPedCollectionsCount`](#getpedcollectionscount) · [`GetPedDecorations`](#getpeddecorations) · [`GetPedDensityMultiplier`](#getpeddensitymultiplier) · [`GetPedDrawableGlobalIndexFromCollection`](#getpeddrawableglobalindexfromcollection) · [`GetPedDrawableVariationCollectionLocalIndex`](#getpeddrawablevariationcollectionlocalindex) · [`GetPedDrawableVariationCollectionName`](#getpeddrawablevariationcollectionname) · [`GetPedEyeColor`](#getpedeyecolor) · [`GetPedFaceFeature`](#getpedfacefeature) · [`GetPedHairColor`](#getpedhaircolor) · [`GetPedHairHighlightColor`](#getpedhairhighlightcolor) · [`GetPedHeadOverlayData`](#getpedheadoverlaydata) · [`GetPedModelHealthConfig`](#getpedmodelhealthconfig) · [`GetPedModelPersonality`](#getpedmodelpersonality) · [`GetPedMovementClipset`](#getpedmovementclipset) · [`GetPedPropCollectionLocalIndex`](#getpedpropcollectionlocalindex) · [`GetPedPropCollectionName`](#getpedpropcollectionname) · [`GetPedPropGlobalIndexFromCollection`](#getpedpropglobalindexfromcollection) · [`GetPedSweat`](#getpedsweat) · [`GetPlayerFromServerId`](#getplayerfromserverid) · [`GetPlayerInvincible_2`](#getplayerinvincible_2) · [`GetPlayerKillFallHeight`](#getplayerkillfallheight) · [`GetPlayerMaxStamina`](#getplayermaxstamina) · [`GetPlayerMeleeWeaponDefenseModifier`](#getplayermeleeweapondefensemodifier) · [`GetPlayerServerId`](#getplayerserverid) · [`GetPlayerStamina`](#getplayerstamina) · [`GetPlayerVehicleDamageModifier`](#getplayervehicledamagemodifier) · [`GetPlayerVehicleDefenseModifier`](#getplayervehicledefensemodifier) · [`GetRandomVehicleDensityMultiplier`](#getrandomvehicledensitymultiplier) · [`GetRopeFlags`](#getropeflags) · [`GetRopeLengthChangeRate`](#getropelengthchangerate) · [`GetRopeTimeMultiplier`](#getropetimemultiplier) · [`GetRopeUpdateOrder`](#getropeupdateorder) · [`GetRuntimeTextureHeight`](#getruntimetextureheight) · [`GetRuntimeTexturePitch`](#getruntimetexturepitch) · [`GetRuntimeTextureWidth`](#getruntimetexturewidth) · [`GetScenarioPedDensityMultiplier`](#getscenariopeddensitymultiplier) · [`GetTimecycleModifierCount`](#gettimecyclemodifiercount) · [`GetTimecycleModifierIndexByName`](#gettimecyclemodifierindexbyname) · [`GetTimecycleModifierNameByIndex`](#gettimecyclemodifiernamebyindex) · [`GetTimecycleModifierStrength`](#gettimecyclemodifierstrength) · [`GetTimecycleModifierVar`](#gettimecyclemodifiervar) · [`GetTimecycleModifierVarCount`](#gettimecyclemodifiervarcount) · [`GetTimecycleModifierVarNameByIndex`](#gettimecyclemodifiervarnamebyindex) · [`GetTimecycleVarCount`](#gettimecyclevarcount) · [`GetTimecycleVarDefaultValueByIndex`](#gettimecyclevardefaultvaluebyindex) · [`GetTimecycleVarNameByIndex`](#gettimecyclevarnamebyindex) · [`GetTrackBrakingDistance`](#gettrackbrakingdistance) · [`GetTrackMaxSpeed`](#gettrackmaxspeed) · [`GetTrackNodeCoords`](#gettracknodecoords) · [`GetTrackNodeCount`](#gettracknodecount) · [`GetTrainCurrentTrackNode`](#gettraincurrenttracknode) · [`GetTrainDoorCount`](#gettraindoorcount) · [`GetTrainDoorOpenRatio`](#gettraindooropenratio) · [`GetTrainSpeed`](#gettrainspeed) · [`GetVehicleAlarmTimeLeft`](#getvehiclealarmtimeleft) · [`GetVehicleCheatPowerIncrease`](#getvehiclecheatpowerincrease) · [`GetVehicleClutch`](#getvehicleclutch) · [`GetVehicleCurrentGear`](#getvehiclecurrentgear) · [`GetVehicleCurrentRpm`](#getvehiclecurrentrpm) · [`GetVehicleDashboardBoost`](#getvehicledashboardboost) · [`GetVehicleDashboardCurrentGear`](#getvehicledashboardcurrentgear) · [`GetVehicleDashboardFuel`](#getvehicledashboardfuel) · [`GetVehicleDashboardLights`](#getvehicledashboardlights) · [`GetVehicleDashboardOilPressure`](#getvehicledashboardoilpressure) · [`GetVehicleDashboardOilTemp`](#getvehicledashboardoiltemp) · [`GetVehicleDashboardRpm`](#getvehicledashboardrpm) · [`GetVehicleDashboardSpeed`](#getvehicledashboardspeed) · [`GetVehicleDashboardTemp`](#getvehicledashboardtemp) · [`GetVehicleDashboardVacuum`](#getvehicledashboardvacuum) · [`GetVehicleDensityMultiplier`](#getvehicledensitymultiplier) · [`GetVehicleDrawnWheelAngleMult`](#getvehicledrawnwheelanglemult) · [`GetVehicleEngineTemperature`](#getvehicleenginetemperature) · [`GetVehicleFuelLevel`](#getvehiclefuellevel) · [`GetVehicleGearRatio`](#getvehiclegearratio) · [`GetVehicleGravityAmount`](#getvehiclegravityamount) · [`GetVehicleHandlingFloat`](#getvehiclehandlingfloat) · [`GetVehicleHandlingInt`](#getvehiclehandlingint) · [`GetVehicleHandlingVector`](#getvehiclehandlingvector) · [`GetVehicleHasFlag`](#getvehiclehasflag) · [`GetVehicleHighGear`](#getvehiclehighgear) · [`GetVehicleIndicatorLights`](#getvehicleindicatorlights) · [`GetVehicleLightMultiplier`](#getvehiclelightmultiplier) · [`GetVehicleNextGear`](#getvehiclenextgear) · [`GetVehicleNumberOfWheels`](#getvehiclenumberofwheels) · [`GetVehicleOilLevel`](#getvehicleoillevel) · [`GetVehicleSteeringScale`](#getvehiclesteeringscale) · [`GetVehicleThrottleOffset`](#getvehiclethrottleoffset) · [`GetVehicleTopSpeedModifier`](#getvehicletopspeedmodifier) · [`GetVehicleTurboPressure`](#getvehicleturbopressure) · [`GetVehicleTypeRaw`](#getvehicletyperaw) · [`GetVehicleWheelBrakePressure`](#getvehiclewheelbrakepressure) · [`GetVehicleWheelFlags`](#getvehiclewheelflags) · [`GetVehicleWheelHealth`](#getvehiclewheelhealth) · [`GetVehicleWheelIsPowered`](#getvehiclewheelispowered) · [`GetVehicleWheelPower`](#getvehiclewheelpower) · [`GetVehicleWheelRimColliderSize`](#getvehiclewheelrimcollidersize) · [`GetVehicleWheelRotationSpeed`](#getvehiclewheelrotationspeed) · [`GetVehicleWheelSize`](#getvehiclewheelsize) · [`GetVehicleWheelSpeed`](#getvehiclewheelspeed) · [`GetVehicleWheelSteeringAngle`](#getvehiclewheelsteeringangle) · [`GetVehicleWheelSurfaceMaterial`](#getvehiclewheelsurfacematerial) · [`GetVehicleWheelSuspensionCompression`](#getvehiclewheelsuspensioncompression) · [`GetVehicleWheelTireColliderSize`](#getvehiclewheeltirecollidersize) · [`GetVehicleWheelTireColliderWidth`](#getvehiclewheeltirecolliderwidth) · [`GetVehicleWheelTractionVectorLength`](#getvehiclewheeltractionvectorlength) · [`GetVehicleWheelWidth`](#getvehiclewheelwidth) · [`GetVehicleWheelXOffset`](#getvehiclewheelxoffset) · [`GetVehicleWheelYRotation`](#getvehiclewheelyrotation) · [`GetVehicleWheelieState`](#getvehiclewheeliestate) · [`GetVehicleXenonLightsCustomColor`](#getvehiclexenonlightscustomcolor) · [`GetVehicleXmasSnowFactor`](#getvehiclexmassnowfactor) · [`GetVisualSettingFloat`](#getvisualsettingfloat) · [`GetWaterQuadAlpha`](#getwaterquadalpha) · [`GetWaterQuadAtCoords`](#getwaterquadatcoords) · [`GetWaterQuadAtCoords_3d`](#getwaterquadatcoords_3d) · [`GetWaterQuadBounds`](#getwaterquadbounds) · [`GetWaterQuadCount`](#getwaterquadcount) · [`GetWaterQuadHasLimitedDepth`](#getwaterquadhaslimiteddepth) · [`GetWaterQuadIsInvisible`](#getwaterquadisinvisible) · [`GetWaterQuadLevel`](#getwaterquadlevel) · [`GetWaterQuadNoStencil`](#getwaterquadnostencil) · [`GetWaterQuadType`](#getwaterquadtype) · [`GetWaveQuadAmplitude`](#getwavequadamplitude) · [`GetWaveQuadAtCoords`](#getwavequadatcoords) · [`GetWaveQuadBounds`](#getwavequadbounds) · [`GetWaveQuadCount`](#getwavequadcount) · [`GetWaveQuadDirection`](#getwavequaddirection) · [`GetWeaponAccuracySpread`](#getweaponaccuracyspread) · [`GetWeaponAnimationOverride`](#getweaponanimationoverride) · [`GetWeaponComponentAccuracyModifier`](#getweaponcomponentaccuracymodifier) · [`GetWeaponComponentCameraHash`](#getweaponcomponentcamerahash) · [`GetWeaponComponentClipSize`](#getweaponcomponentclipsize) · [`GetWeaponComponentDamageModifier`](#getweaponcomponentdamagemodifier) · [`GetWeaponComponentRangeDamageModifier`](#getweaponcomponentrangedamagemodifier) · [`GetWeaponComponentRangeModifier`](#getweaponcomponentrangemodifier) · [`GetWeaponComponentReticuleHash`](#getweaponcomponentreticulehash) · [`GetWeaponDamageModifier`](#getweapondamagemodifier) · [`GetWeaponRecoilShakeAmplitude`](#getweaponrecoilshakeamplitude) · [`GetWorldCoordFromScreenCoord`](#getworldcoordfromscreencoord) · [`HasMinimapOverlayLoaded`](#hasminimapoverlayloaded) · [`IsBigmapActive`](#isbigmapactive) · [`IsBigmapFull`](#isbigmapfull) · [`IsDisabledRawKeyDown`](#isdisabledrawkeydown) · [`IsDisabledRawKeyPressed`](#isdisabledrawkeypressed) · [`IsDisabledRawKeyReleased`](#isdisabledrawkeyreleased) · [`IsDisabledRawKeyUp`](#isdisabledrawkeyup) · [`IsDuiAvailable`](#isduiavailable) · [`IsGameEnhancedVersion`](#isgameenhancedversion) · [`IsNuiFocusKeepingInput`](#isnuifocuskeepinginput) · [`IsNuiFocused`](#isnuifocused) · [`IsPedCollectionComponentVariationGen9Exclusive`](#ispedcollectioncomponentvariationgen9exclusive) · [`IsPedCollectionComponentVariationValid`](#ispedcollectioncomponentvariationvalid) · [`IsPedComponentVariationGen9Exclusive`](#ispedcomponentvariationgen9exclusive) · [`IsRawKeyDown`](#israwkeydown) · [`IsRawKeyPressed`](#israwkeypressed) · [`IsRawKeyReleased`](#israwkeyreleased) · [`IsRawKeyUp`](#israwkeyup) · [`IsStreamingFileReady`](#isstreamingfileready) · [`IsTrackEnabled`](#istrackenabled) · [`IsTrackSwitchedOff`](#istrackswitchedoff) · [`IsVehicleAlarmSet`](#isvehiclealarmset) · [`IsVehicleInteriorLightOn`](#isvehicleinteriorlighton) · [`IsVehicleNeedsToBeHotwired`](#isvehicleneedstobehotwired) · [`IsVehiclePreviouslyOwnedByPlayer`](#isvehiclepreviouslyownedbyplayer) · [`IsVehicleWanted`](#isvehiclewanted) · [`IsVehicleWheelBrokenOff`](#isvehiclewheelbrokenoff) · [`LeaveCursorMode`](#leavecursormode) · [`LoadWaterFromPath`](#loadwaterfrompath) · [`MumbleAddVoiceChannelListen`](#mumbleaddvoicechannellisten) · [`MumbleAddVoiceTargetChannel`](#mumbleaddvoicetargetchannel) · [`MumbleAddVoiceTargetPlayer`](#mumbleaddvoicetargetplayer) · [`MumbleAddVoiceTargetPlayerByServerId`](#mumbleaddvoicetargetplayerbyserverid) · [`MumbleClearVoiceChannel`](#mumbleclearvoicechannel) · [`MumbleClearVoiceTarget`](#mumbleclearvoicetarget) · [`MumbleClearVoiceTargetChannels`](#mumbleclearvoicetargetchannels) · [`MumbleClearVoiceTargetPlayers`](#mumbleclearvoicetargetplayers) · [`MumbleDoesChannelExist`](#mumbledoeschannelexist) · [`MumbleGetTalkerProximity`](#mumblegettalkerproximity) · [`MumbleGetVoiceChannelFromServerId`](#mumblegetvoicechannelfromserverid) · [`MumbleIsActive`](#mumbleisactive) · [`MumbleIsConnected`](#mumbleisconnected) · [`MumbleIsPlayerTalking`](#mumbleisplayertalking) · [`MumbleRemoveVoiceChannelListen`](#mumbleremovevoicechannellisten) · [`MumbleRemoveVoiceTargetChannel`](#mumbleremovevoicetargetchannel) · [`MumbleRemoveVoiceTargetPlayer`](#mumbleremovevoicetargetplayer) · [`MumbleRemoveVoiceTargetPlayerByServerId`](#mumbleremovevoicetargetplayerbyserverid) · [`MumbleSetActive`](#mumblesetactive) · [`MumbleSetAudioInputDistance`](#mumblesetaudioinputdistance) · [`MumbleSetAudioInputIntent`](#mumblesetaudioinputintent) · [`MumbleSetAudioOutputDistance`](#mumblesetaudiooutputdistance) · [`MumbleSetServerAddress`](#mumblesetserveraddress) · [`MumbleSetSubmixForServerId`](#mumblesetsubmixforserverid) · [`MumbleSetTalkerProximity`](#mumblesettalkerproximity) · [`MumbleSetVoiceChannel`](#mumblesetvoicechannel) · [`MumbleSetVoiceTarget`](#mumblesetvoicetarget) · [`MumbleSetVolumeOverride`](#mumblesetvolumeoverride) · [`MumbleSetVolumeOverrideByServerId`](#mumblesetvolumeoverridebyserverid) · [`OnesyncEnableRemoteAttachmentSanitization`](#onesyncenableremoteattachmentsanitization) · [`OverridePedsCanStandOnTopFlag`](#overridepedscanstandontopflag) · [`OverridePedsUseDefaultDriveByClipset`](#overridepedsusedefaultdrivebyclipset) · [`OverridePopGroups`](#overridepopgroups) · [`OverrideReactionToVehicleSiren`](#overridereactiontovehiclesiren) · [`OverrideVehiclePedsCanStandOnTopFlag`](#overridevehiclepedscanstandontopflag) · [`PrepareLight`](#preparelight) · [`RegisterArchetypes`](#registerarchetypes) · [`RegisterFontFile`](#registerfontfile) · [`RegisterFontId`](#registerfontid) · [`RegisterKeyMapping`](#registerkeymapping) · [`RegisterNuiCallback`](#registernuicallback) · [`RegisterNuiCallbackType`](#registernuicallbacktype) · [`RegisterRawNuiCallback`](#registerrawnuicallback) · [`RegisterRopeData`](#registerropedata) · [`RegisterStreamingFileFromCache`](#registerstreamingfilefromcache) · [`RegisterStreamingFileFromKvs`](#registerstreamingfilefromkvs) · [`RegisterStreamingFileFromUrl`](#registerstreamingfilefromurl) · [`RegisterTrackJunction`](#registertrackjunction) · [`RemoveDryVolume`](#removedryvolume) · [`RemoveHealthConfig`](#removehealthconfig) · [`RemoveReplaceTexture`](#removereplacetexture) · [`RemoveTimecycleModifier`](#removetimecyclemodifier) · [`RemoveTimecycleModifierVar`](#removetimecyclemodifiervar) · [`RemoveTrackJunction`](#removetrackjunction) · [`RequestResourceFileSet`](#requestresourcefileset) · [`ResetEntityDrawOutlineRenderTechnique`](#resetentitydrawoutlinerendertechnique) · [`ResetFlyThroughWindscreenParams`](#resetflythroughwindscreenparams) · [`ResetMapZoomDataLevel`](#resetmapzoomdatalevel) · [`ResetMapdataEntityMatrix`](#resetmapdataentitymatrix) · [`ResetPedModelPersonality`](#resetpedmodelpersonality) · [`ResetVehiclePedsCanStandOnTopFlag`](#resetvehiclepedscanstandontopflag) · [`ResetWater`](#resetwater) · [`SelectEntityAtCursor`](#selectentityatcursor) · [`SelectEntityAtPos`](#selectentityatpos) · [`SendDuiMessage`](#sendduimessage) · [`SendDuiMouseDown`](#sendduimousedown) · [`SendDuiMouseMove`](#sendduimousemove) · [`SendDuiMouseUp`](#sendduimouseup) · [`SendDuiMouseWheel`](#sendduimousewheel) · [`SendLoadingScreenMessage`](#sendloadingscreenmessage) · [`SendNuiMessage`](#sendnuimessage) · [`SetAimCooldown`](#setaimcooldown) · [`SetAudioSubmixEffectParamFloat`](#setaudiosubmixeffectparamfloat) · [`SetAudioSubmixEffectParamInt`](#setaudiosubmixeffectparamint) · [`SetAudioSubmixEffectRadioFx`](#setaudiosubmixeffectradiofx) · [`SetAudioSubmixOutputVolumes`](#setaudiosubmixoutputvolumes) · [`SetCalmingQuadBounds`](#setcalmingquadbounds) · [`SetCalmingQuadDampening`](#setcalmingquaddampening) · [`SetDefaultVehicleNumberPlateTextPattern`](#setdefaultvehiclenumberplatetextpattern) · [`SetDiscordAppId`](#setdiscordappid) · [`SetDiscordRichPresenceAction`](#setdiscordrichpresenceaction) · [`SetDiscordRichPresenceAsset`](#setdiscordrichpresenceasset) · [`SetDiscordRichPresenceAssetSmall`](#setdiscordrichpresenceassetsmall) · [`SetDiscordRichPresenceAssetSmallText`](#setdiscordrichpresenceassetsmalltext) · [`SetDiscordRichPresenceAssetText`](#setdiscordrichpresenceassettext) · [`SetDuiUrl`](#setduiurl) · [`SetEmitterProbeLength`](#setemitterprobelength) · [`SetEntityDrawOutline`](#setentitydrawoutline) · [`SetEntityDrawOutlineColor`](#setentitydrawoutlinecolor) · [`SetEntityDrawOutlineRenderTechnique`](#setentitydrawoutlinerendertechnique) · [`SetEntityDrawOutlineShader`](#setentitydrawoutlineshader) · [`SetEntityMatrix`](#setentitymatrix) · [`SetFallDamageLandOnFootMultiplier`](#setfalldamagelandonfootmultiplier) · [`SetFallDamageMultiplier`](#setfalldamagemultiplier) · [`SetFlashLightKeepOnWhileMoving`](#setflashlightkeeponwhilemoving) · [`SetFlyThroughWindscreenParams`](#setflythroughwindscreenparams) · [`SetFogVolumeRenderDisabled`](#setfogvolumerenderdisabled) · [`SetFuelConsumptionRateMultiplier`](#setfuelconsumptionratemultiplier) · [`SetFuelConsumptionState`](#setfuelconsumptionstate) · [`SetGlobalPassengerMassMultiplier`](#setglobalpassengermassmultiplier) · [`SetHandlingField`](#sethandlingfield) · [`SetHandlingFloat`](#sethandlingfloat) · [`SetHandlingInt`](#sethandlingint) · [`SetHandlingVector`](#sethandlingvector) · [`SetHealthConfigDefaultArmor`](#sethealthconfigdefaultarmor) · [`SetHealthConfigDefaultEndurance`](#sethealthconfigdefaultendurance) · [`SetHealthConfigDefaultHealth`](#sethealthconfigdefaulthealth) · [`SetHealthConfigDogTakedownThreshold`](#sethealthconfigdogtakedownthreshold) · [`SetHealthConfigDyingThreshold`](#sethealthconfigdyingthreshold) · [`SetHealthConfigFatiguedThreshold`](#sethealthconfigfatiguedthreshold) · [`SetHealthConfigHurtThreshold`](#sethealthconfighurtthreshold) · [`SetHealthConfigInjuredThreshold`](#sethealthconfiginjuredthreshold) · [`SetHealthConfigInvincible`](#sethealthconfiginvincible) · [`SetHealthConfigMeleeFatalAttack`](#sethealthconfigmeleefatalattack) · [`SetHealthConfigWritheFromBulletThreshold`](#sethealthconfigwrithefrombulletthreshold) · [`SetHudComponentAlign`](#sethudcomponentalign) · [`SetHudComponentSize`](#sethudcomponentsize) · [`SetInteriorPortalCornerPosition`](#setinteriorportalcornerposition) · [`SetInteriorPortalEntityFlag`](#setinteriorportalentityflag) · [`SetInteriorPortalFlag`](#setinteriorportalflag) · [`SetInteriorPortalRoomFrom`](#setinteriorportalroomfrom) · [`SetInteriorPortalRoomTo`](#setinteriorportalroomto) · [`SetInteriorProbeLength`](#setinteriorprobelength) · [`SetInteriorRoomExtents`](#setinteriorroomextents) · [`SetInteriorRoomFlag`](#setinteriorroomflag) · [`SetInteriorRoomTimecycle`](#setinteriorroomtimecycle) · [`SetKeyMappingHideResources`](#setkeymappinghideresources) · [`SetKillFallHeight`](#setkillfallheight) · [`SetLightAlpha`](#setlightalpha) · [`SetLightAo`](#setlightao) · [`SetLightCapsuleSize`](#setlightcapsulesize) · [`SetLightClipRect`](#setlightcliprect) · [`SetLightColor`](#setlightcolor) · [`SetLightCone`](#setlightcone) · [`SetLightCoords`](#setlightcoords) · [`SetLightDirection`](#setlightdirection) · [`SetLightExtraflags`](#setlightextraflags) · [`SetLightFadeDistance`](#setlightfadedistance) · [`SetLightFalloff`](#setlightfalloff) · [`SetLightFlags`](#setlightflags) · [`SetLightHeadlight`](#setlightheadlight) · [`SetLightIntensity`](#setlightintensity) · [`SetLightInterior`](#setlightinterior) · [`SetLightPlane`](#setlightplane) · [`SetLightRadius`](#setlightradius) · [`SetLightShadowDetails`](#setlightshadowdetails) · [`SetLightShadowFadeDistance`](#setlightshadowfadedistance) · [`SetLightSpecularFadeDistance`](#setlightspecularfadedistance) · [`SetLightTexture`](#setlighttexture) · [`SetLightType`](#setlighttype) · [`SetLightVolumeDetails`](#setlightvolumedetails) · [`SetLightVolumetricFadeDistance`](#setlightvolumetricfadedistance) · [`SetManualShutdownLoadingScreenNui`](#setmanualshutdownloadingscreennui) · [`SetMapZoomDataLevel`](#setmapzoomdatalevel) · [`SetMillisecondsPerGameMinute`](#setmillisecondspergameminute) · [`SetMinimapClipType`](#setminimapcliptype) · [`SetMinimapComponentPosition`](#setminimapcomponentposition) · [`SetMinimapOverlayDisplay`](#setminimapoverlaydisplay) · [`SetModelHeadlightConfiguration`](#setmodelheadlightconfiguration) · [`SetMpGamerTagsUseVehicleBehavior`](#setmpgamertagsusevehiclebehavior) · [`SetMpGamerTagsVisibleDistance`](#setmpgamertagsvisibledistance) · [`SetNuiFocus`](#setnuifocus) · [`SetNuiFocusKeepInput`](#setnuifocuskeepinput) · [`SetNuiZindex`](#setnuizindex) · [`SetPedCollectionComponentVariation`](#setpedcollectioncomponentvariation) · [`SetPedCollectionPreloadPropData`](#setpedcollectionpreloadpropdata) · [`SetPedCollectionPreloadVariationData`](#setpedcollectionpreloadvariationdata) · [`SetPedCollectionPropIndex`](#setpedcollectionpropindex) · [`SetPedMeleeCombatLimits`](#setpedmeleecombatlimits) · [`SetPedModelHealthConfig`](#setpedmodelhealthconfig) · [`SetPedModelPersonality`](#setpedmodelpersonality) · [`SetPedTurningThresholds`](#setpedturningthresholds) · [`SetPlayerKillFallHeight`](#setplayerkillfallheight) · [`SetPlayerMaxStamina`](#setplayermaxstamina) · [`SetPlayerStamina`](#setplayerstamina) · [`SetPlayerTalkingOverride`](#setplayertalkingoverride) · [`SetReactionToVehicleSirenDisabled`](#setreactiontovehiclesirendisabled) · [`SetRichPresence`](#setrichpresence) · [`SetRopeLengthChangeRate`](#setropelengthchangerate) · [`SetRopesCreateNetworkWorldState`](#setropescreatenetworkworldstate) · [`SetRuntimeTextureArgbData`](#setruntimetextureargbdata) · [`SetRuntimeTextureImage`](#setruntimetextureimage) · [`SetRuntimeTexturePixel`](#setruntimetexturepixel) · [`SetSnakeoilForEntry`](#setsnakeoilforentry) · [`SetTextChatEnabled`](#settextchatenabled) · [`SetTimecycleModifierVar`](#settimecyclemodifiervar) · [`SetTrackBrakingDistance`](#settrackbrakingdistance) · [`SetTrackEnabled`](#settrackenabled) · [`SetTrackJunctionActive`](#settrackjunctionactive) · [`SetTrackMaxSpeed`](#settrackmaxspeed) · [`SetTrainDoorOpenRatio`](#settraindooropenratio) · [`SetTrainState`](#settrainstate) · [`SetTrainStopAtStations`](#settrainstopatstations) · [`SetTrainsForceDoorsOpen`](#settrainsforcedoorsopen) · [`SetVehicleAlarmTimeLeft`](#setvehiclealarmtimeleft) · [`SetVehicleAutoRepairDisabled`](#setvehicleautorepairdisabled) · [`SetVehicleClutch`](#setvehicleclutch) · [`SetVehicleCurrentGear`](#setvehiclecurrentgear) · [`SetVehicleCurrentRpm`](#setvehiclecurrentrpm) · [`SetVehicleEngineTemperature`](#setvehicleenginetemperature) · [`SetVehicleFlag`](#setvehicleflag) · [`SetVehicleFuelLevel`](#setvehiclefuellevel) · [`SetVehicleGearRatio`](#setvehiclegearratio) · [`SetVehicleGravityAmount`](#setvehiclegravityamount) · [`SetVehicleHandlingField`](#setvehiclehandlingfield) · [`SetVehicleHandlingFloat`](#setvehiclehandlingfloat) · [`SetVehicleHandlingInt`](#setvehiclehandlingint) · [`SetVehicleHandlingVector`](#setvehiclehandlingvector) · [`SetVehicleHighGear`](#setvehiclehighgear) · [`SetVehicleNextGear`](#setvehiclenextgear) · [`SetVehicleNitroPtfxRange`](#setvehiclenitroptfxrange) · [`SetVehicleOilLevel`](#setvehicleoillevel) · [`SetVehiclePitchBias`](#setvehiclepitchbias) · [`SetVehicleRollBias`](#setvehiclerollbias) · [`SetVehicleSteeringAngle`](#setvehiclesteeringangle) · [`SetVehicleSteeringScale`](#setvehiclesteeringscale) · [`SetVehicleSuspensionHeight`](#setvehiclesuspensionheight) · [`SetVehicleTurboPressure`](#setvehicleturbopressure) · [`SetVehicleWheelBrakePressure`](#setvehiclewheelbrakepressure) · [`SetVehicleWheelFlags`](#setvehiclewheelflags) · [`SetVehicleWheelHealth`](#setvehiclewheelhealth) · [`SetVehicleWheelIsPowered`](#setvehiclewheelispowered) · [`SetVehicleWheelPower`](#setvehiclewheelpower) · [`SetVehicleWheelRimColliderSize`](#setvehiclewheelrimcollidersize) · [`SetVehicleWheelRotationSpeed`](#setvehiclewheelrotationspeed) · [`SetVehicleWheelSize`](#setvehiclewheelsize) · [`SetVehicleWheelTireColliderSize`](#setvehiclewheeltirecollidersize) · [`SetVehicleWheelTireColliderWidth`](#setvehiclewheeltirecolliderwidth) · [`SetVehicleWheelTractionVectorLength`](#setvehiclewheeltractionvectorlength)

---
### ActivateTimecycleEditor

`ACTIVATE_TIMECYCLE_EDITOR` · hash `0xEEB9B76A` · **Cliente**

```lua
ActivateTimecycleEditor()
```
```c
void ACTIVATE_TIMECYCLE_EDITOR();
```

**Devuelve:** `void`

**Descripción oficial:**

Activates built-in timecycle editing tool.

---
### AddAudioSubmixOutput

`ADD_AUDIO_SUBMIX_OUTPUT` · hash `0xAC6E290D` · **Cliente**

```lua
AddAudioSubmixOutput(submixId, outputSubmixId)
```
```c
void ADD_AUDIO_SUBMIX_OUTPUT(int submixId, int outputSubmixId);
```

**Parámetros**

- `submixId` (`int`): The input submix.
- `outputSubmixId` (`int`): The output submix. Use `0` for the master game submix.

**Devuelve:** `void`

**Descripción oficial:**

Adds an output for the specified audio submix.

---
### AddAuthorizedParachuteModel

`ADD_AUTHORIZED_PARACHUTE_MODEL` · hash `0x8AC7AE9` · **Cliente**

```lua
AddAuthorizedParachuteModel(modelNameHash)
```
```c
void ADD_AUTHORIZED_PARACHUTE_MODEL(int modelNameHash);
```

**Parámetros**

- `modelNameHash` (`int`): Name hash of the model to allow to be used for the player ped's parachute

**Devuelve:** `void` — None.

**Descripción oficial:**

Adds the given model name hash to the list of valid models for the player ped's parachute.

---
### AddAuthorizedParachutePackModel

`ADD_AUTHORIZED_PARACHUTE_PACK_MODEL` · hash `0x2E86DEA5` · **Cliente**

```lua
AddAuthorizedParachutePackModel(modelNameHash)
```
```c
void ADD_AUTHORIZED_PARACHUTE_PACK_MODEL(int modelNameHash);
```

**Parámetros**

- `modelNameHash` (`int`): Name hash of the model to allow to be used for the player ped's parachute pack

**Devuelve:** `void` — None.

**Descripción oficial:**

Adds the given model name hash to the list of valid models for the player ped's parachute pack.

---
### AddHealthConfig

`ADD_HEALTH_CONFIG` · hash `0x9CBFD5C1` · **Cliente**

```lua
AddHealthConfig(configName, defaultHealth, defaultArmor, defaultEndurance, fatiguedHealthThreshold, injuredHealthThreshold, dyingHealthThreshold, hurtHealthThreshold, dogTakedownThreshold, writheFromBulletThreshold, meleeCardinalFatalAttack, invincible)
```
```c
void ADD_HEALTH_CONFIG(char* configName, float defaultHealth, float defaultArmor, float defaultEndurance, float fatiguedHealthThreshold, float injuredHealthThreshold, float dyingHealthThreshold, float hurtHealthThreshold, float dogTakedownThreshold, float writheFromBulletThreshold, BOOL meleeCardinalFatalAttack, BOOL invincible);
```

**Parámetros**

- `configName` (`char*`): Name of health config. Cannot be default game health config name.
- `defaultHealth` (`float`): Default health value.
- `defaultArmor` (`float`): Default armor value.
- `defaultEndurance` (`float`)
- `fatiguedHealthThreshold` (`float`): Fatigued health threshold value.
- `injuredHealthThreshold` (`float`): Injured health threshold value.
- `dyingHealthThreshold` (`float`): Dying health threshold value.
- `hurtHealthThreshold` (`float`): Hurt health threshold value.
- `dogTakedownThreshold` (`float`): Dog takedown threshold value.
- `writheFromBulletThreshold` (`float`): Writhe from bulled threshold value.
- `meleeCardinalFatalAttack` (`BOOL`): Melee cardinal fatal attack check value.
- `invincible` (`BOOL`): Invincible value.

**Devuelve:** `void`

**Descripción oficial:**

Adds new health config.

---
### AddMinimapOverlay

`ADD_MINIMAP_OVERLAY` · hash `0x4AFD2499` · **Cliente**

```lua
local retval = AddMinimapOverlay(name)
```
```c
int ADD_MINIMAP_OVERLAY(char* name);
```

**Parámetros**

- `name` (`char*`): The path to a `.gfx` file in the current resource. It has to be specified as a `file`.

**Devuelve:** `int` — A minimap overlay ID.

**Descripción oficial:**

Loads a minimap overlay from a GFx file in the current resource.

If you need to control the depth of overlay use [`ADD_MINIMAP_OVERLAY_WITH_DEPTH`](#addminimapoverlaywithdepth).

---
### AddMinimapOverlayWithDepth

`ADD_MINIMAP_OVERLAY_WITH_DEPTH` · hash `0xED0935B5` · **Cliente**

```lua
local retval = AddMinimapOverlayWithDepth(name, depth)
```
```c
int ADD_MINIMAP_OVERLAY_WITH_DEPTH(char* name, int depth);
```

**Parámetros**

- `name` (`char*`): The path to a `.gfx` file in the current resource. It has to be specified as a `file`.
- `depth` (`int`): The depth of new overlay on the minimap. Pass `-1` for game to figure out the highest depth itself. Should not be greater than `0x7EFFFFFD`.

**Devuelve:** `int` — A minimap overlay ID.

**Descripción oficial:**

Loads a minimap overlay from a GFx file in the current resource.

---
### AddReplaceTexture

`ADD_REPLACE_TEXTURE` · hash `0xA66F8F75` · **Cliente**

```lua
AddReplaceTexture(origTxd, origTxn, newTxd, newTxn)
```
```c
void ADD_REPLACE_TEXTURE(char* origTxd, char* origTxn, char* newTxd, char* newTxn);
```

**Parámetros**

- `origTxd` (`char*`)
- `origTxn` (`char*`)
- `newTxd` (`char*`)
- `newTxn` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Experimental natives, please do not use in a live environment.

---
### AddTextEntry

`ADD_TEXT_ENTRY` · hash `0x32CA01C3` · **Cliente**

```lua
AddTextEntry(entryKey, entryText)
```
```c
void ADD_TEXT_ENTRY(char* entryKey, char* entryText);
```

**Parámetros**

- `entryKey` (`char*`)
- `entryText` (`char*`)

**Devuelve:** `void`

---
### AddTextEntryByHash

`ADD_TEXT_ENTRY_BY_HASH` · hash `0x289DA860` · **Cliente**

```lua
AddTextEntryByHash(entryKey, entryText)
```
```c
void ADD_TEXT_ENTRY_BY_HASH(Hash entryKey, char* entryText);
```

**Parámetros**

- `entryKey` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `entryText` (`char*`)

**Devuelve:** `void`

---
### ApplyWeatherCycles

`APPLY_WEATHER_CYCLES` · hash `0x3422291C` · **Cliente**

```lua
local retval = ApplyWeatherCycles(numEntries, msPerCycle)
```
```c
BOOL APPLY_WEATHER_CYCLES(int numEntries, int msPerCycle);
```

**Parámetros**

- `numEntries` (`int`): The number of cycle entries. Must be between 1 and 256
- `msPerCycle` (`int`): The duration in milliseconds of each cycle. Must be between 1000 and 86400000 (24 hours)

**Devuelve:** `BOOL` — Returns true if all parameters were valid, otherwise false.

**Ejemplo (lua):**

```lua
-- Cycle between XMAS weather for 30 seconds (3 * 10000 milliseconds), and SMOG weather for 20 seconds (2 * 10000 milliseconds)
local success = SetWeatherCycleEntry(0, "XMAS", 3) and
                SetWeatherCycleEntry(1, "SMOG", 2) and
                ApplyWeatherCycles(2, 10000)
```

---
### BreakOffVehicleWheel

`BREAK_OFF_VEHICLE_WHEEL` · hash `0xA274CADB` · **Cliente**

```lua
BreakOffVehicleWheel(vehicle, wheelIndex, leaveDebrisTrail, deleteWheel, unknownFlag, putOnFire)
```
```c
void BREAK_OFF_VEHICLE_WHEEL(Vehicle vehicle, int wheelIndex, BOOL leaveDebrisTrail, BOOL deleteWheel, BOOL unknownFlag, BOOL putOnFire);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `wheelIndex` (`int`): The wheel index.
- `leaveDebrisTrail` (`BOOL`): Start "veh_debris_trail" ptfx.
- `deleteWheel` (`BOOL`): True to delete wheel, otherwise detach.
- `unknownFlag` (`BOOL`): Unknown flag.
- `putOnFire` (`BOOL`): Set wheel on fire once detached.

**Devuelve:** `void`

**Descripción oficial:**

Break off vehicle wheel by index. The `leaveDebrisTrail` flag requires `putOnFire` to be true.

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId())

if DoesEntityExist(vehicle) then
  for i = 0, 3 do
    BreakOffVehicleWheel(vehicle, i, true, false, true, false)
  end
end
```

---
### CallMinimapScaleformFunction

`CALL_MINIMAP_SCALEFORM_FUNCTION` · hash `0x4C89C0ED` · **Cliente**

```lua
local retval = CallMinimapScaleformFunction(miniMap, fnName)
```
```c
BOOL CALL_MINIMAP_SCALEFORM_FUNCTION(int miniMap, char* fnName);
```

**Parámetros**

- `miniMap` (`int`): The minimap overlay ID.
- `fnName` (`char*`): A function in the overlay's TIMELINE.

**Devuelve:** `BOOL`

**Descripción oficial:**

This is similar to the PushScaleformMovieFunction natives, except it calls in the `TIMELINE` of a minimap overlay.

---
### ClearVehicleXenonLightsCustomColor

`CLEAR_VEHICLE_XENON_LIGHTS_CUSTOM_COLOR` · hash `0x2867ED8C` · **Cliente**

```lua
ClearVehicleXenonLightsCustomColor(vehicle)
```
```c
void CLEAR_VEHICLE_XENON_LIGHTS_CUSTOM_COLOR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.

**Devuelve:** `void`

**Descripción oficial:**

Removes vehicle xenon lights custom RGB color.

---
### CloneTimecycleModifier

`CLONE_TIMECYCLE_MODIFIER` · hash `0x54D636B3` · **Cliente**

```lua
local retval = CloneTimecycleModifier(sourceModifierName, clonedModifierName)
```
```c
int CLONE_TIMECYCLE_MODIFIER(char* sourceModifierName, char* clonedModifierName);
```

**Parámetros**

- `sourceModifierName` (`char*`): The source timecycle name.
- `clonedModifierName` (`char*`): The clone timecycle name, must be unique.

**Devuelve:** `int` — The cloned timecycle modifier index, or -1 if failed.

**Ejemplo (lua):**

```lua
local sourceName = "underwater"
local cloneName = "my_awesome_timecycle"

local clonedIndex = CloneTimecycleModifier(sourceName, cloneName)
if clonedIndex ~= -1 then
  SetTimecycleModifier(cloneName)
end
```

---
### CommitRuntimeTexture

`COMMIT_RUNTIME_TEXTURE` · hash `0x19D81F4E` · **Cliente**

```lua
CommitRuntimeTexture(tex)
```
```c
void COMMIT_RUNTIME_TEXTURE(long tex);
```

**Parámetros**

- `tex` (`long`): The runtime texture handle.

**Devuelve:** `void`

**Descripción oficial:**

Commits the backing pixels to the specified runtime texture.

---
### CreateAudioSubmix

`CREATE_AUDIO_SUBMIX` · hash `0x658D2BC8` · **Cliente**

```lua
local retval = CreateAudioSubmix(name)
```
```c
int CREATE_AUDIO_SUBMIX(char* name);
```

**Parámetros**

- `name` (`char*`): The audio submix name.

**Devuelve:** `int` — A submix ID, or -1 if the submix could not be created.

**Descripción oficial:**

Creates an audio submix with the specified name, or gets the existing audio submix by that name.

---
### CreateDryVolume

`CREATE_DRY_VOLUME` · hash `0xEB1C6DD` · **Cliente**

```lua
local retval = CreateDryVolume(xMin, yMin, zMin, xMax, yMax, zMax)
```
```c
int CREATE_DRY_VOLUME(float xMin, float yMin, float zMin, float xMax, float yMax, float zMax);
```

**Parámetros**

- `xMin` (`float`): The min X component of the AABB volume where water does not affect the player.
- `yMin` (`float`): The min Y component for the AABB volume.
- `zMin` (`float`): The min Z component for the AABB volume.
- `xMax` (`float`): The max X component for the AABB volume.
- `yMax` (`float`): The max Y component for the AABB volume.
- `zMax` (`float`): The max Z component for the AABB volume.

**Devuelve:** `int`

**Descripción oficial:**

Creates a volume where water effects do not apply.
Useful for preventing water collisions from flooding areas underneath them.
This has no effect on waterquads, only water created from drawables and collisions.
Don't create volumes when your local ped is swimming (e.g. use IS_PED_SWIMMING in your scripts before you call this)

---
### CreateDui

`CREATE_DUI` · hash `0x23EAF899` · **Cliente**

```lua
local retval = CreateDui(url, width, height)
```
```c
long CREATE_DUI(char* url, int width, int height);
```

**Parámetros**

- `url` (`char*`): The initial URL to load in the browser.
- `width` (`int`): The width of the backing surface.
- `height` (`int`): The height of the backing surface.

**Devuelve:** `long` — A DUI object.

**Descripción oficial:**

Creates a DUI browser. This can be used to draw on a runtime texture using CREATE_RUNTIME_TEXTURE_FROM_DUI_HANDLE.

---
### CreateRuntimeTexture

`CREATE_RUNTIME_TEXTURE` · hash `0xFEC3766D` · **Cliente**

```lua
local retval = CreateRuntimeTexture(txd, txn, width, height)
```
```c
long CREATE_RUNTIME_TEXTURE(long txd, char* txn, int width, int height);
```

**Parámetros**

- `txd` (`long`): A handle to the runtime TXD to create the runtime texture in.
- `txn` (`char*`): The name for the texture in the runtime texture dictionary.
- `width` (`int`): The width of the new texture.
- `height` (`int`): The height of the new texture.

**Devuelve:** `long` — A runtime texture handle.

**Descripción oficial:**

Creates a blank runtime texture.

---
### CreateRuntimeTextureFromDuiHandle

`CREATE_RUNTIME_TEXTURE_FROM_DUI_HANDLE` · hash `0xB135472B` · **Cliente**

```lua
local retval = CreateRuntimeTextureFromDuiHandle(txd, txn, duiHandle)
```
```c
long CREATE_RUNTIME_TEXTURE_FROM_DUI_HANDLE(long txd, char* txn, char* duiHandle);
```

**Parámetros**

- `txd` (`long`): A handle to the runtime TXD to create the runtime texture in.
- `txn` (`char*`): The name for the texture in the runtime texture dictionary.
- `duiHandle` (`char*`): The DUI handle returned from GET_DUI_HANDLE.

**Devuelve:** `long` — The runtime texture handle.

**Descripción oficial:**

Creates a runtime texture from a DUI handle.

---
### CreateRuntimeTextureFromImage

`CREATE_RUNTIME_TEXTURE_FROM_IMAGE` · hash `0x786D8BC3` · **Cliente**

```lua
local retval = CreateRuntimeTextureFromImage(txd, txn, fileName)
```
```c
long CREATE_RUNTIME_TEXTURE_FROM_IMAGE(long txd, char* txn, char* fileName);
```

**Parámetros**

- `txd` (`long`): A handle to the runtime TXD to create the runtime texture in.
- `txn` (`char*`): The name for the texture in the runtime texture dictionary.
- `fileName` (`char*`): The file name of an image to load or a base64 data URL. This should preferably be a PNG, and has to be specified as a `file` in the resource manifest.

**Devuelve:** `long` — A runtime texture handle.

**Descripción oficial:**

Creates a runtime texture from the specified file in the current resource or a base64 data URL.

---
### CreateRuntimeTxd

`CREATE_RUNTIME_TXD` · hash `0x1F3AC778` · **Cliente**

```lua
local retval = CreateRuntimeTxd(name)
```
```c
long CREATE_RUNTIME_TXD(char* name);
```

**Parámetros**

- `name` (`char*`): The name for the runtime TXD.

**Devuelve:** `long` — A handle to the runtime TXD.

**Descripción oficial:**

Creates a runtime texture dictionary with the specified name.
Example:

```lua
local txd = CreateRuntimeTxd('meow')
```

---
### CreateTimecycleModifier

`CREATE_TIMECYCLE_MODIFIER` · hash `0x70FA2AFA` · **Cliente**

```lua
local retval = CreateTimecycleModifier(modifierName)
```
```c
int CREATE_TIMECYCLE_MODIFIER(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`): The new timecycle name, must be unique.

**Devuelve:** `int` — The created timecycle modifier index, or -1 if failed.

**Descripción oficial:**

Create a clean timecycle modifier. See [`SET_TIMECYCLE_MODIFIER_VAR`](#settimecyclemodifiervar) to add variables.

**Ejemplo (lua):**

```lua
local modifierName = "my_awesome_timecycle"
local createdIndex = CreateTimecycleModifier(modifierName)

if createdIndex ~= -1 then
  SetTimecycleModifier(modifierName)
end
```

---
### DestroyDui

`DESTROY_DUI` · hash `0xA085CB10` · **Cliente**

```lua
DestroyDui(duiObject)
```
```c
void DESTROY_DUI(long duiObject);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.

**Devuelve:** `void`

**Descripción oficial:**

Destroys a DUI browser.

---
### DisableEditorRuntime

`DISABLE_EDITOR_RUNTIME` · hash `0xB1622B17` · **Cliente**

```lua
DisableEditorRuntime()
```
```c
void DISABLE_EDITOR_RUNTIME();
```

**Devuelve:** `void`

**Descripción oficial:**

Disables the editor runtime mode, changing game behavior to not track entity metadata.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### DisableIdleCamera

`DISABLE_IDLE_CAMERA` · hash `0x3D5AB7F0` · **Cliente**

```lua
DisableIdleCamera(state)
```
```c
void DISABLE_IDLE_CAMERA(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): On/Off

**Devuelve:** `void`

**Descripción oficial:**

Disables the game's afk camera that starts panning around after 30 seconds of inactivity.

---
### DisableRawKeyThisFrame

`DISABLE_RAW_KEY_THIS_FRAME` · hash `0x8BCF0014` · **Cliente**

```lua
local retval = DisableRawKeyThisFrame(rawKeyIndex)
```
```c
BOOL DISABLE_RAW_KEY_THIS_FRAME(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of down state.

**Descripción oficial:**

Disables the specified `rawKeyIndex`, making it not trigger the regular `IS_RAW_KEY_*` natives.

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
local KEY_SPACE = 32
DisableRawKeyThisFrame(KEY_SPACE)
-- This will not get triggered this frame
if IsRawKeyDown(KEY_SPACE) then
	print("unreachable :(")
end
-- this will get triggered
if IsDisabledRawKeyDown(KEY_SPACE) then
    print("Spacebar is down")
end
```

---
### DisableVehiclePassengerIdleCamera

`DISABLE_VEHICLE_PASSENGER_IDLE_CAMERA` · hash `0x5C140555` · **Cliente**

```lua
DisableVehiclePassengerIdleCamera(state)
```
```c
void DISABLE_VEHICLE_PASSENGER_IDLE_CAMERA(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): On/Off

**Devuelve:** `void`

**Descripción oficial:**

Disables the game's afk camera that starts panning around after 30 seconds of inactivity(While riding in a car as a passenger)

---
### DisableWorldhorizonRendering

`DISABLE_WORLDHORIZON_RENDERING` · hash `0xA9C92CDC` · **Cliente**

```lua
DisableWorldhorizonRendering(state)
```
```c
void DISABLE_WORLDHORIZON_RENDERING(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): On/Off

**Devuelve:** `void`

**Descripción oficial:**

Disables the game's world horizon lods rendering (see `farlods.#dd`).
Using the island hopper natives might also affect this state.

---
### DoesTimecycleModifierHasVar

`DOES_TIMECYCLE_MODIFIER_HAS_VAR` · hash `0xC53BB6D3` · **Cliente**

```lua
local retval = DoesTimecycleModifierHasVar(modifierName, varName)
```
```c
BOOL DOES_TIMECYCLE_MODIFIER_HAS_VAR(char* modifierName, char* varName);
```

**Parámetros**

- `modifierName` (`char*`): The name of timecycle modifier.
- `varName` (`char*`): The name of timecycle variable.

**Devuelve:** `BOOL` — Whether or not variable by name was found on the specified timecycle modifier.

**Ejemplo (lua):**

```lua
local modifierName = "superDARK"
local varName = "postfx_noise"

if DoesTimecycleModifierHasVar(modifierName, varName) then
  local success, value1, value2 = GetTimecycleModifierVar(modifierName, varName)

  if success then
    print(string.format("[%s] removed var %s with values: %f %f", modifierName, varName, value1, value2))
    RemoveTimecycleModifierVar(modifierName, varName)
  end
else
    SetTimecycleModifierVar(modifierName, varName, 1.0, 1.0)
    print(string.format("[%s] created var %s", modifierName, varName))
end
```

---
### DoesVehicleUseFuel

`DOES_VEHICLE_USE_FUEL` · hash `0xEF30A696` · **Cliente**

```lua
local retval = DoesVehicleUseFuel(vehicle)
```
```c
BOOL DOES_VEHICLE_USE_FUEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.

**Devuelve:** `BOOL` — True if the vehicle uses fuel to move. False otherwise.

**Descripción oficial:**

Checks whether the vehicle consumes fuel. The check is done based on petrol tank volume and vehicle type. Bicycles and vehicles with petrol tank volume equal to zero (only bicycles by default) do not use fuel. All other vehicles do.

You can customize petrol tank volume using [`SET_HANDLING_FLOAT`](#sethandlingfloat)/[`SET_VEHICLE_HANDLING_FLOAT`](#setvehiclehandlingfloat) natives with `fieldName` equal to `fPetrolTankVolume`.

---
### DoorSystemGetActive

`DOOR_SYSTEM_GET_ACTIVE` · hash `0xF65BBA4B` · **Cliente**

```lua
local retval = DoorSystemGetActive()
```
```c
object DOOR_SYSTEM_GET_ACTIVE();
```

**Devuelve:** `object` — An object containing a list of door system entries.

**Descripción oficial:**

Returns a list of door system entries: a door system hash (see [ADD_DOOR_TO_SYSTEM](../gta5/OBJECT.md#adddoortosystem)) and its object handle.

The data returned adheres to the following layout:

```
[{doorHash1, doorHandle1}, ..., {doorHashN, doorHandleN}]
```

---
### DoorSystemGetSize

`DOOR_SYSTEM_GET_SIZE` · hash `0x237613B3` · **Cliente**

```lua
local retval = DoorSystemGetSize()
```
```c
int DOOR_SYSTEM_GET_SIZE();
```

**Devuelve:** `int` — The number of doors registered in the system

---
### DrawCorona

`DRAW_CORONA` · hash `0xFF44780E` · **Cliente**

```lua
DrawCorona(posX, posY, posZ, size, alpha, red, green, blue, intensity, zBias, dirX, dirY, dirZ, viewThreshold, innerAngle, outerAngle, flags)
```
```c
void DRAW_CORONA(float posX, float posY, float posZ, float size, int alpha, int red, int green, int blue, float intensity, float zBias, float dirX, float dirY, float dirZ, float viewThreshold, float innerAngle, float outerAngle, int flags);
```

**Parámetros**

- `posX` (`float`): The X position of the corona origin.
- `posY` (`float`): The Y position of the corona origin.
- `posZ` (`float`): The Z position of the corona origin.
- `size` (`float`): The size of the corona.
- `alpha` (`int`): The alpha component of the marker color, on a scale from 0-255.
- `red` (`int`): The red component of the marker color, on a scale from 0-255.
- `green` (`int`): The green component of the marker color, on a scale from 0-255.
- `blue` (`int`): The blue component of the marker color, on a scale from 0-255.
- `intensity` (`float`): The intensity of the corona.
- `zBias` (`float`): zBias slightly shifts the depth of surfaces to make sure they don’t overlap or cause visual glitches when they are very close together. The zBias value are usually in the range of 0.0 to 1.0.
- `dirX` (`float`): The X direction of the corona.
- `dirY` (`float`): The Y direction of the corona.
- `dirZ` (`float`): The Z direction of the corona.
- `viewThreshold` (`float`): The view threshold is to determine the fading of the corona based on the distance.
- `innerAngle` (`float`): The inner angle of the corona.
- `outerAngle` (`float`): The outer angle of the corona.
- `flags` (`int`): The corona flags.

**Devuelve:** `void`

**Descripción oficial:**

Allows drawing advanced light effects, known as coronas, which support flares, volumetric lighting, and customizable glow properties.

**Ejemplo (lua):**

```lua
local pedCoords = GetEntityCoords(PlayerPedId())
Citizen.CreateThread(function()
    while true do
        DrawCorona(pedCoords.x, pedCoords.y, pedCoords.z, 5.0, 255, 255, 255, 255, 4.0, 0.2, pedCoords.x, pedCoords.y, pedCoords.z, 1.0, 0.0, 90.0, 2)
        Wait(0)
    end
end)
```

---
### DrawGizmo

`DRAW_GIZMO` · hash `0xEB2EDCA2` · **Cliente**

```lua
local retval = DrawGizmo(matrixPtr, id)
```
```c
BOOL DRAW_GIZMO(long matrixPtr, char* id);
```

**Parámetros**

- `matrixPtr` (`long`): A mutable pointer to a 64-byte buffer of floating-point values, representing an XMFLOAT4X4 in layout.
- `id` (`char*`): A unique identifier of what the gizmo is affecting.

**Devuelve:** `BOOL` — Whether or not the matrix was modified.

**Descripción oficial:**

Draws a gizmo. This function supports SDK infrastructure and is not intended to be used directly from your code.

This should be used from JavaScript or another language supporting mutable buffers like ArrayBuffer.

Matrix layout is as follows:

*   Element \[0], \[1] and \[2] should represent the right vector.
*   Element \[4], \[5] and \[6] should represent the forward vector.
*   Element \[8], \[9] and \[10] should represent the up vector.
*   Element \[12], \[13] and \[14] should represent X, Y and Z translation coordinates.
*   All other elements should be \[0, 0, 0, 1].

---
### DrawGlowSphere

`DRAW_GLOW_SPHERE` · hash `0xBD25EC89` · **Cliente**

```lua
DrawGlowSphere(posX, posY, posZ, radius, colorR, colorG, colorB, intensity, invert, marker)
```
```c
void DRAW_GLOW_SPHERE(float posX, float posY, float posZ, float radius, int colorR, int colorG, int colorB, float intensity, BOOL invert, BOOL marker);
```

**Parámetros**

- `posX` (`float`): Position X.
- `posY` (`float`): Position Y.
- `posZ` (`float`): Position Z.
- `radius` (`float`): Sphere radius.
- `colorR` (`int`): Red.
- `colorG` (`int`): Green.
- `colorB` (`int`): Blue.
- `intensity` (`float`): Intensity.
- `invert` (`BOOL`): Invert rendering.
- `marker` (`BOOL`): Draw as a marker, otherwise as an overlay.

**Devuelve:** `void`

**Descripción oficial:**

Draw a glow sphere this frame. Up to 256 per single frame.

---
### DrawLight

`DRAW_LIGHT` · hash `0x374E5298` · **Cliente**

```lua
DrawLight()
```
```c
void DRAW_LIGHT();
```

**Devuelve:** `void`

**Descripción oficial:**

Draw the prepared light.

---
### DrawLine_2d

`DRAW_LINE_2D` · hash `0xB856A90` · **Cliente**

```lua
DrawLine_2d(x1, y1, x2, y2, width, r, g, b, a)
```
```c
void DRAW_LINE_2D(float x1, float y1, float x2, float y2, float width, int r, int g, int b, int a);
```

**Parámetros**

- `x1` (`float`): First x.
- `y1` (`float`): First y.
- `x2` (`float`): Second x.
- `y2` (`float`): Second y.
- `width` (`float`): Width of line.
- `r` (`int`): Red.
- `g` (`int`): Green.
- `b` (`int`): Blue.
- `a` (`int`): Alpha.

**Devuelve:** `void`

**Descripción oficial:**

Like DRAW_RECT, but it's a line.

---
### DrawRectRotated

`DRAW_RECT_ROTATED` · hash `0xEC37C168` · **Cliente**

```lua
DrawRectRotated(x, y, width, height, rotation, r, g, b, a)
```
```c
void DRAW_RECT_ROTATED(float x, float y, float width, float height, float rotation, int r, int g, int b, int a);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `width` (`float`)
- `height` (`float`)
- `rotation` (`float`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

DRAW_RECT, but with a rotation. Seems to be broken.

---
### EnableEditorRuntime

`ENABLE_EDITOR_RUNTIME` · hash `0xC383871D` · **Cliente**

```lua
EnableEditorRuntime()
```
```c
void ENABLE_EDITOR_RUNTIME();
```

**Devuelve:** `void`

**Descripción oficial:**

Enables the editor runtime mode, changing game behavior to track entity metadata.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### EndFindObject

`END_FIND_OBJECT` · hash `0xDEDA4E50` · **Cliente**

```lua
EndFindObject(findHandle)
```
```c
void END_FIND_OBJECT(int findHandle);
```

**Parámetros**

- `findHandle` (`int`)

**Devuelve:** `void`

---
### EndFindPed

`END_FIND_PED` · hash `0x9615C2AD` · **Cliente**

```lua
EndFindPed(findHandle)
```
```c
void END_FIND_PED(int findHandle);
```

**Parámetros**

- `findHandle` (`int`)

**Devuelve:** `void`

---
### EndFindPickup

`END_FIND_PICKUP` · hash `0x3C407D53` · **Cliente**

```lua
EndFindPickup(findHandle)
```
```c
void END_FIND_PICKUP(int findHandle);
```

**Parámetros**

- `findHandle` (`int`)

**Devuelve:** `void`

---
### EndFindVehicle

`END_FIND_VEHICLE` · hash `0x9227415A` · **Cliente**

```lua
EndFindVehicle(findHandle)
```
```c
void END_FIND_VEHICLE(int findHandle);
```

**Parámetros**

- `findHandle` (`int`)

**Devuelve:** `void`

---
### EnterCursorMode

`ENTER_CURSOR_MODE` · hash `0x780DA86` · **Cliente**

```lua
EnterCursorMode()
```
```c
void ENTER_CURSOR_MODE();
```

**Devuelve:** `void`

**Descripción oficial:**

Enters cursor mode, suppressing mouse movement to the game and displaying a mouse cursor instead. This function supports
SDK infrastructure and is not intended to be used directly from your code.

---
### ExperimentalLoadCloneCreate

`EXPERIMENTAL_LOAD_CLONE_CREATE` · hash `0xD2CB95A3` · **Cliente**

```lua
local retval = ExperimentalLoadCloneCreate(data, objectId, tree)
```
```c
Entity EXPERIMENTAL_LOAD_CLONE_CREATE(char* data, int objectId, char* tree);
```

**Parámetros**

- `data` (`char*`)
- `objectId` (`int`)
- `tree` (`char*`)

**Devuelve:** `Entity`

**Descripción oficial:**

This native is not implemented.

---
### ExperimentalLoadCloneSync

`EXPERIMENTAL_LOAD_CLONE_SYNC` · hash `0x6BC189AC` · **Cliente**

```lua
ExperimentalLoadCloneSync(entity, data)
```
```c
void EXPERIMENTAL_LOAD_CLONE_SYNC(Entity entity, char* data);
```

**Parámetros**

- `entity` (`Entity`)
- `data` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

This native is not implemented.

---
### ExperimentalSaveCloneCreate

`EXPERIMENTAL_SAVE_CLONE_CREATE` · hash `0x9D65CAD2` · **Cliente**

```lua
local retval = ExperimentalSaveCloneCreate(entity)
```
```c
char* EXPERIMENTAL_SAVE_CLONE_CREATE(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `char*`

**Descripción oficial:**

This native is not implemented.

---
### ExperimentalSaveCloneSync

`EXPERIMENTAL_SAVE_CLONE_SYNC` · hash `0x38D19210` · **Cliente**

```lua
local retval = ExperimentalSaveCloneSync(entity)
```
```c
char* EXPERIMENTAL_SAVE_CLONE_SYNC(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `char*`

**Descripción oficial:**

This native is not implemented.

---
### FindFirstObject

`FIND_FIRST_OBJECT` · hash `0xFAA6CB5D` · **Cliente**

```lua
local retval, outEntity = FindFirstObject(outEntity)
```
```c
int FIND_FIRST_OBJECT(Entity* outEntity);
```

**Parámetros**

- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

---
### FindFirstPed

`FIND_FIRST_PED` · hash `0xFB012961` · **Cliente**

```lua
local retval, outEntity = FindFirstPed(outEntity)
```
```c
int FIND_FIRST_PED(Entity* outEntity);
```

**Parámetros**

- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

---
### FindFirstPickup

`FIND_FIRST_PICKUP` · hash `0x3FF9D340` · **Cliente**

```lua
local retval, outEntity = FindFirstPickup(outEntity)
```
```c
int FIND_FIRST_PICKUP(Entity* outEntity);
```

**Parámetros**

- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

---
### FindFirstVehicle

`FIND_FIRST_VEHICLE` · hash `0x15E55694` · **Cliente**

```lua
local retval, outEntity = FindFirstVehicle(outEntity)
```
```c
int FIND_FIRST_VEHICLE(Entity* outEntity);
```

**Parámetros**

- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

---
### FindNextObject

`FIND_NEXT_OBJECT` · hash `0x4E129DBF` · **Cliente**

```lua
local retval, outEntity = FindNextObject(findHandle, outEntity)
```
```c
BOOL FIND_NEXT_OBJECT(int findHandle, Entity* outEntity);
```

**Parámetros**

- `findHandle` (`int`)
- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### FindNextPed

`FIND_NEXT_PED` · hash `0xAB09B548` · **Cliente**

```lua
local retval, outEntity = FindNextPed(findHandle, outEntity)
```
```c
BOOL FIND_NEXT_PED(int findHandle, Entity* outEntity);
```

**Parámetros**

- `findHandle` (`int`)
- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### FindNextPickup

`FIND_NEXT_PICKUP` · hash `0x4107EF0F` · **Cliente**

```lua
local retval, outEntity = FindNextPickup(findHandle, outEntity)
```
```c
BOOL FIND_NEXT_PICKUP(int findHandle, Entity* outEntity);
```

**Parámetros**

- `findHandle` (`int`)
- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### FindNextVehicle

`FIND_NEXT_VEHICLE` · hash `0x8839120D` · **Cliente**

```lua
local retval, outEntity = FindNextVehicle(findHandle, outEntity)
```
```c
BOOL FIND_NEXT_VEHICLE(int findHandle, Entity* outEntity);
```

**Parámetros**

- `findHandle` (`int`)
- `outEntity` (`Entity*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### ForceSnowPass

`FORCE_SNOW_PASS` · hash `0xE6E16170` · **Cliente**

```lua
ForceSnowPass(enabled)
```
```c
void FORCE_SNOW_PASS(BOOL enabled);
```

**Parámetros**

- `enabled` (`BOOL`): Whether or not to force rendering to use a snow pass.

**Devuelve:** `void`

**Descripción oficial:**

Forces the game snow pass to render.

---
### GetActivePlayers

`GET_ACTIVE_PLAYERS` · hash `0xCF143FB9` · **Cliente**

```lua
local retval = GetActivePlayers()
```
```c
object GET_ACTIVE_PLAYERS();
```

**Devuelve:** `object` — An object containing a list of player indices.

**Descripción oficial:**

Returns all player indices for 'active' physical players known to the client.
The data returned adheres to the following layout:

```
[127, 42, 13, 37]
```

---
### GetAllRopes

`GET_ALL_ROPES` · hash `0x760A2D67` · **Cliente**

```lua
local retval = GetAllRopes()
```
```c
object GET_ALL_ROPES();
```

**Devuelve:** `object` — An object containing a list of all rope handles.

**Descripción oficial:**

Returns all rope handles. The data returned adheres to the following layout:

```
[ 770, 1026, 1282, 1538, 1794, 2050, 2306, 2562, 2818, 3074, 3330, 3586, 3842, 4098, 4354, 4610, ...]
```

---
### GetAllTrackJunctions

`GET_ALL_TRACK_JUNCTIONS` · hash `0x81A08523` · **Cliente**

```lua
local retval = GetAllTrackJunctions()
```
```c
object GET_ALL_TRACK_JUNCTIONS();
```

**Devuelve:** `object` — An object containing a list of track junctions ids.``` ```

**Descripción oficial:**

Returns all track junctions on the client
The data returned adheres to the following structure:

```
[1, 2, 4, 6, 69, 420]
```

---
### GetAllVehicleModels

`GET_ALL_VEHICLE_MODELS` · hash `0xD7531645` · **Cliente**

```lua
local retval = GetAllVehicleModels()
```
```c
object GET_ALL_VEHICLE_MODELS();
```

**Devuelve:** `object`

**Descripción oficial:**

Returns all registered vehicle model names, including non-dlc vehicles and custom vehicles in no particular order.

**Example output**

```
	["dubsta", "dubsta2", "dubsta3", "myverycoolcar", "sultan", "sultanrs", ...]
```

This native will not return vehicles that are unregistered (i.e from a resource being stopped) during runtime.

**Ejemplo (lua):**

```lua
RegisterCommand("spawnrandomcar", function()
	local vehicles = GetAllVehicleModels()
	local veh = vehicles[math.random(1, #vehicles)]
	RequestModel(veh)
	repeat Wait(0) until HasModelLoaded(veh)
	local veh = CreateVehicle(veh, GetEntityCoords(PlayerPedId()), GetEntityHeading(PlayerPedId()), true, false)
	SetPedIntoVehicle(PlayerPedId(), veh, -1)
end)
```

---
### GetAmbientPedRangeMultiplier

`GET_AMBIENT_PED_RANGE_MULTIPLIER` · hash `0xB550232D` · **Cliente**

```lua
local retval = GetAmbientPedRangeMultiplier()
```
```c
float GET_AMBIENT_PED_RANGE_MULTIPLIER();
```

**Devuelve:** `float` — Returns ambient ped range multiplier value.

**Descripción oficial:**

A getter for [SET_AMBIENT_PED_RANGE_MULTIPLIER_THIS_FRAME](../gta5/PATHFIND.md#setambientpedrangemultiplierthisframe).

---
### GetAmbientVehicleRangeMultiplier

`GET_AMBIENT_VEHICLE_RANGE_MULTIPLIER` · hash `0x667EC929` · **Cliente**

```lua
local retval = GetAmbientVehicleRangeMultiplier()
```
```c
float GET_AMBIENT_VEHICLE_RANGE_MULTIPLIER();
```

**Devuelve:** `float` — Returns ambient vehicle range multiplier value.

**Descripción oficial:**

A getter for [SET_AMBIENT_VEHICLE_RANGE_MULTIPLIER_THIS_FRAME](../gta5/VEHICLE-1.md#setambientvehiclerangemultiplierthisframe).

---
### GetCalmingQuadAtCoords

`GET_CALMING_QUAD_AT_COORDS` · hash `0x870E8B40` · **Cliente**

```lua
local retval = GetCalmingQuadAtCoords(x, y)
```
```c
int GET_CALMING_QUAD_AT_COORDS(float x, float y);
```

**Parámetros**

- `x` (`float`): The X coordinate
- `y` (`float`): The Y coordinate

**Devuelve:** `int` — The calming quad index at the given position. Returns -1 if there isn't any there.

**Descripción oficial:**

This native returns the index of a calming quad if the given point is inside its bounds.

**Ejemplo (lua):**

```lua
local currentPedPosition = GetEntityCoords(PlayerPedId())
local calmingQuadIndex = GetCalmingQuadAtCoords(currentPedPosition.x, currentPedPosition.y)
```

---
### GetCalmingQuadBounds

`GET_CALMING_QUAD_BOUNDS` · hash `0xFF60E63` · **Cliente**

```lua
local retval, minX, minY, maxX, maxY = GetCalmingQuadBounds(waterQuad)
```
```c
BOOL GET_CALMING_QUAD_BOUNDS(int waterQuad, int* minX, int* minY, int* maxX, int* maxY);
```

**Parámetros**

- `waterQuad` (`int`): The calming quad index
- `minX` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The minX coordinate
- `minY` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The minY coordinate
- `maxX` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The maxX coordinate
- `maxY` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The maxY coordinate

**Devuelve:** `BOOL` — Returns true on success. Bounds are undefined on failure

**Ejemplo (lua):**

```lua
local success, minX, minY, maxX, maxY = GetCalmingQuadBounds(1)
```

---
### GetCalmingQuadCount

`GET_CALMING_QUAD_COUNT` · hash `0xCEBFC42` · **Cliente**

```lua
local retval = GetCalmingQuadCount()
```
```c
int GET_CALMING_QUAD_COUNT();
```

**Devuelve:** `int` — Returns the amount of calming quads loaded.

**Ejemplo (lua):**

```lua
local calmingQuadCount = GetCalmingQuadCount()
```

---
### GetCalmingQuadDampening

`GET_CALMING_QUAD_DAMPENING` · hash `0xB0E3A058` · **Cliente**

```lua
local retval, calmingQuadDampening = GetCalmingQuadDampening(waterQuad, calmingQuadDampening)
```
```c
BOOL GET_CALMING_QUAD_DAMPENING(int waterQuad, float* calmingQuadDampening);
```

**Parámetros**

- `waterQuad` (`int`): The calming quad index
- `calmingQuadDampening` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns true on success. Dampening value is undefined on failure

**Ejemplo (lua):**

```lua
local success, dampening = GetCalmingQuadDampening(1)
```

---
### GetCamMatrix

`GET_CAM_MATRIX` · hash `0x8F57A89D` · **Cliente**

```lua
local rightVector, forwardVector, upVector, position = GetCamMatrix(camera)
```
```c
void GET_CAM_MATRIX(Cam camera, Vector3* rightVector, Vector3* forwardVector, Vector3* upVector, Vector3* position);
```

**Parámetros**

- `camera` (`Cam`)
- `rightVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `forwardVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `upVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `position` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

Returns the world matrix of the specified camera. To turn this into a view matrix, calculate the inverse.

---
### GetClosestTrackNodes

`GET_CLOSEST_TRACK_NODES` · hash `0x59FC24A7` · **Cliente**

```lua
local retval = GetClosestTrackNodes(position, radius)
```
```c
object GET_CLOSEST_TRACK_NODES(Vector3 position, float radius);
```

**Parámetros**

- `position` (`Vector3`): Get track nodes at position
- `radius` (`float`): Get track nodes within radius

**Devuelve:** `object` — Returns a list of tracks and node entries: a trackNode and a trackIdThe data returned adheres to the following layout:    [{trackNode1, trackId1}, ..., {trackNodeN, trackIdN}]

**Descripción oficial:**

Get all track nodes and their track ids within the radius of the specified coordinates.

---
### GetCurrentGameName

`GET_CURRENT_GAME_NAME` · hash `0xACA18ECD` · **Cliente**

```lua
local retval = GetCurrentGameName()
```
```c
char* GET_CURRENT_GAME_NAME();
```

**Devuelve:** `char*` — The game name as a string, one of the following values: gta4, gta5, rdr3

**Descripción oficial:**

This native returns the currently used game's name.

---
### GetCurrentServerEndpoint

`GET_CURRENT_SERVER_ENDPOINT` · hash `0xEA11BFBA` · **Cliente**

```lua
local retval = GetCurrentServerEndpoint()
```
```c
char* GET_CURRENT_SERVER_ENDPOINT();
```

**Devuelve:** `char*` — The peer address of the game server (e.g. `127.0.0.1:30120`), or NULL if not available.

**Descripción oficial:**

Returns the peer address of the remote game server that the user is currently connected to.

---
### GetDuiHandle

`GET_DUI_HANDLE` · hash `0x1655D41D` · **Cliente**

```lua
local retval = GetDuiHandle(duiObject)
```
```c
char* GET_DUI_HANDLE(long duiObject);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.

**Devuelve:** `char*` — The NUI window handle, for use in e.g. CREATE_RUNTIME_TEXTURE_FROM_DUI_HANDLE.

**Descripción oficial:**

Returns the NUI window handle for a specified DUI browser object.

---
### GetEntityAddress

`GET_ENTITY_ADDRESS` · hash `0x9A3144BC` · **Cliente**

```lua
local retval = GetEntityAddress(entity)
```
```c
Any* GET_ENTITY_ADDRESS(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The handle of the entity to get the address of.

**Devuelve:** `Any*` — A pointer containing the memory address of the entity.

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Returns the memory address of an entity.

This native is intended for singleplayer debugging, and may not be available during multiplayer.

---
### GetEntityArchetypeName

`GET_ENTITY_ARCHETYPE_NAME` · hash `0x47B870F5` · **Cliente**

```lua
local retval = GetEntityArchetypeName(entity)
```
```c
char* GET_ENTITY_ARCHETYPE_NAME(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): An entity handle.

**Devuelve:** `char*` — Entity's archetype name

**Descripción oficial:**

Returns entity's archetype name, if available.

---
### GetEntityIndexFromMapdata

`GET_ENTITY_INDEX_FROM_MAPDATA` · hash `0xEE43540D` · **Cliente**

```lua
local retval = GetEntityIndexFromMapdata(mapdata, entity)
```
```c
int GET_ENTITY_INDEX_FROM_MAPDATA(int mapdata, int entity);
```

**Parámetros**

- `mapdata` (`int`): The input map data index from GET_MAPDATA_FROM_HASH_KEY.
- `entity` (`int`): The input entity handle from GET_ENTITY_MAPDATA_OWNER.

**Devuelve:** `int` — A transient (non-persistable) index to the requested entity, or -1.

**Descripción oficial:**

Returns the transient entity index for a specified mapdata/entity pair.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### GetEntityMapdataOwner

`GET_ENTITY_MAPDATA_OWNER` · hash `0xF6B815C5` · **Cliente**

```lua
local retval, mapdataHandle, entityHandle = GetEntityMapdataOwner(entity)
```
```c
BOOL GET_ENTITY_MAPDATA_OWNER(Entity entity, int* mapdataHandle, int* entityHandle);
```

**Parámetros**

- `entity` (`Entity`): An entity owned by map data.
- `mapdataHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The output map data handle.
- `entityHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The output entity handle.

**Devuelve:** `BOOL` — True if successful, false if not.

**Descripción oficial:**

Retrieves the map data and entity handles from a specific entity.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### GetExternalKvpFloat

`GET_EXTERNAL_KVP_FLOAT` · hash `0x3CC98B25` · **Cliente**

```lua
local retval = GetExternalKvpFloat(resource, key)
```
```c
float GET_EXTERNAL_KVP_FLOAT(char* resource, char* key);
```

**Parámetros**

- `resource` (`char*`): The resource to fetch from.
- `key` (`char*`): The key to fetch

**Devuelve:** `float` — A float that contains the value stored in the Kvp or nil/null if none.

**Descripción oficial:**

A getter for [SET_RESOURCE_KVP_FLOAT](compartidos.md#setresourcekvpfloat), but for a specified resource.

**Ejemplo (lua):**

```lua
local kvpValue = GetExternalKvpFloat('drugs', 'mollis') 
if kvpValue then
	-- do something!
end
```

---
### GetExternalKvpInt

`GET_EXTERNAL_KVP_INT` · hash `0x12B8D689` · **Cliente**

```lua
local retval = GetExternalKvpInt(resource, key)
```
```c
int GET_EXTERNAL_KVP_INT(char* resource, char* key);
```

**Parámetros**

- `resource` (`char*`): The resource to fetch from.
- `key` (`char*`): The key to fetch

**Devuelve:** `int` — A int that contains the value stored in the Kvp or nil/null if none.

**Descripción oficial:**

A getter for [SET_RESOURCE_KVP_INT](compartidos.md#setresourcekvpint), but for a specified resource.

**Ejemplo (lua):**

```lua
local kvpValue = GetExternalKvpInt('food', 'bananabread') 
if kvpValue then
	-- do something!
end
```

---
### GetExternalKvpString

`GET_EXTERNAL_KVP_STRING` · hash `0x9080363A` · **Cliente**

```lua
local retval = GetExternalKvpString(resource, key)
```
```c
char* GET_EXTERNAL_KVP_STRING(char* resource, char* key);
```

**Parámetros**

- `resource` (`char*`): The resource to fetch from.
- `key` (`char*`): The key to fetch

**Devuelve:** `char*` — A string that contains the value stored in the Kvp or nil/null if none.

**Descripción oficial:**

A getter for [SET_RESOURCE_KVP](compartidos.md#setresourcekvp), but for a specified resource.

**Ejemplo (lua):**

```lua
local kvpValue = GetExternalKvpString('food', 'codfish') 
if kvpValue then
	-- do something!
end
```

---
### GetFallDamageLandOnFootMultiplier

`GET_FALL_DAMAGE_LAND_ON_FOOT_MULTIPLIER` · hash `0x2C048945` · **Cliente**

```lua
local retval = GetFallDamageLandOnFootMultiplier()
```
```c
float GET_FALL_DAMAGE_LAND_ON_FOOT_MULTIPLIER();
```

**Devuelve:** `float` — Returns the fall damage multiplier applied when a ped lands **on foot** from a fall below the kill fall height threshold (i.e., when the fall does not cause instant death).
 The default value is `3.0`.

**Descripción oficial:**

A getter for [SET_FALL_DAMAGE_LAND_ON_FOOT_MULTIPLIER](https://docs.fivem.net/natives/?_0x164A08C9).

---
### GetFallDamageMultiplier

`GET_FALL_DAMAGE_MULTIPLIER` · hash `0x7C46A6F0` · **Cliente**

```lua
local retval = GetFallDamageMultiplier()
```
```c
float GET_FALL_DAMAGE_MULTIPLIER();
```

**Devuelve:** `float` — Returns the fall damage multiplier applied to all peds when calculating fall damage from falls **below the kill fall height threshold** (i.e., when the fall does not cause instant death).
 The default value is `7.0`.

**Descripción oficial:**

A getter for [SET_FALL_DAMAGE_MULTIPLIER](https://docs.fivem.net/natives/?_0xF2E1A531).

---
### GetFuelConsumptionRateMultiplier

`GET_FUEL_CONSUMPTION_RATE_MULTIPLIER` · hash `0x5550BF9F` · **Cliente**

```lua
local retval = GetFuelConsumptionRateMultiplier()
```
```c
float GET_FUEL_CONSUMPTION_RATE_MULTIPLIER();
```

**Devuelve:** `float` — Current fuel consumption rate multiplier. 0 means that fuel is not consumed.

---
### GetFuelConsumptionState

`GET_FUEL_CONSUMPTION_STATE` · hash `0xC66CD90C` · **Cliente**

```lua
local retval = GetFuelConsumptionState()
```
```c
BOOL GET_FUEL_CONSUMPTION_STATE();
```

**Devuelve:** `BOOL` — True if fuel consumption is turned on. False otherwise.

---
### GetGlobalPassengerMassMultiplier

`GET_GLOBAL_PASSENGER_MASS_MULTIPLIER` · hash `0x78951816` · **Cliente**

```lua
local retval = GetGlobalPassengerMassMultiplier()
```
```c
float GET_GLOBAL_PASSENGER_MASS_MULTIPLIER();
```

**Devuelve:** `float` — Returns the mass of each passenger (not counting the driver) as a percentage of vehicle mass. Default value is 0.05

**Descripción oficial:**

A getter for [SET_GLOBAL_PASSENGER_MASS_MULTIPLIER](#applyweathercycles).

---
### GetHudComponentAlign

`GET_HUD_COMPONENT_ALIGN` · hash `0xCD949E20` · **Cliente**

```lua
local horizontalAlign, verticalAlign = GetHudComponentAlign(id)
```
```c
void GET_HUD_COMPONENT_ALIGN(int id, int* horizontalAlign, int* verticalAlign);
```

**Parámetros**

- `id` (`int`): The hud component id.
- `horizontalAlign` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `verticalAlign` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

See [SET_SCRIPT_GFX_ALIGN](../gta5/GRAPHICS.md#setscriptgfxalign) for details about how gfx align works.

---
### GetHudComponentName

`GET_HUD_COMPONENT_NAME` · hash `0xA91866BC` · **Cliente**

```lua
local retval = GetHudComponentName(id)
```
```c
char* GET_HUD_COMPONENT_NAME(int id);
```

**Parámetros**

- `id` (`int`): The hud component id.

**Devuelve:** `char*` — The hud component name.

---
### GetHudComponentSize

`GET_HUD_COMPONENT_SIZE` · hash `0x12217D33` · **Cliente**

```lua
local retval = GetHudComponentSize(id)
```
```c
Vector3 GET_HUD_COMPONENT_SIZE(int id);
```

**Parámetros**

- `id` (`int`): The hud component id.

**Devuelve:** `Vector3` — A Vector3 with the hud component size X and size Y values.

---
### GetInteriorEntitiesExtents

`GET_INTERIOR_ENTITIES_EXTENTS` · hash `0x322B1192` · **Cliente**

```lua
local bbMinX, bbMinY, bbMinZ, bbMaxX, bbMaxY, bbMaxZ = GetInteriorEntitiesExtents(interiorId)
```
```c
void GET_INTERIOR_ENTITIES_EXTENTS(int interiorId, float* bbMinX, float* bbMinY, float* bbMinZ, float* bbMaxX, float* bbMaxY, float* bbMaxZ);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `bbMinX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMinY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMinZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMaxX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMaxY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMaxZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void` — Interior entities extents.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local minX, minY, minZ, maxX, maxY, maxZ = GetInteriorEntitiesExtents(interiorId, roomId)
  print("current entities extents is: " .. vec(minX, minY, minZ) .." / " .. vec(maxX, maxY, maxZ))
end
```

---
### GetInteriorPortalCornerPosition

`GET_INTERIOR_PORTAL_CORNER_POSITION` · hash `0xF772BB2C` · **Cliente**

```lua
local posX, posY, posZ = GetInteriorPortalCornerPosition(interiorId, portalIndex, cornerIndex)
```
```c
void GET_INTERIOR_PORTAL_CORNER_POSITION(int interiorId, int portalIndex, int cornerIndex, float* posX, float* posY, float* posZ);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `cornerIndex` (`int`): Portal's corner index.
- `posX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `posY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `posZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void` — Portal corner position.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local portalIndex = 0
  local cornerIndex = 0

  local x, y, z = GetInteriorPortalCornerPosition(interiorId, portalIndex, cornerIndex)
  print("position of portal " .. portalIndex .. "corner index " .. cornerIndex .. " is: " .. vec(x, y, z))
end
```

---
### GetInteriorPortalCount

`GET_INTERIOR_PORTAL_COUNT` · hash `0xD05BB8B1` · **Cliente**

```lua
local retval = GetInteriorPortalCount(interiorId)
```
```c
int GET_INTERIOR_PORTAL_COUNT(int interiorId);
```

**Parámetros**

- `interiorId` (`int`): The target interior.

**Devuelve:** `int` — The amount of portals in interior.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local count = GetInteriorPortalCount(interiorId)
  print("interior " .. interiorId .. "has " .. count .. " portals")
end
```

---
### GetInteriorPortalEntityArchetype

`GET_INTERIOR_PORTAL_ENTITY_ARCHETYPE` · hash `0x9A0E1700` · **Cliente**

```lua
local retval = GetInteriorPortalEntityArchetype(interiorId, portalIndex, entityIndex)
```
```c
int GET_INTERIOR_PORTAL_ENTITY_ARCHETYPE(int interiorId, int portalIndex, int entityIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `entityIndex` (`int`): Portal entity index.

**Devuelve:** `int` — Portal entity archetype.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local portalIndex = 0

if interiorId ~= 0 then
  local count = GetInteriorPortalEntityCount(interiorId, portalIndex)
  for i=0, count-1 do
    local archetype = GetInteriorPortalEntityArchetype(interiorId, portalIndex, i)
    print("portal " .. portalIndex .." entity " .. i .. " archetype is: " .. archetype)
  end
end
```

---
### GetInteriorPortalEntityCount

`GET_INTERIOR_PORTAL_ENTITY_COUNT` · hash `0xC68021B` · **Cliente**

```lua
local retval = GetInteriorPortalEntityCount(interiorId, portalIndex)
```
```c
int GET_INTERIOR_PORTAL_ENTITY_COUNT(int interiorId, int portalIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.

**Devuelve:** `int` — Portal entity count.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local portalIndex = 0

if interiorId ~= 0 then
  local count = GetInteriorPortalEntityCount(interiorId, portalIndex)
  print("portal " .. portalIndex .." entity count is: " .. count)
end
```

---
### GetInteriorPortalEntityFlag

`GET_INTERIOR_PORTAL_ENTITY_FLAG` · hash `0x9DA2E811` · **Cliente**

```lua
local retval = GetInteriorPortalEntityFlag(interiorId, portalIndex, entityIndex)
```
```c
int GET_INTERIOR_PORTAL_ENTITY_FLAG(int interiorId, int portalIndex, int entityIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `entityIndex` (`int`): Portal entity index.

**Devuelve:** `int` — Portal entity flag.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local portalIndex = 0

if interiorId ~= 0 then
  local count = GetInteriorPortalEntityCount(interiorId, portalIndex)
  for i=0, count-1 do
    local flag = GetInteriorPortalEntityFlag(interiorId, portalIndex, i)
    print("portal " .. portalIndex .." entity " .. i .. " flag is: " .. flag)
  end
end
```

---
### GetInteriorPortalEntityPosition

`GET_INTERIOR_PORTAL_ENTITY_POSITION` · hash `0x9B7AB83C` · **Cliente**

```lua
local posX, posY, posZ = GetInteriorPortalEntityPosition(interiorId, portalIndex, entityIndex)
```
```c
void GET_INTERIOR_PORTAL_ENTITY_POSITION(int interiorId, int portalIndex, int entityIndex, float* posX, float* posY, float* posZ);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `entityIndex` (`int`): Portal entity index.
- `posX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `posY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `posZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void` — Portal entity position.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local portalIndex = 0

if interiorId ~= 0 then
  local count = GetInteriorPortalEntityCount(interiorId, portalIndex)
  for i=0, count-1 do
    local x, y, z = GetInteriorPortalEntityPosition(interiorId, portalIndex, i)
    print("portal " .. portalIndex .." entity " .. i .. " position is: " .. vec3(x, y, z))
  end
end
```

---
### GetInteriorPortalEntityRotation

`GET_INTERIOR_PORTAL_ENTITY_ROTATION` · hash `0x9F9CEB63` · **Cliente**

```lua
local rotX, rotY, rotZ, rotW = GetInteriorPortalEntityRotation(interiorId, portalIndex, entityIndex)
```
```c
void GET_INTERIOR_PORTAL_ENTITY_ROTATION(int interiorId, int portalIndex, int entityIndex, float* rotX, float* rotY, float* rotZ, float* rotW);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `entityIndex` (`int`): Portal entity index.
- `rotX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rotY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rotZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rotW` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void` — Portal entity rotation.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local portalIndex = 0

if interiorId ~= 0 then
  local count = GetInteriorPortalEntityCount(interiorId, portalIndex)
  for i=0, count-1 do
    local x, y, z, w = GetInteriorPortalEntityRotation(interiorId, portalIndex, i)
    print("portal " .. portalIndex .." entity " .. i .. " rotation is: " .. vec4(x, y, z, w))
  end
end
```

---
### GetInteriorPortalFlag

`GET_INTERIOR_PORTAL_FLAG` · hash `0xC74DA47C` · **Cliente**

```lua
local retval = GetInteriorPortalFlag(interiorId, portalIndex)
```
```c
int GET_INTERIOR_PORTAL_FLAG(int interiorId, int portalIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.

**Devuelve:** `int` — Portal's flag.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local portalFlag = GetInteriorPortalFlag(interiorId, 0)
  print("portal 0 flag is: " .. portalRoomFrom)
end
```

---
### GetInteriorPortalRoomFrom

`GET_INTERIOR_PORTAL_ROOM_FROM` · hash `0xAA9C141D` · **Cliente**

```lua
local retval = GetInteriorPortalRoomFrom(interiorId, portalIndex)
```
```c
int GET_INTERIOR_PORTAL_ROOM_FROM(int interiorId, int portalIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.

**Devuelve:** `int` — Portal's room FROM index.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local roomIndex = 0

  local portalRoomFrom = GetInteriorPortalRoomFrom(interiorId, 0)
  print("portal " .. roomIndex .. " room FROM is: " .. portalRoomFrom)
end
```

---
### GetInteriorPortalRoomTo

`GET_INTERIOR_PORTAL_ROOM_TO` · hash `0x3F47F0E8` · **Cliente**

```lua
local retval = GetInteriorPortalRoomTo(interiorId, portalIndex)
```
```c
int GET_INTERIOR_PORTAL_ROOM_TO(int interiorId, int portalIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.

**Devuelve:** `int` — Portal's room TO index.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local roomIndex = 0

  local portalRoomTo = GetInteriorPortalRoomTo(interiorId, 0)
  print("portal " .. roomIndex .. " room TO is: " .. portalRoomTo)
end
```

---
### GetInteriorPosition

`GET_INTERIOR_POSITION` · hash `0x77A435B0` · **Cliente**

```lua
local posX, posY, posZ = GetInteriorPosition(interiorId)
```
```c
void GET_INTERIOR_POSITION(int interiorId, float* posX, float* posY, float* posZ);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `posX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `posY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `posZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void` — Interior position.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local x, y, z = GetInteriorPosition(interiorId)
  print("current interior " .. interiorId .. " position is: " .. vec(x, y, z))
end
```

---
### GetInteriorRoomCount

`GET_INTERIOR_ROOM_COUNT` · hash `0xA2737C2C` · **Cliente**

```lua
local retval = GetInteriorRoomCount(interiorId)
```
```c
int GET_INTERIOR_ROOM_COUNT(int interiorId);
```

**Parámetros**

- `interiorId` (`int`): The target interior.

**Devuelve:** `int` — The amount of rooms in interior.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local count = GetInteriorRoomCount(interiorId)
  print("interior " .. interiorId .. "has " .. count .. " rooms")
end
```

---
### GetInteriorRoomExtents

`GET_INTERIOR_ROOM_EXTENTS` · hash `0xF9E795DD` · **Cliente**

```lua
local bbMinX, bbMinY, bbMinZ, bbMaxX, bbMaxY, bbMaxZ = GetInteriorRoomExtents(interiorId, roomIndex)
```
```c
void GET_INTERIOR_ROOM_EXTENTS(int interiorId, int roomIndex, float* bbMinX, float* bbMinY, float* bbMinZ, float* bbMaxX, float* bbMaxY, float* bbMaxZ);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomIndex` (`int`): Interior room index.
- `bbMinX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMinY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMinZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMaxX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMaxY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `bbMaxZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void` — Room extents.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local roomHash = GetRoomKeyFromEntity(playerPed)
local roomId = GetInteriorRoomIndexByHash(interiorId, roomHash)

if roomId ~= -1 then
  local minX, minY, minZ, maxX, maxY, maxZ = GetInteriorRoomExtents(interiorId, roomId)
  print("current room extents is: " .. vec(minX, minY, minZ) .." / " .. vec(maxX, maxY, maxZ))
end
```

---
### GetInteriorRoomFlag

`GET_INTERIOR_ROOM_FLAG` · hash `0x6B7AF743` · **Cliente**

```lua
local retval = GetInteriorRoomFlag(interiorId, roomIndex)
```
```c
int GET_INTERIOR_ROOM_FLAG(int interiorId, int roomIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomIndex` (`int`): Interior room index.

**Devuelve:** `int` — Room's flag.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local roomHash = GetRoomKeyFromEntity(playerPed)
local roomId = GetInteriorRoomIndexByHash(interiorId, roomHash)

if roomId ~= -1 then
  local roomFlag = GetInteriorRoomFlag(interiorId, roomId)
  print("current room flag is: " .. roomFlag)
end
```

---
### GetInteriorRoomIndexByHash

`GET_INTERIOR_ROOM_INDEX_BY_HASH` · hash `0xE0EE05F8` · **Cliente**

```lua
local retval = GetInteriorRoomIndexByHash(interiorId, roomHash)
```
```c
int GET_INTERIOR_ROOM_INDEX_BY_HASH(int interiorId, int roomHash);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomHash` (`int`): Interior room hash.

**Devuelve:** `int` — Room index, -1 if failed.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local roomHash = GetRoomKeyFromEntity(playerPed)
local roomId = GetInteriorRoomIndexByHash(interiorId, roomHash)

if roomId ~= -1 then
  print("current room index is: " .. roomId)
end
```

---
### GetInteriorRoomName

`GET_INTERIOR_ROOM_NAME` · hash `0x11755DF2` · **Cliente**

```lua
local retval = GetInteriorRoomName(interiorId, roomIndex)
```
```c
char* GET_INTERIOR_ROOM_NAME(int interiorId, int roomIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomIndex` (`int`): Interior room index.

**Devuelve:** `char*` — Room's name.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local roomHash = GetRoomKeyFromEntity(playerPed)
local roomId = GetInteriorRoomIndexByHash(interiorId, roomHash)

if roomId ~= -1 then
  local roomName = GetInteriorRoomName(interiorId, roomId)
  print("current room name is: " .. roomName)
end
```

---
### GetInteriorRoomTimecycle

`GET_INTERIOR_ROOM_TIMECYCLE` · hash `0x82BA3F88` · **Cliente**

```lua
local retval = GetInteriorRoomTimecycle(interiorId, roomIndex)
```
```c
int GET_INTERIOR_ROOM_TIMECYCLE(int interiorId, int roomIndex);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomIndex` (`int`): Interior room index.

**Devuelve:** `int` — Room's timecycle hash.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local roomHash = GetRoomKeyFromEntity(playerPed)
local roomId = GetInteriorRoomIndexByHash(interiorId, roomHash)

if roomId ~= -1 then
  local roomTimecycle = GetInteriorRoomTimecycle(interiorId, roomId)
  print("current room timecycle hash is: " .. roomTimecycle)
end
```

---
### GetInteriorRotation

`GET_INTERIOR_ROTATION` · hash `0x5A039998` · **Cliente**

```lua
local rotx, rotY, rotZ, rotW = GetInteriorRotation(interiorId)
```
```c
void GET_INTERIOR_ROTATION(int interiorId, float* rotx, float* rotY, float* rotZ, float* rotW);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `rotx` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rotY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rotZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rotW` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void` — Interior rotation in quaternion.

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local x, y, z, w = GetInteriorRotation(interiorId)
  print("current interior " .. interiorId .. " rotation is: " .. vec(x, y, z, w))
end
```

---
### GetKillFallHeight

`GET_KILL_FALL_HEIGHT` · hash `0x57888D4C` · **Cliente**

```lua
local retval = GetKillFallHeight()
```
```c
float GET_KILL_FALL_HEIGHT();
```

**Devuelve:** `float` — Returns the height from which non-player peds will instantly die due to fall damage.\ The default value is `10.0`.

**Descripción oficial:**

A getter for [SET_KILL_FALL_HEIGHT](https://docs.fivem.net/natives/?_0x7E8D83E4).

---
### GetMapZoomDataLevel

`GET_MAP_ZOOM_DATA_LEVEL` · hash `0x1363A998` · **Cliente**

```lua
local retval, zoomScale, zoomSpeed, scrollSpeed, tilesX, tilesY = GetMapZoomDataLevel(index)
```
```c
BOOL GET_MAP_ZOOM_DATA_LEVEL(int index, float* zoomScale, float* zoomSpeed, float* scrollSpeed, float* tilesX, float* tilesY);
```

**Parámetros**

- `index` (`int`): Zoom level index.
- `zoomScale` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: fZoomScale value.
- `zoomSpeed` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: fZoomSpeed value.
- `scrollSpeed` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: fScrollSpeed value.
- `tilesX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: vTiles X.
- `tilesY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: vTiles Y.

**Devuelve:** `BOOL` — A boolean indicating TRUE if the data was received successfully.

**Descripción oficial:**

Returns the zoom level data by index from mapzoomdata.meta file.

---
### GetMapdataEntityHandle

`GET_MAPDATA_ENTITY_HANDLE` · hash `0x30AA6911` · **Cliente**

```lua
local retval, entityHandle = GetMapdataEntityHandle(mapDataHash, entityInternalIdx, entityHandle)
```
```c
BOOL GET_MAPDATA_ENTITY_HANDLE(int mapDataHash, int entityInternalIdx, int* entityHandle);
```

**Parámetros**

- `mapDataHash` (`int`): A mapdata hash from `mapDataLoaded` event.
- `entityInternalIdx` (`int`): An internal entity's index.
- `entityHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The output entity handle.

**Devuelve:** `BOOL` — True if successful, false if not.

**Descripción oficial:**

Retrieves the map data entity handle.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### GetMapdataEntityMatrix

`GET_MAPDATA_ENTITY_MATRIX` · hash `0x2C3CDA93` · **Cliente**

```lua
local retval = GetMapdataEntityMatrix(mapDataHash, entityInternalIdx, matrixPtr)
```
```c
BOOL GET_MAPDATA_ENTITY_MATRIX(int mapDataHash, int entityInternalIdx, long matrixPtr);
```

**Parámetros**

- `mapDataHash` (`int`): A mapdata hash from `mapDataLoaded` event.
- `entityInternalIdx` (`int`): An internal entity's index.
- `matrixPtr` (`long`): A mutable pointer to a 64-byte buffer of floating-point values, representing an XMFLOAT4X4 in layout.

**Devuelve:** `BOOL` — Whether or not the matrix was retrieved.

**Descripción oficial:**

Returns mapdata's entity matrix. This function supports SDK infrastructure and is not intended to be used directly from your code.

This should be used from JavaScript or another language supporting mutable buffers like ArrayBuffer.

Matrix layout is as follows:

*   Element \[0], \[1] and \[2] should represent the right vector.
*   Element \[4], \[5] and \[6] should represent the forward vector.
*   Element \[8], \[9] and \[10] should represent the up vector.
*   Element \[12], \[13] and \[14] should represent X, Y and Z translation coordinates.
*   All other elements should be \[0, 0, 0, 1].

---
### GetMapdataFromHashKey

`GET_MAPDATA_FROM_HASH_KEY` · hash `0xD29D8EDD` · **Cliente**

```lua
local retval = GetMapdataFromHashKey(mapdataHandle)
```
```c
int GET_MAPDATA_FROM_HASH_KEY(Hash mapdataHandle);
```

**Parámetros**

- `mapdataHandle` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The input map data handle.

**Devuelve:** `int` — A transient (non-persistable) index to the requested mapdata, or -1.

**Descripción oficial:**

Returns the transient map data index for a specified hash.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### GetNuiCursorPosition

`GET_NUI_CURSOR_POSITION` · hash `0xBDBA226F` · **Cliente**

```lua
local x, y = GetNuiCursorPosition()
```
```c
void GET_NUI_CURSOR_POSITION(int* x, int* y);
```

**Parámetros**

- `x` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `y` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetNumberOfPedCollectionDrawableVariations

`GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS` · hash `0x310D0271` · **Cliente**

```lua
local retval = GetNumberOfPedCollectionDrawableVariations(ped, componentId, collection)
```
```c
int GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS(Ped ped, int componentId, char* collection);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.

**Devuelve:** `int` — Number of drawables available in the given collection. Returns 0 if ped or collection does not exist.

**Descripción oficial:**

An analogue of [GET_NUMBER_OF_PED_DRAWABLE_VARIATIONS](../gta5/PED-1.md#getnumberofpeddrawablevariations) that returns number of drawable variations inside a single collection instead of the total number across all collections.

---
### GetNumberOfPedCollectionPropDrawableVariations

`GET_NUMBER_OF_PED_COLLECTION_PROP_DRAWABLE_VARIATIONS` · hash `0x3B6A13E1` · **Cliente**

```lua
local retval = GetNumberOfPedCollectionPropDrawableVariations(ped, anchorPoint, collection)
```
```c
int GET_NUMBER_OF_PED_COLLECTION_PROP_DRAWABLE_VARIATIONS(Ped ped, int anchorPoint, char* collection);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.

**Devuelve:** `int` — Number of props available in the given collection. Returns 0 if ped or collection does not exist.

**Descripción oficial:**

An analogue of [GET_NUMBER_OF_PED_PROP_DRAWABLE_VARIATIONS](../gta5/PED-1.md#getnumberofpedpropdrawablevariations) that returns number of prop variations inside a single collection instead of the total number across all collections.

---
### GetNumberOfPedCollectionPropTextureVariations

`GET_NUMBER_OF_PED_COLLECTION_PROP_TEXTURE_VARIATIONS` · hash `0x75CAF9CC` · **Cliente**

```lua
local retval = GetNumberOfPedCollectionPropTextureVariations(ped, anchorPoint, collection, propIndex)
```
```c
int GET_NUMBER_OF_PED_COLLECTION_PROP_TEXTURE_VARIATIONS(Ped ped, int anchorPoint, char* collection, int propIndex);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `propIndex` (`int`): Local prop index inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_PROP_DRAWABLE_VARIATIONS](#getnumberofpedcollectionpropdrawablevariations).

**Devuelve:** `int` — Number of texture variations available for the given prop. Returns 0 if ped or collection does not exist or index is out of bounds.

**Descripción oficial:**

An alternative to [GET_NUMBER_OF_PED_PROP_TEXTURE_VARIATIONS](../gta5/PED-1.md#getnumberofpedproptexturevariations) that uses local collection indexing instead of the global one.

---
### GetNumberOfPedCollectionTextureVariations

`GET_NUMBER_OF_PED_COLLECTION_TEXTURE_VARIATIONS` · hash `0xD2C15D7` · **Cliente**

```lua
local retval = GetNumberOfPedCollectionTextureVariations(ped, componentId, collection, drawableId)
```
```c
int GET_NUMBER_OF_PED_COLLECTION_TEXTURE_VARIATIONS(Ped ped, int componentId, char* collection, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `drawableId` (`int`): Local drawable Id inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations).

**Devuelve:** `int` — Number of texture variations available for the given drawable component. Returns 0 if ped or collection does not exist or index is out of bounds.

**Descripción oficial:**

An alternative to [GET_NUMBER_OF_PED_TEXTURE_VARIATIONS](../gta5/PED-1.md#getnumberofpedtexturevariations) that uses local collection indexing instead of the global one.

---
### GetParkedVehicleDensityMultiplier

`GET_PARKED_VEHICLE_DENSITY_MULTIPLIER` · hash `0xFF72DF84` · **Cliente**

```lua
local retval = GetParkedVehicleDensityMultiplier()
```
```c
float GET_PARKED_VEHICLE_DENSITY_MULTIPLIER();
```

**Devuelve:** `float` — Returns parked vehicle density multiplier value.

**Descripción oficial:**

A getter for [SET_PARKED_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME](../gta5/VEHICLE-2.md#setparkedvehicledensitymultiplierthisframe).

---
### GetPauseMapPointerWorldPosition

`GET_PAUSE_MAP_POINTER_WORLD_POSITION` · hash `0xE5AF7A82` · **Cliente**

```lua
local retval = GetPauseMapPointerWorldPosition()
```
```c
Vector3 GET_PAUSE_MAP_POINTER_WORLD_POSITION();
```

**Devuelve:** `Vector3` — A Vector3 with the pause map pointer world position X and Y values.

**Descripción oficial:**

Returns the world position the pointer is hovering on the pause map.

---
### GetPedCollectionLocalIndexFromDrawable

`GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE` · hash `0x94EB1FE4` · **Cliente**

```lua
local retval = GetPedCollectionLocalIndexFromDrawable(ped, componentId, drawableId)
```
```c
int GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE(Ped ped, int componentId, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `drawableId` (`int`): Global drawable ID. Same as set in [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation). Global drawable ID points to drawables as if drawables from all collections for the given component are placed into one continuous array.

**Devuelve:** `int` — Local index inside a collection that the given global drawable ID corresponds to. Returns -1 if Ped is not found or the global index is out of bounds.

**Descripción oficial:**

Gets local index inside a collection (which can be obtained using [GET_PED_COLLECTION_NAME_FROM_DRAWABLE](#getpedcollectionnamefromdrawable)) for the given global drawable ID. The collection name and index are used in functions like [SET_PED_COLLECTION_COMPONENT_VARIATION](#setpedcollectioncomponentvariation).

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
-- Top for mp_f_freemode_01. From female_freemode_beach collection under index 1.
-- Global index is 17 because there is 16 top variations in the base game collection that goes before the female_freemode_beach collection.
local name = GetPedDrawableCollectionName(ped, 11, 17)
local index = GetPedDrawableCollectionLocalIndex(ped, 11, 17)
-- Equivalent to SetPedComponentVariation(ped, 11, 17, 0, 0)
SetPedCollectionComponentVariation(ped, 11, name, index, 0, 0)
```

---
### GetPedCollectionLocalIndexFromProp

`GET_PED_COLLECTION_LOCAL_INDEX_FROM_PROP` · hash `0xFBDB885F` · **Cliente**

```lua
local retval = GetPedCollectionLocalIndexFromProp(ped, anchorPoint, propIndex)
```
```c
int GET_PED_COLLECTION_LOCAL_INDEX_FROM_PROP(Ped ped, int anchorPoint, int propIndex);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)
- `propIndex` (`int`): Global prop index. Same as set by `drawableId` in [SET_PED_PROP_INDEX](servidor.md#setpedpropindex). Global prop index points to prop as if props from all collections for the given component are placed into one continuous array.

**Devuelve:** `int` — Local index inside a collection that the given global prop index corresponds to. Returns -1 if Ped is not found or the global index is out of bounds.

**Descripción oficial:**

Gets local index inside a collection (which can be obtained using [GET_PED_COLLECTION_NAME_FROM_PROP](#getpedcollectionnamefromprop)) for the given global prop index. The collection name and index are used in functions like [SET_PED_COLLECTION_PROP_INDEX](#setpedcollectionpropindex).

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
-- Hat for mp_f_freemode_01. From female_freemode_beach collection under index 1.
-- Global index is 21 because there is 20 head prop variations in the base game collection that goes before the female_freemode_beach collection.
local name = GetPedPropCollectionName(ped, 0, 21)
local index = GetPedPropCollectionLocalIndex(ped, 0, 21)
-- Equivalent to SetPedPropIndex(ped, 0, 21, 0, false)
SetPedCollectionPropIndex(ped, 0, name, index, 0, false)
```

---
### GetPedCollectionName

`GET_PED_COLLECTION_NAME` · hash `0xFED5D83A` · **Cliente**

```lua
local retval = GetPedCollectionName(ped, index)
```
```c
char* GET_PED_COLLECTION_NAME(Ped ped, int index);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `index` (`int`): The target collection index

**Devuelve:** `char*` — Name of the collection with given index. Base game collection (always stored with index 0) is an empty string. Returns null if Ped is not found or index is out of bounds.

**Descripción oficial:**

Returns name of collection under given index for the given Ped.

Collections are groups of drawable components or props available for the given Ped. Usually collection corresponds to a certain DLC or the base game. See [SET_PED_COLLECTION_COMPONENT_VARIATION](#setpedcollectioncomponentvariation), [SET_PED_COLLECTION_PROP_INDEX](#setpedcollectionpropindex), [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations) etc natives for more details on how to work with collections.

`GET_PED_COLLECTION_NAME` can be used together with [GET_PED_COLLECTIONS_COUNT](#getpedcollectionscount) to list all collections attached to Ped.

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
local count = GetPedCollectionsCount(ped)
for i = 0, count - 1 do
  print(GetPedCollectionName(ped, i))
end
```

---
### GetPedCollectionNameFromDrawable

`GET_PED_COLLECTION_NAME_FROM_DRAWABLE` · hash `0xD6BBA48B` · **Cliente**

```lua
local retval = GetPedCollectionNameFromDrawable(ped, componentId, drawableId)
```
```c
char* GET_PED_COLLECTION_NAME_FROM_DRAWABLE(Ped ped, int componentId, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `drawableId` (`int`): Global drawable ID. Same as set in [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation). Global drawable ID points to drawables as if drawables from all collections for the given component are placed into one continuous array.

**Devuelve:** `char*` — Name of the collection that the given global drawable ID corresponds to. Base game collection is an empty string. Returns null if Ped is not found or the global index is out of bounds.

**Descripción oficial:**

Gets collection name for the given global drawable ID. Together with [GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE](#getpedcollectionlocalindexfromdrawable) is used to get collection and local index (inside the given collection) of the drawable. The collection name and index are used in functions like [SET_PED_COLLECTION_COMPONENT_VARIATION](#setpedcollectioncomponentvariation).

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
-- Top for mp_f_freemode_01. From female_freemode_beach collection under index 1.
-- Global index is 17 because there is 16 top variations in the base game collection that goes before the female_freemode_beach collection.
local name = GetPedDrawableCollectionName(ped, 11, 17)
local index = GetPedDrawableCollectionLocalIndex(ped, 11, 17)
-- Equivalent to SetPedComponentVariation(ped, 11, 17, 0, 0)
SetPedCollectionComponentVariation(ped, 11, name, index, 0, 0)
```

---
### GetPedCollectionNameFromProp

`GET_PED_COLLECTION_NAME_FROM_PROP` · hash `0x8ED0C17` · **Cliente**

```lua
local retval = GetPedCollectionNameFromProp(ped, anchorPoint, propIndex)
```
```c
char* GET_PED_COLLECTION_NAME_FROM_PROP(Ped ped, int anchorPoint, int propIndex);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)
- `propIndex` (`int`): Global prop index. Same as set by `drawableId` in [SET_PED_PROP_INDEX](servidor.md#setpedpropindex). Global prop index points to prop as if props from all collections for the given component are placed into one continuous array.

**Devuelve:** `char*` — Name of the collection that the given global drawable ID corresponds to. Base game collection is an empty string. Returns null if Ped is not found or the global index is out of bounds.

**Descripción oficial:**

Gets collection name for the given global prop index. Together with [GET_PED_COLLECTION_LOCAL_INDEX_FROM_PROP](#getpedcollectionlocalindexfromprop) is used to get collection and local index (inside the given collection) of the prop. The collection name and index are used in functions like [SET_PED_COLLECTION_PROP_INDEX](#setpedcollectionpropindex).

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
-- Hat for mp_f_freemode_01. From female_freemode_beach collection under index 1.
-- Global index is 21 because there is 20 head prop variations in the base game collection that goes before the female_freemode_beach collection.
local name = GetPedPropCollectionName(ped, 0, 21)
local index = GetPedPropCollectionLocalIndex(ped, 0, 21)
-- Equivalent to SetPedPropIndex(ped, 0, 21, 0, false)
SetPedCollectionPropIndex(ped, 0, name, index, 0, false)
```

---
### GetPedCollectionsCount

`GET_PED_COLLECTIONS_COUNT` · hash `0x45946359` · **Cliente**

```lua
local retval = GetPedCollectionsCount(ped)
```
```c
int GET_PED_COLLECTIONS_COUNT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `int` — Number of Ped variation collections. 0 if Ped is not found.

**Descripción oficial:**

Returns number of variation collections available for the given Ped.

Collections are groups of drawable components or props available for the given Ped. Usually collection corresponds to a certain DLC or the base game. See [SET_PED_COLLECTION_COMPONENT_VARIATION](#setpedcollectioncomponentvariation), [SET_PED_COLLECTION_PROP_INDEX](#setpedcollectionpropindex), [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations) etc natives for more details on how to work with collections.

`GET_PED_COLLECTIONS_COUNT` can be used together with [GET_PED_COLLECTION_NAME](#getpedcollectionname) to list all collections attached to Ped.

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
local count = GetPedCollectionsCount(ped)
for i = 0, count - 1 do
  print(GetPedCollectionName(ped, i))
end
```

---
### GetPedDecorations

`GET_PED_DECORATIONS` · hash `0x7CCE1163` · **Cliente**

```lua
local retval = GetPedDecorations(ped)
```
```c
object GET_PED_DECORATIONS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The ped you want to retrieve data for.

**Devuelve:** `object` — An object containing a list of applied decorations.

**Descripción oficial:**

Returns a list of decorations applied to a ped.

The data returned adheres to the following layout:

```
[ [ collectionHash1, overlayHash1 ], ..., [c ollectionHashN, overlayHashN ] ]
```

This command will return undefined data if invoked on a remote player ped.

---
### GetPedDensityMultiplier

`GET_PED_DENSITY_MULTIPLIER` · hash `0xF5A904F9` · **Cliente**

```lua
local retval = GetPedDensityMultiplier()
```
```c
float GET_PED_DENSITY_MULTIPLIER();
```

**Devuelve:** `float` — Returns ped density multiplier value.

**Descripción oficial:**

A getter for [SET_PED_DENSITY_MULTIPLIER_THIS_FRAME](../gta5/PED-1.md#setpeddensitymultiplierthisframe).

---
### GetPedDrawableGlobalIndexFromCollection

`GET_PED_DRAWABLE_GLOBAL_INDEX_FROM_COLLECTION` · hash `0x280F1FC3` · **Cliente**

```lua
local retval = GetPedDrawableGlobalIndexFromCollection(ped, componentId, collection, drawableId)
```
```c
int GET_PED_DRAWABLE_GLOBAL_INDEX_FROM_COLLECTION(Ped ped, int componentId, char* collection, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `drawableId` (`int`): Local drawable Id inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations).

**Devuelve:** `int` — Global drawable ID that corresponds to the given collection and local drawable index. Returns -1 if Ped or collection does not exist or local index is out of bounds.

**Descripción oficial:**

Returns global drawable index based on the local one. Is it a reverse to [GET_PED_COLLECTION_NAME_FROM_DRAWABLE](#getpedcollectionnamefromdrawable) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE](#getpedcollectionlocalindexfromdrawable) natives.

Drawables are stored inside collections. Each collection usually corresponds to a certain DCL or the base game.

If all drawables from all collections are placed into one continuous array - the global index will correspond to the index of drawable in such array. Local index is index of drawable in this array relative to the start of the given collection.

---
### GetPedDrawableVariationCollectionLocalIndex

`GET_PED_DRAWABLE_VARIATION_COLLECTION_LOCAL_INDEX` · hash `0x9970386F` · **Cliente**

```lua
local retval = GetPedDrawableVariationCollectionLocalIndex(ped, componentId)
```
```c
int GET_PED_DRAWABLE_VARIATION_COLLECTION_LOCAL_INDEX(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)

**Devuelve:** `int` — Local drawable index of the drawable that is currently used in the given ped and component.

**Descripción oficial:**

An analogue to [GET_PED_DRAWABLE_VARIATION](../gta5/PED-1.md#getpeddrawablevariation) that returns collection local drawable index (inside [GET_PED_DRAWABLE_VARIATION_COLLECTION_NAME](#getpeddrawablevariationcollectionname) collection) instead of the global drawable index.

---
### GetPedDrawableVariationCollectionName

`GET_PED_DRAWABLE_VARIATION_COLLECTION_NAME` · hash `0xBCE0AB63` · **Cliente**

```lua
local retval = GetPedDrawableVariationCollectionName(ped, componentId)
```
```c
char* GET_PED_DRAWABLE_VARIATION_COLLECTION_NAME(Ped ped, int componentId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)

**Devuelve:** `char*` — Collection name to which the current drawable used in the given ped and component belongs to. Returns null if Ped is not found or index is out of bounds.

**Descripción oficial:**

An analogue to [GET_PED_DRAWABLE_VARIATION](../gta5/PED-1.md#getpeddrawablevariation) that returns collection name instead of the global drawable index.

Should be used together with [GET_PED_DRAWABLE_VARIATION_COLLECTION_LOCAL_INDEX](#getpeddrawablevariationcollectionlocalindex).

---
### GetPedEyeColor

`GET_PED_EYE_COLOR` · hash `0xA47B860F` · **Cliente**

```lua
local retval = GetPedEyeColor(ped)
```
```c
int GET_PED_EYE_COLOR(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `int` — Returns ped's eye colour, or -1 if fails to get.

**Descripción oficial:**

A getter for [\_SET_PED_EYE_COLOR](servidor.md#setpedeyecolor). Returns -1 if fails to get.

**Ejemplo (lua):**

```lua
local pedEyeColour = GetPedEyeColor(PlayerPedId())
if pedEyeColour == 7 then
  print("Gray eyes!")
end
```

---
### GetPedFaceFeature

`GET_PED_FACE_FEATURE` · hash `0xBA352ADD` · **Cliente**

```lua
local retval = GetPedFaceFeature(ped, index)
```
```c
float GET_PED_FACE_FEATURE(Ped ped, int index);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `index` (`int`): Face feature index

**Devuelve:** `float` — Returns ped's face feature value, or 0.0 if fails to get.

**Descripción oficial:**

A getter for [\_SET_PED_FACE_FEATURE](servidor.md#setpedfacefeature). Returns 0.0 if fails to get.

**Ejemplo (lua):**

```lua
local noseWidth = GetPedFaceFeature(PlayerPedId(), 0)
if noseWidth == 1.0 then
  print("You have big nose!")
end
```

---
### GetPedHairColor

`GET_PED_HAIR_COLOR` · hash `0xA3EA2893` · **Cliente**

```lua
local retval = GetPedHairColor(ped)
```
```c
int GET_PED_HAIR_COLOR(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `int` — Returns ped's primary hair colour.

**Descripción oficial:**

A getter for [\_SET_PED_HAIR_COLOR](servidor.md#setpedhairtint). Returns -1 if fails to get.

**Ejemplo (lua):**

```lua
local primaryColour = GetPedHairColor(PlayerPedId())
if primaryColour == 18 then
  print("You have red hair!")
end
```

---
### GetPedHairHighlightColor

`GET_PED_HAIR_HIGHLIGHT_COLOR` · hash `0x4B087305` · **Cliente**

```lua
local retval = GetPedHairHighlightColor(ped)
```
```c
int GET_PED_HAIR_HIGHLIGHT_COLOR(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `int` — Returns ped's secondary hair colour.

**Descripción oficial:**

A getter for [\_SET_PED_HAIR_COLOR](servidor.md#setpedhairtint). Returns -1 if fails to get.

**Ejemplo (lua):**

```lua
local secondaryColour = GetPedHairHighlightColor(PlayerPedId())
if secondaryColour == 32 then
  print("You have pink hair highlight colour!")
end
```

---
### GetPedHeadOverlayData

`GET_PED_HEAD_OVERLAY_DATA` · hash `0xC46EE605` · **Cliente**

```lua
local retval, overlayValue, colourType, firstColour, secondColour, overlayOpacity = GetPedHeadOverlayData(ped, index)
```
```c
BOOL GET_PED_HEAD_OVERLAY_DATA(Ped ped, int index, int* overlayValue, int* colourType, int* firstColour, int* secondColour, float* overlayOpacity);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `index` (`int`): Overlay index
- `overlayValue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Overlay value pointer
- `colourType` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Colour type pointer
- `firstColour` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: First colour pointer
- `secondColour` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Second colour pointer
- `overlayOpacity` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Opacity pointer

**Devuelve:** `BOOL` — Returns ped's head overlay data.

**Descripción oficial:**

A getter for [SET_PED_HEAD_OVERLAY](servidor.md#setpedheadoverlay) and [\_SET_PED_HEAD_OVERLAY_COLOR](servidor.md#setpedheadoverlaycolor) natives.

**Ejemplo (lua):**

```lua
-- getting beard overlay data
local success, overlayValue, colourType, firstColour, secondColour, overlayOpacity = GetPedHeadOverlayData(PlayerPedId(), 1)
if success then
  -- incrementing value
  SetPedHeadOverlay(PlayerPedId(), 1, overlayValue + 1, overlayOpacity)
end
```

---
### GetPedModelHealthConfig

`GET_PED_MODEL_HEALTH_CONFIG` · hash `0xF71542F7` · **Cliente**

```lua
local retval = GetPedModelHealthConfig(modelHash)
```
```c
Hash GET_PED_MODEL_HEALTH_CONFIG(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Ped's model.

**Devuelve:** `Hash`

**Descripción oficial:**

Gets a ped model's health config.

**Ejemplo (lua):**

```lua
GetPedModelHealthConfig(`mp_f_freemode_01`)
```

---
### GetPedModelPersonality

`GET_PED_MODEL_PERSONALITY` · hash `0xFE08CAD6` · **Cliente**

```lua
local retval = GetPedModelPersonality(modelHash)
```
```c
Hash GET_PED_MODEL_PERSONALITY(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Ped's model.

**Devuelve:** `Hash`

**Descripción oficial:**

Gets a ped model's personality type.

---
### GetPedMovementClipset

`GET_PED_MOVEMENT_CLIPSET` · hash `0x69E81E3D` · **Cliente**

```lua
local retval = GetPedMovementClipset(ped)
```
```c
int GET_PED_MOVEMENT_CLIPSET(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `int` — The current movement clipset hash.

---
### GetPedPropCollectionLocalIndex

`GET_PED_PROP_COLLECTION_LOCAL_INDEX` · hash `0xCD420AD1` · **Cliente**

```lua
local retval = GetPedPropCollectionLocalIndex(ped, anchorPoint)
```
```c
int GET_PED_PROP_COLLECTION_LOCAL_INDEX(Ped ped, int anchorPoint);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)

**Devuelve:** `int` — Local drawable index of the drawable that is currently used in the given ped and component, or -1 if the ped does not have a prop at the specified anchor point

**Descripción oficial:**

An analogue to [GET_PED_PROP_INDEX](../gta5/PED-1.md#getpedpropindex) that returns collection local prop index (inside [GET_PED_PROP_COLLECTION_NAME](#getpedpropcollectionname) collection) instead of the global prop index.

---
### GetPedPropCollectionName

`GET_PED_PROP_COLLECTION_NAME` · hash `0x6B5653E4` · **Cliente**

```lua
local retval = GetPedPropCollectionName(ped, anchorPoint)
```
```c
char* GET_PED_PROP_COLLECTION_NAME(Ped ped, int anchorPoint);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)

**Devuelve:** `char*` — Collection name to which the current prop used in the given ped and anchor point belongs to. Returns null if Ped is not found, does not have a prop at the specified anchor point, or if the index is out of bounds.

**Descripción oficial:**

An analogue to [GET_PED_PROP_INDEX](../gta5/PED-1.md#getpedpropindex) that returns collection name instead of the global drawable index.

Should be used together with [GET_PED_PROP_COLLECTION_LOCAL_INDEX](#getpedpropcollectionlocalindex).

---
### GetPedPropGlobalIndexFromCollection

`GET_PED_PROP_GLOBAL_INDEX_FROM_COLLECTION` · hash `0x2CB45CDC` · **Cliente**

```lua
local retval = GetPedPropGlobalIndexFromCollection(ped, anchorPoint, collection, propIndex)
```
```c
int GET_PED_PROP_GLOBAL_INDEX_FROM_COLLECTION(Ped ped, int anchorPoint, char* collection, int propIndex);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `propIndex` (`int`): Local prop index inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_PROP_DRAWABLE_VARIATIONS](#getnumberofpedcollectionpropdrawablevariations).

**Devuelve:** `int` — Global prop index that corresponds to the given collection and local prop index. Returns -1 if Ped or collection does not exist or local index is out of bounds.

**Descripción oficial:**

Returns global prop index based on the local one. Is it a reverse to [GET_PED_COLLECTION_NAME_FROM_PROP](#getpedcollectionnamefromprop) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_PROP](#getpedcollectionlocalindexfromprop) natives.

Props are stored inside collections. Each collection usually corresponds to a certain DCL or the base game.

If all props from all collections are placed into one continuous array - the global index will correspond to the index of the prop in such array. Local index is index of the prop in this array relative to the start of the given collection.

---
### GetPedSweat

`GET_PED_SWEAT` · hash `0x44B91E94` · **Cliente**

```lua
local retval = GetPedSweat(ped)
```
```c
float GET_PED_SWEAT(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped

**Devuelve:** `float` — Returns ped's sweat.

**Descripción oficial:**

A getter for [SET_PED_SWEAT](../gta5/PED-1.md#setpedsweat).

**Ejemplo (lua):**

```lua
local sweat = GetPedSweat(PlayerPedId())
```

---
### GetPlayerFromServerId

`GET_PLAYER_FROM_SERVER_ID` · hash `0x344EA166` · **Cliente**

```lua
local retval = GetPlayerFromServerId(serverId)
```
```c
Player GET_PLAYER_FROM_SERVER_ID(int serverId);
```

**Parámetros**

- `serverId` (`int`): The player's server ID.

**Devuelve:** `Player` — A valid Player ID if one is found, `-1` if not.

**Descripción oficial:**

Gets a local client's Player ID from its server ID counterpart, assuming the passed `serverId` exists on the client.

If no matching client is found, or an invalid value is passed over as the `serverId` native's parameter, the native result will be `-1`.

It's worth noting that this native method can only retrieve information about clients that are culled to the connected client.

**Ejemplo (lua):**

```lua
--We will assume the serverId is '4' in this scenario and that it's a valid serverId.

-- Passing invalid Player IDs such as 'nil' or IDs that don't exist will result in playerId being -1.

local playerId = GetPlayerFromServerId(serverId);

-- If the resulting playerId is not invalid (not equal to -1)
if playerId ~= -1 then
    -- Do our stuff on this player.
end
```

---
### GetPlayerInvincible_2

`GET_PLAYER_INVINCIBLE_2` · hash `0xF2E3912B` · **Cliente**

```lua
local retval = GetPlayerInvincible_2(player)
```
```c
BOOL GET_PLAYER_INVINCIBLE_2(Player player);
```

**Parámetros**

- `player` (`Player`): The player id

**Devuelve:** `BOOL` — A boolean to tell if the player is invincible.

**Descripción oficial:**

Unlike [GET_PLAYER_INVINCIBLE](servidor.md#getplayerinvincible) this native gets both [SET_PLAYER_INVINCIBLE_KEEP_RAGDOLL_ENABLED](../gta5/PLAYER.md#setplayerinvinciblekeepragdollenabled) and [SET_PLAYER_INVINCIBLE](servidor.md#setplayerinvincible) invincibility state.

---
### GetPlayerKillFallHeight

`GET_PLAYER_KILL_FALL_HEIGHT` · hash `0xBFB2990C` · **Cliente**

```lua
local retval = GetPlayerKillFallHeight()
```
```c
float GET_PLAYER_KILL_FALL_HEIGHT();
```

**Devuelve:** `float` — Returns the height from which the player will instantly die due to fall damage.\ The default value is `15.0`.

**Descripción oficial:**

A getter for [SET_PLAYER_KILL_FALL_HEIGHT](https://docs.fivem.net/natives/?_0xAEF2C6A4).

---
### GetPlayerMaxStamina

`GET_PLAYER_MAX_STAMINA` · hash `0xD014AB79` · **Cliente**

```lua
local retval = GetPlayerMaxStamina(playerId)
```
```c
float GET_PLAYER_MAX_STAMINA(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player max stamina.

---
### GetPlayerMeleeWeaponDefenseModifier

`GET_PLAYER_MELEE_WEAPON_DEFENSE_MODIFIER` · hash `0x27E94EF8` · **Cliente**

```lua
local retval = GetPlayerMeleeWeaponDefenseModifier(playerId)
```
```c
float GET_PLAYER_MELEE_WEAPON_DEFENSE_MODIFIER(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player melee weapon defense modifier.

**Descripción oficial:**

A getter for [SET_PLAYER_MELEE_WEAPON_DEFENSE_MODIFIER](../gta5/PLAYER.md#setplayermeleeweapondefensemodifier).

---
### GetPlayerServerId

`GET_PLAYER_SERVER_ID` · hash `0x4D97BCC7` · **Cliente**

```lua
local retval = GetPlayerServerId(player)
```
```c
int GET_PLAYER_SERVER_ID(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `int`

---
### GetPlayerStamina

`GET_PLAYER_STAMINA` · hash `0xE415EC5C` · **Cliente**

```lua
local retval = GetPlayerStamina(playerId)
```
```c
float GET_PLAYER_STAMINA(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player stamina.

---
### GetPlayerVehicleDamageModifier

`GET_PLAYER_VEHICLE_DAMAGE_MODIFIER` · hash `0x78F27B1F` · **Cliente**

```lua
local retval = GetPlayerVehicleDamageModifier(playerId)
```
```c
float GET_PLAYER_VEHICLE_DAMAGE_MODIFIER(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player vehicle damage modifier.

**Descripción oficial:**

A getter for [SET_PLAYER_VEHICLE_DAMAGE_MODIFIER](../gta5/PLAYER.md#setplayervehicledamagemodifier).

---
### GetPlayerVehicleDefenseModifier

`GET_PLAYER_VEHICLE_DEFENSE_MODIFIER` · hash `0x8326E7CD` · **Cliente**

```lua
local retval = GetPlayerVehicleDefenseModifier(playerId)
```
```c
float GET_PLAYER_VEHICLE_DEFENSE_MODIFIER(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player vehicle defense modifier.

**Descripción oficial:**

A getter for [SET_PLAYER_VEHICLE_DEFENSE_MODIFIER](../gta5/PLAYER.md#setplayervehicledefensemodifier).

---
### GetRandomVehicleDensityMultiplier

`GET_RANDOM_VEHICLE_DENSITY_MULTIPLIER` · hash `0x7B0D00C5` · **Cliente**

```lua
local retval = GetRandomVehicleDensityMultiplier()
```
```c
float GET_RANDOM_VEHICLE_DENSITY_MULTIPLIER();
```

**Devuelve:** `float` — Returns random vehicle density multiplier value.

**Descripción oficial:**

A getter for [SET_RANDOM_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME](../gta5/VEHICLE-2.md#setrandomvehicledensitymultiplierthisframe).
Same as vehicle density multiplier.

---
### GetRopeFlags

`GET_ROPE_FLAGS` · hash `0xA80FFE99` · **Cliente**

```lua
local retval = GetRopeFlags(rope)
```
```c
int GET_ROPE_FLAGS(int rope);
```

**Parámetros**

- `rope` (`int`): The rope to get the flags for.

**Devuelve:** `int` — The rope's flags.

**Descripción oficial:**

```cpp
enum eRopeFlags
{
    DrawShadowEnabled = 2,
	Breakable = 4,
	RopeUnwindingFront = 8,
	RopeWinding = 32
}
```

---
### GetRopeLengthChangeRate

`GET_ROPE_LENGTH_CHANGE_RATE` · hash `0x66D70EA3` · **Cliente**

```lua
local retval = GetRopeLengthChangeRate(rope)
```
```c
float GET_ROPE_LENGTH_CHANGE_RATE(int rope);
```

**Parámetros**

- `rope` (`int`): The rope to get the length change rate for.

**Devuelve:** `float` — The rope's length change rate.

---
### GetRopeTimeMultiplier

`GET_ROPE_TIME_MULTIPLIER` · hash `0xF341E6CA` · **Cliente**

```lua
local retval = GetRopeTimeMultiplier(rope)
```
```c
float GET_ROPE_TIME_MULTIPLIER(int rope);
```

**Parámetros**

- `rope` (`int`): The rope to get the time multiplier for.

**Devuelve:** `float` — The rope's time multiplier.

---
### GetRopeUpdateOrder

`GET_ROPE_UPDATE_ORDER` · hash `0x2AB2E0F6` · **Cliente**

```lua
local retval = GetRopeUpdateOrder(rope)
```
```c
int GET_ROPE_UPDATE_ORDER(int rope);
```

**Parámetros**

- `rope` (`int`): The rope to get the update order for.

**Devuelve:** `int` — The rope's update order.

---
### GetRuntimeTextureHeight

`GET_RUNTIME_TEXTURE_HEIGHT` · hash `0x3574AACE` · **Cliente**

```lua
local retval = GetRuntimeTextureHeight(tex)
```
```c
int GET_RUNTIME_TEXTURE_HEIGHT(long tex);
```

**Parámetros**

- `tex` (`long`): A handle to the runtime texture.

**Devuelve:** `int` — The height in pixels.

**Descripción oficial:**

Gets the height of the specified runtime texture.

---
### GetRuntimeTexturePitch

`GET_RUNTIME_TEXTURE_PITCH` · hash `0xCA0A085F` · **Cliente**

```lua
local retval = GetRuntimeTexturePitch(tex)
```
```c
int GET_RUNTIME_TEXTURE_PITCH(long tex);
```

**Parámetros**

- `tex` (`long`): A handle to the runtime texture.

**Devuelve:** `int` — The row pitch in bytes.

**Descripción oficial:**

Gets the row pitch of the specified runtime texture, for use when creating data for `SET_RUNTIME_TEXTURE_ARGB_DATA`.

---
### GetRuntimeTextureWidth

`GET_RUNTIME_TEXTURE_WIDTH` · hash `0xC9F55558` · **Cliente**

```lua
local retval = GetRuntimeTextureWidth(tex)
```
```c
int GET_RUNTIME_TEXTURE_WIDTH(long tex);
```

**Parámetros**

- `tex` (`long`): A handle to the runtime texture.

**Devuelve:** `int` — The width in pixels.

**Descripción oficial:**

Gets the width of the specified runtime texture.

---
### GetScenarioPedDensityMultiplier

`GET_SCENARIO_PED_DENSITY_MULTIPLIER` · hash `0x77C598B2` · **Cliente**

```lua
local retval = GetScenarioPedDensityMultiplier()
```
```c
float GET_SCENARIO_PED_DENSITY_MULTIPLIER();
```

**Devuelve:** `float` — Returns scenario ped density multiplier value.

**Descripción oficial:**

A getter for [SET_SCENARIO_PED_DENSITY_MULTIPLIER_THIS_FRAME](../gta5/PED-2.md#setscenariopeddensitymultiplierthisframe).

---
### GetTimecycleModifierCount

`GET_TIMECYCLE_MODIFIER_COUNT` · hash `0xFE2A1D4D` · **Cliente**

```lua
local retval = GetTimecycleModifierCount()
```
```c
int GET_TIMECYCLE_MODIFIER_COUNT();
```

**Devuelve:** `int` — Returns the amount of timecycle modifiers loaded.

**Ejemplo (lua):**

```lua
local count = GetTimecycleModifierCount()
print("we have  " .. count .. "timecycle modifiers loaded")
```

---
### GetTimecycleModifierIndexByName

`GET_TIMECYCLE_MODIFIER_INDEX_BY_NAME` · hash `0x5F4CD0E2` · **Cliente**

```lua
local retval = GetTimecycleModifierIndexByName(modifierName)
```
```c
int GET_TIMECYCLE_MODIFIER_INDEX_BY_NAME(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`): The timecycle modifier name.

**Devuelve:** `int` — The timecycle modifier index.

**Ejemplo (lua):**

```lua
local modifierIndex = GetTimecycleModifierIndexByName("underwater")
local currentIndex = GetTimecycleModifierIndex()

if currentIndex ~= -1 and currentIndex == modifierIndex then
  print("we're actually using 'underwater' timecycle!")
end
```

---
### GetTimecycleModifierNameByIndex

`GET_TIMECYCLE_MODIFIER_NAME_BY_INDEX` · hash `0x28CB8608` · **Cliente**

```lua
local retval = GetTimecycleModifierNameByIndex(modifierIndex)
```
```c
char* GET_TIMECYCLE_MODIFIER_NAME_BY_INDEX(int modifierIndex);
```

**Parámetros**

- `modifierIndex` (`int`): The timecycle modifier index.

**Devuelve:** `char*` — The timecycle modifier name.

**Ejemplo (lua):**

```lua
local modifierIndex = GetTimecycleModifierIndex()

if modifierIndex ~= -1 then
  local modifierName = GetTimecycleModifierNameByIndex(modifierIndex)
  print("current timecycle name is " .. modifierName)
end
```

---
### GetTimecycleModifierStrength

`GET_TIMECYCLE_MODIFIER_STRENGTH` · hash `0xBE54124A` · **Cliente**

```lua
local retval = GetTimecycleModifierStrength()
```
```c
float GET_TIMECYCLE_MODIFIER_STRENGTH();
```

**Devuelve:** `float` — Returns current timecycle modifier strength.

**Descripción oficial:**

A getter for [SET_TIMECYCLE_MODIFIER_STRENGTH](../gta5/GRAPHICS.md#settimecyclemodifierstrength).

---
### GetTimecycleModifierVar

`GET_TIMECYCLE_MODIFIER_VAR` · hash `0xA7109E12` · **Cliente**

```lua
local retval, value1, value2 = GetTimecycleModifierVar(modifierName, varName)
```
```c
BOOL GET_TIMECYCLE_MODIFIER_VAR(char* modifierName, char* varName, float* value1, float* value2);
```

**Parámetros**

- `modifierName` (`char*`): The name of timecycle modifier.
- `varName` (`char*`): The name of timecycle variable.
- `value1` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `value2` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL` — Whether or not variable by name was found on the specified timecycle modifier.

**Ejemplo (lua):**

```lua
local modifierName = "superDARK"
local varName = "postfx_noise"

if DoesTimecycleModifierHasVar(modifierName, varName) then
  local success, value1, value2 = GetTimecycleModifierVar(modifierName, varName)

  if success then
    print(string.format("[%s] removed var %s with values: %f %f", modifierName, varName, value1, value2))
    RemoveTimecycleModifierVar(modifierName, varName)
  end
else
    SetTimecycleModifierVar(modifierName, varName, 1.0, 1.0)
    print(string.format("[%s] created var %s", modifierName, varName))
end
```

---
### GetTimecycleModifierVarCount

`GET_TIMECYCLE_MODIFIER_VAR_COUNT` · hash `0x60FB60FE` · **Cliente**

```lua
local retval = GetTimecycleModifierVarCount(modifierName)
```
```c
int GET_TIMECYCLE_MODIFIER_VAR_COUNT(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`): The timecycle modifier name.

**Devuelve:** `int` — The amount of variables used on a specified timecycle modifier.

**Ejemplo (lua):**

```lua
local varCount = GetTimecycleModifierVarCount("underwater")

if varCount ~= 0 then
  for index = 0, varCount - 1 do
    local varName = GetTimecycleModifierVarNameByIndex(index)

    print(string.format("[%d] %s", index, varName))
  end
end
```

---
### GetTimecycleModifierVarNameByIndex

`GET_TIMECYCLE_MODIFIER_VAR_NAME_BY_INDEX` · hash `0xE874AB1D` · **Cliente**

```lua
local retval = GetTimecycleModifierVarNameByIndex(modifierName, modifierVarIndex)
```
```c
char* GET_TIMECYCLE_MODIFIER_VAR_NAME_BY_INDEX(char* modifierName, int modifierVarIndex);
```

**Parámetros**

- `modifierName` (`char*`): The name of timecycle modifier.
- `modifierVarIndex` (`int`): The index of a variable on the specified timecycle modifier.

**Devuelve:** `char*` — The name of a variable by index.

**Ejemplo (lua):**

```lua
local varCount = GetTimecycleModifierVarCount("underwater")

if varCount ~= 0 then
  for index = 0, varCount - 1 do
    local varName = GetTimecycleModifierVarNameByIndex(index)

    print(string.format("[%d] %s", index, varName))
  end
end
```

---
### GetTimecycleVarCount

`GET_TIMECYCLE_VAR_COUNT` · hash `0x838B34D8` · **Cliente**

```lua
local retval = GetTimecycleVarCount()
```
```c
int GET_TIMECYCLE_VAR_COUNT();
```

**Devuelve:** `int` — The amount of available variables for timecycle modifiers.

**Descripción oficial:**

Returns the amount of variables available to be applied on timecycle modifiers.

**Ejemplo (lua):**

```lua
local varCount = GetTimecycleVarCount()

if varCount ~= 0 then
  for index = 0, varCount - 1 do
    local varName = GetTimecycleVarNameByIndex(index)
    local varDefault = GetTimecycleVarDefaultValueByIndex(index)

    print(string.format("[%d] %s (%f)", index, varName, varDefault))
  end
end
```

---
### GetTimecycleVarDefaultValueByIndex

`GET_TIMECYCLE_VAR_DEFAULT_VALUE_BY_INDEX` · hash `0x3B90238` · **Cliente**

```lua
local retval = GetTimecycleVarDefaultValueByIndex(varIndex)
```
```c
float GET_TIMECYCLE_VAR_DEFAULT_VALUE_BY_INDEX(int varIndex);
```

**Parámetros**

- `varIndex` (`int`): The index of variable.

**Devuelve:** `float` — The default value of a timecycle variable.

**Descripción oficial:**

See [GET_TIMECYCLE_VAR_COUNT](#gettimecyclevarcount).

**Ejemplo (lua):**

```lua
local varCount = GetTimecycleVarCount()

if varCount ~= 0 then
  for index = 0, varCount - 1 do
    local varName = GetTimecycleVarNameByIndex(index)
    local varDefault = GetTimecycleVarDefaultValueByIndex(index)

    print(string.format("[%d] %s (%f)", index, varName, varDefault))
  end
end
```

---
### GetTimecycleVarNameByIndex

`GET_TIMECYCLE_VAR_NAME_BY_INDEX` · hash `0xC6C55AAF` · **Cliente**

```lua
local retval = GetTimecycleVarNameByIndex(varIndex)
```
```c
char* GET_TIMECYCLE_VAR_NAME_BY_INDEX(int varIndex);
```

**Parámetros**

- `varIndex` (`int`): The index of variable.

**Devuelve:** `char*` — The name of a timecycle variable.

**Descripción oficial:**

See [GET_TIMECYCLE_VAR_COUNT](#gettimecyclevarcount).

**Ejemplo (lua):**

```lua
local varCount = GetTimecycleVarCount()

if varCount ~= 0 then
  for index = 0, varCount - 1 do
    local varName = GetTimecycleVarNameByIndex(index)
    local varDefault = GetTimecycleVarDefaultValueByIndex(index)

    print(string.format("[%d] %s (%f)", index, varName, varDefault))
  end
end
```

---
### GetTrackBrakingDistance

`GET_TRACK_BRAKING_DISTANCE` · hash `0xBF482A5E` · **Cliente**

```lua
local retval = GetTrackBrakingDistance(track)
```
```c
float GET_TRACK_BRAKING_DISTANCE(int track);
```

**Parámetros**

- `track` (`int`): The track id (between 0 - 27)

**Devuelve:** `float` — The braking distance of the track. Used by trains to determine the point to slow down at when entering a station.

---
### GetTrackMaxSpeed

`GET_TRACK_MAX_SPEED` · hash `0x34EE2BF3` · **Cliente**

```lua
local retval = GetTrackMaxSpeed(track)
```
```c
float GET_TRACK_MAX_SPEED(int track);
```

**Parámetros**

- `track` (`int`): The track id (between 0 - 27)

**Devuelve:** `float` — The max speed of the track

---
### GetTrackNodeCoords

`GET_TRACK_NODE_COORDS` · hash `0x1628548E` · **Cliente**

```lua
local retval, coords = GetTrackNodeCoords(trackIndex, trackNode, coords)
```
```c
bool GET_TRACK_NODE_COORDS(int trackIndex, int trackNode, Vector3* coords);
```

**Parámetros**

- `trackIndex` (`int`): The track index
- `trackNode` (`int`): The track node
- `coords` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The resulting track node coords

**Devuelve:** `bool` — Returns if it succeeds in getting coords or not

**Descripción oficial:**

Gets the coordinates of a specific track node.

---
### GetTrackNodeCount

`GET_TRACK_NODE_COUNT` · hash `0x896A0C11` · **Cliente**

```lua
local retval = GetTrackNodeCount(trackIndex)
```
```c
int GET_TRACK_NODE_COUNT(int trackIndex);
```

**Parámetros**

- `trackIndex` (`int`): The track index

**Devuelve:** `int` — The amount of track nodes on the specified track

**Descripción oficial:**

Gets the specified tracks node count.

---
### GetTrainCurrentTrackNode

`GET_TRAIN_CURRENT_TRACK_NODE` · hash `0xE015E854` · **Cliente**

```lua
local retval = GetTrainCurrentTrackNode(train)
```
```c
int GET_TRAIN_CURRENT_TRACK_NODE(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The target train.

**Devuelve:** `int` — Train's current track node index.

---
### GetTrainDoorCount

`GET_TRAIN_DOOR_COUNT` · hash `0x99974721` · **Cliente**

```lua
local retval = GetTrainDoorCount(train)
```
```c
int GET_TRAIN_DOOR_COUNT(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train to obtain the door count for.

**Devuelve:** `int` — The door count.

**Descripción oficial:**

Gets the door count for the specified train.

---
### GetTrainDoorOpenRatio

`GET_TRAIN_DOOR_OPEN_RATIO` · hash `0x40B16551` · **Cliente**

```lua
local retval = GetTrainDoorOpenRatio(train, doorIndex)
```
```c
float GET_TRAIN_DOOR_OPEN_RATIO(Vehicle train, int doorIndex);
```

**Parámetros**

- `train` (`Vehicle`): The train to obtain the door ratio for.
- `doorIndex` (`int`): Zero-based door index.

**Devuelve:** `float` — A value between 0.0 (fully closed) and 1.0 (fully open).

**Descripción oficial:**

Gets the ratio that a door is open for on a train.

**Ejemplo (lua):**

```lua
local doorCount = GetTrainDoorCount(train)
for doorIndex = 0, doorCount - 1 do
    local ratio = GetTrainDoorOpenRatio(train, doorIndex)
    print("Door " .. tostring(doorIndex) .. " is open by a ratio of " .. tostring(ratio))
end
```

**Ejemplo (cs):**

```cs
int doorCount = API.GetTrainDoorCount(train);
for (int doorIndex = 0; doorIndex < doorCount; doorIndex++)
{
    float ratio = API.GetTrainDoorOpenRatio(train, doorIndex);
    Debug.WriteLine($"Door {doorIndex} is open by a ratio of {ratio}");
}
```

---
### GetTrainSpeed

`GET_TRAIN_SPEED` · hash `0x428668B7` · **Cliente**

```lua
local retval = GetTrainSpeed(train)
```
```c
float GET_TRAIN_SPEED(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `float` — The current speed of the train

**Descripción oficial:**

Gets the speed the train is currently going.

---
### GetVehicleAlarmTimeLeft

`GET_VEHICLE_ALARM_TIME_LEFT` · hash `0xC62AAC98` · **Cliente**

```lua
local retval = GetVehicleAlarmTimeLeft(vehicle)
```
```c
int GET_VEHICLE_ALARM_TIME_LEFT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleCheatPowerIncrease

`GET_VEHICLE_CHEAT_POWER_INCREASE` · hash `0xC3C93F28` · **Cliente**

```lua
local retval = GetVehicleCheatPowerIncrease(vehicle)
```
```c
float GET_VEHICLE_CHEAT_POWER_INCREASE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `float` — Returns vehicle's cheat power increase modifier value.

**Descripción oficial:**

A getter for [SET_VEHICLE_CHEAT_POWER_INCREASE](../gta5/VEHICLE-2.md#setvehiclecheatpowerincrease).

---
### GetVehicleClutch

`GET_VEHICLE_CLUTCH` · hash `0x1DAD4583` · **Cliente**

```lua
local retval = GetVehicleClutch(vehicle)
```
```c
float GET_VEHICLE_CLUTCH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleCurrentGear

`GET_VEHICLE_CURRENT_GEAR` · hash `0xB4F4E566` · **Cliente**

```lua
local retval = GetVehicleCurrentGear(vehicle)
```
```c
int GET_VEHICLE_CURRENT_GEAR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleCurrentRpm

`GET_VEHICLE_CURRENT_RPM` · hash `0xE7B12B54` · **Cliente**

```lua
local retval = GetVehicleCurrentRpm(vehicle)
```
```c
float GET_VEHICLE_CURRENT_RPM(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleDashboardBoost

`GET_VEHICLE_DASHBOARD_BOOST` · hash `0xDFFABA2A` · **Cliente**

```lua
local retval = GetVehicleDashboardBoost()
```
```c
float GET_VEHICLE_DASHBOARD_BOOST();
```

**Devuelve:** `float`

---
### GetVehicleDashboardCurrentGear

`GET_VEHICLE_DASHBOARD_CURRENT_GEAR` · hash `0x435C86F4` · **Cliente**

```lua
local retval = GetVehicleDashboardCurrentGear()
```
```c
float GET_VEHICLE_DASHBOARD_CURRENT_GEAR();
```

**Devuelve:** `float` — The current gear.

**Descripción oficial:**

Retrieves the current gear displayed on the dashboard of the vehicle the player is in, returned as a float. This value represents the gear shown in the instrument cluster, such as "R" (0.0) or positive values (e.g., 1.0, 2.0, etc.) for drive gears.

**Nombres antiguos (alias):** `GET_VEHICLE_DASHBOARD_WATER_TEMP` (`GetVehicleDashboardWaterTemp`)

---
### GetVehicleDashboardFuel

`GET_VEHICLE_DASHBOARD_FUEL` · hash `0x19B0B2CE` · **Cliente**

```lua
local retval = GetVehicleDashboardFuel()
```
```c
float GET_VEHICLE_DASHBOARD_FUEL();
```

**Devuelve:** `float`

---
### GetVehicleDashboardLights

`GET_VEHICLE_DASHBOARD_LIGHTS` · hash `0x500FFE9D` · **Cliente**

```lua
local retval = GetVehicleDashboardLights()
```
```c
int GET_VEHICLE_DASHBOARD_LIGHTS();
```

**Devuelve:** `int`

**Descripción oficial:**

Gets the state of the player vehicle's dashboard lights as a bit set
indicator_left = 1
indicator_right = 2
handbrakeLight = 4
engineLight = 8
ABSLight = 16
gasLight = 32
oilLight = 64
headlights = 128
highBeam = 256
batteryLight = 512

---
### GetVehicleDashboardOilPressure

`GET_VEHICLE_DASHBOARD_OIL_PRESSURE` · hash `0x3856D767` · **Cliente**

```lua
local retval = GetVehicleDashboardOilPressure()
```
```c
float GET_VEHICLE_DASHBOARD_OIL_PRESSURE();
```

**Devuelve:** `float`

---
### GetVehicleDashboardOilTemp

`GET_VEHICLE_DASHBOARD_OIL_TEMP` · hash `0x1F5996AA` · **Cliente**

```lua
local retval = GetVehicleDashboardOilTemp()
```
```c
float GET_VEHICLE_DASHBOARD_OIL_TEMP();
```

**Devuelve:** `float`

---
### GetVehicleDashboardRpm

`GET_VEHICLE_DASHBOARD_RPM` · hash `0xF9716A11` · **Cliente**

```lua
local retval = GetVehicleDashboardRpm()
```
```c
float GET_VEHICLE_DASHBOARD_RPM();
```

**Devuelve:** `float` — float 0 to ~1.1 representing the angle of the rpm gauge on the player's vehicle dashboard

---
### GetVehicleDashboardSpeed

`GET_VEHICLE_DASHBOARD_SPEED` · hash `0x9AAD420E` · **Cliente**

```lua
local retval = GetVehicleDashboardSpeed(vehicle)
```
```c
float GET_VEHICLE_DASHBOARD_SPEED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleDashboardTemp

`GET_VEHICLE_DASHBOARD_TEMP` · hash `0x6B6ADAFA` · **Cliente**

```lua
local retval = GetVehicleDashboardTemp()
```
```c
float GET_VEHICLE_DASHBOARD_TEMP();
```

**Devuelve:** `float`

---
### GetVehicleDashboardVacuum

`GET_VEHICLE_DASHBOARD_VACUUM` · hash `0xFABE67A9` · **Cliente**

```lua
local retval = GetVehicleDashboardVacuum()
```
```c
float GET_VEHICLE_DASHBOARD_VACUUM();
```

**Devuelve:** `float`

---
### GetVehicleDensityMultiplier

`GET_VEHICLE_DENSITY_MULTIPLIER` · hash `0xEF7C6538` · **Cliente**

```lua
local retval = GetVehicleDensityMultiplier()
```
```c
float GET_VEHICLE_DENSITY_MULTIPLIER();
```

**Devuelve:** `float` — Returns vehicle density multiplier value.

**Descripción oficial:**

A getter for [SET_VEHICLE_DENSITY_MULTIPLIER_THIS_FRAME](../gta5/VEHICLE-2.md#setvehicledensitymultiplierthisframe).

---
### GetVehicleDrawnWheelAngleMult

`GET_VEHICLE_DRAWN_WHEEL_ANGLE_MULT` · hash `0x21C1DA8E` · **Cliente**

```lua
local retval = GetVehicleDrawnWheelAngleMult(vehicle)
```
```c
float GET_VEHICLE_DRAWN_WHEEL_ANGLE_MULT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

**Descripción oficial:**

Gets a vehicle's multiplier used with a wheel's GET_VEHICLE_WHEEL_STEERING_ANGLE to determine the angle the wheel is rendered.

---
### GetVehicleEngineTemperature

`GET_VEHICLE_ENGINE_TEMPERATURE` · hash `0xF4F495CB` · **Cliente**

```lua
local retval = GetVehicleEngineTemperature(vehicle)
```
```c
float GET_VEHICLE_ENGINE_TEMPERATURE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleFuelLevel

`GET_VEHICLE_FUEL_LEVEL` · hash `0x5F739BB8` · **Cliente**

```lua
local retval = GetVehicleFuelLevel(vehicle)
```
```c
float GET_VEHICLE_FUEL_LEVEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleGearRatio

`GET_VEHICLE_GEAR_RATIO` · hash `0x82E794B7` · **Cliente**

```lua
local retval = GetVehicleGearRatio(vehicle, gear)
```
```c
float GET_VEHICLE_GEAR_RATIO(Vehicle vehicle, int gear);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `gear` (`int`): The vehicles gear you want to get.

**Devuelve:** `float`

**Descripción oficial:**

Gets vehicles gear ratio on choosen gear.

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(-1))
local currentGear = GetVehicleCurrentGear(Vehicle)

print(GetVehicleGearRatio(vehicle, currentGear)) -- will print current vehicle gear to console
```

**Ejemplo (js):**

```js
const vehicle = GetVehiclePedIsIn(PlayerPedId(-1));
const currentGear = GetVehicleCurrentGear(Vehicle);

console.log(GetVehicleGearRatio(vehicle, currentGear)); // will print current vehicle gear to console
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.API;

Vehicle vehicle = Game.PlayerPed.CurrentVehicle;
int currentGear = GetVehicleCurrentGear(vehicle.Handle);

Debug.WriteLine($"{GetVehicleGearRatio(vehicle.Handle, currentGear)}");
```

---
### GetVehicleGravityAmount

`GET_VEHICLE_GRAVITY_AMOUNT` · hash `0xB48A1292` · **Cliente**

```lua
local retval = GetVehicleGravityAmount(vehicle)
```
```c
float GET_VEHICLE_GRAVITY_AMOUNT(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleHandlingFloat

`GET_VEHICLE_HANDLING_FLOAT` · hash `0x642FC12F` · **Cliente**

```lua
local retval = GetVehicleHandlingFloat(vehicle, class_, fieldName)
```
```c
float GET_VEHICLE_HANDLING_FLOAT(Vehicle vehicle, char* class_, char* fieldName);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `class_` (`char*`): The handling class to get. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to get. These match the keys in `handling.meta`.

**Devuelve:** `float` — A floating-point value.

**Descripción oficial:**

Returns the effective handling data of a vehicle as a floating-point value.
Example: `local fSteeringLock = GetVehicleHandlingFloat(vehicle, 'CHandlingData', 'fSteeringLock')`

---
### GetVehicleHandlingInt

`GET_VEHICLE_HANDLING_INT` · hash `0x27396C75` · **Cliente**

```lua
local retval = GetVehicleHandlingInt(vehicle, class_, fieldName)
```
```c
int GET_VEHICLE_HANDLING_INT(Vehicle vehicle, char* class_, char* fieldName);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `class_` (`char*`): The handling class to get. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to get. These match the keys in `handling.meta`.

**Devuelve:** `int` — An integer.

**Descripción oficial:**

Returns the effective handling data of a vehicle as an integer value.
Example: `local modelFlags = GetVehicleHandlingInt(vehicle, 'CHandlingData', 'strModelFlags')`

---
### GetVehicleHandlingVector

`GET_VEHICLE_HANDLING_VECTOR` · hash `0xFB341304` · **Cliente**

```lua
local retval = GetVehicleHandlingVector(vehicle, class_, fieldName)
```
```c
Vector3 GET_VEHICLE_HANDLING_VECTOR(Vehicle vehicle, char* class_, char* fieldName);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `class_` (`char*`): The handling class to get. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to get. These match the keys in `handling.meta`.

**Devuelve:** `Vector3` — An integer.

**Descripción oficial:**

Returns the effective handling data of a vehicle as a vector value.
Example: `local inertiaMultiplier = GetVehicleHandlingVector(vehicle, 'CHandlingData', 'vecInertiaMultiplier')`

---
### GetVehicleHasFlag

`GET_VEHICLE_HAS_FLAG` · hash `0xD85C9F57` · **Cliente**

```lua
local retval = GetVehicleHasFlag(vehicle, flagIndex)
```
```c
bool GET_VEHICLE_HAS_FLAG(Vehicle vehicle, int flagIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain flags for.
- `flagIndex` (`int`): Flag index.

**Devuelve:** `bool` — A boolean for whether the flag is set.### Example```lua local vehicleFlags = {
     FLAG_SMALL_WORKER = 0,
     FLAG_BIG = 1,
     FLAG_NO_BOOT = 2,
     FLAG_ONLY_DURING_OFFICE_HOURS = 3
     -- This is just a example, see fivem-docs to see all flags.
 }
 
 local function getAllVehicleFlags(vehicle)
     local flags = {}
     for i = 0, 256 do
         if GetVehicleHasFlag(vehicle, i) then
             flags[#flags+1] = i
         end
     end
     return flags
 end
 
 local flagsVehicle = GetVehiclePedIsIn(PlayerPedId(), false)
 print(getAllVehicleFlags) ``````javascript const VEHICLE_FLAGS = {
     FLAG_SMALL_WORKER: 0,
     FLAG_BIG: 1,
     FLAG_NO_BOOT: 2,
     FLAG_ONLY_DURING_OFFICE_HOURS: 3
     // This is just a example, see fivem-docs to see all flags.
 };
 
 function getAllVehicleFlags(mVehicle = GetVehiclePedIsIn(PlayerPedId(), false)) {
     const flags = [];
     for (let i = 0; i < 204; i++) {
         if (GetVehicleHasFlag(mVehicle, i)) {
             flags.push(i);
         }
     }
     return flags;
 }
 
 let flagsVehicle = GetVehiclePedIsIn(PlayerPedId(), false);
 console.log(getAllVehicleFlags); ```

**Descripción oficial:**

**Note**: Flags are not the same based on your `gamebuild`. Please see [here](https://docs.fivem.net/docs/game-references/vehicle-references/vehicle-flags) to see a complete list of all vehicle flags.

Get vehicle.meta flag by index. Useful examples include `FLAG_LAW_ENFORCEMENT` (31), `FLAG_RICH_CAR` (36), `FLAG_IS_ELECTRIC` (43), `FLAG_IS_OFFROAD_VEHICLE` (48).

---
### GetVehicleHighGear

`GET_VEHICLE_HIGH_GEAR` · hash `0xF1D1D689` · **Cliente**

```lua
local retval = GetVehicleHighGear(vehicle)
```
```c
int GET_VEHICLE_HIGH_GEAR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleIndicatorLights

`GET_VEHICLE_INDICATOR_LIGHTS` · hash `0x83070354` · **Cliente**

```lua
local retval = GetVehicleIndicatorLights(vehicle)
```
```c
int GET_VEHICLE_INDICATOR_LIGHTS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int` — An integer.

**Descripción oficial:**

Gets the vehicle indicator light state. 0 = off, 1 = left, 2 = right, 3 = both

---
### GetVehicleLightMultiplier

`GET_VEHICLE_LIGHT_MULTIPLIER` · hash `0x7E6E219C` · **Cliente**

```lua
local retval = GetVehicleLightMultiplier(vehicle)
```
```c
float GET_VEHICLE_LIGHT_MULTIPLIER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleNextGear

`GET_VEHICLE_NEXT_GEAR` · hash `0xDDB298AE` · **Cliente**

```lua
local retval = GetVehicleNextGear(vehicle)
```
```c
int GET_VEHICLE_NEXT_GEAR(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleNumberOfWheels

`GET_VEHICLE_NUMBER_OF_WHEELS` · hash `0xEDF4B0FC` · **Cliente**

```lua
local retval = GetVehicleNumberOfWheels(vehicle)
```
```c
int GET_VEHICLE_NUMBER_OF_WHEELS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

---
### GetVehicleOilLevel

`GET_VEHICLE_OIL_LEVEL` · hash `0xFC7F8EF4` · **Cliente**

```lua
local retval = GetVehicleOilLevel(vehicle)
```
```c
float GET_VEHICLE_OIL_LEVEL(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleSteeringScale

`GET_VEHICLE_STEERING_SCALE` · hash `0x954465DE` · **Cliente**

```lua
local retval = GetVehicleSteeringScale(vehicle)
```
```c
float GET_VEHICLE_STEERING_SCALE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleThrottleOffset

`GET_VEHICLE_THROTTLE_OFFSET` · hash `0xD1D07351` · **Cliente**

```lua
local retval = GetVehicleThrottleOffset(vehicle)
```
```c
float GET_VEHICLE_THROTTLE_OFFSET(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float` — A float among -1 and 1 according if the vehicle is moving forwards or backwards

**Nombres antiguos (alias):** `GET_VEHICLE_CURRENT_ACCELERATION` (`GetVehicleCurrentAcceleration`)

---
### GetVehicleTopSpeedModifier

`GET_VEHICLE_TOP_SPEED_MODIFIER` · hash `0x998B7FEE` · **Cliente**

```lua
local retval = GetVehicleTopSpeedModifier(vehicle)
```
```c
float GET_VEHICLE_TOP_SPEED_MODIFIER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.

**Devuelve:** `float` — Returns vehicle's modified top speed.

**Descripción oficial:**

A getter for [MODIFY_VEHICLE_TOP_SPEED](../gta5/VEHICLE-1.md#modifyvehicletopspeed). Returns -1.0 if a modifier is not set.

---
### GetVehicleTurboPressure

`GET_VEHICLE_TURBO_PRESSURE` · hash `0xE02B51D7` · **Cliente**

```lua
local retval = GetVehicleTurboPressure(vehicle)
```
```c
float GET_VEHICLE_TURBO_PRESSURE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleTypeRaw

`GET_VEHICLE_TYPE_RAW` · hash `0xDE73BC10` · **Cliente**

```lua
local retval = GetVehicleTypeRaw(vehicle)
```
```c
int GET_VEHICLE_TYPE_RAW(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle's entity handle.

**Devuelve:** `int` — Returns the vehicles model type

**Descripción oficial:**

Returns the model type of the vehicle as defined by:

```cpp
enum VehicleType
{
	VEHICLE_TYPE_NONE = -1,
	VEHICLE_TYPE_CAR = 0,
	VEHICLE_TYPE_PLANE = 1,
	VEHICLE_TYPE_TRAILER = 2,
	VEHICLE_TYPE_QUADBIKE = 3,
	VEHICLE_TYPE_DRAFT = 4,
	VEHICLE_TYPE_SUBMARINECAR = 5,
	VEHICLE_TYPE_AMPHIBIOUS_AUTOMOBILE = 6,
	VEHICLE_TYPE_AMPHIBIOUS_QUADBIKE = 7,
	VEHICLE_TYPE_HELI = 8,
	VEHICLE_TYPE_BLIMP = 9,
	VEHICLE_TYPE_AUTOGYRO = 10,
	VEHICLE_TYPE_BIKE = 11,
	VEHICLE_TYPE_BICYCLE = 12,
	VEHICLE_TYPE_BOAT = 13,
	VEHICLE_TYPE_TRAIN = 14,
	VEHICLE_TYPE_SUBMARINE = 15,
};
```

---
### GetVehicleWheelBrakePressure

`GET_VEHICLE_WHEEL_BRAKE_PRESSURE` · hash `0x70FE2EFF` · **Cliente**

```lua
local retval = GetVehicleWheelBrakePressure(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_BRAKE_PRESSURE(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

Gets brake pressure of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.
Normal values around 1.0f when braking.

---
### GetVehicleWheelFlags

`GET_VEHICLE_WHEEL_FLAGS` · hash `0xC70FA0C7` · **Cliente**

```lua
local retval = GetVehicleWheelFlags(vehicle, wheelIndex)
```
```c
int GET_VEHICLE_WHEEL_FLAGS(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `int` — An unsigned int containing bit flags.

**Descripción oficial:**

Gets the flags of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### GetVehicleWheelHealth

`GET_VEHICLE_WHEEL_HEALTH` · hash `0x54A677F5` · **Cliente**

```lua
local retval = GetVehicleWheelHealth(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_HEALTH(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

---
### GetVehicleWheelIsPowered

`GET_VEHICLE_WHEEL_IS_POWERED` · hash `0x3CCF1B49` · **Cliente**

```lua
local retval = GetVehicleWheelIsPowered(vehicle, wheelIndex)
```
```c
BOOL GET_VEHICLE_WHEEL_IS_POWERED(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Gets whether the wheel is powered.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.
This is a shortcut to a flag in GET_VEHICLE_WHEEL_FLAGS.

---
### GetVehicleWheelPower

`GET_VEHICLE_WHEEL_POWER` · hash `0xD203287` · **Cliente**

```lua
local retval = GetVehicleWheelPower(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_POWER(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

Gets power being sent to a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### GetVehicleWheelRimColliderSize

`GET_VEHICLE_WHEEL_RIM_COLLIDER_SIZE` · hash `0xCEE21AB2` · **Cliente**

```lua
local retval = GetVehicleWheelRimColliderSize(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_RIM_COLLIDER_SIZE(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `wheelIndex` (`int`): Index of wheel, 0-3.

**Devuelve:** `float` — Float representing size of the rim collider. Not sure what it is used for, probably to detect whether bullets hit rim or tire and puncture it (and to determine size of the wheel when tire is fully blown).

---
### GetVehicleWheelRotationSpeed

`GET_VEHICLE_WHEEL_ROTATION_SPEED` · hash `0xEA1859E5` · **Cliente**

```lua
local retval = GetVehicleWheelRotationSpeed(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_ROTATION_SPEED(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float` — The angular velocity of the wheel.

**Descripción oficial:**

Gets the rotation speed of a wheel.
This is used internally to calcuate GET_VEHICLE_WHEEL_SPEED.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### GetVehicleWheelSize

`GET_VEHICLE_WHEEL_SIZE` · hash `0x4046B66` · **Cliente**

```lua
local retval = GetVehicleWheelSize(vehicle)
```
```c
float GET_VEHICLE_WHEEL_SIZE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.

**Devuelve:** `float` — Float representing size of the wheel (usually between 0.5 and 1.5)

**Descripción oficial:**

Returns vehicle's wheels' size (size is the same for all the wheels, cannot get/set specific wheel of vehicle).
Only works on non-default wheels (returns 0 in case of default wheels).

---
### GetVehicleWheelSpeed

`GET_VEHICLE_WHEEL_SPEED` · hash `0x149C9DA0` · **Cliente**

```lua
local retval = GetVehicleWheelSpeed(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_SPEED(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float` — An integer.

**Descripción oficial:**

Gets speed of a wheel at the tyre.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### GetVehicleWheelSteeringAngle

`GET_VEHICLE_WHEEL_STEERING_ANGLE` · hash `0xA0867448` · **Cliente**

```lua
local retval = GetVehicleWheelSteeringAngle(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_STEERING_ANGLE(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float` — The steering angle of the wheel, with 0 being straight.

**Descripción oficial:**

Gets steering angle of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### GetVehicleWheelSurfaceMaterial

`GET_VEHICLE_WHEEL_SURFACE_MATERIAL` · hash `0xA7F04022` · **Cliente**

```lua
local retval = GetVehicleWheelSurfaceMaterial(vehicle, wheelIndex)
```
```c
int GET_VEHICLE_WHEEL_SURFACE_MATERIAL(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `wheelIndex` (`int`): Index of wheel, 0-3.

**Devuelve:** `int` — Integer representing the index of the current surface material of that wheel. Check materials.dat for the indexes.

---
### GetVehicleWheelSuspensionCompression

`GET_VEHICLE_WHEEL_SUSPENSION_COMPRESSION` · hash `0x2B48175B` · **Cliente**

```lua
local retval = GetVehicleWheelSuspensionCompression(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_SUSPENSION_COMPRESSION(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float` — The current compression of the wheel's suspension.

**Descripción oficial:**

Gets the current suspension compression of a wheel.
Returns a positive value. 0 means the suspension is fully extended, the wheel is off the ground.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### GetVehicleWheelTireColliderSize

`GET_VEHICLE_WHEEL_TIRE_COLLIDER_SIZE` · hash `0xE0BA9FE6` · **Cliente**

```lua
local retval = GetVehicleWheelTireColliderSize(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_TIRE_COLLIDER_SIZE(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `wheelIndex` (`int`): Index of wheel, 0-3.

**Devuelve:** `float` — Float representing size of the wheel collider.

---
### GetVehicleWheelTireColliderWidth

`GET_VEHICLE_WHEEL_TIRE_COLLIDER_WIDTH` · hash `0xEF65929C` · **Cliente**

```lua
local retval = GetVehicleWheelTireColliderWidth(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_TIRE_COLLIDER_WIDTH(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `wheelIndex` (`int`): Index of wheel, 0-3.

**Devuelve:** `float` — Float representing width of the wheel collider.

---
### GetVehicleWheelTractionVectorLength

`GET_VEHICLE_WHEEL_TRACTION_VECTOR_LENGTH` · hash `0x3BCFEE14` · **Cliente**

```lua
local retval = GetVehicleWheelTractionVectorLength(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_TRACTION_VECTOR_LENGTH(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

Gets the traction vector length of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### GetVehicleWheelWidth

`GET_VEHICLE_WHEEL_WIDTH` · hash `0x9C7B59F9` · **Cliente**

```lua
local retval = GetVehicleWheelWidth(vehicle)
```
```c
float GET_VEHICLE_WHEEL_WIDTH(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.

**Devuelve:** `float` — Float representing width of the wheel (usually between 0.1 and 1.5)

**Descripción oficial:**

Returns vehicle's wheels' width (width is the same for all the wheels, cannot get/set specific wheel of vehicle).
Only works on non-default wheels (returns 0 in case of default wheels).

---
### GetVehicleWheelXOffset

`GET_VEHICLE_WHEEL_X_OFFSET` · hash `0xCC90CBCA` · **Cliente**

```lua
local retval = GetVehicleWheelXOffset(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_X_OFFSET(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

Returns the offset of the specified wheel relative to the wheel's axle center.

---
### GetVehicleWheelYRotation

`GET_VEHICLE_WHEEL_Y_ROTATION` · hash `0x2EA4AFFE` · **Cliente**

```lua
local retval = GetVehicleWheelYRotation(vehicle, wheelIndex)
```
```c
float GET_VEHICLE_WHEEL_Y_ROTATION(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `GET_VEHICLE_WHEEL_XROT` (`GetVehicleWheelXrot`)

---
### GetVehicleWheelieState

`GET_VEHICLE_WHEELIE_STATE` · hash `0x137260D1` · **Cliente**

```lua
local retval = GetVehicleWheelieState(vehicle)
```
```c
int GET_VEHICLE_WHEELIE_STATE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle

**Devuelve:** `int` — Vehicle's current wheelie state.

**Descripción oficial:**

List of known states:

```
1: Not wheeling.
65: Vehicle is ready to do wheelie (burnouting).
129: Vehicle is doing wheelie.
```

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
  while true do
    Wait(1)

    local veh = GetVehiclePedIsUsing(PlayerPedId())
    if veh ~= 0 then
      local wheelieState = GetVehicleWheelieState(veh)
      if wheelieState == 1 then
        print("Nothing")
      elseif wheelieState == 65 then
        print("Ready to wheelie!")
      elseif wheelieState == 129 then
        print("Doing wheelie!")
      end
    end
  end
end)
```

---
### GetVehicleXenonLightsCustomColor

`GET_VEHICLE_XENON_LIGHTS_CUSTOM_COLOR` · hash `0xC715F730` · **Cliente**

```lua
local retval, red, green, blue = GetVehicleXenonLightsCustomColor(vehicle)
```
```c
BOOL GET_VEHICLE_XENON_LIGHTS_CUSTOM_COLOR(Vehicle vehicle, int* red, int* green, int* blue);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `red` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Red color (0-255).
- `green` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Green color (0-255).
- `blue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Blue color (0-255).

**Devuelve:** `BOOL` — A boolean indicating if vehicle have custom xenon lights RGB color.

**Descripción oficial:**

Returns vehicle xenon lights custom RGB color values. Do note this native doesn't return non-RGB colors that was set with [\_SET_VEHICLE_XENON_LIGHTS_COLOR](../gta5/VEHICLE-2.md#setvehiclexenonlightscolor).

---
### GetVehicleXmasSnowFactor

`GET_VEHICLE_XMAS_SNOW_FACTOR` · hash `0x16605B30` · **Cliente**

```lua
local retval = GetVehicleXmasSnowFactor()
```
```c
float GET_VEHICLE_XMAS_SNOW_FACTOR();
```

**Devuelve:** `float` — Returns the grip factor for the vehicles wheels during xmas weather. default value is 0.2.

**Descripción oficial:**

A getter for [SET_VEHICLE_XMAS_SNOW_FACTOR](cliente-2.md#setvehiclexmassnowfactor).

---
### GetVisualSettingFloat

`GET_VISUAL_SETTING_FLOAT` · hash `0x15346B4D` · **Cliente**

```lua
local retval = GetVisualSettingFloat(name)
```
```c
float GET_VISUAL_SETTING_FLOAT(char* name);
```

**Parámetros**

- `name` (`char*`): The name of the value to get, such as `pedLight.color.red`.

**Devuelve:** `float` — Returns the floating point value of the specified visual setting on success.

**Descripción oficial:**

A getter for [SET_VISUAL_SETTING_FLOAT](cliente-2.md#setvisualsettingfloat).

---
### GetWaterQuadAlpha

`GET_WATER_QUAD_ALPHA` · hash `0x14088095` · **Cliente**

```lua
local retval, a0, a1, a2, a3 = GetWaterQuadAlpha(waterQuad)
```
```c
BOOL GET_WATER_QUAD_ALPHA(int waterQuad, int* a0, int* a1, int* a2, int* a3);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `a0` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The a0 level
- `a1` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The a1 level
- `a2` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The a2 level
- `a3` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The a3 level

**Devuelve:** `BOOL` — Returns true on success. Alpha values are undefined on failure

**Ejemplo (lua):**

```lua
local success, a0, a1, a2, a3 = GetWaterQuadAlpha(0)
```

---
### GetWaterQuadAtCoords

`GET_WATER_QUAD_AT_COORDS` · hash `0x17321452` · **Cliente**

```lua
local retval = GetWaterQuadAtCoords(x, y)
```
```c
int GET_WATER_QUAD_AT_COORDS(float x, float y);
```

**Parámetros**

- `x` (`float`): The X coordinate
- `y` (`float`): The Y coordinate

**Devuelve:** `int` — The water quad index at the given position. Returns -1 if there isn't any there.

**Descripción oficial:**

This native returns the index of a water quad if the given point is inside its bounds.

*If you also want to check for water level, check out [`GetWaterQuadAtCoords_3d`](#getwaterquadatcoords_3d)*

**Ejemplo (lua):**

```lua
local currentPedPosition = GetEntityCoords(PlayerPedId())
local waterQuadIndex = GetWaterQuadAtCoords(currentPedPosition.x, currentPedPosition.y)
```

---
### GetWaterQuadAtCoords_3d

`GET_WATER_QUAD_AT_COORDS_3D` · hash `0xF8E03DB8` · **Cliente**

```lua
local retval = GetWaterQuadAtCoords_3d(x, y, z)
```
```c
int GET_WATER_QUAD_AT_COORDS_3D(float x, float y, float z);
```

**Parámetros**

- `x` (`float`): The X coordinate
- `y` (`float`): The Y coordinate
- `z` (`float`): The water level inside the water quad

**Devuelve:** `int` — The water quad index at the given position. Returns -1 if there isn't any there. Also returns -1 if the given point is above the water level.

**Descripción oficial:**

This alternative implementation of [`GetWaterQuadAtCoords`](#getwaterquadatcoords) also checks the height of the water level.

**Ejemplo (lua):**

```lua
local currentPedPosition = GetEntityCoords(PlayerPedId())
local waterQuadIndex = GetWaterQuadAtCoords(currentPedPosition.x, currentPedPosition.y, currentPedPosition.z)
```

---
### GetWaterQuadBounds

`GET_WATER_QUAD_BOUNDS` · hash `0x42E9A06A` · **Cliente**

```lua
local retval, minX, minY, maxX, maxY = GetWaterQuadBounds(waterQuad)
```
```c
BOOL GET_WATER_QUAD_BOUNDS(int waterQuad, int* minX, int* minY, int* maxX, int* maxY);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `minX` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The minX coordinate
- `minY` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The minY coordinate
- `maxX` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The maxX coordinate
- `maxY` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The maxY coordinate

**Devuelve:** `BOOL` — Returns true on success. Bounds are undefined on failure

**Ejemplo (lua):**

```lua
local success, minX, minY, maxX, maxY = GetWaterQuadBounds(1)
```

---
### GetWaterQuadCount

`GET_WATER_QUAD_COUNT` · hash `0xB1884159` · **Cliente**

```lua
local retval = GetWaterQuadCount()
```
```c
int GET_WATER_QUAD_COUNT();
```

**Devuelve:** `int` — Returns the amount of water quads loaded.

**Ejemplo (lua):**

```lua
local waterQuadCount = GetWaterQuadCount()
```

---
### GetWaterQuadHasLimitedDepth

`GET_WATER_QUAD_HAS_LIMITED_DEPTH` · hash `0x22EA3BD8` · **Cliente**

```lua
local retval, hasLimitedDepth = GetWaterQuadHasLimitedDepth(waterQuad, hasLimitedDepth)
```
```c
BOOL GET_WATER_QUAD_HAS_LIMITED_DEPTH(int waterQuad, int* hasLimitedDepth);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `hasLimitedDepth` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns if the given water quad has a limited depth.

**Ejemplo (lua):**

```lua
local success, hasLimitedDepth = GetWaterQuadHasLimitedDepth(0)
```

---
### GetWaterQuadIsInvisible

`GET_WATER_QUAD_IS_INVISIBLE` · hash `0x1DEDBD77` · **Cliente**

```lua
local retval, isInvisible = GetWaterQuadIsInvisible(waterQuad, isInvisible)
```
```c
BOOL GET_WATER_QUAD_IS_INVISIBLE(int waterQuad, int* isInvisible);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `isInvisible` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns if the given water quad is invisible

**Ejemplo (lua):**

```lua
local success, isInvisible = GetWaterQuadIsInvisible(0)
```

---
### GetWaterQuadLevel

`GET_WATER_QUAD_LEVEL` · hash `0x6523816B` · **Cliente**

```lua
local retval, waterQuadLevel = GetWaterQuadLevel(waterQuad, waterQuadLevel)
```
```c
BOOL GET_WATER_QUAD_LEVEL(int waterQuad, float* waterQuadLevel);
```

**Parámetros**

- `waterQuad` (`int`): The returned water quad level
- `waterQuadLevel` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns true on success. Level is undefined on failure

**Descripción oficial:**

*level is defined as "z" in water.xml*

**Ejemplo (lua):**

```lua
local success, waterQuadLevel = GetWaterQuadLevel(0)
```

---
### GetWaterQuadNoStencil

`GET_WATER_QUAD_NO_STENCIL` · hash `0x6F4ACBA` · **Cliente**

```lua
local retval, noStencil = GetWaterQuadNoStencil(waterQuad, noStencil)
```
```c
BOOL GET_WATER_QUAD_NO_STENCIL(int waterQuad, int* noStencil);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `noStencil` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns if the given water quad has no stencil.

**Ejemplo (lua):**

```lua
local success, noStencil = GetWaterQuadNoStencil(0)
```

---
### GetWaterQuadType

`GET_WATER_QUAD_TYPE` · hash `0xE2501B8B` · **Cliente**

```lua
local retval, waterType = GetWaterQuadType(waterQuad, waterType)
```
```c
BOOL GET_WATER_QUAD_TYPE(int waterQuad, int* waterType);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `waterType` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns true on success. Type is undefined on failure

**Descripción oficial:**

Valid type definitions:

*   **0** Square
*   **1** Right triangle where the 90 degree angle is at maxX, minY
*   **2** Right triangle where the 90 degree angle is at minX, minY
*   **3** Right triangle where the 90 degree angle is at minX, maxY
*   **4** Right triangle where the 90 degree angle is at maxY, maxY

**Ejemplo (lua):**

```lua
local success, type = GetWaterQuadType(0)
```

---
### GetWaveQuadAmplitude

`GET_WAVE_QUAD_AMPLITUDE` · hash `0x865139A3` · **Cliente**

```lua
local retval, waveQuadAmplitude = GetWaveQuadAmplitude(waveQuad, waveQuadAmplitude)
```
```c
BOOL GET_WAVE_QUAD_AMPLITUDE(int waveQuad, float* waveQuadAmplitude);
```

**Parámetros**

- `waveQuad` (`int`): The wave quad index
- `waveQuadAmplitude` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns true on success. Amplitude is undefined on failure

**Ejemplo (lua):**

```lua
local success, amplitude = GetWaveQuadAmplitude(1)
```

---
### GetWaveQuadAtCoords

`GET_WAVE_QUAD_AT_COORDS` · hash `0x3F5A61A7` · **Cliente**

```lua
local retval = GetWaveQuadAtCoords(x, y)
```
```c
int GET_WAVE_QUAD_AT_COORDS(float x, float y);
```

**Parámetros**

- `x` (`float`): The X coordinate
- `y` (`float`): The Y coordinate

**Devuelve:** `int` — The wave quad index at the given position. Returns -1 if there isn't any there.

**Descripción oficial:**

This native returns the index of a wave quad if the given point is inside its bounds.

**Ejemplo (lua):**

```lua
local currentPedPosition = GetEntityCoords(PlayerPedId())
local waveQuadIndex = GetWaveQuadAtCoords(currentPedPosition.x, currentPedPosition.y)
```

---
### GetWaveQuadBounds

`GET_WAVE_QUAD_BOUNDS` · hash `0xF86136DB` · **Cliente**

```lua
local retval, minX, minY, maxX, maxY = GetWaveQuadBounds(waveQuad)
```
```c
BOOL GET_WAVE_QUAD_BOUNDS(int waveQuad, int* minX, int* minY, int* maxX, int* maxY);
```

**Parámetros**

- `waveQuad` (`int`): The wave quad index
- `minX` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The minX coordinate
- `minY` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The minY coordinate
- `maxX` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The maxX coordinate
- `maxY` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The maxY coordinate

**Devuelve:** `BOOL` — Returns true on success. Bounds are undefined on failure

**Ejemplo (lua):**

```lua
local success, minX, minY, maxX, maxY = GetWaveQuadBounds(1)
```

---
### GetWaveQuadCount

`GET_WAVE_QUAD_COUNT` · hash `0x9250C76` · **Cliente**

```lua
local retval = GetWaveQuadCount()
```
```c
int GET_WAVE_QUAD_COUNT();
```

**Devuelve:** `int` — Returns the amount of wave quads loaded.

**Ejemplo (lua):**

```lua
local waveQuadCount = GetWaveQuadCount()
```

---
### GetWaveQuadDirection

`GET_WAVE_QUAD_DIRECTION` · hash `0xCCE49A1C` · **Cliente**

```lua
local retval, directionX, directionY = GetWaveQuadDirection(waveQuad)
```
```c
BOOL GET_WAVE_QUAD_DIRECTION(int waveQuad, float* directionX, float* directionY);
```

**Parámetros**

- `waveQuad` (`int`): The wave quad index
- `directionX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The wave quad X direction
- `directionY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The wave quad Y direction

**Devuelve:** `BOOL` — Returns true on success. Direction values are undefined on failure

**Ejemplo (lua):**

```lua
local success, directionX, directionY = GetWaveQuadDirection(1)
```

---
### GetWeaponAccuracySpread

`GET_WEAPON_ACCURACY_SPREAD` · hash `0x5343721` · **Cliente**

```lua
local retval = GetWeaponAccuracySpread(weaponHash)
```
```c
float GET_WEAPON_ACCURACY_SPREAD(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon name hash.

**Devuelve:** `float` — The accuracy spread of a weapon.

**Descripción oficial:**

A getter for the accuracy spread of a weapon.

---
### GetWeaponAnimationOverride

`GET_WEAPON_ANIMATION_OVERRIDE` · hash `0x63ED2E7` · **Cliente**

```lua
local retval = GetWeaponAnimationOverride(ped)
```
```c
Hash GET_WEAPON_ANIMATION_OVERRIDE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`): The target ped.

**Devuelve:** `Hash` — The weapon animation override.

**Descripción oficial:**

A getter for [SET_WEAPON_ANIMATION_OVERRIDE](../gta5/WEAPON.md#setweaponanimationoverride).

**Ejemplo (lua):**

```lua
local weaponAnimation = GetWeaponAnimationOverride(PlayerPedId())
```

---
### GetWeaponComponentAccuracyModifier

`GET_WEAPON_COMPONENT_ACCURACY_MODIFIER` · hash `0xC693E278` · **Cliente**

```lua
local retval = GetWeaponComponentAccuracyModifier(componentHash)
```
```c
float GET_WEAPON_COMPONENT_ACCURACY_MODIFIER(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon component name hash.

**Devuelve:** `float` — A weapon component accuracy modifier.

**Descripción oficial:**

A getter for `CWeaponAccuracyModifier` in a weapon component.

---
### GetWeaponComponentCameraHash

`GET_WEAPON_COMPONENT_CAMERA_HASH` · hash `0xACB7E68F` · **Cliente**

```lua
local retval = GetWeaponComponentCameraHash(componentHash)
```
```c
int GET_WEAPON_COMPONENT_CAMERA_HASH(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon component name hash.

**Devuelve:** `int` — The hash of the scope camera.

**Descripción oficial:**

A getter for `CameraHash` in a weapon scope component.

---
### GetWeaponComponentClipSize

`GET_WEAPON_COMPONENT_CLIP_SIZE` · hash `0xE14CF665` · **Cliente**

```lua
local retval = GetWeaponComponentClipSize(componentHash)
```
```c
int GET_WEAPON_COMPONENT_CLIP_SIZE(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon component name hash.

**Devuelve:** `int` — A weapon component clip size.

**Descripción oficial:**

A getter for `ClipSize` in a weapon component.

---
### GetWeaponComponentDamageModifier

`GET_WEAPON_COMPONENT_DAMAGE_MODIFIER` · hash `0x4A0E3855` · **Cliente**

```lua
local retval = GetWeaponComponentDamageModifier(componentHash)
```
```c
float GET_WEAPON_COMPONENT_DAMAGE_MODIFIER(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon component name hash.

**Devuelve:** `float` — A weapon component damage modifier.

**Descripción oficial:**

A getter for `CWeaponDamageModifier` in a weapon component.

---
### GetWeaponComponentRangeDamageModifier

`GET_WEAPON_COMPONENT_RANGE_DAMAGE_MODIFIER` · hash `0xE134FB8D` · **Cliente**

```lua
local retval = GetWeaponComponentRangeDamageModifier(componentHash)
```
```c
float GET_WEAPON_COMPONENT_RANGE_DAMAGE_MODIFIER(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon component name hash.

**Devuelve:** `float` — A weapon component damage modifier.

**Descripción oficial:**

A getter for `CWeaponFallOffModifier` damage modifier value in a weapon component.

---
### GetWeaponComponentRangeModifier

`GET_WEAPON_COMPONENT_RANGE_MODIFIER` · hash `0x2FD0BC1B` · **Cliente**

```lua
local retval = GetWeaponComponentRangeModifier(componentHash)
```
```c
float GET_WEAPON_COMPONENT_RANGE_MODIFIER(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon component name hash.

**Devuelve:** `float` — A weapon component range modifier.

**Descripción oficial:**

A getter for `CWeaponFallOffModifier` range modifier value in a weapon component.

---
### GetWeaponComponentReticuleHash

`GET_WEAPON_COMPONENT_RETICULE_HASH` · hash `0xF9AB9297` · **Cliente**

```lua
local retval = GetWeaponComponentReticuleHash(componentHash)
```
```c
int GET_WEAPON_COMPONENT_RETICULE_HASH(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon component name hash.

**Devuelve:** `int` — The hash of the reticule camera.

**Descripción oficial:**

A getter for `ReticuleHash` in a weapon scope component.

---
### GetWeaponDamageModifier

`GET_WEAPON_DAMAGE_MODIFIER` · hash `0xD979143` · **Cliente**

```lua
local retval = GetWeaponDamageModifier(weaponHash)
```
```c
float GET_WEAPON_DAMAGE_MODIFIER(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon name hash.

**Devuelve:** `float` — A weapon damage modifier.

**Descripción oficial:**

A getter for [\_SET_WEAPON_DAMAGE_MODIFIER](../gta5/WEAPON.md#setweapondamagemodifier).

---
### GetWeaponRecoilShakeAmplitude

`GET_WEAPON_RECOIL_SHAKE_AMPLITUDE` · hash `0x5E1AF5F` · **Cliente**

```lua
local retval = GetWeaponRecoilShakeAmplitude(weaponHash)
```
```c
float GET_WEAPON_RECOIL_SHAKE_AMPLITUDE(Hash weaponHash);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon name hash.

**Devuelve:** `float` — The recoil shake amplitude of a weapon.

**Descripción oficial:**

A getter for the recoil shake amplitude of a weapon.

---
### GetWorldCoordFromScreenCoord

`GET_WORLD_COORD_FROM_SCREEN_COORD` · hash `0xC81D0659` · **Cliente**

```lua
local worldVector, normalVector = GetWorldCoordFromScreenCoord(screenX, screenY)
```
```c
void GET_WORLD_COORD_FROM_SCREEN_COORD(float screenX, float screenY, Vector3* worldVector, Vector3* normalVector);
```

**Parámetros**

- `screenX` (`float`): A screen horizontal axis coordinate (0.0 - 1.0).
- `screenY` (`float`): A screen vertical axis coordinate (0.0 - 1.0).
- `worldVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The world coord vector pointer.
- `normalVector` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The screen normal vector pointer.

**Devuelve:** `void` — A Vector3 representing the world coordinates relative to the specified screen coordinates and a screen plane normal Vector3 (normalised).

**Descripción oficial:**

Converts a screen coordinate into its relative world coordinate.

**Ejemplo (lua):**

```lua
CreateThread(function()
  while true do
    local screenX = GetDisabledControlNormal(0, 239)
    local screenY = GetDisabledControlNormal(0, 240)

    local world, normal = GetWorldCoordFromScreenCoord(screenX, screenY)

    local depth = 10

    local target = world + normal * depth

    DrawSphere(target.x, target.y, target.z, 0.5, 255, 0, 0, 0.5)

    Wait(0)
  end
end)
```

---
### HasMinimapOverlayLoaded

`HAS_MINIMAP_OVERLAY_LOADED` · hash `0xF7535F32` · **Cliente**

```lua
local retval = HasMinimapOverlayLoaded(id)
```
```c
BOOL HAS_MINIMAP_OVERLAY_LOADED(int id);
```

**Parámetros**

- `id` (`int`): A minimap overlay ID.

**Devuelve:** `BOOL` — A boolean indicating load status.

**Descripción oficial:**

Returns whether or not the specific minimap overlay has loaded.

---
### IsBigmapActive

`IS_BIGMAP_ACTIVE` · hash `0xFFF65C63` · **Cliente**

```lua
local retval = IsBigmapActive()
```
```c
BOOL IS_BIGMAP_ACTIVE();
```

**Devuelve:** `BOOL` — A bool indicating if the minimap is currently expanded or normal state.

**Descripción oficial:**

Returns true if the minimap is currently expanded. False if it's the normal minimap state.
Use [`IsBigmapFull`](#isbigmapfull) to check if the full map is currently revealed on the minimap.

**Ejemplo (lua):**

```lua
local expanded = IsBigmapActive()
local fullMap = IsBigmapFull()
print("The minimap is currently " .. (expanded and "expanded" or "normal size") .. " and the full map is currently " .. (fullMap and "revealed" or "not revealed") .. ".")
```

**Ejemplo (cs):**

```cs
bool expanded = IsBigmapActive();
bool fullMap = IsBigmapFull();

Debug.WriteLine($"The minimap is currently {(expanded ? "expanded" : "normal size")} and the full map is currently {(fullMap ? "revealed" : "not revealed")}.");
```

---
### IsBigmapFull

`IS_BIGMAP_FULL` · hash `0x66EE14B2` · **Cliente**

```lua
local retval = IsBigmapFull()
```
```c
BOOL IS_BIGMAP_FULL();
```

**Devuelve:** `BOOL` — Returns true if the full map is currently revealed on the minimap.
 Use [`IsBigmapActive`](#isbigmapactive) to check if the minimap is currently expanded or in it's normal state.

**Ejemplo (lua):**

```lua
local expanded = IsBigmapActive()
local fullMap = IsBigmapFull()
print("The minimap is currently " .. (expanded and "expanded" or "normal size") .. " and the full map is currently " .. (fullMap and "revealed" or "not revealed") .. ".")
```

**Ejemplo (cs):**

```cs
bool expanded = IsBigmapActive();
bool fullMap = IsBigmapFull();

Debug.WriteLine($"The minimap is currently {(expanded ? "expanded" : "normal size")} and the full map is currently {(fullMap ? "revealed" : "not revealed")}.");
```

---
### IsDisabledRawKeyDown

`IS_DISABLED_RAW_KEY_DOWN` · hash `0x36366EC3` · **Cliente**

```lua
local retval = IsDisabledRawKeyDown(rawKeyIndex)
```
```c
BOOL IS_DISABLED_RAW_KEY_DOWN(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of down state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` is pressed down, even if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe).

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsDisabledRawKeyDown(32) then -- KEY_SPACE
    print("Spacebar is down")
end
```

---
### IsDisabledRawKeyPressed

`IS_DISABLED_RAW_KEY_PRESSED` · hash `0x1F7CBBAA` · **Cliente**

```lua
local retval = IsDisabledRawKeyPressed(rawKeyIndex)
```
```c
BOOL IS_DISABLED_RAW_KEY_PRESSED(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of pressed state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` is pressed, even if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe).

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsDisabledRawKeyPressed(32) then -- KEY_SPACE
    print("Spacebar pressed")
end
```

---
### IsDisabledRawKeyReleased

`IS_DISABLED_RAW_KEY_RELEASED` · hash `0x72B66C09` · **Cliente**

```lua
local retval = IsDisabledRawKeyReleased(rawKeyIndex)
```
```c
BOOL IS_DISABLED_RAW_KEY_RELEASED(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of released state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` was released, even if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe).

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsDisabledRawKeyReleased(32) then -- KEY_SPACE
    print("Spacebar released")
end
```

---
### IsDisabledRawKeyUp

`IS_DISABLED_RAW_KEY_UP` · hash `0x2C033875` · **Cliente**

```lua
local retval = IsDisabledRawKeyUp(rawKeyIndex)
```
```c
BOOL IS_DISABLED_RAW_KEY_UP(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of up state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` is up, even if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe).

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsDisabledRawKeyUp(32) then -- KEY_SPACE
    print("Spacebar is up")
end
```

---
### IsDuiAvailable

`IS_DUI_AVAILABLE` · hash `0x7AAC3B4C` · **Cliente**

```lua
local retval = IsDuiAvailable(duiObject)
```
```c
BOOL IS_DUI_AVAILABLE(long duiObject);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.

**Devuelve:** `BOOL` — A boolean indicating TRUE if the browser is created.

**Descripción oficial:**

Returns whether or not a browser is created for a specified DUI browser object.

---
### IsGameEnhancedVersion

`IS_GAME_ENHANCED_VERSION` · hash `0x4DD998F6` · **Cliente**

```lua
local retval = IsGameEnhancedVersion()
```
```c
BOOL IS_GAME_ENHANCED_VERSION();
```

**Devuelve:** `BOOL` — Returns whether this script is running in GTAV Enhanced or not.

---
### IsNuiFocusKeepingInput

`IS_NUI_FOCUS_KEEPING_INPUT` · hash `0x39C9DC92` · **Cliente**

```lua
local retval = IsNuiFocusKeepingInput()
```
```c
BOOL IS_NUI_FOCUS_KEEPING_INPUT();
```

**Devuelve:** `BOOL` — True or false.

**Descripción oficial:**

Checks if keyboard input is enabled during NUI focus using `SET_NUI_FOCUS_KEEP_INPUT`.

---
### IsNuiFocused

`IS_NUI_FOCUSED` · hash `0x98545E6D` · **Cliente**

```lua
local retval = IsNuiFocused()
```
```c
BOOL IS_NUI_FOCUSED();
```

**Devuelve:** `BOOL` — True or false.

**Descripción oficial:**

Returns the current NUI focus state previously set with `SET_NUI_FOCUS`.

---
### IsPedCollectionComponentVariationGen9Exclusive

`IS_PED_COLLECTION_COMPONENT_VARIATION_GEN9_EXCLUSIVE` · hash `0x33B2AFA2` · **Cliente**

```lua
local retval = IsPedCollectionComponentVariationGen9Exclusive(ped, componentId, collection, drawableId)
```
```c
bool IS_PED_COLLECTION_COMPONENT_VARIATION_GEN9_EXCLUSIVE(Ped ped, int componentId, char* collection, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `drawableId` (`int`): Local drawable Id inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations).

**Devuelve:** `bool` — Whether or not the ped component variation is a gen9 exclusive (stub assets).

**Descripción oficial:**

An alternative to [IS_PED_COMPONENT_VARIATION_GEN9\_EXCLUSIVE](#ispedcomponentvariationgen9exclusive) that uses local collection indexing instead of the global one.

The local / collection relative indexing is useful because the global index may get shifted after Title Update. While local index will remain the same which simplifies migration to the newer game version.

Collection name and local index inside the collection can be obtained from the global index using [GET_PED_COLLECTION_NAME_FROM_DRAWABLE](#getpedcollectionnamefromdrawable) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE](#getpedcollectionlocalindexfromdrawable) natives.

---
### IsPedCollectionComponentVariationValid

`IS_PED_COLLECTION_COMPONENT_VARIATION_VALID` · hash `0xCA63A52A` · **Cliente**

```lua
local retval = IsPedCollectionComponentVariationValid(ped, componentId, collection, drawableId, textureId)
```
```c
bool IS_PED_COLLECTION_COMPONENT_VARIATION_VALID(Ped ped, int componentId, char* collection, int drawableId, int textureId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `drawableId` (`int`): Local drawable Id inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_COLLECTION_TEXTURE_VARIATIONS](#getnumberofpedcollectiontexturevariations).

**Devuelve:** `bool` — Returns true if the component variation is valid. This may be useful for randomizing components using loops.

**Descripción oficial:**

An alternative to [IS_PED_COMPONENT_VARIATION_VALID](../gta5/PED-1.md#ispedcomponentvariationvalid) that uses local collection indexing instead of the global one.

The local / collection relative indexing is useful because the global index may get shifted after Title Update. While local index will remain the same which simplifies migration to the newer game version.

Collection name and local index inside the collection can be obtained from the global index using [GET_PED_COLLECTION_NAME_FROM_DRAWABLE](#getpedcollectionnamefromdrawable) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE](#getpedcollectionlocalindexfromdrawable) natives.

---
### IsPedComponentVariationGen9Exclusive

`IS_PED_COMPONENT_VARIATION_GEN9_EXCLUSIVE` · hash `0xC767B581` · **Cliente**

```lua
local retval = IsPedComponentVariationGen9Exclusive(ped, componentId, drawableId)
```
```c
bool IS_PED_COMPONENT_VARIATION_GEN9_EXCLUSIVE(Ped ped, int componentId, int drawableId);
```

**Parámetros**

- `ped` (`Ped`): The target ped.
- `componentId` (`int`): The component id.
- `drawableId` (`int`): The drawable id.

**Devuelve:** `bool` — Whether or not the ped component variation is a gen9 exclusive (stub assets).

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()

for component = 0, 12 do
  local count = GetNumberOfPedDrawableVariations(ped, component)

  for drawable = 0, count - 1 do
    if IsPedComponentVariationGen9Exclusive(ped, component, drawable) then
      print("Component " .. component .. " drawable " .. drawable .. " is a gen9 exclusive, skip!")
    end
  end
end
```

---
### IsRawKeyDown

`IS_RAW_KEY_DOWN` · hash `0xD95A7387` · **Cliente**

```lua
local retval = IsRawKeyDown(rawKeyIndex)
```
```c
BOOL IS_RAW_KEY_DOWN(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of down state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` is pressed down on the keyboard.

This will not be triggered if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe)

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsRawKeyDown(32) then -- KEY_SPACE
    print("Spacebar is down")
end
```

---
### IsRawKeyPressed

`IS_RAW_KEY_PRESSED` · hash `0x69F7C29E` · **Cliente**

```lua
local retval = IsRawKeyPressed(rawKeyIndex)
```
```c
BOOL IS_RAW_KEY_PRESSED(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of pressed state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` is pressed on the keyboard.

This will not be triggered if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe)

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsRawKeyPressed(32) then -- KEY_SPACE
    print("Spacebar pressed")
end
```

---
### IsRawKeyReleased

`IS_RAW_KEY_RELEASED` · hash `0xEAA50861` · **Cliente**

```lua
local retval = IsRawKeyReleased(rawKeyIndex)
```
```c
BOOL IS_RAW_KEY_RELEASED(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of released state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` was just released on the keyboard.

This will not be triggered if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe)

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsRawKeyReleased(32) then -- KEY_SPACE
    print("Spacebar released")
end
```

---
### IsRawKeyUp

`IS_RAW_KEY_UP` · hash `0x36F4E505` · **Cliente**

```lua
local retval = IsRawKeyUp(rawKeyIndex)
```
```c
BOOL IS_RAW_KEY_UP(int rawKeyIndex);
```

**Parámetros**

- `rawKeyIndex` (`int`): Index of raw key from keyboard.

**Devuelve:** `BOOL` — Returns bool value of up state.

**Descripción oficial:**

Gets if the specified `rawKeyIndex` is up  on the keyboard.

This will not be triggered if the key is disabled with [DISABLE_RAW_KEY_THIS_FRAME](#disablerawkeythisframe)

Virtual key codes can be found [here](https://learn.microsoft.com/en-us/windows/win32/inputdev/virtual-key-codes)

**Ejemplo (lua):**

```lua
if IsRawKeyUp(32) then -- KEY_SPACE
    print("Spacebar is up")
end
```

---
### IsStreamingFileReady

`IS_STREAMING_FILE_READY` · hash `0xA194934D` · **Cliente**

```lua
local retval = IsStreamingFileReady(registerAs)
```
```c
BOOL IS_STREAMING_FILE_READY(char* registerAs);
```

**Parámetros**

- `registerAs` (`char*`): The file name to check, for example `asset.ydr`.

**Devuelve:** `BOOL` — Whether or not the streaming file has been registered.

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Returns whether an asynchronous streaming file registration completed.

---
### IsTrackEnabled

`IS_TRACK_ENABLED` · hash `0x31E695CB` · **Cliente**

```lua
local retval = IsTrackEnabled(track)
```
```c
bool IS_TRACK_ENABLED(int track);
```

**Parámetros**

- `track` (`int`): The track id (between 0 - 27)

**Devuelve:** `bool` — If this track is enabled.

**Descripción oficial:**

Getter for [SET_TRACK_ENABLED](#settrackenabled)

---
### IsTrackSwitchedOff

`IS_TRACK_SWITCHED_OFF` · hash `0xE0C53765` · **Cliente**

```lua
local retval = IsTrackSwitchedOff(track)
```
```c
bool IS_TRACK_SWITCHED_OFF(int track);
```

**Parámetros**

- `track` (`int`): The track id (between 0 - 27)

**Devuelve:** `bool` — If this track allows ambient trains to spawn

**Descripción oficial:**

Getter for [SWITCH_TRAIN_TRACK](../gta5/VEHICLE-2.md#switchtraintrack). Determines if ambient trains are able to spawn on this track.

---
### IsVehicleAlarmSet

`IS_VEHICLE_ALARM_SET` · hash `0xDC921211` · **Cliente**

```lua
local retval = IsVehicleAlarmSet(vehicle)
```
```c
BOOL IS_VEHICLE_ALARM_SET(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleInteriorLightOn

`IS_VEHICLE_INTERIOR_LIGHT_ON` · hash `0xA411F72C` · **Cliente**

```lua
local retval = IsVehicleInteriorLightOn(vehicle)
```
```c
BOOL IS_VEHICLE_INTERIOR_LIGHT_ON(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleNeedsToBeHotwired

`IS_VEHICLE_NEEDS_TO_BE_HOTWIRED` · hash `0xF9933BF4` · **Cliente**

```lua
local retval = IsVehicleNeedsToBeHotwired(vehicle)
```
```c
BOOL IS_VEHICLE_NEEDS_TO_BE_HOTWIRED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehiclePreviouslyOwnedByPlayer

`IS_VEHICLE_PREVIOUSLY_OWNED_BY_PLAYER` · hash `0xF849ED67` · **Cliente**

```lua
local retval = IsVehiclePreviouslyOwnedByPlayer(vehicle)
```
```c
BOOL IS_VEHICLE_PREVIOUSLY_OWNED_BY_PLAYER(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleWanted

`IS_VEHICLE_WANTED` · hash `0xA7DAF7C` · **Cliente**

```lua
local retval = IsVehicleWanted(vehicle)
```
```c
BOOL IS_VEHICLE_WANTED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### IsVehicleWheelBrokenOff

`IS_VEHICLE_WHEEL_BROKEN_OFF` · hash `0xCF1BC668` · **Cliente**

```lua
local retval = IsVehicleWheelBrokenOff(vehicle, wheelIndex)
```
```c
BOOL IS_VEHICLE_WHEEL_BROKEN_OFF(Vehicle vehicle, int wheelIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `wheelIndex` (`int`): The wheel index.

**Devuelve:** `BOOL`

**Descripción oficial:**

Getter for [BREAK_OFF_VEHICLE_WHEEL](#breakoffvehiclewheel).

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId())

if DoesEntityExist(vehicle) then
  local isWheelBroken = IsVehicleWheelBrokenOff(vehicle, 1)
  print("Is wheel 1 broken? ", isWheelBroken)
end
```

---
### LeaveCursorMode

`LEAVE_CURSOR_MODE` · hash `0xADECF19E` · **Cliente**

```lua
LeaveCursorMode()
```
```c
void LEAVE_CURSOR_MODE();
```

**Devuelve:** `void`

**Descripción oficial:**

Leaves cursor mode. This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### LoadWaterFromPath

`LOAD_WATER_FROM_PATH` · hash `0xF5102568` · **Cliente**

```lua
local retval = LoadWaterFromPath(resourceName, fileName)
```
```c
BOOL LOAD_WATER_FROM_PATH(char* resourceName, char* fileName);
```

**Parámetros**

- `resourceName` (`char*`): The name of the resource containing your modified water definition
- `fileName` (`char*`): The name of the file

**Devuelve:** `BOOL` — Returns true on success.

**Descripción oficial:**

Define the xml in a resources fxmanifest, under the file(s) section.

**Ejemplo (lua):**

```lua
local success = LoadWaterFromPath('my-resource-name', 'water-all-over-the-place.xml')
```

---
### MumbleAddVoiceChannelListen

`MUMBLE_ADD_VOICE_CHANNEL_LISTEN` · hash `0xC79F44BF` · **Cliente**

```lua
MumbleAddVoiceChannelListen(channel)
```
```c
void MUMBLE_ADD_VOICE_CHANNEL_LISTEN(int channel);
```

**Parámetros**

- `channel` (`int`): A game voice channel ID.

**Devuelve:** `void`

**Descripción oficial:**

Starts listening to the specified channel, when available.

---
### MumbleAddVoiceTargetChannel

`MUMBLE_ADD_VOICE_TARGET_CHANNEL` · hash `0x4D386C9E` · **Cliente**

```lua
MumbleAddVoiceTargetChannel(targetId, channel)
```
```c
void MUMBLE_ADD_VOICE_TARGET_CHANNEL(int targetId, int channel);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).
- `channel` (`int`): A game voice channel ID.

**Devuelve:** `void`

**Descripción oficial:**

Adds the specified channel to the target list for the specified Mumble voice target ID.

---
### MumbleAddVoiceTargetPlayer

`MUMBLE_ADD_VOICE_TARGET_PLAYER` · hash `0x32C5355A` · **Cliente**

```lua
MumbleAddVoiceTargetPlayer(targetId, player)
```
```c
void MUMBLE_ADD_VOICE_TARGET_PLAYER(int targetId, Player player);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).
- `player` (`Player`): A game player index.

**Devuelve:** `void`

**Descripción oficial:**

Adds the specified player to the target list for the specified Mumble voice target ID.

---
### MumbleAddVoiceTargetPlayerByServerId

`MUMBLE_ADD_VOICE_TARGET_PLAYER_BY_SERVER_ID` · hash `0x25F2B65F` · **Cliente**

```lua
MumbleAddVoiceTargetPlayerByServerId(targetId, serverId)
```
```c
void MUMBLE_ADD_VOICE_TARGET_PLAYER_BY_SERVER_ID(int targetId, int serverId);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).
- `serverId` (`int`): The player's server id.

**Devuelve:** `void`

**Descripción oficial:**

Adds the specified player to the target list for the specified Mumble voice target ID.

---
### MumbleClearVoiceChannel

`MUMBLE_CLEAR_VOICE_CHANNEL` · hash `0xBF847807` · **Cliente**

```lua
MumbleClearVoiceChannel()
```
```c
void MUMBLE_CLEAR_VOICE_CHANNEL();
```

**Devuelve:** `void`

---
### MumbleClearVoiceTarget

`MUMBLE_CLEAR_VOICE_TARGET` · hash `0x8555DCBA` · **Cliente**

```lua
MumbleClearVoiceTarget(targetId)
```
```c
void MUMBLE_CLEAR_VOICE_TARGET(int targetId);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).

**Devuelve:** `void`

**Descripción oficial:**

Clears the target list for the specified Mumble voice target ID.

---
### MumbleClearVoiceTargetChannels

`MUMBLE_CLEAR_VOICE_TARGET_CHANNELS` · hash `0x5EA72E76` · **Cliente**

```lua
MumbleClearVoiceTargetChannels(targetId)
```
```c
void MUMBLE_CLEAR_VOICE_TARGET_CHANNELS(int targetId);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).

**Devuelve:** `void`

**Descripción oficial:**

Clears channels from the target list for the specified Mumble voice target ID.

---
### MumbleClearVoiceTargetPlayers

`MUMBLE_CLEAR_VOICE_TARGET_PLAYERS` · hash `0x912E21DA` · **Cliente**

```lua
MumbleClearVoiceTargetPlayers(targetId)
```
```c
void MUMBLE_CLEAR_VOICE_TARGET_PLAYERS(int targetId);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).

**Devuelve:** `void`

**Descripción oficial:**

Clears players from the target list for the specified Mumble voice target ID.

---
### MumbleDoesChannelExist

`MUMBLE_DOES_CHANNEL_EXIST` · hash `0xCC8CA25` · **Cliente**

```lua
local retval = MumbleDoesChannelExist(channel)
```
```c
BOOL MUMBLE_DOES_CHANNEL_EXIST(int channel);
```

**Parámetros**

- `channel` (`int`): A game voice channel ID.

**Devuelve:** `BOOL` — True if the specific channel exists. False otherwise.

**Descripción oficial:**

Check whether specified channel exists on the Mumble server.

---
### MumbleGetTalkerProximity

`MUMBLE_GET_TALKER_PROXIMITY` · hash `0x84E02A32` · **Cliente**

```lua
local retval = MumbleGetTalkerProximity()
```
```c
float MUMBLE_GET_TALKER_PROXIMITY();
```

**Devuelve:** `float` — Talker proximity value.

---
### MumbleGetVoiceChannelFromServerId

`MUMBLE_GET_VOICE_CHANNEL_FROM_SERVER_ID` · hash `0x221C09F1` · **Cliente**

```lua
local retval = MumbleGetVoiceChannelFromServerId(serverId)
```
```c
int MUMBLE_GET_VOICE_CHANNEL_FROM_SERVER_ID(int serverId);
```

**Parámetros**

- `serverId` (`int`): The player's server id.

**Devuelve:** `int` — Int representing the identifier of the voice channel.

**Descripción oficial:**

Returns the mumble voice channel from a player's server id.

---
### MumbleIsActive

`MUMBLE_IS_ACTIVE` · hash `0xE820BC10` · **Cliente**

```lua
local retval = MumbleIsActive()
```
```c
BOOL MUMBLE_IS_ACTIVE();
```

**Devuelve:** `BOOL` — True if the player has enabled voice chat.

---
### MumbleIsConnected

`MUMBLE_IS_CONNECTED` · hash `0xB816370A` · **Cliente**

```lua
local retval = MumbleIsConnected()
```
```c
BOOL MUMBLE_IS_CONNECTED();
```

**Devuelve:** `BOOL` — True if the player is connected to a mumble server.

**Descripción oficial:**

This native will return true if the user succesfully connected to the voice server.
If the user disabled the voice-chat setting it will return false.

---
### MumbleIsPlayerTalking

`MUMBLE_IS_PLAYER_TALKING` · hash `0x33EEF97F` · **Cliente**

```lua
local retval = MumbleIsPlayerTalking(player)
```
```c
BOOL MUMBLE_IS_PLAYER_TALKING(Player player);
```

**Parámetros**

- `player` (`Player`): The target player.

**Devuelve:** `BOOL` — Whether or not the player is talking.

---
### MumbleRemoveVoiceChannelListen

`MUMBLE_REMOVE_VOICE_CHANNEL_LISTEN` · hash `0x231523B7` · **Cliente**

```lua
MumbleRemoveVoiceChannelListen(channel)
```
```c
void MUMBLE_REMOVE_VOICE_CHANNEL_LISTEN(int channel);
```

**Parámetros**

- `channel` (`int`): A game voice channel ID.

**Devuelve:** `void`

**Descripción oficial:**

Stops listening to the specified channel.

---
### MumbleRemoveVoiceTargetChannel

`MUMBLE_REMOVE_VOICE_TARGET_CHANNEL` · hash `0x268DB867` · **Cliente**

```lua
MumbleRemoveVoiceTargetChannel(targetId, channel)
```
```c
void MUMBLE_REMOVE_VOICE_TARGET_CHANNEL(int targetId, int channel);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).
- `channel` (`int`): The game voice channel ID to remove from the target.

**Devuelve:** `void`

**Descripción oficial:**

Removes the specified voice channel from the user's voice targets.

Performs the opposite operation of [MUMBLE_ADD_VOICE_TARGET_CHANNEL](#mumbleaddvoicetargetchannel)

---
### MumbleRemoveVoiceTargetPlayer

`MUMBLE_REMOVE_VOICE_TARGET_PLAYER` · hash `0x88CD646F` · **Cliente**

```lua
MumbleRemoveVoiceTargetPlayer(targetId, player)
```
```c
void MUMBLE_REMOVE_VOICE_TARGET_PLAYER(int targetId, Player player);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).
- `player` (`Player`): The player index to remove from the target.

**Devuelve:** `void`

**Descripción oficial:**

Removes the specified player from the user's voice targets.

Performs the opposite operation of [MUMBLE_ADD_VOICE_TARGET_PLAYER](#mumbleaddvoicetargetplayer)

---
### MumbleRemoveVoiceTargetPlayerByServerId

`MUMBLE_REMOVE_VOICE_TARGET_PLAYER_BY_SERVER_ID` · hash `0x930BD34B` · **Cliente**

```lua
MumbleRemoveVoiceTargetPlayerByServerId(targetId, serverId)
```
```c
void MUMBLE_REMOVE_VOICE_TARGET_PLAYER_BY_SERVER_ID(int targetId, int serverId);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive).
- `serverId` (`int`): The player's server id to remove from the target.

**Devuelve:** `void`

**Descripción oficial:**

Removes the specified player from the user's voice targets.

Performs the opposite operation of [MUMBLE_ADD_VOICE_TARGET_PLAYER_BY_SERVER_ID](#mumbleaddvoicetargetplayerbyserverid)

---
### MumbleSetActive

`MUMBLE_SET_ACTIVE` · hash `0xD932A3F3` · **Cliente**

```lua
MumbleSetActive(state)
```
```c
void MUMBLE_SET_ACTIVE(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): Voice chat state.

**Devuelve:** `void`

---
### MumbleSetAudioInputDistance

`MUMBLE_SET_AUDIO_INPUT_DISTANCE` · hash `0x1B1052E2` · **Cliente**

```lua
MumbleSetAudioInputDistance(distance)
```
```c
void MUMBLE_SET_AUDIO_INPUT_DISTANCE(float distance);
```

**Parámetros**

- `distance` (`float`): The input distance.

**Devuelve:** `void`

**Descripción oficial:**

Sets the current input distance. The player will be able to talk to other players within this distance.

---
### MumbleSetAudioInputIntent

`MUMBLE_SET_AUDIO_INPUT_INTENT` · hash `0x6383526B` · **Cliente**

```lua
MumbleSetAudioInputIntent(intentHash)
```
```c
void MUMBLE_SET_AUDIO_INPUT_INTENT(Hash intentHash);
```

**Parámetros**

- `intentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The intent hash.

**Devuelve:** `void`

**Descripción oficial:**

Use this native to disable noise suppression and high pass filters.

The possible intents for this are as follows (backticks are used to represent hashes):

| Index | Description |
|-|-|
| \`speech\` | Default intent |
| \`music\` | Disable noise suppression and high pass filter |

**Ejemplo (lua):**

```lua
-- disable noise suppression and high pass filter
MumbleSetAudioInputIntent(`music`)

-- set the default intent (enable noise suppression and high pass filter)
MumbleSetAudioInputIntent(`speech`)
```

---
### MumbleSetAudioOutputDistance

`MUMBLE_SET_AUDIO_OUTPUT_DISTANCE` · hash `0x74C597D9` · **Cliente**

```lua
MumbleSetAudioOutputDistance(distance)
```
```c
void MUMBLE_SET_AUDIO_OUTPUT_DISTANCE(float distance);
```

**Parámetros**

- `distance` (`float`): The output distance.

**Devuelve:** `void`

**Descripción oficial:**

Sets the current output distance. The player will be able to hear other players talking within this distance.

---
### MumbleSetServerAddress

`MUMBLE_SET_SERVER_ADDRESS` · hash `0xE6EB2CD8` · **Cliente**

```lua
MumbleSetServerAddress(address, port)
```
```c
void MUMBLE_SET_SERVER_ADDRESS(char* address, int port);
```

**Parámetros**

- `address` (`char*`): The address of the mumble server.
- `port` (`int`): The port of the mumble server.

**Devuelve:** `void`

**Descripción oficial:**

Changes the Mumble server address to connect to, and reconnects to the new address.

Setting the address to an empty string and the port to -1 will reset to the built in FXServer Mumble Implementation.

---
### MumbleSetSubmixForServerId

`MUMBLE_SET_SUBMIX_FOR_SERVER_ID` · hash `0xFE3A3054` · **Cliente**

```lua
MumbleSetSubmixForServerId(serverId, submixId)
```
```c
void MUMBLE_SET_SUBMIX_FOR_SERVER_ID(int serverId, int submixId);
```

**Parámetros**

- `serverId` (`int`): The player's server ID.
- `submixId` (`int`): The submix ID.

**Devuelve:** `void`

**Descripción oficial:**

Sets the audio submix ID for a specified player using Mumble 'Native Audio' functionality.

---
### MumbleSetTalkerProximity

`MUMBLE_SET_TALKER_PROXIMITY` · hash `0x74E927B0` · **Cliente**

```lua
MumbleSetTalkerProximity(value)
```
```c
void MUMBLE_SET_TALKER_PROXIMITY(float value);
```

**Parámetros**

- `value` (`float`): Proximity value.

**Devuelve:** `void`

---
### MumbleSetVoiceChannel

`MUMBLE_SET_VOICE_CHANNEL` · hash `0x8737EEE8` · **Cliente**

```lua
MumbleSetVoiceChannel(channel)
```
```c
void MUMBLE_SET_VOICE_CHANNEL(int channel);
```

**Parámetros**

- `channel` (`int`): A game voice channel ID.

**Devuelve:** `void`

---
### MumbleSetVoiceTarget

`MUMBLE_SET_VOICE_TARGET` · hash `0x960A4A95` · **Cliente**

```lua
MumbleSetVoiceTarget(targetId)
```
```c
void MUMBLE_SET_VOICE_TARGET(int targetId);
```

**Parámetros**

- `targetId` (`int`): A Mumble voice target ID, ranging from 1..30 (inclusive). 0 disables voice targets, and 31 is server loopback.

**Devuelve:** `void`

**Descripción oficial:**

Sets the current Mumble voice target ID to broadcast voice to.

---
### MumbleSetVolumeOverride

`MUMBLE_SET_VOLUME_OVERRIDE` · hash `0x61C309E3` · **Cliente**

```lua
MumbleSetVolumeOverride(player, volume)
```
```c
void MUMBLE_SET_VOLUME_OVERRIDE(Player player, float volume);
```

**Parámetros**

- `player` (`Player`): A game player index.
- `volume` (`float`): The volume, ranging from 0.0 to 1.0 (or above).

**Devuelve:** `void`

**Descripción oficial:**

Overrides the output volume for a particular player on Mumble. This will also bypass 3D audio and distance calculations. -1.0 to reset the override.

Set to -1.0 to reset the Volume override.

---
### MumbleSetVolumeOverrideByServerId

`MUMBLE_SET_VOLUME_OVERRIDE_BY_SERVER_ID` · hash `0xCE8E25B4` · **Cliente**

```lua
MumbleSetVolumeOverrideByServerId(serverId, volume)
```
```c
void MUMBLE_SET_VOLUME_OVERRIDE_BY_SERVER_ID(int serverId, float volume);
```

**Parámetros**

- `serverId` (`int`): The player's server id.
- `volume` (`float`): The volume, ranging from 0.0 to 1.0 (or above).

**Devuelve:** `void`

**Descripción oficial:**

Overrides the output volume for a particular player with the specified server id and player name on Mumble. This will also bypass 3D audio and distance calculations. -1.0 to reset the override.

---
### OnesyncEnableRemoteAttachmentSanitization

`ONESYNC_ENABLE_REMOTE_ATTACHMENT_SANITIZATION` · hash `0x30CE39D8` · **Cliente**

```lua
OnesyncEnableRemoteAttachmentSanitization(enable)
```
```c
void ONESYNC_ENABLE_REMOTE_ATTACHMENT_SANITIZATION(BOOL enable);
```

**Parámetros**

- `enable` (`BOOL`): Whether to enable sanitization.

**Devuelve:** `void`

**Descripción oficial:**

Toggles a check that prevents attaching (networked) entities to remotely owned peds. This is disabled by default.

---
### OverridePedsCanStandOnTopFlag

`OVERRIDE_PEDS_CAN_STAND_ON_TOP_FLAG` · hash `0x90A9E0B2` · **Cliente**

```lua
OverridePedsCanStandOnTopFlag(flag)
```
```c
void OVERRIDE_PEDS_CAN_STAND_ON_TOP_FLAG(BOOL flag);
```

**Parámetros**

- `flag` (`BOOL`): true to override, false to use default game behavior.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether peds can stand on top of *all* vehicles without falling off.

Note this flag is not replicated automatically, you will have to manually do so.

---
### OverridePedsUseDefaultDriveByClipset

`OVERRIDE_PEDS_USE_DEFAULT_DRIVE_BY_CLIPSET` · hash `0xB14F8EAD` · **Cliente**

```lua
OverridePedsUseDefaultDriveByClipset(flag)
```
```c
void OVERRIDE_PEDS_USE_DEFAULT_DRIVE_BY_CLIPSET(BOOL flag);
```

**Parámetros**

- `flag` (`BOOL`): true to override, false to use default game behavior.

**Devuelve:** `void`

**Descripción oficial:**

Allows the bypassing of default game behavior that prevents the use of [SET_PED_DRIVE_BY_CLIPSET_OVERRIDE](../gta5/PED-1.md#setpeddrivebyclipsetoverride) in certain scenarios to avoid clipping issues (e.g., when there is more than one Ped in a vehicle).

Note: This flag and the overridden clipset are not replicated values and require synchronization through user scripts. Additionally, current game behavior also restricts applying this clipset locally when in first-person mode and will require a temporary workaround.

---
### OverridePopGroups

`OVERRIDE_POP_GROUPS` · hash `0xD3BC438F` · **Cliente**

```lua
OverridePopGroups(path)
```
```c
void OVERRIDE_POP_GROUPS(char* path);
```

**Parámetros**

- `path` (`char*`): The file path to load (`popgroups`, `@resource/popgroups`), or `null` to reload the default population groups file.

**Devuelve:** `void`

**Descripción oficial:**

Replaces the `popgroups` (CPopGroupList) meta file with the file in the specified path.

**Ejemplo (lua):**

```lua
-- fxmanifest.lua:
file 'popgroups_dlc.xml'

-- client.lua:
OverridePopGroups('popgroups_dlc.xml')

-- restore the original after five minutes
Wait(1000 * 60 * 5)
OverridePopGroups(nil)
```

---
### OverrideReactionToVehicleSiren

`OVERRIDE_REACTION_TO_VEHICLE_SIREN` · hash `0x3F3EB3F7` · **Cliente**

```lua
OverrideReactionToVehicleSiren(state, reaction)
```
```c
void OVERRIDE_REACTION_TO_VEHICLE_SIREN(BOOL state, int reaction);
```

**Parámetros**

- `state` (`BOOL`): Toggle on or off
- `reaction` (`int`): Decide how they should react

**Devuelve:** `void`

**Descripción oficial:**

Setting the state to true and a value between 0 and 2 will cause pedestrian vehicles to react accordingly to sirens.

```cpp
enum Reactions {
    Left = 0,
    Right = 1,
    Stop = 2
}
```

---
### OverrideVehiclePedsCanStandOnTopFlag

`OVERRIDE_VEHICLE_PEDS_CAN_STAND_ON_TOP_FLAG` · hash `0x7FA03E76` · **Cliente**

```lua
OverrideVehiclePedsCanStandOnTopFlag(vehicle, can)
```
```c
void OVERRIDE_VEHICLE_PEDS_CAN_STAND_ON_TOP_FLAG(Vehicle vehicle, BOOL can);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle.
- `can` (`BOOL`): Can they?

**Devuelve:** `void`

**Descripción oficial:**

Overrides whether or not peds can stand on top of the specified vehicle.

Note this flag is not replicated automatically, you will have to manually do so.

---
### PrepareLight

`PREPARE_LIGHT` · hash `0x584B4C99` · **Cliente**

```lua
PrepareLight(lightType, flags, x, y, z, r, g, b, intensity)
```
```c
void PREPARE_LIGHT(int lightType, int flags, float x, float y, float z, int r, int g, int b, float intensity);
```

**Parámetros**

- `lightType` (`int`): The type of the light
- `flags` (`int`): Light flags
- `x` (`float`): X coordinate of the light position
- `y` (`float`): Y coordinate of the light position
- `z` (`float`): Z coordinate of the light position
- `r` (`int`): Red component of the light color (0-255)
- `g` (`int`): Green component of the light color (0-255)
- `b` (`int`): Blue component of the light color (0-255)
- `intensity` (`float`): Intensity of the light

**Devuelve:** `void`

**Descripción oficial:**

Create a new light with specified type, flags, position, color, and intensity.

---
### RegisterArchetypes

`REGISTER_ARCHETYPES` · hash `0x3C2F9037` · **Cliente**

```lua
RegisterArchetypes(factory)
```
```c
void REGISTER_ARCHETYPES(func factory);
```

**Parámetros**

- `factory` (`func`): A function returning a list of archetypes.

**Devuelve:** `void`

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Registers a set of archetypes with the game engine. These should match `CBaseArchetypeDef` class information from the game.

**Ejemplo (lua):**

```lua
RegisterArchetypes(function()
	return {
		{
			flags = 32,
			bbMin = vector3(-39.99570000, -8.00155600, -2.56818800),
			bbMax = vector3(40.00439000, 7.99858000, 1.44575100),
			bsCentre = vector3(0.00434110, -0.00148870, -0.56121830),
			bsRadius = 40.84160000,
			name = 'my_asset',
			textureDictionary = 'my_asset',
			physicsDictionary = 'my_asset',
			assetName = 'my_asset',
			assetType = 'ASSET_TYPE_DRAWABLE',
			lodDist = 450.45,
			specialAttribute = 0
		}
	}
end)
```

---
### RegisterFontFile

`REGISTER_FONT_FILE` · hash `0x1B3A363` · **Cliente**

```lua
RegisterFontFile(fileName)
```
```c
void REGISTER_FONT_FILE(char* fileName);
```

**Parámetros**

- `fileName` (`char*`): The name of the .gfx file, without extension.

**Devuelve:** `void`

**Descripción oficial:**

Registers a specified .gfx file as GFx font library.
The .gfx file has to be registered with the streamer already.

---
### RegisterFontId

`REGISTER_FONT_ID` · hash `0xACF6D8EE` · **Cliente**

```lua
local retval = RegisterFontId(fontName)
```
```c
int REGISTER_FONT_ID(char* fontName);
```

**Parámetros**

- `fontName` (`char*`): The name of the font in the GFx font library.

**Devuelve:** `int` — An index to use with [SET_TEXT_FONT](../gta5/HUD.md#settextfont) and similar natives.

**Descripción oficial:**

Registers a specified font name for use with text draw commands.

---
### RegisterKeyMapping

`REGISTER_KEY_MAPPING` · hash `0xD7664FD1` · **Cliente**

```lua
RegisterKeyMapping(commandString, description, defaultMapper, defaultParameter)
```
```c
void REGISTER_KEY_MAPPING(char* commandString, char* description, char* defaultMapper, char* defaultParameter);
```

**Parámetros**

- `commandString` (`char*`): The command to execute, and the identifier of the binding.
- `description` (`char*`): A description for in the settings menu.
- `defaultMapper` (`char*`): The [mapper ID](https://docs.fivem.net/docs/game-references/input-mapper-parameter-ids/) to use for the default binding, e.g. `keyboard`.
- `defaultParameter` (`char*`): The [IO parameter ID](https://docs.fivem.net/docs/game-references/input-mapper-parameter-ids/) to use for the default binding, e.g. `f3`.

**Devuelve:** `void`

**Descripción oficial:**

Registers a key mapping for the current resource.

See the related [cookbook post](https://cookbook.fivem.net/2020/01/06/using-the-new-console-key-bindings/) for more information.

Below you can find some examples on how to create these keybindings as well as the alternate keybinding syntax, which is preceded by `~!` to indicate that it's an alternate key.

**Ejemplo (lua):**

```lua
local handsUp = false
CreateThread(function()
    while true do
        Wait(0)
        if handsUp then
            TaskHandsUp(PlayerPedId(), 250, PlayerPedId(), -1, true)
        end
    end
end)
RegisterCommand('+handsup', function()
    handsUp = true
end, false)
RegisterCommand('-handsup', function()
    handsUp = false
end, false)

RegisterKeyMapping('+handsup', 'Hands Up', 'keyboard', 'i')

-- Alternate keybinding syntax
RegisterKeyMapping('~!+handsup', 'Hands Up - Alternate Key', 'keyboard', 'o')
```

---
### RegisterNuiCallback

`REGISTER_NUI_CALLBACK` · hash `0xC59B980C` · **Cliente**

```lua
RegisterNuiCallback(callbackType, callback)
```
```c
void REGISTER_NUI_CALLBACK(char* callbackType, func callback);
```

**Parámetros**

- `callbackType` (`char*`)
- `callback` (`func`)

**Devuelve:** `void`

---
### RegisterNuiCallbackType

`REGISTER_NUI_CALLBACK_TYPE` · hash `0xCD03CDA9` · **Cliente**

```lua
RegisterNuiCallbackType(callbackType)
```
```c
void REGISTER_NUI_CALLBACK_TYPE(char* callbackType);
```

**Parámetros**

- `callbackType` (`char*`)

**Devuelve:** `void`

---
### RegisterRawNuiCallback

`REGISTER_RAW_NUI_CALLBACK` · hash `0xA8AE9C2F` · **Cliente**

```lua
RegisterRawNuiCallback(callbackType, callback)
```
```c
void REGISTER_RAW_NUI_CALLBACK(char* callbackType, func callback);
```

**Parámetros**

- `callbackType` (`char*`)
- `callback` (`func`)

**Devuelve:** `void`

---
### RegisterRopeData

`REGISTER_ROPE_DATA` · hash `0xF213AE8D` · **Cliente**

```lua
local retval = RegisterRopeData(numSections, radius, diffuseTextureName, normalMapName, distanceMappingScale, uvScaleX, uvScaleY, specularFresnel, specularFalloff, specularIntensity, bumpiness, color)
```
```c
int REGISTER_ROPE_DATA(int numSections, float radius, char* diffuseTextureName, char* normalMapName, float distanceMappingScale, float uvScaleX, float uvScaleY, float specularFresnel, float specularFalloff, float specularIntensity, float bumpiness, int color);
```

**Parámetros**

- `numSections` (`int`)
- `radius` (`float`)
- `diffuseTextureName` (`char*`)
- `normalMapName` (`char*`)
- `distanceMappingScale` (`float`)
- `uvScaleX` (`float`)
- `uvScaleY` (`float`)
- `specularFresnel` (`float`)
- `specularFalloff` (`float`)
- `specularIntensity` (`float`)
- `bumpiness` (`float`)
- `color` (`int`)

**Devuelve:** `int` — Returns a non-negative value on success, or -1 if the rope data could not be registered or an invalid argument is passed.

**Descripción oficial:**

Registers a custom rope data with the game. For guidance on what these values should be use common:/data/ropedata.xml as a reference.
Returns a rope type which can be passed into [ADD_ROPE](../gta5/PHYSICS.md#addrope) to use a custom rope design.
Once a rope data is registered it can be used indefinitely and you should take caution not too register too many as to exceed the games limit.

**Ejemplo (lua):**

```lua
-- Create a thick steel cable rope above the players head
local ropeType = RegisterRopeData(6, 0.15, "steel_cable", "steel_cable_n", 1.0, 1.0, 8.775, 0.97, 30.0, 0.25, 1.775, 0x00FFFF00)
if ropeType ~= -1 then
    local coords = GetEntityCoords(PlayerPedId()) + vector3(0.0, 0.0, 5.0)
	AddRope(coords.x, coords.y, coords.z, 0.0, 0.0, 0.0, 25.0, ropeType, 10.0, 0.0, 1.0, false, false, false, 1.0, false, 0)
    RopeLoadTextures()
end
```

---
### RegisterStreamingFileFromCache

`REGISTER_STREAMING_FILE_FROM_CACHE` · hash `0xCEAD2D4B` · **Cliente**

```lua
RegisterStreamingFileFromCache(resourceName, fileName, cacheString)
```
```c
void REGISTER_STREAMING_FILE_FROM_CACHE(char* resourceName, char* fileName, char* cacheString);
```

**Parámetros**

- `resourceName` (`char*`): The resource to add the asset to.
- `fileName` (`char*`): A file name in the resource.
- `cacheString` (`char*`): The string returned from `REGISTER_RESOURCE_ASSET` on the server.

**Devuelve:** `void`

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Registers a dynamic streaming asset from the server with the GTA streaming module system.

---
### RegisterStreamingFileFromKvs

`REGISTER_STREAMING_FILE_FROM_KVS` · hash `0x1493DCC1` · **Cliente**

```lua
RegisterStreamingFileFromKvs(kvsKey)
```
```c
void REGISTER_STREAMING_FILE_FROM_KVS(char* kvsKey);
```

**Parámetros**

- `kvsKey` (`char*`): The KVP key in the current resource to register as an asset.

**Devuelve:** `void`

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Registers a KVP value as an asset with the GTA streaming module system. This function currently won't work.

---
### RegisterStreamingFileFromUrl

`REGISTER_STREAMING_FILE_FROM_URL` · hash `0xF44BFB95` · **Cliente**

```lua
RegisterStreamingFileFromUrl(registerAs, url)
```
```c
void REGISTER_STREAMING_FILE_FROM_URL(char* registerAs, char* url);
```

**Parámetros**

- `registerAs` (`char*`): The file name to register as, for example `asset.ydr`.
- `url` (`char*`): The URL to fetch the asset from.

**Devuelve:** `void`

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Registers a file from an URL as a streaming asset in the GTA streaming subsystem. This will asynchronously register the asset, and caching is done based on the URL itself - cache headers are ignored.

Use `IS_STREAMING_FILE_READY` to check if the asset has been registered successfully.

---
### RegisterTrackJunction

`REGISTER_TRACK_JUNCTION` · hash `0x35F743B5` · **Cliente**

```lua
local retval = RegisterTrackJunction(trackIndex, trackNode, newIndex, newNode, direction)
```
```c
int REGISTER_TRACK_JUNCTION(int trackIndex, int trackNode, int newIndex, int newNode, bool direction);
```

**Parámetros**

- `trackIndex` (`int`): The track index a train should be on
- `trackNode` (`int`): The node a train should be on
- `newIndex` (`int`): The new track index for a train to be placed on
- `newNode` (`int`): The new track node for a train to be placed on
- `direction` (`bool`): The direction a train should be traveling for this junction

**Devuelve:** `int` — The track junction's handle or -1 if invalid.

**Descripción oficial:**

Registers a track junction that when enabled will cause a train on the defined trackIndex, node and direction to change its current track index and begin traveling on the new node

---
### RemoveDryVolume

`REMOVE_DRY_VOLUME` · hash `0x7BCAA6E7` · **Cliente**

```lua
RemoveDryVolume(handle)
```
```c
void REMOVE_DRY_VOLUME(int handle);
```

**Parámetros**

- `handle` (`int`): The handle of the dry volume that needs to be removed.

**Devuelve:** `void`

**Descripción oficial:**

Removes a dry volume from the game session.
See CREATE_DRY_VOLUME for more info

---
### RemoveHealthConfig

`REMOVE_HEALTH_CONFIG` · hash `0xE0ED5FB` · **Cliente**

```lua
RemoveHealthConfig(configName)
```
```c
void REMOVE_HEALTH_CONFIG(char* configName);
```

**Parámetros**

- `configName` (`char*`): Removes config name. Cannot be default game health config name.

**Devuelve:** `void`

**Descripción oficial:**

Removes health config.

---
### RemoveReplaceTexture

`REMOVE_REPLACE_TEXTURE` · hash `0xA896B20A` · **Cliente**

```lua
RemoveReplaceTexture(origTxd, origTxn)
```
```c
void REMOVE_REPLACE_TEXTURE(char* origTxd, char* origTxn);
```

**Parámetros**

- `origTxd` (`char*`)
- `origTxn` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Experimental natives, please do not use in a live environment.

---
### RemoveTimecycleModifier

`REMOVE_TIMECYCLE_MODIFIER` · hash `0x36DF8612` · **Cliente**

```lua
RemoveTimecycleModifier(modifierName)
```
```c
void REMOVE_TIMECYCLE_MODIFIER(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`): The timecycle modifier name.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local modifierName = "my_awesome_timecycle"
RemoveTimecycleModifier(modifierName)
```

---
### RemoveTimecycleModifierVar

`REMOVE_TIMECYCLE_MODIFIER_VAR` · hash `0x5A5E0D05` · **Cliente**

```lua
RemoveTimecycleModifierVar(modifierName, varName)
```
```c
void REMOVE_TIMECYCLE_MODIFIER_VAR(char* modifierName, char* varName);
```

**Parámetros**

- `modifierName` (`char*`): The name of timecycle modifier.
- `varName` (`char*`): The name of timecycle variable.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local modifierName = "superDARK"
local varName = "postfx_noise"

if DoesTimecycleModifierHasVar(modifierName, varName) then
  local success, value1, value2 = GetTimecycleModifierVar(modifierName, varName)

  if success then
    print(string.format("[%s] removed var %s with values: %f %f", modifierName, varName, value1, value2))
    RemoveTimecycleModifierVar(modifierName, varName)
  end
else
    SetTimecycleModifierVar(modifierName, varName, 1.0, 1.0)
    print(string.format("[%s] created var %s", modifierName, varName))
end
```

---
### RemoveTrackJunction

`REMOVE_TRACK_JUNCTION` · hash `0x4F3D2B2A` · **Cliente**

```lua
local retval = RemoveTrackJunction(junctionIndex)
```
```c
bool REMOVE_TRACK_JUNCTION(int junctionIndex);
```

**Parámetros**

- `junctionIndex` (`int`): The junctions index

**Devuelve:** `bool` — Returns if it succeeds in removing a junction or not

**Descripción oficial:**

Removes the specified track junction.

---
### RequestResourceFileSet

`REQUEST_RESOURCE_FILE_SET` · hash `0xE7490533` · **Cliente**

```lua
local retval = RequestResourceFileSet(setName)
```
```c
BOOL REQUEST_RESOURCE_FILE_SET(char* setName);
```

**Parámetros**

- `setName` (`char*`): The name of the file set as specified in `fxmanifest.lua`.

**Devuelve:** `BOOL` — `TRUE` if the set is mounted, `FALSE` if the request is still pending.

**Descripción oficial:**

Requests a resource file set with the specified name to be downloaded and mounted on top of the current resource.

Resource file sets are specified in `fxmanifest.lua` with the following syntax:

```lua
file_set 'addon_ui' {
    'ui/addon/index.html',
    'ui/addon/**.js',
}
```

This command will trigger a script error if the request failed.

**Ejemplo (lua):**

```lua
-- fxmanifest.lua
file_set 'dummies' {
    'dummy/**.txt',
    'potato.txt',
}

-- main script
local function PrintTest()
    local tests = { 'potato.txt', 'dummy/1.txt', 'dummy/b/2.txt' }

    for _, v in ipairs(tests) do
        local data = LoadResourceFile(GetCurrentResourceName(), v)
        print(v, data)
    end
end

RegisterCommand('fileset', function()
    PrintTest()

    while not RequestResourceFileSet('dummies') do
        Wait(100)
    end

    PrintTest()
end)
```

---
### ResetEntityDrawOutlineRenderTechnique

`RESET_ENTITY_DRAW_OUTLINE_RENDER_TECHNIQUE` · hash `0x8EB6EC38` · **Cliente**

```lua
ResetEntityDrawOutlineRenderTechnique()
```
```c
void RESET_ENTITY_DRAW_OUTLINE_RENDER_TECHNIQUE();
```

**Devuelve:** `void`

**Descripción oficial:**

This function undoes changes made by [`SET_ENTITY_DRAW_OUTLINE_RENDER_TECHNIQUE`](#setentitydrawoutlinerendertechnique), restoring the original outline rendering behavior. The default render technique group is `unlit`.

---
### ResetFlyThroughWindscreenParams

`RESET_FLY_THROUGH_WINDSCREEN_PARAMS` · hash `0x6D712937` · **Cliente**

```lua
ResetFlyThroughWindscreenParams()
```
```c
void RESET_FLY_THROUGH_WINDSCREEN_PARAMS();
```

**Devuelve:** `void`

**Descripción oficial:**

Resets parameters which is used by the game for checking is ped needs to fly through windscreen after a crash to default values.

---
### ResetMapZoomDataLevel

`RESET_MAP_ZOOM_DATA_LEVEL` · hash `0x11A5B7ED` · **Cliente**

```lua
ResetMapZoomDataLevel(index)
```
```c
void RESET_MAP_ZOOM_DATA_LEVEL(int index);
```

**Parámetros**

- `index` (`int`): Zoom level index.

**Devuelve:** `void`

**Descripción oficial:**

Resets values from the zoom level data by index to defaults from mapzoomdata.meta.

---
### ResetMapdataEntityMatrix

`RESET_MAPDATA_ENTITY_MATRIX` · hash `0x8143FA4F` · **Cliente**

```lua
local retval = ResetMapdataEntityMatrix(mapDataHash, entityInternalIdx)
```
```c
BOOL RESET_MAPDATA_ENTITY_MATRIX(int mapDataHash, int entityInternalIdx);
```

**Parámetros**

- `mapDataHash` (`int`): A mapdata hash from `mapDataLoaded` event.
- `entityInternalIdx` (`int`): An internal entity's index.

**Devuelve:** `BOOL` — True if successful, false if not.

**Descripción oficial:**

Resets mapdata entity transform matrix to its original state.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### ResetPedModelPersonality

`RESET_PED_MODEL_PERSONALITY` · hash `0x79A12861` · **Cliente**

```lua
ResetPedModelPersonality(modelHash)
```
```c
void RESET_PED_MODEL_PERSONALITY(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Ped's model.

**Devuelve:** `void`

**Descripción oficial:**

Restores an overridden ped model personality type to the default value.

---
### ResetVehiclePedsCanStandOnTopFlag

`RESET_VEHICLE_PEDS_CAN_STAND_ON_TOP_FLAG` · hash `0xDF62CFE2` · **Cliente**

```lua
ResetVehiclePedsCanStandOnTopFlag(vehicle)
```
```c
void RESET_VEHICLE_PEDS_CAN_STAND_ON_TOP_FLAG(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle.

**Devuelve:** `void`

**Descripción oficial:**

Resets whether or not peds can stand on top of the specified vehicle.

Note this flag is not replicated automatically, you will have to manually do so.

---
### ResetWater

`RESET_WATER` · hash `0x1DA4791` · **Cliente**

```lua
ResetWater()
```
```c
void RESET_WATER();
```

**Devuelve:** `void`

**Descripción oficial:**

Resets the water to the games default water.xml.

**Ejemplo (lua):**

```lua
ResetWater()
```

---
### SelectEntityAtCursor

`SELECT_ENTITY_AT_CURSOR` · hash `0x3DD8130F` · **Cliente**

```lua
local retval = SelectEntityAtCursor(hitFlags, precise)
```
```c
Entity SELECT_ENTITY_AT_CURSOR(int hitFlags, BOOL precise);
```

**Parámetros**

- `hitFlags` (`int`): A bit mask of entity types to match.
- `precise` (`BOOL`): Whether to do a *precise* test, i.e. of visual coordinates, too.

**Devuelve:** `Entity` — An entity handle, or zero.

**Descripción oficial:**

Gets the selected entity at the current mouse cursor position, and changes the current selection depth. This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### SelectEntityAtPos

`SELECT_ENTITY_AT_POS` · hash `0xAFE8D405` · **Cliente**

```lua
local retval = SelectEntityAtPos(fracX, fracY, hitFlags, precise)
```
```c
Entity SELECT_ENTITY_AT_POS(float fracX, float fracY, int hitFlags, BOOL precise);
```

**Parámetros**

- `fracX` (`float`): Mouse cursor X fraction.
- `fracY` (`float`): Mouse cursor Y fraction.
- `hitFlags` (`int`): A bit mask of entity types to match.
- `precise` (`BOOL`): Whether to do a *precise* test, i.e. of visual coordinates, too.

**Devuelve:** `Entity` — An entity handle, or zero.

**Descripción oficial:**

Gets the selected entity at the specified mouse cursor position, and changes the current selection depth. This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### SendDuiMessage

`SEND_DUI_MESSAGE` · hash `0xCD380DA9` · **Cliente**

```lua
SendDuiMessage(duiObject, jsonString)
```
```c
void SEND_DUI_MESSAGE(long duiObject, char* jsonString);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.
- `jsonString` (`char*`): The message, encoded as JSON.

**Devuelve:** `void`

**Descripción oficial:**

Sends a message to the specific DUI root page. This is similar to SEND_NUI_MESSAGE.

---
### SendDuiMouseDown

`SEND_DUI_MOUSE_DOWN` · hash `0x5D01F191` · **Cliente**

```lua
SendDuiMouseDown(duiObject, button)
```
```c
void SEND_DUI_MOUSE_DOWN(long duiObject, char* button);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.
- `button` (`char*`): Either `'left'`, `'middle'` or `'right'`.

**Devuelve:** `void`

**Descripción oficial:**

Injects a 'mouse down' event for a DUI object. Coordinates are expected to be set using SEND_DUI_MOUSE_MOVE.

---
### SendDuiMouseMove

`SEND_DUI_MOUSE_MOVE` · hash `0xD9D7A0AA` · **Cliente**

```lua
SendDuiMouseMove(duiObject, x, y)
```
```c
void SEND_DUI_MOUSE_MOVE(long duiObject, int x, int y);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.
- `x` (`int`): The mouse X position.
- `y` (`int`): The mouse Y position.

**Devuelve:** `void`

**Descripción oficial:**

Injects a 'mouse move' event for a DUI object. Coordinates are in browser space.

---
### SendDuiMouseUp

`SEND_DUI_MOUSE_UP` · hash `0x1D735B93` · **Cliente**

```lua
SendDuiMouseUp(duiObject, button)
```
```c
void SEND_DUI_MOUSE_UP(long duiObject, char* button);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.
- `button` (`char*`): Either `'left'`, `'middle'` or `'right'`.

**Devuelve:** `void`

**Descripción oficial:**

Injects a 'mouse up' event for a DUI object. Coordinates are expected to be set using SEND_DUI_MOUSE_MOVE.

---
### SendDuiMouseWheel

`SEND_DUI_MOUSE_WHEEL` · hash `0x2D62133A` · **Cliente**

```lua
SendDuiMouseWheel(duiObject, deltaY, deltaX)
```
```c
void SEND_DUI_MOUSE_WHEEL(long duiObject, int deltaY, int deltaX);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.
- `deltaY` (`int`): The wheel Y delta.
- `deltaX` (`int`): The wheel X delta.

**Devuelve:** `void`

**Descripción oficial:**

Injects a 'mouse wheel' event for a DUI object.

---
### SendLoadingScreenMessage

`SEND_LOADING_SCREEN_MESSAGE` · hash `0x8BBE6CC0` · **Cliente**

```lua
local retval = SendLoadingScreenMessage(jsonString)
```
```c
BOOL SEND_LOADING_SCREEN_MESSAGE(char* jsonString);
```

**Parámetros**

- `jsonString` (`char*`): The JSON-encoded message.

**Devuelve:** `BOOL` — A success value.

**Descripción oficial:**

Sends a message to the `loadingScreen` NUI frame, which contains the HTML page referenced in `loadscreen` resources.

---
### SendNuiMessage

`SEND_NUI_MESSAGE` · hash `0x78608ACB` · **Cliente**

```lua
local retval = SendNuiMessage(jsonString)
```
```c
BOOL SEND_NUI_MESSAGE(char* jsonString);
```

**Parámetros**

- `jsonString` (`char*`)

**Devuelve:** `BOOL`

---
### SetAimCooldown

`SET_AIM_COOLDOWN` · hash `0xA42A3DBF` · **Cliente**

```lua
SetAimCooldown(value)
```
```c
void SET_AIM_COOLDOWN(int value);
```

**Parámetros**

- `value` (`int`): Number of milliseconds between allowed aiming

**Devuelve:** `void`

**Descripción oficial:**

Adds a cooldown between instances of moving and then aiming.
Can be optionally used to hinder 'speedboosting'
To turn off, set value to 0

---
### SetAudioSubmixEffectParamFloat

`SET_AUDIO_SUBMIX_EFFECT_PARAM_FLOAT` · hash `0x9A209B3C` · **Cliente**

```lua
SetAudioSubmixEffectParamFloat(submixId, effectSlot, paramIndex, paramValue)
```
```c
void SET_AUDIO_SUBMIX_EFFECT_PARAM_FLOAT(int submixId, int effectSlot, int paramIndex, float paramValue);
```

**Parámetros**

- `submixId` (`int`): The submix.
- `effectSlot` (`int`): The effect slot for the submix. It is expected that the effect is set in this slot beforehand.
- `paramIndex` (`int`): The parameter index for the effect.
- `paramValue` (`float`): The parameter value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a floating-point parameter for a submix effect.

---
### SetAudioSubmixEffectParamInt

`SET_AUDIO_SUBMIX_EFFECT_PARAM_INT` · hash `0x77FAE2B8` · **Cliente**

```lua
SetAudioSubmixEffectParamInt(submixId, effectSlot, paramIndex, paramValue)
```
```c
void SET_AUDIO_SUBMIX_EFFECT_PARAM_INT(int submixId, int effectSlot, int paramIndex, int paramValue);
```

**Parámetros**

- `submixId` (`int`): The submix.
- `effectSlot` (`int`): The effect slot for the submix. It is expected that the effect is set in this slot beforehand.
- `paramIndex` (`int`): The parameter index for the effect.
- `paramValue` (`int`): The parameter value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets an integer parameter for a submix effect.

---
### SetAudioSubmixEffectRadioFx

`SET_AUDIO_SUBMIX_EFFECT_RADIO_FX` · hash `0xAAA94D53` · **Cliente**

```lua
SetAudioSubmixEffectRadioFx(submixId, effectSlot)
```
```c
void SET_AUDIO_SUBMIX_EFFECT_RADIO_FX(int submixId, int effectSlot);
```

**Parámetros**

- `submixId` (`int`): The submix.
- `effectSlot` (`int`): The effect slot for the submix.

**Devuelve:** `void`

**Descripción oficial:**

Assigns a RadioFX effect to a submix effect slot.

The parameter values for this effect are as follows (backticks are used to represent hashes):

| Index | Type | Description |
|-|-|-|
| \`enabled\` | int | Enables or disables RadioFX on this DSP. |
| \`default\` | int | Sets default parameters for the RadioFX DSP and enables it. |
| \`freq_low\` | float |  |
| \`freq_hi\` | float |  |
| \`fudge\` | float |  |
| \`rm_mod_freq\` | float |  |
| \`rm_mix\` | float |  |
| \`o_freq_lo\` | float |  |
| \`o_freq_hi\` | float |  |

**Ejemplo (lua):**

```lua
-- we want to change the master output
local submix = 0

-- add a RadioFX effect to slot 0
SetAudioSubmixEffectRadioFx(submix, 0)

-- set the default values
SetAudioSubmixEffectParamInt(submix, 0, `default`, 1)
```

---
### SetAudioSubmixOutputVolumes

`SET_AUDIO_SUBMIX_OUTPUT_VOLUMES` · hash `0x825DC0D1` · **Cliente**

```lua
SetAudioSubmixOutputVolumes(submixId, outputSlot, frontLeftVolume, frontRightVolume, rearLeftVolume, rearRightVolume, channel5Volume, channel6Volume)
```
```c
void SET_AUDIO_SUBMIX_OUTPUT_VOLUMES(int submixId, int outputSlot, float frontLeftVolume, float frontRightVolume, float rearLeftVolume, float rearRightVolume, float channel5Volume, float channel6Volume);
```

**Parámetros**

- `submixId` (`int`): The submix.
- `outputSlot` (`int`): The output slot index.
- `frontLeftVolume` (`float`): The volume for the front left channel.
- `frontRightVolume` (`float`): The volume for the front right channel.
- `rearLeftVolume` (`float`): The volume for the rear left channel.
- `rearRightVolume` (`float`): The volume for the rear right channel.
- `channel5Volume` (`float`): The volume for channel 5.
- `channel6Volume` (`float`): The volume for channel 6.

**Devuelve:** `void`

**Descripción oficial:**

Sets the volumes for the sound channels in a submix effect.
Values can be between 0.0 and 1.0.
Channel 5 and channel 6 are not used in voice chat but are believed to be center and LFE channels.
Output slot starts at 0 for the first ADD_AUDIO_SUBMIX_OUTPUT call then incremented by 1 on each subsequent call.

---
### SetCalmingQuadBounds

`SET_CALMING_QUAD_BOUNDS` · hash `0xC5945BD9` · **Cliente**

```lua
local retval = SetCalmingQuadBounds(waterQuad, minX, minY, maxX, maxY)
```
```c
BOOL SET_CALMING_QUAD_BOUNDS(int waterQuad, int minX, int minY, int maxX, int maxY);
```

**Parámetros**

- `waterQuad` (`int`): The calming quad index
- `minX` (`int`): The minX coordinate
- `minY` (`int`): The minY coordinate
- `maxX` (`int`): The maxX coordinate
- `maxY` (`int`): The maxY coordinate

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetCalmingQuadBounds(1, -500, -500, 500, 500)
```

---
### SetCalmingQuadDampening

`SET_CALMING_QUAD_DAMPENING` · hash `0x67977501` · **Cliente**

```lua
local retval = SetCalmingQuadDampening(calmingQuad, dampening)
```
```c
BOOL SET_CALMING_QUAD_DAMPENING(int calmingQuad, float dampening);
```

**Parámetros**

- `calmingQuad` (`int`): The calming quad
- `dampening` (`float`): The dampening value

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetCalmingQuadDampening(0, 1.0)
```

---
### SetDefaultVehicleNumberPlateTextPattern

`SET_DEFAULT_VEHICLE_NUMBER_PLATE_TEXT_PATTERN` · hash `0x79780FD2` · **Cliente**

```lua
SetDefaultVehicleNumberPlateTextPattern(plateIndex, pattern)
```
```c
void SET_DEFAULT_VEHICLE_NUMBER_PLATE_TEXT_PATTERN(int plateIndex, char* pattern);
```

**Parámetros**

- `plateIndex` (`int`): A plate index, or `-1` to set a default for any indices that do not have a specific value.
- `pattern` (`char*`): A number plate pattern string, or a null value to reset to default.

**Devuelve:** `void`

**Descripción oficial:**

Sets the default number plate text pattern for vehicles seen on the local client with the specified plate index as their *default* index (`plateProbabilities` from carvariations).

For consistency, this should be used with the same value on all clients, since vehicles *without* custom text will use a seeded random number generator with this pattern to determine the default plate text.

The default value is `11AAA111`, and using this or a NULL string will revert to the default game RNG.

**Pattern string format**

*   `1` will lead to a random number from 0-9.
*   `A` will lead to a random letter from A-Z.
*   `.` will lead to a random letter *or* number, with 50% probability of being either.
*   `^1` will lead to a literal `1` being emitted.
*   `^A` will lead to a literal `A` being emitted.
*   Any other character will lead to said character being emitted.
*   A string shorter than 8 characters will be padded on the right.

**Ejemplo (lua):**

```lua
SetDefaultVehicleNumberPlateTextPattern(-1, ' AAA111 ')
SetDefaultVehicleNumberPlateTextPattern(4 , ' AAAAAA ')

-- fixed characters: plate will be FAYUM69C for example
SetDefaultVehicleNumberPlateTextPattern(-1, 'F^AYUM11A')
```

---
### SetDiscordAppId

`SET_DISCORD_APP_ID` · hash `0x6A02254D` · **Cliente**

```lua
SetDiscordAppId(appId)
```
```c
void SET_DISCORD_APP_ID(char* appId);
```

**Parámetros**

- `appId` (`char*`): A valid Discord API App Id, can be generated at https://discordapp.com/developers/applications/

**Devuelve:** `void`

**Descripción oficial:**

This native sets the app id for the discord rich presence implementation.

---
### SetDiscordRichPresenceAction

`SET_DISCORD_RICH_PRESENCE_ACTION` · hash `0xCBBC3FAC` · **Cliente**

```lua
SetDiscordRichPresenceAction(index, label, url)
```
```c
void SET_DISCORD_RICH_PRESENCE_ACTION(int index, char* label, char* url);
```

**Parámetros**

- `index` (`int`): The button index, either 0 or 1.
- `label` (`char*`): The text to display on the button.
- `url` (`char*`): The URL to open when clicking the button. This has to start with `fivem://connect/` or `https://`.

**Devuelve:** `void`

**Descripción oficial:**

Sets a clickable button to be displayed in a player's Discord rich presence.

---
### SetDiscordRichPresenceAsset

`SET_DISCORD_RICH_PRESENCE_ASSET` · hash `0x53DFD530` · **Cliente**

```lua
SetDiscordRichPresenceAsset(assetName)
```
```c
void SET_DISCORD_RICH_PRESENCE_ASSET(char* assetName);
```

**Parámetros**

- `assetName` (`char*`): The name of a valid asset registered on Discordapp's developer dashboard. note that the asset has to be registered under the same discord API application set using the SET_DISCORD_APP_ID native.

**Devuelve:** `void`

**Descripción oficial:**

This native sets the image asset for the discord rich presence implementation.

---
### SetDiscordRichPresenceAssetSmall

`SET_DISCORD_RICH_PRESENCE_ASSET_SMALL` · hash `0xF61D04C4` · **Cliente**

```lua
SetDiscordRichPresenceAssetSmall(assetName)
```
```c
void SET_DISCORD_RICH_PRESENCE_ASSET_SMALL(char* assetName);
```

**Parámetros**

- `assetName` (`char*`): The name of a valid asset registered on Discordapp's developer dashboard. Note that the asset has to be registered under the same discord API application set using the SET_DISCORD_APP_ID native.

**Devuelve:** `void`

**Descripción oficial:**

This native sets the small image asset for the discord rich presence implementation.

---
### SetDiscordRichPresenceAssetSmallText

`SET_DISCORD_RICH_PRESENCE_ASSET_SMALL_TEXT` · hash `0x35E62B6A` · **Cliente**

```lua
SetDiscordRichPresenceAssetSmallText(text)
```
```c
void SET_DISCORD_RICH_PRESENCE_ASSET_SMALL_TEXT(char* text);
```

**Parámetros**

- `text` (`char*`): Text to be displayed when hovering over small image asset. Note that you must also set a valid small image asset using the SET_DISCORD_RICH_PRESENCE_ASSET_SMALL native.

**Devuelve:** `void`

**Descripción oficial:**

This native sets the hover text of the small image asset for the discord rich presence implementation.

---
### SetDiscordRichPresenceAssetText

`SET_DISCORD_RICH_PRESENCE_ASSET_TEXT` · hash `0xB029D2FA` · **Cliente**

```lua
SetDiscordRichPresenceAssetText(text)
```
```c
void SET_DISCORD_RICH_PRESENCE_ASSET_TEXT(char* text);
```

**Parámetros**

- `text` (`char*`): Text to be displayed when hovering over image asset. Note that you must also set a valid image asset using the SET_DISCORD_RICH_PRESENCE_ASSET native.

**Devuelve:** `void`

**Descripción oficial:**

This native sets the hover text of the image asset for the discord rich presence implementation.

---
### SetDuiUrl

`SET_DUI_URL` · hash `0xF761D9F3` · **Cliente**

```lua
SetDuiUrl(duiObject, url)
```
```c
void SET_DUI_URL(long duiObject, char* url);
```

**Parámetros**

- `duiObject` (`long`): The DUI browser handle.
- `url` (`char*`): The new URL.

**Devuelve:** `void`

**Descripción oficial:**

Navigates the specified DUI browser to a different URL.

---
### SetEmitterProbeLength

`SET_EMITTER_PROBE_LENGTH` · hash `0x8AA1F3C2` · **Cliente**

```lua
SetEmitterProbeLength(probeLength)
```
```c
void SET_EMITTER_PROBE_LENGTH(float probeLength);
```

**Parámetros**

- `probeLength` (`float`): The desired probe length (20.0 - 150.0)

**Devuelve:** `void`

**Descripción oficial:**

Allows StaticEmitter's without a linked entity to make use of environment features like occlusion and reverb even if they are located higher than 20.0 units above any static collision inside interiors.

This native allows you to extend the probe range up to 150.0 units.

**Ejemplo (lua):**

```lua
RegisterCommand("setEmitterProbeLength", function(src, args, raw)
    local probeLength = (tonumber(args[1]) + 0.0)

    print("Extending emitter probes to: ", probeLength)
    SetEmitterProbeLength(probeLength)
end)

RegisterCommand("resetEmitterProbeLength", function()
    print("Resetting emitter probes to default settings")
    SetEmitterProbeLength(20.0)
end)
```

---
### SetEntityDrawOutline

`SET_ENTITY_DRAW_OUTLINE` · hash `0x76180407` · **Cliente**

```lua
SetEntityDrawOutline(entity, enabled)
```
```c
void SET_ENTITY_DRAW_OUTLINE(Entity entity, BOOL enabled);
```

**Parámetros**

- `entity` (`Entity`): A valid entity handle.
- `enabled` (`BOOL`): Whether or not to draw an outline.

**Devuelve:** `void`

**Descripción oficial:**

Draws an outline around a given entity. This function supports SDK infrastructure and is not intended to be used directly from your code.

---
### SetEntityDrawOutlineColor

`SET_ENTITY_DRAW_OUTLINE_COLOR` · hash `0xB41A56C2` · **Cliente**

```lua
SetEntityDrawOutlineColor(red, green, blue, alpha)
```
```c
void SET_ENTITY_DRAW_OUTLINE_COLOR(int red, int green, int blue, int alpha);
```

**Parámetros**

- `red` (`int`): Red component of color.
- `green` (`int`): Green component of color.
- `blue` (`int`): Blue component of color.
- `alpha` (`int`): Alpha component of color, ignored for shader `0`.

**Devuelve:** `void`

**Descripción oficial:**

Sets color for entity outline. `255, 0, 255, 255` by default.

---
### SetEntityDrawOutlineRenderTechnique

`SET_ENTITY_DRAW_OUTLINE_RENDER_TECHNIQUE` · hash `0x68DFF2DD` · **Cliente**

```lua
SetEntityDrawOutlineRenderTechnique(techniqueGroup)
```
```c
void SET_ENTITY_DRAW_OUTLINE_RENDER_TECHNIQUE(char* techniqueGroup);
```

**Parámetros**

- `techniqueGroup` (`char*`): Technique group name.

**Devuelve:** `void`

**Descripción oficial:**

Sets the render technique for drawing an entity's outline. This function allows you to specify a technique group name to control how the entity's outline is rendered in the game.

List of known technique group's:

```
alt0
alt1
alt2
alt3
alt4
alt5
alt6
alt7
alt8
blit
cube
default
geometry
imposter
imposterdeferred
lightweight0
lightweight0CutOut
lightweight0CutOutTint
lightweight0WaterRefractionAlpha
lightweight4
lightweight4CutOut
lightweight4CutOutTint
lightweight4WaterRefractionAlpha
lightweight8
lightweight8CutOut
lightweight8CutOutTint
lightweight8WaterRefractionAlpha
lightweightHighQuality0
lightweightHighQuality0CutOut
lightweightHighQuality0WaterRefractionAlpha
lightweightHighQuality4
lightweightHighQuality4CutOut
lightweightHighQuality4WaterRefractionAlpha
lightweightHighQuality8
lightweightHighQuality8CutOut
lightweightHighQuality8WaterRefractionAlpha
lightweightNoCapsule4
lightweightNoCapsule8
multilight
tessellate
ui
unlit
waterreflection
waterreflectionalphaclip
waterreflectionalphacliptint
wdcascade
```

---
### SetEntityDrawOutlineShader

`SET_ENTITY_DRAW_OUTLINE_SHADER` · hash `0x5261A01A` · **Cliente**

```lua
SetEntityDrawOutlineShader(shader)
```
```c
void SET_ENTITY_DRAW_OUTLINE_SHADER(int shader);
```

**Parámetros**

- `shader` (`int`): An outline shader variant.

**Devuelve:** `void`

**Descripción oficial:**

Sets variant of shader that will be used to draw entity outline.

Variants are:

*   **0**: Default value, gauss shader.
*   **1**: 2px wide solid color outline.
*   **2**: Fullscreen solid color except for entity.

---
### SetEntityMatrix

`SET_ENTITY_MATRIX` · hash `0xFB0639B` · **Cliente**

```lua
SetEntityMatrix(entity, forwardX, forwardY, forwardZ, rightX, rightY, rightZ, upX, upY, upZ, atX, atY, atZ)
```
```c
void SET_ENTITY_MATRIX(Entity entity, float forwardX, float forwardY, float forwardZ, float rightX, float rightY, float rightZ, float upX, float upY, float upZ, float atX, float atY, float atZ);
```

**Parámetros**

- `entity` (`Entity`): A valid entity handle.
- `forwardX` (`float`)
- `forwardY` (`float`)
- `forwardZ` (`float`)
- `rightX` (`float`)
- `rightY` (`float`)
- `rightZ` (`float`)
- `upX` (`float`)
- `upY` (`float`)
- `upZ` (`float`)
- `atX` (`float`)
- `atY` (`float`)
- `atZ` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Sets an entity's matrix. Arguments are in the same order as with GET_ENTITY_MATRIX.

---
### SetFallDamageLandOnFootMultiplier

`SET_FALL_DAMAGE_LAND_ON_FOOT_MULTIPLIER` · hash `0xA9EC9A79` · **Cliente**

```lua
SetFallDamageLandOnFootMultiplier(multiplier)
```
```c
void SET_FALL_DAMAGE_LAND_ON_FOOT_MULTIPLIER(float multiplier);
```

**Parámetros**

- `multiplier` (`float`): fall damage multiplier to apply when a ped lands on foot from a fall below the kill fall height threshold (i.e., when the fall does not cause instant death). Default value is `3.0`.

**Devuelve:** `void`

**Descripción oficial:**

A setter for [GET_FALL_DAMAGE_LAND_ON_FOOT_MULTIPLIER](https://docs.fivem.net/natives/?_0x3C8A1C92).

---
### SetFallDamageMultiplier

`SET_FALL_DAMAGE_MULTIPLIER` · hash `0xB43B621B` · **Cliente**

```lua
SetFallDamageMultiplier(multiplier)
```
```c
void SET_FALL_DAMAGE_MULTIPLIER(float multiplier);
```

**Parámetros**

- `multiplier` (`float`): fall damage multiplier applied to all peds when calculating fall damage from falls below the kill fall height threshold (i.e., when the fall does not cause instant death). Default value is `7.0`.

**Devuelve:** `void`

**Descripción oficial:**

A setter for [GET_FALL_DAMAGE_MULTIPLIER](https://docs.fivem.net/natives/?_0x2D6A0A83).

---
### SetFlashLightKeepOnWhileMoving

`SET_FLASH_LIGHT_KEEP_ON_WHILE_MOVING` · hash `0x7635B349` · **Cliente**

```lua
SetFlashLightKeepOnWhileMoving(state)
```
```c
void SET_FLASH_LIGHT_KEEP_ON_WHILE_MOVING(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): On/Off

**Devuelve:** `void`

**Descripción oficial:**

Allows Weapon-Flashlight beams to stay visible while moving. Normally it only stays on while aiming.

---
### SetFlyThroughWindscreenParams

`SET_FLY_THROUGH_WINDSCREEN_PARAMS` · hash `0x4D3118ED` · **Cliente**

```lua
local retval = SetFlyThroughWindscreenParams(vehMinSpeed, unkMinSpeed, unkModifier, minDamage)
```
```c
BOOL SET_FLY_THROUGH_WINDSCREEN_PARAMS(float vehMinSpeed, float unkMinSpeed, float unkModifier, float minDamage);
```

**Parámetros**

- `vehMinSpeed` (`float`): Vehicle minimum speed (default 35.0).
- `unkMinSpeed` (`float`): Unknown minimum speed (default 40.0).
- `unkModifier` (`float`): Unknown modifier (default 17.0).
- `minDamage` (`float`): Minimum damage (default 2000.0).

**Devuelve:** `BOOL` — A bool indicating if parameters was set successfully.

**Descripción oficial:**

Sets some in-game parameters which is used for checks is ped needs to fly through windscreen after a crash.

---
### SetFogVolumeRenderDisabled

`SET_FOG_VOLUME_RENDER_DISABLED` · hash `0xFBC64DA3` · **Cliente**

```lua
SetFogVolumeRenderDisabled(state)
```
```c
void SET_FOG_VOLUME_RENDER_DISABLED(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): Toggle on or off.

**Devuelve:** `void`

**Descripción oficial:**

This completely disables rendering of fog volumes (vfxfogvolumeinfo.ymt).

---
### SetFuelConsumptionRateMultiplier

`SET_FUEL_CONSUMPTION_RATE_MULTIPLIER` · hash `0x845F3E5C` · **Cliente**

```lua
SetFuelConsumptionRateMultiplier(multiplier)
```
```c
void SET_FUEL_CONSUMPTION_RATE_MULTIPLIER(float multiplier);
```

**Parámetros**

- `multiplier` (`float`): Global fuel consumption multiplier. If negative - 0 will be used instead.

**Devuelve:** `void`

**Descripción oficial:**

Sets fuel consumption rate multiplier for all vehicles operated by a player. This is a way to slow down or speed up fuel consumption for all vehicles at a time. If 0 - it practically means that fuel will not be consumed. By default is set to 1.

When the multiplier is set to 1 a default 65 litre gas tank car with average fuel consumption can stay idle for ~16.67 hours or run with max RPM for ~2.5 hours.

To customize fuel consumption per vehicle / vehicle class use [`SET_HANDLING_FLOAT`](#sethandlingfloat)/[`SET_VEHICLE_HANDLING_FLOAT`](#setvehiclehandlingfloat) natives with `fieldName` equal to `fPetrolConsumptionRate`. By default it is set to 0.5 for all vehicles.

---
### SetFuelConsumptionState

`SET_FUEL_CONSUMPTION_STATE` · hash `0x81DAD03E` · **Cliente**

```lua
SetFuelConsumptionState(state)
```
```c
void SET_FUEL_CONSUMPTION_STATE(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): True to turn on. False to turn off.

**Devuelve:** `void`

**Descripción oficial:**

Turns on and off fuel consumption in all vehicles operated by a player. NPC operated vehicles will not consume fuel to avoid traffic disruptions.

The default Gta5 behaviour is fuel consumption turned off.

---
### SetGlobalPassengerMassMultiplier

`SET_GLOBAL_PASSENGER_MASS_MULTIPLIER` · hash `0x1C47F6AC` · **Cliente**

```lua
SetGlobalPassengerMassMultiplier(massMul)
```
```c
void SET_GLOBAL_PASSENGER_MASS_MULTIPLIER(float massMul);
```

**Parámetros**

- `massMul` (`float`): Weight of each passenger (not counting the driver) as a percentage of vehicle mass. Is applied to all vehicles. Default value is 0.05

**Devuelve:** `void`

---
### SetHandlingField

`SET_HANDLING_FIELD` · hash `0xFE8064E3` · **Cliente**

```lua
SetHandlingField(vehicle, class_, fieldName, value)
```
```c
void SET_HANDLING_FIELD(char* vehicle, char* class_, char* fieldName, Any value);
```

**Parámetros**

- `vehicle` (`char*`): The vehicle class to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`Any`): The value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a global handling override for a specific vehicle class. The name is supposed to match the `handlingName` field from handling.meta.
Example: `SetHandlingField('AIRTUG', 'CHandlingData', 'fSteeringLock', 360.0)`

---
### SetHandlingFloat

`SET_HANDLING_FLOAT` · hash `0x90DD01C` · **Cliente**

```lua
SetHandlingFloat(vehicle, class_, fieldName, value)
```
```c
void SET_HANDLING_FLOAT(char* vehicle, char* class_, char* fieldName, float value);
```

**Parámetros**

- `vehicle` (`char*`): The vehicle class to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`float`): The floating-point value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a global handling override for a specific vehicle class. The name is supposed to match the `handlingName` field from handling.meta.
Example: `SetHandlingFloat('AIRTUG', 'CHandlingData', 'fSteeringLock', 360.0)`

---
### SetHandlingInt

`SET_HANDLING_INT` · hash `0x8AB3F46C` · **Cliente**

```lua
SetHandlingInt(vehicle, class_, fieldName, value)
```
```c
void SET_HANDLING_INT(char* vehicle, char* class_, char* fieldName, int value);
```

**Parámetros**

- `vehicle` (`char*`): The vehicle class to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`int`): The integer value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a global handling override for a specific vehicle class. The name is supposed to match the `handlingName` field from handling.meta.

---
### SetHandlingVector

`SET_HANDLING_VECTOR` · hash `0x7F9D543` · **Cliente**

```lua
SetHandlingVector(vehicle, class_, fieldName, value)
```
```c
void SET_HANDLING_VECTOR(char* vehicle, char* class_, char* fieldName, Vector3 value);
```

**Parámetros**

- `vehicle` (`char*`): The vehicle class to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`Vector3`): The Vector3 value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a global handling override for a specific vehicle class. The name is supposed to match the `handlingName` field from handling.meta.
Example: `SetHandlingVector('AIRTUG', 'CHandlingData', 'vecCentreOfMassOffset', vector3(0.0, 0.0, -5.0))`

---
### SetHealthConfigDefaultArmor

`SET_HEALTH_CONFIG_DEFAULT_ARMOR` · hash `0x20A1E6A2` · **Cliente**

```lua
SetHealthConfigDefaultArmor(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_DEFAULT_ARMOR(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default armor value for specific health config.

---
### SetHealthConfigDefaultEndurance

`SET_HEALTH_CONFIG_DEFAULT_ENDURANCE` · hash `0x60F20B81` · **Cliente**

```lua
SetHealthConfigDefaultEndurance(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_DEFAULT_ENDURANCE(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default endurance value for specific health config.

---
### SetHealthConfigDefaultHealth

`SET_HEALTH_CONFIG_DEFAULT_HEALTH` · hash `0xC705C778` · **Cliente**

```lua
SetHealthConfigDefaultHealth(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_DEFAULT_HEALTH(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default health value for specific health config.

---
### SetHealthConfigDogTakedownThreshold

`SET_HEALTH_CONFIG_DOG_TAKEDOWN_THRESHOLD` · hash `0x9A995E96` · **Cliente**

```lua
SetHealthConfigDogTakedownThreshold(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_DOG_TAKEDOWN_THRESHOLD(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default dog takedown threshold value for specific health config.

---
### SetHealthConfigDyingThreshold

`SET_HEALTH_CONFIG_DYING_THRESHOLD` · hash `0x9B00FD77` · **Cliente**

```lua
SetHealthConfigDyingThreshold(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_DYING_THRESHOLD(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default dying health threshold value for specific health config.

---
### SetHealthConfigFatiguedThreshold

`SET_HEALTH_CONFIG_FATIGUED_THRESHOLD` · hash `0xC58953FD` · **Cliente**

```lua
SetHealthConfigFatiguedThreshold(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_FATIGUED_THRESHOLD(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default fatigued health threshold value for specific health config.

---
### SetHealthConfigHurtThreshold

`SET_HEALTH_CONFIG_HURT_THRESHOLD` · hash `0x98DF1A83` · **Cliente**

```lua
SetHealthConfigHurtThreshold(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_HURT_THRESHOLD(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default hurt health threshold value for specific health config.

---
### SetHealthConfigInjuredThreshold

`SET_HEALTH_CONFIG_INJURED_THRESHOLD` · hash `0xF9D9B647` · **Cliente**

```lua
SetHealthConfigInjuredThreshold(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_INJURED_THRESHOLD(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default injured health threshold value for specific health config.

---
### SetHealthConfigInvincible

`SET_HEALTH_CONFIG_INVINCIBLE` · hash `0x4A9EEDE6` · **Cliente**

```lua
SetHealthConfigInvincible(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_INVINCIBLE(char* configName, BOOL newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`BOOL`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default invincible value for specific health config.

---
### SetHealthConfigMeleeFatalAttack

`SET_HEALTH_CONFIG_MELEE_FATAL_ATTACK` · hash `0xDD443E53` · **Cliente**

```lua
SetHealthConfigMeleeFatalAttack(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_MELEE_FATAL_ATTACK(char* configName, BOOL newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`BOOL`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default melee cardinal fatal attack value for specific health config.

---
### SetHealthConfigWritheFromBulletThreshold

`SET_HEALTH_CONFIG_WRITHE_FROM_BULLET_THRESHOLD` · hash `0xE97633CB` · **Cliente**

```lua
SetHealthConfigWritheFromBulletThreshold(configName, newValue)
```
```c
void SET_HEALTH_CONFIG_WRITHE_FROM_BULLET_THRESHOLD(char* configName, float newValue);
```

**Parámetros**

- `configName` (`char*`): Name of health config.
- `newValue` (`float`): Value

**Devuelve:** `void`

**Descripción oficial:**

Sets default writhe from bullet threshold value for specific health config.

---
### SetHudComponentAlign

`SET_HUD_COMPONENT_ALIGN` · hash `0xEED219F2` · **Cliente**

```lua
SetHudComponentAlign(id, horizontalAlign, verticalAlign)
```
```c
void SET_HUD_COMPONENT_ALIGN(int id, int horizontalAlign, int verticalAlign);
```

**Parámetros**

- `id` (`int`): The hud component id.
- `horizontalAlign` (`int`): The horizontal alignment.
- `verticalAlign` (`int`): The vertical alignment.

**Devuelve:** `void`

**Descripción oficial:**

See [SET_SCRIPT_GFX_ALIGN](../gta5/GRAPHICS.md#setscriptgfxalign) for details about how gfx align works.

---
### SetHudComponentSize

`SET_HUD_COMPONENT_SIZE` · hash `0x7644A9FA` · **Cliente**

```lua
SetHudComponentSize(id, x, y)
```
```c
void SET_HUD_COMPONENT_SIZE(int id, float x, float y);
```

**Parámetros**

- `id` (`int`): The hud component id.
- `x` (`float`): New size X.
- `y` (`float`): New size Y.

**Devuelve:** `void`

---
### SetInteriorPortalCornerPosition

`SET_INTERIOR_PORTAL_CORNER_POSITION` · hash `0x87F43553` · **Cliente**

```lua
SetInteriorPortalCornerPosition(interiorId, portalIndex, cornerIndex, posX, posY, posZ)
```
```c
void SET_INTERIOR_PORTAL_CORNER_POSITION(int interiorId, int portalIndex, int cornerIndex, float posX, float posY, float posZ);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `cornerIndex` (`int`): Interior corner index.
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local portalCount = GetInteriorPortalCount(interiorId)

  -- rip portals
  for portalIndex = 0, portalCount - 1 do
    for cornerIndex = 0, 3 do -- 4 corners
      SetInteriorPortalCornerPosition(interiorId, portalIndex, cornerIndex, 0.0, 0.0, 0.0)
    end
  end
  
  RefreshInterior(interiorId)
end
```

---
### SetInteriorPortalEntityFlag

`SET_INTERIOR_PORTAL_ENTITY_FLAG` · hash `0x8349CD76` · **Cliente**

```lua
SetInteriorPortalEntityFlag(interiorId, portalIndex, entityIndex, flag)
```
```c
void SET_INTERIOR_PORTAL_ENTITY_FLAG(int interiorId, int portalIndex, int entityIndex, int flag);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `entityIndex` (`int`): Portal entity index.
- `flag` (`int`): New flag value.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local portalIndex = 0

if interiorId ~= 0 then
  local count = GetInteriorPortalEntityCount(interiorId, portalIndex)
  for i=0, count-1 do
    SetInteriorPortalEntityFlag(interiorId, portalIndex, i, 0)
  end
  RefreshInterior(interiorId)
end
```

---
### SetInteriorPortalFlag

`SET_INTERIOR_PORTAL_FLAG` · hash `0x88B2355E` · **Cliente**

```lua
SetInteriorPortalFlag(interiorId, portalIndex, flag)
```
```c
void SET_INTERIOR_PORTAL_FLAG(int interiorId, int portalIndex, int flag);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `flag` (`int`): New flag value.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local portalIndex = 0

  SetInteriorPortalFlag(interiorId, portalIndex, 1)
  RefreshInterior(interiorId)
end
```

---
### SetInteriorPortalRoomFrom

`SET_INTERIOR_PORTAL_ROOM_FROM` · hash `0x298FC783` · **Cliente**

```lua
SetInteriorPortalRoomFrom(interiorId, portalIndex, roomFrom)
```
```c
void SET_INTERIOR_PORTAL_ROOM_FROM(int interiorId, int portalIndex, int roomFrom);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `roomFrom` (`int`): New value.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local portalIndex = 0

  SetInteriorPortalRoomFrom(interiorId, portalIndex, 0)
  RefreshInterior(interiorId)
end
```

---
### SetInteriorPortalRoomTo

`SET_INTERIOR_PORTAL_ROOM_TO` · hash `0x58982680` · **Cliente**

```lua
SetInteriorPortalRoomTo(interiorId, portalIndex, roomTo)
```
```c
void SET_INTERIOR_PORTAL_ROOM_TO(int interiorId, int portalIndex, int roomTo);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `portalIndex` (`int`): Interior portal index.
- `roomTo` (`int`): New value.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  local portalIndex = 0

  SetInteriorPortalRoomTo(interiorId, portalIndex, 0)
  RefreshInterior(interiorId)
end
```

---
### SetInteriorProbeLength

`SET_INTERIOR_PROBE_LENGTH` · hash `0x423F7E39` · **Cliente**

```lua
SetInteriorProbeLength(probeLength)
```
```c
void SET_INTERIOR_PROBE_LENGTH(float probeLength);
```

**Parámetros**

- `probeLength` (`float`): The desired probe length (0.0 - 150.0)

**Devuelve:** `void`

**Descripción oficial:**

Overwrite the games default CPortalTracker interior detection range.
This fixes potentially unwanted behaviour in the base game and allows you to build custom interiors with larger ceiling heights without running into graphical glitches.

By default CPortalTracker will probe 4 units downward trying to reach collisions that are part of the interior the entity is in.
If no collision can be found 16 units are used in some circumstances.

There are 30+ hard coded special cases, only some of them exposed via script (for example `ENABLE_STADIUM_PROBES_THIS_FRAME`).

This native allows you to extend the probe range up to 150 units which is the same value the game uses for the `xs_arena_interior`

**Ejemplo (lua):**

```lua
RegisterCommand("setInteriorProbeLength", function(src, args, raw)
    local probeLength = (tonumber(args[1]) + 0.0)

    print("Extending interior detection probes to: ", probeLength)
    SetInteriorProbeLength(probeLength)
end)

RegisterCommand("resetInteriorProbeLength", function()
    print("Resetting interior detection probes to default settings")
    SetInteriorProbeLength(0.0)
end)
```

---
### SetInteriorRoomExtents

`SET_INTERIOR_ROOM_EXTENTS` · hash `0x4FDCF51E` · **Cliente**

```lua
SetInteriorRoomExtents(interiorId, roomIndex, bbMinX, bbMinY, bbMinZ, bbMaxX, bbMaxY, bbMaxZ)
```
```c
void SET_INTERIOR_ROOM_EXTENTS(int interiorId, int roomIndex, float bbMinX, float bbMinY, float bbMinZ, float bbMaxX, float bbMaxY, float bbMaxZ);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomIndex` (`int`): Interior room index.
- `bbMinX` (`float`)
- `bbMinY` (`float`)
- `bbMinZ` (`float`)
- `bbMaxX` (`float`)
- `bbMaxY` (`float`)
- `bbMaxZ` (`float`)

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)

if interiorId ~= 0 then
  SetInteriorRoomExtents(interiorId, 0, -999.0, -999.0, -100.0, 999.0, 999.0, 100.0) -- 0 is a limbo usually
  RefreshInterior(interiorId)
end
```

---
### SetInteriorRoomFlag

`SET_INTERIOR_ROOM_FLAG` · hash `0x5518D60B` · **Cliente**

```lua
SetInteriorRoomFlag(interiorId, roomIndex, flag)
```
```c
void SET_INTERIOR_ROOM_FLAG(int interiorId, int roomIndex, int flag);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomIndex` (`int`): Interior room index.
- `flag` (`int`): New flag value.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local roomHash = GetRoomKeyFromEntity(playerPed)
local roomId = GetInteriorRoomIndexByHash(interiorId, roomHash)

if roomId ~= -1 then
  SetInteriorRoomFlag(interiorId, roomId, 64)
  RefreshInterior(interiorId)
end
```

---
### SetInteriorRoomTimecycle

`SET_INTERIOR_ROOM_TIMECYCLE` · hash `0x31C9A848` · **Cliente**

```lua
SetInteriorRoomTimecycle(interiorId, roomIndex, timecycleHash)
```
```c
void SET_INTERIOR_ROOM_TIMECYCLE(int interiorId, int roomIndex, int timecycleHash);
```

**Parámetros**

- `interiorId` (`int`): The target interior.
- `roomIndex` (`int`): Interior room index.
- `timecycleHash` (`int`): Timecycle hash.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local playerPed = PlayerPedId()
local interiorId = GetInteriorFromEntity(playerPed)
local roomHash = GetRoomKeyFromEntity(playerPed)
local roomId = GetInteriorRoomIndexByHash(interiorId, roomHash)

if roomId ~= -1 then
  local timecycleHash = GetHashKey("scanline_cam")
  SetInteriorRoomTimecycle(interiorId, roomId, timecycleHash)
  RefreshInterior(interiorId)
end
```

---
### SetKeyMappingHideResources

`SET_KEY_MAPPING_HIDE_RESOURCES` · hash `0xCB0241B5` · **Cliente**

```lua
SetKeyMappingHideResources(hide)
```
```c
void SET_KEY_MAPPING_HIDE_RESOURCES(bool hide);
```

**Parámetros**

- `hide` (`bool`): `true` will disable the display of resource names, and `false` will enable it.

**Devuelve:** `void`

**Descripción oficial:**

Toggles the visibility of resource names in the FiveM key mapping page.

---
### SetKillFallHeight

`SET_KILL_FALL_HEIGHT` · hash `0x24091E09` · **Cliente**

```lua
SetKillFallHeight(height)
```
```c
void SET_KILL_FALL_HEIGHT(float height);
```

**Parámetros**

- `height` (`float`): height from which the non-player peds will instantly die from fall damage. Default value is `10.0`.

**Devuelve:** `void`

**Descripción oficial:**

A setter for [GET_KILL_FALL_HEIGHT](https://docs.fivem.net/natives/?_0x884C8B5A).

---
### SetLightAlpha

`SET_LIGHT_ALPHA` · hash `0xC0EBC38` · **Cliente**

```lua
SetLightAlpha(alpha)
```
```c
void SET_LIGHT_ALPHA(float alpha);
```

**Parámetros**

- `alpha` (`float`): The alpha transparency value (0.0 to 1.0)

**Devuelve:** `void`

**Descripción oficial:**

Set the alpha transparency of the light.

---
### SetLightAo

`SET_LIGHT_AO` · hash `0xE155B53B` · **Cliente**

```lua
SetLightAo(intensity, radius, bias, intensity2)
```
```c
void SET_LIGHT_AO(float intensity, float radius, float bias, float intensity2);
```

**Parámetros**

- `intensity` (`float`): The AO intensity
- `radius` (`float`): The AO radius
- `bias` (`float`): The AO bias
- `intensity2` (`float`): Secondary AO intensity

**Devuelve:** `void`

**Descripción oficial:**

Set ambient occlusion (AO) parameters for a specified light.

---
### SetLightCapsuleSize

`SET_LIGHT_CAPSULE_SIZE` · hash `0xA3881271` · **Cliente**

```lua
SetLightCapsuleSize(size)
```
```c
void SET_LIGHT_CAPSULE_SIZE(float size);
```

**Parámetros**

- `size` (`float`): The capsule size value

**Devuelve:** `void`

**Descripción oficial:**

Set the capsule size of a specified light.

---
### SetLightClipRect

`SET_LIGHT_CLIP_RECT` · hash `0xD9DD0717` · **Cliente**

```lua
SetLightClipRect(x, y, width, height)
```
```c
void SET_LIGHT_CLIP_RECT(int x, int y, int width, int height);
```

**Parámetros**

- `x` (`int`): The x-coordinate of the clip rectangle
- `y` (`int`): The y-coordinate of the clip rectangle
- `width` (`int`): The width of the clip rectangle
- `height` (`int`): The height of the clip rectangle

**Devuelve:** `void`

**Descripción oficial:**

Set the clip rectangle for a created light.

---
### SetLightColor

`SET_LIGHT_COLOR` · hash `0x65FE5132` · **Cliente**

```lua
SetLightColor(r, g, b)
```
```c
void SET_LIGHT_COLOR(int r, int g, int b);
```

**Parámetros**

- `r` (`int`): Red color component (0-255)
- `g` (`int`): Green color component (0-255)
- `b` (`int`): Blue color component (0-255)

**Devuelve:** `void`

**Descripción oficial:**

Set the color of a specified light.

---
### SetLightCone

`SET_LIGHT_CONE` · hash `0x9FE89EF5` · **Cliente**

```lua
SetLightCone(innerConeAngle, outerConeAngle)
```
```c
void SET_LIGHT_CONE(float innerConeAngle, float outerConeAngle);
```

**Parámetros**

- `innerConeAngle` (`float`): The inner cone angle in degrees
- `outerConeAngle` (`float`): The outer cone angle in degrees

**Devuelve:** `void`

**Descripción oficial:**

Set the inner and outer cone angles of a specified light.

---
### SetLightCoords

`SET_LIGHT_COORDS` · hash `0x8950BD08` · **Cliente**

```lua
SetLightCoords(x, y, z)
```
```c
void SET_LIGHT_COORDS(float x, float y, float z);
```

**Parámetros**

- `x` (`float`): The X coordinate
- `y` (`float`): The Y coordinate
- `z` (`float`): The Z coordinate

**Devuelve:** `void`

**Descripción oficial:**

Set the world coordinates of a specified light.

---
### SetLightDirection

`SET_LIGHT_DIRECTION` · hash `0xA6FE1977` · **Cliente**

```lua
SetLightDirection(xDir, yDir, zDir, xTanDir, yTanDir, zTanDir)
```
```c
void SET_LIGHT_DIRECTION(float xDir, float yDir, float zDir, float xTanDir, float yTanDir, float zTanDir);
```

**Parámetros**

- `xDir` (`float`): , **yDir**, **zDir**: Components of the normalized forward (direction) vector
- `yDir` (`float`)
- `zDir` (`float`)
- `xTanDir` (`float`): , **yTanDir**, **zTanDir**: Components of the normalized tangent vector (defines rotation around the forward axis)
- `yTanDir` (`float`)
- `zTanDir` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Set the forward and tangent direction vectors for an existing light, allowing control over its orientation (useful for spotlights and directional lights).

---
### SetLightExtraflags

`SET_LIGHT_EXTRAFLAGS` · hash `0xB2D37E97` · **Cliente**

```lua
SetLightExtraflags(extraFlags)
```
```c
void SET_LIGHT_EXTRAFLAGS(int extraFlags);
```

**Parámetros**

- `extraFlags` (`int`): Bitmask of extra flags

**Devuelve:** `void`

**Descripción oficial:**

Set additional configuration flags for an existing light

---
### SetLightFadeDistance

`SET_LIGHT_FADE_DISTANCE` · hash `0xFA46714D` · **Cliente**

```lua
SetLightFadeDistance(fadeDistance)
```
```c
void SET_LIGHT_FADE_DISTANCE(int fadeDistance);
```

**Parámetros**

- `fadeDistance` (`int`): Maximum distance

**Devuelve:** `void`

**Descripción oficial:**

Set the fade distance.

---
### SetLightFalloff

`SET_LIGHT_FALLOFF` · hash `0x4D7F6E03` · **Cliente**

```lua
SetLightFalloff(falloff)
```
```c
void SET_LIGHT_FALLOFF(float falloff);
```

**Parámetros**

- `falloff` (`float`): A floating‑point value determining the rate at which light intensity diminishes with distance (must be > 0; values ≤ 0 will be clamped internally)

**Devuelve:** `void`

**Descripción oficial:**

Adjust the falloff parameter for an existing light, affecting how light intensity decreases over distance.

---
### SetLightFlags

`SET_LIGHT_FLAGS` · hash `0x28B22733` · **Cliente**

```lua
SetLightFlags(flags)
```
```c
void SET_LIGHT_FLAGS(int flags);
```

**Parámetros**

- `flags` (`int`): Bitmask of flags to apply to the light

**Devuelve:** `void`

**Descripción oficial:**

Set or update specific flags for a created light to control its behavior or properties.

---
### SetLightHeadlight

`SET_LIGHT_HEADLIGHT` · hash `0xFF44D502` · **Cliente**

```lua
SetLightHeadlight(intensity, range)
```
```c
void SET_LIGHT_HEADLIGHT(float intensity, float range);
```

**Parámetros**

- `intensity` (`float`): The intensity level of the headlight
- `range` (`float`): The effective range of the headlight

**Devuelve:** `void`

**Descripción oficial:**

Set the headlight properties of a created light, adjusting its intensity and range.

---
### SetLightIntensity

`SET_LIGHT_INTENSITY` · hash `0x2CC9A71C` · **Cliente**

```lua
SetLightIntensity(intensity)
```
```c
void SET_LIGHT_INTENSITY(float intensity);
```

**Parámetros**

- `intensity` (`float`): The intensity value to set

**Devuelve:** `void`

**Descripción oficial:**

Set the intensity of an existing light.

---
### SetLightInterior

`SET_LIGHT_INTERIOR` · hash `0x1CC72443` · **Cliente**

```lua
SetLightInterior(interiorId, isPortal, roomIndex)
```
```c
void SET_LIGHT_INTERIOR(int interiorId, bool isPortal, int roomIndex);
```

**Parámetros**

- `interiorId` (`int`): The ID of the interior where the light should be active
- `isPortal` (`bool`): Attach to a portal or room
- `roomIndex` (`int`): The specific room

**Devuelve:** `void`

**Descripción oficial:**

Set the interior and room where the light should be active.

---
### SetLightPlane

`SET_LIGHT_PLANE` · hash `0xE46E0CDF` · **Cliente**

```lua
SetLightPlane(x, y, z, w)
```
```c
void SET_LIGHT_PLANE(float x, float y, float z, float w);
```

**Parámetros**

- `x` (`float`): X component of the plane
- `y` (`float`): Y component of the plane
- `z` (`float`): Z component of the plane
- `w` (`float`): W component of the plane

**Devuelve:** `void`

**Descripción oficial:**

Set the plane parameters for a light.

---
### SetLightRadius

`SET_LIGHT_RADIUS` · hash `0x4A4B5CBE` · **Cliente**

```lua
SetLightRadius(radius)
```
```c
void SET_LIGHT_RADIUS(float radius);
```

**Parámetros**

- `radius` (`float`): The radius value to set

**Devuelve:** `void`

**Descripción oficial:**

Set the radius of a created light.

---
### SetLightShadowDetails

`SET_LIGHT_SHADOW_DETAILS` · hash `0xA40EAC1A` · **Cliente**

```lua
SetLightShadowDetails(shadowFlags, shadowDistance, shadowFade, shadowDepthBiasScale)
```
```c
void SET_LIGHT_SHADOW_DETAILS(int shadowFlags, float shadowDistance, float shadowFade, float shadowDepthBiasScale);
```

**Parámetros**

- `shadowFlags` (`int`): Flags controlling shadow behavior
- `shadowDistance` (`float`): The distance at which shadows are rendered
- `shadowFade` (`float`): The fade distance for shadows
- `shadowDepthBiasScale` (`float`): The depth bias scale

**Devuelve:** `void`

**Descripción oficial:**

Set the shadow details for a created light.

---
### SetLightShadowFadeDistance

`SET_LIGHT_SHADOW_FADE_DISTANCE` · hash `0x3C54C2A8` · **Cliente**

```lua
SetLightShadowFadeDistance(fadeDistance)
```
```c
void SET_LIGHT_SHADOW_FADE_DISTANCE(int fadeDistance);
```

**Parámetros**

- `fadeDistance` (`int`): The distance at which the shadow fades

**Devuelve:** `void`

**Descripción oficial:**

Set the fade distance for the shadows of a created light.

---
### SetLightSpecularFadeDistance

`SET_LIGHT_SPECULAR_FADE_DISTANCE` · hash `0xC3A35A50` · **Cliente**

```lua
SetLightSpecularFadeDistance(fadeDistance)
```
```c
void SET_LIGHT_SPECULAR_FADE_DISTANCE(int fadeDistance);
```

**Parámetros**

- `fadeDistance` (`int`): The distance at which specular highlights fade

**Devuelve:** `void`

**Descripción oficial:**

Set the specular fade distance for a created light.

---
### SetLightTexture

`SET_LIGHT_TEXTURE` · hash `0x55A50736` · **Cliente**

```lua
SetLightTexture(textureDict, textureHash)
```
```c
void SET_LIGHT_TEXTURE(char* textureDict, int textureHash);
```

**Parámetros**

- `textureDict` (`char*`): The name of the texture dictionary (TXD) containing the texture
- `textureHash` (`int`): Hash of the texture

**Devuelve:** `void`

**Descripción oficial:**

Assign a texture to an existing light source, allowing custom light shapes or patterns using textures from streaming assets.

---
### SetLightType

`SET_LIGHT_TYPE` · hash `0xCB58679D` · **Cliente**

```lua
SetLightType(lightType)
```
```c
void SET_LIGHT_TYPE(int lightType);
```

**Parámetros**

- `lightType` (`int`): The type of light

**Devuelve:** `void`

**Descripción oficial:**

Change the light type of a already created light.
Certain light type needs more configurations to work properly (Like direction, flags or size)

---
### SetLightVolumeDetails

`SET_LIGHT_VOLUME_DETAILS` · hash `0x2F731AE7` · **Cliente**

```lua
SetLightVolumeDetails(volIntensity, volSizeScale, r, g, b, i, outerExponent)
```
```c
void SET_LIGHT_VOLUME_DETAILS(float volIntensity, float volSizeScale, float r, float g, float b, float i, float outerExponent);
```

**Parámetros**

- `volIntensity` (`float`): Intensity of the volumetric effect
- `volSizeScale` (`float`): Scale of the volumetric volume
- `r` (`float`): Red channel for volumetric outer color (0–255)
- `g` (`float`): Green channel for volumetric outer color (0–255)
- `b` (`float`): Blue channel for volumetric outer color (0–255)
- `i` (`float`): Intensity (alpha) of the volumetric outer color
- `outerExponent` (`float`): Exponent controlling falloff of the volumetric outer glow

**Devuelve:** `void`

**Descripción oficial:**

Set volumetric light properties for an existing light, enabling custom volumetric effects such as fog-like glow.

---
### SetLightVolumetricFadeDistance

`SET_LIGHT_VOLUMETRIC_FADE_DISTANCE` · hash `0xE1F41605` · **Cliente**

```lua
SetLightVolumetricFadeDistance(volumetricFadeDistance)
```
```c
void SET_LIGHT_VOLUMETRIC_FADE_DISTANCE(int volumetricFadeDistance);
```

**Parámetros**

- `volumetricFadeDistance` (`int`): The maximum distance

**Devuelve:** `void`

**Descripción oficial:**

Set the fade distance for volumetric lightingn.

---
### SetManualShutdownLoadingScreenNui

`SET_MANUAL_SHUTDOWN_LOADING_SCREEN_NUI` · hash `0x1722C938` · **Cliente**

```lua
SetManualShutdownLoadingScreenNui(manualShutdown)
```
```c
void SET_MANUAL_SHUTDOWN_LOADING_SCREEN_NUI(BOOL manualShutdown);
```

**Parámetros**

- `manualShutdown` (`BOOL`): TRUE to manually shut down the loading screen NUI.

**Devuelve:** `void`

**Descripción oficial:**

**Note**: This native is deprecated and doesn't work anymore. Use [loadscreen_manual_shutdown](https://docs.fivem.net/docs/scripting-reference/resource-manifest/#loadscreen_manual_shutdown) in the fxmanifest.lua instead.

---
### SetMapZoomDataLevel

`SET_MAP_ZOOM_DATA_LEVEL` · hash `0x447C718E` · **Cliente**

```lua
SetMapZoomDataLevel(index, zoomScale, zoomSpeed, scrollSpeed, tilesX, tilesY)
```
```c
void SET_MAP_ZOOM_DATA_LEVEL(int index, float zoomScale, float zoomSpeed, float scrollSpeed, float tilesX, float tilesY);
```

**Parámetros**

- `index` (`int`): Zoom level index.
- `zoomScale` (`float`): fZoomScale value.
- `zoomSpeed` (`float`): fZoomSpeed value.
- `scrollSpeed` (`float`): fScrollSpeed value.
- `tilesX` (`float`): vTiles X.
- `tilesY` (`float`): vTiles Y.

**Devuelve:** `void`

**Descripción oficial:**

Sets values to the zoom level data by index.

---
### SetMillisecondsPerGameMinute

`SET_MILLISECONDS_PER_GAME_MINUTE` · hash `0x36CA2554` · **Cliente**

```lua
SetMillisecondsPerGameMinute(value)
```
```c
void SET_MILLISECONDS_PER_GAME_MINUTE(int value);
```

**Parámetros**

- `value` (`int`): Milliseconds.

**Devuelve:** `void`

**Descripción oficial:**

Overrides how many real ms are equal to one game minute.
A setter for [`GetMillisecondsPerGameMinute`](../gta5/CLOCK.md#getmillisecondspergameminute).

---
### SetMinimapClipType

`SET_MINIMAP_CLIP_TYPE` · hash `0xB8B4490C` · **Cliente**

```lua
SetMinimapClipType(type)
```
```c
void SET_MINIMAP_CLIP_TYPE(int type);
```

**Parámetros**

- `type` (`int`): 0 for rectangular, 1 for rounded.

**Devuelve:** `void`

**Descripción oficial:**

Sets the type for the minimap blip clipping object to be either rectangular or rounded.

---
### SetMinimapComponentPosition

`SET_MINIMAP_COMPONENT_POSITION` · hash `0x3E882B23` · **Cliente**

```lua
SetMinimapComponentPosition(name, alignX, alignY, posX, posY, sizeX, sizeY)
```
```c
void SET_MINIMAP_COMPONENT_POSITION(char* name, char* alignX, char* alignY, float posX, float posY, float sizeX, float sizeY);
```

**Parámetros**

- `name` (`char*`): The name of the minimap component to override.
- `alignX` (`char*`): Equivalent to the `alignX` field in `frontend.xml`.
- `alignY` (`char*`): Equivalent to the `alignY` field in `frontend.xml`.
- `posX` (`float`): Equivalent to the `posX` field in `frontend.xml`.
- `posY` (`float`): Equivalent to the `posY` field in `frontend.xml`.
- `sizeX` (`float`): Equivalent to the `sizeX` field in `frontend.xml`.
- `sizeY` (`float`): Equivalent to the `sizeY` field in `frontend.xml`.

**Devuelve:** `void`

**Descripción oficial:**

Overrides the minimap component data (from `common:/data/ui/frontend.xml`) for a specified component.

---
### SetMinimapOverlayDisplay

`SET_MINIMAP_OVERLAY_DISPLAY` · hash `0x6A48B3CA` · **Cliente**

```lua
SetMinimapOverlayDisplay(miniMap, x, y, xScale, yScale, alpha)
```
```c
void SET_MINIMAP_OVERLAY_DISPLAY(int miniMap, float x, float y, float xScale, float yScale, float alpha);
```

**Parámetros**

- `miniMap` (`int`): The minimap overlay ID.
- `x` (`float`): The X position for the overlay. This is equivalent to a game coordinate X.
- `y` (`float`): The Y position for the overlay. This is equivalent to a game coordinate Y, except that it's inverted (gfxY = -gameY).
- `xScale` (`float`): The X scale for the overlay. This is equivalent to the Flash \_xscale property, therefore 100 = 100%.
- `yScale` (`float`): The Y scale for the overlay. This is equivalent to the Flash \_yscale property.
- `alpha` (`float`): The alpha value for the overlay. This is equivalent to the Flash \_alpha property, therefore 100 = 100%.

**Devuelve:** `void`

**Descripción oficial:**

Sets the display info for a minimap overlay.

---
### SetModelHeadlightConfiguration

`SET_MODEL_HEADLIGHT_CONFIGURATION` · hash `0x7F6B8D75` · **Cliente**

```lua
SetModelHeadlightConfiguration(modelHash, ratePerSecond, headlightRotation, invertRotation)
```
```c
void SET_MODEL_HEADLIGHT_CONFIGURATION(Hash modelHash, float ratePerSecond, float headlightRotation, BOOL invertRotation);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ratePerSecond` (`float`)
- `headlightRotation` (`float`)
- `invertRotation` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native is deprecated and does nothing!**

---
### SetMpGamerTagsUseVehicleBehavior

`SET_MP_GAMER_TAGS_USE_VEHICLE_BEHAVIOR` · hash `0x7A27BC93` · **Cliente**

```lua
SetMpGamerTagsUseVehicleBehavior(enabled)
```
```c
void SET_MP_GAMER_TAGS_USE_VEHICLE_BEHAVIOR(bool enabled);
```

**Parámetros**

- `enabled` (`bool`): Whether tags should use normal game behavior. Default is true.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether all tags should group (normal game behavior) or should remain independent and above each ped's respective head when in a vehicle.

---
### SetMpGamerTagsVisibleDistance

`SET_MP_GAMER_TAGS_VISIBLE_DISTANCE` · hash `0xD61676B3` · **Cliente**

```lua
SetMpGamerTagsVisibleDistance(distance)
```
```c
void SET_MP_GAMER_TAGS_VISIBLE_DISTANCE(float distance);
```

**Parámetros**

- `distance` (`float`): The visible distance. Default is 100.0f.

**Devuelve:** `void`

**Descripción oficial:**

Sets the maximum distance at which all tags will be visible and which beyond will not be displayed. Distance is measured from the camera position.

---
### SetNuiFocus

`SET_NUI_FOCUS` · hash `0x5B98AE30` · **Cliente**

```lua
SetNuiFocus(hasFocus, hasCursor)
```
```c
void SET_NUI_FOCUS(BOOL hasFocus, BOOL hasCursor);
```

**Parámetros**

- `hasFocus` (`BOOL`)
- `hasCursor` (`BOOL`)

**Devuelve:** `void`

---
### SetNuiFocusKeepInput

`SET_NUI_FOCUS_KEEP_INPUT` · hash `0x3FF5E5F8` · **Cliente**

```lua
SetNuiFocusKeepInput(keepInput)
```
```c
void SET_NUI_FOCUS_KEEP_INPUT(BOOL keepInput);
```

**Parámetros**

- `keepInput` (`BOOL`)

**Devuelve:** `void`

---
### SetNuiZindex

`SET_NUI_ZINDEX` · hash `0x3734AAFF` · **Cliente**

```lua
SetNuiZindex(zIndex)
```
```c
void SET_NUI_ZINDEX(int zIndex);
```

**Parámetros**

- `zIndex` (`int`): New z-index value.

**Devuelve:** `void`

**Descripción oficial:**

Set the z-index of the NUI resource.

---
### SetPedCollectionComponentVariation

`SET_PED_COLLECTION_COMPONENT_VARIATION` · hash `0x88711BBA` · **Cliente**

```lua
SetPedCollectionComponentVariation(ped, componentId, collection, drawableId, textureId, paletteId)
```
```c
void SET_PED_COLLECTION_COMPONENT_VARIATION(Ped ped, int componentId, char* collection, int drawableId, int textureId, int paletteId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `drawableId` (`int`): Local drawable Id inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_COLLECTION_TEXTURE_VARIATIONS](#getnumberofpedcollectiontexturevariations).
- `paletteId` (`int`): 0 to 3.

**Devuelve:** `void`

**Descripción oficial:**

An alternative to [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation) that uses local collection indexing instead of the global one.

The local / collection relative indexing is useful because the global index may get shifted after Title Update. While local index will remain the same which simplifies migration to the newer game version.

Collection name and local index inside the collection can be obtained from the global index using [GET_PED_COLLECTION_NAME_FROM_DRAWABLE](#getpedcollectionnamefromdrawable) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE](#getpedcollectionlocalindexfromdrawable) natives.

---
### SetPedCollectionPreloadPropData

`SET_PED_COLLECTION_PRELOAD_PROP_DATA` · hash `0x14B5BBE0` · **Cliente**

```lua
SetPedCollectionPreloadPropData(ped, anchorPoint, collection, propIndex, textureId)
```
```c
void SET_PED_COLLECTION_PRELOAD_PROP_DATA(Ped ped, int anchorPoint, char* collection, int propIndex, int textureId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `propIndex` (`int`): Local prop index inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_PROP_DRAWABLE_VARIATIONS](#getnumberofpedcollectionpropdrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_COLLECTION_PROP_TEXTURE_VARIATIONS](#getnumberofpedcollectionproptexturevariations).

**Devuelve:** `void`

**Descripción oficial:**

An alternative to [SET_PED_PRELOAD_PROP_DATA](../gta5/PED-1.md#setpedpreloadpropdata) that uses local collection indexing instead of the global one.

The local / collection relative indexing is useful because the global index may get shifted after Title Update. While local index will remain the same which simplifies migration to the newer game version.

Collection name and local index inside the collection can be obtained from the global index using [GET_PED_COLLECTION_NAME_FROM_PROP](#getpedcollectionnamefromprop) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_PROP](#getpedcollectionlocalindexfromprop) natives.

---
### SetPedCollectionPreloadVariationData

`SET_PED_COLLECTION_PRELOAD_VARIATION_DATA` · hash `0x3EC75558` · **Cliente**

```lua
SetPedCollectionPreloadVariationData(ped, componentId, collection, drawableId, textureId)
```
```c
void SET_PED_COLLECTION_PRELOAD_VARIATION_DATA(Ped ped, int componentId, char* collection, int drawableId, int textureId);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `componentId` (`int`): One of the components from [SET_PED_COMPONENT_VARIATION](servidor.md#setpedcomponentvariation)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `drawableId` (`int`): Local drawable Id inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_DRAWABLE_VARIATIONS](#getnumberofpedcollectiondrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_COLLECTION_TEXTURE_VARIATIONS](#getnumberofpedcollectiontexturevariations).

**Devuelve:** `void`

**Descripción oficial:**

An alternative to [SET_PED_PRELOAD_VARIATION_DATA](../gta5/PED-1.md#setpedpreloadvariationdata) that uses local collection indexing instead of the global one.

The local / collection relative indexing is useful because the global index may get shifted after Title Update. While local index will remain the same which simplifies migration to the newer game version.

Collection name and local index inside the collection can be obtained from the global index using [GET_PED_COLLECTION_NAME_FROM_DRAWABLE](#getpedcollectionnamefromdrawable) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_DRAWABLE](#getpedcollectionlocalindexfromdrawable) natives.

---
### SetPedCollectionPropIndex

`SET_PED_COLLECTION_PROP_INDEX` · hash `0x75240BCB` · **Cliente**

```lua
SetPedCollectionPropIndex(ped, anchorPoint, collection, propIndex, textureId, attach)
```
```c
void SET_PED_COLLECTION_PROP_INDEX(Ped ped, int anchorPoint, char* collection, int propIndex, int textureId, BOOL attach);
```

**Parámetros**

- `ped` (`Ped`): The target ped
- `anchorPoint` (`int`): One of the anchor points from [SET_PED_PROP_INDEX](servidor.md#setpedpropindex)
- `collection` (`char*`): Name of the collection. Empty string for the base game collection. See [GET_PED_COLLECTION_NAME](#getpedcollectionname) in order to list all available collections.
- `propIndex` (`int`): Local prop index inside the given collection. Refer to [GET_NUMBER_OF_PED_COLLECTION_PROP_DRAWABLE_VARIATIONS](#getnumberofpedcollectionpropdrawablevariations).
- `textureId` (`int`): The texture id of the drawable. Refer to [GET_NUMBER_OF_PED_COLLECTION_PROP_TEXTURE_VARIATIONS](#getnumberofpedcollectionproptexturevariations).
- `attach` (`BOOL`): Attached or not.

**Devuelve:** `void`

**Descripción oficial:**

An alternative to [SET_PED_PROP_INDEX](servidor.md#setpedpropindex) that uses local collection indexing instead of the global one.

The local / collection relative indexing is useful because the global index may get shifted after Title Update. While local index will remain the same which simplifies migration to the newer game version.

Collection name and local index inside the collection can be obtained from the global index using [GET_PED_COLLECTION_NAME_FROM_PROP](#getpedcollectionnamefromprop) and [GET_PED_COLLECTION_LOCAL_INDEX_FROM_PROP](#getpedcollectionlocalindexfromprop) natives.

---
### SetPedMeleeCombatLimits

`SET_PED_MELEE_COMBAT_LIMITS` · hash `0x8E51EC29` · **Cliente**

```lua
SetPedMeleeCombatLimits(primaryCount, secondaryCount, populationPedCount)
```
```c
void SET_PED_MELEE_COMBAT_LIMITS(int primaryCount, int secondaryCount, int populationPedCount);
```

**Parámetros**

- `primaryCount` (`int`): The number of peds that engage in combat (default: 1)
- `secondaryCount` (`int`): The number of peds that engage in taunting (default: 3)
- `populationPedCount` (`int`): The maximum number of population peds (ambient and scenario) that can engage in combat (default: 3)

**Devuelve:** `void`

**Descripción oficial:**

Override the limits on the number and types of melee combatants. The game is limited to at most ten combatants among the three types: primary, secondary, and observers.

This native infers the number of observers based on the primary and secondary counts.

---
### SetPedModelHealthConfig

`SET_PED_MODEL_HEALTH_CONFIG` · hash `0xAF12A05D` · **Cliente**

```lua
SetPedModelHealthConfig(modelHash, configName)
```
```c
void SET_PED_MODEL_HEALTH_CONFIG(Hash modelHash, char* configName);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Ped's model.
- `configName` (`char*`): Name of health config.

**Devuelve:** `void`

**Descripción oficial:**

Sets a ped model's health config.
Takes effect only after setting player model with `SET_PLAYER_MODEL`.

**Ejemplo (lua):**

```lua
local pedModel = `mp_f_freemode_01`
SetPedModelHealthConfig(pedModel, "Strong")

SetPlayerModel(PlayerId(), pedModel)
SetPedDefaultComponentVariation(PlayerPedId())
```

---
### SetPedModelPersonality

`SET_PED_MODEL_PERSONALITY` · hash `0x46F6B38B` · **Cliente**

```lua
SetPedModelPersonality(modelHash, personalityHash)
```
```c
void SET_PED_MODEL_PERSONALITY(Hash modelHash, Hash personalityHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Ped's model.
- `personalityHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Personality hash.

**Devuelve:** `void`

**Descripción oficial:**

Overrides a ped model personality type.

---
### SetPedTurningThresholds

`SET_PED_TURNING_THRESHOLDS` · hash `0xB300F03` · **Cliente**

```lua
SetPedTurningThresholds(min, max)
```
```c
void SET_PED_TURNING_THRESHOLDS(float min, float max);
```

**Parámetros**

- `min` (`float`): Leftside angle on the above diagram
- `max` (`float`): Rightside angle on the above diagram

**Devuelve:** `void`

**Descripción oficial:**

Purpose: The game's default values for these make shooting while traveling Left quite a bit slower than shooting while traveling right (This could be a game-balance thing?)

Default Min: -45 Degrees
Default Max: 135 Degrees

```
   \ ,- ~ ||~ - ,
, ' \    x   x    ' ,
```

,      \    x    x   x  ,
,         \  x     x      ,
,            \     x    x  ,
,              \      x    ,
,                \   x     ,
,                 \   x x ,
,                  \  x ,
,                 , '
' - , \_ \_ \_ ,  '  \\

If the transition angle is within the shaded portion (x), there will be no transition(Quicker)
The angle corresponds to where you are looking(North on the circle) vs. the heading of your Ped.
Note: For some reason,

You can set these values to whatever you'd like with this native, but keep in mind that the transitional spin is only clockwise for some reason.

I'd personally recommend something like -135/135

---
### SetPlayerKillFallHeight

`SET_PLAYER_KILL_FALL_HEIGHT` · hash `0x86BD5722` · **Cliente**

```lua
SetPlayerKillFallHeight(height)
```
```c
void SET_PLAYER_KILL_FALL_HEIGHT(float height);
```

**Parámetros**

- `height` (`float`): height from which the player peds will instantly die from fall damage. Default value is `15.0`.

**Devuelve:** `void`

**Descripción oficial:**

A setter for [GET_PLAYER_KILL_FALL_HEIGHT](https://docs.fivem.net/natives/?_0x13BC2C63).

---
### SetPlayerMaxStamina

`SET_PLAYER_MAX_STAMINA` · hash `0x35594F67` · **Cliente**

```lua
local retval = SetPlayerMaxStamina(playerId, maxStamina)
```
```c
bool SET_PLAYER_MAX_STAMINA(Player playerId, float maxStamina);
```

**Parámetros**

- `playerId` (`Player`): The player index
- `maxStamina` (`float`): The value you want to set

**Devuelve:** `bool` — Did you manage to set the value.

---
### SetPlayerStamina

`SET_PLAYER_STAMINA` · hash `0xA9EC16C7` · **Cliente**

```lua
local retval = SetPlayerStamina(playerId, stamina)
```
```c
bool SET_PLAYER_STAMINA(Player playerId, float stamina);
```

**Parámetros**

- `playerId` (`Player`): The player index
- `stamina` (`float`): The value you want to set

**Devuelve:** `bool` — Did you manage to set the value.

---
### SetPlayerTalkingOverride

`SET_PLAYER_TALKING_OVERRIDE` · hash `0xFC02CAF6` · **Cliente**

```lua
SetPlayerTalkingOverride(player, state)
```
```c
void SET_PLAYER_TALKING_OVERRIDE(Player player, BOOL state);
```

**Parámetros**

- `player` (`Player`): The target player.
- `state` (`BOOL`): Overriding state.

**Devuelve:** `void`

**Descripción oficial:**

the status of default voip system. It affects on `NETWORK_IS_PLAYER_TALKING` and `mp_facial` animation.
This function doesn't need to be called every frame, it works like a switcher.

---
### SetReactionToVehicleSirenDisabled

`SET_REACTION_TO_VEHICLE_SIREN_DISABLED` · hash `0x8C3EC64F` · **Cliente**

```lua
SetReactionToVehicleSirenDisabled(state)
```
```c
void SET_REACTION_TO_VEHICLE_SIREN_DISABLED(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): Toggle on or off.

**Devuelve:** `void`

**Descripción oficial:**

This completely disables pedestrian vehicles from reacting to sirens. They will not try to do any maneuver to evade.

**Nombres antiguos (alias):** `SET_REACTION_TO_VEHICLE_WITH_SIREN_DISABLED` (`SetReactionToVehicleWithSirenDisabled`)

---
### SetRichPresence

`SET_RICH_PRESENCE` · hash `0x7BDCBD45` · **Cliente**

```lua
SetRichPresence(presenceState)
```
```c
void SET_RICH_PRESENCE(char* presenceState);
```

**Parámetros**

- `presenceState` (`char*`): The rich presence string to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets the player's rich presence detail state for social platform providers to a specified string.

---
### SetRopeLengthChangeRate

`SET_ROPE_LENGTH_CHANGE_RATE` · hash `0x69B680A7` · **Cliente**

```lua
SetRopeLengthChangeRate(rope, lengthChangeRate)
```
```c
void SET_ROPE_LENGTH_CHANGE_RATE(int rope, float lengthChangeRate);
```

**Parámetros**

- `rope` (`int`): The rope to set the length change rate for.
- `lengthChangeRate` (`float`): The rope's new length change rate.

**Devuelve:** `void`

**Descripción oficial:**

Set's the ropes length change rate, which is the speed that rope should wind if started.

---
### SetRopesCreateNetworkWorldState

`SET_ROPES_CREATE_NETWORK_WORLD_STATE` · hash `0xE62FC73` · **Cliente**

```lua
SetRopesCreateNetworkWorldState(shouldCreate)
```
```c
void SET_ROPES_CREATE_NETWORK_WORLD_STATE(BOOL shouldCreate);
```

**Parámetros**

- `shouldCreate` (`BOOL`): Whether to create an underlying network world state

**Devuelve:** `void`

**Descripción oficial:**

Toggles whether the usage of [ADD_ROPE](../gta5/PHYSICS.md#addrope) should create an underlying CNetworkRopeWorldStateData. By default this is set to false.

---
### SetRuntimeTextureArgbData

`SET_RUNTIME_TEXTURE_ARGB_DATA` · hash `0x3963D527` · **Cliente**

```lua
local retval = SetRuntimeTextureArgbData(tex, buffer, length)
```
```c
BOOL SET_RUNTIME_TEXTURE_ARGB_DATA(long tex, char* buffer, int length);
```

**Parámetros**

- `tex` (`long`)
- `buffer` (`char*`)
- `length` (`int`)

**Devuelve:** `BOOL`

---
### SetRuntimeTextureImage

`SET_RUNTIME_TEXTURE_IMAGE` · hash `0x28FC4ECB` · **Cliente**

```lua
local retval = SetRuntimeTextureImage(tex, fileName)
```
```c
BOOL SET_RUNTIME_TEXTURE_IMAGE(long tex, char* fileName);
```

**Parámetros**

- `tex` (`long`): A runtime texture handle.
- `fileName` (`char*`): The file name of an image to load, or a base64 "data:" URL. This should preferably be a PNG, and has to be specified as a `file` in the resource manifest.

**Devuelve:** `BOOL` — TRUE for success, FALSE for failure.

**Descripción oficial:**

Replaces the pixel data in a runtime texture with the image data from a file in the current resource, or a data URL.

If the bitmap is a different size compared to the existing texture, it will be resampled.

This command may end up executed asynchronously, and only update the texture data at a later time.

---
### SetRuntimeTexturePixel

`SET_RUNTIME_TEXTURE_PIXEL` · hash `0xAB65ACEE` · **Cliente**

```lua
SetRuntimeTexturePixel(tex, x, y, r, g, b, a)
```
```c
void SET_RUNTIME_TEXTURE_PIXEL(long tex, int x, int y, int r, int g, int b, int a);
```

**Parámetros**

- `tex` (`long`): A handle to the runtime texture.
- `x` (`int`): The X position of the pixel to change.
- `y` (`int`): The Y position of the pixel to change.
- `r` (`int`): The new R value (0-255).
- `g` (`int`): The new G value (0-255).
- `b` (`int`): The new B value (0-255).
- `a` (`int`): The new A value (0-255).

**Devuelve:** `void`

**Descripción oficial:**

Sets a pixel in the specified runtime texture. This will have to be committed using `COMMIT_RUNTIME_TEXTURE` to have any effect.

---
### SetSnakeoilForEntry

`SET_SNAKEOIL_FOR_ENTRY` · hash `0xA7DD3209` · **Cliente**

```lua
SetSnakeoilForEntry(name, path, data)
```
```c
void SET_SNAKEOIL_FOR_ENTRY(char* name, char* path, char* data);
```

**Parámetros**

- `name` (`char*`)
- `path` (`char*`)
- `data` (`char*`)

**Devuelve:** `void`

---
### SetTextChatEnabled

`SET_TEXT_CHAT_ENABLED` · hash `0x97B2F9F8` · **Cliente**

```lua
local retval = SetTextChatEnabled(enabled)
```
```c
BOOL SET_TEXT_CHAT_ENABLED(BOOL enabled);
```

**Parámetros**

- `enabled` (`BOOL`)

**Devuelve:** `BOOL`

---
### SetTimecycleModifierVar

`SET_TIMECYCLE_MODIFIER_VAR` · hash `0x6E0A422B` · **Cliente**

```lua
SetTimecycleModifierVar(modifierName, varName, value1, value2)
```
```c
void SET_TIMECYCLE_MODIFIER_VAR(char* modifierName, char* varName, float value1, float value2);
```

**Parámetros**

- `modifierName` (`char*`): The name of timecycle modifier.
- `varName` (`char*`): The name of timecycle variable.
- `value1` (`float`): The first value of variable.
- `value2` (`float`): The second value of variable.

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local modifierName = "superDARK"
local varName = "postfx_noise"

if DoesTimecycleModifierHasVar(modifierName, varName) then
  local success, value1, value2 = GetTimecycleModifierVar(modifierName, varName)

  if success then
    print(string.format("[%s] removed var %s with values: %f %f", modifierName, varName, value1, value2))
    RemoveTimecycleModifierVar(modifierName, varName)
  end
else
    SetTimecycleModifierVar(modifierName, varName, 1.0, 1.0)
    print(string.format("[%s] created var %s", modifierName, varName))
end
```

---
### SetTrackBrakingDistance

`SET_TRACK_BRAKING_DISTANCE` · hash `0x77EB78D0` · **Cliente**

```lua
SetTrackBrakingDistance(track, brakingDistance)
```
```c
void SET_TRACK_BRAKING_DISTANCE(int track, float brakingDistance);
```

**Parámetros**

- `track` (`int`): The track id (between 0 - 27)
- `brakingDistance` (`float`): The new braking distance

**Devuelve:** `void`

**Descripción oficial:**

Sets the braking distance of the track. Used by trains to determine the point to slow down when entering a station.

---
### SetTrackEnabled

`SET_TRACK_ENABLED` · hash `0x4B41E84C` · **Cliente**

```lua
SetTrackEnabled(track, enabled)
```
```c
void SET_TRACK_ENABLED(int track, bool enabled);
```

**Parámetros**

- `track` (`int`): The track id (between 0 - 27)
- `enabled` (`bool`): Should this track be enabled

**Devuelve:** `void`

**Descripción oficial:**

Toggles the track being active. If disabled mission trains will not be able to spawn on this track and will look for the next closest track to spawn

---
### SetTrackJunctionActive

`SET_TRACK_JUNCTION_ACTIVE` · hash `0x537B449D` · **Cliente**

```lua
local retval = SetTrackJunctionActive(junctionIndex, state)
```
```c
bool SET_TRACK_JUNCTION_ACTIVE(int junctionIndex, bool state);
```

**Parámetros**

- `junctionIndex` (`int`): The junctions index
- `state` (`bool`): Toggles the state of the junction

**Devuelve:** `bool` — Returns if it succeeds setting the junctions state or not

**Descripción oficial:**

Sets the state of a track junction.

---
### SetTrackMaxSpeed

`SET_TRACK_MAX_SPEED` · hash `0x37BFC732` · **Cliente**

```lua
SetTrackMaxSpeed(track, newSpeed)
```
```c
void SET_TRACK_MAX_SPEED(int track, int newSpeed);
```

**Parámetros**

- `track` (`int`): The track id (between 0 - 27)
- `newSpeed` (`int`): The tracks new speed

**Devuelve:** `void`

**Descripción oficial:**

Sets the max speed for the train tracks. Used by ambient trains and for station calculations

---
### SetTrainDoorOpenRatio

`SET_TRAIN_DOOR_OPEN_RATIO` · hash `0x2468DBE8` · **Cliente**

```lua
SetTrainDoorOpenRatio(train, doorIndex, ratio)
```
```c
void SET_TRAIN_DOOR_OPEN_RATIO(Vehicle train, int doorIndex, float ratio);
```

**Parámetros**

- `train` (`Vehicle`): The train to set the door ratio for.
- `doorIndex` (`int`): Zero-based door index.
- `ratio` (`float`): A value between 0.0 (fully closed) and 1.0 (fully open).

**Devuelve:** `void`

**Descripción oficial:**

Sets the ratio that a door is open for on a train.

**Ejemplo (lua):**

```lua
-- open all doors on a train
local doorCount = GetTrainDoorCount(train)
for doorIndex = 0, doorCount - 1 do
    SetTrainDoorOpenRatio(train, doorIndex, 1.0)
end
```

**Ejemplo (cs):**

```cs
// open all doors on a train
int doorCount = API.GetTrainDoorCount(train);
for (int doorIndex = 0; doorIndex < doorCount; doorIndex++)
{
    API.SetTrainDoorOpenRatio(train, doorIndex, 1.0f);
}
```

---
### SetTrainState

`SET_TRAIN_STATE` · hash `0x61CB74A0` · **Cliente**

```lua
SetTrainState(train, state)
```
```c
void SET_TRAIN_STATE(Vehicle train, int state);
```

**Parámetros**

- `train` (`Vehicle`): The train handle
- `state` (`int`): The trains new state

**Devuelve:** `void` — The trains current state, refer to [GET_TRAIN_STATE](compartidos.md#gettrainstate)

---
### SetTrainStopAtStations

`SET_TRAIN_STOP_AT_STATIONS` · hash `0xECB8B577` · **Cliente**

```lua
SetTrainStopAtStations(train, state)
```
```c
void SET_TRAIN_STOP_AT_STATIONS(Vehicle train, BOOL state);
```

**Parámetros**

- `train` (`Vehicle`): The train handle
- `state` (`BOOL`): True to make the train stop at stations. False to make the train not stop at stations

**Devuelve:** `void`

**Descripción oficial:**

Toggles a train's ability to stop at stations

---
### SetTrainsForceDoorsOpen

`SET_TRAINS_FORCE_DOORS_OPEN` · hash `0xD4D1BA63` · **Cliente**

```lua
SetTrainsForceDoorsOpen(forceOpen)
```
```c
void SET_TRAINS_FORCE_DOORS_OPEN(bool forceOpen);
```

**Parámetros**

- `forceOpen` (`bool`): Should force open.

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables whether train doors should be forced open whilst a player is inside the train. This is enabled by default in multiplayer.

---
### SetVehicleAlarmTimeLeft

`SET_VEHICLE_ALARM_TIME_LEFT` · hash `0xC108EE6F` · **Cliente**

```lua
SetVehicleAlarmTimeLeft(vehicle, time)
```
```c
void SET_VEHICLE_ALARM_TIME_LEFT(Vehicle vehicle, int time);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `time` (`int`)

**Devuelve:** `void`

---
### SetVehicleAutoRepairDisabled

`SET_VEHICLE_AUTO_REPAIR_DISABLED` · hash `0x5F3A3574` · **Cliente**

```lua
SetVehicleAutoRepairDisabled(vehicle, value)
```
```c
void SET_VEHICLE_AUTO_REPAIR_DISABLED(Vehicle vehicle, BOOL value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set disable auto vehicle repair.
- `value` (`BOOL`): Setting the value to  true prevents the vehicle from being repaired when a extra is enabled. Setting the value to false allows the vehicle from being repaired when a extra is enabled.

**Devuelve:** `void`

**Descripción oficial:**

Disables the vehicle from being repaired when a vehicle extra is enabled.

---
### SetVehicleClutch

`SET_VEHICLE_CLUTCH` · hash `0x2F70ACED` · **Cliente**

```lua
SetVehicleClutch(vehicle, clutch)
```
```c
void SET_VEHICLE_CLUTCH(Vehicle vehicle, float clutch);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `clutch` (`float`)

**Devuelve:** `void`

---
### SetVehicleCurrentGear

`SET_VEHICLE_CURRENT_GEAR` · hash `0x8923DD42` · **Cliente**

```lua
SetVehicleCurrentGear(vehicle, gear)
```
```c
void SET_VEHICLE_CURRENT_GEAR(Vehicle vehicle, int gear);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `gear` (`int`): The gear you want the vehicle to use.

**Devuelve:** `void`

---
### SetVehicleCurrentRpm

`SET_VEHICLE_CURRENT_RPM` · hash `0x2A01A8FC` · **Cliente**

```lua
SetVehicleCurrentRpm(vehicle, rpm)
```
```c
void SET_VEHICLE_CURRENT_RPM(Vehicle vehicle, float rpm);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `rpm` (`float`)

**Devuelve:** `void`

---
### SetVehicleEngineTemperature

`SET_VEHICLE_ENGINE_TEMPERATURE` · hash `0x6C93C4A9` · **Cliente**

```lua
SetVehicleEngineTemperature(vehicle, temperature)
```
```c
void SET_VEHICLE_ENGINE_TEMPERATURE(Vehicle vehicle, float temperature);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `temperature` (`float`)

**Devuelve:** `void`

---
### SetVehicleFlag

`SET_VEHICLE_FLAG` · hash `0x63AE1A34` · **Cliente**

```lua
local retval = SetVehicleFlag(vehicle, flagIndex, value)
```
```c
bool SET_VEHICLE_FLAG(Vehicle vehicle, int flagIndex, bool value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set flag for.
- `flagIndex` (`int`): Flag index.
- `value` (`bool`): `true` to enable the flag, `false` to disable it.

**Devuelve:** `bool`

**Descripción oficial:**

This native is a setter for [`GET_VEHICLE_HAS_FLAG`](#getvehiclehasflag).

---
### SetVehicleFuelLevel

`SET_VEHICLE_FUEL_LEVEL` · hash `0xBA970511` · **Cliente**

```lua
SetVehicleFuelLevel(vehicle, level)
```
```c
void SET_VEHICLE_FUEL_LEVEL(Vehicle vehicle, float level);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `level` (`float`)

**Devuelve:** `void`

---
### SetVehicleGearRatio

`SET_VEHICLE_GEAR_RATIO` · hash `0x496EF2F2` · **Cliente**

```lua
SetVehicleGearRatio(vehicle, gear, ratio)
```
```c
void SET_VEHICLE_GEAR_RATIO(Vehicle vehicle, int gear, float ratio);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `gear` (`int`): The vehicles gear you want to change.
- `ratio` (`float`): The gear ratio you want to use.

**Devuelve:** `void`

**Descripción oficial:**

Sets the vehicles gear ratio on choosen gear, reverse gear needs to be a negative float and forward moving gear needs to be a positive float. Refer to the examples if confused.

**Ejemplo (lua):**

```lua
local function Set8SpeedVehicleGears(Vehicle)
    SetVehicleGearRatio(Vehicle, 0, -3.32)  -- reverse gear at -3.21:1
    SetVehicleGearRatio(Vehicle, 1, 4.71)   -- 1st gear at 4.71:1
    SetVehicleGearRatio(Vehicle, 2, 3.14)   -- 2nd gear at 3.14:1
    SetVehicleGearRatio(Vehicle, 3, 2.11)   -- 3rd gear at 2.11:1
    SetVehicleGearRatio(Vehicle, 4, 1.67)   -- 4th gear at 1.67:1
    SetVehicleGearRatio(Vehicle, 5, 1.29)   -- 5th gear at 1.29:1
    SetVehicleGearRatio(Vehicle, 6, 1.0)    -- 6th gear at 1.0:1
    SetVehicleGearRatio(Vehicle, 7, 0.84)   -- 7th gear at 0.84:1
    SetVehicleGearRatio(Vehicle, 8, 0.67)   -- 8th gear at 0.67:1
end
```

**Ejemplo (js):**

```js
function Set8SpeedVehicleGears(Vehicle) {
    SetVehicleGearRatio(Vehicle, 0, -3.32);  // reverse gear at -3.21:1
    SetVehicleGearRatio(Vehicle, 1, 4.71);   // 1st gear at 4.71:1
    SetVehicleGearRatio(Vehicle, 2, 3.14);   // 2nd gear at 3.14:1
    SetVehicleGearRatio(Vehicle, 3, 2.11);   // 3rd gear at 2.11:1
    SetVehicleGearRatio(Vehicle, 4, 1.67);   // 4th gear at 1.67:1
    SetVehicleGearRatio(Vehicle, 5, 1.29);   // 5th gear at 1.29:1
    SetVehicleGearRatio(Vehicle, 6, 1.0);    // 6th gear at 1.0:1
    SetVehicleGearRatio(Vehicle, 7, 0.84);   // 7th gear at 0.84:1
    SetVehicleGearRatio(Vehicle, 8, 0.67);   // 8th gear at 0.67:1
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.API;

public static void Set8SpeedVehicleGears(int Vehicle)
{
    SetVehicleGearRatio(Vehicle, 0, -3.32);  // reverse gear at -3.21:1
    SetVehicleGearRatio(Vehicle, 1, 4.71);   // 1st gear at 4.71:1
    SetVehicleGearRatio(Vehicle, 2, 3.14);   // 2nd gear at 3.14:1
    SetVehicleGearRatio(Vehicle, 3, 2.11);   // 3rd gear at 2.11:1
    SetVehicleGearRatio(Vehicle, 4, 1.67);   // 4th gear at 1.67:1
    SetVehicleGearRatio(Vehicle, 5, 1.29);   // 5th gear at 1.29:1
    SetVehicleGearRatio(Vehicle, 6, 1.0);    // 6th gear at 1.0:1
    SetVehicleGearRatio(Vehicle, 7, 0.84);   // 7th gear at 0.84:1
    SetVehicleGearRatio(Vehicle, 8, 0.67);   // 8th gear at 0.67:1
}
```

---
### SetVehicleGravityAmount

`SET_VEHICLE_GRAVITY_AMOUNT` · hash `0x1A963E58` · **Cliente**

```lua
SetVehicleGravityAmount(vehicle, gravity)
```
```c
void SET_VEHICLE_GRAVITY_AMOUNT(Vehicle vehicle, float gravity);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `gravity` (`float`)

**Devuelve:** `void`

---
### SetVehicleHandlingField

`SET_VEHICLE_HANDLING_FIELD` · hash `0x2BA40795` · **Cliente**

```lua
SetVehicleHandlingField(vehicle, class_, fieldName, value)
```
```c
void SET_VEHICLE_HANDLING_FIELD(Vehicle vehicle, char* class_, char* fieldName, Any value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`Any`): The value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a handling override for a specific vehicle. Certain handling flags can only be set globally using `SET_HANDLING_FIELD`, this might require some experimentation.
Example: `SetVehicleHandlingField(vehicle, 'CHandlingData', 'fSteeringLock', 360.0)`

---
### SetVehicleHandlingFloat

`SET_VEHICLE_HANDLING_FLOAT` · hash `0x488C86D2` · **Cliente**

```lua
SetVehicleHandlingFloat(vehicle, class_, fieldName, value)
```
```c
void SET_VEHICLE_HANDLING_FLOAT(Vehicle vehicle, char* class_, char* fieldName, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`float`): The floating-point value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a handling override for a specific vehicle. Certain handling flags can only be set globally using `SET_HANDLING_FLOAT`, this might require some experimentation.
Example: `SetVehicleHandlingFloat(vehicle, 'CHandlingData', 'fSteeringLock', 360.0)`

---
### SetVehicleHandlingInt

`SET_VEHICLE_HANDLING_INT` · hash `0xC37F4CF9` · **Cliente**

```lua
SetVehicleHandlingInt(vehicle, class_, fieldName, value)
```
```c
void SET_VEHICLE_HANDLING_INT(Vehicle vehicle, char* class_, char* fieldName, int value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`int`): The integer value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a handling override for a specific vehicle. Certain handling flags can only be set globally using `SET_HANDLING_INT`, this might require some experimentation.

---
### SetVehicleHandlingVector

`SET_VEHICLE_HANDLING_VECTOR` · hash `0x12497890` · **Cliente**

```lua
SetVehicleHandlingVector(vehicle, class_, fieldName, value)
```
```c
void SET_VEHICLE_HANDLING_VECTOR(Vehicle vehicle, char* class_, char* fieldName, Vector3 value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set data for.
- `class_` (`char*`): The handling class to set. Only "CHandlingData" is supported at this time.
- `fieldName` (`char*`): The field name to set. These match the keys in `handling.meta`.
- `value` (`Vector3`): The Vector3 value to set.

**Devuelve:** `void`

**Descripción oficial:**

Sets a handling override for a specific vehicle. Certain handling flags can only be set globally using `SET_HANDLING_VECTOR`, this might require some experimentation.

---
### SetVehicleHighGear

`SET_VEHICLE_HIGH_GEAR` · hash `0x20B1B3E6` · **Cliente**

```lua
SetVehicleHighGear(vehicle, gear)
```
```c
void SET_VEHICLE_HIGH_GEAR(Vehicle vehicle, int gear);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `gear` (`int`)

**Devuelve:** `void`

---
### SetVehicleNextGear

`SET_VEHICLE_NEXT_GEAR` · hash `0x3A4566F4` · **Cliente**

```lua
SetVehicleNextGear(vehicle, nextGear)
```
```c
void SET_VEHICLE_NEXT_GEAR(Vehicle vehicle, int nextGear);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `nextGear` (`int`): The vehicles next gear.

**Devuelve:** `void`

---
### SetVehicleNitroPtfxRange

`SET_VEHICLE_NITRO_PTFX_RANGE` · hash `0xA40CB822` · **Cliente**

```lua
SetVehicleNitroPtfxRange(range)
```
```c
void SET_VEHICLE_NITRO_PTFX_RANGE(float range);
```

**Parámetros**

- `range` (`float`): The visible distance. Default is 50.0f.

**Devuelve:** `void`

**Descripción oficial:**

Sets the maximum distance in which [\_SET_VEHICLE_NITRO_ENABLED](../gta5/VEHICLE-2.md#setoverridenitrouslevel) PTFX are rendered. Distance is measured from the camera position.

---
### SetVehicleOilLevel

`SET_VEHICLE_OIL_LEVEL` · hash `0x90D1CAD1` · **Cliente**

```lua
SetVehicleOilLevel(vehicle, level)
```
```c
void SET_VEHICLE_OIL_LEVEL(Vehicle vehicle, float level);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `level` (`float`)

**Devuelve:** `void`

---
### SetVehiclePitchBias

`SET_VEHICLE_PITCH_BIAS` · hash `0x2A6CC9F2` · **Cliente**

```lua
SetVehiclePitchBias(vehicle, value)
```
```c
void SET_VEHICLE_PITCH_BIAS(Vehicle vehicle, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`): Target vehicle.
- `value` (`float`): Pitch bias value.

**Devuelve:** `void`

**Descripción oficial:**

Set the vehicle's pitch bias. Only works on planes.

---
### SetVehicleRollBias

`SET_VEHICLE_ROLL_BIAS` · hash `0x264B45DE` · **Cliente**

```lua
SetVehicleRollBias(vehicle, value)
```
```c
void SET_VEHICLE_ROLL_BIAS(Vehicle vehicle, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`): Target vehicle.
- `value` (`float`): Roll bias value.

**Devuelve:** `void`

**Descripción oficial:**

Set the vehicle's roll bias. Only works on planes.

---
### SetVehicleSteeringAngle

`SET_VEHICLE_STEERING_ANGLE` · hash `0xFFCCC2EA` · **Cliente**

```lua
SetVehicleSteeringAngle(vehicle, angle)
```
```c
void SET_VEHICLE_STEERING_ANGLE(Vehicle vehicle, float angle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `angle` (`float`)

**Devuelve:** `void`

---
### SetVehicleSteeringScale

`SET_VEHICLE_STEERING_SCALE` · hash `0xEB46596F` · **Cliente**

```lua
SetVehicleSteeringScale(vehicle, scale)
```
```c
void SET_VEHICLE_STEERING_SCALE(Vehicle vehicle, float scale);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `scale` (`float`)

**Devuelve:** `void`

---
### SetVehicleSuspensionHeight

`SET_VEHICLE_SUSPENSION_HEIGHT` · hash `0xB3439A01` · **Cliente**

```lua
SetVehicleSuspensionHeight(vehicle, newHeight)
```
```c
void SET_VEHICLE_SUSPENSION_HEIGHT(Vehicle vehicle, float newHeight);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `newHeight` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the height of the vehicle's suspension.
This changes the same value set by Suspension in the mod shop.
Negatives values raise the car. Positive values lower the car.

This is change is visual only. The collision of the vehicle will not move.

---
### SetVehicleTurboPressure

`SET_VEHICLE_TURBO_PRESSURE` · hash `0x6485615E` · **Cliente**

```lua
SetVehicleTurboPressure(vehicle, pressure)
```
```c
void SET_VEHICLE_TURBO_PRESSURE(Vehicle vehicle, float pressure);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `pressure` (`float`)

**Devuelve:** `void`

---
### SetVehicleWheelBrakePressure

`SET_VEHICLE_WHEEL_BRAKE_PRESSURE` · hash `0xE80F4E31` · **Cliente**

```lua
SetVehicleWheelBrakePressure(vehicle, wheelIndex, pressure)
```
```c
void SET_VEHICLE_WHEEL_BRAKE_PRESSURE(Vehicle vehicle, int wheelIndex, float pressure);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `pressure` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Sets brake pressure of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.
Normal values around 1.0f

---
### SetVehicleWheelFlags

`SET_VEHICLE_WHEEL_FLAGS` · hash `0xD2B9E90D` · **Cliente**

```lua
SetVehicleWheelFlags(vehicle, wheelIndex, flags)
```
```c
void SET_VEHICLE_WHEEL_FLAGS(Vehicle vehicle, int wheelIndex, int flags);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `flags` (`int`): bit flags

**Devuelve:** `void`

**Descripción oficial:**

Sets the flags of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### SetVehicleWheelHealth

`SET_VEHICLE_WHEEL_HEALTH` · hash `0xB22ECEFD` · **Cliente**

```lua
SetVehicleWheelHealth(vehicle, wheelIndex, health)
```
```c
void SET_VEHICLE_WHEEL_HEALTH(Vehicle vehicle, int wheelIndex, float health);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `health` (`float`)

**Devuelve:** `void`

---
### SetVehicleWheelIsPowered

`SET_VEHICLE_WHEEL_IS_POWERED` · hash `0xBD5291A0` · **Cliente**

```lua
SetVehicleWheelIsPowered(vehicle, wheelIndex, powered)
```
```c
void SET_VEHICLE_WHEEL_IS_POWERED(Vehicle vehicle, int wheelIndex, BOOL powered);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `powered` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets whether the wheel is powered.
On all wheel drive cars this works to change which wheels receive power, but if a car's fDriveBiasFront doesn't send power to that wheel, it won't get power anyway. This can be fixed by changing the fDriveBiasFront with SET_VEHICLE_HANDLING_FLOAT.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.
This is a shortcut to a flag in SET_VEHICLE_WHEEL_FLAGS.

**Ejemplo (lua):**

```lua
SetVehicleWheelIsPowered(vehicle, 0, true);
```

**Ejemplo (js):**

```js
SetVehicleWheelIsPowered(vehicle, 0, true);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.API;
// ...
// The elusive Left Wheel Drive
Vehicle veh = Game.PlayerPed.CurrentVehicle;
for(int i = 0; i < veh.Wheels.Count; i++){
    SetVehicleWheelIsPowered(veh.Handle, i, i % 2 == 0);
}
```

---
### SetVehicleWheelPower

`SET_VEHICLE_WHEEL_POWER` · hash `0xC6146043` · **Cliente**

```lua
SetVehicleWheelPower(vehicle, wheelIndex, power)
```
```c
void SET_VEHICLE_WHEEL_POWER(Vehicle vehicle, int wheelIndex, float power);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `power` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Sets power being sent to a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### SetVehicleWheelRimColliderSize

`SET_VEHICLE_WHEEL_RIM_COLLIDER_SIZE` · hash `0xF380E184` · **Cliente**

```lua
SetVehicleWheelRimColliderSize(vehicle, wheelIndex, value)
```
```c
void SET_VEHICLE_WHEEL_RIM_COLLIDER_SIZE(Vehicle vehicle, int wheelIndex, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `wheelIndex` (`int`): Index of wheel, 0-3.
- `value` (`float`): Size of rim collider.

**Devuelve:** `void`

**Descripción oficial:**

Not sure what this changes, probably determines physical rim size in case the tire is blown.

---
### SetVehicleWheelRotationSpeed

`SET_VEHICLE_WHEEL_ROTATION_SPEED` · hash `0x35ED100D` · **Cliente**

```lua
SetVehicleWheelRotationSpeed(vehicle, wheelIndex, speed)
```
```c
void SET_VEHICLE_WHEEL_ROTATION_SPEED(Vehicle vehicle, int wheelIndex, float speed);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `speed` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the rotation speed of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
### SetVehicleWheelSize

`SET_VEHICLE_WHEEL_SIZE` · hash `0x53AB5C35` · **Cliente**

```lua
local retval = SetVehicleWheelSize(vehicle, size)
```
```c
BOOL SET_VEHICLE_WHEEL_SIZE(Vehicle vehicle, float size);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set data for.
- `size` (`float`): Size of the wheels (usually between 0.5 and 1.5 is reasonable).

**Devuelve:** `BOOL` — Bool - whether change was successful or not

**Descripción oficial:**

Sets vehicle's wheels' size (size is the same for all the wheels, cannot get/set specific wheel of vehicle).
Only works on non-default wheels.
Returns whether change was successful (can be false if trying to set size for non-default wheels).

---
### SetVehicleWheelTireColliderSize

`SET_VEHICLE_WHEEL_TIRE_COLLIDER_SIZE` · hash `0xB962D05C` · **Cliente**

```lua
SetVehicleWheelTireColliderSize(vehicle, wheelIndex, value)
```
```c
void SET_VEHICLE_WHEEL_TIRE_COLLIDER_SIZE(Vehicle vehicle, int wheelIndex, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `wheelIndex` (`int`): Index of wheel, 0-3.
- `value` (`float`): Radius of tire collider.

**Devuelve:** `void`

**Descripción oficial:**

Use along with SetVehicleWheelSize to resize the wheels (this native sets the collider size affecting physics while SetVehicleWheelSize will change visual size).

---
### SetVehicleWheelTireColliderWidth

`SET_VEHICLE_WHEEL_TIRE_COLLIDER_WIDTH` · hash `0x47BD0270` · **Cliente**

```lua
SetVehicleWheelTireColliderWidth(vehicle, wheelIndex, value)
```
```c
void SET_VEHICLE_WHEEL_TIRE_COLLIDER_WIDTH(Vehicle vehicle, int wheelIndex, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to obtain data for.
- `wheelIndex` (`int`): Index of wheel, 0-3.
- `value` (`float`): Width of tire collider.

**Devuelve:** `void`

**Descripción oficial:**

Use along with SetVehicleWheelWidth to resize the wheels (this native sets the collider width affecting physics while SetVehicleWheelWidth will change visual width).

---
### SetVehicleWheelTractionVectorLength

`SET_VEHICLE_WHEEL_TRACTION_VECTOR_LENGTH` · hash `0x85C85A3A` · **Cliente**

```lua
SetVehicleWheelTractionVectorLength(vehicle, wheelIndex, length)
```
```c
void SET_VEHICLE_WHEEL_TRACTION_VECTOR_LENGTH(Vehicle vehicle, int wheelIndex, float length);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `length` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the traction vector length of a wheel.
Max number of wheels can be retrieved with the native GET_VEHICLE_NUMBER_OF_WHEELS.

---
