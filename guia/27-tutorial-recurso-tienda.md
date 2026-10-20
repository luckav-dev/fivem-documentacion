[← 26-buenas-practicas](26-buenas-practicas.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [28-chuleta →](28-chuleta.md)

# 27. Tutorial completo: recurso "tienda" de principio a fin

Vamos a construir una tienda **standalone** con ox_lib + oxmysql que demuestra todo lo anterior: config, blips, puntos, menú, callback seguro, base de datos y logs.

## 27.1 Estructura

```
lx_tienda/
├── fxmanifest.lua
├── config.lua
├── client/main.lua
├── server/main.lua
├── locales/es.json
└── sql/install.sql
```

## 27.2 `fxmanifest.lua`

```lua
fx_version 'cerulean'
game 'gta5'

name 'lx_tienda'
author 'TuNombre'
description 'Tienda de ejemplo (ox_lib + oxmysql)'
version '1.0.0'

shared_scripts {
    '@ox_lib/init.lua',
    'config.lua',
}
client_script 'client/main.lua'
server_scripts {
    '@oxmysql/lib/MySQL.lua',
    'server/main.lua',
}
files { 'locales/*.json' }

dependencies { 'ox_lib', 'oxmysql', '/onesync' }
```

## 27.3 `config.lua`

```lua
Config = {}

Config.Tiendas = {
    { id = 'grove', nombre = '24/7 Grove Street', coords = vec3(-47.52, -1757.51, 29.42) },
    { id = 'vinewood', nombre = '24/7 Vinewood', coords = vec3(373.87, 325.89, 103.57) },
}

-- El servidor usa ESTOS precios, nunca los que envíe el cliente
Config.Productos = {
    agua = { label = 'Agua', precio = 5, icono = 'bottle-water' },
    pan  = { label = 'Pan',  precio = 3, icono = 'bread-slice' },
}

Config.DistanciaInteraccion = 2.0
```

## 27.4 `locales/es.json`

```json
{
  "abrir": "[E] Abrir %s",
  "comprar": "Comprar %s ($%s)",
  "cantidad": "Cantidad",
  "compra_ok": "Has comprado %sx %s por $%s",
  "sin_dinero": "No tienes suficiente dinero",
  "lejos": "Estás demasiado lejos de la tienda"
}
```

## 27.5 `sql/install.sql`

```sql
CREATE TABLE IF NOT EXISTS `lx_tienda_saldos` (
  `license` VARCHAR(60) NOT NULL,
  `dinero` INT NOT NULL DEFAULT 100,
  PRIMARY KEY (`license`)
);

CREATE TABLE IF NOT EXISTS `lx_tienda_compras` (
  `id` INT AUTO_INCREMENT PRIMARY KEY,
  `license` VARCHAR(60) NOT NULL,
  `producto` VARCHAR(50) NOT NULL,
  `cantidad` INT NOT NULL,
  `total` INT NOT NULL,
  `fecha` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  INDEX `idx_license` (`license`)
);
```

## 27.6 `client/main.lua`

```lua
lib.locale()

-- Blips
CreateThread(function()
    for _, t in ipairs(Config.Tiendas) do
        local blip = AddBlipForCoord(t.coords.x, t.coords.y, t.coords.z)
        SetBlipSprite(blip, 52)
        SetBlipColour(blip, 2)
        SetBlipScale(blip, 0.8)
        SetBlipAsShortRange(blip, true)
        BeginTextCommandSetBlipName('STRING')
        AddTextComponentSubstringPlayerName(t.nombre)
        EndTextCommandSetBlipName(blip)
    end
end)

local function comprar(tiendaId, productoId)
    local p = Config.Productos[productoId]
    local input = lib.inputDialog(p.label, {
        { type = 'number', label = locale('cantidad'), default = 1, min = 1, max = 20, required = true },
    })
    if not input then return end

    local ok, msg = lib.callback.await('lx_tienda:comprar', false, tiendaId, productoId, input[1])
    lib.notify({ description = msg, type = ok and 'success' or 'error' })
end

local function abrirTienda(tienda)
    local opciones = {}
    for id, p in pairs(Config.Productos) do
        opciones[#opciones + 1] = {
            title = locale('comprar', p.label, p.precio),
            icon = p.icono,
            onSelect = function() comprar(tienda.id, id) end,
        }
    end
    lib.registerContext({ id = 'lx_tienda_menu', title = tienda.nombre, options = opciones })
    lib.showContext('lx_tienda_menu')
end

-- Puntos de interacción (sin bucles Wait(0) permanentes)
for _, tienda in ipairs(Config.Tiendas) do
    local punto = lib.points.new({ coords = tienda.coords, distance = Config.DistanciaInteraccion })

    function punto:onEnter() lib.showTextUI(locale('abrir', tienda.nombre)) end
    function punto:onExit() lib.hideTextUI() end
    function punto:nearby()
        if IsControlJustReleased(0, 38) then abrirTienda(tienda) end
    end
end

AddEventHandler('onResourceStop', function(res)
    if res == GetCurrentResourceName() then lib.hideTextUI() end
end)
```

## 27.7 `server/main.lua`

```lua
lib.locale()

local Cooldown = {}
local Tiendas = {}
for _, t in ipairs(Config.Tiendas) do Tiendas[t.id] = t end

local function getLicense(src)
    return GetPlayerIdentifierByType(src, 'license')
end

local function getSaldo(license)
    local dinero = MySQL.scalar.await('SELECT dinero FROM lx_tienda_saldos WHERE license = ?', { license })
    if not dinero then
        MySQL.insert.await('INSERT INTO lx_tienda_saldos (license) VALUES (?)', { license })
        return 100
    end
    return dinero
end

lib.callback.register('lx_tienda:comprar', function(source, tiendaId, productoId, cantidad)
    local src = source

    -- 1. Tipos
    if type(tiendaId) ~= 'string' or type(productoId) ~= 'string' or type(cantidad) ~= 'number' then
        return false, 'Petición inválida'
    end
    cantidad = math.floor(cantidad)
    if cantidad < 1 or cantidad > 20 then return false, 'Cantidad inválida' end

    -- 2. Existen en la config del servidor
    local tienda, producto = Tiendas[tiendaId], Config.Productos[productoId]
    if not tienda or not producto then return false, 'Producto inválido' end

    -- 3. Cooldown
    local ahora = GetGameTimer()
    if Cooldown[src] and ahora - Cooldown[src] < 1000 then return false, 'Espera un momento' end
    Cooldown[src] = ahora

    -- 4. Distancia real (OneSync)
    local coords = GetEntityCoords(GetPlayerPed(src))
    if #(coords - tienda.coords) > Config.DistanciaInteraccion + 3.0 then
        print(('^3[lx_tienda] %s (%s) intentó comprar lejos de la tienda^7'):format(GetPlayerName(src), src))
        return false, locale('lejos')
    end

    -- 5. Dinero y compra (transacción atómica)
    local license = getLicense(src)
    local total = producto.precio * cantidad
    if getSaldo(license) < total then return false, locale('sin_dinero') end

    local ok = MySQL.transaction.await({
        { query = 'UPDATE lx_tienda_saldos SET dinero = dinero - ? WHERE license = ? AND dinero >= ?', values = { total, license, total } },
        { query = 'INSERT INTO lx_tienda_compras (license, producto, cantidad, total) VALUES (?, ?, ?, ?)', values = { license, productoId, cantidad, total } },
    })
    if not ok then return false, 'Error al procesar la compra' end

    -- Aquí darías el ítem con tu inventario, p. ej.:
    -- exports.ox_inventory:AddItem(src, productoId, cantidad)

    return true, locale('compra_ok', cantidad, producto.label, total)
end)

AddEventHandler('playerDropped', function() Cooldown[source] = nil end)

lib.versionCheck('tuusuario/lx_tienda')
```

## 27.8 Instalación

1. Copia `lx_tienda` en `resources/[scripts]/`.
2. Importa `sql/install.sql` en tu base de datos.
3. En `server.cfg`, **después** de `oxmysql` y `ox_lib`: `ensure lx_tienda`.
4. Entra al juego, ve al blip de la tienda y pulsa **E**.


---

[← 26-buenas-practicas](26-buenas-practicas.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [28-chuleta →](28-chuleta.md)
