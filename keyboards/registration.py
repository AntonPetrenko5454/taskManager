from aiogram import types

yesButton = types.InlineKeyboardButton(text='Да', callback_data='yesButton_click')
noButton = types.InlineKeyboardButton(text='Нет', callback_data='noButton_click')
yesNoKeyboard = types.InlineKeyboardMarkup(inline_keyboard=[[yesButton, noButton]])

passwordChangeButton = types.InlineKeyboardButton(text='Изменить пароль', callback_data='passwordChangeButton_click')
fIOChangeButton = types.InlineKeyboardButton(text='Изменить Ф.И.О', callback_data='fIOchangeButton_click')
phoneNumberChangeButton = types.InlineKeyboardButton(text='Изменить номер телефона', callback_data='phoneNumberChangeButton_click')
emailChangeButton = types.InlineKeyboardButton(text='Изменить email', callback_data='emailChangeButton_click')
readyChangeButton = types.InlineKeyboardButton(text='Готово', callback_data='readyChangeButton_click')
editFieldskeyboard = types.InlineKeyboardMarkup(
    inline_keyboard=[[passwordChangeButton, fIOChangeButton, phoneNumberChangeButton, emailChangeButton, readyChangeButton]])