"""Some functions for work with redis"""
from core.config import TTL_SECONDS
from core.logger_config import logger
from core.redis_app import redis_app


def put_hset_in_redis(key: str, datas: dict, expire: int = TTL_SECONDS):
    """This updates some datas and put their in redis and then expire TTL
    more info about hset: https://redis.io/commands/hset"""
    for field, value in datas.items():
        redis_app.hset(key, field, value)
    redis_app.expire(key, expire)
    return True


def hdel_from_redis(key: str, datas: list):
    """This Deletes some keys from redis by keys from dict."""
    logger.debug('delete some datas from redis: %s', datas)
    for val in datas:
        redis_app.hdel(key, val)
    return True
