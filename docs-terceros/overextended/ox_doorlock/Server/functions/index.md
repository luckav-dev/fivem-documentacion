> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_doorlock/Server/functions/index.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Functions

Gets data for a door with the given id, matching the id for the database entry.

## getDoor

```lua
exports.ox_doorlock:getDoor(doorId)
```

Gets data for a door with the given `id`, matching the id for the database entry.

- id: `number`

Return:

- door: `table`

## getDoorFromName

```lua
exports.ox_doorlock:getDoorFromName(name)
```

Gets data for a door with the given `name`, matching the name for the database entry.

- name: `string`

Return:

- door: `table`

## editDoor

```lua
exports.ox_doorlock:editDoor(doorId, data)
```

Edit configuration for the given doorId.

- doorId: `number`
- data: `table`

## setDoorState

```lua
exports.ox_doorlock:setDoorState(doorId, state)
```

Sets a door with the given doorId as locked if state is `true` or `1`.

- doorId: `number`
- state: `0` or `1` or `boolean`
