# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
	def __init__(self, name, description):
		self.name = name
		self.description = description
		self.players = []
		self.items = []
	def __repr__(self):
		return print("You are in room: {self.name}. {self.description}")
	# def __str__(self):
	# 	return ', '.join(['{key}= {value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
