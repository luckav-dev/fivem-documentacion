# Fuentes, autoría y uso

Este repositorio es una **copia de consulta personal y offline**. Reúne documentación pública de FiveM y de su ecosistema para no tener que ir a internet. Cada contenido pertenece a sus autores. Este archivo indica de dónde sale cada carpeta y en qué condiciones.

> ⚠️ **Mantén este repositorio privado.** Los repositorios de la documentación oficial de Cfx.re (`citizenfx/fivem-docs` y `citizenfx/natives`) **no incluyen un archivo de licencia**. Sin una licencia explícita, su contenido sigue protegido por derechos de autor. Tenerlo para tu consulta personal es razonable, pero **redistribuirlo públicamente no está autorizado** de forma expresa.

| Carpeta | Origen | Autoría / licencia | Idioma |
|---|---|---|---|
| [`guia/`](guia/README.md) | Escrita para este repositorio y verificada contra el código fuente y la documentación oficial (ver el [historial](HISTORIAL.md)). | Propia. | Español |
| [`natives/`](natives/README.md) | Generada con [`herramientas/generar_natives.py`](herramientas/generar_natives.py) desde `static.cfx.re/natives/natives.json` y `natives_cfx.json`. | Descripciones: documentación oficial de natives de Cfx.re y colaboradores (`citizenfx/natives`, `citizenfx/fivem` → `ext/native-decls`). Sin licencia explícita. | Formato e índices en español; descripciones originales en inglés |
| [`docs-oficiales/`](docs-oficiales/README.md) | Convertida con [`herramientas/convertir_docs_oficiales.py`](herramientas/convertir_docs_oficiales.py) desde `citizenfx/fivem-docs` (lo que se publica en docs.fivem.net), incluidas imágenes y vídeos. | Cfx.re y colaboradores. Sin licencia explícita. | Inglés (original) e índices en español |
| [`docs-terceros/`](docs-terceros/README.md) | Copias en Markdown de la documentación de Overextended, txAdmin, Qbox, QBCore, ESX y pma-voice. | Cada proyecto. txAdmin, ESX y pma-voice: **MIT**. Overextended, Qbox y QBCore: sin licencia explícita en su repositorio de documentación. Detalle en el `README.md` de cada carpeta. | Inglés (original) e índices en español |
| [`datos/`](datos/README.md) | Bases de datos oficiales en bruto (natives, eventos, RPC). | Cfx.re. | — |
| [`herramientas/`](herramientas/README.md) | Scripts para regenerar y comprobar todo lo anterior. | Propios. | Español |

## Fecha de las copias

Todas las copias se tomaron el **20 de octubre de 2026**. Cada página copiada indica en su primera línea la URL original, el repositorio y el *commit* exacto.

## Por qué el texto copiado está en inglés

Las páginas oficiales y las descripciones de los natives se han copiado **sin modificar**, para que sean exactamente lo que publica Cfx.re. Una traducción automática podría cambiar matices técnicos. Los índices, la navegación y la guía sí están en español.
