# main.py

import asyncio

from aiogram import Bot
from aiogram import Dispatcher

from config import BOT_TOKEN

# Routers
from handlers.start import router as start_router


async def main():

    bot = Bot(BOT_TOKEN)

    dp = Dispatcher()

    # Register Routers
    dp.include_router(start_router)

    print("Tournament Manager is running...")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
