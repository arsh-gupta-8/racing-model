import arcade, math

WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_TITLE = "Racing"

ACCELERATION = 600
DECELERATION = 400
MAX_SPEED = 400
FRICTION = 0.99

ANGLE_CHANGE = 120

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

    self.car.speed = 0
    
    self.spriteList.append(self.car)

    self.left_pressed = False
    self.right_pressed = False
    self.up_pressed = False
    self.down_pressed = False


  def on_draw(self):
    self.clear()
    self.spriteList.draw()


  def on_key_press(self, symbol, modifiers):
    if symbol in (arcade.key.W, arcade.key.UP):
      self.up_pressed = True
    elif symbol in (arcade.key.A, arcade.key.LEFT):
      self.left_pressed = True
    elif symbol in (arcade.key.S, arcade.key.DOWN):
      self.down_pressed = True
    elif symbol in (arcade.key.D, arcade.key.RIGHT):
      self.right_pressed = True


  def on_key_release(self, symbol, modifiers):
    if symbol in (arcade.key.W, arcade.key.UP):
      self.up_pressed = False
    elif symbol in (arcade.key.A, arcade.key.LEFT):
      self.left_pressed = False
    elif symbol in (arcade.key.S, arcade.key.DOWN):
      self.down_pressed = False
    elif symbol in (arcade.key.D, arcade.key.RIGHT):
      self.right_pressed = False


  def on_update(self, delta_time):
    print(self.car.position, self.car.angle)
    angle_rad = math.radians(self.car.angle)

    if self.up_pressed and not self.down_pressed and self.car.speed <= MAX_SPEED:
      self.car.speed += ACCELERATION * delta_time
    elif not self.up_pressed and self.down_pressed and self.car.speed >= -MAX_SPEED/2:
      self.car.speed -= DECELERATION * delta_time
    else:
      self.car.speed *= FRICTION

      if abs(self.car.speed) <= 2:
        self.car.speed = 0

    if self.left_pressed and not self.right_pressed and self.car.speed > 0:
      self.car.angle -= ANGLE_CHANGE * delta_time
    elif not self.left_pressed and self.right_pressed and self.car.speed > 0:
      self.car.angle += ANGLE_CHANGE * delta_time

    self.car.center_x += self.car.speed * math.sin(angle_rad) * delta_time
    self.car.center_y += self.car.speed * math.cos(angle_rad) * delta_time

    
def main():
  """Main function"""
  window = Game()
  arcade.run()


if __name__ == "__main__":
  main()