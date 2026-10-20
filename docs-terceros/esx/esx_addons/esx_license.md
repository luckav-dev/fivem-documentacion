> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_addons/esx_license.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

# esx_license

[Github Link](https://github.com/esx-framework/ESX-Legacy-Addons/tree/main/%5Besx_addons%5D/esx_license)

ESX License is a license system for FiveM. It provides an easy way to manage licenses for your resources - for example, driving license.

## Usage

### AddLicense

- Event: `esx_license:addLicense`
- Usage: `TriggerEvent('esx_license:addLicense', target, licenseType, cb)`
- Example: `TriggerEvent('esx_license:addLicense', source, 'drive_bike', function() end)`

### RemoveLicense

- Event: `esx_license:removeLicense`
- Usage: `TriggerEvent('esx_license:removeLicense', target, licenseType, cb)`
- Example: `TriggerEvent('esx_license:removeLicense', source, 'drive_bike', function() end)`

### GetLicense (Callback)

- Event: `esx_license:getLicense`
- Usage: `TriggerEvent('esx_license:getLicense', licenseType, cb)`
- Example: `TriggerEvent('esx_license:getLicense', 'drive_bike', function(hasLicense) end)`

### GetLicenses (Callback)

- Event: `esx_license:getLicenses`
- Usage: `TriggerEvent('esx_license:getLicenses', target, cb)`
- Example: `TriggerEvent('esx_license:getLicenses', source, function(licenses) end)`

### CheckLicense (Callback)

- Event: `esx_license:checkLicense`
- Usage: `TriggerEvent('esx_license:checkLicense', target, licenseType, cb)`
- Example: `TriggerEvent('esx_license:checkLicense', source, 'drive_bike', function(hasLicense) end)`

### getLicensesList (Callback)

- Event: `esx_license:getLicensesList`
- Usage: `TriggerEvent('esx_license:getLicensesList', cb)`
- Example: `TriggerEvent('esx_license:getLicensesList', function(licenses) end)`
