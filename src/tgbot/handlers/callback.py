from aiogram import types, Dispatcher

from tgbot.keyboards.inline import help_pages_keyboard
from tgbot.misc.help_data import help_information, addictionPage, returnPage, subtractionPage


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
        parse_mode='html'
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
        parse_mode='html'
    )


def register_all_callback(dp: Dispatcher):

    dp.register_callback_query_handler(
        pageBack,
        lambda callback: "back" in callback.data,
        state="*"
    )

    dp.register_callback_query_handler(
        pageForward,
        lambda callback: "forward" in callback.data,
        state="*"
    )
