from aiogram import types


def webAppKeyboard():
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    webApp = types.WebAppInfo(url='https://api.sokol.one/')
    one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webApp)
    keyboard.add(one_butt)
    return keyboard
