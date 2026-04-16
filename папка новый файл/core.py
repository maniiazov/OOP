import random

class Revolver:
    def __init__(self):
        self.capacity = 6
        self.drum = [False] * self.capacity
        self.current_step = 0
        self.spin()

    def spin(self):
        self.drum = [False] * self.capacity
        bullet_index = random.randint(0, self.capacity - 1)
        self.drum[bullet_index] = True
        self.current_step = 0

    def pull_trigger(self):
        result = self.drum[self.current_step]
        self.current_step += 1
        if result or self.current_step >= self.capacity:
            self.spin()
        return result