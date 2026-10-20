> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Callback/JavaScript/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

## Trigger Server Callback

### triggerServerCallback

```ts
triggerServerCallback(eventName, delay, ...args);
```

- eventName: `string`
- delay: `number` or `null`
  - Amount of time until this callback can be triggered again
- ..args: `any`

## Register Client Callback

### onServerCallback

```ts
onServerCallback(eventName, cb);
```

- eventName: `string`
- cb: `function`(...args: `any`)

## Usage Example

For this example to fully make sense take a look at the example on the [server](Server.md#usage-example) page for the callbacks.

```ts
import { onServerCallback, triggerServerCallback } from "@overextended/ox_lib/client";
```

```ts
onServerCallback("test:client", (...args: [number, number, string]) => {
  console.log(args);
  return {
    clientValue: "Value from the client",
  };
});
```

```ts
setTimeout(async () => {
  const args = [1, null, 3, null, null, 6];
  const response = await triggerServerCallback<{ serverValue: number }>("test:server", 1, args);
  if (!response) return;
  console.log("Response from server", response);
}, 100);
```
