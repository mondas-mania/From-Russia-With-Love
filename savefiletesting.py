from items import *
from player import *

savename = input("What do you want to name the file?")
save = open("Save Files/" + savename + ".txt", "w")
save.write(str(len(inventory)) + "\n")
for items in inventory:
    save.write(items.id + "\n")

save.close()

save = open("Save Files/" + savename + ".txt", "r")
savelines = save.readlines()
inv_count = int(savelines[0])
inv_list = savelines[1:inv_count + 1]

print("Inventory = ")
for i in range(0,inv_count):
    inv_list[i] = inv_list[i].rstrip()
    print(inv_list[i])

save.close()

