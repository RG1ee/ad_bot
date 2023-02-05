from aiogram import types, dispatcher


from tgbot.keyboards.inline import help_pages_keyboard, services_keyboard
from tgbot.misc.help_data import help_information, addictionPage, returnPage, subtractionPage
from tgbot.keyboards.inline import packages_keyboard
from tgbot.misc.service_fromat import service_information_format


async def page_back(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if returnPage() <= 0:
        return

    else:
        subtractionPage()
        info = str(help_information[returnPage()])
        await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=info,
            reply_markup=keyboard,
        )


async def page_forward(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if returnPage() >= len(help_information) - 1:
        return

    else:
        addictionPage()
        info = str(help_information[returnPage()])
        await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=info,
            reply_markup=keyboard,
        )


async def show_packages(callback: types.CallbackQuery):
    keyboard = packages_keyboard()

    await callback.bot.send_message(
        callback.message.chat.id,
        text="НАШИ ВЫГОДНЫЕ ПАКЕТЫ С УСЛУГАМИ",
        reply_markup=keyboard
    )
    await callback.bot.delete_message(
        callback.message.chat.id,
        callback.message.message_id
    )


async def show_service_info(callback: types.CallbackQuery):
    service = callback.data.split(":")[1]

    keyboard = types.InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        types.InlineKeyboardButton(
            text="В корзину",
            callback_data=f"inCart:{service}"
            ),
        types.InlineKeyboardButton(
            text="Назад",
            callback_data="returnServices"
        )
    )

    await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text=service_information_format(service),
        reply_markup=keyboard,
        parse_mode='html'
    )


async def return_to_services_list(callback: types.CallbackQuery):
    keyboard = services_keyboard()
    await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Все наши услуги", reply_markup=keyboard)


async def add_to_cart(callback: types.CallbackQuery):
    good = callback.data.split(":")[1]
    await callback.answer(
        text=f"Услуга публикации в канале «{good}» добавлена в корзину",
        show_alert=True
    )


def register_all_callback(dp: dispatcher.Dispatcher):
    dp.register_callback_query_handler(
        page_back,
        lambda callback: "back" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        page_forward,
        lambda callback: "forward" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        show_packages,
        lambda callback: "service_packages" in callback.data,
    )
    dp.register_callback_query_handler(
        show_packages,
        lambda callback: "service_packages" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        show_service_info,
        lambda callback: callback.data.startswith("service:"),
        state="*"
    )
    dp.register_callback_query_handler(
        return_to_services_list,
        lambda callback: "returnServices" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        add_to_cart,
        lambda callback: callback.data.startswith("inCart:"),
        state="*"
    )
