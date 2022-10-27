import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import TOKEN
from handlers.about import registerHandlersAbout
from handlers.enter import registerHandlersEnter
from handlers.task import registerHandlersTask

currentUsers = {}


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher(bot, storage=MemoryStorage())

    registerHandlersEnter(dp)
    registerHandlersAbout(dp)
    registerHandlersTask(dp)

    await dp.start_polling()


if __name__ == '__main__':
    asyncio.run(main())
