from aiogram import types

keyboardTest = types.InlineKeyboardMarkup(row_width=2)
yes2Button = types.InlineKeyboardButton(text='Да', callback_data='yes2Button_click')
no2Button = types.InlineKeyboardButton(text='Нет', callback_data='no2Button_click')
keyboardTest.add(yes2Button, no2Button)


keyboardTestNo = types.InlineKeyboardMarkup(row_width=1)
readyChangeButton = types.InlineKeyboardButton(text='Готово', callback_data='readyChangeButton_click')
passwordChangeButton = types.InlineKeyboardButton(text='Изменить пароль', callback_data='passwordChangeButton_click')
fIOChangeButton = types.InlineKeyboardButton(text='Изменить Ф.И.О', callback_data='fIOchangeButton_click')
phoneNumberChangeButton = types.InlineKeyboardButton(text='Изменить номер телефона', callback_data='phoneNumberChangeButton_click')
emailChangeButton = types.InlineKeyboardButton(text='Изменить email', callback_data='emailChangeButton_click')
keyboardTestNo.add(passwordChangeButton, fIOChangeButton, phoneNumberChangeButton, emailChangeButton,readyChangeButton)

backButtonToTest = types.InlineKeyboardButton(text='Назад', callback_data='backButtonToTest_click')
passwordChangeKeyboard = types.InlineKeyboardMarkup(row_width=1)

fIOChangeKeyboard = types.InlineKeyboardMarkup(row_width=1)
phoneNumberChangeKeyboard = types.InlineKeyboardMarkup(row_width=1)
emailChangeKeyboard = types.ReplyKeyboardMarkup(row_width=1)
readyPasswordButton = types.InlineKeyboardButton(text='Готово', callback_data='readyPasswordButton_click')

readyFIOButton = types.InlineKeyboardButton(text='Готово', callback_data='readyFIOButton_click')
readyPhoneButton = types.InlineKeyboardButton(text='Готово', callback_data='readyPhoneButton_click')
readyEmailButton = types.InlineKeyboardButton(text='Готово', callback_data='readyEmailButton_click')

passwordChangeKeyboard.add(readyPasswordButton, backButtonToTest)
fIOChangeKeyboard.add(readyFIOButton, backButtonToTest)
phoneNumberChangeKeyboard.add(readyPhoneButton, backButtonToTest)
emailChangeKeyboard.add(readyEmailButton, backButtonToTest)

# ???????????????????????
keyboardReg = types.ReplyKeyboardMarkup()
yesNoInKeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
yesNoInKeyboard.add('Да', 'Нет')