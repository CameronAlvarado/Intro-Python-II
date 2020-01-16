from room import Room
from player import Player

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
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

# Main

# Choices
choices = ["n", "s", "e", "w", "q"]

# Instantiate Item for player
item1 = Item('Precious Gem', 'The stone glistens as you rotate it in your hand.')

# Instantiate Player
player1 = Player('Cameron', room['outside'])
name = player1.get_name()

def print_spaces():
	for x in range(0, 50):
		print()

# Clear Terminal
print_spaces()

# Run Intro
print(f'Hello, {name}. Welcome to the maze. Type n, s, e, w to move. q to quit')

# Loop
while True:
	print(f"You are currently in: {player1.location.name}. {player1.location.description}")
	print()
	res = input("Which way? ~~> ")
	if res in choices:
		if res == 'n':
			if hasattr(player1.location, 'n_to'):
				print_spaces()
				player1.location = player1.location.n_to
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 's':
			if hasattr(player1.location, 's_to'):
				print_spaces()
				player1.location = player1.location.s_to
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'e':
			if hasattr(player1.location, 'e_to'):
				print_spaces()
				player1.location = player1.location.e_to
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'w':
			if hasattr(player1.location, 'w_to'):
				print_spaces()
				player1.location = player1.location.w_to
			else:
				print_spaces()
				print("You can't go that way.")
				print()
		elif res == 'q':
			print()
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
