> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/DisableControls/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

A centralized way to track and disable [game controls](https://docs.fivem.net/docs/game-references/controls/#controls).

## lib.disableControls

Call on frame to disable all stored controls.

```lua
lib.disableControls()
```

## lib.disableControls:Add

Adds the specified control(s) to the stored list.  
If the control is already being tracked, the stored counter will be incremented.

```lua
lib.disableControls:Add(...)
```

- vararg: `number` or `number[]`
  - Control(s) to add a stored count of

## lib.disableControls:Remove

Removes the specified control(s) from the stored list.  
If the stored counter for a given control is greater than one, the stored counter will be decremented.

```lua
lib.disableControls:Remove(...)
```

- vararg: `number` or `number[]`
  - Control(s) to remove a stored count of

## lib.disableControls:Clear

Clears the stored counter(s) for the specified control(s).

```lua
lib.disableControls:Clear(...)
```

- vararg: `number` or `number[]`
  - Control(s) to clear out from being tracked
