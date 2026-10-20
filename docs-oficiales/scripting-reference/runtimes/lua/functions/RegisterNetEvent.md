# RegisterNetEvent

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/RegisterNetEvent/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

<!-- alias: RegisterServerEvent for server only -->

Marks the event safe for network use. Aka, allows you to trigger the eventName event on the client, from a server side
script. If you do not provide a callback function use [AddEventHandler][] to listen for the event after registering it.

## Syntax

```lua
RegisterNetEvent(string eventName, function callback)
```

### Required arguments

- **eventName**: A string representing the event name to register.

### Optional arguments

- **callback**: The function to run when the event is called.

## Examples

```lua
RegisterNetEvent('eventName', function(...)
  print('Event fired')
end)
```

or

```lua
RegisterNetEvent('eventName')
AddEventHandler('eventName', function(...)
  print('Event fired')
end)
```

[AddEventHandler]: AddEventHandler.md
