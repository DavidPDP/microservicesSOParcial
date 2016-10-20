# microservicesSOParcial
<b>Autor:</b> Johan David Ballesteros <br>
<b>Código:</b>13103036 <br>
<b>Repositorio:</b> https://github.com/DavidPDP/microservicesSOParcial

---

##Supuestos

Antes de la realización de este parcial, se tienen los siguientes supuestos: <br>
* Se ha instalado las librerías. nano, man y git. 
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

##Creación de los servicios

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

![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/Change.PNG)

```sh
# cd /etc/sysconfig/
# nano iptables
```
Procedemos a reiniciar el servicio de iptables.

![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/IpTables.PNG)

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
<b> Método GET </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/Uno.PNG) <br>
<b> Método POST </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/Dos.PNG) <br>
<b> Método PUT </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/Tres.PNG) <br>
<b> Método DELETE </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/Cuatro.PNG) <br>

### /files/recently_created
<b> Método GET </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/UnoA.PNG) <br>
<b> Método POST </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/DosA.PNG) <br>
<b> Método PUT </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/TresA.PNG) <br>
<b> Método DELETE </b> <br>
![alt text](https://github.com/DavidPDP/microservicesSOParcial/blob/master/images/CuatroA.PNG) <br>

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
##Códigos Fuente

<b> files.py </b>

```python
from flask import Flask, abort, request
import json

from files_commands import get_all_files, add_file, remove_file, get_recently_files

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/files',methods=['POST'])
def create_file():
  contentJson = request.get_json(silent=True)
  filename = contentJson['filename']
  content  = contentJson['content']
  if not filename or not content:
    return "empty username or content", 400
  if add_file(filename,content):
    return "HTTP 201 CREATE", 201
  else:
    return "error while creating file", 400

@app.route(api_url+'/files',methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route(api_url+'/files',methods=['PUT'])
def update_file():
  return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/files',methods=['DELETE'])
def delete_file():
  error = False
  error = remove_file()
  if error:
    return 'HTTP 200 OK', 200
  else:
    return 'HTTP 400 error', 400

@app.route(api_url+'/files/recently_created',methods=['GET'])
def read_recent_file():
  list = {}
  list["files"] = get_recently_files()
  return json.dumps(list), 200

@app.route(api_url+'/files/recently_created',methods=['POST'])
def create_recent_file():
  return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/files/recently_created',methods=['PUT'])
def update_recent_file():
  return "HTTP 404 NOT FOUND", 404

@app.route(api_url+'/files/recently_created',methods=['DELETE'])
def delete_recent_files():
  return "HTTP 404 NOT FOUND", 404


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
```
<b> files_command.py </b>

```python
from subprocess import Popen, PIPE

def get_all_files():
  process = Popen(["ls","/home/filesystem_user"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in process.stdout.readlines()]
  return filter(None, file_list)

def add_file(filename,content):
  process = Popen(["touch", "/home/filesystem_user/" + filename], stdin=PIPE, stdout=PIPE, stderr=PIPE)
  log = open("/home/filesystem_user/" + filename, 'w')
  log.write(content)
  log.flush()
  return True if filename in get_all_files() else False


def remove_file():
  deleteCommand = 'find /home/filesystem_user -type f -maxdepth 1 -not -name ".*" -exec rm {} \;'  	
  process = Popen(deleteCommand, universal_newlines=True, shell=True, stdout=PIPE, stderr=PIPE).communicate()
  return True

def get_recently_files():
  process = Popen(["ls","/home/filesystem_user","-1t"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in process.stdout.readlines()]
  file_list = file_list[:3]
  return filter(None, file_list)
  ```
  
