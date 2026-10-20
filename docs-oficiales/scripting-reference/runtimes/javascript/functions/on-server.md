# On - server

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/on-server/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use `on` function when you want to listen from server only.\
This declares an event which gets triggered with [emit](emit-server.md) from the server.

## Signature

```ts
function on(eventName: string, fn: Function) => void
```

### Required arguments

- **eventName**: The event name you want to expose.
- **fn**: The function to execute when the event get triggered.

## Examples

```ts
on(
  "foo:kickBar",
                   // We can add callback
  (barId: string, cb: Function => {
    DropPlayer(barId, "Foo doesn't want you anymore!");
    cb("Job is done!");
  }
);
```
