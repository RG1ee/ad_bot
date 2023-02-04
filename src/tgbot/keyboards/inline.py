from aiogram import types

from tgbot.database.db_sqlite import DataBaseHelper


def services_keyboard() -> types.InlineKeyboardMarkup:
    db = DataBaseHelper()
    keyboard = types.InlineKeyboardMarkup(row_width=4)
    for service in db.select_all_services():
        keyboard.add(
            types.InlineKeyboardButton(
                text=f"{service[0]}",
                callback_data=f"{service[0]}"
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
                callback_data=f"{package[0]}"
            )
        )

    return keyboard
