import arcade
from core import Revolver
from sprites import VisualLife, GunModel

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Russian Roulette: Heavy Edition"

class GameWindow(arcade.Window):
    def __init__(self):  
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.BLACK
        self.revolver_logic = Revolver()
        self.lives_count = 3
        self.gun = GunModel()
        self.lives_list = arcade.SpriteList()
        self.setup()

    def setup(self):
        self.lives_list.clear()
        for i in range(self.lives_count):
            life = VisualLife(50 + i * 60, SCREEN_HEIGHT - 50)
            self.lives_list.append(life)

    def on_draw(self):
        self.clear()
        self.gun.draw()
        self.lives_list.draw()
        if self.lives_count <= 0:
            arcade.draw_text("GAME OVER", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, 
                             arcade.color.RED, 50, anchor_x="center")

    def on_key_press(self, key, modifiers):
        if key == arcade.key.SPACE and self.lives_count > 0:
            is_shot = self.revolver_logic.pull_trigger()
            if is_shot:
                self.gun.shake()
                self.lives_count -= 1
                if len(self.lives_list) > 0:
                    self.lives_list.pop()
                self.background_color = arcade.color.DARK_RED
            else:
                self.background_color = arcade.color.BLACK

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.background_color = arcade.color.BLACK

if __name__ == "__main__":
    window = GameWindow()
    arcade.run()