# setTick

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/setTick/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

This allows you to create a timer that ticks every game frame / server tick. It can be used client-side or server-side acting like a loop that runs forever unless [cleared][clearTick].

## Syntax

```ts
setTick(() => {});
```

## Examples

```ts
setTick(() => {
    console.log("I'm running every frame/tick!");
});
```

[clearTick]: clearTick.md
