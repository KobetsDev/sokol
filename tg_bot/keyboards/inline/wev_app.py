from aiogram import types
from loader import PAYMENTS_URL


def webAppKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    webApp = types.WebAppInfo(url=PAYMENTS_URL)
    one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webApp)
    keyboard.add(one_butt)
    return keyboard
