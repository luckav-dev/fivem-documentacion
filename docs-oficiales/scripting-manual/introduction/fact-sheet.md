# Fact Sheet

> Fuente original: https://docs.fivem.net/docs/scripting-manual/introduction/fact-sheet/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

Here's a quick informative sheet to get you up to speed with FiveM development.

## What does ScRT mean?

_ScRT_ means _Scripting Runtime_ or _Script Runtime_. FiveM has three different scripting runtimes available (Lua, C# and JavaScript), and they are mentioned down below.

## How do I get started with scripting?

The scripting manual can be found [here](../README.md) and it features the following articles:

- [Introduction to resources](introduction-to-resources.md)
  - [Creating your first script](creating-your-first-script.md)
- [Scripting runtimes](../runtimes/README.md)
  - [Scripting in Lua](../runtimes/lua.md)
  - [Scripting in JavaScript](../runtimes/javascript.md)
  - [Scripting in C#](../runtimes/csharp.md)
- [Migrating from deprecated methods](../migrating-from-deprecated/README.md)
  - [Chat Messages](../migrating-from-deprecated/chat-messages.md)
- [Working with events](../working-with-events/README.md)
  - [Listening for events](../working-with-events/listening-for-events.md)
  - [Triggering events](../working-with-events/triggering-events.md)
- [NUI](../nui-development/README.md)
- [Using Scaleform](../using-scaleform/README.md)
- [Voice](../voice/README.md)
- [Using new game features](../using-new-game-features/README.md)

You can refer to the page mentioned above to see the scripting manual in full detail.

## Natives

### What's a Native?

Simply put, a Native, is a function exposed by the game in order to be called from scripts and either perform a given action in the game itself or request data from it. For example, one would type the following, to get the local player's ped from a Lua script and then give a weapon to that ped.

```lua
ped = GetPlayerPed(-1)
GiveWeaponToPed(ped, GetHashKey("WEAPON_PISTOL"), 100, false, false) -- We got a gun now!
```

### Where are all the natives?

Natives are located [here](../../../natives/README.md).

## Developer Commands & Game References

### Where are all the developer commands?

Developer commands can be found [here](../../client-manual/console-commands.md#developer-commands).

### Where are all the blips, ped models and others?

These are named _Game references_, and they can be found over [here](../../game-references/README.md).

## Performance

### What are hitch warnings?

Hitch warnings indicate that one of your resources is not performing as it should and you should look into the affected resource to _figure out why, using the profiler can help diagnose this._ Things such as these, can sometimes be caused by writing underperforming SQL queries that take a long time to execute, as well as unoptimized loops that end up halting the script execution.

### Profiler

The profiler can be used to diagnose _why_ a resource is taking a long time to execute, there's a [guide](../debugging/using-profiler.md) explaining how to use it, it can be used both on the server and client.

### Resource Monitor (Resmon)

The resource monitor can be used on the client to diagnose which resource is taking a long time to execute, it shows certain things such as cpu usage (msec) and memory usage for each resource.

It can be enabled by typing `resmon true`. It's possible that you see a message such as `Access denied for command resmon` (especially when running in production builds), this means that the developer mode needs to be enabled by launching the FiveM/RedM client using the `+set moo 31337` argument (for example, by adding it to a shortcut).
