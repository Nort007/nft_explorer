import time

from .service_db import get_information_of_condition, create_new_condition, get_user_information


def condition_data(user_id: int, wl_pk_id: int):
    """This function returns the preprared condition data."""
    condition_data = list(get_information_of_condition(user_id, wl_pk_id).dicts())
    if len(condition_data) == 0:
        user = get_user_information(user_id).get()
        create_new_condition(user.id, wl_pk_id)
        condition_data = list(get_information_of_condition(user_id, wl_pk_id).dicts())
    return condition_data[0]


def get_nft_name(values: dict, cb_user: str) -> dict:
    """This function returns the name of the NFT."""
    for i in values['message']['reply_markup']['inline_keyboard']:
        if i[0]['callback_data'] == cb_user:
            return {'original': i[0]['text'], 'from_callback': i[0]['callback_data'].split(':')[1]}
