import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_LEFT = 3

class Human:
	
	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y
		self.direction = 0
 
 
	def update(self, delta):
		
		if self.direction == DIR_UP:
			self.y += 5
		
		if self.y > 130 :
			self.direction = 0
			self.y -= 5
		
class World:
	def __init__(self, width, height):
		self.width = width
		self.height = height
 
		self.human = Human(self, 100, 100)
 
 
	def update(self, delta):
		self.human.update(delta)
		
	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.SPACE:
			self.human.direction = DIR_UP