from aiogram import types


def webAppKeyboard():  # создание клавиатуры с webapp кнопкой
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    # keyboard = types.ReplyKeyboardMarkup(row_width=1)  # создаем клавиатуру
    webApp = types.WebAppInfo(url="https://api.sokol.one/")  # создаем webappinfo - формат хранения url

    # data = types.WebAppData(button_text='qwe', data={'asd': '1'})  # создаем webappinfo - формат хранения url
    one_butt = types.KeyboardButton(text="Тестовая страница", web_app=webApp)  # создаем кнопку типа webapp
    keyboard.add(one_butt)  # добавляем кнопки в клавиатуру
    return keyboard