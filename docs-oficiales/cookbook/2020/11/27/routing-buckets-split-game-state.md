# Routing Buckets: Split Game State

> Fuente original: https://docs.fivem.net/docs/cookbook/2020/11/27/routing-buckets-split-game-state/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

> **⚠️ Advertencia — Cookbook Archive**
>
> **Note:** This Cookbook article was originally published on **November 28, 2020**. Newer information may exist.


Server versions from pipeline ID 3245 and above have added a 'routing bucket' functionality, which is similar in concept to the 'dimension' or 'virtual world' functionality seen in prior non-Rockstar GTA network implementations.

For those unaware or lazy to search, one can assign a player or entity to a routing bucket, and they will only see entities (and players) that belong to the same routing bucket. In addition to that, each routing bucket will have its own 'world grid' for determining population owners, so even if you have population enabled, you'll notice nothing unusual at all when using routing buckets.

Example use cases include:

*   Multi-mode servers where you want to have different games go on without affecting other games
*   Session/party systems
*   'Character screen' being instanced differently from gameplay going on

Example use cases do **explicitly not include interiors.** Interiors should be using the traditional 'conceal' native functions, or the future support for 3D-scoped routing policy, which will also allow specifying any 'instanced' zone for MMO-style servers so a server can have a map area 'dedicated' to a player/party on a mission but still be able to see everything going on outside that zone.

https://www.youtube.com/watch?v=U5kPy0SAXNE&feature=youtu.be&t=275

See the linked timestamp in this GTA Online trailer to see _why_ interiors should not be handled using this support in GTAV, where this was fine in GTA3 series titles because they did not have any interiors looking outwards.

The natives to use are as follows:

*   [GET\_ENTITY\_ROUTING\_BUCKET](../../../../../natives/cfx/servidor.md#getentityroutingbucket)
*   [GET\_PLAYER\_ROUTING\_BUCKET](../../../../../natives/cfx/servidor.md#getplayerroutingbucket)
*   [SET\_ENTITY\_ROUTING\_BUCKET](../../../../../natives/cfx/servidor.md#setentityroutingbucket)
*   [SET\_PLAYER\_ROUTING\_BUCKET](../../../../../natives/cfx/servidor.md#setplayerroutingbucket)

Note that these natives require OneSync to be 'on', _not set to 'legacy' mode_, and at this time might still route game events such as explosions and projectiles - this will be fixed in a near-future server version, as will support for sending network events to a specific routing bucket only.

---

*Original discussion thread: [https://forum.fivem.net/t/routing-buckets-split-game-state/1831709](https://forum.fivem.net/t/routing-buckets-split-game-state/1831709)*
