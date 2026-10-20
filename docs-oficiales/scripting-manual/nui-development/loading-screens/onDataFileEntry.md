# onDataFileEntry

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/onDataFileEntry/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when a data file entry occurred, as either a result of
[startDataFileEntries](startDataFileEntries.md) or [initFunctionInvoking](initFunctionInvoking.md).

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'onDataFileEntry',
    name: string,
    type: number,
    isNew: boolean,
}
```

- **eventName**: The event name.
- **name**: The name of the data file entry.
- **type**: The type of the data file entry.
- **isNew**: Whether this data file entry is new.
