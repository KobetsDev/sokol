from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Хочу КОФЕ!"),
            KeyboardButton(text="Открыть дверь"),
        ],
        [
            KeyboardButton(text="Нужна помощь"),
            KeyboardButton('Переговорка'),
        ],
        [
            KeyboardButton('Открыть шлагбаум'),
            KeyboardButton('Закрыть шлагбаум')
        ]
    ],
    resize_keyboard=True
)
