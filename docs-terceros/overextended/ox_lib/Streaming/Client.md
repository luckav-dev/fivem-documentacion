> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Streaming/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

Check if assets exist, such as models, and loads them into memory.  
Throws errors for invalid assets and returns true if the asset is loaded.

## lib.requestAnimDict

> **Nota:** Remember to call `RemoveAnimDict(dict)` at the end of your code!

**Lua**

```lua
lib.requestAnimDict(dict, timeout)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.requestAnimDict(dict, timeout)
```

- dict: `string`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `10000`

## lib.requestAnimSet

> **Nota:** Remember to call `RemoveAnimSet(set)` at the end of you code!

**Lua**

```lua
lib.requestAnimSet(set, timeout)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.requestAnimSet(set, timeout)
```

- set: `string`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `10000`

## lib.requestAudioBank

> **Nota:** Remember to call `ReleaseScriptAudioBank(set)` at the end of you code!

```lua
lib.requestAudioBank(audioBank, timeout)
```

- audioBank: `string`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `30000`

## lib.requestModel

> **Nota:** Remember to call `SetModelAsNoLongerNeeded(model)` at the end of you code!

**Lua**

```lua
lib.requestModel(model, timeout)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.requestModel(model, timeout)
```

- model: `string`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `10000`

## lib.requestStreamedTextureDict

> **Nota:** Remember to call `SetStreamedTextureDictAsNoLongerNeeded(dict)` at the end of you code!

**Lua**

```lua
lib.requestStreamedTextureDict(dict, timeout)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.requestStreamedTextureDict(dict, timeout)
```

- dict: `string`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `10000`

## lib.requestNamedPtfxAsset

> **Nota:** Remember to call `RemoveNamedPtfxAsset(dict)` at the end of you code!

**Lua**

```lua
lib.requestNamedPtfxAsset(ptFxName, timeout)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.requestNamedPtfxAsset(ptFxName, timeout)
```

- ptFxName: `string`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `10000`

## lib.requestScaleformMovie

> **Nota:** Remember to call `SetScaleformMovieAsNoLongerNeeded(scaleformName)` at the end of you code!

**Lua**

```lua
lib.requestScaleformMovie(scaleformName, timeout)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.requestScaleformMovie(scaleformName, timeout)
```

- scaleformName: `string`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `1000`

## lib.requestWeaponAsset

> **Nota:** Remember to call `RemoveWeaponAsset(weaponType)` at the end of you code!

**Lua**

```lua
lib.requestWeaponAsset(weaponType, timeout, weaponResourceFlags, extraWeaponComponentFlags)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.requestWeaponAsset(weaponType, timeout, weaponResourceFlags, extraWeaponComponentFlags)
```

- weaponType: `string | number`
- timeout?: `number`
  - Number of ticks to wait for the asset to load.
  - Default: `10000`
- weaponResourceFlags?: `WeaponResourceFlags`
  - Default: `31`
- extraWeaponComponentFlags?: `ExtraWeaponComponentFlags`
  - Default: `0`

### WeaponResourceFlags

```
1 WRF_REQUEST_BASE_ANIMS
2 WRF_REQUEST_COVER_ANIMS
4 WRF_REQUEST_MELEE_ANIMS
8 WRF_REQUEST_MOTION_ANIMS
16 WRF_REQUEST_STEALTH_ANIMS
32 WRF_REQUEST_ALL_MOVEMENT_VARIATION_ANIMS
31 WRF_REQUEST_ALL_ANIMS
```

### ExtraWeaponComponentFlags

```
0 WEAPON_COMPONENT_NONE
1 WEAPON_COMPONENT_FLASH
2 WEAPON_COMPONENT_SCOPE
4 WEAPON_COMPONENT_SUPP
8 WEAPON_COMPONENT_SCLIP2
16 WEAPON_COMPONENT_GRIP
```
