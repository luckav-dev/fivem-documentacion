# startInitFunctionOrder

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/startInitFunctionOrder/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered after [startInitFunction](startInitFunction.md), with additional data.
May be triggered multiple times under the same init function type, but with a different `order` value.

Several [initFunctionInvoking](initFunctionInvoking.md) and in turn [initFunctionInvoked](initFunctionInvoked.md) events will be triggered after this.
After the init functions were invoked, **startInitFunctionOrder** may be triggered again with additional functions,
or [endInitFunction](endInitFunction.md) will be triggered, finalizing the process.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'startInitFunctionOrder',
    type: string,
    order: number,
    count: number,
}
```

- **eventName**: The event name.
- **type**: The type of init functions to be invoked.
- **order**: The order of the init functions to be invoked.
- **count**: The amount of init function to be invoked.
