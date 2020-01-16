# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description
	def print_players(self):
		print(self.players)
	def __repr__(self):
		return print("You are in room: {name}. {description}")
	# def __str__(self):
	# 	return f"{self.name}n/n/{self.description}"
