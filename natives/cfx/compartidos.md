# Natives de FiveM (CFX) — cliente y servidor

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

**98** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddConvarChangeListener`](#addconvarchangelistener) · [`AddStateBagChangeHandler`](#addstatebagchangehandler) · [`CancelEvent`](#cancelevent) · [`CreateColshapeCircle`](#createcolshapecircle) · [`CreateColshapeCuboid`](#createcolshapecuboid) · [`CreateColshapeCylinder`](#createcolshapecylinder) · [`CreateColshapePolygon`](#createcolshapepolygon) · [`CreateColshapeRectangle`](#createcolshaperectangle) · [`CreateColshapeSphere`](#createcolshapesphere) · [`DeleteColshape`](#deletecolshape) · [`DeleteFunctionReference`](#deletefunctionreference) · [`DeleteResourceKvp`](#deleteresourcekvp) · [`DeleteResourceKvpNoSync`](#deleteresourcekvpnosync) · [`DoesColshapeExist`](#doescolshapeexist) · [`DoesTrainStopAtStations`](#doestrainstopatstations) · [`DuplicateFunctionReference`](#duplicatefunctionreference) · [`EndFindKvp`](#endfindkvp) · [`EnsureEntityStateBag`](#ensureentitystatebag) · [`ExecuteCommand`](#executecommand) · [`FindKvp`](#findkvp) · [`FormatStackTrace`](#formatstacktrace) · [`GetColshapeCircleData`](#getcolshapecircledata) · [`GetColshapeCuboidData`](#getcolshapecuboiddata) · [`GetColshapeCylinderData`](#getcolshapecylinderdata) · [`GetColshapePolygonData`](#getcolshapepolygondata) · [`GetColshapeRectangleData`](#getcolshaperectangledata) · [`GetColshapeSphereData`](#getcolshapespheredata) · [`GetConvar`](#getconvar) · [`GetConvarBool`](#getconvarbool) · [`GetConvarFloat`](#getconvarfloat) · [`GetConvarInt`](#getconvarint) · [`GetCurrentResourceName`](#getcurrentresourcename) · [`GetEntitiesInRadius`](#getentitiesinradius) · [`GetEntityFromStateBagName`](#getentityfromstatebagname) · [`GetGameBuildNumber`](#getgamebuildnumber) · [`GetGameName`](#getgamename) · [`GetGamePool`](#getgamepool) · [`GetInstanceId`](#getinstanceid) · [`GetInvokingResource`](#getinvokingresource) · [`GetNumResourceMetadata`](#getnumresourcemetadata) · [`GetNumResources`](#getnumresources) · [`GetPlayerFromStateBagName`](#getplayerfromstatebagname) · [`GetPlayerMeleeWeaponDamageModifier`](#getplayermeleeweapondamagemodifier) · [`GetPlayerWeaponDamageModifier`](#getplayerweapondamagemodifier) · [`GetPlayerWeaponDefenseModifier`](#getplayerweapondefensemodifier) · [`GetPlayerWeaponDefenseModifier_2`](#getplayerweapondefensemodifier_2) · [`GetRegisteredCommands`](#getregisteredcommands) · [`GetResourceByFindIndex`](#getresourcebyfindindex) · [`GetResourceCommands`](#getresourcecommands) · [`GetResourceKvpFloat`](#getresourcekvpfloat) · [`GetResourceKvpInt`](#getresourcekvpint) · [`GetResourceKvpString`](#getresourcekvpstring) · [`GetResourceMetadata`](#getresourcemetadata) · [`GetResourceState`](#getresourcestate) · [`GetStateBagKeys`](#getstatebagkeys) · [`GetStateBagValue`](#getstatebagvalue) · [`GetTrainCruiseSpeed`](#gettraincruisespeed) · [`GetTrainDirection`](#gettraindirection) · [`GetTrainState`](#gettrainstate) · [`GetTrainTrackIndex`](#gettraintrackindex) · [`GetVehicleHandbrake`](#getvehiclehandbrake) · [`GetVehicleSteeringAngle`](#getvehiclesteeringangle) · [`GetVehicleType`](#getvehicletype) · [`IsAceAllowed`](#isaceallowed) · [`IsColshapeCircle`](#iscolshapecircle) · [`IsColshapeCuboid`](#iscolshapecuboid) · [`IsColshapeCylinder`](#iscolshapecylinder) · [`IsColshapeEntityTypeSet`](#iscolshapeentitytypeset) · [`IsColshapePolygon`](#iscolshapepolygon) · [`IsColshapeRectangle`](#iscolshaperectangle) · [`IsColshapeSphere`](#iscolshapesphere) · [`IsDuplicityVersion`](#isduplicityversion) · [`IsEntityPositionFrozen`](#isentitypositionfrozen) · [`IsPointInsideColshape`](#ispointinsidecolshape) · [`IsPrincipalAceAllowed`](#isprincipalaceallowed) · [`IsVehicleEngineStarting`](#isvehicleenginestarting) · [`LoadResourceFile`](#loadresourcefile) · [`NetworkGetEntityOwner`](#networkgetentityowner) · [`ProfilerEnterScope`](#profilerenterscope) · [`ProfilerExitScope`](#profilerexitscope) · [`ProfilerIsRecording`](#profilerisrecording) · [`RegisterCommand`](#registercommand) · [`RegisterResourceAsEventHandler`](#registerresourceaseventhandler) · [`RemoveConvarChangeListener`](#removeconvarchangelistener) · [`RemoveStateBagChangeHandler`](#removestatebagchangehandler) · [`SetColshapeEntityType`](#setcolshapeentitytype) · [`SetResourceKvp`](#setresourcekvp) · [`SetResourceKvpFloat`](#setresourcekvpfloat) · [`SetResourceKvpFloatNoSync`](#setresourcekvpfloatnosync) · [`SetResourceKvpInt`](#setresourcekvpint) · [`SetResourceKvpIntNoSync`](#setresourcekvpintnosync) · [`SetResourceKvpNoSync`](#setresourcekvpnosync) · [`SetStateBagValue`](#setstatebagvalue) · [`StartFindKvp`](#startfindkvp) · [`StateBagHasKey`](#statebaghaskey) · [`TriggerEventInternal`](#triggereventinternal) · [`UnregisterCommand`](#unregistercommand) · [`WasEventCanceled`](#waseventcanceled)

---
### AddConvarChangeListener

`ADD_CONVAR_CHANGE_LISTENER` · hash `0xAB7F7241` · **Cliente y servidor**

```lua
local retval = AddConvarChangeListener(conVarFilter, handler)
```
```c
int ADD_CONVAR_CHANGE_LISTENER(char* conVarFilter, func handler);
```

**Parámetros**

- `conVarFilter` (`char*`): The Console Variable to listen for, this can be a pattern like "test:\*", or null for any
- `handler` (`func`): The handler function.

**Devuelve:** `int` — A cookie to remove the change handler.

**Descripción oficial:**

Adds a listener for Console Variable changes.

The function called expects to match the following signature:

```ts
function ConVarChangeListener(conVarName: string, reserved: any);
```

*   **conVarName**: The ConVar that changed.
*   **reserved**: Currently unused.

**Ejemplo (js):**

```js
// listen for all convar changes
AddConvarChangeListener(null, (conVarName, reserved) => {
    print(GetConvarInt(conVarName))
})

// listen to convars that start with "script:"
AddConvarChangeListener("script:*", (conVarName, reserved) => {
    print(GetConvarInt(conVarName))
})
```

---
### AddStateBagChangeHandler

`ADD_STATE_BAG_CHANGE_HANDLER` · hash `0x5BA35AAF` · **Cliente y servidor**

```lua
local retval = AddStateBagChangeHandler(keyFilter, bagFilter, handler)
```
```c
int ADD_STATE_BAG_CHANGE_HANDLER(char* keyFilter, char* bagFilter, func handler);
```

**Parámetros**

- `keyFilter` (`char*`): The key to check for, or null for no filter.
- `bagFilter` (`char*`): The bag ID to check for such as `entity:65535`, or null for no filter.
- `handler` (`func`): The handler function.

**Devuelve:** `int` — A cookie to remove the change handler.

**Descripción oficial:**

Adds a handler for changes to a state bag.

The function called expects to match the following signature:

```ts
function StateBagChangeHandler(bagName: string, key: string, value: any, reserved: number, replicated: boolean);
```

*   **bagName**: The internal bag ID for the state bag which changed. This is usually `player:Source`, `entity:NetID`
    or `localEntity:Handle`.
*   **key**: The changed key.
*   **value**: The new value stored at key. The old value is still stored in the state bag at the time this callback executes.
*   **reserved**: Currently unused.
*   **replicated**: Whether the set is meant to be replicated.

At this time, the change handler can't opt to reject changes.

If bagName refers to an entity, use [GET_ENTITY_FROM_STATE_BAG_NAME](#getentityfromstatebagname) to get the entity handle
If bagName refers to a player, use [GET_PLAYER_FROM_STATE_BAG_NAME](#getplayerfromstatebagname) to get the player handle

**Ejemplo (js):**

```js
AddStateBagChangeHandler("blockTasks", null, async (bagName, key, value /* boolean */) => {
    let entity = GetEntityFromStateBagName(bagName);
    // Whoops, we don't have a valid entity!
    if (entity === 0) return;
    // We don't want to freeze the entity position if the entity collision hasn't loaded yet
    while (!HasCollisionLoadedAroundEntity(entity)) {
        // The entity went out of our scope before the collision loaded
        if (!DoesEntityExist(entity)) return;
        await Delay(250);
    }
    SetEntityInvincible(entity, value)
    FreezeEntityPosition(entity, value)
    TaskSetBlockingOfNonTemporaryEvents(entity, value)
})
```

**Ejemplo (lua):**

```lua
AddStateBagChangeHandler("blockTasks", nil, function(bagName, key, value) 
    local entity = GetEntityFromStateBagName(bagName)
    -- Whoops, we don't have a valid entity!
    if entity == 0 then return end
    -- We don't want to freeze the entity position if the entity collision hasn't loaded yet
    while not HasCollisionLoadedAroundEntity(entity) do
        -- The entity went out of our scope before the collision loaded
        if not DoesEntityExist(entity) then return end
        Wait(250)
    end
    SetEntityInvincible(entity, value)
    FreezeEntityPosition(entity, value)
    TaskSetBlockingOfNonTemporaryEvents(entity, value)
end)
```

**Ejemplo (cs):**

```cs
AddStateBagChangeHandler("blockTasks", null,
    new Action<string, string, object, int, bool>
    (async (bagName, key, value, res, rep) =>
    {
        bool val = (bool)value;

        var entity = GetEntityFromStateBagName(bagName);
        //-- Whoops, we don't have a valid entity!
        if (entity == 0) return;
        //-- We don't want to freeze the entity position if the entity collision hasn't loaded yet
        while (!HasCollisionLoadedAroundEntity(entity))
        {
            //--The entity went out of our scope before the collision loaded
            if (!DoesEntityExist(entity)) return;

            await Delay(250);
        }
        SetEntityInvincible(entity, val);
        FreezeEntityPosition(entity, val);
        TaskSetBlockingOfNonTemporaryEvents(entity, val);
    }));
