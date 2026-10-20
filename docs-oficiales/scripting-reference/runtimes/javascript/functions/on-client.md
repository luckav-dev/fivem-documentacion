# On - client

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/on-client/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use `on` function when you want to listen from client only.\
This declares an event which gets triggered with [emit](emit-client.md) from the client.

## Signature

```ts
function on(eventName: string, fn: Function) => void
```

### Required arguments

- **eventName**: The event name you want to expose.
- **fn**: The function to execute when the event get triggered.

## Examples

```ts
// No arg
on("foo:imReady", () => {
    console.log("I'm ready to go!");
});

// With arg
on("foo:printMyDelivery", (delivery: string) => {
    console.log(`delivery received: ${delivery}`);
});

// Direct function call
on("foo:spawnMyCar", spawnCar);
```
