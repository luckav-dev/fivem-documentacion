# Natives de GTA V — DECORATOR

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `DECORATOR`: **12** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`DecorExistOn`](#decorexiston) · [`DecorGetBool`](#decorgetbool) · [`DecorGetFloat`](#decorgetfloat) · [`DecorGetInt`](#decorgetint) · [`DecorIsRegisteredAsType`](#decorisregisteredastype) · [`DecorRegister`](#decorregister) · [`DecorRegisterLock`](#decorregisterlock) · [`DecorRemove`](#decorremove) · [`DecorSetBool`](#decorsetbool) · [`DecorSetFloat`](#decorsetfloat) · [`DecorSetInt`](#decorsetint) · [`DecorSetTime`](#decorsettime)

---
### DecorExistOn

`DECOR_EXIST_ON` · hash `0x05661B80A8C9165F` · jhash `0x74EF9C40` · **Cliente**

```lua
local retval = DecorExistOn(entity, propertyName)
```
```c
BOOL DECOR_EXIST_ON(Entity entity, char* propertyName);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns whether or not the specified property is set for the entity.  
```

---
### DecorGetBool

`DECOR_GET_BOOL` · hash `0xDACE671663F2F5DB` · jhash `0xDBCE51E0` · **Cliente**

```lua
local retval = DecorGetBool(entity, propertyName)
```
```c
BOOL DECOR_GET_BOOL(Entity entity, char* propertyName);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)

**Devuelve:** `BOOL`

---
### DecorGetFloat

`DECOR_GET_FLOAT` · hash `0x6524A2F114706F43` · jhash `0x8DE5382F` · **Cliente**

```lua
local retval = DecorGetFloat(entity, propertyName)
```
```c
float DECOR_GET_FLOAT(Entity entity, char* propertyName);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)

**Devuelve:** `float`

**Nombres antiguos (alias):** `_DECOR_GET_FLOAT` (`DecorGetFloat`)

---
### DecorGetInt

`DECOR_GET_INT` · hash `0xA06C969B02A97298` · jhash `0xDDDE59B5` · **Cliente**

```lua
local retval = DecorGetInt(entity, propertyName)
```
```c
int DECOR_GET_INT(Entity entity, char* propertyName);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)

**Devuelve:** `int`

---
### DecorIsRegisteredAsType

`DECOR_IS_REGISTERED_AS_TYPE` · hash `0x4F14F9F870D6FBC8` · jhash `0x7CF0971D` · **Cliente**

```lua
local retval = DecorIsRegisteredAsType(propertyName, type)
```
```c
BOOL DECOR_IS_REGISTERED_AS_TYPE(char* propertyName, int type);
```

**Parámetros**

- `propertyName` (`char*`)
- `type` (`int`): See [`DECOR_REGISTER`](#decorregister).

**Devuelve:** `BOOL`

---
### DecorRegister

`DECOR_REGISTER` · hash `0x9FD90732F56403CE` · jhash `0x68BD42A9` · **Cliente**

```lua
DecorRegister(propertyName, type)
```
```c
void DECOR_REGISTER(char* propertyName, int type);
```

**Parámetros**

- `propertyName` (`char*`)
- `type` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```cpp
enum eDecorType
{
    DECOR_TYPE_FLOAT = 1,
    DECOR_TYPE_BOOL = 2,
    DECOR_TYPE_INT = 3,
    DECOR_TYPE_STRING = 4,
    DECOR_TYPE_TIME = 5
};
```

---
### DecorRegisterLock

`DECOR_REGISTER_LOCK` · hash `0xA9D14EEA259F9248` · jhash `0x7F3F1C02` · **Cliente**

```lua
DecorRegisterLock()
```
```c
void DECOR_REGISTER_LOCK();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Called after all decorator type initializations.  
```

---
### DecorRemove

`DECOR_REMOVE` · hash `0x00EE9F297C738720` · jhash `0xE0E2640B` · **Cliente**

```lua
local retval = DecorRemove(entity, propertyName)
```
```c
BOOL DECOR_REMOVE(Entity entity, char* propertyName);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)

**Devuelve:** `BOOL`

---
### DecorSetBool

`DECOR_SET_BOOL` · hash `0x6B1E8E2ED1335B71` · jhash `0x8E101F5C` · **Cliente**

```lua
local retval = DecorSetBool(entity, propertyName, value)
```
```c
BOOL DECOR_SET_BOOL(Entity entity, char* propertyName, BOOL value);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)
- `value` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
This function sets metadata of type bool to specified entity.  
```

---
### DecorSetFloat

`DECOR_SET_FLOAT` · hash `0x211AB1DD8D0F363A` · jhash `0xBC7BD5CB` · **Cliente**

```lua
local retval = DecorSetFloat(entity, propertyName, value)
```
```c
BOOL DECOR_SET_FLOAT(Entity entity, char* propertyName, float value);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)
- `value` (`float`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_DECOR_SET_FLOAT` (`DecorSetFloat`)

---
### DecorSetInt

`DECOR_SET_INT` · hash `0x0CE3AA5E1CA19E10` · jhash `0xDB718B21` · **Cliente**

```lua
local retval = DecorSetInt(entity, propertyName, value)
```
```c
BOOL DECOR_SET_INT(Entity entity, char* propertyName, int value);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)
- `value` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Sets property to int.  
```

---
### DecorSetTime

`DECOR_SET_TIME` · hash `0x95AED7B8E39ECAA4` · jhash `0xBBAEEF94` · **Cliente**

```lua
local retval = DecorSetTime(entity, propertyName, timestamp)
```
```c
BOOL DECOR_SET_TIME(Entity entity, char* propertyName, int timestamp);
```

**Parámetros**

- `entity` (`Entity`)
- `propertyName` (`char*`)
- `timestamp` (`int`)

**Devuelve:** `BOOL`

---
