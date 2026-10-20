[← 09-lua](09-lua.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [11-csharp →](11-csharp.md)

# 10. JavaScript y TypeScript

## 10.1 Entornos

| Lado | Motor | Qué tienes |
|---|---|---|
| Cliente | **V8** (sin Node) | ES moderno, `setTick`, natives globales, `fetch` **no** (usa eventos/NUI). Sin `require` de npm (empaqueta con un *bundler*). |
| Servidor | **Node.js** (16 por defecto, 22 con `node_version '22'`) | `require`/`import` de npm, `fs`, `path`, `http`, `crypto`, `fetch` (Node 18+ → con Node 22), `async/await`. |

## 10.2 Manifest

```lua
fx_version 'cerulean'
game 'gta5'
node_version '22'

client_script 'dist/client.js'
server_script 'dist/server.js'
```

## 10.3 API básica

```js
// ===== client.js =====
setTick(() => {
  // cada frame (equivale a Wait(0)); evita trabajo pesado aquí
});

// Bucle con espera
const delay = (ms) => new Promise((r) => setTimeout(r, ms));
(async () => {
  while (true) {
    const ped = PlayerPedId();
    const [x, y, z] = GetEntityCoords(ped, true);
    await delay(1000);
  }
})();

on('miRecurso:local', (dato) => console.log(dato));   // AddEventHandler
onNet('miRecurso:red', (dato) => console.log(dato));  // RegisterNetEvent + handler
emit('miRecurso:local', 123);                         // TriggerEvent
emitNet('miRecurso:alServidor', { a: 1 });            // TriggerServerEvent

RegisterCommand('hola', (source, args, raw) => {
  emit('chat:addMessage', { args: ['Sistema', `Hola ${args.join(' ')}`] });
}, false);

exports('MiExport', (a, b) => a + b);
const resultado = exports.otro_recurso.OtraFuncion(1, 2);
```

```js
// ===== server.js =====
onNet('miRecurso:alServidor', (data) => {
  const src = global.source;        // ¡guárdalo!
  console.log(`Jugador ${GetPlayerName(src)} envió`, data);
  emitNet('miRecurso:red', src, 'respuesta'); // TriggerClientEvent(src)
  emitNet('miRecurso:red', -1, 'a todos');
});

on('playerConnecting', (name, setKickReason, deferrals) => {
  const src = global.source;
  deferrals.defer();
  setTimeout(() => {
    deferrals.update(`Comprobando a ${name}...`);
    deferrals.done();
  }, 0);
});

on('playerDropped', (reason) => {
  console.log(`${GetPlayerName(global.source)} salió: ${reason}`);
});
```

## 10.4 Diferencias importantes respecto a Lua

- Los natives que en Lua devuelven varios valores en JS devuelven **arrays**: `const [x, y, z] = GetEntityCoords(ped)`.
- Los vectores son arrays `[x, y, z]`, no objetos `vector3`.
- Hashes: `GetHashKey('adder')` (no existe la sintaxis de backticks de CfxLua).
- `source` está en `global.source` (o simplemente `source` en el ámbito global del servidor).
- Los timers (`setTimeout`, `setInterval`) existen en ambos lados y se integran en el *scheduler* de FiveM.
- Usa `Wait` solo en Lua; en JS usa `await new Promise(r => setTimeout(r, ms))`.
- `setTick` devuelve un id: `clearTick(id)` para pararlo.

## 10.5 TypeScript con tipos oficiales

```bash
npm init -y
npm i -D typescript esbuild @citizenfx/client @citizenfx/server @types/node
```

`tsconfig.json` (cliente):

```json
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "strict": true,
    "types": ["@citizenfx/client"],
    "outDir": "dist"
  },
  "include": ["src/client/**/*"]
}
```

Build con esbuild (`build.js`):

```js
const esbuild = require('esbuild');

const comunes = { bundle: true, minify: true, sourcemap: false, logLevel: 'info' };

Promise.all([
  esbuild.build({ ...comunes, entryPoints: ['src/client/main.ts'], outfile: 'dist/client.js', platform: 'browser', target: 'es2020' }),
  esbuild.build({ ...comunes, entryPoints: ['src/server/main.ts'], outfile: 'dist/server.js', platform: 'node', target: 'node22' }),
]).catch(() => process.exit(1));
```

```ts
// src/client/main.ts
RegisterCommand('pos', () => {
  const [x, y, z] = GetEntityCoords(PlayerPedId(), true);
  console.log(`vec3(${x.toFixed(2)}, ${y.toFixed(2)}, ${z.toFixed(2)})`);
}, false);
```

> Empaqueta siempre las dependencias npm en el **cliente** (V8 no tiene `require`). En el **servidor** puedes empaquetar o dejar `node_modules` dentro del recurso.

## 10.6 Servidor: async, base de datos y npm

```js
// server.js con oxmysql (export)
const oxmysql = exports.oxmysql;

onNet('banco:saldo', async () => {
  const src = global.source;
  const license = GetPlayerIdentifierByType(src, 'license');
  const row = await oxmysql.single_async('SELECT saldo FROM cuentas WHERE license = ?', [license]);
  emitNet('banco:saldo:respuesta', src, row?.saldo ?? 0);
});
```

> Las funciones *async* de exports de oxmysql en JS siguen el patrón `query_async`, `single_async`, `scalar_async`, `insert_async`, `update_async`, `prepare_async`.


## Ver también (documentación offline)

- [Oficial: scripting-manual/runtimes/javascript](../docs-oficiales/scripting-manual/runtimes/javascript.md)
- [Oficial: scripting-reference/runtimes/javascript](../docs-oficiales/scripting-reference/runtimes/javascript/README.md)

---

[← 09-lua](09-lua.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [11-csharp →](11-csharp.md)
