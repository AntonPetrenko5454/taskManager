from aiogram import types

addTaskYesButton = types.InlineKeyboardButton(text='Да', callback_data='addTaskYesButton_click')
addTaskNoButton = types.InlineKeyboardButton(text='Нет', callback_data='addTaskNoButton_click')
addTaskKeyboard = types.InlineKeyboardMarkup(inline_keyboard=[[addTaskYesButton], [addTaskNoButton]])
