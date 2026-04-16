import arcade

class VisualLife(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.center_x = x
        self.center_y = y
        self.texture = arcade.make_circle_texture(30, arcade.color.RED)

class GunModel(arcade.Sprite):
    def __init__(self):
        super().__init__()
        self.center_x = 400
        self.center_y = 250
        self.texture = arcade.make_soft_square_texture(100, arcade.color.GRAY, outer_alpha=255)

    def shake(self):
        self.center_x += 10
        arcade.schedule(self._reset_pos, 0.05)

    def _reset_pos(self, delta_time):
        self.center_x = 400
        arcade.unschedule(self._reset_pos)