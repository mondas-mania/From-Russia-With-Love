#!/usr/bin/python3

from dialogue import *
from players import *
from fighter import fight_main
import os
from nonplayercharacters import npcs
from items import items_dict, room_object
from gameparser import *
from savefile import save_file, load_file
from termcolor import colored
checkpoint = True
time_entered = basic_time(0, 0)
rug_moved = False
speed = 1


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def list_of_items(items):
    str_items = ""
    for item in items:
        str_items = str_items + item.name + ", "

    str_items = str_items[:-2]
    return str_items


def print_room_items(room):
    if room["items"]:
        print("There is a " + list_of_items(room["items"]) + " here.")
        print("")


def print_inventory_items(items):
    if items:
        print("You have a " + list_of_items(items) + ".")
        print("")


def print_room(room):
    # Display room name
    print("")
    print(room["name"].upper())
    print("")
    # Display room description
    print(room["description"])
    print("")

    if current_room == rooms["Reception"] and rooms["Reception"]["been"]:
        print(colored("Officer Jing must've clocked out of reception already.", attrs=["bold"]))
        npcs[0].room = rooms["Wai's Secret Room"]
        quest_log.add_tip(create_tip_from_file(3, "Your subconscious", current_time))
    if not current_room["been"]:
        current_room["been"] = True
    # Display room items
    print_room_items(room)


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    global checkpoint
    if checkpoint:
        print(colored("This is a checkpoint so you can save now if you wish.", attrs=["bold"]))
    print("\nYou can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for inv_item in inv_items:
        # Print the available items in the inventory to drop
        print("INSPECT " + inv_item.id.upper() + " to inspect your " + inv_item.name + ".")

    if current_room["checked"]:
        for room_item in room_items:
            # Print the available items in the room to take
            if type(room_item) == room_object:
                print("INSPECT or INTERACT with " + room_item.id.upper() + " to inspect or interact with the " + room_item.name + ".")
            else:
                print("INSPECT or TAKE " + room_item.id.upper() + " to inspect or take the " + room_item.name + ".")
    else:
        print("CHECK the room to see what you find.")

    for characters in npcs:
        if characters.room == current_room:
            if characters.id == "hoody" or characters.id == "smoker" or characters.id == "walkman" or characters.id == "thug" or characters.id == "hooker":
                print("QUESTION or PROFILE " + characters.id.upper() + " to question or profile " + characters.full_name() + ".")
            else:
                print("PROFILE " + characters.id.upper() + " to profile " + characters.full_name() + ".")

    if items_dict["notepad"] in player["inventory"]:
        print("VIEW your quest log.")

    if secret_uncovered and current_room == rooms["Wai's House"]:
        print("FIGHT the bodyguard to enter the secret room.")

    if checkpoint:
        # Allow the user to save their game
        print("SAVE your game.")

    # Allow the user to load the game
    print("LOAD a previous save.")

    print("What do you want to do?")


def is_valid_exit(exits, chosen_exit):
    return chosen_exit in exits


def inv_too_heavy(inv_items, max_mass):
    total_mass = 0
    for items in inv_items:
        total_mass += items.mass

    if total_mass > max_mass:
        return True
    else:
        return False


def execute_go(direction):
    global current_room
    directions = ["north", "south", "east", "west", "up", "down"]

    if direction in directions:
        if move(current_room["exits"], direction) != "":
            previous_room = current_room
            room = move(current_room["exits"], direction)
            current_room = room
            print("")
            if current_room == rooms["Reception"] and not rooms["Reception"]["been"]:
                print(colored("""You walk past reception on your way out and Officer Jing Wu is on reception and says;
"The abandoned warehouse has seen some activity you should probably go check it out in
relation to Wai", so you grab your fedora and trenchcoat and head on to the mean streets
of chicago to catch Wai Wu.
                """, attrs=["bold"]))
                quest_log.add_tip(create_tip_from_file(2, npcs[0], current_time))
            if current_room == rooms["Streets"] and not rooms["Streets"]["been"]:
                print(colored("You decide that this is a good place to start questioning.", attrs=["bold"]))
            if current_room == rooms["Warehouse"] and not rooms["Warehouse"]["been"]:
                print(colored("""You get a feeling when you enter here that this place hasn't been entered for months,
however a tip's a tip, especially when from a friend like Jing, so it's up to you whether to waste even more time here
or to follow the tip up thoroughly""", attrs=["bold"]))
            if current_room == rooms["Warehouse Upper"] and not rooms["Warehouse Upper"]["been"]:
                print("""You reach the horizon of the ladder and your suspicions are confirmed about the lack of 
criminal activity due to the second floor being as barren as the first, however there's a lot to cover.
It's possible there's a clue here somewhere, but it might take time to find, time which you might not have... 
You remind yourself to inform Jing of the bad tip when you next see her""")

            if current_room == rooms["Warehouse"] and previous_room != rooms["Warehouse Upper"]:
                current_time.incr_time(0, 25 / speed)
            elif current_room != rooms["Warehouse Upper"] and previous_room == rooms["Warehouse"]:
                current_time.incr_time(0, 25 / speed)
            else:
                current_time.incr_time(0, 10 / speed)

        else:
            print("You cannot go there.")


def execute_take(item_id):
    item = ""
    global current_room
    global player

    for current_item in current_room["items"]:
        if current_item.id == item_id:
            item = current_item

    if item:
        if not inv_too_heavy(player["inventory"] + [item], 3) and item_id != "rug":
            current_room["items"].remove(item)
            player["inventory"] += [item]
        else:
            print("You cannot take that. It is too much for you to carry.")
    else:
        print("You cannot take that. It is not in the room.")
    

def execute_drop(item_id):
    item = ""
    global current_room
    global player

    for current_items in player["inventory"]:
        if current_items.id == item_id:
            item = current_items

    if item:
        player["inventory"].remove(item)
        current_room["items"] += [item]
    else:
        print("You cannot drop that.")


def execute_question(character):
    if character.room == current_room:
        story_questions(character)
    else:
        print("You cannot question that person.")


def execute_interact(objects):
    global current_room
    interact_object = None
    for current_object in current_room["items"]:
        if current_object.id == objects:
            interact_object = current_object

    if not interact_object:
        print("You cannot interact with that.")
    else:
        interact_object.call_interact()


def execute_profile(character_id):
    to_profile = None
    for characters in npcs:
        if characters.id == character_id:
            to_profile = characters
    if to_profile:
         print(to_profile.description)
    else:
        print("You can't profile that person.")


def execute_inspect(item_id):
    global current_room
    to_inspect = None
    for current_item in player["inventory"]:
        if current_item.id == item_id:
            to_inspect = current_item
    for current_item in current_room["items"]:
        if current_item.id == item_id:
            to_inspect = current_item

    if to_inspect:
        print(to_inspect.inspect + "\n")
    else:
        print("You cannot inspect that.")


def execute_command(command):
    cls()
    continue_story = False
    global current_room

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
            continue_story = True
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
            current_time.incr_time(0, 1 / speed)
        else:
            print("Take what?")

    elif command[0] == "check":
        current_room["checked"] = True
        if current_room == rooms["Warehouse"] or current_room == rooms["Warehouse Upper"]:
            current_time.incr_time(0, 30 / speed)
        else:
            current_time.incr_time(0, 10 / speed)

    elif command[0] == "question":
        success = False
        for characters in npcs:
            if characters.id == command[1]:
                success = True
                execute_question(characters)
                current_time.incr_time(0, 10 / speed)
        if not success:
            print("Question who?")

    elif command[0] == "profile":
        if len(command) > 1:
            execute_profile(command[1])
            current_time.incr_time(0, 2 / speed)
        else:
            print("Question who?")

    elif command[0] == "view":
        if items_dict["notepad"] in player["inventory"]:
            quest_log.print_tips()
        else:
            print("You should pick up your journal from your desk.")

    elif command[0] == "inspect":
        if len(command) > 1:
            execute_inspect(command[1])
        else:
            print("Inspect what?")

    elif command[0] == "interact":
        if len(command) > 1:
            execute_interact(command[1])
            current_time.incr_time(0, 2 / speed)
        else:
            print("Interact with what?")

    elif command[0] == "save":
        save_file()

    elif secret_uncovered and current_room == rooms["Wai's House"] and command[0] == "fight":
        return

    elif command[0] == "load":
        load_file()
        continue_story = True

    else:
        print("This makes no sense.")

    return_list = continue_story
    return return_list


def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)
    user_input = input("> ")
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):
    # Next room to go to
    return rooms[exits[direction]]


