# RemoveEventHandler

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/RemoveEventHandler/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Removes the provided event handler.

## Syntax

```lua
RemoveEventHandler(table eventHandlerData)
```

### Required arguments

- **eventHandlerData**: The return value of [AddEventHandler][].

## Examples

```lua
local eventA = AddEventHandler("someEvent", function()
  print("someEvent executed")
end)

TriggerEvent("someEvent")

RemoveEventHandler(eventA)
```

[AddEventHandler]: AddEventHandler.md
