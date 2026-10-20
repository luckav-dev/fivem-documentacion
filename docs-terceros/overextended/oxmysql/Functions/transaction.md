> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/oxmysql/Functions/transaction.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Transaction

A transaction executes multiple queries and commits them only if all succeed.  
If one fails, none of the queries are committed.

The return value is a boolean, which is the result of the transaction.

## Specific format

When using this format, you must pass an array containing sets of queries and parameters to the transaction method.  
In this case, your queries do not necessarily match and the values are unique to each query.

```lua
-- You might rename "values" as "parameters" for mysql-async compatibility.
local queries = {
    { query = 'INSERT INTO `test` (id) VALUES (?)', values = { 1 }},
    { query = 'INSERT INTO `test` (id, name) VALUES (?, ?)', values = { 2, 'bob' }},
}

-- You can also pass an array of arrays.
local queries = {
  { 'INSERT INTO `test` (id) VALUES (?)', { 1 } },
  { 'INSERT INTO `test` (id, name) VALUES (?, ?)', { 2, 'bob' } },
}
```

## Shared format

When using this format, you must pass an array containing queries and a set containing shared parameters to the transaction method.  
In this case, your queries do not necessarily match and the values are unique to each query.

```lua
-- You might rename "values" as "parameters" for mysql-async compatibility.
local queries = {
    'INSERT INTO `test` (id, name) VALUES (@someid, @somename)',
    'SET `name` = @newname IN `test` WHERE `id` = @someid'
}

local values = {
    someid = 2,
    somename = 'John Doe',
    newname = 'John Notdoe'
}
```

## Promise

**Lua**

```lua
local success = MySQL.transaction.await(queries, values --[[leave nil for specific format]])
print(success)
```

**JS**

```js
const success = await MySQL.transaction(queries, values /*leave nil for specific format*/)
console.log(success)
```

**Aliases**

- `MySQL.Sync.transaction`
- `exports.ghmattimysql.transaction`
- `exports.oxmysql.transaction_async`

## Callback

**Lua**

```lua
-- specific
MySQL.transaction(queries, values, function(success)
    print(success)
end)

-- shared
MySQL.transaction(queries, function(success)
    print(success)
end)
```

**JS**

```js
// specific
MySQL.transaction(queries, (success) => {
  console.log(success)
})

// shared
MySQL.transaction(queries, values, (success) => {
  console.log(success)
})
```

**Aliases**

- `MySQL.Async.transaction`
- `exports.ghmattimysql.transaction`
- `exports.oxmysql.transaction`

## Transaction Isolation Level

This can be set through the convar `mysql_transaction_isolation_level`, and is an integer ranging from `1-4`.  
The default value is 2.

| Convar Value | Result           |
| ------------ | ---------------- |
| 1            | Repeatable Read  |
| 2            | Read Committed   |
| 3            | Read Uncommitted |
| 4            | Serializable     |
