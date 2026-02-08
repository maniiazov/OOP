from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from core.quiz import Quiz


class BotHandlers:
    def __init__(self):
        self.router = Router()
        self.quiz = Quiz()
        self.user_data = {}
        self.register_handlers()

    def register_handlers(self):
        self.router.message.register(self.start_command, Command("start"))
        self.router.message.register(self.start_quiz, Command("quiz"))
        self.router.callback_query.register(self.handle_answer)

    async def start_command(self, message: types.Message):
        await message.answer(
            "Привет 👋\n"
            "Напиши /quiz чтобы начать викторину 🎯"
        )

    async def start_quiz(self, message: types.Message):
        user_id = message.from_user.id
        self.user_data[user_id] = {"score": 0, "q_index": 0}
        await self.send_question(message, user_id)

    async def send_question(self, message: types.Message, user_id: int):
        data = self.user_data[user_id]
        question_data = self.quiz.get_question(data["q_index"])

        if not question_data:
            await self.finish_quiz(message, user_id)
            return

        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=opt, callback_data=opt)]
                for opt in question_data["options"]
            ]
        )

        await message.answer(
            question_data["question"],
            reply_markup=keyboard
        )

    async def handle_answer(self, callback: types.CallbackQuery):
        user_id = callback.from_user.id
        data = self.user_data.get(user_id)

        if not data:
            await callback.answer("Сначала начни викторину через /quiz")
            return

        question_data = self.quiz.get_question(data["q_index"])
        selected_answer = callback.data

        if selected_answer == question_data["correct"]:
            data["score"] += 1

        data["q_index"] += 1

        await callback.answer("Ответ принят!")
        await self.send_question(callback.message, user_id)

    async def finish_quiz(self, message: types.Message, user_id: int):
        score = self.user_data[user_id]["score"]
        total = self.quiz.total_questions()

        await message.answer(
            f"🏁 Викторина окончена!\n"
            f"Твой результат: {score} из {total}"
        )

        del self.user_data[user_id]
