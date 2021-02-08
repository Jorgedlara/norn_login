# norn_login

## Aplicación para login y registro de usuarios

Se trata de una aplicación web para hacer login, logout, registrar un usuario, tiene la opción de recordar la contraseña mediante un correo electrónico y finalmente acceder a un log de la última vez que se inicio sesión

### Tecnologías usadas

Para construir esta aplicación utilicé Django, un framework construido en python, por su simplicidad y velocidad para diseñar aplicaciones desde 0, conectado a una base de datos PotgreSLQ. 

### Arquitectura

Se utilizó la arquitectura MTV propia del framework, para separar los modelos, los templates y la lógica de la aplicación, los modelos utilizados para hacer login fueron los propios que nos proporciona Django, muy útiles ya que consideran la seguridad en cuanto a validaciones y tokens de acceso. Para la lógica de las aplicaciones se utilizaron tanto vistas basadas en funciones como vistas basadas en clases. 

### Instalar el proyecto 

Para correr el proyecto se necesita tener Python instalado y seguir los siguientes pasos:
-	Clonar el repositorio en local
-	Activar desde consola el entorno virtual source env/bin/activate 
-	Acceder desde consola  a la carpeta del proyecto simple_log
-	Desde consola levantar el servidor con el comando python manage.py runserver
-	El proyecto estará corriendo en la dirección http://localhost:8000/
