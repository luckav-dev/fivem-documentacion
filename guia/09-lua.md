[← 08-scripting-fundamentos](08-scripting-fundamentos.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [10-javascript-typescript →](10-javascript-typescript.md)

# 9. Lua en FiveM (CfxLua 5.4)

## 9.1 Qué Lua usa FiveM

- **CfxLua**: una versión modificada de **Lua 5.4.8** basada en *LuaGLM*.
- **Lua 5.3 se eliminó**: anunciado el 24 de junio de 2025 y retirado de producción a finales de julio de 2025. **Todos** los scripts Lua se ejecutan ahora en 5.4, con o sin `lua54 'yes'`.
- Incluye tipos de vector nativos (GLM), extensiones de sintaxis y librerías integradas (`json`, `msgpack`, `promise`).

## 9.2 Cambios de 5.3 → 5.4 que pueden romper scripts antiguos

Si heredas recursos viejos, revisa estos puntos (los anunció Cfx.re al eliminar 5.3):

| Cambio | Qué pasa | Solución |
|---|---|---|
| Sin conversión automática string→número en aritmética y operaciones de bits | `"10" + 5` puede fallar | `tonumber("10") + 5` |
| Literales enteros decimales que desbordan pasan a ser *float* | Números gigantes cambian de tipo | Usa `math.tointeger` o strings |
| `__lt` ya no emula `__le` | Metatablas con solo `__lt` fallan en `<=` | Define `__le` |
| Bucles `for` numéricos | Cambia el comportamiento en casos límite (desbordamiento, paso 0) | Revisa bucles con pasos raros |
| Reglas nuevas de etiquetas `goto` | Errores de compilación en código antiguo con `goto` | Renombra/mueve etiquetas |
| `json.decode` más estricto | No acepta corchetes sueltos, valores sin clave ni claves numéricas en ciertos formatos | Valida el JSON |
| `print` no llama a `tostring` | Usa `__tostring` directamente | Normalmente no afecta |
| `math.random` sembrado aleatoriamente | Ya no hace falta `math.randomseed(os.time())` | Quítalo si quieres |
| `utf8` rechaza *surrogates* | Strings UTF-8 inválidas fallan | Limpia los datos |
| `collectgarbage("setpause"/"setstepmul")` obsoletos | | Usa `collectgarbage("incremental", ...)` |
| `io.lines` devuelve 4 valores | | Normalmente no afecta |

Además, 5.4 añade **variables `<const>` y `<close>`**:

```lua
local MAX_JUGADORES <const> = 64
```

## 9.3 Extensiones de sintaxis de CfxLua

| Extensión | Ejemplo | Equivale a |
|---|---|---|
| **Hash en compilación** (backticks) | `` local h = `adder` `` | `GetHashKey('adder')` (calculado al compilar, más rápido) |
| `joaat(str[, ignoreCase])` | `joaat('adder')` | Hash Joaat en tiempo de ejecución |
| **Operadores compuestos** | `x += 1`, `x -= 1`, `n *= 2`, `n /= 2`, `n <<= 1`, `n >>= 1`, `n &= 3`, `n \|= 4`, `n ^= 2` | `x = x + 1`, etc. |
| **Navegación segura** | `local z = jugador?.coords?.z` | `jugador and jugador.coords and jugador.coords.z` |
| Navegación segura en llamadas y asignaciones (2025) | `obj?.metodo()`, `obj?.valor = 1` | Solo si `obj` no es `nil` |
| **Desempaquetado `in`** | `local x, y, z in coords` | `local x, y, z = coords.x, coords.y, coords.z` |
| **Constructor de conjuntos** | `local s = { .a, .b }` | `{ a = true, b = true }` |
| **Comentarios estilo C** | `/* comentario */` | `--[[ comentario ]]` |
| `each(t)` | `for k, v in each(t) do end` | Iteración genérica (respeta `__iter`) |
| `defer(fn)` | `local _ <close> = defer(function() print('fin') end)` | Ejecuta `fn` al salir del ámbito. Es una **función** de la librería base (no la sentencia `defer ... end` de Ravi) |

> Operadores compuestos disponibles: `+=  -=  *=  /=  <<=  >>=  &=  |=  ^=`. **No** existen `++`, `--` (que en Lua es un comentario) ni `..=`.

Funciones extra en librerías estándar (estilo *WoW*): `table.create`, `table.wipe`, `table.clone`, `table.type`, `string.strjoin`, `string.strtrim`, `string.strsplit`, `string.strconcat`, `string.tostringall`, `scrub`.

## 9.4 Vectores y cuaterniones

```lua
local a = vector3(100.0, 200.0, 30.0)   -- alias corto: vec3(...)
local b = vec3(110.0, 205.0, 30.0)

local distancia = #(a - b)               -- # = magnitud → distancia
local suma = a + b
local escalado = a * 2.0
local xy = a.xy                          -- swizzling → vector2
local normalizado = a / #a               -- vector unitario

local glm = require 'glm'                -- librería GLM completa
local producto = glm.dot(a, b)
local perpendicular = glm.cross(a, b)

local v2 = vec2(1.0, 2.0)
local v4 = vec4(1.0, 2.0, 3.0, 4.0)      -- típico para coords + heading: vec4(x, y, z, h)
local q = quat(1.0, 0.0, 0.0, 0.0)

print(a)                                 -- vector3(100.0, 200.0, 30.0)
print(type(a))                           -- 'vector3'
```

- `GetEntityCoords` devuelve un `vector3`. Compara distancias con `#(a - b) < 5.0` en lugar de `GetDistanceBetweenCoords` (más lento).
- Para guardar un vector en JSON: `{ x = v.x, y = v.y, z = v.z }` (luego `vec3(t.x, t.y, t.z)`).
- `require 'glm'` da acceso a la librería GLM completa (matrices, funciones matemáticas avanzadas).

## 9.5 Librerías y globales integradas

| Global | Descripción |
|---|---|
| `json` | `json.encode(t, { indent = true })`, `json.decode(s)`. Implementación nativa (*rapidjson*). |
| `msgpack` | `msgpack.pack(...)`, `msgpack.unpack(s)` (*cmsgpack* nativo). |
| `promise` | `promise.new()`, `p:resolve(v)`, `p:reject(e)`, `promise.all`, `promise.first`, `promise.map`. |
| `Citizen.Await(p)` | Espera una promesa (dentro de thread/handler). Lanza error si se rechaza. |
| `CreateThread`, `Wait`, `SetTimeout`, `ClearTimeout` | Planificador. |
| `exports` | Exports. |
| `GlobalState`, `Entity`, `Player`, `LocalPlayer` | State bags. |
| `vector2/3/4`, `vec2/3/4`, `quat` | Vectores. |
| `require` | Solo módulos integrados (`'glm'`, `'lmprof'`). Para módulos propios usa `shared_scripts` o `require` de **ox_lib**. |
| `IsDuplicityVersion()` | `true` en servidor. |

### Promesas y await

```lua
local function esperarRespuesta()
    local p = promise.new()
    SetTimeout(1000, function() p:resolve('hecho') end)
    return Citizen.Await(p)
end

CreateThread(function()
    print(esperarRespuesta())   -- 'hecho' (tras 1s)
end)
```

## 9.6 Estilo y buenas prácticas en Lua

- Usa **`local`** siempre. Las globales son más lentas y chocan entre archivos del mismo recurso (todos los scripts de un mismo lado de un recurso comparten el entorno global).
- Cachea natives que llamas mucho en bucles calientes: `local GetEntityCoords = GetEntityCoords`.
- No llames a `PlayerPedId()` miles de veces por frame; guárdalo en una variable o usa `cache.ped` (ox_lib).
- Prefiere **tablas indexadas por clave** (`tabla[id]`) a recorrer arrays para buscar.
- `table.concat` en lugar de concatenar strings en bucles.
- `('%s tiene %d$'):format(nombre, dinero)` para formatear.
- Maneja errores con `pcall`/`xpcall` en código que llama a otros recursos:

```lua
local ok, res = pcall(function()
    return exports.otro_recurso:Algo()
end)
if not ok then print('^1Error: ' .. tostring(res) .. '^0') end
```

## 9.7 Módulos y organización

Dentro de un recurso, los archivos del mismo lado comparten el **entorno global**, así que puedes declarar una tabla y usarla en otros archivos:

```lua
-- shared/config.lua
Config = {}
Config.Debug = false
Config.Tiendas = {
    { nombre = '24/7 Grove', coords = vec3(-47.5, -1757.5, 29.4) },
}
```

```lua
-- client/main.lua
for _, t in ipairs(Config.Tiendas) do
    -- crear blips...
end
```

Con **ox_lib** puedes usar `require` para módulos con ámbito propio (los archivos deben estar en `files` si son de cliente):

```lua
-- modules/utils.lua
local M = {}
function M.redondear(n, d) local m = 10 ^ (d or 0); return math.floor(n * m + 0.5) / m end
return M

-- client/main.lua
local utils = require 'modules.utils'
print(utils.redondear(3.14159, 2))
```

## 9.8 Autocompletado en el editor (VS Code)

- La extensión **"CfxLua IntelliSense"** (`overextended/cfxlua-vscode`) está **descontinuada**, y su *fork* de CommunityOx pertenece a una organización archivada.
- Recomendación actual: **`overextended/fivem-lls-addon`** (natives regenerados semanalmente) con la extensión **Lua** de *sumneko/LuaLS*.

Pasos:

1. Clona el addon: `git clone https://github.com/overextended/fivem-lls-addon`.
2. Crea la variable de entorno `CFX_LUALS_ADDON` apuntando a esa carpeta.
3. Crea `.luarc.json` en tu proyecto:

```json
{
  "runtime": {
    "version": "Lua 5.4",
    "nonstandardSymbol": ["/**/", "`", "+=", "-=", "*=", "/=", "<<=", ">>=", "&=", "|=", "^="],
    "plugin": "${env:CFX_LUALS_ADDON}/plugin.lua"
  },
  "workspace": {
    "library": ["${env:CFX_LUALS_ADDON}/library"]
  }
}
```

4. Añade a `workspace.library` las rutas de las librerías que uses (por ejemplo, tu copia de `ox_lib`) para tener autocompletado de sus funciones.


## 9.9 Referencia completa del runtime Lua (verificada en el código fuente)

Esta sección está sacada **directamente del código fuente de FiveM** (`citizenfx/fivem`: `LuaScriptRuntime.cpp`, `scheduler.lua`, `natives_loader.lua` y el generador de natives `codegen_out_lua.lua`), tal y como está en la build *latest* 37579 (octubre de 2026). Si algo no aparece aquí, **no existe** en el Lua de FiveM.

### 9.9.1 Librerías disponibles en cliente y servidor

| Librería | Cliente | Servidor | Notas |
|---|---|---|---|
| Base (`_G`) | ✅ | ✅ | `dofile` y `loadfile` **no existen** (FiveM los pone a `nil`). `print` y `require` están reemplazados por versiones propias. `load` sí está disponible. |
| `table`, `string`, `math`, `coroutine`, `utf8` | ✅ | ✅ | Con las extensiones de CfxLua (9.3). |
| `debug` | ✅ | ✅ | |
| `json` | ✅ | ✅ | Nativa (*rapidjson*). |
| `msgpack` | ✅ | ✅ | Nativa (*cmsgpack*). |
| **`io`** | ❌ **No existe** | ✅ | Con *sandbox* (ver 9.9.2). |
| **`os`** | ❌ **No existe** | ✅ | Con *sandbox* (ver 9.9.2). |
| `package` | ❌ | ❌ | No se carga: no hay `package.path` ni carga de `.lua` con `require`. |
| `glm`, `lmprof` | Con `require 'glm'` / `require 'lmprof'` | Igual | Son los **únicos** módulos que acepta el `require` nativo. |

> **Error típico:** usar `os.time()`, `os.date()` u `os.clock()` en un `client_script` → `attempt to index a nil value (global 'os')`. En el cliente usa `GetGameTimer()`, `GetCloudTimeAsInt()` (tiempo Unix), `GetLocalTime()` o `GetUtcTime()` (devuelven año, mes, día, hora, minuto, segundo).
>
> El `require` que usan muchos recursos (`require 'modules.utils'`) es el de **ox_lib** (`@ox_lib/init.lua` lo sustituye), no el de FiveM.

### 9.9.2 `io` y `os` en el servidor: qué se permite

| Función | Comportamiento en FiveM |
|---|---|
| `io.open(ruta, modo)` | Lectura normal. **Escritura/creación/añadir** solo dentro de la carpeta del **propio recurso**, salvo permiso explícito (ver abajo). |
| Métodos del archivo abierto: `f:read`, `f:lines`, `f:write`, `f:seek`, `f:setvbuf`, `f:flush`, `f:close` | Funcionan con normalidad. **Para leer línea a línea usa `f:lines()`.** |
| `io.lines(ruta)` | ⚠️ Devuelve un iterador **vacío**: no lee el archivo. |
| `io.write(...)` | Equivale a `print` (sale por la consola, no a un archivo). |
| `io.flush()` | No hace nada. |
| `io.close`, `io.type`, `io.tmpfile` | Disponibles. |
| `io.readdir(ruta)` | **Extra de FiveM**: recorre un directorio. |
| `io.popen(cmd)` | Solo acepta comandos que empiezan por `dir` o `ls` (listar directorios); **cualquier otro comando falla**. |
| `io.input`, `io.output`, `io.read` | **No existen**. |
| `os.execute(cmd)` | **Siempre denegado** (devuelve error de permisos). |
| `os.getenv(nombre)` | Solo responde a `'os'` (`"Windows"` o `"Linux"`); cualquier otra variable devuelve `nil`. |
| `os.remove`, `os.rename`, `os.createdir` | Sujetos al mismo *sandbox* de rutas. `os.createdir` es un extra de FiveM. |
| `os.setlocale` | **No cambia** la configuración regional (solo devuelve el valor). |
| `os.exit` | **No existe**. |
| `os.time`, `os.date`, `os.clock`, `os.difftime`, `os.tmpname` | Normales. |
| `os.microtime()`, `os.nanotime()`, `os.deltatime(a, b)` | **Extras de FiveM**: tiempos de alta resolución. |

Permisos de sistema de archivos entre recursos (comandos de `server.cfg`; **solo funcionan antes de que el servidor termine de arrancar**):

```cfg
add_filesystem_permission mi_recurso write otro_recurso   # o 'read'
add_unsafe_worker_permission mi_recurso_js                 # JS: permitir worker threads
add_unsafe_child_process_permission mi_recurso_js          # JS: permitir procesos hijo
```

> Lo normal y recomendado para leer/escribir archivos del propio recurso es `LoadResourceFile` / `SaveResourceFile` (funcionan igual en Lua, JS y C#).

### 9.9.3 Funciones globales que define el runtime

| Función | Lado | Descripción (según `scheduler.lua`) |
|---|---|---|
| `CreateThread(fn)` / `Citizen.CreateThread` | Ambos | Crea una corrutina que se reanuda en cada tick. |
| `CreateThreadNow(fn)` / `Citizen.CreateThreadNow` | Ambos | Igual, pero empieza a ejecutarse **en el acto** hasta su primer `Wait`. |
| `Wait(ms)` / `Citizen.Wait` | Ambos | Pausa la corrutina actual. Solo dentro de un thread o de un handler de evento (los handlers se ejecutan como corrutinas). |
| `SetTimeout(ms, fn)` / `Citizen.SetTimeout` | Ambos | Ejecuta `fn` una vez tras `ms`. Devuelve un id. |
| `ClearTimeout(id)` / `Citizen.ClearTimeout` | Ambos | Cancela un `SetTimeout`. |
| `Citizen.Await(promesa)` | Ambos | Espera una `promise`; lanza error si se rechaza. |
| `promise.new()`, `promise.all`, `promise.first`, `promise.map` | Ambos | Promesas (*lua-promises*). |
| `AddEventHandler(nombre, fn)` | Ambos | Registra un handler local. **Devuelve** `{ key, name }`. |
| `RemoveEventHandler(handle)` | Ambos | Quita un handler usando lo que devolvió `AddEventHandler`. |
| `RegisterNetEvent(nombre[, fn])` | Ambos | Marca el evento como seguro para recibirlo por red y, si pasas `fn`, añade el handler. |
| `RegisterServerEvent` | Servidor | **Alias** de `RegisterNetEvent` (antiguo). |
| `TriggerEvent(nombre, ...)` | Ambos | Evento local. |
| `TriggerServerEvent(nombre, ...)` | Cliente | Al servidor. |
| `TriggerLatentServerEvent(nombre, bps, ...)` | Cliente | Al servidor, troceado a `bps` bytes/s. |
| `TriggerClientEvent(nombre, destino, ...)` | Servidor | A un jugador o `-1` (todos). |
| `TriggerLatentClientEvent(nombre, destino, bps, ...)` | Servidor | Versión latente. |
| `exports(nombre, fn)` / `exports.recurso:fn(...)` | Ambos | Exports. Si no existe: error `No such export X in resource Y`. No se puede asignar `exports.x = ...` (da error). |
| `GlobalState`, `Entity(e)`, `Player(id)` | Ambos | State bags. |
| `LocalPlayer` | Cliente | Equivale a `Player(-1)`: tu propio jugador. |
| `GetPlayers()` | Servidor | Lista de ids conectados (**strings**). |
| `GetPlayerIdentifiers(src)` / `GetPlayerTokens(src)` | Servidor | Tablas con todos los identificadores / tokens. |
| `PerformHttpRequest(url, cb, metodo, datos, cabeceras, opciones)` | Servidor | HTTP saliente. `opciones.followLocation` (por defecto `true`). Si falla al crearse: `cb(0, nil, {}, 'Failure handling HTTP request')`. |
| `PerformHttpRequestAwait(url, metodo, datos, cabeceras, opciones)` | Servidor | Versión síncrona: devuelve `status, body, headers, errorData`. |
| `RegisterNUICallback(nombre, fn)` / `RegisterNuiCallback` | Cliente | Callback de NUI. |
| `SendNUIMessage(tabla)` | Cliente | Codifica en JSON y llama a `SendNuiMessage`. |
| `GetPlayerEP` | Servidor | Alias de `GetPlayerEndpoint`. |
| `RconPrint(texto)` | Servidor | Alias de `Citizen.Trace` (imprime en consola). |
| `Citizen.Trace(texto)` | Ambos | Imprime sin formato adicional. |
| `Citizen.GetFunctionReference(fn)` | Ambos | Crea una referencia de función para pasarla a natives/otros recursos. |
| `Citizen.InvokeNative(hash, ...)` | Ambos | Llama a un native por su hash (9.9.5). |
| `source` | Ambos | Global con el origen del evento en curso. |

### 9.9.4 Cómo convierte FiveM los natives a funciones Lua

Reglas del generador oficial (`codegen_out_lua.lua`):

1. **Nombre**: se pasa a minúsculas, cada `_letra` se convierte en mayúscula y la primera letra también: `GET_ENTITY_COORDS` → `GetEntityCoords`. Los guiones bajos delante de un número se mantienen: `GET_GROUND_Z_FOR_3D_COORD` → `GetGroundZFor_3dCoord`. Los natives sin nombre se llaman `N_0x...`.
2. **Parámetros puntero** (`int*`, `float*`, `Vector3*`, `BOOL*`, `Entity*`…): **no se pasan**; sus valores se **devuelven** después del resultado normal:

   ```lua
   -- C: BOOL GET_GROUND_Z_FOR_3D_COORD(float x, float y, float z, float* groundZ, BOOL includeWater)
   local encontrado, z = GetGroundZFor_3dCoord(x, y, z, false)

   -- C: void GET_VEHICLE_COLOURS(Vehicle vehicle, int* colorPrimary, int* colorSecondary)
   local primario, secundario = GetVehicleColours(veh)

   -- C: void GET_LOCAL_TIME(int* year, int* month, int* day, int* hour, int* minute, int* second)
   local anio, mes, dia, hora, minuto, segundo = GetLocalTime()
   ```

   **Excepción**: si el native tiene **un único** puntero y es el **último** parámetro, ese argumento sí aparece en la firma, pero es opcional (puedes omitirlo) y el valor se devuelve igualmente:

   ```lua
   -- C: BOOL GET_PED_LAST_DAMAGE_BONE(Ped ped, int* outBone)
   local ok, hueso = GetPedLastDamageBone(ped)
   ```

3. **Parámetros `Hash`**: si pasas un **string**, se convierte automáticamente con `GetHashKey`. `RequestModel('adder')` funciona igual que ``RequestModel(`adder`)``. Aun así, el *backtick* es más rápido porque se calcula al compilar.
4. **Parámetros string**: pasar `nil` o `0` envía un puntero nulo.
5. **Parámetros `func`**: las funciones Lua se convierten solas en referencias de función.
6. **Parámetros `object`** (tablas): se serializan automáticamente con msgpack.
7. Los natives se cargan **bajo demanda** (la primera vez que los usas).

### 9.9.5 `Citizen.InvokeNative` (natives por hash)

Útil para natives que todavía no tienen nombre o que tu build no expone con nombre:

```lua
-- Devuelve un vector3: hay que indicar el tipo de resultado
local coords = Citizen.InvokeNative(0x3FEF770D40960D5A, PlayerPedId(), true, Citizen.ResultAsVector())

