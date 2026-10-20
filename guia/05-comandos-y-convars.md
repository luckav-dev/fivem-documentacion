[← 04-server-cfg](04-server-cfg.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [06-permisos-ace →](06-permisos-ace.md)

# 5. Comandos de consola y convars (referencia completa)

## 5.1 Comandos de recursos

| Comando | Descripción |
|---|---|
| `start <recurso>` | Arranca un recurso parado (acepta categoría). |
| `stop <recurso>` | Para un recurso (acepta categoría). |
| `ensure <recurso>` | Lo reinicia si está arrancado o lo arranca si no. **El más usado.** |
| `restart <recurso>` | Reinicia un recurso arrancado. |
| `refresh` | Reescanea `resources/` para detectar recursos nuevos o manifests modificados. |

## 5.2 Comandos globales y de gestión

| Comando | Descripción |
|---|---|
| `exec <archivo>` | Ejecuta un `.cfg`. |
| `quit [motivo]` | Apaga el servidor (con motivo opcional para los jugadores). |
| `status` | (rconlog) Lista jugadores: id, nombre, identificador, IP, ping. |
| `clientkick <id> <motivo>` | (rconlog) Expulsa a un jugador. |
| `say <mensaje>` | (chat) Mensaje en el chat como consola. |
| `svgui` | Muestra/oculta la interfaz de depuración del servidor (ImGui). |
| `profiler record <ticks>` / `profiler saveJSON <archivo>` | Perfilado del servidor (ver sección 21). |
| `con_addChannelFilter <filtro> <acción>` | Filtra canales de consola por regex (`noprint`, `drop`, `devonly`). |
| `con_removeChannelFilter <filtro> <acción>` | Quita un filtro. |
| `con_channelFilters` | Lista filtros activos. |
| `add_filesystem_permission <origen> <read\|write> <destino>` | Permite que el recurso `origen` lea o escriba archivos del recurso `destino` (por defecto solo puede escribir en sí mismo). Solo funciona en `server.cfg`, antes de que el servidor termine de arrancar. |
| `add_unsafe_worker_permission <recurso>` | Permite *worker threads* a un recurso JS. Misma restricción. |
| `add_unsafe_child_process_permission <recurso>` | Permite crear procesos hijo a un recurso JS. Misma restricción. Úsalo solo con recursos de confianza. |

## 5.3 Convars de configuración

### Red y listado

| Convar | Valores / defecto | Descripción |
|---|---|---|
| `endpoint_add_tcp "ip:puerto"` | — | Crea un endpoint TCP. |
| `endpoint_add_udp "ip:puerto"` | — | Crea un endpoint UDP. |
| `netPort <puerto>` | — | Puerto primario usado para el listado/master y DNS. |
| `sv_endpoints "<ip:puerto> ..."` | — | Direcciones UDP a las que se pueden conectar los clientes (se elige una al azar si hay varias). |
| `sv_hostname` | — | Nombre del servidor. |
| `sets sv_projectName` / `sv_projectDesc` | — | Nombre y descripción del proyecto en la lista. |
| `gametype` / `mapname` | — | Texto mostrado en la lista. |
| `sv_lan` | `false` | Modo LAN: oculto de la lista pública y sin comprobación de licencia. |
| `sv_master1 ""` | — | Hace el servidor privado (desactiva el botón de conectar). |
| `sv_forceIndirectListing` | `false` | Publica la IP del proxy/override en lugar de la real. |
| `sv_listingIpOverride` / `sv_listingHostOverride` | — | Sustituye IP/host enviados al master. |
| `sv_registerMulticastDns` | `true` | Anuncia el servidor por mDNS en LAN. |
| `sv_tcpConnectionTimeoutSeconds` | `5` | Timeout de conexiones TCP inactivas. |
| `net_tcpConnLimit` | `16` | Conexiones TCP simultáneas por IP. |
| `sv_proxyIPRanges "cidr ..."` | — | Rangos considerados proxy inverso (para obtener la IP real). |
| `sv_httpFileServerProxyOnly` | `false` | Solo permite descargas del servidor de archivos desde `sv_proxyIPRanges`. |
| `sv_endpointPrivacy` | — | Oculta IPs de jugadores en informes públicos. |
| `sv_maxClients` | 1-2048 | Slots. >32 requiere OneSync; >64 requiere `onesync on`. |

### OneSync

| Convar | Defecto | Descripción |
|---|---|---|
| `onesync` | `on` | `on` / `legacy` / `off`. |
| `onesync_enableInfinity` | `true` | Sincronización a gran escala (solo al arrancar). |
| `onesync_population` | `true` | Generación de NPCs/tráfico. |
| `onesync_forceMigration` | `true` | Transfiere la propiedad de entidades cuando el owner se va. |
| `onesync_distanceCulling` | `true` | No sincroniza entidades lejanas. |
| `onesync_distanceCullVehicles` | `false` | Aplica *culling* también a vehículos. |
| `onesync_radiusFrequency` | `true` | Actualiza más a menudo las entidades cercanas. |
| `sv_useAccurateSends` | `true` | Envíos de estado según relevancia y distancia. |
| `sv_experimentalStateBagsHandler` | `true` | Serialización más rápida de state bags. |
| `sv_experimentalOnesyncPopulation` | `true` | Corrige el límite de IDs con población desactivada. |
| `sv_experimentalNetGameEventHandler` | `true` | Serialización más rápida de *game events*. |

### Seguridad

| Convar | Defecto | Descripción |
|---|---|---|
| `sv_scriptHookAllowed` | `false` | Permite clientes con ScriptHookV. **No lo actives.** |
| `sv_pureLevel` | — | `1` = permite audio y mods gráficos conocidos; `2` = bloquea todo archivo modificado. |
| `sv_entityLockdown` | `inactive` | `strict` (clientes no crean entidades), `relaxed` (bloquea entidades de script creadas por cliente), `inactive`. |
| `sv_filterRequestControl` | `0` | Filtra `REQUEST_CONTROL_EVENT` (ver tabla abajo). |
| `sv_filterRequestControlSettleTimer` | `30000` | ms hasta que una entidad se considera "asentada". |
| `setr sv_stateBagStrictMode` | `false` | `true` = solo el servidor modifica state bags replicados. |
| `sv_enableNetworkedSounds` | `true` | Permite `NETWORK_PLAY_SOUND_EVENT`. |
| `sv_enableNetworkedPhoneExplosions` | `false` | Permite `REQUEST_PHONE_EXPLOSION_EVENT`. |
| `sv_enableNetworkedScriptEntityStates` | `true` | Permite `SCRIPT_ENTITY_STATE_CHANGE_EVENT`. |
| `sv_enableNetEventReassembly` | `true` | Reensambla eventos de red grandes divididos. |
| `sv_netEventReassemblyMaxPendingEvents` | `100` | Máx. eventos pendientes por cliente (0-254). |
| `sv_netEventReassemblyUnlimitedPendingEvents` | `false` | Elimina ese límite. |
| `sv_requestParanoia` | `0` | Contra *floods* HTTP vía proxy (ver tabla abajo). |
| `sv_authMaxVariance` | `5` | 1-5: probabilidad de que cambie un identificador del proveedor. |
| `sv_authMinTrust` | `1` | 1-5: dificultad para falsificar la identidad. |
| `rcon_password` | (vacío) | Activa RCON (UDP). Vacío = desactivado. |
| `block_net_game_event <nombre>` | — | Bloquea un *net game event* por nombre (necesita `sv_experimentalNetGameEventHandler`, activado por defecto). |
| `unblock_net_game_event <nombre>` | — | Lo desbloquea. |

**`sv_filterRequestControl`:**

| Modo | Efecto |
|---|---|
| `-1` | Como `2` pero además avisa en consola. |
| `0` | Desactivado (defecto). También desactiva la política de buckets/lockdown para estas peticiones. |
| `1` | Bloquea peticiones de control sobre entidades controladas por jugadores (vehículos ocupados) ya "asentadas". |
| `2` | Bloquea peticiones sobre **todas** las entidades controladas por jugadores. |
| `3` | Como `2` + entidades no-jugador asentadas. |
| `4` | Nunca enruta `REQUEST_CONTROL_EVENT`. |

Cualquier modo distinto de `0` bloquea también las peticiones entre *routing buckets* distintos.

**Limitadores de frecuencia (*rate limiters*)**: FXServer limita cuántos eventos y escrituras de state bags acepta de cada cliente. Valores por defecto en Legacy:

| Limitador | Tasa (por segundo) | Ráfaga |
|---|---|---|
| `netEvent` | 50 | 200 |
| `netEventFlood` | 75 | 300 |
| `stateBag` | 75 | 125 |
| `stateBagFlood` | 150 | 175 |
| `stateBagSize` | 128 KiB | 256 KiB |
| `http_info` | 4 | 10 |
| `http_players` | 4 | 10 |
| `http_perf` | 2 | 5 |

Se ajustan con `set rateLimiter_<nombre>_rate <n>` y `set rateLimiter_<nombre>_burst <n>`. Si un recurso legítimo supera los límites (por ejemplo, porque envía eventos en un bucle), **arregla el recurso** en vez de subir los límites. Desde abril de 2025 el servidor también avisa en consola (y en txAdmin) de los eventos demasiado grandes.

**`sv_requestParanoia`:**

| Nivel | Efecto |
|---|---|
| `0` | Desactivado. |
| `1` | Bloquea IPs cuyas peticiones incluyan cabecera `Via`. |
| `2` | Además bloquea las que incluyan `Upgrade-Insecure-Requests` (afecta también a abrir los `.json` desde navegador). |
| `3` | Como `2` y además cierra el socket. |

### Otros

| Convar | Defecto | Descripción |
|---|---|---|
| `gamename` | `gta5` | Juego objetivo (`gta5`/`rdr3`). |
| `sv_enforceGameBuild` | — | Build del juego (solo al arrancar). |
| `sv_replaceExeToSwitchBuilds` | — | **Obsoleta** desde el artefacto 35245 (el cliente usa siempre el ejecutable más reciente y solo carga los DLC de la build fijada). |
| `setr sv_showBusySpinnerOnLoadingScreen` | `true` | `false` oculta el icono de carga de la pantalla de carga (desde marzo de 2025). |
| `load_server_icon <png>` | — | Icono 96x96. |
| `steam_webApiKey` | — | Necesario para obtener `steam:`. |
| `steam_webApiDomain` | `api.steampowered.com` | Dominio de la API de Steam. |
| `sv_prometheusBasicAuthUser` / `Password` | — | Autenticación del endpoint `/perf` (métricas Prometheus). |
| `sv_kvsName` | `default` | Nombre del archivo de KVP del servidor (solo al arrancar). |
| `sv_tebexSecret` | — | Clave de Tebex para la integración. |
| `increase_pool_size <pool> <n>` | — | Aumenta un *pool* de memoria del juego (ver 5.5). |

## 5.4 Game builds (`sv_enforceGameBuild`)

Cada build incluye el contenido de todas las anteriores.

| Número | Alias | DLC (nombre comercial) |
|---|---|---|
| `1` | — | Juego base sin DLC |
| `1604` | `xm18`, `christmas2018`, `mpchristmas2018` | Arena War (**por defecto**) |
| `2060` | `sum`, `mpsum` | Los Santos Summer Special (incluye Diamond Casino & Resort y Diamond Casino Heist) |
| `2189` | `h4`, `heist4`, `mpheist4` | Cayo Perico Heist |
| `2372` | `tuner`, `mptuner` | Los Santos Tuners |
| `2545` | `security`, `mpsecurity` | The Contract |
| `2612` | `mpg9ec` | Contenido "Expanded & Enhanced" |
| `2699` | `mpsum2` | The Criminal Enterprises |
| `2802` | `mpchristmas3` | Los Santos Drug Wars |
| `2944` | `mp2023_01` | San Andreas Mercenaries |
| `3095` | `mp2023_02` | The Chop Shop |
| `3258` | `mp2024_01` | Bottom Dollar Bounties |
| `3407` | `mp2024_02` | Agents of Sabotage |
| `3570` | `mp2025_01` | Money Fronts |
| `3751` | `mp2025_02` | A Safehouse in the Hills |
| `3889` | `mp2026_01` | **The Kortz Center Heist** (la más reciente a octubre de 2026; requiere artefacto **35245 o superior**) |

Consejos:

- Usa **la última build** salvo que algún recurso tuyo no sea compatible.
- Cambiar de build obliga a los jugadores a descargar el contenido del DLC la primera vez.
- Algunas builds nuevas requieren artefactos recientes: si el servidor no reconoce la build, **actualiza los artefactos**.
- Natives, hashes de vehículos/ropa y offsets de *drawables* pueden variar entre builds: prueba todo tras cambiar.

## 5.5 Pools (`increase_pool_size`)

Si ves errores como `Pool full: TxdStore` o `Exhausted pool`, puedes ampliar el *pool* (solo al arrancar, en `server.cfg`):

```cfg
increase_pool_size "TxdStore" 2000
increase_pool_size "FragmentStore" 2000
increase_pool_size "CMoveObject" 100
```

| Pool | Aumento máximo (FiveM) |
|---|---|
| `AnimStore` | 20480 |
| `AttachmentExtension` | 430 |
| `Building` | 20000 |
| `CMoveObject` | 600 |
| `CWeaponComponentInfo` | 2048 |
| `EntityDescPool` | 20480 |
| `fragInstGta` | 2000 |
| `FragmentStore` | 14000 |
| `InteriorProxy` | 450 |
| `LightEntity` | 1000 |
| `netGameEvent` | 400 |
| `Object` | 2000 |
| `ObjectIntelligence` | 512 |
| `OcclusionInteriorInfo` | 20 |
| `OcclusionPathNode` | 5000 |
| `OcclusionPortalEntity` | 750 |
| `OcclusionPortalInfo` | 750 |
| `PortalInst` | 225 |
| `ScaleformStore` | 200 |
| `StaticBounds` | 5000 |
| `TxdStore` | 26000 |

> Ampliar pools aumenta el uso de memoria del cliente. Hazlo solo cuando un error concreto lo indique.


## Ver también (documentación offline)

- [Oficial: server-manual/server-commands](../docs-oficiales/server-manual/server-commands.md)
- [Oficial: scripting-reference/convars](../docs-oficiales/scripting-reference/convars/README.md)
- [Oficial: client-manual/console-commands](../docs-oficiales/client-manual/console-commands.md)

---

[← 04-server-cfg](04-server-cfg.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [06-permisos-ace →](06-permisos-ace.md)
