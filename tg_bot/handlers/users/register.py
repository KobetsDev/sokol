from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_kb import main_kb
from keyboards.default.register_kb import register_kb
from utils.mongo.user_class import User
from aiogram.dispatcher.filters import Text
from utils.error import error_msg

from loader import dp


@dp.message_handler(content_types='contact')
async def register(message: types.Message):
    # check if user in db
    if User(message.from_user.id).get_info() and User(message.from_user.id).get_info().get("status") == 0:
        if await User(message.from_user.id).register_user(message.contact.phone_number):
            await message.answer(f'{message.from_user.full_name}, Вы успешно прошли регистрацию', reply_markup=main_kb)
        else:
            await error_msg(dp, message.from_user)

    else:
        await error_msg(dp, message.from_user)