-- Otros indicadores de resultado: Citizen.ResultAsInteger(), Citizen.ResultAsFloat(),
-- Citizen.ResultAsString(), Citizen.ResultAsLong(), Citizen.ReturnResultAnyway()
-- Punteros de salida: Citizen.PointerValueInt(), Citizen.PointerValueFloat(), Citizen.PointerValueVector()
local encontrado, z = Citizen.InvokeNative(0xC906A7DAB05C8D2B, x, y, z, Citizen.PointerValueFloat(), false, Citizen.ReturnResultAnyway())
```

> Si existe la versión con nombre, úsala: es más legible y FiveM ya gestiona los tipos por ti.

### 9.9.6 Lo que **no** funciona en el Lua de FiveM

| Intento | Por qué falla | Alternativa |
|---|---|---|
| `os.*` / `io.*` en el cliente | No existen en el cliente | `GetGameTimer`, `GetLocalTime`, KVP, `LoadResourceFile` |
| `dofile`, `loadfile` | Eliminados | Añade el archivo a `shared/client/server_scripts`, o `load(LoadResourceFile(...))` |
| `require 'mi_modulo'` sin ox_lib | El `require` nativo solo carga `glm` y `lmprof` | `@ox_lib/init.lua` + `require`, o tablas globales compartidas |
| `os.execute`, `io.popen('cualquier cosa')` | Bloqueados | Ninguna desde Lua (por seguridad) |
| Escribir archivos de **otro** recurso | *Sandbox* | `add_filesystem_permission` en `server.cfg` |
| `Wait()` fuera de un thread o handler | No hay corrutina que pausar | Envuelve el código en `CreateThread` |
| Enviar funciones por `TriggerServerEvent`/`TriggerClientEvent` | Los datos se serializan con msgpack | Envía datos; para lógica usa callbacks (8.3) |
| Enviar *handles* de entidad entre cliente y servidor | Son locales a cada máquina | Envía el **netId** (`NetworkGetNetworkIdFromEntity`) |
| Aritmética con strings (`"5" + 1`) | Lua 5.4 no convierte | `tonumber("5") + 1` |

> **Funciones de ejemplo**: en esta guía, las funciones con nombre en español como `AbrirTienda`, `DarItem`, `QuitarDinero`, `LogSospechoso` o `GuardarTodosLosJugadores` son **tuyas**: representan tu propia lógica y debes implementarlas. Todo lo demás (natives, funciones del runtime y APIs de librerías) está comprobado contra las fuentes oficiales.

## Ver también (documentación offline)

- [Oficial: scripting-manual/runtimes/lua](../docs-oficiales/scripting-manual/runtimes/lua.md)
- [Oficial: scripting-reference/runtimes/lua](../docs-oficiales/scripting-reference/runtimes/lua/README.md)
- [Oficial: cookbook/2019/06/23/lua-support-for-compile-time-jenkins-hashes](../docs-oficiales/cookbook/2019/06/23/lua-support-for-compile-time-jenkins-hashes.md)

---

[← 08-scripting-fundamentos](08-scripting-fundamentos.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [10-javascript-typescript →](10-javascript-typescript.md)
