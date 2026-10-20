> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_core/Events/client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client Events

> **Advertencia:** These events are triggered by ox_core when an action occurs. You should not trigger them from
> other scripts.

## ox:playerLoaded

When a character is loaded

**Lua**

```lua copy
AddEventHandler('ox:playerLoaded', function(playerId, isNew)
    print(playerId, isNew)
end)
```

**JS**

```ts copy
on('ox:playerLoaded', (playerId: number, isNew: boolean) => {
  console.log(playerId, isNew);
});
```

- playerId: `number`
- isNew?: `boolean`

## ox:statusTick

On each status tick, returning changed statuses

**Lua**

```lua copy
AddEventHandler('ox:statusTick', function(statuses)
    print(json.encode(statuses))
end)
```
* statuses: `table<string, number>`

**JS**

```ts copy
on('ox:statusTick', (statuses: Record<string, number>) => {
  console.log(statuses);
});
```
* statuses: `Record<string, number>`

## ox:playerDeath

When the character has died

**Lua**

```lua copy
AddEventHandler('ox:playerDeath', function() end)
```

**JS**

```ts copy
on('ox:playerDeath', () => {});
```

## ox:playerRevived

When the character is revived

**Lua**

```lua copy
AddEventHandler('ox:playerRevived', function() end)
```

**JS**

```ts copy
on('ox:playerRevived', () => {});
```

---

# Net Events

## ox:setGroup

When the character is added or removed from a group

**Lua**

```lua copy
RegisterNetEvent('ox:setGroup', function(groupName, grade)
    print(groupName, grade)
end)
```

**JS**

```ts copy
onNet('ox:setGroup', (groupName: string, grade: number) => {
  console.log(groupName, grade);
});
```

- groupName: `string`
- grade?: `number`

## ox:licenseAdded

When the character got a new license

**Lua**

```lua copy
RegisterNetEvent('ox:licenseAdded', function(licenseName)
    print(licenseName)
end)
```

**JS**

```ts copy
onNet('ox:licenseAdded', (licenseName: string) => {
  console.log(licenseName);
});
```

- licenseName: `string`

## ox:licenseRemoved

When a character's license is removed.

**Lua**

```lua copy
RegisterNetEvent('ox:licenseRemoved', function(licenseName)
    print(licenseName)
end)
```

**JS**

```ts copy
onNet('ox:licenseRemoved', (licenseName: string) => {
  console.log(licenseName);
});
```

- licenseName: `string`

## ox:startCharacterSelect

When the player has spawned.

**Lua**

```lua copy
RegisterNetEvent('ox:startCharacterSelect', function(userId, characters)
    print(userId, characters)
end)
```
* userId: `number`
* characters: `Character[]`

Character
* `table`
    * charId: `number`
    * stateId: `number`
    * firstname: `string`
    * lastname: `string`
    * gender: `string`
    * x?: `number`
    * y?: `number`
    * z?: `number`
    * lastPlayed?: `string`
      * Date format `%d/%m/%Y (dd/mm/yyyy)`

**JS**

```ts copy
onNet('ox:startCharacterSelect', (userId: number, characters: Character[]) => {
  console.log(userId, characters);
});
```

* userId: `number`
* characters: `Character[]`

Character
* `object`
    * charId: `number`
    * stateId: `number`
    * firstname: `string`
    * lastname: `string`
    * gender: `string`
    * x?: `number`
    * y?: `number`
    * z?: `number`
    * lastPlayed?: `string`
      * Date format `%d/%m/%Y (dd/mm/yyyy)`

## ox:setActiveCharacter

When the player has chosen their character.

**Lua**

```lua copy
RegisterNetEvent('ox:setActiveCharacter', function(character, groups)
    print(character, groups)
end)
```
* character: `Character`
* groups: `table<string, number>`

Character
* `table`
  * charId: `number`
  * stateId: `number`
  * firstname: `string`
  * lastname: `string`
  * gender: `string`
  * x?: `number`
  * y?: `number`
  * z?: `number`
  * lastPlayed?: `string`
    * Date format `%d/%m/%Y (dd/mm/yyyy)`
  * health?: `number`
  * armour?: `number`
  * isNew?: `boolean`

**JS**

```ts copy
onNet('ox:setActiveCharacter', (character: Character, groups: Record<string, number>) => {
  console.log(character, groups);
});
```
* character: `Character`
* groups: `Record<string, number>`

Character
* `object`
  * charId: `number`
  * stateId: `number`
  * firstname: `string`
  * lastname: `string`
  * gender: `string`
  * x?: `number`
  * y?: `number`
  * z?: `number`
  * lastPlayed?: `string`
    * Date format `%d/%m/%Y (dd/mm/yyyy)`
  * health?: `number`
  * armour?: `number`
  * isNew?: `boolean`
