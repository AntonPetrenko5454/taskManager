
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from enterState import EnterState
from aiogram.types import ContentType
from aiogram.utils import executor
from config import TOKEN
from user import User
from registrationState import RegistrationState
keyboardEnter=types.InlineKeyboardMarkup(row_width=1)
bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())
##users=[]
currentUsers={}
getTaskButton=types.InlineKeyboardButton(text='Получить задание',callback_data='getTaskButton_click')
giveTaskButton=types.InlineKeyboardButton(text='Дать задание',callback_data='giveTaskButton_click')
allUserInfoButton=types.InlineKeyboardButton(text='Информация о пользователе',callback_data='allUserInfoButton_click')
searchUserButton=types.InlineKeyboardButton(text='Поиск пользователя',callback_data='searchUserButton_click')
botInfoButton=types.InlineKeyboardButton(text='Информация о боте',callback_data='botInfoButton_click')
keyboardEnter.add(getTaskButton,giveTaskButton,allUserInfoButton,searchUserButton,botInfoButton)
primaryKeyboard = types.ReplyKeyboardMarkup()
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
        if info[0]==str(message.from_user.id):
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
    await state.update_data(conditionAcc='unremoved')
    data = await state.get_data()
    await message.answer(f"login: {data['nickname']}")
    await message.answer('Регистрация успешно завершена')
    global usersCount
    usersCount +=1
    fUser=open('user.txt','a')
    fUser.write(f"{message.from_user.id} {data['nickname']} {data['password']} {data['status']} {data['conditionAcc']}\n")

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
    data = await state.get_data()
    x=0
    fUser = open('user.txt','r')
    for line in fUser:
        info=line.split()
        if info[1] == data['nickname'] and info[2] == data['password']:
            fUser.close()
            await message.answer('Добро пожаловать',reply_markup=keyboardEnter)
            fUser = open('user.txt','w')
            fUser.write(f"{message.from_user.id} {data['nickname']} {data['password']} {data['status']} {data['conditionAcc']}\n")
            fUser.close()
            break
        else:
            x=x+1
    if x==usersCount:
        await message.answer('Логин или пароль введены неверно')
    await state.finish()






@dp.message_handler(commands=['start','начать'])
async def startCommands(message: types.Message):
    await message.answer('Hello',reply_markup=primaryKeyboard)





if __name__ == '__main__':
    executor.start_polling(dp)