from db.profiles.model import ProfileModel
from db.profiles_watchlist.model import ProfileWatchlistModel
from db.watchlist.model import WatchlistModel
from db.conditions.model import ConditionModel
from playhouse.shortcuts import model_to_dict
import peewee
from peewee import fn
try:
    from bot_v01.misc import logger
except ModuleNotFoundError:
    pass


def is_banned(ban: bool, user_id: int):
    """Проверяет на бан пользователя."""
    if ban:
        return True
    else:
        return False


def compare_user_id_from_db(user: dict, msg: str):
    """Сравнивает есть ли юзер в базе данных или нет."""
    query = ProfileModel.select().where(ProfileModel.user_id == user['id'])
    try:
        q = query.get()
        logger.info(f"User has been found: {q.username}, cmd: {msg}")
        if is_banned(q.is_banned, q.user_id):
            logger.info(f"User has been banned: {q.username}, cmd: {msg}")
            return False
    except peewee.DoesNotExist:
        add_new_user = ProfileModel.create(user_id=user['id'], is_bot=user['is_bot'], first_name=user['first_name'],
                                           username=user['username'], lang_code=user['language_code'])
        logger.info(f"User has been added: {add_new_user.username}, cmd: {msg}")
    return True


def get_watchlist(user_id: int = None):
    """Список нфт отслеживаемые юзером"""
    watchlist: dict = {}
    if user_id is not None:
        query = (WatchlistModel
                 .select(WatchlistModel)
                 .join(ProfileWatchlistModel)
                 .join(ProfileModel)
                 .where(ProfileModel.user_id == user_id))
        logger.debug(f"query: {query.sql()}")
        if len(query) > 0:
            for i in query:
                watchlist[i.name] = i.address
    return watchlist


def all_wl():
    q = WatchlistModel.select(WatchlistModel)
    names = [i.name for i in q]
    return names


def get_information_of_selected_nft(nft_name: str):
    """Возвращает информацию об конкретной нфт"""
    q = (WatchlistModel
         .select(WatchlistModel)
         .where(fn.LOWER(WatchlistModel.name) == nft_name))
    logger.debug(f"query: {q.sql()}")
    return model_to_dict(q.get())


def get_information_of_condition(user_id: int, nft_name: str):
    """Возвращает информацию по условиям конкретного нфт для конкретного юзера"""
    # ConditionModel.gt, ConditionModel.ge, ConditionModel.lt, ConditionModel.le, ConditionModel.eq
    q = (ConditionModel
         .select(ConditionModel)
         .join(WatchlistModel)
         .where(ConditionModel.watchlist_id == WatchlistModel.select(WatchlistModel.id).where(fn.LOWER(WatchlistModel.name) == nft_name))
         .where(ConditionModel.profile_id == ProfileModel.select(ProfileModel.id).where(ProfileModel.user_id == user_id))
         )
    logger.debug(f"query: {q.sql()}")
    return model_to_dict(q.get())


def update_selected_condition(user_id: int, nft_name: str, condition: str, value: str | float):
    """Обновляет выбранное условие по нфт"""
    q = (ConditionModel
         .update({f"{condition}": value})
         .where(ConditionModel.profile_id == ProfileModel.select(ProfileModel.id).where(ProfileModel.user_id == user_id))
         .where(ConditionModel.watchlist_id == WatchlistModel.select(WatchlistModel.id).where(fn.LOWER(WatchlistModel.name) == nft_name))
         )
    return q.execute()


def add_new_user(user_id: int, is_bot: bool, first_name: str, username: str, lang_code: str):
    # {"id":902886808,"is_bot":false,"first_name":"Alex","username":"flipphonebtc","language_code":"en"}
    """Добавляет нового юзера в базу данных"""
    user, created = ProfileModel.get_or_create(user_id=user_id, is_bot=is_bot, first_name=first_name, username=username, lang_code=lang_code)
    logger.info(f"User has been added: {created}")
    return created
