# 📋 Reporte Smart Rebranding — Frigate → SecureVu
**Fecha:** 2026-03-18 19:01:18  
**Modo:** ✅ Aplicado  
**Módulo Python:** ✅ frigate/ → securevu/  
**Archivos modificados:** 1046  
**Reemplazos totales:** 8187  

---

## 🛡 Zonas Protegidas (no tocadas)

| Patrón | Razón |
|--------|-------|
| `FROM ghcr.io/blakeblackshear/frigate` | Imagen base Docker upstream |
| `ghcr.io/blakeblackshear/frigate` | Referencia a imagen upstream |
| `github.com/blakeblackshear/frigate.git` | Git URL upstream completo |
| `/media/frigate/` | Rutas de grabaciones en disco |
| `{FRIGATE_RTSP_*}` | Variables de autenticación RTSP/ONVIF |
| `{FRIGATE_MQTT_*}` | Variables de autenticación MQTT |
| `{FRIGATE_GENAI_*}` | Variables de API de IA |
| `ccab4aaf_frigate` | ID fijo del add-on de Home Assistant |

---

## 🔊 MQTT — Prefijo por Defecto

> El valor por defecto de `topic_prefix` **se mantiene en `frigate`**.
> Las instalaciones existentes que ya usan `frigate/` no requieren cambios.

---

## 📂 Archivos Modificados por Tipo

### `.conf` — 2 archivos · 14 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `docker/main/rootfs/usr/local/nginx/conf/nginx.conf` | 13 | — |
| `docker/main/rootfs/usr/local/nginx/conf/proxy_trusted_headers.conf` | 1 | — |

### `.html` — 2 archivos · 2 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `web/index.html` | 1 | — |
| `web/login.html` | 1 | — |

### `.ini` — 1 archivos · 15 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `securevu/mypy.ini` | 15 | — |

