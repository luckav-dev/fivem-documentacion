# Natives de GTA V — AUDIO

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `AUDIO`: **276** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivateAudioSlowmoMode`](#activateaudioslowmomode) · [`AddEntityToAudioMixGroup`](#addentitytoaudiomixgroup) · [`AddLineToConversation`](#addlinetoconversation) · [`AddPedToConversation`](#addpedtoconversation) · [`AudioIsScriptedMusicPlaying`](#audioisscriptedmusicplaying) · [`BlipSiren`](#blipsiren) · [`BlockAllSpeechFromPed`](#blockallspeechfromped) · [`BlockDeathJingle`](#blockdeathjingle) · [`BlockSpeechContextGroup`](#blockspeechcontextgroup) · [`CanVehicleReceiveCbRadio`](#canvehiclereceivecbradio) · [`CancelAllPoliceReports`](#cancelallpolicereports) · [`CancelMusicEvent`](#cancelmusicevent) · [`ClearAllBrokenGlass`](#clearallbrokenglass) · [`ClearAmbientZoneListState`](#clearambientzoneliststate) · [`ClearAmbientZoneState`](#clearambientzonestate) · [`ClearCustomRadioTrackList`](#clearcustomradiotracklist) · [`CreateNewScriptedConversation`](#createnewscriptedconversation) · [`DeactivateAudioSlowmoMode`](#deactivateaudioslowmomode) · [`DisablePedPainAudio`](#disablepedpainaudio) · [`DistantCopCarSirens`](#distantcopcarsirens) · [`DoesContextExistForThisPed`](#doescontextexistforthisped) · [`DoesPlayerVehHaveRadio`](#doesplayervehhaveradio) · [`EnableStallWarningSounds`](#enablestallwarningsounds) · [`EnableStuntJumpAudio`](#enablestuntjumpaudio) · [`EnableVehicleExhaustPops`](#enablevehicleexhaustpops) · [`EnableVehicleFanbeltDamage`](#enablevehiclefanbeltdamage) · [`FindRadioStationIndex`](#findradiostationindex) · [`ForceMusicTrackList`](#forcemusictracklist) · [`ForcePedPanicWalla`](#forcepedpanicwalla) · [`ForceUseAudioGameObject`](#forceuseaudiogameobject) · [`ForceVehicleEngineSynth`](#forcevehicleenginesynth) · [`FreezeMicrophone`](#freezemicrophone) · [`FreezeRadioStation`](#freezeradiostation) · [`GetAmbientVoiceNameHash`](#getambientvoicenamehash) · [`GetAudibleMusicTrackTextId`](#getaudiblemusictracktextid) · [`GetCurrentRadioTrackPlaybackTime`](#getcurrentradiotrackplaybacktime) · [`GetCurrentScriptedConversationLine`](#getcurrentscriptedconversationline) · [`GetCurrentTrackSoundName`](#getcurrenttracksoundname) · [`GetIsPreloadedConversationReady`](#getispreloadedconversationready) · [`GetMusicPlaytime`](#getmusicplaytime) · [`GetMusicVolSlider`](#getmusicvolslider) · [`GetNetworkIdFromSoundId`](#getnetworkidfromsoundid) · [`GetNextAudibleBeat`](#getnextaudiblebeat) · [`GetNumUnlockedRadioStations`](#getnumunlockedradiostations) · [`GetPlayerRadioStationGenre`](#getplayerradiostationgenre) · [`GetPlayerRadioStationIndex`](#getplayerradiostationindex) · [`GetPlayerRadioStationName`](#getplayerradiostationname) · [`GetRadioStationName`](#getradiostationname) · [`GetSoundId`](#getsoundid) · [`GetSoundIdFromNetworkId`](#getsoundidfromnetworkid) · [`GetStreamPlayTime`](#getstreamplaytime) · [`GetVariationChosenForScriptedLine`](#getvariationchosenforscriptedline) · [`GetVehicleDefaultHorn`](#getvehicledefaulthorn) · [`GetVehicleDefaultHornIgnoreMods`](#getvehicledefaulthornignoremods) · [`GetVehicleHornSoundIndex`](#getvehiclehornsoundindex) · [`HasLoadedMpDataSet`](#hasloadedmpdataset) · [`HasLoadedSpDataSet`](#hasloadedspdataset) · [`HasSoundFinished`](#hassoundfinished) · [`HintAmbientAudioBank`](#hintambientaudiobank) · [`HintMissionAudioBank`](#hintmissionaudiobank) · [`HintScriptAudioBank`](#hintscriptaudiobank) · [`InitSynchSceneAudioWithEntity`](#initsynchsceneaudiowithentity) · [`InitSynchSceneAudioWithPosition`](#initsynchsceneaudiowithposition) · [`InterruptConversation`](#interruptconversation) · [`InterruptConversationAndPause`](#interruptconversationandpause) · [`IsAlarmPlaying`](#isalarmplaying) · [`IsAmbientSpeechDisabled`](#isambientspeechdisabled) · [`IsAmbientSpeechPlaying`](#isambientspeechplaying) · [`IsAmbientZoneEnabled`](#isambientzoneenabled) · [`IsAnimalVocalizationPlaying`](#isanimalvocalizationplaying) · [`IsAnyPositionalSpeechPlaying`](#isanypositionalspeechplaying) · [`IsAnySpeechPlaying`](#isanyspeechplaying) · [`IsAudioSceneActive`](#isaudiosceneactive) · [`IsGameInControlOfMusic`](#isgameincontrolofmusic) · [`IsHornActive`](#ishornactive) · [`IsMissionCompletePlaying`](#ismissioncompleteplaying) · [`IsMissionCompleteReadyForUi`](#ismissioncompletereadyforui) · [`IsMissionNewsStoryUnlocked`](#ismissionnewsstoryunlocked) · [`IsMobileInterferenceActive`](#ismobileinterferenceactive) · [`IsMobilePhoneCallOngoing`](#ismobilephonecallongoing) · [`IsMobilePhoneRadioActive`](#ismobilephoneradioactive) · [`IsMusicOneshotPlaying`](#ismusiconeshotplaying) · [`IsPedInCurrentConversation`](#ispedincurrentconversation) · [`IsPedRingtonePlaying`](#ispedringtoneplaying) · [`IsPlayerVehRadioEnable`](#isplayervehradioenable) · [`IsRadioFadedOut`](#isradiofadedout) · [`IsRadioRetuning`](#isradioretuning) · [`IsRadioStationFavourited`](#isradiostationfavourited) · [`IsScriptedConversationLoaded`](#isscriptedconversationloaded) · [`IsScriptedConversationOngoing`](#isscriptedconversationongoing) · [`IsScriptedSpeechPlaying`](#isscriptedspeechplaying) · [`IsStreamPlaying`](#isstreamplaying) · [`IsVehicleAudiblyDamaged`](#isvehicleaudiblydamaged) · [`IsVehicleRadioOn`](#isvehicleradioon) · [`LinkStaticEmitterToEntity`](#linkstaticemittertoentity) · [`LoadStream`](#loadstream) · [`LoadStreamWithStartOffset`](#loadstreamwithstartoffset) · [`LockRadioStation`](#lockradiostation) · [`LockRadioStationTrackList`](#lockradiostationtracklist) · [`N_0x02e93c796abd3a97`](#n_0x02e93c796abd3a97) · [`N_0x11579d940949c49e`](#n_0x11579d940949c49e) · [`N_0x19af7ed9b9d23058`](#n_0x19af7ed9b9d23058) · [`N_0x2dd39bf3e2f9c47f`](#n_0x2dd39bf3e2f9c47f) · [`N_0x43fa0dfc5df87815`](#n_0x43fa0dfc5df87815) · [`N_0x55ecf4d13d9903b0`](#n_0x55ecf4d13d9903b0) · [`N_0x58bb377bec7cd5f4`](#n_0x58bb377bec7cd5f4) · [`N_0x5b9853296731e88d`](#n_0x5b9853296731e88d) · [`N_0x8bf907833be275de`](#n_0x8bf907833be275de) · [`N_0x97ffb4adeed08066`](#n_0x97ffb4adeed08066) · [`N_0x9ac92eed5e4793ab`](#n_0x9ac92eed5e4793ab) · [`N_0x9bd7bd55e4533183`](#n_0x9bd7bd55e4533183) · [`N_0xb542de8c3d1cb210`](#n_0xb542de8c3d1cb210) · [`N_0xbef34b1d9624d5dd`](#n_0xbef34b1d9624d5dd) · [`N_0xc1805d05e6d4fe10`](#n_0xc1805d05e6d4fe10) · [`OverrideMicrophoneSettings`](#overridemicrophonesettings) · [`OverridePlayerGroundMaterial`](#overrideplayergroundmaterial) · [`OverrideTrevorRage`](#overridetrevorrage) · [`OverrideUnderwaterStream`](#overrideunderwaterstream) · [`OverrideVehHorn`](#overridevehhorn) · [`PauseScriptedConversation`](#pausescriptedconversation) · [`PlayAmbientSpeechFromPositionNative`](#playambientspeechfrompositionnative) · [`PlayAnimalVocalization`](#playanimalvocalization) · [`PlayDeferredSoundFrontend`](#playdeferredsoundfrontend) · [`PlayEndCreditsMusic`](#playendcreditsmusic) · [`PlayMissionCompleteAudio`](#playmissioncompleteaudio) · [`PlayPain`](#playpain) · [`PlayPedAmbientSpeechAndCloneNative`](#playpedambientspeechandclonenative) · [`PlayPedAmbientSpeechNative`](#playpedambientspeechnative) · [`PlayPedAmbientSpeechWithVoiceNative`](#playpedambientspeechwithvoicenative) · [`PlayPedRingtone`](#playpedringtone) · [`PlayPoliceReport`](#playpolicereport) · [`PlaySound`](#playsound) · [`PlaySoundFromCoord`](#playsoundfromcoord) · [`PlaySoundFromEntity`](#playsoundfromentity) · [`PlaySoundFrontend`](#playsoundfrontend) · [`PlayStreamFromObject`](#playstreamfromobject) · [`PlayStreamFromPed`](#playstreamfromped) · [`PlayStreamFromPosition`](#playstreamfromposition) · [`PlayStreamFromVehicle`](#playstreamfromvehicle) · [`PlayStreamFrontend`](#playstreamfrontend) · [`PlaySynchronizedAudioEvent`](#playsynchronizedaudioevent) · [`PlayVehicleDoorCloseSound`](#playvehicledoorclosesound) · [`PlayVehicleDoorOpenSound`](#playvehicledooropensound) · [`PreloadScriptConversation`](#preloadscriptconversation) · [`PreloadScriptPhoneConversation`](#preloadscriptphoneconversation) · [`PreloadVehicleAudioBank`](#preloadvehicleaudiobank) · [`PrepareAlarm`](#preparealarm) · [`PrepareMusicEvent`](#preparemusicevent) · [`PrepareSynchronizedAudioEvent`](#preparesynchronizedaudioevent) · [`PrepareSynchronizedAudioEventForScene`](#preparesynchronizedaudioeventforscene) · [`RecordBrokenGlass`](#recordbrokenglass) · [`RefreshClosestOceanShoreline`](#refreshclosestoceanshoreline) · [`RegisterScriptWithAudio`](#registerscriptwithaudio) · [`ReleaseAmbientAudioBank`](#releaseambientaudiobank) · [`ReleaseMissionAudioBank`](#releasemissionaudiobank) · [`ReleaseNamedScriptAudioBank`](#releasenamedscriptaudiobank) · [`ReleaseScriptAudioBank`](#releasescriptaudiobank) · [`ReleaseSoundId`](#releasesoundid) · [`ReleaseWeaponAudio`](#releaseweaponaudio) · [`RemoveEntityFromAudioMixGroup`](#removeentityfromaudiomixgroup) · [`RemovePortalSettingsOverride`](#removeportalsettingsoverride) · [`RequestAmbientAudioBank`](#requestambientaudiobank) · [`RequestMissionAudioBank`](#requestmissionaudiobank) · [`RequestScriptAudioBank`](#requestscriptaudiobank) · [`RequestTennisBanks`](#requesttennisbanks) · [`ResetPedAudioFlags`](#resetpedaudioflags) · [`ResetTrevorRage`](#resettrevorrage) · [`ResetVehicleStartupRevSound`](#resetvehiclestartuprevsound) · [`RestartScriptedConversation`](#restartscriptedconversation) · [`ScriptOverridesWindElevation`](#scriptoverrideswindelevation) · [`SetAggressiveHorns`](#setaggressivehorns) · [`SetAmbientVoiceName`](#setambientvoicename) · [`SetAmbientVoiceNameHash`](#setambientvoicenamehash) · [`SetAmbientZoneListState`](#setambientzoneliststate) · [`SetAmbientZoneListStatePersistent`](#setambientzoneliststatepersistent) · [`SetAmbientZoneState`](#setambientzonestate) · [`SetAmbientZoneStatePersistent`](#setambientzonestatepersistent) · [`SetAnimalMood`](#setanimalmood) · [`SetAudioFlag`](#setaudioflag) · [`SetAudioSceneVariable`](#setaudioscenevariable) · [`SetAudioScriptCleanupTime`](#setaudioscriptcleanuptime) · [`SetAudioSpecialEffectMode`](#setaudiospecialeffectmode) · [`SetAudioVehiclePriority`](#setaudiovehiclepriority) · [`SetConversationAudioControlledByAnim`](#setconversationaudiocontrolledbyanim) · [`SetConversationAudioPlaceholder`](#setconversationaudioplaceholder) · [`SetCustomRadioTrackList`](#setcustomradiotracklist) · [`SetCutsceneAudioOverride`](#setcutsceneaudiooverride) · [`SetEmitterRadioStation`](#setemitterradiostation) · [`SetEntityForNullConvPed`](#setentityfornullconvped) · [`SetFrontendRadioActive`](#setfrontendradioactive) · [`SetGlobalRadioSignalLevel`](#setglobalradiosignallevel) · [`SetGpsActive`](#setgpsactive) · [`SetHornEnabled`](#sethornenabled) · [`SetHornPermanentlyOnTime`](#sethornpermanentlyontime) · [`SetInitialPlayerStation`](#setinitialplayerstation) · [`SetMicrophonePosition`](#setmicrophoneposition) · [`SetMobilePhoneRadioState`](#setmobilephoneradiostate) · [`SetMobileRadioEnabledDuringGameplay`](#setmobileradioenabledduringgameplay) · [`SetPedAudioFootstepLoud`](#setpedaudiofootsteploud) · [`SetPedAudioGender`](#setpedaudiogender) · [`SetPedClothEventsEnabled`](#setpedclotheventsenabled) · [`SetPedIsDrunk`](#setpedisdrunk) · [`SetPedRaceAndVoiceGroup`](#setpedraceandvoicegroup) · [`SetPedVoiceFull`](#setpedvoicefull) · [`SetPedVoiceGroup`](#setpedvoicegroup) · [`SetPedVoiceGroupRace`](#setpedvoicegrouprace) · [`SetPedWallaDensity`](#setpedwalladensity) · [`SetPlayerAngry`](#setplayerangry) · [`SetPlayerVehicleAlarmAudioActive`](#setplayervehiclealarmaudioactive) · [`SetPortalSettingsOverride`](#setportalsettingsoverride) · [`SetPositionForNullConvPed`](#setpositionfornullconvped) · [`SetPositionedPlayerVehicleRadioEmitterEnabled`](#setpositionedplayervehicleradioemitterenabled) · [`SetRadioAutoUnfreeze`](#setradioautounfreeze) · [`SetRadioFrontendFadeTime`](#setradiofrontendfadetime) · [`SetRadioRetuneDown`](#setradioretunedown) · [`SetRadioRetuneUp`](#setradioretuneup) · [`SetRadioStationIsVisible`](#setradiostationisvisible) · [`SetRadioStationMusicOnly`](#setradiostationmusiconly) · [`SetRadioToStationIndex`](#setradiotostationindex) · [`SetRadioToStationName`](#setradiotostationname) · [`SetRadioTrack`](#setradiotrack) · [`SetRadioTrackMix`](#setradiotrackmix) · [`SetScriptUpdateDoorAudio`](#setscriptupdatedooraudio) · [`SetSirenKeepOn`](#setsirenkeepon) · [`SetSirenWithNoDriver`](#setsirenwithnodriver) · [`SetStaticEmitterEnabled`](#setstaticemitterenabled) · [`SetUserRadioControlEnabled`](#setuserradiocontrolenabled) · [`SetVariableOnCutsceneAudio`](#setvariableoncutsceneaudio) · [`SetVariableOnSound`](#setvariableonsound) · [`SetVariableOnStream`](#setvariableonstream) · [`SetVariableOnUnderWaterStream`](#setvariableonunderwaterstream) · [`SetVehHasRadioOverride`](#setvehhasradiooverride) · [`SetVehRadioStation`](#setvehradiostation) · [`SetVehicleAudioBodyDamageFactor`](#setvehicleaudiobodydamagefactor) · [`SetVehicleAudioEngineDamageFactor`](#setvehicleaudioenginedamagefactor) · [`SetVehicleBoostActive`](#setvehicleboostactive) · [`SetVehicleHornVariation`](#setvehiclehornvariation) · [`SetVehicleMissileWarningEnabled`](#setvehiclemissilewarningenabled) · [`SetVehicleRadioEnabled`](#setvehicleradioenabled) · [`SetVehicleRadioLoud`](#setvehicleradioloud) · [`SetVehicleStartupRevSound`](#setvehiclestartuprevsound) · [`SkipRadioForward`](#skipradioforward) · [`SkipToNextScriptedConversationLine`](#skiptonextscriptedconversationline) · [`SoundVehicleHornThisFrame`](#soundvehiclehornthisframe) · [`StartAlarm`](#startalarm) · [`StartAudioScene`](#startaudioscene) · [`StartPreloadedConversation`](#startpreloadedconversation) · [`StartScriptConversation`](#startscriptconversation) · [`StartScriptPhoneConversation`](#startscriptphoneconversation) · [`StopAlarm`](#stopalarm) · [`StopAllAlarms`](#stopallalarms) · [`StopAudioScene`](#stopaudioscene) · [`StopAudioScenes`](#stopaudioscenes) · [`StopCurrentPlayingAmbientSpeech`](#stopcurrentplayingambientspeech) · [`StopCurrentPlayingSpeech`](#stopcurrentplayingspeech) · [`StopCutsceneAudio`](#stopcutsceneaudio) · [`StopPedRingtone`](#stoppedringtone) · [`StopPedSpeaking`](#stoppedspeaking) · [`StopPedSpeakingSynced`](#stoppedspeakingsynced) · [`StopScriptedConversation`](#stopscriptedconversation) · [`StopSmokeGrenadeExplosionSounds`](#stopsmokegrenadeexplosionsounds) · [`StopSound`](#stopsound) · [`StopStream`](#stopstream) · [`StopSynchronizedAudioEvent`](#stopsynchronizedaudioevent) · [`TriggerMusicEvent`](#triggermusicevent) · [`TriggerSiren`](#triggersiren) · [`UnblockSpeechContextGroup`](#unblockspeechcontextgroup) · [`UnfreezeRadioStation`](#unfreezeradiostation) · [`UnlockMissionNewsStory`](#unlockmissionnewsstory) · [`UnlockRadioStationTrackList`](#unlockradiostationtracklist) · [`UnregisterScriptWithAudio`](#unregisterscriptwithaudio) · [`UnrequestTennisBanks`](#unrequesttennisbanks) · [`UpdateSoundCoord`](#updatesoundcoord) · [`UpdateUnlockableDjRadioTracks`](#updateunlockabledjradiotracks) · [`UseFootstepScriptSweeteners`](#usefootstepscriptsweeteners) · [`UseSirenAsHorn`](#usesirenashorn)

---
### ActivateAudioSlowmoMode

`ACTIVATE_AUDIO_SLOWMO_MODE` · hash `0xD01005D2BA2EB778` · jhash `0x59A3A17D` · **Cliente**

```lua
ActivateAudioSlowmoMode(mode)
```
```c
void ACTIVATE_AUDIO_SLOWMO_MODE(char* mode);
```

**Parámetros**

- `mode` (`char*`): A string indicating the audio slow motion mode to use, *see the table*.

**Devuelve:** `void`

**Descripción oficial:**

Below is a list of modes and their respective hashes.

| Mode (string)               | Hash               |
|-----------------------------|--------------------|
| SLOWMO_BIG_SCORE_JUMP       | 0x2B981B0C         |
| JSH_EXIT_TUNNEL_SLOWMO      | 0x2562AA6          |
| SLOW_MO_METH_HOUSE_RAYFIRE  | 0xDB9E1909         |
| SLOWMO_FIB4\_TRUCK_SMASH     | 0x9E144347         |
| SLOWMO_PROLOGUE_VAULT       | 0xEA2E68E1         |
| SLOWMO_T1\_RAYFIRE_EXPLOSION | 0xD6D358F3         |
| SLOWMO_T1\_TRAILER_SMASH     | 0xBE607345         |
| BARRY\_01\_SLOWMO             | 0xD59540D4         |
| BARRY\_02\_SLOWMO             | 0x12F140B3         |
| SLOWMO_EXTREME\_04           | 0xF562EA50         |
| NIGEL\_02\_SLOWMO_SETTING     | 0x384689B0         |

**Nombres antiguos (alias):** `0xD01005D2BA2EB778` (`N_0xd01005d2ba2eb778`)

---
### AddEntityToAudioMixGroup

`ADD_ENTITY_TO_AUDIO_MIX_GROUP` · hash `0x153973AB99FE8980` · jhash `0x2BC93264` · **Cliente**

```lua
AddEntityToAudioMixGroup(entity, groupName, fadeIn)
```
```c
void ADD_ENTITY_TO_AUDIO_MIX_GROUP(Entity entity, char* groupName, float fadeIn);
```

**Parámetros**

- `entity` (`Entity`)
- `groupName` (`char*`)
- `fadeIn` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
All found occurrences in b678d:
pastebin.com/ceu67jz8
```

**Nombres antiguos (alias):** `0x153973AB99FE8980` (`N_0x153973ab99fe8980`), `_DYNAMIC_MIXER_RELATED_FN` (`DynamicMixerRelatedFn`)

---
### AddLineToConversation

`ADD_LINE_TO_CONVERSATION` · hash `0xC5EF963405593646` · jhash `0x96CD0513` · **Cliente**

```lua
AddLineToConversation(speakerConversationIndex, context, subtitle, listenerNumber, volumeType, isRandom, interruptible, ducksRadio, ducksScore, audibility, headset, dontInterruptForSpecialAbility, isPadSpeakerRoute)
```
```c
void ADD_LINE_TO_CONVERSATION(int speakerConversationIndex, char* context, char* subtitle, int listenerNumber, int volumeType, BOOL isRandom, BOOL interruptible, BOOL ducksRadio, BOOL ducksScore, int audibility, BOOL headset, BOOL dontInterruptForSpecialAbility, BOOL isPadSpeakerRoute);
```

**Parámetros**

