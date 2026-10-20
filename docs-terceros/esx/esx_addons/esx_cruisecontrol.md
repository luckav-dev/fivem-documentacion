> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_addons/esx_cruisecontrol.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_cruisecontrol

[Github Link](https://github.com/esx-framework/ESX-Legacy-Addons/tree/main/%5Besx_addons%5D/esx_cruisecontrol)

ESX Cruisecontrol includes a cruisecontrol and seatbelt system for safe and relaxing driving

## Configuration

- `Config.HudResource`
    - type: `string`
    - default: `esx_hud`
    - description: The resource name of the HUD resource that should be used to display the cruisecontrol and seatbelt status
- `Config.Cruise`
    - type: `table`
    - description: Configuration for the cruisecontrol
    - options:
        - `Enable`
            - type: `boolean`
            - default: `true`
            - description: Enable or disable the cruisecontrol
        - `Key`
            - type: `string`
            - default: `CAPITAL`
            - description: The key to toggle the cruisecontrol
        - `Export`
            - type: `function`
            - default:
                ```lua
                 Export = function(state)
                    exports[Config.HudResource]:SetCruiseControl(state)
                end
                ```
            - description: Export to set the cruisecontrol status in the HUD
- `Config.Seatbelt`
    - type: `table`
    - description: Configuration for the seatbelt
    - options:
        - `Enable`
            - type: `boolean`
            - default: `true`
            - description: Enable or disable the seatbelt
        - `Key`
            - type: `string`
            - default: `B`
            - description: The key to toggle the seatbelt
        - `EjectCheckSpeed`
            - type: `number`
            - default: `45.0`
            - description: The speed at which the player should be ejected from the vehicle when not wearing a seatbelt
        - `RagollTime`
            - type: `number`
            - default: `1`
            - description: The time in milliseconds the player should be in ragdoll when ejected from the vehicle
        - `Export`
            - type: `function`
            - default:
                ```lua
                Export = function(state)
                  exports[Config.HudResource]:SeatbeltState(state)
                end
                ```
            - description: Export to set the seatbelt status in the HUD
