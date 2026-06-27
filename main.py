"""
Tournament Manager
Main Entry Point
"""

import asyncio
import logging

from aiogram import Bot
from aiogram import Dispatcher

from aiogram.enums import ParseMode
from aiogram.client.default import DefaultBotProperties

from config import BOT_TOKEN

from database.storage import init_db

from handlers.start import router as start_router
from handlers.callbacks import router as callback_router
from handlers.messages import router as message_router


logging.basicConfig(

    level=logging.INFO,

    format="%(asctime)s | %(levelname)s | %(message)s"

)


async def startup(bot: Bot):

    logging.info("Creating database...")

    await init_db()

    me = await bot.get_me()

    logging.info(

        f"Logged in as @{me.username}"

    )

    logging.info(

        "Tournament Manager Started"

    )


async def main():

    bot = Bot(

        token=BOT_TOKEN,

        default=DefaultBotProperties(

            parse_mode=ParseMode.HTML

        )

    )

    dp = Dispatcher()

    dp.include_router(start_router)

    dp.include_router(callback_router)

    dp.include_router(message_router)

    await startup(bot)

    try:

        await dp.start_polling(bot)

    finally:

        await bot.session.close()


if __name__ == "__main__":

    asyncio.run(main())
