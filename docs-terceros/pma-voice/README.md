# pma-voice — copia offline de la documentación

> Copia local en Markdown (GitHub Flavored Markdown) generada el 2026-10-20 para consulta sin conexión. El contenido de las páginas se mantiene en su idioma original (inglés), sin traducir ni resumir.

## Qué es

**pma-voice**: sistema de voz para FiveM/RedM basado en el servidor Mumble interno. El README explica compatibilidad, convars de configuración y la lista de exports; la carpeta `docs/` documenta cada export de cliente/servidor, eventos, *state bags* y los *routing buckets*.

## Origen y licencia

| Dato | Valor |
| --- | --- |
| Repositorio | [AvarianKnight/pma-voice](https://github.com/AvarianKnight/pma-voice) |
| Commit copiado | [`6c9d96e`](https://github.com/AvarianKnight/pma-voice/tree/6c9d96ed7a02e30912f1a0ce92629bf9afbbca8c) (`6c9d96ed7a02e30912f1a0ce92629bf9afbbca8c`) |
| Fecha de copia | 2026-10-20 |
| Licencia | **MIT** (archivo `LICENSE` del repositorio, © 2021 Dillon Skaggs) |
| Archivos Markdown | 18 (0.0 MB) |
| Imágenes/recursos copiados | ninguno |

Cada archivo empieza con una línea `> Fuente original: …` que enlaza el archivo exacto del repositorio en ese commit.

## Cómo se convirtió

- Origen: `README.md` y carpeta `docs/` (Markdown plano). El README original se guarda como `README-original.md`.
- Contenido copiado tal cual; solo se reescriben los enlaces a `docs/…` para que apunten a los `.md` locales.
- No se incluyen archivos que no son documentación (`TODO.md`, código, `docs/_config.yml` de Jekyll).
- Los enlaces internos se reescribieron como rutas relativas a los `.md` generados (con `#ancla` cuando existe); los enlaces externos se mantienen.
- Bloques de código copiados literalmente con su etiqueta de lenguaje; tablas conservadas.
- Imágenes referenciadas (del repositorio y externas descargables) copiadas a `imagenes/` (máx. 5 MB por archivo y ~40 MB por proyecto; las del repositorio tienen prioridad). Las externas se guardan en `imagenes/externas/<dominio>/`.

## Recursos omitidos

Ninguno: todas las imágenes referenciadas se copiaron.

## Observaciones y contenido no convertido

- Nada relevante: todo el contenido se convirtió.

## Índice de archivos

### Raíz

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [README-original.md](README-original.md) | pma-voice | README original: aviso de cambios, compatibilidad, convars de configuración y lista de exports. |

### `docs/`

| Archivo | Título original | Contenido |
| --- | --- | --- |
| [docs/client-getters/events.md](docs/client-getters/events.md) | events | Eventos de cliente que emite pma-voice. |
| [docs/client-setters/removePlayerFromCall.md](docs/client-setters/removePlayerFromCall.md) | removePlayerFromCall | Export de cliente (setter) `removePlayerFromCall`: uso y ejemplo. |
| [docs/client-setters/removePlayerFromRadio.md](docs/client-setters/removePlayerFromRadio.md) | removePlayerFromRadio | Export de cliente (setter) `removePlayerFromRadio`: uso y ejemplo. |
| [docs/client-setters/setCallChannel.md](docs/client-setters/setCallChannel.md) | setCallChannel | Export de cliente (setter) `setCallChannel`: uso y ejemplo. |
| [docs/client-setters/setCallVolume.md](docs/client-setters/setCallVolume.md) | setCallVolume | Export de cliente (setter) `setCallVolume`: uso y ejemplo. |
| [docs/client-setters/setMicClickOffVolume.md](docs/client-setters/setMicClickOffVolume.md) | setMicClickOffVolume | Export de cliente (setter) `setMicClickOffVolume`: uso y ejemplo. |
| [docs/client-setters/setMicClickOnVolume.md](docs/client-setters/setMicClickOnVolume.md) | setMicClickOnVolume | Export de cliente (setter) `setMicClickOnVolume`: uso y ejemplo. |
| [docs/client-setters/setRadioChannel.md](docs/client-setters/setRadioChannel.md) | setRadioChannel | Export de cliente (setter) `setRadioChannel`: uso y ejemplo. |
| [docs/client-setters/setRadioVolume.md](docs/client-setters/setRadioVolume.md) | setRadioVolume | Export de cliente (setter) `setRadioVolume`: uso y ejemplo. |
| [docs/client-setters/setVoiceProperty.md](docs/client-setters/setVoiceProperty.md) | setVoiceProperty | Export de cliente (setter) `setVoiceProperty`: uso y ejemplo. |
| [docs/routingBuckets.md](docs/routingBuckets.md) | routingBuckets | Soporte de pma-voice para routing buckets. |
| [docs/server-getters/getPlayersInRadioChannel.md](docs/server-getters/getPlayersInRadioChannel.md) | getPlayersInRadioChannel | Export de servidor (getter) `getPlayersInRadioChannel`: uso y ejemplo. |
| [docs/server-setters/addChannelCheck.md](docs/server-setters/addChannelCheck.md) | addChannelCheck | Export de servidor (setter) `addChannelCheck`: uso y ejemplo. |
| [docs/server-setters/removeChannelCheck.md](docs/server-setters/removeChannelCheck.md) | removeChannelCheck | Export de servidor (setter) `removeChannelCheck`: uso y ejemplo. |
| [docs/server-setters/setPlayerCall.md](docs/server-setters/setPlayerCall.md) | setPlayerCall | Export de servidor (setter) `setPlayerCall`: uso y ejemplo. |
| [docs/server-setters/setPlayerRadio.md](docs/server-setters/setPlayerRadio.md) | setPlayerRadio | Export de servidor (setter) `setPlayerRadio`: uso y ejemplo. |
| [docs/state-getters/stateBagGetters.md](docs/state-getters/stateBagGetters.md) | stateBagGetters | State bags del jugador que expone pma-voice (radio, llamada, proximidad…). |
