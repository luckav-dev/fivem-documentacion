# Natives de GTA V — STREAMING

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `STREAMING`: **121** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddModelToCreatorBudget`](#addmodeltocreatorbudget) · [`AllowPlayerSwitchAscent`](#allowplayerswitchascent) · [`AllowPlayerSwitchDescent`](#allowplayerswitchdescent) · [`AllowPlayerSwitchOutro`](#allowplayerswitchoutro) · [`AllowPlayerSwitchPan`](#allowplayerswitchpan) · [`BeginSrl`](#beginsrl) · [`ClearFocus`](#clearfocus) · [`ClearHdArea`](#clearhdarea) · [`DisableSwitchOutroFx`](#disableswitchoutrofx) · [`DoesAnimDictExist`](#doesanimdictexist) · [`EnableSwitchPauseBeforeDescent`](#enableswitchpausebeforedescent) · [`EndSrl`](#endsrl) · [`GetGlobalWaterType`](#getglobalwatertype) · [`GetIdealPlayerSwitchType`](#getidealplayerswitchtype) · [`GetLodscale`](#getlodscale) · [`GetNumberOfStreamingRequests`](#getnumberofstreamingrequests) · [`GetPlayerShortSwitchState`](#getplayershortswitchstate) · [`GetPlayerSwitchInterpOutCurrentTime`](#getplayerswitchinterpoutcurrenttime) · [`GetPlayerSwitchInterpOutDuration`](#getplayerswitchinterpoutduration) · [`GetPlayerSwitchJumpCutIndex`](#getplayerswitchjumpcutindex) · [`GetPlayerSwitchState`](#getplayerswitchstate) · [`GetPlayerSwitchType`](#getplayerswitchtype) · [`GetUsedCreatorModelMemoryPercentage`](#getusedcreatormodelmemorypercentage) · [`HasAnimDictLoaded`](#hasanimdictloaded) · [`HasAnimSetLoaded`](#hasanimsetloaded) · [`HasClipSetLoaded`](#hasclipsetloaded) · [`HasCollisionForModelLoaded`](#hascollisionformodelloaded) · [`HasModelLoaded`](#hasmodelloaded) · [`HasNamedPtfxAssetLoaded`](#hasnamedptfxassetloaded) · [`HasPtfxAssetLoaded`](#hasptfxassetloaded) · [`InitCreatorBudget`](#initcreatorbudget) · [`IsEntityFocus`](#isentityfocus) · [`IsIplActive`](#isiplactive) · [`IsModelAPed`](#ismodelaped) · [`IsModelAVehicle`](#ismodelavehicle) · [`IsModelInCdimage`](#ismodelincdimage) · [`IsModelValid`](#ismodelvalid) · [`IsNetworkLoadingScene`](#isnetworkloadingscene) · [`IsNewLoadSceneActive`](#isnewloadsceneactive) · [`IsNewLoadSceneLoaded`](#isnewloadsceneloaded) · [`IsPlayerSwitchInProgress`](#isplayerswitchinprogress) · [`IsSrlLoaded`](#issrlloaded) · [`IsStreamvolActive`](#isstreamvolactive) · [`IsSwitchReadyForDescent`](#isswitchreadyfordescent) · [`IsSwitchSkippingDescent`](#isswitchskippingdescent) · [`LoadAllObjectsNow`](#loadallobjectsnow) · [`LoadGlobalWaterType`](#loadglobalwatertype) · [`LoadScene`](#loadscene) · [`N_0x03f1a106bda7dd3e`](#n_0x03f1a106bda7dd3e) · [`N_0x0811381ef5062fec`](#n_0x0811381ef5062fec) · [`N_0x1e9057a74fd73e23`](#n_0x1e9057a74fd73e23) · [`N_0x20c6c7e4eb082a7f`](#n_0x20c6c7e4eb082a7f) · [`N_0x472397322e92a856`](#n_0x472397322e92a856) · [`N_0x4e52e752c76e7e7a`](#n_0x4e52e752c76e7e7a) · [`N_0x5068f488ddb54dd8`](#n_0x5068f488ddb54dd8) · [`N_0x63eb2b972a218cac`](#n_0x63eb2b972a218cac) · [`N_0x71e7b2e657449aad`](#n_0x71e7b2e657449aad) · [`N_0x933bbeeb8c61b5f4`](#n_0x933bbeeb8c61b5f4) · [`N_0x95a7dabddbb78ae7`](#n_0x95a7dabddbb78ae7) · [`N_0xbeb2d9a1d9a8f55a`](#n_0xbeb2d9a1d9a8f55a) · [`N_0xbed8ca5ff5e04113`](#n_0xbed8ca5ff5e04113) · [`N_0xef39ee20c537e98c`](#n_0xef39ee20c537e98c) · [`N_0xf4a0dadb70f57fa6`](#n_0xf4a0dadb70f57fa6) · [`N_0xf8155a7f03ddfc8e`](#n_0xf8155a7f03ddfc8e) · [`N_0xfb199266061f820a`](#n_0xfb199266061f820a) · [`NetworkStopLoadScene`](#networkstoploadscene) · [`NetworkUpdateLoadScene`](#networkupdateloadscene) · [`NewLoadSceneStart`](#newloadscenestart) · [`NewLoadSceneStartSphere`](#newloadscenestartsphere) · [`NewLoadSceneStop`](#newloadscenestop) · [`OverrideLodscaleThisFrame`](#overridelodscalethisframe) · [`PrefetchSrl`](#prefetchsrl) · [`RemoveAnimDict`](#removeanimdict) · [`RemoveAnimSet`](#removeanimset) · [`RemoveClipSet`](#removeclipset) · [`RemoveIpl`](#removeipl) · [`RemoveModelFromCreatorBudget`](#removemodelfromcreatorbudget) · [`RemoveNamedPtfxAsset`](#removenamedptfxasset) · [`RemovePtfxAsset`](#removeptfxasset) · [`RequestAdditionalCollisionAtCoord`](#requestadditionalcollisionatcoord) · [`RequestAnimDict`](#requestanimdict) · [`RequestAnimSet`](#requestanimset) · [`RequestClipSet`](#requestclipset) · [`RequestCollisionAtCoord`](#requestcollisionatcoord) · [`RequestCollisionForModel`](#requestcollisionformodel) · [`RequestIpl`](#requestipl) · [`RequestMenuPedModel`](#requestmenupedmodel) · [`RequestModel`](#requestmodel) · [`RequestModelsInRoom`](#requestmodelsinroom) · [`RequestNamedPtfxAsset`](#requestnamedptfxasset) · [`RequestPtfxAsset`](#requestptfxasset) · [`SetDitchPoliceModels`](#setditchpolicemodels) · [`SetFocusEntity`](#setfocusentity) · [`SetFocusPosAndVel`](#setfocusposandvel) · [`SetGamePausesForStreaming`](#setgamepausesforstreaming) · [`SetHdArea`](#sethdarea) · [`SetInteriorActive`](#setinterioractive) · [`SetIslandEnabled`](#setislandenabled) · [`SetMapdatacullboxEnabled`](#setmapdatacullboxenabled) · [`SetModelAsNoLongerNeeded`](#setmodelasnolongerneeded) · [`SetPedPopulationBudget`](#setpedpopulationbudget) · [`SetPlayerShortSwitchStyle`](#setplayershortswitchstyle) · [`SetPlayerSwitchEstablishingShot`](#setplayerswitchestablishingshot) · [`SetPlayerSwitchOutro`](#setplayerswitchoutro) · [`SetReducePedModelBudget`](#setreducepedmodelbudget) · [`SetReduceVehicleModelBudget`](#setreducevehiclemodelbudget) · [`SetRenderHdOnly`](#setrenderhdonly) · [`SetSrlTime`](#setsrltime) · [`SetStreaming`](#setstreaming) · [`SetVehiclePopulationBudget`](#setvehiclepopulationbudget) · [`ShutdownCreatorBudget`](#shutdowncreatorbudget) · [`StartPlayerSwitch`](#startplayerswitch) · [`StopPlayerSwitch`](#stopplayerswitch) · [`StreamvolCreateFrustum`](#streamvolcreatefrustum) · [`StreamvolCreateLine`](#streamvolcreateline) · [`StreamvolCreateSphere`](#streamvolcreatesphere) · [`StreamvolDelete`](#streamvoldelete) · [`StreamvolHasLoaded`](#streamvolhasloaded) · [`StreamvolIsValid`](#streamvolisvalid) · [`SwitchToMultiFirstpart`](#switchtomultifirstpart) · [`SwitchToMultiSecondpart`](#switchtomultisecondpart)

---
### AddModelToCreatorBudget

`ADD_MODEL_TO_CREATOR_BUDGET` · hash `0x0BC3144DEB678666` · jhash `0xC0E83320` · **Cliente**

```lua
local retval = AddModelToCreatorBudget(modelHash)
```
```c
BOOL ADD_MODEL_TO_CREATOR_BUDGET(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0BC3144DEB678666` (`N_0x0bc3144deb678666`)

---
### AllowPlayerSwitchAscent

`ALLOW_PLAYER_SWITCH_ASCENT` · hash `0x8E2A065ABDAE6994` · jhash `0x5B1E995D` · **Cliente**

```lua
AllowPlayerSwitchAscent()
```
```c
void ALLOW_PLAYER_SWITCH_ASCENT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x8E2A065ABDAE6994` (`N_0x8e2a065abdae6994`)

---
### AllowPlayerSwitchDescent

`ALLOW_PLAYER_SWITCH_DESCENT` · hash `0xAD5FDF34B81BFE79` · jhash `0x4B4B9A13` · **Cliente**

```lua
AllowPlayerSwitchDescent()
```
```c
void ALLOW_PLAYER_SWITCH_DESCENT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xAD5FDF34B81BFE79` (`N_0xad5fdf34b81bfe79`)

---
### AllowPlayerSwitchOutro

`ALLOW_PLAYER_SWITCH_OUTRO` · hash `0x74DE2E8739086740` · jhash `0x1084F2F4` · **Cliente**

```lua
AllowPlayerSwitchOutro()
```
```c
void ALLOW_PLAYER_SWITCH_OUTRO();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x74DE2E8739086740` (`N_0x74de2e8739086740`)

---
### AllowPlayerSwitchPan

`ALLOW_PLAYER_SWITCH_PAN` · hash `0x43D1680C6D19A8E9` · jhash `0x55CB21F9` · **Cliente**

```lua
AllowPlayerSwitchPan()
```
```c
void ALLOW_PLAYER_SWITCH_PAN();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x43D1680C6D19A8E9` (`N_0x43d1680c6d19a8e9`)

---
### BeginSrl

`BEGIN_SRL` · hash `0x9BADDC94EF83B823` · jhash `0x24F49427` · **Cliente**

```lua
BeginSrl()
```
```c
void BEGIN_SRL();
```

**Devuelve:** `void`

---
### ClearFocus

`CLEAR_FOCUS` · hash `0x31B73D1EA9F01DA2` · jhash `0x34D91E7A` · **Cliente**

```lua
ClearFocus()
```
```c
void CLEAR_FOCUS();
```

**Devuelve:** `void`

---
### ClearHdArea

`CLEAR_HD_AREA` · hash `0xCE58B1CFB9290813` · jhash `0x7CAC6FA0` · **Cliente**

```lua
ClearHdArea()
```
```c
void CLEAR_HD_AREA();
```

**Devuelve:** `void`

---
### DisableSwitchOutroFx

`DISABLE_SWITCH_OUTRO_FX` · hash `0xBD605B8E0E18B3BB` · jhash `0x59CC312D` · **Cliente**

```lua
DisableSwitchOutroFx()
```
```c
void DISABLE_SWITCH_OUTRO_FX();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBD605B8E0E18B3BB` (`N_0xbd605b8e0e18b3bb`)

---
### DoesAnimDictExist

`DOES_ANIM_DICT_EXIST` · hash `0x2DA49C3B79856961` · jhash `0xCD31C872` · **Cliente**

```lua
local retval = DoesAnimDictExist(animDict)
```
```c
BOOL DOES_ANIM_DICT_EXIST(char* animDict);
```

**Parámetros**

- `animDict` (`char*`)

**Devuelve:** `BOOL`

---
### EnableSwitchPauseBeforeDescent

`ENABLE_SWITCH_PAUSE_BEFORE_DESCENT` · hash `0xD4793DFF3AF2ABCD` · jhash `0x4062FF73` · **Cliente**

```lua
EnableSwitchPauseBeforeDescent()
```
```c
void ENABLE_SWITCH_PAUSE_BEFORE_DESCENT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD4793DFF3AF2ABCD` (`N_0xd4793dff3af2abcd`)

---
### EndSrl

`END_SRL` · hash `0x0A41540E63C9EE17` · jhash `0x1977C56A` · **Cliente**

```lua
EndSrl()
```
```c
void END_SRL();
```

**Devuelve:** `void`

**Descripción oficial:**

Clear the current srl and stop rendering the area selected by PREFETCH_SRL and started with BEGIN_SRL.

---
### GetGlobalWaterType

`_GET_GLOBAL_WATER_TYPE` · hash `0xF741BD853611592D` · **Cliente**

```lua
local retval = GetGlobalWaterType()
```
```c
int _GET_GLOBAL_WATER_TYPE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### GetIdealPlayerSwitchType

`GET_IDEAL_PLAYER_SWITCH_TYPE` · hash `0xB5D7B26B45720E05` · jhash `0xD5A450F1` · **Cliente**

```lua
local retval = GetIdealPlayerSwitchType(x1, y1, z1, x2, y2, z2)
```
```c
int GET_IDEAL_PLAYER_SWITCH_TYPE(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `int`

**Descripción oficial:**

```
x1, y1, z1 -- Coords of your ped model  
x2, y2, z2 -- Coords of the ped you want to switch to  
```

---
### GetLodscale

`GET_LODSCALE` · hash `0x0C15B0E443B2349D` · jhash `0x7154B6FD` · **Cliente**

```lua
local retval = GetLodscale()
```
```c
float GET_LODSCALE();
```

**Devuelve:** `float`

**Nombres antiguos (alias):** `0x0C15B0E443B2349D` (`N_0x0c15b0e443b2349d`)

---
### GetNumberOfStreamingRequests

`GET_NUMBER_OF_STREAMING_REQUESTS` · hash `0x4060057271CEBC89` · jhash `0xC2EE9A02` · **Cliente**

```lua
local retval = GetNumberOfStreamingRequests()
```
```c
int GET_NUMBER_OF_STREAMING_REQUESTS();
```

**Devuelve:** `int`

---
### GetPlayerShortSwitchState

`GET_PLAYER_SHORT_SWITCH_STATE` · hash `0x20F898A5D9782800` · jhash `0x9B7BA38F` · **Cliente**

```lua
local retval = GetPlayerShortSwitchState()
```
```c
int GET_PLAYER_SHORT_SWITCH_STATE();
```

**Devuelve:** `int`

---
### GetPlayerSwitchInterpOutCurrentTime

`GET_PLAYER_SWITCH_INTERP_OUT_CURRENT_TIME` · hash `0x5B48A06DD0E792A5` · jhash `0xC7A3D279` · **Cliente**

```lua
local retval = GetPlayerSwitchInterpOutCurrentTime()
```
```c
Any GET_PLAYER_SWITCH_INTERP_OUT_CURRENT_TIME();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x5B48A06DD0E792A5` (`N_0x5b48a06dd0e792a5`)

---
### GetPlayerSwitchInterpOutDuration

`GET_PLAYER_SWITCH_INTERP_OUT_DURATION` · hash `0x08C2D6C52A3104BB` · jhash `0x569847E3` · **Cliente**

```lua
local retval = GetPlayerSwitchInterpOutDuration()
```
```c
int GET_PLAYER_SWITCH_INTERP_OUT_DURATION();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `SET_PLAYER_INVERTED_UP` (`SetPlayerInvertedUp`), `0x08C2D6C52A3104BB` (`N_0x08c2d6c52a3104bb`)

---
### GetPlayerSwitchJumpCutIndex

`GET_PLAYER_SWITCH_JUMP_CUT_INDEX` · hash `0x78C0D93253149435` · jhash `0x02BA7AC2` · **Cliente**

```lua
local retval = GetPlayerSwitchJumpCutIndex()
```
```c
int GET_PLAYER_SWITCH_JUMP_CUT_INDEX();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x78C0D93253149435` (`N_0x78c0d93253149435`)

---
### GetPlayerSwitchState

`GET_PLAYER_SWITCH_STATE` · hash `0x470555300D10B2A5` · jhash `0x39A0E1F2` · **Cliente**

```lua
local retval = GetPlayerSwitchState()
```
```c
int GET_PLAYER_SWITCH_STATE();
```

**Devuelve:** `int` — *   Returns 5 if the player is in the air (in a state of switch). *   Returns 12 if the player is either not in the air or if the switch is completed.

**Ejemplo (lua):**

```lua
local stateSwitch = GetPlayerSwitchState()
if stateSwitch == 5 then
    -- Player is in the air
    elseif stateSwitch == 12 then
    -- Player is not in the air or switch is completed
end
```

**Ejemplo (js):**

```js
const stateSwitch = GetPlayerSwitchState();
if (stateSwitch == 5) {
    // Player is in the air
} else if (stateSwitch == 12) {
    // Player is not in the air or switch is completed
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

int stateSwitch = GetPlayerSwitchState();
if (stateSwitch == 5) {
    // Player is in the air
} else if (stateSwitch == 12) {
    // Player is not in the air or switch is completed
}
```

---
### GetPlayerSwitchType

`GET_PLAYER_SWITCH_TYPE` · hash `0xB3C94A90D9FC9E62` · jhash `0x280DC015` · **Cliente**

```lua
local retval = GetPlayerSwitchType()
```
```c
int GET_PLAYER_SWITCH_TYPE();
```

**Devuelve:** `int`

---
### GetUsedCreatorModelMemoryPercentage

`_GET_USED_CREATOR_MODEL_MEMORY_PERCENTAGE` · hash `0x3D3D8B3BE5A83D35` · jhash `0x3E9C4CBE` · **Cliente**

```lua
local retval = GetUsedCreatorModelMemoryPercentage()
```
```c
float _GET_USED_CREATOR_MODEL_MEMORY_PERCENTAGE();
```

**Devuelve:** `float`

**Descripción oficial:**

```
0.0 = no memory used
1.0 = all memory used

Maximum model memory (as defined in common\data\missioncreatordata.meta) is 100 MiB

GET_*
```

**Nombres antiguos (alias):** `0x3D3D8B3BE5A83D35` (`N_0x3d3d8b3be5a83d35`)

---
### HasAnimDictLoaded

`HAS_ANIM_DICT_LOADED` · hash `0xD031A9162D01088C` · jhash `0x05E6763C` · **Cliente**

```lua
local retval = HasAnimDictLoaded(animDict)
```
```c
BOOL HAS_ANIM_DICT_LOADED(char* animDict);
```

**Parámetros**

- `animDict` (`char*`)

**Devuelve:** `BOOL`

---
### HasAnimSetLoaded

`HAS_ANIM_SET_LOADED` · hash `0xC4EA073D86FB29B0` · jhash `0x4FFF397D` · **Cliente**

```lua
local retval = HasAnimSetLoaded(animSet)
```
```c
BOOL HAS_ANIM_SET_LOADED(char* animSet);
```

**Parámetros**

- `animSet` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Gets whether the specified animation set has finished loading. An animation set provides movement animations for a ped.

Animation set and clip set are synonymous. See [`SET_PED_MOVEMENT_CLIPSET`](PED-1.md#setpedmovementclipset).

---
### HasClipSetLoaded

`HAS_CLIP_SET_LOADED` · hash `0x318234F4F3738AF3` · jhash `0x230D5455` · **Cliente**

```lua
local retval = HasClipSetLoaded(clipSet)
```
```c
BOOL HAS_CLIP_SET_LOADED(char* clipSet);
```

**Parámetros**

- `clipSet` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Alias for HAS_ANIM_SET_LOADED.  
```

---
### HasCollisionForModelLoaded

`HAS_COLLISION_FOR_MODEL_LOADED` · hash `0x22CCA434E368F03A` · jhash `0x41A094F8` · **Cliente**

```lua
local retval = HasCollisionForModelLoaded(model)
```
```c
BOOL HAS_COLLISION_FOR_MODEL_LOADED(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### HasModelLoaded

`HAS_MODEL_LOADED` · hash `0x98A4EB5D89A0C952` · jhash `0x62BFDB37` · **Cliente**

```lua
local retval = HasModelLoaded(model)
```
```c
BOOL HAS_MODEL_LOADED(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model hash to check for.

**Devuelve:** `BOOL` — A boolean indicating whether the archetype is loaded (true) or not (false).

**Descripción oficial:**

Returns whether the specified model (archetype) is currently loaded.

Note that this will return 'true' even if the model has been requested and loaded by something other than the current script, if you're intending to actually use the model in a later frame, you should call REQUEST_MODEL anyway.

---
### HasNamedPtfxAssetLoaded

`HAS_NAMED_PTFX_ASSET_LOADED` · hash `0x8702416E512EC454` · jhash `0x9ACC6446` · **Cliente**

```lua
local retval = HasNamedPtfxAssetLoaded(fxName)
```
```c
BOOL HAS_NAMED_PTFX_ASSET_LOADED(char* fxName);
```

**Parámetros**

- `fxName` (`char*`)

**Devuelve:** `BOOL`

---
### HasPtfxAssetLoaded

`HAS_PTFX_ASSET_LOADED` · hash `0xCA7D9B86ECA7481B` · jhash `0x3EFF96BE` · **Cliente**

```lua
local retval = HasPtfxAssetLoaded()
```
```c
BOOL HAS_PTFX_ASSET_LOADED();
```

**Devuelve:** `BOOL`

---
### InitCreatorBudget

`INIT_CREATOR_BUDGET` · hash `0xB5A4DB34FE89B88A` · jhash `0xE243B2AF` · **Cliente**

```lua
InitCreatorBudget()
```
```c
void INIT_CREATOR_BUDGET();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xB5A4DB34FE89B88A` (`N_0xb5a4db34fe89b88a`), `_LOAD_MISSION_CREATOR_DATA` (`LoadMissionCreatorData`)

---
### IsEntityFocus

`IS_ENTITY_FOCUS` · hash `0x2DDFF3FB9075D747` · jhash `0xB456D707` · **Cliente**

```lua
local retval = IsEntityFocus(entity)
```
```c
BOOL IS_ENTITY_FOCUS(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `BOOL`

---
### IsIplActive

`IS_IPL_ACTIVE` · hash `0x88A741E44A2B3495` · jhash `0xB2C33714` · **Cliente**

```lua
local retval = IsIplActive(iplName)
```
```c
BOOL IS_IPL_ACTIVE(char* iplName);
```

**Parámetros**

- `iplName` (`char*`)

**Devuelve:** `BOOL`

---
### IsModelAPed

`_IS_MODEL_A_PED` · hash `0x75816577FEA6DAD5` · **Cliente**

```lua
local retval = IsModelAPed(model)
```
```c
BOOL _IS_MODEL_A_PED(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

---
### IsModelAVehicle

`IS_MODEL_A_VEHICLE` · hash `0x19AAC8F07BFEC53E` · jhash `0xFFFC85D4` · **Cliente**

```lua
local retval = IsModelAVehicle(model)
```
```c
BOOL IS_MODEL_A_VEHICLE(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the specified model represents a vehicle.  
```

---
### IsModelInCdimage

`IS_MODEL_IN_CDIMAGE` · hash `0x35B9E0803292B641` · jhash `0x1094782F` · **Cliente**

```lua
local retval = IsModelInCdimage(model)
```
```c
BOOL IS_MODEL_IN_CDIMAGE(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Check if model is in cdimage(rpf)  
```

---
### IsModelValid

`IS_MODEL_VALID` · hash `0xC0296A2EDF545E92` · jhash `0xAF8F8E9D` · **Cliente**

```lua
local retval = IsModelValid(model)
```
```c
BOOL IS_MODEL_VALID(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether the specified model exists in the game.  
```

---
### IsNetworkLoadingScene

`IS_NETWORK_LOADING_SCENE` · hash `0x41CA5A33160EA4AB` · jhash `0x6DCFC021` · **Cliente**

```lua
local retval = IsNetworkLoadingScene()
```
```c
BOOL IS_NETWORK_LOADING_SCENE();
```

**Devuelve:** `BOOL`

---
### IsNewLoadSceneActive

`IS_NEW_LOAD_SCENE_ACTIVE` · hash `0xA41A05B6CB741B85` · jhash `0xAD234B7F` · **Cliente**

```lua
local retval = IsNewLoadSceneActive()
```
```c
BOOL IS_NEW_LOAD_SCENE_ACTIVE();
```

**Devuelve:** `BOOL`

---
### IsNewLoadSceneLoaded

`IS_NEW_LOAD_SCENE_LOADED` · hash `0x01B8247A7A8B9AD1` · jhash `0x3ECD839F` · **Cliente**

```lua
local retval = IsNewLoadSceneLoaded()
```
```c
BOOL IS_NEW_LOAD_SCENE_LOADED();
```

**Devuelve:** `BOOL`

---
### IsPlayerSwitchInProgress

`IS_PLAYER_SWITCH_IN_PROGRESS` · hash `0xD9D2CFFF49FAB35F` · jhash `0x56135ACC` · **Cliente**

```lua
local retval = IsPlayerSwitchInProgress()
```
```c
BOOL IS_PLAYER_SWITCH_IN_PROGRESS();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the player is currently switching, false otherwise.  
(When the camera is in the sky moving from Trevor to Franklin for example)  
```

**Nombres antiguos (alias):** `0xD9D2CFFF49FAB35F` (`N_0xd9d2cfff49fab35f`)

---
### IsSrlLoaded

`IS_SRL_LOADED` · hash `0xD0263801A4C5B0BB` · jhash `0x670FA2A6` · **Cliente**

```lua
local retval = IsSrlLoaded()
```
```c
BOOL IS_SRL_LOADED();
```

**Devuelve:** `BOOL` — *   A boolean once BeginSrl srl is loaded.

**Descripción oficial:**

Returns true when the srl from BEGIN_SRL is loaded.

---
### IsStreamvolActive

`IS_STREAMVOL_ACTIVE` · hash `0xBC9823AB80A3DCAC` · jhash `0x56253356` · **Cliente**

```lua
local retval = IsStreamvolActive()
```
```c
BOOL IS_STREAMVOL_ACTIVE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBC9823AB80A3DCAC` (`N_0xbc9823ab80a3dcac`)

---
### IsSwitchReadyForDescent

`IS_SWITCH_READY_FOR_DESCENT` · hash `0xDFA80CB25D0A19B3` · jhash `0x408F7148` · **Cliente**

```lua
local retval = IsSwitchReadyForDescent()
```
```c
BOOL IS_SWITCH_READY_FOR_DESCENT();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xDFA80CB25D0A19B3` (`N_0xdfa80cb25d0a19b3`)

---
### IsSwitchSkippingDescent

`IS_SWITCH_SKIPPING_DESCENT` · hash `0x5B74EA8CFD5E3E7E` · jhash `0x90F64284` · **Cliente**

```lua
local retval = IsSwitchSkippingDescent()
```
```c
BOOL IS_SWITCH_SKIPPING_DESCENT();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `DESTROY_PLAYER_IN_PAUSE_MENU` (`DestroyPlayerInPauseMenu`)

---
### LoadAllObjectsNow

`LOAD_ALL_OBJECTS_NOW` · hash `0xBD6E84632DD4CB3F` · jhash `0xC9DBDA90` · **Cliente**

```lua
LoadAllObjectsNow()
```
```c
void LOAD_ALL_OBJECTS_NOW();
```

**Devuelve:** `void`

---
### LoadGlobalWaterType

`_LOAD_GLOBAL_WATER_TYPE` · hash `0x7E3F55ED251B76D3` · **Cliente**

```lua
LoadGlobalWaterType(waterType)
```
```c
void _LOAD_GLOBAL_WATER_TYPE(int waterType);
```

**Parámetros**

- `waterType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

0 - default
1 - HeistIsland

```
NativeDB Introduced: v2189
```

---
### LoadScene

`LOAD_SCENE` · hash `0x4448EB75B4904BDB` · jhash `0xB72403F5` · **Cliente**

```lua
LoadScene(x, y, z)
```
```c
void LOAD_SCENE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### N_0x03f1a106bda7dd3e

`0x03F1A106BDA7DD3E` · hash `0x03F1A106BDA7DD3E` · **Cliente**

```lua
N_0x03f1a106bda7dd3e()
```
```c
void 0x03F1A106BDA7DD3E();
```

**Devuelve:** `void`

---
### N_0x0811381ef5062fec

`0x0811381EF5062FEC` · hash `0x0811381EF5062FEC` · **Cliente**

```lua
N_0x0811381ef5062fec(p0)
```
```c
void 0x0811381EF5062FEC(Entity p0);
```

**Parámetros**

- `p0` (`Entity`)

**Devuelve:** `void`

---
### N_0x1e9057a74fd73e23

`0x1E9057A74FD73E23` · hash `0x1E9057A74FD73E23` · **Cliente**

```lua
N_0x1e9057a74fd73e23()
```
```c
void 0x1E9057A74FD73E23();
```

**Devuelve:** `void`

---
### N_0x20c6c7e4eb082a7f

`0x20C6C7E4EB082A7F` · hash `0x20C6C7E4EB082A7F` · jhash `0xA6459CAA` · **Cliente**

```lua
N_0x20c6c7e4eb082a7f(p0)
```
```c
void 0x20C6C7E4EB082A7F(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### N_0x472397322e92a856

`0x472397322E92A856` · hash `0x472397322E92A856` · jhash `0x4267DA87` · **Cliente**

```lua
N_0x472397322e92a856()
```
```c
void 0x472397322E92A856();
```

**Devuelve:** `void`

---
### N_0x4e52e752c76e7e7a

`0x4E52E752C76E7E7A` · hash `0x4E52E752C76E7E7A` · jhash `0xA07BAEB9` · **Cliente**

```lua
N_0x4e52e752c76e7e7a(p0)
```
```c
void 0x4E52E752C76E7E7A(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

---
### N_0x5068f488ddb54dd8

`0x5068F488DDB54DD8` · hash `0x5068F488DDB54DD8` · jhash `0xDAB4BAC0` · **Cliente**

```lua
local retval = N_0x5068f488ddb54dd8()
```
```c
Any 0x5068F488DDB54DD8();
```

**Devuelve:** `Any`

---
### N_0x63eb2b972a218cac

`0x63EB2B972A218CAC` · hash `0x63EB2B972A218CAC` · jhash `0xF2CDD6A8` · **Cliente**

```lua
N_0x63eb2b972a218cac()
```
```c
void 0x63EB2B972A218CAC();
```

**Devuelve:** `void`

---
### N_0x71e7b2e657449aad

`0x71E7B2E657449AAD` · hash `0x71E7B2E657449AAD` · jhash `0xEAA51103` · **Cliente**

```lua
local retval = N_0x71e7b2e657449aad()
```
```c
Any 0x71E7B2E657449AAD();
```

**Devuelve:** `Any`

---
### N_0x933bbeeb8c61b5f4

`0x933BBEEB8C61B5F4` · hash `0x933BBEEB8C61B5F4` · jhash `0x74C16879` · **Cliente**

```lua
local retval = N_0x933bbeeb8c61b5f4()
```
```c
BOOL 0x933BBEEB8C61B5F4();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Probably IS_SWITCH_*
```

---
### N_0x95a7dabddbb78ae7

`0x95A7DABDDBB78AE7` · hash `0x95A7DABDDBB78AE7` · jhash `0x9EF0A9CF` · **Cliente**

```lua
N_0x95a7dabddbb78ae7(iplName1, iplName2)
```
```c
void 0x95A7DABDDBB78AE7(char* iplName1, char* iplName2);
```

**Parámetros**

- `iplName1` (`char*`)
- `iplName2` (`char*`)

**Devuelve:** `void`

---
### N_0xbeb2d9a1d9a8f55a

`0xBEB2D9A1D9A8F55A` · hash `0xBEB2D9A1D9A8F55A` · jhash `0x62F02485` · **Cliente**

```lua
N_0xbeb2d9a1d9a8f55a(p0, p1, p2, p3)
```
```c
void 0xBEB2D9A1D9A8F55A(Any p0, Any p1, Any p2, Any p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)

**Devuelve:** `void`

---
### N_0xbed8ca5ff5e04113

`0xBED8CA5FF5E04113` · hash `0xBED8CA5FF5E04113` · jhash `0x9CD6A451` · **Cliente**

```lua
N_0xbed8ca5ff5e04113(p0, p1, p2, p3)
```
```c
void 0xBED8CA5FF5E04113(float p0, float p1, float p2, float p3);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)

**Devuelve:** `void`

---
### N_0xef39ee20c537e98c

`0xEF39EE20C537E98C` · hash `0xEF39EE20C537E98C` · jhash `0x814D0752` · **Cliente**

```lua
N_0xef39ee20c537e98c(p0, p1, p2, p3, p4, p5)
```
```c
void 0xEF39EE20C537E98C(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
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
### N_0xf4a0dadb70f57fa6

`0xF4A0DADB70F57FA6` · hash `0xF4A0DADB70F57FA6` · jhash `0x3DA7AA5D` · **Cliente**

```lua
N_0xf4a0dadb70f57fa6()
```
```c
void 0xF4A0DADB70F57FA6();
```

**Devuelve:** `void`

---
### N_0xf8155a7f03ddfc8e

`0xF8155A7F03DDFC8E` · hash `0xF8155A7F03DDFC8E` · jhash `0xF8F515E4` · **Cliente**

```lua
N_0xf8155a7f03ddfc8e(p0)
```
```c
void 0xF8155A7F03DDFC8E(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### N_0xfb199266061f820a

`0xFB199266061F820A` · hash `0xFB199266061F820A` · jhash `0x17B0A1CD` · **Cliente**

```lua
local retval = N_0xfb199266061f820a()
```
```c
BOOL 0xFB199266061F820A();
```

**Devuelve:** `BOOL`

---
### NetworkStopLoadScene

`NETWORK_STOP_LOAD_SCENE` · hash `0x64E630FAF5F60F44` · jhash `0x24857907` · **Cliente**

```lua
NetworkStopLoadScene()
```
```c
void NETWORK_STOP_LOAD_SCENE();
```

**Devuelve:** `void`

---
### NetworkUpdateLoadScene

`NETWORK_UPDATE_LOAD_SCENE` · hash `0xC4582015556D1C46` · jhash `0xC76E023C` · **Cliente**

```lua
local retval = NetworkUpdateLoadScene()
```
```c
BOOL NETWORK_UPDATE_LOAD_SCENE();
```

**Devuelve:** `BOOL`

---
### NewLoadSceneStart

`NEW_LOAD_SCENE_START` · hash `0x212A8D0D2BABFAC2` · jhash `0xDF9C38B6` · **Cliente**

```lua
local retval = NewLoadSceneStart(posX, posY, posZ, offsetX, offsetY, offsetZ, radius, p7)
```
```c
BOOL NEW_LOAD_SCENE_START(float posX, float posY, float posZ, float offsetX, float offsetY, float offsetZ, float radius, int p7);
```

**Parámetros**

- `posX` (`float`): World `x` coordinate.
- `posY` (`float`): World `y` coordinate.
- `posZ` (`float`): World `z` coordinate.
- `offsetX` (`float`): Offset `x` coordinate.
- `offsetY` (`float`): Offset `y` coordinate.
- `offsetZ` (`float`): Offset `z` coordinate.
- `radius` (`float`): Action radius, value is usually between `3f` and `7000f` in original 1868 scripts.
- `p7` (`int`): 0, 1, 2, 3 or 4 used in decompiled scripts, 0 is by far the most common.

**Devuelve:** `BOOL` — True if success, used only 7 times in decompiled scripts of 1868 (https://github.com/root-cause/v-decompiled-scripts).

**Descripción oficial:**

```
`radius` value is usually between `3f` and `7000f` in original 1868 scripts.
`p7` is 0, 1, 2, 3 or 4 used in decompiled scripts, 0 is by far the most common.
Returns True if success, used only 7 times in decompiled scripts of 1868
```

**Ejemplo (lua):**

```lua
function func_8(vParam0)
    return (-(Sin(vParam0.z)) * Cos(vParam0.x)), (Cos(vParam0.z) * Cos(vParam0.x)), Sin(vParam0.x)
end

Citizen.CreateThread(function()
    local vLocal_43 = vector3(1691.228, 3251.785, 44.2574)
    local vLocal_44 = vector3(2.5652, 0, -4.1481)

    if NewLoadSceneStart(vLocal_43.x, vLocal_43.y, vLocal_43.z, func_8(vLocal_44), 4500.0, 0)) then
          SetPlayerControl(PlayerId(), false, 0)
          local gameTimer = GetGameTimer()

          while not IsNewLoadSceneLoaded() and (GetGameTimer() - gameTimer < 20) do
              Citizen.Wait(0)
          end

          NewLoadSceneStop()
          SetFocusPosAndVel(vLocal_43.x, vLocal_43.y, vLocal_43.z, func_8(vLocal_44))
    end
end)
```

---
### NewLoadSceneStartSphere

`NEW_LOAD_SCENE_START_SPHERE` · hash `0xACCFB4ACF53551B0` · jhash `0xFA037FEB` · **Cliente**

```lua
local retval = NewLoadSceneStartSphere(x, y, z, radius, p4)
```
```c
BOOL NEW_LOAD_SCENE_START_SPHERE(float x, float y, float z, float radius, Any p4);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p4` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
if (!sub_8f12("START LOAD SCENE SAFE")) {
    if (CUTSCENE::GET_CUTSCENE_TIME() > 4178) {
        STREAMING::_ACCFB4ACF53551B0(1973.845458984375, 3818.447265625, 32.43629837036133, 15.0, 2);
        sub_8e9e("START LOAD SCENE SAFE", 1);
    }
}
(Previously known as STREAMING::_NEW_LOAD_SCENE_START_SAFE)
```

**Nombres antiguos (alias):** `0xACCFB4ACF53551B0` (`N_0xaccfb4acf53551b0`)

---
### NewLoadSceneStop

`NEW_LOAD_SCENE_STOP` · hash `0xC197616D221FF4A4` · jhash `0x7C05B1F6` · **Cliente**

```lua
NewLoadSceneStop()
```
```c
void NEW_LOAD_SCENE_STOP();
```

**Devuelve:** `void`

---
### OverrideLodscaleThisFrame

`OVERRIDE_LODSCALE_THIS_FRAME` · hash `0xA76359FC80B2438E` · jhash `0xE5612C1A` · **Cliente**

```lua
OverrideLodscaleThisFrame(scaling)
```
```c
void OVERRIDE_LODSCALE_THIS_FRAME(float scaling);
```

**Parámetros**

- `scaling` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
This allows you to override "extended distance scaling" setting. Needs to be called each frame.
Max scaling seems to be 200.0, normal is 1.0
See https://gfycat.com/DetailedHauntingIncatern
```

**Nombres antiguos (alias):** `0xA76359FC80B2438E` (`N_0xa76359fc80b2438e`)

---
### PrefetchSrl

`PREFETCH_SRL` · hash `0x3D245789CE12982C` · jhash `0x37BE2FBB` · **Cliente**

```lua
PrefetchSrl(srl)
```
```c
void PREFETCH_SRL(char* srl);
```

**Parámetros**

- `srl` (`char*`): A SRL name.

**Devuelve:** `void`

**Descripción oficial:**

This native is used to attribute the SRL that BeginSrl is going to load. This is usually used for 'in-game' cinematics (not cutscenes but camera stuff) instead of SetFocusArea because it loads a specific area of the map which is pretty useful when the camera moves from distant areas.
For instance, GTA:O opening cutscene.

https://pastebin.com/2EeKVeLA : a list of SRL found in srllist.meta
https://pastebin.com/zd9XYUWY : here is the content of a SRL file opened with codewalker.

**Ejemplo (lua):**

```lua
PrefetchSrl('GTAO_INTRO_MALE')
while not IsSrlLoaded() do
	Citizen.Wait(100)
end
BeginSrl()
```

---
### RemoveAnimDict

`REMOVE_ANIM_DICT` · hash `0xF66A602F829E2A06` · jhash `0x0AE050B5` · **Cliente**

```lua
RemoveAnimDict(animDict)
```
```c
void REMOVE_ANIM_DICT(char* animDict);
```

**Parámetros**

- `animDict` (`char*`)

**Devuelve:** `void`

---
### RemoveAnimSet

`REMOVE_ANIM_SET` · hash `0x16350528F93024B3` · jhash `0xD04A817A` · **Cliente**

```lua
RemoveAnimSet(animSet)
```
```c
void REMOVE_ANIM_SET(char* animSet);
```

**Parámetros**

- `animSet` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Unloads the specified animation set. An animation set provides movement animations for a ped.

Animation set and clip set are synonymous. See [`SET_PED_MOVEMENT_CLIPSET`](PED-1.md#setpedmovementclipset).

---
### RemoveClipSet

`REMOVE_CLIP_SET` · hash `0x01F73A131C18CD94` · jhash `0x1E21F7AA` · **Cliente**

```lua
RemoveClipSet(clipSet)
```
```c
void REMOVE_CLIP_SET(char* clipSet);
```

**Parámetros**

- `clipSet` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Alias for REMOVE_ANIM_SET.  
```

---
### RemoveIpl

`REMOVE_IPL` · hash `0xEE6C5AD3ECE0A82D` · jhash `0xDF7CBD36` · **Cliente**

```lua
RemoveIpl(iplName)
```
```c
void REMOVE_IPL(char* iplName);
```

**Parámetros**

- `iplName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

IPL list can be found [here](https://gist.github.com/4mmonium/4c8a076b5f712a7cc64666003009a2e7).

---
### RemoveModelFromCreatorBudget

`REMOVE_MODEL_FROM_CREATOR_BUDGET` · hash `0xF086AD9354FAC3A3` · jhash `0x1C576388` · **Cliente**

```lua
RemoveModelFromCreatorBudget(modelHash)
```
```c
void REMOVE_MODEL_FROM_CREATOR_BUDGET(Hash modelHash);
```

**Parámetros**

- `modelHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF086AD9354FAC3A3` (`N_0xf086ad9354fac3a3`)

---
### RemoveNamedPtfxAsset

`REMOVE_NAMED_PTFX_ASSET` · hash `0x5F61EBBE1A00F96D` · jhash `0xC44762A1` · **Cliente**

```lua
RemoveNamedPtfxAsset(fxName)
```
```c
void REMOVE_NAMED_PTFX_ASSET(char* fxName);
```

**Parámetros**

- `fxName` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_REMOVE_NAMED_PTFX_ASSET` (`RemoveNamedPtfxAsset`)

---
### RemovePtfxAsset

`REMOVE_PTFX_ASSET` · hash `0x88C6814073DD4A73` · jhash `0xC10F178C` · **Cliente**

```lua
RemovePtfxAsset()
```
```c
void REMOVE_PTFX_ASSET();
```

**Devuelve:** `void`

---
### RequestAdditionalCollisionAtCoord

`REQUEST_ADDITIONAL_COLLISION_AT_COORD` · hash `0xC9156DC11411A9EA` · jhash `0xC2CC1DF2` · **Cliente**

```lua
RequestAdditionalCollisionAtCoord(x, y, z)
```
```c
void REQUEST_ADDITIONAL_COLLISION_AT_COORD(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### RequestAnimDict

`REQUEST_ANIM_DICT` · hash `0xD3BD40951412FEF6` · jhash `0xDCA96950` · **Cliente**

```lua
RequestAnimDict(animDict)
```
```c
void REQUEST_ANIM_DICT(char* animDict);
```

**Parámetros**

- `animDict` (`char*`)

**Devuelve:** `void`

---
### RequestAnimSet

`REQUEST_ANIM_SET` · hash `0x6EA47DAE7FAD0EED` · jhash `0x2988B3FC` · **Cliente**

```lua
RequestAnimSet(animSet)
```
```c
void REQUEST_ANIM_SET(char* animSet);
```

**Parámetros**

- `animSet` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Starts loading the specified animation set. An animation set provides movement animations for a ped. See [`SET_PED_MOVEMENT_CLIPSET`](PED-1.md#setpedmovementclipset).

---
### RequestClipSet

`REQUEST_CLIP_SET` · hash `0xD2A71E1A77418A49` · jhash `0x546C627A` · **Cliente**

```lua
RequestClipSet(clipSet)
```
```c
void REQUEST_CLIP_SET(char* clipSet);
```

**Parámetros**

- `clipSet` (`char*`)

**Devuelve:** `void`

---
### RequestCollisionAtCoord

`REQUEST_COLLISION_AT_COORD` · hash `0x07503F7948F491A7` · jhash `0xCD9805E7` · **Cliente**

```lua
RequestCollisionAtCoord(x, y, z)
```
```c
void REQUEST_COLLISION_AT_COORD(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `void`

---
### RequestCollisionForModel

`REQUEST_COLLISION_FOR_MODEL` · hash `0x923CB32A3B874FCB` · jhash `0x3930C042` · **Cliente**

```lua
RequestCollisionForModel(model)
```
```c
void REQUEST_COLLISION_FOR_MODEL(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### RequestIpl

`REQUEST_IPL` · hash `0x41B4893843BBDB74` · jhash `0x3B70D1DB` · **Cliente**

```lua
RequestIpl(iplName)
```
```c
void REQUEST_IPL(char* iplName);
```

**Parámetros**

- `iplName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Exemple: REQUEST_IPL("TrevorsTrailerTrash");
```

---
### RequestMenuPedModel

`REQUEST_MENU_PED_MODEL` · hash `0xA0261AEF7ACFC51E` · jhash `0x48CEB6B4` · **Cliente**

```lua
RequestMenuPedModel(model)
```
```c
void REQUEST_MENU_PED_MODEL(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to request.

**Devuelve:** `void`

**Descripción oficial:**

Calls [`REQUEST_MODEL`](#requestmodel) with the `STRFLAG_PRIORITY_LOAD` and `STRFLAG_FORCE_LOAD` set.

**Nombres antiguos (alias):** `0xA0261AEF7ACFC51E` (`N_0xa0261aef7acfc51e`)

---
### RequestModel

`REQUEST_MODEL` · hash `0x963D27A58DF860AC` · jhash `0xFFF1B500` · **Cliente**

```lua
RequestModel(model)
```
```c
void REQUEST_MODEL(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to request.

**Devuelve:** `void`

**Descripción oficial:**

Request a model (archetype) to be loaded for use by the current script. Use SET_MODEL_AS_NO_LONGER_NEEDED when done using the model in script.

**Ejemplo (lua):**

```lua
local modelHash = `adder`
RequestModel(modelHash)
while not HasModelLoaded(modelHash) do
  Wait(0)
end

-- omitted: creating a vehicle

-- when done using the model
SetModelAsNoLongerNeeded(modelHash)
```

---
### RequestModelsInRoom

`REQUEST_MODELS_IN_ROOM` · hash `0x8A7A40100EDFEC58` · jhash `0x939243FB` · **Cliente**

```lua
RequestModelsInRoom(interior, roomName)
```
```c
void REQUEST_MODELS_IN_ROOM(int interior, char* roomName);
```

**Parámetros**

- `interior` (`int`)
- `roomName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
STREAMING::REQUEST_MODELS_IN_ROOM(l_13BC, "V_FIB01_cur_elev");
STREAMING::REQUEST_MODELS_IN_ROOM(l_13BC, "limbo");
STREAMING::REQUEST_MODELS_IN_ROOM(l_13BB, "V_Office_gnd_lifts");
STREAMING::REQUEST_MODELS_IN_ROOM(l_13BB, "limbo");
STREAMING::REQUEST_MODELS_IN_ROOM(l_13BC, "v_fib01_jan_elev");
STREAMING::REQUEST_MODELS_IN_ROOM(l_13BC, "limbo");
```

**Nombres antiguos (alias):** `0x8A7A40100EDFEC58` (`N_0x8a7a40100edfec58`), `_REQUEST_INTERIOR_ROOM_BY_NAME` (`RequestInteriorRoomByName`)

---
### RequestNamedPtfxAsset

`REQUEST_NAMED_PTFX_ASSET` · hash `0xB80D8756B4668AB6` · jhash `0xCFEA19A9` · **Cliente**

```lua
RequestNamedPtfxAsset(fxName)
```
```c
void REQUEST_NAMED_PTFX_ASSET(char* fxName);
```

**Parámetros**

- `fxName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
 From the b678d decompiled scripts:
 STREAMING::REQUEST_NAMED_PTFX_ASSET("core_snow");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("fm_mission_controler");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("proj_xmas_firework");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_apartment_mp");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_biolab_heist");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_indep_fireworks");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_indep_parachute");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_indep_wheelsmoke");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_mp_cig_plane");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_mp_creator");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_mp_tankbattle");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_ornate_heist");
 STREAMING::REQUEST_NAMED_PTFX_ASSET("scr_prison_break_heist_station");
```

---
### RequestPtfxAsset

`REQUEST_PTFX_ASSET` · hash `0x944955FB2A3935C8` · jhash `0x2C649263` · **Cliente**

```lua
RequestPtfxAsset()
```
```c
void REQUEST_PTFX_ASSET();
```

**Devuelve:** `void`

**Descripción oficial:**

```
maps script name (thread + 0xD0) by lookup via scriptfx.dat - does nothing when script name is empty
```

---
### SetDitchPoliceModels

`SET_DITCH_POLICE_MODELS` · hash `0x42CBE54462D92634` · jhash `0x3EA7FCE4` · **Cliente**

```lua
SetDitchPoliceModels(toggle)
```
```c
void SET_DITCH_POLICE_MODELS(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
This is a NOP function. It does nothing at all.  
```

---
### SetFocusEntity

`SET_FOCUS_ENTITY` · hash `0x198F77705FA0931D` · jhash `0x18DB04AC` · **Cliente**

```lua
SetFocusEntity(entity)
```
```c
void SET_FOCUS_ENTITY(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

```
It seems to make the entity's coords mark the point from which LOD-distances are measured. In my testing, setting a vehicle as the focus entity and moving that vehicle more than 300 distance units away from the player will make the level of detail around the player go down drastically (shadows disappear, textures go extremely low res, etc). The player seems to be the default focus entity.  
```

---
### SetFocusPosAndVel

`SET_FOCUS_POS_AND_VEL` · hash `0xBB7454BAFF08FE25` · jhash `0x14680A60` · **Cliente**

```lua
SetFocusPosAndVel(x, y, z, offsetX, offsetY, offsetZ)
```
```c
void SET_FOCUS_POS_AND_VEL(float x, float y, float z, float offsetX, float offsetY, float offsetZ);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `offsetX` (`float`)
- `offsetY` (`float`)
- `offsetZ` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
Override the area where the camera will render the terrain.
p3, p4 and p5 are usually set to 0.0
```

**Nombres antiguos (alias):** `_SET_FOCUS_AREA` (`SetFocusArea`)

---
### SetGamePausesForStreaming

`SET_GAME_PAUSES_FOR_STREAMING` · hash `0x717CD6E6FAEBBEDC` · jhash `0x9211A28A` · **Cliente**

```lua
SetGamePausesForStreaming(toggle)
```
```c
void SET_GAME_PAUSES_FOR_STREAMING(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetHdArea

`SET_HD_AREA` · hash `0xB85F26619073E775` · jhash `0x80BAA035` · **Cliente**

```lua
SetHdArea(x, y, z, radius)
```
```c
void SET_HD_AREA(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

---
### SetInteriorActive

`SET_INTERIOR_ACTIVE` · hash `0xE37B76C387BE28ED` · jhash `0xE1013910` · **Cliente**

```lua
SetInteriorActive(interiorID, toggle)
```
```c
void SET_INTERIOR_ACTIVE(int interiorID, BOOL toggle);
```

**Parámetros**

- `interiorID` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetIslandEnabled

`SET_ISLAND_ENABLED` · hash `0x9A9D1BA639675CF1` · **Cliente**

```lua
SetIslandEnabled(islandName, toggle)
```
```c
void SET_ISLAND_ENABLED(char* islandName, BOOL toggle);
```

**Parámetros**

- `islandName` (`char*`): The name of the island to be enabled or disabled.
- `toggle` (`BOOL`): A boolean value where `true` enables the island and `false` disables it.

**Devuelve:** `void`

**Descripción oficial:**

Enables the specified island. For more information, see islandhopper.meta

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `_SET_ISLAND_HOPPER_ENABLED` (`SetIslandHopperEnabled`)

---
### SetMapdatacullboxEnabled

`SET_MAPDATACULLBOX_ENABLED` · hash `0xAF12610C644A35C9` · jhash `0x403CD434` · **Cliente**

```lua
SetMapdatacullboxEnabled(name, toggle)
```
```c
void SET_MAPDATACULLBOX_ENABLED(char* name, BOOL toggle);
```

**Parámetros**

- `name` (`char*`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Possible p0 values:  
"prologue"  
"Prologue_Main"  
```

**Nombres antiguos (alias):** `0xAF12610C644A35C9` (`N_0xaf12610c644a35c9`)

---
### SetModelAsNoLongerNeeded

`SET_MODEL_AS_NO_LONGER_NEEDED` · hash `0xE532F5D78798DAAB` · jhash `0xAE0F069E` · **Cliente**

```lua
SetModelAsNoLongerNeeded(model)
```
```c
void SET_MODEL_AS_NO_LONGER_NEEDED(Hash model);
```

**Parámetros**

- `model` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: The model to release ownership of.

**Devuelve:** `void`

**Descripción oficial:**

Releases the script ownership assigned by REQUEST_MODEL. This command should be used when done using a specific model hash in script.

---
### SetPedPopulationBudget

`SET_PED_POPULATION_BUDGET` · hash `0x8C95333CFC3340F3` · jhash `0xD2D026CD` · **Cliente**

```lua
SetPedPopulationBudget(budgetLevel)
```
```c
void SET_PED_POPULATION_BUDGET(int budgetLevel);
```

**Parámetros**

- `budgetLevel` (`int`): Ranges from `0` to `3`, where `0` is lowest (no peds) and `3` is the full budget level.

**Devuelve:** `void`

**Descripción oficial:**

Sets the memory budget level for ped population.

---
### SetPlayerShortSwitchStyle

`SET_PLAYER_SHORT_SWITCH_STYLE` · hash `0x5F2013F8BC24EE69` · jhash `0xF0BD420D` · **Cliente**

```lua
SetPlayerShortSwitchStyle(style)
```
```c
void SET_PLAYER_SHORT_SWITCH_STYLE(int style);
```

**Parámetros**

- `style` (`int`): Always 0

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5F2013F8BC24EE69` (`N_0x5f2013f8bc24ee69`)

---
### SetPlayerSwitchEstablishingShot

`SET_PLAYER_SWITCH_ESTABLISHING_SHOT` · hash `0x0FDE9DBFC0A6BC65` · jhash `0x279077B0` · **Cliente**

```lua
SetPlayerSwitchEstablishingShot(name)
```
```c
void SET_PLAYER_SWITCH_ESTABLISHING_SHOT(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
All names can be found in playerswitchestablishingshots.meta
```

**Nombres antiguos (alias):** `0x0FDE9DBFC0A6BC65` (`N_0x0fde9dbfc0a6bc65`)

---
### SetPlayerSwitchOutro

`SET_PLAYER_SWITCH_OUTRO` · hash `0xC208B673CE446B61` · jhash `0x47352E14` · **Cliente**

```lua
SetPlayerSwitchOutro(cameraCoordX, cameraCoordY, cameraCoordZ, camRotationX, camRotationY, camRotationZ, camFov, camFarClip, rotationOrder)
```
```c
void SET_PLAYER_SWITCH_OUTRO(float cameraCoordX, float cameraCoordY, float cameraCoordZ, float camRotationX, float camRotationY, float camRotationZ, float camFov, float camFarClip, int rotationOrder);
```

**Parámetros**

- `cameraCoordX` (`float`)
- `cameraCoordY` (`float`)
- `cameraCoordZ` (`float`)
- `camRotationX` (`float`)
- `camRotationY` (`float`)
- `camRotationZ` (`float`)
- `camFov` (`float`)
- `camFarClip` (`float`)
- `rotationOrder` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC208B673CE446B61` (`N_0xc208b673ce446b61`)

---
### SetReducePedModelBudget

`SET_REDUCE_PED_MODEL_BUDGET` · hash `0x77B5F9A36BF96710` · jhash `0xAFCB2B86` · **Cliente**

```lua
SetReducePedModelBudget(toggle)
```
```c
void SET_REDUCE_PED_MODEL_BUDGET(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetReduceVehicleModelBudget

`SET_REDUCE_VEHICLE_MODEL_BUDGET` · hash `0x80C527893080CCF3` · jhash `0xCDB4FB7E` · **Cliente**

```lua
SetReduceVehicleModelBudget(toggle)
```
```c
void SET_REDUCE_VEHICLE_MODEL_BUDGET(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetRenderHdOnly

`SET_RENDER_HD_ONLY` · hash `0x40AEFD1A244741F2` · jhash `0x9FA4AF99` · **Cliente**

```lua
SetRenderHdOnly(toggle)
```
```c
void SET_RENDER_HD_ONLY(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x40AEFD1A244741F2` (`N_0x40aefd1a244741f2`)

---
### SetSrlTime

`SET_SRL_TIME` · hash `0xA74A541C6884E7B8` · jhash `0x30F8A487` · **Cliente**

```lua
SetSrlTime(p0)
```
```c
void SET_SRL_TIME(float p0);
```

**Parámetros**

- `p0` (`float`)

**Devuelve:** `void`

---
### SetStreaming

`SET_STREAMING` · hash `0x6E0C692677008888` · jhash `0x27EF6CB2` · **Cliente**

```lua
SetStreaming(toggle)
```
```c
void SET_STREAMING(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetVehiclePopulationBudget

`SET_VEHICLE_POPULATION_BUDGET` · hash `0xCB9E1EB3BE2AF4E9` · jhash `0x1D56993C` · **Cliente**

```lua
SetVehiclePopulationBudget(p0)
```
```c
void SET_VEHICLE_POPULATION_BUDGET(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### ShutdownCreatorBudget

`SHUTDOWN_CREATOR_BUDGET` · hash `0xCCE26000E9A6FAD7` · jhash `0x897A510F` · **Cliente**

```lua
ShutdownCreatorBudget()
```
```c
void SHUTDOWN_CREATOR_BUDGET();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCCE26000E9A6FAD7` (`N_0xcce26000e9a6fad7`)

---
### StartPlayerSwitch

`START_PLAYER_SWITCH` · hash `0xFAA23F2CBA159D67` · jhash `0x0829E975` · **Cliente**

```lua
StartPlayerSwitch(from, to, flags, switchType)
```
```c
void START_PLAYER_SWITCH(Ped from, Ped to, int flags, int switchType);
```

**Parámetros**

- `from` (`Ped`)
- `to` (`Ped`)
- `flags` (`int`): Refer to `eSwitchFlags`
- `switchType` (`int`): Refer to `ePlayerSwitchType`

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum ePlayerSwitchType  
{  
	SWITCH_TYPE_AUTO = 0,
	SWITCH_TYPE_LONG = 1,
	SWITCH_TYPE_MEDIUM = 2,
	SWITCH_TYPE_SHORT = 3
};  
```

```cpp
enum eSwitchFlags {
	SKIP_INTRO = 1,
	SKIP_OUTRO = 2,
	PAUSE_BEFORE_PAN = 4,
	PAUSE_BEFORE_OUTRO = 8,
	SKIP_PAN = 16,
	UNKNOWN_DEST = 32,
	DESCENT_ONLY = 64,
	START_FROM_CAMPOS = 128,
	PAUSE_BEFORE_ASCENT = 256,
	PAUSE_BEFORE_DESCENT = 512,
	ALLOW_SNIPER_AIM_INTRO = 1024,
	ALLOW_SNIPER_AIM_OUTRO = 2048,
	SKIP_TOP_DESCENT = 4096,
	SUPPRESS_OUTRO_FX = 8192,
	SUPPRESS_INTRO_FX = 16384,
	DELAY_ASCENT_FX = 32768
}
```

---
### StopPlayerSwitch

`STOP_PLAYER_SWITCH` · hash `0x95C0A5BBDC189AA1` · jhash `0x2832C010` · **Cliente**

```lua
StopPlayerSwitch()
```
```c
void STOP_PLAYER_SWITCH();
```

**Devuelve:** `void`

---
### StreamvolCreateFrustum

`STREAMVOL_CREATE_FRUSTUM` · hash `0x1F3F018BC3AFA77C` · jhash `0x72344191` · **Cliente**

```lua
local retval = StreamvolCreateFrustum(p0, p1, p2, p3, p4, p5, p6, p7, p8)
```
```c
Any STREAMVOL_CREATE_FRUSTUM(float p0, float p1, float p2, float p3, float p4, float p5, float p6, Any p7, Any p8);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`float`)
- `p7` (`Any`)
- `p8` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Always returns zero.
```

**Nombres antiguos (alias):** `0x1F3F018BC3AFA77C` (`N_0x1f3f018bc3afa77c`)

---
### StreamvolCreateLine

`STREAMVOL_CREATE_LINE` · hash `0x0AD9710CEE2F590F` · jhash `0xC0157255` · **Cliente**

```lua
local retval = StreamvolCreateLine(p0, p1, p2, p3, p4, p5, p6)
```
```c
Any STREAMVOL_CREATE_LINE(float p0, float p1, float p2, float p3, float p4, float p5, Any p6);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)
- `p6` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Always returns zero.
```

**Nombres antiguos (alias):** `0x0AD9710CEE2F590F` (`N_0x0ad9710cee2f590f`)

---
### StreamvolCreateSphere

`STREAMVOL_CREATE_SPHERE` · hash `0x219C7B8D53E429FD` · jhash `0x10B6AB36` · **Cliente**

```lua
local retval = StreamvolCreateSphere(x, y, z, rad, p4, p5)
```
```c
Any STREAMVOL_CREATE_SPHERE(float x, float y, float z, float rad, Any p4, Any p5);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `rad` (`float`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
Always returns zero.
```

**Nombres antiguos (alias):** `0x219C7B8D53E429FD` (`N_0x219c7b8d53e429fd`), `FORMAT_FOCUS_HEADING` (`FormatFocusHeading`)

---
### StreamvolDelete

`STREAMVOL_DELETE` · hash `0x1EE7D8DF4425F053` · jhash `0xE80F8ABE` · **Cliente**

```lua
StreamvolDelete(unused)
```
```c
void STREAMVOL_DELETE(Any unused);
```

**Parámetros**

- `unused` (`Any`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x1EE7D8DF4425F053` (`N_0x1ee7d8df4425f053`)

---
### StreamvolHasLoaded

`STREAMVOL_HAS_LOADED` · hash `0x7D41E9D2D17C5B2D` · jhash `0x1B3521F4` · **Cliente**

```lua
local retval = StreamvolHasLoaded(unused)
```
```c
BOOL STREAMVOL_HAS_LOADED(Any unused);
```

**Parámetros**

- `unused` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x7D41E9D2D17C5B2D` (`N_0x7d41e9d2d17c5b2d`)

---
### StreamvolIsValid

`STREAMVOL_IS_VALID` · hash `0x07C313F94746702C` · jhash `0x42CFE9C0` · **Cliente**

```lua
local retval = StreamvolIsValid(unused)
```
```c
BOOL STREAMVOL_IS_VALID(Any unused);
```

**Parámetros**

- `unused` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x07C313F94746702C` (`N_0x07c313f94746702c`)

---
### SwitchToMultiFirstpart

`SWITCH_TO_MULTI_FIRSTPART` · hash `0xAAB3200ED59016BC` · jhash `0xFB4D062D` · **Cliente**

```lua
SwitchToMultiFirstpart(ped, flags, switchType)
```
```c
void SWITCH_TO_MULTI_FIRSTPART(Ped ped, int flags, int switchType);
```

**Parámetros**

- `ped` (`Ped`): The Ped (player character) for which the switch is initiated.
- `flags` (`int`): Flags control various functionalities: 0 for normal behavior, 1 for no transition, and 255 for Switch IN.
- `switchType` (`int`): Specifies the type of switch (0 - 3): 0 for 1 step towards ped, 1 for 3 steps out from ped, 2 for 1 step out from ped, and 3 for 1 step towards ped.

**Devuelve:** `void`

**Descripción oficial:**

You can check if the player is in a Switch state with [`IS_PLAYER_SWITCH_IN_PROGRESS`](#isplayerswitchinprogress).

***Note:** Doesn't act normally when used on Mount Chiliad.*

**Nombres antiguos (alias):** `0xAAB3200ED59016BC` (`N_0xaab3200ed59016bc`), `_SWITCH_OUT_PLAYER` (`SwitchOutPlayer`)

**Ejemplo (lua):**

```lua
-- Check if the player is in a Switch "state"
if not IsPlayerSwitchInProgress() then
    -- If the player is not already in a Switch state, initiate a Switch
    SwitchToMultiFirstPart(PlayerPedId(), 0, 1)
    -- In this case, switchType is set to 1, which means "3 steps out from ped"
end
```

**Ejemplo (js):**

```js
// Check if the player is in a Switch "state"
if (!IsPlayerSwitchInProgress()) {
    // If the player is not already in a Switch state, initiate a Switch
    SwitchToMultiFirstPart(PlayerPedId(), 0, 1);
    // In this case, switchType is set to 1, which means "3 steps out from ped" according to the documentation
}
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;

// Check if the player is in a Switch "state"
if (!IsPlayerSwitchInProgress()) {
    // If the player is not already in a Switch state, initiate a Switch
    SwitchToMultiFirstPart(API.PlayerPedId(), 0, 1);
    // In this case, switchType is set to 1, which means "3 steps out from ped" according to the documentation
}
```

---
### SwitchToMultiSecondpart

`SWITCH_TO_MULTI_SECONDPART` · hash `0xD8295AF639FD9CB8` · jhash `0x2349373B` · **Cliente**

```lua
SwitchToMultiSecondpart(ped)
```
```c
void SWITCH_TO_MULTI_SECONDPART(Ped ped);
```

**Parámetros**

- `ped` (`Ped`)

**Devuelve:** `void`

**Descripción oficial:**

After using [`SWITCH_TO_MULTI_FIRSTPART`](#switchtomultifirstpart) , use this native to smoothly return the camera to the player's character.

**Nombres antiguos (alias):** `0xD8295AF639FD9CB8` (`N_0xd8295af639fd9cb8`), `_SWITCH_IN_PLAYER` (`SwitchInPlayer`)

**Ejemplo (lua):**

```lua
RegisterCommand("switchPlayer", function()
    if IsPlayerSwitchInProgress() then return end
    local ped = PlayerPedId()
    SwitchToMultiFirstPart(ped, 0, 1)
    Citizen.Wait(5000)
    SwitchToMultiSecondPart(ped)
end, false)
```

**Ejemplo (js):**

```js
RegisterCommand("switchPlayer", () => {
    if (IsPlayerSwitchInProgress()) return;
    const ped = PlayerPedId();
    SwitchToMultiFirstPart(ped, 0, 1);
    Delay(5000); // Delay doesn't exist, you have to make it yourself
    SwitchToMultiSecondPart(ped);
}, false);
```

**Ejemplo (cs):**

```cs
using static CitizenFX.Core.Native.API;
RegisterCommand("switchPlayer", new Action<int, List<object>, string>(async (user, args, raw) =>
{
    if (IsPlayerSwitchInProgress()) return;
    Ped ped = PlayerPedId();
    SwitchToMultiFirstPart(ped, 0, 1);
    await Delay(5000);
    SwitchToMultiSecondPart(ped);
}), false);
```

---
