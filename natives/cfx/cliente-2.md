# Natives de FiveM (CFX) — solo cliente (parte 2 de 2: SetVehicleWheelWidth … UpdateMapdataEntity)

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

**554** natives.

Partes: [1](cliente-1.md) · **[2]**

[← Índice de natives](../README.md)

## Índice de esta página

[`SetVehicleWheelWidth`](#setvehiclewheelwidth) · [`SetVehicleWheelXOffset`](#setvehiclewheelxoffset) · [`SetVehicleWheelYRotation`](#setvehiclewheelyrotation) · [`SetVehicleWheelieState`](#setvehiclewheeliestate) · [`SetVehicleXenonLightsCustomColor`](#setvehiclexenonlightscustomcolor) · [`SetVehicleXmasSnowFactor`](#setvehiclexmassnowfactor) · [`SetVisualSettingFloat`](#setvisualsettingfloat) · [`SetWaterAreaClipRect`](#setwaterareacliprect) · [`SetWaterQuadAlpha`](#setwaterquadalpha) · [`SetWaterQuadBounds`](#setwaterquadbounds) · [`SetWaterQuadHasLimitedDepth`](#setwaterquadhaslimiteddepth) · [`SetWaterQuadIsInvisible`](#setwaterquadisinvisible) · [`SetWaterQuadLevel`](#setwaterquadlevel) · [`SetWaterQuadNoStencil`](#setwaterquadnostencil) · [`SetWaterQuadType`](#setwaterquadtype) · [`SetWaveQuadAmplitude`](#setwavequadamplitude) · [`SetWaveQuadBounds`](#setwavequadbounds) · [`SetWaveQuadDirection`](#setwavequaddirection) · [`SetWeaponAccuracySpread`](#setweaponaccuracyspread) · [`SetWeaponRecoilShakeAmplitude`](#setweaponrecoilshakeamplitude) · [`SetWeaponsNoAimBlocking`](#setweaponsnoaimblocking) · [`SetWeaponsNoAutoreload`](#setweaponsnoautoreload) · [`SetWeaponsNoAutoswap`](#setweaponsnoautoswap) · [`SetWeatherCycleEntry`](#setweathercycleentry) · [`SetWeatherOwnedByNetwork`](#setweatherownedbynetwork) · [`SetWetClothPinRadiusScale`](#setwetclothpinradiusscale) · [`ShutdownLoadingScreenNui`](#shutdownloadingscreennui) · [`StartFindExternalKvp`](#startfindexternalkvp) · [`TriggerLatentServerEventInternal`](#triggerlatentservereventinternal) · [`TriggerServerEventInternal`](#triggerservereventinternal) · [`UnregisterRawNuiCallback`](#unregisterrawnuicallback) · [`UpdateMapdataEntity`](#updatemapdataentity)

---
### SetVehicleWheelWidth

`SET_VEHICLE_WHEEL_WIDTH` · hash `0x64C3F1C0` · **Cliente**

```lua
local retval = SetVehicleWheelWidth(vehicle, width)
```
```c
BOOL SET_VEHICLE_WHEEL_WIDTH(Vehicle vehicle, float width);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle to set data for.
- `width` (`float`): Width of the wheels (usually between 0.1 and 1.5 is reasonable).

**Devuelve:** `BOOL` — Bool - whether change was successful or not

**Descripción oficial:**

Sets vehicle's wheels' width (width is the same for all the wheels, cannot get/set specific wheel of vehicle).
Only works on non-default wheels.
Returns whether change was successful (can be false if trying to set width for non-default wheels).

---
### SetVehicleWheelXOffset

`SET_VEHICLE_WHEEL_X_OFFSET` · hash `0xBD6357D` · **Cliente**

```lua
SetVehicleWheelXOffset(vehicle, wheelIndex, offset)
```
```c
void SET_VEHICLE_WHEEL_X_OFFSET(Vehicle vehicle, int wheelIndex, float offset);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `offset` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

Adjusts the offset of the specified wheel relative to the wheel's axle center.
Needs to be called every frame in order to function properly, as GTA will reset the offset otherwise.
This function can be especially useful to set the track width of a vehicle, for example:

```
function SetVehicleFrontTrackWidth(vehicle, width)
SetVehicleWheelXOffset(vehicle, 0, -width/2)
SetVehicleWheelXOffset(vehicle, 1, width/2)
end
```

---
### SetVehicleWheelYRotation

`SET_VEHICLE_WHEEL_Y_ROTATION` · hash `0xC6C2171F` · **Cliente**

```lua
SetVehicleWheelYRotation(vehicle, wheelIndex, value)
```
```c
void SET_VEHICLE_WHEEL_Y_ROTATION(Vehicle vehicle, int wheelIndex, float value);
```

**Parámetros**

- `vehicle` (`Vehicle`)
- `wheelIndex` (`int`)
- `value` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `SET_VEHICLE_WHEEL_XROT` (`SetVehicleWheelXrot`)

---
### SetVehicleWheelieState

`SET_VEHICLE_WHEELIE_STATE` · hash `0xEAB8DB65` · **Cliente**

```lua
SetVehicleWheelieState(vehicle, state)
```
```c
void SET_VEHICLE_WHEELIE_STATE(Vehicle vehicle, int state);
```

**Parámetros**

- `vehicle` (`Vehicle`): Vehicle
- `state` (`int`): Wheelie state

**Devuelve:** `void`

**Descripción oficial:**

Example script: https://pastebin.com/J6XGbkCW

List of known states:

```
1: Not wheeling.
65: Vehicle is ready to do wheelie (burnouting).
129: Vehicle is doing wheelie.
```

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
  while true do
    Wait(1)

    local ped = PlayerPedId()
    local veh = GetVehiclePedIsUsing(ped)

    if veh ~= 0 then
      -- is vehicle a musclecar
      if GetVehicleClass(veh) == 4 then
        -- is ped a driver
        if GetPedInVehicleSeat(veh, -1) == ped then
          -- don't let vehicle to do wheelie
          SetVehicleWheelieState(veh, 1)
        end
      end
    end
  end
end)
```

---
### SetVehicleXenonLightsCustomColor

`SET_VEHICLE_XENON_LIGHTS_CUSTOM_COLOR` · hash `0x1683E7F0` · **Cliente**

```lua
SetVehicleXenonLightsCustomColor(vehicle, red, green, blue)
```
```c
void SET_VEHICLE_XENON_LIGHTS_CUSTOM_COLOR(Vehicle vehicle, int red, int green, int blue);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle handle.
- `red` (`int`): Red color (0-255).
- `green` (`int`): Green color (0-255).
- `blue` (`int`): Blue color (0-255).

