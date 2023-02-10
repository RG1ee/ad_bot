from datetime import datetime

from aiogram import types, dispatcher

from settings.const import PROVIDER_TOKEN
from tgbot.database.db_sqlite import DataBaseHelper


def build_cart(username_id: int | None) -> tuple[list[dict], str]:
    db = DataBaseHelper()
    prices = [
        dict(
            label=product[1], amount=product[2] * 100
        ) for product in db.select_products_from_cart(username_id)
    ]
    services = ""
    for label in prices:
        services += f" {label['label']}"

    return prices, services.strip()


async def buy_process(callback: types.CallbackQuery):
    db = DataBaseHelper()

    if db.select_form(callback.from_user.id) == []:
        await callback.answer(
            text="Вы ещё не заполнили анкету",
            show_alert=True
        )
        return

    await callback.bot.delete_message(
        callback.message.chat.id,
        callback.message.message_id
    )

    await callback.message.bot.send_invoice(
        callback.message.chat.id,
        title="Размещение рекламного поста",
        description="Оплатите товары",
        payload=build_cart(callback.from_user.id)[1],
        provider_token=PROVIDER_TOKEN,
        currency="rub",
        start_parameter="123",
        prices=build_cart(callback.from_user.id)[0],
        need_email=True
    )


async def checkout_process(pre_checkout: types.PreCheckoutQuery):
    await pre_checkout.bot.answer_pre_checkout_query(
        pre_checkout.id, ok=True, error_message="Что-то пошло не так"
    )


async def successful_payment(message: types.Message):
    db = DataBaseHelper()
    data_to_save = {
        "id_form": db.select_form(message.from_user.id)[0][0],
        "user_id": message.from_user.id,
        "date": datetime.now(),
        "services": message.successful_payment.invoice_payload
    }
    db.clear_cart(message.from_user.id)
    db.add_to_paid_orders(
        data_to_save
    )
    await message.bot.send_message(
        message.chat.id,
        "<b>Оплата</b>\n\n"
        "Успешно ✅\n" +
        "Анкета отправлена на модерацию\n" +
        "Я сообщу Вам когда её опубликуют"
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
