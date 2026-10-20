# Natives de GTA V — CUTSCENE

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `CUTSCENE`: **54** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`CanRequestAssetsForCutsceneEntity`](#canrequestassetsforcutsceneentity) · [`CanSetEnterStateForRegisteredEntity`](#cansetenterstateforregisteredentity) · [`CanSetExitStateForCamera`](#cansetexitstateforcamera) · [`CanSetExitStateForRegisteredEntity`](#cansetexitstateforregisteredentity) · [`DoesCutsceneEntityExist`](#doescutsceneentityexist) · [`GetCutFileNumSections`](#getcutfilenumsections) · [`GetCutsceneEndTime`](#getcutsceneendtime) · [`GetCutscenePlayTime`](#getcutsceneplaytime) · [`GetCutsceneSectionPlaying`](#getcutscenesectionplaying) · [`GetCutsceneTime`](#getcutscenetime) · [`GetCutsceneTotalDuration`](#getcutscenetotalduration) · [`GetEntityIndexOfCutsceneEntity`](#getentityindexofcutsceneentity) · [`GetEntityIndexOfRegisteredEntity`](#getentityindexofregisteredentity) · [`HasCutFileLoaded`](#hascutfileloaded) · [`HasCutsceneCutThisFrame`](#hascutscenecutthisframe) · [`HasCutsceneFinished`](#hascutscenefinished) · [`HasCutsceneLoaded`](#hascutsceneloaded) · [`HasThisCutsceneLoaded`](#hasthiscutsceneloaded) · [`IsCutsceneActive`](#iscutsceneactive) · [`IsCutscenePlaybackFlagSet`](#iscutsceneplaybackflagset) · [`IsCutscenePlaying`](#iscutsceneplaying) · [`N_0x06ee9048fd080382`](#n_0x06ee9048fd080382) · [`N_0x20746f7b1032a3c7`](#n_0x20746f7b1032a3c7) · [`N_0x2f137b508de238f2`](#n_0x2f137b508de238f2) · [`N_0x4cebc1ed31e8925e`](#n_0x4cebc1ed31e8925e) · [`N_0x4fcd976da686580c`](#n_0x4fcd976da686580c) · [`N_0x583df8e3d4afbd98`](#n_0x583df8e3d4afbd98) · [`N_0x5edef0cf8c1dab3c`](#n_0x5edef0cf8c1dab3c) · [`N_0x7f96f23fa9b73327`](#n_0x7f96f23fa9b73327) · [`N_0x8d9df6eca8768583`](#n_0x8d9df6eca8768583) · [`N_0xa0fe76168a189ddb`](#n_0xa0fe76168a189ddb) · [`N_0xc61b86c9f61eb404`](#n_0xc61b86c9f61eb404) · [`N_0xe36a98d8ab3d3c66`](#n_0xe36a98d8ab3d3c66) · [`RegisterEntityForCutscene`](#registerentityforcutscene) · [`RegisterSynchronisedScriptSpeech`](#registersynchronisedscriptspeech) · [`RemoveCutFile`](#removecutfile) · [`RemoveCutscene`](#removecutscene) · [`RequestCutFile`](#requestcutfile) · [`RequestCutscene`](#requestcutscene) · [`RequestCutsceneWithPlaybackList`](#requestcutscenewithplaybacklist) · [`SetCutsceneCanBeSkipped`](#setcutscenecanbeskipped) · [`SetCutsceneEntityStreamingFlags`](#setcutsceneentitystreamingflags) · [`SetCutsceneFadeValues`](#setcutscenefadevalues) · [`SetCutsceneOrigin`](#setcutsceneorigin) · [`SetCutsceneOriginAndOrientation`](#setcutsceneoriginandorientation) · [`SetCutscenePedComponentVariation`](#setcutscenepedcomponentvariation) · [`SetCutscenePedComponentVariationFromPed`](#setcutscenepedcomponentvariationfromped) · [`SetCutscenePedPropVariation`](#setcutscenepedpropvariation) · [`SetCutsceneTriggerArea`](#setcutscenetriggerarea) · [`StartCutscene`](#startcutscene) · [`StartCutsceneAtCoords`](#startcutsceneatcoords) · [`StopCutscene`](#stopcutscene) · [`StopCutsceneImmediately`](#stopcutsceneimmediately) · [`WasCutsceneSkipped`](#wascutsceneskipped)

---
### CanRequestAssetsForCutsceneEntity

`CAN_REQUEST_ASSETS_FOR_CUTSCENE_ENTITY` · hash `0xB56BBBCC2955D9CB` · jhash `0xDD8878E9` · **Cliente**

```lua
local retval = CanRequestAssetsForCutsceneEntity()
```
```c
BOOL CAN_REQUEST_ASSETS_FOR_CUTSCENE_ENTITY();
```

**Devuelve:** `BOOL` — Whether you can request assets for cutscene entities, like components.

**Descripción oficial:**

Returns when it is safe to start applying changes to cutscene entities.

Should always be used for applying components.

See [`SET_CUTSCENE_PED_COMPONENT_VARIATION_FROM_PED`](#setcutscenepedcomponentvariationfromped) and [`REGISTER_ENTITY_FOR_CUTSCENE`](#registerentityforcutscene) for an example.

This will be true before the cutscene is considered loaded

**Nombres antiguos (alias):** `0xB56BBBCC2955D9CB` (`N_0xb56bbbcc2955d9cb`)

---
### CanSetEnterStateForRegisteredEntity

`CAN_SET_ENTER_STATE_FOR_REGISTERED_ENTITY` · hash `0x645D0B458D8E17B5` · jhash `0x55C30B26` · **Cliente**

```lua
local retval = CanSetEnterStateForRegisteredEntity(cutsceneEntName, modelHash)
```
```c
BOOL CAN_SET_ENTER_STATE_FOR_REGISTERED_ENTITY(char* cutsceneEntName, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
modelHash (p1) was always 0 in R* scripts  
```

---
### CanSetExitStateForCamera

`CAN_SET_EXIT_STATE_FOR_CAMERA` · hash `0xB2CBCD0930DFB420` · jhash `0xEDAE6C02` · **Cliente**

```lua
local retval = CanSetExitStateForCamera(p0)
```
```c
BOOL CAN_SET_EXIT_STATE_FOR_CAMERA(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Whether or not it is safe to run functions on the camera,
as the camera is now no longer being used by the cutscene.

---
### CanSetExitStateForRegisteredEntity

`CAN_SET_EXIT_STATE_FOR_REGISTERED_ENTITY` · hash `0x4C6A6451C79E4662` · jhash `0x8FF5D3C4` · **Cliente**

```lua
local retval = CanSetExitStateForRegisteredEntity(cutsceneEntName, modelHash)
```
```c
BOOL CAN_SET_EXIT_STATE_FOR_REGISTERED_ENTITY(char* cutsceneEntName, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`): Name of the entity cHandle in the cutscene
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Can be 0

**Devuelve:** `BOOL` — Whether or not it is safe to begin interacting with the entity

**Descripción oficial:**

Returns if the script can begin interacting with the registered entity. Primarly used for lead-outs of cutscenes.
Returns on frame after cutscene ends, so you cannot get is while using IsCutsceneActive()

Whether it is safe to start doing scripted actions on the entity, like simulating walking out of a cutscene.

---
### DoesCutsceneEntityExist

`DOES_CUTSCENE_ENTITY_EXIST` · hash `0x499EF20C5DB25C59` · jhash `0x58E67409` · **Cliente**

```lua
local retval = DoesCutsceneEntityExist(cutsceneEntName, modelHash)
```
```c
BOOL DOES_CUTSCENE_ENTITY_EXIST(char* cutsceneEntName, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### GetCutFileNumSections

`_GET_CUT_FILE_NUM_SECTIONS` · hash `0x0ABC54DE641DC0FC` · jhash `0xFD8B1AC2` · **Cliente**

```lua
local retval = GetCutFileNumSections(cutsceneName)
```
```c
int _GET_CUT_FILE_NUM_SECTIONS(char* cutsceneName);
```

**Parámetros**

- `cutsceneName` (`char*`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0ABC54DE641DC0FC` (`N_0x0abc54de641dc0fc`)

---
### GetCutsceneEndTime

`GET_CUTSCENE_END_TIME` · hash `0x971D7B15BCDBEF99` · **Cliente**

```lua
local retval = GetCutsceneEndTime()
```
```c
int GET_CUTSCENE_END_TIME();
```

**Devuelve:** `int`

**Descripción oficial:**

Returns the time of the cutscene's end accounting for [`REQUEST_CUTSCENE_WITH_PLAYBACK_LIST`](#requestcutscenewithplaybacklist)

If a cutscene is laid out with 10 second sections, and section 0 and 1 are enabled then it would be 20000ms.

```
NativeDB Introduced: v1734
```

**Nombres antiguos (alias):** `0x971D7B15BCDBEF99` (`N_0x971d7b15bcdbef99`), `_GET_CUTSCENE_END_TIME` (`GetCutsceneEndTime`)

---
### GetCutscenePlayTime

`GET_CUTSCENE_PLAY_TIME` · hash `0x710286BC5EF4D6E1` · **Cliente**

```lua
local retval = GetCutscenePlayTime()
```
```c
int GET_CUTSCENE_PLAY_TIME();
```

**Devuelve:** `int` — Returns the current play time of the cutscene in milliseconds.

**Descripción oficial:**

Gets the current time of the cutscene.

```
NativeDB Introduced: v3258
```

---
### GetCutsceneSectionPlaying

`GET_CUTSCENE_SECTION_PLAYING` · hash `0x49010A6A396553D8` · jhash `0x1026F0D6` · **Cliente**

```lua
local retval = GetCutsceneSectionPlaying()
```
```c
int GET_CUTSCENE_SECTION_PLAYING();
```

**Devuelve:** `int`

---
### GetCutsceneTime

`GET_CUTSCENE_TIME` · hash `0xE625BEABBAFFDAB9` · jhash `0x53F5B5AB` · **Cliente**

```lua
local retval = GetCutsceneTime()
```
```c
int GET_CUTSCENE_TIME();
```

**Devuelve:** `int` — Elapsed time in milliseconds

**Descripción oficial:**

Gets the elapsed time of the current cutscene in

---
### GetCutsceneTotalDuration

`GET_CUTSCENE_TOTAL_DURATION` · hash `0xEE53B14A19E480D4` · jhash `0x0824EBE8` · **Cliente**

```lua
local retval = GetCutsceneTotalDuration()
```
```c
int GET_CUTSCENE_TOTAL_DURATION();
```

**Devuelve:** `int` — Cutscene total length in milliseconds

**Descripción oficial:**

Gets the total length of the cutscene irrespective of playback list in milliseconds
To account for sections, see [`GET_CUTSCENE_END_TIME`](#getcutsceneendtime)

---
### GetEntityIndexOfCutsceneEntity

`GET_ENTITY_INDEX_OF_CUTSCENE_ENTITY` · hash `0x0A2E9FDB9A8C62F6` · jhash `0x1D09ABC7` · **Cliente**

```lua
local retval = GetEntityIndexOfCutsceneEntity(cutsceneEntName, modelHash)
```
```c
Entity GET_ENTITY_INDEX_OF_CUTSCENE_ENTITY(char* cutsceneEntName, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`): I.E MP\_1, MP\_4, Michael, Trevor
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Not strictly neccasary, can get 0

**Devuelve:** `Entity` — Returns entity handle

**Descripción oficial:**

Returns the handle of a cutscene entity, can be ped

---
### GetEntityIndexOfRegisteredEntity

`GET_ENTITY_INDEX_OF_REGISTERED_ENTITY` · hash `0xC0741A26499654CD` · jhash `0x46D18755` · **Cliente**

```lua
local retval = GetEntityIndexOfRegisteredEntity(cutsceneEntName, modelHash)
```
```c
Entity GET_ENTITY_INDEX_OF_REGISTERED_ENTITY(char* cutsceneEntName, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Entity`

---
### HasCutFileLoaded

`HAS_CUT_FILE_LOADED` · hash `0xA1C996C2A744262E` · jhash `0x56D5B144` · **Cliente**

```lua
local retval = HasCutFileLoaded(cutsceneName)
```
```c
BOOL HAS_CUT_FILE_LOADED(char* cutsceneName);
```

**Parámetros**

- `cutsceneName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Simply checks if the cutscene has loaded and doesn't check via CutSceneManager as opposed to HAS_[THIS]_CUTSCENE_LOADED.
```

**Nombres antiguos (alias):** `0xA1C996C2A744262E` (`N_0xa1c996c2a744262e`)

---
### HasCutsceneCutThisFrame

`HAS_CUTSCENE_CUT_THIS_FRAME` · hash `0x708BDD8CD795B043` · jhash `0x4315A7C5` · **Cliente**

```lua
local retval = HasCutsceneCutThisFrame()
```
```c
BOOL HAS_CUTSCENE_CUT_THIS_FRAME();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x708BDD8CD795B043` (`N_0x708bdd8cd795b043`)

---
### HasCutsceneFinished

`HAS_CUTSCENE_FINISHED` · hash `0x7C0A893088881D57` · jhash `0x5DED14B4` · **Cliente**

```lua
local retval = HasCutsceneFinished()
```
```c
BOOL HAS_CUTSCENE_FINISHED();
```

**Devuelve:** `BOOL`

---
### HasCutsceneLoaded

`HAS_CUTSCENE_LOADED` · hash `0xC59F528E9AB9F339` · jhash `0xF9998582` · **Cliente**

```lua
local retval = HasCutsceneLoaded()
```
```c
BOOL HAS_CUTSCENE_LOADED();
```

**Devuelve:** `BOOL`

---
### HasThisCutsceneLoaded

`HAS_THIS_CUTSCENE_LOADED` · hash `0x228D3D94F8A11C3C` · jhash `0x3C5619F2` · **Cliente**

```lua
local retval = HasThisCutsceneLoaded(cutsceneName)
```
```c
BOOL HAS_THIS_CUTSCENE_LOADED(char* cutsceneName);
```

**Parámetros**

- `cutsceneName` (`char*`)

**Devuelve:** `BOOL`

---
### IsCutsceneActive

`IS_CUTSCENE_ACTIVE` · hash `0x991251AFC3981F84` · jhash `0xCCE2FE9D` · **Cliente**

```lua
local retval = IsCutsceneActive()
```
```c
BOOL IS_CUTSCENE_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsCutscenePlaybackFlagSet

`IS_CUTSCENE_PLAYBACK_FLAG_SET` · hash `0x71B74D2AE19338D0` · jhash `0x7B93CDAA` · **Cliente**

```lua
local retval = IsCutscenePlaybackFlagSet(flag)
```
```c
BOOL IS_CUTSCENE_PLAYBACK_FLAG_SET(int flag);
```

**Parámetros**

- `flag` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x71B74D2AE19338D0` (`N_0x71b74d2ae19338d0`)

---
### IsCutscenePlaying

`IS_CUTSCENE_PLAYING` · hash `0xD3C2E180A40F031E` · jhash `0xA3A78392` · **Cliente**

```lua
local retval = IsCutscenePlaying()
```
```c
BOOL IS_CUTSCENE_PLAYING();
```

**Devuelve:** `BOOL`

---
### N_0x06ee9048fd080382

`0x06EE9048FD080382` · hash `0x06EE9048FD080382` · **Cliente**

```lua
N_0x06ee9048fd080382(p0)
```
```c
void 0x06EE9048FD080382(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x20746f7b1032a3c7

`0x20746F7B1032A3C7` · hash `0x20746F7B1032A3C7` · **Cliente**

```lua
N_0x20746f7b1032a3c7(p0, p1, p2, p3)
```
```c
void 0x20746F7B1032A3C7(BOOL p0, BOOL p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### N_0x2f137b508de238f2

`0x2F137B508DE238F2` · hash `0x2F137B508DE238F2` · jhash `0x8338DA1D` · **Cliente**

```lua
N_0x2f137b508de238f2(p0)
```
```c
void 0x2F137B508DE238F2(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x4cebc1ed31e8925e

`0x4CEBC1ED31E8925E` · hash `0x4CEBC1ED31E8925E` · **Cliente**

```lua
local retval = N_0x4cebc1ed31e8925e(cutsceneName)
```
```c
BOOL 0x4CEBC1ED31E8925E(char* cutsceneName);
```

**Parámetros**

- `cutsceneName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function is hard-coded to always return 1.  
```

---
### N_0x4fcd976da686580c

`0x4FCD976DA686580C` · hash `0x4FCD976DA686580C` · **Cliente**

```lua
local retval = N_0x4fcd976da686580c(p0)
```
```c
Any 0x4FCD976DA686580C(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x583df8e3d4afbd98

`0x583DF8E3D4AFBD98` · hash `0x583DF8E3D4AFBD98` · jhash `0x5AE68AE6` · **Cliente**

```lua
local retval = N_0x583df8e3d4afbd98()
```
```c
int 0x583DF8E3D4AFBD98();
```

**Devuelve:** `int`

---
### N_0x5edef0cf8c1dab3c

`0x5EDEF0CF8C1DAB3C` · hash `0x5EDEF0CF8C1DAB3C` · jhash `0xDBD88708` · **Cliente**

```lua
local retval = N_0x5edef0cf8c1dab3c()
```
```c
BOOL 0x5EDEF0CF8C1DAB3C();
```

**Devuelve:** `BOOL`

---
### N_0x7f96f23fa9b73327

`0x7F96F23FA9B73327` · hash `0x7F96F23FA9B73327` · **Cliente**

```lua
N_0x7f96f23fa9b73327(modelHash)
```
```c
void 0x7F96F23FA9B73327(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
SET_VEHICLE_*
```

---
### N_0x8d9df6eca8768583

`0x8D9DF6ECA8768583` · hash `0x8D9DF6ECA8768583` · jhash `0x25A2CABC` · **Cliente**

```lua
N_0x8d9df6eca8768583(threadId)
```
```c
void 0x8D9DF6ECA8768583(int threadId);
```

**Parámetros**

- `threadId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_SCRIPT_*
Sets the cutscene's owning thread ID.
```

---
### N_0xa0fe76168a189ddb

`0xA0FE76168A189DDB` · hash `0xA0FE76168A189DDB` · **Cliente**

```lua
local retval = N_0xa0fe76168a189ddb()
```
```c
int 0xA0FE76168A189DDB();
```

**Devuelve:** `int`

---
### N_0xc61b86c9f61eb404

`0xC61B86C9F61EB404` · hash `0xC61B86C9F61EB404` · jhash `0x35721A08` · **Cliente**

```lua
N_0xc61b86c9f61eb404(toggle)
```
```c
void 0xC61B86C9F61EB404(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Toggles a value (bool) for cutscenes.
SET_*
```

---
### N_0xe36a98d8ab3d3c66

`0xE36A98D8AB3D3C66` · hash `0xE36A98D8AB3D3C66` · jhash `0x04377C10` · **Cliente**

```lua
N_0xe36a98d8ab3d3c66(p0)
```
```c
void 0xE36A98D8AB3D3C66(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### RegisterEntityForCutscene

`REGISTER_ENTITY_FOR_CUTSCENE` · hash `0xE40C1C56DF95C2E8` · jhash `0x7CBC3EC7` · **Cliente**

```lua
RegisterEntityForCutscene(cutsceneEntity, cutsceneEntName, p2, modelHash, p4)
```
```c
void REGISTER_ENTITY_FOR_CUTSCENE(Entity cutsceneEntity, char* cutsceneEntName, int p2, Hash modelHash, int p4);
```

**Parámetros**

- `cutsceneEntity` (`Entity`): Entity to put into the cutscene.
- `cutsceneEntName` (`char*`): cHandle of cutscene entity, i.e Michael, MP\_1, MP\_4, Lamar
- `p2` (`int`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Not strictly neccasary, often 0 in R\* scripts
- `p4` (`int`): 0 for SP, 64 for MP seemingly

**Devuelve:** `void`

**Descripción oficial:**

This can only be run once [`CAN_REQUEST_ASSETS_FOR_CUTSCENE_ENTITY`](#canrequestassetsforcutsceneentity) is true, but can be run before [`HAS_CUTSCENE_LOADED`](#hascutsceneloaded)

**Ejemplo (lua):**

```lua
    -- An example that allows for registering non player_zero peds in place, i.e MP peds.
    RequestCutscene("family_5_mcs_5_p5", 8)
    repeat Wait(0) until CanRequestAssetsForCutsceneEntity()
    SetCutscenePedComponentVariationFromPed("Michael", PlayerPedId(), 0)
    -- Registering can occur at any point past here before starting the cutscene.
    RegisterEntityForCutscene(PlayerPedId(), "Michael", 0, 0, 64)
    repeat Wait(0) until HasCutsceneLoaded()
    StartCutscene(0)
```

---
### RegisterSynchronisedScriptSpeech

`REGISTER_SYNCHRONISED_SCRIPT_SPEECH` · hash `0x2131046957F31B04` · jhash `0xB60CFBB9` · **Cliente**

```lua
RegisterSynchronisedScriptSpeech()
```
```c
void REGISTER_SYNCHRONISED_SCRIPT_SPEECH();
```

**Devuelve:** `void`

**Descripción oficial:**

Only used twice in armenian1.c

---
### RemoveCutFile

`REMOVE_CUT_FILE` · hash `0xD00D76A7DFC9D852` · jhash `0xB70D7C6D` · **Cliente**

```lua
RemoveCutFile(cutsceneName)
```
```c
void REMOVE_CUT_FILE(char* cutsceneName);
```

**Parámetros**

- `cutsceneName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Simply unloads the cutscene and doesn't do extra stuff that REMOVE_CUTSCENE does.
```

**Nombres antiguos (alias):** `0xD00D76A7DFC9D852` (`N_0xd00d76a7dfc9d852`)

---
### RemoveCutscene

`REMOVE_CUTSCENE` · hash `0x440AF51A3462B86F` · jhash `0x8052F533` · **Cliente**

```lua
RemoveCutscene()
```
```c
void REMOVE_CUTSCENE();
```

**Devuelve:** `void`

---
### RequestCutFile

`REQUEST_CUT_FILE` · hash `0x06A3524161C502BA` · jhash `0x0D732CD6` · **Cliente**

```lua
RequestCutFile(cutsceneName)
```
```c
void REQUEST_CUT_FILE(char* cutsceneName);
```

**Parámetros**

- `cutsceneName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Simply loads the cutscene and doesn't do extra stuff that REQUEST_CUTSCENE does.
```

**Nombres antiguos (alias):** `0x06A3524161C502BA` (`N_0x06a3524161c502ba`)

---
### RequestCutscene

`REQUEST_CUTSCENE` · hash `0x7A86743F475D9E09` · jhash `0xB5977853` · **Cliente**

```lua
RequestCutscene(cutsceneName, flags)
```
```c
void REQUEST_CUTSCENE(char* cutsceneName, int flags);
```

**Parámetros**

- `cutsceneName` (`char*`): Case insensitive name of the .cut file
- `flags` (`int`): Usually 8

**Devuelve:** `void`

---
### RequestCutsceneWithPlaybackList

`REQUEST_CUTSCENE_WITH_PLAYBACK_LIST` · hash `0xC23DE0E91C30B58C` · jhash `0xD98F656A` · **Cliente**

```lua
RequestCutsceneWithPlaybackList(cutsceneName, playbackFlags, flags)
```
```c
void REQUEST_CUTSCENE_WITH_PLAYBACK_LIST(char* cutsceneName, int playbackFlags, int flags);
```

**Parámetros**

- `cutsceneName` (`char*`)
- `playbackFlags` (`int`)
- `flags` (`int`): Usually 8

**Devuelve:** `void`

**Descripción oficial:**

```
playbackFlags: Which scenes should be played.
Example: 0x105 (bit 0, 2 and 8 set) will enable scene 1, 3 and 9.
```

**Nombres antiguos (alias):** `0xC23DE0E91C30B58C` (`N_0xc23de0e91c30b58c`), `_REQUEST_CUTSCENE_EX` (`RequestCutsceneEx`)

---
### SetCutsceneCanBeSkipped

`SET_CUTSCENE_CAN_BE_SKIPPED` · hash `0x41FAA8FB2ECE8720` · jhash `0x28D54A7F` · **Cliente**

```lua
SetCutsceneCanBeSkipped(p0)
```
```c
void SET_CUTSCENE_CAN_BE_SKIPPED(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x41FAA8FB2ECE8720` (`N_0x41faa8fb2ece8720`)

---
### SetCutsceneEntityStreamingFlags

`SET_CUTSCENE_ENTITY_STREAMING_FLAGS` · hash `0x4C61C75BEE8184C2` · jhash `0x47DB08A9` · **Cliente**

```lua
SetCutsceneEntityStreamingFlags(cutsceneEntName, p1, p2)
```
```c
void SET_CUTSCENE_ENTITY_STREAMING_FLAGS(char* cutsceneEntName, int p1, int p2);
```

**Parámetros**

- `cutsceneEntName` (`char*`): MP\_1, MP\_2, etc
- `p1` (`int`): Always 0 in R\* scripts
- `p2` (`int`): Always 1 in R\* scripts

**Devuelve:** `void`

**Descripción oficial:**

Only used in networked environment with MP cutscenes

**Nombres antiguos (alias):** `0x4C61C75BEE8184C2` (`N_0x4c61c75bee8184c2`)

---
### SetCutsceneFadeValues

`SET_CUTSCENE_FADE_VALUES` · hash `0x8093F23ABACCC7D4` · jhash `0xD19EF0DD` · **Cliente**

```lua
SetCutsceneFadeValues(p0, p1, p2, p3)
```
```c
void SET_CUTSCENE_FADE_VALUES(BOOL p0, BOOL p1, BOOL p2, BOOL p3);
```

**Parámetros**

- `p0` (`BOOL`)
- `p1` (`BOOL`)
- `p2` (`BOOL`)
- `p3` (`BOOL`)

**Devuelve:** `void`

---
### SetCutsceneOrigin

`SET_CUTSCENE_ORIGIN` · hash `0xB812B3FD1C01CF27` · jhash `0xB0AD7792` · **Cliente**

```lua
SetCutsceneOrigin(x, y, z, heading, p4)
```
```c
void SET_CUTSCENE_ORIGIN(float x, float y, float z, float heading, int p4);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `p4` (`int`): Often -1, 0 or 1

**Devuelve:** `void`

**Descripción oficial:**

Sets cutscene location, used for multiplayer apartments/businesses.

---
### SetCutsceneOriginAndOrientation

`SET_CUTSCENE_ORIGIN_AND_ORIENTATION` · hash `0x011883F41211432A` · **Cliente**

```lua
SetCutsceneOriginAndOrientation(x1, y1, z1, x2, y2, z2, p6)
```
```c
void SET_CUTSCENE_ORIGIN_AND_ORIENTATION(float x1, float y1, float z1, float x2, float y2, float z2, int p6);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `p6` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x011883F41211432A` (`N_0x011883f41211432a`)

---
### SetCutscenePedComponentVariation

`SET_CUTSCENE_PED_COMPONENT_VARIATION` · hash `0xBA01E7B6DEEFBBC9` · jhash `0x6AF994A1` · **Cliente**

```lua
SetCutscenePedComponentVariation(cutsceneEntName, componentId, drawableId, textureId, modelHash)
```
```c
void SET_CUTSCENE_PED_COMPONENT_VARIATION(char* cutsceneEntName, int componentId, int drawableId, int textureId, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`)
- `componentId` (`int`)
- `drawableId` (`int`)
- `textureId` (`int`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

See [`SET_PED_COMPONENT_VARIATION`](../cfx/servidor.md#setpedcomponentvariation)

---
### SetCutscenePedComponentVariationFromPed

`SET_CUTSCENE_PED_COMPONENT_VARIATION_FROM_PED` · hash `0x2A56C06EBEF2B0D9` · jhash `0x1E7DA95E` · **Cliente**

```lua
SetCutscenePedComponentVariationFromPed(cutsceneEntName, ped, modelHash)
```
```c
void SET_CUTSCENE_PED_COMPONENT_VARIATION_FROM_PED(char* cutsceneEntName, Ped ped, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`): Cutscene file cHandle, i.e Michael, Lamar, Franklin, MP\_1-MP\_4
- `ped` (`Ped`): Ped to copy components from
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Not strictly neccasary, can be 0

**Devuelve:** `void`

**Descripción oficial:**

Sets the components for a cutscene ped, this will take precendence over the cutscene's component overrides. This does not require the entity be registered.

See [`REGISTER_ENTITY_FOR_CUTSCENE`](#registerentityforcutscene) for an example.

**Nombres antiguos (alias):** `0x2A56C06EBEF2B0D9` (`N_0x2a56c06ebef2b0d9`)

---
### SetCutscenePedPropVariation

`SET_CUTSCENE_PED_PROP_VARIATION` · hash `0x0546524ADE2E9723` · jhash `0x22E9A9DE` · **Cliente**

```lua
SetCutscenePedPropVariation(cutsceneEntName, componentId, drawableId, textureId, modelHash)
```
```c
void SET_CUTSCENE_PED_PROP_VARIATION(char* cutsceneEntName, int componentId, int drawableId, int textureId, Hash modelHash);
```

**Parámetros**

- `cutsceneEntName` (`char*`): i.e Michael, Trevor, MP\_1, MP\_4
- `componentId` (`int`)
- `drawableId` (`int`)
- `textureId` (`int`)
- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

See [`SET_PED_PROP_INDEX`](../cfx/servidor.md#setpedpropindex)

**Nombres antiguos (alias):** `0x0546524ADE2E9723` (`N_0x0546524ade2e9723`)

---
### SetCutsceneTriggerArea

`SET_CUTSCENE_TRIGGER_AREA` · hash `0x9896CE4721BE84BA` · jhash `0x9D76D9DE` · **Cliente**

```lua
SetCutsceneTriggerArea(p0, p1, p2, p3, p4, p5)
```
```c
void SET_CUTSCENE_TRIGGER_AREA(float p0, float p1, float p2, float p3, float p4, float p5);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only used twice in R* scripts  
```

---
### StartCutscene

`START_CUTSCENE` · hash `0x186D5CB5E7B0FF7B` · jhash `0x210106F6` · **Cliente**

```lua
StartCutscene(flags)
```
```c
void START_CUTSCENE(int flags);
```

**Parámetros**

- `flags` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
flags: Usually 0.
```

---
### StartCutsceneAtCoords

`START_CUTSCENE_AT_COORDS` · hash `0x1C9ADDA3244A1FBF` · jhash `0x58BEA436` · **Cliente**

```lua
StartCutsceneAtCoords(x, y, z, flags)
```
```c
void START_CUTSCENE_AT_COORDS(float x, float y, float z, int flags);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `flags` (`int`): Usually 0

**Devuelve:** `void`

**Descripción oficial:**

Similar to [`SET_CUTSCENE_ORIGIN`](#setcutsceneorigin) but without heading and doesn't need [`START_CUTSCENE`](#startcutscene)

---
### StopCutscene

`STOP_CUTSCENE` · hash `0xC7272775B4DC786E` · jhash `0x5EE84DC7` · **Cliente**

```lua
StopCutscene(p0)
```
```c
void STOP_CUTSCENE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`): Always false

**Devuelve:** `void`

---
### StopCutsceneImmediately

`STOP_CUTSCENE_IMMEDIATELY` · hash `0xD220BDD222AC4A1E` · jhash `0xF528A2AD` · **Cliente**

```lua
StopCutsceneImmediately()
```
```c
void STOP_CUTSCENE_IMMEDIATELY();
```

**Devuelve:** `void`

**Descripción oficial:**

Stop cutscene instantly, will dump registered entities right where they were when ran.

---
### WasCutsceneSkipped

`WAS_CUTSCENE_SKIPPED` · hash `0x40C8656EDAEDD569` · jhash `0xC9B6949D` · **Cliente**

```lua
local retval = WasCutsceneSkipped()
```
```c
BOOL WAS_CUTSCENE_SKIPPED();
```

**Devuelve:** `BOOL`

---
