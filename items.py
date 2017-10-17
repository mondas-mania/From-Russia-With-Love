class item:

    def __init__(self, id, name, description, mass):
        self.id = id
        self.name = name
        self.description = description
        self.mass = mass


id_desc = """You new shiny student ID card. Expires 1 June 2017.
You wonder why they have printed a suicide hotline number on it?..."""
item_id = item("id", "id card", id_desc, 0.010)

laptop_desc = "It has seen better days. At least it has a WiFi card!"
item_laptop = item("laptop", "laptop", laptop_desc, 2.400)

money_desc = "This wad of cash is barely enough to pay your tuition fees."
item_money = item("money", "money", money_desc, 0.100)

biscuits_desc = "A pack of biscuits."
item_biscuits = item("biscuits", "a pack of biscuits", biscuits_desc, 0.100)

pen_desc = "A basic ballpoint pen."
item_pen = item("pen", "a pen", pen_desc, 0.010)

handbook_desc = "This student handbook explains everything. Seriously."
item_handbook = item("handbook", "a student handbook", handbook_desc, 0.150)

weights_desc = "There's no way you can be bothered to try to lift this"
item_weights = item("weights", "10kg weights", weights_desc, 10.000)