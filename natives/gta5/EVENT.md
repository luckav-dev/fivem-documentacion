# Natives de GTA V — EVENT

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `EVENT`: **13** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddShockingEventAtPosition`](#addshockingeventatposition) · [`AddShockingEventForEntity`](#addshockingeventforentity) · [`BlockDecisionMakerEvent`](#blockdecisionmakerevent) · [`ClearDecisionMakerEventResponse`](#cleardecisionmakereventresponse) · [`IsShockingEventInSphere`](#isshockingeventinsphere) · [`RemoveAllShockingEvents`](#removeallshockingevents) · [`RemoveShockingEvent`](#removeshockingevent) · [`RemoveShockingEventSpawnBlockingAreas`](#removeshockingeventspawnblockingareas) · [`SetDecisionMaker`](#setdecisionmaker) · [`SuppressAgitationEventsNextFrame`](#suppressagitationeventsnextframe) · [`SuppressShockingEventTypeNextFrame`](#suppressshockingeventtypenextframe) · [`SuppressShockingEventsNextFrame`](#suppressshockingeventsnextframe) · [`UnblockDecisionMakerEvent`](#unblockdecisionmakerevent)

---
### AddShockingEventAtPosition

`ADD_SHOCKING_EVENT_AT_POSITION` · hash `0xD9F8455409B525E9` · jhash `0x0B30F779` · **Cliente**

```lua
local retval = AddShockingEventAtPosition(eventType, x, y, z, duration)
```
```c
ScrHandle ADD_SHOCKING_EVENT_AT_POSITION(int eventType, float x, float y, float z, float duration);
```

**Parámetros**

- `eventType` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `duration` (`float`)

**Devuelve:** `ScrHandle`

**Descripción oficial:**

```
eventType: https://alloc8or.re/gta5/doc/enums/eEventType.txt
```

---
### AddShockingEventForEntity

`ADD_SHOCKING_EVENT_FOR_ENTITY` · hash `0x7FD8F3BE76F89422` · jhash `0xA81B5B71` · **Cliente**

```lua
local retval = AddShockingEventForEntity(eventType, entity, duration)
```
```c
ScrHandle ADD_SHOCKING_EVENT_FOR_ENTITY(int eventType, Entity entity, float duration);
```

**Parámetros**

- `eventType` (`int`)
- `entity` (`Entity`)
- `duration` (`float`)

**Devuelve:** `ScrHandle`

**Descripción oficial:**

```
eventType: https://alloc8or.re/gta5/doc/enums/eEventType.txt
```

---
### BlockDecisionMakerEvent

`BLOCK_DECISION_MAKER_EVENT` · hash `0xE42FCDFD0E4196F7` · jhash `0x57506EA6` · **Cliente**

```lua
BlockDecisionMakerEvent(name, eventType)
```
```c
void BLOCK_DECISION_MAKER_EVENT(Hash name, int eventType);
```

**Parámetros**

- `name` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `eventType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
eventType: https://alloc8or.re/gta5/doc/enums/eEventType.txt
This is limited to 4 blocked events at a time.
```

---
### ClearDecisionMakerEventResponse

`CLEAR_DECISION_MAKER_EVENT_RESPONSE` · hash `0x4FC9381A7AEE8968` · jhash `0x07ABD94D` · **Cliente**

```lua
ClearDecisionMakerEventResponse(name, eventType)
```
```c
void CLEAR_DECISION_MAKER_EVENT_RESPONSE(Hash name, int eventType);
```

**Parámetros**

- `name` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `eventType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
eventType: https://alloc8or.re/gta5/doc/enums/eEventType.txt
```

---
### IsShockingEventInSphere

`IS_SHOCKING_EVENT_IN_SPHERE` · hash `0x1374ABB7C15BAB92` · jhash `0x2F98823E` · **Cliente**

```lua
local retval = IsShockingEventInSphere(eventType, x, y, z, radius)
```
```c
BOOL IS_SHOCKING_EVENT_IN_SPHERE(int eventType, float x, float y, float z, float radius);
```

**Parámetros**

- `eventType` (`int`)
- `x` (`float`)
- `y` (`float`)
- `z` (`float`)
- `radius` (`float`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
eventType: https://alloc8or.re/gta5/doc/enums/eEventType.txt
```

