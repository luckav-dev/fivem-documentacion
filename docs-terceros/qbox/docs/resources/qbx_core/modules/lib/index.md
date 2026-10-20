> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_core/modules/lib/index.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# lib

*Documentation for the core library module in qbx_core. This module provides the global qbx table with utility functions for string manipulation, math operations, table handling, and vehicle-related functionality used across resources.*

Provides the `qbx` global table with various utility functions.

## Prerequisites

- Lua 5.4 - add `lua54 'yes'` to your fxmanifest.
- [ox_lib](https://coxdocs.dev/ox_lib) - add `@ox_lib/init.lua` to `shared_scripts` in your fxmanifest.

## Installation

Add `@qbx_core/modules/lib.lua` to `shared_scripts` in your fxmanifest. Make sure it's below the `@ox_lib/init.lua` script.
