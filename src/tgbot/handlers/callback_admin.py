from aiogram import types, dispatcher

from tgbot.database.db_sqlite import DataBaseHelper
from tgbot.misc.form_format_db import format_from_db
from tgbot.keyboards.inline import back_to_all_orders_and_confirm_keyboard, all_paid_form_keyboard


async def show_paid_orders(callback: types.CallbackQuery):
    db = DataBaseHelper()
    callback_data = callback.data.split(":")
    print(callback_data)
    keyboard = back_to_all_orders_and_confirm_keyboard(int(callback_data[2]), int(callback_data[1]))

    await callback.bot.delete_message(
        callback.message.chat.id,
        callback.message.message_id
    )
    await callback.bot.send_message(
        callback.message.chat.id,
        ("<b>ДЛЯ НАЧАЛА ВЫЛОЖИТЕ ВАКАНСИЮ В УКАЗАННЫЕ КАНАЛЫ, А ПОТОМ НАЖМИТЕ ПОДТЕРДИТЬ</b>\n" +
         "\nАнкета\n" + format_from_db(int(callback_data[2])) +
         "<b>\nУслуга / Выгодный пакет</b>" +
         f"\n {db.select_paid_orders_by_id(callback_data[1])[0][-1]}\n" +
         "<b>\nДата оплаты</b>" +
         f"\n {db.select_paid_orders_by_id(callback_data[1])[0][3]}"),
        reply_markup=keyboard
    )


async def confirm_order(callback: types.CallbackQuery):
    callback_data = callback.data.split(":")
    print(callback.data)
    db = DataBaseHelper()
    db.confirm_paid_orders(
        int(callback_data[1]),
        int(callback_data[2])
    )
    await callback.bot.delete_message(
        callback.message.chat.id,
        callback.message.message_id
    )
    await callback.bot.send_message(
        callback.message.chat.id,
        text="Успешное подтверждение"
    )
    await callback.bot.send_message(
        callback_data[1],
        text="Ваш заказ выложен на канал!"
    )


async def back_to_all_orders(callback: types.CallbackQuery):
    keyboard = all_paid_form_keyboard()
    await callback.bot.delete_message(
        callback.message.chat.id,
        callback.message.message_id
    )
    await callback.bot.send_message(
        callback.message.chat.id,
        text="Все не опубликованные заказы",
        reply_markup=keyboard
    )


def register_admin_callback(dp: dispatcher.Dispatcher):
    dp.register_callback_query_handler(
        back_to_all_orders,
        lambda callback: "back_to_orders" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        show_paid_orders,
        lambda callback: callback.data.startswith("orders"),
        state="*"
    )
    dp.register_callback_query_handler(
        confirm_order,
        lambda callback: callback.data.startswith("confirm"),
        state="*"
    )
