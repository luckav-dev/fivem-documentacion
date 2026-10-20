# initFunctionInvoking

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/initFunctionInvoking/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when an init function is being invoked, as a result of [startInitFunctionOrder](startInitFunctionOrder.md).

Several [onDataFileEntry](onDataFileEntry.md) may be triggered after this.
After the init function finishes invoking, [initFunctionInvoked](initFunctionInvoked.md) will be triggered.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'initFunctionInvoking',
    type: string,
    name: string,
    idx: number,
}
```

- **eventName**: The event name.
- **type**: The type of init function being invoked.
- **name**: The name of the init function.
- **idx**: The index of the init function.
