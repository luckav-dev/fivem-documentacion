# Client Events

> Fuente original: https://docs.fivem.net/docs/scripting-reference/events/client-events/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

**A list of client side events you can use in your scripts.**

## Core events

These events are part of FiveM and do not require any resource.

### CEventName

```ts
CEventName(entities: number[], eventEntity: number, data: any[]): void
```

An event that is triggered when the game triggers an internal network event.
CEventName can be any event name that GTA 5 throws, e.g.: "CEventShockingCarCrash".
see: [https://docs.fivem.net/docs/game-references/game-events/](../../../game-references/game-events.md) for a list of known events.

**Parámetros**

- `entities: number[]`: All entities receiving/emitting the event, can be empty.
- `eventEntity: number`: Entity the event is related to.
- `data: any[]`: Extra event data.

### entityDamaged

```ts
entityDamaged(victim: number, culprit: number, weapon: number, baseDamage: number): void
```

An event that is triggered when an entity is *locally* damaged.

**Parámetros**

- `victim: number`: The entity which is damaged, or 0 if none.
- `culprit: number`: The damaging entity, or 0 if none.
- `weapon: number`: The hash of the weapon inflicting damage.
- `baseDamage: number`: The base amount of damage inflicted, discounting any modifiers.

### gameEventTriggered

```ts
gameEventTriggered(name: string, data: number[]): void
```

An event that is triggered when the game triggers an internal network event.

**Parámetros**

- `name: string`: The name of the triggered event.
- `data: number[]`: The type-specific event data.

### mumbleConnected

```ts
mumbleConnected(address: string, reconnecting: boolean): void
```

An event triggered when the game completes (re)connecting to a Mumble server.

**Parámetros**

- `address: string`: The address of the Mumble server connected to.
- `reconnecting: boolean`: Is this a reconnection to a Mumble server.

### mumbleDisconnected

```ts
mumbleDisconnected(address: string): void
```

An event triggered when the game disconnects from a Mumble server without being reconnected.

**Parámetros**

- `address: string`: The address of the Mumble server disconnected from.

### onClientResourceStart

```ts
onClientResourceStart(resource: string): void
```

An event that is *queued* after a resource has started.

**Parámetros**

- `resource: string`: The name of the resource that has started.

### onClientResourceStop

```ts
onClientResourceStop(resource: string): void
```

An event that is triggered after a resource has stopped.

**Parámetros**

- `resource: string`: The name of the resource that has stopped.

### onResourceStart

```ts
onResourceStart(resource: string): void
```

An event that is triggered *immediately* when a resource has started.

**Parámetros**

- `resource: string`: The name of the resource that just started.

### onResourceStarting

```ts
onResourceStarting(resource: string): void
```

An event that is triggered when a resource is trying to start.

This can be canceled to prevent the resource from starting.

**Parámetros**

- `resource: string`: The name of the resource that is trying to start.

### onResourceStop

```ts
onResourceStop(resource: string): void
```

An event that is triggered *immediately* when a resource is stopping.

**Parámetros**

- `resource: string`: The name of the resource that is stopping.

### populationPedCreating

```ts
populationPedCreating(x: number, y: number, z: number, model: number, overrideCalls: { setModel: any; setPosition: any }): void
```

An event that is triggered when a ped is being created by the game population system. The event can be canceled to stop creating the ped.

**Parámetros**

- `x: number`: The X position the ped is trying to spawn at.
- `y: number`: The Y position.
- `z: number`: The Z position.
- `model: number`: The intended model.
- `overrideCalls: { setModel: any; setPosition: any }`: Functions to override position or model.
- `setModel: function`
- `model: string | number`: The model hash or name of the target ped model.
- `setPosition: function`
- `x: number`: The X position the ped will spawn at.
- `y: number`: The Y position.
- `z: number`: The Z position.


## spawnmanager events

These events are part of the [spawnmanager](../../../resources/spawnmanager/README.md) resource.

- [playerSpawned](../../../resources/spawnmanager/events/playerSpawned.md)

## mapmanager events

These events are part of the [mapmanager](../../../resources/mapmanager/README.md) resource.

- [onClientMapStart](../../../resources/mapmanager/events/onClientMapStart.md)
- [onClientGameTypeStart](../../../resources/mapmanager/events/onClientGameTypeStart.md)
- [onClientMapStop](../../../resources/mapmanager/events/onClientMapStop.md)
- [onClientGameTypeStop](../../../resources/mapmanager/events/onClientGameTypeStop.md)
- [getMapDirectives](../../../resources/mapmanager/events/getMapDirectives.md)

## baseevents events

These events are part of the [baseevents](../../../resources/baseevents/README.md) resource.

- [onPlayerDied](../../../resources/baseevents/events/onPlayerDied.md)
- [onPlayerKilled](../../../resources/baseevents/events/onPlayerKilled.md)

## sessionmanager events

These events are part of the [sessionmanager](../../../resources/sessionmanager/README.md) resource.

- [playerActivated](../../../resources/sessionmanager/events/playerActivated.md)
- [sessionInitialized](../../../resources/sessionmanager/events/sessionInitialized.md)

## chat events

These events are part of the [chat](../../../resources/chat/README.md) resource.

- [chatMessage](../../../resources/chat/events/chatMessage.md)
- [chat:addMessage](../../../resources/chat/events/chat-addMessage.md)
- [chat:addTemplate](../../../resources/chat/events/chat-addTemplate.md)
- [chat:addSuggestion](../../../resources/chat/events/chat-addSuggestion.md)
- [chat:removeSuggestion](../../../resources/chat/events/chat-removeSuggestion.md)
- [chat:clear](../../../resources/chat/events/chat-clear.md)
