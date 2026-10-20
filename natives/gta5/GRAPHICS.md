# Natives de GTA V — GRAPHICS

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `GRAPHICS`: **392** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddDecal`](#adddecal) · [`AddEntityIcon`](#addentityicon) · [`AddOilDecal`](#addoildecal) · [`AddPetrolDecal`](#addpetroldecal) · [`AddPetrolTrailDecalInfo`](#addpetroltraildecalinfo) · [`AddTcmodifierOverride`](#addtcmodifieroverride) · [`AddVehicleCrewEmblem`](#addvehiclecrewemblem) · [`AdjustNextPosSizeAsNormalized_16_9`](#adjustnextpossizeasnormalized_16_9) · [`AnimpostfxGetUnk`](#animpostfxgetunk) · [`AnimpostfxIsRunning`](#animpostfxisrunning) · [`AnimpostfxPlay`](#animpostfxplay) · [`AnimpostfxStop`](#animpostfxstop) · [`AnimpostfxStopAll`](#animpostfxstopall) · [`AnimpostfxStopAndDoUnk`](#animpostfxstopanddounk) · [`AttachTvAudioToEntity`](#attachtvaudiotoentity) · [`BeginScaleformMovieMethod`](#beginscaleformmoviemethod) · [`BeginScaleformMovieMethodOnFrontend`](#beginscaleformmoviemethodonfrontend) · [`BeginScaleformMovieMethodOnFrontendHeader`](#beginscaleformmoviemethodonfrontendheader) · [`BeginScaleformScriptHudMovieMethod`](#beginscaleformscripthudmoviemethod) · [`BeginTakeHighQualityPhoto`](#begintakehighqualityphoto) · [`BeginTakeMissionCreatorPhoto`](#begintakemissioncreatorphoto) · [`BeginTextCommandScaleformString`](#begintextcommandscaleformstring) · [`CallScaleformMovieMethod`](#callscaleformmoviemethod) · [`CallScaleformMovieMethodWithNumber`](#callscaleformmoviemethodwithnumber) · [`CallScaleformMovieMethodWithNumberAndString`](#callscaleformmoviemethodwithnumberandstring) · [`CallScaleformMovieMethodWithString`](#callscaleformmoviemethodwithstring) · [`CascadeShadowsClearShadowSampleType`](#cascadeshadowsclearshadowsampletype) · [`CascadeShadowsEnableEntityTracker`](#cascadeshadowsenableentitytracker) · [`CascadeShadowsInitSession`](#cascadeshadowsinitsession) · [`CascadeShadowsSetAircraftMode`](#cascadeshadowssetaircraftmode) · [`CascadeShadowsSetCascadeBounds`](#cascadeshadowssetcascadebounds) · [`CascadeShadowsSetCascadeBoundsScale`](#cascadeshadowssetcascadeboundsscale) · [`CascadeShadowsSetDynamicDepthMode`](#cascadeshadowssetdynamicdepthmode) · [`CascadeShadowsSetDynamicDepthValue`](#cascadeshadowssetdynamicdepthvalue) · [`CascadeShadowsSetEntityTrackerScale`](#cascadeshadowssetentitytrackerscale) · [`CascadeShadowsSetShadowSampleType`](#cascadeshadowssetshadowsampletype) · [`ClearDrawOrigin`](#cleardraworigin) · [`ClearExtraTimecycleModifier`](#clearextratimecyclemodifier) · [`ClearTimecycleModifier`](#cleartimecyclemodifier) · [`ClearTvChannelPlaylist`](#cleartvchannelplaylist) · [`CreateCheckpoint`](#createcheckpoint) · [`CreateTrackedPoint`](#createtrackedpoint) · [`DeleteCheckpoint`](#deletecheckpoint) · [`DestroyTrackedPoint`](#destroytrackedpoint) · [`DisableMoonCycleOverride`](#disablemooncycleoverride) · [`DisableOcclusionThisFrame`](#disableocclusionthisframe) · [`DisableScreenblurFade`](#disablescreenblurfade) · [`DisableScriptAmbientEffects`](#disablescriptambienteffects) · [`DisableVehicleDistantlights`](#disablevehicledistantlights) · [`DoesLatestBriefStringExist`](#doeslatestbriefstringexist) · [`DoesParticleFxLoopedExist`](#doesparticlefxloopedexist) · [`DoesVehicleHaveCrewEmblem`](#doesvehiclehavecrewemblem) · [`DontRenderInGameUi`](#dontrenderingameui) · [`DrawBinkMovie`](#drawbinkmovie) · [`DrawBox`](#drawbox) · [`DrawDebugBox`](#drawdebugbox) · [`DrawDebugCross`](#drawdebugcross) · [`DrawDebugLine`](#drawdebugline) · [`DrawDebugLineWithTwoColours`](#drawdebuglinewithtwocolours) · [`DrawDebugSphere`](#drawdebugsphere) · [`DrawDebugText`](#drawdebugtext) · [`DrawDebugText_2d`](#drawdebugtext_2d) · [`DrawInteractiveSprite`](#drawinteractivesprite) · [`DrawLightWithRange`](#drawlightwithrange) · [`DrawLightWithRangeAndShadow`](#drawlightwithrangeandshadow) · [`DrawLine`](#drawline) · [`DrawLowQualityPhotoToPhone`](#drawlowqualityphototophone) · [`DrawMarker`](#drawmarker) · [`DrawMarker_2`](#drawmarker_2) · [`DrawPoly`](#drawpoly) · [`DrawRect`](#drawrect) · [`DrawScaleformMovie`](#drawscaleformmovie) · [`DrawScaleformMovieFullscreen`](#drawscaleformmoviefullscreen) · [`DrawScaleformMovieFullscreenMasked`](#drawscaleformmoviefullscreenmasked) · [`DrawScaleformMovie_3d`](#drawscaleformmovie_3d) · [`DrawScaleformMovie_3dSolid`](#drawscaleformmovie_3dsolid) · [`DrawShowroom`](#drawshowroom) · [`DrawSphere`](#drawsphere) · [`DrawSpotLight`](#drawspotlight) · [`DrawSpotLightWithShadow`](#drawspotlightwithshadow) · [`DrawSprite`](#drawsprite) · [`DrawSpritePoly_2`](#drawspritepoly_2) · [`DrawSpriteUv`](#drawspriteuv) · [`DrawTexturedPoly`](#drawtexturedpoly) · [`DrawTvChannel`](#drawtvchannel) · [`EnableAlienBloodVfx`](#enablealienbloodvfx) · [`EnableClownBloodVfx`](#enableclownbloodvfx) · [`EnableMoonCycleOverride`](#enablemooncycleoverride) · [`EnableMovieKeyframeWait`](#enablemoviekeyframewait) · [`EnableMovieSubtitles`](#enablemoviesubtitles) · [`EndPetrolTrailDecals`](#endpetroltraildecals) · [`EndScaleformMovieMethod`](#endscaleformmoviemethod) · [`EndScaleformMovieMethodReturnValue`](#endscaleformmoviemethodreturnvalue) · [`EndTextCommandScaleformString`](#endtextcommandscaleformstring) · [`EndTextCommandUnparsedScaleformString`](#endtextcommandunparsedscaleformstring) · [`FadeDecalsInRange`](#fadedecalsinrange) · [`FadeUpPedLight`](#fadeuppedlight) · [`ForceRenderInGameUi`](#forcerenderingameui) · [`FreeMemoryForHighQualityPhoto`](#freememoryforhighqualityphoto) · [`FreeMemoryForLowQualityPhoto`](#freememoryforlowqualityphoto) · [`FreeMemoryForMissionCreatorPhoto`](#freememoryformissioncreatorphoto) · [`GetActualScreenResolution`](#getactualscreenresolution) · [`GetAspectRatio`](#getaspectratio) · [`GetBinkMovieTime`](#getbinkmovietime) · [`GetCurrentNumberOfCloudPhotos`](#getcurrentnumberofcloudphotos) · [`GetDecalWashLevel`](#getdecalwashlevel) · [`GetExtraTimecycleModifierIndex`](#getextratimecyclemodifierindex) · [`GetIsHidef`](#getishidef) · [`GetIsPetrolDecalInRange`](#getispetroldecalinrange) · [`GetIsWidescreen`](#getiswidescreen) · [`GetMaximumNumberOfCloudPhotos`](#getmaximumnumberofcloudphotos) · [`GetMaximumNumberOfPhotos`](#getmaximumnumberofphotos) · [`GetRequestingnightvision`](#getrequestingnightvision) · [`GetSafeZoneSize`](#getsafezonesize) · [`GetScaleformMovieMethodReturnValueBool`](#getscaleformmoviemethodreturnvaluebool) · [`GetScaleformMovieMethodReturnValueInt`](#getscaleformmoviemethodreturnvalueint) · [`GetScaleformMovieMethodReturnValueString`](#getscaleformmoviemethodreturnvaluestring) · [`GetScreenCoordFromWorldCoord`](#getscreencoordfromworldcoord) · [`GetScreenResolution`](#getscreenresolution) · [`GetScreenblurFadeCurrentTime`](#getscreenblurfadecurrenttime) · [`GetScriptGfxPosition`](#getscriptgfxposition) · [`GetStatusOfLoadMissionCreatorPhoto`](#getstatusofloadmissioncreatorphoto) · [`GetStatusOfSaveHighQualityPhoto`](#getstatusofsavehighqualityphoto) · [`GetStatusOfSortedListOperation`](#getstatusofsortedlistoperation) · [`GetStatusOfTakeHighQualityPhoto`](#getstatusoftakehighqualityphoto) · [`GetStatusOfTakeMissionCreatorPhoto`](#getstatusoftakemissioncreatorphoto) · [`GetTextureResolution`](#gettextureresolution) · [`GetTimecycleModifierIndex`](#gettimecyclemodifierindex) · [`GetTimecycleTransitionModifierIndex`](#gettimecycletransitionmodifierindex) · [`GetTogglePausedRenderphasesStatus`](#gettogglepausedrenderphasesstatus) · [`GetTvChannel`](#gettvchannel) · [`GetTvVolume`](#gettvvolume) · [`GetUsingnightvision`](#getusingnightvision) · [`GetUsingseethrough`](#getusingseethrough) · [`GetVehicleCrewEmblemRequestState`](#getvehiclecrewemblemrequeststate) · [`GolfTrailGetMaxHeight`](#golftrailgetmaxheight) · [`GolfTrailGetVisualControlPoint`](#golftrailgetvisualcontrolpoint) · [`GolfTrailSetColour`](#golftrailsetcolour) · [`GolfTrailSetEnabled`](#golftrailsetenabled) · [`GolfTrailSetFacing`](#golftrailsetfacing) · [`GolfTrailSetFixedControlPoint`](#golftrailsetfixedcontrolpoint) · [`GolfTrailSetPath`](#golftrailsetpath) · [`GolfTrailSetRadius`](#golftrailsetradius) · [`GolfTrailSetShaderParams`](#golftrailsetshaderparams) · [`GolfTrailSetTessellation`](#golftrailsettessellation) · [`GrassLodResetScriptAreas`](#grasslodresetscriptareas) · [`GrassLodShrinkScriptAreas`](#grasslodshrinkscriptareas) · [`HasScaleformContainerMovieLoadedIntoParent`](#hasscaleformcontainermovieloadedintoparent) · [`HasScaleformMovieFilenameLoaded`](#hasscaleformmoviefilenameloaded) · [`HasScaleformMovieLoaded`](#hasscaleformmovieloaded) · [`HasScaleformMovieNamedLoaded`](#hasscaleformmovienamedloaded) · [`HasScaleformScriptHudMovieLoaded`](#hasscaleformscripthudmovieloaded) · [`HasStreamedTextureDictLoaded`](#hasstreamedtexturedictloaded) · [`IsDecalAlive`](#isdecalalive) · [`IsPlaylistUnk`](#isplaylistunk) · [`IsScaleformMovieDeleting`](#isscaleformmoviedeleting) · [`IsScaleformMovieMethodReturnValueReady`](#isscaleformmoviemethodreturnvalueready) · [`IsScreenblurFadeRunning`](#isscreenblurfaderunning) · [`IsTrackedPointVisible`](#istrackedpointvisible) · [`IsTvPlaylistItemPlaying`](#istvplaylistitemplaying) · [`LoadMissionCreatorPhoto`](#loadmissioncreatorphoto) · [`LoadMovieMeshSet`](#loadmoviemeshset) · [`MoveVehicleDecals`](#movevehicledecals) · [`N_0x0218ba067d249dea`](#n_0x0218ba067d249dea) · [`N_0x02369d5c8a51fdcf`](#n_0x02369d5c8a51fdcf) · [`N_0x03300b57fcac6ddb`](#n_0x03300b57fcac6ddb) · [`N_0x0ae73d8df3a762b2`](#n_0x0ae73d8df3a762b2) · [`N_0x0e4299c549f0d1f1`](#n_0x0e4299c549f0d1f1) · [`N_0x108be26959a9d9bb`](#n_0x108be26959a9d9bb) · [`N_0x14fc5833464340a8`](#n_0x14fc5833464340a8) · [`N_0x1612c45f9e3e0d44`](#n_0x1612c45f9e3e0d44) · [`N_0x1bbc135a4d25edde`](#n_0x1bbc135a4d25edde) · [`N_0x259ba6d4e6f808f1`](#n_0x259ba6d4e6f808f1) · [`N_0x25fc3e33a31ad0c9`](#n_0x25fc3e33a31ad0c9) · [`N_0x27cfb1b1e078cb2d`](#n_0x27cfb1b1e078cb2d) · [`N_0x27feb5254759cde3`](#n_0x27feb5254759cde3) · [`N_0x2a251aa48b2b46db`](#n_0x2a251aa48b2b46db) · [`N_0x2b40a97646381508`](#n_0x2b40a97646381508) · [`N_0x2c42340f916c5930`](#n_0x2c42340f916c5930) · [`N_0x2d3b147afad49de0`](#n_0x2d3b147afad49de0) · [`N_0x2fcb133ca50a49eb`](#n_0x2fcb133ca50a49eb) · [`N_0x30432a0118736e00`](#n_0x30432a0118736e00) · [`N_0x346ef3ecaaab149e`](#n_0x346ef3ecaaab149e) · [`N_0x36f6626459d91457`](#n_0x36f6626459d91457) · [`N_0x393bd2275ceb7793`](#n_0x393bd2275ceb7793) · [`N_0x3c788e7f6438754d`](#n_0x3c788e7f6438754d) · [`N_0x43fa7cbe20dab219`](#n_0x43fa7cbe20dab219) · [`N_0x46d1a61a21f566fc`](#n_0x46d1a61a21f566fc) · [`N_0x4af92acd3141d96c`](#n_0x4af92acd3141d96c) · [`N_0x54e22ea2c1956a8d`](#n_0x54e22ea2c1956a8d) · [`N_0x5b0316762afd4a64`](#n_0x5b0316762afd4a64) · [`N_0x5dbf05db5926d089`](#n_0x5dbf05db5926d089) · [`N_0x5debd9c4dc995692`](#n_0x5debd9c4dc995692) · [`N_0x5f6df3d92271e8a1`](#n_0x5f6df3d92271e8a1) · [`N_0x615d3925e87a3b26`](#n_0x615d3925e87a3b26) · [`N_0x61f95e5bb3e0a8c6`](#n_0x61f95e5bb3e0a8c6) · [`N_0x649c97d52332341a`](#n_0x649c97d52332341a) · [`N_0x6a51f78772175a51`](#n_0x6a51f78772175a51) · [`N_0x759650634f07b6b4`](#n_0x759650634f07b6b4) · [`N_0x7a42b2e236e71415`](#n_0x7a42b2e236e71415) · [`N_0x7ac24eab6d74118d`](#n_0x7ac24eab6d74118d) · [`N_0x7fa5d82b8f58ec06`](#n_0x7fa5d82b8f58ec06) · [`N_0x814af7dcaacc597b`](#n_0x814af7dcaacc597b) · [`N_0x82acc484ffa3b05f`](#n_0x82acc484ffa3b05f) · [`N_0x851cd923176eba7c`](#n_0x851cd923176eba7c) · [`N_0x8cde909a0370bb3a`](#n_0x8cde909a0370bb3a) · [`N_0x908311265d42a820`](#n_0x908311265d42a820) · [`N_0x949f397a288b28b3`](#n_0x949f397a288b28b3) · [`N_0x9641588dab93b4b5`](#n_0x9641588dab93b4b5) · [`N_0x98d18905bf723b99`](#n_0x98d18905bf723b99) · [`N_0x98edf76a7271e4f2`](#n_0x98edf76a7271e4f2) · [`N_0x9b079e5221d984d3`](#n_0x9b079e5221d984d3) · [`N_0xa46b73faa3460ae1`](#n_0xa46b73faa3460ae1) · [`N_0xaae9be70ec7c69ab`](#n_0xaae9be70ec7c69ab) · [`N_0xadd6627c4d325458`](#n_0xadd6627c4d325458) · [`N_0xae51bc858f32ba66`](#n_0xae51bc858f32ba66) · [`N_0xb2ebe8cbc58b90e9`](#n_0xb2ebe8cbc58b90e9) · [`N_0xb3c641f3630bf6da`](#n_0xb3c641f3630bf6da) · [`N_0xb569f41f3e7e83a4`](#n_0xb569f41f3e7e83a4) · [`N_0xba0127da25fd54c9`](#n_0xba0127da25fd54c9) · [`N_0xba3d194057c79a7b`](#n_0xba3d194057c79a7b) · [`N_0xbb90e12cac1dab25`](#n_0xbb90e12cac1dab25) · [`N_0xbcedb009461da156`](#n_0xbcedb009461da156) · [`N_0xbe197eaa669238f4`](#n_0xbe197eaa669238f4) · [`N_0xc0416b061f2b7e5e`](#n_0xc0416b061f2b7e5e) · [`N_0xc35a6d07c93802b2`](#n_0xc35a6d07c93802b2) · [`N_0xc5c8f970d4edff71`](#n_0xc5c8f970d4edff71) · [`N_0xca465d9cc0d231ba`](#n_0xca465d9cc0d231ba) · [`N_0xca4ae345a153d573`](#n_0xca4ae345a153d573) · [`N_0xcb82a0bf0e3e3265`](#n_0xcb82a0bf0e3e3265) · [`N_0xcfd16f0db5a3535c`](#n_0xcfd16f0db5a3535c) · [`N_0xd1c55b110e4df534`](#n_0xd1c55b110e4df534) · [`N_0xdb1ea9411c8911ec`](#n_0xdb1ea9411c8911ec) · [`N_0xe2892e7e55d7073a`](#n_0xe2892e7e55d7073a) · [`N_0xe59343e9e96529e7`](#n_0xe59343e9e96529e7) · [`N_0xe63d7c6eececb66b`](#n_0xe63d7c6eececb66b) · [`N_0xe791df1f73ed2c8b`](#n_0xe791df1f73ed2c8b) · [`N_0xec72c258667be5ea`](#n_0xec72c258667be5ea) · [`N_0xef398beee4ef45f9`](#n_0xef398beee4ef45f9) · [`N_0xf3f776ada161e47d`](#n_0xf3f776ada161e47d) · [`N_0xf51d36185993515d`](#n_0xf51d36185993515d) · [`N_0xf78b803082d4386f`](#n_0xf78b803082d4386f) · [`N_0xfcf6788fc4860cd4`](#n_0xfcf6788fc4860cd4) · [`OverrideInteriorSmokeEnd`](#overrideinteriorsmokeend) · [`OverrideInteriorSmokeLevel`](#overrideinteriorsmokelevel) · [`OverrideInteriorSmokeName`](#overrideinteriorsmokename) · [`OverridePedBadgeTexture`](#overridepedbadgetexture) · [`PassKeyboardInputToScaleform`](#passkeyboardinputtoscaleform) · [`PatchDecalDiffuseMap`](#patchdecaldiffusemap) · [`PlayBinkMovie`](#playbinkmovie) · [`PopTimecycleModifier`](#poptimecyclemodifier) · [`PresetInteriorAmbientCache`](#presetinteriorambientcache) · [`PushTimecycleModifier`](#pushtimecyclemodifier) · [`QueryMovieMeshSetState`](#querymoviemeshsetstate) · [`QueueOperationToCreateSortedListOfPhotos`](#queueoperationtocreatesortedlistofphotos) · [`RegisterNoirScreenEffectThisFrame`](#registernoirscreeneffectthisframe) · [`ReleaseBinkMovie`](#releasebinkmovie) · [`ReleaseMovieMeshSet`](#releasemoviemeshset) · [`RemoveDecal`](#removedecal) · [`RemoveDecalsFromObject`](#removedecalsfromobject) · [`RemoveDecalsFromObjectFacing`](#removedecalsfromobjectfacing) · [`RemoveDecalsFromVehicle`](#removedecalsfromvehicle) · [`RemoveDecalsInRange`](#removedecalsinrange) · [`RemoveParticleFx`](#removeparticlefx) · [`RemoveParticleFxFromEntity`](#removeparticlefxfromentity) · [`RemoveParticleFxInRange`](#removeparticlefxinrange) · [`RemoveScaleformScriptHudMovie`](#removescaleformscripthudmovie) · [`RemoveTcmodifierOverride`](#removetcmodifieroverride) · [`RemoveVehicleCrewEmblem`](#removevehiclecrewemblem) · [`RequestScaleformMovie`](#requestscaleformmovie) · [`RequestScaleformMovieInstance`](#requestscaleformmovieinstance) · [`RequestScaleformMovieSkipRenderWhilePaused`](#requestscaleformmovieskiprenderwhilepaused) · [`RequestScaleformMovieWithIgnoreSuperWidescreen`](#requestscaleformmoviewithignoresuperwidescreen) · [`RequestScaleformScriptHudMovie`](#requestscaleformscripthudmovie) · [`RequestStreamedTextureDict`](#requeststreamedtexturedict) · [`ResetAdaptation`](#resetadaptation) · [`ResetParticleFxOverride`](#resetparticlefxoverride) · [`ResetPausedRenderphases`](#resetpausedrenderphases) · [`ResetScriptGfxAlign`](#resetscriptgfxalign) · [`ReturnTwo`](#returntwo) · [`SaveHighQualityPhoto`](#savehighqualityphoto) · [`ScaleformMovieMethodAddParamBool`](#scaleformmoviemethodaddparambool) · [`ScaleformMovieMethodAddParamFloat`](#scaleformmoviemethodaddparamfloat) · [`ScaleformMovieMethodAddParamInt`](#scaleformmoviemethodaddparamint) · [`ScaleformMovieMethodAddParamLatestBriefString`](#scaleformmoviemethodaddparamlatestbriefstring) · [`ScaleformMovieMethodAddParamLiteralString`](#scaleformmoviemethodaddparamliteralstring) · [`ScaleformMovieMethodAddParamPlayerNameString`](#scaleformmoviemethodaddparamplayernamestring) · [`ScaleformMovieMethodAddParamTextureNameString`](#scaleformmoviemethodaddparamtexturenamestring) · [`SeethroughGetMaxThickness`](#seethroughgetmaxthickness) · [`SeethroughReset`](#seethroughreset) · [`SeethroughSetColorNear`](#seethroughsetcolornear) · [`SeethroughSetFadeEndDistance`](#seethroughsetfadeenddistance) · [`SeethroughSetFadeStartDistance`](#seethroughsetfadestartdistance) · [`SeethroughSetHeatscale`](#seethroughsetheatscale) · [`SeethroughSetHiLightIntensity`](#seethroughsethilightintensity) · [`SeethroughSetHiLightNoise`](#seethroughsethilightnoise) · [`SeethroughSetMaxThickness`](#seethroughsetmaxthickness) · [`SeethroughSetNoiseAmountMax`](#seethroughsetnoiseamountmax) · [`SeethroughSetNoiseAmountMin`](#seethroughsetnoiseamountmin) · [`SetArtificialLightsState`](#setartificiallightsstate) · [`SetArtificialLightsStateAffectsVehicles`](#setartificiallightsstateaffectsvehicles) · [`SetBackfaceculling`](#setbackfaceculling) · [`SetBinkMovie`](#setbinkmovie) · [`SetBinkMovieTime`](#setbinkmovietime) · [`SetBinkMovieUnk_2`](#setbinkmovieunk_2) · [`SetBinkMovieVolume`](#setbinkmovievolume) · [`SetBinkShouldSkip`](#setbinkshouldskip) · [`SetCheckpointCylinderHeight`](#setcheckpointcylinderheight) · [`SetCheckpointIconHeight`](#setcheckpointiconheight) · [`SetCheckpointIconScale`](#setcheckpointiconscale) · [`SetCheckpointRgba`](#setcheckpointrgba) · [`SetCheckpointRgba2`](#setcheckpointrgba2) · [`SetCurrentPlayerTcmodifier`](#setcurrentplayertcmodifier) · [`SetDebugLinesAndSpheresDrawingActive`](#setdebuglinesandspheresdrawingactive) · [`SetDisableDecalRenderingThisFrame`](#setdisabledecalrenderingthisframe) · [`SetDisablePetrolDecalsIgnitingThisFrame`](#setdisablepetroldecalsignitingthisframe) · [`SetDrawOrigin`](#setdraworigin) · [`SetEntityIconColor`](#setentityiconcolor) · [`SetEntityIconVisibility`](#setentityiconvisibility) · [`SetExtraTimecycleModifier`](#setextratimecyclemodifier) · [`SetFlash`](#setflash) · [`SetForcePedFootstepsTracks`](#setforcepedfootstepstracks) · [`SetForceVehicleTrails`](#setforcevehicletrails) · [`SetHidofOverride`](#sethidofoverride) · [`SetNextPlayerTcmodifier`](#setnextplayertcmodifier) · [`SetNightvision`](#setnightvision) · [`SetNoiseoveride`](#setnoiseoveride) · [`SetNoisinessoveride`](#setnoisinessoveride) · [`SetParticleFxBulletImpactScale`](#setparticlefxbulletimpactscale) · [`SetParticleFxCamInsideNonplayerVehicle`](#setparticlefxcaminsidenonplayervehicle) · [`SetParticleFxCamInsideVehicle`](#setparticlefxcaminsidevehicle) · [`SetParticleFxLoopedAlpha`](#setparticlefxloopedalpha) · [`SetParticleFxLoopedColour`](#setparticlefxloopedcolour) · [`SetParticleFxLoopedEvolution`](#setparticlefxloopedevolution) · [`SetParticleFxLoopedFarClipDist`](#setparticlefxloopedfarclipdist) · [`SetParticleFxLoopedOffsets`](#setparticlefxloopedoffsets) · [`SetParticleFxLoopedScale`](#setparticlefxloopedscale) · [`SetParticleFxNonLoopedAlpha`](#setparticlefxnonloopedalpha) · [`SetParticleFxNonLoopedColour`](#setparticlefxnonloopedcolour) · [`SetParticleFxNonLoopedEmitterScale`](#setparticlefxnonloopedemitterscale) · [`SetParticleFxOverride`](#setparticlefxoverride) · [`SetParticleFxShootoutBoat`](#setparticlefxshootoutboat) · [`SetPlayerTcmodifierTransition`](#setplayertcmodifiertransition) · [`SetScaleformMovieAsNoLongerNeeded`](#setscaleformmovieasnolongerneeded) · [`SetScaleformMovieToUseLargeRt`](#setscaleformmovietouselargert) · [`SetScaleformMovieToUseSuperLargeRt`](#setscaleformmovietousesuperlargert) · [`SetScaleformMovieToUseSystemTime`](#setscaleformmovietousesystemtime) · [`SetScriptGfxAlign`](#setscriptgfxalign) · [`SetScriptGfxAlignParams`](#setscriptgfxalignparams) · [`SetScriptGfxDrawBehindPausemenu`](#setscriptgfxdrawbehindpausemenu) · [`SetScriptGfxDrawOrder`](#setscriptgfxdraworder) · [`SetSeethrough`](#setseethrough) · [`SetStreamedTextureDictAsNoLongerNeeded`](#setstreamedtexturedictasnolongerneeded) · [`SetTimecycleModifier`](#settimecyclemodifier) · [`SetTimecycleModifierStrength`](#settimecyclemodifierstrength) · [`SetTrackedPointInfo`](#settrackedpointinfo) · [`SetTransitionOutOfTimecycleModifier`](#settransitionoutoftimecyclemodifier) · [`SetTransitionTimecycleModifier`](#settransitiontimecyclemodifier) · [`SetTvAudioFrontend`](#settvaudiofrontend) · [`SetTvChannel`](#settvchannel) · [`SetTvChannelPlaylist`](#settvchannelplaylist) · [`SetTvChannelPlaylistAtHour`](#settvchannelplaylistathour) · [`SetTvVolume`](#settvvolume) · [`StartNetworkedParticleFxLoopedOnEntity`](#startnetworkedparticlefxloopedonentity) · [`StartNetworkedParticleFxLoopedOnEntityBone`](#startnetworkedparticlefxloopedonentitybone) · [`StartNetworkedParticleFxNonLoopedAtCoord`](#startnetworkedparticlefxnonloopedatcoord) · [`StartNetworkedParticleFxNonLoopedOnEntity`](#startnetworkedparticlefxnonloopedonentity) · [`StartNetworkedParticleFxNonLoopedOnEntityBone`](#startnetworkedparticlefxnonloopedonentitybone) · [`StartNetworkedParticleFxNonLoopedOnPedBone`](#startnetworkedparticlefxnonloopedonpedbone) · [`StartParticleFxLoopedAtCoord`](#startparticlefxloopedatcoord) · [`StartParticleFxLoopedOnEntity`](#startparticlefxloopedonentity) · [`StartParticleFxLoopedOnEntityBone`](#startparticlefxloopedonentitybone) · [`StartParticleFxLoopedOnPedBone`](#startparticlefxloopedonpedbone) · [`StartParticleFxNonLoopedAtCoord`](#startparticlefxnonloopedatcoord) · [`StartParticleFxNonLoopedOnEntity`](#startparticlefxnonloopedonentity) · [`StartParticleFxNonLoopedOnPedBone`](#startparticlefxnonloopedonpedbone) · [`StartPetrolTrailDecals`](#startpetroltraildecals) · [`StopBinkMovie`](#stopbinkmovie) · [`StopParticleFxLooped`](#stopparticlefxlooped) · [`TerraingridActivate`](#terraingridactivate) · [`TerraingridSetColours`](#terraingridsetcolours) · [`TerraingridSetParams`](#terraingridsetparams) · [`TogglePausedRenderphases`](#togglepausedrenderphases) · [`TriggerScreenblurFadeIn`](#triggerscreenblurfadein) · [`TriggerScreenblurFadeOut`](#triggerscreenblurfadeout) · [`Ui3dsceneIsAvailable`](#ui3dsceneisavailable) · [`Ui3dscenePushPreset`](#ui3dscenepushpreset) · [`UnpatchDecalDiffuseMap`](#unpatchdecaldiffusemap) · [`UpdateLightsOnEntity`](#updatelightsonentity) · [`UseParticleFxAsset`](#useparticlefxasset) · [`WashDecalsFromVehicle`](#washdecalsfromvehicle) · [`WashDecalsInRange`](#washdecalsinrange)

---
### AddDecal

`ADD_DECAL` · hash `0xB302244A1839BDAD` · jhash `0xEAD0C412` · **Cliente**

```lua
local retval = AddDecal(decalType, posX, posY, posZ, dirX, dirY, dirZ, sideX, sideY, sideZ, width, height, rCoef, gCoef, bCoef, opacity, timeout, isLongRange, isDynamic, useComplexColn)
```
```c
int ADD_DECAL(int decalType, float posX, float posY, float posZ, float dirX, float dirY, float dirZ, float sideX, float sideY, float sideZ, float width, float height, float rCoef, float gCoef, float bCoef, float opacity, float timeout, BOOL isLongRange, BOOL isDynamic, BOOL useComplexColn);
```

**Parámetros**

- `decalType` (`int`): which type of decal to place, based on the ID, see `DecalTypes` enum.
- `posX` (`float`): X position coordinate.
- `posY` (`float`): Y position coordinate.
- `posZ` (`float`): Z position coordinate.
- `dirX` (`float`): X Orientation.
- `dirY` (`float`): Y Orientation.
- `dirZ` (`float`): Z Orientation.
- `sideX` (`float`): Usually set to 0.
- `sideY` (`float`): Usually set to 1.
- `sideZ` (`float`): Usually set to 0.
- `width` (`float`): Width of the decal.
- `height` (`float`): Height of the decal.
- `rCoef` (`float`): Red Color.
- `gCoef` (`float`): Green Color.
- `bCoef` (`float`): Blue Color.
- `opacity` (`float`): Alpha Color.
- `timeout` (`float`): The lifetime of the decal.
- `isLongRange` (`BOOL`): toggle further LOD draw distance.
- `isDynamic` (`BOOL`): toggle dynamics.
- `useComplexColn` (`BOOL`): use complex coloring.

**Devuelve:** `int` — An integer value representing the added decal index, will return `0` if the decal cannot be added.

**Descripción oficial:**

Places a decal into the world

```cs
public enum DecalTypes  
{  
    splatters_blood = 1010,  
    splatters_blood_dir = 1015,  
    splatters_blood_mist = 1017,  
    splatters_mud = 1020,  
    splatters_paint = 1030,  
    splatters_water = 1040,  
    splatters_water_hydrant = 1050,  
    splatters_blood2 = 1110,  
    weapImpact_metal = 4010,  
    weapImpact_concrete = 4020,  
    weapImpact_mattress = 4030,  
    weapImpact_mud = 4032,  
    weapImpact_wood = 4050,  
    weapImpact_sand = 4053,  
    weapImpact_cardboard = 4040,  
    weapImpact_melee_glass = 4100,  
    weapImpact_glass_blood = 4102,  
    weapImpact_glass_blood2 = 4104,  
    weapImpact_shotgun_paper = 4200,  
    weapImpact_shotgun_mattress,  
    weapImpact_shotgun_metal,  
    weapImpact_shotgun_wood,  
    weapImpact_shotgun_dirt,  
    weapImpact_shotgun_tvscreen,  
    weapImpact_shotgun_tvscreen2,  
    weapImpact_shotgun_tvscreen3,  
    weapImpact_melee_concrete = 4310,  
    weapImpact_melee_wood = 4312,  
    weapImpact_melee_metal = 4314,  
    burn1 = 4421,  
    burn2,  
    burn3,  
    burn4,  
    burn5,  
    bang_concrete_bang = 5000,  
    bang_concrete_bang2,  
    bang_bullet_bang,  
    bang_bullet_bang2 = 5004,  
    bang_glass = 5031,  
    bang_glass2,  
    solidPool_water = 9000,  
    solidPool_blood,  
    solidPool_oil,  
    solidPool_petrol,  
    solidPool_mud,  
    porousPool_water,  
    porousPool_blood,  
    porousPool_oil,  
    porousPool_petrol,  
    porousPool_mud,  
    porousPool_water_ped_drip,  
    liquidTrail_water = 9050  
}  
```

---
### AddEntityIcon

`ADD_ENTITY_ICON` · hash `0x9CD43EEE12BF4DD0` · jhash `0xF3027D21` · **Cliente**

```lua
local retval = AddEntityIcon(entity, icon)
```
```c
Any ADD_ENTITY_ICON(Entity entity, char* icon);
```

**Parámetros**

- `entity` (`Entity`)
- `icon` (`char*`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Example:  
GRAPHICS::ADD_ENTITY_ICON(a_0, "MP_Arrow");  
I tried this and nothing happened...  
```

---
### AddOilDecal

`_ADD_OIL_DECAL` · hash `0x126D7F89FE859A5E` · **Cliente**

```lua
local retval = AddOilDecal(x, y, z, groundLvl, width, transparency)
```
```c
int _ADD_OIL_DECAL(float x, float y, float z, float groundLvl, float width, float transparency);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `groundLvl` (`float`)
- `width` (`float`)
- `transparency` (`float`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### AddPetrolDecal

`ADD_PETROL_DECAL` · hash `0x4F5212C7AD880DF8` · jhash `0x1259DF42` · **Cliente**

```lua
local retval = AddPetrolDecal(x, y, z, groundLvl, width, transparency)
```
```c
int ADD_PETROL_DECAL(float x, float y, float z, float groundLvl, float width, float transparency);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `groundLvl` (`float`)
- `width` (`float`)
- `transparency` (`float`)

