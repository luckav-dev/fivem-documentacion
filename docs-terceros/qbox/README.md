# Qbox — copia offline de la documentación

> Copia local en Markdown (GitHub Flavored Markdown) generada el 2026-10-20 para consulta sin conexión. El contenido de las páginas se mantiene en su idioma original (inglés), sin traducir ni resumir.

## Qué es

Documentación oficial del **Qbox Project**: framework de roleplay para FiveM basado en QBCore (`qbx_core` y recursos `qbx_*`), guía de instalación y conversión desde QBCore, documentación del *Qbox Dashboard* (logging con Grafana/Loki, CDN, copias de seguridad, aplicaciones, equipo, Discord, caché de recursos, Zumble, Nucleus), recursos de Tebex y artículos del blog. Sitio original: <https://docs.qbox.re>.

## Origen y licencia

| Dato | Valor |
| --- | --- |
| Repositorio | [Qbox-project/qbox-docs](https://github.com/Qbox-project/qbox-docs) |
| Commit copiado | [`260c0ec`](https://github.com/Qbox-project/qbox-docs/tree/260c0ecedce58bece2cf94ebef73be42d08258ac) (`260c0ecedce58bece2cf94ebef73be42d08258ac`) |
| Fecha de copia | 2026-10-20 |
| Licencia | sin licencia explícita en el repositorio de documentación (no hay archivo LICENSE; el contenido pertenece a sus autores) |
| Archivos Markdown | 82 (0.3 MB) |
| Imágenes/recursos copiados | 47 (4.5 MB) en [`imagenes/`](imagenes/) |

Cada archivo empieza con una línea `> Fuente original: …` que enlaza el archivo exacto del repositorio en ese commit.

## Cómo se convirtió

- Origen: MDX de Docusaurus (`docs/` y `blog/`); se conserva la estructura `docs/…` y `blog/…`.
- Admoniciones `:::info`, `:::tip`, `:::warning`, `:::danger`, `:::note` (con título opcional) → citas con etiqueta en negrita.
- `<Tabs>`/`<TabItem>` → subsecciones con el nombre de la pestaña en negrita.
- Páginas de API generadas desde OpenAPI (`*.api.mdx` + JSON `ParamsDetails`/`RequestSchema`/`StatusCodes`) → método y ruta, tabla de parámetros y esquemas/ejemplos en bloques `json` construidos a partir de esos JSON.
- `<ReactPlayer>` → enlace al vídeo (`> **Vídeo:** …`). `<Columns>`, `<Card>`, `<CardImage>` (logo Tebex) se eliminan por ser maquetación; `<Button>` → enlace.
- Las rutas absolutas de imagen (`/img/...`) se resuelven contra `static/`.
- En las entradas del blog se añade una línea con autores (identificadores de `blog/authors.yml`) y fecha si existen.
- Los enlaces internos se reescribieron como rutas relativas a los `.md` generados (con `#ancla` cuando existe); los enlaces externos se mantienen.
- Bloques de código copiados literalmente con su etiqueta de lenguaje; tablas conservadas.
- Imágenes referenciadas (del repositorio y externas descargables) copiadas a `imagenes/` (máx. 5 MB por archivo y ~40 MB por proyecto; las del repositorio tienen prioridad). Las externas se guardan en `imagenes/externas/<dominio>/`.

## Recursos omitidos

Estos recursos no se copiaron; el documento mantiene el enlace a la URL original (o al archivo en GitHub si estaba en el repositorio):

| Recurso | Motivo |
| --- | --- |
| `static/img/blogs/install-custom-weapons/using-ox_inventory.mp4` | 9.1 MB > 5 MB |
| `static/img/blogs/install-custom-weapons/vscode-component.mp4` | 8.9 MB > 5 MB |
| `static/img/blogs/install-custom-weapons/different-flashlights.mp4` | 14.5 MB > 5 MB |

## Observaciones y contenido no convertido

- Los vídeos de YouTube y de media.qbox.re se enlazan (no se descargan). Los tres vídeos `.mp4` locales del artículo de armas superan 5 MB y se enlazan a su archivo en GitHub.
- El logo de Tebex (`<CardImage>`) y la maquetación en columnas de las páginas de Tebex se eliminan por ser decorativos.
- `sidebars.ts`, `_category_.yml` y `blog/authors.yml` no se convierten (solo afectan a la navegación del sitio).

## Índice de archivos

### `blog/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [blog/2025/03-26-addon-weapons.md](blog/2025/03-26-addon-weapons.md) | Installing custom weapons using ox_inventory | Blog: instalar armas personalizadas con ox_inventory. |
| [blog/2025/04-20-setup-manifests.md](blog/2025/04-20-setup-manifests.md) | How fxmanifests Work with FiveM | Blog: qué son los fxmanifest y cómo funcionan. |
| [blog/2025/06-17-linux-server.md](blog/2025/06-17-linux-server.md) | Installing server artifacts on Linux | Blog: instalar los artifacts del servidor en Linux. |
| [blog/2025/09-05-navigating.md](blog/2025/09-05-navigating.md) | Navigating Qbox Efficiently | Blog: cómo navegar el código de Qbox de forma eficiente con el editor. |
| [blog/2025/11-19-db-remote-access.md](blog/2025/11-19-db-remote-access.md) | Remotely accessing MariaDB | Blog: acceso remoto seguro a MariaDB (usuario de solo lectura, firewall). |
| [blog/2025/4-19-vscode-intellisense.md](blog/2025/4-19-vscode-intellisense.md) | Setting up VSCode for FiveM and RedM Lua Scripting | Blog: configurar VSCode para programar en Lua para FiveM/RedM. |

### `docs/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [docs/dashboard/applications/forms.md](docs/dashboard/applications/forms.md) | Building a Form | Dashboard › Aplicaciones: construir un formulario y sus preguntas. |
| [docs/dashboard/applications/index.md](docs/dashboard/applications/index.md) | 📝 Applications | Dashboard › Aplicaciones: formularios de whitelist/staff en una página pública. |
| [docs/dashboard/applications/portal.md](docs/dashboard/applications/portal.md) | Portal Page | Dashboard › Aplicaciones: personalizar la página pública (apply.qbox.re). |
| [docs/dashboard/applications/questionnaires.md](docs/dashboard/applications/questionnaires.md) | Questionnaires | Dashboard › Aplicaciones: cuestionarios y votaciones para jugadores. |
| [docs/dashboard/applications/reviewing.md](docs/dashboard/applications/reviewing.md) | Reviewing Applications | Dashboard › Aplicaciones: revisar solicitudes desde el panel o Discord. |
| [docs/dashboard/cdn/api/create-presigned-url.api.md](docs/dashboard/cdn/api/create-presigned-url.api.md) | Create Presigned URL | API del CDN: crear una URL prefirmada (parámetros, respuestas). |
| [docs/dashboard/cdn/api/delete-file.api.md](docs/dashboard/cdn/api/delete-file.api.md) | Delete file | API del CDN: borrar un archivo (parámetros, respuestas). |
| [docs/dashboard/cdn/api/upload-file-presigned-url.api.md](docs/dashboard/cdn/api/upload-file-presigned-url.api.md) | Upload file (Presigned URL) | API del CDN: subir un archivo con URL prefirmada. |
| [docs/dashboard/cdn/api/upload-file.api.md](docs/dashboard/cdn/api/upload-file.api.md) | Upload file | API del CDN: subir un archivo (multipart). |
| [docs/dashboard/cdn/index.md](docs/dashboard/cdn/index.md) | 🖼️ CDN | Dashboard › CDN: almacenamiento y entrega de imágenes/vídeos. |
| [docs/dashboard/cdn/setup/lb-phone.md](docs/dashboard/cdn/setup/lb-phone.md) | LB Phone | Dashboard › CDN: configuración con LB Phone. |
| [docs/dashboard/cdn/setup/sharex.md](docs/dashboard/cdn/setup/sharex.md) | ShareX | Dashboard › CDN: configuración con ShareX. |
| [docs/dashboard/database-backups/index.md](docs/dashboard/database-backups/index.md) | 💽 Database Backups | Dashboard › Copias de seguridad automáticas de la base de datos (qbx_db_backup). |
| [docs/dashboard/discord/index.md](docs/dashboard/discord/index.md) | 🤖 Discord | Dashboard › Conectar el servidor de Discord de la comunidad. |
| [docs/dashboard/index.md](docs/dashboard/index.md) | Getting Started | Qbox Dashboard: qué hace, cómo funcionan las organizaciones y qué incluye cada plan. |
| [docs/dashboard/logging/custom-permissions.md](docs/dashboard/logging/custom-permissions.md) | Dashboard Permissions | Logging: permisos de dashboards con equipos de Grafana. |
| [docs/dashboard/logging/database.md](docs/dashboard/logging/database.md) | Database Visualization | Logging: visualizar la base de datos en Grafana. |
| [docs/dashboard/logging/geomap.md](docs/dashboard/logging/geomap.md) | GTA V Map | Logging: mapa de GTA V (geomap) en Grafana. |
| [docs/dashboard/logging/getting-started.md](docs/dashboard/logging/getting-started.md) | Getting Started | Logging: crear el servidor de logs, entrar en Grafana y enviar los primeros logs. |
| [docs/dashboard/logging/index.md](docs/dashboard/logging/index.md) | 🗃️ Logging | Dashboard › Logging: Grafana, Loki y Prometheus gestionados para logs y métricas. |
| [docs/dashboard/logging/metrics.md](docs/dashboard/logging/metrics.md) | Server Metrics | Logging: métricas de rendimiento de FXServer (/perf, Prometheus). |
| [docs/dashboard/logging/staff-access.md](docs/dashboard/logging/staff-access.md) | Staff Access to Grafana | Logging: acceso del staff a Grafana con su cuenta Qbox. |
| [docs/dashboard/nucleus/index.md](docs/dashboard/nucleus/index.md) | 🌐 Nucleus | Dashboard › Nucleus. |
| [docs/dashboard/resource-cache/index.md](docs/dashboard/resource-cache/index.md) | ⚡ Resource Cache | Dashboard › Caché de recursos: descarga de recursos desde un CDN global. |
| [docs/dashboard/team/audit-log.md](docs/dashboard/team/audit-log.md) | Audit Log | Equipo: registro de auditoría de cambios de miembros y roles. |
| [docs/dashboard/team/discord-access.md](docs/dashboard/team/discord-access.md) | Staff Access through Discord | Equipo: acceso del staff mediante roles de Discord. |
| [docs/dashboard/team/enroll-staff.md](docs/dashboard/team/enroll-staff.md) | Enroll Your Staff | Equipo: dar de alta al staff paso a paso. |
| [docs/dashboard/team/index.md](docs/dashboard/team/index.md) | 👥 Team & Access | Dashboard › Equipo y acceso: miembros, roles y acceso del staff. |
| [docs/dashboard/team/inviting-by-email.md](docs/dashboard/team/inviting-by-email.md) | Inviting by Email | Equipo: invitar a una persona por correo. |
| [docs/dashboard/team/roles.md](docs/dashboard/team/roles.md) | Roles and Permissions | Equipo: roles integrados y personalizados, y permisos de cada uno. |
| [docs/dashboard/zumble/index.md](docs/dashboard/zumble/index.md) | 🎙️ Zumble | Dashboard › Zumble (servidor de voz Mumble alternativo). |
| [docs/introduction/contributors.md](docs/introduction/contributors.md) | Contributing Guidelines | Normas para contribuir a Qbox. |
| [docs/introduction/converting.md](docs/introduction/converting.md) | Converting from QBCore to Qbox | Cómo convertir un servidor y recursos de QBCore a Qbox. |
| [docs/introduction/developers.md](docs/introduction/developers.md) | Developer's Guide | Guía para desarrolladores: buenas prácticas con qbx_core. |
| [docs/introduction/faq.md](docs/introduction/faq.md) | Frequently Asked Questions | Preguntas frecuentes sobre Qbox. |
| [docs/introduction/installation.md](docs/introduction/installation.md) | Installation Guide | Guía de instalación de Qbox con txAdmin y requisitos de MariaDB. |
| [docs/introduction/introduction.md](docs/introduction/introduction.md) | Introduction to the Qbox Framework | Introducción al framework Qbox (origen, soporte, conversión, contribución). |
| [docs/introduction/release.md](docs/introduction/release.md) | Release Readiness Guidelines | Requisitos para publicar versiones estables de recursos Qbox. |
| [docs/resources/qbx_core/commands.md](docs/resources/qbx_core/commands.md) | Commands | Recurso `qbx_core` › comandos. Contiene: `Teleport`, `Teleport to Marker`, `Toggle PVP`, `Add Permission`, `Remove Permission` y 18 más. |
| [docs/resources/qbx_core/convars.md](docs/resources/qbx_core/convars.md) | Convars | Recurso `qbx_core` › convars. Contiene: `enableBridge`, `enableQueue`, `bucketLockdownMode`, `discordLink`, `max_jobs_per_player` y 10 más. |
| [docs/resources/qbx_core/discord.md](docs/resources/qbx_core/discord.md) | Discord Rich Presence | qbx_core: cambiar la Rich Presence de Discord. |
| [docs/resources/qbx_core/events/client.md](docs/resources/qbx_core/events/client.md) | Client Events | Recurso `qbx_core` › eventos › cliente. Contiene: `OnPlayerLoaded`, `SetDuty`, `OnPermissionUpdate`, `playerLoggedOut`, `OnJobUpdate` y 4 más. |
| [docs/resources/qbx_core/events/server.md](docs/resources/qbx_core/events/server.md) | Server Events | Recurso `qbx_core` › eventos › servidor. Contiene: `OnPlayerUnload`, `OnPermissionUpdate`, `OnJobUpdate`, `OnGangUpdate`, `SetDuty` y 4 más. |
| [docs/resources/qbx_core/exports/client.md](docs/resources/qbx_core/exports/client.md) | Client Exports | Recurso `qbx_core` › exports › cliente. Contiene: `Notify`, `HasPrimaryGroup`, `HasGroup`, `GetGroups`. |
| [docs/resources/qbx_core/exports/server.md](docs/resources/qbx_core/exports/server.md) | Server Exports | Recurso `qbx_core` › exports › servidor. Contiene: `CreateJob`, `CreateJobs`, `RemoveJob`, `CreateGangs`, `RemoveGang` y 71 más. |
| [docs/resources/qbx_core/exports/shared.md](docs/resources/qbx_core/exports/shared.md) | Shared Exports | Recurso `qbx_core` › exports › compartido. Contiene: `GetJobs`, `GetGangs`, `GetJob`, `GetGang`, `GetVehiclesByName` y 4 más. |
| [docs/resources/qbx_core/modules/hooks.md](docs/resources/qbx_core/modules/hooks.md) | Hooks | Recurso `qbx_core` › módulos › hooks. Contiene: `registerHook`, `removeHooks`, `Usage`. |
| [docs/resources/qbx_core/modules/lib/client.md](docs/resources/qbx_core/modules/lib/client.md) | Client Lib | Recurso `qbx_core` › módulos › lib › cliente. Contiene: `drawText2d`, `drawText3d`, `getEntityAndNetIdFromBagName`, `entityStateHandler`, `deleteVehicle` y 13 más. |
| [docs/resources/qbx_core/modules/lib/index.md](docs/resources/qbx_core/modules/lib/index.md) | Lib | Recurso `qbx_core` › módulos › lib › index. Contiene: `Prerequisites`, `Installation`. |
| [docs/resources/qbx_core/modules/lib/server.md](docs/resources/qbx_core/modules/lib/server.md) | Server Lib | Recurso `qbx_core` › módulos › lib › servidor. Contiene: `spawnVehicle`. |
| [docs/resources/qbx_core/modules/lib/shared.md](docs/resources/qbx_core/modules/lib/shared.md) | Shared Lib | Recurso `qbx_core` › módulos › lib › compartido. Contiene: `armsWithoutGloves.male`, `armsWithoutGloves.female`, `string.trim`, `string.capitalize`, `math.round` y 6 más. |
| [docs/resources/qbx_core/modules/logger.md](docs/resources/qbx_core/modules/logger.md) | Logger | Recurso `qbx_core` › módulos › logger. Contiene: `Example Usage`. |
| [docs/resources/qbx_core/modules/playerdata.md](docs/resources/qbx_core/modules/playerdata.md) | PlayerData | Recurso `qbx_core` › módulos › datos del jugador. Contiene: `Installation`. |
| [docs/resources/qbx_core/multichar.md](docs/resources/qbx_core/multichar.md) | MultiCharacter | qbx_core: sistema de multipersonaje. |
| [docs/resources/qbx_core/types/gang.md](docs/resources/qbx_core/types/gang.md) | Gangs | Recurso `qbx_core` › tipos › gang. Contiene: `GangData`, `Gang`, `GangGradeData`. |
| [docs/resources/qbx_core/types/job.md](docs/resources/qbx_core/types/job.md) | Jobs | Recurso `qbx_core` › tipos › job. Contiene: `JobData`, `Job`, `JobGradeData`. |
| [docs/resources/qbx_core/types/player.md](docs/resources/qbx_core/types/player.md) | Players | Recurso `qbx_core` › tipos › player. Contiene: `Player`, `PlayerData`, `PlayerEntity`, `PlayerJob`, `PlayerGang`. |
| [docs/resources/qbx_core/types/vehicle.md](docs/resources/qbx_core/types/vehicle.md) | vehicle | Recurso `qbx_core` › tipos › vehicle. Contiene: `Vehicle`. |
| [docs/resources/qbx_diving/events/server.md](docs/resources/qbx_diving/events/server.md) | Server Events | Recurso `qbx_diving` › eventos › servidor. Contiene: `qbx_diving:server:coralTaken`, `qbx_diving:server:sellCoral`. |
| [docs/resources/qbx_garages/callbacks/client.md](docs/resources/qbx_garages/callbacks/client.md) | Client Callbacks | Recurso `qbx_garages` › callbacks › cliente. Contiene: `getGarages`, `getGarageVehicles`, `isParkable`, `parkVehicle`, `payDepotPrice` y 1 más. |
| [docs/resources/qbx_garages/exports/server.md](docs/resources/qbx_garages/exports/server.md) | Server Exports | Recurso `qbx_garages` › exports › servidor. Contiene: `RegisterGarage`, `SetVehicleGarage`, `SetVehicleDepotPrice`, `GetGarages`. |
| [docs/resources/qbx_management/convars.md](docs/resources/qbx_management/convars.md) | Convars | Recurso `qbx_management` › convars. Contiene: `enableGroupManagement`. |
| [docs/resources/qbx_management/exports/client.md](docs/resources/qbx_management/exports/client.md) | Client Exports | Recurso `qbx_management` › exports › cliente. Contiene: `OpenBossMenu`. |
| [docs/resources/qbx_management/exports/server.md](docs/resources/qbx_management/exports/server.md) | Server Exports | Recurso `qbx_management` › exports › servidor. Contiene: `RegisterBossMenu`. |
| [docs/resources/qbx_vehiclekeys/commands.md](docs/resources/qbx_vehiclekeys/commands.md) | Commands | Recurso `qbx_vehiclekeys` › comandos. Contiene: `Give Keys`, `Give permanent keys`. |
| [docs/resources/qbx_vehiclekeys/exports/client.md](docs/resources/qbx_vehiclekeys/exports/client.md) | Client Exports | Recurso `qbx_vehiclekeys` › exports › cliente. Contiene: `HasKeys`. |
| [docs/resources/qbx_vehiclekeys/exports/server.md](docs/resources/qbx_vehiclekeys/exports/server.md) | Server Exports | Recurso `qbx_vehiclekeys` › exports › servidor. Contiene: `HasKeys`, `GiveKeys`, `RemoveKeys`. |
| [docs/resources/qbx_vehicles/exports/hooks.md](docs/resources/qbx_vehicles/exports/hooks.md) | Hooks | Recurso `qbx_vehicles` › exports › hooks. Contiene: `createPlayerVehicle`, `changeVehicleOwner`. |
| [docs/resources/qbx_vehicles/exports/server.md](docs/resources/qbx_vehicles/exports/server.md) | Server Exports | Recurso `qbx_vehicles` › exports › servidor. Contiene: `CreatePlayerVehicle`, `DeletePlayerVehicles`, `DoesPlayerVehiclePlateExist`, `GetPlayerVehicle`, `GetPlayerVehicles` y 4 más. |
| [docs/tebex/slots/canuse.md](docs/tebex/slots/canuse.md) | Prevent Usage | Tebex › Casino Slots: impedir el uso de máquinas (hook propio). |
| [docs/tebex/slots/index.md](docs/tebex/slots/index.md) | 🎰 Casino Slots | Tebex › Casino Slots: presentación y características. |
| [docs/tebex/slots/installation.md](docs/tebex/slots/installation.md) | Installation | Tebex › Casino Slots: instalación. |
| [docs/tebex/slots/logging.md](docs/tebex/slots/logging.md) | Logging Functionality | Tebex › Casino Slots: registro de actividad (logs). |
| [docs/tebex/slots/requireditem.md](docs/tebex/slots/requireditem.md) | Required Item | Tebex › Casino Slots: ítem requerido para jugar. |
| [docs/tebex/weapon-audio/index.md](docs/tebex/weapon-audio/index.md) | 🔫 Weapon Audio | Tebex › Weapon Audio: presentación del paquete de sonidos de armas. |
| [docs/tebex/weapon-audio/installation.md](docs/tebex/weapon-audio/installation.md) | Installation | Tebex › Weapon Audio: instalación y aplicación de audios en weapons.meta. |
