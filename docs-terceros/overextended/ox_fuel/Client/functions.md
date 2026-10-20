> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_fuel/Client/functions.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Functions

## setMoneyCheck

Override the built-in money check.

```lua
exports.ox_fuel:setMoneyCheck(method)
```

### Parameters

- method: `function(): number`

### Example

```lua
exports.ox_fuel:setMoneyCheck(function()
    local accounts = ESX.GetPlayerData().accounts

    for i = 1, #accounts do
        if accounts[i].name == 'bank' then
            return accounts[i].money
        end
    end

    return 0
end)
```
