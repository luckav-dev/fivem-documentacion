# QBCore — copia offline de la documentación

> Copia local en Markdown (GitHub Flavored Markdown) generada el 2026-10-20 para consulta sin conexión. El contenido de las páginas se mantiene en su idioma original (inglés), sin traducir ni resumir.

## Qué es

Documentación oficial de **QBCore Framework** (GitBook): guías de instalación en Windows/Linux, permisos, optimización de scripts, Visual Studio Code, referencia de `qb-core` (objeto core, datos del jugador, shared, exports, eventos y funciones de cliente/servidor, comandos) y la documentación de cada recurso oficial `qb-*`. También incluye las páginas de patrocinadores del proyecto.

## Origen y licencia

| Dato | Valor |
| --- | --- |
| Repositorio | [qbcore-framework/qb-docs](https://github.com/qbcore-framework/qb-docs) |
| Commit copiado | [`930c12e`](https://github.com/qbcore-framework/qb-docs/tree/930c12ec4f60dfbba60253571f1a58980129516d) (`930c12ec4f60dfbba60253571f1a58980129516d`) |
| Fecha de copia | 2026-10-20 |
| Licencia | sin licencia explícita en el repositorio de documentación (no hay archivo LICENSE; el contenido pertenece a sus autores) |
| Archivos Markdown | 83 (0.5 MB) |
| Imágenes/recursos copiados | 77 (41.9 MB) en [`imagenes/`](imagenes/) |

Cada archivo empieza con una línea `> Fuente original: …` que enlaza el archivo exacto del repositorio en ese commit.

## Cómo se convirtió

- Origen: Markdown de GitBook; se conserva la estructura (`guides/`, `qb-core/`, `qbcore-resources/`, `project-sponsors/`).
- El `README.md` original (portada, página de JetBrains) se guarda como `README-original.md` para no chocar con este índice; `SUMMARY.md` (tabla de contenidos de GitBook) se conserva con los enlaces reescritos.
- `{% hint style=… %}` → citas con etiqueta (`info` → Nota, `success` → Consejo, `warning` → Advertencia, `danger` → Peligro).
- `{% embed url=… %}` → enlace (`> **Contenido incrustado:** …`); `{% file src=… %}` → enlace al archivo.
- Enlaces *mention* de GitBook → enlaces normales; los `broken-reference` del original quedan como texto ("Broken link").
- Se eliminan los anclajes vacíos `<a href="#…" id="…"></a>` que GitBook añade a algunos encabezados y el estilo de `<mark>`.
- Las imágenes de `.gitbook/assets/` se copian a `imagenes/`; las tablas HTML y `<details>` se mantienen (GitHub las muestra).
- Los enlaces internos se reescribieron como rutas relativas a los `.md` generados (con `#ancla` cuando existe); los enlaces externos se mantienen.
- Bloques de código copiados literalmente con su etiqueta de lenguaje; tablas conservadas.
- Imágenes referenciadas (del repositorio y externas descargables) copiadas a `imagenes/` (máx. 5 MB por archivo y ~40 MB por proyecto; las del repositorio tienen prioridad). Las externas se guardan en `imagenes/externas/<dominio>/`.

## Recursos omitidos

Estos recursos no se copiaron; el documento mantiene el enlace a la URL original (o al archivo en GitHub si estaba en el repositorio):

| Recurso | Motivo |
| --- | --- |
| [https://camo.githubusercontent.com/fc66647c3b51a173e277dfd20cf5265146a66ee7b470e37d1ea5713fa34008d4/6874747…](https://camo.githubusercontent.com/fc66647c3b51a173e277dfd20cf5265146a66ee7b470e37d1ea5713fa34008d4/68747470733a2f2f696d6775722e636f6d2f666d563067504d2e706e67) | 1.4 MB: externa omitida para respetar el presupuesto de 40 MB (prioridad a imágenes del repositorio) |
| [https://user-images.githubusercontent.com/91661118/143668930-e9475c53-284c-4054-ad9c-88aa98f76768.png](https://user-images.githubusercontent.com/91661118/143668930-e9475c53-284c-4054-ad9c-88aa98f76768.png) | 4.5 MB: externa omitida para respetar el presupuesto de 40 MB (prioridad a imágenes del repositorio) |

## Observaciones y contenido no convertido

- Los archivos `.zip` adjuntos (fuentes FiraCode y JetBrains Mono) no se copian; se enlazan en GitHub.
- Los `{% embed %}` (vídeos, webs) no pueden incrustarse en Markdown: se muestran como enlaces.
- El campo `icon` de la cabecera GitBook (icono del menú) se descarta.

## Índice de archivos

### Raíz

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [README-original.md](README-original.md) | ✍ JetBrains | Portada original del GitBook (patrocinador JetBrains). |
| [SUMMARY.md](SUMMARY.md) | Table of contents | Tabla de contenidos original de GitBook (orden del menú lateral). |

### `guides/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [guides/linux-installation.md](guides/linux-installation.md) | 🐧 Linux Installation | Guía paso a paso para instalar un servidor QBCore en Linux. |
| [guides/miscellaneous-guides.md](guides/miscellaneous-guides.md) | 📑 Miscellaneous Guides | Guías varias (OneSync infinity, oxmysql, contribuir con pull requests, etc.). |
| [guides/script-optimization.md](guides/script-optimization.md) | 🚀 Script Optimization | Consejos para escribir código optimizado. |
| [guides/setting-permissions.md](guides/setting-permissions.md) | 🔓 Setting Permissions | Cómo configurar permisos (ACE/principals) en el servidor. |
| [guides/useful-links.md](guides/useful-links.md) | 🔗 Useful Links | Lista de enlaces útiles para desarrollar en FiveM. |
| [guides/visual-studio-code.md](guides/visual-studio-code.md) | 📝 Visual Studio Code | Configuración de Visual Studio Code, extensiones y fuentes. |
| [guides/windows-installation.md](guides/windows-installation.md) | 🪟 Windows Installation | Guía paso a paso para instalar un servidor QBCore en Windows. |

### `project-sponsors/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [project-sponsors/durty-cloth-tool.md](project-sponsors/durty-cloth-tool.md) | 👕 Durty Cloth Tool | Patrocinador: Durty Cloth Tool (ropa y tatuajes addon). |
| [project-sponsors/forge-mods.md](project-sponsors/forge-mods.md) | ✨ Forge Mods | Patrocinador: Forge Mods (plataforma de contenido para GTA V). |
| [project-sponsors/gitbook.md](project-sponsors/gitbook.md) | 📚 GitBook | Patrocinador: GitBook. |
| [project-sponsors/kakarotdevs.md](project-sponsors/kakarotdevs.md) | 🎥 KakarotDevs | Patrocinador: KakarotDevs (Twitch/YouTube). |
| [project-sponsors/pleb-masters-forge.md](project-sponsors/pleb-masters-forge.md) | 🔎 Pleb Masters: Forge | Patrocinador: Pleb Masters Forge (buscador de datos de GTA V). |
| [project-sponsors/smart-merge-v.md](project-sponsors/smart-merge-v.md) | 🧩 Smart Merge V | Patrocinador: Smart Merge V (resolución de conflictos de mapas). |

### `qb-core/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [qb-core/client-event-reference.md](qb-core/client-event-reference.md) | 🎮 Client Event Reference | Referencia de eventos de cliente de qb-core. |
| [qb-core/client-function-reference.md](qb-core/client-function-reference.md) | 🎮 Client Function Reference | Referencia de funciones de cliente de qb-core. |
| [qb-core/commands.md](qb-core/commands.md) | ❗ Commands | Lista de comandos y el recurso al que pertenecen. |
| [qb-core/core-object.md](qb-core/core-object.md) | Core Object | El objeto core de qb-core: cómo obtenerlo y qué contiene. |
| [qb-core/drawtext.md](qb-core/drawtext.md) | 💬 DrawText | Uso de la función DrawText (NUI) integrada. |
| [qb-core/player-data.md](qb-core/player-data.md) | 📊 Player Data | Acceso y modificación de los datos del jugador (PlayerData). |
| [qb-core/server-event-reference.md](qb-core/server-event-reference.md) | 🖥 Server Event Reference | Referencia de eventos de servidor de qb-core. |
| [qb-core/server-function-reference.md](qb-core/server-function-reference.md) | 🖥️ Server Function Reference | Referencia de funciones de servidor de qb-core. |
| [qb-core/shared-exports.md](qb-core/shared-exports.md) | ↗ Shared Exports | Exports para actualizar los datos shared de forma dinámica. |
| [qb-core/shared.md](qb-core/shared.md) | 📜 Shared | Gestión de trabajos, bandas, vehículos, ítems, etc. en los archivos shared. |

### `qbcore-resources/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [qbcore-resources/qb-adminmenu.md](qbcore-resources/qb-adminmenu.md) | 🔧 qb-adminmenu | Recurso `qb-adminmenu`: introducción, vista previa, comandos. |
| [qbcore-resources/qb-ambulancejob.md](qbcore-resources/qb-ambulancejob.md) | 🚑 qb-ambulancejob | Recurso `qb-ambulancejob`: introducción, configuración, ítems, eventos, callbacks, comandos. |
| [qbcore-resources/qb-apartments.md](qbcore-resources/qb-apartments.md) | 🏨 qb-apartments | Recurso `qb-apartments`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-banking.md](qbcore-resources/qb-banking.md) | 🏦 qb-banking | Recurso `qb-banking`: introducción. |
| [qbcore-resources/qb-bankrobbery.md](qbcore-resources/qb-bankrobbery.md) | 💰 qb-bankrobbery | Recurso `qb-bankrobbery`: introducción, configuración, ítems. |
| [qbcore-resources/qb-busjob.md](qbcore-resources/qb-busjob.md) | 🚌 qb-busjob | Recurso `qb-busjob`: introducción, configuración. |
| [qbcore-resources/qb-cityhall.md](qbcore-resources/qb-cityhall.md) | 🏢 qb-cityhall | Recurso `qb-cityhall`: introducción, vista previa, configuración, comandos. |
| [qbcore-resources/qb-clothing.md](qbcore-resources/qb-clothing.md) | 👕 qb-clothing | Recurso `qb-clothing`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-crypto.md](qbcore-resources/qb-crypto.md) | 🪙 qb-crypto | Recurso `qb-crypto`: introducción, vista previa, configuración, comandos, ítems. |
| [qbcore-resources/qb-diving.md](qbcore-resources/qb-diving.md) | 🤿 qb-diving | Recurso `qb-diving`: introducción, configuración, ítems, comandos. |
| [qbcore-resources/qb-doorlock.md](qbcore-resources/qb-doorlock.md) | 🚪 qb-doorlock | Recurso `qb-doorlock`: introducción, vista previa, configuración, comandos. |
| [qbcore-resources/qb-drugs.md](qbcore-resources/qb-drugs.md) | 💊 qb-drugs | Recurso `qb-drugs`: introducción, configuración, comandos. |
| [qbcore-resources/qb-fitbit.md](qbcore-resources/qb-fitbit.md) | ⌚ qb-fitbit | Recurso `qb-fitbit`: introducción, vista previa. |
| [qbcore-resources/qb-fuel.md](qbcore-resources/qb-fuel.md) | ⛽ qb-fuel | Recurso `qb-fuel`: introducción. |
| [qbcore-resources/qb-garages.md](qbcore-resources/qb-garages.md) | 🚘 qb-garages | Recurso `qb-garages`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-garbagejob.md](qbcore-resources/qb-garbagejob.md) | 🚛 qb-garbagejob | Recurso `qb-garbagejob`: vehículos. |
| [qbcore-resources/qb-hotdogjob.md](qbcore-resources/qb-hotdogjob.md) | 🌭 qb-hotdogjob | Recurso `qb-hotdogjob`. |
| [qbcore-resources/qb-houserobbery.md](qbcore-resources/qb-houserobbery.md) | 🔫 qb-houserobbery | Recurso `qb-houserobbery`. |
| [qbcore-resources/qb-houses.md](qbcore-resources/qb-houses.md) | 🏡 qb-houses | Recurso `qb-houses`: introducción, vista previa, configuración, comandos, ítems. |
| [qbcore-resources/qb-hud.md](qbcore-resources/qb-hud.md) | ℹ qb-hud | Recurso `qb-hud`: introducción, vista previa, problemas comunes, eventos. |
| [qbcore-resources/qb-input.md](qbcore-resources/qb-input.md) | 📝 qb-input | Recurso `qb-input`: introducción. |
| [qbcore-resources/qb-interior.md](qbcore-resources/qb-interior.md) | 🏠 qb-interior | Recurso `qb-interior`: introducción, configuración, uso. |
| [qbcore-resources/qb-inventory.md](qbcore-resources/qb-inventory.md) | 🎒 qb-inventory | Recurso `qb-inventory`: introducción, ítems, hooks, exports. |
| [qbcore-resources/qb-jewelry.md](qbcore-resources/qb-jewelry.md) | 💎 qb-jewelry | Recurso `qb-jewelry`. |
| [qbcore-resources/qb-lapraces.md](qbcore-resources/qb-lapraces.md) | 🏁 qb-lapraces | Recurso `qb-lapraces`: introducción, vista previa, configuración, comandos. |
| [qbcore-resources/qb-loading.md](qbcore-resources/qb-loading.md) | 🔃 qb-loading | Recurso `qb-loading`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-management.md](qbcore-resources/qb-management.md) | 👔 qb-management | Recurso `qb-management`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-mechanicjob.md](qbcore-resources/qb-mechanicjob.md) | 🧑🔧 🧑🔧 🧑🔧 🧑🔧 qb-mechanicjob | Recurso `qb-mechanicjob`: introducción, vista previa, configuración, comandos. |
| [qbcore-resources/qb-menu.md](qbcore-resources/qb-menu.md) | ↖️ qb-menu | Recurso `qb-menu`: introducción. |
| [qbcore-resources/qb-minigames.md](qbcore-resources/qb-minigames.md) | qb-minigames | Recurso `qb-minigames`: introducción, características. |
| [qbcore-resources/qb-multicharacter.md](qbcore-resources/qb-multicharacter.md) | 🙋 qb-multicharacter | Recurso `qb-multicharacter`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-newsjob.md](qbcore-resources/qb-newsjob.md) | 📰 qb-newsjob | Recurso `qb-newsjob`: introducción, configuración, comandos. |
| [qbcore-resources/qb-pawnshop.md](qbcore-resources/qb-pawnshop.md) | 🤑 qb-pawnshop | Recurso `qb-pawnshop`. |
| [qbcore-resources/qb-phone.md](qbcore-resources/qb-phone.md) | 📱 qb-phone | Recurso `qb-phone`: introducción, vista previa, configuración, comandos. |
| [qbcore-resources/qb-policejob.md](qbcore-resources/qb-policejob.md) | 👮 qb-policejob | Recurso `qb-policejob`: introducción, configuración, comandos, ítems. |
| [qbcore-resources/qb-prison.md](qbcore-resources/qb-prison.md) | 🔐 qb-prison | Recurso `qb-prison`: tiendas. |
| [qbcore-resources/qb-radialmenu.md](qbcore-resources/qb-radialmenu.md) | 🔄 qb-radialmenu | Recurso `qb-radialmenu`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-radio.md](qbcore-resources/qb-radio.md) | 📻 qb-radio | Recurso `qb-radio`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-recyclejob.md](qbcore-resources/qb-recyclejob.md) | ♻ qb-recyclejob | Recurso `qb-recyclejob`: introducción, configuración. |
| [qbcore-resources/qb-scoreboard.md](qbcore-resources/qb-scoreboard.md) | 📋 qb-scoreboard | Recurso `qb-scoreboard`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-scrapyard.md](qbcore-resources/qb-scrapyard.md) | 🔋 qb-scrapyard | Recurso `qb-scrapyard`: ítems, vehículos. |
| [qbcore-resources/qb-shops.md](qbcore-resources/qb-shops.md) | 🏪 qb-shops | Recurso `qb-shops`. |
| [qbcore-resources/qb-smallresources.md](qbcore-resources/qb-smallresources.md) | 📚 qb-smallresources | Recurso `qb-smallresources`: introducción, configuración, registros, ítems, comandos. |
| [qbcore-resources/qb-spawn.md](qbcore-resources/qb-spawn.md) | 🗺 qb-spawn | Recurso `qb-spawn`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-storerobbery.md](qbcore-resources/qb-storerobbery.md) | 🔫 qb-storerobbery | Recurso `qb-storerobbery`. |
| [qbcore-resources/qb-streetraces.md](qbcore-resources/qb-streetraces.md) | 🏎 qb-streetraces | Recurso `qb-streetraces`: introducción, configuración, comandos. |
| [qbcore-resources/qb-target.md](qbcore-resources/qb-target.md) | 👁️ qb-target | Recurso `qb-target`: introducción. |
| [qbcore-resources/qb-taxijob.md](qbcore-resources/qb-taxijob.md) | 🚕 qb-taxijob | Recurso `qb-taxijob`. |
| [qbcore-resources/qb-towjob.md](qbcore-resources/qb-towjob.md) | 🛻 qb-towjob | Recurso `qb-towjob`. |
| [qbcore-resources/qb-truckerjob.md](qbcore-resources/qb-truckerjob.md) | 🚛 qb-truckerjob | Recurso `qb-truckerjob`. |
| [qbcore-resources/qb-truckrobbery.md](qbcore-resources/qb-truckrobbery.md) | 🔫 qb-truckrobbery | Recurso `qb-truckrobbery`. |
| [qbcore-resources/qb-vehiclekeys.md](qbcore-resources/qb-vehiclekeys.md) | 🔑 qb-vehiclekeys | Recurso `qb-vehiclekeys`. |
| [qbcore-resources/qb-vehiclesales.md](qbcore-resources/qb-vehiclesales.md) | 📄 qb-vehiclesales | Recurso `qb-vehiclesales`: introducción, vista previa, configuración. |
| [qbcore-resources/qb-vehicleshop.md](qbcore-resources/qb-vehicleshop.md) | 🚗 qb-vehicleshop | Recurso `qb-vehicleshop`: introducción, vista previa, configuración, comandos. |
| [qbcore-resources/qb-vineyard.md](qbcore-resources/qb-vineyard.md) | 🍇 qb-vineyard | Recurso `qb-vineyard`: introducción, configuración. |
| [qbcore-resources/qb-weapons.md](qbcore-resources/qb-weapons.md) | 🔫 qb-weapons | Recurso `qb-weapons`. |
| [qbcore-resources/qb-weathersync.md](qbcore-resources/qb-weathersync.md) | 🌤 qb-weathersync | Recurso `qb-weathersync`: introducción, configuración, exports, eventos, comandos. |
| [qbcore-resources/qb-weed.md](qbcore-resources/qb-weed.md) | 🌿 qb-weed | Recurso `qb-weed`: introducción, configuración. |
