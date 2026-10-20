# initFunctionInvoked

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/initFunctionInvoked/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered after an init function was invoked, after [initFunctionInvoking](initFunctionInvoking.md).

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'initFunctionInvoked',
    type: string,
    name: string,
}
```

- **eventName**: The event name.
- **type**: The type of init function that was invoked.
- **name**: The name of the init function.
