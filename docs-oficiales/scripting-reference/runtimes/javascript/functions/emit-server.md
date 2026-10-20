# Emit - server

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/emit-server/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use `emit` function when you want to trigger an event from the server to the server.\
You need to declare the event on the server with [on](on-server.md) or [onNet](onNet-server.md) first.

## Signature

```ts
function emit(eventName: string, ...args?: any ) => void
```

### Required argument

- **eventName**: The event name you want to trigger.

### Optional arguments

- **...args**: The arguments you want to pass.

## Examples

```ts
// No arg
emit("foo:playerIsHere");

// With args
emit("foo:thisPlayerIsHere", playerId, playerLicense);
```
