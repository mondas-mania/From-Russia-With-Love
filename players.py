from items import *
from map import rooms
from questlog import *

player = {
    "name": ["Kirill", "Sidorov"],

    "inventory": [item_gun],

    "description":
    """Do we want a description?""",

    "health": 250,
    "ammo": 3,
}

bodyguard = {
    "name": ["Frank" , "Guard"],

    "inventory": ["gun"],

    "description":
    """Do we want a description?""",

    "health": 250,
    "ammo": 3,
}


# Start game at the reception
current_weather = ""
current_room = rooms["Reception"]

current_time = basic_time(13, 49)
quest_log = log()

start_tip = create_tip_from_file(1, "Your subconscious", current_time)
quest_log.add_tip(start_tip)



