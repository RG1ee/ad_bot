from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.keyboards.inline import services_keyboard


async def profile(message: types.Message):
    await message.answer("<b>Профиль:</b>\nАнкета отсутствует")


async def help(message: types.Message):
    await message.answer("ПОМОЩЬ")


async def services(message: types.Message):
    keyboard = services_keyboard()
    await message.answer("Все наши услуги", reply_markup=keyboard)


def register_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(help, Text("Помощь🛟"), state="*")
    dp.register_message_handler(profile, Text("Профиль👤"), state="*")
    dp.register_message_handler(services, Text("Все услуги🔥"), state="*")
