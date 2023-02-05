from aiogram import types


def main_keyboard() -> types.ReplyKeyboardMarkup:
    keyboard = types.ReplyKeyboardMarkup(
        resize_keyboard=True, input_field_placeholder="Главное меню"
    )
    keyboard.add(
        types.KeyboardButton(text="Профиль👤"),
        types.KeyboardButton(text="Заполнить анкету📋"),
        types.KeyboardButton(text="Все услуги🔥")
    )
    keyboard.row(
        types.KeyboardButton(text="История заказов🕖"),
        types.KeyboardButton(text="Помощь🛟")
    )

    return keyboard


def admin_keyboard(main_keyboard: types.ReplyKeyboardMarkup):
    keyboard = main_keyboard
    keyboard.row(
        types.KeyboardButton(
            text="Оплаченные анкеты"
        ),
        types.KeyboardButton(
            text="Посмотреть анкеты"
        ),
        types.KeyboardButton(
            text="Выключить уведомления"
        )
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
