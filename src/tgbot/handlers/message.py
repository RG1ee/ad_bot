from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text
from tgbot.database.db_sqlite import DataBaseHelper
from tgbot.keyboards.reply import cart_keyboard
from tgbot.misc.cart_fromat import cart

from tgbot.misc.help_data import help_information, default_page
from tgbot.keyboards.inline import help_pages_keyboard, services_keyboard
from tgbot.misc.decorators import check_user_status
from tgbot.misc.form_format_db import format_from_db


@check_user_status
async def profile(message: types.Message):
    form = format_from_db(message.from_user.id)

    await message.bot.send_message(
        message.chat.id,
        (
            f"{message.from_user.first_name} {message.from_user.last_name}\n" +
            "\n<u>Ваша текущая анкета:</u>" +
            form
        )
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
    cart = cart_keyboard()
    await message.answer(
        "<b>Услуги</b>\n\n" +
        "Добавьте нужные каналы в корзину или выберите готовый пакет услуг",
        reply_markup=keyboard
    )

    await message.bot.send_message(
        message.chat.id,
        text="После выбора, перейди в корзину и оплати",
        reply_markup=cart
    )


@check_user_status
async def show_cart(message: types.Message):
    db = DataBaseHelper()
    all_products_from_cart = db.select_products_from_cart(message.from_user.id)
    if len(all_products_from_cart) > 0:
        keyboard = types.InlineKeyboardMarkup()
        keyboard.row(
            types.InlineKeyboardButton(
                text="Очистить корзину",
                callback_data="clear_cart"
            ),
            types.InlineKeyboardButton(
                text="Оплатить",
                callback_data="buy"
            )
        )

        await message.bot.send_message(
            message.chat.id,
            text=cart(all_products_from_cart),
            reply_markup=keyboard
        )
    else:
        keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
        keyboard.add(
            types.KeyboardButton(
                "Все услуги🔥"
            )
        )
        await message.bot.send_message(
            message.chat.id,
            text="<b>Корзина</b>\n\n" +
            "Ваша корзина пустая, выберите услугу или выгодный пакет",
            reply_markup=keyboard
        )


@check_user_status
async def incorrect_command(message: types.Message):
    await message.answer(
        text="Я не понимаю Вас, выберите ответ с клавиатуры"
    )


def register_message(dp: dispatcher.Dispatcher):
    dp.register_message_handler(help, Text("Помощь🛟"), state="*")
    dp.register_message_handler(profile, Text("Моя анкета📄"), state="*")
    dp.register_message_handler(show_cart, Text("Корзина🛒"))
    dp.register_message_handler(services, Text("Все услуги🔥"), state="*")
    dp.register_message_handler(incorrect_command, state="*")
