import sqlite3

class Database:
    def __init__(self, db_name='todo.db'):
        self.connection = sqlite3.connect(db_name, check_same_thread=False)
        self.cursor = self.connection.cursor()
        self._create_table()
    
    def _create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS classmates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER UNIQUE,
                step INTEGER DEFAULT 0,
                f1 TEXT, f2 TEXT, f3 TEXT, f4 TEXT, f5 TEXT, 
                f6 TEXT, f7 TEXT, f8 TEXT, f9 TEXT, f10 TEXT
            )
        """)
        self.connection.commit()

    def execute(self, query, params=()):
        self.cursor.execute(query, params)
        self.connection.commit()

    def fetchone(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchone()

    def fetchall(self, query, params=()):
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

db = Database()

def get_registration_response(user_id, text):
    fields = [
        "ФИО", "Возраст", "Группа", "Телефон", "Email", 
        "Хобби", "GitHub", "Город", "Предмет", "Ноутбук"
    ]

    user = db.fetchone("SELECT step FROM classmates WHERE user_id = ?", (user_id,))

    if text == "/start":
        db.execute("INSERT OR REPLACE INTO classmates (user_id, step) VALUES (?, 0)", (user_id,))
        return f"1. {fields[0]}:"

    if user:
        step = user[0]
        if step < 10:
            db.execute(f"UPDATE classmates SET f{step+1} = ?, step = ? WHERE user_id = ?", 
                       (text, step + 1, user_id))
            
            if step + 1 < 10:
                return f"{step + 2}. {fields[step + 1]}:"
            else:
                return "Регистрация завершена."

    return "Напишите /start"