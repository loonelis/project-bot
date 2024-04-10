import asyncio
import logging
from aiogram.enums.parse_mode import ParseMode
from aiogram import Bot, Dispatcher
from app.database.models import async_main
from app.handlers import router
from app.ADMIN import admin

from config import TOKEN
async def main():
    await async_main()
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(admin, router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)



if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')