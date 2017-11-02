import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_LEFT = 3
DIR_DOWN = 4

DELAY_TIME = 1

HEALTH = 5

class Human1:
	
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
		return (abs(self.x - other.center_x) <= hit_size) and (abs(self.y - other.center_y) <= hit_size)
		
class Human2:
	
	def __init__(self, world, x, y):
		self.world = world
		self.x = x
		self.y = y
		self.direction = 0
 
 
	def update(self, delta):
		
		if self.direction == DIR_UP and self.y < self.world.height-50:
			self.y += 5
		
		if self.direction == DIR_RIGHT and self.x < self.world.width-50:
			self.x += 5
			
		if self.direction == DIR_LEFT and self.x > self.world.width/2-50:
			self.x -= 5
		
		if self.direction == DIR_DOWN and self.y > 50:
			self.y -= 5
			
	def hit(self, other, hit_size):
		return (abs(self.x - other.center_x) <= hit_size) and (abs(self.y - other.center_y) <= hit_size)
			
class Bullet1(arcade.Sprite):
	
	def __init__(self, file,scale, human1):
		super().__init__(file,scale)
		self.center_x = human1.x
		self.center_y = human1.y
	
 
 
	def update(self):
		self.center_x += 5
		if self.center_x > 1200:
			self.kill()
			
class Bullet2(arcade.Sprite):
	
	def __init__(self, file,scale, human2):
		super().__init__(file,scale)
		self.center_x = human2.x
		self.center_y = human2.y
	
 
 
	def update(self):
		self.center_x -= 5
		if self.center_x < 0:
			self.kill()
		
		
class World:

	def __init__(self, width, height):
		self.width = width
		self.height = height
		self.health1 = HEALTH
		self.health2 = HEALTH
		self.human1 = Human1(self, 100, 100)
		self.human2 = Human2(self, 800, 100)
		
		self.bullet1_list = arcade.SpriteList()
		self.bullet2_list = arcade.SpriteList()
		
		self.bullet1 = Bullet1("images/bullet2.png",1,self.human1)
		self.bullet2 = Bullet2("images/bullet2.png",1,self.human2)
		
		self.shoot1_delay = True
		self.shoot2_delay = True
		
		self.count_time1 = 0
		self.count_time2 = 0
		
	def draw(self):
		self.bullet1_list.draw()
		self.bullet2_list.draw()
		
	def shoot1(self):
		bullet1 = Bullet1("images/bullet1.png",1,self.human1)
		self.bullet1_list.append(bullet1)

	def shoot2(self):
		bullet2 = Bullet2("images/bullet2.png",1,self.human2)
		self.bullet2_list.append(bullet2)
 
	def update(self, delta):
		self.human1.update(delta)
		self.human2.update(delta)
		self.bullet1_list.update()
		self.bullet2_list.update()
		
		self.count_time1 += delta
		if self.count_time1 >= DELAY_TIME:
			self.shoot1_delay = True
			self.count_time1 = 0
		
		self.count_time2 += delta
		if self.count_time2 >= DELAY_TIME:
			self.shoot2_delay = True
			self.count_time2 = 0
			
		for bullet in self.bullet2_list:
			if self.human1.hit(bullet, 30) and self.health1 > 0 and self.health2 > 0:
				self.health1 -= 1
				bullet.kill()
		for bullet in self.bullet1_list:
			if self.human2.hit(bullet, 30) and self.health2 > 0 and self.health1 > 0:
				self.health2 -= 1
				bullet.kill()
		
	def on_key_press(self, key, key_modifiers):
		if key == arcade.key.W:
			self.human1.direction = DIR_UP
		
		if key == arcade.key.D:
			self.human1.direction = DIR_RIGHT
		
		if key == arcade.key.A:
			self.human1.direction = DIR_LEFT
			
		if key == arcade.key.S:
			self.human1.direction = DIR_DOWN
			
		if key == arcade.key.SPACE and self.shoot1_delay:
			self.shoot1()
			self.shoot1_delay = False
			
		if key == arcade.key.UP:
			self.human2.direction = DIR_UP
		
		if key == arcade.key.RIGHT:
			self.human2.direction = DIR_RIGHT
		
		if key == arcade.key.LEFT:
			self.human2.direction = DIR_LEFT
			
		if key == arcade.key.DOWN:
			self.human2.direction = DIR_DOWN
			
		if key == arcade.key.ENTER and self.shoot2_delay:
			self.shoot2()
			self.shoot2_delay = False
			
			