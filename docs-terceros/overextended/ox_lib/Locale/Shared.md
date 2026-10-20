> Fuente original: https://github.com/overextended/docs/blob/328e36feb5b0486d6214971f53c6d2626193cc28/content/docs/ox_lib/Locale/Shared.mdx · repositorio overextended/docs @ 328e36f · copiado el 2026-10-20

# Shared

Allows servers to set a preferred language and attempt to load locale files in any resources using the module.
Locale files should use the [ISO Language Code](http://www.lingoes.net/en/translator/langcode.htm) and be saved as `./locales/langcode.json`

## Setup

To change the preferred language from English, add the convar to your server.cfg and change `en` to the desired language code.

```yaml
setr ox:locale en
```

Create a locales directory and a file for your language.

```json filename="locales/en.json"
{
  "grand_theft_auto": "grand theft auto",
  "male": "male",
  "female": "female",
  "suspect_sex": "suspect is %s"
}
```

```json filename="locales/fr.json"
{
  "grand_theft_auto": "vol de voiture",
  "male": "homme",
  "female": "femme",
  "suspect_sex": "le suspect est %s"
}
```

```lua filename="fxmanifest.lua"
files {
  'locales/*.json'
}
```

## Usage

Initialise the locale module in your resource (once).

**Lua**

```lua
lib.locale()
```

**JS**

  ```ts
  import {initLocale} from '@overextended/ox_lib/shared'

initLocale()

````

Format your strings with the new locale global.
Additional arguments can be sent to format the locale output.

**Lua**

```lua
locale(str, ...)
```

**JS**

```ts
import { locale } from '@overextended/ox_lib/shared'

locale(str, ...)
```

- str: `string`
- vararg?: `string` or `number`

<u>**Example**</u>

**Lua**

```lua
-- Load the locale module
lib.locale()

SetInterval(function()
    print(locale('grand_theft_auto'))
    print(locale('suspect_sex', locale('male')))
end, 5000)
````

**JS**

```ts
import { initLocale, locale } from '@overextended/ox_lib/shared

// Load the locale module
initLocale()

setInterval(() => {
  console.log(locale('grand_theft_auto'))
  console.log(locale('suspect_sex', locale('male')))
}, 5000)
```

## Phrases

You can create a locale string that references other locales to construct a phrase, rather than calling locale multiple times.

```json
{
  "hello": "hello %s",
  "my_name_is": "my name is %s",
  "hello_my_name_is": "${hello}! ${my_name_is}."
}
```

**Lua**

```lua
print(locale('hello_my_name_is', 'doka', 'linden'))
```

**JS**

```ts
import { locale } from '@overextended/ox_lib/shared'

console.log(locale('hello_my_name_is', 'doka', 'linden'))
```

## lib.getLocale

Gets a locale string from another resource and adds it to the dict.

```lua
lib.getLocale(resource, key)
```

- resource: `string`
- key: `string`
