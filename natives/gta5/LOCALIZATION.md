# Natives de GTA V — LOCALIZATION

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `LOCALIZATION`: **3** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`GetCurrentLanguage`](#getcurrentlanguage) · [`LocalizationGetSystemDateFormat`](#localizationgetsystemdateformat) · [`LocalizationGetSystemLanguage`](#localizationgetsystemlanguage)

---
### GetCurrentLanguage

`GET_CURRENT_LANGUAGE` · hash `0x2BDD44CC428A7EAE` · jhash `0x761BE00B` · **Cliente**

```lua
local retval = GetCurrentLanguage()
```
```c
int GET_CURRENT_LANGUAGE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
0 = american (en-US)
1 = french (fr-FR)
2 = german (de-DE)
3 = italian (it-IT)
4 = spanish (es-ES)
5 = brazilian (pt-BR)
6 = polish (pl-PL)
7 = russian (ru-RU)
8 = korean (ko-KR)
9 = chinesetrad (zh-TW)
10 = japanese (ja-JP)
11 = mexican (es-MX)
12 = chinesesimp (zh-CN)
```

**Nombres antiguos (alias):** `_GET_UI_LANGUAGE_ID` (`GetUiLanguageId`), `_GET_CURRENT_LANGUAGE_ID` (`GetCurrentLanguageId`)

---
### LocalizationGetSystemDateFormat

`_LOCALIZATION_GET_SYSTEM_DATE_FORMAT` · hash `0xA8AE43AEC1A61314` · **Cliente**

```lua
local retval = LocalizationGetSystemDateFormat()
```
```c
int _LOCALIZATION_GET_SYSTEM_DATE_FORMAT();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Possible return values: 0, 1, 2
```

**Nombres antiguos (alias):** `_GET_USER_LANGUAGE_ID` (`GetUserLanguageId`)

---
### LocalizationGetSystemLanguage

`_LOCALIZATION_GET_SYSTEM_LANGUAGE` · hash `0x497420E022796B3F` · **Cliente**

```lua
local retval = LocalizationGetSystemLanguage()
```
```c
int _LOCALIZATION_GET_SYSTEM_LANGUAGE();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Same return values as GET_CURRENT_LANGUAGE
```

**Nombres antiguos (alias):** `0x497420E022796B3F` (`N_0x497420e022796b3f`)

---
