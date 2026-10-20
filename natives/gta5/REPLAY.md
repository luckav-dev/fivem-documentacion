# Natives de GTA V — REPLAY

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `REPLAY`: **6** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ActivateRockstarEditor`](#activaterockstareditor) · [`IsInteriorRenderingDisabled`](#isinteriorrenderingdisabled) · [`N_0x5ad3932daeb1e5d3`](#n_0x5ad3932daeb1e5d3) · [`N_0x7e2bd3ef6c205f09`](#n_0x7e2bd3ef6c205f09) · [`N_0xe058175f8eafe79a`](#n_0xe058175f8eafe79a) · [`ResetEditorValues`](#reseteditorvalues)

---
### ActivateRockstarEditor

`_ACTIVATE_ROCKSTAR_EDITOR` · hash `0x49DA8145672B2725` · **Cliente**

```lua
ActivateRockstarEditor()
```
```c
void _ACTIVATE_ROCKSTAR_EDITOR();
```

**Devuelve:** `void`

**Descripción oficial:**

Please note that you will need to call DO_SCREEN_FADE_IN after exiting the Rockstar Editor when you call this.

```
NativeDB Added Parameter 1: int p0
```

**Nombres antiguos (alias):** `0x49DA8145672B2725` (`N_0x49da8145672b2725`)

---
### IsInteriorRenderingDisabled

`_IS_INTERIOR_RENDERING_DISABLED` · hash `0x95AB8B5C992C7B58` · **Cliente**

```lua
local retval = IsInteriorRenderingDisabled()
```
```c
BOOL _IS_INTERIOR_RENDERING_DISABLED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns a bool if interior rendering is disabled, if yes, all "normal" rendered interiors are invisible  
```

---
### N_0x5ad3932daeb1e5d3

`0x5AD3932DAEB1E5D3` · hash `0x5AD3932DAEB1E5D3` · **Cliente**

```lua
N_0x5ad3932daeb1e5d3()
```
```c
void 0x5AD3932DAEB1E5D3();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Disables some other rendering (internal)  
```

---
### N_0x7e2bd3ef6c205f09

`0x7E2BD3EF6C205F09` · hash `0x7E2BD3EF6C205F09` · **Cliente**

```lua
N_0x7e2bd3ef6c205f09(p0, p1)
```
```c
void 0x7E2BD3EF6C205F09(char* p0, BOOL p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

**This native does absolutely nothing, just a nullsub**

```
Something to do with phone cameras.  
startup.c4:  
void sub_2a3d() {  
    UNK2::_7E2BD3EF6C205F09("No_Filter", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam1", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam2", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam3", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam4", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam5", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam6", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam7", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam9", 1);  
    UNK2::_7E2BD3EF6C205F09("phone_cam12", 0);  
}  
```

---
### N_0xe058175f8eafe79a

`0xE058175F8EAFE79A` · hash `0xE058175F8EAFE79A` · **Cliente**

```lua
N_0xe058175f8eafe79a(p0)
```
```c
void 0xE058175F8EAFE79A(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### ResetEditorValues

`_RESET_EDITOR_VALUES` · hash `0x3353D13F09307691` · **Cliente**

```lua
ResetEditorValues()
```
```c
void _RESET_EDITOR_VALUES();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Sets (almost, not sure) all Rockstar Editor values (bIsRecording etc) to 0.  
```

**Nombres antiguos (alias):** `0x3353D13F09307691` (`N_0x3353d13f09307691`)

---