### `.json` — 563 archivos · 4056 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `.vscode/launch.json` | 2 | — |
| `cspell.json` | 3 | — |
| `web/public/locales/ar/components/dialog.json` | 2 | — |
| `web/public/locales/ar/components/player.json` | 2 | — |
| `web/public/locales/ar/views/classificationModel.json` | 1 | — |
| `web/public/locales/ar/views/configEditor.json` | 1 | — |
| `web/public/locales/ar/views/events.json` | 2 | — |
| `web/public/locales/ar/views/explore.json` | 1 | — |
| `web/public/locales/ar/views/faceLibrary.json` | 1 | — |
| `web/public/locales/ar/views/settings.json` | 4 | — |
| `web/public/locales/ar/views/system.json` | 7 | — |
| `web/public/locales/bg/common.json` | 1 | — |
| `web/public/locales/bg/components/auth.json` | 1 | — |
| `web/public/locales/bg/components/dialog.json` | 1 | — |
| `web/public/locales/bg/components/player.json` | 6 | — |
| `web/public/locales/bg/views/classificationModel.json` | 1 | — |
| `web/public/locales/bg/views/configEditor.json` | 2 | — |
| `web/public/locales/bg/views/exports.json` | 1 | — |
| `web/public/locales/bg/views/live.json` | 1 | — |
| `web/public/locales/bg/views/system.json` | 1 | — |
| `web/public/locales/ca/common.json` | 7 | — |
| `web/public/locales/ca/components/auth.json` | 1 | — |
| `web/public/locales/ca/components/dialog.json` | 5 | — |
| `web/public/locales/ca/components/filter.json` | 3 | — |
| `web/public/locales/ca/components/player.json` | 6 | — |
| `web/public/locales/ca/config/cameras.json` | 4 | — |
| `web/public/locales/ca/config/global.json` | 33 | — |
| `web/public/locales/ca/views/classificationModel.json` | 3 | — |
| `web/public/locales/ca/views/configEditor.json` | 2 | — |
| `web/public/locales/ca/views/events.json` | 2 | — |
| `web/public/locales/ca/views/explore.json` | 9 | — |
| `web/public/locales/ca/views/exports.json` | 1 | — |
| `web/public/locales/ca/views/faceLibrary.json` | 1 | — |
| `web/public/locales/ca/views/live.json` | 4 | — |
| `web/public/locales/ca/views/settings.json` | 80 | — |
| `web/public/locales/ca/views/system.json` | 16 | — |
| `web/public/locales/cs/common.json` | 6 | — |
| `web/public/locales/cs/components/auth.json` | 1 | — |
| `web/public/locales/cs/components/dialog.json` | 4 | — |
| `web/public/locales/cs/components/filter.json` | 3 | — |
| `web/public/locales/cs/components/player.json` | 6 | — |
| `web/public/locales/cs/views/classificationModel.json` | 2 | — |
| `web/public/locales/cs/views/configEditor.json` | 2 | — |
| `web/public/locales/cs/views/events.json` | 2 | — |
| `web/public/locales/cs/views/explore.json` | 9 | — |
| `web/public/locales/cs/views/exports.json` | 1 | — |
| `web/public/locales/cs/views/faceLibrary.json` | 1 | — |
| `web/public/locales/cs/views/live.json` | 2 | — |
| `web/public/locales/cs/views/settings.json` | 58 | — |
| `web/public/locales/cs/views/system.json` | 15 | — |
| `web/public/locales/da/common.json` | 7 | — |
| `web/public/locales/da/components/auth.json` | 1 | — |
| `web/public/locales/da/components/dialog.json` | 5 | — |
| `web/public/locales/da/components/player.json` | 6 | — |
| `web/public/locales/da/views/classificationModel.json` | 3 | — |
| `web/public/locales/da/views/configEditor.json` | 2 | — |
| `web/public/locales/da/views/events.json` | 2 | — |
| `web/public/locales/da/views/explore.json` | 2 | — |
| `web/public/locales/da/views/exports.json` | 1 | — |
| `web/public/locales/da/views/faceLibrary.json` | 1 | — |
| `web/public/locales/da/views/live.json` | 2 | — |
| `web/public/locales/da/views/settings.json` | 14 | — |
| `web/public/locales/da/views/system.json` | 14 | — |
| `web/public/locales/de/common.json` | 7 | — |
| `web/public/locales/de/components/auth.json` | 1 | — |
| `web/public/locales/de/components/dialog.json` | 7 | — |
| `web/public/locales/de/components/filter.json` | 3 | — |
| `web/public/locales/de/components/player.json` | 6 | — |
| `web/public/locales/de/config/cameras.json` | 1 | — |
| `web/public/locales/de/config/global.json` | 4 | — |
| `web/public/locales/de/views/classificationModel.json` | 3 | — |
| `web/public/locales/de/views/configEditor.json` | 2 | — |
| `web/public/locales/de/views/events.json` | 2 | — |
| `web/public/locales/de/views/explore.json` | 9 | — |
| `web/public/locales/de/views/exports.json` | 1 | — |
| `web/public/locales/de/views/faceLibrary.json` | 1 | — |
| `web/public/locales/de/views/live.json` | 3 | — |
| `web/public/locales/de/views/settings.json` | 68 | — |
| `web/public/locales/de/views/system.json` | 16 | — |
| `web/public/locales/el/common.json` | 4 | — |
| `web/public/locales/el/components/auth.json` | 1 | — |
| `web/public/locales/el/components/dialog.json` | 4 | — |
| `web/public/locales/el/components/player.json` | 6 | — |
| `web/public/locales/el/views/classificationModel.json` | 1 | — |
| `web/public/locales/el/views/configEditor.json` | 2 | — |
| `web/public/locales/el/views/events.json` | 2 | — |
| `web/public/locales/el/views/explore.json` | 2 | — |
| `web/public/locales/el/views/exports.json` | 1 | — |
| `web/public/locales/el/views/faceLibrary.json` | 1 | — |
| `web/public/locales/el/views/live.json` | 2 | — |
| `web/public/locales/el/views/settings.json` | 13 | — |
| `web/public/locales/el/views/system.json` | 9 | — |
| `web/public/locales/en/common.json` | 7 | — |
| `web/public/locales/en/components/auth.json` | 1 | — |
| `web/public/locales/en/components/dialog.json` | 5 | — |
| `web/public/locales/en/components/filter.json` | 3 | — |
| `web/public/locales/en/components/player.json` | 6 | — |
| `web/public/locales/en/config/cameras.json` | 5 | — |
| `web/public/locales/en/config/global.json` | 34 | — |
| `web/public/locales/en/views/chat.json` | 1 | — |
| `web/public/locales/en/views/classificationModel.json` | 3 | — |
| `web/public/locales/en/views/configEditor.json` | 2 | — |
| `web/public/locales/en/views/events.json` | 2 | — |
| `web/public/locales/en/views/explore.json` | 8 | — |
| `web/public/locales/en/views/exports.json` | 1 | — |
| `web/public/locales/en/views/faceLibrary.json` | 1 | — |
| `web/public/locales/en/views/live.json` | 4 | — |
| `web/public/locales/en/views/motionSearch.json` | 1 | — |
| `web/public/locales/en/views/replay.json` | 2 | — |
| `web/public/locales/en/views/settings.json` | 73 | — |
| `web/public/locales/en/views/system.json` | 16 | — |
| `web/public/locales/es/common.json` | 7 | — |
| `web/public/locales/es/components/auth.json` | 1 | — |
| `web/public/locales/es/components/dialog.json` | 7 | — |
| `web/public/locales/es/components/filter.json` | 3 | — |
| `web/public/locales/es/components/player.json` | 6 | — |
| `web/public/locales/es/config/cameras.json` | 1 | — |
| `web/public/locales/es/config/global.json` | 2 | — |
| `web/public/locales/es/views/classificationModel.json` | 3 | — |
| `web/public/locales/es/views/configEditor.json` | 2 | — |
| `web/public/locales/es/views/events.json` | 2 | — |
| `web/public/locales/es/views/explore.json` | 9 | — |
| `web/public/locales/es/views/exports.json` | 1 | — |
| `web/public/locales/es/views/faceLibrary.json` | 1 | — |
| `web/public/locales/es/views/live.json` | 4 | — |
| `web/public/locales/es/views/settings.json` | 70 | — |
| `web/public/locales/es/views/system.json` | 15 | — |
| `web/public/locales/et/common.json` | 7 | — |
| `web/public/locales/et/components/auth.json` | 1 | — |
| `web/public/locales/et/components/dialog.json` | 5 | — |
| `web/public/locales/et/components/player.json` | 6 | — |
| `web/public/locales/et/views/classificationModel.json` | 1 | — |
| `web/public/locales/et/views/configEditor.json` | 2 | — |
| `web/public/locales/et/views/events.json` | 2 | — |
| `web/public/locales/et/views/explore.json` | 1 | — |
| `web/public/locales/et/views/exports.json` | 1 | — |
| `web/public/locales/et/views/faceLibrary.json` | 1 | — |
| `web/public/locales/et/views/live.json` | 4 | — |
| `web/public/locales/et/views/settings.json` | 18 | — |
| `web/public/locales/et/views/system.json` | 3 | — |
| `web/public/locales/fa/common.json` | 6 | — |
| `web/public/locales/fa/components/dialog.json` | 3 | — |
| `web/public/locales/fa/components/filter.json` | 3 | — |
| `web/public/locales/fa/components/player.json` | 5 | — |
| `web/public/locales/fa/views/classificationModel.json` | 2 | — |
| `web/public/locales/fa/views/events.json` | 1 | — |
| `web/public/locales/fa/views/explore.json` | 7 | — |
| `web/public/locales/fa/views/faceLibrary.json` | 1 | — |
| `web/public/locales/fa/views/live.json` | 1 | — |
| `web/public/locales/fa/views/settings.json` | 44 | — |
| `web/public/locales/fa/views/system.json` | 7 | — |
| `web/public/locales/fi/common.json` | 5 | — |
| `web/public/locales/fi/components/dialog.json` | 3 | — |
| `web/public/locales/fi/components/filter.json` | 3 | — |
| `web/public/locales/fi/components/player.json` | 6 | — |
| `web/public/locales/fi/views/classificationModel.json` | 1 | — |
| `web/public/locales/fi/views/configEditor.json` | 2 | — |
| `web/public/locales/fi/views/events.json` | 2 | — |
| `web/public/locales/fi/views/explore.json` | 3 | — |
| `web/public/locales/fi/views/faceLibrary.json` | 1 | — |
| `web/public/locales/fi/views/live.json` | 2 | — |
| `web/public/locales/fi/views/settings.json` | 32 | — |
| `web/public/locales/fi/views/system.json` | 8 | — |
| `web/public/locales/fr/common.json` | 7 | — |
| `web/public/locales/fr/components/auth.json` | 1 | — |
| `web/public/locales/fr/components/dialog.json` | 7 | — |
| `web/public/locales/fr/components/filter.json` | 3 | — |
| `web/public/locales/fr/components/player.json` | 6 | — |
| `web/public/locales/fr/config/cameras.json` | 1 | — |
| `web/public/locales/fr/views/classificationModel.json` | 3 | — |
| `web/public/locales/fr/views/configEditor.json` | 2 | — |
| `web/public/locales/fr/views/events.json` | 2 | — |
| `web/public/locales/fr/views/explore.json` | 9 | — |
| `web/public/locales/fr/views/exports.json` | 1 | — |
| `web/public/locales/fr/views/faceLibrary.json` | 1 | — |
| `web/public/locales/fr/views/live.json` | 4 | — |
| `web/public/locales/fr/views/settings.json` | 70 | — |
| `web/public/locales/fr/views/system.json` | 15 | — |
| `web/public/locales/gl/common.json` | 1 | — |
| `web/public/locales/gl/components/dialog.json` | 4 | — |
| `web/public/locales/gl/components/player.json` | 2 | — |
| `web/public/locales/gl/views/configEditor.json` | 1 | — |
| `web/public/locales/gl/views/explore.json` | 1 | — |
| `web/public/locales/gl/views/exports.json` | 1 | — |
| `web/public/locales/gl/views/live.json` | 2 | — |
| `web/public/locales/gl/views/settings.json` | 7 | — |
| `web/public/locales/gl/views/system.json` | 7 | — |
| `web/public/locales/he/common.json` | 6 | — |
| `web/public/locales/he/components/dialog.json` | 5 | — |
| `web/public/locales/he/components/filter.json` | 3 | — |
| `web/public/locales/he/components/player.json` | 6 | — |
| `web/public/locales/he/views/classificationModel.json` | 3 | — |
| `web/public/locales/he/views/configEditor.json` | 2 | — |
| `web/public/locales/he/views/events.json` | 2 | — |
| `web/public/locales/he/views/explore.json` | 7 | — |
| `web/public/locales/he/views/exports.json` | 1 | — |
| `web/public/locales/he/views/faceLibrary.json` | 1 | — |
| `web/public/locales/he/views/live.json` | 3 | — |
| `web/public/locales/he/views/settings.json` | 57 | — |
| `web/public/locales/he/views/system.json` | 14 | — |
| `web/public/locales/hi/components/player.json` | 1 | — |
| `web/public/locales/hi/views/configEditor.json` | 1 | — |
| `web/public/locales/hr/common.json` | 7 | — |
| `web/public/locales/hr/components/auth.json` | 1 | — |
| `web/public/locales/hr/components/dialog.json` | 4 | — |
| `web/public/locales/hr/components/filter.json` | 3 | — |
| `web/public/locales/hr/components/player.json` | 6 | — |
| `web/public/locales/hr/views/classificationModel.json` | 3 | — |
| `web/public/locales/hr/views/configEditor.json` | 2 | — |
| `web/public/locales/hr/views/events.json` | 2 | — |
| `web/public/locales/hr/views/explore.json` | 8 | — |
| `web/public/locales/hr/views/exports.json` | 1 | — |
| `web/public/locales/hr/views/faceLibrary.json` | 1 | — |
| `web/public/locales/hr/views/live.json` | 4 | — |
| `web/public/locales/hr/views/settings.json` | 55 | — |
| `web/public/locales/hr/views/system.json` | 15 | — |
| `web/public/locales/hu/common.json` | 6 | — |
| `web/public/locales/hu/components/auth.json` | 1 | — |
| `web/public/locales/hu/components/dialog.json` | 5 | — |
| `web/public/locales/hu/components/filter.json` | 3 | — |
| `web/public/locales/hu/components/player.json` | 6 | — |
| `web/public/locales/hu/views/classificationModel.json` | 2 | — |
| `web/public/locales/hu/views/configEditor.json` | 2 | — |
| `web/public/locales/hu/views/events.json` | 2 | — |
| `web/public/locales/hu/views/explore.json` | 8 | — |
| `web/public/locales/hu/views/exports.json` | 1 | — |
| `web/public/locales/hu/views/faceLibrary.json` | 1 | — |
| `web/public/locales/hu/views/live.json` | 2 | — |
| `web/public/locales/hu/views/settings.json` | 59 | — |
| `web/public/locales/hu/views/system.json` | 14 | — |
| `web/public/locales/id/common.json` | 1 | — |
| `web/public/locales/id/components/auth.json` | 1 | — |
| `web/public/locales/id/components/dialog.json` | 5 | — |
| `web/public/locales/id/components/player.json` | 6 | — |
| `web/public/locales/id/views/classificationModel.json` | 2 | — |
| `web/public/locales/id/views/configEditor.json` | 2 | — |
| `web/public/locales/id/views/events.json` | 2 | — |
| `web/public/locales/id/views/explore.json` | 3 | — |
| `web/public/locales/id/views/exports.json` | 1 | — |
| `web/public/locales/id/views/faceLibrary.json` | 1 | — |
| `web/public/locales/id/views/live.json` | 2 | — |
| `web/public/locales/id/views/settings.json` | 17 | — |
| `web/public/locales/id/views/system.json` | 9 | — |
| `web/public/locales/it/common.json` | 7 | — |
| `web/public/locales/it/components/auth.json` | 1 | — |
| `web/public/locales/it/components/dialog.json` | 7 | — |
| `web/public/locales/it/components/filter.json` | 3 | — |
| `web/public/locales/it/components/player.json` | 6 | — |
| `web/public/locales/it/views/classificationModel.json` | 2 | — |
| `web/public/locales/it/views/configEditor.json` | 2 | — |
| `web/public/locales/it/views/events.json` | 2 | — |
| `web/public/locales/it/views/explore.json` | 9 | — |
| `web/public/locales/it/views/exports.json` | 1 | — |
| `web/public/locales/it/views/faceLibrary.json` | 1 | — |
| `web/public/locales/it/views/live.json` | 4 | — |
| `web/public/locales/it/views/settings.json` | 68 | — |
| `web/public/locales/it/views/system.json` | 15 | — |
| `web/public/locales/ja/common.json` | 7 | — |
| `web/public/locales/ja/components/auth.json` | 1 | — |
| `web/public/locales/ja/components/dialog.json` | 5 | — |
| `web/public/locales/ja/components/filter.json` | 3 | — |
| `web/public/locales/ja/components/player.json` | 6 | — |
| `web/public/locales/ja/views/classificationModel.json` | 3 | — |
| `web/public/locales/ja/views/configEditor.json` | 2 | — |
| `web/public/locales/ja/views/events.json` | 2 | — |
| `web/public/locales/ja/views/explore.json` | 7 | — |
| `web/public/locales/ja/views/exports.json` | 1 | — |
| `web/public/locales/ja/views/faceLibrary.json` | 1 | — |
| `web/public/locales/ja/views/live.json` | 4 | — |
| `web/public/locales/ja/views/settings.json` | 58 | — |
| `web/public/locales/ja/views/system.json` | 15 | — |
| `web/public/locales/ko/common.json` | 7 | — |
| `web/public/locales/ko/components/dialog.json` | 5 | — |
| `web/public/locales/ko/components/player.json` | 6 | — |
| `web/public/locales/ko/views/configEditor.json` | 2 | — |
| `web/public/locales/ko/views/events.json` | 2 | — |
| `web/public/locales/ko/views/explore.json` | 2 | — |
| `web/public/locales/ko/views/exports.json` | 1 | — |
| `web/public/locales/ko/views/faceLibrary.json` | 1 | — |
| `web/public/locales/ko/views/live.json` | 2 | — |
| `web/public/locales/ko/views/settings.json` | 16 | — |
| `web/public/locales/ko/views/system.json` | 14 | — |
| `web/public/locales/lt/common.json` | 7 | — |
| `web/public/locales/lt/components/auth.json` | 1 | — |
| `web/public/locales/lt/components/dialog.json` | 5 | — |
| `web/public/locales/lt/components/filter.json` | 3 | — |
| `web/public/locales/lt/components/player.json` | 6 | — |
| `web/public/locales/lt/views/classificationModel.json` | 3 | — |
| `web/public/locales/lt/views/configEditor.json` | 2 | — |
| `web/public/locales/lt/views/events.json` | 2 | — |
| `web/public/locales/lt/views/explore.json` | 9 | — |
| `web/public/locales/lt/views/exports.json` | 1 | — |
| `web/public/locales/lt/views/faceLibrary.json` | 1 | — |
| `web/public/locales/lt/views/live.json` | 4 | — |
| `web/public/locales/lt/views/settings.json` | 55 | — |
| `web/public/locales/lt/views/system.json` | 15 | — |
| `web/public/locales/lv/common.json` | 7 | — |
| `web/public/locales/lv/components/auth.json` | 1 | — |
| `web/public/locales/lv/components/dialog.json` | 3 | — |
| `web/public/locales/lv/components/player.json` | 6 | — |
| `web/public/locales/lv/views/configEditor.json` | 2 | — |
| `web/public/locales/lv/views/events.json` | 2 | — |
| `web/public/locales/lv/views/explore.json` | 3 | — |
| `web/public/locales/lv/views/exports.json` | 1 | — |
| `web/public/locales/lv/views/faceLibrary.json` | 1 | — |
| `web/public/locales/lv/views/live.json` | 2 | — |
| `web/public/locales/lv/views/settings.json` | 10 | — |
| `web/public/locales/lv/views/system.json` | 9 | — |
| `web/public/locales/nb-NO/common.json` | 7 | — |
| `web/public/locales/nb-NO/components/auth.json` | 1 | — |
| `web/public/locales/nb-NO/components/dialog.json` | 6 | — |
| `web/public/locales/nb-NO/components/filter.json` | 3 | — |
| `web/public/locales/nb-NO/components/player.json` | 6 | — |
| `web/public/locales/nb-NO/views/classificationModel.json` | 3 | — |
| `web/public/locales/nb-NO/views/configEditor.json` | 2 | — |
| `web/public/locales/nb-NO/views/events.json` | 2 | — |
| `web/public/locales/nb-NO/views/explore.json` | 9 | — |
| `web/public/locales/nb-NO/views/exports.json` | 1 | — |
| `web/public/locales/nb-NO/views/faceLibrary.json` | 1 | — |
| `web/public/locales/nb-NO/views/live.json` | 4 | — |
| `web/public/locales/nb-NO/views/settings.json` | 67 | — |
| `web/public/locales/nb-NO/views/system.json` | 14 | — |
| `web/public/locales/nl/common.json` | 7 | — |
| `web/public/locales/nl/components/auth.json` | 1 | — |
| `web/public/locales/nl/components/dialog.json` | 7 | — |
| `web/public/locales/nl/components/filter.json` | 3 | — |
| `web/public/locales/nl/components/player.json` | 6 | — |
| `web/public/locales/nl/config/cameras.json` | 1 | — |
| `web/public/locales/nl/views/classificationModel.json` | 3 | — |
| `web/public/locales/nl/views/configEditor.json` | 2 | — |
| `web/public/locales/nl/views/events.json` | 2 | — |
| `web/public/locales/nl/views/explore.json` | 9 | — |
| `web/public/locales/nl/views/exports.json` | 1 | — |
| `web/public/locales/nl/views/faceLibrary.json` | 1 | — |
| `web/public/locales/nl/views/live.json` | 4 | — |
| `web/public/locales/nl/views/settings.json` | 71 | — |
| `web/public/locales/nl/views/system.json` | 14 | — |
| `web/public/locales/pl/common.json` | 7 | — |
| `web/public/locales/pl/components/auth.json` | 1 | — |
| `web/public/locales/pl/components/dialog.json` | 7 | — |
| `web/public/locales/pl/components/filter.json` | 3 | — |
| `web/public/locales/pl/components/player.json` | 6 | — |
| `web/public/locales/pl/views/classificationModel.json` | 3 | — |
| `web/public/locales/pl/views/configEditor.json` | 2 | — |
| `web/public/locales/pl/views/events.json` | 2 | — |
| `web/public/locales/pl/views/explore.json` | 9 | — |
| `web/public/locales/pl/views/exports.json` | 1 | — |
| `web/public/locales/pl/views/faceLibrary.json` | 1 | — |
| `web/public/locales/pl/views/live.json` | 4 | — |
| `web/public/locales/pl/views/settings.json` | 64 | — |
| `web/public/locales/pl/views/system.json` | 15 | — |
| `web/public/locales/pt/common.json` | 7 | — |
| `web/public/locales/pt/components/auth.json` | 1 | — |
| `web/public/locales/pt/components/dialog.json` | 7 | — |
| `web/public/locales/pt/components/filter.json` | 3 | — |
| `web/public/locales/pt/components/player.json` | 6 | — |
| `web/public/locales/pt/views/classificationModel.json` | 2 | — |
| `web/public/locales/pt/views/configEditor.json` | 2 | — |
| `web/public/locales/pt/views/events.json` | 2 | — |
| `web/public/locales/pt/views/explore.json` | 8 | — |
| `web/public/locales/pt/views/exports.json` | 1 | — |
| `web/public/locales/pt/views/faceLibrary.json` | 1 | — |
| `web/public/locales/pt/views/live.json` | 2 | — |
| `web/public/locales/pt/views/settings.json` | 61 | — |
| `web/public/locales/pt/views/system.json` | 14 | — |
| `web/public/locales/pt-BR/common.json` | 7 | — |
| `web/public/locales/pt-BR/components/auth.json` | 1 | — |
| `web/public/locales/pt-BR/components/dialog.json` | 5 | — |
| `web/public/locales/pt-BR/components/filter.json` | 3 | — |
| `web/public/locales/pt-BR/components/player.json` | 6 | — |
| `web/public/locales/pt-BR/views/classificationModel.json` | 2 | — |
| `web/public/locales/pt-BR/views/configEditor.json` | 2 | — |
| `web/public/locales/pt-BR/views/events.json` | 2 | — |
| `web/public/locales/pt-BR/views/explore.json` | 9 | — |
| `web/public/locales/pt-BR/views/exports.json` | 1 | — |
| `web/public/locales/pt-BR/views/faceLibrary.json` | 1 | — |
| `web/public/locales/pt-BR/views/live.json` | 4 | — |
| `web/public/locales/pt-BR/views/settings.json` | 55 | — |
| `web/public/locales/pt-BR/views/system.json` | 14 | — |
| `web/public/locales/pt_BR/config/cameras.json` | 1 | — |
| `web/public/locales/ro/common.json` | 7 | — |
| `web/public/locales/ro/components/auth.json` | 1 | — |
| `web/public/locales/ro/components/dialog.json` | 7 | — |
| `web/public/locales/ro/components/filter.json` | 3 | — |
| `web/public/locales/ro/components/player.json` | 6 | — |
| `web/public/locales/ro/config/cameras.json` | 5 | — |
| `web/public/locales/ro/config/global.json` | 33 | — |
| `web/public/locales/ro/views/classificationModel.json` | 3 | — |
| `web/public/locales/ro/views/configEditor.json` | 2 | — |
| `web/public/locales/ro/views/events.json` | 2 | — |
| `web/public/locales/ro/views/explore.json` | 9 | — |
| `web/public/locales/ro/views/exports.json` | 1 | — |
| `web/public/locales/ro/views/faceLibrary.json` | 1 | — |
| `web/public/locales/ro/views/live.json` | 4 | — |
| `web/public/locales/ro/views/settings.json` | 80 | — |
| `web/public/locales/ro/views/system.json` | 16 | — |
| `web/public/locales/ru/common.json` | 7 | — |
| `web/public/locales/ru/components/auth.json` | 1 | — |
| `web/public/locales/ru/components/dialog.json` | 6 | — |
| `web/public/locales/ru/components/filter.json` | 3 | — |
| `web/public/locales/ru/components/player.json` | 6 | — |
| `web/public/locales/ru/views/classificationModel.json` | 3 | — |
| `web/public/locales/ru/views/configEditor.json` | 2 | — |
| `web/public/locales/ru/views/events.json` | 2 | — |
| `web/public/locales/ru/views/explore.json` | 9 | — |
| `web/public/locales/ru/views/exports.json` | 1 | — |
| `web/public/locales/ru/views/faceLibrary.json` | 1 | — |
| `web/public/locales/ru/views/live.json` | 4 | — |
| `web/public/locales/ru/views/settings.json` | 65 | — |
| `web/public/locales/ru/views/system.json` | 15 | — |
| `web/public/locales/sk/common.json` | 7 | — |
| `web/public/locales/sk/components/auth.json` | 1 | — |
| `web/public/locales/sk/components/dialog.json` | 4 | — |
| `web/public/locales/sk/components/filter.json` | 3 | — |
| `web/public/locales/sk/components/player.json` | 6 | — |
| `web/public/locales/sk/views/classificationModel.json` | 3 | — |
| `web/public/locales/sk/views/configEditor.json` | 2 | — |
| `web/public/locales/sk/views/events.json` | 1 | — |
| `web/public/locales/sk/views/explore.json` | 8 | — |
| `web/public/locales/sk/views/exports.json` | 1 | — |
| `web/public/locales/sk/views/live.json` | 3 | — |
| `web/public/locales/sk/views/settings.json` | 62 | — |
| `web/public/locales/sk/views/system.json` | 15 | — |
| `web/public/locales/sl/common.json` | 7 | — |
| `web/public/locales/sl/components/auth.json` | 1 | — |
| `web/public/locales/sl/components/dialog.json` | 4 | — |
| `web/public/locales/sl/components/filter.json` | 3 | — |
| `web/public/locales/sl/components/player.json` | 6 | — |
| `web/public/locales/sl/views/configEditor.json` | 2 | — |
| `web/public/locales/sl/views/events.json` | 2 | — |
| `web/public/locales/sl/views/explore.json` | 8 | — |
| `web/public/locales/sl/views/exports.json` | 1 | — |
| `web/public/locales/sl/views/faceLibrary.json` | 1 | — |
| `web/public/locales/sl/views/live.json` | 2 | — |
| `web/public/locales/sl/views/settings.json` | 23 | — |
| `web/public/locales/sl/views/system.json` | 14 | — |
| `web/public/locales/sr/common.json` | 1 | — |
| `web/public/locales/sr/components/dialog.json` | 3 | — |
| `web/public/locales/sr/components/filter.json` | 3 | — |
| `web/public/locales/sr/components/player.json` | 4 | — |
| `web/public/locales/sr/views/configEditor.json` | 1 | — |
| `web/public/locales/sr/views/explore.json` | 1 | — |
| `web/public/locales/sr/views/exports.json` | 1 | — |
| `web/public/locales/sr/views/live.json` | 2 | — |
| `web/public/locales/sr/views/settings.json` | 7 | — |
| `web/public/locales/sr/views/system.json` | 8 | — |
| `web/public/locales/sv/common.json` | 7 | — |
| `web/public/locales/sv/components/auth.json` | 1 | — |
| `web/public/locales/sv/components/dialog.json` | 5 | — |
| `web/public/locales/sv/components/filter.json` | 3 | — |
| `web/public/locales/sv/components/player.json` | 6 | — |
| `web/public/locales/sv/views/classificationModel.json` | 3 | — |
| `web/public/locales/sv/views/configEditor.json` | 2 | — |
| `web/public/locales/sv/views/events.json` | 2 | — |
| `web/public/locales/sv/views/explore.json` | 9 | — |
| `web/public/locales/sv/views/exports.json` | 1 | — |
| `web/public/locales/sv/views/faceLibrary.json` | 1 | — |
| `web/public/locales/sv/views/live.json` | 4 | — |
| `web/public/locales/sv/views/settings.json` | 63 | — |
| `web/public/locales/sv/views/system.json` | 15 | — |
| `web/public/locales/th/common.json` | 6 | — |
| `web/public/locales/th/components/dialog.json` | 5 | — |
| `web/public/locales/th/components/filter.json` | 2 | — |
| `web/public/locales/th/components/player.json` | 6 | — |
| `web/public/locales/th/views/classificationModel.json` | 1 | — |
| `web/public/locales/th/views/configEditor.json` | 1 | — |
| `web/public/locales/th/views/events.json` | 2 | — |
| `web/public/locales/th/views/explore.json` | 1 | — |
| `web/public/locales/th/views/exports.json` | 1 | — |
| `web/public/locales/th/views/live.json` | 2 | — |
| `web/public/locales/th/views/settings.json` | 19 | — |
| `web/public/locales/th/views/system.json` | 9 | — |
| `web/public/locales/tr/common.json` | 7 | — |
| `web/public/locales/tr/components/auth.json` | 1 | — |
| `web/public/locales/tr/components/dialog.json` | 6 | — |
| `web/public/locales/tr/components/filter.json` | 3 | — |
| `web/public/locales/tr/components/player.json` | 6 | — |
| `web/public/locales/tr/views/classificationModel.json` | 3 | — |
| `web/public/locales/tr/views/configEditor.json` | 2 | — |
| `web/public/locales/tr/views/events.json` | 2 | — |
| `web/public/locales/tr/views/explore.json` | 9 | — |
| `web/public/locales/tr/views/exports.json` | 1 | — |
| `web/public/locales/tr/views/faceLibrary.json` | 1 | — |
| `web/public/locales/tr/views/live.json` | 4 | — |
| `web/public/locales/tr/views/settings.json` | 64 | — |
| `web/public/locales/tr/views/system.json` | 14 | — |
| `web/public/locales/uk/common.json` | 6 | — |
| `web/public/locales/uk/components/auth.json` | 1 | — |
| `web/public/locales/uk/components/dialog.json` | 4 | — |
| `web/public/locales/uk/components/filter.json` | 3 | — |
| `web/public/locales/uk/components/player.json` | 6 | — |
| `web/public/locales/uk/views/classificationModel.json` | 2 | — |
| `web/public/locales/uk/views/configEditor.json` | 1 | — |
| `web/public/locales/uk/views/events.json` | 2 | — |
| `web/public/locales/uk/views/explore.json` | 8 | — |
| `web/public/locales/uk/views/exports.json` | 1 | — |
| `web/public/locales/uk/views/faceLibrary.json` | 1 | — |
| `web/public/locales/uk/views/live.json` | 4 | — |
| `web/public/locales/uk/views/settings.json` | 50 | — |
| `web/public/locales/uk/views/system.json` | 8 | — |
| `web/public/locales/ur/components/dialog.json` | 1 | — |
| `web/public/locales/ur/components/player.json` | 1 | — |
| `web/public/locales/ur/views/configEditor.json` | 1 | — |
| `web/public/locales/ur/views/system.json` | 1 | — |
| `web/public/locales/uz/components/dialog.json` | 1 | — |
| `web/public/locales/uz/views/explore.json` | 1 | — |
| `web/public/locales/vi/common.json` | 3 | — |
| `web/public/locales/vi/components/auth.json` | 1 | — |
| `web/public/locales/vi/components/dialog.json` | 4 | — |
| `web/public/locales/vi/components/filter.json` | 3 | — |
| `web/public/locales/vi/components/player.json` | 6 | — |
| `web/public/locales/vi/views/classificationModel.json` | 1 | — |
| `web/public/locales/vi/views/configEditor.json` | 2 | — |
| `web/public/locales/vi/views/events.json` | 2 | — |
| `web/public/locales/vi/views/explore.json` | 9 | — |
| `web/public/locales/vi/views/exports.json` | 1 | — |
| `web/public/locales/vi/views/faceLibrary.json` | 1 | — |
| `web/public/locales/vi/views/live.json` | 3 | — |
| `web/public/locales/vi/views/settings.json` | 51 | — |
| `web/public/locales/vi/views/system.json` | 15 | — |
| `web/public/locales/yue-Hant/common.json` | 7 | — |
| `web/public/locales/yue-Hant/components/auth.json` | 1 | — |
| `web/public/locales/yue-Hant/components/dialog.json` | 5 | — |
| `web/public/locales/yue-Hant/components/filter.json` | 3 | — |
| `web/public/locales/yue-Hant/components/player.json` | 6 | — |
| `web/public/locales/yue-Hant/views/classificationModel.json` | 3 | — |
| `web/public/locales/yue-Hant/views/configEditor.json` | 2 | — |
| `web/public/locales/yue-Hant/views/events.json` | 2 | — |
| `web/public/locales/yue-Hant/views/explore.json` | 9 | — |
| `web/public/locales/yue-Hant/views/exports.json` | 1 | — |
| `web/public/locales/yue-Hant/views/faceLibrary.json` | 1 | — |
| `web/public/locales/yue-Hant/views/live.json` | 4 | — |
| `web/public/locales/yue-Hant/views/settings.json` | 67 | — |
| `web/public/locales/yue-Hant/views/system.json` | 13 | — |
| `web/public/locales/yue_Hant/config/cameras.json` | 1 | — |
| `web/public/locales/zh-CN/common.json` | 7 | — |
| `web/public/locales/zh-CN/components/auth.json` | 1 | — |
| `web/public/locales/zh-CN/components/dialog.json` | 7 | — |
| `web/public/locales/zh-CN/components/filter.json` | 3 | — |
| `web/public/locales/zh-CN/components/player.json` | 6 | — |
| `web/public/locales/zh-CN/views/classificationModel.json` | 3 | — |
| `web/public/locales/zh-CN/views/configEditor.json` | 2 | — |
| `web/public/locales/zh-CN/views/events.json` | 2 | — |
| `web/public/locales/zh-CN/views/explore.json` | 9 | — |
| `web/public/locales/zh-CN/views/exports.json` | 1 | — |
| `web/public/locales/zh-CN/views/faceLibrary.json` | 1 | — |
| `web/public/locales/zh-CN/views/live.json` | 4 | — |
| `web/public/locales/zh-CN/views/settings.json` | 67 | — |
| `web/public/locales/zh-CN/views/system.json` | 15 | — |
| `web/public/locales/zh-Hant/common.json` | 7 | — |
| `web/public/locales/zh-Hant/components/auth.json` | 1 | — |
| `web/public/locales/zh-Hant/components/dialog.json` | 4 | — |
| `web/public/locales/zh-Hant/components/filter.json` | 3 | — |
| `web/public/locales/zh-Hant/components/player.json` | 6 | — |
| `web/public/locales/zh-Hant/views/classificationModel.json` | 1 | — |
| `web/public/locales/zh-Hant/views/configEditor.json` | 2 | — |
| `web/public/locales/zh-Hant/views/events.json` | 2 | — |
| `web/public/locales/zh-Hant/views/explore.json` | 9 | — |
| `web/public/locales/zh-Hant/views/exports.json` | 1 | — |
| `web/public/locales/zh-Hant/views/faceLibrary.json` | 1 | — |
| `web/public/locales/zh-Hant/views/live.json` | 2 | — |
| `web/public/locales/zh-Hant/views/settings.json` | 17 | — |
| `web/public/locales/zh-Hant/views/system.json` | 14 | — |

