#!/usr/bin/python3

from map import rooms
from dialogue import *
from questlog import *
from players import *
from items import *
from gameparser import *
from savefiletesting import save_file, load_file
from termcolor import colored
checkpoint = True


def list_of_items(items):
    str_items = ""
    for item in items:
        str_items = str_items + item.name + ", "

    str_items = str_items[:-2]
    return str_items


def print_room_items(room):
    if room["items"]:
        print("There is " + list_of_items(room["items"]) + " here.")
        print("")


def print_inventory_items(items):
    if items:
        print("You have " + list_of_items(items) + ".")
        print("")


def print_room(room):
    # Display room name
    print("")
    print(room["name"].upper())
    print("")
    # Display room description
    print(room["description"])
    print("")
    # Display room items
    print_room_items(room)


def exit_leads_to(exits, direction):
    return rooms[exits[direction]]["name"]


def print_exit(direction, leads_to):
    print("GO " + direction.upper() + " to " + leads_to + ".")


def print_menu(exits, room_items, inv_items):
    global checkpoint
    print(colored("This is a checkpoint so you can save now if you wish.", attrs=["bold"]))
    print("You can:")
    # Iterate over available exits
    for direction in exits:
        # Print the exit name and where it leads to
        print_exit(direction, exit_leads_to(exits, direction))

    for room_item in room_items:
        # Print the available items in the room to take
        print("TAKE " + room_item.id.upper() + " to take " + room_item.name + ".")

    for inv_item in inv_items:
        # Print the available items in the inventory to drop
        print("DROP " + inv_item.id.upper() + " to drop your " + inv_item.name + ".")

    print("VIEW your quest log.")

    if checkpoint:
        # Allow the user to save their game
        print("SAVE your game.")

    # Allow the user to load the game
    print("LOAD a previous save.")
    
    print("What do you want to do?")
    checkpoint = False


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
        if move(current_room["exits"],direction) != "":
            room = move(current_room["exits"], direction)
            current_room = room
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
        if not inv_too_heavy(player["inventory"] + [item],3):
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
    

def execute_command(command):

    if 0 == len(command):
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")

    elif command[0] == "view":
        quest_log.print_tips()

    elif command[0] == "save":
        save_file()

    elif command[0] == "load":
        load_file()

    else:
        print("This makes no sense.")


def menu(exits, room_items, inv_items):

    # Display menu
    print_menu(exits, room_items, inv_items)

    # Read player's input
    user_input = input("> ")

    # Normalise the input
    normalised_user_input = normalise_input(user_input)

    return normalised_user_input


def move(exits, direction):

    # Next room to go to
    return rooms[exits[direction]]


def story():
    speed = 1
    if item_coffee in player["inventory"]:
        speed *= 1.5
    if current_weather == "":
        speed *= 0.7
    if quest_log.tip[0].text == tips_text_list[1]:
        print("Welcome to the game")


# This is the entry point of our program
def main():
    global tips_text_list
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

    # Main game loop

    while True:
        # Display game status (room description, inventory etc.)
        print_room(current_room)
        print_inventory_items(player["inventory"])
        story()

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], player["inventory"])

        # Execute the player's command
        execute_command(command)


# Are we being run as a script? If so, run main().
# '__main__' is the name of the scope in which top-level code executes.
# See https://docs.python.org/3.4/library/__main__.html for explanation
if __name__ == "__main__":
    main()