**Devuelve:** `void`

**Descripción oficial:**

Sets custom vehicle xenon lights color, allowing to use RGB palette. The game will ignore lights color set by [\_SET_VEHICLE_XENON_LIGHTS_COLOR](../gta5/VEHICLE-2.md#setvehiclexenonlightscolor) when custom color is active. This native is not synced between players. Requires xenon lights mod to be set on vehicle.

**Ejemplo (lua):**

```lua
local vehicle = GetVehiclePedIsUsing(PlayerPedId())
if DoesEntityExist(vehicle) then
  -- Toggle xenon lights mod.
  ToggleVehicleMod(vehicle, 22, true)

  -- Set pink lights color.
  SetVehicleXenonLightsCustomColor(vehicle, 244, 5, 82)
end
```

---
### SetVehicleXmasSnowFactor

`SET_VEHICLE_XMAS_SNOW_FACTOR` · hash `0x80CC4C9E` · **Cliente**

```lua
SetVehicleXmasSnowFactor(gripFactor)
```
```c
void SET_VEHICLE_XMAS_SNOW_FACTOR(float gripFactor);
```

**Parámetros**

- `gripFactor` (`float`): amount of grip strength vehicle wheels have when xmas weather is active, 0.0 being normal weather grip. 0.2 is the default.

**Devuelve:** `void`

---
### SetVisualSettingFloat

`SET_VISUAL_SETTING_FLOAT` · hash `0xD1D31681` · **Cliente**

```lua
SetVisualSettingFloat(name, value)
```
```c
void SET_VISUAL_SETTING_FLOAT(char* name, float value);
```

**Parámetros**

- `name` (`char*`): The name of the value to set, such as `pedLight.color.red`.
- `value` (`float`): The value to write.

**Devuelve:** `void`

**Descripción oficial:**

Overrides a floating point value from `visualsettings.dat` temporarily.

---
### SetWaterAreaClipRect

`SET_WATER_AREA_CLIP_RECT` · hash `0x9FCD2EE6` · **Cliente**

```lua
SetWaterAreaClipRect(minX, minY, maxX, maxY)
```
```c
void SET_WATER_AREA_CLIP_RECT(int minX, int minY, int maxX, int maxY);
```

**Parámetros**

- `minX` (`int`)
- `minY` (`int`)
- `maxX` (`int`)
- `maxY` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Sets world clip boundaries for water quads file (water.xml, water_heistisland.xml)
Used internally by LOAD_GLOBAL_WATER_FILE

**Ejemplo (lua):**

```lua
SetWaterAreaClipRect(-4000, -4000, 4500, 8000)
```

---
### SetWaterQuadAlpha

`SET_WATER_QUAD_ALPHA` · hash `0xF49797EB` · **Cliente**

```lua
local retval = SetWaterQuadAlpha(waterQuad, a0, a1, a2, a3)
```
```c
BOOL SET_WATER_QUAD_ALPHA(int waterQuad, int a0, int a1, int a2, int a3);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `a0` (`int`): The a0 level
- `a1` (`int`): The a1 level
- `a2` (`int`): The a2 level
- `a3` (`int`): The a3 level

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetWaterQuadAlpha(0, 5, 5, 5, 5)
```

---
### SetWaterQuadBounds

`SET_WATER_QUAD_BOUNDS` · hash `0x80AD144C` · **Cliente**

```lua
local retval = SetWaterQuadBounds(waterQuad, minX, minY, maxX, maxY)
```
```c
BOOL SET_WATER_QUAD_BOUNDS(int waterQuad, int minX, int minY, int maxX, int maxY);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `minX` (`int`): The minX coordinate
- `minY` (`int`): The minY coordinate
- `maxX` (`int`): The maxX coordinate
- `maxY` (`int`): The maxY coordinate

**Devuelve:** `BOOL` — Returns true on success.

**Descripción oficial:**

This native allows you to update the bounds of a specified water quad index.

**Ejemplo (lua):**

```lua
local success = SetWaterQuadBounds(0, -5000.0, -5000.0, 5000.0, 5000.0)
```

---
### SetWaterQuadHasLimitedDepth

`SET_WATER_QUAD_HAS_LIMITED_DEPTH` · hash `0xD1FDCFC1` · **Cliente**

```lua
local retval = SetWaterQuadHasLimitedDepth(waterQuad, hasLimitedDepth)
```
```c
BOOL SET_WATER_QUAD_HAS_LIMITED_DEPTH(int waterQuad, BOOL hasLimitedDepth);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `hasLimitedDepth` (`BOOL`): Unknown effect

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetWaterQuadHasLimitedDepth(0, true)
```

---
### SetWaterQuadIsInvisible

`SET_WATER_QUAD_IS_INVISIBLE` · hash `0xA387D917` · **Cliente**

```lua
local retval = SetWaterQuadIsInvisible(waterQuad, isInvisible)
```
```c
BOOL SET_WATER_QUAD_IS_INVISIBLE(int waterQuad, BOOL isInvisible);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `isInvisible` (`BOOL`): Unknown effect

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetWaterQuadIsInvisible(0, true)
```

---
### SetWaterQuadLevel

`SET_WATER_QUAD_LEVEL` · hash `0x6292F7A8` · **Cliente**

```lua
local retval = SetWaterQuadLevel(waterQuad, level)
```
```c
BOOL SET_WATER_QUAD_LEVEL(int waterQuad, float level);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `level` (`float`): The water level inside the water quad

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetWaterQuadLevel(0, 55.0)
```

---
### SetWaterQuadNoStencil

`SET_WATER_QUAD_NO_STENCIL` · hash `0xC3FF42FF` · **Cliente**

```lua
local retval = SetWaterQuadNoStencil(waterQuad, noStencil)
```
```c
BOOL SET_WATER_QUAD_NO_STENCIL(int waterQuad, bool noStencil);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `noStencil` (`bool`): Unknown effect

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetWaterQuadNoStencil(0, true)
```

---
### SetWaterQuadType

`SET_WATER_QUAD_TYPE` · hash `0x50131EB2` · **Cliente**

```lua
local retval = SetWaterQuadType(waterQuad, type)
```
```c
BOOL SET_WATER_QUAD_TYPE(int waterQuad, int type);
```

**Parámetros**

- `waterQuad` (`int`): The water quad index
- `type` (`int`): The water quad type

**Devuelve:** `BOOL` — Returns true on success.

**Descripción oficial:**

This native allows you to update the water quad type.

Valid type definitions:

*   **0** Square
*   **1** Right triangle where the 90 degree angle is at maxX, minY
*   **2** Right triangle where the 90 degree angle is at minX, minY
*   **3** Right triangle where the 90 degree angle is at minX, maxY
*   **4** Right triangle where the 90 degree angle is at maxY, maxY

**Ejemplo (lua):**

```lua
local success = SetWaterQuadType(0, 0)
```

---
### SetWaveQuadAmplitude

`SET_WAVE_QUAD_AMPLITUDE` · hash `0xE4174B7B` · **Cliente**

```lua
local retval = SetWaveQuadAmplitude(waveQuad, amplitude)
```
```c
BOOL SET_WAVE_QUAD_AMPLITUDE(int waveQuad, float amplitude);
```

**Parámetros**

- `waveQuad` (`int`): The wave quad index
- `amplitude` (`float`): The amplitude value

**Devuelve:** `BOOL` — Returns true on success.

**Ejemplo (lua):**

```lua
local success = SetWaveQuadAmplitude(0, 1.0)
```

---
### SetWaveQuadBounds

`SET_WAVE_QUAD_BOUNDS` · hash `0x1FCC1FAF` · **Cliente**

```lua
local retval = SetWaveQuadBounds(waveQuad, minX, minY, maxX, maxY)
```
```c
BOOL SET_WAVE_QUAD_BOUNDS(int waveQuad, int minX, int minY, int maxX, int maxY);
```

**Parámetros**

- `waveQuad` (`int`): The wave quad index
- `minX` (`int`): The minX coordinate
- `minY` (`int`): The minY coordinate
- `maxX` (`int`): The maxX coordinate
- `maxY` (`int`): The maxY coordinate

**Devuelve:** `BOOL` — Returns true on success.

**Descripción oficial:**

This native allows you to update the bounds of a specified water quad index.

**Ejemplo (lua):**

```lua
local success = SetWaveQuadBounds(0, -5000, -5000, 5000, 5000)
```

---
### SetWaveQuadDirection

`SET_WAVE_QUAD_DIRECTION` · hash `0xFC9341A3` · **Cliente**

```lua
local retval = SetWaveQuadDirection(waveQuad, directionX, directionY)
```
```c
BOOL SET_WAVE_QUAD_DIRECTION(int waveQuad, float directionX, float directionY);
```

**Parámetros**

- `waveQuad` (`int`): The wave quad index
- `directionX` (`float`): The minX coordinate
- `directionY` (`float`): The minY coordinate

**Devuelve:** `BOOL` — Returns true on success.

**Descripción oficial:**

directionX/Y should be constrained between -1.0 and 1.0
A positive value will create the wave starting at min and rolling towards max
A negative value will create the wave starting at max and rolling towards min
Applying both values allows you to make diagonal waves

**Ejemplo (lua):**

```lua
local success = SetWaveQuadDirection(0, 0.3, 0.1)
```

---
### SetWeaponAccuracySpread

`SET_WEAPON_ACCURACY_SPREAD` · hash `0x598DD6AE` · **Cliente**

```lua
SetWeaponAccuracySpread(weaponHash, spread)
```
```c
void SET_WEAPON_ACCURACY_SPREAD(Hash weaponHash, float spread);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon name hash.
- `spread` (`float`): Accuracy spread

**Devuelve:** `void`

**Descripción oficial:**

A setter for the accuracy spread of a weapon.

---
### SetWeaponRecoilShakeAmplitude

`SET_WEAPON_RECOIL_SHAKE_AMPLITUDE` · hash `0x9864312F` · **Cliente**

```lua
SetWeaponRecoilShakeAmplitude(weaponHash, amplitude)
```
```c
void SET_WEAPON_RECOIL_SHAKE_AMPLITUDE(Hash weaponHash, float amplitude);
```

**Parámetros**

- `weaponHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*: Weapon name hash.
- `amplitude` (`float`): Recoil shake amplitude

**Devuelve:** `void`

**Descripción oficial:**

A setter for the recoil shake amplitude of a weapon.

---
### SetWeaponsNoAimBlocking

`SET_WEAPONS_NO_AIM_BLOCKING` · hash `0xDFD8F6DE` · **Cliente**

```lua
SetWeaponsNoAimBlocking(state)
```
```c
void SET_WEAPONS_NO_AIM_BLOCKING(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): On/Off

**Devuelve:** `void`

**Descripción oficial:**

Disables weapons aim blocking due to environment for local player.
For non-player peds [SET_PED_ENABLE_WEAPON_BLOCKING](../gta5/PED-1.md#setpedenableweaponblocking) can be used.

---
### SetWeaponsNoAutoreload

`SET_WEAPONS_NO_AUTORELOAD` · hash `0x311150E5` · **Cliente**

```lua
SetWeaponsNoAutoreload(state)
```
```c
void SET_WEAPONS_NO_AUTORELOAD(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): On/Off

**Devuelve:** `void`

**Descripción oficial:**

Disables the game's built-in auto-reloading.

---
### SetWeaponsNoAutoswap

`SET_WEAPONS_NO_AUTOSWAP` · hash `0x2A7B50E` · **Cliente**

```lua
SetWeaponsNoAutoswap(state)
```
```c
void SET_WEAPONS_NO_AUTOSWAP(BOOL state);
```

**Parámetros**

- `state` (`BOOL`): On/Off

**Devuelve:** `void`

**Descripción oficial:**

Disables autoswapping to another weapon when the current weapon runs out of ammo.

---
### SetWeatherCycleEntry

`SET_WEATHER_CYCLE_ENTRY` · hash `0xD264D4E1` · **Cliente**

```lua
local retval = SetWeatherCycleEntry(index, typeName, timeMult)
```
```c
BOOL SET_WEATHER_CYCLE_ENTRY(int index, char* typeName, int timeMult);
```

**Parámetros**

- `index` (`int`): The index of the entry to set. Must be between 0 and 255
- `typeName` (`char*`): The name of the weather type for this cycle
- `timeMult` (`int`): The relative duration of this cycle, which is multiplied by `msPerCycle` during ['APPLY_WEATHER_CYCLES'](cliente-1.md#applyweathercycles). Must be between 1 and 255

**Devuelve:** `BOOL` — Returns true if all parameters were valid, otherwise false.

---
### SetWeatherOwnedByNetwork

`SET_WEATHER_OWNED_BY_NETWORK` · hash `0x2703D582` · **Cliente**

```lua
SetWeatherOwnedByNetwork(network)
```
```c
void SET_WEATHER_OWNED_BY_NETWORK(BOOL network);
```

**Parámetros**

- `network` (`BOOL`): true to let the network control weather, false to not use network weather behavior.

**Devuelve:** `void`

**Descripción oficial:**

Sets whether or not the weather should be owned by the network subsystem.

To be able to use [\_SET_WEATHER_TYPE_TRANSITION](../gta5/MISC.md#setweathertypetransition), this has to be set to false.

---
### SetWetClothPinRadiusScale

`SET_WET_CLOTH_PIN_RADIUS_SCALE` · hash `0xF1BD2CEF` · **Cliente**

```lua
SetWetClothPinRadiusScale(scale)
```
```c
void SET_WET_CLOTH_PIN_RADIUS_SCALE(float scale);
```

**Parámetros**

- `scale` (`float`): A value that controls the wet cloth radius scale, default: 0.3, maximum: 1.0(used for dry cloth by default), lower values increase the adhesion effect of wet cloth, making it cling more tightly to the surface.

**Devuelve:** `void`

**Descripción oficial:**

Modifies the radius scale used in the simulation of wet cloth physics.
This affects how cloth behaves when wet, changing how it sticks or reacts to movement.

**Ejemplo (lua):**

```lua
SetWetClothPinRadiusScale(1.0)
```

---
### ShutdownLoadingScreenNui

`SHUTDOWN_LOADING_SCREEN_NUI` · hash `0xB9234AFB` · **Cliente**

```lua
ShutdownLoadingScreenNui()
```
```c
void SHUTDOWN_LOADING_SCREEN_NUI();
```

**Devuelve:** `void`

**Descripción oficial:**

Shuts down the `loadingScreen` NUI frame, similarly to `SHUTDOWN_LOADING_SCREEN`.

---
### StartFindExternalKvp

`START_FIND_EXTERNAL_KVP` · hash `0x8F2EECC3` · **Cliente**

```lua
local retval = StartFindExternalKvp(resourceName, prefix)
```
```c
int START_FIND_EXTERNAL_KVP(char* resourceName, char* prefix);
```

**Parámetros**

- `resourceName` (`char*`): The resource to try finding the key/values for
- `prefix` (`char*`): A prefix match

**Devuelve:** `int` — A KVP find handle to use with [FIND_KVP](compartidos.md#findkvp) and close with [END_FIND_KVP](compartidos.md#endfindkvp)

**Descripción oficial:**

Equivalent of [START_FIND_KVP](compartidos.md#startfindkvp), but for another resource than the current one.

**Ejemplo (lua):**

```lua
local kvpHandle = StartFindExternalKvp('drugs', 'mollis:')

if kvpHandle ~= -1 then 
	local key
	
	repeat
		key = FindKvp(kvpHandle)

		if key then
			print(('%s: %s'):format(key, GetResourceKvpString(key)))
		end
	until not key

	EndFindKvp(kvpHandle)
else
	print('No KVPs found')
end
```

---
### TriggerLatentServerEventInternal

`TRIGGER_LATENT_SERVER_EVENT_INTERNAL` · hash `0x128737EA` · **Cliente**

```lua
TriggerLatentServerEventInternal(eventName, eventPayload, payloadLength, bps)
```
```c
void TRIGGER_LATENT_SERVER_EVENT_INTERNAL(char* eventName, char* eventPayload, int payloadLength, int bps);
```

**Parámetros**

- `eventName` (`char*`)
- `eventPayload` (`char*`)
- `payloadLength` (`int`)
- `bps` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

The backing function for TriggerLatentServerEvent.

---
### TriggerServerEventInternal

`TRIGGER_SERVER_EVENT_INTERNAL` · hash `0x7FDD1128` · **Cliente**

```lua
TriggerServerEventInternal(eventName, eventPayload, payloadLength)
```
```c
void TRIGGER_SERVER_EVENT_INTERNAL(char* eventName, char* eventPayload, int payloadLength);
```

**Parámetros**

- `eventName` (`char*`)
- `eventPayload` (`char*`)
- `payloadLength` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

The backing function for TriggerServerEvent.

---
### UnregisterRawNuiCallback

`UNREGISTER_RAW_NUI_CALLBACK` · hash `0x7FB46432` · **Cliente**

```lua
UnregisterRawNuiCallback(callbackType)
```
```c
void UNREGISTER_RAW_NUI_CALLBACK(char* callbackType);
```

**Parámetros**

- `callbackType` (`char*`): The callback type to target

**Devuelve:** `void`

**Descripción oficial:**

Will unregister and cleanup a registered NUI callback handler.

Use along side the REGISTER_RAW_NUI_CALLBACK native.

---
### UpdateMapdataEntity

`UPDATE_MAPDATA_ENTITY` · hash `0xFC52CB91` · **Cliente**

```lua
UpdateMapdataEntity(mapdata, entity, entityDef)
```
```c
void UPDATE_MAPDATA_ENTITY(int mapdata, int entity, object entityDef);
```

**Parámetros**

- `mapdata` (`int`): A fwMapData index from GET_MAPDATA_FROM_HASH_KEY.
- `entity` (`int`): An entity index from GET_ENTITY_INDEX_FROM_MAPDATA.
- `entityDef` (`object`): The new entity definition in fwEntityDef format.

**Devuelve:** `void`

**Descripción oficial:**

Transiently updates the entity with the specified mapdata index and entity index.
This function supports SDK infrastructure and is not intended to be used directly from your code.

---
