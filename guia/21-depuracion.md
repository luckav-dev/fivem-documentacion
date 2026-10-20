[← 20-rendimiento](20-rendimiento.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [22-cliente-fivem →](22-cliente-fivem.md)

# 21. Depuración y errores comunes

## 21.1 Dónde mirar

| Lugar | Qué ves |
|---|---|
| **Consola del servidor** / *Live Console* de txAdmin | Errores de `server_scripts`, arranque de recursos, conexiones. |
| **F8** en el cliente | Errores de `client_scripts`, `print` del cliente. |
| **DevTools de NUI** (`nui_devtools`) | Errores de JavaScript y `console.log` de tus interfaces. |
| **Logs del cliente** | `%localappdata%\FiveM\FiveM.app\logs\CitizenFX_log_*.log` |
| **Crash dumps** | `%localappdata%\FiveM\FiveM.app\crashes\` (el cliente ofrece un código de crash para el soporte). |
| **txAdmin → Server Log / System Logs** | Historial de acciones, conexiones, muertes, chat, comandos. |

## 21.2 Leer un error de script

```
SCRIPT ERROR: @mi_recurso/client/main.lua:42: attempt to index a nil value (local 'data')
> handler (@mi_recurso/client/main.lua:42)
```

- `@mi_recurso/client/main.lua:42` → recurso, archivo y **línea**.
- `attempt to index a nil value (local 'data')` → intentaste acceder a `data.algo` cuando `data` era `nil`.
- Las líneas con `>` son la *traza* (de dónde venía la llamada).

## 21.3 Errores frecuentes y soluciones

| Error | Causa | Solución |
|---|---|---|
| `Couldn't find resource X` | La carpeta no existe, mal escrita o falta `refresh`. | Revisa el nombre (sensible a mayúsculas en Linux) y ejecuta `refresh`. |
| `Could not find dependency X for resource Y` | Falta un recurso del que depende. | Instálalo y arráncalo **antes**. |
| `Failed to load script X` | Ruta mal en `fxmanifest.lua` o error de sintaxis. | Revisa rutas/globs y la sintaxis. |
| `No such export X in resource Y` | El recurso Y no está arrancado, el nombre del export es incorrecto o cambió entre versiones. | Comprueba versión y `GetResourceState`. |
| `attempt to index a nil value` | Variable `nil` (jugador no cargado, item inexistente…). | Comprueba antes de usar: `if not x then return end` o `x?.campo`. |
| `attempt to call a nil value (global 'X')` | Función no definida, framework no cargado, orden de carga. | Revisa `shared_scripts` (`@ox_lib/init.lua`, `@es_extended/imports.lua`) y el orden de `ensure`. |
| `attempt to perform arithmetic on a string value` | Lua 5.4 no convierte strings en números. | `tonumber()`. |
| `bad argument #1 to 'X' (number expected, got nil)` | Pasaste `nil` a un native. | Valida argumentos. |
| `mysql_connection_string is not set` / `ER_ACCESS_DENIED_ERROR` | Cadena de conexión ausente o credenciales incorrectas. | Revisa `set mysql_connection_string` y los permisos del usuario SQL. |
| `ER_BAD_FIELD_ERROR` / `ER_NO_SUCH_TABLE` | Falta importar el `.sql` del recurso. | Importa el SQL incluido. |
| `You lack the required entitlement` | Recurso con Asset Escrow no asociado a tu clave. | Usa la clave de la cuenta que compró el recurso; no lo renombres. |
| `Server list query returned an error` / el servidor no aparece | Clave inválida, puertos cerrados, artefacto sin soporte. | Revisa `sv_licenseKey`, firewall, y que el artefacto sea ≥ 35245. |
| `Failed to verify server ownership` / *heartbeat* | La IP no coincide con la registrada en la clave. | Regenera la clave con la IP correcta en Portal. |
| `Pool full: X` / `Exhausted pool` | Demasiados assets de un tipo. | `increase_pool_size` (5.5) y optimiza. |
| `Oversized assets` en consola | Texturas/modelos demasiado grandes. | Optimiza (15.9). |
| `Connection timed out` / `Connection rejected` al entrar | Firewall, servidor saturado, *deferrals* sin `done()`. | Revisa puertos y que todo `defer()` termine en `done()`. |
| *Network event X was not safe for net* | El evento no está registrado con `RegisterNetEvent`. | Regístralo (si debe venir por red). |
| Jugador congelado con cursor | NUI con foco sin liberar. | `SetNuiFocus(false, false)` en todos los caminos de cierre. |
| `mono_rt2 is no longer supported` | Recurso C# con `mono_rt2` caducado. | Quita la línea `mono_rt2` y recompila para el runtime clásico. |

## 21.4 Técnicas de depuración

```lua
-- Modo debug controlado por convar
local DEBUG = GetConvar('mi_recurso_debug', 'false') == 'true'
local function dbg(...) if DEBUG then print('^3[DEBUG]^7', ...) end end

-- Ver tablas
print(json.encode(tabla, { indent = true }))
-- o con ox_lib
lib.print.info(tabla)

-- Medir cuánto tarda algo (SERVIDOR: la librería os solo existe en el servidor)
local t = os.nanotime()
HacerAlgoPesado()          -- tu función
print(('Tardó %.3f ms'):format((os.nanotime() - t) / 1e6))

-- Medir en el CLIENTE (resolución de milisegundos)
local t0 = GetGameTimer()
HacerAlgoPesado()
print(('Tardó %d ms'):format(GetGameTimer() - t0))
```

- Reinicia solo tu recurso con `ensure mi_recurso` (no hace falta reiniciar el servidor).
- Si un recurso de cliente no se actualiza, puede ser caché: `ensure` de nuevo o borra la caché del cliente.
- Usa un **servidor local de desarrollo** (`sv_lan true` o tu propia clave) con `sv_maxclients 2` y sin recursos innecesarios.


## Ver también (documentación offline)

- [Oficial: support](../docs-oficiales/support/README.md)
- [Oficial: support/server-issues](../docs-oficiales/support/server-issues.md)
- [Oficial: support/client-issues](../docs-oficiales/support/client-issues.md)
- [Oficial: support/server-debug](../docs-oficiales/support/server-debug.md)
- [Oficial: client-manual/enabling-full-client-dumps](../docs-oficiales/client-manual/enabling-full-client-dumps.md)

---

[← 20-rendimiento](20-rendimiento.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [22-cliente-fivem →](22-cliente-fivem.md)
