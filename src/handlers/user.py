from aiogram import types, Dispatcher


async def start_message(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.username}")


def register_start_message(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=["start"], state="*")
