# Declaring the dialogue lists
jing_list = []
street1_list = []
street2_list = []
street3_list = []
thug_list = []
hooker_list = []

npc_id_list = ["", "jing", "hoody", "smoker", "walkman", "thug", "hooker"]
npc_dict = {
    # Needs to be in the same order as in dialogue.txt and npc_name_list, starting at 1
    1: jing_list,
    2: street1_list,
    3: street2_list,
    4: street3_list,
    5: thug_list,
    6: hooker_list
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
        if npc_id_list[keys] == npc.id:
            text = npc_dict[keys][dialogue_id]
            npc.print_dialogue(text)
