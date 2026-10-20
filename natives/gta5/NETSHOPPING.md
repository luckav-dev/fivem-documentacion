# Natives de GTA V — NETSHOPPING

> Generado el 2026-10-20 desde la base de datos oficial de Cfx.re (`static.cfx.re/natives`). Las descripciones son las **oficiales, en inglés y sin modificar**. Las firmas Lua siguen las reglas del generador oficial de FiveM: ver [cómo leer esta referencia](../README.md#cómo-leer-cada-entrada).

Namespace `NETSHOPPING`: **42** natives.

[← Índice de natives](../README.md)

## Índice de esta página

[`N_0x0395cb47b022e62c`](#n_0x0395cb47b022e62c) · [`N_0x170910093218c8b9`](#n_0x170910093218c8b9) · [`N_0x357b152ef96c30b6`](#n_0x357b152ef96c30b6) · [`N_0x613f125ba3bd2eb9`](#n_0x613f125ba3bd2eb9) · [`N_0x72eb7ba9b69bf6ab`](#n_0x72eb7ba9b69bf6ab) · [`N_0x74a0fd0688f1ee45`](#n_0x74a0fd0688f1ee45) · [`N_0x79edac677ca62f81`](#n_0x79edac677ca62f81) · [`N_0x85f6c9aba1de2bcf`](#n_0x85f6c9aba1de2bcf) · [`N_0xc13c38e47ea5df31`](#n_0xc13c38e47ea5df31) · [`N_0xc830417d630a50f9`](#n_0xc830417d630a50f9) · [`N_0xe3e5a7c64ca2c6ed`](#n_0xe3e5a7c64ca2c6ed) · [`NetGameserverBasketAddItem`](#netgameserverbasketadditem) · [`NetGameserverBasketApplyServerData`](#netgameserverbasketapplyserverdata) · [`NetGameserverBasketDelete`](#netgameserverbasketdelete) · [`NetGameserverBasketEnd`](#netgameserverbasketend) · [`NetGameserverBasketIsFull`](#netgameserverbasketisfull) · [`NetGameserverBasketStart`](#netgameserverbasketstart) · [`NetGameserverBeginService`](#netgameserverbeginservice) · [`NetGameserverCatalogIsReady`](#netgameservercatalogisready) · [`NetGameserverCatalogItemExists`](#netgameservercatalogitemexists) · [`NetGameserverCatalogItemExistsHash`](#netgameservercatalogitemexistshash) · [`NetGameserverCheckoutStart`](#netgameservercheckoutstart) · [`NetGameserverDeleteCharacterSlot`](#netgameserverdeletecharacterslot) · [`NetGameserverDeleteCharacterSlotGetStatus`](#netgameserverdeletecharacterslotgetstatus) · [`NetGameserverDeleteSetTelemetryNonceSeed`](#netgameserverdeletesettelemetrynonceseed) · [`NetGameserverEndService`](#netgameserverendservice) · [`NetGameserverGetBalance`](#netgameservergetbalance) · [`NetGameserverGetCatalogState`](#netgameservergetcatalogstate) · [`NetGameserverGetPrice`](#netgameservergetprice) · [`NetGameserverGetTransactionManagerData`](#netgameservergettransactionmanagerdata) · [`NetGameserverIsCatalogValid`](#netgameserveriscatalogvalid) · [`NetGameserverIsSessionRefreshPending`](#netgameserverissessionrefreshpending) · [`NetGameserverIsSessionValid`](#netgameserverissessionvalid) · [`NetGameserverSessionApplyReceivedData`](#netgameserversessionapplyreceiveddata) · [`NetGameserverSetTelemetryNonceSeed`](#netgameserversettelemetrynonceseed) · [`NetGameserverStartSession`](#netgameserverstartsession) · [`NetGameserverTransferBankToWallet`](#netgameservertransferbanktowallet) · [`NetGameserverTransferCashGetStatus`](#netgameservertransfercashgetstatus) · [`NetGameserverTransferCashGetStatus_2`](#netgameservertransfercashgetstatus_2) · [`NetGameserverTransferCashSetTelemetryNonceSeed`](#netgameservertransfercashsettelemetrynonceseed) · [`NetGameserverTransferWalletToBank`](#netgameservertransferwallettobank) · [`NetGameserverUseServerTransactions`](#netgameserveruseservertransactions)

---
### N_0x0395cb47b022e62c

`0x0395CB47B022E62C` · hash `0x0395CB47B022E62C` · **Cliente**

```lua
local retval, p0 = N_0x0395cb47b022e62c(p0)
```
```c
BOOL 0x0395CB47B022E62C(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x170910093218c8b9

`0x170910093218C8B9` · hash `0x170910093218C8B9` · **Cliente**

```lua
local retval, p0 = N_0x170910093218c8b9(p0)
```
```c
BOOL 0x170910093218C8B9(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0x357b152ef96c30b6

`0x357B152EF96C30B6` · hash `0x357B152EF96C30B6` · **Cliente**

```lua
local retval = N_0x357b152ef96c30b6()
```
```c
Any 0x357B152EF96C30B6();
```

**Devuelve:** `Any`

---
### N_0x613f125ba3bd2eb9

`0x613F125BA3BD2EB9` · hash `0x613F125BA3BD2EB9` · **Cliente**

```lua
local retval = N_0x613f125ba3bd2eb9()
```
```c
BOOL 0x613F125BA3BD2EB9();
```

**Devuelve:** `BOOL`

---
### N_0x72eb7ba9b69bf6ab

`0x72EB7BA9B69BF6AB` · hash `0x72EB7BA9B69BF6AB` · **Cliente**

```lua
local retval = N_0x72eb7ba9b69bf6ab()
```
```c
BOOL 0x72EB7BA9B69BF6AB();
```

**Devuelve:** `BOOL`

---
### N_0x74a0fd0688f1ee45

`0x74A0FD0688F1EE45` · hash `0x74A0FD0688F1EE45` · **Cliente**

```lua
local retval = N_0x74a0fd0688f1ee45(p0)
```
```c
int 0x74A0FD0688F1EE45(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `int`

**Descripción oficial:**

```
NET_GAMESERVER_*
```

---
### N_0x79edac677ca62f81

`0x79EDAC677CA62F81` · hash `0x79EDAC677CA62F81` · **Cliente**

```lua
local retval = N_0x79edac677ca62f81(transactionId)
```
```c
BOOL 0x79EDAC677CA62F81(int transactionId);
```

**Parámetros**

- `transactionId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NET_GAMESERVER_*

Checks if the transaction status is equal to 3.

NativeDB Introduced: v1365
```

---
### N_0x85f6c9aba1de2bcf

`0x85F6C9ABA1DE2BCF` · hash `0x85F6C9ABA1DE2BCF` · **Cliente**

```lua
local retval = N_0x85f6c9aba1de2bcf()
```
```c
Any 0x85F6C9ABA1DE2BCF();
```

**Devuelve:** `Any`

---
### N_0xc13c38e47ea5df31

`0xC13C38E47EA5DF31` · hash `0xC13C38E47EA5DF31` · **Cliente**

```lua
local retval, p0 = N_0xc13c38e47ea5df31(p0)
```
```c
BOOL 0xC13C38E47EA5DF31(Any* p0);
```

**Parámetros**

- `p0` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

---
### N_0xc830417d630a50f9

`0xC830417D630A50F9` · hash `0xC830417D630A50F9` · **Cliente**

```lua
local retval = N_0xc830417d630a50f9(transactionId)
```
```c
BOOL 0xC830417D630A50F9(int transactionId);
```

**Parámetros**

- `transactionId` (`int`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NET_GAMESERVER_*

Checks if the transaction status is equal to 1.

NativeDB Introduced: v1365
```

---
### N_0xe3e5a7c64ca2c6ed

`0xE3E5A7C64CA2C6ED` · hash `0xE3E5A7C64CA2C6ED` · **Cliente**

```lua
local retval = N_0xe3e5a7c64ca2c6ed()
```
```c
Any 0xE3E5A7C64CA2C6ED();
```

**Devuelve:** `Any`

---
### NetGameserverBasketAddItem

`_NET_GAMESERVER_BASKET_ADD_ITEM` · hash `0xF30980718C8ED876` · **Cliente**

```lua
local retval, itemData = NetGameserverBasketAddItem(quantity)
```
```c
BOOL _NET_GAMESERVER_BASKET_ADD_ITEM(Any* itemData, int quantity);
```

**Parámetros**

- `itemData` (`Any*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `quantity` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xF30980718C8ED876` (`N_0xf30980718c8ed876`), `_NETWORK_SHOP_BASKET_ADD_ITEM` (`NetworkShopBasketAddItem`)

---
### NetGameserverBasketApplyServerData

`_NET_GAMESERVER_BASKET_APPLY_SERVER_DATA` · hash `0xE1A0450ED46A7812` · **Cliente**

```lua
local retval, p1 = NetGameserverBasketApplyServerData(p0, p1)
```
```c
BOOL _NET_GAMESERVER_BASKET_APPLY_SERVER_DATA(Any p0, Any* p1);
```

**Parámetros**

- `p0` (`Any`)
- `p1` (`Any*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE1A0450ED46A7812` (`N_0xe1a0450ed46a7812`), `_NETWORK_SHOP_BASKET_APPLY_SERVER_DATA` (`NetworkShopBasketApplyServerData`)

---
### NetGameserverBasketDelete

`_NET_GAMESERVER_BASKET_DELETE` · hash `0xFA336E7F40C0A0D0` · **Cliente**

```lua
local retval = NetGameserverBasketDelete()
```
```c
BOOL _NET_GAMESERVER_BASKET_DELETE();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v372
```

---
### NetGameserverBasketEnd

`_NET_GAMESERVER_BASKET_END` · hash `0xA65568121DF2EA26` · **Cliente**

```lua
local retval = NetGameserverBasketEnd()
```
```c
BOOL _NET_GAMESERVER_BASKET_END();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA65568121DF2EA26` (`N_0xa65568121df2ea26`), `0xE547E9114277098F` (`N_0xe547e9114277098f`), `_NETWORK_SHOP_BASKET_END` (`NetworkShopBasketEnd`)

---
### NetGameserverBasketIsFull

`_NET_GAMESERVER_BASKET_IS_FULL` · hash `0x27F76CC6C55AD30E` · **Cliente**

```lua
local retval = NetGameserverBasketIsFull()
```
```c
BOOL _NET_GAMESERVER_BASKET_IS_FULL();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x27F76CC6C55AD30E` (`N_0x27f76cc6c55ad30e`), `_NETWORK_SHOP_BASKET_IS_FULL` (`NetworkShopBasketIsFull`)

---
### NetGameserverBasketStart

`_NET_GAMESERVER_BASKET_START` · hash `0x279F08B1A4B29B7E` · **Cliente**

```lua
local retval, transactionId = NetGameserverBasketStart(categoryHash, actionHash, flags)
```
```c
BOOL _NET_GAMESERVER_BASKET_START(int* transactionId, Hash categoryHash, Hash actionHash, int flags);
```

**Parámetros**

- `transactionId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `categoryHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `actionHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `flags` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `_NETWORK_SHOP_BASKET_START` (`NetworkShopBasketStart`)

---
### NetGameserverBeginService

`_NET_GAMESERVER_BEGIN_SERVICE` · hash `0x3C5FD37B5499582E` · **Cliente**

```lua
local retval, transactionId = NetGameserverBeginService(categoryHash, itemHash, actionTypeHash, value, flags)
```
```c
BOOL _NET_GAMESERVER_BEGIN_SERVICE(int* transactionId, Hash categoryHash, Hash itemHash, Hash actionTypeHash, int value, int flags);
```

**Parámetros**

- `transactionId` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `categoryHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `itemHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `actionTypeHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `value` (`int`)
- `flags` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3C5FD37B5499582E` (`N_0x3c5fd37b5499582e`), `_NETWORK_SHOP_BEGIN_SERVICE` (`NetworkShopBeginService`)

---
### NetGameserverCatalogIsReady

`_NET_GAMESERVER_CATALOG_IS_READY` · hash `0x3C4487461E9B0DCB` · **Cliente**

```lua
local retval = NetGameserverCatalogIsReady()
```
```c
BOOL _NET_GAMESERVER_CATALOG_IS_READY();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x3C4487461E9B0DCB` (`N_0x3c4487461e9b0dcb`)

---
### NetGameserverCatalogItemExists

`_NET_GAMESERVER_CATALOG_ITEM_EXISTS` · hash `0xBD4D7EAF8A30F637` · **Cliente**

```lua
local retval = NetGameserverCatalogItemExists(name)
```
```c
BOOL _NET_GAMESERVER_CATALOG_ITEM_EXISTS(char* name);
```

**Parámetros**

- `name` (`char*`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xBD4D7EAF8A30F637` (`N_0xbd4d7eaf8a30f637`), `_NETWORK_SHOP_IS_ITEM_UNLOCKED` (`NetworkShopIsItemUnlocked`), `_NETWORK_SHOP_DOES_ITEM_EXIST` (`NetworkShopDoesItemExist`)

---
### NetGameserverCatalogItemExistsHash

`_NET_GAMESERVER_CATALOG_ITEM_EXISTS_HASH` · hash `0x247F0F73A182EA0B` · **Cliente**

```lua
local retval = NetGameserverCatalogItemExistsHash(hash)
```
```c
BOOL _NET_GAMESERVER_CATALOG_ITEM_EXISTS_HASH(Hash hash);
```

**Parámetros**

- `hash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x247F0F73A182EA0B` (`N_0x247f0f73a182ea0b`), `_NETWORK_SHOP_IS_ITEM_UNLOCKED_HASH` (`NetworkShopIsItemUnlockedHash`), `_NETWORK_SHOP_DOES_ITEM_EXIST_HASH` (`NetworkShopDoesItemExistHash`)

---
### NetGameserverCheckoutStart

`_NET_GAMESERVER_CHECKOUT_START` · hash `0x39BE7CEA8D9CC8E6` · **Cliente**

```lua
local retval = NetGameserverCheckoutStart(transactionId)
```
```c
BOOL _NET_GAMESERVER_CHECKOUT_START(int transactionId);
```

**Parámetros**

- `transactionId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x39BE7CEA8D9CC8E6` (`N_0x39be7cea8d9cc8e6`), `_NETWORK_SHOP_CHECKOUT_START` (`NetworkShopCheckoutStart`)

---
### NetGameserverDeleteCharacterSlot

`_NET_GAMESERVER_DELETE_CHARACTER_SLOT` · hash `0x51F1A8E48C3D2F6D` · **Cliente**

```lua
local retval = NetGameserverDeleteCharacterSlot(slot, transfer, reason)
```
```c
BOOL _NET_GAMESERVER_DELETE_CHARACTER_SLOT(int slot, BOOL transfer, Hash reason);
```

**Parámetros**

- `slot` (`int`)
- `transfer` (`BOOL`)
- `reason` (`Hash`) *(acepta un string: se convierte con GetHashKey)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x51F1A8E48C3D2F6D` (`N_0x51f1a8e48c3d2f6d`)

---
### NetGameserverDeleteCharacterSlotGetStatus

`_NET_GAMESERVER_DELETE_CHARACTER_SLOT_GET_STATUS` · hash `0x0A6D923DFFC9BD89` · **Cliente**

```lua
local retval = NetGameserverDeleteCharacterSlotGetStatus()
```
```c
int _NET_GAMESERVER_DELETE_CHARACTER_SLOT_GET_STATUS();
```

**Devuelve:** `int`

**Nombres antiguos (alias):** `0x0A6D923DFFC9BD89` (`N_0x0a6d923dffc9bd89`)

---
### NetGameserverDeleteSetTelemetryNonceSeed

`_NET_GAMESERVER_DELETE_SET_TELEMETRY_NONCE_SEED` · hash `0x112CEF1615A1139F` · **Cliente**

```lua
local retval = NetGameserverDeleteSetTelemetryNonceSeed()
```
```c
BOOL _NET_GAMESERVER_DELETE_SET_TELEMETRY_NONCE_SEED();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x112CEF1615A1139F` (`N_0x112cef1615a1139f`), `_NETWORK_SHOP_DELETE_SET_TELEMETRY_NONCE_SEED` (`NetworkShopDeleteSetTelemetryNonceSeed`)

---
### NetGameserverEndService

`_NET_GAMESERVER_END_SERVICE` · hash `0xE2A99A9B524BEFFF` · **Cliente**

```lua
local retval = NetGameserverEndService(transactionId)
```
```c
BOOL _NET_GAMESERVER_END_SERVICE(int transactionId);
```

**Parámetros**

- `transactionId` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xE2A99A9B524BEFFF` (`N_0xe2a99a9b524befff`), `_NETWORK_SHOP_END_SERVICE` (`NetworkShopEndService`), `_NETWORK_SHOP_TERMINATE_SERVICE` (`NetworkShopTerminateService`)

---
### NetGameserverGetBalance

`_NET_GAMESERVER_GET_BALANCE` · hash `0x35A1B3E1D1315CFA` · **Cliente**

```lua
local retval = NetGameserverGetBalance(inventory, playerbalance)
```
```c
BOOL _NET_GAMESERVER_GET_BALANCE(BOOL inventory, BOOL playerbalance);
```

**Parámetros**

- `inventory` (`BOOL`)
- `playerbalance` (`BOOL`)

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Note: only one of the arguments can be set to true at a time
```

**Nombres antiguos (alias):** `0x35A1B3E1D1315CFA` (`N_0x35a1b3e1d1315cfa`)

---
### NetGameserverGetCatalogState

`_NET_GAMESERVER_GET_CATALOG_STATE` · hash `0xCF38DAFBB49EDE5E` · **Cliente**

```lua
local retval, state = NetGameserverGetCatalogState(state)
```
```c
BOOL _NET_GAMESERVER_GET_CATALOG_STATE(int* state);
```

**Parámetros**

- `state` (`int*`) *(puntero: se devuelve como valor de retorno, argumento opcional)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xCF38DAFBB49EDE5E` (`N_0xcf38dafbb49ede5e`)

---
### NetGameserverGetPrice

`_NET_GAMESERVER_GET_PRICE` · hash `0xC27009422FCCA88D` · **Cliente**

```lua
local retval = NetGameserverGetPrice(itemHash, categoryHash, p2)
```
```c
int _NET_GAMESERVER_GET_PRICE(Hash itemHash, Hash categoryHash, BOOL p2);
```

**Parámetros**

- `itemHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `categoryHash` (`Hash`) *(acepta un string: se convierte con GetHashKey)*
- `p2` (`BOOL`)

**Devuelve:** `int`

**Descripción oficial:**

```
bool is always true in game scripts  
```

**Nombres antiguos (alias):** `_NETWORK_SHOP_GET_PRICE` (`NetworkShopGetPrice`)

---
### NetGameserverGetTransactionManagerData

`_NET_GAMESERVER_GET_TRANSACTION_MANAGER_DATA` · hash `0x897433D292B44130` · **Cliente**

```lua
local retval, p0, p1 = NetGameserverGetTransactionManagerData()
```
```c
BOOL _NET_GAMESERVER_GET_TRANSACTION_MANAGER_DATA(int* p0, BOOL* p1);
```

**Parámetros**

- `p0` (`int*`) *(puntero: se devuelve como valor de retorno, no se pasa)*
- `p1` (`BOOL*`) *(puntero: se devuelve como valor de retorno, no se pasa)*

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x897433D292B44130` (`N_0x897433d292b44130`)

---
### NetGameserverIsCatalogValid

`_NET_GAMESERVER_IS_CATALOG_VALID` · hash `0x2B949A1E6AEC8F6A` · **Cliente**

```lua
local retval = NetGameserverIsCatalogValid()
```
```c
BOOL _NET_GAMESERVER_IS_CATALOG_VALID();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2B949A1E6AEC8F6A` (`N_0x2b949a1e6aec8f6a`)

---
### NetGameserverIsSessionRefreshPending

`_NET_GAMESERVER_IS_SESSION_REFRESH_PENDING` · hash `0x810E8431C0614BF9` · **Cliente**

```lua
local retval = NetGameserverIsSessionRefreshPending()
```
```c
BOOL _NET_GAMESERVER_IS_SESSION_REFRESH_PENDING();
```

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x810E8431C0614BF9` (`N_0x810e8431c0614bf9`), `_NETWORK_SHOP_GET_TRANSACTIONS_DISABLED` (`NetworkShopGetTransactionsDisabled`)

---
### NetGameserverIsSessionValid

`_NET_GAMESERVER_IS_SESSION_VALID` · hash `0xB24F0944DA203D9E` · **Cliente**

```lua
local retval = NetGameserverIsSessionValid(charSlot)
```
```c
BOOL _NET_GAMESERVER_IS_SESSION_VALID(int charSlot);
```

**Parámetros**

- `charSlot` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xB24F0944DA203D9E` (`N_0xb24f0944da203d9e`), `_NETWORK_SHOP_GET_TRANSACTIONS_ENABLED_FOR_CHARACTER` (`NetworkShopGetTransactionsEnabledForCharacter`)

---
### NetGameserverSessionApplyReceivedData

`_NET_GAMESERVER_SESSION_APPLY_RECEIVED_DATA` · hash `0x2F41D51BA3BCD1F1` · **Cliente**

```lua
local retval = NetGameserverSessionApplyReceivedData(charSlot)
```
```c
BOOL _NET_GAMESERVER_SESSION_APPLY_RECEIVED_DATA(int charSlot);
```

**Parámetros**

- `charSlot` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x2F41D51BA3BCD1F1` (`N_0x2f41d51ba3bcd1f1`), `_NETWORK_SHOP_SESSION_APPLY_RECEIVED_DATA` (`NetworkShopSessionApplyReceivedData`)

---
### NetGameserverSetTelemetryNonceSeed

`_NET_GAMESERVER_SET_TELEMETRY_NONCE_SEED` · hash `0x9507D4271988E1AE` · **Cliente**

```lua
local retval = NetGameserverSetTelemetryNonceSeed(p0)
```
```c
BOOL _NET_GAMESERVER_SET_TELEMETRY_NONCE_SEED(int p0);
```

**Parámetros**

- `p0` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0x9507D4271988E1AE` (`N_0x9507d4271988e1ae`), `_NETWORK_SHOP_SET_TELEMETRY_NONCE_SEED` (`NetworkShopSetTelemetryNonceSeed`)

---
### NetGameserverStartSession

`_NET_GAMESERVER_START_SESSION` · hash `0xA135AC892A58FC07` · **Cliente**

```lua
local retval = NetGameserverStartSession(charSlot)
```
```c
BOOL _NET_GAMESERVER_START_SESSION(int charSlot);
```

**Parámetros**

- `charSlot` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xA135AC892A58FC07` (`N_0xa135ac892a58fc07`), `_NETWORK_SHOP_START_SESSION` (`NetworkShopStartSession`)

---
### NetGameserverTransferBankToWallet

`_NET_GAMESERVER_TRANSFER_BANK_TO_WALLET` · hash `0xD47A2C1BA117471D` · **Cliente**

```lua
local retval = NetGameserverTransferBankToWallet(charSlot, amount)
```
```c
BOOL _NET_GAMESERVER_TRANSFER_BANK_TO_WALLET(int charSlot, int amount);
```

**Parámetros**

- `charSlot` (`int`)
- `amount` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xD47A2C1BA117471D` (`N_0xd47a2c1ba117471d`), `_NETWORK_TRANSFER_BANK_TO_WALLET` (`NetworkTransferBankToWallet`)

---
### NetGameserverTransferCashGetStatus

`_NET_GAMESERVER_TRANSFER_CASH_GET_STATUS` · hash `0x23789E777D14CE44` · **Cliente**

```lua
local retval = NetGameserverTransferCashGetStatus()
```
```c
int _NET_GAMESERVER_TRANSFER_CASH_GET_STATUS();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Same as 0x350AA5EBC03D3BD2
```

**Nombres antiguos (alias):** `0x23789E777D14CE44` (`N_0x23789e777d14ce44`)

---
### NetGameserverTransferCashGetStatus_2

`_NET_GAMESERVER_TRANSFER_CASH_GET_STATUS_2` · hash `0x350AA5EBC03D3BD2` · **Cliente**

```lua
local retval = NetGameserverTransferCashGetStatus_2()
```
```c
int _NET_GAMESERVER_TRANSFER_CASH_GET_STATUS_2();
```

**Devuelve:** `int`

**Descripción oficial:**

```
Same as 0x23789E777D14CE44
```

**Nombres antiguos (alias):** `0x350AA5EBC03D3BD2` (`N_0x350aa5ebc03d3bd2`)

---
### NetGameserverTransferCashSetTelemetryNonceSeed

`_NET_GAMESERVER_TRANSFER_CASH_SET_TELEMETRY_NONCE_SEED` · hash `0x498C1E05CE5F7877` · **Cliente**

```lua
local retval = NetGameserverTransferCashSetTelemetryNonceSeed()
```
```c
BOOL _NET_GAMESERVER_TRANSFER_CASH_SET_TELEMETRY_NONCE_SEED();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
Used to be NETWORK_SHOP_CASH_TRANSFER_SET_TELEMETRY_NONCE_SEED
```

**Nombres antiguos (alias):** `0x498C1E05CE5F7877` (`N_0x498c1e05ce5f7877`), `_NETWORK_SHOP_CASH_TRANSFER_SET_TELEMETRY_NONCE_SEED` (`NetworkShopCashTransferSetTelemetryNonceSeed`)

---
### NetGameserverTransferWalletToBank

`_NET_GAMESERVER_TRANSFER_WALLET_TO_BANK` · hash `0xC2F7FE5309181C7D` · **Cliente**

```lua
local retval = NetGameserverTransferWalletToBank(charSlot, amount)
```
```c
BOOL _NET_GAMESERVER_TRANSFER_WALLET_TO_BANK(int charSlot, int amount);
```

**Parámetros**

- `charSlot` (`int`)
- `amount` (`int`)

**Devuelve:** `BOOL`

**Nombres antiguos (alias):** `0xC2F7FE5309181C7D` (`N_0xc2f7fe5309181c7d`), `_NETWORK_TRANSFER_WALLET_TO_BANK` (`NetworkTransferWalletToBank`)

---
### NetGameserverUseServerTransactions

`_NET_GAMESERVER_USE_SERVER_TRANSACTIONS` · hash `0x7D2708796355B20B` · **Cliente**

```lua
local retval = NetGameserverUseServerTransactions()
```
```c
BOOL _NET_GAMESERVER_USE_SERVER_TRANSACTIONS();
```

**Devuelve:** `BOOL`

**Descripción oficial:**

```
NativeDB Introduced: v1290
```

---