### `.jsx` — 1 archivos · 1 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `docs/src/components/LanguageAlert/index.jsx` | 1 | — |

### `.md` — 77 archivos · 1381 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `.github/copilot-instructions.md` | 22 | — |
| `.github/pull_request_template.md` | 3 | — |
| `README.md` | 21 | — |
| `README_CN.md` | 17 | — |
| `TRADEMARK.md` | 23 | — |
| `docs/README.md` | 1 | — |
| `docs/docs/configuration/advanced.md` | 42 | — |
| `docs/docs/configuration/audio_detectors.md` | 14 | — |
| `docs/docs/configuration/authentication.md` | 38 | — |
| `docs/docs/configuration/autotracking.md` | 41 | — |
| `docs/docs/configuration/bird_classification.md` | 1 | — |
| `docs/docs/configuration/birdseye.md` | 2 | — |
| `docs/docs/configuration/camera_specific.md` | 10 | — |
| `docs/docs/configuration/cameras.md` | 8 | — |
| `docs/docs/configuration/custom_classification/object_classification.md` | 10 | — |
| `docs/docs/configuration/custom_classification/state_classification.md` | 7 | — |
| `docs/docs/configuration/face_recognition.md` | 17 | — |
| `docs/docs/configuration/ffmpeg_presets.md` | 7 | — |
| `docs/docs/configuration/genai/config.md` | 25 | — |
| `docs/docs/configuration/genai/objects.md` | 11 | — |
| `docs/docs/configuration/genai/review_summaries.md` | 7 | — |
| `docs/docs/configuration/hardware_acceleration_enrichments.md` | 9 | — |
| `docs/docs/configuration/hardware_acceleration_video.md` | 25 | — |
| `docs/docs/configuration/index.md` | 13 | — |
| `docs/docs/configuration/license_plate_recognition.md` | 60 | — |
| `docs/docs/configuration/live.md` | 41 | — |
| `docs/docs/configuration/masks.md` | 10 | — |
| `docs/docs/configuration/metrics.md` | 37 | — |
| `docs/docs/configuration/motion_detection.md` | 5 | — |
| `docs/docs/configuration/notifications.md` | 7 | — |
| `docs/docs/configuration/object_detectors.md` | 82 | — |
| `docs/docs/configuration/object_filters.md` | 1 | — |
| `docs/docs/configuration/objects.md` | 1 | — |
| `docs/docs/configuration/pwa.md` | 6 | — |
| `docs/docs/configuration/record.md` | 9 | — |
| `docs/docs/configuration/reference.md` | 23 | — |
| `docs/docs/configuration/restream.md` | 13 | — |
| `docs/docs/configuration/review.md` | 8 | — |
| `docs/docs/configuration/semantic_search.md` | 19 | — |
| `docs/docs/configuration/snapshots.md` | 8 | — |
| `docs/docs/configuration/stationary_objects.md` | 3 | — |
| `docs/docs/configuration/tls.md` | 17 | — |
| `docs/docs/configuration/zones.md` | 7 | — |
| `docs/docs/development/contributing-boards.md` | 6 | — |
| `docs/docs/development/contributing.md` | 25 | — |
| `docs/docs/frigate/camera_setup.md` | 8 | — |
| `docs/docs/frigate/glossary.md` | 4 | — |
| `docs/docs/frigate/hardware.md` | 23 | — |
| `docs/docs/frigate/index.md` | 2 | — |
| `docs/docs/frigate/installation.md` | 105 | — |
| `docs/docs/frigate/planning_setup.md` | 6 | — |
| `docs/docs/frigate/updating.md` | 29 | — |
| `docs/docs/frigate/video_pipeline.md` | 2 | — |
| `docs/docs/guides/configuring_go2rtc.md` | 9 | — |
| `docs/docs/guides/getting_started.md` | 34 | — |
| `docs/docs/guides/ha_network_storage.md` | 12 | — |
| `docs/docs/guides/ha_notifications.md` | 10 | — |
| `docs/docs/guides/reverse_proxy.md` | 30 | — |
| `docs/docs/integrations/home-assistant.md` | 63 | — |
| `docs/docs/integrations/homekit.md` | 8 | — |
| `docs/docs/integrations/mqtt.md` | 77 | — |
| `docs/docs/integrations/plus.md` | 22 | — |
| `docs/docs/integrations/third_party_extensions.md` | 30 | — |
| `docs/docs/plus/annotating.md` | 4 | — |
| `docs/docs/plus/faq.md` | 12 | — |
| `docs/docs/plus/first_model.md` | 9 | — |
| `docs/docs/plus/index.md` | 23 | — |
| `docs/docs/troubleshooting/cpu.md` | 11 | — |
| `docs/docs/troubleshooting/dummy-camera.md` | 5 | — |
| `docs/docs/troubleshooting/edgetpu.md` | 9 | — |
| `docs/docs/troubleshooting/faqs.md` | 26 | — |
| `docs/docs/troubleshooting/gpu.md` | 1 | — |
| `docs/docs/troubleshooting/memory.md` | 27 | — |
| `docs/docs/troubleshooting/recordings.md` | 6 | — |
| `docs/static/img/branding/LICENSE.md` | 7 | — |
| `notebooks/README.md` | 2 | — |
| `web/README.md` | 3 | — |

