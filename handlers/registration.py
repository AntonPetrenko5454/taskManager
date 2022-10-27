from aiogram import types

from registrationState import RegistrationState


@dp.callback_query_handler(text='readyPasswordButton_click')
async def readyPasswordButtonClick(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(password=call.message.text)


@dp.callback_query_handler(text='readyFIOButton_click')
async def readyFIOButtonClick(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(fullName=call.message.text)


@dp.callback_query_handler(text='readyPhoneButton_click')
async def readyPhoneButtonClick(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(phoneNumber=call.message.text)


@dp.callback_query_handler(text='readyEmailButton_click')
async def readyEmailButtonClick(call: types.CallbackQuery, state: FSMContext):
    await state.update_data(email=call.message.text)


'''@dp.callback_query_handler(text='yes2Button_click')
async def yes2ButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Регистрация успешно завершена')
    await call.message.answer('Выберите род деятельности , которым вы хотите заниматься', reply_markup=criteriaKeyboard)

    await call.answer()'''


@dp.message_handler(state=RegistrationState.edit)
async def getEdit(message: types.Message, state: FSMContext):
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


'''@dp.callback_query_handler(text='no2Button_click')
async def no2ButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Что вы хотите изменить?', reply_markup=keyboardTestNo)
    await call.answer()
    await RegistrationState.last()'''


@dp.callback_query_handler(text='passwordChangeButton_click')
async def passwordButtonClick(call: types.CallbackQuery, state: FSMContext):
    # await call.message.edit_text('Введите ваш новый пароль ', reply_markup=passwordChangeKeyboard)
    # await call.answer()
    # await state.set_state(RegistrationState.password.state)
    await RegistrationState.password.set()


@dp.callback_query_handler(text='fIOChangeButton_click')
async def fIOButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Введите Ф.И.О', reply_markup=fIOChangeKeyboard)
    await call.answer()
    await RegistrationState.last()


@dp.callback_query_handler(text='phoneNumberChangeButton_click')
async def phoneButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Введите ваш новый телефон', reply_markup=phoneNumberChangeKeyboard)
    await call.answer()
    await RegistrationState.last()


@dp.callback_query_handler(text='emailChangeButton_click')
async def emailButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Введите ваш новый email', reply_markup=emailChangeKeyboard)
    await call.answer()
    await RegistrationState.last()


@dp.callback_query_handler(text='backButtonToTest_click')
async def backButtonToTestClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Что вы хотите изменить?', reply_markup=keyboardTestNo)
    await call.answer()


@dp.callback_query_handler(text='readyChangeButton_click')
async def readyButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer('Регистрация успешно завершена')
    await call.message.answer('Выберите род деятельности , которым вы хотите заниматься', reply_markup=criteriaKeyboard)
    data = await state.get_data()
    UserController.AddNewUser(call.message.from_user.id, data['nickname'], data['password'], data['fullName'],
                              data['phoneNumber'], data['email'])
    await state.finish()
    await call.answer()


# ??????????????????????????????????????????????????????????????????????????????????????????????????????????
@dp.callback_query_handler(text='teacherButton_click')
async def teacherButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите предмет учителя', reply_markup=teacherKeyboard)
    await call.answer()


@dp.callback_query_handler(text='backCriteriasButton_click')
async def backCriteriasButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите род деятельности , которым вы хотите заниматься',
                                 reply_markup=criteriaKeyboard)
    await call.answer()



@dp.message_handler(regexp='Регистрация')
async def registration(message: types.Message):
    if UserController.HasUser(message.from_user.id):
        await message.answer('Вы уже зарегистрированы')
        return
    else:
        await message.answer('Введите nickname')
        await RegistrationState.nickname.set()


@dp.message_handler(state=RegistrationState.nickname)
async def getNickname(message: types.Message, state: FSMContext):
    await state.update_data(nickname=message.text)
    if UserController.IsNicknameFree(message.text):
        await message.answer('Такой nickname уже есть')
    else:
        await message.answer('Введите пароль')
        await RegistrationState.next()


@dp.message_handler(state=RegistrationState.password)
async def getFullName(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)

    data = await state.get_data()
    if 'edit' in data.keys() and data['edit'] == True:
        await RegistrationState.last()
        return
    await message.answer('Введите ваше Ф.И.О')
    await RegistrationState.next()


@dp.message_handler(state=RegistrationState.fullName)
async def getphoneNumber(message: types.Message, state: FSMContext):
    await state.update_data(fullName=message.text)
    await message.answer('Введите ваш номер телефона, для того чтобы с вами было легче связаться')
    await RegistrationState.next()


@dp.message_handler(state=RegistrationState.phoneNumber)
async def getEmail(message: types.Message, state: FSMContext):
    await state.update_data(phoneNumber=message.text)
    await message.answer('Введите вашу электронную почту')
    await RegistrationState.next()


@dp.message_handler(state=RegistrationState.email)
async def getStatus(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)

    data = await state.get_data()
    await message.answer(
        f"login: {data['nickname']}\npassword: {data['password']}\nФ.И.О: {data['fullName']}\nТелефон: {data['phoneNumber']}\nemail: {data['email']}")

    await message.answer('Правильно ли вы ввели информацию?', reply_markup=yesNoInKeyboard)

    await RegistrationState.next()

