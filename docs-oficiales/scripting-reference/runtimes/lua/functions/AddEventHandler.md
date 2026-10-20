# AddEventHandler

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/AddEventHandler/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use this to listen for events, see the [events][listening-for-events] page for more info.

## Syntax

```lua
AddEventHandler(string eventName, function callback)
```

### Required arguments

- **eventName**: The name of the event you want to listen to.
- **callback**: The function to run when the event is called.

## Examples

-- SERVER

Don't forget to [RegisterNetEvent][]!

```lua
AddEventHandler('eventName', function(text)
  print(('I just received %s from %i'):format(text, source)) -- I just received Hello world! from (player id)
  -- source is a global variable (Player's id)
end)
```

-- CLIENT

```lua
TriggerServerEvent('eventName', 'Hello world!')
```

[listening-for-events]: ../../../../scripting-manual/working-with-events/listening-for-events.md
[RegisterNetEvent]: RegisterNetEvent.md
