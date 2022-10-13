from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from enterState import EnterState
from aiogram.types import ContentType
from aiogram.utils import executor
from config import TOKEN
from userController import UserController
from userInfo import UserInfo
from registrationState import RegistrationState

keyboardEnter = types.InlineKeyboardMarkup(row_width=1)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())
currentUsers = {}
backButton = types.InlineKeyboardButton(text='Назад', callback_data='backButton_click')

###Проверка информации при регистрации
keyboardTest = types.InlineKeyboardMarkup(row_width=2)
yes2Button = types.InlineKeyboardButton(text='Да', callback_data='yes2Button_click')
no2Button = types.InlineKeyboardButton(text='Нет', callback_data='no2Button_click')
keyboardTest.add(yes2Button, no2Button)
keyboardTestNo = types.InlineKeyboardMarkup(row_width=1)
readyChangeButton = types.InlineKeyboardButton(text='Готово', callback_data='readyChangeButton_click')
passwordChangeButton = types.InlineKeyboardButton(text='Изменить пароль', callback_data='passwordChangeButton_click')
fIOChangeButton = types.InlineKeyboardButton(text='Изменить Ф.И.О', callback_data='fIOchangeButton_click')
telephonNumberChangeButton = types.InlineKeyboardButton(text='Изменить номер телефона', callback_data='telephonNumberChangeButton_click')
emailChangeButton = types.InlineKeyboardButton(text='Изменить email', callback_data='emailChangeButton_click')
keyboardTestNo.add(passwordChangeButton, fIOChangeButton, telephonNumberChangeButton, emailChangeButton,readyChangeButton)
backButtonToTest = types.InlineKeyboardButton(text='Назад', callback_data='backButtonToTest_click')
passwordChangeKeyboard = types.InlineKeyboardMarkup(row_width=1)
fIOChangeKeyboard = types.InlineKeyboardMarkup(row_width=1)
telephonNumberChangeKeyboard = types.InlineKeyboardMarkup(row_width=1)
emailChangeKeyboard = types.ReplyKeyboardMarkup(row_width=1)
readyPasswordButton = types.InlineKeyboardButton(text='Готово', callback_data='readyPasswordButton_click')
readyFIOButton = types.InlineKeyboardButton(text='Готово', callback_data='readyFIOButton_click')
readyPhoneButton = types.InlineKeyboardButton(text='Готово', callback_data='readyPhoneButton_click')
readyEmailButton = types.InlineKeyboardButton(text='Готово', callback_data='readyEmailButton_click')
passwordChangeKeyboard.add(readyPasswordButton, backButtonToTest)
fIOChangeKeyboard.add(readyFIOButton, backButtonToTest)
telephonNumberChangeKeyboard.add(readyPhoneButton, backButtonToTest)
emailChangeKeyboard.add(readyEmailButton, backButtonToTest)


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
        #await message.answer('Что вы хотите изменить?', reply_markup=keyboardTestNo)
        #await state.update_data(edit=True)
        await state.finish()
        await RegistrationState.nickname.set()

    if message.text == 'Да':
        data = await state.get_data()
        UserController.AddNewUser(message.from_user.id, data['nickname'], data['password'], data['fullName'],
                                  data['telephonNumber'], data['email'])
        await state.finish()



'''@dp.callback_query_handler(text='no2Button_click')
async def no2ButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Что вы хотите изменить?', reply_markup=keyboardTestNo)
    await call.answer()
    await RegistrationState.last()'''

@dp.callback_query_handler(text='passwordChangeButton_click')
async def passwordButtonClick(call: types.CallbackQuery, state: FSMContext):
    #await call.message.edit_text('Введите ваш новый пароль ', reply_markup=passwordChangeKeyboard)
    #await call.answer()
    #await state.set_state(RegistrationState.password.state)
    await RegistrationState.password.set()


@dp.callback_query_handler(text='fIOChangeButton_click')
async def fIOButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Введите Ф.И.О', reply_markup=fIOChangeKeyboard)
    await call.answer()
    await RegistrationState.last()

@dp.callback_query_handler(text='telephonNumberChangeButton_click')
async def telephonButtonClick(call: types.CallbackQuery, state: FSMContext):
    await call.message.edit_text('Введите ваш новый телефон', reply_markup=telephonNumberChangeKeyboard)
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
                              data['telephonNumber'], data['email'])
    await state.finish()
    await call.answer()


