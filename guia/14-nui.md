[← 13-red-onesync-statebags-buckets](13-red-onesync-statebags-buckets.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [15-streaming-assets →](15-streaming-assets.md)

# 14. NUI (interfaces web dentro del juego)

**NUI** (*New UI*) permite mostrar interfaces hechas con **HTML/CSS/JavaScript** encima del juego, renderizadas con un navegador Chromium (CEF) embebido. Se usa para HUDs, menús, inventarios, teléfonos, tablets policiales, pantallas de carga…

## 14.1 Estructura mínima

```
mi_ui/
├── fxmanifest.lua
├── client.lua
└── html/
    ├── index.html
    ├── style.css
    └── app.js
```

```lua
-- fxmanifest.lua
fx_version 'cerulean'
game 'gta5'

ui_page 'html/index.html'
files { 'html/index.html', 'html/style.css', 'html/app.js' }
client_script 'client.lua'
```

```html
<!-- html/index.html -->
<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <link rel="stylesheet" href="style.css">
</head>
<body>
  <div id="menu" class="oculto">
    <h1 id="titulo">Menú</h1>
    <button id="cerrar">Cerrar</button>
  </div>
  <script src="app.js"></script>
</body>
</html>
```

```css
/* html/style.css: el fondo SIEMPRE transparente */
html, body { margin: 0; background: transparent; font-family: sans-serif; overflow: hidden; }
.oculto { display: none; }
#menu { position: absolute; top: 50%; left: 50%; transform: translate(-50%, -50%);
        background: rgba(20,20,20,.9); color: #fff; padding: 24px; border-radius: 12px; }
```

## 14.2 Lua → NUI: `SendNUIMessage`

```lua
-- client.lua
local abierto = false

local function abrirMenu()
    abierto = true
    SetNuiFocus(true, true)                 -- (foco de teclado, cursor)
    SendNUIMessage({ action = 'abrir', titulo = 'Tienda 24/7' })
end

RegisterCommand('menu', abrirMenu, false)
```

```js
// html/app.js
window.addEventListener('message', (event) => {
  const data = event.data;
  if (data.action === 'abrir') {
    document.getElementById('titulo').textContent = data.titulo;
    document.getElementById('menu').classList.remove('oculto');
  }
});
```

## 14.3 NUI → Lua: `RegisterNUICallback` + `fetch`

```js
// html/app.js
document.getElementById('cerrar').addEventListener('click', async () => {
  document.getElementById('menu').classList.add('oculto');
  const resp = await fetch(`https://${GetParentResourceName()}/cerrar`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=UTF-8' },
    body: JSON.stringify({ motivo: 'boton' }),
  });
  const json = await resp.json();
  console.log(json);
});

// Cerrar con ESC
window.addEventListener('keydown', (e) => {
  if (e.key === 'Escape') document.getElementById('cerrar').click();
});
```

```lua
-- client.lua
RegisterNUICallback('cerrar', function(data, cb)
    abierto = false
    SetNuiFocus(false, false)
    print('Cerrado por: ' .. tostring(data.motivo))
    cb({ ok = true })     -- ¡SIEMPRE responde al callback, o el fetch se queda colgado!
end)
```

- `RegisterNuiCallback` es un alias de `RegisterNUICallback`. Para recibir el cuerpo sin procesar existe `RegisterRawNuiCallback`.
- `GetParentResourceName()` es una función que FiveM inyecta en la página NUI y devuelve el nombre del recurso.
- La URL es `https://<nombre_recurso>/<callback>`.
- Los datos viajan como JSON.

## 14.4 Foco, ratón y teclado

| Native | Descripción |
|---|---|
| `SetNuiFocus(teclado, cursor)` | Da el foco a la NUI. **Recuerda quitarlo al cerrar.** |
| `SetNuiFocusKeepInput(true)` | Mantiene los controles del juego mientras la NUI tiene foco (para HUDs interactivos; combínalo con `DisableControlAction` para lo que no quieras). |
| `IsNuiFocused()` | ¿Tiene foco la NUI? |
| `SetCursorLocation(x, y)` | Mueve el cursor (0.0-1.0). |

> Si un jugador se queda "atascado" sin poder moverse, casi siempre es una NUI que no ha llamado a `SetNuiFocus(false, false)`. Añade siempre un `onResourceStop` que lo quite.

## 14.5 Rutas de archivos dentro de NUI

