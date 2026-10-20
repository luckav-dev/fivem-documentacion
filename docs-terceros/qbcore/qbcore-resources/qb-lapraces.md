> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qbcore-resources/qb-lapraces.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# 🏁 qb-lapraces

*Please! No more left turns!*

## Introduction

* Authorized players can create races that show up on the race app of [qb-phone.md](qb-phone.md)

## Preview

## Configuration

### General

```lua
Config = {}
Config.RaceSetupAllowed = true -- changes dynamically, don't edit this
Config.WhitelistedCreators = {
    "CITIZENID", -- List the player citizenid's allowed to create races
}
```

## Commands

* /cancelrace - Cancel the currently active race
* /togglesetup - Toggle the race creator
