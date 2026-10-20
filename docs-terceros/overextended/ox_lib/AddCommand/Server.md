> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/AddCommand/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

Registers commands and simplifies argument validation, permissions, and chat suggestions.

```lua
lib.addCommand(commandName, properties, cb)
```

- commandName: `string` or `string[]`
- properties: `table` or `false`
  - help?: `string`
  - restricted?: `boolean` or `string` or `string[]`
  - params?: `table[]`
    - name: `string`
    - help?: `string`
    - type?: `'number'` or `'playerId'` or `'string'` or `'longString'`
    - optional?: `boolean`

```lua
lib.addCommand('giveitem', {
    help = 'Gives an item to a player',
    params = {
        {
            name = 'target',
            type = 'playerId',
            help = 'Target player\'s server id',
        },
        {
            name = 'item',
            type = 'string',
            help = 'Name of the item to give',
        },
        {
            name = 'count',
            type = 'number',
            help = 'Amount of the item to give, or blank to give 1',
            optional = true,
        },
        {
            name = 'metatype',
            help = 'Sets the item\'s "metadata.type"',
            optional = true,
        },
    },
    restricted = 'group.admin'
}, function(source, args, raw)
    local item = Items(args.item)

    if item then
        Inventory.AddItem(args.target, item.name, args.count or 1, args.metatype)
    end
end)
```
