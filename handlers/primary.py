from aiogram import types, Router
from aiogram.filters import Command
from keyboards.primary import primaryKeyboard

router = Router()


# TODO: commands_prefix - эксперимент
@router.message(Command(commands=['start']))
async def startCommand(message: types.Message):
    await message.answer('Войдите в аккаунт или зарегестрируйтесь', reply_markup=primaryKeyboard)
