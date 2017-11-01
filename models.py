import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_LEFT = 3
DIR_DOWN = 4

class ModelSprite(arcade.Sprite):
	def __init__(self, *args, **kwargs):
		self.model = kwargs.pop('model', None)
 
		super().__init__(*args, **kwargs)
 
	def sync_with_model(self):
		if self.model:
			self.set_position(self.model.x, self.model.y)
 
	def draw(self):
		self.sync_with_model()
		super().draw()

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
			
	def hit(self, other, hit_size):
		return (abs(self.x - other.x) <= hit_size) and (abs(self.y - other.y) <= hit_size)
			
class Bullet():
	
	def __init__(self, world, human, x, y):
		self.world = world
		self.human = human
		self.x = x
		self.y = y
		self.bullet_list = None
		self.bullet_list = arcade.SpriteList()
	
 
 
	def update(self, delta):
		self.x += 5
		
		
class World:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.score = 5
 
		self.human = Human(self, 100, 100)
		self.bullet = Bullet(self,self,100, 100)
		self.bullet_list = self.bullet.bullet_list
 
	def update(self, delta):
		self.human.update(delta)
		self.bullet_list.update()
		
	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.W:
			self.human.direction = DIR_UP
		
		if key == arcade.key.D:
			self.human.direction = DIR_RIGHT
		
		if key == arcade.key.A:
			self.human.direction = DIR_LEFT
			
		if key == arcade.key.S:
			self.human.direction = DIR_DOWN
			
		if key == arcade.key.SPACE:
			self.bullet_list = ModelSprite('images/bullet.png',model=self.world.bullet)
			self.bullet_list.append(self,bullet)