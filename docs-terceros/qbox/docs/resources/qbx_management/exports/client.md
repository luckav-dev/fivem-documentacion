> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_management/exports/client.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Client Exports

*Documentation for client-side exports in the qbx_management resource. These exports provide functionality for managing boss menus and other management-related features for jobs and gangs within the Qbox framework.*

## OpenBossMenu

Open the primary job or gang boss menu as long as you have the proper permissions.

```lua
exports.qbx_management:OpenBossMenu(groupType)
```

- groupType: `'gang' | 'job'`
