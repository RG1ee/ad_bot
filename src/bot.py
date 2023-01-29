import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage import memory

from settings.const import token
from handlers.echo import register_echo
from handlers.start import register_start_message

logger = logging.getLogger(__name__)


def register_all_handlers(dp: Dispatcher):
    
    register_start_message(dp)
    register_echo(dp)
    

async def main():
    logging.basicConfig(
        level=logging.INFO
    )
    logger.info("bot start")

    storage = memory.MemoryStorage()

    bot = Bot(token)
    dp = Dispatcher(bot, storage=storage)

    register_all_handlers(dp)

    try:
        await dp.start_polling()
    finally:
        await dp.storage.close()
        await dp.storage.wait_closed()
        await bot.session.close()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logger.error("bot stop")