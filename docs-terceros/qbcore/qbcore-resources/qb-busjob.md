> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qbcore-resources/qb-busjob.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# 🚌 qb-busjob

*NPC's have places to be!*

> **Peligro:** THIS RESOURCE IS A WORK IN PROGRESS

## Introduction

* Allows your players to go to the bus depot and start driving around Los Santos collecting passengers from bus stops and dropping them off at others

## Configuration

```lua
Config = {}
Config.AllowedVehicles = {} -- Define the bus model to use
Config.Location = vector4() -- Set the blip and vehicle withdraw location
Config.NPCLocations = {} -- The bus stop locations
Config.NpcSkins = {} -- List of ped models randomly chosen to spawn
```
