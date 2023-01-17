import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import BotCommand
from config import TOKEN
from handlers import about, enter, primary, registration


async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()

    dp.include_router(about.router)
    dp.include_router(enter.router)
    dp.include_router(primary.router)
    dp.include_router(registration.router)

    await bot.set_my_commands([BotCommand(command='start', description='Старт')])
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == '__main__':
    asyncio.run(main())
