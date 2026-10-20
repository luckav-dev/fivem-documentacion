> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/WaitFor/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

## lib.waitFor

Calls a function repeatedly until it receives a non-nil value, or it times out.  
The function result is then returned.

```lua
lib.waitFor(cb, errMessage, timeout)
```

- cb: `function`
  - A function to call each frame.
- errMessage?: `string`
  - The error message to display if the function times out.
- timeout?: `number | false`
  - The duration to run the function for, defaulting to 1000ms, unless set to `false`.

```lua
local value --[['abc']] = lib.waitFor(function()
    if math.random(0, 1) == 1 then return 'abc' end
end)
```
