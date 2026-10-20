> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Interface/Client/notify.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Notifications

## lib.notify

Custom notifications with a lot of styling options.

**Lua**

**Client**

```lua
lib.notify(data)
```

**Server**

```lua
TriggerClientEvent('ox_lib:notify', source, data)
```

**JS**

```ts
import lib from '@overextended/ox_lib/client';

lib.notify(data);
```

- id?: `string`
  - When set the current notification will be unique and only shown once on screen when spammed.
- title?: `string`
  - Must provide if there is no description
- description?: `string`
  - Must provide if there is no title
  - Markdown support
- duration?: `number`
  - Default: `3000`
- showDuration?: `boolean`
  - Default: `true`
- position?: `'top'` or `'top-right'` or `'top-left'` or `'bottom'` or `'bottom-right'` or `'bottom-left'` or `'center-right'` or `'center-left'`
  - Default: `'top-right'`
- type?: `'inform'` or `'error'` or `'success'`or `'warning'`
  - Default: `'inform'`
- style?: `table` (`object`)
  - React CSS styling format
- icon?: `string`
  - Font Awesome 6 icon name
- iconColor?: `string`
  - CSS Legal Color Values
- iconAnimation?: `'spin'` `'spinPulse'` `'spinReverse'` `'pulse'` `'beat'` `'fade'` `'beatFade'` `'bounce'` `'shake'`
- alignIcon?: `'top'` or `'center'`
  - Default: `'center'`
- sound?: `table` (`object`)
  - bank?: `string`
    - name of audio bank that contains the soundset provided
  - set: `string`
    - Soundset the soundname is a member of.
  - name: `string`

> **Nota:** Setting `iconColor` will get rid of the contrasted icon colour and it's circular background.

## Usage Example

### Standard

**Lua**

```lua
lib.notify({
    title = 'Notification title',
    description = 'Notification description',
    type = 'success'
})
```

**JS**

```ts
import lib from '@overextended/ox_lib/client';

lib.notify({
  title: 'Notification title',
  description: 'Notification description',
  type: 'success',
});
```

![notification](../../../imagenes/externas/i.imgur.com/UOISjlm-67720d.png)

### Custom

**Lua**

```lua
lib.notify({
    id = 'some_identifier',
    title = 'Notification title',
    description = 'Notification description',
    showDuration = false,
    position = 'top',
    style = {
        backgroundColor = '#141517',
        color = '#C1C2C5',
        ['.description'] = {
          color = '#909296'
        }
    },
    icon = 'ban',
    iconColor = '#C53030'
})
```

**JS**

```ts
import lib from '@overextended/ox_lib/client';

lib.notify({
  id: 'some_identifier',
  title: 'Notification title',
  description: 'Notification description',
  showDuration: false,
  position: 'top',
  style: {
    backgroundColor: '#141517',
    color: '#C1C2C5',
    '.decription': {
      color: '#909296',
    },
  },
  icon: 'ban',
  iconColor: '#C53030',
});
```

![custom_notification](../../../imagenes/externas/i.imgur.com/1qwsJsH-470a6f.png)
