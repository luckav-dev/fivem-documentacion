> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/tebex/slots/requireditem.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Required Item

Not only can you change the required item. You can change what item it takes when spinning **and** give a completely different item when the player wins! Let's navigate to `server/utils.lua`.

```lua
function CanSpin(source, betAmount)
    local itemName = 'cash'
    local itemCount = exports.ox_inventory:GetItemCount(source, itemName)

    ...
end
```

Simply change the `itemName` variable to whatever item you want to use. The same goes goes for the rewarding.

```lua
function RewardPlayer(source, winAmount)
    local itemName = 'cash'
    ...
end
```

Same changes apply here :D
