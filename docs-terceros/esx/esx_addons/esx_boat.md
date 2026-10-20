> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_addons/esx_boat.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_boat

[Github Link](https://github.com/esx-framework/ESX-Legacy-Addons/tree/main/%5Besx_addons%5D/esx_boat)

This resource for ESX adds boat shops and boat garages around San Andreas, the island has been populated with boat garages, and comes defaulted with one boat shop.

## Configuration

- `Config.LicenseEnable`
    - type:`boolean`
    - default:`true`
    - description: Require players to have a boating license to purchase boats.
- `Config.LicensePrice`
    - type:`int`
    - default:`5000`
    - description: The price of the boating license.
- `Config.MarkerType`
    - type:`string`
    - default:`1`
    - description: The marker type for the boat shop.
- `Config.DrawDistance`
    - type:`float`
    - default:`10.0`
    - description: The draw distance for the boat shop marker.
- `Config.Marker` & `Config.StoreMarker`
    - type:`table`
    - description: The marker for the boat shop.
    - `x`
        - type:`float`
        - description: The x position of the marker.
    - `y`
        - type:`float`
        - description: The y position of the marker.
    - `z`
        - type:`float`
        - description: The z position of the marker.
    - `r`
        - type:`float`
        - description: The red value of the marker.
    - `g`
        - type:`float`
        - description: The green value of the marker.
    - `b`
        - type:`float`
        - description: The blue value of the marker.

## Exports

### getGarages

returns `Config.Zones.Garages`

```lua
local garages = exports['esx_boat']:getGarages()
```
