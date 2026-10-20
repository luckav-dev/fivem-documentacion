> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/tebex/slots/canuse.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Prevent Usage

Have your own casino membership logic? Want to add some other requirements before a player can use the slot machine? No problem! Simply navigate to `server/utils.lua` and find the following function:

```lua
function CanUse(source)
    return true
end
```

Here you can add your own logic. To prevent the player from using the slot machine, simply return `false`.

```lua
function CanUse(source)
    local player = exports.qbx_core:GetPlayer(source)
    if not player.PlayerData.metadata.casino_member then
        return false
    end
    return true
end
```
