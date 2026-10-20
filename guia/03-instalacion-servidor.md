[← 02-conceptos-fundamentales](02-conceptos-fundamentales.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [04-server-cfg →](04-server-cfg.md)

# 3. Instalación y puesta en marcha del servidor

## 3.1 Requisitos

### Hardware orientativo

| Tamaño de servidor | CPU | RAM | Disco | Red |
|---|---|---|---|---|
| Desarrollo / pruebas (1-10 jugadores) | 2-4 núcleos modernos | 4-8 GB | SSD 30 GB | Doméstica |
| Pequeño (≤ 48 jugadores) | 4 núcleos con **alta frecuencia** (single-thread) | 8-16 GB | NVMe 60 GB | 100 Mbps-1 Gbps |
| Mediano (48-128) | 6-8 núcleos alta frecuencia | 16-32 GB | NVMe | 1 Gbps + anti-DDoS |
| Grande (128-2048) | CPU de gama alta (frecuencia > núcleos) | 32-64 GB | NVMe | 1-10 Gbps + anti-DDoS |

> FXServer es muy dependiente del **rendimiento por núcleo**. Una CPU con menos núcleos pero más GHz suele rendir mejor que una con muchos núcleos lentos. La base de datos (MariaDB) conviene tenerla en el mismo host o en la misma red local.

### Software

- **Windows**: Windows 10/11 o Windows Server 2016+ (x64). **Visual C++ Redistributable** (2015-2022 x64) instalado.
- **Linux**: cualquier distribución x64 moderna (Debian/Ubuntu recomendadas). El artefacto de Linux trae su propio *rootfs* Alpine, así que casi no necesita dependencias (`xz-utils` o `tar` para descomprimir).
- **Base de datos** (si usas framework): **MariaDB 11.4 LTS u 11.8 LTS** (recomendadas; la 10.6 llegó a fin de soporte en julio de 2026 y `ox_core` exige 11.4+). MySQL 8 funciona pero da más problemas (palabras reservadas, valores por defecto en JSON/LONGTEXT).
- **Git** (opcional pero recomendado) para versionar tu `server-data`.

## 3.2 Obtener una clave de servidor (*license key*)

1. Entra en **https://portal.cfx.re** e inicia sesión con tu cuenta Cfx.re (la del foro).
2. Ve a **Server Management → Registration Keys** (o similar) y pulsa **Generate key**.
3. Indica la **IP pública** del servidor y el tipo (Windows/Linux/hosting).
4. Copia la clave (`cfxk_xxxxxxxxxxxxxxxxxxxx_xxxxxx`).
5. En `server.cfg`: `sv_licenseKey "cfxk_..."`.

> Cada clave está ligada a una cuenta. No la compartas ni la subas a GitHub. Si se filtra, revócala en el portal.

### Metadatos del servidor en Portal (desde el 21 de octubre de 2026)

Portal pasa a ser el lugar donde se configuran los datos que aparecen en la lista de servidores:

- **Nombre**, **descripción**, hasta **5 tags**, **banner** (recomendado 2560×280) y **enlace de Discord**.
- Los servidores que no lo configuren mostrarán *"Missing server data (must be configured in Portal)"*.
- Límites aplicados desde febrero de 2026: `sv_projectName` 40 caracteres, `sv_hostname` 120 y `sv_projectDesc` 250. Los colores en el título ya no se muestran.

En Portal también tienes: tus **assets** comprados (Asset Escrow, con historial de hasta 5 versiones y changelogs), la subida de recursos si eres creador y la gestión de claves.

## 3.3 Descargar los artefactos (FXServer)

Los artefactos son las versiones compiladas del servidor. La página oficial de descarga es:

- **https://docs.fivem.net/docs/server-download/?platform=legacy** (elige `os=windows` o `os=linux`)

> Las antiguas URLs de índice `runtime.fivem.net/artifacts/fivem/build_server_windows/master/` y `.../build_proot_linux/master/` ahora **redirigen** a esa página. Los enlaces directos a cada archivo (`.../master/<build>-<hash>/server.7z` o `fx.tar.xz`) siguen funcionando.

Canales:

| Canal | Build (20 oct 2026) | Uso |
|---|---|---|
| **Recommended** | **35245** | El que debes usar en producción. Probado por Cfx.re. |
| **Latest** | 37579 | La más nueva del *pipeline*. Pruébala antes de ponerla en producción. |

Enlaces directos del *recommended* actual:

- Windows: `https://runtime.fivem.net/artifacts/fivem/build_server_windows/master/35245-6efb47dff473c0e2a12fb50b08d74c0eb24a50d5/server.7z`
- Linux: `https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/35245-6efb47dff473c0e2a12fb50b08d74c0eb24a50d5/fx.tar.xz`

### Política de soporte (EOS / EOL)

- Una build *recommended* tiene soporte hasta **6 semanas** después de la siguiente; una *latest*, hasta **2 semanas** después.
- En la lista de servidores, los artefactos sin soporte se marcan en gris (**EOS**, *End of Support*) o en rojo (**EOL**, *End of Life*).
- Los artefactos **con más de tres meses sin soporte** no se pueden unir desde la lista de servidores.
- **Desde el 15 de octubre de 2026 no se puede conectar a servidores con artefactos anteriores a 35245.** Con 35245 o superior, el cliente ejecuta siempre el ejecutable estable más reciente de GTA V y carga solo el contenido DLC de la build fijada en `sv_enforceGameBuild` (por eso `sv_replaceExeToSwitchBuilds` queda obsoleto).

> Consulta siempre la página de descarga y el foro antes de actualizar un servidor en producción.

## 3.4 Estructura de carpetas recomendada

Separa siempre **binarios** (artefactos) de **datos** (tu configuración y recursos):

```
FXServer/
├── server/                 ← Artefactos (se reemplazan al actualizar)
│   ├── FXServer.exe        (Windows)  /  run.sh + alpine/ (Linux)
│   ├── citizen/
│   └── components.json ...
└── server-data/            ← TU servidor (versionar con git)
    ├── server.cfg
    ├── resources/
    │   ├── [cfx-default]/  ← recursos base (chat, spawnmanager…)
    │   ├── [framework]/    ← es_extended / qb-core / qbx_core
    │   ├── [ox]/           ← ox_lib, oxmysql, ox_inventory, ox_target…
    │   ├── [scripts]/      ← tus scripts
    │   ├── [maps]/         ← MLOs, ymaps
    │   ├── [vehicles]/     ← vehículos add-on
    │   └── [clothing]/     ← ropa/EUP
    ├── cache/              ← generado automáticamente (no versionar)
    └── txData/             ← datos de txAdmin si se usa (no versionar)
```

## 3.5 Instalación en Windows (con txAdmin, recomendado)

1. Crea `C:\FXServer\server` y `C:\FXServer\server-data`.
2. Descarga el `server.7z` del canal **recommended** y descomprímelo (7-Zip) en `C:\FXServer\server`.
3. Ejecuta `FXServer.exe` **sin** argumentos +exec. Se iniciará **txAdmin** y te mostrará:
   - Una URL (`http://localhost:40120`) y un **PIN** de 4 dígitos.
4. Abre la URL, introduce el PIN y **vincula tu cuenta Cfx.re** (o crea una cuenta local).
5. Sigue el asistente:
   - **Server Name**.
   - **Deployment type**: *Popular Recipes* (ESX, QBCore, QBox, CFX Default…), *Existing Server Data* (si ya tienes `server-data`), *Remote URL Template*, *Custom Template*.
   - Introduce la **license key**.
   - txAdmin descargará los recursos, creará la base de datos (si la receta lo requiere) y generará `server.cfg`.
6. Pulsa **Start Server** en el panel.
7. Abre FiveM → F8 → `connect localhost:30120` (o `connect 127.0.0.1`).

## 3.6 Instalación en Windows (manual, sin txAdmin)

```bat
cd C:\FXServer
git clone https://github.com/citizenfx/cfx-server-data.git server-data
```

Crea `server-data\server.cfg` (ver [sección 4](04-server-cfg.md#4-servercfg-a-fondo)) y luego un `start.bat` en `server-data`:

```bat
@echo off
cd /d C:\FXServer\server-data
C:\FXServer\server\FXServer.exe +exec server.cfg
pause
```

> Si arrancas `FXServer.exe` con `+exec server.cfg`, txAdmin **no** se inicia. Para usar txAdmin arranca sin `+exec` y apunta txAdmin a tu `server-data`.

## 3.7 Instalación en Linux

```bash
# 1. Usuario dedicado (nunca ejecutes el servidor como root)
sudo adduser --disabled-login fivem
sudo -iu fivem

# 2. Artefactos
mkdir -p ~/FXServer/server && cd ~/FXServer/server
# Copia la URL del fx.tar.xz "recommended" desde la página de descarga (ejemplo: 35245)
wget https://runtime.fivem.net/artifacts/fivem/build_proot_linux/master/35245-6efb47dff473c0e2a12fb50b08d74c0eb24a50d5/fx.tar.xz
tar xf fx.tar.xz
rm fx.tar.xz

# 3. Datos del servidor
cd ~/FXServer
git clone https://github.com/citizenfx/cfx-server-data.git server-data

# 4. Arrancar (con txAdmin)
cd ~/FXServer/server
./run.sh

# 4b. Arrancar sin txAdmin
cd ~/FXServer/server-data
bash ~/FXServer/server/run.sh +exec server.cfg
```

### Mantenerlo en segundo plano

**Con `screen` / `tmux`:**

```bash
screen -S fivem
cd ~/FXServer/server && ./run.sh
# Ctrl+A, D para salir sin cerrarlo; screen -r fivem para volver
```

**Con `systemd`** (`/etc/systemd/system/fivem.service`):

```ini
[Unit]
Description=FiveM FXServer (txAdmin)
After=network.target mariadb.service

[Service]
Type=simple
User=fivem
WorkingDirectory=/home/fivem/FXServer/server
ExecStart=/bin/bash /home/fivem/FXServer/server/run.sh
Restart=on-failure
RestartSec=10
LimitNOFILE=65535

[Install]
WantedBy=multi-user.target
```

```bash
sudo systemctl daemon-reload
sudo systemctl enable --now fivem
journalctl -u fivem -f
```

## 3.8 Puertos y firewall

| Puerto | Protocolo | Uso |
|---|---|---|
| **30120** | **TCP + UDP** | Puerto del juego (conexión, HTTP de recursos, sincronización). Configurable con `endpoint_add_tcp/udp`. |
| **40120** | TCP | Panel web de txAdmin (no lo expongas si no hace falta; mejor tras VPN o con contraseña fuerte + 2FA). |
| 3306 | TCP | MariaDB/MySQL (**nunca** lo abras a Internet). |

**Windows (PowerShell como administrador):**

```powershell
New-NetFirewallRule -DisplayName "FiveM TCP" -Direction Inbound -Protocol TCP -LocalPort 30120 -Action Allow
New-NetFirewallRule -DisplayName "FiveM UDP" -Direction Inbound -Protocol UDP -LocalPort 30120 -Action Allow
```

**Linux (ufw):**

```bash
sudo ufw allow 30120/tcp
sudo ufw allow 30120/udp
sudo ufw allow from <TU_IP> to any port 40120 proto tcp   # txAdmin solo desde tu IP
```

En casa también tendrás que **redirigir los puertos** (port forwarding) en el router hacia la IP local del PC.

## 3.9 Conectarse al servidor

- **F8 (consola del cliente)**: `connect 127.0.0.1:30120` / `connect mi.dominio.com`
- **Enlace directo**: `fivem://connect/127.0.0.1:30120`
- **Código Cfx**: `cfx.re/join/xxxxxx` (aparece en la consola del servidor cuando está listado públicamente).
- **Lista de servidores** del cliente, buscando por nombre o tags.
- **Favoritos / historial** en el cliente.

## 3.10 Actualizar el servidor (artefactos)

1. **Para** el servidor (desde txAdmin o cerrando la consola).
2. **Copia de seguridad** de `server-data` (o al menos `server.cfg`, `resources/` y `txData/`) y de la base de datos.
3. Borra el contenido de la carpeta `server/` (binarios) — **no** `server-data` ni `txData`.
4. Descomprime el nuevo artefacto *recommended* en `server/`.
5. Arranca y revisa la consola en busca de errores.

> Nunca mezcles archivos de versiones distintas de artefactos en la misma carpeta. Mantén la carpeta antigua unos días por si necesitas volver atrás.

## 3.11 Recursos base de `cfx-server-data`

| Recurso | Para qué sirve | ¿Necesario? |
|---|---|---|
| `mapmanager` | Gestiona mapas y gamemodes. | Sí, si usas `spawnmanager` |
| `spawnmanager` | Lógica de aparición/reaparición (`exports.spawnmanager:spawnPlayer`). | Si no tienes framework con su propio spawn |
| `sessionmanager` | Gestión de sesión de host (legado). | Recomendado |
| `chat` | Chat por defecto y sugerencias de comandos. | Recomendado |
| `basic-gamemode` | Gamemode mínimo. | Opcional |
| `hardcap` | Limita jugadores al `sv_maxclients`. | Recomendado |
| `rconlog` | Comandos `status`, `clientkick` y log RCON. | Opcional |
| `baseevents` | Eventos `baseevents:onPlayerDied`, `onPlayerKilled`, `enteredVehicle`, `leftVehicle`… | Opcional |
| `fivem-map-skater` / `fivem-map-hipster` | Mapas de ejemplo con puntos de aparición. | Opcional |
| `webpack` / `yarn` | *Builders* para recursos JS que usan dependencias npm. | Si los necesitas |
| `runcode` | Ejecutar código desde consola (solo desarrollo). | **No en producción** |
| `money`, `money-fountain`, `ped-money-drops`, `player-data` | Ejemplos educativos. | No |


## Ver también (documentación offline)

- [Oficial: server-manual/setting-up-a-server-txadmin](../docs-oficiales/server-manual/setting-up-a-server-txadmin.md)
- [Oficial: server-manual/setting-up-a-server-vanilla](../docs-oficiales/server-manual/setting-up-a-server-vanilla.md)
- [Oficial: getting-started/setup-fivem-server](../docs-oficiales/getting-started/setup-fivem-server.md)
- [Oficial: server-manual/end-of-support-end-of-life](../docs-oficiales/server-manual/end-of-support-end-of-life.md)

---

[← 02-conceptos-fundamentales](02-conceptos-fundamentales.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [04-server-cfg →](04-server-cfg.md)
