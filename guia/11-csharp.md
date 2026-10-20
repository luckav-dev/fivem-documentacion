[← 10-javascript-typescript](10-javascript-typescript.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [12-natives-guia-practica →](12-natives-guia-practica.md)

# 11. C# (.NET / Mono)

## 11.1 Proyecto

FiveM ejecuta C# con **Mono** (compatible con .NET Standard 2.0 / .NET Framework 4.x). Se compila a **DLL** y se carga desde el manifest.

`MiRecurso.Client.csproj`:

```xml
<Project Sdk="Microsoft.NET.Sdk">
  <PropertyGroup>
    <TargetFramework>net452</TargetFramework>
    <DebugType>portable</DebugType>
    <AssemblyName>MiRecurso.Client.net</AssemblyName>
  </PropertyGroup>
  <ItemGroup>
    <PackageReference Include="CitizenFX.Core.Client" Version="1.0.*" ExcludeAssets="runtime" />
  </ItemGroup>
</Project>
```

`MiRecurso.Server.csproj`: igual pero `TargetFramework` `netstandard2.0` y `CitizenFX.Core.Server`.

> El nombre del DLL **debe terminar en `.net.dll`** para que FiveM lo reconozca como ensamblado de script.

Manifest:

```lua
fx_version 'cerulean'
game 'gta5'

client_script 'Client/bin/Release/net452/MiRecurso.Client.net.dll'
server_script 'Server/bin/Release/netstandard2.0/MiRecurso.Server.net.dll'
```

## 11.2 Script básico

```csharp
using System;
using System.Threading.Tasks;
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

namespace MiRecurso.Client
{
    public class Main : BaseScript
    {
        public Main()
        {
            EventHandlers["onClientResourceStart"] += new Action<string>(OnStart);
            EventHandlers["miRecurso:red"] += new Action<string>(msg => Debug.WriteLine(msg));

            RegisterCommand("pos", new Action<int, System.Collections.Generic.List<object>, string>((src, args, raw) =>
            {
                var p = Game.PlayerPed.Position;
                Debug.WriteLine($"vec3({p.X:F2}, {p.Y:F2}, {p.Z:F2})");
            }), false);

            Exports.Add("Sumar", new Func<int, int, int>((a, b) => a + b));
        }

        private void OnStart(string res)
        {
            if (res != GetCurrentResourceName()) return;
            TriggerServerEvent("miRecurso:alServidor", "hola");
        }

        [Tick]
        private async Task OnTick()
        {
            // cada frame
            await Delay(1000); // espera 1s antes del siguiente tick de este método
        }
    }
}
```

Servidor:

```csharp
using System;
using CitizenFX.Core;
using static CitizenFX.Core.Native.API;

namespace MiRecurso.Server
{
    public class Main : BaseScript
    {
        public Main()
        {
            EventHandlers["miRecurso:alServidor"] += new Action<Player, string>(OnMensaje);
            EventHandlers["playerConnecting"] += new Action<Player, string, dynamic, dynamic>(OnConnecting);
        }

        private void OnMensaje([FromSource] Player jugador, string msg)
        {
            Debug.WriteLine($"{jugador.Name}: {msg}");
            jugador.TriggerEvent("miRecurso:red", "respuesta");
            TriggerClientEvent("miRecurso:red", "a todos");
        }

        private async void OnConnecting([FromSource] Player p, string name, dynamic setKickReason, dynamic deferrals)
        {
            deferrals.defer();
            await Delay(0);
            deferrals.update("Comprobando...");
            deferrals.done();
        }
    }
}
```

## 11.3 Conceptos

| Concepto | Equivalente Lua |
|---|---|
| `BaseScript` | Cada clase que hereda es un "script" que FiveM instancia. |
| `[Tick]` / `Tick += OnTick` | `CreateThread` con bucle. |
| `await Delay(ms)` | `Wait(ms)`. |
| `EventHandlers["x"] += ...` | `AddEventHandler` / `RegisterNetEvent`. |
| `[FromSource] Player` | `source`. |
| `TriggerServerEvent` / `TriggerClientEvent` / `player.TriggerEvent` | Igual. |
| `Exports["recurso"].Funcion(...)` | `exports.recurso:Funcion(...)`. |
| `Players` (servidor) | `GetPlayers()`. |
| `Function.Call(Hash.X, ...)` | `Citizen.InvokeNative`. |
| `API.*` (static import) | Natives directamente. |

Wrappers útiles en cliente: `Game.PlayerPed`, `World.CreateVehicle(model, pos, heading)`, `Vehicle`, `Ped`, `Entity`, `Model`, `Screen.ShowNotification`.

> **Mono v2 (`mono_rt2`)**: era un runtime C# experimental que se activaba con una cadena de "prerelease" con fecha de caducidad. La última fecha aceptada fue el **30 de junio de 2026**; en los artefactos actuales los recursos con `mono_rt2` muestran *"mono_rt2 is no longer supported"* y **no se cargan**. En FiveM Legacy usa el runtime clásico (Mono v1) con `CitizenFX.Core.Client` / `CitizenFX.Core.Server`.

## 11.4 Plantillas oficiales

```bash
dotnet new -i CitizenFX.Templates
dotnet new cfx-resource -n MiRecurso
```

Genera la estructura con proyectos de cliente, servidor y `fxmanifest.lua`.


## Ver también (documentación offline)

- [Oficial: scripting-manual/runtimes/csharp](../docs-oficiales/scripting-manual/runtimes/csharp.md)
- [Oficial: scripting-reference/runtimes/csharp](../docs-oficiales/scripting-reference/runtimes/csharp/README.md)
- [Oficial: cookbook/2020/02/24/try-the-new-citizenfx-c-templates-for-fivem](../docs-oficiales/cookbook/2020/02/24/try-the-new-citizenfx-c-templates-for-fivem.md)

---

[← 10-javascript-typescript](10-javascript-typescript.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [12-natives-guia-practica →](12-natives-guia-practica.md)
