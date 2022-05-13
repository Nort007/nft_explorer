from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot_v01.keyboards.inline.callback_datas import wl_settings_callback, wl_conditions_callback, wl_sub_conditions_callback


def main_settings_menu(nft_name: str):
    """Возвращает клавиатуру настроек пользователя"""
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(InlineKeyboardButton(text='Edit', callback_data=wl_settings_callback.new(action='edit_main_settings_menu', nft=nft_name)))
    return keyboard


def edit_conditions_menu(nft_name: str, conditions: list):
    """Клавиатура изменений условий
    edc - edit_contract; edn - edit_name;
    btmm - back_to_main_menu;"""
    keyboard = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='gt', callback_data=wl_conditions_callback.new(action='gt', nft=nft_name, conditions=conditions)),
                InlineKeyboardButton(text='ge', callback_data=wl_conditions_callback.new(action='ge', nft=nft_name, conditions=conditions)),
                InlineKeyboardButton(text='lt', callback_data=wl_conditions_callback.new(action='lt', nft=nft_name, conditions=conditions)),
                InlineKeyboardButton(text='le', callback_data=wl_conditions_callback.new(action='le', nft=nft_name, conditions=conditions)),
                InlineKeyboardButton(text='eq', callback_data=wl_conditions_callback.new(action='eq', nft=nft_name, conditions=conditions)),
            ],
            [
                InlineKeyboardButton(text='<< Back', callback_data=wl_conditions_callback.new(action='btmm', nft=nft_name, conditions=conditions)),
            ]
        ]
    )
    return keyboard


def edit_sub_conditions_menu(nft_name: str):
    """Кнопка возврата к меню с выбором условий для изменения"""
    keyboard = InlineKeyboardMarkup(
        row_width=1,
        inline_keyboard=[
            [
                InlineKeyboardButton(text='<< Back', callback_data=wl_sub_conditions_callback.new(action='back_to_settings_menu', nft=nft_name)),
            ]
        ]
    )
    return keyboard
