# Author: https://github.com/Tsprnay
import hashlib

from aiogram.types.input_file import FSInputFile
from quart import Quart, request

from config import linepay_id, linepay_secret2, support_username, bot, admin_ids
from language import language

app = Quart(__name__)

@app.route('/payment_notification', methods=['POST'])
async def payment_notification():
    m_id = linepay_id
    m_secret_2 = linepay_secret2

    order_id = (await request.form).get('order_id')
    amount = (await request.form).get('amount')
    sign = (await request.form).get('sign')

    _sign = hashlib.md5(f"{m_id}|{m_secret_2}|{amount}|{order_id}".encode()).hexdigest()

    async def getIP():
        if 'HTTP_X_REAL_IP' in request.headers:
            return request.headers['HTTP_X_REAL_IP']
        return request.remote_addr

    allowed_ips = ['45.142.122.86', '92.255.111.15']
    if await getIP() not in allowed_ips:
        return "wrong ip"

    if sign != _sign:
        return "wrong sign"

    file = FSInputFile(path="file/Tokens.apk")

    order_id_raw, sub_number, user_id = order_id.split('|')
    for id in admin_ids:
        await bot.send_message(id, language['admin_successfully_message'].format(amount=amount, user_id=user_id, sub_number=sub_number), parse_mode='HTML')
    await bot.send_document(user_id,document=file, caption=language[f'user_successfully_message_{sub_number}'].format(support=support_username), parse_mode='HTML')
    return "Payment processed successfully"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4480)
