# Natives de GTA V — CAM

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `CAM`: **245** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivateCamWithInterpAndFovCurve`](#activatecamwithinterpandfovcurve) · [`AddCamSplineNode`](#addcamsplinenode) · [`AddCamSplineNodeUsingCamera`](#addcamsplinenodeusingcamera) · [`AddCamSplineNodeUsingCameraFrame`](#addcamsplinenodeusingcameraframe) · [`AddCamSplineNodeUsingGameplayFrame`](#addcamsplinenodeusinggameplayframe) · [`AnimateGameplayCamZoom`](#animategameplaycamzoom) · [`AnimatedShakeCam`](#animatedshakecam) · [`AnimatedShakeScriptGlobal`](#animatedshakescriptglobal) · [`AttachCamToEntity`](#attachcamtoentity) · [`AttachCamToPedBone`](#attachcamtopedbone) · [`AttachCamToVehicleBone`](#attachcamtovehiclebone) · [`ClampGameplayCamPitch`](#clampgameplaycampitch) · [`ClampGameplayCamYaw`](#clampgameplaycamyaw) · [`CreateCam`](#createcam) · [`CreateCamWithParams`](#createcamwithparams) · [`CreateCamera`](#createcamera) · [`CreateCameraWithParams`](#createcamerawithparams) · [`CreateCinematicShot`](#createcinematicshot) · [`CustomMenuCoordinates`](#custommenucoordinates) · [`DestroyAllCams`](#destroyallcams) · [`DestroyCam`](#destroycam) · [`DetachCam`](#detachcam) · [`DisableAimCamThisUpdate`](#disableaimcamthisupdate) · [`DisableCamCollisionForEntity`](#disablecamcollisionforentity) · [`DisableCamCollisionForObject`](#disablecamcollisionforobject) · [`DisableCinematicBonnetCameraThisUpdate`](#disablecinematicbonnetcamerathisupdate) · [`DisableOnFootFirstPersonViewThisUpdate`](#disableonfootfirstpersonviewthisupdate) · [`DoScreenFadeIn`](#doscreenfadein) · [`DoScreenFadeOut`](#doscreenfadeout) · [`DoesCamExist`](#doescamexist) · [`EnableCrosshairThisFrame`](#enablecrosshairthisframe) · [`ForceCinematicRenderingThisUpdate`](#forcecinematicrenderingthisupdate) · [`GetCamActiveViewModeContext`](#getcamactiveviewmodecontext) · [`GetCamAnimCurrentPhase`](#getcamanimcurrentphase) · [`GetCamCoord`](#getcamcoord) · [`GetCamDofStrength`](#getcamdofstrength) · [`GetCamFarClip`](#getcamfarclip) · [`GetCamFarDof`](#getcamfardof) · [`GetCamFov`](#getcamfov) · [`GetCamNearClip`](#getcamnearclip) · [`GetCamNearDof`](#getcamneardof) · [`GetCamRot`](#getcamrot) · [`GetCamSplineNodeIndex`](#getcamsplinenodeindex) · [`GetCamSplineNodePhase`](#getcamsplinenodephase) · [`GetCamSplinePhase`](#getcamsplinephase) · [`GetCamViewModeForContext`](#getcamviewmodeforcontext) · [`GetDebugCamera`](#getdebugcamera) · [`GetFinalRenderedCamCoord`](#getfinalrenderedcamcoord) · [`GetFinalRenderedCamFarClip`](#getfinalrenderedcamfarclip) · [`GetFinalRenderedCamFarDof`](#getfinalrenderedcamfardof) · [`GetFinalRenderedCamFov`](#getfinalrenderedcamfov) · [`GetFinalRenderedCamMotionBlurStrength`](#getfinalrenderedcammotionblurstrength) · [`GetFinalRenderedCamNearClip`](#getfinalrenderedcamnearclip) · [`GetFinalRenderedCamNearDof`](#getfinalrenderedcamneardof) · [`GetFinalRenderedCamRot`](#getfinalrenderedcamrot) · [`GetFinalRenderedInWhenFriendlyFov`](#getfinalrenderedinwhenfriendlyfov) · [`GetFinalRenderedInWhenFriendlyRot`](#getfinalrenderedinwhenfriendlyrot) · [`GetFirstPersonAimCamZoomFactor`](#getfirstpersonaimcamzoomfactor) · [`GetFocusPedOnScreen`](#getfocuspedonscreen) · [`GetFollowPedCamViewMode`](#getfollowpedcamviewmode) · [`GetFollowPedCamZoomLevel`](#getfollowpedcamzoomlevel) · [`GetFollowVehicleCamViewMode`](#getfollowvehiclecamviewmode) · [`GetFollowVehicleCamZoomLevel`](#getfollowvehiclecamzoomlevel) · [`GetGameplayCamCoord`](#getgameplaycamcoord) · [`GetGameplayCamFov`](#getgameplaycamfov) · [`GetGameplayCamRelativeHeading`](#getgameplaycamrelativeheading) · [`GetGameplayCamRelativePitch`](#getgameplaycamrelativepitch) · [`GetGameplayCamRot`](#getgameplaycamrot) · [`GetRenderingCam`](#getrenderingcam) · [`HardAttachCamToEntity`](#hardattachcamtoentity) · [`HardAttachCamToPedBone`](#hardattachcamtopedbone) · [`IgnoreMenuPreferenceForBonnetCameraThisUpdate`](#ignoremenupreferenceforbonnetcamerathisupdate) · [`InterpolateCamWithParams`](#interpolatecamwithparams) · [`InvalidateIdleCam`](#invalidateidlecam) · [`InvalidateVehicleIdleCam`](#invalidatevehicleidlecam) · [`IsAimCamActive`](#isaimcamactive) · [`IsAimCamThirdPersonActive`](#isaimcamthirdpersonactive) · [`IsAllowedIndependentCameraModes`](#isallowedindependentcameramodes) · [`IsBonnetCinematicCamRendering`](#isbonnetcinematiccamrendering) · [`IsCamActive`](#iscamactive) · [`IsCamInterpolating`](#iscaminterpolating) · [`IsCamPlayingAnim`](#iscamplayinganim) · [`IsCamRendering`](#iscamrendering) · [`IsCamShaking`](#iscamshaking) · [`IsCamSplinePaused`](#iscamsplinepaused) · [`IsCinematicCamInputActive`](#iscinematiccaminputactive) · [`IsCinematicCamRendering`](#iscinematiccamrendering) · [`IsCinematicCamShaking`](#iscinematiccamshaking) · [`IsCinematicIdleCamRendering`](#iscinematicidlecamrendering) · [`IsCinematicShotActive`](#iscinematicshotactive) · [`IsFirstPersonAimCamActive`](#isfirstpersonaimcamactive) · [`IsFollowPedCamActive`](#isfollowpedcamactive) · [`IsFollowVehicleCamActive`](#isfollowvehiclecamactive) · [`IsGameplayCamLookingBehind`](#isgameplaycamlookingbehind) · [`IsGameplayCamRendering`](#isgameplaycamrendering) · [`IsGameplayCamShaking`](#isgameplaycamshaking) · [`IsGameplayHintActive`](#isgameplayhintactive) · [`IsInVehicleCamDisabled`](#isinvehiclecamdisabled) · [`IsScreenFadedIn`](#isscreenfadedin) · [`IsScreenFadedOut`](#isscreenfadedout) · [`IsScreenFadingIn`](#isscreenfadingin) · [`IsScreenFadingOut`](#isscreenfadingout) · [`IsScriptGlobalShaking`](#isscriptglobalshaking) · [`IsSphereVisible`](#isspherevisible) · [`N_0x0225778816fdc28c`](#n_0x0225778816fdc28c) · [`N_0x0aa27680a0bd43fa`](#n_0x0aa27680a0bd43fa) · [`N_0x12ded8ca53d47ea5`](#n_0x12ded8ca53d47ea5) · [`N_0x17fca7199a530203`](#n_0x17fca7199a530203) · [`N_0x1f2300cb7fa7b7f6`](#n_0x1f2300cb7fa7b7f6) · [`N_0x247acbc4abbc9d1c`](#n_0x247acbc4abbc9d1c) · [`N_0x271017b9ba825366`](#n_0x271017b9ba825366) · [`N_0x28b022a17b068a3a`](#n_0x28b022a17b068a3a) · [`N_0x2f7f2b26dd3f18ee`](#n_0x2f7f2b26dd3f18ee) · [`N_0x3044240d2e0fa842`](#n_0x3044240d2e0fa842) · [`N_0x324c5aa411da7737`](#n_0x324c5aa411da7737) · [`N_0x380b4968d1e09e55`](#n_0x380b4968d1e09e55) · [`N_0x4008edf7d6e48175`](#n_0x4008edf7d6e48175) · [`N_0x469f2ecdec046337`](#n_0x469f2ecdec046337) · [`N_0x4879e4fe39074cdf`](#n_0x4879e4fe39074cdf) · [`N_0x59424bd75174c9b1`](#n_0x59424bd75174c9b1) · [`N_0x5a43c76f7fc7ba5f`](#n_0x5a43c76f7fc7ba5f) · [`N_0x5c41e6babc9e2112`](#n_0x5c41e6babc9e2112) · [`N_0x5c48a1d6e3b33179`](#n_0x5c48a1d6e3b33179) · [`N_0x5d96cfb59da076a0`](#n_0x5d96cfb59da076a0) · [`N_0x62374889a4d59f72`](#n_0x62374889a4d59f72) · [`N_0x62ecfcfdee7885d6`](#n_0x62ecfcfdee7885d6) · [`N_0x705a276ebff3133d`](#n_0x705a276ebff3133d) · [`N_0x7295c203dd659dfe`](#n_0x7295c203dd659dfe) · [`N_0x91ef6ee6419e5b97`](#n_0x91ef6ee6419e5b97) · [`N_0x9dfe13ecdc1ec196`](#n_0x9dfe13ecdc1ec196) · [`N_0x9f97da93681f87ea`](#n_0x9f97da93681f87ea) · [`N_0xa2767257a320fc82`](#n_0xa2767257a320fc82) · [`N_0xa7092afe81944852`](#n_0xa7092afe81944852) · [`N_0xaabd62873ffb1a33`](#n_0xaabd62873ffb1a33) · [`N_0xb1381b97f70c7b30`](#n_0xb1381b97f70c7b30) · [`N_0xbf72910d0f26f025`](#n_0xbf72910d0f26f025) · [`N_0xc8391c309684595a`](#n_0xc8391c309684595a) · [`N_0xc8b5c4a79cc18b94`](#n_0xc8b5c4a79cc18b94) · [`N_0xccd078c2665d2973`](#n_0xccd078c2665d2973) · [`N_0xced08cbe8ebb97c7`](#n_0xced08cbe8ebb97c7) · [`N_0xdb90c6cca48940f1`](#n_0xdb90c6cca48940f1) · [`N_0xdd79df9f4d26e1c9`](#n_0xdd79df9f4d26e1c9) · [`N_0xe111a7c0d200cbc5`](#n_0xe111a7c0d200cbc5) · [`N_0xf55e4046f6f831dc`](#n_0xf55e4046f6f831dc) · [`N_0xfd3151cd37ea2245`](#n_0xfd3151cd37ea2245) · [`OverrideCamSplineMotionBlur`](#overridecamsplinemotionblur) · [`OverrideCamSplineVelocity`](#overridecamsplinevelocity) · [`PlayCamAnim`](#playcamanim) · [`PlaySynchronizedCamAnim`](#playsynchronizedcamanim) · [`PointCamAtCoord`](#pointcamatcoord) · [`PointCamAtEntity`](#pointcamatentity) · [`PointCamAtPedBone`](#pointcamatpedbone) · [`RenderScriptCams`](#renderscriptcams) · [`ReplayFreeCamGetMaxRange`](#replayfreecamgetmaxrange) · [`SetCamActive`](#setcamactive) · [`SetCamActiveWithInterp`](#setcamactivewithinterp) · [`SetCamAffectsAiming`](#setcamaffectsaiming) · [`SetCamAnimCurrentPhase`](#setcamanimcurrentphase) · [`SetCamControlsMiniMapHeading`](#setcamcontrolsminimapheading) · [`SetCamCoord`](#setcamcoord) · [`SetCamDebugName`](#setcamdebugname) · [`SetCamDofFnumberOfLens`](#setcamdoffnumberoflens) · [`SetCamDofFocalLengthMultiplier`](#setcamdoffocallengthmultiplier) · [`SetCamDofFocusDistanceBias`](#setcamdoffocusdistancebias) · [`SetCamDofMaxNearInFocusDistance`](#setcamdofmaxnearinfocusdistance) · [`SetCamDofMaxNearInFocusDistanceBlendLevel`](#setcamdofmaxnearinfocusdistanceblendlevel) · [`SetCamDofPlanes`](#setcamdofplanes) · [`SetCamDofStrength`](#setcamdofstrength) · [`SetCamEffect`](#setcameffect) · [`SetCamFarClip`](#setcamfarclip) · [`SetCamFarDof`](#setcamfardof) · [`SetCamFov`](#setcamfov) · [`SetCamInheritRollVehicle`](#setcaminheritrollvehicle) · [`SetCamMotionBlurStrength`](#setcammotionblurstrength) · [`SetCamNearClip`](#setcamnearclip) · [`SetCamNearDof`](#setcamneardof) · [`SetCamParams`](#setcamparams) · [`SetCamRot`](#setcamrot) · [`SetCamShakeAmplitude`](#setcamshakeamplitude) · [`SetCamSplineDuration`](#setcamsplineduration) · [`SetCamSplineNodeEase`](#setcamsplinenodeease) · [`SetCamSplineNodeExtraFlags`](#setcamsplinenodeextraflags) · [`SetCamSplineNodeVelocityScale`](#setcamsplinenodevelocityscale) · [`SetCamSplinePhase`](#setcamsplinephase) · [`SetCamSplineSmoothingStyle`](#setcamsplinesmoothingstyle) · [`SetCamUseShallowDofMode`](#setcamuseshallowdofmode) · [`SetCamViewModeForContext`](#setcamviewmodeforcontext) · [`SetCinematicButtonActive`](#setcinematicbuttonactive) · [`SetCinematicCamShakeAmplitude`](#setcinematiccamshakeamplitude) · [`SetCinematicModeActive`](#setcinematicmodeactive) · [`SetCinematicNewsChannelActiveThisUpdate`](#setcinematicnewschannelactivethisupdate) · [`SetFirstPersonAimCamNearClipThisUpdate`](#setfirstpersonaimcamnearclipthisupdate) · [`SetFirstPersonAimCamZoomFactor`](#setfirstpersonaimcamzoomfactor) · [`SetFirstPersonCamPitchRange`](#setfirstpersoncampitchrange) · [`SetFlyCamCoordAndConstrain`](#setflycamcoordandconstrain) · [`SetFlyCamHorizontalResponse`](#setflycamhorizontalresponse) · [`SetFlyCamMaxHeight`](#setflycammaxheight) · [`SetFlyCamVerticalSpeedMultiplier`](#setflycamverticalspeedmultiplier) · [`SetFollowPedCamThisUpdate`](#setfollowpedcamthisupdate) · [`SetFollowPedCamViewMode`](#setfollowpedcamviewmode) · [`SetFollowTurretSeatCam`](#setfollowturretseatcam) · [`SetFollowVehicleCamViewMode`](#setfollowvehiclecamviewmode) · [`SetFollowVehicleCamZoomLevel`](#setfollowvehiclecamzoomlevel) · [`SetGameplayCamFollowPedThisUpdate`](#setgameplaycamfollowpedthisupdate) · [`SetGameplayCamHash`](#setgameplaycamhash) · [`SetGameplayCamRawPitch`](#setgameplaycamrawpitch) · [`SetGameplayCamRawYaw`](#setgameplaycamrawyaw) · [`SetGameplayCamRelativeHeading`](#setgameplaycamrelativeheading) · [`SetGameplayCamRelativePitch`](#setgameplaycamrelativepitch) · [`SetGameplayCamRelativeRotation`](#setgameplaycamrelativerotation) · [`SetGameplayCamShakeAmplitude`](#setgameplaycamshakeamplitude) · [`SetGameplayCamVehicleCamera`](#setgameplaycamvehiclecamera) · [`SetGameplayCamVehicleCameraName`](#setgameplaycamvehiclecameraname) · [`SetGameplayCoordHint`](#setgameplaycoordhint) · [`SetGameplayEntityHint`](#setgameplayentityhint) · [`SetGameplayHintAnimCloseup`](#setgameplayhintanimcloseup) · [`SetGameplayHintAnimOffsetx`](#setgameplayhintanimoffsetx) · [`SetGameplayHintAnimOffsety`](#setgameplayhintanimoffsety) · [`SetGameplayHintBaseOrbitPitchOffset`](#setgameplayhintbaseorbitpitchoffset) · [`SetGameplayHintFollowDistanceScalar`](#setgameplayhintfollowdistancescalar) · [`SetGameplayHintFov`](#setgameplayhintfov) · [`SetGameplayObjectHint`](#setgameplayobjecthint) · [`SetGameplayPedHint`](#setgameplaypedhint) · [`SetGameplayVehicleHint`](#setgameplayvehiclehint) · [`SetInVehicleCamStateThisUpdate`](#setinvehiclecamstatethisupdate) · [`SetTableGamesCameraThisUpdate`](#settablegamescamerathisupdate) · [`SetThirdPersonAimCamNearClipThisUpdate`](#setthirdpersonaimcamnearclipthisupdate) · [`SetUseHiDof`](#setusehidof) · [`SetUseHiDofInCutscene`](#setusehidofincutscene) · [`SetWidescreenBorders`](#setwidescreenborders) · [`ShakeCam`](#shakecam) · [`ShakeCinematicCam`](#shakecinematiccam) · [`ShakeGameplayCam`](#shakegameplaycam) · [`ShakeScriptGlobal`](#shakescriptglobal) · [`StopCamPointing`](#stopcampointing) · [`StopCamShaking`](#stopcamshaking) · [`StopCinematicCamShaking`](#stopcinematiccamshaking) · [`StopCinematicShot`](#stopcinematicshot) · [`StopCutsceneCamShaking`](#stopcutscenecamshaking) · [`StopGameplayCamShaking`](#stopgameplaycamshaking) · [`StopGameplayHint`](#stopgameplayhint) · [`StopRenderingScriptCamsUsingCatchUp`](#stoprenderingscriptcamsusingcatchup) · [`StopScriptGlobalShaking`](#stopscriptglobalshaking) · [`UseScriptCamForAmbientPopulationOriginThisFrame`](#usescriptcamforambientpopulationoriginthisframe) · [`UseVehicleCamStuntSettingsThisUpdate`](#usevehiclecamstuntsettingsthisupdate)

---
### ActivateCamWithInterpAndFovCurve

`_ACTIVATE_CAM_WITH_INTERP_AND_FOV_CURVE` · hash `0x34CFC4C2A38E83E3` · **Cliente**

```lua
ActivateCamWithInterpAndFovCurve(camTo, camFrom, duration, easeLocation, easeRotation, easeFove)
```
```c
void _ACTIVATE_CAM_WITH_INTERP_AND_FOV_CURVE(Cam camTo, Cam camFrom, int duration, int easeLocation, int easeRotation, int easeFove);
```

**Parámetros**

- `camTo` (`Cam`)
- `camFrom` (`Cam`)
- `duration` (`int`)
- `easeLocation` (`int`)
- `easeRotation` (`int`)
- `easeFove` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v3258
```

---
### AddCamSplineNode

`ADD_CAM_SPLINE_NODE` · hash `0x8609C75EC438FB3B` · jhash `0xAD3C7EAA` · **Cliente**

```lua
AddCamSplineNode(camera, x, y, z, xRot, yRot, zRot, length, p8, transitionType)
```
```c
void ADD_CAM_SPLINE_NODE(Cam camera, float x, float y, float z, float xRot, float yRot, float zRot, int length, int p8, int transitionType);
```

**Parámetros**

