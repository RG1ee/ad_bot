from aiogram import types


def main_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, input_field_placeholder="Главное меню"
    )
    keyboard.add(
        types.KeyboardButton(text="Профиль👤"),
        types.KeyboardButton(text="Заполнить анкету📋")
    )
    keyboard.row(
        types.KeyboardButton(text="Что-то ещё🔜"),
        types.KeyboardButton(text="Помощь")
    )

    return keyboard


def cancel_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, input_field_placeholder="Заполнение анкеты"
    )
    keyboard.add(
        types.KeyboardButton(text="Отменить🛑")
    )

    return keyboard


def confirm_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True,
        input_field_placeholder="Подтвердить заполнение"
    )
    keyboard.add(
        types.KeyboardButton(text="Подтвердить✅"),
        types.KeyboardButton(text="Отменить🛑")
    )

    return keyboard
