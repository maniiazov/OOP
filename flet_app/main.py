import flet as ft

class WeatherApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Температура областей КР"
        self.page.window_width = 500
        self.page.window_height = 800
        self.page.scroll = "adaptive"

        self.regions = [
            "Чуйская область", "Ошская область", "Баткенская область",
            "Нарынская область", "Иссык-Кульская область", 
            "Таласская область", "Джалал-Абадская область"
        ]

        self.inputs = []
        self.result_text = ft.Text(size=22, weight="bold")
        self.max_text = ft.Text(size=18, weight="500")
        self.min_text = ft.Text(size=18, weight="500")

        self.build_ui()

    def build_ui(self):
        self.page.add(ft.Text("Введите температуру по областям", size=20, weight="bold"))
        
        for region in self.regions:
            field = ft.TextField(label=region, width=450, keyboard_type=ft.KeyboardType.NUMBER)
            self.inputs.append(field)
            self.page.add(field)
        
        calc_button = ft.ElevatedButton("Рассчитать", on_click=self.calculate_average, width=450)
        
        self.page.add(calc_button, self.result_text, self.max_text, self.min_text)
    
    def calculate_average(self, e):
        temperatures = []
        try:
            for field in self.inputs:
                temperatures.append(float(field.value.strip()))

            average = sum(temperatures) / len(temperatures)
            
            
            if average > 20:
                self.result_text.color = "green"
            elif 10 <= average <= 20:
                self.result_text.color = "blue"
            else:
                self.result_text.color = "red"

            self.result_text.value = f"Средняя температура: {average:.2f}°C"
            self.max_text.value = f"Самая максимальная: {max(temperatures)}°C"
            self.min_text.value = f"Самая минимальная: {min(temperatures)}°C"

        except (ValueError, TypeError):
            self.result_text.value = "Ошибка: введите все числа"
            self.result_text.color = "orange"
            self.max_text.value = ""
            self.min_text.value = ""
        
        self.page.update()

def main(page: ft.Page):
    WeatherApp(page)

if __name__ == "__main__":
    ft.app(target=main)