> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_fuel/Server/functions.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Functions

## setPaymentMethod

Override the built-in payment method.

```lua
exports.ox_fuel:setPaymentMethod(method)
```

### Parameters

- method: `function(): boolean?`

### Example

```lua
exports.ox_fuel:setPaymentMethod(function(playerId, amount)
    local xPlayer = ESX.GetPlayerFromId(playerId)
    local bankAmount = xPlayer.getAccount('bank').money

    if bankAmount >= amount then
        xPlayer.removeAccountMoney('bank', amount)
        return true
    end

    TriggerClientEvent('ox_lib:notify', source, {
        type = 'error',
        description = locale('not_enough_money', amount - bankAmount)
    })
end)
```
