# Canceling Events

> Fuente original: https://docs.fivem.net/docs/scripting-manual/working-with-events/canceling-events/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

## Canceling Events

To cancel an event, use the [`CANCEL_EVENT`](../../../natives/cfx/compartidos.md#cancelevent) native from within an event handler. This does not stop other event handlers from running.

## Example

**Lua**

```lua
AddEventHandler("eventName", function(eventParam1, eventParam2)
    -- Canceling this event!
    CancelEvent()
end)
```

**C#**

```csharp
EventHandlers["eventName"] += new Action<string, bool>(TargetFunction);

private void TargetFunction(string param1, bool param2)
{
    // Canceling this event!
    CancelEvent();
}
```

**JS**

```js
on('eventName', (eventParam1, eventParam2) => {
    // Canceling this event!
    CancelEvent();
});
```

## Checking for canceled events

To check if the last event you triggered was canceled, use the [`WAS_EVENT_CANCELED`](../../../natives/cfx/compartidos.md#waseventcanceled) native. This only works for **local** events.

## Example

**Lua**

```lua
TriggerEvent("eventName", eventParam1, eventParam2)

if WasEventCanceled() then
    -- Code that runs if the event was canceled.
end
```

In Lua, the `TriggerEvent()` function returns true if the event was canceled, allowing you to also use the following syntax:

**Lua**

```lua
if TriggerEvent("eventName", eventParam1, eventParam2) then
    -- Code that runs if the event was canceled.
end
```

**C#**

```csharp
TriggerEvent("eventName", eventParam1, eventParam2);

if (WasEventCanceled())
{
    // Code that runs if the event was canceled.
}
```

**JS**

```js
emit("eventName", eventParam1, eventParam2);

if (WasEventCanceled()) {
    // Code that runs if the event was canceled.
}
```
