from aiogram import types

backToMainButton = types.InlineKeyboardButton(text='Назад', callback_data='backUserInfoButton_click')
myTaskInfoButton = types.InlineKeyboardButton(text='Мои задачи', callback_data='myTaskInfoButton_click')
changeUserInfoButton = types.InlineKeyboardButton(text='Изменить свои данные', callback_data='changeUserInfoButton_click')

userInfoKeyboard = types.InlineKeyboardMarkup(inline_keyboard=[[myTaskInfoButton], [changeUserInfoButton], [backToMainButton]])
