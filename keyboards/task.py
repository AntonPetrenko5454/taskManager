from aiogram import types

addTaskKeyboard = types.InlineKeyboardMarkup(row_width=1)


addTaskFirstStageKeyboard = types.InlineKeyboardMarkup()
addTaskCheckKeyboard= types.InlineKeyboardMarkup(row_width=1)
addTaskYesButton= types.InlineKeyboardButton(text='Да', callback_data='addTaskYesButton_click')
addTaskNoButton= types.InlineKeyboardButton(text='Нет', callback_data='addTaskNoButton_click')
addTaskCheckKeyboard.add(addTaskYesButton,addTaskNoButton)
getTaskKeyboard = types.InlineKeyboardMarkup(row_width=1)
getTaskButton = types.InlineKeyboardButton(text='Получить задание', callback_data='getTaskButton_click')



