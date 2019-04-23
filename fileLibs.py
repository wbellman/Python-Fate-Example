import settings
import datetime 

from stringLibs import rpad

def append_file(filename, data):
  with open(filename, "a") as f:
    f.write(data)

def save_file(filename, data):
  with open(filename, "w") as f:
    f.write(data)

def load_file(filename):
  with open(filename, "r") as f:
    data = f.read()
    return data

def log(data):
  now = datetime.datetime.now().time()
  message = f'{rpad(now.hour,2,"0")}:{rpad(now.minute,2,"0")}:{rpad(now.second,2,"0")} - {data}\n'
  append_file(settings.logfile, message )