
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from enterState import EnterState
from aiogram.types import ContentType
from aiogram.utils import executor
from config import TOKEN
from userInfo import UserInfo
from registrationState import RegistrationState
keyboardEnter=types.InlineKeyboardMarkup(row_width=1)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())
##users=[]
currentUsers={}





backButton=types.InlineKeyboardButton(text='Назад',callback_data='backButton_click')
###Выход
keyboardYesNo=types.ReplyKeyboardMarkup()
yesNoButtons=['Да','Нет']
keyboardYesNo.add(yesNoButtons)
keyboardExit=types.ReplyKeyboardMarkup()
exitButton=['Выход']
keyboardExit.add(exitButton)
@dp.message_handler(commands='Выход')
async def exitButton(message: types.Message,state: FSMContext):
    await message.answer('Вы уверены , что хотите выйти ?',reply_markup=keyboardYesNo)

@dp.message_handler(commands='Да')
async def yesButton(message: types.Message,state: FSMContext):
    fUser = open('user.txt','a')
    for line in fUser:
        info = line.split()
        if info[0] == str(message.from_user.id):
            info[3]=='offline'
            fUser.close()
    await message.answer('',reply_markup=primaryKeyboard)
@dp.message_handler(commands='Нет')
async def noButton(message: types.Message,state: FSMContext):
    await message.answer('Добро пожаловать',reply_markup=keyboardEnter)






### род деятельности


criteriaKeyboard=types.InlineKeyboardMarkup(row_width=2)
teacherKeyboard=types.InlineKeyboardMarkup(row_width=1)
criteriasButtons=[]
teacherButtons=[]
backCriteriasButton=types.InlineKeyboardButton(text='Назад',callback_data='backCriteriasButton_click')
programmingButton=types.InlineKeyboardButton(text='Программирование',callback_data='programmingButton_click')
handymanButton=types.InlineKeyboardButton(text='Разнорабочий',callback_data='handymanButton_click')
teacherButton=types.InlineKeyboardButton(text='Учитель',callback_data='teacherButton_click')

@dp.callback_query_handler(text='teacherButton_click')
async def teacherButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите предмет учителя', reply_markup=teacherKeyboard)
    await call.answer()

@dp.callback_query_handler(text='backCriteriasButton_click')
async def backCriteriasButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Выберите род деятельности , которым вы хотите заниматься', reply_markup=criteriaKeyboard)
    await call.answer()
teacherMathsButton=types.InlineKeyboardButton(text='Математика',callback_data='teacherMathsButton_click')
teacherRussianLanguageButton=types.InlineKeyboardButton(text='Русский язык',callback_data='teacherRussianLanguageButton_click')
###teacherButtons.add(teacherMathsButton,teacherRussianLanguageButton)
teacherKeyboard.add(teacherMathsButton,teacherRussianLanguageButton,backCriteriasButton)
###criteriasButtons.append(programmingButton,handymanButton,teacherButton)
criteriaKeyboard.add(programmingButton,handymanButton,teacherButton)







### дать задание
giveTaskKeyboard=types.InlineKeyboardMarkup(row_width=1)
giveTaskButton=types.InlineKeyboardButton(text='Дать задание',callback_data='giveTaskButton_click')
giveTaskButton21=types.InlineKeyboardButton(text='Дать задание пользователю',callback_data='giveTaskButton21_click')
giveTaskButton22=types.InlineKeyboardButton(text='Выставить задание на аукцион',callback_data='giveTaskButton22_click')
giveTaskKeyboard.add(giveTaskButton21,giveTaskButton22,backButton)
giveTaskKeyboard21=types.InlineKeyboardMarkup(row_width=1)
giveTaskKeyboard22=types.InlineKeyboardMarkup(row_width=1)
backGiveButton=types.InlineKeyboardButton(text='Назад',callback_data='backGiveButton_click')
giveTaskKeyboard21.add(backGiveButton)
giveTaskKeyboard22.add(backGiveButton)

@dp.callback_query_handler(text='giveTaskButton_click')
async def giveTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете дать задание конкретному пользователю или выставить задание на аукцион',reply_markup=giveTaskKeyboard)
    await call.answer()

@dp.callback_query_handler(text='giveTaskButton21_click')
async def giveTaskButtonClick21(call: types.CallbackQuery):
    await call.message.edit_text('Введите ID или nickname пользователя , которому вы хотите дать задание',reply_markup=giveTaskKeyboard21)
    await call.answer()

@dp.callback_query_handler(text='giveTaskButton22_click')
async def giveTaskButtonClick22(call: types.CallbackQuery):
    await call.message.edit_text('Выберите критерии , по которым вы будете давать задачу',reply_markup=giveTaskKeyboard22)
    await call.answer()

@dp.callback_query_handler(text='backGiveButton_click')
async def backGiveButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете дать задание конкретному пользователю или выставить задание на аукцион',reply_markup=giveTaskKeyboard)
    await call.answer()


