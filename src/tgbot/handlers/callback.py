from aiogram import types, dispatcher

from tgbot.keyboards.inline import help_pages_keyboard
from tgbot.misc.help_data import help_information, addictionPage, returnPage, subtractionPage
from tgbot.keyboards.inline import packages_keyboard


async def pageBack(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if returnPage() <= 0:
        return
    subtractionPage()
    info = str(help_information[returnPage()])
    await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text=info,
        reply_markup=keyboard,
    )


async def pageForward(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if returnPage() >= len(help_information):
        return
    addictionPage()
    info = str(help_information[returnPage()])
    await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text=info,
        reply_markup=keyboard,
    )


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
        pageBack,
        lambda callback: "back" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        pageForward,
        lambda callback: "forward" in callback.data,
    )
    dp.register_callback_query_handler(
        show_packages,
        lambda callback: "service_packages" in callback.data,
        state="*"
    )
