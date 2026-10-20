> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Table/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

Adds additional functions alongside the standard table library.

## lib.table.contains

Checks if `table` contains the given `value`. Only intended for simple values and unnested tables.

```lua
lib.table.contains(tbl, value)
```

- tbl: `table`
- value: `any`

Return:

- isContained: `boolean`

## lib.table.matches

Compares if two values are equal, iterating over tables and matching both keys and values.

```lua
lib.table.matches(tableOne, tableTwo)
```

- tableOne: `table`
- tableTwo: `table`

Return:

- matches: `boolean`

## lib.table.deepclone

Recursively clones a table to ensure no table references remain.

```lua
lib.table.deepclone(tbl)
```

- tbl: `table`

Return:

- clonedTable: `table`

## lib.table.merge

Merges two tables together. Duplicate keys will be added together if they are numbers, otherwise `tableTwo`'s value will be used.

```lua
lib.table.merge(tableOne, tableTwo)
```

- tableOne: `table`
- tableTwo: `table`
- addDuplicateNumbers: `boolean`
  - Duplicate keys equal to numbers will be added together unless set to `false`.

Return:

- tableOne: `table`

## lib.table.freeze

Makes a table read-only, preventing further modification. Unfrozen tables stored within `table` are still mutable.

```lua
lib.table.freeze(tbl)
```

- tbl: `table`

Return:

- frozenTable: `table`

## lib.table.isFrozen

Returns true if `tbl` is set as read-only.

```lua
lib.table.isFrozen(tbl)
```

- tbl: `table`

Return:

- isFrozen: `boolean`
