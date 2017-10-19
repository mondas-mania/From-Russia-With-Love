from items import *
from map import rooms
from questlog import log, tip, basic_time

name = ["", ""]

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

current_time = basic_time(10, 0)
quest_log = log()
quest_log.add_tip(tip("You should head to your desk to pick up your assignments.", "Your subconscious", current_time.display_time()))
