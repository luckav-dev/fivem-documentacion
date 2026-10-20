> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/String/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

## lib.string

Extends the standard Lua string table with extra functions.

```
string = lib.string
```

### string.random

Outputs a random string based on a given pattern.

```lua
string.random(pattern, length)
```

- pattern: `string`
- `1` will output a random number from 0-9.
- `A` will output a random letter from A-Z.
- `a` will output a random letter from a-z.
- `.` will output a random letter or number.
- `^` will output the following character literally.
- Any other character will output said character.
- length?: `number`
  - Sets the length of the returned string, either padding it or omitting characters.

Return:

- string: `string`
