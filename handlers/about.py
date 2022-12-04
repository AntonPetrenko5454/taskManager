from aiogram import types, Dispatcher

from keyboards.about import userInfoKeyboard
from controllers.userController import UserController


async def userInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию', reply_markup=userInfoKeyboard)
    await call.answer()


async def historyTaskButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Ваша история задач:'          ''', reply_markup=historyTaskKeyboard''')
    await call.answer()


async def userInfoButtonClick(call: types.CallbackQuery):
    userinfo=UserController.GetUserInfo(call.from_user.id)
    await call.message.edit_text(f"Login: {userinfo[1]} \nPassword: {userinfo[2]} \nФ.И.О: {userinfo[3]} \nTелефон: {userinfo[4]} \nEmail: {userinfo[5]}")
    await call.answer()


async def backUserInfoButtonClick(call: types.CallbackQuery):
    await call.message.edit_text('Тут вы можете посмотреть личную информацию', reply_markup=userInfoKeyboard)
    await call.answer()


def registerHandlersAbout(dp: Dispatcher):
    dp.register_callback_query_handler(userInfoButtonClick, lambda call: call.data == 'userInfoButton_click', state='*')
    dp.register_callback_query_handler(historyTaskButtonClick, lambda call: call.data == 'historyTaskButton_click', state='*')
    dp.register_callback_query_handler(userInfoButtonClick, lambda call: call.data == 'userInfoButton_click', state='*')
    dp.register_callback_query_handler(backUserInfoButtonClick, lambda call: call.data == 'backUserInfoButton_click', state='*')