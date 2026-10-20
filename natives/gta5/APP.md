# Natives de GTA V — APP

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `APP`: **17** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AppClearBlock`](#appclearblock) · [`AppCloseApp`](#appcloseapp) · [`AppCloseBlock`](#appcloseblock) · [`AppDataValid`](#appdatavalid) · [`AppDeleteAppData`](#appdeleteappdata) · [`AppGetDeletedFileStatus`](#appgetdeletedfilestatus) · [`AppGetFloat`](#appgetfloat) · [`AppGetInt`](#appgetint) · [`AppGetString`](#appgetstring) · [`AppHasLinkedSocialClubAccount`](#apphaslinkedsocialclubaccount) · [`AppHasSyncedData`](#apphassynceddata) · [`AppSaveData`](#appsavedata) · [`AppSetApp`](#appsetapp) · [`AppSetBlock`](#appsetblock) · [`AppSetFloat`](#appsetfloat) · [`AppSetInt`](#appsetint) · [`AppSetString`](#appsetstring)

---
### AppClearBlock

`APP_CLEAR_BLOCK` · hash `0x5FE1DF3342DB7DBA` · jhash `0xDAB86A18` · **Cliente**

```lua
AppClearBlock()
```
```c
void APP_CLEAR_BLOCK();
```

**Devuelve:** `void`

---
### AppCloseApp

`APP_CLOSE_APP` · hash `0xE41C65E07A5F05FC` · jhash `0x03767C7A` · **Cliente**

```lua
AppCloseApp()
```
```c
void APP_CLOSE_APP();
```

**Devuelve:** `void`

---
### AppCloseBlock

`APP_CLOSE_BLOCK` · hash `0xE8E3FCF72EAC0EF8` · jhash `0xED97B202` · **Cliente**

```lua
AppCloseBlock()
```
```c
void APP_CLOSE_BLOCK();
```

**Devuelve:** `void`

---
### AppDataValid

`APP_DATA_VALID` · hash `0x846AA8E7D55EE5B6` · jhash `0x72BDE002` · **Cliente**

```lua
local retval = AppDataValid()
```
```c
BOOL APP_DATA_VALID();
```

**Devuelve:** `BOOL`

---
### AppDeleteAppData

`APP_DELETE_APP_DATA` · hash `0x44151AEA95C8A003` · jhash `0x2A2FBD1C` · **Cliente**

```lua
local retval = AppDeleteAppData(appName)
```
```c
BOOL APP_DELETE_APP_DATA(char* appName);
```

**Parámetros**

- `appName` (`char*`)

**Devuelve:** `BOOL`

---
### AppGetDeletedFileStatus

`APP_GET_DELETED_FILE_STATUS` · hash `0xC9853A2BE3DED1A6` · jhash `0x784D550B` · **Cliente**

```lua
local retval = AppGetDeletedFileStatus()
```
```c
int APP_GET_DELETED_FILE_STATUS();
```

**Devuelve:** `int`

---
### AppGetFloat

`APP_GET_FLOAT` · hash `0x1514FB24C02C2322` · jhash `0xD87F3A1C` · **Cliente**

```lua
local retval = AppGetFloat(property)
```
```c
float APP_GET_FLOAT(char* property);
```

**Parámetros**

- `property` (`char*`)

**Devuelve:** `float`

---
### AppGetInt

`APP_GET_INT` · hash `0xD3A58A12C77D9D4B` · jhash `0x2942AAD2` · **Cliente**

```lua
local retval = AppGetInt(property)
```
```c
int APP_GET_INT(char* property);
```

**Parámetros**

- `property` (`char*`)

**Devuelve:** `int`

---
### AppGetString

`APP_GET_STRING` · hash `0x749B023950D2311C` · jhash `0x849CEB80` · **Cliente**

```lua
local retval = AppGetString(property)
```
```c
char* APP_GET_STRING(char* property);
```

**Parámetros**

- `property` (`char*`)

**Devuelve:** `char*`

---
### AppHasLinkedSocialClubAccount

`APP_HAS_LINKED_SOCIAL_CLUB_ACCOUNT` · hash `0x71EEE69745088DA0` · jhash `0xD368BA15` · **Cliente**

```lua
local retval = AppHasLinkedSocialClubAccount()
```
```c
BOOL APP_HAS_LINKED_SOCIAL_CLUB_ACCOUNT();
```

**Devuelve:** `BOOL`

---
### AppHasSyncedData

`APP_HAS_SYNCED_DATA` · hash `0xCA52279A7271517F` · jhash `0x1DE2A63D` · **Cliente**

```lua
local retval = AppHasSyncedData(appName)
```
```c
BOOL APP_HAS_SYNCED_DATA(char* appName);
```

**Parámetros**

- `appName` (`char*`)

**Devuelve:** `BOOL`

---
### AppSaveData

`APP_SAVE_DATA` · hash `0x95C5D356CDA6E85F` · jhash `0x84A3918D` · **Cliente**

```lua
AppSaveData()
```
```c
void APP_SAVE_DATA();
```

**Devuelve:** `void`

---
### AppSetApp

`APP_SET_APP` · hash `0xCFD0406ADAF90D2B` · jhash `0x8BAC4146` · **Cliente**

```lua
AppSetApp(appName)
```
```c
void APP_SET_APP(char* appName);
```

**Parámetros**

- `appName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Called in the gamescripts like:  
APP::APP_SET_APP("car");  
APP::APP_SET_APP("dog");  
```

---
### AppSetBlock

`APP_SET_BLOCK` · hash `0x262AB456A3D21F93` · jhash `0xC2D54DD9` · **Cliente**

```lua
AppSetBlock(blockName)
```
```c
void APP_SET_BLOCK(char* blockName);
```

**Parámetros**

- `blockName` (`char*`)

**Devuelve:** `void`

---
### AppSetFloat

`APP_SET_FLOAT` · hash `0x25D7687C68E0DAA4` · jhash `0xF3076135` · **Cliente**

```lua
AppSetFloat(property, value)
```
```c
void APP_SET_FLOAT(char* property, float value);
```

**Parámetros**

- `property` (`char*`)
- `value` (`float`)

**Devuelve:** `void`

---
### AppSetInt

`APP_SET_INT` · hash `0x607E8E3D3E4F9611` · jhash `0x1B509C32` · **Cliente**

```lua
AppSetInt(property, value)
```
```c
void APP_SET_INT(char* property, int value);
```

**Parámetros**

- `property` (`char*`)
- `value` (`int`)

**Devuelve:** `void`

---
### AppSetString

`APP_SET_STRING` · hash `0x3FF2FCEC4B7721B4` · jhash `0x23DF19A8` · **Cliente**

```lua
AppSetString(property, value)
```
```c
void APP_SET_STRING(char* property, char* value);
```

**Parámetros**

- `property` (`char*`)
- `value` (`char*`)

**Devuelve:** `void`

---
