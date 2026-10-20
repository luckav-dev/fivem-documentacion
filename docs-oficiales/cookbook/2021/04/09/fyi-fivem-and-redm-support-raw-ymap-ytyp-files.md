# FYI: FiveM and RedM support raw .ymap/.ytyp files

> Fuente original: https://docs.fivem.net/docs/cookbook/2021/04/09/fyi-fivem-and-redm-support-raw-ymap-ytyp-files/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

> **⚠️ Advertencia — Cookbook Archive**
>
> **Note:** This Cookbook article was originally published on **April 09, 2021**. Newer information may exist.


For a while now, you've been able to use XML-format .ytyp/.ymap files in FiveM and RedM, without doing a conversion between XML and PSO/RSC format: just make sure the .xml file is just named `mh1_01.ymap` without any extra extension, and it should be parsed and used fine.

Note that these are loaded using the game parser, so this may behave differently in some ways from CodeWalker/OpenIV's parsers.

---

*Original discussion thread: [https://forum.fivem.net/t/fyi-fivem-and-redm-support-raw-ymap-ytyp-files/2597624](https://forum.fivem.net/t/fyi-fivem-and-redm-support-raw-ymap-ytyp-files/2597624)*
