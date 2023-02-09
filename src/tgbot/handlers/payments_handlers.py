from datetime import datetime

from aiogram import types, dispatcher

from settings.const import PROVIDER_TOKEN
from tgbot.database.db_sqlite import DataBaseHelper


def build_cart(username_id) -> list:
    db = DataBaseHelper()
    prices = [
        types.LabeledPrice(
            label=product[1], amount=product[2] * 100
        ) for product in db.select_products_from_cart(username_id)
    ]
    print(db.select_form(username_id))

    return prices


async def buy_process(callback: types.CallbackQuery):
    await callback.bot.delete_message(
        callback.message.chat.id,
        callback.message.message_id
    )
    await callback.message.bot.send_invoice(
        callback.message.chat.id,
        title="Размещение вакансии в канал",
        description="Оплатите товары",
        payload="example",
        provider_token=PROVIDER_TOKEN,
        currency="rub",
        start_parameter="example",
        prices=build_cart(callback.from_user.id),
        need_email=True
    )


async def checkout_process(pre_checkout: types.PreCheckoutQuery):
    await pre_checkout.bot.answer_pre_checkout_query(
        pre_checkout.id, ok=True, error_message="что-то пошло не так"
    )


async def successful_payment(message: types.Message):
    db = DataBaseHelper()
    data_to_save = {
        "id_from": db.select_form(message.from_user.id)[0][0],
        "user_id": message.from_user.id,
        "date": datetime.now()
    }
    db.clear_cart(message.from_user.id)
    db.add_to_paid_orders(
        data_to_save
    )
    await message.bot.send_message(
        message.chat.id,
        "Оплата прошла"
    )


def register_payments_handlers(dp: dispatcher.Dispatcher):
    dp.register_callback_query_handler(
        buy_process,
        lambda callback: "buy" in callback.data
    )
    dp.register_pre_checkout_query_handler(
        checkout_process,
        lambda _: True,
        state="*"
    )
    dp.register_message_handler(
        successful_payment,
        content_types=types.ContentTypes.SUCCESSFUL_PAYMENT,
        state="*"
    )
