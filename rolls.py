import random
import time
import settings

from fileLibs import log

def do_roll_pole(character, pole, multiplier = 1):
    outcomes = list(roll_pole(character,pole,multiplier))

    log(f'{character["name"]} roll outcome: {str(outcomes)}')

    print("Outcome:")
    i = 1
    for outcome in outcomes:

        print( "Roll " + str(i) + ": " + outcome )
        i = i + 1

    input("Enter to continue: ")

def roll_high(number, pole, specialty):
    def roll(x):
        if x == number and specialty:
            return None
        elif x < number:
            return True
        else:
            return False
    return roll

def roll_low(number, pole, specialty):
    def roll(x):
        if x == number and specialty:
            return None
        elif x < number:
            return True
        else:
            return False
    return roll

def str_roll(roll):
    if roll == None:
        return "INSIGHT!!!"
    elif roll:
            return "Success!"
    else:
        return "Fail!"

def roll_pole(character, pole, multiplier = 1 ):

    # Do Rolls
    rolls = []
    for _ in range(multiplier):
        rolls.append(random.randint(1,6))

    log(f'{character["name"]} rolled {str(rolls)}.')

    specialty = character["pole"].upper() == pole.upper()
    char_number = character["number"]

    #print("DEBUG:: pole:" + pole + " num:" + str(char_number) + " sp:" + str(specialty) + " rls:" + str(rolls))

    outcomes = []

    if pole.upper() == settings.high_pole.upper():
        outcomes = map( roll_high(char_number,pole,specialty) , rolls)

    else:
        outcomes = map( roll_low(char_number,pole,specialty) , rolls)

    return map( str_roll, outcomes )
