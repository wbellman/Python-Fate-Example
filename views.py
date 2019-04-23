import time
import settings

from printLibs import printl, printc
from inputLibs import get_number

def print_character(character):
  print()
  printc(character["realname"],"-",40)
  print()
  print( character["name"] + " (" + character["role"] + ") -- " + character["pole"].title() + ":" + str(character["number"]) )
  print()
  print( "Goal: " + character["goal"])
  print()
  if len(character["notes"]) > 0:
    print("Notes:")
    n = 1
    for note in character["notes"]:
      print("  " + str(n) + ". " + note )
    print()
  printc("","-",40)
  print()
  print()    

def print_characters(characters,short = True):
  if len(characters) < 1:
    print("No characters defined.")

  i = 1
  for character in characters:
    if short:
      print( str(i) + ". " + character["name"].ljust(20) + " (" + character["realname"] + ")")  
      i = i + 1
    else:
      print_character(character)

def do_character_list(characters):
  printc("Characters", "-")
  print_characters(characters) 
  print()

def do_view_characters(characters):
  printc("Characters", "-")
  print_characters(characters,False) 
  input("Enter to continue: ")

def do_select_character(characters):
  print()
  printl("0. Abort")
  do_character_list(characters)

  number = get_number("Character #")

  if number == 0:
    return None

  number = number - 1

  if number >= len(characters):
    print("Invalid character!")
    return do_select_character(characters)
  
  else:
    return characters[number]

def do_set_multiplier():
  print()
  return get_number("Multiplier")

def do_set_pole():
  print()
  print("0. Abort")
  print("1. " + settings.high_pole)
  print("2. " + settings.low_pole)
  number = get_number("Pole")

  if number == 0:
    return None
  elif number == 1:
    return settings.high_pole
  elif number == 2:
    return settings.low_pole
  else:
    print("Invalid pole.") 
    return do_set_pole()
