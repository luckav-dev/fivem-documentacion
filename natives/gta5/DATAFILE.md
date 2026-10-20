# Natives de GTA V — DATAFILE

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `DATAFILE`: **57** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`DataarrayAddBool`](#dataarrayaddbool) · [`DataarrayAddDict`](#dataarrayadddict) · [`DataarrayAddFloat`](#dataarrayaddfloat) · [`DataarrayAddInt`](#dataarrayaddint) · [`DataarrayAddString`](#dataarrayaddstring) · [`DataarrayAddVector`](#dataarrayaddvector) · [`DataarrayGetBool`](#dataarraygetbool) · [`DataarrayGetCount`](#dataarraygetcount) · [`DataarrayGetDict`](#dataarraygetdict) · [`DataarrayGetFloat`](#dataarraygetfloat) · [`DataarrayGetInt`](#dataarraygetint) · [`DataarrayGetString`](#dataarraygetstring) · [`DataarrayGetType`](#dataarraygettype) · [`DataarrayGetVector`](#dataarraygetvector) · [`DatadictCreateArray`](#datadictcreatearray) · [`DatadictCreateDict`](#datadictcreatedict) · [`DatadictGetArray`](#datadictgetarray) · [`DatadictGetBool`](#datadictgetbool) · [`DatadictGetDict`](#datadictgetdict) · [`DatadictGetFloat`](#datadictgetfloat) · [`DatadictGetInt`](#datadictgetint) · [`DatadictGetString`](#datadictgetstring) · [`DatadictGetType`](#datadictgettype) · [`DatadictGetVector`](#datadictgetvector) · [`DatadictSetBool`](#datadictsetbool) · [`DatadictSetFloat`](#datadictsetfloat) · [`DatadictSetInt`](#datadictsetint) · [`DatadictSetString`](#datadictsetstring) · [`DatadictSetVector`](#datadictsetvector) · [`DatafileClearWatchList`](#datafileclearwatchlist) · [`DatafileCreate`](#datafilecreate) · [`DatafileDelete`](#datafiledelete) · [`DatafileDeleteRequestedFile`](#datafiledeleterequestedfile) · [`DatafileFlushMissionHeader`](#datafileflushmissionheader) · [`DatafileGetFileDict`](#datafilegetfiledict) · [`DatafileHasLoadedFileData`](#datafilehasloadedfiledata) · [`DatafileHasValidFileData`](#datafilehasvalidfiledata) · [`DatafileIsSavePending`](#datafileissavepending) · [`DatafileIsValidRequestId`](#datafileisvalidrequestid) · [`DatafileLoadOfflineUgc`](#datafileloadofflineugc) · [`DatafileSelectActiveFile`](#datafileselectactivefile) · [`DatafileSelectCreatorStats`](#datafileselectcreatorstats) · [`DatafileSelectUgcData`](#datafileselectugcdata) · [`DatafileSelectUgcPlayerData`](#datafileselectugcplayerdata) · [`DatafileSelectUgcStats`](#datafileselectugcstats) · [`DatafileStartSaveToCloud`](#datafilestartsavetocloud) · [`DatafileStoreMissionHeader`](#datafilestoremissionheader) · [`DatafileUpdateSaveToCloud`](#datafileupdatesavetocloud) · [`DatafileWatchRequestId`](#datafilewatchrequestid) · [`N_0x6ad0bd5e087866cb`](#n_0x6ad0bd5e087866cb) · [`N_0xa6eef01087181edd`](#n_0xa6eef01087181edd) · [`N_0xdbf860cf1db8e599`](#n_0xdbf860cf1db8e599) · [`UgcCreateContent`](#ugccreatecontent) · [`UgcCreateMission`](#ugccreatemission) · [`UgcSetPlayerData`](#ugcsetplayerdata) · [`UgcUpdateContent`](#ugcupdatecontent) · [`UgcUpdateMission`](#ugcupdatemission)

---
### DataarrayAddBool

`DATAARRAY_ADD_BOOL` · hash `0xF8B0F5A43E928C76` · jhash `0x08174B90` · **Cliente**

```lua
local arrayData = DataarrayAddBool(value)
```
```c
void DATAARRAY_ADD_BOOL(Any* arrayData, BOOL value);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `value` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ARRAY_VALUE_ADD_BOOLEAN` (`ArrayValueAddBoolean`)

---
### DataarrayAddDict

`DATAARRAY_ADD_DICT` · hash `0x6889498B3E19C797` · jhash `0xC174C71B` · **Cliente**

```lua
local retval, arrayData = DataarrayAddDict(arrayData)
```
```c
Any* DATAARRAY_ADD_DICT(Any* arrayData);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any*`

**Nombres antiguos (alias):** `_ARRAY_VALUE_ADD_OBJECT` (`ArrayValueAddObject`)

---
### DataarrayAddFloat

`DATAARRAY_ADD_FLOAT` · hash `0x57A995FD75D37F56` · jhash `0xE4302123` · **Cliente**

```lua
local arrayData = DataarrayAddFloat(value)
```
```c
void DATAARRAY_ADD_FLOAT(Any* arrayData, float value);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `value` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ARRAY_VALUE_ADD_FLOAT` (`ArrayValueAddFloat`)

---
### DataarrayAddInt

`DATAARRAY_ADD_INT` · hash `0xCABDB751D86FE93B` · jhash `0xF29C0B36` · **Cliente**

```lua
local arrayData = DataarrayAddInt(value)
```
```c
void DATAARRAY_ADD_INT(Any* arrayData, int value);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `value` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ARRAY_VALUE_ADD_INTEGER` (`ArrayValueAddInteger`)

---
### DataarrayAddString

`DATAARRAY_ADD_STRING` · hash `0x2F0661C155AEEEAA` · jhash `0xF3C01350` · **Cliente**

```lua
local arrayData = DataarrayAddString(value)
```
```c
void DATAARRAY_ADD_STRING(Any* arrayData, char* value);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `value` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ARRAY_VALUE_ADD_STRING` (`ArrayValueAddString`)

---
### DataarrayAddVector

`DATAARRAY_ADD_VECTOR` · hash `0x407F8D034F70F0C2` · jhash `0x16F464B6` · **Cliente**

```lua
local arrayData = DataarrayAddVector(valueX, valueY, valueZ)
```
```c
void DATAARRAY_ADD_VECTOR(Any* arrayData, float valueX, float valueY, float valueZ);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `valueX` (`float`)
- `valueY` (`float`)
- `valueZ` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_ARRAY_VALUE_ADD_VECTOR3` (`ArrayValueAddVector3`)

---
### DataarrayGetBool

`DATAARRAY_GET_BOOL` · hash `0x50C1B2874E50C114` · jhash `0xA2E5F921` · **Cliente**

```lua
local retval, arrayData = DataarrayGetBool(arrayIndex)
```
```c
BOOL DATAARRAY_GET_BOOL(Any* arrayData, int arrayIndex);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `arrayIndex` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_BOOLEAN` (`ArrayValueGetBoolean`)

---
### DataarrayGetCount

`DATAARRAY_GET_COUNT` · hash `0x065DB281590CEA2D` · jhash `0xA8A21766` · **Cliente**

```lua
local retval, arrayData = DataarrayGetCount(arrayData)
```
```c
int DATAARRAY_GET_COUNT(Any* arrayData);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_SIZE` (`ArrayValueGetSize`)

---
### DataarrayGetDict

`DATAARRAY_GET_DICT` · hash `0x8B5FADCC4E3A145F` · jhash `0xECE81278` · **Cliente**

```lua
local retval, arrayData = DataarrayGetDict(arrayIndex)
```
```c
Any* DATAARRAY_GET_DICT(Any* arrayData, int arrayIndex);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `arrayIndex` (`int`)

**Devuelve:** `Any*`

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_OBJECT` (`ArrayValueGetObject`)

---
### DataarrayGetFloat

`DATAARRAY_GET_FLOAT` · hash `0xC0C527B525D7CFB5` · jhash `0x08AD2CC2` · **Cliente**

```lua
local retval, arrayData = DataarrayGetFloat(arrayIndex)
```
```c
float DATAARRAY_GET_FLOAT(Any* arrayData, int arrayIndex);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `arrayIndex` (`int`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_FLOAT` (`ArrayValueGetFloat`)

---
### DataarrayGetInt

`DATAARRAY_GET_INT` · hash `0x3E5AE19425CD74BE` · jhash `0xBB120CFC` · **Cliente**

```lua
local retval, arrayData = DataarrayGetInt(arrayIndex)
```
```c
int DATAARRAY_GET_INT(Any* arrayData, int arrayIndex);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `arrayIndex` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_INTEGER` (`ArrayValueGetInteger`)

---
### DataarrayGetString

`DATAARRAY_GET_STRING` · hash `0xD3F2FFEB8D836F52` · jhash `0x93F985A6` · **Cliente**

```lua
local retval, arrayData = DataarrayGetString(arrayIndex)
```
```c
char* DATAARRAY_GET_STRING(Any* arrayData, int arrayIndex);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `arrayIndex` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_STRING` (`ArrayValueGetString`)

---
### DataarrayGetType

`DATAARRAY_GET_TYPE` · hash `0x3A0014ADB172A3C5` · jhash `0xFA2402C8` · **Cliente**

```lua
local retval, arrayData = DataarrayGetType(arrayIndex)
```
```c
int DATAARRAY_GET_TYPE(Any* arrayData, int arrayIndex);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `arrayIndex` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Types:  
1 = Boolean  
2 = Integer  
3 = Float  
4 = String  
5 = Vector3  
6 = Object  
7 = Array  
```

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_TYPE` (`ArrayValueGetType`)

---
### DataarrayGetVector

`DATAARRAY_GET_VECTOR` · hash `0x8D2064E5B64A628A` · jhash `0x80E3DA55` · **Cliente**

```lua
local retval, arrayData = DataarrayGetVector(arrayIndex)
```
```c
Vector3 DATAARRAY_GET_VECTOR(Any* arrayData, int arrayIndex);
```

**Parámetros**

- `arrayData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `arrayIndex` (`int`)

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `_ARRAY_VALUE_GET_VECTOR3` (`ArrayValueGetVector3`)

---
### DatadictCreateArray

`DATADICT_CREATE_ARRAY` · hash `0x5B11728527CA6E5F` · jhash `0x03939B8D` · **Cliente**

```lua
local retval, objectData = DatadictCreateArray(key)
```
```c
Any* DATADICT_CREATE_ARRAY(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `Any*`

**Nombres antiguos (alias):** `_OBJECT_VALUE_ADD_ARRAY` (`ObjectValueAddArray`)

---
### DatadictCreateDict

`DATADICT_CREATE_DICT` · hash `0xA358F56F10732EE1` · jhash `0x96A8E05F` · **Cliente**

```lua
local retval, objectData = DatadictCreateDict(key)
```
```c
Any* DATADICT_CREATE_DICT(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `Any*`

**Nombres antiguos (alias):** `_OBJECT_VALUE_ADD_OBJECT` (`ObjectValueAddObject`)

---
### DatadictGetArray

`DATADICT_GET_ARRAY` · hash `0x7A983AA9DA2659ED` · jhash `0x1F2F7D00` · **Cliente**

```lua
local retval, objectData = DatadictGetArray(key)
```
```c
Any* DATADICT_GET_ARRAY(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `Any*`

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_ARRAY` (`ObjectValueGetArray`)

---
### DatadictGetBool

`DATADICT_GET_BOOL` · hash `0x1186940ED72FFEEC` · jhash `0x8876C872` · **Cliente**

```lua
local retval, objectData = DatadictGetBool(key)
```
```c
BOOL DATADICT_GET_BOOL(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_BOOLEAN` (`ObjectValueGetBoolean`)

---
### DatadictGetDict

`DATADICT_GET_DICT` · hash `0xB6B9DDC412FCEEE2` · jhash `0xC9C13D8D` · **Cliente**

```lua
local retval, objectData = DatadictGetDict(key)
```
```c
Any* DATADICT_GET_DICT(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `Any*`

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_OBJECT` (`ObjectValueGetObject`)

---
### DatadictGetFloat

`DATADICT_GET_FLOAT` · hash `0x06610343E73B9727` · jhash `0xA92C1AF4` · **Cliente**

```lua
local retval, objectData = DatadictGetFloat(key)
```
```c
float DATADICT_GET_FLOAT(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_FLOAT` (`ObjectValueGetFloat`)

---
### DatadictGetInt

`DATADICT_GET_INT` · hash `0x78F06F6B1FB5A80C` · jhash `0xA6C68693` · **Cliente**

```lua
local retval, objectData = DatadictGetInt(key)
```
```c
int DATADICT_GET_INT(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_INTEGER` (`ObjectValueGetInteger`)

---
### DatadictGetString

`DATADICT_GET_STRING` · hash `0x3D2FD9E763B24472` · jhash `0x942160EC` · **Cliente**

```lua
local retval, objectData = DatadictGetString(key)
```
```c
char* DATADICT_GET_STRING(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_STRING` (`ObjectValueGetString`)

---
### DatadictGetType

`DATADICT_GET_TYPE` · hash `0x031C55ED33227371` · jhash `0x2678342A` · **Cliente**

```lua
local retval, objectData = DatadictGetType(key)
```
```c
int DATADICT_GET_TYPE(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
Types:  
1 = Boolean  
2 = Integer  
3 = Float  
4 = String  
5 = Vector3  
6 = Object  
7 = Array  
```

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_TYPE` (`ObjectValueGetType`)

---
### DatadictGetVector

`DATADICT_GET_VECTOR` · hash `0x46CD3CB66E0825CC` · jhash `0xE84A127A` · **Cliente**

```lua
local retval, objectData = DatadictGetVector(key)
```
```c
Vector3 DATADICT_GET_VECTOR(Any* objectData, char* key);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)

**Devuelve:** `Vector3`

**Nombres antiguos (alias):** `_OBJECT_VALUE_GET_VECTOR3` (`ObjectValueGetVector3`)

---
### DatadictSetBool

`DATADICT_SET_BOOL` · hash `0x35124302A556A325` · jhash `0x9B29D99B` · **Cliente**

```lua
local objectData = DatadictSetBool(key, value)
```
```c
void DATADICT_SET_BOOL(Any* objectData, char* key, BOOL value);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)
- `value` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_OBJECT_VALUE_ADD_BOOLEAN` (`ObjectValueAddBoolean`)

---
### DatadictSetFloat

`DATADICT_SET_FLOAT` · hash `0xC27E1CC2D795105E` · jhash `0xE972CACF` · **Cliente**

```lua
local objectData = DatadictSetFloat(key, value)
```
```c
void DATADICT_SET_FLOAT(Any* objectData, char* key, float value);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)
- `value` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_OBJECT_VALUE_ADD_FLOAT` (`ObjectValueAddFloat`)

---
### DatadictSetInt

`DATADICT_SET_INT` · hash `0xE7E035450A7948D5` · jhash `0xEFCF554A` · **Cliente**

```lua
local objectData = DatadictSetInt(key, value)
```
```c
void DATADICT_SET_INT(Any* objectData, char* key, int value);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)
- `value` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_OBJECT_VALUE_ADD_INTEGER` (`ObjectValueAddInteger`)

---
### DatadictSetString

`DATADICT_SET_STRING` · hash `0x8FF3847DADD8E30C` · jhash `0xD437615C` · **Cliente**

```lua
local objectData = DatadictSetString(key, value)
```
```c
void DATADICT_SET_STRING(Any* objectData, char* key, char* value);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)
- `value` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_OBJECT_VALUE_ADD_STRING` (`ObjectValueAddString`)

---
### DatadictSetVector

`DATADICT_SET_VECTOR` · hash `0x4CD49B76338C7DEE` · jhash `0x75FC6C3C` · **Cliente**

```lua
local objectData = DatadictSetVector(key, valueX, valueY, valueZ)
```
```c
void DATADICT_SET_VECTOR(Any* objectData, char* key, float valueX, float valueY, float valueZ);
```

**Parámetros**

- `objectData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `key` (`char*`)
- `valueX` (`float`)
- `valueY` (`float`)
- `valueZ` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_OBJECT_VALUE_ADD_VECTOR3` (`ObjectValueAddVector3`)

---
### DatafileClearWatchList

`DATAFILE_CLEAR_WATCH_LIST` · hash `0x6CC86E78358D5119` · jhash `0x5B39D0AC` · **Cliente**

```lua
DatafileClearWatchList()
```
```c
void DATAFILE_CLEAR_WATCH_LIST();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x6CC86E78358D5119` (`N_0x6cc86e78358d5119`)

---
### DatafileCreate

`DATAFILE_CREATE` · hash `0xD27058A1CA2B13EE` · jhash `0x95F8A221` · **Cliente**

```lua
DatafileCreate()
```
```c
void DATAFILE_CREATE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
```

---
### DatafileDelete

`DATAFILE_DELETE` · hash `0x9AB9C1CFC8862DFB` · jhash `0xDEF31B0A` · **Cliente**

```lua
DatafileDelete()
```
```c
void DATAFILE_DELETE();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
```

---
### DatafileDeleteRequestedFile

`DATAFILE_DELETE_REQUESTED_FILE` · hash `0x8F5EA1C01D65A100` · jhash `0x9DB63CFF` · **Cliente**

```lua
local retval = DatafileDeleteRequestedFile(p0)
```
```c
BOOL DATAFILE_DELETE_REQUESTED_FILE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8F5EA1C01D65A100` (`N_0x8f5ea1c01d65a100`)

---
### DatafileFlushMissionHeader

`DATAFILE_FLUSH_MISSION_HEADER` · hash `0xC55854C7D7274882` · jhash `0xF11F956F` · **Cliente**

```lua
DatafileFlushMissionHeader()
```
```c
void DATAFILE_FLUSH_MISSION_HEADER();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC55854C7D7274882` (`N_0xc55854c7d7274882`)

---
### DatafileGetFileDict

`DATAFILE_GET_FILE_DICT` · hash `0x906B778CA1DC72B6` · jhash `0x86DDF9C2` · **Cliente**

```lua
local retval = DatafileGetFileDict()
```
```c
char* DATAFILE_GET_FILE_DICT();
```

**Devuelve:** `char*`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
```

**Nombres antiguos (alias):** `0x906B778CA1DC72B6` (`N_0x906b778ca1dc72b6`)

---
### DatafileHasLoadedFileData

`DATAFILE_HAS_LOADED_FILE_DATA` · hash `0x15FF52B809DB2353` · jhash `0x36FB8B3F` · **Cliente**

```lua
local retval = DatafileHasLoadedFileData(p0)
```
```c
BOOL DATAFILE_HAS_LOADED_FILE_DATA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x15FF52B809DB2353` (`N_0x15ff52b809db2353`)

---
### DatafileHasValidFileData

`DATAFILE_HAS_VALID_FILE_DATA` · hash `0xF8CC1EBE0B62E29F` · jhash `0x2A9411DA` · **Cliente**

```lua
local retval = DatafileHasValidFileData(p0)
```
```c
BOOL DATAFILE_HAS_VALID_FILE_DATA(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF8CC1EBE0B62E29F` (`N_0xf8cc1ebe0b62e29f`)

---
### DatafileIsSavePending

`DATAFILE_IS_SAVE_PENDING` · hash `0xBEDB96A7584AA8CF` · jhash `0x5DCD0796` · **Cliente**

```lua
local retval = DatafileIsSavePending()
```
```c
BOOL DATAFILE_IS_SAVE_PENDING();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Example:  
if (!DATAFILE::_BEDB96A7584AA8CF())  
{  
    if (!g_109E3)  
	{  
        if (((sub_d4f() == 2) == 0) && (!NETWORK::NETWORK_IS_GAME_IN_PROGRESS()))  
{  
            if (NETWORK::NETWORK_IS_CLOUD_AVAILABLE())  
	{  
                g_17A8B = 0;  
            }  
            if (!g_D52C)  
	{  
                sub_730();  
            }  
        }  
    }  
}  
```

**Nombres antiguos (alias):** `0xBEDB96A7584AA8CF` (`N_0xbedb96a7584aa8cf`)

---
### DatafileIsValidRequestId

`DATAFILE_IS_VALID_REQUEST_ID` · hash `0xFCCAE5B92A830878` · jhash `0x01393D16` · **Cliente**

```lua
local retval = DatafileIsValidRequestId(index)
```
```c
BOOL DATAFILE_IS_VALID_REQUEST_ID(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFCCAE5B92A830878` (`N_0xfccae5b92a830878`)

---
### DatafileLoadOfflineUgc

`DATAFILE_LOAD_OFFLINE_UGC` · hash `0xC5238C011AF405E4` · jhash `0x660C468E` · **Cliente**

```lua
local retval = DatafileLoadOfflineUgc(filename)
```
```c
BOOL DATAFILE_LOAD_OFFLINE_UGC(char* filename);
```

**Parámetros**

- `filename` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Loads a User-Generated Content (UGC) file. These files can be found in "[GTA5]\data\ugc" and "[GTA5]\common\patch\ugc". They seem to follow a naming convention, most likely of "[name]_[part].ugc". See example below for usage.
Returns whether or not the file was successfully loaded.
Example:
DATAFILE::_LOAD_UGC_FILE("RockstarPlaylists") // loads "rockstarplaylists_00.ugc"
```

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `_LOAD_UGC_FILE` (`LoadUgcFile`)

---
### DatafileSelectActiveFile

`DATAFILE_SELECT_ACTIVE_FILE` · hash `0x22DA66936E0FFF37` · jhash `0xB41064A4` · **Cliente**

```lua
local retval = DatafileSelectActiveFile(p0)
```
```c
BOOL DATAFILE_SELECT_ACTIVE_FILE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0x22DA66936E0FFF37` (`N_0x22da66936e0fff37`)

---
### DatafileSelectCreatorStats

`DATAFILE_SELECT_CREATOR_STATS` · hash `0x01095C95CD46B624` · jhash `0xB8515B2F` · **Cliente**

```lua
local retval = DatafileSelectCreatorStats(p0)
```
```c
BOOL DATAFILE_SELECT_CREATOR_STATS(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0x01095C95CD46B624` (`N_0x01095c95cd46b624`)

---
### DatafileSelectUgcData

`DATAFILE_SELECT_UGC_DATA` · hash `0xA69AC4ADE82B57A4` · jhash `0xE8D56DA2` · **Cliente**

```lua
local retval = DatafileSelectUgcData(p0)
```
```c
BOOL DATAFILE_SELECT_UGC_DATA(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0xA69AC4ADE82B57A4` (`N_0xa69ac4ade82b57a4`)

---
### DatafileSelectUgcPlayerData

`DATAFILE_SELECT_UGC_PLAYER_DATA` · hash `0x52818819057F2B40` · jhash `0xA4D1B30E` · **Cliente**

```lua
local retval = DatafileSelectUgcPlayerData(p0)
```
```c
BOOL DATAFILE_SELECT_UGC_PLAYER_DATA(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0x52818819057F2B40` (`N_0x52818819057f2b40`)

---
### DatafileSelectUgcStats

`DATAFILE_SELECT_UGC_STATS` · hash `0x9CB0BFA7A9342C3D` · jhash `0xCB6A351E` · **Cliente**

```lua
local retval = DatafileSelectUgcStats(p0, p1)
```
```c
BOOL DATAFILE_SELECT_UGC_STATS(int p0, BOOL p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 3: Any p2
```

**Nombres antiguos (alias):** `0x9CB0BFA7A9342C3D` (`N_0x9cb0bfa7a9342c3d`)

---
### DatafileStartSaveToCloud

`DATAFILE_START_SAVE_TO_CLOUD` · hash `0x83BCCE3224735F05` · jhash `0x768CBB35` · **Cliente**

```lua
local retval = DatafileStartSaveToCloud(filename)
```
```c
BOOL DATAFILE_START_SAVE_TO_CLOUD(char* filename);
```

**Parámetros**

- `filename` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 2: Any p1
```

**Nombres antiguos (alias):** `0x83BCCE3224735F05` (`N_0x83bcce3224735f05`)

---
### DatafileStoreMissionHeader

`DATAFILE_STORE_MISSION_HEADER` · hash `0x2ED61456317B8178` · jhash `0x4E03F632` · **Cliente**

```lua
DatafileStoreMissionHeader()
```
```c
void DATAFILE_STORE_MISSION_HEADER();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
```

**Nombres antiguos (alias):** `0x2ED61456317B8178` (`N_0x2ed61456317b8178`)

---
### DatafileUpdateSaveToCloud

`DATAFILE_UPDATE_SAVE_TO_CLOUD` · hash `0x4DFDD9EB705F8140` · jhash `0x0B4087F7` · **Cliente**

```lua
local retval, p0 = DatafileUpdateSaveToCloud(p0)
```
```c
BOOL DATAFILE_UPDATE_SAVE_TO_CLOUD(BOOL* p0);
```

**Parámetros**

- `p0` (`BOOL*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x4DFDD9EB705F8140` (`N_0x4dfdd9eb705f8140`)

---
### DatafileWatchRequestId

`DATAFILE_WATCH_REQUEST_ID` · hash `0xAD6875BBC0FC899C` · jhash `0x621388FF` · **Cliente**

```lua
DatafileWatchRequestId(id)
```
```c
void DATAFILE_WATCH_REQUEST_ID(int id);
```

**Parámetros**

- `id` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Adds the given request ID to the watch list.
```

**Nombres antiguos (alias):** `0xAD6875BBC0FC899C` (`N_0xad6875bbc0fc899c`)

---
### N_0x6ad0bd5e087866cb

`0x6AD0BD5E087866CB` · hash `0x6AD0BD5E087866CB` · **Cliente**

```lua
N_0x6ad0bd5e087866cb(p0)
```
```c
void 0x6AD0BD5E087866CB(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xa6eef01087181edd

`0xA6EEF01087181EDD` · hash `0xA6EEF01087181EDD` · **Cliente**

```lua
local retval = N_0xa6eef01087181edd(p0, p1)
```
```c
Any 0xA6EEF01087181EDD(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### N_0xdbf860cf1db8e599

`0xDBF860CF1DB8E599` · hash `0xDBF860CF1DB8E599` · **Cliente**

```lua
local retval = N_0xdbf860cf1db8e599(p0)
```
```c
Any 0xDBF860CF1DB8E599(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

---
### UgcCreateContent

`UGC_CREATE_CONTENT` · hash `0xC84527E235FCA219` · jhash `0xF09157B0` · **Cliente**

```lua
local retval = UgcCreateContent(data, dataCount, contentName, description, tagsCsv, contentTypeName, publish)
```
```c
BOOL UGC_CREATE_CONTENT(char* data, int dataCount, char* contentName, char* description, char* tagsCsv, char* contentTypeName, BOOL publish);
```

**Parámetros**

- `data` (`char*`)
- `dataCount` (`int`)
- `contentName` (`char*`)
- `description` (`char*`)
- `tagsCsv` (`char*`)
- `contentTypeName` (`char*`)
- `publish` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 8: Any p7
```

**Nombres antiguos (alias):** `0xC84527E235FCA219` (`N_0xc84527e235fca219`)

---
### UgcCreateMission

`UGC_CREATE_MISSION` · hash `0xA5EFC3E847D60507` · jhash `0xD96860FC` · **Cliente**

```lua
local retval = UgcCreateMission(contentName, description, tagsCsv, contentTypeName, publish)
```
```c
BOOL UGC_CREATE_MISSION(char* contentName, char* description, char* tagsCsv, char* contentTypeName, BOOL publish);
```

**Parámetros**

- `contentName` (`char*`)
- `description` (`char*`)
- `tagsCsv` (`char*`)
- `contentTypeName` (`char*`)
- `publish` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 6: Any p5
```

**Nombres antiguos (alias):** `0xA5EFC3E847D60507` (`N_0xa5efc3e847d60507`)

---
### UgcSetPlayerData

`UGC_SET_PLAYER_DATA` · hash `0x692D808C34A82143` · jhash `0xBB6321BD` · **Cliente**

```lua
local retval = UgcSetPlayerData(contentId, rating, contentTypeName)
```
```c
BOOL UGC_SET_PLAYER_DATA(char* contentId, float rating, char* contentTypeName);
```

**Parámetros**

- `contentId` (`char*`)
- `rating` (`float`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 4: Any p3
```

**Nombres antiguos (alias):** `0x692D808C34A82143` (`N_0x692d808c34a82143`)

---
### UgcUpdateContent

`UGC_UPDATE_CONTENT` · hash `0x648E7A5434AF7969` · jhash `0x459F2683` · **Cliente**

```lua
local retval, data = UgcUpdateContent(contentId, dataCount, contentName, description, tagsCsv, contentTypeName)
```
```c
BOOL UGC_UPDATE_CONTENT(char* contentId, Any* data, int dataCount, char* contentName, char* description, char* tagsCsv, char* contentTypeName);
```

**Parámetros**

- `contentId` (`char*`)
- `data` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `dataCount` (`int`)
- `contentName` (`char*`)
- `description` (`char*`)
- `tagsCsv` (`char*`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 8: Any p7
```

**Nombres antiguos (alias):** `0x648E7A5434AF7969` (`N_0x648e7a5434af7969`)

---
### UgcUpdateMission

`UGC_UPDATE_MISSION` · hash `0x4645DE9980999E93` · jhash `0xDBB83E2B` · **Cliente**

```lua
local retval = UgcUpdateMission(contentId, contentName, description, tagsCsv, contentTypeName)
```
```c
BOOL UGC_UPDATE_MISSION(char* contentId, char* contentName, char* description, char* tagsCsv, char* contentTypeName);
```

**Parámetros**

- `contentId` (`char*`)
- `contentName` (`char*`)
- `description` (`char*`)
- `tagsCsv` (`char*`)
- `contentTypeName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 6: Any p5
```

**Nombres antiguos (alias):** `0x4645DE9980999E93` (`N_0x4645de9980999e93`)

---
