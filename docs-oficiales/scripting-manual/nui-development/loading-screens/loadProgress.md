# loadProgress

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/loadProgress/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered when the loading progress percentage is updated.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'loadProgress',
    loadFraction: number,
}
```

- **eventName**: The event name.
- **loadFraction**: The total loading percentage as a fraction from 0 to 1 (inclusive).

## Examples

```html
<!-- loading screen bar -->
<progress id="loading-bar" value="0" max="1"></progress>

<script type="text/javascript">
window.addEventListener('message', (event) => {
    // ensure that we are handling the loadProgress event
    if (event.data.eventName !== 'loadProgress') return;

    // use the event's data to fill up the loading bar
    document.getElementById('loading-bar').value = event.data.loadFraction;
});
</script>
```
