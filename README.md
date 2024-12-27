**Blog de Autos - Proyecto final**

Buenas, les presento mi primer proyecto de programación utilizando python y django. Es un blog sobre autos donde los usuarios pueden ver diferentes vehículos, dar "me gusta" y escribir sobre ellos.
¿Qué puede hacer el sitio?

Para todos los visitantes:

Ver los autos publicados
Leer sobre el dueño de la página en "Acerca de mí"
Leer las publicaciones del blog


Para usuarios registrados:

Dar "me gusta" a los autos
Ver su perfil con los autos que les gustaron
Cambiar su contraseña
Subir una foto de perfil


Para el administrador:

Crear, editar y eliminar autos
Crear y gestionar categorías
Editar la sección "Acerca de mí"
Moderar las publicaciones



Cómo iniciarlo

Primero que nada, asegurarse de tener Python instalado
Clona el repositorio:

bashCopygit clone https://github.com/Gonzagarcia98/blog_autos
cd blog_autos

Crea un entorno virtual e instala lo necesario:

bashCopypython -m venv venv
venv\Scripts\activate  # En Windows
pip install -r requirements.txt

Configura la base de datos:

bashCopypython manage.py migrate

Crea un superusuario (administrador):

bashCopypython manage.py createsuperuser

Inicia el servidor:

bashCopypython manage.py runserver

¡Listo! Entra a http://127.0.0.1:8000/ en tu navegador

Estructura del proyecto

blog/ - App principal con los autos y categorías
accounts/ - App para manejar usuarios y perfiles
media/ - Carpeta donde se guardan las imágenes subidas
templates/ - Archivos HTML

Cosas que aprendí haciendo este proyecto

Cómo usar Django y su sistema de templates
Cómo manejar usuarios y autenticación
Cómo trabajar con bases de datos y modelos
Cómo subir y mostrar imágenes
Cómo usar Git para control de versiones

Para finalizar, mencionar que quedaron algunas cosas pendientes, por ejemplo:

Un sistema de comentarios
Más filtros de busqueda
Y obviamente, mayor estilado y diseño.

Espero que con todo lo que tiene para mejorar, sirva para empezar este camino.

Felices fiestas!!! 
