# RegisterNUICallback

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/RegisterNUICallback/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

> **⚠️ Advertencia**
>
> **Legacy API:** This function is kept for backwards compatibility. New code should use the [`REGISTER_NUI_CALLBACK`](../../../../../natives/cfx/cliente-1.md#registernuicallback) native instead. Refer to the current [NUI callback documentation][nuicallbackinlua] for examples.


## Syntax

```lua
RegisterNUICallback(string eventName, function callback)
```

### Required arguments

- **eventName**: The name of the event you want to listen to.
- **callback**: The function to run when the event is called from NUI.

## Examples

LUA

```lua
RegisterNUICallback('getItemInfo', function(data, cb)
    -- POST data gets parsed as JSON automatically
    local itemId = data.itemId

    if not itemCache[itemId] then
        cb({ error = 'No such item!' })
        return
    end

    -- and so does callback response data
    cb(itemCache[itemId])
end)
```

Browser-side JS, this calls into the NUI Callback to and will get the NUI data back as a response

```js
fetch(`https://${GetParentResourceName()}/getItemInfo`, {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json; charset=UTF-8',
    },
    body: JSON.stringify({
        itemId: 'my-item'
    })
}).then(resp => resp.json()).then(resp => console.log(resp));
```

[nuicallbackinlua]: ../../../../scripting-manual/nui-development/nui-callbacks.md#registering-a-nui-callback-in-lua
