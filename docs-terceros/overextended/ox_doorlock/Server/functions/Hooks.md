> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_doorlock/Server/functions/Hooks.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Hooks

Event hooks allow 3rd party resources to define new behaviour without modifying the doorlock system code directly.

## registerHook

```lua
exports.ox_doorlock:registerHook(eventName, function(payload) end, options)
```

- eventName: `string`
- payload: `table`
- options?: `table`
  - print?: `boolean`
    - Print to the console when triggering the event.
  - nameFilter?: `string`
    - The event will only trigger for specific doors

Return:

- hookId: `number`

### doorAuthorization

Triggered when opening/closing door.  
By returning `false`, you can override door authorization allowing to use your own logic.

- Payload: `table`
  - source: `number`
  - door: `DoorData`
  - lockpick: boolean
  - authorised: boolean

**Example**

Allow hotel room's owner open/close door

```lua
local hookId = exports.ox_doorlock:registerHook('doorAuthorization', function(payload)
    local hotel, apartment = payload.door.name:match("HotelDoor_(%w+)_([%d]+)")
    return IsAuthorized(payload.source, hotel, apartment)
end, {
    nameFilter = "HotelDoor_%w+_[%d]+"
})
```

## removeHooks

Removes a hook created by the invoking resource with the the specified id.  
If no id is specified then all hooks registered by the resource are removed.

```lua
exports.ox_doorlock:removeHooks(id)
```

- id?: `number`
