import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage import memory

from settings import config
from tgbot.misc.register_all_services import register_all_services
from tgbot.database.db_sqlite import DataBaseHelper

logger = logging.getLogger(__name__)


async def main():
    logging.basicConfig(
        level=logging.INFO
    )
    logger.info("Starting Bot!")
    conf = config.load_config()

    storage = memory.MemoryStorage()

    bot = Bot(token=conf.tg_bot.token)
    bot["config"] = conf

    dp = Dispatcher(bot, storage=storage)
    await register_all_services(dp)

    try:
        DataBaseHelper().setup_table
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("Bot stopped!")
