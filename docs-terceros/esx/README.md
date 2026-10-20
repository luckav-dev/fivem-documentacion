# ESX Legacy — copia offline de la documentación

> Copia local en Markdown (GitHub Flavored Markdown) generada el 2026-10-20 para consulta sin conexión. El contenido de las páginas se mantiene en su idioma original (inglés), sin traducir ni resumir.

## Qué es

Documentación oficial de **ESX Legacy** (Nextra): núcleo `es_extended` (funciones de cliente y servidor, xPlayer, eventos, configuración, módulos), recursos del núcleo (`esx_context`, `esx_menu_*`, `esx_notify`, `esx_multicharacter`…), addons `esx_*`, tutoriales de instalación y desarrollo, herramientas y problemas comunes. Sitio original: <https://docs.esx-framework.org>.

## Origen y licencia

| Dato | Valor |
| --- | --- |
| Repositorio | [esx-framework/esx-legacy-documenation](https://github.com/esx-framework/esx-legacy-documenation) |
| Commit copiado | [`031b7f7`](https://github.com/esx-framework/esx-legacy-documenation/tree/031b7f7543db595e3a6503e822107b7f60ce14ec) (`031b7f7543db595e3a6503e822107b7f60ce14ec`) |
| Fecha de copia | 2026-10-20 |
| Licencia | **MIT** (archivo `LICENSE` del repositorio, © ESX Framework) |
| Archivos Markdown | 81 (0.3 MB) |
| Imágenes/recursos copiados | 27 (40.0 MB) en [`imagenes/`](imagenes/) |

Cada archivo empieza con una línea `> Fuente original: …` que enlaza el archivo exacto del repositorio en ese commit.

## Cómo se convirtió

- Origen: MDX de Nextra en `src/pages/en/`; se conserva la estructura (p. ej. `esx_core.md` junto a la carpeta `esx_core/`).
- `<Callout type=…>` → citas con etiqueta en negrita.
- `<FileTree>` → árbol de carpetas en un bloque `text`. `<ToolsList />` → lista de enlaces generada desde `src/data/tools.ts`.
- El título visual `<div style={{fontSize…}}>` de *troubleshoot* → encabezado `#`; se eliminan los `className`/`style` JSX.
- Las imágenes de `public/` (rutas `/tutorial-images/...`) y las externas descargables se copian a `imagenes/`.
- Se corrigieron dos vallas de código defectuosas del original (ver *Observaciones*).
- Los enlaces internos se reescribieron como rutas relativas a los `.md` generados (con `#ancla` cuando existe); los enlaces externos se mantienen.
- Bloques de código copiados literalmente con su etiqueta de lenguaje; tablas conservadas.
- Imágenes referenciadas (del repositorio y externas descargables) copiadas a `imagenes/` (máx. 5 MB por archivo y ~40 MB por proyecto; las del repositorio tienen prioridad). Las externas se guardan en `imagenes/externas/<dominio>/`.

## Recursos omitidos

Estos recursos no se copiaron; el documento mantiene el enlace a la URL original (o al archivo en GitHub si estaba en el repositorio):

| Recurso | Motivo |
| --- | --- |
| [https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04093311.png](https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04093311.png) | externa no descargada: descarga fallida (HTTPError) 404 |
| [https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04080213.png](https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04080213.png) | externa no descargada: > 5 MB |
| [https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04082103.png](https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04082103.png) | externa no descargada: > 5 MB |
| [https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04101625.png](https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04101625.png) | externa no descargada: > 5 MB |
| [https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04085222.png](https://r2.fivemanage.com/SVPyt7tsQi4njkYd2eKX6/Screenshot2025-01-04085222.png) | externa no descargada: > 5 MB |
| [https://media.discordapp.net/attachments/1370464258382368918/1411718707842912296/482157467-7f03706b-1794-40…](https://media.discordapp.net/attachments/1370464258382368918/1411718707842912296/482157467-7f03706b-1794-40ac-9cf5-bba13dadd9c4.png?ex=68b5ad00&is=68b45b80&hm=c96f3dd053b35a1eff0b4d79b6d0ece10ab5d418a156330bd369b1e94094af8e&=&format=webp&quality=lossless&width=1529&height=860) | externa no descargada: descarga fallida (HTTPError) 404 |
| [https://private-user-images.githubusercontent.com/90266455/483988755-d6681576-502c-43ed-a243-2181254fc9b2.p…](https://private-user-images.githubusercontent.com/90266455/483988755-d6681576-502c-43ed-a243-2181254fc9b2.png?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3NTY4MjEwNTIsIm5iZiI6MTc1NjgyMDc1MiwicGF0aCI6Ii85MDI2NjQ1NS80ODM5ODg3NTUtZDY2ODE1NzYtNTAyYy00M2VkLWEyNDMtMjE4MTI1NGZjOWIyLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNTA5MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjUwOTAyVDEzNDU1MlomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTk4N2JkYTQwOTZkMzg0NDI2Y2MwNjYwMzkwNzUxMmQyZWZkOWY0YmMxYzYyMTdiY2RjZThlZmI2ODY5NzA3OTUmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0In0.zpClCFy504O4ZrxUyRPYqn9gUhIK_d-GQGQhWquizGk) | externa no descargada: descarga fallida (HTTPError) 404 |
| [https://i.gyazo.com/483dfe7f779d5d85e908a61cd6505b5e.png](https://i.gyazo.com/483dfe7f779d5d85e908a61cd6505b5e.png) | externa no descargada: descarga fallida (HTTPError) 503 |
| [https://i.gyazo.com/b221b628cfb26581d2848aefdd318c72.png](https://i.gyazo.com/b221b628cfb26581d2848aefdd318c72.png) | externa no descargada: descarga fallida (HTTPError) 503 |
| [https://i.gyazo.com/ed571574e704017b41b7234321624319.png](https://i.gyazo.com/ed571574e704017b41b7234321624319.png) | externa no descargada: descarga fallida (HTTPError) 503 |
| [https://i.gyazo.com/thumb/1200/6ebb0adb3c4ddd26d902a5cfc3eceede-png.jpg](https://i.gyazo.com/thumb/1200/6ebb0adb3c4ddd26d902a5cfc3eceede-png.jpg) | externa no descargada: descarga fallida (HTTPError) 503 |

## Observaciones y contenido no convertido

- esx_core/esx_notify.md: valla de código sobrante al final del original eliminada
- esx_core/esx_skin.md: bloque de código sin cerrar en el original; se añadió la valla de cierre
- Las imágenes de i.gyazo.com (troubleshoot) respondieron 503 y algunas de r2.fivemanage.com superan 5 MB: se mantienen como enlaces externos.
- `_meta.js` (orden/títulos del menú lateral de Nextra), los componentes de anuncios y el resto de `src/` no son contenido y no se convierten.

## Índice de archivos

### Raíz

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [esx_addons.md](esx_addons.md) | ESX Legacy Addons - Complete Collection of FiveM Roleplay Scripts | Índice de los addons oficiales de ESX Legacy. |
| [esx_core.md](esx_core.md) | ESX Core Framework Documentation - Complete Developer Reference | Índice de la documentación del núcleo de ESX Legacy. |
| [index.md](index.md) | ESX Legacy Framework - Complete FiveM Roleplay Server Framework | Portada de ESX Legacy: características del framework y primeros pasos. |
| [tools.md](tools.md) | Tools | Herramientas online externas útiles para desarrollar (lista de enlaces). |
| [troubleshoot.md](troubleshoot.md) | Troubleshooting | Problemas comunes (natives no soportados, conexión a la base de datos, ESX = nil). |

### `esx_addons/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [esx_addons/esx_accessories.md](esx_addons/esx_accessories.md) | esx_accessories | Addon `esx_accessories`: configuración. |
| [esx_addons/esx_addonaccount.md](esx_addons/esx_addonaccount.md) | esx_addonaccount | Addon `esx_addonaccount`: API. |
| [esx_addons/esx_addoninventory.md](esx_addons/esx_addoninventory.md) | esx_addoninventory | Addon `esx_addoninventory`: API. |
| [esx_addons/esx_adminmenu.md](esx_addons/esx_adminmenu.md) | esx_adminmenu | Addon `esx_adminmenu`: requisitos, permisos, comandos. |
| [esx_addons/esx_ambulancejob.md](esx_addons/esx_ambulancejob.md) | esx_ambulancejob | Addon `esx_ambulancejob`: configuración. |
| [esx_addons/esx_animations.md](esx_addons/esx_animations.md) | esx_animations | Addon `esx_animations`: configuración, exports, requisitos. |
| [esx_addons/esx_banking.md](esx_addons/esx_banking.md) | esx_banking | Addon `esx_banking`: configuración. |
| [esx_addons/esx_barbershop.md](esx_addons/esx_barbershop.md) | esx_barbershop | Addon `esx_barbershop`: configuración. |
| [esx_addons/esx_basicneeds.md](esx_addons/esx_basicneeds.md) | esx_basicneeds | Addon `esx_basicneeds`. |
| [esx_addons/esx_billing.md](esx_addons/esx_billing.md) | esx_billing | Addon `esx_billing`: uso. |
| [esx_addons/esx_boat.md](esx_addons/esx_boat.md) | esx_boat | Addon `esx_boat`. |
| [esx_addons/esx_clotheshop.md](esx_addons/esx_clotheshop.md) | esx_clotheshop | Addon `esx_clotheshop`: configuración. |
| [esx_addons/esx_cruisecontrol.md](esx_addons/esx_cruisecontrol.md) | esx_cruisecontrol | Addon `esx_cruisecontrol`: configuración. |
| [esx_addons/esx_datastore.md](esx_addons/esx_datastore.md) | esx_datastore | Addon `esx_datastore`: API. |
| [esx_addons/esx_dmvschool.md](esx_addons/esx_dmvschool.md) | esx_dmvschool | Addon `esx_dmvschool`: configuración. |
| [esx_addons/esx_drugs.md](esx_addons/esx_drugs.md) | esx_drugs | Addon `esx_drugs`: configuración. |
| [esx_addons/esx_garage.md](esx_addons/esx_garage.md) | esx_garage | Addon `esx_garage`. |
| [esx_addons/esx_hud.md](esx_addons/esx_hud.md) | esx_hud | Addon `esx_hud`: características, requisitos. |
| [esx_addons/esx_joblisting.md](esx_addons/esx_joblisting.md) | esx_joblisting | Addon `esx_joblisting`: configuración. |
| [esx_addons/esx_jobs.md](esx_addons/esx_jobs.md) | esx_jobs | Addon `esx_jobs`. |
| [esx_addons/esx_license.md](esx_addons/esx_license.md) | esx_license | Addon `esx_license`. |
| [esx_addons/esx_lscustom.md](esx_addons/esx_lscustom.md) | esx_lscustom | Addon `esx_lscustom`: configuración. |
| [esx_addons/esx_mechanicjob.md](esx_addons/esx_mechanicjob.md) | esx_mechanicjob | Addon `esx_mechanicjob`. |
| [esx_addons/esx_optionalneeds.md](esx_addons/esx_optionalneeds.md) | esx_optionalneeds | Addon `esx_optionalneeds`: uso. |
| [esx_addons/esx_policejob.md](esx_addons/esx_policejob.md) | esx_policejob | Addon `esx_policejob`. |
| [esx_addons/esx_property.md](esx_addons/esx_property.md) | esx_property | Addon `esx_property`: características. |
| [esx_addons/esx_rpchat.md](esx_addons/esx_rpchat.md) | esx_rpchat | Addon `esx_rpchat`. |
| [esx_addons/esx_service.md](esx_addons/esx_service.md) | esx_service | Addon `esx_service`. |
| [esx_addons/esx_shops.md](esx_addons/esx_shops.md) | esx_shops | Addon `esx_shops`: requisitos, instalación, configuración. |
| [esx_addons/esx_society.md](esx_addons/esx_society.md) | esx_society | Addon `esx_society`: requisitos, configuración, uso. |
| [esx_addons/esx_status.md](esx_addons/esx_status.md) | esx_status | Addon `esx_status`: uso. |
| [esx_addons/esx_taxijob.md](esx_addons/esx_taxijob.md) | esx_taxijob | Addon `esx_taxijob`: configuración. |
| [esx_addons/esx_vehicleshop.md](esx_addons/esx_vehicleshop.md) | esx_vehicleshop | Addon `esx_vehicleshop`: configuración. |
| [esx_addons/esx_weaponshop.md](esx_addons/esx_weaponshop.md) | esx_weaponshop | Addon `esx_weaponshop`. |

### `esx_core/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [esx_core/es_extended.md](esx_core/es_extended.md) | es_extended | Introducción a es_extended, el recurso principal de ESX. |
| [esx_core/es_extended/client.md](esx_core/es_extended/client.md) | Client | Índice de la API de cliente de es_extended. |
| [esx_core/es_extended/client/functions.md](esx_core/es_extended/client/functions.md) | Functions | es_extended › cliente › funciones. Contiene: `IsPlayerLoaded`, `GetPlayerData`, `SecureNetEvent`, `DisableSpawnManager`, `SearchInventory` y 15 más. |
| [esx_core/es_extended/client/imports/point.md](esx_core/es_extended/client/imports/point.md) | Points | es_extended › cliente › imports › point. Contiene: `Properties`, `Create a Point`, `Delete a Point`, `Hide/UnHide a Point`. |
| [esx_core/es_extended/client/imports/require.md](esx_core/es_extended/client/imports/require.md) | Require | es_extended › cliente › imports › require. Contiene: `Examples`. |
| [esx_core/es_extended/client/modules/callback.md](esx_core/es_extended/client/modules/callback.md) | Callback | es_extended › cliente › módulos › callback. Contiene: `TriggerServerCallback`, `AwaitServerCallback`, `RegisterClientCallback`. |
| [esx_core/es_extended/client/modules/game.md](esx_core/es_extended/client/modules/game.md) | ESX.Game | es_extended › cliente › módulos › game. Contiene: `GetPedMugshot`, `Teleport`, `SpawnObject`, `SpawnLocalObject`, `DeleteVehicle` y 22 más. |
| [esx_core/es_extended/client/modules/interactions.md](esx_core/es_extended/client/modules/interactions.md) | Interactions | es_extended › cliente › módulos › interactions. Contiene: `RegisterInteraction`, `GetInteractKey`. |
| [esx_core/es_extended/client/modules/scaleform.md](esx_core/es_extended/client/modules/scaleform.md) | Scaleform | es_extended › cliente › módulos › scaleform. Contiene: `ShowFreemodeMessage`, `ShowBreakingNews`, `ShowPopupWarning`, `ShowTrafficMovie`, `Utils`. |
| [esx_core/es_extended/client/modules/streaming.md](esx_core/es_extended/client/modules/streaming.md) | Streaming | es_extended › cliente › módulos › streaming. Contiene: `RequestModel`, `RequestStreamedTextureDict`, `RequestNamedPtfxAsset`, `RequestAnimSet`, `RequestAnimDict` y 1 más. |
| [esx_core/es_extended/client/ui.md](esx_core/es_extended/client/ui.md) | UI | es_extended › cliente › interfaz (UI). Contiene: `RegisterType`, `Open`, `Close`, `CloseAll`, `GetOpened` y 2 más. |
| [esx_core/es_extended/commands.md](esx_core/es_extended/commands.md) | Commands | Comandos de administración incluidos en es_extended. |
| [esx_core/es_extended/config/adjustments.md](esx_core/es_extended/config/adjustments.md) | Adjustments | Ajustes (adjustments) de comportamiento del juego. |
| [esx_core/es_extended/config/logs.md](esx_core/es_extended/config/logs.md) | Discord Logging Config | Configuración de logs a Discord. |
| [esx_core/es_extended/config/main.md](esx_core/es_extended/config/main.md) | Main Config | Configuración principal de es_extended. |
| [esx_core/es_extended/config/weapon.md](esx_core/es_extended/config/weapon.md) | Weapon | Configuración de armas. |
| [esx_core/es_extended/events/client.md](esx_core/es_extended/events/client.md) | Clientsided Events | es_extended › eventos › cliente. Contiene: `esx:addInventoryItem`, `esx:playerLoaded`, `esx:onPlayerDeath`, `esx:playerJumping`, `esx:enteringVehicle` y 6 más. |
| [esx_core/es_extended/events/server.md](esx_core/es_extended/events/server.md) | Serversided Events | es_extended › eventos › servidor. Contiene: `esx:playerLoaded`, `esx:playerLogout`, `esx:playerDropped`, `esx:playerLoaded`, `esx:playerJumping` y 11 más. |
| [esx_core/es_extended/playerdata.md](esx_core/es_extended/playerdata.md) | PlayerData | Estructura de los datos del jugador (PlayerData). |
| [esx_core/es_extended/server/functions.md](esx_core/es_extended/server/functions.md) | Serverside Functions | es_extended › servidor › funciones. Contiene: `Globals`, `Print a Trace`, `RegisterServerCallback`, `TriggerClientCallback`, `AwaitClientCallback` y 26 más. |
| [esx_core/es_extended/server/onesync.md](esx_core/es_extended/server/onesync.md) | Serverside OneSync Functions | Funciones de servidor basadas en OneSync. |
| [esx_core/es_extended/server/xplayer.md](esx_core/es_extended/server/xplayer.md) | xPlayer Functions | Funciones del objeto xPlayer (servidor). |
| [esx_core/es_extended/shared.md](esx_core/es_extended/shared.md) | Shared Functions | Funciones compartidas (cliente y servidor) de es_extended. |
| [esx_core/es_extended/shared/math.md](esx_core/es_extended/shared/math.md) | math | es_extended › compartido › math. Contiene: `Round`, `GroupDigits`, `Trim`, `GetHeadingFromCoords`. |
| [esx_core/es_extended/shared/playerdata.md](esx_core/es_extended/shared/playerdata.md) | Player Data | es_extended › compartido › datos del jugador. Contiene: `Server`, `Client`. |
| [esx_core/es_extended/shared/table.md](esx_core/es_extended/shared/table.md) | table | es_extended › compartido › table. Contiene: `DumpTable`, `SizeOf`, `Set`, `IndexOf`, `LastIndexOf` y 11 más. |
| [esx_core/es_extended/shared/timeout.md](esx_core/es_extended/shared/timeout.md) | timeout | es_extended › compartido › timeout. Contiene: `SetTimeout`, `ClearTimeout`. |
| [esx_core/esx_context.md](esx_core/esx_context.md) | esx_context | Recurso del núcleo `esx_context`: vista previa. |
| [esx_core/esx_identity.md](esx_core/esx_identity.md) | esx_identity | Recurso del núcleo `esx_identity`. |
| [esx_core/esx_menu_default.md](esx_core/esx_menu_default.md) | esx_menu_default | Recurso del núcleo `esx_menu_default`. |
| [esx_core/esx_menu_dialog.md](esx_core/esx_menu_dialog.md) | esx_menu_dialog | Recurso del núcleo `esx_menu_dialog`. |
| [esx_core/esx_menu_list.md](esx_core/esx_menu_list.md) | esx_menu_list | Recurso del núcleo `esx_menu_list`. |
| [esx_core/esx_multicharacter.md](esx_core/esx_multicharacter.md) | esx_multicharacter | Recurso del núcleo `esx_multicharacter`. |
| [esx_core/esx_notify.md](esx_core/esx_notify.md) | esx_notify | Recurso del núcleo `esx_notify`: exports. |
| [esx_core/esx_progressbar.md](esx_core/esx_progressbar.md) | esx_progressbar | Recurso del núcleo `esx_progressbar`. |
| [esx_core/esx_skin.md](esx_core/esx_skin.md) | esx_skin | Recurso del núcleo `esx_skin`. |
| [esx_core/esx_textui.md](esx_core/esx_textui.md) | esx_textui | Recurso del núcleo `esx_textui`. |
| [esx_core/skinchanger.md](esx_core/skinchanger.md) | skinchanger | Recurso skinchanger (cambio de apariencia del personaje). |

### `tutorial/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [tutorial/coding_practices.md](tutorial/coding_practices.md) | Best Coding Practices | Buenas prácticas de programación. |
| [tutorial/coding_practices/annotations.md](tutorial/coding_practices/annotations.md) | Annotations | Uso de anotaciones de tipos (LuaLS) en el código. |
| [tutorial/developing.md](tutorial/developing.md) | Developing a ESX Script | Tutorial para desarrollar un script ESX (extensiones VSCode, estructura, ejemplos). |
| [tutorial/install.md](tutorial/install.md) | Installing ESX Legacy | Tutorial de instalación de ESX Legacy. |
