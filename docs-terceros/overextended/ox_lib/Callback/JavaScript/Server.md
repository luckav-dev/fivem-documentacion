> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Callback/JavaScript/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

## Trigger Client Callback

### triggerClientCallback

```ts
triggerClientCallback(eventName, playerId, ...args);
```

- eventName: `string`
- playerId: `number`
- ...args: `any`

## Register Server Callback

### onClientCallback

```ts
onClientCallback(eventName, cb);
```

- eventName: `string`
- cb: `function`(playerId: `number`, ...args: `any`)

## Usage Example

For this example to fully make sense take a look at the example on the [client](Client.md#usage-example) page for the callbacks.

```ts
import { onClientCallback, triggerClientCallback } from "@overextended/ox_lib/server";
```

```ts
onClientCallback("test:server", (playerId, ...args: [number, null, number, null, null, number]) => {
  console.log("onClientCallback", playerId, ...args);
  return {
    serverValue: 3000,
  };
});
```

```ts
setTimeout(async () => {
  const response = await triggerClientCallback<{ clientValue: string }>("test:client", 1, [
    1,
    null,
    3,
    null,
    null,
    6,
  ]);
  if (!response) return;
  console.log(response.clientValue);
  console.log("Response from client", response);
}, 100);
```