### `.py` — 222 archivos · 1886 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `benchmark.py` | 5 | — |
| `benchmark_motion.py` | 3 | — |
| `docker/main/rootfs/usr/local/ffmpeg/get_ffmpeg_path.py` | 4 | — |
| `docker/main/rootfs/usr/local/go2rtc/create_config.py` | 17 | — |
| `docker/main/rootfs/usr/local/nginx/get_nginx_settings.py` | 4 | — |
| `generate_config_translations.py` | 16 | — |
| `migrations/002_add_clip_snapshot.py` | 1 | — |
| `migrations/004_add_bbox_region_area.py` | 1 | — |
| `migrations/005_make_end_time_nullable.py` | 1 | — |
| `migrations/006_add_motion_active_objects.py` | 1 | — |
| `migrations/007_add_retain_indefinitely.py` | 1 | — |
| `migrations/008_add_sub_label.py` | 1 | — |
| `migrations/009_add_object_filter_ratio.py` | 1 | — |
| `migrations/010_add_plus_image_id.py` | 1 | — |
| `migrations/012_add_segment_size.py` | 1 | — |
| `migrations/014_event_updates_for_fp.py` | 1 | — |
| `migrations/015_event_refactor.py` | 1 | — |
| `migrations/016_sublabel_increase.py` | 1 | — |
| `migrations/018_add_dbfs.py` | 1 | — |
| `migrations/023_add_regions.py` | 1 | — |
| `migrations/026_add_notification_tokens.py` | 1 | — |
| `migrations/028_optional_event_thumbnail.py` | 1 | — |
| `migrations/030_create_user_review_status.py` | 1 | — |
| `process_clip.py` | 13 | — |
| `securevu/__main__.py` | 18 | — |
| `securevu/api/app.py` | 53 | — |
| `securevu/api/auth.py` | 38 | — |
| `securevu/api/camera.py` | 25 | — |
| `securevu/api/chat.py` | 18 | — |
| `securevu/api/classification.py` | 42 | — |
| `securevu/api/debug_replay.py` | 7 | — |
| `securevu/api/defs/query/regenerate_query_parameters.py` | 1 | — |
| `securevu/api/defs/query/review_query_parameters.py` | 1 | — |
| `securevu/api/defs/request/events_body.py` | 1 | — |
| `securevu/api/defs/request/export_recordings_body.py` | 1 | — |
| `securevu/api/defs/response/review_response.py` | 1 | — |
| `securevu/api/event.py` | 38 | — |
| `securevu/api/export.py` | 16 | — |
| `securevu/api/fastapi_app.py` | 22 | — |
| `securevu/api/media.py` | 42 | — |
| `securevu/api/motion_search.py` | 7 | — |
| `securevu/api/notification.py` | 6 | — |
| `securevu/api/preview.py` | 5 | — |
| `securevu/api/record.py` | 7 | — |
| `securevu/api/review.py` | 10 | — |
| `securevu/app.py` | 56 | — |
| `securevu/camera/activity_manager.py` | 5 | — |
| `securevu/camera/maintainer.py` | 12 | — |
| `securevu/camera/state.py` | 7 | — |
| `securevu/comms/dispatcher.py` | 19 | — |
| `securevu/comms/events_updater.py` | 1 | — |
| `securevu/comms/inter_process.py` | 1 | — |
| `securevu/comms/mqtt.py` | 5 | — |
| `securevu/comms/webpush.py` | 11 | — |
| `securevu/comms/ws.py` | 5 | — |
| `securevu/comms/zmq_proxy.py` | 1 | — |
| `securevu/config/__init__.py` | 1 | — |
| `securevu/config/auth.py` | 4 | — |
| `securevu/config/base.py` | 1 | — |
| `securevu/config/camera/audio.py` | 4 | — |
| `securevu/config/camera/birdseye.py` | 3 | — |
| `securevu/config/camera/camera.py` | 6 | — |
| `securevu/config/camera/detect.py` | 4 | — |
| `securevu/config/camera/ffmpeg.py` | 6 | — |
| `securevu/config/camera/genai.py` | 2 | — |
| `securevu/config/camera/live.py` | 2 | — |
| `securevu/config/camera/mask.py` | 5 | — |
| `securevu/config/camera/motion.py` | 2 | — |
| `securevu/config/camera/mqtt.py` | 2 | — |
| `securevu/config/camera/notification.py` | 2 | — |
| `securevu/config/camera/objects.py` | 5 | — |
| `securevu/config/camera/onvif.py` | 5 | — |
| `securevu/config/camera/record.py` | 9 | — |
| `securevu/config/camera/review.py` | 5 | — |
| `securevu/config/camera/snapshots.py` | 3 | — |
| `securevu/config/camera/timestamp.py` | 3 | — |
| `securevu/config/camera/ui.py` | 3 | — |
| `securevu/config/camera/updater.py` | 4 | — |
| `securevu/config/camera/zone.py` | 1 | — |
| `securevu/config/camera_group.py` | 2 | — |
| `securevu/config/classification.py` | 17 | — |
| `securevu/config/config.py` | 33 | — |
| `securevu/config/database.py` | 4 | — |
| `securevu/config/env.py` | 5 | — |
| `securevu/config/logger.py` | 3 | — |
| `securevu/config/mqtt.py` | 6 | — |
| `securevu/config/network.py` | 8 | — |
| `securevu/config/proxy.py` | 5 | — |
| `securevu/config/telemetry.py` | 4 | — |
| `securevu/config/tls.py` | 3 | — |
| `securevu/config/ui.py` | 2 | — |
| `securevu/const.py` | 5 | — |
| `securevu/data_processing/common/audio_transcription/model.py` | 4 | — |
| `securevu/data_processing/common/face/model.py` | 8 | — |
| `securevu/data_processing/common/license_plate/mixin.py` | 12 | — |
| `securevu/data_processing/common/license_plate/model.py` | 1 | — |
| `securevu/data_processing/post/api.py` | 3 | — |
| `securevu/data_processing/post/audio_transcription.py` | 8 | — |
| `securevu/data_processing/post/license_plate.py` | 11 | — |
| `securevu/data_processing/post/object_descriptions.py` | 14 | — |
| `securevu/data_processing/post/review_descriptions.py` | 13 | — |
| `securevu/data_processing/post/semantic_trigger.py` | 12 | — |
| `securevu/data_processing/real_time/api.py` | 3 | — |
| `securevu/data_processing/real_time/audio_transcription.py` | 7 | — |
| `securevu/data_processing/real_time/bird.py` | 9 | — |
| `securevu/data_processing/real_time/custom_classification.py` | 13 | — |
| `securevu/data_processing/real_time/face.py` | 13 | — |
| `securevu/data_processing/real_time/license_plate.py` | 7 | — |
| `securevu/data_processing/real_time/whisper_online.py` | 1 | — |
| `securevu/data_processing/types.py` | 1 | — |
| `securevu/debug_replay.py` | 28 | — |
| `securevu/detectors/detection_api.py` | 1 | — |
| `securevu/detectors/detection_runners.py` | 11 | — |
| `securevu/detectors/detector_config.py` | 4 | — |
| `securevu/detectors/plugins/cpu_tfl.py` | 3 | — |
| `securevu/detectors/plugins/deepstack.py` | 2 | — |
| `securevu/detectors/plugins/degirum.py` | 3 | — |
| `securevu/detectors/plugins/edgetpu_tfl.py` | 2 | — |
| `securevu/detectors/plugins/hailo8l.py` | 4 | — |
| `securevu/detectors/plugins/memryx.py` | 14 | — |
| `securevu/detectors/plugins/onnx.py` | 4 | — |
| `securevu/detectors/plugins/openvino.py` | 5 | — |
| `securevu/detectors/plugins/rknn.py` | 7 | — |
| `securevu/detectors/plugins/synaptics.py` | 2 | — |
| `securevu/detectors/plugins/teflon_tfl.py` | 2 | — |
| `securevu/detectors/plugins/tensorrt.py` | 4 | — |
| `securevu/detectors/plugins/zmq_ipc.py` | 2 | — |
| `securevu/embeddings/__init__.py` | 14 | — |
| `securevu/embeddings/embeddings.py` | 12 | — |
| `securevu/embeddings/genai_embedding.py` | 2 | — |
| `securevu/embeddings/maintainer.py` | 34 | — |
| `securevu/embeddings/onnx/base_embedding.py` | 3 | — |
| `securevu/embeddings/onnx/face_embedding.py` | 5 | — |
| `securevu/embeddings/onnx/jina_v1_embedding.py` | 6 | — |
| `securevu/embeddings/onnx/jina_v2_embedding.py` | 6 | — |
| `securevu/embeddings/onnx/lpr_embedding.py` | 6 | — |
| `securevu/events/audio.py` | 20 | — |
| `securevu/events/cleanup.py` | 7 | — |
| `securevu/events/maintainer.py` | 9 | — |
| `securevu/ffmpeg_presets.py` | 5 | — |
| `securevu/genai/__init__.py` | 9 | — |
| `securevu/genai/azure-openai.py` | 4 | — |
| `securevu/genai/gemini.py` | 4 | — |
| `securevu/genai/llama_cpp.py` | 5 | — |
| `securevu/genai/manager.py` | 11 | — |
| `securevu/genai/ollama.py` | 5 | — |
| `securevu/genai/openai.py` | 4 | — |
| `securevu/jobs/manager.py` | 2 | — |
| `securevu/jobs/media_sync.py` | 6 | — |
| `securevu/jobs/motion_search.py` | 10 | — |
| `securevu/log.py` | 1 | — |
| `securevu/motion/__init__.py` | 1 | — |
| `securevu/motion/frigate_motion.py` | 5 | `securevu/motion/securevu_motion.py` |
| `securevu/motion/improved_motion.py` | 4 | — |
| `securevu/object_detection/base.py` | 18 | — |
| `securevu/object_detection/util.py` | 1 | — |
| `securevu/output/birdseye.py` | 10 | — |
| `securevu/output/camera.py` | 1 | — |
| `securevu/output/output.py` | 18 | — |
| `securevu/output/preview.py` | 7 | — |
| `securevu/plus.py` | 2 | — |
| `securevu/ptz/autotrack.py` | 13 | — |
| `securevu/ptz/onvif.py` | 5 | — |
| `securevu/record/cleanup.py` | 7 | — |
| `securevu/record/export.py` | 9 | — |
| `securevu/record/maintainer.py` | 11 | — |
| `securevu/record/record.py` | 10 | — |
| `securevu/review/maintainer.py` | 12 | — |
| `securevu/review/review.py` | 9 | — |
| `securevu/service_manager/multiprocessing.py` | 3 | — |
| `securevu/stats/emitter.py` | 9 | — |
| `securevu/stats/prometheus.py` | 34 | — |
| `securevu/stats/util.py` | 18 | — |
| `securevu/storage.py` | 7 | — |
| `securevu/test/http_api/base_http_test.py` | 10 | — |
| `securevu/test/http_api/test_http_app.py` | 4 | — |
| `securevu/test/http_api/test_http_camera_access.py` | 7 | — |
| `securevu/test/http_api/test_http_config_set.py` | 13 | — |
| `securevu/test/http_api/test_http_event.py` | 16 | — |
| `securevu/test/http_api/test_http_latest_frame.py` | 6 | — |
| `securevu/test/http_api/test_http_media.py` | 3 | — |
| `securevu/test/http_api/test_http_review.py` | 4 | — |
| `securevu/test/test_birdseye.py` | 1 | — |
| `securevu/test/test_camera_pw.py` | 1 | — |
| `securevu/test/test_config.py` | 183 | — |
| `securevu/test/test_copy_yuv_to_position.py` | 1 | — |
| `securevu/test/test_ffmpeg_presets.py` | 39 | — |
| `securevu/test/test_gpu_stats.py` | 1 | — |
| `securevu/test/test_maintainer.py` | 10 | — |
| `securevu/test/test_motion_detector.py` | 2 | — |
| `securevu/test/test_obects.py` | 1 | — |
| `securevu/test/test_object_detector.py` | 14 | — |
| `securevu/test/test_preview_loader.py` | 1 | — |
| `securevu/test/test_proxy_auth.py` | 2 | — |
| `securevu/test/test_record_retention.py` | 2 | — |
| `securevu/test/test_reduce_boxes.py` | 1 | — |
| `securevu/test/test_storage.py` | 9 | — |
| `securevu/test/test_video.py` | 2 | — |
| `securevu/test/test_yuv_region_2_rgb.py` | 1 | — |
| `securevu/timeline.py` | 6 | — |
| `securevu/track/__init__.py` | 1 | — |
| `securevu/track/centroid_tracker.py` | 3 | — |
| `securevu/track/norfair_tracker.py` | 15 | — |
| `securevu/track/object_processing.py` | 16 | — |
| `securevu/track/tracked_object.py` | 8 | — |
| `securevu/types.py` | 4 | — |
| `securevu/util/audio.py` | 2 | — |
| `securevu/util/builtin.py` | 4 | — |
| `securevu/util/camera_cleanup.py` | 2 | — |
| `securevu/util/classification.py` | 13 | — |
| `securevu/util/config.py` | 22 | — |
| `securevu/util/downloader.py` | 4 | — |
| `securevu/util/file.py` | 2 | — |
| `securevu/util/media.py` | 2 | — |
| `securevu/util/model.py` | 1 | — |
| `securevu/util/object.py` | 5 | — |
| `securevu/util/process.py` | 10 | — |
| `securevu/util/rknn_converter.py` | 3 | — |
| `securevu/util/schema.py` | 7 | — |
| `securevu/util/services.py` | 8 | — |
| `securevu/video.py` | 25 | — |
| `securevu/watchdog.py` | 7 | — |

