> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/esx_textui.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_textui

The text ui (hud) system used by `es_extended`
**Only available on clientside**

### TextUI
This function will show a text ui pop up.

**Arguments**
- message: `string`
  - The TextUI message.

**TextUI types**
- success 
- error 
- info

**ESX Example** 
```lua
ESX.TextUI('Press [E] to use', 'error')
```

**Export Example** 
```lua
exports['esx_textui']:TextUI('Press [E] to use', 'error')
```

### HideUI 
This function will hide the TextUI.

> **Advertencia:** This will close any TextUI that is currently open.

**ESX Example** 
```lua
local interactCoords = vector3(0, 0, 0)
CreateThread(function()
    local TextUI
    while true do
        local coords = GetEntityCoords(PlayerPedId())
        local inDist = #(coords - interactCoords) < 2.0
        if inDist and not TextUI then 
            ESX.TextUI('Press [E] to interact')
        elseif inDist and TextUI then 
            ESX.HideUI() 
        end
        Wait(500)
    end 
end) 
```

**Export Example** 
```lua
local interactCoords = vector3(0, 0, 0)
CreateThread(function()
    local TextUI
    while true do
        local coords = GetEntityCoords(PlayerPedId())
        local inDist = #(coords - interactCoords) < 2.0
        if inDist and not TextUI then 
            exports['esx_textui']:TextUI('Press [E] to interact')
        elseif inDist and TextUI then 
            exports['esx_textui']:HideUI()
        end
        Wait(500)
    end 
end) 
```
