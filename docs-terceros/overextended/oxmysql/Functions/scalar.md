> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/oxmysql/Functions/scalar.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Scalar

Returns the first column for a single row.

## Promise

**Lua**

```lua
local firstName = MySQL.scalar.await('SELECT `firstname` FROM `users` WHERE `identifier` = ? LIMIT 1', {
    identifier
})

print(firstName)
```

**JS**

```js
const firstName = await MySQL.scalar('SELECT `firstname` FROM `users` WHERE `identifier` = ? LIMIT 1', [
  identifier
])

console.log(firstName)
```

**Aliases**

- `MySQL.Sync.fetchScalar`
- `exports.ghmattimysql.scalar`
- `exports.oxmysql.scalar_async`

## Callback

**Lua**

```lua
MySQL.scalar('SELECT `firstname` FROM `users` WHERE `identifier` = ? LIMIT 1', {
    identifier
}, function(firstName)
    print(firstName)
end)
```

**JS**

```js
MySQL.scalar('SELECT `firstname` FROM `users` WHERE `identifier` = ? LIMIT 1', [
  identifier
], (firstName) => {
  console.log(firstName)
})
```

**Aliases**

- `MySQL.Async.fetchScalar`
- `exports.ghmattimysql.scalar`
- `exports.oxmysql.scalar`