### `.sh` — 6 archivos · 19 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `.devcontainer/post_create.sh` | 4 | — |
| `docker/main/build_nginx.sh` | 1 | — |
| `docker/main/install_deps.sh` | 1 | — |
| `docker/main/install_hailort.sh` | 2 | — |
| `docker/main/install_memryx.sh` | 10 | — |
| `docker/tensorrt/detector/build_python_tensorrt.sh` | 1 | — |

### `.ts` — 25 archivos · 119 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `docs/docusaurus.config.ts` | 21 | — |
| `docs/sidebars.ts` | 14 | — |
| `web/src/components/config-form/theme/frigateTheme.ts` | 4 | `web/src/components/config-form/theme/securevuTheme.ts` |
| `web/src/components/config-form/theme/index.ts` | 4 | — |
| `web/src/hooks/use-allowed-cameras.ts` | 3 | — |
| `web/src/hooks/use-camera-activity.ts` | 7 | — |
| `web/src/hooks/use-camera-friendly-name.ts` | 4 | — |
| `web/src/hooks/use-camera-live-mode.ts` | 3 | — |
| `web/src/hooks/use-config-override.ts` | 5 | — |
| `web/src/hooks/use-date-utils.ts` | 5 | — |
| `web/src/hooks/use-doc-domain.ts` | 2 | — |
| `web/src/hooks/use-draggable-element.ts` | 3 | — |
| `web/src/hooks/use-navigation.ts` | 3 | — |
| `web/src/hooks/use-stats.ts` | 10 | — |
| `web/src/hooks/use-user-persistence.ts` | 1 | — |
| `web/src/hooks/use-zone-friendly-name.ts` | 4 | — |
| `web/src/lib/config-schema/index.ts` | 1 | — |
| `web/src/types/configForm.ts` | 3 | — |
| `web/src/types/frigateConfig.ts` | 1 | `web/src/types/securevuConfig.ts` |
| `web/src/types/log.ts` | 1 | — |
| `web/src/types/stats.ts` | 1 | — |
| `web/src/types/ws.ts` | 7 | — |
| `web/src/utils/cameraUtil.ts` | 2 | — |
| `web/src/utils/configUtil.ts` | 5 | — |
| `web/src/utils/logUtil.ts` | 5 | — |

