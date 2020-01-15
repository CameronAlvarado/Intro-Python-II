# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, current_room):
		self.name = name
		self.current_room = current_room
	def __str__(self):
		return ', '.join(['{key}= {value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
	