from aiogram import types, Dispatcher, Router
from aiogram.fsm.context import FSMContext
from aiogram.types import CallbackQuery
from aiogram3_calendar import DialogCalendar, SimpleCalendar, simple_cal_callback

from controllers.service_controller import ServiceController
from controllers.task_controller import TaskController
from keyboards.main import mainKeyboard
from aiogram.filters import Text

from keyboards.services import getServicesKeyboard
from keyboards.task import addTaskKeyboard
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
    await call.message.edit_text('Выберите критерий задания', reply_markup=getServicesKeyboard('task'))
    await state.set_state(TaskState.service)


@router.callback_query(Text(startswith='task_service_'), TaskState.service)
async def serviceClick(call: types.CallbackQuery, state: FSMContext):
    serviceId = int(call.data.split('_')[2])
    await state.update_data(service=serviceId)
    keyboard = getServicesKeyboard('task', serviceId)
    if keyboard:
        await call.message.edit_text('Выберите род деятельности', reply_markup=keyboard)
    else:
        await call.message.edit_text('Придумайте название вашей задаче')
        await state.set_state(TaskState.name)
    await call.answer()


@router.message(TaskState.name)
async def get_name(message: types.Message, state: FSMContext):
    await state.update_data(name=message.text)
    await message.answer('Напишите цель вашей задачи')
    await state.set_state(TaskState.text)


@router.message(TaskState.text)
async def get_text(message: types.Message, state: FSMContext):
    await state.update_data(text=message.text)
    await message.answer('Напишите дату к которой эту задачу должны выполнить',
                         reply_markup=await SimpleCalendar().start_calendar())


@router.callback_query(simple_cal_callback.filter())
async def process_simple_calendar(callback_query: CallbackQuery, callback_data: dict, state: FSMContext):
    selected, date = await SimpleCalendar().process_selection(callback_query, callback_data)
    if selected:
        await state.update_data(date=f'{date.strftime("%d/%m/%Y")}')
        await callback_query.message.answer('Напишите место работы , если такого нет , то можете поставить "-"')
        await state.set_state(TaskState.address)


@router.message(TaskState.address)
async def get_address(message: types.Message, state: FSMContext):
    await state.update_data(address=message.text)
    await message.answer('Укажите желаемую стоимость')
    await state.set_state(TaskState.price)


@router.message(TaskState.price)
async def get_price(message: types.Message, state: FSMContext):
    await state.update_data(price=message.text)
    data = await state.get_data()
    await message.answer('Правильно ли вы ввели данные задачи?\n'
                         f"Критерии : {ServiceController.getServiceName(data['service'])}\nНазвание: {data['name']}\nЦель: {data['text']}\nДата: {data['date']}\nАдрес: {data['address']}\nЦена: {data['price']}"
                         , reply_markup=addTaskKeyboard)


@router.callback_query(Text(text='addTaskYesButton_click'))
async def add_task(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Задание успешно добавлено в список задач', reply_markup=mainKeyboard)
    data = await state.get_data()
    TaskController.add_new_task(data['service'], data['name'], data['text'], data['date'], data['address'],
                                data['price'], call.from_user.id, call.message.date, 'new')
    await state.clear()


@router.callback_query(Text(text='addTaskNoButton_click'))
async def redo_task(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('выберите критерий задания')
    await state.set_state(TaskState.service)


async def backToEnterButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите действие', reply_markup=mainKeyboard)
    await call.answer()


@router.callback_query(Text(text='addTaskButton_click'))
async def giveTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('')
    await call.answer()


'''@router.callback_query(Text(text='myTasksInfoButton_click'))
async def my_tasks_button_click(call: types.CallbackQuery):
    mas=TaskController.find_user_tasks(call.from_user.id)
    tasks=[]
    n=0
    for i in range(len(mas)):
        for y in range(i):
            tasks.append(mas[i][y])
        n=n+1
        await call.message.answer(f"Ваша задача номер {n}\nКритерии:{str(mas[i][12])}\nНазвание:{str(mas[i][1])}\nЦель:{str(mas[i][9])}\nДата:{str(mas[i][4])}\nАдрес:{str(mas[i][7])}\nЦена:{str(mas[i][5])}")'''


@router.callback_query(Text(text='getTaskButton_click'))
async def get_task_button_click(call: types.CallbackQuery):
    keyboard = getServicesKeyboard('task')
    if keyboard:
        await call.message.edit_text('Выберите критерий задания', reply_markup=keyboard)
    else:
        call.message.edit_text('Выберите задание')


def registerHandlersTask(dp: Dispatcher):
    dp.register_callback_query_handler(exitButtonClick, lambda call: call.data == 'exitButton_click', state='*')
    # TODO: Пересечение callback
    # dp.register_callback_query_handler(yesButtonClick, lambda call: call.data == 'yesButton_click', state='*')
    # dp.register_callback_query_handler(noButtonClick, lambda call: call.data == 'noButton_click', state='*')
    dp.register_callback_query_handler(backToEnterButtonClick, lambda call: call.data == 'backToEnterButton_click',
                                       state='*')
