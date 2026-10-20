> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/client/modules/interactions.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# Interactions

This module is responsible for handling all interactions between players and the world.

## Functions

### RegisterInteraction
Register a new interaction.

**Arguments**
- name: `string`
  - The name of the interaction.
- onPress: `function`
  - The function to call when the interaction is pressed.
- condition: `function`
  - The function to call to check if the interaction is possible.

**Example using [points](../imports/point.md)**
```lua
local canInteract = false
local point = ESX.Point:new({
    coords = vec3(0, 0, 0),
    hidden = false,
    enter = function()
        canInteract = true
        ESX.TextUI(("Press [%s] to interact"):format(ESX.GetInteractKey()))
    end,
    leave = function()
        canInteract = false
        ESX.HideUI()
    end
})

ESX.RegisterInteraction('my_interaction', function()
  print('Interaction pressed')
end, function()
  return canInteract
end)
```

### GetInteractKey
Get the global interact key ("E" by default).

**Example**
```lua
local key = ESX.GetInteractKey()

print("Interact key: " .. key)
```
