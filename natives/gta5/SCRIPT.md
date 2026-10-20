# Natives de GTA V — SCRIPT

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `SCRIPT`: **37** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`BgEndContext`](#bgendcontext) · [`BgEndContextHash`](#bgendcontexthash) · [`BgStartContext`](#bgstartcontext) · [`BgStartContextHash`](#bgstartcontexthash) · [`DoesScriptExist`](#doesscriptexist) · [`DoesScriptWithNameHashExist`](#doesscriptwithnamehashexist) · [`GetEventAtIndex`](#geteventatindex) · [`GetEventData`](#geteventdata) · [`GetEventExists`](#geteventexists) · [`GetHashOfThisScriptName`](#gethashofthisscriptname) · [`GetIdOfThisThread`](#getidofthisthread) · [`GetNameOfThread`](#getnameofthread) · [`GetNoLoadingScreen`](#getnoloadingscreen) · [`GetNumberOfEvents`](#getnumberofevents) · [`GetNumberOfReferencesOfScriptWithNameHash`](#getnumberofreferencesofscriptwithnamehash) · [`GetThisScriptName`](#getthisscriptname) · [`HasScriptLoaded`](#hasscriptloaded) · [`HasScriptWithNameHashLoaded`](#hasscriptwithnamehashloaded) · [`IsThreadActive`](#isthreadactive) · [`LockLoadingScreenButtons`](#lockloadingscreenbuttons) · [`N_0x0f6f1ebbc4e1d5e6`](#n_0x0f6f1ebbc4e1d5e6) · [`N_0x22e21fbcfc88c149`](#n_0x22e21fbcfc88c149) · [`N_0x760910b49d2b98ea`](#n_0x760910b49d2b98ea) · [`N_0x829cd22e043a2577`](#n_0x829cd22e043a2577) · [`N_0x836b62713e0534ca`](#n_0x836b62713e0534ca) · [`RequestScript`](#requestscript) · [`RequestScriptWithNameHash`](#requestscriptwithnamehash) · [`ScriptThreadIteratorGetNextThreadId`](#scriptthreaditeratorgetnextthreadid) · [`ScriptThreadIteratorReset`](#scriptthreaditeratorreset) · [`SetNoLoadingScreen`](#setnoloadingscreen) · [`SetScriptAsNoLongerNeeded`](#setscriptasnolongerneeded) · [`SetScriptWithNameHashAsNoLongerNeeded`](#setscriptwithnamehashasnolongerneeded) · [`ShutdownLoadingScreen`](#shutdownloadingscreen) · [`TerminateThisThread`](#terminatethisthread) · [`TerminateThread`](#terminatethread) · [`TriggerScriptEvent`](#triggerscriptevent) · [`TriggerScriptEvent_2`](#triggerscriptevent_2)

---
### BgEndContext

`BG_END_CONTEXT` · hash `0xDC2BACD920D0A0DD` · jhash `0x11F38FB3` · **Cliente**

```lua
BgEndContext(contextName)
```
```c
void BG_END_CONTEXT(char* contextName);
```

**Parámetros**

- `contextName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Deletes the given context from the background scripts context map.

NativeDB Introduced: v323
```

---
### BgEndContextHash

`BG_END_CONTEXT_HASH` · hash `0x107E5CC7CA942BC1` · jhash `0x3D981EBF` · **Cliente**

```lua
BgEndContextHash(contextHash)
```
```c
void BG_END_CONTEXT_HASH(Hash contextHash);
```

**Parámetros**

- `contextHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Hashed version of 0xDC2BACD920D0A0DD.

NativeDB Introduced: v323
```

---
### BgStartContext

`BG_START_CONTEXT` · hash `0x9D5A25BADB742ACD` · jhash `0xF3F1D953` · **Cliente**

```lua
BgStartContext(contextName)
```
```c
void BG_START_CONTEXT(char* contextName);
```

**Parámetros**

- `contextName` (`char*`)

**Devuelve:** `void`

**Descripción oficial:**

```
Inserts the given context into the background scripts context map.

NativeDB Introduced: v323
```

---
### BgStartContextHash

`BG_START_CONTEXT_HASH` · hash `0x75B18E49607874C7` · jhash `0x67B23E17` · **Cliente**

```lua
BgStartContextHash(contextHash)
```
```c
void BG_START_CONTEXT_HASH(Hash contextHash);
```

**Parámetros**

- `contextHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
Hashed version of 0x9D5A25BADB742ACD.

NativeDB Introduced: v323
```

---
### DoesScriptExist

`DOES_SCRIPT_EXIST` · hash `0xFC04745FBE67C19A` · jhash `0xDEAB87AB` · **Cliente**

```lua
local retval = DoesScriptExist(scriptName)
```
```c
BOOL DOES_SCRIPT_EXIST(char* scriptName);
```

**Parámetros**

- `scriptName` (`char*`)

**Devuelve:** `BOOL`

---
### DoesScriptWithNameHashExist

`DOES_SCRIPT_WITH_NAME_HASH_EXIST` · hash `0xF86AA3C56BA31381` · jhash `0x19EAE282` · **Cliente**

```lua
local retval = DoesScriptWithNameHashExist(scriptHash)
```
```c
BOOL DOES_SCRIPT_WITH_NAME_HASH_EXIST(Hash scriptHash);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF86AA3C56BA31381` (`N_0xf86aa3c56ba31381`), `_DOES_SCRIPT_WITH_NAME_HASH_EXIST` (`DoesScriptWithNameHashExist`)

---
### GetEventAtIndex

`GET_EVENT_AT_INDEX` · hash `0xD8F66A3A60C62153` · jhash `0xB49C1442` · **Cliente**

```lua
local retval = GetEventAtIndex(eventGroup, eventIndex)
```
```c
int GET_EVENT_AT_INDEX(int eventGroup, int eventIndex);
```

**Parámetros**

- `eventGroup` (`int`)
- `eventIndex` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
eventGroup: 0 = SCRIPT_EVENT_QUEUE_AI (CEventGroupScriptAI), 1 = SCRIPT_EVENT_QUEUE_NETWORK (CEventGroupScriptNetwork)
```

---
### GetEventData

`GET_EVENT_DATA` · hash `0x2902843FCD2B2D79` · jhash `0x4280F92F` · **Cliente**

```lua
local retval, eventData = GetEventData(eventGroup, eventIndex, eventDataSize)
```
```c
BOOL GET_EVENT_DATA(int eventGroup, int eventIndex, int* eventData, int eventDataSize);
```

**Parámetros**

- `eventGroup` (`int`)
- `eventIndex` (`int`)
- `eventData` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `eventDataSize` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
eventGroup: 0 = SCRIPT_EVENT_QUEUE_AI (CEventGroupScriptAI), 1 = SCRIPT_EVENT_QUEUE_NETWORK (CEventGroupScriptNetwork)
Note: eventDataSize is NOT the size in bytes, it is the size determined by the SIZE_OF operator (RAGE Script operator, not C/C++ sizeof). That is, the size in bytes divided by 8 (script variables are always 8-byte aligned!).
```

---
### GetEventExists

`GET_EVENT_EXISTS` · hash `0x936E6168A9BCEDB5` · jhash `0xA1B447B5` · **Cliente**

```lua
local retval = GetEventExists(eventGroup, eventIndex)
```
```c
BOOL GET_EVENT_EXISTS(int eventGroup, int eventIndex);
```

**Parámetros**

- `eventGroup` (`int`)
- `eventIndex` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
eventGroup: 0 = SCRIPT_EVENT_QUEUE_AI (CEventGroupScriptAI), 1 = SCRIPT_EVENT_QUEUE_NETWORK (CEventGroupScriptNetwork)
```

---
### GetHashOfThisScriptName

`GET_HASH_OF_THIS_SCRIPT_NAME` · hash `0x8A1C8B1738FFE87E` · jhash `0x2BEE1F45` · **Cliente**

```lua
local retval = GetHashOfThisScriptName()
```
```c
Hash GET_HASH_OF_THIS_SCRIPT_NAME();
```

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `_GET_THIS_SCRIPT_HASH` (`GetThisScriptHash`)

---
### GetIdOfThisThread

`GET_ID_OF_THIS_THREAD` · hash `0xC30338E8088E2E21` · jhash `0xDE524830` · **Cliente**

```lua
local retval = GetIdOfThisThread()
```
```c
int GET_ID_OF_THIS_THREAD();
```

**Devuelve:** `int`

---
### GetNameOfThread

`_GET_NAME_OF_THREAD` · hash `0x05A42BA9FC8DA96B` · jhash `0xBE7ACD89` · **Cliente**

```lua
local retval = GetNameOfThread(threadId)
```
```c
char* _GET_NAME_OF_THREAD(int threadId);
```

**Parámetros**

- `threadId` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `_GET_THREAD_NAME` (`GetThreadName`)

---
### GetNoLoadingScreen

`GET_NO_LOADING_SCREEN` · hash `0x18C1270EA7F199BC` · jhash `0x27512BA0` · **Cliente**

```lua
local retval = GetNoLoadingScreen()
```
```c
BOOL GET_NO_LOADING_SCREEN();
```

**Devuelve:** `BOOL` — The value that was set by [SET_NO_LOADING_SCREEN](#setnoloadingscreen)

**Nombres antiguos (alias):** `_GET_NO_LOADING_SCREEN` (`GetNoLoadingScreen`)

**Ejemplo (lua):**

```lua
SetNoLoadingScreen(true)
print(GetNoLoadingScreen()) -- will return true
```

---
### GetNumberOfEvents

`GET_NUMBER_OF_EVENTS` · hash `0x5F92A689A06620AA` · jhash `0xA3525D60` · **Cliente**

```lua
local retval = GetNumberOfEvents(eventGroup)
```
```c
int GET_NUMBER_OF_EVENTS(int eventGroup);
```

**Parámetros**

- `eventGroup` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
eventGroup: 0 = SCRIPT_EVENT_QUEUE_AI (CEventGroupScriptAI), 1 = SCRIPT_EVENT_QUEUE_NETWORK (CEventGroupScriptNetwork)
```

---
### GetNumberOfReferencesOfScriptWithNameHash

`_GET_NUMBER_OF_REFERENCES_OF_SCRIPT_WITH_NAME_HASH` · hash `0x2C83A9DA6BFFC4F9` · jhash `0x029D3841` · **Cliente**

```lua
local retval = GetNumberOfReferencesOfScriptWithNameHash(scriptHash)
```
```c
int _GET_NUMBER_OF_REFERENCES_OF_SCRIPT_WITH_NAME_HASH(Hash scriptHash);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
Gets the number of instances of the specified script is currently running.
Actually returns numRefs - 1.
if (program)
	v3 = rage::scrProgram::GetNumRefs(program) - 1;
return v3;
```

**Nombres antiguos (alias):** `_GET_NUMBER_OF_INSTANCES_OF_STREAMED_SCRIPT` (`GetNumberOfInstancesOfStreamedScript`), `_GET_NUMBER_OF_INSTANCES_OF_SCRIPT_WITH_NAME_HASH` (`GetNumberOfInstancesOfScriptWithNameHash`)

---
### GetThisScriptName

`GET_THIS_SCRIPT_NAME` · hash `0x442E0A7EDE4A738A` · jhash `0xA40FD5D9` · **Cliente**

```lua
local retval = GetThisScriptName()
```
```c
char* GET_THIS_SCRIPT_NAME();
```

**Devuelve:** `char*`

---
### HasScriptLoaded

`HAS_SCRIPT_LOADED` · hash `0xE6CC9F3BA0FB9EF1` · jhash `0x5D67F751` · **Cliente**

```lua
local retval = HasScriptLoaded(scriptName)
```
```c
BOOL HAS_SCRIPT_LOADED(char* scriptName);
```

**Parámetros**

- `scriptName` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Returns if a script has been loaded into the game. Used to see if a script was loaded after requesting.

---
### HasScriptWithNameHashLoaded

`HAS_SCRIPT_WITH_NAME_HASH_LOADED` · hash `0x5F0F0C783EB16C04` · jhash `0x06674818` · **Cliente**

```lua
local retval = HasScriptWithNameHashLoaded(scriptHash)
```
```c
BOOL HAS_SCRIPT_WITH_NAME_HASH_LOADED(Hash scriptHash);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_HAS_STREAMED_SCRIPT_LOADED` (`HasStreamedScriptLoaded`)

---
### IsThreadActive

`IS_THREAD_ACTIVE` · hash `0x46E9AE36D8FA6417` · jhash `0x78D7A5A0` · **Cliente**

```lua
local retval = IsThreadActive(threadId)
```
```c
BOOL IS_THREAD_ACTIVE(int threadId);
```

**Parámetros**

- `threadId` (`int`)

**Devuelve:** `BOOL`

---
### LockLoadingScreenButtons

`_LOCK_LOADING_SCREEN_BUTTONS` · hash `0xB1577667C3708F9B` · jhash `0xB03BCCDF` · **Cliente**

```lua
LockLoadingScreenButtons()
```
```c
void _LOCK_LOADING_SCREEN_BUTTONS();
```

**Devuelve:** `void`

**Descripción oficial:**

Updates the display of the MP/SP loading buttons, and locks the state so that other options are not displayed or changed. This can only be done once.

**Nombres antiguos (alias):** `0xB1577667C3708F9B` (`N_0xb1577667c3708f9b`)

---
### N_0x0f6f1ebbc4e1d5e6

`0x0F6F1EBBC4E1D5E6` · hash `0x0F6F1EBBC4E1D5E6` · jhash `0xF8E5F73A` · **Cliente**

```lua
local retval = N_0x0f6f1ebbc4e1d5e6(scriptIndex, p1)
```
```c
BOOL 0x0F6F1EBBC4E1D5E6(int scriptIndex, char* p1);
```

**Parámetros**

- `scriptIndex` (`int`)
- `p1` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
BG_*

NativeDB Introduced: v323
```

---
### N_0x22e21fbcfc88c149

`0x22E21FBCFC88C149` · hash `0x22E21FBCFC88C149` · jhash `0x682CB7E1` · **Cliente**

```lua
local retval = N_0x22e21fbcfc88c149(scriptIndex, p1)
```
```c
int 0x22E21FBCFC88C149(int scriptIndex, char* p1);
```

**Parámetros**

- `scriptIndex` (`int`)
- `p1` (`char*`)

**Devuelve:** `int`

**Descripción oficial:**

```
BG_*

NativeDB Introduced: v323
```

---
### N_0x760910b49d2b98ea

`0x760910B49D2B98EA` · hash `0x760910B49D2B98EA` · jhash `0x5C95B670` · **Cliente**

```lua
N_0x760910b49d2b98ea()
```
```c
void 0x760910B49D2B98EA();
```

**Devuelve:** `void`

**Descripción oficial:**

```
Sets bit 1 in GtaThread+0x154

BG_*

NativeDB Introduced: v323
```

---
### N_0x829cd22e043a2577

`0x829CD22E043A2577` · hash `0x829CD22E043A2577` · jhash `0xC515E735` · **Cliente**

```lua
local retval = N_0x829cd22e043a2577(p0)
```
```c
int 0x829CD22E043A2577(Hash p0);
```

**Parámetros**

- `p0` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `int`

**Descripción oficial:**

```
BG_*

NativeDB Introduced: v323
```

---
### N_0x836b62713e0534ca

`0x836B62713E0534CA` · hash `0x836B62713E0534CA` · jhash `0x22B9F132` · **Cliente**

```lua
local retval = N_0x836b62713e0534ca()
```
```c
BOOL 0x836B62713E0534CA();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Returns true if bit 0 in GtaThread+0x154 is set.

BG_*

NativeDB Introduced: v323
```

---
### RequestScript

`REQUEST_SCRIPT` · hash `0x6EB5F71AA68F2E8E` · jhash `0xE26B2666` · **Cliente**

```lua
RequestScript(scriptName)
```
```c
void REQUEST_SCRIPT(char* scriptName);
```

**Parámetros**

- `scriptName` (`char*`)

**Devuelve:** `void`

---
### RequestScriptWithNameHash

`REQUEST_SCRIPT_WITH_NAME_HASH` · hash `0xD62A67D26D9653E6` · jhash `0x1C68D9DC` · **Cliente**

```lua
RequestScriptWithNameHash(scriptHash)
```
```c
void REQUEST_SCRIPT_WITH_NAME_HASH(Hash scriptHash);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Descripción oficial:**

```
formerly _REQUEST_STREAMED_SCRIPT  
```

**Nombres antiguos (alias):** `_REQUEST_STREAMED_SCRIPT` (`RequestStreamedScript`)

---
### ScriptThreadIteratorGetNextThreadId

`SCRIPT_THREAD_ITERATOR_GET_NEXT_THREAD_ID` · hash `0x30B4FA1C82DD4B9F` · jhash `0x1E28B28F` · **Cliente**

```lua
local retval = ScriptThreadIteratorGetNextThreadId()
```
```c
int SCRIPT_THREAD_ITERATOR_GET_NEXT_THREAD_ID();
```

**Devuelve:** `int`

**Descripción oficial:**

```
If the function returns 0, the end of the iteration has been reached.
```

**Nombres antiguos (alias):** `0x30B4FA1C82DD4B9F` (`N_0x30b4fa1c82dd4b9f`), `_GET_ID_OF_NEXT_THREAD_IN_ENUMERATION` (`GetIdOfNextThreadInEnumeration`)

---
### ScriptThreadIteratorReset

`SCRIPT_THREAD_ITERATOR_RESET` · hash `0xDADFADA5A20143A8` · jhash `0xBB4E2F66` · **Cliente**

```lua
ScriptThreadIteratorReset()
```
```c
void SCRIPT_THREAD_ITERATOR_RESET();
```

**Devuelve:** `void`

**Descripción oficial:**

Starts a new iteration of the current threads.
Call this first, then SCRIPT_THREAD_ITERATOR_GET_NEXT_THREAD_ID (0x30B4FA1C82DD4B9F)

**Nombres antiguos (alias):** `0xDADFADA5A20143A8` (`N_0xdadfada5a20143a8`), `_BEGIN_ENUMERATING_THREADS` (`BeginEnumeratingThreads`)

---
### SetNoLoadingScreen

`SET_NO_LOADING_SCREEN` · hash `0x5262CC1995D07E09` · jhash `0xC8055034` · **Cliente**

```lua
SetNoLoadingScreen(toggle)
```
```c
void SET_NO_LOADING_SCREEN(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`): Enabled/Disable

