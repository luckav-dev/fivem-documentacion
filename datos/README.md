# Datos oficiales en bruto

[← Inicio del repositorio](../README.md)

Archivos originales descargados el 20/10/2026. Los usan los scripts de [`herramientas/`](../herramientas/README.md), y puedes usarlos en tus propias herramientas (autocompletado, búsquedas, generadores).

| Archivo | Origen | Contenido |
|---|---|---|
| `natives.json` | https://static.cfx.re/natives/natives.json | Los 6.436 natives de GTA V agrupados por namespace: nombre, hash, jhash, parámetros, tipo devuelto, descripción, ejemplos y alias. |
| `natives_cfx.json` | https://static.cfx.re/natives/natives_cfx.json | Los natives propios de FiveM/RedM (CFX), con `apiset` (`client`, `server`, `shared`) y `game`. |
| `eventos_cliente.json` | https://runtime.fivem.net/doc/events/client.html.json | Lista oficial de eventos de cliente (HTML generado por TypeDoc). |
| `eventos_servidor.json` | https://runtime.fivem.net/doc/events/server.html.json | Lista oficial de eventos de servidor. |
| `rpc_spec_natives.lua` | `citizenfx/fivem` → `ext/natives/rpc_spec_natives.lua` | Natives de GTA V que FiveM permite llamar desde el servidor como RPC. |

Ejemplo: buscar un native por nombre con Python, sin internet:

```python
import json
natives = json.load(open('datos/natives.json', encoding='utf-8'))
for namespace, lista in natives.items():
    for h, n in lista.items():
        if n.get('name') == 'GET_ENTITY_COORDS':
            print(namespace, h, n['params'], n['results'])
```
