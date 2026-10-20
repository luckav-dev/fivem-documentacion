# clearTick

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/clearTick/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Removes a tick timer, stopping it from running. This is to be used in combination with a [setTick][setTick] id.

## Syntax

```ts
clearTick(id);
```

### Required arguments

- **id**: The timer to be cleared.

## Examples

This example creates a tick timer that prints a string to the console. We then clear it 5000ms after the server/client started.

```ts
const timer = setTick(() => {
  console.log("I'm running.");
});

setTimeout(() => {
  clearTick(timer);
  console.log('I stopped running.');
}, 5000);
```

[setTick]: setTick.md
