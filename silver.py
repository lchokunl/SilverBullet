import arcade
import arcade.key
from models import Human,World

SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600


class SilverBulletGameWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.WHITE)
		self.human_sprite = arcade.Sprite('images/human.png')
		self.world = World(width, height)
 
 
	def on_draw(self):
		arcade.start_render()
		self.human_sprite.draw()
		
	def update(self, delta):
		self.world.update(delta)
		self.human_sprite.set_position(self.world.human.x, self.world.human.y)
		
	def on_key_press(self, key, key_modifiers):
		self.world.on_key_press(key, key_modifiers)
		
 
	
 
 
if __name__ == '__main__':
    window = SilverBulletGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()