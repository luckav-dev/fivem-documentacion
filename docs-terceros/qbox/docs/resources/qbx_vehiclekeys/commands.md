> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_vehiclekeys/commands.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# Slash Commands

*Slash Commands for Qbox's qbx_vehiclekeys. Learn about the available slash commands and their usage.*

Below is a list of commands available from qbx_vehiclekeys.
These commands are located at `qbx-vehiclekeys/server/commands.lua` for further inspection

--- 

## Give Keys

> **Nota:** This command is available to **all players** (no special permission group required).

Hand over the keys of your current vehicle to someone.  
If you omit the `id` parameter, the keys go to the closest player—or to every occupant of the vehicle if you’re all inside the same car.

Command: `/givekeys`

Parameters:

Parameters:
- ` ID of player `
    - optional
    - Type: ` integer `

Example:
```lua
/givekeys 42   -- give the keys to player ID 42
/givekeys      -- give the keys to the closest player (or everyone in the vehicle)
```

---

## Give permanent keys

> **Nota:** This command is restricted to players in the `group.admin` permission group.

Grant a player a permanent set of keys for the vehicle you’re currently inside (or last used).

Command: `/addkeys`

Parameters:

Parameters:
- ` ID of player `
    - optional
    - Type: ` integer `

Example:
```lua
/addkeys 23   -- give a key to player 23
/addkeys      -- give yourself a key for the current vehicle
```
---