| Ruta | Uso |
|---|---|
| `https://cfx-nui-mi_recurso/html/img.png` | **Forma recomendada** para archivos de un recurso (deben estar en `files`). |
| `nui://mi_recurso/html/img.png` | Forma antigua. Sigue funcionando para cargar archivos, pero **ya no es un "contexto seguro"** (APIs del navegador como portapapeles, cripto, etc. pueden fallar). |
| Rutas relativas (`img/logo.png`) | Relativas a la `ui_page`. |

Imágenes de ítems de inventario, por ejemplo: `https://cfx-nui-ox_inventory/web/images/agua.png`.

## 14.6 Depurar la NUI

- **Con el juego abierto**, las herramientas de depuración remota de CEF están en **http://localhost:13172/**: ábrelo desde Chrome/Edge en el mismo PC y elige la página de tu recurso (documentación oficial).
- También puedes abrirlas con **`nui_devTools`** en la consola F8, pero solo si el **modo desarrollador** está activo.
- `console.log` dentro de la NUI aparece en las DevTools, **no** en F8.
- Para desarrollar con *hot-reload*, puedes apuntar `ui_page` a `http://localhost:5173` mientras desarrollas con Vite (y volver a la build final para producción).

## 14.7 NUI con React/Vue/Svelte + Vite

1. Crea el proyecto en `mi_recurso/web`: `npm create vite@latest web -- --template react-ts`.
2. En `vite.config.ts` pon `base: './'` para que las rutas sean relativas y `build.outDir: 'dist'`.
3. `npm run build` → genera `web/dist`.
4. Manifest:

```lua
ui_page 'web/dist/index.html'
files { 'web/dist/index.html', 'web/dist/assets/*' }
```

Helper de `fetch` para NUI (TypeScript):

```ts
export async function fetchNui<T = unknown>(evento: string, data?: unknown): Promise<T> {
  const recurso = (window as any).GetParentResourceName ? (window as any).GetParentResourceName() : 'nui-dev';
  const resp = await fetch(`https://${recurso}/${evento}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json; charset=UTF-8' },
    body: JSON.stringify(data ?? {}),
  });
  return resp.json();
}
```

Hook para escuchar mensajes:

```ts
import { useEffect } from 'react';

export function useNuiEvent<T>(action: string, handler: (data: T) => void) {
  useEffect(() => {
    const listener = (e: MessageEvent) => {
      if (e.data?.action === action) handler(e.data.data);
    };
    window.addEventListener('message', listener);
    return () => window.removeEventListener('message', listener);
  }, [action, handler]);
}
```

> Hay *boilerplates* populares que ya traen esto montado (p. ej. `project-error/fivem-react-boilerplate-lua` —React 19 + Vite— o `overextended/fivem-typescript-boilerplate`). Búscalos en GitHub.

## 14.8 Pantalla de carga (*loadscreen*)

```lua
-- fxmanifest.lua de un recurso de loadscreen
fx_version 'cerulean'
game 'gta5'

loadscreen 'index.html'
loadscreen_manual_shutdown 'yes'   -- opcional
files { 'index.html', 'style.css', 'script.js', 'music.ogg', 'bg.webm' }   -- formatos libres (ver 14.11)
client_script 'client.lua'
```

```lua
-- client.lua (solo si loadscreen_manual_shutdown = 'yes')
AddEventHandler('playerSpawned', function()
    ShutdownLoadingScreenNui()
end)
```

Eventos que recibe la pantalla de carga (en `window.addEventListener('message')`):

```js
const handlers = {
  startInitFunctionOrder(data) { /* data.type, data.order, data.count */ },
  initFunctionInvoking(data)   { /* data.name, data.idx */ },
  startDataFileEntries(data)   { /* data.count */ },
  performMapLoadFunction(data) { /* data.idx */ },
  onLogLine(data)              { console.log(data.message); },
  loadProgress(data)           { document.querySelector('#barra').style.width = `${data.loadFraction * 100}%`; },
};
window.addEventListener('message', (e) => (handlers[e.data.eventName] || (() => {}))(e.data));
```

Dentro de la pantalla de carga también tienes `window.nuiHandoverData`: el bloque de *handover* de la conexión (ver `deferrals.handover`, 8.14) más `serverAddress` (dirección del servidor).

- El native `SetManualShutdownLoadingScreenNui` está **obsoleto**: usa `loadscreen_manual_shutdown 'yes'` en el manifest.
- `setr sv_showBusySpinnerOnLoadingScreen false` oculta el icono giratorio de carga.

## 14.9 DUI (páginas web como texturas en el mundo)

Las **DUI** permiten renderizar una página web en una **textura** (pantallas de TV, carteles, cines):

```lua
local dui = CreateDui('https://ejemplo.com', 1280, 720)
local handle = GetDuiHandle(dui)
local txd = CreateRuntimeTxd('mi_tv_txd')
CreateRuntimeTextureFromDuiHandle(txd, 'mi_tv_tex', handle)

