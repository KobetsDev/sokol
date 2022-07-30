from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Text
from loader import bot
from keyboards.default.main_kb import main_kb

from utils.door.main_door import opendoor

@dp.message_handler(Text(equals="Открыть дверь"),state="*")
async def admin_login(message: types.Message):
    status = opendoor()
    print(status)
    if not status:
        await bot.send_message(message.from_user.id, f"Дверь открыта, проходите", reply_markup=main_kb)
        # add door as opened
        #dbf.door_opened(message.from_user.id)
    else:
        await bot.send_message(message.from_user.id, f"Возникла какая-то ошибка. Пожалуйста воспользуйтесь звонком", reply_markup=main_kb)
