from items import *
from map import rooms
from termcolor import colored


class npc:
    def __init__(self, id, name, inventory, room, description):
        self.id = id
        self.name = name.split()
        self.inventory = inventory
        self.room = room
        self.description = description

    def add_item(self, item):
        self.inventory += item

    def remove_item(self, item):
        self.inventory.remove(item)

    def info_change(self, new_name, new_desc):
        if new_name != "":
            self.name = new_name

        if new_desc != "":
            self.description = new_desc

    def change_room(self, new_room):
        self.room = new_room

    def full_name(self):
        name_txt = self.name[0] + " " + self.name[1]
        return name_txt.capitalize()

    def inv_list(self):
        inv = []
        for items in self.inventory:
            inv.append(items.name)
        return inv

    def print_dialogue(self, text):
        print(colored(self.full_name() + ": ", attrs=["bold"]) + text)


jing_desc = "The surprisingly enthusiastic receptionist here at the station."
npc_jing = npc("jing", "Jing Wu", [item_coffee], rooms["Reception"], jing_desc)
wai_desc = "The head honcho."
npc_wai = npc("wai", "Wai Wu", [item_gun], rooms["Wai's Secret Room"], wai_desc)
street_1_desc = "Looks like a man in his early twenties hanging around the streets keeping to himself."
npc_street_1 = npc("hoody", "the man with a hoody", [], rooms["Streets"], street_1_desc)
street_2_desc = "Looks like a man in his late forties who would seem at home in an advert on the television."
npc_street_2 = npc("smoker", "the man smoking", [], rooms["Streets"], street_2_desc)
street_3_desc = "Looks like a woman in her late twenties who seems quite shaken and wary of her belongings."
npc_street_3 = npc("walkman", "the woman with a walkman", [], rooms["Streets"], street_3_desc)
thug_alley_desc = """A brutish man who stands guarding an entrance to Wai Wu's club.
You had better not get on his bad side."""
npc_thug_alley = npc("thug", "the thug", [], rooms["Alleyway"], thug_alley_desc)
woman_alley_desc = """You get the feeling she is a prostitute, not that she would ever admit it to a detective,
however that's not of interest today."""
npc_woman_alley = npc("hooker", "potential prostitute", [], rooms["Alleyway"], woman_alley_desc)


npcs = [npc_jing, npc_wai, npc_street_1, npc_street_2, npc_street_3, npc_thug_alley, npc_woman_alley]

