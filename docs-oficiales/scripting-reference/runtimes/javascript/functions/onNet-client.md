# onNet - client

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/onNet-client/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use `onNet` function when you want to listen from client **AND** from server.\
This declares an event which gets triggered with [emit](emit-client.md) (from client) or [emitNet](emitNet-server.md) (from server).

## Signature

```ts
function onNet(eventName: string, fn: Function) => void
```

### Required arguments

- **eventName**: The event name you want to expose.
- **fn**: The function to execute when the event get triggered.

## Examples

```ts
let myNameIs = "Carl";

onNet("foo:serverCalledYou", (newName: string) => {
    myNameIs = newName;
    console.warn(`Someone change your name to ${newName}`);

    if (newName.toLowerCase() === "idiot") {
        console.warn("Looks like he didn't like you.");
    }
});
```
