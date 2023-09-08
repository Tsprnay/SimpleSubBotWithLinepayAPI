# Author: https://github.com/Tsprnay
from aiogram import Bot, types, Router, F

from config import subs
from functions.keyboard import payment_link
from functions.payment import create_invoice, order_id_generator
from language import language

router = Router()

@router.callback_query(F.data.startswith("sub_"))
async def callback_handler(query: types.CallbackQuery, bot: Bot):
    sub_number = query.data.split('_')[1]
    sub_price = subs[sub_number]
    order_id_raw = await order_id_generator(query.from_user.id)
    order_id = order_id_raw + f"|{sub_number}|{query.from_user.id}"
    link = await create_invoice(sub_price, order_id)
    await bot.send_message(query.from_user.id, language["invoice_message"].format(amount=sub_price, order_id=order_id_raw), reply_markup=payment_link(link))