def move_rug():
    global checkpoint
    print("You pull away the rug and see an unlocked trap door!")
    rooms["Drug Den"]["exits"]["down"] = "Den Basement"
    checkpoint = True


def secret_room():
    global secret_uncovered
    print("You see a secret room inside Wai's club that you are sure isn't public knowledge.")
    secret_uncovered = True


def story_questions(character):
    if character.id == "hoody" or character.id == "smoker" or character.id == "walkman":
        print_dialogue(character, 1)
        if character.id == "hoody":
            quest_log.add_tip(create_tip_from_file(4, npcs[2], current_time))
        elif character.id == "smoker":
            quest_log.add_tip(create_tip_from_file(5, npcs[3], current_time))
        elif character.id == "walkman":
            quest_log.add_tip(create_tip_from_file(6, npcs[4], current_time))
    elif character.id == "thug" or character.id == "hooker":
        print_dialogue(character, 1)
        if character.id == "thug":
            quest_log.add_tip(create_tip_from_file(7, npcs[5], current_time))
        elif character.id == "hooker":
            quest_log.add_tip(create_tip_from_file(8, npcs[6], current_time))


def story():
    global current_room
    global time_entered
    global rug_moved
    global secret_uncovered
    global speed

    if items_dict["coffee"] in player["inventory"]:
        speed *= 1.5

    if len(quest_log.tip) > 0:
        if quest_log.tip[0].text == tips_text_list[1]:
            print("Welcome to the game. You should CHECK the room around you and find your notepad.")
            quest_log.remove_tip_by_text(tips_text_list[1])
            quest_log.add_tip(create_tip_from_file(9, npcs[0], current_time))
            print("""You sit at your desk in the 5th precinct of the Chicago PD waiting for the next crime to come over your desk,
and by chance it does, in the form of information coming in concerning "Wai Wu" the primary distributor for
the deadly drug Python, they're leaving town tonight and you have to catch them by 8 p.m. later today.
It's currently 2 p.m. and the pressure is on,

You look around the room and see numerous messy desks and a coffee machine
    """)

    if current_room == rooms["Drug Den"] and not rug_moved and not rooms["Drug Den"]["been"]:
        time_entered = get_time_from_str(current_time.display_time())

    if time_entered.hours != 0 and (diff_times(current_time, time_entered).mins >= 10 or diff_times(current_time, time_entered).hours >= 1) and not rug_moved and current_room == rooms["Drug Den"]:
        print("You swear the rug has been moved since last time.")
        rug_moved = True
        items_dict["rug"].interact = move_rug

    if items_dict["blueprints"] in player["inventory"]:
        secret_room()

    if secret_uncovered and current_room == rooms["Wai's House"]:
        print("It seems you must fight the bodyguard if you wish to enter the secret room.")
        print("Now you know where the secret room is, the guards see your newfound drive so reach for their weapons,")
        print("but this doesn't have to end in a firefight yet, not if you play it cool for the time being")
        print("Are you up for a fight, bearing in mind the weapons you have on you?")
        print("FIGHT the bodyguard for access")
        print("CONTINUE to look around the building as normal")
        print("What do you choose?")
        choice = None
        while choice != "fight" and choice != "continue":
            choice = input("> ").lower().strip()
            if choice == "fight":
                cls()
                success = fight_main(fighter_bodyguard)
                if not success:
                    print("""The guards take you down and you succumb to your wounds,
knowing that Wai will escape and ruin more lives""")
                    return False
                else:
                    print("You can save here if you wish:")
                    save_file()
                    rooms["Wai's House"]["exits"]["down"] = "Wai's Secret Room"
                    print("You make sure to have a gun on you before you head down to the secret chamber.")
                    if not items_dict["gun"] in player["inventory"]:
                        player["inventory"].append(items_dict["gun"])
                    current_room = rooms["Wai's Secret Room"]

    if current_room == rooms["Wai's Secret Room"] and current_time.hours < 20:
        cls()
        print("""You look to the middle of the room and behind the desk you see a dark figure
collecting documents and money from a safe. They turn round and they disrobe to reveal
your dearest friend: Jing Wu.
“Aha, You didn’t expect this turn of events did you Sidorov, I was under your nose this
entire time and you couldn’t see it.”
You take out your gun and try to talk Jing down;
“Jing, how could you do this to so many people? I can’t believe I’ve been so blind”.
She jumps backwards and brings out a gun.""")
        quest_log.add_tip(create_tip_from_file(11, "Your subconscious", current_time))
        success = fight_main(fighter_wai)
        if not success:
            print("""Seemingly out of nowhere Jing has a well placed shot that manages to find your torso.
As you begin to bleed out out she collects the remainder of her documents.
“Better luck next time, Sidorov...” she sneers as she locks the secret hatch and leaves you for dead.
You’ve failed and you live with your mistakes before you slowly die""")
            return False
        else:
            print("""You eventually manage to shoot Jing in the shoulder and she collapses to the ground.
You handcuff her. “You’ll regret this Kirill, believe me” she shouts.
You call in backup to bag all the evidence and to take her back to the station.
With the ledger and the evidence contained in the room
you know that “Wai Wu” is going down for a long time""")
            return "won"
    elif current_room == rooms["Wai's Secret Room"] and current_time.hours >= 20:
        print("""You see that the safe behind the desk has already been pillaged and you realise
that you’ve been too late, Wai Wu has moved on to the next city and you’ve failed your assignment.
You feel the shame of knowing you could’ve caught them and that you may never hear of them again
        """)
        quest_log.add_tip(create_tip_from_file(12, "Your subconscious", current_time))
        return False

    return True