### `.tsx` — 126 archivos · 545 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `web/src/App.tsx` | 4 | — |
| `web/src/api/ws.tsx` | 14 | — |
| `web/src/components/Statusbar.tsx` | 3 | — |
| `web/src/components/audio/AudioLevelGraph.tsx` | 3 | — |
| `web/src/components/button/DownloadVideoButton.tsx` | 3 | — |
| `web/src/components/camera/DebugCameraImage.tsx` | 1 | — |
| `web/src/components/camera/FriendlyNameLabel.tsx` | 1 | — |
| `web/src/components/camera/ResizingCameraImage.tsx` | 1 | — |
| `web/src/components/card/AnimatedEventCard.tsx` | 3 | — |
| `web/src/components/card/ReviewCard.tsx` | 3 | — |
| `web/src/components/card/SearchThumbnail.tsx` | 3 | — |
| `web/src/components/card/SearchThumbnailFooter.tsx` | 3 | — |
| `web/src/components/classification/ClassificationModelEditDialog.tsx` | 3 | — |
| `web/src/components/classification/wizard/Step1NameAndDefine.tsx` | 3 | — |
| `web/src/components/classification/wizard/Step2StateArea.tsx` | 3 | — |
| `web/src/components/config-form/ConfigForm.tsx` | 2 | — |
| `web/src/components/config-form/sectionExtras/CameraReviewStatusToggles.tsx` | 3 | — |
| `web/src/components/config-form/sectionExtras/NotificationsSettingsExtras.tsx` | 4 | — |
| `web/src/components/config-form/sections/BaseSection.tsx` | 4 | — |
| `web/src/components/config-form/theme/fields/DetectorHardwareField.tsx` | 1 | — |
| `web/src/components/config-form/theme/fields/LayoutGridField.tsx` | 1 | — |
| `web/src/components/config-form/theme/widgets/ObjectLabelSwitchesWidget.tsx` | 3 | — |
| `web/src/components/config-form/theme/widgets/SwitchesWidget.tsx` | 3 | — |
| `web/src/components/filter/CalendarFilterButton.tsx` | 4 | — |
| `web/src/components/filter/CameraGroupSelector.tsx` | 5 | — |
| `web/src/components/filter/CamerasFilterButton.tsx` | 1 | — |
| `web/src/components/filter/ExportFilterGroup.tsx` | 3 | — |
| `web/src/components/filter/ReviewFilterGroup.tsx` | 4 | — |
| `web/src/components/filter/SearchFilterGroup.tsx` | 5 | — |
| `web/src/components/graph/LineGraph.tsx` | 4 | — |
| `web/src/components/graph/SystemGraph.tsx` | 3 | — |
| `web/src/components/icons/FrigatePlusIcon.tsx` | 4 | `web/src/components/icons/SecureVuPlusIcon.tsx` |
| `web/src/components/input/InputWithTags.tsx` | 5 | — |
| `web/src/components/menu/GeneralSettings.tsx` | 5 | — |
| `web/src/components/menu/LiveContextMenu.tsx` | 3 | — |
| `web/src/components/menu/SearchResultActions.tsx` | 3 | — |
| `web/src/components/navigation/Bottombar.tsx` | 4 | — |
| `web/src/components/overlay/CameraInfoDialog.tsx` | 1 | — |
| `web/src/components/overlay/CreateRoleDialog.tsx` | 3 | — |
| `web/src/components/overlay/CreateTriggerDialog.tsx` | 3 | — |
| `web/src/components/overlay/CreateUserDialog.tsx` | 3 | — |
| `web/src/components/overlay/CustomTimeSelector.tsx` | 3 | — |
| `web/src/components/overlay/EditRoleCamerasDialog.tsx` | 3 | — |
| `web/src/components/overlay/LogInfoDialog.tsx` | 3 | — |
| `web/src/components/overlay/ObjectTrackOverlay.tsx` | 4 | — |
| `web/src/components/overlay/ReviewActivityCalendar.tsx` | 3 | — |
| `web/src/components/overlay/detail/AnnotationSettingsPane.tsx` | 3 | — |
| `web/src/components/overlay/detail/DetailActionsMenu.tsx` | 3 | — |
| `web/src/components/overlay/detail/ObjectPath.tsx` | 3 | — |
| `web/src/components/overlay/detail/ObjectPathPlotter.tsx` | 3 | — |
| `web/src/components/overlay/detail/SearchDetailDialog.tsx` | 7 | — |
| `web/src/components/overlay/detail/TrackingDetails.tsx` | 7 | — |
| `web/src/components/overlay/dialog/FrigatePlusDialog.tsx` | 5 | `web/src/components/overlay/dialog/SecureVuPlusDialog.tsx` |
| `web/src/components/overlay/dialog/SearchFilterDialog.tsx` | 32 | — |
| `web/src/components/player/BirdseyeLivePlayer.tsx` | 1 | — |
| `web/src/components/player/GenericVideoPlayer.tsx` | 1 | — |
| `web/src/components/player/HlsVideoPlayer.tsx` | 11 | — |
| `web/src/components/player/LivePlayer.tsx` | 1 | — |
| `web/src/components/player/MsePlayer.tsx` | 1 | — |
| `web/src/components/player/PreviewPlayer.tsx` | 3 | — |
| `web/src/components/player/PreviewThumbnailPlayer.tsx` | 3 | — |
| `web/src/components/player/VideoControls.tsx` | 9 | — |
| `web/src/components/player/WebRTCPlayer.tsx` | 1 | — |
| `web/src/components/player/dynamic/DynamicVideoPlayer.tsx` | 3 | — |
| `web/src/components/settings/CameraEditForm.tsx` | 3 | — |
| `web/src/components/settings/CameraStreamingDialog.tsx` | 3 | — |
| `web/src/components/settings/CameraWizardDialog.tsx` | 2 | — |
| `web/src/components/settings/MotionMaskEditPane.tsx` | 4 | — |
| `web/src/components/settings/ObjectMaskEditPane.tsx` | 4 | — |
| `web/src/components/settings/PolygonItem.tsx` | 3 | — |
| `web/src/components/settings/SearchSettings.tsx` | 3 | — |
| `web/src/components/settings/ZoneEditPane.tsx` | 4 | — |
| `web/src/components/settings/wizard/Step1NameCamera.tsx` | 3 | — |
| `web/src/components/timeline/DetailStream.tsx` | 10 | — |
| `web/src/components/timeline/EventMenu.tsx` | 3 | — |
| `web/src/components/timeline/segment-metadata.tsx` | 4 | — |
| `web/src/components/trigger/wizard/Step1NameAndType.tsx` | 3 | — |
| `web/src/components/trigger/wizard/Step3ThresholdAndActions.tsx` | 3 | — |
| `web/src/components/ws/WsMessageFeed.tsx` | 3 | — |
| `web/src/context/detail-stream-context.tsx` | 3 | — |
| `web/src/context/language-provider.tsx` | 1 | — |
| `web/src/context/providers.tsx` | 1 | — |
| `web/src/context/streaming-settings-provider.tsx` | 1 | — |
| `web/src/context/theme-provider.tsx` | 1 | — |
| `web/src/pages/ClassificationModel.tsx` | 1 | — |
| `web/src/pages/ConfigEditor.tsx` | 3 | — |
| `web/src/pages/Events.tsx` | 3 | — |
| `web/src/pages/Explore.tsx` | 3 | — |
| `web/src/pages/FaceLibrary.tsx` | 5 | — |
| `web/src/pages/Live.tsx` | 3 | — |
| `web/src/pages/LoginPage.tsx` | 1 | — |
| `web/src/pages/Logs.tsx` | 5 | — |
| `web/src/pages/MotionSearch.tsx` | 3 | — |
| `web/src/pages/Replay.tsx` | 4 | — |
| `web/src/pages/Settings.tsx` | 9 | — |
| `web/src/pages/System.tsx` | 5 | — |
| `web/src/pages/UIPlayground.tsx` | 3 | — |
| `web/src/utils/iconUtil.tsx` | 3 | — |
| `web/src/views/classification/ModelSelectionView.tsx` | 3 | — |
| `web/src/views/classification/ModelTrainingView.tsx` | 1 | — |
| `web/src/views/events/EventView.tsx` | 4 | — |
| `web/src/views/events/MotionPreviewsPane.tsx` | 4 | — |
| `web/src/views/explore/ExploreView.tsx` | 3 | — |
| `web/src/views/live/DraggableGridLayout.tsx` | 4 | — |
| `web/src/views/live/LiveBirdseyeView.tsx` | 3 | — |
| `web/src/views/live/LiveCameraView.tsx` | 7 | — |
| `web/src/views/live/LiveDashboardView.tsx` | 5 | — |
| `web/src/views/motion-search/MotionSearchDialog.tsx` | 3 | — |
| `web/src/views/motion-search/MotionSearchView.tsx` | 3 | — |
| `web/src/views/recording/RecordingView.tsx` | 3 | — |
| `web/src/views/search/SearchView.tsx` | 3 | — |
| `web/src/views/settings/AuthenticationView.tsx` | 3 | — |
| `web/src/views/settings/CameraManagementView.tsx` | 3 | — |
| `web/src/views/settings/EnrichmentsSettingsView.tsx` | 3 | — |
| `web/src/views/settings/FrigatePlusSettingsView.tsx` | 66 | `web/src/views/settings/SecureVuPlusSettingsView.tsx` |
| `web/src/views/settings/MasksAndZonesView.tsx` | 3 | — |
| `web/src/views/settings/MotionTunerView.tsx` | 3 | — |
| `web/src/views/settings/ObjectSettingsView.tsx` | 4 | — |
| `web/src/views/settings/SystemDetectionModelSettingsView.tsx` | 8 | — |
| `web/src/views/settings/TriggerView.tsx` | 3 | — |
| `web/src/views/settings/UiSettingsView.tsx` | 3 | — |
| `web/src/views/settings/components/FrigatePlusCurrentModelSummary.tsx` | 15 | `web/src/views/settings/components/SecureVuPlusCurrentModelSummary.tsx` |
| `web/src/views/system/CameraMetrics.tsx` | 8 | — |
| `web/src/views/system/EnrichmentMetrics.tsx` | 5 | — |
| `web/src/views/system/GeneralMetrics.tsx` | 5 | — |
| `web/src/views/system/StorageMetrics.tsx` | 6 | — |

