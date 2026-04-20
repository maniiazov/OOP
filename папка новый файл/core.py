import random
import smtplib

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
    
from email.message import EmailMessage

def send_notification(name):

    msg = EmailMessage()
    msg.set_content(f"Создана новая анкета на имя: {name}")
    msg['Subject'] = 'Регистрация анкеты'
    msg['From'] = "your_email@gmail.com"  
    msg['To'] = "recipient@mail.ru"      


    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login("your_email@gmail.com", "your_app_password")
            smtp.send_message(msg)
        return True
    except Exception as e:
        print(f"Ошибка почты: {e}")
        return False

def validate_input(text):

    return len(text.strip()) > 0