from aiogram import types

userInfoButton = types.InlineKeyboardButton(text='Информация о пользователе', callback_data='userInfoButton_click')

addTaskButton = types.InlineKeyboardButton(text='Создать задачу', callback_data='addTaskButton_click')
getTaskButton = types.InlineKeyboardButton(text='Посмотреть заявки', callback_data='getTaskButton_click')
botInfoButton = types.InlineKeyboardButton(text='Информация о боте', callback_data='botInfoButton_click')

mainKeyboard = types.InlineKeyboardMarkup(inline_keyboard=[[addTaskButton],[getTaskButton],[userInfoButton],[botInfoButton]])