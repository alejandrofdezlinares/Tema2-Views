Práctica Django: Views y Templates

Descripción

En esta práctica he trabajado con Django para aprender a crear modelos, guardar datos en una base de datos y mostrarlos en páginas web mediante vistas, URLs y templates.

He realizado dos proyectos diferentes utilizando la estructura base del repositorio Tema2-Views.

1. Proyecto de animales de una protectora

Creación de los modelos

Primero, he creado tres modelos con tres atributos cada uno:

Animales: contiene el nombre, el tipo y el cuidador responsable. El cuidador está relacionado con los usuarios de administración de Django mediante una clave foránea.

Protectora: almacena el nombre, la descripción y la fecha de creación.

Colaboradores: guarda el nombre, el cargo y la fecha de entrada en la protectora.

Inserción de datos

Después, he creado registros en la base de datos para cada modelo desde el panel de administración de Django. Para los animales, he creado también un usuario adicional para poder asignar distintos cuidadores.

Creación de vistas, URLs y templates

A continuación, he desarrollado tres vistas, una para cada modelo. Cada vista obtiene todos los registros correspondientes de la base de datos y los pasa mediante una variable al template.

Después, he configurado tres URLs para acceder a las vistas y he creado tres templates HTML para mostrar detalladamente la información de los animales, las protectoras y los colaboradores.

2. Proyecto de una red social de videojuegos

En el segundo proyecto he repetido el mismo procedimiento, pero desarrollando mi propia idea: una red social relacionada con los videojuegos.

Creación de los modelos

He creado tres modelos para organizar la información:

Amigos: permite representar las relaciones de amistad entre usuarios.

Grupos: permite crear grupos y asociar usuarios a ellos.

Videojuegos: almacena información relacionada con los videojuegos.

Inserción de datos

He creado los usuarios necesarios antes de establecer las relaciones de amistad entre ellos.

Para los grupos, he desarrollado mi propio modelo dentro de la aplicación de videojuegos, diferenciándolo de los grupos de administración de Django, que sirven para gestionar permisos y roles de los usuarios.

También he creado registros para los videojuegos y los demás modelos.

Creación de vistas, URLs y templates

Siguiendo el procedimiento del primer proyecto, he creado tres vistas que consultan los registros de cada modelo y pasan los datos a sus respectivos templates.

Después, he configurado tres URLs para acceder a esas vistas y he creado tres plantillas HTML que muestran la información almacenada en la base de datos.

Tecnologías utilizadas

Python: lenguaje utilizado para desarrollar la aplicación.

Django: framework utilizado para crear los modelos, las vistas y las rutas.

Base de datos: almacenamiento de los registros de cada modelo.

HTML y templates de Django: presentación de los datos en páginas web.

Git y GitHub: control de versiones y organización del código mediante ramas.

Organización del repositorio

El repositorio está organizado en las siguientes ramas:

Tema2-Views: contiene la estructura base utilizada en los proyectos.

1.Proyecto_Animales: contiene el proyecto de la protectora de animales.

2.Proyecto_Videojuegos: contiene el proyecto de la red social de videojuegos.

Repositorio: Tema2-Views en GitHub

Conclusión

Con esta práctica he aprendido a crear modelos en Django, introducir y consultar datos en la base de datos, relacionar usuarios con otros modelos y conectar las vistas con las URLs y los templates para mostrar información dinámica en una página web.