**Devuelve:** `int`

---
### AddPetrolTrailDecalInfo

`ADD_PETROL_TRAIL_DECAL_INFO` · hash `0x967278682CB6967A` · jhash `0xBAEC6ADD` · **Cliente**

```lua
AddPetrolTrailDecalInfo(x, y, z, p3)
```
```c
void ADD_PETROL_TRAIL_DECAL_INFO(float x, float y, float z, float p3);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x967278682CB6967A` (`N_0x967278682cb6967a`)

---
### AddTcmodifierOverride

`ADD_TCMODIFIER_OVERRIDE` · hash `0x1A8E2C8B9CF4549C` · jhash `0xE8F538B5` · **Cliente**

```lua
AddTcmodifierOverride(modifierName1, modifierName2)
```
```c
void ADD_TCMODIFIER_OVERRIDE(char* modifierName1, char* modifierName2);
```

**Parámetros**

- `modifierName1` (`char*`)
- `modifierName2` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1A8E2C8B9CF4549C` (`N_0x1a8e2c8b9cf4549c`)

---
### AddVehicleCrewEmblem

`ADD_VEHICLE_CREW_EMBLEM` · hash `0x428BDCB9DA58DA53` · jhash `0x12077738` · **Cliente**

```lua
local retval = AddVehicleCrewEmblem(vehicle, ped, boneIndex, x1, x2, x3, y1, y2, y3, z1, z2, z3, scale, p13, alpha)
```
```c
BOOL ADD_VEHICLE_CREW_EMBLEM(Vehicle vehicle, Ped ped, int boneIndex, float x1, float x2, float x3, float y1, float y2, float y3, float z1, float z2, float z3, float scale, Any p13, int alpha);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `ped` (`Ped`)
- `boneIndex` (`int`)
- `x1` (`float`)
- `x2` (`float`)
- `x3` (`float`)
- `y1` (`float`)
- `y2` (`float`)
- `y3` (`float`)
- `z1` (`float`)
- `z2` (`float`)
- `z3` (`float`)
- `scale` (`float`)
- `p13` (`Any`)
- `alpha` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
boneIndex is always chassis_dummy in the scripts. The x/y/z params are location relative to the chassis bone.
```

**Nombres antiguos (alias):** `_ADD_CLAN_DECAL_TO_VEHICLE` (`AddClanDecalToVehicle`)

---
### AdjustNextPosSizeAsNormalized_16_9

`ADJUST_NEXT_POS_SIZE_AS_NORMALIZED_16_9` · hash `0xEFABC7722293DA7C` · **Cliente**

```lua
AdjustNextPosSizeAsNormalized_16_9()
```
```c
void ADJUST_NEXT_POS_SIZE_AS_NORMALIZED_16_9();
```

**Devuelve:** `void`

**Descripción oficial:**

Must call this every frame, will adjust the next drawn scaleform movie size values to normalized 16:9

**Nombres antiguos (alias):** `0xEFABC7722293DA7C` (`N_0xefabc7722293da7c`)

---
### AnimpostfxGetUnk

`_ANIMPOSTFX_GET_UNK` · hash `0xE35B38A27E8E7179` · **Cliente**

```lua
local retval = AnimpostfxGetUnk(effectName)
```
```c
float _ANIMPOSTFX_GET_UNK(char* effectName);
```

**Parámetros**

- `effectName` (`char*`)

**Devuelve:** `float`

**Descripción oficial:**

See [`ANIMPOSTFX_PLAY`](#animpostfxplay)

**Nombres antiguos (alias):** `0xE35B38A27E8E7179` (`N_0xe35b38a27e8e7179`)

---
### AnimpostfxIsRunning

`ANIMPOSTFX_IS_RUNNING` · hash `0x36AD3E690DA5ACEB` · jhash `0x089D5921` · **Cliente**

```lua
local retval = AnimpostfxIsRunning(effectName)
```
```c
BOOL ANIMPOSTFX_IS_RUNNING(char* effectName);
```

**Parámetros**

- `effectName` (`char*`)

**Devuelve:** `BOOL` — Whether the specified effect is active

**Descripción oficial:**

See [`ANIMPOSTFX_PLAY`](#animpostfxplay).

**Nombres antiguos (alias):** `_GET_SCREEN_EFFECT_IS_ACTIVE` (`GetScreenEffectIsActive`)

---
### AnimpostfxPlay

`ANIMPOSTFX_PLAY` · hash `0x2206BF9A37B7F724` · jhash `0x1D980479` · **Cliente**

```lua
AnimpostfxPlay(effectName, duration, looped)
```
```c
void ANIMPOSTFX_PLAY(char* effectName, int duration, BOOL looped);
```

**Parámetros**

- `effectName` (`char*`)
- `duration` (`int`)
- `looped` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
duration - is how long to play the effect for in milliseconds. If 0, it plays the default length
if loop is true, the effect won't stop until you call ANIMPOSTFX_STOP on it. (only loopable effects)
```

**Nombres antiguos (alias):** `_START_SCREEN_EFFECT` (`StartScreenEffect`)

---
### AnimpostfxStop

`ANIMPOSTFX_STOP` · hash `0x068E835A1D0DC0E3` · jhash `0x06BB5CDA` · **Cliente**

```lua
AnimpostfxStop(effectName)
```
```c
void ANIMPOSTFX_STOP(char* effectName);
```

**Parámetros**

- `effectName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

See [`ANIMPOSTFX_PLAY`](#animpostfxplay).

**Nombres antiguos (alias):** `_STOP_SCREEN_EFFECT` (`StopScreenEffect`)

---
### AnimpostfxStopAll

`ANIMPOSTFX_STOP_ALL` · hash `0xB4EDDC19532BFB85` · jhash `0x4E6D875B` · **Cliente**

```lua
AnimpostfxStopAll()
```
```c
void ANIMPOSTFX_STOP_ALL();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `_STOP_ALL_SCREEN_EFFECTS` (`StopAllScreenEffects`)

---
### AnimpostfxStopAndDoUnk

`_ANIMPOSTFX_STOP_AND_DO_UNK` · hash `0xD2209BE128B5418C` · **Cliente**

```lua
AnimpostfxStopAndDoUnk(effectName)
```
```c
void _ANIMPOSTFX_STOP_AND_DO_UNK(char* effectName);
```

**Parámetros**

- `effectName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Stops the effect and sets a value (bool) in its data (+0x199) to false; See [`ANIMPOSTFX_PLAY`](#animpostfxplay).

**Nombres antiguos (alias):** `0xD2209BE128B5418C` (`N_0xd2209be128b5418c`)

---
### AttachTvAudioToEntity

`ATTACH_TV_AUDIO_TO_ENTITY` · hash `0x845BAD77CC770633` · jhash `0x784944DB` · **Cliente**

```lua
AttachTvAudioToEntity(entity)
```
```c
void ATTACH_TV_AUDIO_TO_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
Might be more appropriate in AUDIO?  
```

---
### BeginScaleformMovieMethod

`BEGIN_SCALEFORM_MOVIE_METHOD` · hash `0xF6E48914C7A8694E` · jhash `0x215ABBE8` · **Cliente**

```lua
local retval = BeginScaleformMovieMethod(scaleform, methodName)
```
```c
BOOL BEGIN_SCALEFORM_MOVIE_METHOD(int scaleform, char* methodName);
```

**Parámetros**

- `scaleform` (`int`)
- `methodName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Push a function from the Scaleform onto the stack  
```

**Nombres antiguos (alias):** `_PUSH_SCALEFORM_MOVIE_FUNCTION` (`PushScaleformMovieFunction`)

---
### BeginScaleformMovieMethodOnFrontend

`BEGIN_SCALEFORM_MOVIE_METHOD_ON_FRONTEND` · hash `0xAB58C27C2E6123C6` · jhash `0xF6015178` · **Cliente**

```lua
local retval = BeginScaleformMovieMethodOnFrontend(functionName)
```
```c
BOOL BEGIN_SCALEFORM_MOVIE_METHOD_ON_FRONTEND(char* functionName);
```

**Parámetros**

- `functionName` (`char*`): The function name of the scaleform to call.

**Devuelve:** `BOOL`

**Descripción oficial:**

Starts frontend (pause menu) scaleform movie methods.
This can be used when you want to make custom frontend menus, and customize things like images or text in the menus etc.

Use [`BEGIN_SCALEFORM_MOVIE_METHOD_ON_FRONTEND_HEADER`](#beginscaleformmoviemethodonfrontendheader) for header scaleform functions.

**Nombres antiguos (alias):** `0xAB58C27C2E6123C6` (`N_0xab58c27c2e6123c6`), `_PUSH_SCALEFORM_MOVIE_FUNCTION_N` (`PushScaleformMovieFunctionN`), `_BEGIN_SCALEFORM_MOVIE_METHOD_N` (`BeginScaleformMovieMethodN`)

---
### BeginScaleformMovieMethodOnFrontendHeader

`BEGIN_SCALEFORM_MOVIE_METHOD_ON_FRONTEND_HEADER` · hash `0xB9449845F73F5E9C` · jhash `0x5E219B67` · **Cliente**

```lua
local retval = BeginScaleformMovieMethodOnFrontendHeader(functionName)
```
```c
BOOL BEGIN_SCALEFORM_MOVIE_METHOD_ON_FRONTEND_HEADER(char* functionName);
```

**Parámetros**

- `functionName` (`char*`): Scaleform function name.

**Devuelve:** `BOOL`

**Descripción oficial:**

Starts frontend (pause menu) scaleform movie methods for header options.

Use [`BEGIN_SCALEFORM_MOVIE_METHOD_ON_FRONTEND`](#beginscaleformmoviemethodonfrontend) to customize the content inside the frontend menus.

**Nombres antiguos (alias):** `0xB9449845F73F5E9C` (`N_0xb9449845f73f5e9c`), `_BEGIN_SCALEFORM_MOVIE_METHOD_V` (`BeginScaleformMovieMethodV`)

---
### BeginScaleformScriptHudMovieMethod

`BEGIN_SCALEFORM_SCRIPT_HUD_MOVIE_METHOD` · hash `0x98C494FD5BDFBFD5` · jhash `0x5D66CE1E` · **Cliente**

```lua
local retval = BeginScaleformScriptHudMovieMethod(hudComponent, methodName)
```
```c
BOOL BEGIN_SCALEFORM_SCRIPT_HUD_MOVIE_METHOD(int hudComponent, char* methodName);
```

**Parámetros**

- `hudComponent` (`int`)
- `methodName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Pushes a function from the Hud component Scaleform onto the stack. Same behavior as GRAPHICS::BEGIN_SCALEFORM_MOVIE_METHOD, just a hud component id instead of a Scaleform.
Known components:
19 - MP_RANK_BAR
20 - HUD_DIRECTOR_MODE
This native requires more research - all information can be found inside of 'hud.gfx'. Using a decompiler, the different components are located under "scripts\__Packages\com\rockstargames\gtav\hud\hudComponents" and "scripts\__Packages\com\rockstargames\gtav\Multiplayer".
```

**Nombres antiguos (alias):** `_PUSH_SCALEFORM_MOVIE_FUNCTION_FROM_HUD_COMPONENT` (`PushScaleformMovieFunctionFromHudComponent`), `_BEGIN_SCALEFORM_MOVIE_METHOD_HUD_COMPONENT` (`BeginScaleformMovieMethodHudComponent`)

---
### BeginTakeHighQualityPhoto

`BEGIN_TAKE_HIGH_QUALITY_PHOTO` · hash `0xA67C35C56EB1BD9D` · jhash `0x47B0C137` · **Cliente**

```lua
local retval = BeginTakeHighQualityPhoto()
```
```c
BOOL BEGIN_TAKE_HIGH_QUALITY_PHOTO();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA67C35C56EB1BD9D` (`N_0xa67c35c56eb1bd9d`)

---
### BeginTakeMissionCreatorPhoto

`BEGIN_TAKE_MISSION_CREATOR_PHOTO` · hash `0x1DD2139A9A20DCE8` · jhash `0xBA9AD458` · **Cliente**

```lua
local retval = BeginTakeMissionCreatorPhoto()
```
```c
BOOL BEGIN_TAKE_MISSION_CREATOR_PHOTO();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1DD2139A9A20DCE8` (`N_0x1dd2139a9a20dce8`)

---
### BeginTextCommandScaleformString

`BEGIN_TEXT_COMMAND_SCALEFORM_STRING` · hash `0x80338406F3475E55` · jhash `0x3AC9CB55` · **Cliente**

```lua
BeginTextCommandScaleformString(textLabel)
```
```c
void BEGIN_TEXT_COMMAND_SCALEFORM_STRING(char* textLabel);
```

**Parámetros**

- `textLabel` (`char*`): a GXT text label

**Devuelve:** `void`

**Descripción oficial:**

```
Called prior to adding a text component to the UI. After doing so, GRAPHICS::END_TEXT_COMMAND_SCALEFORM_STRING is called.
Examples:
GRAPHICS::BEGIN_TEXT_COMMAND_SCALEFORM_STRING("NUMBER");
HUD::ADD_TEXT_COMPONENT_INTEGER(MISC::ABSI(a_1));
GRAPHICS::END_TEXT_COMMAND_SCALEFORM_STRING();
GRAPHICS::BEGIN_TEXT_COMMAND_SCALEFORM_STRING("STRING");
HUD::_ADD_TEXT_COMPONENT_STRING(a_2);
GRAPHICS::END_TEXT_COMMAND_SCALEFORM_STRING();
GRAPHICS::BEGIN_TEXT_COMMAND_SCALEFORM_STRING("STRTNM2");
HUD::_0x17299B63C7683A2B(v_3);
HUD::_0x17299B63C7683A2B(v_4);
GRAPHICS::END_TEXT_COMMAND_SCALEFORM_STRING();
GRAPHICS::BEGIN_TEXT_COMMAND_SCALEFORM_STRING("STRTNM1");
HUD::_0x17299B63C7683A2B(v_3);
GRAPHICS::END_TEXT_COMMAND_SCALEFORM_STRING();
```

**Nombres antiguos (alias):** `_BEGIN_TEXT_COMPONENT` (`BeginTextComponent`)

---
### CallScaleformMovieMethod

`CALL_SCALEFORM_MOVIE_METHOD` · hash `0xFBD96D87AC96D533` · jhash `0x7AB77B57` · **Cliente**

```lua
CallScaleformMovieMethod(scaleform, method)
```
```c
void CALL_SCALEFORM_MOVIE_METHOD(int scaleform, char* method);
```

**Parámetros**

- `scaleform` (`int`)
- `method` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Calls the Scaleform function.  
```

**Nombres antiguos (alias):** `_CALL_SCALEFORM_MOVIE_FUNCTION_VOID` (`CallScaleformMovieFunctionVoid`)

---
### CallScaleformMovieMethodWithNumber

`CALL_SCALEFORM_MOVIE_METHOD_WITH_NUMBER` · hash `0xD0837058AE2E4BEE` · jhash `0x557EDA1D` · **Cliente**

```lua
CallScaleformMovieMethodWithNumber(scaleform, methodName, param1, param2, param3, param4, param5)
```
```c
void CALL_SCALEFORM_MOVIE_METHOD_WITH_NUMBER(int scaleform, char* methodName, float param1, float param2, float param3, float param4, float param5);
```

**Parámetros**

- `scaleform` (`int`)
- `methodName` (`char*`)
- `param1` (`float`)
- `param2` (`float`)
- `param3` (`float`)
- `param4` (`float`)
- `param5` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Calls the Scaleform function and passes the parameters as floats.  
The number of parameters passed to the function varies, so the end of the parameter list is represented by -1.0.  
```

**Nombres antiguos (alias):** `_CALL_SCALEFORM_MOVIE_FUNCTION_FLOAT_PARAMS` (`CallScaleformMovieFunctionFloatParams`)

---
### CallScaleformMovieMethodWithNumberAndString

`CALL_SCALEFORM_MOVIE_METHOD_WITH_NUMBER_AND_STRING` · hash `0xEF662D8D57E290B1` · jhash `0x6EAF56DE` · **Cliente**

```lua
CallScaleformMovieMethodWithNumberAndString(scaleform, methodName, floatParam1, floatParam2, floatParam3, floatParam4, floatParam5, stringParam1, stringParam2, stringParam3, stringParam4, stringParam5)
```
```c
void CALL_SCALEFORM_MOVIE_METHOD_WITH_NUMBER_AND_STRING(int scaleform, char* methodName, float floatParam1, float floatParam2, float floatParam3, float floatParam4, float floatParam5, char* stringParam1, char* stringParam2, char* stringParam3, char* stringParam4, char* stringParam5);
```

**Parámetros**

- `scaleform` (`int`)
- `methodName` (`char*`)
- `floatParam1` (`float`)
- `floatParam2` (`float`)
- `floatParam3` (`float`)
- `floatParam4` (`float`)
- `floatParam5` (`float`)
- `stringParam1` (`char*`)
- `stringParam2` (`char*`)
- `stringParam3` (`char*`)
- `stringParam4` (`char*`)
- `stringParam5` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Calls the Scaleform function and passes both float and string parameters (in their respective order).  
The number of parameters passed to the function varies, so the end of the float parameters is represented by -1.0, and the end of the string parameters is represented by 0 (NULL).  
NOTE: The order of parameters in the function prototype is important! All float parameters must come first, followed by the string parameters.  
Examples:  
// function MY_FUNCTION(floatParam1, floatParam2, stringParam)  
GRAPHICS::_CALL_SCALEFORM_MOVIE_FUNCTION_MIXED_PARAMS(scaleform, "MY_FUNCTION", 10.0, 20.0, -1.0, -1.0, -1.0, "String param", 0, 0, 0, 0);  
// function MY_FUNCTION_2(floatParam, stringParam1, stringParam2)  
GRAPHICS::_CALL_SCALEFORM_MOVIE_FUNCTION_MIXED_PARAMS(scaleform, "MY_FUNCTION_2", 10.0, -1.0, -1.0, -1.0, -1.0, "String param #1", "String param #2", 0, 0, 0);  
```

**Nombres antiguos (alias):** `_CALL_SCALEFORM_MOVIE_FUNCTION_MIXED_PARAMS` (`CallScaleformMovieFunctionMixedParams`)

---
### CallScaleformMovieMethodWithString

`CALL_SCALEFORM_MOVIE_METHOD_WITH_STRING` · hash `0x51BC1ED3CC44E8F7` · jhash `0x91A7FCEB` · **Cliente**

```lua
CallScaleformMovieMethodWithString(scaleform, methodName, param1, param2, param3, param4, param5)
```
```c
void CALL_SCALEFORM_MOVIE_METHOD_WITH_STRING(int scaleform, char* methodName, char* param1, char* param2, char* param3, char* param4, char* param5);
```

**Parámetros**

- `scaleform` (`int`)
- `methodName` (`char*`)
- `param1` (`char*`)
- `param2` (`char*`)
- `param3` (`char*`)
- `param4` (`char*`)
- `param5` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Calls the Scaleform function and passes the parameters as strings.  
The number of parameters passed to the function varies, so the end of the parameter list is represented by 0 (NULL).  
```

**Nombres antiguos (alias):** `_CALL_SCALEFORM_MOVIE_FUNCTION_STRING_PARAMS` (`CallScaleformMovieFunctionStringParams`)

---
### CascadeShadowsClearShadowSampleType

`_CASCADE_SHADOWS_CLEAR_SHADOW_SAMPLE_TYPE` · hash `0x27CB772218215325` · **Cliente**

```lua
CascadeShadowsClearShadowSampleType()
```
```c
void _CASCADE_SHADOWS_CLEAR_SHADOW_SAMPLE_TYPE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x27CB772218215325` (`N_0x27cb772218215325`), `_CASCADESHADOWS_RESET_TYPE` (`CascadeshadowsResetType`)

---
### CascadeShadowsEnableEntityTracker

`CASCADE_SHADOWS_ENABLE_ENTITY_TRACKER` · hash `0x80ECBC0C856D3B0B` · jhash `0xFE903D0F` · **Cliente**

```lua
CascadeShadowsEnableEntityTracker(toggle)
```
```c
void CASCADE_SHADOWS_ENABLE_ENTITY_TRACKER(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
When this is set to ON, shadows only draw as you get nearer.
When OFF, they draw from a further distance.
```

**Nombres antiguos (alias):** `_SET_FAR_SHADOWS_SUPPRESSED` (`SetFarShadowsSuppressed`)

---
### CascadeShadowsInitSession

`CASCADE_SHADOWS_INIT_SESSION` · hash `0x03FC694AE06C5A20` · jhash `0x48F16186` · **Cliente**

```lua
CascadeShadowsInitSession()
```
```c
void CASCADE_SHADOWS_INIT_SESSION();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x03FC694AE06C5A20` (`N_0x03fc694ae06c5a20`)

---
### CascadeShadowsSetAircraftMode

`CASCADE_SHADOWS_SET_AIRCRAFT_MODE` · hash `0x6DDBF9DFFC4AC080` · jhash `0x9F470BE3` · **Cliente**

```lua
CascadeShadowsSetAircraftMode(p0)
```
```c
void CASCADE_SHADOWS_SET_AIRCRAFT_MODE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6DDBF9DFFC4AC080` (`N_0x6ddbf9dffc4ac080`)

---
### CascadeShadowsSetCascadeBounds

`CASCADE_SHADOWS_SET_CASCADE_BOUNDS` · hash `0xD2936CAB8B58FCBD` · jhash `0x84F05943` · **Cliente**

```lua
CascadeShadowsSetCascadeBounds(p0, p1, p2, p3, p4, p5, p6, p7)
```
```c
void CASCADE_SHADOWS_SET_CASCADE_BOUNDS(Any p0, BOOL p1, float p2, float p3, float p4, float p5, BOOL p6, float p7);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`BOOL`)
- `p7` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD2936CAB8B58FCBD` (`N_0xd2936cab8b58fcbd`)

---
### CascadeShadowsSetCascadeBoundsScale

`CASCADE_SHADOWS_SET_CASCADE_BOUNDS_SCALE` · hash `0x5F0F3F56635809EF` · jhash `0x13D4ABC0` · **Cliente**

```lua
CascadeShadowsSetCascadeBoundsScale(p0)
```
```c
void CASCADE_SHADOWS_SET_CASCADE_BOUNDS_SCALE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5F0F3F56635809EF` (`N_0x5f0f3f56635809ef`)

---
### CascadeShadowsSetDynamicDepthMode

`CASCADE_SHADOWS_SET_DYNAMIC_DEPTH_MODE` · hash `0xD39D13C9FEBF0511` · jhash `0x4A124267` · **Cliente**

```lua
CascadeShadowsSetDynamicDepthMode(p0)
```
```c
void CASCADE_SHADOWS_SET_DYNAMIC_DEPTH_MODE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD39D13C9FEBF0511` (`N_0xd39d13c9febf0511`)

---
### CascadeShadowsSetDynamicDepthValue

`CASCADE_SHADOWS_SET_DYNAMIC_DEPTH_VALUE` · hash `0x02AC28F3A01FA04A` · jhash `0xB19B2764` · **Cliente**

```lua
CascadeShadowsSetDynamicDepthValue(p0)
```
```c
void CASCADE_SHADOWS_SET_DYNAMIC_DEPTH_VALUE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x02AC28F3A01FA04A` (`N_0x02ac28f3a01fa04a`)

---
### CascadeShadowsSetEntityTrackerScale

`CASCADE_SHADOWS_SET_ENTITY_TRACKER_SCALE` · hash `0x5E9DAF5A20F15908` · jhash `0xD2157428` · **Cliente**

```lua
CascadeShadowsSetEntityTrackerScale(p0)
```
```c
void CASCADE_SHADOWS_SET_ENTITY_TRACKER_SCALE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5E9DAF5A20F15908` (`N_0x5e9daf5a20f15908`)

---
### CascadeShadowsSetShadowSampleType

`CASCADE_SHADOWS_SET_SHADOW_SAMPLE_TYPE` · hash `0xB11D94BC55F41932` · jhash `0xDE10BA1F` · **Cliente**

```lua
CascadeShadowsSetShadowSampleType(type)
```
```c
void CASCADE_SHADOWS_SET_SHADOW_SAMPLE_TYPE(char* type);
```

**Parámetros**

- `type` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Possible values:
"CSM_ST_POINT"
"CSM_ST_LINEAR"
"CSM_ST_TWOTAP"
"CSM_ST_BOX3x3"
"CSM_ST_BOX4x4"
"CSM_ST_DITHER2_LINEAR"
"CSM_ST_CUBIC"
"CSM_ST_DITHER4"
"CSM_ST_DITHER16"
"CSM_ST_SOFT16"
"CSM_ST_DITHER16_RPDB"
"CSM_ST_POISSON16_RPDB_GNORM"
"CSM_ST_HIGHRES_BOX4x4"
"CSM_ST_CLOUDS_SIMPLE"
"CSM_ST_CLOUDS_LINEAR"
"CSM_ST_CLOUDS_TWOTAP"
"CSM_ST_CLOUDS_BOX3x3"
"CSM_ST_CLOUDS_BOX4x4"
"CSM_ST_CLOUDS_DITHER2_LINEAR"
"CSM_ST_CLOUDS_SOFT16"
"CSM_ST_CLOUDS_DITHER16_RPDB"
"CSM_ST_CLOUDS_POISSON16_RPDB_GNORM"
```

**Nombres antiguos (alias):** `0xB11D94BC55F41932` (`N_0xb11d94bc55f41932`), `_CASCADESHADOWS_SET_TYPE` (`CascadeshadowsSetType`)

---
### ClearDrawOrigin

`CLEAR_DRAW_ORIGIN` · hash `0xFF0B610F6BE0D7AF` · jhash `0xDD76B263` · **Cliente**

```lua
ClearDrawOrigin()
```
```c
void CLEAR_DRAW_ORIGIN();
```

**Devuelve:** `void`

**Descripción oficial:**

Resets the screen's draw-origin which was changed by the function [`SET_DRAW_ORIGIN`](#setdraworigin) back to `x=0, y=0`. See [`SET_DRAW_ORIGIN`](#setdraworigin) for further information.

---
### ClearExtraTimecycleModifier

`_CLEAR_EXTRA_TIMECYCLE_MODIFIER` · hash `0x92CCC17A7A2285DA` · jhash `0x6776720A` · **Cliente**

```lua
ClearExtraTimecycleModifier()
```
```c
void _CLEAR_EXTRA_TIMECYCLE_MODIFIER();
```

**Devuelve:** `void`

**Descripción oficial:**

