import arcade
from core import Revolver, send_notification, validate_input
from sprites import VisualLife, GunModel, UserAvatar

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Russian Roulette: Heavy Edition"

class GameWindow(arcade.Window):
    def __init__(self):  
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        self.background_color = arcade.color.BLACK
        self.revolver_logic = Revolver()
        self.lives_count = 3
        

        self.gun_list = arcade.SpriteList()
        self.gun = GunModel()
        self.gun_list.append(self.gun)
        
        self.avatar_list = arcade.SpriteList()
        
        self.lives_list = arcade.SpriteList()
        self.setup()
        
        self.user_name = "Islam" 
        self.ui_color = arcade.color.BLACK
        self.error_text = ""

    def setup(self):
        self.lives_list.clear()
        for i in range(self.lives_count):
            life = VisualLife(50 + i * 60, SCREEN_HEIGHT - 50)
            self.lives_list.append(life)

    def on_draw(self):
        self.clear()
        arcade.set_background_color(self.ui_color)
        

        self.gun_list.draw()
        self.lives_list.draw()
        self.avatar_list.draw()

        if self.error_text:
            arcade.draw_text(self.error_text, SCREEN_WIDTH // 2, 100, 
                             arcade.color.RED, 20, anchor_x="center")

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
                self.ui_color = arcade.color.DARK_RED
            else:
                self.ui_color = arcade.color.BLACK

        if key == arcade.key.ENTER:
            if validate_input(self.user_name):
                self.ui_color = arcade.color.DARK_GREEN
                self.error_text = ""
                

                self.avatar_list.clear()
                try:

                    new_avatar = UserAvatar("photo.jpg", 400, 450)
                    self.avatar_list.append(new_avatar)
                except Exception:
                    self.error_text = "ФАЙЛ photo.jpg НЕ НАЙДЕН"
                

                send_notification(self.user_name)
            else:
                self.ui_color = arcade.color.MAROON
                self.error_text = "ОШИБКА: ИМЯ ПУСТОЕ"

    def on_key_release(self, key, modifiers):
        if key == arcade.key.SPACE:
            self.ui_color = arcade.color.BLACK

if __name__ == "__main__":
    window = GameWindow()
    arcade.run()