# Pomodoro Rosso

**Pomodoro Rosso** es una aplicación de escritorio desarrollada en Python para facilitar el cálculo de ingredientes necesarios a partir de diversos pedidos. Está diseñada para optimizar la compra y planificación en rotiserías u otros comercios de alimentos.

## Tecnologías usadas

- Python
- Flet (interfaz de usuario)
- SQLite (base de datos local)
- dotenv (manejo de variables de entorno)
- pytest (para pruebas unitarias)

## Instalación

1. Clonar el repositorio:

   ```bash
   git clone https://github.com/rwsilvera/Pomodoro-Rosso.git
   cd Pomodoro-Rosso
   ```

2. Crear y activar un entorno virtual:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate      # En Windows
   source venv/bin/activate    # En Linux/Mac
   ```

3. Instalar las dependencias:

   ```bash
   pip install -r requirements.txt
   ```

## Configuración

El proyecto utiliza un archivo `.env` para definir variables de entorno. Este archivo **no debe subirse** al repositorio y debe estar listado en `.gitignore`.

Ejemplo de contenido del archivo `.env`:

```ini
DB_USER=USUARIO
DB_PASSWORD=CONTRASEÑA
DB_DSN=HOST:PUERTO/SERVICIO
```

Ejemplo de contenido del archivo `.gitignore`:

```gitignore
venv/
.env

__pycache__/
*.py[cod]

.pytest_cache/
```

## Pruebas unitarias

Este proyecto incluye pruebas unitarias utilizando `pytest`.

Para ejecutarlas desde la raíz del proyecto:

```bash
pytest
```

## Base de datos con Docker

Este proyecto utiliza una base de datos que puede levantarse localmente con Docker.

Para iniciar la base de datos, asegurate de tener Docker instalado y ejecutá el siguiente comando:

```bash
docker compose up -d
```

Si necesitás detener los servicios:

```bash
docker compose down
```