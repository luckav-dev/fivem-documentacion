> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Scaleform/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

## lib.scaleform:new

Constructs a new instance of the scaleform class.

```lua
lib.scaleform:new(data)
```

- data: `table | string`
  - name: `string`
  - fullScreen?: `boolean`
  - x?: `number`
  - y?: `number`
  - width?: `number`
  - height?: `number`
  - renderTarget?: `table`
    - name: `string`
    - model: `string | number`

Returns:

- scaleform: `Scaleform`
  - scaleform: `number`
  - draw: `boolean`
  - target: `number`
  - targetName: `string`
  - sfHandle?: `number`
  - fullScreen: `boolean`

  Methods:
  - callMethod: `function`(name: `string`, args: `(number | string | boolean)[]`, returnValue?: `string`)
  - setFullScreen: `function`(isFullscreen: `boolean`)
  - setProperties: `function`(x: `number`, y: `number`, width: `number`, height: `number`)
  - setRenderTarget: `function`(name: `string`, model: `string | number`)
  - isDrawing: `function`
  - draw: `function`
  - startDrawing: `function`
  - stopDrawing: `function`
  - dispose: `function`

### Usage Example

```lua
local scaleform = lib.scaleform:new({
  name = 'scaleform',
  fullScreen = boolean,
  x = 1.0,
  y = 1.0,
  width = 2.0,
  height = 2.0,
  renderTarget = {
    name = 'target',
    model = `model_name`
  }
})

-- Call a Scaleform Method
scaleform:callMethod('method', { 1, 2, 3 })

-- Set Fullscreen Scaleform
scaleform:setFullScreen(false)

-- Set Scaleform Properties (x, y, width, height)
scaleform:setProperties(1.0, 1.0, 2.0, 2.0)

-- Set Scaleform Render Target
scaleform:setRenderTarget('target', `model_name`)

-- Get Drawing State
local state = scaleform:isDrawing()

-- Draw
scaleform:draw()

-- Start Drawing
scaleform:startDrawing()

-- Stop Drawing
scaleform:stopDrawing()

-- Dispose of Scaleform
scaleform:dispose()
```
