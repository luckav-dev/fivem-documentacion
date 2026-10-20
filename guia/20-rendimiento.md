[← 19-seguridad](19-seguridad.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [21-depuracion →](21-depuracion.md)

# 20. Rendimiento y optimización

## 20.1 Medir antes de optimizar

| Herramienta | Dónde | Qué muestra |
|---|---|---|
| `resmon 1` | F8 (cliente) | Tiempo de CPU (ms) y memoria de **cada recurso** en el cliente. |
| `profiler record 500` → `profiler view` / `profiler saveJSON archivo.json` | F8 o consola del servidor | Perfil detallado de N frames (visor en Chrome DevTools/Perfetto). |
| `cl_drawfps true` / `cl_drawperf true` | F8 | FPS y estadísticas. |
| `netgraph true` | F8 | Ping, pérdida de paquetes, ancho de banda. |
| `strdbg` / `strlist` / `strmem` | F8 | Streaming de assets y memoria. |
| txAdmin → *Dashboard* | Panel | CPU/RAM del servidor, gráfico de rendimiento por hilo. |
| `/perf` (Prometheus) | `http://IP:30120/perf/` | Histogramas de tiempo de tick (protegido con `sv_prometheusBasicAuthUser/Password`). |

> Algunos comandos de desarrollador del cliente (`resmon`, `strdbg`, `profiler`…) pueden requerir el **modo desarrollador**. Si ves *"Access denied for command"*, inicia FiveM con `+set moo 31337` o usa un canal de actualización de desarrollo (Ajustes → canal *Beta/Canary*).

**Referencia en `resmon`:** un recurso de cliente bien hecho debería estar en **0.00-0.02 ms** en reposo. Por encima de 0.10 ms constante, revisa; por encima de 0.5-1 ms, hay un problema serio.

## 20.2 Cliente: reglas de oro

1. **Nunca `Wait(0)` permanente** si no dibujas nada. Usa **espera dinámica** (8.1) o `lib.points`/`lib.zones` (ox_lib).
2. **Un solo bucle** por recurso que gestione varias cosas, mejor que diez bucles.
3. **Cachea** `PlayerPedId()`, coordenadas y vehículo: actualízalos cada 250-500 ms en vez de por frame (o usa `cache.*` de ox_lib).
4. **Evita natives caros por frame**: `GetGamePool`, `GetClosestVehicle`, `GetEntityCoords` de muchas entidades, raycasts.
5. **`RegisterKeyMapping`** en lugar de comprobar teclas cada frame.
6. **Eventos en lugar de *polling***: reacciona a `gameEventTriggered`, state bags o `lib.onCache` en lugar de comprobar cada frame si algo cambió.
7. Libera modelos/animaciones con `SetModelAsNoLongerNeeded`/`RemoveAnimDict`.
8. **NUI**: pocas actualizaciones por segundo, nada de animaciones pesadas ocultas (14.10).

```lua
-- ❌ Mal: 3 natives por frame, siempre
CreateThread(function()
    while true do
        local ped = PlayerPedId()
        local veh = GetVehiclePedIsIn(ped, false)
        if veh ~= 0 then
            local vel = GetEntitySpeed(veh) * 3.6
            SendNUIMessage({ vel = vel })    -- ¡60 mensajes por segundo a la NUI!
        end
        Wait(0)
    end
end)

-- ✅ Bien: solo actúa dentro de vehículo y a 10 Hz
CreateThread(function()
    while true do
        local veh = GetVehiclePedIsIn(PlayerPedId(), false)
        if veh ~= 0 then
            SendNUIMessage({ vel = math.floor(GetEntitySpeed(veh) * 3.6) })
            Wait(100)
        else
            Wait(1000)
        end
    end
end)
```

## 20.3 Servidor: reglas de oro

1. **No bloquees el hilo principal**: nada de bucles enormes sin `Wait`, ni lecturas de archivos gigantes en cada evento.
2. **Base de datos**: consultas indexadas, cacheadas y en lote; nunca por tick (16.4).
3. **Envía eventos solo a quien los necesita** (jugadores cercanos, por *scope* o bucket), no a `-1` constantemente.
4. **State bags** para estado persistente compartido en vez de reenviar eventos (13.4), pero sin meter tablas gigantes que cambian cada segundo.
5. **Eventos latentes** para datos grandes.
6. **Limita entidades**: limpia vehículos abandonados, objetos y peds de script. Miles de entidades en red degradan a todos.
7. **Reinicios programados** (txAdmin) cada 6-12 h en servidores grandes para liberar memoria.

## 20.4 Población y entidades

- La población (tráfico, peatones) consume CPU de los clientes y ancho de banda. Reduce densidad con los multiplicadores *ThisFrame* (12.12) o desactiva con `onesync_population false`/buckets sin población.
- Evita `SetEntityDistanceCullingRadius`: Cfx.re marca los natives de *culling* como obsoletos y con problemas conocidos sin solución.
- Borra entidades de script cuando ya no se usen (`DeleteEntity` en servidor).

## 20.5 Streaming

- Vigila el tamaño total de assets que descarga un jugador nuevo; cientos de vehículos/ropa en 4K → descargas de varios GB y *crasheos* por memoria.
- Optimiza texturas (15.9) y elimina recursos que no uses.
- Usa un **servidor de archivos/caché externo** (proxy de descargas, 25.3) en servidores grandes para no saturar el ancho de banda del servidor de juego.


## Ver también (documentación offline)

- [Oficial: scripting-manual/debugging/using-profiler](../docs-oficiales/scripting-manual/debugging/using-profiler.md)

---

[← 19-seguridad](19-seguridad.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [21-depuracion →](21-depuracion.md)
