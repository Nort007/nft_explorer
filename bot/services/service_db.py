from db.profiles.model import ProfileModel
import asyncio
import json
import peewee
from bot.misc import logger


def compare_user_id_from_db(user: dict, msg: str):
    """Сравнивает есть ли юзер в базе данных или нет."""
    query = ProfileModel.select().where(ProfileModel.user_id == user['id'])
    try:
        q = query.get()
        logger.info(f"User has been found: {q.username}, cmd: {msg}")
    except peewee.DoesNotExist:
        add_new_user = ProfileModel.create(user_id=user['id'], is_bot=user['is_bot'], first_name=user['first_name'],
                                           username=user['username'], lang_code=user['language_code'])
        logger.info(f"User has been added: {add_new_user.username}, cmd: {msg}")
    return True