- `camera` (`Cam`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `length` (`int`)
- `p8` (`int`)
- `transitionType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
I filled p1-p6 (the floats) as they are as other natives with 6 floats in a row are similar and I see no other method. So if a test from anyone proves them wrong please correct.  
p7 (length) determines the length of the spline, affects camera path and duration of transition between previous node and this one  
p8 big values ~100 will slow down the camera movement before reaching this node  
p9 != 0 seems to override the rotation/pitch (bool?)  
```

---
### AddCamSplineNodeUsingCamera

`ADD_CAM_SPLINE_NODE_USING_CAMERA` · hash `0x0FB82563989CF4FB` · jhash `0xBA6C085B` · **Cliente**

```lua
AddCamSplineNodeUsingCamera(cam, cam2, length, p3)
```
```c
void ADD_CAM_SPLINE_NODE_USING_CAMERA(Cam cam, Cam cam2, int length, int p3);
```

**Parámetros**

- `cam` (`Cam`): Camera to add cam2 as a node to
- `cam2` (`Cam`): Camera used for reference
- `length` (`int`): Duration used for transition, has no effect for the first node.
- `p3` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Takes a camera and uses the information from it as a camera spline node.

**Nombres antiguos (alias):** `0x0FB82563989CF4FB` (`N_0x0fb82563989cf4fb`)

**Ejemplo (cs):**

```cs
AddCamSplineNodeUsingCamera(cam, CreateCamWithParams("DEFAULT_SCRIPTED_CAMERA", 975.9832f, 191.3923f, 86.82342f, -2.795285f, -0f, 154.0656f, 45f, true, 2), 5000, 3);
```

---
### AddCamSplineNodeUsingCameraFrame

`ADD_CAM_SPLINE_NODE_USING_CAMERA_FRAME` · hash `0x0A9F2A468B328E74` · jhash `0x30510511` · **Cliente**

```lua
AddCamSplineNodeUsingCameraFrame(cam, cam2, p2, p3)
```
```c
void ADD_CAM_SPLINE_NODE_USING_CAMERA_FRAME(Cam cam, Cam cam2, int p2, int p3);
```

**Parámetros**

- `cam` (`Cam`)
- `cam2` (`Cam`)
- `p2` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0A9F2A468B328E74` (`N_0x0a9f2a468b328e74`)

---
### AddCamSplineNodeUsingGameplayFrame

`ADD_CAM_SPLINE_NODE_USING_GAMEPLAY_FRAME` · hash `0x609278246A29CA34` · jhash `0xB4737F03` · **Cliente**

```lua
AddCamSplineNodeUsingGameplayFrame(cam, p1, p2)
```
```c
void ADD_CAM_SPLINE_NODE_USING_GAMEPLAY_FRAME(Cam cam, int p1, int p2);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`int`)
- `p2` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x609278246A29CA34` (`N_0x609278246a29ca34`)

---
### AnimateGameplayCamZoom

`_ANIMATE_GAMEPLAY_CAM_ZOOM` · hash `0xDF2E1F7742402E81` · jhash `0x77340650` · **Cliente**

```lua
AnimateGameplayCamZoom(p0, distance)
```
```c
void _ANIMATE_GAMEPLAY_CAM_ZOOM(float p0, float distance);
```

**Parámetros**

- `p0` (`float`)
- `distance` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Seems to animate the gameplay camera zoom.  
Eg. _ANIMATE_GAMEPLAY_CAM_ZOOM(1f, 1000f);  
will animate the camera zooming in from 1000 meters away.  
Game scripts use it like this:  
// Setting this to 1 prevents V key from changing zoom  
PLAYER::SET_PLAYER_FORCED_ZOOM(PLAYER::PLAYER_ID(), 1);  
// These restrict how far you can move cam up/down left/right  
CAM::_CLAMP_GAMEPLAY_CAM_YAW(-20f, 50f);  
CAM::_CLAMP_GAMEPLAY_CAM_PITCH(-60f, 0f);  
CAM::_ANIMATE_GAMEPLAY_CAM_ZOOM(1f, 1f);  
```

---
### AnimatedShakeCam

`ANIMATED_SHAKE_CAM` · hash `0xA2746EEAE3E577CD` · jhash `0xE1168767` · **Cliente**

```lua
AnimatedShakeCam(cam, p1, p2, p3, amplitude)
```
```c
void ANIMATED_SHAKE_CAM(Cam cam, char* p1, char* p2, char* p3, float amplitude);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`char*`)
- `p2` (`char*`)
- `p3` (`char*`)
- `amplitude` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example from michael2 script.  
CAM::ANIMATED_SHAKE_CAM(l_5069, "shake_cam_all@", "light", "", 1f);  
```

---
### AnimatedShakeScriptGlobal

`ANIMATED_SHAKE_SCRIPT_GLOBAL` · hash `0xC2EAE3FB8CDBED31` · jhash `0xCB75BD9C` · **Cliente**

```lua
AnimatedShakeScriptGlobal(p0, p1, p2, p3)
```
```c
void ANIMATED_SHAKE_SCRIPT_GLOBAL(char* p0, char* p1, char* p2, float p3);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`char*`)
- `p2` (`char*`)
- `p3` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
CAM::ANIMATED_SHAKE_SCRIPT_GLOBAL("SHAKE_CAM_medium", "medium", "", 0.5f);
```

**Nombres antiguos (alias):** `0xC2EAE3FB8CDBED31` (`N_0xc2eae3fb8cdbed31`)

---
### AttachCamToEntity

`ATTACH_CAM_TO_ENTITY` · hash `0xFEDB7D269E8C60E3` · jhash `0xAD7C45F6` · **Cliente**

```lua
AttachCamToEntity(cam, entity, xOffset, yOffset, zOffset, isRelative)
```
```c
void ATTACH_CAM_TO_ENTITY(Cam cam, Entity entity, float xOffset, float yOffset, float zOffset, BOOL isRelative);
```

**Parámetros**

- `cam` (`Cam`): The camera handle.
- `entity` (`Entity`): The entity handle.
- `xOffset` (`float`): X-axis offset
- `yOffset` (`float`): Y-axis offset
- `zOffset` (`float`): Z-axis offset
- `isRelative` (`BOOL`): Whether or not the camera will be relative to the entity

**Devuelve:** `void`

**Descripción oficial:**

```
Last param determines if its relative to the Entity  
```

**Ejemplo (lua):**

```lua
local entity = PlayerPedId()
local cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)

AttachCamToEntity(cam,entity, 0.0, 0.0, 0.0, true) --attach camera to the center of the entity

SetCamActive(cam, true)
RenderScriptCams(true, false, 0, true, true)
```

---
### AttachCamToPedBone

`ATTACH_CAM_TO_PED_BONE` · hash `0x61A3DBA14AB7F411` · jhash `0x506BB35C` · **Cliente**

```lua
AttachCamToPedBone(cam, ped, boneIndex, xOffset, yOffset, zOffset, isRelative)
```
```c
void ATTACH_CAM_TO_PED_BONE(Cam cam, Ped ped, int boneIndex, float xOffset, float yOffset, float zOffset, BOOL isRelative);
```

**Parámetros**

- `cam` (`Cam`): The camera handle.
- `ped` (`Ped`): The ped handle.
- `boneIndex` (`int`): This is different to boneID, use ['GET_PED_BONE_INDEX'](PED-1.md#getpedboneindex) to get the index from the ID. use the index for attaching to specific bones. `cam` will be attached to the center of `ped` if bone index given doesn't correspond to bone indexes for that entity type.
- `xOffset` (`float`): X-axis offset
- `yOffset` (`float`): Y-axis offset
- `zOffset` (`float`): Z-axis offset
- `isRelative` (`BOOL`): Whether or not the camera will be relative to the bone

**Devuelve:** `void`

**Descripción oficial:**

This native works with peds only.

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
local cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)

AttachCamToPedBone(cam,ped,4089, 0.0, 0.0, 0.0, true) -- attach it to a finger on the left hand

SetCamActive(cam, true)
RenderScriptCams(true, false, 0, true, true)
```

---
### AttachCamToVehicleBone

`_ATTACH_CAM_TO_VEHICLE_BONE` · hash `0x8DB3F12A02CAEF72` · **Cliente**

```lua
AttachCamToVehicleBone(cam, vehicle, boneIndex, relativeRotation, rotX, rotY, rotZ, offX, offY, offZ, fixedDirection)
```
```c
void _ATTACH_CAM_TO_VEHICLE_BONE(Cam cam, Vehicle vehicle, int boneIndex, BOOL relativeRotation, float rotX, float rotY, float rotZ, float offX, float offY, float offZ, BOOL fixedDirection);
```

**Parámetros**

- `cam` (`Cam`): The camera handle.
- `vehicle` (`Vehicle`): The vehicle handle.
- `boneIndex` (`int`)
- `relativeRotation` (`BOOL`): Whether or not the camera rotation will relative the vehicle rotation.
- `rotX` (`float`): The X rotation.
- `rotY` (`float`): The Y rotation.
- `rotZ` (`float`): The Z rotation.
- `offX` (`float`): The X offset direction.
- `offY` (`float`): The Y offset direction.
- `offZ` (`float`): The Z offset direction.
- `fixedDirection` (`BOOL`): Whether or not the camera direction will relative to the vehicle direction.

**Devuelve:** `void`

**Descripción oficial:**

This native works with vehicles only.
Bone indexes are usually given by this native [GET_ENTITY_BONE_INDEX_BY_NAME](ENTITY.md#getentityboneindexbyname).

**Nombres antiguos (alias):** `0x8DB3F12A02CAEF72` (`N_0x8db3f12a02caef72`)

---
### ClampGameplayCamPitch

`_CLAMP_GAMEPLAY_CAM_PITCH` · hash `0xA516C198B7DCA1E1` · jhash `0xFA3A16E7` · **Cliente**

```lua
ClampGameplayCamPitch(minimum, maximum)
```
```c
void _CLAMP_GAMEPLAY_CAM_PITCH(float minimum, float maximum);
```

**Parámetros**

- `minimum` (`float`)
- `maximum` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
minimum: Degrees between -90f and 90f.
maximum: Degrees between -90f and 90f.
Clamps the gameplay camera's current pitch.
Eg. _CLAMP_GAMEPLAY_CAM_PITCH(0.0f, 0.0f) will set the vertical angle directly behind the player.
```

---
### ClampGameplayCamYaw

`_CLAMP_GAMEPLAY_CAM_YAW` · hash `0x8F993D26E0CA5E8E` · jhash `0x749909AC` · **Cliente**

```lua
ClampGameplayCamYaw(minimum, maximum)
```
```c
void _CLAMP_GAMEPLAY_CAM_YAW(float minimum, float maximum);
```

**Parámetros**

