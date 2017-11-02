import arcade
import arcade.key
from models import Human1,World

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

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


class SilverBulletGameWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.WHITE)
		self.world = World(width, height)
		self.human1_sprite = ModelSprite('images/human1.png',model=self.world.human1)
		self.human2_sprite = ModelSprite('images/human2.png',model=self.world.human2)
		

 
 
	def on_draw(self):
		arcade.start_render()
		self.human1_sprite.draw()
		self.human2_sprite.draw()
		self.world.draw()
		
		arcade.draw_text("Player1' Health ",10, self.height - 30,arcade.color.BLACK, 20)
		arcade.draw_text(str(self.world.health1),60, self.height - 100,arcade.color.BLACK, 50)
		arcade.draw_text("Player2' Health " ,1000, self.height - 30,arcade.color.BLACK, 20)
		arcade.draw_text(str(self.world.health2),1070, self.height - 100,arcade.color.BLACK, 50)
		
		if self.world.health1 == 0:
			arcade.draw_text("Player2 Win !" ,450, self.height - 200,arcade.color.BLACK, 40)
		
		if self.world.health2 == 0:
			arcade.draw_text("Player1 Win !" ,450, self.height - 200,arcade.color.BLACK, 40)
		
		
		
	def update(self, delta):
		self.world.update(delta)
		
		
	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)
		
 
	
 
 
if __name__ == '__main__':
    window = SilverBulletGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()