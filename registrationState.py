from aiogram.dispatcher.filters.state import StatesGroup, State


class RegistrationState(StatesGroup):
    nickname = State()
    password = State()
    fullName = State()
    phoneNumber = State()
    email = State()