### получить задание
getTaskKeyboard=types.InlineKeyboardMarkup(row_width=1)
getTaskButton=types.InlineKeyboardButton(text='Получить задание',callback_data='getTaskButton_click')
getTaskKeyboard21=types.InlineKeyboardMarkup(row_width=1)
getTaskKeyboard22=types.InlineKeyboardMarkup(row_width=1)
backGetButton=types.InlineKeyboardButton(text='Назад',callback_data='backGetButton_click')
getTaskButton21=types.InlineKeyboardButton(text='Посмотреть запросы',callback_data='getTaskButton21_click')
getTaskButton22=types.InlineKeyboardButton(text='Встать в очередь',callback_data='getTaskButton22_click')
getTaskKeyboard.add(getTaskButton21,getTaskButton22,backButton)
getTaskKeyboard21.add(backGetButton)
getTaskKeyboard22.add(backGetButton)

@dp.callback_query_handler(text='getTaskButton_click')
async def getTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете получить задание от конкретного пользователя или встать в очередь за заданием',reply_markup=getTaskKeyboard)
    await call.answer()

@dp.callback_query_handler(text='getTaskButton21_click')
async def getTaskButtonClick21(call: types.CallbackQuery):
    await call.message.edit_text('запросы: \n',reply_markup=getTaskKeyboard21)
    await call.answer()

@dp.callback_query_handler(text='getTaskButton22_click')
async def getTaskButtonClick22(call: types.CallbackQuery):
    await call.message.edit_text('Выберите род деятельности задания',reply_markup=getTaskKeyboard22)
    await call.answer()

@dp.callback_query_handler(text='backGetButton_click')
async def backGetButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете получить задание от конкретного пользователя или встать в очередь за заданием',reply_markup=getTaskKeyboard)
    await call.answer()

### личная информация
userInfoKeyboard=types.InlineKeyboardMarkup(row_width=1)
allUserInfoButton=types.InlineKeyboardButton(text='Информация о пользователе',callback_data='allUserInfoButton_click')
historyTaskKeyboard=types.InlineKeyboardMarkup(row_width=1)
allUserInfoKeyboard=types.InlineKeyboardMarkup(row_width=1)
backUserInfoButton=types.InlineKeyboardButton(text='Назад',callback_data='backUserInfoButton_click')
historyTaskButton=types.InlineKeyboardButton(text='История задач',callback_data='historyTaskButton_click')
changeUserInfoButton=types.InlineKeyboardButton(text='Ваши данные',callback_data='userInfoButton_click')
userInfoKeyboard.add(historyTaskButton,changeUserInfoButton,backButton)
historyTaskKeyboard.add(backUserInfoButton)
allUserInfoKeyboard.add(backUserInfoButton)

@dp.callback_query_handler(text='allUserInfoButton_click')
async def allUserInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию', reply_markup=userInfoKeyboard)
    await call.answer()

@dp.callback_query_handler(text='historyTaskButton_click')
async def historyTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Ваша история задач:',reply_markup=historyTaskKeyboard)
    await call.answer()

@dp.callback_query_handler(text='userInfoButton_click')
async def userInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Ф.И.O: \n Возраст: \n Страна: \n Отзывы: \n',reply_markup=allUserInfoKeyboard)
    await call.answer()

@dp.callback_query_handler(text='backUserInfoButton_click')
async def backUserInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию',reply_markup=userInfoKeyboard)
    await call.answer()

### поиск пользователя
searchUserKeyboard=types.InlineKeyboardMarkup(row_width=1)
searchUserKeyboard21=types.InlineKeyboardMarkup(row_width=1)
backSearchUserButton=types.InlineKeyboardButton(text='Назад',callback_data='backSearchUserButton_click')
searchUserButton=types.InlineKeyboardButton(text='Поиск пользователя',callback_data='searchUserButton_click')
searchUserKeyboard.add(backButton)
searchUserKeyboard21.add(backSearchUserButton)

@dp.callback_query_handler(text='searchUserButton_click')
async def searchUserButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Введите nickname или ID пользователя', reply_markup=searchUserKeyboard)
    await call.answer()

@dp.callback_query_handler(text='backSearchUserButton_click')
async def backSearchUserButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Введите nickname или ID пользователя',reply_markup=searchUserKeyboard21)
    await call.answer()


### информация о боте
botInfoKeyboard=types.InlineKeyboardMarkup(row_width=1)
botInfoKeyboard21=types.InlineKeyboardMarkup(row_width=1)
botInfoWishKeyboard=types.InlineKeyboardMarkup(row_width=1)
botInfoReviewKeyboard=types.InlineKeyboardMarkup(row_width=1)
botInfoReviewWriteKeyboard=types.InlineKeyboardMarkup(row_width=1)
backBotInfoButton=types.InlineKeyboardButton(text='Назад',callback_data='backBotInfoButton_click')
botInfoButton=types.InlineKeyboardButton(text='Информация о боте',callback_data='botInfoButton_click')
writeWishBotButton=types.InlineKeyboardButton(text='Оставить пожелание',callback_data='writeWishBotButton_click')
writeReviewBotButton=types.InlineKeyboardButton(text='Оставить отзыв',callback_data='writeReviewBotButton_click')
seeReviewBotButton=types.InlineKeyboardButton(text='Посмотреть отзывы',callback_data='seeReviewBotButton_click')
botInfoKeyboard.add(writeWishBotButton,seeReviewBotButton,backButton)
botInfoReviewWriteKeyboard.add(writeReviewBotButton,backBotInfoButton)
botInfoWishKeyboard.add(backBotInfoButton)

