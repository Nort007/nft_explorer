from aiogram import Dispatcher

from .my_watchlist import watchlist_command
from .purchase import (selected_nft, edit_selected_nft, edit_selected_conditions, ConditionState, check_valid_condition)
from .purchases_add_group_channel import user_channel_group, user_channel_group_handler, GrouChannelState
from .purchases_del_nft import del_user_nft
from .purchases_new_nft import new_nft_to_watchlist, NFTState, choosen_option, search_option


def setup(dp: Dispatcher):
    dp.register_message_handler(watchlist_command, commands=['mywatchlist'])
    dp.register_message_handler(check_valid_condition, state=ConditionState.value_of_condition)
    dp.register_callback_query_handler(callback=edit_selected_nft, text_contains='back_to_settings_menu')
    dp.register_callback_query_handler(callback=edit_selected_nft, text_contains='edit_main_settings_menu')
    dp.register_callback_query_handler(callback=watchlist_command, text_contains='btmm')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='gt:')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='ge:')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='lt:')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='le:')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='eq:')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='edc:')
    dp.register_callback_query_handler(callback=edit_selected_conditions, text_contains='edn:')
    dp.register_callback_query_handler(callback=selected_nft, text_contains='wl')


def setup_purchases_new_nft(dp: Dispatcher):
    dp.register_message_handler(search_option, commands=['newnft'])
    dp.register_message_handler(new_nft_to_watchlist, state=NFTState.name_or_address)
    dp.register_callback_query_handler(callback=choosen_option, text_contains='name')
    dp.register_callback_query_handler(callback=choosen_option, text_contains='address')


def setup_delnft(dp: Dispatcher):
    dp.register_message_handler(watchlist_command, commands=['delnft'])
    dp.register_callback_query_handler(callback=del_user_nft, text_contains='del')


def setup_add_group_channel(dp: Dispatcher):
    dp.register_message_handler(user_channel_group, commands=['addgc'])
    dp.register_message_handler(callback=user_channel_group_handler, state=GrouChannelState.group_or_channel)
