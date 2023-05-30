from aiogram.fsm.state import StatesGroup, State

class TaskState(StatesGroup):
    service = State()
    name = State()
    text = State()
    date = State()
    price = State()
    address = State()