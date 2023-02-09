from aiogram import types, dispatcher

from tgbot.misc.cart_fromat import cart

from tgbot.misc.help_data import help_information, addiction_page, return_page, subtraction_page
from tgbot.misc.service_fromat import service_information_format
from tgbot.misc.decorators import check_user_status
from tgbot.database.db_sqlite import DataBaseHelper
from tgbot.keyboards.inline import (
    help_pages_keyboard,
    services_keyboard,
    packages_keyboard,
    back_and_cart_keyboard, back_to_menu_keyboard, profile_keyboard,
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


@check_user_status
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
    keyboard = back_and_cart_keyboard(callback.data.split(":")[1])

    await callback.bot.delete_message(callback.message.chat.id, callback.message.message_id)
    await callback.message.answer(
        text=service_information_format(callback.data.split(":")[1]),
        reply_markup=keyboard
    )


async def add_to_cart(callback: types.CallbackQuery):
    db = DataBaseHelper()
    service_data = db.select_service_with_key(callback.data.split(":")[1])
    cart_data = db.check_product_in_cart(callback.from_user.id)
    try:
        for i in cart_data:
            if callback.data.split(":")[1] in i:
                await callback.answer(
                    text="Услуга уже добавлена в корзину",
                    show_alert=True
                )
                return
    except Exception:
        pass

    db.add_product_to_cart(callback.from_user.id, service_data[0])
    await callback.answer(
        text=f"Услуга публикации в канале «{service_data[0][0]}» добавлена в корзину",
        show_alert=True
    )


async def show_cart(callback: types.CallbackQuery):
    db = DataBaseHelper()
    all_products_from_cart = db.select_products_from_cart(callback.from_user.id)
    await callback.bot.delete_message(
        callback.message.chat.id, callback.message.message_id
    )
    keyboard = back_to_menu_keyboard()
    if len(all_products_from_cart) > 0:
        keyboard.row(
            types.InlineKeyboardButton(
                text="Очистить корзину",
                callback_data="clear_cart"
            ),
            types.InlineKeyboardButton(
                text="Оплатить",
                callback_data="buy"
            )
        )

        await callback.bot.send_message(
            callback.message.chat.id,
            text=cart(all_products_from_cart),
            reply_markup=keyboard
        )
    else:
        await callback.bot.send_message(
            callback.message.chat.id,
            text="Корзина пуста",
            reply_markup=keyboard
        )


async def return_to_services_list(callback: types.CallbackQuery):
    keyboard = services_keyboard()
    await callback.bot.delete_message(
        callback.message.chat.id, callback.message.message_id
    )
    await callback.message.answer("Все наши услуги", reply_markup=keyboard)


async def back_to_menu(callback: types.CallbackQuery):
    keyboard = profile_keyboard()
    await callback.bot.delete_message(
        callback.message.chat.id, callback.message.message_id
    )
    await callback.bot.send_message(
        callback.message.chat.id,
        text="<b>Профиль</b>\n\n" +
        f"{callback.from_user.first_name} {callback.from_user.last_name}",
        reply_markup=keyboard
    )


async def clear_cart(callback: types.CallbackQuery):
    db = DataBaseHelper()
    db.clear_cart(callback.from_user.id)

    keyboard = back_to_menu_keyboard()

    await callback.bot.delete_message(
        callback.message.chat.id, callback.message.message_id
    )
    await callback.bot.send_message(
        callback.message.chat.id,
        text="Корзина пуста",
        reply_markup=keyboard
    )


def register_all_callback(dp: dispatcher.Dispatcher):
    dp.register_callback_query_handler(
        clear_cart,
        lambda callback: "clear_cart" in callback.data,
        state="*"
    )
    dp.register_callback_query_handler(
        back_to_menu,
        lambda callback: "back_to_menu" in callback.data,
        state="*"
    )
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
    dp.register_callback_query_handler(
        show_cart,
        lambda callback: "cart" in callback.data,
        state="*"
    )
