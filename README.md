# microservicesSOParcial
<b>Autor:</b> Johan David Ballesteros <br>
<b>Código:</b>13103036 

---


##Preparación Del Ambiente De Trabajo

<b>Creación del usuario</b>

Se procede a crear el usuario filesystem_user con su respectiva contraseña.

```sh
# useradd filesystem_user
# passwd filesystem_user
```
<b>Activación de permisos</b>

Se adiciona el usuario filesystem_user al grupo del administrador(root).

```sh
# usermod -G wheel filesystem_user
# visudo
Se adiciona al visudo la siguiente línea: filesystem ALL=(ALL) ALL
```
<b>Cración y activación del ambiente</b>

Se procede a crear el directorio enviroments dentro del home de filesystem_user. Siguiente a esto se instala el ambiente virtual. Por último se activa el ambiente virtual creado.

```sh
$ mkdir enviroments
$ cd enviroments
$ virtualenv flask_env
$ cd ~/envs
$ . flask_env/bin/activate
```

Ahora se procede a instalar las librerías Flask.

```sh
$ pip install Flask
$ pip freeze > requirements.txt
$ pip install -r requirements.txt
```



