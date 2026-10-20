[← 14-nui](14-nui.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [16-base-de-datos →](16-base-de-datos.md)

# 15. Streaming de assets (vehículos, mapas, ropa, armas…)

## 15.1 Carpeta `stream`

Todo archivo dentro de una carpeta llamada **`stream`** (o subcarpetas suyas) de un recurso se **transmite** a los clientes y el juego lo carga como si fuera parte del juego. No hace falta declararlo en el manifest.

| Extensión | Contenido |
|---|---|
| `.ytd` | Diccionario de texturas. |
| `.ydr` | Modelo (drawable) simple. |
| `.ydd` | Diccionario de drawables (ropa, cabezas). |
| `.yft` | Modelo fragmentable (vehículos, objetos rompibles). |
| `.ybn` | Colisiones (*bounds*). |
| `.ymap` | Colocación de entidades en el mapa. |
| `.ytyp` | Definición de arquetipos (props, MLOs). |
| `.ymf` | Manifest de mapa. |
| `.ycd` | Animaciones (clip dictionary). |
| `.ypt` | Efectos de partículas. |
| `.ynv` / `.ynd` | Navmesh / nodos de ruta. |
| `.awc` | Audio. |
| `.gfx` | Scaleform. |
| `.ymt` | Metadatos binarios (ropa, escenarios). |

Los archivos **`.meta`** (XML) **no** van en `stream`: se declaran con `data_file` (ver 15.6).

## 15.2 Reemplazo vs *add-on*

- **Reemplazo** (*replace*): el archivo tiene el **mismo nombre** que uno del juego (`adder.yft`) y lo sustituye.
- **Add-on**: añade un modelo **nuevo** con nombre propio (`micoche.yft`) más sus metas. Es lo recomendado: no rompe nada del juego base.

## 15.3 Vehículo add-on completo

```
mi_coche/
├── fxmanifest.lua
├── stream/
│   ├── micoche.yft
│   ├── micoche_hi.yft
│   ├── micoche.ytd
│   └── micoche+hi.ytd      (opcional)
└── data/
    ├── vehicles.meta
    ├── carvariations.meta
    ├── carcols.meta
    ├── handling.meta
    └── vehiclelayouts.meta (si lo trae)
```

```lua
fx_version 'cerulean'
game 'gta5'

files {
    'data/vehicles.meta',
    'data/carvariations.meta',
    'data/carcols.meta',
    'data/handling.meta',
    'data/vehiclelayouts.meta',
}

data_file 'HANDLING_FILE'          'data/handling.meta'
data_file 'VEHICLE_METADATA_FILE'  'data/vehicles.meta'
data_file 'CARCOLS_FILE'           'data/carcols.meta'
data_file 'VEHICLE_VARIATION_FILE' 'data/carvariations.meta'
data_file 'VEHICLE_LAYOUTS_FILE'   'data/vehiclelayouts.meta'
```

Nombre del vehículo en el juego (para que no salga "NULL"):

```lua
-- client.lua
CreateThread(function()
    AddTextEntry('MICOCHE', 'Mi Coche Deportivo')   -- gameName de vehicles.meta
end)
```

### Pack de varios vehículos

Puedes juntar muchos coches en un solo recurso con metas combinados o usando globs:

```lua
files { 'data/**/*.meta' }
data_file 'HANDLING_FILE'          'data/**/handling.meta'
data_file 'VEHICLE_METADATA_FILE'  'data/**/vehicles.meta'
data_file 'CARCOLS_FILE'           'data/**/carcols.meta'
data_file 'VEHICLE_VARIATION_FILE' 'data/**/carvariations.meta'
```

> Cuidado: demasiados vehículos/ropa de alta calidad aumentan la **memoria de texturas** y los tiempos de carga. Optimiza (ver 15.9).

## 15.4 Mapas: ymaps y MLOs

- Un **ymap** coloca objetos en el mundo. Basta con meterlo en `stream/`.
- Un **MLO** (*Milo*, interior) suele traer `.ymap` + `.ytyp` + `.ybn` + `.ydr` + `.ytd`.
- Si el MLO trae `.ytyp`, en muchos casos hay que declararlo:

```lua
fx_version 'cerulean'
game 'gta5'
this_is_a_map 'yes'

data_file 'DLC_ITYP_REQUEST' 'stream/mi_interior.ytyp'
```

- Para quitar edificios del mapa base hay que usar ymaps con *entity removal* (o recursos tipo "map fixes").
- Interiores del juego (IPL) se cargan con `RequestIpl` o con recursos como **bob74_ipl**.

## 15.5 Ropa add-on (EUP y similares)

- La ropa se basa en archivos `.ydd`/`.ytd` con nombres especiales (`mp_m_freemode_01_mp_m_mi_pack^jbib_000_u.ydd`) y un `.ymt` de metadatos de *ped* (`mp_m_freemode_01_mp_m_mi_pack.ymt`).
- Herramientas como **Durty Cloth Tool** o **Grzyb's/Clothing Tool** generan el recurso de *streaming* listo para FiveM.
- Las prendas add-on se suman **después** de las del juego, así que sus índices de *drawable* dependen del **game build**: cambiar de build puede desplazar los IDs.

## 15.6 `data_file`: tipos más usados

| Tipo | Archivo típico |
|---|---|
| `HANDLING_FILE` | `handling.meta` |
| `VEHICLE_METADATA_FILE` | `vehicles.meta` |
| `CARCOLS_FILE` | `carcols.meta` (modkits, sirenas, luces) |
| `VEHICLE_VARIATION_FILE` | `carvariations.meta` |
| `VEHICLE_LAYOUTS_FILE` | `vehiclelayouts.meta` |
| `CONTENT_UNLOCKING_META_FILE` | `contentunlocks.meta` |
| `PED_METADATA_FILE` | `peds.meta` |
| `SHOP_PED_APPAREL_META_FILE` | metas de ropa de tienda (`shop_*.meta`) |
| `PED_PERSONALITY_FILE` | `pedpersonality.meta` |
| `WEAPONINFO_FILE` | `weapons.meta` |
| `WEAPON_ANIMATIONS_FILE` | `weaponanimations.meta` |
| `WEAPON_METADATA_FILE` | `weaponarchetypes.meta` |
| `WEAPONCOMPONENTSINFO_FILE` | `weaponcomponents.meta` |
| `LOADOUTS_FILE` | `loadouts.meta` |
| `DLC_ITYP_REQUEST` | `*.ytyp` |
| `AUDIO_GAMEDATA` | `*_game.dat` |
| `AUDIO_SOUNDDATA` | `*_sounds.dat` |
| `AUDIO_SYNTHDATA` | `*_amp.dat` |
| `AUDIO_WAVEPACK` | carpeta con `.awc` |
| `TIMECYCLEMOD_FILE` | `timecycle_mods_*.xml` |
| `SCALEFORM_DLC_FILE` | `*.gfx` |
| `TEXTFILE_METAFILE` | textos (gxt2) |
| `TRAINCONFIGS_FILE` | `trains.xml` |
| `TRAINTRACK_FILE` | `traintracks.xml` |
| `INTERIOR_PROXY_ORDER_FILE` | `interiorproxies.meta` |

Lista completa y oficial: https://docs.fivem.net/docs/game-references/data-files/

## 15.7 Armas add-on

```lua
fx_version 'cerulean'
game 'gta5'

files {
    'meta/weaponarchetypes.meta',
    'meta/weaponanimations.meta',
    'meta/pedpersonality.meta',
    'meta/weapons.meta',
    'meta/weaponcomponents.meta',
}

data_file 'WEAPON_METADATA_FILE'      'meta/weaponarchetypes.meta'
data_file 'WEAPON_ANIMATIONS_FILE'    'meta/weaponanimations.meta'
data_file 'PED_PERSONALITY_FILE'      'meta/pedpersonality.meta'
data_file 'WEAPONCOMPONENTSINFO_FILE' 'meta/weaponcomponents.meta'
data_file 'WEAPONINFO_FILE'           'meta/weapons.meta'
```

## 15.8 Texturas en tiempo de ejecución (runtime TXD)

```lua
local txd = CreateRuntimeTxd('mis_logos')
CreateRuntimeTextureFromImage(txd, 'logo', 'img/logo.png')  -- archivo en 'files'
-- Usar: DrawSprite('mis_logos', 'logo', 0.5, 0.5, 0.1, 0.1, 0.0, 255, 255, 255, 255)
```

## 15.9 Optimización de assets

- **Tamaño de texturas**: evita `.ytd` de más de **16 MB** (FiveM avisa de *oversized assets* en consola) — reduce a 2K/1K, usa compresión DXT, genera *mipmaps*.
- **Polígonos**: vehículos de 500k+ polígonos destrozan el rendimiento; usa LODs (`_hi.yft` + versión baja).
- **Herramientas**: **CodeWalker** (mapas, ymaps), **OpenIV** (explorar y editar RPF), **Sollumz** (Blender: modelos, MLOs), **ZModeler3** (vehículos), **Texture Toolkit**/**Paint.NET + DDS**.
- Usa `strdbg` (F8) para ver qué se está transmitiendo y cuánto ocupa.
- Revisa los avisos de *"physical memory"* y *"virtual memory"* del recurso en `resmon`.

## 15.10 Assets de pago y escrow

- Los assets comprados en tiendas Tebex suelen venir **cifrados con Asset Escrow** y solo funcionan en los servidores cuya clave pertenece a la cuenta que los compró.
- Si un recurso con escrow da *"You lack the required entitlement"*, la clave del servidor no pertenece a la cuenta que tiene el recurso, la suscripción caducó o el recurso se ha renombrado.
- El escrow admite Lua y modelos (YFT, YDD, YDR); **la NUI no se cifra**.
- Más en la [sección 23](23-monetizacion-y-legal.md#23-monetización-legalidad-y-asset-escrow).


## Ver también (documentación offline)

- [Oficial: assets-manual](../docs-oficiales/assets-manual/README.md)
- [Oficial: game-references/data-files](../docs-oficiales/game-references/data-files.md)
- [Oficial: cookbook/2021/04/09/fyi-fivem-and-redm-support-raw-ymap-ytyp-files](../docs-oficiales/cookbook/2021/04/09/fyi-fivem-and-redm-support-raw-ymap-ytyp-files.md)
- [Oficial: cookbook/2021/04/13/using-modified-scenario-files-on-fivem](../docs-oficiales/cookbook/2021/04/13/using-modified-scenario-files-on-fivem.md)

---

[← 14-nui](14-nui.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [16-base-de-datos →](16-base-de-datos.md)
