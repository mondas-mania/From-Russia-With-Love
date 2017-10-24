from players import *
from gameparser import *
import math
from random import randint
from time import sleep
##CHANGE WEAPON DURING FIGHT##
##BLOCKING FEATURE ADDITION##
def hitpoints(a,b):
	return randint(1,3)*(randint(a, b))



def attacking():
	bodyguard_hit = hitpoints(3,9)
	sleep(2)
	player_hit = hitpoints(3,9)
	player["health"] -= bodyguard_hit
	bodyguard["health"] -= player_hit

def chooseweapon():
	print ("You have: " + " ".join(str(x) for x in player["inventory"]).upper())
	choose = input("Which weapon would you like to use?")
	attacking()

def print_stats():
	#Print out battle stats 
	print ("----- STATS -----")
	print (" ".join(str(x) for x in player["name"]))
	print ("Health is " + str(player["health"]))
	print ("Ammo is " + str(player["ammo"]))
	print ("-----")

	print (" ".join(str(x) for x in bodyguard["name"]))
	print ("Health is " + str(bodyguard["health"]))
	print ("Ammo is " + str(bodyguard["ammo"]))
	print ("-----------------" + "\n")
	chooseweapon()
	

def main():
	while player["health"] and bodyguard["health"] > 0:
		if player["health"] < 0:
			print ("Frank wins!")
		elif bodyguard["health"] < 0:
			print ("Kirill wins!")
		else:
			print_stats()
			

	
main()