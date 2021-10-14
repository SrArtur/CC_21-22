# Configuración

En este documento detallaremos la configuración de Git y Github siguiendo como referencia [Documentación Hito 0](http://jj.github.io/CC/documentos/proyecto/0.Repositorio). En la que se da por hecho la creación de cuenta en Github así como la instalación de Git. 

## Autenticación en dos pasos

Para incrementar la seguridad de nuestra cuenta de Github podemos (es bastante recomendable) habilitar la autenticación en dos pasos o a partir de su traducción en inglés, segundo factor de autenticación.

Para ello es necesario ir al apartado _Settings_ y a continuación, _Two-Factor authentication_. Tenemos la opción de hacerlo a través de un gestor de contraseñas o por el número de teléfono. Una vez terminado este proceso, ya tendríamos nuestra cuenta más segura.

![](/home/arturo/Imágenes/2FA.png)

## Edición del perfil

Es necesario para la correcta identificación de la persona, añadiendo datos necesarios como el nombre completo, así como ciudad y universidad. Todo este proceso lo podemos hacer en el apartado _Profile_. Se recomienda también cambiar el avatar del perfil.

## Clave SSH

Es importante para conectarte a tu cuenta de Github sin necesidad de iniciar sesión en ese dispositivo.

Para ello, lo primero es crearnos la clave: 
~~~
ssh-keygen -t rsa -b 4096 -C "aoa2eso@gmail.com"
~~~

A continuación, nos pedirá que introduzcamos una _passphrase_. Si la introducimos, nos la pedirá cada vez que intentemos conectarnos por SSH, así que es bastante recomendable introducirla. Podemos comprobar que se ha creado correctamente con el siguiente comando:

~~~
11:52:22 arturo@miair ~ → ls -al ~/.ssh/
total 16
drwx------  2 arturo arturo 4096 oct 14 11:50 .
drwxr-xr-x 22 arturo arturo 4096 oct 14 10:12 ..
-rw-------  1 arturo arturo 3434 oct 14 11:50 id_rsa
-rw-r--r--  1 arturo arturo  743 oct 14 11:50 id_rsa.pub
~~~

El siguiente paso es añadir nuestra clave SSH a Github. Lo podremos hacer en el apartado _SSH and GPG Keyys_ del apartado _Settings_. Debemos introducir un titulo a modo identificador de ese dispositvo y nuestra clave SSH. Para ver la clave podemos hacerlo con el siguiente comando en un terminal:
~~~
cat ~/.ssh/id_rsa.pub
~~~

El resultado, será lo que debemos incluir en el apartado _Key_. Si hemos hecho correctamente este proceso, nos aparece en Github de la siguiente manera:

![](/home/arturo/Imágenes/ssh.png)