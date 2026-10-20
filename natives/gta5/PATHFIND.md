# Natives de GTA V — PATHFIND

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `PATHFIND`: **59** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddNavmeshBlockingObject`](#addnavmeshblockingobject) · [`AddNavmeshRequiredRegion`](#addnavmeshrequiredregion) · [`AreAllNavmeshRegionsLoaded`](#areallnavmeshregionsloaded) · [`AreNodesLoadedForArea`](#arenodesloadedforarea) · [`CalculateTravelDistanceBetweenPoints`](#calculatetraveldistancebetweenpoints) · [`ClearGpsDisabledZoneAtIndex`](#cleargpsdisabledzoneatindex) · [`DisableNavmeshInArea`](#disablenavmeshinarea) · [`DoesNavmeshBlockingObjectExist`](#doesnavmeshblockingobjectexist) · [`GenerateDirectionsToCoord`](#generatedirectionstocoord) · [`GetClosestMajorVehicleNode`](#getclosestmajorvehiclenode) · [`GetClosestRoad`](#getclosestroad) · [`GetClosestVehicleNode`](#getclosestvehiclenode) · [`GetClosestVehicleNodeWithHeading`](#getclosestvehiclenodewithheading) · [`GetGpsBlipRouteFound`](#getgpsbliproutefound) · [`GetGpsBlipRouteLength`](#getgpsbliproutelength) · [`GetHeightmapBottomZForArea`](#getheightmapbottomzforarea) · [`GetHeightmapBottomZForPosition`](#getheightmapbottomzforposition) · [`GetHeightmapTopZForArea`](#getheightmaptopzforarea) · [`GetHeightmapTopZForPosition`](#getheightmaptopzforposition) · [`GetNextGpsDisabledZoneIndex`](#getnextgpsdisabledzoneindex) · [`GetNthClosestVehicleNode`](#getnthclosestvehiclenode) · [`GetNthClosestVehicleNodeFavourDirection`](#getnthclosestvehiclenodefavourdirection) · [`GetNthClosestVehicleNodeId`](#getnthclosestvehiclenodeid) · [`GetNthClosestVehicleNodeIdWithHeading`](#getnthclosestvehiclenodeidwithheading) · [`GetNthClosestVehicleNodeWithHeading`](#getnthclosestvehiclenodewithheading) · [`GetNumNavmeshesExistingInArea`](#getnumnavmeshesexistinginarea) · [`GetPointOnRoadSide`](#getpointonroadside) · [`GetPosAlongGpsTypeRoute`](#getposalonggpstyperoute) · [`GetRandomVehicleNode`](#getrandomvehiclenode) · [`GetRoadBoundaryUsingHeading`](#getroadboundaryusingheading) · [`GetSafeCoordForPed`](#getsafecoordforped) · [`GetStreetNameAtCoord`](#getstreetnameatcoord) · [`GetVehicleNodeIsGpsAllowed`](#getvehiclenodeisgpsallowed) · [`GetVehicleNodeIsSwitchedOff`](#getvehiclenodeisswitchedoff) · [`GetVehicleNodePosition`](#getvehiclenodeposition) · [`GetVehicleNodeProperties`](#getvehiclenodeproperties) · [`IsNavmeshLoadedInArea`](#isnavmeshloadedinarea) · [`IsNavmeshRequiredRegionOwnedByAnyThread`](#isnavmeshrequiredregionownedbyanythread) · [`IsPointOnRoad`](#ispointonroad) · [`IsVehicleNodeIdValid`](#isvehiclenodeidvalid) · [`LoadAllPathNodes`](#loadallpathnodes) · [`N_0xaa76052dda9bfc3e`](#n_0xaa76052dda9bfc3e) · [`RemoveNavmeshBlockingObject`](#removenavmeshblockingobject) · [`RemoveNavmeshRequiredRegions`](#removenavmeshrequiredregions) · [`RequestPathsPreferAccurateBoundingstruct`](#requestpathspreferaccurateboundingstruct) · [`SetAiGlobalPathNodesType`](#setaiglobalpathnodestype) · [`SetAllPathsCacheBoundingstruct`](#setallpathscacheboundingstruct) · [`SetAmbientPedRangeMultiplierThisFrame`](#setambientpedrangemultiplierthisframe) · [`SetGpsDisabledZone`](#setgpsdisabledzone) · [`SetGpsDisabledZoneAtIndex`](#setgpsdisabledzoneatindex) · [`SetIgnoreNoGpsFlag`](#setignorenogpsflag) · [`SetIgnoreSecondaryRouteNodes`](#setignoresecondaryroutenodes) · [`SetPedPathsBackToOriginal`](#setpedpathsbacktooriginal) · [`SetPedPathsInArea`](#setpedpathsinarea) · [`SetRoadsBackToOriginal`](#setroadsbacktooriginal) · [`SetRoadsBackToOriginalInAngledArea`](#setroadsbacktooriginalinangledarea) · [`SetRoadsInAngledArea`](#setroadsinangledarea) · [`SetRoadsInArea`](#setroadsinarea) · [`UpdateNavmeshBlockingObject`](#updatenavmeshblockingobject)

---
### AddNavmeshBlockingObject

`ADD_NAVMESH_BLOCKING_OBJECT` · hash `0xFCD5C8E06E502F5A` · jhash `0x2952BA56` · **Cliente**

```lua
local retval = AddNavmeshBlockingObject(x, y, z, width, length, height, heading, bPermanent, flags)
```
```c
Any ADD_NAVMESH_BLOCKING_OBJECT(float x, float y, float z, float width, float length, float height, float heading, BOOL bPermanent, int flags);
```

**Parámetros**

- `x` (`float`): The x coordinate to create the block on.
- `y` (`float`): The y coordinate.
- `z` (`float`): The z coordinate.
- `width` (`float`): The width of the block.
- `length` (`float`): The length of the block.
- `height` (`float`): The height of the block.
- `heading` (`float`): The heading of object in degrees.
- `bPermanent` (`BOOL`): A boolean indicating if the blocking object is permanent (`true`/`false`).
- `flags` (`int`): Flag for the blocking object, refer to `eBlockingObjectFlags`.

**Devuelve:** `Any`

**Descripción oficial:**

Creates a navmesh blocking object, vehicles will avoid driving through this area.

Only 32 blocking objects may exist at a given time and must be manually managed. See [`REMOVE_NAVMESH_BLOCKING_OBJECT`](#removenavmeshblockingobject) and [`onResourceStop`](https://docs.fivem.net/docs/scripting-reference/events/list/onResourceStop/)

```cpp
enum eBlockingObjectFlags {
    // Default Flag
    BLOCKING_OBJECT_DEFAULT = 0,
    // Blocking object will block wander paths
    BLOCKING_OBJECT_WANDERPATH = 1,
    // Blocking object will block (regular) shortest-paths
    BLOCKING_OBJECT_SHORTESTPATH = 2,
    // Blocking object will block flee paths
    BLOCKING_OBJECT_FLEEPATH = 4,
    // Blocking object will block all paths
    BLOCKING_OBJECT_ALLPATHS = 7,
}
```

---
### AddNavmeshRequiredRegion

`ADD_NAVMESH_REQUIRED_REGION` · hash `0x387EAD7EE42F6685` · jhash `0x12B086EA` · **Cliente**

```lua
AddNavmeshRequiredRegion(x, y, radius)
```
```c
void ADD_NAVMESH_REQUIRED_REGION(float x, float y, float radius);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `radius` (`float`)

