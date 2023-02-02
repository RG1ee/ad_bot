from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text



from settings.const import CHAT_ID, CHAT_LINK
from tgbot.keyboards.reply import KB_SETTINGS, FORM_KB_SETTINGS
from tgbot.handlers.form import Form


async def profile(message: types.Message):
    await message.answer("<b>Профиль:</b>\nАнкета отсутствует", parse_mode='html')


async def form(message: types.Message):
    await message.answer("Начнём заполнять анкету")
    await message.answer(
        "Для начала напишите название Вашей компании:",
        reply_markup=FORM_KB_SETTINGS
    )
    await Form.company_name.set()


async def help(message: types.Message):
    await message.answer("ПОМОЩЬ")


async def start_message(message: types.Message):

    await message.answer(f"Здравствуйте, {message.from_user.first_name}")


    sub_status = await message.bot.get_chat_member(
        chat_id=CHAT_ID,
        user_id=message.from_user.id
        )
    if sub_status.status != types.ChatMemberStatus.LEFT:
        await message.answer(
            text="Выберите нужное действие",
            reply_markup=KB_SETTINGS)
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
    dp.register_message_handler(form, Text("Заполнить анкету📋"), state="*")
