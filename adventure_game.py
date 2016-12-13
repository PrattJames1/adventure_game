import sys
import time

def living_room():
	move = input("\nYou're in the living room.\n" +
		"Where would you like to move next? \n")

	if move == "q":
		print("Exiting...")
		time.sleep(2)
		sys.exit
	elif move == "north":
		print("Walking north...")
		time.sleep(2)
		dining_room()
	elif move == "east":
		print("Walking east...")
		time.sleep(2)
		theater()
	elif move == "south":
		print("Walking south...")
		time.sleep(2)
		front_porch()
	elif move == "west":
		print("Walking west...")
		time.sleep(2)
		garage()
	else:
		print("\nInvalid input!")
		living_room()


def front_porch():
	move = input("\nYou're on your front porch.\n" +
	"Where would you like to move next? \n")

	if move == "q":
		print("Exiting...")
		time.sleep(2)
		sys.exit
	elif move == "north":
		print("Walking north...")
		time.sleep(2)
		living_room()
	elif move == "east":
		print("Walking east...")
		time.sleep(2)
		print("\nYou make awkward eye contact with your neighbor." +
		"You shouldn't go that way.")
		front_porch()
	elif move == "south":
		print("Walking south...")
		time.sleep(2)
		print("\nYou look out onto the busy street." +
		"You shouldn't leave your front porch!")
		front_porch()
	elif move == "west":
		print("Walking west...")
		time.sleep(2)
		print("\nYou see mountains in the distance,\n" +
		"but you shouldn't leave your front porch!")
		front_porch()
	else:
		print("Thinking...")
		time.sleep(2)
		print("\nInvalid input!\n")
		front_porch()


def theater():
	move = input("\nYou're in your fancy theater.\n" +
	"Monty Python and the Holy Grail is playing.\n" +
	"Where would you like to move next? \n")

	if move == "q":
		print("Exiting...")
		time.sleep(2)
		sys.exit
	elif move == "north":
		print("Walking north...")
		time.sleep(2)
		print("\nYou run into a wall. Ouch.")
		theater()
	elif move == "east":
		print("Walking east...")
		time.sleep(2)
		print("\nYou run into the TV screen.")
		theater()
	elif move == "south":
		print("Walking south...")
		time.sleep(2)
		print("\nYou run into a wall. Ouch.")
		theater()
	elif move == "west":
		print("Walking west...")
		time.sleep(2)
		living_room()
	else:
		print("Thinking...")
		time.sleep(2)
		print("\nInvalid input!")
		theater()


def garage():
	move = input("\nYou're in your garage.\n" +
	"It's crowded with storage boxes. Should clean this place up!\n" +
	"Where would you like to move next? \n")

	if move == "q":
		print("Exiting...")
		time.sleep(2)
		sys.exit
	elif move == "north":
		print("Walking north...")
		time.sleep(2)
		print("\nYou open up a box of books. Nothing interesting.")
		garage()
	elif move == "east":
		print("Walking east...")
		time.sleep(2)
		living_room()
	elif move == "south":
		print("Walking south...")
		time.sleep(2)
		print("\nYou run into a concrete wall. Medic!")
		garage()
	elif move == "west":
		print("Walking west...")
		time.sleep(2)
		print("\nYou observe your closed garage door." +
		"You shouldn't leave your garage!")
		garage()
	else:
		print("Thinking...")
		time.sleep(2)
		print("\nInvalid input!\n")
		garage()


def dining_room():
	move = input("\nYou're in the dining room.\n" +
	"Just an empty dining room table and some chairs.\n" +
	"Where would you like to move next? \n")

	if move == "q":
		print("Exiting...")
		time.sleep(2)
		sys.exit
	elif move == "north":
		print("Walking north...")
		time.sleep(2)
		kitchen()
	elif move == "east":
		print("Walking east...")
		time.sleep(2)
		print("\nYou look east and see your mum's fancy china.")
		dining_room()
	elif move == "south":
		print("Walking south...")
		time.sleep(2)
		living_room()
	elif move == "west":
		print("Walking west...")
		time.sleep(2)
		print("\nYou look out the window and see mountains to the west.")
		dining_room()
	else:
		print("Thinking...")
		time.sleep(2)
		print("\nInvalid input!\n")
		dining_room()


def kitchen():
	move = input("\nYou're in your cozy kitchen.\n" +
	"Where would you like to move next? \n")

	if move == "q":
		print("Exiting...")
		time.sleep(2)
		sys.exit
	elif move == "north":
		print("Walking north...")
		time.sleep(2)
		print("\nAll you see is your stove.")
		kitchen()
	elif move == "east":
		print("Walking east...")
		time.sleep(2)
		print("\nYou see Jesus to the east.")
		kitchen()
	elif move == "south":
		print("Walking south...")
		time.sleep(2)
		dining_room()
	elif move == "west":
		print("Walking west...")
		time.sleep(2)
		print("\nYou see your empty fridge and a list stuck to it saying:\n" +
		"Go grocery shopping!")
		kitchen()
	else:
		print("Thinking...")
		time.sleep(2)
		print("\nInvalid input!\n")
		kitchen()



print("\nWelcome to your house!\n" +
"Type north, east, south, or west to move around.\n" +
"Otherwise, type q to quit.")

living_room()
