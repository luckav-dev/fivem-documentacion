> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/resources/qbx_core/modules/logger.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# logger

*Documentation for the logger module in the qbx_core resource. This module provides logging functionality that can output to both Discord webhooks and ox_lib's logging system, supporting various log levels and customization options.*

> **Nota:** See the ox_lib [Logger](https://coxdocs.dev/ox_lib/Modules/Logger/Server) for further details.

Adds a logger that logs to Discord if a webhook is given, and with ox_lib otherwise.

```lua
local logger = require '@qbx_core.modules.logger'

logger.log(log)
```

- log: `table`
  - source: `string`
    - The source of the log; usually a player ID or the name of a resource.
  - event: `string`
    - The action or `event` being logged; usually a verb describing what the name is doing.
    - Example: `'SpawnVehicle'`
  - message: `string`
    - A message attached to the log.
  - webhook?: `string`
    - Discord logs only.
    - The URL of the webhook that this should log to.
  - color?: `string`
    - Discord logs only.
    - The color the message should be.
  - tags?: `string[]`
    - Discord logs only.
    - Tags to be added to the Discord message.
    - Example: `{ '<@&roleid>', '<@userid>', '@everyone' }`

## Example Usage

```lua
local logger = require '@qbx_core.modules.logger'

logger.log({
  source = 'my source',
  event = 'my event',
  message = 'my message',
  tags = { '@everyone' },
})
```
