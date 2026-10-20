# onResourceStop

> Fuente original: https://docs.fivem.net/docs/scripting-reference/events/list/onResourceStop/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Called while a resource stops.

## Parameters

```
string resourceName
```

- resourceName: The name of the resource that stopped.

## Examples

This example prints the name of the current resource, when stopped.

### Lua Example:

```lua
AddEventHandler('onResourceStop', function(resourceName)
  if (GetCurrentResourceName() ~= resourceName) then
    return
  end
  print('The resource ' .. resourceName .. ' was stopped.')
end)
```

### C\# Example:

```csharp
// in the class constructor
EventHandlers["onResourceStop"] += new Action<string>(OnResourceStop);

// delegate method
private void OnResourceStop(string resourceName)
{
  if(GetCurrentResourceName() != resourceName) return;

  Debug.WriteLine($"The resource {resourceName} was stopped.");
}
```

### JavaScript Example:

```js
on("onResourceStop", (resourceName) => {
  if(GetCurrentResourceName() != resourceName) {
    return;
  }

  console.log(`The resource ${resourceName} has been stopped.`)
});
```
