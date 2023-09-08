# Author: https://github.com/Tsprnay
from aiogram import Bot, types, Router, F

from functions.keyboard import choose_sub
from language import language

router = Router()

@router.message(F.text == language["start_button"])
async def text_handler(message: types.Message, bot: Bot):
    await bot.send_message(message.from_user.id, language["choose_sub_message"], reply_markup=choose_sub())
