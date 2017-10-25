from items import *
from map import rooms
from questlog import *

name = ["Kirill", "Sidorov"]

inventory = [item_badge]

# Start game at the reception
current_room = rooms["Office"]

current_time = basic_time(14, 00)
quest_log = log()