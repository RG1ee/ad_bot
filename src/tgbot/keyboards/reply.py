from aiogram import types


KB = [
    [
        types.KeyboardButton(text="Профиль👤"),
        types.KeyboardButton(text="Заполнить анкету📋"),
        types.KeyboardButton(text="Что-то ещё🔜"),
        types.KeyboardButton(text="Помощь")
    ]
]
KB_SETTINGS = types.ReplyKeyboardMarkup(
    keyboard=KB,
    resize_keyboard=True,
    input_field_placeholder="Главное меню"
)


FORM_KB = [
    [
        types.KeyboardButton(text="Отмена🛑")
    ]
]
FORM_KB_SETTINGS = types.ReplyKeyboardMarkup(
    keyboard=FORM_KB,
    resize_keyboard=True,
    input_field_placeholder="Заполнение анкеты"
)


FORM_CONFIRM_KB = [
    [
        types.KeyboardButton(text="Подтвердить✅"),
        types.KeyboardButton(text="Отмена🛑")
    ]
]
FORM_CONFIRM_KB_SETTINGS = types.ReplyKeyboardMarkup(
    keyboard=FORM_CONFIRM_KB,
    resize_keyboard=True,
    input_field_placeholder="Подтвердите заполнение"
)
