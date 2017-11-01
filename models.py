import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_LEFT = 3
DIR_DOWN = 4

class Human:
	
	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y
		self.direction = 0
 
 
	def update(self, delta):
		
		if self.direction == DIR_UP and self.y < self.world.height-50:
			self.y += 5
		
		if self.direction == DIR_RIGHT and self.x < self.world.width/2-50:
			self.x += 5
			
		if self.direction == DIR_LEFT and self.x > 50:
			self.x -= 5
		
		if self.direction == DIR_DOWN and self.y > 50:
			self.y -= 5
		
class World:
	def __init__(self, width, height):
		self.width = width
		self.height = height
 
		self.human = Human(self, 100, 100)
 
 
	def update(self, delta):
		self.human.update(delta)
		
	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.W:
			self.human.direction = DIR_UP
		
		if key == arcade.key.D:
			self.human.direction = DIR_RIGHT
		
		if key == arcade.key.A:
			self.human.direction = DIR_LEFT
			
		if key == arcade.key.S:
			self.human.direction = DIR_DOWN