# onClientGameTypeStart

> Fuente original: https://docs.fivem.net/docs/resources/mapmanager/events/onClientGameTypeStart/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

## Parameters

```
string resourceName
```

- **resourceName**: The name of the resource/gametype that started.

## Examples

### JavaScript Example:

```js
on('onClientGameTypeStart', (name) => {
   console.log('Map started: ', name);
});
```
