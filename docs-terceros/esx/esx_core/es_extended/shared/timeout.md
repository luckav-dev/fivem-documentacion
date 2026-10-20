> Fuente original: https://github.com/esx-framework/esx-legacy-documenation/blob/031b7f7543db595e3a6503e822107b7f60ce14ec/src/pages/en/esx_core/es_extended/shared/timeout.mdx · repositorio esx-framework/esx-legacy-documenation @ 031b7f7 · copiado el 2026-10-20

## Timeout

### SetTimeout
Sets a timeout for specified millisecond, after finishing the callback gets triggered.

**Arguments**
- msec: `number`
  - The amount of milliseconds to wait.
- cb: `function`
  - The callback to trigger after the timeout.

**Returns**
- timeoutId: `number`
  - The timeout id.

### ClearTimeout
Clears/Cancels the timeout. 

**Arguments**
- timeoutId: `number`
  - The timeout to clear.
