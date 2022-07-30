from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


register_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Нужна помощь"),
            KeyboardButton('Регистрация', request_contact=True),
            KeyboardButton('Переговорка'),
        ],
    ],
    resize_keyboard=True
)
