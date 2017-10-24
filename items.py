class item:
    def __init__(self, id, name, description, mass):
        self.id = id
        self.name = name
        self.description = description
        self.mass = mass


# Items can be added in the following format:
badge_desc = """A slightly grubby badge showing that you are part of the [Insert initials here]PD"""
item_badge = item("id", "id card", badge_desc, 0.010)

coffee_desc = "You can already tell it's going to be a long day."
item_coffee = item("coffee", "a cup of coffee", coffee_desc, 0.150)

gun_desc = "Might need this later."
item_gun = item("gun", "a pistol", gun_desc, 0.800)

# This dictionary just relates the 'simple name' to the item object
# Add any new items to the dictionary like this
items_dict = {
    item_badge.id: item_badge,
    item_coffee.id: item_coffee
}