###Выход
keyboardYesNo = types.InlineKeyboardMarkup(row_width=2)
yesButton = types.InlineKeyboardButton(text='Да', callback_data='yesButton_click')
noButton = types.InlineKeyboardButton(text='Нет', callback_data='noButton_click')
keyboardYesNo.add(yesButton, noButton)
exitButton = types.InlineKeyboardButton(text='Выход', callback_data='exitButton_click')


@dp.callback_query_handler(text='exitButton_click')
async def exitButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Вы уверены , что хотите выйти ?', reply_markup=keyboardYesNo)
    await call.answer()


@dp.callback_query_handler(text='yesButton_click')
async def yesButtonClick(call: types.CallbackQuery):
    await call.message.answer('Вы успешно вышли')


@dp.callback_query_handler(text='noButton_click')
async def noButtonClick(call: types.CallbackQuery):
    await call.message.answer('Добро пожаловать', reply_markup=keyboardEnter)
    await call.answer()


### род деятельности


criteriaKeyboard = types.InlineKeyboardMarkup(row_width=2)
teacherKeyboard = types.InlineKeyboardMarkup(row_width=1)
criteriasButtons = []
teacherButtons = []
backCriteriasButton = types.InlineKeyboardButton(text='Назад', callback_data='backCriteriasButton_click')
programmingButton = types.InlineKeyboardButton(text='Программирование', callback_data='programmingButton_click')
handymanButton = types.InlineKeyboardButton(text='Разнорабочий', callback_data='handymanButton_click')
teacherButton = types.InlineKeyboardButton(text='Учитель', callback_data='teacherButton_click')


@dp.callback_query_handler(text='teacherButton_click')
async def teacherButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите предмет учителя', reply_markup=teacherKeyboard)
    await call.answer()


@dp.callback_query_handler(text='backCriteriasButton_click')
async def backCriteriasButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите род деятельности , которым вы хотите заниматься',
                                 reply_markup=criteriaKeyboard)
    await call.answer()


teacherMathsButton = types.InlineKeyboardButton(text='Математика', callback_data='teacherMathsButton_click')
teacherRussianLanguageButton = types.InlineKeyboardButton(text='Русский язык',
                                                          callback_data='teacherRussianLanguageButton_click')
###teacherButtons.add(teacherMathsButton,teacherRussianLanguageButton)
teacherKeyboard.add(teacherMathsButton, teacherRussianLanguageButton, backCriteriasButton)
###criteriasButtons.append(programmingButton,handymanButton,teacherButton)
criteriaKeyboard.add(programmingButton, handymanButton, teacherButton)

### дать задание
giveTaskKeyboard = types.InlineKeyboardMarkup(row_width=1)
giveTaskButton = types.InlineKeyboardButton(text='Дать задание', callback_data='giveTaskButton_click')
giveTaskButton21 = types.InlineKeyboardButton(text='Дать задание пользователю', callback_data='giveTaskButton21_click')
giveTaskButton22 = types.InlineKeyboardButton(text='Выставить задание на аукцион',
                                              callback_data='giveTaskButton22_click')
giveTaskKeyboard.add(giveTaskButton21, giveTaskButton22, backButton)
giveTaskKeyboard21 = types.InlineKeyboardMarkup(row_width=1)
giveTaskKeyboard22 = types.InlineKeyboardMarkup(row_width=1)
backGiveButton = types.InlineKeyboardButton(text='Назад', callback_data='backGiveButton_click')
giveTaskKeyboard21.add(backGiveButton)
giveTaskKeyboard22.add(backGiveButton)


@dp.callback_query_handler(text='giveTaskButton_click')
async def giveTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете дать задание конкретному пользователю или выставить задание на аукцион',
                                 reply_markup=giveTaskKeyboard)
    await call.answer()


@dp.callback_query_handler(text='giveTaskButton21_click')
async def giveTaskButtonClick21(call: types.CallbackQuery):
    await call.message.edit_text('Введите ID или nickname пользователя , которому вы хотите дать задание',
                                 reply_markup=giveTaskKeyboard21)
    await call.answer()


@dp.callback_query_handler(text='giveTaskButton22_click')
async def giveTaskButtonClick22(call: types.CallbackQuery):
    await call.message.edit_text('Выберите критерии , по которым вы будете давать задачу',
                                 reply_markup=giveTaskKeyboard22)
    await call.answer()


@dp.callback_query_handler(text='backGiveButton_click')
async def backGiveButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете дать задание конкретному пользователю или выставить задание на аукцион',
                                 reply_markup=giveTaskKeyboard)
    await call.answer()


