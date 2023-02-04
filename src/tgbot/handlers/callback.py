from aiogram import types, dispatcher

from tgbot.keyboards.inline import packages_keyboard


async def show_packages(callback: types.CallbackQuery):
    keyboard = packages_keyboard()

    await callback.bot.send_message(
        callback.message.chat.id,
        text="НАШИ ВЫГОДНЫЕ ПАКЕТЫ С УСЛУГАМИ",
        reply_markup=keyboard
    )
    await callback.bot.delete_message(
        callback.message.chat.id,
        callback.message.message_id
    )


def register_all_callback(dp: dispatcher.Dispatcher):
    dp.register_callback_query_handler(
        show_packages,
        lambda callback: "service_packages" in callback.data,
        state="*"
    )
