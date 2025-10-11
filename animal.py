class Animal:
    def __init__(self, name, color, eat):
        self.name = name
        self.color = color
        self.eat = eat

    def sound(self, noise):
        return f"{self.name} издаёт звук: {noise}"

    def __str__(self):
        return f"Имя: {self.name}\nЦвет: {self.color}\nПитание: {self.eat}"
    
    
class Mammal(Animal):
    def __init__(self, name, color, eat, fur):
        super().__init__(name, color, eat)
        self.fur = fur

    def feed_milk(self):
        return f"{self.name} кормит детёнышей молоком."

    def __str__(self):
        return super().__str__() + f"\nШерсть: {self.fur}"


class Predator(Mammal):
    def __init__(self, name, color, eat, fur, power):
        super().__init__(name, color, eat, fur)
        self.power = power

    def hunt(self):
        return f"{self.name} охотится со скоростью {self.power} км/ч!"

    def __str__(self):
        return super().__str__() + f"\nСила охоты: {self.power} км/ч"


lion = Mammal(name="Лев", color="золотистый", eat="мясо", fur="густая")
print(lion)
print(lion.sound("РРРРР!"))
print(lion.feed_milk())

print("\n")

tiger = Predator(name="Тигр", color="оранжевый", eat="мясо", fur="полосатая", power=45)
print(tiger)
print(tiger.hunt())