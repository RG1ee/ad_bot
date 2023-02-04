from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.misc.help_data import help_information
from tgbot.misc.help_data import defaultPage
from tgbot.keyboards.inline import help_pages_keyboard
from tgbot.keyboards.inline import services_keyboard
from tgbot.keyboards.inline import help_pages_keyboard
from tgbot.misc.help_data import help_information
from tgbot.misc.help_data import defaultPage


async def profile(message: types.Message):
    await message.answer("<b>Профиль:</b>\nАнкета отсутствует")


async def help(message: types.Message):
    defaultPage()
    keyboard = help_pages_keyboard()
    await message.answer(
        text=help_information[0],
        reply_markup=keyboard
    )


async def services(message: types.Message):
    keyboard = services_keyboard()
    await message.answer("Все наши услуги", reply_markup=keyboard)


def register_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(help, Text("Помощь🛟"), state="*")
    dp.register_message_handler(profile, Text("Профиль👤"), state="*")
    dp.register_message_handler(services, Text("Все услуги🔥"), state="*")
