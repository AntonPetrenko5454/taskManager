from aiogram import types, Dispatcher, Router
from aiogram.filters import Text

from controllers.task_controller import TaskController
from keyboards.about import userInfoKeyboard
from controllers.user_controller import UserController
from keyboards.main import mainKeyboard

router = Router()



'''@router.callback_query(Text(text="changeUserInfoButton_click"))
async def changeUserInfoButtonClick(call: types.CallbackQuery):'''


@router.callback_query(Text(text='myTaskInfoButton_click'))
async def my_tasks_button_click(call: types.CallbackQuery):
    mas=TaskController.find_user_tasks(call.from_user.id)
    tasks=[]
    n=0
    for i in range(len(mas)):
        for y in range(i):
            tasks.append(mas[i][y])
        n=n+1
        await call.message.answer(f"Ваша задача номер {n}\nКритерии:{str(mas[i][12])}\nНазвание:{str(mas[i][1])}\nЦель:{str(mas[i][9])}\nДата:{str(mas[i][4])}\nАдрес:{str(mas[i][7])}\nЦена:{str(mas[i][5])}")



@router.callback_query(Text(text="userInfoButton_click"))
async def userInfoButtonClick(call: types.CallbackQuery):
    userinfo=UserController.GetUserInfo(call.from_user.id)
    await call.message.edit_text(f"Login: {userinfo[1]} \nPassword: {userinfo[2]} \nФ.И.О: {userinfo[3]} \nTелефон: {userinfo[4]} \nEmail: {userinfo[5]}",reply_markup=userInfoKeyboard)
    await call.answer()


@router.callback_query(Text(text="backUserInfoButton_click"))
async def backUserInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Добро пожаловать', reply_markup=mainKeyboard)
    await call.answer()
