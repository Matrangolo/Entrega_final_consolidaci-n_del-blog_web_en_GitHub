
# Blog de Python con Django

Proyecto final de la Diplomatura de Python de Coderhouse.

## Descripción

Aplicación web desarrollada con Python y Django que permite crear, visualizar, editar y eliminar publicaciones de un blog.

El sistema cuenta con autenticación de usuarios, perfiles y carga opcional de imágenes.

## Tecnologías utilizadas

- Python
- Django
- SQLite
- HTML y CSS
- Pillow
- python-decouple

## Funcionalidades

- Registro de usuarios.
- Inicio y cierre de sesión.
- Perfil de usuario.
- Listado de publicaciones.
- Vista detallada de cada publicación.
- Creación de publicaciones.
- Edición y eliminación de publicaciones.
- Carga opcional de imágenes.
- Estados de publicación: borrador y publicado.
- Protección de vistas mediante autenticación.
- Restricción de edición y eliminación al autor.
- Panel de administración de Django.

## Instalación

### 1. Clonar el repositorio

```bash
git clone URL_DEL_REPOSITORIO
cd blog_python_coderhouse
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows (PowerShell):

```powershell
.\venv\Scripts\Activate.ps1
```

En Linux o macOS:

```bash
source venv/bin/activate
```

### 4. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 5. Configurar las variables de entorno

Crear un archivo `.env` en la raíz del proyecto siguiendo `.env.example`.

Debe contener:

```dotenv
SECRET_KEY=tu_clave_secreta
```

Para generar una clave segura:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

### 6. Aplicar las migraciones

```bash
python manage.py migrate
```

### 7. Crear un superusuario (opcional)

```bash
python manage.py createsuperuser
```

### 8. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

http://127.0.0.1:8000/

## Rutas principales

- `/` — Inicio del blog.
- `/post/crear/` — Crear publicación.
- `/accounts/registro/` — Registro de usuarios.
- `/accounts/login/` — Inicio de sesión.
- `/accounts/perfil/` — Perfil de usuario.
- `/admin/` — Panel administrativo.

## Consideraciones

- La base de datos SQLite se genera localmente.
- Las imágenes se guardan en la carpeta `media/`.
- La carpeta `media/`, el archivo `.env` y la base de datos local no se incluyen en el repositorio.
- El proyecto está configurado para ejecutarse en un entorno de desarrollo local.

## Autor

Valentín Matrangolo

Proyecto desarrollado para la Diplomatura de Python de Coderhouse.