**Devuelve:** `void`

**Descripción oficial:**

Doesn't seem to do anything. Set value can be retrieved using [`GET_NO_LOADING_SCREEN`](#getnoloadingscreen).

**Ejemplo (lua):**

```lua
SetNoLoadingScreen(true)
print(GetNoLoadingScreen()) -- will return true
```

---
### SetScriptAsNoLongerNeeded

`SET_SCRIPT_AS_NO_LONGER_NEEDED` · hash `0xC90D2DCACD56184C` · jhash `0x6FCB7795` · **Cliente**

```lua
SetScriptAsNoLongerNeeded(scriptName)
```
```c
void SET_SCRIPT_AS_NO_LONGER_NEEDED(char* scriptName);
```

**Parámetros**

- `scriptName` (`char*`)

**Devuelve:** `void`

---
### SetScriptWithNameHashAsNoLongerNeeded

`SET_SCRIPT_WITH_NAME_HASH_AS_NO_LONGER_NEEDED` · hash `0xC5BC038960E9DB27` · jhash `0x96C26F66` · **Cliente**

```lua
SetScriptWithNameHashAsNoLongerNeeded(scriptHash)
```
```c
void SET_SCRIPT_WITH_NAME_HASH_AS_NO_LONGER_NEEDED(Hash scriptHash);
```

