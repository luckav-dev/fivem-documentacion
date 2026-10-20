> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_addons/esx_optionalneeds.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_optionalneeds

[Github Link](https://github.com/esx-framework/ESX-Legacy-Addons/tree/main/%5Besx_addons%5D/esx_optionalneeds)

ESX Optional Needs, is a system that adds a new layer of realism to your server. What does it add? Alcoholism!

## Configuration

- `Config.TickTime`
    - type: `integer`
    - default: `100`
    - description: The time in ms between each tick of the system.
- `Config.UpdateClientTime`
    - type: `integer`
    - default: `5000`
    - description: The time in ms between each update of the client.

### Usage

```lua
TriggerEvent("esx_status:add", "drunk", 250000)
```
