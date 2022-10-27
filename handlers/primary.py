from aiogram import types, Dispatcher
from keyboards.primary import primaryKeyboard


async def startCommand(message: types.Message):
    await message.answer('Войдите в аккаунт или зарегестрируйтесь', reply_markup=primaryKeyboard)


def registerHandlersCommon(dp: Dispatcher):
    dp.register_message_handler(startCommand, commands=['start'], state="*")
