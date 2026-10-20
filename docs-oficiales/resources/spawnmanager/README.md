# spawnmanager

> Fuente original: https://docs.fivem.net/docs/resources/spawnmanager/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

## About

The spawnmanager is a base resource that handles the spawning of the player. It allows you to choose when and where to spawn the player and also control how they respawn.

Spawnmanager is included and maintained at the [cfx-server-data](https://github.com/citizenfx/cfx-server-data) repository.

Map resources for [mapmanager](../mapmanager/README.md) will have their spawnpoints loaded and usable in spawnmanager, as long as they are started *after* spawnmanager.

## Exports

### Client

- [spawnPlayer](functions/spawnPlayer.md)
- [addSpawnPoint](functions/addSpawnPoint.md)
- [removeSpawnPoint](functions/removeSpawnPoint.md)
- [loadSpawns](functions/loadSpawns.md)
- [setAutoSpawn](functions/setAutoSpawn.md)
- [setAutoSpawnCallback](functions/setAutoSpawnCallback.md)
- [forceRespawn](functions/forceRespawn.md)

## Events

### Client

- [playerSpawned](events/playerSpawned.md)
