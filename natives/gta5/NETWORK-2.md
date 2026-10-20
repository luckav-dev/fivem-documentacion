# Natives de GTA V — NETWORK (parte 2 de 2: SetNetworkVehiclePositionUpdateMultiplier … VehToNet)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `NETWORK`: **823** natives.

Partes: [1](NETWORK-1.md) · **[2]**

[← Índice de natives](../README.md)

## Índice de esta página

[`SetNetworkVehiclePositionUpdateMultiplier`](#setnetworkvehiclepositionupdatemultiplier) · [`SetNetworkVehicleRespotTimer`](#setnetworkvehiclerespottimer) · [`SetPlayerInvisibleLocally`](#setplayerinvisiblelocally) · [`SetPlayerVisibleLocally`](#setplayervisiblelocally) · [`SetRelationshipToPlayer`](#setrelationshiptoplayer) · [`SetStoreEnabled`](#setstoreenabled) · [`ShutdownAndLaunchSinglePlayerGame`](#shutdownandlaunchsingleplayergame) · [`ShutdownAndLoadMostRecentSave`](#shutdownandloadmostrecentsave) · [`TextureDownloadGetName`](#texturedownloadgetname) · [`TextureDownloadHasFailed`](#texturedownloadhasfailed) · [`TextureDownloadRelease`](#texturedownloadrelease) · [`TextureDownloadRequest`](#texturedownloadrequest) · [`TitleTextureDownloadRequest`](#titletexturedownloadrequest) · [`TriggerScriptCrcCheckOnPlayer`](#triggerscriptcrccheckonplayer) · [`UgcCancelQuery`](#ugccancelquery) · [`UgcClearCreateResult`](#ugcclearcreateresult) · [`UgcClearModifyResult`](#ugcclearmodifyresult) · [`UgcClearOfflineQuery`](#ugcclearofflinequery) · [`UgcClearQueryResults`](#ugcclearqueryresults) · [`UgcCopyContent`](#ugccopycontent) · [`UgcDidGetSucceed`](#ugcdidgetsucceed) · [`UgcGetBookmarkedContent`](#ugcgetbookmarkedcontent) · [`UgcGetCachedDescription`](#ugcgetcacheddescription) · [`UgcGetContentCategory`](#ugcgetcontentcategory) · [`UgcGetContentDescriptionHash`](#ugcgetcontentdescriptionhash) · [`UgcGetContentFileVersion`](#ugcgetcontentfileversion) · [`UgcGetContentHasPlayerBookmarked`](#ugcgetcontenthasplayerbookmarked) · [`UgcGetContentHasPlayerRecord`](#ugcgetcontenthasplayerrecord) · [`UgcGetContentHash`](#ugcgetcontenthash) · [`UgcGetContentId`](#ugcgetcontentid) · [`UgcGetContentIsPublished`](#ugcgetcontentispublished) · [`UgcGetContentIsVerified`](#ugcgetcontentisverified) · [`UgcGetContentLanguage`](#ugcgetcontentlanguage) · [`UgcGetContentName`](#ugcgetcontentname) · [`UgcGetContentNum`](#ugcgetcontentnum) · [`UgcGetContentPath`](#ugcgetcontentpath) · [`UgcGetContentRating`](#ugcgetcontentrating) · [`UgcGetContentRatingCount`](#ugcgetcontentratingcount) · [`UgcGetContentRatingNegativeCount`](#ugcgetcontentratingnegativecount) · [`UgcGetContentRatingPositiveCount`](#ugcgetcontentratingpositivecount) · [`UgcGetContentTotal`](#ugcgetcontenttotal) · [`UgcGetContentUpdatedDate`](#ugcgetcontentupdateddate) · [`UgcGetContentUserId`](#ugcgetcontentuserid) · [`UgcGetContentUserName`](#ugcgetcontentusername) · [`UgcGetCreateContentId`](#ugcgetcreatecontentid) · [`UgcGetCreateResult`](#ugcgetcreateresult) · [`UgcGetCreatorNum`](#ugcgetcreatornum) · [`UgcGetCrewContent`](#ugcgetcrewcontent) · [`UgcGetFriendContent`](#ugcgetfriendcontent) · [`UgcGetGetByCategory`](#ugcgetgetbycategory) · [`UgcGetModifyResult`](#ugcgetmodifyresult) · [`UgcGetMyContent`](#ugcgetmycontent) · [`UgcGetQueryResult`](#ugcgetqueryresult) · [`UgcGetRootContentId`](#ugcgetrootcontentid) · [`UgcHasCreateFinished`](#ugchascreatefinished) · [`UgcHasGetFinished`](#ugchasgetfinished) · [`UgcHasModifyFinished`](#ugchasmodifyfinished) · [`UgcIsGetting`](#ugcisgetting) · [`UgcIsLanguageSupported`](#ugcislanguagesupported) · [`UgcPoliciesMakePrivate`](#ugcpoliciesmakeprivate) · [`UgcPublish`](#ugcpublish) · [`UgcQueryByContentId`](#ugcquerybycontentid) · [`UgcQueryByContentIds`](#ugcquerybycontentids) · [`UgcQueryMyContent`](#ugcquerymycontent) · [`UgcQueryRecentlyCreatedContent`](#ugcqueryrecentlycreatedcontent) · [`UgcRequestCachedDescription`](#ugcrequestcacheddescription) · [`UgcRequestContentDataFromIndex`](#ugcrequestcontentdatafromindex) · [`UgcRequestContentDataFromParams`](#ugcrequestcontentdatafromparams) · [`UgcSetBookmarked`](#ugcsetbookmarked) · [`UgcSetDeleted`](#ugcsetdeleted) · [`UgcSetQueryDataFromOffline`](#ugcsetquerydatafromoffline) · [`UgcTextureDownloadRequest`](#ugctexturedownloadrequest) · [`UsePlayerColourInsteadOfTeamColour`](#useplayercolourinsteadofteamcolour) · [`VehToNet`](#vehtonet)

---
### SetNetworkVehiclePositionUpdateMultiplier

`_SET_NETWORK_VEHICLE_POSITION_UPDATE_MULTIPLIER` · hash `0xA2A707979FE754DC` · **Cliente**

```lua
SetNetworkVehiclePositionUpdateMultiplier(vehicle, multiplier)
```
```c
void _SET_NETWORK_VEHICLE_POSITION_UPDATE_MULTIPLIER(Vehicle vehicle, float multiplier);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `multiplier` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
rage::netBlenderLinInterp::GetPositionMaxForUpdateLevel
```

**Nombres antiguos (alias):** `0xA2A707979FE754DC` (`N_0xa2a707979fe754dc`), `_SET_NETWORK_VEHICLE_BLENDER_DISTANCE_MULTIPLIER` (`SetNetworkVehicleBlenderDistanceMultiplier`)

---
### SetNetworkVehicleRespotTimer

`SET_NETWORK_VEHICLE_RESPOT_TIMER` · hash `0xEC51713AB6EC36E8` · jhash `0x2C30912D` · **Cliente**

```lua
SetNetworkVehicleRespotTimer(netId, time)
```
```c
void SET_NETWORK_VEHICLE_RESPOT_TIMER(int netId, int time);
```

**Parámetros**

- `netId` (`int`)
- `time` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 3: Any p2
NativeDB Added Parameter 4: Any p3
```

---
### SetPlayerInvisibleLocally

`SET_PLAYER_INVISIBLE_LOCALLY` · hash `0x12B37D54667DB0B8` · jhash `0x18227209` · **Cliente**

```lua
SetPlayerInvisibleLocally(player, toggle)
```
```c
void SET_PLAYER_INVISIBLE_LOCALLY(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetPlayerVisibleLocally

`SET_PLAYER_VISIBLE_LOCALLY` · hash `0xFAA10F1FAFB11AF2` · jhash `0xBA2BB4B4` · **Cliente**

```lua
SetPlayerVisibleLocally(player, toggle)
```
```c
void SET_PLAYER_VISIBLE_LOCALLY(Player player, BOOL toggle);
```

**Parámetros**

- `player` (`Player`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetRelationshipToPlayer

`_SET_RELATIONSHIP_TO_PLAYER` · hash `0xA7C511FA1C5BDA38` · **Cliente**

```lua
SetRelationshipToPlayer(player, p1)
```
```c
void _SET_RELATIONSHIP_TO_PLAYER(Player player, BOOL p1);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Enables ghosting between specific players. Name is between `_SET_RELATIONSHIP_GROUP_DONT_AFFECT_WANTED_LEVEL` and `SET_ROADS_BACK_TO_ORIGINAL`.

**Nombres antiguos (alias):** `0xA7C511FA1C5BDA38` (`N_0xa7c511fa1c5bda38`)

---
### SetStoreEnabled

`SET_STORE_ENABLED` · hash `0x9641A9FF718E9C5E` · jhash `0xC1F6443B` · **Cliente**

```lua
SetStoreEnabled(toggle)
```
```c
void SET_STORE_ENABLED(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Access to the store for shark cards etc...  
```

---
### ShutdownAndLaunchSinglePlayerGame

`SHUTDOWN_AND_LAUNCH_SINGLE_PLAYER_GAME` · hash `0x593850C16A36B692` · jhash `0x92B7351C` · **Cliente**

```lua
ShutdownAndLaunchSinglePlayerGame()
```
```c
void SHUTDOWN_AND_LAUNCH_SINGLE_PLAYER_GAME();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Starts a new singleplayer game (at the prologue).  
```

---
### ShutdownAndLoadMostRecentSave

`_SHUTDOWN_AND_LOAD_MOST_RECENT_SAVE` · hash `0x9ECA15ADFE141431` · **Cliente**

```lua
local retval = ShutdownAndLoadMostRecentSave()
```
```c
BOOL _SHUTDOWN_AND_LOAD_MOST_RECENT_SAVE();
```

**Devuelve:** `BOOL` — always seems to be 1

**Descripción oficial:**

Disconnects you from the session, and starts loading single player, however you still remain connected to the server (only if you're the host, if you're not then you also (most likely) get disconnected from the server) and other players will not be able to join until you exit the game.

If you're already in SP then it'll re-load singleplayer.

You might need to DoScreenFadeIn and ShutdownLoadingScreen otherwise you probably won't end up loading into SP at all.

Somewhat related note: opening the pause menu after loading into this 'singleplayer' mode crashes the game.

**Nombres antiguos (alias):** `0x9ECA15ADFE141431` (`N_0x9eca15adfe141431`)

---
### TextureDownloadGetName

`TEXTURE_DOWNLOAD_GET_NAME` · hash `0x3448505B6E35262D` · jhash `0xA40EF65A` · **Cliente**

```lua
local retval = TextureDownloadGetName(p0)
```
```c
char* TEXTURE_DOWNLOAD_GET_NAME(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `char*`

---
### TextureDownloadHasFailed

`TEXTURE_DOWNLOAD_HAS_FAILED` · hash `0x5776ED562C134687` · jhash `0xE4547765` · **Cliente**

```lua
local retval = TextureDownloadHasFailed(p0)
```
```c
BOOL TEXTURE_DOWNLOAD_HAS_FAILED(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5776ED562C134687` (`N_0x5776ed562c134687`)

---
### TextureDownloadRelease

`TEXTURE_DOWNLOAD_RELEASE` · hash `0x487EB90B98E9FB19` · jhash `0xEE8D9E70` · **Cliente**

```lua
TextureDownloadRelease(p0)
```
```c
void TEXTURE_DOWNLOAD_RELEASE(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `void`

---
### TextureDownloadRequest

`TEXTURE_DOWNLOAD_REQUEST` · hash `0x16160DA74A8E74A2` · jhash `0xAD546CC3` · **Cliente**

```lua
local retval, PlayerHandle = TextureDownloadRequest(FilePath, Name, p3)
```
```c
int TEXTURE_DOWNLOAD_REQUEST(int* PlayerHandle, char* FilePath, char* Name, BOOL p3);
```

**Parámetros**

- `PlayerHandle` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `FilePath` (`char*`)
- `Name` (`char*`)
- `p3` (`BOOL`)

**Devuelve:** `int`

---
### TitleTextureDownloadRequest

`TITLE_TEXTURE_DOWNLOAD_REQUEST` · hash `0x0B203B4AFDE53A4F` · jhash `0x1856D008` · **Cliente**

```lua
local retval = TitleTextureDownloadRequest(FilePath, Name, p2)
```
```c
int TITLE_TEXTURE_DOWNLOAD_REQUEST(char* FilePath, char* Name, BOOL p2);
```

**Parámetros**

- `FilePath` (`char*`)
- `Name` (`char*`)
- `p2` (`BOOL`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0B203B4AFDE53A4F` (`N_0x0b203b4afde53a4f`)

---
### TriggerScriptCrcCheckOnPlayer

`_TRIGGER_SCRIPT_CRC_CHECK_ON_PLAYER` · hash `0x46FB3ED415C7641C` · jhash `0xF9A51B92` · **Cliente**

```lua
local retval = TriggerScriptCrcCheckOnPlayer(player, p1, scriptHash)
```
```c
BOOL _TRIGGER_SCRIPT_CRC_CHECK_ON_PLAYER(Player player, int p1, Hash scriptHash);
```

**Parámetros**

- `player` (`Player`)
- `p1` (`int`)
- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p1 = 6
```

**Nombres antiguos (alias):** `0x46FB3ED415C7641C` (`N_0x46fb3ed415c7641c`), `_NETWORK_IS_PLAYER_IN_SCRIPT` (`NetworkIsPlayerInScript`)

---
### UgcCancelQuery

`UGC_CANCEL_QUERY` · hash `0xE9B99B6853181409` · jhash `0x021D5A94` · **Cliente**

```lua
UgcCancelQuery()
```
```c
void UGC_CANCEL_QUERY();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE9B99B6853181409` (`N_0xe9b99b6853181409`)

---
### UgcClearCreateResult

`UGC_CLEAR_CREATE_RESULT` · hash `0x17440AA15D1D3739` · jhash `0x133FF2D5` · **Cliente**

```lua
UgcClearCreateResult()
```
```c
void UGC_CLEAR_CREATE_RESULT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x17440AA15D1D3739` (`N_0x17440aa15d1d3739`)

---
### UgcClearModifyResult

`UGC_CLEAR_MODIFY_RESULT` · hash `0xA1E5E0204A6FCC70` · jhash `0x405ECA16` · **Cliente**

```lua
UgcClearModifyResult()
```
```c
void UGC_CLEAR_MODIFY_RESULT();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA1E5E0204A6FCC70` (`N_0xa1e5e0204a6fcc70`)

---
### UgcClearOfflineQuery

`UGC_CLEAR_OFFLINE_QUERY` · hash `0x61A885D3F7CFEE9A` · jhash `0xE13C1F7F` · **Cliente**

```lua
UgcClearOfflineQuery()
```
```c
void UGC_CLEAR_OFFLINE_QUERY();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x61A885D3F7CFEE9A` (`N_0x61a885d3f7cfee9a`)

---
### UgcClearQueryResults

`UGC_CLEAR_QUERY_RESULTS` · hash `0xBA96394A0EECFA65` · jhash `0x0D35DD93` · **Cliente**

```lua
UgcClearQueryResults()
```
```c
void UGC_CLEAR_QUERY_RESULTS();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBA96394A0EECFA65` (`N_0xba96394a0eecfa65`)

---
### UgcCopyContent

`UGC_COPY_CONTENT` · hash `0x152D90E4C1B4738A` · jhash `0x08243B79` · **Cliente**

```lua
local retval, p0, p1 = UgcCopyContent()
```
```c
BOOL UGC_COPY_CONTENT(Any* p0, Any* p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x152D90E4C1B4738A` (`N_0x152d90e4c1b4738a`)

---
### UgcDidGetSucceed

`UGC_DID_GET_SUCCEED` · hash `0x941E5306BCD7C2C7` · jhash `0x3970B0DA` · **Cliente**

```lua
local retval = UgcDidGetSucceed()
```
```c
Any UGC_DID_GET_SUCCEED();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x941E5306BCD7C2C7` (`N_0x941e5306bcd7c2c7`)

---
### UgcGetBookmarkedContent

`UGC_GET_BOOKMARKED_CONTENT` · hash `0xD5A4B59980401588` · jhash `0x4609D596` · **Cliente**

```lua
local retval, p2, p3 = UgcGetBookmarkedContent(p0, p1)
```
```c
BOOL UGC_GET_BOOKMARKED_CONTENT(Any p0, Any p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD5A4B59980401588` (`N_0xd5a4b59980401588`)

---
### UgcGetCachedDescription

`UGC_GET_CACHED_DESCRIPTION` · hash `0x40F7E66472DF3E5C` · jhash `0x70A2845C` · **Cliente**

```lua
local retval = UgcGetCachedDescription(p0, p1)
```
```c
char* UGC_GET_CACHED_DESCRIPTION(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0x40F7E66472DF3E5C` (`N_0x40f7e66472df3e5c`)

---
### UgcGetContentCategory

`UGC_GET_CONTENT_CATEGORY` · hash `0xA7BAB11E7C9C6C5A` · jhash `0x5E8A7559` · **Cliente**

```lua
local retval = UgcGetContentCategory(p0)
```
```c
int UGC_GET_CONTENT_CATEGORY(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xA7BAB11E7C9C6C5A` (`N_0xa7bab11e7c9c6c5a`), `_GET_CONTENT_CATEGORY` (`GetContentCategory`)

---
### UgcGetContentDescriptionHash

`UGC_GET_CONTENT_DESCRIPTION_HASH` · hash `0x7CF0448787B23758` · jhash `0x91534C6E` · **Cliente**

```lua
local retval = UgcGetContentDescriptionHash(p0)
```
```c
int UGC_GET_CONTENT_DESCRIPTION_HASH(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x7CF0448787B23758` (`N_0x7cf0448787b23758`), `_GET_CONTENT_DESCRIPTION_HASH` (`GetContentDescriptionHash`)

---
### UgcGetContentFileVersion

`UGC_GET_CONTENT_FILE_VERSION` · hash `0x37025B27D9B658B1` · jhash `0xFF7D44E6` · **Cliente**

```lua
local retval = UgcGetContentFileVersion(p0, p1)
```
```c
Any UGC_GET_CONTENT_FILE_VERSION(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x37025B27D9B658B1` (`N_0x37025b27d9b658b1`), `_GET_CONTENT_FILE_VERSION` (`GetContentFileVersion`)

---
### UgcGetContentHasPlayerBookmarked

`UGC_GET_CONTENT_HAS_PLAYER_BOOKMARKED` · hash `0x993CBE59D350D225` · jhash `0x0DEB3F5A` · **Cliente**

```lua
local retval = UgcGetContentHasPlayerBookmarked(p0)
```
```c
BOOL UGC_GET_CONTENT_HAS_PLAYER_BOOKMARKED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x993CBE59D350D225` (`N_0x993cbe59d350d225`)

---
### UgcGetContentHasPlayerRecord

`UGC_GET_CONTENT_HAS_PLAYER_RECORD` · hash `0x70EA8DA57840F9BE` · jhash `0x11DC0F27` · **Cliente**

```lua
local retval = UgcGetContentHasPlayerRecord(p0)
```
```c
BOOL UGC_GET_CONTENT_HAS_PLAYER_RECORD(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x70EA8DA57840F9BE` (`N_0x70ea8da57840f9be`)

---
### UgcGetContentHash

`UGC_GET_CONTENT_HASH` · hash `0x3A17A27D75C74887` · jhash `0x8E1D8F78` · **Cliente**

```lua
local retval = UgcGetContentHash()
```
```c
Hash UGC_GET_CONTENT_HASH();
```

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0x3A17A27D75C74887` (`N_0x3a17a27d75c74887`)

---
### UgcGetContentId

`UGC_GET_CONTENT_ID` · hash `0x55AA95F481D694D2` · jhash `0x331AEABF` · **Cliente**

```lua
local retval = UgcGetContentId(p0)
```
```c
char* UGC_GET_CONTENT_ID(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Return the mission id of a job.
```

**Nombres antiguos (alias):** `0x55AA95F481D694D2` (`N_0x55aa95f481d694d2`), `_GET_CONTENT_ID` (`GetContentId`)

---
### UgcGetContentIsPublished

`UGC_GET_CONTENT_IS_PUBLISHED` · hash `0x3054F114121C21EA` · jhash `0xA850DDE1` · **Cliente**

```lua
local retval = UgcGetContentIsPublished(p0)
```
```c
BOOL UGC_GET_CONTENT_IS_PUBLISHED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3054F114121C21EA` (`N_0x3054f114121c21ea`)

---
### UgcGetContentIsVerified

`UGC_GET_CONTENT_IS_VERIFIED` · hash `0xA9240A96C74CCA13` · jhash `0x8F6754AE` · **Cliente**

```lua
local retval = UgcGetContentIsVerified(p0)
```
```c
BOOL UGC_GET_CONTENT_IS_VERIFIED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA9240A96C74CCA13` (`N_0xa9240a96c74cca13`)

---
### UgcGetContentLanguage

`UGC_GET_CONTENT_LANGUAGE` · hash `0x32DD916F3F7C9672` · jhash `0xA2C5BD9D` · **Cliente**

```lua
local retval = UgcGetContentLanguage(p0)
```
```c
Any UGC_GET_CONTENT_LANGUAGE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x32DD916F3F7C9672` (`N_0x32dd916f3f7c9672`)

---
### UgcGetContentName

`UGC_GET_CONTENT_NAME` · hash `0xBF09786A7FCAB582` · jhash `0xA5A0C695` · **Cliente**

```lua
local retval = UgcGetContentName(p0)
```
```c
char* UGC_GET_CONTENT_NAME(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xBF09786A7FCAB582` (`N_0xbf09786a7fcab582`)

---
### UgcGetContentNum

`UGC_GET_CONTENT_NUM` · hash `0xE0A6138401BCB837` · jhash `0x2DE69817` · **Cliente**

```lua
local retval = UgcGetContentNum()
```
```c
Any UGC_GET_CONTENT_NUM();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xE0A6138401BCB837` (`N_0xe0a6138401bcb837`)

---
### UgcGetContentPath

`UGC_GET_CONTENT_PATH` · hash `0xBAF6BABF9E7CCC13` · jhash `0x744A9EA5` · **Cliente**

```lua
local retval = UgcGetContentPath(p0, p1)
```
```c
char* UGC_GET_CONTENT_PATH(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xBAF6BABF9E7CCC13` (`N_0xbaf6babf9e7ccc13`), `_UGC_GET_CLOUD_PATH` (`UgcGetCloudPath`)

---
### UgcGetContentRating

`UGC_GET_CONTENT_RATING` · hash `0x1ACCFBA3D8DAB2EE` · jhash `0x1E34953F` · **Cliente**

```lua
local retval = UgcGetContentRating(p0, p1)
```
```c
Any UGC_GET_CONTENT_RATING(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x1ACCFBA3D8DAB2EE` (`N_0x1accfba3d8dab2ee`)

---
### UgcGetContentRatingCount

`UGC_GET_CONTENT_RATING_COUNT` · hash `0x759299C5BB31D2A9` · jhash `0x771FE190` · **Cliente**

```lua
local retval = UgcGetContentRatingCount(p0, p1)
```
```c
Any UGC_GET_CONTENT_RATING_COUNT(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x759299C5BB31D2A9` (`N_0x759299c5bb31d2a9`)

---
### UgcGetContentRatingNegativeCount

`UGC_GET_CONTENT_RATING_NEGATIVE_COUNT` · hash `0x4E548C0D7AE39FF9` · jhash `0x41A0FB02` · **Cliente**

```lua
local retval = UgcGetContentRatingNegativeCount(p0, p1)
```
```c
Any UGC_GET_CONTENT_RATING_NEGATIVE_COUNT(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x4E548C0D7AE39FF9` (`N_0x4e548c0d7ae39ff9`)

---
### UgcGetContentRatingPositiveCount

`UGC_GET_CONTENT_RATING_POSITIVE_COUNT` · hash `0x87E5C46C187FE0AE` · jhash `0x3276D9D3` · **Cliente**

```lua
local retval = UgcGetContentRatingPositiveCount(p0, p1)
```
```c
Any UGC_GET_CONTENT_RATING_POSITIVE_COUNT(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x87E5C46C187FE0AE` (`N_0x87e5c46c187fe0ae`)

---
### UgcGetContentTotal

`UGC_GET_CONTENT_TOTAL` · hash `0x769951E2455E2EB5` · jhash `0x81BD8D3B` · **Cliente**

```lua
local retval = UgcGetContentTotal()
```
```c
Any UGC_GET_CONTENT_TOTAL();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x769951E2455E2EB5` (`N_0x769951e2455e2eb5`)

---
### UgcGetContentUpdatedDate

`UGC_GET_CONTENT_UPDATED_DATE` · hash `0xCFD115B373C0DF63` · jhash `0xA19A238D` · **Cliente**

```lua
local p1 = UgcGetContentUpdatedDate(p0, p1)
```
```c
void UGC_GET_CONTENT_UPDATED_DATE(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xCFD115B373C0DF63` (`N_0xcfd115b373c0df63`)

---
### UgcGetContentUserId

`UGC_GET_CONTENT_USER_ID` · hash `0xCD67AD041A394C9C` · jhash `0x8F3137E6` · **Cliente**

```lua
local retval = UgcGetContentUserId(p0)
```
```c
char* UGC_GET_CONTENT_USER_ID(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xCD67AD041A394C9C` (`N_0xcd67ad041a394c9c`), `_GET_CONTENT_USER_ID` (`GetContentUserId`), `GET_PLAYER_ADVANCED_MODIFIER_PRIVILEGES` (`GetPlayerAdvancedModifierPrivileges`)

---
### UgcGetContentUserName

`UGC_GET_CONTENT_USER_NAME` · hash `0x703F12425ECA8BF5` · jhash `0xB9137BA7` · **Cliente**

```lua
local retval = UgcGetContentUserName(p0)
```
```c
char* UGC_GET_CONTENT_USER_NAME(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0x703F12425ECA8BF5` (`N_0x703f12425eca8bf5`)

---
### UgcGetCreateContentId

`UGC_GET_CREATE_CONTENT_ID` · hash `0xC55A0B40FFB1ED23` · jhash `0x82146BE9` · **Cliente**

```lua
local retval = UgcGetCreateContentId()
```
```c
char* UGC_GET_CREATE_CONTENT_ID();
```

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xC55A0B40FFB1ED23` (`N_0xc55a0b40ffb1ed23`)

---
### UgcGetCreateResult

`UGC_GET_CREATE_RESULT` · hash `0xFBC5E768C7A77A6A` · jhash `0xCE569932` · **Cliente**

```lua
local retval = UgcGetCreateResult()
```
```c
Any UGC_GET_CREATE_RESULT();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xFBC5E768C7A77A6A` (`N_0xfbc5e768c7a77a6a`)

---
### UgcGetCreatorNum

`UGC_GET_CREATOR_NUM` · hash `0x597F8DBA9B206FC7` · jhash `0x410C61D1` · **Cliente**

```lua
local retval = UgcGetCreatorNum()
```
```c
Any UGC_GET_CREATOR_NUM();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x597F8DBA9B206FC7` (`N_0x597f8dba9b206fc7`)

---
### UgcGetCrewContent

`UGC_GET_CREW_CONTENT` · hash `0x9F6E2821885CAEE2` · jhash `0xA6D8B798` · **Cliente**

```lua
local retval, p3, p4 = UgcGetCrewContent(p0, p1, p2)
```
```c
BOOL UGC_GET_CREW_CONTENT(Any p0, Any p1, Any p2, Any* p3, Any* p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9F6E2821885CAEE2` (`N_0x9f6e2821885caee2`)

---
### UgcGetFriendContent

`UGC_GET_FRIEND_CONTENT` · hash `0xF9E1CCAE8BA4C281` · jhash `0x9EFBD5D1` · **Cliente**

```lua
local retval, p2, p3 = UgcGetFriendContent(p0, p1)
```
```c
BOOL UGC_GET_FRIEND_CONTENT(Any p0, Any p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF9E1CCAE8BA4C281` (`N_0xf9e1ccae8ba4c281`)

---
### UgcGetGetByCategory

`UGC_GET_GET_BY_CATEGORY` · hash `0x678BB03C1A3BD51E` · jhash `0x67E74842` · **Cliente**

```lua
local retval, p3, p4 = UgcGetGetByCategory(p0, p1, p2)
```
```c
BOOL UGC_GET_GET_BY_CATEGORY(Any p0, Any p1, Any p2, Any* p3, Any* p4);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x678BB03C1A3BD51E` (`N_0x678bb03c1a3bd51e`)

---
### UgcGetModifyResult

`UGC_GET_MODIFY_RESULT` · hash `0x5A0A3D1A186A5508` · jhash `0x1F0DD8AF` · **Cliente**

```lua
local retval = UgcGetModifyResult()
```
```c
Any UGC_GET_MODIFY_RESULT();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x5A0A3D1A186A5508` (`N_0x5a0a3d1a186a5508`)

---
### UgcGetMyContent

`UGC_GET_MY_CONTENT` · hash `0x3195F8DD0D531052` · jhash `0x4C2C0D1F` · **Cliente**

```lua
local retval, p2, p3 = UgcGetMyContent(p0, p1)
```
```c
BOOL UGC_GET_MY_CONTENT(Any p0, Any p1, Any* p2, Any* p3);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3195F8DD0D531052` (`N_0x3195f8dd0d531052`)

---
### UgcGetQueryResult

`UGC_GET_QUERY_RESULT` · hash `0xEDF7F927136C224B` · jhash `0xCC2356E3` · **Cliente**

```lua
local retval = UgcGetQueryResult()
```
```c
Any UGC_GET_QUERY_RESULT();
```

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0xEDF7F927136C224B` (`N_0xedf7f927136c224b`)

---
### UgcGetRootContentId

`UGC_GET_ROOT_CONTENT_ID` · hash `0xC0173D6BFF4E0348` · jhash `0x0E5E8E5C` · **Cliente**

```lua
local retval = UgcGetRootContentId(p0)
```
```c
char* UGC_GET_ROOT_CONTENT_ID(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `char*`

**Descripción oficial:**

```
Return the root content id of a job.
```

**Nombres antiguos (alias):** `0xC0173D6BFF4E0348` (`N_0xc0173d6bff4e0348`), `_GET_ROOT_CONTENT_ID` (`GetRootContentId`)

---
### UgcHasCreateFinished

`UGC_HAS_CREATE_FINISHED` · hash `0x5E24341A7F92A74B` · jhash `0xE69E8D0D` · **Cliente**

```lua
local retval = UgcHasCreateFinished()
```
```c
BOOL UGC_HAS_CREATE_FINISHED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5E24341A7F92A74B` (`N_0x5e24341a7f92a74b`)

---
### UgcHasGetFinished

`UGC_HAS_GET_FINISHED` · hash `0x02ADA21EA2F6918F` · jhash `0x50296140` · **Cliente**

```lua
local retval = UgcHasGetFinished()
```
```c
BOOL UGC_HAS_GET_FINISHED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x02ADA21EA2F6918F` (`N_0x02ada21ea2f6918f`)

---
### UgcHasModifyFinished

`UGC_HAS_MODIFY_FINISHED` · hash `0x299EF3C576773506` · jhash `0x611E0BE2` · **Cliente**

```lua
local retval = UgcHasModifyFinished()
```
```c
BOOL UGC_HAS_MODIFY_FINISHED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x299EF3C576773506` (`N_0x299ef3c576773506`)

---
### UgcIsGetting

`UGC_IS_GETTING` · hash `0xD53ACDBEF24A46E8` · jhash `0x4908A514` · **Cliente**

```lua
local retval = UgcIsGetting()
```
```c
BOOL UGC_IS_GETTING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD53ACDBEF24A46E8` (`N_0xd53acdbef24a46e8`)

---
### UgcIsLanguageSupported

`UGC_IS_LANGUAGE_SUPPORTED` · hash `0xF53E48461B71EECB` · jhash `0xB4668B23` · **Cliente**

```lua
local retval = UgcIsLanguageSupported(p0)
```
```c
BOOL UGC_IS_LANGUAGE_SUPPORTED(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF53E48461B71EECB` (`N_0xf53e48461b71eecb`)

---
### UgcPoliciesMakePrivate

`UGC_POLICIES_MAKE_PRIVATE` · hash `0x5CAE833B0EE0C500` · jhash `0x0D4F845D` · **Cliente**

```lua
local retval = UgcPoliciesMakePrivate(p0)
```
```c
BOOL UGC_POLICIES_MAKE_PRIVATE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x5CAE833B0EE0C500` (`N_0x5cae833b0ee0c500`)

---
### UgcPublish

`UGC_PUBLISH` · hash `0x1DE0F5F50D723CAA` · jhash `0xAD334B40` · **Cliente**

```lua
local retval = UgcPublish(contentId, baseContentId, contentTypeName)
```
```c
BOOL UGC_PUBLISH(char* contentId, char* baseContentId, char* contentTypeName);
```

**Parámetros**

- `contentId` (`char*`)
- `baseContentId` (`char*`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1DE0F5F50D723CAA` (`N_0x1de0f5f50d723caa`)

---
### UgcQueryByContentId

`UGC_QUERY_BY_CONTENT_ID` · hash `0x158EC424F35EC469` · jhash `0xDED82A6E` · **Cliente**

```lua
local retval = UgcQueryByContentId(contentId, latestVersion, contentTypeName)
```
```c
BOOL UGC_QUERY_BY_CONTENT_ID(char* contentId, BOOL latestVersion, char* contentTypeName);
```

**Parámetros**

- `contentId` (`char*`)
- `latestVersion` (`BOOL`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x158EC424F35EC469` (`N_0x158ec424f35ec469`)

---
### UgcQueryByContentIds

`UGC_QUERY_BY_CONTENT_IDS` · hash `0xC7397A83F7A2A462` · jhash `0x47B3C35E` · **Cliente**

```lua
local retval, data = UgcQueryByContentIds(count, latestVersion, contentTypeName)
```
```c
BOOL UGC_QUERY_BY_CONTENT_IDS(Any* data, int count, BOOL latestVersion, char* contentTypeName);
```

**Parámetros**

- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `count` (`int`)
- `latestVersion` (`BOOL`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC7397A83F7A2A462` (`N_0xc7397a83f7a2a462`)

---
### UgcQueryMyContent

`UGC_QUERY_MY_CONTENT` · hash `0x9BF438815F5D96EA` · jhash `0xCBA7242F` · **Cliente**

```lua
local retval, p2 = UgcQueryMyContent(p0, p1, p3, p4, p5)
```
```c
BOOL UGC_QUERY_MY_CONTENT(Any p0, Any p1, Any* p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9BF438815F5D96EA` (`N_0x9bf438815f5d96ea`)

---
### UgcQueryRecentlyCreatedContent

`_UGC_QUERY_RECENTLY_CREATED_CONTENT` · hash `0x6D4CB481FAC835E8` · jhash `0x40CF0783` · **Cliente**

```lua
local retval = UgcQueryRecentlyCreatedContent(offset, count, contentTypeName, p3)
```
```c
BOOL _UGC_QUERY_RECENTLY_CREATED_CONTENT(int offset, int count, char* contentTypeName, int p3);
```

**Parámetros**

- `offset` (`int`)
- `count` (`int`)
- `contentTypeName` (`char*`)
- `p3` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6D4CB481FAC835E8` (`N_0x6d4cb481fac835e8`)

---
### UgcRequestCachedDescription

`UGC_REQUEST_CACHED_DESCRIPTION` · hash `0x5E0165278F6339EE` · jhash `0x1C4F9FDB` · **Cliente**

```lua
local retval = UgcRequestCachedDescription(p0)
```
```c
int UGC_REQUEST_CACHED_DESCRIPTION(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x5E0165278F6339EE` (`N_0x5e0165278f6339ee`)

---
### UgcRequestContentDataFromIndex

`UGC_REQUEST_CONTENT_DATA_FROM_INDEX` · hash `0x171DF6A0C07FB3DC` · jhash `0x84315226` · **Cliente**

```lua
local retval = UgcRequestContentDataFromIndex(p0, p1)
```
```c
int UGC_REQUEST_CONTENT_DATA_FROM_INDEX(int p0, int p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x171DF6A0C07FB3DC` (`N_0x171df6a0c07fb3dc`)

---
### UgcRequestContentDataFromParams

`UGC_REQUEST_CONTENT_DATA_FROM_PARAMS` · hash `0x7FD2990AF016795E` · jhash `0x38FC2EEB` · **Cliente**

```lua
local retval = UgcRequestContentDataFromParams(contentTypeName, contentId, p2, p3, p4)
```
```c
int UGC_REQUEST_CONTENT_DATA_FROM_PARAMS(char* contentTypeName, char* contentId, int p2, int p3, int p4);
```

**Parámetros**

- `contentTypeName` (`char*`)
- `contentId` (`char*`)
- `p2` (`int`)
- `p3` (`int`)
- `p4` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x7FD2990AF016795E` (`N_0x7fd2990af016795e`)

---
### UgcSetBookmarked

`UGC_SET_BOOKMARKED` · hash `0x274A1519DFC1094F` · jhash `0x980D45D7` · **Cliente**

```lua
local retval = UgcSetBookmarked(contentId, bookmarked, contentTypeName)
```
```c
BOOL UGC_SET_BOOKMARKED(char* contentId, BOOL bookmarked, char* contentTypeName);
```

**Parámetros**

- `contentId` (`char*`)
- `bookmarked` (`BOOL`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x274A1519DFC1094F` (`N_0x274a1519dfc1094f`)

---
### UgcSetDeleted

`UGC_SET_DELETED` · hash `0xD05D1A6C74DA3498` · jhash `0x48CCC328` · **Cliente**

```lua
local retval, p0, p2 = UgcSetDeleted(p1)
```
```c
BOOL UGC_SET_DELETED(Any* p0, BOOL p1, Any* p2);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`BOOL`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD05D1A6C74DA3498` (`N_0xd05d1a6c74da3498`)

---
### UgcSetQueryDataFromOffline

`UGC_SET_QUERY_DATA_FROM_OFFLINE` · hash `0xF98DDE0A8ED09323` · jhash `0x213C6D36` · **Cliente**

```lua
UgcSetQueryDataFromOffline(p0)
```
```c
void UGC_SET_QUERY_DATA_FROM_OFFLINE(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xF98DDE0A8ED09323` (`N_0xf98dde0a8ed09323`)

---
### UgcTextureDownloadRequest

`UGC_TEXTURE_DOWNLOAD_REQUEST` · hash `0x308F96458B7087CC` · jhash `0x68C9AF69` · **Cliente**

```lua
local retval, p0, p4 = UgcTextureDownloadRequest(p1, p2, p3, p5)
```
```c
Any UGC_TEXTURE_DOWNLOAD_REQUEST(Any* p0, Any p1, Any p2, Any p3, Any* p4, BOOL p5);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p5` (`BOOL`)

**Devuelve:** `Any`

**Nombres antiguos (alias):** `0x308F96458B7087CC` (`N_0x308f96458b7087cc`)

---
### UsePlayerColourInsteadOfTeamColour

`USE_PLAYER_COLOUR_INSTEAD_OF_TEAM_COLOUR` · hash `0x77758139EC9B66C7` · jhash `0x4DD46DAE` · **Cliente**

```lua
UsePlayerColourInsteadOfTeamColour(toggle)
```
```c
void USE_PLAYER_COLOUR_INSTEAD_OF_TEAM_COLOUR(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### VehToNet

`VEH_TO_NET` · hash `0xB4C94523F023419C` · jhash `0xF17634EB` · **Cliente**

```lua
local retval = VehToNet(vehicle)
```
```c
int VEH_TO_NET(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `int`

**Descripción oficial:**

```
calls from vehicle to net.  
```

---
