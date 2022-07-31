from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.main_kb import main_kb
from keyboards.default.register_kb import register_kb
from keyboards.inline.wev_app import webAppKeyboard
from utils.mongo.user_class import User
from aiogram.types.message import ContentType
from loader import dp, bot


@dp.pre_checkout_query_handler(lambda query: True)
async def process_pre_checkout_query(pre_checkout_query: types.PreCheckoutQuery):
    print('qwe', pre_checkout_query)
    await bot.answer_pre_checkout_query(pre_checkout_query.id, ok=True)


@dp.message_handler(content_types=ContentType.SUCCESSFUL_PAYMENT)
async def process_successful_payment(message: types.Message):
    print('successful_payment:')
    pmnt = message.successful_payment.to_python()
    for key, val in pmnt.items():
        print(f'{key} = {val}')

    await bot.answer(
        message.chat.id, f'''
Ура! Платеж на сумму `{message.successful_payment.total_amount // 100} {message.successful_payment.currency}` совершен успешно!
Приятного ожидания!
Заказать ещё своему другу -  [/buy](/buy "Заказать ещё")
''',  parse_mode='MarkdownV2'
    )
