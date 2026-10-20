# Natives de GTA V — ZONE

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `ZONE`: **9** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`ClearPopscheduleOverrideVehicleModel`](#clearpopscheduleoverridevehiclemodel) · [`GetHashOfMapAreaAtCoords`](#gethashofmapareaatcoords) · [`GetNameOfZone`](#getnameofzone) · [`GetZoneAtCoords`](#getzoneatcoords) · [`GetZoneFromNameId`](#getzonefromnameid) · [`GetZonePopschedule`](#getzonepopschedule) · [`GetZoneScumminess`](#getzonescumminess) · [`OverridePopscheduleVehicleModel`](#overridepopschedulevehiclemodel) · [`SetZoneEnabled`](#setzoneenabled)

---
### ClearPopscheduleOverrideVehicleModel

`CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL` · hash `0x5C0DE367AA0D911C` · jhash `0x7A72A24E` · **Cliente**

```lua
ClearPopscheduleOverrideVehicleModel(scheduleId)
```
```c
void CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL(int scheduleId);
```

**Parámetros**

- `scheduleId` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
Only used once in the decompiled scripts. Seems to be related to scripted vehicle generators.  
Modified example from "am_imp_exp.c4", line 6418:  
/* popSchedules[0] = ZONE::GET_ZONE_POPSCHEDULE(ZONE::GET_ZONE_AT_COORDS(891.3, 807.9, 188.1));  
etc.  
*/  
STREAMING::SET_MODEL_AS_NO_LONGER_NEEDED(vehicleHash);  
ZONE::CLEAR_POPSCHEDULE_OVERRIDE_VEHICLE_MODEL(popSchedules[index]);  
```

---
### GetHashOfMapAreaAtCoords

`GET_HASH_OF_MAP_AREA_AT_COORDS` · hash `0x7EE64D51E8498728` · jhash `0xB5C5C99B` · **Cliente**

```lua
local retval = GetHashOfMapAreaAtCoords(x, y, z)
```
```c
Hash GET_HASH_OF_MAP_AREA_AT_COORDS(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `Hash`

**Descripción oficial:**

```
Returns a hash representing which part of the map the given coords are located.  
Possible return values:  
(Hash of) city -> -289320599  
(Hash of) countryside -> 2072609373  
C# Example :  
Ped player = Game.Player.Character;  
Hash h = Function.Call<Hash>(Hash.GET_HASH_OF_MAP_AREA_AT_COORDS, player.Position.X, player.Position.Y, player.Position.Z);  
```

---
### GetNameOfZone

`GET_NAME_OF_ZONE` · hash `0xCD90657D4C30E1CA` · jhash `0x7875CE91` · **Cliente**

```lua
local retval = GetNameOfZone(x, y, z)
```
```c
char* GET_NAME_OF_ZONE(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `char*`

**Descripción oficial:**

```
AIRP = Los Santos International Airport  
ALAMO = Alamo Sea  
ALTA = Alta  
ARMYB = Fort Zancudo  
BANHAMC = Banham Canyon Dr  
BANNING = Banning  
BAYTRE = Baytree Canyon  
BEACH = Vespucci Beach  
BHAMCA = Banham Canyon  
BRADP = Braddock Pass  
BRADT = Braddock Tunnel  
BURTON = Burton  
CALAFB = Calafia Bridge  
CANNY = Raton Canyon  
CCREAK = Cassidy Creek  
CHAMH = Chamberlain Hills  
CHIL = Vinewood Hills  
CHU = Chumash  
CMSW = Chiliad Mountain State Wilderness  
CYPRE = Cypress Flats  
DAVIS = Davis  
DELBE = Del Perro Beach  
DELPE = Del Perro  
DELSOL = La Puerta  
DESRT = Grand Senora Desert  
DOWNT = Downtown  
DTVINE = Downtown Vinewood  
EAST_V = East Vinewood  
EBURO = El Burro Heights  
ELGORL = El Gordo Lighthouse  
ELYSIAN = Elysian Island  
GALFISH = Galilee  
GALLI = Galileo Park  
GOLF = GWC and Golfing Society  
GRAPES = Grapeseed  
GREATC = Great Chaparral  
HARMO = Harmony  
HAWICK = Hawick  
HORS = Vinewood Racetrack  
HUMLAB = Humane Labs and Research  
JAIL = Bolingbroke Penitentiary  
KOREAT = Little Seoul  
LACT = Land Act Reservoir  
LAGO = Lago Zancudo  
LDAM = Land Act Dam  
LEGSQU = Legion Square  
LMESA = La Mesa  
LOSPUER = La Puerta  
MIRR = Mirror Park  
MORN = Morningwood  
MOVIE = Richards Majestic  
MTCHIL = Mount Chiliad  
MTGORDO = Mount Gordo  
MTJOSE = Mount Josiah  
MURRI = Murrieta Heights  
NCHU = North Chumash  
NOOSE = N.O.O.S.E  
OBSERV = Galileo Observatory  
OCEANA = Pacific Ocean  
PALCOV = Paleto Cove  
PALETO = Paleto Bay  
PALFOR = Paleto Forest  
PALHIGH = Palomino Highlands  
PALMPOW = Palmer-Taylor Power Station  
PBLUFF = Pacific Bluffs  
PBOX = Pillbox Hill  
PROCOB = Procopio Beach  
RANCHO = Rancho  
RGLEN = Richman Glen  
RICHM = Richman  
ROCKF = Rockford Hills  
RTRAK = Redwood Lights Track  
SANAND = San Andreas  
SANCHIA = San Chianski Mountain Range  
SANDY = Sandy Shores  
SKID = Mission Row  
SLAB = Stab City  
STAD = Maze Bank Arena  
STRAW = Strawberry  
TATAMO = Tataviam Mountains  
TERMINA = Terminal  
TEXTI = Textile City  
TONGVAH = Tongva Hills  
TONGVAV = Tongva Valley  
VCANA = Vespucci Canals  
VESP = Vespucci  
VINE = Vinewood  
WINDF = Ron Alternates Wind Farm  
WVINE = West Vinewood  
ZANCUDO = Zancudo River  
ZP_ORT = Port of South Los Santos  
ZQ_UAR = Davis Quartz  
PROL = Prologue / North Yankton
ISHeist = Cayo Perico Island
```

---
### GetZoneAtCoords

`GET_ZONE_AT_COORDS` · hash `0x27040C25DE6CB2F4` · jhash `0xC9018181` · **Cliente**

```lua
local retval = GetZoneAtCoords(x, y, z)
```
```c
int GET_ZONE_AT_COORDS(float x, float y, float z);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)

**Devuelve:** `int`

---
### GetZoneFromNameId

`GET_ZONE_FROM_NAME_ID` · hash `0x98CD1D2934B76CC1` · jhash `0x8EC68304` · **Cliente**

```lua
local retval = GetZoneFromNameId(zoneName)
```
```c
int GET_ZONE_FROM_NAME_ID(char* zoneName);
```

**Parámetros**

- `zoneName` (`char*`): The zone name like "Z_RMAN2", most-left column of popzone.ipl

**Devuelve:** `int` — The zone ID, index in the popzone.ipl file starting with 1

**Descripción oficial:**

Refer to https://docs.fivem.net/docs/game-references/zones/ for a list of all zones including their integer ID, string ID, short name and full name

**Ejemplo (lua):**

```lua
local zoneId = GetZoneFromNameId("Z_GOLF3")
print(zoneId) -- 3
```

---
### GetZonePopschedule

`GET_ZONE_POPSCHEDULE` · hash `0x4334BC40AA0CB4BB` · jhash `0x20AB2FC9` · **Cliente**

```lua
local retval = GetZonePopschedule(zoneId)
```
```c
int GET_ZONE_POPSCHEDULE(int zoneId);
```

**Parámetros**

- `zoneId` (`int`)

**Devuelve:** `int`

---
### GetZoneScumminess

`GET_ZONE_SCUMMINESS` · hash `0x5F7B268D15BA0739` · jhash `0xB2FB5C4C` · **Cliente**

```lua
local retval = GetZoneScumminess(zoneId)
```
```c
int GET_ZONE_SCUMMINESS(int zoneId);
```

**Parámetros**

- `zoneId` (`int`): The zone id

**Devuelve:** `int` — The zone scumminess level

**Descripción oficial:**

Gets the zone scumminess level, used to calculate the cellphone signal strength.

```cpp
enum eZoneScumminess
{
    SCUMMINESS_POSH = 0,
    SCUMMINESS_NICE = 1,
    SCUMMINESS_ABOVE_AVERAGE = 2,
    SCUMMINESS_BELOW_AVERAGE = 3,
    SCUMMINESS_CRAP = 4,
    SCUMMINESS_SCUM = 5
}
```

---
### OverridePopscheduleVehicleModel

`OVERRIDE_POPSCHEDULE_VEHICLE_MODEL` · hash `0x5F7D596BAC2E7777` · jhash `0x3F0A3680` · **Cliente**

```lua
OverridePopscheduleVehicleModel(scheduleId, vehicleHash)
```
```c
void OVERRIDE_POPSCHEDULE_VEHICLE_MODEL(int scheduleId, Hash vehicleHash);
```

**Parámetros**

- `scheduleId` (`int`)
- `vehicleHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Only used once in the decompiled scripts. Seems to be related to scripted vehicle generators.  
Modified example from "am_imp_exp.c4", line 6406:  
/* popSchedules[0] = ZONE::GET_ZONE_POPSCHEDULE(ZONE::GET_ZONE_AT_COORDS(891.3, 807.9, 188.1));  
etc.  
*/  
ZONE::OVERRIDE_POPSCHEDULE_VEHICLE_MODEL(popSchedules[index], vehicleHash);  
STREAMING::REQUEST_MODEL(vehicleHash);  
```

---
### SetZoneEnabled

`SET_ZONE_ENABLED` · hash `0xBA5ECEEA120E5611` · jhash `0x04E21B03` · **Cliente**

```lua
SetZoneEnabled(zoneId, toggle)
```
```c
void SET_ZONE_ENABLED(int zoneId, BOOL toggle);
```

**Parámetros**

- `zoneId` (`int`)
- `toggle` (`BOOL`)

**Devuelve:** `void`

---
