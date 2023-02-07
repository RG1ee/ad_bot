from aiogram import types

from tgbot.database.db_sqlite import DataBaseHelper


def help_pages_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()

    keyboard.add(
            types.InlineKeyboardButton(text="<<<", callback_data="back"),
            types.InlineKeyboardButton(text=">>>", callback_data="forward")
    )

    return keyboard


def services_keyboard() -> types.InlineKeyboardMarkup:
    db = DataBaseHelper()
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    for service in db.select_all_services():
        keyboard.add(
            types.InlineKeyboardButton(
                text=f"{service[0]}",
                callback_data=f"service:{service[0]}:{service[1]}:{service[-1]}"
            )
        )

    keyboard.row(
        types.InlineKeyboardButton(
            text="ВЫГОДНЫЕ ПАКЕТЫ",
            callback_data="service_packages"
        )
    )

    return keyboard


def packages_keyboard() -> types.InlineKeyboardMarkup:
    db = DataBaseHelper()
    keyboard = types.InlineKeyboardMarkup(row_width=3)
    for package in db.select_all_packeges():
        keyboard.add(
            types.InlineKeyboardButton(
                text=f"{package[0]}",
                callback_data="pgShow"
            )
        )

    return keyboard


def back_and_cart_keyboard(service) -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text="В корзину",
            callback_data=f"add_to_cart:{service}"),
        types.InlineKeyboardButton(
            text="Назад",
            callback_data="return_services"
        )
    )

    return keyboard


def profile_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        types.InlineKeyboardButton(
            text="Корзина", callback_data="cart"
        ),
        types.InlineKeyboardButton(
            text="Мои вакансии", callback_data="my_form"
        )
    )

    return keyboard


def back_to_menu_keyboard() -> types.InlineKeyboardMarkup:
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton(
            text="Назад",
            callback_data="back_to_menu"
        )
    )

    return keyboard