### получить задание
getTaskKeyboard = types.InlineKeyboardMarkup(row_width=1)
getTaskButton = types.InlineKeyboardButton(text='Получить задание', callback_data='getTaskButton_click')
getTaskKeyboard21 = types.InlineKeyboardMarkup(row_width=1)
getTaskKeyboard22 = types.InlineKeyboardMarkup(row_width=1)
backGetButton = types.InlineKeyboardButton(text='Назад', callback_data='backGetButton_click')
getTaskButton21 = types.InlineKeyboardButton(text='Посмотреть запросы', callback_data='getTaskButton21_click')
getTaskButton22 = types.InlineKeyboardButton(text='Встать в очередь', callback_data='getTaskButton22_click')
getTaskKeyboard.add(getTaskButton21, getTaskButton22, backButton)
getTaskKeyboard21.add(backGetButton)
getTaskKeyboard22.add(backGetButton)


@dp.callback_query_handler(text='getTaskButton_click')
async def getTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text(
        'Тут вы можете получить задание от конкретного пользователя или встать в очередь за заданием',
        reply_markup=getTaskKeyboard)
    await call.answer()


@dp.callback_query_handler(text='getTaskButton21_click')
async def getTaskButtonClick21(call: types.CallbackQuery):
    await call.message.edit_text('запросы: \n', reply_markup=getTaskKeyboard21)
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


### личная информация
userInfoKeyboard = types.InlineKeyboardMarkup(row_width=1)
allUserInfoButton = types.InlineKeyboardButton(text='Информация о пользователе',
                                               callback_data='allUserInfoButton_click')
historyTaskKeyboard = types.InlineKeyboardMarkup(row_width=1)
allUserInfoKeyboard = types.InlineKeyboardMarkup(row_width=1)
backUserInfoButton = types.InlineKeyboardButton(text='Назад', callback_data='backUserInfoButton_click')
historyTaskButton = types.InlineKeyboardButton(text='История задач', callback_data='historyTaskButton_click')
changeUserInfoButton = types.InlineKeyboardButton(text='Ваши данные', callback_data='userInfoButton_click')
userInfoKeyboard.add(historyTaskButton, changeUserInfoButton, backButton)
historyTaskKeyboard.add(backUserInfoButton)
allUserInfoKeyboard.add(backUserInfoButton)


@dp.callback_query_handler(text='allUserInfoButton_click')
async def allUserInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию', reply_markup=userInfoKeyboard)
    await call.answer()


@dp.callback_query_handler(text='historyTaskButton_click')
async def historyTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Ваша история задач:', reply_markup=historyTaskKeyboard)
    await call.answer()


@dp.callback_query_handler(text='userInfoButton_click')
async def userInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Ф.И.O: \n Возраст: \n Страна: \n Отзывы: \n', reply_markup=allUserInfoKeyboard)
    await call.answer()


@dp.callback_query_handler(text='backUserInfoButton_click')
async def backUserInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию', reply_markup=userInfoKeyboard)
    await call.answer()


### поиск пользователя
searchUserKeyboard = types.InlineKeyboardMarkup(row_width=1)
searchUserKeyboard21 = types.InlineKeyboardMarkup(row_width=1)
backSearchUserButton = types.InlineKeyboardButton(text='Назад', callback_data='backSearchUserButton_click')
searchUserButton = types.InlineKeyboardButton(text='Поиск пользователя', callback_data='searchUserButton_click')
searchUserKeyboard.add(backButton)
searchUserKeyboard21.add(backSearchUserButton)


@dp.callback_query_handler(text='searchUserButton_click')
async def searchUserButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Введите nickname или ID пользователя', reply_markup=searchUserKeyboard)
    await call.answer()


@dp.callback_query_handler(text='backSearchUserButton_click')
async def backSearchUserButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Введите nickname или ID пользователя', reply_markup=searchUserKeyboard21)
    await call.answer()


