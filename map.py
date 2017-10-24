from items import *

room_reception = {
    "name": "",

    "description":
    """You walk past reception on your way out and Officer Jing Wu is on reception and says; "The abandoned warehouse has seen some activity you should probably go check it out in relation to Big Bill", so you grab your fedora and trenchcoat and head on to the mean streets of chicago to catch Big Bill.
    
    """,

    "exits": {},

    "items": []
}

room_desks = {
    "name": "Your office",
    
    "description":
    """"You sit at your desk in the 5th precinct of Chicago waiting for the next crime to come over your desk, and by chance it does, in the form of information coming in concerning "Big Bill" the primary distributor for the deadly drug python, he's leaving town tonight and you have to catch him by 2a.m the following morning. It's currently 2 p.m and the pressure is on, you have X turns to catch Big Bill and take down his drug cartel”

    """,

    "exits": {},

    "items": []
}

room_den_main = {
    "name": "",

    "description": "You walk through the broken and burned door to find numerous drug addicts scattered around the room like autumn leaves, with the floor coated in blankets and carpets, Bill clearly uses this place to treat his best customers. There is a hollowed out oil drum in the corner that was used recently for a fire, the embers cover the room. You see a somewhat intact piece of paper on the floor. You feel this room is important in your task to take down Big Bill",

    "exits": {},

    "items": []
}

room_den_basement = {
    "name": "",

    "description": "You enter a clean and organised room full of filing cabinets that had clearly been emptied recently. The large desk in the center displays a large blueprint, seemingly of Big Bill’s Pimp House",

    "exits": {},

    "items": []
}

room_streets = {
    "name": "",

    "description": "You see 3 people on the main street outside the station, the street looks clean and well kept compared to the dark street you see in the distance. The bright lights and bustle of the city assaults your senses. You decide that this is a good place to start questioning.",

    "exits": {},

    "items": []
}

room_dark_alley = {
    "name": "",

    "description": "You walk into a dingy and filthy alley, full with Ladies of the night, you see the large bright neon sign for "Bill's Pimp House" in the distance. There are never-do-wells in the alley but a couple people catch your eye, a thug, and a prostitute. They may know something about Bill.",

    "exits": {},

    "items": []
}

room_warehouse_lower = {
    "name": "",

    "description": "You walk through the large industrial sized garage door and see a massive empty warehouse. There are no signs of recent activity whatsoever, you wonder why there was a tip off about some possible criminal doings. You see a ladder leading to a second level, however you have a feeling that the warehouse is a red herring",

    "exits": {},

    "items": []
}

room_warehouse_upper = {
    "name": "",

    "description": "You reach the horizon of the ladder and your suspicions are confirmed about the lack of criminal activity due to the second floor being as barren as the first. You remind yourself to inform Jing when you next see her",

    "exits": {},

    "items": []
}

room_wai_house = {
    "name": "",

    "description": "As you enter the garish royal purple and gold door you see the numerous scandily clad women surrounding you and the vast number of guards protecting each door. In the corner of the room you see a sign that reads "Bill's Office". Upon inspection you notice each guard holds a pistol on their belt. You think that the guards won't give up information easily",

    "exits": {},

    "items": []
}

room_wai_house_secret = {
    "name": "",

    "description": "You walk through the hatch to find a bright room draped in royal purple and gold. The walls adorned with modern art, and a elaborate chandelier hanging from the ceiling A mahogany desk lies in the center of the room covered in documents.",

    "exits": {},

    "items": []
}

# Add any new rooms to the dictionary with whatever appropriate name you want
rooms = {
    "Reception": room_reception,
    "Office": room_desks,
    "Drug Den": room_den_main,
    "Den Basement": room_den_basement,
    "Streets": room_streets,
    "Alleyway": room_dark_alley,
    "Warehouse": room_warehouse_lower,
    "Warehouse Upper": room_warehouse_upper,
    "Wai's House": room_wai_house,
    "Wai's Secret Room": room_wai_house_secret
}
