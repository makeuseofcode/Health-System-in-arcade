import arcade

# Set window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set player movement speed
PLAYER_MOVEMENT_SPEED = 5

class GameWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        # Create player and enemy objects
        self.player = arcade.SpriteCircle(30, arcade.color.BLUE)
        self.enemy = arcade.SpriteCircle(30, arcade.color.RED)
        self.player.center_x = 100
        self.player.center_y = 100
        self.enemy.center_x = 400
        self.enemy.center_y = 300

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.enemy.draw()

    def update(self, delta_time):
        pass

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player.center_x -= PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.center_x += PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.UP:
            self.player.center_y += PLAYER_MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.center_y -= PLAYER_MOVEMENT_SPEED

def main():
    game = GameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