```

---
### CancelEvent

`CANCEL_EVENT` · hash `0xFA29D35D` · **Cliente y servidor**

```lua
CancelEvent()
```
```c
void CANCEL_EVENT();
```

**Devuelve:** `void`

**Descripción oficial:**

Cancels the currently executing event.

---
### CreateColshapeCircle

`CREATE_COLSHAPE_CIRCLE` · hash `0xB9C5AC6D` · **Cliente y servidor**

```lua
local retval = CreateColshapeCircle(x, y, radius)
```
```c
int CREATE_COLSHAPE_CIRCLE(float x, float y, float radius);
```

**Parámetros**

- `x` (`float`): Center X coordinate.
- `y` (`float`): Center Y coordinate.
- `radius` (`float`): Radius of the circle.

**Devuelve:** `int` — The collision shape ID, or `-1` on failure.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Creates a circle collision shape at the specified 2D position with the given radius.

When an entity enters or leaves a collision shape, the `onColshapeEnter` and `onColshapeExit` events are triggered. Both events are called with the entity handle that triggered them and the collision shape ID.

**Ejemplo (lua):**

```lua
-- Create a circle colshape and listen for enter/exit events
local colShape = CreateColshapeCircle(293.089, 180.466, 10.0)
print('created colshape with id ' .. tostring(colShape))

AddEventHandler('onColshapeEnter', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' entered colshape ' .. tostring(shape))
end)

AddEventHandler('onColshapeExit', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' left colshape ' .. tostring(shape))
end)
```

**Ejemplo (js):**

```js
const colShape = CreateColshapeCircle(293.089, 180.466, 10.0);
console.log(`created colshape with id ${colShape}`);

on('onColshapeEnter', (entity, shape) => {
    console.log(`entity ${entity} entered colshape ${shape}`);
});

on('onColshapeExit', (entity, shape) => {
    console.log(`entity ${entity} left colshape ${shape}`);
});
```

**Ejemplo (cs):**

```cs
int colShape = CreateColshapeCircle(293.089f, 180.466f, 10.0f);
Debug.WriteLine($"created colshape with id {colShape}");

EventHandlers["onColshapeEnter"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} entered colshape {shape}");
});

EventHandlers["onColshapeExit"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} left colshape {shape}");
});
```

---
### CreateColshapeCuboid

`CREATE_COLSHAPE_CUBOID` · hash `0x79AE8777` · **Cliente y servidor**

```lua
local retval = CreateColshapeCuboid(x, y, z, width, depth, height)
```
```c
int CREATE_COLSHAPE_CUBOID(float x, float y, float z, float width, float depth, float height);
```

**Parámetros**

- `x` (`float`): Center X coordinate.
- `y` (`float`): Center Y coordinate.
- `z` (`float`): Center Z coordinate.
- `width` (`float`): Total width (X extent).
- `depth` (`float`): Total depth (Y extent).
- `height` (`float`): Total height (Z extent).

**Devuelve:** `int` — The collision shape ID, or `-1` on failure.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Creates a cuboid (axis-aligned box) collision shape at the specified 3D position.

When an entity enters or leaves a collision shape, the `onColshapeEnter` and `onColshapeExit` events are triggered. Both events are called with the entity handle that triggered them and the collision shape ID.

**Ejemplo (lua):**

```lua
-- Create a cuboid colshape and listen for enter/exit events
local colShape = CreateColshapeCuboid(293.089, 180.466, 30.0, 10.0, 10.0, 5.0)
print('created colshape with id ' .. tostring(colShape))

AddEventHandler('onColshapeEnter', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' entered colshape ' .. tostring(shape))
end)

AddEventHandler('onColshapeExit', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' left colshape ' .. tostring(shape))
end)
```

**Ejemplo (js):**

```js
const colShape = CreateColshapeCuboid(293.089, 180.466, 30.0, 10.0, 10.0, 5.0);
console.log(`created colshape with id ${colShape}`);

on('onColshapeEnter', (entity, shape) => {
    console.log(`entity ${entity} entered colshape ${shape}`);
});

on('onColshapeExit', (entity, shape) => {
    console.log(`entity ${entity} left colshape ${shape}`);
});
```

**Ejemplo (cs):**

```cs
int colShape = CreateColshapeCuboid(293.089f, 180.466f, 30.0f, 10.0f, 10.0f, 5.0f);
Debug.WriteLine($"created colshape with id {colShape}");

EventHandlers["onColshapeEnter"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} entered colshape {shape}");
});

EventHandlers["onColshapeExit"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} left colshape {shape}");
});
```

---
### CreateColshapeCylinder

`CREATE_COLSHAPE_CYLINDER` · hash `0x59AD59AC` · **Cliente y servidor**

```lua
local retval = CreateColshapeCylinder(x, y, z, radius, height)
```
```c
int CREATE_COLSHAPE_CYLINDER(float x, float y, float z, float radius, float height);
```

**Parámetros**

- `x` (`float`): Center X coordinate.
- `y` (`float`): Center Y coordinate.
- `z` (`float`): Center Z coordinate.
- `radius` (`float`): Radius of the cylinder.
- `height` (`float`): Total height of the cylinder.

**Devuelve:** `int` — The collision shape ID, or `-1` on failure.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Creates a cylinder collision shape at the specified 3D position.

When an entity enters or leaves a collision shape, the `onColshapeEnter` and `onColshapeExit` events are triggered. Both events are called with the entity handle that triggered them and the collision shape ID.

**Ejemplo (lua):**

```lua
-- Create a cylinder colshape and listen for enter/exit events
local colShape = CreateColshapeCylinder(293.089, 180.466, 30.0, 10.0, 5.0)
print('created colshape with id ' .. tostring(colShape))

AddEventHandler('onColshapeEnter', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' entered colshape ' .. tostring(shape))
end)

AddEventHandler('onColshapeExit', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' left colshape ' .. tostring(shape))
end)
```

**Ejemplo (js):**

```js
const colShape = CreateColshapeCylinder(293.089, 180.466, 30.0, 10.0, 5.0);
console.log(`created colshape with id ${colShape}`);

on('onColshapeEnter', (entity, shape) => {
    console.log(`entity ${entity} entered colshape ${shape}`);
});

on('onColshapeExit', (entity, shape) => {
    console.log(`entity ${entity} left colshape ${shape}`);
});
```

**Ejemplo (cs):**

```cs
int colShape = CreateColshapeCylinder(293.089f, 180.466f, 30.0f, 10.0f, 5.0f);
Debug.WriteLine($"created colshape with id {colShape}");

EventHandlers["onColshapeEnter"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} entered colshape {shape}");
});

EventHandlers["onColshapeExit"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} left colshape {shape}");
});
```

---
### CreateColshapePolygon

`CREATE_COLSHAPE_POLYGON` · hash `0x1B055F04` · **Cliente y servidor**

```lua
local retval = CreateColshapePolygon(minZ, maxZ, points)
```
```c
int CREATE_COLSHAPE_POLYGON(float minZ, float maxZ, object points);
```

**Parámetros**

- `minZ` (`float`): Minimum Z height of the polygon.
- `maxZ` (`float`): Maximum Z height of the polygon.
- `points` (`object`): An array of interleaved x, y point pairs (e.g., `{x1, y1, x2, y2, x3, y3, ...}`). Must contain at least 3 pairs.

**Devuelve:** `int` — The collision shape ID, or `-1` on failure.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Creates a polygon collision shape defined by a set of 2D points extruded between `minZ` and `maxZ`. Requires at least 3 points.

When an entity enters or leaves a collision shape, the `onColshapeEnter` and `onColshapeExit` events are triggered. Both events are called with the entity handle that triggered them and the collision shape ID.

**Ejemplo (lua):**

```lua
-- Create a polygon colshape and listen for enter/exit events
local colShape = CreateColshapePolygon(28.0, 32.0, { 293.089, 180.466, 303.089, 180.466, 298.089, 190.466 })
print('created colshape with id ' .. tostring(colShape))

AddEventHandler('onColshapeEnter', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' entered colshape ' .. tostring(shape))
end)

AddEventHandler('onColshapeExit', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' left colshape ' .. tostring(shape))
end)
```

**Ejemplo (js):**

```js
const colShape = CreateColshapePolygon(28.0, 32.0, [293.089, 180.466, 303.089, 180.466, 298.089, 190.466]);
console.log(`created colshape with id ${colShape}`);

on('onColshapeEnter', (entity, shape) => {
    console.log(`entity ${entity} entered colshape ${shape}`);
});

