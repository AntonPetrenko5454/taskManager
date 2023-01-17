from aiogram import types, Dispatcher, Router
from aiogram.filters import Text

from keyboards.about import userInfoKeyboard
from controllers.user_controller import UserController

router = Router()


@router.callback_query(Text(text="userInfoButton_click"))
async def userInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию', reply_markup=userInfoKeyboard)
    await call.answer()


@router.callback_query(Text(text="historyTaskButton_click"))
async def historyTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Ваша история задач:'          ''', reply_markup=historyTaskKeyboard''')
    await call.answer()


@router.callback_query(Text(text="userInfoButton_click"))
async def userInfoButtonClick(call: types.CallbackQuery):
    userinfo=UserController.GetUserInfo(call.from_user.id)
    await call.message.edit_text(f"Login: {userinfo[1]} \nPassword: {userinfo[2]} \nФ.И.О: {userinfo[3]} \nTелефон: {userinfo[4]} \nEmail: {userinfo[5]}")
    await call.answer()


@router.callback_query(Text(text="backUserInfoButton_click"))
async def backUserInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию', reply_markup=userInfoKeyboard)
    await call.answer()
