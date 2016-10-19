from subprocess import Popen, PIPE

def get_all_files():
  grep_process = Popen(["ls","/home/filesystem_user"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in p.stdout.readlines()]
  return filter(None, file_list)

def add_file(filename,content):
  finalContent = '+ content +'
  add_process = Popen(["echo",finalContent,">", filename], stdout=PIPE, stderr=PIPE)
  add_process.wait()
  return True if filename in get_all_files() else False

def remove_file(filename):
    remove_process = Popen(["sudo","rm","-r",filename], stdout=PIPE, stderr=PIPE)
    remove_process.wait()
    return False if username in get_all_files() else True

def get_recently_files():
  grep_process = Popen(["ls","/home/filesystem_user"], stdout=PIPE, stderr=PIPE)
  file_list =  [path.rstrip('\n') for path in p.stdout.readlines()]
  file_list = file_list[:10]
  return filter(None, file_list)
