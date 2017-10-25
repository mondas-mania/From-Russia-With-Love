from players import *
from gameparser import *
from items import *
import math
from random import randint
from time import sleep

# BLOCKING FEATURE ADDITION##
# Need to add this to game.py if in certain room. Variable to check whether or not we have already fought. 


def hitpoints(a,b):
    return randint(1,3)*(randint(a, b))

def randomwep():
    #chooses a random weapon out of the bodyguards inventory
    weaponnum = randint(0, len(bodyguard["inventory"]))
    weaponnum -= 1
    #makes a random number between 0 and length of inventory -1
    chosenweapon = str(bodyguard["inventory"][weaponnum])
    #chose item with random number out of inventory
    print ("Bodyguard chose " + chosenweapon)


    #for the num chosen, change damage 
    if weaponnum == 0 and bodyguard["ammo"] >0:
        bodyguard["ammo"] -= 1
        return hitpoints(20,40)
    elif weaponnum == 1:
        return hitpoints(20,30)
    else:
        return hitpoints(10,20)
        

def chooseweapon():
    print ("You have: " + " ".join(str(x) for x in player["inventory"]).upper() + " and you also have your FISTS!")
    print ("You can also BLOCK an attack taking less damage and slightly injure the bodyguard. Use if both on low health!")
    choose = input("Use weapon or block?")

    normalised_user_input = ','.join(normalise_input(choose))

    if normalised_user_input == "gun" and player["ammo"] > 0:
        player["ammo"] -= 1
        attacking(20,40)
    elif normalised_user_input == "fists":
        attacking(10,20)
    elif normalised_user_input == "block": #need to work this out
        blocking(10,20)
    else:
        print ("That is not a valid option. Please try again.")
        chooseweapon()
    
def attacking(c,d):
    #c and d change depending on weapon choice
    player_hit = hitpoints(c,d)
    bodyguard_hit = randomwep()
    
    print ("-----")
    print ("You hit the bodyguard for " + str(player_hit))
    print ("Bodyguard hit you for " + str(bodyguard_hit))
    print ("-----")

    
    player["health"] -= bodyguard_hit
    bodyguard["health"] -= player_hit

    print_stats()

def blocking(c,d):
    #c and d change depending on weapon choice
    player_hit = round(hitpoints(c,d)/2,1) #rounds to 1dp
    bodyguard_hit = round(randomwep()/10,1)
   
    
    print ("----- BLOCKING -----")
    print ("You hit the bodyguard for " + str(player_hit))
    print ("Bodyguard hit you for " + str(bodyguard_hit))
    print ("-----")

    
    player["health"] -= bodyguard_hit #does give strange numbers sometimes
    bodyguard["health"] -= player_hit

    print_stats()

def print_stats():
    # Print out battle stats
    print ("----- STATS -----")
    print (" ".join(str(x) for x in player["name"]))
    print ("Health is " + str(player["health"]))
    print ("Gun ammo is " + str(player["ammo"]))
    print ("-----")

    print (" ".join(str(x) for x in bodyguard["name"]))
    print ("Health is: " + str(bodyguard["health"]))
    print ("Gun ammo is: " + str(bodyguard["ammo"]))
    print ("-----------------" + "\n")
    

def mainfight():
    print ("Welcome to the fight")
    print ("These are your stats for the game"  + "\n")
    print_stats()
    chooseweapon()
    while True:
        if player["health"] and bodyguard["health"] < 0:
            print ("You both died. RIP!")
            False()
        else:
            if player["health"] <= 0:
                print ("Frank wins!")
                False()
            elif bodyguard["health"] <= 0:
                print ("You won!")
                False()
            else:
                chooseweapon()


