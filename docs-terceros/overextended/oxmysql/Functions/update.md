> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/oxmysql/Functions/update.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Update

Returns the number of rows affected by the query.

## Promise

**Lua**

```lua
local affectedRows = MySQL.update.await('UPDATE users SET firstname = ? WHERE identifier = ?', {
    newName, identifier
})

print(affectedRows)
```

**JS**

```js
const affectedRows = await MySQL.update('UPDATE users SET firstname = ? WHERE identifier = ?', [
  newName, identifier
])

console.log(affectedRows)
```

**Aliases**

- `MySQL.Sync.execute`
- `exports.ghmattimysql.executeSync`
- `exports.oxmysql.update_async`

## Callback

**Lua**

```lua
MySQL.update('UPDATE users SET firstname = ? WHERE identifier = ?', {
    newName, identifier
}, function(affectedRows)
    print(affectedRows)
end)
```

**JS**

```js
MySQL.update('UPDATE users SET firstname = ? WHERE identifier = ?', [
  newName, identifier
], (affectedRows) => {
  console.log(affectedRows)
})
```

**Aliases**

- `MySQL.Async.execute`
- `exports.ghmattimysql.execute`
- `exports.oxmysql.update`
