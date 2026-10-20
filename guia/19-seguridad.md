[← 18-voz](18-voz.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [20-rendimiento →](20-rendimiento.md)

# 19. Seguridad y anti-cheat

## 19.1 Principios

1. **El cliente miente.** Todo lo que viene del cliente (eventos, state bags, callbacks NUI) puede estar manipulado: un *executor* de cheats puede disparar **cualquier** `TriggerServerEvent` con **cualquier** argumento.
2. **El servidor decide.** Dinero, ítems, permisos, precios, recompensas, posiciones válidas: se calculan y comprueban en el servidor.
3. **Mínimo privilegio.** Registra como *net event* solo lo imprescindible, da ACE solo a quien las necesita y no expongas secretos al cliente.
4. **Defensa en profundidad.** Combina validación por evento, límites de frecuencia, convars de seguridad, logs y un anti-cheat.

## 19.2 Errores típicos (y cómo evitarlos)

| Mal ❌ | Bien ✅ |
|---|---|
| `TriggerServerEvent('banco:dar', 5000)` y el servidor suma lo que llega | El servidor calcula la cantidad según la acción real (trabajo completado, precio de la tienda en `Config` del servidor). |
| El cliente dice "he completado el trabajo" y el servidor paga | El servidor comprueba distancia al punto, tiempo transcurrido desde el inicio y que el jugador tenía ese trabajo activo. |
| Precios en un `shared/config.lua` que el servidor lee del **evento** | El servidor usa su **propia** copia del `Config`, nunca el precio que envía el cliente. |
| Evento admin `admin:darDinero` sin comprobar permisos | `if not IsPlayerAceAllowed(src, 'admin.dinero') then return end` |
| Webhook de Discord en un `client_script` | Webhook en `server_script`, leído de una convar `set`. |
| SQL concatenado con datos del jugador | Placeholders `?` (ver 16.4). |
| `RegisterNetEvent` en eventos que solo se usan entre recursos del servidor | `AddEventHandler` (no es accesible desde la red). |
| Borrar entidades que manda el cliente por netId sin comprobar | Comprueba propietario, distancia, tipo y modelo. |
| Callback NUI que llama directamente a un evento de servidor con los datos tal cual | Validar en el servidor igualmente. |

## 19.3 Plantilla de evento seguro

```lua
local Cooldown = {}

RegisterNetEvent('tienda:comprar', function(itemName, cantidad)
    local src = source

    -- 1. Tipos y rangos
    if type(itemName) ~= 'string' or type(cantidad) ~= 'number' then return end
    cantidad = math.floor(cantidad)
    if cantidad < 1 or cantidad > 50 then return end

    -- 2. El ítem existe en la config DEL SERVIDOR
    local item = Config.ItemsTienda[itemName]
    if not item then return end

    -- 3. Frecuencia
    local ahora = GetGameTimer()
    if Cooldown[src] and ahora - Cooldown[src] < 500 then return end
    Cooldown[src] = ahora

    -- 4. Contexto: está cerca de una tienda
    local coords = GetEntityCoords(GetPlayerPed(src))
    local cerca = false
    for _, t in ipairs(Config.Tiendas) do
        if #(coords - t.coords) < 5.0 then cerca = true break end
    end
    if not cerca then
        return LogSospechoso(src, 'compra lejos de tienda')
    end

    -- 5. Lógica con datos del servidor
    local precio = item.precio * cantidad
    if not QuitarDinero(src, precio) then return end
    DarItem(src, itemName, cantidad)
end)

AddEventHandler('playerDropped', function() Cooldown[source] = nil end)
```

## 19.4 Convars de seguridad recomendadas

```cfg
sv_scriptHookAllowed 0
sv_pureLevel 1
set sv_entityLockdown relaxed           # o strict si TODO se crea en servidor
set sv_filterRequestControl 2
setr sv_stateBagStrictMode false        # true si ningún recurso escribe state bags desde el cliente
sv_endpointPrivacy true
set sv_enableNetworkedPhoneExplosions false
set sv_requestParanoia 1                # si estás detrás de proxy, revísalo antes
# Bloquear eventos de juego que no uses:
# block_net_game_event REQUEST_PHONE_EXPLOSION_EVENT
```

## 19.5 Eventos de juego para detectar trampas (servidor)

```lua
-- Explosiones: bloquear tipos peligrosos y registrar
AddEventHandler('explosionEvent', function(sender, ev)
    -- IDs de tipo de explosión: 0 GRENADE, 1 GRENADELAUNCHER, 2 STICKYBOMB, 3 MOLOTOV, 4 ROCKET, 5 TANKSHELL...
    -- (lista completa en la documentación del native ADD_EXPLOSION)
    local prohibidas = { [1] = true, [4] = true, [5] = true }
    if prohibidas[ev.explosionType] then
        CancelEvent()
        LogSospechoso(sender, ('explosión tipo %s'):format(ev.explosionType))
    end
end)

-- Armas entregadas por otros clientes (no las da el servidor)
AddEventHandler('giveWeaponEvent', function(sender, data)
    CancelEvent()
    LogSospechoso(sender, 'giveWeaponEvent')
end)

-- Intentos de quitar tareas a otros jugadores (sacarlos del coche, congelarlos)
AddEventHandler('clearPedTasksEvent', function(sender, data)
    if data.immediately then
        CancelEvent()
        LogSospechoso(sender, 'clearPedTasksEvent')
    end
end)

-- Daño anómalo
AddEventHandler('weaponDamageEvent', function(sender, data)
    if data.weaponDamage > 500 then
        CancelEvent()
        LogSospechoso(sender, 'daño excesivo ' .. data.weaponDamage)
    end
end)
```

> Ajusta estas reglas a tu servidor y **prueba** antes de banear automáticamente: los falsos positivos son peores que no tener reglas.

## 19.6 Protección de eventos con tokens: ¿sirve?

Los "tokens" que se pasan en cada `TriggerServerEvent` **no protegen de verdad**: el cheat puede leer el token desde la memoria del cliente. La seguridad real es **validar en el servidor** (19.3). Los tokens solo añaden fricción.

## 19.7 Eventos "trampa" (*honeypots*)

Registra eventos con nombres atractivos que **ningún recurso legítimo** usa (`esx_admin:giveMoney`, `bank:addMoney`…) y banea a quien los dispare:

```lua
local trampas = { 'esx:giveInventoryItemAdmin', 'banco:darDineroGratis', 'admin:setGod' }
for _, ev in ipairs(trampas) do
    RegisterNetEvent(ev, function()
        local src = source
        LogSospechoso(src, 'honeypot ' .. ev)
        -- BanPlayer(src, 'Uso de cheats')
    end)
end
```

## 19.8 Identificadores, tokens y bans

- Guarda **todos** los identificadores (`license`, `license2`, `fivem`, `discord`, `steam`, `ip`) **y** los tokens (`GetPlayerTokens`) al banear.
- Al conectar (`playerConnecting`), comprueba si **cualquiera** de ellos coincide con un ban.
- `ip` cambia y puede compartirse (VPN, residencias): no lo uses como único criterio.
- txAdmin incluye un sistema de **bans y avisos** con base de datos propia que ya hace esto.

## 19.9 Anti-cheat

- **Cfx.re** tiene medidas propias en el cliente y bans globales para cheats conocidos.
- txAdmin ofrece bans, avisos, logs de acciones y de servidor.
- Existen anti-cheats de terceros (de pago y gratuitos). Elige uno con buena reputación y que no rompa tu framework; ningún anti-cheat sustituye a validar tus eventos.
- **Cuidado con "anti-cheats" o recursos *leakeados***: suelen traer *backdoors* (código ofuscado que hace `PerformHttpRequest` y ejecuta lo que recibe con `load`). Busca en tus recursos `load(`, `loadstring`, `PerformHttpRequest` a dominios raros, `assert(load(` y código ofuscado.

```bash
# Buscar patrones sospechosos en todos los recursos (Linux)
grep -rnE "assert\(load|loadstring\(|load\(.*PerformHttpRequest|\\\\x[0-9a-f]{2}\\\\x" resources/ --include=*.lua | head -50
```

## 19.10 Seguridad del host

- Servidor de juego con **usuario sin privilegios** (nunca `root`/Administrador).
- Firewall: solo 30120 TCP/UDP (y 40120 restringido a tu IP o tras VPN).
- txAdmin con contraseñas fuertes y cuentas Cfx.re individuales para cada admin; revoca accesos de quien deje el staff.
- Mantén artefactos, txAdmin y recursos actualizados.
- Backups automáticos fuera del servidor (BD + `server-data`).
- **Protección DDoS** del proveedor de hosting; para grandes servidores, proxies/redes de mitigación (ver 25.3).


## Ver también (documentación offline)

- [Oficial: developers/server-security](../docs-oficiales/developers/server-security.md)
- [Oficial: developers/sandbox](../docs-oficiales/developers/sandbox.md)

---

[← 18-voz](18-voz.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [20-rendimiento →](20-rendimiento.md)
