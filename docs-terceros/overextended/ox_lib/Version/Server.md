> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Version/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

## lib.versionCheck

Compares the resource version to the latest published release on GitHub.  
[Utilises GitHub's release API](https://docs.github.com/en/rest/reference/releases)

```lua
lib.versionCheck(repository)
```

- repository: `string`

**Lua**

```lua
lib.versionCheck('overextended/ox_lib')
```

**JS**

```ts
import lib from '@overextended/ox_lib/server'

lib.versionCheck('overextended/ox_lib')
```
