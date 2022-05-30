from db.profiles.model import ProfileModel
from db.profiles_watchlist.model import ProfileWatchlistModel
from db.watchlist.model import WatchlistModel
from db.conditions.model import ConditionModel
from playhouse.shortcuts import model_to_dict
import peewee
from peewee import fn
from bot_v01.misc import logger
from db.base.base_model import psql_db
from db.mailing.model import MailingModel


@psql_db.atomic()
def add_or_update_mailing(public_channel: str = None, chat_id: int = None, active: bool = False, user_pk_id: int = None):
    try:
        if chat_id is None:
            q = MailingModel.create(public_channel=public_channel, active=active, profile_id=user_pk_id)
        elif chat_id is not None:
            q = MailingModel.create(chat_id=chat_id, active=active, profile_id=user_pk_id)
        elif public_channel is None and chat_id is None:
            return False
        else:
            return False
    except peewee.IntegrityError as e:
        print(e)
        psql_db.rollback()
        if chat_id is None:
            q = MailingModel.update(public_channel=public_channel, active=active).where(MailingModel.profile_id == user_pk_id).execute()
        elif chat_id is not None:
            q = MailingModel.update(chat_id=chat_id, active=active).where(MailingModel.profile_id == user_pk_id).execute()
        else:
            return False
    return q


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


def query_option(option: str):
    """В частом случае функция возвращает опции из /newnft когда юзер добавляет коллекцию себе по адресу или имени.
    Возвращает в основном для where в запросе к базе данных."""
    if option == 'name':
        return WatchlistModel.name
    elif option == 'address':
        return WatchlistModel.address
    else:
        logger.error(f"Option '{option}' is not supported")
        raise ValueError(f"Option '{option}' is not supported")


def get_watchlist(user_id: int = None, option: str = None, value: str = None):
    """Список нфт отслеживаемые юзером, если нет параметров, то все коллекции отслеживаемые юзером."""
    watchlist: dict = {}
    if user_id is not None:
        query = (WatchlistModel
                 .select(WatchlistModel)
                 .join(ProfileWatchlistModel)
                 .join(ProfileModel)
                 .where(ProfileModel.user_id == user_id)
                 )
        # logger.debug(f"query: {query.sql()}")
        # if len(query) > 0:
        #     for i in query:
        #         watchlist[i.name] = i.address
    return query


def select_chosen_collection_by_user(user_id: int = None, option: str = None, value: str = None):
    """Возвращает все или конкретную коллекцию отслеживаемые юзером."""
    # where_option = query_option(option)
    if option == 'name':
        where_join = (fn.LOWER(WatchlistModel.name) == value.lower()) | (fn.LOWER(WatchlistModel.slug) == value.lower())
    elif option == 'address':
        where_join = WatchlistModel.address == value
    else:
        return
    q = (WatchlistModel
         .select(WatchlistModel, ProfileWatchlistModel, ProfileModel)
         .join(ProfileWatchlistModel, on=(ProfileWatchlistModel.watchlist_id == WatchlistModel.id))
         .join(ProfileModel, on=(ProfileModel.id == ProfileWatchlistModel.profile_id)).where(ProfileModel.user_id == user_id)
         .where(where_join)
         )
    logger.debug(f"query: {q.sql()}")
    return q


def add_new_bind_to_profiles_watchlist():
    pass


def all_wl():
    q = WatchlistModel.select(WatchlistModel)
    names = [i.name for i in q]
    return names


def get_information_of_selected_nft(value: str, option: str = 'name'):
    """Возвращает информацию об конкретной нфт"""
    # where_option = query_option(option)
    if option == 'name':
        where_option = (fn.LOWER(WatchlistModel.name) == value) | (fn.LOWER(WatchlistModel.slug) == value)
    elif option == 'address':
        where_option = WatchlistModel.address == value
    else:
        return
    q = (WatchlistModel
         .select(WatchlistModel)
         .where(where_option)
         )
    logger.debug(f"query: {q.sql()}")
    return q


def add_new_nft_collection(name: str = None, address: str = None, slug: str = None):
    """Добавляет новую коллекцию нфт"""
    add_new_collection = WatchlistModel.create(name=name, address=address, slug=slug)
    logger.info(f"Collection {add_new_collection.name} has been added")
    return {'id': add_new_collection.id, 'name': add_new_collection.name, 'address': add_new_collection.address}


def get_information_of_condition(user_id: int, nft_wl_id: int):
    """Возвращает информацию по условиям конкретного нфт для конкретного юзера"""
    # ConditionModel.gt, ConditionModel.ge, ConditionModel.lt, ConditionModel.le, ConditionModel.eq
    q = (ConditionModel
         .select(ConditionModel)
         .join(WatchlistModel)
         .where(ConditionModel.watchlist_id == WatchlistModel.select(WatchlistModel.id).where(WatchlistModel.id == nft_wl_id))
         .where(ConditionModel.profile_id == ProfileModel.select(ProfileModel.id).where(ProfileModel.user_id == user_id))
         )
    logger.debug(f"query: {q.sql()}")
    return q


def create_new_condition(user_pk_id: int, wl_pk_id: int):
    return ConditionModel.create(profile_id=user_pk_id, watchlist_id=wl_pk_id)


def update_selected_condition(user_pk: int, nft_pk: int, condition: str, value: str | float):
    """Обновляет выбранное условие по нфт"""
    q = (ConditionModel
         .update({f"{condition}": value})
         .where(ConditionModel.profile_id == user_pk)
         .where(ConditionModel.watchlist_id == nft_pk))
    return q.execute()


def add_new_user(user_id: int, is_bot: bool, first_name: str, username: str, lang_code: str):
    # {"id":902886808,"is_bot":false,"first_name":"Alex","username":"flipphonebtc","language_code":"en"}
    """Добавляет нового юзера в базу данных"""
    user, created = ProfileModel.get_or_create(user_id=user_id, is_bot=is_bot, first_name=first_name, username=username, lang_code=lang_code)
    logger.info(f"User has been added: {created}")
    return created


def get_user_information(user_id: int = None):
    return ProfileModel.select(ProfileModel).where(ProfileModel.user_id == user_id)


def add_new_profiles_watchlist(user_pk_id: int, wl_id: int):
    return ProfileWatchlistModel.create(profile_id=user_pk_id, watchlist_id=wl_id)


def del_from_profiles_watchlist(user_id: int, wl_pk_id: int):
    # query = (ProfileWatchlistModel
    #          .delete()
    #          .join(ProfileModel)
    #          .where(ProfileWatchlistModel.profile_id == user_id, ProfileWatchlistModel.watchlist_id == wl_pk_id))
    # return query.execute()
    query = (ProfileWatchlistModel
             .delete()
             .where(ProfileWatchlistModel.watchlist_id == wl_pk_id)
             .where(ProfileWatchlistModel.profile_id == ProfileModel.select(ProfileModel.id).where(ProfileModel.user_id == user_id))
             )
    return query.execute()

# test = del_from_profiles_watchlist(user_id=902886808, wl_pk_id=9)
# print(test)
