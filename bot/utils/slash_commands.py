from aiogram import types
from .keyboards import initial_menu
from bot.services.check_user_id import compare_user_id_from_db


async def start_command(message: types.Message):
    print(message.from_user.values['id'])
    if compare_user_id_from_db(message.from_user.values['id']) is True:
        await message.reply('Initial start', reply_markup=initial_menu())
