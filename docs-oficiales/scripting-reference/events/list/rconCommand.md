# rconCommand

> Fuente original: https://docs.fivem.net/docs/scripting-reference/events/list/rconCommand/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

## Parameters

> **⚠️ Advertencia**
>
> This event is deprecated. Please use [`REGISTER_COMMAND`](../../../../natives/cfx/compartidos.md#registercommand) instead, and use the `restricted` flag.


```
string command, table/array arguments
```

- **command**: A string containing the command name that was executed.
- **arguments**: A list containing all arguments passed to the command.

## Examples

### JavaScript Example:

```js
on('rconCommand', (command, args) => {
    console.log(`${command} called over RCON with ${args}`)
});
```
