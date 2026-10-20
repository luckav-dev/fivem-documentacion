# Natives de GTA V — ITEMSET

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `ITEMSET`: **9** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddToItemset`](#addtoitemset) · [`CleanItemset`](#cleanitemset) · [`CreateItemset`](#createitemset) · [`DestroyItemset`](#destroyitemset) · [`GetIndexedItemInItemset`](#getindexediteminitemset) · [`GetItemsetSize`](#getitemsetsize) · [`IsInItemset`](#isinitemset) · [`IsItemsetValid`](#isitemsetvalid) · [`RemoveFromItemset`](#removefromitemset)

---
### AddToItemset

`ADD_TO_ITEMSET` · hash `0xE3945201F14637DD` · jhash `0x6B0FE61B` · **Cliente**

```lua
local retval = AddToItemset(p0, p1)
```
```c
BOOL ADD_TO_ITEMSET(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `BOOL`

---
### CleanItemset

`CLEAN_ITEMSET` · hash `0x41BC0D722FC04221` · jhash `0x919A4858` · **Cliente**

```lua
CleanItemset(p0)
```
```c
void CLEAN_ITEMSET(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### CreateItemset

`CREATE_ITEMSET` · hash `0x35AD299F50D91B24` · jhash `0x0A113B2C` · **Cliente**

```lua
local retval = CreateItemset(distri)
```
```c
Vehicle CREATE_ITEMSET(BOOL distri);
```

**Parámetros**

- `distri` (`BOOL`)

**Devuelve:** `Vehicle`

---
### DestroyItemset

`DESTROY_ITEMSET` · hash `0xDE18220B1C183EDA` · jhash `0x83CE1A4C` · **Cliente**

```lua
DestroyItemset(p0)
```
```c
void DESTROY_ITEMSET(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### GetIndexedItemInItemset

`GET_INDEXED_ITEM_IN_ITEMSET` · hash `0x7A197E2521EE2BAB` · jhash `0x3F712874` · **Cliente**

```lua
local retval = GetIndexedItemInItemset(p0, p1)
```
```c
Any GET_INDEXED_ITEM_IN_ITEMSET(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `Any`

---
### GetItemsetSize

`GET_ITEMSET_SIZE` · hash `0xD9127E83ABF7C631` · jhash `0x2B31F41A` · **Cliente**

```lua
local retval = GetItemsetSize(x)
```
```c
Any GET_ITEMSET_SIZE(ScrHandle x);
```

**Parámetros**

- `x` (`ScrHandle`)

**Devuelve:** `Any`

---
### IsInItemset

`IS_IN_ITEMSET` · hash `0x2D0FC594D1E9C107` · jhash `0x0D4B9730` · **Cliente**

```lua
local retval = IsInItemset(p0, p1)
```
```c
BOOL IS_IN_ITEMSET(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `BOOL`

---
### IsItemsetValid

`IS_ITEMSET_VALID` · hash `0xB1B1EA596344DFAB` · jhash `0xD201FC29` · **Cliente**

```lua
local retval = IsItemsetValid(p0)
```
```c
BOOL IS_ITEMSET_VALID(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### RemoveFromItemset

`REMOVE_FROM_ITEMSET` · hash `0x25E68244B0177686` · jhash `0xA9565228` · **Cliente**

```lua
RemoveFromItemset(p0, p1)
```
```c
void REMOVE_FROM_ITEMSET(Any p0, Any p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)

**Devuelve:** `void`

---
