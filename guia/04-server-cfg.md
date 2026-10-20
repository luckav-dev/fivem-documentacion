[← 03-instalacion-servidor](03-instalacion-servidor.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [05-comandos-y-convars →](05-comandos-y-convars.md)

# 4. `server.cfg` a fondo

El `server.cfg` es un archivo de **comandos de consola** que se ejecutan en orden al arrancar. Todo lo que pones ahí podrías escribirlo a mano en la consola del servidor.

## 4.1 `set`, `sets`, `setr` y `exec`

| Comando | Qué hace |
|---|---|
| `set nombre valor` | Define una **convar** solo en el servidor. |
| `sets nombre valor` | Define una convar **y la publica** en la lista de servidores (*server info*): tags, idioma, descripción… |
| `setr nombre valor` | Define una convar **replicada** a los clientes (se puede leer con `GetConvar` desde el cliente). |
| `exec archivo.cfg` | Ejecuta otro archivo `.cfg` (útil para separar permisos, secretos o recursos). Admite `@recurso/archivo.cfg`. |
| `#` o `//` | Comentarios. |

> **Nunca uses `setr` ni `sets` con secretos** (tokens, contraseñas, webhooks): los clientes o la lista pública podrían verlos. Usa `set`.

## 4.2 `server.cfg` completo y comentado

```cfg
## ======================================================
##  RED / PUERTOS
## ======================================================
endpoint_add_tcp "0.0.0.0:30120"
endpoint_add_udp "0.0.0.0:30120"

## ======================================================
##  IDENTIDAD DEL SERVIDOR (lista pública)
##  Desde el 21/10/2026 el nombre, la descripción, los tags, el banner y el
##  Discord que se ven en la lista se configuran en portal.cfx.re.
##  Mantén estas líneas igualmente (consola, txAdmin, recursos que las leen).
##  Límites: sv_projectName 40 caracteres, sv_hostname 120, sv_projectDesc 250.
## ======================================================
sv_hostname "^2Mi Servidor RP ^7| ^3Español ^7| Serious RP"
sets sv_projectName "Mi Servidor RP"
sets sv_projectDesc "Servidor de roleplay serio en español con economía realista."
sets tags "roleplay, rp, español, serious, economy"
sets locale "es-ES"
sets banner_detail "https://midominio.com/banner_detail.png"       # 1920x200 aprox.
sets banner_connecting "https://midominio.com/banner_connecting.png"
sets Discord "https://discord.gg/xxxx"
load_server_icon logo.png        # PNG 96x96 en la carpeta server-data

## ¿Mostrar candado de allowlist en la lista?
# sets sv_appearAllowlisted true
# sets sv_allowlistInstructions "Solicita acceso en nuestro Discord"

## ======================================================
##  LICENCIA / CLAVES
## ======================================================
sv_licenseKey "cfxk_XXXXXXXXXXXXXXXXXXXX_XXXXXX"
set steam_webApiKey "none"        # Pon tu API key de Steam si necesitas identificadores steam:

## ======================================================
##  JUGADORES / ONESYNC / BUILD
## ======================================================
sv_maxclients 48                  # >32 requiere OneSync; >64 requiere "onesync on"
set onesync on
sv_enforceGameBuild 3889          # The Kortz Center Heist (ver tabla de builds)
# set onesync_population true     # NPCs/tráfico (true por defecto)

## ======================================================
##  SEGURIDAD
## ======================================================
sv_scriptHookAllowed 0            # Nunca permitas ScriptHookV en servidores públicos
sv_endpointPrivacy true           # Oculta IPs de jugadores
sv_pureLevel 1                    # 0 = sin control; 1 = permite audio y gráficos conocidos; 2 = bloquea todo
set sv_entityLockdown relaxed     # inactive | relaxed | strict (ver sección 13)
set sv_filterRequestControl 2     # Bloquea robo de control de entidades de jugadores
setr sv_stateBagStrictMode false  # true = solo el servidor puede escribir state bags replicados
# rcon_password "xxxxx"           # Déjalo sin definir si no usas RCON
# sv_master1 ""                   # Servidor privado (oculta botón conectar; no lo quita de la lista)

## ======================================================
##  BASE DE DATOS (oxmysql)
## ======================================================
set mysql_connection_string "mysql://usuario:contraseña@127.0.0.1:3306/mi_base?charset=utf8mb4"
# Alternativa formato clave=valor:
# set mysql_connection_string "server=127.0.0.1;database=mi_base;userid=usuario;password=contraseña;charset=utf8mb4"
set mysql_slow_query_warning 200  # avisa de consultas lentas (ms)
# set mysql_ui true               # Interfaz /mysql (oxmysql)

## ======================================================
##  VOZ (pma-voice)
## ======================================================
setr voice_useNativeAudio true
setr voice_useSendingRangeOnly true
setr voice_defaultCycle "F11"

## ======================================================
##  RECURSOS (el ORDEN importa: dependencias primero)
## ======================================================
ensure mapmanager
ensure chat
ensure spawnmanager
ensure sessionmanager
ensure hardcap
ensure baseevents

ensure oxmysql
ensure ox_lib
# ensure es_extended   /  ensure qb-core  /  ensure qbx_core
ensure [framework]
ensure [ox]
ensure [scripts]
ensure [maps]
ensure [vehicles]

## ======================================================
##  PERMISOS (ver sección 6)
## ======================================================
add_ace group.admin command allow
add_ace group.admin command.quit deny
add_principal identifier.fivem:123456 group.admin
add_principal identifier.license:abcdef0123456789 group.admin

## Secretos en archivo aparte (añádelo a .gitignore)
exec secrets.cfg
```

`secrets.cfg` (no lo subas nunca al repositorio):

```cfg
sv_licenseKey "cfxk_..."
set mysql_connection_string "mysql://..."
set discord_bot_token "..."
```

## 4.3 Colores en el nombre del servidor

Códigos `^0`-`^9` (válidos en `sv_hostname`, chat y `print` de consola):

| Código | Color |
|---|---|
| `^0` | Blanco |
| `^1` | Rojo |
| `^2` | Verde |
| `^3` | Amarillo |
| `^4` | Azul |
| `^5` | Azul claro / cian |
| `^6` | Morado / violeta |
| `^7` | Blanco (reset) |
| `^8` | Rojo oscuro / naranja |
| `^9` | Gris / rosa (depende del contexto) |

> Desde febrero de 2026 la lista pública de servidores **no muestra los colores** del título y aplica límites de caracteres. Los colores siguen funcionando en la consola, el chat y `print`.

## 4.4 Orden de carga y dependencias

- Los recursos se arrancan **en el orden** en que aparecen los `ensure`.
- Si un recurso declara `dependency 'oxmysql'` en su manifest, FXServer intenta arrancar la dependencia antes; si no existe, el recurso **no arranca** (`Could not find dependency oxmysql for resource X`).
- Si un recurso usa exports de otro en el **primer tick** (al cargar el archivo), el otro debe estar arrancado antes.
- `ensure [categoria]` arranca **todo** lo que hay dentro, en orden alfabético de carpeta, después de resolver dependencias.


## Ver también (documentación offline)

- [Oficial: server-manual/server-commands](../docs-oficiales/server-manual/server-commands.md)
- [Oficial: scripting-reference/convars](../docs-oficiales/scripting-reference/convars/README.md)

---

[← 03-instalacion-servidor](03-instalacion-servidor.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [05-comandos-y-convars →](05-comandos-y-convars.md)