### `.txt` — 3 archivos · 2 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `.cspell/frigate-dictionary.txt` | 0 | `.cspell/securevu-dictionary.txt` |
| `docker/main/requirements-wheels.txt` | 1 | — |
| `docker/rocm/requirements-wheels-rocm.txt` | 1 | — |

### `.yaml` — 1 archivos · 10 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `docs/static/frigate-api.yaml` | 10 | `docs/static/securevu-api.yaml` |

### `.yml` — 12 archivos · 111 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `.github/DISCUSSION_TEMPLATE/beta-support.yml` | 8 | — |
| `.github/DISCUSSION_TEMPLATE/camera-support.yml` | 14 | — |
| `.github/DISCUSSION_TEMPLATE/config-support.yml` | 13 | — |
| `.github/DISCUSSION_TEMPLATE/detector-support.yml` | 11 | — |
| `.github/DISCUSSION_TEMPLATE/general-support.yml` | 14 | — |
| `.github/DISCUSSION_TEMPLATE/hardware-acceleration-support.yml` | 12 | — |
| `.github/DISCUSSION_TEMPLATE/question.yml` | 6 | — |
| `.github/DISCUSSION_TEMPLATE/report-a-bug.yml` | 18 | — |
| `.github/ISSUE_TEMPLATE/config.yml` | 5 | — |
| `.github/workflows/ci.yml` | 2 | — |
| `.github/workflows/pull_request.yml` | 4 | — |
| `docker-compose.yml` | 4 | — |

