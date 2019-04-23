# Python Libs
import time
import json
import datetime

# Custom Libs
from printLibs import menu,  clear
from inputLibs import get_upper,  get_string
from fileLibs import load_file,  save_file,  log

# Game Functions
from create import do_create_character,  do_add_note
from rolls import do_roll_pole

from views import do_view_characters,  do_select_character,  do_character_list,  do_set_multiplier,  do_set_pole,  print_character

# Settings system
import settings

####################################################

debug = False
settings.init()

characters = []

if debug:
    characters.append({"realname": "Bob",  "name": "Super Dan",  "role": "Hero",  "pole": settings.high_pole,  "number": 4,  "goal": "Observe and protect.",  "notes": []})
    characters.append({"realname": "Dave",  "name": "The Mole",  "role": "Hero",  "pole": settings.low_pole,     "number": 4,  "goal": "To dig out crime.",  "notes": []})

## MENUS ###########################################

def main_menu():

    global characters

    clear()

    do_character_list(characters)

    menu("Main Menu", [
        "CC. Create Character",
        "VA. View All Characters",
        "VC. View Character",
        "RP. Roll pole",
        "NT. Add notes",
        "SV. Save",
        "LD. Load",
        "QT. Quit",
    ], "=")
    response = get_upper("Option")

    if response == "CC":
        character = do_create_character()
        characters.append(character)
        log(f'Created character: {character["name"]} ({character["realname"]})')

    elif response == "VA":
        do_view_characters(characters)

    elif response == "VC":
        character = do_select_character(characters)
        if character == None:
            return True

        print_character(character)
        input("Enter to continue: ")

    elif response == "RP":
        character = do_select_character(characters)
        if character == None:
            return True

        pole = do_set_pole()
        if pole == None:
            return True

        multiplier = do_set_multiplier()    

        do_roll_pole(character, pole, multiplier) 

    elif response == "NT":
        character = do_select_character(characters)
        if character == None:
            return True

        do_add_note(character)
        log(f'Added a note to {character["name"]}.')

    elif response == "SV":
        name = get_string("File")
        js = json.dumps(characters)
        save_file(name, js)
        log(f'Saved "{name}".')

    elif response == "LD":
        name = get_string("File")
        js = load_file(name)
        characters = json.loads(js)
        log(f'Loaded "{name}".')

    elif response == "QT":
        return False
    
    else:
        print("Not an option.")
        time.sleep(1)
    
    return True

## MAIN LOOP #######################################

log("Menu initialized...")
loop = True
while(loop):
    loop = main_menu()

## EOF #############################################