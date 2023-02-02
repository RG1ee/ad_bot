from aiogram import types, Dispatcher

from settings.const import CHAT_ID, CHAT_LINK


async def start_message(message: types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}")

    sub_status = await message.bot.get_chat_member(
        CHAT_ID, message.from_user.id
    )
    if sub_status.status != types.ChatMemberStatus.LEFT:
        pass
    else:
        await message.answer(
            "Для начала работы "
            f"требуется подписка на телеграм канал:\n{CHAT_LINK}"
            )


def register_start_message(dp: Dispatcher):
    dp.register_message_handler(
        start_message, commands=["start"], state="*"
    )
