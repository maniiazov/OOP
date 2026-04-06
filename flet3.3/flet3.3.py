import flet as ft
import sqlite3


conn = sqlite3.connect("workers.db", check_same_thread=False)
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS staff (id INTEGER PRIMARY KEY, name TEXT, job TEXT)")
conn.commit()

def main(page: ft.Page):
    page.title = "Учет сотрудников"
    page.theme_mode = "dark"
    

    name_input = ft.TextField(label="ФИО", expand=True)
    job_input = ft.TextField(label="Должность", expand=True)
    results_list = ft.Column()

    def update_list(e=None):
        results_list.controls.clear()
        search_term = f"%{search_field.value}%"
        sort_column = sort_dd.value if sort_dd.value else "name"
        
        cur.execute(f"SELECT * FROM staff WHERE name LIKE ? ORDER BY {sort_column}", (search_term,))
        
        for row in cur.fetchall():
            results_list.controls.append(
                ft.ListTile(
                    leading=ft.Icon("person"),
                    title=ft.Text(row[1]),
                    subtitle=ft.Text(row[2]),
                    trailing=ft.IconButton(
                        icon="delete",
                        on_click=lambda _, id=row[0]: delete_person(id)
                    )
                )
            )
        page.update()

    def add_person(e):
        if name_input.value:
            cur.execute("INSERT INTO staff (name, job) VALUES (?, ?)", (name_input.value, job_input.value))
            conn.commit()
            name_input.value = job_input.value = ""
            update_list()

    def delete_person(person_id):
        cur.execute("DELETE FROM staff WHERE id = ?", (person_id,))
        conn.commit()
        update_list()


    search_field = ft.TextField(label="Поиск...", on_change=update_list, expand=True)
    sort_dd = ft.Dropdown(
        label="Сортировка",
        value="name",
        options=[
            ft.dropdown.Option("name", "По имени"),
            ft.dropdown.Option("job", "По должности"),
        ],
        width=150
    )
    sort_dd.on_change = update_list

    page.add(
        ft.Text("Регистрация сотрудников", size=25, weight="bold"),
        ft.Row([name_input, job_input]),
        ft.ElevatedButton("Добавить", icon="add", on_click=add_person),
        ft.Divider(),
        ft.Row([search_field, sort_dd]),
        results_list
    )

    update_list()

ft.app(target=main)