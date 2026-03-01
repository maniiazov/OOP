import flet

class EmployeeApp:
    def __init__(self, page: flet.Page):
        self.page = page
        self.page.title = 'Каталог сотрудников компании'
        self.page.window_width = 600
        self.page.window_height = 800
        self.employees = []
        self.build_ui()

    def build_ui(self):
        self.first_name = flet.TextField(label="Имя", expand=True)
        self.last_name = flet.TextField(label='Фамилия', expand=True)
        self.age = flet.TextField(label='Возраст', keyboard_type=flet.KeyboardType.NUMBER)
        self.salary = flet.TextField(label='Зарплата', keyboard_type=flet.KeyboardType.NUMBER)
        
        self.position = flet.Dropdown(
            label='Должность',
            width=200,
            options=[
                flet.dropdown.Option("Разработчик"),
                flet.dropdown.Option("Дизайнер"),
                flet.dropdown.Option("Менеджер"),
                flet.dropdown.Option("Тестировщик"),
            ]
        )

        self.employee_list_view = flet.ListView(expand=True, spacing=10, padding=10)
        self.error_text = flet.Text(color=flet.Colors.RED)

        add_button = flet.ElevatedButton(
            'Добавить сотрудника', 
            on_click=self.add_employee,
            bgcolor=flet.Colors.BLUE,
            color=flet.Colors.WHITE
        )

        self.page.add(
            flet.Text("Форма ввода", size=20, weight='bold'),
            flet.Row([self.first_name, self.last_name]),
            flet.Row([self.age, self.salary, self.position]),
            self.error_text,
            flet.Row([add_button], alignment=flet.MainAxisAlignment.CENTER),
            flet.Divider(),
            flet.Text("Список (сортировка ↑)", size=18, weight='bold'),
            self.employee_list_view
        )

    def add_employee(self, e):
        if not all([self.first_name.value, self.last_name.value, self.age.value, 
                    self.salary.value, self.position.value]):
            self.error_text.value = "Заполните все поля!"
            self.page.update()
            return

        try:
            age_val = int(self.age.value)
            salary_val = float(self.salary.value)
        except ValueError:
            self.error_text.value = "Числа введены некорректно!"
            self.page.update()
            return

        new_emp = {
            "id": len(self.employees) + 1,
            "name": f"{self.first_name.value} {self.last_name.value}",
            "age": age_val,
            "pos": self.position.value,
            "salary": salary_val
        }

        self.employees.append(new_emp)
        self.employees.sort(key=lambda x: x['salary'])
        self.error_text.value = ""
        self.clear_inputs()
        self.render_list()

    def delete_employee(self, emp_id):
        self.employees = [emp for emp in self.employees if emp['id'] != emp_id]
        self.render_list()

    def render_list(self):
        self.employee_list_view.controls.clear()
        for emp in self.employees:
            is_high = emp['salary'] > 100000
            self.employee_list_view.controls.append(
                flet.Container(
                    padding=10,
                    border_radius=8,
                    bgcolor=flet.Colors.YELLOW_100 if is_high else flet.Colors.GREY_100,
                    content=flet.Row([
                        flet.Column([
                            flet.Text(f"{emp['name']}", weight='bold'),
                            flet.Text(f"{emp['pos']} | Возраст: {emp['age']}"),
                            flet.Text(f"Зарплата: {emp['salary']}", 
                                     color=flet.Colors.GREEN_700 if is_high else flet.Colors.BLACK,
                                     weight="bold" if is_high else "normal")
                        ], expand=True),
                        flet.IconButton(
                            icon=flet.Icons.DELETE, 
                            icon_color=flet.Colors.RED, 
                            on_click=lambda _, id=emp['id']: self.delete_employee(id)
                        )
                    ])
                )
            )
        self.page.update()

    def clear_inputs(self):
        self.first_name.value = ""
        self.last_name.value = ""
        self.age.value = ""
        self.salary.value = ""
        self.position.value = None
        self.page.update()

if __name__ == '__main__':
    flet.app(target=main if 'main' in locals() else lambda page: EmployeeApp(page))