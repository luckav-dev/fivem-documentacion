> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Print/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

Prints to console conditionally based on convars set.
Different level prints are colored and labeled.
Resource name is always included.

## lib.print

```lua
lib.print.error(...)
lib.print.warn(...)
lib.print.info(...)
lib.print.verbose(...)
lib.print.debug(...)
```

- vararg: `any`
  - What to print in console. Converts tables into a pretty-print format.

### Example

```lua
lib.print.warn("query latency high: ", latency)
```

### Levels

- Error
  - Indicates a failure in the system.

- Warn
  - Warns of an unexpected condition, or a state which is likely to cause an error in the future.

- Info
  - Information about high-level, successful operations.

- Verbose
  - More detailed information containing intermediate steps of high-level, operations

- Debug - Used by developers to understand the system and may contain detailed trace information.
  Should generally not be turned on when not debugging.

### Config

Use the following convars to set your print level. Prints less severe than the current level will not be executed.
For example, a level of info will print error, warn, and info, but not verbose nor debug. Defaults to info if not set.
Resource specific print levels override the global convar.

```bash
set ox:printlevel "info"
set ox:printlevel:ox_inventory "warn"
set ox:printlevel:<resourceName> "<level>"
```
