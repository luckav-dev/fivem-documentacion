# Referencia completa de natives (offline)

Generada el 2026-10-20 desde la base de datos oficial de Cfx.re. Contiene **6436 natives de GTA V** y **942 natives propios de FiveM (CFX)**: firma Lua, declaración C, parámetros, valor devuelto, descripción oficial, nombres antiguos y ejemplos oficiales.

- Para regenerarla con la versión más reciente: `python3 herramientas/generar_natives.py --descargar`.
- Para buscar un native sin internet: `grep -rn "GetEntityCoords" natives/` o el [índice alfabético](#índice-alfabético).

## Cómo leer cada entrada

- **Título**: nombre tal como lo escribes en Lua/JS (`GET_ENTITY_COORDS` → `GetEntityCoords`).
- **Línea de datos**: nombre oficial, hash (para `Citizen.InvokeNative`) y en qué lado se puede usar.
- **Bloque `lua`**: cómo se llama desde Lua. Los parámetros **puntero** (`int*`, `float*`, `Vector3*`…) **no se pasan**: se devuelven después de `retval`. Excepción del generador oficial: si el **único** puntero es el **último** parámetro, aparece como argumento (opcional) y también se devuelve.
- **Bloque `c`**: declaración original del native.
- **Parámetros `Hash`**: aceptan un string (FiveM lo convierte con `GetHashKey`).
- **Servidor (RPC)**: natives de GTA V que FiveM permite llamar desde el servidor; se ejecutan en el cliente dueño de la entidad.
- **Descripción oficial**: texto original de la documentación (inglés), sin modificar.

## Natives propios de FiveM (CFX)

| Lado | Natives | Archivos |
|---|---|---|
| compartidos | 98 | [compartidos.md](cfx/compartidos.md) |
| servidor | 290 | [servidor.md](cfx/servidor.md) |
| cliente | 554 | [cliente-1.md](cfx/cliente-1.md) · [cliente-2.md](cfx/cliente-2.md) |

## Natives de GTA V por namespace

| Namespace | Natives | Archivos |
|---|---|---|
| `APP` | 17 | [APP.md](gta5/APP.md) |
| `AUDIO` | 276 | [AUDIO.md](gta5/AUDIO.md) |
| `BRAIN` | 11 | [BRAIN.md](gta5/BRAIN.md) |
| `CAM` | 245 | [CAM.md](gta5/CAM.md) |
| `CLOCK` | 16 | [CLOCK.md](gta5/CLOCK.md) |
| `CUTSCENE` | 54 | [CUTSCENE.md](gta5/CUTSCENE.md) |
| `DATAFILE` | 57 | [DATAFILE.md](gta5/DATAFILE.md) |
| `DECORATOR` | 12 | [DECORATOR.md](gta5/DECORATOR.md) |
| `DLC` | 11 | [DLC.md](gta5/DLC.md) |
| `ENTITY` | 185 | [ENTITY.md](gta5/ENTITY.md) |
| `EVENT` | 13 | [EVENT.md](gta5/EVENT.md) |
| `FILES` | 47 | [FILES.md](gta5/FILES.md) |
| `FIRE` | 18 | [FIRE.md](gta5/FIRE.md) |
| `GRAPHICS` | 392 | [GRAPHICS.md](gta5/GRAPHICS.md) |
| `HUD` | 509 | [HUD.md](gta5/HUD.md) |
| `INTERIOR` | 45 | [INTERIOR.md](gta5/INTERIOR.md) |
| `ITEMSET` | 9 | [ITEMSET.md](gta5/ITEMSET.md) |
| `LOADINGSCREEN` | 8 | [LOADINGSCREEN.md](gta5/LOADINGSCREEN.md) |
| `LOCALIZATION` | 3 | [LOCALIZATION.md](gta5/LOCALIZATION.md) |
| `MISC` | 323 | [MISC.md](gta5/MISC.md) |
| `MOBILE` | 25 | [MOBILE.md](gta5/MOBILE.md) |
| `MONEY` | 301 | [MONEY.md](gta5/MONEY.md) |
| `NETSHOPPING` | 42 | [NETSHOPPING.md](gta5/NETSHOPPING.md) |
| `NETWORK` | 823 | [NETWORK-1.md](gta5/NETWORK-1.md) · [NETWORK-2.md](gta5/NETWORK-2.md) |
| `OBJECT` | 163 | [OBJECT.md](gta5/OBJECT.md) |
| `PAD` | 48 | [PAD.md](gta5/PAD.md) |
| `PATHFIND` | 59 | [PATHFIND.md](gta5/PATHFIND.md) |
| `PED` | 612 | [PED-1.md](gta5/PED-1.md) · [PED-2.md](gta5/PED-2.md) |
| `PHYSICS` | 49 | [PHYSICS.md](gta5/PHYSICS.md) |
| `PLAYER` | 248 | [PLAYER.md](gta5/PLAYER.md) |
| `RECORDING` | 17 | [RECORDING.md](gta5/RECORDING.md) |
| `REPLAY` | 6 | [REPLAY.md](gta5/REPLAY.md) |
| `SAVEMIGRATION` | 3 | [SAVEMIGRATION.md](gta5/SAVEMIGRATION.md) |
| `SCRIPT` | 37 | [SCRIPT.md](gta5/SCRIPT.md) |
| `SHAPETEST` | 11 | [SHAPETEST.md](gta5/SHAPETEST.md) |
| `SOCIALCLUB` | 83 | [SOCIALCLUB.md](gta5/SOCIALCLUB.md) |
| `STATS` | 311 | [STATS.md](gta5/STATS.md) |
| `STREAMING` | 121 | [STREAMING.md](gta5/STREAMING.md) |
| `SYSTEM` | 26 | [SYSTEM.md](gta5/SYSTEM.md) |
| `TASK` | 306 | [TASK.md](gta5/TASK.md) |
| `VEHICLE` | 751 | [VEHICLE-1.md](gta5/VEHICLE-1.md) · [VEHICLE-2.md](gta5/VEHICLE-2.md) |
| `WATER` | 12 | [WATER.md](gta5/WATER.md) |
| `WEAPON` | 122 | [WEAPON.md](gta5/WEAPON.md) |
| `ZONE` | 9 | [ZONE.md](gta5/ZONE.md) |

## Índice alfabético

[A](indice/A.md) · [B](indice/B.md) · [C](indice/C.md) · [D](indice/D.md) · [E](indice/E.md) · [F](indice/F.md) · [G](indice/G.md) · [H](indice/H.md) · [I](indice/I.md) · [K](indice/K.md) · [L](indice/L.md) · [M](indice/M.md) · [N](indice/N.md) · [N_0x](indice/N_0x.md) · [O](indice/O.md) · [P](indice/P.md) · [Q](indice/Q.md) · [R](indice/R.md) · [S](indice/S.md) · [T](indice/T.md) · [U](indice/U.md) · [V](indice/V.md) · [W](indice/W.md)
