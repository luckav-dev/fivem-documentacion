> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/oxmysql/placeholders.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Placeholders

Placeholders allow for query parameters to be safely executed, preventing [common SQL injection methods](https://bobby-tables.com/).

Parameters can be passed an an array or object (referred to as named parameters).

```lua
local identifier = 'license:abc123'
local group = 'admin'

MySQL.scalar('SELECT `username` FROM `users` WHERE `identifier` = ? AND `group` = ?', { identifier, group })

-- Named placeholders (deprecated)
MySQL.scalar('SELECT `username` FROM `users` WHERE `identifier` = @identifier AND `group` = @group', {
    group = group
    identifier = identifier
})
```

These are distinct from prepared statements which are handled by the MySQL server; you can use `MySQL.prepare` for more optimised and secure queries.
