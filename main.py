
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import ContentType
from aiogram.utils import executor
from config import TOKEN
from user import User
from registrationState import RegistrationState

bot = Bot(token=TOKEN)
dp = Dispatcher(bot,storage=MemoryStorage())
##users=[]

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
   await message.answer('Введите nickname')

   await RegistrationState.nickname.set()


@dp.message_handler(state=RegistrationState.nickname)
async def getNickname(message: types.Message,state: FSMContext):
    await state.update_data(nickname= message.text)
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
    await state.update_data(password= message.text)
    data = await state.get_data()
    await message.answer(f"login: {data['nickname']}")
    await message.answer('Регистрация успешно завершена')
    global usersCount
    usersCount +=1
    fUser=open('user.txt','a')
    fUser.write(f"{usersCount} {data['nickname']} {data['password']}\n")

    fUser.close()
    await state.finish()


@dp.message_handler(commands=['start','начать'])
async def startCommands(message: types.Message):
    await message.answer('Hello',reply_markup=primaryKeyboard)





if __name__ == '__main__':
    executor.start_polling(dp)