### `Dockerfile` — 5 archivos · 26 reemplazos

| Archivo | Reemplazos | Renombrado a |
|---------|-----------|--------------|
| `docker/main/Dockerfile` | 21 | — |
| `docker/rockchip/Dockerfile` | 2 | — |
| `docker/rocm/Dockerfile` | 1 | — |
| `docker/rpi/Dockerfile` | 1 | — |
| `docker/synaptics/Dockerfile` | 1 | — |

---

## 🖼 Imágenes — Reemplazo Manual

| Archivo | Dimensiones sugeridas | Estado |
|---------|----------------------|--------|
| `docs/static/img/branding/favicon.ico` | ICO multi-size | ⬜ Pendiente |
| `docs/static/img/branding/frigate.png` | Ver diseño | ⬜ Pendiente |
| `docs/static/img/frigate-autotracking-example.gif` | Ver diseño | ⬜ Pendiente |
| `docs/static/img/plus/fedex-logo.jpg` | SVG vectorial | ⬜ Pendiente |
| `web/images/branding/apple-touch-icon.png` | 180×180 px | ⬜ Pendiente |
| `web/images/branding/favicon-16x16.png` | 16×16 px | ⬜ Pendiente |
| `web/images/branding/favicon-32x32.png` | 32×32 px | ⬜ Pendiente |
| `web/images/branding/favicon.ico` | ICO multi-size | ⬜ Pendiente |
| `web/images/branding/favicon.png` | ICO multi-size | ⬜ Pendiente |
| `web/public/images/apple-touch-icon.png` | 180×180 px | ⬜ Pendiente |
| `web/public/images/maskable-icon.png` | Ver diseño | ⬜ Pendiente |

---

## 🚀 Comandos Post-Rebranding

```bash
# 1. Reemplazar imágenes con assets de SecureCorp Mexico

# 2. Si el módulo Python fue renombrado, actualizar pyproject.toml:
# [tool.poetry.scripts]
# securevu = 'securevu.__main__:main'

# 3. Reconstruir el frontend
cd web && npm install && npm run build

# 4. Construir la imagen Docker
docker build -t securevu:latest .

# 5. Verificar que el módulo Python importa correctamente
docker run --rm securevu:latest python -c "import securevu; print('OK')"

# 6. Mantener topic_prefix en 'frigate' en config.yml si ya está en producción:
# mqtt:
#   topic_prefix: frigate

# 7. Commit y push
git add . && git commit -m "rebrand: Frigate -> SecureVu (SecureCorp Mexico)"
git push origin main
```