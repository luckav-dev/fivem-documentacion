> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qbcore-resources/qb-pawnshop.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# 🤑 qb-pawnshop

*Need some quick cash?*

## Introduction

* Players can go to the pawn shop and sell items or melt them down to earn other reward items.

> **Consejo:** The pawnshop can be open all the time or only between configured times!

> **Nota:** Players can obtain items for the pawnshop through [qb-houserobbery.md](qb-houserobbery.md) and [qb-jewelry.md](qb-jewelry.md)

## Configuration

### General

```lua
Config = {}
Config.PawnLocation = vector3(412.34, 314.81, 103.13) -- interaction point
Config.BankMoney = false -- pay player in bank or set to false for cash
Config.UseTimes = false -- Set to false if you want the pawnshop open 24/7
Config.TimeOpen = 7 -- Opening Time
Config.TimeClosed = 17 -- Closing Time
Config.SendMeltingEmail = true -- enable/disable email when melting finished
```

### Pawnshop items

```lua
Config.PawnItems = { -- items that can be sold to the pawnshop
    [1] = {
        item = "goldchain", -- item name
        price = math.random(50,100) -- item sale price
    },
    [2] = {
        item = "diamond_ring",
        price = math.random(50,100)
    },
    [3] = {
        item = "rolex",
        price = math.random(50,100)
    },
    [4] = {
        item = "10kgoldchain",
        price = math.random(50,100)
    },
    [5] = {
        item = "tablet",
        price = math.random(50,100)
    },
    [6] = {
        item = "iphone",
        price = math.random(50,100)
    },
    [7] = {
        item = "samsungphone",
        price = math.random(50,100)
    },
    [8] = {
        item = "laptop",
        price = math.random(50,100)
    }
}
```

### Melting items

```lua
Config.MeltingItems = { -- items able to be melted
    [1] = {
        item = "goldchain", -- item name to melt
        rewards = {
            [1] = {
                item = "goldbar", -- reward item name
                amount = 2 -- reward item amount
            }
        },
        meltTime = 0.15 -- time in minutes for melting to complete
    },
}
```
