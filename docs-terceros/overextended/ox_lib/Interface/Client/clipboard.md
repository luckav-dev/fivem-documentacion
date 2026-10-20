> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Interface/Client/clipboard.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Clipboard

## lib.setClipboard

Sets the player's clipboard to the specified string value.

> **Nota:** Will not work if focus is already taken by some NUI component.

> **Nota:** To create a new line use `\t\n` not just `\n` in your string.

**Lua**

```lua
lib.setClipboard(value)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client';

lib.setClipboard(value);
```

- value: `string`
