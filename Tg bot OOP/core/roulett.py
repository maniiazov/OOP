import random

class RussianRouletteGame:
    def __init__(self, p1_id, p2_id, p1_name, p2_name):
        self.chambers = [0, 0, 0, 0, 0, 1]
        random.shuffle(self.chambers)
        self.current_index = 0
        self.is_active = True
        self.players = [
            {'id': p1_id, 'name': p1_name},
            {'id': p2_id, 'name': p2_name}
        ]
        self.turn = random.randint(0, 1)

    def shoot(self, user_id):
        if not self.is_active:
            return "Игра окончена. Перезарядите барабан."

        current_player = self.players[self.turn]
        if user_id != current_player['id']:
            return f"Не твой ход! Сейчас очередь {current_player['name']}."

        if self.chambers[self.current_index] == 1:
            self.is_active = False
            return f"💥 БАХ! {current_player['name']} выбывает. Игра окончена."
        
        self.current_index += 1
        self.turn = 1 - self.turn
        next_player = self.players[self.turn]
        return f"Щелчок... {current_player['name']} жив. 🔫 Очередь {next_player['name']}!"

    def reset(self):
        random.shuffle(self.chambers)
        self.current_index = 0
        self.is_active = True
        self.turn = random.randint(0, 1)
        return "Револьвер перезаряжен!"