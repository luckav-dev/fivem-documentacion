> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_core/States.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Global States

> **Advertencia:** These global state bags are automatically assigned by ox_core and therefore should not be edited.

## groups

Contains an array of the names of all registered groups.

**Returns**

- `string[]`

## group.\<name\>

Contains information about the specified group.

**Returns**

- data: `object`
  - name: `string`
  - label: `string`
  - grades: `string[]`
  - type: `string`
  - hasAccount: `boolean`
  - accountRoles: `string[]`
  - principal: `string`

## \<name\>:count

Contains the number of players that have the specified group.

**Returns**

- `number`

## \<name\>:activeCount

Contains the number of players that have the specified group set as active.

**Returns**

- `number`

## status.\<name\>

Contains information about the specified status.

**Returns**

- data: `object`
  - name: `string`
  - default: `number`
  - onTick: `number`

## license.\<name\>

Contains information about the specified license.

**Returns**

- data: `object`
  - label: `string`

## accountRoles

Contains an array of the names of all registered account roles.

**Returns**

- `string[]`

## accountRole.\<name\>

Contains information about the specified account role.

**Returns**

- data: `object`
  - deposit: `0` | `1`
  - withdraw: `0` | `1`
  - addUser: `0` | `1`
  - removeUser: `0` | `1`
  - manageUser: `0` | `1`
  - transferOwnership: `0` | `1`
  - viewHistory: `0` | `1`
  - manageAccount: `0` | `1`
  - closeAccount: `0` | `1`
  - sendInvoice: `0` | `1`
  - payInvoice: `0` | `1`
