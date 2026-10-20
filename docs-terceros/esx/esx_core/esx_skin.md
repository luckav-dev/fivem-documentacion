> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/esx_skin.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_skin

The skin managing system used by `es_extended`
**Only available on clientside**

### Get Last Skin
Get the player's last known skin

**Example**
```lua
TriggerEvent("esx_skin:getLastSkin", function(lastSkin)
    print(json.encode(lastSkin))
end)
```

### Open the skin menu
Open the skin menu
**Arguments**
- submitCb: `function`
  - Callback that should be triggered when saving the skin.
- cancelCb?: `function`
  - Callback that should be triggered when abborting.

### Get the current skin
Get the current skin
**Arguments**
- cb: `function`
  - Callback that should be triggered when the skin is received.

**Example**
```lua
ESX.TriggerServerCallback("esx_skin:getPlayerSkin", function(skin)
    if skin == nil then
        TriggerEvent("skinchanger:loadSkin", { sex = 0 }, OpenSaveableMenu)
        Wait(100)
    else
        TriggerEvent("skinchanger:loadSkin", skin)
        Wait(100)
    end
end)
```

### Open the skin menu
Open the skin menu.

**Arguments**
- submitCb?: `function`
  - Callback that should be triggered when saving the skin.
- cancelCb?: `function`
  - Callback that should be triggered when abborting.

**Example**
```lua
TriggerEvent("esx_skin:openSaveableMenu", 
    function()
        finished = true
    end, function()
        finished = true
end)
```
