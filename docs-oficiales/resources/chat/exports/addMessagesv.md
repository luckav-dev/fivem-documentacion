# addMessage (server)

> Fuente original: https://docs.fivem.net/docs/resources/chat/exports/addMessagesv/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../README.md)

## About

Using this export allows you to add a message to the target players chat.

Message object structure:

```lua
message = {
  template = template,
  color = color,
  multiline = true,
  args = {author, otherArgs...}
}
```

## Name

```
addMessage
```

## Parameters

```
int target, object/string message
```

## Examples

This example sends a chat message to all players.

### Lua Example:

```lua
AddEventHandler('onResourceStart', function(resourceName)
  if (GetCurrentResourceName() ~= resourceName) then
    return
  end
  exports.chat:addMessage(-1, {
    color = {255, 0, 0},
    args = {"SYSTEM", string.format("%s has started.", resourceName)}
  })
end)
```

Output:

![screenshot-1](../../../_archivos/chat_addMessage_export.png)
