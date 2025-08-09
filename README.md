# Doggie - Recetas para Perros

Este es un proyecto Django para gestionar y mostrar recetas de comida para perros.

## Características Principales

- Listado y detalle de recetas.
- Gestión de pacientes (mascotas).
- Autenticación de usuarios utilizando `django-allauth`.
- Carga de imágenes para recetas y pacientes.

## Prerrequisitos

- Python 3.13
- Git

## Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone <URL-DEL-REPOSITORIO>
    cd Doggie
    ```

2.  **Crea y activa un entorno virtual:**
    ```bash
    # En Windows
    python -m venv venv
    venv\Scripts\activate

    # En macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

5.  **Crea un superusuario para acceder al admin de Django:**
    ```bash
    python manage.py createsuperuser
    ```

6.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El sitio estará disponible en `http://127.0.0.1:8000`.

## Librerías Clave Utilizadas

- **[Django](https://www.djangoproject.com/):** El framework web utilizado para construir la aplicación.
- **[django-allauth](https://django-allauth.readthedocs.io/en/latest/):** Una aplicación integrada para la autenticación, registro y gestión de cuentas de usuario.
- **[Pillow](https://pillow.readthedocs.io/en/stable/):** Una librería para el manejo y procesamiento de imágenes.

## Estructura del Proyecto

- `recetas/`: La aplicación principal de Django que contiene los modelos, vistas y plantillas para las recetas y pacientes.
- `recetas_perros/`: El directorio de configuración del proyecto Django.
- `media/`: Directorio donde se almacenan las imágenes subidas por los usuarios.
- `db.sqlite3`: El archivo de la base de datos SQLite utilizada para el desarrollo.
