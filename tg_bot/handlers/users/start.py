from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_kb import main_kb
from keyboards.default.register_kb import register_kb
from utils.mongo.user_class import User

from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    # check if user in db
    if User(message.from_user.id).get_info():
        if User(message.from_user.id).get_info().get("status") == 1:
            await message.answer(f'{message.from_user.full_name}, добро пожаловать Домой,', reply_markup=main_kb)
        else:
            await message.answer(f'{message.from_user.full_name}, добро пожаловать Домой,', reply_markup=register_kb)
    else:
        user = message.from_user
        user_data = {
            "username": user.username,
            "firstname": user.first_name,
            "lastname": user.last_name,
        }
        if User(message.from_user.id).add_user(user_data, message.text):
            await message.answer(f"Я не узнал вас, но это не повторится. "
                                 f"Сейчас Вам доступен ограниченный функционал, "
                                 f"но вы можете зарегистрироваться", reply_markup=register_kb)
        else:
            await message.answer("Произошла какая-то ошибка. Напишите админу @dionisboss")
