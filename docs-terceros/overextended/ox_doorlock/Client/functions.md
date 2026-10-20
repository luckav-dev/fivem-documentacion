> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_doorlock/Client/functions.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Functions

## pickClosestDoor

Attempt to pick the lock of the closest door. Dependant on server-side checks and may fail.

```lua
exports.ox_doorlock:pickClosestDoor()
```

## useClosestDoor

Interact with the closest door. Dependant on server-side checks and may fail.

```lua
exports.ox_doorlock:useClosestDoor()
```

## getClosestDoor

Returns the closest door.

```lua
exports.ox_doorlock:getClosestDoor()
```

Return:

- door: `number`
