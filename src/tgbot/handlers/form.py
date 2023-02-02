from aiogram import types, Dispatcher


from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext


from tgbot.misc.form_format import format
from tgbot.keyboards.reply import KB_SETTINGS, FORM_CONFIRM_KB_SETTINGS


class Form(StatesGroup):
    company_name = State()
    company_discription = State()
    responsibilities = State()
    requirements = State()
    terms = State()
    contact_link = State()


async def confirm_handler(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        try:
            await message.answer(
                f"Анкета компании <b>{data['company_name']}</b> сохранена",
                reply_markup=KB_SETTINGS,
                parse_mode='html'
                )
            await state.finish()
        except:
            await message.bot.delete_message(chat_id=message.chat.id, message_id=message.message_id)


async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.answer(
        'Заполнение анкеты отменено, возвращение в главное меню',
        reply_markup=KB_SETTINGS
        )


async def company_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_name'] = message.text

    await Form.next()
    await message.answer(
        "Далее опишите, чем занимается Ваша компания?"
    )


async def company_discription(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['company_discription'] = message.text

    await Form.next()
    await message.answer(
        "Опишите, что именно будет выполнять работник?"
    )


async def responsibilities(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['responsibilities'] = message.text

    await Form.next()
    await message.answer(
        "Какие требования будут к рабонику?"
    )


async def requirements(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['requirements'] = message.text

    await Form.next()
    await message.answer(
        "Расскажите про условия работы в Вашей компании"
    )


async def terms(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['terms'] = message.text

    await Form.next()
    await message.answer(
        "Теперь требуется указать способ связи с Вами и свой контакт:"
    )


async def contact_link(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['contact_link'] = message.text
    

    await message.answer(
        text=format(data),
        parse_mode='html',
        reply_markup=FORM_CONFIRM_KB_SETTINGS
        )


def register_form(dp: Dispatcher):
    dp.register_message_handler(confirm_handler, Text("Подтвердить✅") ,state='*')
    dp.register_message_handler(cancel_handler, Text("Отмена🛑") ,state='*')
    dp.register_message_handler(company_name, state=Form.company_name)
    dp.register_message_handler(company_discription, state=Form.company_discription)
    dp.register_message_handler(responsibilities, state=Form.responsibilities)
    dp.register_message_handler(requirements, state=Form.requirements)
    dp.register_message_handler(terms, state=Form.terms)
    dp.register_message_handler(contact_link, state=Form.contact_link)
