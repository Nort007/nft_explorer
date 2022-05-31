from bot_v01.services import get_mailing, get_watchlist, disclosure_fully_infromation_of_users
import collections


def all_channels_groups() -> dict:
    """
    Получение всех групп и каналов пользователей и сортировка их.
    :return:
    """
    gc_dict = {}
    datas = disclosure_fully_infromation_of_users().dicts()
    for data in datas:
        print(data)
    return gc_dict


all_channels_groups()
