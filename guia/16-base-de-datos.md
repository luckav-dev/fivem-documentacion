[← 15-streaming-assets](15-streaming-assets.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [17-frameworks →](17-frameworks.md)

# 16. Base de datos (MariaDB + oxmysql)

## 16.1 Instalar MariaDB

**Versiones recomendadas (octubre 2026):**

| Serie | Tipo | Fin de soporte |
|---|---|---|
| **11.8** | LTS | febrero 2030 |
| **11.4** | LTS | mayo 2029 |
| 12.3 | LTS (nueva) | junio 2029 |
| 10.11 | LTS | febrero 2028 |
| 10.6 | LTS | **julio 2026 (ya sin soporte)** |

> Usa **MariaDB 11.4 LTS u 11.8 LTS**. Se desaconseja MySQL 8 (palabras reservadas como `group`, sin valores por defecto en columnas JSON/LONGTEXT) y **XAMPP** (versiones viejas, inseguro, no pensado para producción).

**Windows:** instalador MSI de https://mariadb.org/download → marca "Use UTF8 as default server's character set" → pon contraseña de root. Cliente gráfico: **HeidiSQL** (viene incluido; última versión 12.21).

**Linux (Debian/Ubuntu):**

```bash
# Repositorio oficial de MariaDB (elige la serie en https://mariadb.org/download/?t=repo-config)
sudo apt install mariadb-server
sudo mariadb-secure-installation
sudo mariadb
```

```sql
CREATE DATABASE fivem CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'fivem'@'localhost' IDENTIFIED BY 'una_contraseña_larga_y_segura';
GRANT ALL PRIVILEGES ON fivem.* TO 'fivem'@'localhost';
FLUSH PRIVILEGES;
```

> **Nunca** uses el usuario `root` para FiveM y **nunca** abras el puerto 3306 a Internet.

## 16.2 oxmysql: instalación y conexión

**oxmysql** (Overextended, v2.14.x) es el conector estándar de FiveM. Sustituye (y es compatible con) los antiguos `mysql-async` y `ghmattimysql`.

```cfg
# server.cfg (usa SET, nunca setr)
set mysql_connection_string "mysql://fivem:contraseña@127.0.0.1:3306/fivem?charset=utf8mb4"
# o formato clave=valor:
# set mysql_connection_string "user=fivem;password=contraseña;host=127.0.0.1;port=3306;database=fivem"

set mysql_slow_query_warning 150   # ms: avisa de consultas lentas
# set mysql_debug true             # registra todas las consultas (solo desarrollo)
# set mysql_ui true                # interfaz de consultas con el comando /mysql

ensure oxmysql                      # SIEMPRE antes que los recursos que lo usan
```

> Si la contraseña tiene caracteres como `; , / ? : @ & = + $ #`, usa el **otro** formato de cadena o cámbiala; romperán el formato URI.

En el manifest de tu recurso:

```lua
server_scripts {
    '@oxmysql/lib/MySQL.lua',
    'server/*.lua',
}
dependency 'oxmysql'
```

## 16.3 API de oxmysql (Lua)

Cada función tiene forma **`.await`** (síncrona dentro de un thread/handler) y forma con **callback**.

```lua
-- SELECT varias filas → array de filas
local filas = MySQL.query.await('SELECT * FROM vehiculos WHERE propietario = ?', { license })

-- Una sola fila → tabla o nil
local fila = MySQL.single.await('SELECT nombre, dinero FROM usuarios WHERE license = ? LIMIT 1', { license })

-- Un solo valor → valor o nil
local dinero = MySQL.scalar.await('SELECT dinero FROM usuarios WHERE license = ?', { license })

-- INSERT → id insertado
local id = MySQL.insert.await('INSERT INTO usuarios (license, nombre) VALUES (?, ?)', { license, nombre })

-- UPDATE/DELETE → filas afectadas
local n = MySQL.update.await('UPDATE usuarios SET dinero = dinero + ? WHERE license = ?', { 500, license })

-- Sentencia preparada en el servidor (solo placeholders ?), más rápida para consultas repetidas
local r = MySQL.prepare.await('SELECT dinero FROM usuarios WHERE license = ?', { license })

-- Transacción (todo o nada)
local ok = MySQL.transaction.await({
    { query = 'UPDATE usuarios SET dinero = dinero - ? WHERE license = ?', values = { 100, origen } },
    { query = 'UPDATE usuarios SET dinero = dinero + ? WHERE license = ?', values = { 100, destino } },
})

-- Forma con callback
MySQL.query('SELECT * FROM usuarios', {}, function(resultado)
    print(#resultado)
end)

-- Ejecutar SQL al arrancar (crear tablas)
MySQL.ready(function()
    MySQL.query([[
        CREATE TABLE IF NOT EXISTS mi_tabla (
            id INT AUTO_INCREMENT PRIMARY KEY,
            license VARCHAR(60) NOT NULL,
            datos LONGTEXT NULL,
            creado TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            INDEX idx_license (license)
        )
    ]])
end)
```

- Placeholders: usa **`?`** con un array de valores. Los placeholders con nombre (`@nombre`) están **obsoletos**.
- Para "insertar o actualizar" usa `INSERT ... ON DUPLICATE KEY UPDATE`.
- En JavaScript: `exports.oxmysql.query_async(sql, params)`, `single_async`, `scalar_async`, `insert_async`, `update_async`, `prepare_async`, `transaction_async`, o el paquete npm `@overextended/oxmysql`.

## 16.4 Buenas prácticas SQL en FiveM

- **Nunca concatenes** datos del jugador en el SQL (`'... WHERE nombre = "' .. nombre .. '"'`): **inyección SQL**. Usa siempre `?`.
- Crea **índices** en las columnas por las que filtras (`license`, `citizenid`, `identifier`, `plate`).
- No hagas consultas **por frame** ni dentro de bucles grandes; **cachea** en memoria y guarda periódicamente o al desconectar.
- Guarda datos de jugador en `playerDropped` **y** cada X minutos (por si el servidor se cae).
- Usa `utf8mb4` para soportar emojis y caracteres especiales.
- Para datos complejos (metadatos, inventarios), `LONGTEXT` con JSON o columnas `JSON` en MariaDB.
- Haz **backups** automáticos (`mariadb-dump` diario + rotación). txAdmin no hace copias de la BD por ti.

```bash
# Backup diario (cron) 
mariadb-dump -u fivem -p'contraseña' --single-transaction --routines fivem | gzip > /backups/fivem_$(date +%F).sql.gz
find /backups -name "fivem_*.sql.gz" -mtime +14 -delete
```

## 16.5 Patrón: caché de jugador + guardado

```lua
local Jugadores = {}  -- [src] = { license, dinero, ... }

local function cargar(src)
    local license = GetPlayerIdentifierByType(src, 'license')
    local fila = MySQL.single.await('SELECT * FROM usuarios WHERE license = ?', { license })
    if not fila then
        MySQL.insert.await('INSERT INTO usuarios (license, nombre, dinero) VALUES (?, ?, ?)', { license, GetPlayerName(src), 500 })
        fila = { license = license, dinero = 500 }
    end
    Jugadores[src] = fila
end

local function guardar(src)
    local p = Jugadores[src]
    if not p then return end
    MySQL.update.await('UPDATE usuarios SET dinero = ? WHERE license = ?', { p.dinero, p.license })
end

RegisterNetEvent('mi_core:jugadorListo', function() cargar(source) end)

AddEventHandler('playerDropped', function()
    local src = source
    guardar(src)
    Jugadores[src] = nil
end)

CreateThread(function()
    while true do
        Wait(5 * 60 * 1000)               -- cada 5 minutos
        for src in pairs(Jugadores) do guardar(src) end
    end
end)

AddEventHandler('onResourceStop', function(res)
    if res ~= GetCurrentResourceName() then return end
    for src in pairs(Jugadores) do guardar(src) end
end)
```


## Ver también (documentación offline)

- [Terceros: overextended](../docs-terceros/overextended/README.md)

---

[← 15-streaming-assets](15-streaming-assets.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [17-frameworks →](17-frameworks.md)
