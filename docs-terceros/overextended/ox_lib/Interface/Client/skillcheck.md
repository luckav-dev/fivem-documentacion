> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Interface/Client/skillcheck.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Skill Check

## lib.skillCheck

Runs a skill check with the defined difficulty.

**Lua**

```lua
lib.skillCheck(difficulty, inputs)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client';

lib.skillCheck(difficulty, inputs);
```

- difficulty: `'easy'` or `'medium'` or `'hard'` or `table`
  - Preset difficulties:
    - 'easy' - `{ areaSize: 50, speedMultiplier: 1 }`
    - 'medium' - `{ areaSize: 40, speedMultiplier: 1.5 }`
    - 'hard' - `{ areaSize: 25, speedMultiplier: 1.75 }`
  - Custom difficulties can be set by sending an object instead of one of the preset strings above
    - areaSize: `number`
      - Size of the success area in degrees
    - speedMultiplier: `number`
      - Multiplier for the speed of the indicator
- inputs?: `string[]`
  - A random key will be picked from the inputs table for each skill check
  - If no inputs are defined the key is defaulted to `e`

## lib.skillCheckActive

Returns true if a skill check is currently active.

**Lua**

```lua
lib.skillCheckActive()
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.skillCheckActive()
```

## lib.cancelSkillCheck

Cancels the currently ongoing skill check.

**Lua**

```lua
lib.cancelSkillCheck()
```

**JS**

```ts
import lib from '@overextended/ox_lib/client'

lib.cancelSkillCheck()
```

## Usage Example

**Lua**

```lua
local success = lib.skillCheck({'easy', 'easy', {areaSize = 60, speedMultiplier = 2}, 'hard'}, {'w', 'a', 's', 'd'})
```

**JS**

```ts
import lib from '@overextended/ox_lib/client';

const success = await lib.skillCheck(
  ['easy', 'easy', { areaSize: 60, speedMultiplier: 2 }, 'hard'],
  ['w', 'a', 's', 'd']
);
```

![skillcheck_example](../../../imagenes/externas/i.imgur.com/rgfkn0S-075919.png)
