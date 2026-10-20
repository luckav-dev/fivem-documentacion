# txAdmin — copia offline de la documentación

> Copia local en Markdown (GitHub Flavored Markdown) generada el 2026-10-20 para consulta sin conexión. El contenido de las páginas se mantiene en su idioma original (inglés), sin traducir ni resumir.

## Qué es

Documentación técnica de **txAdmin**, el panel web de administración de servidores FiveM/RedM incluido en FXServer: menú in-game, permisos, eventos emitidos, ficheros de receta (recipes), configuración por variables de entorno, logs, estado de Discord, traducciones y notas de desarrollo. Se copia la carpeta `docs/` del repositorio.

## Origen y licencia

| Dato | Valor |
| --- | --- |
| Repositorio | [citizenfx/txAdmin](https://github.com/citizenfx/txAdmin) |
| Commit copiado | [`8a9a414`](https://github.com/citizenfx/txAdmin/tree/8a9a41410000fd92a527fe11bae2b8eeeb8b10e0) (`8a9a41410000fd92a527fe11bae2b8eeeb8b10e0`) |
| Fecha de copia | 2026-10-20 |
| Licencia | **MIT** (archivo `LICENSE` del repositorio, © Take-Two Interactive Software, Inc.) |
| Archivos Markdown | 12 (0.1 MB) |
| Imágenes/recursos copiados | 2 (0.2 MB) en [`imagenes/`](imagenes/) |

Cada archivo empieza con una línea `> Fuente original: …` que enlaza el archivo exacto del repositorio en ese commit.

## Cómo se convirtió

- Origen: Markdown plano de `docs/`; el contenido se copia tal cual (solo se reescriben enlaces e imágenes).
- Los enlaces a código fuente del repositorio (`/core/...`) apuntan a GitHub en el commit copiado.
- La etiqueta literal `<Command>` de `dev-notes.md` se escapa (`&lt;Command&gt;`) para que GitHub la muestre.
- `dev-notes.md` contiene notas internas del autor (mezcla de inglés y portugués) y se conserva igual.
- Los enlaces internos se reescribieron como rutas relativas a los `.md` generados (con `#ancla` cuando existe); los enlaces externos se mantienen.
- Bloques de código copiados literalmente con su etiqueta de lenguaje; tablas conservadas.
- Imágenes referenciadas (del repositorio y externas descargables) copiadas a `imagenes/` (máx. 5 MB por archivo y ~40 MB por proyecto; las del repositorio tienen prioridad). Las externas se guardan en `imagenes/externas/<dominio>/`.

## Recursos omitidos

Ninguno: todas las imágenes referenciadas se copiaron.

## Observaciones y contenido no convertido

- `docs/palettes.json` (datos de colores, no documentación) no se convierte.
- dev-notes.md: el enlace `/core/playerLogic/playerClasses.ts#L281` no corresponde a ninguna página copiada; apunta a la URL de GitHub.

## Índice de archivos

### Raíz

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [custom-server-log.md](custom-server-log.md) | Logging Extra Data | Cómo registrar datos extra (comandos, eventos) en el log del servidor de txAdmin. |
| [dev-notes.md](dev-notes.md) | repo stuff | Notas internas de desarrollo del autor (tareas, ideas, referencias; texto en inglés y portugués). |
| [development.md](development.md) | txAdmin Development | Cómo preparar el entorno y desarrollar txAdmin (estructura, scripts, compilación). |
| [discord-status.md](discord-status.md) | Custom Discord Status Embed | Personalización del embed de estado del servidor en Discord. |
| [env-config.md](env-config.md) | Environment Configuration | Configuración de txAdmin mediante variables de entorno. |
| [events.md](events.md) | Events Broadcasted | Eventos que txAdmin emite a los recursos del servidor y sus datos. |
| [feature-graveyard.md](feature-graveyard.md) | Feature Graveyard | Funciones retiradas de txAdmin y el motivo. |
| [logs.md](logs.md) | Logging | Sistema de logs de txAdmin (tipos de log, almacenamiento, rotación). |
| [menu.md](menu.md) | In-Game Menu | Menú in-game de txAdmin: acceso, permisos, convars y comandos. |
| [permissions.md](permissions.md) | permissions | Lista de permisos de administrador de txAdmin. |
| [recipe.md](recipe.md) | Recipe Files | Formato de los archivos de receta (recipes) para desplegar servidores y sus acciones. |
| [translation.md](translation.md) | Translation Support | Cómo añadir o mejorar traducciones de txAdmin. |
