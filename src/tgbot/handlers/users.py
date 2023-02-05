from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from settings.const import CHAT_ID, CHAT_LINK
from tgbot.keyboards.reply import main_keyboard, admin_keyboard
from tgbot.database.db_sqlite import DataBaseHelper


async def profile(message: types.Message):
    await message.answer("<b>Профиль:</b>\nАнкета отсутствует")


async def start_message(message: types.Message, state: FSMContext):
    await message.answer(f"Здравствуйте, {message.from_user.first_name}")

    await state.finish()

    user_status = await message.bot.get_chat_member(
        chat_id=CHAT_ID,
        user_id=message.from_user.id
    )

    if user_status.status == types.ChatMemberStatus.CREATOR:
        keyboard = admin_keyboard()
        await message.answer(
            text="Выберите нужное действие",
            reply_markup=keyboard
        )

    elif user_status.status != types.ChatMemberStatus.LEFT:
        db = DataBaseHelper()
        db.insert_user(message.from_user.id)
        keyboard = main_keyboard()
        await message.answer(
            text="Выберите нужное действие",
            reply_markup=keyboard
        )

    else:
        await message.answer(
            "Для начала работы "
            f"требуется подписка на телеграм канал:\n{CHAT_LINK}"
        )


def register_user(dp: Dispatcher):
    dp.register_message_handler(start_message, commands=["start"], state="*")
