> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qbcore-resources/qb-minigames.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# qb-minigames

*How many times shall you fail!*

## Introduction

**`qb-minigames`** is a lightweight collection of skill-based minigames designed to add interactive challenges to your server's gameplay. Each minigame can be used as a standalone mechanic or embedded into scripts like robberies, hacking, crafting, or lockpicking to increase player engagement.

These minigames are implemented entirely in Lua with simple client exports, making them easy to integrate with existing `qb-core` resources or custom logic

> **Nota:** Credit: These minigames are ported from browser games originally found at [codingnepalweb.com](https://www.codingnepalweb.com/best-javascript-games-for-beginners) — full credit to the original creator(s)

## Features

* 🧠 **Quiz**: Multi-question trivia with time pressure
* 🔡 **Word Guess**: Hangman-style challenge with limited mistakes
* 🔀 **Word Scramble**: Unscramble the word before time runs out
* ⌨️ **Key Minigame**: Timed key presses with fault tracking
* 🛠️ **Lockpick**: Classic lockpicking challenge with limited tries
* 💻 **Hacking**: Pattern memory and input within a time limit
* 🎯 **Skillbar**: Reaction-based challenge with difficulty and custom keys
* 🔢 **Pinpad**: Input a correct code using a keypad UI

***

## Quiz

Presents a series of multiple-choice questions that the player must answer correctly within a time limit

* **questions**: `table`
  * A list of questions, each with:
    * **question**: `string`
    * **answer**: `string`
    * **options**: `table` — a list of possible answers
* **requiredCorrect**: `number`
* **timePerQuestion**: `number` (in seconds)

```lua
local success = exports['qb-minigames']:Quiz({
  { question = 'What color is a peach?', answer = 'pink', options = { 'red', 'yellow', 'orange', 'blue', 'pink' } },
  { question = 'What color is an apple?', answer = 'red', options = { 'red', 'yellow', 'orange', 'blue', 'pink' } },
  { question = 'What color is an orange?', answer = 'orange', options = { 'red', 'yellow', 'orange', 'blue', 'pink' } },
  { question = 'What color is a banana?', answer = 'yellow', options = { 'red', 'yellow', 'orange', 'blue', 'pink' } },
  { question = 'What color is a strawberry?', answer = 'red', options = { 'red', 'yellow', 'orange', 'blue', 'pink' } },
  { question = 'What color is a blueberry?', answer = 'blue', options = { 'red', 'yellow', 'orange', 'blue', 'pink' } },
}, 3, 15)

if success then
  print('success')
else
  print('fail')
end
```

***

## WordGuess

A classic hangman-style game where the player must guess the letters of a hidden word, with a limited number of wrong guesses allowed

* **word**: `string`
* **hint**: `string`
* **maxWrongGuesses**: `number`

```lua
local success = exports['qb-minigames']:WordGuess(
  'fivem',
  'the game modification you are playing on',
  5
)

if success then
  print('success')
else
  print('fail')
end
```

***

## WordScramble

Presents the player with a scrambled word and a hint. The player must unscramble it within a time limit.

* **word**: `string`
* **hint**: `string`
* **timeLimit**: `number` (in seconds)

```lua
local success = exports['qb-minigames']:WordScramble(
  'fivem',
  'the game modification you are playing on',
  30
)

if success then
  print('success')
else
  print('fail')
end
```

***

## KeyMinigame

Requires the player to rapidly press randomly shown keys a specified number of times. Tracks incorrect inputs and early exits.

* **requiredPresses**: `number`
  * Total number of correct key presses required.

```lua
local result = exports['qb-minigames']:KeyMinigame(10)

if result.quit then
  print('User quit game early')
  return
end

if result.faults > 3 then
  print('User got more than 3 keys wrong')
end
```

***

## Lockpick

A timed lockpicking minigame where the player must successfully pick a lock within a set number of tries.

* **attempts**: `number`
  * The number of lockpick attempts the player is allowed.

```lua
local success = exports['qb-minigames']:Lockpick(5)

if success then
  print('success')
else
  print('fail')
end
```

***

## Hacking

A memory-based hacking minigame where the player must solve a visual pattern challenge within a time limit.

* **gridSize**: `number`
  * The number of characters in the code block the player must memorize.
* **timeLimit**: `number`
  * Time (in seconds) to solve the hack.

```lua
local success = exports['qb-minigames']:Hacking(5, 30)

if success then
  print('success')
else
  print('fail')
end
```

***

## Skillbar

A reaction-based minigame where the player must press the correct keys at the right time. Supports custom difficulty and key sets.

* **difficulty**: `string` (optional)
  * Can be `"easy"`, `"medium"`, or `"hard"`. Defaults to `"easy"` if omitted.
* **keys**: `string` (optional)
  * A string of allowed key inputs (e.g. `"wasd"`). Defaults to `"1234"` if omitted.

```lua
luaCopyEdit-- Basic: uses default difficulty and keys ("easy", "1234")
local success = exports['qb-minigames']:Skillbar()

-- Medium difficulty with default keys
local success = exports['qb-minigames']:Skillbar("medium")

-- Easy difficulty with custom keys
local success = exports['qb-minigames']:Skillbar("easy", "wasdfgh")

if success then
  print('success')
else
  print('fail')
end
```

***

## Pinpad

A numeric keypad minigame where the player must input the correct pin code. The minigame uses keys `1–9` and tracks user actions.

* **pin**: `number`
  * The correct 4-digit code (must use digits 1–9).

```lua
luaCopyEditlocal result = exports['qb-minigames']:StartPinpad(1234)

if result.quit then
  print('User quit game early')
elseif result.correct then
  print('User passed game')
else
  print('User failed game')
end
```
