import flet as ft
import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("employees.db", check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                position TEXT,
                department TEXT
            )
        """)
        self.conn.commit()

    def add_employee(self, name, position, department):
        self.cursor.execute(
            "INSERT INTO employees (name, position, department) VALUES (?, ?, ?)",
            (name, position, department)
        )
        self.conn.commit()

    def get_employees(self, search="", sort_by="name"):
        query = f"SELECT * FROM employees WHERE name LIKE ? ORDER BY {sort_by}"
        self.cursor.execute(query, (f"%{search}%",))
        return self.cursor.fetchall()

    def delete_employee(self, emp_id):
        self.cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
        self.conn.commit()

class EmployeeApp:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.title = "Учет сотрудников"
        self.db = Database()
        
        self.name_input = ft.TextField(label="ФИО", expand=True)
        self.pos_input = ft.TextField(label="Должность", width=200)
        self.dept_input = ft.TextField(label="Отдел", width=150)
        
        self.search_field = ft.TextField(
            label="Поиск...", 
            prefix_icon=ft.Icons.SEARCH,
            on_change=self.update_list
        )
        
        self.sort_options = ft.Dropdown(
            label="Сортировка",
            width=200,
            value="name",
            options=[
                ft.dropdown.Option("name", "По имени"),
                ft.dropdown.Option("position", "По должности"),
                ft.dropdown.Option("department", "По отделу"),
            ],
            on_change=self.update_list
        )

        self.results_list = ft.Column(scroll=ft.ScrollMode.ADAPTIVE, expand=True)

        self.page.add(
            ft.Row([self.name_input, ft.FloatingActionButton(icon=ft.Icons.ADD, on_click=self.add_clicked)]),
            ft.Row([self.pos_input, self.dept_input]),
            ft.Divider(),
            ft.Row([self.search_field, self.sort_options]),
            self.results_list
        )
        self.update_list()

    def add_clicked(self, e):
        if self.name_input.value:
            self.db.add_employee(self.name_input.value, self.pos_input.value, self.dept_input.value)
            self.name_input.value = self.pos_input.value = self.dept_input.value = ""
            self.update_list()

    def delete_clicked(self, emp_id):
        self.db.delete_employee(emp_id)
        self.update_list()

    def update_list(self, e=None):
        self.results_list.controls.clear()
        for emp in self.db.get_employees(self.search_field.value, self.sort_options.value):
            emp_id, name, pos, dept = emp
            self.results_list.controls.append(
                ft.ListTile(
                    leading=ft.Icon(ft.Icons.PERSON),
                    title=ft.Text(name),
                    subtitle=ft.Text(f"{pos} | {dept}"),
                    trailing=ft.IconButton(ft.Icons.DELETE, on_click=lambda e, id=emp_id: self.delete_clicked(id))
                )
            )
        self.page.update()

if __name__ == "__main__":
    ft.app(target=lambda page: EmployeeApp(page))