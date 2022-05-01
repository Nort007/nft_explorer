import asyncio
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


main_naming_buttons = ['NFT menu', 'Exit']
nft_naming_buttons = ['New', 'Edit', 'Delete', 'Back to main menu']


def initial_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for name in main_naming_buttons:
        markup.add(KeyboardButton(text=name))
    return markup


def nft_menu() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    for name in nft_naming_buttons:
        markup.add(KeyboardButton(text=name))
    return markup


def test1() -> ReplyKeyboardMarkup:
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(KeyboardButton(text='test1'))
    return markup
