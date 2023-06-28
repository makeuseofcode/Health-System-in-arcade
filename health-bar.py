import arcade

# Set window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Set player movement speed
PLAYER_MOVEMENT_SPEED = 15

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
        self.player_health = 100
        self.heal_rate = 1  # Health points healed per second
        self.heal_timer = 0  # Timer for healing

    def update(self, delta_time):
        # ...
        # Update healing timer
        self.heal_timer += delta_time

        print(self.player_health)

        # Heal the player's health every 2 seconds
        if self.heal_timer >= 2:
            self.player_health += self.heal_rate
            self.heal_timer = 0

        # Ensure health doesn't exceed the maximum value
        if self.player_health > 100:
            self.player_health = 100
    
    

        if arcade.check_for_collision(self.player, self.enemy):
            self.player_health -= 0.1

        if self.player_health <= 0:
            arcade.close_window()

    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        self.enemy.draw()

        arcade.draw_rectangle_filled(SCREEN_WIDTH // 2, 20, SCREEN_WIDTH, 20, arcade.color.LIGHT_GRAY)
        health_width = self.player_health / 100 * SCREEN_WIDTH
        arcade.draw_rectangle_filled(health_width // 2, 20, health_width, 20, arcade.color.GREEN)


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
