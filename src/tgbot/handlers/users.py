from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text

from settings.const import CHAT_ID, CHAT_LINK
from tgbot.keyboards.reply import main_keyboard


async def profile(message: types.Message):
    await message.answer("<b>Профиль:</b>\nАнкета отсутствует", parse_mode='html')


async def help(message: types.Message):
    await message.answer("ПОМОЩЬ")


async def start_message(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}")

    sub_status = await message.bot.get_chat_member(
        chat_id=CHAT_ID,
        user_id=message.from_user.id
    )
    if sub_status.status != types.ChatMemberStatus.LEFT:
        keyboard = main_keyboard()
        await message.answer(
            text="Выберите нужное действие",
            reply_markup=keyboard
        )
        pass
    else:
        await message.answer(
            "Для начала работы "
            f"требуется подписка на телеграм канал:\n{CHAT_LINK}"
        )


def register_functions_user(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=["start"], state="*")
    dp.register_message_handler(help, commands=["help"], state="*")
    dp.register_message_handler(profile, Text("Профиль👤"), state="*")
