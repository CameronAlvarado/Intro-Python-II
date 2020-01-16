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

room['overlook'].contains_item = item['gem']
room['treasure'].contains_item = item['bomb']

# Main

# Instantiate Player

player1 = Player('Cameron', room['outside'])
player1.items.append(item['match'])

# Instantaite Player in Room

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
print(f'Hello, {player1.name}. Welcome to the maze. Type n, s, e, w to move. q to quit')
print()

# Loop
while True:
	# Choices
	choices = ["n", "s", "e", "w", "q", "i"]
	print(player1.current_room.return_room())
	print()
	if player1.current_room.items is True:
		print(f'This room contains: {player1.current_room.items}')
		print()
	else:
		None
	res = input("Which way? ~~> ")
	if res in choices:
		if res == 'i':
			print_spaces()
			print(f"Your items include: {player1.items}")
			print()
		if res == 'n':
			if hasattr(player1.current_room, 'n_to'):
				print_spaces()
				# room[player1.current_room].player_list.remove(player1)
				player1.current_room = player1.current_room.n_to
				# room[player1.current_room].player_list.append(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 's':
			if hasattr(player1.current_room, 's_to'):
				print_spaces()
				# room[player1.current_room].player_list.remove(player1)
				player1.current_room = player1.current_room.s_to
				# room[player1.current_room].player_list.append(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'e':
			if hasattr(player1.current_room, 'e_to'):
				print_spaces()
				# room[player1.current_room].player_list.remove(player1)
				player1.current_room = player1.current_room.e_to
				# room[player1.current_room].player_list.appens(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'w':
			if hasattr(player1.current_room, 'w_to'):
				print_spaces()
				# room[player1.current_room].player_list.remove(player1)
				player1.current_room = player1.current_room.w_to
				# room[player1.current_room].player_list.append(player1)
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'q':
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
