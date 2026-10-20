> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/oxmysql/Functions/query.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Query

When selecting data, returns all matching rows and columns; otherwise, returns data like insertId, affectedRows, etc.

## Promise

**Lua**

```lua
local response = MySQL.query.await('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ?', {
    identifier
})

if response then
    for i = 1, #response do
        local row = response[i]
        print(row.firstname, row.lastname)
    end
end
```

**JS**

```js
const response = await MySQL.query('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ?', [
  identifier
])

if (response) {
  response.forEach((row) => {
    console.log(row.identifier, row.firstname, row.lastname)
  })
}
```

**Aliases**

- `MySQL.Sync.fetchAll`
- `exports.ghmattimysql.execute`
- `exports.oxmysql.query_async`

## Callback

**Lua**

```lua
MySQL.query('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ?', {
    identifier
}, function(response)
    if response then
        for i = 1, #response do
            local row = response[i]
            print(row.firstname, row.lastname)
        end
    end
end)
```

**JS**

```js
MySQL.query('SELECT `firstname`, `lastname` FROM `users` WHERE `identifier` = ?', [
  identifier
], (response) => {
  if (response) {
    response.forEach((row) => {
      console.log(row.firstname, row.lastname)
    })
  }
})
```

**Aliases**

- `MySQL.Async.fetchAll`
- `exports.ghmattimysql.execute`
- `exports.oxmysql.query`
