from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers inthe distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}

# Declare all the items

item = {
	'gem': Item('Precious Gem', 'The stone glistens as you rotate it in your hand.'),

	'bomb': Item('Bomb', 'The small black orb smells of gunpowder'),

	'match': Item('Flint', 'You could use this for lighting something')
}


# Link rooms together

room['outside'].n_to = room['foyer'] # remove player from outside
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Link items to rooms

room['overlook'].item_list.append(item['gem'])
room['treasure'].item_list.append(item['bomb'])

# Main

# Instantiate Player and Room

player1 = Player('Cameron', room['outside'])
player1.items.append(item['match'])
room['outside'].player_list.append(player1)

# Formatting text

def print_spaces():
	for x in range(0, 50):
		print()

def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  

print_spaces()

# Run Intro
print(f'Hello, {player1.name}. Welcome to the maze. Type w, a, s, d to move. x to quit. e to pick up. q to drop')
print()

# Loop
while True:
	# Choices
	choices = ["w", "a", "s", "d", "q", "i", "x", "q", "e"]

	print(player1.current_room.return_room())
	print()
	if len(player1.current_room.item_list) is not 0:
		print(f'This room contains: {player1.current_room.item_list}')
		print()
	else:
		None

	room_item = player1.current_room.item_list
	player_item = player1.items

	room = player1.current_room

	res = input("Which way? ~~> ")
	if res in choices:
		if res == 'e':
			if len(room.item_list) is not 0:
				player1.get_item(room_item[0])
				room.remove_item(room_item[0])
				print_spaces()
				print(f"You picked up a {player_item[0]}.")
				print()
			else:
				print("There are no items here.")
		if res == 'q':
			if len(player1.items) is not 0:
				room.add_item(player_item[0])
				player1.drop_item(player_item[0])
				print_spaces()
				print(f"You dropped a {room_item[0].name}.")
				print()
			else:
				print_spaces()
				print("You have no items to drop.")
				print()
		if res == 'i':
			print_spaces()
			print(f"Your items include: {player1.items}")
			print()
		if res == 'w':
			if hasattr(player1.current_room, 'n_to'):
				print_spaces()
				player1.current_room.player_list.remove(player1)
				player1.current_room = player1.current_room.n_to
				player1.current_room.player_list.append(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 's':
			if hasattr(player1.current_room, 's_to'):
				print_spaces()
				player1.current_room.player_list.remove(player1)
				player1.current_room = player1.current_room.s_to
				player1.current_room.player_list.append(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'd':
			if hasattr(player1.current_room, 'e_to'):
				print_spaces()
				player1.current_room.player_list.remove(player1)
				player1.current_room = player1.current_room.e_to
				player1.current_room.player_list.append(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'a':
			if hasattr(player1.current_room, 'w_to'):
				print_spaces()
				player1.current_room.player_list.remove(player1)
				player1.current_room = player1.current_room.w_to
				player1.current_room.player_list.append(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'x':
			print_spaces()
			print("Thank you for playing")
			print()
			break
	else:
		print_spaces()
		print("You can only enter the commands n, s, e, w, and q.")
		print()

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