### информация о боте
botInfoKeyboard = types.InlineKeyboardMarkup(row_width=1)
botInfoKeyboard21 = types.InlineKeyboardMarkup(row_width=1)
botInfoWishKeyboard = types.InlineKeyboardMarkup(row_width=1)
botInfoReviewKeyboard = types.InlineKeyboardMarkup(row_width=1)
botInfoReviewWriteKeyboard = types.InlineKeyboardMarkup(row_width=1)
backBotInfoButton = types.InlineKeyboardButton(text='Назад', callback_data='backBotInfoButton_click')
botInfoButton = types.InlineKeyboardButton(text='Информация о боте', callback_data='botInfoButton_click')
writeWishBotButton = types.InlineKeyboardButton(text='Оставить пожелание', callback_data='writeWishBotButton_click')
writeReviewBotButton = types.InlineKeyboardButton(text='Оставить отзыв', callback_data='writeReviewBotButton_click')
seeReviewBotButton = types.InlineKeyboardButton(text='Посмотреть отзывы', callback_data='seeReviewBotButton_click')
botInfoKeyboard.add(writeWishBotButton, seeReviewBotButton, backButton)
botInfoReviewWriteKeyboard.add(writeReviewBotButton, backBotInfoButton)
botInfoWishKeyboard.add(backBotInfoButton)


@dp.callback_query_handler(text='botInfoButton_click')
async def botInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете прочитать информацию о боте или оставить пожелание/отзыв',
                                 reply_markup=botInfoKeyboard)
    await call.answer()


@dp.callback_query_handler(text='writeWishBotButton_click')
async def botWriteWishButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете написать пожелания , которые вы хотели бы видеть в нашем боте',
                                 reply_markup=botInfoWishKeyboard)
    await call.answer()


@dp.callback_query_handler(text='seeReviewBotButton_click')
async def botSeeReviewButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Отзывы: \n', reply_markup=botInfoReviewWriteKeyboard)
    await call.answer()


@dp.callback_query_handler(text='writeReviewBotButton_click')
async def botWriteReviewButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете оставить отзыв об функциональности бота ',
                                 reply_markup=botInfoReviewWriteKeyboard)
    await call.answer()


@dp.callback_query_handler(text='backBotInfoButton_click')
async def backBotInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете прочитать информацию о боте или оставить пожелание/отзыв',
                                 reply_markup=botInfoKeyboard)
    await call.answer()


keyboardEnter.add(getTaskButton, giveTaskButton, allUserInfoButton, searchUserButton, botInfoButton, exitButton)

primaryKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
primaryKeyboard.add('Регистрация', 'Вход')
keyboardReg = types.ReplyKeyboardMarkup()
yesNoInKeyboard=types.ReplyKeyboardMarkup(resize_keyboard=True)
yesNoInKeyboard.add('Да','Нет')


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
async def getTelephonNumber(message: types.Message, state: FSMContext):
    await state.update_data(fullName=message.text)
    await message.answer('Введите ваш номер телефона, для того чтобы с вами было легче связаться')
    await RegistrationState.next()


@dp.message_handler(state=RegistrationState.telephonNumber)
async def getEmail(message: types.Message, state: FSMContext):
    await state.update_data(telephonNumber=message.text)
    await message.answer('Введите вашу электронную почту')
    await RegistrationState.next()


@dp.message_handler(state=RegistrationState.email)
async def getStatus(message: types.Message, state: FSMContext):
    await state.update_data(email=message.text)

    data = await state.get_data()
    await message.answer(
        f"login: {data['nickname']}\npassword: {data['password']}\nФ.И.О: {data['fullName']}\nТелефон: {data['telephonNumber']}\nemail: {data['email']}")

    await message.answer('Правильно ли вы ввели информацию?', reply_markup=yesNoInKeyboard)

    await RegistrationState.next()



@dp.message_handler(regexp='вход')
async def enterName(message: types.Message):
    await message.answer('Введите логин')
    await EnterState.nickname.set()


@dp.message_handler(state=EnterState.nickname)
async def enterPassword(message: types.Message, state: FSMContext):
    await message.answer('Введите пароль')
    await state.update_data(nickname=message.text)
    await EnterState.password.set()


@dp.message_handler(state=EnterState.password)
async def checkInfo(message: types.Message, state: FSMContext):
    await state.update_data(password=message.text)
    await state.update_data(status='online')
    data = await state.get_data()

    await state.finish()


@dp.message_handler(commands=['start', 'начать'])
async def startCommands(message: types.Message):
    await message.answer('Hello', reply_markup=primaryKeyboard)


'''async def on_startup(_):
    await bot.send_message(bot.get_me().id,text='sfsfsdf',reply_markup=primaryKeyboard)'''


@dp.callback_query_handler(text='backButton_click')
async def backButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Добро пожаловать', reply_markup=keyboardEnter)
    await call.answer()


if __name__ == '__main__':
    executor.start_polling(dp)
