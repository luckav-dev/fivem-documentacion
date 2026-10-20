# Citizen.Trace

> Fuente original: https://docs.fivem.net/docs/scripting-reference/runtimes/lua/functions/Citizen.Trace/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

## Syntax

```lua
Citizen.Trace(message)
```

Outputs the passed message to any trace listeners, including the console output and the log file. Does not add a newline
by itself, therefore suffix a message with `"\n"`.

## Examples

This example will print "Hello, World!".

```lua
Citizen.Trace("Hello, World!\n")
```

<!--
is this function even exclusive to lua? and where is it defined?
alias: RconPrint
-->
