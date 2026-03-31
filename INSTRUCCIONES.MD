# 🛡️ Guía de Implementación - SecureVu (SecureCorp Mexico)

Esta guía detalla los pasos necesarios para instalar y desplegar **SecureVu** con la nueva identidad visual y configuraciones de red optimizadas.

---

### 1. Clonación y Preparación del Repositorio
Primero, clona el proyecto y asegúrate de cambiarte a la rama que contiene los logos e iconos corregidos:

```bash
# Clonar el repositorio oficial
git clone [https://github.com/SecureCorp-Mexico/SecureVu.git](https://github.com/SecureCorp-Mexico/SecureVu.git)

# Entrar a la carpeta
cd SecureVu

# Cambiar a la rama de branding
git checkout rebrand-logos


Construcción de la Infraestructura (Docker)
Este paso crea la imagen del sistema e integra los archivos de configuración de red y puertos (5000, 8554, 8555):

Bash
# Construir la imagen de SecureVu
docker compose build

# Levantar los servicios en segundo plano
docker compose up -d


Compilación de la Interfaz Web (PASO CRÍTICO) ⚠️
Para que el logo de los anillos concéntricos y los nuevos iconos aparezcan en el navegador, es obligatorio compilar el frontend dentro del contenedor.

IMPORTANTE: Se asignan 4GB de memoria RAM al proceso para evitar el error JavaScript heap out of memory.

Bash
# 1. Entrar a la terminal del contenedor
docker exec -it frigate-devcontainer bash

# 2. Ir al directorio del código web
cd /workspace/frigate/web

# 3. Aumentar memoria de Node y compilar
export NODE_OPTIONS="--max-old-space-size=4096"
npm install && npm run build

# 4. Salir del contenedor
exit