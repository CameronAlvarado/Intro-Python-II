# Implement a class to hold room information. This should have name and
# description attributes.

# Room holds items

class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.player_list = []
		self.item_list = []
	# def print_players(self):
	# 	print(self.player_list)
	def return_room(self):
		return f"You are in the {self.name}. {self.description}"
	# def __repr__(self):
	# 	return self.get()
