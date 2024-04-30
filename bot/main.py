import asyncio
import logging

import aiogram.exceptions
from aiogram import Bot
from aiogram.dispatcher.dispatcher import Dispatcher
from config import settings
from handlers.task import tasks_router
bot = Bot(token=settings.TOKEN)
dp = Dispatcher()


async def main():
    dp.include_routers(tasks_router)
    try:
        await bot.delete_webhook()
        await dp.start_polling(bot, skip_updates=True)
    except aiogram.exceptions.TelegramNetworkError as e:
        logging.error(e)
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(main())
