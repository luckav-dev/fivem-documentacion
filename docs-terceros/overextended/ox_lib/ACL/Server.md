> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/ACL/Server.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Server

Wrapper around the built-in ACL system. Handles lib.addCommand and ox_groups permissions.  
Refer to [Basic Aces & Principals overview/guide](https://forum.cfx.re/t/basic-aces-principals-overview-guide/90917) for more information.

## lib.addAce

Assigns the ace permission to a principal. Third parameter defaults to 'allow', while passing `false` sets the permission to 'deny'.

**Lua**

```lua
lib.addAce(principal, ace, allow)

lib.addAce('group.admin', 'command.say')
```

**JS**

```ts
import lib from '@overextended/ox_lib/server'

lib.addAce(principal, ace, allow)

lib.addAce('group.admin', 'command.say')
```

- principal: `string`
- ace: `string`
- allow: `boolean`

## lib.removeAce

Removes the ace permission from a principal. Third parameter defaults to 'allow', while passing `false` sets the permission to 'deny'.

**Lua**

```lua
lib.removeAce(principal, ace, allow)

lib.removeAce('group.admin', 'command.say')
```

**JS**

```ts
import lib from '@overextended/ox_lib/server'

lib.removeAce(principal, ace, allow)

lib.removeAce('group.admin', 'command.say')
```

- principal: `string`
- ace: `string`
- allow: `boolean`

## lib.addPrincipal

Assigns a principal to a parent principal. Children inherit permissions from the parent.

**Lua**

```lua
lib.addPrincipal(child, parent)

lib.addPrincipal('player.1', 'group.moderator')
```

**JS**

```ts
import lib from '@overextended/ox_lib/server'

lib.addPrincipal(child, parent)

lib.addPrincipal('player.1', 'group.moderator')
```

- child: `string`
- parent: `string`

## lib.removePrincipal

Removes a principal from a parent principal.

**Lua**

```lua
lib.removePrincipal(child, parent)

lib.removePrincipal('player.1', 'group.moderator')
```

**JS**

```ts
import lib from '@overextended/ox_lib/server'

lib.removePrincipal(child, parent)

lib.removePrincipal('player.1', 'group.moderator')
```

- child: `string`
- parent: `string`
