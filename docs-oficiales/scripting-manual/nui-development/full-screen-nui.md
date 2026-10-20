# Fullscreen NUI

> Fuente original: https://docs.fivem.net/docs/scripting-manual/nui-development/full-screen-nui/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../README.md)

The most common use case of NUI is a full-screen 'UI page', which is overlaid on top of the game and may or may not have
input focus. These are supported on both FiveM and RedM at this time, and are part of basic Citizen framework level
support.

The following natives are related to using full-screen NUI:

- [`SEND_NUI_MESSAGE`](../../../natives/cfx/cliente-1.md#sendnuimessage)
- [`SET_NUI_FOCUS`](../../../natives/cfx/cliente-1.md#setnuifocus)

## Setting up a fullscreen NUI page

To assign a full-screen NUI page to a resource, currently you need to specify a single `ui_page` in the
[resource manifest][resource-manifest] for the resource containing an UI page, like shown below:

```lua
-- specify the root page, relative to the resource
ui_page 'main.html'

-- every client-side file still needs to be added to the resource packfile!
files {
    'main.html',
    'build/main.js',
}
```

```lua
-- a page can also be hosted externally
ui_page 'https://ui-frontend.cfx.example.com/b20210501/index.html'
```

## Referencing other assets

The NUI system registers a `https://cfx-nui-` protocol scope for resource files. Therefore, you can reference a file in a resource
as follows:

```html
<script type="text/javascript" src="https://cfx-nui-my-resource/production.js" async></script>
```

This formerly was known as `nui://`, but this is no longer a secure context in newer browser versions.

## Developer tools

CEF remote debugging tools are exposed on [http://localhost:13172/](http://localhost:13172/) as long as the game is
running. You can use any Chromium-based browser to easily access these tools.

Alternately, it can be opened using the `nui_devTools` command in the game's <kbd>F8</kbd> console, assuming the
developer mode is enabled.

## NUI focus

There's a limited focus stack for NUI resources, you can set focus to the **current** resource using the
[`SET_NUI_FOCUS`](../../../natives/cfx/cliente-1.md#setnuifocus) native, which will set keyboard focus and/or mouse cursor focus depending on the
provided arguments.

The most recently focused resource will be ordered on top of the focus stack, and resources are currently implemented
as full-screen iframes: that means there's no click-through across resources.

## NUI messages

You can send a [message][mdn-messages] to the current resource's NUI page using the [`SEND_NUI_MESSAGE`](../../../natives/cfx/cliente-1.md#sendnuimessage)
native, or if using Lua, the convenience wrapper
[SendNUIMessage][send-nui-message] which encodes a JSON string for you..

For example:



```lua
-- Lua
SendNUIMessage({
    type = 'open'
})
```





```js
// JS
SendNuiMessage(JSON.stringify({
    type: 'open'
}))
```





```csharp
// C#, assumes Newtonsoft.Json PCL version is referenced
SendNuiMessage(JsonConvert.SerializeObject(new
{
    type = "open"
}));
```



```js
// browser side
window.addEventListener('message', (event) => {
    if (event.data.type === 'open') {
        doOpen();
    }
});
```

[mdn-messages]: https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage#The_dispatched_event
[send-nui-message]: ../../scripting-reference/runtimes/lua/functions/SendNUIMessage.md
[resource-manifest]: ../../scripting-reference/resource-manifest/README.md