-- Opción A: dibujarla en pantalla (cada frame)
-- DrawSprite('mi_tv_txd', 'mi_tv_tex', 0.5, 0.5, 0.3, 0.3, 0.0, 255, 255, 255, 255)

-- Opción B: sustituir la textura de un modelo del mundo
-- ⚠️ La documentación oficial marca AddReplaceTexture como "Experimental natives,
--    please do not use in a live environment".
AddReplaceTexture('prop_tv_flat_01', 'script_rt_tvscreen', 'mi_tv_txd', 'mi_tv_tex')

-- Otros: SetDuiUrl(dui, url), SendDuiMessage(dui, json.encode({...})), IsDuiAvailable(dui),
-- SendDuiMouseMove/Down/Up/Wheel(...), DestroyDui(dui)
```

## 14.10 Rendimiento NUI

- Una NUI con animaciones CSS pesadas, vídeos o `setInterval` rápidos **consume FPS** aunque esté oculta. Pausa lo que no se ve.
- Envía mensajes solo cuando cambian los datos, no cada frame (para un HUD de velocidad, 10-20 veces/seg es suficiente).
- Usa imágenes optimizadas (WebP) y evita fuentes enormes.
- No cargues frameworks gigantes para una UI simple.

## 14.11 Qué soporta el navegador de FiveM (CEF): referencia verificada

Todo lo de esta sección sale del **código fuente del cliente** (`code/components/nui-core`, `glue/NUIMediaAccess.cpp`, `nui-core/include/EpoxyScript.h`) en la build *latest* 37579 (20/10/2026) y de la documentación oficial de NUI.

### Motor

| Dato | Valor |
|---|---|
| Motor | **Chromium Embedded Framework** (fork `citizenfx/cef`). |
| Versión | **CEF 144.19.61 / Chromium 144.0.7559** (`cef_binary_144.19.61-cfx-m144-osr`) en el código actual. Builds de servidor/cliente anteriores pueden traer un Chromium más antiguo. |
| Renderizado | Fuera de pantalla (*OSR*), compuesto encima del juego. Aceleración por GPU (`enable-gpu-rasterization`, `ignore-gpu-blocklist`), ANGLE sobre **Direct3D 11**. |
| WebGL | Soportado y acelerado (la documentación oficial menciona *"accelerated WebGL"*). El propio FiveM usa **WebGL2**. |
| Codificación por defecto | UTF-8. |
| Cada recurso | Es un **iframe a pantalla completa**: no hay *click-through* entre recursos y el foco funciona como una **pila**: el último recurso que pidió `SetNuiFocus` queda encima. |

### Funciones que FiveM activa o fuerza

| Función | Estado |
|---|---|
| Reproducción automática de audio y vídeo | ✅ **Sin necesidad de gesto del usuario** (`autoplay-policy=no-user-gesture-required`): `audio.play()` funciona directamente. |
| `localStorage` | ✅ Persiste entre sesiones del juego (FiveM desactiva `ThirdPartyStoragePartitioning` precisamente para no perder el `localStorage` de las NUI). El origen es `https://cfx-nui-<recurso>`, así que cada recurso tiene su propio almacenamiento. |
| Contexto seguro (HTTPS) | ✅ Para archivos del recurso usa `https://cfx-nui-<recurso>/...`. `nui://` ya **no** es contexto seguro. |
| Micrófono y cámara (`getUserMedia`) | ✅ **Con permiso del jugador**: aparece un aviso y la decisión se guarda **por servidor y recurso**. Si el jugador no está conectado a un servidor, se permite sin preguntar. |
| Captura de escritorio / pantalla (`getDisplayMedia`) | ❌ **Siempre bloqueada** ("se ha demostrado que se abusa de ella"). |
| `ui_page` externa | ✅ Se permite una URL `https://...` como `ui_page` (documentación oficial). |
| CORS | No se aplica actualmente: FiveM arranca CEF con `disable-web-security`. El propio código lo marca como **pendiente de quitar** (*"TODO: remove this flag in the future"*), así que **no dependas de ello**: haz que tus APIs externas envíen cabeceras CORS correctas. |

### Funciones desactivadas a propósito (no las uses)

Según los *flags* que FiveM pasa a Chromium:

