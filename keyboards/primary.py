from aiogram import types

# TODO: input_field_placeholder проверить как работает
primaryKeyboard = types.ReplyKeyboardMarkup(keyboard=[[types.KeyboardButton(text='Регистрация')],
                                                      [types.KeyboardButton(text='Вход')]],
                                            resize_keyboard=True, input_field_placeholder='Выберите действие')
