> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qbcore-resources/qb-interior.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# 🏠 qb-interior

*Which shell will it be?*

## Introduction

* Handles all the logic for spawning shell models by exporting functions that can be called in other client-side files

## Configuration

> **Consejo:** This resource requires no configuration unless you want to add more exports

## What's included?

> **Nota:** The below pdf file shows which shell models come by default

> **Archivo:** [k4mb1shellstarter.pdf](../imagenes/k4mb1shellstarter.pdf)

> **Consejo:** Optionally, this resource comes pre-configured for all of [K4MB1](https://www.k4mb1maps.com/) shells!

## Usage example

```lua
RegisterCommand('spawnshell', function()
    local ped = PlayerPedId()
    local coords = GetEntityCoords(ped)
    local shell = exports['qb-interior']:CreateApartmentShell(coords)
end)
```