# This is the entry point of our program
def main():
    global tips_text_list
    global checkpoint
    intro_text = """ 
 _____  ____   ___   ___ ___      ____  __ __  _____ _____ ____   ____      __    __  ____  ______  __ __      _       ___   __ __    ___ 
|     ||    \ /   \ |   |   |    |    \|  |  |/ ___// ___/|    | /    |    |  |__|  ||    ||      ||  |  |    | |     /   \ |  |  |  /  _]
|   __||  D  )     || _   _ |    |  D  )  |  (   \_(   \_  |  | |  o  |    |  |  |  | |  | |      ||  |  |    | |    |     ||  |  | /  [_ 
|  |_  |    /|  O  ||  \_/  |    |    /|  |  |\__  |\__  | |  | |     |    |  |  |  | |  | |_|  |_||  _  |    | |___ |  O  ||  |  ||    _]
|   _] |    \|     ||   |   |    |    \|  :  |/  \ |/  \ | |  | |  _  |    |  `  '  | |  |   |  |  |  |  |    |     ||     ||  :  ||   [_ 
|  |   |  .  \     ||   |   |    |  .  \     |\    |\    | |  | |  |  |     \      /  |  |   |  |  |  |  |    |     ||     | \   / |     |
|__|   |__|\_|\___/ |___|___|    |__|\_|\__,_| \___| \___||____||__|__|      \_/\_/  |____|  |__|  |__|__|    |_____| \___/   \_/  |_____|
                                                                                                                                                                                                                                                                                 
    """
    print(colored(intro_text, "red", attrs=["bold"]))
    init_dialogue()
    start_tip = create_tip_from_file(1, "Your subconscious", current_time)
    quest_log.add_tip(start_tip)
    living = True
    story()
    # Main game loop
    while True:

        if not living:
            break
        print_room(current_room)
        print_inventory_items(player["inventory"])
        continue_story = False
        while not continue_story:
            print("Time: " + current_time.display_time())
            command = menu(current_room["exits"], current_room["items"], player["inventory"])
            continue_story = execute_command(command)
            living = story()
            if not living or living == "won":
                break
        if checkpoint:
            checkpoint = False

    if not living:
        print("Game over!")
        load_file()
    if living == "won":
        print("CONGRATULATIONS")
        print("YOU STOPPED THE RUTHLESS DRUG DEALER JING 'WAI' WU")


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