@dp.callback_query_handler(text='botInfoButton_click')
async def botInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете прочитать информацию о боте или оставить пожелание/отзыв',reply_markup=botInfoKeyboard)
    await call.answer()

@dp.callback_query_handler(text='writeWishBotButton_click')
async def botWriteWishButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете написать пожелания , которые вы хотели бы видеть в нашем боте',reply_markup=botInfoWishKeyboard)
    await call.answer()

@dp.callback_query_handler(text='seeReviewBotButton_click')
async def botSeeReviewButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Отзывы: \n',reply_markup=botInfoReviewWriteKeyboard)
    await call.answer()

@dp.callback_query_handler(text='writeReviewBotButton_click')
async def botWriteReviewButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете оставить отзыв об функциональности бота ',reply_markup=botInfoReviewWriteKeyboard)
    await call.answer()

@dp.callback_query_handler(text='backBotInfoButton_click')
async def backBotInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете прочитать информацию о боте или оставить пожелание/отзыв',reply_markup=botInfoKeyboard)
    await call.answer()






keyboardEnter.add(getTaskButton,giveTaskButton,allUserInfoButton,searchUserButton,botInfoButton)








primaryKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)

primaryKeyboard.add('Регистрация','Вход')

keyboardReg = types.ReplyKeyboardMarkup()
usersCount=len(open('user.txt').readlines())

'''fUser=open('user.txt')
for line in fUser:
    info=line.split()
    user=User(info[0],info[1],info[2])
    users.append(user)
fUser.close()'''


@dp.message_handler(regexp='Регистрация')
async def registration(message: types.Message):
    x=0
    fUser = open('user.txt', 'r')
    for line in fUser:
        info = line.split()
        if info[0] == str(message.from_user.id):
            await message.answer('Регистрация невозможна , такой ID уже есть')
            fUser.close()
            break
        else:
            x=x+1
    if x==usersCount:
        await message.answer('Введите nickname')
        await RegistrationState.nickname.set()



@dp.message_handler(state=RegistrationState.nickname)
async def getNickname(message: types.Message,state: FSMContext):
    await state.update_data(nickname=message.text)
    fUser = open('user.txt', 'r')
    for line in fUser:
        info = line.split()
        if info[1] == message.text:
            await message.answer('Такой nickname уже есть')
            return
    fUser.close()
    await message.answer('Введите пароль')

    await RegistrationState.next()


@dp.message_handler(state=RegistrationState.password)
async def getPassword(message: types.Message,state: FSMContext):
    await state.update_data(password=message.text)
    await state.update_data(status='offline')

    data = await state.get_data()
    await message.answer(f"login: {data['nickname']}")
    await message.answer('Регистрация успешно завершена')
    global usersCount
    usersCount +=1
    fUser=open('user.txt','a')
    fUser.write(f"{message.from_user.id} {data['nickname']} {data['password']} {data['status']}\n")
    await message.answer('Выберите род деятельности , которым вы хотите заниматься',reply_markup=criteriaKeyboard)
    fUser.close()
    await state.finish()
@dp.message_handler(regexp='вход')
async def enterName(message: types.Message):
    await message.answer('Введите логин')
    await EnterState.nickname.set()

@dp.message_handler(state=EnterState.nickname)
async def enterPassword(message: types.Message,state: FSMContext):
    await message.answer('Введите пароль')
    await state.update_data(nickname=message.text)
    await EnterState.password.set()

@dp.message_handler(state=EnterState.password)
async def checkInfo(message: types.Message,state: FSMContext):
    await state.update_data(password=message.text)
    await state.update_data(status='online')
    data = await state.get_data()
    x=0
    fUser = open('user.txt','r')
    for line in fUser:
        info=line.split()
        if info[1] == data['nickname'] and info[2] == data['password']:
            fUser.close()
            await message.answer('Добро пожаловать',reply_markup=keyboardEnter)
            fUser = open('user.txt','w')
            fUser.write(f"{message.from_user.id} {data['nickname']} {data['password']} {data['status']}\n")
            fUser.close()
            break
        else:
            x=x+1
    if x==usersCount:
        await message.answer('Логин или пароль введены неверно')
    await state.finish()

@dp.callback_query_handler(text='backButton_click')
async def backButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Добро пожаловать',reply_markup=keyboardEnter)
    await call.answer()

if __name__ == '__main__':
    executor.start_polling(dp)