- `speakerConversationIndex` (`int`)
- `context` (`char*`)
- `subtitle` (`char*`)
- `listenerNumber` (`int`)
- `volumeType` (`int`)
- `isRandom` (`BOOL`)
- `interruptible` (`BOOL`)
- `ducksRadio` (`BOOL`)
- `ducksScore` (`BOOL`)
- `audibility` (`int`): See eAudibility
- `headset` (`BOOL`)
- `dontInterruptForSpecialAbility` (`BOOL`)
- `isPadSpeakerRoute` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eAudibility {
	AUD_AUDIBILITY_NORMAL = 0,
	AUD_AUDIBILITY_CLEAR = 1,
	AUD_AUDIBILITY_CRITICAL = 2,
	AUD_AUDIBILITY_LEAD_IN = 3
}
```

---
### AddPedToConversation

`ADD_PED_TO_CONVERSATION` · hash `0x95D9F4BC443956E7` · jhash `0xF8D5EB86` · **Cliente**

```lua
AddPedToConversation(speakerConversationIndex, ped, voiceName)
```
```c
void ADD_PED_TO_CONVERSATION(int speakerConversationIndex, Ped ped, char* voiceName);
```

**Parámetros**

- `speakerConversationIndex` (`int`)
- `ped` (`Ped`)
- `voiceName` (`char*`)

**Devuelve:** `void`

---
### AudioIsScriptedMusicPlaying

`AUDIO_IS_SCRIPTED_MUSIC_PLAYING` · hash `0x845FFC3A4FEEFA3E` · jhash `0x86E995D1` · **Cliente**

```lua
local retval = AudioIsScriptedMusicPlaying()
```
```c
BOOL AUDIO_IS_SCRIPTED_MUSIC_PLAYING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3D120012440E6683` (`N_0x3d120012440e6683`)

---
### BlipSiren

`BLIP_SIREN` · hash `0x1B9025BDA76822B6` · jhash `0xC0EB6924` · **Cliente**

```lua
BlipSiren(vehicle)
```
```c
void BLIP_SIREN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

Plays a siren blip from the vehicle when you double press the horn key.

This only works on vehicles with sirens.

---
### BlockAllSpeechFromPed

`BLOCK_ALL_SPEECH_FROM_PED` · hash `0xF8AD2EED7C47E8FE` · **Cliente**

```lua
BlockAllSpeechFromPed(ped, shouldBlock, suppressOutgoingNetworkSpeech)
```
```c
void BLOCK_ALL_SPEECH_FROM_PED(Ped ped, BOOL shouldBlock, BOOL suppressOutgoingNetworkSpeech);
```

**Parámetros**

- `ped` (`Ped`)
- `shouldBlock` (`BOOL`)
- `suppressOutgoingNetworkSpeech` (`BOOL`): Defaults to `true`.

**Devuelve:** `void`

**Descripción oficial:**

Blocks *all* speech playing on the given ped, including speech triggered by natives such as [PLAY_PED_AMBIENT_SPEECH_WITH_VOICE_NATIVE](#playpedambientspeechwithvoicenative)

The flag itself is not synced, it must be called on each machine that wishes to suppress the speech.

The `SuppressOutgoingNetworkSpeech` flag can be set to `false` if you want speech triggered locally through `PLAY_PED_AMBIENT_SPEECH_*` related native calls to still be audible on remote machines, even though it was blocked on the local one.

**Nombres antiguos (alias):** `0xF8AD2EED7C47E8FE` (`N_0xf8ad2eed7c47e8fe`)

---
### BlockDeathJingle

`BLOCK_DEATH_JINGLE` · hash `0xF154B8D1775B2DEC` · jhash `0xD2858D8A` · **Cliente**

```lua
BlockDeathJingle(blocked)
```
```c
void BLOCK_DEATH_JINGLE(BOOL blocked);
```

**Parámetros**

- `blocked` (`BOOL`): Sets if the death jingle can play when a player dies or not

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF154B8D1775B2DEC` (`N_0xf154b8d1775b2dec`)

---
### BlockSpeechContextGroup

`BLOCK_SPEECH_CONTEXT_GROUP` · hash `0xA8A7D434AFB4B97B` · **Cliente**

```lua
BlockSpeechContextGroup(groupName, contextBlockTarget)
```
```c
void BLOCK_SPEECH_CONTEXT_GROUP(char* groupName, int contextBlockTarget);
```

**Parámetros**

- `groupName` (`char*`): the name of the context group to be blocked
- `contextBlockTarget` (`int`): the group of peds that should be used (refer to eAudContextBlockTarget)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eAudContextBlockTarget {
	AUD_CONTEXT_BLOCK_PLAYER = 0,
	AUD_CONTEXT_BLOCK_NPCS = 1,
	AUD_CONTEXT_BLOCK_BUDDYS = 2,
	AUD_CONTEXT_BLOCK_EVERYONE = 3,

	AUD_CONTEXT_BLOCK_TARGETS_TOTAL
}
```

Stop a certain group of peds from using a certain group of speech contexts.

Note that the block will be automatically removed when the calling script finishes

**Nombres antiguos (alias):** `0xA8A7D434AFB4B97B` (`N_0xa8a7d434afb4b97b`)

---
### CanVehicleReceiveCbRadio

`CAN_VEHICLE_RECEIVE_CB_RADIO` · hash `0x032A116663A4D5AC` · jhash `0xCBA99F4A` · **Cliente**

```lua
local retval = CanVehicleReceiveCbRadio(vehicle)
```
```c
BOOL CAN_VEHICLE_RECEIVE_CB_RADIO(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL` — Returns true if the vehicle can currently receive CB radio (ie. it has a capable radio and is in range of a transmitter)

**Nombres antiguos (alias):** `_IS_VEHICLE_RADIO_LOUD` (`IsVehicleRadioLoud`)

---
### CancelAllPoliceReports

`CANCEL_ALL_POLICE_REPORTS` · hash `0xB4F90FAF7670B16F` · **Cliente**

```lua
CancelAllPoliceReports()
```
```c
void CANCEL_ALL_POLICE_REPORTS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB4F90FAF7670B16F` (`N_0xb4f90faf7670b16f`), `_DISABLE_POLICE_REPORTS` (`DisablePoliceReports`), `_CANCEL_CURRENT_POLICE_REPORT` (`CancelCurrentPoliceReport`)

---
### CancelMusicEvent

`CANCEL_MUSIC_EVENT` · hash `0x5B17A90291133DA5` · jhash `0x89FF942D` · **Cliente**

```lua
local retval = CancelMusicEvent(eventName)
```
```c
BOOL CANCEL_MUSIC_EVENT(char* eventName);
```

**Parámetros**

- `eventName` (`char*`): the name of the event to cancel

**Devuelve:** `BOOL` — True of the event was cancelled, false otherwise.

**Descripción oficial:**

```
All music event names found in the b617d scripts: pastebin.com/GnYt0R3P
```

---
### ClearAllBrokenGlass

`CLEAR_ALL_BROKEN_GLASS` · hash `0xB32209EFFDC04913` · jhash `0xE6B033BF` · **Cliente**

```lua
ClearAllBrokenGlass()
```
```c
void CLEAR_ALL_BROKEN_GLASS();
```

**Devuelve:** `void`

---
### ClearAmbientZoneListState

`CLEAR_AMBIENT_ZONE_LIST_STATE` · hash `0x120C48C614909FA4` · jhash `0x38B9B8D4` · **Cliente**

```lua
ClearAmbientZoneListState(zoneListName, forceUpdate)
```
```c
void CLEAR_AMBIENT_ZONE_LIST_STATE(char* zoneListName, BOOL forceUpdate);
```

**Parámetros**

- `zoneListName` (`char*`): The zone name to clear
- `forceUpdate` (`BOOL`): Whether ot not to force a zone to become disabled even if its currently active

**Devuelve:** `void`

**Descripción oficial:**

Resets the list of ambients zones enabled/disabled status to its value before it was modified by this script.

Default behaviour is that any state change only gets applied once the player leaves the zone.

---
### ClearAmbientZoneState

`CLEAR_AMBIENT_ZONE_STATE` · hash `0x218DD44AAAC964FF` · jhash `0xCDFF3C82` · **Cliente**

```lua
ClearAmbientZoneState(zoneName, forceUpdate)
```
```c
void CLEAR_AMBIENT_ZONE_STATE(char* zoneName, BOOL forceUpdate);
```

**Parámetros**

- `zoneName` (`char*`): the zone name to clear
- `forceUpdate` (`BOOL`): Whether ot not to force a zone to become disabled even if its currently active

**Devuelve:** `void`

**Descripción oficial:**

Resets the ambient zone enabled/disabled status to its value before it was modified by this script

Default behaviour is that any state change only gets applied once the player leaves the zone.

---
### ClearCustomRadioTrackList

`CLEAR_CUSTOM_RADIO_TRACK_LIST` · hash `0x1654F24A88A8E3FE` · jhash `0x1D766976` · **Cliente**

```lua
ClearCustomRadioTrackList(radioStation)
```
```c
void CLEAR_CUSTOM_RADIO_TRACK_LIST(char* radioStation);
```

**Parámetros**

- `radioStation` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Clears the previously queued custom track lost for the given radio station.

**Nombres antiguos (alias):** `0x1654F24A88A8E3FE` (`N_0x1654f24a88a8e3fe`)

---
### CreateNewScriptedConversation

`CREATE_NEW_SCRIPTED_CONVERSATION` · hash `0xD2C91A0B572AAE56` · jhash `0xB2BC25F8` · **Cliente**

```lua
CreateNewScriptedConversation()
```
```c
void CREATE_NEW_SCRIPTED_CONVERSATION();
```

**Devuelve:** `void`

---
### DeactivateAudioSlowmoMode

`DEACTIVATE_AUDIO_SLOWMO_MODE` · hash `0xDDC635D5B3262C56` · jhash `0x0E387BFE` · **Cliente**

```lua
DeactivateAudioSlowmoMode(mode)
```
```c
void DEACTIVATE_AUDIO_SLOWMO_MODE(char* mode);
```

**Parámetros**

- `mode` (`char*`): name of the mode to deactivate

**Devuelve:** `void`

**Descripción oficial:**

Deactivates the named slowmo mode.

**Nombres antiguos (alias):** `0xDDC635D5B3262C56` (`N_0xddc635d5b3262c56`)

---
### DisablePedPainAudio

`DISABLE_PED_PAIN_AUDIO` · hash `0xA9A41C1E940FB0E8` · jhash `0x3B8E2D5F` · **Cliente**

```lua
DisablePedPainAudio(ped, shouldDisable)
```
```c
void DISABLE_PED_PAIN_AUDIO(Ped ped, BOOL shouldDisable);
```

**Parámetros**

- `ped` (`Ped`)
- `shouldDisable` (`BOOL`)

**Devuelve:** `void`

---
### DistantCopCarSirens

`DISTANT_COP_CAR_SIRENS` · hash `0x552369F549563AD5` · jhash `0x13EB5861` · **Cliente**

```lua
DistantCopCarSirens(shouldPlay)
```
```c
void DISTANT_COP_CAR_SIRENS(BOOL shouldPlay);
```

**Parámetros**

- `shouldPlay` (`BOOL`): True will play distand sounds, false will disable them.

**Devuelve:** `void`

**Descripción oficial:**

Toggles fake distant siren sounds

**Nombres antiguos (alias):** `0x552369F549563AD5` (`N_0x552369f549563ad5`), `_FORCE_AMBIENT_SIREN` (`ForceAmbientSiren`)

---
### DoesContextExistForThisPed

`DOES_CONTEXT_EXIST_FOR_THIS_PED` · hash `0x49B99BF3FDA89A7A` · jhash `0x8BD5F11E` · **Cliente**

```lua
local retval = DoesContextExistForThisPed(ped, speechName, allowBackupPVGs)
```
```c
BOOL DOES_CONTEXT_EXIST_FOR_THIS_PED(Ped ped, char* speechName, BOOL allowBackupPVGs);
```

**Parámetros**

- `ped` (`Ped`)
- `speechName` (`char*`)
- `allowBackupPVGs` (`BOOL`)

**Devuelve:** `BOOL` — True of the PedVoiceGroup exists, false otherwise.

**Descripción oficial:**

Checks if the context exists for the ped, searching through the voices in its PedVoiceGroup.

The final argument can be set to true to allow searching in backup PVGs

**Nombres antiguos (alias):** `0x49B99BF3FDA89A7A` (`N_0x49b99bf3fda89a7a`), `_CAN_PED_SPEAK` (`CanPedSpeak`)

---
### DoesPlayerVehHaveRadio

`DOES_PLAYER_VEH_HAVE_RADIO` · hash `0x109697E2FFBAC8A1` · jhash `0x46B0C696` · **Cliente**

```lua
local retval = DoesPlayerVehHaveRadio()
```
```c
BOOL DOES_PLAYER_VEH_HAVE_RADIO();
```

**Devuelve:** `BOOL` — Returns `true` if the player's current vehicle has a radio. Returns `false` if it does not, or if the player is not in any vehicle.

**Descripción oficial:**

Checks if the vehicle the local player is currently in has a radio.

**Nombres antiguos (alias):** `0x109697E2FFBAC8A1` (`N_0x109697e2ffbac8a1`)

---
### EnableStallWarningSounds

`ENABLE_STALL_WARNING_SOUNDS` · hash `0xC15907D667F7CFB2` · jhash `0x563B635D` · **Cliente**

```lua
EnableStallWarningSounds(vehicle, enable)
```
```c
void ENABLE_STALL_WARNING_SOUNDS(Vehicle vehicle, BOOL enable);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `enable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Enable or disable the plane stall warning sounds

**Nombres antiguos (alias):** `0xC15907D667F7CFB2` (`N_0xc15907d667f7cfb2`)

---
### EnableStuntJumpAudio

`ENABLE_STUNT_JUMP_AUDIO` · hash `0xB81CF134AEB56FFB` · **Cliente**

```lua
EnableStuntJumpAudio()
```
```c
void ENABLE_STUNT_JUMP_AUDIO();
```

**Devuelve:** `void`

**Descripción oficial:**

Enable the stunt jump audio detection code

This native is meant to be called per-frame for as long as detection is wanted.

**Nombres antiguos (alias):** `0xB81CF134AEB56FFB` (`N_0xb81cf134aeb56ffb`)

---
### EnableVehicleExhaustPops

`ENABLE_VEHICLE_EXHAUST_POPS` · hash `0x2BE4BC731D039D5A` · jhash `0x2A60A90E` · **Cliente**

```lua
EnableVehicleExhaustPops(vehicle, toggle)
```
```c
void ENABLE_VEHICLE_EXHAUST_POPS(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`): Enables or disables exaust pops.

**Devuelve:** `void`

**Descripción oficial:**

Enable or disable exhaust pops on the given vehicle.

**Nombres antiguos (alias):** `0x2BE4BC731D039D5A` (`N_0x2be4bc731d039d5a`)

---
### EnableVehicleFanbeltDamage

`ENABLE_VEHICLE_FANBELT_DAMAGE` · hash `0x1C073274E065C6D2` · jhash `0x9365E042` · **Cliente**

```lua
EnableVehicleFanbeltDamage(vehicle, enableFanbeltDamage)
```
```c
void ENABLE_VEHICLE_FANBELT_DAMAGE(Vehicle vehicle, BOOL enableFanbeltDamage);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `enableFanbeltDamage` (`BOOL`): Enables fanbelt damage

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1C073274E065C6D2` (`N_0x1c073274e065c6d2`)

---
### FindRadioStationIndex

`FIND_RADIO_STATION_INDEX` · hash `0x8D67489793FF428B` · jhash `0xECA1512F` · **Cliente**

```lua
local retval = FindRadioStationIndex(stationNameHash)
```
```c
int FIND_RADIO_STATION_INDEX(int stationNameHash);
```

**Parámetros**

- `stationNameHash` (`int`): the station name hash to search for

**Devuelve:** `int` — The station index for the specified hash, or 254 if the radio station did not exist.

---
### ForceMusicTrackList

`FORCE_MUSIC_TRACK_LIST` · hash `0x4E0AF9114608257C` · **Cliente**

```lua
ForceMusicTrackList(radioStation, trackListName, timeOffsetMilliseconds)
```
```c
void FORCE_MUSIC_TRACK_LIST(char* radioStation, char* trackListName, int timeOffsetMilliseconds);
```

**Parámetros**

- `radioStation` (`char*`)
- `trackListName` (`char*`)
- `timeOffsetMilliseconds` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Forces the chosen station to paly the given music track list. All other music track lists will be locked.

**Nombres antiguos (alias):** `0x4E0AF9114608257C` (`N_0x4e0af9114608257c`), `_FORCE_RADIO_TRACK_LIST_POSITION` (`ForceRadioTrackListPosition`)

---
### ForcePedPanicWalla

`FORCE_PED_PANIC_WALLA` · hash `0x062D5EAD4DA2FA6A` · jhash `0xD87AF337` · **Cliente**

```lua
ForcePedPanicWalla()
```
```c
void FORCE_PED_PANIC_WALLA();
```

**Devuelve:** `void`

**Descripción oficial:**

Forces the ambient peds into their panic walla state

**Nombres antiguos (alias):** `0x062D5EAD4DA2FA6A` (`N_0x062d5ead4da2fa6a`)

---
### ForceUseAudioGameObject

`FORCE_USE_AUDIO_GAME_OBJECT` · hash `0x4F0C413926060B38` · jhash `0x33B0B007` · **Cliente**

```lua
ForceUseAudioGameObject(vehicle, gameObjectName)
```
```c
void FORCE_USE_AUDIO_GAME_OBJECT(Vehicle vehicle, char* gameObjectName);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `gameObjectName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

This native sets the audio to the specific vehicle hash's audioNameHash.

**Nombres antiguos (alias):** `0x4F0C413926060B38` (`N_0x4f0c413926060b38`), `_SET_VEHICLE_AUDIO` (`SetVehicleAudio`), `_FORCE_VEHICLE_ENGINE_AUDIO` (`ForceVehicleEngineAudio`)

---
### ForceVehicleEngineSynth

`_FORCE_VEHICLE_ENGINE_SYNTH` · hash `0xEB7D0E1FCC8FE17A` · **Cliente**

```lua
ForceVehicleEngineSynth(vehicle, force)
```
```c
void _FORCE_VEHICLE_ENGINE_SYNTH(Vehicle vehicle, BOOL force);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `force` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

This native is used alongside with [`SET_VEHICLE_TYRE_BURST`](VEHICLE-2.md#setvehicletyreburst).

```
NativeDB Introduced: v3258
```

---
### FreezeMicrophone

`FREEZE_MICROPHONE` · hash `0xD57AAAE0E2214D11` · jhash `0x2B9D91E8` · **Cliente**

```lua
FreezeMicrophone()
```
```c
void FREEZE_MICROPHONE();
```

**Devuelve:** `void`

**Descripción oficial:**

Allows script to freeze the microphone for a single frame, mantaining its current transform/settings.
This native should be called every frame you want to keep the microphone frozen, when you stop calling it it will automatically unfreeze

**Nombres antiguos (alias):** `0xD57AAAE0E2214D11` (`N_0xd57aaae0e2214d11`)

---
### FreezeRadioStation

`FREEZE_RADIO_STATION` · hash `0x344F393B027E38C3` · jhash `0x286BF543` · **Cliente**

```lua
FreezeRadioStation(radioStation)
```
```c
void FREEZE_RADIO_STATION(char* radioStation);
```

**Parámetros**

- `radioStation` (`char*`)

**Devuelve:** `void`

---
### GetAmbientVoiceNameHash

`GET_AMBIENT_VOICE_NAME_HASH` · hash `0x5E203DA2BA15D436` · **Cliente**

```lua
local retval = GetAmbientVoiceNameHash(ped)
```
```c
Hash GET_AMBIENT_VOICE_NAME_HASH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `Hash` — The hash of the voice name in use by the ped.

**Nombres antiguos (alias):** `0x5E203DA2BA15D436` (`N_0x5e203da2ba15d436`), `_GET_AMBIENT_VOICE_NAME_HASH` (`GetAmbientVoiceNameHash`)

---
### GetAudibleMusicTrackTextId

`GET_AUDIBLE_MUSIC_TRACK_TEXT_ID` · hash `0x50B196FC9ED6545B` · jhash `0xA2B88CA7` · **Cliente**

```lua
local retval = GetAudibleMusicTrackTextId()
```
```c
int GET_AUDIBLE_MUSIC_TRACK_TEXT_ID();
```

**Devuelve:** `int`

---
### GetCurrentRadioTrackPlaybackTime

`_GET_CURRENT_RADIO_TRACK_PLAYBACK_TIME` · hash `0x3E65CDE5215832C1` · **Cliente**

```lua
local retval = GetCurrentRadioTrackPlaybackTime(radioStationName)
```
```c
int _GET_CURRENT_RADIO_TRACK_PLAYBACK_TIME(char* radioStationName);
```

**Parámetros**

- `radioStationName` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
Return the playback time (in milliseconds) of the radio stations current track. 

NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x3E65CDE5215832C1` (`N_0x3e65cde5215832c1`), `_GET_CURRENT_RADIO_STATION_HASH` (`GetCurrentRadioStationHash`)

---
### GetCurrentScriptedConversationLine

`GET_CURRENT_SCRIPTED_CONVERSATION_LINE` · hash `0x480357EE890C295A` · jhash `0x9620E41F` · **Cliente**

```lua
local retval = GetCurrentScriptedConversationLine()
```
```c
int GET_CURRENT_SCRIPTED_CONVERSATION_LINE();
```

**Devuelve:** `int`

---
### GetCurrentTrackSoundName

`GET_CURRENT_TRACK_SOUND_NAME` · hash `0x34D66BC058019CE0` · **Cliente**

```lua
local retval = GetCurrentTrackSoundName(radioStationName)
```
```c
Hash GET_CURRENT_TRACK_SOUND_NAME(char* radioStationName);
```

**Parámetros**

- `radioStationName` (`char*`)

**Devuelve:** `Hash` — The current sound name as a hash for the currently playing track on the given station.

**Nombres antiguos (alias):** `0x34D66BC058019CE0` (`N_0x34d66bc058019ce0`), `_GET_CURRENT_RADIO_TRACK_NAME` (`GetCurrentRadioTrackName`)

---
### GetIsPreloadedConversationReady

`GET_IS_PRELOADED_CONVERSATION_READY` · hash `0xE73364DB90778FFA` · jhash `0x336F3D35` · **Cliente**

```lua
local retval = GetIsPreloadedConversationReady()
```
```c
BOOL GET_IS_PRELOADED_CONVERSATION_READY();
```

**Devuelve:** `BOOL` — Returns true if the preloaded conversation has finished preparing.

**Nombres antiguos (alias):** `0xE73364DB90778FFA` (`N_0xe73364db90778ffa`)

---
### GetMusicPlaytime

`GET_MUSIC_PLAYTIME` · hash `0xE7A0D23DC414507B` · jhash `0xD633C809` · **Cliente**

```lua
local retval = GetMusicPlaytime()
```
```c
int GET_MUSIC_PLAYTIME();
```

**Devuelve:** `int` — Returns the play time in milliseconds of the current score track.

---
### GetMusicVolSlider

`GET_MUSIC_VOL_SLIDER` · hash `0x3A48AB4445D499BE` · jhash `0x93A44A1F` · **Cliente**

```lua
local retval = GetMusicVolSlider()
```
```c
int GET_MUSIC_VOL_SLIDER();
```

**Devuelve:** `int` — Returns the current volume slider position from 0 to 10

**Nombres antiguos (alias):** `0x3A48AB4445D499BE` (`N_0x3a48ab4445d499be`)

---
### GetNetworkIdFromSoundId

`GET_NETWORK_ID_FROM_SOUND_ID` · hash `0x2DE3F0A134FFBC0D` · jhash `0x2576F610` · **Cliente**

```lua
local retval = GetNetworkIdFromSoundId(soundId)
```
```c
int GET_NETWORK_ID_FROM_SOUND_ID(int soundId);
```

**Parámetros**

- `soundId` (`int`)

**Devuelve:** `int` — Returns the network id for the specific sound

---
### GetNextAudibleBeat

`GET_NEXT_AUDIBLE_BEAT` · hash `0xC64A06D939F826F5` · **Cliente**

```lua
local retval, timeInSeconds, bpm, beatNum = GetNextAudibleBeat()
```
```c
BOOL GET_NEXT_AUDIBLE_BEAT(float* timeInSeconds, float* bpm, int* beatNum);
```

**Parámetros**

- `timeInSeconds` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: time in seconds until the start of the next beat
- `bpm` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: current tempo in beats per minute,
- `beatNum` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: integer beat within the bar

**Devuelve:** `BOOL` — Returns information on beat information for any audible music.

**Nombres antiguos (alias):** `0xC64A06D939F826F5` (`N_0xc64a06d939f826f5`)

---
### GetNumUnlockedRadioStations

`GET_NUM_UNLOCKED_RADIO_STATIONS` · hash `0xF1620ECB50E01DE7` · jhash `0xCC91FCF5` · **Cliente**

```lua
local retval = GetNumUnlockedRadioStations()
```
```c
int GET_NUM_UNLOCKED_RADIO_STATIONS();
```

**Devuelve:** `int` — Returns the number of radio stations currently unlocked in the game. This can change as a result of DLC and/or script calls.

**Nombres antiguos (alias):** `_MAX_RADIO_STATION_INDEX` (`MaxRadioStationIndex`)

---
### GetPlayerRadioStationGenre

`GET_PLAYER_RADIO_STATION_GENRE` · hash `0xA571991A7FE6CCEB` · jhash `0x872CF0EA` · **Cliente**

```lua
local retval = GetPlayerRadioStationGenre()
```
```c
int GET_PLAYER_RADIO_STATION_GENRE();
```

**Devuelve:** `int` — Returns the genre of the players current radio station

---
### GetPlayerRadioStationIndex

`GET_PLAYER_RADIO_STATION_INDEX` · hash `0xE8AF77C4C06ADC93` · jhash `0x1C4946AC` · **Cliente**

```lua
local retval = GetPlayerRadioStationIndex()
```
```c
int GET_PLAYER_RADIO_STATION_INDEX();
```

**Devuelve:** `int` — Returns the index of the current players radio station, or 255 if the radio is off

---
### GetPlayerRadioStationName

`GET_PLAYER_RADIO_STATION_NAME` · hash `0xF6D733C32076AD03` · jhash `0xD909C107` · **Cliente**

```lua
local retval = GetPlayerRadioStationName()
```
```c
char* GET_PLAYER_RADIO_STATION_NAME();
```

**Devuelve:** `char*` — Returns the name of the players radio station. This serves as the text label.

---
### GetRadioStationName

`GET_RADIO_STATION_NAME` · hash `0xB28ECA15046CA8B9` · jhash `0x3DF493BC` · **Cliente**

```lua
local retval = GetRadioStationName(stationIndex)
```
```c
char* GET_RADIO_STATION_NAME(int stationIndex);
```

**Parámetros**

- `stationIndex` (`int`)

**Devuelve:** `char*` — Returns the name of the radio station with the specified index. This serves as the text label.

---
### GetSoundId

`GET_SOUND_ID` · hash `0x430386FE9BF80B45` · jhash `0x6AE0AD56` · **Cliente**

```lua
local retval = GetSoundId()
```
```c
int GET_SOUND_ID();
```

**Devuelve:** `int` — Returns a sound id which can be used to control the sound after its has started playing.

**Descripción oficial:**

If a playback function has a soundId field but the sound doesn't need to be altered after triggering then pass a value of -1 for fire-and-forget playback, rather than getting a soundId.

SoundId's can be reused, without needing to release them and grab a new one.

If a sound's finished playing, you can reuse its SoundId to kick off another one.

If the sound's not finished playing, it'll be stopped first (fading out or whatever is set up in RAVE by the sound designer), and the new one kicked off; usually it is safer to just get a new SoundId.

SoundId's are not automatically cleaned up, you must use [RELEASE_SOUND_ID](#releasesoundid) after you've finished using them to allow the engine to recycle the sound id.

---
### GetSoundIdFromNetworkId

`GET_SOUND_ID_FROM_NETWORK_ID` · hash `0x75262FD12D0A1C84` · jhash `0xD064D4DC` · **Cliente**

```lua
local retval = GetSoundIdFromNetworkId(netId)
```
```c
int GET_SOUND_ID_FROM_NETWORK_ID(int netId);
```

**Parámetros**

- `netId` (`int`): Network ID of sound.

**Devuelve:** `int` — Integer representing a sound id, -1 on failure.

**Descripción oficial:**

Counterpart: [`GET_NETWORK_ID_FROM_SOUND_ID`](#getnetworkidfromsoundid).

**Nombres antiguos (alias):** `0x75262FD12D0A1C84` (`N_0x75262fd12d0a1c84`)

---
### GetStreamPlayTime

`GET_STREAM_PLAY_TIME` · hash `0x4E72BBDBCA58A3DB` · jhash `0xB4F0AD56` · **Cliente**

```lua
local retval = GetStreamPlayTime()
```
```c
int GET_STREAM_PLAY_TIME();
```

**Devuelve:** `int` — Returns the currently playing stream's play time

---
### GetVariationChosenForScriptedLine

`GET_VARIATION_CHOSEN_FOR_SCRIPTED_LINE` · hash `0xAA19F5572C38B564` · jhash `0xB58B8FF3` · **Cliente**

```lua
local retval = GetVariationChosenForScriptedLine(textLabel)
```
```c
int GET_VARIATION_CHOSEN_FOR_SCRIPTED_LINE(char* textLabel);
```

**Parámetros**

- `textLabel` (`char*`): all the text labels for filenames in `AmericanDialogueFiles.txt` appear to end with the letter 'A', it is the script's responsibility to add this 'A' before calling `GET_VARIATION_CHOSEN_FOR_SCRIPTED_LINE`.

**Devuelve:** `int` — Returns the variation chosen for a given script speech line, or `0` if it hasn't been chosen yet.Returns `-1` if there is no conversation active or if the active conversation doesn't contain this line or if the text label can't be found in the currently loaded text blocks

**Nombres antiguos (alias):** `0xAA19F5572C38B564` (`N_0xaa19f5572c38b564`)

---
### GetVehicleDefaultHorn

`GET_VEHICLE_DEFAULT_HORN` · hash `0x02165D55000219AC` · jhash `0xE84ABC19` · **Cliente**

```lua
local retval = GetVehicleDefaultHorn(vehicle)
```
```c
Hash GET_VEHICLE_DEFAULT_HORN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `Hash` — Returns the horn sound hash

---
### GetVehicleDefaultHornIgnoreMods

`GET_VEHICLE_DEFAULT_HORN_IGNORE_MODS` · hash `0xACB5DCCA1EC76840` · jhash `0xFD4B5B3B` · **Cliente**

