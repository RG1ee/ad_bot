from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.misc.help_data import help_information, default_page
from tgbot.keyboards.inline import help_pages_keyboard, services_keyboard, profile_keyboard
from tgbot.misc.decorators import check_user_status


@check_user_status
async def profile(message: types.Message):
    keyboard = profile_keyboard()
    await message.bot.send_message(
        message.chat.id,
        text="<b>Профиль\n\n</b>" +
        f"{message.from_user.first_name} {message.from_user.last_name}",
        reply_markup=keyboard
    )


@check_user_status
async def help(message: types.Message):
    default_page()
    keyboard = help_pages_keyboard()
    await message.answer(
        text=help_information[0],
        reply_markup=keyboard
    )


@check_user_status
async def services(message: types.Message):
    keyboard = services_keyboard()
    await message.answer("Все наши услуги", reply_markup=keyboard)


def register_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(help, Text("Помощь🛟"), state="*")
    dp.register_message_handler(profile, Text("Профиль👤"), state="*")
    dp.register_message_handler(services, Text("Все услуги🔥"), state="*")
