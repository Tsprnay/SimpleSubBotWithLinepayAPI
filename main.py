import asyncio
import logging
from handlers import start_handler, text_handler, callback_handler
from config import bot, dp
from aiogram import types
from aiogram import Router, F
import subprocess

logging.basicConfig(level=logging.INFO)

async def main():
    dp.include_routers(start_handler.router, text_handler.router, callback_handler.router)

    subprocess.Popen(['python', 'functions/payment_router.py'])

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logging.info("Боты остановлены")
