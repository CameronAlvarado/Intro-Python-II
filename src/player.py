# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, location):
		self.name = name
		self.location = location
	def get_name(self):
		return self.name
	def __repr__(self):
		return print()

	# def __str__(self):
	# 	return ', '.join(['{key}= {value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
	