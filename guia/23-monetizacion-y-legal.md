[← 22-cliente-fivem](22-cliente-fivem.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [24-txadmin →](24-txadmin.md)

# 23. Monetización, legalidad y Asset Escrow

> Esto **no es asesoramiento legal**. Lee siempre los documentos oficiales: el texto vinculante es el del PLA.

## 23.1 Creator Platform License Agreement (PLA)

- Documento: **https://fivem.net/terms** (redirige al PDF vigente, *"Last Updated: Sept. 10 2026"*). Hubo una actualización importante en vigor desde el **12 de enero de 2026**.
- Partes: **Rockstar Games** y **Take-Two**. Incorpora los Términos de Servicio y las Normas de la Comunidad de Rockstar.

**Obligaciones de un servidor:**

- Toda web/tienda del servidor debe identificar al **operador**, dar un **email de contacto** y mostrar el aviso: **"[NOMBRE DEL SERVIDOR] IS NOT APPROVED, SPONSORED, OR ENDORSED BY ROCKSTAR GAMES"**.
- **No** usar propiedad intelectual de Rockstar en el nombre o la marca del servidor (logos, "GTA", tipografías oficiales…).
- **No** usar música con licencia ni voces del juego alteradas.

**Monetización prohibida (§3.1):**

1. Retirada de dinero real (*cash-out*) o apuestas con dinero real.
2. Cajas de botín (*loot boxes*), *gacha*, sorteos.
3. **Vender moneda virtual del juego por dinero real.**
4. Vender objetos virtuales creados por Rockstar.
5. Servidores patrocinados por marcas o presentados como "oficiales".
6. Tiendas que agregan *assets* de terceros.
7. Publicidad o patrocinios de terceros.
8. Criptomonedas o NFTs.

Otros puntos: Rockstar puede exigir el uso de **servicios autorizados** (como Tebex) y prohibir proveedores no autorizados con 30 días de aviso; en el **Marketplace**, las compras únicas son irrevocables y las suscripciones terminan con la suscripción; prohibido usar los assets para entrenar IA.

## 23.2 Tebex

- **Tebex** es el **socio de monetización exclusivo** de Cfx.re. Las tiendas de servidor (VIP, prioridad de cola, cosméticos permitidos) y la venta de recursos van por Tebex.
- Configuración: crea la tienda en Tebex, vincúlala y pon la clave en `server.cfg`:

```cfg
set sv_tebexSecret "tu_clave_secreta_de_tebex"
```

- Tebex ejecuta **comandos** en tu servidor cuando alguien compra (por ejemplo `darvip {id}`); créalos con `RegisterCommand` restringido y valida los argumentos.
- Solo los **creadores acreditados por Tebex** pueden revender assets. Un servidor pillado con assets *leakeados* recibe una **suspensión de 2 semanas**; si reincide, **cierre permanente** (política de agosto de 2025).

## 23.3 Asset Escrow

**Asset Escrow** cifra recursos de pago para que solo funcionen en servidores autorizados.

- Admite **Lua** y modelos **YFT, YDD, YDR**. **La NUI no se cifra.** Tamaño máximo: 1 GB.
- El creador sube el recurso a **Portal** y lo vende **solo** a través de paquetes "FiveM Asset" de Tebex.
- El comprador lo descarga desde **Portal** (o desde Tebex) y funciona en los servidores cuya clave pertenece a su cuenta.
- Los assets **no se pueden transferir** entre cuentas. Los de suscripción se retiran al caducar.
- Portal guarda hasta **5 versiones** de cada asset con su *changelog* (desde mayo de 2026).
- El creador decide qué queda abierto con `escrow_ignore` en el manifest (normalmente `config.lua`, locales, `client/editable.lua`…).

```lua
escrow_ignore {
    'config.lua',
    'locales/*.lua',
    'client/editable.lua',
    'server/editable.lua',
}
```

## 23.4 Si vendes recursos (creadores)

1. Cuenta en Cfx.re + vinculación con Tebex como creador.
2. Prepara el recurso: deja configurables los archivos con `escrow_ignore`, documenta dependencias.
3. Súbelo en Portal → *Assets* → *Create*.
4. Crea el paquete en tu tienda Tebex de tipo **FiveM Asset** y asócialo.
5. Mantén versiones con *changelog* en Portal.


## Ver también (documentación offline)

- [Oficial: server-manual/asset-escrow](../docs-oficiales/server-manual/asset-escrow.md)
- [Oficial: server-manual/setting-up-a-tebex-store](../docs-oficiales/server-manual/setting-up-a-tebex-store.md)

---

[← 22-cliente-fivem](22-cliente-fivem.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [24-txadmin →](24-txadmin.md)
