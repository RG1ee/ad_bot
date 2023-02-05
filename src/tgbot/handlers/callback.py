from aiogram import types, dispatcher

from tgbot.misc.help_data import help_information, addiction_page, return_page, subtraction_page
from tgbot.misc.service_fromat import service_information_format
from tgbot.keyboards.inline import (
    help_pages_keyboard,
    services_keyboard,
    packages_keyboard,
    back_and_cart_keyboard,
)


async def page_back(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if return_page() <= 0:
        return

    else:
        subtraction_page()
        info = str(help_information[return_page()])
        await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=info,
            reply_markup=keyboard,
        )


async def page_forward(callback: types.CallbackQuery):
    keyboard = help_pages_keyboard()

    if return_page() >= len(help_information) - 1:
        return

    else:
        addiction_page()
        info = str(help_information[return_page()])
        await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
        await callback.message.answer(
            text=info,
            reply_markup=keyboard
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
    service_data = callback.data.split(":")[1]
    keyboard = back_and_cart_keyboard(service_data)

    await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text=service_information_format(service_data),
        reply_markup=keyboard
    )


async def add_to_cart(callback: types.CallbackQuery):
    await callback.answer(
        text=f"Услуга публикации в канале «{callback.data.split(':')[1]}» добавлена в корзину",
        show_alert=True
    )


async def return_to_services_list(callback: types.CallbackQuery):
    keyboard = services_keyboard()
    await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer("Все наши услуги", reply_markup=keyboard)


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
        state="*"
    )
    dp.register_callback_query_handler(
        show_packages,
        lambda callback: "service_packages" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        show_service_info,
        lambda callback: callback.data.startswith("service"),
        state="*"
    )
    dp.register_callback_query_handler(
        return_to_services_list,
        lambda callback: "return_services" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        add_to_cart,
        lambda callback: callback.data.startswith("add_to_cart"),
        state="*"
    )
