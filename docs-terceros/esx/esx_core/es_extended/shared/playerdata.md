> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/shared/playerdata.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# Player Data

Information about the player

The playerdata of a player contains a lot of values for further explanations please go to their respecting tab.

## How to get playerdata

### Server
You can get the playerdata by indexing the xPlayer object as it also contains everything(excluding client only data).

### Client
If you want to use PlayerData in your script you should use the import method to get the ESX object. 
It automatically gets the ESX object for you and refreshes your locally saved PlayerData object.

And can then accessed via ESX.PlayerData

**Visualized example what is contained, not actual data**
```lua
    PlayerData = {
        coords = vector3(0, 0, 0),
        ped = PlayerPedId(),
        group = "user",
        identifier = "char1:1ee4f3096a4051f782385478ddd133f883114876",
        ssn = "123-45-6789"
        inventory = {},
        job = {},
        loadout = {},
        name = "Knoblauchbrot",
        playerId = 1,
        source = 1,
        variables = {},
        weight = 12,
        maxWeight = 24,
        metadata = {},
        admin = false,
        license = "license:1ee4f3096a4051f782385478ddd133f883114876",
        dateofbirth = "01/01/2000",
        height = 181,
        dead = false,
        firstName = "John",
        lastName = "Doe",
        sex = 0,
        money = 187,
        accounts = {}
    }
```
