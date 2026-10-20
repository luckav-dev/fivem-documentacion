# Server Events

> Fuente original: https://docs.fivem.net/docs/scripting-reference/events/server-events/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

**A list of server side events you can use in your scripts.**

## Core events

These events are part of FiveM and don't require any additional resources.

### entityCreated

```ts
entityCreated(handle: number): void
```

A server-side event that is triggered when an entity has been created.

**Parámetros**

- `handle: number`

### entityCreating

```ts
entityCreating(handle: number): void
```

A server-side event that is triggered when an entity is being created.

This event **can** be canceled to instantly delete the entity.

**Parámetros**

- `handle: number`

### entityRemoved

```ts
entityRemoved(entity: number): void
```

Triggered when an entity is removed on the server.

**Parámetros**

- `entity: number`: The handle of the entity that got removed.

### onResourceListRefresh

```ts
onResourceListRefresh(): void
```

A server-side event triggered when the `refresh` command completes.

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

### onServerResourceStart

```ts
onServerResourceStart(resource: string): void
```

An event that is *queued* after a resource has started.

**Parámetros**

- `resource: string`: The name of the resource that has started.

### onServerResourceStop

```ts
onServerResourceStop(resource: string): void
```

An event that is triggered after a resource has stopped.

**Parámetros**

- `resource: string`: The name of the resource that has stopped.

### playerConnecting

```ts
playerConnecting(playerName: string, setKickReason: (reason: string) => void, deferrals: { defer: any; done: any; handover: any; presentCard: any; update: any }, source: string): void
```

A server-side event that is triggered when a player is trying to connect.

This event can be canceled to reject the player *instantly*, assuming you haven't yielded.

**Parámetros**

- `playerName: string`: The display name of the player connecting.
- `setKickReason: (reason: string) => void`: A function used to set a reason message for when the event is canceled.
- `reason: string`
- `deferrals: { defer: any; done: any; handover: any; presentCard: any; update: any }`: An object to control deferrals.
- `defer: function`
- `done: function`
- `Optional failureReason: string`: If specified, the connection will be refused, and the user will see the specified message as a result. If this is not specified, the user will be allowed to connect.
- `handover: function`
- `data: {}`: Data to pass to the connecting client.
- `[key: string]: any`
- `presentCard: function`
- `card: string | object`: An object containing card data, or a serialized JSON string with the card information.
- `Optional cb: (data: any, rawData: string) => void`: If present, will be invoked on an `Action.Submit` event from the Adaptive Card.
- `data: any`: A parsed version of the data sent from the card.
- `rawData: string`: A JSON string containing the data sent from the card.
- `update: function`
- `message: string`: The string to send to the client.
- `source: string`: The player's *temporary* NetID (a number in Lua/JS), **not a real argument, use [FromSource] or source**.

### playerEnteredScope

```ts
playerEnteredScope(data: { for: string; player: string }): void
```

A server-side event that is triggered when a player enters another player's scope.

**Parámetros**

- `data: { for: string; player: string }`: Data containing the players entering each other's scope.
- `for: string`: The player for which the scope is being entered.
- `player: string`: The player that is entering the scope.

### playerJoining

```ts
playerJoining(source: string, oldID: string): void
```

A server-side event that is triggered when a player has a finally-assigned NetID.

**Parámetros**

- `source: string`: The player's NetID (a number in Lua/JS), **not a real argument, use [FromSource] or source**.
- `oldID: string`: The original TempID for the connecting player, as specified during playerConnecting.

### playerLeftScope

```ts
playerLeftScope(data: { for: string; player: string }): void
```

A server-side event that is triggered when a player leaves another player's scope.

**Parámetros**

- `data: { for: string; player: string }`: Data containing the players leaving each other's scope.
- `for: string`: The player for which the scope is being left.
- `player: string`: The player that is leaving the scope.

### ptFxEvent

```ts
ptFxEvent(sender: number, data: { assetHash: number; axisBitset: number; effectHash: number; entityNetId: number; f100: number; f105: number; f106: number; f107: number; f109: boolean; f110: boolean; f111: boolean; f92: number; isOnEntity: boolean; offsetX: number; offsetY: number; offsetZ: number; posX: number; posY: number; posZ: number; rotX: number; rotY: number; rotZ: number; scale: number }): void
```

Triggered when a particle fx (ptFx) is created.

**Parámetros**

- `sender: number`: The ID of the player that triggered the event.
- `data: { assetHash: number; axisBitset: number; effectHash: number; entityNetId: number; f100: number; f105: number; f106: number; f107: number; f109: boolean; f110: boolean; f111: boolean; f92: number; isOnEntity: boolean; offsetX: number; offsetY: number; offsetZ: number; posX: number; posY: number; posZ: number; rotX: number; rotY: number; rotZ: number; scale: number }`: The event data.
- `assetHash: number`
- `axisBitset: number`
- `effectHash: number`
- `entityNetId: number`
- `f100: number`
- `f105: number`
- `f106: number`
- `f107: number`
- `f109: boolean`
- `f110: boolean`
- `f111: boolean`
- `f92: number`
- `isOnEntity: boolean`
- `offsetX: number`
- `offsetY: number`
- `offsetZ: number`
- `posX: number`
- `posY: number`
- `posZ: number`
- `rotX: number`
- `rotY: number`
- `rotZ: number`
- `scale: number`

### removeAllWeaponsEvent

```ts
removeAllWeaponsEvent(sender: number, data: { pedId: number }): void
```

Triggered when a player removes all weapons from a ped owned by another player.

**Parámetros**

- `sender: number`: The ID of the player that triggered the event.
- `data: { pedId: number }`: The event data.
- `pedId: number`

### startProjectileEvent

