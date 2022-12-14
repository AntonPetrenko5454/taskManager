import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import BotCommand

from config import TOKEN
from handlers.about import registerHandlersAbout
from handlers.enter import registerHandlersEnter
from handlers.primary import registerHandlersCommon
from handlers.registration import registerHandlersRegistration
from handlers.task import registerHandlersTask

currentUsers = {}


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    registerHandlersEnter(dp)
    registerHandlersAbout(dp)
    registerHandlersTask(dp)
    registerHandlersRegistration(dp)
    registerHandlersCommon(dp)

    await bot.set_my_commands([BotCommand(command='start', description='Старт')])

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
