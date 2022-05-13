from aiogram import Dispatcher
from .my_watchlist import watchlist_command
from .purchase import (selected_nft, edit_selected_nft, edit_selected_conditions, ConditionState, check_valid_condition)
from .purchases_new_nft import new_nft_to_watchlist


def setup(dp: Dispatcher):
    dp.register_message_handler(watchlist_command, commands=['mywatchlist'])
    dp.register_message_handler(check_valid_condition, state=ConditionState.value_of_condition)
    dp.register_callback_query_handler(callback=edit_selected_nft, text_contains='back_to_settings_menu')
    dp.register_callback_query_handler(callback=edit_selected_nft, text_contains='edit_main_settings_menu')
    dp.register_callback_query_handler(callback=watchlist_command, text_contains='btmm')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='gt')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='ge')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='lt')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='le')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='eq')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='edc')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='edn')
    dp.register_callback_query_handler(callback=selected_nft)


def setup_purchases_new_nft(dp: Dispatcher):
    dp.register_message_handler(new_nft_to_watchlist, commands=['newnft'])
