from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from enterState import EnterState


async def enterName(message: types.Message):
    await message.answer('Введите логин')
    await EnterState.nickname.set()


async def enterPassword(message: types.Message, state: FSMContext):
    await message.answer('Введите пароль')
    await state.update_data(nickname=message.text)
    await EnterState.password.set()


async def checkInfo(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    # TODO: Проверка корректности и перенаправление его на клавиатуру ________
    #       Если не корректный ввод, то перенаправление его на _______________
    await state.finish()


def registerHandlersEnter(dp: Dispatcher):
    dp.register_message_handler(enterName, commands=['Вход'], state="*")
    dp.register_message_handler(enterPassword, state=EnterState.nickname)
    dp.register_message_handler(checkInfo, state=EnterState.password)
