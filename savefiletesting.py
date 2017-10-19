from items import *
from player import *
from map import rooms
from time_system import *
from termcolor import colored
import os


def print_save_files():
    directory = os.listdir("Save-Files/")
    print("The existing files are: ")
    for i in range(0, len(directory)):
        directory[i] = directory[i][0:len(directory[i]) - 4]
        print(colored(directory[i], "green"))


def get_file_name(message):
    while True:
        valid_name = True
        print(message + "Type 'cancel' to return to previous menu.")
        input_text = input("> ")

        if input_text.lower() == "cancel":
            return False

        for chars in input_text:
            if not (chars.isalpha() or chars.isdigit()) and chars != "-" and chars != "_":
                valid_name = False

        if valid_name and len(input_text) > 0:
            return input_text

        print(colored("Sorry that isn't a valid name", "red"))


def save_file():
    global inventory
    global current_room
    print_save_files()
    savename = get_file_name("What do you want to name the save? ")

    if not savename:
        return

    save = open("Save-Files/" + savename + ".txt", "w")
    save.write(str(len(inventory)) + "\n")
    for items in inventory:
        save.write(items.id + "\n")

    save.write(current_room["name"])

    save.close()


def load_file():
    global inventory
    global current_room
    savename = ""
    print_save_files()
    while (savename + ".txt") not in os.listdir("Save Files/"):
        savename = get_file_name("Which save do you want to load? ")

        if not savename:
            return

        if (savename + ".txt") not in os.listdir("Save Files/"):
            print(colored("Sorry that save doesn't exist", "red"))

    save = open("Save-Files/" + savename + ".txt", "r")

    savelines = save.readlines()
    inv_count = int(savelines[0])
    inv_list = savelines[1:inv_count + 1]

    for i in range(0, inv_count):
        inv_list[i] = inv_list[i].rstrip()

    new_inventory = []
    for new_items in inv_list:
        new_inventory.append(items_dict[new_items])

    inventory = new_inventory

    room_name = savelines[inv_count + 1]
    for room in rooms:
        if rooms[room]["name"] == room_name:
            current_room = room

    save.close()


basic_time(10, 39).display_time()
save_file()
load_file()


