from items import items_dict
from termcolor import colored

room_desks = {
    "name": "station",

    "description":
        """The 5th precinct of the Chicago Police Department looks just as it ever does.
There are desks and dividers all around as the station buzzes with people,
ranging from Officers to Detectives to civilians. Hard to imagine that there
could be this much wrong in this region alone as to cause this amount of buzz.
        """,

    "exits": {"down": "Reception"},

    "items": [items_dict["gun"], items_dict["notepad"], items_dict["clock"], items_dict["desk"], items_dict["brew"]],

    "been": True,

    "checked": False
}

room_reception = {
    "name": "reception",

    "description":
    """The reception seems quite busy, just like the rest of the station upstairs.
At least you know you're out in the city today instead of dealing with the inevitable
paperwork that will come of this rush.
    """,

    "exits": {"up": "Station", "west": "Streets"},

    "items": [items_dict["rug"], items_dict["clock"]],

    "been": False,

    "checked": False
}

room_streets = {
    "name": "the city streets",

    "description":
    """You see 3 people on the main street outside the station, the street looks clean and well kept
compared to the dark street you see in the distance. The bright lights and bustle of the city assaults your senses.""",

    "exits": {"west": "Warehouse", "east": "Reception", "south": "Drug Den", "north": "Alleyway"},

    "items": [],

    "been": False,

    "checked": False
}

room_dark_alley = {
    "name": "a dark alleyway",

    "description":
    """You walk into a dingy and filthy alley, full with Ladies of the night, you see the large
bright neon sign for """ + colored("Wai's Pimp House", attrs=["bold"]) + """ in the distance. There are never-do-wells
in the alley but a couple people catch your eye, a thug, and a prostitute. They may know something about Wai.""",

    "exits": {"south": "Streets", "west": "Wai's House"},

    "items": [],

    "been": False,

    "checked": False
}

room_den_main = {
    "name": "the notorious drug den",

    "description":
    """You walk through the broken and burned door to find numerous drug addicts scattered around
the room like autumn leaves, with the floor coated in blankets and carpets, Wai clearly uses this place to
treat their best customers. There is a hollowed out oil drum in the corner that was used recently for a fire, 
the embers cover the room. You see a somewhat intact piece of paper on the floor. You feel this room is important 
in your task to take down Wai
    """,

    "exits": {"north": "Streets"},

    "items": [items_dict["rug"]],

    "been": False,

    "checked": False
}

room_den_basement = {
    "name": "the drug den's basement",

    "description":
    """You enter a clean and organised room full of filing cabinets that had clearly been emptied or ruined recently.
The large desk in the center displays a large blueprint, seemingly of Wai Wu's Pimp House""",

    "exits": {"up": "Drug Den"},

    "items": [items_dict["shank"], items_dict["blueprints"], items_dict["paper"]],

    "been": False,

    "checked": False
}

room_warehouse_lower = {
    "name": "the local abandoned warehouse",

    "description":
    """You walk through the large industrial sized garage door and see a massive empty warehouse.
There are no signs of recent activity whatsoever, you wonder why there was a tip off about some possible
criminal doings. You see a ladder leading to a second level.""",

    "exits": {"up": "Warehouse Upper", "east": "Streets"},

    "items": [],

    "been": False,

    "checked": False
}

room_warehouse_upper = {
    "name": "the warehouse's upper floor",

    "description":
    """The place seems even emptier than the ground floor, and the place is massive.
Could take a good half an hour or so to thoroughly check this place out.
    """,

    "exits": {"down": "Warehouse"},

    "items": [],

    "been": False,

    "checked": False
}

room_wai_house = {
    "name": "Wai Wu's club",

    "description":
    """As you enter the garish royal purple and gold door you see the numerous
scantily clad women surrounding you and the vast number of guards protecting each door. 
In the corner of the room you see a sign that reads """ + colored("Wai's Office\n", attrs=["bold"]) +
    """Upon inspection you notice each guard holds a pistol on their belt. 
You think that the guards won't give up information easily""",

    "exits": {"east": "Alleyway"},

    "items": [],

    "been": False,

    "checked": False
}

room_wai_house_secret = {
    "name": "a newly revealed room",

    "description": """You walk through the hatch to find a bright room draped in royal purple and gold.
The walls adorned with modern art, and a elaborate chandelier hanging from the ceiling.
A mahogany desk lies in the center of the room covered in documents.""",

    "exits": {"up": "Wai's House"},

    "items": [],

    "been": False,

    "checked": False
}

# Add any new rooms to the dictionary with whatever appropriate name you want
rooms = {
    "Reception": room_reception,
    "Station": room_desks,
    "Drug Den": room_den_main,
    "Den Basement": room_den_basement,
    "Streets": room_streets,
    "Alleyway": room_dark_alley,
    "Warehouse": room_warehouse_lower,
    "Warehouse Upper": room_warehouse_upper,
    "Wai's House": room_wai_house,
    "Wai's Secret Room": room_wai_house_secret
}
