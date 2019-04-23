import time
import random
import settings

from inputLibs import get_number, get_upper, get_string

def do_create_character():

  print()

  realname = get_string("Real Name", 9)
  name     = get_string("Name", 9)
  role     = get_string("Role", 9)
  pole     = get_string("Pole", 9)
  number   = get_number("Number", 9)
  goal     = get_string("Goal", 9)

  return {
    'realname': realname,
    'name': name,
    'role': role,
    'pole': pole,
    'number': number,
    'goal': goal,
    'notes': [] 
    }

def do_add_note(character):
  note = get_string("Note")
  character["notes"].append(note)