# Práctica Django: Views y Templates

## Descripción

En esta práctica he trabajado con Django para crear dos proyectos web, aprendiendo a definir modelos, guardar datos en una base de datos y mostrar esa información mediante vistas, URLs y plantillas HTML (*templates*).

He organizado el trabajo en diferentes ramas de GitHub, utilizando una estructura base común para los dos proyectos.

## 1. Preparación del proyecto

Primero, he utilizado el repositorio de GitHub `Tema2-Views` y he preparado la estructura del proyecto Django.

Los principales comandos utilizados para crear y preparar un proyecto Django son:

# Crear un entorno virtual
python -m venv venv

# Activar el entorno virtual en Windows
venv\Scripts\activate

# Instalar Django
pip install django

# Crear un proyecto Django
django-admin startproject mysite .

# Crear una aplicación
python manage.py startapp protectora

He utilizado la estructura del proyecto para organizar la configuración, las aplicaciones y las rutas de la web.

## 2. Proyecto de animales de una protectora

### Creación de modelos

He creado tres modelos en `models.py`:

- **Animal:** contiene el nombre, el tipo y el cuidador responsable, relacionado mediante una clave foránea con los usuarios de Django.
- **Protectora:** almacena el nombre, la descripción y la fecha de creación.
- **Colaborador:** guarda el nombre, el cargo y la fecha de entrada en la protectora.

### Migraciones de la base de datos

Después de definir los modelos, he utilizado los siguientes comandos para generar y aplicar las migraciones:

python manage.py makemigrations
python manage.py migrate


Estos comandos permiten preparar la base de datos para almacenar la información de los modelos.

### Creación de registros

He accedido al panel de administración de Django para crear registros de animales, protectoras y colaboradores. También he creado un usuario adicional para poder asignar cuidadores a los animales.

Para acceder al panel, he utilizado el servidor de desarrollo:


python manage.py runserver


### Creación de vistas

En `views.py` he creado tres funciones: `animales()`, `protectoras()` y `colaboradores()`.

Cada función utiliza `objects.all()` para obtener todos los registros de su modelo y `render()` para enviar los datos a su plantilla HTML correspondiente.

Por ejemplo:


def animales(request):
    animales = Animal.objects.all()
    return render(
        request,
        'protectora/animales.html',
        {'animales': animales}
    )


### Configuración de URLs

He configurado tres rutas para acceder a las vistas y consultar la información de los animales, las protectoras y los colaboradores.

### Creación de templates

He creado tres plantillas HTML para mostrar los datos obtenidos desde las vistas:

- `animales.html`
- `protectoras.html`
- `colaboradores.html`

De esta forma, cada página muestra la información almacenada en su modelo correspondiente.

## 3. Proyecto de una red social de videojuegos

En el segundo proyecto he repetido el procedimiento anterior, desarrollando mi propia idea: una red social relacionada con los videojuegos.

### Creación de modelos

He creado tres modelos:

- **Amigos:** representa las relaciones de amistad entre usuarios.
- **Grupos:** permite crear grupos y asociar usuarios.
- **Videojuegos:** almacena información relacionada con los videojuegos.

### Inserción de datos

He creado primero los usuarios necesarios para poder establecer las relaciones de amistad. Después, he añadido las amistades y los registros correspondientes a los demás modelos.

Para los grupos, he creado un modelo propio dentro de la aplicación de videojuegos, diferenciándolo de los grupos de administración de Django, que sirven para gestionar permisos y roles.

### Vistas, URLs y templates

He creado tres vistas para consultar los registros de los modelos, tres URLs para acceder a ellas y tres plantillas HTML para mostrar la información.

También he utilizado las migraciones para reflejar los modelos en la base de datos.

## 4. Comandos principales de Django

Estos son los comandos principales utilizados durante el desarrollo y las comprobaciones del proyecto:


# Crear migraciones a partir de los modelos
python manage.py makemigrations

# Aplicar las migraciones
python manage.py migrate

# Crear un superusuario para acceder al administrador
python manage.py createsuperuser

# Iniciar el servidor de desarrollo
python manage.py runserver

El superusuario permite acceder al panel de administración de Django para gestionar los datos.

## 5. Control de versiones con Git y GitHub

He utilizado Git para organizar el trabajo en ramas y GitHub para almacenar el repositorio remoto.

Los comandos habituales para gestionar los cambios son:


# Consultar el estado de los archivos
git status

# Crear y cambiar a una rama
git checkout -b nombre-rama

# Añadir los cambios
git add .

# Crear un commit
git commit -m "Descripción de los cambios"

# Subir la rama al repositorio remoto
git push -u origin nombre-rama


He organizado el trabajo en las siguientes ramas:

- `Tema2-Views`: estructura base.
- `1.Proyecto_Animales`: proyecto de la protectora.
- `2.Proyecto_Videojuegos`: proyecto de la red social.

También he configurado el repositorio para excluir los archivos innecesarios mediante `.gitignore`, manteniendo la base de datos para que se puedan comprobar los registros creados, tal como se solicita en la práctica.
