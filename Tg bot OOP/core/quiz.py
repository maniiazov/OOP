class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "Столица Испании?",
                "options": ["Мадрид", "Бишкек", "Пекин"],
                "correct": "Мадрид"
            },
            {
                "question": "123 + 123?",
                "options": ["123123", "246", "528"],
                "correct": "246"
            },
            {
                "question": "БМВ или Мерседес?",
                "options": ["Ауди", "Чанган", "Мерседес", "БМВ"],
                "correct": "БМВ"
            },
            {
                "question": "Столица Франции?",
                "options": ["Берлин", "Париж", "Рим", "Мадрид"],
                "correct": "Париж"
            },
            {
                "question": "2 + 2 = ?",
                "options": ["3", "4", "5", "22"],
                "correct": "4"
            },
            {
                "question": "Самый большой океан?",
                "options": ["Атлантический", "Индийский", "Тихий", "Северный Ледовитый"],
                "correct": "Тихий"
            },
            {
                "question": "Какой язык понимает Python?",
                "options": ["Русский", "Английский", "Python", "Жесты"],
                "correct": "Python"
            },
            {
                "question": "Что выведет print(1 == 1)?",
                "options": ["1", "True", "False", "Error"],
                "correct": "True"
            },
            {
                "question": "Кто создал Python?",
                "options": ["Илон Маск", "Гвидо ван Россум", "Билл Гейтс", "Линус Торвальдс"],
                "correct": "Гвидо ван Россум"
            },
            {
                "question": "Какой файл запускает Django-сервер?",
                "options": ["run.py", "start.py", "manage.py", "server.py"],
                "correct": "manage.py"
            },
            {
                "question": "Что значит HTML?",
                "options": [
                    "Hyper Text Markup Language",
                    "High Text Machine Language",
                    "Hyperlinks Text Making Language",
                    "Home Tool Markup Language"
                ],
                "correct": "Hyper Text Markup Language"
            },
            {
                "question": "Какой символ используется для комментариев в Python?",
                "options": ["//", "#", "<!-- -->", "/* */"],
                "correct": "#"
            },
            {
                "question": "Что из этого НЕ является типом данных в Python?",
                "options": ["int", "str", "float", "char"],
                "correct": "char"
            },
            {
                "question": "Как правильно создать список?",
                "options": ["()", "{}", "[]", "<>"],
                "correct": "[]"
            },
            {
                "question": "Что вернёт len('Python')?",
                "options": ["5", "6", "7", "Ошибка"],
                "correct": "6"
            },
            {
                "question": "Какой оператор используется для проверки равенства?",
                "options": ["=", "==", "!=", "=>"],
                "correct": "=="
            },
            {
                "question": "Что такое Git?",
                "options": [
                    "Язык программирования",
                    "База данных",
                    "Система контроля версий",
                    "Текстовый редактор"
                ],
                "correct": "Система контроля версий"
            },
            {
                "question": "Что делают программисты, когда код не работает?",
                "options": [
                    "Паникуют",
                    "Гуглят",
                    "Чинят",
                    "Всё вышеперечисленное"
                ],
                "correct": "Всё вышеперечисленное"
            }
        ]

    def get_question(self, index):
        if 0 <= index < len(self.questions):
            return self.questions[index]
        return None

    def total_questions(self):
        return len(self.questions)
