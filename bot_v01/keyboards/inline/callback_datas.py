from aiogram.utils.callback_data import CallbackData


wl_callback = CallbackData('wl', 'action')
wl_settings_callback = CallbackData('wl_settings', 'action', 'nft')
wl_conditions_callback = CallbackData('wl_conditions', 'action', 'nft', 'conditions')
wl_sub_conditions_callback = CallbackData('wl_subconditions', 'action', 'nft')
wl_selected_condition = CallbackData('wl_selected_condition', 'action', 'nft', 'condition')
