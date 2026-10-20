# Natives de GTA V — SOCIALCLUB

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `SOCIALCLUB`: **83** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`IsRockstarMessageReadyForScript`](#isrockstarmessagereadyforscript) · [`N_0x07dbd622d9533857`](#n_0x07dbd622d9533857) · [`N_0x116fb94dc4b79f17`](#n_0x116fb94dc4b79f17) · [`N_0x16da8172459434aa`](#n_0x16da8172459434aa) · [`N_0x19853b5b17d77bca`](#n_0x19853b5b17d77bca) · [`N_0x1d12a56fc95be92e`](#n_0x1d12a56fc95be92e) · [`N_0x225798743970412b`](#n_0x225798743970412b) · [`N_0x2570e26be63964e3`](#n_0x2570e26be63964e3) · [`N_0x2d874d4ae612a65f`](#n_0x2d874d4ae612a65f) · [`N_0x3001bef2feca3680`](#n_0x3001bef2feca3680) · [`N_0x33df47cc0642061b`](#n_0x33df47cc0642061b) · [`N_0x44aca259d67651db`](#n_0x44aca259d67651db) · [`N_0x450819d8cf90c416`](#n_0x450819d8cf90c416) · [`N_0x4737980e8a283806`](#n_0x4737980e8a283806) · [`N_0x487912fd248efddf`](#n_0x487912fd248efddf) · [`N_0x4a7d6e727f941747`](#n_0x4a7d6e727f941747) · [`N_0x4ed9c8d6da297639`](#n_0x4ed9c8d6da297639) · [`N_0x50a8a36201dbf83e`](#n_0x50a8a36201dbf83e) · [`N_0x675721c9f644d161`](#n_0x675721c9f644d161) · [`N_0x699e4a5c8c893a18`](#n_0x699e4a5c8c893a18) · [`N_0x6bfb12ce158e3dd4`](#n_0x6bfb12ce158e3dd4) · [`N_0x710bcda8071eded1`](#n_0x710bcda8071eded1) · [`N_0x7db18ca8cad5b098`](#n_0x7db18ca8cad5b098) · [`N_0x7ffcbfee44ecfabf`](#n_0x7ffcbfee44ecfabf) · [`N_0x8a4416c0db05fa66`](#n_0x8a4416c0db05fa66) · [`N_0x8cc469ab4d349b7c`](#n_0x8cc469ab4d349b7c) · [`N_0x9237e334f6e43156`](#n_0x9237e334f6e43156) · [`N_0x92da6e70ef249bd1`](#n_0x92da6e70ef249bd1) · [`N_0x9de5d2f723575ed0`](#n_0x9de5d2f723575ed0) · [`N_0xa468e0be12b12c70`](#n_0xa468e0be12b12c70) · [`N_0xc2c97ea97711d1ae`](#n_0xc2c97ea97711d1ae) · [`N_0xc5a35c73b68f3c49`](#n_0xc5a35c73b68f3c49) · [`N_0xd8122c407663b995`](#n_0xd8122c407663b995) · [`N_0xe4f6e8d07a2f0f51`](#n_0xe4f6e8d07a2f0f51) · [`N_0xe75a4a2e5e316d86`](#n_0xe75a4a2e5e316d86) · [`N_0xea95c0853a27888e`](#n_0xea95c0853a27888e) · [`N_0xf22ca0fd74b80e7a`](#n_0xf22ca0fd74b80e7a) · [`N_0xf6baaaf762e1bf40`](#n_0xf6baaaf762e1bf40) · [`N_0xfe4c1d0d3b9cc17e`](#n_0xfe4c1d0d3b9cc17e) · [`N_0xff8f3a92b75ed67a`](#n_0xff8f3a92b75ed67a) · [`RockstarMessageGetString`](#rockstarmessagegetstring) · [`ScEmailMessageClearRecipList`](#scemailmessageclearreciplist) · [`ScEmailMessagePushGamerToRecipList`](#scemailmessagepushgamertoreciplist) · [`ScGamerdataGetBool`](#scgamerdatagetbool) · [`ScGamerdataGetFloat`](#scgamerdatagetfloat) · [`ScGamerdataGetInt`](#scgamerdatagetint) · [`ScGetHasAchievementBeenPassed`](#scgethasachievementbeenpassed) · [`ScGetNickname`](#scgetnickname) · [`ScInboxGetEmails`](#scinboxgetemails) · [`ScInboxGetMessageIsReadAtIndex`](#scinboxgetmessageisreadatindex) · [`ScInboxGetMessageTypeAtIndex`](#scinboxgetmessagetypeatindex) · [`ScInboxGetTotalNumMessages`](#scinboxgettotalnummessages) · [`ScInboxMessageDoApply`](#scinboxmessagedoapply) · [`ScInboxMessageGetBountyData`](#scinboxmessagegetbountydata) · [`ScInboxMessageGetDataBool`](#scinboxmessagegetdatabool) · [`ScInboxMessageGetDataInt`](#scinboxmessagegetdataint) · [`ScInboxMessageGetDataString`](#scinboxmessagegetdatastring) · [`ScInboxMessageGetString`](#scinboxmessagegetstring) · [`ScInboxMessageGetUgcdata`](#scinboxmessagegetugcdata) · [`ScInboxMessagePop`](#scinboxmessagepop) · [`ScInboxMessagePushGamerToEventRecipList`](#scinboxmessagepushgamertoeventreciplist) · [`ScInboxMessageSendBountyPresenceEvent`](#scinboxmessagesendbountypresenceevent) · [`ScInboxMessageSendUgcStatUpdateEvent`](#scinboxmessagesendugcstatupdateevent) · [`ScLicenseplateAdd`](#sclicenseplateadd) · [`ScLicenseplateGetAddIsPending`](#sclicenseplategetaddispending) · [`ScLicenseplateGetAddStatus`](#sclicenseplategetaddstatus) · [`ScLicenseplateGetCount`](#sclicenseplategetcount) · [`ScLicenseplateGetIsvalidIsPending`](#sclicenseplategetisvalidispending) · [`ScLicenseplateGetIsvalidStatus`](#sclicenseplategetisvalidstatus) · [`ScLicenseplateGetPlate`](#sclicenseplategetplate) · [`ScLicenseplateGetPlateData`](#sclicenseplategetplatedata) · [`ScLicenseplateIsvalid`](#sclicenseplateisvalid) · [`ScLicenseplateSetPlateData`](#sclicenseplatesetplatedata) · [`ScPresenceAttrSetFloat`](#scpresenceattrsetfloat) · [`ScPresenceAttrSetInt`](#scpresenceattrsetint) · [`ScPresenceAttrSetString`](#scpresenceattrsetstring) · [`ScProfanityCheckString`](#scprofanitycheckstring) · [`ScProfanityCheckUgcString`](#scprofanitycheckugcstring) · [`ScProfanityGetCheckIsPending`](#scprofanitygetcheckispending) · [`ScProfanityGetCheckIsValid`](#scprofanitygetcheckisvalid) · [`ScProfanityGetStringPassed`](#scprofanitygetstringpassed) · [`ScProfanityGetStringStatus`](#scprofanitygetstringstatus) · [`SetHandleRockstarMessageViaScript`](#sethandlerockstarmessageviascript)

---
### IsRockstarMessageReadyForScript

`_IS_ROCKSTAR_MESSAGE_READY_FOR_SCRIPT` · hash `0xBC1CC91205EC8D6E` · jhash `0x6C5738AB` · **Cliente**

```lua
local retval = IsRockstarMessageReadyForScript()
```
```c
BOOL _IS_ROCKSTAR_MESSAGE_READY_FOR_SCRIPT();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBC1CC91205EC8D6E` (`N_0xbc1cc91205ec8d6e`)

---
### N_0x07dbd622d9533857

`0x07DBD622D9533857` · hash `0x07DBD622D9533857` · **Cliente**

```lua
local retval = N_0x07dbd622d9533857(p0)
```
```c
Any 0x07DBD622D9533857(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x116fb94dc4b79f17

`0x116FB94DC4B79F17` · hash `0x116FB94DC4B79F17` · jhash `0xAF3C081B` · **Cliente**

```lua
N_0x116fb94dc4b79f17(p0)
```
```c
void 0x116FB94DC4B79F17(char* p0);
```

**Parámetros**

- `p0` (`char*`)

**Devuelve:** `void`

---
### N_0x16da8172459434aa

`0x16DA8172459434AA` · hash `0x16DA8172459434AA` · **Cliente**

```lua
local retval = N_0x16da8172459434aa()
```
```c
Any 0x16DA8172459434AA();
```

**Devuelve:** `Any`

---
### N_0x19853b5b17d77bca

`0x19853B5B17D77BCA` · hash `0x19853B5B17D77BCA` · jhash `0xD26CCA46` · **Cliente**

```lua
local retval, p1 = N_0x19853b5b17d77bca(p0, p1)
```
```c
BOOL 0x19853B5B17D77BCA(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x1d12a56fc95be92e

`0x1D12A56FC95BE92E` · hash `0x1D12A56FC95BE92E` · jhash `0x92452C0E` · **Cliente**

```lua
local retval = N_0x1d12a56fc95be92e()
```
```c
BOOL 0x1D12A56FC95BE92E();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Added Parameter 2: char* p1
NativeDB Added Parameter 3: char* p2
NativeDB Introduced: v323
```

---
### N_0x225798743970412b

`0x225798743970412B` · hash `0x225798743970412B` · **Cliente**

```lua
local retval, p0 = N_0x225798743970412b(p0)
```
```c
BOOL 0x225798743970412B(int* p0);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x2570e26be63964e3

`0x2570E26BE63964E3` · hash `0x2570E26BE63964E3` · jhash `0x59394583` · **Cliente**

```lua
local retval = N_0x2570e26be63964e3()
```
```c
BOOL 0x2570E26BE63964E3();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Added Parameter 2: float* p1
NativeDB Added Parameter 3: char* p2
NativeDB Introduced: v323
```

---
### N_0x2d874d4ae612a65f

`0x2D874D4AE612A65F` · hash `0x2D874D4AE612A65F` · **Cliente**

```lua
local retval = N_0x2d874d4ae612a65f()
```
```c
Any 0x2D874D4AE612A65F();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### N_0x3001bef2feca3680

`0x3001BEF2FECA3680` · hash `0x3001BEF2FECA3680` · jhash `0x4D4C37B3` · **Cliente**

```lua
local retval = N_0x3001bef2feca3680()
```
```c
BOOL 0x3001BEF2FECA3680();
```

**Devuelve:** `BOOL`

---
### N_0x33df47cc0642061b

`0x33DF47CC0642061B` · hash `0x33DF47CC0642061B` · jhash `0xBBA8D34D` · **Cliente**

```lua
local retval = N_0x33df47cc0642061b()
```
```c
BOOL 0x33DF47CC0642061B();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Added Parameter 2: char* p1
NativeDB Introduced: v323
```

---
### N_0x44aca259d67651db

`0x44ACA259D67651DB` · hash `0x44ACA259D67651DB` · **Cliente**

```lua
local p0 = N_0x44aca259d67651db(p1)
```
```c
void 0x44ACA259D67651DB(Any* p0, Any p1);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`Any`)

**Devuelve:** `void`

---
### N_0x450819d8cf90c416

`0x450819D8CF90C416` · hash `0x450819D8CF90C416` · jhash `0x0572EB5E` · **Cliente**

```lua
local retval = N_0x450819d8cf90c416()
```
```c
BOOL 0x450819D8CF90C416();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Introduced: v323
```

---
### N_0x4737980e8a283806

`0x4737980E8A283806` · hash `0x4737980E8A283806` · **Cliente**

```lua
local retval, p1 = N_0x4737980e8a283806(p0, p1)
```
```c
BOOL 0x4737980E8A283806(int p0, Any* p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x487912fd248efddf

`0x487912FD248EFDDF` · hash `0x487912FD248EFDDF` · jhash `0x579B4510` · **Cliente**

```lua
local retval = N_0x487912fd248efddf(p0, p1)
```
```c
BOOL 0x487912FD248EFDDF(Any p0, float p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`float`)

**Devuelve:** `BOOL`

---
### N_0x4a7d6e727f941747

`0x4A7D6E727F941747` · hash `0x4A7D6E727F941747` · jhash `0x8E7AEEB7` · **Cliente**

```lua
local retval, p0 = N_0x4a7d6e727f941747(p0)
```
```c
Any 0x4A7D6E727F941747(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `Any`

---
### N_0x4ed9c8d6da297639

`0x4ED9C8D6DA297639` · hash `0x4ED9C8D6DA297639` · jhash `0xC5E08B66` · **Cliente**

```lua
local retval = N_0x4ed9c8d6da297639()
```
```c
Any 0x4ED9C8D6DA297639();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### N_0x50a8a36201dbf83e

`0x50A8A36201DBF83E` · hash `0x50A8A36201DBF83E` · jhash `0x8DA93C3D` · **Cliente**

```lua
local retval = N_0x50a8a36201dbf83e()
```
```c
BOOL 0x50A8A36201DBF83E();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Added Parameter 2: float* p1
NativeDB Introduced: v323
```

---
### N_0x675721c9f644d161

`0x675721C9F644D161` · hash `0x675721C9F644D161` · jhash `0x486867E6` · **Cliente**

```lua
N_0x675721c9f644d161()
```
```c
void 0x675721C9F644D161();
```

**Devuelve:** `void`

---
### N_0x699e4a5c8c893a18

`0x699E4A5C8C893A18` · hash `0x699E4A5C8C893A18` · jhash `0xCE7D50A8` · **Cliente**

```lua
local retval, p2 = N_0x699e4a5c8c893a18(p0, p1, p2)
```
```c
BOOL 0x699E4A5C8C893A18(int p0, char* p1, Any* p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`char*`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x6bfb12ce158e3dd4

`0x6BFB12CE158E3DD4` · hash `0x6BFB12CE158E3DD4` · jhash `0x24D84334` · **Cliente**

```lua
local retval = N_0x6bfb12ce158e3dd4(p0)
```
```c
BOOL 0x6BFB12CE158E3DD4(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0x710bcda8071eded1

`0x710BCDA8071EDED1` · hash `0x710BCDA8071EDED1` · jhash `0x04EE74A3` · **Cliente**

```lua
local retval = N_0x710bcda8071eded1()
```
```c
BOOL 0x710BCDA8071EDED1();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Added Parameter 2: int* p1
NativeDB Introduced: v323
```

---
### N_0x7db18ca8cad5b098

`0x7DB18CA8CAD5B098` · hash `0x7DB18CA8CAD5B098` · **Cliente**

```lua
local retval = N_0x7db18ca8cad5b098()
```
```c
Any 0x7DB18CA8CAD5B098();
```

**Devuelve:** `Any`

---
### N_0x7ffcbfee44ecfabf

`0x7FFCBFEE44ECFABF` · hash `0x7FFCBFEE44ECFABF` · **Cliente**

```lua
local retval = N_0x7ffcbfee44ecfabf()
```
```c
Any 0x7FFCBFEE44ECFABF();
```

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

---
### N_0x8a4416c0db05fa66

`0x8A4416C0DB05FA66` · hash `0x8A4416C0DB05FA66` · **Cliente**

```lua
local retval, newsStoryData = N_0x8a4416c0db05fa66(newsStoryData)
```
```c
BOOL 0x8A4416C0DB05FA66(Any* newsStoryData);
```

**Parámetros**

- `newsStoryData` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0x8cc469ab4d349b7c

`0x8CC469AB4D349B7C` · hash `0x8CC469AB4D349B7C` · jhash `0xE778B2A7` · **Cliente**

```lua
local retval, p2 = N_0x8cc469ab4d349b7c(p0, p1, p2)
```
```c
BOOL 0x8CC469AB4D349B7C(int p0, char* p1, Any* p2);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`char*`)
- `p2` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x9237e334f6e43156

`0x9237E334F6E43156` · hash `0x9237E334F6E43156` · jhash `0x65D84665` · **Cliente**

```lua
local retval = N_0x9237e334f6e43156(p0)
```
```c
Any 0x9237E334F6E43156(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

---
### N_0x92da6e70ef249bd1

`0x92DA6E70EF249BD1` · hash `0x92DA6E70EF249BD1` · jhash `0xAED95A6F` · **Cliente**

```lua
local retval, p1 = N_0x92da6e70ef249bd1(p0, p1)
```
```c
BOOL 0x92DA6E70EF249BD1(char* p0, int* p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x9de5d2f723575ed0

`0x9DE5D2F723575ED0` · hash `0x9DE5D2F723575ED0` · jhash `0x37DD48B5` · **Cliente**

```lua
local retval = N_0x9de5d2f723575ed0()
```
```c
BOOL 0x9DE5D2F723575ED0();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Added Parameter 2: char* p1
NativeDB Introduced: v323
```

---
### N_0xa468e0be12b12c70

`0xA468E0BE12B12C70` · hash `0xA468E0BE12B12C70` · jhash `0xB21288FA` · **Cliente**

```lua
local retval = N_0xa468e0be12b12c70()
```
```c
BOOL 0xA468E0BE12B12C70();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
NativeDB Introduced: v323
```

---
### N_0xc2c97ea97711d1ae

`0xC2C97EA97711D1AE` · hash `0xC2C97EA97711D1AE` · jhash `0xF929F61D` · **Cliente**

```lua
local retval = N_0xc2c97ea97711d1ae()
```
```c
BOOL 0xC2C97EA97711D1AE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Introduced: v323
```

---
### N_0xc5a35c73b68f3c49

`0xC5A35C73B68F3C49` · hash `0xC5A35C73B68F3C49` · jhash `0x7E24BD6E` · **Cliente**

```lua
local retval = N_0xc5a35c73b68f3c49()
```
```c
BOOL 0xC5A35C73B68F3C49();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: int p0
NativeDB Added Parameter 2: char* p1
NativeDB Added Parameter 3: float* p2
NativeDB Introduced: v323
```

---
### N_0xd8122c407663b995

`0xD8122C407663B995` · hash `0xD8122C407663B995` · jhash `0x1C65B038` · **Cliente**

```lua
local retval = N_0xd8122c407663b995()
```
```c
Any 0xD8122C407663B995();
```

**Devuelve:** `Any`

---
### N_0xe4f6e8d07a2f0f51

`0xE4F6E8D07A2F0F51` · hash `0xE4F6E8D07A2F0F51` · **Cliente**

```lua
local retval = N_0xe4f6e8d07a2f0f51(p0)
```
```c
Any 0xE4F6E8D07A2F0F51(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `Any`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xe75a4a2e5e316d86

`0xE75A4A2E5E316D86` · hash `0xE75A4A2E5E316D86` · jhash `0x28C57FA0` · **Cliente**

```lua
local retval = N_0xe75a4a2e5e316d86()
```
```c
BOOL 0xE75A4A2E5E316D86();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Added Parameter 1: char* p0
NativeDB Added Parameter 2: int* p1
NativeDB Added Parameter 3: char* p2
NativeDB Introduced: v323
```

---
### N_0xea95c0853a27888e

`0xEA95C0853A27888E` · hash `0xEA95C0853A27888E` · **Cliente**

```lua
N_0xea95c0853a27888e()
```
```c
void 0xEA95C0853A27888E();
```

**Devuelve:** `void`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
### N_0xf22ca0fd74b80e7a

`0xF22CA0FD74B80E7A` · hash `0xF22CA0FD74B80E7A` · jhash `0xF379DCE4` · **Cliente**

```lua
local retval = N_0xf22ca0fd74b80e7a(p0)
```
```c
BOOL 0xF22CA0FD74B80E7A(Any p0);
```

**Parámetros**

- `p0` (`Any`)

**Devuelve:** `BOOL`

---
### N_0xf6baaaf762e1bf40

`0xF6BAAAF762E1BF40` · hash `0xF6BAAAF762E1BF40` · jhash `0x7AA36406` · **Cliente**

```lua
local retval, p1 = N_0xf6baaaf762e1bf40(p0, p1)
```
```c
BOOL 0xF6BAAAF762E1BF40(char* p0, int* p1);
```

**Parámetros**

- `p0` (`char*`)
- `p1` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0xfe4c1d0d3b9cc17e

`0xFE4C1D0D3B9CC17E` · hash `0xFE4C1D0D3B9CC17E` · jhash `0x8A023024` · **Cliente**

```lua
local retval = N_0xfe4c1d0d3b9cc17e(p0, p1)
```
```c
BOOL 0xFE4C1D0D3B9CC17E(Any p0, BOOL p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`BOOL`)

**Devuelve:** `BOOL`

---
### N_0xff8f3a92b75ed67a

`0xFF8F3A92B75ED67A` · hash `0xFF8F3A92B75ED67A` · jhash `0xC96456BA` · **Cliente**

```lua
local retval = N_0xff8f3a92b75ed67a()
```
```c
Any 0xFF8F3A92B75ED67A();
```

**Devuelve:** `Any`

---
### RockstarMessageGetString

`_ROCKSTAR_MESSAGE_GET_STRING` · hash `0xDF649C4E9AFDD788` · jhash `0x468668F0` · **Cliente**

```lua
local retval = RockstarMessageGetString()
```
```c
char* _ROCKSTAR_MESSAGE_GET_STRING();
```

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xDF649C4E9AFDD788` (`N_0xdf649c4e9afdd788`)

---
### ScEmailMessageClearRecipList

`SC_EMAIL_MESSAGE_CLEAR_RECIP_LIST` · hash `0x55DF6DB45179236E` · jhash `0xD094F11A` · **Cliente**

```lua
ScEmailMessageClearRecipList()
```
```c
void SC_EMAIL_MESSAGE_CLEAR_RECIP_LIST();
```

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x55DF6DB45179236E` (`N_0x55df6db45179236e`)

---
### ScEmailMessagePushGamerToRecipList

`SC_EMAIL_MESSAGE_PUSH_GAMER_TO_RECIP_LIST` · hash `0x2330C12A7A605D16` · jhash `0x9A703A2B` · **Cliente**

```lua
local networkHandle = ScEmailMessagePushGamerToRecipList(networkHandle)
```
```c
void SC_EMAIL_MESSAGE_PUSH_GAMER_TO_RECIP_LIST(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

---
### ScGamerdataGetBool

`SC_GAMERDATA_GET_BOOL` · hash `0x8416FE4E4629D7D7` · jhash `0xDF45B2A7` · **Cliente**

```lua
local retval = ScGamerdataGetBool(name)
```
```c
BOOL SC_GAMERDATA_GET_BOOL(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
sfink: from scripts:
func_720(socialclub::_0x8416FE4E4629D7D7("bIgnoreCheaterOverride"));
func_719(socialclub::_0x8416FE4E4629D7D7("bIgnoreBadSportOverride"));
```

**Nombres antiguos (alias):** `0x8416FE4E4629D7D7` (`N_0x8416fe4e4629d7d7`), `_SC_GET_IS_PROFILE_ATTRIBUTE_SET` (`ScGetIsProfileAttributeSet`)

---
### ScGamerdataGetFloat

`SC_GAMERDATA_GET_FLOAT` · hash `0xA770C8EEC6FB2AC5` · jhash `0x515AF67C` · **Cliente**

```lua
local retval, outValue = ScGamerdataGetFloat(name, outValue)
```
```c
BOOL SC_GAMERDATA_GET_FLOAT(char* name, float* outValue);
```

**Parámetros**

- `name` (`char*`)
- `outValue` (`float*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `_0xA770C8EEC6FB2AC5` (`N_0xa770c8eec6fb2ac5`)

---
### ScGamerdataGetInt

`SC_GAMERDATA_GET_INT` · hash `0xC85A7127E7AD02AA` · jhash `0xF8BDA989` · **Cliente**

```lua
local retval, outValue = ScGamerdataGetInt(name, outValue)
```
```c
BOOL SC_GAMERDATA_GET_INT(char* name, int* outValue);
```

**Parámetros**

- `name` (`char*`)
- `outValue` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v323
```

**Nombres antiguos (alias):** `_0xC85A7127E7AD02AA` (`N_0xc85a7127e7ad02aa`)

---
### ScGetHasAchievementBeenPassed

`_SC_GET_HAS_ACHIEVEMENT_BEEN_PASSED` · hash `0x418DC16FAE452C1C` · **Cliente**

```lua
local retval = ScGetHasAchievementBeenPassed(achievement)
```
```c
BOOL _SC_GET_HAS_ACHIEVEMENT_BEEN_PASSED(int achievement);
```

**Parámetros**

- `achievement` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Same as HAS_ACHIEVEMENT_BEEN_PASSED
```

**Nombres antiguos (alias):** `0x418DC16FAE452C1C` (`N_0x418dc16fae452c1c`)

---
### ScGetNickname

`_SC_GET_NICKNAME` · hash `0x198D161F458ECC7F` · **Cliente**

```lua
local retval = ScGetNickname()
```
```c
char* _SC_GET_NICKNAME();
```

**Devuelve:** `char*`

**Descripción oficial:**

```
Returns the nickname of the logged-in Rockstar Social Club account.
```

---
### ScInboxGetEmails

`_SC_INBOX_GET_EMAILS` · hash `0x040ADDCBAFA1018A` · **Cliente**

```lua
ScInboxGetEmails(offset, limit)
```
```c
void _SC_INBOX_GET_EMAILS(int offset, int limit);
```

**Parámetros**

- `offset` (`int`)
- `limit` (`int`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0x040ADDCBAFA1018A` (`N_0x040addcbafa1018a`)

---
### ScInboxGetMessageIsReadAtIndex

`SC_INBOX_GET_MESSAGE_IS_READ_AT_INDEX` · hash `0x93028F1DB42BFD08` · jhash `0xD1ED1D48` · **Cliente**

```lua
local retval = ScInboxGetMessageIsReadAtIndex(msgIndex)
```
```c
BOOL SC_INBOX_GET_MESSAGE_IS_READ_AT_INDEX(int msgIndex);
```

**Parámetros**

- `msgIndex` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x93028F1DB42BFD08` (`N_0x93028f1db42bfd08`), `_IS_SC_INBOX_VALID` (`IsScInboxValid`)

---
### ScInboxGetMessageTypeAtIndex

`SC_INBOX_GET_MESSAGE_TYPE_AT_INDEX` · hash `0xBB8EA16ECBC976C4` · jhash `0x5ECF955D` · **Cliente**

```lua
local retval = ScInboxGetMessageTypeAtIndex(msgIndex)
```
```c
Hash SC_INBOX_GET_MESSAGE_TYPE_AT_INDEX(int msgIndex);
```

**Parámetros**

- `msgIndex` (`int`)

**Devuelve:** `Hash`

**Nombres antiguos (alias):** `0xBB8EA16ECBC976C4` (`N_0xbb8ea16ecbc976c4`), `_SC_INBOX_MESSAGE_INIT` (`ScInboxMessageInit`)

---
### ScInboxGetTotalNumMessages

`SC_INBOX_GET_TOTAL_NUM_MESSAGES` · hash `0x03A93FF1A2CA0864` · jhash `0x6BE5DF29` · **Cliente**

```lua
local retval = ScInboxGetTotalNumMessages()
```
```c
int SC_INBOX_GET_TOTAL_NUM_MESSAGES();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x03A93FF1A2CA0864` (`N_0x03a93ff1a2ca0864`), `_GET_TOTAL_SC_INBOX_IDS` (`GetTotalScInboxIds`)

---
### ScInboxMessageDoApply

`SC_INBOX_MESSAGE_DO_APPLY` · hash `0x9A2C8064B6C1E41A` · jhash `0xEBE420A4` · **Cliente**

```lua
local retval = ScInboxMessageDoApply(p0)
```
```c
BOOL SC_INBOX_MESSAGE_DO_APPLY(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9A2C8064B6C1E41A` (`N_0x9a2c8064b6c1e41a`), `_SC_INBOX_MESSAGE_PUSH` (`ScInboxMessagePush`)

---
### ScInboxMessageGetBountyData

`_SC_INBOX_MESSAGE_GET_BOUNTY_DATA` · hash `0x87E0052F08BD64E6` · jhash `0xAB3346B5` · **Cliente**

```lua
local retval, outData = ScInboxMessageGetBountyData(index, outData)
```
```c
BOOL _SC_INBOX_MESSAGE_GET_BOUNTY_DATA(int index, int* outData);
```

**Parámetros**

- `index` (`int`)
- `outData` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x87E0052F08BD64E6` (`N_0x87e0052f08bd64e6`)

---
### ScInboxMessageGetDataBool

`_SC_INBOX_MESSAGE_GET_DATA_BOOL` · hash `0xFFE5C16F402D851D` · **Cliente**

```lua
local retval = ScInboxMessageGetDataBool(p0, p1)
```
```c
BOOL _SC_INBOX_MESSAGE_GET_DATA_BOOL(int p0, char* p1);
```

**Parámetros**

- `p0` (`int`)
- `p1` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xFFE5C16F402D851D` (`N_0xffe5c16f402d851d`)

---
### ScInboxMessageGetDataInt

`SC_INBOX_MESSAGE_GET_DATA_INT` · hash `0xA00EFE4082C4056E` · jhash `0x88068C7C` · **Cliente**

```lua
local retval, out = ScInboxMessageGetDataInt(p0, context, out)
```
```c
BOOL SC_INBOX_MESSAGE_GET_DATA_INT(int p0, char* context, int* out);
```

**Parámetros**

- `p0` (`int`)
- `context` (`char*`)
- `out` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### ScInboxMessageGetDataString

`SC_INBOX_MESSAGE_GET_DATA_STRING` · hash `0x7572EF42FC6A9B6D` · jhash `0x15607620` · **Cliente**

```lua
local retval = ScInboxMessageGetDataString(p0, context, out)
```
```c
BOOL SC_INBOX_MESSAGE_GET_DATA_STRING(int p0, char* context, char* out);
```

**Parámetros**

- `p0` (`int`)
- `context` (`char*`)
- `out` (`char*`)

**Devuelve:** `BOOL`

---
### ScInboxMessageGetString

`_SC_INBOX_MESSAGE_GET_STRING` · hash `0xF3E31D16CBDCB304` · jhash `0x2C959AF9` · **Cliente**

```lua
local retval = ScInboxMessageGetString(p0)
```
```c
char* _SC_INBOX_MESSAGE_GET_STRING(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `char*`

**Nombres antiguos (alias):** `0xF3E31D16CBDCB304` (`N_0xf3e31d16cbdcb304`)

---
### ScInboxMessageGetUgcdata

`SC_INBOX_MESSAGE_GET_UGCDATA` · hash `0x69D82604A1A5A254` · jhash `0x88CA3BFC` · **Cliente**

```lua
local retval, p1 = ScInboxMessageGetUgcdata(p0, p1)
```
```c
BOOL SC_INBOX_MESSAGE_GET_UGCDATA(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### ScInboxMessagePop

`_SC_INBOX_MESSAGE_POP` · hash `0x2C015348CF19CA1D` · jhash `0x19EE0CCB` · **Cliente**

```lua
local retval = ScInboxMessagePop(p0)
```
```c
BOOL _SC_INBOX_MESSAGE_POP(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2C015348CF19CA1D` (`N_0x2c015348cf19ca1d`)

---
### ScInboxMessagePushGamerToEventRecipList

`_SC_INBOX_MESSAGE_PUSH_GAMER_TO_EVENT_RECIP_LIST` · hash `0xDA024BDBD600F44A` · jhash `0x0B9A3512` · **Cliente**

```lua
local networkHandle = ScInboxMessagePushGamerToEventRecipList(networkHandle)
```
```c
void _SC_INBOX_MESSAGE_PUSH_GAMER_TO_EVENT_RECIP_LIST(int* networkHandle);
```

**Parámetros**

- `networkHandle` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xDA024BDBD600F44A` (`N_0xda024bdbd600f44a`)

---
### ScInboxMessageSendBountyPresenceEvent

`_SC_INBOX_MESSAGE_SEND_BOUNTY_PRESENCE_EVENT` · hash `0x6AFD2CD753FEEF83` · jhash `0x628F489B` · **Cliente**

```lua
local retval = ScInboxMessageSendBountyPresenceEvent(data)
```
```c
BOOL _SC_INBOX_MESSAGE_SEND_BOUNTY_PRESENCE_EVENT(char* data);
```

**Parámetros**

- `data` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x6AFD2CD753FEEF83` (`N_0x6afd2cd753feef83`)

---
### ScInboxMessageSendUgcStatUpdateEvent

`_SC_INBOX_MESSAGE_SEND_UGC_STAT_UPDATE_EVENT` · hash `0xA68D3D229F4F3B06` · jhash `0x75324674` · **Cliente**

```lua
ScInboxMessageSendUgcStatUpdateEvent(data)
```
```c
void _SC_INBOX_MESSAGE_SEND_UGC_STAT_UPDATE_EVENT(char* data);
```

**Parámetros**

- `data` (`char*`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xA68D3D229F4F3B06` (`N_0xa68d3d229f4f3b06`)

---
### ScLicenseplateAdd

`SC_LICENSEPLATE_ADD` · hash `0x1989C6E6F67E76A8` · jhash `0xEEDE7FAB` · **Cliente**

```lua
local retval, tokenOut = ScLicenseplateAdd(plateText, plateData, tokenOut)
```
```c
BOOL SC_LICENSEPLATE_ADD(char* plateText, char* plateData, int* tokenOut);
```

**Parámetros**

- `plateText` (`char*`)
- `plateData` (`char*`)
- `tokenOut` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Social Club native to add license plate for the user

**Nombres antiguos (alias):** `0x1989C6E6F67E76A8` (`N_0x1989c6e6f67e76a8`)

---
### ScLicenseplateGetAddIsPending

`SC_LICENSEPLATE_GET_ADD_IS_PENDING` · hash `0x07C61676E5BB52CD` · jhash `0xE190E45A` · **Cliente**

```lua
local retval = ScLicenseplateGetAddIsPending(token)
```
```c
BOOL SC_LICENSEPLATE_GET_ADD_IS_PENDING(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Returns true if the add license plate text request is still pending.

**Nombres antiguos (alias):** `0x07C61676E5BB52CD` (`N_0x07c61676e5bb52cd`)

---
### ScLicenseplateGetAddStatus

`SC_LICENSEPLATE_GET_ADD_STATUS` · hash `0x8147FFF6A718E1AD` · jhash `0x930B3AE5` · **Cliente**

```lua
local retval = ScLicenseplateGetAddStatus(token)
```
```c
int SC_LICENSEPLATE_GET_ADD_STATUS(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

Returns a status for adding the license plate

**Nombres antiguos (alias):** `0x8147FFF6A718E1AD` (`N_0x8147fff6a718e1ad`)

---
### ScLicenseplateGetCount

`SC_LICENSEPLATE_GET_COUNT` · hash `0x700569DBA175A77C` · jhash `0x159FE39C` · **Cliente**

```lua
local retval = ScLicenseplateGetCount(token)
```
```c
int SC_LICENSEPLATE_GET_COUNT(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

Gets number of plates in the response of the get license plates request.
Range: \[0, count) can be used as second argument to \_0x1D4446A62D35B0D0 and \_0x2E89990DDFF670C3

**Nombres antiguos (alias):** `0x700569DBA175A77C` (`N_0x700569dba175a77c`)

---
### ScLicenseplateGetIsvalidIsPending

`SC_LICENSEPLATE_GET_ISVALID_IS_PENDING` · hash `0xD302E99EDF0449CF` · jhash `0x86DAE6D6` · **Cliente**

```lua
local retval = ScLicenseplateGetIsvalidIsPending(token)
```
```c
BOOL SC_LICENSEPLATE_GET_ISVALID_IS_PENDING(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Checks if the "is valid license plate" request is still pending.

**Nombres antiguos (alias):** `0xD302E99EDF0449CF` (`N_0xd302e99edf0449cf`)

---
### ScLicenseplateGetIsvalidStatus

`SC_LICENSEPLATE_GET_ISVALID_STATUS` · hash `0x5C4EBFFA98BDB41C` · jhash `0x9AA2BA3F` · **Cliente**

```lua
local retval = ScLicenseplateGetIsvalidStatus(token)
```
```c
int SC_LICENSEPLATE_GET_ISVALID_STATUS(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

Gets the status of the is valid license plate request

**Nombres antiguos (alias):** `0x5C4EBFFA98BDB41C` (`N_0x5c4ebffa98bdb41c`)

---
### ScLicenseplateGetPlate

`SC_LICENSEPLATE_GET_PLATE` · hash `0x1D4446A62D35B0D0` · jhash `0x4CE9BAA7` · **Cliente**

```lua
local retval = ScLicenseplateGetPlate(token, plateIndex)
```
```c
char* SC_LICENSEPLATE_GET_PLATE(int token, int plateIndex);
```

**Parámetros**

- `token` (`int`)
- `plateIndex` (`int`): The plate index from the list of result plates. Use SC_LICENSEPLATE_GET_COUNT for the number of plates.

**Devuelve:** `char*`

**Descripción oficial:**

Gets license plate text related to the get license plate info request

---
### ScLicenseplateGetPlateData

`SC_LICENSEPLATE_GET_PLATE_DATA` · hash `0x2E89990DDFF670C3` · jhash `0x05303FC8` · **Cliente**

```lua
local retval = ScLicenseplateGetPlateData(token, plateIndex)
```
```c
char* SC_LICENSEPLATE_GET_PLATE_DATA(int token, int plateIndex);
```

**Parámetros**

- `token` (`int`)
- `plateIndex` (`int`): The plate index from the list of result plates. Use SC_LICENSEPLATE_GET_COUNT for the number of plates.

**Devuelve:** `char*`

**Descripción oficial:**

Gets license plate data related to the get license plate info request

**Nombres antiguos (alias):** `0x2E89990DDFF670C3` (`N_0x2e89990ddff670c3`)

---
### ScLicenseplateIsvalid

`SC_LICENSEPLATE_ISVALID` · hash `0x0F73393BAC7E6730` · jhash `0x5298F472` · **Cliente**

```lua
local retval, tokenOut = ScLicenseplateIsvalid(plateText, tokenOut)
```
```c
BOOL SC_LICENSEPLATE_ISVALID(char* plateText, int* tokenOut);
```

**Parámetros**

- `plateText` (`char*`)
- `tokenOut` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

SC native to start a request for if license plate text is valid

**Nombres antiguos (alias):** `_0x0F73393BAC7E6730` (`N_0x0f73393bac7e6730`)

---
### ScLicenseplateSetPlateData

`SC_LICENSEPLATE_SET_PLATE_DATA` · hash `0xD0EE05FE193646EA` · jhash `0x9F98FA5C` · **Cliente**

```lua
local retval = ScLicenseplateSetPlateData(oldPlateText, newPlateText, plateData)
```
```c
BOOL SC_LICENSEPLATE_SET_PLATE_DATA(char* oldPlateText, char* newPlateText, char* plateData);
```

**Parámetros**

- `oldPlateText` (`char*`)
- `newPlateText` (`char*`)
- `plateData` (`char*`)

**Devuelve:** `BOOL`

**Descripción oficial:**

Changes the license plate for the user (no insert).

**Nombres antiguos (alias):** `0xD0EE05FE193646EA` (`N_0xd0ee05fe193646ea`)

---
### ScPresenceAttrSetFloat

`SC_PRESENCE_ATTR_SET_FLOAT` · hash `0xC4C4575F62534A24` · jhash `0x94BF0D35` · **Cliente**

```lua
local retval = ScPresenceAttrSetFloat()
```
```c
BOOL SC_PRESENCE_ATTR_SET_FLOAT();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v323
NativeDB Added Parameter 1: Hash attrHash
NativeDB Added Parameter 2: float value
```

**Nombres antiguos (alias):** `0xC4C4575F62534A24` (`N_0xc4c4575f62534a24`)

---
### ScPresenceAttrSetInt

`SC_PRESENCE_ATTR_SET_INT` · hash `0x1F1E9682483697C7` · jhash `0x90C74343` · **Cliente**

```lua
local retval = ScPresenceAttrSetInt(attrHash, value)
```
```c
BOOL SC_PRESENCE_ATTR_SET_INT(Hash attrHash, int value);
```

**Parámetros**

- `attrHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1F1E9682483697C7` (`N_0x1f1e9682483697c7`)

---
### ScPresenceAttrSetString

`SC_PRESENCE_ATTR_SET_STRING` · hash `0x287F1F75D2803595` · jhash `0x3ACE6D6B` · **Cliente**

```lua
local retval = ScPresenceAttrSetString(attrHash, value)
```
```c
BOOL SC_PRESENCE_ATTR_SET_STRING(Hash attrHash, char* value);
```

**Parámetros**

- `attrHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x287F1F75D2803595` (`N_0x287f1f75d2803595`)

---
### ScProfanityCheckString

`SC_PROFANITY_CHECK_STRING` · hash `0x75632C5ECD7ED843` · jhash `0xDF084A6B` · **Cliente**

```lua
local retval, token = ScProfanityCheckString(string, token)
```
```c
BOOL SC_PROFANITY_CHECK_STRING(char* string, int* token);
```

**Parámetros**

- `string` (`char*`)
- `token` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Descripción oficial:**

Starts a task to check an entered string for profanity on the ROS/Social Club services.

See also: [`SC_PROFANITY_GET_CHECK_IS_VALID`](#scprofanitygetcheckisvalid) and [`SC_PROFANITY_GET_CHECK_IS_PENDING`](#scprofanitygetcheckispending).

**Nombres antiguos (alias):** `0x75632C5ECD7ED843` (`N_0x75632c5ecd7ed843`), `_SC_START_CHECK_STRING_TASK` (`ScStartCheckStringTask`)

---
### ScProfanityCheckUgcString

`_SC_PROFANITY_CHECK_UGC_STRING` · hash `0xEB2BF817463DFA28` · **Cliente**

```lua
local retval, token = ScProfanityCheckUgcString(string, token)
```
```c
BOOL _SC_PROFANITY_CHECK_UGC_STRING(char* string, int* token);
```

**Parámetros**

- `string` (`char*`)
- `token` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xEB2BF817463DFA28` (`N_0xeb2bf817463dfa28`)

---
### ScProfanityGetCheckIsPending

`SC_PROFANITY_GET_CHECK_IS_PENDING` · hash `0x82E4A58BABC15AE7` · jhash `0xA796D7A7` · **Cliente**

```lua
local retval = ScProfanityGetCheckIsPending(token)
```
```c
BOOL SC_PROFANITY_GET_CHECK_IS_PENDING(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x82E4A58BABC15AE7` (`N_0x82e4a58babc15ae7`), `_SC_GET_CHECK_STRING_STATUS` (`ScGetCheckStringStatus`)

---
### ScProfanityGetCheckIsValid

`SC_PROFANITY_GET_CHECK_IS_VALID` · hash `0x1753344C770358AE` · jhash `0xFFED3676` · **Cliente**

```lua
local retval = ScProfanityGetCheckIsValid(token)
```
```c
BOOL SC_PROFANITY_GET_CHECK_IS_VALID(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x1753344C770358AE` (`N_0x1753344c770358ae`), `_SC_HAS_CHECK_STRING_TASK_COMPLETED` (`ScHasCheckStringTaskCompleted`)

---
### ScProfanityGetStringPassed

`SC_PROFANITY_GET_STRING_PASSED` · hash `0x85535ACF97FC0969` · jhash `0x09497F31` · **Cliente**

```lua
local retval = ScProfanityGetStringPassed(token)
```
```c
BOOL SC_PROFANITY_GET_STRING_PASSED(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x85535ACF97FC0969` (`N_0x85535acf97fc0969`)

---
### ScProfanityGetStringStatus

`SC_PROFANITY_GET_STRING_STATUS` · hash `0x930DE22F07B1CCE3` · jhash `0x4D8A6521` · **Cliente**

```lua
local retval = ScProfanityGetStringStatus(token)
```
```c
int SC_PROFANITY_GET_STRING_STATUS(int token);
```

**Parámetros**

- `token` (`int`)

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x930DE22F07B1CCE3` (`N_0x930de22f07b1cce3`)

---
### SetHandleRockstarMessageViaScript

`_SET_HANDLE_ROCKSTAR_MESSAGE_VIA_SCRIPT` · hash `0xBFA0A56A817C6C7D` · jhash `0x2FB9F53C` · **Cliente**

```lua
SetHandleRockstarMessageViaScript(toggle)
```
```c
void _SET_HANDLE_ROCKSTAR_MESSAGE_VIA_SCRIPT(BOOL toggle);
```

**Parámetros**

- `toggle` (`BOOL`)

**Devuelve:** `void`

**Nombres antiguos (alias):** `0xBFA0A56A817C6C7D` (`N_0xbfa0a56a817c6c7d`)

---