---
### RemoveAllShockingEvents

`REMOVE_ALL_SHOCKING_EVENTS` · hash `0xEAABE8FDFA21274C` · jhash `0x64DF6282` · **Cliente**

```lua
RemoveAllShockingEvents(p0)
```
```c
void REMOVE_ALL_SHOCKING_EVENTS(BOOL p0);
```

**Parámetros**

- `p0` (`BOOL`)

**Devuelve:** `void`

---
### RemoveShockingEvent

`REMOVE_SHOCKING_EVENT` · hash `0x2CDA538C44C6CCE5` · jhash `0xF82D5A87` · **Cliente**

```lua
local retval = RemoveShockingEvent(event)
```
```c
BOOL REMOVE_SHOCKING_EVENT(ScrHandle event);
```

**Parámetros**

- `event` (`ScrHandle`)

**Devuelve:** `BOOL`

---
### RemoveShockingEventSpawnBlockingAreas

`REMOVE_SHOCKING_EVENT_SPAWN_BLOCKING_AREAS` · hash `0x340F1415B68AEADE` · jhash `0xA0CE89C8` · **Cliente**

```lua
RemoveShockingEventSpawnBlockingAreas()
```
```c
void REMOVE_SHOCKING_EVENT_SPAWN_BLOCKING_AREAS();
```

**Devuelve:** `void`

---
### SetDecisionMaker

`SET_DECISION_MAKER` · hash `0xB604A2942ADED0EE` · jhash `0x19CEAC9E` · **Cliente**

```lua
SetDecisionMaker(ped, name)
```
```c
void SET_DECISION_MAKER(Ped ped, Hash name);
```

**Parámetros**

- `ped` (`Ped`)
- `name` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

---
### SuppressAgitationEventsNextFrame

`SUPPRESS_AGITATION_EVENTS_NEXT_FRAME` · hash `0x5F3B7749C112D552` · jhash `0x80340396` · **Cliente**

```lua
SuppressAgitationEventsNextFrame()
```
```c
void SUPPRESS_AGITATION_EVENTS_NEXT_FRAME();
```

**Devuelve:** `void`

---
### SuppressShockingEventTypeNextFrame

`SUPPRESS_SHOCKING_EVENT_TYPE_NEXT_FRAME` · hash `0x3FD2EC8BF1F1CF30` · jhash `0xA0FDCB82` · **Cliente**

```lua
SuppressShockingEventTypeNextFrame(eventType)
```
```c
void SUPPRESS_SHOCKING_EVENT_TYPE_NEXT_FRAME(int eventType);
```

**Parámetros**

- `eventType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
eventType: https://alloc8or.re/gta5/doc/enums/eEventType.txt
```

---
### SuppressShockingEventsNextFrame

`SUPPRESS_SHOCKING_EVENTS_NEXT_FRAME` · hash `0x2F9A292AD0A3BD89` · jhash `0x4CC674B5` · **Cliente**

```lua
SuppressShockingEventsNextFrame()
```
```c
void SUPPRESS_SHOCKING_EVENTS_NEXT_FRAME();
```

**Devuelve:** `void`

---
### UnblockDecisionMakerEvent

`UNBLOCK_DECISION_MAKER_EVENT` · hash `0xD7CD9CF34F2C99E8` · jhash `0x62A3161D` · **Cliente**

```lua
UnblockDecisionMakerEvent(name, eventType)
```
```c
void UNBLOCK_DECISION_MAKER_EVENT(Hash name, int eventType);
```

**Parámetros**

- `name` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `eventType` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
eventType: https://alloc8or.re/gta5/doc/enums/eEventType.txt
```

---
