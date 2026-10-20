> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_core/index.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Ox Core

**Enlaces del recurso:** [GitHub](https://github.com/overextended/ox_core) · [Descargar](https://github.com/overextended/ox_core/releases/latest/download/ox_core.zip) · [npm](https://www.npmjs.com/package/@overextended/ox_core)

A modern FiveM framework, designed to properly support features like OneSync, statebags, and server-side entities.

## txAdmin recipe

If you're looking to quickly install and setup ox_core, try using [our recipe](https://github.com/overextended/txAdminRecipe).

## Installation

> **Nota:** We **strongly** recommend referring to [Guides](../guides/index.md) to setup necessary development tools.

### 1. Install all resource dependencies.

- [oxmysql](../oxmysql/index.md)
- [ox_lib](../ox_lib/index.md)

### 2. Download a release or build the source code.

- Download the [latest release](https://github.com/overextended/ox_core/releases/latest).
- Setup [Git](../guides/git.md), [Node.js](../guides/nodejs.md), and [bun](../guides/bun.md).
- Download and setup [MariaDB 11.4+](https://mariadb.com/downloads/community/community-server/).
- Run the following commands in your CLI (e.g. Terminal, Command Prompt).

```bash
git clone https://github.com/overextended/ox_core.git
cd ox_core
bun i
bun run build
```

### 3. Install optional dependencies.

These resources aren't strictly required, but they are strongly recommended.

- [ox_inventory](../ox_inventory/index.md)
- [npwd](https://github.com/project-error/npwd)
- [illenium-appearance](https://github.com/iLLeniumStudios/illenium-appearance/archive/refs/heads/main.zip)

## Using ox_core in your resources

### Lua

You can import ox_core definitions by loading `@ox_core/lib/init.lua` into your resource.

**fxmanifest.lua**

This can be a client_script or server_script, if preferred.
```lua
shared_script '@ox_core/lib/init.lua'
```

**require**

If you prefer, you can use our [require](../ox_lib/Require/Shared.md) function from [ox_lib](../ox_lib/index.md).
```lua
local Ox = require '@ox_core.lib.init'
```

### JavaScript

To use ox_core with your JavaScript resources you'll need to use our npm package, providing full support for TypeScript and Intellisense.

[npm](https://www.npmjs.com/package/@overextended/ox_core)

To get started, try our [fivem-typescript-boilerplate](https://github.com/overextended/fivem-typescript-boilerplate) and install the ox_core package.

```bash
bun i @overextended/ox_core
```

## Config

Resource configuration is handled using [convars](https://docs.fivem.net/docs/scripting-reference/convars/).

### Replicated

These convars should use the `setr` command to be read by clients.

- `ox:debug`
  - Default: `false`
  - Enables debug messages and commands. Also allows players to have the same identifiers. Enabled by default when using `bun watch`.
- `ox:characterSlots`
  - Default: `1`
  - Sets the number of character slots available for character selection resources (e.g. ox_charselect).
- `ox:plateFormat`
  - Default: `"........"`
  - See [SET_DEFAULT_VEHICLE_NUMBER_PLATE_TEXT_PATTERN](https://docs.fivem.net/natives/?_0x79780FD2).
- `ox:deathSystem`
  - Default: `true`
  - Enables the built-in death and respawn system. When disabled the `isDead` player state will still be set to `true` and the `ox:playerDeath` event will be triggered.
- `ox:hospitalBlips`
  - Default: `true`
  - Enables the hospital blips used when reviving with the default deathSystem.
- `ox:characterSelect`
  - Default: `true`
  - Enables built-in character registration, and uses that character when joining.
- `ox:spawnLocation`
  - Default: `[-258.211, -293.077, 21.6132, 206.0]`
  - Sets the default spawn location for newly created characters.
- `ox:defaultVehicleStore`
  - Default: `'impound'`
  - On resource start any vehicles that were previously spawned will be stored here. An empty string will not update the database.
