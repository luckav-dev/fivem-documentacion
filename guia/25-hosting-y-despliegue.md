[← 24-txadmin](24-txadmin.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [26-buenas-practicas →](26-buenas-practicas.md)

# 25. Hosting, despliegue y operación

## 25.1 Opciones de hosting

| Tipo | Pros | Contras |
|---|---|---|
| **PC de casa** | Gratis, ideal para desarrollar | IP doméstica expuesta, sin protección DDoS, ancho de banda de subida limitado |
| **VPS** | Barato, control total | Rendimiento por núcleo variable; ojo con CPUs compartidas |
| **Servidor dedicado** | Máximo rendimiento y control | Más caro, administración propia |
| **Hosting específico de FiveM** (panel) | Fácil, txAdmin preinstalado | Menos control, a veces sobrevendido |

Al elegir: **CPU de alta frecuencia**, **NVMe**, **protección DDoS** con filtrado para juegos (UDP) y ubicación cercana a tus jugadores.

## 25.2 Flujo de trabajo recomendado

1. `server-data` en un **repositorio Git privado** (sin `secrets.cfg`, `cache/`, `txData/`).
2. Un **servidor de desarrollo** local o separado; nunca pruebes en producción.
3. Despliegue: `git pull` en el servidor + `ensure` del recurso cambiado (o reinicio programado).
4. **Backups** automáticos de BD y `server-data` fuera de la máquina.
5. **Changelog** para tu comunidad.

`.gitignore` sugerido:

```gitignore
cache/
txData/
secrets.cfg
*.log
node_modules/
db/
.DS_Store
Thumbs.db
```

## 25.3 Proxies y descargas a gran escala

Con un proxy (nginx) delante del servidor puedes ocultar la IP real, servir las descargas con caché y usar HTTPS con tu dominio:

```cfg
# server.cfg
set sv_forceIndirectListing true                     # la lista no anuncia la IP real
set sv_listingHostOverride "fivem.midominio.com"     # la lista consulta tu dominio/proxy
set sv_proxyIPRanges "100.64.1.1/32"                 # IP(s) del proxy (CIDR): pueden enviar X-Real-IP
set sv_endpoints "100.64.1.2:30120"                  # endpoint(s) UDP reales o proxies de UDP
fileserver_add ".*" "https://fivem.midominio.com/files"  # descargas de recursos a través del proxy
set adhesive_cdnKey "una_clave_secreta"              # ofuscación con clave global (necesaria para cachear)
```

```nginx
# nginx: proxy de conexión + caché de archivos
upstream backend {
    server 100.64.1.2:30120;
}

proxy_cache_path /srv/cache levels=1:2 keys_zone=assets:48m max_size=20g inactive=2h;

server {
    listen 443 ssl http2;
    server_name fivem.midominio.com;
    ssl_certificate     /etc/letsencrypt/live/fivem.midominio.com/fullchain.pem;
    ssl_certificate_key /etc/letsencrypt/live/fivem.midominio.com/privkey.pem;

    location / {
        proxy_pass http://backend;
        proxy_pass_request_headers on;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
    }

    location /files/ {
        proxy_pass http://backend$request_uri;
        proxy_cache assets;
        proxy_cache_valid 1y;
        proxy_cache_lock on;
        proxy_cache_revalidate on;
        add_header X-Cache-Status $upstream_cache_status;
    }
}
```

Comprueba que funciona abriendo en el navegador `https://fivem.midominio.com/info.json`, `/players.json` y `/dynamic.json`, y que `/client` responde *"/client is POST only"*.

> El UDP del juego **no** pasa por nginx HTTP: o lo expones directamente en `sv_endpoints` o usas un proxy UDP (nginx `stream`, o el de tu proveedor anti-DDoS).

> El antiguo proxy inverso `*.users.cfx.re` se cerró el **31 de marzo de 2026**: si dependías de él, configura tu propio dominio/proxy.

## 25.4 Mantenimiento periódico

- **Semanal**: revisar errores en consola, recursos con alto `resmon`, tamaño de la BD.
- **Mensual**: actualizar artefactos *recommended*, txAdmin, ox_lib/oxmysql/framework (leyendo *changelogs*), revisar bans y logs.
- **Siempre**: probar actualizaciones en desarrollo primero y tener un plan de vuelta atrás.


## Ver también (documentación offline)

- [Oficial: server-manual/proxy-setup](../docs-oficiales/server-manual/proxy-setup.md)
- [Oficial: server-manual/static-ips](../docs-oficiales/server-manual/static-ips.md)
- [Oficial: server-manual/game-server-hosting-providers](../docs-oficiales/server-manual/game-server-hosting-providers.md)
- [Oficial: cookbook/2019/10/29/optimizing-resource-downloads-using-a-caching-proxy](../docs-oficiales/cookbook/2019/10/29/optimizing-resource-downloads-using-a-caching-proxy.md)

---

[← 24-txadmin](24-txadmin.md) · [Índice de la guía](README.md) · [Inicio del repositorio](../README.md) · [26-buenas-practicas →](26-buenas-practicas.md)
