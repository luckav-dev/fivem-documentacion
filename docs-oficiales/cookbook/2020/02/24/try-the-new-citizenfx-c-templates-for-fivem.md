# Try the new CitizenFX C# templates for FiveM

> Fuente original: https://docs.fivem.net/docs/cookbook/2020/02/24/try-the-new-citizenfx-c-templates-for-fivem/ · repositorio `citizenfx/fivem-docs` @ `6ec9770` · copiado el 2026-10-20 · [índice de la documentación oficial](../../../../README.md)

> **⚠️ Advertencia — Cookbook Archive**
>
> **Note:** This Cookbook article was originally published on **February 24, 2020**. Newer information may exist.


We've recently published the [CitizenFX.Templates package](https://www.nuget.org/packages/CitizenFX.Templates/) on NuGet, which includes a nice template for making a fully C#-based resource using the latest recommendations. The docs will be updated whenever more people confirm this works and report some feedback as to this, but for now here's the steps to set it up:

```
dotnet new -i CitizenFX.Templates
mkdir MyResource
cd MyResource
dotnet new cfx-resource
```

You'll find helpful instructions afterwards in the generated `README.md`.
