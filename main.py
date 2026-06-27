"""
Tournament Manager
Main entry point
"""

import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config import BOT_TOKEN
from database.storage import init_db

# Routers
from handlers.start import router as start_router
from handlers.callbacks import router as callback_router
from handlers.messages import router as message_router


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s"
)


async def on_startup(bot: Bot):

    logging.info("Initializing database...")

    await init_db()

    bot_info = await bot.get_me()

    logging.info(
        f"Logged in as @{bot_info.username}"
    )

    logging.info("Tournament Manager started successfully.")


async def main():

    bot = Bot(
        token=BOT_TOKEN,
        default=DefaultBotProperties(
            parse_mode=ParseMode.HTML
        )
    )

    dp = Dispatcher()

    # Register routers
    dp.include_router(start_router)
    dp.include_router(callback_router)
    dp.include_router(message_router)

    await on_startup(bot)

    try:
        await dp.start_polling(bot)

    finally:
        await bot.session.close()


if __name__ == "__main__":

    try:
        asyncio.run(main())

    except KeyboardInterrupt:
        logging.info("Bot stopped.")