**Devuelve:** `void`

---
### AreAllNavmeshRegionsLoaded

`ARE_ALL_NAVMESH_REGIONS_LOADED` · hash `0x8415D95B194A3AEA` · jhash `0x34C4E789` · **Cliente**

```lua
local retval = AreAllNavmeshRegionsLoaded()
```
```c
BOOL ARE_ALL_NAVMESH_REGIONS_LOADED();
```

**Devuelve:** `BOOL`

---
### AreNodesLoadedForArea

`ARE_NODES_LOADED_FOR_AREA` · hash `0xF7B79A50B905A30D` · jhash `0x86E80A17` · **Cliente**

```lua
local retval = AreNodesLoadedForArea(x1, y1, x2, y2)
```
```c
BOOL ARE_NODES_LOADED_FOR_AREA(float x1, float y1, float x2, float y2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `x2` (`float`)
- `y2` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF7B79A50B905A30D` (`N_0xf7b79a50b905a30d`), `_ARE_PATH_NODES_LOADED_IN_AREA` (`ArePathNodesLoadedInArea`)

---
### CalculateTravelDistanceBetweenPoints

`CALCULATE_TRAVEL_DISTANCE_BETWEEN_POINTS` · hash `0xADD95C7005C4A197` · jhash `0xB114489B` · **Cliente**

```lua
local retval = CalculateTravelDistanceBetweenPoints(x1, y1, z1, x2, y2, z2)
```
```c
float CALCULATE_TRAVEL_DISTANCE_BETWEEN_POINTS(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

Calculates the travel distance between a set of points.
Doesn't seem to correlate with distance on gps sometimes.

This function returns the value 100000.0 over long distances, seems to be a failure mode result, potentially occurring when not all path nodes are loaded into pathfind.

---
### ClearGpsDisabledZoneAtIndex

`CLEAR_GPS_DISABLED_ZONE_AT_INDEX` · hash `0x2801D0012266DF07` · jhash `0x59090745` · **Cliente**

```lua
ClearGpsDisabledZoneAtIndex(index)
```
```c
void CLEAR_GPS_DISABLED_ZONE_AT_INDEX(int index);
```

**Parámetros**

- `index` (`int`): Index of disabled zone.

**Devuelve:** `void`

**Descripción oficial:**

Clears a disabled GPS route area from a certain index previously set using [`SET_GPS_DISABLED_ZONE_AT_INDEX`](#setgpsdisabledzoneatindex).

**Nombres antiguos (alias):** `0x2801D0012266DF07` (`N_0x2801d0012266df07`), `_CLEAR_GPS_DISABLED_ZONE_AT_INDEX` (`ClearGpsDisabledZoneAtIndex`)

---
### DisableNavmeshInArea

`DISABLE_NAVMESH_IN_AREA` · hash `0x4C8872D8CDBE1B8B` · jhash `0x6E37F132` · **Cliente**

```lua
DisableNavmeshInArea(posMinX, posMinY, posMinZ, posMaxX, posMaxY, posMaxZ, bDisable)
```
```c
void DISABLE_NAVMESH_IN_AREA(float posMinX, float posMinY, float posMinZ, float posMaxX, float posMaxY, float posMaxZ, bool bDisable);
```

**Parámetros**

- `posMinX` (`float`): X Min Coordinate.
- `posMinY` (`float`): Y Min Coordinate.
- `posMinZ` (`float`): Z Min Coordinate.
- `posMaxX` (`float`): X Max Coordinate.
- `posMaxY` (`float`): Y Max Coordinate.
- `posMaxZ` (`float`): Z Max Coordinate.
- `bDisable` (`bool`): Whether to disable the navmesh or not.

**Devuelve:** `void`

**Descripción oficial:**

Use this if you want to completely disable a large area of navmesh.
For smaller areas, use [`ADD_NAVMESH_BLOCKING_OBJECT`](#addnavmeshblockingobject) instead.

---
### DoesNavmeshBlockingObjectExist

`DOES_NAVMESH_BLOCKING_OBJECT_EXIST` · hash `0x0EAEB0DB4B132399` · jhash `0x4B67D7EE` · **Cliente**

```lua
local retval = DoesNavmeshBlockingObjectExist(p0)
```
```c
BOOL DOES_NAVMESH_BLOCKING_OBJECT_EXIST(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x0EAEB0DB4B132399` (`N_0x0eaeb0db4b132399`)

---
### GenerateDirectionsToCoord

`GENERATE_DIRECTIONS_TO_COORD` · hash `0xF90125F1F79ECDF8` · jhash `0xED35C094` · **Cliente**

```lua
local retval, direction, vehicle, distToNxJunction = GenerateDirectionsToCoord(x, y, z, p3)
```
```c
int GENERATE_DIRECTIONS_TO_COORD(float x, float y, float z, BOOL p3, int* direction, float* vehicle, float* distToNxJunction);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`BOOL`)
- `direction` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `vehicle` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `distToNxJunction` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `int`

**Descripción oficial:**

```
p3 is 0 in the only game script occurrence (trevor3) but 1 doesn't seem to make a difference
distToNxJunction seems to be the distance in metres * 10.0f
direction:
0 = This happens randomly during the drive for seemingly no reason but if you consider that this native is only used in trevor3, it seems to mean "Next frame, stop whatever's being said and tell the player the direction."
1 = Route is being calculated or the player is going in the wrong direction
2 = Please Proceed the Highlighted Route
3 = In (distToNxJunction) Turn Left
4 = In (distToNxJunction) Turn Right
5 = In (distToNxJunction) Keep Straight
6 = In (distToNxJunction) Turn Sharply To The Left
7 = In (distToNxJunction) Turn Sharply To The Right
8 = Route is being recalculated or the navmesh is confusing. This happens randomly during the drive but consistently at {2044.0358, 2996.6116, 44.9717} if you face towards the bar and the route needs you to turn right. In that particular case, it could be a bug with how the turn appears to be 270 deg. CCW instead of "right." Either way, this seems to be the engine saying "I don't know the route right now."
return value set to 0 always
```

---
### GetClosestMajorVehicleNode

