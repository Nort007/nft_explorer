from bot_v01.services.service_db import get_information_of_condition


def condition_data(user_id: int, nft_name: str):
    """This function returns the preprared condition data."""
    condition_data = get_information_of_condition(user_id, nft_name)
    list_of_conditions = ['gt', 'ge', 'lt', 'le', 'eq']
    for k, v in condition_data.items():
        if k in list_of_conditions:
            if condition_data[k] == -1:
                condition_data[k] = None
    return condition_data
