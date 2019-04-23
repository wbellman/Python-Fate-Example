## Imports #######################################
from os import name, system

##################################################

# MENU ###########################################
def menu(name,options,menu_border = "-"):
  printc(" " + name + " ", menu_border)
  for option in options:
    printl( " " + option )
  printc("", menu_border)

# SCREEN FUNCTIONS ###############################
def clear():
  if name == "nt":
    system("cls")
  else:
    system("clear")

# PRINT FUNCTIONS ################################
def printl( str, fill=" ", chars = 40):
  print(str.ljust(chars,fill))

def printc( str, fill=" ", chars = 40):
  print(str.center(chars,fill))

def printr( str, fill=" ", chars = 40):
  print(str.rjust(chars,fill))

# EOF #############################################