from playhouse.shortcuts import model_to_dict

from bot_v01.misc import logger
from gem import information_by_name, gem_collection as gem_collection_by_address
from .service_db import (get_information_of_selected_nft, add_new_nft_collection, get_user_information, add_new_profiles_watchlist,
                         select_chosen_collection_by_user)


def bind_nft_to_user(*params, user_id):
    """Получает информацию по коллекции, если она есть то привязывает к юзеру,
    если нет то добавляет в общий список и привязывает к юзеру."""
    params = params[0]
    datas = {'profiles_watchlist': None, 'name_collection': None, 'user_pk_id': None, 'wl_id': None}
    info_of_selected_nft = get_information_of_selected_nft(option=params['option'], value=params['name_or_address'].lower())
    logger.debug(f"found amount by params: {info_of_selected_nft.count()}")
    user_info = get_user_information(user_id=user_id).get()
    if info_of_selected_nft.count() == 1:
        disclosure_information = model_to_dict(info_of_selected_nft.get())  # about nft
        logger.debug(f'output: {disclosure_information}')
        if select_chosen_collection_by_user(user_id=user_id, option=params['option'], value=params['name_or_address']).count() == 0:
            datas.update(name_collection=disclosure_information['name'], user_pk_id=user_info, wl_id=disclosure_information['id'])
        else:
            datas.update(name_collection=disclosure_information['name'])
    else:
        """Добавляет тут коллекцию т.к. ее нет."""
        if params['option'] == 'name':
            response_by_name = information_by_name(name=params['name_or_address'])
            if response_by_name is False:
                return 'Collection not found, try again.'
            else:
                new_collection = add_new_nft_collection(name=response_by_name['name'], slug=response_by_name['slug'])
                datas.update(name_collection=new_collection['name'])
        else:
            response_by_address = gem_collection_by_address(addr=params['name_or_address'])
            if response_by_address is False:
                return 'Collection not found, try again.'
            else:
                new_collection = add_new_nft_collection(name=response_by_address['name'], address=response_by_address['address'],
                                                        slug=response_by_address['slug'])
                datas.update(name_collection=new_collection['name'])
        datas.update(user_pk_id=user_info, wl_id=new_collection['id'])
    if datas['user_pk_id'] is not None:
        new_profiles_watchlist = add_new_profiles_watchlist(user_pk_id=datas['user_pk_id'], wl_id=datas['wl_id'])
    return {'text': f"{datas['name_collection']} has been added."}
