> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/client/imports/point.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# Points

Points are a better way to handle player proximity events. They are more efficient than using a `CreateThread` to check if a player is near a certain point.

## Properties

- `coords`
    - type: `table`/ `vector3`
    - description: The coordinates of the point
- `distance`
    - type: `number`
    - description: The distance to draw the point at
- `hidden`
    - type: `boolean`
    - description: Whether the point is hidden or not
- `enter`
    - type: `function`
    - description: A function that is called when the player enters the point
- `leave`
    - type: `function`
    - description: A function that is called when the player leaves the point
- `inside`
    - type: `function`
    - description: A function that is called every frame when player is inside the point

## Create a Point

```lua
local point = ESX.Point:new({
        coords = vector3(0.0, 0.0, 0.0),
        distance = 15.0,
        enter = function()
            print("Entered point")
        end,
        leave = function()
            print("Left point")
        end,
        inside = function(point)
            local distance = point.currDistance
            print("Inside point, distance: " .. distance)
        end
    })
```

## Delete a Point

```lua
---- [[ Create a point ]] ----#
local point = [[ Point Class ]]
point:delete()
```

## Hide/UnHide a Point

```lua
---- [[ Create a point ]] ----
local point = [[ Point Class ]]
local hidden = true
point:toggle(hidden)
```
