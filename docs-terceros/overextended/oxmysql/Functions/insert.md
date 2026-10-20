> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/oxmysql/Functions/insert.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# insert

Inserts a new entry into the database and returns the insert id for the row, if valid.

## Promise

**Lua**

```lua
local id = MySQL.insert.await('INSERT INTO `users` (identifier, firstname, lastname) VALUES (?, ?, ?)', {
    identifier, firstName, lastName
})

print(id)
```

**JS**

```js
const id = await MySQL.insert('INSERT INTO `users` (identifier, firstname, lastname) VALUES (?, ?, ?)', [
  identifier, firstName, lastName
])

console.log(id)
```

**Aliases**

- `MySQL.Sync.insert`
- `exports.ghmattimysql.executeSync`
- `exports.oxmysql.insert_async`

## Callback

**Lua**

```lua
MySQL.insert('INSERT INTO `users` (identifier, firstname, lastname) VALUES (?, ?, ?)', {
    identifier, firstName, lastName
}, function(id)
    print(id)
end)
```

**JS**

```js
MySQL.insert('INSERT INTO `users` (identifier, firstname, lastname) VALUES (?, ?, ?)', [
  identifier, firstName, lastName
], (id) => {
  console.log(id)
})
```

**Aliases**

- `MySQL.Async.insert`
- `exports.ghmattimysql.execute`
- `exports.oxmysql.insert`
