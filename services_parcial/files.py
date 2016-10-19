from flask import Flask, abort, request
import json

from files_commands import get_all_files, add_file, remove_file

app = Flask(__name__)
api_url = '/v1.0'

@app.route(api_url+'/files',methods=['POST'])
def create_file():
  contentJson = request.get_json(silent=True)
  filename = content['filename']
  content  = content['content']
  if not filename or not content:
    return "empty username or content", 400
  if filename in get_all_files():
    return "The file already exist", 400
  if add_file(filename,content):
    return "user created", 201
  else:
    return "error while creating file", 400

@app.route(api_url+'/files',methods=['GET'])
def read_file():
  list = {}
  list["files"] = get_all_files()
  return json.dumps(list), 200

@app.route(api_url+'/files',methods=['PUT'])
def update_file():
  return "not found", 404

@app.route(api_url+'/files',methods=['DELETE'])
def delete_file():
  error = False
  for filename in get_all_files():
    if not remove_file(filename):
        error = True

  if error:
    return 'some files were not deleted', 400
  else:
    return 'all files were deleted', 200

if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')
