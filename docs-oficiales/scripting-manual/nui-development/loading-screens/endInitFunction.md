# endInitFunction

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/endInitFunction/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when init functions completed invoking, finalizing the [startInitFunction](startInitFunction.md) event process.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'endInitFunction',
    type: string,
}
```

- **eventName**: The event name.
- **type**: The type of init functions that finished invoking.
