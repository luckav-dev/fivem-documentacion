# onResourceStart

> Fuente original: https://docs.fivem.net/docs/scripting-reference/events/list/onResourceStart/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

Called while a resource starts.

## Parameters

```
string resourceName
```

- resourceName: The name of the resource that started.

## Examples

This example prints the name of the current resource, upon start.

### Lua Example:

```lua
AddEventHandler('onResourceStart', function(resourceName)
  if (GetCurrentResourceName() ~= resourceName) then
    return
  end
  print('The resource ' .. resourceName .. ' has been started.')
end)
```

### C\# Example:

```csharp
// in the class constructor
EventHandlers["onResourceStart"] += new Action<string>(OnResourceStart);

// delegate method
private void OnResourceStart(string resourceName)
{
  if (GetCurrentResourceName() != resourceName) return;

  Debug.WriteLine($"The resource {resourceName} has been started.");
}
```

### JavaScript Example:

```js
on("onResourceStart", (resourceName) => {
  if(GetCurrentResourceName() != resourceName) {
    return;
  }

  console.log(`The resource ${resourceName} has been started.`)
});
```
