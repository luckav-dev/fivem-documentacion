[← 28-chuleta](28-chuleta.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [30-glosario →](30-glosario.md)

# 29. Preguntas frecuentes (FAQ)

**¿Necesito `lua54 'yes'` en 2026?**
No. Desde julio de 2025 todo Lua es 5.4. La línea es inofensiva.

**¿Qué artefacto uso?**
El **recommended** (35245 a 20 de octubre de 2026). Nada por debajo de 35245 permite conexiones desde el 15 de octubre de 2026.

**¿Qué game build pongo?**
La última: `sv_enforceGameBuild 3889` (*The Kortz Center Heist*), salvo incompatibilidades.

**¿ESX, QBCore o Qbox?**
Para un servidor nuevo: **Qbox** (moderno, ox) o **ESX Legacy 1.16** (muy activo). QBCore se mueve poco. Ver 17.

**¿ox_lib de Overextended o de CommunityOx?**
De **Overextended** (`github.com/overextended`). CommunityOx está archivado desde abril de 2026.

**¿Puedo vender dinero del juego por dinero real?**
**No.** Está prohibido por el PLA (§3.1). Lo mismo con cajas de botín, apuestas, cripto/NFT y publicidad de terceros. Usa Tebex para lo que sí está permitido.

**¿Cómo pongo mi servidor privado?**
`sv_master1 ""` (desactiva el botón de conectar, no lo borra de la lista) o una allowlist (txAdmin o `playerConnecting`). Para desarrollo local: `sv_lan true`.

**Mi servidor no aparece en la lista.**
Revisa la clave (`sv_licenseKey`), los puertos 30120 TCP/UDP, que el artefacto tenga soporte y, desde el 21/10/2026, los metadatos del servidor en Portal.

**¿Por qué mi script consume tanto en `resmon`?**
Casi siempre un `Wait(0)` permanente o natives caros por frame. Ver 20.2.

**¿Cómo protejo mis eventos?**
Validando todo en el servidor (19.3). Los tokens no son protección real.

**¿Dónde están los logs del cliente?**
`%localappdata%\FiveM\FiveM.app\logs\`.

**¿Mis recursos C# con `mono_rt2` ya no cargan?**
La prueba de Mono v2 caducó el 30/06/2026. Quita `mono_rt2` y compila para el runtime clásico (`CitizenFX.Core`).

**Algunos jugadores tienen un `license:` nuevo.**
Es por la actualización de seguridad de cuentas del 24/06/2026. Pueden volver a elegir su identidad por defecto hasta el 24/06/2027; ten un proceso para migrar personajes.


---

[← 28-chuleta](28-chuleta.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [30-glosario →](30-glosario.md)
