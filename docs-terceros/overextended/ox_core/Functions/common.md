> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_core/Functions/common.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Common

## Ox.GetGroupPermissions

Returns the `OxGroupPermissions` object for the group

```lua
Ox.GetGroupPermissions(groupName)
```

**Parameters**

- groupName: `string`

**Returns**

- `OxGroupPermissions`

## Ox.GetTopVehicleStats

Returns an object containing the top vehicle stats, either overall or for a specific category (land, air, sea).

```lua
Ox.GetTopVehicleStats(category?)
```

**Parameters**

- category?: `string`

**Returns**

- `VehicleStats` | `{ [string]: VehicleStats }`

### VehicleStats

- `object`
  - acceleration: `number`
  - braking: `number`
  - handling: `number`
  - speed: `number`
  - traction: `number`

## Ox.GetVehicleData

Returns VehicleData for all vehicles, or optionally a specific model or array of models.

```lua
Ox.GetVehicleData(filter?)
```

**Parameters**

- filter?: `string` | `string[]`

**Returns**

- `{ [string]: VehicleData }` | `VehicleData`

### VehicleData

- `object`
  - class: `VehicleClasses`
  - doors: `number`
  - make: `string`
  - name: `string`
  - price: `number`
  - seats: `number`
  - type: `string`
  - weapons?: `true`

## Ox.GetVehicleNetworkType

Returns the netobj type of a vehicle model, which may differ from the vehicle type (e.g. blimp is networked as heli).

```lua
Ox.GetVehicleNetworkType(modelName)
```

**Parameters**

- modelName: `string`

**Returns**

- `string`
