> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/oxmysql/Functions/single.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Single

Returns all selected columns for a single row.

## Promise

**Lua**

```lua
local row = MySQL.single.await('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ? LIMIT 1', {
    identifier
})

if not row then return end

print(row.firstname, row.lastname)
```

**JS**

```js
const row = await MySQL.single('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ? LIMIT 1', [
  identifier
])

if (!row) return;

console.log(row.firstname, row.lastname)
```

**Aliases**

- `exports.oxmysql.single_async`

## Callback

**Lua**

```lua
MySQL.single('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ? LIMIT 1', {
    identifier
}, function(row)
    if not row then return end

    print(row.firstname, row.lastname)
end)
```

**JS**

```js
MySQL.single('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ? LIMIT 1', [
  identifier
], (row) => {
  if (!row) return;

  console.log(row.firstname, row.lastname)
})
```

**Aliases**

- `exports.oxmysql.single`
