from aiogram import types, Dispatcher
from keyboards.main import mainKeyboard


async def exitButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Вы уверены, что хотите выйти?')
    await call.answer()


async def yesButtonClick(call: types.CallbackQuery):
    # TODO: Реализация авторизации для выхода и выхода
    await call.message.answer('Войдите в аккаунт или зарегестрируйтесь')


async def noButtonClick(call: types.CallbackQuery):
    await call.message.answer('Выберите действие', reply_markup=mainKeyboard)
    await call.answer()


async def backToEnterButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите действие', reply_markup=mainKeyboard)
    await call.answer()


def registerHandlersTask(dp: Dispatcher):
    dp.register_callback_query_handler(exitButtonClick, lambda call: call.data == 'exitButton_click', state='*')
    # TODO: Пересечение callback
    # dp.register_callback_query_handler(yesButtonClick, lambda call: call.data == 'yesButton_click', state='*')
    # dp.register_callback_query_handler(noButtonClick, lambda call: call.data == 'noButton_click', state='*')
    dp.register_callback_query_handler(backToEnterButtonClick, lambda call: call.data == 'backToEnterButton_click', state='*')

'''
@dp.callback_query_handler(text='giveTaskButton_click')
async def giveTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете дать задание конкретному пользователю или выставить задание на аукцион',
                                 reply_markup=addTaskKeyboard)
    await call.answer()


@dp.callback_query_handler(text='giveTaskButton21_click')
async def giveTaskButtonClick21(call: types.CallbackQuery):
    await call.message.edit_text('Введите ID или nickname пользователя, которому вы хотите дать задание',
                                 reply_markup=giveTaskKeyboard21)
    await call.answer()


@dp.callback_query_handler(text='giveTaskButton22_click')
async def giveTaskButtonClick22(call: types.CallbackQuery):
    await call.message.edit_text('Выберите критерии, по которым вы будете давать задачу',
                                 reply_markup=giveTaskKeyboard22)
    await call.answer()


@dp.callback_query_handler(text='backGiveButton_click')
async def backGiveButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете дать задание конкретному пользователю или выставить задание на аукцион',
                                 reply_markup=addTaskKeyboard)
    await call.answer()


@dp.callback_query_handler(text='getTaskButton_click')
async def getTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text(
        'Тут вы можете получить задание от конкретного пользователя или встать в очередь за заданием',
        reply_markup=getTaskKeyboard)
    await call.answer()


@dp.callback_query_handler(text='getTaskButton21_click')
async def getTaskButtonClick21(call: types.CallbackQuery):
    await call.message.edit_text('Запросы: \n', reply_markup=getTaskKeyboard21)
    await call.answer()


@dp.callback_query_handler(text='getTaskButton22_click')
async def getTaskButtonClick22(call: types.CallbackQuery):
    await call.message.edit_text('Выберите род деятельности задания', reply_markup=getTaskKeyboard22)
    await call.answer()


@dp.callback_query_handler(text='backGetButton_click')
async def backGetButtonClick(call: types.CallbackQuery):
    await call.message.edit_text(
        'Тут вы можете получить задание от конкретного пользователя или встать в очередь за заданием',
        reply_markup=getTaskKeyboard)
    await call.answer()
'''