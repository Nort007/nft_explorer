from bot_v01.services.service_db import get_watchlist
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot_v01.keyboards.inline.callback_datas import wl_callback


def watchlist_menu(user_id):
    """
    Возвращает список продуктов из списка избранного пользователя
    :param user_id:
    :return:
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    for key, value in get_watchlist(user_id).items():
        cb_action = key.lower().replace(' ', '_')
        keyboard.add(InlineKeyboardButton(text=key, callback_data=wl_callback.new(action=cb_action)))
    return keyboard