- `minimum` (`float`)
- `maximum` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
minimum: Degrees between -180f and 180f.
maximum: Degrees between -180f and 180f.
Clamps the gameplay camera's current yaw.
Eg. _CLAMP_GAMEPLAY_CAM_YAW(0.0f, 0.0f) will set the horizontal angle directly behind the player.
```

---
### CreateCam

`CREATE_CAM` · hash `0xC3981DCE61D9E13F` · jhash `0xE9BF2A7D` · **Cliente**

```lua
local retval = CreateCam(camName, active)
```
```c
Cam CREATE_CAM(char* camName, BOOL active);
```

**Parámetros**

- `camName` (`char*`): A string representing the camera type, the game will convert the string into a joaat hash upon native execution.
- `active` (`BOOL`): Set to true if you wish to make this new camera the active camera.

**Devuelve:** `Cam` — A camera handle referencing the camera that was created.

**Descripción oficial:**

Creates a camera with the specified cam name, You can use `SET_CAM_` natives to manipulate the camera.\
Make sure to call [RENDER_SCRIPT_CAMS](#renderscriptcams) once the camera is created, or this won't have any visible effect.

**Camera names:**

*   DEFAULT_SCRIPTED_CAMERA
*   DEFAULT_ANIMATED_CAMERA
*   DEFAULT_SPLINE_CAMERA
*   DEFAULT_SCRIPTED_FLY_CAMERA
*   TIMED_SPLINE_CAMERA
*   CUSTOM_TIMED_SPLINE_CAMERA
*   ROUNDED_SPLINE_CAMERA
*   SMOOTHED_SPLINE_CAMERA

**Ejemplo (lua):**

```lua
local cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)
```

**Ejemplo (js):**

```js
const cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true);
```

**Ejemplo (cs):**

```cs
int cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true);
```

---
### CreateCamWithParams

`CREATE_CAM_WITH_PARAMS` · hash `0xB51194800B257161` · jhash `0x23B02F15` · **Cliente**

```lua
local retval = CreateCamWithParams(camName, posX, posY, posZ, rotX, rotY, rotZ, fov, active, rotationOrder)
```
```c
Cam CREATE_CAM_WITH_PARAMS(char* camName, float posX, float posY, float posZ, float rotX, float rotY, float rotZ, float fov, BOOL active, int rotationOrder);
```

**Parámetros**

- `camName` (`char*`): A string representing the camera type, the game will convert the string into a joaat hash upon native execution.
- `posX` (`float`): The x position of the camera (you can also send a vector3 instead of the bulk coordinates)
- `posY` (`float`): The y position of the camera (you can also send a vector3 instead of the bulk coordinates)
- `posZ` (`float`): The z position of the camera (you can also send a vector3 instead of the bulk coordinates)
- `rotX` (`float`): The x rotation of the camera
- `rotY` (`float`): The y rotation of the camera
- `rotZ` (`float`): The z rotation of the camera
- `fov` (`float`): The Field Of View of the camera, is the observable world that is seen
- `active` (`BOOL`): Set to true if you wish to make this new camera the active camera.
- `rotationOrder` (`int`): The order of rotation, see [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation)

**Devuelve:** `Cam` — A camera handle.

**Descripción oficial:**

Create a camera with the specified cam name/type, You can use `SET_CAM_` natives to manipulate the camera.

Take a look at [CREATE_CAM](#createcam) if you would like to see the available camera names.

**Ejemplo (lua):**

```lua
local cam = CreateCamWithParams("DEFAULT_SCRIPTED_CAMERA", 561.3, 301.3, 63.0, 0.0, 0.0, 0.0, 90.0)
```

**Ejemplo (js):**

```js
const cam = CreateCamWithParams("DEFAULT_SCRIPTED_CAMERA", 561.3, 301.3, 63.0, 0.0, 0.0, 0.0, 90.0);
```

**Ejemplo (cs):**

```cs
int cam = CreateCamWithParams("DEFAULT_SCRIPTED_CAMERA", 561.3f, 301.3f, 63.0f, 0.0f, 0.0f, 0.0f, 90.0f);
```

---
### CreateCamera

`CREATE_CAMERA` · hash `0x5E3CF89C6BCCA67D` · jhash `0x5D6739AE` · **Cliente**

```lua
local retval = CreateCamera(camHash, active)
```
```c
Cam CREATE_CAMERA(Hash camHash, BOOL active);
```

**Parámetros**

- `camHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of the camera type, use [GET_HASH_KEY](../cfx/servidor.md#gethashkey) to get the camera hash from the name.
- `active` (`BOOL`): Set to true if you wish to make this new camera the active camera.

**Devuelve:** `Cam` — A camera handle referencing the camera that was created.

**Descripción oficial:**

Creates a camera with the specified camera hash, You can use `SET_CAM_` natives to manipulate the camera.
Make sure to call [RENDER_SCRIPT_CAMS](#renderscriptcams) once the camera is created, or this won't have any visible effect.

Take a look at [CREATE_CAM](#createcam) if you would like to see the available camera names.

```
NativeDB Introduced: v323
```

**Ejemplo (lua):**

```lua
-- creates a camera with the "DEFAULT_SCRIPTED_CAMERA" type
local cam = CreateCamera(GetHashKey("DEFAULT_SCRIPTED_CAMERA"), true)

RenderScriptCams(true, false, 0, true, true)
```

**Ejemplo (js):**

```js
// creates a camera with the "DEFAULT_SCRIPTED_CAMERA" type
const cam = CreateCamera(GetHashKey("DEFAULT_SCRIPTED_CAMERA"), true);

RenderScriptCams(true, false, 0, true, true)
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// creates a camera with the "DEFAULT_SCRIPTED_CAMERA" type
int cam = CreateCamera(GetHashKey("DEFAULT_SCRIPTED_CAMERA"), true);

RenderScriptCams(true, false, 0, true, true);
```

---
### CreateCameraWithParams

`CREATE_CAMERA_WITH_PARAMS` · hash `0x6ABFA3E16460F22D` · jhash `0x0688BE9A` · **Cliente**

```lua
local retval = CreateCameraWithParams(camHash, posX, posY, posZ, rotX, rotY, rotZ, fov, active, rotationOrder)
```
```c
Cam CREATE_CAMERA_WITH_PARAMS(Hash camHash, float posX, float posY, float posZ, float rotX, float rotY, float rotZ, float fov, BOOL active, int rotationOrder);
```

**Parámetros**

- `camHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The hash of the camera type, use [GET_HASH_KEY](../cfx/servidor.md#gethashkey) to get the camera hash from the name.
- `posX` (`float`): The x position of the camera.
- `posY` (`float`): The y position of the camera.
- `posZ` (`float`): The z position of the camera.
- `rotX` (`float`): The x rotation of the camera.
- `rotY` (`float`): The y rotation of the camera.
- `rotZ` (`float`): The z rotation of the camera.
- `fov` (`float`): The Field Of View of the camera, is the observable world that is seen.
- `active` (`BOOL`): Set to true if you wish to make this new camera the active camera.
- `rotationOrder` (`int`): The order of rotation, see [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation).

**Devuelve:** `Cam` — A camera handle.

**Descripción oficial:**

Create a camera with the specified camera hash, You can use `SET_CAM_` natives to manipulate the camera.
Make sure to call [RENDER_SCRIPT_CAMS](#renderscriptcams) once the camera is created, or this won't have any visible effect.

Take a look at [CREATE_CAM](#createcam) if you would like to see the available camera names.

```
NativeDB Introduced: v323
```

---
### CreateCinematicShot

`CREATE_CINEMATIC_SHOT` · hash `0x741B0129D4560F31` · jhash `0xAC494E35` · **Cliente**

```lua
CreateCinematicShot(p0, p1, p2, entity)
```
```c
void CREATE_CINEMATIC_SHOT(Any p0, int p1, Any p2, Entity entity);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`int`)
- `p2` (`Any`)
- `entity` (`Entity`)

**Devuelve:** `void`

---
### CustomMenuCoordinates

`CUSTOM_MENU_COORDINATES` · hash `0x487A82C650EB7799` · jhash `0xA6E73135` · **Cliente**

```lua
CustomMenuCoordinates(p0)
```
```c
void CUSTOM_MENU_COORDINATES(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
some camera effect that is used in the drunk-cheat, and turned off (by setting it to 0.0) along with the shaking effects once the drunk cheat is disabled.  
```

**Nombres antiguos (alias):** `0x487A82C650EB7799` (`N_0x487a82c650eb7799`)

---
### DestroyAllCams

`DESTROY_ALL_CAMS` · hash `0x8E5FB15663F79120` · jhash `0x10C151CE` · **Cliente**

```lua
DestroyAllCams(bScriptHostCam)
```
```c
void DESTROY_ALL_CAMS(BOOL bScriptHostCam);
```

**Parámetros**

- `bScriptHostCam` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
BOOL param indicates whether the cam should be destroyed if it belongs to the calling script.  
```

---
### DestroyCam

`DESTROY_CAM` · hash `0x865908C81A2C22E9` · jhash `0xC39302BD` · **Cliente**

```lua
DestroyCam(cam, bScriptHostCam)
```
```c
void DESTROY_CAM(Cam cam, BOOL bScriptHostCam);
```

**Parámetros**

- `cam` (`Cam`)
- `bScriptHostCam` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
BOOL param indicates whether the cam should be destroyed if it belongs to the calling script.  
```

---
### DetachCam

`DETACH_CAM` · hash `0xA2FABBE87F4BAD82` · jhash `0xF4FBF14A` · **Cliente**

```lua
DetachCam(cam)
```
```c
void DETACH_CAM(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `void`

---
### DisableAimCamThisUpdate

`DISABLE_AIM_CAM_THIS_UPDATE` · hash `0x1A31FE0049E542F6` · jhash `0x1BAA7182` · **Cliente**

```lua
DisableAimCamThisUpdate()
```
```c
void DISABLE_AIM_CAM_THIS_UPDATE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1A31FE0049E542F6` (`N_0x1a31fe0049e542f6`)

---
### DisableCamCollisionForEntity

`_DISABLE_CAM_COLLISION_FOR_ENTITY` · hash `0x2AED6301F67007D5` · jhash `0x2701A9AD` · **Cliente**

```lua
DisableCamCollisionForEntity(entity)
```
```c
void _DISABLE_CAM_COLLISION_FOR_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2AED6301F67007D5` (`N_0x2aed6301f67007d5`)

---
### DisableCamCollisionForObject

`DISABLE_CAM_COLLISION_FOR_OBJECT` · hash `0x49482F9FCD825AAA` · jhash `0xC4736ED3` · **Cliente**

```lua
DisableCamCollisionForObject(entity)
```
```c
void DISABLE_CAM_COLLISION_FOR_OBJECT(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x49482F9FCD825AAA` (`N_0x49482f9fcd825aaa`)

---
### DisableCinematicBonnetCameraThisUpdate

`DISABLE_CINEMATIC_BONNET_CAMERA_THIS_UPDATE` · hash `0xADFF1B2A555F5FBA` · jhash `0x5AC6DAC9` · **Cliente**

```lua
DisableCinematicBonnetCameraThisUpdate()
```
```c
void DISABLE_CINEMATIC_BONNET_CAMERA_THIS_UPDATE();
```

**Devuelve:** `void`

**Descripción oficial:**

Disables first person camera while in a vehicle for the current tick.

**Nombres antiguos (alias):** `_DISABLE_VEHICLE_FIRST_PERSON_CAM_THIS_FRAME` (`DisableVehicleFirstPersonCamThisFrame`)

---
### DisableOnFootFirstPersonViewThisUpdate

`DISABLE_ON_FOOT_FIRST_PERSON_VIEW_THIS_UPDATE` · hash `0xDE2EF5DA284CC8DF` · **Cliente**

```lua
DisableOnFootFirstPersonViewThisUpdate()
```
```c
void DISABLE_ON_FOOT_FIRST_PERSON_VIEW_THIS_UPDATE();
```

**Devuelve:** `void`

**Descripción oficial:**

Disables first person camera while on foot for the current tick.

**Nombres antiguos (alias):** `_DISABLE_FIRST_PERSON_CAM_THIS_FRAME` (`DisableFirstPersonCamThisFrame`)

---
### DoScreenFadeIn

`DO_SCREEN_FADE_IN` · hash `0xD4E8E24955024033` · jhash `0x66C1BDEE` · **Cliente**

```lua
DoScreenFadeIn(duration)
```
```c
void DO_SCREEN_FADE_IN(int duration);
```

**Parámetros**

- `duration` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Fades the screen in.  
duration: The time the fade should take, in milliseconds.  
```

---
### DoScreenFadeOut

`DO_SCREEN_FADE_OUT` · hash `0x891B5B39AC6302AF` · jhash `0x89D01805` · **Cliente**

```lua
DoScreenFadeOut(duration)
```
```c
void DO_SCREEN_FADE_OUT(int duration);
```

**Parámetros**

- `duration` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Fades the screen out.  
duration: The time the fade should take, in milliseconds.  
```

---
### DoesCamExist

`DOES_CAM_EXIST` · hash `0xA7A932170592B50E` · jhash `0x1EF89DC0` · **Cliente**

```lua
local retval = DoesCamExist(cam)
```
```c
BOOL DOES_CAM_EXIST(Cam cam);
```

**Parámetros**

- `cam` (`Cam`): The camera handle to look for.

**Devuelve:** `BOOL` — A boolean value representing whether the camera exists or not.

**Descripción oficial:**

Looks up a camera handle in the current camera pool and returns `true` if the handle is found, otherwise it returns `false`.

---
### EnableCrosshairThisFrame

`_ENABLE_CROSSHAIR_THIS_FRAME` · hash `0xEA7F0AD7E9BA676F` · jhash `0xA61FF9AC` · **Cliente**

```lua
EnableCrosshairThisFrame()
```
```c
void _ENABLE_CROSSHAIR_THIS_FRAME();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Shows the crosshair even if it wouldn't show normally. Only works for one frame, so make sure to call it repeatedly.  
```

---
### ForceCinematicRenderingThisUpdate

`FORCE_CINEMATIC_RENDERING_THIS_UPDATE` · hash `0xA41BCD7213805AAC` · jhash `0xFBB85E02` · **Cliente**

```lua
ForceCinematicRenderingThisUpdate(enable)
```
```c
void FORCE_CINEMATIC_RENDERING_THIS_UPDATE(BOOL enable);
```

**Parámetros**

- `enable` (`BOOL`): Whether it should force the cinematic rendering or not.

**Devuelve:** `void`

**Descripción oficial:**

Forces the camera to be in cinematic mode while the player is in a car. This has to be called every frame, e.g. in a `Wait(0)` loop.

**Nombres antiguos (alias):** `0xA41BCD7213805AAC` (`N_0xa41bcd7213805aac`)

---
### GetCamActiveViewModeContext

`_GET_CAM_ACTIVE_VIEW_MODE_CONTEXT` · hash `0x19CAFA3C87F7C2FF` · **Cliente**

```lua
local retval = GetCamActiveViewModeContext()
```
```c
int _GET_CAM_ACTIVE_VIEW_MODE_CONTEXT();
```

**Devuelve:** `int` — The active view mode context.

**Descripción oficial:**

Enumerated type defined in camControlHelperMetadataViewModes:

```cpp
enum eContext {
    ON_FOOT = 0, // [G|S]ET_FOLLOW_PED_CAM_*
    IN_VEHICLE = 1, // [G|S]ET_FOLLOW_VEHICLE_CAM_*
    ON_BIKE = 2,
    IN_BOAT = 3,
    IN_AIRCRAFT = 4,
    IN_SUBMARINE = 5,
    IN_HELI = 6,
    IN_TURRET = 7,
}
```

**Nombres antiguos (alias):** `0x19CAFA3C87F7C2FF` (`N_0x19cafa3c87f7c2ff`)

---
### GetCamAnimCurrentPhase

`GET_CAM_ANIM_CURRENT_PHASE` · hash `0xA10B2DB49E92A6B0` · jhash `0x345F72D0` · **Cliente**

```lua
local retval = GetCamAnimCurrentPhase(cam)
```
```c
float GET_CAM_ANIM_CURRENT_PHASE(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

---
### GetCamCoord

`GET_CAM_COORD` · hash `0xBAC038F7459AE5AE` · jhash `0x7C40F09C` · **Cliente**

```lua
local retval = GetCamCoord(cam)
```
```c
Vector3 GET_CAM_COORD(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `Vector3`

---
### GetCamDofStrength

`_GET_CAM_DOF_STRENGTH` · hash `0x06D153C0B99B6128` · **Cliente**

```lua
local retval = GetCamDofStrength(cam)
```
```c
float _GET_CAM_DOF_STRENGTH(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### GetCamFarClip

`GET_CAM_FAR_CLIP` · hash `0xB60A9CFEB21CA6AA` · jhash `0x09F119B8` · **Cliente**

```lua
local retval = GetCamFarClip(cam)
```
```c
float GET_CAM_FAR_CLIP(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

---
### GetCamFarDof

`GET_CAM_FAR_DOF` · hash `0x255F8DAFD540D397` · jhash `0x98C5CCE9` · **Cliente**

```lua
local retval = GetCamFarDof(cam)
```
```c
float GET_CAM_FAR_DOF(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

---
### GetCamFov

`GET_CAM_FOV` · hash `0xC3330A45CCCDB26A` · jhash `0xD6E9FCF5` · **Cliente**

```lua
local retval = GetCamFov(cam)
```
```c
float GET_CAM_FOV(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

---
### GetCamNearClip

`GET_CAM_NEAR_CLIP` · hash `0xC520A34DAFBF24B1` · jhash `0xCFCD35EE` · **Cliente**

```lua
local retval = GetCamNearClip(cam)
```
```c
float GET_CAM_NEAR_CLIP(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

---
### GetCamNearDof

`_GET_CAM_NEAR_DOF` · hash `0xC2612D223D915A1C` · **Cliente**

```lua
local retval = GetCamNearDof(cam)
```
```c
float _GET_CAM_NEAR_DOF(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

**Descripción oficial:**

```
NativeDB Introduced: v2699
```

---
### GetCamRot

`GET_CAM_ROT` · hash `0x7D304C1C955E3E12` · jhash `0xDAC84C9F` · **Cliente**

```lua
local retval = GetCamRot(cam, rotationOrder)
```
```c
Vector3 GET_CAM_ROT(Cam cam, int rotationOrder);
```

**Parámetros**

- `cam` (`Cam`): The camera handle.
- `rotationOrder` (`int`): The order of rotation, see [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation)

**Devuelve:** `Vector3` — A `Vector3` representing the camera rotation in degrees.

**Descripción oficial:**

Gets a camera's rotation by handle (`cam`) lookup, outputs a `Vector3` in degrees.

**Ejemplo (lua):**

```lua
-- We need a valid camera handle for this to work.
local theCamHandle = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)

-- Let's set the camera rotation for illustrative purposes
SetCamRot(theCamHandle, 0.1, 0.2, 0.3, 0)

-- We are now able to get the camera rotation.
local camRot = GetCamRot(theCamHandle, 0) -- vector3(0.100000, 0.200000, 0.300000)
Citizen.Trace(string.format("Cam Rotation is x: %f, y: %f, z: %f", camRot.x, camRot.y, camRot.z))
```

---
### GetCamSplineNodeIndex

`GET_CAM_SPLINE_NODE_INDEX` · hash `0xB22B17DF858716A6` · jhash `0xF8AEB6BD` · **Cliente**

```lua
local retval = GetCamSplineNodeIndex(cam)
```
```c
int GET_CAM_SPLINE_NODE_INDEX(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `int`

---
### GetCamSplineNodePhase

`GET_CAM_SPLINE_NODE_PHASE` · hash `0xD9D0E694C8282C96` · jhash `0x7B9522F6` · **Cliente**

```lua
local retval = GetCamSplineNodePhase(cam)
```
```c
float GET_CAM_SPLINE_NODE_PHASE(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

**Descripción oficial:**

```
I'm pretty sure the parameter is the camera as usual, but I am not certain so I'm going to leave it as is.  
```

---
### GetCamSplinePhase

`GET_CAM_SPLINE_PHASE` · hash `0xB5349E36C546509A` · jhash `0x39784DD9` · **Cliente**

```lua
local retval = GetCamSplinePhase(cam)
```
```c
float GET_CAM_SPLINE_PHASE(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `float`

**Descripción oficial:**

```
Can use this with SET_CAM_SPLINE_PHASE to set the float it this native returns.  
(returns 1.0f when no nodes has been added, reached end of non existing spline)  
```

---
### GetCamViewModeForContext

`GET_CAM_VIEW_MODE_FOR_CONTEXT` · hash `0xEE778F8C7E1142E2` · jhash `0xF3B148A6` · **Cliente**

```lua
local retval = GetCamViewModeForContext(context)
```
```c
int GET_CAM_VIEW_MODE_FOR_CONTEXT(int context);
```

**Parámetros**

- `context` (`int`): See [`_GET_CAM_ACTIVE_VIEW_MODE_CONTEXT`](#getcamactiveviewmodecontext).

**Devuelve:** `int`

**Descripción oficial:**

See [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode) for the view mode enum.

**Nombres antiguos (alias):** `0xEE778F8C7E1142E2` (`N_0xee778f8c7e1142e2`)

---
### GetDebugCamera

`_GET_DEBUG_CAMERA` · hash `0x77C3CEC46BE286F6` · **Cliente**

```lua
local retval = GetDebugCamera()
```
```c
Cam _GET_DEBUG_CAMERA();
```

**Devuelve:** `Cam`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x77C3CEC46BE286F6` (`N_0x77c3cec46be286f6`)

---
### GetFinalRenderedCamCoord

`GET_FINAL_RENDERED_CAM_COORD` · hash `0xA200EB1EE790F448` · jhash `0x9C84BDA0` · **Cliente**

```lua
local retval = GetFinalRenderedCamCoord()
```
```c
Vector3 GET_FINAL_RENDERED_CAM_COORD();
```

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `_GET_GAMEPLAY_CAM_COORDS` (`GetGameplayCamCoords`)

---
### GetFinalRenderedCamFarClip

`GET_FINAL_RENDERED_CAM_FAR_CLIP` · hash `0xDFC8CBC606FDB0FC` · jhash `0x46CB3A49` · **Cliente**

```lua
local retval = GetFinalRenderedCamFarClip()
```
```c
float GET_FINAL_RENDERED_CAM_FAR_CLIP();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xDFC8CBC606FDB0FC` (`N_0xdfc8cbc606fdb0fc`), `_GET_GAMEPLAY_CAM_FAR_CLIP` (`GetGameplayCamFarClip`)

---
### GetFinalRenderedCamFarDof

`GET_FINAL_RENDERED_CAM_FAR_DOF` · hash `0x9780F32BCAF72431` · jhash `0xF24777CA` · **Cliente**

```lua
local retval = GetFinalRenderedCamFarDof()
```
```c
float GET_FINAL_RENDERED_CAM_FAR_DOF();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x9780F32BCAF72431` (`N_0x9780f32bcaf72431`), `_GET_GAMEPLAY_CAM_FAR_DOF` (`GetGameplayCamFarDof`)

---
### GetFinalRenderedCamFov

`GET_FINAL_RENDERED_CAM_FOV` · hash `0x80EC114669DAEFF4` · jhash `0x721B763B` · **Cliente**

```lua
local retval = GetFinalRenderedCamFov()
```
```c
float GET_FINAL_RENDERED_CAM_FOV();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x80EC114669DAEFF4` (`N_0x80ec114669daeff4`)

---
### GetFinalRenderedCamMotionBlurStrength

`GET_FINAL_RENDERED_CAM_MOTION_BLUR_STRENGTH` · hash `0x162F9D995753DC19` · jhash `0x38992E83` · **Cliente**

```lua
local retval = GetFinalRenderedCamMotionBlurStrength()
```
```c
float GET_FINAL_RENDERED_CAM_MOTION_BLUR_STRENGTH();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x162F9D995753DC19` (`N_0x162f9d995753dc19`), `_GET_GAMEPLAY_CAM_FAR_CLIP_2` (`GetGameplayCamFarClip_2`)

---
### GetFinalRenderedCamNearClip

`GET_FINAL_RENDERED_CAM_NEAR_CLIP` · hash `0xD0082607100D7193` · jhash `0x457AE195` · **Cliente**

```lua
local retval = GetFinalRenderedCamNearClip()
```
```c
float GET_FINAL_RENDERED_CAM_NEAR_CLIP();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xD0082607100D7193` (`N_0xd0082607100d7193`), `_GET_GAMEPLAY_CAM_NEAR_CLIP` (`GetGameplayCamNearClip`)

---
### GetFinalRenderedCamNearDof

`GET_FINAL_RENDERED_CAM_NEAR_DOF` · hash `0xA03502FC581F7D9B` · jhash `0x19297A7A` · **Cliente**

```lua
local retval = GetFinalRenderedCamNearDof()
```
```c
float GET_FINAL_RENDERED_CAM_NEAR_DOF();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xA03502FC581F7D9B` (`N_0xa03502fc581f7d9b`), `_GET_GAMEPLAY_CAM_NEAR_DOF` (`GetGameplayCamNearDof`)

---
### GetFinalRenderedCamRot

`GET_FINAL_RENDERED_CAM_ROT` · hash `0x5B4E4C817FCC2DFB` · jhash `0x1FFBEFC5` · **Cliente**

```lua
local retval = GetFinalRenderedCamRot(rotationOrder)
```
```c
Vector3 GET_FINAL_RENDERED_CAM_ROT(int rotationOrder);
```

**Parámetros**

- `rotationOrder` (`int`)

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `_GET_GAMEPLAY_CAM_ROT_2` (`GetGameplayCamRot_2`)

---
### GetFinalRenderedInWhenFriendlyFov

`GET_FINAL_RENDERED_IN_WHEN_FRIENDLY_FOV` · hash `0x5F35F6732C3FBBA0` · jhash `0x23E3F106` · **Cliente**

```lua
local retval = GetFinalRenderedInWhenFriendlyFov(player)
```
```c
float GET_FINAL_RENDERED_IN_WHEN_FRIENDLY_FOV(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x5F35F6732C3FBBA0` (`N_0x5f35f6732c3fbba0`)

---
### GetFinalRenderedInWhenFriendlyRot

`GET_FINAL_RENDERED_IN_WHEN_FRIENDLY_ROT` · hash `0x26903D9CD1175F2C` · jhash `0xACADF916` · **Cliente**

```lua
local retval = GetFinalRenderedInWhenFriendlyRot(player, rotationOrder)
```
```c
Vector3 GET_FINAL_RENDERED_IN_WHEN_FRIENDLY_ROT(Player player, int rotationOrder);
```

**Parámetros**

- `player` (`Player`)
- `rotationOrder` (`int`)

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `0x26903D9CD1175F2C` (`N_0x26903d9cd1175f2c`)

---
### GetFirstPersonAimCamZoomFactor

`GET_FIRST_PERSON_AIM_CAM_ZOOM_FACTOR` · hash `0x7EC52CC40597D170` · jhash `0x33951005` · **Cliente**

```lua
local retval = GetFirstPersonAimCamZoomFactor()
```
```c
float GET_FIRST_PERSON_AIM_CAM_ZOOM_FACTOR();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `_GET_GAMEPLAY_CAM_ZOOM` (`GetGameplayCamZoom`)

---
### GetFocusPedOnScreen

`GET_FOCUS_PED_ON_SCREEN` · hash `0x89215EC747DF244A` · jhash `0xFD99BE2B` · **Cliente**

```lua
local retval = GetFocusPedOnScreen(p0, p1, p2, p3, p4, p5, p6, p7, p8)
```
```c
Ped GET_FOCUS_PED_ON_SCREEN(float p0, int p1, float p2, float p3, float p4, float p5, float p6, int p7, int p8);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`int`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`int`)
- `p8` (`int`)

**Devuelve:** `Ped`

**Nombres antiguos (alias):** `0x89215EC747DF244A` (`N_0x89215ec747df244a`)

---
### GetFollowPedCamViewMode

`GET_FOLLOW_PED_CAM_VIEW_MODE` · hash `0x8D4D46230B2C353A` · jhash `0xA65FF946` · **Cliente**

```lua
local retval = GetFollowPedCamViewMode()
```
```c
int GET_FOLLOW_PED_CAM_VIEW_MODE();
```

**Devuelve:** `int` — Returns a value from the view mode enumeration

**Descripción oficial:**

```cpp
// view mode enumeration
enum eCamViewMode 
{
	THIRD_PERSON_NEAR = 0,
	THIRD_PERSON_MEDIUM = 1,
	THIRD_PERSON_FAR = 2,
	CINEMATIC = 3,
	FIRST_PERSON = 4,
};
```

---
### GetFollowPedCamZoomLevel

`GET_FOLLOW_PED_CAM_ZOOM_LEVEL` · hash `0x33E6C8EFD0CD93E9` · jhash `0x57583DF1` · **Cliente**

```lua
local retval = GetFollowPedCamZoomLevel()
```
```c
int GET_FOLLOW_PED_CAM_ZOOM_LEVEL();
```

**Devuelve:** `int`

**Descripción oficial:**

See [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode) for the follow mode enum.

---
### GetFollowVehicleCamViewMode

`GET_FOLLOW_VEHICLE_CAM_VIEW_MODE` · hash `0xA4FF579AC0E3AAAE` · jhash `0xA4B4DB03` · **Cliente**

```lua
local retval = GetFollowVehicleCamViewMode()
```
```c
int GET_FOLLOW_VEHICLE_CAM_VIEW_MODE();
```

**Devuelve:** `int`

**Descripción oficial:**

See [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode) for the follow mode enum.

---
### GetFollowVehicleCamZoomLevel

`GET_FOLLOW_VEHICLE_CAM_ZOOM_LEVEL` · hash `0xEE82280AB767B690` · jhash `0x8CD67DE3` · **Cliente**

```lua
local retval = GetFollowVehicleCamZoomLevel()
```
```c
int GET_FOLLOW_VEHICLE_CAM_ZOOM_LEVEL();
```

**Devuelve:** `int`

**Descripción oficial:**

See [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode) for the follow mode enum.

---
### GetGameplayCamCoord

`GET_GAMEPLAY_CAM_COORD` · hash `0x14D6F5678D8F1B37` · jhash `0x9388CF79` · **Cliente**

```lua
local retval = GetGameplayCamCoord()
```
```c
Vector3 GET_GAMEPLAY_CAM_COORD();
```

**Devuelve:** `Vector3`

---
### GetGameplayCamFov

`GET_GAMEPLAY_CAM_FOV` · hash `0x65019750A0324133` · jhash `0x4D6B3BFA` · **Cliente**

```lua
local retval = GetGameplayCamFov()
```
```c
float GET_GAMEPLAY_CAM_FOV();
```

**Devuelve:** `float`

---
### GetGameplayCamRelativeHeading

`GET_GAMEPLAY_CAM_RELATIVE_HEADING` · hash `0x743607648ADD4587` · jhash `0xCAF839C2` · **Cliente**

```lua
local retval = GetGameplayCamRelativeHeading()
```
```c
float GET_GAMEPLAY_CAM_RELATIVE_HEADING();
```

**Devuelve:** `float`

---
### GetGameplayCamRelativePitch

`GET_GAMEPLAY_CAM_RELATIVE_PITCH` · hash `0x3A6867B4845BEDA2` · jhash `0xFC5A4946` · **Cliente**

```lua
local retval = GetGameplayCamRelativePitch()
```
```c
float GET_GAMEPLAY_CAM_RELATIVE_PITCH();
```

**Devuelve:** `float` — Returns the relative pitch of the gameplay camera

**Ejemplo (lua):**

```lua
local pitch = GetGameplayCamRelativePitch()
print("LocalPlayer pitch: " .. pitch)
```

---
### GetGameplayCamRot

`GET_GAMEPLAY_CAM_ROT` · hash `0x837765A25378F0BB` · jhash `0x13A010B5` · **Cliente**

```lua
local retval = GetGameplayCamRot(rotationOrder)
```
```c
Vector3 GET_GAMEPLAY_CAM_ROT(int rotationOrder);
```

**Parámetros**

- `rotationOrder` (`int`): The order of rotation, see [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation)

**Devuelve:** `Vector3` — A `Vector3` representing the gameplay camera rotation in degrees.

**Descripción oficial:**

This function takes a rotation order and outputs a `Vector3` in degrees.

It first calls a game function to calculate these values given the rotation order and effectively multiplies those values by `180/PI`, hence degrees since the function it calls outputs radians which are then converted to degrees.

**Ejemplo (lua):**

```lua
local camRot = GetGameplayCamRot(0) -- vector3(-14.74518, 0.05254443, 95.24616)
Citizen.Trace(string.format("Cam Rotation is x: %f, y: %f, z: %f", camRot.x, camRot.y, camRot.z))
```

---
### GetRenderingCam

`GET_RENDERING_CAM` · hash `0x5234F9F10919EABA` · jhash `0x0FCF4DF1` · **Cliente**

```lua
local retval = GetRenderingCam()
```
```c
Cam GET_RENDERING_CAM();
```

**Devuelve:** `Cam`

---
### HardAttachCamToEntity

`HARD_ATTACH_CAM_TO_ENTITY` · hash `0x202A5ED9CE01D6E7` · **Cliente**

```lua
HardAttachCamToEntity(cam, entity, xRot, yRot, zRot, xOffset, yOffset, zOffset, isRelative)
```
```c
void HARD_ATTACH_CAM_TO_ENTITY(Cam cam, Entity entity, float xRot, float yRot, float zRot, float xOffset, float yOffset, float zOffset, BOOL isRelative);
```

**Parámetros**

- `cam` (`Cam`): The camera handle.
- `entity` (`Entity`): The entity handle.
- `xRot` (`float`): X-axis rotation.
- `yRot` (`float`): Y-axis rotation.
- `zRot` (`float`): Z-axis rotation.
- `xOffset` (`float`): X-axis offset
- `yOffset` (`float`): Y-axis offset
- `zOffset` (`float`): Z-axis offset
- `isRelative` (`BOOL`): Whether or not the camera position will be relative to the entity rotation

**Devuelve:** `void`

**Descripción oficial:**

Attaches a camera to an entity, including full matrix transformations for both rotation and position offsets.

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `0x202A5ED9CE01D6E7` (`N_0x202a5ed9ce01d6e7`)

**Ejemplo (lua):**

```lua
-- assuming that the obj variable was created earlier in the script
local cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)

-- attaches the camera to the object rotated 90 degrees and offset 10 x values
HardAttachCamToEntity(cam, obj, 0.0, 0.0, 90.0, 10.0, 0.0, 0.0, true)

-- renders the camera
RenderScriptCams(true, false, 0, true, true)
```

**Ejemplo (js):**

```js
// assuming that the obj variable was created earlier in the script
const cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)

// attaches the camera to the object rotated 90 degrees and offset 10 x values
HardAttachCamToEntity(cam, obj, 0.0, 0.0, 90.0, 10.0, 0.0, 0.0, true)

// renders the camera
RenderScriptCams(true, false, 0, true, true)
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// assuming that the obj variable was created earlier in the script
int cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true);

// attaches the camera to the object rotated 90 degrees and offset 10 x values
HardAttachCamToEntity(cam, obj, 0.0f, 0.0f, 90.0f, 10.0f, 0.0f, 0.0f, true);

// renders the camera
RenderScriptCams(true, false, 0, true, true);
```

---
### HardAttachCamToPedBone

`HARD_ATTACH_CAM_TO_PED_BONE` · hash `0x149916F50C34A40D` · **Cliente**

```lua
HardAttachCamToPedBone(cam, ped, boneIndex, xRot, yRot, zRot, xOffset, yOffset, zOffset, isRelative)
```
```c
void HARD_ATTACH_CAM_TO_PED_BONE(Cam cam, Ped ped, int boneIndex, float xRot, float yRot, float zRot, float xOffset, float yOffset, float zOffset, BOOL isRelative);
```

**Parámetros**

- `cam` (`Cam`): The camera handle.
- `ped` (`Ped`): The ped handle.
- `boneIndex` (`int`): This is different to boneID, use [`GET_PED_BONE_INDEX`](PED-1.md#getpedboneindex) to get the index from the ID. use the index for attaching to specific bones. `cam` will be attached to the center of `ped` if bone index given doesn't correspond to bone indexes for that entity type.
- `xRot` (`float`): X-axis rotation.
- `yRot` (`float`): Y-axis rotation.
- `zRot` (`float`): Z-axis rotation.
- `xOffset` (`float`): X-axis offset.
- `yOffset` (`float`): Y-axis offset.
- `zOffset` (`float`): Z-axis offset.
- `isRelative` (`BOOL`): Whether or not the camera position will be relative to the bone rotation.

**Devuelve:** `void`

**Descripción oficial:**

Attaches a camera to a specific bone of a Ped, including full matrix transformations for both rotation and position offsets.
This native works with peds only.

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0x149916F50C34A40D` (`N_0x149916f50c34a40d`), `_ATTACH_CAM_TO_PED_BONE_2` (`AttachCamToPedBone_2`)

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
local cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)
local BONETAG_L_FINGER01 = 4089

-- attach it to a finger on the left hand and rotates it 90 degrees on the X-axis
HardAttachCamToPedBone(cam, ped, BONETAG_L_FINGER01, 90.0, 0.0, 0.0, 0.0, 0.0, 0.0, true)

-- renders the camera
RenderScriptCams(true, false, 0, true, true)
```

**Ejemplo (js):**

```js
const ped = PlayerPedId()
const cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)
const BONETAG_L_FINGER01= 4089

// attach it to a finger on the left hand and rotates it 90 degrees on the X-axis
HardAttachCamToPedBone(cam, ped, BONETAG_L_FINGER01, 90.0, 0.0, 0.0, 0.0, 0.0, 0.0, true)

// renders the camera
RenderScriptCams(true, false, 0, true, true)
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int ped = PlayerPedId();
int cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true);
int BONETAG_L_FINGER01 = 4089;

// attach it to a finger on the left hand and rotates it 90 degrees on the X-axis
HardAttachCamToPedBone(cam, ped, BONETAG_L_FINGER01, 90.0f, 0.0f, 0.0f, 0.0f, 0.0f, 0.0f, true);

// renders the camera
RenderScriptCams(true, false, 0, true, true);
```

---
### IgnoreMenuPreferenceForBonnetCameraThisUpdate

`IGNORE_MENU_PREFERENCE_FOR_BONNET_CAMERA_THIS_UPDATE` · hash `0x7B8A361C1813FBEF` · **Cliente**

```lua
IgnoreMenuPreferenceForBonnetCameraThisUpdate()
```
```c
void IGNORE_MENU_PREFERENCE_FOR_BONNET_CAMERA_THIS_UPDATE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7B8A361C1813FBEF` (`N_0x7b8a361c1813fbef`)

---
### InterpolateCamWithParams

`_INTERPOLATE_CAM_WITH_PARAMS` · hash `0xDDA77EE33C005AAF` · **Cliente**

```lua
InterpolateCamWithParams(camera, camPosX, camPosY, camPosZ, camRotX, camRotY, camRotZ, fov, duration, posCurveType, rotCurveType, rotOrder, fovCurveType)
```
```c
void _INTERPOLATE_CAM_WITH_PARAMS(Cam camera, float camPosX, float camPosY, float camPosZ, float camRotX, float camRotY, float camRotZ, float fov, int duration, int posCurveType, int rotCurveType, int rotOrder, int fovCurveType);
```

**Parámetros**

- `camera` (`Cam`)
- `camPosX` (`float`)
- `camPosY` (`float`)
- `camPosZ` (`float`)
- `camRotX` (`float`)
- `camRotY` (`float`)
- `camRotZ` (`float`)
- `fov` (`float`)
- `duration` (`int`)
- `posCurveType` (`int`)
- `rotCurveType` (`int`)
- `rotOrder` (`int`)
- `fovCurveType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Interpolates the camera to specified parameters over a set duration using various curve types for position, rotation, and fov.

```
NativeDB Introduced: v3258
```

---
### InvalidateIdleCam

`INVALIDATE_IDLE_CAM` · hash `0xF4F2C0D4EE209E20` · jhash `0xD75CDD75` · **Cliente**

```lua
InvalidateIdleCam()
```
```c
void INVALIDATE_IDLE_CAM();
```

**Devuelve:** `void`

**Descripción oficial:**

Resets the idle camera timer. Calling that in a loop once every few seconds is enough to disable the idle cinematic camera.

**Nombres antiguos (alias):** `0xF4F2C0D4EE209E20` (`N_0xf4f2c0d4ee209e20`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
	while true do
		InvalidateIdleCam()
		InvalidateVehicleIdleCam()
		Wait(1000) --The idle camera activates after 30 second so we don't need to call this per frame
	end
end)
```

---
### InvalidateVehicleIdleCam

`_INVALIDATE_VEHICLE_IDLE_CAM` · hash `0x9E4CFFF989258472` · jhash `0x65DDE8AF` · **Cliente**

```lua
InvalidateVehicleIdleCam()
```
```c
void _INVALIDATE_VEHICLE_IDLE_CAM();
```

**Devuelve:** `void`

**Descripción oficial:**

Resets the vehicle idle camera timer. Calling this in a loop will disable the idle camera.

**Nombres antiguos (alias):** `0x9E4CFFF989258472` (`N_0x9e4cfff989258472`)

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
	while true do
		InvalidateIdleCam()
		InvalidateVehicleIdleCam()
		Wait(1000) --The idle camera activates after 30 second so we don't need to call this per frame
	end
end)
```

---
### IsAimCamActive

`IS_AIM_CAM_ACTIVE` · hash `0x68EDDA28A5976D07` · jhash `0xC24B4F6F` · **Cliente**

```lua
local retval = IsAimCamActive()
```
```c
BOOL IS_AIM_CAM_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsAimCamThirdPersonActive

`_IS_AIM_CAM_THIRD_PERSON_ACTIVE` · hash `0x74BD83EA840F6BC9` · jhash `0x8F320DE4` · **Cliente**

```lua
local retval = IsAimCamThirdPersonActive()
```
```c
BOOL _IS_AIM_CAM_THIRD_PERSON_ACTIVE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_A*
```

**Nombres antiguos (alias):** `0x74BD83EA840F6BC9` (`N_0x74bd83ea840f6bc9`)

---
### IsAllowedIndependentCameraModes

`IS_ALLOWED_INDEPENDENT_CAMERA_MODES` · hash `0xEAF0FA793D05C592` · **Cliente**

```lua
local retval = IsAllowedIndependentCameraModes()
```
```c
BOOL IS_ALLOWED_INDEPENDENT_CAMERA_MODES();
```

**Devuelve:** `BOOL` — Returns if the "Allow Independent Camera Modes" setting in Pause Menu is turned On or Off.

**Nombres antiguos (alias):** `0xEAF0FA793D05C592` (`N_0xeaf0fa793d05c592`)

---
### IsBonnetCinematicCamRendering

`IS_BONNET_CINEMATIC_CAM_RENDERING` · hash `0xD7360051C885628B` · jhash `0x1DD55F13` · **Cliente**

```lua
local retval = IsBonnetCinematicCamRendering()
```
```c
BOOL IS_BONNET_CINEMATIC_CAM_RENDERING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD7360051C885628B` (`N_0xd7360051c885628b`)

---
### IsCamActive

`IS_CAM_ACTIVE` · hash `0xDFB2B516207D3534` · jhash `0x4B58F177` · **Cliente**

```lua
local retval = IsCamActive(cam)
```
```c
BOOL IS_CAM_ACTIVE(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether or not the passed camera handle is active.  
```

---
### IsCamInterpolating

`IS_CAM_INTERPOLATING` · hash `0x036F97C908C2B52C` · jhash `0x7159CB5D` · **Cliente**

```lua
local retval = IsCamInterpolating(cam)
```
```c
BOOL IS_CAM_INTERPOLATING(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `BOOL`

---
### IsCamPlayingAnim

`IS_CAM_PLAYING_ANIM` · hash `0xC90621D8A0CEECF2` · jhash `0xB998CB49` · **Cliente**

```lua
local retval = IsCamPlayingAnim(cam, animName, animDictionary)
```
```c
BOOL IS_CAM_PLAYING_ANIM(Cam cam, char* animName, char* animDictionary);
```

**Parámetros**

- `cam` (`Cam`)
- `animName` (`char*`)
- `animDictionary` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

[Animations list](https://alexguirre.github.io/animations-list/)

---
### IsCamRendering

`IS_CAM_RENDERING` · hash `0x02EC0AF5C5A49B7A` · jhash `0x6EC6B5B2` · **Cliente**

```lua
local retval = IsCamRendering(cam)
```
```c
BOOL IS_CAM_RENDERING(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `BOOL`

---
### IsCamShaking

`IS_CAM_SHAKING` · hash `0x6B24BFE83A2BE47B` · jhash `0x0961FD9B` · **Cliente**

```lua
local retval = IsCamShaking(cam)
```
```c
BOOL IS_CAM_SHAKING(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `BOOL`

---
### IsCamSplinePaused

`IS_CAM_SPLINE_PAUSED` · hash `0x0290F35C0AD97864` · jhash `0x60B34FF5` · **Cliente**

```lua
local retval = IsCamSplinePaused(p0)
```
```c
BOOL IS_CAM_SPLINE_PAUSED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### IsCinematicCamInputActive

`IS_CINEMATIC_CAM_INPUT_ACTIVE` · hash `0xF5F1E89A970B7796` · jhash `0x01A900C8` · **Cliente**

```lua
local retval = IsCinematicCamInputActive()
```
```c
BOOL IS_CINEMATIC_CAM_INPUT_ACTIVE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0xF5F1E89A970B7796` (`N_0xf5f1e89a970b7796`), `_IS_CINEMATIC_CAM_ACTIVE` (`IsCinematicCamActive`)

---
### IsCinematicCamRendering

`IS_CINEMATIC_CAM_RENDERING` · hash `0xB15162CB5826E9E8` · jhash `0x80471AD9` · **Cliente**

```lua
local retval = IsCinematicCamRendering()
```
```c
BOOL IS_CINEMATIC_CAM_RENDERING();
```

**Devuelve:** `BOOL`

---
### IsCinematicCamShaking

`IS_CINEMATIC_CAM_SHAKING` · hash `0xBBC08F6B4CB8FF0A` · jhash `0x8376D939` · **Cliente**

```lua
local retval = IsCinematicCamShaking()
```
```c
BOOL IS_CINEMATIC_CAM_SHAKING();
```

**Devuelve:** `BOOL`

---
### IsCinematicIdleCamRendering

`IS_CINEMATIC_IDLE_CAM_RENDERING` · hash `0xCA9D2AA3E326D720` · jhash `0x96A07066` · **Cliente**

```lua
local retval = IsCinematicIdleCamRendering()
```
```c
BOOL IS_CINEMATIC_IDLE_CAM_RENDERING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xCA9D2AA3E326D720` (`N_0xca9d2aa3e326d720`)

---
### IsCinematicShotActive

`IS_CINEMATIC_SHOT_ACTIVE` · hash `0xCC9F3371A7C28BC9` · jhash `0xA4049042` · **Cliente**

```lua
local retval = IsCinematicShotActive(p0)
```
```c
BOOL IS_CINEMATIC_SHOT_ACTIVE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### IsFirstPersonAimCamActive

`IS_FIRST_PERSON_AIM_CAM_ACTIVE` · hash `0x5E346D934122613F` · jhash `0xD6280468` · **Cliente**

```lua
local retval = IsFirstPersonAimCamActive()
```
```c
BOOL IS_FIRST_PERSON_AIM_CAM_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsFollowPedCamActive

`IS_FOLLOW_PED_CAM_ACTIVE` · hash `0xC6D3D26810C8E0F9` · jhash `0x9F9E856C` · **Cliente**

```lua
local retval = IsFollowPedCamActive()
```
```c
BOOL IS_FOLLOW_PED_CAM_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsFollowVehicleCamActive

`IS_FOLLOW_VEHICLE_CAM_ACTIVE` · hash `0xCBBDE6D335D6D496` · jhash `0x8DD49B77` · **Cliente**

```lua
local retval = IsFollowVehicleCamActive()
```
```c
BOOL IS_FOLLOW_VEHICLE_CAM_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsGameplayCamLookingBehind

`IS_GAMEPLAY_CAM_LOOKING_BEHIND` · hash `0x70FDA869F3317EA9` · jhash `0x33C83F17` · **Cliente**

```lua
local retval = IsGameplayCamLookingBehind()
```
```c
BOOL IS_GAMEPLAY_CAM_LOOKING_BEHIND();
```

**Devuelve:** `BOOL`

---
### IsGameplayCamRendering

`IS_GAMEPLAY_CAM_RENDERING` · hash `0x39B5D1B10383F0C8` · jhash `0x0EF276DA` · **Cliente**

```lua
local retval = IsGameplayCamRendering()
```
```c
BOOL IS_GAMEPLAY_CAM_RENDERING();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Examples when this function will return 0 are:
- During busted screen.
- When player is coming out from a hospital.
- When player is coming out from a police station.
- When player is buying gun from AmmuNation.
```

---
### IsGameplayCamShaking

`IS_GAMEPLAY_CAM_SHAKING` · hash `0x016C090630DF1F89` · jhash `0x3457D681` · **Cliente**

```lua
local retval = IsGameplayCamShaking()
```
```c
BOOL IS_GAMEPLAY_CAM_SHAKING();
```

**Devuelve:** `BOOL`

---
### IsGameplayHintActive

`IS_GAMEPLAY_HINT_ACTIVE` · hash `0xE520FF1AD2785B40` · jhash `0xAD8DA205` · **Cliente**

```lua
local retval = IsGameplayHintActive()
```
```c
BOOL IS_GAMEPLAY_HINT_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsInVehicleCamDisabled

`_IS_IN_VEHICLE_CAM_DISABLED` · hash `0x4F32C0D5A90A9B40` · **Cliente**

```lua
local retval = IsInVehicleCamDisabled()
```
```c
BOOL _IS_IN_VEHICLE_CAM_DISABLED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4F32C0D5A90A9B40` (`N_0x4f32c0d5a90a9b40`)

---
### IsScreenFadedIn

`IS_SCREEN_FADED_IN` · hash `0x5A859503B0C08678` · jhash `0x4F37276D` · **Cliente**

```lua
local retval = IsScreenFadedIn()
```
```c
BOOL IS_SCREEN_FADED_IN();
```

**Devuelve:** `BOOL`

---
### IsScreenFadedOut

`IS_SCREEN_FADED_OUT` · hash `0xB16FCE9DDC7BA182` · jhash `0x9CAA05FA` · **Cliente**

```lua
local retval = IsScreenFadedOut()
```
```c
BOOL IS_SCREEN_FADED_OUT();
```

**Devuelve:** `BOOL`

---
### IsScreenFadingIn

`IS_SCREEN_FADING_IN` · hash `0x5C544BC6C57AC575` · jhash `0xC7C82800` · **Cliente**

```lua
local retval = IsScreenFadingIn()
```
```c
BOOL IS_SCREEN_FADING_IN();
```

**Devuelve:** `BOOL`

---
### IsScreenFadingOut

`IS_SCREEN_FADING_OUT` · hash `0x797AC7CB535BA28F` · jhash `0x79275A57` · **Cliente**

```lua
local retval = IsScreenFadingOut()
```
```c
BOOL IS_SCREEN_FADING_OUT();
```

**Devuelve:** `BOOL`

---
### IsScriptGlobalShaking

`IS_SCRIPT_GLOBAL_SHAKING` · hash `0xC912AF078AF19212` · jhash `0x6AEFE6A5` · **Cliente**

```lua
local retval = IsScriptGlobalShaking()
```
```c
BOOL IS_SCRIPT_GLOBAL_SHAKING();
```

**Devuelve:** `BOOL` — Returns `true` if a scripted global camera shake is currently in effect, otherwise `false`.

**Descripción oficial:**

Determines if a global camera shake is currently active. You can stop the currently active global camera shake using [STOP_SCRIPT_GLOBAL_SHAKING](#stopscriptglobalshaking).

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xC912AF078AF19212` (`N_0xc912af078af19212`)

**Ejemplo (lua):**

```lua
-- Print whether a global camera shake is currently active
print(IsScriptGlobalShaking())
```

**Ejemplo (js):**

```js
// Print whether a global camera shake is currently active
console.log(IsScriptGlobalShaking());
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Print whether a global camera shake is currently active
Debug.WriteLine(IsScriptGlobalShaking());
```

---
### IsSphereVisible

`IS_SPHERE_VISIBLE` · hash `0xE33D59DA70B58FDF` · jhash `0xDD1329E2` · **Cliente**

```lua
local retval = IsSphereVisible(x, y, z, radius)
```
```c
BOOL IS_SPHERE_VISIBLE(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

---
### N_0x0225778816fdc28c

`0x0225778816FDC28C` · hash `0x0225778816FDC28C` · jhash `0x1126E37C` · **Cliente**

```lua
N_0x0225778816fdc28c(p0)
```
```c
void 0x0225778816FDC28C(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
some camera effect that is (also) used in the drunk-cheat, and turned off (by setting it to 0.0) along with the shaking effects once the drunk cheat is disabled. Possibly a cinematic or script-cam version of _0x487A82C650EB7799  
```

---
### N_0x0aa27680a0bd43fa

`0x0AA27680A0BD43FA` · hash `0x0AA27680A0BD43FA` · **Cliente**

```lua
N_0x0aa27680a0bd43fa()
```
```c
void 0x0AA27680A0BD43FA();
```

**Devuelve:** `void`

---
### N_0x12ded8ca53d47ea5

`0x12DED8CA53D47EA5` · hash `0x12DED8CA53D47EA5` · jhash `0x067BA6F5` · **Cliente**

```lua
N_0x12ded8ca53d47ea5(p0)
```
```c
void 0x12DED8CA53D47EA5(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Hardcoded to only work in multiplayer.  
```

---
### N_0x17fca7199a530203

`0x17FCA7199A530203` · hash `0x17FCA7199A530203` · jhash `0xF26E339C` · **Cliente**

```lua
N_0x17fca7199a530203()
```
```c
void 0x17FCA7199A530203();
```

**Devuelve:** `void`

---
### N_0x1f2300cb7fa7b7f6

`0x1F2300CB7FA7B7F6` · hash `0x1F2300CB7FA7B7F6` · jhash `0x6739AD55` · **Cliente**

```lua
local retval = N_0x1f2300cb7fa7b7f6()
```
```c
Any 0x1F2300CB7FA7B7F6();
```

**Devuelve:** `Any`

---
### N_0x247acbc4abbc9d1c

`0x247ACBC4ABBC9D1C` · hash `0x247ACBC4ABBC9D1C` · **Cliente**

```lua
N_0x247acbc4abbc9d1c(p0)
```
```c
void 0x247ACBC4ABBC9D1C(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x271017b9ba825366

`0x271017B9BA825366` · hash `0x271017B9BA825366` · jhash `0x43220969` · **Cliente**

```lua
N_0x271017b9ba825366(p0, p1)
```
```c
void 0x271017B9BA825366(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x28b022a17b068a3a

`0x28B022A17B068A3A` · hash `0x28B022A17B068A3A` · **Cliente**

```lua
N_0x28b022a17b068a3a(p0, p1)
```
```c
void 0x28B022A17B068A3A(float p0, float p1);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

F\*

```
NativeDB Introduced: v1734
```

---
### N_0x2f7f2b26dd3f18ee

`0x2F7F2B26DD3F18EE` · hash `0x2F7F2B26DD3F18EE` · jhash `0x2F29F0D5` · **Cliente**

```lua
N_0x2f7f2b26dd3f18ee(p0, p1)
```
```c
void 0x2F7F2B26DD3F18EE(float p0, float p1);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0x3044240d2e0fa842

`0x3044240D2E0FA842` · hash `0x3044240D2E0FA842` · jhash `0xC0B00C20` · **Cliente**

```lua
local retval = N_0x3044240d2e0fa842()
```
```c
BOOL 0x3044240D2E0FA842();
```

**Devuelve:** `BOOL`

---
### N_0x324c5aa411da7737

`0x324C5AA411DA7737` · hash `0x324C5AA411DA7737` · **Cliente**

```lua
N_0x324c5aa411da7737(p0)
```
```c
void 0x324C5AA411DA7737(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### N_0x380b4968d1e09e55

`0x380B4968D1E09E55` · hash `0x380B4968D1E09E55` · **Cliente**

```lua
N_0x380b4968d1e09e55()
```
```c
void 0x380B4968D1E09E55();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x4008edf7d6e48175

`0x4008EDF7D6E48175` · hash `0x4008EDF7D6E48175` · jhash `0xD1EEBC45` · **Cliente**

```lua
N_0x4008edf7d6e48175(p0)
```
```c
void 0x4008EDF7D6E48175(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x469f2ecdec046337

`0x469F2ECDEC046337` · hash `0x469F2ECDEC046337` · **Cliente**

```lua
N_0x469f2ecdec046337(p0)
```
```c
void 0x469F2ECDEC046337(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x4879e4fe39074cdf

`0x4879E4FE39074CDF` · hash `0x4879E4FE39074CDF` · **Cliente**

```lua
local retval = N_0x4879e4fe39074cdf()
```
```c
BOOL 0x4879E4FE39074CDF();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
A*
```

---
### N_0x59424bd75174c9b1

`0x59424BD75174C9B1` · hash `0x59424BD75174C9B1` · **Cliente**

```lua
N_0x59424bd75174c9b1()
```
```c
void 0x59424BD75174C9B1();
```

**Devuelve:** `void`

---
### N_0x5a43c76f7fc7ba5f

`0x5A43C76F7FC7BA5F` · hash `0x5A43C76F7FC7BA5F` · jhash `0xE206C450` · **Cliente**

```lua
N_0x5a43c76f7fc7ba5f()
```
```c
void 0x5A43C76F7FC7BA5F();
```

**Devuelve:** `void`

---
### N_0x5c41e6babc9e2112

`0x5C41E6BABC9E2112` · hash `0x5C41E6BABC9E2112` · **Cliente**

```lua
N_0x5c41e6babc9e2112(p0)
```
```c
void 0x5C41E6BABC9E2112(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x5c48a1d6e3b33179

`0x5C48A1D6E3B33179` · hash `0x5C48A1D6E3B33179` · jhash `0xDA931D65` · **Cliente**

```lua
local retval = N_0x5c48a1d6e3b33179(cam)
```
```c
BOOL 0x5C48A1D6E3B33179(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
W*
```

---
### N_0x5d96cfb59da076a0

`0x5D96CFB59DA076A0` · hash `0x5D96CFB59DA076A0` · **Cliente**

```lua
N_0x5d96cfb59da076a0(vehicle, p1, p2)
```
```c
void 0x5D96CFB59DA076A0(Vehicle vehicle, int p1, float p2);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`int`)
- `p2` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

p1: 0..16

```
NativeDB Introduced: v2060
```

---
### N_0x62374889a4d59f72

`0x62374889A4D59F72` · hash `0x62374889A4D59F72` · **Cliente**

```lua
N_0x62374889a4d59f72()
```
```c
void 0x62374889A4D59F72();
```

**Devuelve:** `void`

---
### N_0x62ecfcfdee7885d6

`0x62ECFCFDEE7885D6` · hash `0x62ECFCFDEE7885D6` · jhash `0x837F8581` · **Cliente**

```lua
N_0x62ecfcfdee7885d6()
```
```c
void 0x62ECFCFDEE7885D6();
```

**Devuelve:** `void`

---
### N_0x705a276ebff3133d

`0x705A276EBFF3133D` · hash `0x705A276EBFF3133D` · jhash `0x60C23785` · **Cliente**

```lua
local retval = N_0x705a276ebff3133d()
```
```c
BOOL 0x705A276EBFF3133D();
```

**Devuelve:** `BOOL`

---
### N_0x7295c203dd659dfe

`0x7295C203DD659DFE` · hash `0x7295C203DD659DFE` · **Cliente**

```lua
N_0x7295c203dd659dfe()
```
```c
void 0x7295C203DD659DFE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
_RESET_*

_RESET_GAMEPLAY_CAM_RELATIVE_ORBIT_HOLD_TIME?
```

```
NativeDB Introduced: v2699
```

---
### N_0x91ef6ee6419e5b97

`0x91EF6EE6419E5B97` · hash `0x91EF6EE6419E5B97` · jhash `0x9DB5D391` · **Cliente**

```lua
N_0x91ef6ee6419e5b97(p0)
```
```c
void 0x91EF6EE6419E5B97(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x9dfe13ecdc1ec196

`0x9DFE13ECDC1EC196` · hash `0x9DFE13ECDC1EC196` · jhash `0x92302899` · **Cliente**

```lua
N_0x9dfe13ecdc1ec196(p0, p1)
```
```c
void 0x9DFE13ECDC1EC196(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_FOLLOW_*
```

**Nombres antiguos (alias):** `SET_TIME_IDLE_DROP` (`SetTimeIdleDrop`)

---
### N_0x9f97da93681f87ea

`0x9F97DA93681F87EA` · hash `0x9F97DA93681F87EA` · **Cliente**

```lua
N_0x9f97da93681f87ea()
```
```c
void 0x9F97DA93681F87EA();
```

**Devuelve:** `void`

**Descripción oficial:**

B\*

```
NativeDB Introduced: v1734
```

---
### N_0xa2767257a320fc82

`0xA2767257A320FC82` · hash `0xA2767257A320FC82` · **Cliente**

```lua
N_0xa2767257a320fc82(p0, p1)
```
```c
void 0xA2767257A320FC82(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0xa7092afe81944852

`0xA7092AFE81944852` · hash `0xA7092AFE81944852` · **Cliente**

```lua
N_0xa7092afe81944852()
```
```c
void 0xA7092AFE81944852();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xaabd62873ffb1a33

`0xAABD62873FFB1A33` · hash `0xAABD62873FFB1A33` · **Cliente**

```lua
N_0xaabd62873ffb1a33(p0, p1)
```
```c
void 0xAABD62873FFB1A33(Any p0, Any p1);
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
### N_0xb1381b97f70c7b30

`0xB1381B97F70C7B30` · hash `0xB1381B97F70C7B30` · **Cliente**

```lua
N_0xb1381b97f70c7b30()
```
```c
void 0xB1381B97F70C7B30();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

---
### N_0xbf72910d0f26f025

`0xBF72910D0F26F025` · hash `0xBF72910D0F26F025` · **Cliente**

```lua
local retval = N_0xbf72910d0f26f025()
```
```c
Any 0xBF72910D0F26F025();
```

**Devuelve:** `Any`

---
### N_0xc8391c309684595a

`0xC8391C309684595A` · hash `0xC8391C309684595A` · jhash `0x1F9DE6E4` · **Cliente**

```lua
N_0xc8391c309684595a()
```
```c
void 0xC8391C309684595A();
```

**Devuelve:** `void`

---
### N_0xc8b5c4a79cc18b94

`0xC8B5C4A79CC18B94` · hash `0xC8B5C4A79CC18B94` · jhash `0x44473EFC` · **Cliente**

```lua
N_0xc8b5c4a79cc18b94(cam)
```
```c
void 0xC8B5C4A79CC18B94(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `void`

---
### N_0xccd078c2665d2973

`0xCCD078C2665D2973` · hash `0xCCD078C2665D2973` · jhash `0xCAFEE798` · **Cliente**

```lua
N_0xccd078c2665d2973(p0)
```
```c
void 0xCCD078C2665D2973(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xced08cbe8ebb97c7

`0xCED08CBE8EBB97C7` · hash `0xCED08CBE8EBB97C7` · jhash `0x68BA0730` · **Cliente**

```lua
N_0xced08cbe8ebb97c7(p0, p1)
```
```c
void 0xCED08CBE8EBB97C7(float p0, float p1);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0xdb90c6cca48940f1

`0xDB90C6CCA48940F1` · hash `0xDB90C6CCA48940F1` · jhash `0x20BFF6E5` · **Cliente**

```lua
N_0xdb90c6cca48940f1(p0)
```
```c
void 0xDB90C6CCA48940F1(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xdd79df9f4d26e1c9

`0xDD79DF9F4D26E1C9` · hash `0xDD79DF9F4D26E1C9` · jhash `0x6B0E9D57` · **Cliente**

```lua
N_0xdd79df9f4d26e1c9()
```
```c
void 0xDD79DF9F4D26E1C9();
```

**Devuelve:** `void`

---
### N_0xe111a7c0d200cbc5

`0xE111A7C0D200CBC5` · hash `0xE111A7C0D200CBC5` · **Cliente**

```lua
N_0xe111a7c0d200cbc5(p0, p1)
```
```c
void 0xE111A7C0D200CBC5(Any p0, float p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0xf55e4046f6f831dc

`0xF55E4046F6F831DC` · hash `0xF55E4046F6F831DC` · **Cliente**

```lua
N_0xf55e4046f6f831dc(p0, p1)
```
```c
void 0xF55E4046F6F831DC(Any p0, float p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0xfd3151cd37ea2245

`0xFD3151CD37EA2245` · hash `0xFD3151CD37EA2245` · **Cliente**

```lua
N_0xfd3151cd37ea2245(entity)
```
```c
void 0xFD3151CD37EA2245(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

---
### OverrideCamSplineMotionBlur

`OVERRIDE_CAM_SPLINE_MOTION_BLUR` · hash `0x7DCF7C708D292D55` · jhash `0x633179E6` · **Cliente**

```lua
OverrideCamSplineMotionBlur(cam, p1, p2, p3)
```
```c
void OVERRIDE_CAM_SPLINE_MOTION_BLUR(Cam cam, int p1, float p2, float p3);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`int`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Max value for p1 is 15.  
```

---
### OverrideCamSplineVelocity

`OVERRIDE_CAM_SPLINE_VELOCITY` · hash `0x40B62FA033EB0346` · jhash `0x326A17E2` · **Cliente**

```lua
OverrideCamSplineVelocity(cam, p1, p2, p3)
```
```c
void OVERRIDE_CAM_SPLINE_VELOCITY(Cam cam, int p1, float p2, float p3);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`int`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### PlayCamAnim

`PLAY_CAM_ANIM` · hash `0x9A2D0FB2E7852392` · jhash `0xBCEFB87E` · **Cliente**

```lua
local retval = PlayCamAnim(cam, animName, animDictionary, x, y, z, xRot, yRot, zRot, p9, p10)
```
```c
BOOL PLAY_CAM_ANIM(Cam cam, char* animName, char* animDictionary, float x, float y, float z, float xRot, float yRot, float zRot, BOOL p9, int p10);
```

**Parámetros**

- `cam` (`Cam`)
- `animName` (`char*`)
- `animDictionary` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `xRot` (`float`)
- `yRot` (`float`)
- `zRot` (`float`)
- `p9` (`BOOL`)
- `p10` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Atleast one time in a script for the zRot Rockstar uses GET_ENTITY_HEADING to help fill the parameter.  
p9 is unknown at this time.  
p10 throughout all the X360 Scripts is always 2.  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### PlaySynchronizedCamAnim

`PLAY_SYNCHRONIZED_CAM_ANIM` · hash `0xE32EFE9AB4A9AA0C` · jhash `0x9458459E` · **Cliente**

```lua
local retval = PlaySynchronizedCamAnim(camera, scene, animName, animDictionary)
```
```c
BOOL PLAY_SYNCHRONIZED_CAM_ANIM(Cam camera, int scene, char* animName, char* animDictionary);
```

**Parámetros**

- `camera` (`Cam`)
- `scene` (`int`)
- `animName` (`char*`)
- `animDictionary` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Examples:  
CAM::PLAY_SYNCHRONIZED_CAM_ANIM(l_2734, NETWORK::_02C40BF885C567B6(l_2739), "PLAYER_EXIT_L_CAM", "mp_doorbell");  
CAM::PLAY_SYNCHRONIZED_CAM_ANIM(l_F0D[7/*1*/], l_F4D[15/*1*/], "ah3b_attackheli_cam2", "missheistfbi3b_helicrash");  
```

[Animations list](https://alexguirre.github.io/animations-list/)

---
### PointCamAtCoord

`POINT_CAM_AT_COORD` · hash `0xF75497BB865F0803` · jhash `0x914BC21A` · **Cliente**

```lua
PointCamAtCoord(cam, x, y, z)
```
```c
void POINT_CAM_AT_COORD(Cam cam, float x, float y, float z);
```

**Parámetros**

- `cam` (`Cam`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
local coords = vector3(402.99, -998.02, -99.00)
local cam = CreateCamWithParams("DEFAULT_SCRIPTED_CAMERA", coords.x, coords.y, coords.z, 0.00, 0.00, 0.00, 50.00, false, 0)
PointCamAtCoord(cam, coords.x, coords.y, coords.z)
```

---
### PointCamAtEntity

`POINT_CAM_AT_ENTITY` · hash `0x5640BFF86B16E8DC` · jhash `0x7597A0F7` · **Cliente**

```lua
PointCamAtEntity(cam, entity, offsetX, offsetY, offsetZ, p5)
```
```c
void POINT_CAM_AT_ENTITY(Cam cam, Entity entity, float offsetX, float offsetY, float offsetZ, BOOL p5);
```

**Parámetros**

- `cam` (`Cam`): Cam (Return value of CREATE_CAM or CREATE_CAM_WITH_PARAMS).
- `entity` (`Entity`): Entity for the camera to point at.
- `offsetX` (`float`): X offset for the camera (left/right).
- `offsetY` (`float`): Y offset for the camera (forward/backward).
- `offsetZ` (`float`): Z offset for the camera (up/down).
- `p5` (`BOOL`): Always seems to be 1 (true).

**Devuelve:** `void`

**Descripción oficial:**

Points the camera at the specified entity.

Offset works like [GET_OFFSET_FROM_ENTITY_IN_WORLD_COORDS](ENTITY.md#getoffsetfromentityinworldcoords).

**Ejemplo (lua):**

```lua
local cam = CreateCameraWithParams("DEFAULT_SCRIPTED_CAMERA", GetEntityCoords(PlayerPedId()), 0.0, 0.0, 0.0, 90.0, true, 2)
PointCamAtEntity(cam, PlayerPedId(), 0.0, 0.0, 0.0, true)
RenderScriptCams(true, false, 0, true, true)
```

---
### PointCamAtPedBone

`POINT_CAM_AT_PED_BONE` · hash `0x68B2B5F33BA63C41` · jhash `0x09F47049` · **Cliente**

```lua
PointCamAtPedBone(cam, ped, boneIndex, x, y, z, p6)
```
```c
void POINT_CAM_AT_PED_BONE(Cam cam, Ped ped, int boneIndex, float x, float y, float z, BOOL p6);
```

**Parámetros**

- `cam` (`Cam`)
- `ped` (`Ped`)
- `boneIndex` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p6` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Parameters p0-p5 seems correct. The bool p6 is unknown, but through every X360 script it's always 1. Please correct p0-p5 if any prove to be wrong.  
```

---
### RenderScriptCams

`RENDER_SCRIPT_CAMS` · hash `0x07E5B515DB0636FC` · jhash `0x74337969` · **Cliente**

```lua
RenderScriptCams(render, ease, easeTime, easeCoordsAnim, p4)
```
```c
void RENDER_SCRIPT_CAMS(BOOL render, BOOL ease, int easeTime, BOOL easeCoordsAnim, BOOL p4);
```

**Parámetros**

- `render` (`BOOL`): Whether to render the cams or not.
- `ease` (`BOOL`): If true it will make a smooth transition between the current camera and the new rendered camera.
- `easeTime` (`int`): The in milliseconds for the transition to happen.
- `easeCoordsAnim` (`BOOL`): If false it will only do the smooth transition to the rotation and the coords will be set instantly.
- `p4` (`BOOL`): Doesn't seem to change anything.

**Devuelve:** `void`

**Descripción oficial:**

Renders the camera previously created with [CREATE_CAM](#createcam) or [CREATE_CAMERA](#createcamera)

```
NativeDB Added Parameter 6: Any p5
```

**Ejemplo (lua):**

```lua
local casino = vector3(881.31, 74.71, 94.43)

-- Create the camera that will be used for RenderScriptCams
local cam = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)
-- Set the camera coordinates to be in front of the Casino
SetCamCoord(cam, casino.x, casino.y, casino.z)
-- Rotate the camera towards the casino
SetCamRot(cam, -25.0, 0.0, -124.22)

-- Render the camera and so a smooth transition for 2000ms
RenderScriptCams(true, true, 2000, false, true)

-- tell the game to load maps, collisions, objects, etc around the casino.
SetFocusPosAndVel(casino.x, casino.y, casino.z, 0.0, 0.0, 0.0)

 -- We wait 5 seconds + 2 extra for the transition
Wait(7000)
-- Remove the cam, we no longer need it
DestroyCam(cam) 

-- reset streaming focus to be at the local player ped
ClearFocus()
-- Stop rendering the script camera and interpolate back to their player ped
RenderScriptCams(false, true, 2000, false, false)
```

---
### ReplayFreeCamGetMaxRange

`_REPLAY_FREE_CAM_GET_MAX_RANGE` · hash `0x8BFCEB5EA1B161B6` · **Cliente**

```lua
local retval = ReplayFreeCamGetMaxRange()
```
```c
float _REPLAY_FREE_CAM_GET_MAX_RANGE();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x8BFCEB5EA1B161B6` (`N_0x8bfceb5ea1b161b6`)

---
### SetCamActive

`SET_CAM_ACTIVE` · hash `0x026FB97D0A425F84` · jhash `0x064659C2` · **Cliente**

```lua
SetCamActive(cam, active)
```
```c
void SET_CAM_ACTIVE(Cam cam, BOOL active);
```

**Parámetros**

- `cam` (`Cam`)
- `active` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Set camera as active/inactive.  
```

---
### SetCamActiveWithInterp

`SET_CAM_ACTIVE_WITH_INTERP` · hash `0x9FBDA379383A52A4` · jhash `0x7983E7F0` · **Cliente**

```lua
SetCamActiveWithInterp(camTo, camFrom, duration, easeLocation, easeRotation)
```
```c
void SET_CAM_ACTIVE_WITH_INTERP(Cam camTo, Cam camFrom, int duration, int easeLocation, int easeRotation);
```

**Parámetros**

- `camTo` (`Cam`)
- `camFrom` (`Cam`)
- `duration` (`int`)
- `easeLocation` (`int`)
- `easeRotation` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Previous declaration void SET_CAM_ACTIVE_WITH_INTERP(Cam camTo, Cam camFrom, int duration, BOOL easeLocation, BOOL easeRotation) is completely wrong. The last two params are integers not BOOLs...  
```

---
### SetCamAffectsAiming

`SET_CAM_AFFECTS_AIMING` · hash `0x8C1DC7770C51DC8D` · jhash `0x0C74F9AF` · **Cliente**

```lua
SetCamAffectsAiming(cam, toggle)
```
```c
void SET_CAM_AFFECTS_AIMING(Cam cam, BOOL toggle);
```

**Parámetros**

- `cam` (`Cam`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Allows you to aim and shoot at the direction the camera is facing.  
```

---
### SetCamAnimCurrentPhase

`SET_CAM_ANIM_CURRENT_PHASE` · hash `0x4145A4C44FF3B5A6` · jhash `0x3CB1D17F` · **Cliente**

```lua
SetCamAnimCurrentPhase(cam, phase)
```
```c
void SET_CAM_ANIM_CURRENT_PHASE(Cam cam, float phase);
```

**Parámetros**

- `cam` (`Cam`)
- `phase` (`float`)

**Devuelve:** `void`

---
### SetCamControlsMiniMapHeading

`SET_CAM_CONTROLS_MINI_MAP_HEADING` · hash `0x661B5C8654ADD825` · jhash `0xE1A0B2F1` · **Cliente**

```lua
SetCamControlsMiniMapHeading(cam, toggle)
```
```c
void SET_CAM_CONTROLS_MINI_MAP_HEADING(Cam cam, BOOL toggle);
```

**Parámetros**

- `cam` (`Cam`): Cam handle returned by [CREATE_CAM](#createcam)
- `toggle` (`BOOL`): Whether or not this camera should control the minimap heading.

**Devuelve:** `void`

**Descripción oficial:**

Makes the minimap follow a scripted camera's rotation instead of the gameplay cam.

**Nombres antiguos (alias):** `0x661B5C8654ADD825` (`N_0x661b5c8654add825`)

---
### SetCamCoord

`SET_CAM_COORD` · hash `0x4D41783FB745E42E` · jhash `0x7A8053AF` · **Cliente**

```lua
SetCamCoord(cam, posX, posY, posZ)
```
```c
void SET_CAM_COORD(Cam cam, float posX, float posY, float posZ);
```

**Parámetros**

- `cam` (`Cam`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the position of the cam.  
```

---
### SetCamDebugName

`SET_CAM_DEBUG_NAME` · hash `0x1B93E0107865DD40` · jhash `0x9B00DF3F` · **Cliente**

```lua
SetCamDebugName(camera, name)
```
```c
void SET_CAM_DEBUG_NAME(Cam camera, char* name);
```

**Parámetros**

- `camera` (`Cam`)
- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
NOTE: Debugging functions are not present in the retail version of the game.  
```

---
### SetCamDofFnumberOfLens

`_SET_CAM_DOF_FNUMBER_OF_LENS` · hash `0x7DD234D6F3914C5B` · **Cliente**

```lua
SetCamDofFnumberOfLens(camera, p1)
```
```c
void _SET_CAM_DOF_FNUMBER_OF_LENS(Cam camera, float p1);
```

**Parámetros**

- `camera` (`Cam`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native has its name defined inside its codE  
```

**Nombres antiguos (alias):** `0x7DD234D6F3914C5B` (`N_0x7dd234d6f3914c5b`)

---
### SetCamDofFocalLengthMultiplier

`_SET_CAM_DOF_FOCAL_LENGTH_MULTIPLIER` · hash `0x47B595D60664CFFA` · **Cliente**

```lua
SetCamDofFocalLengthMultiplier(camera, multiplier)
```
```c
void _SET_CAM_DOF_FOCAL_LENGTH_MULTIPLIER(Cam camera, float multiplier);
```

**Parámetros**

- `camera` (`Cam`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Native name labeled within its code
```

**Nombres antiguos (alias):** `0x47B595D60664CFFA` (`N_0x47b595d60664cffa`)

---
### SetCamDofFocusDistanceBias

`_SET_CAM_DOF_FOCUS_DISTANCE_BIAS` · hash `0xC669EEA5D031B7DE` · **Cliente**

```lua
SetCamDofFocusDistanceBias(camera, p1)
```
```c
void _SET_CAM_DOF_FOCUS_DISTANCE_BIAS(Cam camera, float p1);
```

**Parámetros**

- `camera` (`Cam`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native has a name defined inside its code  
```

**Nombres antiguos (alias):** `0xC669EEA5D031B7DE` (`N_0xc669eea5d031b7de`)

---
### SetCamDofMaxNearInFocusDistance

`_SET_CAM_DOF_MAX_NEAR_IN_FOCUS_DISTANCE` · hash `0xC3654A441402562D` · **Cliente**

```lua
SetCamDofMaxNearInFocusDistance(camera, p1)
```
```c
void _SET_CAM_DOF_MAX_NEAR_IN_FOCUS_DISTANCE(Cam camera, float p1);
```

**Parámetros**

- `camera` (`Cam`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native has a name defined inside its code  
```

**Nombres antiguos (alias):** `0xC3654A441402562D` (`N_0xc3654a441402562d`)

---
### SetCamDofMaxNearInFocusDistanceBlendLevel

`_SET_CAM_DOF_MAX_NEAR_IN_FOCUS_DISTANCE_BLEND_LEVEL` · hash `0x2C654B4943BDDF7C` · **Cliente**

```lua
SetCamDofMaxNearInFocusDistanceBlendLevel(camera, p1)
```
```c
void _SET_CAM_DOF_MAX_NEAR_IN_FOCUS_DISTANCE_BLEND_LEVEL(Cam camera, float p1);
```

**Parámetros**

- `camera` (`Cam`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This native has a name defined inside its code  
```

**Nombres antiguos (alias):** `0x2C654B4943BDDF7C` (`N_0x2c654b4943bddf7c`)

---
### SetCamDofPlanes

`SET_CAM_DOF_PLANES` · hash `0x3CF48F6F96E749DC` · jhash `0xAD6C2B8F` · **Cliente**

```lua
SetCamDofPlanes(cam, p1, p2, p3, p4)
```
```c
void SET_CAM_DOF_PLANES(Cam cam, float p1, float p2, float p3, float p4);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)

**Devuelve:** `void`

---
### SetCamDofStrength

`SET_CAM_DOF_STRENGTH` · hash `0x5EE29B4D7D5DF897` · jhash `0x3CC4EB3F` · **Cliente**

```lua
SetCamDofStrength(cam, dofStrength)
```
```c
void SET_CAM_DOF_STRENGTH(Cam cam, float dofStrength);
```

**Parámetros**

- `cam` (`Cam`): The camera handle
- `dofStrength` (`float`): Depth of Field strength (between 0.0 and 1.0)

**Devuelve:** `void`

**Descripción oficial:**

Specifies how much the DoF effect should be applied (Set using [`SET_CAM_NEAR_DOF`](#setcamneardof), [`SET_CAM_FAR_DOF`](#setcamfardof), etc.)

**Ejemplo (lua):**

```lua
CreateThread(function()
    local camera = CreateCam("DEFAULT_SCRIPTED_FLY_CAMERA", true)
    -- Set the cam coordinates to the player coords
    local playerCoords = GetEntityCoords(PlayerPedId())
    SetCamCoord(camera, playerCoords)
    -- Render the camera we just created
    RenderScriptCams(true)
    -- Use a shallow depth of field
    SetCamUseShallowDofMode(camera, true)
    -- Set at what distance your camera should start to focus (Example: 0.7 meters)
    SetCamNearDof(camera, 0.7)
    -- Set at what distance your camera should stop focusing (Example: 1.3 meters)
    SetCamFarDof(camera, 1.3)
    -- Apply 100% of the DoF effect (The native you're reading documentation on)
    SetCamDofStrength(camera, 1.0)

    while DoesCamExist(camera) do
        -- Use DoF effect (needs to be called every tick)
        SetUseHiDof()
        Citizen.Wait(0)  
    end
end)
```

---
### SetCamEffect

`_SET_CAM_EFFECT` · hash `0x80C8B1846639BB19` · jhash `0xB06CCD38` · **Cliente**

```lua
SetCamEffect(p0)
```
```c
void _SET_CAM_EFFECT(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
if p0 is 0, effect is cancelled  
if p0 is 1, effect zooms in, gradually tilts cam clockwise apx 30 degrees, wobbles slowly. Motion blur is active until cancelled.  
if p0 is 2, effect immediately tilts cam clockwise apx 30 degrees, begins to wobble slowly, then gradually tilts cam back to normal. The wobbling will continue until the effect is cancelled.  
```

---
### SetCamFarClip

`SET_CAM_FAR_CLIP` · hash `0xAE306F2A904BF86E` · jhash `0x0D23E381` · **Cliente**

```lua
SetCamFarClip(cam, farClip)
```
```c
void SET_CAM_FAR_CLIP(Cam cam, float farClip);
```

**Parámetros**

- `cam` (`Cam`)
- `farClip` (`float`)

**Devuelve:** `void`

---
### SetCamFarDof

`SET_CAM_FAR_DOF` · hash `0xEDD91296CD01AEE0` · jhash `0x58515E8E` · **Cliente**

```lua
SetCamFarDof(cam, farDOF)
```
```c
void SET_CAM_FAR_DOF(Cam cam, float farDOF);
```

**Parámetros**

- `cam` (`Cam`): The camera handle
- `farDOF` (`float`): Distance in in standard units

**Devuelve:** `void`

**Descripción oficial:**

Specifies when the camera should stop being in focus. Can be used together with [`SET_USE_HI_DOF`](#setusehidof), [`SET_CAM_NEAR_DOF`](#setcamneardof), [`SET_CAM_USE_SHALLOW_DOF_MODE`](#setcamuseshallowdofmode), [`SET_CAM_DOF_STRENGTH`](#setcamdofstrength) and other DoF related natives.

**Usage Example**

A usage example for this native can be found in the following native documentation: [`SET_CAM_DOF_STRENGTH`](#setcamdofstrength).

---
### SetCamFov

`SET_CAM_FOV` · hash `0xB13C14F66A00D047` · jhash `0xD3D5D74F` · **Cliente**

```lua
SetCamFov(cam, fieldOfView)
```
```c
void SET_CAM_FOV(Cam cam, float fieldOfView);
```

**Parámetros**

- `cam` (`Cam`): The camera whose FOV is being set.
- `fieldOfView` (`float`): The new FOV value, in degrees. Valid range is from `1.0f` (minimum FOV, for a very narrow view) to `130.0f` (maximum FOV, for a very wide view).

**Devuelve:** `void`

**Descripción oficial:**

Adjusts the field of view (FOV) for a specified camera, allowing for a wider or narrower perspective of the game world. The field of view is measured in degrees and affects how much of the game world is visible at any given moment through the camera.

```
NativeDB Introduced: v323
```

---
### SetCamInheritRollVehicle

`SET_CAM_INHERIT_ROLL_VEHICLE` · hash `0x45F1DE9C34B93AE6` · jhash `0xE4BD5342` · **Cliente**

```lua
SetCamInheritRollVehicle(cam, p1)
```
```c
void SET_CAM_INHERIT_ROLL_VEHICLE(Cam cam, BOOL p1);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
The native seems to only be called once.  
The native is used as so,  
CAM::SET_CAM_INHERIT_ROLL_VEHICLE(l_544, getElem(2, &l_525, 4));  
In the exile1 script.  
```

---
### SetCamMotionBlurStrength

`SET_CAM_MOTION_BLUR_STRENGTH` · hash `0x6F0F77FBA9A8F2E6` · jhash `0xFD6E0D67` · **Cliente**

```lua
SetCamMotionBlurStrength(cam, strength)
```
```c
void SET_CAM_MOTION_BLUR_STRENGTH(Cam cam, float strength);
```

**Parámetros**

- `cam` (`Cam`)
- `strength` (`float`)

**Devuelve:** `void`

---
### SetCamNearClip

`SET_CAM_NEAR_CLIP` · hash `0xC7848EFCCC545182` · jhash `0x46DB13B1` · **Cliente**

```lua
SetCamNearClip(cam, nearClip)
```
```c
void SET_CAM_NEAR_CLIP(Cam cam, float nearClip);
```

**Parámetros**

- `cam` (`Cam`)
- `nearClip` (`float`)

**Devuelve:** `void`

---
### SetCamNearDof

`SET_CAM_NEAR_DOF` · hash `0x3FA4BF0A7AB7DE2C` · jhash `0xF28254DF` · **Cliente**

```lua
SetCamNearDof(cam, nearDOF)
```
```c
void SET_CAM_NEAR_DOF(Cam cam, float nearDOF);
```

**Parámetros**

- `cam` (`Cam`): The camera handle
- `nearDOF` (`float`): Distance in in standard units

**Devuelve:** `void`

**Descripción oficial:**

Specifies when the camera should start being in focus. Can be used together with [`SET_USE_HI_DOF`](#setusehidof), [`SET_CAM_FAR_DOF`](#setcamfardof), [`SET_CAM_USE_SHALLOW_DOF_MODE`](#setcamuseshallowdofmode), [`SET_CAM_DOF_STRENGTH`](#setcamdofstrength) and other DoF related natives.

**Usage Example**

A usage example for this native can be found in the following native documentation: [`SET_CAM_DOF_STRENGTH`](#setcamdofstrength).

---
### SetCamParams

`SET_CAM_PARAMS` · hash `0xBFD8727AEA3CCEBA` · jhash `0x2167CEBF` · **Cliente**

```lua
SetCamParams(cam, posX, posY, posZ, rotX, rotY, rotZ, fieldOfView, transitionSpeed, p9, p10, rotationOrder)
```
```c
void SET_CAM_PARAMS(Cam cam, float posX, float posY, float posZ, float rotX, float rotY, float rotZ, float fieldOfView, int transitionSpeed, int p9, int p10, int rotationOrder);
```

**Parámetros**

- `cam` (`Cam`)
- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `rotX` (`float`)
- `rotY` (`float`)
- `rotZ` (`float`)
- `fieldOfView` (`float`)
- `transitionSpeed` (`int`): The speed of transition/interpolation to these new values
- `p9` (`int`)
- `p10` (`int`)
- `rotationOrder` (`int`): The order of rotation, see [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation)

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
-- This is recreating the above mentioned heli transition from finale_heist2a.c
  local cam = CreateCameraWithParams('DEFAULT_SCRIPTED_CAMERA', -1659.574, -707.8544, 29.23778, -7.422939, 0.059666, -117.3886, 43.0557, false, 2)
SetCamActive(cam, true)
RenderScriptCams(true, false, 3000, true, false, false)
SetCamParams(cam, -1660.919, -710.7487, 28.88381, -7.50235, 0.059666, -111.7328, 43.0557, 9100, 0, 0, 2);
```

**Ejemplo (js):**

```js
// This is recreating the above mentioned heli transition from finale_heist2a.c
let cam = CreateCameraWithParams('DEFAULT_SCRIPTED_CAMERA', -1659.574, -707.8544, 29.23778, -7.422939, 0.059666, -117.3886, 43.0557, false, 2)
SetCamActive(cam, true)
RenderScriptCams(true, false, 3000, true, false, false)
SetCamParams(cam, -1660.919, -710.7487, 28.88381, -7.50235, 0.059666, -111.7328, 43.0557, 9100, 0, 0, 2);
```

---
### SetCamRot

`SET_CAM_ROT` · hash `0x85973643155D0B07` · jhash `0xEE38B3C1` · **Cliente**

```lua
SetCamRot(cam, rotX, rotY, rotZ, rotationOrder)
```
```c
void SET_CAM_ROT(Cam cam, float rotX, float rotY, float rotZ, int rotationOrder);
```

**Parámetros**

- `cam` (`Cam`): The camera handle to use, in order to change the rotation
- `rotX` (`float`): Rotation on X
- `rotY` (`float`): Rotation on Y
- `rotZ` (`float`): Rotation on Z
- `rotationOrder` (`int`): The order of rotation, see [`GET_ENTITY_ROTATION`](../cfx/servidor.md#getentityrotation)

**Devuelve:** `void`

**Descripción oficial:**

Sets the rotation of the camera.

**Ejemplo (lua):**

```lua
-- We need a valid camera handle for this to work.
local theCamHandle = CreateCam("DEFAULT_SCRIPTED_CAMERA", true)
SetCamRot(theCamHandle, 0.1, 0.2, 0.3, 0)
```

---
### SetCamShakeAmplitude

`SET_CAM_SHAKE_AMPLITUDE` · hash `0xD93DB43B82BC0D00` · jhash `0x60FF6382` · **Cliente**

```lua
SetCamShakeAmplitude(cam, amplitude)
```
```c
void SET_CAM_SHAKE_AMPLITUDE(Cam cam, float amplitude);
```

**Parámetros**

- `cam` (`Cam`)
- `amplitude` (`float`)

**Devuelve:** `void`

---
### SetCamSplineDuration

`SET_CAM_SPLINE_DURATION` · hash `0x1381539FEE034CDA` · jhash `0x3E91FC8A` · **Cliente**

```lua
SetCamSplineDuration(cam, timeDuration)
```
```c
void SET_CAM_SPLINE_DURATION(Cam cam, int timeDuration);
```

**Parámetros**

- `cam` (`Cam`)
- `timeDuration` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
I named p1 as timeDuration as it is obvious. I'm assuming tho it is ran in ms(Milliseconds) as usual.  
```

---
### SetCamSplineNodeEase

`SET_CAM_SPLINE_NODE_EASE` · hash `0x83B8201ED82A9A2D` · jhash `0x21D275DA` · **Cliente**

```lua
SetCamSplineNodeEase(cam, p1, p2, p3)
```
```c
void SET_CAM_SPLINE_NODE_EASE(Cam cam, int p1, int p2, float p3);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`int`)
- `p2` (`int`)
- `p3` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x83B8201ED82A9A2D` (`N_0x83b8201ed82a9a2d`)

---
### SetCamSplineNodeExtraFlags

`SET_CAM_SPLINE_NODE_EXTRA_FLAGS` · hash `0x7BF1A54AE67AC070` · jhash `0xC90B2DDC` · **Cliente**

```lua
SetCamSplineNodeExtraFlags(cam, p1, flags)
```
```c
void SET_CAM_SPLINE_NODE_EXTRA_FLAGS(Cam cam, int p1, int flags);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`int`)
- `flags` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7BF1A54AE67AC070` (`N_0x7bf1a54ae67ac070`)

---
### SetCamSplineNodeVelocityScale

`SET_CAM_SPLINE_NODE_VELOCITY_SCALE` · hash `0xA6385DEB180F319F` · jhash `0xA3BD9E94` · **Cliente**

```lua
SetCamSplineNodeVelocityScale(cam, p1, scale)
```
```c
void SET_CAM_SPLINE_NODE_VELOCITY_SCALE(Cam cam, int p1, float scale);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`int`)
- `scale` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA6385DEB180F319F` (`N_0xa6385deb180f319f`)

---
### SetCamSplinePhase

`SET_CAM_SPLINE_PHASE` · hash `0x242B5874F0A4E052` · jhash `0xF0AED233` · **Cliente**

```lua
SetCamSplinePhase(cam, p1)
```
```c
void SET_CAM_SPLINE_PHASE(Cam cam, float p1);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`float`)

**Devuelve:** `void`

---
### SetCamSplineSmoothingStyle

`SET_CAM_SPLINE_SMOOTHING_STYLE` · hash `0xD1B0F412F109EA5D` · jhash `0x15E141CE` · **Cliente**

```lua
SetCamSplineSmoothingStyle(cam, smoothingStyle)
```
```c
void SET_CAM_SPLINE_SMOOTHING_STYLE(Cam cam, int smoothingStyle);
```

**Parámetros**

- `cam` (`Cam`): The DEFAULT_SPLINE_CAMERA to apply the smoothing to
- `smoothingStyle` (`int`): 0 to 3, 0 no additional smoothing, 1 smooth lead-in, 2 smooth lead-out, 3 smooth lead-in & lead-out

**Devuelve:** `void`

**Descripción oficial:**

Sets the smoothing style for a DEFAULT_SPLINE_CAMERA
Ranges from 0 to 3 in rockstar scripts although there are actually 26

```
0: No lead-in or lead-out smoothing
1: Smooth lead-in
2: Smooth lead-out
3: Both lead-in and lead-out are smoothed
4-6: Longer speed up, lead-in, lead-out, and both in order as above. 
6: see above, but missed a node in testing(?)
7: Smoothed lead-in, longer smoothed lead-out
8: Longer lead-in and lead-out than 6, didn't drop node
9: Constant acceleration
10: Constant deceleration. Dropped 2 nodes in testing.
11: Same as 0
12: 10 but slower lead-in, reaches end node less early
13: Extremely close to 3, slightly longer lead-in/lead-out
14: Constant acceleration, dropped last 2 nodes in testing and halted (?)
15: Very similar to 10, did not drop any nodes.
16: Long lead-in, dropped 2 nodes in testing, very long leadout.
17: Constant acceleration, slower speed-up than 9
18: Same as 17 is to 9, slightly longer lead-out, lingers at end node
19: Very long lead in and out
20: Very long, gradual lead-in acceleration at start, gets extremely fast
21: Same as 20 but for constant deceleration
22: 20 and 21 combined, long linger at end node. Dropped 2 nodes in testing
23: Constant acceleration, doesn't complete path before it stops
24: Same as 23 but with constant deceleration, but completes path
25: 23 and 24 combined, insanely fast at middle.
26: No noticable lead-in, misses last 2 nodes in testing
27+: Alternates between 0 and 26
```

The above is documented and graphed at [Spline Cam Interp Graphs](https://docs.google.com/spreadsheets/d/1ejyiMcEYrhhQOL0mLe8664UN-vU4Oh-SBqQnVcKlFIk/edit?usp=sharing)

Using 1-3 will result in misalignment from the passed durations for the spline nodes, the overall duration will remain but other nodes will be shortened if smoothing anything.

Graph below demonstrates interpolation between 0-1000 and back 10 times.

![](https://i.imgur.com/68htz5K.png)

**Nombres antiguos (alias):** `0xD1B0F412F109EA5D` (`N_0xd1b0f412f109ea5d`)

---
### SetCamUseShallowDofMode

`SET_CAM_USE_SHALLOW_DOF_MODE` · hash `0x16A96863A17552BB` · jhash `0x8306C256` · **Cliente**

```lua
SetCamUseShallowDofMode(cam, toggle)
```
```c
void SET_CAM_USE_SHALLOW_DOF_MODE(Cam cam, BOOL toggle);
```

**Parámetros**

- `cam` (`Cam`): The camera handle
- `toggle` (`BOOL`): Boolean if the camera should use a shallow depth of field or not

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables the usage of a shallow DOF. Needs to be set to true to use [`SET_CAM_NEAR_DOF`](#setcamneardof), [`SET_CAM_FAR_DOF`](#setcamfardof), etc. Doesn't need to be called every tick.

**Usage Example**

A usage example for this native can be found in the following native documentation: [`SET_CAM_DOF_STRENGTH`](#setcamdofstrength).

---
### SetCamViewModeForContext

`SET_CAM_VIEW_MODE_FOR_CONTEXT` · hash `0x2A2173E46DAECD12` · jhash `0x1DEBCB45` · **Cliente**

```lua
SetCamViewModeForContext(context, viewMode)
```
```c
void SET_CAM_VIEW_MODE_FOR_CONTEXT(int context, int viewMode);
```

**Parámetros**

- `context` (`int`): The view context; see [`_GET_CAM_ACTIVE_VIEW_MODE_CONTEXT`](#getcamactiveviewmodecontext).
- `viewMode` (`int`): The view mode; see [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode).

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2A2173E46DAECD12` (`N_0x2a2173e46daecd12`)

---
### SetCinematicButtonActive

`SET_CINEMATIC_BUTTON_ACTIVE` · hash `0x51669F7D1FB53D9F` · jhash `0x3FBC5D00` · **Cliente**

```lua
SetCinematicButtonActive(p0)
```
```c
void SET_CINEMATIC_BUTTON_ACTIVE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### SetCinematicCamShakeAmplitude

`SET_CINEMATIC_CAM_SHAKE_AMPLITUDE` · hash `0xC724C701C30B2FE7` · jhash `0x67510C4B` · **Cliente**

```lua
SetCinematicCamShakeAmplitude(p0)
```
```c
void SET_CINEMATIC_CAM_SHAKE_AMPLITUDE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### SetCinematicModeActive

`SET_CINEMATIC_MODE_ACTIVE` · hash `0xDCF0754AC3D6FD4E` · jhash `0x2009E747` · **Cliente**

```lua
SetCinematicModeActive(toggle)
```
```c
void SET_CINEMATIC_MODE_ACTIVE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Toggles the vehicle cinematic cam; requires the player ped to be in a vehicle to work.
```

---
### SetCinematicNewsChannelActiveThisUpdate

`SET_CINEMATIC_NEWS_CHANNEL_ACTIVE_THIS_UPDATE` · hash `0xDC9DA9E8789F5246` · jhash `0x4938C82F` · **Cliente**

```lua
SetCinematicNewsChannelActiveThisUpdate()
```
```c
void SET_CINEMATIC_NEWS_CHANNEL_ACTIVE_THIS_UPDATE();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDC9DA9E8789F5246` (`N_0xdc9da9e8789f5246`)

---
### SetFirstPersonAimCamNearClipThisUpdate

`SET_FIRST_PERSON_AIM_CAM_NEAR_CLIP_THIS_UPDATE` · hash `0x0AF7B437918103B3` · jhash `0x0E21069D` · **Cliente**

```lua
SetFirstPersonAimCamNearClipThisUpdate(distance)
```
```c
void SET_FIRST_PERSON_AIM_CAM_NEAR_CLIP_THIS_UPDATE(float distance);
```

**Parámetros**

- `distance` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0AF7B437918103B3` (`N_0x0af7b437918103b3`), `_SET_FIRST_PERSON_CAM_NEAR_CLIP` (`SetFirstPersonCamNearClip`)

---
### SetFirstPersonAimCamZoomFactor

`SET_FIRST_PERSON_AIM_CAM_ZOOM_FACTOR` · hash `0x70894BD0915C5BCA` · jhash `0x9F4AF763` · **Cliente**

```lua
SetFirstPersonAimCamZoomFactor(zoomFactor)
```
```c
void SET_FIRST_PERSON_AIM_CAM_ZOOM_FACTOR(float zoomFactor);
```

**Parámetros**

- `zoomFactor` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x70894BD0915C5BCA` (`N_0x70894bd0915c5bca`)

---
### SetFirstPersonCamPitchRange

`_SET_FIRST_PERSON_CAM_PITCH_RANGE` · hash `0xBCFC632DB7673BF0` · jhash `0x76DAC96C` · **Cliente**

```lua
SetFirstPersonCamPitchRange(minAngle, maxAngle)
```
```c
void _SET_FIRST_PERSON_CAM_PITCH_RANGE(float minAngle, float maxAngle);
```

**Parámetros**

- `minAngle` (`float`)
- `maxAngle` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBCFC632DB7673BF0` (`N_0xbcfc632db7673bf0`)

---
### SetFlyCamCoordAndConstrain

`SET_FLY_CAM_COORD_AND_CONSTRAIN` · hash `0xC91C6C55199308CA` · jhash `0x60B345DE` · **Cliente**

```lua
SetFlyCamCoordAndConstrain(cam, x, y, z)
```
```c
void SET_FLY_CAM_COORD_AND_CONSTRAIN(Cam cam, float x, float y, float z);
```

**Parámetros**

- `cam` (`Cam`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC91C6C55199308CA` (`N_0xc91c6c55199308ca`)

---
### SetFlyCamHorizontalResponse

`SET_FLY_CAM_HORIZONTAL_RESPONSE` · hash `0x503F5920162365B2` · jhash `0x56F9ED27` · **Cliente**

```lua
SetFlyCamHorizontalResponse(cam, p1, p2, p3)
```
```c
void SET_FLY_CAM_HORIZONTAL_RESPONSE(Cam cam, float p1, float p2, float p3);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x503F5920162365B2` (`N_0x503f5920162365b2`)

---
### SetFlyCamMaxHeight

`SET_FLY_CAM_MAX_HEIGHT` · hash `0xF9D02130ECDD1D77` · jhash `0x71570DBA` · **Cliente**

```lua
SetFlyCamMaxHeight(cam, height)
```
```c
void SET_FLY_CAM_MAX_HEIGHT(Cam cam, float height);
```

**Parámetros**

- `cam` (`Cam`)
- `height` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF9D02130ECDD1D77` (`N_0xf9d02130ecdd1d77`), `_SET_CAMERA_RANGE` (`SetCameraRange`)

---
### SetFlyCamVerticalSpeedMultiplier

`_SET_FLY_CAM_VERTICAL_SPEED_MULTIPLIER` · hash `0xE827B9382CFB41BA` · **Cliente**

```lua
SetFlyCamVerticalSpeedMultiplier(cam, p1, p2, p3)
```
```c
void _SET_FLY_CAM_VERTICAL_SPEED_MULTIPLIER(Cam cam, float p1, float p2, float p3);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE827B9382CFB41BA` (`N_0xe827b9382cfb41ba`)

---
### SetFollowPedCamThisUpdate

`SET_FOLLOW_PED_CAM_THIS_UPDATE` · hash `0x44A113DD6FFC48D1` · jhash `0x1425F6AC` · **Cliente**

```lua
local retval = SetFollowPedCamThisUpdate(camName, easeTime)
```
```c
BOOL SET_FOLLOW_PED_CAM_THIS_UPDATE(char* camName, int easeTime);
```

**Parámetros**

- `camName` (`char*`): The name of the camera to use this update
- `easeTime` (`int`): The time in milliseconds to ease in the camera

**Devuelve:** `BOOL` — Return `true` if the camera is set successfully and `false` otherwise.

**Descripción oficial:**

Overrides the ped follow camera (not first person camera) with the specified camera. The game loads all camera metadata from `update/update.rpf/x64/data/metadata/cameras.ymt` and `x64a.rpf/data/metadata/cameras.ymt` with the ped follow cameras being of type `camFollowPedCameraMetadata`.

| Follow Camera Names                          |
|----------------------------------------------|
| DEFAULT_FOLLOW_PED_CAMERA                    |
| FOLLOW_PED_ATTACHED_TO_ROPE_CAMERA           |
| FOLLOW_PED_ON_EXILE1\_LADDER_CAMERA           |
| FOLLOW_PED_SKY_DIVING_CAMERA                 |
| FOLLOW_PED_SKY_DIVING_FAMILY5\_CAMERA         |
| NIGHTCLUB_FOLLOW_PED_CAMERA                  |
| FOLLOW_PED_INTIMIDATION_CAMERA               |
| FOLLOW_PED_IN_WATER_CAMERA                   |
| FOLLOW_PED_PRONE_CAMERA                      |
| FOLLOW_PED_ON_SEAT_CAMERA                    |
| FOLLOW_PED_HANGING_UPSIDE_DOWN_CAMERA        |
| FOLLOW_PED_ATTACHED_TO_ROPE_CAMERA           |
| CUSTOM_TRANSITION_AFTER_WARP_SKY_DIVE_CAMERA |
| FOLLOW_PED_ON_HORSE_CAMERA                   |
| FOLLOW_PED_ON_LOUNGER_CAMERA                 |

Other camera hashes (names not found yet)

```cpp
// 0x5DBBFB6E
// 0xA38DB056
// 0x16B702A3
// 0x41D72A2E
```

**Nombres antiguos (alias):** `SET_FOLLOW_PED_CAM_CUTSCENE_CHAT` (`SetFollowPedCamCutsceneChat`)

**Ejemplo (lua):**

```lua
CreateThread(function()
    while true do
        SetFollowPedCamThisUpdate("FOLLOW_PED_ATTACHED_TO_ROPE_CAMERA", 500) -- Zoomed out the ped camera
        Wait(0)
    end
end)
```

---
### SetFollowPedCamViewMode

`SET_FOLLOW_PED_CAM_VIEW_MODE` · hash `0x5A4F9EDF1673F704` · jhash `0x495DBE8D` · **Cliente**

```lua
SetFollowPedCamViewMode(viewMode)
```
```c
void SET_FOLLOW_PED_CAM_VIEW_MODE(int viewMode);
```

**Parámetros**

- `viewMode` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

See [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode) for the follow mode enum.

---
### SetFollowTurretSeatCam

`_SET_FOLLOW_TURRET_SEAT_CAM` · hash `0x5C90CAB09951A12F` · **Cliente**

```lua
SetFollowTurretSeatCam(seatIndex)
```
```c
void _SET_FOLLOW_TURRET_SEAT_CAM(int seatIndex);
```

**Parámetros**

- `seatIndex` (`int`): See [IS_TURRET_SEAT](VEHICLE-1.md#isturretseat)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

**Nombres antiguos (alias):** `0x5C90CAB09951A12F` (`N_0x5c90cab09951a12f`)

---
### SetFollowVehicleCamViewMode

`SET_FOLLOW_VEHICLE_CAM_VIEW_MODE` · hash `0xAC253D7842768F48` · jhash `0xC4FBBBD3` · **Cliente**

```lua
SetFollowVehicleCamViewMode(viewMode)
```
```c
void SET_FOLLOW_VEHICLE_CAM_VIEW_MODE(int viewMode);
```

**Parámetros**

- `viewMode` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

See [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode) for the follow mode enum.

---
### SetFollowVehicleCamZoomLevel

`SET_FOLLOW_VEHICLE_CAM_ZOOM_LEVEL` · hash `0x19464CB6E4078C8A` · jhash `0x8F55EBBE` · **Cliente**

```lua
SetFollowVehicleCamZoomLevel(zoomLevel)
```
```c
void SET_FOLLOW_VEHICLE_CAM_ZOOM_LEVEL(int zoomLevel);
```

**Parámetros**

- `zoomLevel` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

See [`GET_FOLLOW_PED_CAM_VIEW_MODE`](#getfollowpedcamviewmode) for the follow mode enum.

---
### SetGameplayCamFollowPedThisUpdate

`SET_GAMEPLAY_CAM_FOLLOW_PED_THIS_UPDATE` · hash `0x8BBACBF51DA047A8` · jhash `0x7D3007A2` · **Cliente**

```lua
SetGameplayCamFollowPedThisUpdate(ped)
```
```c
void SET_GAMEPLAY_CAM_FOLLOW_PED_THIS_UPDATE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8BBACBF51DA047A8` (`N_0x8bbacbf51da047a8`)

---
### SetGameplayCamHash

`_SET_GAMEPLAY_CAM_HASH` · hash `0x425A920FDB9A0DDA` · **Cliente**

```lua
SetGameplayCamHash(camName)
```
```c
void _SET_GAMEPLAY_CAM_HASH(char* camName);
```

**Parámetros**

- `camName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets gameplay camera to hash
```

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0x425A920FDB9A0DDA` (`N_0x425a920fdb9a0dda`)

---
### SetGameplayCamRawPitch

`_SET_GAMEPLAY_CAM_RAW_PITCH` · hash `0x759E13EBC1C15C5A` · **Cliente**

```lua
SetGameplayCamRawPitch(pitch)
```
```c
void _SET_GAMEPLAY_CAM_RAW_PITCH(float pitch);
```

**Parámetros**

- `pitch` (`float`)

**Devuelve:** `void`

---
### SetGameplayCamRawYaw

`_SET_GAMEPLAY_CAM_RAW_YAW` · hash `0x103991D4A307D472` · **Cliente**

```lua
SetGameplayCamRawYaw(yaw)
```
```c
void _SET_GAMEPLAY_CAM_RAW_YAW(float yaw);
```

**Parámetros**

- `yaw` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Does nothing  
```

```
NativeDB Added Parameter 2: Any p1
```

---
### SetGameplayCamRelativeHeading

`SET_GAMEPLAY_CAM_RELATIVE_HEADING` · hash `0xB4EC2312F4E5B1F1` · jhash `0x20C6217C` · **Cliente**

```lua
SetGameplayCamRelativeHeading(heading)
```
```c
void SET_GAMEPLAY_CAM_RELATIVE_HEADING(float heading);
```

**Parámetros**

- `heading` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the camera position relative to heading in float from -360 to +360.  
Heading is alwyas 0 in aiming camera.  
```

---
### SetGameplayCamRelativePitch

`SET_GAMEPLAY_CAM_RELATIVE_PITCH` · hash `0x6D0858B8EDFD2B7D` · jhash `0x6381B963` · **Cliente**

```lua
SetGameplayCamRelativePitch(angle, scalingFactor)
```
```c
void SET_GAMEPLAY_CAM_RELATIVE_PITCH(float angle, float scalingFactor);
```

**Parámetros**

- `angle` (`float`): the angle to rotate the camera by
- `scalingFactor` (`float`): always seems to be set to 1.0 in native calls

**Devuelve:** `void`

**Descripción oficial:**

This native sets the camera's pitch (rotation on the x-axis).

---
### SetGameplayCamRelativeRotation

`_SET_GAMEPLAY_CAM_RELATIVE_ROTATION` · hash `0x48608C3464F58AB4` · **Cliente**

```lua
SetGameplayCamRelativeRotation(roll, pitch, yaw)
```
```c
void _SET_GAMEPLAY_CAM_RELATIVE_ROTATION(float roll, float pitch, float yaw);
```

**Parámetros**

- `roll` (`float`)
- `pitch` (`float`)
- `yaw` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x48608C3464F58AB4` (`N_0x48608c3464f58ab4`)

---
### SetGameplayCamShakeAmplitude

`SET_GAMEPLAY_CAM_SHAKE_AMPLITUDE` · hash `0xA87E00932DB4D85D` · jhash `0x9219D44A` · **Cliente**

```lua
SetGameplayCamShakeAmplitude(amplitude)
```
```c
void SET_GAMEPLAY_CAM_SHAKE_AMPLITUDE(float amplitude);
```

**Parámetros**

- `amplitude` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the amplitude for the gameplay (i.e. 3rd or 1st) camera to shake. Used in script "drunk_controller.ysc.c4" to simulate making the player drunk.  
```

---
### SetGameplayCamVehicleCamera

`_SET_GAMEPLAY_CAM_VEHICLE_CAMERA` · hash `0x21E253A7F8DA5DFB` · **Cliente**

```lua
SetGameplayCamVehicleCamera(vehicleName)
```
```c
void _SET_GAMEPLAY_CAM_VEHICLE_CAMERA(char* vehicleName);
```

**Parámetros**

- `vehicleName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
From b617 scripts:
CAM::_21E253A7F8DA5DFB("DINGHY");
CAM::_21E253A7F8DA5DFB("ISSI2");
CAM::_21E253A7F8DA5DFB("SPEEDO");
```

**Nombres antiguos (alias):** `0x21E253A7F8DA5DFB` (`N_0x21e253a7f8da5dfb`)

---
### SetGameplayCamVehicleCameraName

`_SET_GAMEPLAY_CAM_VEHICLE_CAMERA_NAME` · hash `0x11FA5D3479C7DD47` · **Cliente**

```lua
SetGameplayCamVehicleCameraName(vehicleModel)
```
```c
void _SET_GAMEPLAY_CAM_VEHICLE_CAMERA_NAME(Hash vehicleModel);
```

**Parámetros**

- `vehicleModel` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x11FA5D3479C7DD47` (`N_0x11fa5d3479c7dd47`)

---
### SetGameplayCoordHint

`SET_GAMEPLAY_COORD_HINT` · hash `0xD51ADCD2D8BC0FB3` · jhash `0xF27483C9` · **Cliente**

```lua
SetGameplayCoordHint(x, y, z, duration, blendOutDuration, blendInDuration, unk)
```
```c
void SET_GAMEPLAY_COORD_HINT(float x, float y, float z, int duration, int blendOutDuration, int blendInDuration, int unk);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `duration` (`int`)
- `blendOutDuration` (`int`)
- `blendInDuration` (`int`)
- `unk` (`int`)

**Devuelve:** `void`

---
### SetGameplayEntityHint

`SET_GAMEPLAY_ENTITY_HINT` · hash `0x189E955A8313E298` · jhash `0x66C32306` · **Cliente**

```lua
SetGameplayEntityHint(entity, xOffset, yOffset, zOffset, p4, p5, p6, p7, p8)
```
```c
void SET_GAMEPLAY_ENTITY_HINT(Entity entity, float xOffset, float yOffset, float zOffset, BOOL p4, int p5, int p6, int p7, Any p8);
```

**Parámetros**

- `entity` (`Entity`)
- `xOffset` (`float`)
- `yOffset` (`float`)
- `zOffset` (`float`)
- `p4` (`BOOL`)
- `p5` (`int`)
- `p6` (`int`)
- `p7` (`int`)
- `p8` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
p6 & p7 - possibly length or time  
```

---
### SetGameplayHintAnimCloseup

`_SET_GAMEPLAY_HINT_ANIM_CLOSEUP` · hash `0xE3433EADAAF7EE40` · jhash `0x2F0CE859` · **Cliente**

```lua
SetGameplayHintAnimCloseup(toggle)
```
```c
void _SET_GAMEPLAY_HINT_ANIM_CLOSEUP(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `GET_IS_MULTIPLAYER_BRIEF` (`GetIsMultiplayerBrief`), `0xE3433EADAAF7EE40` (`N_0xe3433eadaaf7ee40`)

---
### SetGameplayHintAnimOffsetx

`_SET_GAMEPLAY_HINT_ANIM_OFFSETX` · hash `0x5D7B620DAE436138` · jhash `0xFC7464A0` · **Cliente**

```lua
SetGameplayHintAnimOffsetx(xOffset)
```
```c
void _SET_GAMEPLAY_HINT_ANIM_OFFSETX(float xOffset);
```

**Parámetros**

- `xOffset` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5D7B620DAE436138` (`N_0x5d7b620dae436138`)

---
### SetGameplayHintAnimOffsety

`_SET_GAMEPLAY_HINT_ANIM_OFFSETY` · hash `0xC92717EF615B6704` · jhash `0x3554AA0E` · **Cliente**

```lua
SetGameplayHintAnimOffsety(yOffset)
```
```c
void _SET_GAMEPLAY_HINT_ANIM_OFFSETY(float yOffset);
```

**Parámetros**

- `yOffset` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC92717EF615B6704` (`N_0xc92717ef615b6704`)

---
### SetGameplayHintBaseOrbitPitchOffset

`SET_GAMEPLAY_HINT_BASE_ORBIT_PITCH_OFFSET` · hash `0xD1F8363DFAD03848` · jhash `0x79472AE3` · **Cliente**

```lua
SetGameplayHintBaseOrbitPitchOffset(value)
```
```c
void SET_GAMEPLAY_HINT_BASE_ORBIT_PITCH_OFFSET(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD1F8363DFAD03848` (`N_0xd1f8363dfad03848`), `_SET_GAMEPLAY_HINT_ANGLE` (`SetGameplayHintAngle`)

---
### SetGameplayHintFollowDistanceScalar

`SET_GAMEPLAY_HINT_FOLLOW_DISTANCE_SCALAR` · hash `0xF8BDBF3D573049A1` · jhash `0x72E8CD3A` · **Cliente**

```lua
SetGameplayHintFollowDistanceScalar(value)
```
```c
void SET_GAMEPLAY_HINT_FOLLOW_DISTANCE_SCALAR(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF8BDBF3D573049A1` (`N_0xf8bdbf3d573049a1`), `_SET_GAMEPLAY_HINT_ANIM_OFFSETZ` (`SetGameplayHintAnimOffsetz`)

---
### SetGameplayHintFov

`SET_GAMEPLAY_HINT_FOV` · hash `0x513403FB9C56211F` · jhash `0x96FD173B` · **Cliente**

```lua
SetGameplayHintFov(FOV)
```
```c
void SET_GAMEPLAY_HINT_FOV(float FOV);
```

**Parámetros**

- `FOV` (`float`)

**Devuelve:** `void`

---
### SetGameplayObjectHint

`SET_GAMEPLAY_OBJECT_HINT` · hash `0x83E87508A2CA2AC6` · jhash `0x2ED5E2F8` · **Cliente**

```lua
SetGameplayObjectHint(p0, p1, p2, p3, p4, p5, p6, p7)
```
```c
void SET_GAMEPLAY_OBJECT_HINT(Any p0, float p1, float p2, float p3, BOOL p4, Any p5, Any p6, Any p7);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`BOOL`)
- `p5` (`Any`)
- `p6` (`Any`)
- `p7` (`Any`)

**Devuelve:** `void`

---
### SetGameplayPedHint

`SET_GAMEPLAY_PED_HINT` · hash `0x2B486269ACD548D3` · jhash `0x7C27343E` · **Cliente**

```lua
SetGameplayPedHint(p0, x1, y1, z1, p4, duration, blendOutDuration, blendInDuration)
```
```c
void SET_GAMEPLAY_PED_HINT(Ped p0, float x1, float y1, float z1, BOOL p4, int duration, int blendOutDuration, int blendInDuration);
```

**Parámetros**

- `p0` (`Ped`)
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `p4` (`BOOL`)
- `duration` (`int`)
- `blendOutDuration` (`int`)
- `blendInDuration` (`int`)

**Devuelve:** `void`

---
### SetGameplayVehicleHint

`SET_GAMEPLAY_VEHICLE_HINT` · hash `0xA2297E18F3E71C2E` · jhash `0x2C9A11D8` · **Cliente**

```lua
SetGameplayVehicleHint(vehicle, offsetX, offsetY, offsetZ, p4, time, easeInTime, easeOutTime)
```
```c
void SET_GAMEPLAY_VEHICLE_HINT(Vehicle vehicle, float offsetX, float offsetY, float offsetZ, BOOL p4, int time, int easeInTime, int easeOutTime);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to focus on.
- `offsetX` (`float`): Position offset X
- `offsetY` (`float`): Position offset Y
- `offsetZ` (`float`): Position offset Z
- `p4` (`BOOL`)
- `time` (`int`): Effect duration
- `easeInTime` (`int`): Effect fade in duration
- `easeOutTime` (`int`): EFfect fade out duration

**Devuelve:** `void`

**Descripción oficial:**

Focuses the camera on the specified vehicle.

---
### SetInVehicleCamStateThisUpdate

`SET_IN_VEHICLE_CAM_STATE_THIS_UPDATE` · hash `0xE9EA16D6E54CDCA4` · jhash `0x4B22C5CB` · **Cliente**

```lua
SetInVehicleCamStateThisUpdate(p0, p1)
```
```c
void SET_IN_VEHICLE_CAM_STATE_THIS_UPDATE(Vehicle p0, int p1);
```

**Parámetros**

- `p0` (`Vehicle`)
- `p1` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE9EA16D6E54CDCA4` (`N_0xe9ea16d6e54cdca4`)

---
### SetTableGamesCameraThisUpdate

`SET_TABLE_GAMES_CAMERA_THIS_UPDATE` · hash `0x79C0E43EB9B944E2` · **Cliente**

```lua
local retval = SetTableGamesCameraThisUpdate(hash)
```
```c
BOOL SET_TABLE_GAMES_CAMERA_THIS_UPDATE(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Hash for table game

**Devuelve:** `BOOL` — Returns a boolean value indicating if the camera settings were successfully overriden for this current frame.

**Descripción oficial:**

Override the camera work of the third-person camera to table game for current frame only.

|                  HashKey                    |       Hash        |    Game         |
| :---------------------------------: | :-----------:| :-------------:  |
| `CASINO_LUCKY_WHEEL_CAMERA` |   `5891389`   |  Lucky Wheel    |
| `CASINO_SLOT_MACHINE_CAMERA` |  `518572876`  |     Slots       |
| `CASINO_ROULETTE_CAMERA` |   `71681063`  |    Roulette     |
| `CASINO_BLACKJACK_CAMERA` | `-2124244681` |    Blackjack    |
| `CASINO_POKER_CAMERA` | `-1938411241` |   Three Cards   |
| `CASINO_INSIDE_TRACK_CAMERA` | `1929822423` |   Inside Track    |
| `ARCADE_LOVE_PROFESSOR_P1_CAMERA` | `545868034` |   LoveProfessorP1   |
| `ARCADE_LOVE_PROFESSOR_P2_CAMERA` | `935304251` |   LoveProfessorP2   |

**Nombres antiguos (alias):** `0x79C0E43EB9B944E2` (`N_0x79c0e43eb9b944e2`)

**Ejemplo (lua):**

```lua
CreateThread(function()
    while true do
      -- override to lucky wheel camera work
      SetTableGamesCameraThisUpdate(GetHashKey("CASINO_LUCKY_WHEEL_CAMERA"))
      Wait(0)
    end
end)
```

---
### SetThirdPersonAimCamNearClipThisUpdate

`SET_THIRD_PERSON_AIM_CAM_NEAR_CLIP_THIS_UPDATE` · hash `0x42156508606DE65E` · jhash `0x71E9C63E` · **Cliente**

```lua
SetThirdPersonAimCamNearClipThisUpdate(distance)
```
```c
void SET_THIRD_PERSON_AIM_CAM_NEAR_CLIP_THIS_UPDATE(float distance);
```

**Parámetros**

- `distance` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x42156508606DE65E` (`N_0x42156508606de65e`), `_SET_THIRD_PERSON_AIM_CAM_NEAR_CLIP` (`SetThirdPersonAimCamNearClip`)

---
### SetUseHiDof

`SET_USE_HI_DOF` · hash `0xA13B0222F3D94A94` · jhash `0x8BBF2950` · **Cliente**

```lua
SetUseHiDof()
```
```c
void SET_USE_HI_DOF();
```

**Devuelve:** `void`

**Descripción oficial:**

Needs to be called every tick to make the active camera use a high depth of field.\
The DoF can be customized using [`SET_CAM_NEAR_DOF`](#setcamneardof), [`SET_CAM_FAR_DOF`](#setcamfardof), [`SET_CAM_USE_SHALLOW_DOF_MODE`](#setcamuseshallowdofmode), [`SET_CAM_DOF_STRENGTH`](#setcamdofstrength) and other DoF related natives.

**Usage Example**

A usage example for this native can be found in the following native documentation: [`SET_CAM_DOF_STRENGTH`](#setcamdofstrength).

---
### SetUseHiDofInCutscene

`_SET_USE_HI_DOF_IN_CUTSCENE` · hash `0x731A880555DA3647` · **Cliente**

```lua
SetUseHiDofInCutscene()
```
```c
void _SET_USE_HI_DOF_IN_CUTSCENE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Only used in R* Script fm_mission_controller_2020
```

```
NativeDB Introduced: v2699
```

---
### SetWidescreenBorders

`SET_WIDESCREEN_BORDERS` · hash `0xDCD4EA924F42D01A` · jhash `0x1A75DC9A` · **Cliente**

```lua
SetWidescreenBorders(p0, p1)
```
```c
void SET_WIDESCREEN_BORDERS(BOOL p0, int p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`int`)

**Devuelve:** `void`

---
### ShakeCam

`SHAKE_CAM` · hash `0x6A25241C340D3822` · jhash `0x1D4211B0` · **Cliente**

```lua
ShakeCam(cam, shakeName, intensity)
```
```c
void SHAKE_CAM(Cam cam, char* shakeName, float intensity);
```

**Parámetros**

- `cam` (`Cam`): The camera handle.
- `shakeName` (`char*`): The name of the shake.
- `intensity` (`float`): The intensity of the shake.

**Devuelve:** `void`

**Descripción oficial:**

See [`SHAKE_GAMEPLAY_CAM`](#shakegameplaycam) for a full list of camera shakes.

---
### ShakeCinematicCam

`SHAKE_CINEMATIC_CAM` · hash `0xDCE214D9ED58F3CF` · jhash `0x61815F31` · **Cliente**

```lua
ShakeCinematicCam(shakeName, intensity)
```
```c
void SHAKE_CINEMATIC_CAM(char* shakeName, float intensity);
```

**Parámetros**

- `shakeName` (`char*`): The name of the shake.
- `intensity` (`float`): The intensity of the shake.

**Devuelve:** `void`

**Descripción oficial:**

See [`SHAKE_GAMEPLAY_CAM`](#shakegameplaycam) for a full list of camera shakes.

---
### ShakeGameplayCam

`SHAKE_GAMEPLAY_CAM` · hash `0xFD55E49555E017CF` · jhash `0xF2EFE660` · **Cliente**

```lua
ShakeGameplayCam(shakeName, intensity)
```
```c
void SHAKE_GAMEPLAY_CAM(char* shakeName, float intensity);
```

**Parámetros**

- `shakeName` (`char*`): The name of the shake.
- `intensity` (`float`): The intensity of the shake.

**Devuelve:** `void`

**Descripción oficial:**

Shakes the gameplay cam with the specified shake name and intensity.

List of camera shake names:

```
ASSAULT_RIFLE_RECOIL_SHAKE
BOAT_WATER_ENTRY_SHAKE
CAMERA_OPERATOR_SHAKE_X
CAMERA_OPERATOR_SHAKE_Z
CAMERA_OPERATOR_TURBULENCE_SHAKE
CARBINE_RIFLE_ACCURACY_OFFSET_SHAKE
CARBINE_RIFLE_RECOIL_SHAKE
CINEMATIC_SHOOTING_RUN_SHAKE
DAMPED_HAND_SHAKE
DEATH_FAIL_IN_EFFECT_SHAKE
DEATH_FAIL_OUT_EFFECT_SHAKE
DEFAULT_DEPLOY_PARACHUTE_SHAKE
DEFAULT_FIRST_PERSON_RECOIL_SHAKE
DEFAULT_KILL_EFFECT_SHAKE
DEFAULT_THIRD_PERSON_ACCURACY_OFFSET_SHAKE
DEFAULT_THIRD_PERSON_RECOIL_SHAKE
DRUNK_SHAKE
FAMILY5_DRUG_TRIP_SHAKE
FIRST_PERSON_AIM_SHAKE
FIRST_PERSON_DEPLOY_PARACHUTE_SHAKE
FOLLOW_RUN_SHAKE
FOLLOW_SWIM_SHAKE
FPS_ASSAULT_RIFLE_RECOIL_SHAKE
FPS_BOLT_RELOAD_SHAKE
FPS_BULLET_HIT_SHAKE
FPS_DEATH_SHAKE
FPS_GRENADE_LAUNCHER_RECOIL_SHAKE
FPS_MAG_DROP_SHAKE
FPS_MAG_RELOAD_SHAKE
FPS_MELEE_HIT_SHAKE
FPS_MG_RECOIL_SHAKE
FPS_MINIGUN_RECOIL_SHAKE
FPS_PISTOL_RECOIL_SHAKE
FPS_RPG_RECOIL_SHAKE
FPS_SHOTGUN_PUMP_SHAKE
FPS_SHOTGUN_RECOIL_SHAKE
FPS_SMG_RECOIL_SHAKE
FPS_STEERING_WHEEL_HIT_SHAKE
FPS_TANK_RECOIL_SHAKE
FPS_THROW_SHAKE
FPS_VEHICLE_HIT_SHAKE
FPS_ZOOM_IN_SHAKE
GAMEPLAY_EXPLOSION_SHAKE
GRENADE_EXPLOSION_SHAKE
GRENADE_LAUNCHER_RECOIL_SHAKE
HAND_SHAKE
HAND_SHAKE_ROLL
HIGH_DIVE_SHAKE
HIGH_FALL_SHAKE
HIGH_SPEED_BOAT_SHAKE
HIGH_SPEED_POV_SHAKE
HIGH_SPEED_VEHICLE_SHAKE
HIGH_SPEED_VIBRATION_POV_SHAKE
IDLE_HAND_SHAKE
JOLT_SHAKE
KILL_SHOT_SHAKE
LARGE_EXPLOSION_SHAKE
LOW_ORBIT_HIGH_SPEED_CAMERA_SHAKE
LOW_ORBIT_INACCURACY_CAMERA_SHAKE
MEDIUM_EXPLOSION_SHAKE
MG_RECOIL_SHAKE
MINIGUN_RECOIL_SHAKE
PARACHUTING_SHAKE
PISTOL_RECOIL_SHAKE
PLANE_PART_SPEED_SHAKE
POV_IDLE_SHAKE
REPLAY_DRUNK_SHAKE
REPLAY_EXPLOSION_SHAKE
REPLAY_HAND_SHAKE
REPLAY_HIGH_SPEED_VEHICLE_SHAKE
REPLAY_SKY_DIVING_SHAKE
ROAD_VIBRATION_SHAKE
RPG_RECOIL_SHAKE
SHOTGUN_RECOIL_SHAKE
SKY_DIVING_SHAKE
SMALL_EXPLOSION_SHAKE
SMG_RECOIL_SHAKE
STUNT_HAND_SHAKE
SWITCH_HAND_SHAKE
TANK_RECOIL_SHAKE
VEH_IMPACT_HEADING_SHAKE
VEH_IMPACT_PITCH_HEADING_SHAKE_FPS
VEH_IMPACT_PITCH_SHAKE
VIBRATE_SHAKE
WATER_BOB_SHAKE
WOBBLY_SHAKE
```

---
### ShakeScriptGlobal

`SHAKE_SCRIPT_GLOBAL` · hash `0xF4C8CF9E353AFECA` · jhash `0x2B0F05CD` · **Cliente**

```lua
ShakeScriptGlobal(p0, p1)
```
```c
void SHAKE_SCRIPT_GLOBAL(char* p0, float p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
CAM::SHAKE_SCRIPT_GLOBAL("HAND_SHAKE", 0.2);
```

**Nombres antiguos (alias):** `0xF4C8CF9E353AFECA` (`N_0xf4c8cf9e353afeca`)

---
### StopCamPointing

`STOP_CAM_POINTING` · hash `0xF33AB75780BA57DE` · jhash `0x5435F6A5` · **Cliente**

```lua
StopCamPointing(cam)
```
```c
void STOP_CAM_POINTING(Cam cam);
```

**Parámetros**

- `cam` (`Cam`)

**Devuelve:** `void`

---
### StopCamShaking

`STOP_CAM_SHAKING` · hash `0xBDECF64367884AC3` · jhash `0x40D0EB87` · **Cliente**

```lua
StopCamShaking(cam, p1)
```
```c
void STOP_CAM_SHAKING(Cam cam, BOOL p1);
```

**Parámetros**

- `cam` (`Cam`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### StopCinematicCamShaking

`STOP_CINEMATIC_CAM_SHAKING` · hash `0x2238E588E588A6D7` · jhash `0x71C12904` · **Cliente**

```lua
StopCinematicCamShaking(p0)
```
```c
void STOP_CINEMATIC_CAM_SHAKING(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### StopCinematicShot

`STOP_CINEMATIC_SHOT` · hash `0x7660C6E75D3A078E` · jhash `0xD78358C5` · **Cliente**

```lua
StopCinematicShot(p0)
```
```c
void STOP_CINEMATIC_SHOT(Hash p0);
```

**Parámetros**

- `p0` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### StopCutsceneCamShaking

`STOP_CUTSCENE_CAM_SHAKING` · hash `0xDB629FFD9285FA06` · jhash `0xF07D603D` · **Cliente**

```lua
StopCutsceneCamShaking()
```
```c
void STOP_CUTSCENE_CAM_SHAKING();
```

**Devuelve:** `void`

---
### StopGameplayCamShaking

`STOP_GAMEPLAY_CAM_SHAKING` · hash `0x0EF93E9F3D08C178` · jhash `0xFD569E4E` · **Cliente**

```lua
StopGameplayCamShaking(bStopImmediately)
```
```c
void STOP_GAMEPLAY_CAM_SHAKING(BOOL bStopImmediately);
```

**Parámetros**

- `bStopImmediately` (`BOOL`): Should the shake stop this frame.

**Devuelve:** `void`

---
### StopGameplayHint

`STOP_GAMEPLAY_HINT` · hash `0xF46C581C61718916` · jhash `0x1BC28B7B` · **Cliente**

```lua
StopGameplayHint(bStopImmediately)
```
```c
void STOP_GAMEPLAY_HINT(BOOL bStopImmediately);
```

**Parámetros**

- `bStopImmediately` (`BOOL`): Specifies whether the gameplay hint camera should stop instantly `true` or gradually transition out `false`.

**Devuelve:** `void`

**Descripción oficial:**

Terminates the current gameplay hint camera, with an option for immediate cessation or a gradual fade out.

```
NativeDB Introduced: v323
```

---
### StopRenderingScriptCamsUsingCatchUp

`STOP_RENDERING_SCRIPT_CAMS_USING_CATCH_UP` · hash `0xC819F3CBB62BF692` · jhash `0xD3C08183` · **Cliente**

```lua
StopRenderingScriptCamsUsingCatchUp(bShouldApplyAcrossAllThreads, distanceToBlend, blendType)
```
```c
void STOP_RENDERING_SCRIPT_CAMS_USING_CATCH_UP(BOOL bShouldApplyAcrossAllThreads, float distanceToBlend, int blendType);
```

**Parámetros**

- `bShouldApplyAcrossAllThreads` (`BOOL`): If `true`, ensures that the rendering stop request is enforced regardless of other script threads that might still expect rendering to be active. Use with caution to avoid conflicts.
- `distanceToBlend` (`float`): Specifies the distance over which the camera should blend from the scripted camera back to the gameplay camera. A value of `0.0` uses the game's default blending distance.
- `blendType` (`int`): An integer representing `eCamSplineSmoothingFlags` to determine the smoothness of the camera transition. Common values include `CAM_SPLINE_SLOW_IN_OUT_SMOOTH` among others, defining the easing of the blend.

**Devuelve:** `void`

**Descripción oficial:**

Instructs the game engine to stop rendering scripted cameras and transition back to the gameplay camera, optionally applying custom blending and rendering options.

```cpp
enum eRenderingOptionFlags {
    RO_NO_OPTIONS = 0,
    RO_STOP_RENDERING_OPTION_WHEN_PLAYER_EXITS_INTO_COVER = 1
};
```

```cpp
enum eCamSplineSmoothingFlags {
	// No smoothing just moves at a constant rate
	CAM_SPLINE_NO_SMOOTH = 0,
	// Decelerates when approaching a node
	CAM_SPLINE_SLOW_IN_SMOOTH = 1, 
	// Accelerates slowly when leaving a node
	CAM_SPLINE_SLOW_OUT_SMOOTH = 2,    
	// Decelerates when approaching a node and accelerates slowly when leaving a node
	CAM_SPLINE_SLOW_IN_OUT_SMOOTH = 3,
	CAM_SPLINE_VERY_SLOW_IN = 4,
	CAM_SPLINE_VERY_SLOW_OUT = 5,
	CAM_SPLINE_VERY_SLOW_IN_SLOW_OUT = 6,
	CAM_SPLINE_SLOW_IN_VERY_SLOW_OUT = 7,
	CAM_SPLINE_VERY_SLOW_IN_VERY_SLOW_OUT = 8,
	CAM_SPLINE_EASE_IN = 9,
	CAM_SPLINE_EASE_OUT = 10,
	CAM_SPLINE_QUADRATIC_EASE_IN = 11,
	CAM_SPLINE_QUADRATIC_EASE_OUT = 12,
	CAM_SPLINE_QUADRATIC_EASE_IN_OUT = 13,
	CAM_SPLINE_CUBIC_EASE_IN = 14,
	CAM_SPLINE_CUBIC_EASE_OUT = 15,
	CAM_SPLINE_CUBIC_EASE_IN_OUT = 16,
	CAM_SPLINE_QUARTIC_EASE_IN = 17,
	CAM_SPLINE_QUARTIC_EASE_OUT = 18,
	CAM_SPLINE_QUARTIC_EASE_IN_OUT = 19,
	CAM_SPLINE_QUINTIC_EASE_IN = 20,
	CAM_SPLINE_QUINTIC_EASE_OUT = 21,
	CAM_SPLINE_QUINTIC_EASE_IN_OUT = 22,
	CAM_SPLINE_CIRCULAR_EASE_IN = 23,
	CAM_SPLINE_CIRCULAR_EASE_OUT = 24,
	CAM_SPLINE_CIRCULAR_EASE_IN_OUT = 25 
};
```

```
NativeDB Added Parameter 4: int renderingOptions : An integer bitmask of eRenderingOptionFlags to apply specific rendering behaviors during the transition. RO_NO_OPTIONS signifies no special options are applied.
```

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xC819F3CBB62BF692` (`N_0xc819f3cbb62bf692`), `_RENDER_FIRST_PERSON_CAM` (`RenderFirstPersonCam`)

---
### StopScriptGlobalShaking

`STOP_SCRIPT_GLOBAL_SHAKING` · hash `0x1C9D7949FA533490` · jhash `0x26FCFB96` · **Cliente**

```lua
StopScriptGlobalShaking(bStopImmediately)
```
```c
void STOP_SCRIPT_GLOBAL_SHAKING(BOOL bStopImmediately);
```

**Parámetros**

- `bStopImmediately` (`BOOL`): A boolean indicating whether the camera shake should stop instantly (TRUE) or gradually fade out (FALSE).

**Devuelve:** `void`

**Descripción oficial:**

Stops the currently active global camera shake that was initiated by a script. You can check if a global camera shake is active using [IS_SCRIPT_GLOBAL_SHAKING](#isscriptglobalshaking).

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x1C9D7949FA533490` (`N_0x1c9d7949fa533490`)

**Ejemplo (lua):**

```lua
-- Stops the currently active global camera shake with a gradual fade out
if IsScriptGlobalShaking() then
    StopScriptGlobalShaking(false)
end
```

**Ejemplo (js):**

```js
// Stops the currently active global camera shake with a gradual fade out
if (IsScriptGlobalShaking()) {
    StopScriptGlobalShaking(false);
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Stops the currently active global camera shake with a gradual fade out
if (IsScriptGlobalShaking())
{
    StopScriptGlobalShaking(false);
}
```

---
### UseScriptCamForAmbientPopulationOriginThisFrame

`USE_SCRIPT_CAM_FOR_AMBIENT_POPULATION_ORIGIN_THIS_FRAME` · hash `0x271401846BD26E92` · jhash `0x8DC53629` · **Cliente**

```lua
UseScriptCamForAmbientPopulationOriginThisFrame(vehicles, peds)
```
```c
void USE_SCRIPT_CAM_FOR_AMBIENT_POPULATION_ORIGIN_THIS_FRAME(BOOL vehicles, BOOL peds);
```

**Parámetros**

- `vehicles` (`BOOL`)
- `peds` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the ambient ped & vehicle population spawning origin to be based around the active scripted camera for this frame
This will prevent vehicles from being created close to the camera and/or on-screen

**Nombres antiguos (alias):** `0x271401846BD26E92` (`N_0x271401846bd26e92`)

---
### UseVehicleCamStuntSettingsThisUpdate

`USE_VEHICLE_CAM_STUNT_SETTINGS_THIS_UPDATE` · hash `0x6493CF69859B116A` · **Cliente**

```lua
UseVehicleCamStuntSettingsThisUpdate()
```
```c
void USE_VEHICLE_CAM_STUNT_SETTINGS_THIS_UPDATE();
```

**Devuelve:** `void`

**Descripción oficial:**

Applies a predefined set of vehicle camera settings optimized for capturing stunts, effective for the current game update/frame.

```
NativeDB Introduced: v791
```

**Nombres antiguos (alias):** `0x6493CF69859B116A` (`N_0x6493cf69859b116a`), `_USE_STUNT_CAMERA_THIS_FRAME` (`UseStuntCameraThisFrame`)

---
