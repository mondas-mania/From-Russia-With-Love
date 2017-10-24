from items import *
from map import rooms
from questlog import *

name = ["Kirill", "Sidorov"]

inventory = [item_badge]

current_weather = ""

# Start game at the reception
current_room = rooms["Office"]

current_time = basic_time(13, 49)
quest_log = log()