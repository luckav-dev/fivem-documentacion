# Overextended (ox_lib, oxmysql, ox_inventory, ox_target, ox_core, ox_doorlock, ox_fuel) — copia offline de la documentación

> Copia local en Markdown (GitHub Flavored Markdown) generada el 2026-10-20 para consulta sin conexión. El contenido de las páginas se mantiene en su idioma original (inglés), sin traducir ni resumir.

## Qué es

Documentación oficial de los recursos de **Overextended** para FiveM: la librería `ox_lib` (módulos reutilizables, interfaz, zonas, callbacks…), el conector de base de datos `oxmysql`, el inventario `ox_inventory`, el sistema de interacción `ox_target`, el framework `ox_core`, las puertas `ox_doorlock`, el combustible `ox_fuel`, además de guías de herramientas (Git, Node.js, Bun, tipos Lua). Sitio original: <https://overextended.dev/docs>.

## Origen y licencia

| Dato | Valor |
| --- | --- |
| Repositorio | [overextended/docs](https://github.com/overextended/docs) |
| Commit copiado | [`328e36f`](https://github.com/overextended/docs/tree/328e36feb5b0486d6214971f53c6d2626193cc28) (`328e36feb5b0486d6214971f53c6d2626193cc28`) |
| Fecha de copia | 2026-10-20 |
| Licencia | sin licencia explícita en el repositorio de documentación (no hay archivo LICENSE; el contenido pertenece a sus autores) |
| Archivos Markdown | 126 (0.4 MB) |
| Imágenes/recursos copiados | 39 (3.0 MB) en [`imagenes/`](imagenes/) |

Cada archivo empieza con una línea `> Fuente original: …` que enlaza el archivo exacto del repositorio en ese commit.

## Cómo se convirtió

- Origen: archivos MDX (Fumadocs) de `content/docs/`; se conserva la misma estructura de carpetas (`.mdx` → `.md`).
- `<Callout>` → cita con etiqueta en negrita (`> **Nota:**`, `> **Advertencia:**`, `> **Peligro:**`, `> **Consejo:**`).
- `<Tabs>`/`<Tab>` → subsecciones consecutivas encabezadas por el nombre de la pestaña en negrita (p. ej. **Lua**, **JS**).
- Encabezados con `[step]` → encabezados numerados (`### 1. …`).
- `<Cards>` dinámicas (generadas a partir del árbol de páginas) → listas de enlaces a las páginas hermanas.
- `<include>` → se inserta el contenido de la página incluida (indicándolo con una línea en cursiva).
- `<ResourceLinks>`, `GhButton`, `NpmButton` → enlaces normales (GitHub / descarga / npm).
- `CreatorCodes(...)` → tabla con los códigos de creador (en el sitio original el orden es aleatorio).
- Banners visuales (`<div style=…>` con logo de fondo) → enlace en negrita; el logo de fondo no se conserva.
- Los enlaces internos se reescribieron como rutas relativas a los `.md` generados (con `#ancla` cuando existe); los enlaces externos se mantienen.
- Bloques de código copiados literalmente con su etiqueta de lenguaje; tablas conservadas.
- Imágenes referenciadas (del repositorio y externas descargables) copiadas a `imagenes/` (máx. 5 MB por archivo y ~40 MB por proyecto; las del repositorio tienen prioridad). Las externas se guardan en `imagenes/externas/<dominio>/`.

## Recursos omitidos

Ninguno: todas las imágenes referenciadas se copiaron.

## Observaciones y contenido no convertido

- ox_inventory/Functions/Server/index.md: enlace roto en el original `./GetInventory.md` redirigido al ancla #getinventory del mismo archivo
- ox_target/Functions/Client.md: ancla obsoleta `#libzonessphere` del original redirigida a `#sphere-zone`
- ox_target/Functions/Client.md: ancla obsoleta `#libzonesbox` del original redirigida a `#box-zone`
- ox_target/Functions/Client.md: ancla obsoleta `#libzonespoly` del original redirigida a `#polygonprism-zone`
- Componentes puramente visuales eliminados: logotipos de fondo de los banners (Fivemanage, Prism Host) y estilos.
- Las páginas `meta.json`/`_category_.yml` (orden del menú lateral del sitio) no se convierten; el índice sigue el orden alfabético.

## Índice de archivos

### Raíz

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [index.md](index.md) | Documentation | Portada de la documentación: enlaces a recursos para desarrolladores y códigos de creador de Tebex. |

### `guides/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [guides/bun.md](guides/bun.md) | Bun | Guía para instalar Bun como gestor de paquetes/entorno de ejecución. |
| [guides/git.md](guides/git.md) | Git | Guía para instalar y configurar Git. |
| [guides/index.md](guides/index.md) | Resources | Índice de las guías de herramientas (Git, Node.js, Bun, tipos Lua). |
| [guides/lua-types.md](guides/lua-types.md) | Lua Types | Pasos para tener autocompletado y anotaciones de tipos en Lua (LLS, fivem-lls-addon, ox_types). |
| [guides/nodejs.md](guides/nodejs.md) | Node.js | Guía para instalar Node.js (necesario para compilar interfaces web). |

### `ox_core/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [ox_core/Classes/Client/OxPlayer.md](ox_core/Classes/Client/OxPlayer.md) | OxPlayer | ox_core › clases › cliente › OxPlayer. Contiene: `OxPlayer`, `OxPlayer.addStatus`, `OxPlayer.get`, `OxPlayer.getCoords`, `OxPlayer.getGroup` y 7 más. |
| [ox_core/Classes/Server/OxAccount.md](ox_core/Classes/Server/OxAccount.md) | OxAccount | ox_core › clases › servidor › OxAccount. Contiene: `OxAccount`, `OxAccountMetadata`, `OxAccount.get`, `OxAccount.addBalance`, `OxAccount.removeBalance` y 9 más. |
| [ox_core/Classes/Server/OxPlayer.md](ox_core/Classes/Server/OxPlayer.md) | OxPlayer | ox_core › clases › servidor › OxPlayer. Contiene: `OxPlayer`, `OxPlayer.addLicense`, `OxPlayer.addStatus`, `OxPlayer.createCharacter`, `OxPlayer.deleteCharacter` y 23 más. |
| [ox_core/Classes/Server/OxVehicle.md](ox_core/Classes/Server/OxVehicle.md) | OxVehicle | ox_core › clases › servidor › OxVehicle. Contiene: `OxVehicle`, `OxVehicle.delete`, `OxVehicle.despawn`, `OxVehicle.get`, `OxVehicle.getCoords` y 11 más. |
| [ox_core/Events/client.md](ox_core/Events/client.md) | Client Events | ox_core › eventos › cliente. Contiene: `ox:playerLoaded`, `ox:statusTick`, `ox:playerDeath`, `ox:playerRevived`, `ox:setGroup` y 4 más. |
| [ox_core/Events/server.md](ox_core/Events/server.md) | Server Events | ox_core › eventos › servidor. Contiene: `ox:savedPlayers`, `ox:setActiveGroup`, `ox:setGroup`, `ox:licenseAdded`, `ox:licenseRemoved` y 12 más. |
| [ox_core/Functions/common.md](ox_core/Functions/common.md) | Common | ox_core › funciones › comunes. Contiene: `Ox.GetGroupPermissions`, `Ox.GetTopVehicleStats`, `Ox.GetVehicleData`, `Ox.GetVehicleNetworkType`. |
| [ox_core/Functions/server.md](ox_core/Functions/server.md) | Server | ox_core › funciones › servidor. Contiene: `Ox.CreateAccount`, `Ox.CreateGroup`, `Ox.CreateVehicle`, `Ox.DeleteAccountInvoice`, `Ox.DeleteGroup` y 30 más. |
| [ox_core/index.md](ox_core/index.md) | Ox Core | Introducción a ox_core: receta de txAdmin, instalación, uso con Lua/TypeScript y configuración. |
| [ox_core/States.md](ox_core/States.md) | Global States | Estados globales (GlobalState) que expone ox_core. |

### `ox_doorlock/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [ox_doorlock/Client/functions.md](ox_doorlock/Client/functions.md) | Functions | ox_doorlock › cliente › funciones. Contiene: `pickClosestDoor`, `useClosestDoor`, `getClosestDoor`. |
| [ox_doorlock/index.md](ox_doorlock/index.md) | Ox Doorlock | Introducción a ox_doorlock: instalación, uso y creación de puertas. |
| [ox_doorlock/Server/events.md](ox_doorlock/Server/events.md) | Events | ox_doorlock › servidor › eventos. Contiene: `ox_doorlock:stateChanged`. |
| [ox_doorlock/Server/functions/Hooks.md](ox_doorlock/Server/functions/Hooks.md) | Hooks | ox_doorlock › servidor › funciones › hooks. Contiene: `doorAuthorization`. |
| [ox_doorlock/Server/functions/index.md](ox_doorlock/Server/functions/index.md) | Functions | ox_doorlock › servidor › funciones. Contiene: `getDoor`, `getDoorFromName`, `editDoor`, `setDoorState`. |
| [ox_doorlock/settings.md](ox_doorlock/settings.md) | Door Settings | Ajustes configurables de cada puerta. |

### `ox_fuel/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [ox_fuel/Client/functions.md](ox_fuel/Client/functions.md) | Functions | ox_fuel › cliente › funciones. Contiene: `Parameters`, `Example`. |
| [ox_fuel/index.md](ox_fuel/index.md) | Ox Fuel | Introducción a ox_fuel: instalación y configuración. |
| [ox_fuel/Server/functions.md](ox_fuel/Server/functions.md) | Functions | ox_fuel › servidor › funciones. Contiene: `Parameters`, `Example`. |
| [ox_fuel/Shared.md](ox_fuel/Shared.md) | Shared | ox_fuel › compartido. Contiene: `Get vehicle fuel amount`, `Set vehicle fuel amount`. |

### `ox_inventory/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [ox_inventory/Events/Client.md](ox_inventory/Events/Client.md) | Client | ox_inventory › eventos › cliente. Contiene: `ox_inventory:disarm`, `ox_inventory:suppressItemNotifications`, `ox_inventory:updateInventory`, `ox_inventory:currentWeapon`, `ox_inventory:itemCount` y 2 más. |
| [ox_inventory/Events/Server.md](ox_inventory/Events/Server.md) | Server | ox_inventory › eventos › servidor. Contiene: `ox_inventory:openedInventory`, `ox_inventory:closedInventory`, `ox_inventory:usedItem`. |
| [ox_inventory/Frameworks/esx.md](ox_inventory/Frameworks/esx.md) | ESX | Integración de ox_inventory con ESX. |
| [ox_inventory/Frameworks/qbx.md](ox_inventory/Frameworks/qbx.md) | Qbox | Integración de ox_inventory con Qbox. |
| [ox_inventory/Functions/Client.md](ox_inventory/Functions/Client.md) | Client | ox_inventory › funciones › cliente. Contiene: `openInventory`, `useItem`, `useSlot`, `setStashTarget`, `getCurrentWeapon` y 15 más. |
| [ox_inventory/Functions/Server/Hooks.md](ox_inventory/Functions/Server/Hooks.md) | Hooks | ox_inventory › funciones › servidor › hooks. Contiene: `registerHook`, `removeHooks`, `Post-hook events`. |
| [ox_inventory/Functions/Server/index.md](ox_inventory/Functions/Server/index.md) | Server | ox_inventory › funciones › servidor. Contiene: `setPlayerInventory`, `forceOpenInventory`, `UpdateVehicle`, `Items`, `AddItem` y 36 más. |
| [ox_inventory/Guides/crafting.md](ox_inventory/Guides/crafting.md) | Crafting | Guía para crear bancos de crafteo. |
| [ox_inventory/Guides/creatingItems.md](ox_inventory/Guides/creatingItems.md) | Creating Items | Guía para crear ítems (definición, uso, contenedores, armas). |
| [ox_inventory/Guides/metadata.md](ox_inventory/Guides/metadata.md) | Metadata | Guía de uso de metadatos en ítems. |
| [ox_inventory/Guides/shops.md](ox_inventory/Guides/shops.md) | Creating Shops | Guía para crear tiendas. |
| [ox_inventory/Guides/stashes.md](ox_inventory/Guides/stashes.md) | Custom Stashes | Guía para registrar alijos (stashes) personalizados. |
| [ox_inventory/index.md](ox_inventory/index.md) | Ox Inventory | Introducción a ox_inventory: requisitos, instalación, configuración y compatibilidad. |
| [ox_inventory/issues.md](ox_inventory/issues.md) | Common Issues | Problemas comunes de ox_inventory y sus soluciones. |

### `ox_lib/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [ox_lib/ACL/Server.md](ox_lib/ACL/Server.md) | Server | Módulo `ACL` de ox_lib (servidor). Contiene: `lib.addAce`, `lib.removeAce`, `lib.addPrincipal`, `lib.removePrincipal`. |
| [ox_lib/AddCommand/Server.md](ox_lib/AddCommand/Server.md) | Server | Módulo `AddCommand` de ox_lib (servidor). |
| [ox_lib/AddKeybind/Client.md](ox_lib/AddKeybind/Client.md) | Client | Módulo `AddKeybind` de ox_lib (cliente). Contiene: `Enable / Disable Keybinds`, `Keybind pressed states`. |
| [ox_lib/Array/Shared.md](ox_lib/Array/Shared.md) | Shared | Módulo `Array` de ox_lib (compartido). Contiene: `lib.array:new`, `lib.array.from`, `lib.array.at`, `lib.array.merge`, `lib.array.every` y 17 más. |
| [ox_lib/Cache/Client.md](ox_lib/Cache/Client.md) | Client | Módulo `Cache` de ox_lib (cliente). Contiene: `Default values`, `lib.onCache`. |
| [ox_lib/Cache/Shared.md](ox_lib/Cache/Shared.md) | Shared | Módulo `Cache` de ox_lib (compartido). Contiene: `Default values`, `Adding new cached values`. |
| [ox_lib/Callback/JavaScript/Client.md](ox_lib/Callback/JavaScript/Client.md) | Client | Módulo `Callback` de ox_lib (JavaScript › cliente). Contiene: `Trigger Server Callback`, `Register Client Callback`, `Usage Example`. |
| [ox_lib/Callback/JavaScript/Server.md](ox_lib/Callback/JavaScript/Server.md) | Server | Módulo `Callback` de ox_lib (JavaScript › servidor). Contiene: `Trigger Client Callback`, `Register Server Callback`, `Usage Example`. |
| [ox_lib/Callback/Lua/Client.md](ox_lib/Callback/Lua/Client.md) | Client | Módulo `Callback` de ox_lib (Lua › cliente). Contiene: `lib.callback`, `lib.callback.await`, `lib.callback.register`. |
| [ox_lib/Callback/Lua/Server.md](ox_lib/Callback/Lua/Server.md) | Server | Módulo `Callback` de ox_lib (Lua › servidor). Contiene: `lib.callback`, `lib.callback.await`, `lib.callback.register`. |
| [ox_lib/Class/Shared.md](ox_lib/Class/Shared.md) | Shared | Módulo `Class` de ox_lib (compartido). Contiene: `Classes`, `OxClass`, `lib.class`. |
| [ox_lib/Cron/Server.md](ox_lib/Cron/Server.md) | Server | Módulo `Cron` de ox_lib (servidor). Contiene: `* Wildcards`, `, Lists`, `- Ranges`, `/ Steps`, `lib.cron.new`. |
| [ox_lib/DisableControls/Client.md](ox_lib/DisableControls/Client.md) | Client | Módulo `DisableControls` de ox_lib (cliente). Contiene: `lib.disableControls`, `lib.disableControls:Add`, `lib.disableControls:Remove`, `lib.disableControls:Clear`. |
| [ox_lib/Dui/Javascript/Client.md](ox_lib/Dui/Javascript/Client.md) | Client | Módulo `Dui` de ox_lib (JavaScript › cliente). Contiene: `Usage Example`. |
| [ox_lib/Dui/Lua/Client.md](ox_lib/Dui/Lua/Client.md) | Client | Módulo `Dui` de ox_lib (Lua › cliente). Contiene: `Usage Example`. |
| [ox_lib/GameEntity.md](ox_lib/GameEntity.md) | GameEntity | Métodos comunes de entidades (clase base usada por Ped, Prop, Vehicle y Player). |
| [ox_lib/GetClosestObject/Shared.md](ox_lib/GetClosestObject/Shared.md) | Shared | Módulo `GetClosestObject` de ox_lib (compartido). Contiene: `lib.getClosestObject`. |
| [ox_lib/GetClosestPed/Shared.md](ox_lib/GetClosestPed/Shared.md) | Shared | Módulo `GetClosestPed` de ox_lib (compartido). Contiene: `lib.getClosestPed`. |
| [ox_lib/GetClosestPlayer/Client.md](ox_lib/GetClosestPlayer/Client.md) | Client | Módulo `GetClosestPlayer` de ox_lib (cliente). Contiene: `lib.getClosestPlayer`. |
| [ox_lib/GetClosestPlayer/Server.md](ox_lib/GetClosestPlayer/Server.md) | Server | Módulo `GetClosestPlayer` de ox_lib (servidor). Contiene: `lib.getClosestPlayer`. |
| [ox_lib/GetClosestVehicle/Shared.md](ox_lib/GetClosestVehicle/Shared.md) | Shared | Módulo `GetClosestVehicle` de ox_lib (compartido). Contiene: `lib.getClosestVehicle`. |
| [ox_lib/GetFilesInDirectory/Server.md](ox_lib/GetFilesInDirectory/Server.md) | Server | Módulo `GetFilesInDirectory` de ox_lib (servidor). Contiene: `lib.getFilesInDirectory`. |
| [ox_lib/GetNearbyObjects/Shared.md](ox_lib/GetNearbyObjects/Shared.md) | Shared | Módulo `GetNearbyObjects` de ox_lib (compartido). Contiene: `lib.getNearbyObjects`. |
| [ox_lib/GetNearbyPeds/Shared.md](ox_lib/GetNearbyPeds/Shared.md) | Shared | Módulo `GetNearbyPeds` de ox_lib (compartido). Contiene: `lib.getNearbyPeds`. |
| [ox_lib/GetNearbyPlayers/Shared.md](ox_lib/GetNearbyPlayers/Shared.md) | Shared | Módulo `GetNearbyPlayers` de ox_lib (compartido). Contiene: `lib.getNearbyPlayers`. |
| [ox_lib/GetNearbyVehicles/JavaScript/Shared.md](ox_lib/GetNearbyVehicles/JavaScript/Shared.md) | Shared | Módulo `GetNearbyVehicles` de ox_lib (JavaScript › compartido). Contiene: `getNearbyVehicles`. |
| [ox_lib/GetNearbyVehicles/Lua/Shared.md](ox_lib/GetNearbyVehicles/Lua/Shared.md) | Shared | Módulo `GetNearbyVehicles` de ox_lib (Lua › compartido). Contiene: `lib.getNearbyVehicles`. |
| [ox_lib/Grid/Shared.md](ox_lib/Grid/Shared.md) | Shared | Módulo `Grid` de ox_lib (compartido). Contiene: `GridEntry Class`, `lib.grid.getCellPosition`, `lib.grid.getCell`, `lib.grid.getNearbyEntries`, `lib.grid.addEntry` y 1 más. |
| [ox_lib/Hooks.md](ox_lib/Hooks.md) | Hooks | Sistema de hooks de ox_lib (registro y ejecución de hooks). |
| [ox_lib/index.md](ox_lib/index.md) | Ox Lib | Introducción a ox_lib: instalación, convars, uso desde Lua/JS, iconos y compilación de la UI. |
| [ox_lib/Interface/Client/alert.md](ox_lib/Interface/Client/alert.md) | Alert Dialog | ox_lib › interfaz (cliente): Alert Dialog. Contiene: `lib.alertDialog`, `lib.closeAlertDialog`, `Example`. |
| [ox_lib/Interface/Client/clipboard.md](ox_lib/Interface/Client/clipboard.md) | Clipboard | ox_lib › interfaz (cliente): Clipboard. Contiene: `lib.setClipboard`. |
| [ox_lib/Interface/Client/context.md](ox_lib/Interface/Client/context.md) | Context Menu | ox_lib › interfaz (cliente): Context Menu. Contiene: `lib.registerContext`, `lib.showContext`, `lib.hideContext`, `lib.getOpenContextMenu`, `Usage Example`. |
| [ox_lib/Interface/Client/index.md](ox_lib/Interface/Client/index.md) | Interface | Índice de los componentes de interfaz de ox_lib (lado cliente). |
| [ox_lib/Interface/Client/input.md](ox_lib/Interface/Client/input.md) | Input Dialog | ox_lib › interfaz (cliente): Input Dialog. Contiene: `lib.inputDialog`, `lib.closeInputDialog`, `Usage Example`. |
| [ox_lib/Interface/Client/menu.md](ox_lib/Interface/Client/menu.md) | Menu | ox_lib › interfaz (cliente): Menu. Contiene: `lib.registerMenu`, `lib.showMenu`, `lib.hideMenu`, `lib.getOpenMenu`, `lib.setMenuOptions` y 1 más. |
| [ox_lib/Interface/Client/notify.md](ox_lib/Interface/Client/notify.md) | Notifications | ox_lib › interfaz (cliente): Notifications. Contiene: `Standard`, `Custom`. |
| [ox_lib/Interface/Client/progress.md](ox_lib/Interface/Client/progress.md) | Progress | ox_lib › interfaz (cliente): Progress. Contiene: `lib.progressBar`, `lib.progressCircle`, `lib.progressActive`, `lib.cancelProgress`. |
| [ox_lib/Interface/Client/radial.md](ox_lib/Interface/Client/radial.md) | Radial Menu | ox_lib › interfaz (cliente): Radial Menu. Contiene: `lib.addRadialItem`, `lib.removeRadialItem`, `lib.clearRadialItems`, `lib.registerRadial`, `lib.showRadialMenu` y 4 más. |
| [ox_lib/Interface/Client/skillcheck.md](ox_lib/Interface/Client/skillcheck.md) | Skill Check | ox_lib › interfaz (cliente): Skill Check. Contiene: `lib.skillCheck`, `lib.skillCheckActive`, `lib.cancelSkillCheck`, `Usage Example`. |
| [ox_lib/Interface/Client/textui.md](ox_lib/Interface/Client/textui.md) | TextUI | ox_lib › interfaz (cliente): TextUI. Contiene: `lib.showTextUI`, `lib.hideTextUI`, `lib.isTextUIOpen`, `Usage Example`. |
| [ox_lib/Locale/Shared.md](ox_lib/Locale/Shared.md) | Shared | Módulo `Locale` de ox_lib (compartido). Contiene: `Setup`, `Usage`, `Phrases`, `lib.getLocale`. |
| [ox_lib/Logger/Server.md](ox_lib/Logger/Server.md) | Server | Módulo `Logger` de ox_lib (servidor). Contiene: `lib.logger`, `Datadog`, `Grafana Loki`, `Fivemanage`. |
| [ox_lib/Marker/Client.md](ox_lib/Marker/Client.md) | Client | Módulo `Marker` de ox_lib (cliente). Contiene: `lib.marker`, `Marker Class`, `lib.marker.new`. |
| [ox_lib/Math/Shared.md](ox_lib/Math/Shared.md) | Shared | Módulo `Math` de ox_lib (compartido). Contiene: `math.toscalars`, `math.tovector`, `math.normaltorotation`, `math.torgba`, `math.hextorgb` y 6 más. |
| [ox_lib/Ped.md](ox_lib/Ped.md) | Ped | Clase `Ped` de ox_lib (constructor y métodos). |
| [ox_lib/PlayAnim/Client.md](ox_lib/PlayAnim/Client.md) | Client | Módulo `PlayAnim` de ox_lib (cliente). Contiene: `lib.playAnim`. |
| [ox_lib/Player.md](ox_lib/Player.md) | Player | Clase `Player` de ox_lib (constructor y métodos, incluye los de Ped). |
| [ox_lib/Points/JavaScript/Client.md](ox_lib/Points/JavaScript/Client.md) | Client | Módulo `Points` de ox_lib (JavaScript › cliente). Contiene: `Points`. |
| [ox_lib/Points/Lua/Client.md](ox_lib/Points/Lua/Client.md) | Client | Módulo `Points` de ox_lib (Lua › cliente). Contiene: `CPoint Class`, `lib.points.new`, `lib.points.getAllPoints`, `lib.points.getNearbyPoints`, `lib.points.getClosestPoint`. |
| [ox_lib/Print/Shared.md](ox_lib/Print/Shared.md) | Shared | Módulo `Print` de ox_lib (compartido). Contiene: `Example`, `Levels`, `Config`. |
| [ox_lib/Prop.md](ox_lib/Prop.md) | Prop | Clase `Prop` de ox_lib (constructor y métodos). |
| [ox_lib/Raycast/Client.md](ox_lib/Raycast/Client.md) | Client | Módulo `Raycast` de ox_lib (cliente). Contiene: `lib.raycast.fromCoords`, `lib.raycast.fromCamera`, `lib.raycast.cam`. |
| [ox_lib/Require/Shared.md](ox_lib/Require/Shared.md) | Shared | Módulo `Require` de ox_lib (compartido). Contiene: `require`, `lib.load`, `lib.loadJson`. |
| [ox_lib/Scaleform/Client.md](ox_lib/Scaleform/Client.md) | Client | Módulo `Scaleform` de ox_lib (cliente). Contiene: `Usage Example`. |
| [ox_lib/Selector/Shared.md](ox_lib/Selector/Shared.md) | Shared | Módulo `Selector` de ox_lib (compartido). Contiene: `OxSelector Class`, `lib.selector`, `OxSelector:getRandom`, `OxSelector:getRandomWeighted`, `OxSelector:getRandomAmount` y 7 más. |
| [ox_lib/Streaming/Client.md](ox_lib/Streaming/Client.md) | Client | Módulo `Streaming` de ox_lib (cliente). Contiene: `lib.requestAnimDict`, `lib.requestAnimSet`, `lib.requestAudioBank`, `lib.requestModel`, `lib.requestStreamedTextureDict` y 3 más. |
| [ox_lib/String/Shared.md](ox_lib/String/Shared.md) | Shared | Módulo `String` de ox_lib (compartido). Contiene: `string.random`. |
| [ox_lib/Table/Shared.md](ox_lib/Table/Shared.md) | Shared | Módulo `Table` de ox_lib (compartido). Contiene: `lib.table.contains`, `lib.table.matches`, `lib.table.deepclone`, `lib.table.merge`, `lib.table.freeze` y 1 más. |
| [ox_lib/Timer/Shared.md](ox_lib/Timer/Shared.md) | Shared | Módulo `Timer` de ox_lib (compartido). Contiene: `lib.timer`, `pause`, `play`, `forceEnd`, `isPaused` y 2 más. |
| [ox_lib/Vehicle.md](ox_lib/Vehicle.md) | Vehicle | Clase `Vehicle` de ox_lib (constructor y métodos). |
| [ox_lib/VehicleProperties/Client.md](ox_lib/VehicleProperties/Client.md) | Client | Módulo `VehicleProperties` de ox_lib (cliente). Contiene: `lib.getVehicleProperties`, `lib.setVehicleProperties`, `Vehicle Properties`. |
| [ox_lib/Version/Server.md](ox_lib/Version/Server.md) | Server | Módulo `Version` de ox_lib (servidor). Contiene: `lib.versionCheck`. |
| [ox_lib/Version/Shared.md](ox_lib/Version/Shared.md) | Shared | Módulo `Version` de ox_lib (compartido). Contiene: `lib.checkDependency`. |
| [ox_lib/WaitFor/Shared.md](ox_lib/WaitFor/Shared.md) | Shared | Módulo `WaitFor` de ox_lib (compartido). Contiene: `lib.waitFor`. |
| [ox_lib/Zones/Shared.md](ox_lib/Zones/Shared.md) | Shared | Módulo `Zones` de ox_lib (compartido). Contiene: `Polygon/Prism Zone`, `Box Zone`, `Sphere Zone`, `Methods`, `Utility Functions` y 2 más. |

### `ox_target/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [ox_target/Functions/Client.md](ox_target/Functions/Client.md) | Client | ox_target › funciones › cliente. Contiene: `disableTargeting`, `isActive`, `getTargetOptions`, `addGlobalOption`, `removeGlobalOption` y 19 más. |
| [ox_target/index.md](ox_target/index.md) | Ox Target | Introducción a ox_target: instalación, convars y compatibilidad. |
| [ox_target/TargetOptions.md](ox_target/TargetOptions.md) | TargetOptions | Opciones disponibles al definir objetivos de ox_target. |

### `oxmysql/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [oxmysql/benchmark.md](oxmysql/benchmark.md) | Benchmark | Comparativa de rendimiento de oxmysql. |
| [oxmysql/Functions/insert.md](oxmysql/Functions/insert.md) | insert | Función `insert` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/Functions/prepare.md](oxmysql/Functions/prepare.md) | Prepare | Función `prepare` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/Functions/query.md](oxmysql/Functions/query.md) | Query | Función `query` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/Functions/rawExecute.md](oxmysql/Functions/rawExecute.md) | RawExecute | Función `rawExecute` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/Functions/scalar.md](oxmysql/Functions/scalar.md) | Scalar | Función `scalar` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/Functions/single.md](oxmysql/Functions/single.md) | Single | Función `single` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/Functions/transaction.md](oxmysql/Functions/transaction.md) | Transaction | Función `transaction` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/Functions/update.md](oxmysql/Functions/update.md) | Update | Función `update` de oxmysql: sintaxis y ejemplos en Lua/JS. |
| [oxmysql/index.md](oxmysql/index.md) | OxMySQL | Introducción a oxmysql: instalación, cadena de conexión, convars y uso. |
| [oxmysql/placeholders.md](oxmysql/placeholders.md) | Placeholders | Uso de marcadores (placeholders) en consultas SQL. |
| [oxmysql/ui.md](oxmysql/ui.md) | Using the Debug UI | Uso de la interfaz de depuración de consultas. |

### `resources/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [resources/fivemanage.md](resources/fivemanage.md) | Fivemanage | Presentación de Fivemanage (CDN de imágenes/vídeo y logs para servidores FiveM). |
| [resources/index.md](resources/index.md) | Resources | Índice de recursos para desarrolladores (servicios y plantillas recomendados). |
| [resources/prism-host.md](resources/prism-host.md) | Prism Host | Presentación del proveedor de hosting Prism Host. |
| [resources/tebex-creators.md](resources/tebex-creators.md) | Tebex Creators | Tabla de códigos de creador de Tebex respaldados por Overextended. |
| [resources/templates.md](resources/templates.md) | Templates | Plantillas (boilerplates) recomendadas para crear recursos. |
