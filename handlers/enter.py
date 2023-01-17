from aiogram import types, Dispatcher, Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from controllers.user_controller import UserController
from enter_state import EnterState
from keyboards.main import mainKeyboard
from keyboards.primary import primaryKeyboard

router = Router()


@router.message(Text(contains='Вход', ignore_case=True))
async def enterName(message: types.Message, state: FSMContext):
    await message.answer('Введите логин')
    await state.set_state(EnterState.nickname)


@router.message(EnterState.nickname)
async def enterPassword(message: types.Message, state: FSMContext):
    await message.answer('Введите пароль')
    await state.update_data(nickname=message.text)
    await state.set_state(EnterState.password)


@router.message(EnterState.password)
async def checkInfo(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()

    if not UserController.Authorization(message.from_user.id, data['nickname'], data['password']):
        await message.answer('Логин или пароль введены не верно', reply_markup=primaryKeyboard)
    else:
        await message.answer('Добро пожаловать',reply_markup=mainKeyboard)

    await state.clear()
