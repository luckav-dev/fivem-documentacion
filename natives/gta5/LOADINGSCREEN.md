# Natives de GTA V — LOADINGSCREEN

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `LOADINGSCREEN`: **8** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`LoadingscreenGetLoadFreemode`](#loadingscreengetloadfreemode) · [`LoadingscreenGetLoadFreemodeWithEventName`](#loadingscreengetloadfreemodewitheventname) · [`LoadingscreenIsLoadingFreemode`](#loadingscreenisloadingfreemode) · [`LoadingscreenSetIsLoadingFreemode`](#loadingscreensetisloadingfreemode) · [`LoadingscreenSetLoadFreemode`](#loadingscreensetloadfreemode) · [`LoadingscreenSetLoadFreemodeWithEventName`](#loadingscreensetloadfreemodewitheventname) · [`N_0xf2ca003f167e21d2`](#n_0xf2ca003f167e21d2) · [`N_0xfa1e0e893d915215`](#n_0xfa1e0e893d915215)

---
### LoadingscreenGetLoadFreemode

`_LOADINGSCREEN_GET_LOAD_FREEMODE` · hash `0xEF7D17BC6C85264C` · jhash `0xD87F3A9E` · **Cliente**

```lua
local retval = LoadingscreenGetLoadFreemode()
```
```c
BOOL _LOADINGSCREEN_GET_LOAD_FREEMODE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEF7D17BC6C85264C` (`N_0xef7d17bc6c85264c`)

---
### LoadingscreenGetLoadFreemodeWithEventName

`_LOADINGSCREEN_GET_LOAD_FREEMODE_WITH_EVENT_NAME` · hash `0x8AA464D4E0F6ACCD` · jhash `0x94BCAC7C` · **Cliente**

```lua
local retval = LoadingscreenGetLoadFreemodeWithEventName()
```
```c
BOOL _LOADINGSCREEN_GET_LOAD_FREEMODE_WITH_EVENT_NAME();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8AA464D4E0F6ACCD` (`N_0x8aa464d4e0f6accd`)

---
### LoadingscreenIsLoadingFreemode

`_LOADINGSCREEN_IS_LOADING_FREEMODE` · hash `0xC6DC823253FBB366` · jhash `0x734CFEDA` · **Cliente**

```lua
local retval = LoadingscreenIsLoadingFreemode()
```
```c
BOOL _LOADINGSCREEN_IS_LOADING_FREEMODE();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC6DC823253FBB366` (`N_0xc6dc823253fbb366`), `_IS_UI_LOADING_MULTIPLAYER` (`IsUiLoadingMultiplayer`)

---
### LoadingscreenSetIsLoadingFreemode

`_LOADINGSCREEN_SET_IS_LOADING_FREEMODE` · hash `0xC7E7181C09F33B69` · jhash `0x8C227332` · **Cliente**

```lua
LoadingscreenSetIsLoadingFreemode(toggle)
```
```c
void _LOADINGSCREEN_SET_IS_LOADING_FREEMODE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xC7E7181C09F33B69` (`N_0xc7e7181c09f33b69`)

---
### LoadingscreenSetLoadFreemode

`_LOADINGSCREEN_SET_LOAD_FREEMODE` · hash `0xB0C56BD3D808D863` · jhash `0xC0B971EA` · **Cliente**

```lua
LoadingscreenSetLoadFreemode(toggle)
```
```c
void _LOADINGSCREEN_SET_LOAD_FREEMODE(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `_GET_BROADCAST_FINSHED_LOS_SOUND` (`GetBroadcastFinshedLosSound`), `0xB0C56BD3D808D863` (`N_0xb0c56bd3d808d863`)

---
### LoadingscreenSetLoadFreemodeWithEventName

`_LOADINGSCREEN_SET_LOAD_FREEMODE_WITH_EVENT_NAME` · hash `0xFC309E94546FCDB5` · jhash `0x7D90EEE5` · **Cliente**

```lua
LoadingscreenSetLoadFreemodeWithEventName(toggle)
```
```c
void _LOADINGSCREEN_SET_LOAD_FREEMODE_WITH_EVENT_NAME(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only occurrence was false, in maintransition.  
```

**Nombres antiguos (alias):** `0xFC309E94546FCDB5` (`N_0xfc309e94546fcdb5`), `_IS_IN_LOADING_SCREEN` (`IsInLoadingScreen`)

---
### N_0xf2ca003f167e21d2

`0xF2CA003F167E21D2` · hash `0xF2CA003F167E21D2` · jhash `0x106C8317` · **Cliente**

```lua
local retval = N_0xf2ca003f167e21d2()
```
```c
int 0xF2CA003F167E21D2();
```

**Devuelve:** `int` — Hard-coded to always return 0.

**Nombres antiguos (alias):** `_RETURN_ZERO` (`ReturnZero`)

---
### N_0xfa1e0e893d915215

`0xFA1E0E893D915215` · hash `0xFA1E0E893D915215` · jhash `0x5C350D78` · **Cliente**

```lua
N_0xfa1e0e893d915215(toggle)
```
```c
void 0xFA1E0E893D915215(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
