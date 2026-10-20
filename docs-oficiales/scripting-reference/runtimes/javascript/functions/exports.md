# Exports

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/javascript/functions/exports/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

Use this to export functions so they can be called from other resources.\
Read more on [exports](../../../../scripting-manual/runtimes/javascript.md#using-exports)

## Signature

```ts
function exports(exportedName: string, fn: Function) => void
```

### Required arguments

- **exportedName**: The function name you want to export.
- **fn**: The function to execute when the export is called.

## Examples

```ts
exports("printSomething", () => {
  console.log("Something");
});
```

```ts
exports("dropPlayer", (src: string, reason: string) => {
  DropPlayer(src, reason);
});

// OR

exports("dropPlayer", DropPlayer);
```
