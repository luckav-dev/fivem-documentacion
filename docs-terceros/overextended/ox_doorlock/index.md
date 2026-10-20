> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_doorlock/index.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Ox Doorlock

**Enlaces del recurso:** [GitHub](https://github.com/overextended/ox_doorlock) · [Descargar](https://github.com/overextended/ox_doorlock/releases/latest/download/ox_doorlock.zip)

A door management resource that can be used standalone or alongside ox_core, qbx_core, and es_extended.

## Installation

> **Nota:** We **strongly** recommend referring to [Guides](../guides/index.md) for setting up Git, Node.js, and bun.

### 1. Install all resource dependencies.

- [oxmysql](../oxmysql/index.md)
- [ox_lib](../ox_lib/index.md)

### 2. Download a release or build the source code.

- Download the [latest release](https://github.com/overextended/ox_doorlock/releases/latest).

```bash
git clone https://github.com/overextended/ox_doorlock.git
cd ox_doorlock/web
bun i
bun run build
```

### 3. Install optional dependencies.

These resources aren't required but provide additional functionality.

- [ox_target](../ox_target/index.md)

## Opening the UI

If you have installed and started the resource, you can use `/doorlock` to open the UI.

- If the cursor is displayed but not the UI then you have not built it.
- You may not be authorised to use the command.

  - Enter `test_ace player.1 command.doorlock` in the server console (replace 1 with your server id).

## Convert doors

Door configuration files written for nui_doorlock can be automatically added to your MySQL database.

- Any files with the `.lua` extension placed in the `ox_doorlock/convert` directory will be read on resource start.
- If the directory doesn't exist, you can create it.
- Conversion cannot be guaranteed, especially if the config was not written for nui_doorlock.

## Adding new native audio

A guide can be found [here](https://forum.cfx.re/t/how-to-make-a-simplesound-using-native-audio/5156001) for adding new native audio.
