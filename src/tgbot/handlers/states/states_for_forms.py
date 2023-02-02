from aiogram import types, dispatcher
from aiogram.dispatcher.filters import Text


from tgbot.misc.form_format import format
from tgbot.keyboards.reply import cancel_keyboard, confirm_keyboard, main_keyboard
from tgbot.misc.states.states import FSMForm


async def cancel_handler(message: types.Message, state: dispatcher.FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    keyboard = main_keyboard()
    await state.finish()
    await message.answer(
        'Заполнение анкеты отменено, возвращение в главное меню',
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
            "Пришли мне текст"
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
            "Пришли мне текст"
        )
        return

    async with state.proxy() as data:
        data['company_discription'] = message.text

    await FSMForm.next()
    await message.answer(
        "Опишите, что именно будет выполнять работник?"
    )


async def responsibilities(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Пришли мне текст"
        )
        return

    async with state.proxy() as data:
        data['responsibilities'] = message.text

    await FSMForm.next()
    await message.answer(
        "Какие требования будут к рабонику?"
    )


async def requirements(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Пришли мне текст"
        )
        return

    async with state.proxy() as data:
        data['requirements'] = message.text

    await FSMForm.next()
    await message.answer(
        "Расскажите про условия работы в Вашей компании"
    )


async def terms(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Пришли мне текст"
        )
        return

    async with state.proxy() as data:
        data['terms'] = message.text

    await FSMForm.next()
    await message.answer(
        "Теперь требуется указать способ связи с Вами и свой контакт:"
    )


async def contact_link(message: types.Message, state: dispatcher.FSMContext):
    if not message.text:
        await message.bot.send_message(
            message.from_user.id,
            "Пришли мне текст"
        )
        return

    async with state.proxy() as data:
        data['contact_link'] = message.text
        data_to_save = {
            "company_name": data["company_name"],
            "company_discription": data["company_discription"],
            "responsibilities": data["responsibilities"],
            "requirements": data["requirements"],
            "terms": data["terms"],
            "contact_link": data["contact_link"]
        }
        await state.finish()

    keyboard = confirm_keyboard()
    await message.answer(
        text=format(data_to_save),
        parse_mode='html',
        reply_markup=keyboard
    )


def register_state_form(dp: dispatcher.Dispatcher):
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