on('onColshapeExit', (entity, shape) => {
    console.log(`entity ${entity} left colshape ${shape}`);
});
```

**Ejemplo (cs):**

```cs
int colShape = CreateColshapePolygon(28.0f, 32.0f, new float[] { 293.089f, 180.466f, 303.089f, 180.466f, 298.089f, 190.466f });
Debug.WriteLine($"created colshape with id {colShape}");

EventHandlers["onColshapeEnter"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} entered colshape {shape}");
});

EventHandlers["onColshapeExit"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} left colshape {shape}");
});
```

---
### CreateColshapeRectangle

`CREATE_COLSHAPE_RECTANGLE` · hash `0x58C3F669` · **Cliente y servidor**

```lua
local retval = CreateColshapeRectangle(x, y, z, width, depth, heading)
```
```c
int CREATE_COLSHAPE_RECTANGLE(float x, float y, float z, float width, float depth, float heading);
```

**Parámetros**

- `x` (`float`): Center X coordinate.
- `y` (`float`): Center Y coordinate.
- `z` (`float`): Center Z coordinate.
- `width` (`float`): Total width.
- `depth` (`float`): Total depth.
- `heading` (`float`): Rotation heading in radians.

**Devuelve:** `int` — The collision shape ID, or `-1` on failure.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Creates a rotated rectangle collision shape at the specified 3D position.

When an entity enters or leaves a collision shape, the `onColshapeEnter` and `onColshapeExit` events are triggered. Both events are called with the entity handle that triggered them and the collision shape ID.

**Ejemplo (lua):**

```lua
-- Create a rectangle colshape and listen for enter/exit events
local colShape = CreateColshapeRectangle(293.089, 180.466, 30.0, 10.0, 10.0, 0.0)
print('created colshape with id ' .. tostring(colShape))

AddEventHandler('onColshapeEnter', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' entered colshape ' .. tostring(shape))
end)

AddEventHandler('onColshapeExit', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' left colshape ' .. tostring(shape))
end)
```

**Ejemplo (js):**

```js
const colShape = CreateColshapeRectangle(293.089, 180.466, 30.0, 10.0, 10.0, 0.0);
console.log(`created colshape with id ${colShape}`);

on('onColshapeEnter', (entity, shape) => {
    console.log(`entity ${entity} entered colshape ${shape}`);
});

on('onColshapeExit', (entity, shape) => {
    console.log(`entity ${entity} left colshape ${shape}`);
});
```

**Ejemplo (cs):**

```cs
int colShape = CreateColshapeRectangle(293.089f, 180.466f, 30.0f, 10.0f, 10.0f, 0.0f);
Debug.WriteLine($"created colshape with id {colShape}");

EventHandlers["onColshapeEnter"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} entered colshape {shape}");
});

EventHandlers["onColshapeExit"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} left colshape {shape}");
});
```

---
### CreateColshapeSphere

`CREATE_COLSHAPE_SPHERE` · hash `0xB6710ACB` · **Cliente y servidor**

```lua
local retval = CreateColshapeSphere(x, y, z, radius)
```
```c
int CREATE_COLSHAPE_SPHERE(float x, float y, float z, float radius);
```

**Parámetros**

- `x` (`float`): Center X coordinate.
- `y` (`float`): Center Y coordinate.
- `z` (`float`): Center Z coordinate.
- `radius` (`float`): Radius of the sphere.

**Devuelve:** `int` — The collision shape ID, or `-1` on failure.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Creates a sphere collision shape at the specified 3D position with the given radius.

When an entity enters or leaves a collision shape, the `onColshapeEnter` and `onColshapeExit` events are triggered. Both events are called with the entity handle that triggered them and the collision shape ID.

**Ejemplo (lua):**

```lua
-- Create a sphere colshape and listen for enter/exit events
local colShape = CreateColshapeSphere(293.089, 180.466, 30.0, 10.0)
print('created colshape with id ' .. tostring(colShape))

AddEventHandler('onColshapeEnter', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' entered colshape ' .. tostring(shape))
end)

AddEventHandler('onColshapeExit', function(entity, shape)
    print('entity ' .. tostring(entity) .. ' left colshape ' .. tostring(shape))
end)
```

**Ejemplo (js):**

```js
const colShape = CreateColshapeSphere(293.089, 180.466, 30.0, 10.0);
console.log(`created colshape with id ${colShape}`);

on('onColshapeEnter', (entity, shape) => {
    console.log(`entity ${entity} entered colshape ${shape}`);
});

on('onColshapeExit', (entity, shape) => {
    console.log(`entity ${entity} left colshape ${shape}`);
});
```

**Ejemplo (cs):**

```cs
int colShape = CreateColshapeSphere(293.089f, 180.466f, 30.0f, 10.0f);
Debug.WriteLine($"created colshape with id {colShape}");

EventHandlers["onColshapeEnter"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} entered colshape {shape}");
});

