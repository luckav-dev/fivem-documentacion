# SendNUIMessage

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/SendNUIMessage/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use this to send data to the NUI (NewUI)

## Syntax

```lua
SendNUIMessage(table data)
```

### Required arguments

- **data** data that will be sent and received in NUI

## Examples

LUA

```lua
SendNUIMessage({
    hello = "world",
    action = "showMessage"
})
```

JS (NUI PART)

```js
window.addEventListener('message', (event) => {
    let data = event.data
    if(data.action == 'showMessage') {
        console.log(`Hello ${data.hello}!`) // will print Hello world! in the console (F8)
    }
})
```
