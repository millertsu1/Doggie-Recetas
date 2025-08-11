# Doggie - Recetas para Perros

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=plastic&logo=python) ![Django](https://img.shields.io/badge/Django-5.1.3-092E20?style=plastic&logo=django) ![django-allauth](https://img.shields.io/badge/django--allauth-65.7.0-blue?style=plastic) ![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-38B2AC?style=plastic&logo=tailwind-css) ![PostCSS](https://img.shields.io/badge/PostCSS-DD3A0A?style=plastic&logo=postcss) ![daisyUI](https://img.shields.io/badge/daisyUI-1E40AF?style=plastic)

Este es un proyecto Django para gestionar y mostrar recetas de comida para perros.

## Características Principales

- Listado y detalle de recetas.
- Gestión de pacientes (mascotas).
- Autenticación de usuarios utilizando `django-allauth`.
- Carga de imágenes para recetas y pacientes.

## Prerrequisitos

- Python 3.13
- Git
- Node.js (con npm)

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

3.  **Instala las dependencias de Python:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Instala las dependencias de Node.js para Tailwind CSS:**
    ```bash
    cd theme/static_src
    npm install
    ```

5.  **Compila los estilos de Tailwind CSS:**
    ```bash
    # Para desarrollo (con auto-recarga)
    npm run dev

    # Para producción (minificado)
    npm run build
    ```

6.  **Aplica las migraciones de la base de datos:**
    ```bash
    python manage.py migrate
    ```

7.  **Crea un superusuario para acceder al admin de Django:**
    ```bash
    python manage.py createsuperuser
    ```

8.  **Ejecuta el servidor de desarrollo:**
    ```bash
    python manage.py runserver
    ```
    El sitio estará disponible en `http://127.0.0.1:8000`.

## Librerías Clave Utilizadas

- **[Django](https://www.djangoproject.com/):** El framework web utilizado para construir la aplicación.
- **[django-allauth](https://django-allauth.readthedocs.io/en/latest/):** Una aplicación integrada para la autenticación, registro y gestión de cuentas de usuario.
- **[Pillow](https://pillow.readthedocs.io/en/stable/):** Una librería para el manejo y procesamiento de imágenes.
- **[Tailwind CSS](https://tailwindcss.com/):** Un framework de CSS para un diseño rápido y personalizado.
- **[daisyUI](https://daisyui.com/):** Un plugin de Tailwind CSS para componentes de UI.

## Estructura del Proyecto

- `recetas/`: La aplicación principal de Django que contiene los modelos, vistas y plantillas para las recetas y pacientes.
- `recetas_perros/`: El directorio de configuración del proyecto Django.
- `theme/`: La aplicación de Django para gestionar el tema, incluyendo la configuración de Tailwind CSS.
- `media/`: Directorio donde se almacenan las imágenes subidas por los usuarios.
- `db.sqlite3`: El archivo de la base de datos SQLite utilizada para el desarrollo.
