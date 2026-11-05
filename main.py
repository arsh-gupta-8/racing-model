"""
Platformer Game

python -m arcade.examples.platform_tutorial.01_open_window
"""
import arcade

# Constants
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Racing"


class Game(arcade.Window):

  def __init__(self):

    super().__init__(WINDOW_WIDTH, WINDOW_HEIGHT, WINDOW_TITLE)

    self.background_color = arcade.csscolor.CORNFLOWER_BLUE

    self.spriteList = arcade.SpriteList()
    
    self.car = arcade.Sprite(
      "sprites/Car.png",
      scale=0.25,
    )
    self.car.center_x = WINDOW_WIDTH // 2
    self.car.center_y = WINDOW_HEIGHT // 2
    
    self.spriteList.append(self.car)


  def on_draw(self):

    self.clear()

    self.spriteList.draw()


def main():
  """Main function"""
  window = Game()
  arcade.run()


if __name__ == "__main__":
  main()