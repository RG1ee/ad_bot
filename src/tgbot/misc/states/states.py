from aiogram.dispatcher.filters.state import State, StatesGroup


class FSMForm(StatesGroup):
    company_name = State()
    company_discription = State()
    responsibilities = State()
    requirements = State()
    terms = State()
    contact_link = State()
