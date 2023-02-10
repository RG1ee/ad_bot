from aiogram import types, dispatcher

from tgbot.keyboards.inline import all_paid_form_keyboard
from tgbot.database.db_sqlite import DataBaseHelper


async def paid_forms(message: types.Message):
    db = DataBaseHelper()
    keyboard = all_paid_form_keyboard()
    if len(db.select_all_paid_orders()) > 0:
        await message.bot.send_message(
            message.chat.id,
            text="Все не опубликованные заказы",
            reply_markup=keyboard
        )
    else:
        await message.bot.send_message(
            message.chat.id,
            text="Заказов нет"
        )


def register_admin_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        paid_forms,
        dispatcher.filters.Text("Оплаченные анкеты"),
        is_admin=True,
        state="*"
    )
