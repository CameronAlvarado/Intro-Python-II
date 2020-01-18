# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
	def __init__(self, name, current_room):
		self.name = name
		self.current_room = current_room
		self.items = []
	def get_name(self):
		return self.name
	def get_item(self, item):
		return self.items.append(item)
	def drop_item(self, item):
		return self.items.remove(item)
	def __repr__(self):
		return f"{self.name}, {self.current_room}"

	# def __str__(self):
	# 	return ', '.join(['{key}= {value}'.format(key=key, value=self.__dict__.get(key)) for key in self.__dict__])
	