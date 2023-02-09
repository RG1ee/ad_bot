from aiogram import Dispatcher

from tgbot.filters.admin import AdminFilter
from tgbot.handlers.users import register_user
from tgbot.handlers.message import register_message
from tgbot.misc.set_bot_commands import set_default_commands
from tgbot.handlers.states.states_for_forms import register_state_form
from tgbot.handlers.callback import register_all_callback
from tgbot.handlers.payments_handlers import register_payments_handlers


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp: Dispatcher):
    register_user(dp)
    register_message(dp)
    register_state_form(dp)
    register_all_callback(dp)
    register_payments_handlers(dp)


async def register_all_services(dp: Dispatcher):
    register_all_filters(dp)
    register_all_handlers(dp)
    await set_default_commands(dp)
