> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/esx_notify.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_notify

The notification system used by `es_extended`

**Arguments**
- message: `string`
- The notification message
- type: `string`
- The notification type
- length: `number`
- The notification length
- title: `string?`
- The notification title (optional)
- position: `string?`
- Teh notification position (optional)

**Notification Types**
- success
- error
- info
- warning

**Notification positions**
- top-right
- top-left
- top-middle
- bottom-right
- bottom-left
- bottom-middle
- middle-left
- middle-right (Default)

## Client Triggers

### ESX Function

**Example**
```lua
ESX.ShowNotification("message here", "success", 3000, "title here", "top-left")
```

### Export

**Example**
```lua
exports['esx_notify']:Notify('error', 'This is my new test.',  1500, "Test Notification", "top-left") 
```

## Server Triggers

**Example**
```lua
TriggerClientEvent("esx:showNotification", playerId, "This is my new test.", "error", 1500, "Test Notification", "top-left")
```