```ts
startProjectileEvent(sender: number, data: { commandFireSingleBullet: boolean; effectGroup: number; firePositionX: number; firePositionY: number; firePositionZ: number; initialPositionX: number; initialPositionY: number; initialPositionZ: number; ownerId: number; projectileHash: number; targetEntity: number; throwTaskSequence: number; unk10: number; unk11: number; unk12: number; unk13: number; unk14: number; unk15: number; unk16: number; unk3: number; unk4: number; unk5: number; unk6: number; unk7: number; unk9: number; unkX8: number; unkY8: number; unkZ8: number; weaponHash: number }): void
```

Triggered when a projectile is created.

**Parámetros**

- `sender: number`: The ID of the player that triggered the event.
- `data: { commandFireSingleBullet: boolean; effectGroup: number; firePositionX: number; firePositionY: number; firePositionZ: number; initialPositionX: number; initialPositionY: number; initialPositionZ: number; ownerId: number; projectileHash: number; targetEntity: number; throwTaskSequence: number; unk10: number; unk11: number; unk12: number; unk13: number; unk14: number; unk15: number; unk16: number; unk3: number; unk4: number; unk5: number; unk6: number; unk7: number; unk9: number; unkX8: number; unkY8: number; unkZ8: number; weaponHash: number }`: The event data.
- `commandFireSingleBullet: boolean`
- `effectGroup: number`
- `firePositionX: number`
- `firePositionY: number`
- `firePositionZ: number`
- `initialPositionX: number`
- `initialPositionY: number`
- `initialPositionZ: number`
- `ownerId: number`
- `projectileHash: number`
- `targetEntity: number`
- `throwTaskSequence: number`
- `unk10: number`
- `unk11: number`
- `unk12: number`
- `unk13: number`
- `unk14: number`
- `unk15: number`
- `unk16: number`
- `unk3: number`
- `unk4: number`
- `unk5: number`
- `unk6: number`
- `unk7: number`
- `unk9: number`
- `unkX8: number`
- `unkY8: number`
- `unkZ8: number`
- `weaponHash: number`

### weaponDamageEvent

```ts
weaponDamageEvent(sender: number, data: { actionResultId: number; actionResultName: number; damageFlags: number; damageTime: number; damageType: number; f104: number; f112: boolean; f112_1: number; f120: number; f133: boolean; hasActionResult: boolean; hasImpactDir: boolean; hasVehicleData: boolean; hitComponent: number; hitEntityWeapon: boolean; hitGlobalId: number; hitGlobalIds: number[]; hitWeaponAmmoAttachment: boolean; impactDirX: number; impactDirY: number; impactDirZ: number; isNetTargetPos: boolean; localPosX: number; localPosY: number; localPosZ: number; overrideDefaultDamage: boolean; parentGlobalId: number; silenced: boolean; suspensionIndex: number; tyreIndex: number; weaponDamage: number; weaponType: number; willKill: boolean }): void
```

Triggered when a client wants to apply damage to a remotely-owned entity. This event can be canceled.

**Parámetros**

- `sender: number`: The server-side player ID of the player that triggered the event.
- `data: { actionResultId: number; actionResultName: number; damageFlags: number; damageTime: number; damageType: number; f104: number; f112: boolean; f112_1: number; f120: number; f133: boolean; hasActionResult: boolean; hasImpactDir: boolean; hasVehicleData: boolean; hitComponent: number; hitEntityWeapon: boolean; hitGlobalId: number; hitGlobalIds: number[]; hitWeaponAmmoAttachment: boolean; impactDirX: number; impactDirY: number; impactDirZ: number; isNetTargetPos: boolean; localPosX: number; localPosY: number; localPosZ: number; overrideDefaultDamage: boolean; parentGlobalId: number; silenced: boolean; suspensionIndex: number; tyreIndex: number; weaponDamage: number; weaponType: number; willKill: boolean }`: The event data.
- `actionResultId: number`
- `actionResultName: number`
- `damageFlags: number`
- `damageTime: number`: The timestamp the damage was originally inflicted at. This should match the global network timer.
- `damageType: number`: A value (between 0 and 3) containing an internal damage type. Specific values are currently unknown.
- `f104: number`
- `f112: boolean`
- `f112_1: number`
- `f120: number`
- `f133: boolean`
- `hasActionResult: boolean`
- `hasImpactDir: boolean`
- `hasVehicleData: boolean`
- `hitComponent: number`
- `hitEntityWeapon: boolean`: Whether the damage should be inflicted as if it hit the weapon the entity is carrying. This likely applies to grenades being hit, which should explode, but also normal weapons, which should not harm the player much.
- `hitGlobalId: number`: The network ID of the victim entity.
- `hitGlobalIds: number[]`: An array containing network IDs of victim entities. If there is more than one, the first one will be set in `hitGlobalId`.
- `hitWeaponAmmoAttachment: boolean`: Whether the damage should be inflicted as if it hit an ammo attachment component on the weapon. This applies to players/peds carrying weapons where another player shooting the ammo component makes the weapon explode.
- `impactDirX: number`
- `impactDirY: number`
- `impactDirZ: number`
- `isNetTargetPos: boolean`
- `localPosX: number`
- `localPosY: number`
- `localPosZ: number`
- `overrideDefaultDamage: boolean`: If set, 'weaponDamage' is valid. If unset, the game infers the damage from weapon metadata.
- `parentGlobalId: number`
- `silenced: boolean`: Set when the damage is applied using a silenced weapon.
- `suspensionIndex: number`
- `tyreIndex: number`
- `weaponDamage: number`: The amount of damage inflicted, if `overrideDefaultDamage` is set. If not, this value is set to `0`.
- `weaponType: number`: The weapon hash for the inflicted damage.
- `willKill: boolean`: Whether the originating client thinks this should be instantly-lethal damage, such as a critical headshot.
