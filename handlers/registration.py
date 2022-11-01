from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext

from keyboards.registration import yesNoKeyboard
from registrationState import RegistrationState
from userController import UserController


async def getNickname(message: types.Message):
    if UserController.HasUser(message.from_user.id):
        await message.answer('Вы уже зарегистрированы')
        return
    else:
        await message.answer('Введите nickname')
        await RegistrationState.nickname.set()


async def getPassword(message: types.Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    if UserController.IsNicknameFree(message.text):
        await message.answer('Такой nickname уже есть')
    else:
        await message.answer('Введите пароль')
        await RegistrationState.next()


async def getFullName(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    data = await state.get_data()
    if 'edit' in data.keys() and data['edit']:
        await RegistrationState.last()
        return
    await message.answer('Введите ваше Ф.И.О')
    await RegistrationState.next()


async def getPhoneNumber(message: types.Message, state: FSMContext):
    await state.update_data(fullName=message.text)
    await message.answer('Введите ваш номер телефона, для того чтобы с вами было легче связаться')
    await RegistrationState.next()


async def getEmail(message: types.Message, state: FSMContext):
    await state.update_data(phoneNumber=message.text)
    await message.answer('Введите вашу электронную почту')
    await RegistrationState.next()


async def getEdit(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)
    data = await state.get_data()
    await message.answer(
        f"login: {data['nickname']}\npassword: {data['password']}\nФ.И.О: {data['fullName']}\nТелефон: {data['phoneNumber']}\nemail: {data['email']}")
    await message.answer('Правильно ли вы ввели информацию?', reply_markup=yesNoKeyboard)
    await RegistrationState.next()


async def finish(message: types.Message, state: FSMContext):
    if message.text == 'Нет':
        # await message.answer('Что вы хотите изменить?', reply_markup=keyboardTestNo)
        # await state.update_data(edit=True)
        await state.finish()
        await RegistrationState.nickname.set()

    if message.text == 'Да':
        data = await state.get_data()
        UserController.AddNewUser(message.from_user.id, data['nickname'], data['password'], data['fullName'],
                                  data['phoneNumber'], data['email'])
        await state.finish()

async def yesButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Регистрация успешно завершена')
    await call.message.answer('Выберите род деятельности , которым вы хотите заниматься', reply_markup=criteriaKeyboard)
    await call.answer()


async def noButtonClick(call: types.CallbackQuery, state: FSMContext):
    # await call.message.edit_text('Что вы хотите изменить?', reply_markup=keyboardTestNo)
    # TODO: Проверить будет ли переход на начальное состояние
    await call.answer()
    await RegistrationState.nickname.set()

def registerHandlersRegistration(dp: Dispatcher):
    dp.register_message_handler(getNickname, commands=['Регистрация'], state="*")
    dp.register_message_handler(getPassword, state=RegistrationState.nickname)
    dp.register_message_handler(getFullName, state=RegistrationState.password)
    dp.register_message_handler(getPhoneNumber, state=RegistrationState.fullName)
    dp.register_message_handler(getEmail, state=RegistrationState.phoneNumber)
    dp.register_message_handler(getEdit, state=RegistrationState.email)
    dp.register_message_handler(finish, state=RegistrationState.edit)

    dp.register_callback_query_handler(yesButtonClick, lambda call: call.data == 'yesButton_click', state='*')
    dp.register_callback_query_handler(noButtonClick, lambda call: call.data == 'noButton_click', state='*')
