from aiogram import types, Dispatcher


async def echo(message: types.Message):
    await message.answer("К сожалению, я не знаю данной команды😢")


def register_echo(dp: Dispatcher):
    dp.register_message_handler(
        echo, state="*"
    )
