from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from keyboards.registration import yesNoKeyboard
from keyboards.services import getServicesKeyboard
from registrationState import RegistrationState
from controllers.userController import UserController


async def startRegistration(message: types.Message):
    if UserController.HasUser(message.from_user.id):
        await message.answer('Вы уже зарегистрированы')
        return
    else:
        await message.answer('Введите nickname')
        await RegistrationState.nickname.set()


async def getNickname(message: types.Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    if UserController.IsNicknameFree(message.text):
        await message.answer('Такой nickname уже есть')
    else:
        await message.answer('Введите пароль')
        await RegistrationState.next()


async def getPassword(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    if 'edit' in data.keys() and data['edit']:
        await RegistrationState.last()
        return
    await message.answer('Введите ваше Ф.И.О')
    await RegistrationState.next()


async def getFullName(message: types.Message, state: FSMContext):
    await state.update_data(fullName=message.text)
    await message.answer('Введите ваш номер телефона, для того чтобы с вами было легче связаться')
    await RegistrationState.next()


async def getPhoneNumber(message: types.Message, state: FSMContext):
    await state.update_data(phoneNumber=message.text)
    await message.answer('Введите вашу электронную почту')
    await RegistrationState.next()


async def getEmail(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    await message.answer('Выберите род деятельности', reply_markup=getServicesKeyboard())
    await RegistrationState.next()


async def yesButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Регистрация успешно завершена')
    data = await state.get_data()
    UserController.AddNewUser(call.from_user.id, data['nickname'], data['password'], data['fullName'],
                              data['phoneNumber'], data['email'])
    await state.next
    await call.answer()


async def getService(message: types.Message, state: FSMContext):
    await state.update_data(service=message.text)
    data = await state.get_data()
    await message.answer(
        f"Login: {data['nickname']}\nPassword: {data['password']}\nФ.И.О: {data['fullName']}\nТелефон: {data['phoneNumber']}\nEmail: {data['email']}")
    await message.answer('Правильно ли вы ввели информацию?', reply_markup=yesNoKeyboard)
    await state.finish()


async def noButtonClick(call: types.CallbackQuery, state: FSMContext):
    # await call.message.edit_text('Что вы хотите изменить?', reply_markup=keyboardTestNo)
    # TODO: Проверить будет ли переход на начальное состояние
    await state.finish()
    await call.message.answer('Введите nickname')
    await RegistrationState.nickname.set()


async def serviceClick(call: types.CallbackQuery, state: FSMContext):
    serviceId = int(call.data.split('_')[1])
    await state.update_data(service=serviceId)
    keyboard = getServicesKeyboard(serviceId)
    if keyboard:
        await call.message.edit_text('Выберите род деятельности', reply_markup=keyboard)
    data = await state.get_data()
    print(data)


def registerHandlersRegistration(dp: Dispatcher):
    dp.register_message_handler(startRegistration, regexp='Регистрация', state="*")
    dp.register_message_handler(getNickname, state=RegistrationState.nickname)
    dp.register_message_handler(getPassword, state=RegistrationState.password)
    dp.register_message_handler(getFullName, state=RegistrationState.fullName)
    dp.register_message_handler(getPhoneNumber, state=RegistrationState.phoneNumber)
    dp.register_message_handler(getEmail, state=RegistrationState.email)
    dp.register_message_handler(getService, state=RegistrationState.service)

    dp.register_callback_query_handler(yesButtonClick, lambda call: call.data == 'yesButton_click', state='*')
    dp.register_callback_query_handler(noButtonClick, lambda call: call.data == 'noButton_click', state='*')
    dp.register_callback_query_handler(serviceClick, lambda call: call.data.startswith('service_'),
                                       state=RegistrationState.service)
