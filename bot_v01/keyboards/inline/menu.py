from bot_v01.services.service_db import get_watchlist
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot_v01.keyboards.inline.callback_datas import wl_callback, wl_new_nft, wl_callback_del
import peewee


def watchlist_menu(user_id, del_menu: bool = False):
    """
    Возвращает список продуктов из списка избранного пользователя.
    del_menu=True: callback takes name nft and watchlist primary key id.
    del_menu=False: only name by watchlist.
    :param user_id:
    :return:
    """
    keyboard = InlineKeyboardMarkup(row_width=1)
    user_watchlist = get_watchlist(user_id)
    try:
        for watchlist in list(user_watchlist.dicts()):
            cb_action = watchlist['name'].lower().replace(' ', '_')
            if del_menu:
                keyboard.add(
                    InlineKeyboardButton(text=watchlist['name'],
                                         callback_data=wl_callback_del.new(del_action=cb_action, wlid=watchlist['id'])))
            else:
                keyboard.add(InlineKeyboardButton(text=watchlist['name'], callback_data=wl_callback.new(action=cb_action)))
        return keyboard
    except peewee.DoesNotExist:
        return


def new_nft_menu():
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Name', callback_data=wl_new_nft.new(action='name')),
                InlineKeyboardButton(text='Address', callback_data=wl_new_nft.new(action='address')),
            ]
        ]
    )
    return keyboard
