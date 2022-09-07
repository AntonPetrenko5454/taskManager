from aiogram.dispatcher.filters.state import StatesGroup, State

class EnterState(StatesGroup):
    nickname= State()
    password= State()
    status= State()
    conditionAcc=State()