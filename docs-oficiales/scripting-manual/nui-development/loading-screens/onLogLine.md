# onLogLine

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/loading-screens/onLogLine/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Triggered to log the initialization of resources.

## Event Data

This is the `data` provided to the message event:

```ts
interface EventData {
    eventName: 'onLogLine',
    message: string,
}
```

- **eventName**: The event name.
- **message**: The log message.

## Examples

```html
<!-- loading screen bar -->
<p id="log"></p>

<script type="text/javascript">
window.addEventListener('message', (event) => {
    // ensure that we are handling the onLogLine event
    if (event.data.eventName !== 'onLogLine') return;

    // use the event's data to fill up the log line
    document.getElementById('log').innerText = event.data.message;
});
</script>
```
