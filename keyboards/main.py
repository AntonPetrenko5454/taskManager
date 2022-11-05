from aiogram import types

mainKeyboard = types.InlineKeyboardMarkup(row_width=1)
userInfoButton = types.InlineKeyboardButton(text='Информация о пользователе', callback_data='userInfoButton_click')

mainKeyboard.add( userInfoButton)
