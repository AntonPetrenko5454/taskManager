from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from userController import UserController
from enterState import EnterState
from keyboards.main import mainKeyboard
from keyboards.primary import primaryKeyboard


async def enterName(message: types.Message):
    await message.answer('Введите логин')
    await EnterState.nickname.set()
    print(message.from_user.id)


async def enterPassword(message: types.Message, state: FSMContext):
    await message.answer('Введите пароль')
    await state.update_data(nickname=message.text)
    await EnterState.password.set()


async def checkInfo(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()

    if not UserController.Authorization(message.from_user.id, data['nickname'], data['password']):
        await message.answer('Логин или пароль введены не верно', reply_markup=primaryKeyboard)
    else:
        await message.answer('Добро пожаловать',reply_markup=mainKeyboard)

    await state.finish()


def registerHandlersEnter(dp: Dispatcher):
    dp.register_message_handler(enterName, regexp='Вход', state="*")
    dp.register_message_handler(enterPassword, state=EnterState.nickname)
    dp.register_message_handler(checkInfo, state=EnterState.password)
