
# Declaring the dialogue lists
jing_list = []

npc_name_list = ["", "Jing Wu"]
npc_dict = {
    # Needs to be in the same order as in dialogue.txt and npc_name_list, starting at 1
    1: jing_list
}


def init_dialogue():
    # Can be left alone
    dialogue = open("dialogue.txt", "r")
    dialogue_all = dialogue.readlines()
    dialogue.close()
    character = 0
    for lines in dialogue_all:
        if lines[0] == "#":
            character += 1

        if character != 0:
            npc_dict[character].append(lines)


def print_dialogue(npc, dialogue_id):
    # Can be left alone
    for keys in npc_dict:
        if npc_name_list[keys] == npc.full_name():
            text = npc_dict[keys][dialogue_id]
            npc.print_dialogue(text)
