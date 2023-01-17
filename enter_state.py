from aiogram.fsm.state import StatesGroup, State


class EnterState(StatesGroup):
    nickname = State()
    password = State()
