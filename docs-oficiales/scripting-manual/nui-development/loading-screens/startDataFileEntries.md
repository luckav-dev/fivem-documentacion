# startDataFileEntries

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/startDataFileEntries/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when data file entries are incoming.

Several [onDataFileEntry](onDataFileEntry.md) events will be triggered after this,
and a [endDataFileEntries](endDataFileEntries.md) event will be triggered after the given data files entries are done.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'startDataFileEntries',
    count: number,
}
```

- **eventName**: The event name.
- **count**: The amount of data file entries incoming.