**Parámetros**

- `scriptHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `_SET_STREAMED_SCRIPT_AS_NO_LONGER_NEEDED` (`SetStreamedScriptAsNoLongerNeeded`)

---
### ShutdownLoadingScreen

`SHUTDOWN_LOADING_SCREEN` · hash `0x078EBE9809CCD637` · jhash `0xA2826D17` · **Cliente**

```lua
ShutdownLoadingScreen()
```
```c
void SHUTDOWN_LOADING_SCREEN();
```

**Devuelve:** `void`

**Descripción oficial:**

Shuts down the loading screen and switches to normal game view. Should only be used by [spawnmanager](https://docs.fivem.net/docs/resources/spawnmanager/) or similar resources after loading and spawning the player ped. If no script does this, the game is stuck in the infamous bridge screen with the "Awaiting scripts" text and loading circle at the bottom right corner.

![](https://i.imgur.com/WULopNH.jpeg)

**Ejemplo (lua):**

```lua
ShutdownLoadingScreen()
```

---
### TerminateThisThread

`TERMINATE_THIS_THREAD` · hash `0x1090044AD1DA76FA` · jhash `0x3CD9CBB7` · **Cliente**

```lua
TerminateThisThread()
```
```c
void TERMINATE_THIS_THREAD();
```

**Devuelve:** `void`

---
### TerminateThread

`TERMINATE_THREAD` · hash `0xC8B189ED9138BCD4` · jhash `0x253FD520` · **Cliente**

```lua
TerminateThread(threadId)
```
```c
void TERMINATE_THREAD(int threadId);
```

**Parámetros**

- `threadId` (`int`)

**Devuelve:** `void`

---
### TriggerScriptEvent

`TRIGGER_SCRIPT_EVENT` · hash `0x5AE99C571D5BBE5D` · jhash `0x54763B35` · **Cliente**

```lua
local eventData = TriggerScriptEvent(eventGroup, eventDataSize, playerBits)
```
```c
void TRIGGER_SCRIPT_EVENT(int eventGroup, int* eventData, int eventDataSize, int playerBits);
```

**Parámetros**

- `eventGroup` (`int`)
- `eventData` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `eventDataSize` (`int`)
- `playerBits` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
eventGroup: 0 = SCRIPT_EVENT_QUEUE_AI (CEventGroupScriptAI), 1 = SCRIPT_EVENT_QUEUE_NETWORK (CEventGroupScriptNetwork)
Note: eventDataSize is NOT the size in bytes, it is the size determined by the SIZE_OF operator (RAGE Script operator, not C/C++ sizeof). That is, the size in bytes divided by 8 (script variables are always 8-byte aligned!).
playerBits (also known as playersToBroadcastTo) is a bitset that indicates which players this event should be sent to. In order to send the event to specific players only, use (1 << playerIndex). Set all bits if it should be broadcast to all players.
```

---
### TriggerScriptEvent_2

`_TRIGGER_SCRIPT_EVENT_2` · hash `0xA40CC53DF8E50837` · **Cliente**

```lua
local eventData = TriggerScriptEvent_2(eventGroup, eventDataSize, playerBits)
```
```c
void _TRIGGER_SCRIPT_EVENT_2(int eventGroup, int* eventData, int eventDataSize, int playerBits);
```

**Parámetros**

- `eventGroup` (`int`)
- `eventData` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `eventDataSize` (`int`)
- `playerBits` (`int`)

**Devuelve:** `void`

**Descripción oficial:**

```
See TRIGGER_SCRIPT_EVENT
```

**Nombres antiguos (alias):** `0xA40CC53DF8E50837` (`N_0xa40cc53df8e50837`)

---
