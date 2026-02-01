import tkinter as tk
import pygame
import os
from PIL import Image, ImageTk

pygame.mixer.init()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def abs_path(file):
    return os.path.join(BASE_DIR, file)

def play_sound(file):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

current_img = None

def show_image(file, label):
    global current_img
    img = Image.open(file)
    img = img.resize((300, 200))
    current_img = ImageTk.PhotoImage(img)
    label.config(image=current_img)

def create_app():
    root = tk.Tk()
    root.title("Car Exhaust Sounds")
    root.geometry('370x600')
    root.resizable(False, False)


    image_label = tk.Label(root)
    image_label.pack()


    # BMW E60
    tk.Button(root, text="Bmw E60", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/audio/E60.mp3")),
                               show_image(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/photo/E60.jpg"), image_label)]
             ).pack(pady=10)

    #RS7
    tk.Button(root, text="Audi RS7", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/audio/RS7.mp3")),
                               show_image(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/photo/RS7.jpg"), image_label)]
              ).pack(pady=10)

    #C63
    tk.Button(root, text="Mercedes C63", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/audio/V63.mp3")),
                               show_image(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/photo/S63.jpg"), image_label)]
              ).pack(pady=10)

    #GTR
    tk.Button(root, text="GTR 34", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/audio/GTR34.mp3")),
                               show_image(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/photo/GTR.jpg"), image_label)]
              ).pack(pady=10)

    #DOG
    tk.Button(root, text="DOG", font=("Arial", 14),
              command=lambda: [play_sound(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/audio/Мне этот мир понятен.mp3")),
                               show_image(abs_path("/Users/islammakeev/Desktop/begining_of_died/lab11/photo/DOG.jpg"), image_label)]
              ).pack(pady=10)

    root.mainloop()

create_app()
