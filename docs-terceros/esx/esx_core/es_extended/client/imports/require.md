> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/client/imports/require.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# Require

Loads the given module. The function starts by indexing the loaded table to determine whether `modname` is already loaded. If it is, then `require` returns the value stored at `loaded[modname]`.
    - Module names are the path to a file relative to the resource.
    - The module name must point to a `.lua` file.
    - Use `.` to separate directories in a path.
    - Modules can be loaded from external resources using `@resource.modname`.

## Examples

```lua
require '@resource.client.modname'
```

> **Advertencia:** Client modules must be defined in the `file` section of the resource manifest.
> ```lua
>     file 'modname.lua'
>     -- or
>     files {
>     'modname.lua'
>     }
> ```

> Credit to [Overextended](https://overextended.dev/ox_lib/Modules/Require/Shared) for the documentation.
