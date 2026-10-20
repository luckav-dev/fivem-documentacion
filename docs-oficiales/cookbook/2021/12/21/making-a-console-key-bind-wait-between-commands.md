# Making a Console Key Bind Wait Between Commands

> Fuente original: https://docs.fivem.net/docs/cookbook/2021/12/21/making-a-console-key-bind-wait-between-commands/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

> **⚠️ Advertencia — Cookbook Archive**
>
> **Note:** This Cookbook article was originally published on **December 21, 2021**. Newer information may exist.


Someone recently asked in a chat room if it were possible to delay executing multiple different commands when using the `bind` command in the F8 console to make custom key binds.

This is, of course, entirely possible using a variant of the `wait` command taken from Quake:

```
# this will run 'say hello', wait 1.5 second (1500 milliseconds), and run 'e wave'
bind keyboard F11 "say hello; wait 1500; e wave"
```

---

*Original discussion thread: [https://forum.fivem.net/t/making-a-console-key-bind-wait-between-commands/4791223](https://forum.fivem.net/t/making-a-console-key-bind-wait-between-commands/4791223)*
