import arcade
SCREEN_WIDTH = 1200
SCREEN_HEIGHT = 600

class SilverBulletGameWindow(arcade.Window):
	def __init__(self, width, height):
		super().__init__(width, height)
		arcade.set_background_color(arcade.color.WHITE)
		self.human_sprite = arcade.Sprite('images/human.png')
		self.human_sprite.set_position(100, 100)
 
		
 
 
	def on_draw(self):
		arcade.start_render()
		self.human_sprite.draw()
		
 
	
 
 
if __name__ == '__main__':
    window = SilverBulletGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()