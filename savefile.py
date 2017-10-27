from players import *
from map import rooms
from questlog import *
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
    global player
    global current_room
    global current_time
    global quest_log

    print_save_files()
    savename = get_file_name("What do you want to name the save? Type cancel to cancel the save.")

    if not savename:
        return
    elif savename == "cancel":
        return

    save = open("Save-Files/" + savename + ".txt", "w", encoding="utf8")
    save.write(str(len(player["inventory"])) + "\n")
    for items in player["inventory"]:
        save.write(items.id + "\n")

    save.write(current_room["name"] + "\n")
    save.write(current_time.display_time() + "\n")

    if "down" in rooms["Drug Den"]["exits"]:
        save.write("True" + "\n")
    else:
        save.write("False" + "\n")
    if secret_uncovered:
        save.write("True" + "\n")
    else:
        save.write("False" + "\n")

    save.write(str(len(quest_log.tip)) + "\n")
    for tips in quest_log.tip:
        save.write(tips.text + " ~ " + tips.source.id + " ~ " + tips.time.display_time() + "\n")

    save.close()


def load_file():
    global player
    global current_room
    global current_time
    global secret_uncovered

    savename = ""
    print_save_files()
    while (savename + ".txt") not in os.listdir("Save-Files/"):
        savename = get_file_name("Which save do you want to load? ")

        if not savename:
            return

        if (savename + ".txt") not in os.listdir("Save-Files/"):
            print(colored("Sorry that save doesn't exist", "red"))

    save = open("Save-Files/" + savename + ".txt", "r", encoding="utf8")

    savelines = save.readlines()
    save.close()
    line_pos = 0
    inv_count = int(savelines[line_pos])
    line_pos = inv_count + 1
    inv_list = savelines[1:line_pos]

    for i in range(0, inv_count):
        inv_list[i] = inv_list[i].rstrip()

    new_inventory = []
    for new_items in inv_list:
        new_inventory.append(items_dict[new_items])

    player["inventory"] = new_inventory

    room_name = savelines[line_pos]
    print("Room = " + room_name)
    for room in rooms:
        if rooms[room]["name"] == room_name:
            current_room = room

    line_pos += 1
    print("Time = " + savelines[line_pos])
    current_time = get_time_from_str(savelines[line_pos])

    if savelines[line_pos + 1] == "True":
        rooms["Drug Den"]["exits"]["down"] = "Den Basement"
    if savelines[line_pos + 2] == "True":
        secret_uncovered = True

    line_pos += 3
    tip_count = int(savelines[line_pos])

    line_pos += 1
    tip_list = savelines[line_pos:line_pos + tip_count + 1]

    quest_log.print_tips()
    quest_log.clear_all()
    for full_tip in tip_list:
        txt = ""
        source = ""
        time_str = ""
        section = 1
        for chars in full_tip:
            if chars == "~":
                section += 1
            elif section == 1 and chars != "~":
                txt += chars
            elif section == 2 and chars != "~":
                source += chars
            elif section == 3 and chars != "~":
                time_str += chars

        new_tip = tip(txt.strip(), source.strip(), get_time_from_str(time_str))
        quest_log.add_tip(new_tip)


# The below lines can be uncommented to test the functionality of the game
# save_file()
# load_file()
# print(str(player["inventory"]))
# quest_log.print_tips()


