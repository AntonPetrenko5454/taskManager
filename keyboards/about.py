from aiogram import types

backToMainButton = types.InlineKeyboardButton(text='Назад', callback_data='backUserInfoButton_click')
historyTaskButton = types.InlineKeyboardButton(text='История задач', callback_data='historyTaskButton_click')
changeUserInfoButton = types.InlineKeyboardButton(text='Ваши данные', callback_data='userInfoButton_click')
userInfoKeyboard = types.InlineKeyboardMarkup(inline_keyboard=[[historyTaskButton], [changeUserInfoButton], [backToMainButton]])
