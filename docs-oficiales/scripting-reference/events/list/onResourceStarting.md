# onResourceStarting

> Fuente original: https://docs.fivem.net/docs/scripting-reference/events/list/onResourceStarting/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Called before a resource starts. This event can be canceled to prevent this resource from starting.

## Parameters

```
string resourceName
```

- resourceName: The name of the resource that is trying to start.

## Examples

This example prevents any resource called 'pineapple' from starting.

### Lua Example:

```lua
AddEventHandler('onResourceStarting', function(resourceName)
  if resourceName == 'pineapple' then
    CancelEvent()
  end
end)
```

### C\# Example:

```csharp
// in the class constructor
EventHandlers["onResourceStarting"] += new Action<string>(OnResourceStarting);

// delegate method
private void OnResourceStarting(string resourceName)
{
  if (resourceName == "pineapple")
  {
    CancelEvent();
  }
}
```

### JavaScript Example:

```js
on("onResourceStarting", (resourceName) => {
  if (resourceName === "pineapple") {
    CancelEvent();
  }
});
```
