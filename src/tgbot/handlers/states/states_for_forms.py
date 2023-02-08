from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text
from settings.const import CHAT_ID

from tgbot.misc.form_format import format
from tgbot.keyboards.reply import admin_keyboard, cancel_keyboard, confirm_keyboard, main_keyboard
from tgbot.misc.states.states import FSMForm
from tgbot.database.db_sqlite import DataBaseHelper


async def confirm_handler(message: types.Message, state: dispatcher.FSMContext):
    async with state.proxy() as data:
        try:
            user_status = await message.bot.get_chat_member(
                chat_id=CHAT_ID,
                user_id=message.from_user.id
            )

            if user_status.status == types.ChatMemberStatus.CREATOR:
                keyboard = admin_keyboard(main_keyboard())
            else:
                keyboard = main_keyboard()
            data_to_save = {
                "company_name": data["company_name"],
                "company_discription": data["company_discription"],
                "responsibilities": data["responsibilities"],
                "requirements": data["requirements"],
                "terms": data["terms"],
                "contact_link": data["contact_link"],
                "user_forms": data["user_forms"],
            }
            db = DataBaseHelper()
            db.insert_from(data_to_save)
            await message.answer(
                f"Анкета компании <b>{data['company_name']}</b> сохранена",
                reply_markup=keyboard
            )
            await state.finish()
        except Exception:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


async def cancel_handler(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)

    await state.finish()

    user_status = await message.bot.get_chat_member(
        chat_id=CHAT_ID,
        user_id=message.from_user.id
    )

    if user_status.status == types.ChatMemberStatus.CREATOR:
        keyboard = admin_keyboard(main_keyboard())
    else:
        keyboard = main_keyboard()

    await message.answer(
        "Заполнение анкеты отменено, возвращение в главное меню",
        reply_markup=keyboard
    )


async def start_new_form(
    message: types.Message, state: dispatcher.FSMContext
) -> None:
    current_state = await state.get_state()
    if current_state is not None:
        await state.finish()

    keyboard = cancel_keyboard()
    await message.answer("Начнём заполнять анкету")
    await message.answer(
        "Для начала напишите название Вашей компании:",
        reply_markup=keyboard
    )
    await FSMForm.first()


async def save_company_name(
    message: types.Message, state: dispatcher.FSMContext
) -> None:
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return

    async with state.proxy() as data:
        data["company_name"] = message.text

        await FSMForm.next()
        await message.answer(
            "Далее опишите, чем занимается Ваша компания?"
        )


async def company_discription(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return

    async with state.proxy() as data:
        data["company_discription"] = message.text

    await FSMForm.next()
    await message.answer(
        "Опишите, что именно будет выполнять работник?"
    )


async def responsibilities(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return

    async with state.proxy() as data:
        data["responsibilities"] = message.text.replace("\n", "\n—")

    await FSMForm.next()
    await message.answer(
        "Какие требования будут к рабонику?"
    )


async def requirements(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return

    async with state.proxy() as data:
        data["requirements"] = message.text.replace("\n", "\n—")

    await FSMForm.next()
    await message.answer(
        "Расскажите про условия работы в Вашей компании"
    )


async def terms(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return

    async with state.proxy() as data:
        data["terms"] = message.text.replace("\n", "\n—")

    await FSMForm.next()
    await message.answer(
        "Теперь требуется указать способ связи с Вами и свой контакт:"
    )


async def contact_link(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Я лучше понимаю, если мне пишут текстом😉"
        )
        return

    async with state.proxy() as data:
        keyboard = confirm_keyboard()
        try:
            if data["contact_link"] is not None:
                await message.answer(
                    "Я не понимаю Вас, выберите ответ с клавиатуры",
                    reply_markup=keyboard
                    )
                return
        except Exception:
            data["contact_link"] = message.text
            data["user_forms"] = message.from_user.id

    await message.answer(
        text=format(data),
        reply_markup=keyboard
    )


def register_state_form(dp: dispatcher.Dispatcher):
    dp.register_message_handler(
        confirm_handler,
        Text("Подтвердить✅"),
        state="*"
    )
    dp.register_message_handler(
        cancel_handler,
        Text("Отменить🛑"),
        state="*"
    )
    dp.register_message_handler(
        start_new_form, Text("Заполнить анкету📋"), state="*"
    )
    dp.register_message_handler(
        save_company_name,
        state=FSMForm.company_name,
        content_types="any"
    )
    dp.register_message_handler(
        company_discription,
        state=FSMForm.company_discription,
        content_types="any"
    )
    dp.register_message_handler(
        responsibilities,
        state=FSMForm.responsibilities,
        content_types="any"
    )
    dp.register_message_handler(
        requirements,
        state=FSMForm.requirements,
        content_types="any"
    )
    dp.register_message_handler(
        terms,
        state=FSMForm.terms,
        content_types="any"
    )
    dp.register_message_handler(
        contact_link,
        state=FSMForm.contact_link,
        content_types="any"
    )
