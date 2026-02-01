import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from confict import token

bot = Bot(token)
dp = Dispatcher()

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Привет \n Хочешь заказать пиццу?",
        reply_markup=keyboard)
keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Да"), KeyboardButton(text="Нет")]
    ],
    resize_keyboard=True)


@dp.message(lambda m: m.text == "Да")
async def yes_answer(message: types.Message):
    await message.answer("Осуждаю тебя")

@dp.message(lambda m: m.text == "Нет")
async def no_answer(message: types.Message):
    await message.answer("Уважаю")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