`GET_CLOSEST_MAJOR_VEHICLE_NODE` · hash `0x2EABE3B06F58C1BE` · jhash `0x04B5F15B` · **Cliente**

```lua
local retval, outPosition = GetClosestMajorVehicleNode(x, y, z, zMeasureMult, zTolerance)
```
```c
BOOL GET_CLOSEST_MAJOR_VEHICLE_NODE(float x, float y, float z, Vector3* outPosition, float zMeasureMult, int zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes coords
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`int`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `BOOL` — Returns the closest major vehicle node.

**Descripción oficial:**

Same as [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode), but with the node flag `GCNF_INCLUDE_SWITCHED_OFF_NODES` set.

---
### GetClosestRoad

`GET_CLOSEST_ROAD` · hash `0x132F52BBA570FE92` · jhash `0x567B0E11` · **Cliente**

```lua
local retval, srcNode, targetNode, laneCountForward, laneCountBackward, width = GetClosestRoad(x, y, z, minimumEdgeLength, minimumLaneCount, onlyMajorRoads)
```
```c
bool GET_CLOSEST_ROAD(float x, float y, float z, float minimumEdgeLength, int minimumLaneCount, Vector3* srcNode, Vector3* targetNode, int* laneCountForward, int* laneCountBackward, float* width, BOOL onlyMajorRoads);
```

**Parámetros**

- `x` (`float`): x position
- `y` (`float`): y position
- `z` (`float`): z position
- `minimumEdgeLength` (`float`): Minimum distance the srcNode must be from the targetNode.
- `minimumLaneCount` (`int`): Minimum number of lanes the connection must have.
- `srcNode` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Position of the edge source
- `targetNode` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Position of the edge target
- `laneCountForward` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Lane count forward
- `laneCountBackward` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Lane count backwards
- `width` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Width of gap in middle of road between forward and backward lanes.
- `onlyMajorRoads` (`BOOL`): Return major roads only.

**Devuelve:** `bool` — Returns `true` if a road was found, `false` otherwise.

**Descripción oficial:**

Finds an edge (node connection to another node) that satisfies the specified criteria.

---
### GetClosestVehicleNode

`GET_CLOSEST_VEHICLE_NODE` · hash `0x240A18690AE96513` · jhash `0x6F5F1E6C` · **Cliente**

```lua
local retval, outPosition = GetClosestVehicleNode(x, y, z, nodeFlags, zMeasureMult, zTolerance)
```
```c
BOOL GET_CLOSEST_VEHICLE_NODE(float x, float y, float z, Vector3* outPosition, int nodeFlags, float zMeasureMult, float zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes coords
- `nodeFlags` (`int`): Node flags
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`float`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `BOOL` — Returns the closest vehicle node matching the node flags.

**Descripción oficial:**

```cpp
enum eGetClosestNodeFlags {
    GCNF_INCLUDE_SWITCHED_OFF_NODES = 1,
    GCNF_INCLUDE_BOAT_NODES = 2,
    GCNF_IGNORE_SLIPLANES = 4,
    GCNF_IGNORE_SWITCHED_OFF_DEADENDS = 8,
    GCNF_GET_HEADING = 256,
    GCNF_FAVOUR_FACING = 512
}
```

---
### GetClosestVehicleNodeWithHeading

`GET_CLOSEST_VEHICLE_NODE_WITH_HEADING` · hash `0xFF071FB798B803B0` · jhash `0x8BD5759B` · **Cliente**

```lua
local retval, outPosition, outHeading = GetClosestVehicleNodeWithHeading(x, y, z, nodeFlags, zMeasureMult, zTolerance)
```
```c
BOOL GET_CLOSEST_VEHICLE_NODE_WITH_HEADING(float x, float y, float z, Vector3* outPosition, float* outHeading, int nodeFlags, float zMeasureMult, int zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes coords
- `outHeading` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes heading
- `nodeFlags` (`int`): Node flags, see [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode)
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`int`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `BOOL` — Returns the closest vehicle node with its heading.

**Descripción oficial:**

Same as [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode), but with the node flag `GCNF_GET_HEADING` set, causing the native to also return the heading.

---
### GetGpsBlipRouteFound

`GET_GPS_BLIP_ROUTE_FOUND` · hash `0x869DAACBBE9FA006` · jhash `0x286F82CC` · **Cliente**

```lua
local retval = GetGpsBlipRouteFound()
```
```c
BOOL GET_GPS_BLIP_ROUTE_FOUND();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x869DAACBBE9FA006` (`N_0x869daacbbe9fa006`)

---
### GetGpsBlipRouteLength

`GET_GPS_BLIP_ROUTE_LENGTH` · hash `0xBBB45C3CF5C8AA85` · jhash `0x4B770634` · **Cliente**

```lua
local retval = GetGpsBlipRouteLength()
```
```c
int GET_GPS_BLIP_ROUTE_LENGTH();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0xBBB45C3CF5C8AA85` (`N_0xbbb45c3cf5c8aa85`)

---
### GetHeightmapBottomZForArea

`_GET_HEIGHTMAP_BOTTOM_Z_FOR_AREA` · hash `0x3599D741C9AC6310` · jhash `0x76751DD4` · **Cliente**

```lua
local retval = GetHeightmapBottomZForArea(x1, y1, x2, y2)
```
```c
float _GET_HEIGHTMAP_BOTTOM_Z_FOR_AREA(float x1, float y1, float x2, float y2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `x2` (`float`)
- `y2` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns CGameWorldHeightMap's minimum Z among all grid nodes that intersect with the specified rectangle.
```

**Nombres antiguos (alias):** `0x3599D741C9AC6310` (`N_0x3599d741c9ac6310`)

---
### GetHeightmapBottomZForPosition

`_GET_HEIGHTMAP_BOTTOM_Z_FOR_POSITION` · hash `0x336511A34F2E5185` · jhash `0xA07C5B7D` · **Cliente**

```lua
local retval = GetHeightmapBottomZForPosition(x, y)
```
```c
float _GET_HEIGHTMAP_BOTTOM_Z_FOR_POSITION(float x, float y);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns CGameWorldHeightMap's minimum Z value at specified point (grid node).
```

**Nombres antiguos (alias):** `0x336511A34F2E5185` (`N_0x336511a34f2e5185`)

---
### GetHeightmapTopZForArea

`_GET_HEIGHTMAP_TOP_Z_FOR_AREA` · hash `0x8ABE8608576D9CE3` · jhash `0x3ED21C90` · **Cliente**

```lua
local retval = GetHeightmapTopZForArea(x1, y1, x2, y2)
```
```c
float _GET_HEIGHTMAP_TOP_Z_FOR_AREA(float x1, float y1, float x2, float y2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `x2` (`float`)
- `y2` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns CGameWorldHeightMap's maximum Z among all grid nodes that intersect with the specified rectangle.
```

**Nombres antiguos (alias):** `0x8ABE8608576D9CE3` (`N_0x8abe8608576d9ce3`)

---
### GetHeightmapTopZForPosition

`_GET_HEIGHTMAP_TOP_Z_FOR_POSITION` · hash `0x29C24BFBED8AB8FB` · jhash `0x3FE8C5A0` · **Cliente**

```lua
local retval = GetHeightmapTopZForPosition(x, y)
```
```c
float _GET_HEIGHTMAP_TOP_Z_FOR_POSITION(float x, float y);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)

**Devuelve:** `float`

**Descripción oficial:**

```
Returns CGameWorldHeightMap's maximum Z value at specified point (grid node).
```

**Nombres antiguos (alias):** `0x29C24BFBED8AB8FB` (`N_0x29c24bfbed8ab8fb`)

---
### GetNextGpsDisabledZoneIndex

`GET_NEXT_GPS_DISABLED_ZONE_INDEX` · hash `0xD3A6A0EF48823A8C` · jhash `0xBE92551F` · **Cliente**

```lua
local retval = GetNextGpsDisabledZoneIndex(index)
```
```c
int GET_NEXT_GPS_DISABLED_ZONE_INDEX(int index);
```

**Parámetros**

- `index` (`int`)

**Devuelve:** `int` — The disabled zone index

**Descripción oficial:**

Gets the next zone that has been disabled using SET_GPS_DISABLED_ZONE_AT_INDEX.

```
NativeDB Removed Parameter 1: int index
```

**Nombres antiguos (alias):** `0xD3A6A0EF48823A8C` (`N_0xd3a6a0ef48823a8c`)

---
### GetNthClosestVehicleNode

`GET_NTH_CLOSEST_VEHICLE_NODE` · hash `0xE50E52416CCF948B` · jhash `0xF125BFCC` · **Cliente**

```lua
local retval, outPosition = GetNthClosestVehicleNode(x, y, z, nthClosest, nodeFlags, zMeasureMult, zTolerance)
```
```c
BOOL GET_NTH_CLOSEST_VEHICLE_NODE(float x, float y, float z, int nthClosest, Vector3* outPosition, int nodeFlags, float zMeasureMult, float zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `nthClosest` (`int`): The index of the node to return
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes coords
- `nodeFlags` (`int`): Node flags, see [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode)
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`float`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `BOOL` — Returns the nth closest vehicle node.

**Descripción oficial:**

Same as [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode), but returns the nth closest node instead of the first.

---
### GetNthClosestVehicleNodeFavourDirection

`GET_NTH_CLOSEST_VEHICLE_NODE_FAVOUR_DIRECTION` · hash `0x45905BE8654AE067` · jhash `0x928A4DEC` · **Cliente**

```lua
local retval, outPosition, outHeading = GetNthClosestVehicleNodeFavourDirection(x, y, z, desiredX, desiredY, desiredZ, nthClosest, nodeFlags, zMeasureMult, zTolerance)
```
```c
BOOL GET_NTH_CLOSEST_VEHICLE_NODE_FAVOUR_DIRECTION(float x, float y, float z, float desiredX, float desiredY, float desiredZ, int nthClosest, Vector3* outPosition, float* outHeading, int nodeFlags, float zMeasureMult, float zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `desiredX` (`float`): The X direction to favour
- `desiredY` (`float`): The Y direction to favour
- `desiredZ` (`float`): The Z direction to favour
- `nthClosest` (`int`): The index of the node to return
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes coords
- `outHeading` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes heading
- `nodeFlags` (`int`): Node flags, see [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode)
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`float`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `BOOL` — Returns the nth closest vehicle node with its heading favouring the desired direction.

**Descripción oficial:**

Like [`GET_CLOSEST_VEHICLE_NODE_WITH_HEADING`](#getclosestvehiclenodewithheading), but returns the nth closest node instead of the first.

---
### GetNthClosestVehicleNodeId

`GET_NTH_CLOSEST_VEHICLE_NODE_ID` · hash `0x22D7275A79FE8215` · jhash `0x3F358BEA` · **Cliente**

```lua
local retval = GetNthClosestVehicleNodeId(x, y, z, nthClosest, nodeFlags, zMeasureMult, zTolerance)
```
```c
int GET_NTH_CLOSEST_VEHICLE_NODE_ID(float x, float y, float z, int nthClosest, int nodeFlags, float zMeasureMult, float zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `nthClosest` (`int`): The index of the node to return
- `nodeFlags` (`int`): Node flags, see [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode)
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`float`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `int` — Returns the nth closest vehicle nodes id.

---
### GetNthClosestVehicleNodeIdWithHeading

`GET_NTH_CLOSEST_VEHICLE_NODE_ID_WITH_HEADING` · hash `0x6448050E9C2A7207` · jhash `0xC1AEB88D` · **Cliente**

```lua
local retval, outPosition, outHeading = GetNthClosestVehicleNodeIdWithHeading(x, y, z, nthClosest, nodeFlags, zMeasureMult, zTolerance)
```
```c
int GET_NTH_CLOSEST_VEHICLE_NODE_ID_WITH_HEADING(float x, float y, float z, int nthClosest, Vector3* outPosition, float* outHeading, int nodeFlags, float zMeasureMult, float zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `nthClosest` (`int`): The index of the node to return
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes coords
- `outHeading` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes heading
- `nodeFlags` (`int`): Node flags, see [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode)
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`float`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `int` — Returns the nth closest vehicle nodes id with its heading.

---
### GetNthClosestVehicleNodeWithHeading

`GET_NTH_CLOSEST_VEHICLE_NODE_WITH_HEADING` · hash `0x80CA6A8B6C094CC4` · jhash `0x7349C856` · **Cliente**

```lua
local retval, outPosition, outHeading, totalLanes = GetNthClosestVehicleNodeWithHeading(x, y, z, nthClosest, nodeFlags, zMeasureMult, zTolerance)
```
```c
BOOL GET_NTH_CLOSEST_VEHICLE_NODE_WITH_HEADING(float x, float y, float z, int nthClosest, Vector3* outPosition, float* outHeading, int* totalLanes, int nodeFlags, float zMeasureMult, float zTolerance);
```

**Parámetros**

- `x` (`float`): X coordinate
- `y` (`float`): Y coordinate
- `z` (`float`): Z coordinate
- `nthClosest` (`int`): The index of the node to return
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes coords
- `outHeading` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the found nodes heading
- `totalLanes` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Pointer to the total lanes (forward + backward) of the found node
- `nodeFlags` (`int`): Node flags, see [`GET_CLOSEST_VEHICLE_NODE`](#getclosestvehiclenode)
- `zMeasureMult` (`float`): How strongly the difference in the Z direction should be weighted
- `zTolerance` (`float`): How far apart the Z coords have to be before `zMeasureMult` kicks in

**Devuelve:** `BOOL` — Returns `true` if the node was found, or `false` if the node was not found, or was not streamed in.

**Descripción oficial:**

Get the nth closest vehicle node with its heading and total lane count. If you need specific forward and backward lane counts use [`GET_CLOSEST_ROAD`](#getclosestroad).

---
### GetNumNavmeshesExistingInArea

`GET_NUM_NAVMESHES_EXISTING_IN_AREA` · hash `0x01708E8DD3FF8C65` · jhash `0x76AFFBB5` · **Cliente**

```lua
local retval = GetNumNavmeshesExistingInArea(posMinX, posMinY, posMinZ, posMaxX, posMaxY, posMaxZ)
```
```c
int GET_NUM_NAVMESHES_EXISTING_IN_AREA(float posMinX, float posMinY, float posMinZ, float posMaxX, float posMaxY, float posMaxZ);
```

**Parámetros**

- `posMinX` (`float`): Min X Coordinate.
- `posMinY` (`float`): Min Y Coordinate.
- `posMinZ` (`float`): Min Z Coordinate.
- `posMaxX` (`float`): Max X Coordinate.
- `posMaxY` (`float`): Max Y Coordinate.
- `posMaxZ` (`float`): Max Z Coordinate.

**Devuelve:** `int` — Returns the number of navmeshes which exist in the given area (irrespective of whether they are currently loaded or not)

**Nombres antiguos (alias):** `0x01708E8DD3FF8C65` (`N_0x01708e8dd3ff8c65`)

---
### GetPointOnRoadSide

`_GET_POINT_ON_ROAD_SIDE` · hash `0x16F46FB18C8009E4` · jhash `0xF6422F9A` · **Cliente**

```lua
local retval, outPosition = GetPointOnRoadSide(x, y, z, p3, outPosition)
```
```c
BOOL _GET_POINT_ON_ROAD_SIDE(float x, float y, float z, int p3, Vector3* outPosition);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `p3` (`int`)
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x16F46FB18C8009E4` (`N_0x16f46fb18c8009e4`)

---
### GetPosAlongGpsTypeRoute

`GET_POS_ALONG_GPS_TYPE_ROUTE` · hash `0xF3162836C28F9DA5` · jhash `0x40BB1149` · **Cliente**

```lua
local retval, result = GetPosAlongGpsTypeRoute(bStartAtPlayerPos, fDistanceAlongRoute, slotType)
```
```c
BOOL GET_POS_ALONG_GPS_TYPE_ROUTE(Vector3* result, BOOL bStartAtPlayerPos, float fDistanceAlongRoute, int slotType);
```

**Parámetros**

- `result` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Coordinates of waypoint marker
- `bStartAtPlayerPos` (`BOOL`): Should we project distance from the player position or from next node.
- `fDistanceAlongRoute` (`float`): Distance we want to get the position along the route.
- `slotType` (`int`): Type of gps route to check against. See `eGpsSlotType`.

**Devuelve:** `BOOL` — will return `true` if a position is returned, `false` if not.

**Descripción oficial:**

Native to get a position along current player GPS route using supplied slot.
This native was previously named `GET_GPS_WAYPOINT_ROUTE_END`, but its named changed.

```cpp
enum eGpsSlotType {
	GPS_SLOT_WAYPOINT = 0,
	GPS_SLOT_RADAR_BLIP = 1,
	GPS_SLOT_DISCRETE = 2
}
```

**Nombres antiguos (alias):** `0xF3162836C28F9DA5` (`N_0xf3162836c28f9da5`), `GET_GPS_WAYPOINT_ROUTE_END` (`GetGpsWaypointRouteEnd`)

---
### GetRandomVehicleNode

`GET_RANDOM_VEHICLE_NODE` · hash `0x93E0DB8440B73A7D` · jhash `0xAD1476EA` · **Cliente**

```lua
local retval, outPosition, nodeId = GetRandomVehicleNode(x, y, z, radius, p4, p5, p6)
```
```c
BOOL GET_RANDOM_VEHICLE_NODE(float x, float y, float z, float radius, BOOL p4, BOOL p5, BOOL p6, Vector3* outPosition, int* nodeId);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)
- `p4` (`BOOL`)
- `p5` (`BOOL`)
- `p6` (`BOOL`)
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `nodeId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

---
### GetRoadBoundaryUsingHeading

`GET_ROAD_BOUNDARY_USING_HEADING` · hash `0xA0F8A7517A273C05` · jhash `0x5E440AC7` · **Cliente**

```lua
local retval, outPosition = GetRoadBoundaryUsingHeading(x, y, z, heading, outPosition)
```
```c
BOOL GET_ROAD_BOUNDARY_USING_HEADING(float x, float y, float z, float heading, Vector3* outPosition);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `heading` (`float`)
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA0F8A7517A273C05` (`N_0xa0f8a7517a273c05`), `_GET_ROAD_SIDE_POINT_WITH_HEADING` (`GetRoadSidePointWithHeading`)

---
### GetSafeCoordForPed

`GET_SAFE_COORD_FOR_PED` · hash `0xB61C8E878A4199CA` · jhash `0xB370270A` · **Cliente**

```lua
local retval, outPosition = GetSafeCoordForPed(x, y, z, onlyOnPavement, flags)
```
```c
BOOL GET_SAFE_COORD_FOR_PED(float x, float y, float z, BOOL onlyOnPavement, Vector3* outPosition, int flags);
```

**Parámetros**

- `x` (`float`): The X coordinate of the point to check.
- `y` (`float`): The Y coordinate of the point to check.
- `z` (`float`): The Z coordinate of the point to check.
- `onlyOnPavement` (`BOOL`): Sets the `GSC_FLAG_ONLY_PAVEMENT` flag.
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The location of the safe coord.
- `flags` (`int`): The search flags.

**Devuelve:** `BOOL` — Returns true if a safe coord was found and false otherwise.

**Descripción oficial:**

```cpp
enum eSafePositionFlags {
    // Only navmesh polygons marked as pavement
    GSC_FLAG_ONLY_PAVEMENT = 1,
    // Only navmesh polygons not marked as "isolated"
    GSC_FLAG_NOT_ISOLATED = 2,
    // No navmesh polygons created from interiors
    GSC_FLAG_NOT_INTERIOR = 4,
    // No navmesh polygons marked as water
    GSC_FLAG_NOT_WATER = 8,
    // Only navmesh polygons marked as "network spawn candidate"
    GSC_FLAG_ONLY_NETWORK_SPAWN = 16,
    // Specify whether to use a flood-fill from the starting position, as opposed to scanning all polygons within the search volume
    GSC_FLAG_USE_FLOOD_FILL = 32
}
```

---
### GetStreetNameAtCoord

`GET_STREET_NAME_AT_COORD` · hash `0x2EB41072B4C1E4C0` · jhash `0xDEBEEFCF` · **Cliente**

```lua
local streetName, crossingRoad = GetStreetNameAtCoord(x, y, z)
```
```c
void GET_STREET_NAME_AT_COORD(float x, float y, float z, Hash* streetName, Hash* crossingRoad);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `streetName` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `crossingRoad` (`Hash*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Determines the name of the street which is the closest to the given coordinates.
x,y,z - the coordinates of the street
streetName - returns a hash to the name of the street the coords are on
crossingRoad - if the coordinates are on an intersection, a hash to the name of the crossing road
Note: the names are returned as hashes, the strings can be returned using the function HUD::GET_STREET_NAME_FROM_HASH_KEY.
```

---
### GetVehicleNodeIsGpsAllowed

`GET_VEHICLE_NODE_IS_GPS_ALLOWED` · hash `0xA2AE5C478B96E3B6` · jhash `0xEE4B1219` · **Cliente**

```lua
local retval = GetVehicleNodeIsGpsAllowed(nodeID)
```
```c
BOOL GET_VEHICLE_NODE_IS_GPS_ALLOWED(int nodeID);
```

**Parámetros**

- `nodeID` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns false for nodes that aren't used for GPS routes.
Example:
Nodes in Fort Zancudo and LSIA are false
```

**Nombres antiguos (alias):** `0xA2AE5C478B96E3B6` (`N_0xa2ae5c478b96e3b6`), `_GET_SUPPORTS_GPS_ROUTE_FLAG` (`GetSupportsGpsRouteFlag`)

---
### GetVehicleNodeIsSwitchedOff

`GET_VEHICLE_NODE_IS_SWITCHED_OFF` · hash `0x4F5070AA58F69279` · jhash `0x56737A3C` · **Cliente**

```lua
local retval = GetVehicleNodeIsSwitchedOff(nodeID)
```
```c
BOOL GET_VEHICLE_NODE_IS_SWITCHED_OFF(int nodeID);
```

**Parámetros**

- `nodeID` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true when the node is Offroad. Alleys, some dirt roads, and carparks return true.
Normal roads where plenty of Peds spawn will return false
```

**Nombres antiguos (alias):** `0x4F5070AA58F69279` (`N_0x4f5070aa58f69279`), `_GET_IS_SLOW_ROAD_FLAG` (`GetIsSlowRoadFlag`)

---
### GetVehicleNodePosition

`GET_VEHICLE_NODE_POSITION` · hash `0x703123E5E7D429C2` · jhash `0xE38E252D` · **Cliente**

```lua
local outPosition = GetVehicleNodePosition(nodeId, outPosition)
```
```c
void GET_VEHICLE_NODE_POSITION(int nodeId, Vector3* outPosition);
```

**Parámetros**

- `nodeId` (`int`)
- `outPosition` (`Vector3*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Descripción oficial:**

```
Calling this with an invalid node id, will crash the game.
Note that IS_VEHICLE_NODE_ID_VALID simply checks if nodeId is not zero. It does not actually ensure that the id is valid.
Eg. IS_VEHICLE_NODE_ID_VALID(1) will return true, but will crash when calling GET_VEHICLE_NODE_POSITION().
```

---
### GetVehicleNodeProperties

`GET_VEHICLE_NODE_PROPERTIES` · hash `0x0568566ACBB5DEDC` · jhash `0xCC90110B` · **Cliente**

```lua
local retval, density, flags = GetVehicleNodeProperties(x, y, z)
```
```c
BOOL GET_VEHICLE_NODE_PROPERTIES(float x, float y, float z, int* density, int* flags);
```

**Parámetros**

- `x` (`float`): x position of search
- `y` (`float`): y position of search
- `z` (`float`): z position of search
- `density` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The traffic density the current node will spawn in a range of 0-15.
- `flags` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: The vehicle node flags, see `eVehicleNodeProperties`.

**Devuelve:** `BOOL` — Returns `true` if the node was found, or `false` if the node was not found, or was not streamed in.

**Descripción oficial:**

Gets the density and flags of the closest node to the specified position.\
Density is a value between 0 and 15, indicating how busy the road is.

```cpp
enum eVehicleNodeProperties {
	OFF_ROAD = 1 << 0,
	ON_PLAYERS_ROAD =  1 << 1,
	NO_BIG_VEHICLES = 1 << 2,
	SWITCHED_OFF = 1 << 3,
	TUNNEL_OR_INTERIOR = 1 << 4,
	LEADS_TO_DEAD_END = 1 << 5,
	HIGHWAY = 1 << 6,
	JUNCTION = 1 << 7,
	TRAFFIC_LIGHT = 1 << 8,
	GIVE_WAY = 1 << 9,
	WATER = 1 << 10,
}
```

---
### IsNavmeshLoadedInArea

`IS_NAVMESH_LOADED_IN_AREA` · hash `0xF813C7E63F9062A5` · jhash `0x4C2BA99E` · **Cliente**

```lua
local retval = IsNavmeshLoadedInArea(x1, y1, z1, x2, y2, z2)
```
```c
BOOL IS_NAVMESH_LOADED_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether navmesh for the region is loaded. The region is a rectangular prism defined by it's top left deepest corner to it's bottom right shallowest corner.  
If you can re-word this so it makes more sense, please do. I'm horrible with words sometimes...  
```

---
### IsNavmeshRequiredRegionOwnedByAnyThread

`_IS_NAVMESH_REQUIRED_REGION_OWNED_BY_ANY_THREAD` · hash `0x705A844002B39DC0` · **Cliente**

```lua
local retval = IsNavmeshRequiredRegionOwnedByAnyThread()
```
```c
BOOL _IS_NAVMESH_REQUIRED_REGION_OWNED_BY_ANY_THREAD();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
IS_*
```

**Nombres antiguos (alias):** `0x705A844002B39DC0` (`N_0x705a844002b39dc0`)

---
### IsPointOnRoad

`IS_POINT_ON_ROAD` · hash `0x125BF4ABFC536B09` · jhash `0xCF198055` · **Cliente**

```lua
local retval = IsPointOnRoad(x, y, z, vehicle)
```
```c
BOOL IS_POINT_ON_ROAD(float x, float y, float z, Vehicle vehicle);
```

**Parámetros**

- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Gets a value indicating whether the specified position is on a road.  
The vehicle parameter is not implemented (ignored).  
```

---
### IsVehicleNodeIdValid

`IS_VEHICLE_NODE_ID_VALID` · hash `0x1EAF30FCFBF5AF74` · jhash `0x57DFB1EF` · **Cliente**

```lua
local retval = IsVehicleNodeIdValid(vehicleNodeId)
```
```c
BOOL IS_VEHICLE_NODE_ID_VALID(int vehicleNodeId);
```

**Parámetros**

- `vehicleNodeId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if the id is non zero.  
```

---
### LoadAllPathNodes

`LOAD_ALL_PATH_NODES` · hash `0x80E4A6EDDB0BE8D9` · jhash `0xC66E28C3` · **Cliente**

```lua
local retval = LoadAllPathNodes(keepInMemory)
```
```c
BOOL LOAD_ALL_PATH_NODES(BOOL keepInMemory);
```

**Parámetros**

- `keepInMemory` (`BOOL`): if true, all path nodes will be loaded and be kept in memory; otherwise, all path nodes will be loaded, but unloaded as the game sees fit.

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This native has been removed in v1180.  
```

---
### N_0xaa76052dda9bfc3e

`0xAA76052DDA9BFC3E` · hash `0xAA76052DDA9BFC3E` · jhash `0xD0F51299` · **Cliente**

```lua
N_0xaa76052dda9bfc3e(p0, p1, p2, p3, p4, p5, p6)
```
```c
void 0xAA76052DDA9BFC3E(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5, Any p6);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)
- `p6` (`Any`)

**Devuelve:** `void`

---
### RemoveNavmeshBlockingObject

`REMOVE_NAVMESH_BLOCKING_OBJECT` · hash `0x46399A7895957C0E` · jhash `0x098602B0` · **Cliente**

```lua
RemoveNavmeshBlockingObject(p0)
```
```c
void REMOVE_NAVMESH_BLOCKING_OBJECT(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `void`

---
### RemoveNavmeshRequiredRegions

`REMOVE_NAVMESH_REQUIRED_REGIONS` · hash `0x916F0A3CDEC3445E` · jhash `0x637BB680` · **Cliente**

```lua
RemoveNavmeshRequiredRegions()
```
```c
void REMOVE_NAVMESH_REQUIRED_REGIONS();
```

**Devuelve:** `void`

---
### RequestPathsPreferAccurateBoundingstruct

`_REQUEST_PATHS_PREFER_ACCURATE_BOUNDINGSTRUCT` · hash `0x07FB139B592FA687` · jhash `0x2CDA5012` · **Cliente**

```lua
local retval = RequestPathsPreferAccurateBoundingstruct(x1, y1, x2, y2)
```
```c
BOOL _REQUEST_PATHS_PREFER_ACCURATE_BOUNDINGSTRUCT(float x1, float y1, float x2, float y2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `x2` (`float`)
- `y2` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Used internally for long range tasks
```

**Nombres antiguos (alias):** `0x07FB139B592FA687` (`N_0x07fb139b592fa687`)

---
### SetAiGlobalPathNodesType

`_SET_AI_GLOBAL_PATH_NODES_TYPE` · hash `0xF74B1FFA4A15FBEA` · **Cliente**

```lua
SetAiGlobalPathNodesType(type)
```
```c
void _SET_AI_GLOBAL_PATH_NODES_TYPE(int type);
```

**Parámetros**

- `type` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

Activates Cayo Perico path nodes if passed `1`. GPS navigation will start working, maybe more stuff will change, not sure. It seems if you try to unload (pass `0`) when close to the island, your game might crash.

```
NativeDB Introduced: v2189
```

---
### SetAllPathsCacheBoundingstruct

`_SET_ALL_PATHS_CACHE_BOUNDINGSTRUCT` · hash `0x228E5C6AD4D74BFD` · jhash `0xD6A3B458` · **Cliente**

```lua
SetAllPathsCacheBoundingstruct(toggle)
```
```c
void _SET_ALL_PATHS_CACHE_BOUNDINGSTRUCT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
Toggles a global boolean, name is probably a hash collision but describes its functionality.
```

**Nombres antiguos (alias):** `0x228E5C6AD4D74BFD` (`N_0x228e5c6ad4d74bfd`)

---
### SetAmbientPedRangeMultiplierThisFrame

`SET_AMBIENT_PED_RANGE_MULTIPLIER_THIS_FRAME` · hash `0x0B919E1FB47CC4E0` · jhash `0x3C5085E4` · **Cliente**

```lua
SetAmbientPedRangeMultiplierThisFrame(multiplier)
```
```c
void SET_AMBIENT_PED_RANGE_MULTIPLIER_THIS_FRAME(float multiplier);
```

**Parámetros**

- `multiplier` (`float`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x0B919E1FB47CC4E0` (`N_0x0b919e1fb47cc4e0`)

---
### SetGpsDisabledZone

`SET_GPS_DISABLED_ZONE` · hash `0xDC20483CD3DD5201` · jhash `0x720B8073` · **Cliente**

```lua
SetGpsDisabledZone(x1, y1, z1, x2, y2, z2)
```
```c
void SET_GPS_DISABLED_ZONE(float x1, float y1, float z1, float x2, float y2, float z2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)

**Devuelve:** `void`

---
### SetGpsDisabledZoneAtIndex

`SET_GPS_DISABLED_ZONE_AT_INDEX` · hash `0xD0BC1C6FB18EE154` · jhash `0x98BDB311` · **Cliente**

```lua
SetGpsDisabledZoneAtIndex(x1, y1, z1, x2, y2, z2, index)
```
```c
void SET_GPS_DISABLED_ZONE_AT_INDEX(float x1, float y1, float z1, float x2, float y2, float z2, int index);
```

**Parámetros**

- `x1` (`float`): X coordinate of first vector.
- `y1` (`float`): Y coordinate of first vector.
- `z1` (`float`): Z coordinate of first vector.
- `x2` (`float`): X coordinate of second vector.
- `y2` (`float`): Y coordinate of second vector.
- `z2` (`float`): Z coordinate of second vector.
- `index` (`int`): Index of zone.

**Devuelve:** `void`

**Descripción oficial:**

Disables the GPS route displayed on the minimap while within a certain zone (area). When in a disabled zone and creating a waypoint, the GPS route is not shown on the minimap until you are outside of the zone. When disabled, the direct distance is shown on minimap opposed to distance to travel. Seems to only work before setting a waypoint.

You can clear the disabled zone with CLEAR_GPS_DISABLED_ZONE_AT_INDEX.

**Setting a waypoint at the same coordinate:**

Disabled Zone:

![](https://i.imgur.com/vsxkvjC.png)

Enabled Zone (normal):

![](https://i.imgur.com/OUZYLWL.png)

**Nombres antiguos (alias):** `0xD0BC1C6FB18EE154` (`N_0xd0bc1c6fb18ee154`)

---
### SetIgnoreNoGpsFlag

`SET_IGNORE_NO_GPS_FLAG` · hash `0x72751156E7678833` · jhash `0xB72CF194` · **Cliente**

```lua
SetIgnoreNoGpsFlag(toggle)
```
```c
void SET_IGNORE_NO_GPS_FLAG(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetIgnoreSecondaryRouteNodes

`_SET_IGNORE_SECONDARY_ROUTE_NODES` · hash `0x1FC289A0C3FF470F` · jhash `0x90DF7A4C` · **Cliente**

```lua
SetIgnoreSecondaryRouteNodes(toggle)
```
```c
void _SET_IGNORE_SECONDARY_ROUTE_NODES(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
See: SET_BLIP_ROUTE
```

**Nombres antiguos (alias):** `0x1FC289A0C3FF470F` (`N_0x1fc289a0c3ff470f`)

---
### SetPedPathsBackToOriginal

`SET_PED_PATHS_BACK_TO_ORIGINAL` · hash `0xE04B48F2CC926253` · jhash `0x3F1ABDA4` · **Cliente**

```lua
SetPedPathsBackToOriginal(p0, p1, p2, p3, p4, p5)
```
```c
void SET_PED_PATHS_BACK_TO_ORIGINAL(Any p0, Any p1, Any p2, Any p3, Any p4, Any p5);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any`)
- `p2` (`Any`)
- `p3` (`Any`)
- `p4` (`Any`)
- `p5` (`Any`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 7: Any p6
```

---
### SetPedPathsInArea

`SET_PED_PATHS_IN_AREA` · hash `0x34F060F4BF92E018` · jhash `0x2148EA84` · **Cliente**

```lua
SetPedPathsInArea(x1, y1, z1, x2, y2, z2, unknown)
```
```c
void SET_PED_PATHS_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2, BOOL unknown);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `unknown` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Added Parameter 8: Any p7
```

---
### SetRoadsBackToOriginal

`SET_ROADS_BACK_TO_ORIGINAL` · hash `0x1EE7063B80FFC77C` · jhash `0x86AC4A85` · **Cliente**

```lua
SetRoadsBackToOriginal(p0, p1, p2, p3, p4, p5)
```
```c
void SET_ROADS_BACK_TO_ORIGINAL(float p0, float p1, float p2, float p3, float p4, float p5);
```

**Parámetros**

- `p0` (`float`)
- `p1` (`float`)
- `p2` (`float`)
- `p3` (`float`)
- `p4` (`float`)
- `p5` (`float`)

**Devuelve:** `void`

**Descripción oficial:**

```
missing a last parameter int p6  
```

```
NativeDB Added Parameter 7: Any p6
```

---
### SetRoadsBackToOriginalInAngledArea

`SET_ROADS_BACK_TO_ORIGINAL_IN_ANGLED_AREA` · hash `0x0027501B9F3B407E` · jhash `0x9DB5D209` · **Cliente**

```lua
SetRoadsBackToOriginalInAngledArea(x1, y1, z1, x2, y2, z2, width)
```
```c
void SET_ROADS_BACK_TO_ORIGINAL_IN_ANGLED_AREA(float x1, float y1, float z1, float x2, float y2, float z2, float width);
```

**Parámetros**

- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area

**Devuelve:** `void`

**Descripción oficial:**

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

```
NativeDB Added Parameter 8: Any p7

bool p7 - always 1  
```

---
### SetRoadsInAngledArea

`SET_ROADS_IN_ANGLED_AREA` · hash `0x1A5AA1208AF5DB59` · jhash `0xBD088F4B` · **Cliente**

```lua
SetRoadsInAngledArea(x1, y1, z1, x2, y2, z2, width, unknown1, unknown2, unknown3)
```
```c
void SET_ROADS_IN_ANGLED_AREA(float x1, float y1, float z1, float x2, float y2, float z2, float width, BOOL unknown1, BOOL unknown2, BOOL unknown3);
```

**Parámetros**

- `x1` (`float`): X dimension of the angled area 'origin'
- `y1` (`float`): Y dimension of the angled area 'origin'
- `z1` (`float`): Z dimension of the angled area 'origin'
- `x2` (`float`): X dimension of the angled area 'extent'
- `y2` (`float`): Y dimension of the angled area 'extent'
- `z2` (`float`): Z dimension of the angled area 'extent'
- `width` (`float`): Width of the angled area
- `unknown1` (`BOOL`)
- `unknown2` (`BOOL`)
- `unknown3` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

unknown3 is related to `SEND_SCRIPT_WORLD_STATE_EVENT > CNetworkRoadNodeWorldStateData` in networked environments.

See [`IS_POINT_IN_ANGLED_AREA`](OBJECT.md#ispointinangledarea) for the definition of an angled area.

---
### SetRoadsInArea

`SET_ROADS_IN_AREA` · hash `0xBF1A602B5BA52FEE` · jhash `0xEBC7B918` · **Cliente**

```lua
SetRoadsInArea(x1, y1, z1, x2, y2, z2, nodeEnabled, unknown2)
```
```c
void SET_ROADS_IN_AREA(float x1, float y1, float z1, float x2, float y2, float z2, BOOL nodeEnabled, BOOL unknown2);
```

**Parámetros**

- `x1` (`float`)
- `y1` (`float`)
- `z1` (`float`)
- `x2` (`float`)
- `y2` (`float`)
- `z2` (`float`)
- `nodeEnabled` (`BOOL`)
- `unknown2` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

When this is set to false, all nodes in the area get disabled.

`GET_VEHICLE_NODE_IS_SWITCHED_OFF` returns true afterwards.

If it's true,

`GET_VEHICLE_NODE_IS_SWITCHED_OFF` returns false.

---
### UpdateNavmeshBlockingObject

`UPDATE_NAVMESH_BLOCKING_OBJECT` · hash `0x109E99373F290687` · jhash `0x4E9776D0` · **Cliente**

```lua
UpdateNavmeshBlockingObject(object, posX, posY, posZ, scaleX, scaleY, scaleZ, heading, flags)
```
```c
void UPDATE_NAVMESH_BLOCKING_OBJECT(Object object, float posX, float posY, float posZ, float scaleX, float scaleY, float scaleZ, float heading, int flags);
```

**Parámetros**

- `object` (`Object`): Navmesh Blocking Object by ID. must be returned by [`ADD_NAVMESH_BLOCKING_OBJECT`](#addnavmeshblockingobject).
- `posX` (`float`): X position coordinate.
- `posY` (`float`): Y position coordinate.
- `posZ` (`float`): Z position coordinate.
- `scaleX` (`float`): X Scale.
- `scaleY` (`float`): Y Scale.
- `scaleZ` (`float`): Z Scale.
- `heading` (`float`): Heading of the blocking object.
- `flags` (`int`): Flags for the blocking object, see [`ADD_NAVMESH_BLOCKING_OBJECT`](#addnavmeshblockingobject) for list of blocking object flags.

**Devuelve:** `void`

---
