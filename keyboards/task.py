from aiogram import types

addTaskKeyboard = types.InlineKeyboardMarkup(row_width=1)
addTaskButton = types.InlineKeyboardButton(text='Дать задание', callback_data='addTaskButton_click')
addTaskButton_userTask = types.InlineKeyboardButton(text='Дать задание пользователю', callback_data='addTaskButton_userTask_click')
addTaskButton_auction = types.InlineKeyboardButton(text='Выставить задание на аукцион', callback_data='addTaskButton_auction_click')
addTaskBackButton = types.InlineKeyboardButton(text='Назад', callback_data='addTaskBackButton_click')
exitButton = types.InlineKeyboardButton(text='Выход', callback_data='exitButton_click')
addTaskKeyboard.add(addTaskButton_userTask, addTaskButton_auction, addTaskBackButton)

keyboardYesNo = types.InlineKeyboardMarkup(row_width=2)
yesButton = types.InlineKeyboardButton(text='Да', callback_data='yesButton_click')
noButton = types.InlineKeyboardButton(text='Нет', callback_data='noButton_click')
keyboardYesNo.add(yesButton, noButton)

getTaskKeyboard = types.InlineKeyboardMarkup(row_width=1)
getTaskButton = types.InlineKeyboardButton(text='Получить задание', callback_data='getTaskButton_click')
getTaskButton_showRequests = types.InlineKeyboardButton(text='Посмотреть запросы', callback_data='getTaskButton_showRequests_click')
getTaskButton_enqueue = types.InlineKeyboardButton(text='Встать в очередь', callback_data='getTaskButton_enqueue_click')
getTaskBackButton = types.InlineKeyboardButton(text='Назад', callback_data='getTaskBackButton_click')
getTaskKeyboard.add(getTaskButton_showRequests, getTaskButton_enqueue, getTaskBackButton)