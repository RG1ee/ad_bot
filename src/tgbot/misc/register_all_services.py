from aiogram import Dispatcher

from tgbot.filters.admin import AdminFilter
from tgbot.handlers.users import register_functions_user
from tgbot.misc.set_bot_commands import set_default_commands
from tgbot.handlers.states.states_for_forms import register_state_form
from tgbot.handlers.callback import register_all_callback


def register_all_filters(dp: Dispatcher):
    dp.filters_factory.bind(AdminFilter)


def register_all_handlers(dp: Dispatcher):
    register_functions_user(dp)
    register_state_form(dp)
    register_all_callback(dp)


async def register_all_services(dp: Dispatcher):
    register_all_filters(dp)
    register_all_handlers(dp)
    await set_default_commands(dp)
