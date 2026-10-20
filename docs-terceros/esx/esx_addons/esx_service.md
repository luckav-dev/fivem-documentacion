> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_addons/esx_service.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_service

[Github Link](https://github.com/esx-framework/ESX-Legacy-Addons/tree/main/%5Besx_addons%5D/esx_service)

ESX Service is a basic script, that allows for on/off duty switching for players. It is a simple script that can be used for any type of service, such as police, ambulance, taxi, etc.

## Usage

### Enable Service

```lua
ESX.TriggerServerCallback('esx_service:enableService', function(canTakeService, maxInService, inServiceCount)

  if canTakeService then
    ESX.ShowNotification('You enabled service')
  else
    ESX.ShowNotification('Service is full: ' .. inServiceCount .. '/' .. maxInService)
  end

end, 'taxi')
```

### Disable Service

```lua
TriggerServerEvent('esx_service:disableService', 'taxi')
```
