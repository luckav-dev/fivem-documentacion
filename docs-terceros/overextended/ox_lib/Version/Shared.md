> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Version/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

## lib.checkDependency

Check if a resource is using a specified version or higher, allowing for compatibility checks or throwing errors.

```lua
lib.checkDependency(resource, version)
```

- resource: `string`
- version: `string`

**Lua**

```lua
if not lib.checkDependency('ox_lib', '1.5.0') then error() end
```

**JS**

```ts
import lib from '@overextended/ox_lib/shared'
// import { checkDependency } from '@overextended/ox_lib/shared'

if (!lib.checkDependency('ox_lib', '1.5.0')) error()
```