```lua
local retval = GetVehicleDefaultHornIgnoreMods(vehicle)
```
```c
Hash GET_VEHICLE_DEFAULT_HORN_IGNORE_MODS(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `Hash` — Returns the horn sound hash ignoring any horn mods applied to the car

**Nombres antiguos (alias):** `0xACB5DCCA1EC76840` (`N_0xacb5dcca1ec76840`), `_GET_VEHICLE_HORN_HASH` (`GetVehicleHornHash`)

---
### GetVehicleHornSoundIndex

`GET_VEHICLE_HORN_SOUND_INDEX` · hash `0xD53F3A29BCE2580E` · **Cliente**

```lua
local retval = GetVehicleHornSoundIndex(vehicle)
```
```c
int GET_VEHICLE_HORN_SOUND_INDEX(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int` — The current horn sound index being used by the given vehicle

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

**Nombres antiguos (alias):** `0xD53F3A29BCE2580E` (`N_0xd53f3a29bce2580e`), `0x22FECB546C276A30` (`N_0x22fecb546c276a30`), `_GET_VEHICLE_DEFAULT_HORN_VARIATION` (`GetVehicleDefaultHornVariation`)

---
### HasLoadedMpDataSet

`HAS_LOADED_MP_DATA_SET` · hash `0x544810ED9DB6BBE6` · **Cliente**

```lua
local retval = HasLoadedMpDataSet()
```
```c
BOOL HAS_LOADED_MP_DATA_SET();
```

**Devuelve:** `BOOL` — Returns true if the audio for the Multiplayer data set has loaded

**Nombres antiguos (alias):** `0x544810ED9DB6BBE6` (`N_0x544810ed9db6bbe6`), `_HAS_MULTIPLAYER_AUDIO_DATA_LOADED` (`HasMultiplayerAudioDataLoaded`)

---
### HasLoadedSpDataSet

`HAS_LOADED_SP_DATA_SET` · hash `0x5B50ABB1FE3746F4` · **Cliente**

```lua
local retval = HasLoadedSpDataSet()
```
```c
BOOL HAS_LOADED_SP_DATA_SET();
```

**Devuelve:** `BOOL` — Returns true if the audio for the Single Player data set has loaded

**Nombres antiguos (alias):** `0x5B50ABB1FE3746F4` (`N_0x5b50abb1fe3746f4`), `_HAS_MULTIPLAYER_AUDIO_DATA_UNLOADED` (`HasMultiplayerAudioDataUnloaded`)

---
### HasSoundFinished

`HAS_SOUND_FINISHED` · hash `0xFCBDCE714A7C88E5` · jhash `0xE85AEC2E` · **Cliente**

```lua
local retval = HasSoundFinished(soundId)
```
```c
BOOL HAS_SOUND_FINISHED(int soundId);
```

**Parámetros**

- `soundId` (`int`)

**Devuelve:** `BOOL` — Returns true if the sound has finished playing, false otherwise.

---
### HintAmbientAudioBank

`HINT_AMBIENT_AUDIO_BANK` · hash `0x8F8C0E370AE62F5C` · jhash `0xF1850DDC` · **Cliente**

```lua
local retval = HintAmbientAudioBank(bankName, bOverNetwork)
```
```c
BOOL HINT_AMBIENT_AUDIO_BANK(char* bankName, BOOL bOverNetwork);
```

**Parámetros**

- `bankName` (`char*`)
- `bOverNetwork` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

This native is marked as a deprecated native internally, use [HINT_SCRIPT_AUDIO_BANK](#hintscriptaudiobank) instead

---
### HintMissionAudioBank

`HINT_MISSION_AUDIO_BANK` · hash `0x40763EA7B9B783E7` · **Cliente**

```lua
local retval = HintMissionAudioBank(bankName, bOverNetwork, playerBits)
```
```c
BOOL HINT_MISSION_AUDIO_BANK(char* bankName, BOOL bOverNetwork, int playerBits);
```

**Parámetros**

- `bankName` (`char*`)
- `bOverNetwork` (`BOOL`)
- `playerBits` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

This is marked as a deprecated function internally, please use [HINT_SCRIPT_AUDIO_BANK](#hintscriptaudiobank) instead.

**Nombres antiguos (alias):** `0x40763EA7B9B783E7` (`N_0x40763ea7b9b783e7`)

---
### HintScriptAudioBank

`HINT_SCRIPT_AUDIO_BANK` · hash `0xFB380A29641EC31A` · jhash `0x41FA0E51` · **Cliente**

```lua
local retval = HintScriptAudioBank(bankName, bOverNetwork)
```
```c
BOOL HINT_SCRIPT_AUDIO_BANK(char* bankName, BOOL bOverNetwork);
```

**Parámetros**

- `bankName` (`char*`)
- `bOverNetwork` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Hints that this bank would be good to load if there are free slots.
Does not guarentee loading of the bank, [REQUEST_SCRIPT_AUDIO_BANK](#requestambientaudiobank) MUST be used as normal before triggering sounds"

This native has a new argument on newer game builds:

*   **playerBits**: likely used to specifiy players to sync to as a bit mask (1 << (0-128))

---
### InitSynchSceneAudioWithEntity

`INIT_SYNCH_SCENE_AUDIO_WITH_ENTITY` · hash `0x950A154B8DAB6185` · jhash `0xA17F9AB0` · **Cliente**

```lua
InitSynchSceneAudioWithEntity(audioName, entity)
```
```c
void INIT_SYNCH_SCENE_AUDIO_WITH_ENTITY(char* audioName, Entity entity);
```

**Parámetros**

- `audioName` (`char*`)
- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x950A154B8DAB6185` (`N_0x950a154b8dab6185`), `_SET_SYNCHRONIZED_AUDIO_EVENT_POSITION_THIS_FRAME` (`SetSynchronizedAudioEventPositionThisFrame`)

---
### InitSynchSceneAudioWithPosition

`INIT_SYNCH_SCENE_AUDIO_WITH_POSITION` · hash `0xC8EDE9BDBCCBA6D4` · jhash `0x55A21772` · **Cliente**

```lua
InitSynchSceneAudioWithPosition(audioName, x, y, z)
```
```c
void INIT_SYNCH_SCENE_AUDIO_WITH_POSITION(char* audioName, float x, float y, float z);
```

**Parámetros**

- `audioName` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC8EDE9BDBCCBA6D4` (`N_0xc8ede9bdbccba6d4`)

---
### InterruptConversation

`INTERRUPT_CONVERSATION` · hash `0xA018A12E5C5C2FA6` · jhash `0xF3A67AF3` · **Cliente**

```lua
InterruptConversation(interrupterPed, context, voiceName)
```
```c
void INTERRUPT_CONVERSATION(Ped interrupterPed, char* context, char* voiceName);
```

**Parámetros**

- `interrupterPed` (`Ped`): the ped speaking
- `context` (`char*`): the line to use
- `voiceName` (`char*`): the voicename for the audio asset

**Devuelve:** `void`

**Descripción oficial:**

Handles conversation interrupts, using the code-side system for improved timing and to minimize unfriendly logic interactions.

---
### InterruptConversationAndPause

`INTERRUPT_CONVERSATION_AND_PAUSE` · hash `0x8A694D7A68F8DC38` · jhash `0xDD4A3F1F` · **Cliente**

```lua
InterruptConversationAndPause(interrupterPed, context, voiceName)
```
```c
void INTERRUPT_CONVERSATION_AND_PAUSE(Ped interrupterPed, char* context, char* voiceName);
```

**Parámetros**

- `interrupterPed` (`Ped`): the ped speaking
- `context` (`char*`): the line to use
- `voiceName` (`char*`): the voicename for the audio asset

**Devuelve:** `void`

**Descripción oficial:**

Handles conversation interrupts and pauses, using the code-side system for improved timing and to minimize unfriendly logic interactions.

**Nombres antiguos (alias):** `0x8A694D7A68F8DC38` (`N_0x8a694d7a68f8dc38`)

---
### IsAlarmPlaying

`IS_ALARM_PLAYING` · hash `0x226435CB96CCFC8C` · jhash `0x9D8E1D23` · **Cliente**

```lua
local retval = IsAlarmPlaying(alarmName)
```
```c
BOOL IS_ALARM_PLAYING(char* alarmName);
```

**Parámetros**

- `alarmName` (`char*`)

**Devuelve:** `BOOL` — Returns true if an alarm is currently playing with the specified name

**Ejemplo (lua):**

```lua
local bAlarmPlaying = IsAlarmPlaying("PORT_OF_LS_HEIST_FORT_ZANCUDO_ALARMS")
```

---
### IsAmbientSpeechDisabled

`IS_AMBIENT_SPEECH_DISABLED` · hash `0x932C2D096A2C3FFF` · jhash `0x109D1F89` · **Cliente**

```lua
local retval = IsAmbientSpeechDisabled(ped)
```
```c
BOOL IS_AMBIENT_SPEECH_DISABLED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns true if ambient speech for the ped has been disabled

---
### IsAmbientSpeechPlaying

`IS_AMBIENT_SPEECH_PLAYING` · hash `0x9072C8B49907BFAD` · jhash `0x1972E8AA` · **Cliente**

```lua
local retval = IsAmbientSpeechPlaying(ped)
```
```c
BOOL IS_AMBIENT_SPEECH_PLAYING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns true if the ped is currently playing ambient speech

---
### IsAmbientZoneEnabled

`IS_AMBIENT_ZONE_ENABLED` · hash `0x01E2817A479A7F9B` · jhash `0xBFABD872` · **Cliente**

```lua
local retval = IsAmbientZoneEnabled(ambientZone)
```
```c
BOOL IS_AMBIENT_ZONE_ENABLED(char* ambientZone);
```

**Parámetros**

- `ambientZone` (`char*`)

**Devuelve:** `BOOL` — Returns true if the given ambient zone is allowed to be active

---
### IsAnimalVocalizationPlaying

`IS_ANIMAL_VOCALIZATION_PLAYING` · hash `0xC265DF9FB44A9FBD` · jhash `0x0CBAF2EF` · **Cliente**

```lua
local retval = IsAnimalVocalizationPlaying(pedHandle)
```
```c
BOOL IS_ANIMAL_VOCALIZATION_PLAYING(Ped pedHandle);
```

**Parámetros**

- `pedHandle` (`Ped`)

**Devuelve:** `BOOL` — Returns true of the ped is currently playing animal sounds

**Nombres antiguos (alias):** `0xC265DF9FB44A9FBD` (`N_0xc265df9fb44a9fbd`)

---
### IsAnyPositionalSpeechPlaying

`IS_ANY_POSITIONAL_SPEECH_PLAYING` · hash `0x30CA2EF91D15ADF8` · **Cliente**

```lua
local retval = IsAnyPositionalSpeechPlaying()
```
```c
BOOL IS_ANY_POSITIONAL_SPEECH_PLAYING();
```

**Devuelve:** `BOOL` — Returns `true` if any ped-independent positional scripted speech (i.e. triggered using [PLAY_AMBIENT_SPEECH_FROM_POSITION_NATIVE](#playambientspeechfrompositionnative)) is currently playing, `false` otherwise.

**Descripción oficial:**

Determines if any ped-independent, positionally-based scripted speech is currently active. This typically includes speech events triggered using [`PLAY_AMBIENT_SPEECH_FROM_POSITION_NATIVE`](#playambientspeechfrompositionnative).

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `0x30CA2EF91D15ADF8` (`N_0x30ca2ef91d15adf8`)

---
### IsAnySpeechPlaying

`IS_ANY_SPEECH_PLAYING` · hash `0x729072355FA39EC9` · jhash `0x2B74A6D6` · **Cliente**

```lua
local retval = IsAnySpeechPlaying(ped)
```
```c
BOOL IS_ANY_SPEECH_PLAYING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns true if the specified ped is playing any speech

---
### IsAudioSceneActive

`IS_AUDIO_SCENE_ACTIVE` · hash `0xB65B60556E2A9225` · jhash `0xACBED05C` · **Cliente**

```lua
local retval = IsAudioSceneActive(scene)
```
```c
BOOL IS_AUDIO_SCENE_ACTIVE(char* scene);
```

**Parámetros**

- `scene` (`char*`): the name of the scene

**Devuelve:** `BOOL` — Returns true if the script is already running the named scene, false otherwise

---
### IsGameInControlOfMusic

`IS_GAME_IN_CONTROL_OF_MUSIC` · hash `0x6D28DC1671E334FD` · jhash `0x7643170D` · **Cliente**

```lua
local retval = IsGameInControlOfMusic()
```
```c
BOOL IS_GAME_IN_CONTROL_OF_MUSIC();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Hardcoded to return 1  
```

---
### IsHornActive

`IS_HORN_ACTIVE` · hash `0x9D6BFC12B05C6121` · jhash `0x20E2BDD0` · **Cliente**

```lua
local retval = IsHornActive(vehicle)
```
```c
BOOL IS_HORN_ACTIVE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL` — Returns true if the vehicle is currently playing a horn sound

---
### IsMissionCompletePlaying

`IS_MISSION_COMPLETE_PLAYING` · hash `0x19A30C23F5827F8A` · jhash `0x939982A1` · **Cliente**

```lua
local retval = IsMissionCompletePlaying()
```
```c
BOOL IS_MISSION_COMPLETE_PLAYING();
```

**Devuelve:** `BOOL` — Returns true if the mission complete audio is playing

---
### IsMissionCompleteReadyForUi

`IS_MISSION_COMPLETE_READY_FOR_UI` · hash `0x6F259F82D873B8B8` · jhash `0xCBE09AEC` · **Cliente**

```lua
local retval = IsMissionCompleteReadyForUi()
```
```c
BOOL IS_MISSION_COMPLETE_READY_FOR_UI();
```

**Devuelve:** `BOOL` — Returns true if the script should draw the mission complete UI to be in sync with audio.

**Nombres antiguos (alias):** `0x6F259F82D873B8B8` (`N_0x6f259f82d873b8b8`)

---
### IsMissionNewsStoryUnlocked

`IS_MISSION_NEWS_STORY_UNLOCKED` · hash `0x66E49BF55B4B1874` · jhash `0x27305D37` · **Cliente**

```lua
local retval = IsMissionNewsStoryUnlocked(newsStory)
```
```c
BOOL IS_MISSION_NEWS_STORY_UNLOCKED(int newsStory);
```

**Parámetros**

- `newsStory` (`int`)

**Devuelve:** `BOOL` — Returns true of the specific story is available to be played back

**Nombres antiguos (alias):** `GET_NUMBER_OF_PASSENGER_VOICE_VARIATIONS` (`GetNumberOfPassengerVoiceVariations`)

---
### IsMobileInterferenceActive

`IS_MOBILE_INTERFERENCE_ACTIVE` · hash `0xC8B1B2425604CDD0` · jhash `0x16FB88B5` · **Cliente**

```lua
local retval = IsMobileInterferenceActive()
```
```c
BOOL IS_MOBILE_INTERFERENCE_ACTIVE();
```

**Devuelve:** `BOOL` — Returns true of mobile phone interference is currently happening

**Nombres antiguos (alias):** `0xC8B1B2425604CDD0` (`N_0xc8b1b2425604cdd0`)

---
### IsMobilePhoneCallOngoing

`IS_MOBILE_PHONE_CALL_ONGOING` · hash `0x7497D2CE2C30D24C` · jhash `0x4ED1400A` · **Cliente**

```lua
local retval = IsMobilePhoneCallOngoing()
```
```c
BOOL IS_MOBILE_PHONE_CALL_ONGOING();
```

**Devuelve:** `BOOL` — Returns true of a mobile phone call is currently happening.

---
### IsMobilePhoneRadioActive

`IS_MOBILE_PHONE_RADIO_ACTIVE` · hash `0xB35CE999E8EF317E` · jhash `0x6E502A5B` · **Cliente**

```lua
local retval = IsMobilePhoneRadioActive()
```
```c
BOOL IS_MOBILE_PHONE_RADIO_ACTIVE();
```

**Devuelve:** `BOOL` — Returns true if the mobile phone radio is active

---
### IsMusicOneshotPlaying

`IS_MUSIC_ONESHOT_PLAYING` · hash `0xA097AB275061FB21` · jhash `0x2705C4D5` · **Cliente**

```lua
local retval = IsMusicOneshotPlaying()
```
```c
BOOL IS_MUSIC_ONESHOT_PLAYING();
```

**Devuelve:** `BOOL` — Returns true if a one shot is currently playing or prepared

**Nombres antiguos (alias):** `0xA097AB275061FB21` (`N_0xa097ab275061fb21`)

---
### IsPedInCurrentConversation

`IS_PED_IN_CURRENT_CONVERSATION` · hash `0x049E937F18F4020C` · jhash `0x7B2F0743` · **Cliente**

```lua
local retval = IsPedInCurrentConversation(ped)
```
```c
BOOL IS_PED_IN_CURRENT_CONVERSATION(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns true if the ped is in the currently playing conversation

---
### IsPedRingtonePlaying

`IS_PED_RINGTONE_PLAYING` · hash `0x1E8E5E20937E3137` · jhash `0xFE576EE4` · **Cliente**

```lua
local retval = IsPedRingtonePlaying(ped)
```
```c
BOOL IS_PED_RINGTONE_PLAYING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns true if the peds ringtone is currently playing

---
### IsPlayerVehRadioEnable

`IS_PLAYER_VEH_RADIO_ENABLE` · hash `0x5F43D83FD6738741` · jhash `0x2A3E5E8B` · **Cliente**

```lua
local retval = IsPlayerVehRadioEnable()
```
```c
BOOL IS_PLAYER_VEH_RADIO_ENABLE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5F43D83FD6738741` (`N_0x5f43d83fd6738741`), `_IS_PLAYER_VEHICLE_RADIO_ENABLED` (`IsPlayerVehicleRadioEnabled`)

---
### IsRadioFadedOut

`IS_RADIO_FADED_OUT` · hash `0x0626A247D2405330` · jhash `0x815CAE99` · **Cliente**

```lua
local retval = IsRadioFadedOut()
```
```c
BOOL IS_RADIO_FADED_OUT();
```

**Devuelve:** `BOOL` — Returns true if the radio is currently faded out

**Nombres antiguos (alias):** `0x0626A247D2405330` (`N_0x0626a247d2405330`)

---
### IsRadioRetuning

`IS_RADIO_RETUNING` · hash `0xA151A7394A214E65` · jhash `0xCF29097B` · **Cliente**

```lua
local retval = IsRadioRetuning()
```
```c
BOOL IS_RADIO_RETUNING();
```

**Devuelve:** `BOOL` — Returns true if the radio is tuning to a station

---
### IsRadioStationFavourited

`IS_RADIO_STATION_FAVOURITED` · hash `0x2B1784DB08AFEA79` · **Cliente**

```lua
local retval = IsRadioStationFavourited(radioStation)
```
```c
BOOL IS_RADIO_STATION_FAVOURITED(char* radioStation);
```

**Parámetros**

- `radioStation` (`char*`)

**Devuelve:** `BOOL` — Returns whether a radio station is a favourite.

**Nombres antiguos (alias):** `_IS_RADIO_STATION_VISIBLE` (`IsRadioStationVisible`)

---
### IsScriptedConversationLoaded

`IS_SCRIPTED_CONVERSATION_LOADED` · hash `0xDF0D54BE7A776737` · jhash `0xE1870EA9` · **Cliente**

```lua
local retval = IsScriptedConversationLoaded()
```
```c
BOOL IS_SCRIPTED_CONVERSATION_LOADED();
```

**Devuelve:** `BOOL` — Returns true if the first batch of lines for the currently requested conversation have loaded successfully.

---
### IsScriptedConversationOngoing

`IS_SCRIPTED_CONVERSATION_ONGOING` · hash `0x16754C556D2EDE3D` · jhash `0xCB8FD96F` · **Cliente**

```lua
local retval = IsScriptedConversationOngoing()
```
```c
BOOL IS_SCRIPTED_CONVERSATION_ONGOING();
```

**Devuelve:** `BOOL`

---
### IsScriptedSpeechPlaying

`IS_SCRIPTED_SPEECH_PLAYING` · hash `0xCC9AA18DCC7084F4` · jhash `0x2C653904` · **Cliente**

```lua
local retval = IsScriptedSpeechPlaying(ped)
```
```c
BOOL IS_SCRIPTED_SPEECH_PLAYING(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `BOOL` — Returns true if scripted speech is currently playing from the given ped.

---
### IsStreamPlaying

`IS_STREAM_PLAYING` · hash `0xD11FA52EB849D978` · jhash `0xF1F51A14` · **Cliente**

```lua
local retval = IsStreamPlaying()
```
```c
BOOL IS_STREAM_PLAYING();
```

**Devuelve:** `BOOL` — Returns true if the script is currently playing a stream.

---
### IsVehicleAudiblyDamaged

`IS_VEHICLE_AUDIBLY_DAMAGED` · hash `0x5DB8010EE71FDEF2` · jhash `0x6E660D3F` · **Cliente**

```lua
local retval = IsVehicleAudiblyDamaged(vehicle)
```
```c
BOOL IS_VEHICLE_AUDIBLY_DAMAGED(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL` — Returns true if the vehicle has any audible damage effects applied to it.

**Nombres antiguos (alias):** `0x5DB8010EE71FDEF2` (`N_0x5db8010ee71fdef2`)

---
### IsVehicleRadioOn

`IS_VEHICLE_RADIO_ON` · hash `0x0BE4BE946463F917` · **Cliente**

```lua
local retval = IsVehicleRadioOn(vehicle)
```
```c
BOOL IS_VEHICLE_RADIO_ON(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to check

**Devuelve:** `BOOL` — Returns true if the given vehicle's radio on

**Nombres antiguos (alias):** `0x0BE4BE946463F917` (`N_0x0be4be946463f917`), `_IS_VEHICLE_RADIO_ENABLED` (`IsVehicleRadioEnabled`)

**Ejemplo (lua):**

```lua
local radioEnabled = IsVehicleRadioEnabled(GetVehiclePedIsIn(PlayerPedId(), false))
print(radioEnabled)
```

**Ejemplo (cs):**

```cs
bool radioEnabled = API.IsVehicleRadioEnabled(API.GetVehiclePedIsIn(Game.PlayerPed.Handle, false));
Debug.WriteLine(radioEnabled.ToString());
```

---
### LinkStaticEmitterToEntity

`LINK_STATIC_EMITTER_TO_ENTITY` · hash `0x651D3228960D08AF` · **Cliente**

```lua
LinkStaticEmitterToEntity(emitterName, entity)
```
```c
void LINK_STATIC_EMITTER_TO_ENTITY(char* emitterName, Entity entity);
```

**Parámetros**

- `emitterName` (`char*`)
- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

Links a static emitter to the given entity

**Nombres antiguos (alias):** `0x651D3228960D08AF` (`N_0x651d3228960d08af`), `_LINK_STATIC_EMITTER_TO_ENTITY` (`LinkStaticEmitterToEntity`)

---
### LoadStream

`LOAD_STREAM` · hash `0x1F1F957154EC51DF` · jhash `0x0D89599D` · **Cliente**

```lua
local retval = LoadStream(streamName, soundSet)
```
```c
BOOL LOAD_STREAM(char* streamName, char* soundSet);
```

**Parámetros**

- `streamName` (`char*`)
- `soundSet` (`char*`): an optional sound set, default is null

**Devuelve:** `BOOL`

**Descripción oficial:**

Load in named stream. Optionally can specify a sound set which contains the sound specified by name.

Names for the streams can be found [here](https://gist.github.com/4mmonium/2bd2c9c54d6ca5cbdb7b156a82a3a85a), the list will be updated as more are found.

---
### LoadStreamWithStartOffset

`LOAD_STREAM_WITH_START_OFFSET` · hash `0x59C16B79F53B3712` · jhash `0xE5B5745C` · **Cliente**

```lua
local retval = LoadStreamWithStartOffset(streamName, startOffset, soundSet)
```
```c
BOOL LOAD_STREAM_WITH_START_OFFSET(char* streamName, int startOffset, char* soundSet);
```

**Parámetros**

- `streamName` (`char*`)
- `startOffset` (`int`)
- `soundSet` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Load in named stream. Optionally can specify a sound set which contains the sound specified by name.

---
### LockRadioStation

`LOCK_RADIO_STATION` · hash `0x477D9DB48F889591` · **Cliente**

```lua
LockRadioStation(radioStationName, toggle)
```
```c
void LOCK_RADIO_STATION(char* radioStationName, BOOL toggle);
```

**Parámetros**

- `radioStationName` (`char*`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

This disables the radio station completely - it won't be selectable on the radio wheel or ever be heard coming from a vehicle/ambient emitter

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x94f2e83ead7e6b82` (`N_0x94f2e83ead7e6b82`), `_SET_RADIO_STATION_DISABLED` (`SetRadioStationDisabled`), `_LOCK_RADIO_STATION` (`LockRadioStation`)

---
### LockRadioStationTrackList

`LOCK_RADIO_STATION_TRACK_LIST` · hash `0xFF5E5EA2DCEEACF3` · **Cliente**

```lua
LockRadioStationTrackList(radioStation, trackListName)
```
```c
void LOCK_RADIO_STATION_TRACK_LIST(char* radioStation, char* trackListName);
```

**Parámetros**

- `radioStation` (`char*`)
- `trackListName` (`char*`)

**Devuelve:** `void`

---
### N_0x02e93c796abd3a97

`0x02E93C796ABD3A97` · hash `0x02E93C796ABD3A97` · jhash `0x3C395AEE` · **Cliente**

```lua
N_0x02e93c796abd3a97(p0)
```
```c
void 0x02E93C796ABD3A97(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x11579d940949c49e

`0x11579D940949C49E` · hash `0x11579D940949C49E` · **Cliente**

```lua
N_0x11579d940949c49e(p0)
```
```c
void 0x11579D940949C49E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0x19af7ed9b9d23058

`0x19AF7ED9B9D23058` · hash `0x19AF7ED9B9D23058` · jhash `0xA58BBF4F` · **Cliente**

```lua
N_0x19af7ed9b9d23058()
```
```c
void 0x19AF7ED9B9D23058();
```

**Devuelve:** `void`

---
### N_0x2dd39bf3e2f9c47f

`0x2DD39BF3E2F9C47F` · hash `0x2DD39BF3E2F9C47F` · **Cliente**

```lua
local retval = N_0x2dd39bf3e2f9c47f()
```
```c
Any 0x2DD39BF3E2F9C47F();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v463
```

---
### N_0x43fa0dfc5df87815

`0x43FA0DFC5DF87815` · hash `0x43FA0DFC5DF87815` · jhash `0x7BED1872` · **Cliente**

```lua
N_0x43fa0dfc5df87815(vehicle, p1)
```
```c
void 0x43FA0DFC5DF87815(Vehicle vehicle, BOOL p1);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x55ecf4d13d9903b0

`0x55ECF4D13D9903B0` · hash `0x55ECF4D13D9903B0` · **Cliente**

```lua
N_0x55ecf4d13d9903b0(p0, p1, p2, p3)
```
```c
void 0x55ECF4D13D9903B0(Any p0, Any p1, Any p2, Any p3);
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
### N_0x58bb377bec7cd5f4

`0x58BB377BEC7CD5F4` · hash `0x58BB377BEC7CD5F4` · jhash `0x8CE63FA1` · **Cliente**

```lua
N_0x58bb377bec7cd5f4(p0, p1)
```
```c
void 0x58BB377BEC7CD5F4(BOOL p0, BOOL p1);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)

**Devuelve:** `void`

---
### N_0x5b9853296731e88d

`0x5B9853296731E88D` · hash `0x5B9853296731E88D` · **Cliente**

```lua
N_0x5b9853296731e88d(p0, p1, p2, p3, p4, p5)
```
```c
void 0x5B9853296731E88D(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
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
### N_0x8bf907833be275de

`0x8BF907833BE275DE` · hash `0x8BF907833BE275DE` · jhash `0x2CD26D69` · **Cliente**

```lua
N_0x8bf907833be275de(p0, p1)
```
```c
void 0x8BF907833BE275DE(float p0, float p1);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)

**Devuelve:** `void`

---
### N_0x97ffb4adeed08066

`0x97FFB4ADEED08066` · hash `0x97FFB4ADEED08066` · **Cliente**

```lua
N_0x97ffb4adeed08066(p0, p1)
```
```c
void 0x97FFB4ADEED08066(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

---
### N_0x9ac92eed5e4793ab

`0x9AC92EED5E4793AB` · hash `0x9AC92EED5E4793AB` · jhash `0xE67446E9` · **Cliente**

```lua
N_0x9ac92eed5e4793ab()
```
```c
void 0x9AC92EED5E4793AB();
```

**Devuelve:** `void`

---
### N_0x9bd7bd55e4533183

`0x9BD7BD55E4533183` · hash `0x9BD7BD55E4533183` · **Cliente**

```lua
N_0x9bd7bd55e4533183(p0, p1, p2)
```
```c
void 0x9BD7BD55E4533183(Any p0, Any p1, Any p2);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xb542de8c3d1cb210

`0xB542DE8C3D1CB210` · hash `0xB542DE8C3D1CB210` · jhash `0x789D8C6C` · **Cliente**

```lua
N_0xb542de8c3d1cb210(p0)
```
```c
void 0xB542DE8C3D1CB210(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xbef34b1d9624d5dd

`0xBEF34B1D9624D5DD` · hash `0xBEF34B1D9624D5DD` · jhash `0xE0047BFD` · **Cliente**

```lua
N_0xbef34b1d9624d5dd(p0)
```
```c
void 0xBEF34B1D9624D5DD(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0xc1805d05e6d4fe10

`0xC1805D05E6D4FE10` · hash `0xC1805D05E6D4FE10` · jhash `0x7ABB89D2` · **Cliente**

```lua
N_0xc1805d05e6d4fe10(vehicle)
```
```c
void 0xC1805D05E6D4FE10(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VEH*
```

---
### OverrideMicrophoneSettings

`OVERRIDE_MICROPHONE_SETTINGS` · hash `0x75773E11BA459E90` · **Cliente**

```lua
OverrideMicrophoneSettings(hash, toggle)
```
```c
void OVERRIDE_MICROPHONE_SETTINGS(Hash hash, BOOL toggle);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets audio flag "OverrideMicrophoneSettings"

Allows the script to ovverride the current microphone settings

**Nombres antiguos (alias):** `0x75773E11BA459E90` (`N_0x75773e11ba459e90`), `_OVERRIDE_MICROPHONE_SETTINGS` (`OverrideMicrophoneSettings`)

---
### OverridePlayerGroundMaterial

`OVERRIDE_PLAYER_GROUND_MATERIAL` · hash `0xD2CC78CD3D0B50F9` · jhash `0xC307D531` · **Cliente**

```lua
OverridePlayerGroundMaterial(overriddenMaterialHash, scriptOverrides)
```
```c
void OVERRIDE_PLAYER_GROUND_MATERIAL(Hash overriddenMaterialHash, BOOL scriptOverrides);
```

**Parámetros**

- `overriddenMaterialHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `scriptOverrides` (`BOOL`): True to override with the given overridenMaterialHash, false to stop overriding

**Devuelve:** `void`

**Descripción oficial:**

Sets the footstep tuning modes

**Nombres antiguos (alias):** `0xD2CC78CD3D0B50F9` (`N_0xd2cc78cd3d0b50f9`)

---
### OverrideTrevorRage

`OVERRIDE_TREVOR_RAGE` · hash `0x13AD665062541A7E` · jhash `0x05B9B5CF` · **Cliente**

```lua
OverrideTrevorRage(voiceEffect)
```
```c
void OVERRIDE_TREVOR_RAGE(char* voiceEffect);
```

**Parámetros**

- `voiceEffect` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

This native enables the audio flag "TrevorRageIsOverridden" and sets the voice effect to `voiceEffect`

To clear the override use [RESET_TREVOR_RAGE](#resettrevorrage)

---
### OverrideUnderwaterStream

`OVERRIDE_UNDERWATER_STREAM` · hash `0xF2A9CDABCEA04BD6` · jhash `0x9A083B7E` · **Cliente**

```lua
OverrideUnderwaterStream(streamName, override)
```
```c
void OVERRIDE_UNDERWATER_STREAM(char* streamName, BOOL override);
```

**Parámetros**

- `streamName` (`char*`)
- `override` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

This native allows a scripter to override the current underwater stream.
It needs to be called before going into the water

It needs to also be called with OVERRIDE_UNDERWATER_STREAM("", false) in order to stop overriding.

---
### OverrideVehHorn

`OVERRIDE_VEH_HORN` · hash `0x3CDC1E622CCE0356` · jhash `0x2ACAB783` · **Cliente**

```lua
OverrideVehHorn(vehicle, override, hornHash)
```
```c
void OVERRIDE_VEH_HORN(Vehicle vehicle, BOOL override, int hornHash);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle you want to change the horn on.
- `override` (`BOOL`): Must be set to true. If set to false, the default horn hash will be restored.
- `hornHash` (`int`): A horn hash.

**Devuelve:** `void`

**Descripción oficial:**

Overrides the vehicle's horn hash.

When changing this hash on a vehicle, [`_GET_VEHICLE_HORN_HASH`](#getvehicledefaulthornignoremods) will **not** return the 'overwritten' hash. It will still always return the default horn hash (same as [`GET_VEHICLE_DEFAULT_HORN`](#getvehicledefaulthorn)).

List of possible hashes (found in decompiled scripts):

|        signed |     unsigned |      hex     |
|--------------:|-------------:|:------------:|
|  `1604822495` | `1604822495` | `0x5FA7A5DF` |
| `-1262465009` | `3032502287` | `0xB4C0500F` |
|  `-889553789` | `3405413507` | `0xCAFA7C83` |
| `-1557943086` | `2737024210` | `0xA323ACD2` |
| `-1318696617` | `2976270679` | `0xB1664957` |
|    `-7740003` | `4287227293` | `0xFF89E59D` |
| `-1815146967` | `2479820329` | `0x93CF0E29` |
|  `-339919356` | `3955047940` | `0xEBBD3E04` |

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsIn(PlayerPedId(), false)

-- These are the most common horn hashes found in the decompiled scripts.
local horns = {
    1604822495,
    3032502287,
    3405413507,
    2737024210,
    2976270679,
    4287227293,
    2479820329,
    3955047940
}

local randomHornHash = horns[math.random(1, #horns)]

print(randomHornHash)

OverrideVehHorn(vehicle, true, randomHornHash)
```

---
### PauseScriptedConversation

`PAUSE_SCRIPTED_CONVERSATION` · hash `0x8530AD776CD72B12` · jhash `0xE2C9C6F8` · **Cliente**

```lua
PauseScriptedConversation(finishCurrentLine)
```
```c
void PAUSE_SCRIPTED_CONVERSATION(BOOL finishCurrentLine);
```

**Parámetros**

- `finishCurrentLine` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

To resume the conversation use [RESTART_SCRIPTED_CONVERSATION](#restartscriptedconversation)

---
### PlayAmbientSpeechFromPositionNative

`PLAY_AMBIENT_SPEECH_FROM_POSITION_NATIVE` · hash `0xED640017ED337E45` · jhash `0xA1A1402E` · **Cliente**

```lua
PlayAmbientSpeechFromPositionNative(speechName, voiceName, x, y, z, speechParam)
```
```c
void PLAY_AMBIENT_SPEECH_FROM_POSITION_NATIVE(char* speechName, char* voiceName, float x, float y, float z, char* speechParam);
```

**Parámetros**

- `speechName` (`char*`)
- `voiceName` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `speechParam` (`char*`): See [`PLAY_PED_AMBIENT_SPEECH_NATIVE`](#playpedambientspeechnative) for params

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xED640017ED337E45` (`N_0xed640017ed337e45`), `_PLAY_AMBIENT_SPEECH_AT_COORDS` (`PlayAmbientSpeechAtCoords`)

---
### PlayAnimalVocalization

`PLAY_ANIMAL_VOCALIZATION` · hash `0xEE066C7006C49C0A` · jhash `0x498849F3` · **Cliente**

```lua
PlayAnimalVocalization(pedHandle, animalType, speechName)
```
```c
void PLAY_ANIMAL_VOCALIZATION(Ped pedHandle, int animalType, char* speechName);
```

**Parámetros**

- `pedHandle` (`Ped`)
- `animalType` (`int`)
- `speechName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eAudAnimalType {
	AUD_ANIMAL_NONE = -1,
	AUD_ANIMAL_BOAR = 0,
	AUD_ANIMAL_CHICKEN = 1,
	AUD_ANIMAL_DOG = 2,
	AUD_ANIMAL_DOG_ROTTWEILER = 3,
	AUD_ANIMAL_HORSE = 4,
	AUD_NUM_ANIMALS = 5
}
```

**Nombres antiguos (alias):** `0xEE066C7006C49C0A` (`N_0xee066c7006c49c0a`)

---
### PlayDeferredSoundFrontend

`PLAY_DEFERRED_SOUND_FRONTEND` · hash `0xCADA5A0D0702381E` · jhash `0xC70E6CFA` · **Cliente**

```lua
PlayDeferredSoundFrontend(soundName, soundsetName)
```
```c
void PLAY_DEFERRED_SOUND_FRONTEND(char* soundName, char* soundsetName);
```

**Parámetros**

- `soundName` (`char*`)
- `soundsetName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCADA5A0D0702381E` (`N_0xcada5a0d0702381e`)

---
### PlayEndCreditsMusic

`PLAY_END_CREDITS_MUSIC` · hash `0xCD536C4D33DCC900` · jhash `0x8E88B3CC` · **Cliente**

```lua
PlayEndCreditsMusic(bActive)
```
```c
void PLAY_END_CREDITS_MUSIC(BOOL bActive);
```

**Parámetros**

- `bActive` (`BOOL`)

**Devuelve:** `void`

---
### PlayMissionCompleteAudio

`PLAY_MISSION_COMPLETE_AUDIO` · hash `0xB138AAB8A70D3C69` · jhash `0x3033EA1D` · **Cliente**

```lua
PlayMissionCompleteAudio(audioName)
```
```c
void PLAY_MISSION_COMPLETE_AUDIO(char* audioName);
```

**Parámetros**

- `audioName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Called 38 times in the scripts. There are 5 different audioNames used.
 One unknown removed below.
AUDIO::PLAY_MISSION_COMPLETE_AUDIO("DEAD");
AUDIO::PLAY_MISSION_COMPLETE_AUDIO("FRANKLIN_BIG_01");
AUDIO::PLAY_MISSION_COMPLETE_AUDIO("GENERIC_FAILED");
AUDIO::PLAY_MISSION_COMPLETE_AUDIO("TREVOR_SMALL_01");
```

---
### PlayPain

`PLAY_PAIN` · hash `0xBC9AE166038A5CEC` · jhash `0x874BD6CB` · **Cliente**

```lua
PlayPain(ped, damageReason, rawDamage)
```
```c
void PLAY_PAIN(Ped ped, int damageReason, float rawDamage);
```

**Parámetros**

- `ped` (`Ped`): The ped entity.
- `damageReason` (`int`): The damage reason/type, refer to eAudDamageReason
- `rawDamage` (`float`): Damage value, defaults to 0.0

**Devuelve:** `void`

**Descripción oficial:**

This native had a 4th parameter added in newer game builds
`syncOverNetwork` creates a `CPedPlayPainEvent` when set to true, by default this variable is false.

You won't be able to use this for clones (remote pedestrians that are not owned by you) or migrating peds if `syncOverNetwork` is set to true; it simply won't execute.

The `ped` should also have speech for this to work.

```cpp
enum eAudDamageReason {
	AUD_DAMAGE_REASON_DEFAULT = 0,
	AUD_DAMAGE_REASON_FALLING = 1,
	AUD_DAMAGE_REASON_SUPER_FALLING = 2,
	AUD_DAMAGE_REASON_SCREAM_PANIC = 3,
	AUD_DAMAGE_REASON_SCREAM_PANIC_SHORT = 4,
	AUD_DAMAGE_REASON_SCREAM_SCARED = 5,
	AUD_DAMAGE_REASON_SCREAM_SHOCKED = 6,
	AUD_DAMAGE_REASON_SCREAM_TERROR = 7,
	AUD_DAMAGE_REASON_ON_FIRE = 8,
	AUD_DAMAGE_REASON_DROWNING = 9,
	// drowning on the surface of water, after we time out
	AUD_DAMAGE_REASON_SURFACE_DROWNING = 10,
	AUD_DAMAGE_REASON_INHALE = 11,
	AUD_DAMAGE_REASON_EXHALE = 12,
	AUD_DAMAGE_REASON_POST_FALL_GRUNT = 13,
	AUD_DAMAGE_REASON_ENTERING_RAGDOLL_DEATH = 14,
	AUD_DAMAGE_REASON_EXPLOSION = 15,
	AUD_DAMAGE_REASON_MELEE = 16,
	AUD_DAMAGE_REASON_SHOVE = 17,
	AUD_DAMAGE_REASON_WHEEZE = 18,
	AUD_DAMAGE_REASON_COUGH = 19,
	AUD_DAMAGE_REASON_TAZER = 20,
	AUD_DAMAGE_REASON_EXHAUSTION = 21,
	AUD_DAMAGE_REASON_CLIMB_LARGE = 22,
	AUD_DAMAGE_REASON_CLIMB_SMALL = 23,
	AUD_DAMAGE_REASON_JUMP = 24,
	AUD_DAMAGE_REASON_COWER = 25,
	AUD_DAMAGE_REASON_WHIMPER = 26,
	AUD_DAMAGE_REASON_DYING_MOAN = 27,
	AUD_DAMAGE_REASON_CYCLING_EXHALE = 28,
	AUD_DAMAGE_REASON_PAIN_RAPIDS = 29,
	AUD_DAMAGE_REASON_SNEEZE = 30,
	AUD_DAMAGE_REASON_MELEE_SMALL_GRUNT = 31,
	AUD_DAMAGE_REASON_MELEE_LARGE_GRUNT = 32,
	AUD_DAMAGE_REASON_POST_FALL_GRUNT_LOW = 33
}
```

**Ejemplo (lua):**

```lua
-- Play ON_FIRE (8) for all nearby peds, don't create an event (last parameter set to false)
for _, ped in ipairs(GetGamePool('CPed')) do
    PlayPain(ped, 8, 0.0, false)
end
```

---
### PlayPedAmbientSpeechAndCloneNative

`PLAY_PED_AMBIENT_SPEECH_AND_CLONE_NATIVE` · hash `0xC6941B4A3A8FBBB9` · jhash `0x444180DB` · **Cliente**

```lua
PlayPedAmbientSpeechAndCloneNative(ped, speechName, speechParam)
```
```c
void PLAY_PED_AMBIENT_SPEECH_AND_CLONE_NATIVE(Ped ped, char* speechName, char* speechParam);
```

**Parámetros**

- `ped` (`Ped`)
- `speechName` (`char*`)
- `speechParam` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

See [`PLAY_PED_AMBIENT_SPEECH_NATIVE`](#playpedambientspeechnative) for parameter specifications.

```
NativeDB Added Parameter 4: Any p3
```

**Nombres antiguos (alias):** `_PLAY_AMBIENT_SPEECH2` (`PlayAmbientSpeech2`)

---
### PlayPedAmbientSpeechNative

`PLAY_PED_AMBIENT_SPEECH_NATIVE` · hash `0x8E04FEDD28D42462` · jhash `0x5C57B85D` · **Cliente**

```lua
PlayPedAmbientSpeechNative(ped, speechName, speechParam)
```
```c
void PLAY_PED_AMBIENT_SPEECH_NATIVE(Ped ped, char* speechName, char* speechParam);
```

**Parámetros**

- `ped` (`Ped`): The ped to play the ambient speech.
- `speechName` (`char*`): Name of the speech to play, eg. "GENERIC_HI".
- `speechParam` (`char*`): Name of the speechParam rage game object to look to for various details on how the speech should be played.

**Devuelve:** `void`

**Descripción oficial:**

Plays ambient speech; see also [`PLAY_PED_AMBIENT_SPEECH_AND_CLONE_NATIVE`](#playpedambientspeechandclonenative). Some speeches only play on certain ped models.

A full list of speech names can be found [here](https://docs.fivem.net/docs/game-references/speeches/).

```cpp
static const char *SpeechParams[] = {
    "SPEECH_PARAMS_ADD_BLIP",
    "SPEECH_PARAMS_ADD_BLIP_ALLOW_REPEAT",
    "SPEECH_PARAMS_ADD_BLIP_FORCE",
    "SPEECH_PARAMS_ADD_BLIP_INTERRUPT",
    "SPEECH_PARAMS_ADD_BLIP_INTERRUPT_FORCE",
    "SPEECH_PARAMS_ADD_BLIP_SHOUTED",
    "SPEECH_PARAMS_ADD_BLIP_SHOUTED_FORCE",
    "SPEECH_PARAMS_ALLOW_REPEAT",
    "SPEECH_PARAMS_BEAT",
    "SPEECH_PARAMS_FORCE",
    "SPEECH_PARAMS_FORCE_FRONTEND",
    "SPEECH_PARAMS_FORCE_HELI",
    "SPEECH_PARAMS_FORCE_MEGAPHONE",
    "SPEECH_PARAMS_FORCE_NO_REPEAT_FRONTEND",
    "SPEECH_PARAMS_FORCE_NORMAL",
    "SPEECH_PARAMS_FORCE_NORMAL_CLEAR",
    "SPEECH_PARAMS_FORCE_NORMAL_CRITICAL",
    "SPEECH_PARAMS_FORCE_PRELOAD_ONLY",
    "SPEECH_PARAMS_FORCE_PRELOAD_ONLY_SHOUTED",
    "SPEECH_PARAMS_FORCE_PRELOAD_ONLY_SHOUTED_CLEAR",
    "SPEECH_PARAMS_FORCE_PRELOAD_ONLY_SHOUTED_CRITICAL",
    "SPEECH_PARAMS_FORCE_SHOUTED",
    "SPEECH_PARAMS_FORCE_SHOUTED_CLEAR",
    "SPEECH_PARAMS_FORCE_SHOUTED_CRITICAL",
    "SPEECH_PARAMS_HELI",
    "SPEECH_PARAMS_INTERRUPT",
    "SPEECH_PARAMS_INTERRUPT_FRONTEND",
    "SPEECH_PARAMS_INTERRUPT_NO_FORCE",
    "SPEECH_PARAMS_INTERRUPT_NO_FORCE_FRONTEND",
    "SPEECH_PARAMS_INTERRUPT_SHOUTED",
    "SPEECH_PARAMS_INTERRUPT_SHOUTED_CLEAR",
    "SPEECH_PARAMS_INTERRUPT_SHOUTED_CRITICAL",
    "SPEECH_PARAMS_MEGAPHONE",
    "SPEECH_PARAMS_SHOUTED",
    "SPEECH_PARAMS_SHOUTED_CLEAR",
    "SPEECH_PARAMS_SHOUTED_CRITICAL",
    "SPEECH_PARAMS_STANDARD"
}
```

**Nombres antiguos (alias):** `_PLAY_AMBIENT_SPEECH1` (`PlayAmbientSpeech1`)

---
### PlayPedAmbientSpeechWithVoiceNative

`PLAY_PED_AMBIENT_SPEECH_WITH_VOICE_NATIVE` · hash `0x3523634255FC3318` · jhash `0x8386AE28` · **Cliente**

```lua
PlayPedAmbientSpeechWithVoiceNative(ped, speechName, voiceName, speechParam, p4)
```
```c
void PLAY_PED_AMBIENT_SPEECH_WITH_VOICE_NATIVE(Ped ped, char* speechName, char* voiceName, char* speechParam, BOOL p4);
```

**Parámetros**

- `ped` (`Ped`)
- `speechName` (`char*`)
- `voiceName` (`char*`)
- `speechParam` (`char*`)
- `p4` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This is the same as PLAY_PED_AMBIENT_SPEECH_NATIVE and PLAY_PED_AMBIENT_SPEECH_AND_CLONE_NATIVE but it will allow you to play a speech file from a specific voice file. It works on players and all peds, even animals.
EX (C#):
GTA.Native.Function.Call(Hash._0x3523634255FC3318, Game.Player.Character, "GENERIC_INSULT_HIGH", "s_m_y_sheriff_01_white_full_01", "SPEECH_PARAMS_FORCE_SHOUTED", 0);
The first param is the ped you want to play it on, the second is the speech name, the third is the voice name, the fourth is the speech param, and the last param is usually always 0.
```

**Nombres antiguos (alias):** `_PLAY_AMBIENT_SPEECH_WITH_VOICE` (`PlayAmbientSpeechWithVoice`)

---
### PlayPedRingtone

`PLAY_PED_RINGTONE` · hash `0xF9E56683CA8E11A5` · jhash `0x1D530E47` · **Cliente**

```lua
PlayPedRingtone(ringtoneName, ped, p2)
```
```c
void PLAY_PED_RINGTONE(char* ringtoneName, Ped ped, BOOL p2);
```

**Parámetros**

- `ringtoneName` (`char*`)
- `ped` (`Ped`)
- `p2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
All found occurrences in b617d, sorted alphabetically and identical lines removed: pastebin.com/RFb4GTny  
AUDIO::PLAY_PED_RINGTONE("Remote_Ring", PLAYER::PLAYER_PED_ID(), 1);  
AUDIO::PLAY_PED_RINGTONE("Dial_and_Remote_Ring", PLAYER::PLAYER_PED_ID(), 1);  
```

---
### PlayPoliceReport

`PLAY_POLICE_REPORT` · hash `0xDFEBD56D9BD1EB16` · jhash `0x3F277B62` · **Cliente**

```lua
local retval = PlayPoliceReport(name, p1)
```
```c
int PLAY_POLICE_REPORT(char* name, float p1);
```

**Parámetros**

- `name` (`char*`)
- `p1` (`float`)

**Devuelve:** `int`

**Descripción oficial:**

```
Plays the given police radio message.
All found occurrences in b617d, sorted alphabetically and identical lines removed: pastebin.com/GBnsQ5hr
```

---
### PlaySound

`PLAY_SOUND` · hash `0x7FF4944CC209192D` · jhash `0xB6E1917F` · **Cliente**

```lua
PlaySound(soundId, audioName, audioRef, p3, p4, p5)
```
```c
void PLAY_SOUND(int soundId, char* audioName, char* audioRef, BOOL p3, Any p4, BOOL p5);
```

**Parámetros**

- `soundId` (`int`)
- `audioName` (`char*`)
- `audioRef` (`char*`)
- `p3` (`BOOL`)
- `p4` (`Any`)
- `p5` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
All found occurrences in b617d, sorted alphabetically and identical lines removed: pastebin.com/A8Ny8AHZ  
```

---
### PlaySoundFromCoord

`PLAY_SOUND_FROM_COORD` · hash `0x8D8686B622B88120` · jhash `0xCAD3E2D5` · **Cliente**

```lua
PlaySoundFromCoord(soundId, audioName, x, y, z, audioRef, isNetwork, range, p8)
```
```c
void PLAY_SOUND_FROM_COORD(int soundId, char* audioName, float x, float y, float z, char* audioRef, BOOL isNetwork, int range, BOOL p8);
```

**Parámetros**

- `soundId` (`int`)
- `audioName` (`char*`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `audioRef` (`char*`)
- `isNetwork` (`BOOL`)
- `range` (`int`)
- `p8` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
All found occurrences in b617d, sorted alphabetically and identical lines removed: pastebin.com/eeFc5DiW  
gtaforums.com/topic/795622-audio-for-mods  
```

---
### PlaySoundFromEntity

`PLAY_SOUND_FROM_ENTITY` · hash `0xE65F427EB70AB1ED` · jhash `0x95AE00F8` · **Cliente**

```lua
PlaySoundFromEntity(soundId, audioName, entity, audioRef, isNetwork, p5)
```
```c
void PLAY_SOUND_FROM_ENTITY(int soundId, char* audioName, Entity entity, char* audioRef, BOOL isNetwork, Any p5);
```

**Parámetros**

- `soundId` (`int`)
- `audioName` (`char*`)
- `entity` (`Entity`)
- `audioRef` (`char*`)
- `isNetwork` (`BOOL`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
All found occurrences in b617d, sorted alphabetically and identical lines removed: pastebin.com/f2A7vTj0   
No changes made in b678d.  
gtaforums.com/topic/795622-audio-for-mods  
```

---
### PlaySoundFrontend

`PLAY_SOUND_FRONTEND` · hash `0x67C540AA08E4A6F5` · jhash `0x2E458F74` · **Cliente**

```lua
PlaySoundFrontend(soundId, audioName, audioRef, p3)
```
```c
void PLAY_SOUND_FRONTEND(int soundId, char* audioName, char* audioRef, BOOL p3);
```

**Parámetros**

- `soundId` (`int`)
- `audioName` (`char*`)
- `audioRef` (`char*`)
- `p3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
List: https://pastebin.com/DCeRiaLJ
All occurrences as of Cayo Perico Heist DLC (b2189), sorted alphabetically and identical lines removed: https://git.io/JtLxM
```

---
### PlayStreamFromObject

`PLAY_STREAM_FROM_OBJECT` · hash `0xEBAA9B64D76356FD` · jhash `0xC5266BF7` · **Cliente**

```lua
PlayStreamFromObject(object)
```
```c
void PLAY_STREAM_FROM_OBJECT(Object object);
```

**Parámetros**

- `object` (`Object`)

**Devuelve:** `void`

**Descripción oficial:**

Plays a preloaded stream back from the specified object.

---
### PlayStreamFromPed

`PLAY_STREAM_FROM_PED` · hash `0x89049DD63C08B5D1` · jhash `0xA1D7FABE` · **Cliente**

```lua
PlayStreamFromPed(ped)
```
```c
void PLAY_STREAM_FROM_PED(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

Plays a preloaded stream back from the specified ped.

**Nombres antiguos (alias):** `0x89049DD63C08B5D1` (`N_0x89049dd63c08b5d1`)

---
### PlayStreamFromPosition

`PLAY_STREAM_FROM_POSITION` · hash `0x21442F412E8DE56B` · jhash `0x6FE5D865` · **Cliente**

```lua
PlayStreamFromPosition(x, y, z)
```
```c
void PLAY_STREAM_FROM_POSITION(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Plays a preloaded stream back from the specified Vector3.

**Nombres antiguos (alias):** `SPECIAL_FRONTEND_EQUAL` (`SpecialFrontendEqual`)

---
### PlayStreamFromVehicle

`PLAY_STREAM_FROM_VEHICLE` · hash `0xB70374A758007DFA` · jhash `0xF8E4BDA2` · **Cliente**

```lua
PlayStreamFromVehicle(vehicle)
```
```c
void PLAY_STREAM_FROM_VEHICLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

Plays a preloaded stream back from the specified ped vehicle

---
### PlayStreamFrontend

`PLAY_STREAM_FRONTEND` · hash `0x58FCE43488F9F5F4` · jhash `0x2C2A16BC` · **Cliente**

```lua
PlayStreamFrontend()
```
```c
void PLAY_STREAM_FRONTEND();
```

**Devuelve:** `void`

---
### PlaySynchronizedAudioEvent

`PLAY_SYNCHRONIZED_AUDIO_EVENT` · hash `0x8B2FD4560E55DD2D` · jhash `0x507F3241` · **Cliente**

```lua
local retval = PlaySynchronizedAudioEvent(sceneId)
```
```c
BOOL PLAY_SYNCHRONIZED_AUDIO_EVENT(int sceneId);
```

**Parámetros**

- `sceneId` (`int`)

**Devuelve:** `BOOL`

---
### PlayVehicleDoorCloseSound

`PLAY_VEHICLE_DOOR_CLOSE_SOUND` · hash `0x62A456AA4769EF34` · jhash `0xBA2CF407` · **Cliente**

```lua
PlayVehicleDoorCloseSound(vehicle, doorIndex)
```
```c
void PLAY_VEHICLE_DOOR_CLOSE_SOUND(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)

**Devuelve:** `void`

---
### PlayVehicleDoorOpenSound

`PLAY_VEHICLE_DOOR_OPEN_SOUND` · hash `0x3A539D52857EA82D` · jhash `0x84930330` · **Cliente**

```lua
PlayVehicleDoorOpenSound(vehicle, doorIndex)
```
```c
void PLAY_VEHICLE_DOOR_OPEN_SOUND(Vehicle vehicle, int doorIndex);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `doorIndex` (`int`)

**Devuelve:** `void`

---
### PreloadScriptConversation

`PRELOAD_SCRIPT_CONVERSATION` · hash `0x3B3CAD6166916D87` · jhash `0xDDF5C579` · **Cliente**

```lua
PreloadScriptConversation(displaySubtitles, addToBriefScreen, cloneConversation, interruptible)
```
```c
void PRELOAD_SCRIPT_CONVERSATION(BOOL displaySubtitles, BOOL addToBriefScreen, BOOL cloneConversation, BOOL interruptible);
```

**Parámetros**

- `displaySubtitles` (`BOOL`)
- `addToBriefScreen` (`BOOL`): Defaults to true
- `cloneConversation` (`BOOL`): Defaults to false
- `interruptible` (`BOOL`): Defaults to true

**Devuelve:** `void`

**Descripción oficial:**

Similar to [START_SCRIPT_CONVERSATION](#startscriptconversation), except that is starts the conversation off paused.

A scripter can then kick off the conversation by calling [START_PRELOADED_CONVERSATION](#startpreloadedconversation).

If they want to check that the conversation is done preloading, they can use [GET_IS_PRELOADED_CONVERSATION_READY](#getispreloadedconversationready)

---
### PreloadScriptPhoneConversation

`PRELOAD_SCRIPT_PHONE_CONVERSATION` · hash `0x6004BCB0E226AAEA` · jhash `0x9ACB213A` · **Cliente**

```lua
PreloadScriptPhoneConversation(displaySubtitles, addToBriefScreen)
```
```c
void PRELOAD_SCRIPT_PHONE_CONVERSATION(BOOL displaySubtitles, BOOL addToBriefScreen);
```

**Parámetros**

- `displaySubtitles` (`BOOL`)
- `addToBriefScreen` (`BOOL`): Defaults to true

**Devuelve:** `void`

---
### PreloadVehicleAudioBank

`PRELOAD_VEHICLE_AUDIO_BANK` · hash `0xCA4CEA6AE0000A7E` · **Cliente**

```lua
PreloadVehicleAudioBank(model)
```
```c
void PRELOAD_VEHICLE_AUDIO_BANK(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

Request that we preload the required audio bank for a given vehicle model.

```
NativeDB Introduced: v1180
```

**Nombres antiguos (alias):** `0xCA4CEA6AE0000A7E` (`N_0xca4cea6ae0000a7e`), `_PRELOAD_VEHICLE_AUDIO` (`PreloadVehicleAudio`)

---
### PrepareAlarm

`PREPARE_ALARM` · hash `0x9D74AE343DB65533` · jhash `0x084932E8` · **Cliente**

```lua
local retval = PrepareAlarm(alarmName)
```
```c
BOOL PREPARE_ALARM(char* alarmName);
```

**Parámetros**

- `alarmName` (`char*`)

**Devuelve:** `BOOL` — Returns true if the alarm was successfully prepared

**Descripción oficial:**

Prepares any banks required to play the given alarm

---
### PrepareMusicEvent

`PREPARE_MUSIC_EVENT` · hash `0x1E5185B72EF5158A` · jhash `0x534A5C1C` · **Cliente**

```lua
local retval = PrepareMusicEvent(eventName)
```
```c
BOOL PREPARE_MUSIC_EVENT(char* eventName);
```

**Parámetros**

- `eventName` (`char*`)

**Devuelve:** `BOOL` — Returns true if the event is prepared, false otherwise

**Descripción oficial:**

Prepares the specified music event. Preparing it in advance will preload any required data so that it's ready to play immediately.

---
### PrepareSynchronizedAudioEvent

`PREPARE_SYNCHRONIZED_AUDIO_EVENT` · hash `0xC7ABCACA4985A766` · jhash `0xE1D91FD0` · **Cliente**

```lua
local retval = PrepareSynchronizedAudioEvent(audioEvent, startOffsetMs)
```
```c
BOOL PREPARE_SYNCHRONIZED_AUDIO_EVENT(char* audioEvent, int startOffsetMs);
```

**Parámetros**

- `audioEvent` (`char*`): The audio event name.
- `startOffsetMs` (`int`): Unused parameter (since v323)

**Devuelve:** `BOOL`

---
### PrepareSynchronizedAudioEventForScene

`PREPARE_SYNCHRONIZED_AUDIO_EVENT_FOR_SCENE` · hash `0x029FE7CD1B7E2E75` · jhash `0x7652DD49` · **Cliente**

```lua
local retval = PrepareSynchronizedAudioEventForScene(sceneId, audioEvent)
```
```c
BOOL PREPARE_SYNCHRONIZED_AUDIO_EVENT_FOR_SCENE(int sceneId, char* audioEvent);
```

**Parámetros**

- `sceneId` (`int`)
- `audioEvent` (`char*`)

**Devuelve:** `BOOL` — Returns true if prepared, false otherwise

---
### RecordBrokenGlass

`RECORD_BROKEN_GLASS` · hash `0xFBE20329593DEC9D` · jhash `0x53FC3FEC` · **Cliente**

```lua
RecordBrokenGlass(x, y, z, radius)
```
```c
void RECORD_BROKEN_GLASS(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Creates a broken glass area

**Nombres antiguos (alias):** `0xFBE20329593DEC9D` (`N_0xfbe20329593dec9d`)

---
### RefreshClosestOceanShoreline

`REFRESH_CLOSEST_OCEAN_SHORELINE` · hash `0x5D2BFAAB8D956E0E` · **Cliente**

```lua
RefreshClosestOceanShoreline()
```
```c
void REFRESH_CLOSEST_OCEAN_SHORELINE();
```

**Devuelve:** `void`

**Descripción oficial:**

Refreshes the closest shoreline using the nearest road position.

**Nombres antiguos (alias):** `0x5D2BFAAB8D956E0E` (`N_0x5d2bfaab8d956e0e`)

---
### RegisterScriptWithAudio

`REGISTER_SCRIPT_WITH_AUDIO` · hash `0xC6ED9D5092438D91` · jhash `0xA6203643` · **Cliente**

```lua
RegisterScriptWithAudio(inChargeOfAudio)
```
```c
void REGISTER_SCRIPT_WITH_AUDIO(BOOL inChargeOfAudio);
```

**Parámetros**

- `inChargeOfAudio` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### ReleaseAmbientAudioBank

`RELEASE_AMBIENT_AUDIO_BANK` · hash `0x65475A218FFAA93D` · jhash `0x8C938784` · **Cliente**

```lua
ReleaseAmbientAudioBank()
```
```c
void RELEASE_AMBIENT_AUDIO_BANK();
```

**Devuelve:** `void`

**Descripción oficial:**

This native has been marked as deprecated internally, please use [RELEASE_SCRIPT_AUDIO_BANK](#releasescriptaudiobank) instead.

---
### ReleaseMissionAudioBank

`RELEASE_MISSION_AUDIO_BANK` · hash `0x0EC92A1BF0857187` · jhash `0x8E8824C7` · **Cliente**

```lua
ReleaseMissionAudioBank()
```
```c
void RELEASE_MISSION_AUDIO_BANK();
```

**Devuelve:** `void`

**Descripción oficial:**

This native has been marked as deprecated internally, please use [RELEASE_SCRIPT_AUDIO_BANK](#releasescriptaudiobank) instead.

---
### ReleaseNamedScriptAudioBank

`RELEASE_NAMED_SCRIPT_AUDIO_BANK` · hash `0x77ED170667F50170` · jhash `0x16707ABC` · **Cliente**

```lua
ReleaseNamedScriptAudioBank(audioBank)
```
```c
void RELEASE_NAMED_SCRIPT_AUDIO_BANK(char* audioBank);
```

**Parámetros**

- `audioBank` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Unloads the specified audioBank

---
### ReleaseScriptAudioBank

`RELEASE_SCRIPT_AUDIO_BANK` · hash `0x7A2D8AD0A9EB9C3F` · jhash `0x22F865E5` · **Cliente**

```lua
ReleaseScriptAudioBank()
```
```c
void RELEASE_SCRIPT_AUDIO_BANK();
```

**Devuelve:** `void`

**Descripción oficial:**

Unloads all audio banks requested by this script.

---
### ReleaseSoundId

`RELEASE_SOUND_ID` · hash `0x353FC880830B88FA` · jhash `0x9C080899` · **Cliente**

```lua
ReleaseSoundId(soundId)
```
```c
void RELEASE_SOUND_ID(int soundId);
```

**Parámetros**

- `soundId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

This should be called once a sound has finished being manipulated by the script so that its SoundId can be released and re-used.

---
### ReleaseWeaponAudio

`RELEASE_WEAPON_AUDIO` · hash `0xCE4AC0439F607045` · jhash `0x6096504C` · **Cliente**

```lua
ReleaseWeaponAudio()
```
```c
void RELEASE_WEAPON_AUDIO();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### RemoveEntityFromAudioMixGroup

`REMOVE_ENTITY_FROM_AUDIO_MIX_GROUP` · hash `0x18EB48CFC41F2EA0` · jhash `0x308ED0EC` · **Cliente**

```lua
RemoveEntityFromAudioMixGroup(entity, fadeOut)
```
```c
void REMOVE_ENTITY_FROM_AUDIO_MIX_GROUP(Entity entity, float fadeOut);
```

**Parámetros**

- `entity` (`Entity`)
- `fadeOut` (`float`): Defaults to 0.0

**Devuelve:** `void`

**Descripción oficial:**

Removes an entity from its current mix group.

**Nombres antiguos (alias):** `0x18EB48CFC41F2EA0` (`N_0x18eb48cfc41f2ea0`)

---
### RemovePortalSettingsOverride

`REMOVE_PORTAL_SETTINGS_OVERRIDE` · hash `0xB4BBFD9CD8B3922B` · jhash `0xD24B4D0C` · **Cliente**

```lua
RemovePortalSettingsOverride(portalSettingsName)
```
```c
void REMOVE_PORTAL_SETTINGS_OVERRIDE(char* portalSettingsName);
```

**Parámetros**

- `portalSettingsName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
 Found in the b617d scripts, duplicates removed:
 AUDIO::_B4BBFD9CD8B3922B("V_CARSHOWROOM_PS_WINDOW_UNBROKEN");
 AUDIO::_B4BBFD9CD8B3922B("V_CIA_PS_WINDOW_UNBROKEN");
 AUDIO::_B4BBFD9CD8B3922B("V_DLC_HEIST_APARTMENT_DOOR_CLOSED");
 AUDIO::_B4BBFD9CD8B3922B("V_FINALEBANK_PS_VAULT_INTACT");
 AUDIO::_B4BBFD9CD8B3922B("V_MICHAEL_PS_BATHROOM_WITH_WINDOW");
```

For events like cars driving through windows, allows script to unocclude that window

**Nombres antiguos (alias):** `0xB4BBFD9CD8B3922B` (`N_0xb4bbfd9cd8b3922b`)

---
### RequestAmbientAudioBank

`REQUEST_AMBIENT_AUDIO_BANK` · hash `0xFE02FFBED8CA9D99` · jhash `0x23C88BC7` · **Cliente**

```lua
local retval = RequestAmbientAudioBank(bankName, bOverNetwork)
```
```c
BOOL REQUEST_AMBIENT_AUDIO_BANK(char* bankName, BOOL bOverNetwork);
```

**Parámetros**

- `bankName` (`char*`)
- `bOverNetwork` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

This native is marked as deprecated internally, please use [REQUEST_SCRIPT_AUDIO_BANK](#requestscriptaudiobank)

This native has a new argument on newer game builds:

*   **playerBits**:

---
### RequestMissionAudioBank

`REQUEST_MISSION_AUDIO_BANK` · hash `0x7345BDD95E62E0F2` · jhash `0x916E37CA` · **Cliente**

```lua
local retval = RequestMissionAudioBank(bankName, bOverNetwork)
```
```c
BOOL REQUEST_MISSION_AUDIO_BANK(char* bankName, BOOL bOverNetwork);
```

**Parámetros**

- `bankName` (`char*`)
- `bOverNetwork` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

This native is marked as deprecated internally, please use [REQUEST_SCRIPT_AUDIO_BANK](#requestscriptaudiobank)

This native has a new argument on newer game builds:

*   **playerBits**:

---
### RequestScriptAudioBank

`REQUEST_SCRIPT_AUDIO_BANK` · hash `0x2F844A8B08D76685` · jhash `0x21322887` · **Cliente**

```lua
local retval = RequestScriptAudioBank(bankName, bOverNetwork)
```
```c
BOOL REQUEST_SCRIPT_AUDIO_BANK(char* bankName, BOOL bOverNetwork);
```

**Parámetros**

- `bankName` (`char*`)
- `bOverNetwork` (`BOOL`)

**Devuelve:** `BOOL` — Requests and returns true/false if the script audio bank has laoded

**Descripción oficial:**

This native has a new argument on newer game builds:

*   **playerBits**:

---
### RequestTennisBanks

`REQUEST_TENNIS_BANKS` · hash `0x4ADA3F19BE4A6047` · jhash `0x13777A0B` · **Cliente**

```lua
RequestTennisBanks(opponentPed)
```
```c
void REQUEST_TENNIS_BANKS(Ped opponentPed);
```

**Parámetros**

- `opponentPed` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

Loads the tennis vocalization banks into a couple animal slots.

**Nombres antiguos (alias):** `0x4ADA3F19BE4A6047` (`N_0x4ada3f19be4a6047`), `_SET_PED_TALK` (`SetPedTalk`)

---
### ResetPedAudioFlags

`RESET_PED_AUDIO_FLAGS` · hash `0xF54BB7B61036F335` · jhash `0xDF720C86` · **Cliente**

```lua
ResetPedAudioFlags(ped)
```
```c
void RESET_PED_AUDIO_FLAGS(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

---
### ResetTrevorRage

`RESET_TREVOR_RAGE` · hash `0xE78503B10C4314E0` · jhash `0xE80CF0D4` · **Cliente**

```lua
ResetTrevorRage()
```
```c
void RESET_TREVOR_RAGE();
```

**Devuelve:** `void`

**Descripción oficial:**

Clears the override set by [OVERRIDE_TREVOR_RAGE](#overridetrevorrage)

---
### ResetVehicleStartupRevSound

`RESET_VEHICLE_STARTUP_REV_SOUND` · hash `0xD2DCCD8E16E20997` · **Cliente**

```lua
ResetVehicleStartupRevSound(vehicle)
```
```c
void RESET_VEHICLE_STARTUP_REV_SOUND(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

Resets the override for [SET_VEHICLE_STARTUP_REV_SOUND](#setvehiclestartuprevsound)

**Nombres antiguos (alias):** `0xD2DCCD8E16E20997` (`N_0xd2dccd8e16e20997`)

---
### RestartScriptedConversation

`RESTART_SCRIPTED_CONVERSATION` · hash `0x9AEB285D1818C9AC` · jhash `0x6CB24B56` · **Cliente**

```lua
RestartScriptedConversation()
```
```c
void RESTART_SCRIPTED_CONVERSATION();
```

**Devuelve:** `void`

**Descripción oficial:**

Restarts a conversation that was previously paused with [PAUSE_SCRIPTED_CONVERSATION](#pausescriptedconversation)

---
### ScriptOverridesWindElevation

`SCRIPT_OVERRIDES_WIND_ELEVATION` · hash `0x70B8EC8FC108A634` · jhash `0x95050CAD` · **Cliente**

```lua
ScriptOverridesWindElevation(override, windElevationHashName)
```
```c
void SCRIPT_OVERRIDES_WIND_ELEVATION(BOOL override, Hash windElevationHashName);
```

**Parámetros**

- `override` (`BOOL`)
- `windElevationHashName` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

Overrides wind elevation sounds

**Nombres antiguos (alias):** `0x70B8EC8FC108A634` (`N_0x70b8ec8fc108a634`)

---
### SetAggressiveHorns

`SET_AGGRESSIVE_HORNS` · hash `0x395BF71085D1B1D9` · jhash `0x01D6EABE` · **Cliente**

```lua
SetAggressiveHorns(toggle)
```
```c
void SET_AGGRESSIVE_HORNS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Makes pedestrians sound their horn longer, faster and more agressive when they use their horn.

---
### SetAmbientVoiceName

`SET_AMBIENT_VOICE_NAME` · hash `0x6C8065A3B780185B` · jhash `0xBD2EA1A1` · **Cliente**

```lua
SetAmbientVoiceName(ped, voiceName)
```
```c
void SET_AMBIENT_VOICE_NAME(Ped ped, char* voiceName);
```

**Parámetros**

- `ped` (`Ped`)
- `voiceName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the specified ped to use a specific voice different to the one associated with their model.

---
### SetAmbientVoiceNameHash

`SET_AMBIENT_VOICE_NAME_HASH` · hash `0x9A53DED9921DE990` · **Cliente**

```lua
SetAmbientVoiceNameHash(ped, hash)
```
```c
void SET_AMBIENT_VOICE_NAME_HASH(Ped ped, Hash hash);
```

**Parámetros**

- `ped` (`Ped`)
- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

Sets the specified ped to use a specific voice different to the one associated with their model.

**Nombres antiguos (alias):** `0x9A53DED9921DE990` (`N_0x9a53ded9921de990`), `_SET_AMBIENT_VOICE_NAME_HASH` (`SetAmbientVoiceNameHash`)

---
### SetAmbientZoneListState

`SET_AMBIENT_ZONE_LIST_STATE` · hash `0x9748FA4DE50CCE3E` · jhash `0xBF80B412` · **Cliente**

```lua
SetAmbientZoneListState(zoneListName, enabled, forceUpdate)
```
```c
void SET_AMBIENT_ZONE_LIST_STATE(char* zoneListName, BOOL enabled, BOOL forceUpdate);
```

**Parámetros**

- `zoneListName` (`char*`)
- `enabled` (`BOOL`): Enables/disables a list of ambient zones for the duration of this script
- `forceUpdate` (`BOOL`): Set to true to force a zone to become disabled even if its currently active, default behaviour is to only change state when the player leaves the zone.

**Devuelve:** `void`

---
### SetAmbientZoneListStatePersistent

`SET_AMBIENT_ZONE_LIST_STATE_PERSISTENT` · hash `0xF3638DAE8C4045E1` · jhash `0x5F5A2605` · **Cliente**

```lua
SetAmbientZoneListStatePersistent(ambientZone, enabled, forceUpdate)
```
```c
void SET_AMBIENT_ZONE_LIST_STATE_PERSISTENT(char* ambientZone, BOOL enabled, BOOL forceUpdate);
```

**Parámetros**

- `ambientZone` (`char*`)
- `enabled` (`BOOL`): Enables/disables a list of ambient zones persistently
- `forceUpdate` (`BOOL`): Set to true to force a zone to become disabled even if its currently active, default behaviour is to only change state when the player leaves the zone.

**Devuelve:** `void`

---
### SetAmbientZoneState

`SET_AMBIENT_ZONE_STATE` · hash `0xBDA07E5950085E46` · jhash `0x2849CAC9` · **Cliente**

```lua
SetAmbientZoneState(zoneName, enabled, forceUpdate)
```
```c
void SET_AMBIENT_ZONE_STATE(char* zoneName, BOOL enabled, BOOL forceUpdate);
```

**Parámetros**

- `zoneName` (`char*`)
- `enabled` (`BOOL`): Enables/disables an ambient zone for the duration of this script
- `forceUpdate` (`BOOL`): Set to true to force a zone to become disabled even if its currently active, default behaviour is to only change state when the player leaves the zone.

**Devuelve:** `void`

---
### SetAmbientZoneStatePersistent

`SET_AMBIENT_ZONE_STATE_PERSISTENT` · hash `0x1D6650420CEC9D3B` · jhash `0xC1FFB672` · **Cliente**

```lua
SetAmbientZoneStatePersistent(zoneName, enabled, forceUpdate)
```
```c
void SET_AMBIENT_ZONE_STATE_PERSISTENT(char* zoneName, BOOL enabled, BOOL forceUpdate);
```

**Parámetros**

- `zoneName` (`char*`)
- `enabled` (`BOOL`): Enables/disables an ambient zone for the duration of this script
- `forceUpdate` (`BOOL`): Set to true to force a zone to become disabled even if its currently active, default behaviour is to only change state when the player leaves the zone.

**Devuelve:** `void`

---
### SetAnimalMood

`SET_ANIMAL_MOOD` · hash `0xCC97B29285B1DC3B` · jhash `0x3EA7C6CB` · **Cliente**

```lua
SetAnimalMood(animal, mood)
```
```c
void SET_ANIMAL_MOOD(Ped animal, int mood);
```

**Parámetros**

- `animal` (`Ped`)
- `mood` (`int`): Refer to `eAudAnimalMood`

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eAudAnimalMood {
	AUD_ANIMAL_MOOD_ANGRY = 0,
	AUD_ANIMAL_MOOD_PLAYFUL = 1,

	AUD_ANIMAL_MOOD_NUM_MOODS = 2
}
```

---
### SetAudioFlag

`SET_AUDIO_FLAG` · hash `0xB9EFD5C25018725A` · jhash `0x1C09C9E0` · **Cliente**

```lua
SetAudioFlag(flagName, toggle)
```
```c
void SET_AUDIO_FLAG(char* flagName, BOOL toggle);
```

**Parámetros**

- `flagName` (`char*`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Generic interface to toggle audio functionality, with auto-reset on script termination and support for multiple script threads

Flags used in game scripts:
| Flag Name | Description of Usage |
| ----- | -------- |
| ActivateSwitchWheelAudio | |
| AllowAmbientSpeechInSlowMo | |
| AllowCutsceneOverScreenFade | |
| AllowForceRadioAfterRetune | |
| AllowPainAndAmbientSpeechToPlayDuringCutscene | |
| AllowPlayerAIOnMission | |
| AllowPoliceScannerWhenPlayerHasNoControl | |
| AllowRadioDuringSwitch | |
| AllowRadioOverScreenFade | |
| AllowScoreAndRadio | |
| AllowScriptedSpeechInSlowMo | |
| AvoidMissionCompleteDelay | |
| DisableAbortConversationForDeathAndInjury | |
| DisableAbortConversationForRagdoll | |
| DisableBarks | |
| DisableFlightMusic | |
| DisableNPCHeadsetSpeechAttenuation | |
| DisableReplayScriptStreamRecording | |
| EnableHeadsetBeep | |
| EnableMissileLockWarningForAllVehicles | |
| ForceConversationInterrupt | |
| ForceSeamlessRadioSwitch | |
| ForceSniperAudio | |
| FrontendRadioDisabled | |
| HoldMissionCompleteWhenPrepared | |
| IsDirectorModeActive |  Allows you to play speech infinitely without any pauses like in Director Mode. |
| IsPlayerOnMissionForSpeech | |
| ListenerReverbDisabled | |
| LoadMPData | |
| MobileRadioInGame | |
| OnlyAllowScriptTriggerPoliceScanner | |
| PlayerOnDLCHeist4Island | |
| PlayMenuMusic | |
| PoliceScannerDisabled | |
| ScriptedConvListenerMaySpeak | |
| SpeechDucksScore | |
| SuppressPlayerScubaBreathing | |
| UseQuietSceneSoftVersion | |
| WantedMusicDisabled | |
| WantedMusicOnMission | |

```
All flag IDs and hashes:
ID: 01 | Hash: 0x20A7858F
ID: 02 | Hash: 0xA11C2259
ID: 03 | Hash: 0x08DE4700
ID: 04 | Hash: 0x989F652F
ID: 05 | Hash: 0x3C9E76BA
ID: 06 | Hash: 0xA805FEB0
ID: 07 | Hash: 0x4B94EA26
ID: 08 | Hash: 0x803ACD34
ID: 09 | Hash: 0x7C741226
ID: 10 | Hash: 0x31DB9EBD
ID: 11 | Hash: 0xDF386F18
ID: 12 | Hash: 0x669CED42
ID: 13 | Hash: 0x51F22743
ID: 14 | Hash: 0x2052B35C
ID: 15 | Hash: 0x071472DC
ID: 16 | Hash: 0xF9928BCC
ID: 17 | Hash: 0x7ADBDD48
ID: 18 | Hash: 0xA959BA1A
ID: 19 | Hash: 0xBBE89B60
ID: 20 | Hash: 0x87A08871
ID: 21 | Hash: 0xED1057CE
ID: 22 | Hash: 0x1584AD7A
ID: 23 | Hash: 0x8582CFCB
ID: 24 | Hash: 0x7E5E2FB0
ID: 25 | Hash: 0xAE4F72DB
ID: 26 | Hash: 0x5D16D1FA
ID: 27 | Hash: 0x06B2F4B8
ID: 28 | Hash: 0x5D4CDC96
ID: 29 | Hash: 0x8B5A48BA
ID: 30 | Hash: 0x98FBD539
ID: 31 | Hash: 0xD8CB0473
ID: 32 | Hash: 0x5CBB4874
ID: 33 | Hash: 0x2E9F93A9
ID: 34 | Hash: 0xD93BEA86
ID: 35 | Hash: 0x92109B7D
ID: 36 | Hash: 0xB7EC9E4D
ID: 37 | Hash: 0xCABDBB1D
ID: 38 | Hash: 0xB3FD4A52
ID: 39 | Hash: 0x370D94E5
ID: 40 | Hash: 0xA0F7938F
ID: 41 | Hash: 0xCBE1CE81
ID: 42 | Hash: 0xC27F1271
ID: 43 | Hash: 0x9E3258EB
ID: 44 | Hash: 0x551CDA5B
ID: 45 | Hash: 0xCB6D663C
ID: 46 | Hash: 0x7DACE87F
ID: 47 | Hash: 0xF9DE416F
ID: 48 | Hash: 0x882E6E9E
ID: 49 | Hash: 0x16B447E7
ID: 50 | Hash: 0xBD867739
ID: 51 | Hash: 0xA3A58604
ID: 52 | Hash: 0x7E046BBC
ID: 53 | Hash: 0xD95FDB98
ID: 54 | Hash: 0x5842C0ED
ID: 55 | Hash: 0x285FECC6
ID: 56 | Hash: 0x9351AC43
ID: 57 | Hash: 0x50032E75
ID: 58 | Hash: 0xAE6D0D59
ID: 59 | Hash: 0xD6351785
ID: 60 | Hash: 0xD25D71BC
ID: 61 | Hash: 0x1F7F6423
ID: 62 | Hash: 0xE24C3AA6
ID: 63 | Hash: 0xBFFDD2B7
```

---
### SetAudioSceneVariable

`SET_AUDIO_SCENE_VARIABLE` · hash `0xEF21A9EF089A2668` · jhash `0x19BB3CE8` · **Cliente**

```lua
SetAudioSceneVariable(scene, variableName, value)
```
```c
void SET_AUDIO_SCENE_VARIABLE(char* scene, char* variableName, float value);
```

**Parámetros**

- `scene` (`char*`): name of the scene
- `variableName` (`char*`): name of the variable to add/change
- `value` (`float`): value to set the variable to

**Devuelve:** `void`

---
### SetAudioScriptCleanupTime

`SET_AUDIO_SCRIPT_CLEANUP_TIME` · hash `0xA5F377B175A699C5` · jhash `0xE812925D` · **Cliente**

```lua
SetAudioScriptCleanupTime(timeMs)
```
```c
void SET_AUDIO_SCRIPT_CLEANUP_TIME(int timeMs);
```

**Parámetros**

- `timeMs` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Set a delay in milliseconds for the audio to be cleaned up when the script finishes.

**Nombres antiguos (alias):** `0xA5F377B175A699C5` (`N_0xa5f377b175a699c5`)

---
### SetAudioSpecialEffectMode

`SET_AUDIO_SPECIAL_EFFECT_MODE` · hash `0x12561FCBB62D5B9C` · jhash `0x62B43677` · **Cliente**

```lua
SetAudioSpecialEffectMode(mode)
```
```c
void SET_AUDIO_SPECIAL_EFFECT_MODE(int mode);
```

**Parámetros**

- `mode` (`int`): Audio mode to apply this frame

**Devuelve:** `void`

**Descripción oficial:**

Needs to be called every frame.

```cpp
enum eAudSpecialEffectMode
{
	kSpecialEffectModeNormal = 0,
	kSpecialEffectModeUnderwater = 1,
	kSpecialEffectModeStoned = 2,
	kSpecialEffectModePauseMenu = 3,
	kSpecialEffectModeSlowMotion = 4,
	kSpecialEffectModeDrunkStage01 = 5,
	kSpecialEffectModeDrunkStage02 = 6,
	kSpecialEffectModeDrunkStage03 = 7,
	NUM_AUDSPECIALEFFECTMODE
};
```

**Nombres antiguos (alias):** `0x12561FCBB62D5B9C` (`N_0x12561fcbb62d5b9c`)

---
### SetAudioVehiclePriority

`SET_AUDIO_VEHICLE_PRIORITY` · hash `0xE5564483E407F914` · jhash `0x271A9766` · **Cliente**

```lua
SetAudioVehiclePriority(vehicle, priority)
```
```c
void SET_AUDIO_VEHICLE_PRIORITY(Vehicle vehicle, int priority);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `priority` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the priority for the given vehicle. This is a hint for the audio system as to what LOD the
vehicle should use.

'High' priority will bump up the activation range significantly and prevent it
from dropping when the vehicle is not within the view frustrum.

'Max' will attempt to keep the vehicle at maximum LOD regardless of how far it is from the listener or what it is currently doing. Be careful with this!

There is a hard limit of 5 simulataneous granular cars (including the player) so we are quite limited on the number
we can play at once, so setting vehicles to max priority will reduce the number of engines availble for regular NPC vehicles

```cpp
enum eAudVehiclePriority {
	AUDIO_VEHICLE_PRIORITY_NORMAL = 0,
	AUDIO_VEHICLE_PRIORITY_MEDIUM = 1,
	AUDIO_VEHICLE_PRIORITY_MAX = 2,
	AUDIO_VEHICLE_PRIORITY_HIGH = 3,
}
```

---
### SetConversationAudioControlledByAnim

`SET_CONVERSATION_AUDIO_CONTROLLED_BY_ANIM` · hash `0x0B568201DD99F0EB` · jhash `0x1193ED6E` · **Cliente**

```lua
SetConversationAudioControlledByAnim(enable)
```
```c
void SET_CONVERSATION_AUDIO_CONTROLLED_BY_ANIM(BOOL enable);
```

**Parámetros**

- `enable` (`BOOL`): Pass in true to set conversation flow to be controlled by animation triggers.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether or not scripted conversation flow should be controlled by anim triggers

**Nombres antiguos (alias):** `0x0B568201DD99F0EB` (`N_0x0b568201dd99f0eb`)

---
### SetConversationAudioPlaceholder

`SET_CONVERSATION_AUDIO_PLACEHOLDER` · hash `0x61631F5DF50D1C34` · **Cliente**

```lua
SetConversationAudioPlaceholder(isPlaceHolder)
```
```c
void SET_CONVERSATION_AUDIO_PLACEHOLDER(BOOL isPlaceHolder);
```

**Parámetros**

- `isPlaceHolder` (`BOOL`): Whether or not the conversation should use robot speech or not

**Devuelve:** `void`

**Descripción oficial:**

Used to determine whether conversation should use robot speech or not

**Nombres antiguos (alias):** `0x61631F5DF50D1C34` (`N_0x61631f5df50d1c34`)

---
### SetCustomRadioTrackList

`SET_CUSTOM_RADIO_TRACK_LIST` · hash `0x4E404A9361F75BB2` · jhash `0x128C3873` · **Cliente**

```lua
SetCustomRadioTrackList(radioStation, trackListName, forceNow)
```
```c
void SET_CUSTOM_RADIO_TRACK_LIST(char* radioStation, char* trackListName, BOOL forceNow);
```

**Parámetros**

- `radioStation` (`char*`)
- `trackListName` (`char*`)
- `forceNow` (`BOOL`): wheter or not to interrupt the current track on the tracklist

**Devuelve:** `void`

**Descripción oficial:**

Queues up a custom track list on the specified radio station. The content in the track list will be played as soon as possible.
The station does not have to be frozen.

**Nombres antiguos (alias):** `0x4E404A9361F75BB2` (`N_0x4e404a9361f75bb2`)

---
### SetCutsceneAudioOverride

`SET_CUTSCENE_AUDIO_OVERRIDE` · hash `0x3B4BF5F0859204D9` · jhash `0xCE1332B7` · **Cliente**

```lua
SetCutsceneAudioOverride(name)
```
```c
void SET_CUTSCENE_AUDIO_OVERRIDE(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
All occurrences found in b617d, sorted alphabetically and identical lines removed:
AUDIO::SET_CUTSCENE_AUDIO_OVERRIDE("_AK");
AUDIO::SET_CUTSCENE_AUDIO_OVERRIDE("_CUSTOM");
AUDIO::SET_CUTSCENE_AUDIO_OVERRIDE("_TOOTHLESS");
```

Add a suffix to the cutscene audio name. Call before loading the cutscene.

---
### SetEmitterRadioStation

`SET_EMITTER_RADIO_STATION` · hash `0xACF57305B12AF907` · jhash `0x87431585` · **Cliente**

```lua
SetEmitterRadioStation(emitterName, radioStation)
```
```c
void SET_EMITTER_RADIO_STATION(char* emitterName, char* radioStation);
```

**Parámetros**

- `emitterName` (`char*`)
- `radioStation` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Retunes a named static emitter to the specified station

---
### SetEntityForNullConvPed

`SET_ENTITY_FOR_NULL_CONV_PED` · hash `0x892B6AB8F33606F5` · jhash `0x88203DDA` · **Cliente**

```lua
SetEntityForNullConvPed(speakerConversationIndex, entity)
```
```c
void SET_ENTITY_FOR_NULL_CONV_PED(int speakerConversationIndex, Entity entity);
```

**Parámetros**

- `speakerConversationIndex` (`int`)
- `entity` (`Entity`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x892B6AB8F33606F5` (`N_0x892b6ab8f33606f5`)

---
### SetFrontendRadioActive

`SET_FRONTEND_RADIO_ACTIVE` · hash `0xF7F26C6E9CC9EBB8` · jhash `0xB1172075` · **Cliente**

```lua
SetFrontendRadioActive(active)
```
```c
void SET_FRONTEND_RADIO_ACTIVE(BOOL active);
```

**Parámetros**

- `active` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Allows the radio to be played in the frontend.

---
### SetGlobalRadioSignalLevel

`SET_GLOBAL_RADIO_SIGNAL_LEVEL` · hash `0x159B7318403A1CD8` · **Cliente**

```lua
SetGlobalRadioSignalLevel(signalLevel)
```
```c
void SET_GLOBAL_RADIO_SIGNAL_LEVEL(float signalLevel);
```

**Parámetros**

- `signalLevel` (`float`): Radio signal level.

**Devuelve:** `void`

**Descripción oficial:**

Sets the global radio signal level, lower value will cause radio static.
Used only a handful of times in scripts.

**Nombres antiguos (alias):** `0x159B7318403A1CD8` (`N_0x159b7318403a1cd8`)

---
### SetGpsActive

`SET_GPS_ACTIVE` · hash `0x3BD3F52BA9B1E4E8` · jhash `0x0FC3379A` · **Cliente**

```lua
SetGpsActive(active)
```
```c
void SET_GPS_ACTIVE(BOOL active);
```

**Parámetros**

- `active` (`BOOL`)

**Devuelve:** `void`

---
### SetHornEnabled

`SET_HORN_ENABLED` · hash `0x76D683C108594D0E` · jhash `0x6EB92D05` · **Cliente**

```lua
SetHornEnabled(vehicle, toggle)
```
```c
void SET_HORN_ENABLED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetHornPermanentlyOnTime

`SET_HORN_PERMANENTLY_ON_TIME` · hash `0x9D3AF56E94C9AE98` · jhash `0x2F0A16D1` · **Cliente**

```lua
SetHornPermanentlyOnTime(vehicle, time)
```
```c
void SET_HORN_PERMANENTLY_ON_TIME(Vehicle vehicle, float time);
```

**Parámetros**

- `vehicle` (`Vehicle`): The target vehicle.
- `time` (`float`): The duration for the horn to sound, in milliseconds.

**Devuelve:** `void`

**Descripción oficial:**

Sounds the vehicle's horn for a specified duration. The behavior of this native changes significantly depending on the occupancy of the driver's seat:

*   **Empty Driver Seat:** The horn will sound continuously for the entire duration specified in the `time` parameter.
*   **Occupied Driver Seat:** The `time` parameter is entirely ignored. The horn will only sound very briefly, simulating a quick tap of the horn button.
*   **Interruption:** If a ped enters the driver seat while the horn is actively sounding (triggered by this native), the horn will stop immediately.

**Nombres antiguos (alias):** `0x9D3AF56E94C9AE98` (`N_0x9d3af56e94c9ae98`)

---
### SetInitialPlayerStation

`SET_INITIAL_PLAYER_STATION` · hash `0x88795F13FACDA88D` · jhash `0x9B069233` · **Cliente**

```lua
SetInitialPlayerStation(radioStation)
```
```c
void SET_INITIAL_PLAYER_STATION(char* radioStation);
```

**Parámetros**

- `radioStation` (`char*`)

**Devuelve:** `void`

---
### SetMicrophonePosition

`SET_MICROPHONE_POSITION` · hash `0xB6AE90EDDE95C762` · jhash `0xAD7BB191` · **Cliente**

```lua
SetMicrophonePosition(p0, x1, y1, z1, x2, y2, z2, x3, y3, z3)
```
```c
void SET_MICROPHONE_POSITION(BOOL p0, float x1, float y1, float z1, float x2, float y2, float z2, float x3, float y3, float z3);
```

**Parámetros**

- `p0` (`BOOL`)
- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `x3` (`float`)
- `y3` (`float`)
- `z3` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
If this is the correct name, what microphone? I know your TV isn't going to reach out and adjust your headset so..  
```

---
### SetMobilePhoneRadioState

`SET_MOBILE_PHONE_RADIO_STATE` · hash `0xBF286C554784F3DF` · jhash `0xE1E0ED34` · **Cliente**

```lua
SetMobilePhoneRadioState(state)
```
```c
void SET_MOBILE_PHONE_RADIO_STATE(BOOL state);
```

**Parámetros**

- `state` (`BOOL`)

**Devuelve:** `void`

---
### SetMobileRadioEnabledDuringGameplay

`SET_MOBILE_RADIO_ENABLED_DURING_GAMEPLAY` · hash `0x1098355A16064BB3` · jhash `0x990085F0` · **Cliente**

```lua
SetMobileRadioEnabledDuringGameplay(toggle)
```
```c
void SET_MOBILE_RADIO_ENABLED_DURING_GAMEPLAY(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPedAudioFootstepLoud

`_SET_PED_AUDIO_FOOTSTEP_LOUD` · hash `0x0653B735BFBDFE87` · **Cliente**

```lua
SetPedAudioFootstepLoud(ped, toggle)
```
```c
void _SET_PED_AUDIO_FOOTSTEP_LOUD(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Enables/disables ped's "loud" footstep sound.
```

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x0653B735BFBDFE87` (`N_0x0653b735bfbdfe87`)

---
### SetPedAudioGender

`_SET_PED_AUDIO_GENDER` · hash `0xA5342D390CDA41D6` · **Cliente**

```lua
SetPedAudioGender(ped, p1)
```
```c
void _SET_PED_AUDIO_GENDER(Ped ped, BOOL p1);
```

**Parámetros**

- `ped` (`Ped`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA5342D390CDA41D6` (`N_0xa5342d390cda41d6`)

---
### SetPedClothEventsEnabled

`SET_PED_CLOTH_EVENTS_ENABLED` · hash `0x29DA3CA8D8B2692D` · **Cliente**

```lua
SetPedClothEventsEnabled(ped, enabled)
```
```c
void SET_PED_CLOTH_EVENTS_ENABLED(Ped ped, BOOL enabled);
```

**Parámetros**

- `ped` (`Ped`)
- `enabled` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

**Nombres antiguos (alias):** `0x29DA3CA8D8B2692D` (`N_0x29da3ca8d8b2692d`), `_SET_PED_AUDIO_FOOTSTEP_QUIET` (`SetPedAudioFootstepQuiet`)

---
### SetPedIsDrunk

`SET_PED_IS_DRUNK` · hash `0x95D2D383D5396B8A` · jhash `0xD2EA77A3` · **Cliente**

```lua
SetPedIsDrunk(ped, toggle)
```
```c
void SET_PED_IS_DRUNK(Ped ped, BOOL toggle);
```

**Parámetros**

- `ped` (`Ped`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets the ped so they sound drunk

---
### SetPedRaceAndVoiceGroup

`SET_PED_RACE_AND_VOICE_GROUP` · hash `0x1B7ABE26CBCBF8C7` · **Cliente**

```lua
SetPedRaceAndVoiceGroup(ped, pedRace, pvgHash)
```
```c
void SET_PED_RACE_AND_VOICE_GROUP(Ped ped, int pedRace, int pvgHash);
```

**Parámetros**

- `ped` (`Ped`)
- `pedRace` (`int`)
- `pvgHash` (`int`): PedVoiceGroup hash, defaults to 0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1B7ABE26CBCBF8C7` (`N_0x1b7abe26cbcbf8c7`)

---
### SetPedVoiceFull

`SET_PED_VOICE_FULL` · hash `0x40CF0D12D142A9E8` · **Cliente**

```lua
SetPedVoiceFull(ped)
```
```c
void SET_PED_VOICE_FULL(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

Calls the same internal function [`_SET_PED_VOICE_GROUP`](#setpedvoicegroup) calls, but passes `voiceGroupHash` (defined as a parameter in the referenced native) as `0`.

**Nombres antiguos (alias):** `0x40CF0D12D142A9E8` (`N_0x40cf0d12d142a9e8`), `_SET_PED_SCREAM` (`SetPedScream`)

---
### SetPedVoiceGroup

`_SET_PED_VOICE_GROUP` · hash `0x7CDC8C3B89F661B3` · **Cliente**

```lua
SetPedVoiceGroup(ped, voiceGroupHash)
```
```c
void _SET_PED_VOICE_GROUP(Ped ped, Hash voiceGroupHash);
```

**Parámetros**

- `ped` (`Ped`)
- `voiceGroupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
From the scripts:
AUDIO::_SET_PED_VOICE_GROUP(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("PAIGE_PVG"));
AUDIO::_SET_PED_VOICE_GROUP(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("TALINA_PVG"));
AUDIO::_SET_PED_VOICE_GROUP(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("FEMALE_LOST_BLACK_PVG"));
AUDIO::_SET_PED_VOICE_GROUP(PLAYER::PLAYER_PED_ID(), MISC::GET_HASH_KEY("FEMALE_LOST_WHITE_PVG"));
```

**Nombres antiguos (alias):** `0x7CDC8C3B89F661B3` (`N_0x7cdc8c3b89f661b3`)

---
### SetPedVoiceGroupRace

`_SET_PED_VOICE_GROUP_RACE` · hash `0x0BABC1345ABBFB16` · **Cliente**

```lua
SetPedVoiceGroupRace(ped, voiceGroupHash)
```
```c
void _SET_PED_VOICE_GROUP_RACE(Ped ped, Hash voiceGroupHash);
```

**Parámetros**

- `ped` (`Ped`)
- `voiceGroupHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Dat151RelType == 29
```

```
NativeDB Introduced: v2699
```

---
### SetPedWallaDensity

`SET_PED_WALLA_DENSITY` · hash `0x149AEE66F0CB3A99` · jhash `0xE64F97A0` · **Cliente**

```lua
SetPedWallaDensity(density, applyValue)
```
```c
void SET_PED_WALLA_DENSITY(float density, float applyValue);
```

**Parámetros**

- `density` (`float`): desired walla density
- `applyValue` (`float`): how much the desired density affects the actual one

**Devuelve:** `void`

**Descripción oficial:**

Overrides the calculated ped density that is used to modulate the ambient ped walla sounds (in exteriors only)

If you want to use this for interiors, use [SET_PED_INTERIOR_WALLA_DENSITY](#n_0x8bf907833be275de)

**Nombres antiguos (alias):** `0x149AEE66F0CB3A99` (`N_0x149aee66f0cb3a99`)

---
### SetPlayerAngry

`SET_PLAYER_ANGRY` · hash `0xEA241BB04110F091` · jhash `0x782CA58D` · **Cliente**

```lua
SetPlayerAngry(ped, isAngry)
```
```c
void SET_PLAYER_ANGRY(Ped ped, BOOL isAngry);
```

**Parámetros**

- `ped` (`Ped`)
- `isAngry` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Sets a player ped to use his ANGRY speech contexts

---
### SetPlayerVehicleAlarmAudioActive

`SET_PLAYER_VEHICLE_ALARM_AUDIO_ACTIVE` · hash `0x6FDDAD856E36988A` · jhash `0x934BE749` · **Cliente**

```lua
SetPlayerVehicleAlarmAudioActive(vehicle, active)
```
```c
void SET_PLAYER_VEHICLE_ALARM_AUDIO_ACTIVE(Vehicle vehicle, BOOL active);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `active` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Enable player vehicle specific alarm disarm/arm sound triggering

**Nombres antiguos (alias):** `0x6FDDAD856E36988A` (`N_0x6fddad856e36988a`)

---
### SetPortalSettingsOverride

`SET_PORTAL_SETTINGS_OVERRIDE` · hash `0x044DBAD7A7FA2BE5` · jhash `0x8AD670EC` · **Cliente**

```lua
SetPortalSettingsOverride(oldPortalSettingsName, newPortalSettingsName)
```
```c
void SET_PORTAL_SETTINGS_OVERRIDE(char* oldPortalSettingsName, char* newPortalSettingsName);
```

**Parámetros**

- `oldPortalSettingsName` (`char*`)
- `newPortalSettingsName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x044DBAD7A7FA2BE5` (`N_0x044dbad7a7fa2be5`)

---
### SetPositionForNullConvPed

`SET_POSITION_FOR_NULL_CONV_PED` · hash `0x33E3C6C6F2F0B506` · jhash `0x73C6F979` · **Cliente**

```lua
SetPositionForNullConvPed(speakerConversationIndex, x, y, z)
```
```c
void SET_POSITION_FOR_NULL_CONV_PED(int speakerConversationIndex, float x, float y, float z);
```

**Parámetros**

- `speakerConversationIndex` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x33E3C6C6F2F0B506` (`N_0x33e3c6c6f2f0b506`)

---
### SetPositionedPlayerVehicleRadioEmitterEnabled

`SET_POSITIONED_PLAYER_VEHICLE_RADIO_EMITTER_ENABLED` · hash `0xDA07819E452FFE8F` · **Cliente**

```lua
SetPositionedPlayerVehicleRadioEmitterEnabled(enabled)
```
```c
void SET_POSITIONED_PLAYER_VEHICLE_RADIO_EMITTER_ENABLED(BOOL enabled);
```

**Parámetros**

- `enabled` (`BOOL`): enables/disables a positioned emitter for the player vehicle radio

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDA07819E452FFE8F` (`N_0xda07819e452ffe8f`)

---
### SetRadioAutoUnfreeze

`SET_RADIO_AUTO_UNFREEZE` · hash `0xC1AA9F53CE982990` · jhash `0xA40196BF` · **Cliente**

```lua
SetRadioAutoUnfreeze(toggle)
```
```c
void SET_RADIO_AUTO_UNFREEZE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): if true the radio will automatically unfreeze as soon as the player gets in a vehicle

**Devuelve:** `void`

---
### SetRadioFrontendFadeTime

`SET_RADIO_FRONTEND_FADE_TIME` · hash `0x2C96CDB04FCA358E` · jhash `0xC8B514E2` · **Cliente**

```lua
SetRadioFrontendFadeTime(fadeTime)
```
```c
void SET_RADIO_FRONTEND_FADE_TIME(float fadeTime);
```

**Parámetros**

- `fadeTime` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x2C96CDB04FCA358E` (`N_0x2c96cdb04fca358e`)

---
### SetRadioRetuneDown

`SET_RADIO_RETUNE_DOWN` · hash `0xDD6BCF9E94425DF9` · jhash `0xD70ECC80` · **Cliente**

```lua
SetRadioRetuneDown()
```
```c
void SET_RADIO_RETUNE_DOWN();
```

**Devuelve:** `void`

**Descripción oficial:**

Sets radio to tune down. (Changes radio station)

**Nombres antiguos (alias):** `0xDD6BCF9E94425DF9` (`N_0xdd6bcf9e94425df9`)

---
### SetRadioRetuneUp

`SET_RADIO_RETUNE_UP` · hash `0xFF266D1D0EB1195D` · jhash `0x53DB6994` · **Cliente**

```lua
SetRadioRetuneUp()
```
```c
void SET_RADIO_RETUNE_UP();
```

**Devuelve:** `void`

**Descripción oficial:**

Sets the radio to tune up. (changes radio station)

**Nombres antiguos (alias):** `0xFF266D1D0EB1195D` (`N_0xff266d1d0eb1195d`)

---
### SetRadioStationIsVisible

`_SET_RADIO_STATION_IS_VISIBLE` · hash `0x4CAFEBFA21EC188D` · **Cliente**

```lua
SetRadioStationIsVisible(radioStation, toggle)
```
```c
void _SET_RADIO_STATION_IS_VISIBLE(char* radioStation, BOOL toggle);
```

**Parámetros**

- `radioStation` (`char*`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Doesn't have an effect in Story Mode.

```
NativeDB Introduced: v2372
```

---
### SetRadioStationMusicOnly

`SET_RADIO_STATION_MUSIC_ONLY` · hash `0x774BD811F656A122` · jhash `0xB1FF7137` · **Cliente**

```lua
SetRadioStationMusicOnly(radioStation, toggle)
```
```c
void SET_RADIO_STATION_MUSIC_ONLY(char* radioStation, BOOL toggle);
```

**Parámetros**

- `radioStation` (`char*`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
6 calls in the b617d scripts, removed identical lines:
AUDIO::SET_RADIO_STATION_MUSIC_ONLY("RADIO_01_CLASS_ROCK", 1);
AUDIO::SET_RADIO_STATION_MUSIC_ONLY(AUDIO::GET_RADIO_STATION_NAME(10), 0);
AUDIO::SET_RADIO_STATION_MUSIC_ONLY(AUDIO::GET_RADIO_STATION_NAME(10), 1);
```

**Nombres antiguos (alias):** `0x774BD811F656A122` (`N_0x774bd811f656a122`)

---
### SetRadioToStationIndex

`SET_RADIO_TO_STATION_INDEX` · hash `0xA619B168B8A8570F` · jhash `0x1D82766D` · **Cliente**

```lua
SetRadioToStationIndex(radioStation)
```
```c
void SET_RADIO_TO_STATION_INDEX(int radioStation);
```

**Parámetros**

- `radioStation` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Sets radio station by index.  
```

---
### SetRadioToStationName

`SET_RADIO_TO_STATION_NAME` · hash `0xC69EDA28699D5107` · jhash `0x7B36E35E` · **Cliente**

```lua
SetRadioToStationName(stationName)
```
```c
void SET_RADIO_TO_STATION_NAME(char* stationName);
```

**Parámetros**

- `stationName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Find the radio station list [here](https://gist.github.com/4mmonium/b47d6512a2d992cbf4eea15d9038b581)

---
### SetRadioTrack

`SET_RADIO_TRACK` · hash `0xB39786F201FEE30B` · jhash `0x76E96212` · **Cliente**

```lua
SetRadioTrack(radioStation, radioTrack)
```
```c
void SET_RADIO_TRACK(char* radioStation, char* radioTrack);
```

**Parámetros**

- `radioStation` (`char*`)
- `radioTrack` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only found this one in the decompiled scripts:  
AUDIO::SET_RADIO_TRACK("RADIO_03_HIPHOP_NEW", "ARM1_RADIO_STARTS");  
```

---
### SetRadioTrackMix

`_SET_RADIO_TRACK_MIX` · hash `0x2CB0075110BE1E56` · **Cliente**

```lua
SetRadioTrackMix(radioStationName, mixName, p2)
```
```c
void _SET_RADIO_TRACK_MIX(char* radioStationName, char* mixName, int p2);
```

**Parámetros**

- `radioStationName` (`char*`)
- `mixName` (`char*`)
- `p2` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

---
### SetScriptUpdateDoorAudio

`SET_SCRIPT_UPDATE_DOOR_AUDIO` · hash `0x06C0023BED16DD6B` · jhash `0xE61110A2` · **Cliente**

```lua
SetScriptUpdateDoorAudio(doorHash, toggle)
```
```c
void SET_SCRIPT_UPDATE_DOOR_AUDIO(Hash doorHash, BOOL toggle);
```

**Parámetros**

- `doorHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x06C0023BED16DD6B` (`N_0x06c0023bed16dd6b`)

---
### SetSirenKeepOn

`_SET_SIREN_KEEP_ON` · hash `0xF584CF8529B51434` · **Cliente**

```lua
SetSirenKeepOn(vehicle, toggle)
```
```c
void _SET_SIREN_KEEP_ON(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0xF584CF8529B51434` (`N_0xf584cf8529b51434`)

---
### SetSirenWithNoDriver

`SET_SIREN_WITH_NO_DRIVER` · hash `0x1FEF0683B96EBCF2` · jhash `0x77182D58` · **Cliente**

```lua
SetSirenWithNoDriver(vehicle, toggle)
```
```c
void SET_SIREN_WITH_NO_DRIVER(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetStaticEmitterEnabled

`SET_STATIC_EMITTER_ENABLED` · hash `0x399D2D3B33F1B8EB` · jhash `0x91F72E92` · **Cliente**

```lua
SetStaticEmitterEnabled(emitterName, toggle)
```
```c
void SET_STATIC_EMITTER_ENABLED(char* emitterName, BOOL toggle);
```

**Parámetros**

- `emitterName` (`char*`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Example:
AUDIO::SET_STATIC_EMITTER_ENABLED((Any*)"LOS_SANTOS_VANILLA_UNICORN_01_STAGE", false);    AUDIO::SET_STATIC_EMITTER_ENABLED((Any*)"LOS_SANTOS_VANILLA_UNICORN_02_MAIN_ROOM", false);    AUDIO::SET_STATIC_EMITTER_ENABLED((Any*)"LOS_SANTOS_VANILLA_UNICORN_03_BACK_ROOM", false);
This turns off surrounding sounds not connected directly to peds.
```

---
### SetUserRadioControlEnabled

`SET_USER_RADIO_CONTROL_ENABLED` · hash `0x19F21E63AE6EAE4E` · jhash `0x52E054CE` · **Cliente**

```lua
SetUserRadioControlEnabled(toggle)
```
```c
void SET_USER_RADIO_CONTROL_ENABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVariableOnCutsceneAudio

`_SET_VARIABLE_ON_CUTSCENE_AUDIO` · hash `0xBCC29F935ED07688` · jhash `0xD63CF33A` · **Cliente**

```lua
SetVariableOnCutsceneAudio(variableName, value)
```
```c
void _SET_VARIABLE_ON_CUTSCENE_AUDIO(char* variableName, float value);
```

**Parámetros**

- `variableName` (`char*`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VARIABLE_ON_*
```

**Nombres antiguos (alias):** `GET_PLAYER_HEADSET_SOUND_ALTERNATE` (`GetPlayerHeadsetSoundAlternate`)

---
### SetVariableOnSound

`SET_VARIABLE_ON_SOUND` · hash `0xAD6B3148A78AE9B6` · jhash `0x606EE5FA` · **Cliente**

```lua
SetVariableOnSound(soundId, variableName, value)
```
```c
void SET_VARIABLE_ON_SOUND(int soundId, char* variableName, float value);
```

**Parámetros**

- `soundId` (`int`)
- `variableName` (`char*`)
- `value` (`float`)

**Devuelve:** `void`

---
### SetVariableOnStream

`SET_VARIABLE_ON_STREAM` · hash `0x2F9D3834AEB9EF79` · jhash `0xF67BB44C` · **Cliente**

```lua
SetVariableOnStream(p0, p1)
```
```c
void SET_VARIABLE_ON_STREAM(char* p0, float p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
From the scripts, p0:  
"ArmWrestlingIntensity",  
"INOUT",  
"Monkey_Stream",  
"ZoomLevel"  
```

---
### SetVariableOnUnderWaterStream

`SET_VARIABLE_ON_UNDER_WATER_STREAM` · hash `0x733ADF241531E5C2` · jhash `0x62D026BE` · **Cliente**

```lua
SetVariableOnUnderWaterStream(variableName, value)
```
```c
void SET_VARIABLE_ON_UNDER_WATER_STREAM(char* variableName, float value);
```

**Parámetros**

- `variableName` (`char*`)
- `value` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
AUDIO::SET_VARIABLE_ON_UNDER_WATER_STREAM("inTunnel", 1.0);
AUDIO::SET_VARIABLE_ON_UNDER_WATER_STREAM("inTunnel", 0.0);
```

**Nombres antiguos (alias):** `0x733ADF241531E5C2` (`N_0x733adf241531e5c2`)

---
### SetVehHasRadioOverride

`_SET_VEH_HAS_RADIO_OVERRIDE` · hash `0x3E45765F3FBB582F` · **Cliente**

```lua
SetVehHasRadioOverride(vehicle)
```
```c
void _SET_VEH_HAS_RADIO_OVERRIDE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2372
```

**Nombres antiguos (alias):** `0x3E45765F3FBB582F` (`N_0x3e45765f3fbb582f`)

---
### SetVehRadioStation

`SET_VEH_RADIO_STATION` · hash `0x1B9C0099CB942AC6` · jhash `0xE391F55F` · **Cliente**

```lua
SetVehRadioStation(vehicle, radioStation)
```
```c
void SET_VEH_RADIO_STATION(Vehicle vehicle, char* radioStation);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `radioStation` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Find the radio station list [here](https://gist.github.com/4mmonium/b47d6512a2d992cbf4eea15d9038b581)

---
### SetVehicleAudioBodyDamageFactor

`SET_VEHICLE_AUDIO_BODY_DAMAGE_FACTOR` · hash `0x01BB4D577D38BD9E` · jhash `0xE81FAC68` · **Cliente**

```lua
SetVehicleAudioBodyDamageFactor(vehicle, intensity)
```
```c
void SET_VEHICLE_AUDIO_BODY_DAMAGE_FACTOR(Vehicle vehicle, float intensity);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle to modify
- `intensity` (`float`): A value 0.0 - 1.0. Higher the value, the more likely the vehicle is to make the sound while decelerating

**Devuelve:** `void`

**Descripción oficial:**

Vehicle will make a 'rattling' noise when decelerating

**Nombres antiguos (alias):** `0x01BB4D577D38BD9E` (`N_0x01bb4d577d38bd9e`)

---
### SetVehicleAudioEngineDamageFactor

`SET_VEHICLE_AUDIO_ENGINE_DAMAGE_FACTOR` · hash `0x59E7B488451F4D3A` · jhash `0x23BE6432` · **Cliente**

```lua
SetVehicleAudioEngineDamageFactor(vehicle, damageFactor)
```
```c
void SET_VEHICLE_AUDIO_ENGINE_DAMAGE_FACTOR(Vehicle vehicle, float damageFactor);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `damageFactor` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x59E7B488451F4D3A` (`N_0x59e7b488451f4d3a`)

---
### SetVehicleBoostActive

`SET_VEHICLE_BOOST_ACTIVE` · hash `0x4A04DE7CAB2739A1` · jhash `0x072F15F2` · **Cliente**

```lua
SetVehicleBoostActive(vehicle, toggle)
```
```c
void SET_VEHICLE_BOOST_ACTIVE(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VEHICLE_BOOST_ACTIVE(vehicle, 1, 0);  
SET_VEHICLE_BOOST_ACTIVE(vehicle, 0, 0);   
Will give a boost-soundeffect.  
```

---
### SetVehicleHornVariation

`_SET_VEHICLE_HORN_VARIATION` · hash `0x0350E7E17BA767D0` · **Cliente**

```lua
SetVehicleHornVariation(vehicle, value)
```
```c
void _SET_VEHICLE_HORN_VARIATION(Vehicle vehicle, int value);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `value` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1365
```

**Nombres antiguos (alias):** `0x0350E7E17BA767D0` (`N_0x0350e7e17ba767d0`), `0xCDA42C4BB9BDE779` (`N_0xcda42c4bb9bde779`)

---
### SetVehicleMissileWarningEnabled

`SET_VEHICLE_MISSILE_WARNING_ENABLED` · hash `0xF3365489E0DD50F9` · jhash `0x8AFC488D` · **Cliente**

```lua
SetVehicleMissileWarningEnabled(vehicle, toggle)
```
```c
void SET_VEHICLE_MISSILE_WARNING_ENABLED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle to toggle warning system for.
- `toggle` (`BOOL`): `true` to enable, `false` to disable.

**Devuelve:** `void`

**Descripción oficial:**

Toggles the incoming missile warning system for specified vehicle.

**Nombres antiguos (alias):** `0xF3365489E0DD50F9` (`N_0xf3365489e0dd50f9`)

---
### SetVehicleRadioEnabled

`SET_VEHICLE_RADIO_ENABLED` · hash `0x3B988190C0AA6C0B` · jhash `0x6F812CAB` · **Cliente**

```lua
SetVehicleRadioEnabled(vehicle, toggle)
```
```c
void SET_VEHICLE_RADIO_ENABLED(Vehicle vehicle, BOOL toggle);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
can't seem to enable radio on cop cars etc  
```

---
### SetVehicleRadioLoud

`SET_VEHICLE_RADIO_LOUD` · hash `0xBB6F1CAEC68B0BCE` · jhash `0x8D9EDD99` · **Cliente**

```lua
SetVehicleRadioLoud(vehicle, loud)
```
```c
void SET_VEHICLE_RADIO_LOUD(Vehicle vehicle, BOOL loud);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `loud` (`BOOL`)

**Devuelve:** `void`

---
### SetVehicleStartupRevSound

`SET_VEHICLE_STARTUP_REV_SOUND` · hash `0xF1F8157B8C3F171C` · jhash `0x1C0C5E4C` · **Cliente**

```lua
SetVehicleStartupRevSound(vehicle, soundName, setName)
```
```c
void SET_VEHICLE_STARTUP_REV_SOUND(Vehicle vehicle, char* soundName, char* setName);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `soundName` (`char*`)
- `setName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Overrides the vehicle's startup engine rev sound.

You can reset this with [RESET_VEHICLE_STARTUP_REV_SOUND](#resetvehiclestartuprevsound)

**Nombres antiguos (alias):** `0xF1F8157B8C3F171C` (`N_0xf1f8157b8c3f171c`)

---
### SkipRadioForward

`SKIP_RADIO_FORWARD` · hash `0x6DDBBDD98E2E9C25` · jhash `0x10D36630` · **Cliente**

```lua
SkipRadioForward()
```
```c
void SKIP_RADIO_FORWARD();
```

**Devuelve:** `void`

---
### SkipToNextScriptedConversationLine

`SKIP_TO_NEXT_SCRIPTED_CONVERSATION_LINE` · hash `0x9663FE6B7A61EB00` · jhash `0x85C98304` · **Cliente**

```lua
SkipToNextScriptedConversationLine()
```
```c
void SKIP_TO_NEXT_SCRIPTED_CONVERSATION_LINE();
```

**Devuelve:** `void`

---
### SoundVehicleHornThisFrame

`_SOUND_VEHICLE_HORN_THIS_FRAME` · hash `0x9C11908013EA4715` · jhash `0xDE8BA3CD` · **Cliente**

```lua
SoundVehicleHornThisFrame(vehicle)
```
```c
void _SOUND_VEHICLE_HORN_THIS_FRAME(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_*
```

**Nombres antiguos (alias):** `0x9C11908013EA4715` (`N_0x9c11908013ea4715`)

---
### StartAlarm

`START_ALARM` · hash `0x0355EF116C4C97B2` · jhash `0x703F524B` · **Cliente**

```lua
StartAlarm(alarmName, skipStartup)
```
```c
void START_ALARM(char* alarmName, BOOL skipStartup);
```

**Parámetros**

- `alarmName` (`char*`)
- `skipStartup` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

You should call [PREPARE_ALARM](#preparealarm) and wait for its value to be true before using this

---
### StartAudioScene

`START_AUDIO_SCENE` · hash `0x013A80FC08F6E4F2` · jhash `0xE48D757B` · **Cliente**

```lua
local retval = StartAudioScene(scene)
```
```c
BOOL START_AUDIO_SCENE(char* scene);
```

**Parámetros**

- `scene` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Used to prepare a scene where the surrounding sound is muted or a bit changed. This does not play any sound.  
List of all usable scene names found in b617d. Sorted alphabetically and identical names removed: pastebin.com/MtM9N9CC  
```

---
### StartPreloadedConversation

`START_PRELOADED_CONVERSATION` · hash `0x23641AFE870AF385` · jhash `0xA170261B` · **Cliente**

```lua
StartPreloadedConversation()
```
```c
void START_PRELOADED_CONVERSATION();
```

**Devuelve:** `void`

**Descripción oficial:**

For use with [PRELOAD_SCRIPT_CONVERSATION](#preloadscriptconversation) and [GET_IS_PRELOADED_CONVERSATION_READY](#getispreloadedconversationready)

---
### StartScriptConversation

`START_SCRIPT_CONVERSATION` · hash `0x6B17C62C9635D2DC` · jhash `0xE5DE7D9D` · **Cliente**

```lua
StartScriptConversation(displaySubtitles, addToBriefScreen, cloneConversation, interruptible)
```
```c
void START_SCRIPT_CONVERSATION(BOOL displaySubtitles, BOOL addToBriefScreen, BOOL cloneConversation, BOOL interruptible);
```

**Parámetros**

- `displaySubtitles` (`BOOL`)
- `addToBriefScreen` (`BOOL`): Defaults to true
- `cloneConversation` (`BOOL`): Defaults to false
- `interruptible` (`BOOL`): Defaults to true

**Devuelve:** `void`

---
### StartScriptPhoneConversation

`START_SCRIPT_PHONE_CONVERSATION` · hash `0x252E5F915EABB675` · jhash `0x38E42D07` · **Cliente**

```lua
StartScriptPhoneConversation(displaySubtitles, addToBriefScreen)
```
```c
void START_SCRIPT_PHONE_CONVERSATION(BOOL displaySubtitles, BOOL addToBriefScreen);
```

**Parámetros**

- `displaySubtitles` (`BOOL`)
- `addToBriefScreen` (`BOOL`): Defaults to true

**Devuelve:** `void`

---
### StopAlarm

`STOP_ALARM` · hash `0xA1CADDCD98415A41` · jhash `0xF987BE8C` · **Cliente**

```lua
StopAlarm(alarmName, instantStop)
```
```c
void STOP_ALARM(char* alarmName, BOOL instantStop);
```

**Parámetros**

- `alarmName` (`char*`)
- `instantStop` (`BOOL`): Whether to kill the alarm instantly, or to let the audio system turn it off when it becomes inaudible

**Devuelve:** `void`

---
### StopAllAlarms

`STOP_ALL_ALARMS` · hash `0x2F794A877ADD4C92` · jhash `0xC3CB9DC6` · **Cliente**

```lua
StopAllAlarms(instantStop)
```
```c
void STOP_ALL_ALARMS(BOOL instantStop);
```

**Parámetros**

- `instantStop` (`BOOL`): Whether to kill the alarm instantly, or to let the audio system turn it off when it becomes inaudible

**Devuelve:** `void`

---
### StopAudioScene

`STOP_AUDIO_SCENE` · hash `0xDFE8422B3B94E688` · jhash `0xA08D8C58` · **Cliente**

```lua
StopAudioScene(sceneName)
```
```c
void STOP_AUDIO_SCENE(char* sceneName);
```

**Parámetros**

- `sceneName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Stops the named mixing scene (which was previously started by this script)

---
### StopAudioScenes

`STOP_AUDIO_SCENES` · hash `0xBAC7FC81A75EC1A1` · jhash `0xF6C7342A` · **Cliente**

```lua
StopAudioScenes()
```
```c
void STOP_AUDIO_SCENES();
```

**Devuelve:** `void`

**Descripción oficial:**

Stops all mixed scenes which were previously started by this script

---
### StopCurrentPlayingAmbientSpeech

`STOP_CURRENT_PLAYING_AMBIENT_SPEECH` · hash `0xB8BEC0CA6F0EDB0F` · jhash `0xBB8E64BF` · **Cliente**

```lua
StopCurrentPlayingAmbientSpeech(ped)
```
```c
void STOP_CURRENT_PLAYING_AMBIENT_SPEECH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

Stops currently playing ambient speech.

---
### StopCurrentPlayingSpeech

`STOP_CURRENT_PLAYING_SPEECH` · hash `0x7A73D05A607734C7` · jhash `0x5B7463F4` · **Cliente**

```lua
StopCurrentPlayingSpeech(ped)
```
```c
void STOP_CURRENT_PLAYING_SPEECH(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

Stops currently playing speech (Pain, ambient, scripted, breathing).

**Nombres antiguos (alias):** `0x7A73D05A607734C7` (`N_0x7a73d05a607734c7`), `_SET_PED_MUTE` (`SetPedMute`)

---
### StopCutsceneAudio

`STOP_CUTSCENE_AUDIO` · hash `0x806058BBDC136E06` · jhash `0x55461BE6` · **Cliente**

```lua
StopCutsceneAudio()
```
```c
void STOP_CUTSCENE_AUDIO();
```

**Devuelve:** `void`

**Descripción oficial:**

Stops audio for the current cutscene.

**Nombres antiguos (alias):** `0x806058BBDC136E06` (`N_0x806058bbdc136e06`)

---
### StopPedRingtone

`STOP_PED_RINGTONE` · hash `0x6C5AE23EFA885092` · jhash `0xFEEA107C` · **Cliente**

```lua
StopPedRingtone(ped)
```
```c
void STOP_PED_RINGTONE(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

Stops a ped's ringtone from playing

---
### StopPedSpeaking

`STOP_PED_SPEAKING` · hash `0x9D64D7405520E3D3` · jhash `0xFF92B49D` · **Cliente**

```lua
StopPedSpeaking(ped, shouldDisable)
```
```c
void STOP_PED_SPEAKING(Ped ped, BOOL shouldDisable);
```

**Parámetros**

- `ped` (`Ped`)
- `shouldDisable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

This doesn't stop a piece of dialogue that has been triggered.

This stops the ability to force ambient dialogue if set to true - however setting it to false, then triggering a context, then setting it to true again will allow this.

Nb. This does not sync over the network, it will only affect peds locally. Use [STOP_PED_SPEAKING_SYNCED](#stoppedspeakingsynced) if you need to affect peds on other machines too.

---
### StopPedSpeakingSynced

`STOP_PED_SPEAKING_SYNCED` · hash `0xAB6781A5F3101470` · **Cliente**

```lua
StopPedSpeakingSynced(ped, shouldDisable)
```
```c
void STOP_PED_SPEAKING_SYNCED(Ped ped, BOOL shouldDisable);
```

**Parámetros**

- `ped` (`Ped`)
- `shouldDisable` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

This doesn't stop a piece of dialogue that has been triggered.

This stops the ability to force ambient dialogue if set to true - however setting it to false, then triggering a context, then setting it to true again will allow this.

The ped will also be prevented from speaking on remote machines. Use [STOP_PED_SPEAKING](#stoppedspeaking) if you just want to affect the local machine.

**Nombres antiguos (alias):** `0xAB6781A5F3101470` (`N_0xab6781a5f3101470`)

---
### StopScriptedConversation

`STOP_SCRIPTED_CONVERSATION` · hash `0xD79DEEFB53455EBA` · jhash `0xAB77DA7D` · **Cliente**

```lua
local retval = StopScriptedConversation(finishCurrentLine)
```
```c
int STOP_SCRIPTED_CONVERSATION(BOOL finishCurrentLine);
```

**Parámetros**

- `finishCurrentLine` (`BOOL`)

**Devuelve:** `int`

---
### StopSmokeGrenadeExplosionSounds

`STOP_SMOKE_GRENADE_EXPLOSION_SOUNDS` · hash `0xE4E6DD5566D28C82` · jhash `0x7262B5BA` · **Cliente**

```lua
StopSmokeGrenadeExplosionSounds()
```
```c
void STOP_SMOKE_GRENADE_EXPLOSION_SOUNDS();
```

**Devuelve:** `void`

**Descripción oficial:**

Stops all smoke grenade sounds

**Nombres antiguos (alias):** `0xE4E6DD5566D28C82` (`N_0xe4e6dd5566d28c82`)

---
### StopSound

`STOP_SOUND` · hash `0xA3B0C41BA5CC0BB5` · jhash `0xCD7F4030` · **Cliente**

```lua
StopSound(soundId)
```
```c
void STOP_SOUND(int soundId);
```

**Parámetros**

- `soundId` (`int`): The sound id to stop

**Devuelve:** `void`

**Descripción oficial:**

Stops the sound from currently playing, there isn't a way to resume a sound
after stopping it.

---
### StopStream

`STOP_STREAM` · hash `0xA4718A1419D18151` · jhash `0xD1E364DE` · **Cliente**

```lua
StopStream()
```
```c
void STOP_STREAM();
```

**Devuelve:** `void`

---
### StopSynchronizedAudioEvent

`STOP_SYNCHRONIZED_AUDIO_EVENT` · hash `0x92D6A88E64A94430` · jhash `0xADEED2B4` · **Cliente**

```lua
local retval = StopSynchronizedAudioEvent(p0)
```
```c
BOOL STOP_SYNCHRONIZED_AUDIO_EVENT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### TriggerMusicEvent

`TRIGGER_MUSIC_EVENT` · hash `0x706D57B0F50DA710` · jhash `0xB6094948` · **Cliente**

```lua
local retval = TriggerMusicEvent(eventName)
```
```c
BOOL TRIGGER_MUSIC_EVENT(char* eventName);
```

**Parámetros**

- `eventName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
List of all usable event names found in b617d used with this native. Sorted alphabetically and identical names removed: pastebin.com/RzDFmB1W  
All music event names found in the b617d scripts: pastebin.com/GnYt0R3P  
```

---
### TriggerSiren

`_TRIGGER_SIREN` · hash `0x66C3FB05206041BA` · **Cliente**

```lua
TriggerSiren(vehicle)
```
```c
void _TRIGGER_SIREN(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `void`

**Descripción oficial:**

... When not in a vehicle

```
NativeDB Introduced: v1290
```

**Nombres antiguos (alias):** `0x66C3FB05206041BA` (`N_0x66c3fb05206041ba`)

---
### UnblockSpeechContextGroup

`UNBLOCK_SPEECH_CONTEXT_GROUP` · hash `0x2ACABED337622DF2` · **Cliente**

```lua
UnblockSpeechContextGroup(groupName)
```
```c
void UNBLOCK_SPEECH_CONTEXT_GROUP(char* groupName);
```

**Parámetros**

- `groupName` (`char*`): Context group name to unblock.

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1493
```

Removes all instances of a given context block.

**Nombres antiguos (alias):** `0x2ACABED337622DF2` (`N_0x2acabed337622df2`)

---
### UnfreezeRadioStation

`UNFREEZE_RADIO_STATION` · hash `0xFC00454CF60B91DD` · jhash `0x4D46202C` · **Cliente**

```lua
UnfreezeRadioStation(radioStation)
```
```c
void UNFREEZE_RADIO_STATION(char* radioStation);
```

**Parámetros**

- `radioStation` (`char*`)

**Devuelve:** `void`

---
### UnlockMissionNewsStory

`UNLOCK_MISSION_NEWS_STORY` · hash `0xB165AB7C248B2DC1` · jhash `0xCCD9ABE4` · **Cliente**

```lua
UnlockMissionNewsStory(newsStory)
```
```c
void UNLOCK_MISSION_NEWS_STORY(int newsStory);
```

**Parámetros**

- `newsStory` (`int`)

**Devuelve:** `void`

---
### UnlockRadioStationTrackList

`UNLOCK_RADIO_STATION_TRACK_LIST` · hash `0x031ACB6ABA18C729` · jhash `0xBE998184` · **Cliente**

```lua
UnlockRadioStationTrackList(radioStation, trackListName)
```
```c
void UNLOCK_RADIO_STATION_TRACK_LIST(char* radioStation, char* trackListName);
```

**Parámetros**

- `radioStation` (`char*`)
- `trackListName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
AUDIO::UNLOCK_RADIO_STATION_TRACK_LIST("RADIO_16_SILVERLAKE", "MIRRORPARK_LOCKED");
```

**Nombres antiguos (alias):** `0x031ACB6ABA18C729` (`N_0x031acb6aba18c729`)

---
### UnregisterScriptWithAudio

`UNREGISTER_SCRIPT_WITH_AUDIO` · hash `0xA8638BE228D4751A` · jhash `0x66728EFE` · **Cliente**

```lua
UnregisterScriptWithAudio()
```
```c
void UNREGISTER_SCRIPT_WITH_AUDIO();
```

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

```
On last-gen this just runs blr and this func is called by several other functions other then the native's table.  
```

---
### UnrequestTennisBanks

`UNREQUEST_TENNIS_BANKS` · hash `0x0150B6FF25A9E2E5` · jhash `0x1134F68B` · **Cliente**

```lua
UnrequestTennisBanks()
```
```c
void UNREQUEST_TENNIS_BANKS();
```

**Devuelve:** `void`

**Descripción oficial:**

Unloads tennis vocalization banks loaded with [`REQUEST_TENNIS_BANKS`](#requesttennisbanks).

**Nombres antiguos (alias):** `0x0150B6FF25A9E2E5` (`N_0x0150b6ff25a9e2e5`)

---
### UpdateSoundCoord

`UPDATE_SOUND_COORD` · hash `0x7EC3C679D0E7E46B` · **Cliente**

```lua
UpdateSoundCoord(soundId, x, y, z)
```
```c
void UPDATE_SOUND_COORD(int soundId, float x, float y, float z);
```

**Parámetros**

- `soundId` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Updates a playing sounds absolute position.

**Nombres antiguos (alias):** `0x7EC3C679D0E7E46B` (`N_0x7ec3c679d0e7e46b`)

---
### UpdateUnlockableDjRadioTracks

`UPDATE_UNLOCKABLE_DJ_RADIO_TRACKS` · hash `0x47AED84213A47510` · **Cliente**

```lua
UpdateUnlockableDjRadioTracks(allowTrackReprioritization)
```
```c
void UPDATE_UNLOCKABLE_DJ_RADIO_TRACKS(BOOL allowTrackReprioritization);
```

**Parámetros**

- `allowTrackReprioritization` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Unlocks any available DJ radio tracks based on the tuneable status

```
NativeDB Introduced: v1493	
```

**Nombres antiguos (alias):** `_UPDATE_LSUR` (`UpdateLsur`)

---
### UseFootstepScriptSweeteners

`USE_FOOTSTEP_SCRIPT_SWEETENERS` · hash `0xBF4DC1784BE94DFA` · jhash `0xD99E275B` · **Cliente**

```lua
UseFootstepScriptSweeteners(ped, useSweetner, soundSetHash)
```
```c
void USE_FOOTSTEP_SCRIPT_SWEETENERS(Ped ped, BOOL useSweetner, Hash soundSetHash);
```

**Parámetros**

- `ped` (`Ped`)
- `useSweetner` (`BOOL`)
- `soundSetHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

Allows script to trigger a sweetener footstep sound

**Nombres antiguos (alias):** `0xBF4DC1784BE94DFA` (`N_0xbf4dc1784be94dfa`)

---
### UseSirenAsHorn

`USE_SIREN_AS_HORN` · hash `0xFA932DE350266EF8` · jhash `0xC6BC16F3` · **Cliente**

```lua
UseSirenAsHorn(vehicle, sirenAsHorn)
```
```c
void USE_SIREN_AS_HORN(Vehicle vehicle, BOOL sirenAsHorn);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `sirenAsHorn` (`BOOL`)

**Devuelve:** `void`

---
