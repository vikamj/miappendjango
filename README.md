# learn-django
Repositorio para aprender Django

# Instalación de Django

1. Crear entorno virtual y activarlo
2. Instalar Django: 
```
python -m pip install Django
```
3. Ver versión de Django:
```
python3 -m django --version
```
4. Crear proyecto:
```
django-admin startproject <nombre_de_tu_app> .
```
5. Deberías ver una carpeta con el nombre `<nombre_de_tu_app>`

# Servidor de desarrollo

Navegar hasta la ubicación de `manage.py` y ejecutar:
```
python manage.py runserver
```
El servidor abre por defecto en `http://localhost:8000/`

# Crear una app

0. Parar el servidor de desarrollo con `Ctrl + C`
1. Navegamos hasta la ubicación de `manage.py` y ejecutamos:
2. Crear app:
```
python manage.py startapp <nombre_de_tu_app>
```
3. Deberías ver una carpeta con el nombre `<nombre_de_tu_app>`

# Añadir un HTML

Seguir los pasos de [este tutorial](https://www.w3schools.com/django/django_templates.php)

1. Crear `templates` en la carpeta de la app
2. Crear `index.html` o algún HTML en la carpeta `templates`
3. Actualizamos `views.py`:
```python
from django.template import loader
from django.http import HttpResponse

def hello_world(request):
    template = loader.get_template('hello_world.html')
    return HttpResponse(template.render())
```
4. Actualizamos `settings.py`:
```python
INSTALLED_APPS = [
    ...
    '<nombre_de_carpeta_de_app>'
    ]
```
5. Ejecutamos la migración:
```
python manage.py migrate
```
6. Ejecutamos el servidor de desarrollo:
```
python manage.py runserver
```

## Creamos tabla en la base de datos

[Más información](https://www.w3schools.com/django/django_models.php)

**models.py**

```python
from django.db import models

class Member(models.Model):
    id = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
```
- Crea migración: 
```
python manage.py makemigrations members
```
- Ejecuta migración:
```
python manage.py migrate
```
- Ver SQL para crear tabla:
```
python manage.py sqlmigrate members 0001
```
**SQLite3**
- Para ver las tablas en SQLite3, 
A. Desde el `shell` con sqlite3 `<nombre_de_base_de_datos>` -> `.tables`
B. Abrir plugin de SQLite3 en VSCode -> Quick Query -> elegir base de datos y ejecutamos:
```
SELECT name FROM sqlite_master WHERE type='table';
```
Veremos algo como:
```
...
members_member
```
o en mi caso:
```
...
hello_world_app_member
```
**Importante:** No se modifican las tablas de Django.

## Insertar datos en la base de datos

[Más información](https://www.w3schools.com/django/django_insert_data.php)

- Abrimos el shell interactivo de Python y Django:
```
python manage.py shell
```
- Importamos el modelo:
```python
from <nombre_de_la_app>.models import Member
```
* nombre_de_la_app: nombre de la carpeta de la app -> `members` o en mi caso `hello_world_app`

- Creamos un objeto:
```python
member = Member(id=1, firstname='John', lastname='Doe')
```
- Guardamos el objeto:
```python
member.save()
```
- Verificamos que se guardó:
```python
Member.objects.all().values()
```

## Static

1. Creamos carpeta `static` en la carpeta de la **app** -> `hello_world_app/static` o `members`
2. Creamos una hoja de estilos, por ejemplo `main.css` o `style.css`
3. Actualizamos `settings.py`:
```python
STATIC_ROOT = BASE_DIR / 'productionfiles'
STATIC_URL = '/static/'
```
Ejecutamos este comando para generar los `statics`(archivos) de producción:
```
py manage.py collectstatic
```

Se deben generar unos 131 archivos en la carpeta `productionfiles`.

4. Instalamos Whitenoise para servir los statics:
```
pip install whitenoise
```
5. Actualizamos `settings.py`:
```python
MIDDLEWARES = [
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
] 
```
Colocamos DEBUG en `False`:
```python
DEBUG = False
```
6. Añadimos la hoja de estilos en `master.html`:
```
{% load static %}
...
<head>

...
<link rel="stylesheet" href="{% static 'main.css' %}">
...
</head>
```
7. Ejecutamos el servidor de desarrollo:
```
python manage.py runserver
```

## Deploy en PythonAnywhere

1. Crear cuenta en [PythonAnywhere](https://www.pythonanywhere.com/)
2. Crear un nuevo Bash Console -> `Bash Console`
- Subir los archivos del proyecto a PythonAnywhere
```
git clone <URL_repositorio>
```
3. Creamos entorno virtual:
```
python -m venv <nombre_del_entorno>
```
- Activamos el entorno virtual:
```
source <nombre_del_entorno>/bin/activate
```
4. Instalamos Django y los `requirements`.
- Navegamos hasta `requirements.txt` y ejecutamos:
```
pip install -r requirements.txt
```
5. Ejecutar las migraciones de Django:
```
python manage.py migrate
```
--> Tiene que salir todo **OK**

- Generamos los estáticos para producción:
```
python manage.py collectstatic
```
--> Tiene que salir más de 131 archivos, en mi caso 137.

Ahora si haces `python manage.py runserver` y **NO** sale error o warning (aunque la salida la bloquea el servidor), sabemos que todo está bien.

### Crear superuser

[Pasos para crear y ver superusuario](https://stackoverflow.com/questions/45275897/how-to-get-superuser-details-in-django)

```
from django.contrib.auth.models import User

superusers = User.objects.filter(is_superuser=True)
```

Cambiar contraseña:
```
python manage.py changepassword <nombre_de_usuario>
```