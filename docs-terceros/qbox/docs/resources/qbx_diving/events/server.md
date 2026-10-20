> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_diving/events/server.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Server Events

*A detailed documentation of server-side events for the qbx_diving resource. This document outlines both non-networked and networked events related to diving activities, such as coral collection and selling mechanics. Each event includes its purpose, usage examples, and parameter specifications.*

> **Advertencia:** These events **MUST NOT** be triggered by any other scripts.

## Non-Networked Events

### qbx_diving:server:coralTaken

Triggered when a player has collected coral from the sea bed.

```lua
AddEventHandler('qbx_diving:server:coralTaken', function(coords) end)
```

- coords: `vector3`

## Networked Events

### qbx_diving:server:sellCoral

Triggered when a player attempts to sell coral. \
Does not guarantee that the player has any coral in their inventory.

```lua
RegisterNetEvent('qbx_diving:server:sellCoral', function() end)
```
