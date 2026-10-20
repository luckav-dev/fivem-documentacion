> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_target/index.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Ox Target

**Enlaces del recurso:** [GitHub](https://github.com/overextended/ox_target) · [Descargar](https://github.com/overextended/ox_target/releases/latest/download/ox_target.zip)

A performant and flexible standalone targeting resource or "third-eye", with additional functionality for ox_inventory, ox_core, qbx_core, and es_extended.

## Installation

> **Nota:** We **strongly** recommend referring to [Guides](../guides/index.md) for setting up Git, Node.js, and bun.

### 1. Install all resource dependencies

- [ox_lib](../ox_lib/index.md)

### 2. Download a release or clone the source code.

- Download the [latest release](https://github.com/overextended/ox_target/releases/latest).

```bash
git clone https://github.com/overextended/ox_target.git
```

### 3. Config

Resource configuration is handled using [convars](https://docs.fivem.net/docs/scripting-reference/convars/).

```bash
# Toggle targeting when pressing the hotkey, instead of holding it down.
setr ox_target:toggleHotkey 0

# Change the key to enable targeting (https://docs.fivem.net/docs/game-references/input-mapper-parameter-ids/keyboard)
setr ox_target:defaultHotkey LMENU

# Draw a sprite (circle) at the centroid of a zone.
setr ox_target:drawSprite 1

# Enable built-in targeting options, e.g. toggling vehicle doors.
setr ox_target:defaults 1

# Enable debugging / testing options, entity outlines, and a raycast indicator.
setr ox_target:debug 0

# Enable / Disable leftclick to select options
setr ox_target:leftClick 1
```

## Supported Frameworks

These aren't necessary to run ox_target, but they will add additional features.

- [ox_core](https://github.com/overextended/ox_core)
- [esx](https://github.com/esx-framework/esx-legacy)
- [qbx_core](https://github.com/Qbox-project/qbx_core)
