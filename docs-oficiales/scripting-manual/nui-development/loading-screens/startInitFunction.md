# startInitFunction

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/startInitFunction/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when init functions are about to be invoked.

[startInitFunctionOrder](startInitFunctionOrder.md) will be triggered after this with additional info,
in turn triggering multiple [initFunctionInvoking](initFunctionInvoking.md) and in turn [initFunctionInvoked](initFunctionInvoked.md) triggers.
After the init functions were invoked, [startInitFunctionOrder](startInitFunctionOrder.md) will be triggered again with additional functions,
or [endInitFunction](endInitFunction.md) will be triggered, finalizing the process.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'startInitFunction',
    type: string,
}
```

- **eventName**: The event name.
- **type**: The type of init functions to be invoked.
