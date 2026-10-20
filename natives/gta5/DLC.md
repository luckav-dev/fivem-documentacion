# Natives de GTA V — DLC

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `DLC`: **11** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`GetExtraContentPackHasBeenInstalled`](#getextracontentpackhasbeeninstalled) · [`GetIsLoadingScreenActive`](#getisloadingscreenactive) · [`HasCloudRequestsFinished`](#hascloudrequestsfinished) · [`IsDlcPresent`](#isdlcpresent) · [`N_0x241fca5b1aa14f75`](#n_0x241fca5b1aa14f75) · [`N_0x9489659372a81585`](#n_0x9489659372a81585) · [`N_0xa213b11dff526300`](#n_0xa213b11dff526300) · [`N_0xc4637a6d03c24cc3`](#n_0xc4637a6d03c24cc3) · [`N_0xf2e07819ef1a5289`](#n_0xf2e07819ef1a5289) · [`OnEnterMp`](#onentermp) · [`OnEnterSp`](#onentersp)

---
### GetExtraContentPackHasBeenInstalled

`_GET_EXTRA_CONTENT_PACK_HAS_BEEN_INSTALLED` · hash `0x8D30F648014A92B5` · jhash `0xF69B729C` · **Cliente**

```lua
local retval = GetExtraContentPackHasBeenInstalled()
```
```c
BOOL _GET_EXTRA_CONTENT_PACK_HAS_BEEN_INSTALLED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x8D30F648014A92B5` (`N_0x8d30f648014a92b5`)

---
### GetIsLoadingScreenActive

`GET_IS_LOADING_SCREEN_ACTIVE` · hash `0x10D0A8F259E93EC9` · jhash `0x517B601B` · **Cliente**

```lua
local retval = GetIsLoadingScreenActive()
```
```c
BOOL GET_IS_LOADING_SCREEN_ACTIVE();
```

**Devuelve:** `BOOL` — Wether the player is still in the loadingscreen

**Descripción oficial:**

When loading in, returns true until [`SHUTDOWN_LOADING_SCREEN`](SCRIPT.md#shutdownloadingscreen) was called. Note that this is referring to the game's loading screen, not the NUI loadingscreen and is therefore not impacted by [loadscreen_manual_shutdown](https://docs.fivem.net/docs/scripting-reference/resource-manifest/#loadscreen_manual_shutdown).

**Ejemplo (lua):**

```lua
-- Close the loading screen if it's still active
if GetIsLoadingScreenActive() then
    ShutdownLoadingScreen()
end
```

---
### HasCloudRequestsFinished

`HAS_CLOUD_REQUESTS_FINISHED` · hash `0x46E2B844905BC5F0` · jhash `0x6087C10C` · **Cliente**

```lua
local retval, variable = HasCloudRequestsFinished(unused)
```
```c
BOOL HAS_CLOUD_REQUESTS_FINISHED(BOOL* variable, Any unused);
```

**Parámetros**

- `variable` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `unused` (`Any`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Sets the value of the specified variable to 0.
Always returns true.
```

**Nombres antiguos (alias):** `_NULLIFY` (`Nullify`)

---
### IsDlcPresent

`IS_DLC_PRESENT` · hash `0x812595A0644CE1DE` · jhash `0x1F321943` · **Cliente**

```lua
local retval = IsDlcPresent(dlcHash)
```
```c
BOOL IS_DLC_PRESENT(Hash dlcHash);
```

**Parámetros**

- `dlcHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Example:
DLC::IS_DLC_PRESENT($\mpbusiness2\);
($ = gethashkey)
bruteforce these:
0xB119F6D
0x96F02EE6
```

---
### N_0x241fca5b1aa14f75

`0x241FCA5B1AA14F75` · hash `0x241FCA5B1AA14F75` · jhash `0x0AF83036` · **Cliente**

```lua
local retval = N_0x241fca5b1aa14f75()
```
```c
BOOL 0x241FCA5B1AA14F75();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Only used once in scripts, in maintransition.
maintransition.c4, line ~82432:
if (PED::_7350823473013C02(PLAYER::PLAYER_PED_ID()) && (DECORATOR::_241FCA5B1AA14F75() == 0)) {
    g_2542A5 = a_1; // 'g_2542A5' used in 'building_controller.ysc' for IPL stuff?
    return 1;
}
Likely used solely for the players ped. The function it's in seems to only be used for initialization/quitting. Called among natives to discard scaleforms, disable frontend, fading in/out, etc. Neighboring strings to some calls include "HUD_JOINING", "HUD_QUITTING".
Most likely ARE_*
```

---
### N_0x9489659372a81585

`0x9489659372A81585` · hash `0x9489659372A81585` · jhash `0xC2169164` · **Cliente**

```lua
local retval = N_0x9489659372a81585()
```
```c
BOOL 0x9489659372A81585();
```

**Devuelve:** `BOOL` — Hard-coded to always return 0.

---
### N_0xa213b11dff526300

`0xA213B11DFF526300` · hash `0xA213B11DFF526300` · jhash `0xF79A97F5` · **Cliente**

```lua
local retval = N_0xa213b11dff526300()
```
```c
BOOL 0xA213B11DFF526300();
```

**Devuelve:** `BOOL` — Hard-coded to always return 1.

---
### N_0xc4637a6d03c24cc3

`0xC4637A6D03C24CC3` · hash `0xC4637A6D03C24CC3` · **Cliente**

```lua
local retval = N_0xc4637a6d03c24cc3()
```
```c
BOOL 0xC4637A6D03C24CC3();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

GET_IS_LOADING_\*

```
NativeDB Introduced: v1734
```

---
### N_0xf2e07819ef1a5289

`0xF2E07819EF1A5289` · hash `0xF2E07819EF1A5289` · jhash `0x881B1FDB` · **Cliente**

```lua
local retval = N_0xf2e07819ef1a5289()
```
```c
BOOL 0xF2E07819EF1A5289();
```

**Devuelve:** `BOOL` — Hard-coded to always return 1.

---
### OnEnterMp

`ON_ENTER_MP` · hash `0x0888C3502DBBEEF5` · jhash `0xC65586A9` · **Cliente**

```lua
OnEnterMp()
```
```c
void ON_ENTER_MP();
```

**Devuelve:** `void`

**Descripción oficial:**

```
This loads the GTA:O dlc map parts (high end garages, apartments).
Works in singleplayer.
In order to use GTA:O heist IPL's you have to call this native with the following params: SET_INSTANCE_PRIORITY_MODE(1);
```

**Nombres antiguos (alias):** `_LOAD_MP_DLC_MAPS` (`LoadMpDlcMaps`)

---
### OnEnterSp

`ON_ENTER_SP` · hash `0xD7C10C4A637992C9` · jhash `0x8BF60FC3` · **Cliente**

```lua
OnEnterSp()
```
```c
void ON_ENTER_SP();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Unloads GROUP_MAP (GTAO/MP) DLC data and loads GROUP_MAP_SP DLC. Neither are loaded by default, 0888C3502DBBEEF5 is a cognate to this function and loads MP DLC (and unloads SP DLC by extension).
The original (and wrong) definition is below:
This unload the GTA:O DLC map parts (like high end garages/apartments).
Works in singleplayer.
```

**Nombres antiguos (alias):** `0xD7C10C4A637992C9` (`N_0xd7c10c4a637992c9`), `_LOAD_SP_DLC_MAPS` (`LoadSpDlcMaps`)

---
