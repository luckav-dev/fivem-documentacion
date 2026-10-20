# Lua Support for Compile-Time Jenkins Hashes

> Fuente original: https://docs.fivem.net/docs/cookbook/2019/06/23/lua-support-for-compile-time-jenkins-hashes/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

> **⚠️ Advertencia — Cookbook Archive**
>
> **Note:** This Cookbook article was originally published on **June 23, 2019**. Newer information may exist.


In GTA/RAGE games, you'll often encounter native functions either taking or returning a Jenkins one-at-a-time hash, like the ones returned by [GET\_HASH\_KEY](../../../../../natives/gta5/MISC.md#gethashkey).

Traditionally, code would have had to either hardcode hashes (like `-1044093321`), or use GET\_HASH\_KEY directly (like `GetHashKey("a_m_y_skater_01")`). This would have lead to either less readability and maintainability, or having to wait for a slow native invocation.

Starting in releases of FiveM/FXServer shipping within the next week, CfxLua has gained support for a new string literal: the backtick string -- ` `` `. Now, you'll have an alternative to the former two, that will still be readable, and will be replaced with a hash during Lua compilation time: `` `a_m_y_skater_01` ``.

Let's look at a real-world example:

```
CreateThread(function()
    while true do
        Wait(0)

        local f = 0
        local ped = PlayerPedId()

        for i = 1, 10000 do
            if GetEntityModel(ped) == `a_m_y_skater_01` then
                f = f + 1
            end
        end

        print(f)
    end
end)
```

This Lua code runs at around 18 milliseconds per tick on our testing system. The old-style equivalent would've run a lot worse - replacing the `` `a_m_y_skater_01` `` part with `GetHashKey('a_m_y_skater_01')` results in a tick time of _43 milliseconds_ on the same system - more than twice as slow!

---

*Original discussion thread: [https://forum.fivem.net/t/lua-support-for-compile-time-jenkins-hashes/600570](https://forum.fivem.net/t/lua-support-for-compile-time-jenkins-hashes/600570)*
