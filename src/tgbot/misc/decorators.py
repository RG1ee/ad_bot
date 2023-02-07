from aiogram import types

from settings.const import CHAT_ID, CHAT_LINK


def check_user_status(func):
    async def check_user(handlers):
        user_status = await handlers.bot.get_chat_member(
            chat_id=CHAT_ID,
            user_id=handlers.from_user.id
        )

        if user_status["status"] != types.ChatMemberStatus.LEFT:
            await func(handlers)
        else:
            await handlers.bot.send_message(
                handlers.chat.id,
                "Для начала работы "
                f"требуется подписка на телеграм канал:\n{CHAT_LINK}",
                reply_markup=types.ReplyKeyboardRemove()
            )

    return check_user
