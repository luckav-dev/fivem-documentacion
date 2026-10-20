# Natives de GTA V — MISC

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `MISC`: **323** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`Absf`](#absf) · [`Absi`](#absi) · [`Acos`](#acos) · [`ActivityFeedCreate`](#activityfeedcreate) · [`AddDispatchSpawnBlockingAngledArea`](#adddispatchspawnblockingangledarea) · [`AddDispatchSpawnBlockingArea`](#adddispatchspawnblockingarea) · [`AddHospitalRestart`](#addhospitalrestart) · [`AddPoliceRestart`](#addpolicerestart) · [`AddPopMultiplierArea`](#addpopmultiplierarea) · [`AddPopMultiplierSphere`](#addpopmultipliersphere) · [`AddReplayStatValue`](#addreplaystatvalue) · [`AddStuntJump`](#addstuntjump) · [`AddStuntJumpAngled`](#addstuntjumpangled) · [`AddTacticalAnalysisPoint`](#addtacticalanalysispoint) · [`AllowMissionCreatorWarp`](#allowmissioncreatorwarp) · [`AreProfileSettingsValid`](#areprofilesettingsvalid) · [`AreStringsEqual`](#arestringsequal) · [`Asin`](#asin) · [`Atan`](#atan) · [`Atan2`](#atan2) · [`BeginReplayStats`](#beginreplaystats) · [`BlockDispatchServiceResourceCreation`](#blockdispatchserviceresourcecreation) · [`CancelOnscreenKeyboard`](#cancelonscreenkeyboard) · [`CancelStuntJump`](#cancelstuntjump) · [`CleanupAsyncInstall`](#cleanupasyncinstall) · [`ClearAngledAreaOfVehicles`](#clearangledareaofvehicles) · [`ClearArea`](#cleararea) · [`ClearAreaLeaveVehicleHealth`](#cleararealeavevehiclehealth) · [`ClearAreaOfCops`](#clearareaofcops) · [`ClearAreaOfObjects`](#clearareaofobjects) · [`ClearAreaOfPeds`](#clearareaofpeds) · [`ClearAreaOfProjectiles`](#clearareaofprojectiles) · [`ClearAreaOfVehicles`](#clearareaofvehicles) · [`ClearBit`](#clearbit) · [`ClearCloudHat`](#clearcloudhat) · [`ClearOverrideWeather`](#clearoverrideweather) · [`ClearReplayStats`](#clearreplaystats) · [`ClearRestartCustomPosition`](#clearrestartcustomposition) · [`ClearTacticalAnalysisPoints`](#cleartacticalanalysispoints) · [`ClearWeatherTypeNowPersistNetwork`](#clearweathertypenowpersistnetwork) · [`ClearWeatherTypePersist`](#clearweathertypepersist) · [`CompareStrings`](#comparestrings) · [`CopyMemory`](#copymemory) · [`CreateIncident`](#createincident) · [`CreateIncidentWithEntity`](#createincidentwithentity) · [`DeleteIncident`](#deleteincident) · [`DeleteStuntJump`](#deletestuntjump) · [`DisableHospitalRestart`](#disablehospitalrestart) · [`DisablePoliceRestart`](#disablepolicerestart) · [`DisableStuntJumpSet`](#disablestuntjumpset) · [`DisplayOnscreenKeyboard`](#displayonscreenkeyboard) · [`DisplayOnscreenKeyboardWithLongerInitialString`](#displayonscreenkeyboardwithlongerinitialstring) · [`DoAutoSave`](#doautosave) · [`DoesPopMultiplierAreaExist`](#doespopmultiplierareaexist) · [`DoesPopMultiplierSphereExist`](#doespopmultipliersphereexist) · [`EnableDispatchService`](#enabledispatchservice) · [`EnableStuntJumpSet`](#enablestuntjumpset) · [`EnableTennisMode`](#enabletennismode) · [`EndReplayStats`](#endreplaystats) · [`FindSpawnPointInDirection`](#findspawnpointindirection) · [`ForceGameStatePlaying`](#forcegamestateplaying) · [`ForceLightningFlash`](#forcelightningflash) · [`GetAllocatedStackSize`](#getallocatedstacksize) · [`GetAngleBetween_2dVectors`](#getanglebetween_2dvectors) · [`GetBaseElementMetadata`](#getbaseelementmetadata) · [`GetBenchmarkIterationsFromCommandLine`](#getbenchmarkiterationsfromcommandline) · [`GetBenchmarkPassFromCommandLine`](#getbenchmarkpassfromcommandline) · [`GetBenchmarkTime`](#getbenchmarktime) · [`GetBitsInRange`](#getbitsinrange) · [`GetCloudHatOpacity`](#getcloudhatopacity) · [`GetCoordsOfProjectileTypeInArea`](#getcoordsofprojectiletypeinarea) · [`GetCoordsOfProjectileTypeWithinDistance`](#getcoordsofprojectiletypewithindistance) · [`GetDistanceBetweenCoords`](#getdistancebetweencoords) · [`GetFakeWantedLevel`](#getfakewantedlevel) · [`GetFrameCount`](#getframecount) · [`GetFrameTime`](#getframetime) · [`GetGameTimer`](#getgametimer) · [`GetGlobalCharBuffer`](#getglobalcharbuffer) · [`GetGroundZAndNormalFor_3dCoord`](#getgroundzandnormalfor_3dcoord) · [`GetGroundZExcludingObjectsFor_3dCoord`](#getgroundzexcludingobjectsfor_3dcoord) · [`GetGroundZFor_3dCoord`](#getgroundzfor_3dcoord) · [`GetHashKey`](#gethashkey) · [`GetHeadingFromVector_2d`](#getheadingfromvector_2d) · [`GetIndexOfCurrentLevel`](#getindexofcurrentlevel) · [`GetIsAutoSaveOff`](#getisautosaveoff) · [`GetIsPlayerInAnimalForm`](#getisplayerinanimalform) · [`GetLinePlaneIntersection`](#getlineplaneintersection) · [`GetMissionFlag`](#getmissionflag) · [`GetModelDimensions`](#getmodeldimensions) · [`GetNextWeatherTypeHashName`](#getnextweathertypehashname) · [`GetNumDispatchedUnitsForPlayer`](#getnumdispatchedunitsforplayer) · [`GetNumSuccessfulStuntJumps`](#getnumsuccessfulstuntjumps) · [`GetNumberOfFreeStacksOfThisSize`](#getnumberoffreestacksofthissize) · [`GetOnscreenKeyboardResult`](#getonscreenkeyboardresult) · [`GetPowerSavingModeDuration`](#getpowersavingmodeduration) · [`GetPrevWeatherTypeHashName`](#getprevweathertypehashname) · [`GetProfileSetting`](#getprofilesetting) · [`GetProjectileNearPed`](#getprojectilenearped) · [`GetRainLevel`](#getrainlevel) · [`GetRandomEventFlag`](#getrandomeventflag) · [`GetRandomFloatInRange`](#getrandomfloatinrange) · [`GetRandomIntInRange`](#getrandomintinrange) · [`GetRandomIntInRange_2`](#getrandomintinrange_2) · [`GetReplayStatAtIndex`](#getreplaystatatindex) · [`GetReplayStatCount`](#getreplaystatcount) · [`GetReplayStatMissionType`](#getreplaystatmissiontype) · [`GetSizeOfSaveData`](#getsizeofsavedata) · [`GetSnowLevel`](#getsnowlevel) · [`GetStatusOfMissionRepeatSave`](#getstatusofmissionrepeatsave) · [`GetTennisSwingAnimComplete`](#gettennisswinganimcomplete) · [`GetTotalSuccessfulStuntJumps`](#gettotalsuccessfulstuntjumps) · [`GetWeatherTypeTransition`](#getweathertypetransition) · [`GetWindDirection`](#getwinddirection) · [`GetWindSpeed`](#getwindspeed) · [`HasAsyncInstallFinished`](#hasasyncinstallfinished) · [`HasBulletImpactedInArea`](#hasbulletimpactedinarea) · [`HasBulletImpactedInBox`](#hasbulletimpactedinbox) · [`HasButtonCombinationJustBeenEntered`](#hasbuttoncombinationjustbeenentered) · [`HasCheatStringJustBeenEntered`](#hascheatstringjustbeenentered) · [`HasResumedFromSuspend`](#hasresumedfromsuspend) · [`HaveCreditsReachedEnd`](#havecreditsreachedend) · [`IgnoreNextRestart`](#ignorenextrestart) · [`IsAreaOccupied`](#isareaoccupied) · [`IsAussieVersion`](#isaussieversion) · [`IsAutoSaveInProgress`](#isautosaveinprogress) · [`IsBitSet`](#isbitset) · [`IsBulletInAngledArea`](#isbulletinangledarea) · [`IsBulletInArea`](#isbulletinarea) · [`IsBulletInBox`](#isbulletinbox) · [`IsCommandLineBenchmarkValueSet`](#iscommandlinebenchmarkvalueset) · [`IsDurangoVersion`](#isdurangoversion) · [`IsFrontendFading`](#isfrontendfading) · [`IsInPowerSavingMode`](#isinpowersavingmode) · [`IsIncidentValid`](#isincidentvalid) · [`IsJapaneseVersion`](#isjapaneseversion) · [`IsMemoryCardInUse`](#ismemorycardinuse) · [`IsMinigameInProgress`](#isminigameinprogress) · [`IsNextWeatherType`](#isnextweathertype) · [`IsOrbisVersion`](#isorbisversion) · [`IsPcVersion`](#ispcversion) · [`IsPointObscuredByAMissionEntity`](#ispointobscuredbyamissionentity) · [`IsPopMultiplierAreaUnk`](#ispopmultiplierareaunk) · [`IsPositionOccupied`](#ispositionoccupied) · [`IsPrevWeatherType`](#isprevweathertype) · [`IsProjectileInArea`](#isprojectileinarea) · [`IsProjectileTypeInAngledArea`](#isprojectiletypeinangledarea) · [`IsProjectileTypeInArea`](#isprojectiletypeinarea) · [`IsProjectileTypeWithinDistance`](#isprojectiletypewithindistance) · [`IsPs3Version`](#isps3version) · [`IsSniperBulletInArea`](#issniperbulletinarea) · [`IsSniperInverted`](#issniperinverted) · [`IsSteamVersion`](#issteamversion) · [`IsStringNull`](#isstringnull) · [`IsStringNullOrEmpty`](#isstringnullorempty) · [`IsStuntJumpInProgress`](#isstuntjumpinprogress) · [`IsStuntJumpMessageShowing`](#isstuntjumpmessageshowing) · [`IsTennisMode`](#istennismode) · [`IsThisAMinigameScript`](#isthisaminigamescript) · [`IsXbox360Version`](#isxbox360version) · [`LandingMenuIsActive`](#landingmenuisactive) · [`LoadCloudHat`](#loadcloudhat) · [`N_0x06462a961e94b67c`](#n_0x06462a961e94b67c) · [`N_0x1178e104409fe58c`](#n_0x1178e104409fe58c) · [`N_0x19bfed045c647c49`](#n_0x19bfed045c647c49) · [`N_0x2107a3773771186d`](#n_0x2107a3773771186d) · [`N_0x21c235bc64831e5a`](#n_0x21c235bc64831e5a) · [`N_0x23227df0b2115469`](#n_0x23227df0b2115469) · [`N_0x31125fd509d9043f`](#n_0x31125fd509d9043f) · [`N_0x39455bf4f4f55186`](#n_0x39455bf4f4f55186) · [`N_0x397baa01068baa96`](#n_0x397baa01068baa96) · [`N_0x48f069265a0e4bec`](#n_0x48f069265a0e4bec) · [`N_0x54f157e0336a3822`](#n_0x54f157e0336a3822) · [`N_0x5b1f2e327b6b6fe1`](#n_0x5b1f2e327b6b6fe1) · [`N_0x65d2ebb47e1cec21`](#n_0x65d2ebb47e1cec21) · [`N_0x693478acbd7f18e7`](#n_0x693478acbd7f18e7) · [`N_0x6f2135b6129620c1`](#n_0x6f2135b6129620c1) · [`N_0x6fddf453c0c756ec`](#n_0x6fddf453c0c756ec) · [`N_0x703cc7f60cbb2b57`](#n_0x703cc7f60cbb2b57) · [`N_0x7ec6f9a478a6a512`](#n_0x7ec6f9a478a6a512) · [`N_0x7f8f6405f4777af6`](#n_0x7f8f6405f4777af6) · [`N_0x8269816f6cfd40f8`](#n_0x8269816f6cfd40f8) · [`N_0x8951eb9c6906d3c8`](#n_0x8951eb9c6906d3c8) · [`N_0x8d74e26f54b4e5c3`](#n_0x8d74e26f54b4e5c3) · [`N_0x916ca67d26fd1e37`](#n_0x916ca67d26fd1e37) · [`N_0x97e7e2c04245115b`](#n_0x97e7e2c04245115b) · [`N_0xa0ad167e4b39d9a2`](#n_0xa0ad167e4b39d9a2) · [`N_0xa4a0065e39c9f25c`](#n_0xa4a0065e39c9f25c) · [`N_0xb51b9ab9ef81868c`](#n_0xb51b9ab9ef81868c) · [`N_0xba4b8d83bdc75551`](#n_0xba4b8d83bdc75551) · [`N_0xd10282b6e3751ba0`](#n_0xd10282b6e3751ba0) · [`N_0xd642319c54aadeb6`](#n_0xd642319c54aadeb6) · [`N_0xd9f692d349249528`](#n_0xd9f692d349249528) · [`N_0xe3d969d2785ffb5e`](#n_0xe3d969d2785ffb5e) · [`N_0xe532ec1a63231b4f`](#n_0xe532ec1a63231b4f) · [`N_0xe95b0c7d5ba3b96b`](#n_0xe95b0c7d5ba3b96b) · [`N_0xeb078ca2b5e82add`](#n_0xeb078ca2b5e82add) · [`N_0xeb2104e905c6f2e9`](#n_0xeb2104e905c6f2e9) · [`N_0xebd3205a207939ed`](#n_0xebd3205a207939ed) · [`N_0xfa3ffb0eebc288a3`](#n_0xfa3ffb0eebc288a3) · [`N_0xfaa457ef263e8763`](#n_0xfaa457ef263e8763) · [`N_0xfb00ca71da386228`](#n_0xfb00ca71da386228) · [`NetworkSetScriptIsSafeForNetworkGame`](#networksetscriptissafefornetworkgame) · [`NextOnscreenKeyboardResultWillDisplayUsingTheseFonts`](#nextonscreenkeyboardresultwilldisplayusingthesefonts) · [`OverrideSaveHouse`](#overridesavehouse) · [`PauseDeathArrestRestart`](#pausedeatharrestrestart) · [`PlayTennisDiveAnim`](#playtennisdiveanim) · [`PlayTennisSwingAnim`](#playtennisswinganim) · [`PopulateNow`](#populatenow) · [`PreloadCloudHat`](#preloadcloudhat) · [`QueueMissionRepeatLoad`](#queuemissionrepeatload) · [`QueueMissionRepeatSave`](#queuemissionrepeatsave) · [`QuitGame`](#quitgame) · [`RegisterBoolToSave`](#registerbooltosave) · [`RegisterEnumToSave`](#registerenumtosave) · [`RegisterFloatToSave`](#registerfloattosave) · [`RegisterInt64ToSave`](#registerint64tosave) · [`RegisterIntToSave`](#registerinttosave) · [`RegisterSaveHouse`](#registersavehouse) · [`RegisterTextLabelToSave`](#registertextlabeltosave) · [`RegisterTextLabelToSave_2`](#registertextlabeltosave_2) · [`RemoveDispatchSpawnBlockingArea`](#removedispatchspawnblockingarea) · [`RemovePopMultiplierArea`](#removepopmultiplierarea) · [`RemovePopMultiplierSphere`](#removepopmultipliersphere) · [`RemoveStealthKill`](#removestealthkill) · [`ResetBenchmarkRecording`](#resetbenchmarkrecording) · [`ResetDispatchIdealSpawnDistance`](#resetdispatchidealspawndistance) · [`ResetDispatchSpawnBlockingAreas`](#resetdispatchspawnblockingareas) · [`ResetDispatchSpawnLocation`](#resetdispatchspawnlocation) · [`ResetDispatchTimeBetweenSpawnAttempts`](#resetdispatchtimebetweenspawnattempts) · [`RestartGame`](#restartgame) · [`SaveBenchmarkRecording`](#savebenchmarkrecording) · [`ScriptRaceGetPlayerSplitTime`](#scriptracegetplayersplittime) · [`ScriptRaceInit`](#scriptraceinit) · [`ScriptRacePlayerHitCheckpoint`](#scriptraceplayerhitcheckpoint) · [`ScriptRaceShutdown`](#scriptraceshutdown) · [`SetBeastModeActive`](#setbeastmodeactive) · [`SetBit`](#setbit) · [`SetBitsInRange`](#setbitsinrange) · [`SetCloudSettingsOverride`](#setcloudsettingsoverride) · [`SetCloudsAlpha`](#setcloudsalpha) · [`SetCreditsActive`](#setcreditsactive) · [`SetDispatchIdealSpawnDistance`](#setdispatchidealspawndistance) · [`SetDispatchSpawnLocation`](#setdispatchspawnlocation) · [`SetDispatchTimeBetweenSpawnAttempts`](#setdispatchtimebetweenspawnattempts) · [`SetDispatchTimeBetweenSpawnAttemptsMultiplier`](#setdispatchtimebetweenspawnattemptsmultiplier) · [`SetExplosiveAmmoThisFrame`](#setexplosiveammothisframe) · [`SetExplosiveMeleeThisFrame`](#setexplosivemeleethisframe) · [`SetFadeInAfterDeathArrest`](#setfadeinafterdeatharrest) · [`SetFadeInAfterLoad`](#setfadeinafterload) · [`SetFadeOutAfterArrest`](#setfadeoutafterarrest) · [`SetFadeOutAfterDeath`](#setfadeoutafterdeath) · [`SetFakeWantedLevel`](#setfakewantedlevel) · [`SetFireAmmoThisFrame`](#setfireammothisframe) · [`SetForcePlayerToJump`](#setforceplayertojump) · [`SetGamePaused`](#setgamepaused) · [`SetGravityLevel`](#setgravitylevel) · [`SetIncidentRequestedUnits`](#setincidentrequestedunits) · [`SetIncidentUnk`](#setincidentunk) · [`SetInstancePriorityHint`](#setinstancepriorityhint) · [`SetInstancePriorityMode`](#setinstanceprioritymode) · [`SetMinigameInProgress`](#setminigameinprogress) · [`SetMissionFlag`](#setmissionflag) · [`SetOverrideWeather`](#setoverrideweather) · [`SetPlayerIsInAnimalForm`](#setplayerisinanimalform) · [`SetPlayerRockstarEditorDisabled`](#setplayerrockstareditordisabled) · [`SetRainLevel`](#setrainlevel) · [`SetRandomEventFlag`](#setrandomeventflag) · [`SetRandomSeed`](#setrandomseed) · [`SetRandomWeatherType`](#setrandomweathertype) · [`SetRestartCustomPosition`](#setrestartcustomposition) · [`SetRiotModeEnabled`](#setriotmodeenabled) · [`SetSaveHouse`](#setsavehouse) · [`SetSaveMenuActive`](#setsavemenuactive) · [`SetSnowLevel`](#setsnowlevel) · [`SetStuntJumpsCanTrigger`](#setstuntjumpscantrigger) · [`SetSuperJumpThisFrame`](#setsuperjumpthisframe) · [`SetThisScriptCanBePaused`](#setthisscriptcanbepaused) · [`SetThisScriptCanRemoveBlipsCreatedByAnyScript`](#setthisscriptcanremoveblipscreatedbyanyscript) · [`SetTimeScale`](#settimescale) · [`SetWeatherTypeNow`](#setweathertypenow) · [`SetWeatherTypeNowPersist`](#setweathertypenowpersist) · [`SetWeatherTypeOvertimePersist`](#setweathertypeovertimepersist) · [`SetWeatherTypePersist`](#setweathertypepersist) · [`SetWeatherTypeTransition`](#setweathertypetransition) · [`SetWind`](#setwind) · [`SetWindDirection`](#setwinddirection) · [`SetWindSpeed`](#setwindspeed) · [`ShootSingleBulletBetweenCoords`](#shootsinglebulletbetweencoords) · [`ShootSingleBulletBetweenCoordsIgnoreEntity`](#shootsinglebulletbetweencoordsignoreentity) · [`ShootSingleBulletBetweenCoordsIgnoreEntityNew`](#shootsinglebulletbetweencoordsignoreentitynew) · [`ShouldUseMetricMeasurements`](#shouldusemetricmeasurements) · [`SlerpNearQuaternion`](#slerpnearquaternion) · [`StartBenchmarkRecording`](#startbenchmarkrecording) · [`StartSaveArrayWithSize`](#startsavearraywithsize) · [`StartSaveData`](#startsavedata) · [`StartSaveStructWithSize`](#startsavestructwithsize) · [`StopBenchmarkRecording`](#stopbenchmarkrecording) · [`StopSaveArray`](#stopsavearray) · [`StopSaveData`](#stopsavedata) · [`StopSaveStruct`](#stopsavestruct) · [`StringToInt`](#stringtoint) · [`SupressRandomEventThisFrame`](#supressrandomeventthisframe) · [`Tan`](#tan) · [`TerminateAllScriptsWithThisName`](#terminateallscriptswiththisname) · [`ToggleShowOptionalStuntJumpCamera`](#toggleshowoptionalstuntjumpcamera) · [`UiStartedEndUserBenchmark`](#uistartedenduserbenchmark) · [`UnloadCloudHat`](#unloadcloudhat) · [`UpdateOnscreenKeyboard`](#updateonscreenkeyboard) · [`UsingMissionCreator`](#usingmissioncreator) · [`WaterOverrideFadeIn`](#wateroverridefadein) · [`WaterOverrideFadeOut`](#wateroverridefadeout) · [`WaterOverrideSetOceannoiseminamplitude`](#wateroverridesetoceannoiseminamplitude) · [`WaterOverrideSetOceanwaveamplitude`](#wateroverridesetoceanwaveamplitude) · [`WaterOverrideSetOceanwavemaxamplitude`](#wateroverridesetoceanwavemaxamplitude) · [`WaterOverrideSetOceanwaveminamplitude`](#wateroverridesetoceanwaveminamplitude) · [`WaterOverrideSetRipplebumpiness`](#wateroverridesetripplebumpiness) · [`WaterOverrideSetRippledisturb`](#wateroverridesetrippledisturb) · [`WaterOverrideSetRipplemaxbumpiness`](#wateroverridesetripplemaxbumpiness) · [`WaterOverrideSetRippleminbumpiness`](#wateroverridesetrippleminbumpiness) · [`WaterOverrideSetShorewaveamplitude`](#wateroverridesetshorewaveamplitude) · [`WaterOverrideSetShorewavemaxamplitude`](#wateroverridesetshorewavemaxamplitude) · [`WaterOverrideSetShorewaveminamplitude`](#wateroverridesetshorewaveminamplitude) · [`WaterOverrideSetStrength`](#wateroverridesetstrength)

---
### Absf

`ABSF` · hash `0x73D57CFFDD12C355` · jhash `0xAF6F6E0B` · **Cliente**

```lua
local retval = Absf(value)
```
```c
float ABSF(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `float`

---
### Absi

`ABSI` · hash `0xF0D31AD191A74F87` · jhash `0xB44677C5` · **Cliente**

```lua
local retval = Absi(value)
```
```c
int ABSI(int value);
```

**Parámetros**

- `value` (`int`)

**Devuelve:** `int`

---
### Acos

`ACOS` · hash `0x1D08B970013C34B6` · jhash `0xF4038776` · **Cliente**

```lua
local retval = Acos(p0)
```
```c
float ACOS(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `float`

---
### ActivityFeedCreate

`ACTIVITY_FEED_CREATE` · hash `0x4DCDF92BF64236CD` · **Cliente**

```lua
ActivityFeedCreate(captionString, condensedCaptionString)
```
```c
void ACTIVITY_FEED_CREATE(char* captionString, char* condensedCaptionString);
```

**Parámetros**

- `captionString` (`char*`): The main text or caption for the activity feed post. This is the primary message displayed in the feed entry.
- `condensedCaptionString` (`char*`): A shorter or condensed version of the caption, used in cases where space is limited or a brief summary is required.

**Devuelve:** `void`

**Descripción oficial:**

Creates and opens a new activity feed post to start filling in.

**Note**: This is a PS4 related native, resulting in a nullsub on the PC platform. This native won't do anything when invoked.

**Nombres antiguos (alias):** `0x4DCDF92BF64236CD` (`N_0x4dcdf92bf64236cd`)

---
### AddDispatchSpawnBlockingAngledArea

`_ADD_DISPATCH_SPAWN_BLOCKING_ANGLED_AREA` · hash `0x918C7B2D2FF3928B` · jhash `0xF557BAF9` · **Cliente**

```lua
local retval = AddDispatchSpawnBlockingAngledArea(x1, y1, z1, x2, y2, z2, width)
```
```c
Any _ADD_DISPATCH_SPAWN_BLOCKING_ANGLED_AREA(float x1, float y1, float z1, float x2, float y2, float z2, float width);
```

**Parámetros**

- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area

**Devuelve:** `Any`

**Descripción oficial:**

To remove, see: [`REMOVE_DISPATCH_SPAWN_BLOCKING_AREA`](#removedispatchspawnblockingarea).

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

**Nombres antiguos (alias):** `0x918C7B2D2FF3928B` (`N_0x918c7b2d2ff3928b`)

---
### AddDispatchSpawnBlockingArea

`_ADD_DISPATCH_SPAWN_BLOCKING_AREA` · hash `0x2D4259F1FEB81DA9` · **Cliente**

```lua
local retval = AddDispatchSpawnBlockingArea(x1, y1, x2, y2)
```
```c
Any _ADD_DISPATCH_SPAWN_BLOCKING_AREA(float x1, float y1, float x2, float y2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `x2` (`float`)
- `y2` (`float`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x2D4259F1FEB81DA9` (`N_0x2d4259f1feb81da9`)

---
### AddHospitalRestart

`ADD_HOSPITAL_RESTART` · hash `0x1F464EF988465A81` · jhash `0x4F3E3104` · **Cliente**

```lua
local retval = AddHospitalRestart(x, y, z, p3, p4)
```
```c
int ADD_HOSPITAL_RESTART(float x, float y, float z, float p3, Any p4);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`float`)
- `p4` (`Any`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the index of the newly created hospital spawn point.  
p3 might be radius?  
```

---
### AddPoliceRestart

`ADD_POLICE_RESTART` · hash `0x452736765B31FC4B` · jhash `0xE96C29FE` · **Cliente**

```lua
local retval = AddPoliceRestart(p0, p1, p2, p3, p4)
```
```c
Any ADD_POLICE_RESTART(float p0, float p1, float p2, float p3, Any p4);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`Any`)

**Devuelve:** `Any`

---
### AddPopMultiplierArea

`ADD_POP_MULTIPLIER_AREA` · hash `0x67F6413D3220E18D` · jhash `0x42BF09B3` · **Cliente**

```lua
local retval = AddPopMultiplierArea(x1, y1, z1, x2, y2, z2, p6, p7, p8)
```
```c
int ADD_POP_MULTIPLIER_AREA(float x1, float y1, float z1, float x2, float y2, float z2, float p6, float p7, BOOL p8);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `p6` (`float`)
- `p7` (`float`)
- `p8` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Added Parameter 10: BOOL p9
```

**Nombres antiguos (alias):** `0x67F6413D3220E18D` (`N_0x67f6413d3220e18d`)

---
### AddPopMultiplierSphere

`ADD_POP_MULTIPLIER_SPHERE` · hash `0x32C7A7E8C43A1F80` · jhash `0xCE4A3D20` · **Cliente**

```lua
local retval = AddPopMultiplierSphere(x, y, z, radius, pedMultiplier, vehicleMultiplier, p6, p7)
```
```c
int ADD_POP_MULTIPLIER_SPHERE(float x, float y, float z, float radius, float pedMultiplier, float vehicleMultiplier, BOOL p6, BOOL p7);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `pedMultiplier` (`float`)
- `vehicleMultiplier` (`float`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
This native is adding a zone, where you can change density settings. For example, you can add a zone on 0.0, 0.0, 0.0 with radius 900.0 and vehicleMultiplier 0.0, and you will not see any new population vehicle spawned in a radius of 900.0 from 0.0, 0.0, 0.0. Returns the id. You can have only 15 zones at the same time. You can remove zone using REMOVE_POP_MULTIPLIER_SPHERE
```

**Nombres antiguos (alias):** `0x32C7A7E8C43A1F80` (`N_0x32c7a7e8c43a1f80`)

---
### AddReplayStatValue

`ADD_REPLAY_STAT_VALUE` · hash `0x69FE6DC87BD2A5E9` · jhash `0x81216EE0` · **Cliente**

```lua
AddReplayStatValue(value)
```
```c
void ADD_REPLAY_STAT_VALUE(Any value);
```

**Parámetros**

- `value` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x69FE6DC87BD2A5E9` (`N_0x69fe6dc87bd2a5e9`)

---
### AddStuntJump

`ADD_STUNT_JUMP` · hash `0x1A992DA297A4630C` · jhash `0xB630E5FF` · **Cliente**

```lua
local retval = AddStuntJump(x1, y1, z1, x2, y2, z2, x3, y3, z3, x4, y4, z4, camX, camY, camZ, unk1, unk2, unk3)
```
```c
int ADD_STUNT_JUMP(float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3, float x4, float y4, float z4, float camX, float camY, float camZ, int unk1, int unk2, int unk3);
```

**Parámetros**

- `x1` (`float`): Jump entry left far bottom corner coordinate X.
- `y1` (`float`): Jump entry left far bottom corner coordinate Y.
- `z1` (`float`): Jump entry left far bottom corner coordinate Z.
- `x2` (`float`): Jump entry right near top corner coordinate X.
- `y2` (`float`): Jump entry right near top corner coordinate Y.
- `z2` (`float`): Jump entry right near top corner coordinate Z.
- `x3` (`float`): Landing zone end coordinate X.
- `y3` (`float`): Landing zone end coordinate Y.
- `z3` (`float`): Landing zone end coordinate Z.
- `x4` (`float`): Landing zone start coordinate X.
- `y4` (`float`): Landing zone start coordinate Y.
- `z4` (`float`): Landing zone start coordinate Z.
- `camX` (`float`): Stuntcam (cinematic) coordinate x.
- `camY` (`float`): Stuntcam (cinematic) coordinate y.
- `camZ` (`float`): Stuntcam (cinematic) coordinate z.
- `unk1` (`int`): Unknown, always 150.
- `unk2` (`int`): Unknown, always 0.
- `unk3` (`int`): Unknown, always 0.

**Devuelve:** `int` — The ID of the stunt jump that was added.

**Descripción oficial:**

See description of [`ADD_STUNT_JUMP_ANGLED`](#addstuntjumpangled) for detailed info. The only difference really is this one does not have the radius (or angle, not sure) floats parameters for entry and landing zones.

---
### AddStuntJumpAngled

`ADD_STUNT_JUMP_ANGLED` · hash `0xBBE5D803A5360CBF` · jhash `0xB9B7E777` · **Cliente**

```lua
local retval = AddStuntJumpAngled(x1, y1, z1, x2, y2, z2, radius1, x3, y3, z3, x4, y4, z4, radius2, camX, camY, camZ, unk1, unk2, unk3)
```
```c
int ADD_STUNT_JUMP_ANGLED(float x1, float y1, float z1, float x2, float y2, float z2, float radius1, float x3, float y3, float z3, float x4, float y4, float z4, float radius2, float camX, float camY, float camZ, int unk1, int unk2, int unk3);
```

**Parámetros**

- `x1` (`float`): Entry zone bottom left corner x.
- `y1` (`float`): Entry zone bottom left corner y.
- `z1` (`float`): Entry zone bottom left corner z.
- `x2` (`float`): Entry zone top right corner x.
- `y2` (`float`): Entry zone top right corner y.
- `z2` (`float`): Entry zone top right corner z.
- `radius1` (`float`): Probably a "feather" radius for entry zone, you need to enter the jump within the min/max coordinates, or within this radius of those two coordinates.
- `x3` (`float`): Landing zone start corner coordinate x.
- `y3` (`float`): Landing zone start corner coordinate y.
- `z3` (`float`): Landing zone start corner coordinate z.
- `x4` (`float`): Landing zone end corner coordinate x.
- `y4` (`float`): Landing zone end corner coordinate y.
- `z4` (`float`): Landing zone end corner coordinate z.
- `radius2` (`float`): Probably a "feather" radius for landing zone, you need to land within the min/max coordinates, or within this radius of those two coordinates.
- `camX` (`float`): Stunt (cinematic) camera x position.
- `camY` (`float`): Stunt (cinematic) camera y position.
- `camZ` (`float`): Stunt (cinematic) camera z position.
- `unk1` (`int`): always 150
- `unk2` (`int`): always 0
- `unk3` (`int`): always 0

**Devuelve:** `int` — The ID of the stuntjump that was created.

**Descripción oficial:**

Creates a new stunt jump.

The radius1 and radius2 might actually not be a radius at all, but that's what it seems to me testing them in-game. But they may be 'angle' floats instead, considering this native is named ADD_STUNT_JUMP\_**ANGLED**.

Info about the specific 'parameter sections':

**x1, y1, z1, x2, y2, z2 and radius1:**

First coordinates are for the jump entry area, and the radius that will be checked around that area. So if you're not exactly within the coordinates, but you are within the outter radius limit then it will still register as entering the stunt jump. Note as mentioned above, the radius is just a guess, I'm not really sure about it's exact purpose.

**x3, y3, z3, x4, y4, z4 and radius2:**

Next part is the landing area, again starting with the left bottom (nearest to the stunt jump entry zone) coordinate, and the second one being the top right furthest away part of the landing area. Followed by another (most likely) radius float, this is usually slightly larger than the entry zone 'radius' float value, just because you have quite a lot of places where you can land (I'm guessing).

**camX, camY and camZ:**

The final coordinate in this native is the Camera position. Rotation and zoom/FOV is managed by the game itself, you just need to provide the camera location.

**unk1, unk2 and unk3:**

Not sure what these are for, but they're always `150, 0, 0` in decompiled scripts.

Visualized example in-game:

![](https://d.fivem.dev/2019-03-15\_18-24\_c7802\_846.png)

Here is a list of almost all of the stunt jumps from GTA V (taken from decompiled scripts): https://pastebin.com/EW1jBPkY

**Ejemplo (lua):**

```lua
local data = {
    entry = {
        leftbottom = vector3(-963.1714, -2778.506, 14.47828),
        righttop = vector3(-965.7361, -2777.121, 19.46395),
        radius = 8.0
    },
    landing = {
        start = vector3(-988.8297, -2830.789, 11.96478),
        ending = vector3(-1027.989, -2895.436, 16.95805),
        radius = 18.0
    },
    camcoords = vector3(-967.196, -2811.716, 14.5521),
    unk1 = 150,
    unk2 = 0,
    unk3 = 0

}

local stuntjump = AddStuntJumpAngled(
    data.entry.leftbottom, 
    data.entry.righttop,
    data.entry.radius,
    data.landing.start,
    data.landing.ending,
    data.landing.radius,
    data.camcoords,
    data.unk1,
    data.unk2,
    data.unk3
)

print("New stunt jump added, id: " .. stuntjump)

Citizen.CreateThread(function()
    while true do
        Wait(0)
        DrawLine(data.entry.leftbottom, data.entry.righttop, 255, 255, 255, 255)
        DrawLine(data.landing.start, data.landing.ending, 255, 0, 0, 255)
        DrawMarker(28, data.camcoords.x, data.camcoords.y, data.camcoords.z, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 1.0, 255, 255, 255, 150, false, false, 2, false, nil, nil, false)
    end
end)
```

---
### AddTacticalAnalysisPoint

`_ADD_TACTICAL_ANALYSIS_POINT` · hash `0xB8721407EE9C3FF6` · jhash `0x24A4E0B2` · **Cliente**

```lua
AddTacticalAnalysisPoint(x, y, z)
```
```c
void _ADD_TACTICAL_ANALYSIS_POINT(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Adds a point related to CTacticalAnalysis
```

**Nombres antiguos (alias):** `0xB8721407EE9C3FF6` (`N_0xb8721407ee9c3ff6`)

---
### AllowMissionCreatorWarp

`ALLOW_MISSION_CREATOR_WARP` · hash `0xDEA36202FC3382DF` · jhash `0x082BA6F2` · **Cliente**

```lua
AllowMissionCreatorWarp(toggle)
```
```c
void ALLOW_MISSION_CREATOR_WARP(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDEA36202FC3382DF` (`N_0xdea36202fc3382df`)

---
### AreProfileSettingsValid

`ARE_PROFILE_SETTINGS_VALID` · hash `0x5AA3BEFA29F03AD4` · jhash `0x46B5A15C` · **Cliente**

```lua
local retval = AreProfileSettingsValid()
```
```c
BOOL ARE_PROFILE_SETTINGS_VALID();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5AA3BEFA29F03AD4` (`N_0x5aa3befa29f03ad4`)

---
### AreStringsEqual

`ARE_STRINGS_EQUAL` · hash `0x0C515FAB3FF9EA92` · jhash `0x877C0BC5` · **Cliente**

```lua
local retval = AreStringsEqual(string1, string2)
```
```c
BOOL ARE_STRINGS_EQUAL(char* string1, char* string2);
```

**Parámetros**

- `string1` (`char*`)
- `string2` (`char*`)

**Devuelve:** `BOOL`

---
### Asin

`ASIN` · hash `0xC843060B5765DCE7` · jhash `0x998E5CAD` · **Cliente**

```lua
local retval = Asin(value)
```
```c
float ASIN(float value);
```

**Parámetros**

- `value` (`float`)

**Devuelve:** `float` — Returns the inverse sine in radians of the specified value

---
### Atan

`ATAN` · hash `0xA9D1795CD5043663` · jhash `0x7A03CC8E` · **Cliente**

```lua
local retval = Atan(p0)
```
```c
float ATAN(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `float`

---
### Atan2

`ATAN2` · hash `0x8927CBF9D22261A4` · jhash `0x2508AC81` · **Cliente**

```lua
local retval = Atan2(p0, p1)
```
```c
float ATAN2(float p0, float p1);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)

**Devuelve:** `float`

---
### BeginReplayStats

`BEGIN_REPLAY_STATS` · hash `0xE0E500246FF73D66` · jhash `0x17F4F44D` · **Cliente**

```lua
BeginReplayStats(p0, p1)
```
```c
void BEGIN_REPLAY_STATS(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
### BlockDispatchServiceResourceCreation

`BLOCK_DISPATCH_SERVICE_RESOURCE_CREATION` · hash `0x9B2BD3773123EA2F` · jhash `0xE0F0684F` · **Cliente**

```lua
BlockDispatchServiceResourceCreation(dispatchService, toggle)
```
```c
void BLOCK_DISPATCH_SERVICE_RESOURCE_CREATION(int dispatchService, BOOL toggle);
```

**Parámetros**

- `dispatchService` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9B2BD3773123EA2F` (`N_0x9b2bd3773123ea2f`)

---
### CancelOnscreenKeyboard

`CANCEL_ONSCREEN_KEYBOARD` · hash `0x58A39BE597CE99CD` · jhash `0x196444BB` · **Cliente**

```lua
CancelOnscreenKeyboard()
```
```c
void CANCEL_ONSCREEN_KEYBOARD();
```

**Devuelve:** `void`

**Descripción oficial:**

Closes the onscreen keyboard on console versions of the game.

**NOTE:** Do not use this native in FiveM/PC, because [`UPDATE_ONSCREEN_KEYBOARD`](#updateonscreenkeyboard) value doesn't get cleaned up and stays as `0`.
You should use [`FORCE_CLOSE_TEXT_INPUT_BOX`](HUD.md#forceclosetextinputbox) instead.

**Nombres antiguos (alias):** `0x58A39BE597CE99CD` (`N_0x58a39be597ce99cd`), `_CANCEL_ONSCREEN_KEYBOARD` (`CancelOnscreenKeyboard`)

---
### CancelStuntJump

`CANCEL_STUNT_JUMP` · hash `0xE6B7B0ACD4E4B75E` · jhash `0xF43D9821` · **Cliente**

```lua
CancelStuntJump()
```
```c
void CANCEL_STUNT_JUMP();
```

**Devuelve:** `void`

---
### CleanupAsyncInstall

`_CLEANUP_ASYNC_INSTALL` · hash `0xC79AE21974B01FB2` · **Cliente**

```lua
CleanupAsyncInstall()
```
```c
void _CLEANUP_ASYNC_INSTALL();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC79AE21974B01FB2` (`N_0xc79ae21974b01fb2`)

---
### ClearAngledAreaOfVehicles

`CLEAR_ANGLED_AREA_OF_VEHICLES` · hash `0x11DB3500F042A8AA` · jhash `0xF11A3018` · **Cliente**

```lua
ClearAngledAreaOfVehicles(x1, y1, z1, x2, y2, z2, width, p7, p8, p9, p10, p11)
```
```c
void CLEAR_ANGLED_AREA_OF_VEHICLES(float x1, float y1, float z1, float x2, float y2, float z2, float width, BOOL p7, BOOL p8, BOOL p9, BOOL p10, BOOL p11);
```

**Parámetros**

- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area
- `p7` (`BOOL`)
- `p8` (`BOOL`)
- `p9` (`BOOL`)
- `p10` (`BOOL`)
- `p11` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 13: Any p12
```

---
### ClearArea

`CLEAR_AREA` · hash `0xA56F01F3765B93A0` · jhash `0x854E9AB8` · **Cliente**

```lua
ClearArea(X, Y, Z, radius, p4, ignoreCopCars, ignoreObjects, p7)
```
```c
void CLEAR_AREA(float X, float Y, float Z, float radius, BOOL p4, BOOL ignoreCopCars, BOOL ignoreObjects, BOOL p7);
```

**Parámetros**

- `X` (`float`)
- `Y` (`float`)
- `Z` (`float`)
- `radius` (`float`)
- `p4` (`BOOL`)
- `ignoreCopCars` (`BOOL`)
- `ignoreObjects` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example: CLEAR_AREA(0, 0, 0, 30, true, false, false, false);  
```

---
### ClearAreaLeaveVehicleHealth

`CLEAR_AREA_LEAVE_VEHICLE_HEALTH` · hash `0x957838AAF91BD12D` · jhash `0x20E4FFD9` · **Cliente**

```lua
ClearAreaLeaveVehicleHealth(x, y, z, radius, p4, p5, p6, p7)
```
```c
void CLEAR_AREA_LEAVE_VEHICLE_HEALTH(float x, float y, float z, float radius, BOOL p4, BOOL p5, BOOL p6, BOOL p7);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
MISC::_0x957838AAF91BD12D(x, y, z, radius, false, false, false, false); seem to make all objects go away, peds, vehicles etc. All booleans set to true doesn't seem to change anything.
```

**Nombres antiguos (alias):** `0x957838AAF91BD12D` (`N_0x957838aaf91bd12d`), `_CLEAR_AREA_OF_EVERYTHING` (`ClearAreaOfEverything`)

---
### ClearAreaOfCops

`CLEAR_AREA_OF_COPS` · hash `0x04F8FC8FCF58F88D` · jhash `0x95C53824` · **Cliente**

```lua
ClearAreaOfCops(x, y, z, radius, createNetEvent)
```
```c
void CLEAR_AREA_OF_COPS(float x, float y, float z, float radius, BOOL createNetEvent);
```

**Parámetros**

- `x` (`float`): The x coordinate of where to clear cops.
- `y` (`float`): The y coordinate of where to clear cops.
- `z` (`float`): The z coordinate of where to clear cops.
- `radius` (`float`): The area radius to clear cops.
- `createNetEvent` (`BOOL`): specifies whether a `CClearAreaEvent` event of should be created for online use.

**Devuelve:** `void`

**Descripción oficial:**

Clears an area of cops at the given coordinates and radius.

**Ejemplo (lua):**

```lua
-- Clear the area, do also create an event
ClearAreaOfCops(0.0, 0.0, 0.0, 10000.0, true)
```

---
### ClearAreaOfObjects

`CLEAR_AREA_OF_OBJECTS` · hash `0xDD9B9B385AAC7F5B` · jhash `0xBB720FE7` · **Cliente**

```lua
ClearAreaOfObjects(x, y, z, radius, flags)
```
```c
void CLEAR_AREA_OF_OBJECTS(float x, float y, float z, float radius, int flags);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
I looked through the PC scripts that this site provides you with a link to find. It shows the last param mainly uses, (0, 2, 6, 16, and 17) so I am going to assume it is a type of flag.  
```

---
### ClearAreaOfPeds

`CLEAR_AREA_OF_PEDS` · hash `0xBE31FD6CE464AC59` · jhash `0x25BE7FA8` · **Cliente**

```lua
ClearAreaOfPeds(x, y, z, radius, createNetEvent)
```
```c
void CLEAR_AREA_OF_PEDS(float x, float y, float z, float radius, BOOL createNetEvent);
```

**Parámetros**

- `x` (`float`): The x coordinate of where to clear peds.
- `y` (`float`): The y coordinate of where to clear peds.
- `z` (`float`): The z coordinate of where to clear peds.
- `radius` (`float`): The area radius to clear peds.
- `createNetEvent` (`BOOL`): specifies whether a `CClearAreaEvent` event of should be created for online use.

**Devuelve:** `void`

**Descripción oficial:**

Clears an area of peds at the given coordinates and radius.

**Ejemplo (lua):**

```lua
-- Clear the area, do also create an event
ClearAreaOfPeds(0.0, 0.0, 0.0, 10000.0, true)
```

---
### ClearAreaOfProjectiles

`CLEAR_AREA_OF_PROJECTILES` · hash `0x0A1CB9094635D1A6` · jhash `0x18DB5434` · **Cliente**

```lua
ClearAreaOfProjectiles(x, y, z, radius, createNetEvent)
```
```c
void CLEAR_AREA_OF_PROJECTILES(float x, float y, float z, float radius, BOOL createNetEvent);
```

**Parámetros**

- `x` (`float`): The x coordinate of where to clear projectiles.
- `y` (`float`): The y coordinate of where to clear projectiles.
- `z` (`float`): The z coordinate of where to clear projectiles.
- `radius` (`float`): The area radius to clear projectiles.
- `createNetEvent` (`BOOL`): specifies whether a `CClearAreaEvent` event of should be created for online use.

**Devuelve:** `void`

**Descripción oficial:**

Clears an area of projectiles at the given coordinates and radius.

**Ejemplo (lua):**

```lua
-- Clear the area, do also create an event
ClearAreaOfProjectiles(0.0, 0.0, 0.0, 10000.0, true)
```

---
### ClearAreaOfVehicles

`CLEAR_AREA_OF_VEHICLES` · hash `0x01C7B9B38428AEB6` · jhash `0x63320F3C` · **Cliente**

```lua
ClearAreaOfVehicles(x, y, z, radius, p4, p5, p6, p7, p8)
```
```c
void CLEAR_AREA_OF_VEHICLES(float x, float y, float z, float radius, BOOL p4, BOOL p5, BOOL p6, BOOL p7, BOOL p8);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example: 		CLEAR_AREA_OF_VEHICLES(0, 0, 0, 10000, false, false, false, false, false);  
```

```
NativeDB Added Parameter 10: BOOL p9
```

---
### ClearBit

`CLEAR_BIT` · hash `0xE80492A9AC099A93` · jhash `0x8BC9E618` · **Cliente**

```lua
local address = ClearBit(offset)
```
```c
void CLEAR_BIT(int* address, int offset);
```

**Parámetros**

- `address` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `offset` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
This sets bit [offset] of [address] to off.
Example:
MISC::CLEAR_BIT(&bitAddress, 1);
To check if this bit has been enabled:
MISC::IS_BIT_SET(bitAddress, 1); // will return 0 afterwards
```

---
### ClearCloudHat

`_CLEAR_CLOUD_HAT` · hash `0x957E790EA1727B64` · jhash `0x2D7787BC` · **Cliente**

```lua
ClearCloudHat()
```
```c
void _CLEAR_CLOUD_HAT();
```

**Devuelve:** `void`

---
### ClearOverrideWeather

`CLEAR_OVERRIDE_WEATHER` · hash `0x338D2E3477711050` · jhash `0x7740EA4E` · **Cliente**

```lua
ClearOverrideWeather()
```
```c
void CLEAR_OVERRIDE_WEATHER();
```

**Devuelve:** `void`

---
### ClearReplayStats

`CLEAR_REPLAY_STATS` · hash `0x1B1AB132A16FDA55` · jhash `0xC47DFF02` · **Cliente**

```lua
ClearReplayStats()
```
```c
void CLEAR_REPLAY_STATS();
```

**Devuelve:** `void`

---
### ClearRestartCustomPosition

`_CLEAR_RESTART_CUSTOM_POSITION` · hash `0xA2716D40842EAF79` · **Cliente**

```lua
ClearRestartCustomPosition()
```
```c
void _CLEAR_RESTART_CUSTOM_POSITION();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA2716D40842EAF79` (`N_0xa2716d40842eaf79`), `_SET_NEXT_RESPAWN_TO_CUSTOM` (`SetNextRespawnToCustom`)

---
### ClearTacticalAnalysisPoints

`_CLEAR_TACTICAL_ANALYSIS_POINTS` · hash `0xB3CD58CCA6CDA852` · jhash `0x66C3C59C` · **Cliente**

```lua
ClearTacticalAnalysisPoints()
```
```c
void _CLEAR_TACTICAL_ANALYSIS_POINTS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB3CD58CCA6CDA852` (`N_0xb3cd58cca6cda852`)

---
### ClearWeatherTypeNowPersistNetwork

`CLEAR_WEATHER_TYPE_NOW_PERSIST_NETWORK` · hash `0x0CF97F497FE7D048` · **Cliente**

```lua
ClearWeatherTypeNowPersistNetwork(transitionTimeInMs)
```
```c
void CLEAR_WEATHER_TYPE_NOW_PERSIST_NETWORK(int transitionTimeInMs);
```

**Parámetros**

- `transitionTimeInMs` (`int`): Transition time in milliseconds.

**Devuelve:** `void`

**Descripción oficial:**

Clears the active weather type after a specific amount of time determined by `transitionTimeInMs`.

**Nombres antiguos (alias):** `0x0CF97F497FE7D048` (`N_0x0cf97f497fe7d048`)

**Ejemplo (lua):**

```lua
RegisterCommand('weathertransition', function(source, args)
    -- Set the weather type to foggy so we can see the change
    SetWeatherTypeNowPersist("FOGGY")
    -- Clear the weather and run the transition
    local transitionTimeInMs = tonumber(args[1]) or 5000
    if transitionTimeInMs > 0 then
        ClearWeatherTypeNowPersistNetwork(transitionTimeInMs)
    end
end, false)
```

---
### ClearWeatherTypePersist

`CLEAR_WEATHER_TYPE_PERSIST` · hash `0xCCC39339BEF76CF5` · jhash `0x6AB757D8` · **Cliente**

```lua
ClearWeatherTypePersist()
```
```c
void CLEAR_WEATHER_TYPE_PERSIST();
```

**Devuelve:** `void`

---
### CompareStrings

`COMPARE_STRINGS` · hash `0x1E34710ECD4AB0EB` · jhash `0xFE25A58F` · **Cliente**

```lua
local retval = CompareStrings(str1, str2, matchCase, maxLength)
```
```c
int COMPARE_STRINGS(char* str1, char* str2, BOOL matchCase, int maxLength);
```

**Parámetros**

- `str1` (`char*`)
- `str2` (`char*`)
- `matchCase` (`BOOL`)
- `maxLength` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Compares two strings up to a specified number of characters.
Parameters:
str1 - String to be compared.
str2 - String to be compared.
matchCase - Comparison will be case-sensitive.
maxLength - Maximum number of characters to compare. A value of -1 indicates an infinite length.
Returns:
A value indicating the relationship between the strings:
<0 - The first non-matching character in 'str1' is less than the one in 'str2'. (e.g. 'A' < 'B', so result = -1)
0 - The contents of both strings are equal.
>0 - The first non-matching character in 'str1' is less than the one in 'str2'. (e.g. 'B' > 'A', so result = 1)
Examples:
MISC::COMPARE_STRINGS("STRING", "string", false, -1); // 0; equal
MISC::COMPARE_STRINGS("TESTING", "test", false, 4); // 0; equal
MISC::COMPARE_STRINGS("R2D2", "R2xx", false, 2); // 0; equal
MISC::COMPARE_STRINGS("foo", "bar", false, -1); // 4; 'f' > 'b'
MISC::COMPARE_STRINGS("A", "A", true, 1); // 0; equal
When comparing case-sensitive strings, lower-case characters are greater than upper-case characters:
MISC::COMPARE_STRINGS("A", "a", true, 1); // -1; 'A' < 'a'
MISC::COMPARE_STRINGS("a", "A", true, 1); // 1; 'a' > 'A'
```

---
### CopyMemory

`_COPY_MEMORY` · hash `0x213AEB2B90CBA7AC` · **Cliente**

```lua
local dst = CopyMemory(src, size)
```
```c
void _COPY_MEMORY(Any* dst, Any src, int size);
```

**Parámetros**

- `dst` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `src` (`Any`)
- `size` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x213AEB2B90CBA7AC` (`N_0x213aeb2b90cba7ac`)

---
### CreateIncident

`CREATE_INCIDENT` · hash `0x3F892CAF67444AE7` · jhash `0xFC5FF7B3` · **Cliente**

```lua
local retval, outIncidentID = CreateIncident(dispatchService, x, y, z, numUnits, radius, outIncidentID)
```
```c
BOOL CREATE_INCIDENT(int dispatchService, float x, float y, float z, int numUnits, float radius, int* outIncidentID);
```

**Parámetros**

- `dispatchService` (`int`): Refer to [ENABLE_DISPATCH_SERVICE](#enabledispatchservice) for dispatch types
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `numUnits` (`int`)
- `radius` (`float`)
- `outIncidentID` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 8: Any p7
NativeDB Added Parameter 9: Any p8
```

---
### CreateIncidentWithEntity

`CREATE_INCIDENT_WITH_ENTITY` · hash `0x05983472F0494E60` · jhash `0xBBC35B03` · **Cliente**

```lua
local retval, outIncidentID = CreateIncidentWithEntity(dispatchService, ped, numUnits, radius, outIncidentID)
```
```c
BOOL CREATE_INCIDENT_WITH_ENTITY(int dispatchService, Ped ped, int numUnits, float radius, int* outIncidentID);
```

**Parámetros**

- `dispatchService` (`int`): Refer to [ENABLE_DISPATCH_SERVICE](#enabledispatchservice) for dispatch types
- `ped` (`Ped`)
- `numUnits` (`int`)
- `radius` (`float`)
- `outIncidentID` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL` — Returns true if the incident was succesfully made

**Descripción oficial:**

```
NativeDB Added Parameter 6: Any p5
NativeDB Added Parameter 7: Any p6
```

---
### DeleteIncident

`DELETE_INCIDENT` · hash `0x556C1AA270D5A207` · jhash `0x212BD0DC` · **Cliente**

```lua
DeleteIncident(incidentId)
```
```c
void DELETE_INCIDENT(int incidentId);
```

**Parámetros**

- `incidentId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Delete an incident with a given id.  
=======================================================  
Correction, I have change this to int, instead of int*  
as it doesn't use a pointer to the createdIncident.  
If you try it you will crash (or) freeze.  
=======================================================  
```

---
### DeleteStuntJump

`DELETE_STUNT_JUMP` · hash `0xDC518000E39DAE1F` · jhash `0x840CB5DA` · **Cliente**

```lua
DeleteStuntJump(p0)
```
```c
void DELETE_STUNT_JUMP(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### DisableHospitalRestart

`DISABLE_HOSPITAL_RESTART` · hash `0xC8535819C450EBA8` · jhash `0x09F49C72` · **Cliente**

```lua
DisableHospitalRestart(hospitalIndex, toggle)
```
```c
void DISABLE_HOSPITAL_RESTART(int hospitalIndex, BOOL toggle);
```

**Parámetros**

- `hospitalIndex` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
The game by default has 5 hospital respawn points. Disabling them all will cause the player to respawn at the last position they were.
```

---
### DisablePoliceRestart

`DISABLE_POLICE_RESTART` · hash `0x23285DED6EBD7EA3` · jhash `0x0A280324` · **Cliente**

```lua
DisablePoliceRestart(policeIndex, toggle)
```
```c
void DISABLE_POLICE_RESTART(int policeIndex, BOOL toggle);
```

**Parámetros**

- `policeIndex` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Disables the spawn point at the police house on the specified index.
policeIndex: The police house index.
toggle: true to enable the spawn point, false to disable.
- Nacorpio
```

---
### DisableStuntJumpSet

`DISABLE_STUNT_JUMP_SET` · hash `0xA5272EBEDD4747F6` · jhash `0x644C9FA4` · **Cliente**

```lua
DisableStuntJumpSet(p0)
```
```c
void DISABLE_STUNT_JUMP_SET(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### DisplayOnscreenKeyboard

`DISPLAY_ONSCREEN_KEYBOARD` · hash `0x00DC833F2568DBF6` · jhash `0xAD99F2CE` · **Cliente**

```lua
DisplayOnscreenKeyboard(keyboardType, windowTitle, description, defaultText, defaultConcat1, defaultConcat2, defaultConcat3, maxInputLength)
```
```c
void DISPLAY_ONSCREEN_KEYBOARD(int keyboardType, char* windowTitle, char* description, char* defaultText, char* defaultConcat1, char* defaultConcat2, char* defaultConcat3, int maxInputLength);
```

**Parámetros**

- `keyboardType` (`int`): See the list above. Default is `0`.
- `windowTitle` (`char*`): Text label for the title of the box.
- `description` (`char*`): Has no use on PC.
- `defaultText` (`char*`): Default text that is written in the input field.
- `defaultConcat1` (`char*`)
- `defaultConcat2` (`char*`)
- `defaultConcat3` (`char*`)
- `maxInputLength` (`int`): Max number of characters that can be typed (2 - 256).

**Devuelve:** `void`

**Descripción oficial:**

Displays a text input box.

```cpp
enum eKeyboardType
{
  ONSCREEN_KEYBOARD_ENGLISH = 0,
  ONSCREEN_KEYBOARD_LOCALISED = 1,
  ONSCREEN_KEYBOARD_PASSWORD = 2,
  ONSCREEN_KEYBOARD_GAMERTAG = 3,
  ONSCREEN_KEYBOARD_EMAIL = 4,
  ONSCREEN_KEYBOARD_BASIC_ENGLISH = 5,
  ONSCREEN_KEYBOARD_FILENAME = 6
};
```

**Ejemplo (lua):**

```lua
AddTextEntry("my_input_title", "Enter something cool:")

DisplayOnscreenKeyboard(0, "my_input_title", "", "", "", "", "", 30) -- Show the text input box

while UpdateOnscreenKeyboard() == 0 do Wait(0) end -- Wait for the user to stop editing

-- This block of code is reached after the user is done editing

local inputUpdate = UpdateOnscreenKeyboard()

if inputUpdate == 1 then -- User hit OK in the text input box
  local result = GetOnscreenKeyboardResult()
  print("You wrote this in the input box:", result)
elseif inputUpdate == 2 then
  print("You canceled the input!")
else -- -1 or 3
  print("An error has occurred")
end
```

---
### DisplayOnscreenKeyboardWithLongerInitialString

`DISPLAY_ONSCREEN_KEYBOARD_WITH_LONGER_INITIAL_STRING` · hash `0xCA78CFA0366592FE` · jhash `0xD2688412` · **Cliente**

```lua
DisplayOnscreenKeyboardWithLongerInitialString(keyboardType, windowTitle, description, defaultText, defaultConcat1, defaultConcat2, defaultConcat3, defaultConcat4, defaultConcat5, defaultConcat6, defaultConcat7, maxInputLength)
```
```c
void DISPLAY_ONSCREEN_KEYBOARD_WITH_LONGER_INITIAL_STRING(int keyboardType, char* windowTitle, char* description, char* defaultText, char* defaultConcat1, char* defaultConcat2, char* defaultConcat3, char* defaultConcat4, char* defaultConcat5, char* defaultConcat6, char* defaultConcat7, int maxInputLength);
```

**Parámetros**

- `keyboardType` (`int`): See [`DISPLAY_ONSCREEN_KEYBOARD`](#displayonscreenkeyboard)
- `windowTitle` (`char*`): Text label of the window title.
- `description` (`char*`): Unused on PC.
- `defaultText` (`char*`): Default text that is written in the input field.
- `defaultConcat1` (`char*`)
- `defaultConcat2` (`char*`)
- `defaultConcat3` (`char*`)
- `defaultConcat4` (`char*`)
- `defaultConcat5` (`char*`)
- `defaultConcat6` (`char*`)
- `defaultConcat7` (`char*`)
- `maxInputLength` (`int`): Value between 2 - 500.

**Devuelve:** `void`

**Descripción oficial:**

Displays the text input box with support for input with 500 characters.

**Nombres antiguos (alias):** `0xCA78CFA0366592FE` (`N_0xca78cfa0366592fe`), `_DISPLAY_ONSCREEN_KEYBOARD_2` (`DisplayOnscreenKeyboard_2`)

---
### DoAutoSave

`DO_AUTO_SAVE` · hash `0x50EEAAD86232EE55` · jhash `0x54C44B1A` · **Cliente**

```lua
DoAutoSave()
```
```c
void DO_AUTO_SAVE();
```

**Devuelve:** `void`

---
### DoesPopMultiplierAreaExist

`DOES_POP_MULTIPLIER_AREA_EXIST` · hash `0x1327E2FE9746BAEE` · jhash `0xE933B34A` · **Cliente**

```lua
local retval = DoesPopMultiplierAreaExist(id)
```
```c
BOOL DOES_POP_MULTIPLIER_AREA_EXIST(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1327E2FE9746BAEE` (`N_0x1327e2fe9746baee`)

---
### DoesPopMultiplierSphereExist

`DOES_POP_MULTIPLIER_SPHERE_EXIST` · hash `0x171BAFB3C60389F4` · jhash `0xD2B7A5A0` · **Cliente**

```lua
local retval = DoesPopMultiplierSphereExist(id)
```
```c
BOOL DOES_POP_MULTIPLIER_SPHERE_EXIST(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x171BAFB3C60389F4` (`N_0x171bafb3c60389f4`)

---
### EnableDispatchService

`ENABLE_DISPATCH_SERVICE` · hash `0xDC0F817884CDD856` · jhash `0x0B710A51` · **Cliente**

```lua
EnableDispatchService(dispatchService, toggle)
```
```c
void ENABLE_DISPATCH_SERVICE(int dispatchService, BOOL toggle);
```

**Parámetros**

- `dispatchService` (`int`): The ID of the dispatch service to toggle.
- `toggle` (`BOOL`): True to enable the dispatch service, false to disable the dispatch service.

**Devuelve:** `void`

**Descripción oficial:**

Enables or disables the specified 'dispatch service' type. 'Dispatch services' are used for spawning AI response peds/vehicles for events such as a fire in the street (type 3 - DT_FireDepartment), or gunfire in a gang area (type 11 - DT_Gangs).

List of dispatch services:

```cpp
enum eDispatchType
{
	DT_Invalid = 0,
	DT_PoliceAutomobile = 1,
	DT_PoliceHelicopter = 2,
	DT_FireDepartment = 3,
	DT_SwatAutomobile = 4,
	DT_AmbulanceDepartment = 5,
	DT_PoliceRiders = 6,
	DT_PoliceVehicleRequest = 7,
	DT_PoliceRoadBlock = 8,
	DT_PoliceAutomobileWaitPulledOver = 9,
	DT_PoliceAutomobileWaitCruising = 10,
	DT_Gangs = 11,
	DT_SwatHelicopter = 13,
	DT_PoliceBoat = 14,
	DT_ArmyVehicle = 15,
	DT_BikerBackup = 15
};
```

Note that 'dispatch service' has nothing to do with the police scanner (audio), to toggle that, use [SET_AUDIO_FLAG](AUDIO.md#setaudioflag) with `'PoliceScannerDisabled'`.

**Nombres antiguos (alias):** `0xDC0F817884CDD856` (`N_0xdc0f817884cdd856`)

---
### EnableStuntJumpSet

`ENABLE_STUNT_JUMP_SET` · hash `0xE369A5783B866016` · jhash `0x9D1E7785` · **Cliente**

```lua
EnableStuntJumpSet(p0)
```
```c
void ENABLE_STUNT_JUMP_SET(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### EnableTennisMode

`ENABLE_TENNIS_MODE` · hash `0x28A04B411933F8A6` · jhash `0x0BD3F9EC` · **Cliente**

```lua
EnableTennisMode(ped, toggle, p2)
```
```c
void ENABLE_TENNIS_MODE(Ped ped, BOOL toggle, BOOL p2);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Makes the ped jump around like they're in a tennis match  
```

---
### EndReplayStats

`END_REPLAY_STATS` · hash `0xA23E821FBDF8A5F2` · jhash `0xCB570185` · **Cliente**

```lua
EndReplayStats()
```
```c
void END_REPLAY_STATS();
```

**Devuelve:** `void`

---
### FindSpawnPointInDirection

`FIND_SPAWN_POINT_IN_DIRECTION` · hash `0x6874E2190B0C1972` · jhash `0x71AEFD77` · **Cliente**

```lua
local retval, spawnPoint = FindSpawnPointInDirection(posX, posY, posZ, dirX, dirY, dirZ, distance, spawnPoint)
```
```c
BOOL FIND_SPAWN_POINT_IN_DIRECTION(float posX, float posY, float posZ, float dirX, float dirY, float dirZ, float distance, Vector3* spawnPoint);
```

**Parámetros**

- `posX` (`float`)
- `posY` (`float`)
- `posZ` (`float`)
- `dirX` (`float`)
- `dirY` (`float`)
- `dirZ` (`float`)
- `distance` (`float`)
- `spawnPoint` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Finds a position ahead of the player by predicting the players next actions.  
The positions match path finding node positions.  
When roads diverge, the position may rapidly change between two or more positions. This is due to the engine not being certain of which path the player will take.  
```

---
### ForceGameStatePlaying

`FORCE_GAME_STATE_PLAYING` · hash `0xC0AA53F866B3134D` · jhash `0x5D209F25` · **Cliente**

```lua
ForceGameStatePlaying()
```
```c
void FORCE_GAME_STATE_PLAYING();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Sets the localplayer playerinfo state back to playing (State 0)  
States are:  
-1: "Invalid"  
0: "Playing"  
1: "Died"  
2: "Arrested"  
3: "Failed Mission"  
4: "Left Game"  
5: "Respawn"  
6: "In MP Cutscene"  
```

**Nombres antiguos (alias):** `_RESET_LOCALPLAYER_STATE` (`ResetLocalplayerState`)

---
### ForceLightningFlash

`FORCE_LIGHTNING_FLASH` · hash `0xF6062E089251C898` · jhash `0xDF38165E` · **Cliente**

```lua
ForceLightningFlash()
```
```c
void FORCE_LIGHTNING_FLASH();
```

**Devuelve:** `void`

**Descripción oficial:**

```
creates single lightning+thunder at random position  
```

**Nombres antiguos (alias):** `_CREATE_LIGHTNING_THUNDER` (`CreateLightningThunder`)

---
### GetAllocatedStackSize

`GET_ALLOCATED_STACK_SIZE` · hash `0x8B3CA62B1EF19B62` · jhash `0x4E9CA30A` · **Cliente**

```lua
local retval = GetAllocatedStackSize()
```
```c
int GET_ALLOCATED_STACK_SIZE();
```

**Devuelve:** `int`

---
### GetAngleBetween_2dVectors

`GET_ANGLE_BETWEEN_2D_VECTORS` · hash `0x186FC4BE848E1C92` · jhash `0xDBF75E58` · **Cliente**

```lua
local retval = GetAngleBetween_2dVectors(x1, y1, x2, y2)
```
```c
float GET_ANGLE_BETWEEN_2D_VECTORS(float x1, float y1, float x2, float y2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `x2` (`float`)
- `y2` (`float`)

**Devuelve:** `float`

---
### GetBaseElementMetadata

`_GET_BASE_ELEMENT_METADATA` · hash `0xB335F761606DB47C` · jhash `0xE23416C1` · **Cliente**

```lua
local retval, p1, p2 = GetBaseElementMetadata(p3, p4)
```
```c
BOOL _GET_BASE_ELEMENT_METADATA(Any* p1, Any* p2, Any p3, BOOL p4);
```

**Parámetros**

- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any`)
- `p4` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB335F761606DB47C` (`N_0xb335f761606db47c`)

---
### GetBenchmarkIterationsFromCommandLine

`_GET_BENCHMARK_ITERATIONS_FROM_COMMAND_LINE` · hash `0x4750FC27570311EC` · **Cliente**

```lua
local retval = GetBenchmarkIterationsFromCommandLine()
```
```c
int _GET_BENCHMARK_ITERATIONS_FROM_COMMAND_LINE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns value of the '-benchmarkIterations' command line option.
```

**Nombres antiguos (alias):** `0x4750FC27570311EC` (`N_0x4750fc27570311ec`)

---
### GetBenchmarkPassFromCommandLine

`_GET_BENCHMARK_PASS_FROM_COMMAND_LINE` · hash `0x1B2366C3F2A5C8DF` · **Cliente**

```lua
local retval = GetBenchmarkPassFromCommandLine()
```
```c
int _GET_BENCHMARK_PASS_FROM_COMMAND_LINE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns value of the '-benchmarkPass' command line option.
```

**Nombres antiguos (alias):** `0x1B2366C3F2A5C8DF` (`N_0x1b2366c3f2a5c8df`)

---
### GetBenchmarkTime

`_GET_BENCHMARK_TIME` · hash `0xE599A503B3837E1B` · **Cliente**

```lua
local retval = GetBenchmarkTime()
```
```c
float _GET_BENCHMARK_TIME();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0xE599A503B3837E1B` (`N_0xe599a503b3837e1b`)

---
### GetBitsInRange

`GET_BITS_IN_RANGE` · hash `0x53158863FCC0893A` · jhash `0xCA03A1E5` · **Cliente**

```lua
local retval = GetBitsInRange(var, rangeStart, rangeEnd)
```
```c
int GET_BITS_IN_RANGE(int var, int rangeStart, int rangeEnd);
```

**Parámetros**

- `var` (`int`)
- `rangeStart` (`int`)
- `rangeEnd` (`int`)

**Devuelve:** `int`

---
### GetCloudHatOpacity

`_GET_CLOUD_HAT_OPACITY` · hash `0x20AC25E781AE4A84` · **Cliente**

```lua
local retval = GetCloudHatOpacity()
```
```c
float _GET_CLOUD_HAT_OPACITY();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x20AC25E781AE4A84` (`N_0x20ac25e781ae4a84`)

---
### GetCoordsOfProjectileTypeInArea

`GET_COORDS_OF_PROJECTILE_TYPE_IN_AREA` · hash `0x8D7A43EC6A5FEA45` · jhash `0x1A40454B` · **Cliente**

```lua
local retval, projectilePos = GetCoordsOfProjectileTypeInArea(x1, y1, z1, x2, y2, z2, projectileHash, ownedByPlayer)
```
```c
BOOL GET_COORDS_OF_PROJECTILE_TYPE_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2, Hash projectileHash, Vector3* projectilePos, BOOL ownedByPlayer);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `projectileHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `projectilePos` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8D7A43EC6A5FEA45` (`N_0x8d7a43ec6a5fea45`), `_GET_IS_PROJECTILE_TYPE_IN_AREA` (`GetIsProjectileTypeInArea`)

---
### GetCoordsOfProjectileTypeWithinDistance

`GET_COORDS_OF_PROJECTILE_TYPE_WITHIN_DISTANCE` · hash `0xDFB4138EEFED7B81` · jhash `0x6BDE5CE4` · **Cliente**

```lua
local retval, outCoords = GetCoordsOfProjectileTypeWithinDistance(ped, weaponHash, distance, ownedByPlayer)
```
```c
BOOL GET_COORDS_OF_PROJECTILE_TYPE_WITHIN_DISTANCE(Ped ped, Hash weaponHash, float distance, Vector3* outCoords, BOOL ownedByPlayer);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `distance` (`float`)
- `outCoords` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xDFB4138EEFED7B81` (`N_0xdfb4138eefed7b81`), `_GET_PROJECTILE_NEAR_PED_COORDS` (`GetProjectileNearPedCoords`)

---
### GetDistanceBetweenCoords

`GET_DISTANCE_BETWEEN_COORDS` · hash `0xF1B760881820C952` · jhash `0xF698765E` · **Cliente**

```lua
local retval = GetDistanceBetweenCoords(x1, y1, z1, x2, y2, z2, useZ)
```
```c
float GET_DISTANCE_BETWEEN_COORDS(float x1, float y1, float z1, float x2, float y2, float z2, BOOL useZ);
```

**Parámetros**

- `x1` (`float`): The X coordinate of the first point.
- `y1` (`float`): The Y coordinate of the first point.
- `z1` (`float`): The Z coordinate of the first point.
- `x2` (`float`): The X coordinate of the second point.
- `y2` (`float`): The Y coordinate of the second point.
- `z2` (`float`): The Z coordinate of the second point.
- `useZ` (`BOOL`): Whether or not to use the Z coordinate.

**Devuelve:** `float` — The distance between the passed points in units.

**Descripción oficial:**

Returns the distance between two three-dimensional points, optionally ignoring the Z values.
If useZ is false, only the 2D plane (X-Y) will be considered for calculating the distance.
Consider using this faster native instead: SYSTEM::VDIST - DVIST always takes in consideration the 3D coordinates.

**Ejemplo (lua):**

```lua
local dist = GetDistanceBetweenCoords(0.0, 0.0, 0.0, 5.0, 5.0, 5.0, true)

-- language faster equivalent:
local firstVec = vector3(0.0, 0.0, 0.0)
local secondVec = vector3(5.0, 5.0, 5.0)

local dist = #(firstVec - secondVec) -- Use Z
local dist = #(firstVec.xy - secondVec.xy) -- Do not use Z
```

**Ejemplo (cs):**

```cs
float dist = GetDistanceBetweenCoords(0f, 0f, 0f, 5f, 5f, 5f, true)

// language faster equivalent:

Vector3 firstVec = new Vector3(0f, 0f, 0f);
Vector3 secondVec = new Vector3(5f, 5f, 5f);

float dist = firstVec.DistanceToSquared(secondVec); // Use Z
float dist = firstVec.DistanceToSquared2D(secondVec); // Do not use Z
```

---
### GetFakeWantedLevel

`GET_FAKE_WANTED_LEVEL` · hash `0x4C9296CBCD1B971E` · jhash `0x0022A430` · **Cliente**

```lua
local retval = GetFakeWantedLevel()
```
```c
int GET_FAKE_WANTED_LEVEL();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x4C9296CBCD1B971E` (`N_0x4c9296cbcd1b971e`)

---
### GetFrameCount

`GET_FRAME_COUNT` · hash `0xFC8202EFC642E6F2` · jhash `0xB477A015` · **Cliente**

```lua
local retval = GetFrameCount()
```
```c
int GET_FRAME_COUNT();
```

**Devuelve:** `int` — The number of the current frame being displayed.

**Descripción oficial:**

Gets the number of the current frame being displayed.

**Ejemplo (lua):**

```lua
-- Create a thread
Citizen.CreateThread(function()
    -- Loop forever
    while true do
        -- Get the number of the current frame being displayed
        local startCount = GetFrameCount()

        -- Wait one second
        Wait(1000)

        -- Get the new number of the current frame being displayed, after waiting one second
        local endCount = GetFrameCount()

        -- Calculate the number of frames that have been rendered between the two points
        local frameNum = endCount - startCount

        -- Print the output to the console, mentioning that it is an approximate value
        print("Approximate FPS: "..frameNum)
    end
end)
```

---
### GetFrameTime

`GET_FRAME_TIME` · hash `0x15C40837039FFAF7` · jhash `0x96374262` · **Cliente**

```lua
local retval = GetFrameTime()
```
```c
float GET_FRAME_TIME();
```

**Devuelve:** `float` — The frame time (in seconds) of the last frame.

**Descripción oficial:**

Gets the high precision frame time of the last frame in seconds.

*note: the example above is way less precise.*

**Ejemplo (lua):**

```lua
local time1 = GetGameTimer()
Citizen.Wait(0)

-- Prints for example 0.01253530010581 at around 90 FPS
print(GetFrameTime())

-- This would print about the same as above, but is less accurate, ie: 0.012
print((GetGameTimer() - time1) / 1000)
```

---
### GetGameTimer

`GET_GAME_TIMER` · hash `0x9CD27B0045628463` · jhash `0xA4EA0691` · **Cliente**

```lua
local retval = GetGameTimer()
```
```c
int GET_GAME_TIMER();
```

**Devuelve:** `int`

---
### GetGlobalCharBuffer

`_GET_GLOBAL_CHAR_BUFFER` · hash `0x24DA7D7667FD7B09` · **Cliente**

```lua
local retval = GetGlobalCharBuffer()
```
```c
char* _GET_GLOBAL_CHAR_BUFFER();
```

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns pointer to an empty string.
GET_C*
```

**Nombres antiguos (alias):** `0x24DA7D7667FD7B09` (`N_0x24da7d7667fd7b09`)

---
### GetGroundZAndNormalFor_3dCoord

`GET_GROUND_Z_AND_NORMAL_FOR_3D_COORD` · hash `0x8BDC7BFC57A81E76` · jhash `0x64D91CED` · **Cliente**

```lua
local retval, groundZ, normal = GetGroundZAndNormalFor_3dCoord(x, y, z)
```
```c
BOOL GET_GROUND_Z_AND_NORMAL_FOR_3D_COORD(float x, float y, float z, float* groundZ, Vector3* normal);
```

**Parámetros**

- `x` (`float`): X-coordinate of the point to check.
- `y` (`float`): Y-coordinate of the point to check.
- `z` (`float`): Z-coordinate of the point to check.
- `groundZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: A pointer to a float where the ground Z-coordinate will be stored if found.
- `normal` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: A pointer to a Vector3 structure where the surface normal at the ground point will be stored.

**Devuelve:** `BOOL` — Returns `true` if ground is found below the given coordinates and the surface normal could be determined, otherwise `false`.

**Descripción oficial:**

Attempts to identify the highest ground Z-coordinate and determine the corresponding surface normal directly beneath a specified 3D coordinate.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x8BDC7BFC57A81E76` (`N_0x8bdc7bfc57a81e76`), `_GET_GROUND_Z_COORD_WITH_OFFSETS` (`GetGroundZCoordWithOffsets`)

**Ejemplo (lua):**

```lua
local x, y, z = 100.0, -200.0, 50.0
local success, groundZ, normal = GetGroundZAndNormalFor_3dCoord(x, y, z)

if success then
    print("Ground Z found at: ", groundZ)
    print("Surface normal is: ", normal.x, normal.y, normal.z)
else
    print("No ground found.")
end
```

**Ejemplo (js):**

```js
const x = 100.0, y = -200.0, z = 50.0;
const success = GetGroundZAndNormalFor_3dCoord(x, y, z);

if (success) {
    console.log("Ground Z found at: ", groundZ);
    console.log("Surface normal is: ", normal.x, normal.y, normal.z);
} else {
    console.log("No ground found.");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

float x = 100.0f, y = -200.0f, z = 50.0f;
bool success = GetGroundZAndNormalFor_3dCoord(x, y, z, out float groundZ, out Vector3 normal);

if (success) {
    Debug.WriteLine($"Ground Z found at: {groundZ}");
    Debug.WriteLine($"Surface normal is: {normal.X}, {normal.Y}, {normal.Z}");
} else {
    Debug.WriteLine("No ground found.");
}
```

---
### GetGroundZExcludingObjectsFor_3dCoord

`GET_GROUND_Z_EXCLUDING_OBJECTS_FOR_3D_COORD` · hash `0x9E82F0F362881B29` · **Cliente**

```lua
local retval, groundZ = GetGroundZExcludingObjectsFor_3dCoord(x, y, z, waterAsGround)
```
```c
BOOL GET_GROUND_Z_EXCLUDING_OBJECTS_FOR_3D_COORD(float x, float y, float z, float* groundZ, BOOL waterAsGround);
```

**Parámetros**

- `x` (`float`): X-coordinate of the point to check.
- `y` (`float`): Y-coordinate of the point to check.
- `z` (`float`): Z-coordinate of the point to check.
- `groundZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: A pointer to a float where the ground Z-coordinate will be stored if found.
- `waterAsGround` (`BOOL`): If set to `true`, water will be included in the check, and its height will be returned if it is higher than the ground level.

**Devuelve:** `BOOL` — Returns `true` if ground (or water, if specified) is found below the given coordinates, otherwise `false`.

**Descripción oficial:**

Determines the highest ground Z-coordinate directly below a specified 3D coordinate, excluding any objects at that point. Optionally, water can be considered as ground when determining the highest point.

```
NativeDB Added Parameter 6: BOOL ignoreDistToWaterLevelCheck - If set to true, the distance to the water level will be ignored when checking for water as ground. 
```

```
NativeDB Introduced: v505
```

**Nombres antiguos (alias):** `0x9E82F0F362881B29` (`N_0x9e82f0f362881b29`), `_GET_GROUND_Z_FOR_3D_COORD_2` (`GetGroundZFor_3dCoord_2`)

---
### GetGroundZFor_3dCoord

`GET_GROUND_Z_FOR_3D_COORD` · hash `0xC906A7DAB05C8D2B` · jhash `0xA1BFD5E0` · **Cliente**

```lua
local retval, groundZ = GetGroundZFor_3dCoord(x, y, z, includeWater)
```
```c
BOOL GET_GROUND_Z_FOR_3D_COORD(float x, float y, float z, float* groundZ, BOOL includeWater);
```

**Parámetros**

- `x` (`float`): Position on the X-axis to get ground elevation.
- `y` (`float`): Position on the Y-axis to get ground elevation.
- `z` (`float`): Position on the Z-axis to get ground elevation.
- `groundZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The Z coordinate for the ground.
- `includeWater` (`BOOL`): Determines if the top water level at the specified position should be considered the ground elevation. (It would only matter if the specified position is located above or under the water)

**Devuelve:** `BOOL` — This native\`s first return value (retval) will return true if the ground elevation has been found, and the second (groundZ) will return the z-coord which represents the ground elevation at the specified position.

**Descripción oficial:**

This native gets the ground level (ground elevation) and returns the Z coordinate that represents it.
Note: This native can only calculate the elevation when the coordinates are within the render distance of the client.

```
NativeDB Added Parameter 6: BOOL p5
```

**Ejemplo (lua):**

```lua
local ped = PlayerPedId()
local pedCoords = GetEntityCoords(ped) 
local retval, groundZ = GetGroundZFor_3dCoord(pedCoords.x, pedCoords.y, pedCoords.z, true)

if retval then
   -- Do stuff with groundZ
end
```

---
### GetHashKey

`GET_HASH_KEY` · hash `0xD24D37CC275948CC` · jhash `0x98EFF6F1` · **Cliente**

```lua
local retval = GetHashKey(string)
```
```c
Hash GET_HASH_KEY(char* string);
```

**Parámetros**

- `string` (`char*`): The string to hash.

**Devuelve:** `Hash` — The hash of `string`.

**Descripción oficial:**

This native converts its past string to hash. It is hashed using jenkins one at a time method.

**Ejemplo (lua):**

```lua
local zentorno = GetHashKey('zentorno')

if GetEntityModel(car) == zentorno then
    print('Car is a zentorno!')
end
```

---
### GetHeadingFromVector_2d

`GET_HEADING_FROM_VECTOR_2D` · hash `0x2FFB6B224F4B2926` · jhash `0xD209D52B` · **Cliente**

```lua
local retval = GetHeadingFromVector_2d(dx, dy)
```
```c
float GET_HEADING_FROM_VECTOR_2D(float dx, float dy);
```

**Parámetros**

- `dx` (`float`)
- `dy` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
dx = x1 - x2
dy = y1 - y2
```

---
### GetIndexOfCurrentLevel

`GET_INDEX_OF_CURRENT_LEVEL` · hash `0xCBAD6729F7B1F4FC` · jhash `0x6F203C6E` · **Cliente**

```lua
local retval = GetIndexOfCurrentLevel()
```
```c
int GET_INDEX_OF_CURRENT_LEVEL();
```

**Devuelve:** `int`

---
### GetIsAutoSaveOff

`GET_IS_AUTO_SAVE_OFF` · hash `0x6E04F06094C87047` · jhash `0xA8546914` · **Cliente**

```lua
local retval = GetIsAutoSaveOff()
```
```c
BOOL GET_IS_AUTO_SAVE_OFF();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if profile setting 208 is equal to 0.
```

**Nombres antiguos (alias):** `0x6E04F06094C87047` (`N_0x6e04f06094c87047`)

---
### GetIsPlayerInAnimalForm

`_GET_IS_PLAYER_IN_ANIMAL_FORM` · hash `0x9689123E3F213AA5` · **Cliente**

```lua
local retval = GetIsPlayerInAnimalForm()
```
```c
BOOL _GET_IS_PLAYER_IN_ANIMAL_FORM();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Although we don't have a jenkins hash for this one, the name is 100% confirmed.
```

**Nombres antiguos (alias):** `0x9689123E3F213AA5` (`N_0x9689123e3f213aa5`)

---
### GetLinePlaneIntersection

`GET_LINE_PLANE_INTERSECTION` · hash `0xF56DFB7B61BE7276` · jhash `0xC6CC812C` · **Cliente**

```lua
local retval, intersectionParameter = GetLinePlaneIntersection(x1, y1, z1, x2, y2, z2, planeX, planeY, planeZ, planeNormalX, planeNormalY, planeNormalZ, intersectionParameter)
```
```c
BOOL GET_LINE_PLANE_INTERSECTION(float x1, float y1, float z1, float x2, float y2, float z2, float planeX, float planeY, float planeZ, float planeNormalX, float planeNormalY, float planeNormalZ, float* intersectionParameter);
```

**Parámetros**

- `x1` (`float`): The X-coordinate of the first point of the line segment.
- `y1` (`float`): The Y-coordinate of the first point of the line segment.
- `z1` (`float`): The Z-coordinate of the first point of the line segment. Together, `x1`, `y1`, and `z1` define the starting point of the line segment.
- `x2` (`float`): The X-coordinate of the second point of the line segment.
- `y2` (`float`): The Y-coordinate of the second point of the line segment.
- `z2` (`float`): The Z-coordinate of the second point of the line segment. Together, `x2`, `y2`, and `z2` define the ending point of the line segment.
- `planeX` (`float`): The X-coordinate of a point on the plane. This, along with `planeY` and `planeZ`, specifies a point that lies on the plane's surface.
- `planeY` (`float`): The Y-coordinate of a point on the plane.
- `planeZ` (`float`): The Z-coordinate of a point on the plane.
- `planeNormalX` (`float`): The X-component of the plane's normal vector. The normal vector is perpendicular to the plane's surface and defines its orientation.
- `planeNormalY` (`float`): The Y-component of the plane's normal vector.
- `planeNormalZ` (`float`): The Z-component of the plane's normal vector. Together, `planeNormalX`, `planeNormalY`, and `planeNormalZ` fully describe the plane's orientation in 3D space.
- `intersectionParameter` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: A pointer to a float. This parameter is used to return the value of `t` at which the line segment intersects the plane. The value of `t` is a scalar multiplier that can be used to calculate the exact intersection point on the line segment. If the line does not intersect the plane, the value of `t` is not meaningful.

**Devuelve:** `BOOL` — Returns `true` if the line segment intersects the plane, in which case the `intersectionParameter` will contain the intersection point's parameter value. Returns `false` if there is no intersection, making the `intersectionParameter` value irrelevant.

**Descripción oficial:**

Determines whether a line segment intersects a plane and, if so, returns the parameter value at which this intersection occurs.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0xF56DFB7B61BE7276` (`N_0xf56dfb7b61be7276`)

**Ejemplo (lua):**

```lua
-- Define the line segment with start and end points
local startX, startY, startZ = 100.0, -200.0, 50.0
local endX, endY, endZ = 200.0, -100.0, 50.0

-- Define the plane with a point on the plane and the normal vector
local planeX, planeY, planeZ = 150.0, -150.0, 50.0
local normalX, normalY, normalZ = 0.0, 0.0, 1.0

-- Call the native
local success, intersectionParameter = GetLinePlaneIntersection(startX, startY, startZ, endX, endY, endZ, planeX, planeY, planeZ, normalX, normalY, normalZ, intersectionParameter)

if success then
    -- Calculate the intersection point using intersectionParameter
    local intersectX = startX + (endX - startX) * intersectionParameter
    local intersectY = startY + (endY - startY) * intersectionParameter
    local intersectZ = startZ + (endZ - startZ) * intersectionParameter
    
    print("Intersection point at: (" .. intersectX .. ", " .. intersectY .. ", " .. intersectZ .. ")")
else
    print("No intersection found.")
end
```

**Ejemplo (js):**

```js
// Define the line segment with start and end points
const startX = 100.0, startY = -200.0, startZ = 50.0;
const endX = 200.0, endY = -100.0, endZ = 50.0;

// Define the plane with a point on the plane and the normal vector
const planeX = 150.0, planeY = -150.0, planeZ = 50.0;
const normalX = 0.0, normalY = 0.0, normalZ = 1.0;

// Call the native
const [success, intersectionParameter] = GetLinePlaneIntersection(startX, startY, startZ, endX, endY, endZ, planeX, planeY, planeZ, normalX, normalY, normalZ, intersectionParameter);

if (success) {
    // Calculate the intersection point using intersectionParameter
    const intersectX = startX + (endX - startX) * intersectionParameter;
    const intersectY = startY + (endY - startY) * intersectionParameter;
    const intersectZ = startZ + (endZ - startZ) * intersectionParameter;
    
    console.log(`Intersection point at: (${intersectX}, ${intersectY}, ${intersectZ})`);
} else {
    console.log("No intersection found.");
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Define the line segment with start and end points
float startX = 100.0f, startY = -200.0f, startZ = 50.0f;
float endX = 200.0f, endY = -100.0f, endZ = 50.0f;

// Define the plane with a point on the plane and the normal vector
float planeX = 150.0f, planeY = -150.0f, planeZ = 50.0f;
float normalX = 0.0f, normalY = 0.0f, normalZ = 1.0f;

// Call the native
bool success = GetLinePlaneIntersection(startX, startY, startZ, endX, endY, endZ, planeX, planeY, planeZ, normalX, normalY, normalZ, out float intersectionParameter);

if (success) {
    // Calculate the intersection point using intersectionParameter
    float intersectX = startX + (endX - startX) * intersectionParameter;
    float intersectY = startY + (endY - startY) * intersectionParameter;
    float intersectZ = startZ + (endZ - startZ) * intersectionParameter;
    
    Debug.WriteLine($"Intersection point at: ({intersectX}, {intersectY}, {intersectZ})");
} else {
    Debug.WriteLine("No intersection found.");
}
```

---
### GetMissionFlag

`GET_MISSION_FLAG` · hash `0xA33CDCCDA663159E` · jhash `0x95115F97` · **Cliente**

```lua
local retval = GetMissionFlag()
```
```c
BOOL GET_MISSION_FLAG();
```

**Devuelve:** `BOOL`

---
### GetModelDimensions

`GET_MODEL_DIMENSIONS` · hash `0x03E8D3D5F549087A` · jhash `0x91ABB8E0` · **Cliente**

```lua
local minimum, maximum = GetModelDimensions(modelHash)
```
```c
void GET_MODEL_DIMENSIONS(Hash modelHash, Vector3* minimum, Vector3* maximum);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `minimum` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `maximum` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Gets the dimensions of a model.
Calculate (maximum - minimum) to get the size, in which case, Y will be how long the model is.
Example from the scripts: MISC::GET_MODEL_DIMENSIONS(ENTITY::GET_ENTITY_MODEL(PLAYER::PLAYER_PED_ID()), &v_1A, &v_17);
```

---
### GetNextWeatherTypeHashName

`GET_NEXT_WEATHER_TYPE_HASH_NAME` · hash `0x711327CD09C8F162` · jhash `0x353E8056` · **Cliente**

```lua
local retval = GetNextWeatherTypeHashName()
```
```c
Hash GET_NEXT_WEATHER_TYPE_HASH_NAME();
```

**Devuelve:** `Hash`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

**Nombres antiguos (alias):** `_GET_NEXT_WEATHER_TYPE` (`GetNextWeatherType`)

---
### GetNumDispatchedUnitsForPlayer

`_GET_NUM_DISPATCHED_UNITS_FOR_PLAYER` · hash `0xEB4A0C2D56441717` · jhash `0x3CE5BF6B` · **Cliente**

```lua
local retval = GetNumDispatchedUnitsForPlayer(dispatchService)
```
```c
int _GET_NUM_DISPATCHED_UNITS_FOR_PLAYER(int dispatchService);
```

**Parámetros**

- `dispatchService` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xEB4A0C2D56441717` (`N_0xeb4a0c2d56441717`), `_GET_NUMBER_OF_DISPATCHED_UNITS_FOR_PLAYER` (`GetNumberOfDispatchedUnitsForPlayer`)

---
### GetNumSuccessfulStuntJumps

`GET_NUM_SUCCESSFUL_STUNT_JUMPS` · hash `0x996DD1E1E02F1008` · jhash `0x006F9BA2` · **Cliente**

```lua
local retval = GetNumSuccessfulStuntJumps()
```
```c
int GET_NUM_SUCCESSFUL_STUNT_JUMPS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x996DD1E1E02F1008` (`N_0x996dd1e1e02f1008`)

---
### GetNumberOfFreeStacksOfThisSize

`GET_NUMBER_OF_FREE_STACKS_OF_THIS_SIZE` · hash `0xFEAD16FC8F9DFC0F` · jhash `0x11A178B8` · **Cliente**

```lua
local retval = GetNumberOfFreeStacksOfThisSize(stackSize)
```
```c
int GET_NUMBER_OF_FREE_STACKS_OF_THIS_SIZE(int stackSize);
```

**Parámetros**

- `stackSize` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `_GET_FREE_STACK_SLOTS_COUNT` (`GetFreeStackSlotsCount`)

---
### GetOnscreenKeyboardResult

`GET_ONSCREEN_KEYBOARD_RESULT` · hash `0x8362B09B91893647` · jhash `0x44828FB3` · **Cliente**

```lua
local retval = GetOnscreenKeyboardResult()
```
```c
char* GET_ONSCREEN_KEYBOARD_RESULT();
```

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns NULL unless UPDATE_ONSCREEN_KEYBOARD() returns 1 in the same tick.  
```

---
### GetPowerSavingModeDuration

`_GET_POWER_SAVING_MODE_DURATION` · hash `0xABB2FA71C83A1B72` · **Cliente**

```lua
local retval = GetPowerSavingModeDuration()
```
```c
int _GET_POWER_SAVING_MODE_DURATION();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns duration of how long the game has been in power-saving mode (aka "constrained") in milliseconds.
```

**Nombres antiguos (alias):** `0xABB2FA71C83A1B72` (`N_0xabb2fa71c83a1b72`)

---
### GetPrevWeatherTypeHashName

`GET_PREV_WEATHER_TYPE_HASH_NAME` · hash `0x564B884A05EC45A3` · jhash `0xA8171E9E` · **Cliente**

```lua
local retval = GetPrevWeatherTypeHashName()
```
```c
Hash GET_PREV_WEATHER_TYPE_HASH_NAME();
```

**Devuelve:** `Hash`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

**Nombres antiguos (alias):** `_GET_PREV_WEATHER_TYPE` (`GetPrevWeatherType`)

---
### GetProfileSetting

`GET_PROFILE_SETTING` · hash `0xC488FF2356EA7791` · jhash `0xD374BEBC` · **Cliente**

```lua
local retval = GetProfileSetting(profileSetting)
```
```c
int GET_PROFILE_SETTING(int profileSetting);
```

**Parámetros**

- `profileSetting` (`int`)

**Devuelve:** `int`

---
### GetProjectileNearPed

`_GET_PROJECTILE_NEAR_PED` · hash `0x82FDE6A57EE4EE44` · jhash `0x507BC6F7` · **Cliente**

```lua
local retval, outCoords, outProjectile = GetProjectileNearPed(ped, weaponHash, distance, ownedByPlayer)
```
```c
BOOL _GET_PROJECTILE_NEAR_PED(Ped ped, Hash weaponHash, float distance, Vector3* outCoords, Object* outProjectile, BOOL ownedByPlayer);
```

**Parámetros**

- `ped` (`Ped`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `distance` (`float`)
- `outCoords` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `outProjectile` (`Object*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x82FDE6A57EE4EE44` (`N_0x82fde6a57ee4ee44`)

---
### GetRainLevel

`GET_RAIN_LEVEL` · hash `0x96695E368AD855F3` · jhash `0xC9F67F28` · **Cliente**

```lua
local retval = GetRainLevel()
```
```c
float GET_RAIN_LEVEL();
```

**Devuelve:** `float`

---
### GetRandomEventFlag

`GET_RANDOM_EVENT_FLAG` · hash `0xD2D57F1D764117B1` · jhash `0x794CC92C` · **Cliente**

```lua
local retval = GetRandomEventFlag()
```
```c
BOOL GET_RANDOM_EVENT_FLAG();
```

**Devuelve:** `BOOL`

---
### GetRandomFloatInRange

`GET_RANDOM_FLOAT_IN_RANGE` · hash `0x313CE5879CEB6FCD` · jhash `0x0562C4D0` · **Cliente**

```lua
local retval = GetRandomFloatInRange(startRange, endRange)
```
```c
float GET_RANDOM_FLOAT_IN_RANGE(float startRange, float endRange);
```

**Parámetros**

- `startRange` (`float`)
- `endRange` (`float`)

**Devuelve:** `float`

---
### GetRandomIntInRange

`GET_RANDOM_INT_IN_RANGE` · hash `0xD53343AA4FB7DD28` · jhash `0x4051115B` · **Cliente**

```lua
local retval = GetRandomIntInRange(startRange, endRange)
```
```c
int GET_RANDOM_INT_IN_RANGE(int startRange, int endRange);
```

**Parámetros**

- `startRange` (`int`)
- `endRange` (`int`)

**Devuelve:** `int`

---
### GetRandomIntInRange_2

`_GET_RANDOM_INT_IN_RANGE_2` · hash `0xF2D49816A804D134` · **Cliente**

```lua
local retval = GetRandomIntInRange_2(startRange, endRange)
```
```c
int _GET_RANDOM_INT_IN_RANGE_2(int startRange, int endRange);
```

**Parámetros**

- `startRange` (`int`)
- `endRange` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v1734
```

---
### GetReplayStatAtIndex

`GET_REPLAY_STAT_AT_INDEX` · hash `0x8098C8D6597AAE18` · jhash `0x22BE2423` · **Cliente**

```lua
local retval = GetReplayStatAtIndex(index)
```
```c
int GET_REPLAY_STAT_AT_INDEX(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x8098C8D6597AAE18` (`N_0x8098c8d6597aae18`)

---
### GetReplayStatCount

`GET_REPLAY_STAT_COUNT` · hash `0xDC9274A7EF6B2867` · jhash `0xC7BD1AF0` · **Cliente**

```lua
local retval = GetReplayStatCount()
```
```c
int GET_REPLAY_STAT_COUNT();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xDC9274A7EF6B2867` (`N_0xdc9274a7ef6b2867`)

---
### GetReplayStatMissionType

`GET_REPLAY_STAT_MISSION_TYPE` · hash `0x2B626A0150E4D449` · jhash `0x710E5D1E` · **Cliente**

```lua
local retval = GetReplayStatMissionType()
```
```c
int GET_REPLAY_STAT_MISSION_TYPE();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x2B626A0150E4D449` (`N_0x2b626a0150e4d449`)

---
### GetSizeOfSaveData

`GET_SIZE_OF_SAVE_DATA` · hash `0xA09F896CE912481F` · jhash `0x9EF0BC64` · **Cliente**

```lua
local retval = GetSizeOfSaveData(p0)
```
```c
int GET_SIZE_OF_SAVE_DATA(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xA09F896CE912481F` (`N_0xa09f896ce912481f`)

---
### GetSnowLevel

`GET_SNOW_LEVEL` · hash `0xC5868A966E5BE3AE` · jhash `0x1B09184F` · **Cliente**

```lua
local retval = GetSnowLevel()
```
```c
float GET_SNOW_LEVEL();
```

**Devuelve:** `float`

---
### GetStatusOfMissionRepeatSave

`GET_STATUS_OF_MISSION_REPEAT_SAVE` · hash `0x2B5E102E4A42F2BF` · jhash `0x144AAF22` · **Cliente**

```lua
local retval = GetStatusOfMissionRepeatSave()
```
```c
int GET_STATUS_OF_MISSION_REPEAT_SAVE();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x2B5E102E4A42F2BF` (`N_0x2b5e102e4a42f2bf`)

---
### GetTennisSwingAnimComplete

`GET_TENNIS_SWING_ANIM_COMPLETE` · hash `0x17DF68D720AA77F8` · jhash `0x8501E727` · **Cliente**

```lua
local retval = GetTennisSwingAnimComplete(ped)
```
```c
BOOL GET_TENNIS_SWING_ANIM_COMPLETE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x17DF68D720AA77F8` (`N_0x17df68d720aa77f8`)

---
### GetTotalSuccessfulStuntJumps

`GET_TOTAL_SUCCESSFUL_STUNT_JUMPS` · hash `0x6856EC3D35C81EA4` · jhash `0x495BE324` · **Cliente**

```lua
local retval = GetTotalSuccessfulStuntJumps()
```
```c
int GET_TOTAL_SUCCESSFUL_STUNT_JUMPS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x6856EC3D35C81EA4` (`N_0x6856ec3d35c81ea4`)

---
### GetWeatherTypeTransition

`_GET_WEATHER_TYPE_TRANSITION` · hash `0xF3BBE884A14BB413` · jhash `0x9A5C1D56` · **Cliente**

```lua
local weatherType1, weatherType2, percentWeather2 = GetWeatherTypeTransition()
```
```c
void _GET_WEATHER_TYPE_TRANSITION(Hash* weatherType1, Hash* weatherType2, float* percentWeather2);
```

**Parámetros**

- `weatherType1` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `weatherType2` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `percentWeather2` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

---
### GetWindDirection

`GET_WIND_DIRECTION` · hash `0x1F400FEF721170DA` · jhash `0x89499A0D` · **Cliente**

```lua
local retval = GetWindDirection()
```
```c
Vector3 GET_WIND_DIRECTION();
```

**Devuelve:** `Vector3` — The wind direction

**Descripción oficial:**

Used for hunting in singleplayer and for golfing in both sp and online. The [`GET_HEADING_FROM_VECTOR_2D`](#getheadingfromvector_2d) native can be used to get the wind heading from the direction.

**Ejemplo (lua):**

```lua
CreateThread(function()
    while true do
        local windDirection = GetWindDirection()

        -- Gets the wind direction in degrees (math.atan converts the inverse tangent into radians and then math.deg converts it from radians to degrees)
        local degrees = math.deg(math.atan(windDirection.x, windDirection.y))
        print("wind direction in degrees:", degrees)

        -- Draws an airplane marker above the player's head to show the wind direction
        local coords = GetEntityCoords(PlayerPedId())
        DrawMarker(7, coords.x, coords.y, coords.z + 1.0, windDirection.x, windDirection.y, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 255, 128, 0, 50, false, false, 2, false, nil, nil, false)

        -- Get world heading from the direction
        print("wind direction in world heading:", GetHeadingFromVector_2d(windDirection.x, windDirection.y))

        Wait(0)
    end
end)
```

**Ejemplo (js):**

```js
setTick(() => {
    const [windDirectionX, windDirectionY, _windDirectionZ] = GetWindDirection();

    // Gets the wind direction in degrees (Math.atan2 converts the inverse tangent into radians and then we coverte the radians to degrees)
    const degrees = Math.atan2(windDirectionX, windDirectionY) * (180 / Math.PI);
    console.log(`wind direction in degrees: ${degrees}`);

    // Draws an airplane marker above the player's head to show the wind direction
    const [playerX, playerY, playerZ] = GetEntityCoords(PlayerPedId());
    DrawMarker(7, playerX, playerY, playerZ + 1.0, windDirectionX, windDirectionY, 0.0, 0.0, 0.0, 0.0, 2.0, 2.0, 2.0, 255, 128, 0, 50, false, false, 2, false, null, null, false);

    // Get world heading from the direction
    console.log(`wind direction in world heading: ${GetHeadingFromVector_2d(windDirectionX, windDirectionY)}`);
});
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

public Main() 
{
    Tick += OnTick;
}

private async Task OnTick()
{
    Vector3 windDirection = GetWindDirection();

    // Gets the wind direction in degrees (Math.Atan2 converts the inverse tangent into radians and then we coverte the radians to degrees)
    var degrees = Math.Atan2(windDirection.X, windDirection.Y) * (180 / Math.PI);
    Debug.WriteLine($"wind direction in degrees: {degrees}");

    // Draws an airplane marker above the player's head to show the wind direction
    Vector3 playerCoords = Game.PlayerPed.Position;
    DrawMarker(7, playerCoords.X, playerCoords.Y, playerCoords.Z + 1f, windDirection.X, windDirection.Y, 0f, 0f, 0f, 0f, 2f, 2f, 2f, 255, 128, 0, 50, false, false, 2, false, null, null, false);

    // Get world heading from the direction
    Debug.WriteLine($"wind direction in world heading: {GetHeadingFromVector_2d(windDirection.X, windDirection.Y)}");
}
```

---
### GetWindSpeed

`GET_WIND_SPEED` · hash `0xA8CF1CC0AFCD3F12` · jhash `0x098F0F3C` · **Cliente**

```lua
local retval = GetWindSpeed()
```
```c
float GET_WIND_SPEED();
```

**Devuelve:** `float` — The wind speed in meters per second

**Ejemplo (lua):**

```lua
local beaufortScale = {
    [0] = 0.2,
    [1] = 1.5,
    [2] = 3.3,
    [3] = 5.4,
    [4] = 7.9,
    [5] = 10.7,
    [6] = 13.8,
    [7] = 17.1,
    [8] = 20.7,
    [9] = 24.4,
    [10] = 28.4,
    [11] = 32.6,
    [12] = 32.7
}

local windSpeed = GetWindSpeed()
for i = 0, 12 do
    if windSpeed <= beaufortScale[i] or i == 12 then
        print(string.format("The current wind speed (%.2f m/s) is the equivalent to Beaufort number %s on the Beaufort scale", windSpeed, i))
        break
    end
end
```

**Ejemplo (js):**

```js
const beaufortScale = [ 0.2, 1.5, 3.3, 5.4, 7.9, 10.7, 13.8, 17.1, 20.7, 24.4, 28.4, 32.6, 32.7 ];
const windSpeed = GetWindSpeed();

for (let i = 0; i < beaufortScale.length; i++) {
    if (windSpeed <= beaufortScale[i] || i == 12) {
        console.log(`The current wind speed (${windSpeed.toFixed(2)} m/s) is the equivalent to Beaufort number ${i} on the Beaufort scale`);
        break;
    };
};
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// ...

float[] beaufortScale = { 0.2f, 1.5f, 3.3f, 5.4f, 7.9f, 10.7f, 13.8f, 17.1f, 20.7f, 24.4f, 28.4f, 32.6f, 32.7f };
var windSpeed = GetWindSpeed();

for (int i = 0; i < beaufortScale.Length; i++)
{
    if (windSpeed <= beaufortScale[i] || i == 12)
    {
        Debug.WriteLine($"The current wind speed ({windSpeed} m/s) the equivalent to Beaufort number {i} on the Beaufort scale");
        break;
    }
}
```

---
### HasAsyncInstallFinished

`_HAS_ASYNC_INSTALL_FINISHED` · hash `0x14832BF2ABA53FC5` · **Cliente**

```lua
local retval = HasAsyncInstallFinished()
```
```c
BOOL _HAS_ASYNC_INSTALL_FINISHED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Hardcoded to always return true.
```

**Nombres antiguos (alias):** `0x14832BF2ABA53FC5` (`N_0x14832bf2aba53fc5`)

---
### HasBulletImpactedInArea

`HAS_BULLET_IMPACTED_IN_AREA` · hash `0x9870ACFB89A90995` · jhash `0x902BC7D9` · **Cliente**

```lua
local retval = HasBulletImpactedInArea(x, y, z, p3, p4, p5)
```
```c
BOOL HAS_BULLET_IMPACTED_IN_AREA(float x, float y, float z, float p3, BOOL p4, BOOL p5);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`float`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p3 - possibly radius?  
```

---
### HasBulletImpactedInBox

`HAS_BULLET_IMPACTED_IN_BOX` · hash `0xDC8C5D7CFEAB8394` · jhash `0x2C2618CC` · **Cliente**

```lua
local retval = HasBulletImpactedInBox(p0, p1, p2, p3, p4, p5, p6, p7)
```
```c
BOOL HAS_BULLET_IMPACTED_IN_BOX(float p0, float p1, float p2, float p3, float p4, float p5, BOOL p6, BOOL p7);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)

**Devuelve:** `BOOL`

---
### HasButtonCombinationJustBeenEntered

`_HAS_BUTTON_COMBINATION_JUST_BEEN_ENTERED` · hash `0x071E2A839DE82D90` · jhash `0xFF6191E1` · **Cliente**

```lua
local retval = HasButtonCombinationJustBeenEntered(hash, amount)
```
```c
BOOL _HAS_BUTTON_COMBINATION_JUST_BEEN_ENTERED(Hash hash, int amount);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `amount` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This native appears on the cheat_controller script and tracks a combination of buttons, which may be used to toggle cheats in-game. Credits to ThreeSocks for the info. The hash contains the combination, while the "amount" represents the amount of buttons used in a combination. 
INT_SCORES_SCORTED was a hash collision
```

**Nombres antiguos (alias):** `0x071E2A839DE82D90` (`N_0x071e2a839de82d90`)

---
### HasCheatStringJustBeenEntered

`_HAS_CHEAT_STRING_JUST_BEEN_ENTERED` · hash `0x557E43C447E700A8` · **Cliente**

```lua
local retval = HasCheatStringJustBeenEntered(hash)
```
```c
BOOL _HAS_CHEAT_STRING_JUST_BEEN_ENTERED(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Get inputted "Cheat code", for example:
while (TRUE)
{
    if (MISC::_557E43C447E700A8(${fugitive}))
    {
       // Do something.
    }
    SYSTEM::WAIT(0);
}
Calling this will also set the last saved string hash to zero.
```

**Nombres antiguos (alias):** `0x557E43C447E700A8` (`N_0x557e43c447e700a8`)

---
### HasResumedFromSuspend

`_HAS_RESUMED_FROM_SUSPEND` · hash `0xE8B9C0EC9E183F35` · **Cliente**

```lua
local retval = HasResumedFromSuspend()
```
```c
BOOL _HAS_RESUMED_FROM_SUSPEND();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Hardcoded to return false.
```

**Nombres antiguos (alias):** `0xE8B9C0EC9E183F35` (`N_0xe8b9c0ec9e183f35`)

---
### HaveCreditsReachedEnd

`HAVE_CREDITS_REACHED_END` · hash `0x075F1D57402C93BA` · jhash `0x2569C9A7` · **Cliente**

```lua
local retval = HaveCreditsReachedEnd()
```
```c
BOOL HAVE_CREDITS_REACHED_END();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x075F1D57402C93BA` (`N_0x075f1d57402c93ba`)

---
### IgnoreNextRestart

`IGNORE_NEXT_RESTART` · hash `0x21FFB63D8C615361` · jhash `0xDA13A4B6` · **Cliente**

```lua
IgnoreNextRestart(toggle)
```
```c
void IGNORE_NEXT_RESTART(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### IsAreaOccupied

`IS_AREA_OCCUPIED` · hash `0xA61B4DF533DCB56E` · jhash `0xC013972F` · **Cliente**

```lua
local retval = IsAreaOccupied(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
```
```c
BOOL IS_AREA_OCCUPIED(float p0, float p1, float p2, float p3, float p4, float p5, BOOL p6, BOOL p7, BOOL p8, BOOL p9, BOOL p10, Any p11, BOOL p12);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`BOOL`)
- `p7` (`BOOL`)
- `p8` (`BOOL`)
- `p9` (`BOOL`)
- `p10` (`BOOL`)
- `p11` (`Any`)
- `p12` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsAussieVersion

`IS_AUSSIE_VERSION` · hash `0x9F1935CA1F724008` · jhash `0x944BA1DC` · **Cliente**

```lua
local retval = IsAussieVersion()
```
```c
BOOL IS_AUSSIE_VERSION();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
if (MISC::IS_AUSSIE_VERSION()) {
    sub_127a9(&l_31, 1024); // l_31 |= 1024
    l_129 = 3;
    sub_129d2("AUSSIE VERSION IS TRUE!?!?!"); // DEBUG
}
Used to block some of the prostitute stuff due to laws in Australia.
```

---
### IsAutoSaveInProgress

`IS_AUTO_SAVE_IN_PROGRESS` · hash `0x69240733738C19A0` · jhash `0x36F75399` · **Cliente**

```lua
local retval = IsAutoSaveInProgress()
```
```c
BOOL IS_AUTO_SAVE_IN_PROGRESS();
```

**Devuelve:** `BOOL`

---
### IsBitSet

`IS_BIT_SET` · hash `0xA921AA820C25702F` · jhash `0x902E26AC` · **Cliente**

```lua
local retval = IsBitSet(address, offset)
```
```c
BOOL IS_BIT_SET(int address, int offset);
```

**Parámetros**

- `address` (`int`)
- `offset` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns bit's boolean state from [offset] of [address].
Example:
MISC::IS_BIT_SET(bitAddress, 1);
To enable and disable bits, see:
MISC::SET_BIT(&bitAddress, 1);   // enable
MISC::CLEAR_BIT(&bitAddress, 1); // disable
```

---
### IsBulletInAngledArea

`IS_BULLET_IN_ANGLED_AREA` · hash `0x1A8B5F3C01E2B477` · jhash `0xE2DB58F7` · **Cliente**

```lua
local retval = IsBulletInAngledArea(x1, y1, z1, x2, y2, z2, width, ownedByPlayer)
```
```c
BOOL IS_BULLET_IN_ANGLED_AREA(float x1, float y1, float z1, float x2, float y2, float z2, float width, BOOL ownedByPlayer);
```

**Parámetros**

- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL` — True if a bullet, as maintained by a pool within CWeaponManager, has been fired into the defined angled area.

**Descripción oficial:**

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

For projectiles, see: [`IS_PROJECTILE_TYPE_IN_ANGLED_AREA`](#isprojectiletypeinangledarea)

---
### IsBulletInArea

`IS_BULLET_IN_AREA` · hash `0x3F2023999AD51C1F` · jhash `0xB54F46CA` · **Cliente**

```lua
local retval = IsBulletInArea(x, y, z, radius, ownedByPlayer)
```
```c
BOOL IS_BULLET_IN_AREA(float x, float y, float z, float radius, BOOL ownedByPlayer);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsBulletInBox

`IS_BULLET_IN_BOX` · hash `0xDE0F6D7450D37351` · jhash `0xAB73ED26` · **Cliente**

```lua
local retval = IsBulletInBox(x1, y1, z1, x2, y2, z2, ownedByPlayer)
```
```c
BOOL IS_BULLET_IN_BOX(float x1, float y1, float z1, float x2, float y2, float z2, BOOL ownedByPlayer);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

---
### IsCommandLineBenchmarkValueSet

`_IS_COMMAND_LINE_BENCHMARK_VALUE_SET` · hash `0xA049A5BE0F04F2F8` · **Cliente**

```lua
local retval = IsCommandLineBenchmarkValueSet()
```
```c
BOOL _IS_COMMAND_LINE_BENCHMARK_VALUE_SET();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if command line option '-benchmark' is set.
```

**Nombres antiguos (alias):** `0xA049A5BE0F04F2F8` (`N_0xa049a5be0f04f2f8`)

---
### IsDurangoVersion

`IS_DURANGO_VERSION` · hash `0x4D982ADB1978442D` · jhash `0x46FB06A5` · **Cliente**

```lua
local retval = IsDurangoVersion()
```
```c
BOOL IS_DURANGO_VERSION();
```

**Devuelve:** `BOOL` — Hard-coded to always return 0.

---
### IsFrontendFading

`IS_FRONTEND_FADING` · hash `0x7EA2B6AF97ECA6ED` · jhash `0x8FF6232C` · **Cliente**

```lua
local retval = IsFrontendFading()
```
```c
BOOL IS_FRONTEND_FADING();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function is hard-coded to always return 0.  
```

---
### IsInPowerSavingMode

`_IS_IN_POWER_SAVING_MODE` · hash `0x684A41975F077262` · **Cliente**

```lua
local retval = IsInPowerSavingMode()
```
```c
BOOL _IS_IN_POWER_SAVING_MODE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
aka "constrained"
```

**Nombres antiguos (alias):** `0x684A41975F077262` (`N_0x684a41975f077262`)

---
### IsIncidentValid

`IS_INCIDENT_VALID` · hash `0xC8BC6461E629BEAA` · jhash `0x31FD0BA4` · **Cliente**

```lua
local retval = IsIncidentValid(incidentId)
```
```c
BOOL IS_INCIDENT_VALID(int incidentId);
```

**Parámetros**

- `incidentId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
=======================================================  
Correction, I have change this to int, instead of int*  
as it doesn't use a pointer to the createdIncident.  
If you try it you will crash (or) freeze.  
=======================================================  
```

---
### IsJapaneseVersion

`IS_JAPANESE_VERSION` · hash `0xB8C0BB75D8A77DB3` · **Cliente**

```lua
local retval = IsJapaneseVersion()
```
```c
BOOL IS_JAPANESE_VERSION();
```

**Devuelve:** `BOOL` — Returns `true` when GTA:V is running with the Japanese executable.

**Descripción oficial:**

```
NativeDB Introduced: 2545
```

---
### IsMemoryCardInUse

`IS_MEMORY_CARD_IN_USE` · hash `0x8A75CE2956274ADD` · jhash `0x40CE4DFD` · **Cliente**

```lua
local retval = IsMemoryCardInUse()
```
```c
BOOL IS_MEMORY_CARD_IN_USE();
```

**Devuelve:** `BOOL`

---
### IsMinigameInProgress

`IS_MINIGAME_IN_PROGRESS` · hash `0x2B4A15E44DE0F478` · jhash `0x53A95E13` · **Cliente**

```lua
local retval = IsMinigameInProgress()
```
```c
BOOL IS_MINIGAME_IN_PROGRESS();
```

**Devuelve:** `BOOL`

---
### IsNextWeatherType

`IS_NEXT_WEATHER_TYPE` · hash `0x2FAA3A30BEC0F25D` · jhash `0x99CB167F` · **Cliente**

```lua
local retval = IsNextWeatherType(weatherType)
```
```c
BOOL IS_NEXT_WEATHER_TYPE(char* weatherType);
```

**Parámetros**

- `weatherType` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

---
### IsOrbisVersion

`IS_ORBIS_VERSION` · hash `0xA72BC0B675B1519E` · jhash `0x40282018` · **Cliente**

```lua
local retval = IsOrbisVersion()
```
```c
BOOL IS_ORBIS_VERSION();
```

**Devuelve:** `BOOL` — Hard-coded to always return 0.

---
### IsPcVersion

`IS_PC_VERSION` · hash `0x48AF36444B965238` · jhash `0x4D5D9EE3` · **Cliente**

```lua
local retval = IsPcVersion()
```
```c
BOOL IS_PC_VERSION();
```

**Devuelve:** `BOOL` — Hard-coded to always return 1.

---
### IsPointObscuredByAMissionEntity

`IS_POINT_OBSCURED_BY_A_MISSION_ENTITY` · hash `0xE54E209C35FFA18D` · jhash `0xC161558D` · **Cliente**

```lua
local retval = IsPointObscuredByAMissionEntity(p0, p1, p2, p3, p4, p5, p6)
```
```c
BOOL IS_POINT_OBSCURED_BY_A_MISSION_ENTITY(float p0, float p1, float p2, float p3, float p4, float p5, Any p6);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`Any`)

**Devuelve:** `BOOL`

---
### IsPopMultiplierAreaUnk

`_IS_POP_MULTIPLIER_AREA_UNK` · hash `0x1312F4B242609CE3` · **Cliente**

```lua
local retval = IsPopMultiplierAreaUnk(id)
```
```c
BOOL _IS_POP_MULTIPLIER_AREA_UNK(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### IsPositionOccupied

`IS_POSITION_OCCUPIED` · hash `0xADCDE75E1C60F32D` · jhash `0x452E8D9E` · **Cliente**

```lua
local retval = IsPositionOccupied(x, y, z, range, p4, checkVehicles, checkPeds, p7, p8, ignoreEntity, p10)
```
```c
BOOL IS_POSITION_OCCUPIED(float x, float y, float z, float range, BOOL p4, BOOL checkVehicles, BOOL checkPeds, BOOL p7, BOOL p8, Entity ignoreEntity, BOOL p10);
```

**Parámetros**

- `x` (`float`): X coordinate of the position to check.
- `y` (`float`): Y coordinate of the position to check.
- `z` (`float`): Z coordinate of the position to check.
- `range` (`float`): The range, seems to not be very accurate during testing.
- `p4` (`BOOL`): Unknown, when set to true it seems to always return true no matter what I try.
- `checkVehicles` (`BOOL`): Check for any vehicles in that area.
- `checkPeds` (`BOOL`): Check for any peds in that area.
- `p7` (`BOOL`): Unknown.
- `p8` (`BOOL`): Unknown.
- `ignoreEntity` (`Entity`): This entity will be ignored if it's in the area. Set to 0 if you don't want to exclude any entities.
- `p10` (`BOOL`): Unknown.

**Devuelve:** `BOOL` — Returns true if there is anything in that location matching the provided parameters.

**Descripción oficial:**

The BOOL parameters that are documented have not been confirmed. They are just documented from what I've found during testing. They may not work as expected in all cases.

---
### IsPrevWeatherType

`IS_PREV_WEATHER_TYPE` · hash `0x44F28F86433B10A9` · jhash `0x250ADA61` · **Cliente**

```lua
local retval = IsPrevWeatherType(weatherType)
```
```c
BOOL IS_PREV_WEATHER_TYPE(char* weatherType);
```

**Parámetros**

- `weatherType` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

---
### IsProjectileInArea

`IS_PROJECTILE_IN_AREA` · hash `0x5270A8FBC098C3F8` · jhash `0x78E1A557` · **Cliente**

```lua
local retval = IsProjectileInArea(x1, y1, z1, x2, y2, z2, ownedByPlayer)
```
```c
BOOL IS_PROJECTILE_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2, BOOL ownedByPlayer);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Determines whether there is a projectile within the specified coordinates. The coordinates form a rectangle.  
ownedByPlayer = only projectiles fired by the player will be detected.  
```

---
### IsProjectileTypeInAngledArea

`IS_PROJECTILE_TYPE_IN_ANGLED_AREA` · hash `0xF0BC12401061DEA0` · jhash `0xD1AE2681` · **Cliente**

```lua
local retval = IsProjectileTypeInAngledArea(x1, y1, z1, x2, y2, z2, width, p7, weaponHash, ownedByPlayer)
```
```c
BOOL IS_PROJECTILE_TYPE_IN_ANGLED_AREA(float x1, float y1, float z1, float x2, float y2, float z2, float width, float p7, Hash weaponHash, BOOL ownedByPlayer);
```

**Parámetros**

- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area
- `p7` (`float`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

```
NativeDB Removed Parameter 7: float p7
```

---
### IsProjectileTypeInArea

`IS_PROJECTILE_TYPE_IN_AREA` · hash `0x2E0DC353342C4A6D` · jhash `0x2B73BCF6` · **Cliente**

```lua
local retval = IsProjectileTypeInArea(x1, y1, z1, x2, y2, z2, type, ownedByPlayer)
```
```c
BOOL IS_PROJECTILE_TYPE_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2, int type, BOOL ownedByPlayer);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `type` (`int`)
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Determines whether there is a projectile of a specific type within the specified coordinates. The coordinates form a axis-aligned bounding box.  
```

---
### IsProjectileTypeWithinDistance

`IS_PROJECTILE_TYPE_WITHIN_DISTANCE` · hash `0x34318593248C8FB2` · jhash `0xBE81F1E2` · **Cliente**

```lua
local retval = IsProjectileTypeWithinDistance(x, y, z, projHash, radius, ownedByPlayer)
```
```c
BOOL IS_PROJECTILE_TYPE_WITHIN_DISTANCE(float x, float y, float z, Hash projHash, float radius, BOOL ownedByPlayer);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `projHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `radius` (`float`)
- `ownedByPlayer` (`BOOL`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x34318593248C8FB2` (`N_0x34318593248c8fb2`), `_IS_PROJECTILE_TYPE_IN_RADIUS` (`IsProjectileTypeInRadius`)

---
### IsPs3Version

`IS_PS3_VERSION` · hash `0xCCA1072C29D096C2` · jhash `0x4C0D5303` · **Cliente**

```lua
local retval = IsPs3Version()
```
```c
BOOL IS_PS3_VERSION();
```

**Devuelve:** `BOOL` — Hard-coded to always return 0.

---
### IsSniperBulletInArea

`IS_SNIPER_BULLET_IN_AREA` · hash `0xFEFCF11B01287125` · jhash `0x0483715C` · **Cliente**

```lua
local retval = IsSniperBulletInArea(x1, y1, z1, x2, y2, z2)
```
```c
BOOL IS_SNIPER_BULLET_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2);
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
Determines whether there is a sniper bullet within the specified coordinates. The coordinates form an axis-aligned bounding box.  
```

---
### IsSniperInverted

`IS_SNIPER_INVERTED` · hash `0x61A23B7EDA9BDA24` · jhash `0x5C3BF51B` · **Cliente**

```lua
local retval = IsSniperInverted()
```
```c
BOOL IS_SNIPER_INVERTED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function is hard-coded to always return 0.  
```

---
### IsSteamVersion

`IS_STEAM_VERSION` · hash `0x0A27B2B6282F7169` · **Cliente**

```lua
local retval = IsSteamVersion()
```
```c
BOOL IS_STEAM_VERSION();
```

**Devuelve:** `BOOL` — Returns `true` when GTA:V is running with the Steam executable.

**Descripción oficial:**

```
NativeDB Introduced: 2545
```

---
### IsStringNull

`IS_STRING_NULL` · hash `0xF22B6C47C6EAB066` · jhash `0x8E71E00F` · **Cliente**

```lua
local retval = IsStringNull(string)
```
```c
BOOL IS_STRING_NULL(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `BOOL`

---
### IsStringNullOrEmpty

`IS_STRING_NULL_OR_EMPTY` · hash `0xCA042B6957743895` · jhash `0x42E9F2CA` · **Cliente**

```lua
local retval = IsStringNullOrEmpty(string)
```
```c
BOOL IS_STRING_NULL_OR_EMPTY(char* string);
```

**Parámetros**

- `string` (`char*`)

**Devuelve:** `BOOL`

---
### IsStuntJumpInProgress

`IS_STUNT_JUMP_IN_PROGRESS` · hash `0x7A3F19700A4D0525` · jhash `0xF477D0B1` · **Cliente**

```lua
local retval = IsStuntJumpInProgress()
```
```c
BOOL IS_STUNT_JUMP_IN_PROGRESS();
```

**Devuelve:** `BOOL`

---
### IsStuntJumpMessageShowing

`IS_STUNT_JUMP_MESSAGE_SHOWING` · hash `0x2272B0A1343129F4` · jhash `0x021636EE` · **Cliente**

```lua
local retval = IsStuntJumpMessageShowing()
```
```c
BOOL IS_STUNT_JUMP_MESSAGE_SHOWING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2272B0A1343129F4` (`N_0x2272b0a1343129f4`)

---
### IsTennisMode

`IS_TENNIS_MODE` · hash `0x5D5479D115290C3F` · jhash `0x04A947BA` · **Cliente**

```lua
local retval = IsTennisMode(ped)
```
```c
BOOL IS_TENNIS_MODE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

---
### IsThisAMinigameScript

`IS_THIS_A_MINIGAME_SCRIPT` · hash `0x7B30F65D7B710098` · jhash `0x7605EF6F` · **Cliente**

```lua
local retval = IsThisAMinigameScript()
```
```c
BOOL IS_THIS_A_MINIGAME_SCRIPT();
```

**Devuelve:** `BOOL`

---
### IsXbox360Version

`IS_XBOX360_VERSION` · hash `0xF6201B4DAF662A9D` · jhash `0x24005CC8` · **Cliente**

```lua
local retval = IsXbox360Version()
```
```c
BOOL IS_XBOX360_VERSION();
```

**Devuelve:** `BOOL` — Hard-coded to always return 0.

---
### LandingMenuIsActive

`_LANDING_MENU_IS_ACTIVE` · hash `0x3BBBD13E5041A79E` · **Cliente**

```lua
local retval = LandingMenuIsActive()
```
```c
BOOL _LANDING_MENU_IS_ACTIVE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the current frontend menu is FE_MENU_VERSION_LANDING_MENU
```

**Nombres antiguos (alias):** `0x3BBBD13E5041A79E` (`N_0x3bbbd13e5041a79e`)

---
### LoadCloudHat

`LOAD_CLOUD_HAT` · hash `0xFC4842A34657BFCB` · jhash `0xED88FC61` · **Cliente**

```lua
LoadCloudHat(name, transitionTime)
```
```c
void LOAD_CLOUD_HAT(char* name, float transitionTime);
```

**Parámetros**

- `name` (`char*`)
- `transitionTime` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
The following cloudhats are useable:
altostratus
Cirrus
cirrocumulus
Clear 01
Cloudy 01
Contrails
Horizon
horizonband1
horizonband2
horizonband3
horsey
Nimbus
Puffs
RAIN
Snowy 01
Stormy 01
stratoscumulus
Stripey
shower
Wispy
```

**Nombres antiguos (alias):** `_SET_CLOUD_HAT_TRANSITION` (`SetCloudHatTransition`)

---
### N_0x06462a961e94b67c

`0x06462A961E94B67C` · hash `0x06462A961E94B67C` · jhash `0x5A45B11A` · **Cliente**

```lua
N_0x06462a961e94b67c()
```
```c
void 0x06462A961E94B67C();
```

**Devuelve:** `void`

**Descripción oficial:**

```
CLEAR_*
```

---
### N_0x1178e104409fe58c

`0x1178E104409FE58C` · hash `0x1178E104409FE58C` · **Cliente**

```lua
N_0x1178e104409fe58c(p0, p1)
```
```c
void 0x1178E104409FE58C(Any p0, Any p1);
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
### N_0x19bfed045c647c49

`0x19BFED045C647C49` · hash `0x19BFED045C647C49` · jhash `0x1A332D2D` · **Cliente**

```lua
local retval = N_0x19bfed045c647c49(ped)
```
```c
BOOL 0x19BFED045C647C49(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
GET_TENNIS_*; references 0xFBFEC0E9 = interruptswing
```

---
### N_0x2107a3773771186d

`0x2107A3773771186D` · hash `0x2107A3773771186D` · jhash `0x78350773` · **Cliente**

```lua
local retval = N_0x2107a3773771186d()
```
```c
BOOL 0x2107A3773771186D();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
HAS_*
```

---
### N_0x21c235bc64831e5a

`0x21C235BC64831E5A` · hash `0x21C235BC64831E5A` · jhash `0xCAECF37E` · **Cliente**

```lua
local retval = N_0x21c235bc64831e5a(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
Vector3 0x21C235BC64831E5A(float p0, float p1, float p2, float p3, float p4, float p5, float p6, float p7, float p8, BOOL p9);
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
- `p8` (`float`)
- `p9` (`BOOL`)

**Devuelve:** `Vector3`

**Descripción oficial:**

```
GET_C*
```

---
### N_0x23227df0b2115469

`0x23227DF0B2115469` · hash `0x23227DF0B2115469` · **Cliente**

```lua
N_0x23227df0b2115469()
```
```c
void 0x23227DF0B2115469();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x31125fd509d9043f

`0x31125FD509D9043F` · hash `0x31125FD509D9043F` · **Cliente**

```lua
local p0 = N_0x31125fd509d9043f(p0)
```
```c
void 0x31125FD509D9043F(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x39455bf4f4f55186

`0x39455BF4F4F55186` · hash `0x39455BF4F4F55186` · **Cliente**

```lua
local retval = N_0x39455bf4f4f55186(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12)
```
```c
Any 0x39455BF4F4F55186(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9, Any p10, Any p11, Any p12);
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

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### N_0x397baa01068baa96

`0x397BAA01068BAA96` · hash `0x397BAA01068BAA96` · jhash `0x39771F21` · **Cliente**

```lua
local retval = N_0x397baa01068baa96()
```
```c
int 0x397BAA01068BAA96();
```

**Devuelve:** `int`

---
### N_0x48f069265a0e4bec

`0x48F069265A0E4BEC` · hash `0x48F069265A0E4BEC` · jhash `0xF91B8C33` · **Cliente**

```lua
local p0 = N_0x48f069265a0e4bec(name)
```
```c
void 0x48F069265A0E4BEC(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only found 3 times in decompiled scripts. Not a whole lot to go off of.
MISC::_48F069265A0E4BEC(a_0, "Movie_Name_For_This_Player");
MISC::_48F069265A0E4BEC(&a_0._fB, "Ringtone_For_This_Player");
MISC::_48F069265A0E4BEC(&a_0._f1EC4._f12[v_A/*6*/], &v_13); // where v_13 is "MPATMLOGSCRS0" thru "MPATMLOGSCRS15"
```

---
### N_0x54f157e0336a3822

`0x54F157E0336A3822` · hash `0x54F157E0336A3822` · jhash `0x49F977A9` · **Cliente**

```lua
N_0x54f157e0336a3822(ped, p1, p2)
```
```c
void 0x54F157E0336A3822(Ped ped, char* p1, float p2);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`char*`)
- `p2` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
From the scripts:
MISC::_54F157E0336A3822(sub_aa49(a_0), "ForcedStopDirection", v_E);
Related to tennis mode.
SET_*
```

---
### N_0x5b1f2e327b6b6fe1

`0x5B1F2E327B6B6FE1` · hash `0x5B1F2E327B6B6FE1` · jhash `0x50C39926` · **Cliente**

```lua
local retval = N_0x5b1f2e327b6b6fe1()
```
```c
Any 0x5B1F2E327B6B6FE1();
```

**Devuelve:** `Any`

---
### N_0x65d2ebb47e1cec21

`0x65D2EBB47E1CEC21` · hash `0x65D2EBB47E1CEC21` · **Cliente**

```lua
N_0x65d2ebb47e1cec21(toggle)
```
```c
void 0x65D2EBB47E1CEC21(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets GtaThread+0x14A

SET_S*
```

---
### N_0x693478acbd7f18e7

`0x693478ACBD7F18E7` · hash `0x693478ACBD7F18E7` · **Cliente**

```lua
N_0x693478acbd7f18e7()
```
```c
void 0x693478ACBD7F18E7();
```

**Devuelve:** `void`

---
### N_0x6f2135b6129620c1

`0x6F2135B6129620C1` · hash `0x6F2135B6129620C1` · jhash `0x8B2DE971` · **Cliente**

```lua
N_0x6f2135b6129620c1(toggle)
```
```c
void 0x6F2135B6129620C1(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets bit 3 in GtaThread+0x150

SET_T*
```

---
### N_0x6fddf453c0c756ec

`0x6FDDF453C0C756EC` · hash `0x6FDDF453C0C756EC` · jhash `0xC3C10FCC` · **Cliente**

```lua
local retval = N_0x6fddf453c0c756ec()
```
```c
BOOL 0x6FDDF453C0C756EC();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
HAS_*
Probably something like "has game been started for the first time".
```

---
### N_0x703cc7f60cbb2b57

`0x703CC7F60CBB2B57` · hash `0x703CC7F60CBB2B57` · **Cliente**

```lua
N_0x703cc7f60cbb2b57(p0)
```
```c
void 0x703CC7F60CBB2B57(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x7ec6f9a478a6a512

`0x7EC6F9A478A6A512` · hash `0x7EC6F9A478A6A512` · **Cliente**

```lua
N_0x7ec6f9a478a6a512()
```
```c
void 0x7EC6F9A478A6A512();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Possibly used to clear scenario points.

CLEAR_*
```

---
### N_0x7f8f6405f4777af6

`0x7F8F6405F4777AF6` · hash `0x7F8F6405F4777AF6` · jhash `0x89459F0A` · **Cliente**

```lua
local retval = N_0x7f8f6405f4777af6(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9)
```
```c
float 0x7F8F6405F4777AF6(float p0, float p1, float p2, float p3, float p4, float p5, float p6, float p7, float p8, BOOL p9);
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
- `p8` (`float`)
- `p9` (`BOOL`)

**Devuelve:** `float`

---
### N_0x8269816f6cfd40f8

`0x8269816F6CFD40F8` · hash `0x8269816F6CFD40F8` · jhash `0x74E8FAD9` · **Cliente**

```lua
local p0 = N_0x8269816f6cfd40f8(name)
```
```c
void 0x8269816F6CFD40F8(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only found 2 times in decompiled scripts. Not a whole lot to go off of.
MISC::_8269816F6CFD40F8(&a_0._f1F5A._f6[0/*8*/], "TEMPSTAT_LABEL"); // gets saved in a struct called "g_SaveData_STRING_ScriptSaves"
MISC::_8269816F6CFD40F8(&a_0._f4B4[v_1A/*8*/], &v_5); // where v_5 is "Name0" thru "Name9", gets saved in a struct called "OUTFIT_Name"
```

---
### N_0x8951eb9c6906d3c8

`0x8951EB9C6906D3C8` · hash `0x8951EB9C6906D3C8` · **Cliente**

```lua
N_0x8951eb9c6906d3c8()
```
```c
void 0x8951EB9C6906D3C8();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x8d74e26f54b4e5c3

`0x8D74E26F54B4E5C3` · hash `0x8D74E26F54B4E5C3` · jhash `0xE77199F7` · **Cliente**

```lua
N_0x8d74e26f54b4e5c3(p0)
```
```c
void 0x8D74E26F54B4E5C3(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
I*
```

---
### N_0x916ca67d26fd1e37

`0x916CA67D26FD1E37` · hash `0x916CA67D26FD1E37` · **Cliente**

```lua
N_0x916ca67d26fd1e37(p0)
```
```c
void 0x916CA67D26FD1E37(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Does nothing (it's a nullsub). Seems to be PS4 specific.

```
NativeDB Introduced: v2060
```

---
### N_0x97e7e2c04245115b

`0x97E7E2C04245115B` · hash `0x97E7E2C04245115B` · **Cliente**

```lua
N_0x97e7e2c04245115b(p0)
```
```c
void 0x97E7E2C04245115B(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xa0ad167e4b39d9a2

`0xA0AD167E4B39D9A2` · hash `0xA0AD167E4B39D9A2` · **Cliente**

```lua
local retval = N_0xa0ad167e4b39d9a2(p0, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p13)
```
```c
Any 0xA0AD167E4B39D9A2(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6, Any p7, Any p8, Any p9, Any p10, Any p11, Any p12, Any p13);
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

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xa4a0065e39c9f25c

`0xA4A0065E39C9F25C` · hash `0xA4A0065E39C9F25C` · jhash `0xC4D71AB4` · **Cliente**

```lua
local retval, p0, p1, fadeInAfterLoad, p3 = N_0xa4a0065e39c9f25c()
```
```c
BOOL 0xA4A0065E39C9F25C(Vector3* p0, float* p1, BOOL* fadeInAfterLoad, BOOL* p3);
```

**Parámetros**

- `p0` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `fadeInAfterLoad` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
GET_SAVE_*

GET_SAVE_UNLESS_CUSTOM_DOT ?
```

---
### N_0xb51b9ab9ef81868c

`0xB51B9AB9EF81868C` · hash `0xB51B9AB9EF81868C` · jhash `0x75B06B5A` · **Cliente**

```lua
N_0xb51b9ab9ef81868c(toggle)
```
```c
void 0xB51B9AB9EF81868C(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### N_0xba4b8d83bdc75551

`0xBA4B8D83BDC75551` · hash `0xBA4B8D83BDC75551` · **Cliente**

```lua
N_0xba4b8d83bdc75551(p0)
```
```c
void 0xBA4B8D83BDC75551(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xd10282b6e3751ba0

`0xD10282B6E3751BA0` · hash `0xD10282B6E3751BA0` · **Cliente**

```lua
local retval = N_0xd10282b6e3751ba0()
```
```c
Any 0xD10282B6E3751BA0();
```

**Devuelve:** `Any`

---
### N_0xd642319c54aadeb6

`0xD642319C54AADEB6` · hash `0xD642319C54AADEB6` · jhash `0xC58250F1` · **Cliente**

```lua
local retval = N_0xd642319c54aadeb6()
```
```c
Any 0xD642319C54AADEB6();
```

**Devuelve:** `Any`

---
### N_0xd9f692d349249528

`0xD9F692D349249528` · hash `0xD9F692D349249528` · jhash `0xE0C9307E` · **Cliente**

```lua
N_0xd9f692d349249528()
```
```c
void 0xD9F692D349249528();
```

**Devuelve:** `void`

**Descripción oficial:**

```
RESET_*
```

---
### N_0xe3d969d2785ffb5e

`0xE3D969D2785FFB5E` · hash `0xE3D969D2785FFB5E` · **Cliente**

```lua
N_0xe3d969d2785ffb5e()
```
```c
void 0xE3D969D2785FFB5E();
```

**Devuelve:** `void`

**Descripción oficial:**

```
sets something to 1  
```

---
### N_0xe532ec1a63231b4f

`0xE532EC1A63231B4F` · hash `0xE532EC1A63231B4F` · jhash `0xA0D8C749` · **Cliente**

```lua
N_0xe532ec1a63231b4f(p0, p1)
```
```c
void 0xE532EC1A63231B4F(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_*
```

---
### N_0xe95b0c7d5ba3b96b

`0xE95B0C7D5BA3B96B` · hash `0xE95B0C7D5BA3B96B` · **Cliente**

```lua
local retval = N_0xe95b0c7d5ba3b96b(ped)
```
```c
BOOL 0xE95B0C7D5BA3B96B(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Related to tennis mode. Checks for `0x0FCED5ADF = swung`

---
### N_0xeb078ca2b5e82add

`0xEB078CA2B5E82ADD` · hash `0xEB078CA2B5E82ADD` · **Cliente**

```lua
N_0xeb078ca2b5e82add(p0, p1)
```
```c
void 0xEB078CA2B5E82ADD(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xeb2104e905c6f2e9

`0xEB2104E905C6F2E9` · hash `0xEB2104E905C6F2E9` · **Cliente**

```lua
local retval = N_0xeb2104e905c6f2e9()
```
```c
Any 0xEB2104E905C6F2E9();
```

**Devuelve:** `Any`

---
### N_0xebd3205a207939ed

`0xEBD3205A207939ED` · hash `0xEBD3205A207939ED` · **Cliente**

```lua
local p0 = N_0xebd3205a207939ed(p0)
```
```c
void 0xEBD3205A207939ED(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0xfa3ffb0eebc288a3

`0xFA3FFB0EEBC288A3` · hash `0xFA3FFB0EEBC288A3` · **Cliente**

```lua
N_0xfa3ffb0eebc288a3(p0)
```
```c
void 0xFA3FFB0EEBC288A3(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2060
```

---
### N_0xfaa457ef263e8763

`0xFAA457EF263E8763` · hash `0xFAA457EF263E8763` · jhash `0x6B4335DD` · **Cliente**

```lua
local p0 = N_0xfaa457ef263e8763(name)
```
```c
void 0xFAA457EF263E8763(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Another unknown label type...
MISC::_FAA457EF263E8763(a_0, "Thumb_label");
MISC::_FAA457EF263E8763(&a_0._f10, "Photo_label");
MISC::_FAA457EF263E8763(a_0, "GXTlabel");
MISC::_FAA457EF263E8763(&a_0._f21, "StringComp");
MISC::_FAA457EF263E8763(&a_0._f43, "SecondStringComp");
MISC::_FAA457EF263E8763(&a_0._f53, "ThirdStringComp");
MISC::_FAA457EF263E8763(&a_0._f32, "SenderStringComp");
MISC::_FAA457EF263E8763(&a_0._f726[v_1A/*16*/], &v_20); // where v_20 is "LastJobTL_0_1" thru "LastJobTL_2_1", gets saved in a struct called "LAST_JobGamer_TL"
MISC::_FAA457EF263E8763(&a_0._f4B, "PAID_PLAYER");
MISC::_FAA457EF263E8763(&a_0._f5B, "RADIO_STATION");
```

---
### N_0xfb00ca71da386228

`0xFB00CA71DA386228` · hash `0xFB00CA71DA386228` · jhash `0x054EC103` · **Cliente**

```lua
N_0xfb00ca71da386228()
```
```c
void 0xFB00CA71DA386228();
```

**Devuelve:** `void`

---
### NetworkSetScriptIsSafeForNetworkGame

`NETWORK_SET_SCRIPT_IS_SAFE_FOR_NETWORK_GAME` · hash `0x9243BAC96D64C050` · jhash `0x878486CE` · **Cliente**

```lua
NetworkSetScriptIsSafeForNetworkGame()
```
```c
void NETWORK_SET_SCRIPT_IS_SAFE_FOR_NETWORK_GAME();
```

**Devuelve:** `void`

---
### NextOnscreenKeyboardResultWillDisplayUsingTheseFonts

`NEXT_ONSCREEN_KEYBOARD_RESULT_WILL_DISPLAY_USING_THESE_FONTS` · hash `0x3ED1438C1F5C6612` · jhash `0x3301EA47` · **Cliente**

```lua
NextOnscreenKeyboardResultWillDisplayUsingTheseFonts(fontBitField)
```
```c
void NEXT_ONSCREEN_KEYBOARD_RESULT_WILL_DISPLAY_USING_THESE_FONTS(int fontBitField);
```

**Parámetros**

- `fontBitField` (`int`): See the list above.

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eFontBitField
{
  FONT_BIT_STANDARD = 1,
  FONT_BIT_CURSIVE = 2,
  FONT_BIT_ROCKSTAR_TAG = 4
  FONT_BIT_LEADERBOARD = 8
  FONT_BIT_CONDENSED = 16
  FONT_BIT_FIXED_WIDTH_NUMBERS = 32
  FONT_BIT_CONDENSED_NOT_GAMERNAME = 64
  FONT_BIT_PRICEDOWN = 128
};
```

**Nombres antiguos (alias):** `0x3ED1438C1F5C6612` (`N_0x3ed1438c1f5c6612`)

---
### OverrideSaveHouse

`OVERRIDE_SAVE_HOUSE` · hash `0x1162EA8AE9D24EEA` · jhash `0x47436C12` · **Cliente**

```lua
local retval, p6, p7 = OverrideSaveHouse(p0, p1, p2, p3, p4, p5)
```
```c
BOOL OVERRIDE_SAVE_HOUSE(BOOL p0, float p1, float p2, float p3, float p4, BOOL p5, Vector3* p6, float* p7);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`BOOL`)
- `p6` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p7` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### PauseDeathArrestRestart

`PAUSE_DEATH_ARREST_RESTART` · hash `0x2C2B3493FBF51C71` · jhash `0x296574AE` · **Cliente**

```lua
PauseDeathArrestRestart(toggle)
```
```c
void PAUSE_DEATH_ARREST_RESTART(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_DISABLE_AUTOMATIC_RESPAWN` (`DisableAutomaticRespawn`)

---
### PlayTennisDiveAnim

`PLAY_TENNIS_DIVE_ANIM` · hash `0x8FA9C42FC5D7C64B` · jhash `0x0C8865DF` · **Cliente**

```lua
PlayTennisDiveAnim(ped, p1, p2, p3, p4, p5)
```
```c
void PLAY_TENNIS_DIVE_ANIM(Ped ped, int p1, float p2, float p3, float p4, BOOL p5);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`int`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8FA9C42FC5D7C64B` (`N_0x8fa9c42fc5d7c64b`)

---
### PlayTennisSwingAnim

`PLAY_TENNIS_SWING_ANIM` · hash `0xE266ED23311F24D4` · jhash `0xC20A7D2B` · **Cliente**

```lua
PlayTennisSwingAnim(ped, animDict, animName, p3, p4, p5)
```
```c
void PLAY_TENNIS_SWING_ANIM(Ped ped, char* animDict, char* animName, float p3, float p4, BOOL p5);
```

**Parámetros**

- `ped` (`Ped`)
- `animDict` (`char*`)
- `animName` (`char*`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE266ED23311F24D4` (`N_0xe266ed23311f24d4`)

---
### PopulateNow

`POPULATE_NOW` · hash `0x7472BB270D7B4F3E` · jhash `0x72C20700` · **Cliente**

```lua
PopulateNow()
```
```c
void POPULATE_NOW();
```

**Devuelve:** `void`

**Descripción oficial:**

```
spawns a few distant/out-of-sight peds, vehicles, animals etc each time it is called  
```

---
### PreloadCloudHat

`PRELOAD_CLOUD_HAT` · hash `0x11B56FBBF7224868` · jhash `0x8727A4C5` · **Cliente**

```lua
PreloadCloudHat(name)
```
```c
void PRELOAD_CLOUD_HAT(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Found in the scripts:
MISC::_11B56FBBF7224868("CONTRAILS");
```

**Nombres antiguos (alias):** `0x11B56FBBF7224868` (`N_0x11b56fbbf7224868`)

---
### QueueMissionRepeatLoad

`QUEUE_MISSION_REPEAT_LOAD` · hash `0x72DE52178C291CB5` · jhash `0xF62B3C48` · **Cliente**

```lua
local retval = QueueMissionRepeatLoad()
```
```c
BOOL QUEUE_MISSION_REPEAT_LOAD();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x72DE52178C291CB5` (`N_0x72de52178c291cb5`)

---
### QueueMissionRepeatSave

`QUEUE_MISSION_REPEAT_SAVE` · hash `0x44A0BDC559B35F6E` · jhash `0x3589452B` · **Cliente**

```lua
local retval = QueueMissionRepeatSave()
```
```c
BOOL QUEUE_MISSION_REPEAT_SAVE();
```

**Devuelve:** `BOOL` — Returns 1 if the message isn't currently on screen.

**Descripción oficial:**

Shows the screen which is visible before you redo a mission? The game will make a restoration point where you will cameback when the mission is over.

**Nombres antiguos (alias):** `0x44A0BDC559B35F6E` (`N_0x44a0bdc559b35f6e`)

---
### QuitGame

`QUIT_GAME` · hash `0xEB6891F03362FB12` · **Cliente**

```lua
QuitGame()
```
```c
void QUIT_GAME();
```

**Devuelve:** `void`

**Descripción oficial:**

Quits the game.

**Nombres antiguos (alias):** `0xEB6891F03362FB12` (`N_0xeb6891f03362fb12`), `_FORCE_SOCIAL_CLUB_UPDATE` (`ForceSocialClubUpdate`)

---
### RegisterBoolToSave

`REGISTER_BOOL_TO_SAVE` · hash `0xC8F4131414C835A1` · jhash `0x5417E0E0` · **Cliente**

```lua
local p0 = RegisterBoolToSave(name)
```
```c
void REGISTER_BOOL_TO_SAVE(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

---
### RegisterEnumToSave

`REGISTER_ENUM_TO_SAVE` · hash `0x10C2FA78D0E128A1` · jhash `0x9B38374A` · **Cliente**

```lua
local p0 = RegisterEnumToSave(name)
```
```c
void REGISTER_ENUM_TO_SAVE(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

---
### RegisterFloatToSave

`REGISTER_FLOAT_TO_SAVE` · hash `0x7CAEC29ECB5DFEBB` · jhash `0xDB06F7AD` · **Cliente**

```lua
local p0 = RegisterFloatToSave(name)
```
```c
void REGISTER_FLOAT_TO_SAVE(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

---
### RegisterInt64ToSave

`_REGISTER_INT64_TO_SAVE` · hash `0xA735353C77334EA0` · **Cliente**

```lua
local p0 = RegisterInt64ToSave(name)
```
```c
void _REGISTER_INT64_TO_SAVE(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA735353C77334EA0` (`N_0xa735353c77334ea0`)

---
### RegisterIntToSave

`REGISTER_INT_TO_SAVE` · hash `0x34C9EE5986258415` · jhash `0xB930956F` · **Cliente**

```lua
local p0 = RegisterIntToSave(name)
```
```c
void REGISTER_INT_TO_SAVE(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

---
### RegisterSaveHouse

`REGISTER_SAVE_HOUSE` · hash `0xC0714D0A7EEECA54` · jhash `0x39C1849A` · **Cliente**

```lua
local retval, p4 = RegisterSaveHouse(p0, p1, p2, p3, p5, p6)
```
```c
Any REGISTER_SAVE_HOUSE(float p0, float p1, float p2, float p3, Any* p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `Any`

---
### RegisterTextLabelToSave

`REGISTER_TEXT_LABEL_TO_SAVE` · hash `0xEDB1232C5BEAE62F` · jhash `0x284352C4` · **Cliente**

```lua
local p0 = RegisterTextLabelToSave(name)
```
```c
void REGISTER_TEXT_LABEL_TO_SAVE(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

---
### RegisterTextLabelToSave_2

`_REGISTER_TEXT_LABEL_TO_SAVE_2` · hash `0x6F7794F28C6B2535` · jhash `0xE2089749` · **Cliente**

```lua
local p0 = RegisterTextLabelToSave_2(name)
```
```c
void _REGISTER_TEXT_LABEL_TO_SAVE_2(Any* p0, char* name);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Seems to have the same functionality as REGISTER_TEXT_LABEL_TO_SAVE?
MISC::_6F7794F28C6B2535(&a_0._f1, "tlPlateText");
MISC::_6F7794F28C6B2535(&a_0._f1C, "tlPlateText_pending");
MISC::_6F7794F28C6B2535(&a_0._f10B, "tlCarAppPlateText");
"tl" prefix sounds like "Text Label"
```

**Nombres antiguos (alias):** `0x6F7794F28C6B2535` (`N_0x6f7794f28c6b2535`)

---
### RemoveDispatchSpawnBlockingArea

`REMOVE_DISPATCH_SPAWN_BLOCKING_AREA` · hash `0x264AC28B01B353A5` · jhash `0xA8D2FB92` · **Cliente**

```lua
RemoveDispatchSpawnBlockingArea(p0)
```
```c
void REMOVE_DISPATCH_SPAWN_BLOCKING_AREA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### RemovePopMultiplierArea

`REMOVE_POP_MULTIPLIER_AREA` · hash `0xB129E447A2EDA4BF` · jhash `0xFBDBE374` · **Cliente**

```lua
RemovePopMultiplierArea(id, p1)
```
```c
void REMOVE_POP_MULTIPLIER_AREA(int id, BOOL p1);
```

**Parámetros**

- `id` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB129E447A2EDA4BF` (`N_0xb129e447a2eda4bf`)

---
### RemovePopMultiplierSphere

`REMOVE_POP_MULTIPLIER_SPHERE` · hash `0xE6869BECDD8F2403` · jhash `0x92E7E4EB` · **Cliente**

```lua
RemovePopMultiplierSphere(id, p1)
```
```c
void REMOVE_POP_MULTIPLIER_SPHERE(int id, BOOL p1);
```

**Parámetros**

- `id` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE6869BECDD8F2403` (`N_0xe6869becdd8f2403`)

---
### RemoveStealthKill

`_REMOVE_STEALTH_KILL` · hash `0xA6A12939F16D85BE` · jhash `0x42B484ED` · **Cliente**

```lua
RemoveStealthKill(hash, p1)
```
```c
void _REMOVE_STEALTH_KILL(Hash hash, BOOL p1);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Appears to remove stealth kill action from memory
```

**Nombres antiguos (alias):** `0xA6A12939F16D85BE` (`N_0xa6a12939f16d85be`)

---
### ResetBenchmarkRecording

`_RESET_BENCHMARK_RECORDING` · hash `0x437138B6A830166A` · **Cliente**

```lua
ResetBenchmarkRecording()
```
```c
void _RESET_BENCHMARK_RECORDING();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Begins with RESET_*. Next character in the name is either D or E.
```

**Nombres antiguos (alias):** `0x437138B6A830166A` (`N_0x437138b6a830166a`)

---
### ResetDispatchIdealSpawnDistance

`RESET_DISPATCH_IDEAL_SPAWN_DISTANCE` · hash `0x77A84429DD9F0A15` · jhash `0xDA65ECAA` · **Cliente**

```lua
ResetDispatchIdealSpawnDistance()
```
```c
void RESET_DISPATCH_IDEAL_SPAWN_DISTANCE();
```

**Devuelve:** `void`

---
### ResetDispatchSpawnBlockingAreas

`RESET_DISPATCH_SPAWN_BLOCKING_AREAS` · hash `0xAC7BFD5C1D83EA75` · jhash `0x9A17F835` · **Cliente**

```lua
ResetDispatchSpawnBlockingAreas()
```
```c
void RESET_DISPATCH_SPAWN_BLOCKING_AREAS();
```

**Devuelve:** `void`

---
### ResetDispatchSpawnLocation

`_RESET_DISPATCH_SPAWN_LOCATION` · hash `0x5896F2BD5683A4E1` · **Cliente**

```lua
ResetDispatchSpawnLocation()
```
```c
void _RESET_DISPATCH_SPAWN_LOCATION();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### ResetDispatchTimeBetweenSpawnAttempts

`RESET_DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS` · hash `0xEB2DB0CAD13154B3` · jhash `0x1479E85A` · **Cliente**

```lua
ResetDispatchTimeBetweenSpawnAttempts(p0)
```
```c
void RESET_DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### RestartGame

`RESTART_GAME` · hash `0xE574A662ACAEFBB1` · **Cliente**

```lua
RestartGame()
```
```c
void RESTART_GAME();
```

**Devuelve:** `void`

**Descripción oficial:**

In singleplayer it does exactly what the name implies. In FiveM / GTA:Online it shows the `Disconnecting from GTA Online` warning screen message and quits the game.
After quitting, the game process is started again (as the name implies).

**Nombres antiguos (alias):** `0xE574A662ACAEFBB1` (`N_0xe574a662acaefbb1`), `_RESTART_GAME` (`RestartGame`)

---
### SaveBenchmarkRecording

`_SAVE_BENCHMARK_RECORDING` · hash `0x37DEB0AA183FB6D8` · **Cliente**

```lua
SaveBenchmarkRecording()
```
```c
void _SAVE_BENCHMARK_RECORDING();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Saves the benchmark recording to %USERPROFILE%\Documents\Rockstar Games\GTA V\Benchmarks and submits some metrics.
```

**Nombres antiguos (alias):** `0x37DEB0AA183FB6D8` (`N_0x37deb0aa183fb6d8`)

---
### ScriptRaceGetPlayerSplitTime

`SCRIPT_RACE_GET_PLAYER_SPLIT_TIME` · hash `0x8EF5573A1F801A5C` · jhash `0x07FF553F` · **Cliente**

```lua
local retval, p1, p2 = ScriptRaceGetPlayerSplitTime(player)
```
```c
BOOL SCRIPT_RACE_GET_PLAYER_SPLIT_TIME(Player player, int* p1, int* p2);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p2` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8EF5573A1F801A5C` (`N_0x8ef5573a1f801a5c`)

---
### ScriptRaceInit

`SCRIPT_RACE_INIT` · hash `0x0A60017F841A54F2` · jhash `0x2D33F15A` · **Cliente**

```lua
ScriptRaceInit(numCheckpoints, numLaps, numPlayers, localPlayer)
```
```c
void SCRIPT_RACE_INIT(int numCheckpoints, int numLaps, int numPlayers, Player localPlayer);
```

**Parámetros**

- `numCheckpoints` (`int`): The total number of checkpoints in the race
- `numLaps` (`int`): The total number of laps in the race.
- `numPlayers` (`int`): The total number of players participating in the race.
- `localPlayer` (`Player`): Local player in the race.

**Devuelve:** `void`

**Descripción oficial:**

Initializes a script race in GTA:Online and sets up the helper split time system.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x0A60017F841A54F2` (`N_0x0a60017f841a54f2`)

---
### ScriptRacePlayerHitCheckpoint

`SCRIPT_RACE_PLAYER_HIT_CHECKPOINT` · hash `0x1BB299305C3E8C13` · jhash `0xA27F4472` · **Cliente**

```lua
ScriptRacePlayerHitCheckpoint(ped, checkpoint, lap, time)
```
```c
void SCRIPT_RACE_PLAYER_HIT_CHECKPOINT(Ped ped, int checkpoint, int lap, int time);
```

**Parámetros**

- `ped` (`Ped`): The index of the Ped who hit the checkpoint.
- `checkpoint` (`int`): The checkpoint number that the player has passed.
- `lap` (`int`): The current lap that the player is on.
- `time` (`int`): The time it took for the player to reach this checkpoint from the start of the race or the last checkpoint.

**Devuelve:** `void`

**Descripción oficial:**

Records that a player has successfully passed a checkpoint during a scripted race in GTA:Online. This native should be used after initializing the race with [`SCRIPT_RACE_INIT`](#scriptraceinit).

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x1BB299305C3E8C13` (`N_0x1bb299305c3e8c13`)

---
### ScriptRaceShutdown

`SCRIPT_RACE_SHUTDOWN` · hash `0x1FF6BF9A63E5757F` · jhash `0xDF99925C` · **Cliente**

```lua
ScriptRaceShutdown()
```
```c
void SCRIPT_RACE_SHUTDOWN();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1FF6BF9A63E5757F` (`N_0x1ff6bf9a63e5757f`)

---
### SetBeastModeActive

`_SET_BEAST_MODE_ACTIVE` · hash `0x438822C279B73B93` · **Cliente**

```lua
SetBeastModeActive(player)
```
```c
void _SET_BEAST_MODE_ACTIVE(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x438822C279B73B93` (`N_0x438822c279b73b93`)

---
### SetBit

`SET_BIT` · hash `0x933D6A9EEC1BACD0` · jhash `0x4EFE7E6B` · **Cliente**

```lua
local address = SetBit(offset)
```
```c
void SET_BIT(int* address, int offset);
```

**Parámetros**

- `address` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `offset` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
This sets bit [offset] of [address] to on.
The offsets used are different bits to be toggled on and off, typically there is only one address used in a script.
Example:
MISC::SET_BIT(&bitAddress, 1);
To check if this bit has been enabled:
MISC::IS_BIT_SET(bitAddress, 1); // will return 1 afterwards
Please note, this method may assign a value to [address] when used.
```

---
### SetBitsInRange

`SET_BITS_IN_RANGE` · hash `0x8EF07E15701D61ED` · jhash `0x32094719` · **Cliente**

```lua
local var = SetBitsInRange(rangeStart, rangeEnd, p3)
```
```c
void SET_BITS_IN_RANGE(int* var, int rangeStart, int rangeEnd, int p3);
```

**Parámetros**

- `var` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `rangeStart` (`int`)
- `rangeEnd` (`int`)
- `p3` (`int`)

**Devuelve:** `void`

---
### SetCloudSettingsOverride

`SET_CLOUD_SETTINGS_OVERRIDE` · hash `0x02DEAAC8F8EA7FE7` · **Cliente**

```lua
SetCloudSettingsOverride(overrideSettingsName)
```
```c
void SET_CLOUD_SETTINGS_OVERRIDE(char* overrideSettingsName);
```

**Parámetros**

- `overrideSettingsName` (`char*`): The name of the cloud settings to use. Use a empty string to clear the override and return to the default settings.

**Devuelve:** `void`

**Descripción oficial:**

Overrides the cloud settings, which are normally controlled by the weather, with the specified named version. This native allows for custom cloud formations and behaviors that deviate from the default settings associated with the game's current weather conditions.

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `0x02DEAAC8F8EA7FE7` (`N_0x02deaac8f8ea7fe7`)

---
### SetCloudsAlpha

`SET_CLOUDS_ALPHA` · hash `0xF36199225D6D8C86` · **Cliente**

```lua
SetCloudsAlpha(opacity)
```
```c
void SET_CLOUDS_ALPHA(float opacity);
```

**Parámetros**

- `opacity` (`float`): The opacity value to set for clouds.

**Devuelve:** `void`

**Descripción oficial:**

Allows modification of the cloud opacity. It can also be used in other contexts, such as when the player is in a switch state [`IS_PLAYER_SWITCH_IN_PROGRESS`](STREAMING.md#isplayerswitchinprogress).

**Nombres antiguos (alias):** `0xF36199225D6D8C86` (`N_0xf36199225d6d8c86`), `_SET_CLOUD_HAT_OPACITY` (`SetCloudHatOpacity`)

**Ejemplo (lua):**

```lua
-- Check if the player is in a Switch "state"
if IsPlayerSwitchInProgress() then
    -- If the player is in a Switch state, set the clouds opacity to 1.0
    SetCloudsAlpha(1.0)
end
```

**Ejemplo (js):**

```js
// Check if the player is in a Switch "state"
if (IsPlayerSwitchInProgress()) {
    // If the player is in a Switch state, set the clouds opacity to 1.0
    SetCloudsAlpha(1.0);
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
// Check if the player is in a Switch "state"
if (IsPlayerSwitchInProgress()) {
    // If the player is in a Switch state, set the clouds opacity to 1.0
    SetCloudsAlpha(1f);
}
```

---
### SetCreditsActive

`SET_CREDITS_ACTIVE` · hash `0xB938B7E6D3C0620C` · jhash `0xEC2A0ECF` · **Cliente**

```lua
SetCreditsActive(toggle)
```
```c
void SET_CREDITS_ACTIVE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetDispatchIdealSpawnDistance

`SET_DISPATCH_IDEAL_SPAWN_DISTANCE` · hash `0x6FE601A64180D423` · jhash `0x6283BE32` · **Cliente**

```lua
SetDispatchIdealSpawnDistance(p0)
```
```c
void SET_DISPATCH_IDEAL_SPAWN_DISTANCE(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### SetDispatchSpawnLocation

`SET_DISPATCH_SPAWN_LOCATION` · hash `0xD10F442036302D50` · jhash `0x6F009E33` · **Cliente**

```lua
SetDispatchSpawnLocation(x, y, z)
```
```c
void SET_DISPATCH_SPAWN_LOCATION(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD10F442036302D50` (`N_0xd10f442036302d50`)

---
### SetDispatchTimeBetweenSpawnAttempts

`SET_DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS` · hash `0x44F7CBC1BEB3327D` · jhash `0xABADB709` · **Cliente**

```lua
SetDispatchTimeBetweenSpawnAttempts(p0, p1)
```
```c
void SET_DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS(Any p0, float p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)

**Devuelve:** `void`

---
### SetDispatchTimeBetweenSpawnAttemptsMultiplier

`SET_DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS_MULTIPLIER` · hash `0x48838ED9937A15D1` · jhash `0x1C996BCD` · **Cliente**

```lua
SetDispatchTimeBetweenSpawnAttemptsMultiplier(p0, p1)
```
```c
void SET_DISPATCH_TIME_BETWEEN_SPAWN_ATTEMPTS_MULTIPLIER(Any p0, float p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)

**Devuelve:** `void`

---
### SetExplosiveAmmoThisFrame

`SET_EXPLOSIVE_AMMO_THIS_FRAME` · hash `0xA66C71C98D5F2CFB` · jhash `0x2EAFA1D1` · **Cliente**

```lua
SetExplosiveAmmoThisFrame(player)
```
```c
void SET_EXPLOSIVE_AMMO_THIS_FRAME(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### SetExplosiveMeleeThisFrame

`SET_EXPLOSIVE_MELEE_THIS_FRAME` · hash `0xFF1BED81BFDC0FE0` · jhash `0x96663D56` · **Cliente**

```lua
SetExplosiveMeleeThisFrame(player)
```
```c
void SET_EXPLOSIVE_MELEE_THIS_FRAME(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### SetFadeInAfterDeathArrest

`SET_FADE_IN_AFTER_DEATH_ARREST` · hash `0xDA66D2796BA33F12` · jhash `0xACDE6985` · **Cliente**

```lua
SetFadeInAfterDeathArrest(toggle)
```
```c
void SET_FADE_IN_AFTER_DEATH_ARREST(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets whether the game should fade in after the player dies or is arrested.  
```

---
### SetFadeInAfterLoad

`SET_FADE_IN_AFTER_LOAD` · hash `0xF3D78F59DFE18D79` · jhash `0x6E00EB0B` · **Cliente**

```lua
SetFadeInAfterLoad(toggle)
```
```c
void SET_FADE_IN_AFTER_LOAD(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetFadeOutAfterArrest

`SET_FADE_OUT_AFTER_ARREST` · hash `0x1E0B4DC0D990A4E7` · jhash `0xCB074B9D` · **Cliente**

```lua
SetFadeOutAfterArrest(toggle)
```
```c
void SET_FADE_OUT_AFTER_ARREST(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets whether the game should fade out after the player is arrested.  
```

---
### SetFadeOutAfterDeath

`SET_FADE_OUT_AFTER_DEATH` · hash `0x4A18E01DF2C87B86` · jhash `0xC9F6F0BC` · **Cliente**

```lua
SetFadeOutAfterDeath(toggle)
```
```c
void SET_FADE_OUT_AFTER_DEATH(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets whether the game should fade out after the player dies.  
```

---
### SetFakeWantedLevel

`SET_FAKE_WANTED_LEVEL` · hash `0x1454F2448DE30163` · jhash `0x85B1C9FA` · **Cliente**

```lua
SetFakeWantedLevel(fakeWantedLevel)
```
```c
void SET_FAKE_WANTED_LEVEL(int fakeWantedLevel);
```

**Parámetros**

- `fakeWantedLevel` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets a visually fake wanted level on the user interface. Used by Rockstar's scripts to "override" regular wanted levels and make custom ones while the real wanted level and multipliers are still in effect.
Max is 6, anything above this makes it just 6. Also the mini-map gets the red & blue flashing effect.
```

---
### SetFireAmmoThisFrame

`SET_FIRE_AMMO_THIS_FRAME` · hash `0x11879CDD803D30F4` · jhash `0x7C18FC8A` · **Cliente**

```lua
SetFireAmmoThisFrame(player)
```
```c
void SET_FIRE_AMMO_THIS_FRAME(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

---
### SetForcePlayerToJump

`_SET_FORCE_PLAYER_TO_JUMP` · hash `0xA1183BCFEE0F93D1` · **Cliente**

```lua
SetForcePlayerToJump(player)
```
```c
void _SET_FORCE_PLAYER_TO_JUMP(Player player);
```

**Parámetros**

- `player` (`Player`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0xA1183BCFEE0F93D1` (`N_0xa1183bcfee0f93d1`)

---
### SetGamePaused

`SET_GAME_PAUSED` · hash `0x577D1284D6873711` · jhash `0x8230FF6C` · **Cliente**

```lua
SetGamePaused(toggle)
```
```c
void SET_GAME_PAUSED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Make sure to call this from the correct thread if you're using multiple threads because all other threads except the one which is calling SET_GAME_PAUSED will be paused which means you will lose control and the game remains in paused mode until you exit GTA5.exe  
```

---
### SetGravityLevel

`SET_GRAVITY_LEVEL` · hash `0x740E14FAD5842351` · jhash `0x2D833F4A` · **Cliente**

```lua
SetGravityLevel(level)
```
```c
void SET_GRAVITY_LEVEL(int level);
```

**Parámetros**

- `level` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eGravityLevel
{
    GRAV_EARTH = 0, // earth gravity 9.8m/s2
    GRAV_MOON = 1, // moon gravity 2.4m/s2
    GRAV_LOW = 2, // very low gravity
    GRAV_ZERO = 3 // zero gravity
}
```

---
### SetIncidentRequestedUnits

`SET_INCIDENT_REQUESTED_UNITS` · hash `0xB08B85D860E7BA3C` · jhash `0x0242D88E` · **Cliente**

```lua
SetIncidentRequestedUnits(incidentId, dispatchService, numUnits)
```
```c
void SET_INCIDENT_REQUESTED_UNITS(int incidentId, int dispatchService, int numUnits);
```

**Parámetros**

- `incidentId` (`int`)
- `dispatchService` (`int`)
- `numUnits` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB08B85D860E7BA3C` (`N_0xb08b85d860e7ba3c`)

---
### SetIncidentUnk

`_SET_INCIDENT_UNK` · hash `0xD261BA3E7E998072` · jhash `0x1F38102E` · **Cliente**

```lua
SetIncidentUnk(incidentId, p1)
```
```c
void _SET_INCIDENT_UNK(int incidentId, float p1);
```

**Parámetros**

- `incidentId` (`int`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_INCIDENT_*
```

**Nombres antiguos (alias):** `0xD261BA3E7E998072` (`N_0xd261ba3e7e998072`)

---
### SetInstancePriorityHint

`SET_INSTANCE_PRIORITY_HINT` · hash `0xC5F0A8EBD3F361CE` · jhash `0xE202879D` · **Cliente**

```lua
SetInstancePriorityHint(flag)
```
```c
void SET_INSTANCE_PRIORITY_HINT(int flag);
```

**Parámetros**

- `flag` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets an unknown flag used by CScene in determining which entities from CMapData scene nodes to draw, similar to SET_INSTANCE_PRIORITY_MODE.
```

**Nombres antiguos (alias):** `_SET_UNK_MAP_FLAG` (`SetUnkMapFlag`)

---
### SetInstancePriorityMode

`SET_INSTANCE_PRIORITY_MODE` · hash `0x9BAE5AD2508DF078` · jhash `0x721B2492` · **Cliente**

```lua
SetInstancePriorityMode(toggle)
```
```c
void SET_INSTANCE_PRIORITY_MODE(int toggle);
```

**Parámetros**

- `toggle` (`int`): toggles the instance priority mode

**Devuelve:** `void`

**Descripción oficial:**

Sets the maximum prop density and changes a loading screen flag from 'loading story mode' to 'loading GTA Online'. It causes a loading screen to show as it reloads map data.

**Nombres antiguos (alias):** `_ENABLE_MP_DLC_MAPS` (`EnableMpDlcMaps`), `_USE_FREEMODE_MAP_BEHAVIOR` (`UseFreemodeMapBehavior`), `_LOWER_MAP_PROP_DENSITY` (`LowerMapPropDensity`)

---
### SetMinigameInProgress

`SET_MINIGAME_IN_PROGRESS` · hash `0x19E00D7322C6F85B` · jhash `0x348B9046` · **Cliente**

```lua
SetMinigameInProgress(toggle)
```
```c
void SET_MINIGAME_IN_PROGRESS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetMissionFlag

`SET_MISSION_FLAG` · hash `0xC4301E5121A0ED73` · jhash `0x57592D52` · **Cliente**

```lua
SetMissionFlag(toggle)
```
```c
void SET_MISSION_FLAG(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If true, the player can't save the game.   
If the parameter is true, sets the mission flag to true, if the parameter is false, the function does nothing at all.  
^ also, if the mission flag is already set, the function does nothing at all  
```

---
### SetOverrideWeather

`SET_OVERRIDE_WEATHER` · hash `0xA43D5C6FE51ADBEF` · jhash `0xD9082BB5` · **Cliente**

```lua
SetOverrideWeather(weatherType)
```
```c
void SET_OVERRIDE_WEATHER(char* weatherType);
```

**Parámetros**

- `weatherType` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

---
### SetPlayerIsInAnimalForm

`_SET_PLAYER_IS_IN_ANIMAL_FORM` · hash `0x4EBB7E87AA0DBED4` · **Cliente**

```lua
SetPlayerIsInAnimalForm(toggle)
```
```c
void _SET_PLAYER_IS_IN_ANIMAL_FORM(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If toggle is true, the ped's head is shown in the pause menu
If toggle is false, the ped's head is not shown in the pause menu
```

**Nombres antiguos (alias):** `0x4EBB7E87AA0DBED4` (`N_0x4ebb7e87aa0dbed4`), `_SHOW_PED_IN_PAUSE_MENU` (`ShowPedInPauseMenu`)

---
### SetPlayerRockstarEditorDisabled

`_SET_PLAYER_ROCKSTAR_EDITOR_DISABLED` · hash `0x9D8D44ADBBA61EF2` · **Cliente**

```lua
SetPlayerRockstarEditorDisabled(toggle)
```
```c
void _SET_PLAYER_ROCKSTAR_EDITOR_DISABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_PLAYER_*
```

**Nombres antiguos (alias):** `0x9D8D44ADBBA61EF2` (`N_0x9d8d44adbba61ef2`)

---
### SetRainLevel

`_SET_RAIN_LEVEL` · hash `0x643E26EA6E024D92` · **Cliente**

```lua
SetRainLevel(level)
```
```c
void _SET_RAIN_LEVEL(float level);
```

**Parámetros**

- `level` (`float`): Strength of rain effects

**Devuelve:** `void`

**Descripción oficial:**

Controls rain, rain sounds and the creation of puddles.

With an `level` higher than `0.5f`, only the creation of puddles gets faster, rain and rain sound won't increase after that.

With an `level` of `0.0f` rain and rain sounds are disabled and there won't be any new puddles.

To use the rain level of the current weather, call this native with `-1f` as `level`.

**Nombres antiguos (alias):** `_SET_RAIN_FX_INTENSITY` (`SetRainFxIntensity`)

---
### SetRandomEventFlag

`SET_RANDOM_EVENT_FLAG` · hash `0x971927086CFD2158` · jhash `0xA77F31E8` · **Cliente**

```lua
SetRandomEventFlag(toggle)
```
```c
void SET_RANDOM_EVENT_FLAG(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
If the parameter is true, sets the random event flag to true, if the parameter is false, the function does nothing at all.  
Does nothing if the mission flag is set.  
```

---
### SetRandomSeed

`SET_RANDOM_SEED` · hash `0x444D98F98C11F3EC` · jhash `0xDB3FEB5C` · **Cliente**

```lua
SetRandomSeed(seed)
```
```c
void SET_RANDOM_SEED(int seed);
```

**Parámetros**

- `seed` (`int`)

**Devuelve:** `void`

---
### SetRandomWeatherType

`SET_RANDOM_WEATHER_TYPE` · hash `0x8B05F884CF7E8020` · jhash `0xE7AA1BC9` · **Cliente**

```lua
SetRandomWeatherType()
```
```c
void SET_RANDOM_WEATHER_TYPE();
```

**Devuelve:** `void`

---
### SetRestartCustomPosition

`_SET_RESTART_CUSTOM_POSITION` · hash `0x706B5EDCAA7FA663` · **Cliente**

```lua
SetRestartCustomPosition(x, y, z, heading)
```
```c
void _SET_RESTART_CUSTOM_POSITION(float x, float y, float z, float heading);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x706B5EDCAA7FA663` (`N_0x706b5edcaa7fa663`), `_SET_CUSTOM_RESPAWN_POSITION` (`SetCustomRespawnPosition`)

---
### SetRiotModeEnabled

`SET_RIOT_MODE_ENABLED` · hash `0x2587A48BC88DFADF` · jhash `0xD9660339` · **Cliente**

```lua
SetRiotModeEnabled(toggle)
```
```c
void SET_RIOT_MODE_ENABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Turn on or off riot mode. Set to `true` to enable riot mode.

**Devuelve:** `void`

**Descripción oficial:**

Activates riot mode. All NPCs are being hostile to each other (including player). Also the game will give weapons (pistols, smgs) to random NPCs.

**Nombres antiguos (alias):** `0x2587A48BC88DFADF` (`N_0x2587a48bc88dfadf`)

---
### SetSaveHouse

`SET_SAVE_HOUSE` · hash `0x4F548CABEAE553BC` · jhash `0xC3240BB4` · **Cliente**

```lua
SetSaveHouse(p0, p1, p2)
```
```c
void SET_SAVE_HOUSE(Any p0, BOOL p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### SetSaveMenuActive

`SET_SAVE_MENU_ACTIVE` · hash `0xC9BF75D28165FF77` · jhash `0xF5CCF164` · **Cliente**

```lua
SetSaveMenuActive(ignoreVehicle)
```
```c
void SET_SAVE_MENU_ACTIVE(BOOL ignoreVehicle);
```

**Parámetros**

- `ignoreVehicle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
ignoreVehicle - bypasses vehicle check of the local player (it will not open if you are in a vehicle and this is set to false)
```

---
### SetSnowLevel

`_SET_SNOW_LEVEL` · hash `0x7F06937B0CDCBC1A` · **Cliente**

```lua
SetSnowLevel(level)
```
```c
void _SET_SNOW_LEVEL(float level);
```

**Parámetros**

- `level` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1868
```

---
### SetStuntJumpsCanTrigger

`SET_STUNT_JUMPS_CAN_TRIGGER` · hash `0xD79185689F8FD5DF` · jhash `0x3C806A2D` · **Cliente**

```lua
SetStuntJumpsCanTrigger(toggle)
```
```c
void SET_STUNT_JUMPS_CAN_TRIGGER(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD79185689F8FD5DF` (`N_0xd79185689f8fd5df`)

---
### SetSuperJumpThisFrame

`SET_SUPER_JUMP_THIS_FRAME` · hash `0x57FFF03E423A4C0B` · jhash `0x86745EF3` · **Cliente**

```lua
SetSuperJumpThisFrame(player)
```
```c
void SET_SUPER_JUMP_THIS_FRAME(Player player);
```

**Parámetros**

- `player` (`Player`): The player we are setting this for.

**Devuelve:** `void`

**Descripción oficial:**

Allows the player to perform super jumps. This function must be called every frame for it to work.
It basically OR's a flag for a single frame, allowing the ped to perform a super jump only when the flag is set.

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
    while true do
        SetSuperJumpThisFrame(PlayerId())
        -- Try enabling the two down below if you also want invincibility and no ragdoll effects
        --SetPlayerInvincible(PlayerId(), true)
        --SetPedCanRagdoll(PlayerPedId(), false)
        Citizen.Wait(0)
    end
end)
```

---
### SetThisScriptCanBePaused

`SET_THIS_SCRIPT_CAN_BE_PAUSED` · hash `0xAA391C728106F7AF` · jhash `0xA0C3CE29` · **Cliente**

```lua
SetThisScriptCanBePaused(toggle)
```
```c
void SET_THIS_SCRIPT_CAN_BE_PAUSED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetThisScriptCanRemoveBlipsCreatedByAnyScript

`SET_THIS_SCRIPT_CAN_REMOVE_BLIPS_CREATED_BY_ANY_SCRIPT` · hash `0xB98236CAAECEF897` · jhash `0xD06F1720` · **Cliente**

```lua
SetThisScriptCanRemoveBlipsCreatedByAnyScript(toggle)
```
```c
void SET_THIS_SCRIPT_CAN_REMOVE_BLIPS_CREATED_BY_ANY_SCRIPT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Bool indicating if the script that called this native can remove blips created by other scripts.

**Devuelve:** `void`

**Descripción oficial:**

Normally, blips can only be removed by the script or resource that created them. However, this native function allows a script to bypass this logic and remove blips from any script.

---
### SetTimeScale

`SET_TIME_SCALE` · hash `0x1D408577D440E81E` · jhash `0xA7F84694` · **Cliente**

```lua
SetTimeScale(timeScale)
```
```c
void SET_TIME_SCALE(float timeScale);
```

**Parámetros**

- `timeScale` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Maximum value is 1.  
At a value of 0 the game will still run at a minimum time scale.  
Slow Motion 1: 0.6  
Slow Motion 2: 0.4  
Slow Motion 3: 0.2  
```

---
### SetWeatherTypeNow

`SET_WEATHER_TYPE_NOW` · hash `0x29B487C359E19889` · jhash `0x361E9EAC` · **Cliente**

```lua
SetWeatherTypeNow(weatherType)
```
```c
void SET_WEATHER_TYPE_NOW(char* weatherType);
```

**Parámetros**

- `weatherType` (`char*`): The weather type to set. This should be one of the predefined weather type strings.

**Devuelve:** `void`

**Descripción oficial:**

Immediately changes the game's weather to the specified type, which will then persist for one cycle before the game resumes its natural weather progression.

**Note:** This native is not supported in networked sessions. Please refer to [`SET_OVERRIDE_WEATHER`](#setoverrideweather) or [`SET_WEATHER_TYPE_NOW_PERSIST`](#setweathertypenowpersist) if you want to override weather in networked sessions.

```
NativeDB Introduced: v323
```

**Weather Types:**

*   CLEAR
*   EXTRASUNNY
*   CLOUDS
*   OVERCAST
*   RAIN
*   CLEARING
*   THUNDER
*   SMOG
*   FOGGY
*   XMAS
*   SNOW
*   SNOWLIGHT
*   BLIZZARD
*   HALLOWEEN
*   NEUTRAL
*   RAIN_HALLOWEEN
*   SNOW_HALLOWEEN

---
### SetWeatherTypeNowPersist

`SET_WEATHER_TYPE_NOW_PERSIST` · hash `0xED712CA327900C8A` · jhash `0xC869FE97` · **Cliente**

```lua
SetWeatherTypeNowPersist(weatherType)
```
```c
void SET_WEATHER_TYPE_NOW_PERSIST(char* weatherType);
```

**Parámetros**

- `weatherType` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

---
### SetWeatherTypeOvertimePersist

`SET_WEATHER_TYPE_OVERTIME_PERSIST` · hash `0xFB5045B7C42B75BF` · jhash `0x386F0D25` · **Cliente**

```lua
SetWeatherTypeOvertimePersist(weatherType, time)
```
```c
void SET_WEATHER_TYPE_OVERTIME_PERSIST(char* weatherType, float time);
```

**Parámetros**

- `weatherType` (`char*`): The weather type to override to.
- `time` (`float`): A float on how long to take to transition (in seconds).

**Devuelve:** `void`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

**Nombres antiguos (alias):** `_SET_WEATHER_TYPE_OVER_TIME` (`SetWeatherTypeOverTime`)

---
### SetWeatherTypePersist

`SET_WEATHER_TYPE_PERSIST` · hash `0x704983DF373B198F` · jhash `0xC6C04C75` · **Cliente**

```lua
SetWeatherTypePersist(weatherType)
```
```c
void SET_WEATHER_TYPE_PERSIST(char* weatherType);
```

**Parámetros**

- `weatherType` (`char*`): The weather type to be set as persistent. Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for a list of weather type strings.

**Devuelve:** `void`

**Descripción oficial:**

Sets the current weather type to persist indefinitely until changed.

**Note:** This native is not supported in networked sessions. Please refer to [`SET_OVERRIDE_WEATHER`](#setoverrideweather) or [`SET_WEATHER_TYPE_NOW_PERSIST`](#setweathertypenowpersist) if you want to override weather in networked sessions.

```
NativeDB Introduced: v323
```

---
### SetWeatherTypeTransition

`_SET_WEATHER_TYPE_TRANSITION` · hash `0x578C752848ECFA0C` · jhash `0x5CA74040` · **Cliente**

```lua
SetWeatherTypeTransition(weatherType1, weatherType2, percentWeather2)
```
```c
void _SET_WEATHER_TYPE_TRANSITION(Hash weatherType1, Hash weatherType2, float percentWeather2);
```

**Parámetros**

- `weatherType1` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `weatherType2` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `percentWeather2` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Refer to [`SET_WEATHER_TYPE_NOW`](#setweathertypenow) for weather types.

```
Mixes two weather types. If percentWeather2 is set to 0.0f, then the weather will be entirely of weatherType1, if it is set to 1.0f it will be entirely of weatherType2. If it's set somewhere in between, there will be a mixture of weather behaviors. To test, try this in the RPH console, and change the float to different values between 0 and 1:  
execute "NativeFunction.Natives.x578C752848ECFA0C(Game.GetHashKey(""RAIN""), Game.GetHashKey(""SMOG""), 0.50f);  
```

---
### SetWind

`SET_WIND` · hash `0xAC3A74E8384A9919` · jhash `0xC6294698` · **Cliente**

```lua
SetWind(speed)
```
```c
void SET_WIND(float speed);
```

**Parámetros**

- `speed` (`float`): The wind speed (clamped to between 0.0 and 1.0)

**Devuelve:** `void`

**Descripción oficial:**

Sets the the raw wind speed value. The wind speed will stay persistent until it is reset (see examples).

**Ejemplo (lua):**

```lua
-- Stops all and any wind
SetWind(0)

-- Sets the wind to 6 m/s
SetWind(0.5)

-- Allows the game dynamically change the wind again
SetWind(-1)
```

**Ejemplo (js):**

```js
// Stops all and any wind
SetWind(0);

// Sets the wind to 6 m/s
SetWind(0.5);

// Allows the game dynamically change the wind again
SetWind(-1);
```

**Ejemplo (cs):**

```cs
// Stops all and any wind
SetWind(0f);

// Sets the wind to 6 m/s
SetWind(0.5f);

// Allows the game dynamically change the wind again
SetWind(-1f);
```

---
### SetWindDirection

`SET_WIND_DIRECTION` · hash `0xEB0F4468467B4528` · jhash `0x381AEEE9` · **Cliente**

```lua
SetWindDirection(direction)
```
```c
void SET_WIND_DIRECTION(float direction);
```

**Parámetros**

- `direction` (`float`): the [wind direction](https://en.wikipedia.org/wiki/Wind_direction) in radians

**Devuelve:** `void`

**Descripción oficial:**

Sets the wind direction. The wind direction will stay persistent until it is reset (see examples).

**Ejemplo (lua):**

```lua
-- 180 degrees, wind will blow from the south
SetWindDirection(math.rad(180.0))

-- Allows the game to dynamically change the wind direction again
SetWindDirection(-1)
```

**Ejemplo (js):**

```js
// 180 degrees, wind will blow from the south
SetWindDirection(180.0 * (Math.PI / 180));

// Allows the game to dynamically change the wind direction again
SetWindDirection(-1);
```

**Ejemplo (cs):**

```cs
// 180 degrees, wind will blow from the south
SetWindDirection(3.1415f);

// Allows the game to dynamically change the wind direction again
SetWindDirection(-1f);
```

---
### SetWindSpeed

`SET_WIND_SPEED` · hash `0xEE09ECEDBABE47FC` · jhash `0x45705F94` · **Cliente**

```lua
SetWindSpeed(speed)
```
```c
void SET_WIND_SPEED(float speed);
```

**Parámetros**

- `speed` (`float`): wind speed in meters per second

**Devuelve:** `void`

**Descripción oficial:**

Using this native will clamp the wind speed value to a range of 0.0 - 12.0. The wind speed will stay persistent until it is reset (see examples).

**Ejemplo (lua):**

```lua
-- Sets the wind speed to 0 meters per second
SetWind(0)

-- Sets the wind to 11.99 m/s
SetWind(11.99)

-- Allows the game dynamically change the wind speed again
SetWind(-1)
```

**Ejemplo (js):**

```js
// Sets the wind speed to 0 meters per second
SetWind(0);

// Sets the wind to 11.99 m/s
SetWind(11.99);

// Allows the game dynamically change the wind speed again
SetWind(-1);
```

**Ejemplo (cs):**

```cs
// Sets the wind speed to 0 meters per second
SetWind(0f);

// Sets the wind to 11.99 m/s
SetWind(11.99f);

// Allows the game dynamically change the wind speed again
SetWind(-1f);
```

---
### ShootSingleBulletBetweenCoords

`SHOOT_SINGLE_BULLET_BETWEEN_COORDS` · hash `0x867654CBC7606F2C` · jhash `0xCB7415AC` · **Cliente**

```lua
ShootSingleBulletBetweenCoords(x1, y1, z1, x2, y2, z2, damage, pureAccuracy, weaponHash, ownerPed, isAudible, isInvisible, speed)
```
```c
void SHOOT_SINGLE_BULLET_BETWEEN_COORDS(float x1, float y1, float z1, float x2, float y2, float z2, int damage, BOOL pureAccuracy, Hash weaponHash, Ped ownerPed, BOOL isAudible, BOOL isInvisible, float speed);
```

**Parámetros**

- `x1` (`float`): The X coordinate to start the shot at.
- `y1` (`float`): The Y coordinate to start the shot at.
- `z1` (`float`): The Z coordinate to start the shot at.
- `x2` (`float`): The X coordinate the shot should end up at.
- `y2` (`float`): The Y coordinate the shot should end up at.
- `z2` (`float`): The Z coordinate the shot should end up at.
- `damage` (`int`): The amount of damage the bullet carries.
- `pureAccuracy` (`BOOL`): Whether the bullet should have pinpoint accuracy.
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Hash of the weapon the bullet is used as ammunition for.
- `ownerPed` (`Ped`): Owner of the bullet, e.g. if the bullet kills someone the kill feed shows 'X was shot by ownerPed.'
- `isAudible` (`BOOL`): Whether the bullet should be audible. Optional, defaults to true
- `isInvisible` (`BOOL`): Whether the bullet should be invisible. Optional, defaults to false
- `speed` (`float`): Speed the bullet should fly at. Optional

**Devuelve:** `void`

**Descripción oficial:**

Shoots a bullet from the first vector to the second vector. The weapon used as weaponHash should already be loaded via REQUEST_WEAPON_ASSET, otherwise the bullet may fail to materialise.

---
### ShootSingleBulletBetweenCoordsIgnoreEntity

`SHOOT_SINGLE_BULLET_BETWEEN_COORDS_IGNORE_ENTITY` · hash `0xE3A7742E0B7A2F8B` · jhash `0x52ACCB7B` · **Cliente**

```lua
ShootSingleBulletBetweenCoordsIgnoreEntity(x1, y1, z1, x2, y2, z2, damage, p7, weaponHash, ownerPed, isAudible, isInvisible, speed, entity)
```
```c
void SHOOT_SINGLE_BULLET_BETWEEN_COORDS_IGNORE_ENTITY(float x1, float y1, float z1, float x2, float y2, float z2, int damage, BOOL p7, Hash weaponHash, Ped ownerPed, BOOL isAudible, BOOL isInvisible, float speed, Entity entity);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `damage` (`int`)
- `p7` (`BOOL`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ownerPed` (`Ped`)
- `isAudible` (`BOOL`)
- `isInvisible` (`BOOL`)
- `speed` (`float`)
- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
entity - entity to ignore  
```

```
NativeDB Added Parameter 15: Any p14
```

**Nombres antiguos (alias):** `0xE3A7742E0B7A2F8B` (`N_0xe3a7742e0b7a2f8b`), `_SHOOT_SINGLE_BULLET_BETWEEN_COORDS_PRESET_PARAMS` (`ShootSingleBulletBetweenCoordsPresetParams`)

---
### ShootSingleBulletBetweenCoordsIgnoreEntityNew

`SHOOT_SINGLE_BULLET_BETWEEN_COORDS_IGNORE_ENTITY_NEW` · hash `0xBFE5756E7407064A` · jhash `0xCCDC33CC` · **Cliente**

```lua
ShootSingleBulletBetweenCoordsIgnoreEntityNew(x1, y1, z1, x2, y2, z2, damage, p7, weaponHash, ownerPed, isAudible, isInvisible, speed, entity, p14, p15, p16, p17)
```
```c
void SHOOT_SINGLE_BULLET_BETWEEN_COORDS_IGNORE_ENTITY_NEW(float x1, float y1, float z1, float x2, float y2, float z2, int damage, BOOL p7, Hash weaponHash, Ped ownerPed, BOOL isAudible, BOOL isInvisible, float speed, Entity entity, BOOL p14, BOOL p15, BOOL p16, BOOL p17);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `damage` (`int`)
- `p7` (`BOOL`)
- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `ownerPed` (`Ped`)
- `isAudible` (`BOOL`)
- `isInvisible` (`BOOL`)
- `speed` (`float`)
- `entity` (`Entity`)
- `p14` (`BOOL`)
- `p15` (`BOOL`)
- `p16` (`BOOL`)
- `p17` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 19: Any p18
NativeDB Added Parameter 20: Any p19
NativeDB Added Parameter 21: Any p20
```

**Nombres antiguos (alias):** `0xBFE5756E7407064A` (`N_0xbfe5756e7407064a`), `_SHOOT_SINGLE_BULLET_BETWEEN_COORDS_WITH_EXTRA_PARAMS` (`ShootSingleBulletBetweenCoordsWithExtraParams`)

---
### ShouldUseMetricMeasurements

`SHOULD_USE_METRIC_MEASUREMENTS` · hash `0xD3D15555431AB793` · jhash `0xBAF17315` · **Cliente**

```lua
local retval = ShouldUseMetricMeasurements()
```
```c
BOOL SHOULD_USE_METRIC_MEASUREMENTS();
```

**Devuelve:** `BOOL` — Returns true if the game is using the metric measurement system, false if imperial is used.

**Descripción oficial:**

Returns true if the game is using the metric measurement system (profile setting 227), false if imperial is used.

**Nombres antiguos (alias):** `0xD3D15555431AB793` (`N_0xd3d15555431ab793`), `_IS_GAME_USING_METRIC_MEASUREMENT_SYSTEM` (`IsGameUsingMetricMeasurementSystem`)

**Ejemplo (lua):**

```lua
if (ShouldUseMetricMeasurements()) then
    print("Distance to finish line: 8,04672 km.")
else
    print("Distance to finish line: 5 mi.")
end
```

---
### SlerpNearQuaternion

`SLERP_NEAR_QUATERNION` · hash `0xF2F6A2FA49278625` · jhash `0x87B92190` · **Cliente**

```lua
local outX, outY, outZ, outW = SlerpNearQuaternion(t, x, y, z, w, x1, y1, z1, w1)
```
```c
void SLERP_NEAR_QUATERNION(float t, float x, float y, float z, float w, float x1, float y1, float z1, float w1, float* outX, float* outY, float* outZ, float* outW);
```

**Parámetros**

- `t` (`float`): acceleration differenzial (am_rollercoaster.c func\_134)
- `x` (`float`): rotation parameter (maybe X axys)
- `y` (`float`): rotation parameter (maybe X axys)
- `z` (`float`): rotation parameter (maybe X axys)
- `w` (`float`): rotation parameter (maybe X axys)
- `x1` (`float`): rotation parameter (maybe Y axys)
- `y1` (`float`): rotation parameter (maybe Y axys)
- `z1` (`float`): rotation parameter (maybe Y axys)
- `w1` (`float`): rotation parameter (maybe Y axys)
- `outX` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: output value calculated (X)
- `outY` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: output value calculated (Y)
- `outZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: output value calculated (Z)
- `outW` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: output value calculated (W)

**Devuelve:** `void`

**Descripción oficial:**

This native always come right before SET_ENTITY_QUATERNION where its final 4 parameters are SLERP_NEAR_QUATERNION p9 to p12

**Nombres antiguos (alias):** `0xF2F6A2FA49278625` (`N_0xf2f6a2fa49278625`)

**Ejemplo (cs):**

```cs
// Example from am_rollercoaster.c
// where func_136 calculates arctan of given values and func_135 calculates both sin and cos

void func_134(int iParam0, int iParam1, float fParam2) cippalippo
{
	int iVar0;
	int iVar1;
	int iVar2;
	int iVar3;
	float fVar4;
	var uVar5[4];
	var uVar6[4];
	var uVar7[4];
	float fVar8;
	
	iVar0 = func_47(iParam1);
	iVar1 = iParam1;
	iVar2 = func_48(iParam1);
	iVar3 = func_48(iVar2);
	if (fParam2 < 0f)
	{
		fParam2 = (fParam2 + Local_1417[(iLocal_714 - 1) /*5*/].f_3);
	}
	fVar8 = ((fParam2 - Local_1417[iVar1 /*5*/].f_3) / (Local_1417[iVar2 /*5*/].f_3 - Local_1417[iVar1 /*5*/].f_3));
	if (fVar8 < 0.5f)
	{
		fVar4 = (fVar8 + 0.5f);
		func_135(func_136(iVar0, iVar1), &(uVar5[0]), &(uVar5[1]), &(uVar5[2]), &(uVar5[3]));
		func_135(func_136(iVar1, iVar2), &(uVar6[0]), &(uVar6[1]), &(uVar6[2]), &(uVar6[3]));
	}
	else
	{
		fVar4 = (fVar8 - 0.5f);
		func_135(func_136(iVar1, iVar2), &(uVar5[0]), &(uVar5[1]), &(uVar5[2]), &(uVar5[3]));
		func_135(func_136(iVar2, iVar3), &(uVar6[0]), &(uVar6[1]), &(uVar6[2]), &(uVar6[3]));
	}
	MISC::_0xF2F6A2FA49278625(fVar4, uVar5[0], uVar5[1], uVar5[2], uVar5[3], uVar6[0], uVar6[1], uVar6[2], uVar6[3], &(uVar7[0]), &(uVar7[1]), &(uVar7[2]), &(uVar7[3]));
	ENTITY::SET_ENTITY_QUATERNION(iLocal_719[iParam0], uVar7[0], uVar7[1], uVar7[2], uVar7[3]);
}
```

---
### StartBenchmarkRecording

`_START_BENCHMARK_RECORDING` · hash `0x92790862E36C2ADA` · **Cliente**

```lua
StartBenchmarkRecording()
```
```c
void _START_BENCHMARK_RECORDING();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Begins with START_*. Next character in the name is either D or E.
```

**Nombres antiguos (alias):** `0x92790862E36C2ADA` (`N_0x92790862e36c2ada`)

---
### StartSaveArrayWithSize

`START_SAVE_ARRAY_WITH_SIZE` · hash `0x60FE567DF1B1AF9D` · jhash `0x893A342C` · **Cliente**

```lua
local p0 = StartSaveArrayWithSize(size, arrayName)
```
```c
void START_SAVE_ARRAY_WITH_SIZE(Any* p0, int size, char* arrayName);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `size` (`int`)
- `arrayName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_START_SAVE_ARRAY` (`StartSaveArray`)

---
### StartSaveData

`START_SAVE_DATA` · hash `0xA9575F812C6A7997` · jhash `0x881A694D` · **Cliente**

```lua
local p0 = StartSaveData(p1, p2)
```
```c
void START_SAVE_DATA(Any* p0, Any p1, BOOL p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`BOOL`)

**Devuelve:** `void`

---
### StartSaveStructWithSize

`START_SAVE_STRUCT_WITH_SIZE` · hash `0xBF737600CDDBEADD` · jhash `0xFB45728E` · **Cliente**

```lua
local p0 = StartSaveStructWithSize(size, structName)
```
```c
void START_SAVE_STRUCT_WITH_SIZE(Any* p0, int size, char* structName);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `size` (`int`)
- `structName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_START_SAVE_STRUCT` (`StartSaveStruct`)

---
### StopBenchmarkRecording

`_STOP_BENCHMARK_RECORDING` · hash `0xC7DB36C24634F52B` · **Cliente**

```lua
StopBenchmarkRecording()
```
```c
void _STOP_BENCHMARK_RECORDING();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Begins with STOP_*. Next character in the name is either D or E.
```

**Nombres antiguos (alias):** `0xC7DB36C24634F52B` (`N_0xc7db36c24634f52b`)

---
### StopSaveArray

`STOP_SAVE_ARRAY` · hash `0x04456F95153C6BE4` · jhash `0x0CAD8217` · **Cliente**

```lua
StopSaveArray()
```
```c
void STOP_SAVE_ARRAY();
```

**Devuelve:** `void`

---
### StopSaveData

`STOP_SAVE_DATA` · hash `0x74E20C9145FB66FD` · jhash `0x3B1C07C8` · **Cliente**

```lua
StopSaveData()
```
```c
void STOP_SAVE_DATA();
```

**Devuelve:** `void`

---
### StopSaveStruct

`STOP_SAVE_STRUCT` · hash `0xEB1774DF12BB9F12` · jhash `0xC2624A28` · **Cliente**

```lua
StopSaveStruct()
```
```c
void STOP_SAVE_STRUCT();
```

**Devuelve:** `void`

---
### StringToInt

`STRING_TO_INT` · hash `0x5A5F40FE637EB584` · jhash `0x590A8160` · **Cliente**

```lua
local retval, outInteger = StringToInt(string, outInteger)
```
```c
BOOL STRING_TO_INT(char* string, int* outInteger);
```

**Parámetros**

- `string` (`char*`)
- `outInteger` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns false if it's a null or empty string or if the string is too long. outInteger will be set to -999 in that case.  
If all checks have passed successfully, the return value will be set to whatever strtol(string, 0i64, 10); returns.  
```

---
### SupressRandomEventThisFrame

`SUPRESS_RANDOM_EVENT_THIS_FRAME` · hash `0x1EAE0A6E978894A2` · jhash `0x8F60366E` · **Cliente**

```lua
SupressRandomEventThisFrame(eventType, enable)
```
```c
void SUPRESS_RANDOM_EVENT_THIS_FRAME(int eventType, BOOL enable);
```

**Parámetros**

- `eventType` (`int`): The type of the event to be suppressed or enabled. Use the `eEventType` enum for specific event types.
- `enable` (`BOOL`): Set to `false` to suppress the event for this frame; set to `true` to enable it.

**Devuelve:** `void`

**Descripción oficial:**

Suppresses or enables a specific type of random event for the current frame.

```cpp
enum eEventType {
    RC_PED_STEAL_VEHICLE = 0,
    RC_PED_JAY_WALK_LIGHT = 1,
    RC_COP_PURSUE = 2,
    RC_COP_PURSUE_VEHICLE_FLEE_SPAWNED = 3,
    RC_COP_VEHICLE_DRIVING_FAST = 4,
    RC_COP_VEHICLE_DRIVING_SLOW = 5,
    RC_DRIVER_RECKLESS = 6,
    RC_DRIVER_PRO = 7,
    RC_PED_PURSUE_WHEN_HIT_BY_CAR = 8
}
```

**Nombres antiguos (alias):** `0x1EAE0A6E978894A2` (`N_0x1eae0a6e978894a2`)

**Ejemplo (lua):**

```lua
local eventToDisable = 0 -- RC_PED_STEAL_VEHICLE

CreateThread(function()
    while true do
        Wait(0)
        SupressRandomEventThisFrame(eventToDisable, true)
    end
end)
```

**Ejemplo (js):**

```js
const eventToDisable = 0; // RC_PED_STEAL_VEHICLE

setTick(() => {
    SupressRandomEventThisFrame(eventToDisable, true);
});
```

---
### Tan

`TAN` · hash `0x632106CC96E82E91` · jhash `0xD320CE5E` · **Cliente**

```lua
local retval = Tan(p0)
```
```c
float TAN(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `float`

---
### TerminateAllScriptsWithThisName

`TERMINATE_ALL_SCRIPTS_WITH_THIS_NAME` · hash `0x9DC711BC69C548DF` · jhash `0x9F861FD4` · **Cliente**

```lua
TerminateAllScriptsWithThisName(scriptName)
```
```c
void TERMINATE_ALL_SCRIPTS_WITH_THIS_NAME(char* scriptName);
```

**Parámetros**

- `scriptName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

For a full list, see [here](https://gist.github.com/4mmonium/f76f3ecef649ed275b260b433ea84494).

---
### ToggleShowOptionalStuntJumpCamera

`TOGGLE_SHOW_OPTIONAL_STUNT_JUMP_CAMERA` · hash `0xFB80AB299D2EE1BD` · **Cliente**

```lua
ToggleShowOptionalStuntJumpCamera(toggle)
```
```c
void TOGGLE_SHOW_OPTIONAL_STUNT_JUMP_CAMERA(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Set to `true` to enable the optional stunt jump camera angles, or `false` to disable them and use the default camera view.

**Devuelve:** `void`

**Descripción oficial:**

Enable/disable optional stunt camera.

```
NativeDB Introduced: v757
```

**Nombres antiguos (alias):** `0xFB80AB299D2EE1BD` (`N_0xfb80ab299d2ee1bd`)

---
### UiStartedEndUserBenchmark

`UI_STARTED_END_USER_BENCHMARK` · hash `0xEA2F2061875EED90` · **Cliente**

```lua
local retval = UiStartedEndUserBenchmark()
```
```c
BOOL UI_STARTED_END_USER_BENCHMARK();
```

**Devuelve:** `BOOL` — Returns true if the current frontend menu is `FE_MENU_VERSION_SP_PAUSE`, `false` otherwise.

**Descripción oficial:**

Returns whether the In-Game Pause Menu Launched the Benchmark Tests.

**Nombres antiguos (alias):** `0xEA2F2061875EED90` (`N_0xea2f2061875eed90`), `_UI_IS_SINGLEPLAYER_PAUSE_MENU_ACTIVE` (`UiIsSingleplayerPauseMenuActive`)

---
### UnloadCloudHat

`UNLOAD_CLOUD_HAT` · hash `0xA74802FB8D0B7814` · jhash `0xC9FA6E07` · **Cliente**

```lua
UnloadCloudHat(name, p1)
```
```c
void UNLOAD_CLOUD_HAT(char* name, float p1);
```

**Parámetros**

- `name` (`char*`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Called 4 times in the b617d scripts:
MISC::_A74802FB8D0B7814("CONTRAILS", 0);
```

**Nombres antiguos (alias):** `0xA74802FB8D0B7814` (`N_0xa74802fb8d0b7814`)

---
### UpdateOnscreenKeyboard

`UPDATE_ONSCREEN_KEYBOARD` · hash `0x0CF2B696BBF945AE` · jhash `0x23D0A1CE` · **Cliente**

```lua
local retval = UpdateOnscreenKeyboard()
```
```c
int UPDATE_ONSCREEN_KEYBOARD();
```

**Devuelve:** `int` — Returns a value from the list above.

**Descripción oficial:**

Returns the current state of the text input box.

```cpp
enum eOSKStatus
{
  OSK_INVALID = -1,
  OSK_PENDING = 0,
  OSK_SUCCESS = 1,
  OSK_CANCELLED = 2,
  OSK_FAILED = 3
};
```

---
### UsingMissionCreator

`USING_MISSION_CREATOR` · hash `0xF14878FC50BEC6EE` · jhash `0x20AB0B6B` · **Cliente**

```lua
UsingMissionCreator(toggle)
```
```c
void USING_MISSION_CREATOR(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### WaterOverrideFadeIn

`WATER_OVERRIDE_FADE_IN` · hash `0xA8434F1DFF41D6E7` · jhash `0x5F3DDEC0` · **Cliente**

```lua
WaterOverrideFadeIn(p0)
```
```c
void WATER_OVERRIDE_FADE_IN(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA8434F1DFF41D6E7` (`N_0xa8434f1dff41d6e7`)

---
### WaterOverrideFadeOut

`WATER_OVERRIDE_FADE_OUT` · hash `0xC3C221ADDDE31A11` · jhash `0x63A89684` · **Cliente**

```lua
WaterOverrideFadeOut(p0)
```
```c
void WATER_OVERRIDE_FADE_OUT(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC3C221ADDDE31A11` (`N_0xc3c221addde31a11`)

---
### WaterOverrideSetOceannoiseminamplitude

`WATER_OVERRIDE_SET_OCEANNOISEMINAMPLITUDE` · hash `0x31727907B2C43C55` · jhash `0xD447439D` · **Cliente**

```lua
WaterOverrideSetOceannoiseminamplitude(minAmplitude)
```
```c
void WATER_OVERRIDE_SET_OCEANNOISEMINAMPLITUDE(float minAmplitude);
```

**Parámetros**

- `minAmplitude` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x31727907B2C43C55` (`N_0x31727907b2c43c55`)

---
### WaterOverrideSetOceanwaveamplitude

`WATER_OVERRIDE_SET_OCEANWAVEAMPLITUDE` · hash `0x405591EC8FD9096D` · jhash `0x584E9C59` · **Cliente**

```lua
WaterOverrideSetOceanwaveamplitude(amplitude)
```
```c
void WATER_OVERRIDE_SET_OCEANWAVEAMPLITUDE(float amplitude);
```

**Parámetros**

- `amplitude` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x405591EC8FD9096D` (`N_0x405591ec8fd9096d`)

---
### WaterOverrideSetOceanwavemaxamplitude

`WATER_OVERRIDE_SET_OCEANWAVEMAXAMPLITUDE` · hash `0xB3E6360DDE733E82` · jhash `0x0DE40C28` · **Cliente**

```lua
WaterOverrideSetOceanwavemaxamplitude(maxAmplitude)
```
```c
void WATER_OVERRIDE_SET_OCEANWAVEMAXAMPLITUDE(float maxAmplitude);
```

**Parámetros**

- `maxAmplitude` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB3E6360DDE733E82` (`N_0xb3e6360dde733e82`)

---
### WaterOverrideSetOceanwaveminamplitude

`WATER_OVERRIDE_SET_OCEANWAVEMINAMPLITUDE` · hash `0xF751B16FB32ABC1D` · jhash `0x5656D578` · **Cliente**

```lua
WaterOverrideSetOceanwaveminamplitude(minAmplitude)
```
```c
void WATER_OVERRIDE_SET_OCEANWAVEMINAMPLITUDE(float minAmplitude);
```

**Parámetros**

- `minAmplitude` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF751B16FB32ABC1D` (`N_0xf751b16fb32abc1d`)

---
### WaterOverrideSetRipplebumpiness

`WATER_OVERRIDE_SET_RIPPLEBUMPINESS` · hash `0x7C9C0B1EEB1F9072` · jhash `0x98C9138B` · **Cliente**

```lua
WaterOverrideSetRipplebumpiness(bumpiness)
```
```c
void WATER_OVERRIDE_SET_RIPPLEBUMPINESS(float bumpiness);
```

**Parámetros**

- `bumpiness` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x7C9C0B1EEB1F9072` (`N_0x7c9c0b1eeb1f9072`)

---
### WaterOverrideSetRippledisturb

`WATER_OVERRIDE_SET_RIPPLEDISTURB` · hash `0xB9854DFDE0D833D6` · jhash `0x4671AC2E` · **Cliente**

```lua
WaterOverrideSetRippledisturb(disturb)
```
```c
void WATER_OVERRIDE_SET_RIPPLEDISTURB(float disturb);
```

**Parámetros**

- `disturb` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB9854DFDE0D833D6` (`N_0xb9854dfde0d833d6`)

---
### WaterOverrideSetRipplemaxbumpiness

`WATER_OVERRIDE_SET_RIPPLEMAXBUMPINESS` · hash `0x9F5E6BB6B34540DA` · jhash `0x1C0CAE89` · **Cliente**

```lua
WaterOverrideSetRipplemaxbumpiness(maxBumpiness)
```
```c
void WATER_OVERRIDE_SET_RIPPLEMAXBUMPINESS(float maxBumpiness);
```

**Parámetros**

- `maxBumpiness` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x9F5E6BB6B34540DA` (`N_0x9f5e6bb6b34540da`)

---
### WaterOverrideSetRippleminbumpiness

`WATER_OVERRIDE_SET_RIPPLEMINBUMPINESS` · hash `0x6216B116083A7CB4` · jhash `0xFB1A9CDE` · **Cliente**

```lua
WaterOverrideSetRippleminbumpiness(minBumpiness)
```
```c
void WATER_OVERRIDE_SET_RIPPLEMINBUMPINESS(float minBumpiness);
```

**Parámetros**

- `minBumpiness` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6216B116083A7CB4` (`N_0x6216b116083a7cb4`)

---
### WaterOverrideSetShorewaveamplitude

`WATER_OVERRIDE_SET_SHOREWAVEAMPLITUDE` · hash `0xB8F87EAD7533B176` · jhash `0x625181DC` · **Cliente**

```lua
WaterOverrideSetShorewaveamplitude(amplitude)
```
```c
void WATER_OVERRIDE_SET_SHOREWAVEAMPLITUDE(float amplitude);
```

**Parámetros**

- `amplitude` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB8F87EAD7533B176` (`N_0xb8f87ead7533b176`)

---
### WaterOverrideSetShorewavemaxamplitude

`WATER_OVERRIDE_SET_SHOREWAVEMAXAMPLITUDE` · hash `0xA7A1127490312C36` · jhash `0x6926AB03` · **Cliente**

```lua
WaterOverrideSetShorewavemaxamplitude(maxAmplitude)
```
```c
void WATER_OVERRIDE_SET_SHOREWAVEMAXAMPLITUDE(float maxAmplitude);
```

**Parámetros**

- `maxAmplitude` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA7A1127490312C36` (`N_0xa7a1127490312c36`)

---
### WaterOverrideSetShorewaveminamplitude

`WATER_OVERRIDE_SET_SHOREWAVEMINAMPLITUDE` · hash `0xC3EAD29AB273ECE8` · jhash `0xBEBBFDC8` · **Cliente**

```lua
WaterOverrideSetShorewaveminamplitude(minAmplitude)
```
```c
void WATER_OVERRIDE_SET_SHOREWAVEMINAMPLITUDE(float minAmplitude);
```

**Parámetros**

- `minAmplitude` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC3EAD29AB273ECE8` (`N_0xc3ead29ab273ece8`)

---
### WaterOverrideSetStrength

`WATER_OVERRIDE_SET_STRENGTH` · hash `0xC54A08C85AE4D410` · jhash `0xDA02F415` · **Cliente**

```lua
WaterOverrideSetStrength(strength)
```
```c
void WATER_OVERRIDE_SET_STRENGTH(float strength);
```

**Parámetros**

- `strength` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This seems to edit the water wave, intensity around your current location.  
0.0f = Normal  
1.0f = So Calm and Smooth, a boat will stay still.  
3.0f = Really Intense.  
```

**Nombres antiguos (alias):** `0xC54A08C85AE4D410` (`N_0xc54a08c85ae4d410`)

---
