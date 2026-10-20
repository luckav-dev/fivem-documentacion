> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_management/exports/server.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Server Exports

*Documentation for server-side exports in the qbx_management resource. These exports provide functionality for registering and managing boss menus, handling group finances, and other management-related features for jobs and gangs within the Qbox framework.*

## RegisterBossMenu

Creates a boss menu.

> **Advertencia:** This is a runtime-only change.
> This won't persist across restarts and won't modify files.

```lua
exports.qbx_management:RegisterBossMenu(menuInfo)
```

- menuInfo: `table`
  - groupName: `string`
  - type: `'gang' | 'job'`
  - coords: `vector3`
  - size?: `vector3`
    - Default: `vec3(1.5, 1.5, 1.5)`
  - rotation?: `number`
    - Default: `0.0`
