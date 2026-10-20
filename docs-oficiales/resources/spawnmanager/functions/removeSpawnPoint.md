# removeSpawnPoint

> Fuente original: https://docs.fivem.net/docs/resources/spawnmanager/functions/removeSpawnPoint/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

## About

This export allows you to remove an existing spawnpoint from the spawnmanager.

## Name

```
removeSpawnPoint
```

## Parameters

```
int spawnIdx
```

### Required Arguments

- **spawnIdx** The index of the spawnpoint to remove.

## Examples

### Lua Example:

```lua
-- Add a new spawnpoint!
local mySpawnPoint = exports.spawnmanager:addSpawnPoint({
    x = 466.8401,
    y = 197.7201,
    z = 111.5291,
    heading = 291.71,
    model = 'a_m_m_farmer_01'
})

-- Now let's remove it...
exports.spawnmanager:removeSpawnPoint(mySpawnPoint)
```
