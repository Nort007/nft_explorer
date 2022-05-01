from aiogram import types
from .keyboards import initial_menu
from bot.services.service_db import compare_user_id_from_db


async def start_command(message: types.Message):
    if compare_user_id_from_db(dict(message.from_user), msg=message.text):
        await message.reply('Initial start', reply_markup=initial_menu())