Clears the secondary timecycle modifier usually set with [`SetExtraTimecycleModifier`](#setextratimecyclemodifier)

**Nombres antiguos (alias):** `0x92CCC17A7A2285DA` (`N_0x92ccc17a7a2285da`)

---
### ClearTimecycleModifier

`CLEAR_TIMECYCLE_MODIFIER` · hash `0x0F07E7745A236711` · jhash `0x8D8DF8EE` · **Cliente**

```lua
ClearTimecycleModifier()
```
```c
void CLEAR_TIMECYCLE_MODIFIER();
```

**Devuelve:** `void`

---
### ClearTvChannelPlaylist

`CLEAR_TV_CHANNEL_PLAYLIST` · hash `0xBEB3D46BB7F043C0` · jhash `0xCBE7068F` · **Cliente**

```lua
ClearTvChannelPlaylist(tvChannel)
```
```c
void CLEAR_TV_CHANNEL_PLAYLIST(int tvChannel);
```

**Parámetros**

- `tvChannel` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBEB3D46BB7F043C0` (`N_0xbeb3d46bb7f043c0`)

---
### CreateCheckpoint

`CREATE_CHECKPOINT` · hash `0x0134F0835AB6BFCB` · jhash `0xF541B690` · **Cliente**

```lua
local retval = CreateCheckpoint(type, posX1, posY1, posZ1, posX2, posY2, posZ2, diameter, red, green, blue, alpha, reserved)
```
```c
int CREATE_CHECKPOINT(int type, float posX1, float posY1, float posZ1, float posX2, float posY2, float posZ2, float diameter, int red, int green, int blue, int alpha, int reserved);
```

**Parámetros**

- `type` (`int`)
- `posX1` (`float`)
- `posY1` (`float`)
- `posZ1` (`float`)
- `posX2` (`float`)
- `posY2` (`float`)
- `posZ2` (`float`)
- `diameter` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)
- `reserved` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Creates a checkpoint. Returns the handle of the checkpoint.  
20/03/17 : Attention, checkpoints are already handled by the game itself, so you must not loop it like markers.
Parameters:  
* type - The type of checkpoint to create. See below for a list of checkpoint types.  
* pos1 - The position of the checkpoint.  
* pos2 - The position of the next checkpoint to point to.  
* diameter - The diameter of the checkpoint.
* color - The color of the checkpoint.  
* reserved - Special parameter, see below for details. Usually set to 0 in the scripts.  
Checkpoint types (prior to game build 2189):  
0-4---------Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker  
5-9---------Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker  
10-14-------Ring: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker  
15-19-------1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker        
20-24-------Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker   
25-29-------Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker      
30-34-------Cylinder: 1 arrow, 2 arrow, 3 arrows, CycleArrow, Checker   
35-38-------Ring: Airplane Up, Left, Right, UpsideDown  
39----------?  
40----------Ring: just a ring  
41----------?  
42-44-------Cylinder w/ number (uses 'reserved' parameter)  
45-47-------Cylinder no arrow or number  
If using type 42-44, reserved sets number / number and shape to display  
0-99------------Just numbers (0-99)  
100-109-----------------Arrow (0-9)  
110-119------------Two arrows (0-9)  
120-129----------Three arrows (0-9)  
130-139----------------Circle (0-9)  
140-149------------CycleArrow (0-9)  
150-159----------------Circle (0-9)  
160-169----Circle  w/ pointer (0-9)  
170-179-------Perforated ring (0-9)  
180-189----------------Sphere (0-9)  
```

[Checkpoint Types](https://docs.fivem.net/docs/game-references/checkpoints/) as of game build 2189

---
### CreateTrackedPoint

`CREATE_TRACKED_POINT` · hash `0xE2C9439ED45DEA60` · jhash `0x3129C31A` · **Cliente**

```lua
local retval = CreateTrackedPoint()
```
```c
int CREATE_TRACKED_POINT();
```

**Devuelve:** `int`

**Descripción oficial:**

Creates a tracked point: useful for checking the visibility of a 3D point on screen.

Tracked points must be manually managed and will not be destroyed on resource stop (they are not an instance of CScriptResource). See [`DESTROY_TRACKED_POINT`](#destroytrackedpoint) and [onResourceStop](https://docs.fivem.net/docs/scripting-reference/events/list/onResourceStop/).

Only 64 points may be tracked at a given time.

---
### DeleteCheckpoint

`DELETE_CHECKPOINT` · hash `0xF5ED37F54CD4D52E` · jhash `0xB66CF3CA` · **Cliente**

```lua
DeleteCheckpoint(checkpoint)
```
```c
void DELETE_CHECKPOINT(int checkpoint);
```

**Parámetros**

- `checkpoint` (`int`)

**Devuelve:** `void`

---
### DestroyTrackedPoint

`DESTROY_TRACKED_POINT` · hash `0xB25DC90BAD56CA42` · jhash `0x14AC675F` · **Cliente**

```lua
DestroyTrackedPoint(point)
```
```c
void DESTROY_TRACKED_POINT(int point);
```

**Parámetros**

- `point` (`int`)

**Devuelve:** `void`

---
### DisableMoonCycleOverride

`DISABLE_MOON_CYCLE_OVERRIDE` · hash `0x2BF72AD5B41AA739` · **Cliente**

```lua
DisableMoonCycleOverride()
```
```c
void DISABLE_MOON_CYCLE_OVERRIDE();
```

**Devuelve:** `void`

**Descripción oficial:**

Removes any custom moon cycle overrides that have been configured with [ENABLE_MOON_CYCLE_OVERRIDE](#enablemooncycleoverride)

**Nombres antiguos (alias):** `0x2BF72AD5B41AA739` (`N_0x2bf72ad5b41aa739`), `_RESET_EXTRA_TIMECYCLE_MODIFIER_STRENGTH` (`ResetExtraTimecycleModifierStrength`)

**Ejemplo (lua):**

```lua
DisableMoonCycleOverride()
```

---
### DisableOcclusionThisFrame

`DISABLE_OCCLUSION_THIS_FRAME` · hash `0x3669F1B198DCAA4F` · jhash `0x0DCC0B8B` · **Cliente**

```lua
DisableOcclusionThisFrame()
```
```c
void DISABLE_OCCLUSION_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

This disables all occluders that cause the 'flickering' rendering under the map and inside buildings with no interiors, note that this may impact performance on lower end systems.

**Nombres antiguos (alias):** `0x3669F1B198DCAA4F` (`N_0x3669f1b198dcaa4f`)

**Ejemplo (lua):**

```lua
-- Example thread that has to run every frame
Citizen.CreateThread(function()
  while true do
    DisableOcclusionThisFrame()
    Citizen.Wait(0)
  end
end)
```

---
### DisableScreenblurFade

`DISABLE_SCREENBLUR_FADE` · hash `0xDE81239437E8C5A8` · jhash `0xDB7AECDA` · **Cliente**

```lua
DisableScreenblurFade()
```
```c
void DISABLE_SCREENBLUR_FADE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDE81239437E8C5A8` (`N_0xde81239437e8c5a8`), `PAUSED_SCREENBLUR_LOADED` (`PausedScreenblurLoaded`)

---
### DisableScriptAmbientEffects

`_DISABLE_SCRIPT_AMBIENT_EFFECTS` · hash `0xEFD97FF47B745B8D` · **Cliente**

```lua
DisableScriptAmbientEffects(p0)
```
```c
void _DISABLE_SCRIPT_AMBIENT_EFFECTS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEFD97FF47B745B8D` (`N_0xefd97ff47b745b8d`)

---
### DisableVehicleDistantlights

`DISABLE_VEHICLE_DISTANTLIGHTS` · hash `0xC9F98AC1884E73A2` · jhash `0x7CFAE36F` · **Cliente**

```lua
DisableVehicleDistantlights(toggle)
```
```c
void DISABLE_VEHICLE_DISTANTLIGHTS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### DoesLatestBriefStringExist

`DOES_LATEST_BRIEF_STRING_EXIST` · hash `0x5E657EF1099EDD65` · jhash `0x91A081A1` · **Cliente**

```lua
local retval = DoesLatestBriefStringExist(briefValue)
```
```c
BOOL DOES_LATEST_BRIEF_STRING_EXIST(int briefValue);
```

**Parámetros**

- `briefValue` (`int`): A value indicating brief text.

**Devuelve:** `BOOL`

**Descripción oficial:**

Used in pi_menu.c. Checks if there is a brief entry for specified value.
Values:
0 - Dialogue brief
1 - Help text brief
2 - Mission Objective brief

**Nombres antiguos (alias):** `0x5E657EF1099EDD65` (`N_0x5e657ef1099edd65`)

---
### DoesParticleFxLoopedExist

`DOES_PARTICLE_FX_LOOPED_EXIST` · hash `0x74AFEF0D2E1E409B` · jhash `0xCBF91D2A` · **Cliente**

```lua
local retval = DoesParticleFxLoopedExist(ptfxHandle)
```
```c
BOOL DOES_PARTICLE_FX_LOOPED_EXIST(int ptfxHandle);
```

**Parámetros**

- `ptfxHandle` (`int`)

**Devuelve:** `BOOL`

---
### DoesVehicleHaveCrewEmblem

`DOES_VEHICLE_HAVE_CREW_EMBLEM` · hash `0x060D935D3981A275` · jhash `0x6D58F73B` · **Cliente**

```lua
local retval = DoesVehicleHaveCrewEmblem(vehicle, p1)
```
```c
BOOL DOES_VEHICLE_HAVE_CREW_EMBLEM(Vehicle vehicle, int p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_HAS_VEHICLE_GOT_DECAL` (`HasVehicleGotDecal`), `_DOES_VEHICLE_HAVE_DECAL` (`DoesVehicleHaveDecal`)

---
### DontRenderInGameUi

`DONT_RENDER_IN_GAME_UI` · hash `0x22A249A53034450A` · jhash `0x932FDB81` · **Cliente**

```lua
DontRenderInGameUi(p0)
```
```c
void DONT_RENDER_IN_GAME_UI(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x22A249A53034450A` (`N_0x22a249a53034450a`)

---
### DrawBinkMovie

`_DRAW_BINK_MOVIE` · hash `0x7118E83EEB9F7238` · **Cliente**

```lua
DrawBinkMovie(binkMovie, posX, posY, scaleX, scaleY, rotation, r, g, b, a)
```
```c
void _DRAW_BINK_MOVIE(int binkMovie, float posX, float posY, float scaleX, float scaleY, float rotation, int r, int g, int b, int a);
```

**Parámetros**

- `binkMovie` (`int`): The movie to be drawn (from [`_SET_BINK_MOVIE`](#setbinkmovie)).
- `posX` (`float`): The centered x position of the movie (0.0 - 1.0).
- `posY` (`float`): The centered y position of the movie (0.0 - 1.0).
- `scaleX` (`float`): The x scale of the movie (0.0 - 1.0).
- `scaleY` (`float`): The y scale of the movie (0.0 - 1.0).
- `rotation` (`float`): The rotation of the movie (0.0 - 360.0).
- `r` (`int`): The red value of the movie (0 - 255).
- `g` (`int`): The green value of the movie (0 - 255).
- `b` (`int`): The blue value of the movie (0 - 255).
- `a` (`int`): The alpha value of the movie (0 - 255).

**Devuelve:** `void`

**Descripción oficial:**

Must be called each frame, will play at specified position on screen when called with [`_PLAY_BINK_MOVIE`](#playbinkmovie)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    local binkint = SetBinkMovie("casino_trailer") -- BINK movie, list can be found at https://gist.github.com/ItsJunction/8046f28c29ea8ff2821e9e4f933f595f
    SetBinkMovieTime(binkint, 0.0) -- Seeks to 0%, just incase of errors.

    while (GetBinkMovieTime(binkint) < 100.0) do
        print(math.floor(GetBinkMovieTime(binkint) * 100)/100 .. "%") -- Prints current playtime (as percentage).
        PlayBinkMovie(binkint)
        DrawBinkMovie(binkint, 0.5, 0.5, 1.0, 1.0, 0.0, 255, 255, 255, 255) -- This example draws and plays in fullscreen in the center (no matter the resolution).
        Citizen.Wait(0)
    end
end)
```

---
### DrawBox

`DRAW_BOX` · hash `0xD3A9971CADAC7252` · jhash `0xCD4D9DD5` · **Cliente**

```lua
DrawBox(x1, y1, z1, x2, y2, z2, red, green, blue, alpha)
```
```c
void DRAW_BOX(float x1, float y1, float z1, float x2, float y2, float z2, int red, int green, int blue, int alpha);
```

**Parámetros**

- `x1` (`float`): The x-coordinate of the first corner of the box.
- `y1` (`float`): The y-coordinate of the first corner of the box.
- `z1` (`float`): The z-coordinate of the first corner of the box.
- `x2` (`float`): The x-coordinate of the opposite corner of the box.
- `y2` (`float`): The y-coordinate of the opposite corner of the box.
- `z2` (`float`): The z-coordinate of the opposite corner of the box.
- `red` (`int`): The red color component of the box (0 - 255).
- `green` (`int`): The green color component of the box (0 - 255).
- `blue` (`int`): The blue color component of the box (0 - 255).
- `alpha` (`int`): The alpha value of the box (0 - 255).

**Devuelve:** `void`

**Descripción oficial:**

This native draws a box between two vectors in the game world. It is typically used for visualizing boundaries or areas of interest. The color of the box is specified by the red, green, and blue parameters, with alpha determining its opacity. This native should be called every frame for continuous rendering.

```
NativeDB Introduced: v323
```

---
### DrawDebugBox

`DRAW_DEBUG_BOX` · hash `0x083A2CA4F2E573BD` · jhash `0x8524A848` · **Cliente**

```lua
DrawDebugBox(x1, y1, z1, x2, y2, z2, r, g, b, a)
```
```c
void DRAW_DEBUG_BOX(float x1, float y1, float z1, float x2, float y2, float z2, int r, int g, int b, int a);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### DrawDebugCross

`DRAW_DEBUG_CROSS` · hash `0x73B1189623049839` · jhash `0xB6DF3709` · **Cliente**

```lua
DrawDebugCross(x, y, z, size, red, green, blue, alpha)
```
```c
void DRAW_DEBUG_CROSS(float x, float y, float z, float size, int red, int green, int blue, int alpha);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `size` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### DrawDebugLine

`DRAW_DEBUG_LINE` · hash `0x7FDFADE676AA3CB0` · jhash `0xABF783AB` · **Cliente**

```lua
DrawDebugLine(x1, y1, z1, x2, y2, z2, r, g, b, a)
```
```c
void DRAW_DEBUG_LINE(float x1, float y1, float z1, float x2, float y2, float z2, int r, int g, int b, int a);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### DrawDebugLineWithTwoColours

`DRAW_DEBUG_LINE_WITH_TWO_COLOURS` · hash `0xD8B9A8AC5608FF94` · jhash `0xE8BFF632` · **Cliente**

```lua
DrawDebugLineWithTwoColours(x1, y1, z1, x2, y2, z2, r1, g1, b1, r2, g2, b2, alpha1, alpha2)
```
```c
void DRAW_DEBUG_LINE_WITH_TWO_COLOURS(float x1, float y1, float z1, float x2, float y2, float z2, int r1, int g1, int b1, int r2, int g2, int b2, int alpha1, int alpha2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `r1` (`int`)
- `g1` (`int`)
- `b1` (`int`)
- `r2` (`int`)
- `g2` (`int`)
- `b2` (`int`)
- `alpha1` (`int`)
- `alpha2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### DrawDebugSphere

`DRAW_DEBUG_SPHERE` · hash `0xAAD68E1AB39DA632` · jhash `0x304D0EEF` · **Cliente**

```lua
DrawDebugSphere(x, y, z, radius, red, green, blue, alpha)
```
```c
void DRAW_DEBUG_SPHERE(float x, float y, float z, float radius, int red, int green, int blue, int alpha);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### DrawDebugText

`DRAW_DEBUG_TEXT` · hash `0x3903E216620488E8` · jhash `0x269B006F` · **Cliente**

```lua
DrawDebugText(text, x, y, z, red, green, blue, alpha)
```
```c
void DRAW_DEBUG_TEXT(char* text, float x, float y, float z, int red, int green, int blue, int alpha);
```

**Parámetros**

- `text` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### DrawDebugText_2d

`DRAW_DEBUG_TEXT_2D` · hash `0xA3BB2E9555C05A8F` · jhash `0x528B973B` · **Cliente**

```lua
DrawDebugText_2d(text, x, y, z, red, green, blue, alpha)
```
```c
void DRAW_DEBUG_TEXT_2D(char* text, float x, float y, float z, int red, int green, int blue, int alpha);
```

**Parámetros**

- `text` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### DrawInteractiveSprite

`_DRAW_INTERACTIVE_SPRITE` · hash `0x2BC54A8188768488` · **Cliente**

```lua
DrawInteractiveSprite(textureDict, textureName, screenX, screenY, width, height, heading, red, green, blue, alpha)
```
```c
void _DRAW_INTERACTIVE_SPRITE(char* textureDict, char* textureName, float screenX, float screenY, float width, float height, float heading, int red, int green, int blue, int alpha);
```

**Parámetros**

- `textureDict` (`char*`): Name of texture dictionary to load texture from
- `textureName` (`char*`): Name of texture to load from texture dictionary
- `screenX` (`float`): Screen X
- `screenY` (`float`): Screen Y
- `width` (`float`): Scale X
- `height` (`float`): Scale Y
- `heading` (`float`): Texture rotation in degrees (default = 0.0) positive is clockwise, measured in degrees
- `red` (`int`): Color
- `green` (`int`): Color
- `blue` (`int`): Color
- `alpha` (`int`): Opacity level

**Devuelve:** `void`

**Descripción oficial:**

Similar to [\_DRAW_SPRITE](#drawsprite), but seems to be some kind of "interactive" sprite, at least used by render targets.
These seem to be the only dicts ever requested by this native:

```
prop_screen_biker_laptop
Prop_Screen_GR_Disruption
Prop_Screen_TaleOfUs
prop_screen_nightclub
Prop_Screen_IE_Adhawk
prop_screen_sm_free_trade_shipping
prop_screen_hacker_truck
MPDesktop
Prop_Screen_Nightclub
And a few others
```

**Nombres antiguos (alias):** `0x2BC54A8188768488` (`N_0x2bc54a8188768488`)

---
### DrawLightWithRange

`DRAW_LIGHT_WITH_RANGE` · hash `0xF2A1B2771A01DBD4` · jhash `0x6A396E9A` · **Cliente**

```lua
DrawLightWithRange(posX, posY, posZ, colorR, colorG, colorB, range, intensity)
```
```c
void DRAW_LIGHT_WITH_RANGE(float posX, float posY, float posZ, int colorR, int colorG, int colorB, float range, float intensity);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `colorR` (`int`)
- `colorG` (`int`)
- `colorB` (`int`)
- `range` (`float`)
- `intensity` (`float`)

**Devuelve:** `void`

---
### DrawLightWithRangeAndShadow

`_DRAW_LIGHT_WITH_RANGE_AND_SHADOW` · hash `0xF49E9A9716A04595` · **Cliente**

```lua
DrawLightWithRangeAndShadow(x, y, z, r, g, b, range, intensity, shadow)
```
```c
void _DRAW_LIGHT_WITH_RANGE_AND_SHADOW(float x, float y, float z, int r, int g, int b, float range, float intensity, float shadow);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `range` (`float`)
- `intensity` (`float`)
- `shadow` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_DRAW_LIGHT_WITH_RANGE_WITH_SHADOW` (`DrawLightWithRangeWithShadow`)

---
### DrawLine

`DRAW_LINE` · hash `0x6B7256074AE34680` · jhash `0xB3426BCC` · **Cliente**

```lua
DrawLine(x1, y1, z1, x2, y2, z2, red, green, blue, alpha)
```
```c
void DRAW_LINE(float x1, float y1, float z1, float x2, float y2, float z2, int red, int green, int blue, int alpha);
```

**Parámetros**

- `x1` (`float`): The x-coordinate of the starting point of the line.
- `y1` (`float`): The y-coordinate of the starting point of the line.
- `z1` (`float`): The z-coordinate of the starting point of the line.
- `x2` (`float`): The x-coordinate of the ending point of the line.
- `y2` (`float`): The y-coordinate of the ending point of the line.
- `z2` (`float`): The z-coordinate of the ending point of the line.
- `red` (`int`): The red color component of the line (0 - 255).
- `green` (`int`): The green color component of the line (0 - 255).
- `blue` (`int`): The blue color component of the line (0 - 255).
- `alpha` (`int`): The alpha value of the line (0 - 255).

**Devuelve:** `void`

**Descripción oficial:**

This native draws a line between two vectors in the game world. It is typically used for visualizing paths or connections between points. The color of the line is specified by the red, green, and blue parameters, with alpha determining its opacity. This native should be called every frame for continuous rendering.

```
NativeDB Introduced: v323
```

---
### DrawLowQualityPhotoToPhone

`DRAW_LOW_QUALITY_PHOTO_TO_PHONE` · hash `0x1072F115DAB0717E` · jhash `0xE9F2B68F` · **Cliente**

```lua
DrawLowQualityPhotoToPhone(p0, p1)
```
```c
void DRAW_LOW_QUALITY_PHOTO_TO_PHONE(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1072F115DAB0717E` (`N_0x1072f115dab0717e`)

---
### DrawMarker

`DRAW_MARKER` · hash `0x28477EC23D892089` · jhash `0x48D84A02` · **Cliente**

```lua
DrawMarker(type, posX, posY, posZ, dirX, dirY, dirZ, rotX, rotY, rotZ, scaleX, scaleY, scaleZ, red, green, blue, alpha, bobUpAndDown, faceCamera, rotationOrder, rotate, textureDict, textureName, drawOnEnts)
```
```c
void DRAW_MARKER(int type, float posX, float posY, float posZ, float dirX, float dirY, float dirZ, float rotX, float rotY, float rotZ, float scaleX, float scaleY, float scaleZ, int red, int green, int blue, int alpha, BOOL bobUpAndDown, BOOL faceCamera, int rotationOrder, BOOL rotate, char* textureDict, char* textureName, BOOL drawOnEnts);
```

**Parámetros**

- `type` (`int`): The marker type to draw.
- `posX` (`float`): The X coordinate to draw the marker at.
- `posY` (`float`): The Y coordinate to draw the marker at.
- `posZ` (`float`): The Z coordinate to draw the marker at.
- `dirX` (`float`): The X component of the direction vector for the marker, or 0.0 to use rotX/Y/Z.
- `dirY` (`float`): The Y component of the direction vector for the marker, or 0.0 to use rotX/Y/Z.
- `dirZ` (`float`): The Z component of the direction vector for the marker, or 0.0 to use rotX/Y/Z.
- `rotX` (`float`): The X rotation for the marker. Only used if the direction vector is 0.0.
- `rotY` (`float`): The Y rotation for the marker. Only used if the direction vector is 0.0.
- `rotZ` (`float`): The Z rotation for the marker. Only used if the direction vector is 0.0.
- `scaleX` (`float`): The scale for the marker on the X axis.
- `scaleY` (`float`): The scale for the marker on the Y axis.
- `scaleZ` (`float`): The scale for the marker on the Z axis.
- `red` (`int`): The red component of the marker color, on a scale from 0-255.
- `green` (`int`): The green component of the marker color, on a scale from 0-255.
- `blue` (`int`): The blue component of the marker color, on a scale from 0-255.
- `alpha` (`int`): The alpha component of the marker color, on a scale from 0-255.
- `bobUpAndDown` (`BOOL`): Whether or not the marker should slowly animate up/down.
- `faceCamera` (`BOOL`): Whether the marker should be a 'billboard', as in, should constantly face the camera.
- `rotationOrder` (`int`): The order yaw, pitch and roll is applied. Usually `2`.
- `rotate` (`BOOL`): Rotations only apply to the heading.
- `textureDict` (`char*`): A texture dictionary to draw the marker with, or NULL. Example: 'GolfPutting'
- `textureName` (`char*`): A texture name in `textureDict` to draw the marker with, or NULL. Example: 'PuttingMarker'
- `drawOnEnts` (`BOOL`): Whether or not the marker should draw on intersecting entities.

**Devuelve:** `void`

**Descripción oficial:**

Draws a marker with the specified appearance at the target location. This has to be called every frame, e.g. in a `Wait(0)` loop.

There's a [list of markers](https://docs.fivem.net/docs/game-references/markers/) on the FiveM documentation site.

**Ejemplo (lua):**

```lua
CreateThread(function()
	while true do
		-- draw every frame
		Wait(0)

		local pedCoords = GetEntityCoords(PlayerPedId())
		DrawMarker(2, pedCoords.x, pedCoords.y, pedCoords.z + 2, 0.0, 0.0, 0.0, 0.0, 180.0, 0.0, 2.0, 2.0, 2.0, 255, 128, 0, 50, false, true, 2, nil, nil, false)
	end
end)
```

---
### DrawMarker_2

`_DRAW_MARKER_2` · hash `0xE82728F0DE75D13A` · **Cliente**

```lua
DrawMarker_2(type, posX, posY, posZ, dirX, dirY, dirZ, rotX, rotY, rotZ, scaleX, scaleY, scaleZ, red, green, blue, alpha, bobUpAndDown, faceCamera, rotationOrder, rotate, textureDict, textureName, drawOnEnts, p24)
```
```c
void _DRAW_MARKER_2(int type, float posX, float posY, float posZ, float dirX, float dirY, float dirZ, float rotX, float rotY, float rotZ, float scaleX, float scaleY, float scaleZ, int red, int green, int blue, int alpha, BOOL bobUpAndDown, BOOL faceCamera, int rotationOrder, BOOL rotate, char* textureDict, char* textureName, BOOL drawOnEnts, BOOL p24);
```

**Parámetros**

- `type` (`int`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `dirX` (`float`)
- `dirY` (`float`)
- `dirZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `scaleX` (`float`)
- `scaleY` (`float`)
- `scaleZ` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)
- `bobUpAndDown` (`BOOL`)
- `faceCamera` (`BOOL`)
- `rotationOrder` (`int`)
- `rotate` (`BOOL`)
- `textureDict` (`char*`)
- `textureName` (`char*`)
- `drawOnEnts` (`BOOL`)
- `p24` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 26: BOOL p25
```

**Nombres antiguos (alias):** `0xE82728F0DE75D13A` (`N_0xe82728f0de75d13a`)

---
### DrawPoly

`DRAW_POLY` · hash `0xAC26716048436851` · jhash `0xABD19253` · **Cliente**

```lua
DrawPoly(x1, y1, z1, x2, y2, z2, x3, y3, z3, red, green, blue, alpha)
```
```c
void DRAW_POLY(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3, int red, int green, int blue, int alpha);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `x3` (`float`)
- `y3` (`float`)
- `z3` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
x/y/z - Location of a vertex (in world coords), presumably.  
----------------  
x1, y1, z1     : Coordinates for the first point  
x2, y2, z2     : Coordinates for the second point  
x3, y3, z3     : Coordinates for the third point  
r, g, b, alpha : Color with RGBA-Values  
Keep in mind that only one side of the drawn triangle is visible: It's the side, in which the vector-product of the vectors heads to: (b-a)x(c-a) Or (b-a)x(c-b).  
But be aware: The function seems to work somehow differently. I have trouble having them drawn in rotated orientation. Try it yourself and if you somehow succeed, please edit this and post your solution.  
I recommend using a predefined function to call this.  
[VB.NET]  
Public Sub DrawPoly(a As Vector3, b As Vector3, c As Vector3, col As Color)  
    [Function].Call(Hash.DRAW_POLY, a.X, a.Y, a.Z, b.X, b.Y, b.Z, c.X, c.Y, c.Z, col.R, col.G, col.B, col.A)  
End Sub  
[C#]  
public void DrawPoly(Vector3 a, Vector3 b, Vector3 c, Color col)  
{  
    Function.Call(Hash.DRAW_POLY, a.X, a.Y, a.Z, b.X, b.Y, b.Z, c.X, c.Y, c.Z, col.R, col.G, col.B, col.A);  
}  
BTW: Intersecting triangles are not supported: They overlap in the order they were called.  
```

---
### DrawRect

`DRAW_RECT` · hash `0x3A618A217E5154F0` · jhash `0xDD2BFC77` · **Cliente**

```lua
DrawRect(x, y, width, height, r, g, b, a)
```
```c
void DRAW_RECT(float x, float y, float width, float height, int r, int g, int b, int a);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `width` (`float`)
- `height` (`float`)
- `r` (`int`)
- `g` (`int`)
- `b` (`int`)
- `a` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Draws a rectangle on the screen.  
-x: The relative X point of the center of the rectangle. (0.0-1.0, 0.0 is the left edge of the screen, 1.0 is the right edge of the screen)  
-y: The relative Y point of the center of the rectangle. (0.0-1.0, 0.0 is the top edge of the screen, 1.0 is the bottom edge of the screen)  
-width: The relative width of the rectangle. (0.0-1.0, 1.0 means the whole screen width)  
-height: The relative height of the rectangle. (0.0-1.0, 1.0 means the whole screen height)  
-R: Red part of the color. (0-255)  
-G: Green part of the color. (0-255)  
-B: Blue part of the color. (0-255)  
-A: Alpha part of the color. (0-255, 0 means totally transparent, 255 means totally opaque)  
The total number of rectangles to be drawn in one frame is apparently limited to 399.  
```

```
NativeDB Added Parameter 9: BOOL p8
```

---
### DrawScaleformMovie

`DRAW_SCALEFORM_MOVIE` · hash `0x54972ADAF0294A93` · jhash `0x48DA6A58` · **Cliente**

```lua
DrawScaleformMovie(scaleformHandle, x, y, width, height, red, green, blue, alpha, unk)
```
```c
void DRAW_SCALEFORM_MOVIE(int scaleformHandle, float x, float y, float width, float height, int red, int green, int blue, int alpha, int unk);
```

**Parámetros**

- `scaleformHandle` (`int`)
- `x` (`float`)
- `y` (`float`)
- `width` (`float`)
- `height` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)
- `unk` (`int`)

**Devuelve:** `void`

---
### DrawScaleformMovieFullscreen

`DRAW_SCALEFORM_MOVIE_FULLSCREEN` · hash `0x0DF606929C105BE1` · jhash `0x7B48E696` · **Cliente**

```lua
DrawScaleformMovieFullscreen(scaleform, red, green, blue, alpha, unk)
```
```c
void DRAW_SCALEFORM_MOVIE_FULLSCREEN(int scaleform, int red, int green, int blue, int alpha, int unk);
```

**Parámetros**

- `scaleform` (`int`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)
- `unk` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
unk is not used so no need  
```

---
### DrawScaleformMovieFullscreenMasked

`DRAW_SCALEFORM_MOVIE_FULLSCREEN_MASKED` · hash `0xCF537FDE4FBD4CE5` · jhash `0x9C59FC06` · **Cliente**

```lua
DrawScaleformMovieFullscreenMasked(scaleform1, scaleform2, red, green, blue, alpha)
```
```c
void DRAW_SCALEFORM_MOVIE_FULLSCREEN_MASKED(int scaleform1, int scaleform2, int red, int green, int blue, int alpha);
```

**Parámetros**

- `scaleform1` (`int`)
- `scaleform2` (`int`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

---
### DrawScaleformMovie_3d

`DRAW_SCALEFORM_MOVIE_3D` · hash `0x87D51D72255D4E78` · jhash `0xC4F63A89` · **Cliente**

```lua
DrawScaleformMovie_3d(scaleform, posX, posY, posZ, rotX, rotY, rotZ, p7, sharpness, p9, scaleX, scaleY, scaleZ, p13)
```
```c
void DRAW_SCALEFORM_MOVIE_3D(int scaleform, float posX, float posY, float posZ, float rotX, float rotY, float rotZ, float p7, float sharpness, float p9, float scaleX, float scaleY, float scaleZ, Any p13);
```

**Parámetros**

- `scaleform` (`int`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `p7` (`float`)
- `sharpness` (`float`)
- `p9` (`float`)
- `scaleX` (`float`)
- `scaleY` (`float`)
- `scaleZ` (`float`)
- `p13` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x87D51D72255D4E78` (`N_0x87d51d72255d4e78`)

---
### DrawScaleformMovie_3dSolid

`DRAW_SCALEFORM_MOVIE_3D_SOLID` · hash `0x1CE592FDC749D6F5` · jhash `0x899933C8` · **Cliente**

```lua
DrawScaleformMovie_3dSolid(scaleform, posX, posY, posZ, rotX, rotY, rotZ, p7, p8, p9, scaleX, scaleY, scaleZ, p13)
```
```c
void DRAW_SCALEFORM_MOVIE_3D_SOLID(int scaleform, float posX, float posY, float posZ, float rotX, float rotY, float rotZ, float p7, float p8, float p9, float scaleX, float scaleY, float scaleZ, Any p13);
```

**Parámetros**

- `scaleform` (`int`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `p7` (`float`)
- `p8` (`float`)
- `p9` (`float`)
- `scaleX` (`float`)
- `scaleY` (`float`)
- `scaleZ` (`float`)
- `p13` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1CE592FDC749D6F5` (`N_0x1ce592fdc749d6f5`), `_DRAW_SCALEFORM_MOVIE_3D_NON_ADDITIVE` (`DrawScaleformMovie_3dNonAdditive`)

---
### DrawShowroom

`_DRAW_SHOWROOM` · hash `0x98C4FE6EC34154CA` · jhash `0x9A0E3BFE` · **Cliente**

```lua
local retval = DrawShowroom(p0, ped, p2, posX, posY, posZ)
```
```c
BOOL _DRAW_SHOWROOM(char* p0, Ped ped, int p2, float posX, float posY, float posZ);
```

**Parámetros**

- `p0` (`char*`)
- `ped` (`Ped`)
- `p2` (`int`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
It's called after 0xD3A10FC7FD8D98CD and 0xF1CEA8A4198D8E9A  
p0 was always "CELEBRATION_WINNER"  
```

**Nombres antiguos (alias):** `0x98C4FE6EC34154CA` (`N_0x98c4fe6ec34154ca`)

---
### DrawSphere

`_DRAW_SPHERE` · hash `0x799017F9E3B10112` · **Cliente**

```lua
DrawSphere(x, y, z, radius, r, g, b, opacity)
```
```c
void _DRAW_SPHERE(float x, float y, float z, float radius, int r, int g, int b, float opacity);
```

**Parámetros**

- `x` (`float`): X coordinate of the sphere
- `y` (`float`): Y coordinate of the sphere
- `z` (`float`): Z coordinate of the sphere
- `radius` (`float`): Size of the sphere, `1.0` = 1 meter
- `r` (`int`): Color red `0`-`255`
- `g` (`int`): Color green `0`-`255`
- `b` (`int`): Color blue `0`-`255`
- `opacity` (`float`): Opacity from `0.0`-`1.0`

**Devuelve:** `void`

**Descripción oficial:**

Draws a 3D sphere, typically seen in the GTA:O freemode event "Penned In".

Example:
![](https://i.imgur.com/nCbtS4H.png)

```lua
DrawSphere(35.45, 172.66, 126.22, 1.0, 0, 0, 255, 0.2)
```

**Nombres antiguos (alias):** `0x799017F9E3B10112` (`N_0x799017f9e3b10112`)

---
### DrawSpotLight

`DRAW_SPOT_LIGHT` · hash `0xD0F64B265C8C8B33` · jhash `0xBDBC410C` · **Cliente**

```lua
DrawSpotLight(posX, posY, posZ, dirX, dirY, dirZ, colorR, colorG, colorB, distance, brightness, hardness, radius, falloff)
```
```c
void DRAW_SPOT_LIGHT(float posX, float posY, float posZ, float dirX, float dirY, float dirZ, int colorR, int colorG, int colorB, float distance, float brightness, float hardness, float radius, float falloff);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `dirX` (`float`)
- `dirY` (`float`)
- `dirZ` (`float`)
- `colorR` (`int`)
- `colorG` (`int`)
- `colorB` (`int`)
- `distance` (`float`)
- `brightness` (`float`)
- `hardness` (`float`)
- `radius` (`float`)
- `falloff` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Parameters:  
* pos - coordinate where the spotlight is located  
* dir - the direction vector the spotlight should aim at from its current position  
* r,g,b - color of the spotlight  
* distance - the maximum distance the light can reach  
* brightness - the brightness of the light  
* roundness - "smoothness" of the circle edge  
* radius - the radius size of the spotlight  
* falloff - the falloff size of the light's edge
Example in C# (spotlight aims at the closest vehicle):  
Vector3 myPos = Game.Player.Character.Position;  
Vehicle nearest = World.GetClosestVehicle(myPos , 1000f);  
Vector3 destinationCoords = nearest.Position;  
Vector3 dirVector = destinationCoords - myPos;  
dirVector.Normalize();  
Function.Call(Hash.DRAW_SPOT_LIGHT, pos.X, pos.Y, pos.Z, dirVector.X, dirVector.Y, dirVector.Z, 255, 255, 255, 100.0f, 1f, 0.0f, 13.0f, 1f);  
```

---
### DrawSpotLightWithShadow

`_DRAW_SPOT_LIGHT_WITH_SHADOW` · hash `0x5BCA583A583194DB` · jhash `0x32BF9598` · **Cliente**

```lua
DrawSpotLightWithShadow(posX, posY, posZ, dirX, dirY, dirZ, colorR, colorG, colorB, distance, brightness, roundness, radius, falloff, shadowId)
```
```c
void _DRAW_SPOT_LIGHT_WITH_SHADOW(float posX, float posY, float posZ, float dirX, float dirY, float dirZ, int colorR, int colorG, int colorB, float distance, float brightness, float roundness, float radius, float falloff, int shadowId);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `dirX` (`float`)
- `dirY` (`float`)
- `dirZ` (`float`)
- `colorR` (`int`)
- `colorG` (`int`)
- `colorB` (`int`)
- `distance` (`float`)
- `brightness` (`float`)
- `roundness` (`float`)
- `radius` (`float`)
- `falloff` (`float`)
- `shadowId` (`int`)

**Devuelve:** `void`

---
### DrawSprite

`DRAW_SPRITE` · hash `0xE7FFAE5EBF23D890` · jhash `0x1FEC16B0` · **Cliente**

```lua
DrawSprite(textureDict, textureName, screenX, screenY, width, height, heading, red, green, blue, alpha)
```
```c
void DRAW_SPRITE(char* textureDict, char* textureName, float screenX, float screenY, float width, float height, float heading, int red, int green, int blue, int alpha);
```

**Parámetros**

- `textureDict` (`char*`)
- `textureName` (`char*`)
- `screenX` (`float`)
- `screenY` (`float`)
- `width` (`float`)
- `height` (`float`)
- `heading` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Draws a 2D sprite on the screen.  
Parameters:  
textureDict - Name of texture dictionary to load texture from (e.g. "CommonMenu", "MPWeaponsCommon", etc.)  
textureName - Name of texture to load from texture dictionary (e.g. "last_team_standing_icon", "tennis_icon", etc.)  
screenX/Y - Screen offset (0.5 = center)  
scaleX/Y - Texture scaling. Negative values can be used to flip the texture on that axis. (0.5 = half)  
heading - Texture rotation in degrees (default = 0.0) positive is clockwise, measured in degrees  
red,green,blue - Sprite color (default = 255/255/255)  
alpha - opacity level  
```

```
NativeDB Added Parameter 12: BOOL p11
```

---
### DrawSpritePoly_2

`_DRAW_SPRITE_POLY_2` · hash `0x736D7AA1B750856B` · **Cliente**

```lua
DrawSpritePoly_2(x1, y1, z1, x2, y2, z2, x3, y3, z3, red1, green1, blue1, alpha1, red2, green2, blue2, alpha2, red3, green3, blue3, alpha3, textureDict, textureName, u1, v1, w1, u2, v2, w2, u3, v3, w3)
```
```c
void _DRAW_SPRITE_POLY_2(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3, float red1, float green1, float blue1, int alpha1, float red2, float green2, float blue2, int alpha2, float red3, float green3, float blue3, int alpha3, char* textureDict, char* textureName, float u1, float v1, float w1, float u2, float v2, float w2, float u3, float v3, float w3);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `x3` (`float`)
- `y3` (`float`)
- `z3` (`float`)
- `red1` (`float`)
- `green1` (`float`)
- `blue1` (`float`)
- `alpha1` (`int`)
- `red2` (`float`)
- `green2` (`float`)
- `blue2` (`float`)
- `alpha2` (`int`)
- `red3` (`float`)
- `green3` (`float`)
- `blue3` (`float`)
- `alpha3` (`int`)
- `textureDict` (`char*`)
- `textureName` (`char*`)
- `u1` (`float`)
- `v1` (`float`)
- `w1` (`float`)
- `u2` (`float`)
- `v2` (`float`)
- `w2` (`float`)
- `u3` (`float`)
- `v3` (`float`)
- `w3` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Used for drawling Deadline trailing lights, see deadline.ytd

Each vertex has its own colour that is blended/illuminated on the texture. Additionally, the R, G, and B components are floats that are int-casted internally.

For UVW mapping (u,v,w parameters), reference your favourite internet resource for more details.

**Nombres antiguos (alias):** `0x736D7AA1B750856B` (`N_0x736d7aa1b750856b`)

---
### DrawSpriteUv

`_DRAW_SPRITE_UV` · hash `0x95812F9B26074726` · **Cliente**

```lua
DrawSpriteUv(textureDict, textureName, x, y, width, height, u1, v1, u2, v2, heading, red, green, blue, alpha)
```
```c
void _DRAW_SPRITE_UV(char* textureDict, char* textureName, float x, float y, float width, float height, float u1, float v1, float u2, float v2, float heading, int red, int green, int blue, int alpha);
```

**Parámetros**

- `textureDict` (`char*`)
- `textureName` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `width` (`float`)
- `height` (`float`)
- `u1` (`float`)
- `v1` (`float`)
- `u2` (`float`)
- `v2` (`float`)
- `heading` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Similar to DRAW_SPRITE, but allows to specify the texture coordinates used to draw the sprite.
u1, v1 - texture coordinates for the top-left corner
u2, v2 - texture coordinates for the bottom-right corner

```
NativeDB Introduced: v1868
```

---
### DrawTexturedPoly

`DRAW_TEXTURED_POLY` · hash `0x29280002282F1928` · **Cliente**

```lua
DrawTexturedPoly(x1, y1, z1, x2, y2, z2, x3, y3, z3, red, green, blue, alpha, textureDict, textureName, u1, v1, w1, u2, v2, w2, u3, v3, w3)
```
```c
void DRAW_TEXTURED_POLY(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3, int red, int green, int blue, int alpha, char* textureDict, char* textureName, float u1, float v1, float w1, float u2, float v2, float w2, float u3, float v3, float w3);
```

**Parámetros**

- `x1` (`float`): The x-coordinate of the first vector.
- `y1` (`float`): The y-coordinate of the first vector.
- `z1` (`float`): The z-coordinate of the first vector.
- `x2` (`float`): The x-coordinate of the second vector.
- `y2` (`float`): The y-coordinate of the second vector.
- `z2` (`float`): The z-coordinate of the second vector.
- `x3` (`float`): The x-coordinate of the third vector.
- `y3` (`float`): The y-coordinate of the third vector.
- `z3` (`float`): The z-coordinate of the third vector.
- `red` (`int`): The red color component of the polygon (0 - 255).
- `green` (`int`): The green color component of the polygon (0 - 255).
- `blue` (`int`): The blue color component of the polygon (0 - 255).
- `alpha` (`int`): The alpha value of the polygon (0 - 255).
- `textureDict` (`char*`): The name of the texture dictionary.
- `textureName` (`char*`): The name of the texture.
- `u1` (`float`): The u-coordinate of the first UV mapping.
- `v1` (`float`): The v-coordinate of the first UV mapping.
- `w1` (`float`): The w-coordinate of the first UV mapping.
- `u2` (`float`): The u-coordinate of the second UV mapping.
- `v2` (`float`): The v-coordinate of the second UV mapping.
- `w2` (`float`): The w-coordinate of the second UV mapping.
- `u3` (`float`): The u-coordinate of the third UV mapping.
- `v3` (`float`): The v-coordinate of the third UV mapping.
- `w3` (`float`): The w-coordinate of the third UV mapping.

**Devuelve:** `void`

**Descripción oficial:**

This native draws a textured polygon between three vectors in the game world. It's commonly utilized for rendering deadline trailing lights, with additional details available in the `deadline.ytd` file. UVW mapping details (u,v,w parameters) can be found on various internet resources. This native is specifically used for drawing textured polygons on the screen, where UV coordinates define the texture mapping and color/alpha parameters define the appearance of the polygon. This native should be called every frame for continuous rendering.

```
NativeDB Introduced: v877
```

**Nombres antiguos (alias):** `0x29280002282F1928` (`N_0x29280002282f1928`), `_DRAW_SPRITE_POLY` (`DrawSpritePoly`)

---
### DrawTvChannel

`DRAW_TV_CHANNEL` · hash `0xFDDC2B4ED3C69DF0` · jhash `0x8129EF89` · **Cliente**

```lua
DrawTvChannel(xPos, yPos, xScale, yScale, rotation, red, green, blue, alpha)
```
```c
void DRAW_TV_CHANNEL(float xPos, float yPos, float xScale, float yScale, float rotation, int red, int green, int blue, int alpha);
```

**Parámetros**

- `xPos` (`float`)
- `yPos` (`float`)
- `xScale` (`float`)
- `yScale` (`float`)
- `rotation` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
All calls to this native are preceded by calls to GRAPHICS::_0x61BB1D9B3A95D802 and GRAPHICS::_0xC6372ECD45D73BCD, respectively.
"act_cinema.ysc", line 1483:
HUD::SET_HUD_COMPONENT_POSITION(15, 0.0, -0.0375);
HUD::SET_TEXT_RENDER_ID(l_AE);
GRAPHICS::_0x61BB1D9B3A95D802(4);
GRAPHICS::_0xC6372ECD45D73BCD(1);
if (GRAPHICS::_0x0AD973CA1E077B60(${movie_arthouse})) {
    GRAPHICS::DRAW_TV_CHANNEL(0.5, 0.5, 0.7375, 1.0, 0.0, 255, 255, 255, 255);
} else {
    GRAPHICS::DRAW_TV_CHANNEL(0.5, 0.5, 1.0, 1.0, 0.0, 255, 255, 255, 255);
}
"am_mp_property_int.ysc", line 102545:
if (ENTITY::DOES_ENTITY_EXIST(a_2._f3)) {
    if (HUD::IS_NAMED_RENDERTARGET_LINKED(ENTITY::GET_ENTITY_MODEL(a_2._f3))) {
        HUD::SET_TEXT_RENDER_ID(a_2._f1);
        GRAPHICS::_0x61BB1D9B3A95D802(4);
        GRAPHICS::_0xC6372ECD45D73BCD(1);
        GRAPHICS::DRAW_TV_CHANNEL(0.5, 0.5, 1.0, 1.0, 0.0, 255, 255, 255, 255);
        if (GRAPHICS::GET_TV_CHANNEL() == -1) {
            sub_a8fa5(a_2, 1);
        } else {
            sub_a8fa5(a_2, 1);
            GRAPHICS::ATTACH_TV_AUDIO_TO_ENTITY(a_2._f3);
        }
        HUD::SET_TEXT_RENDER_ID(HUD::GET_DEFAULT_SCRIPT_RENDERTARGET_RENDER_ID());
    }
}
```

---
### EnableAlienBloodVfx

`ENABLE_ALIEN_BLOOD_VFX` · hash `0x9DCE1F0F78260875` · jhash `0xCE8B8748` · **Cliente**

```lua
EnableAlienBloodVfx(toggle)
```
```c
void ENABLE_ALIEN_BLOOD_VFX(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Creates a motion-blur sort of effect, this native does not seem to work, however by using the [`ANIMPOSTFX_PLAY`](#animpostfxplay) native with `"DrugsMichaelAliensFight"` as the effect parameter, you should be able to get the effect.

This native does not seem to work, however by using the [ANIMPOSTFX_PLAY](#animpostfxplay) native with "DrugsMichaelAliensFight" as the effect parameter, you should be able to get the effect.

**Nombres antiguos (alias):** `0x9DCE1F0F78260875` (`N_0x9dce1f0f78260875`)

---
### EnableClownBloodVfx

`ENABLE_CLOWN_BLOOD_VFX` · hash `0xD821490579791273` · jhash `0xC61C75E9` · **Cliente**

```lua
EnableClownBloodVfx(toggle)
```
```c
void ENABLE_CLOWN_BLOOD_VFX(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Whether to toggle the clown VFX on or off.

**Devuelve:** `void`

**Descripción oficial:**

If true, this native will create purple explosions upon projectile impact, add comic-like PTFX when firing a weapon, create a sound on bullet impact and have its own "blood effect".

If the PTFX asset "scr_rcbarry2" is not requested using ([`RequestNamedPtfxAsset`](#enableclownbloodvfx)) then this native **will not work as intended**.

Excerpt from fm_content_drug_lab_work.c:

```
STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_rcbarry2");
if (STREAMING::HAS_NAMED_PTFX_ASSET_LOADED("scr_rcbarry2"))
{
  GRAPHICS::ENABLE_CLOWN_BLOOD_VFX(true);
  AUDIO::START_AUDIO_SCENE("DLC_CM2022_DRUG_TRIP_SPRINKLERS_SCENE");
  func_720(26);
}
```

**Nombres antiguos (alias):** `SET_CAMERA_ENDTIME` (`SetCameraEndtime`)

**Ejemplo (lua):**

```lua
RequestNamedPtfxAsset("scr_rcbarry2") -- Request the PTFX
while not HasNamedPtfxAssetLoaded("scr_rcbarry2") do
  Citizen.Wait(0)
end
EnableClownBloodVfx(true) -- Enable the clown PTFX
```

---
### EnableMoonCycleOverride

`ENABLE_MOON_CYCLE_OVERRIDE` · hash `0x2C328AF17210F009` · **Cliente**

```lua
EnableMoonCycleOverride(phase)
```
```c
void ENABLE_MOON_CYCLE_OVERRIDE(float phase);
```

**Parámetros**

- `phase` (`float`): A value indicating the moon cycle.

**Devuelve:** `void`

**Descripción oficial:**

Enable a custom moon cycle, allowing control of which lunar phase the moon is in.

Valid values are from `0.0` to `1.0`, with `0.5` representing a full moon.

| Value |   Lunar Phase   |
| :---: | :-------------: |
| `0.1` | Waxing Crescent |
| `0.2` |  First Quarter  |
| `0.3` | Waxing Gibbous  |
| `0.5` |    Full Moon    |
| `0.7` | Waning Gibbous  |
| `0.8` |  Third Quarter  |
| `0.9` | Waning Crescent |

The moon phase can be disabled with [DISABLE_MOON_CYCLE_OVERRIDE](#disablemooncycleoverride)

**Nombres antiguos (alias):** `0x2C328AF17210F009` (`N_0x2c328af17210f009`), `_SET_EXTRA_TIMECYCLE_MODIFIER_STRENGTH` (`SetExtraTimecycleModifierStrength`)

**Ejemplo (lua):**

```lua
EnableMoonCycleOverride(0.5)
```

---
### EnableMovieKeyframeWait

`ENABLE_MOVIE_KEYFRAME_WAIT` · hash `0x74C180030FDE4B69` · jhash `0x796DE696` · **Cliente**

```lua
EnableMovieKeyframeWait(toggle)
```
```c
void ENABLE_MOVIE_KEYFRAME_WAIT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x74C180030FDE4B69` (`N_0x74c180030fde4b69`)

---
### EnableMovieSubtitles

`ENABLE_MOVIE_SUBTITLES` · hash `0x873FA65C778AD970` · jhash `0xC2DEBA3D` · **Cliente**

```lua
EnableMovieSubtitles(toggle)
```
```c
void ENABLE_MOVIE_SUBTITLES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### EndPetrolTrailDecals

`END_PETROL_TRAIL_DECALS` · hash `0x0A123435A26C36CD` · jhash `0xCCCA6855` · **Cliente**

```lua
EndPetrolTrailDecals()
```
```c
void END_PETROL_TRAIL_DECALS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0A123435A26C36CD` (`N_0x0a123435a26c36cd`)

---
### EndScaleformMovieMethod

`END_SCALEFORM_MOVIE_METHOD` · hash `0xC6796A8FFA375E53` · jhash `0x02DBF2D7` · **Cliente**

```lua
EndScaleformMovieMethod()
```
```c
void END_SCALEFORM_MOVIE_METHOD();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Pops and calls the Scaleform function on the stack  
```

**Nombres antiguos (alias):** `_POP_SCALEFORM_MOVIE_FUNCTION_VOID` (`PopScaleformMovieFunctionVoid`)

---
### EndScaleformMovieMethodReturnValue

`END_SCALEFORM_MOVIE_METHOD_RETURN_VALUE` · hash `0xC50AA39A577AF886` · jhash `0x2F38B526` · **Cliente**

```lua
local retval = EndScaleformMovieMethodReturnValue()
```
```c
int END_SCALEFORM_MOVIE_METHOD_RETURN_VALUE();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `_POP_SCALEFORM_MOVIE_FUNCTION` (`PopScaleformMovieFunction`), `_END_SCALEFORM_MOVIE_METHOD_RETURN` (`EndScaleformMovieMethodReturn`)

---
### EndTextCommandScaleformString

`END_TEXT_COMMAND_SCALEFORM_STRING` · hash `0x362E2D3FE93A9959` · jhash `0x386CE0B8` · **Cliente**

```lua
EndTextCommandScaleformString()
```
```c
void END_TEXT_COMMAND_SCALEFORM_STRING();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `_END_TEXT_COMPONENT` (`EndTextComponent`)

---
### EndTextCommandUnparsedScaleformString

`END_TEXT_COMMAND_UNPARSED_SCALEFORM_STRING` · hash `0xAE4E8157D9ECF087` · jhash `0x2E80DB52` · **Cliente**

```lua
EndTextCommandUnparsedScaleformString()
```
```c
void END_TEXT_COMMAND_UNPARSED_SCALEFORM_STRING();
```

**Devuelve:** `void`

**Descripción oficial:**

Same as END_TEXT_COMMAND_SCALEFORM_STRING but does not perform HTML conversion for text tokens.
Also useful for when you are trying to add blips and inputs in your scaleform (If the scaleform supports it).

**Nombres antiguos (alias):** `0xAE4E8157D9ECF087` (`N_0xae4e8157d9ecf087`), `_END_TEXT_COMMAND_SCALEFORM_STRING_2` (`EndTextCommandScaleformString_2`)

---
### FadeDecalsInRange

`FADE_DECALS_IN_RANGE` · hash `0xD77EDADB0420E6E0` · jhash `0xF81E884A` · **Cliente**

```lua
FadeDecalsInRange(x, y, z, radius, duration)
```
```c
void FADE_DECALS_IN_RANGE(float x, float y, float z, float radius, float duration);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `duration` (`float`): A duration in seconds.

**Devuelve:** `void`

---
### FadeUpPedLight

`FADE_UP_PED_LIGHT` · hash `0xC9B18B4619F48F7B` · jhash `0x93628786` · **Cliente**

```lua
FadeUpPedLight(p0)
```
```c
void FADE_UP_PED_LIGHT(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC9B18B4619F48F7B` (`N_0xc9b18b4619f48f7b`)

---
### ForceRenderInGameUi

`FORCE_RENDER_IN_GAME_UI` · hash `0xDC459CFA0CCE245B` · jhash `0x7E946E87` · **Cliente**

```lua
ForceRenderInGameUi(toggle)
```
```c
void FORCE_RENDER_IN_GAME_UI(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDC459CFA0CCE245B` (`N_0xdc459cfa0cce245b`)

---
### FreeMemoryForHighQualityPhoto

`FREE_MEMORY_FOR_HIGH_QUALITY_PHOTO` · hash `0xD801CC02177FA3F1` · jhash `0x9CBA682A` · **Cliente**

```lua
FreeMemoryForHighQualityPhoto()
```
```c
void FREE_MEMORY_FOR_HIGH_QUALITY_PHOTO();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD801CC02177FA3F1` (`N_0xd801cc02177fa3f1`)

---
### FreeMemoryForLowQualityPhoto

`FREE_MEMORY_FOR_LOW_QUALITY_PHOTO` · hash `0x6A12D88881435DCA` · jhash `0x108F36CC` · **Cliente**

```lua
FreeMemoryForLowQualityPhoto()
```
```c
void FREE_MEMORY_FOR_LOW_QUALITY_PHOTO();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6A12D88881435DCA` (`N_0x6a12d88881435dca`)

---
### FreeMemoryForMissionCreatorPhoto

`FREE_MEMORY_FOR_MISSION_CREATOR_PHOTO` · hash `0x0A46AF8A78DC5E0A` · jhash `0x9E553002` · **Cliente**

```lua
FreeMemoryForMissionCreatorPhoto()
```
```c
void FREE_MEMORY_FOR_MISSION_CREATOR_PHOTO();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0A46AF8A78DC5E0A` (`N_0x0a46af8a78dc5e0a`)

---
### GetActualScreenResolution

`GET_ACTUAL_SCREEN_RESOLUTION` · hash `0x873C9F3104101DD3` · **Cliente**

```lua
local x, y = GetActualScreenResolution()
```
```c
void GET_ACTUAL_SCREEN_RESOLUTION(int* x, int* y);
```

**Parámetros**

- `x` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `y` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

Returns current screen resolution.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `_GET_SCREEN_ACTIVE_RESOLUTION` (`GetScreenActiveResolution`), `_GET_ACTIVE_SCREEN_RESOLUTION` (`GetActiveScreenResolution`)

---
### GetAspectRatio

`GET_ASPECT_RATIO` · hash `0xF1307EF624A80D87` · **Cliente**

```lua
local retval = GetAspectRatio(physicalAspect)
```
```c
float GET_ASPECT_RATIO(BOOL physicalAspect);
```

**Parámetros**

- `physicalAspect` (`BOOL`): A boolean value. Passing in `true` returns the physical aspect ratio of the game window. Passing in `false` returns the aspect ratio of the main game window.

**Devuelve:** `float` — The aspect ratio of the game window as a floating-point number.

**Descripción oficial:**

This native retrieves the aspect ratio of the game window. If `physicalAspect` is `true`, it returns the physical aspect ratio of the game window, which is useful for 3x1 modes. Otherwise, it returns the aspect ratio of the main game window, considering any custom overrides from the settings menu.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `_GET_SCREEN_ASPECT_RATIO` (`GetScreenAspectRatio`), `_GET_ASPECT_RATIO` (`GetAspectRatio`)

---
### GetBinkMovieTime

`_GET_BINK_MOVIE_TIME` · hash `0x8E17DDD6B9D5BF29` · **Cliente**

```lua
local retval = GetBinkMovieTime(binkMovie)
```
```c
float _GET_BINK_MOVIE_TIME(int binkMovie);
```

**Parámetros**

- `binkMovie` (`int`)

**Devuelve:** `float`

**Descripción oficial:**

In percentage: 0.0 - 100.0

```
NativeDB Introduced: v1734
```

---
### GetCurrentNumberOfCloudPhotos

`GET_CURRENT_NUMBER_OF_CLOUD_PHOTOS` · hash `0x473151EBC762C6DA` · jhash `0x21DBF0C9` · **Cliente**

```lua
local retval = GetCurrentNumberOfCloudPhotos()
```
```c
int GET_CURRENT_NUMBER_OF_CLOUD_PHOTOS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x473151EBC762C6DA` (`N_0x473151ebc762c6da`), `_GET_NUMBER_OF_PHOTOS` (`GetNumberOfPhotos`), `_GET_CURRENT_NUMBER_OF_PHOTOS` (`GetCurrentNumberOfPhotos`)

---
### GetDecalWashLevel

`GET_DECAL_WASH_LEVEL` · hash `0x323F647679A09103` · jhash `0x054448EF` · **Cliente**

```lua
local retval = GetDecalWashLevel(decal)
```
```c
float GET_DECAL_WASH_LEVEL(int decal);
```

**Parámetros**

- `decal` (`int`)

**Devuelve:** `float`

---
### GetExtraTimecycleModifierIndex

`_GET_EXTRA_TIMECYCLE_MODIFIER_INDEX` · hash `0xBB0527EC6341496D` · **Cliente**

```lua
local retval = GetExtraTimecycleModifierIndex()
```
```c
int _GET_EXTRA_TIMECYCLE_MODIFIER_INDEX();
```

**Devuelve:** `int` — An integer representing the Timecycle modifier

**Descripción oficial:**

See [`GET_TIMECYCLE_MODIFIER_INDEX`](#gettimecyclemodifierindex) for use, works the same just for the secondary timecycle modifier.

**Nombres antiguos (alias):** `0xBB0527EC6341496D` (`N_0xbb0527ec6341496d`)

---
### GetIsHidef

`GET_IS_HIDEF` · hash `0x84ED31191CC5D2C9` · jhash `0x1C340359` · **Cliente**

```lua
local retval = GetIsHidef()
```
```c
BOOL GET_IS_HIDEF();
```

**Devuelve:** `BOOL` — A boolean value indicating whether the game is running in high-definition (`true`) or not (`false`).

**Descripción oficial:**

This native indicates whether the game is running in high-definition (HD) resolution. It returns `false` if the resolution is less than `1280x720` and `true` if it's equal to or greater than `1280x720`.

```
NativeDB Introduced: v323
```

---
### GetIsPetrolDecalInRange

`GET_IS_PETROL_DECAL_IN_RANGE` · hash `0x2F09F7976C512404` · jhash `0x242C6A04` · **Cliente**

```lua
local retval = GetIsPetrolDecalInRange(xCoord, yCoord, zCoord, radius)
```
```c
BOOL GET_IS_PETROL_DECAL_IN_RANGE(float xCoord, float yCoord, float zCoord, float radius);
```

**Parámetros**

- `xCoord` (`float`)
- `yCoord` (`float`)
- `zCoord` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2F09F7976C512404` (`N_0x2f09f7976c512404`)

---
### GetIsWidescreen

`GET_IS_WIDESCREEN` · hash `0x30CF4BDA4FCB1905` · jhash `0xEC717AEF` · **Cliente**

```lua
local retval = GetIsWidescreen()
```
```c
BOOL GET_IS_WIDESCREEN();
```

**Devuelve:** `BOOL` — A boolean value indicating whether the game is running in widescreen mode (`true`) or not (`false`).Returns `false` for narrow format aspect ratios (3:2, 4:3, 5:4, etc.) and `true` for wide format aspect ratios (5:3, 16:9, 16:10, etc.). If the aspect ratio is set to "Auto" in the game settings, it returns `false` or `true` based on the actual set resolution ratio.

**Descripción oficial:**

This native retrieves whether the game is running in widescreen mode or not.

```
NativeDB Introduced: v323
```

---
### GetMaximumNumberOfCloudPhotos

`GET_MAXIMUM_NUMBER_OF_CLOUD_PHOTOS` · hash `0xDC54A7AF8B3A14EF` · jhash `0x239272BD` · **Cliente**

```lua
local retval = GetMaximumNumberOfCloudPhotos()
```
```c
int GET_MAXIMUM_NUMBER_OF_CLOUD_PHOTOS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
This function is hard-coded to always return 96.
```

**Nombres antiguos (alias):** `0xDC54A7AF8B3A14EF` (`N_0xdc54a7af8b3a14ef`), `_GET_MAXIMUM_NUMBER_OF_PHOTOS_2` (`GetMaximumNumberOfPhotos_2`)

---
### GetMaximumNumberOfPhotos

`GET_MAXIMUM_NUMBER_OF_PHOTOS` · hash `0x34D23450F028B0BF` · jhash `0x727AA63F` · **Cliente**

```lua
local retval = GetMaximumNumberOfPhotos()
```
```c
int GET_MAXIMUM_NUMBER_OF_PHOTOS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
This function is hard-coded to always return 0.
```

---
### GetRequestingnightvision

`GET_REQUESTINGNIGHTVISION` · hash `0x35FB78DC42B7BD21` · jhash `0xF3A6309E` · **Cliente**

```lua
local retval = GetRequestingnightvision()
```
```c
BOOL GET_REQUESTINGNIGHTVISION();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x35FB78DC42B7BD21` (`N_0x35fb78dc42b7bd21`)

---
### GetSafeZoneSize

`GET_SAFE_ZONE_SIZE` · hash `0xBAF107B6BB2C97F0` · jhash `0x3F0D1A6F` · **Cliente**

```lua
local retval = GetSafeZoneSize()
```
```c
float GET_SAFE_ZONE_SIZE();
```

**Devuelve:** `float`

**Descripción oficial:**

```
Gets the scale of safe zone. if the safe zone size scale is max, it will return 1.0.  
```

---
### GetScaleformMovieMethodReturnValueBool

`GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_BOOL` · hash `0xD80A80346A45D761` · **Cliente**

```lua
local retval = GetScaleformMovieMethodReturnValueBool(methodReturn)
```
```c
BOOL GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_BOOL(int methodReturn);
```

**Parámetros**

- `methodReturn` (`int`): Operation handle returned by [`END_SCALEFORM_MOVIE_METHOD_RETURN_VALUE`](#endscaleformmoviemethodreturnvalue)

**Devuelve:** `BOOL` — The return value passed from actionscript to game code.

**Nombres antiguos (alias):** `0xD80A80346A45D761` (`N_0xd80a80346a45d761`), `_GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_BOOL` (`GetScaleformMovieMethodReturnValueBool`)

---
### GetScaleformMovieMethodReturnValueInt

`GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_INT` · hash `0x2DE7EFA66B906036` · jhash `0x2CFB0E6D` · **Cliente**

```lua
local retval = GetScaleformMovieMethodReturnValueInt(method_return)
```
```c
int GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_INT(int method_return);
```

**Parámetros**

- `method_return` (`int`): The return value of this native: `EndScaleformMovieMethodReturn`

**Devuelve:** `int` — Returns an int in the same way `GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_STRING` returns a string.

**Descripción oficial:**

Used to get a return value from a scaleform function. Returns an int in the same way GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_STRING returns a string.

**Nombres antiguos (alias):** `0x2DE7EFA66B906036` (`N_0x2de7efa66b906036`), `_GET_SCALEFORM_MOVIE_FUNCTION_RETURN_INT` (`GetScaleformMovieFunctionReturnInt`)

---
### GetScaleformMovieMethodReturnValueString

`GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_STRING` · hash `0xE1E258829A885245` · jhash `0x516862EB` · **Cliente**

```lua
local retval = GetScaleformMovieMethodReturnValueString(method_return)
```
```c
char* GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_STRING(int method_return);
```

**Parámetros**

- `method_return` (`int`): The return value of this native: `EndScaleformMovieMethodReturn`

**Devuelve:** `char*` — Returns a string in the same way `GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_INT` returns an int.

**Descripción oficial:**

Used to get a return value from a scaleform function. Returns a string in the same way GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_INT returns an int.

**Nombres antiguos (alias):** `SITTING_TV` (`SittingTv`), `_GET_SCALEFORM_MOVIE_FUNCTION_RETURN_STRING` (`GetScaleformMovieFunctionReturnString`)

**Ejemplo (lua):**

```lua
local a = RequestScaleformMovie("translate") --scaleform gfx
while not HasScaleformMovieLoaded(a) do
    Citizen.Wait(0)
end
BeginScaleformMovieMethod(a,"EnglishToChinese") --call function
ScaleformMovieMethodAddParamPlayerNameString("Good") --input
local b = EndScaleformMovieMethodReturnValue()
while true do
    if IsScaleformMovieMethodReturnValueReady(b) then
       local c = GetScaleformMovieMethodReturnValueString(b) --output
       print(c)
       break
    end
    Citizen.Wait(0)
end
```

---
### GetScreenCoordFromWorldCoord

`GET_SCREEN_COORD_FROM_WORLD_COORD` · hash `0x34E82F05DF2974F5` · jhash `0x1F950E4B` · **Cliente**

```lua
local retval, screenX, screenY = GetScreenCoordFromWorldCoord(worldX, worldY, worldZ)
```
```c
BOOL GET_SCREEN_COORD_FROM_WORLD_COORD(float worldX, float worldY, float worldZ, float* screenX, float* screenY);
```

**Parámetros**

- `worldX` (`float`)
- `worldY` (`float`)
- `worldZ` (`float`)
- `screenX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `screenY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Convert a world coordinate into its relative screen coordinate.  (WorldToScreen)
Returns a boolean; whether or not the operation was successful. It will return false if the coordinates given are not visible to the rendering camera.
For .NET users...
VB:
Public Shared Function World3DToScreen2d(pos as vector3) As Vector2
        Dim x2dp, y2dp As New Native.OutputArgument
        Native.Function.Call(Of Boolean)(Native.Hash.GET_SCREEN_COORD_FROM_WORLD_COORD , pos.x, pos.y, pos.z, x2dp, y2dp)
        Return New Vector2(x2dp.GetResult(Of Single), y2dp.GetResult(Of Single))

    End Function
C#:
Vector2 World3DToScreen2d(Vector3 pos)
    {
        var x2dp = new OutputArgument();
        var y2dp = new OutputArgument();
        Function.Call<bool>(Hash.GET_SCREEN_COORD_FROM_WORLD_COORD , pos.X, pos.Y, pos.Z, x2dp, y2dp);
        return new Vector2(x2dp.GetResult<float>(), y2dp.GetResult<float>());
    }
//USE VERY SMALL VALUES FOR THE SCALE OF RECTS/TEXT because it is dramatically larger on screen than in 3D, e.g '0.05' small.
Used to be called _WORLD3D_TO_SCREEN2D
I thought we lost you from the scene forever. It does seem however that calling SET_DRAW_ORIGIN then your natives, then ending it. Seems to work better for certain things such as keeping boxes around people for a predator missile e.g.
```

**Nombres antiguos (alias):** `_WORLD3D_TO_SCREEN2D` (`World3dToScreen2d`)

---
### GetScreenResolution

`GET_SCREEN_RESOLUTION` · hash `0x888D57E407E63624` · jhash `0x29F3572F` · **Cliente**

```lua
local x, y = GetScreenResolution()
```
```c
void GET_SCREEN_RESOLUTION(int* x, int* y);
```

**Parámetros**

- `x` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `y` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

Hardcoded to always return 1280x720. Use [`_GET_ACTIVE_SCREEN_RESOLUTION`](#getactualscreenresolution) to retrieve the correct screen resolution.

---
### GetScreenblurFadeCurrentTime

`GET_SCREENBLUR_FADE_CURRENT_TIME` · hash `0x5CCABFFCA31DDE33` · jhash `0xEA432A94` · **Cliente**

```lua
local retval = GetScreenblurFadeCurrentTime()
```
```c
float GET_SCREENBLUR_FADE_CURRENT_TIME();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `IS_PARTICLE_FX_DELAYED_BLINK` (`IsParticleFxDelayedBlink`)

---
### GetScriptGfxPosition

`_GET_SCRIPT_GFX_POSITION` · hash `0x6DD8F5AA635EB4B2` · **Cliente**

```lua
local calculatedX, calculatedY = GetScriptGfxPosition(x, y)
```
```c
void _GET_SCRIPT_GFX_POSITION(float x, float y, float* calculatedX, float* calculatedY);
```

**Parámetros**

- `x` (`float`): The input X coordinate.
- `y` (`float`): The input Y coordinate.
- `calculatedX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: A pointer to the calculated X value.
- `calculatedY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: A pointer to the calculated Y value.

**Devuelve:** `void`

**Descripción oficial:**

Calculates the effective X/Y fractions when applying the values set by `SET_SCRIPT_GFX_ALIGN` and
`SET_SCRIPT_GFX_ALIGN_PARAMS`.

**Nombres antiguos (alias):** `0x6DD8F5AA635EB4B2` (`N_0x6dd8f5aa635eb4b2`)

**Ejemplo (lua):**

```lua
local calcX, calcX = GetScriptGfxPosition(0.2, 0.2)
```

---
### GetStatusOfLoadMissionCreatorPhoto

`GET_STATUS_OF_LOAD_MISSION_CREATOR_PHOTO` · hash `0x1670F8D05056F257` · jhash `0x226B08EA` · **Cliente**

```lua
local retval = GetStatusOfLoadMissionCreatorPhoto(p0)
```
```c
int GET_STATUS_OF_LOAD_MISSION_CREATOR_PHOTO(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x1670F8D05056F257` (`N_0x1670f8d05056f257`)

---
### GetStatusOfSaveHighQualityPhoto

`GET_STATUS_OF_SAVE_HIGH_QUALITY_PHOTO` · hash `0x0C0C4E81E1AC60A0` · jhash `0xEC5D0317` · **Cliente**

```lua
local retval = GetStatusOfSaveHighQualityPhoto()
```
```c
int GET_STATUS_OF_SAVE_HIGH_QUALITY_PHOTO();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0C0C4E81E1AC60A0` (`N_0x0c0c4e81e1ac60a0`)

---
### GetStatusOfSortedListOperation

`GET_STATUS_OF_SORTED_LIST_OPERATION` · hash `0xF5BED327CEA362B1` · jhash `0x596B900D` · **Cliente**

```lua
local retval = GetStatusOfSortedListOperation(scanForSaving)
```
```c
int GET_STATUS_OF_SORTED_LIST_OPERATION(BOOL scanForSaving);
```

**Parámetros**

- `scanForSaving` (`BOOL`)

**Devuelve:** `int` — 0 - Succeeded, 1 - In progress, 2 - Failed

**Descripción oficial:**

Returns status of gallery photo fetch, which was requested by [`QUEUE_OPERATION_TO_CREATE_SORTED_LIST_OF_PHOTOS`](#queueoperationtocreatesortedlistofphotos).

**Nombres antiguos (alias):** `0xF5BED327CEA362B1` (`N_0xf5bed327cea362b1`)

---
### GetStatusOfTakeHighQualityPhoto

`GET_STATUS_OF_TAKE_HIGH_QUALITY_PHOTO` · hash `0x0D6CA79EEEBD8CA3` · jhash `0x65376C9B` · **Cliente**

```lua
local retval = GetStatusOfTakeHighQualityPhoto()
```
```c
int GET_STATUS_OF_TAKE_HIGH_QUALITY_PHOTO();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0D6CA79EEEBD8CA3` (`N_0x0d6ca79eeebd8ca3`)

---
### GetStatusOfTakeMissionCreatorPhoto

`GET_STATUS_OF_TAKE_MISSION_CREATOR_PHOTO` · hash `0x90A78ECAA4E78453` · jhash `0xADBBA287` · **Cliente**

```lua
local retval = GetStatusOfTakeMissionCreatorPhoto()
```
```c
int GET_STATUS_OF_TAKE_MISSION_CREATOR_PHOTO();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x90A78ECAA4E78453` (`N_0x90a78ecaa4e78453`)

---
### GetTextureResolution

`GET_TEXTURE_RESOLUTION` · hash `0x35736EE65BD00C11` · jhash `0x096DAA4D` · **Cliente**

```lua
local retval = GetTextureResolution(textureDict, textureName)
```
```c
Vector3 GET_TEXTURE_RESOLUTION(char* textureDict, char* textureName);
```

**Parámetros**

- `textureDict` (`char*`)
- `textureName` (`char*`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
Returns the texture resolution of the passed texture dict+name.  
Note: Most texture resolutions are doubled compared to the console version of the game.  
```

---
### GetTimecycleModifierIndex

`GET_TIMECYCLE_MODIFIER_INDEX` · hash `0xFDF3D97C674AFB66` · jhash `0x594FEEC4` · **Cliente**

```lua
local retval = GetTimecycleModifierIndex()
```
```c
int GET_TIMECYCLE_MODIFIER_INDEX();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Only use for this in the PC scripts is:
if (GRAPHICS::GET_TIMECYCLE_MODIFIER_INDEX() != -1)
For a full list, see here: pastebin.com/cnk7FTF2
```

---
### GetTimecycleTransitionModifierIndex

`GET_TIMECYCLE_TRANSITION_MODIFIER_INDEX` · hash `0x459FD2C8D0AB78BC` · jhash `0x03C44E4B` · **Cliente**

```lua
local retval = GetTimecycleTransitionModifierIndex()
```
```c
int GET_TIMECYCLE_TRANSITION_MODIFIER_INDEX();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x459FD2C8D0AB78BC` (`N_0x459fd2c8d0ab78bc`)

---
### GetTogglePausedRenderphasesStatus

`GET_TOGGLE_PAUSED_RENDERPHASES_STATUS` · hash `0xEB3DAC2C86001E5E` · jhash `0xD4F5D07D` · **Cliente**

```lua
local retval = GetTogglePausedRenderphasesStatus()
```
```c
BOOL GET_TOGGLE_PAUSED_RENDERPHASES_STATUS();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEB3DAC2C86001E5E` (`N_0xeb3dac2c86001e5e`)

---
### GetTvChannel

`GET_TV_CHANNEL` · hash `0xFC1E275A90D39995` · jhash `0x6B96145A` · **Cliente**

```lua
local retval = GetTvChannel()
```
```c
int GET_TV_CHANNEL();
```

**Devuelve:** `int`

---
### GetTvVolume

`GET_TV_VOLUME` · hash `0x2170813D3DD8661B` · jhash `0x39555CF0` · **Cliente**

```lua
local retval = GetTvVolume()
```
```c
float GET_TV_VOLUME();
```

**Devuelve:** `float`

---
### GetUsingnightvision

`GET_USINGNIGHTVISION` · hash `0x2202A3F42C8E5F79` · jhash `0x62619061` · **Cliente**

```lua
local retval = GetUsingnightvision()
```
```c
BOOL GET_USINGNIGHTVISION();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_IS_NIGHTVISION_INACTIVE` (`IsNightvisionInactive`), `_IS_NIGHTVISION_ACTIVE` (`IsNightvisionActive`)

---
### GetUsingseethrough

`GET_USINGSEETHROUGH` · hash `0x44B80ABAB9D80BD3` · jhash `0x1FE547F2` · **Cliente**

```lua
local retval = GetUsingseethrough()
```
```c
BOOL GET_USINGSEETHROUGH();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_IS_SEETHROUGH_ACTIVE` (`IsSeethroughActive`)

---
### GetVehicleCrewEmblemRequestState

`GET_VEHICLE_CREW_EMBLEM_REQUEST_STATE` · hash `0xFE26117A5841B2FF` · jhash `0x4F4D76E8` · **Cliente**

```lua
local retval = GetVehicleCrewEmblemRequestState(vehicle, p1)
```
```c
int GET_VEHICLE_CREW_EMBLEM_REQUEST_STATE(Vehicle vehicle, int p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xFE26117A5841B2FF` (`N_0xfe26117a5841b2ff`)

---
### GolfTrailGetMaxHeight

`GOLF_TRAIL_GET_MAX_HEIGHT` · hash `0xA4819F5E23E2FFAD` · jhash `0xA08B46AD` · **Cliente**

```lua
local retval = GolfTrailGetMaxHeight()
```
```c
float GOLF_TRAIL_GET_MAX_HEIGHT();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xA4819F5E23E2FFAD` (`N_0xa4819f5e23e2ffad`)

---
### GolfTrailGetVisualControlPoint

`GOLF_TRAIL_GET_VISUAL_CONTROL_POINT` · hash `0xA4664972A9B8F8BA` · jhash `0xECD470F0` · **Cliente**

```lua
local retval = GolfTrailGetVisualControlPoint(p0)
```
```c
Vector3 GOLF_TRAIL_GET_VISUAL_CONTROL_POINT(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `0xA4664972A9B8F8BA` (`N_0xa4664972a9b8f8ba`)

---
### GolfTrailSetColour

`GOLF_TRAIL_SET_COLOUR` · hash `0x12995F2E53FFA601` · jhash `0x804F444C` · **Cliente**

```lua
GolfTrailSetColour(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11)
```
```c
void GOLF_TRAIL_SET_COLOUR(int p0, int p1, int p2, int p3, int p4, int p5, int p6, int p7, int p8, int p9, int p10, int p11);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`int`)
- `p3` (`int`)
- `p4` (`int`)
- `p5` (`int`)
- `p6` (`int`)
- `p7` (`int`)
- `p8` (`int`)
- `p9` (`int`)
- `p10` (`int`)
- `p11` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x12995F2E53FFA601` (`N_0x12995f2e53ffa601`)

---
### GolfTrailSetEnabled

`GOLF_TRAIL_SET_ENABLED` · hash `0xA51C4B86B71652AE` · jhash `0x5D3BFFC9` · **Cliente**

```lua
GolfTrailSetEnabled(toggle)
```
```c
void GOLF_TRAIL_SET_ENABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA51C4B86B71652AE` (`N_0xa51c4b86b71652ae`)

---
### GolfTrailSetFacing

`GOLF_TRAIL_SET_FACING` · hash `0x06F761EA47C1D3ED` · jhash `0x0D830DC7` · **Cliente**

```lua
GolfTrailSetFacing(p0)
```
```c
void GOLF_TRAIL_SET_FACING(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x06F761EA47C1D3ED` (`N_0x06f761ea47c1d3ed`)

---
### GolfTrailSetFixedControlPoint

`GOLF_TRAIL_SET_FIXED_CONTROL_POINT` · hash `0xB1BB03742917A5D6` · jhash `0x3BB12B75` · **Cliente**

```lua
GolfTrailSetFixedControlPoint(type, xPos, yPos, zPos, p4, red, green, blue, alpha)
```
```c
void GOLF_TRAIL_SET_FIXED_CONTROL_POINT(int type, float xPos, float yPos, float zPos, float p4, int red, int green, int blue, int alpha);
```

**Parámetros**

- `type` (`int`)
- `xPos` (`float`)
- `yPos` (`float`)
- `zPos` (`float`)
- `p4` (`float`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
12 matches across 4 scripts. All 4 scripts were job creators.
type ranged from 0 - 2.
p4 was always 0.2f. Likely scale.
assuming p5 - p8 is RGBA, the graphic is always yellow (255, 255, 0, 255).
Tested but noticed nothing.
```

**Nombres antiguos (alias):** `0xB1BB03742917A5D6` (`N_0xb1bb03742917a5d6`)

---
### GolfTrailSetPath

`GOLF_TRAIL_SET_PATH` · hash `0x312342E1A4874F3F` · jhash `0xD9653728` · **Cliente**

```lua
GolfTrailSetPath(p0, p1, p2, p3, p4, p5, p6, p7, p8)
```
```c
void GOLF_TRAIL_SET_PATH(float p0, float p1, float p2, float p3, float p4, float p5, float p6, float p7, BOOL p8);
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
- `p8` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p8 seems to always be false.  
```

**Nombres antiguos (alias):** `0x312342E1A4874F3F` (`N_0x312342e1a4874f3f`)

---
### GolfTrailSetRadius

`GOLF_TRAIL_SET_RADIUS` · hash `0x2485D34E50A22E84` · jhash `0x72BA8A14` · **Cliente**

```lua
GolfTrailSetRadius(p0, p1, p2)
```
```c
void GOLF_TRAIL_SET_RADIUS(float p0, float p1, float p2);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2485D34E50A22E84` (`N_0x2485d34e50a22e84`)

---
### GolfTrailSetShaderParams

`GOLF_TRAIL_SET_SHADER_PARAMS` · hash `0x9CFDD90B2B844BF7` · jhash `0x4EA70FB4` · **Cliente**

```lua
GolfTrailSetShaderParams(p0, p1, p2, p3, p4)
```
```c
void GOLF_TRAIL_SET_SHADER_PARAMS(float p0, float p1, float p2, float p3, float p4);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only appeared in Golf & Golf_mp. Parameters were all ptrs  
```

**Nombres antiguos (alias):** `0x9CFDD90B2B844BF7` (`N_0x9cfdd90b2b844bf7`)

---
### GolfTrailSetTessellation

`GOLF_TRAIL_SET_TESSELLATION` · hash `0xDBAA5EC848BA2D46` · jhash `0xBB1A1294` · **Cliente**

```lua
GolfTrailSetTessellation(p0, p1)
```
```c
void GOLF_TRAIL_SET_TESSELLATION(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDBAA5EC848BA2D46` (`N_0xdbaa5ec848ba2d46`)

---
### GrassLodResetScriptAreas

`_GRASS_LOD_RESET_SCRIPT_AREAS` · hash `0x302C91AB2D477F7E` · **Cliente**

```lua
GrassLodResetScriptAreas()
```
```c
void _GRASS_LOD_RESET_SCRIPT_AREAS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x302C91AB2D477F7E` (`N_0x302c91ab2d477f7e`)

---
### GrassLodShrinkScriptAreas

`_GRASS_LOD_SHRINK_SCRIPT_AREAS` · hash `0x6D955F6A9E0295B1` · **Cliente**

```lua
GrassLodShrinkScriptAreas(x, y, z, radius, p4, p5, p6)
```
```c
void _GRASS_LOD_SHRINK_SCRIPT_AREAS(float x, float y, float z, float radius, float p4, float p5, float p6);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Wraps 0xAAE9BE70EC7C69AB with FLT_MAX as p7, Jenkins: 0x73E96210?
```

**Nombres antiguos (alias):** `0x6D955F6A9E0295B1` (`N_0x6d955f6a9e0295b1`)

---
### HasScaleformContainerMovieLoadedIntoParent

`HAS_SCALEFORM_CONTAINER_MOVIE_LOADED_INTO_PARENT` · hash `0x8217150E1217EBFD` · jhash `0x1DFE8D8A` · **Cliente**

```lua
local retval = HasScaleformContainerMovieLoadedIntoParent(scaleformHandle)
```
```c
BOOL HAS_SCALEFORM_CONTAINER_MOVIE_LOADED_INTO_PARENT(int scaleformHandle);
```

**Parámetros**

- `scaleformHandle` (`int`)

**Devuelve:** `BOOL`

---
### HasScaleformMovieFilenameLoaded

`HAS_SCALEFORM_MOVIE_FILENAME_LOADED` · hash `0x0C1C5D756FB5F337` · jhash `0x494A9E50` · **Cliente**

```lua
local retval = HasScaleformMovieFilenameLoaded(scaleformName)
```
```c
BOOL HAS_SCALEFORM_MOVIE_FILENAME_LOADED(char* scaleformName);
```

**Parámetros**

- `scaleformName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Only values used in the scripts are:
"heist_mp"
"heistmap_mp"
"instructional_buttons"
"heist_pre"
```

**Nombres antiguos (alias):** `0x0C1C5D756FB5F337` (`N_0x0c1c5d756fb5f337`), `_HAS_NAMED_SCALEFORM_MOVIE_LOADED` (`HasNamedScaleformMovieLoaded`)

---
### HasScaleformMovieLoaded

`HAS_SCALEFORM_MOVIE_LOADED` · hash `0x85F01B8D5B90570E` · jhash `0xDDFB6448` · **Cliente**

```lua
local retval = HasScaleformMovieLoaded(scaleformHandle)
```
```c
BOOL HAS_SCALEFORM_MOVIE_LOADED(int scaleformHandle);
```

**Parámetros**

- `scaleformHandle` (`int`)

**Devuelve:** `BOOL`

---
### HasScaleformMovieNamedLoaded

`_HAS_SCALEFORM_MOVIE_NAMED_LOADED` · hash `0x9743BCCF7CD6E1F6` · **Cliente**

```lua
local retval, scaleformHandle = HasScaleformMovieNamedLoaded(scaleformName)
```
```c
BOOL _HAS_SCALEFORM_MOVIE_NAMED_LOADED(int* scaleformHandle, char* scaleformName);
```

**Parámetros**

- `scaleformHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Scaleform movie handle
- `scaleformName` (`char*`): Name of the Scaleform movie to check

**Devuelve:** `BOOL` — Returns `true` if the named Scaleform movie is loaded, `false` otherwise.

**Descripción oficial:**

Check if a Scaleform movie with the given name has been loaded.

```
NativeDB Introduced: v3407
```

---
### HasScaleformScriptHudMovieLoaded

`HAS_SCALEFORM_SCRIPT_HUD_MOVIE_LOADED` · hash `0xDF6E5987D2B4D140` · jhash `0x79B43255` · **Cliente**

```lua
local retval = HasScaleformScriptHudMovieLoaded(hudComponent)
```
```c
BOOL HAS_SCALEFORM_SCRIPT_HUD_MOVIE_LOADED(int hudComponent);
```

**Parámetros**

- `hudComponent` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_HAS_HUD_SCALEFORM_LOADED` (`HasHudScaleformLoaded`)

---
### HasStreamedTextureDictLoaded

`HAS_STREAMED_TEXTURE_DICT_LOADED` · hash `0x0145F696AAAAD2E4` · jhash `0x3F436EEF` · **Cliente**

```lua
local retval = HasStreamedTextureDictLoaded(textureDict)
```
```c
BOOL HAS_STREAMED_TEXTURE_DICT_LOADED(char* textureDict);
```

**Parámetros**

- `textureDict` (`char*`)

**Devuelve:** `BOOL`

---
### IsDecalAlive

`IS_DECAL_ALIVE` · hash `0xC694D74949CAFD0C` · jhash `0xCDD4A61A` · **Cliente**

```lua
local retval = IsDecalAlive(decal)
```
```c
BOOL IS_DECAL_ALIVE(int decal);
```

**Parámetros**

- `decal` (`int`)

**Devuelve:** `BOOL`

---
### IsPlaylistUnk

`_IS_PLAYLIST_UNK` · hash `0x1F710BFF7DAE6261` · **Cliente**

```lua
local retval = IsPlaylistUnk(tvChannel, p1)
```
```c
BOOL _IS_PLAYLIST_UNK(int tvChannel, Any p1);
```

**Parámetros**

- `tvChannel` (`int`)
- `p1` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1604
```

---
### IsScaleformMovieDeleting

`IS_SCALEFORM_MOVIE_DELETING` · hash `0x86255B1FC929E33E` · **Cliente**

```lua
local retval = IsScaleformMovieDeleting(scaleformIndex)
```
```c
BOOL IS_SCALEFORM_MOVIE_DELETING(int scaleformIndex);
```

**Parámetros**

- `scaleformIndex` (`int`): Scaleform index returned by [`REQUEST_SCALEFORM_MOVIE`](#requestscaleformmovie) (or similar natives).

**Devuelve:** `BOOL` — Returns true if a scaleform movie is being deleted from streaming memory (After it has been marked as no longer needed with [`SET_SCALEFORM_MOVIE_AS_NO_LONGER_NEEDED`](#setscaleformmovieasnolongerneeded).

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x86255B1FC929E33E` (`N_0x86255b1fc929e33e`)

---
### IsScaleformMovieMethodReturnValueReady

`IS_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_READY` · hash `0x768FF8961BA904D6` · jhash `0x5CD7C3C0` · **Cliente**

```lua
local retval = IsScaleformMovieMethodReturnValueReady(method_return)
```
```c
BOOL IS_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_READY(int method_return);
```

**Parámetros**

- `method_return` (`int`): The return value of this native: `EndScaleformMovieMethodReturn`

**Devuelve:** `BOOL` — Returns true if the return value of a scaleform function is ready to be collected

**Descripción oficial:**

methodReturn: The return value of this native: END_SCALEFORM_MOVIE_METHOD_RETURN_VALUE
Returns true if the return value of a scaleform function is ready to be collected (using GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_STRING or GET_SCALEFORM_MOVIE_METHOD_RETURN_VALUE_INT).

**Nombres antiguos (alias):** `0x768FF8961BA904D6` (`N_0x768ff8961ba904d6`), `_GET_SCALEFORM_MOVIE_FUNCTION_RETURN_BOOL` (`GetScaleformMovieFunctionReturnBool`)

---
### IsScreenblurFadeRunning

`IS_SCREENBLUR_FADE_RUNNING` · hash `0x7B226C785A52A0A9` · jhash `0x926B8734` · **Cliente**

```lua
local retval = IsScreenblurFadeRunning()
```
```c
BOOL IS_SCREENBLUR_FADE_RUNNING();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether screen transition to blur/from blur is running.
```

**Nombres antiguos (alias):** `0x7B226C785A52A0A9` (`N_0x7b226c785a52a0a9`)

---
### IsTrackedPointVisible

`IS_TRACKED_POINT_VISIBLE` · hash `0xC45CCDAAC9221CA8` · jhash `0x0BFC4F64` · **Cliente**

```lua
local retval = IsTrackedPointVisible(point)
```
```c
BOOL IS_TRACKED_POINT_VISIBLE(int point);
```

**Parámetros**

- `point` (`int`)

**Devuelve:** `BOOL`

---
### IsTvPlaylistItemPlaying

`_IS_TV_PLAYLIST_ITEM_PLAYING` · hash `0x0AD973CA1E077B60` · jhash `0x4D1EB0FB` · **Cliente**

```lua
local retval = IsTvPlaylistItemPlaying(videoCliphash)
```
```c
BOOL _IS_TV_PLAYLIST_ITEM_PLAYING(Hash videoCliphash);
```

**Parámetros**

- `videoCliphash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_*
```

**Nombres antiguos (alias):** `0x0AD973CA1E077B60` (`N_0x0ad973ca1e077b60`), `_LOAD_TV_CHANNEL` (`LoadTvChannel`)

---
### LoadMissionCreatorPhoto

`LOAD_MISSION_CREATOR_PHOTO` · hash `0x4862437A486F91B0` · jhash `0x56C1E488` · **Cliente**

```lua
local retval, p1, p2 = LoadMissionCreatorPhoto(p0, p3)
```
```c
BOOL LOAD_MISSION_CREATOR_PHOTO(char* p0, Any* p1, Any* p2, BOOL p3);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4862437A486F91B0` (`N_0x4862437a486f91b0`)

---
### LoadMovieMeshSet

`LOAD_MOVIE_MESH_SET` · hash `0xB66064452270E8F1` · jhash `0x9627905C` · **Cliente**

```lua
local retval = LoadMovieMeshSet(movieMeshSetName)
```
```c
int LOAD_MOVIE_MESH_SET(char* movieMeshSetName);
```

**Parámetros**

- `movieMeshSetName` (`char*`)

**Devuelve:** `int`

---
### MoveVehicleDecals

`MOVE_VEHICLE_DECALS` · hash `0x84C8D7C2D30D3280` · jhash `0xCE9E6CF2` · **Cliente**

```lua
MoveVehicleDecals(p0, p1)
```
```c
void MOVE_VEHICLE_DECALS(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x0218ba067d249dea

`0x0218BA067D249DEA` · hash `0x0218BA067D249DEA` · **Cliente**

```lua
N_0x0218ba067d249dea()
```
```c
void 0x0218BA067D249DEA();
```

**Devuelve:** `void`

---
### N_0x02369d5c8a51fdcf

`0x02369D5C8A51FDCF` · hash `0x02369D5C8A51FDCF` · jhash `0xFDF6D8DA` · **Cliente**

```lua
N_0x02369d5c8a51fdcf(toggle)
```
```c
void 0x02369D5C8A51FDCF(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
DISABLE_S*
```

---
### N_0x03300b57fcac6ddb

`0x03300B57FCAC6DDB` · hash `0x03300B57FCAC6DDB` · jhash `0x60F72371` · **Cliente**

```lua
N_0x03300b57fcac6ddb(p0)
```
```c
void 0x03300B57FCAC6DDB(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x0ae73d8df3a762b2

`0x0AE73D8DF3A762B2` · hash `0x0AE73D8DF3A762B2` · jhash `0x342FA2B4` · **Cliente**

```lua
N_0x0ae73d8df3a762b2(p0)
```
```c
void 0x0AE73D8DF3A762B2(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x0e4299c549f0d1f1

`0x0E4299C549F0D1F1` · hash `0x0E4299C549F0D1F1` · jhash `0x9BABCBA4` · **Cliente**

```lua
N_0x0e4299c549f0d1f1(toggle)
```
```c
void 0x0E4299C549F0D1F1(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0x108be26959a9d9bb

`0x108BE26959A9D9BB` · hash `0x108BE26959A9D9BB` · jhash `0x24A7A7F6` · **Cliente**

```lua
N_0x108be26959a9d9bb(toggle)
```
```c
void 0x108BE26959A9D9BB(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
UI3DSCENE_*
```

---
### N_0x14fc5833464340a8

`0x14FC5833464340A8` · hash `0x14FC5833464340A8` · **Cliente**

```lua
N_0x14fc5833464340a8()
```
```c
void 0x14FC5833464340A8();
```

**Devuelve:** `void`

---
### N_0x1612c45f9e3e0d44

`0x1612C45F9E3E0D44` · hash `0x1612C45F9E3E0D44` · **Cliente**

```lua
N_0x1612c45f9e3e0d44()
```
```c
void 0x1612C45F9E3E0D44();
```

**Devuelve:** `void`

---
### N_0x1bbc135a4d25edde

`0x1BBC135A4D25EDDE` · hash `0x1BBC135A4D25EDDE` · **Cliente**

```lua
N_0x1bbc135a4d25edde(p0)
```
```c
void 0x1BBC135A4D25EDDE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x259ba6d4e6f808f1

`0x259BA6D4E6F808F1` · hash `0x259BA6D4E6F808F1` · **Cliente**

```lua
N_0x259ba6d4e6f808f1(p0)
```
```c
void 0x259BA6D4E6F808F1(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x25fc3e33a31ad0c9

`0x25FC3E33A31AD0C9` · hash `0x25FC3E33A31AD0C9` · **Cliente**

```lua
N_0x25fc3e33a31ad0c9(p0)
```
```c
void 0x25FC3E33A31AD0C9(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x27cfb1b1e078cb2d

`0x27CFB1B1E078CB2D` · hash `0x27CFB1B1E078CB2D` · jhash `0xC2703B88` · **Cliente**

```lua
N_0x27cfb1b1e078cb2d()
```
```c
void 0x27CFB1B1E078CB2D();
```

**Devuelve:** `void`

---
### N_0x27feb5254759cde3

`0x27FEB5254759CDE3` · hash `0x27FEB5254759CDE3` · jhash `0xD63FCB3E` · **Cliente**

```lua
local retval = N_0x27feb5254759cde3(textureDict, p1)
```
```c
BOOL 0x27FEB5254759CDE3(char* textureDict, BOOL p1);
```

**Parámetros**

- `textureDict` (`char*`)
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

---
### N_0x2a251aa48b2b46db

`0x2A251AA48B2B46DB` · hash `0x2A251AA48B2B46DB` · **Cliente**

```lua
N_0x2a251aa48b2b46db()
```
```c
void 0x2A251AA48B2B46DB();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### N_0x2b40a97646381508

`0x2B40A97646381508` · hash `0x2B40A97646381508` · **Cliente**

```lua
N_0x2b40a97646381508(p0)
```
```c
void 0x2B40A97646381508(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x2c42340f916c5930

`0x2C42340F916C5930` · hash `0x2C42340F916C5930` · **Cliente**

```lua
local retval = N_0x2c42340f916c5930(p0)
```
```c
Any 0x2C42340F916C5930(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x2d3b147afad49de0

`0x2D3B147AFAD49DE0` · hash `0x2D3B147AFAD49DE0` · **Cliente**

```lua
N_0x2d3b147afad49de0(textureDict, textureName, x, y, width, height, p6, red, green, blue, alpha, p11)
```
```c
void 0x2D3B147AFAD49DE0(char* textureDict, char* textureName, float x, float y, float width, float height, float p6, int red, int green, int blue, int alpha, int p11);
```

**Parámetros**

- `textureDict` (`char*`): inside script_txds.rpf, browse it with OpenIV
- `textureName` (`char*`): textureName
- `x` (`float`): x position must be between 0.0 and 1.0 (1.0 being the most right side of the screen)
- `y` (`float`): y position must be between 0.0 and 1.0 (1.0 being the most bottom side of the screen)
- `width` (`float`): width 0.0 - 1.0 is the reasonable amount generally
- `height` (`float`): height 0.0 - 1.0 is the reasonable amount generally
- `p6` (`float`): almost always 0.0
- `red` (`int`): red color
- `green` (`int`): green color
- `blue` (`int`): blue color
- `alpha` (`int`): alpha
- `p11` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used in arcade games and Beam hack minigame in Doomsday Heist. For example, [Penetrator Arcade Game](https://streamable.com/8igrzw)

NativeDB Introduced: v1290
```

**Ejemplo (lua):**

```lua
-- drawing the game area for penetrator arcade game
Citizen.CreateThread(function()
    RequestStreamedTextureDict("MPArcadeDegenatron", false)
    while not HasStreamedTextureDictLoaded("MPArcadeDegenatron") do Citizen.Wait(1) end
    while true do
        N_0x2d3b147afad49de0("MPArcadeDegenatron", "penetrator_scene_frame", 0.5, 0.5, 0.4, 0.6, 0.0, 255, 0, 0, 255, 0)
        Citizen.Wait(1)
    end
end)
```

---
### N_0x2fcb133ca50a49eb

`0x2FCB133CA50A49EB` · hash `0x2FCB133CA50A49EB` · **Cliente**

```lua
local retval = N_0x2fcb133ca50a49eb(p0)
```
```c
Any 0x2FCB133CA50A49EB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x30432a0118736e00

`0x30432A0118736E00` · hash `0x30432A0118736E00` · **Cliente**

```lua
local retval = N_0x30432a0118736e00()
```
```c
Hash 0x30432A0118736E00();
```

**Devuelve:** `Hash`

**Descripción oficial:**

```
GET_CURRENT_*

NativeDB Introduced: v1493
```

---
### N_0x346ef3ecaaab149e

`0x346EF3ECAAAB149E` · hash `0x346EF3ECAAAB149E` · jhash `0x88EAF398` · **Cliente**

```lua
N_0x346ef3ecaaab149e()
```
```c
void 0x346EF3ECAAAB149E();
```

**Devuelve:** `void`

---
### N_0x36f6626459d91457

`0x36F6626459D91457` · hash `0x36F6626459D91457` · jhash `0xC07C64C9` · **Cliente**

```lua
N_0x36f6626459d91457(p0)
```
```c
void 0x36F6626459D91457(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### N_0x393bd2275ceb7793

`0x393BD2275CEB7793` · hash `0x393BD2275CEB7793` · **Cliente**

```lua
local retval = N_0x393bd2275ceb7793()
```
```c
Any 0x393BD2275CEB7793();
```

**Devuelve:** `Any`

---
### N_0x3c788e7f6438754d

`0x3C788E7F6438754D` · hash `0x3C788E7F6438754D` · **Cliente**

```lua
N_0x3c788e7f6438754d(checkpointHandle, x, y, z)
```
```c
void 0x3C788E7F6438754D(int checkpointHandle, float x, float y, float z);
```

**Parámetros**

- `checkpointHandle` (`int`): the handle of a created checkpoint
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

Sets the given checkpoint target to the new coords

---
### N_0x43fa7cbe20dab219

`0x43FA7CBE20DAB219` · hash `0x43FA7CBE20DAB219` · **Cliente**

```lua
N_0x43fa7cbe20dab219(p0)
```
```c
void 0x43FA7CBE20DAB219(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x46d1a61a21f566fc

`0x46D1A61A21F566FC` · hash `0x46D1A61A21F566FC` · jhash `0x2056A015` · **Cliente**

```lua
N_0x46d1a61a21f566fc(p0)
```
```c
void 0x46D1A61A21F566FC(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### N_0x4af92acd3141d96c

`0x4AF92ACD3141D96C` · hash `0x4AF92ACD3141D96C` · jhash `0xC9EF81ED` · **Cliente**

```lua
N_0x4af92acd3141d96c()
```
```c
void 0x4AF92ACD3141D96C();
```

**Devuelve:** `void`

---
### N_0x54e22ea2c1956a8d

`0x54E22EA2C1956A8D` · hash `0x54E22EA2C1956A8D` · jhash `0x8BE3D47F` · **Cliente**

```lua
N_0x54e22ea2c1956a8d(p0)
```
```c
void 0x54E22EA2C1956A8D(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### N_0x5b0316762afd4a64

`0x5B0316762AFD4A64` · hash `0x5B0316762AFD4A64` · jhash `0xA9DC8558` · **Cliente**

```lua
local retval = N_0x5b0316762afd4a64()
```
```c
int 0x5B0316762AFD4A64();
```

**Devuelve:** `int`

---
### N_0x5dbf05db5926d089

`0x5DBF05DB5926D089` · hash `0x5DBF05DB5926D089` · **Cliente**

```lua
N_0x5dbf05db5926d089(p0)
```
```c
void 0x5DBF05DB5926D089(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x5debd9c4dc995692

`0x5DEBD9C4DC995692` · hash `0x5DEBD9C4DC995692` · **Cliente**

```lua
N_0x5debd9c4dc995692()
```
```c
void 0x5DEBD9C4DC995692();
```

**Devuelve:** `void`

---
### N_0x5f6df3d92271e8a1

`0x5F6DF3D92271E8A1` · hash `0x5F6DF3D92271E8A1` · jhash `0x18136DE0` · **Cliente**

```lua
N_0x5f6df3d92271e8a1(toggle)
```
```c
void 0x5F6DF3D92271E8A1(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
DISABLE_*
```

**Nombres antiguos (alias):** `SET_PARTICLE_FX_BLOOD_SCALE` (`SetParticleFxBloodScale`)

---
### N_0x615d3925e87a3b26

`0x615D3925E87A3B26` · hash `0x615D3925E87A3B26` · jhash `0x1E3A3126` · **Cliente**

```lua
N_0x615d3925e87a3b26(checkpoint)
```
```c
void 0x615D3925E87A3B26(int checkpoint);
```

**Parámetros**

- `checkpoint` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Unknown. Called after creating a checkpoint (type: 51) in the creators.  
```

---
### N_0x61f95e5bb3e0a8c6

`0x61F95E5BB3E0A8C6` · hash `0x61F95E5BB3E0A8C6` · **Cliente**

```lua
N_0x61f95e5bb3e0a8c6(p0)
```
```c
void 0x61F95E5BB3E0A8C6(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x649c97d52332341a

`0x649C97D52332341A` · hash `0x649C97D52332341A` · **Cliente**

```lua
N_0x649c97d52332341a(p0)
```
```c
void 0x649C97D52332341A(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x6a51f78772175a51

`0x6A51F78772175A51` · hash `0x6A51F78772175A51` · **Cliente**

```lua
N_0x6a51f78772175a51(toggle)
```
```c
void 0x6A51F78772175A51(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_F*
```

---
### N_0x759650634f07b6b4

`0x759650634F07B6B4` · hash `0x759650634F07B6B4` · jhash `0x25D569EB` · **Cliente**

```lua
local retval = N_0x759650634f07b6b4(p0)
```
```c
BOOL 0x759650634F07B6B4(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

---
### N_0x7a42b2e236e71415

`0x7A42B2E236E71415` · hash `0x7A42B2E236E71415` · jhash `0x431AA036` · **Cliente**

```lua
N_0x7a42b2e236e71415()
```
```c
void 0x7A42B2E236E71415();
```

**Devuelve:** `void`

**Descripción oficial:**

```
UI3DSCENE_*
```

---
### N_0x7ac24eab6d74118d

`0x7AC24EAB6D74118D` · hash `0x7AC24EAB6D74118D` · jhash `0xB2410EAB` · **Cliente**

```lua
local retval = N_0x7ac24eab6d74118d(p0)
```
```c
BOOL 0x7AC24EAB6D74118D(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `BOOL`

---
### N_0x7fa5d82b8f58ec06

`0x7FA5D82B8F58EC06` · hash `0x7FA5D82B8F58EC06` · jhash `0x1F3CADB0` · **Cliente**

```lua
local retval = N_0x7fa5d82b8f58ec06()
```
```c
BOOL 0x7FA5D82B8F58EC06();
```

**Devuelve:** `BOOL`

---
### N_0x814af7dcaacc597b

`0x814AF7DCAACC597B` · hash `0x814AF7DCAACC597B` · **Cliente**

```lua
N_0x814af7dcaacc597b(p0)
```
```c
void 0x814AF7DCAACC597B(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x82acc484ffa3b05f

`0x82ACC484FFA3B05F` · hash `0x82ACC484FFA3B05F` · **Cliente**

```lua
local retval = N_0x82acc484ffa3b05f(p0)
```
```c
Any 0x82ACC484FFA3B05F(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x851cd923176eba7c

`0x851CD923176EBA7C` · hash `0x851CD923176EBA7C` · jhash `0xDCBA251B` · **Cliente**

```lua
N_0x851cd923176eba7c()
```
```c
void 0x851CD923176EBA7C();
```

**Devuelve:** `void`

---
### N_0x8cde909a0370bb3a

`0x8CDE909A0370BB3A` · hash `0x8CDE909A0370BB3A` · **Cliente**

```lua
N_0x8cde909a0370bb3a(toggle)
```
```c
void 0x8CDE909A0370BB3A(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Used only once in the scripts (taxi_clowncar)

SET_PARTICLE_FX_*
```

---
### N_0x908311265d42a820

`0x908311265D42A820` · hash `0x908311265D42A820` · **Cliente**

```lua
N_0x908311265d42a820(p0)
```
```c
void 0x908311265D42A820(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### N_0x949f397a288b28b3

`0x949F397A288B28B3` · hash `0x949F397A288B28B3` · jhash `0xE3880F5A` · **Cliente**

```lua
N_0x949f397a288b28b3(p0)
```
```c
void 0x949F397A288B28B3(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### N_0x9641588dab93b4b5

`0x9641588DAB93B4B5` · hash `0x9641588DAB93B4B5` · **Cliente**

```lua
N_0x9641588dab93b4b5(p0)
```
```c
void 0x9641588DAB93B4B5(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x98d18905bf723b99

`0x98D18905BF723B99` · hash `0x98D18905BF723B99` · **Cliente**

```lua
local retval = N_0x98d18905bf723b99()
```
```c
Any 0x98D18905BF723B99();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### N_0x98edf76a7271e4f2

`0x98EDF76A7271E4F2` · hash `0x98EDF76A7271E4F2` · **Cliente**

```lua
N_0x98edf76a7271e4f2()
```
```c
void 0x98EDF76A7271E4F2();
```

**Devuelve:** `void`

**Descripción oficial:**

```
REQUEST_*
```

---
### N_0x9b079e5221d984d3

`0x9B079E5221D984D3` · hash `0x9B079E5221D984D3` · jhash `0x447A9EB9` · **Cliente**

```lua
N_0x9b079e5221d984d3(p0)
```
```c
void 0x9B079E5221D984D3(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
FORCE_*
```

---
### N_0xa46b73faa3460ae1

`0xA46B73FAA3460AE1` · hash `0xA46B73FAA3460AE1` · **Cliente**

```lua
N_0xa46b73faa3460ae1(p0)
```
```c
void 0xA46B73FAA3460AE1(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xaae9be70ec7c69ab

`0xAAE9BE70EC7C69AB` · hash `0xAAE9BE70EC7C69AB` · **Cliente**

```lua
N_0xaae9be70ec7c69ab(p0, p1, p2, p3, p4, p5, p6, p7)
```
```c
void 0xAAE9BE70EC7C69AB(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7);
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

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xadd6627c4d325458

`0xADD6627C4D325458` · hash `0xADD6627C4D325458` · **Cliente**

```lua
N_0xadd6627c4d325458(p0)
```
```c
void 0xADD6627C4D325458(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xae51bc858f32ba66

`0xAE51BC858F32BA66` · hash `0xAE51BC858F32BA66` · **Cliente**

```lua
N_0xae51bc858f32ba66(p0, p1, p2, p3, p4)
```
```c
void 0xAE51BC858F32BA66(Any p0, float p1, float p2, float p3, float p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

---
### N_0xb2ebe8cbc58b90e9

`0xB2EBE8CBC58B90E9` · hash `0xB2EBE8CBC58B90E9` · **Cliente**

```lua
local retval = N_0xb2ebe8cbc58b90e9()
```
```c
Any 0xB2EBE8CBC58B90E9();
```

**Devuelve:** `Any`

---
### N_0xb3c641f3630bf6da

`0xB3C641F3630BF6DA` · hash `0xB3C641F3630BF6DA` · jhash `0xF6B837F0` · **Cliente**

```lua
N_0xb3c641f3630bf6da(p0)
```
```c
void 0xB3C641F3630BF6DA(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Setter for 0xE59343E9E96529E7

SET_M*
```

---
### N_0xb569f41f3e7e83a4

`0xB569F41F3E7E83A4` · hash `0xB569F41F3E7E83A4` · **Cliente**

```lua
N_0xb569f41f3e7e83a4(p0)
```
```c
void 0xB569F41F3E7E83A4(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xba0127da25fd54c9

`0xBA0127DA25FD54C9` · hash `0xBA0127DA25FD54C9` · **Cliente**

```lua
N_0xba0127da25fd54c9(p0, p1)
```
```c
void 0xBA0127DA25FD54C9(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0xba3d194057c79a7b

`0xBA3D194057C79A7B` · hash `0xBA3D194057C79A7B` · **Cliente**

```lua
N_0xba3d194057c79a7b(p0)
```
```c
void 0xBA3D194057C79A7B(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PARTICLE_FX_*
```

---
### N_0xbb90e12cac1dab25

`0xBB90E12CAC1DAB25` · hash `0xBB90E12CAC1DAB25` · jhash `0x3968E915` · **Cliente**

```lua
N_0xbb90e12cac1dab25(p0)
```
```c
void 0xBB90E12CAC1DAB25(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### N_0xbcedb009461da156

`0xBCEDB009461DA156` · hash `0xBCEDB009461DA156` · jhash `0x5AB94128` · **Cliente**

```lua
local retval = N_0xbcedb009461da156()
```
```c
Any 0xBCEDB009461DA156();
```

**Devuelve:** `Any`

---
### N_0xbe197eaa669238f4

`0xBE197EAA669238F4` · hash `0xBE197EAA669238F4` · **Cliente**

```lua
local retval = N_0xbe197eaa669238f4(p0, p1, p2, p3)
```
```c
Any 0xBE197EAA669238F4(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
This function is hard-coded to always return 0.  
```

---
### N_0xc0416b061f2b7e5e

`0xC0416B061F2B7E5E` · hash `0xC0416B061F2B7E5E` · jhash `0x1A1A72EF` · **Cliente**

```lua
N_0xc0416b061f2b7e5e(p0)
```
```c
void 0xC0416B061F2B7E5E(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
GOLF_TRAIL_SET_*
```

---
### N_0xc35a6d07c93802b2

`0xC35A6D07C93802B2` · hash `0xC35A6D07C93802B2` · **Cliente**

```lua
N_0xc35a6d07c93802b2()
```
```c
void 0xC35A6D07C93802B2();
```

**Devuelve:** `void`

---
### N_0xc5c8f970d4edff71

`0xC5C8F970D4EDFF71` · hash `0xC5C8F970D4EDFF71` · **Cliente**

```lua
N_0xc5c8f970d4edff71(p0)
```
```c
void 0xC5C8F970D4EDFF71(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xca465d9cc0d231ba

`0xCA465D9CC0D231BA` · hash `0xCA465D9CC0D231BA` · **Cliente**

```lua
N_0xca465d9cc0d231ba(p0)
```
```c
void 0xCA465D9CC0D231BA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xca4ae345a153d573

`0xCA4AE345A153D573` · hash `0xCA4AE345A153D573` · jhash `0x64BA4648` · **Cliente**

```lua
N_0xca4ae345a153d573(p0)
```
```c
void 0xCA4AE345A153D573(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xcb82a0bf0e3e3265

`0xCB82A0BF0E3E3265` · hash `0xCB82A0BF0E3E3265` · jhash `0xCFCDC518` · **Cliente**

```lua
local retval = N_0xcb82a0bf0e3e3265(p0)
```
```c
int 0xCB82A0BF0E3E3265(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

---
### N_0xcfd16f0db5a3535c

`0xCFD16F0DB5A3535C` · hash `0xCFD16F0DB5A3535C` · **Cliente**

```lua
N_0xcfd16f0db5a3535c(toggle)
```
```c
void 0xCFD16F0DB5A3535C(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0xd1c55b110e4df534

`0xD1C55B110E4DF534` · hash `0xD1C55B110E4DF534` · jhash `0xD99EC000` · **Cliente**

```lua
N_0xd1c55b110e4df534(p0)
```
```c
void 0xD1C55B110E4DF534(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_TV_???  
```

---
### N_0xdb1ea9411c8911ec

`0xDB1EA9411C8911EC` · hash `0xDB1EA9411C8911EC` · **Cliente**

```lua
N_0xdb1ea9411c8911ec(checkpointHandle)
```
```c
void 0xDB1EA9411C8911EC(int checkpointHandle);
```

**Parámetros**

- `checkpointHandle` (`int`): the handle of a created checkpoint

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

This native is used for the "larger" circular checkpoints, and sets the circle/ring around the checkpoint to point in the same direction as the inner arrow

---
### N_0xe2892e7e55d7073a

`0xE2892E7E55D7073A` · hash `0xE2892E7E55D7073A` · jhash `0x455F1084` · **Cliente**

```lua
N_0xe2892e7e55d7073a(p0)
```
```c
void 0xE2892E7E55D7073A(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### N_0xe59343e9e96529e7

`0xE59343E9E96529E7` · hash `0xE59343E9E96529E7` · jhash `0xD906A3A9` · **Cliente**

```lua
local retval = N_0xe59343e9e96529e7()
```
```c
float 0xE59343E9E96529E7();
```

**Devuelve:** `float`

**Descripción oficial:**

```
Getter for 0xB3C641F3630BF6DA

GET_M*
```

---
### N_0xe63d7c6eececb66b

`0xE63D7C6EECECB66B` · hash `0xE63D7C6EECECB66B` · jhash `0xD34A6CBA` · **Cliente**

```lua
N_0xe63d7c6eececb66b(toggle)
```
```c
void 0xE63D7C6EECECB66B(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
TOGGLE_*
```

---
### N_0xe791df1f73ed2c8b

`0xE791DF1F73ED2C8B` · hash `0xE791DF1F73ED2C8B` · jhash `0x9D84554C` · **Cliente**

```lua
local retval = N_0xe791df1f73ed2c8b(p0)
```
```c
Any 0xE791DF1F73ED2C8B(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
This function is hard-coded to always return 0.  
```

---
### N_0xec72c258667be5ea

`0xEC72C258667BE5EA` · hash `0xEC72C258667BE5EA` · jhash `0x9C106AD9` · **Cliente**

```lua
local retval = N_0xec72c258667be5ea(p0)
```
```c
Any 0xEC72C258667BE5EA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
This function is hard-coded to always return 0.  
```

---
### N_0xef398beee4ef45f9

`0xEF398BEEE4EF45F9` · hash `0xEF398BEEE4EF45F9` · **Cliente**

```lua
N_0xef398beee4ef45f9(p0)
```
```c
void 0xEF398BEEE4EF45F9(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xf3f776ada161e47d

`0xF3F776ADA161E47D` · hash `0xF3F776ADA161E47D` · **Cliente**

```lua
N_0xf3f776ada161e47d(p0, p1)
```
```c
void 0xF3F776ADA161E47D(Any p0, Any p1);
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
### N_0xf51d36185993515d

`0xF51D36185993515D` · hash `0xF51D36185993515D` · jhash `0x20EABD0F` · **Cliente**

```lua
N_0xf51d36185993515d(checkpoint, posX, posY, posZ, unkX, unkY, unkZ)
```
```c
void 0xF51D36185993515D(int checkpoint, float posX, float posY, float posZ, float unkX, float unkY, float unkZ);
```

**Parámetros**

- `checkpoint` (`int`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `unkX` (`float`)
- `unkY` (`float`)
- `unkZ` (`float`)

**Devuelve:** `void`

---
### N_0xf78b803082d4386f

`0xF78B803082D4386F` · hash `0xF78B803082D4386F` · **Cliente**

```lua
N_0xf78b803082d4386f(p0)
```
```c
void 0xF78B803082D4386F(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### N_0xfcf6788fc4860cd4

`0xFCF6788FC4860CD4` · hash `0xFCF6788FC4860CD4` · **Cliente**

```lua
N_0xfcf6788fc4860cd4(checkpoint)
```
```c
void 0xFCF6788FC4860CD4(int checkpoint);
```

**Parámetros**

- `checkpoint` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

SET_CHECKPOINT_\*

```
NativeDB Introduced: v1734
```

---
### OverrideInteriorSmokeEnd

`OVERRIDE_INTERIOR_SMOKE_END` · hash `0xEFB55E7C25D3B3BE` · jhash `0xE29EE145` · **Cliente**

```lua
OverrideInteriorSmokeEnd()
```
```c
void OVERRIDE_INTERIOR_SMOKE_END();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xEFB55E7C25D3B3BE` (`N_0xefb55e7c25d3b3be`)

---
### OverrideInteriorSmokeLevel

`OVERRIDE_INTERIOR_SMOKE_LEVEL` · hash `0x1600FD8CF72EBC12` · jhash `0xD87CC710` · **Cliente**

```lua
OverrideInteriorSmokeLevel(level)
```
```c
void OVERRIDE_INTERIOR_SMOKE_LEVEL(float level);
```

**Parámetros**

- `level` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1600FD8CF72EBC12` (`N_0x1600fd8cf72ebc12`)

---
### OverrideInteriorSmokeName

`OVERRIDE_INTERIOR_SMOKE_NAME` · hash `0x2A2A52824DB96700` · jhash `0x0F486429` · **Cliente**

```lua
OverrideInteriorSmokeName(name)
```
```c
void OVERRIDE_INTERIOR_SMOKE_NAME(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2A2A52824DB96700` (`N_0x2a2a52824db96700`)

---
### OverridePedBadgeTexture

`_OVERRIDE_PED_BADGE_TEXTURE` · hash `0x95EB5E34F821BABE` · **Cliente**

```lua
local retval = OverridePedBadgeTexture(ped, txd, txn)
```
```c
BOOL _OVERRIDE_PED_BADGE_TEXTURE(Ped ped, char* txd, char* txn);
```

**Parámetros**

- `ped` (`Ped`)
- `txd` (`char*`)
- `txn` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Overriding ped badge texture to a passed texture. It's synced between players (even custom textures!), don't forget to request used dict on *all* clients to make it sync properly. Can be removed by passing empty strings.
```

**Nombres antiguos (alias):** `0x95EB5E34F821BABE` (`N_0x95eb5e34f821babe`)

---
### PassKeyboardInputToScaleform

`PASS_KEYBOARD_INPUT_TO_SCALEFORM` · hash `0xD1C7CB175E012964` · jhash `0xE9183D3A` · **Cliente**

```lua
local retval = PassKeyboardInputToScaleform(scaleformHandle)
```
```c
BOOL PASS_KEYBOARD_INPUT_TO_SCALEFORM(int scaleformHandle);
```

**Parámetros**

- `scaleformHandle` (`int`): Scaleform movie handle returned by [REQUEST_SCALEFORM_MOVIE](#requestscaleformmovie)

**Devuelve:** `BOOL` — Bool indicating if an input occurred this frame and was passed to the scaleform.

**Descripción oficial:**

Passes keyboard input to scaleform. You must call this native every frame. Once an input occurs, this native will return true and call `SET_PC_KEY` scaleform movie method with the key that has been inputted.

The key parameter which is passed to the scaleform can also be: "BACKSPACE", "ENTER" or "\x1b" (Which is ESC).
This native is only used in `web_browser.c` as of game build 2944.

**Nombres antiguos (alias):** `0xD1C7CB175E012964` (`N_0xd1c7cb175e012964`)

---
### PatchDecalDiffuseMap

`PATCH_DECAL_DIFFUSE_MAP` · hash `0x8A35C742130C6080` · jhash `0x335695CF` · **Cliente**

```lua
PatchDecalDiffuseMap(decalType, textureDict, textureName)
```
```c
void PATCH_DECAL_DIFFUSE_MAP(int decalType, char* textureDict, char* textureName);
```

**Parámetros**

- `decalType` (`int`)
- `textureDict` (`char*`)
- `textureName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
REQUEST_STREAMED_TEXTURE_DICT("MPOnMissMarkers", false);  
*uParam0.f_809 = add_decal(9120, vParam1, vVar4, vVar7, 2f, 2f, to_float(iVar0) / 255f, to_float(iVar1) / 255f, to_float(iVar2) / 255f, 1f, -1f, 1, 0, 0);  
PATCH_DECAL_DIFFUSE_MAP(9120, "MPOnMissMarkers", "Capture_The_Flag_Base_Icon");  
```

**Nombres antiguos (alias):** `0x8A35C742130C6080` (`N_0x8a35c742130c6080`), `_ADD_DECAL_TO_MARKER` (`AddDecalToMarker`), `_OVERRIDE_DECAL_TEXTURE` (`OverrideDecalTexture`)

---
### PlayBinkMovie

`_PLAY_BINK_MOVIE` · hash `0x70D2CC8A542A973C` · **Cliente**

```lua
PlayBinkMovie(binkMovie)
```
```c
void _PLAY_BINK_MOVIE(int binkMovie);
```

**Parámetros**

- `binkMovie` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### PopTimecycleModifier

`POP_TIMECYCLE_MODIFIER` · hash `0x3C8938D7D872211E` · jhash `0x79D7D235` · **Cliente**

```lua
PopTimecycleModifier()
```
```c
void POP_TIMECYCLE_MODIFIER();
```

**Devuelve:** `void`

---
### PresetInteriorAmbientCache

`PRESET_INTERIOR_AMBIENT_CACHE` · hash `0xD7021272EB0A451E` · jhash `0x137E3E24` · **Cliente**

```lua
PresetInteriorAmbientCache(timecycleModifierName)
```
```c
void PRESET_INTERIOR_AMBIENT_CACHE(char* timecycleModifierName);
```

**Parámetros**

- `timecycleModifierName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only one match in the scripts:
GRAPHICS::PRESET_INTERIOR_AMBIENT_CACHE("int_carrier_hanger");
```

**Nombres antiguos (alias):** `0xD7021272EB0A451E` (`N_0xd7021272eb0a451e`), `_PRESET_INTERIOR_AMBIENT_CACHE` (`PresetInteriorAmbientCache`)

---
### PushTimecycleModifier

`PUSH_TIMECYCLE_MODIFIER` · hash `0x58F735290861E6B4` · jhash `0x7E082045` · **Cliente**

```lua
PushTimecycleModifier()
```
```c
void PUSH_TIMECYCLE_MODIFIER();
```

**Devuelve:** `void`

---
### QueryMovieMeshSetState

`QUERY_MOVIE_MESH_SET_STATE` · hash `0x9B6E70C5CEEF4EEB` · jhash `0x9D5D9B38` · **Cliente**

```lua
local retval = QueryMovieMeshSetState(p0)
```
```c
Any QUERY_MOVIE_MESH_SET_STATE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x9B6E70C5CEEF4EEB` (`N_0x9b6e70c5ceef4eeb`)

---
### QueueOperationToCreateSortedListOfPhotos

`QUEUE_OPERATION_TO_CREATE_SORTED_LIST_OF_PHOTOS` · hash `0x2A893980E96B659A` · jhash `0x199FABF0` · **Cliente**

```lua
local retval = QueueOperationToCreateSortedListOfPhotos(scanForSaving)
```
```c
BOOL QUEUE_OPERATION_TO_CREATE_SORTED_LIST_OF_PHOTOS(BOOL scanForSaving);
```

**Parámetros**

- `scanForSaving` (`BOOL`)

**Devuelve:** `BOOL` — Returns true if the operation began.

**Descripción oficial:**

Queues a scan of all gallery photos.
Also see [`GET_STATUS_OF_SORTED_LIST_OPERATION`](#getstatusofsortedlistoperation)

**Nombres antiguos (alias):** `0x2A893980E96B659A` (`N_0x2a893980e96b659a`)

---
### RegisterNoirScreenEffectThisFrame

`_REGISTER_NOIR_SCREEN_EFFECT_THIS_FRAME` · hash `0xA44FF770DFBC5DAE` · **Cliente**

```lua
RegisterNoirScreenEffectThisFrame()
```
```c
void _REGISTER_NOIR_SCREEN_EFFECT_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Used with 'NG_filmnoir_BW{01,02}' timecycles and the "NOIR_FILTER_SOUNDS" audioref.

**Nombres antiguos (alias):** `0xA44FF770DFBC5DAE` (`N_0xa44ff770dfbc5dae`)

---
### ReleaseBinkMovie

`_RELEASE_BINK_MOVIE` · hash `0x04D950EEFA4EED8C` · **Cliente**

```lua
ReleaseBinkMovie(binkMovie)
```
```c
void _RELEASE_BINK_MOVIE(int binkMovie);
```

**Parámetros**

- `binkMovie` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### ReleaseMovieMeshSet

`RELEASE_MOVIE_MESH_SET` · hash `0xEB119AA014E89183` · jhash `0x4FA5501D` · **Cliente**

```lua
ReleaseMovieMeshSet(movieMeshSet)
```
```c
void RELEASE_MOVIE_MESH_SET(int movieMeshSet);
```

**Parámetros**

- `movieMeshSet` (`int`)

**Devuelve:** `void`

---
### RemoveDecal

`REMOVE_DECAL` · hash `0xED3F346429CCD659` · jhash `0xA4363188` · **Cliente**

```lua
RemoveDecal(decal)
```
```c
void REMOVE_DECAL(int decal);
```

**Parámetros**

- `decal` (`int`)

**Devuelve:** `void`

---
### RemoveDecalsFromObject

`REMOVE_DECALS_FROM_OBJECT` · hash `0xCCF71CBDDF5B6CB9` · jhash `0x8B67DCA7` · **Cliente**

```lua
RemoveDecalsFromObject(obj)
```
```c
void REMOVE_DECALS_FROM_OBJECT(Object obj);
```

**Parámetros**

- `obj` (`Object`)

**Devuelve:** `void`

---
### RemoveDecalsFromObjectFacing

`REMOVE_DECALS_FROM_OBJECT_FACING` · hash `0xA6F6F70FDC6D144C` · jhash `0xF4999A55` · **Cliente**

```lua
RemoveDecalsFromObjectFacing(obj, x, y, z)
```
```c
void REMOVE_DECALS_FROM_OBJECT_FACING(Object obj, float x, float y, float z);
```

**Parámetros**

- `obj` (`Object`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### RemoveDecalsFromVehicle

`REMOVE_DECALS_FROM_VEHICLE` · hash `0xE91F1B65F2B48D57` · jhash `0x831D06CA` · **Cliente**

```lua
RemoveDecalsFromVehicle(vehicle)
```
```c
void REMOVE_DECALS_FROM_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

---
### RemoveDecalsInRange

`REMOVE_DECALS_IN_RANGE` · hash `0x5D6B2D4830A67C62` · jhash `0x06A619A0` · **Cliente**

```lua
RemoveDecalsInRange(x, y, z, range)
```
```c
void REMOVE_DECALS_IN_RANGE(float x, float y, float z, float range);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `range` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Removes all decals in range from a position, it includes the bullet holes, blood pools, petrol...  
```

---
### RemoveParticleFx

`REMOVE_PARTICLE_FX` · hash `0xC401503DFE8D53CF` · jhash `0x6BA48C7E` · **Cliente**

```lua
RemoveParticleFx(ptfxHandle, p1)
```
```c
void REMOVE_PARTICLE_FX(int ptfxHandle, BOOL p1);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### RemoveParticleFxFromEntity

`REMOVE_PARTICLE_FX_FROM_ENTITY` · hash `0xB8FEAEEBCC127425` · jhash `0xCEDE52E9` · **Cliente**

```lua
RemoveParticleFxFromEntity(entity)
```
```c
void REMOVE_PARTICLE_FX_FROM_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### RemoveParticleFxInRange

`REMOVE_PARTICLE_FX_IN_RANGE` · hash `0xDD19FA1C6D657305` · jhash `0x7EB8F275` · **Cliente**

```lua
RemoveParticleFxInRange(X, Y, Z, radius)
```
```c
void REMOVE_PARTICLE_FX_IN_RANGE(float X, float Y, float Z, float radius);
```

**Parámetros**

- `X` (`float`)
- `Y` (`float`)
- `Z` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

---
### RemoveScaleformScriptHudMovie

`REMOVE_SCALEFORM_SCRIPT_HUD_MOVIE` · hash `0xF44A5456AC3F4F97` · jhash `0x03D87600` · **Cliente**

```lua
RemoveScaleformScriptHudMovie(hudComponent)
```
```c
void REMOVE_SCALEFORM_SCRIPT_HUD_MOVIE(int hudComponent);
```

**Parámetros**

- `hudComponent` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF44A5456AC3F4F97` (`N_0xf44a5456ac3f4f97`)

---
### RemoveTcmodifierOverride

`REMOVE_TCMODIFIER_OVERRIDE` · hash `0x15E33297C3E8DC60` · jhash `0x805BAB08` · **Cliente**

```lua
RemoveTcmodifierOverride(p0)
```
```c
void REMOVE_TCMODIFIER_OVERRIDE(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x15E33297C3E8DC60` (`N_0x15e33297c3e8dc60`)

---
### RemoveVehicleCrewEmblem

`REMOVE_VEHICLE_CREW_EMBLEM` · hash `0xD2300034310557E4` · jhash `0x667046A8` · **Cliente**

```lua
RemoveVehicleCrewEmblem(vehicle, p1)
```
```c
void REMOVE_VEHICLE_CREW_EMBLEM(Vehicle vehicle, int p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD2300034310557E4` (`N_0xd2300034310557e4`)

---
### RequestScaleformMovie

`REQUEST_SCALEFORM_MOVIE` · hash `0x11FE353CF9733E6F` · jhash `0xC67E3DCB` · **Cliente**

```lua
local retval = RequestScaleformMovie(scaleformName)
```
```c
int REQUEST_SCALEFORM_MOVIE(char* scaleformName);
```

**Parámetros**

- `scaleformName` (`char*`)

**Devuelve:** `int`

---
### RequestScaleformMovieInstance

`REQUEST_SCALEFORM_MOVIE_INSTANCE` · hash `0xC514489CFB8AF806` · jhash `0x7CC8057D` · **Cliente**

```lua
local retval = RequestScaleformMovieInstance(scaleformName)
```
```c
int REQUEST_SCALEFORM_MOVIE_INSTANCE(char* scaleformName);
```

**Parámetros**

- `scaleformName` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

Same as [REQUEST_SCALEFORM_MOVIE](#requestscaleformmovie), except it seems to fix stretched scaleforms on ultrawide.

---
### RequestScaleformMovieSkipRenderWhilePaused

`REQUEST_SCALEFORM_MOVIE_SKIP_RENDER_WHILE_PAUSED` · hash `0xBD06C611BB9048C2` · **Cliente**

```lua
local retval = RequestScaleformMovieSkipRenderWhilePaused(scaleformName)
```
```c
int REQUEST_SCALEFORM_MOVIE_SKIP_RENDER_WHILE_PAUSED(char* scaleformName);
```

**Parámetros**

- `scaleformName` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

Requests a scaleform movie that doesn't render when the game is paused (With [`SET_GAME_PAUSED`](MISC.md#setgamepaused)).

**Nombres antiguos (alias):** `_REQUEST_SCALEFORM_MOVIE3` (`RequestScaleformMovie3`), `_REQUEST_SCALEFORM_MOVIE_INTERACTIVE` (`RequestScaleformMovieInteractive`)

---
### RequestScaleformMovieWithIgnoreSuperWidescreen

`REQUEST_SCALEFORM_MOVIE_WITH_IGNORE_SUPER_WIDESCREEN` · hash `0x65E7E78842E74CDB` · **Cliente**

```lua
local retval = RequestScaleformMovieWithIgnoreSuperWidescreen(scaleformName)
```
```c
int REQUEST_SCALEFORM_MOVIE_WITH_IGNORE_SUPER_WIDESCREEN(char* scaleformName);
```

**Parámetros**

- `scaleformName` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

Requests a scaleform movie, which has no widescreen adjustments while rendering (Useful for when your scaleform doesn't fully draw on the screen and borders are visible).

**Nombres antiguos (alias):** `0x65E7E78842E74CDB` (`N_0x65e7e78842e74cdb`), `_REQUEST_SCALEFORM_MOVIE_2` (`RequestScaleformMovie_2`)

---
### RequestScaleformScriptHudMovie

`REQUEST_SCALEFORM_SCRIPT_HUD_MOVIE` · hash `0x9304881D6F6537EA` · jhash `0x7AF85862` · **Cliente**

```lua
RequestScaleformScriptHudMovie(hudComponent)
```
```c
void REQUEST_SCALEFORM_SCRIPT_HUD_MOVIE(int hudComponent);
```

**Parámetros**

- `hudComponent` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9304881D6F6537EA` (`N_0x9304881d6f6537ea`), `_REQUEST_HUD_SCALEFORM` (`RequestHudScaleform`)

---
### RequestStreamedTextureDict

`REQUEST_STREAMED_TEXTURE_DICT` · hash `0xDFA2EF8E04127DD5` · jhash `0x4C9B035F` · **Cliente**

```lua
RequestStreamedTextureDict(textureDict, p1)
```
```c
void REQUEST_STREAMED_TEXTURE_DICT(char* textureDict, BOOL p1);
```

**Parámetros**

- `textureDict` (`char*`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This function can requests texture dictonaries from following RPFs:
scaleform_generic.rpf
scaleform_minigames.rpf
scaleform_minimap.rpf
scaleform_web.rpf
last param isnt a toggle
```

---
### ResetAdaptation

`RESET_ADAPTATION` · hash `0xE3E2C1B4C59DBC77` · jhash `0xD8CC7221` · **Cliente**

```lua
ResetAdaptation(numFrames)
```
```c
void RESET_ADAPTATION(int numFrames);
```

**Parámetros**

- `numFrames` (`int`): Number of frames.

**Devuelve:** `void`

**Descripción oficial:**

Resets AnimPostFX adaptation.

**Nombres antiguos (alias):** `0xE3E2C1B4C59DBC77` (`N_0xe3e2c1b4c59dbc77`)

---
### ResetParticleFxOverride

`RESET_PARTICLE_FX_OVERRIDE` · hash `0x89C8553DD3274AAE` · jhash `0x9E8D8B72` · **Cliente**

```lua
ResetParticleFxOverride(name)
```
```c
void RESET_PARTICLE_FX_OVERRIDE(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Resets the effect of SET_PARTICLE_FX_OVERRIDE
```

**Nombres antiguos (alias):** `0x89C8553DD3274AAE` (`N_0x89c8553dd3274aae`), `_RESET_PARTICLE_FX_ASSET_OLD_TO_NEW` (`ResetParticleFxAssetOldToNew`)

---
### ResetPausedRenderphases

`RESET_PAUSED_RENDERPHASES` · hash `0xE1C8709406F2C41C` · jhash `0x0113EAE4` · **Cliente**

```lua
ResetPausedRenderphases()
```
```c
void RESET_PAUSED_RENDERPHASES();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE1C8709406F2C41C` (`N_0xe1c8709406f2c41c`)

---
### ResetScriptGfxAlign

`RESET_SCRIPT_GFX_ALIGN` · hash `0xE3A3DB414A373DAB` · jhash `0x3FE33BD6` · **Cliente**

```lua
ResetScriptGfxAlign()
```
```c
void RESET_SCRIPT_GFX_ALIGN();
```

**Devuelve:** `void`

**Descripción oficial:**

This function resets the alignment set using `SET_SCRIPT_GFX_ALIGN` and `SET_SCRIPT_GFX_ALIGN_PARAMS` to the default
values ('I', 'I'; 0, 0, 0, 0). This should be used after having used the aforementioned functions in order to not affect
any other scripts attempting to draw.

**Nombres antiguos (alias):** `0xE3A3DB414A373DAB` (`N_0xe3a3db414a373dab`), `_SCREEN_DRAW_POSITION_END` (`ScreenDrawPositionEnd`)

---
### ReturnTwo

`_RETURN_TWO` · hash `0x40AFB081F8ADD4EE` · jhash `0x762E5C5F` · **Cliente**

```lua
local retval = ReturnTwo(p0)
```
```c
int _RETURN_TWO(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x40AFB081F8ADD4EE` (`N_0x40afb081f8add4ee`)

---
### SaveHighQualityPhoto

`SAVE_HIGH_QUALITY_PHOTO` · hash `0x3DEC726C25A11BAC` · jhash `0x3B15D33C` · **Cliente**

```lua
local retval = SaveHighQualityPhoto(unused)
```
```c
BOOL SAVE_HIGH_QUALITY_PHOTO(int unused);
```

**Parámetros**

- `unused` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3DEC726C25A11BAC` (`N_0x3dec726c25a11bac`)

---
### ScaleformMovieMethodAddParamBool

`SCALEFORM_MOVIE_METHOD_ADD_PARAM_BOOL` · hash `0xC58424BA936EB458` · jhash `0x0D4AE8CB` · **Cliente**

```lua
ScaleformMovieMethodAddParamBool(value)
```
```c
void SCALEFORM_MOVIE_METHOD_ADD_PARAM_BOOL(BOOL value);
```

**Parámetros**

- `value` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Pushes a boolean for the Scaleform function onto the stack.  
```

**Nombres antiguos (alias):** `_PUSH_SCALEFORM_MOVIE_FUNCTION_PARAMETER_BOOL` (`PushScaleformMovieFunctionParameterBool`), `_PUSH_SCALEFORM_MOVIE_METHOD_PARAMETER_BOOL` (`PushScaleformMovieMethodParameterBool`)

---
### ScaleformMovieMethodAddParamFloat

`SCALEFORM_MOVIE_METHOD_ADD_PARAM_FLOAT` · hash `0xD69736AAE04DB51A` · jhash `0x9A01FFDA` · **Cliente**

```lua
ScaleformMovieMethodAddParamFloat(value)
```
```c
void SCALEFORM_MOVIE_METHOD_ADD_PARAM_FLOAT(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Pushes a float for the Scaleform function onto the stack.  
```

**Nombres antiguos (alias):** `_PUSH_SCALEFORM_MOVIE_FUNCTION_PARAMETER_FLOAT` (`PushScaleformMovieFunctionParameterFloat`), `_PUSH_SCALEFORM_MOVIE_METHOD_PARAMETER_FLOAT` (`PushScaleformMovieMethodParameterFloat`)

---
### ScaleformMovieMethodAddParamInt

`SCALEFORM_MOVIE_METHOD_ADD_PARAM_INT` · hash `0xC3D0841A0CC546A6` · jhash `0x716777CB` · **Cliente**

```lua
ScaleformMovieMethodAddParamInt(value)
```
```c
void SCALEFORM_MOVIE_METHOD_ADD_PARAM_INT(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Pushes an integer for the Scaleform function onto the stack.  
```

**Nombres antiguos (alias):** `_PUSH_SCALEFORM_MOVIE_FUNCTION_PARAMETER_INT` (`PushScaleformMovieFunctionParameterInt`), `_PUSH_SCALEFORM_MOVIE_METHOD_PARAMETER_INT` (`PushScaleformMovieMethodParameterInt`)

---
### ScaleformMovieMethodAddParamLatestBriefString

`SCALEFORM_MOVIE_METHOD_ADD_PARAM_LATEST_BRIEF_STRING` · hash `0xEC52C631A1831C03` · jhash `0x83A9811D` · **Cliente**

```lua
ScaleformMovieMethodAddParamLatestBriefString(value)
```
```c
void SCALEFORM_MOVIE_METHOD_ADD_PARAM_LATEST_BRIEF_STRING(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Values:
0 - Dialogue Brief
1 - Help Text Brief
2 - Mission Objective Brief

**Nombres antiguos (alias):** `0xEC52C631A1831C03` (`N_0xec52c631a1831c03`), `_SCALEFORM_MOVIE_METHOD_ADD_PARAM_INT_STRING` (`ScaleformMovieMethodAddParamIntString`)

---
### ScaleformMovieMethodAddParamLiteralString

`SCALEFORM_MOVIE_METHOD_ADD_PARAM_LITERAL_STRING` · hash `0x77FE3402004CD1B0` · **Cliente**

```lua
ScaleformMovieMethodAddParamLiteralString(string)
```
```c
void SCALEFORM_MOVIE_METHOD_ADD_PARAM_LITERAL_STRING(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Adds a literal string to a scaleform movie method.
There doesn't seem to be any difference between this and other `SCALEFORM_MOVIE_METHOD_ADD_PARAM_*_STRING` natives in game code.

**Nombres antiguos (alias):** `0x77FE3402004CD1B0` (`N_0x77fe3402004cd1b0`), `_PUSH_SCALEFORM_MOVIE_METHOD_PARAMETER_STRING_2` (`PushScaleformMovieMethodParameterString_2`), `_SCALEFORM_MOVIE_METHOD_ADD_PARAM_TEXTURE_NAME_STRING_2` (`ScaleformMovieMethodAddParamTextureNameString_2`)

---
### ScaleformMovieMethodAddParamPlayerNameString

`SCALEFORM_MOVIE_METHOD_ADD_PARAM_PLAYER_NAME_STRING` · hash `0xE83A3E3557A56640` · jhash `0xCCBF0334` · **Cliente**

```lua
ScaleformMovieMethodAddParamPlayerNameString(string)
```
```c
void SCALEFORM_MOVIE_METHOD_ADD_PARAM_PLAYER_NAME_STRING(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
This method is the equivalent to PUSH_SCALEFORM_MOVIE_FUNCTION_PARAMETER_STRING when using it to add a new button (like "INSTRUCTIONAL_BUTTONS").  
When switching with a controller, the icons update and become the controller's icons.  
```

**Nombres antiguos (alias):** `0xE83A3E3557A56640` (`N_0xe83a3e3557a56640`), `_PUSH_SCALEFORM_MOVIE_METHOD_PARAMETER_BUTTON_NAME` (`PushScaleformMovieMethodParameterButtonName`)

---
### ScaleformMovieMethodAddParamTextureNameString

`SCALEFORM_MOVIE_METHOD_ADD_PARAM_TEXTURE_NAME_STRING` · hash `0xBA7148484BD90365` · jhash `0x4DAAD55B` · **Cliente**

```lua
ScaleformMovieMethodAddParamTextureNameString(string)
```
```c
void SCALEFORM_MOVIE_METHOD_ADD_PARAM_TEXTURE_NAME_STRING(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_PUSH_SCALEFORM_MOVIE_FUNCTION_PARAMETER_STRING` (`PushScaleformMovieFunctionParameterString`), `_PUSH_SCALEFORM_MOVIE_METHOD_PARAMETER_STRING` (`PushScaleformMovieMethodParameterString`)

---
### SeethroughGetMaxThickness

`_SEETHROUGH_GET_MAX_THICKNESS` · hash `0x43DBAE39626CE83F` · **Cliente**

```lua
local retval = SeethroughGetMaxThickness()
```
```c
float _SEETHROUGH_GET_MAX_THICKNESS();
```

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### SeethroughReset

`SEETHROUGH_RESET` · hash `0x70A64C0234EF522C` · jhash `0x310E9B67` · **Cliente**

```lua
SeethroughReset()
```
```c
void SEETHROUGH_RESET();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### SeethroughSetColorNear

`SEETHROUGH_SET_COLOR_NEAR` · hash `0x1086127B3A63505E` · jhash `0x5B2A67A8` · **Cliente**

```lua
SeethroughSetColorNear(red, green, blue)
```
```c
void SEETHROUGH_SET_COLOR_NEAR(int red, int green, int blue);
```

**Parámetros**

- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1086127B3A63505E` (`N_0x1086127b3a63505e`)

---
### SeethroughSetFadeEndDistance

`_SEETHROUGH_SET_FADE_END_DISTANCE` · hash `0x9D75795B9DC6EBBF` · **Cliente**

```lua
SeethroughSetFadeEndDistance(distance)
```
```c
void _SEETHROUGH_SET_FADE_END_DISTANCE(float distance);
```

**Parámetros**

- `distance` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9D75795B9DC6EBBF` (`N_0x9d75795b9dc6ebbf`)

---
### SeethroughSetFadeStartDistance

`_SEETHROUGH_SET_FADE_START_DISTANCE` · hash `0xA78DE25577300BA1` · **Cliente**

```lua
SeethroughSetFadeStartDistance(distance)
```
```c
void _SEETHROUGH_SET_FADE_START_DISTANCE(float distance);
```

**Parámetros**

- `distance` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA78DE25577300BA1` (`N_0xa78de25577300ba1`)

---
### SeethroughSetHeatscale

`SEETHROUGH_SET_HEATSCALE` · hash `0xD7D0B00177485411` · jhash `0x654F0287` · **Cliente**

```lua
SeethroughSetHeatscale(index, heatScale)
```
```c
void SEETHROUGH_SET_HEATSCALE(int index, float heatScale);
```

**Parámetros**

- `index` (`int`)
- `heatScale` (`float`): min: 0.0 max: 0.75

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD7D0B00177485411` (`N_0xd7d0b00177485411`)

---
### SeethroughSetHiLightIntensity

`_SEETHROUGH_SET_HI_LIGHT_INTENSITY` · hash `0x19E50EB6E33E1D28` · **Cliente**

```lua
SeethroughSetHiLightIntensity(intensity)
```
```c
void _SEETHROUGH_SET_HI_LIGHT_INTENSITY(float intensity);
```

**Parámetros**

- `intensity` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x19E50EB6E33E1D28` (`N_0x19e50eb6e33e1d28`)

---
### SeethroughSetHiLightNoise

`_SEETHROUGH_SET_HI_LIGHT_NOISE` · hash `0x1636D7FC127B10D2` · **Cliente**

```lua
SeethroughSetHiLightNoise(noise)
```
```c
void _SEETHROUGH_SET_HI_LIGHT_NOISE(float noise);
```

**Parámetros**

- `noise` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1636D7FC127B10D2` (`N_0x1636d7fc127b10d2`)

---
### SeethroughSetMaxThickness

`_SEETHROUGH_SET_MAX_THICKNESS` · hash `0x0C8FAC83902A62DF` · **Cliente**

```lua
SeethroughSetMaxThickness(thickness)
```
```c
void _SEETHROUGH_SET_MAX_THICKNESS(float thickness);
```

**Parámetros**

- `thickness` (`float`): min: 1.0 max: 10000.0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0C8FAC83902A62DF` (`N_0x0c8fac83902a62df`)

---
### SeethroughSetNoiseAmountMax

`_SEETHROUGH_SET_NOISE_AMOUNT_MAX` · hash `0xFEBFBFDFB66039DE` · **Cliente**

```lua
SeethroughSetNoiseAmountMax(amount)
```
```c
void _SEETHROUGH_SET_NOISE_AMOUNT_MAX(float amount);
```

**Parámetros**

- `amount` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFEBFBFDFB66039DE` (`N_0xfebfbfdfb66039de`)

---
### SeethroughSetNoiseAmountMin

`_SEETHROUGH_SET_NOISE_AMOUNT_MIN` · hash `0xFF5992E1C9E65D05` · **Cliente**

```lua
SeethroughSetNoiseAmountMin(amount)
```
```c
void _SEETHROUGH_SET_NOISE_AMOUNT_MIN(float amount);
```

**Parámetros**

- `amount` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xFF5992E1C9E65D05` (`N_0xff5992e1c9e65d05`)

---
### SetArtificialLightsState

`SET_ARTIFICIAL_LIGHTS_STATE` · hash `0x1268615ACE24D504` · jhash `0xAA2A0EAF` · **Cliente**

```lua
SetArtificialLightsState(state)
```
```c
void SET_ARTIFICIAL_LIGHTS_STATE(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): True turns off all artificial light sources in the map: buildings, street lights, car lights, etc. False turns them back on.

**Devuelve:** `void`

**Descripción oficial:**

Does not affect weapons, particles, fire/explosions, flashlights or the sun.

When set to true, all emissive textures (including ped components that have light effects), street lights, building lights, vehicle lights, etc will all be turned off.

Used in Humane Labs Heist for EMP.

**Nombres antiguos (alias):** `_SET_BLACKOUT` (`SetBlackout`)

**Ejemplo (lua):**

```lua
-- Disable all lights in the map.
SetArtificialLightsState(true)

-- Enable all lights in the map.
SetArtificialLightsState(false)
```

**Ejemplo (cs):**

```cs
// Disable all lights in the map.
SetArtificialLightsState(true);

// Enable all lights in the map.
SetArtificialLightsState(false);
```

---
### SetArtificialLightsStateAffectsVehicles

`_SET_ARTIFICIAL_LIGHTS_STATE_AFFECTS_VEHICLES` · hash `0xE2B187C0939B3D32` · **Cliente**

```lua
SetArtificialLightsStateAffectsVehicles(toggle)
```
```c
void _SET_ARTIFICIAL_LIGHTS_STATE_AFFECTS_VEHICLES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

If "blackout" is enabled, this native allows you to ignore "blackout" for vehicles.

```
NativeDB Introduced: v2060
```

---
### SetBackfaceculling

`SET_BACKFACECULLING` · hash `0x23BA6B0C2AD7B0D3` · jhash `0xC44C2F44` · **Cliente**

```lua
SetBackfaceculling(toggle)
```
```c
void SET_BACKFACECULLING(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x23BA6B0C2AD7B0D3` (`N_0x23ba6b0c2ad7b0d3`)

---
### SetBinkMovie

`_SET_BINK_MOVIE` · hash `0x338D9F609FD632DB` · **Cliente**

```lua
local retval = SetBinkMovie(name)
```
```c
int _SET_BINK_MOVIE(char* name);
```

**Parámetros**

- `name` (`char*`): The BINK movie to play (with or without file extension).

**Devuelve:** `int`

**Descripción oficial:**

Creates an integer (usually 1) for a BINK movie to be called with other natives.
[List of all BINK movies (alphabetically ordered) as of b2802](https://gist.github.com/ItsJunction/8046f28c29ea8ff2821e9e4f933f595f)

**Nombres antiguos (alias):** `_SET_BINK_MOVIE_REQUESTED` (`SetBinkMovieRequested`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    local binkint = SetBinkMovie("casino_trailer")
    SetBinkMovieTime(binkint, 0.0) -- Seeks to 0%

    while (GetBinkMovieTime(binkint) < 100.0) do -- Very Basic Idea That Works?
        print(math.floor(GetBinkMovieTime(binkint) * 100)/100 .. "%") -- Prints current playtime (as percentage).
        PlayBinkMovie(binkint)
        DrawBinkMovie(binkint, 0.5, 0.5, 1.0, 1.0, 0.0, 255, 255, 255, 255) -- This example draws and plays in Fullscreen and in the center of screen (no matter the resolution).
        Citizen.Wait(0)
    end
end)
```

---
### SetBinkMovieTime

`_SET_BINK_MOVIE_TIME` · hash `0x0CB6B3446855B57A` · **Cliente**

```lua
SetBinkMovieTime(binkMovie, progress)
```
```c
void _SET_BINK_MOVIE_TIME(int binkMovie, float progress);
```

**Parámetros**

- `binkMovie` (`int`): The movie that is being played.
- `progress` (`float`): As a percentage (0.0 - 100.0).

**Devuelve:** `void`

**Descripción oficial:**

Seeks a BINK movie to a specified position.

**Nombres antiguos (alias):** `_SET_BINK_MOVIE_PROGRESS` (`SetBinkMovieProgress`)

**Ejemplo (lua):**

```lua
-- Movie drawn prior
SetBinkMovieTime(1, 50.0) -- Seeks to 50% in.
```

---
### SetBinkMovieUnk_2

`_SET_BINK_MOVIE_UNK_2` · hash `0xF816F2933752322D` · **Cliente**

```lua
SetBinkMovieUnk_2(binkMovie, p1)
```
```c
void _SET_BINK_MOVIE_UNK_2(int binkMovie, BOOL p1);
```

**Parámetros**

- `binkMovie` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### SetBinkMovieVolume

`_SET_BINK_MOVIE_VOLUME` · hash `0xAFF33B1178172223` · **Cliente**

```lua
SetBinkMovieVolume(binkMovie, value)
```
```c
void _SET_BINK_MOVIE_VOLUME(int binkMovie, float value);
```

**Parámetros**

- `binkMovie` (`int`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
binkMovie: Is return value from _SET_BINK_MOVIE. Has something to do with bink volume? (audRequestedSettings::SetVolumeCurveScale)
```

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `_SET_BINK_MOVIE_UNK` (`SetBinkMovieUnk`)

---
### SetBinkShouldSkip

`_SET_BINK_SHOULD_SKIP` · hash `0x6805D58CAA427B72` · **Cliente**

```lua
SetBinkShouldSkip(binkMovie, shouldSkip)
```
```c
void _SET_BINK_SHOULD_SKIP(int binkMovie, BOOL shouldSkip);
```

**Parámetros**

- `binkMovie` (`int`)
- `shouldSkip` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `_0x6805D58CAA427B72` (`N_0x6805d58caa427b72`)

---
### SetCheckpointCylinderHeight

`SET_CHECKPOINT_CYLINDER_HEIGHT` · hash `0x2707AAE9D9297D89` · jhash `0xFF0F9B22` · **Cliente**

```lua
SetCheckpointCylinderHeight(checkpoint, nearHeight, farHeight, radius)
```
```c
void SET_CHECKPOINT_CYLINDER_HEIGHT(int checkpoint, float nearHeight, float farHeight, float radius);
```

**Parámetros**

- `checkpoint` (`int`)
- `nearHeight` (`float`)
- `farHeight` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the cylinder height of the checkpoint.  
Parameters:  
* nearHeight - The height of the checkpoint when inside of the radius.  
* farHeight - The height of the checkpoint when outside of the radius.  
* radius - The radius of the checkpoint.  
```

---
### SetCheckpointIconHeight

`_SET_CHECKPOINT_ICON_HEIGHT` · hash `0x4B5B4DA5D79F1943` · jhash `0x80151CCF` · **Cliente**

```lua
SetCheckpointIconHeight(checkpoint, height_multiplier)
```
```c
void _SET_CHECKPOINT_ICON_HEIGHT(int checkpoint, float height_multiplier);
```

**Parámetros**

- `checkpoint` (`int`): The checkpoint the multiplier should be applied to.
- `height_multiplier` (`float`): The multiplier for the icon height above the checkpoint's coordinates. Default is 1.0

**Devuelve:** `void`

**Descripción oficial:**

This multiplies the height of the icon inside a checkpoint with the default height of about 2 units above the checkpoint's coordinates.

**Nombres antiguos (alias):** `0x4B5B4DA5D79F1943` (`N_0x4b5b4da5d79f1943`), `_SET_CHECKPOINT_SCALE` (`SetCheckpointScale`)

**Ejemplo (lua):**

```lua
local checkpoint = CreateCheckpoint(...)
SetCheckpointIconHeight(checkpoint, 2.0) -- places the icon two times as high as the default.
```

---
### SetCheckpointIconScale

`_SET_CHECKPOINT_ICON_SCALE` · hash `0x44621483FF966526` · **Cliente**

```lua
SetCheckpointIconScale(checkpoint, scale)
```
```c
void _SET_CHECKPOINT_ICON_SCALE(int checkpoint, float scale);
```

**Parámetros**

- `checkpoint` (`int`)
- `scale` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x44621483FF966526` (`N_0x44621483ff966526`)

---
### SetCheckpointRgba

`SET_CHECKPOINT_RGBA` · hash `0x7167371E8AD747F7` · jhash `0xEF9C8CB3` · **Cliente**

```lua
SetCheckpointRgba(checkpoint, red, green, blue, alpha)
```
```c
void SET_CHECKPOINT_RGBA(int checkpoint, int red, int green, int blue, int alpha);
```

**Parámetros**

- `checkpoint` (`int`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the checkpoint color.  
```

---
### SetCheckpointRgba2

`SET_CHECKPOINT_RGBA2` · hash `0xB9EA40907C680580` · jhash `0xA5456DBB` · **Cliente**

```lua
SetCheckpointRgba2(checkpoint, red, green, blue, alpha)
```
```c
void SET_CHECKPOINT_RGBA2(int checkpoint, int red, int green, int blue, int alpha);
```

**Parámetros**

- `checkpoint` (`int`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the checkpoint icon color.
```

**Nombres antiguos (alias):** `_SET_CHECKPOINT_ICON_RGBA` (`SetCheckpointIconRgba`)

---
### SetCurrentPlayerTcmodifier

`SET_CURRENT_PLAYER_TCMODIFIER` · hash `0xBBF327DED94E4DEB` · jhash `0x85BA15A4` · **Cliente**

```lua
SetCurrentPlayerTcmodifier(modifierName)
```
```c
void SET_CURRENT_PLAYER_TCMODIFIER(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBBF327DED94E4DEB` (`N_0xbbf327ded94e4deb`)

---
### SetDebugLinesAndSpheresDrawingActive

`SET_DEBUG_LINES_AND_SPHERES_DRAWING_ACTIVE` · hash `0x175B6BFC15CDD0C5` · jhash `0x1418CA37` · **Cliente**

```lua
SetDebugLinesAndSpheresDrawingActive(enabled)
```
```c
void SET_DEBUG_LINES_AND_SPHERES_DRAWING_ACTIVE(BOOL enabled);
```

**Parámetros**

- `enabled` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### SetDisableDecalRenderingThisFrame

`SET_DISABLE_DECAL_RENDERING_THIS_FRAME` · hash `0x4B5CFC83122DF602` · jhash `0xA706E84D` · **Cliente**

```lua
SetDisableDecalRenderingThisFrame()
```
```c
void SET_DISABLE_DECAL_RENDERING_THIS_FRAME();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x4B5CFC83122DF602` (`N_0x4b5cfc83122df602`)

---
### SetDisablePetrolDecalsIgnitingThisFrame

`SET_DISABLE_PETROL_DECALS_IGNITING_THIS_FRAME` · hash `0xD9454B5752C857DC` · jhash `0xEAB6417C` · **Cliente**

```lua
SetDisablePetrolDecalsIgnitingThisFrame()
```
```c
void SET_DISABLE_PETROL_DECALS_IGNITING_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Prevents gas / petrol decals (aka gas / petrol trails and puddles) to be ignited on fire during the frame in which the native is called.

**Note**: This native needs to be called every frame to prevent ignition.

**Nombres antiguos (alias):** `0xD9454B5752C857DC` (`N_0xd9454b5752c857dc`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    while true do
        SetDisablePetrolDecalsIgnitingThisFrame()
        Citizen.Wait(0)
    end
end)
```

---
### SetDrawOrigin

`SET_DRAW_ORIGIN` · hash `0xAA0008F3BBB8F416` · jhash `0xE10198D5` · **Cliente**

```lua
SetDrawOrigin(x, y, z, p3)
```
```c
void SET_DRAW_ORIGIN(float x, float y, float z, Any p3);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the on-screen drawing origin for draw-functions in world coordinates.

The effect can be reset by calling [`CLEAR_DRAW_ORIGIN`](#cleardraworigin) and is limited to 32 different origins each frame.

**Ejemplo (cs):**

```cs
// From now on, the screen coordinate which displays the given world coordinate on the screen is seen as x=0,y=0.  
Vector3 boneCoord = somePed.GetBoneCoord(Bone.SKEL_Head);  
Function.Call(Hash.SET_DRAW_ORIGIN, boneCoord.X, boneCoord.Y, boneCoord.Z, 0);  
Function.Call(Hash.DRAW_SPRITE, "helicopterhud", "hud_corner", -0.01, -0.015, 0.013, 0.013, 0.0, 255, 0, 0, 200);  
Function.Call(Hash.DRAW_SPRITE, "helicopterhud", "hud_corner", 0.01, -0.015, 0.013, 0.013, 90.0, 255, 0, 0, 200);  
Function.Call(Hash.DRAW_SPRITE, "helicopterhud", "hud_corner", -0.01, 0.015, 0.013, 0.013, 270.0, 255, 0, 0, 200);  
Function.Call(Hash.DRAW_SPRITE, "helicopterhud", "hud_corner", 0.01, 0.015, 0.013, 0.013, 180.0, 255, 0, 0, 200);  
Function.Call(Hash.CLEAR_DRAW_ORIGIN);
```

---
### SetEntityIconColor

`SET_ENTITY_ICON_COLOR` · hash `0x1D5F595CCAE2E238` · jhash `0x6EE1E946` · **Cliente**

```lua
SetEntityIconColor(entity, red, green, blue, alpha)
```
```c
void SET_ENTITY_ICON_COLOR(Entity entity, int red, int green, int blue, int alpha);
```

**Parámetros**

- `entity` (`Entity`)
- `red` (`int`)
- `green` (`int`)
- `blue` (`int`)
- `alpha` (`int`)

**Devuelve:** `void`

---
### SetEntityIconVisibility

`SET_ENTITY_ICON_VISIBILITY` · hash `0xE0E8BEECCA96BA31` · jhash `0xD1D2FD52` · **Cliente**

```lua
SetEntityIconVisibility(entity, toggle)
```
```c
void SET_ENTITY_ICON_VISIBILITY(Entity entity, BOOL toggle);
```

**Parámetros**

- `entity` (`Entity`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetExtraTimecycleModifier

`_SET_EXTRA_TIMECYCLE_MODIFIER` · hash `0x5096FD9CCB49056D` · jhash `0x908A335E` · **Cliente**

```lua
SetExtraTimecycleModifier(modifierName)
```
```c
void _SET_EXTRA_TIMECYCLE_MODIFIER(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`)

**Devuelve:** `void`

---
### SetFlash

`SET_FLASH` · hash `0x0AB84296FED9CFC6` · jhash `0x7E55A1EE` · **Cliente**

```lua
SetFlash(p0, p1, fadeIn, duration, fadeOut)
```
```c
void SET_FLASH(float p0, float p1, float fadeIn, float duration, float fadeOut);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `fadeIn` (`float`)
- `duration` (`float`)
- `fadeOut` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Purpose of p0 and p1 unknown.  
```

---
### SetForcePedFootstepsTracks

`_SET_FORCE_PED_FOOTSTEPS_TRACKS` · hash `0xAEEDAD1420C65CC0` · jhash `0xC53576CA` · **Cliente**

```lua
SetForcePedFootstepsTracks(toggle)
```
```c
void _SET_FORCE_PED_FOOTSTEPS_TRACKS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Forces footstep tracks on all surfaces.
USE_/USING_*
```

---
### SetForceVehicleTrails

`_SET_FORCE_VEHICLE_TRAILS` · hash `0x4CC7F0FEA5283FE0` · jhash `0x7158B1EA` · **Cliente**

```lua
SetForceVehicleTrails(toggle)
```
```c
void _SET_FORCE_VEHICLE_TRAILS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Forces vehicle trails on all surfaces.
USE_/USING_*
```

---
### SetHidofOverride

`SET_HIDOF_OVERRIDE` · hash `0xBA3D65906822BED5` · jhash `0x513D444B` · **Cliente**

```lua
SetHidofOverride(p0, p1, nearplaneOut, nearplaneIn, farplaneOut, farplaneIn)
```
```c
void SET_HIDOF_OVERRIDE(BOOL p0, BOOL p1, float nearplaneOut, float nearplaneIn, float farplaneOut, float farplaneIn);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)
- `nearplaneOut` (`float`)
- `nearplaneIn` (`float`)
- `farplaneOut` (`float`)
- `farplaneIn` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBA3D65906822BED5` (`N_0xba3d65906822bed5`), `_SET_HIDOF_ENV_BLUR_PARAMS` (`SetHidofEnvBlurParams`)

---
### SetNextPlayerTcmodifier

`SET_NEXT_PLAYER_TCMODIFIER` · hash `0xBF59707B3E5ED531` · jhash `0x554BA16E` · **Cliente**

```lua
SetNextPlayerTcmodifier(modifierName)
```
```c
void SET_NEXT_PLAYER_TCMODIFIER(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBF59707B3E5ED531` (`N_0xbf59707b3e5ed531`)

---
### SetNightvision

`SET_NIGHTVISION` · hash `0x18F621F7A5B1F85D` · jhash `0xD1E5565F` · **Cliente**

```lua
SetNightvision(toggle)
```
```c
void SET_NIGHTVISION(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enables Night Vision.  
Example:  
C#: Function.Call(Hash.SET_NIGHTVISION, true);  
C++: GRAPHICS::SET_NIGHTVISION(true);  
BOOL toggle:  
true = turns night vision on for your player.  
false = turns night vision off for your player.  
```

---
### SetNoiseoveride

`SET_NOISEOVERIDE` · hash `0xE787BF1C5CF823C9` · jhash `0xD576F5DD` · **Cliente**

```lua
SetNoiseoveride(toggle)
```
```c
void SET_NOISEOVERIDE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetNoisinessoveride

`SET_NOISINESSOVERIDE` · hash `0xCB6A7C3BB17A0C67` · jhash `0x046B62D9` · **Cliente**

```lua
SetNoisinessoveride(value)
```
```c
void SET_NOISINESSOVERIDE(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `void`

---
### SetParticleFxBulletImpactScale

`SET_PARTICLE_FX_BULLET_IMPACT_SCALE` · hash `0x27E32866E9A5C416` · jhash `0xC1AD5DDF` · **Cliente**

```lua
SetParticleFxBulletImpactScale(scale)
```
```c
void SET_PARTICLE_FX_BULLET_IMPACT_SCALE(float scale);
```

**Parámetros**

- `scale` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x27E32866E9A5C416` (`N_0x27e32866e9a5c416`)

---
### SetParticleFxCamInsideNonplayerVehicle

`SET_PARTICLE_FX_CAM_INSIDE_NONPLAYER_VEHICLE` · hash `0xACEE6F360FC1F6B6` · jhash `0x6B125A02` · **Cliente**

```lua
SetParticleFxCamInsideNonplayerVehicle(vehicle, p1)
```
```c
void SET_PARTICLE_FX_CAM_INSIDE_NONPLAYER_VEHICLE(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### SetParticleFxCamInsideVehicle

`SET_PARTICLE_FX_CAM_INSIDE_VEHICLE` · hash `0xEEC4047028426510` · jhash `0x19EC0001` · **Cliente**

```lua
SetParticleFxCamInsideVehicle(p0)
```
```c
void SET_PARTICLE_FX_CAM_INSIDE_VEHICLE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### SetParticleFxLoopedAlpha

`SET_PARTICLE_FX_LOOPED_ALPHA` · hash `0x726845132380142E` · jhash `0x5ED49BE1` · **Cliente**

```lua
SetParticleFxLoopedAlpha(ptfxHandle, alpha)
```
```c
void SET_PARTICLE_FX_LOOPED_ALPHA(int ptfxHandle, float alpha);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `alpha` (`float`)

**Devuelve:** `void`

---
### SetParticleFxLoopedColour

`SET_PARTICLE_FX_LOOPED_COLOUR` · hash `0x7F8F65877F88783B` · jhash `0x5219D530` · **Cliente**

```lua
SetParticleFxLoopedColour(ptfxHandle, r, g, b, bLocalOnly)
```
```c
void SET_PARTICLE_FX_LOOPED_COLOUR(int ptfxHandle, float r, float g, float b, BOOL bLocalOnly);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `r` (`float`): range from 0.0 to 1.0
- `g` (`float`): range from 0.0 to 1.0
- `b` (`float`): range from 0.0 to 1.0
- `bLocalOnly` (`BOOL`): False by default. Defines whether the effect should be sent and modified over the network or not. Set this to `true` if you don't want to send the effect over the network.

**Devuelve:** `void`

**Descripción oficial:**

Sets the colour tint of a previously started looped particle effect

You can use the [inverse lerp](https://www.gamedev.net/articles/programming/general-and-gameplay-programming/inverse-lerp-a-super-useful-yet-often-overlooked-function-r5230/) method to normalize in a range from 0.0 to 1.0 an rgb

---
### SetParticleFxLoopedEvolution

`SET_PARTICLE_FX_LOOPED_EVOLUTION` · hash `0x5F0C4B5B1C393BE2` · jhash `0x1CBC1373` · **Cliente**

```lua
SetParticleFxLoopedEvolution(ptfxHandle, propertyName, amount, noNetwork)
```
```c
void SET_PARTICLE_FX_LOOPED_EVOLUTION(int ptfxHandle, char* propertyName, float amount, BOOL noNetwork);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `propertyName` (`char*`)
- `amount` (`float`)
- `noNetwork` (`BOOL`)

**Devuelve:** `void`

---
### SetParticleFxLoopedFarClipDist

`SET_PARTICLE_FX_LOOPED_FAR_CLIP_DIST` · hash `0xDCB194B85EF7B541` · jhash `0x233DE879` · **Cliente**

```lua
SetParticleFxLoopedFarClipDist(ptfxHandle, range)
```
```c
void SET_PARTICLE_FX_LOOPED_FAR_CLIP_DIST(int ptfxHandle, float range);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `range` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_PARTICLE_FX_LOOPED_RANGE` (`SetParticleFxLoopedRange`)

---
### SetParticleFxLoopedOffsets

`SET_PARTICLE_FX_LOOPED_OFFSETS` · hash `0xF7DDEBEC43483C43` · jhash `0x641F7790` · **Cliente**

```lua
SetParticleFxLoopedOffsets(ptfxHandle, x, y, z, rotX, rotY, rotZ)
```
```c
void SET_PARTICLE_FX_LOOPED_OFFSETS(int ptfxHandle, float x, float y, float z, float rotX, float rotY, float rotZ);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)

**Devuelve:** `void`

---
### SetParticleFxLoopedScale

`SET_PARTICLE_FX_LOOPED_SCALE` · hash `0xB44250AAA456492D` · jhash `0x099B8B49` · **Cliente**

```lua
SetParticleFxLoopedScale(ptfxHandle, scale)
```
```c
void SET_PARTICLE_FX_LOOPED_SCALE(int ptfxHandle, float scale);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `scale` (`float`)

**Devuelve:** `void`

---
### SetParticleFxNonLoopedAlpha

`SET_PARTICLE_FX_NON_LOOPED_ALPHA` · hash `0x77168D722C58B2FC` · jhash `0x497EAFF2` · **Cliente**

```lua
SetParticleFxNonLoopedAlpha(alpha)
```
```c
void SET_PARTICLE_FX_NON_LOOPED_ALPHA(float alpha);
```

**Parámetros**

- `alpha` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Usage example for C#:  
Function.Call(Hash.SET_PARTICLE_FX_NON_LOOPED_ALPHA, new InputArgument[] { 0.1f });  
		Note: the argument alpha ranges from 0.0f-1.0f !  
```

---
### SetParticleFxNonLoopedColour

`SET_PARTICLE_FX_NON_LOOPED_COLOUR` · hash `0x26143A59EF48B262` · jhash `0x7B689E20` · **Cliente**

```lua
SetParticleFxNonLoopedColour(r, g, b)
```
```c
void SET_PARTICLE_FX_NON_LOOPED_COLOUR(float r, float g, float b);
```

**Parámetros**

- `r` (`float`): Red (0.0 - 1.0)
- `g` (`float`): Green (0.0 - 1.0)
- `b` (`float`): Blue (0.0 - 1.0)

**Devuelve:** `void`

**Descripción oficial:**

Only works on some fx's, while on others it might SEEM to work "properly", but the colors can be "strange" or even completly different from what you've expected. Reason for this is that those fx's might already have colors "baked into them" which then start to act as a "mixing palette", resulting in a different color than expected. A hypothetical example of this would be if the fx itself is already full (bright) red (RGB: 1.0, 0.0, 0.0) and you then set the color to (bright) green (RGB: 0.0, 1.0, 0.0), that it MIGHT result in Yellow (RGB: 1.0, 1.0, 0.0).

This doc previously stated that the set color is **NOT** networked, however it does actually turns out to be networked. Tested with all fireworks effects and several other FX effects resulted in colored fx effects on all clients when used in combination with [START_NETWORKED_PARTICLE_FX_NON_LOOPED_AT_COORD](#startnetworkedparticlefxnonloopedatcoord).
This might however not be the case for all types of particle fx's, so it's recommended to test this thoroughly with multiple clients before releasing your script for example.

---
### SetParticleFxNonLoopedEmitterScale

`_SET_PARTICLE_FX_NON_LOOPED_EMITTER_SCALE` · hash `0x1E2E01C00837D26E` · **Cliente**

```lua
SetParticleFxNonLoopedEmitterScale(p0, p1, scale)
```
```c
void _SET_PARTICLE_FX_NON_LOOPED_EMITTER_SCALE(float p0, float p1, float scale);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `scale` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### SetParticleFxOverride

`SET_PARTICLE_FX_OVERRIDE` · hash `0xEA1E2D93F6F75ED9` · jhash `0xC92719A7` · **Cliente**

```lua
SetParticleFxOverride(oldAsset, newAsset)
```
```c
void SET_PARTICLE_FX_OVERRIDE(char* oldAsset, char* newAsset);
```

**Parámetros**

- `oldAsset` (`char*`)
- `newAsset` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_PTFX_ASSET_OLD_2_NEW` (`SetPtfxAssetOld_2New`), `_SET_PARTICLE_FX_ASSET_OLD_TO_NEW` (`SetParticleFxAssetOldToNew`)

---
### SetParticleFxShootoutBoat

`SET_PARTICLE_FX_SHOOTOUT_BOAT` · hash `0x96EF97DAEB89BEF5` · jhash `0xD938DEE0` · **Cliente**

```lua
SetParticleFxShootoutBoat(p0)
```
```c
void SET_PARTICLE_FX_SHOOTOUT_BOAT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### SetPlayerTcmodifierTransition

`SET_PLAYER_TCMODIFIER_TRANSITION` · hash `0xBDEB86F4D5809204` · jhash `0x9559BB38` · **Cliente**

```lua
SetPlayerTcmodifierTransition(value)
```
```c
void SET_PLAYER_TCMODIFIER_TRANSITION(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBDEB86F4D5809204` (`N_0xbdeb86f4d5809204`)

---
### SetScaleformMovieAsNoLongerNeeded

`SET_SCALEFORM_MOVIE_AS_NO_LONGER_NEEDED` · hash `0x1D132D614DD86811` · jhash `0x5FED3BA1` · **Cliente**

```lua
local scaleformHandle = SetScaleformMovieAsNoLongerNeeded(scaleformHandle)
```
```c
void SET_SCALEFORM_MOVIE_AS_NO_LONGER_NEEDED(int* scaleformHandle);
```

**Parámetros**

- `scaleformHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### SetScaleformMovieToUseLargeRt

`SET_SCALEFORM_MOVIE_TO_USE_LARGE_RT` · hash `0x32F34FF7F617643B` · **Cliente**

```lua
SetScaleformMovieToUseLargeRt(scaleformMovieId, useLargeRT)
```
```c
void SET_SCALEFORM_MOVIE_TO_USE_LARGE_RT(int scaleformMovieId, BOOL useLargeRT);
```

**Parámetros**

- `scaleformMovieId` (`int`): The handle of the Scaleform to be used.
- `useLargeRT` (`BOOL`): A boolean switch to enable/disable the use of the large rendertarget.

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v573
```

Configures a Scaleform movie to render to a large render target (1280x720), which is useful for ensuring higher quality and clarity in certain display scenarios. Such as displaying the name of an organization (CEO Office) in a visually impactful way for example.

**Nombres antiguos (alias):** `0x32F34FF7F617643B` (`N_0x32f34ff7f617643b`)

---
### SetScaleformMovieToUseSuperLargeRt

`SET_SCALEFORM_MOVIE_TO_USE_SUPER_LARGE_RT` · hash `0xE6A9F00D4240B519` · **Cliente**

```lua
SetScaleformMovieToUseSuperLargeRt(scaleformHandle, toggle)
```
```c
void SET_SCALEFORM_MOVIE_TO_USE_SUPER_LARGE_RT(int scaleformHandle, BOOL toggle);
```

**Parámetros**

- `scaleformHandle` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Adjusts a scaleform movie's dimensions to fit a large rendertarget. Mostly used in casino scripts.

**Nombres antiguos (alias):** `0xE6A9F00D4240B519` (`N_0xe6a9f00d4240b519`), `_SET_SCALEFORM_FIT_RENDERTARGET` (`SetScaleformFitRendertarget`)

---
### SetScaleformMovieToUseSystemTime

`SET_SCALEFORM_MOVIE_TO_USE_SYSTEM_TIME` · hash `0x6D8EB211944DCE08` · jhash `0x18C9DE8D` · **Cliente**

```lua
SetScaleformMovieToUseSystemTime(scaleform, toggle)
```
```c
void SET_SCALEFORM_MOVIE_TO_USE_SYSTEM_TIME(int scaleform, BOOL toggle);
```

**Parámetros**

- `scaleform` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetScriptGfxAlign

`SET_SCRIPT_GFX_ALIGN` · hash `0xB8A850F20A067EB6` · jhash `0x228A2598` · **Cliente**

```lua
SetScriptGfxAlign(horizontalAlign, verticalAlign)
```
```c
void SET_SCRIPT_GFX_ALIGN(int horizontalAlign, int verticalAlign);
```

**Parámetros**

- `horizontalAlign` (`int`): The horizontal alignment. This can be 67 ('C'), 76 ('L'), or 82 ('R').
- `verticalAlign` (`int`): The vertical alignment. This can be 67 ('C'), 66 ('B'), or 84 ('T').

**Devuelve:** `void`

**Descripción oficial:**

This function anchors script draws to a side of the safe zone. This needs to be called to make the interface
independent of the player's safe zone configuration.

These values are equivalent to `alignX` and `alignY` in `common:/data/ui/frontend.xml`, which can be used as a baseline
for default alignment.

Valid values for `horizontalAlign`, from original documentation:

*   **C (67)** - Center: DRAW_TEXT starts in the middle of the screen, while DRAW_RECT starts on the right; both move with
    the right side of the screen.
*   **L (76)** - Left: Anchors to the left side, DRAW_RECT starts on the left side of the screen, same as DRAW_TEXT when
    centered.
*   **R (82)** - Right: DRAW_TEXT starts on the left side (normal 0,0), while DRAW_RECT starts some short distance away
    from the right side of the screen, both move with the right side of the screen.

Valid values for `verticalAlign`, from original documentation:

*   **B (66)** - Bottom: DRAW_RECT starts about as far as the middle of the map from the bottom, while DRAW_TEXT is about
    rather centered.
*   **C (67)** - Center: It starts at a certain distance from the bottom, but the distance is fixed, the distance is
    different from 66.
*   **T (84)** - Top: Anchors to the top, DRAW_RECT starts on the top of the screen, DRAW_TEXT just below it.

Using any other value (including 0) will result in the safe zone not being taken into account for this draw. The
canonical value for this is 'I' (73).

For example, you can use `SET_SCRIPT_GFX_ALIGN(0, 84)` to only scale on the Y axis (to the top), but not change the X
axis.

To reset the value, use `RESET_SCRIPT_GFX_ALIGN`.

**Nombres antiguos (alias):** `_SET_SCREEN_DRAW_POSITION` (`SetScreenDrawPosition`), `_SCREEN_DRAW_POSITION_BEGIN` (`ScreenDrawPositionBegin`)

**Ejemplo (lua):**

```lua
-- align the next draw to the top left
SetScriptGfxAlign(string.byte('L'), string.byte('T'))

-- prints "THIS LABEL NEEDS TO BE HERE !!!"
BeginTextCommandDisplayText('DUMMY1')
EndTextCommandDisplayText(0.0, 0.0)

-- reset the script draw alignment
ResetScriptGfxAlign()
```

---
### SetScriptGfxAlignParams

`SET_SCRIPT_GFX_ALIGN_PARAMS` · hash `0xF5A2C681787E579D` · jhash `0x76C641E4` · **Cliente**

```lua
SetScriptGfxAlignParams(x, y, w, h)
```
```c
void SET_SCRIPT_GFX_ALIGN_PARAMS(float x, float y, float w, float h);
```

**Parámetros**

- `x` (`float`): The X offset for the item to be drawn.
- `y` (`float`): The Y offset for the item to be drawn.
- `w` (`float`): The width of the item to be drawn.
- `h` (`float`): The height of the item to be drawn.

**Devuelve:** `void`

**Descripción oficial:**

Sets the draw offset/calculated size for `SET_SCRIPT_GFX_ALIGN`. If using any alignment other than left/top, the game
expects the width/height to be configured using this native in order to get a proper starting position for the draw
command.

**Nombres antiguos (alias):** `0xF5A2C681787E579D` (`N_0xf5a2c681787e579d`), `_SCREEN_DRAW_POSITION_RATIO` (`ScreenDrawPositionRatio`)

---
### SetScriptGfxDrawBehindPausemenu

`SET_SCRIPT_GFX_DRAW_BEHIND_PAUSEMENU` · hash `0xC6372ECD45D73BCD` · jhash `0xF8FBCC25` · **Cliente**

```lua
SetScriptGfxDrawBehindPausemenu(flag)
```
```c
void SET_SCRIPT_GFX_DRAW_BEHIND_PAUSEMENU(BOOL flag);
```

**Parámetros**

- `flag` (`BOOL`): A boolean value.

**Devuelve:** `void`

**Descripción oficial:**

Sets a flag defining whether or not script draw commands should continue being drawn behind the pause menu. This is usually used for TV channels and other draw commands that are used with a world render target.

**Nombres antiguos (alias):** `0xC6372ECD45D73BCD` (`N_0xc6372ecd45d73bcd`)

---
### SetScriptGfxDrawOrder

`SET_SCRIPT_GFX_DRAW_ORDER` · hash `0x61BB1D9B3A95D802` · jhash `0xADF81D24` · **Cliente**

```lua
SetScriptGfxDrawOrder(order)
```
```c
void SET_SCRIPT_GFX_DRAW_ORDER(int order);
```

**Parámetros**

- `order` (`int`): The intended draw order/layer.

**Devuelve:** `void`

**Descripción oficial:**

Sets the draw order for script draw commands.
Examples from decompiled scripts:
GRAPHICS::SET_SCRIPT_GFX_DRAW_ORDER(7);
GRAPHICS::DRAW_RECT(0.5, 0.5, 3.0, 3.0, v\_4, v\_5, v\_6, a\_0.\_f172, 0);
GRAPHICS::SET_SCRIPT_GFX_DRAW_ORDER(1);
GRAPHICS::DRAW_RECT(0.5, 0.5, 1.5, 1.5, 0, 0, 0, 255, 0);

```cpp
enum eGfxDrawOrder
{
    GFX_ORDER_BEFORE_HUD_PRIORITY_LOW = 0,
    GFX_ORDER_BEFORE_HUD = 1,
    GFX_ORDER_BEFORE_HUD_PRIORITY_HIGH = 2,
    GFX_ORDER_AFTER_HUD_PRIORITY_LOW = 3,
    GFX_ORDER_AFTER_HUD = 4,
    GFX_ORDER_AFTER_HUD_PRIORITY_HIGH = 5,
    GFX_ORDER_AFTER_FADE_PRIORITY_LOW = 6,
    GFX_ORDER_AFTER_FADE = 7,
    GFX_ORDER_AFTER_FADE_PRIORITY_HIGH = 8,
}
```

**Nombres antiguos (alias):** `0x61BB1D9B3A95D802` (`N_0x61bb1d9b3a95d802`), `_SET_2D_LAYER` (`Set_2dLayer`), `_SET_UI_LAYER` (`SetUiLayer`)

---
### SetSeethrough

`SET_SEETHROUGH` · hash `0x7E08924259E08CE0` · jhash `0x74D4995C` · **Cliente**

```lua
SetSeethrough(toggle)
```
```c
void SET_SEETHROUGH(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Toggles Heatvision on/off.  
```

---
### SetStreamedTextureDictAsNoLongerNeeded

`SET_STREAMED_TEXTURE_DICT_AS_NO_LONGER_NEEDED` · hash `0xBE2CACCF5A8AA805` · jhash `0xF07DDA38` · **Cliente**

```lua
SetStreamedTextureDictAsNoLongerNeeded(textureDict)
```
```c
void SET_STREAMED_TEXTURE_DICT_AS_NO_LONGER_NEEDED(char* textureDict);
```

**Parámetros**

- `textureDict` (`char*`)

**Devuelve:** `void`

---
### SetTimecycleModifier

`SET_TIMECYCLE_MODIFIER` · hash `0x2C933ABF17A1DF41` · jhash `0xA81F3638` · **Cliente**

```lua
SetTimecycleModifier(modifierName)
```
```c
void SET_TIMECYCLE_MODIFIER(char* modifierName);
```

**Parámetros**

- `modifierName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Loads the specified timecycle modifier. Modifiers are defined separately in another file (e.g. "timecycle_mods_1.xml")
Parameters:
modifierName - The modifier to load (e.g. "V_FIB_IT3", "scanline_cam", etc.)
```

---
### SetTimecycleModifierStrength

`SET_TIMECYCLE_MODIFIER_STRENGTH` · hash `0x82E7FFCD5B2326B3` · jhash `0x458F4F45` · **Cliente**

```lua
SetTimecycleModifierStrength(strength)
```
```c
void SET_TIMECYCLE_MODIFIER_STRENGTH(float strength);
```

**Parámetros**

- `strength` (`float`)

**Devuelve:** `void`

---
### SetTrackedPointInfo

`SET_TRACKED_POINT_INFO` · hash `0x164ECBB3CF750CB0` · jhash `0x28689AA4` · **Cliente**

```lua
SetTrackedPointInfo(point, x, y, z, radius)
```
```c
void SET_TRACKED_POINT_INFO(int point, float x, float y, float z, float radius);
```

**Parámetros**

- `point` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

---
### SetTransitionOutOfTimecycleModifier

`SET_TRANSITION_OUT_OF_TIMECYCLE_MODIFIER` · hash `0x1CBA05AE7BD7EE05` · jhash `0x56345F6B` · **Cliente**

```lua
SetTransitionOutOfTimecycleModifier(transitionTime)
```
```c
void SET_TRANSITION_OUT_OF_TIMECYCLE_MODIFIER(float transitionTime);
```

**Parámetros**

- `transitionTime` (`float`): How long the transition should take (In seconds)

**Devuelve:** `void`

**Descripción oficial:**

Transitions current timecycle modifier out.

**Nombres antiguos (alias):** `0x1CBA05AE7BD7EE05` (`N_0x1cba05ae7bd7ee05`)

---
### SetTransitionTimecycleModifier

`SET_TRANSITION_TIMECYCLE_MODIFIER` · hash `0x3BCF567485E1971C` · jhash `0xBB2BA72A` · **Cliente**

```lua
SetTransitionTimecycleModifier(modifierName, transition)
```
```c
void SET_TRANSITION_TIMECYCLE_MODIFIER(char* modifierName, float transition);
```

**Parámetros**

- `modifierName` (`char*`): The name of a timecycle
- `transition` (`float`): The speed to transition to `modifierName`. Appears to be half-seconds (?)

**Devuelve:** `void`

**Descripción oficial:**

This native doesn't work like [`SetWeatherTypeTransition`](MISC.md#setweathertypetransition).

---
### SetTvAudioFrontend

`SET_TV_AUDIO_FRONTEND` · hash `0x113D2C5DC57E1774` · jhash `0x2E0DFA35` · **Cliente**

```lua
SetTvAudioFrontend(toggle)
```
```c
void SET_TV_AUDIO_FRONTEND(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Probably changes tvs from being a 3d audio to being "global" audio
```

---
### SetTvChannel

`SET_TV_CHANNEL` · hash `0xBAABBB23EB6E484E` · jhash `0x41A8A627` · **Cliente**

```lua
SetTvChannel(channel)
```
```c
void SET_TV_CHANNEL(int channel);
```

**Parámetros**

- `channel` (`int`)

**Devuelve:** `void`

---
### SetTvChannelPlaylist

`SET_TV_CHANNEL_PLAYLIST` · hash `0xF7B38B8305F1FE8B` · jhash `0xB262DE67` · **Cliente**

```lua
SetTvChannelPlaylist(tvChannel, playlistName, restart)
```
```c
void SET_TV_CHANNEL_PLAYLIST(int tvChannel, char* playlistName, BOOL restart);
```

**Parámetros**

- `tvChannel` (`int`)
- `playlistName` (`char*`)
- `restart` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Loads specified video sequence into the TV Channel
TV_Channel ranges from 0-2
VideoSequence can be any of the following:
"PL_STD_CNT" CNT Standard Channel
"PL_STD_WZL" Weazel Standard Channel
"PL_LO_CNT"
"PL_LO_WZL"
"PL_SP_WORKOUT"
"PL_SP_INV" - Jay Norris Assassination Mission Fail
"PL_SP_INV_EXP" - Jay Norris Assassination Mission Success
"PL_LO_RS" - Righteous Slaughter Ad
"PL_LO_RS_CUTSCENE" - Righteous Slaughter Cut-scene
"PL_SP_PLSH1\_INTRO"
"PL_LES1\_FAME_OR_SHAME"
"PL_STD_WZL_FOS_EP2"
"PL_MP_WEAZEL" - Weazel Logo on loop
"PL_MP_CCTV" - Generic CCTV loop
Restart:
0=video sequence continues as normal
1=sequence restarts from beginning every time that channel is selected
The above playlists work as intended, and are commonly used, but there are many more playlists, as seen in `tvplaylists.xml`. A pastebin below outlines all playlists, they will be surronded by the name tag I.E. (<Name>PL_STD_CNT</Name> = PL_STD_CNT).
https://pastebin.com/zUzGB6h7

**Nombres antiguos (alias):** `0xF7B38B8305F1FE8B` (`N_0xf7b38b8305f1fe8b`), `_LOAD_TV_CHANNEL_SEQUENCE` (`LoadTvChannelSequence`)

---
### SetTvChannelPlaylistAtHour

`SET_TV_CHANNEL_PLAYLIST_AT_HOUR` · hash `0x2201C576FACAEBE8` · jhash `0x78C4DCBE` · **Cliente**

```lua
SetTvChannelPlaylistAtHour(tvChannel, playlistName, hour)
```
```c
void SET_TV_CHANNEL_PLAYLIST_AT_HOUR(int tvChannel, char* playlistName, int hour);
```

**Parámetros**

- `tvChannel` (`int`)
- `playlistName` (`char*`)
- `hour` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2201C576FACAEBE8` (`N_0x2201c576facaebe8`)

---
### SetTvVolume

`SET_TV_VOLUME` · hash `0x2982BF73F66E9DDC` · jhash `0xF3504F4D` · **Cliente**

```lua
SetTvVolume(volume)
```
```c
void SET_TV_VOLUME(float volume);
```

**Parámetros**

- `volume` (`float`)

**Devuelve:** `void`

---
### StartNetworkedParticleFxLoopedOnEntity

`START_NETWORKED_PARTICLE_FX_LOOPED_ON_ENTITY` · hash `0x6F60E89A7B64EE1D` · jhash `0x110752B2` · **Cliente**

```lua
local retval = StartNetworkedParticleFxLoopedOnEntity(effectName, entity, xOffset, yOffset, zOffset, xRot, yRot, zRot, scale, xAxis, yAxis, zAxis)
```
```c
int START_NETWORKED_PARTICLE_FX_LOOPED_ON_ENTITY(char* effectName, Entity entity, float xOffset, float yOffset, float zOffset, float xRot, float yRot, float zRot, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis);
```

**Parámetros**

- `effectName` (`char*`)
- `entity` (`Entity`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
network fx  
```

```
NativeDB Added Parameter 13: Any p12
NativeDB Added Parameter 14: Any p13
NativeDB Added Parameter 15: Any p14
NativeDB Added Parameter 16: Any p15
```

**Nombres antiguos (alias):** `0x6F60E89A7B64EE1D` (`N_0x6f60e89a7b64ee1d`), `_START_PARTICLE_FX_LOOPED_ON_ENTITY_2` (`StartParticleFxLoopedOnEntity_2`)

---
### StartNetworkedParticleFxLoopedOnEntityBone

`START_NETWORKED_PARTICLE_FX_LOOPED_ON_ENTITY_BONE` · hash `0xDDE23F30CC5A0F03` · jhash `0xF478EFCF` · **Cliente**

```lua
local retval = StartNetworkedParticleFxLoopedOnEntityBone(effectName, entity, xOffset, yOffset, zOffset, xRot, yRot, zRot, boneIndex, scale, xAxis, yAxis, zAxis)
```
```c
int START_NETWORKED_PARTICLE_FX_LOOPED_ON_ENTITY_BONE(char* effectName, Entity entity, float xOffset, float yOffset, float zOffset, float xRot, float yRot, float zRot, int boneIndex, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis);
```

**Parámetros**

- `effectName` (`char*`)
- `entity` (`Entity`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `boneIndex` (`int`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
network fx  
```

```
NativeDB Added Parameter 14: Any p13
NativeDB Added Parameter 15: Any p14
NativeDB Added Parameter 16: Any p15
NativeDB Added Parameter 17: Any p16
```

**Nombres antiguos (alias):** `0xDDE23F30CC5A0F03` (`N_0xdde23f30cc5a0f03`), `_START_PARTICLE_FX_LOOPED_ON_ENTITY_BONE_2` (`StartParticleFxLoopedOnEntityBone_2`)

---
### StartNetworkedParticleFxNonLoopedAtCoord

`START_NETWORKED_PARTICLE_FX_NON_LOOPED_AT_COORD` · hash `0xF56B8137DF10135D` · jhash `0x633F8C48` · **Cliente**

```lua
local retval = StartNetworkedParticleFxNonLoopedAtCoord(effectName, xPos, yPos, zPos, xRot, yRot, zRot, scale, xAxis, yAxis, zAxis)
```
```c
BOOL START_NETWORKED_PARTICLE_FX_NON_LOOPED_AT_COORD(char* effectName, float xPos, float yPos, float zPos, float xRot, float yRot, float zRot, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis);
```

**Parámetros**

- `effectName` (`char*`)
- `xPos` (`float`)
- `yPos` (`float`)
- `zPos` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

NOTE: the [USE_PARTICLE_FX_ASSET](#useparticlefxasset) needs to be called before EVERY StartNetworkedParticleFxNonLoopedAtCoord(....) call!

List with lots of particle effects: https://gist.githubusercontent.com/alexguirre/af70f0122957f005a5c12bef2618a786/raw/899e93c5611ba58138c56873bb6f56664a776af4/Particles%2520Effects%2520Dump.txt

Note: Not all particles on this list are for non looped and vice versa, neither are all of them suited/meant to have SetParticleFxNonLoopedColour(....) called on them.

```
NativeDB Added Parameter 12: BOOL p11
```

**Nombres antiguos (alias):** `_START_PARTICLE_FX_NON_LOOPED_AT_COORD_2` (`StartParticleFxNonLoopedAtCoord_2`)

**Ejemplo (lua):**

```lua
-- If the PtfxAsset hasn't been loaded yet, you'll need to load it first
if not HasNamedPtfxAssetLoaded("scr_indep_fireworks") then
	RequestNamedPtfxAsset("scr_indep_fireworks")
	while not HasNamedPtfxAssetLoaded("scr_indep_fireworks") do
		Wait(10)
	end
end

local CurrentPlayerCoords = GetEntityCoords(GetPlayerPed(-1))

UseParticleFxAssetNextCall("scr_indep_fireworks") -- Prepare the Particle FX for the next upcomming Particle FX call
SetParticleFxNonLoopedColour(1.0, 0.0, 0.0) -- Setting the color to Red (R, G, B)
StartNetworkedParticleFxNonLoopedAtCoord("scr_indep_firework_burst_spawn", CurrentPlayerCoords, 0.0, 0.0, 0.0, 1.0, false, false, false, false) -- Start the animation itself

RemoveNamedPtfxAsset("scr_indep_fireworks") -- Clean up
```

---
### StartNetworkedParticleFxNonLoopedOnEntity

`START_NETWORKED_PARTICLE_FX_NON_LOOPED_ON_ENTITY` · hash `0xC95EB1DB6E92113D` · jhash `0x469A2B4A` · **Cliente**

```lua
local retval = StartNetworkedParticleFxNonLoopedOnEntity(effectName, entity, offsetX, offsetY, offsetZ, rotX, rotY, rotZ, scale, axisX, axisY, axisZ)
```
```c
BOOL START_NETWORKED_PARTICLE_FX_NON_LOOPED_ON_ENTITY(char* effectName, Entity entity, float offsetX, float offsetY, float offsetZ, float rotX, float rotY, float rotZ, float scale, BOOL axisX, BOOL axisY, BOOL axisZ);
```

**Parámetros**

- `effectName` (`char*`)
- `entity` (`Entity`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `scale` (`float`)
- `axisX` (`BOOL`)
- `axisY` (`BOOL`)
- `axisZ` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_START_PARTICLE_FX_NON_LOOPED_ON_ENTITY_2` (`StartParticleFxNonLoopedOnEntity_2`)

---
### StartNetworkedParticleFxNonLoopedOnEntityBone

`_START_NETWORKED_PARTICLE_FX_NON_LOOPED_ON_ENTITY_BONE` · hash `0x02B1F2A72E0F5325` · **Cliente**

```lua
local retval = StartNetworkedParticleFxNonLoopedOnEntityBone(effectName, entity, offsetX, offsetY, offsetZ, rotX, rotY, rotZ, boneIndex, scale, axisX, axisY, axisZ)
```
```c
BOOL _START_NETWORKED_PARTICLE_FX_NON_LOOPED_ON_ENTITY_BONE(char* effectName, Entity entity, float offsetX, float offsetY, float offsetZ, float rotX, float rotY, float rotZ, int boneIndex, float scale, BOOL axisX, BOOL axisY, BOOL axisZ);
```

**Parámetros**

- `effectName` (`char*`)
- `entity` (`Entity`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `boneIndex` (`int`)
- `scale` (`float`)
- `axisX` (`BOOL`)
- `axisY` (`BOOL`)
- `axisZ` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### StartNetworkedParticleFxNonLoopedOnPedBone

`START_NETWORKED_PARTICLE_FX_NON_LOOPED_ON_PED_BONE` · hash `0xA41B6A43642AC2CF` · jhash `0x161780C1` · **Cliente**

```lua
local retval = StartNetworkedParticleFxNonLoopedOnPedBone(effectName, ped, offsetX, offsetY, offsetZ, rotX, rotY, rotZ, boneIndex, scale, axisX, axisY, axisZ)
```
```c
BOOL START_NETWORKED_PARTICLE_FX_NON_LOOPED_ON_PED_BONE(char* effectName, Ped ped, float offsetX, float offsetY, float offsetZ, float rotX, float rotY, float rotZ, int boneIndex, float scale, BOOL axisX, BOOL axisY, BOOL axisZ);
```

**Parámetros**

- `effectName` (`char*`)
- `ped` (`Ped`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `boneIndex` (`int`)
- `scale` (`float`)
- `axisX` (`BOOL`)
- `axisY` (`BOOL`)
- `axisZ` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_START_PARTICLE_FX_NON_LOOPED_ON_PED_BONE_2` (`StartParticleFxNonLoopedOnPedBone_2`)

---
### StartParticleFxLoopedAtCoord

`START_PARTICLE_FX_LOOPED_AT_COORD` · hash `0xE184F4F0DC5910E7` · jhash `0xD348E3E6` · **Cliente**

```lua
local retval = StartParticleFxLoopedAtCoord(effectName, x, y, z, xRot, yRot, zRot, scale, xAxis, yAxis, zAxis, p11)
```
```c
int START_PARTICLE_FX_LOOPED_AT_COORD(char* effectName, float x, float y, float z, float xRot, float yRot, float zRot, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis, BOOL p11);
```

**Parámetros**

- `effectName` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)
- `p11` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
GRAPHICS::START_PARTICLE_FX_LOOPED_AT_COORD("scr_fbi_falling_debris", 93.7743f, -749.4572f, 70.86904f, 0f, 0f, 0f, 0x3F800000, 0, 0, 0, 0)  
p11 seems to be always 0  
```

---
### StartParticleFxLoopedOnEntity

`START_PARTICLE_FX_LOOPED_ON_ENTITY` · hash `0x1AE42C1660FD6517` · jhash `0x0D06FF62` · **Cliente**

```lua
local retval = StartParticleFxLoopedOnEntity(effectName, entity, xOffset, yOffset, zOffset, xRot, yRot, zRot, scale, xAxis, yAxis, zAxis)
```
```c
int START_PARTICLE_FX_LOOPED_ON_ENTITY(char* effectName, Entity entity, float xOffset, float yOffset, float zOffset, float xRot, float yRot, float zRot, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis);
```

**Parámetros**

- `effectName` (`char*`)
- `entity` (`Entity`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)

**Devuelve:** `int`

---
### StartParticleFxLoopedOnEntityBone

`START_PARTICLE_FX_LOOPED_ON_ENTITY_BONE` · hash `0xC6EB449E33977F0B` · jhash `0x23BF0F9B` · **Cliente**

```lua
local retval = StartParticleFxLoopedOnEntityBone(effectName, entity, xOffset, yOffset, zOffset, xRot, yRot, zRot, boneIndex, scale, xAxis, yAxis, zAxis)
```
```c
int START_PARTICLE_FX_LOOPED_ON_ENTITY_BONE(char* effectName, Entity entity, float xOffset, float yOffset, float zOffset, float xRot, float yRot, float zRot, int boneIndex, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis);
```

**Parámetros**

- `effectName` (`char*`)
- `entity` (`Entity`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `boneIndex` (`int`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)

**Devuelve:** `int`

---
### StartParticleFxLoopedOnPedBone

`START_PARTICLE_FX_LOOPED_ON_PED_BONE` · hash `0xF28DA9F38CD1787C` · jhash `0xF8FC196F` · **Cliente**

```lua
local retval = StartParticleFxLoopedOnPedBone(effectName, ped, xOffset, yOffset, zOffset, xRot, yRot, zRot, boneIndex, scale, xAxis, yAxis, zAxis)
```
```c
int START_PARTICLE_FX_LOOPED_ON_PED_BONE(char* effectName, Ped ped, float xOffset, float yOffset, float zOffset, float xRot, float yRot, float zRot, int boneIndex, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis);
```

**Parámetros**

- `effectName` (`char*`)
- `ped` (`Ped`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `boneIndex` (`int`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)

**Devuelve:** `int`

---
### StartParticleFxNonLoopedAtCoord

`START_PARTICLE_FX_NON_LOOPED_AT_COORD` · hash `0x25129531F77B9ED3` · jhash `0xDD79D679` · **Cliente**

```lua
local retval = StartParticleFxNonLoopedAtCoord(effectName, xPos, yPos, zPos, xRot, yRot, zRot, scale, xAxis, yAxis, zAxis)
```
```c
int START_PARTICLE_FX_NON_LOOPED_AT_COORD(char* effectName, float xPos, float yPos, float zPos, float xRot, float yRot, float zRot, float scale, BOOL xAxis, BOOL yAxis, BOOL zAxis);
```

**Parámetros**

- `effectName` (`char*`)
- `xPos` (`float`)
- `yPos` (`float`)
- `zPos` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `scale` (`float`)
- `xAxis` (`BOOL`)
- `yAxis` (`BOOL`)
- `zAxis` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
GRAPHICS::START_PARTICLE_FX_NON_LOOPED_AT_COORD("scr_paleto_roof_impact", -140.8576f, 6420.789f, 41.1391f, 0f, 0f, 267.3957f, 0x3F800000, 0, 0, 0);  
Axis - Invert Axis Flags  
list: pastebin.com/N9unUFWY  
-------------------------------------------------------------------  
C#  
Function.Call<int>(Hash.START_PARTICLE_FX_NON_LOOPED_AT_COORD, = you are calling this function.  
char *effectname = This is an in-game effect name, for e.g. "scr_fbi4_trucks_crash" is used to give the effects when truck crashes etc  
float x, y, z pos = this one is Simple, you just have to declare, where do you want this effect to take place at, so declare the ordinates  
float xrot, yrot, zrot = Again simple? just mention the value in case if you want the effect to rotate.  
float scale = is declare the scale of the effect, this may vary as per the effects for e.g 1.0f  
bool xaxis, yaxis, zaxis = To bool the axis values.  
example:  
Function.Call<int>(Hash.START_PARTICLE_FX_NON_LOOPED_AT_COORD, "scr_fbi4_trucks_crash", GTA.Game.Player.Character.Position.X, GTA.Game.Player.Character.Position.Y, GTA.Game.Player.Character.Position.Z + 4f, 0, 0, 0, 5.5f, 0, 0, 0);  
```

---
### StartParticleFxNonLoopedOnEntity

`START_PARTICLE_FX_NON_LOOPED_ON_ENTITY` · hash `0x0D53A3B8DA0809D2` · jhash `0x9604DAD4` · **Cliente**

```lua
local retval = StartParticleFxNonLoopedOnEntity(effectName, entity, offsetX, offsetY, offsetZ, rotX, rotY, rotZ, scale, axisX, axisY, axisZ)
```
```c
BOOL START_PARTICLE_FX_NON_LOOPED_ON_ENTITY(char* effectName, Entity entity, float offsetX, float offsetY, float offsetZ, float rotX, float rotY, float rotZ, float scale, BOOL axisX, BOOL axisY, BOOL axisZ);
```

**Parámetros**

- `effectName` (`char*`)
- `entity` (`Entity`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `scale` (`float`)
- `axisX` (`BOOL`)
- `axisY` (`BOOL`)
- `axisZ` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Starts a particle effect on an entity for example your player.  
List: pastebin.com/N9unUFWY  
Example:  
C#:  
Function.Call(Hash.REQUEST_NAMED_PTFX_ASSET, "scr_rcbarry2");                     Function.Call(Hash._SET_PTFX_ASSET_NEXT_CALL, "scr_rcbarry2");                             Function.Call(Hash.START_PARTICLE_FX_NON_LOOPED_ON_ENTITY, "scr_clown_appears", Game.Player.Character, 0.0, 0.0, -0.5, 0.0, 0.0, 0.0, 1.0, false, false, false);  
Internally this calls the same function as GRAPHICS::START_PARTICLE_FX_NON_LOOPED_ON_PED_BONE  
however it uses -1 for the specified bone index, so it should be possible to start a non looped fx on an entity bone using that native  
```

---
### StartParticleFxNonLoopedOnPedBone

`START_PARTICLE_FX_NON_LOOPED_ON_PED_BONE` · hash `0x0E7E72961BA18619` · jhash `0x53DAEF4E` · **Cliente**

```lua
local retval = StartParticleFxNonLoopedOnPedBone(effectName, ped, offsetX, offsetY, offsetZ, rotX, rotY, rotZ, boneIndex, scale, axisX, axisY, axisZ)
```
```c
BOOL START_PARTICLE_FX_NON_LOOPED_ON_PED_BONE(char* effectName, Ped ped, float offsetX, float offsetY, float offsetZ, float rotX, float rotY, float rotZ, int boneIndex, float scale, BOOL axisX, BOOL axisY, BOOL axisZ);
```

**Parámetros**

- `effectName` (`char*`)
- `ped` (`Ped`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `boneIndex` (`int`)
- `scale` (`float`)
- `axisX` (`BOOL`)
- `axisY` (`BOOL`)
- `axisZ` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
GRAPHICS::START_PARTICLE_FX_NON_LOOPED_ON_PED_BONE("scr_sh_bong_smoke", PLAYER::PLAYER_PED_ID(), -0.025f, 0.13f, 0f, 0f, 0f, 0f, 31086, 0x3F800000, 0, 0, 0);  
Axis - Invert Axis Flags  
list: pastebin.com/N9unUFWY  
```

---
### StartPetrolTrailDecals

`START_PETROL_TRAIL_DECALS` · hash `0x99AC7F0D8B9C893D` · jhash `0xE3938B0B` · **Cliente**

```lua
StartPetrolTrailDecals(p0)
```
```c
void START_PETROL_TRAIL_DECALS(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x99AC7F0D8B9C893D` (`N_0x99ac7f0d8b9c893d`)

---
### StopBinkMovie

`_STOP_BINK_MOVIE` · hash `0x63606A61DE68898A` · **Cliente**

```lua
StopBinkMovie(binkMovie)
```
```c
void _STOP_BINK_MOVIE(int binkMovie);
```

**Parámetros**

- `binkMovie` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### StopParticleFxLooped

`STOP_PARTICLE_FX_LOOPED` · hash `0x8F75998877616996` · jhash `0xD245455B` · **Cliente**

```lua
StopParticleFxLooped(ptfxHandle, p1)
```
```c
void STOP_PARTICLE_FX_LOOPED(int ptfxHandle, BOOL p1);
```

**Parámetros**

- `ptfxHandle` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
p1 is always 0 in the native scripts  
```

---
### TerraingridActivate

`TERRAINGRID_ACTIVATE` · hash `0xA356990E161C9E65` · jhash `0xA1CB6C94` · **Cliente**

```lua
TerraingridActivate(toggle)
```
```c
void TERRAINGRID_ACTIVATE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Enables or disables the golf putting grid display.

**Devuelve:** `void`

**Descripción oficial:**

This native enables/disables the gold putting grid display (https://i.imgur.com/slYthff.png).
This requires these two natives to be called as well to configure the grid: [`TERRAINGRID_SET_PARAMS`](#terraingridsetparams) and [`TERRAINGRID_SET_COLOURS`](#terraingridsetcolours).

**Nombres antiguos (alias):** `0xA356990E161C9E65` (`N_0xa356990e161c9e65`)

---
### TerraingridSetColours

`TERRAINGRID_SET_COLOURS` · hash `0x5CE62918F8D703C7` · jhash `0xDF552973` · **Cliente**

```lua
TerraingridSetColours(lowR, lowG, lowB, lowAlpha, R, G, B, Alpha, highR, highG, highB, highAlpha)
```
```c
void TERRAINGRID_SET_COLOURS(int lowR, int lowG, int lowB, int lowAlpha, int R, int G, int B, int Alpha, int highR, int highG, int highB, int highAlpha);
```

**Parámetros**

- `lowR` (`int`): red value for the lower level
- `lowG` (`int`): green value for the lower level
- `lowB` (`int`): blue value for the lower level
- `lowAlpha` (`int`): alpha value for the lower level
- `R` (`int`): red value for the normal level
- `G` (`int`): green value for the normal level
- `B` (`int`): blue value for the normal level
- `Alpha` (`int`): alpha value for the normal level
- `highR` (`int`): red value for the upper level
- `highG` (`int`): green value for the upper level
- `highB` (`int`): blue value for the upper level
- `highAlpha` (`int`): alpha value for the upper level

**Devuelve:** `void`

**Descripción oficial:**

This native is used along with these two natives: [`TERRAINGRID_ACTIVATE`](#terraingridactivate) and [`TERRAINGRID_SET_PARAMS`](#terraingridsetparams).
This native sets the colors for the golf putting grid. the 'min...' values are for the lower areas that the grid covers, the 'max...' values are for the higher areas that the grid covers, all remaining values are for the 'normal' ground height.
All those natives combined they will output something like this:
![](https://i.imgur.com/slYthff.png)

Old description:
Only called in golf and golf_mp\
parameters used are\
GRAPHICS::\_0x5CE62918F8D703C7(255, 0, 0, 64, 255, 255, 255, 5, 255, 255, 0, 64);

**Nombres antiguos (alias):** `0x5CE62918F8D703C7` (`N_0x5ce62918f8d703c7`)

**Ejemplo (cs):**

```cs
N_0xa356990e161c9e65(true); // toggle on/off

// this native configures the location, size, rotation, normal height, and the difference ratio between min, normal and max.
N_0x1c4fc5752bcd8e48(-1114.121f, 220.789f, 63.78f, -1f, 0.85f, 0f, 15f, 15f, -1f, 20f, 40f, 63.78f, 0.2f);

// This native defines the colors (and alpha/opacity levels) for min, normal and max heights.
// (in this case: red for lower, white for normal, yellow for higher)
N_0x5ce62918f8d703c7(255, 0, 0, 64, 255, 255, 255, 5, 255, 255, 0, 64);
```

---
### TerraingridSetParams

`TERRAINGRID_SET_PARAMS` · hash `0x1C4FC5752BCD8E48` · jhash `0x3B637AA7` · **Cliente**

```lua
TerraingridSetParams(x, y, z, p3, rotation, p5, width, height, p8, scale, glowIntensity, normalHeight, heightDiff)
```
```c
void TERRAINGRID_SET_PARAMS(float x, float y, float z, float p3, float rotation, float p5, float width, float height, float p8, float scale, float glowIntensity, float normalHeight, float heightDiff);
```

**Parámetros**

- `x` (`float`): Grid center x coord.
- `y` (`float`): Grid center y coord.
- `z` (`float`): Grid center z coord.
- `p3` (`float`): Not sure, but seems to be the amount of lines top/bottom there are in the grid. -1.0 works best.
- `rotation` (`float`): Grid rotation (keep between 0.0 and 1.0).
- `p5` (`float`): Offset top/bottom (? not sure about this one, seems weird).
- `width` (`float`): Grid width (usually 15.0).
- `height` (`float`): Grid height (usually 15.0).
- `p8` (`float`): Not sure, but seems to be the amount of lines left/right there are in the grid. -1.0 works best.
- `scale` (`float`): Zoom / scale (higher values = smaller (more) squares) (lower values = bigger (less) squares).
- `glowIntensity` (`float`): glow intensity / opacity (40.0 is fine for daylight, 15.0 is fine for night time).
- `normalHeight` (`float`): The z coord for 'normal' height (white grid lines level).
- `heightDiff` (`float`): This is the height difference/margin used for line color changes. 0.2 works fine (normalHeight + 0.2 = yellow, normalHeight - 0.2 = red).

**Devuelve:** `void`

**Descripción oficial:**

This native is used along with these two natives: [`TERRAINGRID_ACTIVATE`](#terraingridactivate) and [`TERRAINGRID_SET_COLOURS`](#terraingridsetcolours).

This native configures the location, size, rotation, normal height, and the difference ratio between min, normal and max.

All those natives combined they will output something like this:
![](https://i.imgur.com/slYthff.png)

**Nombres antiguos (alias):** `0x1C4FC5752BCD8E48` (`N_0x1c4fc5752bcd8e48`)

**Ejemplo (cs):**

```cs
N_0xa356990e161c9e65(true); // toggle on/off

// this native configures the location, size, rotation, normal height, and the difference ratio between min, normal and max.
N_0x1c4fc5752bcd8e48(-1114.121f, 220.789f, 63.78f, -1f, 0.85f, 0f, 15f, 15f, -1f, 20f, 40f, 63.78f, 0.2f);

// This native defines the colors (and alpha/opacity levels) for min, normal and max heights.
// (in this case: red for lower, white for normal, yellow for higher)
N_0x5ce62918f8d703c7(255, 0, 0, 64, 255, 255, 255, 5, 255, 255, 0, 64);
```

---
### TogglePausedRenderphases

`TOGGLE_PAUSED_RENDERPHASES` · hash `0xDFC252D8A3E15AB7` · jhash `0x30ADE541` · **Cliente**

```lua
TogglePausedRenderphases(toggle)
```
```c
void TOGGLE_PAUSED_RENDERPHASES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Setting it to `false` will exclude render updates as mentioned in the description, until it's set back to `true`.

**Devuelve:** `void`

**Descripción oficial:**

Switches the rendering display to exclude everything except PostFX, resulting in a frozen screen before the UI pass.

**Nombres antiguos (alias):** `_ENABLE_GAMEPLAY_CAM` (`EnableGameplayCam`), `_SET_FROZEN_RENDERING_DISABLED` (`SetFrozenRenderingDisabled`)

---
### TriggerScreenblurFadeIn

`TRIGGER_SCREENBLUR_FADE_IN` · hash `0xA328A24AAA6B7FDC` · jhash `0x5604B890` · **Cliente**

```lua
local retval = TriggerScreenblurFadeIn(transitionTime)
```
```c
BOOL TRIGGER_SCREENBLUR_FADE_IN(float transitionTime);
```

**Parámetros**

- `transitionTime` (`float`): Time in milliseconds to transition into a fully blurred screen

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_TRANSITION_TO_BLURRED` (`TransitionToBlurred`)

---
### TriggerScreenblurFadeOut

`TRIGGER_SCREENBLUR_FADE_OUT` · hash `0xEFACC8AEF94430D5` · jhash `0x46617502` · **Cliente**

```lua
local retval = TriggerScreenblurFadeOut(transitionTime)
```
```c
BOOL TRIGGER_SCREENBLUR_FADE_OUT(float transitionTime);
```

**Parámetros**

- `transitionTime` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_TRANSITION_FROM_BLURRED` (`TransitionFromBlurred`)

---
### Ui3dsceneIsAvailable

`UI3DSCENE_IS_AVAILABLE` · hash `0xD3A10FC7FD8D98CD` · jhash `0xE40A0F1A` · **Cliente**

```lua
local retval = Ui3dsceneIsAvailable()
```
```c
BOOL UI3DSCENE_IS_AVAILABLE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD3A10FC7FD8D98CD` (`N_0xd3a10fc7fd8d98cd`)

---
### Ui3dscenePushPreset

`UI3DSCENE_PUSH_PRESET` · hash `0xF1CEA8A4198D8E9A` · jhash `0x2E7D9B98` · **Cliente**

```lua
local retval = Ui3dscenePushPreset(presetName)
```
```c
BOOL UI3DSCENE_PUSH_PRESET(char* presetName);
```

**Parámetros**

- `presetName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
All presets can be found in common\data\ui\uiscenes.meta
```

**Nombres antiguos (alias):** `0xF1CEA8A4198D8E9A` (`N_0xf1cea8a4198d8e9a`)

---
### UnpatchDecalDiffuseMap

`UNPATCH_DECAL_DIFFUSE_MAP` · hash `0xB7ED70C49521A61D` · jhash `0x7B786555` · **Cliente**

```lua
UnpatchDecalDiffuseMap(decalType)
```
```c
void UNPATCH_DECAL_DIFFUSE_MAP(int decalType);
```

**Parámetros**

- `decalType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
GRAPHICS::UNPATCH_DECAL_DIFFUSE_MAP(9123);  
GRAPHICS::SET_STREAMED_TEXTURE_DICT_AS_NO_LONGER_NEEDED("MPMissMarkers256");  
```

**Nombres antiguos (alias):** `0xB7ED70C49521A61D` (`N_0xb7ed70c49521a61d`), `_UNDO_DECAL_TEXTURE_OVERRIDE` (`UndoDecalTextureOverride`)

---
### UpdateLightsOnEntity

`UPDATE_LIGHTS_ON_ENTITY` · hash `0xDEADC0DEDEADC0DE` · jhash `0xC12AC47A` · **Cliente**

```lua
UpdateLightsOnEntity(entity)
```
```c
void UPDATE_LIGHTS_ON_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDEADC0DEDEADC0DE` (`N_0xdeadc0dedeadc0de`), `_ENTITY_DESCRIPTION_TEXT` (`EntityDescriptionText`)

---
### UseParticleFxAsset

`USE_PARTICLE_FX_ASSET` · hash `0x6C38AF3693A69A91` · jhash `0x9C720B61` · **Cliente**

```lua
UseParticleFxAsset(name)
```
```c
void USE_PARTICLE_FX_ASSET(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
From the b678d decompiled scripts:
 GRAPHICS::_SET_PTFX_ASSET_NEXT_CALL("FM_Mission_Controler");
 GRAPHICS::_SET_PTFX_ASSET_NEXT_CALL("scr_apartment_mp");
 GRAPHICS::_SET_PTFX_ASSET_NEXT_CALL("scr_indep_fireworks");
 GRAPHICS::_SET_PTFX_ASSET_NEXT_CALL("scr_mp_cig_plane");
 GRAPHICS::_SET_PTFX_ASSET_NEXT_CALL("scr_mp_creator");
 GRAPHICS::_SET_PTFX_ASSET_NEXT_CALL("scr_ornate_heist");
 GRAPHICS::_SET_PTFX_ASSET_NEXT_CALL("scr_prison_break_heist_station");
```

**Nombres antiguos (alias):** `_SET_PTFX_ASSET_NEXT_CALL` (`SetPtfxAssetNextCall`), `_USE_PARTICLE_FX_ASSET_NEXT_CALL` (`UseParticleFxAssetNextCall`)

---
### WashDecalsFromVehicle

`WASH_DECALS_FROM_VEHICLE` · hash `0x5B712761429DBC14` · jhash `0x2929F11A` · **Cliente**

```lua
WashDecalsFromVehicle(vehicle, p1)
```
```c
void WASH_DECALS_FROM_VEHICLE(Vehicle vehicle, float p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`float`)

**Devuelve:** `void`

---
### WashDecalsInRange

`WASH_DECALS_IN_RANGE` · hash `0x9C30613D50A6ADEF` · jhash `0xDEECBC57` · **Cliente**

```lua
WashDecalsInRange(p0, p1, p2, p3, p4)
```
```c
void WASH_DECALS_IN_RANGE(Any p0, Any p1, Any p2, Any p3, Any p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)

**Devuelve:** `void`

---
