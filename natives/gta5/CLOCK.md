# Natives de GTA V — CLOCK

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `CLOCK`: **16** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`AddToClockTime`](#addtoclocktime) · [`AdvanceClockTimeTo`](#advanceclocktimeto) · [`GetClockDayOfMonth`](#getclockdayofmonth) · [`GetClockDayOfWeek`](#getclockdayofweek) · [`GetClockHours`](#getclockhours) · [`GetClockMinutes`](#getclockminutes) · [`GetClockMonth`](#getclockmonth) · [`GetClockSeconds`](#getclockseconds) · [`GetClockYear`](#getclockyear) · [`GetLocalTime`](#getlocaltime) · [`GetMillisecondsPerGameMinute`](#getmillisecondspergameminute) · [`GetPosixTime`](#getposixtime) · [`GetUtcTime`](#getutctime) · [`PauseClock`](#pauseclock) · [`SetClockDate`](#setclockdate) · [`SetClockTime`](#setclocktime)

---
### AddToClockTime

`ADD_TO_CLOCK_TIME` · hash `0xD716F30D8C8980E2` · jhash `0xCC40D20D` · **Cliente**

```lua
AddToClockTime(hours, minutes, seconds)
```
```c
void ADD_TO_CLOCK_TIME(int hours, int minutes, int seconds);
```

**Parámetros**

- `hours` (`int`)
- `minutes` (`int`)
- `seconds` (`int`)

**Devuelve:** `void`

---
### AdvanceClockTimeTo

`ADVANCE_CLOCK_TIME_TO` · hash `0xC8CA9670B9D83B3B` · jhash `0x57B8DA7C` · **Cliente**

```lua
AdvanceClockTimeTo(hour, minute, second)
```
```c
void ADVANCE_CLOCK_TIME_TO(int hour, int minute, int second);
```

**Parámetros**

- `hour` (`int`)
- `minute` (`int`)
- `second` (`int`)

**Devuelve:** `void`

---
### GetClockDayOfMonth

`GET_CLOCK_DAY_OF_MONTH` · hash `0x3D10BC92A4DB1D35` · jhash `0xC7A5ACB7` · **Cliente**

```lua
local retval = GetClockDayOfMonth()
```
```c
int GET_CLOCK_DAY_OF_MONTH();
```

**Devuelve:** `int`

---
### GetClockDayOfWeek

`GET_CLOCK_DAY_OF_WEEK` · hash `0xD972E4BD7AEB235F` · jhash `0x84E4A289` · **Cliente**

```lua
local retval = GetClockDayOfWeek()
```
```c
int GET_CLOCK_DAY_OF_WEEK();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the current day of the week.  
0: Sunday  
1: Monday  
2: Tuesday  
3: Wednesday  
4: Thursday  
5: Friday  
6: Saturday  
```

---
### GetClockHours

`GET_CLOCK_HOURS` · hash `0x25223CA6B4D20B7F` · jhash `0x7EF8316F` · **Cliente**

```lua
local retval = GetClockHours()
```
```c
int GET_CLOCK_HOURS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the current ingame hour, expressed without zeros. (09:34 will be represented as 9)  
```

---
### GetClockMinutes

`GET_CLOCK_MINUTES` · hash `0x13D2B8ADD79640F2` · jhash `0x94AAC486` · **Cliente**

```lua
local retval = GetClockMinutes()
```
```c
int GET_CLOCK_MINUTES();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the current ingame clock minute.  
```

---
### GetClockMonth

`GET_CLOCK_MONTH` · hash `0xBBC72712E80257A1` · jhash `0x3C48A3D5` · **Cliente**

```lua
local retval = GetClockMonth()
```
```c
int GET_CLOCK_MONTH();
```

**Devuelve:** `int`

---
### GetClockSeconds

`GET_CLOCK_SECONDS` · hash `0x494E97C2EF27C470` · jhash `0x099C927E` · **Cliente**

```lua
local retval = GetClockSeconds()
```
```c
int GET_CLOCK_SECONDS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the current ingame clock second. Note that ingame clock seconds change really fast since a day in GTA is only 48 minutes in real life.  
```

---
### GetClockYear

`GET_CLOCK_YEAR` · hash `0x961777E64BDAF717` · jhash `0xB8BECF15` · **Cliente**

```lua
local retval = GetClockYear()
```
```c
int GET_CLOCK_YEAR();
```

**Devuelve:** `int`

---
### GetLocalTime

`GET_LOCAL_TIME` · hash `0x50C7A99057A69748` · jhash `0x124BCFA2` · **Cliente**

```lua
local year, month, day, hour, minute, second = GetLocalTime()
```
```c
void GET_LOCAL_TIME(int* year, int* month, int* day, int* hour, int* minute, int* second);
```

**Parámetros**

- `year` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `month` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `day` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `hour` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `minute` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `second` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Gets local system time as year, month, day, hour, minute and second.  
Example usage:  
int year;  
int month;  
int day;  
int hour;  
int minute;  
int second;  
or use std::tm struct  
TIME::GET_LOCAL_TIME(&year, &month, &day, &hour, &minute, &second);  
```

---
### GetMillisecondsPerGameMinute

`GET_MILLISECONDS_PER_GAME_MINUTE` · hash `0x2F8B4D1C595B11DB` · jhash `0x3B74095C` · **Cliente**

```lua
local retval = GetMillisecondsPerGameMinute()
```
```c
int GET_MILLISECONDS_PER_GAME_MINUTE();
```

**Devuelve:** `int` — A number of milliseconds that equals to one game minute.

**Descripción oficial:**

Returns how many real ms are equal to one game minute.
A getter for [`SetMillisecondsPerGameMinute`](../cfx/cliente-1.md#setmillisecondspergameminute).

---
### GetPosixTime

`GET_POSIX_TIME` · hash `0xDA488F299A5B164E` · jhash `0xE15A5281` · **Cliente**

```lua
local year, month, day, hour, minute, second = GetPosixTime()
```
```c
void GET_POSIX_TIME(int* year, int* month, int* day, int* hour, int* minute, int* second);
```

**Parámetros**

- `year` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `month` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `day` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `hour` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `minute` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `second` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Gets system time as year, month, day, hour, minute and second.  
Example usage:  
	int year;  
	int month;  
	int day;  
	int hour;  
	int minute;  
	int second;  
	TIME::GET_POSIX_TIME(&year, &month, &day, &hour, &minute, &second);  
```

---
### GetUtcTime

`GET_UTC_TIME` · hash `0x8117E09A19EEF4D3` · jhash `0xC589CD7D` · **Cliente**

```lua
local year, month, day, hour, minute, second = GetUtcTime()
```
```c
void GET_UTC_TIME(int* year, int* month, int* day, int* hour, int* minute, int* second);
```

**Parámetros**

- `year` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `month` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `day` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `hour` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `minute` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `second` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `void`

**Descripción oficial:**

```
Gets current UTC time
```

**Nombres antiguos (alias):** `_GET_UTC_TIME` (`GetUtcTime`)

---
### PauseClock

`PAUSE_CLOCK` · hash `0x4055E40BD2DBEC1D` · jhash `0xB02D6124` · **Cliente**

```lua
PauseClock(toggle)
```
```c
void PAUSE_CLOCK(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

---
### SetClockDate

`SET_CLOCK_DATE` · hash `0xB096419DF0D06CE7` · jhash `0x96891C94` · **Cliente**

```lua
SetClockDate(day, month, year)
```
```c
void SET_CLOCK_DATE(int day, int month, int year);
```

**Parámetros**

- `day` (`int`)
- `month` (`int`)
- `year` (`int`)

**Devuelve:** `void`

---
### SetClockTime

`SET_CLOCK_TIME` · hash `0x47C3B5848C3E45D8` · jhash `0x26F6AF14` · **Cliente**

```lua
SetClockTime(hour, minute, second)
```
```c
void SET_CLOCK_TIME(int hour, int minute, int second);
```

**Parámetros**

- `hour` (`int`)
- `minute` (`int`)
- `second` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
SET_CLOCK_TIME(12, 34, 56);  
```

---
