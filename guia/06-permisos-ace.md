[← 05-comandos-y-convars](05-comandos-y-convars.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [07-recursos-y-fxmanifest →](07-recursos-y-fxmanifest.md)

# 6. Permisos: sistema ACE

FiveM tiene un sistema de permisos integrado basado en **ACE** (*Access Control Entries*) y **principals**.

## 6.1 Conceptos

- **Principal**: "quién". Ej.: `identifier.license:xxxx`, `identifier.discord:1234`, `identifier.fivem:5678`, `group.admin`, `resource.mi_recurso`, `builtin.everyone`.
- **Object (objeto)**: "qué". Ej.: `command`, `command.ban`, `mi_recurso.abrir_menu`, `vehicle.spawn`.
- **ACE**: regla `principal + objeto + allow/deny`.
- **Herencia**: `add_principal hijo padre` hace que el hijo herede los permisos del padre.
- Los objetos son jerárquicos con puntos: permitir `command` permite `command.lo_que_sea`, salvo que exista un `deny` más específico.
- `deny` siempre gana sobre `allow` del mismo nivel.

## 6.2 Comandos

```cfg
add_ace <principal> <objeto> <allow|deny>
remove_ace <principal> <objeto> <allow|deny>
add_principal <hijo> <padre>
remove_principal <hijo> <padre>
test_ace <principal> <objeto>          # comprueba si está permitido
list_aces                              # lista todas las ACE
list_principals                        # lista toda la herencia
```

## 6.3 Ejemplo de jerarquía completa

```cfg
# Grupos (de menor a mayor)
add_principal group.mod group.helper
add_principal group.admin group.mod
add_principal group.superadmin group.admin

# Permisos de cada grupo
add_ace group.helper chat.staff allow
add_ace group.mod command.kick allow
add_ace group.mod command.tp allow
add_ace group.admin command allow        # todos los comandos
add_ace group.admin command.quit deny    # menos apagar el servidor
add_ace group.superadmin command.quit allow

# Asignar jugadores
add_principal identifier.fivem:1234567 group.superadmin
add_principal identifier.license:1a2b3c4d5e6f group.admin
add_principal identifier.discord:123456789012345678 group.mod

# Permitir a un recurso ejecutar comandos (p. ej. que pueda usar ExecuteCommand)
add_ace resource.mi_admin command allow

# Permitir a un recurso arrancar/parar otros recursos
add_ace resource.mi_gestor command.start allow
add_ace resource.mi_gestor command.stop allow
add_ace resource.mi_gestor command.ensure allow
```

## 6.4 Usar ACE desde scripts

**Comandos restringidos** — con el tercer parámetro `true`, FiveM exige `command.<nombre>`:

```lua
RegisterCommand('anuncio', function(source, args, raw)
    local texto = table.concat(args, ' ')
    TriggerClientEvent('chat:addMessage', -1, { args = { '^1ANUNCIO', texto } })
end, true) -- restringido: requiere "command.anuncio"
```

**Comprobar permisos propios:**

```lua
-- servidor
if IsPlayerAceAllowed(source, 'mi_recurso.abrir_menu') then
    -- permitido
end
```

```cfg
add_ace group.admin mi_recurso.abrir_menu allow
```

**Añadir/quitar permisos en caliente desde un script** (el recurso necesita permiso para ejecutar `add_principal`):

```lua
ExecuteCommand(('add_principal identifier.%s group.admin'):format(license))
```

```cfg
add_ace resource.mi_admin command.add_principal allow
add_ace resource.mi_admin command.remove_principal allow
```

> Los frameworks (ESX, QBCore, Qbox) suelen tener su propio sistema de grupos que **se apoya** en ACE (`group.admin`, `qbcore.god`, etc.). Revisa su documentación para no duplicar.


## Ver también (documentación offline)

- [Oficial: cookbook/2021/07/17/quick-note-on-using-built-in-acl-security](../docs-oficiales/cookbook/2021/07/17/quick-note-on-using-built-in-acl-security.md)
- [Oficial: resources/txAdmin/permissions](../docs-oficiales/resources/txAdmin/permissions.md)

---

[← 05-comandos-y-convars](05-comandos-y-convars.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [07-recursos-y-fxmanifest →](07-recursos-y-fxmanifest.md)
