from aiogram import types, Dispatcher
from settings.const import chat_id, chat_link


async def start_message(message: types.Message):

    await message.answer(f"Здравствуйте, {message.from_user.first_name}")

    sub_status = await message.bot.get_chat_member(
        chat_id=chat_id,
        user_id=message.chat.id
        )
    if sub_status.status != types.ChatMemberStatus.LEFT:
        pass
    else:
        await message.answer(
            "Для начала работы "
            f"требуется подписка на телеграм канал:\n{chat_link}"
            )


def register_start_message(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=["start"], state="*")
