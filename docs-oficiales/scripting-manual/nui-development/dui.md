# Direct-Rendered UI

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/dui/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

In FiveM, you can also render NUI to a runtime texture, which is called DUI for 'direct NUI'. The following natives help
with this:

- [`CREATE_DUI`](../../../natives/cfx/cliente-1.md#createdui)
- [`CREATE_RUNTIME_TEXTURE_FROM_DUI_HANDLE`](../../../natives/cfx/cliente-1.md#createruntimetexturefromduihandle)
- [`DESTROY_DUI`](../../../natives/cfx/cliente-1.md#destroydui)
- [`GET_DUI_HANDLE`](../../../natives/cfx/cliente-1.md#getduihandle)
- [`IS_DUI_AVAILABLE`](../../../natives/cfx/cliente-1.md#isduiavailable)
- [`SEND_DUI_MESSAGE`](../../../natives/cfx/cliente-1.md#sendduimessage)
- [`SEND_DUI_MOUSE_DOWN`](../../../natives/cfx/cliente-1.md#sendduimousedown)
- [`SEND_DUI_MOUSE_MOVE`](../../../natives/cfx/cliente-1.md#sendduimousemove)
- [`SEND_DUI_MOUSE_UP`](../../../natives/cfx/cliente-1.md#sendduimouseup)
- [`SEND_DUI_MOUSE_WHEEL`](../../../natives/cfx/cliente-1.md#sendduimousewheel)
- [`SET_DUI_URL`](../../../natives/cfx/cliente-1.md#setduiurl)

The native documentation contains information for each of these, but here are some creative use cases for this:

- Rendering in 2D space using [`DRAW_SPRITE`](../../../natives/gta5/GRAPHICS.md#drawsprite)
- Rendering to a game render target object using similar natives.
- Rendering arbitrarily in world space using a specialized Scaleform, like in this
  [forum topic](https://forum.cfx.re/t/131208).

This can be used to make cinema screens, asynchronous in-game hint overlays, etc. fairly trivially.
