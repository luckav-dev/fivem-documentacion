> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_doorlock/Server/events.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Events

## Handlers

These events **should not** be triggered by any other scripts.

### ox_doorlock:stateChanged

Triggered when a doors state is updated.

```lua
AddEventHandler('ox_doorlock:stateChanged', function(source, doorId, state, usedItem) end)
```

- source: `number` or `nil`
- doorId: `number`
- state: `boolean`
- usedItem: `string` or `false` or `nil`
