# Author: https://github.com/Tsprnay
import os

from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')

linepay_id = os.getenv('LINEPAY_ID')
linepay_secret1 = os.getenv('LINEPAY_SECRET1')
linepay_secret2 = os.getenv('LINEPAY_SECRET2')

admin_ids = [401914972, 1113265912]
support_username = os.getenv('SUPPORT_USERNAME')

bot = Bot(token=token)
dp = Dispatcher(storage=MemoryStorage())

subs = {
    "1": "120",
    "2": "200",
    "3": "360",
    "4": "500",
    "5": "620",
}
