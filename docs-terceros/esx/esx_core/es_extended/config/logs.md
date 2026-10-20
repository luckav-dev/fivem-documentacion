> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/config/logs.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# Discord Logging Config

> **Advertencia:** It is not recommended to use discord logging for production servers.
> Discord logging can be slow and unreliable, with often rate limits.
> So try looking at options like Datadog or Grafana.

### Webhooks
This specifies the webhooks for specific functions. You can also add your own webhooks here.
- default (Logging for everything that doesn't have a specific group)
- test (Logging for testing purposes)
- Chat (Logging of the ingame chat)
- UserActions (Commands ran by players)
- Resources (Logging for resources)
- Paycheck (Logging the playcheck if enabled)

Adding your own webhook:
**Example**
```lua
Config.Webhooks = {
    default = '',
    test = '',
    Chat = '',
    UserActions = '',
    Resources = '',
    Paycheck = '',
    Police = '' -- My custom webhook for logging my custom police actions
},
```

### Colors
This specifies the colors that can be used by the logs. You can also add your own colors here. Make sure to use the "Decimal value" of the colors.
For help you can use this website: [spycolor.com](https://www.spycolor.com/)
