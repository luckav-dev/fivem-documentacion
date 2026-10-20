# onNet - server

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/onNet-server/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use `onNet` function when you want to listen from server **AND** from client.\
This declares an event which gets triggered with [emit](emit-server.md) (from server) or [emitNet](emitNet-client.md) (from client).

## Signature

```ts
function onNet(eventName: string, fn: Function) => void
```

### Required arguments

- **eventName**: The event name you want to expose.
- **fn**: The function to execute when the event get triggered.

## Examples

```ts
onNet(
  "myResource:doMassiveStuff",
  (heavyArg: Array<string>) => {
    heavyArg = heavyArg.map(val => val + ".");
    // Note that source is accessible when the event is called from a client.
    // Read more on emit on the dedicated emit page
    emit("myResource:returnMassiveStuff", source, heavyArg);
  }
);
```
