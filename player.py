from items import *
from map import rooms
from time_system import *
from questlog import *

name = ["", ""]

inventory = [item_id, item_laptop, item_money]

# Start game at the reception
current_room = rooms["Reception"]

current_time = basic_time(13, 49)
quest_log = log()
quest_log.add_tip(tip("You should head to your desk to pick up your assignments.", "Your subconscious", current_time))
quest_log.add_tip(tip("Read them dude", "Your subconscious", current_time))
#quest_log.print_tips()
