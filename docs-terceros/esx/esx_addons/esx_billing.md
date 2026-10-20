> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_addons/esx_billing.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_billing

[Github Link](https://github.com/esx-framework/ESX-Legacy-Addons/tree/main/%5Besx_addons%5D/esx_billing)

This resource for ESX adds possibility for different jobs to send bills to players, for example making police units able to give people fines. It comes with a menu for paying bills, to open the menu the default keybind is F7.

There is a server event available in order to register bills in the database/

### Usage

- Show the bill menu: `F7`
- Using the bill event:

```lua
local amount                         = 100
local closestPlayer, closestDistance = ESX.Game.GetClosestPlayer()

if closestPlayer == -1 or closestDistance > 3.0 then
	ESX.ShowNotification('There\'s no players nearby!')
else
	TriggerServerEvent('esx_billing:sendBill', GetPlayerServerId(closestPlayer), 'society_taxi', 'Taxi', amount)
end
```
