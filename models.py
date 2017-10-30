import arcade.key

class Human:
	
	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y
		self.direction = 0
 
 
	def switch_direction(self):
		if self.direction == Ship.DIR_HORIZONTAL:
			self.direction = Ship.DIR_VERTICAL
		else:
			self.direction = Ship.DIR_HORIZONTAL
 
 
	def update(self, delta):
		if key == arcade.key.SPACE:
			self.y += 5
		
		
class World:
	def __init__(self, width, height):
		self.width = width
		self.height = height
 
		self.human = Human(self, 100, 100)
 
 
	def update(self, delta):
		self.human.update(delta)
		
	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.SPACE:
			self.human.switch_direction()