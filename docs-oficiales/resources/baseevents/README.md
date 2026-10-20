# baseevents

> Fuente original: https://docs.fivem.net/docs/resources/baseevents/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

## About

This resource adds basic events for developers to use in their scripts. Some third party resources may depend on this resource, if this is the case then you must start this resource _before_ starting that third party resource.

## Exports

This resource does not have any export functions.

## Events

### Client

- [`baseevents:onPlayerDied`](events/onPlayerDied.md)
- [`baseevents:onPlayerKilled`](events/onPlayerKilled.md)
- [`baseevents:onPlayerWasted`](events/onPlayerWasted.md)

### Server

- [`baseevents:onPlayerDied`](events/onPlayerDied.md)
- [`baseevents:onPlayerKilled`](events/onPlayerKilled.md)
- [`baseevents:onPlayerWasted`](events/onPlayerWasted.md)
- [`baseevents:enteringVehicle`](events/enteringVehicle.md)
- [`baseevents:enteringAborted`](events/enteringAborted.md)
- [`baseevents:enteredVehicle`](events/enteredVehicle.md)
- [`baseevents:leftVehicle`](events/leftVehicle.md)

**Note:** Don't forget to add `ensure baseevents` in server.cfg.
