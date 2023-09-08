# Author: https://github.com/Tsprnay
from aiogram import Bot, types, Router
from aiogram.filters import Command

from functions.keyboard import start_button
from language import language

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, language["start_message"], reply_markup=start_button())
