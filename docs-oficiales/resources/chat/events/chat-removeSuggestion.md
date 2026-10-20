# chat:removeSuggestion

> Fuente original: https://docs.fivem.net/docs/resources/chat/events/chat-removeSuggestion/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

## About

Triggering this allows you to remove any existing command suggestions for the specified command.

## Name

```
chat:removeSuggestion
```

## Parameters

```
string commandName
```

## Examples

This example removes the suggestion that was created with the example of [chat:addSuggestion](chat-addSuggestion.md).

### Lua Example:

```lua
TriggerEvent('chat:removeSuggestion', '/command')
```

### C\# Example:

```csharp
TriggerEvent("chat:removeSuggestion", "/command");
```

### JavaScript Example:

```javascript
emit('chat:removeSuggestion', '/command');
```
