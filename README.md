# microservicesSOParcial
<b>Autor:</b> Johan David Ballesteros <br>
<b>Código:</b>13103036 

---

##Supuestos

Antes de la realización de este parcial, se tienen los siguientes supuestos: <br>
* Se ha instalado las librerías. nano, man, git, 
* Se ha generado el token "parcial", que por seguridad se entenderá que "parcial" es el token.

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

URIs.

|   |POST   |GET   |PUT   |DELETE   |
|---|---|---|---|---|
| /files  | Crear archivo  | Obtener listado de archivos  | No aplica | Elimina todos los archivos  |
| /files/recently_created  | No aplica  | Retorna los archivos que se crearon recientemente  | No aplica | No aplica  |

Formatos de envío de las solicitudes.

|   |POST   |GET   |PUT   |DELETE   |
|---|---|---|---|---|
| /files  | JSON  | No aplica  | No aplica  | No aplica  |
| /files/recently_created  | No aplica  | No aplica  | No aplica  | No aplica  |

Formatos de respuesta de las solicitudes.

|   |POST   |GET   |PUT   |DELETE   |
|---|---|---|---|---|
| /files  | HTTP 201 CREATED | JSON | HTTP 404 NOT FOUND | HTTP 200 OK |
| /files/recently_created  | HTTP 404 NOT FOUND | JSON  | HTTP 404 NOT FOUND | HTTP 404 NOT FOUND |

Se procede a crear un directorio donde se alojarán los archivos .py con los métodos de los servicios que cumplan los anteriores contratos.

```sh
$ cd ~/
$ mkdir microservicesParcial
```
Se proceden a crear los siguientes archivos: <br>

<b> files.py </b> : [Vista del archivo](https://github.com/DavidPDP/microservicesSOParcial/blob/master/services_parcial/files.py) <br>

<b> files_commands.py </b> : [Vista del archivo](https://github.com/DavidPDP/microservicesSOParcial/blob/master/services_parcial/files_commands.py) <br>

##Habilitar Puertos

Una vez creado los archivos .py, se procede a activar los puertos.

```sh
# cd /etc/sysconfig/
# nano iptables
```
Procedemos a reiniciar el servicio de iptables.

[!alt text]()

##Pruebas con PostMan

Ahora proseguimos a probar los servicios creados por medio de la herramienta PostMan. <br>

A continuación se muestran los formatos tipo JSON (intercambio de datos).

```json
{
  "filename": "carta",
  "content": "this is the file content"
}
```

```json
{
  "files": [
    "carta",
    "listado",
    "tareas",
    "recordatorio"
  ]
}
```
### /files
<b> Método GET </b>
[!alt text]()
<b> Método POST </b>
[!alt text]()
<b> Método PUT </b>
[!alt text]()
<b> Método DELETE </b>

### /files/recently_created
<b> Método GET </b>
[!alt text]()
<b> Método POST </b>
[!alt text]()
<b> Método PUT </b>
[!alt text]()
<b> Método DELETE </b>

##Envío de la solución por GitHub

Ahora comprobado los servicios, se procede a subir la solución al repositorio ubicado en GitHub.

```sh
$ cd ~/
$ mkdir repositories
$ cd repositories
$ git clone https://github.com/DavidPDP/microservicesSOParcial.git
$ git config remote.origin.url "https://parcial@https://github.com/DavidPDP/microservicesSOParcial"
$ cd ~/
$ cp microservicesParcial repositories/microservicesSOParcial
$ cd repositories
$ git add microservicesParcial
$ git commit -m "Se adjunta la solución del parcial uno de la asignatura Sistemas Operativos"
$ git push origin master
```
