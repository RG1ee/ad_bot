from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text

from tgbot.misc.help_data import help_information, default_page
from tgbot.keyboards.inline import help_pages_keyboard, services_keyboard, profile_keyboard
from tgbot.misc.decorators import check_user_status
from tgbot.misc.form_format_db import format_from_db


@check_user_status
async def profile(message: types.Message):
    form = format_from_db(message.from_user.id)
    keyboard = profile_keyboard()

    await message.bot.send_message(
        message.chat.id,
        text=("<b>Профиль\n\n</b>") +
        f"{message.from_user.first_name} {message.from_user.last_name}\n" +
        "\n<u>Ваша текущая анкета:</u>" +
        form,
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
    await message.answer(
        "<b>Услуги</b>\n\n" +
        "Добавьте нужные каналы в корзину или выберите готовый пакет услуг",
        reply_markup=keyboard
        )


@check_user_status
async def incorrect_command(message: types.Message):
    await message.answer(
        text="Я не понимаю Вас, выберите ответ с клавиатуры"
    )


def register_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(help, Text("Помощь🛟"), state="*")
    dp.register_message_handler(profile, Text("Профиль👤"), state="*")
    dp.register_message_handler(services, Text("Все услуги🔥"), state="*")
    dp.register_message_handler(incorrect_command, state="*")
