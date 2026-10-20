# endDataFileEntries

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/endDataFileEntries/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when data file entries have ended, after the [startDataFileEntries](startDataFileEntries.md) event
and several [onDataFileEntry](onDataFileEntry.md) events.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'endDataFileEntries',
}
```

- **eventName**: The event name.
