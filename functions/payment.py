# Author: https://github.com/Tsprnay
import hashlib
import string
import random

from config import linepay_id, linepay_secret1

async def order_id_generator(user_id, length=10):
    letters = string.ascii_letters + string.digits
    random_id = ''.join(random.choices(letters, k=length))
    return f"{user_id}[{random_id}]"

async def create_invoice(amount, order_id):
    m_id = linepay_id
    m_secret_1 = linepay_secret1
    amount = amount
    order_id = order_id

    hash_string = f"{m_id}|{m_secret_1}|{amount}|{order_id}"
    hash_value = hashlib.md5(hash_string.encode()).hexdigest()

    link = f"https://linepay.fun/pay?order_id={order_id}&m_id={m_id}&amount={amount}&sign={hash_value}"
    return link
