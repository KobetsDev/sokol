import logging
from aiogram import types
from aiogram import Dispatcher

from data.config import admins
from .notify_admins import need_assitance


async def error_msg(dp: Dispatcher, user_data: types.User):
    try:
        await dp.bot.send_message(user_data.id, "Произошла какая то ошибка. Напишите @dionisboss")
        await need_assitance(dp, user_data)
    except Exception as err:
        logging.exception(err)
