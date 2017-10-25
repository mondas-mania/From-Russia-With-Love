from items import items_dict
from map import rooms
from questlog import *

player = {
    "name": ["Kirill", "Sidorov"],
    "inventory": [items_dict["badge"], items_dict["wallet"]],
    "health": 1500,
    "ammo": 3
}

fighter_bodyguard = {
    "name": ["Frank", "Johnson"],
    "inventory": [items_dict["gun"]],
    "health": 10,
    "ammo": 3
}

fighter_wai = {
    "name": ["Jing", "Wu"],
    "inventory": [items_dict["gun"]],
    "health": 250,
    "ammo": 3
}


# Start game at the reception
current_weather = ""
current_room = rooms["Station"]

current_time = basic_time(14, 00)
quest_log = log()



