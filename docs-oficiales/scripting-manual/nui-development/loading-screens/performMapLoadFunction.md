# performMapLoadFunction

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/performMapLoadFunction/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when a map load function was called, either by itself or as a result of [onDataFileEntry](onDataFileEntry.md).

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'performMapLoadFunction',
    idx: number,
}
```

- **eventName**: The event name.
- **idx**: The map index.
