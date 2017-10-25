from players import *
from random import randint
from time import sleep
# CHANGE WEAPON DURING FIGHT##
# BLOCKING FEATURE ADDITION##


# CHANGE WEAPON DURING FIGHT##
def hitpoints(a, b):
    return randint(1, 3)*(randint(a, b))


def attacking(fighter, player_weapon, fighter_weapon):
    dmg_multiplier = {"fists": 1, "gun": 5, "shank": 3}
    player_dmg_multiplier = dmg_multiplier[player_weapon]
    fighter_dmg_multiplier = dmg_multiplier[fighter_weapon]

    fighter_hit = hitpoints(3, 9) * fighter_dmg_multiplier
    sleep(0.5)
    player_hit = hitpoints(3, 9) * player_dmg_multiplier
    if fighter_hit >= (7 * fighter_dmg_multiplier) and player_weapon != "fists":
        print("Your weapon got knocked out of your hand onto the floor!")
        player["inventory"].remove(items_dict[player_weapon])
        current_room["items"].append(items_dict[player_weapon])
    elif player_hit >= (8 * player_dmg_multiplier) and fighter_weapon != "fists":
        print("Their weapon got knocked out of their hand onto the floor!")
        fighter["inventory"].remove(items_dict[fighter_weapon])

    player["health"] -= fighter_hit
    fighter["health"] -= player_hit


def choose_weapon(fighter):
    weapons = [items_dict["gun"].id, items_dict["shank"].id]
    print("You have: ")
    for items in player["inventory"]:
        if items.id in weapons:
            print(items.id.upper() + ",")
    print("FISTS")
    choose = None
    while not choose:
        print("Which weapon would you like to use?")
        input_text = input("> ").lower().strip()
        if input_text in weapons or input_text == "fists":
            choose = input_text
    if items_dict["gun"] in fighter["inventory"] and fighter["ammo"] > 0:
        fighter_weapon = "gun"
        fighter["ammo"] -= 1
    elif items_dict["shank"] in fighter["inventory"]:
        fighter_weapon = "shank"
    else:
        fighter_weapon = "fists"

    if choose == "gun":
        player["ammo"] -= 1

    attacking(fighter, choose, fighter_weapon)


def print_stats(fighter):
    # Print out battle stats
    print("----- STATS -----")
    print(" ".join(str(x) for x in player["name"]))
    print("Health is " + str(player["health"]))
    if items_dict["gun"] in player["inventory"]:
        print("Ammo is " + str(player["ammo"]))
    print("-----")

    print(" ".join(str(x) for x in fighter["name"]))
    print("Health is " + str(fighter["health"]))
    if items_dict["gun"] in fighter["inventory"]:
        print("Ammo is " + str(fighter["ammo"]))
    print("-----------------" + "\n")
    choose_weapon(fighter)


def fight_main(fighter):
    win = False
    while player["health"] >= 0 and fighter["health"] >= 0:
        print_stats(fighter)

    if player["health"] < 0:
        print(fighter["name"][0] + " wins the fight!")
        print("Bad luck!")
    elif fighter["health"] < 0:
        print("You win the fight!")
        win = True

    return win


# fight_main(fighter_bodyguard)
