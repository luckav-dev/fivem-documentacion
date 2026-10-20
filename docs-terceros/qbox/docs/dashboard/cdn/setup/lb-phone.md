> Fuente original: https://github.com/Qbox-project/qbox-docs/blob/260c0ecedce58bece2cf94ebef73be42d08258ac/docs/dashboard/cdn/setup/lb-phone.mdx · repositorio Qbox-project/qbox-docs @ 260c0ec · copiado el 2026-10-20

# LB Phone

This guide will go over how to set up the Qbox CDN with [LB Phone](https://store.lbscripts.com/package/5356987)

## Changing upload method

Navigate to `lb-phone > config > config.lua`, in here we will search for `Config.UploadMethod`. This will give you 3 different options for all the file types. Change them all to `Qbox` like so:

```lua
Config.UploadMethod.Video = "Qbox" -- "Fivemanage" or "LBUpload" or "Custom"
Config.UploadMethod.Image = "Qbox" -- "Fivemanage" or "LBUpload" or "Custom"
Config.UploadMethod.Audio = "Qbox" -- "Fivemanage" or "LBUpload" or "Custom"
```

## Adding your API keys

Navigate to `server > apiKeys.lua`. Here you will see a table with all the API keys for the different upload methods. Simply add the same API key that you generated in the Qbox CDN dashboard.

```lua
API_KEYS = {
    Video = "API_KEY_HERE",
    Image = "API_KEY_HERE",
    Audio = "API_KEY_HERE",
}
```

And done, now your camera will work securely through presigned urls meaning your API keys never get leaked through lb-phone.
