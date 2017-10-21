from items import *
from map import rooms
from questlog import *

name = ["Kirill", "Sidorov"]

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

current_time = basic_time(13, 49)
quest_log = log()

start_tip = create_tip_from_file(1, "Your subconscious", current_time)
quest_log.add_tip(start_tip)