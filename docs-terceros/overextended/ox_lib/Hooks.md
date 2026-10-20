> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Hooks.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Hooks

Hooks allow resources to add custom logic to existing actions without modifying the original code. They work by running a set of callbacks (hook events) through a pipeline whenever a specific action occurs. Each hook can inspect the data and reject the action if needed.

After the pipeline completes, a post-hook event can run to handle the final result, such as logging or cleanup, without affecting the outcome.

This feature expands upon the idea of hooks introduced by [ox_inventory](../ox_inventory/Functions/Server/Hooks.md).

See our [internally registered hooks](https://github.com/overextended/ox_lib/blob/main/resource/state/server.lua) for examples.

# HookPipeline

Creates a hook pipeline for a specific event, which manages a collection of registered hooks and controls execution flow through filtering, rejection, and dispatching.

**Lua**

```lua
lib.hook:new(event, filter)
```

**TypeScript**

```ts
import { HookPipeline } from "@overextended/ox_lib/hooks";

new HookPipeline(event, filter)
```

- event: `string`
- filter?: `function(hook, payload): boolean`
  - Used to filter out registered hooks based on if they pass a predicate function.

**Returns:** `HookPipeline`

## Methods

### registerHook

A hook is a registered callback executed during a hook pipeline. It can inspect the payload, perform validation, and optionally reject the operation.

**Lua**

```lua
pipeline:registerHook(handler, options)
```

**TypeScript**

```ts
pipeline.registerHook(handler, options)
```

- handler: `function(payload: unknown): boolean`
- options?: `table`
  - Optional metadata to attach to the hook.

### remove

Removes hooks from the pipeline.

**Lua**

```lua
pipeline:remove(hookId)
```

**TypeScript**

```ts
pipeline.remove(hookId)
```

- hookId?: `string`
  - If defined, only the specified hook is removed - otherwise all hooks for the invoking resource are removed.

### dispatch

Executes each registered hook in order of registration, checking the payload against a provided filter using the hook options and executing the hook callback.

A hook may block execution by returning `false` from a registered handler.

If any hook rejects the execution, dispatch is cancelled and `result.ok` is set to `false`.

The returned object acts as a finalisation handle and emits results to registered handlers once closed.

**Lua**

```lua
local hook <close> = pipeline:dispatch(payload)
```

**TypeScript**

```ts
using hook = pipeline.dispatch(payload)
```

- payload: `unknown`

# EventHook

Allows resources to call [`pipeline.registerHook`](#registerhook) using exports.

**Lua**

```lua
lib.registerHook(eventName, handler, options)
```

**TypeScript**

```ts
import { registerHook } from "@overextended/ox_lib/hooks";

registerHook(eventName, handler, options)
```

- eventName: `string`
- handler?: `function(payload: unknown): boolean`
- options?: Optional metadata to attach to the hook.

## Methods

### on

Attaches an event handler to the hook which is executed after all hooks have been dispatched, allowing follow-up logic for successful or rejected events.

**Lua**

```lua
hook:on(handler)
```

**TypeScript**

```ts
hook.on(handler)
```

- handler: `function(ok: boolean, payload: unknown)`

### off

Detatches the currently registered post-hook event handler, if one exists.

**Lua**

```lua
hook:off()
```

**TypeScript**

```ts
hook.off()
```

### remove

Fully removes this hook from both the local event system and the external hook pipeline provided from the originating resource.

**Lua**

```lua
hook:remove()
```

**TypeScript**

```ts
hook.remove()
```

# Registered Hooks

These hook pipelines are registered and managed by ox_lib for other resources to interact with.

See [EventHook](Hooks.md#eventhook) for more information.

## ox_lib:setPlayerState

When using `sv_stateBagStrictMode` players cannot arbitrarily modify their own states, and changes will be rejected by default.

**Lua**

```lua
lib.registerHook('ox_lib:setPlayerState', predicate, { key: state })
```

**TypeScript**

```ts
import { registerHook } from "@overextended/ox_lib/hooks";

registerHook('ox_lib:setPlayerState', predicate, { key: state })
```

## ox_lib:setEntityState

When using `sv_stateBagStrictMode` players cannot arbitrarily modify entity states, and changes will be rejected by default.

**Lua**

```lua
lib.registerHook('ox_lib:setEntityState', predicate, { key: state })
```

**TypeScript**

```ts
import { registerHook } from "@overextended/ox_lib/hooks";

registerHook('ox_lib:setEntityState', predicate, { key: state })
```
