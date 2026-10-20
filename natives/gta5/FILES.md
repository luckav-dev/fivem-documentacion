# Natives de GTA V — FILES

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `FILES`: **47** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`DoesShopPedApparelHaveRestrictionTag`](#doesshoppedapparelhaverestrictiontag) · [`GetDlcVehicleData`](#getdlcvehicledata) · [`GetDlcVehicleFlags`](#getdlcvehicleflags) · [`GetDlcVehicleModLockHash`](#getdlcvehiclemodlockhash) · [`GetDlcVehicleModel`](#getdlcvehiclemodel) · [`GetDlcWeaponComponentData`](#getdlcweaponcomponentdata) · [`GetDlcWeaponComponentDataSp`](#getdlcweaponcomponentdatasp) · [`GetDlcWeaponData`](#getdlcweapondata) · [`GetDlcWeaponDataSp`](#getdlcweapondatasp) · [`GetForcedComponent`](#getforcedcomponent) · [`GetForcedProp`](#getforcedprop) · [`GetHashNameForComponent`](#gethashnameforcomponent) · [`GetHashNameForProp`](#gethashnameforprop) · [`GetNumDlcVehicles`](#getnumdlcvehicles) · [`GetNumDlcWeaponComponents`](#getnumdlcweaponcomponents) · [`GetNumDlcWeaponComponentsSp`](#getnumdlcweaponcomponentssp) · [`GetNumDlcWeapons`](#getnumdlcweapons) · [`GetNumDlcWeaponsSp`](#getnumdlcweaponssp) · [`GetNumTattooShopDlcItems`](#getnumtattooshopdlcitems) · [`GetShopPedApparelForcedComponentCount`](#getshoppedapparelforcedcomponentcount) · [`GetShopPedApparelForcedPropCount`](#getshoppedapparelforcedpropcount) · [`GetShopPedApparelVariantComponentCount`](#getshoppedapparelvariantcomponentcount) · [`GetShopPedApparelVariantPropCount`](#getshoppedapparelvariantpropcount) · [`GetShopPedComponent`](#getshoppedcomponent) · [`GetShopPedOutfit`](#getshoppedoutfit) · [`GetShopPedOutfitComponentVariant`](#getshoppedoutfitcomponentvariant) · [`GetShopPedOutfitLocate`](#getshoppedoutfitlocate) · [`GetShopPedOutfitPropVariant`](#getshoppedoutfitpropvariant) · [`GetShopPedProp`](#getshoppedprop) · [`GetShopPedQueryComponent`](#getshoppedquerycomponent) · [`GetShopPedQueryOutfit`](#getshoppedqueryoutfit) · [`GetShopPedQueryProp`](#getshoppedqueryprop) · [`GetTattooShopDlcItemData`](#gettattooshopdlcitemdata) · [`GetTattooShopDlcItemIndex`](#gettattooshopdlcitemindex) · [`GetVariantComponent`](#getvariantcomponent) · [`GetVariantProp`](#getvariantprop) · [`InitShopPedComponent`](#initshoppedcomponent) · [`InitShopPedProp`](#initshoppedprop) · [`IsContentItemLocked`](#iscontentitemlocked) · [`IsDlcVehicleMod`](#isdlcvehiclemod) · [`LoadContentChangeSetGroup`](#loadcontentchangesetgroup) · [`N_0x6cebe002e58dee97`](#n_0x6cebe002e58dee97) · [`N_0x96e2929292a4db77`](#n_0x96e2929292a4db77) · [`SetupShopPedApparelQuery`](#setupshoppedapparelquery) · [`SetupShopPedApparelQueryTu`](#setupshoppedapparelquerytu) · [`SetupShopPedOutfitQuery`](#setupshoppedoutfitquery) · [`UnloadContentChangeSetGroup`](#unloadcontentchangesetgroup)

---
### DoesShopPedApparelHaveRestrictionTag

`DOES_SHOP_PED_APPAREL_HAVE_RESTRICTION_TAG` · hash `0x341DE7ED1D2A1BFD` · jhash `0x8E2C7FD5` · **Cliente**

```lua
local retval = DoesShopPedApparelHaveRestrictionTag(componentHash, restrictionTagHash, componentId)
```
```c
BOOL DOES_SHOP_PED_APPAREL_HAVE_RESTRICTION_TAG(Hash componentHash, Hash restrictionTagHash, int componentId);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `restrictionTagHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `componentId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x341DE7ED1D2A1BFD` (`N_0x341de7ed1d2a1bfd`)

---
### GetDlcVehicleData

`GET_DLC_VEHICLE_DATA` · hash `0x33468EDC08E371F6` · jhash `0xCF428FA4` · **Cliente**

```lua
local retval, outData = GetDlcVehicleData(dlcVehicleIndex, outData)
```
```c
BOOL GET_DLC_VEHICLE_DATA(int dlcVehicleIndex, Any* outData);
```

**Parámetros**

- `dlcVehicleIndex` (`int`): takes a number from 0 to `GET_NUM_DLC_VEHICLES()` - 1.
- `outData` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: a struct of 3 8-byte items.

**Devuelve:** `BOOL` — A boolean value return if find or not the dlcVehicleIndex.

**Descripción oficial:**

The Second item in the struct `*(Hash *)(outData + 1)` is the vehicle hash.

---
### GetDlcVehicleFlags

`GET_DLC_VEHICLE_FLAGS` · hash `0x5549EE11FA22FCF2` · jhash `0xAB12738C` · **Cliente**

```lua
local retval = GetDlcVehicleFlags(dlcVehicleIndex)
```
```c
int GET_DLC_VEHICLE_FLAGS(int dlcVehicleIndex);
```

**Parámetros**

- `dlcVehicleIndex` (`int`)

**Devuelve:** `int`

---
### GetDlcVehicleModLockHash

`GET_DLC_VEHICLE_MOD_LOCK_HASH` · hash `0xC098810437312FFF` · jhash `0x59352658` · **Cliente**

```lua
local retval = GetDlcVehicleModLockHash(hash)
```
```c
Hash GET_DLC_VEHICLE_MOD_LOCK_HASH(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0xC098810437312FFF` (`N_0xc098810437312fff`)

---
### GetDlcVehicleModel

`GET_DLC_VEHICLE_MODEL` · hash `0xECC01B7C5763333C` · jhash `0xA2201E09` · **Cliente**

```lua
local retval = GetDlcVehicleModel(dlcVehicleIndex)
```
```c
Hash GET_DLC_VEHICLE_MODEL(int dlcVehicleIndex);
```

**Parámetros**

- `dlcVehicleIndex` (`int`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
dlcVehicleIndex is 0 to GET_NUM_DLC_VEHICLS()  
```

---
### GetDlcWeaponComponentData

`GET_DLC_WEAPON_COMPONENT_DATA` · hash `0x6CF598A2957C2BF8` · jhash `0x4B83FCAF` · **Cliente**

```lua
local retval, ComponentDataPtr = GetDlcWeaponComponentData(dlcWeaponIndex, dlcWeapCompIndex, ComponentDataPtr)
```
```c
BOOL GET_DLC_WEAPON_COMPONENT_DATA(int dlcWeaponIndex, int dlcWeapCompIndex, int* ComponentDataPtr);
```

**Parámetros**

- `dlcWeaponIndex` (`int`)
- `dlcWeapCompIndex` (`int`)
- `ComponentDataPtr` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
p0 seems to be the weapon index  
p1 seems to be the weapon component index  
struct DlcComponentData{  
int attachBone;  
int padding1;  
int bActiveByDefault;  
int padding2;  
int unk;  
int padding3;  
int componentHash;  
int padding4;  
int unk2;  
int padding5;  
int componentCost;  
int padding6;  
char nameLabel[64];  
char descLabel[64];  
};  
```

---
### GetDlcWeaponComponentDataSp

`_GET_DLC_WEAPON_COMPONENT_DATA_SP` · hash `0x31D5E073B6F93CDC` · **Cliente**

```lua
local retval, ComponentDataPtr = GetDlcWeaponComponentDataSp(dlcWeaponIndex, dlcWeapCompIndex, ComponentDataPtr)
```
```c
BOOL _GET_DLC_WEAPON_COMPONENT_DATA_SP(int dlcWeaponIndex, int dlcWeapCompIndex, int* ComponentDataPtr);
```

**Parámetros**

- `dlcWeaponIndex` (`int`)
- `dlcWeapCompIndex` (`int`)
- `ComponentDataPtr` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Same as GET_DLC_WEAPON_COMPONENT_DATA but only works for DLC components that are available in SP.

```
NativeDB Introduced: v2060
```

---
### GetDlcWeaponData

`GET_DLC_WEAPON_DATA` · hash `0x79923CD21BECE14E` · jhash `0xD88EC8EA` · **Cliente**

```lua
local retval, outData = GetDlcWeaponData(dlcWeaponIndex, outData)
```
```c
BOOL GET_DLC_WEAPON_DATA(int dlcWeaponIndex, int* outData);
```

**Parámetros**

- `dlcWeaponIndex` (`int`)
- `outData` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
dlcWeaponIndex takes a number from 0 - GET_NUM_DLC_WEAPONS() - 1.  
struct DlcWeaponData  
{  
int emptyCheck; //use DLC1::_IS_DLC_DATA_EMPTY on this  
int padding1;  
int weaponHash;  
int padding2;  
int unk;  
int padding3;  
int weaponCost;  
int padding4;  
int ammoCost;  
int padding5;  
int ammoType;  
int padding6;  
int defaultClipSize;  
int padding7;  
char nameLabel[64];  
char descLabel[64];  
char desc2Label[64]; // usually "the" + name  
char upperCaseNameLabel[64];  
};  
```

---
### GetDlcWeaponDataSp

`_GET_DLC_WEAPON_DATA_SP` · hash `0x310836EE7129BA33` · **Cliente**

```lua
local retval, outData = GetDlcWeaponDataSp(dlcWeaponIndex, outData)
```
```c
BOOL _GET_DLC_WEAPON_DATA_SP(int dlcWeaponIndex, int* outData);
```

**Parámetros**

- `dlcWeaponIndex` (`int`)
- `outData` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Same as GET_DLC_WEAPON_DATA but only works for DLC weapons that are available in SP.

```
NativeDB Introduced: v2060
```

---
### GetForcedComponent

`GET_FORCED_COMPONENT` · hash `0x6C93ED8C2F74859B` · jhash `0x382C70BE` · **Cliente**

```lua
local nameHash, enumValue, componentType = GetForcedComponent(componentHash, forcedComponentIndex)
```
```c
void GET_FORCED_COMPONENT(Hash componentHash, int forcedComponentIndex, Hash* nameHash, int* enumValue, int* componentType);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `forcedComponentIndex` (`int`)
- `nameHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `enumValue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `componentType` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetForcedProp

`GET_FORCED_PROP` · hash `0xE1CA84EBF72E691D` · jhash `0x22DAE257` · **Cliente**

```lua
local nameHash, enumValue, anchorPoint = GetForcedProp(componentHash, forcedPropIndex)
```
```c
void GET_FORCED_PROP(Hash componentHash, int forcedPropIndex, Hash* nameHash, int* enumValue, int* anchorPoint);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `forcedPropIndex` (`int`)
- `nameHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `enumValue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `anchorPoint` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xE1CA84EBF72E691D` (`N_0xe1ca84ebf72e691d`)

---
### GetHashNameForComponent

`GET_HASH_NAME_FOR_COMPONENT` · hash `0x0368B3A838070348` · jhash `0xC8A4BF12` · **Cliente**

```lua
local retval = GetHashNameForComponent(entity, componentId, drawableVariant, textureVariant)
```
```c
Hash GET_HASH_NAME_FOR_COMPONENT(Entity entity, int componentId, int drawableVariant, int textureVariant);
```

**Parámetros**

- `entity` (`Entity`)
- `componentId` (`int`)
- `drawableVariant` (`int`)
- `textureVariant` (`int`)

**Devuelve:** `Hash`

---
### GetHashNameForProp

`GET_HASH_NAME_FOR_PROP` · hash `0x5D6160275CAEC8DD` · jhash `0x7D876DC0` · **Cliente**

```lua
local retval = GetHashNameForProp(entity, componentId, propIndex, propTextureIndex)
```
```c
Hash GET_HASH_NAME_FOR_PROP(Entity entity, int componentId, int propIndex, int propTextureIndex);
```

**Parámetros**

- `entity` (`Entity`)
- `componentId` (`int`)
- `propIndex` (`int`)
- `propTextureIndex` (`int`)

**Devuelve:** `Hash`

---
### GetNumDlcVehicles

`GET_NUM_DLC_VEHICLES` · hash `0xA7A866D21CD2329B` · jhash `0x8EAF9CF6` · **Cliente**

```lua
local retval = GetNumDlcVehicles()
```
```c
int GET_NUM_DLC_VEHICLES();
```

**Devuelve:** `int`

**Descripción oficial:**

Returns the total number of DLC vehicles.

---
### GetNumDlcWeaponComponents

`GET_NUM_DLC_WEAPON_COMPONENTS` · hash `0x405425358A7D61FE` · jhash `0x476B23A9` · **Cliente**

```lua
local retval = GetNumDlcWeaponComponents(dlcWeaponIndex)
```
```c
int GET_NUM_DLC_WEAPON_COMPONENTS(int dlcWeaponIndex);
```

**Parámetros**

- `dlcWeaponIndex` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the total number of DLC weapon components.
```

---
### GetNumDlcWeaponComponentsSp

`_GET_NUM_DLC_WEAPON_COMPONENTS_SP` · hash `0xAD2A7A6DFF55841B` · **Cliente**

```lua
local retval = GetNumDlcWeaponComponentsSp(dlcWeaponIndex)
```
```c
int _GET_NUM_DLC_WEAPON_COMPONENTS_SP(int dlcWeaponIndex);
```

**Parámetros**

- `dlcWeaponIndex` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

Returns the total number of DLC weapon components that are available in SP.

```
NativeDB Introduced: v2060
```

---
### GetNumDlcWeapons

`GET_NUM_DLC_WEAPONS` · hash `0xEE47635F352DA367` · jhash `0x2B757E6C` · **Cliente**

```lua
local retval = GetNumDlcWeapons()
```
```c
int GET_NUM_DLC_WEAPONS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Returns the total number of DLC weapons.
```

---
### GetNumDlcWeaponsSp

`_GET_NUM_DLC_WEAPONS_SP` · hash `0x4160B65AE085B5A9` · **Cliente**

```lua
local retval = GetNumDlcWeaponsSp()
```
```c
int _GET_NUM_DLC_WEAPONS_SP();
```

**Devuelve:** `int`

**Descripción oficial:**

Returns the total number of DLC weapons that are available in SP (availableInSP field in shop_weapon.meta).

```
NativeDB Introduced: v2060
```

---
### GetNumTattooShopDlcItems

`GET_NUM_TATTOO_SHOP_DLC_ITEMS` · hash `0x278F76C3B0A8F109` · jhash `0x71D0CF3E` · **Cliente**

```lua
local retval = GetNumTattooShopDlcItems(character)
```
```c
int GET_NUM_TATTOO_SHOP_DLC_ITEMS(int character);
```

**Parámetros**

- `character` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
Character types:
0 = Michael,
1 = Franklin,
2 = Trevor,
3 = MPMale,
4 = MPFemale
```

**Nombres antiguos (alias):** `0x278F76C3B0A8F109` (`N_0x278f76c3b0a8f109`), `_GET_NUM_DECORATIONS` (`GetNumDecorations`)

---
### GetShopPedApparelForcedComponentCount

`GET_SHOP_PED_APPAREL_FORCED_COMPONENT_COUNT` · hash `0xC6B9DB42C04DD8C3` · jhash `0xCE70F183` · **Cliente**

```lua
local retval = GetShopPedApparelForcedComponentCount(componentHash)
```
```c
int GET_SHOP_PED_APPAREL_FORCED_COMPONENT_COUNT(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Returns number of possible values of the forcedComponentIndex argument of GET_FORCED_COMPONENT.
```

**Nombres antiguos (alias):** `_GET_NUM_FORCED_COMPONENTS` (`GetNumForcedComponents`)

---
### GetShopPedApparelForcedPropCount

`GET_SHOP_PED_APPAREL_FORCED_PROP_COUNT` · hash `0x017568A8182D98A6` · jhash `0xC560D7C0` · **Cliente**

```lua
local retval = GetShopPedApparelForcedPropCount(componentHash)
```
```c
int GET_SHOP_PED_APPAREL_FORCED_PROP_COUNT(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Returns number of possible values of the forcedPropIndex argument of GET_FORCED_PROP.
```

**Nombres antiguos (alias):** `0x017568A8182D98A6` (`N_0x017568a8182d98a6`)

---
### GetShopPedApparelVariantComponentCount

`GET_SHOP_PED_APPAREL_VARIANT_COMPONENT_COUNT` · hash `0xC17AD0E5752BECDA` · jhash `0x159751B4` · **Cliente**

```lua
local retval = GetShopPedApparelVariantComponentCount(componentHash)
```
```c
int GET_SHOP_PED_APPAREL_VARIANT_COMPONENT_COUNT(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xC17AD0E5752BECDA` (`N_0xc17ad0e5752becda`)

---
### GetShopPedApparelVariantPropCount

`_GET_SHOP_PED_APPAREL_VARIANT_PROP_COUNT` · hash `0xD40AAC51E8E4C663` · **Cliente**

```lua
local retval = GetShopPedApparelVariantPropCount(propHash)
```
```c
int _GET_SHOP_PED_APPAREL_VARIANT_PROP_COUNT(Hash propHash);
```

**Parámetros**

- `propHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Ped helmet prop hash

**Devuelve:** `int` — This native returns 1 when the player helmet has a visor (there is another prop index for the same helmet with closed/opened visor variant) that can be toggled. 0 if there's no alternative version with a visor for this helmet prop.

**Nombres antiguos (alias):** `0xD40AAC51E8E4C663` (`N_0xd40aac51e8e4c663`)

**Ejemplo (lua):**

```lua
local iVar16 = GetPedPropIndex(PlayerPedId(), 0) -- helmet prop index
local iVar17 = GetPedPropTextureIndex(PlayerPedId(), 0) -- helmet prop index
local iVar18 = GetHashNameForProp(PlayerPedId(), 0, iVar16, iVar17) -- gets the hash name for the helmet
if N_0xd40aac51e8e4c663(iVar18) > 0 then -- visor variant so can toggle the visor
    BeginTextCommandDisplayHelp("VISOR_TOGGLE") -- Hold ~INPUT_SWITCH_VISOR~ to flip your helmet visor open or closed when on foot or on a motorcycle. You can also set the default state of your Helmet Visor in the Style section of the Interaction menu.
    EndTextCommandDisplayHelp(0, 0, true, 6000)
end
```

---
### GetShopPedComponent

`GET_SHOP_PED_COMPONENT` · hash `0x74C0E2A57EC66760` · jhash `0xB39677C5` · **Cliente**

```lua
local outComponent = GetShopPedComponent(componentHash, outComponent)
```
```c
void GET_SHOP_PED_COMPONENT(Hash componentHash, Any* outComponent);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outComponent` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
More info here: https://gist.github.com/root-cause/3b80234367b0c856d60bf5cb4b826f86
```

---
### GetShopPedOutfit

`GET_SHOP_PED_OUTFIT` · hash `0xB7952076E444979D` · jhash `0xCAFE9209` · **Cliente**

```lua
local p1 = GetShopPedOutfit(p0, p1)
```
```c
void GET_SHOP_PED_OUTFIT(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetShopPedOutfitComponentVariant

`GET_SHOP_PED_OUTFIT_COMPONENT_VARIANT` · hash `0x19F2A026EDF0013F` · jhash `0x818534AC` · **Cliente**

```lua
local retval, outComponentVariant = GetShopPedOutfitComponentVariant(outfit, slot, outComponentVariant)
```
```c
BOOL GET_SHOP_PED_OUTFIT_COMPONENT_VARIANT(Hash outfit, int slot, Any* outComponentVariant);
```

**Parámetros**

- `outfit` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: A structure, see [`GET_SHOP_PED_QUERY_OUTFIT`](#getshoppedqueryoutfit).
- `slot` (`int`): outfit slot.
- `outComponentVariant` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_GET_PROP_FROM_OUTFIT` (`GetPropFromOutfit`)

---
### GetShopPedOutfitLocate

`GET_SHOP_PED_OUTFIT_LOCATE` · hash `0x073CA26B079F956E` · jhash `0x2798F56F` · **Cliente**

```lua
local retval = GetShopPedOutfitLocate(p0)
```
```c
int GET_SHOP_PED_OUTFIT_LOCATE(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x073CA26B079F956E` (`N_0x073ca26b079f956e`)

---
### GetShopPedOutfitPropVariant

`GET_SHOP_PED_OUTFIT_PROP_VARIANT` · hash `0xA9F9C2E0FDE11CBB` · jhash `0x6641A864` · **Cliente**

```lua
local retval, outPropVariant = GetShopPedOutfitPropVariant(outfitHash, variantIndex, outPropVariant)
```
```c
BOOL GET_SHOP_PED_OUTFIT_PROP_VARIANT(Hash outfitHash, int variantIndex, Any* outPropVariant);
```

**Parámetros**

- `outfitHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `variantIndex` (`int`)
- `outPropVariant` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA9F9C2E0FDE11CBB` (`N_0xa9f9c2e0fde11cbb`)

---
### GetShopPedProp

`GET_SHOP_PED_PROP` · hash `0x5D5CAFF661DDF6FC` · jhash `0xDB0A7A58` · **Cliente**

```lua
local outProp = GetShopPedProp(componentHash, outProp)
```
```c
void GET_SHOP_PED_PROP(Hash componentHash, Any* outProp);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `outProp` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x5D5CAFF661DDF6FC` (`N_0x5d5caff661ddf6fc`)

---
### GetShopPedQueryComponent

`GET_SHOP_PED_QUERY_COMPONENT` · hash `0x249E310B2D920699` · jhash `0xC0718904` · **Cliente**

```lua
local outComponent = GetShopPedQueryComponent(componentId, outComponent)
```
```c
void GET_SHOP_PED_QUERY_COMPONENT(int componentId, int* outComponent);
```

**Parámetros**

- `componentId` (`int`)
- `outComponent` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetShopPedQueryOutfit

`GET_SHOP_PED_QUERY_OUTFIT` · hash `0x6D793F03A631FE56` · jhash `0x2F8013A1` · **Cliente**

```lua
local outfit = GetShopPedQueryOutfit(outfitIndex, outfit)
```
```c
void GET_SHOP_PED_QUERY_OUTFIT(int outfitIndex, Any* outfit);
```

**Parámetros**

- `outfitIndex` (`int`)
- `outfit` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
struct Outfit_s  
{  
	int mask, torso, pants, parachute, shoes, misc1, tops1, armour, crew, tops2, hat, glasses, earpiece;  
	int maskTexture, torsoTexture, pantsTexture, parachuteTexture, shoesTexture, misc1Texture, tops1Texture,   
		armourTexture, crewTexture, tops2Texture, hatTexture, glassesTexture, earpieceTexture;  
};  
```

---
### GetShopPedQueryProp

`GET_SHOP_PED_QUERY_PROP` · hash `0xDE44A00999B2837D` · jhash `0x1D3C1466` · **Cliente**

```lua
local outProp = GetShopPedQueryProp(componentId, outProp)
```
```c
void GET_SHOP_PED_QUERY_PROP(int componentId, Any* outProp);
```

**Parámetros**

- `componentId` (`int`)
- `outProp` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### GetTattooShopDlcItemData

`GET_TATTOO_SHOP_DLC_ITEM_DATA` · hash `0xFF56381874F82086` · jhash `0x2E9D628C` · **Cliente**

```lua
local retval, outComponent = GetTattooShopDlcItemData(characterType, decorationIndex, outComponent)
```
```c
BOOL GET_TATTOO_SHOP_DLC_ITEM_DATA(int characterType, int decorationIndex, Any* outComponent);
```

**Parámetros**

- `characterType` (`int`): Which character to get the tattoo data for (Refer to `eTattooFaction` above).
- `decorationIndex` (`int`): Tattoo index, value between 0 and [GET_NUM_TATTOO_SHOP_DLC_ITEMS](#getnumtattooshopdlcitems).
- `outComponent` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*: The referenced struct.

**Devuelve:** `BOOL` — A bool indicating that the tattoo data exists in the files.

**Descripción oficial:**

Returns data that adheres to the tattoo shop item data that is used in shop_tattoo.meta

Character types:

```cpp
enum eTattooFaction
{
	TATTOO_SP_MICHAEL = 0,
	TATTOO_SP_FRANKLIN = 1,
	TATTOO_SP_TREVOR = 2,
	TATTOO_MP_FM = 3,
	TATTOO_MP_FM_F = 4
}
```

Returned struct properties:

```cpp
struct sTattooShopItemValues
{
	// Lock hash, used with IS_CONTENT_ITEM_LOCKED
	int LockHash;
	// Unique ID of this slot. It can also be 0.
	int Index;
	// Collection hash of this tattoo
	int CollectionHash;
	// Preset hash of this tattoo
	int PresetHash;
	// Cost of this tattoo in shops.
	int Cost;
	// Secondary placement of this tattoo.
	int eFacing;
	// Location of this tattoo on the body (for example, for torso there would be chest upper, stomach, etc)
	int UpdateGroup;
	// This tattoo's name in the form of a text label.
	const char* NameTextLabel;
};
```

**Nombres antiguos (alias):** `0xFF56381874F82086` (`N_0xff56381874f82086`), `_GET_TATTOO_COLLECTION_DATA` (`GetTattooCollectionData`)

**Ejemplo (lua):**

```lua
local function TattooBlobToTable(blob)
    local LockHash = string.unpack('<i4', blob, 1) & 0xFFFFFFFF -- uint (hash)
    local Index = string.unpack('<i4', blob, 9) -- int
    local Collection = string.unpack('<i4', blob, 17) & 0xFFFFFFFF -- uint (hash)
    local Preset = string.unpack('<i4', blob, 25) & 0xFFFFFFFF -- uint (hash)
    local Price = string.unpack('<i4', blob, 33) -- int
    local eFacing = string.unpack('<i4', blob, 41) -- TattooZoneData
    local UpdateGroup = string.unpack('<i4', blob, 49) -- uint (hash)
    local TextLabel = string.unpack('z', blob, 57) -- uint

    return {
        LockHash = LockHash,
        Index = Index,
        Collection = Collection,
        Preset = Preset,
        Price = Price,
        eFacing = eFacing,
        UpdateGroup = UpdateGroup,
        TextLabel = TextLabel
    }
end

function GetTattooDlcItemDataTable(CharacterType, DecorationIndex)
	local blob = string.rep('\0\0\0\0\0\0\0\0', 7+16)
	if not Citizen.InvokeNative(0xFF56381874F82086, CharacterType, DecorationIndex, blob) then return nil end -- Data doesn't exist, return a nil

	return TattooBlobToTable(blob) -- Return the data table
end

local numberOfTattoos = GetNumTattooShopDlcItems(3) -- get all tattoos for mpmale
for i = 0, numberOfTattoos - 1 do
	local tattooData = GetTattooDlcItemDataTable(3, i)
	-- Do stuff with your tattoo data
end
```

**Ejemplo (js):**

```js
const characterType = 4; // MPFemale.
const tattooIndex = 0; // Value between 0 and GetNumDecorations(characterType).

const structArray = new Uint32Array(new ArrayBuffer(10 * 8));

if (Citizen.invokeNative("0xFF56381874F82086", characterType, tattooIndex, structArray))
{
    console.log(JSON.stringify(structArray));
}
```

---
### GetTattooShopDlcItemIndex

`GET_TATTOO_SHOP_DLC_ITEM_INDEX` · hash `0x10144267DD22866C` · **Cliente**

```lua
local retval = GetTattooShopDlcItemIndex(character, collection, preset)
```
```c
int GET_TATTOO_SHOP_DLC_ITEM_INDEX(int character, int collection, int preset);
```

**Parámetros**

- `character` (`int`): AKA eFaction in shop_tattoo.meta. Which character this tattoo belongs to. See [GET_NUM_TATTOO_SHOP_DLC_ITEMS](#getnumtattooshopdlcitems).
- `collection` (`int`): Which collection this tattoo belongs to. If you specify `-1`, it will check all collections.
- `preset` (`int`): Which preset this tattoo belongs to.

**Devuelve:** `int` — Returns the actual index (Not ID from `shop_tattoo.meta`) from `0` to [GET_NUM_TATTOO_SHOP_DLC_ITEMS](#getnumtattooshopdlcitems), or `-1` (if it failed to find the tattoo) of a tattoo.

**Descripción oficial:**

```
NativeDB Introduced: v2189
```

**Nombres antiguos (alias):** `0x10144267DD22866C` (`N_0x10144267dd22866c`)

---
### GetVariantComponent

`GET_VARIANT_COMPONENT` · hash `0x6E11F282F11863B6` · jhash `0xE4FF7103` · **Cliente**

```lua
local nameHash, enumValue, componentType = GetVariantComponent(componentHash, variantComponentIndex)
```
```c
void GET_VARIANT_COMPONENT(Hash componentHash, int variantComponentIndex, Hash* nameHash, int* enumValue, int* componentType);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `variantComponentIndex` (`int`)
- `nameHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `enumValue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `componentType` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

---
### GetVariantProp

`_GET_VARIANT_PROP` · hash `0xD81B7F27BC773E66` · **Cliente**

```lua
local nameHash, enumValue, anchorPoint = GetVariantProp(componentHash, variantPropIndex)
```
```c
void _GET_VARIANT_PROP(Hash componentHash, int variantPropIndex, Hash* nameHash, int* enumValue, int* anchorPoint);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `variantPropIndex` (`int`)
- `nameHash` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `enumValue` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `anchorPoint` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xD81B7F27BC773E66` (`N_0xd81b7f27bc773e66`)

---
### InitShopPedComponent

`INIT_SHOP_PED_COMPONENT` · hash `0x1E8C308FD312C036` · jhash `0xB818C7FC` · **Cliente**

```lua
local outComponent = InitShopPedComponent(outComponent)
```
```c
void INIT_SHOP_PED_COMPONENT(int* outComponent);
```

**Parámetros**

- `outComponent` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### InitShopPedProp

`INIT_SHOP_PED_PROP` · hash `0xEB0A2B758F7B850F` · jhash `0xF5659E50` · **Cliente**

```lua
local outProp = InitShopPedProp(outProp)
```
```c
void INIT_SHOP_PED_PROP(int* outProp);
```

**Parámetros**

- `outProp` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### IsContentItemLocked

`IS_CONTENT_ITEM_LOCKED` · hash `0xD4D7B033C3AA243C` · jhash `0x06396058` · **Cliente**

```lua
local retval = IsContentItemLocked(itemHash)
```
```c
BOOL IS_CONTENT_ITEM_LOCKED(Hash itemHash);
```

**Parámetros**

- `itemHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_IS_OUTFIT_EMPTY` (`IsOutfitEmpty`), `_IS_DLC_DATA_EMPTY` (`IsDlcDataEmpty`)

---
### IsDlcVehicleMod

`IS_DLC_VEHICLE_MOD` · hash `0x0564B9FF9631B82C` · jhash `0x35BCA844` · **Cliente**

```lua
local retval = IsDlcVehicleMod(hash)
```
```c
BOOL IS_DLC_VEHICLE_MOD(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0564B9FF9631B82C` (`N_0x0564b9ff9631b82c`)

---
### LoadContentChangeSetGroup

`_LOAD_CONTENT_CHANGE_SET_GROUP` · hash `0x6BEDF5769AC2DC07` · **Cliente**

```lua
LoadContentChangeSetGroup(hash)
```
```c
void _LOAD_CONTENT_CHANGE_SET_GROUP(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
From fm_deathmatch_creator and fm_race_creator:

FILES::_UNLOAD_CONTENT_CHANGE_SET_GROUP(joaat("GROUP_MAP_SP"));
FILES::_LOAD_CONTENT_CHANGE_SET_GROUP(joaat("GROUP_MAP"));

NativeDB Introduced: v1604
```

---
### N_0x6cebe002e58dee97

`0x6CEBE002E58DEE97` · hash `0x6CEBE002E58DEE97` · **Cliente**

```lua
local retval = N_0x6cebe002e58dee97(componentHash)
```
```c
int 0x6CEBE002E58DEE97(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

Returns some sort of index/offset for props.
Needs \_GET_NUM_PROPS_FROM_OUTFIT to be called with p3 = true and componentId = -1 first, returns -1 otherwise.

```
NativeDB Introduced: v2189
```

---
### N_0x96e2929292a4db77

`0x96E2929292A4DB77` · hash `0x96E2929292A4DB77` · **Cliente**

```lua
local retval = N_0x96e2929292a4db77(componentHash)
```
```c
int 0x96E2929292A4DB77(Hash componentHash);
```

**Parámetros**

- `componentHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

Returns some sort of index/offset for components.
Needs \_GET_NUM_PROPS_FROM_OUTFIT to be called with p3 = false and componentId with the drawable's component slot first, returns -1 otherwise.

```
NativeDB Introduced: v2189
```

---
### SetupShopPedApparelQuery

`SETUP_SHOP_PED_APPAREL_QUERY` · hash `0x50F457823CE6EB5F` · jhash `0xC937FF3D` · **Cliente**

```lua
local retval = SetupShopPedApparelQuery(p0, p1, p2, p3)
```
```c
int SETUP_SHOP_PED_APPAREL_QUERY(int p0, int p1, int p2, int p3);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`int`)
- `p2` (`int`)
- `p3` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x50F457823CE6EB5F` (`N_0x50f457823ce6eb5f`)

---
### SetupShopPedApparelQueryTu

`SETUP_SHOP_PED_APPAREL_QUERY_TU` · hash `0x9BDF59818B1E38C1` · jhash `0x594E862C` · **Cliente**

```lua
local retval = SetupShopPedApparelQueryTu(character, p1, p2, p3, p4, componentId)
```
```c
int SETUP_SHOP_PED_APPAREL_QUERY_TU(int character, int p1, int p2, BOOL p3, int p4, int componentId);
```

**Parámetros**

- `character` (`int`)
- `p1` (`int`)
- `p2` (`int`)
- `p3` (`BOOL`)
- `p4` (`int`)
- `componentId` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
character is 0 for Michael, 1 for Franklin, 2 for Trevor, 3 for freemode male, and 4 for freemode female.
componentId is between 0 and 11 and corresponds to the usual component slots.
p1 could be the outfit number; unsure.
p2 is usually -1; unknown function.
p3 appears to be for selecting between clothes and props; false is used with components/clothes, true is used with props.
p4 is usually -1; unknown function.
componentId is -1 when p3 is true in decompiled scripts.
```

**Nombres antiguos (alias):** `_GET_NUM_PROPS_FROM_OUTFIT` (`GetNumPropsFromOutfit`)

---
### SetupShopPedOutfitQuery

`SETUP_SHOP_PED_OUTFIT_QUERY` · hash `0xF3FBE2D50A6A8C28` · jhash `0x1ECD23E7` · **Cliente**

```lua
local retval = SetupShopPedOutfitQuery(character, p1)
```
```c
int SETUP_SHOP_PED_OUTFIT_QUERY(int character, BOOL p1);
```

**Parámetros**

- `character` (`int`)
- `p1` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
characters
0: Michael
1: Franklin
2: Trevor
3: MPMale
4: MPFemale
```

**Nombres antiguos (alias):** `0xF3FBE2D50A6A8C28` (`N_0xf3fbe2d50a6a8c28`)

---
### UnloadContentChangeSetGroup

`_UNLOAD_CONTENT_CHANGE_SET_GROUP` · hash `0x3C1978285B036B25` · **Cliente**

```lua
UnloadContentChangeSetGroup(hash)
```
```c
void _UNLOAD_CONTENT_CHANGE_SET_GROUP(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
From fm_deathmatch_creator and fm_race_creator:

FILES::_UNLOAD_CONTENT_CHANGE_SET_GROUP(joaat("GROUP_MAP_SP"));
FILES::_LOAD_CONTENT_CHANGE_SET_GROUP(joaat("GROUP_MAP"));

NativeDB Introduced: v1604
```

---
