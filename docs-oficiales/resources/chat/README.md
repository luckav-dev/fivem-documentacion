# chat

> Fuente original: https://docs.fivem.net/docs/resources/chat/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

## About

The chat resource provides custom chat functionality for FiveM using a NUI-based interface.
It is included and maintained at the cfx-server-data repository.

## Exports

### Client

- [addMessage](exports/addMessagecl.md)
- [addSuggestion](exports/addSuggestion.md)

### Server

- [addMessage](exports/addMessagesv.md)
- [registerMessageHook](exports/registerMessageHook.md)
- [registerMode](exports/registerMode.md)

## Events

### Client

- [chatMessage](events/chatMessage.md) (deprecated, use chat:addMessage instead)
- [chat:addMessage](events/chat-addMessage.md)
- [chat:addSuggestion](events/chat-addSuggestion.md)
- [chat:addSuggestions](events/chat-addSuggestions.md)
- [chat:removeSuggestion](events/chat-removeSuggestion.md)
- [chat:addTemplate](events/chat-addTemplate.md)
- [chat:clear](events/chat-clear.md)

### Server

- [chatMessage](events/chatMessage.md)
