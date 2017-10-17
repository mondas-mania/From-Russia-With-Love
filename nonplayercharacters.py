from items import *
from map import rooms


class npc:
    def __init__(self, name, inventory, room, description):
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
        return name_txt

    def inv_list(self):
        inv = []
        for items in self.inventory:
            inv.append(items.name)
        return inv


jing_desc = "The surprisingly enthusiastic receptionist here at the station."
npc_jing = npc("Jing Wu", [item_pen, item_biscuits], rooms["Reception"], jing_desc)
