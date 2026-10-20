> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Points/JavaScript/Client.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Client

## Points

Simple and centralised distance checking, supporting callbacks when entering, leaving, and standing in-range of set coordinates.

```ts
Point<T>({ coords, distance, onEnter, onExit, nearby, args });
```

- coords: `number[]`
- distance: `number`
- onEnter?: `function`
- onExit?: `function`
- nearby?: `function`
- args?: `T`

```ts
import { Point, cache } from "@overextended/ox_lib/client";

function nearby(this: Point<{ dunak: string }>) {
  // @ts-ignore
  DrawMarker(
    2,
    this.coords.x,
    this.coords.y,
    this.coords.z,
    0,
    0,
    0,
    0,
    180,
    0,
    1,
    1,
    1,
    200,
    20,
    20,
    50,
    false,
    true,
    2,
    false,
    null,
    null,
    false,
  );

  if (this.currentDistance && this.currentDistance < 1 && IsControlJustReleased(0, 38)) {
    console.log("Inside marker", this.id);
    console.log(this.args?.dunak);
  }
}

const point = new Point({
  coords: GetEntityCoords(cache.ped, false),
  distance: 5,
  nearby: nearby,
  args: {
    dunak: "nerd",
  },
});

point.onEnter = () => {
  console.log("Entered range of point", point.id);
};

point.onExit = () => {
  console.log("Left range of point", point.id);
};
```
