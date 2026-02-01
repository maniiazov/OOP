from abc import ABC, abstractmethod


class Payment(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    @abstractmethod
    def refund(self, amount):
        pass


class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} сом через банковскую карту прошла успешно.")

    def refund(self, amount):
        print(f"Возврат {amount} сом на банковскую карту выполнен.")


class CryptoPayment(Payment):
    def pay(self, amount):
        print(f"Оплата {amount} сом в криптовалюте прошла успешно.")

    def refund(self, amount):
        print(f"Возврат {amount} сом в криптовалюте выполнен.")


payments = [CreditCardPayment(), CryptoPayment()]
for p in payments:
    p.pay(1000)



class Course(ABC):
    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def get_materials(self):
        pass

    @abstractmethod
    def end(self):
        pass


class PythonCourse(Course):
    def start(self):
        print("Курс по Python начат.")

    def get_materials(self):
        print("Материалы: основы синтаксиса, функции, классы.")

    def end(self):
        print("Курс по Python завершён.")


class MathCourse(Course):
    def start(self):
        print("Курс по математике начат.")

    def get_materials(self):
        print("Материалы: алгебра, геометрия, тригонометрия.")

    def end(self):
        print("Курс по математике завершён.")



courses = [PythonCourse(), MathCourse()]
for c in courses:
    c.start()
    c.get_materials()
    c.end()


class Delivery(ABC):
    @abstractmethod
    def calculate_cost(self, distance):
        pass

    @abstractmethod
    def deliver(self):
        pass


class AirDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 20 
    def deliver(self):
        print("Доставка по воздуху выполнена.")


class GroundDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 10

    def deliver(self):
        print("Доставка по земле выполнена.")


class SeaDelivery(Delivery):
    def calculate_cost(self, distance):
        return distance * 5

    def deliver(self):
        print("Доставка по морю выполнена.")


deliveries = [AirDelivery(), GroundDelivery(), SeaDelivery()]
for d in deliveries:
    cost = d.calculate_cost(100)
    print(f"{d.__class__.__name__}: стоимость доставки {cost} сом.")
    d.deliver()



class BankAccount:
    def __init__(self, owner, pin):
        self.__owner = owner
        self.__balance = 0
        self.__pin = pin

    def deposit(self, amount, pin):
        if pin == self.__pin and amount > 0:
            self.__balance += amount
            print(f"{amount} сом зачислено на счёт.")
        else:
            print("Ошибка: неверный PIN или сумма.")

    def withdraw(self, amount, pin):
        if pin != self.__pin:
            print("Ошибка: неверный PIN.")
        elif amount <= 0:
            print("Ошибка: некорректная сумма.")
        elif amount > self.__balance:
            print("Ошибка: недостаточно средств.")
        else:
            self.__balance -= amount
            print(f"{amount} сом снято со счёта.")

    def change_pin(self, old_pin, new_pin):
        if old_pin == self.__pin:
            self.__pin = new_pin
            print("PIN успешно изменён.")
        else:
            print("Ошибка: старый PIN неверный.")

    def get_balance(self):
        print(f"Баланс: {self.__balance} сом.")


acc = BankAccount("Имран", 1234)
acc.deposit(1000, 1234)
acc.withdraw(300, 1234)
acc.get_balance()
acc.change_pin(1234, 5678)



class UserProfile:
    def __init__(self, email, password):
        self.__email = email
        self.__password = password
        self._status = "basic"

    def login(self, email, password):
        if email == self.__email and password == self.__password:
            print("Вход выполнен успешно.")
            return True
        else:
            print("Ошибка: неверные данные.")
            return False

    def upgrade_to_premium(self):
        self._status = "premium"
        print("Пользователь обновлён до премиум-статуса.")

    def get_info(self):
        print(f"Email: {self.__email}, Статус: {self._status}")


user = UserProfile("test@gmail.com", "1123123")
if user.login("test@gmail.com", "1123123"):
    user.get_info()
    user.upgrade_to_premium()
    user.get_info()
 
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
        self.__discount = 0

    def get_price(self):
        return self.price * (1 - self.__discount / 100)

    def set_discount(self, percent, is_admin=False):
        if is_admin:
            self.__discount = percent
            print(f"Скидка {percent}% установлена.")
        else:
            print("Ошибка: нет прав администратора.")


prod = Product("Телефон", 20000)
print("Цена без скидки:", prod.get_price())
prod.set_discount(10, is_admin=True)
print("Цена со скидкой:", prod.get_price())


class TextFile:
    def open(self):
        print("Открыт текстовый файл (.txt).")


class ImageFile:
    def open(self):
        print("Открыт файл изображения (.jpg, .png).")


class AudioFile:
    def open(self):
        print("Открыт аудиофайл (.mp3).")


def open_all(files):
    for f in files:
        f.open()


files = [TextFile(), ImageFile(), AudioFile()]
open_all(files)


class Car:
    def move(self, distance):
        speed = 100
        time = distance / speed
        print(f"Машина проедет {distance} км за {time:.2f} часов.")


class Truck:
    def move(self, distance):
        speed = 60
        time = distance / speed
        print(f"Грузовик проедет {distance} км за {time:.2f} часов.")


class Bicycle:
    def move(self, distance):
        speed = 20
        time = distance / speed
        print(f"Велосипед проедет {distance} км за {time:.2f} часов.")


def simulate_transport(transport_list, distance):
    for t in transport_list:
        t.move(distance)


simulate_transport([Car(), Truck(), Bicycle()], 200)


class Student:
    def access_portal(self):
        print("Студент: доступ к расписанию и домашним заданиям.")


class Teacher:
    def access_portal(self):
        print("Преподаватель: доступ к выставлению оценок.")


class Administrator:
    def access_portal(self):
        print("Администратор: доступ к управлению пользователями.")


users = [Student(), Teacher(), Administrator()]
for u in users:
    u.access_portal()
