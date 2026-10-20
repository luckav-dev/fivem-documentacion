> Fuente original: https://github.com/qbcore-framework/qb-docs/blob/930c12ec4f60dfbba60253571f1a58980129516d/qbcore-resources/qb-menu.md · repositorio qbcore-framework/qb-docs @ 930c12e · copiado el 2026-10-20

# ↖️ qb-menu

*I like buttons*

## Introduction

The **QB Menu** system is a Lua-based interactive menu integrated with a web-based user interface

> **Consejo:** Menu icons can be found on the [Font Awesome](https://fontawesome.com/) website

### Features

* Dynamic menu creation
* Support for icons and images
* Menu sorting functionality
* Client-server communication
* Easy-to-use Lua and JavaScript interfaces
* Exports and events for extensive integration

## openMenu

Opens the menu with provided data

* data: `table`&#x20;
  * header: `string` (optional)
  * txt: `string` (optional)
  * icon: `string` (optional)
  * isMenuHeader: `boolean` (optional)
  * disabled: `boolean` (optional)
  * hidden: `boolean` (optional)
  * action: `function`(optional)
  * params: `table` (optional)
    * event: `string`
    * args: `any` (optional)
    * isServer: `boolean` (optional)
    * isCommand: `boolean` (optional)
    * isQBCommand: `boolean` (optional)
    * isAction: `boolean` (optional)
* sort: `boolean`
* skipFirst: `boolean`

```lua
exports['qb-menu']:openMenu({
    { 
        header = "First Item", 
        icon = "icon-name", 
        txt = "Description",
        isMenuHeader = false,
        disabled = false,
        hidden = false,
        params = {
            event = "event:name",
            args = { arg1 = "value1" },
            isServer = false,
            isCommand = false,
            isQBCommand = false,
            isAction = false
        }
    },
    { 
        header = "Second Item", 
        txt = "Another description",
        isMenuHeader = false,
        disabled = true,
        hidden = false
    },
    {
        header = "Third Item", 
        txt = "Another description",
        action = function()
           print('You selected the Third Item')
        end
    }
       
}, true, false)
```

## closeMenu

Closes the menu

```lua
exports['qb-menu']:closeMenu()
```
