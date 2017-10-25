class item:
    def __init__(self, id, name, inspect, mass):
        self.id = id
        self.name = name
        self.inspect = inspect
        self.mass = mass


class room_object:
    def __init__(self, id, name, interact, inspect):
        self.id = id
        self.name = name
        self.interact = interact
        self.inspect = inspect

    def call_interact(self):
        if type(self.interact) == str:
            print(self.interact)
        else:
            self.interact()


# Items can be added in the following format:
badge_inspect = """A slightly grubby badge showing that you are part of the CPD"""
item_badge = item("badge", "police badge", badge_inspect, 0.100)

coffee_inspect = "You can already tell it's going to be a long day."
item_coffee = item("coffee", "cup of coffee", coffee_inspect, 0.150)

gun_inspect = "Safety is on, fully loaded, no history of jamming. Couldn't ask for a more reliable weapon."
item_gun = item("gun", "pistol", gun_inspect, 0.800)

shank_inspect = "Careful! Someone could get hurt with this."
item_shank = item("shank", "crude shank", shank_inspect, 0.400)

wallet_inspect = "Plenty cash to go about your day with, with an ID with a rather unflattering image of yourself."
item_wallet = item("wallet", "wallet", wallet_inspect, 0.700)

notepad_inspect = "Your notepad where you have your assignment and notes written down."
item_notepad = item("notepad", "notepad", notepad_inspect, 0.400)

blueprints_inspect = "These seem to be blueprints to Wai's club - could be useful to get to know it."
item_blueprints = item("blueprints", "blueprints to the club", blueprints_inspect, 0.100)

burnt_inspect = """There are only tiny patches where the font is legible despite the burning - 
you can make out a 'J', a 'n' and a 'Wu'. Maybe it was a message sent to Wai Wu, or information about them"""
item_burnt = item("paper", "pieces of burnt paper", burnt_inspect, 0.001)


# Objects can be added in a similar way, and are unmovable things in rooms that add a bit of variety to each room
rug_interact = "You step on the rug and hear the floor creak as normal."
rug_inspect = """A perfectly normal rug"""
obj_rug = room_object("rug", "worn rug", rug_interact, rug_inspect)

clock_interact = "As much as you wish it was time to go home, you probably shouldn't change the time."
clock_inspect = "You see it is broken, what a shame... At least you have a watch on."
obj_clock = room_object("clock", "wall-mounted clock", clock_interact, clock_inspect)

coffee_machine_interact = "You already got a cup earlier, surely you can't want another already?"
coffee_machine_inspect = "It looks like it's been well used."
obj_coffee_machine = room_object("brew", "coffee pot", coffee_machine_interact, coffee_machine_inspect)

desk_interact = "You find old paperwork that you've been too busy to file away."
desk_inspect = "A messy desk with whatever you need for your normal day."
obj_desk = room_object("desk", "messy desk", desk_interact, desk_inspect)

# This dictionary just relates the 'simple name' to the item object
# Add any new items to the dictionary like this
items_dict = {
    item_badge.id: item_badge,
    item_coffee.id: item_coffee,
    item_gun.id: item_gun,
    item_shank.id: item_shank,
    item_wallet.id: item_wallet,
    item_notepad.id: item_notepad,
    item_blueprints.id: item_blueprints,
    item_burnt.id: item_burnt,
    obj_rug.id: obj_rug,
    obj_clock.id: obj_clock,
    obj_coffee_machine.id: obj_coffee_machine,
    obj_desk.id: obj_desk
}