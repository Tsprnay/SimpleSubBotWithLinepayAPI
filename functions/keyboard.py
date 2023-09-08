# Author: https://github.com/Tsprnay
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

from language import language

def start_button() -> ReplyKeyboardMarkup:
    keyboard = ReplyKeyboardBuilder()
    keyboard.button(text=language["start_button"])
    #keyboard.adjust(2)
    return keyboard.as_markup(resize_keyboard=True)

def choose_sub():
    buttons = [
        [
            types.InlineKeyboardButton(text=language["sub1_button"], callback_data="sub_1"),
            types.InlineKeyboardButton(text=language["sub2_button"], callback_data="sub_2"),
            types.InlineKeyboardButton(text=language["sub3_button"], callback_data="sub_3")
        ],
        [
            types.InlineKeyboardButton(text=language["sub4_button"], callback_data="sub_4"),
            types.InlineKeyboardButton(text=language["sub5_button"], callback_data="sub_5")
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard

def payment_link(link):
    buttons = [
        [
            types.InlineKeyboardButton(text="💳 Оплатить", url=link)
        ]
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=buttons)
    return keyboard
