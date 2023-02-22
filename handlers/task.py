import dp as dp
from aiogram import types, Dispatcher, Router
from aiogram.fsm.context import FSMContext

from controllers.task_controller import TaskController
from keyboards.main import mainKeyboard
from keyboards.task import getTaskKeyboard, addTaskKeyboard
from aiogram.filters import Text

from task_state import TaskState

router = Router()


async def exitButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Вы уверены, что хотите выйти?')
    await call.answer()


async def yesButtonClick(call: types.CallbackQuery):
    # TODO: Реализация авторизации для выхода и выхода
    await call.message.answer('Войдите в аккаунт или зарегестрируйтесь')


async def noButtonClick(call: types.CallbackQuery):
    await call.message.answer('Выберите действие', reply_markup=mainKeyboard)
    await call.answer()

@router.callback_query(Text(text='addTaskButton_click'))
async def start_making_task(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Выберите критерий задания')
    await state.set_state(TaskState.criteria)


@router.message(TaskState.criteria)
async def get_criteria(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(criteria=call.message.text)
    await call.message.answer('Придумайте название вашей задаче')
    await state.set_state(TaskState.name)


@router.message(TaskState.name)
async def get_name(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(name=call.message.text)
    await call.message.answer('Напишите цель вашей задачи')
    await state.set_state(TaskState.text)


@router.message(TaskState.text)
async def get_text(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(text=call.message.text)
    await call.message.answer('Напишите дату к которой эту задачу должны выполнить')
    await state.set_state(TaskState.date)


@router.message(TaskState.date)
async def get_date(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(date=call.message.text)
    await call.message.answer('Напишите место работы , если такого нет , то можете поставить <->')
    await state.set_state(TaskState.address)

@router.message(TaskState.address)
async def get_address(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(address=call.message.text)
    await call.message.answer('Укажите желаемую стоимость')
    await state.set_state(TaskState.price)
@router.message(TaskState.price)
async def get_price(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(price=call.message.text)
    data = await state.get_data()
    await call.message.answer('Правильно ли вы ввели данные задачи?\n'
                              f"Критерии: {data['criteria']}\nНазвание: {data['name']}\nЦель: {data['text']}\nДата: {data['date']}\nАдрес: {data['address']}\nЦена: {data['price']}"
                              , reply_markup=addTaskKeyboard)

@router.callback_query(Text(text='addTaskCheckYesButton_click'))
async def add_task(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Задание успешно добавлено в список задач',reply_markup=mainKeyboard)
    data = await state.get_data()
    TaskController.add_new_task(data['criteria'], data['name'], data['text'], data['date'], data['address'], data['price'], call.from_user.id)
    await state.clear()


@router.callback_query(Text(text='addTaskCheckNoButton_click'))
async def redo_task(call:types.CallbackQuery,state: FSMContext):
    await state.clear()
    await call.message.answer('выберите критерий задания')
    await state.set_state(TaskState.criteria)

async def backToEnterButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите действие', reply_markup=mainKeyboard)
    await call.answer()


@router.callback_query(Text(text='addTaskButton_click'))
async def giveTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('')
    await call.answer()


def registerHandlersTask(dp: Dispatcher):
    dp.register_callback_query_handler(exitButtonClick, lambda call: call.data == 'exitButton_click', state='*')
    # TODO: Пересечение callback
    # dp.register_callback_query_handler(yesButtonClick, lambda call: call.data == 'yesButton_click', state='*')
    # dp.register_callback_query_handler(noButtonClick, lambda call: call.data == 'noButton_click', state='*')
    dp.register_callback_query_handler(backToEnterButtonClick, lambda call: call.data == 'backToEnterButton_click',
                                       state='*')
