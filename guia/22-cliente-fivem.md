[← 21-depuracion](21-depuracion.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [23-monetizacion-y-legal →](23-monetizacion-y-legal.md)

# 22. El cliente FiveM

## 22.1 Instalación

1. Descarga desde **https://fivem.net** (botón de descarga de FiveM).
2. Ejecuta `FiveM.exe`; se instalará en `%localappdata%\FiveM\`.
3. Al abrirlo te pedirá iniciar sesión con tu cuenta de Rockstar (verifica que tienes GTA V) y opcionalmente con tu cuenta Cfx.re.
4. Desde 2026 FiveM tiene su propia **Steam App ID** (Rich Presence y grupos de amigos en Steam).

## 22.2 Carpetas importantes

| Ruta | Contenido |
|---|---|
| `%localappdata%\FiveM\FiveM.app\` | Instalación del cliente. |
| `...\FiveM.app\CitizenFX.ini` | Configuración (ruta del juego, canal de actualización). |
| `...\FiveM.app\data\server-cache\` | Caché de recursos descargados de servidores. |
| `...\FiveM.app\data\cache\`, `server-cache-priv\`, `nui-storage\` | Otras cachés (NUI, archivos privados). |
| `...\FiveM.app\logs\` | Logs del cliente. |
| `...\FiveM.app\crashes\` | Volcados de *crash*. |
| `...\FiveM.app\plugins\` | Plugins gráficos permitidos (ReShade/ENB según `sv_pureLevel`). |
| `...\FiveM.app\mods\` | Mods locales (solo en servidores sin *pure mode*). |

**Limpiar caché** (soluciona muchos problemas de descarga/texturas): cierra FiveM y borra `data\cache`, `data\server-cache` y `data\server-cache-priv`. **No** borres `citizen` ni el resto de la carpeta. Borrar `caches.xml` soluciona algunos errores de descarga.

## 22.3 Opciones de lanzamiento

| Opción | Efecto |
|---|---|
| `FiveM.exe -b3407` | Lanza con una build concreta del juego. |
| `FiveM.exe -pure_1` | Fuerza *pure mode* nivel 1. |
| `FiveM.exe +set moo 31337` | Activa el modo desarrollador del cliente (comandos de depuración). |
| `fivem://connect/IP:PUERTO` | Conexión directa (también `fivem://connect/cfx.re/join/xxxx`). |

## 22.4 Comandos de consola del cliente (F8)

**Para todos:**

| Comando | Uso |
|---|---|
| `connect <ip:puerto \| cfx.re/join/xxxx>` | Conectarse. |
| `disconnect` | Desconectarse. |
| `quit` | Salir. |
| `cl_drawfps true` | Mostrar FPS. |
| `cl_drawperf true` | Estadísticas de rendimiento. |
| `bind keyboard F7 "comando"` / `rbind` / `unbind` | Asignar teclas a comandos. |
| `loadlevel` / `storymode` | Cargar mapas / modo historia (según disponibilidad). |

**De desarrollo** (pueden requerir modo desarrollador):

| Comando | Uso |
|---|---|
| `resmon 1` | Monitor de recursos. |
| `netgraph true` | Gráfico de red. |
| `strdbg`, `strlist`, `strmem` | Depuración de streaming. |
| `profiler record 500` / `profiler status` / `profiler view` / `profiler saveJSON x.json` | Perfilador. |
| `nui_devtools` | DevTools de NUI. |
| `netEventLog` | Registro de eventos de red. |
| `cl_drawResTimeGraphs` / `cl_drawResTimeWarnings` | Gráficas/avisos de tiempo por recurso. |
| `cmdlist` | Lista de comandos disponibles. |
| `save_gta_cache` | Guarda la caché del juego. |

La consola F8 tiene un **cuadro de filtro** (desde 2025) para buscar en la salida.

## 22.5 Nombres de jugador

Si el jugador no tiene otro nombre configurado, FiveM le asigna un nombre aleatorio tipo *"IcyGoose1337"* en lugar del nombre de usuario de Windows.

## 22.6 Problemas habituales del jugador

| Problema | Solución |
|---|---|
| "Could not find game executable" | Indica la ruta de GTA V en Ajustes o en `CitizenFX.ini`. |
| Errores de propiedad del juego | Abre el Rockstar Games Launcher e inicia sesión; verifica los archivos del juego. |
| *Crash* al entrar a un servidor concreto | Limpia la caché; prueba otra build; revisa la memoria (assets pesados). |
| Texturas que no cargan | Ajustes gráficos (calidad de texturas), cierra programas que usen VRAM, limpia caché. |
| No se oye la voz | Permisos de micrófono de Windows, dispositivo en Ajustes → Voz, tecla N por defecto. |
| "Server is running an outdated version" | El servidor usa artefactos sin soporte; debe actualizar a ≥ 35245. |


## Ver también (documentación offline)

- [Oficial: client-manual](../docs-oficiales/client-manual/README.md)
- [Oficial: client-manual/console-commands](../docs-oficiales/client-manual/console-commands.md)

---

[← 21-depuracion](21-depuracion.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [23-monetizacion-y-legal →](23-monetizacion-y-legal.md)
