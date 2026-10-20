[← 25-hosting-y-despliegue](25-hosting-y-despliegue.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [27-tutorial-recurso-tienda →](27-tutorial-recurso-tienda.md)

# 26. Buenas prácticas de desarrollo

## 26.1 Nombres y organización

- **Nombres de recursos** en minúsculas, sin espacios: `mi_tienda`, `prefix_trabajo_basurero`. Usa un **prefijo** propio para tus recursos (`lx_`, `rp_`…).
- **Nombres de eventos** con espacio de nombres: `recurso:accion` o `recurso:server:accion` / `recurso:client:accion`.
- **Exports** en PascalCase o camelCase, pero **consistentes**.
- Separa `client/`, `server/`, `shared/`, `web/`, `locales/`, `sql/`.
- Un `config.lua` (compartido) para lo que el dueño del servidor quiere cambiar, y `server/config.lua` (solo servidor) para valores sensibles (precios autoritativos, webhooks).

## 26.2 Configuración

```lua
-- shared/config.lua
Config = {}
Config.Locale = GetConvar('ox:locale', 'es')
Config.Debug = false
Config.Blip = { sprite = 52, color = 2, scale = 0.8 }
```

```lua
-- server/config.lua (no visible para el cliente)
ServerConfig = {
    Webhook = GetConvar('mi_tienda_webhook', ''),
    Precios = { agua = 5, pan = 3 },
}
```

## 26.3 Locales (traducciones)

Con ox_lib: `locales/es.json`, `locales/en.json` + `lib.locale()` (ver 17.1). Sin librerías:

```lua
-- locales/es.lua
Locales = Locales or {}
Locales['es'] = { compra_ok = 'Has comprado %sx %s', sin_dinero = 'No tienes dinero suficiente' }

-- shared/locale.lua
function _L(key, ...)
    local str = (Locales[Config.Locale] or Locales['es'])[key] or key
    return select('#', ...) > 0 and str:format(...) or str
end
```

## 26.4 Versionado y comprobación de actualizaciones

- Usa **SemVer** (`1.2.3`) en `version` del manifest y etiquetas/releases en GitHub.
- `lib.versionCheck('usuario/repositorio')` (ox_lib) avisa en consola si hay una versión nueva.
- Mantén un `CHANGELOG.md` en tus recursos.

## 26.5 Lista de comprobación antes de publicar un recurso

- [ ] Funciona en un servidor limpio con solo sus dependencias.
- [ ] Sin errores en F8 ni en consola del servidor.
- [ ] `resmon` en reposo ≈ 0.00-0.02 ms.
- [ ] Todos los eventos de red validados en el servidor (tipos, rangos, permisos, distancia, *cooldown*).
- [ ] Sin secretos en archivos de cliente.
- [ ] Limpieza en `onResourceStop` (entidades, blips, NUI, foco).
- [ ] SQL incluido (`sql/install.sql`) e índices creados.
- [ ] README con instalación, dependencias, configuración y capturas.
- [ ] Licencia (si es *open source*: MIT, GPL-3.0, LGPL-3.0…).


---

[← 25-hosting-y-despliegue](25-hosting-y-despliegue.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [27-tutorial-recurso-tienda →](27-tutorial-recurso-tienda.md)