EventHandlers["onColshapeExit"] += new Action<int, int>((entity, shape) =>
{
    Debug.WriteLine($"entity {entity} left colshape {shape}");
});
```

---
### DeleteColshape

`DELETE_COLSHAPE` · hash `0x16B9F12B` · **Cliente y servidor**

```lua
DeleteColshape(colShapeId)
```
```c
void DELETE_COLSHAPE(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID to delete.

**Devuelve:** `void`

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Deletes an existing collision shape by its ID.

---
### DeleteFunctionReference

`DELETE_FUNCTION_REFERENCE` · hash `0x1E86F206` · **Cliente y servidor**

```lua
DeleteFunctionReference(referenceIdentity)
```
```c
void DELETE_FUNCTION_REFERENCE(char* referenceIdentity);
```

**Parámetros**

- `referenceIdentity` (`char*`)

**Devuelve:** `void`

---
### DeleteResourceKvp

`DELETE_RESOURCE_KVP` · hash `0x7389B5DF` · **Cliente y servidor**

```lua
DeleteResourceKvp(key)
```
```c
void DELETE_RESOURCE_KVP(char* key);
```

**Parámetros**

- `key` (`char*`): The key to delete

**Devuelve:** `void`

**Ejemplo (lua):**

```lua
DeleteResourceKvp('liberty_city')
```

---
### DeleteResourceKvpNoSync

`DELETE_RESOURCE_KVP_NO_SYNC` · hash `0x4152C90` · **Cliente y servidor**

```lua
DeleteResourceKvpNoSync(key)
```
```c
void DELETE_RESOURCE_KVP_NO_SYNC(char* key);
```

**Parámetros**

- `key` (`char*`): The key to delete

**Devuelve:** `void`

**Descripción oficial:**

Nonsynchronous [DELETE_RESOURCE_KVP](#deleteresourcekvp) operation; see [FLUSH_RESOURCE_KVP](#getresourcekvpstring).

---
### DoesColshapeExist

`DOES_COLSHAPE_EXIST` · hash `0x9A2EC46D` · **Cliente y servidor**

```lua
local retval = DoesColshapeExist(colShapeId)
```
```c
BOOL DOES_COLSHAPE_EXIST(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID to check.

**Devuelve:** `BOOL` — `true` if the collision shape exists, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether a collision shape with the given ID exists.

---
### DoesTrainStopAtStations

`DOES_TRAIN_STOP_AT_STATIONS` · hash `0x77CC80DC` · **Cliente y servidor**

```lua
local retval = DoesTrainStopAtStations(train)
```
```c
BOOL DOES_TRAIN_STOP_AT_STATIONS(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `BOOL` — True if the train stops at stations. False otherwise

---
### DuplicateFunctionReference

`DUPLICATE_FUNCTION_REFERENCE` · hash `0xF4E2079D` · **Cliente y servidor**

```lua
local retval = DuplicateFunctionReference(referenceIdentity)
```
```c
char* DUPLICATE_FUNCTION_REFERENCE(char* referenceIdentity);
```

**Parámetros**

- `referenceIdentity` (`char*`)

**Devuelve:** `char*`

---
### EndFindKvp

`END_FIND_KVP` · hash `0xB3210203` · **Cliente y servidor**

```lua
EndFindKvp(handle)
```
```c
void END_FIND_KVP(int handle);
```

**Parámetros**

- `handle` (`int`): The KVP find handle returned from [START_FIND_KVP](#startfindkvp)

**Devuelve:** `void` — None.

---
### EnsureEntityStateBag

`ENSURE_ENTITY_STATE_BAG` · hash `0x3BB78F05` · **Cliente y servidor**

```lua
EnsureEntityStateBag(entity)
```
```c
void ENSURE_ENTITY_STATE_BAG(Entity entity);
```

**Parámetros**

- `entity` (`Entity`)

**Devuelve:** `void`

**Descripción oficial:**

Internal function for ensuring an entity has a state bag.

---
### ExecuteCommand

`EXECUTE_COMMAND` · hash `0x561C060B` · **Cliente y servidor**

```lua
ExecuteCommand(commandString)
```
```c
void EXECUTE_COMMAND(char* commandString);
```

**Parámetros**

- `commandString` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

Depending on your use case you may need to use `add_acl resource.<your_resource_name> command.<command_name> allow` to use this native in your resource.

**Ejemplo (lua):**

```lua
Citizen.CreateThread(function()
  -- stop the server after 1 minute
  Citizen.Wait(60000)
  ExecuteCommand("quit Shortlived")
end)
```

---
### FindKvp

`FIND_KVP` · hash `0xBD7BEBC5` · **Cliente y servidor**

```lua
local retval = FindKvp(handle)
```
```c
char* FIND_KVP(int handle);
```

**Parámetros**

- `handle` (`int`): The KVP find handle returned from [START_FIND_KVP](#startfindkvp)

**Devuelve:** `char*` — None.

---
### FormatStackTrace

`FORMAT_STACK_TRACE` · hash `0xD70C3BCA` · **Cliente y servidor**

```lua
local retval = FormatStackTrace(traceData)
```
```c
char* FORMAT_STACK_TRACE(object traceData);
```

**Parámetros**

- `traceData` (`object`)

**Devuelve:** `char*`

**Descripción oficial:**

An internal function for converting a stack trace object to a string.

---
### GetColshapeCircleData

`GET_COLSHAPE_CIRCLE_DATA` · hash `0x1DC0D547` · **Cliente y servidor**

```lua
local retval, x, y, radius = GetColshapeCircleData(colShapeId)
```
```c
BOOL GET_COLSHAPE_CIRCLE_DATA(int colShapeId, float* x, float* y, float* radius);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `x` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center X coordinate.
- `y` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Y coordinate.
- `radius` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Radius of the circle.

**Devuelve:** `BOOL` — `true` if the data was retrieved successfully. Returns `false` if the ID is invalid or the shape is not a circle.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Gets the circle collision shape data.

---
### GetColshapeCuboidData

`GET_COLSHAPE_CUBOID_DATA` · hash `0x9D0BC07C` · **Cliente y servidor**

```lua
local retval, x, y, z, width, depth, height = GetColshapeCuboidData(colShapeId)
```
```c
BOOL GET_COLSHAPE_CUBOID_DATA(int colShapeId, float* x, float* y, float* z, float* width, float* depth, float* height);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `x` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center X coordinate.
- `y` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Y coordinate.
- `z` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Z coordinate.
- `width` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Total width.
- `depth` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Total depth.
- `height` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Total height.

**Devuelve:** `BOOL` — `true` if the data was retrieved successfully. Returns `false` if the ID is invalid or the shape is not a cuboid.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Gets the cuboid collision shape data.

---
### GetColshapeCylinderData

`GET_COLSHAPE_CYLINDER_DATA` · hash `0x83B79CDA` · **Cliente y servidor**

```lua
local retval, x, y, z, radius, height = GetColshapeCylinderData(colShapeId)
```
```c
BOOL GET_COLSHAPE_CYLINDER_DATA(int colShapeId, float* x, float* y, float* z, float* radius, float* height);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `x` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center X coordinate.
- `y` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Y coordinate.
- `z` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Z coordinate.
- `radius` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Radius of the cylinder.
- `height` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Total height of the cylinder.

**Devuelve:** `BOOL` — `true` if the data was retrieved successfully. Returns `false` if the ID is invalid or the shape is not a cylinder.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Gets the cylinder collision shape data.

---
### GetColshapePolygonData

`GET_COLSHAPE_POLYGON_DATA` · hash `0xCD8BFE8D` · **Cliente y servidor**

```lua
local retval, minZ, maxZ = GetColshapePolygonData(colShapeId)
```
```c
object GET_COLSHAPE_POLYGON_DATA(int colShapeId, float* minZ, float* maxZ);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `minZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Minimum Z height.
- `maxZ` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Maximum Z height.

**Devuelve:** `object` — An array of interleaved x, y point pairs.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Gets the polygon collision shape data. Returns an empty array if the ID is invalid or the shape is not a polygon.

---
### GetColshapeRectangleData

`GET_COLSHAPE_RECTANGLE_DATA` · hash `0xED8B05DF` · **Cliente y servidor**

```lua
local retval, x, y, z, width, depth, heading = GetColshapeRectangleData(colShapeId)
```
```c
BOOL GET_COLSHAPE_RECTANGLE_DATA(int colShapeId, float* x, float* y, float* z, float* width, float* depth, float* heading);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `x` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center X coordinate.
- `y` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Y coordinate.
- `z` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Z coordinate.
- `width` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Total width.
- `depth` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Total depth.
- `heading` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Rotation heading in radians.

**Devuelve:** `BOOL` — `true` if the data was retrieved successfully. Returns `false` if the ID is invalid or the shape is not a rectangle.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Gets the rectangle collision shape data.

---
### GetColshapeSphereData

`GET_COLSHAPE_SPHERE_DATA` · hash `0xFF94C6DB` · **Cliente y servidor**

```lua
local retval, x, y, z, radius = GetColshapeSphereData(colShapeId)
```
```c
BOOL GET_COLSHAPE_SPHERE_DATA(int colShapeId, float* x, float* y, float* z, float* radius);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `x` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center X coordinate.
- `y` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Y coordinate.
- `z` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Center Z coordinate.
- `radius` (`float*`) *(puntero: se devuelve como valor de retorno, no se pasa)*: Radius of the sphere.

**Devuelve:** `BOOL` — `true` if the data was retrieved successfully. Returns `false` if the ID is invalid or the shape is not a sphere.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Gets the sphere collision shape data.

---
### GetConvar

`GET_CONVAR` · hash `0x6CCD2564` · **Cliente y servidor**

```lua
local retval = GetConvar(varName, default_)
```
```c
char* GET_CONVAR(char* varName, char* default_);
```

**Parámetros**

- `varName` (`char*`): The console variable to look up.
- `default_` (`char*`): The default value to set if none is found.

**Devuelve:** `char*` — Returns the convar value if it can be found, otherwise it returns the assigned `default`.

**Descripción oficial:**

Can be used to get a console variable of type `char*`, for example a string.

**Ejemplo (lua):**

```lua
if GetConvar('voice_useNativeAudio', 'false') == 'true' then
    Citizen.Trace('Native Audio is enabled.')
end
```

---
### GetConvarBool

`GET_CONVAR_BOOL` · hash `0x7E8EBFE5` · **Cliente y servidor**

```lua
local retval = GetConvarBool(varName, defaultValue)
```
```c
BOOL GET_CONVAR_BOOL(char* varName, BOOL defaultValue);
```

**Parámetros**

- `varName` (`char*`): The console variable to look up.
- `defaultValue` (`BOOL`): The default value to set if none is found.

**Devuelve:** `BOOL` — Returns the convar value if it can be found, otherwise it returns the assigned `default`.

**Descripción oficial:**

Can be used to get a console variable casted back to `bool`.

**Ejemplo (lua):**

```lua
if GetConvarBool('dev_mode', false) then
    print("Dev Mode is eanbled, load dev mode menus")
end
```

---
### GetConvarFloat

`GET_CONVAR_FLOAT` · hash `0x9E666D` · **Cliente y servidor**

```lua
local retval = GetConvarFloat(varName, defaultValue)
```
```c
float GET_CONVAR_FLOAT(char* varName, float defaultValue);
```

**Parámetros**

- `varName` (`char*`): The console variable to get
- `defaultValue` (`float`): The default value to set, if none are found.

**Devuelve:** `float` — Returns the value set in varName, or `default` if none are specified

**Descripción oficial:**

This will have floating point inaccuracy.

---
### GetConvarInt

`GET_CONVAR_INT` · hash `0x935C0AB2` · **Cliente y servidor**

```lua
local retval = GetConvarInt(varName, default_)
```
```c
int GET_CONVAR_INT(char* varName, int default_);
```

**Parámetros**

- `varName` (`char*`): The console variable to look up.
- `default_` (`int`): The default value to set if none is found (variable not set using [SET_CONVAR](servidor.md#setconvar), or not accessible).

**Devuelve:** `int` — Returns the convar value if it can be found, otherwise it returns the assigned `default`.

**Descripción oficial:**

Can be used to get a console variable casted back to `int` (an integer value).

**Ejemplo (lua):**

```lua
if GetConvarInt('remainingRounds', 0) < 900 then
    Citizen.Trace("Less than 900 rounds remaining...")
end
```

---
### GetCurrentResourceName

`GET_CURRENT_RESOURCE_NAME` · hash `0xE5E9EBBB` · **Cliente y servidor**

```lua
local retval = GetCurrentResourceName()
```
```c
char* GET_CURRENT_RESOURCE_NAME();
```

**Devuelve:** `char*` — The name of the resource.

**Descripción oficial:**

Returns the name of the currently executing resource.

---
### GetEntitiesInRadius

`GET_ENTITIES_IN_RADIUS` · hash `0xDFFBA12F` · **Cliente y servidor**

```lua
local retval = GetEntitiesInRadius(x, y, z, radius, entityType, sortByDistance, models)
```
```c
object GET_ENTITIES_IN_RADIUS(float x, float y, float z, float radius, int entityType, BOOL sortByDistance, object models);
```

**Parámetros**

- `x` (`float`): The X coordinate.
- `y` (`float`): The Y coordinate.
- `z` (`float`): The Z coordinate.
- `radius` (`float`): Max distance from coordinate to entity
- `entityType` (`int`): Entity types see list below
- `sortByDistance` (`BOOL`): Sort output entites by distance from nearest to farthest
- `models` (`object`): List of allowed models its also optional

**Devuelve:** `object` — An array containing entity handles for each entity.

**Descripción oficial:**

**Supported types**

*   \[1] : Peds (including animals) and players.
*   \[2] : Vehicles.
*   \[3] : Objects (props), doors, and projectiles.

**Coordinates need to be send unpacked (x,y,z)**

```lua

-- Define the allowed model hashes
local allowedModelHashes = { GetHashKey("p_crate03x"), GetHashKey("p_crate22x") }

-- Get the player's current coordinates
local playerCoords = GetEntityCoords(PlayerPedId())

-- Retrieve all entities of type Object (type 3) within a radius of 10.0 units
-- that match the allowed model hashes
-- and sort output entities by distance
local entities = GetEntitiesInRadius(playerCoords.x, playerCoords.y, playerCoords.z, 10.0, 3, true, allowedModelHashes)

-- Iterate through the list of entities and print their ids
for i = 1, #entities do
    local entity = entities[i]
    print(entity)
end

```

---
### GetEntityFromStateBagName

`GET_ENTITY_FROM_STATE_BAG_NAME` · hash `0x4BDF1867` · **Cliente y servidor**

```lua
local retval = GetEntityFromStateBagName(bagName)
```
```c
Entity GET_ENTITY_FROM_STATE_BAG_NAME(char* bagName);
```

**Parámetros**

- `bagName` (`char*`): An internal state bag ID from the argument to a state bag change handler.

**Devuelve:** `Entity` — The entity handle or 0 if the state bag name did not refer to an entity, or the entity does not exist.

**Descripción oficial:**

Returns the entity handle for the specified state bag name. For use with [ADD_STATE_BAG_CHANGE_HANDLER](#addstatebagchangehandler).

**Ejemplo (js):**

```js
AddStateBagChangeHandler("blockTasks", null, async (bagName, key, value /* boolean */) => {
    let entity = GetEntityFromStateBagName(bagName);
    // Whoops, we were don't have a valid entity!
    if (entity === 0) return;
    // We don't want to freeze the entity position if the entity collision hasn't loaded yet
    while (!HasCollisionLoadedAroundEntity(entity)) {
        // The entity went out of our scope before the collision loaded
        if (!DoesEntityExist(entity)) return;
        await Delay(250);
    }
    SetEntityInvincible(entity, value)
    FreezeEntityPosition(entity, value)
    TaskSetBlockingOfNonTemporaryEvents(entity, value)
})
```

**Ejemplo (lua):**

```lua
AddStateBagChangeHandler("blockTasks", nil, function(bagName, key, value) 
    local entity = GetEntityFromStateBagName(bagName)
    -- Whoops, we don't have a valid entity!
    if entity == 0 then return end
    -- We don't want to freeze the entity position if the entity collision hasn't loaded yet
    while not HasCollisionLoadedAroundEntity(entity) do
        -- The entity went out of our scope before the collision loaded
        if not DoesEntityExist(entity) then return end
        Wait(250)
    end
    SetEntityInvincible(entity, value)
    FreezeEntityPosition(entity, value)
    TaskSetBlockingOfNonTemporaryEvents(entity, value)
end)
```

---
### GetGameBuildNumber

`GET_GAME_BUILD_NUMBER` · hash `0x804B9F7B` · **Cliente y servidor**

```lua
local retval = GetGameBuildNumber()
```
```c
int GET_GAME_BUILD_NUMBER();
```

**Devuelve:** `int` — The build number, or **0** if no build number is known.

**Descripción oficial:**

Returns the internal build number of the current game being executed.

Possible values:

*   FiveM
    *   1604
    *   2060
    *   2189
    *   2372
    *   2545
    *   2612
    *   2699
    *   2802
    *   2944
    *   3095
    *   3258
    *   3323
    *   3407
    *   3570
    *   3751
    *   3788
    *   3889
*   RedM
    *   1311
    *   1355
    *   1436
    *   1491
*   LibertyM
    *   43
*   FXServer
    *   0

---
### GetGameName

`GET_GAME_NAME` · hash `0xE8EAA18B` · **Cliente y servidor**

```lua
local retval = GetGameName()
```
```c
char* GET_GAME_NAME();
```

**Devuelve:** `char*` — The game the script environment is running in.

**Descripción oficial:**

Returns the current game being executed.

Possible values:

| Return value | Meaning                        |
| ------------ | ------------------------------ |
| `fxserver`   | Server-side code ('Duplicity') |
| `fivem`      | FiveM for GTA V                |
| `libertym`   | LibertyM for GTA IV            |
| `redm`       | RedM for Red Dead Redemption 2 |

---
### GetGamePool

`GET_GAME_POOL` · hash `0x2B9D4F50` · **Cliente y servidor**

```lua
local retval = GetGamePool(poolName)
```
```c
object GET_GAME_POOL(char* poolName);
```

**Parámetros**

- `poolName` (`char*`): The pool name to get a list of entities from.

**Devuelve:** `object` — An array containing entity handles for each entity in the named pool.

**Descripción oficial:**

Returns a list of entity handles (script GUID) for all entities in the specified pool - the data returned is an array as
follows:

```json
[ 770, 1026, 1282, 1538, 1794, 2050, 2306, 2562, 2818, 3074, 3330, 3586, 3842, 4098, 4354, 4610, ...]
```

**Supported pools**

*   `CPed`: Peds (including animals) and players.
*   `CObject`: Objects (props), doors, and projectiles.
*   `CNetObject`: Networked objects
*   `CVehicle`: Vehicles.
*   `CPickup`: Pickups.

**Ejemplo (lua):**

```lua
local vehiclePool = GetGamePool('CVehicle') -- Get the list of vehicles (entities) from the pool
for i = 1, #vehiclePool do -- loop through each vehicle (entity)
    if GetPedInVehicleSeat(vehiclePool[i], -1) == 0 then
        DeleteEntity(vehiclePool[i]) -- Delete vehicles (entities) that don't have a driver
    end
end
```

---
### GetInstanceId

`GET_INSTANCE_ID` · hash `0x9F1C4383` · **Cliente y servidor**

```lua
local retval = GetInstanceId()
```
```c
int GET_INSTANCE_ID();
```

**Devuelve:** `int`

---
### GetInvokingResource

`GET_INVOKING_RESOURCE` · hash `0x4D52FE5B` · **Cliente y servidor**

```lua
local retval = GetInvokingResource()
```
```c
char* GET_INVOKING_RESOURCE();
```

**Devuelve:** `char*`

---
### GetNumResourceMetadata

`GET_NUM_RESOURCE_METADATA` · hash `0x776E864` · **Cliente y servidor**

```lua
local retval = GetNumResourceMetadata(resourceName, metadataKey)
```
```c
int GET_NUM_RESOURCE_METADATA(char* resourceName, char* metadataKey);
```

**Parámetros**

- `resourceName` (`char*`): The resource name.
- `metadataKey` (`char*`): The key to look up in the resource manifest.

**Devuelve:** `int`

**Descripción oficial:**

Gets the amount of metadata values with the specified key existing in the specified resource's manifest.
See also: [Resource manifest](https://docs.fivem.net/docs/scripting-reference/resource-manifest/)

---
### GetNumResources

`GET_NUM_RESOURCES` · hash `0x863F27B` · **Cliente y servidor**

```lua
local retval = GetNumResources()
```
```c
int GET_NUM_RESOURCES();
```

**Devuelve:** `int`

---
### GetPlayerFromStateBagName

`GET_PLAYER_FROM_STATE_BAG_NAME` · hash `0xA56135E0` · **Cliente y servidor**

```lua
local retval = GetPlayerFromStateBagName(bagName)
```
```c
int GET_PLAYER_FROM_STATE_BAG_NAME(char* bagName);
```

**Parámetros**

- `bagName` (`char*`): An internal state bag ID from the argument to a state bag change handler.

**Devuelve:** `int` — The player handle or 0 if the state bag name did not refer to a player, or the player does not exist.

**Descripción oficial:**

On the server this will return the players source, on the client it will return the player handle.

**Ejemplo (js):**

```js
AddStateBagChangeHandler("isDead", null, async (bagName, key, value /* boolean */) => {
    const ply = GetPlayerFromStateBagName(bagName);
    // The player doesn't exist!
    if (ply === 0) return;
    console.log(`Player: ${GetPlayerName(ply)} ${value ? 'died!' : 'is alive!'`)
})
```

**Ejemplo (lua):**

```lua
AddStateBagChangeHandler("isDead", nil, function(bagName, key, value) 
    local ply = GetPlayerFromStateBagName(bagName)
    -- The player doesn't exist!
    if ply == 0 then return end
    print("Player: " .. GetPlayerName(ply) .. value and 'died!' or 'is alive!')
end)
```

---
### GetPlayerMeleeWeaponDamageModifier

`GET_PLAYER_MELEE_WEAPON_DAMAGE_MODIFIER` · hash `0x8689A825` · **Cliente y servidor**

```lua
local retval = GetPlayerMeleeWeaponDamageModifier(playerId)
```
```c
float GET_PLAYER_MELEE_WEAPON_DAMAGE_MODIFIER(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — Returns player melee weapon damage modifier value.

**Descripción oficial:**

A getter for [SET_PLAYER_MELEE_WEAPON_DAMAGE_MODIFIER](../gta5/PLAYER.md#setplayermeleeweapondamagemodifier).

---
### GetPlayerWeaponDamageModifier

`GET_PLAYER_WEAPON_DAMAGE_MODIFIER` · hash `0x2A3D7CDA` · **Cliente y servidor**

```lua
local retval = GetPlayerWeaponDamageModifier(playerId)
```
```c
float GET_PLAYER_WEAPON_DAMAGE_MODIFIER(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player weapon damage modifier.

**Descripción oficial:**

A getter for [SET_PLAYER_WEAPON_DAMAGE_MODIFIER](../gta5/PLAYER.md#setplayerweapondamagemodifier).

---
### GetPlayerWeaponDefenseModifier

`GET_PLAYER_WEAPON_DEFENSE_MODIFIER` · hash `0xF1543251` · **Cliente y servidor**

```lua
local retval = GetPlayerWeaponDefenseModifier(playerId)
```
```c
float GET_PLAYER_WEAPON_DEFENSE_MODIFIER(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player weapon defense modifier.

**Descripción oficial:**

A getter for [SET_PLAYER_WEAPON_DEFENSE_MODIFIER](../gta5/PLAYER.md#setplayerweapondefensemodifier).

---
### GetPlayerWeaponDefenseModifier_2

`GET_PLAYER_WEAPON_DEFENSE_MODIFIER_2` · hash `0x986B65FF` · **Cliente y servidor**

```lua
local retval = GetPlayerWeaponDefenseModifier_2(playerId)
```
```c
float GET_PLAYER_WEAPON_DEFENSE_MODIFIER_2(Player playerId);
```

**Parámetros**

- `playerId` (`Player`): The player index.

**Devuelve:** `float` — The value of player weapon defense modifier 2.

**Descripción oficial:**

A getter for [\_SET_PLAYER_WEAPON_DEFENSE_MODIFIER\_2](../gta5/PLAYER.md#setplayerweapondefensemodifier_2).

---
### GetRegisteredCommands

`GET_REGISTERED_COMMANDS` · hash `0xD4BEF069` · **Cliente y servidor**

```lua
local retval = GetRegisteredCommands()
```
```c
object GET_REGISTERED_COMMANDS();
```

**Devuelve:** `object` — An object containing registered commands.

**Descripción oficial:**

Returns all commands that are registered in the command system.
The data returned adheres to the following layout:

```
[
{
"name": "cmdlist",
"resource": "resource",
"arity" = -1,
},
{
"name": "command1"
"resource": "resource_2",
"arity" = -1,
}
]
```

---
### GetResourceByFindIndex

`GET_RESOURCE_BY_FIND_INDEX` · hash `0x387246B7` · **Cliente y servidor**

```lua
local retval = GetResourceByFindIndex(findIndex)
```
```c
char* GET_RESOURCE_BY_FIND_INDEX(int findIndex);
```

**Parámetros**

- `findIndex` (`int`): The index of the resource (starting at 0)

**Devuelve:** `char*` — The resource name as a `string`

**Ejemplo (lua):**

```lua
local resourceList = {}
for i = 0, GetNumResources(), 1 do
  local resource_name = GetResourceByFindIndex(i)
  if resource_name and GetResourceState(resource_name) == "started" then
    table.insert(resourceList, resource_name)
  end
end
print(table.unpack(resourceList))
```

---
### GetResourceCommands

`GET_RESOURCE_COMMANDS` · hash `0x97628584` · **Cliente y servidor**

```lua
local retval = GetResourceCommands(resource)
```
```c
object GET_RESOURCE_COMMANDS(char* resource);
```

**Parámetros**

- `resource` (`char*`)

**Devuelve:** `object` — An object containing registered commands.

**Descripción oficial:**

Returns all commands registered by the specified resource.
The data returned adheres to the following layout:

```
[
{
"name": "cmdlist",
"resource": "example_resource",
"arity" = -1,
},
{
"name": "command1"
"resource": "example_resource2",
"arity" = -1,
}
]
```

---
### GetResourceKvpFloat

`GET_RESOURCE_KVP_FLOAT` · hash `0x35BDCEEA` · **Cliente y servidor**

```lua
local retval = GetResourceKvpFloat(key)
```
```c
float GET_RESOURCE_KVP_FLOAT(char* key);
```

**Parámetros**

- `key` (`char*`): The key to fetch

**Devuelve:** `float` — The floating-point value stored under the specified key, or 0.0 if not found.

**Descripción oficial:**

A getter for [SET_RESOURCE_KVP_FLOAT](#setresourcekvpfloat).

**Ejemplo (lua):**

```lua
local kvpValue = GetResourceKvpFloat('mollis')
if kvpValue ~= 0.0 then
	-- do something!
end
```

---
### GetResourceKvpInt

`GET_RESOURCE_KVP_INT` · hash `0x557B586A` · **Cliente y servidor**

```lua
local retval = GetResourceKvpInt(key)
```
```c
int GET_RESOURCE_KVP_INT(char* key);
```

**Parámetros**

- `key` (`char*`): The key to fetch

**Devuelve:** `int` — The integer value stored under the specified key, or 0 if not found.

**Descripción oficial:**

A getter for [SET_RESOURCE_KVP_INT](#setresourcekvpint).

**Ejemplo (lua):**

```lua
local kvpValue = GetResourceKvpInt('bananabread') 
if kvpValue ~= 0 then
	-- do something!
end
```

---
### GetResourceKvpString

`GET_RESOURCE_KVP_STRING` · hash `0x5240DA5A` · **Cliente y servidor**

```lua
local retval = GetResourceKvpString(key)
```
```c
char* GET_RESOURCE_KVP_STRING(char* key);
```

**Parámetros**

- `key` (`char*`): The key to fetch

**Devuelve:** `char*` — The string value stored under the specified key, or nil/null if not found.

**Descripción oficial:**

A getter for [SET_RESOURCE_KVP](#setresourcekvp).

**Ejemplo (lua):**

```lua
local kvpValue = GetResourceKvpString('codfish') 
if kvpValue then
	-- do something!
end
```

---
### GetResourceMetadata

`GET_RESOURCE_METADATA` · hash `0x964BAB1D` · **Cliente y servidor**

```lua
local retval = GetResourceMetadata(resourceName, metadataKey, index)
```
```c
char* GET_RESOURCE_METADATA(char* resourceName, char* metadataKey, int index);
```

**Parámetros**

- `resourceName` (`char*`): The resource name.
- `metadataKey` (`char*`): The key in the resource manifest.
- `index` (`int`): The value index, in a range from \[0..GET_NUM_RESOURCE_METDATA-1].

**Devuelve:** `char*`

**Descripción oficial:**

Gets the metadata value at a specified key/index from a resource's manifest.
See also: [Resource manifest](https://docs.fivem.net/docs/scripting-reference/resource-manifest/)

---
### GetResourceState

`GET_RESOURCE_STATE` · hash `0x4039B485` · **Cliente y servidor**

```lua
local retval = GetResourceState(resourceName)
```
```c
char* GET_RESOURCE_STATE(char* resourceName);
```

**Parámetros**

- `resourceName` (`char*`): The name of the resource.

**Devuelve:** `char*` — The resource state. One of `"missing", "started", "starting", "stopped", "stopping", "uninitialized" or "unknown"`.

**Descripción oficial:**

Returns the current state of the specified resource.

---
### GetStateBagKeys

`GET_STATE_BAG_KEYS` · hash `0x78D864C7` · **Cliente y servidor**

```lua
local retval = GetStateBagKeys(bagName)
```
```c
object GET_STATE_BAG_KEYS(char* bagName);
```

**Parámetros**

- `bagName` (`char*`): The name of the bag.

**Devuelve:** `object` — Returns an array containing all keys for which the state bag has associated values.

---
### GetStateBagValue

`GET_STATE_BAG_VALUE` · hash `0x637F4C75` · **Cliente y servidor**

```lua
local retval = GetStateBagValue(bagName, key)
```
```c
object GET_STATE_BAG_VALUE(char* bagName, char* key);
```

**Parámetros**

- `bagName` (`char*`)
- `key` (`char*`)

**Devuelve:** `object` — Value.

**Descripción oficial:**

Returns the value of a state bag key.

---
### GetTrainCruiseSpeed

`GET_TRAIN_CRUISE_SPEED` · hash `0xA4921EF5` · **Cliente y servidor**

```lua
local retval = GetTrainCruiseSpeed(train)
```
```c
float GET_TRAIN_CRUISE_SPEED(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `float` — The desired cruise speed of the train. Not the speed the train is currently traveling at

**Descripción oficial:**

Gets the trains desired speed.

---
### GetTrainDirection

`GET_TRAIN_DIRECTION` · hash `0x8DAF79B6` · **Cliente y servidor**

```lua
local retval = GetTrainDirection(train)
```
```c
BOOL GET_TRAIN_DIRECTION(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `BOOL` — True if the train is moving forward on the track, False otherwise

**Descripción oficial:**

Gets the direction the train is facing

---
### GetTrainState

`GET_TRAIN_STATE` · hash `0x81B50033` · **Cliente y servidor**

```lua
local retval = GetTrainState(train)
```
```c
int GET_TRAIN_STATE(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `int` — The trains current state```cpp enum eTrainState
 {
     MOVING = 0,
     ENTERING_STATION,
     OPENING_DOORS,
     STOPPED,
     CLOSING_DOORS,
     LEAVING_STATION,
 } ```

---
### GetTrainTrackIndex

`GET_TRAIN_TRACK_INDEX` · hash `0x9AA339D` · **Cliente y servidor**

```lua
local retval = GetTrainTrackIndex(train)
```
```c
int GET_TRAIN_TRACK_INDEX(Vehicle train);
```

**Parámetros**

- `train` (`Vehicle`): The train handle

**Devuelve:** `int` — The track index the train is currently on.

---
### GetVehicleHandbrake

`GET_VEHICLE_HANDBRAKE` · hash `0x483B013C` · **Cliente y servidor**

```lua
local retval = GetVehicleHandbrake(vehicle)
```
```c
BOOL GET_VEHICLE_HANDBRAKE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### GetVehicleSteeringAngle

`GET_VEHICLE_STEERING_ANGLE` · hash `0x1382FCEA` · **Cliente y servidor**

```lua
local retval = GetVehicleSteeringAngle(vehicle)
```
```c
float GET_VEHICLE_STEERING_ANGLE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `float`

---
### GetVehicleType

`GET_VEHICLE_TYPE` · hash `0xA273060E` · **Cliente y servidor**

```lua
local retval = GetVehicleType(vehicle)
```
```c
char* GET_VEHICLE_TYPE(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`): The vehicle's entity handle.

**Devuelve:** `char*` — If the entity is a vehicle, the vehicle type. If it is not a vehicle, the return value will be null.

**Descripción oficial:**

Returns the type of the passed vehicle.

For client scripts, reference the more detailed [GET_VEHICLE_TYPE_RAW](cliente-1.md#getvehicletyperaw) native.

**Vehicle types**

*   automobile
*   bike
*   boat
*   heli
*   plane
*   submarine
*   trailer
*   train

---
### IsAceAllowed

`IS_ACE_ALLOWED` · hash `0x7EBB9929` · **Cliente y servidor**

```lua
local retval = IsAceAllowed(object)
```
```c
BOOL IS_ACE_ALLOWED(char* object);
```

**Parámetros**

- `object` (`char*`)

**Devuelve:** `BOOL`

---
### IsColshapeCircle

`IS_COLSHAPE_CIRCLE` · hash `0xAAEB581A` · **Cliente y servidor**

```lua
local retval = IsColshapeCircle(colShapeId)
```
```c
BOOL IS_COLSHAPE_CIRCLE(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.

**Devuelve:** `BOOL` — `true` if the collision shape is a circle, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether the collision shape is a circle type.

---
### IsColshapeCuboid

`IS_COLSHAPE_CUBOID` · hash `0x80A7B8DF` · **Cliente y servidor**

```lua
local retval = IsColshapeCuboid(colShapeId)
```
```c
BOOL IS_COLSHAPE_CUBOID(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.

**Devuelve:** `BOOL` — `true` if the collision shape is a cuboid, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether the collision shape is a cuboid type.

---
### IsColshapeCylinder

`IS_COLSHAPE_CYLINDER` · hash `0xA9CC9F3D` · **Cliente y servidor**

```lua
local retval = IsColshapeCylinder(colShapeId)
```
```c
BOOL IS_COLSHAPE_CYLINDER(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.

**Devuelve:** `BOOL` — `true` if the collision shape is a cylinder, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether the collision shape is a cylinder type.

---
### IsColshapeEntityTypeSet

`IS_COLSHAPE_ENTITY_TYPE_SET` · hash `0xB5B22C62` · **Cliente y servidor**

```lua
local retval = IsColshapeEntityTypeSet(colShapeId, entityType)
```
```c
BOOL IS_COLSHAPE_ENTITY_TYPE_SET(int colShapeId, int entityType);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `entityType` (`int`): The entity type index to check.

**Devuelve:** `BOOL` — `true` if the entity type is enabled for this collision shape, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether the collision shape has a specific entity type enabled for detection.

---
### IsColshapePolygon

`IS_COLSHAPE_POLYGON` · hash `0x91E01B1E` · **Cliente y servidor**

```lua
local retval = IsColshapePolygon(colShapeId)
```
```c
BOOL IS_COLSHAPE_POLYGON(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.

**Devuelve:** `BOOL` — `true` if the collision shape is a polygon, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether the collision shape is a polygon type.

---
### IsColshapeRectangle

`IS_COLSHAPE_RECTANGLE` · hash `0xAE0F25EA` · **Cliente y servidor**

```lua
local retval = IsColshapeRectangle(colShapeId)
```
```c
BOOL IS_COLSHAPE_RECTANGLE(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.

**Devuelve:** `BOOL` — `true` if the collision shape is a rectangle, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether the collision shape is a rectangle type.

---
### IsColshapeSphere

`IS_COLSHAPE_SPHERE` · hash `0xC53E0758` · **Cliente y servidor**

```lua
local retval = IsColshapeSphere(colShapeId)
```
```c
BOOL IS_COLSHAPE_SPHERE(int colShapeId);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.

**Devuelve:** `BOOL` — `true` if the collision shape is a sphere, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Returns whether the collision shape is a sphere type.

---
### IsDuplicityVersion

`IS_DUPLICITY_VERSION` · hash `0xCF24C52E` · **Cliente y servidor**

```lua
local retval = IsDuplicityVersion()
```
```c
BOOL IS_DUPLICITY_VERSION();
```

**Devuelve:** `BOOL` — A boolean value.

**Descripción oficial:**

Gets whether or not this is the CitizenFX server.

---
### IsEntityPositionFrozen

`IS_ENTITY_POSITION_FROZEN` · hash `0xEDBE6ADD` · **Cliente y servidor**

```lua
local retval = IsEntityPositionFrozen(entity)
```
```c
bool IS_ENTITY_POSITION_FROZEN(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to check for

**Devuelve:** `bool` — Boolean stating if it is frozen or not.

**Descripción oficial:**

A getter for [FREEZE_ENTITY_POSITION](servidor.md#freezeentityposition).

**Ejemplo (lua):**

```lua
local isFrozen = IsEntityPositionFrozen(PlayerPedId())
```

**Ejemplo (js):**

```js
const isFrozen = IsEntityPositionFrozen(PlayerPedId());
```

---
### IsPointInsideColshape

`IS_POINT_INSIDE_COLSHAPE` · hash `0x324DCFA6` · **Cliente y servidor**

```lua
local retval = IsPointInsideColshape(colShapeId, x, y, z)
```
```c
BOOL IS_POINT_INSIDE_COLSHAPE(int colShapeId, float x, float y, float z);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `x` (`float`): Point X coordinate.
- `y` (`float`): Point Y coordinate.
- `z` (`float`): Point Z coordinate.

**Devuelve:** `BOOL` — `true` if the point is inside the collision shape, `false` otherwise.

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Tests whether a 3D point is inside the specified collision shape.

---
### IsPrincipalAceAllowed

`IS_PRINCIPAL_ACE_ALLOWED` · hash `0x37CF52CE` · **Cliente y servidor**

```lua
local retval = IsPrincipalAceAllowed(principal, object)
```
```c
BOOL IS_PRINCIPAL_ACE_ALLOWED(char* principal, char* object);
```

**Parámetros**

- `principal` (`char*`)
- `object` (`char*`)

**Devuelve:** `BOOL`

---
### IsVehicleEngineStarting

`IS_VEHICLE_ENGINE_STARTING` · hash `0xBB340D04` · **Cliente y servidor**

```lua
local retval = IsVehicleEngineStarting(vehicle)
```
```c
BOOL IS_VEHICLE_ENGINE_STARTING(Vehicle vehicle);
```

**Parámetros**

- `vehicle` (`Vehicle`)

**Devuelve:** `BOOL`

---
### LoadResourceFile

`LOAD_RESOURCE_FILE` · hash `0x76A9EE1F` · **Cliente y servidor**

```lua
local retval = LoadResourceFile(resourceName, fileName)
```
```c
char* LOAD_RESOURCE_FILE(char* resourceName, char* fileName);
```

**Parámetros**

- `resourceName` (`char*`): The resource name.
- `fileName` (`char*`): The file in the resource.

**Devuelve:** `char*` — The file contents

**Descripción oficial:**

Reads the contents of a text file in a specified resource.
If executed on the client, this file has to be included in `files` in the resource manifest.
Example: `local data = LoadResourceFile("devtools", "data.json")`

---
### NetworkGetEntityOwner

`NETWORK_GET_ENTITY_OWNER` · hash `0x526FEE31` · **Cliente y servidor**

```lua
local retval = NetworkGetEntityOwner(entity)
```
```c
int NETWORK_GET_ENTITY_OWNER(Entity entity);
```

**Parámetros**

- `entity` (`Entity`): The entity to get the owner for.

**Devuelve:** `int` — On the server, the server ID of the entity owner. On the client, returns the player/slot ID of the entity owner.

**Descripción oficial:**

Returns the owner ID of the specified entity.

---
### ProfilerEnterScope

`PROFILER_ENTER_SCOPE` · hash `0xC795A4A9` · **Cliente y servidor**

```lua
ProfilerEnterScope(scopeName)
```
```c
void PROFILER_ENTER_SCOPE(char* scopeName);
```

**Parámetros**

- `scopeName` (`char*`): Scope name.

**Devuelve:** `void`

**Descripción oficial:**

Scope entry for profiler.

---
### ProfilerExitScope

`PROFILER_EXIT_SCOPE` · hash `0xB39CA35C` · **Cliente y servidor**

```lua
ProfilerExitScope()
```
```c
void PROFILER_EXIT_SCOPE();
```

**Devuelve:** `void`

**Descripción oficial:**

Scope exit for profiler.

---
### ProfilerIsRecording

`PROFILER_IS_RECORDING` · hash `0xF8B7D7BB` · **Cliente y servidor**

```lua
local retval = ProfilerIsRecording()
```
```c
BOOL PROFILER_IS_RECORDING();
```

**Devuelve:** `BOOL` — True or false.

**Descripción oficial:**

Returns true if the profiler is active.

---
### RegisterCommand

`REGISTER_COMMAND` · hash `0x5FA79B0F` · **Cliente y servidor**

```lua
RegisterCommand(commandName, handler, restricted)
```
```c
void REGISTER_COMMAND(char* commandName, func handler, BOOL restricted);
```

**Parámetros**

- `commandName` (`char*`): The command you want to register.
- `handler` (`func`): A handler function that gets called whenever the command is executed.
- `restricted` (`BOOL`): If this is a server command and you set this to true, then players will need the command.yourCommandName ace permission to execute this command.

**Devuelve:** `void`

**Descripción oficial:**

Registered commands can be executed by entering them in the client console (this works for client side and server side registered commands). Or by entering them in the server console/through an RCON client (only works for server side registered commands). Or if you use a supported chat resource, like the default one provided in the cfx-server-data repository, then you can enter the command in chat by prefixing it with a `/`.

Commands registered using this function can also be executed by resources, using the [`ExecuteCommand` native](#executecommand).

The restricted bool is not used on the client side. Permissions can only be checked on the server side, so if you want to limit your command with an ace permission automatically, make it a server command (by registering it in a server script).

**Example result**:

![](https://i.imgur.com/TaCnG09.png)

**Ejemplo (lua):**

```lua
-- (server side script)
-- Registers a command named 'ping'.
RegisterCommand("ping", function(source, args, rawCommand)
    -- If the source is > 0, then that means it must be a player.
    if (source > 0) then
    
        -- result (using the default GTA:O chat theme) https://i.imgur.com/TaCnG09.png
        TriggerClientEvent("chat:addMessage", -1, {
            args = {
                GetPlayerName(source),
                "PONG!"
            },
            color = { 5, 255, 255 }
        })
    
    -- If it's not a player, then it must be RCON, a resource, or the server console directly.
    else
        print("This command was executed by the server console, RCON client, or a resource.")
    end
end, false --[[this command is not restricted, everyone can use this.]])
```

**Ejemplo (cs):**

```cs
RegisterCommand("ping", new Action<int, List<object>, string>((source, args, rawCommand) =>
{
    if (source > 0) // it's a player.
    {
        // Create a message object.
        dynamic messageObject = new ExpandoObject();
        // Set the message object args (message author, message content)
        messageObject.args = new string[] { GetPlayerName(source.ToString()), "PONG!" };
        // Set the message color (r, g, b)
        messageObject.color = new int[] { 5, 255, 255 };

        // Trigger the client event with the message object on all clients.
        TriggerClientEvent("chat:addMessage", messageObject);
    }
    // It's not a player, so it's the server console, a RCON client, or a resource.
    else
    {
        Debug.WriteLine("This command was executed by the server console, RCON client, or a resource.");
    }
}), false /*This command is also not restricted, anyone can use it.*/ );
```

---
### RegisterResourceAsEventHandler

`REGISTER_RESOURCE_AS_EVENT_HANDLER` · hash `0xD233A168` · **Cliente y servidor**

```lua
RegisterResourceAsEventHandler(eventName)
```
```c
void REGISTER_RESOURCE_AS_EVENT_HANDLER(char* eventName);
```

**Parámetros**

- `eventName` (`char*`): An event name, or "\*" to disable HLL event filtering for this resource.

**Devuelve:** `void`

**Descripción oficial:**

An internal function which allows the current resource's HLL script runtimes to receive state for the specified event.

---
### RemoveConvarChangeListener

`REMOVE_CONVAR_CHANGE_LISTENER` · hash `0xEAC49841` · **Cliente y servidor**

```lua
RemoveConvarChangeListener(cookie)
```
```c
void REMOVE_CONVAR_CHANGE_LISTENER(int cookie);
```

**Parámetros**

- `cookie` (`int`): The cookie returned from [ADD_CONVAR_CHANGE_LISTENER](#addconvarchangelistener)

**Devuelve:** `void`

---
### RemoveStateBagChangeHandler

`REMOVE_STATE_BAG_CHANGE_HANDLER` · hash `0xD36BE661` · **Cliente y servidor**

```lua
RemoveStateBagChangeHandler(cookie)
```
```c
void REMOVE_STATE_BAG_CHANGE_HANDLER(int cookie);
```

**Parámetros**

- `cookie` (`int`): The cookie.

**Devuelve:** `void`

**Descripción oficial:**

**Experimental**: This native may be altered or removed in future versions of CitizenFX without warning.

Removes a handler for changes to a state bag.

---
### SetColshapeEntityType

`SET_COLSHAPE_ENTITY_TYPE` · hash `0xB3A4D128` · **Cliente y servidor**

```lua
SetColshapeEntityType(colShapeId, entityType, value)
```
```c
void SET_COLSHAPE_ENTITY_TYPE(int colShapeId, int entityType, BOOL value);
```

**Parámetros**

- `colShapeId` (`int`): The collision shape ID.
- `entityType` (`int`): The entity type index.
- `value` (`BOOL`): `true` to include this entity type in detection, `false` to exclude it.

**Devuelve:** `void`

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Sets whether the collision shape should detect a specific entity type.

---
### SetResourceKvp

`SET_RESOURCE_KVP` · hash `0x21C7A35B` · **Cliente y servidor**

```lua
SetResourceKvp(key, value)
```
```c
void SET_RESOURCE_KVP(char* key, char* value);
```

**Parámetros**

- `key` (`char*`): The key to set
- `value` (`char*`): The value to write

**Devuelve:** `void`

**Descripción oficial:**

A setter for [GET_RESOURCE_KVP_STRING](#getresourcekvpstring).

**Ejemplo (lua):**

```lua
SetResourceKvp('mollis', 'vesuvius citrate')
```

---
### SetResourceKvpFloat

`SET_RESOURCE_KVP_FLOAT` · hash `0x9ADD2938` · **Cliente y servidor**

```lua
SetResourceKvpFloat(key, value)
```
```c
void SET_RESOURCE_KVP_FLOAT(char* key, float value);
```

**Parámetros**

- `key` (`char*`): The key to set
- `value` (`float`): The value to write

**Devuelve:** `void`

**Descripción oficial:**

A setter for [GET_RESOURCE_KVP_FLOAT](#getresourcekvpfloat).

**Ejemplo (lua):**

```lua
local lickMy = 42.5
SetResourceKvpFloat('bananabread', lickMy)
```

---
### SetResourceKvpFloatNoSync

`SET_RESOURCE_KVP_FLOAT_NO_SYNC` · hash `0x3517BFBE` · **Cliente y servidor**

```lua
SetResourceKvpFloatNoSync(key, value)
```
```c
void SET_RESOURCE_KVP_FLOAT_NO_SYNC(char* key, float value);
```

**Parámetros**

- `key` (`char*`): The key to set
- `value` (`float`): The value to write

**Devuelve:** `void`

**Descripción oficial:**

Nonsynchronous [SET_RESOURCE_KVP_FLOAT](#setresourcekvpfloat) operation; see [FLUSH_RESOURCE_KVP](#getresourcekvpstring).

---
### SetResourceKvpInt

`SET_RESOURCE_KVP_INT` · hash `0x6A2B1E8` · **Cliente y servidor**

```lua
SetResourceKvpInt(key, value)
```
```c
void SET_RESOURCE_KVP_INT(char* key, int value);
```

**Parámetros**

- `key` (`char*`): The key to set
- `value` (`int`): The value to write

**Devuelve:** `void`

**Descripción oficial:**

A setter for [GET_RESOURCE_KVP_INT](#getresourcekvpint).

**Ejemplo (lua):**

```lua
local lickMy = 42
SetResourceKvp('bananabread', lickMy)
```

---
### SetResourceKvpIntNoSync

`SET_RESOURCE_KVP_INT_NO_SYNC` · hash `0x26AEB707` · **Cliente y servidor**

```lua
SetResourceKvpIntNoSync(key, value)
```
```c
void SET_RESOURCE_KVP_INT_NO_SYNC(char* key, int value);
```

**Parámetros**

- `key` (`char*`): The key to set
- `value` (`int`): The value to write

**Devuelve:** `void`

**Descripción oficial:**

Nonsynchronous [SET_RESOURCE_KVP_INT](#setresourcekvpint) operation; see [FLUSH_RESOURCE_KVP](#getresourcekvpstring).

---
### SetResourceKvpNoSync

`SET_RESOURCE_KVP_NO_SYNC` · hash `0xCF9A2FF` · **Cliente y servidor**

```lua
SetResourceKvpNoSync(key, value)
```
```c
void SET_RESOURCE_KVP_NO_SYNC(char* key, char* value);
```

**Parámetros**

- `key` (`char*`): The key to set
- `value` (`char*`): The value to write

**Devuelve:** `void`

**Descripción oficial:**

Nonsynchronous [SET_RESOURCE_KVP](#setresourcekvp) operation; see [FLUSH_RESOURCE_KVP](#getresourcekvpstring).

---
### SetStateBagValue

`SET_STATE_BAG_VALUE` · hash `0x8D50E33A` · **Cliente y servidor**

```lua
SetStateBagValue(bagName, keyName, valueData, valueLength, replicated)
```
```c
void SET_STATE_BAG_VALUE(char* bagName, char* keyName, char* valueData, int valueLength, BOOL replicated);
```

**Parámetros**

- `bagName` (`char*`)
- `keyName` (`char*`)
- `valueData` (`char*`)
- `valueLength` (`int`)
- `replicated` (`BOOL`)

**Devuelve:** `void`

**Descripción oficial:**

Internal function for setting a state bag value.

---
### StartFindKvp

`START_FIND_KVP` · hash `0xDD379006` · **Cliente y servidor**

```lua
local retval = StartFindKvp(prefix)
```
```c
int START_FIND_KVP(char* prefix);
```

**Parámetros**

- `prefix` (`char*`): A prefix match

**Devuelve:** `int` — A KVP find handle to use with [FIND_KVP](#findkvp) and close with [END_FIND_KVP](#endfindkvp)

**Ejemplo (lua):**

```lua
SetResourceKvp('mollis:2', 'should be taken with alcohol')
SetResourceKvp('mollis:1', 'vesuvius citrate')
SetResourceKvp('mollis:manufacturer', 'Betta Pharmaceuticals')

local kvpHandle = StartFindKvp('mollis:')

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
### StateBagHasKey

`STATE_BAG_HAS_KEY` · hash `0x12A330` · **Cliente y servidor**

```lua
local retval = StateBagHasKey(bagName, key)
```
```c
bool STATE_BAG_HAS_KEY(char* bagName, char* key);
```

**Parámetros**

- `bagName` (`char*`): The name of the bag.
- `key` (`char*`): The key used to check data existence.

**Devuelve:** `bool` — Returns true if the data associated with the specified key exists; otherwise, returns false.

---
### TriggerEventInternal

`TRIGGER_EVENT_INTERNAL` · hash `0x91310870` · **Cliente y servidor**

```lua
TriggerEventInternal(eventName, eventPayload, payloadLength)
```
```c
void TRIGGER_EVENT_INTERNAL(char* eventName, char* eventPayload, int payloadLength);
```

**Parámetros**

- `eventName` (`char*`)
- `eventPayload` (`char*`)
- `payloadLength` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

The backing function for TriggerEvent.

---
### UnregisterCommand

`UNREGISTER_COMMAND` · hash `0x9F73FDC` · **Cliente y servidor**

```lua
UnregisterCommand(commandId)
```
```c
void UNREGISTER_COMMAND(int commandId);
```

**Parámetros**

- `commandId` (`int`): The command ID returned by `REGISTER_COMMAND`.

**Devuelve:** `void`

**Descripción oficial:**

> This native only works in FiveM for GTAV Enhanced.

Unregisters a command that was previously registered with `REGISTER_COMMAND`, using the command ID returned by that native.

**Ejemplo (lua):**

```lua
local commandId = RegisterCommand("hello", function(source, args, rawCommand)
    print("hello!")
end, false)

-- later, when the command is no longer needed
UnregisterCommand(commandId)
```

---
### WasEventCanceled

`WAS_EVENT_CANCELED` · hash `0x58382A19` · **Cliente y servidor**

```lua
local retval = WasEventCanceled()
```
```c
BOOL WAS_EVENT_CANCELED();
```

**Devuelve:** `BOOL` — A boolean.

**Descripción oficial:**

Returns whether or not the currently executing event was canceled.

---
