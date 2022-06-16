"""Celery basic functions. It's reduce await time."""
import asyncio

from api.services.service_redis import put_hset_in_redis
from api.services.service_tg import send_message
from core.celery_app import celery_app
from core.logger_config import logger


@celery_app.task(acks_late=True)
def send_code(username: str, user_id: int, code: int | str):
    """This function implements the sending of the code by celery."""
    logger.debug('sending:message: username, user_id, code: %s %s %s', username, user_id, code)
    asyncio.run(send_message(chat_id=user_id, msg=code))


@celery_app.task(acks_late=True)
def celery_put_in_redis(key: str, datas: dict, expire: bool):
    """This function implements the putting of the data in redis by celery."""
    return put_hset_in_redis(key=key, datas=datas, expire=expire)