- **APIs de hardware**: WebUSB, WebBluetooth, WebHID y Web Serial.
- **Presentation API / Media Router** (enviar a TV), *Document Picture-in-Picture*.
- **Impresión** (*PrintCompositor*), **autocompletado** y monedero, **corrector ortográfico** (API, servicio y sugerencias), autocorrector, **Live Caption**.
- **Compute Pressure** (`PressureObserver`).
- **Teclas multimedia del teclado** (para que la NUI no se las robe a otros programas).
- **Zoom con gesto de pellizco** en el *trackpad*.
- **Extensiones**, sincronización, inicio de sesión de Google.
- **Decodificación y codificación de vídeo por hardware**: el vídeo se decodifica por **software**, así que un vídeo 4K a pantalla completa consume CPU.
- En Chromium 144, FiveM desactiva además dos funciones experimentales de Blink que estaban rotas: tamaños `width`/`height` como atributos en SVG anidados y una que podía colgar la interfaz.

### Formatos de audio y vídeo

- El staff de Cfx.re ha indicado en el foro que los **códecs propietarios (H.264 / MP4, AAC)** no están soportados en la NUI.
- **Usa formatos libres**: vídeo **WebM** (VP8/VP9/AV1) y audio **Ogg** (Opus/Vorbis) o WebM/Opus.
- Si un vídeo o audio no se reproduce, conviértelo, por ejemplo con `ffmpeg -i in.mp4 -c:v libvpx-vp9 -b:v 2M -c:a libopus out.webm`.

### Globales que FiveM inyecta en tus páginas NUI

| Global | Qué es |
|---|---|
| `GetParentResourceName()` | Nombre de tu recurso (para `fetch('https://' + GetParentResourceName() + '/callback')`). |
| `window.nuiTargetGame` | `'gta5'` en FiveM (`'rdr3'` en RedM). Útil para recursos compartidos. |
| `window.nuiSystemLanguages` | Array con los idiomas del sistema Windows del jugador (p. ej. `['es-ES', 'en-US']`). Útil para elegir idioma por defecto. |
| `window.nuiHandoverData` | **Solo en la pantalla de carga**: datos de `deferrals.handover` más `serverAddress`. |
| `window.invokeNative('openUrl', url)` | Abre una URL `http(s)` en el navegador del jugador. Si el dominio no es de confianza para FiveM, **el jugador ve una confirmación** antes. |
| `CfxGameViewRenderer` | Clase para dibujar **la imagen del juego** dentro de un `<canvas>` con WebGL2 (cámaras de móvil, monitores de seguridad…). |
| `<object type="application/x-cfx-game-view">` | Forma antigua de lo mismo: FiveM la sustituye automáticamente por un `<canvas>` con la vista del juego. |

Ejemplo de vista del juego en la NUI:

```html
<canvas id="vista" style="width: 480px; height: 270px"></canvas>
<script>
  const canvas = document.getElementById('vista');
  const renderer = new CfxGameViewRenderer(canvas);   // inyectado por FiveM
  new ResizeObserver(() => renderer.resize(canvas.clientWidth, canvas.clientHeight)).observe(canvas);
  // renderer.destroy() al cerrar
</script>
```

### Depuración

- DevTools remotas: **http://localhost:13172/** mientras el juego está abierto.
- Comando F8 `nui_devTools`: requiere el modo desarrollador.

### Buenas prácticas derivadas de lo anterior

- Fondo `transparent` en `html, body`; si no, taparás el juego.
- Pausa animaciones y vídeos ocultos (autoplay está siempre permitido y la decodificación es por CPU).
- Guarda preferencias de UI en `localStorage` o en KVP del cliente (desde Lua).
- Si necesitas micrófono (radio por NUI, notas de voz), explica al jugador por qué aparece el permiso.


## Ver también (documentación offline)

- [Oficial: scripting-manual/nui-development](../docs-oficiales/scripting-manual/nui-development/README.md)
- [Oficial: scripting-manual/nui-development/full-screen-nui](../docs-oficiales/scripting-manual/nui-development/full-screen-nui.md)
- [Oficial: scripting-manual/nui-development/nui-callbacks](../docs-oficiales/scripting-manual/nui-development/nui-callbacks.md)
- [Oficial: scripting-manual/nui-development/dui](../docs-oficiales/scripting-manual/nui-development/dui.md)
- [Oficial: scripting-manual/nui-development/loading-screens](../docs-oficiales/scripting-manual/nui-development/loading-screens/README.md)

---

[← 13-red-onesync-statebags-buckets](13-red-onesync-statebags-buckets.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [15-streaming-assets →](15-streaming-assets.md)
