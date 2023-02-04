from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text


async def profile(message: types.Message):
    await message.answer("<b>Профиль:</b>\nАнкета отсутствует")


async def help(message: types.Message):
    await message.answer("ПОМОЩЬ")


def register_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(help, Text("Помощь🛟"), state="*")
    dp.register_message_handler(profile, Text("Профиль👤"), state="*")
