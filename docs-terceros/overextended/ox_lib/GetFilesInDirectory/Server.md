> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/GetFilesInDirectory/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

## lib.getFilesInDirectory

Gets a list of all files in a specified resource directory, along with the file count

```lua
lib.getFilesInDirectory(path, pattern)
```

- path: `string`
  - The relative or absolute path to the directory where files should be listed.
- pattern: `string`
  - Pattern to check for when searching for files.

Returns:

- files: `string[]`
- fileCount: `number`
