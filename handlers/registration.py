from aiogram import types, Router
from aiogram.filters import Text
from aiogram.fsm.context import FSMContext
from keyboards.registration import yesNoKeyboard
from keyboards.services import getServicesKeyboard
from registration_state import RegistrationState
from controllers.user_controller import UserController
from aiogram import F

router = Router()


@router.message(F.text.regexp('Регистрация'))
async def startRegistration(message: types.Message, state: FSMContext):
    if UserController.HasUser(message.from_user.id):
        await message.answer('Вы уже зарегистрированы')
        return
    else:
        await message.answer('Введите nickname')
        await state.set_state(RegistrationState.nickname)


@router.message(RegistrationState.nickname)
async def getNickname(message: types.Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    if UserController.IsNicknameFree(message.text):
        await message.answer('Такой nickname уже есть')
    else:
        await message.answer('Введите пароль')
        await state.set_state(RegistrationState.password)


@router.message(RegistrationState.password)
async def getPassword(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    if 'edit' in data.keys() and data['edit']:
        await RegistrationState.last()
        return
    await message.answer('Введите ваше Ф.И.О')
    await state.set_state(RegistrationState.fullName)


@router.message(RegistrationState.fullName)
async def getFullName(message: types.Message, state: FSMContext):
    await state.update_data(fullName=message.text)
    await message.answer('Введите ваш номер телефона, для того чтобы с вами было легче связаться')
    await state.set_state(RegistrationState.phoneNumber)


@router.message(RegistrationState.phoneNumber)
async def getPhoneNumber(message: types.Message, state: FSMContext):
    await state.update_data(phoneNumber=message.text)
    await message.answer('Введите вашу электронную почту')
    await state.set_state(RegistrationState.email)


@router.message(RegistrationState.email)
async def getEmail(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Выберите род деятельности', reply_markup=getServicesKeyboard('registration'))
    await state.set_state(RegistrationState.service)


@router.callback_query(Text(text='yesButton_click'))
async def yesButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Регистрация успешно завершена')
    data = await state.get_data()
    UserController.AddNewUser(call.from_user.id, data['nickname'], data['password'], data['fullName'],
                              data['phoneNumber'], data['email'])
    await state.clear()


@router.callback_query(Text(text='noButton_click'))
async def noButtonClick(call: types.CallbackQuery, state: FSMContext):
    await state.clear()
    await call.message.answer('Введите nickname')
    await state.set_state(RegistrationState.nickname)

@router.callback_query(Text(startswith='registration_service_'), RegistrationState.service)
async def serviceClick(call: types.CallbackQuery, state: FSMContext):
    serviceId = int(call.data.split('_')[2])
    await state.update_data(service=serviceId)
    keyboard = getServicesKeyboard('registration', serviceId)
    if keyboard:
        await call.message.edit_text('Выберите род деятельности', reply_markup=keyboard)
    else:
        data = await state.get_data()
        await call.message.answer(
            f"Login: {data['nickname']}\nPassword: {data['password']}\nФ.И.О: {data['fullName']}\nТелефон: {data['phoneNumber']}\nEmail: {data['email']}\nСервис: {data['service']}")
        await call.message.answer('Правильно ли вы ввели информацию?', reply_markup=yesNoKeyboard)
    await state.set_state(RegistrationState.service)
    await call.answer()
