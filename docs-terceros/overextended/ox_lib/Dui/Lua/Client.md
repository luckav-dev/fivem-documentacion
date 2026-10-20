> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Dui/Lua/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

Simple and centralised dui creation, supporting sending message, change url and deletion

## lib.dui:new

Constructs instance of Dui.

```lua
lib.dui:new(data)
```

- data: `table`
  - url: `string`
  - width: `number`
  - height: `number`
  - debug?: `boolean`

Returns:

- dui: `Dui`
  - url: `string`
  - duiObject: `number`
  - duiHandle: `string`
  - runtimeTxd: `number`
  - txdObject: `number`
  - dictName: `string`
  - txtName: `string`
  - setUrl: `function`(url: `string`)
  - sendMessage: `function`(data: `table`)
  - remove: `function`

### Usage Example

```lua
local dui = lib.dui:new({
	url = ("nui://%s/web/index.html"):format(cache.resource),
	width = 1920,
	height = 1080,
	debug = true
})

-- Change url
dui:setUrl("https://google.com")

-- Send a message
dui:sendMessage({
	action = "display",
	value = true
})

-- Destroy
dui:remove()
```
