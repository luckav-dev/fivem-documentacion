# EmitNet - client

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/emitNet-client/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use `emitNet` function when you want to trigger an event from the client to the server.\
You need to declare the event on the server with [onNet](onNet-server.md) first.

## Signature

```ts
function emitNet(eventName: string, ...args?: any ) => void
```

### Required argument

- **eventName**: The event name you want to trigger.

### Optional arguments

- **...args**: The arguments you want to pass.

## Examples

```ts
// No arg
emitNet("foo:killPatrickForMe");

// With args
emitNet("foo:killThisGuyForMe", 2);
```
