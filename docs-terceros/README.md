# Documentación de terceros (copia offline)

Copia local, en Markdown compatible con GitHub, de la documentación de frameworks y herramientas de FiveM de terceros, para poder consultarla sin conexión a internet. Generada el 2026-10-20.

- El contenido de cada página se conserva en su **idioma original (inglés)**, sin traducir ni resumir.
- Cada archivo empieza con una nota `> Fuente original: …` con el enlace al archivo del repositorio y el commit.
- Cada proyecto tiene su propio `README.md` (en español) con el origen, la licencia, cómo se convirtió y un índice completo con la descripción de cada archivo.

## Proyectos

| Proyecto | Repositorio @ commit | Licencia | Archivos .md | Imágenes | Tamaño total |
| --- | --- | --- | --- | --- | --- |
| [Overextended](overextended/README.md) | [overextended/docs](https://github.com/overextended/docs) @ `328e36f` | sin licencia explícita | 127 | 39 | 3.4 MB |
| [txAdmin](txadmin/README.md) | [citizenfx/txAdmin](https://github.com/citizenfx/txAdmin) @ `8a9a414` | MIT | 13 | 2 | 0.3 MB |
| [Qbox](qbox/README.md) | [Qbox-project/qbox-docs](https://github.com/Qbox-project/qbox-docs) @ `260c0ec` | sin licencia explícita | 83 | 47 | 4.9 MB |
| [QBCore](qbcore/README.md) | [qbcore-framework/qb-docs](https://github.com/qbcore-framework/qb-docs) @ `930c12e` | sin licencia explícita | 84 | 77 | 42.3 MB |
| [ESX Legacy](esx/README.md) | [esx-framework/esx-legacy-documenation](https://github.com/esx-framework/esx-legacy-documenation) @ `031b7f7` | MIT | 82 | 27 | 40.3 MB |
| [pma-voice](pma-voice/README.md) | [AvarianKnight/pma-voice](https://github.com/AvarianKnight/pma-voice) @ `6c9d96e` | MIT | 19 | 0 | 0.0 MB |

El número de archivos `.md` incluye el `README.md` de índice de cada proyecto.

## Contenido de cada proyecto

- [**Overextended**](overextended/README.md): ox_lib, oxmysql, ox_inventory, ox_target, ox_core, ox_doorlock, ox_fuel y guías.
- [**txAdmin**](txadmin/README.md): menú in-game, permisos, eventos, recetas, variables de entorno, logs.
- [**Qbox**](qbox/README.md): framework Qbox (qbx_core y recursos qbx_*), Qbox Dashboard, Tebex y blog.
- [**QBCore**](qbcore/README.md): guías, referencia de qb-core y recursos qb-*.
- [**ESX Legacy**](esx/README.md): es_extended, recursos del núcleo, addons esx_* y tutoriales.
- [**pma-voice**](pma-voice/README.md): sistema de voz (convars, exports, eventos, state bags).

## Regenerar

La copia se generó con scripts de conversión fuera del repositorio (clonado con `git clone --depth 1` de cada repositorio de origen, conversión MDX/GitBook/Docusaurus/Nextra → GFM y validación de enlaces, vallas de código y restos de MDX). Para actualizarla, vuelve a clonar los repositorios y repite la conversión.
