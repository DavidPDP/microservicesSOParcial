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

<b>Creación de los servicios</b>

Para la creación de servicios se describe los siguientes contratos.

|   |POST   |GET   |PUT   |DELETE   |
|---|---|---|---|---|
| /files  | Crear archivo  | Obtener listado de archivos  | No aplica | Elimina todos los archivos  |
| /files/recently_created  | No aplica  | Retorna los archivos que se crearon recientemente  | No aplica | No aplica  |

Descripción de los formatos de envío de las solicitudes

|   |POST   |GET   |PUT   |DELETE   |
|---|---|---|---|---|
| /files  | JSON  | No aplica  | No aplica  | No aplica  |
| /files/recently_created  | No aplica  | No aplica  | No aplica  | No aplica  |

Descripción de los formatos de respuesta de las solicitudes

|   |POST   |GET   |PUT   |DELETE   |
|---|---|---|---|---|
| /files  | HTTP 201 CREATED | JSON | HTTP 404 NOT FOUND | HTTP 200 OK |
| /files/recently_created  | HTTP 404 NOT FOUND | JSON  | HTTP 404 NOT FOUND | HTTP 404 NOT FOUND |


