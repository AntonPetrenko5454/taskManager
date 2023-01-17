from aiogram import types

userInfoButton = types.InlineKeyboardButton(text='Информация о пользователе', callback_data='userInfoButton_click')
mainKeyboard = types.InlineKeyboardMarkup(inline_keyboard=[[userInfoButton]])
