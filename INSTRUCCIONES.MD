Guía de Implementación
Cualquier persona que quiera instalar SecureVu con tus logos deberá seguir estos pasos exactos

Paso 1: Clonación y Rama
Bash
git clone https://github.com/SecureCorp-Mexico/SecureVu.git
cd SecureVu
git checkout rebrand-logos


Paso 2: Construcción de Imagen
Bash
docker compose build
docker compose up -d


Paso 3: Compilación de Interfaz (Crítico)
Debido a que el entorno es de desarrollo, la interfaz debe compilarse manualmente para inyectar los logos:

Bash
docker exec -it frigate-devcontainer bash
cd /workspace/frigate/web
export NODE_OPTIONS="--max-old-space-size=4096" # Evita error de memoria
npm install && npm run build
exit